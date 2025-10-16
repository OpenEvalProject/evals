# Peer review - Round 1

Editors:
- Bernhard Schmid, University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38012.021](https://doi.org/10.7554/eLife.38012.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Wild suburbia: mammal communities are larger and more diverse in moderately developed areas" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Bernhard Schmid as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ian Baldwin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Marc Kéry (Reviewer #3) and Ingolf Kühn (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The value of this paper is that it addresses a question of broad relevance with novel methods. The question is whether human population density near two US cities reduces the occurrence of large mammals in four types of habitats, large forests, forest fragments, open areas and yards. The assessment method involved 557 citizens operating cameras deployed for around 20 days at each of 1427 locations throughout a period of 4 years. In addition, the authors compared the results of this assessment with a global data set.

The result was that mammal occurrence did not decline with human population density and even showed an opposite tendency, except for bobcats. Even though this results is not "strong" in the sense that the main point is the absence of a negative influence of human population density, it does send a very important message, in particular because it is based on such a large sampling scheme with a clear design of five human population density levels (wild < rural < exurban < suburban < urban) factorially crossed with the four habitat types (obviously, these two factors were not fully orthogonal because for example open areas and yards could not be found in the wild).

Essential revisions:

The interpretation of human population density as equivalent to disturbance is less important than implied by the authors and should be better justified. In particular, the comparison with the so-called intermediate disturbance hypothesis at the start of the Results and Discussion section seems unnecessary and unjustified, because it is not really tested later on nor even discussed. In fact, the curves drawn in Figure 1 are not really hump-shaped and probably do not have significant downwards curvature at high human population density (interpreted as high disturbance). The hump is even more elusive if Figure 3 is inspected.

Currently, the discussion is somewhat US-centered. Although the two case-study cities are from that region, it would make the paper more relevant if comparisons with literature from other regions, including Europe, and involving other taxonomic groups would be included. In this context it would also be important to put the levels of human population densities in the two studied cities in relation to cities in the old world, which often occupy much smaller areas.

The major issue you need to address in the revision is the description of methods. The detailed comments from the reviewers in this regard are listed below:

I am not sure whether the results are influenced by a measurement bias, i.e. species tending to have higher activity in more disturbed regions and hence being more frequently recorded.

Subsection “Detection rate models”: Either refer from here to the last paragraph of the “Occupancy models” subsection or mention already here how large (long) the burn-in phase was and report the value of i.

Subsection “Occupancy models”: To me it is not clear which species were paired: all ones, or just predators?

Subsection “Occupancy models”: Explain the elements of the formula (including subscripts).

Subsection “Comparison with global occupancy data”: Be explicit on how this was assessed.

Currently, the information about the study design is placed in different parts of the manuscript so that it is difficult to get the overview. Supplementary file 1 is the most useful in this context, even though it would be easier if number of camera locations would also be shown (in addition to number of nights). It is not clear, if there was an additional spatial stratification that was not used in the analyses. For example, I could imagine that within each cell in Supplementary file 1 there were some spatial units and within these spatial units camera locations. Even if that was not the case, the question remains if spatial distance and arrangement of camera locations should have been considered.

Why did you use the crude models of rarefaction rather than obtain the inferences on species richness (including species accumulation) from the multi-species occupancy model of Rota et al.? See Dorazio et al. (2006) for how this can be done. Also, please cite the important work of Dorazio and Royle (2005) and Dorazio et al. (2006) as a foundation on which models such as that by Rota et al. are built.

- Subsection “Model covariates” the sentence “We represented whether a site allowed hunting or not using 0/1.” sounds strange, rewrite.

- Subsection “Model covariates”: Please explain what a restrictive prior is.

- Subsection “Occupancy models”: Really, the other basic groundstone on which your work is based are the multispecies occupancy models of Dorazio and Royle and of Gelfand (independently developed in 2005). These should also be cited.

- Subsection “Occupancy models”: “We assumed all species occurred independently…”. Does this fit with what was just said “It contains single-species (first order)…”?

Subsection “Data reporting”: The first part of this paragraph is a bit weird to me. If you have to have a formal paragraph like this for the journal specifications, please ignore. As of now it reads like you are trying to convince the reader why an observational study was chosen instead of a true experiment. I think it is given that a camera trap study is going to be more of an observational study – we just try to standardize our sampling design as much as possible. If this paragraph is not required, I would just go straight into your methods – i.e. study design, site selection, sample size, etc.

Subsection “Data reporting”: How did you randomize your sites? Did you use GIS and place random points within some bounds of a polygon (e.g. yard or forest preserve)? Did you place a grid across the city and chose sites closes to a random intersect? Please be more specific.

Subsection “Citizen science camera trap surveys”: Please report the mean number of cameras deployed per volunteer (as an aside, please be consistent with the use of volunteer and citizen scientist).

Subsection “Citizen science camera trap surveys”: 200 m seems close together for mammal occupancy. Please justify the independence between sites, or, consider changing your terminology from true occupancy and maybe use habitat use instead.

Subsection “Citizen science camera trap surveys”: Were cameras rotated continuously throughout the year or did sampling only occur during a particular season. Please clarify? If they were rotated throughout the year, did you revisit sites or are some sites sampled in the earlier part of the calendar year being compared to sites sample later (let’s say early spring vs. late fall). If this is the case I would be worried that the sampling periods would violate the assumption of closure for your occupancy models. Please clarify and or address the issue.

Throughout the statistical analyses: It is clear that multiple authors wrote the different sections. Please take the time to be consistent in your tone, terminology, and methods descriptions throughout. For, example R is cited 3 different ways.

Subsection “Model covariates”: Please justify why you decided to use a single season occupancy model for multiple seasons with a year covariate instead of a dynamic occupancy model. The way you did it is not wrong but does not consider the dynamics between years. If you are violating closer (see comment above), you could sub-divide your data into appropriate seasons (considering closure) and use a multi-season occupancy model instead.

Subsection “Model covariates”: Please specify if you used NLCD land use data set and used an open space category or used the NLCD canopy cover dataset.

Subsection “Model covariates”: I am a bit confused here. So, you used the percentage of forested area within the 5 km buffer that was at least connected to a large continuous forest patch larger than 1km? Could that linkage continue outside the patch? For example, would a small 5m2 patch on the edge of the buffer be counted if it were connected to a larger forest patch that continues outside the buffer? It’s just a bit confusing, please clarify.

Subsection “Model covariates”: Also confused here. So now you measured the percentage of forest cover within a 100m radius? But it didn't have to be connected to continuous forest cover? So, a small vacant lot with some trees would be counted?

Subsection “Model covariates”: I have concerns about using number of detections/trap night as a metric of prey abundance (even just relative abundance). In our system, we get rabbits just sitting in front of the camera all day. How can you tease apart that a single rabbit didn't sit in front of the camera continuously triggering it at one site, but not another. For example, what if in a single night one rabbit sat in front of a camera for 100 minutes (100 detections) at site A and 100 rabbits passed in front of the camera a single time (100 detections) at site B? Very different abundance, but you get the same answer.

Subsection “Model covariates”: Does NDVI get at understory? Will a cell with really dense canopy cover but no understory give a different value than one with really dense canopy cover and thick understory? From what I have experienced, dense canopy cover in an urban park (with no understory) will often show up the same as a forested area if there are few gaps in the tree.

Subsection “Model covariates”: Did you use monthly NDVI, did you pick a month with peak greenness, or did you average across the month? I am assuming you used one value since you did not use a dynamic occupancy model, but please clarify.

Subsection “Model covariates”: Indicate which camera model was the reference.

Subsection “Detection rate models”: Did you have adequate fit for both your Poisson and occupancy models? Figure 4—figure supplement 1 has huge error bars, which could be a result of over parameterizing the model. Maybe report results from PPC in supplemental table. However, PPC checks for occupancy models are tough as they have trouble accounting for the correcting of detection. Cross validation is probably best. See Hooten and Hobbs (2015).

Subsection “Occupancy models”: I think you need to mention that you ran an occupancy model for a subset of species (and mention species) somewhere here. Unless you ran a multi-species model for all the species, in which case I don't see any mention of the rest of the species in the Results section.

Subsection “Occupancy models”: I am assuming that the city indicator is a 1 or a 0 based on your table in supplemental material, but this is not clear in the text. Please clarify how that interaction is formulated. You also need to report which city is represented by 1 and which city is represented by 0. Without this your tables don't mean much. You also need to report the intercept value of your model in your supplemental tables, so the reader can interpret results for the reference city.

Subsection “Comparison with global occupancy data”: Here is where the global comparison is first mentioned. I think you need a justification and a bit of a background in the introduction. Until I got to the Discussion section and saw the results, I was left wondering what the point of this analysis was.

Subsection “Study sites”: This passage is written a bit unclearly. As is, it sounds like you deliberately avoided urban areas in both cities. I suggest rephrasing for clarity.

Subsection “Model covariates”: I am assuming 'hunting' means hunting was allowed or hunting was recorded during the sample period? Be more specific.

Subsection “Model covariates”: I suggest putting the covariate abbreviation that you use in your models and tables in parentheses after each time they are mentioned in the text. I think this will help the reader follow along.

Subsection “Model covariates”: I suggest rephrasing to "We included an indicator (0 or 1) to categorize whether a site allowed hunting or not." Also, I assume that 0 indicates no hunting? But please be explicit in the text.

Subsection “Detection rate models”: Change 'count' to Poisson.

Subsection “Detection rate models”: I think you should say what your thinning rate was instead of just ith.

Subsection “Occupancy models”: What about plot type and all the other covariates?
