# Peer review - Round 1

Editors:
- Robert Waterhouse, Université Lausanne Switzerland
- Diethard Tautz, Max-Planck Institute for Evolutionary Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36495.175](https://doi.org/10.7554/eLife.36495.175)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Firefly genomes illuminate parallel origins of bioluminescence in beetles" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

General assessment:

The reviewers find the results presented in this manuscript compelling and generally comprehensively supported. The study's wide-ranging exploration of the evolution of bioluminescence within beetles brings together newly generated genomic, transcriptomic, and mass-spectrometry data for two firefly species and a click beetle. A key asset of this work is the integrated approach to exploring this evolutionary novelty, including discussion of which biochemical components may have been ancestral and predated independent acquisition of the associated traits required for the full manifestation of beetle bioluminescence.

Central conclusions:

1) By comparing the genomic regions that harbour the luciferase genes and reconstructing the full gene tree of the luciferases and homologous peroxisomal and non-peroxisomal fatty acyl-CoA synthetases (PACSs and ACSs) they present evidence that the firefly luciferases originated from an ancient duplication and subsequent neofunctionalisation of a PACS gene followed by a duplication of this ancestral luciferase to produce Luc1 (which remained in the same genomic neighbourhood) and Luc2 (which are elsewhere in the genomes). These analyses further suggest that the click-beetle luciferase arose from an independent duplication and subsequent neofunctionalisation of a PACS gene.

2) Complementary evolutionary analyses incorporating luciferases from several other species to perform ancestral state reconstructions further support the conclusion that the firefly and click-beetle luciferases arose through independent gene duplication events. Furthermore, molecular adaptation analysis identified a 'burst' of diversification along the branch leading to the click-beetle luciferases, consistent with neofunctionalisation of an ancestral PACS gene to acquire luciferase activity.

3) Transcriptomic analyses in the fireflies identified putative enzymes involved in the metabolism required to support bioluminescence, as well as non-enzymes that may also be important.

4) Assessing presence of lucibufagins (unpalatable defence steroids) in the three species suggests that they are only present in P. pyralis. The authors hypothesize that an expansion through multiple gene duplications of a cytochrome P450 gene (CYP303) in P. pyralis, but which remains as a single-copy gene in other species, may be linked to lucibufagin metabolism. This interestingly suggests that producing lucibufagins as a defence could in fact be a derived feature in Lampyrinae.

5) Overall, the conclusion that bioluminescence was independently acquired in the firefly and click beetle lineages is convincingly supported by phylogenetic, syntenic, and previous (anatomical) results.

6) Characterisation of the holobiomes of the three species and identified putative symbionts, a parasitoid fly, as well as bacteria and viruses.

Essential revisions:

1) Orthology analyses

Concerns were raised regarding the possibility that gene sets were not first filtered to select one protein per gene. If this is the case then these analyses will need to be performed on filtered gene sets and all downstream analyses that employ the orthology results will need to be updated, with conclusions revised accordingly.

2) Quality assessments

The assessments are comprehensive, although a few details need to be checked (see below), but concluding that all three genomes and the annotations are 'high-quality' is misleading. The best assembly (P. pyralis) likely contains non-collapsed haplotypes while I. luminosus remains fragmented (~90K scaffolds), and the annotated gene sets appear to be less complete than the assemblies suggest they should be. Reassurances of manual curation supporting analyses of specific gene families (e.g. the ACTSs, PACSs, P450s and DNMTs) should therefore be clearly presented.

3) Molecular adaptation analyses

Several points were raised regarding these analyses and the results (see below for details). (i) presenting results only for the Elateridae leads to the assumption that no positive results were found for the Lampyridae, but this is not discussed at all. (ii) reporting of some of the results leads to some confusion, e.g. the employed p-value cut-off and very high omega values. The results also leave at least two of the reviewers wondering about whether any specific sequence changes could be identified that might be linked to acquiring luciferase activity.

4) The 'contentious' hypothesis

Given that several recent studies are cited that have already lent support to the hypothesis on the independent origins of bioluminescence in beetles, including a 2016 paper from the same first author, emphasising the claimed 'contention' is unnecessary.

