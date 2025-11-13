# The homophilic receptor PTPRK selectively dephosphorylates multiple junctional regulators to promote cell–cell adhesion

## Authors

- Gareth W Fearnley<sup>1</sup>
- Katherine A Young<sup>1</sup>
- James R Edgar<sup>1</sup> ([ORCID: 0000-0001-7903-8199](https://orcid.org/0000-0001-7903-8199))
- Robin Antrobus<sup>1</sup>
- Iain M Hay<sup>1</sup>
- Wei-Ching Liang<sup>3</sup>
- Nadia Martinez-Martin<sup>4</sup>
- WeiYu Lin<sup>3</sup>
- Janet E Deane<sup>1</sup> ([ORCID: 0000-0002-4863-0330](https://orcid.org/0000-0002-4863-0330))
- Hayley J Sharpe<sup>1</sup> ([ORCID: 0000-0002-4723-298X](https://orcid.org/0000-0002-4723-298X)) †

### Affiliations

1. Cambridge Institute for Medical Research University of Cambridge Cambridge United Kingdom
2. Department of Pathology University of Cambridge Cambridge United Kingdom
3. Antibody Engineering Department Genentech South San Francisco United States
4. Microchemistry, Proteomics and Lipidomics Department Genentech South San Francisco United States

† Corresponding author

## Abstract

Cell-cell communication in multicellular organisms depends on the dynamic and reversible phosphorylation of protein tyrosine residues. The receptor-linked protein tyrosine phosphatases (RPTPs) receive cues from the extracellular environment and are well placed to influence cell signaling. However, the direct events downstream of these receptors have been challenging to resolve. We report here that the homophilic receptor PTPRK is stabilized at cell-cell contacts in epithelial cells. By combining interaction studies, quantitative tyrosine phosphoproteomics, proximity labeling and dephosphorylation assays we identify high confidence PTPRK substrates. PTPRK directly and selectively dephosphorylates at least five substrates, including Afadin, PARD3 and δ-catenin family members, which are all important cell-cell adhesion regulators. In line with this, loss of PTPRK phosphatase activity leads to disrupted cell junctions and increased invasive characteristics. Thus, identifying PTPRK substrates provides insight into its downstream signaling and a potential molecular explanation for its proposed tumor suppressor function.

## Introduction

Multicellular organisms have evolved elaborate mechanisms of intercellular communication in order to organize cells into functioning tissues. The phosphorylation of protein tyrosine residues is an essential feature of cell-cell communication and effectively coordinates diverse cell behaviors such as cell adhesion and motility in response to external stimuli. Kinases and phosphatases dynamically regulate phosphotyrosine levels, such that cells are primed to acutely respond to developmental cues or changes to their local environment. In particular, enzyme-linked cell surface receptors transduce external signals to the cell interior. For example, receptor tyrosine kinases (RTKs) dimerize upon ligand binding leading to trans-autophosphorylation, which recruits phosphotyrosine-binding proteins that propagate a variety of signaling cascades (Hunter, 2009). Protein tyrosine phosphatases (PTPs) are often thought to function in terminating or thresholding such signals (Agazie and Hayman, 2003). However, it is increasingly apparent that phosphatases themselves can propagate signals in response to growth factors; with the best example being PTPN11/SHP2; a key therapeutic target in cancer (Brown and Cooper, 1996). Moreover, many human PTPs are receptor-linked suggesting they can also receive input from the extracellular environment. The effects of protein phosphorylation are site-specific, for example, phosphorylation of Src Tyr419 upregulates kinase activity but phosphorylation of Tyr530 reduces it (Mohebiany et al., 2013). Thus, both kinases and phosphatases can modulate signaling cascades to affect cell behaviors. Despite this, the roles and substrates of the classical PTP family remain comparatively understudied.

The receptor type PTPs (RPTPs) are type one transmembrane proteins subdivided according to their extracellular domain (ECD) features. Like RTKs, RPTPs link extracellular sensing to intracellular catalysis. The regulatory mechanisms for most of the 21 RPTPs encoded by the human genome are poorly characterized (Tonks, 2006); however, it is known that the R2B RPTP subfamily form homophilic interactions and have been proposed to respond to cell-cell contact (Aricescu et al., 2007). There are four human R2B receptors: PTPRK, PTPRM, PTPRT and PTPRU, which share a common domain architecture of one MAM (meprin/A5/μ), one immunoglobulin (Ig)-like and four fibronectin (FN) domains combined with an uncharacterized juxtamembrane domain and tandem intracellular phosphatase domains; the first active (D1) and the second inactive (D2) (Figure 1A). Structural and biophysical studies suggest the PTPRM extracellular domain forms a rigid, pH-dependent, homophilic interaction in trans through the MAM-and Ig domains of one molecule and the FN1 and FN2 domains of another molecule, with the possibility of further cis interactions (Aricescu et al., 2007). Several cell adhesion proteins, such as cadherins and catenins, are proposed substrates for PTPRM (Craig and Brady-Kalnay, 2015). Its paralog PTPRK was identified as a candidate driver gene in mouse intestinal tumorigenesis by insertional mutagenesis (March et al., 2011; Starr et al., 2009) and was more recently identified as a gene fusion partner with the oncogene RSPO3 in a subset of human colorectal cancers (Seshagiri et al., 2012). Furthermore, single nucleotide polymorphisms (SNPs) within the PTPRK genic region are associated with inflammatory bowel diseases (IBDs) and type I diabetes age of onset (Inshaw et al., 2018; Trynka et al., 2011). PTPRK is regulated by a proteolytic cascade involving furin, ADAM10 and γ-secretase (Anders et al., 2006) and might function to dephosphorylate proteins such as EGFR (Xu et al., 2005) or STAT3 (Chen et al., 2015). PTPRK mRNA is broadly expressed, except in immune cells, skeletal muscle and testes (Figure 1—figure supplement 1A), and is upregulated by transforming growth factor β (TGFβ) signaling (Wang et al., 2005). Despite its importance in disease and signaling, the events downstream of PTPRK are not well established.

![Figure 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig1-v1.jpg)

**Figure 1.:** (A) Schematic of full length PTPRK. The extracellular MAM, Ig and fibronectin domains mediate homophilic interactions. The intracellular domain comprises a juxtamembrane domain and two PTP domains; one active (D1) and one inactive (D2). (B) Structured illumination microscopy images of MCF10As immunostained for PTPRK (F4 clone; magenta) and E-Cadherin (green). Graphs indicate fluorescence intensity through the Z-axis in indicated boxed regions. Scale bars = 10 µm. (C) Fluorescence microscopy images from co-cultures of wildtype and nuclear mApple-expressing PTPRK knockout MCF10As that were immunostained for PTPRK (magenta) and E-Cadherin (green). Nuclei were stained with Hoechst (blue). mApple positive PTPRK KO cells are indicated by orange asterisks. Cell junctions where PTPRK is absent are highlighted by white arrows. Scale bars = 20 µm. (D) MCF10As were plated at indicated densities and analyzed by immunoblot after 3 days in culture. Arrows indicate full length (top) and furin-cleaved PTPRK (bottom). See also Figure 1—figure supplement 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) mRNA expression of R2B PTPs in Human tissues. Raw data obtained from Genotype-tissue expression portal (GTExportal.org; GTEx Consortium et al., 2015). (B) 15 rabbit monoclonal antibodies were screened for their ability to specifically detect PTPRK by immunoblot. Immunoblot analysis of lysates generated from HEK293 cells transiently transfected with HA-PTPRK or an siRNA pool targeting PTPRK mRNA. Left: The indicated Rabbit monoclonal antibodies detected bands at 215 kDa (full length PTPRK) and 95 kDa (Furin-cleaved PTPRK), which are depleted by siRNA and increased with PTPRK overexpression. This suggests the antibodies recognize epitopes C-terminal to the Furin-cleavage site. Right panel: immunoblot probed with a commercial mouse monoclonal antibody raised against a PTPRK extracellular fragment (Sc-374315). No bands corresponding to predicted sizes (Full length 215 kDa; Furin-cleaved extracellular fragment:~120 kDa.) or modulated by siRNA depletion or overexpression were observed. (C) PTPRK antibody recognition based on (B). (D) 15 monoclonal antibodies were screened for their ability to specifically detect PTPRK by immunofluorescence. Immunostaining of MCF10As transfected with a non-targeting or PTPRK siRNA using PTPRK rabbit monoclonal antibody clone 1 .F4 (Magenta). F-actin (green) and nuclei (blue) were stained with phalloidin and Hoechst, respectively. Scale bars = 50 µm. (E) MCF10As were transfected with plasmids for the expression of Cas9, eGFP and single guide RNAs targeting PTPRK exons 1 and 2. eGFP-positive cells were cloned and expanded. Lysates from three clones grown individually or pooled were analyzed by immunoblot. PTPRK was detected using a mix of 2 .G6, 2 .H4 and 4 .H5 monoclonal antibodies. (F) Quantitative PCR analysis of confluent MCF10A cDNA using the indicated probes. Ct values relative to the housekeeping gene RPL19 were normalized using 2-ΔCt. The means of technical duplicates are shown. (G) Summary of secreted protein microarray with two purified protein libraries representing more than 1500 genes (≈50% single transmembrane receptors and partial secreted factor coverage) against the recombinant Fc-tagged PTPRK extracellular domain. Each intersection plot represents two independent microarray screens and dots represent average scores for each protein in the library. The lower left square represents all non-hit proteins with a cut-off of 10. Data analysis for hit calling is described in the Materials and methods section.

Phosphatases present unique experimental challenges. For example, their signal, removal of phosphate, is inherently negative and means it is critical that they are studied in an appropriate context (Fahs et al., 2016). Given their homophilic interactions and subcellular localization, it is highly likely that the R2B family function at cell-cell contacts. We therefore reasoned that the appropriate context to assess their function would be in confluent, contact-inhibited epithelial monolayers. By combining proteomics approaches with in vitro and cell-based dephosphorylation assays we find that PTPRK displays striking substrate selectivity. In addition, there are distinct requirements for the two PTPRK intracellular phosphatase domains for substrate recognition. Multiple lines of evidence converge on five high confidence substrates: Afadin (AF6), PARD3 (Par3), p120Cat (p120-Catenin; CTNND1), PKP3 and PKP4 (p0071), which are known regulators of junctional organization. Indeed, PTPRK loss perturbs epithelial junction integrity and promotes invasive behaviors in spheroid cultures, consistent with its putative tumor suppressor role.

## Results

### PTPRK localizes to cell-cell contacts in epithelial cells

In order to detect endogenous PTPRK by immunoblot and immunofluorescence, we generated and characterized monoclonal antibodies against the purified PTPRK extracellular domain (ECD) (Figure 1—figure supplement 1B–D). Using one of our antibodies for structured illumination microscopy, we found PTPRK localized to puncta at basal cell-cell contacts that partially overlap with the adherens junction (AJ) protein E-Cadherin in MCF10A epithelial cells (Figure 1B). Homophilic interactions of the R2B receptor family have been demonstrated using suspension cell or bead aggregation assays (Brady-Kalnay et al., 1993; Gebbink et al., 1993; Sap et al., 1994; Zondag et al., 1995), and PTPRM-based structural and biophysical studies (Aricescu et al., 2006; Aricescu et al., 2007). To investigate homophilic PTPRK interactions in cells, we generated CRISPR/Cas9 PTPRK knockout (KO) MCF10A cells (Figure 1—figure supplement 1E), stably expressing nuclear mApple, and co-cultured them with unlabeled wildtype cells. By immunostaining, PTPRK is strikingly absent from cell-cell contacts between wildtype and adjacent KO cells, despite expression of other R2B receptors (Figure 1C and Figure 1—figure supplement 1F). Consistently, PTPRK protein levels increase with increasing cell density (Figure 1D). Finally, screening recombinant PTPRK ECD against a secreted protein microarray did not identify any additional ligands (Figure 1—figure supplement 1G). Thus, in combination, our data indicates homophilic trans-interactions stabilize PTPRK at cell-cell contacts in epithelial cells.

### The PTPRK interactome reveals associations with cell adhesion regulators

To understand the function of PTPRK at cell-cell contacts we aimed to identify its direct substrates. Previous studies have described PTP substrate-trapping mutations, which correspond to D1057A and C1089S for the longest isoform of human PTPRK (Flint et al., 1997). We purified bacterially-expressed, biotinylated PTPRK wildtype and substrate-trapping intracellular domains (ICDs), as well as the pseudophosphatase D2 domain, and coupled them to streptavidin beads (Figure 2—figure supplement 1A and B) for affinity purification followed by mass spectrometry (AP-MS). We confirmed that the wildtype ICD could potently dephosphorylate tyrosine phosphorylated peptides, whereas the substrate traps and D2 domain were inactive, even at high concentrations (Figure 2—figure supplement 1C). To generate cell lysates enriched with tyrosine phosphorylated proteins, confluent MCF10A cells were treated with pervanadate, an irreversible PTP inhibitor (Figure 2A; Huyer et al., 1997). Excess vanadate was chelated with EDTA and endogenous PTP active site cysteine residues were alkylated with iodoacetamide, which was quenched by DTT, as previously described (Blanchetot et al., 2005). We confirmed that the substrate-trapping mutants bound tyrosine phosphorylated proteins (Figure 2—figure supplement 1D). Next, proteins bound to PTPRK domains after pull downs were trypsinized and identified by mass spectrometry.

![Figure 2.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig2-v1.jpg)

**Figure 2.:** (A) Experimental schematic of PTPRK interactome and substrate trapping studies. DA = D1057A, CS = C1089S. (B–D) Statistically enriched (p<0.05, n = 4) proteins after pull downs from pervanadate treated MCF10A lysates are displayed on volcano plots comparing PTPRK-ICD to beads control (B), PTPRK-ICD-DA to PTPRK-ICD (C) and PTPRK-ICD-CS to PTPRK-ICD (D). (E) GO term analysis of proteins statistically enriched (p<0.05) on PTPRK-ICD domains using Metascape. (F–G) Selected PTPRK interactors identified by mass spectrometry were validated by immunoblot analysis. Input and supernatants reveal the extent of protein depletion by recombinant proteins. Arrow indicates relevant band. See also Figure 2—figure supplements 1, 2 and 3. (H) Confluent, pervanadate-treated MCF10A lysates were used for pull downs with PTPRK D1057A ICD. Where indicated, pull downs were incubated with and without 20 mM vanadate for 30 min. 4% inputs (I), 4% supernatants (S), 4% eluates (E; following vanadate treatment) and pull downs (P) were subjected to immunoblot analysis. (I) Confluent, pervanadate-treated MCF10A lysates were treated with or without CIP to remove protein phosphorylation and were used for pull downs with PTPRK C1089S ICD. 4% inputs (I), 4% supernatants (S) and pull downs (P) were subjected to immunoblot analysis.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) His- and Avi-tagged PTPRK domains were expressed in E. coli cultured in biotin-supplemented media and purified using Nickel-NTA beads, followed by size exclusion chromatography (SEC). DA = D1057A mutant. CS = C1089S mutant. (B) SEC-purified proteins bound to streptavidin resin were eluted and resolved by SDS-PAGE followed by Coomassie staining. In; input, B; beads. (C) The phosphatase activity of indicated amounts of purified proteins was assessed using the Biomol green assay with two tyrosine phosphorylated peptides as substrates and was quantified at 620 nm. (D) Recombinant proteins bound to streptavidin resin were used in pull down assays from pervanadate treated Hs27 fibroblast lysates. After extensive washing, bound proteins were eluted in sample buffer and analyzed by immunoblot.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A–C) Volcano plots showing statistically enriched (p<0.05, n = 3) proteins bound to the indicated recombinant proteins after pull downs from pervanadate-treated confluent Hs27 cell lysates comparing PTPRK-ICD to beads control (A), PTPRK-ICD-D1057A to PTPRK-ICD (B) and PTPRK-ICD-C1089S to PTPRK-ICD (C). Grey points that appear significant were consistently found on the beads-only control. (D) Comparison of proteins enriched on the PTPRK-ICD after pulldowns from MCF10A and Hs27 lysates. Protein lists were used as inputs for BioVenn (Hulsen et al., 2008). (E) Pull downs using PTPRK-ICD D1057A and PTPRK-D2 domains from confluent, pervanadate-treated MCF10A lysates were incubated with and without 20 mM vanadate for 30 min. 4% inputs (I), 4% supernatants (S), 4% eluates (E; following treatment) and pull downs (P) were subjected to immunoblot analysis.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) Volcano plot showing statistically enriched (p<0.05, n = 3) proteins bound to the indicated recombinant proteins after pull downs from pervanadate-treated confluent MCF10A cell lysates comparing PTPRK-D2 to beads control. (B) Comparison of proteins enriched on PTPRK-D2 and PTPRK-ICD domains after pulldowns from MCF10A lysates. Protein lists were used as inputs for BioVenn (Hulsen et al., 2008). (C) After size exclusion chromatography (SEC), purified protein was incubated with or without streptavidin and subjected to SDS PAGE followed by Coomassie staining to determine the extent of biotinylation. Arrows indicate the purified domains and the respective streptavidin-induced mobility shift. (D–E) PTPRK interactors identified by mass spectrometry were validated using pull downs with the specified PTPRK and PTPRM protein domains from pervanadate-treated, confluent MCF10A cell lysates followed by immunoblot analysis. Input and supernatants reveal the extent of protein depletion by recombinant proteins.

Sixty-four proteins were >2 fold enriched (p<0.05; n = 4) on the wildtype PTPRK-ICD (Figure 2B and Figure 2—source data 1 and 2). We also screened for interactors using pervanadate-treated Hs27 Human fibroblast lysates (n = 3); another cell line that undergoes contact inhibition of proliferation (Figure 2—figure supplement 2A–C). We found that only 21% of the PTPRK-ICD interactome overlapped between MCF10A and Hs27 cells (Figure 2—figure supplement 2D), which might reflect differences in protein expression or phosphorylation between the cell lines. The first substrate trap (D1057A) enriched the serine/threonine kinase MAP4K4 and RAPGEF6, which were both recently linked to Hippo signaling (Figure 2C and Figure 2—figure supplement 2B; Meng et al., 2018). FMRP and the cell junction associated proteins PARD3, Afadin (AF-6/MLLT4) and PLEKHA6 were enriched on the second substrate trap (C1089S; Figure 2D and Figure 2—figure supplement 2C). Gene ontology (GO) term analysis for the PTPRK interactome highlights the enrichment of cell junction proteins across all domains (Figure 2E).

We used pull downs followed by immunoblotting to confirm interactions with previously reported PTPRK interactors (MINK1, PKP4, DLG5 and PTPN14 [St-Denis et al., 2016]) as well as proteins bound to the PTPRK substrate traps in this study, including FMRP-interacting NUFIP2. RAPGEF6, MAP4K4 and PARD3 were reproducibly enriched on substrate traps (Figure 2F and G). We did not observe interactions with previously reported R2B receptor substrates including E-Cadherin, β-Catenin, STAT3, EGFR (pY1068) and Paxillin (DEPOD database; Duan et al., 2015) besides p120Cat (Zondag et al., 2000), which was enriched on the C1089S trap along with PKP4 and NUFIP2 (Figure 2G). The principle of substrate trapping necessitates a direct interaction mediated by phosphotyrosine (Flint et al., 1997). We tested whether trapped proteins could be competed off PTPRK-D1057A using the phosphate mimetic orthovanadate. The MAP4K4 interaction with PTPRK D1057A ICD from pervanadate lysates was competed using orthovanadate, consistent with phosphotyrosine-mediated trapping (Figure 2H and Figure 2—figure supplement 2E). In contrast, Afadin was not depleted by orthovanadate treatment. Furthermore, PARD3, PKP4 and p120Cat bind the C1089S ICD less effectively in the absence of phosphorylation, also supporting the efficacy of the trapping approach (Figure 2I). However, we noted that all substrate-trapped proteins could still interact with PTPRK domains in phosphatase-treated lysates (Figure 2H and I) and most interactors can bind to the enzymatically active WT ICD (Figure 2F and G), indicating phosphorylation-independent PTPRK interactions. Furthermore, the PTPRK-D2 domain alone was sufficient to pull down approximately a third of PTPRK ICD interactors (Figure 2—figure supplement 3A and B; Figure 2—source data 2). Although substrate trapping was effective, our data indicate that because many proteins can bind PTPRK independently of phosphorylation or to its D2 pseudophosphatase domain (Figure 2F and G), trapping approaches alone could miss potential substrates.

To investigate interaction specificity further, we purified the ICD of the paralogous receptor PTPRM, which is 75% identical to PTPRK at the amino acid level (Figure 2—figure supplement 3C). Afadin, RAPGEF6 and NUFIP2 interact specifically with PTPRK, indicated by their biased depletion from supernatants. Interestingly, we found several that bound both PTPRK and PTPRM ICDs such as PARD3 and PKP4. Although MAP4K4, MINK1, PTPN14, DLG5 and p120Cat are depleted by both ICDs, they appear to have a higher affinity for PTPRK in pull downs (Figure 2—figure supplement 3D and E). Overall, the PTPRK interactome is enriched with cell junction-related proteins and shows partial overlap with PTPRM. Together, these data suggest that PTPRK and PTPRM have both unique and redundant roles at cell junctions.

### The PTPRK dependent tyrosine phosphoproteome

Next, we reasoned that PTPRK deletion should result in the hyperphosphorylation of its substrates. To investigate this, we used quantitative tyrosine phosphoproteomics to compare wildtype and PTPRK KO MCF10A cells. We investigated the tyrosine phosphoproteome of confluent cells 24 hr post media change in order to observe residual phosphorylation, initially induced by EGF and/or serum growth factors. To this end, tyrosine phosphorylated peptides were enriched from trypsinized SILAC (stable isotopomeric versions of amino acids)-labeled wildtype and PTPRK KO MCF10A lysates using anti-pTyr Abs and biotin-tagged phosphotyrosine ‘superbinder’ mutant Src Homology 2 (SH2) domains (Tong et al., 2017) (Figure 3A and Figure 3—figure supplement 1A). We identified 282 quantifiable phosphotyrosine sites on 185 proteins (Figure 3—source data 1) from three experiments. Interestingly, 15 phosphosites were statistically upregulated in PTPRK KO cells compared to wildtype in at least two experiments, but only one site, in PAG1, was down regulated (Figure 3B). Strikingly, Afadin, PARD3 and PLEKHA6, which were all ‘substrate-trapped’ by PTPRK-C1089S, were amongst the proteins possessing enriched phosphosites in PTPRK KO cells (Figure 3B). Moreover, we identified upregulated phosphorylation in at least one experiment for p120Cat, PKP2, PKP3 and PKP4, which are δ-catenin family proteins and interact with the PTPRK ICD (Figure 3B and Figure 3—figure supplement 1B). Sites on KIAA1217 and Girdin were also upregulated in PTPRK KO cells, and analysis of our raw interaction data (Figure 2—source data 1) showed peptides for each protein were present in PTPRK pull downs, suggesting they are also potential substrates. Unfortunately, antibodies were not available to study them further. Critically, our total proteome analysis showed that the observed phosphosite levels on all proteins were not due to differences in protein amounts, except for PLEKHA6, which was not quantified (Figure 3C and Figure 3—source data 1 and 2). Beyond PTPRK-interacting proteins we found upregulated phosphosites on several other cell-cell adhesion regulators as well as ST5, ARHGAP5 and the receptor DCBLD2 (Figure 3B and D). Interestingly, DCBLD2 was previously identified as a PTPRK-interacting protein in a large-scale AP-MS study (Huttlin et al., 2017). In contrast, specific sites on Paxillin, EGFR and STAT3 were not changed or were undetectable (Figure 3B and Figure 3—source data 1). Thus, by combining the PTPRK interactome with tyrosine phosphoproteomics we have identified eight candidate substrates (Figure 3—figure supplement 1C).

![Figure 3.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig3-v1.jpg)

**Figure 3.:** (A) Schematic of workflow to enrich and identify phosphotyrosine peptides from SILAC-labeled wildtype and PTPRK KO MCF10As. Equal amounts of wildtype and PTPRK KO cell lysates were combined prior to trypsinization. A 10% sample was reserved for total proteome analysis. Tyrosine phosphorylated peptides were enriched using anti-phosphotyrosine antibodies and SH2 domain ‘superbinders’. (B) Volcano plot of tyrosine phosphosites detected in PTPRK KO and wildtype MCF10As. Phosphosites > 50% enriched in (p<0.05; n = 3) in PTPRK KO cells are labeled red and those enriched in wildtype are blue. FDR = 0.01, two valid values required. (C) Volcano plot of protein abundance. Proteins > 50% more abundant (p<0.05; n = 3) in PTPRK KO MCF10As are shown in red, and wildtype in blue. FDR = 0.01, two valid values required. (D) Overview of proteins with at least one tyrosine phosphorylation site increased in PTPRK KO cells as determined by quantitative proteomics (FDR = 0.01, one valid value required). Tyrosine phosphosite change in PTPRK KO cells compared to wildtype is indicated by colored circles:>3 fold up; purple,>1.5 fold up; red,<1.5 fold up or down (no change); grey. Proteins identified as interactors by AP-MS or immunoblotting in this study are highlighted in bold and italics. *Denotes proteins enriched on substrate traps. See also Figure 3—figure supplements 1 and 2.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) After SEC, proteins were incubated with or without streptavidin and subjected to SDS PAGE followed by Coomassie staining to determine the extent of biotinylation. Arrows indicate the purified domains and the respective streptavidin-induced mobility shift. (B) Volcano plot of tyrosine phosphosites detected in PTPRK KO and wildtype MCF10As. Phosphosites > 50% enriched in (p<0.05; n = 3) in PTPRK KO cells are labeled red and those enriched in wildtype are blue. FDR = 0.01, one valid value required. (C) Proteins with upregulated phosphotyrosine sites in PTPRK KO cells that were also identified as PTPRK interactors, either by proteomics or immunoblotting. (D) Weblogo representation of amino acids surrounding phosphotyrosine from candidate substrates in (C). (E) Surface charge representation of PTPRK-D1 (left; PDB: 2C7S Eswaran et al., 2006) showing acetate bound to the active site. Yellow line represents the approximate binding location for a ~ five amino acid phosphopeptide. Scale indicates kcal/mol·e. (F) Phopshopeptide motifs derived from PTPRK candidate substrates ([STEADNR][NPDHLRTY][INSEPGV]pY[VADIEFGSY][DTEGIKNQRS][LFPSTANR]) were used to search the phosphosite plus database. Scramble 1 and 2 correspond to the following searches: [LFPSTANR][DTEGIKNQRS][VADIEFGSY]pY[INSEGPV][INSEGPV][STEADNR] and [INSEGPV][NPDHLRTY][STEADNR]pY[LFPSTANR][DTEGIKNQRS], respectively. Listed are PTPRK-interacting proteins with phosphosites predicted by the consensus. Number of overlapping proteins between phosphosite plus searches and interactors are shown on Venn diagrams.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A–B) PTPRK interactors identified by mass spectrometry were validated using pull downs with the specified PTPRK and PTPRM protein domains from pervanadate-treated, confluent MCF10A cell lysates followed by immunoblot analysis. Input and supernatants reveal the extent of protein depletion by recombinant proteins. (C) GO term analysis using Metascape of proteins with increased tyrosine phosphorylation in PTPRK KO MCF10As. FDR = 0.01, one valid value required.

