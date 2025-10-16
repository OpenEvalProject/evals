# Peer review - Round 1

Editors:
- Sarah E Cobey, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78770.sa0](https://doi.org/10.7554/eLife.78770.sa0)

Han et al., analyze sequences from randomly sampled COVID-19 cases in the Netherlands to understand the impact of flight restrictions on the importation of SARS-CoV-2 variants. In line with prior observations and common wisdom, they find that targeted flight restrictions were not effective at preventing introductions of new lineages and that their early spread in the Netherlands was sustained by urban centers. These useful findings, based on unusually strong sequence collection techniques, can inform surveillance policy and improve basic understanding of the spread of SARS-CoV-2 variants.


---

# Peer review - Round 1

Editors:
- Sarah E Cobey, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78770.sa1](https://doi.org/10.7554/eLife.78770.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Regional importation and asymmetric within-country spread of SARS-CoV-2 variants of concern in the Netherlands" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please streamline the narrative arc and logic of the paper. The reviewers questioned (including in the consultation session) what the estimation of variant growth rates adds to the analysis. It seems important to emphasize that the qualitatively estimated impacts of flight bans are if anything underestimated here, given other concurrent NPIs; please clarify which restrictions were in place. Please also see Reviewer 2's comment on the role of nightclubs.

2) There were technical concerns about the soundness of the results. It appears as though only one chain was used; several are traditional and safer. Biases might be introduced by the use of a strict vs. relaxed clock. A discrete phylogeographic model would be more appropriate. These improvements would lend greater confidence to the results. There should also be some treatment (at least in the Discussion) of the potential impact of sampling biases (inside and outside The Netherlands) on the results.

3) The reviewers found many of the figures confusing or unhelpful. Please revise them in light of the suggestions below.

Reviewer #1 (Recommendations for the authors):

1. I realize this is pretty foundational to phylogeographic methods (and welcome being referred to a textbook or classic paper I have missed), but how sensitive are the results – e.g., estimates of importation from ground travel/various areas---to sampling biases? For this question, I'm mostly thinking about deliberate subsampling biases (e.g., 2:1 Netherlands to non-Netherlands).

2. I'm curious about the potential magnitude of these effects due to biases in case ascertainment that might be poorly understood. In the U.S., there were many-fold differences in populations' access to testing and probability of being reported as a case, conditional on infection. These differences had strong socioeconomic and spatial associations. It seems deeply misleading to me to describe the sequencing as "random." It's not, unless case identification was random, which it wasn't. Maybe you could say something like "sequences were collected from a random sample of cases." But it would be good in the Methods and maybe the main text to describe exactly what is known about case ascertainment biases in The Netherlands over the study period, and the potential impacts of case ascertainment biases within The Netherlands and between countries on the estimated flows.

3. There's one mention of flight bans but otherwise "restrictions" is used. It would be useful to describe the restriction/ban on air travel precisely for people less familiar with the policies.

4. The github repo needs better documentation and structure to ensure reproducibility.

Reviewer #2 (Recommendations for the authors):

I have found the manuscript in need of several improvements:

1. The focus of the manuscript is somewhat diffuse and at times misguided, where for example the analysis of SARS-CoV-2 introductions into the Netherlands seems fine, others are questionable like using continuous instead of discrete phylogeography, and the analysis of VOC growth rate differences feeling a bit pointless, especially in light of the narrative the authors seem to push regarding the role of nightclubs in SARS-CoV-2 transmission. The authors should rethink the structure of the manuscript and what they want to say with it. If it's finding that travel restrictions do not achieve their goals – perfect! But adding analyses to beef up the manuscript afterward doesn't add much to the story.

2. There are a couple of technical issues that should be addressed. Firstly, all Bayesian MCMC analyses describe a single chain which is not standard. Ideally, at least two independent runs are expected for any MCMC analysis. Secondly, some of the figures don't seem like they convey much information, e.g. Figure 1C, Figure 3, and the bottom panel in Figure 4, and their use should therefore be reconsidered.

Overall, the manuscript has potential but requires substantial effort to improve, starting with its scope.

