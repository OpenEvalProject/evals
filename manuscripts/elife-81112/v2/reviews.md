# Peer review - Round 1

Editors:
- Tâm Mignot, https://ror.org/035xkbk20 CNRS-Aix Marseille University France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81112.sa0](https://doi.org/10.7554/eLife.81112.sa0)

This fundamental research significantly enhances our comprehension of the influence of substrate physical properties during the initial stages of biofilm development. By integrating microfluidics, single-cell motility, and modeling, the study provides compelling proof that mechanical interactions between the substrate and Type-IV pili drive these phenomena. This work is likely to attract a wide range of readers interested in micro-communities, their structure, and ecology.


---

# Peer review - Round 1

Editors:
- Tâm Mignot, https://ror.org/035xkbk20 CNRS-Aix Marseille University France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81112.sa1](https://doi.org/10.7554/eLife.81112.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Substrate stiffness impacts early biofilm formation by modulating Pseudomonas aeruginosa twitching motility" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Tam Mignot as the Reviewing Editor and Arturo Casadevall as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors conclude that motility changes are not due to physiological changes resulting from surface sensing, but rather that mechanical properties of the substrate are responsible for modulating motility differences. However, this conclusion is derived partly from the use of a chpA mutant, which the authors' data demonstrate does not exhibit differences in motility compared to WT. These data are very surprising given that several published studies demonstrate a defect in both pilus synthesis and twitching motility in PilChp mutants (including chpA). It is unclear what the differences are between the presented study and the published literature leading to the disparity in these results.

There are a number of phenotypes linked to the chpA mutant strain: are the authors observing them with the strain they used? What actually is the level of pili in the strain they manipulate? In addition, to confirm this very surprising result, it would be important to repeat it with a pilG mutant (PilG regulation by ChpA phospho-transfer drives much of the PilChp signaling pathway, so this would be a nice way to validate the surprising results shown in figure S6). This is a critical control considering the kinetic modeling and the conclusion that this phenomenon is purely mechanical is based on this result. Should the authors obtain similar results for a pilG mutant, it would be important to incorporate some discussion about what may be leading to the observed differences.

Other revisions:

– The authors conclude that twitching motility plays a key role in the rigidity modulation of microcolony formation by PA on soft elastic substrates based on data shown in supplemental figure 4. It would be nice to see confirmation that the colony morphology does not change in T4P mutants on the softest substrates (2.7 kPa pads) as a control.

– The jump in timescale needs to be better explained. Local speeds of roughly 1 um/s turn into effective speeds of um/min when one looks at a frame rate of one per minute. This might be just a reflection of the random nature of the motility but should be better explained in the text and the model. On a general note, one of the difficulties in navigating the paper as it stands is the definition of many parameters in a global manner as fits from derived equations whose assumptions are not always fully validated. For instance, Equation (1) assumes no new addition because of the flushing of the channel with the clean medium. Yet the first peak of residence time on 2.7 kPa gels is around 5 minutes per Figure S7 whereas the calculation of Vg is done over 100 minutes which should leave plenty of time for detachment and reattachment of bacteria upstream of the recording field of view. Similarly, the definition of Vcm is not easy to follow or apprehend. Is it that the general averages of the velocities are too noisy?

– The subtraction of the average velocity of the pilA mutant directly in Equation 10, could be warranted, but it would also require a little bit more explanation. All in all, a better effort in the explanation of the pros and cons of the data analysis choices will go a long way in making the article readily understandable for all. Presenting other more straightforward ways of extracting the different parameters (direct averages, choice of cut-offs…) will be helpful even in only supplementals. Another instance of assumptions that could also suffer some outliers is the assumption on line 141 that bacteria move along their long axis as it has been shown that in liquid, they can move perpendicular to it (Gibiansky et al. Science 330(6001):197).

