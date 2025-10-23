# Peer review - Round 1

Editors:
- Christian Kost, University of Osnabrück Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65948.sa1](https://doi.org/10.7554/eLife.65948.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript is of broad interest to readers in the field of microbial ecology and systems biology, especially for researchers who study the assembly of multi-species communities. The authors examine how the presence of one or two different carbon sources affect the growth of microbial communities within the corresponding environment. The work combines mathematical modeling, experiments profiling the taxonomic composition of model communities grown on different carbon source(s), and measurements of the growth rate of isolates from these communities to arrive at the conclusion that in some contexts, one carbon source has a dominant effect on the composition of a community.

Decision letter after peer review:

Thank you for submitting your article "Nutrient dominance governs the assembly of microbial communities in mixed nutrient environments" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Meredith Schuman as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Silvio Waschina (Reviewer #1); Babak Momeni (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. Statistical analyses: There are several issues regarding the statistical analysis of the data.

a. One concern is about the statistical analysis of abundances across different cases (e.g. the results in Figure 2C). The authors have averaged the deviation in abundances (epsilon) across different cases. However, this is not a fair comparison. For example, a change from 1 to 11% in abundance is not comparable to a change from 70 to 80%. I recognize that alternative approaches have limitations as well (e.g. noise if the change in abundance is normalized to abundance). Nevertheless, the authors should avoid basing their conclusions (e.g. lines 187-191) on the mean of epsilon, because those conclusions will be biased by cases that have higher abundance.

b. The authors use one-sample t-tests to verify whether the growth observed in the two carbon source environments differs significantly from the expected growth. However, this test assumes that there is no variation in the predicted values. Since this assumption is clearly wrong, the authors should use a two-sample t-test (or any other equivalent) instead.

2. There are several cases of dominance (one genus/family taking over the community) when specific sugars are supplied. This observation raises the question whether these cases can skew the conclusions. For example, the null prediction will hold if there are extreme specialists that utilize preferentially one particular resource. However, what happens if only cases without dominance by one genus/family were included in the analysis? The authors should briefly discuss whether and how this situation would affect their results.

3. It would be helpful to have information about growth yield on the different carbon sources, in addition to growth rate. Thus, if possible (no additional experiment required), it would be good to include OD measurements or DNA concentrations from the extractions to provide information on the yield of communities on different amounts of a single carbon source.

4. In Figure S9, it looks like there is poor growth overall on benzoate and glycine. On glycine in particular, the fastest growth rates that are reported seem to be close to 0.01/h, or one doubling every 100 hours. In the community assembly experiments, communities are transferred every 48 h with a dilution rate of 125x. Given these slow growth rates, it remains unclear how these communities could have survived on these two carbon sources for 10 serial passages. Is it possible that the growth rates differ between the 384 well plate and the 96-well deep well plates? Or were the isolates sampled not representative of members of the complex community in general? Did the communities as a whole grow on glycine and benzoate? Please clarify this issue.

5. It remains generally unclear whether or not the experimental system is carbon limited across all of the different conditions and in all resource combinations tested. If growth on one carbon source requires a lot of oxygen consumption, and growth on the other carbon source requires less, then oxygen may be a hidden limiting resource. This type of dynamic could provide an additional reason why pairs of similar nutrients are better predicted than pairs of dissimilar nutrients: similar nutrients enter the central metabolism at similar points and are more likely to consume additional resources in a stoichiometrically similar manner. The authors should provide evidence that rules out this possibility.

6. Given that the consumer resource model is a valuable addition to the manuscript, it would be better to move it to the Results section. Moreover, a more in-depth discussion of the role specific resources play for metabolism and growth should be included. In particular, when presenting and discussing Figure 4, it would be helpful to briefly state how the species and families (in terms of their nutrient preference) were set up in the model. In this context, the authors also may want to consider mentioning some of the work by Hwa lab and Egli lab, as they may shed some light on the underlying mechanisms of the observed patterns in this manuscript.

Reviewer #1 (Recommendations for the authors):

line 52 (abstract): "sugars generally dominate organic acids." From the context it is not immediately clear what is meant by "dominate". The meaning becomes clear when reading the manuscript, but the meaning of "dominance" remains vague when reading the abstract only.

line 74 & line 81: Please briefly explain the term "enrichment community" as this might not be directly clear to all the potential readers.

Lines 107-110: The construction of the null expectation model is well-explained and justified. Yet, I was surprised by the sentence about the potential ecological and metabolic interactions between species (lines 107-110), which states that these are not affected by mixing nutrients. For instance, in the prominent example of overflow metabolism some bacterial species do not oxidize sugars completely but excrete notable amounts of organic acids (often acetate), which can serve as nutrient for acetate-oxidizing bacteria. In such a situation, the metabolic interaction would be strongly influenced by the combination of available nutrients; say two sugars enable acetate cross-feeding while a combination of two organic acids could potentially disable the interactions with significant impact on community assembly. The mentioned sentence (lines 107ff) gives the impression that nutrient combinations that interactively influence community assembly by altering metabolic interactions between species cannot be detected as deviation of the observed community structure to the expected structure based on the null (additive) model. In short, my suggestions would be to differentiate in the text between nutrient-independent metabolic interactions (i.e. those interactions taken place independently of the available nutrient(s)) and nutrient combination-dependent metabolic interactions (i.e. interactions that are affected in their expression/flux based on the identity of nutrient combinations).

lines 139-140: Although you specify this in the methods section, it would be nice if you could add to this sentence on which basis the 1:1 carbon source ratio was calculated to prevent confusion between molar, mass and C-molar ratio. Also, it would be great to briefly explain the motivation why carbon source concentrations were adjusted to equal C-molar concentrations (and not mass or molar) in the methods section and to state the final molar concentrations for each respective single CS media in Table S1.

lines 145-148: Are there, besides to the diversity in biochemistry, specific reasons for the choice of the ten carbon sources? Are these also relevant/potential nutrients for soil microorganisms?

line 150: This is the first occurrence of the abbreviation of ESV. Please state the full term here.

Reviewer #2 (Recommendations for the authors):

The authors in this manuscript examine the impact of the metabolites on the composition of microbial communities. Specifically, they search for a link between the composition of a community when supplemented with a combination of carbon sources with communities formed under each of those sources. To address this, they examine the assembly of communities in defined nutrient mixes through enrichment.

In my opinion, the setup and approach they have chosen makes perfect sense for addressing the question they have posed. Overall, I think this manuscript is a helpful step forward to explain some of the patterns that have been observed in microbiome studies.

1. I have a concern about the statistical analysis of abundances across different cases. This applies, for example, when interpreting the results in Figure 2C. The authors have averaged the deviation in abundances (epsilon) across different cases. However, I am not sure if this offers a fair comparison. For example a change from 1 to 11% in abundance is not comparable to a change from 70 to 80%. I recognize that alternative approaches have limitations as well (e.g. noise if the change in abundance is normalized to abundance). Nevertheless, I would discourage basing the conclusions (e.g. lines 187-191) on the mean of epsilon, because those conclusions will be biased by cases that have higher abundance.

Reviewer #3 (Recommendations for the authors):

1. It would be helpful to have information about growth yield on the different carbon sources, in addition to growth rate. Maybe you measured OD prior to collecting samples prior to DNA extraction? Or maybe you have the DNA concentrations from the extractions? Also, if there is any information on the yield of communities on different amounts of a single carbon source, that would be excellent to include. This is not to suggest more experiments!

2. In Figure S9, it looks like there is poor growth overall on benzoate and glycine. On glycine in particular, the fastest growth rates that you are reporting seems close to 0.01/h, or one doubling every 100 hours. In your community assembly experiments, you transfer every 48 h with a dilution rate of 125x. After 10 passages, I don't understand how a community made of strains growing at these slow rates could survive on these two carbon sources. Is it possible that the growth rates between the 384 well plate and the 96-well deep well plates differ? Or were the isolates sampled not representative of members of the complex community in general? Did the communities as a whole grow on glycine and benzoate?

3. I would like more evidence to support the assertion that the experimental system is carbon limited across all of the different conditions and in all resource combinations. If growth on one carbon source requires a lot of oxygen consumption, and growth on the other carbon source requires less, then oxygen may be a hidden limiting resource. This type of dynamic could provide an additional reason why pairs of similar nutrients are better predicted than pairs of dissimilar nutrients- similar nutrients enter central metabolism at similar points and are more likely to consume additional resources in a stoichiometrically similar manner.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Nutrient dominance governs the assembly of microbial communities in mixed nutrient environments" for consideration by eLife. The evaluation has been overseen by Christian Kost (Reviewing Editor) and Meredith Schuman (Senior Editor).

We think that the revised version of the manuscript has significantly improved in terms of clarity. Also, you have sufficiently addressed all comments raised by the reviewers. However, there are two points left we would like you to revise before we can finally accept the manuscript for publication in eLife:

1. In the current version, you included the analysis on the O2-requirement for utilising the different carbon sources in the Discussion section. Please report this result in the Results section.

2. The panels of the figures are inconsistently labelled (i.e. the way panels A,B,C are presented). Please arrange these panels consistently in all figures from left to right and top to bottom in case panels fill more than one row.