As stated in the public review part I think the authors should reframe, and refocus their manuscript. I think a study on the ineffectiveness of targeted flight cancellations is worthwhile but I don't see the added value (or good justification) of using continuous (instead of discrete) phylogeography or the logistic regressions.

I should also say that the narrative being pushed about nightclub reopenings is very flimsy and potentially confounded with the Netherlands having an age-tiered vaccination programme with age groups being given access around June 2021. This is not mentioned at all in the text and offers an alternative hypothesis for the distribution of cases across age groups during the reopening. I understand the authors are officially not claiming that there is strong evidence for it but when it comes up more than once in the text and is part of the discussion I personally would like it to be backed up with more evidence and all caveats addressed properly.

Line 76 "The four aforementioned VOCs also emerged in the Netherlands" – 'emerged' is often understood as 'originated', better to say 'arrived to' or 'dominated' here.

Figure 1A – Middle panel should say "Lineage proportions" for clarity, consider labelling each dominant area with the lineage that it represents since the legend in Figure 1C contains too many colours.

Figure 1A – The bottom panel should say "Mobility change (percent)" to make it intuitive.

Figure 1B – I have a personal preference for neatly-delineated colour maps and it's up to the authors if they want to change the limits between incidence and sequences so they're, for example, multiples of 20s and 500s, respectively.

Figure 1C – Not sure the tree is adding much here.

Line 143 "and continued to accumulate in frequencies" – change to 'frequency'.

Figure 2 – Worth shading European states with good sequencing programmes with a similar hue? Are those countries not flying passengers in?

Figure 3 – This figure is so messy perhaps it's not worth using? If the authors are dead-set on having some representation of migrations maybe there are better ways of doing it rather than a mess that says "there's a lot of movement"?

Figure 4 – Panel B is not labelled.

Geographic diffusion analyses indicate that more populous regions in the Netherlands play a large role in virus introduction and dissemination but surely this is entirely expected, given that such areas host transportation hubs for introductions and have more hosts to seed other areas.

Line 278 "locatthed" -> "located".

Paragraph 2 of the discussion contains passages that are more suitable for the Results section.

A very large dataset is analysed in BEAST so why did the authors decide to not use a relaxed clock and infer the rate naively? I find it very hard to believe that a dataset spanning close to a year would not have a temporal signal to inform the rate.

In all MCMC analyses, only one MCMC chain is mentioned. I'm sure the authors are aware that most studies are expected to run at least two independent ones, particularly with complex data like these.

Reviewer #3 (Recommendations for the authors):

1. Line 53: "Coronavirus-19 disease" should be "coronavirus disease 2019".

2. Line 88: samples were randomly selected for sequencing, not genomes.

3. Variants of concern (VOC), variants, and genotypes are used interchangeably. It would help to just pick of these and use them consistently.

4. I have a few suggestions regarding the visualization of Figure 1:

4.1. I would suggest using the Pangolin lineages as labels in panel C, and only list variants that are the focus of the study (all other lineages can be listed as "other").

4.2. The colors for 20D, 20I, 21A, 21I, and 21J are very similar (same in Figure 4). I would suggest using more distinctive colors to make it easier to see which color represents each of the variants.

4.3. It would be helpful to indicate the first detection of Α, Β, Γ, and Δ in Figure 1a.

5. Line 129. Did S Gene Target Failure (SGTF) influence the first detection of Α?

6. Figure 3. Panels B and D are hard to read, and may not be necessary to include. The advantage of only showing panels A and C is that their size can be increased.

7. Discussion. It would be helpful to start the discussion with a summary of the main findings. As raised before, I am not sure if the effect of international travel restrictions can really be distinguished from other interventions. Moreover, as Omicron was not part of the current study, I would refrain from speculating on the impact of those targeted flight restrictions as it is outside of the scope of the current study.

8. Limitations of the study are missing in the discussion.

9. Line 278: "locathed" should be "located".

10. Line 310. Methods lack a description of the used nucleic acid extraction method and diagnostic assay. Methods should also include a description of the used bioinformatics pipeline with specifics for how consensus genomes were generated (e.g. minimum depth and minimum frequency threshold to call consensus).
