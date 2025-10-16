# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85275.sa0](https://doi.org/10.7554/eLife.85275.sa0)

This valuable work presents new results to characterize the relationship between electrical excitation and torque generation in stick insect joints. The evidence supporting this work is a series of torque-voltage measurements across individuals. The strength of evidence is compelling in supporting the outcomes.


---

# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85275.sa1](https://doi.org/10.7554/eLife.85275.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A hierarchical model for external electrical control of an insect, accounting for inter-individual variation of muscle force properties" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Nick Gravish (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The clarity of this work suffers from its structure: the models (and the parameters within) are central to the results of this study. The integration of data-driven modeling and experiment is the main reason this work is exciting! Yet, these are introduced far after the results are presented. While this is partially due to the section structure set forward, some basic aspects of the models and experimental system should be introduced prior to delineating the results in order to provide clarity.

2) The referees were concerned that it was not clear from the presentation of the results how substantial the contributions in this paper are to the field as a whole. The authors should better articulate the importance of their contributions, or, missing that, they should better explain what the challenges have been and what would need to be done to overcome them.

3) Along these lines, authors are missing an opportunity to make their work more impactful, by limiting the motivation and discussion to the domain of cyborgs, which is in itself important but quite a small field of research. There are many important animal locomotions, and even mechanical sensing, problems where this understanding is extremely relevant and useful. For example, stiffening the legs can help animals generate larger forces during locomotion in rough terrain, in behaviors that can benefit from higher forces (e.g., escape from predators, fighting between males during courtship), even in mechanical sensing (e.g., web-making spiders may modulate leg stiffness as part of its strategies to modulate how prey vibration is sensed by vibration sensors in its legs). A few studies that may help the authors appreciate and think about the broad implications:

a. Sponberg et al. (2011), A single muscle's multifunctional control potential of body dynamics for postural control and running, Phil. Trans. Royal Soc. B. 366(1570): 1592-1605.

b. Blickhan (1986), Stiffness of an arthropod leg joint, J. Biomechanics, 19(5), 375-384.

c. Wang et al. (2022), Cockroaches adjust body and appendages to traverse cluttered large obstacles, J. Exp. Biol., 225(10), jeb243605.

d. Mhatre et al. (2018), Posture controls mechanical tuning in the black widow spider mechanosensory system, bioRxiv, 484238.

Please comment on the relationship of the results in this study to the above line of research.

4) While it is interesting that inter-individual differences are important in the torque output from the joint, are these inter-individual differences related to any distinct differences among the insects studied (e.g., body mass, limb length, cross-sectional muscle area, and age all would likely influence torque)? While the referees are not advocating that all of the above parameters (age, size, etc) be added into a more complex model, they think it is important to provide any known information about the variance in individual size/age/etc, perhaps as a supplementary table.

5) Line 145 states that "Models 1-2 and 2-1 most accurately predicted the posterior predictive distribution.", is this a typo? The referees were under the impression that Models 1-2 and 2-2 are the best, as they are linear and nonlinear models with hierarchical slopes. In the paragraph starting at line 147 and the subsequent paragraph it is argued that while the nonlinear model 2-2 worked well, the linear model is still better. "The comparison of the linear model (model 1-2) with the nonlinear model (model 2-2) using the WAIC for all conditions (muscle type and applied voltage) resulted in lower values for the linear model." But certainly, both are quite close in WAIC, and the question is: might there be reasons from muscle physiology on stick insects to expect a non-linear model? While the linear model had the marginally lowest WAIC without any prior assumptions about the torque-duration curve, certainly much is known about the effect of stimulation on force production, and might including that information validate the non-linear model over linear? Alternatively, if the goal is to just model the data under 500ms stimulation because this is the relevant timescale for walking behavior (line 181), then the linear model is fine. But reading the manuscript the referees got the impression the goal was to best model the torque-voltage relationship, which would include the full excitation range and incorporates known information from muscle physiology. Please comment on these concerns and edit the manuscript as needed.

6) Figure 3 is a bit confusing, as this plot is meant to compare the experimental data with the hierarchical model distribution. However, all the model distributions across the 10 insects look identical. Wasn't the point of the hierarchical model that the slope parameter varies across individuals (isn't this what Figure 4 demonstrates?)? So, shouldn't the distributions and green fit lines all be different for the individuals? Please comment.

7) It is stated that 20 insects were tested, but all the plots show only 10. Is this just because the other 10 were not presented? Or were observations discarded from the other 10 insects for some reason? This is important to describe so that readers can assess the results.

8) What is the order of presentation of different voltages? It is stated that muscle fatigue should be negligible for under 50 stimulations, but the range of the 2V experiments alone is between 49-79 stimulations. So, were another ~50 stimulations performed at the three other voltages? And if so, was fatigue a possible issue?

9) Also, were there "warm-up" effects too where the muscle force increased with subsequent stimulations? It would be important to provide some characterization of this.

10) More information should be provided about the ordering of the different excitation experiments. The methods do not describe what the time duration between excitations was, how many were performed over what time period, etc. Additionally, it looks like four different voltage amplitudes were performed which I could only observe from figures 2 and 4. It would be beneficial to describe in detail the full sequence of data collection on an insect.

11) It is stated that muscle fatigue should be negligible for under 50 stimulations, but the range of the 2V experiments alone was between 49-79 stimulations. So, were another ~50 stimulations performed at the three other voltages? And if so, was fatigue a possible issue? Also, were there "warm up" effects too where the muscle force increased with subsequent stimulations? It would be useful to provide some characterization of this.

