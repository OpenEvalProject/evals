# Peer review - Round 1

Editors:
- Tatiana Pasternak, https://ror.org/01s5ya894 National Institute of Neurological Disorders and Stroke United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72136.sa0](https://doi.org/10.7554/eLife.72136.sa0)

The final revision of the manuscript addressed the remaining issues raised by the reviewers. They felt that the paper is an important contribution to the field, providing new and testable insights into the interaction between cortical areas during the memory delay and that the work is likely to become "an influential reference for future modeling efforts" and deserves publication in eLife.


---

# Peer review - Round 1

Editors:
- Tatiana Pasternak, https://ror.org/01s5ya894 National Institute of Neurological Disorders and Stroke United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72136.sa1](https://doi.org/10.7554/eLife.72136.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mechanisms of distributed working memory in a large-scale network of macaque neocortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tirin Moore as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The manuscript was well received by the two reviewers who felt that the large-scale distributed model of working memory has major strengths and fills an important gap in the literature. However, they also had a number of reservations and made suggestions which must be addressed for the manuscript to be accepted for publication in eLife.

Both reviewers were concerned about the lack of consideration of recent work documenting the existence silent delay activity. The concern is that the proposed model relies heavily and exclusively on persistent attractor states and the impression the manuscript created that these states are the only current thinking about working memory.

The reservations raised by the two reviewers are summarized below and along with the original critiques will provide the guide to the revision, should you decide to revise the manuscript.

1. Both reviewers recommend that the work is re-framed by taking into account newer studies and asked the authors "consider changing the tone of manuscript, so that it doesn't come across as if persistent attractors are state-of-the-art thinking about working memory".

2. Abstract, Introduction and Discussion

Please clarify in the Introduction and in Discussion that you are testing one model of working memory and acknowledge that there are other models that consider more complex dynamics of activity recorded during the delay. Also, please incorporate into the Abstract and Introduction the effects of deactivation and resistance to the distractors tested by your model.

3. Please address the point questioning the idea that "anatomical constraints" actually play a critical role in the model. If they are indeed critical to the model, provide documentation.

4. Consider moving the simplified model into the Supplementary Materials.

5. Discuss whether and how the proposed model explains extensive reports of silent periods in delay activity. A related issue is to what extent the proposed model depends on persistent activity and whether it can incorporate an STP.

6. In the Discussion please expand the point already made in the manuscript that "silent activity periods associated with silent WM (Masse et al., 2019; Mongillo et al., 2008; Stokes, 2015) could also be due to distributed WM effects".

7. Please provide the definition of "persistent" activity and consider the recommendation to change "persistent" to "elevated" or to "delay activity. Please also address the comment that past observations of "persistent" activity were based on activity averaged across trials, rather than on a trial-by-trial basis.

Reviewer #1 (Recommendations for the authors):

Overall the interesting findings seem to be obfuscated by seemingly not so relevant ones. For instance, both the abstract and introduction seem to ignore a main finding, which is the deactivation of the attractor by inactivating the top area. CIB and more resilience to distractors is not properly introduced, either (however mentioned in the abstract). Instead, the authors give relevance to a concept already in the literature, ie bistability accomplished through inter-area connectivity (Eding et al., PNAS, Guo et al., Nature) and to the fact that the model is “anatomically constrained”, which it is not clear that is indeed the case.

Anatomical constraints.

The abstract reads: “we developed an anatomically constrained model” but it is not clear in what ways the anatomical data constrains the main model. Indeed, in a supplementary figure and in the simplified model the authors show that it does not seem to matter much “Similar conclusions can be obtained when the anatomical structure of the cortical network is changed -for example, by randomly shuffling individual projection strength values”. This raises the question of which of the new insights depend on this and other “biological constraints”. Namely: “counterstream inhibitory bias”, superiority of distributed WM in resisting distractors, deactivation of global attractor by silencing a top layer, inactivation relationship with specific areas, etc. Each finding should be accompanied by how they are affected by including or not specific “biological constraints”. If some, like anatomical connectivity, are not critical, then they obfuscates the main findings and worsens the overall readability of the paper (which is very good, but a bit long) and could be removed or moved to a supplementary figure showing unequivocally in what ways it does (not) constrain the model. It is somewhat acknowledged in the paper that the main driver of the findings is the gradient of recurrent excitation (“As a matter of fact, the relevant parameter here is the strength of synaptic excitation that varies across cortical space, in the form of a macroscopic gradient”), but this is not very clear at times. Again, if this is indeed the case, less emphasis should be given to the anatomical “constraints” and instead the relevant feature should be spelled out clearly and early on (in the abstract and intro)

