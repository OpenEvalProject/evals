# Author response - Round 1

Authors:
- Allison L Hicks ([ORCID: 0000-0003-1372-1301](https://orcid.org/0000-0003-1372-1301))
- Stephen M Kissler ([ORCID: 0000-0003-3062-7800](https://orcid.org/0000-0003-3062-7800))
- Tatum D Mortimer ([ORCID: 0000-0001-6255-690X](https://orcid.org/0000-0001-6255-690X))
- Kevin C Ma
- George Taiaroa
- Melinda Ashcroft
- Deborah A Williamson ([ORCID: 0000-0001-7363-6665](https://orcid.org/0000-0001-7363-6665))
- Marc Lipsitch ([ORCID: 0000-0003-1504-9213](https://orcid.org/0000-0003-1504-9213))
- Yonatan H Grad ([ORCID: 0000-0001-5646-1314](https://orcid.org/0000-0001-5646-1314))

## Response text

DOI: [10.7554/eLife.56367.sa2](https://doi.org/10.7554/eLife.56367.sa2)

Essential revisions:

1) How would a low rate of either sequencing or phenotyping error affect the different approaches? Presumably, these effects would not qualitatively affect the outcomes, but would such error rates, which are often observed, falsely improve or weaken one approach?.

Thank you for bringing this up and giving us the opportunity to clarify and address this.

While false-positive phenotyping errors (i.e., a susceptible isolate that was called resistant) would presumably be further investigated and ultimately corrected, we agree that false-negative phenotyping errors (i.e., a resistant isolate that was called susceptible) could absolutely delay detection of a novel AMR variant. However, we don’t believe there is reason to think that this should disproportionately affect detection efficiency of any of the targeted sampling approaches compared to random sampling or compared to each other.

Sequencing errors could affect the efficiency of the phylogeny-aware sampling approaches. The differential prevalence of resistance variants among datasets might raise the concern that the improved detection efficiency by phylogeny-aware sampling arose from study-dependent sequencing artifacts. However, we evaluated each dataset separately, so variation in sequencing methods across datasets should not have confounded our analyses. When applied in a surveillance setting, we do agree that sequencing errors could in theory result in closely related isolates appearing to be more distantly related, thus reducing the increased efficiency of phylogeny-aware sampling compared to random sampling. However, we don’t expect that the opposite would occur (i.e., it is unlikely that sequencing errors would result in distantly related isolates appearing to be very closely related), so sequencing errors are unlikely to make the clonal group approach worse than random sampling. Further, we expect that the influence of sequencing errors should be largely ameliorated by inspecting sequencing quality prior to analysis. We have now added some discussion of sequencing errors (Discussion, fourth paragraph).

2) The resistance markers used are mostly point mutations or recombinant alleles. What are the expectations for the performance of these sampling approaches for acquired resistance genes (e.g., plasmid borne AMR genes)?

Thank you for bringing up this point. We agree that it is not entirely clear how phylogeny-aware sampling (particularly when based on reference-based mapping, as we have done here) will perform in detecting novel variants associated with gene acquisition. While the gonococcal resistance variants associated with plasmids are too prevalent to be useful for our evaluations here, there is some evidence for a relationship between the core genome and the presence/absence of these plasmids, suggesting that core genome-based phylogeny-aware sampling may still be useful for these kinds of resistance variants. We also suspect that with the genomic data required for phylogeny-informed sampling, it may be possible to rapidly identify some novel resistance by screening for homologs of known resistance genes from other species. Further, k-mer based methods that allow for clustering based on both core and accessory genome similarity may be more useful in the context of novel resistance associated with gene acquisition. We have now expanded our discussion of this (Discussion, fifth paragraph).

3) There are other large datasets with genomic and phenotypic information (e.g., NARMS) that could be used to test this-and find this approach useful. While I do not expect (nor want) the authors to examine these datasets, recognizing that this technique would be useful for large surveillance systems should be mentioned. It would be a shame for surveillance systems to be unaware of these findings.

Thank you for this suggestion. We agree that these targeted sampling approaches may be more broadly applicable outside of the context of maintaining diagnostics. We have now highlighted this in the Discussion (eighth paragraph).
