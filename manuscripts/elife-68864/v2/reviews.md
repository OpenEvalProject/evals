# Peer review - Round 1

Editors:
- Joshua T Schiffer, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68864.sa1](https://doi.org/10.7554/eLife.68864.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Thank you for submitting your work entitled "Dynamically linking influenza virus infection with lung injury to predict disease severity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Joshua T Schiffer.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers all appreciated the attention to an important question and the combination of experimental data and modeling to understand immune control of influenza in mice. However, the decision to reject the manuscript was based on two major factors:

1) The use of total CD8 rather than antigen-specific or 'active' (cytokine producing) cells.

2) The lack of statistical analysis in comparing different (and quite complex) models (especially since many of the conclusions rested upon model comparison).

As indicated, all reviewers were excited by the approach to combining novel experimental and mathematical approaches and felt that the validity of the conclusions and priority of the manuscript would increase if these issues could be addressed. However, ELife requires that authors are able to complete revisions in less than two months and it was concluded that it is unlikely that these concerns could be addressed within this timeframe.

I hope that this result will not discourage your work in this area or future submission to eLife.

Essential revisions:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Reviewer #1:

This is a tour de force paper describing a set of elegant experiments specifically designed for mathematical model testing and validation. The model takes the unprecedented step of linking kinetics of viral shedding, generation of infected cells, CD8+ T cell response and development of lung injury. Scientific conclusions are justified based on the analysis. The prediction that CD8 expansion but not levels of CD8+ T cells impact time to viral elimination is interesting and novel. The idea that infected cell density lowers Tcell-mediated clearance is also interesting and suggests a bottleneck to rapid immune clearance once a threshold of severity is surpassed.

Figures 3 and 4 are particularly instructive and interesting.

Overall, the paper could be substantially improved in terms of interpretation of the results and clarification of language regarding scientific conclusions. There are also a few slightly unclear sections.

1) In the introduction and conclusion, there is no mention that the balb c murine model may not capture the pathophysiology of influenza infection in humans. In particular, the relative contributions of humoral versus cell-mediated containment of infection may differ. The concepts of original antigenic sin and differential host susceptibility which may account for substantial heterogeneity in disease severity in human adults, are not captured in mice. The authors should directly admit this limitation and specifically acknowledge that the conclusions of their mathematical model (as elegant as they are) may not be fully generalizable to human infection. In addition, cited articles regarding flu pathogenesis should be labelled according to whether they are from humans, ferrets or mice. I would strongly consider reorganizing the discussion towards summarizing what conclusions might be relevant for human infections and what experimental data could be gathered to validate model predictions.

2) A key component of influenza pathogenesis is completely neglected, which is that a majority of infected people do not develop any lung disease. Instead, infection is limited to the upper airways. Therefore, a key role of the acquired immune response may be limiting spread from the upper to the lower airway. Under the best of circumstances, the author's model is relevant to only a subset of human cases. While the experimental system does not allow assessment of progression from upper to lower tract disease, this should be acknowledged as a major limitation of the system.

3) Figure 1: It is stated multiple times in the paper that Figure 1 demonstrates heterogeneity in viral loads. This is not the case as the standard deviation merely shows the confidence in the mean. Individual data points should be plotted to demonstrate heterogeneity in viral load and CD8+ T cell counts at each time point across mice.

4) Line 108: What percentage of infections are cleared within 4h? Are these included in the means and SDs in Figure 1? What is the proposed mechanism of these aborted infections?

5) A critical component of the model that is only mentioned in passing throughout the paper is the time delay in CD8 proliferation. The time delay parameter is as critical to the model as the density dependent CD8 killing rate (see Appendix 3 Figure A4). Yet the biology underpinning this delay is given short thrift in the discussion. It would also be useful to show that a model without this assumption fails to fit the data.

6) Table 1: are all parameter fitted? Are there references from the literature confirming that some of these values are realistic?

7) The term "model ensembles" described in line 148 is never adequately defined. The subsequent section of the paper is therefore confusing. Is this essentially describing the fact that several parameters are not identifiable because they are correlated to achieve model fit? This would not negate the model's validity but should at least be stated. Does Figure 2A only include parameter sets that resulted in optimal fit to the data (<5% error from the best fit) as described in the methods? Please clarify.

8) Line 320: the authors never show that small changes in viral load can lead to major changes in disease severity. They actually could do this with the sensitivity analysis output and it would be quite useful. However, without these simulations explicitly shown, this sentence should be removed.