5) Repeat annotation

The main text only discusses repeats in P. pyralis, but does not consider if the repeat content could have been inflated by the inclusion of haplotypes in the assembly. A complex repeat in I. luminosus is discussed in the supplement, but how it relates to reconstructing the luciferase/ACSs/PACSs locus is ignored in the main text. It remains unclear whether the repeat annotations offer any insights into the rearrangement histories of these loci in the three beetle genomes.

The full reviews are appended below but you need only consider the summary and essential points above.

Reviewer #1:

Fallon et al. present their findings from comparative genomic analyses that focus on elucidating the origins of bioluminescence in beetles. They generate genome assemblies with hybrid approaches using multiple technologies for two fireflies and one click-beetle: a high-quality assembly with linkage group assignments for P. pyralis, a good-quality assembly for A. lateralis, and a fragmented but still relatively decent assembly for the click beetle, I. luminosus.

1) The fact that, for all three beetle species, the BUSCO completeness scores of the annotated gene sets are lower than for the assembly assessments suggests that despite the seemingly well-designed annotation strategies, they have failed to produce the best-quality automated annotations for these assemblies. As annotation pipelines employ a lot more evidence than BUSCO (which just uses profiles with Augustus), they generally produce gene set annotations that score better, or as good as, assessing the assemblies directly e.g. in Appendix 4—table 3 Dmela from 99.4% to 99.8%, Tcast from 98.4% to 99.0%. Having said that, the gene set completeness is still fairly good, and the main focus of the study is only on a limited set of genes, where manual curation was performed, so this should not substantially affect the main conclusions but should probably nonetheless be noted.

2) Labelling all three as 'high-quality genomes' is perhaps a bit of a stretch.

3) The very high levels of duplicated BUSCOs in the gene sets of Dmela and a Tcast in Appendix 4—table 3 seem to suggest that alternative transcripts were not first filtered from the gene sets. To obtain reliable estimates of real gene duplications the annotations must be first filtered to select one protein representative per gene. The other species may be less affected by this as they probably do not have many alternative transcripts annotated (a problem also for orthology analysis, see below). This needs to be fixed to ensure that conclusions about levels of gene duplication are based on sound and like-for-like analyses.

4) Figure 2F. The BUSCO C and D percentages do not seem to match those presented in the supplement, 93.7% vs. 94.8% and 1.3% vs. 1.4%.

5) The numbers presented as part of the orthology analyses are confusing. For example, Total numbers per species in Figure 2E do not match those reported in the text (numbers in the text are much higher). This might be explained if the figure only shows clustered genes (rather than all genes), but if so then this is not very well explained and hence the confusion. Much more worrying is the total gene count in Figure 2E for Drosophila melanogaster, 16991 genes – how can this possibly be when the current annotation at FlyBase has only 13931 protein-coding genes? Appendix 4—figure 8 gives a clue as to how this could be, as it shows 8 isoforms (alternative transcripts) of a single D. melanogaster gene. This would suggest that orthology clustering did not first select one protein per gene, a procedure that is more-or-less standard for most orthology delineation approaches. I am not familiar with the inner-workings of OrthoFinder, so perhaps the already-delineated clusters can be filtered to remove alternative transcripts, but I suspect it would be more rigorous to re-do the clustering using pre-filtered gene sets.

6) Figure 3D. I could not find mention of the sizes of the regions not shown for Ppyr1.3 LG1. The first one you can work out must span from 28400 to 30700 (so 2300), the second from after 30800 to before 67450 (so a bit less than 36650). Given the size, especially of the second one, it would be fairer to the reader to explicitly label these, and probably also to enumerate the number of genes in these regions.

7) Figure 3. The density of the figure makes it rather hard to figure out, but could it be that the orientation of PpyrMGST is inverted in 3B compared to 3D? Also, could there be a PACS missing in 3B for A. lateralis?

