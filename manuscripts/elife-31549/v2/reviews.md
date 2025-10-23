# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31549.sa1](https://doi.org/10.7554/eLife.31549.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Induction of Plasmodium falciparum gametocytemia in the Controlled Human Malaria Infection model: a randomised trial comparing four antimalarial drug regimens" for consideration by eLife. Your article has been favorably evaluated by Prabhat Jha (Senior Editor) and three reviewers, one of whom, Ben Cooper (Reviewer #3), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Nicholas J White (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes a novel controlled human malaria infection model for Plasmodium falciparum that consistently and safely induces gametocytaemia using four different drug-regimens based on sulfadoxine-pyrimethamime and piperaquine. Estimated mean gametocyte circulation times were about 3 and 5 days for male and female gametocytes respectively and the timing of gametocyte appearance indicated probable commitment to gametocyte production in the first wave of asexual parasites. This work has importance for understanding gametocyte dynamics and evaluating transmission blocking interventions.

Essential revisions:

1) Clarification of sample size calculations is required (see reviewer 1 comments).

2) The section on parasite DNA and RNA quantification needs strengthening.a) The performance characteristics of the 18S DNA and mRNA assays needs presenting in detail or references provided to detailed validation – accuracy at different densities, reproducibility, linearity, criteria for limits of detection etc.

b) The volume of blood taken and assayed needs stating.

c) Validation of gametocyte quantification needs support – particularly with reference to stability of transcript numbers per cell and any assumptions made in the derivation of a gametocyte density (see reviewer 2 comments).

3) Details of statistical analysis performed and reporting of results of the analysis are inadequate. See comments from all three reviewers for more details. The response should include addressing reviewer 2's concerns about modelling the decline in gametocyte densities. It would also be helpful for authors to provide the code used for data analysis as recommended in eLife's transparent reporting form.

4) The CONSORT guidelines for trial reporting should be followed (see reviewer 1 comments).

5) More details of the membrane feeding experiments need to be reported (see reviewer 1 and 3 comments).

6) Figures 2, 4 and (ideally) 5 should be improved to better convey information (see reviewer 1 and 3 comments).

Reviewer #1:

Deliberate infections treated with SP and piperaquine have been shown to be followed by gametocytaemia. This paper reports a small study with 16 participants with the objective of determining which of four drug combinations work best for inducing gametocytaemia in CHMI.

Introduction, last paragraph. The aim is to "induce stable gametocyte carriage". What is considered to be stable is buried as a footnote to Supplementary file 1. The optimal characteristics (density, duration) are also implied rather than stated.

The primary study outcome (subsection “Study outcome”) is prevalence of gametocytes by Pfs25 qRT-PCR. Was this the presence of female gametocytes at any of the twice daily measurements from day 6?

The sample size calculation (subsection “Statistical analysis”, first paragraph) appears to set the bar very low. Even so, I could not quite reproduce the calculation: an exact binomial 90% confidence interval for 6/7 would have lower bound 47.6%. It might be that you used an approximation, but since the numbers are small an exact CI seems more appropriate. Why did you choose a 90% confidence interval rather than the more conventional 95%? (with 95% CI, the lower bound for 6/7 would be 42.1%). The numbers are very small, and nowhere is it really explained why more data would be hard to collect.

There was an odd dissonance between the simple comparisons for hypothesis tests (ANOVA, Fisher's Exact test) and a more sophisticated analysis to "identify which study arm potentially deviated from the others". I'm not sure what this involves since few details were given, but it includes a prior for R^2 which seems unintuitive, and, given the limited sample size, could be stretching the data further than it can bear. It was also written without clarity in the Results e.g. "96.5% probability of being the highest" – the LD-PIP/SP mean was anyway the highest in the trial. Do you mean the chance of the population mean of LD-PIP/SP being the highest?

It would be useful to briefly state the assumptions in the previously developed model to estimate the gametocyte half-life.

It is not obvious that the AUC is the most useful measure – a short spike in gametocytes could be equal to longer low-level gametocytaemia. Clarification of what the optimal characteristics for drug development are would help. The AUC as a measure may also suffer from the non-independence of each time-point from the previous time-points – from a high peak (which may have occurred by chance or not due to the drugs), then further high values might tend to follow. A suggestion only: it might be possible to take into account the non-independence between time-points and use all the data, by using a statistical time-series model with a lag from the asexual densities or a simple mechanistic model fitted to the data. You might need more than four participants per arm for that but you might also be able to borrow strength for some parameters.

The Results section focuses on differences between the arms but it is unfortunate that the AUC is the only reported measure of gametocytaemia which is (borderline) significant between the arms for gametocytaemia (or the other p-values are just not mentioned). Looking at the graphs, I think the effect is plausible, but there is very limited evidence due to the small sample size.

That three mosquitoes were infected cannot be interpreted without the numbers of mosquitoes fed (Results, fifth paragraph).

The male and female gametocytes were measured by different assays which may have different levels of detection. The results for the sex-ratio should be interpreted with caution.

The CONSORT guidelines for reporting should be followed for eLife. Since this is a phase 1/2 trial with a small sample of healthy participants, the most appropriate CONSORT guidelines would be: CONSORT 2010 statement: extension to randomised pilot and feasibility trials (http://www.bmj.com/content/355/bmj.i5239). The reporting guidelines cover design, randomization, intervention, sample size, bias, generalisability and access to the pilot protocol.

Given that the emphasis in the results is on the differences between arms, Figure 4, where all groups are combined, is not easy to interpret.

There is little mention of the next steps for the induced gametocytes. If they are to be used in testing interventions that reduce gametocyte development, how would they be used?

It is not discussed why the different combinations of drug might have different effects.

Reviewer #2:

This is a very interesting and informative study of Plasmodium falciparum malaria gametocyte dynamics which exploits the opportunities provided by the resurgence of interest in human challenge studies and the development of methodologies for sensitive quantitation of nucleic acid concentrations. In general this is a very good piece of work but more details on the validation of qPCR gametocyte quantitation are essential if it is to be published. If there is one disappointment it is the complete absence of reference to the early observations of gametocytaemia in human challenge studies – notably the work of Shute and Cuica whose conclusions were in broad agreement with the current paper. The earliest reference is from 1986.

A list of questions or comments in the order they appear in the manuscript:

1) "It is widely accepted that malaria elimination is unlikely to be attainable in the majority of endemic settings with currently available resources and tools". Perhaps this could be attenuated? Many think the obstacles are primarily political, organisational and financial.

2) "maturation of gametocytes takes place predominantly in the bone marrow".

