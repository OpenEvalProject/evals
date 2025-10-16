# Author response - Round 1

Authors:
- John P Liska
- Declan P Rowley
- Trevor Thai Kim Nguyen ([ORCID: 0009-0005-3277-9535](https://orcid.org/0009-0005-3277-9535))
- Jens-Oliver Muthmann ([ORCID: 0000-0002-0439-9704](https://orcid.org/0000-0002-0439-9704))
- Daniel A Butts ([ORCID: 0000-0002-0158-5317](https://orcid.org/0000-0002-0158-5317))
- Jacob Yates ([ORCID: 0000-0001-8322-5982](https://orcid.org/0000-0001-8322-5982))
- Alexander C Huk ([ORCID: 0000-0003-1430-6935](https://orcid.org/0000-0003-1430-6935))

## Response text

DOI: [10.7554/eLife.87736.3.sa4](https://doi.org/10.7554/eLife.87736.3.sa4)

The following is the authors’ response to the original reviews.

Reviewer 1(Public Review):

“but an obvious influencing factor that the authors could investigate in their own data set is the retinal input. In Fig1b, the authors even show these data in the form of gaze and pupil size. In these example data, by eye, it looks like the pupil size is positively correlated with the run speed. This would of course have large consequences on the activity in V1, but the authors do not do anything with these data. The study would improve substantially if the authors would correlate their run speed traces with other factors that they have recorded too, such as pupil size and gaze.”

Absolutely. We have added a first level of eye movement (and pupil size) analyses to the revised manuscript, resulting in an additional figure. In short, we found that eye movements are unlikely to play a significant role in our primary results, as the patterns of eye movements differed only slightly between running and stationary periods, and the measured impacts of such eye movements were also quantitatively much smaller than the primary effect sizes.

We also note that in analyzing the eye movements, we also found that pupil size was larger during running than stationary. This is suggestive evidence that running is correlated with increases in arousal. Although more work will be needed to calibrate and quantify how much this factor affects neural responses (and perhaps to dissociate it from running per se), the simple analysis we present suggest that the large differences we observe could be explained by a difference between how arousal and running are correlated in the monkey versus the mouse. Instead, it appears that both species have at least qualitatively similar relations between pupil size (a standard proxy for arousal) and running.

On this issue, we have added extensive discussion of the relevant recent work by Talluri et al. (2023) who attempted a similar cross-species analysis that considered spontaneous body movements and their effect on cortical activity (as well as the possibility that eye movements are a critical mediator in these modulations). Due to delays in revising our manuscript, we regret that our earlier submission had not cited this work, but we now do our best to highlight its importance and the synergy between these two papers. The full citation is listed below:

Talluri BC, Kang I, Lazere A, Quinn KR, Kaliss N, Yates JL, Butts DA, Nienborg H. Activity in primate visual cortex is minimally driven by spontaneous movements. Nat Neurosci. 2023 Nov;26(11):1953-1959. doi: 10.1038/s41593-023-01459-5.

There is a finer level of analysis that we hope to do in the future along these lines. It would rely on detailed characterization of each receptive field, building an image-computable model linking those receptive fields to the neural activity, and doing so at a finer time grain that links individual eye movements and changes in the spike train within a stimulus presentation (as opposed to working at the level of spike counts per stimulus presentation). Because these steps need to be accomplished together— and each requires substantial additional work and would go beyond the first-order findings we report in this work— we hope to report on such finer analyses in a standalone paper later. We are working on being able to do this in both marmoset and mouse.

More generally, we want to emphatically agree that what is missing from this paper is the “why?”! We have done our best to show that a fair comparison reveals quantitatively different phenomena in marmoset and mouse. In the revised discussion, we lay out many lines of work that we hope will gain traction on this deeper mechanistic point. There’s a lot to do, and several of the possibilities are already current topics of exploration in our ongoing work.

“Looking at the raster plot, however, shows that this strong positive correlation must be due entirely to the lower half of the neurons significantly increasing their firing rate as the mouse starts to run; in fact, the upper 25% or so of the neurons show exactly the opposite (strong suppression of the neurons as the mouse starts running). It would be more balanced if this heterogeneity in the response is at least mentioned somewhere in the text.”

We are also intrigued by the heterogeneity of effects at the single neuron level. That is why the next section of the paper is dedicated to analyzing effects on a cell-by-cell basis. The fractions of neurons showing either increases or decreases are described separately, to get at this very issue.

Reviewer 2 (Public Review)::

“For example, it is known that the locomotion gain modulation varies with layer in the mouse visual cortex, with neurons in the infragranular layers expressing a diversity of modulations (Erisken et al. 2014 Current Biology). However, for the marmoset dataset, it was not reported from which cortical layer the neurons are from, leaving this point unanswered.”

Reviewer 2 called for more consideration of details that have been addressed in the mouse literature, such as the cortical layer of the cells, and related aspects of circuitry. We have greatly re-worked the Discussion to address several of these issues. In short, the manuscript’s set of data were collected without strong traction on layers or cell types, and it will be quite interesting to get a better handle on this using both refinements to our recording procedures as well as new techniques that are now possible in the marmoset for future studies.

“In this regard, it is worth noting that the authors report an interesting difference between the foveal and peripheral parts of the visual cortex in marmoset. It will be interesting to investigate these differences in more detail in future studies. Likewise, while running might be an important behavioral state for mice, other behavioral states might be more relevant for marmosets and do modulate the activity of the primate visual cortex more profoundly. Future work could leverage the opportunities that the marmoset model system offers to reveal new insights about behavioral-related modulation in the primate brain.”

Same page! We have expanded the discussion to better emphasize these points and are already deep in follow up experiments to explore the foveal and peripheral representations.

Reviewer 3(Public Review):****:

“However, the authors did not take full advantage of the quantity and diversity of the marmoset visual cortex recordings in their analyses. They mention recording and analyzing the activity of peripheral V1 neurons but mainly present results involving foveal V1 neurons. Foveal neurons, with their small receptive fields strongly affected by precise eye position, would seem to be less likely to be comparable to rodent data. If the authors have a reason for not doing so, they should provide an explanation.”

We agree, and hope the reviewer finds our overall reply, detailed response to Reviewer 1 (who raised a similar issue), and corresponding updates to the manuscript appropriate for this stage of understanding.

“Given that the marmosets are motivated to run with liquid rewards, the authors should provide more context as to how this may or may not affect marmoset V1 activity. Additionally, the lack of consideration of eye movements or position presents a major absence for the marmoset results, and fails to take advantage of one of the key differences between primate and rodent visual systems - the marmosets have a fovea, and make eye movements that fixate in various locations on the screen during the task.”

In addition to the response above, we have made edits to the manuscript to speak to issues of arousal and eye movements (also detailed in previous responses). Given the modest decrease in activity we see, the usual concerns about potential increases in neural activity related to eye movements (which we quantify in the revision) and other issues related to motivation are hard to specifically relate to existing literature. But in the revised Discussion we talk more about how future work can/should dissociate these factors, as has been done in the mouse literature.

“Finally, the model provides a strong basis for comparison at the level of neuronal populations, but some methodological choices are insufficiently described and may have an impact on interpreting the claims.”

We have also clarified the shared-gain model’s description, which we agree needed additional detail and clarification.