8) Figure 4B. I must preface these next few comments with the fact that I am familiar with PAML's codeml approaches but not with HyPhy's aBSREL approach. I tried to read up on aBSREL but could not easily find good documentation on how to interpret the results. The main reason I was confused is that I don't know how to interpret an omega value of 147.67 labelled on the branch to LlumLuc+PjanLuc [after writing that and then looking at the actual aBSREL tree I realised that this label is in fact referring to the blue star branch – so if I misread that then others might too]. Although this node is not the main result, such a high omega value seems strange (if indeed omega represents dN/dS here) as it implies estimates along that branch of ~150 times more non-synonymous changes than synonymous changes. I'm guessing that with few sites (1.53%) it can send the ratio sky-high. In which case, is it even meaningful to report this value on the figure? Indeed it seems aBSREL results on github and in the aBSREL paper they usually show nothing higher than omega=10.

9) While familiarising myself with aBSREL I noted in the 2015 paper that it states "over 80% of branches in typical gene phylogenies can be adequately modeled with a single ω ratio model". The aBSREL analysis of the Elateridae luciferases and PACSs identified 20 branches with two rate classes and 17 with one – so is this gene tree particularly atypical? Or is there something else happening here?

10) Figure 4B. A second question that immediately sprang to mind – how do these results compare with similar tests using PAML instead? For example, PMID:28094282 reports results from both approaches for neofunctionalisation of Caf1-55 after duplication. Confirmation of this kind, even just in the supplement, would help to reassure those, like me, who are still relatively new to aBSREL. I was unable to access the files on FigShare so I could not take a look at the data myself – since writing that I now have access. This however added to my confusion somewhat: Figure 4 legend states that there were 3 branches with significant (p<0.001) evidence of positive selection, but the aBSREL_stout_results.txt file reports only one (PangLucV) with p<0.001.

11) Another question that Figure 4 raises is why the molecular adaptation analysis was only performed on the Elateridae (plus PpyrLuc1 as outgroup)? Does it mean that the rest of the tree showed no signals of episodic positive selection, or that this was not examined? Or was there some technical reason why this was not performed, e.g. too many branches to test? Even if the tests fail to identify any significant signals of episodic positive selection, would it not be intriguing to examine amino acids in the alignment that are common to all/most luciferases but not amongst the PACSs/ACSs – i.e. have the two neofunctionalisation events converged on a common or slightly different molecular solution to luciferase activity? What do residues previously linked to the active site or cleft look like? Do site tests (rather than branch tests) pick up any of these potentially interesting amino acid positions?

12) Definition of subfunctionalisation. I am personally not overly put off by the use of subfunctionalisation to describe the differentiation of firefly Luc1 and Luc2. Nevertheless, in some circles (and perhaps more so when discussing enzymes in particular) subfunctionalisation would more strictly refer to an ancestral function being partitioned between the duplicates – i.e. the ancestral function can now only be performed through both extant copies working to together. In this case the ancestral (molecular) function is luciferase activity, and the (molecular) functions of Luc1 and Luc2 are still both luciferase activity. What distinguishes them is where and when they are expressed – i.e. divergence of function between the two copies is in terms of expression rather than molecular function. Clarifying this, or avoiding using subfunctionalisation at all, would therefore perhaps be advisable.

13) Long-read sequence assembly of the firefly Pyrocoelia pectoralis genome. Fu et al., 2017. This very recent data publication offers the opportunity to at least examine the Luc1 locus in a second Lampyridae.

The level of detail provided in the supplement is overwhelming for a reviewer (I did not read all 140 pages), but at the same time it is very much appreciated as it clearly documents detailed background information and methods. I wish more manuscripts were this well supported with such detailed supplementary materials. Subsection “Opsin analysis” still has MS Word comments.

Finally, the characterisation the holobiomes of the three species and identify putative symbionts, a parasitoid fly, as well as bacteria and viruses: this is encouraging to see, as (a) it suggests contaminant screening was comprehensive, and (b) 'contaminants' can actually be very interesting!

Reviewer #2:

