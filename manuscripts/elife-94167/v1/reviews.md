# Peer review - Round 1

Editors:
- Ilona C Grunwald Kadow, University of Bonn Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94167.3.sa0](https://doi.org/10.7554/eLife.94167.3.sa0)

This important paper presents a thoroughly detailed methodology for mesoscale-imaging of extensive areas of the cortex, either from a top or lateral perspective, in behaving mice. The examples of scientific results to be derived with this method offer promising and stimulating insights. Overall, the method and results presented are convincing and will be of interest to neuroscientists focused on cortical processing in rodents and beyond.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94167.3.sa1](https://doi.org/10.7554/eLife.94167.3.sa1)

Summary:

The authors introduce two preparations for observing large-scale cortical activity in mice during behavior. Alongside, they present intriguing preliminary findings utilizing these methods. This paper is poised to be an invaluable resource for researchers engaged in extensive cortical recording in behaving mice.

Strengths:

Comprehensive methodological detailing:

The paper excels in providing an exceptionally detailed description of the methods used. This meticulous documentation includes a step-by-step workflow, complemented by thorough workflow, protocols and list of materials in the supplementary materials.

Minimal of movement artifacts:

A notable strength of this study is the remarkably low movement artifacts, with specific strategies outlined to attain this outcome.

Insightful preliminary data and analysis:

The preliminary data unveiled in the study reveal interesting heterogeneity in the relationships between neural activity and detailed behavioral features, particularly notable in the lateral cortex. This aspect of the findings is intriguing and suggests avenues for further exploration.

Weaknesses:

Clarification about the extent of the method in title:

The title of the paper, using the term "pan-cortical", may inadvertently suggest that both the top and lateral view preparations are utilized in the same set of mice, while the authors employ either the dorsal view (which offers limited access to the lateral ventral regions) or the lateral view (which restricts access to the opposite side of the cortex).

Despite the authors not identifying qualitative effects, tilting the mouse's head could potentially influence behavioral outcomes in certain paradigms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94167.3.sa2](https://doi.org/10.7554/eLife.94167.3.sa2)

Summary:

The authors present a comprehensive technical overview of the challenging acquisition of large-scale cortical activity, including surgical procedures and custom 3D-printed headbar designs to obtain neural activity from large parts of the dorsal or lateral neocortex. They then describe technical adjustments for stable head fixation, light shielding, and noise insulation in a 2-photon mesoscope and provide a workflow for multisensory mapping and alignment of the obtained large-scale neural data sets in the Allen CCF framework. Lastly, they show different analytical approaches to relate single-cell activity from various cortical areas to spontaneous activity by using visualization and clustering tools, such as Rastermap, PCA-based cell sorting, and B-SOID behavioral motif detection.

The study contains a lot of useful technical information that should be of interest to the field. It tackles a timely problem that an increasing number of labs will be facing as recent technical advances allow the activity measurement of an increasing number of neurons across multiple areas in awake mice. Since the acquisition of cortical data with a large field of view in awake animals poses unique experimental challenges, the provided information could be very helpful to promote standard workflows for data acquisition and analysis and push the field forward.

Strengths:

The proposed methodology is technically sound and the authors provide convincing data to suggest that they successfully solved various challenging problems, such as motion artifacts of large imaging preparations or high-frequency noise emissions, during 2-photon imaging. Overall, the authors achieved their goal of demonstrating a comprehensive approach for imaging neural data across many cortical areas and providing several examples that demonstrate the validity of their methods and recapitulate and further extend some recent findings in the field. A particular focus of the results is to emphasize the need for imaging large population activity across cortical areas to identify cross-area information processing during active behaviors.

Weaknesses:

The manuscript contains a lot of technical details and might be challenging for readers without previous experimental experience. However, the different paragraphs illuminate a large range of technical aspects and challenges of large-scale functional imaging. Therefore, the work should be a valuable source of solutions for a diverse audience.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94167.3.sa3](https://doi.org/10.7554/eLife.94167.3.sa3)

Summary

In their manuscript, Vickers and McCormick have demonstrated the potential of leveraging mesoscale two-photon calcium imaging data to unravel complex behavioural motifs in mice. Particularly commendable is their dedication in providing detailed surgical preparations and corresponding design files, a contribution that will greatly benefit the broader neuroscience community as a whole. The quality of the data is high and examples are available to the community. More importantly, the authors have acquired activity-clustered neural ensembles at an unprecedented spatial scale to further correlate with high level behaviour motifs identified by B-SOiD. Such an advancement marks a significant contribution to the field. While the manuscript is comprehensive and the analytical strategy proposed is promising, some technical aspects warrant further clarification. Overall, the authors have presented an invaluable and innovative approach, effectively laying a solid foundation for future research in correlating large scale neural ensembles with behavioural. The implementation of a custom sound insulator for the scanner is a great idea and should be something implemented by others.

This is a methods paper, but there is no large diagram (in the main figures) that shows how all the parts are connected, communicating and triggering between each other. This is described in the methods and now supplemental figure, but a visual representation would greatly benefit the readers looking to implement something similar as a main figure but I guess they can find it in the methods. No stats for the results shown in Figure 6e, it would be useful to know which of these neural densities for all areas show a clear statistical significance across all the behaviors. While I understand that this is a methods paper, it seems like the authors are aware of the literature surrounding large neuronal recordings during mouse behavior. Indeed, in line 178-179 the authors mention how a significant portion of the variance in neural activity can be attributed to changes in "arousal or self-directed movement even during spontaneous behavior." Why then did the authors not make an attempt at a simple linear model that tries to predict the activity of their many thousands of neurons by employing the multitude of regressors at their disposal (pupil, saccades, stimuli, movements, facial changes, etc). These models are straightforward to implement, and indeed it would benefit this work if the model extracts information on par with what it's known from the literature. We also realize such a model could be done in the future.
