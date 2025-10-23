# Peer review - Round 1

Editors:
- Chris P Ponting, University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59959.sa1](https://doi.org/10.7554/eLife.59959.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Previous work led to a general expectation that genetic variants commonly have large effects on exon inclusion levels and that these will often explain disease risk or trait variation. This manuscript corrects this more general view and, importantly, indicates which genetic variants are most/least likely to alter disease risk. The study resolves this issue at depth (across all PSI values) using extensive genetic data sets.

Decision letter after peer review:

Thank you for submitting your article "Mutations primarily alter the inclusion of alternatively spliced exons" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nuno L Barbosa-Morais (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This is an extensive and generally carefully executed study of existing mutagenesis data, human data from GTEx, and some novel mutagenesis data. Results represent the most in-depth, genome-wide comparative examination of the impact of sequence variation on splicing of exons over the spectrum of PSI levels. The authors show that exons of intermediate inclusion levels are much more easily affected by genetic effects on splicing, with high included/excluded exons being much more robust to genetic effects. This represents an important and potentially clinically useful observation. Furthermore, via an analysis of exonic splicing enhancers (ESEs), they add some mechanistic interpretability to this general finding.

Essential revisions:

1) The GTEx analysis needs to account for linkage disequilibrium in order to account for non-independent tests. The approach using a simple effect size cutoff ("only 14% of which are associated with changes in inclusion greater than 10%") is insufficient because it leads to issues with multi-counting data and some difficulties in biological interpretation. Including each variant-exon pair in the downstream analysis pools data from different tissues and introduces massive non-independence in the data. The data should be filtered to have each exon represented only once by either: (a) performing sQTL mapping and then choosing the variant with the best p-value to represent a given variant association to splicing (or fine-mapping analysis), or (b) simply merging the intronic/exonic analyses (or only analyze e.g. exons) because – as you argue – the GTEx variants that you analyze are not necessarily the causal exonic or intronic variants that you seek to study. Our preference is (a).

2) Your study would be more insightful if you could investigate, at greater detail, determinants underlying the effects of mutations that have the greatest impact on PSIs of constitutive/highly included exons. In addition to examining relative splice site strength, such an analysis could also take into account the frequency at which mutations result in the creation of predicted exonic splicing silencers. Your ESE analysis should take account of both splice site strength and ESE frequency/content and go beyond previous analyses, e.g. Fairbrother, Burge and colleagues, Science 2002, because of the richer data set. For example, what is the relative impact of mutations on constitutive exons with weaker vs. stronger 5' and or 3' splice sites? Does a higher frequency of ESEs in constitutive exons confer robustness to effects of mutations even when the flanking splice sites are relatively weak?

3) The authors refer to the potential significance of the results when interpreting variant effects in disease studies, yet should provide an analysis that does this. Using a resource such as ClinVar, there is an opportunity to determine whether otherwise similarly annotated variants (e.g. synonymous variants) in exons of intermediate inclusion levels are more likely to be implicated in disease.