In this manuscript, Fallon et al. explore the evolution of bioluminescence within the beetles, focusing on newly generated genomic and transcriptomic data for two distantly related species of firefly in comparison with a bioluminescent click beetle. This work is very comprehensive, incorporating a variety of sequencing methods to generate decent to high quality genome assemblies, supported by empirical data ranging from tissue-specific RNA-seq and bisulfite sequencing to mass-spec and holobiont analyses. The conclusion that bioluminescence was independently acquired in the firefly and click beetle lineages is convincingly supported by phylogenetic, syntenic, and previous (anatomical) results. A key asset of this work is the integrated approach to exploring this evolutionary novelty, including discussion of which biochemical components may have been ancestral and predated independent acquisition of the associated subtraits required for the full manifestation of beetle bioluminescence. I also appreciated the efforts taken in assessing synteny across fairly old lineages that have experienced a fair amount of gene shuffling. The extensive supplementary reports and files provide detailed documentation of the work. To strengthen this manuscript for publication, there are a few places where the analyses could be rounded out (particularly across the three species, to make the text less P. pyralis-centric), where the presentation of the material ought to be polished for clarity and to best reach a broader readership, and where a few (apparent) contradictions need to be reconciled.

Specific rounding-out analyses:

1) In support of the evolutionary scenario presented in Figure 3B and in light of the rather high repetitive content in P. pyralis (42.6%), do the authors detect any harbinger repetitive or transposable element sequences flanking either Luc1 or Luc2 in either P. pyralis or A. lateralis? Here and elsewhere, please make cross-species assessments more accessible. While total repetitive content for P. pyralis is reported in the main text, it appears that the only way to determine this for A. lateralis and I. luminosus is by manually summing up the final columns of Appendix 2—table 2 and Appendix 3—table 3 deep within the supplement.

2) As the repetitive content of P. pyralis may be inflated due to heterozygosity (suggested by the BUSCO duplicates), is it possible to add a filtering step or otherwise take levels of heterozygosity into account so as to make a more accurate estimation of repeat load?

3) Given the branch lengths in Figure 3C, is Luc2 more slowly evolving/ conserved than Luc1? Please perform the same molecular adaptation analysis on firefly Luc1 and Luc2 as presented in Figure 4B for the click beetle lineage Luc genes.

4) Given the care with which P450 genes were identified and curated in P. pyralis, please provide documentation that ensures the same level of care was used in assessing P450s in the other two species, which is particularly important (a) to support the claim of a P. pyralis-specific expansion of the CYP303 family and (b) in light of the low-quality assembly of I. luminosus. Please also ensure that the relevant supplementary sections are indeed cited in the main text section on P450s. Lastly, how were pseudogenes determined?

5) Regarding the enzymatic (not "enzymological", Introduction, last paragraph) basis of bioluminescence, highly efficient enzymes with high protein stability need not also be highly expressed at the transcript level. The analysis presented in Figure 6 fruitfully considers four selection criteria for candidate genes, but the other three criteria alone, without high expression, are already informative. Removing the high expression criterion would ~double the number of potential candidate genes. Do the authors find any important candidates among this set? Although two expected candidate genes are confirmed in the current analysis, take care to avoid the impression of cherry picking in data presentation. Two genes comprise a rather small litmus test. Were other expected candidates not found?

6) In terms of both phylogeny and synteny, I do not find the designated Clade C (Figure 3C-D) well motivated as a distinct clade.

Aspects to restructure or clarify:

1) It is counterproductive and unnecessary to oversell the text. Citing Darwin three times throughout the manuscript (Introduction and Discussion) to highlight the historical interest in and speculation on independent origins of bioluminescence in beetles belies the unsupported claim in the Abstract that this is a "contentious" hypothesis. Indeed, several recent studies are cited that have already lent support to this hypothesis, including a 2016 paper from the same first author. Similarly, the superlative claims in the first paragraph about the interest and importance of firefly bioluminescence are doubtful in comparison with GFP from jellyfish. A more consistent and milder tone would be helpful. With the data, the P. pyralis genome assembly is indeed high quality, but while the A. lateralis assembly is good, it is not as good and certainly not on par with that of Tribolium castaneum (subsection “Sequencing and assembly yield high-quality genomes”, second paragraph, based on scaffold number and NG50 statistics in Figure 2F). The orthogroup analysis in Figure 1E does not show a striking difference in number of shared OGs among the two fireflies compared to among all three species or pairwise between either firefly and the click beetle, although there is a high number of click beetle-specific OGs.

