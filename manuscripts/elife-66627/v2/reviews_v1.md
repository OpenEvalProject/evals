# Peer review - Round 1

Editors:
- Krzysztof Wabnik, https://ror.org/03n6nwv02 Technical University of Madrid Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66627.sa0](https://doi.org/10.7554/eLife.66627.sa0)

The main contribution of the article is the establishment of a framework for radial plant growth that was constructed using experimental observations fed into elegant computational models. This study will be of interest to plant scientists and more generally developmental biologists, working on mechanisms of tissue growth patterning.


---

# Peer review - Round 1

Editors:
- Krzysztof Wabnik, https://ror.org/03n6nwv02 Technical University of Madrid Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66627.sa1](https://doi.org/10.7554/eLife.66627.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Computational modelling of cambium activity provides a regulatory framework for simulating radial plant growth" for consideration by eLife. Your article has been reviewed by 2 experts in the field, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Przemyslaw Prusinkiewicz (Reviewer #2). The Reviewing Editor has drafted this to help you prepare a revised submission.

Major concerns rose by both reviewers relate to presentation, description, and clarification of models. Furthermore, the discussion of key model findings and their relevance should be improved. There are also major concerns on the experimental data quantification, the derived claims and how they relate to the presented models. Note this might also imply a deeper study of the presented models.

Specific comments of the reviewers:

Reviewer #1 (Recommendations for the authors):

Apart of the issues I have already expressed in the Public Review, please find below additional considerations:

– The authors need to work more on the clarity about some aspects of the model. How the growth is implemented in all the models? How diffusion is implemented? How the forces are implemented and the impact of the cell wall thickness? How the final timepoint is determined? I believe equation 5 needs to be revised.

Apart of the issues I have already expressed, please find below additional considerations:

– As I have already previously mentioned, an accurate image quantification with the proper replicates would help understand better the conclusions that can be extracted from the experiments. Otherwise, some statements about the results are not fully supported, and visual inspection of the images can lead to different and contradictory conclusions. For instance:

Figure 2 and Figure S1 look qualitatively different:

– In Figure 2, H4pro:mCherry seems equally expressed in the PXYpro:CFP domain and the SMLX5pro:CFP domain, without a clear maxima.

– In Figure S1, H4pro:mCherry it is much clearer its maxima at the interface of both domains, and is not that clear H4pro:mCherry is really much expression in the PXYpro:CFP domain.

Could the authors clarify these differences, and also how this is related to the statement in line 188? I would strongly recommend to do some kind of quantification, with more replicates.

The expression of PXYpro:CFP in Figure 3A looks like this marker is also reaching xylem, not just cambium. Although this seems contradictory with line 231, in which it is stated the PXYpro:CFP is surrounding the xylem cells. Quantification of the fluorescence and clarification in the text will help understand these apparent contradictions. If there is just a thin PXYpro:CFP band surrounding the xylem, it would be good to understand why this band is narrower sometimes and why is wider (eg Figure 2A)

– To have stronger conclusions about the proliferative state of the cell cycle, apart of doing the proper quantification, it might be useful to see the outline of the cells. Perhaps the combination of such data together with the modelling of the H4 marker could help to proof that cell proliferation is enhanced in that cambium region, and would enable to discard other possible interpretations.

– I would strongly suggest to study in depth the pattern formation capabilities of Model 3, including studying how the main parameters impact in the result of the outcomes (or a simplified version of it, as long as it can recapitulate the main perturbations). Perhaps this model needs to be revised, such that the cambium front instability does not occur. But perhaps the authors are in a misleading region of the parameter space. Also, the dynamics is important of these models, so there might be some observables that would be worth quantifying along time.

Reviewer #2 (Recommendations for the authors):

– The main weakness of this paper is, in my opinion, the presentation of the results. The progression through a sequence of models has some rationale – it presumably depicts the path of refinements through which the authors arrived at the final model – but makes this paper tedious to read and obscures key results. It would be beneficial if the paper focused on a well-organized, crisp, mathematically sound presentation of the final model, including all relevant equations, put carefully in the context of the essential molecular-level information, and with clearly stated discussion of lessons learned and shortcomings of the model. The intermediate steps, which may be of interest to researchers who want to continue this line of study, could be delegated to supplementary materials.

– Summary of key molecular players in lines 76-105 is very dense and requires an explanatory figure illustrating the proposed interactions.

