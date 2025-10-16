# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65760.sa1](https://doi.org/10.7554/eLife.65760.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript takes a deep dive into the skeletal effects of burrowing and eusocial Damaraland mole rats. By exploring the genetic and skeletal consequences of breeding restricted to a single queen with multiple and closely-timed pregnancies and lactation, this study offers a compelling story that will bolster textbooks on skeletal biology, mammalian evolution, and ethology. The results show the molecular mechanisms driving adaptive plasticity within the unusually expanded lumbar spine and thin limb bones of queens are an adaptive consequence of breeding status.

Decision letter after peer review:

Thank you for submitting your article "Morphological and genomic shifts in mole-rat 'queens' increase fecundity but reduce skeletal integrity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) From Reviewer #1: I recommend generating a new first figure with an image of the queens and non-breeders along with a full skeleton (x-ray is fine). Because this work is a novel case-study in mole rats that I think belongs in textbooks, a figure illustrating the study taxon with a bit of introduction and then highlighting of the skeleton will potentially broaden the audience. I could easily see this work as part of skeletal biology course.

2) Please also address all of the smaller editing and clarification changes requested by both reviewers.

Reviewer #1 (Recommendations for the authors):

Additional Figure: I recommend generating a new first figure with an image of the queens and non-breeders along with a full skeleton (x-ray is fine). Because this work is a novel case-study in mole rats that I think belongs in textbooks, a figure illustrating the study taxon with a bit of introduction and then highlighting of the skeleton will potentially broaden the audience. I could easily see this work as part of skeletal biology course.

Figure 1 b: Change the shape of mean dots for queens such that they are different than that of non-breeders

Line 623, I believe the VivaCT uses a known-density phantom for comparisons. Is density data available? This isn't a requirement but might offer another compelling measure to support a conclusion that extends beyond just endosteal resorption.

Does the concentration and integrity of collagens shift with breeding status?

This is lovely work. Thank you for publishing. Best of luck.

Reviewer #2 (Recommendations for the authors):

I cannot comment on the gene regulation analyses or suitability of the protocols associated with those, as this is not my area of expertise. Specifically, I cannot comment on methods section line 500 – 620.

I have several minor comments, by line:

Ln331: "a correlate of minimum resistance to bending" would be more accurate description of Imin – it's the minimum second moment of inertia

Ln418: Also perhaps the extent to which this represents a recoverable insult given longevity in queens for this species, see:

Schmidt, C. M., Jarvis, J. U. M., and Bennett, N. C. (2013). The long-lived queen: reproduction and longevity in female eusocial Damaraland mole-rats (Fukomys damarensis). African Zoology, 48(1), 193-196. doi:10.1080/15627020.2013.11407583

Ln631: Imin and CA can be extracted directly from the cross-section in Rhino using Areamoment without need for ImageJ. but here you re-thresholded a.tif or converted an extracted.eps and then used that in ImageJ, correct? Was this done to manual segment the endosteal margin?

Ln632: this macro extracts many other biomechanical properties (Imax,Imin, J, CA, TA, Theta, Ix, Iy), what was the rationale for selecting Imin? For example, J (Polar second moment of area) is often considered the most relevant indicator of a bones' mechanical performance. See, for example:

Ruff, C. B., Trinkaus, E., Walker, A., and Larsen, C. S. (1993). Postcranial robusticity in Homo. I: Temporal trends and mechanical interpretation. American journal of physical anthropology, 91(1), 21-53.

Imin is perhaps least likely to be strongly correlated with body mass. See also Davies and Shaw:

Davies, T. G., and Stock, J. T. (2014). The influence of relative body breadth on the diaphyseal morphology of the human lower limb. American Journal of Human Biology, 26(6), 822-835.

Ln636: More information needs to be provided about how bone shape was evaluated. I assume this was done using the scaled mesh files (post-alignment) or was this run using the full-size meshes? How is the method computing differences between meshes? Is mesh face number standardized/reduced? What are the output data that are used to assess similarity? I did not find any information (or a figure illustrating) the differences in shape between the queens and non-breeders for either element – what were the main differences in shape that held predictive power in the sample?

Ln673: This is an interesting idea and I appreciate the authors' consideration of this aspect since it attempts to estimate the consequence of bone resorption. However, it may be useful to add a caveat on the assumptions associated with this approach – mainly, I am not sure how valid it may be to extrapolate a linear model based on body mass of mice in comparison to that of a mole-rat. Figure S2a indicates around 150 g body mass for the specimens in the study, and certainly well below 35 g for a mouse. Also, the weaker relationship between body mass and CA for these mole rats (cited earlier in the manuscript) and the likelihood that the relationship between body mass and CA may follow a different trajectory for the two species may impact the validity of this estimate.

Ln691: Please provide all code associated with analyses performed in R and Matlab.
