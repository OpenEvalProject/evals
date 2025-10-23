# Peer review - Round 1

Editors:
- Diethard Tautz, Max-Planck Institute for Evolutionary Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57468.sa1](https://doi.org/10.7554/eLife.57468.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Plasticity and evolutionary convergence in the locomotor skeleton of Greater Antillean Anolis lizards" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kathryn Kavanagh (Reviewer #2); Paul Brakefield (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This study is an important advance providing empirical evidence that developmental plasticity is not biasing options for selection in this widely studied Anolis radiation. Despite this lack of facilitating plasticity, the anole species do tend to evolve similar phenotypes in similar habitats. The authors conclude that any plasticity is a transient effect and that parallelism does not depend on plasticity.

It is a strength of the study that it analysed the shape of pectoral and pelvic girdles and long bone thickness, rather than just length, to see if skeleton parts that responded to mechanical stress are more evolvable. The result that 'signature traits' that evolved to adapt to a particular habitat differed among ecomorph pairs suggested that the skeletal parts involved in adaptation are not in fact parallel. But it is unclear whether this is just noise in the system or a real signal of the lineage or habitat.

Essential revisions:

1) The conclusions depend very much on a procedure in morphometrics that appears to be problematic, namely the "Transformation of morphological dataset" described in the text and the supplement. This is not well justified with no proof or reference. Why should one collect landmark data, apply some sort of random standardisation to them and add/treat them with other linear variables? This adds further random signal to the landmark data prior to the Procrustes fit. Hence, there needs to be a clear justification of this procedure.

2) Instead one could do a 2 Block Partial Least Squares analysis to compare 2 sets of variables regardless of the type of data (e.g. Procrustes coordinates of the skull versus diet). This is routinely used in this type of studies in which one wishes to calculate the strength of association (i.e. covariation) between 2 sets of different variables (Rohlf and Corti, 2000) and is a general analysis in squamate studies (Adams and Rohlf, 2000). There is no a priori or some sort of rescaling of the data beforehand.

3) The study includes shape data versus different types of size data with the size data quite possibly being correlated among themselves, but there is no test for this. One would have expected analyses similar to the ones carried out in Dickson et al., 2017. For instance at P.6 paragraph starting with "To determine…by ANCOVA and PGLS".

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Plasticity and evolutionary convergence in the locomotor skeleton of Greater Antillean Anolis lizards" for consideration by eLife. Your article has been re-reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen Diethard Tautz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kathryn Kavanagh (Reviewer #2); Paul Brakefield (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

There is overall a positive assessment of your revisions, but there remains the central problem around the statistics. We acknowledge that there is no way to capture all aspects of morphological change, and it seems a good attempt to create a new combined metric including shape measurements in addition to linear measurements. However, the statistical morphometrics specialist among the reviewers (reviewer #1) still raises substantial issues that are outlined in the review. To resolve this, we should like to ask you to work out in more detail of what you had only generally indicated in your response letter. You should properly separate the different types of measurements (size, shape), analyze them individually and not use transformations. Your conclusions will evidently be strengthened by having individual analyses of traits and perhaps can be interpreted more clearly as individual evolved characters that could be linked to functional and developmental processes. Also, it would be more comparable to previous studies. You may in addition want to include the combined metric, but you need to discuss the issues with this that were brought up by the statistical expert.

Reviewer #1:

The response of the reviewers regarding the transformation of the data has not removed my concern. As it stands, the morphological dataset (prior to the "transformation") includes Procrustes aligned landmark coordinates, centroid size and some linear measurements, that is, a mixture of shape variables (of which 7 are redundant because of the degrees of freedom lost during the Procrustes fit) and various size variables. As such, this is already difficult to expect to be an easily interpretable signal (in particular size and shape signals are confounded and their potential relationships are irretrievable).

The authors refer to Stuart et al., 2017 as a similar approach to the construction of a morphological dataset. This is indeed a similar approach and Stuart et al., 2017 likewise suffers from the same weaknesses (linear dependency of the shape variables and increased difficultness of biological interpretations).

Of greater concern is the transformation of the data suggested, which further deteriorates the biological meaningfulness the authors expect to extract from the data: Procrustes shape variables, for instance, are linked by the geometry of the shapes they describe. Centring to zero and dividing each of them by their standard deviation completely destroy the meaningful relationships among these shape variables.

In summary, this is not a path to obtain a "valid multivariate space" for the analyses envisioned. The multivariate space obtained combines incommensurate variables and therefore lacks meaningful metric and inner product, compromising the valid usage of the notion of angle central to the research question of the paper.

The authors report that they obtain similar results when working on subsets of the data. They add Figure 4—figure supplement 1 to support this. However, this is not informative since it is a document without its context. They did some separate angle analyses on each subset of their data. Angles in high-dimensional spaces, as they occur particularly in geometric morphometrics, can appear contrary to our intuition from two- or three-dimensional planes and spaces. Therefore, some caution is necessary when interpreting them. In a two-dimensional space, given one vector, there is only one direction that is perpendicular to it. In three dimensions, by contrast, there is a whole plane that is perpendicular to the first vector, and there is thus a greater number of different ways in which the vectors can have different directions. Therefore, even relatively large angles between vectors can suggest that the resemblance between them is unlikely to be of random origin.

This is what I would then suggest them to do: work and present results for internally coherent subsets of data (size data, shape data) allowing easier interpretations, additional visualisations (shape changes for instance), and avoiding questionable inferences from a mathematically ill-defined morphospace.

Reviewer #2:

The authors have satisfactorily responded to the reviews and updated their manuscript appropriately. Another reviewer should look at the statistical analysis as I'm not an expert. I look forward to seeing the paper published.

Reviewer #3:

The authors have done a good, indeed excellent, job in their response. I would welcome publication.
