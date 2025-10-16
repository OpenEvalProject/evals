# Peer review - Round 1

Editors:
- Isabel Rodriguez-Barraquer, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49058.032](https://doi.org/10.7554/eLife.49058.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Modelling the dynamics of Plasmodium falciparum gametocytes in humans during malaria infection" for consideration by eLife. Your article has been reviewed by Neil Ferguson as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this work, the authors have extended a within-host model of a P. falciparum infection to include gametocyte production. The model is calibrated to parasitaemia from 17 volunteers in a controlled human infection study. Although well thought out and well written, a number of concerns remain: (1) several clarifications need to be made in the description of the models; (2) additional justification is needed for the statistical validation of the results; (3) the section on predicting the impact of gametocyte kinetics seems poorly supported.

Essential revisions:

1) Model description

- a and t in the model are never defined (subsection “Study population and measurements”).

- Γ is never defined (subsection “Gametocyte dynamics model”).

- Where do the parameters ranges from Table 2 originate? Why are the death rates so high? For example, the maximum death rate of gametocytes is 0.1/hr, suggesting an average life span of 10 hours.

- Although never stated in this manuscript, it seems that the inoculum from the Collins paper was 2800 parasites. Discuss how the range of 0-10 parasites/mL relates to this.

- Vc, V1 and V2 are never defined (subsection “Pharmacokinetic model of piperaquine (PQP)”).

- How are the initial conditions of the drug model chosen? Why are there two spikes for some patients and only one for others (Figure 6—figure supplement 1)?

- In the fitting of the PK model, was only a single starting set considered? Why is it necessary and valid to increase the upper bound for qc? For different parameters, several patients hit the upper or lower bounds. In particular, Volunteers 105 and 20 hit the bounds on almost all parameters. Could their optimal fit be outside the range?

- Justification for all parameter choices and ranges, specifically when the fitted parameters fall on the bound of these ranges is necessary. If there is a specific biological reason to keep the bounds as they are that should be noted. If there is not a biological reason, the bounds should be widened to show that the parameters fitted, and thus the major conclusions, are not impacted by their choice of bounds.

- Throughout the paper there is discussion of "sexual commitment rate" but reference is always to the percentage commitment. That distinction should be clear and consistent throughout the manuscript. (See Table 1; subsection “Predicting the impact of gametocyte kinetics on human-to-mosquito transmissibility”; Figure 4CD axes labels; Discussion section; Table 2; subsection “Fitting the model to parasitaemia data”; Figure 1—figure supplement 15A axes label; Figure1—figure supplement 1 caption; Figure 1—figure supplement 2 caption; Figure 1—figure supplement 10 caption).

2) Statistical quantification in subsection “Model fitting and validation”, can "very well" be quantified? Can "excellent predictive" be quantified? Also, "very persistent" seems in contradiction of the previous paragraph of discussion of discrepancies. Why is there no discussion in the text of Figure 3? It seems a major point of the paper. How does one validate "visually capture the data" in the caption of Appendix 1?

3) Predicting likelihood of transmission. Although a reference is given for the choice of 108 parasite/mL for newly hospitalized cases, this number differs from the values seen in other important references (Eichner et al.,). For the non-infectious period, the 103 parasites/mL is listed as a value below which there is no transmission. As written in the manuscript it sounds like transmission is likely above this value. Furthermore, Figure 4 is confusing. What is the line in D? The only mention refers to when Gc=103, which is all of the values in D. The scaling (log vs linear) in these figures is confusing. Why use log on the fraction of sexual commitment? Why use linear on the Gc value?

4) Subsection “Predicting the impact of gametocyte kinetics on human-to-mosquito transmissibility” seem to suggest that, when determining the point during the infection at which the patient is hospitalised, total parasite density is a better indicator that asexual parasite density. This statement surprised me: a reference to Saralambda et al., 2010 is provided, but I can't find any mention of this. Have I understood the statement correctly, and is there any evidence of this? This is an important point, as the results presented in Figure 4 depend on the determination of the time of hospitalisation (which presumably is a proxy for the patient becoming febrile). The asexual parasite population is responsible for the rupturing of red blood cells every 48 hours, which is often linked to symptomatic malaria. The statement in subsection “Predicting the impact of gametocyte kinetics on human-to-mosquito transmissibility” seems to be contradicted in the Discussion section, which is a bit confusing.

5) In subsection “Gametocyte dynamics model” the authors state that piperaquine does not kill immature or mature gametocytes, although there is no reference for this. in vitro evidence (S.H. Adjalley et al., 2011) suggests that the drug does have some effect on very young gametocytes (stages I and II). I think it is reasonable to neglect these effects in the model, but less reasonable to state that there aren't any (I appreciate that I'm being a bit fussy here). Neglecting this drug effect may lead to an increased estimate for the death rate of immature gametocytes, but this is just speculation on my part and I'm not suggesting that the model should be re-fitted at this stage.

6) In Figure 2, several of the panels contain data points that look to be below the stated limit of detected (e.g. all data points after day 14 for Volunteer 202). I imagine that these represent zeros (data points for which the parasitaemia was below the limit of detection), this should be stated somewhere if so.

7) I'm a bit confused by the red line in Figure 4D. The caption of the figure states that, "The red curves indicate the cases corresponding to gametocytaemia of 103 parasites/mL". But my understanding of Figure 4D is that at every point (of the 2D surface) gametocytaemia has reached 103 gametocytes / mL. Have I understood this correctly? It could be that the red line on this panel is a contour of constant tc, which should be clearly stated if this is the case. *The results presented in Figure 4C suggest that newly hospitalised malaria patients are unlikely to be infectious. How do these results compare with clinical trial data? Baseline gametocytaemia is routinely recorded in clinical trials of uncomplicated malaria. It would be interesting to see how the results compare (and why they might be different).

8) One limitation of the study is that the circulation time of mature gametocytes cannot be estimated with any accuracy, due to the lack of patient follow-up. The authors do acknowledge this, but I think the statement (subsection “Estimation of gametocyte dynamics parameters”), "… we found that the circulating gametocyte lifespan… was much longer than that estimated from the neurosyphilis patient data…" is too strong and should be adjusted. In particular, using a constant hazard for gametocyte death (which was not found to provide the best model fit to the neurosyphilis patient data) in the case where an adequate follow up period was not available will overestimate the circulation time of the gametocytes.

9) In Table 2, I wonder if the prior on parameter f should be 0-100%, not 0-1%. Figure 1—figure supplement 1 and Figure 1—figure supplement 10 suggests that the relevant marginal posteriors extend beyond 0.01 (here f not converted to a percentage). Furthermore, in Table 1 the authors compare the commitment rate to the much higher values obtained elsewhere, particularly in vitro. It would be a curious comparison, if higher values were excluded from the model by using a uniform prior between 0-1%.

10) In Figure 1—figure supplement 1, I was initially confused by the high values for rp. Toward the end of the Methods section, the authors do explain how to convert this value to a net multiplication rate, which does clarify the matter. This parameter could be called (e.g.) the raw multiplication rate, but I leave this to the authors' discretion.
