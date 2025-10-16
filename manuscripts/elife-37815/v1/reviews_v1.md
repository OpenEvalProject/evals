# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37815.024](https://doi.org/10.7554/eLife.37815.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Elementary sensory-motor transformations underlying olfactory navigation in walking fruit flies" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ronald L Calabrese as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors present a creative analysis of fly walking navigation in response to an attractive odor (apple cider vinegar, ACV) in a mini wind tunnel that creates a boundary layer odor plume in which the fly is constrained to walk. Flies were placed in the rectangular arenas, where they were exposed to a constant flow of filtered, humidified air, defining the wind direction. Into this airflow pulses of odor were injected with rapid onset and offset kinetics, producing a front of odor that was transported down the arena at 11.9 cm/s. The odor dynamics were monitored by a photo-ionization detector (PID). They also constructed and tested flies in larger wind tunnels capable of delivering a turbulent boundary layer odor plume after the mini wind tunnel results. They also developed a simple computational model of how odor dynamics and wind direction influence changes in forward and angular velocity to simulate results in both types of wind tunnels. All flies tested were genetically blinded. Behavioral results with odor pulses show that flies have two basic responses with odor onset flies orient upwind and increase their ground speed (on response), and with odor offset, they reduce their ground speed and increase their rate of turning (off response). By mechanically blocking antennal wind sensation, they show that antennal mechanosensation is required for the directional components of these behaviors – on response, while odor offset is sufficient to induce changes in ground speed and turning – off response. Using time-varying odor stimuli, they show that the responses, on and off, low pass filter the odor dynamics and fitting their model they estimate 0.72 s and 4.84 s time constants respectively and that both responses show adaptation to odor with a time constant around 10 s. With the model they show that simulated flies respond similarly to the mean of all flies and that by simply changing the gains of the on and off responses they can capture individual variation about this mean. They then test files in the turbulent plume of the larger wind tunnel and find that their model can likewise capture their behavior including failures to find the odor source. They conclude that integration over time may be a useful computational strategy for navigating in a boundary layer plume, allowing flies to head upwind more continuously in the face of odor fluctuations, and to generate re-orientations clustered at the plume edges. The impact of the paper is in reducing walking navigation in a turbulent boundary layer to two basic stimulus driven responses one bi-modal (wind and odor on response) and one unimodal (odor off response) and providing a simple model to show how these responses interact in real odor plumes. They recognize that their analyses/conclusions are a first order approximation and that other variables/responses can be considered in future but nevertheless, the work is a major step forward in walking odor navigation and should be of wide interest in the behavioral neuroscience community.

Essential revisions:

1) As stated in the shortened review of reviewer 2, the authors should consider experiments in which one antenna is blocked; mechanoreceptors and potentially also olfactory receptors. These experiments will address the contribution of bilateral antennal sampling, which is known to be important in flies and other insects.

2) There are concerns that using only blind flies may influence the navigation strategy observed. Any data from sighted flies that could be included should be, or the potential implications of blindness should be more extensively discussed.

3) As stated in the shortened review of reviewer 3, the model should be better clarified and the parameters better rationalized.

4) The Discussion should more extensively discuss the type of navigation the flies are doing here better in the context of flight navigation.

Reviewer #2:

- In past work, several labs have reported the contribution of bilateral sampling (stereo-olfaction), from the pioneering work of Axel Borst in 1983 to the recent optogenetic-stimulation experiments conducted by Gaudry and Wilson. The fact that this aspect of the navigation mechanism is not addressed in the present manuscript represents a weakness. It seems that the author could have tested relatively easily the behavior of unilaterally wind-blind flies. They could then ask whether up-wind surges are possible with a single functional antenna, whether unilaterally wind-blind flies display a turn bias, etc. Likewise, unilateral olfactory impairment could have been produced through mechanical impairments (Duistermars and Frye, 2009). Combining these results in the model would nicely complete the present analysis. Although this weakness is minor, the authors are encouraged to address it.

- The use of blind (norpA) mutants in the olfactory navigation experiments is sensible. I was nonetheless wondering whether the authors have any evidence that the orientation strategy of blind flies is the same as wild-type flies? It is known that vision plays an important role for flying Drosophila to pinpoint the location of a food source (Saxena and Sane, 2018). Blinding walking flies might therefore affect their natural responses to olfactory simulations.

Reviewer #3:

1) The modeling part should be strengthened: while it is understood that the model is empirical, some more intuition and details would definitely help.

