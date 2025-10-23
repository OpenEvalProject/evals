# Peer review - Round 1

Editors:
- Bernhard Schmid, University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73819.sa1](https://doi.org/10.7554/eLife.73819.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this paper, the authors use a trait-based model of plant growth and water flow in drylands to show that under increasing water shortage, spatial self-organization can help plant communities to maintain biodiversity and thus ecosystem functioning. Spatially heterogeneous ecosystem management may support these processes.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Linking spatial self-organization to community assembly and biodiversity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Gianalberto Losapio (Reviewer #2); Mara Baudena (Reviewer #3).

While we cannot go forward with the current version of the manuscript, since revision would almost certainly take substantially longer than allowed per eLife policy, we remain very interested in the work. We would therefore welcome a substantially revised version, which we would treat as a new submission, but aim to recruit the same editors and reviewers.

Reviewer #1:

Bera et al. study the response of vegetation in water-limited ecosystems to changes in the precipitation regime. Previous studies have shown that spatial processes, in particular the redistribution of (soil and surface) water, may play an important role in mediating the ecosystem response. An important consequence of this redistribution is the spatial self-organization of vegetation into regular spatial patterns, consisting of vegetation patches that act as sinks for (surface) water, and surrounding areas of bare soil that act as water sources. At the ecosystem level, the additional water input in vegetation patches may enable vegetation to persist at precipitation levels that are too low to sustain a spatially uniform cover.

While most model studies of spatial self-organization and pattern formation describe vegetation dynamics through 1-2 biomass variables, the current study extends this previous work by considering a trait diversity gradient, considering a large number (N=128) of discrete trait classes that range from stress-tolerant to fast-growing characteristics. The results show that in the absence of spatial pattern formation, a decrease in precipitation leads to a shift in the biomass distribution toward the more stress-tolerant trait classes. At the onset of pattern formation, however, soil water availability increases at the locations where vegetation patches form, enabling the more fast-growing trait classes to increase in biomass, and this shift is accompanied by an increase in functional diversity of trait classes as well. It is also shown that once these patterned ecosystem states are formed, the main adaptation to further decreases in precipitation occurs either through shrinking the size of existing patches, or by reducing the number of patches; in contrast, biomass and community composition of the patches remains relatively stable. Finally, it is shown that for certain precipitation conditions, functional diversity is maximized when the ecosystem is in a hybrid state, where part of the landscape has a spatially uniform vegetation cover, and part of the landscape is in a patterned state.

A potential strength of this paper is that the community assembly and biodiversity perspective on spatial self-organization may highlight the relevance of pattern formation in ecosystems more clearly to a broad audience. The formulation of a trait/strategy gradient of discrete classes is certainly an interesting suggestion to connect the typical single/few biomass variable(s) approach to a community-level approach. The community assembly process is modelled in a very specific way, and the manuscript would benefit from an expanded ecological motivation of the processes that are being mimicked, and thereby explain more clearly what taxonomic level of organization is being considered. In addition, it would be useful if the authors could provide further clarification as to what extent the community diversity dynamics can be separated from total biomass dynamics of patterned water-limited ecosystems given the current approach. These points are explained in further detail below.

• First, it was not entirely clear to this reviewer how the reaction parts of the model equations determine the optimal trait value χ, and how this value varies as a function of precipitation. Assuming a single trait class, and plotting the relevant equilibrium values of the three state variables shed some light on this issue. [Unfortunately, there does not seem to be a possibility to attach the figure with these plots to this review report]. Assuming the non-spatial equilibrium solution was derived correctly , the optimum biomass (B) value shifts across the trait spectrum with changing precipitation (in the non-spatial model version, solving the surface water equation for equilibrium will always yield that all precipitation infiltrates, i.e. regardless of the values of surface water, H, and χ). The equilibrium of soil water availability (W), which is the growth limiting resource of the vegetation, shows an inverse pattern with biomass. This result is in line with a classical results (e.g. Tilman 1982), in that the most successful strategy is the one that is able to reduce the limiting resource to the lowest equilibrium value. With all trait classes competing for the soil water resource, however, it is then not immediately clear why the most successful trait class is not outcompeting the other classes. This leads to a second point, about the way in which community trait adaptation is modelled.

• The authors model trait adaptation through a diffusion approximation between trait classes. That is, every timestep, a small amount of biomass flows from the class with higher biomass to the neighboring trait class with lower biomass. From an ecological point of view, it seems that this process is describing adaptation of vegetation that is already present, so this process seems to be limited to intraspecific phenotypic plasticity. From the text, however, it seems that the trait classes correspond to higher taxonomic levels of organization, when describing shifts from fast growing to stress-tolerant species, for example. It is not entirely clear, however, how biomass flows as assumed in the model could occur at these higher levels of organization.

• Combining the observations from the previous two points, there is a concern that for a given level of precipitation, there is a single trait class with optimal biomass/lowest soil water level that is dominant, with the neighboring trait classes being sustained by the diffusion of biomass from the optimal class to neighboring inferior classes. This would seem a bit problematic, as it would mean that most classes are not a true fit for the environment, and only persist due to the continuous inflow of biomass. Taking a clue from the previous papers of the authors, it seems this may not be the case, though. Specifically, in the paper by Nathan et al. (2016) it seems that all trait classes are started at low initial biomass density, and the resulting steady state (in the absence of biomass flows between classes) seems to show similar biomass profiles as shown in Figures 4,5 and 7 of the current paper. While the current model formulation seems slightly different, similar results may apply here. Indeed, keeping all trait classes at non-zero (but low) density, and when the (abiotic and biotic) environment permits, let each class increase in biomass seems like the most straightforward approach to model community assembly dynamics. Given the above discussion about these trait classes competing for a single resource (soil water), and one trait class being able to drive this resource availability to the lowest level, it would then be useful to readers to explain why multiple trait classes can coexist here, and how (for spatial uniform solutions) the equilibrium soil water level with multiple trait classes present compares to the equilibrium soil water level when only the optimal trait class is present. Furthermore, if results as presented in Nathan et al. (2016) indeed hold in the current case, perhaps it means that the biomass profile responses as shown in e.g. Figure 5 would also occur if there was no biomass flow between trait classes included, but that the time needed to adjust the profile would take much longer as compared to when the drift term/second trait derivative is included. In summary, further clarification of what the biomass flows between classes represent, and the role it plays in driving the presented results would be useful for readers.

• In addition, it would be useful for readers to understand to what extent the shifts in average trait values and functional diversity can be decoupled from the biomass and soil water responses to changes in precipitation that would occur in a model with only a single biomass variable. For example, early studies on self-organization in semi-arid ecosystems already showed that the shift toward a patterned state involved the formation of patches with higher biomass, and higher soil water availability, as compared to the preceding spatially uniform state, and that the biomass in these patches remains relatively stable under decreasing rainfall, while their geometry changes (e.g. Rietkerk et al. 2002). It has also been observed that for a given environmental condition, biomass in vegetation patches tends to increase with pattern wavelength (e.g. Bastiaansen and Doelman 2018; Bastiaansen et al. 2018). Given the model formulation, one wonders whether higher biomass in the single variable model is not automatically corresponding to higher abundance of faster growing species and a higher functional diversity (as the diffusion of biomass can cover a broader range when starting from higher mass in the optimal trait class). There are some indications in the current work that the linkage is more complicated, for example, the biomass peak in Figure 7c is lower, but also broader as compared to the distribution of Figure 7b, but it is currently not entirely clear how this result can be explained (for example, it might be the case that in the spatially patterned states, the biomass profiles also vary in space).

• The possibility of hybrid states, where part of the landscape is in a spatially uniform state, while the other part of the landscape is in a patterned state, is quite interesting. To better understand how such states could be leveraged in management strategies, it would be useful if a bit more information could be provided on how these hybrid states emerge, and whether one can anticipate whether a perturbation will grow until a fully patterned state, or whether the expansion will halt at some point, yielding the hybrid state. It seems that being able to distinguish these case would be necessary in the design of planning and management strategies. Also, in Figure 3a, the region of parameter space in which hybrid states occur is not very large; it is not entirely clear whether the full range of hybrid states is left out here for visual considerations, or whether these states only occur within this narrow range in the vicinity of the Turing instability point.

References:

Bastiaansen R, Doelman A. 2018. The dynamics of disappearing pulses in a singularly perturbed reaction-diffusion system with parameters that vary in time and space. Physica D 388: 45-72.

Bastiaansen R, Jaïbi O, Deblauwe V, Eppinga MB, Siteur K, Siero E, Mermoz S, Bouvet A, Doelman A, Rietkerk M. 2018. Multistability of model and real dryland ecosystems through spatial self-organization. Proceedings of the National Academy of Sciences USA 115:11256-11261.

Nathan J, Osem Y, Shachak M, Meron E. 2016. Linking functional diversity to resource availability and disturbance: a mechanistic approach for water limited plant communities. Journal of Ecology 104: 419-429.

Rietkerk M, Boerlijst MC, van Langevelde F, HilleRisLambers R, van de Koppel J, Kumar L, Prins HHT, De Roos AM. 2002. Self-organization of vegetation in arid ecosystems. American Naturalist 160: 524-530.

Tilman D. 1982. Resource competition and community structure. Princeton University Press, Princeton, NJ, USA.

Comments for the authors:

• Line 17: the term "re-patterning" may read as a non-patterned state becoming patterned again, whereas here it seems to refer to a spatial rearrangement of an existing patterned state.

• Line 39: resources (i.e. plural)?

• Lines 80-99: This is an introduction to the model description, rather than a result, as the header suggests.

• Lines 100-164: This is the model description, which seems to be part of the material and methods rather than a result.

• Line 179: when χ increase from 0.95 to 1.00 however, it seems that the Turing threshold start to increase, how can this reversal be explained?

• Lines 302-310: this explanation is clear, but it is an example that can also be explained by the biomass dynamics of a single variable model.

• Line 329: this is case where it would be useful for readers to understand how one can anticipate the formation of either hybrid or fully patterned states, and how this relates to the particular perturbation(s) imposed.

• Figures: Why are the biomass values in Figure 4,5 and 7 about an order of magnitude higher than in Figure 3?

Reviewer #2:

Conspicuous, repetitive patterns such as spots and stripes can be observed in every biome throughout the world. This work provides a new theoretical model for understanding self-organization of vegetation patterns in arid ecosystems and their response to climate (precipitation) change. Processes of spatial self-organization underlying the development of vegetation patterns have been studied for decades, with roots in the work of the great scientist Alan Turing. Ecologists use the Turing reaction-diffusion theory that builds on positive feedback relations between two variables, namely vegetation growth and water transport. Yet, it has been difficult to include multiple, different species as in real-world vegetations.

This paper addresses such shortcoming and extends previous vegetation pattern formation models by including different plant types. It provides a general framework that builds on the resource allocation tradeoff between growth versus stress-tolerance. Authors show when and how vegetation is robust to changes in precipitation via spatial self-organization and selection (differential plant mortality) along the growth-tolerance tradeoff. With increasing aridity, the ecosystem shifts from spatial uniform vegetation to patterned one, such as stripes, and, with further drought, to bare ground. Notably, self-organizing processes mitigate the impact of drought on ecosystem functioning and services by allowing fast-growing, productive species to persist in drier climate. This framework and associated results have important implications for the conservation and management of arid ecosystems and rangelands.

The conclusions of this paper are mostly well supported by data, but some aspects of model presentation, parameter choices, and data interpretation need to be clarified and extended.

1) Model presentation. It would be better to explain the model in ecological terms first, clarifying parameter biological meaning and justifying their choice. In doing so, creating a specific 'Methods' section, which now is lacking, would be of help too. Authors should clarify whether and how the model follows the conservation of mass principle involving precipitation and evapotranspiration. Are root growth and seed dispersal included for this purpose? Why are they not referred to any further in the analysis and discussion? Why a specific term for plant transpiration is not included, or is to somehow phenomenologically incorporated into the growth-tolerance tradeoff? In doing so, authors should also pay attention to water balance as above (H) and below (W) ground water are not independent from each other.