2) Although individual figure panels are generally quite nice, the organization of the figures is incredibly poor. As near as I can see, the main text refers to material in the sequence 1A, C, B, 2F, E, A, B, D, C, 3C, A, D, B, 4, 6 before 5, then 5B, A, C, D. Reorder appropriately, and consider whether 3A truly is germane to that section of the manuscript. Similarly, the care in depicting the PTS1 motif in Figure 3 is only finally explained much later in the main text (subsection “Metabolic adaptation of the firefly lantern”, second paragraph). I also found the figures very dense, visually, with insufficient white space between panels and with some elements too small even when viewed digitally at >2x print size. For example, the arrowhead to the click beetle organs in 1C is too small and by physically touching what it is pointing to obscures rather than highlights. It took several passes before I found the Ppyr LG1 label above the schematic in 3D, and I initially mistook the quotation marks in the Figure 6 table to mean omissions rather than "ditto".

3) I found the extent to which the reader is continually referred to the supplement, without any main text Materials and methods section, very frustrating. Judicious inclusion in the main text of key specifics would be helpful, including: specifying that the sex determination system is XO (subsection “Sequencing and assembly yield high-quality genomes”, third paragraph), that the "targeted molecular evolution analysis" uses a specific, citable pipeline (Mesquite, suppl. reference 213, for main text subsection “Independent origins of firefly and click beetle luciferase”, last paragraph), whether the entire protein (or gene locus?) is considered in the molecular adaptation analysis, which non-luminescent tissues were used (subsection “Metabolic adaptation of the firefly lantern”, first paragraph), which BUSCO version/ taxonomic group/ number of genes was used (Figure 2 legend), etc.

4) Although extensive and well structured, please polish the supplement. For example, remove lingering track changes/comments, cross-reference across sections as appropriate (e.g., for P450s per species and in comparative analyses), and ensure that information is clearly presented. For example, the main text is vague on the nature of the non-bioluminescent tissues used for the DE analysis, yet the list of libraries in Appendix 1—table 1 is based on opaque internal identifiers ("OAG"?) that make it difficult to ascertain either tissue type or number of biological replicates. Similarly, although I appreciate the detail presented on gene structure in Appendix 4—figure 4, *'s or other annotations to highlight identities would make the alignment easier to assess.

5) Throughout, consider a broad readership and avoid ambiguous jargon. I am still uncertain how "evolutionary events" fit into the Hi-C "long-range" analysis (subsection “Sequencing and assembly yield high-quality genomes”). The intended meanings of the term "promiscuous" (Discussion) are unclear. If a single enzyme can process multiple substrates (functionally promiscuous), how does this equate with a "need" for duplication and subfunctionalization for high specificity? That there are multiple synthesis possibilities to produce luciferin is not "promiscuous". In the legend for Figure 3, "Color gradients indicate the TPM values of whole body" is not nearly as accessible to a non-bioinformatician interested in beetle evolution as "Color gradients denote gene expression levels (TPM) from whole-body samples…". And similar instances (e.g., define BSN-TPM in the legend to Figure 6)…

6) Although the first Results section is appropriately concise as a foundation for the subsequent sections, the paragraph breaks and text flow within this wide-ranging section are difficult to follow and would benefit from smoothing and textual transitions.

7) Please make clear whether the genome assembly or OGS was used for specific analyses (e.g., subsection “The genomic context of firefly luciferase evolution”, first and second paragraphs). Was there really a de novo scan of the assembly itself?

8) Not all PACS/ ACS genes included in the phylogeny in 3C are shown in 3D. Please comment on the gene nomenclature and numbering conventions used for the taxa presented here, and whether genes not depicted in 3D are scattered in the genome.

9) The comment about potential lysosomes and the biological significance of an opsin gene being expressed within the light organ itself are unclear (“Metabolic adaptation of the firefly lantern”, last paragraph).

10) New genomes are continuously forthcoming. Provide a reference for the 62 referred to in the last paragraph of the subsection “Genomic insights into firefly chemical defense”.