Using these candidate substrates, we next aimed to determine any sequence selectivity by PTPRK. Previously, Barr et al. (2009) tested recombinant PTPs against a panel of phosphopeptides and observed limited sequence selectivity. For example, PTPRK showed reduced activity against peptides with basic residues in the three positions N-terminal to phosphotyrosine, including an EGFR-pY1068-containing peptide. In contrast, PTPRB showed no sequence preference (Barr et al., 2009). To investigate whether our candidate substrates shared common features we generated a consensus sequence, which showed a slight bias against basic residues immediately adjacent to the phosphotyrosine (Figure 3—figure supplement 1D). This is consistent with the positively charged PTPRK active site entrance observed in its crystal structure, which may preclude binding of positively charged or basic amino acids (Figure 3—figure supplement 1E). We next searched the phosphosite plus database with a seven amino acid consensus sequence phosphotyrosine and cross-referenced to the PTPRK interactome (Figure 2—source data 1). Beyond the candidate substrates, we identified an additional 18 phosphosites matching the consensus including substrate-trapped MAP4K4 and junction-associated ABLIM3 (Matsuda et al., 2010). In contrast, when we scrambled the consensus sequence we found fewer PTPRK interactors were identified (Figure 3—figure supplement 1F). Therefore, PTP substrate consensus sequences might be useful in expanding a candidate substrate list when interactors are known, but most likely only represents a permissive sequence for dephosphorylation, rather than a strict requirement.

Based on our data and these analyses, PKP3, MAP4K4 and ABLIM3 were also included as candidate substrates after confirming interactions with PTPRK and PTPRM domains (Figure 3—figure supplement 2A and B). A GO term analysis of statistically-enriched phosphosites from at least one sample (Figure 3D and Figure 3—figure supplement 2C) showed a bias towards proteins with roles in cell junction and actin cytoskeleton organization. Interestingly, several phosphosites identified here are growth factor- and, in most cases, Src kinase-dependent (Reddy et al., 2016). Importantly, however, the Src family kinase activating phosphotyrosine (e.g. Src-Y419) is 1.6-fold lower in PTPRK KO cells, therefore such kinase activity does not explain the observed differences (Figure 3—source data 1). Thus, PTPRK influences the tyrosine phosphorylation of numerous interacting proteins in cells, suggesting it has non-redundant cellular phosphatase activity.

### PTPRK interacts with candidate substrates in confluent MCF10A cells

To investigate proximity interactions of proteins identified by AP-MS and phosphoproteomics in confluent cells we used BioID (Roux et al., 2012). We confirmed the cell surface localization of mutant BirA and flag-tagged PTPRK-C1089S and truncated PTPRK, lacking an ICD, by immunostaining. Truncated PTPRK showed notably stronger staining at the cell surface than PTPRK-C1089S, perhaps reflecting the loss of an endocytic or degradative signal in the ICD (Figure 4—figure supplement 1A). Immunoblots of pulldowns from doxycycline-induced, confluent cells revealed enrichment on PTPRK-C1089S over the truncated form for the candidate substrates Afadin, PARD3, p120Cat, PKP3, PKP4, as well as ABLIM3 and EGFR, but not E-Cadherin, Paxillin, β-Catenin, Tubulin or ZO2 (Figure 4A and B, and Figure 4—figure supplement 1B). Importantly, MINK1, PKP4, PTPN14 and DLG5 were also enriched and were previously identified by PTPRK BioID in HEK293 cells (St-Denis et al., 2016), lending additional support to our observations (Figure 4C). These data confirm that several of the interactors identified by AP-MS and phosphoproteomics experiments also interact with PTPRK in confluent MCF10A cells.

![Figure 4.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig4-v1.jpg)

**Figure 4.:** (A) Representative immunoblot analysis of biotin pull downs from MCF10As expressing tGFP or PTPRK BioID constructs. See Materials and methods for details. Red and blue arrows indicate exogenous and endogenous PTPRK, respectively. (B) Quantification of BioID immunoblots. Green bars indicate the number of times a protein was enriched on PTPRK-C1089S.BirA*-Flag, compared to PTPRK.ECD +TMD.BirA*-Flag in separate experiments. Purple bars indicate the number of times a protein was not enriched or was not detected in any pull downs. n ≥ 1. (C) Schematic representation of PTPRK proximity-labeling by BioID. PTPRK extracellular domain homology model is based on PTPRM (PDB: 2V5Y; Aricescu et al., 2007). Proteins within the dotted lines were detected in pull downs from indicated BioID lysates. Proteins not detectably biotinylated are listed on the left. Proteins in bold and italics were previously identified as PTPRK interactors using BioID in HEK293 cells (St-Denis et al., 2016). See also Figure 4—figure supplement 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) MCF10As with stably integrated doxycycline-inducible expression constructs (PTPRK-ECD +TMD-BirA*-Flag and PTPRK-C1089s-BirA*-Flag) were treated with 150 ng/ml and 500 ng/ml doxycycline, respectively, and immunostained using an anti-Flag antibody. F-actin and nuclei were stained with phalloidin and Hoechst, respectively. Scale bars = 50 µm. (B) Representative immunoblot analysis of biotin pull downs from MCF10As expressing tGFP or PTPRK BioID constructs. See Materials and methods for details. Red and blue arrows indicate exogenous and endogenous PTPRK, respectively. * residual ABLIM3 signal.

