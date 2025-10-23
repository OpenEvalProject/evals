# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85910.sa0](https://doi.org/10.7554/eLife.85910.sa0)

In this manuscript, the authors present a valuable tool and resource to create stable odorant landscapes (gradients) for the study of chemotaxis in small model organisms. Using a metal oxide-sensor-based approach, odor concentration is measured in space and time to produce data-driven simulations of the odor diffusion process. Combined with a system of distributed odorous air flows, odorant landscapes are generated to characterize aspects of olfactory navigation in C. elegans and the Drosophila larva.


---

# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85910.sa1](https://doi.org/10.7554/eLife.85910.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Continuous odor profile monitoring to study olfactory navigation in small animals" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Piali Sengupta as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As described in their reports, the reviewers appreciate the merits of the sophisticated methodology and assays introduced in your manuscript to create controlled odorant landscapes. The reviewers raised a series of concerns related to the methodology and its use. We ask that you address these concerns in a revised manuscript.

Methodological concerns:

– The authors should experimentally characterize the sensitivity range (log concentrations over which detection is reliable), temporal resolution, and stability (potential existence of drifts) of their sensor array in response to more rapid changes in odor concentration. They should discuss their results in the context of published studies where metal oxide sensors have previously been employed to measure odor dynamics in turbulent airborne environments.

– It would be important to rule out the heat effects of the metal oxide sensor arrays on the behavior of C. elegans and Drosophila larvae. The authors should discuss the existence of such heat effects. They should also discuss whether physical interactions with the sensors themselves could affect the odor stimulus.

– The authors must generalize their conclusions to other odors that are commonly used to study olfactory behavior in Drosophila and C. elegans, and that have lower water solubility. More generally, they should discuss the type of odors that are compatible with their methodology.

– The authors should include a more thoughtful comparison of the pros and cons of their methodology with respect to the spectroscopic approach presented in Louis et al. 2008. In Tadres et al. 2022, numerical simulations of odor gradients were constrained by spectroscopy data. These simulations showed that gradients produced by a single source of ethyl butyrate are relatively stable, which is consistent with the behavior of larvae. While the reviewers don't dispute the fact that the more complex assay introduced by the authors might enhance the stability of odor gradients, it is probably misleading to conclude that all gradients produced by a single odor source are unstable.

– As supporting material, it would be important to list cost estimates to build the assay and provide general information related to the sensitivity, odor selectivity, and temporal resolution of the methodology. Given that the methodology is considered a Tools and Resources, it would also be extremely valuable to provide more information (possibly a tutorial) to help other labs adopt the methodology to characterize odor landscapes in new assays.

Additional request:

The methodology and experiments presented in the manuscript offer the opportunity to compare odor-evoked behaviors in two species in response to the same environment. To illustrate the potential of the methodology, the authors are strongly encouraged to analyze the behavior of both species using the same procedure and metrics to report similarities and differences in behavioral algorithms. This addition should help the reader define whether the methodology enables to draw new conclusions or if it recapitulates previous observations. If the authors decide that they won't proceed with a deeper behavioral analysis, they should tone down their claims about algorithmic findings in their abstract and the rest of the manuscript.

Reviewer #1 (Recommendations for the authors):

Measuring airborne odorant gradient is notoriously challenging. The goals of this manuscript are twofold: (1) to develop a technique to characterize the spatial properties and temporal stability of airborne odorant landscapes; (2) to produce stationary odorant landscapes with controlled and predictable geometries that are suitable to refine the study of navigation behavior (chemotaxis) in small animals such as C. elegans and the Drosophila larva. Tackling these two problems should improve future correlations between sensation and behavior to study the neural bases of sensory encoding and action selection.

To achieve their first goal, the authors propose to use a distributed array of digital gas sensors. The resolution of the measurements reported in the manuscript is impressive: they go beyond the state of the art. Although these measurements remain discrete in space, they provide valuable data to fit a biophysical model of the diffusion of the odor and its reaction with the arena where the odorant landscape is created. While the technique allows monitoring odorant landscapes in space and time, it also has limitations.

First, the measurements require modifying the experimental conditions where the behavior is tested. The landscape cannot be directly measured while the behavior is taking place. Second, the dimensions of the digital gas sensors (~1 cm) are relatively large compared to the size of the tested animals (~1 mm). This limits the resolution of the spatial measurements of odorant landscapes with small dimensions where even smaller animals are studied. In particular, the system might not be able to detect differences in concentrations between the individual inlets of the odor delivery system, which reduces the accuracy of the reconstruction of a landscape and the evaluation of its variability.

