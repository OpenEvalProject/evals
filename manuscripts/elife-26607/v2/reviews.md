# Peer review - Round 1

Editors:
- Tâm Mignot, Aix Marseille University-CNRS UMR7283 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26607.050](https://doi.org/10.7554/eLife.26607.050)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mechanism of bidirectional thermotaxis in Escherichia coli" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript "Mechanism of bidirectional thermotaxis in Escherichia coli" by Paulick et al. describes a study of the response of bacteria to temperature changes, and how this response can lead to the accumulation of the bacteria at a specific temperature in a gradient. The study combines FRET measurements of the CheA activity, measurements of cell movement in microfluidic channels across which a temperature gradient is applied, and a mathematical model that describes how the response of the signal transduction pathway to temperature changes is influenced by the presence of attractants and by the methylation state of the receptors. The manuscript is well-written and the results are for the most part clear and well-explained. The topic of the manuscript is very important and timely. There has been a lot of discussion of how bacteria sense and respond to temperature recently, but no clear answer has been provided yet, and this study advances this question significantly.

Several concerns should however be addressed before the manuscript is published:

1) The links between the findings and previous literature should be clarified in several instances:

A) One of the main findings of the study is that with the two ligands (Serine and MeAsp) present, the bacteria will not accumulate at a specific temperature, and only when one or the other is present then the bacteria would accumulate at a specific temperature. However, other studies (such as Yoney and Salman 2015) have claimed that in complex medium which contains the two ligands, the bacteria have a favored temperature at which they accumulate in a gradient. How do these results align with the previous results? Can the ratio of the ligands used in the experiments be important? I think that the authors should address this contradiction and explain if this is a specific case, or if it is a contradiction that should be clarified in future studies and with further tests?

B) Another contradiction between the results presented in this study and previous results is that Tar does not switch response from thermophilic to cryophilic. This has been observed previously in Mizuno and Imae 1984, albeit at the level of cell behavior and not CheA activity. I think that the authors should address this contradiction better. Do they think that there is another layer of control between CheY-P and the motor switching? Do they think that the dynamics of CheY-P binding to CheZ is different than its biding unbinding dynamics to the motor? Or do they think that the previous results are not accurate enough?)

C) One more contradiction between these results and previous results is that here, the authors do not observe switching in the response of wt bacteria in buffer, whereas in a previous publication of one of the co-authors (Paster and Ryu 2008) it was reported that the response (which again was measured at the motor level) switched direction around 37 degrees.

D) The authors claim here that the accumulation temperature of the bacteria is actually chosen to optimize their growth. This is based on the fact that addition of serine to the growth medium seems to have the least effect on the growth around the accumulation temperature of the bacteria (~30degrees). However, they also show that the accumulation temperature of the bacteria can change as a function of the O.D. (Figure 3—figure supplement 2) due to the change in the expression level of the receptors Tar and Tsr. How does this result integrate with the previous one – a test at the motor level?

2) Definitions, experimental methodology and analysis should be better explained:

A) The narrative has been built around the concept of an accumulation temperature. This term however, has not been explained in the text. It seems that the peaks in cell distributions (motility assays, Figure 2E) are likely what the authors term as cell accumulation. The FRET data on the other hand provides information about cross-over temperatures, where the network's thermophilic response inverts to cryophilic. Brownian motion, drift, cell-filament characteristics, hydrodynamic interactions together ensure that the accumulation temperatures and the cross-over temperatures are related, but not quite the same. Hence, the repeated conflation of 'accumulation' with the FRET data throughout the text is questionable.

B) The variable thermal gradients and channel widths employed in the motility assays make it difficult to ascertain whether the peak cell density appears due to the receptor-level interactions as suggested, or whether it is a function of wide channels and steep thermal gradients. For example, the gradients in Figure 2E and Figure 2—figure supplement 2 are ~ 1.5 deg/100 μm to 2.5 degree/100 um. Compared to these, figures where peaks are missing employ about half the thermal gradient. Can the authors confirm whether the accumulation is not a function of steep gradients alone?

