# Peer review - Round 1

Editors:
- Prabhat Jha, Saint Michael's Hospital , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23061.019](https://doi.org/10.7554/eLife.23061.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Modelling primaquine-induced haemolysis in G6PD deficiency" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Prabhat Jha as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Dennis Shanks (Reviewer #2).

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper needs to cite all available data and not the selected sources currently used. Some specifications about the genotypes and regimes need to be improved.

Essential revisions:

Reviewer #1

I've taken a quick look at the paper. It's not an area I know about, but the basic biology seems to have been described fairly clearly. The modelling is interesting and seems convincing but is a bit short on details. In particular I'd like to know:

a) More evidence that the five studies identified really capture the entirety of the useful literature – could they point to a recent literature review or even a commentary (or do a rapid review of their own)?

b) More information about the model fit/validation in Figures 2,3, particularly since the data represent individuals with a range of G6PDd variants. What algorithm did they use for the fit (they mention least squares but that is just a vague term for a large class of fitting methods), what parameters were used (and what produced by the fit), and do the resulting parameters correspond to what we know about genetic variation (and indeed geographic variation in treatment etc.)?

c) Given the variation in the historical studies, in what way were they used to generate priors for the MCMC algorithm? (It would be useful for the prior and posterior distributions to be shown, including the joint distributions and measures of association for the posteriors)

d) For the results, it would be more useful to present them in probabilistic terms rather than show multiple lines on a graph (and in some cases ignore uncertainty entirely).

Reviewer #2

The manuscript reviewed concerns mathematical modeling of an important severe adverse event seen during vivax malaria treatment with primaquine. Unlike most modeling papers this manuscript has a firm, practical conclusion in the form of an alternative dosing regimen. I also found the paper much more accessible than other modeling papers however I would state that I am not a modeling expert and the editor should have the manuscript reviewed by someone with such expertise. The numbers match clinical reality as I perceive it, but someone needs to check how the figures were generated. The conclusion that the proposed regimen needs to be tested in a clinical trial is rational and fully supported. It seems likely that the large Mahidol Oxford group is already doing so and if a clinical trial has been initiated something to that effect should be inserted into the Discussion.

If possible, it is important to ground a model in reality which is done by using all the available data. The authors do so and the sparse data is rather a comment on how little has been done recently on primaquine. This model would not have been possible without the same group's recent weekly primaquine study (Kheng et al., 2015) done in Cambodia. The best available estimates from mass drug administration programs in China in the 1970s and returning US military in the 1950s suggest that the Severe Adverse Event (massive hemolysis) rate is about 1:10,000. Could the authors insert these historical studies into their model to determine if this estimated rate matches what the model generates using 22.5 mg daily for 10 days (China) and 15mg daily for 14 days (US military)? This is certainly not essential but would be a good addition if it was in the realm of statistical possibilities.

If the suggested revised primaquine regimen passes a clinical trial, then this particular modeling exercise will be exceptional in having delivered an actual advance in public health practice.

Reviewer #3

This paper addresses a pertinent limitation to the treatment of Plasmodium vivax malaria and proposes a novel treatment regimen for an existing licenced drug. The analysis revisits a largely forgotten idea previously suggested in the 1950s which could revolutionise how P. vivax radical cure is administered and potentially greatly increase access to treatment and hence reduce the burden of P. vivax malaria.

The paper presents a model framework which utilises the available historical data about the dynamics of primaquine-induced haemolysis in G6PD deficient patients. The parameterised model is then applied to simulate the haemolytic impact of different primaquine treatment regimens on G6PDd patients and concludes with a recommended optimal regimen which in most cases would not cross the limiting toxicity threshold (assuming the parameters defined here). The paper is clearly and logically presented, though I am not a modeller so may have missed some technical aspects of the model. I have a few remarks:

1) Cambodia dataset genotypes: Specify the genotypes of the G6PDd patients from the Cambodian study. If any of these were heterozygous it would mask the full impact of the haemolysis on hemi- or homozygotes. Heterozygotes should be excluded from the model fitting to ensure that the resulting model is a "worse case" model for individuals with 100% G6PDd RBC.

2) Anaemia: The recommended "regimen A" triggers an overall drop in Hb of 4g/dL. While this is a progressive drop, it is nevertheless considerable. The starting Hb* (steady state Hb conc.) has important implications for the safety of this haemolysis, and anaemia will be common among P. vivax patients. The Hb* conc. used in Figures 7 and 8 is the median value from the Kheng dataset, but Figure 4 shows there is wide variation around this. How are the Hb dynamics of the ascending regimens affected by a lower Hb*? Do the dynamics of the Hb drop differ or is it just a shift down the y-axis? The proposed "safety threshold" would be crossed if the starting Hb were 13g/dL or lower (which would be common), and an Hb*of <12g/dL could fall below the "limiting toxicity threshold". The issue of anaemia needs to be better addressed regarding the regimen's suitability for roll-out as a standard treatment.

3) The recommended regimen A has a total dose of only 375mg, while the opening statement of the paragraph "Safe optimal regimen" indicates that 420mg are necessary for radical cure. Further justification needed regarding the rationale for this discrepancy.

4) Aside from fears around drug-induced haemolysis, a major limitation to the current 14 day regimen is compliance. The proposed regimen A is 50% longer at 21 days. While this issue is beyond the scope of this paper, it should at least be acknowledged in the Discussion.
