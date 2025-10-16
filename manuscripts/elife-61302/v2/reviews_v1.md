# Peer review - Round 1

Editors:
- Kassandra M Ori-McKenney, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61302.sa1](https://doi.org/10.7554/eLife.61302.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using a combination of genetic, cell biological, and cutting-edge imaging techniques, this paper defines the individual and cooperative roles of the microtubule motors, kinesin-1 and kinesin-3, in vesicle transport. Although multiple motor populations exist on the same cargo, how distinct motors compete and cooperate to ensure efficient transport are open questions. By precisely analyzing motor position on Rab6 vesicles, this study helps to elucidate the contribution of these different kinesin motor classes to controlling vesicle size, driving regional transport, and opposing dynein in a tug-of-war scenario, thus providing new insights into multimotor cargo transport.

Decision letter after peer review:

Thank you for submitting your article "Concerted action of kinesins KIF5B and KIF13B promotes efficient secretory vesicle transport to microtubule plus ends" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Suzanne Pfeffer as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Serra-Marques, Martin et al. investigate the individual and cooperative roles of specific kinesins in transporting Rab6 secretory vesicles in HeLa cells using CRISPR and live-cell imaging. They find that both KIF5B and KIF13B cooperate in transporting Rab6 vesicles, but Eg5 and other kinesin-3s (KIF1B and KIF1C) are dispensable for Rab6 vesicle transport. They show that both KIF5B and KIF13B localize to these vesicles and coordinate their activities such that KIF5B is the main driver of the cargos on older, MAP7-decorated microtubules, and KIF13B takes over as the main transporter on freshly-polymerized microtubule ends that are largely devoid of MAP7. Interestingly, their data also indicate that KIF5B is important for controlling Rab6 vesicle size, which KIF13B cannot rescue. By analyzing subpixel localization of the motors, they find that the motors localize to the front of the vesicle when driving transport, but upon directional cargo switching, KIF5B localizes to the back of the vesicle when opposing dynein. Overall, this paper provides substantial insight into motor cooperation of cargo transport and clarifies the contribution of these distinct classes of motors during Rab6 vesicle transport.

Revisions for this paper:

1) The metrics used to quantify motility are sensitive to tracking errors and uncertainty. The authors quantify the number of runs (Figure 2D, F; Figure 7C) and the average speed (Figure 3A, B, D, E, H). The number of runs is sensitive to linking errors in tracking. A single, long trajectory is often misrepresented as multiple shorter trajectories. These linking errors are sensitive to small differences in the signal-to-noise ratio between experiments and conditions, and the set of tracking parameters used. The average speed is reported only for the long, processive runs (tracks>20 frames, segments<6 frames with velocity vector correlation >0.6). For many vesicular cargoes, these long runs represent <10% of the total motility. In the 4X-KO cells, it is expected there is very little processive motility, yet the average speed is higher than in control cells. Frame-to-frame velocities are often over-estimated due to the tracking uncertainty. Metrics like mean-squared displacement are less sensitive to tracking errors, and the velocity of the processive segments can be determined from the mean-squared displacement (see for example Chugh et al., 2018, Biophys. J.). The authors should also report either the average velocity of the entire run (including pauses), or the fraction of time represented by the processive segments to aid in interpreting the velocity data.

2) The authors show that transient expression of either KIF13B or KIF5B partially rescues Rab6 motility in 4X-KO cells and that knock-out of KIF13B and KIF5B have an additive effect. They also analyze two vesicles where KIF13B and KIF5B co-localize on the same vesicle. The authors conclude that KIF13B and KIF5B cooperate to transport Rab6 vesicles. However, the nature of this cooperation is unclear. Are the motors recruited sequentially to the vesicles, or at the same time? Is there a subset of vesicles enriched for KIF13B and a subset enriched for KIF5B? Is motor recruitment dependent on localization in the cell? These open questions should be addressed in the Discussion.

3) The imaging and tracking of fluorescently-labeled kinesins in cells as shown in Figure 4 is impressive. This is often challenging as kinesin-3 forms bright accumulations at the cell periphery and there is a large soluble pool of motors, making it difficult to image individual vesicles. The authors should provide additional details on how they addressed these challenges. Control experiments to assess crosstalk between fluorescence images would increase confidence in the colocalization results.

4) In Figure 5, it is very interesting that only KIF5B opposes dynein. It would be informative to determine which kinesin was engaged on the Rab6 vesicle before the switch to the retrograde direction. Can the authors analyze the velocity of the run right before the switch to the retrograde direction? If the velocity corresponds with KIF5B (the one example provided seems to show a slow run prior to the switch), this could indicate that KIF5B opposes dynein more actively because KIF5B was the motor that was engaged at the time of the switch. Or if the velocity corresponds with KIF13B, this could indicate that KIF5B becomes specifically engaged upon a direction reversal. In any case, an analysis of the speed distributions before the switch would be provide insight into vesicle movement and motor engagement before the change in direction.

5) In Figure 8G, the tracks for KIF13B-380 motility are difficult to see, which is surprising as KIF13B has been shown to be a superprocessive motor. Is this construct a dimer? If not, do the authors interpret the data as a high binding affinity of the monomer for new microtubules and if so, do they have any speculation on what could be the molecular mechanism? It appears as if KIF13B-380 and EB3 colocalize at the plus ends for a period of time before both are lost but then quickly replenished. Is this common?

6) In general, the reviewers were interested in the localization and velocity of KIF5B vs. KIF13B cargo runs. One reviewer pointed out that in Figure 2E, it seems like about half of the KIF5B events start at or near the Golgi whereas most of the KIF13B events are away from the Golgi? Did the authors find this to be generally true or just apparent in these example images? Furthermore, the results in Figure 8 suggest a potential switch from KIF5B to KIF13B motor engagement upon a change in lattice/MAP7 distribution. Is the velocity of Rab6 vesicles different on central vs. peripheral microtubules? For example, in Figure 4E, are the two examples in different regions of the cell? Do the authors think the intermediate speeds are a result of the motors switching roles? Additional analysis and discussion would strengthen the paper.