C) In general what are the dimensions of the microfluidic channel used for tracking cells under a gradient? Channels used in Figure 1—figure supplement 1B and Figure 2E seem to be different.

D) The experiments in the temperature gradient are not well explained. Maybe adding a figure showing typical trajectories of cells that were used to calculate the TMC, and showing the x and y directions in the channel can help. Also, explain how the normalized cell count in Figure 2D and E was obtained.

E) The driving force for the thermotactic response in the presence of the two attractants reduces at higher temperatures (Figure 2A). It seems quite possible that under a treatment of 10:1 MeAsp/serine, the cells might avoid lower temperature regions and concentrate near higher temperatures (40-45 degrees). Would the authors consider that an accumulation? In other words, how sharp does the peak need to be in order to be termed as accumulation?

F) The temperature dynamics in the FRET experiments should be more clearly explained in a graph showing how fast the temperature increased, and how long it took to stabilize.

G) It is suggested in the Abstract and elsewhere that the model explains accumulation temperature, but quantitative predictions of either accumulation or cross-over temperatures are not presented. The model makes qualitative predictions that appear similar to the observed cross-over behavior but it quits unexpectedly at temperatures above 35 °C. Predictions over the entire temperature range employed in the experiments. How were the parametric values (–subsection “Mathematical modeling”, last paragraph) taken from previous works, fitting experiments? In general, the authors would greatly help the reader understand the model better by explaining the physics underlying the modulation of equilibrium methylation levels by changes in demethylation/methylation kinetics.

Reviewer #2:

The manuscript "Mechanism of bidirectional thermotaxis in Escherichia coli" by Paulick et al. describes a study of the response of bacteria to temperature changes, and how this response can lead to the accumulation of the bacteria at a specific temperature in a gradient. The study combines FRET measurements of the CheA activity, measurements of cell movement in microfluidic channels across which a temperature gradient is applied, and a mathematical model that describes how the response of the signal transduction pathway to temperature changes is influenced by the presence of attractants and by the methylation state of the receptors. The manuscript is well-written and the results are for the most part clear and well-explained. The topic of the manuscript is very important and timely. There has been a lot of discussion of how bacteria sense and respond to temperature recently, but no clear answer has been provided yet, and this study advances this question significantly.

I have however few questions that I think the authors should address before publication:

1) Some experimental details are lacking.a) The dimensions of the microfluidic channel used for tracking cells under a gradient is not clearly specified. In Figure 1—figure supplement 1B it looks like it is 500µm wide, which matches most graphs presented, however, in Figure 2E it seems to be different.

b) The experiments in the temperature gradient are not well explained. Maybe adding a figure showing typical trajectories of cells that were used to calculate the TMC, and showing the x and y directions in the channel can help. Also, explain how the normalized cell count in Figure 2D and E was obtained.

c) The temperature dynamics in the FRET experiments should be presented in a figure. How fast was the temperature increase, and how long until it stabilized? These details should be included.

2) The values used in the mathematical model should be explained. Why did the authors use these values in the simulations (subsection “Mathematical modeling”, last paragraph –)? Were they taken from a previous work? Were they obtained from fitting to experiments? Etc.

3) One of the main findings of the study is that with the two ligands (Serine and MeAsp) present, the bacteria will not accumulate at a specific temperature, and only when one or the other is present then the bacteria would accumulate at a specific temperature. However, other studies (such as Yoney and Salman 2015) have claimed that in complex medium which contains the two ligands, the bacteria have a favored temperature at which they accumulate in a gradient. How do these results align with the previous results? Can the ratio of the ligands used in the experiments be important? I think that the authors should address this contradiction and explain if this is a specific case, or if it is a contradiction that should be clarified in future studies and with further tests?