The second goal of the study is to produce odorant landscapes with enhanced stability compared to existing systems. The airflow-based olfactometer features spatially patterned odorized air. While this system represents an improvement with respect to published assays in C. elegans, its contribution to the larva is less obvious. The geometry of the landscapes resulting from the linear array of odorized air flows is essentially uni-dimensional. This produces geometries that are fundamentally different from the radially symmetric gradients emitted by odor cups that have been used by other labs for many years. The authors conclude that gradients resulting from the diffusion of a single source are unstable due to the absorption of the odor by the agar. This conclusion was drawn for odorant molecules that are water-soluble (or miscible in water like ethanol). Whether the same conclusion holds for odorant molecules with low or negligible water solubility is unknown, which precludes a generalization of the results to odors that have been more commonly used in the field.

The manuscript would benefit from additional work to demonstrate how the tool can advance the understanding of chemotaxis in C. elegans and the Drosophila larva. Besides the fact that the authors chose to characterize larval chemotaxis with an odor that has not been used in previous work, the behavioral characterization is limited given the potential capabilities of the new tool. Presently, it falls short of reporting "chemotaxis strategies for C. elegans and D. melanogaster larvae populations under different spatial odor landscapes" as stated in the abstract. This incompleteness is a missed opportunity to validate the merit of the methodology.

I praise the authors for the technical achievement presented in the manuscript. Combining a spatial array of digital gas sensors with computational simulations of the odor diffusion process is ingenious. However, several aspects of the methodology require further characterization and more careful validation to be helpful as a tool that can be widely adopted by other labs. Below is a list of shortcomings that should be addressed:

1. Although the multi-odorous-air-flow delivery system is simplified compared to the original design published by Gershow et al. in 2012, it remains complex. It would be important to test the reproducibility of landscapes produced by this system. In addition, it would be useful to demonstrate the flexibility with which landscapes with different geometries can be created. One notable limitation of the system is that gradients can only be designed in one direction. This precludes the creation of radially symmetric gradients produced by a point source, such as those that have been typically used in C. elegans (e.g. Pierce-Shimomura & Lockery 1999) or in the Drosophila larva (learning assay developed by Gerber and coworkers). Given the tiled arrangement of the airflow inlets, is the gradient smooth at the scale of a worm or "bumps" expected in the odor profile over the y-axis? This question is likely to be unresolved by the odor measurements since there is a higher density of tubes compared to sensors along the y-axis.

2. The manuscript reports that the high absorption of butanone by the agar significantly affects the properties of the resulting odorant landscape. As a result, odorant landscapes produced by a single odor droplet can flatten over time in such a way that the gradient might be nearly inexistent after a couple of minutes. This conclusion is significant since larval olfaction has been frequently studied with a single odor source (a cup or a droplet). As indicated by the authors in lines 270-271, butanone is a water-soluble odorant molecule. By comparison, most odors that have been used to study olfactory behaviors in the Drosophila larva have a low solubility in water. For instance, 1-octanol (<1g/L), benzaldehyde (<10g/L), pentyl acetate (<2g/L) and geranyl acetate (<1 g/L) are all far less soluble than butanone (275 g/L). This difference in water solubility is likely to affect the stability of the odorant gradient. Were odor measurements not combined with computational modeling of the odor diffusion-reaction process in Tadres et al. 2022 (Science Advances) to establish that gradients of ethyl butyrate and ethyl acetate are relatively stable for 5 min?

3. Technical question related to Figure 3: in this figure, the butanone droplet appears to be placed on the lid without agar (line 24) whereas it is placed directly on the agar gel in the condition with agar (line 251). The placement of the butanone droplet on the lid versus on the agar is an important distinction besides just the presence or absence of agar. This point is not addressed in the discussion of Figure 3. The authors should use the same type of odor source to make comparisons across conditions.

4. The behavioral quantification of the chemotactic behavior of C. elegans reproduces a series of results that have already been published. Weathervaning appears to be reproduced, but its strength might be lower than that reported by IIno and Yoshida 2009. It would be helpful if the authors could present a graph with the average curvature rate as a function of the bearing of the gradient to permit a comparison with Iino and Yoshida 2009.

In contrast with the behavioral quantification of C. elegans, the behavioral quantification of larvae is minimal. Essentially, the authors report that larvae turn less while moving upgradient and turn more while moving downgradient. This quantification does not justify the highly-quantitative assay introduced in the manuscript. In addition, could the authors show that larvae are capable of "weathervaning"? Another interesting application of the assay would be to establish how the navigational performances of larvae change with the steepness (or other geometric features) of stationary odorant gradients. This would also show that larvae are capable of precise chemotaxis in gradients that are essentially 1D compared to 2D gradients resulting from point sources.