Simplified model.

It is not very clear what we gain with this model, if not to show that with homogeneous coupling (instead of heterogeneous from experimental data, see above) similar findings are achieved. The model is motivated by “The above model, albeit a simplification of real brain circuits, includes several biologically realistic features, which makes it difficult to identify essential ingredients for the emergence of distributed WM.” This seems a good reason to remove the “biological constraints” from the “full model” (see above). Additionally, because of where this model is introduced in the paper, it becomes unclear when the simplified or the full model is used in the following figures. This could be improved if the simplified model was introduced only in the supplementary material or in a subpanel with a clear title. At a minimum, all captions should say if the full/simplified model were used.

Previous experimental literature.

Overall we feel that several studies were not properly considered. For instance, Guo et al., Nature is not cited properly, nor discussed. Note for example that also in this paper there was a model – in addition to clear empirical evidence – with different areas and similar concepts as the ones that are explored here.

Likewise, both "Cortical information flow during flexible sensorimotor decisions" Markus Siegel et al., Nature and also Panichello and Buschman, Nature were not considered in this study. In both studies, they recorded from several areas across the hierarchy (from visual cortex to PFC) during WM and DM, so they seem to be extremely relevant, especially to constrain the model further in future studies. For example, Panichello and Buschman show clear WM codes in V4, not present in the current model. Another example: "We observed (…) a sharp binary jump of activity, areas like LIP exhibited a more gradual ramping activity, resembling temporal accumulation of information in decision-making(Shadlen and Newsome, 2001)". Siegel et al., Science show very convincing evidence that this is actually not the case and the model does not seem to match the latencies reported here.

Of course, this mismatch between data and model is not very important and it does not reduce the value of the current model, but the authors should consider toning down claims like "strong agreement with" or "an excellent agreement with a large body of data, from decades of monkey neurophysiological" which occur throughout the study. The model is a great proof of concept that provides several important insights, but it is far from being in "strong agreement" with what happens in the brain.

Somatosensory WM.

Relatedly, the authors perform an experiment that simulates "somatosensory WM". While the question as to which areas trigger the global attractor is interesting and would deserve to be explored further, the way this is framed (i.e. studying different WM modalities) is misleading and should be adapted. Figure2—figure supplement2 shows that the same global attractor is engaged irrespectively of which area is stimulated. The evidence points otherwise (see Christophel et al., 2017). For example Figure2—figure supplement2 shows persistent activity in IT, which would not be expected for somatosensory WM?

Inactivations.

It would be nice to have a schematic of when this inactivation is performed (which we think it is throughout the trial), like in FIGURE 7. It seems that the point made in fig6 C needs the areas to be silenced in the opposite direction (ie hierarchical order) to be conclusive. Figure F seems important, as well as the result in G, but it is very confusing. We would consider simplifying it to show more clearly the relevant features/points made. Again: how much of the findings (in particular the "bowtie" analyses) here depend on the "anatomical constraints" is unclear.

"which is in agreement with classical prefrontal lesion studies(Curtis and D'esposito, 2004)" The cited paper does not do what the authors did in the model. This line should be removed of better explained

"In some cases, inactivating specific areas might even lead to a disinhibition of other areas and to a general reinforcement of the attractor". Again, unclear why this is. Does this depend on gradient of recurrent excitation, hierarchy location or anatomical connectivity?

Relationship with other mechanisms of working memory.

This paragraph, while important, seems a bit incomplete in the current form. In particular the part where activity-silent is discussed. The results presented here seem to depend strongly on the persistent activity hypothesis of working memory. Does it make sense to think about distributed attractors through short-term plasticity? The relationship with silent activity does not seem straightforward and this discussion failed to illuminate it.

In the next paragraph, the authors say "This also means that silent activity periods associated with silent WM (Masse et al., 2019; Mongillo et al., 2008; Stokes, 2015)could also be due to distributed WM effects. Optogenetic inactivations could be used to test this result." This is an interesting idea, but could be expanded a bit more. Intriguingly, the authors cite papers (Masse et al., 2019; Mongillo et al.,) of local circuits with actual activity-siment mechanism. Instead, the author should cite empirical evidence of silent periods, of which the model proposed here offers an alternative view. For example: Wolff et al., Nature Neuroscience (Human occipital cortex), Barbosa et al., Nature Neuroscience (monkey PFC) and Akrami et al., Nature, (rodent PPC) etc.

Reviewer #2 (Recommendations for the authors):