4) Another contradiction between the results presented in this study and previous results is that Tar does not switch response from thermophilic to cryophilic. This has been observed previously in Mizuno and Imae 1984, albeit at the level of cell behavior and not CheA activity. I think that the authors should address this contradiction better. Do they think that there is another layer of control between CheY-P and the motor switching? Do they think that the dynamics of CheY-P binding to CheZ is different than its biding unbinding dynamics to the motor? Or do they think that the previous results are not accurate enough?

5) One more contradiction between these results and previous results is that here the authors do not observe switching in the response of wt bacteria in buffer, whereas in a previous publication of one of the co-authors (Paster and Ryu 2008) it was reported that the response (which again was measured at the motor level) switched direction around 37 degrees. The questions raised in (4) also apply here, and I think that the authors should address this contradiction more clearly, and maybe add a test at the motor level.

6) The authors claim here that the accumulation temperature of the bacteria is actually chosen to optimize their growth. This is based on the fact that addition of serine to the growth medium seems to have the least effect on the growth around the accumulation temperature of the bacteria (~30degrees). However, they also show that the accumulation temperature of the bacteria can change as a function of the O.D. (Figure 3—figure supplement 2) due to the change in the expression level of the receptors Tar and Tsr. How does this result integrate with the previous one?

In general, I think that this is an excellent study and very important, which provides significant advancement to the field, but I think the authors should discuss some of these contradictions more, even if they cannot provide clear cut answers to these contradictions at this point.

Reviewer #3:

Paulick et al. have investigated an interesting response of the chemotaxis machinery to a non-chemical stimulus. The team's expertise in the FRET technique is clearly evident once again – the experimental data are solid. The conclusions, for most parts, are well-founded. The observed inversion of the chemotaxis machinery from a thermophilic to a cryophilic response has been modeled by taking into account an interaction between the tar and tsr receptors. This work addresses several puzzling aspects of prior studies and is likely to be of wide interest.

1) The narrative has been built around the concept of an accumulation temperature. This term however, has not been explained in the text. It seems that the peaks in cell distributions (motility assays, Figure 2E) are likely what the authors term as cell accumulation. The FRET data on the other hand provides information about cross-over temperatures, where the network's thermophilic response inverts to cryophilic. Brownian motion, drift, cell-filament characteristics, hydrodynamic interactions together ensure that the accumulation temperatures and the cross-over temperatures are related, but not quite the same. Hence, I don't agree with the repeated conflation of 'accumulation' with the FRET data throughout the text.

2) The variable thermal gradients and channel widths employed in the motility assays make it difficult to ascertain whether the peak cell density appears due to the receptor-level interactions as suggested, or whether it is a function of wide channels and steep thermal gradients. For example, the gradients in Figure 2E and Figure 2—figure supplement 2 are ~ 1.5 deg/100 μm to 2.5 degree/100 um. Compared to these, figures where peaks are missing employ about half the thermal gradient. Can the authors confirm whether the accumulation is not a function of steep gradients alone?

3) The driving force for the thermotactic response in the presence of the two attractants reduces at higher temperatures (Figure 2A). It seems quite possible that under a treatment of 10:1 MeAsp/serine, the cells might avoid lower temperature regions and concentrate near higher temperatures (40-45 degrees). Would the authors consider that an accumulation? In other words, how sharp does the peak need to be in order to be termed as accumulation?

4) It is suggested in the Abstract and elsewhere that the model explains accumulation temperature, but I did not find any quantitative predictions of either accumulation or cross-over temperatures. The model makes qualitative predictions that appear similar to the observed cross-over behavior but I can't tell for sure since it quits unexpectedly at temperatures above 35 °C. I request an inclusion of predictions over the entire temperature range employed in the experiments and a note on how the parametric values (subsection “subsection “Mathematical modeling”, last paragraph) were determined. Most importantly, the authors would greatly help the reader understand the model better by explaining the physics underlying the modulation of equilibrium methylation levels by changes in demethylation/methylation kinetics.