### PTPRK directly and selectively dephosphorylates polarity and junctional proteins

We next sought to determine whether PTPRK could directly dephosphorylate any of its binding partners in vitro, with a particular focus on proteins that were hyperphosphorylated in PTPRK KO cells. Phosphatases have a reputation for promiscuity therefore we included the intracellular domain of the closely related receptor PTPRM and assayed a panel of negative controls. Using an in vitro para-nitrophenylphosphate (pNPP) colorimetric dephosphorylation assay, we determined that a three-fold higher molar ratio of PTPRM was required to match PTPRK activity (Figure 5—figure supplement 1A), consistent with a previous study (Barr et al., 2009). Interestingly, a three-fold higher molar ratio of PTPRK-ICD was required for equivalent activity to the D1 domain, suggesting the D2 reduces D1 enzyme activity (Figure 5—figure supplement 1A).

To identify proteins dephosphorylated by PTPRK, pervanadate-treated MCF10A cell lysates were incubated with recombinant protein domains, followed by phosphotyrosine immunoprecipitation and immunoblotting (Figure 5A). We expected dephosphorylated proteins to be depleted from immunoprecipitates but present in supernatants, or, as observed for PKP4, to show a shift in molecular weight. In these assays phosphoproteins from different reactions were equally enriched by IP, as indicated by phosphotyrosine immunoblots, but the lysates incubated with active phosphatase domains had fewer phosphoproteins overall based on depletion from supernatants (Lower panel; Figure 5B). Consistent with our interaction data, several previously reported R2B receptor substrates including E-Cadherin, STAT3, β-Catenin, Paxillin and EGFR-pY1068 (Duan et al., 2015), were not dephosphorylated by either PTPRK or PTPRM under these conditions (Figure 5B and Figure 5—figure supplement 1B-C). In contrast, the PTPRK ICD, but strikingly not the PTPRK-D1 or PTPRM domains, completely dephosphorylated Afadin (Figure 5B and Figure 5—figure supplement 1B), suggesting a combined role for the D1 and D2 domains in its recognition and selective dephosphorylation. PARD3 and PKP3 were preferentially dephosphorylated by the PTPRK and PTPRM ICDs. In contrast, the PTPRK and PTPRM D1 domains alone were sufficient to dephosphorylate ABLIM3, PKP4 and p120Cat (Figure 5B). Conversely, RAPGEF6 and MINK1 were not clearly dephosphorylated by the domains under these conditions (Figure 5—figure supplement 1B and C). MAP4K4, FMRP and NUFIP2 were not detectably tyrosine phosphorylated in the cell lysates, precluding us from assessing dephosphorylation (Figure 5—figure supplement 1C). It has been suggested for the R2A RPTPs that the inactive D2 domain can inhibit the D1 domain (Wallace et al., 1998). However, addition of PTPRK-D2 to PTPRK-D1 did not affect its activity against, for example, p120Cat (Figure 5B). In combination with our interaction studies, these data suggest that PTPRM and PTPRK have overlapping substrate specificities for δ-catenin proteins, ABLIM3 and PARD3, and the PTPRK-ICD selectively dephosphorylates Afadin.

![Figure 5.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig5-v1.jpg)

**Figure 5.:** (A) Workflow of in-lysate dephosphorylation assay. Recombinant PTPRK and PTPRM domains were incubated with pervanadate-treated MCF10A lysates for 1.5 hr at 4°C, followed by immunoprecipitation of tyrosine phosphorylated proteins. (B) Pervanadate-treated MCF10A lysates were incubated with the indicated domains at an amount pre-determined to give equal phosphatase-activity prior to phosphotyrosine immunoprecipitation and immunoblot analysis. (C) Pull downs using chimeric RPTPs from confluent, pervanadate-treated MCF10A lysates were subjected to immunoblot analysis. (D) Pervanadate-treated MCF10A lysates were incubated with the indicated domains prior to phosphotyrosine immunoprecipitation and immunoblot analysis. See also Figure 5—figure supplements 1 and 2.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) The indicated PTPRK and PTPRM domains were assayed for phosphatase activity using the pNPP colorimetric assay. Control wells contained pNPP only. Protein amounts used are shown. (B) Pervanadate-treated MCF10A lysates were incubated with predetermined amounts of the indicated domains to give equal phosphatase-activity, prior to phosphotyrosine immunoprecipitation and immunoblot analysis. (C) Recombinant proteins consisting of combinations of PTPRK and PTPRM D1 and D2 domains were expressed in and using Ni-NTA affinity resin. Purified proteins were then subjected to size exclusion chromatography. (D) Recombinant His- and Avi-tagged PTPRK and PTPRM chimeric domains were purified from E. coli cultured in biotin-supplemented media, incubated ±streptavidin and subjected to SDS-PAGE and Coomassie staining, to determine the extent of biotinylation. Arrows indicate the purified domains and the respective streptavidin-induced mobility shift. (E) The indicated recombinant PTPRK and PTPRM chimeric domains were incubated were assayed for phosphatase activity using the pNPP colorimetric assay. Control wells contained pNPP. Protein amounts used are shown.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Pull downs using PTPRK-ICD D1057A and PTPRK-D2 domains from confluent, pervanadate-treated MCF10A lysates were incubated with and without 20 mM vanadate for 30 min. 4% inputs (I), 4% supernatants (S), 4% eluates (E; following treatment) and final pull downs (P) were subjected to immunoblot analysis. (B) Confluent, pervanadate-treated MCF10A lysates were treated with or without 20 U/ml CIP at 4°C for 16 hr to remove protein phosphorylation and were used for pull downs with PTPRK D2 domain. 4% inputs (I), 4% supernatants (S) and pull downs (P) were subjected to immunoblot analysis. (C) Clustal Omega alignment of PTPRK-D1 vs PTPRK-D2 vs PTPRK-D2 triple mutant generated using Jalview. (D) The indicated PTPRK domains were assayed for phosphatase activity using the pNPP colorimetric assay. Activity levels relative to PTPRK ICD are shown. Error bars denote ±SEM of technical triplicates. (E) Pull downs using indicated wildtype and mutant PTPRK domains from confluent, pervanadate-treated MCF10A lysates were analyzed by immunoblot. (F) Ribbon and surface representations of CD45 (PTPRC; PDB: 1YGR; Nam et al., 2005). The corresponding ‘active site’ cysteine residues (C828S for D1 and C1144 for D2) are highlighted in red. (G) Surface charge representation of PTPRK-D1 (left; PDB: 2C7S [Eswaran et al., 2006]) and PTPRK-D2 (right; homology model based on PDB: 6D3F (PTPRE-D2; [Lountos et al., 2018])).

To further investigate the role of the PTPRK and PTPRM domains in substrate selectivity, we generated chimeric proteins consisting of combinations of the PTPRK and PTPRM D1 and D2 domains (Figure 5C and Figure 5—figure supplement 1D). In pull down assays, we found that PARD3 and p120Cat bound to all proteins (Figure 5C). Consistent with our previous findings, Afadin and NUFIP2 showed a preference for proteins with the PTPRK-D2 domain, which is particularly evident by supernatant depletion (Figure 5C). In contrast, RAPGEF6 bound equally to both PTPRK domains (Figure 5C). In dephosphorylation assays, proteins with the PTPRM D1 were used at a 3-fold higher concentration than PTPRK D1 domains to compensate for their lower activity (Figure 5—figure supplement 1E). Strikingly, the PTPRK-D2 domain is sufficient to recruit Afadin for dephosphorylation by PTPRM-D1 (Figure 5D). In contrast, p120Cat is dephosphorylated by all domains, based on its presence in the associated supernatants (Figure 5D). Consistent with our previous findings, Paxillin is not dephosphorylated by any PTPRK or PTPRM combinations (Figure 5D). Together, these data demonstrate that PTPRK and PTPRM can directly and selectively dephosphorylate substrates, and that the D2 pseudophosphatase domain is necessary and sufficient for recruitment of the PTPRK-specific substrate, Afadin.

A role for RPTP pseudophosphatase domains in substrate recognition has been proposed, however, the mechanism remains elusive. Structural studies on other RPTP D2 domains show a canonical PTP fold (Barr et al., 2009; Nam et al., 1999; Nam et al., 2005) and resemble substrate traps due to amino acid variation in key catalytic motifs. For example, the LAR (PTPRF) D2 domain could be converted to an active PTP by just two mutations (Nam et al., 1999). We were unable to deplete Afadin from the PTPRK D2 domain with vanadate or dephosphorylation of cell lysates, suggesting binding is not mediated by phosphotyrosine (Figure 5—figure supplement 2A and B). We next attempted to reactivate the PTPRK D2 domain by reintroducing canonical sequences to the WPD loop, PTP signature motif and Q loop (Figure 5—figure supplement 2C; Andersen et al., 2001). Using a pNPP assay, we found no impact of the mutations on D2 domain activity (Figure 5—figure supplement 2D), similar to recent failed attempts to reactivate the PTPRE D2 domain (Lountos et al., 2018). Importantly, the D2 domain mutations did not abrogate binding to several interactors (Figure 5—figure supplement 2E). The catalytic cysteine, which forms a phosphocysteine intermediate in PTP D1 domains (Pannifer et al., 1998), is conserved in most RPTP D2 domains (Andersen et al., 2001). However, the CD45 (PTPRC) D2 domain structure shows that this key cysteine is occluded when compared to that of the D1 (Figure 5—figure supplement 2F). We generated a homology model for the PTPRK D2 domain based on PTPRE, and found that the surface charge surrounding the putative active site significantly diverges from that of the D1 domain (Figure 5—figure supplement 2G). These data suggest the D2 domain substrate recognition mechanism does not require substrate phosphorylation, which is consistent with our earlier findings (Figure 2H and I) as well as PTPRK D2 domain structural and sequence features.

### PTPRK dephosphorylates p120Cat-pY228 and -pY904 in MCF10A cells

The Phosphosite plus database includes 17 frequently phosphorylated Human p120Cat tyrosine residues that have been identified by mass spectrometry (Hornbeck et al., 2015). By the same criteria, the larger protein Afadin is phosphorylated on only five tyrosine residues (Hornbeck et al., 2015). This difference might explain why PTPRK completely dephosphorylates most of the Afadin present in lysates, but only a fraction of p120Cat (Figure 5B). Therefore, our dephosphorylation assays are likely to be quite conservative, particularly for proteins with many phosphosites. Our phosphoproteomics data revealed hyperphosphorylation of p120Cat-Y174, -Y228, -Y865 and -Y904 in PTPRK KO cells, suggesting these could be direct targets for PTPRK. Antibodies were available to detect phosphorylated p120Cat-Y228 and -Y904. To determine whether these sites could be directly dephosphorylated we incubated pervanadate lysates with recombinant protein domains and immunoblotted for specific phosphosites. In all cases, PTP domains did not dephosphorylate EGFR-pY1068 or Paxillin-pY118 (Figure 6A and Figure 6—figure supplement 1A and B). In contrast, PTPRK-D1 and ICD, but not the catalytically inactive PTPRK-C1089S (Figure 6A) or pervanadate-inhibited PTPRK ICD (Figure 6—figure supplement 1A), almost completely dephosphorylated both p120Cat-pY228 and -pY904 sites. PTPRM also dephosphorylated both sites (Figure 6—figure supplement 1B). Whilst these p120Cat sites are efficiently dephosphorylated by PTPRK, only a small fraction of p120Cat undergoes complete dephosphorylation (Figure 5B). Combined with the observation that p120Cat-pY257 levels were unchanged in PTPRK KO cells by phosphoproteomics (Figure 3—source data 1) our data are consistent with PTPRK site selectivity, at least for p120Cat.

![Figure 6.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig6-v1.jpg)

**Figure 6.:** (A) Pervanadate-treated MCF10A lysates were incubated with and without the indicated recombinant PTPRK-D1, PTPRK-ICD or PTPRK-C1089S-ICD for 1.5 hr at 4°C, prior to immunoblot analysis. (B–C) Lysates from confluent wildtype and PTPRK KO MCF10As were analyzed by immunoblot and quantified by densitometry. Error bars denote ±SEM (n ≥ 3). Unpaired, two-tailed t test: *p<0.05, **p<0.005. (D) Wildtype or PTPRK KO MCF10As, with stably-integrated doxycycline-inducible tGFP, PTPRK or PTPRK-C1089S, were cultured for 6 days with indicated concentrations of doxycycline then lysed and subjected to immunoblot analysis. (E) Densitometric quantification of p120Cat phosphorylation normalized against total p120Cat. Error bars denote ±SEM (n = 5). Two-way ANOVA (Tukey’s multiple comparisons test): *p<0.005**, p<0.005, ***p<0.0005. See also Figure 6—figure supplement 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A–B) Pervanadate-treated MCF10A lysates were incubated with and without the indicated recombinant PTPRK-ICD or PTPRM-ICD protein domains, with or without pervanadate (10 mM) for 1.5 hr at 4°C, prior to immunoblot analysis.

Immunoblotting confirms that p120Cat-pY228 and -pY904 are increased on average 3–4-fold in confluent PTPRK KO cells compared to wildtype, whereas Paxillin-pY118 is unchanged, consistent with our phosphoproteomics results (n = 4; Figure 6B and C; Figure 3—source data 2). We next used the site-specific p120Cat phosphoantibodies to assess whether the direct dephosphorylation of putative substrates observed in vitro translated to an intact cellular context. Doxycycline-induction of PTPRK, but not the C1089S mutant, in PTPRK KO cells reproducibly and dose-dependently reduced p120Cat-pY228 and -pY904 levels, without affecting total p120Cat (n = 5; Figure 6D and E). Conversely, reintroduction of PTPRK did not affect Paxillin-pY118. These results suggest PTPRK is an active and selective tyrosine phosphatase for p120Cat in confluent MCF10A cells.

### PTPRK promotes junction integrity in epithelial cells

We have demonstrated that Afadin, PARD3, PKP3, PKP4, and p120Cat are high confidence substrates for PTPRK, with PLEKHA6, MAP4K4, PKP2, KIAA1217, ABLIM3 and Girdin also being good candidates. Because these proteins are linked by roles in cell-cell junction organization, we sought to determine the impact of PTPRK loss on MCF10A morphology. Wildtype and PTPRK KO cells displayed signaling differences by phosphoproteomics at 24 hr after media change (Figure 3B). We therefore used the same conditions to investigate junctional integrity of confluent cells. To this end, wildtype and PTPRK KO cells grown on transwell filters were analyzed by electron microscopy. Wildtype cells were more closely packed and organized than PTPRK KO cells, which exhibited large gaps between cells (Figure 7A). Moreover, we observed a striking reduction in cell height in PTPRK KO cells (Figure 7A (inset) and 7B). We further investigated junctional integrity by measuring the transepithelial electrical resistance (TEER) and FITC dextran permeability of cells grown on transwell filters. PTPRK KO cells exhibited a ~ 50% reduction in TEER and a small but significant increase in FITC-dextran permeability compared to wildtype cells indicating a leakier monolayer (Figure 7—figure supplement 1A–B). TEER measurements were partially rescued by reintroduction of PTPRK, but not a catalytically inactive mutant (Figure 7C). Consistent with this altered organization, immunostained PTPRK KO cells grown on coverslips displayed a ~ 20% decrease in the intensity of F-actin, the AJ protein E-Cadherin, the desmosomal protein Desmoglein 3 (DSG3) and the PTPRK substrate p120Cat (Figure 7—figure supplement 1C–F). The junctional markers also displayed reduced colocalization with F-actin (Figure 7—figure supplement 1G–H). However, the levels of these junctional proteins were unaffected by PTPRK loss (Figure 6B and Figure 7—figure supplement 1I). Reintroduction of PTPRK or PTPRK-C1089S was able to partially rescue E-Cadherin intensity (Figure 7D and Figure 7—figure supplement 2A), however, catalytic activity was required to rescue F-actin intensity (Figure 7D–E). In line with this, rescue of E-Cadherin and F-actin colocalization requires PTPRK D1 domain activity, suggesting PTPRK substrate hyperphosphorylation contributes to impaired junctional integrity.

