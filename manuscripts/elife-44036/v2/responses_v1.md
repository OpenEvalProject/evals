# Author response - Round 1

Authors:
- Sonia Q Sen ([ORCID: 0000-0003-4693-3378](https://orcid.org/0000-0003-4693-3378))
- Sachin Chanchani
- Tony D Southall ([ORCID: 0000-0002-8645-4198](https://orcid.org/0000-0002-8645-4198))
- Chris Q Doe ([ORCID: 0000-0001-5980-8029](https://orcid.org/0000-0001-5980-8029))

## Response text

DOI: [10.7554/eLife.44036.026](https://doi.org/10.7554/eLife.44036.026)

[…] However, one concern that merits more attention is that the data in Figure 7, the crux of the conclusion for integration of the chromatin signaling, does not appear to be to the same level of rigor as the technical aspects. Authors need to address this point, by providing either more convincing data in Figure 7 or, minimally, providing more details in the results and interpretation of Figure 7 data.

Reviewer #1:

[…] Additionally, the data in Figure 7B is not completely convincing – the binding enrichment curves are quite broad and appear very noisy, suggesting that the n value of # peaks is very small, although the Monte Carlo analysis shows significance (throughout the figures authors should provide an n value in their plots).

We appreciate these comments, and have added new text to the Discussion and a new panel to Figure 7. See also new data in response to the third comment below. There are several likely reasons for the relatively low (but significant!) correlation between Gsb occupancy and the open chromatin states of the two NBs. First, different cell populations are used (NB lineages vs. total embryonic cells), different stages are assayed (0-12 vs. 9-12), different methods are used (ChIP vs. Dam). Despite these differences we were actually very pleasantly surprised to see significant enrichment of Gsb bound loci at open chromatin in a NB-specific manner – NB 5-6 shows enrichment, whereas NB7-4 does not. We have added the above text to the Discussion. We have also added a graphical representation of the Monte Carlo analysis used in 7B to the revised Figure 7 (new 7C), which demonstrates the significance of the enriched Gsb binding at unique NB5-6 Hb peaks.

We agree that it would be ideal to compare Dam (open chromatin) to Gsb-Dam (Gsb binding), but we do not yet have a Gsb-Dam fly stock. We would be very interested in adding these data in the future as an eLife Research Advance (Patterson et al., 2014) linking back to our current paper.

Dr Mandel is also correct in noting that the number of peaks is small in 7B. While the number of peaks used in 7A (sites of open chromatin) are 20,838 and 18,201 for the NB5-6 and 29,817 and 31,080 for NB7-4, the number of peaks used in 7B (NB-specific Hb-bound loci) is 504 and 718. We have now mentioned the numbers of peaks used in these plots in the figure legend.

As well as toning down wording in the title, Abstract and Discussion that they have proven intersection, as opposed to generating data that is consistent with this conclusion. There is no direct evidence presented that the STF open chromatin is sufficient for binding of Hb, only that the binding of the two factors is enriched in close proximity in open chromatin. In their Discussion, authors indicate that experiments to determine causality of Gsb binding/open chromatin for Hb binding lie outside the scope of the paper. Agreed, such studies would involve further work, but as it stands the current study doesn't support the bold title that the chromatin landscape allows integration.

We appreciate this comment, and we have completely rewritten our title and Abstract accordingly. We have changed the title to: “Neuroblast-specific open chromatin landscapes allow the temporal transcription factor, Hunchback, to bind neuroblast-specific genomic loci” which leaves room for future experimental verification. In the Impact statement, Introduction, and Discussion we say that “our findings support a model” or “we propose that” in all places.

Unless I missed it, authors do not state explicitly precisely how close the Hb and STF sites of enrichment are? Related to this, in terms of strengthening the correlative data, authors might consider plotting the distributions of distances of the closest Gsb peaks (or motifs) from the peak center of the Dam:Hb peaks and doing the same for other "control" STF or TFFs/motifs Chip data.

This was a great suggestion, thank you! We found that of the 503 Hb enriched loci in NB5-6, 101 had a Gsb peak within 2Kb of the centre, whereas, this number was only 49 for NB7-4. A Fisher’s exact test on these data found this spatial relationship to be highly significant for NB5-6 (p=8.7812e-19), but not for NB7-4 (p=0.077982). These findings have been added to the text.

Authors indicate that they didn't see any other motifs close to Hb sites but it wasn't clear whether the analysis was genome wide? It might also be optimal for authors to perform their own ChIP experiments to make this critical point.

We now say in the last paragraph of the Discussion: “we have been unable to find any de novo DNA motif enriched within 1kb of Hb-bound loci throughout the genome.” We feel our Hb-Dam data is sufficient to identify Hb binding sites, and we have validated it against very high quality Hb ChIP experiments using stage 9 whole embryos with excellent correlation.

Regarding the Discussion. How does Gsb open chromatin – must be recruiting enzymes? Anything known about a Gsb complex? Are the Gsb binding sites associated with enhancer chromatin marks?

Thank you very much for this comment and for provoking us to dive into the mammalian Pax literature. Although Drosophila Gsb shows no protein or genetic interactions with chromatin regulators (Flybase and PubMed), its closest mammalian relatives, Pax3 and Pax7, are well-known to recruit trithorax complex proteins to open chromatin. We now cite these studies in the Discussion: “Although nothing is currently known about the role of Gsb in chromatin regulation, the closely related mammalian Pax3 and Pax7 transcription factors can recruit histone methyltransferase to promote open chromatin and increase target gene expression (Diao et al., 2012; Kawabe et al., 2012; McKinnell et al., 2008). […] It would be informative to test whether Gsb can recruit trithorax complex methyltransferases to open genomic loci in row 5 neuroblasts, and whether this is required for row 5 neuroblast spatial identity and differential binding of Hb.” These experiments are now among our highest priorities for the coming year!

Reviewer #3:

[…] One thing confused me. The Abstract says:

"Profiling chromatin accessibility showed that each neuroblast had a distinct chromatin landscape: Hunchback-bound loci in NB5-6 were in open chromatin, but the same loci in NB7-4 were in closed chromatin."

I assume this is just poorly worded since it seems to contradict what's said in the paper (The data show that Hb binding in NB7-4 is in open chromatin in NB7-4)? I'm putting this in the major comments section since having an Abstract that says the opposite of the paper isn't good.

You are correct, it was poor wording. We have changed this sentence to say:

“each neuroblast had distinct open chromatin domains, which correlated with differential Hb-bound loci in each neuroblast.”