11) It would be interesting and helpful for the authors to slightly expand the discussion on the possible link between bioluminescence and lucibufagin evolution. Is this a belt and braces situation of being doubly sure between CYP303 expansion and the whole body glow afforded by Luc2?

12) T. castaneum is a long established insect species for genetics and genomics and would be the more taxonomically appropriate outgroup for the four-species orthogroup analysis shown in main text Figure 2E.

Issues to reconcile:

1) Given the availability of fresh A. lateralis material for applications such as RNA-seq, I find it weak that the flow cytometry measurements for this species are based on only a single biological specimen.

2) If PACS genes gave rise to firefly luciferase genes (Figure 3B), why is the opposite evolutionary direction assumed for IlumLuc (subsection “Independent origins of firefly and click beetle luciferase”, first paragraph)?

3) What is the evidence that IlumLuc is highly expressed in the abdominal lanterns (subsection “Independent origins of firefly and click beetle luciferase”, first paragraph) if the RNA-seq sample is only based on the prothorax (legend for Figure 3C)?

I provided extensive, specific details above, but an overall concern is presentation, especially figures that are too dense and with poorly ordered and possibly irrelevant material.

Reviewer #3:

The manuscript, entitled "Firefly genomes illuminate parallel origins of bioluminescence in beetles," presents a comparative genomics analysis (with supporting data) of the evolution of bioluminescence in beetles. Focal firefly taxa in two lineages (Lampyridae subfamilies Lampyrinae and Luciolinae) are examined, as well as a bioluminescent click beetle (family Elateridae). The analysis is novel in providing strong genetic evidence supporting the independent evolution of bioluminescent light organs in Lampyrid and Elaterid beetles, as well as new insights into the origin of luciferase enzymes and the light organ itself. High quality draft genomes are provided, as well as supporting data (chromatin analysis, transcriptomic data, structural comparisons), to underpin the manuscript. Additionally, the authors investigate aspects of chemical defense in these beetles related to the lucibufagin steroid family, using mass spec of different tissues and life stages. The data suggests that only some lineages possess this defense chemistry, and the biosynthesis may be generated using a unique subfamily of cytochrome P450 genes. This P450 group (CYP303) is uniquely expanded in the Lampyrinae firefly subfamily. Finally, the authors examine evidence for symbionts, finding a Tenericutes mollicute might play an important role in firefly metabolism.

The manuscript is well written and carefully composed, with strong supporting evidence for the majority of analyses. It addresses a fascinating question, the molecular and evolutionary origin of bioluminescence, while also developing important resources for comparative genomics (that will likely benefit a broader research community). In addition, the supporting experiments involving mass spec, RNAseq, and chromatin analysis provide a richer foundation of knowledge than many genome papers achieve. My general view is that this is a significant publication that merits acceptance in eLife.

Some (hopefully constructive) criticisms are as follows.

Different genome sequencing methods were used to construct the data for this project, resulting in unequal assembly quality. This possibly impacts the analysis of parallel evolution in the luciferase homology gene family (based on protein blast), as incorrectly assembled or missing data might bias results in the more limited reference genome of the elaterid. An alternative approach to searching for these genes might be undertaken to help confirm these results, i.e. PCR or the use of ATRAM using the raw reads (https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-015-0515-2)

Some aspects of the figures seem uninformative (at least to the content of this paper). In Figure 1, the geographical distribution and sampling of P. pyralis is shown. This could be moved to the supplement, as it has minimal bearing on the paper as a whole. In Figure 2, much of the content seems better for supplement. I liked Figure 3 (very dense information though), and also wondered if a model of the evolution of the lantern from a peroxisome might want a cartoon figure.

Figure 4B. The large values of omega emerge as a result of a lack of synonymous sites (no synonymous sites lead omega to be infinity). Y. Ziheng suggests reporting likelihood ratio test statistics as being more informative.

Reviewer #4:

This study analyses the genomes of two fireflies and a click beetle to investigate the origins of bioluminescence. The authors offer convincing evidence for two independent origins thus showing that bioluminescence most likely evolved convergently in fireflies and click beetles. This manuscript is well written and the study provides many novel and interesting findings. I have a few specific comments.