![Figure 7.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig7-v1.jpg)

**Figure 7.:** (A) Wildtype (Left) and PTPRK KO (Right) MCF10As were cultured on transwell filters before being fixed and prepared for conventional electron microscopy (EM). Scale bar = 5 µm. (B) Quantification of cell height relative to transwell filter. Three measurements per image were averaged. Each data point relates to one EM image. Error bars denote ±SEM. Unpaired, two tailed t test ***p<0.0005. (C) Stable PTPRK KO MCF10As were grown to confluence with or without 250 ng/ml doxycycline on 0.4 µm transwell filters prior to TEER analysis. Error bars denote ±SEM (n = 3). Two-way ANOVA (Sidak's multiple comparisons test): *p<0.05. (D) Confluent PTPRK KO MCF10As, with stably-integrated doxycycline-inducible PTPRK or PTPRK-C1089S, were cultured for 6 days with or without 250 ng/ml doxycycline then fixed and stained for E-Cadherin and F-actin. A representative confocal microscopy image is shown. Scale bar = 20 µm. (E) Quantification of relative F-actin staining intensity. 10 random fields/replicate were averaged. Error bars denote ±SEM (n ≥ 3). Two-way ANOVA (Sidak's multiple comparisons test): *p<0.05 (F) Quantification of colocalization (Pearson coefficient) between E-Cadherin and F-actin staining. 10 random fields/biological replicate were averaged. Error bars denote ±SEM (n = 3). Two-way ANOVA (Sidak's multiple comparisons test): *p<0.05. See also Figure 7—figure supplement 1.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) Wildtype and PTPRK KO MCF10As grown to confluence on 0.4 µm transwell filters were subjected to a media change 24 hr prior to TEER analysis. Error bars denote ±SEM (n = 3). Unpaired, two-tailed t test: *p<0.05. (B) Fluorescence intensity of the lower chamber of 0.4 µm transwell filters with wildtype and PTPRK KO MCF10As after incubation with 3 mg/ml 250 kDa FITC Dextran (added to the upper chamber) for 24 hr. (C–D) Confluent wildtype and PTPRK KO MCF10As were fixed and stained for E-Cadherin (C), DSG3 (D) or p120Cat (E) and F-actin. A representative confocal microscopy image is shown. Scale bar = 20 µm. (F) Quantification of relative F-actin, E-Cadherin, DSG3 and p120Cat staining intensity comparing wildtype and PTPRK KO MCF10As. 10 random fields/biological replicate were averaged. Error bars denote ±SEM (n ≥ 3). Two-way ANOVA (Sidak's multiple comparisons test): **p<0.005, ***p<0.0005. (G–H) Quantification of co-localization (Pearson coefficient) between E-Cadherin (F) or DSG3 (G) and F-actin staining comparing wildtype and PTPRK KO MCF10As. Error bars denote ±SEM (n = 3). Unpaired, two-tailed t test: *p<0.05. (I) Immunoblot analysis of confluent wildtype and PTPRK KO MCF10A.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** (A) Quantification of relative E-Cadherin staining intensity. 10 random fields/replicate were averaged. Error bars denote ±SEM (n ≥ 3). Two-way ANOVA (Sidak's multiple comparisons test): *p<0.05.

It has previously been reported that shRNAs targeting PTPRK in MCF10A cells perturbs their morphogenesis in 3D culture (Ramesh et al., 2015). We find PTPRK KO cells mostly form normal acini (Figure 8 and Figure 8—figure supplement 1A); however,~20% exhibited a branched or protrusive morphology after 14 days in culture (Figure 8B), resembling the previously described invasive behavior observed upon combined EGFR and Src overexpression in MCF10A cells (Dimri et al., 2007). When we collected intact spheroids for immunostaining we found normal apical polarization of the Golgi (Figure 8C). However, PTPRK KO spheroids were significantly larger, by diameter, than wildtype (Figure 8D), despite similar proliferation rates of subconfluent cells in 2D (Figure 8—figure supplement 1B). Overall, our results support a role for PTPRK in promoting cell-cell junctions and repressing invasive behavior, probably through recruitment and dephosphorylation of several cell junction organizers.

![Figure 8.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig8-v1.jpg)

**Figure 8.:** (A) Phase contrast images of wildtype and PTPRK KO. MCF10A spheroids after 14 day culture in Matrigel. Scale bar = 200 µm. (B) Frequency of aberrant acini observed in six independent wells each of wildtype and PTPRK KO MCF10A spheroids. Unpaired, two-tailed t test: *p<0.05. (C) Representative images of MCF10A spheroids stained for the Golgi marker GM130, F-actin and nuclei (Hoechst), after removal from Matrigel. Scale bar = 20 µm. (D) Circles were traced over cross sections, based on the Hoechst channel, for a total of 563 WT and 551 PTPRK KO immunostained spheroids from three entire slides per genotype and diameters calculated in Zen Pro. Unpaired, two-tailed t test: ***p<0.0005. See also Figure 8—figure supplement 1.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/44597/elife-44597-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A) Phase contrast images of wildtype and PTPRK KO MCF10A spheroids after 14 day culture in Matrigel. Scale bars = 200 µm. (B) BrdU incorporation assay performed on subconfluent WT and PTPRK KO MCF10As (n = 3). Unpaired, two-tailed t test: ns = not significant.

## Discussion

We have used unbiased approaches to identify five high confidence substrates of the cell-contact sensing receptor PTPRK, including Afadin, PARD3, p120Cat, PKP3 and PKP4. These substrates are linked to cell-cell junction organization, which is perturbed when PTPRK is deleted. Importantly, our findings demonstrate the substrate selectivity of this receptor, which requires both its active and inactive PTP domains. We also identify PTPRK as a key mediator of adhesive signaling. Our conclusions have implications not only for understanding PTP biology and cell-cell junction phosphoregulation, but also provide molecular insight into how PTPRK might function as a tumor suppressor.

Cross-referencing the PTPRK interactome with the PTPRK-dependent tyrosine phosphoproteome enabled us to identify candidate substrates to assay for cellular interactions and direct dephosphorylation. Substrate-trapping methods in combination with mass spectrometry are commonly used to identify PTP substrates (Blanchetot et al., 2005). We used two mutants affecting the WPD catalytic motif (D1057A) and catalytic cysteine within the PTP signature motif (C1089S) and found enrichment of distinct proteins on each. Using both Hs27 and MCF10A lysates, MAP4K4 and RAPGEF6 were enriched on the D1057A trap. Both were partially competed from traps with the phosphate mimetic vanadate, suggesting phosphorylation-dependent interaction. However, we could not validate RAPGEF6 or MAP4K4 as PTPRK substrates by in vitro dephosphorylation or phosphoproteomics, perhaps reflecting a limitation to the sensitivity or selectivity of our assays. Interestingly, these proteins were recently linked to mechanotransduction and hippo signaling, along with the PTPRK interactor MINK1 (Meng et al., 2018). An interesting future line of research will be to determine whether PTPRK is an upstream regulator of this new mechanotransduction pathway.

The cell junction organizers PARD3, Afadin and PLEKHA6 were all trapped by the C1089S mutant. Our immunoblots also highlighted phosphorylation-dependent enrichment of p120Cat and PKP4 on this trap. These five proteins were subsequently found to be hyperphosphorylated in PTPRK KO cells, suggesting that the C1089S mutant was effective in identifying substrates. However, we also found hyperphosphorylation of other PTPRK-binding partners in KO cells, indicating the traps alone were too restrictive in identifying substrates. Indeed, the PTPRK pseudophosphatase D2 domain was sufficient for substrate recognition, which may have masked the effect of the substrate traps, particularly as we have shown that D2 domain binding to most proteins is independent of tyrosine phosphorylation. By considering the entire PTPRK interactome, we could include the armadillo family proteins PKP3, PKP4 and p120Cat as substrates. Our criteria were quite conservative, and it is likely that ABLIM3, PLEKHA6, Girdin, KIAA1217 and PKP2 are also substrates, all of which are also linked to junction organization (Gallegos et al., 2016; Guo et al., 2014). Furthermore, we cannot rule out the existence of additional PTPRK substrates, for example, that are expressed in different cellular contexts, particularly as we observed divergent interactomes between epithelial and fibroblast cells.

Strikingly, most of the candidate PTPRK substrates identified here have orthologs in Drosophila, yet the R2B receptor family first appears in chordates (Chen et al., 2017). This suggests that rather than co-evolving with its substrates, PTPRK regulates pre-established functional protein complexes. In this way, PTPRK would have introduced new regulation, and perhaps function, to existing signaling networks for chordate and vertebrate-specific organization. Indeed, there are genetic links between orthologs for RAPGEF6, PARD3 and Afadin in the regulation of Drosophila AJ formation (Bonello et al., 2018). Furthermore, PARD3 and p120Cat Drosophila orthologs have been linked to the control of E-Cadherin internalization and recycling (Bulgakova and Brown, 2016). Several PTPRK substrates belong to the δ-catenin family, which undergoes significant expansion from one gene in Drosophila to seven in vertebrates (Carnahan et al., 2010). We did not detect ACRVF, PKP1 or δ-catenin (CTNND2) in MCF10A total proteomes (Figure 3—source data 1); however, these might be additional R2B family substrates in other cell types, such as neurons (Paffenholz and Franke, 1997). PKP2 was an interactor and hyperphosphorylated in PTPRK KO cells, but its dephosphorylation was not assessed. PKP3 has been proposed to promote the stability of desmosomes upon overexpression (Gurjar et al., 2018). PKP4 is targeted to both adherens junctions and desmosomes, but its role is less well understood (Hatzfeld et al., 2003). Our finding that PTPRK promotes junctional integrity raises the possibility that dephosphorylation of substrates, such as p120Cat, would stabilize cadherin-based junctional assemblies. Interestingly, our ultrastructural analysis showed that PTPRK KO cells have leakier junctions and are shorter and less organized. This is reminiscent of the proposed role of p120Cat in controlling epithelial cell lateral domain expansion and shape maturation by balancing junctional contractility and maturation through regulation of E-Cadherin and RhoA (Yu et al., 2016), which reportedly depends on p120Cat tyrosine phosphorylation status (Castaño et al., 2007; Davis et al., 2003; Fukumoto et al., 2008). Indeed, we show that PTPRK dephosphorylates p120Cat in cells, and that PTPRK phosphatase activity is necessary to rescue junctional deficits.

Afadin appears to be a unique PTPRK substrate; it was not dephosphorylated by the very closely related PTPRM and it had the highest fold increase in tyrosine phosphorylation in PTPRK KO cells. Strikingly, this specificity is determined in large part by the PTPRK D2 pseudophosphatase domain, which was sufficient to recruit Afadin for dephosphorylation by the PTPRM D1 domain. This might reflect the greater identity between the PTPRK and PTPRM active D1 domains than the D2 domains (78% vs 73.6%). In line with this, we found little evidence for a PTPRK substrate consensus sequence other than a bias against basic residues immediately adjacent to the phosphotyrosine site, similar to previous reports for other PTPs (Barr et al., 2009). Several RPTPs have tandem intracellular PTP domains and the precise function of the inactive D2 domains remain to be determined (Tonks, 2006). The Janus kinases have a similar tandem arrangement where a pseudokinase domain regulates kinase activity (Babon et al., 2014). Indeed, regulation of the PTP D1 by D2 domains has been suggested for several RPTPs (Toledano-Katchalski et al., 2003). We do observe a three-fold reduction in PTPRK ICD enzyme activity compared to the D1 domain alone. However, when free D2 domain was added to free D1 domain, we saw no impact on activity. Instead, we find a key role for the pseudophosphatase domain in substrate recognition, similar to findings for CD45/PTPRC (Nam et al., 2005). We further show that unlike LAR (Nam et al., 1999), the PTPRK D2 domain could not easily be reactivated by mutation. Additionally, we rule out a role for the D2 domain in phosphotyrosine recognition using dephosphorylated lysates, vanadate competition and a PTPRK homology model. Several previous reports have shown that wildtype PTPs can interact with substrates, which are presumably in a dephosphorylated state (Chen et al., 2006; Lee and Bennett, 2013; Timms et al., 1998). Thus, PTPRK might serve as a scaffold for dephosphorylated proteins either by recruiting non-phosphorylated proteins, or by dephosphorylating already phosphorylated proteins upon recruitment. It is likely that the combination of recognition and dephosphorylation is important for full PTPRK function. Determining the spatiotemporal dynamics of PTPRK protein recruitment will be an important next step.

PTPRK and PTPRM both dephosphorylated PARD3, p120Cat, PKP3 and PKP4 in lysates. Despite this, hyperphosphorylation of sites on each of these proteins were found in PTPRK KO cells, indicating that PTPRM cannot fully compensate for PTPRK loss. This could be due to lower PTPRM expression levels in MCF10A cells, possible differences in site selectivity or its intrinsically lower catalytic activity (this study and Barr et al., 2009). Vertebrate genomes all encode at least 4 R2B family members, with distinct expression profiles (Figure 1—figure supplement 1A). For example, by in situ hybridization the receptors display divergent expression patterns in the adult mouse cerebellum (Besco et al., 2004). Assuming they are regulated similarly by cell-cell contact, our results indicate that receptor expression patterns will determine subtly distinct responses to cell contact.

Several phosphosites that are regulated by PTPRK have been characterized previously. p120Cat-Y228 is phosphorylated in response to EGFR and a construct with N terminal phosphorylation-deficient mutations (including Y228F) is capable of rescuing adhesion phenotypes caused by p120cat deletion (Mariner et al., 2004). In contrast, a phosphomimetic p120Cat -Y228E mutant increased recruitment of RhoA (Castaño et al., 2007). Afadin Y1237 phosphorylation, the rat equivalent of Human Afadin Y1230, has been shown to mediate recruitment of SHP2, implicating it in Ras-Mitogen activated protein kinase signaling (Nakata et al., 2007). This supports the role of PTPRK-mediated dephosphorylation of this site in tumor suppression.

PTPRK is the only R2B family member implicated by transposon-based mouse forward genetics in the progression of several cancers (March et al., 2011; Starr et al., 2009) and has been proposed to function as a tumor suppressor. Moreover, specific gene fusions result in its promoter driving the expression of oncogenic RSPO3 in a subset of colorectal cancers (Seshagiri et al., 2012). This is consistent with PTPRK being the predominant R2B receptor expressed in the mouse intestinal epithelium (Haber et al., 2017). Our findings of abrogated junction organization, spheroid overgrowth and invasive behavior in PTPRK-deficient cells support its role as a tumor suppressor. Several of the PTPRK substrates identified here have been linked to cancer, including PARD3 loss-of-function in invasion (de la Rosa et al., 2017), and oncogenic and tumor suppressive roles for p120Cat (Schackmann et al., 2013). Thus, their combined dysregulation could contribute to pathological phenotypes in a PTPRK mutant setting. Compromised epithelial barrier integrity is also linked to inflammatory bowel disease susceptibility; therefore, PTPRK SNPs linked to celiac disease should be investigated (Trynka et al., 2011). Our analysis of PTPRK KO cells showed downregulation of epithelial markers such as Keratin14, and upregulation of several mesenchymal markers such as vitronectin (VTN; Figure 3C and Figure 3—source data 1). PTPRK is a TGFβ target gene (Wang et al., 2005), and our data suggest it functions to suppress epithelial to mesenchymal transition (EMT), indicating a negative feedback role that could lead to pathological effects if perturbed (Brabletz et al., 2018).

