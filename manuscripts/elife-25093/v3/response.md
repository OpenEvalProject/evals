# Author response - Round 1

Authors:
- Aashiq H Kachroo ([ORCID: 0000-0001-9770-778X](https://orcid.org/0000-0001-9770-778X))
- Jon M Laurent ([ORCID: 0000-0001-6583-4741](https://orcid.org/0000-0001-6583-4741))
- Azat Akhmetov
- Madelyn Szilagyi-Jones
- Claire D McWhite ([ORCID: 0000-0001-7346-3047](https://orcid.org/0000-0001-7346-3047))
- Alice Zhao
- Edward M Marcotte ([ORCID: 0000-0001-8808-180X](https://orcid.org/0000-0001-8808-180X))

## Response text

DOI: [10.7554/eLife.25093.026](https://doi.org/10.7554/eLife.25093.026)

Reviewer #1:

[…] 1) The authors do a very poor job of describing the basis for choosing and refining the 60 coli genes. It is really hard to believe that there are only 60 good orthologs between yeast and E. coli. What exactly were the criteria for choosing those? Further, they did not indicate what possibly was the issue with the 9/60 that did not have a complementation assay. Was it a problem with the corresponding yeast host strain(s) or was it difficult to clone these genes? This should be spelled out, perhaps as an explicit description in the Materials and methods section. Complete tables of all orthologs attempted for all the donor species tested, along with reasons for failure for the 9 that missed in bacteria for example, should be provided in the supplement.

To obtain clear loss-of-function phenotypes, we chose all E. coli orthologs of essential yeast genes with no lineage specific duplications (i.e., only 1:1 orthologs). Though in total there are 460 shared orthogroups between E. coli and yeast (as per InParanoid 8), only 58 fit the criteria of 1) yeast essentiality and 2) 1:1 orthology. We have now clarified this process in the text and in the Materials and methods section, and corrected a typo in the prior Figure 1A(60 vs. 58). As now described in the text (subsection “Many E. coli genes successfully complement lethal defects in their yeast orthologs”, first paragraph; subsection “Ortholog inference”), we used Inparanoid 8 to identify the 58 E. coli genes that are 1:1 orthologs of essential yeast genes. We cloned and confirmed the sequence of all 58 of these E. coli genes in yeast expression vectors. Of these, 51 provided informative assays, 5 were inconclusive, and 2 had no matched yeast strains available to test replaceability. We have modified the Supplementary file 1appropriately.

2) From what I could conclude, in both bacteria and Arabidopsis there was an issue with complementing Sc-hem12. The bacteria one could not be integrated and both Arabidopsis orthologs failed to complement. What is the issue with Hem12? How come the human ortholog Hs-UROD did complement? Even if there is no single clear answer to these questions a hypothesis would be welcome.

Our observations were that the bacterial ortholog (Ec-hemE) of Sc-HEM12 functionally replaced only when constitutively expressed under the GPD promoter. Human Hs-UROD also replaced when so expressed. However, plant versions did not work when constitutively expressed on plasmids. Thus, to address the issue of why we observed differential replaceability across variants of this gene, we performed the following analyses:

A) In the case of the Ec-HemE bacterial replacement at the yeast genomic locus, we suspect that the reason for not obtaining a replacement is that we used only 60bp of sequence homology to the flanking yeast locus, limiting the efficiency of the homologous repair. However, it is still possible that the bacterial version at the yeast native locus does not replace the yeast gene function, explaining the lack of positive clones. We did not pursue this particular case in more depth.

B) The human Hs-UROD version available in the human ORFeome had a single mutation resulting in a single amino acid change G303V. This variant is non-replaceable as explained in the text (subsection “Each yeast heme biosynthesis enzyme can be replaced by its human ortholog”, first paragraph). Reverting this mutation back to wild type (encoding glycine) allowed successful replacement of the yeast gene (Figure 6—figure supplement 3C).

C) The plant co-orthologs of the yeast gene Sc-Hem12 (AtHEME1/E2) did not replace the yeast gene when expressed under the control of the GPD promoter. In response to the referee’s queries, we have now tested and eliminated two possible reasons for this lack of replacement:

i) Plant heme pathway proteins possess chloroplast localization signals (CLS) at their N-termini, and we showed two cases where GFP-tagged plant proteins localize to mitochondria in yeast (At-PPOX1 and At-FC-I). However, the Sc- Hem12 reactions take place in the cytosol. We therefore first suspected mislocalization to the mitochondria to be the likely reason for non-replaceability. We have now tested whether the removal of the At-HEME1 or AtHEME2 CLS would allow functional replacement; however, this was unsuccessful (Figure 6—figure supplement 1B’’’). We also tested At-HEMC, an initially poor replacer. For this gene, removal of the CLS significantly enhanced replaceability compared to the wild type protein (Figure 6—figure supplement 1B’’), demonstrating that the CLS did indeed contribute to non-replaceability in some cases.

ii) We next suspected functional divergence or sub-functionalization as a potential contributor to the lack of complementation. We co-expressed both paralogs (testing both the wild type and CLS-less versions) under the control of a GPD promoter on two different plasmids with different selections for transformation (SD-Ura and Hygromycin). Co-expression of both genes in the same strain failed to functionally replace the yeast gene function (Figure 6—figure supplement 1B’’’), ruling out sub-functionalization as a likely reason for the failure to complement.