– Although ARF5 is mentioned early on (line 101), the role of auxin is downplayed (c.f. lines 441-443). However, the recent paper by Smetana et al. (ref. 10) attributes a significant role to auxin. This discrepancy should at least be discussed.

– The authors tacitly assume that considering the cross-section of an organ such as the hypocotyl suffices to explain the radial organization of its tissues. Perhaps this is true; nevertheless, it is an assumption, which should be clearly stated as such. In particular, if auxin indeed is involved in the tissue patterning, wouldn't its flow in the longitudinal direction play a role?

– There are previous modeling papers dealing with the organization of tissues in shoots and roots, in particular:

Marta Ibañes et al., Brassinosteroid signaling and auxin transport are required to establish the periodic pattern of Arabidopsis shoot vascular bundles, PNAS 2009

N. Fàbregas et al., Auxin Influx Carriers Control Vascular Patterning and Xylem Differentiation in Arabidopsis thaliana, PLOS Genetics 2015

These papers should be cited.

– The idea of distinguishing real substances, tissues etc. from their models using an asterisk is an interesting one; however, in order to be really helpful it should be applied very consistently throughout. Currently there are inconsistencies: for example, in the legend to the right of Figure 5F symbol DF is not starred, but in the figure caption it is.

– The systems of equations representing the models are not adequately presented. For example, Model 1 deals with xylem, phloem and cambium cells, the latter in two states (Figure 1), yet Equations 2-4 apparently characterize only cambium cells. Further models are described even less rigorously. The list of parameters (Table S1) is obscure, as the equations involving listed parameters are not explicitly given. The readers should not be required to reverse-engineer the code to understand how the models really work.

– The models describe a growing system, yet the equations do not include a term representing a decrease in concentrations of molecules in the cells due to cell growth. Why?

– There are also further questions regarding the models. How and on what basis was the initial tissue template (Figure 1A) specified? What are the initial values of the variables? What are the mathematical conditions for attributing types to cells in the tissue?

– Why it the initial frame ( = the template?) in Model 3B (Movies 5x) different from those used previously?

– The table in Figure 5 G includes the heading "Initial values (after run)": What does this mean? (It sounds like an oxymoron.)

– Hollow phrases such as "minimal framework of intercellular communication loops" (lines 37-38) or "reciprocal and interconnected gradients of regulators along the radial sequence of tissues" (line 483) should be avoided, especially in the absence of a proper description of the mathematical models.

– The section on the physical properties of cambium does not adequately address the problem of radial file formation. The question of factors determining the orientation of cell divisions has been extensively addressed in literature (including numerous models), and references to three old papers do not sufficiently position the issue. The algorithm employed in the models to determine the orientation of the divisions is not explained (presumably, the authors just rely on a default algorithm implemented in Virtual Leaf). The observation that stiffening of xylem cell walls may contribute to the organization of cells into files is of some interest, but begs a biomechanical analysis, which is absent.

– Lines 435-437. Listing Turing (reference 43) as representative of "using positional information mediated by morphogenetic gradients" is inappropriate, given the long history of tension between Turing's reaction-diffusion concept and Wolpert's idea of positional information. The paper by J. Green and J. Sharpe, "Positional information and reaction-diffusion: two big ideas in developmental biology combine", Development 2015, provides an authoritative recent perspective on this tension.

– The discussion seems to be largely disconnected from the content of the paper. In particular, the relation of the text beginning in line 449 to the modeling effort is not clear. Is the phrasing "In contrast to our expectations…" supposed to mean "In contrast to the model"? Then, what is the reason for the discrepancy? Or, were these expectations independent of the model, in which case the question arises, how are they related to the topic of the paper, "Computational modelling of cambium activity…"

– Lines 579-580 state: "All simulations within Model 1, Model 2, and Model 3 […] were repeated at least ten times." Why? If the models were deterministic, they would produce the same results. If they included stochastic terms, the results of different runs would differ, but there is no indication of stochastic terms in the paper.

– Line 592 and following: Which parameters were optimized? The statement "The parameter space contains an interval for each parameter from which the parameter value can be chosen" is unclear: what would be a parameter for which a value cannot be chosen? Also, how many runs were performed to optimize? How was the end of the optimization process decided?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Computational modelling of cambium activity provides a regulatory framework for simulating radial plant growth" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Most of the remaining issues relate to the either lack of detailed explanations or confusing sentences. I suggest authors go carefully through all comments of Reviewers and try to address those for clarification.