Two different filters are being used for the ON and the OFF. What is the logic and the reason for these two different choices, namely the subtraction in the OFF? It would also be useful if the filters in Figure 4 looked more what they really are, to avoid possible confusion.

It is mentioned that the distribution of angular velocities is not matched to the data. How is this discrepancy rationalized? There are also other discrepancies, e.g. in the timing in Figure 4. While the desire to highlight positive results is comprehensible, those limitations are equally important for a global understanding, and should be mentioned in the discussion.

The model has a number of parameters that are empirically tuned. Any insight and comment on how they are affected if the source intensity and/or the wind velocity and/or the fluctuation level are modified would be useful, and again help the reader rationalize the empirical findings.

How is the decrease in Figure 3A-B rationalized?

The finding that local search is not influenced by the wind is particularly interesting. What does that imply for the turns that the fly is making? Are they oriented with respect to the exit direction of the insect from the plume?

2) The presentation and the discussion on conditions of the walking flies' olfactory searches need improvement and clarifications.

Odor detections and turbulence at 50m (in the atmospheric boundary layer) are not like at 50cm from a source (in a boundary layer). It should be stressed that searches for walking flies are happening at sub-meter distances and clear distinctions with the situation of moths (where searches are over tens or even hundreds of meters) should be made. This is not done in the present version, where the introduction focuses on laminar vs turbulent conditions only, and there is no mention of this basic fundamental difference between moths and walking flies.

The last paragraph of subsection “Temporal features of odor driving ON and OFF behaviors”, is another illustration of the above point. The discussion proceeds on the basis that odor detections experienced by moths and walking flies are similar, which is far from being the case. At tens/hundreds of meters, the size of the odor filaments is very small, and the plume is broken up, contrary to what happens at 50cm. A sense of the differences between typical durations of whiffs for the two situations is provided by the comparison between Figure 3 and Figure 4 in Phys. Rev. X, 041015 (2014). The peaks in the two distributions differ by two orders of magnitude, which is theoretically understood by the very different properties of transport at those distances.

Another difference is that at 50cm, inside the plume the level of concentration is fluctuating but detections are essentially continuous. The only way to lose the signal is to cross the well-defined border of the plume (which is again not the case at tens of meters, where the plume is genuinely broken up). This makes that the main issue of the search, even in the presence of turbulence, is to keep contact with the continuous trail, i.e. not that different from the tracking of a laminar tube. While the continuity of detections is somehow witnessed by Figure 6J, it should be made more explicit. It would also be useful to add to Figure 6A a plot of the signal on the scale of the detection level Kd defined in Eq. (7) (which is what really matters). Finally, the work Curr. Biol. 26, 1261, 2016 should be mentioned as it also deals with similar distances (for rodents) and shows that there is enough signal to permit even gradient-climbing searches.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Elementary sensory-motor transformations underlying olfactory navigation in walking fruit flies" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Please respond to the reviewer comments below. These should be quick to accomplish and will not require re-review.

Reviewer #2:

The authors have revised their manuscript in a way that addresses the concerns I (reviewer 1) raised in my first report. The technical limitations that prevented them to carry out unilateral olfactory stimulation experiments are reasonable. Instead, the authors take advantage of their computational simulations to determine the potential contribution of bilateral sampling to the navigational performances. The results described in the new Figure 7 represents a great addition to the manuscript – I praise the authors for including this new material. What I am not entirely following is the choice of w1118 as the background of the sighted control. w1118 is obviously the right genetic background for the "sighted control", but the w1118 allele affects the visual system of the fly. Since the white-eyed phenotype was not used to keep track of the norpA mutation, I am unsure why w1118 was used as the background of the tested flies in the first place. This choice cannot (and might not have to) be changed, but the authors should consider justifying the use of w1118 background in the Materials and methods section (other readers might be puzzled as well). While it is true that the sighted control demonstrates ON and OFF responses, blindness produces significant behavioral differences that the reader should keep in mind. It might be worth mentioning this point again in the Discussion section.

Reviewer #3:

The authors have taken into account most previous comments in a satisfactory way. The logic of the choice of the parameters, filters, etc., is more transparent. The Discussion section has improved and the Introduction makes clearer the conditions of the search.

The authors have not modified Figure 6. I disagree with their argument since the mean profile is quite relevant at those distances, as their work also shows. However, this is not my paper and since the point can be grasped alternatively (even though less transparently), I shall not insist.

The authors have included the comment: "Second, plumes developing near a boundary are broad and relatively continuous, while those in open air, particularly at the long distances covered by moths, are much more intermittent", which is good. Adding also a reference to older experimental data, e.g. Yee et al.,(1993), would be useful.