Subsection “Independent origins of firefly and click beetle luciferase”, last paragraph and Figure 4B: Why is the analysis of molecular evolution only carried out on click beetle luciferase and not also on the fireflies?

Furthermore, is it possible to identify the specific adaptive mutations? Are homologous positions evolving adaptively in both suspected origins of luciferase or at least within the same domain/structure? Structuring of supplementary information and its referencing within the manual need to be improved.

Overall, I was very pleased with the quality of figures and the density of information they convey. However, several points concerning their arrangement, ordering, relevance, etc.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Firefly genomes illuminate parallel origins of bioluminescence in beetles" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz (Senior Editor), a Reviewing Editor, and four reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Thank you for the detailed responses to the queries raised by the four reviewers and your efforts to address them in the main text and supplementary information. For the most part the reviewers are generally pleased with the updates, clarifications, etc. and feel that the manuscript is much improved. As the feedback is mostly positive, I have not requested a formal second round of reviews, but instead have consulted the reviewers to compile the following list of issues which we feel were not completely addressed through your revisions or that require some further clarifications.

1) Orthology analyses

The filtering of isoforms prior to orthology analyses is rather convoluted, the standard practice (as indicated on the OrthoFinder GitHub page) is to select the longest transcript (coding sequence) per gene (unless some other evidence supports selecting a canonical transcript). Nevertheless, the applied strategy has removed many alternative transcripts, and it is clearly indicated in the legend, and properly detailed (with scripts) in the supplement, and this issue mainly affects Tribolium and Drosophila, and Drosophila is no longer shown in Figure 2E (only the most observant reader would find Appendix 4—figure 1 with 15'152 genes for Drosophila when in fact it has only 13'931), so it is acceptable, albeit imprecise. Please ensure that any result that relies on or makes reference to Drosophila or Tribolium orthologues (e.g. gene trees) are checked to make sure they are not impacted by the erroneous inclusion of alternative transcripts.

2) BUSCO results

Lower geneset than genome BUSCO completeness: please add a qualifier P5L116, along the lines of – Higher BUSCO completeness of the assemblies compared to the genesets suggests that future curation efforts will lead to improved annotation completeness.

3) Molecular adaptation analyses

If we understand correctly, MEME was used only to test the branch leading to EAncLuc – so what about PmeLucV and PangLucV branches? If we understand correctly, PAML was used to test all three of these branches, but in the supplement we see results from only one background vs. foreground test, so this leaves us confused. Essentially – did the complementary tests confirm all three branches identified with aBSREL or not? Given the very high omega values for PmeLucV and PangLucV branches, and the low proportions of sites, are these perhaps not trustworthy anyway? We would be more inclined to dismiss these as unreliable rather than explain them by evoking sexual selection.

4) semi-redundant legends in Figure 4A

In the figure itself it is not immediately clear that the bottom left legend refers to inferred states of branches and nodes while the boxed legend next to the Elateridae refers to the observed states of extant species. Please make this difference clear.

5) Figure 3a) Please check the Ppyr scale and labels, going by the scale bar the distance between tick marks 28,000 and 28,350 should correspond to 50 Kbp – yes?

b) "whether genes not depicted in 3D are scattered in the genome"

We feel that the description in the legend could be more precise. Specifically "About ten PACS and ACS genes flank the Luc1 gene in both firefly genomes." E.g. something like the following (but please check details): Nine of the 12 A. lateralis PACS/ACS genes flank AlatLuc1 on scaffold 228, while four of the 11 P. pyralis PACS/ACS genes are neighbours of PpyrLuc1 on LG1 with a further six 2.4 Mbp and 39.1 Mbp downstream.

c) Reviewer.1 – "Given the size, especially of the second one, it would be fairer to the reader to explicitly label these, and probably also to enumerate the number of genes in these regions." We feel it is important to state how many genes are in these not-shown regions (labelled 2.4 Mbp and 36.7 Mbp) because if they are packed with other genes it hints at more shuffling while if just 'expanded' with inserted TEs then the synteny with Alat seems more confident.
