# Peer review - Round 1

Editors:
- Neil M Ferguson, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27694.044](https://doi.org/10.7554/eLife.27694.044)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The intractable challenge of evaluating cattle vaccination as a control for bovine Tuberculosis" for consideration by eLife. Your article has been favorably evaluated by Tadatsugu Taniguchi (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers thought the work to be important and of broad interest, but each raised a number distinct and important major issues which need to be addressed in a revised submission. In addition, all reviewers found the current manuscript overlong and lacking in clarity. We would urge greater selectivity in presenting key results, and a substantial overhaul (and shortening) of the main text of the paper. Additional analyses and detailed methods can be included as supplementary information.

The reviewers also raised concerns about how study power was considered, and the issues of likely attack rates in transmission experiments and extrinsic infection rates should also be given particular consideration, in addition to the other detailed comments made.

Reviewer #1:

This paper explores an important topic – how to test the efficacy of a bovine TB vaccine – using simulation models of TB transmission to test different trial designs. Overall, the analysis seem rigorous to the extent I could judge it, but ambiguity or missing details left me with several significant questions. The presentation of the paper is far from ideal overall – it is much too long, difficult to follow, and lack of required detail in the Materials and methods means it is not always clear how results have been derived. Really the paper needs major reorganisation, with a (much) shorter and selective main text, then a more detailed supplement to detail methods, parameterisation and sensitivity analyses.

Issues:

- Subsection “Review of estimated cattle-to-cattle transmission rates for bovine TB” is critical – the failure of the AHVLA experiment fundamentally calls into question the feasibility of experimental studies of vaccine efficacy in the UK context. This really needs to be highlighted up front in the paper (not just in the Materials and methods). I note the authors contention that increasing group size and the proportion of the group initially infected would likely substantially increase infection rates, but given the cost of such studies and the need to demonstrate that the results will likely transfer to the field setting, I would suggest that funding any large-scale transmission study should be contingent upon achieving a higher attack rate in a small pilot (e.g. 50 animals, 25 infected, 25 uninfected). Such a pilot would also give invaluable data with which to better power future vaccine studies.

- How exactly are the expected values plotted in Figure 3A (and like figures) being estimated? No details are given in the Materials and methods. I'm guessing it is the average of the estimated VE over a large number of simulations of the experimental transmission study of X herds? How was VE calculated – using the expressions given in Figure 1? Giving some representation of the 95% range of the estimates from single experiments would be useful.

- Likewise, how exactly are the estimates of power calculated in Figure 3B? I presume from their simulations? In doing so, are they also simulating a 2-level analysis of the simulated trial results (i.e. accounting for variation between herds)? What primary end-point is being evaluated – a difference in attack rates between vaccinated and control herds, or estimation of VE to some level of precision (e.g. +/-0.05). I would suggest the latter is more useful. i.e. for a fixed set of assumptions about VE, run 1000 simulations of the trial in X herds, and count the number of simulations, Z, for which the desired measure of efficacy is estimated to within +/-0.05 (say) of its true value. Power is then Z/1000.

- "Clearly the latter methods have a higher power and that is the method that is used for estimation and calculation of the post-hoc power from the simulation studies described below (A4)". I am confused. What does A4 refer to? Which tables and figures use the FS based approximate analytical calculation and which use direct simulation? Precise details of how vaccine efficacy and power was calculated from simulations of the experimental design should be given. I don't frankly see that the analytical approach in the subsection “Sample size calculations for natural transmission study” adds anything very much. Given any experiment must have a fixed duration, what is important is the net attack rate seen in the vaccinated and control animals over the duration of the experiment. This depends on the transmission rate (and how that varies as a function of the time from infection) and the duration of the study phases (i.e. contact time). Going from transmission rates to R and back confuses things, at least for me. I would rather see Figure 10 show the posterior distribution for transmission rate (including the herd size factor), therefore. This would be more informative than the estimates given in Table 12. It would also allow Figure 9 to be removed – which doesn't add anything informative beyond Figure 11 in my view – indeed the addition of the red vertical dashed lines to Figure 9 is confusing.

- Continuing in the same vein, the paper gives the impression that Table 11 is driven by the results of Table 10, which misses the subtleties of Figure 11. This latter figure is the most interesting in the paper, but I didn't understand some of the trends in Figure 11. Why does increasing contact time decrease power (for fixed group size) for some model variants and vaccine efficacies? I can only assume this is because infection rates are saturating in both groups. However, if the experiment was analysed making use of all the DIVA test results in a survival analysis, this shouldn't matter – the higher infection hazard in the control group animals should still be resolvable in the first phase, and the lower infectiousness of the vaccinated animals in the second phase. As I've said above, the authors need to give precise details of how power is being estimated from the simulation for Figure 11 (see above) – how are the (simulated) experimental results being analysed, what is the trial primary end-point (i.e. what statistical test is being examined when calculating power)? Again, given the cost of such experiments, analysis needs to make best possible use of the data collected – which survival analysis is more likely to achieve than simple comparison of final attack rates.

- In the first paragraph of the subsection “Group size and duration of transmission studies under different transmission scenarios” – What are Figures B3 and B4 and what is Table B1? Assuming Table B1 is actually Table 12, how are the values given in that table used to generate Figure 9 on? In particular, were the first 2 rows of Table 12 used for any simulations, or just the Conlan et al. estimates? As mentioned elsewhere, I would drop the Conlan 2012 results – presumably they were superseded by the 2015 ones, and they give rather optimistic results for the trial contact times.

- Table 11, 25% effect size – the bottom-most rows have a group size of 800, while this group size isn't mentioned in Table 10. Is this a typo? As commented below, I don't feel including all the 2012 model variants adds anything here.

- The second paragraph of the subsection “Comparison of field estimates of cattle-to-cattle transmission rates” is unnecessary. Presumably the 2015 models are preferred, so reference to and results relating to the 2012 model (half of Figure 8, Figures 9, 11, Figure 11—figure supplements 2, 4, half of Table 11) can be removed.

Reviewer #2:

This paper is a well written, thorough and painstaking analysis of a narrow technical issue, sample size calculations for a hypothetical trial of vaccination to protect cattle from bovine TB. It is a substantial and technically useful piece of work, though not easily generalizable given the specific and complicated details of bovine TB epidemiology and management in the UK.

I agree with the statement (subsection “Conceptual design to estimate vaccine efficacy and herd level effectiveness”, fifth paragraph) that it is important to evaluate the impact of vaccination on infectiousness as well as susceptibility – as a rule the former is ignored.

The prediction that there would be, in the situation modelled, only a very small indirect impact of vaccination means that very large sample sizes would be needed for a trial to detect it. The situation modelled includes current test and slaughter practices, but presumably if a vaccine were to be used it would not be used in conjunction with these. If it was, as is spelt out later, the additional benefit would be very small and presumably not cost effective. Or is that the point the authors wish to make? Either way, a vaccination-only scenario would be of interest (regardless of current EC requirements).

The way statistical power is estimated (more than "slightly" unusual in my view – Discussion, third paragraph) also makes the study less generalizable. It would help to set out what efficacy we are looking for, greater than zero seems a very low bar. (What's more, the subsequent discussion about the DIVA test implies that even if the vaccine itself had zero efficacy there would be some effect of the more sensitive test – Discussion, sixth paragraph). These impacts could be partitioned by varying parameter settings appropriately.

The role of extrinsic infection (Discussion, eighth paragraph) could also be explored more systematically. The issue of testing efficacy locally when the ultimate aim would be to intervene over a whole population is problematic for many intervention trials for infectious disease.

Overall, I felt that, though a rather daunting volume of results are presented already, more could have been done to dissect out the likely multiple contributors to the low efficacy anticipated in a herd level vaccination trial.

Reviewer #3:

General Comments/Suggestions:

This manuscript describes the adaptation of previously published models to understand how field trials might (or might not!) detect the benefits of a bTB vaccine deployed in Britain. In general, the methods and conclusions seem sound, and represent an important warning on relying on these sorts of trials. I did have some problems understanding the interpretation results shown in the figures associated with this manuscript, and I suspect that some figures may not be referred to correctly. I have included some suggestions below on how to make the figures more easily readable. The mathematical typesetting in the manuscript also made it somewhat less readable – typesetting that sets apart mathematical entities like R and R0 more clearly would have helped me, and would also have limited confusion when "R" is used both as a reproduction parameter, and as a compartment (e.g. in the SORI model).

Because this work is based on mathematical modelling, I would urge the authors to make as much of the modelling code as possible available on a public repository, or provide links to the previously-published code used. Publishing code in this way makes the work much more reproducible.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "The intractable challenge of evaluating cattle vaccination as a control for bovine Tuberculosis" for peer review at eLife. Your revised article has been favorably evaluated by Tadatsugu Taniguchi (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

Please review the major comments of reviewer #1 (the Reviewing Editor), which center on the interpretation of your results and their relevance for policy. We would then ask you to respond within the next two weeks with your views on how justified you feel these comments to be, and an action plan and timetable for the completion of any additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

Reviewer #1:

The rewritten paper is much clearer and more comprehensible. My few technical comments are detailed below. I do have more major issues with the conclusions and tone of the paper however:

- Given the problematic experience with previous transmission experiments, my own conclusion from reading this paper was that relatively small field trial of 200 herds would give valuable information about the likely veterinary health impact of vaccination at the individual animal level (but that a trial with 500 herds would be needed to measure herd-level effectiveness).

- Data from an experimental study is fundamentally different in quality than that from a randomised field trial. In human public health, the former might be viewed as equivalent to a pre-phase II human challenge study, which gives proof of concept. It does not guarantee that the results can be read across to the natural setting – which is why phase III trials are still needed.

- The authors seem unnecessarily pessimistic about what their simulations imply for the feasibility of field trials, at least at the individual animal level. I interpret Figure 3 as showing that a trial run in 200 herds would have excellent power at measuring the direct effect of vaccination, and reasonable power at measuring the 'total' effect.

- Yes, measuring indirect effects is difficult, but arguably is addressable in a post-marketing (phase IV) implementation study.

- I think there are issues with a cluster-randomised trial with 50% coverage in each cluster (herd). Even for the vaccinated animals, outcomes will be different in a herd with 100% vs 50% coverage of a leaky vaccine. Plus, presumably the goal for any widescale vaccination policy would be 100% coverage? A 3-arm trial with herd level vaccination coverage of 0, 50% and 100% in the three arms might be more informative. Comparing attack rates in the 0 and 100% arms would give a measure of total effect (the most important outcome). Comparing vaccinated animals in the 50% and 100% coverage arms and unvaccinated animals in the 50% and 0% arms would give more information (and therefore power) to differentiated impacts of vaccination on infectiousness and susceptibility.

- Appendix 2 on whole-herd effectiveness is interesting and critically important (to the extent I would much rather see this in the main text and the discussion of experimental transmission studies in an appendix) – and in my view calls into question the whole viability of vaccination, if the overall impact on herd breakdowns is really only likely to be in the range of 10-20%. Putting that (major) issue to one side, the results in this section also highlight the potential benefits of a 3-arm design.

- Regarding the discussion of bias in RR measures – it is unsurprising that such measures underestimate εs – it's the difference between comparing a hazard with a cumulative hazard.

- Indeed, Figure 3 (and the supplementary version) seems to show that one could use models to quite reliably go back from the measured relative risks to the underlying effect of vaccine on susceptibility – albeit not on infectiousness. – Figure

Reviewer #2:

The first round of reviews seems to have picked up a large number of errors and presentational issues. The authors have addressed these fairly comprehensively and the manuscript is greatly improved as a result. If the topic is thought appropriate for eLife then I recommend that the manuscript is now acceptable for publication.

Reviewer #3:

In general I am satisfied with the re-organisation and changes made. I find the manuscript is more focused and easier to get through in its current form. I still find the Appendices somewhat arduous, and would encourage the authors to consider any last-minute changes they can make to streamline them, but I accept that sometimes Appendices with technical content can be long.

I was a bit disappointed that the authors felt they could not address the impact of the distribution of latencies on the design, but accept their justification that, with the very high level of uncertainty on these distributions, they do not want to "muddy the waters" in this already very long submission.

I appreciate the links to public code repositories.