The authors should also provide a quantitative analysis of radial fluorescence profiles as they previously performed in Shi et al. 2019. I believe this analysis will further strengthen authors claims. For ease, there is a number of alternative strategies that Reviewer #1 suggested for authors to consider while doing this analysis.

Reviewer #1 (Recommendations for the authors):

I appreciate the replies of the authors to my comments and the points they addressed, I think the quality of the manuscript has improved. See below some other comments I would like to make of this new revised version of the manuscript.

– I still find some statements about the interpretation of the cambium activity fluorescence reporters might require to be better supported. I understand that a detailed quantification might not be possible, but I would strongly recommend authors to do radial intensity profiles to support their statements, as the authors very nicely did in a previous publication [Shi et al. 2019] (e.g. one could do it with Fiji, with a certain line width and doing some binning along the line to smoothen fluctuations).

For instance, these are interpretations of the authors I did not find convincing:

Lines 284-287: 'PXY promoter reporter activity was observed distally to xylem sectors, whereas the SMXL5 promoter activity was as usual present distally to the PXY activity domain. Interestingly, PXYpro:CFP and SMXL5pro:YFP activity domains were still completely distinct '

I would say PXY promoter activity was observed also within the xylem sectors. I am not sure if PXYpro:CFP and SMXL5pro:YFP would be indeed completely distinct, perhaps they overlap?

It would be good to show the radial quantified profiles in WT as well, to better appreciate the differences with the mutants.

If the authors still find quantification is not the way to go, I would suggest doing zooms of the regions of interest, and showing single and composite channels to facilitate the interpretation.

– In the IRX3pro:CLE41 mutant, the statement about lower number of xylem cells should be better supported; looking at the time course of Figure 3—figure supplement 2, earlier time points in the IRX3pro:CLE41 line might suggest this is not the case. I think this raises the question of having more repeats to support this statement (having said that, more repeats of the pxy mutant would be also desirable). Also, I am wondering whether authors are referring to absolute numbers of xylem cells or fraction of xylem cells, could they clarify? Also, to support the claimed statements, a quantification with ilastik of xylem cells might be realistic to do.

– The authors conclude that the cell wall thickness in the procambial cells is smaller than in its surrounding tissues. The way they show it should be revised. First, it is not clear if they do it with Direct Red 23 (line 418) or Direct Yellow 96 (mentioned in the caption of Figure4—figure supplement 1). Second, it is not clear the mean intensity of Direct Red 23 or Direct Yellow could be a good proxy of cell wall thickness – could the authors justify this? (I am not an expert in this topic, but this should be clear and justified to non-experts as myself). In the case of Direct Yellow 96, the mean intensity might be related to the amount of xyloglucans if I understand it well from Ursache et al. 2018; in the case of Direct Red 23, I understand the fluorescence is related to cellulose content at a given part of the cell wall – but not forcely to thickness, and therefore overall stiffness. Third, the quantification using the Radial Profile function might be very misleading, given there can be other factors affecting the outcome, such as the density of cells at a given radial binning, the cell heterogeneity while being a tissue averaged measure, etc – better to do it at a cellular resolution.

– The diffusion operator as described in the appendix, if I understood it well and I am not wrong, it would not fulfil conservation of mass if it is applied to a tissue made of cells of different sizes. For instance, if you apply your operator to two cells with very two different sizes and make the numbers in terms of the exchange number of molecules (i.e., convert the expression of concentrations to number of molecules and cell volumes), the larger cell will have more flux of molecules than the smaller cell. Given the modelled tissue has cell size heterogeneity that can not be avoided, why didn't the authors use laplacians that could follow a conservation of mass such as in Sukumar and Bolander (2003)? I am wondering whether this violation of mass conservation might affect the presented computational results.

– I appreciate the performed model robustness analysis by the authors. For completeness, I think it would be important to include some additional simulations assessing the effect of diffusion rates (and/or the degradation of the modelled diffusible species), at least for CLE41. I believe some parameter ranges might stabilize the front – my suggestion is not to push to an in depth study on the front instability, which I understood is beyond the scope of this manuscript, but rather to ask for a more complete and robust analysis of essential parameters of the model.
