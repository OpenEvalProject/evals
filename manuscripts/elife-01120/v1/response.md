# Author response - Round 1

Authors:
- Sean Michael Boyle
- Shane McInally
- Anandasankar Ray

## Response text

DOI: [10.7554/eLife.01120.015](https://doi.org/10.7554/eLife.01120.015)

1A) “…they can only predict more ligands based on receptors that have already been experimentally tested against a large number of ligands.”

We agree with the critique that we are only able to predict ligands for which a training odor set has been made available. We had included this information within the Results section, but have now incorporated this into our Abstract and Discussion sections.

1B) “…they predicted ligands for only 19 Ors; although technically it may constitute the “majority” of ORNs that utilize Ors, it is certainly not a “majority” of ∼50 ORN types in adult Drosophila (as a significant fraction of ORNs utilize Irs).”

We agree that the wording could come across as ambiguous, which is not our intention. We have modified the text to clarify the distinction and included a short discussion of potential for predictions from other classes of chemoreceptors in the Discussion section.

1C) “…the validated 71% came from only 9 Ors; it is unclear whether this can be generalized to the other untested Or classes.”

The rationale for selecting the 9 receptors for testing was accessibility to electrophysiology and unambiguous identification using a diagnostic odor panel. We have modified the text in the Abstract to accurately present the experimental data and clarify that 9 Ors were validated.

1D) “…there is no evidence that any of the agonists or antagonists identified in silico are better (higher affinity) or more likely to be the true biologically relevant ligands for these receptors than those identified in small chemical libraries based on ecologically reasoning (i.e., the training set).”

We agree with the critique. Our focus in this analysis was to create a method that could identify a large number of active compounds, which we were successful at. We expect this will be useful for hypothesis generation and potentially identifying stronger, or ecologically and behaviorally important odors. We anticipate that availability of large number of candidate ligands will also be useful in behavioral disruption programs for pest and disease vector species, since it will allow a researcher to judiciously select affordable, pleasant smelling and environmentally safe chemicals for applications.

2A) “In Table 1 what are the numbers given for each descriptor? If these are classes of descriptors then how many descriptors from the original set of over 3,000 are actually being used, and what are they? And how do they appear to be relevant to odor quality?”

The numbers in Table 1 represent the total number of molecular descriptors from these classes that were identified by our approach as an overview. We agree that it would be much more informative to provide the exact molecular descriptor sets that were optimized for each receptor. We have now created a new table that provides molecular descriptor symbols, weights, descriptions, classes, and descriptive dimensionality for each Or-optimized set used in our study. This provides a wealth of useful data. While several of these descriptors are very specific and represent high dimensional graph based theory, a number of selected descriptors are easily understood such as functional group counts and atom types descriptors. Through this table readers will be able to identify which functional groups and 2D fingerprints are most important for a particular receptor and specialists will be able to utilize them in their own analysis such as the prediction pipeline we have created.

2B) “The description of the SFS approach does not provide any detail as to how each incremental descriptor was chosen to grow the set.”

We apologize for being unclear and have clarified this in the Materials and methods section.

3) “…this very intriguing analysis should go in the Discussion or a deeper analysis is required for the reader.”

We agree and thank you for your suggestion. We have moved this section to the Discussion.

4) “The authors should provide more raw data from their analyses.”

We thank you for this suggestion and agree that this manuscript would benefit from increased raw data. We have incorporated several new supplemental tables and figures. Newly incorporated data includes: optimized molecular descriptor sets for each predicted Or, including name, weight, class, description, and dimensionality; top 100 predicted compounds for each of the receptors analyzed; APoA plots for individual Ors; and pharmacophore structures for active compounds for each Or.