I am not suggesting that the authors overhaul their model and start over. But a re-write (and some changing of terms, see below) would serve them well. I would encourage the authors to consider changing the tone of manuscript so that it doesn't come across as if persistent attractors are state-of-the-art thinking about working memory. I suggest a more up-front acknowledging of the newer developments (as opposed to a single paragraph near the end of the Discussion) and that their work will focus on mechanisms that allow average activity to remain elevated. Right now, it reads as if "persistent activity" is everything, with a disclaimer near the end.

Finally, I encourage the authors to not use the term "persistent activity" (try elevated or sustained elevated activity or just "delay activity"). As noted above, there is evidence against persistent activity. But more to the point, there is little or no evidence for persistent activity. Virtually all of the work purporting such evidence averaged neural activity across multiple trials. Across-trial averaging masks more complex dynamics like gaps of no spiking. One cannot conclude persistent firing from averaged data. It can only be addressed in real time at the single trial level. Also, there is a no definition of "persistent". Is it a spike every 5 ms? Every 10 ms? Every 100 ms? Using a term like "persistent activity" when it is not well defined and for which there is little direct evidence muddies the waters and does not do a service to the field.

Other comments:

One cannot help but wonder how the hierarchical trends discussed here relate to other hierarchical trends. For example, there is a gradual progression from sensory-related activity to task-relevant activity as one ascends the hierarchy. Or the greater mixed selectivity in higher cortex. Maybe those are separate issues. But if the authors have any insights into how their model contributes to them, it would certainly add value to their manuscript.

Page 4: "LIP exhibited a more gradual ramping activity, resembling temporal accumulation of information in decision making (Shadlen and Newsome, 2001)". Again, this was state-of-the-art like a decade ago. It ignores more recent work by Pillow, Shenoy, and others showing that the ramp-up is not gradual. When examined on the single-trial level, the activity is instead a series of discrete state changes. This does not take anything away from the elegant and important work of Shadlen and Newsome, without which the newer work would not have been possible. But, again, by focusing on older, not newer, work, the authors are not giving a full account of where we are in 2021.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mechanisms of distributed working memory in a large-scale network of macaque neocortex" for further consideration by eLife. Your revised article has been evaluated by Tirin Moore (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewers were largely satisfied with the revised manuscript with one exception. They were concerned about the discussion of the role of plasticity in Attractor and Activity-Silent models (lines 559-566). It was felt that the work referred to in the Wang recent review which showed more spiking activity during manipulation of working memory, did not rule out synaptic plasticity. Furthermore, it was pointed out that Activity-Silent models also predict that spiking may be used to "ping" the network and read out the memories. In this case, the role of plasticity is to HELP the spiking, not to replace it.

To address this concern, this section should be modified. One option would be to provide clear evidence that synaptic plasticity only holds for Activity-Silent models and is not required by the attractor models. This can be done by citing specific references with the appropriate simulations/data or by providing new simulations/data.

Alternatively, this paragraph should be modified by allowing short-term plasticity to play a role in both types of models.

Reviewer #1 (Recommendations for the authors):

With most of my initial concerns addressed and the inclusion of interesting, new simulations, I fully support the publication of the manuscript in the current form.

Reviewer #2 (Recommendations for the authors):

The authors' revisions are mostly adequate.

However, the statements that activity-silent models " (1) it cannot filter out distractors that occur later in time than behavioral relevant stimuli, (2) it does not have a severely limited capacity (a characteristic of working memory) and (3) it is incapable of internal manipulation of information" is not true.

The activity-silent models can explain all of this. Synaptic weight changes are driven and refreshed by spiking. Thus, they have the same features and same control as attractor-state models. 1. Distractors can be filtered out by controlling spiking. 2. They do have a severe capacity limitation due to limitations in the spiking refresh rate. Multiple memories cannot be in the active state at the same time. That leads to capacity limitations. 3. Manipulation of WM is achieved by controlling spiking episodes, just like the attractor-state models.

The issue is that in testing the activity-silent models, the author has shifted too much of the burden to synapses alone. That is a misrepresentation of the activity-silent models. It is easy to refute a model if one makes a straw model of it. In the activity-silent models, synapses don't do everything. The help activity by briefly carrying the memories between spiking. That is why they are also referred to as "synaptic attractor" models. Because they also involve attractor states, they have many of the same features and mechanisms as attractor-state models. As a wise colleague recently said, the attractor-state and synaptic-attractor models are more similar than different. The characterization that the former can explain a variety of WM phenomena but the latter cannot is not accurate.

I think this is a valuable review. It is well-written. Attractor dynamics are indeed important and the review offers important insights. But surely these insights can be offered with misrepresenting other models.