12) The authors also seem to be only addressing certain parameters rather than the potential adjustable parameters. PWM, voltage, and frequency are adjustable, but the paper only varied voltage and burst duration. It is unclear whether factors such as frequency (which has been shown to affect muscle force values) were investigated or not. If they were investigated in preliminary experiments, it would help if they were described; if not, it would also help to explain why, to help the readers understand why only burst duration and voltage were varied.

13) The data and code were not yet made available. The referees request access to both the data set and the code, as both are necessary to assess the reproducibility of this study.

14) Given the potential ethical considerations of 'cyborg control of insects,' the authors should discuss the potential ethical implications of extensions of their work with respect to animal welfare and other societal implications.

Reviewer #1 (Recommendations for the authors):

Overall, I think this is an interesting and useful study and that it will nicely move the field forward. The primary suggestion I have is a slight reorganisation as noted in the Public Review: while I understand that journal section structure puts some limitations on this (and while I agree that overly technical information should be placed so as not to disrupt the flow of the narrative), introducing some basic features of the experiments and models upfront (perhaps in a Table form) would be very helpful in understanding what the results mean. I also recommend moving Figure 5 before the results Figures.

The data and code were not yet made available (as far as I can tell), which is a bit disappointing. From the text, I understand they will be made available upon publication; but it is difficult to assess the reproducibility of this study without access to these as a referee.

Reviewer #3 (Recommendations for the authors):

1. The work itself seems not very substantial. It seems that the authors did relatively simple experiments, and just tried many different simple models to fit the data. It is not clear whether there is a substantial contribution. The authors should think harder about this and better articulate the contribution to the field with such a relatively simple study (as it appears). Or explain better what the challenges have been to better show why this initial first step is not as straightforward as it appears to be.

2. I think the author is missing an opportunity to make their work more impactful, by limiting the motivation and discussion to the domain of cyborgs, which is in itself important but quite a small field of research. There are many important animal locomotions and even mechanical sensing problems where this understanding is extremely relevant and useful. For example, stiffening the legs can help animals generate larger forces during locomotion in rough terrain, in behaviors that can benefit from higher forces (e.g., escape from predators, fighting between males during courtship), even in mechanical sensing (e.g., web-making spiders may modulate leg stiffness as part of its strategies to modulate how prey vibration is sensed by vibration sensors in its legs). A few studies that may help the authors appreciate and think about the broad implications:

a. Sponberg et al. (2011), A single muscle's multifunctional control potential of body dynamics for postural control and running, Phil. Trans. Royal Soc. B. 366(1570): 1592-1605.

b. Blickhan (1986), Stiffness of an arthropod leg joint, J. Biomechanics, 19(5), 375-384.

c. Wang et al. (2022), Cockroaches adjust body and appendages to traverse cluttered large obstacles, J. Exp. Biol., 225(10), jeb243605.

d. Mhatre et al. (2018), Posture controls mechanical tuning in the black widow spider mechanosensory system, bioRxiv, 484238.

3. The authors seem to be only addressing certain parameters rather than the potential adjustable parameters. PWM, voltage, and frequency are adjustable, but the paper only varied voltage and burst duration. It is unclear whether factors such as frequency (which has been shown to affect muscle force values) were investigated or not. If they were investigated in preliminary experiments, it would help if they were described; if not, it would also help to explain why, to help the readers understand why only burst duration and voltage were varied.

4. It is difficult to understand the Results and Discussion without reading the Method and Materials first. I know that eLife has Methods later, but the meaning of certain acronyms was not at least briefly explained until later in the paper, making it hard to understand when one reads it.

5. What are the resulting modelling equations generated for each? Is it possible to output the resulting modeling equations created from the Makrov Chain Monte Carlo method? It is difficult to see how they compare and are different from the simple linear and power equations that are used for 1-1 and 2-1.

a. What is the power function constant used for 2-1? It seems to be that \γ is 1, but doesn't that make it a linear function?

6. It is unclear how the author settled at the default parameters of the PWM signals to 2 V, 50 Hz, and 30% duty ratio.

7. For Figure 3, why is the prediction only compared with models 1-2? From what I gather, models 1-2 and 2-2 were the most accurate in predicting the posterior predictive distribution, why is specifically 1-2 addressed?

8. The intro addresses how inter-species variability can cause issues with the precise control of different animals. Is this issue addressed in this paper? It is not clear to me how this modelling can account for individual species variability considering the models only include variables for the burst duration and joint torque. Is the assumption that generating an appropriate model can lead to creating a robust feedback control system to control for interspecies variability?

9. The pictures of the experimental setup are confusing, it would be helpful if there was a schematic of the setup and some labels were given on where the muscles that were tested are located.

10. Not sure what the difference between hierarchical models and non-hierarchical models is, and where it is addressed.

11. Overall there are too many plots to understand, reducing the number of plots and increasing the font size on the plots will help increase the clarity and understanding of each figure.

Specific Comments:

1. Can you explain why there is a different number of simulations (n) for each animal? (Referring to Figure 3)

2. Unknown o? on line 349, not sure if hierarchical model o is a thing.

3. The labels for each of the y values and x values are very hard to see and are very blurry, it is hard to get a good sense of what these numbers mean for Figure 4, or what the y-axis and x-axis mean. Increasing the number font would be helpful for reading any of these graphs.
