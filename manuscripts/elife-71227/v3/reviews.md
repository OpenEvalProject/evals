# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71227.sa0](https://doi.org/10.7554/eLife.71227.sa0)

The authors present a study of the swimming behaviour of the zoospores of the water mold Phytophthora (Greek "Plant Destroyer"), which is responsible for significant crop damage worldwide. The motility of the zoospores is likely a significant contributor to the successful spread of the disease, and as such its study has potential wide impact. The authors suggest using a model that the anterior "hairy" (covered with mastigonemes) flagellum is the primary contributor to motility, and show with high-speed imaging that the microorganism is able to turn on the spot by stopping its posterior flagellum, and changing the beat-pattern of its anterior flagellum from "sperm-like" to "Chlamydomonas-like".


---

# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71227.sa1](https://doi.org/10.7554/eLife.71227.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "Cooperation of two opposite flagella allows high-speed swimming and active turning in zoospores" for peer review at eLife. Your article is being evaluated by 2 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor.

While the reviewers and editor are supportive of the paper, it was our consensus opinion that a substantial amount of revision to the manuscript is needed to clarify the points below. Furthermore, since active turning and steering feature prominently in the title and abstract, it would be crucial to further investigate the flagellar motion and gait changes during turns. Without this, we believe that the conclusions of the paper are overstated.

Reviewer #2:

The capacity for swimming microorganisms to efficiently explore their environment can be essential for their survival and proliferation. This manuscript by Galiana et al., examines the swimming characteristics of P. parasitica, a plant pathogen known for causing widespread disease and economic loss. The authors present high-speed video recordings which reveal how individual cells execute turning events during their swimming motion. There is considerable experimental data, which in combination with a mathematical model for flagellar motion, sheds light on how the two flagella collectively produce locomotion and turning events.

The turning events are largely portrayed as being due to temporary arresting of the posterior flagellar beating. E.g., "turning requires the posterior flagellum to halt, while the anterior one continue beating". However, while stopping the posterior beating is necessary, it is not sufficient. What is lacking is a detailed explanation of precisely how the cells turn. From Video 4, it appears that the anterior flagellum changes its gait completely from a sinusoidal travelling wave to something more reminiscent of Chlamydomonas, with distinct power and recovery strokes (but with mastigonemes). The oscillations of angle of Figure 4d indeed suggest that a distinct gait is employed to turn the cell. The authors mention this on line 389, but this is not investigated further, citing imaging capabilities. Cell turning events seem to require coordinating the stop/start motion of one flagellum and distinct gait changes in the other, but the mechanism(s) behind this remain unclear.

From the trajectories presented in Figure 2, numerous quantities are extracted, including swimming speed, turning angle, run times, etc. The swimming speed threshold is essential for delineating turns events from 'runs', and one method for extracting Uth is presented. This leads to the conclusion that the most likely reorientation angle (Δθ, see Figure 2g) is actually 0 degrees. i.e. the cell stops and then continues in the same direction. It could be that this is an artefact of a relatively high value of Uth, which misclassifies one run into two smaller ones. This sensitivity is further shown in Figure 2b – increasing Uth to just ~125 microns/second would result in one single turning event (taus) instead of three distinct ones. It is not clear from the data how the results would change if Uth were varied in a sensitivity analysis, or defined in another way.

The authors have presented an experimental system which is capable of recording reasonably long trajectories of swimming P. parasitica cells, and an analysis pipeline which can extract statistical distributions of various swimming properties. The overarching assumption is that the 2D measurements can be extrapolated to three dimensions. Given the displayed trajectories are quite long (several millimetres), it seems that there are very few issues with the cells swimming out of focus. It is likely that the shallow chamber (100 microns) helps to maintain the cells within the focal plane and helps to minimise biases in the run time measurement. However, if that is the case, it's hard to know the effect that confinement has on the motility characteristics. It could be that the stop-start motion with Δθ=0 actually represents failed out-of-plane turning events.

The authors utilised microscopic parameters from the swimming motion to predict the bulk diffusivity. It was mentioned that the direct measurement of D is unreliable given the small number of trajectories and their short duration. However, this seems to be inconsistent with the supplementary videos, which show cells in focus for extended periods of time and allow collection of trajectory data. Even if individual MSD measurements cannot be collected in large sets, perhaps a bulk diffusivity could be measured at lower magnification. At the moment, there is no strong quantitative link between the simulated diffusivity and the actual spreading of cells.

A simplified mathematical model is developed in which resistive force theory (RFT) applied to the two flagella calculates the propulsive force on the cell body. This is then used to derive a closed form expression for the swimming speed (Equation 5), which predicts values commensurate with the observed swimming speeds (Figure 3). It is an interesting finding that the mastigonemes modify the sign of the propulsive force (also noted in previous works), enabling the anterior flagellum to pull the cell through the fluid. The planar motion of the flagellum in the model seems reasonable given the dynamics presented in Video 3. However, it is unclear by what mechanism the cells rotate as they swim. Perhaps this has something to do with the off-axis position of the flagellar base. Since the helical motion of the cells features prominently in the paper and is likely important for overall dispersal, it would be great if the model could account for viscous torques, calculate the cell body rotation rate and characteristics of the helical path.

The observed dynamics have been classified into straight runs and turning events. However, many of the 'runs' are certainly not straight (see Figure 2). It is not clear whether these curved trajectories are due to rotational diffusion, or perhaps from hydrodynamic interactions with the boundaries (bacteria are known to swim in circles near no-slip walls). This could have significant implications for the dispersal calculations, and for classification of events within the trajectories.