3) The 3D7 "lineage" is well known, but it is also well known to be different in different laboratories! Perhaps a few additional sentences on this particular lineage would be valuable. In particular whether there is any evidence that serial passage through volunteers and these laboratory reared mosquitoes has altered its biological properties – notably infectivity over the years? Please also confirm wild type PfDHFR and DHPS and single copy plasmepsin 2/3.

4) "until malaria parasites were detected at a density of {greater than or equal to}5000 parasites per milliliter (Pf/mL) by qPCR or a positive thick blood smear" – – were any volunteers symptomatic at this density?

5) Piperaquine base or piperaquine phosphate?

6) Safety seems rightly to have been a major concern. Did anyone look at the ECG if metoclopramide was given to piperaquine recipients? Was there any additional QTc prolongation?

7) The section on parasite DNA and RNA quantitation needs considerable strengthening as it is the central component of the paper. This is important.a) The performance characteristics of the 18S DNA and mRNA assays needs presenting in detail or references provided to detailed validation – accuracy at different densities, reproducibility, linearity, criteria for limits of detection etc.

b) The volume of blood taken and assayed needs stating.

c) Validation of gametocyte quantitation needs support – particularly with reference to stability of transcript numbers per cell and any assumptions made in the derivation of a gametocyte density.

8) Bousema et al., 2010 is referred to – which if I understand correctly assumes a single first order decline in gametocyte densities. Is this justified? It would be valuable to describe, if possible, the residuals around the model fits and comment on any heteroscedasticity. This is particularly important considering that a major finding of this report is that male gametocytes appear to be cleared more rapidly than female gametocytes. If in fact the gametocyte clearance profile is more complex (e.g. multiexponential) then the lower density male gametocytes may appear to be more rapidly eliminated whereas, in fact, the slower terminal phase of elimination is below the limit of accurate detection. A similar problem has bedevilled assessment of the pharmacokinetic properties of slowly eliminated antimalarials.

9) It is not very clear what modelling approach was used to fit the model – was this a mixed effect model? Were any covariates incorporated – if so which? What programme was used?

10) Is there any explanation for the liver function test abnormalities?

11) "SP has long been associated with a rapid appearance of gametocytes that is too early to be explained by de novo gametocyte production upon drug pressure and has thus been hypothesized to reflect an efflux of sequestered gametocytes upon treatment". True – but it is not very clear from the text whether this study's results supports this hypothesis. Could the authors be explicit here? The implication is that such early released gametocytes should be more immature- and thus the period during which Plasmodium falciparum gametocytes are not infectious (after release into the circulation) should be longer in these circumstances. Is there any evidence for this?

12) "The highly abundant Pfs25 mRNA makes the female gametocyte qRT-PCR more sensitive than the male PfMGET qRT-PCR." Could this be elaborated upon- or at least referenced?

Reviewer #3:

This paper describes a novel controlled human malaria infection model that consistently achieves gametocyte carriage. This work is important with implications for understanding of P. falciparum transmission dynamics and broad significance for the future study of transmission blocking interventions.

The paper is, in most respects, clearly written. There are, however, some aspects of reporting where it is not entirely clear exactly what was done and why (particularly in relation to statistical methods).

Results, fifth paragraph. Details of these membrane feeding experiments are lacking from the Materials and methods. In particular, how many mosquitos on each feeding day? Even if full details are presented in the references describing the protocols for these experiments, it would be useful to summarise some of the key numbers in the manuscript to give the reader an idea of what these numbers mean. See also Discussion, third paragraph – "the very low rate". Since only the numerators are reported, there is no information on what this rate actually is.

Subsection “Statistical analysis”, second paragraph. More details need to be given here. What non-parametric tests were used and what exactly was the statistical model implemented in the Bayesian framework (code for this does not appear to have been provided). Also, the R package rstanarm is mentioned, but appears not to be acknowledged in the references. It probably should be along with the appropriate references for Stan and R.

Table 3 is confusing. Why are some adverse events listed twice in the leftmost column? Duration time units should be given.
