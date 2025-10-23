# Peer review - Round 1

Editors:
- Bianca Jones Marlin, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63207.sa1](https://doi.org/10.7554/eLife.63207.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We congratulate you on your development of a neural network that automatically identifies grooming in mice. Your work to characterize grooming behavior across strains, sex and conditions for C57 mice (e.g. lighting, season), to identify loci and genes linked to grooming and open field behavior and to identify human homologs for genes linked to grooming in mice will have sustained influence on the field.

Decision letter after peer review:

Thank you for submitting your article "Action detection using a neural network elucidates the genetics of mouse grooming behavior" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Taffe as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ioana Carcea (Reviewer #2); Nancy Padilla (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In summary, Geuther et al. demonstrate the use of machine learning to identify and classify grooming behaviors in an impressively varied cohort of mice species. Using a 3D convolutional neural network that automatically identifies grooming in mice, they conducted a genome-wide association study (GWAS) to identify loci and genes linked to grooming and open-field behavior. Finally, the authors performed analyses to identify human homologs for genes linked to grooming in mice, with a focus on loci associated with psychiatric illness in humans. Novel findings include the identification of gene-phenotype modules that identify genes linked to both human and mouse phenotypes.

Essential revisions:

1) It is unclear how robust the grooming algorithm is to new videos/new animals. Were the training video clips all from a small subset of videos? The authors say 2M frames were annotated from 1,253 video segments, but it is unclear how many strains/mice/videos (not video clips or segments) they came from in total. In the Materials and methods, they mention that the training data comes from 1,253 video clips but there are no additional details. How many animals were represented in the training dataset and in the testing dataset? How robust is the algorithm to differences in animal size (which can be affected by camera distance) and to video frame rate? Where all videos used with this network taken at identical camera distances, video frame rates, and backgrounds (e.g. home cage vs. white background)? Since the training dataset needed for good performance is so large (2M frames) understanding the flexibility of the network is crucial for the community to adopt it successfully. When using and implementing the network, the devil is on the details.

2) The authors train JAABA with 20% of their dataset and show in Figure 3A and supplementary figure that it performs worse than the new network with the same 20%, but AUCs are relatively similar. But to be sure that this is not a fluke of the specific subset of the data used and to have statistical power to claim the superiority the authors should subsample the training data and repeat the comparison more times. This way they can determine if there the network with 20% of the data outperforms JAABA in every case or with X probability.

3) The authors use k-means clustering for different analyses, but there are no details on how the different clustering procedures were done.

4) Reviewers have concerns related to the robustness of the 3D convolutional neural network. We believe that in order for the scientific community to take advantage of this tool the authors need to provide more information.
