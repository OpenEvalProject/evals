# Peer review - Round 1

Editors:
- Anna Akhmanova, Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47003.sa1](https://doi.org/10.7554/eLife.47003.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Brand and colleagues present an agent-based model of respiratory syncytial virus transmission and vaccination and use it to explore potential vaccination schedules in pregnant women. They find up to 50% reductions in infant RSV infections with fairly high coverage of the prenatal vaccine. This work is important for informing future vaccination policy when RSV vaccines become available.

Decision letter after peer review:

Thank you for submitting your article "Reducing RSV hospitalisation in a lower-income country by vaccinating mothers-to-be and their households" for consideration by eLife. Your article has been reviewed by Neil Ferguson as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Katherine Atkins (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the current study Brand et al. use a mathematical model to estimate reductions in RSV hospitalizations in children following a theoretical maternal and >1 y/o vaccines. The study builds on much previous work conducted by members of the same group and adds an important dimension to the question surrounding RSV epidemiology and the potential for vaccination.

The authors find modest reductions in overall hospitalizations but a sizable reduction in hospitalizations in children <1 y/o – the most vulnerable group. It is encouraging to see the modelling being conducted with an LMIC setting too, as most previous RSV modelling efforts have been HIC-based. The modeling methods are sound (and elegant) but the manuscript would benefit from some clarification of both methods and results.

Essential revisions:

1) I think it would be helpful if more motivation were to be provided on the reasoning behind the household model choice. If I understand correctly, there is a serious computational downside of solving these types of models, at the expense of some epidemiological realism (with respect to neglecting exposure-dependent parameters, for instance). I'm not advocating the authors conduct a comparison, but I'm interested to know whether the choice of household model can ultimately reflect the impact of household-based strategies more accurately than a more epidemiologically-realistic model can using approximations for the mother-child contact (for this, see again, Atkins et al., 2016).

2) The paper needs to be grounded in relation to vaccines currently being developed. There is no discussion as of now of potential future vaccines and there should be to motivate the work.

3) From what I understand, the contact within the household is assumed to be density dependent, whereas the contact outside of the household is assumed to be frequency dependent – is this right? Could you mention this?

4) Hasn't there been mixing matrices conducted in Kilifi that could be used?

5) It is a big assumption that the demographics are fixed in the 10 years of prediction. The birthrate has been declining in Kenya over the past 15 years (see https://www.indexmundi.com/g/g.aspx?c=ke&v=25). Thus, the reported reductions may be over-estimated.

6. I'd like to have a comprehensive parameter table that describes all parameters used (vaccine duration, uptake etc. – including fitted parameters). This would help in understand the base case scenario – which was difficult to find as well as the reliability of the model and deviation from previous work.

7) Figure 2 suggests to me that the model underestimates the number of hospitalisations. It would be useful to see the absolute numbers stratified by age (rather than just by% ).

8) Figure 5A: It is extremely surprising to me that the post-vaccine dynamics immediately equilibrate – do the age distribution infection also equilibrate immediately? Presumably, but this is also surprising.

9) Figure 6: I can't decipher what these combined strategies are – we need more information in the caption accompanied with a separate table that spells out which vaccine strategies are being considered. It is very difficult to interpret the differences between the strategies otherwise.

10) Does Figure 6 really report avoided hospitalizations? If so, why do avoided hospitalizations go down with increasing coverage? Also, I would suggest reversing the order of the legend to match the order of the lines.

11) Introduction: I'm not sure I agree with this assessment. Admittedly in the context of pertussis, but nevertheless, our modelling study suggested the benefit of cocooning in the presence of direct protection of the infant was extremely marginal (Atkins et al., 2016). That is, in terms of impact, there was no point in cocooning when substantial direct protection had been achieved.

12) Results section: Where are the derivations for the equations in box 1? They are not immediately obvious.

13) Results section: I'm a little sceptical at both the values of R0 and the conclusions drawn, namely that community transmission has an R0 < 1 (on average an infection initiated at random) produces <1 other case in the community). This is because when R0 is calculated from a model, the structure of the model, as the authors note, can substantially impact the value of R0 calculated. While the authors note the difference between age and household related structure, the number of exposure classes will also make a difference I think. Perhaps the authors can comment on this.

14) Materials and methods section: Originally you said you split up <1 and >1 years, but there is discussion of finer age groups here, this needs to be explained more clearly as I'm confused with the age stratification, its parameterisation and how it was implemented in the model.

15) Subsection “Conditional age of individuals”: When you say 'we calculated empirical distributions', it's not clear how you constructed these distributions, or how they were 'empirical' – more information please. Presumably there are parameterised from the KDHSS survey, but it's not clear. More link between the data and the distributions needed I think.

16) Subsection “Hospitalisation rates”: I think I understand what the authors are trying to do here – there needs a little bit of a fudge to account for the exposure-dependent nature of RSV infection that is missing from the model. However, there are two forces at play here, which I think need to be captured independently. First, is the age-specific nature of infection – evidence points to severe infection / hospitalisation being necessarily age dependent, when the lung pathways are not fully developed and infected infants are more at risk of bronchiolitis than their older counterparts. (arguably very young infants are also more likely to be picked up in surveillance through increased testing and reporting). There is then the exposure-dependent nature of infection, that is the higher chance of asymptomatic infection with increasing exposures. Thus, with passive protection from either extended life monoclonals or by maternal vaccination, the idea is to push infants out of their most risky period (age-dependent severe infection), with the trade-off that no vaccine- or natural-immunity is elicited and they still have the same risk of symptomatic infection as younger individuals. If I understand correctly, the model captures the latter mechanism, but not the first. More clarity is needed on distinguishing these phenomenons I think.
