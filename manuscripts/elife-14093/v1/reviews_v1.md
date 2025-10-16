# Peer review - Round 1

Editors:
- Christian S Hardtke, University of Lausanne , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14093.047](https://doi.org/10.7554/eLife.14093.047)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A Stochastic Multicellular Model Identifies Disorders as Biological Watermarks in Self-organized Patterns" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. All reviewers and the editors agree that your work is of potential interest, however they also identified a number of shortcomings that we would like to ask you to address. Please pay attention to the following essential revisions. The reviewers and editors agree that without them, and depending on their outcome, the paper could not be published. They are the following:

1) To convince your audience that your model is capable of the self-organization shown experimentally, you would have to demonstrate that it is able to create a whorled pattern from a random starting point. This is important because a random starting point may change the way the system responds to noise.

2) To demonstrate robustness of the model and its in vivo credibility, we believe it is important that you vary some of the assumptions and parameters in the model, such as the spatial and temporal discretization, the choice of inhibition function (which would vary the nature of the inhibition), and the presence/absence of a secondary mechanism for plastochron control.

Moreover, ideally, you could in addition demonstrate that you get similar results analyzing mistakes in an unrelated system. This would considerably strengthen the credibility of your approach.

Find more details in the reviews pasted below, and please address to your best capacity the other points raised in there.

Reviewer #1:

The authors propose that we can learn something about the mechanism that creates a pattern, not just by looking at the pattern itself, but also by looking carefully at the mistakes it makes. Motivated by recent work, the authors use phyllotactic patterns in order to explore this idea. I find the idea interesting. They suggest that the analysis of the mistakes can help us to understand the mechanism, and they give us an example, the ahp6 mutant, that their analysis shows is more likely the result of a reduction in size of the inhibitory field about primordia, rather than a change in meristem size. This would allow us to distinguish between these two choices. This is not really proof that this is the case, but rather a proof of principle that the idea has discriminating power. In this case there are other possibilities that would need to be excluded, such as increased/decreased noise in location selection due to changes in cell size, or any other input that could affect noise in the system.

I would have like to have seen more exploration of the effect of other model formulations of the model on the results they observe. For example, does the rate of permutations depend on the choice of the inhibition function? What about the spatial and temporal discretization? The growth rate? What does the shape of the curve look like in response to noise in the sampling of the peripheral circle where primordia are formed?

Specific comments:

General: I am not really fond of the comparison to watermarks, I find it a bit misleading as the perturbations are random after all.

Introduction: The presentation in the Introduction suggests that Douady and Couder pioneered the inhibition field model of phyllotaxis. Although they contributed considerably to the field, the authors should perhaps mention at least a few of the others that came before, such as Thornley (1975), Mitchison (1977), Veen and Lindenmayer (1977), Young (1978), Schwabe and Clewer (1984), Chapman and Perry (1987), etc.

Results: The authors write that it has been shown that the central zone is high in auxin. Based on the data, I would say it has been "suggested" or "proposed". Data to support this idea is only from Arabidopsis inflorescense meristem, and from the DII reporter without the recent control construct added by Weijers. The data looks completely different in tomato, where DR5 works just fine in the central zone.

Results: The authors report dislocations in other species, and then immediately assume that it is due to variation in the plastochron. One other possibility could be variations in inhibition threshold. In most inhibition models of phyllotaxis these two are tied together, but that is not necessarily the case in planta. In fact, does not their previous work (Besnard et al. 2014) claim that the timing (i.e. plastochron) is controlled somewhat independently? To report that it is a variation in plastochron, analysis of the timing of primordium initiation at the meristem is required.

Also it is not clear to me from the side views in Figure 2 if these dislocations are just random positioning, or are permutations as stated in the figure caption and text. You would need an image or diagram from the top, or the angles plotted on a graph in order to see if this is the case.

Results: The authors state that the inhibition profile can be seen as an energy. In what sense is it an energy? I think it would be less confusing for the reader, and more accurate to refer to it as the inhibition profile.

Property 2 is reported in the caption for Figure 5G in Smith et al. (2006, CJB), you should probably reference that work in this context.

In a simulation experiment, they perturb the model by initiating primordia at a local inhibition minimum that is not the global minimum and observe recovery. They need the control experiment here. What happens when they initiate a primordia at a random location? Does not the pattern also recover (as it does in ablation experiments)? How does this compare?