In order to calculate a cell's 'run time', it is necessary to visualise two successive turning events which bookend a single run. However, for cells swimming in three dimensions, the probability of observing a given run length depends on the value of the run length. Can the authors please provide information about any biases in their data collection, and the extent of any biases in the presented distributions? This could include discussion of depth of field, chamber height, and whether any cells were excluded.

The motility strategy examined in this paper is described as "steering" and is presented as a possible method for pathogenic cells to target the plant host. However, the dynamics are all spatially isotropic, and it is not clear how cells could navigate towards specific chemical cues (e.g. potassium, physical cues, electrical signals).

The motor efficiency is determined in terms of the swimming speed to wave propagation. There are many ways of calculating efficiency in low Reynolds number hydrodynamics, many of which include power/energy calculations. The authors allude to a link between power and drag due to mastigonemes, but it's hard to determine from the presented results how much energy the cell needs to swim. I think it would be very helpful to expand the section on efficiency, connecting with other established methods, and results for other organisms.

Quantifying the microscale trajectory features and predicting the collective cell diffusivity requires a threshold value of Uth. It would be very important to examine the sensitivity of the measurements to the value of Uth, and explore the implications if another definition was chosen.

Figure 2. Some of the time-dependent processes are plotted in terms of frame number (t/dt), and others in absolute time (t). It would be best to include all processes in terms of t, so that conclusions are independent of frame rate.

Line 38 mentions that E. coli possess "a passive helical flagellum", but they possess a bundle of these. Please correct the numbers.

There is a need to better distinguish between axial rotation and cell "rotation" during turns. Perhaps it would be better not to use the same word.

Line 58. The organisms can apparently swim for several hours. However, this may be very short compared to the timescales required to find a plant. Can the authors please elaborate on how motility can be sustained in a typical environment, and how long it might take for a cell to reach its target (assuming no active navigation)?

The article should be carefully read by a native English speaker. For example, "underwhelming knowledge" is not an appropriate way of describing open questions. "Flimsy" also refers to an object's structural integrity and not its shape. The word "accumulating" is used extensively throughout the paper but is not appropriate since it implies temporal integrating. i.e drag and velocity don't 'accumulate' along the flagellum.

Reviewer #3 (Recommendations for the authors):

The authors present a study of the swimming behaviour of the zoospores of the water mold Phytopthora, which combines experimental imaging of fixed cells (to examine structure), image capture and analysis of multiple swimming cells to examine bulk swimming behaviour, high-speed imaging to characterise on the spot turning behaviour, and an analytical mathematical model of the straight "run" swimming behaviour that incorporates the mastigonemes on the anterior flagellum.

In terms of what is already known about these systems, it is already known that Phytophora zoospores swim with two flagella at the high speeds shown herein, and that the anterior flagellum is covered with mastigonemes (see for instance the authors' previous work DOI: 10.1016/j.csbj.2020.10.045). It has also been known for some time that mastigonemes reverse the expected direction of propulsion for a flagellum beating with a sperm-like (travelling wave) waveform, so this behaviour is expected, and indeed commented on in the authors' previous work. The model provided is based upon previous models (see eg https://doi.org/10.1063/1.3608240), which should be made clearer in the text, with the adaptation being that there are 2 flagella and a body here.

The main novel components are (1) the discussion that the anterior flagellum accounts for the majority of the propulsion, and (2) the characterisation of the on-the-spot turning (as far as I know). The first point is based on analysis from the analytical model. My concerns with this conclusion are three-fold. Firstly, it relies on mastigonemes remaining rigid and normal to the tangent of the main flagellum, whereas some bending with the flow is to be expected (reducing their impact). Secondly, the resistive force theory model, while qualitatively powerful, does not include hydrodynamic interactions between neighbouring mastigonemes, which may also reduce their impact. Thirdly, it is quite sensitive to the mastigoneme density once this drops to around 10 per micron (the way in which the mastigoneme density was estimated, and the data, should be made clear in the manuscript), and fourthly, the posterior flagellum naturally beats at around twice the frequency (probably because they are expending the same amount of energy), so I do not feel that the conclusion "we consider the anterior flagellum as the main motor of zoospores because it has the ability to immensely increase or decrease speed with a small adjustment of its beating frequency" is justified.

The characterisation of the on-the spot turning from high speed image microscopy is very nice, to the best of my knowledge novel, and the analogues to peritrichous bacteria and Chlamydomonas well drawn up. This section is well described (though not modelled), but would probably benefit from a schematic in addition to the set of experimental images.

The paper would benefit from a clearer exposition of what the novel components are in relation to previous work, and a link back to the motivation of crop damage and how this understanding of motility may be used in future pest control strategies.

While I enjoyed reading the article, the authors should endeavour to make it clearer in certain places what has come before, and what is the novel component. For instance, the modelling seems to follow the arguments of https://doi.org/10.1063/1.3608240, and while this is cited elsewhere, I believe this should be stated very clearer in the model section. Secondly, there are a few sentences which mislead with respect to aspects of the novelty, for instance:

1. "Despite the relevance of zoospore spreading in the epidemics of plant diseases, it is not known how these zoospores swim and steer with two opposite beating flagella." For the swimming this is clearly known, as the authors commented on in their previous work, it is the turning I believe that was not well characterised.

2. "Here, we introduce a new type of microswimmer, named Phytophthora zoospores, which has two different flagella collaborating for unique swimming and turning mechanisms (Figure 1(a))." – you have presented work previously on the swimming of this organism.

I believe the data on mastigoneme density is critical to one of your conclusions, and should be presented carefully, and I believe this conclusion about the anterior flagellum being the main driver for motility is probably not correct, more broadly – it certainly needs more careful treatment.
