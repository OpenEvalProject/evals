# Author response - Round 1

Authors:
- Christopher J Giuliano ([ORCID: 0000-0002-0586-6095](https://orcid.org/0000-0002-0586-6095))
- Ann Lin
- Joan C Smith
- Ann C Palladino
- Jason M Sheltzer ([ORCID: 0000-0003-1381-1323](https://orcid.org/0000-0003-1381-1323))

## Response text

DOI: [10.7554/eLife.32838.057](https://doi.org/10.7554/eLife.32838.057)

Essential revisions:

1) Although the Cal51 xenograft data are reasonable, the MDA-MB-231 xenograft data in Figure 2G are simply not convincing The Rosa 26 c1 cells did not grow at all (this is unexpected given that MDA-MB-231 cells generally grow very aggressively as xenograft tumors), whereas the MDA-MB-231 KO c1 cell tumors grew reasonably well. In contrast, both the MDA-MB-231 KO c2 and Rosa26 c2 cells grew poorly and with odd kinetics. The authors need to clearly acknowledge these imperfections in their own data and explain why the MDA-MB-231 cell results look so strange.

MDA-MB-231 is a highly-heterogeneous breast cancer cell line. Sub-populations within MDA-MB-231 exhibit significant differences in gene expression, proliferation, and colony-formation ability. For instance, Khan et al., 2017, derived single-cell clones from 12 MDA-MB-231 cells, and observed striking differences in their growth rates. Sub-populations within MDA-MB-231 are also known to exhibit varying levels of “stem cell-like” or “tumor-initiating” behavior (Fillmore et al., 2008). We hypothesized that the poor growth of our MDA-MB-231 clones as xenografts could simply reflect the fact that cells in the parental population display different abilities to form tumors, and, by chance, we isolated several clones with limited tumor initiating capacity. To test this, we performed additional xenografts using non-clonally-derived MDA-MB-231 populations (Figure 2—figure supplement 2). For these experiments, we transduced the MDA-MB-231 parental population with a Rosa26 gRNA or two different gRNAs targeting MELK, and then selected gRNA-expressing cells without single-cell cloning. We verified by western blotting that the transduced cells exhibited near-complete depletion of MELK (Figure 2—figure supplement 2A). When these cell populations were injected into nude mice, they grew significantly faster than our MDA-MB-231 clones grew, and the animals had to be sacrificed within 26 days after injection. Additionally, the MELK-depleted populations grew at comparable or superior rates to the control populations. These results suggest that the poor growth of our clonal xenografts is due to differences in tumor-formation potential between single cells from MDA-MB-231, and further verify that MELK is dispensable for breast cancer growth.

2) The Sanger sequencing of the PCR product from the knockout clones as shown is not a very informative presentation of the data. It would be more rigorous to pick ~10 clones of the PCR product after topo cloning and sequence these to get a more accurate representation of the gRNA-mediated alterations. Are the alterations shown homozygous, heterozygous, or hemizygous?

We initially verified our A375 and DLD1 MELK-knockout clones by PCR-amplifying and sequencing the site targeted by the gRNA and by western blotting. As suggested by the reviewers, we further verified knockout status by using TOPO cloning to sequence individual MELK alleles from each clone (Figure 1—figure supplement 1A). In total, 58 of 58 alleles that we sequenced had mutations at the locus targeted by the guide RNA, verifying on-target CRISPR cutting. DLD1 is a diploid cancer cell line with two copies of MELK, and our sequencing indicated that one MELK-KO clone has a homozygous 10bp deletion in MELK, while the other clone has different indels in each allele.

A375 is an aneuploid cell line with three copies of MELK. Two findings from this clone are worth noting. First, in one clone, we recovered seven different indel mutations in the MELK gene. We hypothesize that at the time of single-cell sorting, one allele in this cell had acquired a small deletion that did not fully abolish gRNA recognition. Then, during clonal expansion, this allele underwent additional mutagenesis to generate the multiple large indels that we recovered. Secondly, in another A375 clone, we identified one allele that had three different single-nucleotide substitutions that generated three independent missense mutations (E15V, T16I, I17L). For our guide design, we followed the strategy of Shi and Vakoc (Nature Biotech, 2015), and chose gRNA sequences that target conserved, functional protein domains. The guide present in this clone targets the MELK ATP binding domain, likely explaining why these missense mutations are sufficient to destabilize the protein despite the lack of an indel.

To provide additional evidence that all of our MELK-knockout clones lack detectable MELK protein, we performed western blotting using a second antibody that recognizes a distinct MELK epitope. We observed no protein expression in any MELK-KO clone using antibodies that recognize either the MELK N-terminus or the MELK C-terminus (Figure 2—figure supplement 1B). In total, 100% of our topo-sequenced alleles harbor mutations in MELK, and western blotting with multiple antibodies failed to detect MELK, verifying that our MELK-KO clones lack wild-type MELK.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

The revised manuscript has been improved; however, the title, as written, implies that a new function of MELK has been revealed, and does not adequately describe the key conclusion. While the key conclusion is actually quite similar to that reflected in the title of your previous eLife article, it would be more appropriate to change the title to something along those lines.

We have changed our manuscript's title to “MELK expression correlates with tumor mitotic activity but is not required for cancer growth”.