Also the authors argue that noise in divergence angle order does not propagate far, but that it has a long effect on the timing, but they don't really give any proof this. We would need to see the time, divergence angle pairs produced by the model, and the model would have to have a similar discretization in time as in space (in most simulation models space it much more coarsely discretized than time). Finally, I might be convinced if they could show evidence of this in planta. It seems to me that after ablation experiments the timing recovers just as fast as the divergence angle.

Stochastic model section: Again they are assuming there is no separate control of the plastochron. I wonder if their stochastic model leads to a different outcome than just adding noise to the system? An example would be the Smith et al. (2006, CJB) model, where noise is added to the peripheral circle sampling point positions, which would also have the effect of adding noise to the inhibition threshold. Don't get me wrong, I appreciate a proper stochastic model, but the worth of such models becomes apparent when they demonstrate different behavior than a simple deterministic model + noise. Is this really the case here?

Speaking of the Smith et al. model, another major source of noise in this system is the fact that the resolution of the possible locations for primordia to initiate is very low. Fate change is a cellular phenomena, and there are really not very many cells around the peripheral zone, maybe 30-40 cells. This gives a resolution of around 10 degrees, a considerable source of noise. Given this it would seem that a perturbation of the possible initiation locations would be very relevant.

Materials and methods: The common phyllotaxis angles are irrational, and have the property that new primordia will be placed far from existing ones. It is therefore not surprising that if you include higher permutations, you start to obtain a roughly uniform sampling of the entire meristem. Consideration of 5 permutations gives 6 matching points, 52.5, 105, 137.5, 190, 275, 327.5 so random angles will always be close to one of these locations, which could explain the data in Figure 7. I would need to see statistics on this to demonstrate that these angle matches are really closer than random.

Reviewer #2:

Phyllotaxis has fascinated philosophers and scientists for centuries being one of few known examples of biological patterns characterized by such regularity, and hundreds of papers were published focused on biological and mathematical interpretations of this unique trait. The submitted manuscript, however, shows that "the other side" of real phyllotactic patterns, namely their perturbations, can also be informative in terms of shoot development regulation. The authors present two models of phyllotactic pattern generation: in the first model the "classical" assumptions often used in phyllotactic pattern models are employed; in the second one stochastic factors are added. Patterns generated with the aid of two models are compared with one another as well as with the empirical data, mainly on Arabidopsis inflorescence phyllotaxis (wild type and mutants). I would like to point several advantages of the presented stochastic model: it accounts for expansion (growth) of the apex surface; primordia simulated in the model are generated by groups of "cells" which all contribute to the pattern formation; the model reproduces real phyllotactic patterns as shown by comparison of pattern parameters, in particular the disorders in the patterns; the biological meaning of the variables used in the model is thoroughly and critically discussed, and those that can have the biological meaning assigned are recognized.

I would like to point to three topics that could be addressed by the authors:

1) In the Introduction and Abstract, the authors state that developmental disorders are generally not considered as informative. I would not point it so strongly, since in fact studies on mutant phenotypes are often studies on disturbed patterns that lead us to conclusions on pattern generation mechanisms. Also some old literature was devoted to teratology, i.e. disturbed development, in order to speculate on developmental mechanisms.

2) From my knowledge on empirical and theoretical papers on phyllotaxis one of the discrepancies between the two is in that in nature, so-called fused or double primordia (or leaves) can be sometimes observed, while they are most often not generated by models. Would it be possible to generate such primordia in the stochastic model (decreasing the epsilon value)? This could provide one more example of pattern perturbation in support of the model.

3) Most reference to empirical data are done with Arabidopsis, obviously a good choice since some mechanisms on the phyllotaxis regulation are recognized based on the mutation. Nevertheless, the relative size of primordia in Arabidopsis is large, and they are not densely packed around its SAM (low numbers of contact parastichies), while in other species primordia are relatively small and densely packed. I understand that the phyllotaxis parameters used for comparison with model generated phyllotaxis, are not available for these species, but these cases could be to larger extent referred to. For example, shoots with relatively small primordia and short plastochrons (conifer twigs, Asteraceae capitulum) would support the model conclusion on relationships between plastochron duration and frequency of permutations (Results); just have a look on the already dead Christmas tree thicker twigs or trunk, and you will most likely find some permutations in support of the model.

