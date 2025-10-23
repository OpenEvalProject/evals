# Peer review - Round 1

Editors:
- Paula Fernandez, INTA Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91597.3.sa0](https://doi.org/10.7554/eLife.91597.3.sa0)

The authors describe an important tool, GromovMatcher, that can be used to compare proteomic data from various experimental approaches. The underlying method is innovative, the algorithm is clearly described, and the validation that is presented is convincing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91597.3.sa1](https://doi.org/10.7554/eLife.91597.3.sa1)

Summary:

The authors have implemented Optimal Transport algorithm in GromovMatcher for comparing LC/MS features from different datasets. This paper gains significance in the proteomics field for performing meta-analysis of LC/MS data.

Strengths:

The main strength is that GromovMatcher acheives significant performance metrics compared to other existing methods. The authors have done extensive comparisons to claim that GromovMatcher performs well.

Weaknesses:

The authors might need to add the limitation of datasets and thus have tested/validated their tool using simulated data in the abstract as well.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91597.3.sa2](https://doi.org/10.7554/eLife.91597.3.sa2)

Summary

The goal of untargeted metabolomics is to identify differences between metabolomes of different biological samples.

Untargeted metabolomics identifies features with specific mass-to-charge-ratio (m/z) and retention time (RT). Matching those to specific metabolites based on the model compounds from databases is laborious and not always possible, which is why methods for comparing samples on the level of unmatched features are crucial.

The main purpose of the GromovMatcher method presented here is to merge and compare untargeted metabolomes from different experiments. These larger datasets could then be used to advance biological analyses, for example, for identification of metabolic disease markers.

The main problem that complicates merging different experiments is that m/z and RT vary slightly for the same feature (metabolite).

The main idea behind the GromovMatcher is built on the assumption that if two features match between two datasets (that feature i from dataset 1 matches feature j from dataset 2, and feature k from dataset 1 matches feature l from dataset 2), then the correlations or distances between the two features within each of the datasets (i and k, and j and l) will be similar. The authors then use the Gromov-Wasserstein method to find the best matches matrix from these data.

The variation in m/z between the same features in different experiments is a user-defined value and it is initially set to 0.01 ppm. There is no clear limit for RT deviations, so the method estimates a non-linear deviation (drift) of RT between two studies. GromovMatcher estimates the drift between two studies, and then discards the matching pairs where the drift would deviate significantly from the estimate. It learns the drift from a weighted spline regression.

The authors validate the performance of their GromovMatcher method using a dataset of cord blood. They use 20 different splits and compare the GromovMatcher (both its GM and GMT iterations, whereby GMT version uses the deviation from estimated RT drift to filter the matching matrix) with two other matching methods: M2S and metabCombiner.

The second validation was done using a (scaled and centered) dataset of metabolics from cancer datasets from the EPIC cohort that were manually matched by an expert. This dataset was also used to show that using automated methods can identify more features that are associated with a particular group of samples than what was found by manual matching. Specifically, the authors identify additional features connected to alcohol consumption.

Strengths:

I see the main strength of this work in its combination of all levels of information (m/z, RT, and higher-order information on correlations between features) and using each of the types of information in a way that is appropriate for the measure. The most innovative aspect is using the Gromov-Wasserstein method to match the features based on distance matrices.

The authors of the paper identify two main shortcomings with previously established methods that attempt to match features from different experiments: (a) all other methods require fine-tuning of user-defined parameters, and, more importantly, (b) do not consider correlations between features. The main strength of the GromovMatcher is that it incorporates the information on distances between the features (in addition to also using m/z and RT).

Weaknesses:

The main weakness is that there seem not to be enough manually curated datasets that could be used for validation. It will, therefore, be important, for the authors, and the field in general to keep validating and improving their methods if more datasets become available.

The second weakness, as emphasized by the authors in the discussion is that the method as it is set up now can be directly used only to compare two datasets. I am confident that the authors will successfully implement novel algorithms to address this issue in the future.