– While the simple kinetic model presented does encapsulate many of the aspects of the data in an understandable way, some of the assumptions should be discussed further. The assumption that pili only binds with its tips is reasonable but it is very strong. While this assumption allows many simplifications in the model, type IV pili can potentially bind throughout their length, and as they can be microns in length, so can the binding region. The Koch et al. 2021b does go over the reasoning but having a small discussion earlier in the paper would be great.

– The formation of biofilms in a constant flow channel is a well characterized and common technique, yet it would be important to mention that it might be a condition quite remote to conditions found by bacteria in their common environment where the renewal of nutrients and environment might not be controlled. A small discussion around this theme might be nice.

– It could be interesting to discuss the rather large errors on different estimates of the parameters found (Vmax, E0 particularly).

- In Figure 1 and in a few figures: the 4 stiffnesses used (2.7, 18.5, 65, and 84 kPa) are not always all presented and sometimes in a non-matching set, as in Figure 1. That would be great if this could be corrected.

Text:

– The authors refer to the clusters of single cells measured in this study as colonies; this is a bit confusing since colonies generally refer to macroscopic scale (visible to the naked eye) colonies on plates. I suggest changing instances of "colony" to "microcolony" for clarity throughout.

– There is a typo in the figure legend of supplemental figure 4 and main text figure 4; it should read PAO1 pilA::Tn5 (two colons instead of one).

– The authors have a "data not shown" statement in the legend of supplemental figure 8; they should include the data (can be in the same figure, but should be shown instead of just referenced).

– Dephine instead of Delphine in the authors' names line 5.

– 85 kPa instead of 84 on page 6 of the supplemental in the legend.

Reviewer #1 (Recommendations for the authors):

– The authors conclude that twitching motility plays a key role in the rigidity modulation of microcolony formation by PA on soft elastic substrates based on data shown in supplemental figure 4. It would be nice to see confirmation that the colony morphology does not change in T4P mutants on the softest substrates (2.7 kPa pads) as a control.

– The authors demonstrate in supplemental figure 6 that chpA mutants have similar Vg on stiff surfaces compared to WT (figure 2C). This result is very surprising considering PilChp mutants are known to be defective in pilus synthesis and twitching motility (Bertrand et al. 2010), yet pili are presumably driving the motility seen here. To confirm this very surprising result, I would like to see it repeated with a pilG mutant (PilG regulation by ChpA phospho-transfer drives much of the PilChp signaling pathway, so this would be a nice way to validate the surprising results shown in figure S6). This is a critical control considering the kinetic modeling and the conclusion that this phenomenon is purely mechanical is based on this result. Should the authors obtain similar results for a pilG mutant, it would be nice if they incorporate some discussion about what may be leading to the observed differences.

– The authors use "typical pilus retraction speed" of 1 um/min, but this has been measured in PA to be 0.5 um/min (Skerker and Berg 2001). Would this value change result in differences in the authors' model?

Reviewer #2 (Recommendations for the authors):

As a follow-up on the point 1 in the Public Review: The subtraction of the average velocity of the pilA mutant directly in Equation 10, while maybe warranted, would require a little bit more explanation. All in all, a better effort in the explanation of the pros and cons of the data analysis choices will go a long way in making the article readily understandable for all. Even presenting other more straightforward ways of extracting the different parameters (direct averages, choice of cut-offs…) will be helpful even in only supplementals. Another instance of assumptions that could also suffer some outliers is the assumption on line 141 that bacteria move along their long axis as it has been shown that in liquid they can move perpendicular to it (Gibiansky et al. Science 330(6001):197).

– The formation of biofilms in a constant flow channel is a well characterized and common technique, yet it would be important to mention that it might be a condition quite remote to conditions found by bacteria in their common environment where the renewal of nutrients and environment might not be controlled. A small discussion around this theme might be nice.

– It could be interesting to discuss the rather large errors on different estimates of the parameters found (Vmax, E0 particularly).

– In Figure 1 and in a few figures: the 4 stiffnesses used (2.7, 18.5, 65, and 84 kPa) are not always all presented and sometimes in a non-matching set, as in Figure 1. That would be great if this could be corrected.