5. The introduction is slightly misleading. One motivation of the work is to design a setup where measurements of odor concentrations characterizing an odorant landscape can be done during behavioral experiments. One would expect that these measurements would be done in 2D across the assay. Instead, the measurements are made on the border of the arena, which partly contradicts the original goal of the methodology. I appreciate that the presence of the sensors in the arena is not compatible with behavioral experiments, but the implications of this limitation should be more thoroughly discussed in the manuscript. It also reinforces the need to establish the level of fluctuations in odor concentrations inside the arena in real-life conditions.

More generally, how do the authors envision the use of their new methodology by regular labs working on olfaction? If, on the one hand, their primary goal is to propose a technique that will be adopted by many experimental labs, one should acknowledge that most labs might find it challenging to conduct odor measurements, optimize the convection-reaction-diffusion model and simulate new odorant landscapes. Going through the pipeline would require a "tutorial". If, on the other hand, the goal of the methodology is to draw attention on potential artifacts associated with the instability of odorant gradients in published assays, the authors should conduct a more thorough analysis of the stability of representative experimental conditions.

6. Appendix 1 argues that the convection-diffusion model and the reaction-convection-diffusion model are equivalent if the odor flow between the air and agar are in equilibrium. How is this equilibrium defined quantitatively?

Reviewer #2 (Recommendations for the authors):

This manuscript by Chen et al. describes an apparatus for measuring odor-evoked navigation behavior in C. elegans and Drosophila larvae. The major advance is using an array of metal oxide sensors to measure odor gradients. The authors apply this tool to generate stable gradients in an agar environment. They then measure odor-evoked behavior in both worms and fly larvae, demonstrating the ability to recover previously described stimulus-behavior associations such as biased random walking and weathervaning.

The problem of controlling and measuring odor dynamics is a challenge for all studies of odor-guided navigation and new approaches to these problems are welcome. While the present study shows the potential of the metal oxide sensor array approach, several considerations are missing that would help other researchers to evaluate whether this approach would be useful, and are important for evaluating claims made with this device.

1) Metal oxide sensors have previously been employed to measure odor dynamics in turbulent airborne environments (e.g. Schmuker et al. 2016, Tariq et al. 2021, Dinnler et al. 2022). Two major issues raised by these previous studies are that (1) metal oxide sensors have a fast onset but very slow offset which complicates inference of odor dynamics, and (2) sensor drift can complicate absolute concentration measurements. The authors should discuss these previous studies and show data on the temporal resolution and stability of their sensor array in response to more rapid changes in odor concentration.

2) Previous studies have used a spectroscopic approach to quantify odor gradients in agar (Louis et al. 2008). The authors state that this approach is not compatible with simultaneous behavioral measurements, while the metal oxide sensors are, however, it is not totally clear to me why this should be. While a direct comparison of these two methods would be ideal, a more thoughtful comparison of the pros and cons of the two methods would be most helpful to other researchers.

3) A major issue for using the metal oxide sensor arrays during behavior would seem to be the heat generated by the arrays. This should be discussed and any heat effects on behavior should be described, as thermotaxis behavior has been described in both species studied here.

4) It is not clear that this device allows for "precise" measurements at the location of the animal as claimed in the abstract. First, the measurements are in the air and are predicted to be related to the concentration in agar through a scalar. Second, measurements are made at the edges of the agar plate and internal concentrations are inferred. Although these appear to be stable in the absence of animals, local fluctuations due to animal movement cannot be measured.

Suggestions:

The focus of this study is on animals that move in a viscose substrate such as worms and larvae, where odors form stable gradients. While this is implied by the term "small model organisms" the authors should distinguish this from animals other than small model animals (adult flies, larval fish) that move in turbulent environments where the temporal resolution of the system would need to be much higher.

The ability to measure odor-evoked behavior in two species in response to the same environment seems like a bit of a missed opportunity here. Can the behavior of both species be analyzed using the same methods and similarities and differences in behavioral algorithms described?

Overall I think this is an interesting approach but I think there are a large number of specific claims that need to be softened or toned down:

line 18: "Crucially and unlike previous methods, our method allows continuous monitoring of the odor profile during behavior" I don't think this is true. For example, the Vickers and Baker 1994 study used an extra moth antenna to measure odor plume fluctuations in flying moths, and the Tariq 2021 study measured odor at the location of a navigating mouse using metal oxide sensors.

line 23-24: "accurately inferred" "precise odor concentration" not sure these are true for the reasons listed in 4 above.

line 35-36: "small mode organisms" I guess this means worms and larvae but I think it would be helpful to specifically say animals that move in a substrate or mostly navigate in gradient (as opposed to turbulent) environments.

line 46: "no technique currently exists for precise control and continuous monitoring of an odor landscape." This is not true either. Many published approaches here include optogenetics to create virtual environments, precise generation of odor waveforms, controlled flow chambers, etc.