Finally, our results provide evidence for cross-talk between PTPRK and growth factor signaling. Although PTPRK does not dephosphorylate EGFR in our assays, consistent with previous peptide assays (Barr et al., 2009), we did observe an interaction by BioID. Indeed, EGFR family interactions with R2B receptors have been reported (Yao et al., 2017). Growth factor stimulation leads to PTPRK tyrosine phosphorylation (Batth et al., 2018; Reddy et al., 2016) and it has been suggested that RTK-induced PTP inhibition by oxidation impacts cellular signaling (Reynolds et al., 2003). PTPs are well-placed to fine-tune and tailor responses to particular cellular contexts. Several PTPRK substrates are phosphorylated in a Src-dependent manner (Reddy et al., 2016). PTPRK might therefore provide feedback in the context of cell contact by dephosphorylating its substrates to promote junctional integrity. Indeed, overexpression of v-Src in epithelial cells leads to junction disassembly and EMT (Woodcock et al., 2009). Thus, such PTPs could act as interpreters of the cellular context. Interestingly, an analogous role for the contact-sensing RTK EphA2 was recently reported (Stallaert et al., 2018).

In summary, by defining the substrate repertoire of human PTPRK, we reveal mechanistic insight into its putative tumor suppressor role through its control of cell-cell junctions and suppression of EMT. Our study raises new questions about the phosphoregulation of junctional proteins and implicates PTPRK as a direct sensor and mediator of cell adhesion. We show that the PTPRK D2 domain is critical for substrate recognition, yet binds proteins independently of phosphorylation status. It will be of great interest to determine whether these findings hold true for other RPTPs. In addition, it is unknown whether the R2B receptor extracellular regions, which were previously described as spacer clamps (Aricescu et al., 2007), affect phosphatase activity or substrate recruitment. Finally, we show that PTPRK, like other PTPs (Li et al., 2013), does not recognize a peptide consensus sequence, unlike certain serine/threonine phosphatases (Shi, 2009), highlighting the need for the approach we have taken. Thus, we provide a framework for systematically identifying RPTP substrates, which in turn will advance our knowledge of these poorly characterized, yet important enzymes.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>PTPRK</td>
      <td></td>
      <td>ENSEMBL: ENST00000368213.9</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MCF10A</td>
      <td>ATCC</td>
      <td>CRL-10317</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>HEK293T</td>
      <td>D Ron</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>HEK293</td>
      <td>Sigma (ECACC)</td>
      <td>85120602-1VL</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>Hs27 Fibroblasts</td>
      <td>Sigma (ECACC)</td>
      <td>94041901-1VL</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MCF10A PTPRK KO A4</td>
      <td>This study</td>
      <td></td>
      <td>CRISPR/Cas9 and clonal selection</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MCF10A PTPRK KO E3</td>
      <td>This study</td>
      <td></td>
      <td>CRISPR/Cas9 and clonal selection</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MCF10A PTPRK KO H1</td>
      <td>This study</td>
      <td></td>
      <td>CRISPR/Cas9 and clonal selection</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MCF10A PTPRK KO pooled</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A PTPRK KO pooled.tGFP</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A PTPRK KO pooled.tGFP.P2A.PTPRK</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A PTPRK KO pooled.tGFP.P2A.PTPRK.C1089S</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A.tGFP</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A.tGFP.P2A.PTPRK.ECD-TMD.BirA*-Flag</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A.tGFP.P2A.PTPRK.C1089S.BirA*-Flag</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A PTPRK KO pooled.nuclear mApple</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Transfected construct (H. sapiens)</td>
      <td>MCF10A.nuclear mApple</td>
      <td>This study</td>
      <td></td>
      <td>Lentivirally transduced stable cell line</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-PTPRK</td>
      <td>This study</td>
      <td>2 .G6</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-PTPRK</td>
      <td>This study</td>
      <td>2 .H4</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-PTPRK</td>
      <td>This study</td>
      <td>2 .H5</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-PTPRK</td>
      <td>This study</td>
      <td>1 .F4</td>
      <td>FACS (1:200) and Immunofluorescence (IF; 1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-PTPRK</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#Sc- 374315</td>
      <td>Western blot: 1:1000 (note: we did not observe any specific signal for PTPRK with this antibody)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-PARD3</td>
      <td>Sigma</td>
      <td>Cat#HPA030443 (lot: C105765)</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-PARD3</td>
      <td>Merck Millipore</td>
      <td>Cat#07–330</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-RAPGEF6</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#sc-398642 (F-8)</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-Afadin</td>
      <td>BD Transduction Labs</td>
      <td>Cat#610732</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-DLG5</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#SC374594 (A-11)</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-PTPN14</td>
      <td>R and D Systems</td>
      <td>Cat#MAB4458</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-E-Cadherin</td>
      <td>BD Transduction Labs</td>
      <td>Cat#610181</td>
      <td>Western blot: 1:1000 IF: 1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-b-Catenin</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#9562S</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-Phospho-EGFR (Y1068)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#3777S</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-EGFR</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#4267S</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-phospho-tyrosine(P-Tyr-1000)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#8954</td>
      <td>Western blot: 1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-MAP4K4</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#5146</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-NUFIP2</td>
      <td>Bethyl Laboratories, Inc</td>
      <td>Cat#A301-600A</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-FMRP1</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat#MA5-15499</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-MINK1/MAP4K6</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat#PA5-28901</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-PKP4</td>
      <td>Bethyl Laboratories, Inc</td>
      <td>Cat#A304-649A</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-P120 catenin</td>
      <td>BD Transduction Laboratories</td>
      <td>Cat#610133</td>
      <td>Western blot: 1:1000 IF: 1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-GM130</td>
      <td>BD Transduction Laboratories</td>
      <td>Cat#610822</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-STAT3</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#4904S</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-Paxillin</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#12065 (D9G12)</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-Tubulin (Alpha)</td>
      <td>Sigma</td>
      <td>Cat#T6199</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-PTPRM</td>
      <td>Santa Cruz</td>
      <td>Cat#sc-56959</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-PKP3</td>
      <td>Abcam</td>
      <td>Cat#AB109441</td>
      <td>Western blot: 1:10000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit-anti-ABLIM3</td>
      <td>Sigma</td>
      <td>Cat#HPA003245</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit-Anti-ZO2</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat#711400</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit-anti-Phospho-P120 catenin (Y904)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#2910</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit-anti-Phospho-P120 catenin (Y228)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#2911</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Phospho-Paxillin (Y118)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#2541</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit-anti-b-Actin</td>
      <td>SIGMA</td>
      <td>Cat#A2066</td>
      <td>Western blot: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse-anti-DSG3</td>
      <td>Bio-Rad</td>
      <td>Cat#MCA2273T</td>
      <td>Western blot: 1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP conjugated-Donkey anti-Rabbit IgG</td>
      <td>Jackson Immuno-Research</td>
      <td>Cat#711-035-152</td>
      <td>Western blot: 1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP conjugated- Donkey anti-Mouse IgG</td>
      <td>Jackson Immuno-Research</td>
      <td>Cat#711-035-152</td>
      <td>Western blot: 1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP conjugated- Mouse anti-Rabbit IgG (Conformation specific)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#5127S</td>
      <td>Western blot: 1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Atto-488 Goat Anti-mouse IgG</td>
      <td>Sigma</td>
      <td>Cat#62197</td>
      <td>IF: 1:400</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Atto-488 Goat Anti-mouse IgG</td>
      <td>Sigma</td>
      <td>Cat#62197</td>
      <td>IF: 1:400</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor-647 Goat Anti Rabbit IgG</td>
      <td>Jackson Immuno-Research</td>
      <td>Cat#111-605-003</td>
      <td>IF: 1:400</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCW57.tGFP.P2A.MCS</td>
      <td>Addgene</td>
      <td>Cat#71783</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pRK.HA.PTPRK.flag</td>
      <td>Genentech</td>
      <td></td>
      <td>Corresponds to Uniprot identifier: Q15262-3</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pRK.PTPRK(1-752).IgG1</td>
      <td>Genentech</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b</td>
      <td>J. Deane</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSP.Cas9.(BB).eGFP</td>
      <td>D Ron</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMD2.G</td>
      <td>Addgene</td>
      <td>Cat#12259</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>psPAX2</td>
      <td>Addgene</td>
      <td>Cat#12260</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-puro</td>
      <td>Addgene</td>
      <td>Cat#39481</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PTPRK-BirA-R118G-Flag</td>
      <td>A-C Gingras</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCW57.tGFP.P2A.PTPRK</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCW57.tGFP.P2A.PTPRK.C1089S</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCW57.tGFP.P2A.PTPRK(1-785).BirA-R118G.Flag</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCW57.tGFP.P2A.PTPRK.C1089S.BirA-R118G.Flag</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRK.ICD</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRK.ICD.D1057A</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRK.ICD.C1089S</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRK.D1</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRK.D2</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi. PTPRK.D2.triple</td>
      <td>This study</td>
      <td></td>
      <td>Mutations: A1346P, S1347D, L1384S, E1427Q, A1428T</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRM.ICD</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRM.D1</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi. PTPRK-D1_K-D2.</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRM-D1_M-D2</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRK-D1_M-D2.</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.PTPRM-D1_K-D2.</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.Src.sbSH2</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b.His.TEV.Avi.Grb2.sbSH2</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSP.Cas9.PTPRK.sgRNA1</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSP.Cas9.PTPRK.sgRNA2</td>
      <td>This study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>ON-TARGETplus Human PTPRK siRNA</td>
      <td>Dharmacon, GE Healthcare</td>
      <td>Cat#J-004204–06</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>ON-TARGETplus Non-targeting pool siRNA</td>
      <td>Dharmacon, GE Healthcare</td>
      <td>Cat#D-001810-10-05</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>PTPRK CRISPR, BbsI.PTPRKgRNA1.Fwd</td>
      <td>SIGMA</td>
      <td></td>
      <td>CACCGCATGGATACGACTGCGGCGG</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>PTPRK CRISPR, BbsI.PTPRKgRNA1.Rev</td>
      <td>SIGMA</td>
      <td></td>
      <td>AAACCCGCCGCAGTCGTATCCATGC</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>PTPRK CRISPR, BbsI.PTPRKgRNA2.Fwd</td>
      <td>SIGMA</td>
      <td></td>
      <td>CACCGATCTCGGGTGGTAGATAATG</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>PTPRK CRISPR, BbsI.PTPRKgRNA2.Rev</td>
      <td>SIGMA</td>
      <td></td>
      <td>AAACCATTATCTACCACCCGAGATC</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>TaqMan probe: Hs02338565_gH (RPL19)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#4331182</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>TaqMan probe: Hs00267788_m1 (PTPRK)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#4331182</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>TaqMan probe: Hs00267809_m1 (PTPRM)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#4331182</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>TaqMan probe: Hs00179247_m1 (PTPRT)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#4331182</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>TaqMan probe: Hs00963911_m1 (PTPRU)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#4351372</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>DADE-pTyr-LIPQQG- phospho-peptide</td>
      <td>Cambridge Research Biochemicals</td>
      <td>Cat#crb1000746</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>END-pTyr-INASL-phospho-peptide</td>
      <td>Cambridge Research Biochemicals</td>
      <td>Cat#crb1000745</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Catalase</td>
      <td>Sigma</td>
      <td>Cat#C134514</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Cholera Toxin</td>
      <td>Sigma</td>
      <td>Cat#C-8052</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Insulin</td>
      <td>Sigma</td>
      <td>Cat#I-1882</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Epidermal Growth Factor</td>
      <td>Peprotech</td>
      <td>Cat#AF-100-15-1MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Lysyl endopeptidase (LysC)</td>
      <td>Wako</td>
      <td>Cat#129–02541</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Trypsin (proteomics grade)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#90058</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>BIOMOL Green reagent</td>
      <td>ENZO</td>
      <td>Cat#BML-AK111-0250</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Phosphate standard</td>
      <td>ENZO</td>
      <td>Cat#BML-KI102-0001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Q5 High-Fidelity DNA Polymerase</td>
      <td>New England Biolabs</td>
      <td>Cat#M0491S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Phusion Hot Start II DNA polymerase</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#F549L</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>EZ-ECL substrate</td>
      <td>Geneflow</td>
      <td>Cat#K1-0170</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NuPAGE MES (2-ethanesulfonic acid) SDS running buffer</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat#NP0002</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>InstantBlue</td>
      <td>Expedeon</td>
      <td>Cat#ISB1L</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Phosphatase inhibitor cocktail</td>
      <td>Roche</td>
      <td>Cat#04906845001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TaqMan Universal Master Mix II</td>
      <td>Applied Biosystems</td>
      <td>Cat#4440040</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MycoAlertTM PLUS Mycoplasma Detection Kit</td>
      <td>Lonza</td>
      <td>#LT07-705</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MycoProbe Mycoplasma Detection Kit</td>
      <td>R and D Systems</td>
      <td>#CUL001B</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrogen peroxide</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#H/1750/15</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium orthovanadate</td>
      <td>Alfa Aesar</td>
      <td>Cat#J60191</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>250 kDa-FITC-dextran</td>
      <td>Sigma</td>
      <td>Cat#FD250S-100MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Para-Nitrophenol-phosphate (pNPP)</td>
      <td>New England Biolabs</td>
      <td>Cat#P0757</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>IPTG</td>
      <td>Generon</td>
      <td>Cat#GEN-S-02122</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-biotin</td>
      <td>Sigma</td>
      <td>Cat#B4639</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-glutamine</td>
      <td>Sigma</td>
      <td>Cat#G7513</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrocortisone</td>
      <td>Sigma</td>
      <td>Cat#H-0888</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Puromycin</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#A11138-03</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phosphate free H2O</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#10977–035</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>8M Guanidine HCl</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#24115</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EPPS pH 8.5</td>
      <td>Alfa Aesar</td>
      <td>Cat#561296</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trifluoroacetic Acid (TFA)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#28904</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Acetonitrile</td>
      <td>VWR</td>
      <td>Cat#8364.290</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium phosphate dibasic (Na2HPO4)</td>
      <td>Acros Organics</td>
      <td>Cat#343811000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NH4OH</td>
      <td>Acros Organics</td>
      <td>Cat#460801000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methanol-free 16% (w/v) paraformaldehyde (PFA)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#28906</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Maxquant</td>
      <td>Computational Systems Biochemistry</td>
      <td></td>
      <td>Max Planck Institute of Biochemistry</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Perseus</td>
      <td>Computational Systems Biochemistry</td>
      <td></td>
      <td>Max Planck Institute of Biochemistry</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI/ImageJ</td>
      <td>Laboratory for Optical and Computational Instrumentation</td>
      <td></td>
      <td>University of Wisconsin-Madison</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen Blue</td>
      <td>Zeiss</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen Black</td>
      <td>Zeiss</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Graphpad</td>
      <td>Prism</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Chimera</td>
      <td>UCSF</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>HRP-conjugated Streptavidin</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#434323</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>STABLE competent E. coli</td>
      <td>NEB</td>
      <td>Cat#C3040I</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DH5alpha competent E. coli</td>
      <td>Invitrogen</td>
      <td>Cat#18265017</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>BL21 DE3 Rosetta E. coli</td>
      <td>J Deane</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DMEM</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#41965–039</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ham's F-12</td>
      <td>Sigma</td>
      <td>Cat#N4888</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Horse Serum</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#16050–122</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fibroblast growth medium (FGM)</td>
      <td>Promocell</td>
      <td>Cat#C-23010</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fetal Bovine Serum</td>
      <td>Sigma</td>
      <td>Cat#F7524-500ml</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Trypsin-EDTA solution</td>
      <td>Sigma</td>
      <td>Cat#T3924</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>GeneJuice transfection reagent</td>
      <td>Merck Millipore</td>
      <td>Cat#70967–3</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>EDTA-free protease inhibitors</td>
      <td>Roche</td>
      <td>Cat#11836170001</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lipofectamine RNAiMax</td>
      <td>Invitrogen</td>
      <td>Cat#13778075</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>OptiMEM</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#31985070</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lipofectamine LTX</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat#15338100</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Protein G agarose beads</td>
      <td>Merck Millipore</td>
      <td>Cat#16–266</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ni-NTA agarose</td>
      <td>QIAGEN</td>
      <td>Cat#1018244</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Streptavidin-coated magnetic beads</td>
      <td>New England Biolabs</td>
      <td>Cat#S1420S</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Streptavidin agarose</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat#20357</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DMEM SILAC media</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#PI89985</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ham's F-12 SILAC media</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#88424</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Heavy Arginine + 10</td>
      <td>Sigma</td>
      <td>Cat#608033–250 mg</td>
      <td></td>
    </tr>
    <tr>
      <td>other</td>
      <td>Heavy Lysine + 8</td>
      <td>Sigma</td>
      <td>Cat#608041–100 mg</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Proline</td>
      <td>Sigma</td>
      <td>Cat#P0380</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Light Arginine</td>
      <td>Sigma</td>
      <td>Cat#A5006</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Light Lysine</td>
      <td>Sigma</td>
      <td>Cat#L5501</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Hoechst 33342</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#62249</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>BODIPY 558/568 phalloidin</td>
      <td>Invitrogen</td>
      <td>Cat#B3475</td>
      <td>IF: 1:400</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>ProLong Gold antifade</td>
      <td>Invitrogen</td>
      <td>Cat#P36934</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Normal Serum Block</td>
      <td>BioLegend</td>
      <td>Cat#927502</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Matrigel</td>
      <td>Corning</td>
      <td>Cat#356231</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>0.2 mm nitrocellulose membrane</td>
      <td>GE Healthcare</td>
      <td>Cat#15289804</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>0.4 mm pore size Transwell filter</td>
      <td>Corning</td>
      <td>Cat#353095</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>24-well companion plates for Transwell filters</td>
      <td>Corning</td>
      <td>Cat#353504</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Millicell ERS-2 Volt/Ohm meter</td>
      <td>Merck Millipore</td>
      <td>Cat#MERS00002</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Superdex 200 16/600 column</td>
      <td>GE Healthcare</td>
      <td>Cat#28-9893-35</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Superdex 75 16/600 column</td>
      <td>GE Healthcare</td>
      <td>Cat#28-9893-33</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ultracel-3K regenerated cellulose centrifugal filter</td>
      <td>Merck Millipore</td>
      <td>Cat#UFC900324</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ultracel-10 K regenerated cellulose centrifugal filter</td>
      <td>Merck Millipore</td>
      <td>Cat#UFC901024</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ultracel-30 K regenerated cellulose centrifugal filter</td>
      <td>Merck Millipore</td>
      <td>Cat#UFC903024</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>NuPAGE 4–12% Bis-Tris gel</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#NP0321BOX</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1.5 ml low protein binding centrifuge tubes</td>
      <td>Eppendorf</td>
      <td>Cat#0030 108. 116</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1cc/50 mg Sep-Pak Vac tC18 cartridges</td>
      <td>Waters</td>
      <td>Cat#WAT054960,</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1.5 ml Diagenode sonicator tubes</td>
      <td>Diagenode</td>
      <td>Cat#C30010010</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>5 ml low protein binding centrifuge tubes</td>
      <td>Eppendorf</td>
      <td>Cat#0030 108.302</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>2 ml low protein binding centrifuge tubes</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#88379</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Graphite spin columns</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#88302</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Titansphere Phos-TiO Tips (200 ml/3 mg)</td>
      <td>GL Sciences Inc</td>
      <td>Cat#5010–21311</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>18 mm x 18 mm,1.5 mm thick high- performance coverslips</td>
      <td>Zeiss</td>
      <td>Cat#474030-9000-000</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cells and cell culture

MCF10A cells were purchased directly from the American Type Culture Collection (ATCC; LGC Standards), and HEK293 and Hs27 cells were from the European Collection of Authenticated Cell Lines (ECACC; Sigma- Aldrich, UK). Cells were cultured in 75 cm2 vented tissue culture flasks and incubated at 37°C in a humidified 5% CO2 atmosphere and passaged, using trypsin-EDTA solution (Sigma-Aldrich), prior to reaching confluence, typically every 2–4 days depending on the cell line. MCF10A cells were grown in MCF10A growth media as described by the Brugge lab (Debnath et al., 2003) consisting of 50:50 DMEM (Thermo Fisher Scientific, UK)/Ham's F-12 (Sigma-Aldrich) containing 5% (v/v) horse serum (Thermo Fisher Scientific), 20 ng/ml EGF (Peprotech, UK), 0.5 μg/ml hydrocortisone (Sigma-Aldrich), 100 ng/ml cholera toxin (Sigma-Aldrich) 10 μg/ml insulin (Sigma-Aldrich). Hs27 cells were cultured in Fibroblast growth medium (Promocell, UK). HEK293 and HEK293T cells were cultured in DMEM containing 10% (v/v) FBS (Sigma-Aldrich), 2 mM L-glutamine (Sigma-Aldrich). Cell lines were tested for the presence of Mycoplasma using commercially available kits (see Key Resources table).

For SILAC analysis, MCF10A cells were cultured for 14 days in modified MCF10A growth media containing 50:50 SILAC DMEM (Thermo Fisher Scientific): SILAC F12 (Thermo Fisher Scientific), 5% (v/v) dialyzed horse serum and other supplements described above. For heavy labeling, 50 μg/ml lysine +8 (Sigma-Aldrich), 40 μg/ml arginine +10 (Sigma-Aldrich), 200 μg/ml proline (Sigma-Aldrich) were added. For light labeling, 50 μg/ml lysine (Sigma-Aldrich) and 40 μg/ml arginine (Sigma-Aldrich) were added. Isotopic labeling was assessed by mass spectrometry, following in-gel tryptic digest. At the start of each experiment heavy amino acid incorporation was ≥93%.

### Plasmids and constructs

Amino acid (aa) numbering is based on the following sequences; PTPRK; UniProt ID: Q15262-3, PTPRM; UniProt ID: P28827-1. All point mutations were introduced by polymerase chain reaction (PCR) using either Q5 High-Fidelity DNA (New England Biolabs, UK) or Phusion Hot Start II DNA (Thermo Fisher Scientific) polymerases as per manufacturer’s protocol. The cDNA for the human PTPRK extracellular domain (ECD) of (aa 1–746) was synthesized with a C-terminal IgG1 tag fusion (GenScript, USA) and subcloned into the pRK vector (Genentech, USA). For transient mammalian expression, full-length human PTPRK coding expressing a N-terminal hemagglutinin (HA) tag and a C-terminal Flag tag was subcloned into the pRK vector. For stable integration with lentivirus infection, full length human PTPRK with and without a C-terminal BirA-R118G (BirA*)-Flag tag and truncated PTPRK (aa 1–785) with a C terminal BirA*-Flag tag were subcloned in-frame into pCW57.GFP.2A.MCS (a gift from Adam Karpf; #71783, Addgene, USA). For labeling nuclei, mApple with a C-terminal SV40 large T-antigen nuclear localization signal (PKKKRKV) was subcloned into the pLenti-puro vector (a gift from Ie-Ming Shih; #39481, Addgene). For bacterial expression, human coding sequences corresponding to PTPRK D1 (aa 864–1150) PTPRK D2 (aa 1150–1439), PTPRK intracellular domain (ICD; aa 864–1439), PTPRK ICD-C1089S, PTPRK ICD-D1057A, PTPRM D1(aa 877–1163), PTPRM ICD (aa 877–1452), PTPRK D1 (aa 864–1147)-BstBI-PTPRK D2 (aa 1150–1439), PTPRM D1 (aa 877–1159)-BstBI-PTPRM D2 (aa 1160–1452), PTPRK D1 (aa 864–1147)-BstBI-PTPRM D2 (aa 1160–1452), PTPRM D1 (aa 877–1159)-BstBI-PTPRK D2 (aa 1150–1439) were subcloned into a modified pET-15b bacterial expression vector in frame encoding an N-terminal His.TEV.AviTag (MGSSHHHHHHSSGVDLGTENLYFQGTGGLNDIFEAQKIEWHEGGGS).

The previously described Src and Grb2 mutant SH2 domains (Bian et al., 2016) were synthesized (Thermo Fisher Scientific) and subcloned into the same modified pET-15b bacterial expression vector by restriction digest.

### Antibody production

New Zealand White (NZW) Rabbits were purchased from Western Oregon Rabbit Company (WORC). Rabbits were housed and immunized in Josman, LLC. The guideline of the animal care was under regulation of the Institutional Animal Care and User Committee (IACUC) requirement. The immunization protocol was approved by Roche IACUC and Genentech Laboratory Animal Resources. New Zealand White (NZW) rabbits were immunized with murine PTPRK protein. Rabbit anti-PTPRK mAb were generated from an antigen-specific single B cell cultivation and cloning platform based on a modified protocol (Seeber et al., 2014). PTPRK+/IgG + single B cells were directly sorted into culture plates using flow cytometry. The B cell culture supernatants were collected for High-Throughput screening by ELISA for binding to murine PTPRK and an unrelated control protein. PTPRK-specific B cells were lysed and immediately frozen at −80°C until molecular cloning. Variable regions (VH and VL) of each monoclonal antibody from rabbit B cells were then cloned into expression vectors from extracted mRNA as previously described (Seeber et al., 2014). Individual recombinant rabbit antibodies were expressed in Expi293 cells and subsequently purified with protein A. Purified anti-PTPRK antibodies were then subjected to functional activity assays and kinetic screening. Lead clones were selected for large scale antibody production.

### Lipid-based transfection of siRNA duplexes

Cells were transfected with siRNA duplexes using lipofectamine RNAiMAX (Thermo Fisher Scientific). For a 6-well plate, 15 μl of 2 μM siRNA duplexes were added to 481 μl of serum/antibiotic-free OptiMEM (Thermo Fisher Scientific) and allowed to settle at RT for 5 min. 4 μl of lipofectamine RNAiMAX was then added, the mixture inverted briefly and incubated at RT for 20 min. Cells were seeded at 1.25–2.5 × 105 cells/ml in a 1 ml volume of complete growth medium, followed by immediate dropwise addition of the siRNA/lipofectamine mixture to give a final siRNA concentration of 20 nM. Cells were returned to the incubator after 30 min at RT. After 24 hr total incubation, media were replaced for complete growth medium. Cells were allowed to recover for 48–72 hr prior to treatment or processing for analysis. All siRNA duplexes where purchased from Dharmacon (Horizon Discovery, UK).

### CRISPR/Cas9 genome editing

Oligos for single guide RNAs targeting exons 1 and 2 of PTPRK were cloned into pspCas9.(BB).eGFP as previously described (Ran et al., 2013). MCF10A cells were transfected with plasmids using Lipofectamine LTX with PLUS Reagent as per manufacturer’s instructions (Thermo Fisher Scientific). After 48 hr eGFP positive cells were single-cell sorted using flow cytometry. Clones were expanded and protein levels assessed by Western blot. Targeted regions of the genome were amplified by PCR and sequenced to confirm editing.

### Lentivirus production and infection

15 × 106 HEK293T cells were seeded in 12 ml of complete growth medium/15 cm2 dish (two dishes per lentivirus) and incubated for 24 hr at 37°C with 5% CO2. Each 15 cm2 dish was then transfected with either 6 μg of pCW57.GFP.2A. or pLenti.puro expression plasmid encoding the desired construct, 12 μg of the psPAX2 packing plasmid (a gift from Didier Trono; #12260, Addgene) and 3 μg of the pMD2.G envelope plasmid (a gift from Didier Trono; #12259, Addgene) using the GeneJuice transfection reagent (Merck Millipore, UK) as per manufacturer’s instructions. After 24 hr media was then replaced with 16 ml complete growth medium. 48–72 hr post-transfection, culture medium was collected and filtered through a 0.45 μm mixed cellulose esters membrane. Viral particles were pelleted via ultracentrifugation at 100,000 x g for 1.5 hr at 4°C and resuspended in 600 μl of OptiMEM (Thermo Fisher Scientific). Lentivirus was aliquoted and stored at −80°C until required.

For lentiviral infections, 1.6 × 105 cells were seeded per well of a six well plate in 900 μl of growth medium, prior to the drop-wise addition of 100 μl lentivirus. After 30 min at room temperature (RT), cells were returned to the incubator. 72 hr later cells were reseeded in 0.4 μg/ml puromycin (Gibco, Thermo Fisher Scientific) selection medium.

### PTPRK extracellular domain screen

PTPRK ECD was expressed in HEK293S cells and purified using standard affinity chromatography procedures. Purified recombinant PTPRK ECD was screened as protein A microbeads complexes, carrying a Cy5-labeled IgG as an inert carrier to allow visualization of any binding partners against the Extracellular Protein Microarray Technology, as described previously (Martinez-Martin et al., 2016; Yeh et al., 2016). This platform (consisting of >1500 purified proteins, representing ≈50% of the single transmembrane-containing receptors in humans), in combination with a query protein multimerization approach for enhanced detection of binding partners, has enabled identification of multiple interactions between extracellular proteins (Martinez-Martin et al., 2016; Yeh et al., 2016), including low affinity interactions that often characterize receptors expressed on the cell surface (Martinez-Martin, 2017; Wright, 2009).

### Pervanadate treatment

Two × 106 cells were seeded per 10 cm2 dish and cultured for 6 days with a media change on day 3 and day 5. Cells were stimulated with 6 ml of complete growth medium containing 1 mM fresh sodium pervanadate (made as outlined below) for 30 min at 37°C/5% CO2. Cells were then transferred onto ice and washed twice with ice-cold PBS, prior to the addition of 600 μl of ice-cold lysis buffer (50 mM Tris-HCl pH 7.5, 150 mM NaCl, 10% (v/v) glycerol, 1% (v/v) triton X-100, 1 mM EDTA, 5 mM iodoacetamide, 1 mM sodium orthovanadate, 10 mM NaF, 1X EDTA-free protease inhibitors (Roche, UK)), and incubated on a rocker at 4°C in the dark. Lysates were harvested, followed by the addition of DTT to a final concentration of 10 mM and incubated for 15 min on ice. Lysates were cleared by centrifugation at 14000 x g for 15 min at 4°C and supernatants were transferred into fresh tubes. Pervanadate-treated cell lysates were then snap frozen and stored at −80°C until required.

To generate a 50 mM pervanadate working stock, 5 μl of 3% (w/v) H2O2 (Thermo Fisher Scientific) was diluted in 45 μl of 20 mM HEPES pH 7.3 prior to the addition of 490 μl of 100 mM Na3VO4 (Alfa Aesar, Thermo Fisher Scientific) and 440 μl of H2O, the solution was mixed by gentle inversion and incubated at RT for 5 min. After 5 min, a small amount of catalase (Sigma-Aldrich) was added to the pervanadate solution using a pipette tip and mixed by gentle inversion to quench unreacted H2O2. Freshly made pervanadate solution was used within 5 min to avoid decomposition of the complex.

### RT-qPCR

RNA was extracted using the RNeasy Plus Mini Kit (Qiagen, UK) according to the manufacturer’s instructions. cDNA was prepared using the High-Capacity cDNA Reverse Transcription Kit as per manufacturer’s instructions (Applied Biosystems). RT-qPCR was performed using the TaqMan Universal Master Mix II (Applied Biosystems, Thermo Fisher Scientific), 50 ng cDNA and specific Taqman probes for PTPRK, PTPRM, PTPRT, PTPRU and RPL19 Real-time PCR was performed with the 7900HT Fast Real-Time PCR System (Thermo Fisher Scientific). Expression levels were normalized to the reference gene RPL19. Gene specific primers are listed in the Key Resources table.

### SDS-PAGE and immunoblotting

SDS PAGE and immunoblotting were carried out as previously described (Fearnley et al., 2015). 25–50 μg of cell lysate was resuspended in an appropriate volume of 5X SDS-PAGE sample buffer (0.25 M Tris-HCl pH 6.8, 10% (w/v) SDS, 20% (v/v) glycerol, 0.1% (w/v) bromophenol blue, 10% (v/v) β-mercaptoethanol) and incubated at 92°C for 5 min. Samples were run on a 8, 10 or 12% (v/v) SDS-polyacrylamide resolving gel with a 5% (v/v) SDS-PAGE stacking gel and subjected to electrophoresis at 120–130 V for ~1–2 hr in 25 mM Tris, 190 mM glycine, 0.1% (w/v) SDS. Proteins were transferred onto 0.2 µm reinforced nitrocellulose membranes (GE Healthcare) at 300 mA for 3–4 hr at 4°C in 25 mM Tris, 190 mM glycine, 20% (v/v) methanol. Membranes were briefly rinsed in TBS-T (20 mM Tris pH 7.6, 137 mM NaCl, 0.1% (v/v) Tween-20) prior to incubation for 20–60 min in 5% (w/v) skimmed milk/TBS-T to block non-specific antibody binding. The blocking solution was removed and membranes rinsed in TBS-T prior to primary antibody incubation (4–5 hr at RT or overnight at 4°C). Membranes were then subjected to 3 × 10 min washes in TBS-T, prior to incubation with HRP-conjugated species-specific anti-IgG antibodies (1–2 hr at RT). Membranes were then subjected to 3 × 10 min washes in TBS-T, prior to being incubated with combined EZ-ECL solution (Geneflow, UK) and imaged using a Bio-Rad ChemiDoc MP imaging system.

### Expression, biotinylation (AviTag) and purification of recombinant proteins

Escherichia coli BL21(DE3) Rosetta cells transformed with the relevant expression construct were cultured at 30°C/220 rpm in 1 l of 2XTY medium containing 50 μg/ml carbenicillin and 34 μg/ml chloramphenicol until the OD600 reached 0.6–0.7. Cultures were then transferred to 20°C/220 rpm and allowed to equilibrate, prior to the addition of 1 mM isopropyl-thio-β-D-galactopyranoside (IPTG; Generon, UK) and 200 μM of D-biotin (Sigma-Aldrich). Cells were harvested after 20 hr by centrifugation at 4000 x g for 30 min and bacterial pellets stored at −20°C until required. Prior to lysis, cells were subjected to one round of freeze-thaw. Cells were lysed in purification buffer (50 mM HEPES pH 7.5 for PTP domains (50 mM Tris pH 7.4 for SH2 domain mutants), 500 mM NaCl, 5% (v/v) glycerol and 0.5 mM TCEP), containing EDTA-free protease inhibitor tablets (Roche) using a Constant Systems cell disruptor and the cell extract was clarified via centrifugation at 40000 x g for 30 min at 4°C. The supernatant was removed and incubated with 0.5 ml of Ni-NTA agarose (Qiagen) for 1 hr at 4°C. Ni-NTA Agarose was then pelleted via centrifugation at 500 x g for 5 min at 4°C and packed into a gravity flow column. Ni-NTA agarose was then washed with 10 volumes of purification buffer containing 5 mM imidazole, followed by 20 volumes of purification buffer containing 20 mM imidazole; prior to elution in purification buffer containing 250 mM imidazole. The eluted protein was then subjected to size exclusion chromatography (SEC) using a Superdex 200 16/600 column (GE Healthcare Life Sciences, Thermo Fisher Scientific) for PTP domains or Superdex 75 16/600 column (GE Healthcare Life Sciences, Thermo Fisher Scientific) for SH2 mutant domains. Columns were equilibrated in SEC buffer (50 mM HEPES pH 7.5 (50 mM Tris pH 7.4 for SH2 domains), 150 mM NaCl, 5% (v/v) glycerol, 5 mM DTT). Protein was concentrated to 2–10 mg/ml using an Ultracel-3K, Ultracel-10 K or Ultracel-30 K regenerated cellulose centrifugal filter (Merck Millipore), prior to snap-freezing and storage at −80°C until required. The purified protein was assessed by SDS-PAGE and staining with InstantBlue (Expedeon, UK).

### Confirmation of AviTag biotinylation via streptavidin gel shift assay

Biotinylated recombinant proteins (2–10 μg) were solubilized in 4 μl of 5X SDS-PAGE sample buffer and incubated at 95°C for 5 min. Samples were then cooled to RT and allowed to equilibrate for 5 min. 24 μl of 2 mg/ml streptavidin/PBS (approx. 5-fold molar excess) was then added and the mixture was incubated at RT for 5 min. Samples were then run on a NuPAGE 4–12% Bis-Tris gel (Thermo Fisher Scientific) in NuPAGE MES (2-ethanesulfonic acid) gel running buffer (Thermo Fisher Scientific) at 190 V for 30 min. Protein only and streptavidin only controls should be included. Proteins were then visualized via staining with InstantBlue (Expedeon) for 1 hr at RT. Gels were imaged using a Bio-Rad ChemiDoc MP imaging system and the percentage of biotinylated protein determined via 2D-densitometry using Fiji (Schindelin et al., 2012).

### Recombinant protein pull downs

25–50 μg (tandem or single domain, respectively) of biotinylated His.TEV.Avi.PTPx domains were conjugated to 167 μl of pre-washed streptavidin-coated magnetic beads suspension (4 mg/ml; New England Biolabs) in 500 μl of ice-cold size exclusion buffer (50 mM HEPES pH 7.5 (50 mM Tris pH 7.4 for SH2 domains), 150 mM NaCl, 5% (v/v) glycerol, 5 mM DTT) at 4°C for 1–2 hr on a rotator. A beads-only control was treated identically. Samples were briefly spun, transferred onto a magnetic stand and washed 3 times with 1 ml of ice-cold size exclusion buffer, followed by two washes with 1 ml of ice-cold 150 mM NaCl wash buffer (20 mM Tris-HCl pH 7.4, 150 mM NaCl, 10% (v/v) glycerol, 1% (v/v) triton X-100, 1 mM EDTA pH 8.0). Conjugated PTP domains were then blocked in 1 ml of ice-cold 5% (w/v) BSA in 150 mM NaCl wash buffer containing 1x EDTA-free protease inhibitors (Roche) at 4°C for 1 hr on a rotator. Simultaneously, freshly thawed pervanadate-treated cell lysate was then pre-cleared with streptavidin-coated magnetic beads (167 μl of bead suspension (4 mg/ml) per ml of lysate) at 4°C for 1 hr on a rotator. Blocked conjugated PTPx domains were then briefly spun, transferred onto a magnetic stand and washed twice with 1 ml of ice-cold 150 mM NaCl wash buffer; prior to incubation with 1 ml of 1 mg/ml pre-cleared pervandate-treated lysate at 4°C on for 1.5 hr on a rotator. In a cold room, beads were pulled to a magnet and supernatant removed. Beads were then washed twice in 1 ml ice-cold 150 mM NaCl wash buffer including a brief spin and separation by magnet. Beads were then washed once with 1 ml ice-cold 150 mM NaCl wash buffer without resuspension and washed twice more in 1 ml ice-cold 150 mM NaCl wash buffer with resuspension. Next beads were washed once without resuspension and twice with resuspension in 1 ml ice-cold 500 mM NaCl wash buffer (20 mM Tris-HCl pH 7.4, 150 mM NaCl, 10% (v/v) glycerol, 1% (v/v) triton X-100, 1 mM EDTA pH 8.0). Finally, beads were washed once without resuspension and once with resuspension in 1 ml ice-cold TBS (20 mM Tris pH 7.6, 137 mM NaCl). For immunoblot analysis, beads were resuspended in 20 μl of 18% (v/v) formamide,1 mM EDTA pH 8.0 made up in TBS, incubated at 95°C for 5 min, followed by addition of 30 μl of 5x SDS-PAGE sample buffer containing 2 mM biotin and incubated at 95°C for 10 min. After a brief spin, beads were separated by magnet and supernatants subjected to SDS-PAGE. For analysis by mass spectrometry, beads were subject to two further washes without resuspension and one further wash with resuspension in 1 ml ice-cold 50 mM ammonium bicarbonate pH 8.0, followed by on-bead tryptic digest.

### On-bead tryptic digest

Streptavidin beads for tryptic digest were resuspended in 95 μl of 50 mM ammonium bicarbonate pH 8.0, prior to the addition of 5 μl of 100 mM DTT (5 mM final DTT concentration), and incubation at 56°C for 30 min. 10 μl of 154 mM iodoacetamide (IAA) was then added (14 mM final IAA concentration) and samples incubated in the dark at RT for 20 min. Unreacted IAA was then quenched by the addition of 7 μl of 100 mM DTT (10 mM final DTT concentration), and incubation at RT for 15 min. Next, 31.5 μl of 50 mM ammonium bicarbonate pH 8.0 and 1.5 μl of LysC (0.005 AU/μl; Wako) was added to each sample, followed by incubation at RT for 3 hr with shaking. 150 μl of 7.7 ng/μl trypsin (Thermo Fisher Scientific) in 50 mM ammonium bicarbonate pH 8.0) was added to each sample (3.84 ng/μl final trypsin concentration) and incubate at 37°C overnight with shaking. An additional 150 μl of 7.7 ng/μl trypsin was then added to each sample (5.1 ng/μl final trypsin concentration), followed by incubation at 37°C for 2 hr with shaking. Samples were briefly spun and placed onto a magnetic stand, supernatant was then transferred into a low protein-binding tube (Eppendorf, Thermo Fisher Scientific). Beads were then washed twice with 150 μl of proteomics grade water (Thermo Fisher Scientific) and resulting supernatants added to the first supernatant. Samples were then centrifuged at 18400 x g for 10 min at 4°C and supernatant transferred into a new low protein-binding tube. Samples were then adjusted to 1% (v/v) TFA, prior to centrifugation at 21000 x g for 10 min at 4°C and supernatants transferred into a new low protein-binding tube. Each tryptic digest was desalted using a 1cc/50 mg Sep-Pak C18 cartridge (Waters). All buffers were made using proteomics grade water. Sep-Paks were equilibrated via washing with twice with 1 ml 100% (v/v) acetonitrile (AcN; VWR), twice with 1 ml 50% (v/v) AcN/0.1% (v/v) TFA and twice with 1 ml 0.1% (v/v) TFA. Samples were then slowly loaded onto each Sep-Pak; flow-through was reapplied once. Sep-Paks were then washed three times with 1 ml 0.1% (v/v) TFA. Peptides were then eluted into a new low protein-binding tube by addition of two 350 μl volumes of 50% (v/v) AcN/0.1% (v/v) TFA. Peptide samples were then dried down using a vacuum centrifuge (Concentrator 5301, Eppendorf) at 30–45°C. Peptide pellets were then stored at −20°C until further processing.

### Mass spectrometry acquisition and data analysis for pull downs

LC-MS/MS data were acquired on either a Q Exactive (Thermo Fisher Scientific) or a Q Exactive Plus (Thermo Fisher Scientific) each coupled, via an EASYspray source, to an RSLC3000 nanoUHPLC. Peptides were loaded onto a 100 µm ID x 2 cm Acclaim PepMap nanoViper precolumn (Thermo Fisher Scientific) and resolved using a 75 µm ID x 50 cm, 2 µm particle PepMap RSLC C18 EASYspray column at 40°C. NanoUHPLCs were operated with solvent A (0.1% formic acid) and solvent B (80% MeCN, 0.1% formic acid). Peptides were resolved on the Q Exactive by a gradient rising from 3% to 40% B by 60 mins and on the Q Exactive Plus by a gradient ring from 10% to 40% B by 57 min. MS spectra on the Q Exactive were acquired between m/z 400 to 1400 and between m/z 400 to 1500 on the Q Exactive Plus. Both operated MS/MS triggered in a top 10 DDA fashion.

Raw files were processed on MaxQuant v.1.5.2.8 or 1.5.8.3. using default settings. Quantification was carried out using Perseus ver. 1.5.8.5 (Tyanova et al., 2016). For label-free quantification (LFQ), LFQ intensities from MaxQuant were log2(x) transformed prior to filtering out proteins branded as identified only by site, reverse or potential contaminants. Proteins were then further filtered out based on the minimum number of valid values in one group, to be stringent we required a minimum of three (MCF10A experiments) or two (Hs27 experiments) valid values. Missing values were then imputed from the normal distribution and statistical significance was calculated via a two-sample, two-sided t test performed with truncation by a permutation-based FDR (threshold value 0.05). High confidence interactors were defined as >2 fold enrichment (over beads only), significant (p>0.05) and a CRAPome score ≤137 (Mellacheruvu et al., 2013).

### pNPP phosphatase activity assay

All buffers were made in phosphate-free H2O (Thermo Fisher Scientific). Recombinant phosphatase was added to a 96-well plate in a total volume of 50 μl reaction buffer (50 mM HEPES pH 7.4, 150 mM NaCl, 5% (v/v) glycerol, 5 mM DTT). 50 μl of reaction buffer containing 20 mM pNPP (New England Biolabs) was then added and the plate was incubated at RT for 3–15 min. Reactions were stopped by the addition of 50 μl 0.58 M NaOH (0.193 final concentration) and the absorbance read at 405 nm using a 96-well plate reader (SpectraMax M5, Molecular Devices, UK).

### BIOMOL green phosphatase activity assay

All buffers were made in phosphate-free water (Thermo Fisher Scientific). In a 96-well plate, 30 μl of reaction buffer containing 100 μM each of DADE-pTyr-LIPQQG-Acid phosphopeptide and END-pTyr-INASL-Acid phosphopeptides (Cambridge Research Biochemicals) was incubated at 30°C for 3 min, prior to the addition of recombinant phosphatase in a total volume of 20 μl reaction buffer. The assay was then incubated at RT for 2.5–3.5 min. Reaction was stopped by the addition of 100 μl of BIOMOL Green reagent (ENZO, UK), followed by incubation at RT for 15–30 min. The absorbance was then read at 620 nm using a 96-well plate reader (SpectraMax M5, Molecular Devices). Enzyme activity was compared against a standard curve from serial dilutions of a phosphate standard (ENZO).

### Quantitative tyrosine phosphoproteomics and total proteomics

2 × 106 WT or PTPRK-KO SILAC labeled MCF10A cells were seeded into three 10 cm2 dishes in heavy (WT) or light (PTPRK-KO) SILAC medium for each experiment. Cells were cultured for 7 days with a media change on days 2 (10 ml), 4 (12 ml), 5 (12 ml) and 6 (12 ml). On day 7, cells were placed on ice, washed twice with ice-cold PBS and lysed in 150 μl of 6M guanidine (Thermo Fisher Scientific) in 50 mM EPPS pH 8.5 (Alfa Aesar) with 1X EDTA-free protease inhibitor cocktail (Roche) and 1X phosphatase inhibitor cocktail (Roche). Samples were transferred into Diagenode sonication tubes (Diagenode, UK) on ice, vortexed at max speed for 30 s and sonicated at 4°C on high power for 5 × 30 s pulses using a water bath sonicator (Bioruptor, Diagenode). Samples were cleared twice by centrifugation at 13000 x g for 10 min at 4°C with supernatants transferred to new low protein-binding tubes (Eppendorf). Protein concentration was then determined by BCA assay and equal amounts of heavy and light labeled protein lysates were transferred into 5 ml low protein-binding tubes (Eppendorf) to give a maximum combined volume of 600 μl. A total of 10 mg of protein from heavy and light lysates was processed per replicate. Proteins were reduced by addition of 30 μl DTT/200 mM EPPS pH 8.5 (5 mM final DTT concentration), vortexed and incubated at RT for 20 min. Proteins were then alkylated by addition of 16.8 μl of 500 mM IAA/200 mM EPPS pH 8.5 (14 mM final IAA concentration), vortexed and incubated at RT for 20 min in the dark. Unreacted IAA was quenched via the addition of 30 μl of freshly thawed 100 mM DTT/200 mM EPPS pH 8.5 (8.9 mM final DTT concentration), prior to vortexing and incubation at RT for 15 min. Samples were diluted to a final concentration of 1.5 M guanidine by addition of 1.8 ml 200 mM EPPS pH 8.5. Next, 0.06 AU of LysC (Wako) was added to each sample, prior to vortexing and incubation at RT for 3 hr with shaking. Samples were split in half and transferred to two new 5 ml low protein-binding tubes. Samples were diluted to a final concentration of 0.5 M Guanidine by adding 2.48 ml 200 mM EPPS pH 8.5. 100 μl of 124 ng/μl Trypsin (Thermo Fisher Scientific)/EPPS pH 8.5 was then added to each sample, prior to vortexing and incubation at 37°C overnight with shaking. An additional 100 μl of 124 ng/μl Trypsin/EPPS pH 8.5 was then added, prior to vortexing and incubation at 37°C for 2 hr with shaking. Tryptic digests were then acidified via the addition of 39.8 μl TFA (Thermo Fisher Scientific) or 1% (v/v) TFA final concentration. Samples were then split into two new 2 ml low protein-binding tubes (Thermo Fisher Scientific), prior to centrifugation at 21000 x g for 10 min. Supernatants were transferred to a new 2 ml low protein-binding tubes, prior to being snap-frozen and stored at −80°C or desalted. Tryptic digests were desalted using 1cc/50 mg Sep-Pak Vac tC18 cartridges (Waters, UK); 20 mg/~40 ml of tryptic digest was split across four 1cc/50 mg Sep-Pak Vac tC18 cartridges. Sep-Paks were equilibrate, washed and loaded as described above. Peptides were eluted in a stepwise manner into new 1.5 ml low protein -binding tubes. Fraction 1: 350 μl 12.5% (v/v) AcN/0.1% (v/v) TFA, Fraction 2: 350 μl 25% (v/v) AcN/0.1% (v/v) TFA, Fraction 3: 350 μl 37.5% (v/v) AcN/0.1% (v/v) TFA, Fraction 4: 350 μl 50% (v/v) AcN/0.1% (v/v) TFA. Corresponding fractions were then pooled and 10% (v/v) removed for total proteome analysis. Peptides were then dried down using a vacuum centrifuge (Concentrator 5301, Eppendorf) at 45°C and stored at −20°C until further processing.

For phospho-tyrosine enrichment, peptide fractions were resuspended in 400 μl of ice-cold IAP buffer (50 mM Tris-HCL pH 7.4, 10 mM Na2HPO4 (Acros Organics), 100 mM NaCl) and incubated for 10 min on ice. Added to each fraction was 10 μl of rabbit anti-pY-1000 antibody (Cell Signal Technologies, New England Biolabs) pre-conjugated to 5 μl of protein G agarose bead suspension (Merck Millipore) and 2.4 μg each of biotinylated Src and Grb2 SH2 mutant domains, pre-conjugated to 5 μl of streptavidin agarose bead suspension (Thermo Fisher Scientific) and ice-cold IAP buffer up to 1 ml. Samples were then incubated at 4°C for 16–24 hr on a rotator. Beads were pelleted via at 14000 x g for 30 s and washed three times with 1 ml ice-cold IAP buffer followed by two washes with 1 ml ice-cold proteomics grade water. Peptides from each fraction were eluted in 125 μl of 0.15% (v/v) TFA at RT for 15 min; beads were pelleted and the supernatant transferred to a new 1.5 ml low protein binding tube (Eppendorf). This step was repeated for a total of three elutions and supernatants combined. Eluted peptides were then desalted using graphite spin columns (Thermo Fisher Scientific), according to manufacturer’s instructions, using two columns per fraction, and dried down using a vacuum centrifuge at 45°C. For further enrichment of phospho-peptides using TiO2, peptide fractions were resuspended in 100 μl 2% (v/v) TFA and incubated at RT for 10 min. Each fraction was then split and processed on two Titansphere Phos-TiO Tips (200 μl/3 mg; GL Sciences Inc) as per manufacturer’s instructions. Peptides were eluted in 50 μl of 5% (w/v) NH4OH (35% w/v; Acros Organics, Thermo Fisher Scientific), followed by 50 μl of 60% (v/v) AcN. Peptide samples were then dried down using a vacuum centrifuge at 45°C, prior to storage at −20°C or −80°C before analysis by mass spectrometry.

### Mass spectrometry acquisition and data analysis for quantitative tyrosine phosphoproteomics and total proteomics

Samples were resuspended in 20 μL sample solution (3% MeCN, 0.1% trifluroacetic acid). LC-MS/MS data acquisition was performed on a Q Exactive Plus and an Orbitrap Fusion Lumos (Thermo Fisher Scientific) with both instruments configured to RSLC3000 nanoUHPLCs. Both the Q Exactive Plus and the Fusion Lumos were operated with an EASYspray source using a 50 cm PepMap EASYspray emitter at 40°C. The Fusion Lumos was also operated using a 75 cm Acclaim PepMap column at 55°C with SilicaTip coated emitters (New Objective, USA). All nanoHPLCs were operated with solvent A (0.1% formic acid) and solvent B (80% MeCN, 0.1% formic acid).

Total peptides were resolved using four different gradients. Gradient 1 (for sample fraction 1) rose from 3% to 15% solvent B by 125 min and 40% B by 175 min. Gradient 2 (for sample fraction 2) rose from 3% to 25% B by 125 min and 40% B by 175 min. Gradient 3 (for sample fraction 3) rose from 3% to 40% B by 175 min and gradient 4 (for sample fraction 4) rose from 12% to 58% B by 175 min.

Phosphopeptides were resolved using four different gradients. Gradient 1 (for sample fraction 1) rose from 3% to 15% solvent B by 70 min and 40% B by 95 min. Gradient 2 (for sample fraction 2) rose from 3% to 25% B by 80 min and 40% B by 95 min. Gradient 3 (for sample fraction 3) rose from 10% to 40% B by 95 min and gradient 4 (for sample fraction 4) rose from 15% to 50% B by 95 min. MS/MS data on the Q Exactive Plus were acquired in a Top10 DDA fashion and on the Fusion Lumos MS/MS data were acquired in the ion trap using a 3 s cycle.

Data were processed using MaxQuant v.1.6.2.3 with a Uniprot Homo sapiens database (downloaded 28/1/2018). Variable modifications were set as oxidation (M), acetylation (protein N-terminus) and phospho (STY) with ‘re-quantify’ and ‘match between runs’ enabled. Peptide and protein FDR were set to 0.01. Quantification was carried out using Perseus ver. 1.5.8.5 (Tyanova et al., 2016). Normalized H/L ratios from MaxQuant were log2(x) transformed prior to filtering out proteins labeled as identified only by site or reverse. Proteins were then further filtered out based on the minimum number of valid values; a minimum of two valid values were required for high confidence analysis. Missing values were then imputed from the normal distribution and log2(x) transformed normalized H/L SILAC ratios were inverted, prior to averaging. Statistical significance was calculated via a one-sample, two-sided t test performed with truncation by a Benjamini Hochberg FDR (threshold value 0.05).

### Identification of cellular interactors using BioID

4 × 106 WT MCF10A cells stably transduced with pCW57.tGFP, pCW57.tGFP.P2A.PTPRK.C1089S-BirA*-FLAG or pCW57.tGFP.P2A.PTPRK.1–785.BirA*-FLAG were seeded into 10 cm2 dishes (three per condition). 24 hr after seeding, media was changed and doxycycline was added at 500 ng/ml for PTPRK.C1089S-BirA*-FLAG and tGFP, and 150 ng/ml for PTPRK.1–785-BirA*-FLAG. On the fourth day, doxycycline containing media was replaced and supplemented with 50 μM biotin (Sigma-Aldrich). After 24 hr, cells were lysed in 600 μl RIPA buffer (50 mM Tris–HCl pH 7.5, 150 mM NaCl, 1% (v/v) NP-40, 0.5% (w/v) sodium deoxycholate, 1 mM EDTA, 0.2% (w/v) SDS) and complete protease inhibitor cocktail (Roche). Cell lysates were then sonicated and clarified at 16500 x g for 10 min at 4°C. Equal amounts (3–4 mg) of lysate were transferred into 1.5 ml tubes which contained 50 μl of streptavidin agarose bead suspension (Thermo Fisher Scientific) that had previously been washed in RIPA buffer. Samples were then made up to 1 ml total volume in RIPA buffer and incubated at 4°C on a rotator overnight. Beads were pelleted at 14000 x g for 30 s at 4°C, supernatant removed and beads washed once with 1 ml 2% (w/v) SDS in PBS, followed by two washes with 1 ml 50 mM NaCl, 1% (v/v) NP-40, 50 mM Tris pH 7.5% and 0.2% (w/v) SDS including 8 min incubations on a rotator at RT. Proteins were eluted by incubation at 92°C in SDS sample buffer supplemented with 3 mM biotin for 10 min, prior to immunoblot analysis.

### In lysate dephosphorylation assay

All steps were performed on ice unless indicated. Each recombinant phosphatase domain was added to a total volume of 342 μl ice-cold 150 mM NaCl wash buffer to which 50 μl (200 μg) of freshly thawed pervanadate-treated cell lysate was added. Samples were mixed by gentle inversion and reactions were then incubated for 1.5 hr at 4°C on a rotator. 8 μl of 20% (w/v) SDS was then added (0.4% (w/v) final SDS concentration), samples were vortexed and incubated for 5–10 min. Samples were then diluted with 400 μl ice-cold 150 mM NaCl wash buffer to 0.2% (w/v) SDS final concentration and vortexed; prior to the addition of 5 μl of rabbit-anti-phospho-tyrosine antibody (Cell Signaling Technology). Samples were then incubated for 2–4 hr at 4°C on a rotator. 40 μl of washed protein G agarose bead suspension (Merck Millipore) was then added, prior to incubation overnight at 4°C on a rotator. Beads were pelleted at 15000 x g for 30 s at 4°C and washed five times in 1 ml of ice-cold 150 mM NaCl wash buffer. After the final wash, beads were transferred to RT and resuspended in SDS-PAGE sample buffer and incubated at 92°C for 10 min. Beads were pelleted at 15000 x g for 30 s and the supernatant transferred into a new microfuge tube. Samples were stored at −20°C prior to SDS-PAGE and immunoblot analysis.

### Protein structure presentation and homology modeling

All manipulations and homology modeling based on existing structures were performed using University of California San Francisco (UCSF) Chimera (Pettersen et al., 2004).

### Immunostaining MCF10A monolayers

5 × 105 cells were seeded in 3 ml of complete growth medium on 18 mm x 18 mm,1.5 mm thick high-performance coverslips (Zeiss, UK). Cells were cultured for 6 days, with a media change on day 3, and then every day thereafter. On day 6, media was removed and cells fixed in 500 μl of methanol-free 4% (w/v) para-formaldehyde (PFA; Thermo Fisher Scientific) in PBS for 10 min at RT. Coverslips were then rinsed with 5 × 500 μl of PBS, followed by permeabilization in 500 μl of 0.5% (v/v) triton X-100, 3% (w/v) BSA in PBS for 2 min at room temperature and blocking in 1 ml of 0.2% (v/v) triton X-100, 3% (w/v) BSA in PBS for 1 hr at RT. Coverslips were then incubated with primary antibody (1:100 dilution) for 1–5 hr at RT. followed by five 500 μl 5 min washes with 0.2% (v/v) triton X-100, 3% (w/v) BSA in PBS. Coverslips were then incubated with species-specific fluorophore- conjugated anti-IgG antibodies (1:250 dilution) containing Hoechst 33342 (1:2000; Thermo Fisher Scientific) with or without BODIPY 558/568 phalloidin (1:250; Thermo Fisher Scientific), for 45–60 min at RT in the dark. Coverslips were then rinsed twice with 500 μl 0.2% (v/v) triton X-100, 3% (w/v) BSA in PBS, followed by three 500 μl washes (5 min) with PBS. Coverslips were then mounted onto 1.0 mm thick slides using ProLong Gold antifade (Thermo Fisher Scientific). Slides were imaged using either a LSM880 confocal, LSM710 confocal, Elyra PS1 Super resolution or an AxioImager Z2 microscope (Zeiss).

### MCF10A spheroid cultures and immunostaining

MCF10As were cultured as spheroids following the previously described ‘3D on-top’ method (Lee et al., 2007). 96-well plates were chilled for 30 min in the fridge before use. 15 μl Matrigel (Corning, Thermo Fisher Scientific), was spread evenly on the bottom of each well and allowed to set at 37°C for 20 min. 5 × 103 MCF10A cells per well were resuspended in MCF10A growth media and layered on top of the matrix and incubated for 20 min. 30 μl MCF10A growth media containing 10% (v/v) Matrigel was then added on top of the cells. Media was replaced with 30 μl complete growth media and 2% (v/v) Matrigel every 2–3 days for 7 days and then switched to EGF-free MCF10A growth media and 2% (v/v) Matrigel for 7 days. Acini were imaged at 10x magnification on day 14, using the EVOS FL Cell Imaging System (Thermo Fisher Scientific).

Spheroids were extracted from Matrigel as previously described (Lee et al., 2007). Media was aspirated and wells washed twice with PBS. Spheroids were extracted using 5 mM EDTA in PBS and gentle shaking for 30 min. Spheroids were then briefly centrifuged at 115 x g and the majority of supernatant aspirated. The remaining supernatant was used to resuspend the spheroids prior to transferring them onto a glass slide. Spheroids were fixed in 4% (v/v) paraformaldehyde (Thermo Fisher Scientific) for 20 min at RT and then permeabilized with 0.5% (v/v) Triton X-100 for 10 min at 4°C. The fixed spheroids were then washed three times in 100 mM glycine in PBS with 10 min per wash. Next, the spheroids were blocked in IF buffer (0.1% (w/v) BSA; 0.2% (v/v) Triton X-100; 0.05% (v/v) Tween-20) with 10% (v/v) normal serum block (BioLegend, USA) for 60 min at RT. Primary antibody was incubated overnight at 4°C then washed three times with IF buffer. Secondary antibody was incubated for 45 min at RT. The spheroids were then washed once with IF buffer for 20 min, followed by two subsequent washes with PBS for 10 min each. They were then mounted with Prolong Gold Antifade Mounting medium (Thermo Fisher Scientific) and imaged using an LSM880 confocal or an AxioImager Z2 microscope (Zeiss).

### Quantification of confocal microscopy images

For immunostained cell monolayers, five random fields were imaged per condition and the results averaged. Image analysis was carried out using Fiji. The Pearson correlation coefficient for two images was determined using the Coloc2 plugin; whilst the fluorescence intensity of an image was analyzed using a custom macro: run(‘Auto Threshold’, ‘method = Default ignore_black white’); run(‘Set Measurements...‘, ‘integrated limit display redirect = None decimal = 3’); run(‘Measure’).

For spheroids, aberrant spheroids were quantified using bright field images of 6 independent wells of WT and PTPRK KO MCF10A spheroids. three non-overlapping images from each well were manually counted for aberrant spheroids. Spheroid diameter was calculated using the circle measurement tool in Zen Pro (Zeiss). A circle was traced around individual spheroids in whole slide images for WT and PTPRK KO MCF10A spheroids using the Hoechst channel.

### BrdU incorporation ELISA

In a 96-well plate, 1 × 104 MCF10A cells per well were seeded in 90 μl of complete growth medium and cultured for 2 days. A final concentration of 10 μM bromodeoxyuridine (BrdU) was added to each well and left to incorporate for 2 hr. A BrdU-based cell proliferation ELISA was then performed according to manufacturer’s instructions (Roche, Germany). Absorbance was measured at 370 nm (reference wavelength 492 nm) using a 96-well plate reader (SpectraMax M5, Molecular Devices).

### Trans-epithelial electrical resistance (TEER)

5 × 105 cells were seeded in 500 μl of complete growth medium onto the apical side of a 0.4 μm pore size Transwell filter (Corning) inserted into a 24-well companion plate containing (Corning) 500 μl of complete growth medium. Cells were cultured for 6–7 days to allow formation of a complete monolayer, with a media change day three and then every day thereafter. Growth medium was replaced 24 hr prior to TEER assessment; 5–10 readings were taken using a Millicell ERS-2 Volt/Ohm meter (Merck Millipore) and a mean was calculated. TEER value was calculated as follows: (Sample average TEER measurement (Ω) – Blank average TEER measurement (Ω)) x Trans-well surface area (0.3 cm2).

### Fluorescein isothiocyanate (FITC)-dextran cell permeability assay

Cells were seeded on the apical side of transwell filters as described for TEER experiments. Growth medium was replaced 24 hr prior the addition of 250 kDa-FITC-dextran (3 mg/ml final concentration; Sigma-Aldrich) to the apical side of the insert; cells were then incubated for 24 hr. After 24 hr inserts were removed and the basal media was mixed by gentle pipetting. Per condition, 4 × 100 μl samples were transfer into a 96-well plate and the fluorescence intensity was measured using a 96-well plate fluorimeter (SpectraMax M5, Molecular Devices) at excitation 494 nm and emission at 515 nm.

### Accession codes

The mass spectrometry proteomics data have been deposited to the ProteomeXchange Consortium via the PRIDE partner repository (Vizcaíno et al., 2016) with the dataset identifier PXD013055.
