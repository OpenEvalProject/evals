# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/01cwqze88 National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78635.sa0](https://doi.org/10.7554/eLife.78635.sa0)

This important article uses an impressively rich data set (obtained and curated by the authors) to compare the structural brain connectomes of many animals spanning six taxonomic orders. The approach is innovative and relies on graph theoretical measures to describe the connectivity, which means it can be done without the need to spatially/functionally match the brains. The authors find compelling evidence that there is more variability between than within order. They attribute this effect to changes in local connectivity features, whereas global patterns are preserved. The approach can potentially be a useful way to study phylogeny and brain evolution.


---

# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/01cwqze88 National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78635.sa1](https://doi.org/10.7554/eLife.78635.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A connectomics-based taxonomy of mammals" for consideration by eLife, and sorry for the delay in getting the reviews back to you.

Your article has been reviewed by 3 peer reviewers, including Saad Jbabdi as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Katja Heuer (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The paper was well received. There are several technical comments that need addressing, but the main revision in my opinion concerns the need for more insight as to what is driving the similarities and differences in the connectomes. See the detailed comments below.

Please find below the detailed reviews. I have tried to merge the 3 reviewer comments into a single set of comments, so these might not be in a sensible order.

Reviewer Comments

Reviewers' (Recommendations for the authors):

I think the assumption of the use of the same 200 regions for all species should be shown to be justified.

I would have liked to have seen more detail on how the differences between species is really implemented on the brains, if even in a few species. For instance, some of the authors have published extensively on human specializations in connectivity. It would be nice to show that some of the differences they identified in that work fall under the 'local regional connectivity profile' features that are reported here.

Species names sometimes correspond to groups of species. Would it be possible to provide the exact species names? The dataset in Zenodo includes, for example, "Macaque" which I assume may be Rhesus macaques, but for example, "colobus" is a group of monkeys including several species and it would be good to know which species have been included here. Given the vast nature of the dataset, either the exact English names, or the binomial species names, or a csv file which could allow potential users of the data to make the correspondence could be great to facilitate reuse of the data.

On page 6 the authors conclude that given the larger connectome similarity within one taxonomic group, the organisation of the brain connectome may be under selection pressure. However, also the Brownian motion model of evolution – where phenotypes are assumed to vary randomly along the phylogenetic tree – can explain phenotypes that are more similar within one taxonomic group.

When the authors introduce that the "common space" approach was used, maybe they can add a short note on what this means in addition to just the reference?

Methods: in the abstract, the authors say the data was "collected using a single protocol on a single scanner." whereas in the methods section they refer to 2 scanners and 2 field strengths. It seems quite standard to acquire small animal brains on a scanner with higher field strength and different head coils, there is no problem, I just thought maybe there is no need for the 1-scanner statement in the abstract? If the authors wanted to keep something along these lines, it could take up the idea they mention of a "unified MRI protocol was implemented for all species" I guess.

On page 7, the authors say "Consistent with the notion that neural circuit evolution involves local circuit modifications to adapt to specific challenges [10], such as extreme environmental pressures [36, 79, 89], or to support specific behaviours." I would just suggest a slight reformulation, as evolution doesn't do modifications to adapt to challenges or to support behaviour, but rather involves random modifications, that then may have provided an advantage in facing certain challenges or supporting certain behaviours.

On page 8, the authors suggest a "This scaling results in less space for white matter connectivity with increasing brain size." I wonder how this result compares with the reports of a positive allometry of white matter. For example, Zhang and Sejnowski

(https://doi.org/10.1073/pnas.090504197) report a scaling of 1.23 for white matter and build a scaling model for justifying it. There are several references within that paper that go in the same direction. The positive scaling of WM seems also intuitively true, as mice have very little WM compared with monkeys or humans, for example.

Other Comments:

– Visualisation

Some comments / suggestions on the various visualisations in the paper:

– I think a 2D scatter plot using multidimensional scaling would nicely show the between and within order distances (I tried it on your data, it looks nice). This could be complemented by a hierarchical clustering diagram?

– I am not sure why you need to min-max rescale all the distances to be between 0 and 1. In addition, min-max measures are sensitive to outliers. If one group happens to have an outlier, that could drive the entire group to be at the extreme. Is this likely to be happening here? It would also be useful to know at what stage this rescaling is done?

– I don't think the histograms in figures 2 and 3 should be shown using kde smoothing. It hides the data, and actually does a disservice to the data (e.g. in Figure 2B, the diagonal values are visibly lower than the extra diagonal values, but when kde-smoothed the effect appears to be lower than it is).

Another thing about the spectral approach: the lowest eigenvalue is famously important in telling us something about how connected the network is in general (i.e. how easy it is to break it down). Did you see any differences between and within species/orders in this measure?