We speculate that there could be several other reasons why complementation failed, including unknown intermediate reactions, required localization in a special compartment (e.g. chloroplast) or different transcriptional/translational regulation in plants that might contribute to the lack of functional replaceability.

We have incorporated the new data into the manuscript, and indicate (subsection “Most yeast heme biosynthesis enzymes can also be successfully plant-ized”, last paragraph) that we tested multiple hypotheses to attempt to explain these trends.

3) For the hemH pink phenotype, to show that this is actually due to the specific substrate proposed, they should delete Sc-HEM14 (or another upstream function) to genetically verify that the pink phenotype disappears because formation of protoprophyrin IX should be prevented by this "upstream" mutation.

We have now performed additional experiments to confirm our hypothesis regarding protoporphyrin IX accumulation. Using CRISPR, we deleted the Sc-HEM14 ORF in wild type BY4741, Sc-hem15Δ::Ec-HemH,and Sc-hem15Δ::Ec-MLS-HemHstrains. Consistent with protoporphyrin IX being the pink pigment in the Sc-hem15Δ::Ec-HemHstrain, the Sc- hem15Δ::Ec-HemH hem14Δ strain lost the pink phenotype, even after growing for 6 days.

Moreover, we observed that all strains carrying the hem14Δ allele were in fact significantly paler than even wild type BY4741 cells, presumably reflecting extensive protoporphyrin IX depletion in these cells. These data are now provided in Figure 5—figure supplement 2.

Reviewer #2:

[…] Apart from the general point above, the main interest of this work lies in the analysis of various predictors and correlates of ortholog replaceability. I do not share the authors' surprise regarding the lack of correlation between replaceability and sequence conservation. It has been shown in a number of analyses that there is at best a very limited connection between sequence conservation and gene essentiality (Jordan IK, Rogozin IB, Wolf YI, Koonin EV. Essential genes are more evolutionarily conserved than are nonessential genes in bacteria. Genome Res. 2002 Jun;12(6):962-8; Wang Z, Zhang J. Why is the correlation between gene importance and gene evolutionary rate so weak? PLoS Genet. 2009 Jan;5(1):e1000329). I think we see here a manifestation of the same phenomenon: sequence conservation depends much stronger on the abundance of a protein product and the gene-specific functional constraints than on the "importance".

The shape of the dependency in Figure 3B seems paradoxical at first glance (non-monotonic curve, with moderately conserved genes being most replaceable) but I suspect is explained by the different in replaceability among functional classes of genes (Figure 3C). I find it highly desirable to test this directly and discuss accordingly.

Though the majority of the proteins tested had moderate sequence conservation, we saw no particular relationship between sequence conservation and functional replaceability. We now expand on this point and have incorporated the citations mentioned by the referee in the subsection “Conclusions” (first paragraph). We additionally tested for the enrichment of particular GO Biological Process categories within each bin of sequence identity from Figure 3B. Those genes in the 40-50% category had an enrichment in glucose metabolism (3 of the 7 genes). Other than that bin, no other category had any significant enrichment in biological processes or KEGG pathways. We now discuss this point specifically in the first paragraph of the subsection “Replaceability varies strongly across different biological processes”.

To me, the results in Figure 3C are indeed the most interesting in the paper. Again, this looks striking and at least superficially, paradoxical, in that genes in the most highly conserved categories, such as translation and tRNA modification, are virtually non-replaceable. I believe the explanation lies in the complexity hypothesis (Jain R, Rivera MC, Lake JA. Horizontal gene transfer among genomes: the complexity hypothesis. Proc Natl Acad Sci U S A. 1999 Mar 30;96(7):3801-6) that seems to be the best explanation for the rates of horizontal gene transfer in different functional classes of prokaryotic genes. Indeed, ortholog replacement studied here can be considered an extreme, "forced" variant of horizontal gene transfer. I think a thoughtful discussion of these parallels and their utility for explaining the results could make the present story considerably more interesting.

Our results in Figure 3Cdo seem to agree with the complexity hypothesis, in that housekeeping genes are more likely to be replaceable while informational genes are not. We have added a short discussion of this topic in the subsection “Conclusions” (first paragraph).
