# Peer review - Round 1

Editors:
- Frederik Graw, https://ror.org/038t36y30 Heidelberg University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75427.sa0](https://doi.org/10.7554/eLife.75427.sa0)

This work should be of interest to a broad readership in infectious diseases, especially those people interested in modeling of infections. It combines statistical and mechanistic modeling to find assayable correlates of immunity for vaccines. This method could be relevant to many diseases or vaccines, although the particular markers identified here likely will be limited in their generalizability.


---

# Peer review - Round 1

Editors:
- Frederik Graw, https://ror.org/038t36y30 Heidelberg University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75427.sa1](https://doi.org/10.7554/eLife.75427.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "SARS-CoV-2 mechanistic correlates of protection: insight from modelling response to vaccines" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The reviewers appreciated the developed approach and analyses, but had several concerns regarding the robustness of the methods and estimates, as well as the conclusions drawn from it. In particular, they identified the following main points that would need to be addressed in order to advance the study:

Essential revisions:

(1) A more detailed explanation of the used methods. This especially applies to the selection of biomarkers, as well as addressing the potential risk of overfitting in case of the mechanistic model.

(2) A revision of the title to specify that the analysis is limited to non-human primates in the light of the specific comments by the reviewers below.

(3) A more detailed discussion of the limitations of the study and reconsideration of the conclusions with regard to the interpretability of the non-human data for the human situation and possible caveats in the analysis. An inclusion of human data sets as suggested by reviewer 2 is not necessarily warranted. But a more detailed/extended discussion of the literature on correlates of protection should be included. Please also have a look at the detailed suggestions and links provided by reviewer 2.

We would welcome a substantially revised version of the manuscript addressing all of the issues mentioned by the reviewers. Please also see the detailed suggestions that are made by the reviewers below, and we hope you will find them helpful in this regard.

Reviewer #1 (Recommendations for the authors):

The model used seems adequate, but there are several modeling options that could be better justified. This would help the reader understand the modeling approach better. In some cases, this is simply a case of explaining earlier why you are making the choice that you make. For example, why do you model infection and non-infectious virus (Line 119)? I think this is to fit both virus and infected cells, but this is not clear when you present this choice, which then makes it a little unclear in line 124 when you say that sgRNA is proportional to infected cells. Again, why this choice? Wouldn't it also be reasonable to consider gRNA plus sgRNA to be proportional to infected cells? Another modeling choice that could be better explained is why you consider the inoculum virus separately (its own compartment and its own clearance rate)? In Line 401 you say, "to be able to distinguish", but why is that needed?

When you describe the model in the Results section, it would also be important to say something about the coupling of URT and trachea – this is only at the end of the model description in the Methods, but since you mention the two compartments in the results, the reader (who may not read the Methods first) may be confused.

Some more questions about the model. Is the clearance rate the same for infectious and non-infections virus? Line 470, you use profile likelihood for these parameters, what about the values of the other parameters when you are calculating these profiles? Line 511, this seems a little bit circular: you estimate all parameters with gs zero, then fix all parameters and try to estimate the two gs. But perhaps the other parameters would be different with g not zero?

The process for automatic selection of biomarkers also needs a little more clarification. It seems to be a generalization of stepwise analyses, but the issue of the combination of two lower ranked markers potentially being better than a higher ranked one is not mentioned or discussed. This is an issue because each parameter is tried individually. Also, you say (line 526) that it is possible to add time-varying covariates in this methodology, but you don't say anything about how that is done (it is not trivial), and in fact you almost don't say anything about results with time-varying covariates. Some of these aspects may also be relevant for discussion or limitation of the approach.

Line 238, even though you say that the mechanistic model was better, that is not what is presented in Table S1, where the group effect model is better. Please clarify. Also, in line 246 you state "no additional effect", but Table S1 presents results for δ. Also, Table S1 is not mentioned in this section of the manuscript.

I may have missed it, but it seems that in the "Results" nothing is said about time varying markers…

Something seems strange in some graphs in figure 2b and S8. In some cases, the mean value appears to be below every individual value; or sometimes above every individual value (for example, in the naïve). Also, are the thin lines individual predictions as stated, why do these lines have kinks instead of being smooth and do they really go through every data point in every animal (this is clear for example in the naïve, where the thin lines are clearly visible, are not smooth and go through every data point)?

Reviewer #2 (Recommendations for the authors):

– What the authors state the main contribution as (new framework of modeling) and what I found to be the main conclusion (vaccine-induced antibody binding indicates protectiveness) are different. Because the model and analytical approach is not particularly novel, I would suggest redesigning the manuscript to highlight the data and biological conclusions.