Another unclear point is that growth rates for the same plant functional groups are assumed to be constant among different species within the same group and are confounded by biomass production. Why is that the case? Furthermore, how many different species are characterizing each functional group? How are interspecific interactions accounted for (more specifically, see comment below)?

Finally, stress tolerance is purely phenomenological. There is no actual mechanism/parameter describing it. Rather, it "simply" appears as low/high mortality, which in turn is said to be due to high/low tolerance. This leads to a sort of circularity between mortality and tolerance. Yet, mortality can occur due to other biophysical factors (e.g. disturbance, fire, herbivory, pathogens). A drawback of this assumption is that a mechanism of drought tolerance is often to invest in belowground organs, including roots. However, according to the proposed model, it turns out that fast growing species with low investment in tolerance also have high investment in roots; vice versa, tolerant species have low investment in roots. This is a bit counterintuitive and not well biologically supported.

2) Parameter choice.

N = 128 is an extremely high number for plant functional groups. It is even quite unrealistic to have 128 species per square meter, so this value is not very reasonable. Please run the model and report results with more realistic N (e.g. from 4-64) as well as with different sets of N values keeping all other parameters constant.

Gamma (rate of water uptake by plants' roots): why is it in that unit of m2/kg * y? Why are you now considering the area (and not the volume) per biomass unit?

A is not defined in the text.

M min: why 0.5 mortality? Having M max set to 0.9, please consider a lower mortality value set to 0.1, and please report evidence (hopefully) demonstrating the robustness of results to such change.

Kmin and Kmax are in two different units, and should both be kg/m2.

Values of precipitation (P, mean annual precipitation) are not reported.

3) Results presentation and interpretation.

