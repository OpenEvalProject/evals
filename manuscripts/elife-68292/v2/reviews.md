# Peer review - Round 1

Editors:
- Helena Pérez Valle, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68292.sa1](https://doi.org/10.7554/eLife.68292.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Capturing scientific knowledge in computable form" to eLife for consideration as a Feature Article. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by two members of the eLife Features Team (Helena Pérez Valle and Peter Rodgers).

The reviewers and editors have discussed the reviews and we have drafted this decision letter to help you prepare a revised submission.

Summary:

The manuscript of Wong et al., introduces Biofactoid, a novel and intuitive tool to collect interaction data from publications. The manuscript text is clear and provides both a general background for non-specialists as well as it contains the key technical details for experts. The figures nicely illustrate Biofactoid and its application. The authors not only developed the tool but also carried out multiple tests and pilots with users, editors and invited authors. All these phases are properly documented and presented in the manuscript. However, a number of points need to be addressed to make the article suitable for publication.

Essential revisions:

1. Please revise the title so that it more precisely describes the current capabilities of Biofactoid and the use cases demonstrated.

2. The amount of information collected for an interaction (that is, after the drawing just the type of molecular event) is not enough to really utilize the power of this approach in other projects. In particular not having an option to add some kind of biological context and detection methods is a missed opportunity. Please consider introducing an optional box for the biological context, in particular to name the tissue/cell line or the condition (healthy, cancer, etc.). This could come very useful when there are conflicting entries (A activates B; A inhibits B). With the biological context it could be clear that both are correct, otherwise it would look like the same interactors but different signs for the interaction and no further information. As for the type of detection, integrating the Molecular Interactions Controlled Vocabulary (https://www.ebi.ac.uk/ols/ontologies/mi) and facilitating data entry with autocomplete functions would provide useful extra information without overly increasing the time it takes to make a submission. Please consider updating Biofactoid to include this functionality. Please also clarify what ontology (if any) is used for relationships in Biofactoid.

3. Please highlight the fact that submissions to Biofactoid can be edited by users later on using the link sent in the original email. This may be useful if users make a mistake during the submission process or if they need to update the diagram during the publication process.

4. Please address whether there is a process for removing a submission altogether (e.g. if a submission is found to be incorrect or if a paper is being retracted).

5. The two sub-figures of Figure 2B are not easily reproducible. With https://biofactoid.org/ as an entry point, it was not possible to get any networks spanning more than the small ones extracted from a single article as shown in Figure 2A. With pathwaycommons.org as an entry point, it was not possible to find the interactions given in the figure. Concretely, on https://www.pathwaycommons.org/, trying "senp1 sirt3" and clicking on "Interactions", the result was "No interactions to display". Please provide more detailed instructions so the figures shown can be reproduced, or modify Figure 2B to reflect a network that can be obtained using Biofactoid.

6. Please include a discussion of how the facts stated in the paper, regarding the use of Biofactoid, could be qualitatively or quantitatively assessed. Currently, an author working with Biofactoid at all is taken as a successful end point, but surely it will be important to verify that the tool works as described and is, therefore, useful to the community. An assessment could be done, for example, in comparison to professional curators' work, as is often done for text mining approaches.

7. Please include the overall number of recorded facts generated over the multi-step process, including the number of papers used and the facts per paper.

8. Please temper your statements regarding the search and exploration functions of the system. Currently biofactoid.org seems to have no query interface. Since the data is not yet in PathwayCommons, interactive access is effectively only by browsing the papers shown in the landing page, but the figures and text imply much more functionality than is actually available to the user at this point.

9. Please include a comparison to related approaches, considering the citations referenced in line 235 of the manuscript.

10. Please state under what license contributors to Biofactoid are contributing their data, and make it clear both in the article and also in the website, so that users know how they can (re)use the data.

11. Please provide each of the Figures in your manuscript as a separate figure file.