line 97: "odor profile in the chamber" I think the abstract implies that you can make precise measurements at the location of the animal but it is clearer later on that these are inferred measurements across the arena.

line 160: "quantifying airborne odor concentrations" There is a large literature on this in the turbulent navigation field that is not cited or discussed in this paper.

line 175: "metal oxide sensors" can you give estimates of cost, sensitivity, odor selectivity, and temporal resolution? I would expect this to be in a supplement.

line 204: 1-second temporal resolution. What is the evidence for this? Is this a sampling rate or does it take into account the dynamics of the sensor as shown in the Tariq paper?

line 251: "remove two sensor bars and replace them with agar" I think it needs to be clearer upfront that the sensors have to be removed to do agar measurements.

line 371: butanone chemotaxis in Drosophila larvae. should cite the Jung and Bhandawat 2015 paper here that closely examines butanone-evoked navigation in adult flies and compares it to vinegar-evoked navigation.

line 399: "This last feature…sets this method apart from previous approaches" It is not clear to me why the spectroscopic approach could not in principle be used during behavior.

line 405: "In the future, such tuning curves may form the basis of investigations into neural mechanisms driving the sensorimotor transformations underlying navigation" Lots of this has been done! Seems weird to say this as a future thing and not cite the many many circuit cracking papers in worms and flies that have been pursued with other apparatus.

lines 438-440: "at the quasi-equilibrium conditions used in our experiments the odor concentration in agar is related to the airborne odor concentration directly above it up to a scalar that we predict to be constant across the agar." But is this actually true? This is quite far from the claim in the abstract that you can precisely measure the concentration at the location of the animal.

Reviewer #3 (Recommendations for the authors):

In this paper, Chen et al. propose a new method to measure odor stimuli in space and time. Measuring the odor stimulus is a key step in interpreting odor-driven behavior and understanding the neural mechanisms that mediate it, but this task still challenges every experimenter in the field. As described in the introduction, there is basically not a single method that is good for most behavioral assays, even when these involve small animals such as C. elegans and D. melanogaster. Previous approaches are either invasive, very expensive, or limited to very small behavioral arenas. The strength of the proposed method is to be cheap and to have a reasonable spatial (1 cm) and temporal (1 s) resolution. The full sensor array introduced here cannot be located throughout the behavioral arena, but a mathematical model shows that it is sufficient to measure the odor stimulus at certain specific positions to reconstruct the full spatial profile. In other assays, such mathematical considerations might not be possible and physical constraints might make it impossible to use the sensor during behavior, however, it can still be used to measure the odor landscape in a separate experiment, and, with a certain degree of reproducibility (which will depend on the specific delivery system), this is still better than no measure. It should be noted that the method is limited to 2D measurements, which is sufficient for the walking or crawling behavior of small animals in non-turbulent conditions, but it cannot be extended to 3D assays. It remains moreover unclear what is the sensitivity range of the sensor for the odors used in the paper (butanone and ethanol) and what is expected for other odorants (which compounds are detectable?).

As proof of principle, the authors use this new method to characterize the behavior of C. elegans and D. melanogaster as a function of the concentration gradient encountered along their moving trajectories. In this respect, it remains unclear whether the method allows new conclusions or simply recapitulates previous observations.

Sensors:

It would be important to know more about the sensitivity range of the sensors. It seems that the concentration used here does not saturate the sensors: what is the full scale of sensitivity for the x-axis in Figure 1- S1? Is the calibration curve similar for ethanol? And what kinds of odors are expected to be detectable?

Another point that is not mentioned is whether the sensor itself affects the odor stimulus: for example, through an absorption/release mechanism similar to what happens with the agar: I guess one should compare Figure 2a to Figure 4b? No interference with the stimulus would be a clear advantage of this approach over the PID and should be stated.

Behavioral analysis:

Regarding the paragraphs on C. elegans and D. melanogaster, I would suggest that the authors clarify what is a new finding vs what is already known, and in which cases the measurement of the odor gradient is critical.

Clearly, Figure 7 requires such measurements; however, the significance of the result is somehow obscure: what do we expect for the relationship between drift velocity and gradient? Also, there seems to be a very small and possibly not significant (I do not find a statistical test) positive drift for the high range of the tested gradients: could these gradients be too shallow?

Is the same analysis of drift vs gradient not possible with D. melanogaster? Moreover, I wonder why the turn rate for -90 and 90 degrees do not have similar values: both directions are perpendicular to the gradient, wouldn't one expect the same behavior? The heading change, in that concern, is as expected, with similar absolute value and opposite direction. Also unclear why the heading change is similar for 180 and 0 degrees.