Parameter range of precipitation in figure 3 is odd. Why in one case precipitation ranges from 0 to 160 while in another it is only 60-120? Furthermore, in paragraph 198-213 and associated results in Figure 5. the Choice of precipitation values is somehow discordant from the previous model. Please provide motivation for this choice, clarify and uniformize it.

Throughout the text, authors claim to address plant-plant interactions, particularly intra and interspecific competition. However, it is not clear how competition was modelled neither whether it was included in the model. In its current state, it is just an assumption pulled out when discussing results – a classic 'passepartout' used by ecologists. Furthermore, why only competition is invoked in interpreting results when facilitation is known to be much more relevant in pattern formation and biodiversity maintenance in arid systems?

Finally, authors seem to create confusion around community composition, which is defined as the (taxonomic) identity of all different species inhabiting a community. Notably, it is remarkably different from the xmax parameter used in the model, which as a matter of facts is just the value of the most productive (notably, not necessarily the most abundant) functional group.

Reviewer #3:

In this paper, the authors use a mathematical model of plant and water dynamics in drylands to show that drylands adaptive capacity to respond to changes, via spatial self-organization in space has also beneficial effects in preserving its biodiversity and ecosystem functions.

The model is an extension of a large body of previous, well-established works on plant self-organisation in drylands. The model is well described and motivated (with one main exception, see below), the analyses are robust and the results are very convincingly supporting the conclusions. I however have an issue with one of the assumptions in the model equations. The authors included a term for "mutations" in traits that (1) is not introduced or motivated (2) its effects/importance are not highlighted by specific analyses (3) the possible implications or limitations connected to it are not discussed. To my knowledge, this term is also not based on earlier work. All these elements need to be included, as at the moment is for example unclear what the authors intended to represent by including the mutation term (evolutionary time scales? Or adaptation?). Also, it would be especially good to include an analysis of how influential this term is for the final results.

Assuming the authors can address this one concern, the results are surely important as they connect for the first time plant spatial self-organization to its biodiversity preservation, in the face of future expected climatic changes and probable land degradation. These findings, although theoretical, have the potential to be useful also for guiding adaptive and dynamic land management, as they underline the importance of taking into account spatial vegetation distribution in drylands management.

Besides the major point about the mutation term, I list here two other important points:

– The authors state that they represent highly tolerant plants by representing the plants with a small mortality. However, in their model, plant mortality does not depend on soil water levels. How can the authors reconcile these two aspects? Also, one could argue that mortality is related to the average life span, not specifically to tolerance to highly stressful condition. The authors should better justify this point and discuss the implication of this assumption.

– In the model, there is shading feedback too, not only infiltration feedback. However the authors state there's only infiltration feedback in l. 84, could they please explain?