Reviewer #3:

My ability to fully interpret this paper is very limited since it is mainly mathematical and my background is biology. However, I understand the main message to be that the authors take an inhibitory field model for phyllotaxis and integrate stochasticity into it. The stochastic model recapitulates the normal patterns of organogenesis as well as observed deviations. It also enables the authors to infer information about the sources of noise.

I think that the ability to help pin-point the root cause for why a pattern is disrupted is very useful and hence this paper is helpful to phyllotaxis researchers. However, I still have concern over the paper's general significance.

My other concern is how model-dependent the conclusions are in any case. Their model, based on abstracted inhibitory fields rather than self-organising auxin transport seems to me to lack a fundamental feature of the latter. For instance, auxin application to un-patterned meristems reveals that organ spacing is robust to random initial distributions of applied auxin (Reinhardt et al., 2003). From what I understand of the model in this paper (and I may be wrong) this fundamental property is not a feature. The ability of the system to form patterns dynamically from random starting points is however captured by less abstracted models based on polarity feed-back from auxin concentrations (Jonsson et al., 2006).

If the model used does not have this property I am worried that the conclusions are not relevant to the real plant.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A Stochastic Multicellular Model Identifies Biological Watermarks from Disorders in Self-organized Patterns" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers and editors agree that you should change the manuscript title to reflect its more narrow proof of concept nature, for example "[…] from Disorders in the self-organizing pattern of phyllotaxis".

Please fix some of the wording, in particular the use of inhibition vs energy (see comments below), to avoid misunderstandings in the context of the wider literature.

Please address the issue of the dynamic definition of inhibitory fields. This appears to be an important limitation of your current model, and although we do not ask you to resolve it at this point, we would like to ask you to explicitly spell out this limitation If it is not captured in the model. That is, specification (or growth of the organ) and the generation of inhibition could occur simultaneously and dynamically rather than in a consecutive, step-wise fashion as is modelled here. Maybe you could also comment on how would this influence the way the system responds to noise?

Find more details in the reviewer comments below, but you only need to respond to the points raised above.

Reviewer #1:

I am mostly satisfied with the changes the authors have made to address the comments from the initial review. It is too bad that they were not able to apply their method to another patterning system, but the authors argue that it would be a complete work in itself, although I am not so sure. I think the application of the method to at least one other system would speak to the potential generality of their ideas, and without it the paper seems in a bit of a niche area (i.e. plant phyllotaxis specific).

Reviewer #2:

Judging from the answers to Editor's and Reviewers' comments provided by the authors and, most of all, from the changes introduced in the manuscript, it has been significantly improved and most of the suggested changes have been introduced: more modelling was performed widening the examined cases, and model interpretation has been improved, also the changes have been made in the main text as suggested. Nevertheless, the manuscript in the present form is for me more clear and representing a broader approach to the problem.

Reviewer #3:

The authors have now attempted to address my main point which was to test whether the model could create a whorled pattern from a random starting point. While I'm happy the authors have done this simulation I still have a remaining concern on this point. This is that in their description of this process they relate that the first primordium is specified stochastically.

The current models for phyllotaxis based on polarized auxin transport are able to self-organize auxin peaks (and hence primordia) simultaneously. Auxin is dynamically distributed over time to create spacing similar to a Turing mechanism. Again, the spacing process for all auxin peaks occurs spontaneously and dynamically. From the supplied description I am still not convinced this model captures this dynamic. In other words, in current models based on auxin transport (e.g. Johnson et al. (2006), an inhibitory field isn't specified only after a primordium is specified (as seems to be the case here), it is being generated dynamically during the process of specification i.e. auxin build-up. Hence the whole process can adjust to changing conditions as they occur – it is dynamic. In contrast, in the whorl simulations here, it seems an initial position is specified by noise and then others are specified in quick succession at a spacing that allows several to form around the apex in the same plastochron but not really in a spontaneous manner.

I guess it really comes down to the question: Can the authors map their model (with or without the stochasticity) on to the class of models represented by the current polarized transport models? For instance, as done by Newell, Shipman and Sun (2008) Journal Theoretical Biology 251, 421-439.

Overall I do think it is critical to show that the model they have chosen to use captures the same fundamental properties as exhibited by models that are more closely based on current experimental work.
