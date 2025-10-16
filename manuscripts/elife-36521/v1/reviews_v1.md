# Peer review - Round 1

Editors:
- Ruth Emily Ley, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36521.026](https://doi.org/10.7554/eLife.36521.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Experimental evaluation of the importance of colonization history in early-life gut microbiota assembly" for consideration by eLife. Your article has been reviewed by Wendy Garrett as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper by Martinez et al. aims to study an important and fundamental question of community establishment, and specifically, how order of exposure/colonization effects the final composition of communities. It is tested here in the gut of mice, WT or Rag1-/-, to start and understand the adaptive immune system's role in community establishment. Together, these studies suggest that the timing of colonization can play a significant role in determining emergent community composition. The reviewers agree that this work is of great interest to the larger microbiome community, with strong implications on the establishment of the human microbial communities as well. The data are extremely interesting, but some additional analyses can lift the manuscript even higher.

Essential revisions:

The sample collection is not 100% clear. Multiple figures refer to "Parents A" and "Parents B", and it's unclear where these samples came from. If it is indeed from the fur of the parents, then we should have had "Parents AB" as well, so it's unclear.

Subsection “Establishing a mouse model using distinct, complex microbial communities to study the importance of colonization history”: The authors state a desire "to avoid microbiomes from animal care facilities", but then select an individual (donor A) from a colony maintained for three generations in such a facility (and, presumably, indoors, consuming standardized chow, etc). Why? Also, in subsection “Donor mice”, it sounds like one mouse gave rise to three generations. Perhaps edit (unless this was a cloning lab). The donor A mouse is described as "wild" but was born and lived in a lab.

The experiment design looks good, but there are key analyses that I would expect to see in the paper. Some appear later but should be presented much earlier. Please include a better analysis of bacterial species found in donor vs. recipients. Analysis of the transmitted bacterial species, not in terms of overall statistics (like Shannon diversity), or PCoA plots, but big heat map(s) that show(s) which strains were transferred and which were not. And/or rank abundance curves with relevant taxa highlighted. The PCoA plots often show different axes (not always named axis 1 and 2), and it feels like there are more interesting results in the full data.

Figure 1B: It seems like data from Parents A/B are missing from both WT and Rag1-/- experiments. I wonder if these parents had higher alpha-diversity, too (like the pups), because they were exposed to a mixture. Please add if available. (To be clear, I mean the parents of the AB/AB treatment mice, given that the parents of the A/B and B/A treatment mice are shown.)

Figure 1C: How come there is variation in samples A,B in panel C but not in B? How many samples are in each group?

Figure 2 needs a lot of polishing. Axes are not consistent, sizes are not consistent. Clearly, it is not ready for publishing. PCoA axis should have% variance explained added to them.

Subsection “Assessing the importance of colonization history and dispersal limitation towards shaping gut microbiota structure” and Figure 2A: It appears that all of the recipient animals cluster closer to donor A than they do to donor B. Is this consistent with the statement that "B/A mice clustered closer to Donor B"? Is there a significant difference in the clustering of A/B vs. B/A mice with Donor A vs. Donor B? In Figure 2A, parent colors are not distinguishable from A/B, B/A; the x-axis label is missing; Parents A/B are missing.

Figure 2C: I am puzzled by the differences across the various colonization orders. It seems that for A/B and B/A within cage and across cages are not that different, whereas for AB/AB there is a strong difference there. How can this be explained? I am also surprised that there is a significant difference in AB/AB comparing across cages to across isolators (*** P < 0.001). The figure doesn't seem to show that strong difference.

Subsection “Assessing the importance of colonization history and dispersal limitation towards shaping gut microbiota structure”: The Adonis analysis and the distances shown in Figure 2C do not seem to agree. From Figure 2C, it appears the isolator would have the strongest effect, and not the cage. Can you provide more details on your Adonis analysis?

Subsection “Assessing the importance of colonization history and dispersal limitation towards shaping gut microbiota structure”: Nice result. To support that local extinction (within isolators) was by drift and not by selection, could you examine the relative abundance of those types (that disappeared) in the donor communities (i.e., the metacommunity)? Assuming low abundance types are more likely to drift to local extinction.

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects”: Before digging deeper into the order, there are clear species that are absent in one donor, and present in the recipients, and it would be very interesting to understand what these are.

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects”: In the linear mixed model analysis, were cage/isolators variable taken into account? The authors made it clear in the previous section that these are relevant variables, yet they are not mentioned here more.

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects”: I would name these (inhibitory/facilitative effects) the opposite. If a strain is overrepresented when inoculated first, that would not be inhibitory. I find these confusing, maybe you should consider explaining it in more detail?

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects”: Please indicate the total number of cases; the three cherry picked examples all have quite low abundances – less than 1%, less than 0.1% –which raises a concern about detection limits and whether these are just sampling depth effects. Were any highly abundant types affected?

The figures are not sharp enough. Some figures do not convey the message clearly and concisely (like the experimental design figures). E.g. Figure 3A – what are the values shown – abundance or log values? A label is missing. The entire figure needs much polishing as well. All the sizes are different, and it is not well positioned of all panels. PCoA plots should not show clustering of samples (for example, with a circle surrounding each group of samples), as this visualization is misleading to show more separation than what the data support. Overall, figures are missing legend headers, axis names, units explanation, etc.

Subsection “Establishing a mouse model using distinct, complex microbial communities to study the importance of colonization history” and in particular "[…] colonization order is the only experimental variable in the model.": Is host age (and associated factors like weaning status and parental proximity) not also a variable? There is no control in which day 10 A or B is followed by day 36 sham; or day 10 sham is followed by day 36 A or B. Isn't it possible that A and B differ in the degree to which their species can persist at a particular developmental age without the competing community? (Overall, pieces of this paragraph might fit better in the Introduction or Discussion section, rather than Results section.) Likewise, in subsection “Timing of arrival impacts persistence of individual colonizers” (second paragraph), by "timing", do the authors mean host age, or relative to the timing of C3H introduction, or both? Again, controls in which nothing was introduced on day 10 might shed light on this.

Subsection “The adaptive immune system does not contribute to historical contingency in gut microbiota assembly”: Nice result. Why not show the data?

Please standardize the terminology:

– Subsection “Establishing a mouse model using distinct, complex microbial communities to study the importance of colonization history”: "OTUs" are often called "types", sometimes called "nodes" or "OTUs", and said to be potentially differentiated by "only one nucleotide". Please clarify what the entities are, and when they differ from one analysis to another (if they do). Please establish terms clearly and use consistently.

– Figure 1A "day 78", subsection “Gut microbiota of recipient mice shows higher diversity when compared to donors” "week 12" and later "day 72": If these all mean the same thing, then please standardize.

Subsection “Timing of arrival impacts persistence of individual colonizers”: The authors mentioned before that gavaging earlier than 10 days may be harmful, and yet here they are gavaging at age 5 days?

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects” and subsection “Timing of arrival impacts persistence of individual colonizers”: Instead of not showing the data, add a supplementary figure.

Supplementary file 1: What do the "a", "b", "ab" symbols mean?

Subsection “Assessing the importance of colonization history and dispersal limitation towards shaping gut microbiota structure”, regarding "niche-related differences should be marginal in our study": This is confusing, because it would seem that unweaned and weaned mouse gut environments, for example, must be quite different in terms of niches. There's no control for developmental age, and we don't know how A or B act individually based on timing, it seems? (This repeats an above comment.) What might we expect to see had the experiments been performed in adult germ-free animals?

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects”: The statement that "bacterial functions among gut microbiota members are not necessarily related to phylogeny" is quite bold based on the evidence provided. The authors should consider defining "functions" more clearly or providing evidence that horizontal gene transfer (rather than phylogeny) does explain bacterial functions if they believe this to be true.

Subsection “Bacterial types affected by colonization order and mechanisms of priority effects” and Figure 3C: These results are fascinating, please discuss more. It seems like in some cases (left panels) it's really a mutual exclusive abundance of the two types, whereas in the right panels, it seems like these could co-exist, like in the AB/AB samples.

Subsection “Timing of arrival impacts persistence of individual colonizers”: The logical path/flow from experiment 1 (donor A, B) to experiment 2 (4-strain, C3H) is unclear. There's a lack of integration between the two; like two separate studies with similar themes placed side by side. What findings from the first prompted the second? What rationale?

Subsection “Timing of arrival impacts persistence of individual colonizers”: This is a really interesting result. Does it have anything to do with the microbial composition of the pooled cecal samples used for the day 10 gavage. Do you have any data on these pooled communities? Do they have any of these species tested here?

Subsection “Timing of arrival impacts persistence of individual colonizers”: It seems that there are several non-exclusive alternate explanations that are also consistent with the observations, given the very small number of species tested. For example, one could imagine that the timing of species introduction relative to innate immune system development could be a contributing factor, or that non-identical species also contribute to competitive exclusion.

Subsection “The adaptive immune system does not contribute to historical contingency in gut microbiota assembly”: The word "adapt" is used loosely here. Adaptation through monopolization – what does that mean? The host (immune system) can respond and adapt during postnatal development.

Discussion section: It is striking that 19/20 species that are effected by colonization order in WT mice show the same behavior in Rag1-/- mice, suggesting that this activity is coded into their genomes – does this make it a deterministic process? Can the authors provide any insight into the features in the genomes of these ~20 species that likely contribute to this result?

Although the discussion is already quite long, perhaps some sections could be condensed in order to clarify the limitations of the sample sizes used (2 communities, 4 species) in deriving general principles. This would be helpful for a general audience.

The paper seems to be inconsistent in whether the effects observed are large or small. E.g., "Given the importance of historical contingency for gut microbiota assembly, clinical and medical interventions early in life (e.g., antibiotics, C-sections, formula feeding) are likely to have longer lasting consequences." vs. "Although the relative importance of assembly history appears small in our experiments (and less than that of dispersal limitation)[…]" For general readers, it would be helpful to be more quantitative about the magnitude of these changes.

Other examples from subsection “The adaptive immune system does not contribute to historical contingency in gut microbiota assembly”:

– Quote "significantly lower": Looking at the plot, the effect seems quite subtle.

– Larger effect sizes/more bacterial types in what compared to what? This is confusing.

– In the last paragraph, "both were increased" in Rag1-/-: I’m not sure given the data, and I’m not sure you agree, given your Abstract.

Many typos include:

"stains": strains

"locus": loci

"-wide wide": -wide

"importance": importance of

"ceca": cecum

"this a finding": this finding

"time a": time of a

"bacterial types bacterial types": bacterial types

"types to significantly differ": types that significantly differed

"inoculums": inocula

"impact colonization": impact of colonization

"assignation": assignment

"B-specific of the donor": B-specific types of the donor