9) Line 386: this is a false statement. See Figure 3 in https://www.nejm.org/doi/full/10.1056/NEJMoa1716197

Reviewer #2:

General assessment: The study presents a thorough combination of different experimental measurements with mathematical modeling to link viral dynamics and disease pathology in a mouse model of influenza infection. They find a very remarkable connection between the area of lung injured, the CD8+ T cell response and the development of disease symptoms of the animals. The discovered connections could advance the understanding of influenza virus infection in mice, but, in my view, the proposed predictive value should be further corroborated by appropriate analyses. I consider this as a very interesting study that is methodologically sound and innovative. However, I would have some comments (see below) that question the significance of this work for the field as requested by eLife.

1) A major concern affects the CD8+ T cell response used for modeling. It is stated that the total number of CD8+ T cells rather than the virus specific CD8+ T cells were used as the later often show varying dynamics (line 447-451). In which way would the use of virus-specific CD8+ T cells skew the results as mentioned? It would be an interesting question if the found density-dependent CD8+ T cell mediated clearance also holds if only virus-specific CD8+ T cells are considered. In addition, a population of memory cells was explicitly included in the model to reduce the number of CD8+ T cells responsible for clearing infected cells. This might not be necessary if virus-specific cells show a different dynamic than the total lung-resident CD8+ T cell population. In this regard, also the statement that the magnitude rather than the efficacy of the CD8 + T cells controls clearance could be questioned (line 98-99), as these aspects were not separately investigated in the experimental data nor the modeling framework.

2) Although the authors investigate the impact of the magnitude of the CD8+T cell response on the recovery time using their identified model (Figure 3), they do not use/extend these analyses to show the predicted changes for disease dynamics and pathology as based on the "workflow" shown in Figure 5. I think the study would substantially benefit if the postulated connectivity between disease dynamics and pathology, and the proposed impact of these findings on "forecasting disease progression, potential complications and therapeutic efficacy (line 23)" is shown at least theoretically for some scenarios (e.g. those used in Figure 3 that affect recovery time).

3) The analysis here benefits from the possibility to measure local viral loads and CD8+ T cell populations within the lungs of mice. I consider this as being rather difficult to be done in humans, as well as finding appropriate quantitative markers for disease pathology, such as weight loss. Therefore, I do not directly see the claimed ability of this study to enhance the ability to forecast disease progression and potential complications, at least not in humans. Even for mice it would be important to know if e.g. having only a limited number of measurements on the dynamics of the CD8+ T cell response and the viral load (e.g. until day 4 or 6 if this could be measured in vivo) is sufficient to parameterize the whole model appropriately in order to predict further dynamics.

Reviewer #3:

The authors present an interesting mix of modelling and experimental work looking at CD8 T cell control of influenza virus infection in mice. This extends previous work by looking at infected cell area, and coming to some slightly different conclusions on the mechanisms of T cell control. The strength of the conclusions is not well justified, and therefore the advance of previous work seems somewhat incremental.

1) Table 1 includes 21 parameters to fit CD8 and viral load. However, figure 1 suggests there are only 24 data points. This seems rather over-parameterized? This seems very evident when the authors justify the model, because for every potential inflection of each curve, they seem to add another parameter. But are all of these justified? Does adding additional parameters improve the fit (by AIC, for example)?

2) There appears no consideration of 'significance' in comparing the fit of different models. For example, the authors state (lines 127-135) that density dependence in clearance was a better fit than in CD8 expansion (as used previously), and just refer to the shape of curves on specific days. Surely something like an AIC for overall fit would be useful in comparing different models?

3) There seems a major confusion between 'total CD8' in lung, and virus-specific CD8. These seem used interchangeably. For example, line 166-168: 10% of (antigen specific) cells survive into memory, and here the authors comment they observe 17% (of peak total CD8). In the discussion (line 262 onwards) the authors discuss CD8E – referring to literature on antigen specific cells and comparing their results to these – when they have not measured this. This is justified because cells of different specificity have different kinetics. But since the total CD8 number is being used to predict the effects of antigen-specific cells (and this is the central conclusion of the manuscript) – surely some measure of what is functional (?cytokine secreting) or antigen-specific (tetramer or ICS positive) is necessary?

4) Model comparisons with data seem very vague. For example in Figure 4c the authors state (line 221-222) "the dynamics of the damaged cells of the lung correspond precisely to the dynamics of the maximum CD8". This sounds like it may be quantitative, but the figure just looks like they both peak around day 8 and decline. The CD8 increase on day 2 – whereas lesion does not increase until later. The same is true for the claim that AUC of infection matches active infection area (Figure 4B).

