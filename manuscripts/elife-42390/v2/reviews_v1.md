# Peer review - Round 1

Editors:
- Miles P Davenport, University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42390.sa1](https://doi.org/10.7554/eLife.42390.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

HIV remains a major global health threat, with the virus infecting and destroying CD4+ (“helper”) T cells. This work combines clinical data and mathematical analysis to understand how T cell numbers are affected by infection and treatment at different ages.

Decision letter after peer review:

Thank you for submitting your article "A mechanistic model for long-term immunological outcomes in South African HIV-infected children and adults receiving ART" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Neil Ferguson as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nikos Pantazis (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes a novel approach to characterizing CD4 cell recovery following ART initiation by modelling the ratio of CD4 counts of persons on ART to those of age/sex matched non-HIV infected individuals from the same population. The authors apply nonlinear mixed models which are based on plausible biological mechanisms. The model is demonstrated using treatment cohort data from children and adults from South Africa.

Both reviewers and I agree that the idea of modelling ratios is innovative and has great potential to improve the conceptualization of immune recovery following HIV treatment initiation. However, the impact of the work would be greatly enhanced through a clearer and more intuitive exposition and demonstration of both the proposed model and the alternative existing models which on which this work innovates. The reviewers have also raised important questions about the selection of individuals and data cleaning, and how these choices might influence the results. Finally, the data and assumptions for the “healthy individual” reference population in different scenarios need to be clarified. Most fundamentally, it is not clear how CD4 cell growth rates are estimates for healthy individuals when all of the data informing model inference are amongst ART patients.

We encourage resubmission of the manuscript, but anticipate that it will be substantially revised to provide an intuitive exposition of the proposed model.

Essential revisions:

– Incorporate an intuitive exposition of the proposed ratio model including figures illustrating the concepts and quantities introduced (carrying capacity, growth rate), how these are related to the model parameters, and how the model is affected by permuting each parameter.

– Consider focusing on only one of the two scenarios regarding the treatment of the baseline values as a covariate or not. Both options could be presented, explaining the pros and cons of each and how one was chosen, but then focus on one for the rest of the manuscript.

– Clearly explain how CD4 trajectories for non-HIV infected “healthy” individuals were modeled, and how these parameters were estimated given that there are no data about non-HIV infected individuals in the dataset used for model estimation. Subsection “Variable scaling” paragraph three describes CD4 is taken to be constant in healthy adults (independent of age and gender), but in the Results there is a growth rate for healthy adults >0. How is this growth rate estimated?

Given that CD4 levels at various ages come from external sources, authors should clarify better how they obtained the y-values required for the calculation of the ratios (z-values). Even reading S1, it is not clear if y-values for children of a given age were all the same (based on the predicted value from the exponential model; was it a double exponential as stated in the main text or single exponential as stated in S1?) or there was some variability allowed (and if yes, was it taken into account?). Moreover, I was puzzled even more in the adults case: how similar were the results when using modelled y-values (Figure 2—figure supplement 2) compared to using a constant value of 800 cells/μL? How different are the results compared to an analysis of just CD4 counts if scaling is just division by a constant?

– Relate the outputs of the models to outcomes of clinical relevance: such how long does it take to reach "normal" levels? What is the proportion of patients that is expected to reach these levels after a certain duration of treatment? How do baseline CD4, age, sex, viral load, virologic response etc. affect these quantities?

– Provide greater details on each of the exclusion criteria, how the selection of study participants might have affected estimates and results, and sensitivity analysis around these decisions. For example, more than 90% of the study participants are excluded when requiring at least 4 CD4 measurements and completeness in other key covariates. I suspect that the ">=4 CD4 measurements requirement" accounts for a large part of this >90% exclusion. What about the mechanisms behind this selection and their effects on the validity of the results? Do people have fewer CD4 measurements due to staggered entry into the study (more likely a "Missing Completely At Random" mechanism) or are they lost to follow-up or even dead before contributing at least 4 measurements (more likely "Missing At Random" or even "Missing Not At Random"). The issue should be thoroughly discussed and choices for the analysis should be well justified.

– Providing datasets and R code to explore the model and reproduce analyses may help readers to explore and understand the dynamics of the proposed model and data processing steps to prepare the modeled quantities.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A Mechanistic Model for long-term Immunological outcomes in South African HIV-infected Children and Adults receiving ART" for further consideration by eLife. Your revised article has been evaluated by Neil Ferguson (Senior Editor) and a Reviewing Editor.

There are only a couple of remaining areas where we believe additional clarifications could be made. In particular, additions in the Materials and methods section and figures to give intuitive understanding of the model parameters would be helpful. Suggestions are outlined below:

Editorial comments:

– It is confusing that Equation 3 about CD4 trajectory for HIV-negative adults is expressed in terms of time since ART initiation since they do not initiate ART. It would be clearer to express this as a relationship between age and CD4 trajectory, and then expressing Equation 2 as a function of age at ART initiation and time since ART initiation.

– It would be helpful to give Equation 1 a descriptive interpretation of all of the parameters in Equations 2, 3, and 4 (k, q, y0, x0, z0, K, Q) and (2) examples of typical values or ranges for each parameter. It might be helpful to put this in a table that the reader can refer back to later.

– Subsection “Variable scaling”: My understanding of the methods is that the outcome variable that is modelled is the scaled CD4 count, rather than the CD4 count itself. Is that correct? If so, perhaps useful to clarify that in the first sentence of this section.

– Figure 2: This figure showing the logistic model would be more helpful for intuitively explaining the model with improved labelling and descriptions. What is “x-var” and “time-t”? What are the units on the axes? It is not clear how the vertical axis relates to CD4 or scaled CD4.

– Figure 3—figure supplement 2 and Figure 4—figure supplement 2: These figures are very helpful. A few aspects could be clearer:

* What are the solid and dashed lines?

* It would be helpful to add annotations for age at initiation and other relevant covariate values for each panel.

* Is it feasible to present this also with an axis for CD4 count? Or add a separate figure showing the data and trajectories for a couple respondents on both the scaled and natural CD4 scale?

– The eLife editorial guidance indicates that data and analysis code should be made available for tranparency and reproducibility. The authors have responded to the editorial request for this with contact information for a data request for IeDEA cohort data, but have not provided analysis code or data to reproduce the results. Especially given the stated objective of the manuscript to propose methodological advancement for modelling CD4 recovery, I think it would be very helpful to provide a limited dataset of the observations used in the analysis and code to reproduce the analysis, such that readers can implement and extend the proposed methods. This does not need to be the full IeDEA dataset, only the observations and covariates used in analysis in a suitable format for reproducing.