– Getting into the business of claiming there is some magical "correlate" is very tricky. I don't feel that this is what we need to understand the infection or response to vaccination, and the work in this manuscript does not assess sufficient data to make broad claims about any clinically-meaningful correlate. With as much data as there is in the literature, a validation using human data is warranted.

– In the introduction, the authors reference studies that suggest "binding antibodies to SARS-CoV-2 and in vitro neutralization of virus infection are clearly associated with protection". This seems to be the same conclusion that the authors came to and makes me question: what is new here?

– A more robust introduction that highlights the current conclusions and limitations of models in the literature is needed, particularly because the model presented is only a minor modification of those models. In addition, the model lacks immune dynamics, which would make its usefulness limited.

– In addition to the point above, while the model is a standard, previously published viral dynamics model with minor modifications, it was not adequately described for the broad readership of eLife. Perhaps I missed it, but I couldn't find where the terms were statistically justified?

– Several models have shown that viral load data, even when defined between compartments, is insufficient to distinguish transport between the nasal passages and trachea (e.g., Khan et al. Viruses, Ke et al. MedRxiv, Pinky et al. PCB, among others). In light of these studies, this part of the model seems unnecessary and one unsupported by the data. In addition, these other studies have also shown that viral and immune parameters are distinct in the nasopharynx and trachea. In the authors' work, the data were joined and no effective comparison was made, which may cloud the parameter estimates and conclusions. Minimally, a discussion and reference of these published works is needed.

– Another limitation of the model and the data is that viral loads in the nasopharynx can be similar when disease is not. Can the approach here be used to assess vaccine efficacy (in terms of reducing disease)?

– Curiously, CD8 T cells were measured in the serum, but this type of measurement tends to not reflect the events in the tissue where resident T cells are thought to be important. There were some comments made about the infected cell clearance rate, but it did not seem that the data were used to evaluate the parameter estimates or model conclusions.

– Macaques, unfortunately, are not a great model to assess the individual heterogeneity observed in humans. Dissecting the heterogeneity from different sources would be greatly beneficial, but it seems naïve to assume that this can be done using animal models. I suggest using a human dataset, where there are many to choose from in the literature, or artificially creating one from human data and see if the model can still perform.

Possible data sets and information:

(i) CDC list of studies of correlates of protection, reinfection studies, etc.:

https://www.cdc.gov/coronavirus/2019-ncov/science/science-briefs/vaccine-induced-immunity.html

(ii) These quantify antibody binding + other immunology: https://www.science.org/doi/full/10.1126/science.abm3425

https://www.nature.com/articles/s41586-021-03738-2?r=artikellink

https://www.sciencedirect.com/science/article/pii/S0092867421007066

(iii) One that has nice temporal data of lots of different antibodies and cells: https://www.science.org/doi/10.1126/science.abf4063

(iv) One that shows antibody levels + whether the macaque was protected: https://www.nature.com/articles/s41586-020-03041-6

– In reference to Table S1, it is stated that vaccinated and unvaccinated animals could be distinguished. Why is this the goal? We would know who is/isn't vaccinated – a better question is who among the vaccinated would not be protected from infection and/or disease.

– In Line 189-191, the authors state "both specific antibodies and specific CD8+ T cells are mechanisms commonly considered important for killing infected cells. We retained the anti-RBD binding IgG Ab that were positively associated to the increase of the loss of infected cells.". Unfortunately, this statement is incorrect as antibodies cannot kill infected cells. Antibodies neutralize virus so that cells are not infected, but they cannot kill cells.

– Prior studies have found that antibodies have a limited role during infection (e.g., see Goyal et al. Viruses). How does this fit into the results?

– Figure 2 is difficult to assess what is data and what is the model, and the model fit is difficult to see. It seems a though the 95% confidence intervals (gray shading) are also not indicative the model. Why are there multiple peaks and does the model capture that?

– The discussion could be improved. It lacked discussion of how the work fits into the literature, particularly other published SARS-CoV-2 models, how the correlate might be used in the clinic, etc. In addition, a discussion about the differences in dynamics within the nasopharynx and trachea in vaccinated individuals would have been interesting.

– It's unclear to me why the reproduction number R was under 1 for the alphaCD40.RBD group when there was replication for several days in this group.

Reviewer #3 (Recommendations for the authors):

First, a suggestion regarding my overfitting concern:

• The number of non-human primates in each arm of these studies is understandably limited, but cross-validation could be used to reduce the extent of overfitting even with limited replicates.

Next, two suggestions to enhance clarity:

• The rationale for the use of profile likelihood should be made explicit. Why do a few parameters using this approach and then later do rest with full maximum likelihood? Is it a limitation of the optimization software?

• In the model, why separately track virions from the inoculum versus virions generated in host? If it is just to allow for different clearance rates, why do we expect these to be different?