5) There seems relatively little explanation of the link between viral loads and lung lesions. For example, viral load peaks on day 2 and decreases thereafter. But lung lesion size is barely detectable at this time, and increases rapidly? The authors argue that AUC of virus = active area. How does this arise? Do infected cells produce a burst of virus and remain antigen positive for some time? What resolves antigen negative cells? How does lung lesion size (and %active inactive) directly relate to viral load? The authors make arguments around these issues, and figure 5 might lead one to believe there is some modelling to link all these, but there does not appear to be a mechanistic explanation?

6) The entire section "density dependent infected cell clearance" involves a lot of speculation on recovery time, CD8 thresholds etc. This seems entirely dependent on the model formulation, and average parameters (which are widely distributed). Is there any experimental evidence to support this modelling speculation?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Dynamically Linking Influenza Virus Infection Kinetics, Lung Injury, Inflammation, and Disease Severity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Joshua T Schiffer as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Sara Sawyer as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) Please include analyses in which δ_e does not approach its boundary value.

2) Please include AICs and model fits for models which are less supported by the data.

3) Please rewrite the abstract, introduction and discussion to highlight the scientific conclusions of the paper, rather than just the substantial technical achievements of the paper (fitting a model to several longitudinal data types in a complex and potentially representative model system of influenza).

4) Please frame the paper's conclusions and limitations more specifically in reference to their potential relevance for human infection. Specifically, highlight that the system employed in this paper is akin to a primary infection model rather than re-infection. Please also make an effort to partition past literature into mouse and human studies for better clarity.

Reviewer #1 (Recommendations for the authors):

The experimental data and modeling are highly robust. The conclusions of the paper are clearly supported by the results. The sensitivity analysis is particularly impressive and suggests a system that is highly conserved across a wide parameter space. Model validation with CD8+ depletion is a nice addition that leads to interesting and surprising conclusions. The figures are highly instructive and easy to read.

An area where the paper could be improved is conveying the actual scientific conclusions more clearly and precisely with more focused review of existing literature. The relevance of the paper's conclusions for human influenza could be discussed with more careful language.

First, the mechanistic conclusions of the work could be emphasized along with the methodology of the work. At present, these are completely lacking from the abstract which somewhat blandly just says that the paper describes a model which fits to data. From my perspective, currently underemphasized and novel / interesting conclusions are that:

1) CD8+ mediated killing becomes much more rapid on a per capita basis (40000 fold increase) when infected cells dip below several hundred cells approximately 7 days post infection.

2) There is a negative correlation between infected cell clearance by innate versus CD8+ mediated mechanisms, implying that poorer initial clearance of virus may result in more effective later killing by acquired immune mechanisms.

3) Even ~80% reduction in maximal CD8E+ levels could prolong infection by 10 days though delay in attaining these threshold CD8E+ levels due to experimental or in silico CD8+ depletion only delays viral elimination by a day.

4) Most interesting and counterintuitively, CD8+ depletion allows for considerable reductions in the size of lung lesions as well as inflammation scores and degree of weight loss during primary influenza infection. This result suggests that CD8+ T cells have the potential to create significant bystander damage in the lung.

Second, the introduction and discussion continue to not differentiate whether past experimental results are from humans or mice. It is somewhat misleading to cite mouse studies without acknowledging that these are from a model that in no way captures the totality of human infection conditions. For all animal models of human infection, the strengths of the model (ability to control experimental inputs and obtain frequent measurements) are counter-balanced by lack of realism. Humans have a complex background of immunity based on past vaccination and infection, different modes of exposure and other innumerable differences. In most human infections, the degree of lung involvement is minimal. Please stipulate in the review of existing literature which papers were done in mice versus humans. Please also frame conclusions of this paper in the discussion in terms of how it may or may not be relevant to human infection.

Third, this is a primary infection model, and this point also should be emphasized. The greatest relevance of the mouse model in the paper may be for pediatric infection in humans, rather than adults who have had multiple prior influenza exposures and possibly vaccinations. Presumably CD8+ responses can be expected to be more rapid with availability of a pre-existing population of tissue resident CD8+ T cells as would occur with re-infection. The results of CD8+ depletion prior to re-infection would potentially be very different (likely harmful) in a re-infection model and this should be discussed. This is mentioned in Line 467 but is given short attention elsewhere.

