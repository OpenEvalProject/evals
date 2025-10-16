# Author response - Round 1

Authors:
- James A Watson ([ORCID: 0000-0001-5524-0325](https://orcid.org/0000-0001-5524-0325))
- Stije J Leopold ([ORCID: 0000-0002-0482-5689](https://orcid.org/0000-0002-0482-5689))
- Julie A Simpson ([ORCID: 0000-0002-2660-2013](https://orcid.org/0000-0002-2660-2013))
- Nicholas PJ Day
- Arjen M Dondorp ([ORCID: 0000-0001-5190-2395](https://orcid.org/0000-0001-5190-2395))
- Nicholas J White ([ORCID: 0000-0002-1897-1978](https://orcid.org/0000-0002-1897-1978))

## Response text

DOI: [10.7554/eLife.43154.007](https://doi.org/10.7554/eLife.43154.007)

[Editors’ note: the author responses to the first round of peer review follow.]

[…] However for reasons stated below, both reviewers have major concerns with the analysis. As a result, this paper cannot be published in something like its current form. The first Case Study is not appropriate because it doesn't ask well-posed causal questions, and the second Case Study is essentially a critique of another paper that I can't verify includes a correct description of what the other paper did. If it is a correct description, it is a very important point that should be made as a letter or some other way, and the simulation is superfluous except to provide an illustration to those outside the epidemiology field.

The summary letter clearly demonstrates that both the editors and the reviewers have spent considerable time delving into the paper and the accompanying code. We are very grateful. The synthesized criticisms are informed and constructive and this assessment and review is much appreciated and will ultimately lead to a substantially improved manuscript.

We would like to appeal against the decision to reject the paper.

The major concern (point 1) is that Case Study 1 does not ask well-posed causal questions because it does not discuss interventions. However, both reviewers acknowledge that this view is not universal in the field of causal inference and that this perspective is subject to some debate. We accept that consideration and presentation of this important aspect was lacking in the submitted version of the paper. However, contextual understanding of the medical aspects of severe malaria is needed for a correct interpretation of our results. Severe malaria is a medical emergency with high mortality, and a very rapid evolution. Most deaths occur in the first 24 hours following admission to hospital resulting from sudden onset of acute complications. The pathological process and therapeutic implications are more comparable to haemorrhage. There is a single well-defined and feasible intervention: blood transfusion. Indeed, severe malaria is the major reason for blood transfusion in children in sub-Saharan Africa. Severe malaria is the consequence of the malaria parasite invading a substantial proportion of circulating red blood cells, and these invaded red cells blocking the microcirculation – a process with a time course measured in hours. Anaemia results largely from obligatory haemolysis following schizogony, and sequestration of infected and uninfected red cells. To this extent, the primary way in which the variable haematocrit changes is clear. Furthermore, the degree of anaemia (measured as haematocrit) is certainly a determinant of patient outcome and has considerable practical utility. The counterfactual outcomes of interest are those that would be observed if it were possible to change the haematocrit on admission. Transfusion on admission is the only acute intervention to treat severe malaria in this emergency situation. The other interventions that are mentioned to treat anaemia are not relevant in this context. Patients would die before any drugs acting on the blood marrow took effect; active case detection cannot be done in remote rural areas where severe malaria kills most children; iron supplements at a population level are not a reasonable intervention providing no protection against acute haemolysis causing anaemia in falciparum malaria. Thus, in the case of haematocrit, the way in which this variable changes is known; there is practical utility in its measurement; and the only relevant intervention is transfusion. For these reasons we do not think that the measured causal effect can be explained as a weighted average of multiple factors. However, we agree with the reviewers, that this might not the case for each of the other variables.

The other critique is the dependence on the time of admission. Every study in severe malaria suffers from the selection bias of only considering patients who seek treatment at larger health centres. However, the problem addressed in our paper addresses the real-life situation on how to manage patients with severe falciparum malaria admitted to hospital. Whether or not to transfuse these patients on admission is a very important question and we believe causal reasoning is essential in the debate. We find that moderate anaemia is not harmful and could be even be beneficial in severe malaria. We are careful not to overstate the implications for blood transfusion due to the exploratory nature of the analysis. Our finding may explain why the very large FEAST study reported a six-fold higher mortality in patients who were above the recommended haematocrit transfusion threshold yet still received a blood transfusion. In summary, the causal question for haematocrit is well-posed and this work should help guide future analyses of transfusion-based intervention studies.

Well-defined interventions are also potentially available for raised blood urea nitrogen: the intervention is here is hemofiltration or dialysis; high parasitaemia: the intervention is the anti-parasitic drug; pulmonary oedema: the intervention is oxygen and positive pressure ventilation. For seizures, anticonvulsants can be given. For acidosis there are experimental treatments. For coma itself there are no direct interventions possible and we agree to remove this from Figure 4. However, we think anaemia, pulmonary oedema, seizures and blood urea nitrogen should stay in Figure 4. None of these variables are chronic unalterable health states but the result of the acute infection.

The second major concern (point 4) is that Case Study 2 is a critique of two recent major papers (notably one in eLife) and that the validity of this critique cannot be verified. Both Nature genetics and eLife only accept correspondence up to one year after publication (publication dates were 2014 and January 2017, respectively), and therefore this channel of communication is closed. The availability of open channels for balanced critiques of published research is essential for reproducible research. We are sure that eLife promotes this healthy scientific exchange. We have asked Professor Kwiatkowski (corresponding author for both papers) which of the possible analyses were done and it was confirmed to be scenario b (from your summary letter). When we subsequently sent our concerns along with a draft manuscript (in total two emails), no response was given. We have the email correspondence to verify these exchanges.

This highlights the problems of publishing data analytic results with no accompanying code. Even if their data were openly available, reproducing the analysis would require reverse engineering. We have gone to significant effort to support all our results with open, carefully annotated code and deidentified data.

As a final point, it is mentioned that the simulation study we present in Case Study 2 is superfluous. We respectfully disagree. This simple simulation shows that reasonable values of the effect of G6PD deficiency on anaemia (taken from previous published estimates) would suffice to explain the observed negative association between cerebral malaria and severe malarial anaemia. This `sensitivity’ analysis is an important building block in the argument: if larger, unreasonable effects were necessary to explain the observed results, a residual direct effect could still be posited.

Would eLife consider our appeal under the following set of conditions?

· We will add to the Methods section careful consideration of the counterfactual states underlying the exposure variables.

· We will remove coma as an exposure with an interpretable causal effect and add a point to this effect in the discussion.

· We will address the concerns in point 2. This highlights an error in the manuscript and this will be changed accordingly.

· We disagree with point 3. All variables considered are at the point of admission and therefore there are no feedback loops involved. The didactic aspect will also be addressed, but the DAG in Figure 3 is useful in that it shows the overall picture of expert knowledge in severe malaria using the key admission variables.

[Editors’ note: the author responses to the re-review follow.]

[…] We can think of a few different ways you might proceed; a focused paper on the second part (which would seem appropriate for eLife given the publication of the prior paper in the journal); a tutorial paper that uses the second part as an example but is more generally about causal reasoning; or perhaps the full paper (in which case we would suggest switching the order of the parts because the G6PD piece is easier to understand so could naturally come first). This last possibility seems unwieldy for the same reasons as the original paper.

You are free to take or leave any of these suggestions, but this is how we see the paper. If you do split it up, we would suggest that the G6PD part (with or without surrounding tutorial material) would be of greatest interest to eLife given the prior publication. The mortality prediction part is a large and complex approach to a focused clinical question that might by itself be a very good paper for a more specialized journal.

This is a re-submission of a previously rejected paper, entitled "Causal pathways in severe malaria". Following the recommendations of the senior editor (Prof. Neil Ferguson), after a successful appeal against the reject decision, we have made considerable changes to the manuscript. We have kept only the section which deals with Berksonian bias in two recent major publications (Malaria Gen Nature Genetics 2014, and Clarke et al., 2017) which report a protective effect of G6PD deficiency in severe cerebral falciparum malaria. Our re-submission focuses on highlighting how Berkson’s bias likely explains all of the observed association. This would invalidate the model of balancing selection for G6PD deficiency mutations proposed by Clarke et al.

The only relevant reviewer comment concerning this re-submission is now:

4) For Case Study II, it is hard to understand what was done in Clarke et al., the paper in eLife that they criticize. We can't tell on a brief look at that paper whether the comparison was between:

a) Severe malaria anemia (SMA) (+- cerebral malaria CM) vs. population controls, and separately CM+-SMA vs. population controls, for G6PD status (which would not suffer from the problem the authors posit);

b) SMA only vs. population controls, and CM only vs. population controls (in which the CM only group would be depleted of those with SMA, and thus a risk factor for SMA would falsely look protective against CM only);

c) SMA vs. CM among severe malaria (which appears to be the case for the DAG presented in Figure 7, though I'm not sure), which seems to be what the R code posted on GitHub assumes.

This needs to be clarified further before it can be evaluated.

The Materials and methods section of the paper now shows that scenario 3 is almost certainly the one used in Clarke et al.to demonstrate a protective effect of G6PD deficiency on cerebral malaria. Although it is not directly stated in the Clarke et al. Materials and methods section, we show that it can be deduced from tabular data presented in the paper.

We suggest that the article type of this re-submission is modified from `Research Article’ to `Short Report’ in light of its new brevity.

[Editors’ note: the author responses to the re-review follow.]

The reviewers and reviewing editor have discussed the manuscript and believe it can be made acceptable for publication after some crucial but relatively minor revisions:

1) Clarity about what was done. Reviewers had a hard time establishing precisely what was done in the two papers, and how that relates to the simulations. In particular, please:

a) State precisely the regression that was made in each paper [which we believe was Pr(CM and not SMA) vs Pr (control), in logistic regression with G6PD genotype as predictor in a case-control format, and similarly for SMA and not CM) and quote the relevant passage in each paper that states the exclusion of dual cases.

b) State that this is the same comparison (with certain simplifications e.g. males only) in the simulation.

We agree that the original presentation lacked clarity and we have substantially rewritten the Materials and methods section in light of this comment (subsection "Data analysis in Clarke et al., 2017, and MalariaGEN et al., 2014".

The rationale for why we believe our simulation mimics these reported results is then given in the subsection "Sensitivity analysis".

The bias stems directly from the selection distortion in the CM case definition. The adjustment for sickle cell in the logistic regressions in both MalariaGen, 2014, and Clarke et al., 2017, will not impact on the bias we are investigating in our simulation study. Sickle cell is a confounder between the two clinical presentations – as demonstrated in the causal diagram (Author response image 1), an extension of Figure 1 in our paper to include a vertex for sickle cell status – and the authors are correct to adjust for it, therefore removing any biased association. Our simulation assumes that SMA and CM occur independently thereby reflecting the adjusted relationships in both papers (subsection "Sensitivity analysis").

Sickle cell mutations will increase the likelihood of anaemia and are presumed protective against CM.

2) Address a reviewer concern that the statistical noise around the estimated OR looks large in your simulations given the use of 1 million people. This may be a false impression or may be due to the rarity of one cell in the odds ratio, but please explain.

This was a typo in the code – the original plot was not based on 105 rather than 106 individuals. We have corrected this and the noise in the plot (Figure 2) is greatly reduced. We thank the reviewer for pointing this out!

3) Address a reviewer concern that producing a close quantitative match to the biased odds ratio for CM is not easily interpretable given the simplifying assumptions notably males only – would that not change the value substantially so that the agreement becomes qualitative rather than quantitative? A simulation including females would be simple to do.

In fact, we contrast our simulated results against the reported results in males only. We get an almost perfect match for the reported results in males. This has been made clearer in the Results (second paragraph). Therefore, in our opinion, there are no major simplifying assumptions that should impact this simulation/sensitivity analysis.

Although it is simple to generate proportions of females and males with G6PDd under an assumption of Hardy-Weinberg equilibrium, a simulation involving females is in fact more complicated. It necessitates assumptions regarding the gene dose effect (female heterozygotes are mosaics of deficient and normal red blood cells). As the simulation is currently written, there is a unique free parameter and this facilitates interpretation. The gene dose effect would require one extra parameter for which there are little data on which to calibrate it.

4) Reviewers found point #1 confusing perhaps for several reasons, one of which is the use of Berkson's bias as the explanation here. Indeed, on first reading I had thought that the mistake was that the earlier papers had looked at predictors of SMA and CM among all severe malaria patients (without healthy controls). That would be classic Berkson's bias as taught in basic epidemiology classes. The bias you have identified is closely related, is still a form of collider bias, but is not exactly the same; it is that "CM" is really "CM and not SMA" and vice versa. The wording about Berkson's bias may just mislead people – maybe you want to say collider bias, and make clearer in the DAG how this works. Removing Berkson from the title could also clarify for those who only read the title!

We agree and thank you for this suggestion. The title has been changed to "collider bias" and we have changed all mentions in the main text to collider bias also.

In the DAG in Figure 1, we have changed the name of the collider variable from "Included in study" to "Case definition". This shows how the case definition is simultaneously dependent on both clinical presentations.