Line 60: stating that other studies have had limited success is rather insulting. Please rephrase and be more specific about why this study breaks new ground.

Line 81: "viral loads in the upper respiratory tract do not reflect the lower respiratory tract environment. " Please include a citation, remove or clarify that this is a possible confounding variable in the analysis.

Line 91: define lung histomorphometry. This is a fairly novel approach for most readers.

Line 101: This is a strong statement about viral load. Unless formal correlate studies have been done in humans (which they have not), I would day "may not be correlated" or remove altogether.

Line 201: involved with what? I am not sure what this sentence means.

Line 209: I would suggest denoting a separate section to the sensitivity analysis versus the parameter fitting as the fitted correlation between δ and δ_e appears separate mechanistically from the relationship between δ and viral clearance / total # of CD8E

Line 251: Please cite the clinical correlate oof this in the discussion. Immuncompromised humans often shed influenza (and SARS CoV-2) for months. See work from Jesse Bloom's group published in eLife on this subject.

Line 321 should this read "clear infected cells from the lung?" I am confused about what this sentence means.

Figure 5D: why are the dots yellow? Is the magenta line CD8 depleted?

Line 386: Has antiviral therapy been linked with extent of radiologic lung lesions in clinical trials. This would be a very atypical clinical trial endpoint so please be more precise with language. It is possible as previously mentioned in the paper that viral load may not predict lesion size or disease severity in humans.

Line 477: add degree of immunity from prior infections as a critical variable

Reviewer #2 (Recommendations for the authors):

This is a revised version of a previously reviewed article. The authors performed extensive additional analyses to address previous concerns and issues raised by the reviewers. However, there are a few additional points which, in my view, still would need some clarification:

1. As pointed out by one of the previous reviewers, the remarkable ability of the model to basically cover every change in the dynamics observed within the data (Figure 1) could suggest that the model is overfitting the data. In response, the authors mentioned that they performed robust fitting and sensitivity analyses, and also mentioned that they performed several different model attempts to reach at their final model. However, the current information provided, as e.g. in Figure 2 showing the parameter estimates, do not seem to fully support this claim. The authors state that "the majority of parameters are well-defined" with the exception of three parameters. However, also the death rate δ_E reaches the imposed boundary for fitting, which seems to be not addressed. As this parameter controls the CD8-mediated death rate and, thus, could be critical for the argument of a density-dependent death rate, I think this should be discussed/investigated in more detail. In addition, it could be very convincing if the AICs of some of the models tested that did not fit the data (i.e. reduced models as claimed within the response), are shown within the manuscript to support their claims. In addition, just as a suggestion, approaches that do not explicitly describe the mechanistic of the CD8+ T cell response but rather describe the measured responses by a spline function could be considered as well (see Kouyos et al. PLoS Comp Biol 2010), reducing the complexity of the model by still being able to examine the relationship between CD8+ T cell response and immunopathology.

2. Lung immunohistopathology is quantified based on tissue sections of individual mice. Did the authors analyze the whole (i.e. 3D) lung for regions of active/inactive lesions or only representative 2D tissue sections? In addition, how many mice/tissue sections were analyzed at each time point (e.g. Figure B/C)? It would be interesting to know how representative a 2D tissue section as shown in Figure 4A would be for the situation in a mouse, and also how representative it would be across mice. I apologize if I missed this information in the text but I think these details should be provided.

3. In Figure 5 B and D the difference between the fitted (black) and predicted (purple) relationships does not seem to be explained within the figure legend nor the text. I have difficulties to understand how these two things are related. The same holds true for Figure 5A, where there is no information on what the purple curve represents.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your thoroughly revised article "Dynamically Linking Influenza Virus Infection Kinetics, Lung Injury, Inflammation, and Disease Severity" for consideration by eLife. Your article has been reviewed by 1 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sara Sawyer as the Senior Editor.

Essential Revisions:

We thank you for taking the effort to making excellent revisions and thoroughly addressing all reviewer comments. We apologize for not noticing this in the last revision but the Discussion section of the paper lacks a limitations paragraph and there are indeed several limitations that are not mentioned (lack of complete realism of the mouse model as a model of human infection; the fact that the weight loss equations that relate to inflammation are not "mechanistic" and therefore provide only some insight; other arms of the immune response are not studied in depth (humoral) experimentally and this system and may be important). A brief acknowledgment of these and other limitations, and possible next steps to address them, would really strengthen the impact of this paper.
