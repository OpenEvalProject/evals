# Modular metabolite assembly in Caenorhabditis elegans depends on carboxylesterases and formation of lysosome-related organelles

## Authors

- Henry H Le<sup>1</sup> ([ORCID: 0000-0003-2942-2357](https://orcid.org/0000-0003-2942-2357))
- Chester JJ Wrobel<sup>1</sup>
- Sarah M Cohen<sup>2</sup>
- Jingfang Yu<sup>1</sup> ([ORCID: 0000-0003-1770-5368](https://orcid.org/0000-0003-1770-5368))
- Heenam Park<sup>2</sup>
- Maximilian J Helf<sup>1</sup>
- Brian J Curtis<sup>1</sup>
- Joseph C Kruempel<sup>3</sup>
- Pedro Reis Rodrigues<sup>1</sup>
- Patrick J Hu<sup>4</sup>
- Paul W Sternberg<sup>2</sup> ([ORCID: 0000-0002-7699-0173](https://orcid.org/0000-0002-7699-0173)) †
- Frank C Schroeder<sup>1</sup> ([ORCID: 0000-0002-4420-0237](https://orcid.org/0000-0002-4420-0237)) †

### Affiliations

1. Boyce Thompson Institute and Department of Chemistry and Chemical Biology, Cornell University Ithaca United States
2. Division of Biology and Biological Engineering, California Institute of Technology Pasadena United States
3. Department of Molecular and Integrative Physiology, University of Michigan Medical School Ann Arbor United States
4. Departments of Medicine and Cell and Developmental Biology, Vanderbilt University School of Medicine Nashville United States

† Corresponding author

## Abstract

Signaling molecules derived from attachment of diverse metabolic building blocks to ascarosides play a central role in the life history of C. elegans and other nematodes; however, many aspects of their biogenesis remain unclear. Using comparative metabolomics, we show that a pathway mediating formation of intestinal lysosome-related organelles (LROs) is required for biosynthesis of most modular ascarosides as well as previously undescribed modular glucosides. Similar to modular ascarosides, the modular glucosides are derived from highly selective assembly of moieties from nucleoside, amino acid, neurotransmitter, and lipid metabolism, suggesting that modular glucosides, like the ascarosides, may serve signaling functions. We further show that carboxylesterases that localize to intestinal organelles are required for the assembly of both modular ascarosides and glucosides via ester and amide linkages. Further exploration of LRO function and carboxylesterase homologs in C. elegans and other animals may reveal additional new compound families and signaling paradigms.

## Introduction

Recent studies indicate that the metabolomes of animals, from model systems such as Caenorhabditis elegans and Drosophila to humans, may include >100,000 of compounds (da Silva et al., 2015; Artyukhin et al., 2018). The structures and functions of most of these small molecules have not been identified, representing a largely untapped reservoir of chemical diversity and bioactivities. In C. elegans (Girard et al., 2007), a large modular library of small-molecule signals, the ascarosides, are involved in almost every aspect of its life history, including aging, development, and behavior (Schroeder, 2015; Butcher, 2017; Butcher et al., 2007; Jeong et al., 2005). The ascarosides represent a structurally diverse chemical language, derived from glycosides of the dideoxysugar ascarylose and hydroxylated short-chain fatty acid (Figure 1a; von Reuss et al., 2012). Structural and functional specificity arises from optional attachment of additional moieties to the sugar, for example indole-3-carboxylic acid (e.g. icas#3 (1)), or carboxy-terminal additions to the fatty acid chain, such as p-aminobenzoic acid (PABA, as in ascr#8 (2)) or O-glucosyl uric acid (e.g. uglas#11 (3), Figure 1b; Artyukhin et al., 2018; Artyukhin et al., 2013; Bose et al., 2014; Aprison and Ruvinsky, 2017; Curtis et al., 2020; Pungaliya et al., 2009). Given that even small changes in the chemical structures of the ascarosides often result in starkly altered biological function, ascaroside biosynthesis appears to correspond to a carefully regulated encoding process in which biological state is translated into chemical structures (Panda et al., 2017). Thus, the biosynthesis of ascarosides and other C. elegans signaling molecules (e.g. nacq#1) (Ludewig et al., 2019) represents a fascinating model system for the endogenous regulation of inter-organismal small-molecule signaling in metazoans. However, for most of the >200 recently identified C. elegans metabolites (Artyukhin et al., 2018; von Reuss et al., 2012; Artyukhin et al., 2013), biosynthetic knowledge is sparse. Previous studies have demonstrated that conserved metabolic pathways, for example peroxisomal β-oxidation (Artyukhin et al., 2013; Bose et al., 2014) and amino acid catabolism (von Reuss et al., 2012; Srinivasan et al., 2012; Figure 1a), contribute to ascaroside biosynthesis; however, many aspects of the mechanisms underlying assembly of multi-modular metabolites remains unclear.

![Figure 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig1-v2.jpg)

**Figure 1.:** (a) Modular ascarosides are assembled from simple ascarosides, e.g. ascr#1 (5) or ascr#3 (9), and building blocks from other metabolic pathways, e.g. glucosyl uric acid (6), p-aminobenzoic acid (PABA, 8) indole-3-carboxylic acid (11), or succinyl octopamine (12). We hypothesize that glo-1-dependent gut granules play a central role in their biosynthesis. (b) Examples for modular ascarosides and their biological context. (c) UAR-1 in P. pacificus converts simple ascarosides into the 4′-ureidoisobutyric-acid-bearing ascarosides, for example ubas#3 (4). (d) Strategy for comparative metabolomic analysis of LRO-deficient glo-1 mutants. (e) Example for modular ascarosides whose production is increased in glo-1 mutants.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** cest genes (direct homologs of Ppa-uar-1) are colored in red.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Bars represent the mean of six replicates and error bars standard deviation.

Recently, metabolomic analysis of mutants of the Rab-GTPase glo-1, which lack a specific type of lysosome-related organelles (LROs, also referred to as autofluorescent gut granules), revealed complete loss of 4′-modified ascarosides (Panda et al., 2017). The glo-1-dependent LROs are acidic, pigmented compartments that are related to mammalian melanosomes and drosophila eye pigment organelles (Coburn and Gems, 2013; Hermann et al., 2005). LROs form when lysosomes fuse with other cellular compartments, for example peroxisomes, and appear to play an important role for recycling proteins and metabolites (Coburn and Gems, 2013). Additionally, it has been suggested that LROs may be involved in the production and secretion of diverse signaling molecules (Dell'Angelica et al., 2000; Luzio et al., 2014), and the observation that glo-1 mutant worms are deficient in 4′-modified ascarosides suggested that intestinal organelles may serve as hubs for their assembly (Figure 1a; Panda et al., 2017). In addition to the autofluorescent LROs, several other types of intestinal granules have been characterized in C. elegans, including lipid droplets (Cao et al., 2019) and lysosome-related organelles that are not glo-1-dependent (Tanji et al., 2016).

Parallel studies of other Caenorhabditis species (Dong et al., 2016; Bergame et al., 2019; Dolke et al., 2019) and Pristionchus pacificus (Falcke et al., 2018), a nematode species being developed as a satellite model system to C. elegans (Rae et al., 2008), revealed that production of modular ascarosides is widely conserved among nematodes. Leveraging the high genomic diversity of sequenced P. pacificus isolates, genome-wide association studies coupled to metabolomic analysis revealed that uar-1, a carboxylesterase from the α/ß-hydrolase superfamily with homology to cholinesterases (AChEs), is required for 4′-attachment of an ureidoisobutyryl moiety to a subset of ascarosides, e.g. ubas#3 (4, Figure 1c; Falcke et al., 2018). Homology searches revealed a large expansion of carboxylesterase (cest) homologs in P. pacificus as well as C. elegans (Figure 1—figure supplement 1), and recently it was shown that in C. elegans, the uar-1 homologs cest-3, cest-8, and cest-9.2 are involved in the 4′-attachment of other acyl groups in modular ascarosides (Faghih et al., 2020). Based on these findings, we posited that cest homologs localize to glo-1-dependent intestinal granules where they control assembly of modular ascarosides, and perhaps other modular metabolites. In this work, we present a comprehensive assessment of the impact of glo-1-deletion on the C. elegans metabolome and uncover the central role of cest homologs that localize to intestinal granules in the biosynthesis of diverse modular metabolites.

## Results

### Novel classes of LRO-dependent metabolites

To gain a comprehensive overview of the role of glo-1 in C. elegans metabolism, we employed a fully untargeted comparison of the metabolomes of a glo-1 null mutant and wild-type worms (Figure 1d). HPLC–high-resolution mass spectrometry (HPLC–HRMS) data for the exo-metabolomes (excreted compounds) and endo-metabolomes (compounds extractable from the worm bodies) of the two strains were analyzed using the Metaboseek comparative metabolomics platform, which integrates the xcms package (Tautenhahn et al., 2008). These comparative analyses revealed that the glo-1 mutation has a dramatic impact on C. elegans metabolism. For example, in negative ionization mode, we detected >1000 molecular features that were at least 10-fold less abundant in the glo-1 exo- and endo-metabolomes, as well as >3000 molecular features that are 10-fold upregulated in glo-1 mutants. For further characterization of differential features, we employed tandem mass spectrometry (MS2) based molecular networking, a method which groups metabolites based on shared fragmentation patterns (Figure 1d, Figure 2—figure supplements 1–4; Wang et al., 2016). The resulting four MS2 networks – for data obtained in positive and negative ionization mode for the exo- and endo-metabolomes – revealed several large clusters of features whose abundances were largely abolished or greatly increased in glo-1 worms. Notably, although some differential MS2 clusters represented known compounds, for example ascarosides, the majority of clusters were found to represent previously undescribed metabolite families.

In agreement with previous studies (Panda et al., 2017), biosynthesis of most modular ascarosides was abolished or substantially reduced in glo-1 mutants, including all 4′-modified ascarosides, e.g. icas#3 (1) (Figure 1b, Figure 2—figure supplement 5a). Similarly, production of ascarosides modified at the carboxy terminus, e.g. uglas#11 (3) derived from ester formation between ascr#1 (5) and uric acid glucoside (Curtis et al., 2020) (6), and ascr#8 (2), derived from formation of an amide bond between ascr#7 (7) and of p-amino benzoic acid (8), was largely abolished in glo-1 mutants (Figure 1a–b, Figure 2—figure supplement 5a). Metabolites plausibly representing building blocks of these modular ascarosides were not strongly perturbed in glo-1 mutants (Figure 1—figure supplement 2). For example, abundances of unmodified ascarosides, for example ascr#3 (9) and ascr#10 (10), or metabolites representing 4′-modifications, for example indole-3-carboxylic acid (11) and octopamine succinate (12), were not significantly perturbed in the mutant (Figure 1a, Figure 2—figure supplement 5a, Figure 1—figure supplement 2). In contrast, a subset of modular ascaroside glucose esters (e.g. iglas#1 (13) and glas#10 (14), Figure 1e), was strongly increased in glo-1 mutants (Figure 2—figure supplement 5b). These results suggest that glo-1-dependent intestinal organelles function as a central hub for the biosynthesis of most modular ascarosides, with the exception of a subset of ascarosylated glucosides, whose increased production in glo-1 mutants may be indicative of a shunt pathway for ascarosyl-CoA derivatives (Zhang et al., 2015; Zhang et al., 2016; Zhang et al., 2018), which represent plausible precursors for modular ascarosides modified at the carboxy terminus.

Next, we analyzed the most prominent MS2 clusters representing previously uncharacterized metabolites whose production is abolished or strongly reduced in glo-1 mutants (Figure 2). Detailed analysis of their MS2 spectra indicated that they may represent a large family of modular hexose derivatives incorporating moieties from diverse primary metabolic pathways. For example, MS2 spectra from clusters I, II, and III of the positive-ionization network suggested phosphorylated hexose glycosides of indole, anthranilic acid, tyramine, or octopamine, which are further decorated with a wide variety of fatty acyl moieties derived from fatty acid or amino acid metabolism, for example nicotinic acid, pyrrolic acid, or tiglic acid (Figure 2, Appendix 1—table 1; Coburn and Gems, 2013; Stupp et al., 2013). Given the previous identification of the glucosides iglu#1/2 (15/16, Figure 2e) and angl#1/2 (17/18), we hypothesized that clusters I, II, and III represent a modular library of glucosides, in which N-glucosylated indole, anthranilic acid, tyramine, or octopamine (O'Donnell et al., 2020) serve as scaffolds for attachment of diverse building blocks. To further support these structural assignments, a series of modular metabolites based on N-glucosylated indole (‘iglu’) were selected for total synthesis. Synthetic standards for the non-phosphorylated parent compounds of iglu#4 (19), iglu#6 (20), iglu#8 (21), and iglu#10 (22) matched HPLC retention times and MS2 spectra of the corresponding natural compounds (Figure 2—figure supplement 6), confirming their structures and enabling tentative structural assignments for a large number of additional modular glucosides, including their phosphorylated derivatives, e.g. iglu#12 (23), iglu#41 (24), angl#4 (cluster II, 25), and tyglu#4 (cluster III, 26) (Figure 2). The proposed structures include several glucosides of the neurotransmitters tyramine and octopamine, whose incorporation could be verified by comparison with data from a recently described feeding experiment with stable isotope-labeled tyrosine (O'Donnell et al., 2020). Similar to ascaroside biosynthesis, the production of modular glucosides is life stage dependent; for example, production of specific tyramine glucosides peaks at the L3 larval stage, whereas production of angl#4 increases until the adult stage (Figure 2—figure supplement 8). Notably, modular glucosides were detected primarily as their phosphorylated derivatives, as respective non-phosphorylated species were generally less abundant. In contrast to most ascarosides, the phosphorylated glucosides are more abundant in the endo-metabolome than the exo-metabolome, suggesting that phosphorylated glucosides may be specifically retained in the body (Figure 2—figure supplement 7).

![Figure 2.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-v2.jpg)

**Figure 2.:** (a) Partial MS2 network (positive ion mode) for C. elegans endo-metabolome highlighting three clusters of modular glucosides that are down regulated in the glo-1 mutants (also see Figure 2—figure supplements 1–4). Red represents downregulated and blue upregulated features compared to wildtype C. elegans. (b) Cluster I feature several modular indole glucoside derivatives. Structures were proposed based on MS2 fragmentation patterns, also see Appendix 1—table 1. Compounds whose non-phosphorylated analogs were synthesized are marked (*). Shown ion chromatograms demonstrate loss of iglu#4 in glo-1 mutants. (c,d) Examples for modular glucosides detected as part of clusters II and III. Ion chromatograms show abolishment of angl#4 (25) (c) and tyglu#4 (26) (d) production in glo-1 mutants. (e) Modular glucosides are derived from combinatorial assembly of a wide range of building blocks. Incorporation of moieties was confirmed via total synthesis of example compounds (green) or stable isotope labeling (blue). For all compounds, 3-phosphorylation was proposed based on the established structures of iglu#2 (16), angl#2 (18), and uglas#11 (3).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Red and blue represent features that are down- and up-regulated in glo-1 mutant worms, respectively. Clusters II and III with representative modular glucoside structures that are glo-1 dependent (right).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Red and blue represent features that are down- and up-regulated in glo-1 mutant worms, respectively.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Red and blue represent features that are down- and upregulated in glo-1 mutant worms, respectively.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Red and blue represent features that are down- and upregulated in glo-1 mutant worms, respectively.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Bars represent the mean of 6 (glo-1) and 2 (glo-4) biological replicates and error bars standard deviation. (c) Peak area relative to wildtype of simple and modular ascarosides in glo-4 mutant worms. Bars represent the mean of two replicates. n.d., not detected.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** (a) Ion chromatograms of synthetic iglu#4 (19), and the levels of iglu#3 (34) in wildtype (N2), cest-4, cest-2.2 and cest-1.1. (b) MS2 spectra of synthetic iglu#3 (34) and the natural compound. Ion chromatograms of other indole containing glucosides in C. elegans and corresponding synthetic samples (black traces), including iglu#5 (SI-2), whose production is reduced but not abolished in glo-1 mutants, as well as largely glo-1 dependent iglu#7 (SI-3) and, iglu#9 (SI-4).

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** Concentrations were calculated with respect to the volume pre-extraction, that is, the aggregate volume of the worm bodies and the volume of the media. Bars represent mean of six replicates. Error bars are standard deviation of the mean, and p-values are depicted in the Figure.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp8-v2.jpg)

**Figure 2—figure supplement 8.:** Levels of (a) iglu#2 (16), (b) iglu#4 (19), (c) angl#4 (25), and (d) tyglu#6 (proposed structure, SI-6) at different stages of development of C. elegans.

![Figure 2—figure supplement 9.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp9-v2.jpg)

**Figure 2—figure supplement 9.:** Bars represent mean of 6 replicates, with error bar representing standard deviation.

![Figure 2—figure supplement 10.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig2-figsupp10-v2.jpg)

As in the case of modular ascarosides, the abundances of putative building blocks of the newly identified modular glucosides were not strongly perturbed in glo-1 mutants. For example, abundances of anthranilic acid, indole, octopamine, and tyramine were not significantly affected in glo-1 null animals (Figure 2—figure supplement 9). Notably, abundances of the glucosides scaffold, e.g. iglu#1 and angl#1, were also largely unaltered or even slightly increased in glo-1 mutants (Figure 2—figure supplement 9). In addition, production of some of the identified modular glucosides, e.g. iglu#5, is reduced but not fully abolished in glo-1 worms (Figure 2—figure supplement 6).

To confirm our results, we additionally compared the glo-1 metabolome with that of glo-4 mutants. glo-4 encodes a predicted guanyl-nucleotide exchange factor acting upstream of glo-1, and like glo-1 mutants, glo-4 worms do not form LROs (Hermann et al., 2005). We found that the glo-4 metabolome closely resembles that of glo-1 worms, lacking most of the modular ascarosides and ascarosides detected in wildtype worms (Figure 2—figure supplement 5c). Correspondingly, similar sets of compounds are upregulated in glo-1 and glo-4 mutants relative to wild type, including ascarosyl glucosides and ascaroside phosphates. Compounds accumulating in glo-1 and glo-4 mutant worms further include a diverse array of small peptides (primarily three to six amino acids), consistent with the proposed role of LROs in the breakdown of peptides derived from proteolysis (Figure 2—figure supplement 10; Bird et al., 2009). Taken together, our results indicate that, in addition to their roles in the degradation of metabolic waste, the LROs serve as hotspots of biosynthetic activity, where building blocks from diverse metabolic pathways are attached to glucoside and ascaroside scaffolds (Figure 1a).

### Carboxylesterases are required for modular assembly

Comparing the relative abundances of different members of the identified families of modular glucosides and ascarosides, it appears that combinations of different building blocks and scaffolds are highly specific, suggesting the presence of dedicated biosynthetic pathways. For example, uric acid glucoside, gluric#1 (6), is preferentially combined with an ascaroside bearing a seven-carbon side chain (to form uglas#11, 3), whereas ascarosides bearing a nine-carbon side chain are preferentially attached to the anomeric position of free glucose, as in glas#10 (14) (Artyukhin et al., 2018; von Reuss et al., 2012). Similarly, tiglic acid is preferentially attached to indole and tyramine glucosides but not to anthranilic acid glucosides (Appendix 1—table 1). Given that 4′-modification of ascarosides in P. pacificus and C. elegans require cest homologs, we hypothesized that the biosynthesis of other modular ascarosides as well as the newly identified glucosides may be under the control of cest family enzymes (Falcke et al., 2018; Faghih et al., 2020). From a list of 44 uar-1 homologs from BLAST analysis (Appendix 1—table 2), we selected seven for further study (Figure 3a, Appendix 1—table 3). The selected homologs are predicted to have intestinal expression, one primary site of small molecule biosynthesis in C. elegans (Artyukhin et al., 2018), and are closely related to the UAR-1 gene, while representing different sub-branches of the phylogenetic tree. Utilizing a recently optimized CRISPR/Cas9 method, we obtained two null mutant strains for five of the selected genes (Wang et al., 2018). Mutants for the remaining two homologs, ges-1 and cest-6, had been previously obtained (Appendix 1—table 3). We then analyzed the exo- and endo-metabolomes of this set of mutant strains by HPLC-HRMS to identify features that are absent or strongly downregulated in null mutants of a specific candidate gene compared to wildtype worms and all other mutants in this study. We found that two of the seven tested homologs (cest-1.1, cest-2.2) are defective in the production of two different families of modular ascarosides, whereas cest-4 mutants were defective in the biosynthesis of a specific subset of modular indole glucosides (Figure 3). The metabolomes of mutants for the remaining four cest homologs did not exhibit any significant differences compared to wild type under the tested conditions.

![Figure 3.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig3-v2.jpg)

**Figure 3.:** (a) Serine hydrolase dendrogram relating P. pacificus uar-1 to homologous predicted genes in C. elegans. Ppa-uar-1, cest-3, cest-8, cest-9.2 (green) mediate ester formation at the 4′-position of ascarosides in P. pacificus and C. elegans. Genes shown in red color were selected for the current study. (b,c) Production of ascr#8 (2), ascr#81 (27), and ascr#82 (28) is abolished in cest-2.2 mutants Isogenic revertant strains of the cest-2.2 null mutants in which the STOP-IN cassette was precisely excised, demonstrate wild-type-like recovery of the associated metabolite. (d,e) Production of uglas#1 and uglas#11 is abolished in cest-1.1(null) mutants and recovered in genetic revertants. (f) Biosynthesis of positional isomers uglas#14 (31) and uglas#15 (32) is unaltered or increased in cest-1.1 mutants (f). (g) Production of uglas#1 and uglas#11, but not gluric#1, is abolished in cest-1.1(S213) mutants. (h,i) Production of the anthranilic-acid-modified glucoside iglu#4 is largely abolished in cest-4 mutants and fully recovered in genetic revertants. (j) Production of iglu#6 (36) and iglu#8 (37), whose structures are closely related to that of iglu#4, is not abolished in cest-4 mutants. Ion chromatograms in panels b, d, and g further demonstrate abolishment in glo-1 mutants. n.d., not detected. Error bars are standard deviation of the mean, and p-values are depicted in the Figure.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Values were normalized relative to ascr#82 (28). Bars represent the mean of 3 replicates, and error bars are standard deviation.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig3-figsupp2-v2.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig3-figsupp3-v2.jpg)

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Bars represent the mean of three replicates, and error bars are standard deviation.

Analysis of the metabolomes of the two cest-2.2 null mutants revealed loss of dauer pheromone component and male attractant ascr#8 (2) as well as of the closely related ascr#81 (27) and ascr#82 (28) (Figure 3b, Figure 3—figure supplements 1 and 2b). Biosynthetically, the ascr#8 family of ascarosides are derived from amide formation between ascr#7 (ΔC7, 7) and folate-derived p-aminobenzoic acid (PABA, 8), PABA-glutamate (29), or PABA-diglutamate, respectively. We did not detect any significant reduction in the production of plausible ascr#8 precursors, including PABA and PABA-glutamate, or ascr#7 (Figure 3b, Figure 3—figure supplement 2b). Biosynthesis of ascr#8, ascr#81, and ascr#82 was recovered in cest-2.2 mutant worms in which the cest-2.2 sequence had been restored to wild type using CRISPR/Cas9 (Figure 3c, Figure 3—figure supplement 3b). These results indicate that CEST-2.2 is required specifically for biosynthesis of the amide linkage between the carboxy terminus of ascr#7 and PABA derivatives, in contrast to the implied functions of UAR-1, CEST-8, CEST-3, and CEST-9.2, which are involved in the formation of ester bonds between various head groups and the 4′-hydroxy group of ascarylose (Falcke et al., 2018; Faghih et al., 2020).

In cest-1.1 null mutants (cest-1.1(null)), biosynthesis of the nucleoside-like ascaroside uglas#1 (30) and its phosphorylated derivative uglas#11 (3) was abolished (Figure 3d, Figure 3—figure supplement 2a). uglas#1 and uglas#11 are derived from the attachment of ascr#1, bearing a seven carbon (C7) side chain, to the uric acid gluconucleoside gluric#1 (6). Production of ascr#1 (5) and gluric#1 (6), representing plausible building blocks of uglas#1 (30), was not reduced (Figure 3—figure supplement 2a). Furthermore, production of uglas#14 (31) and uglas#15 (32), isomers of uglas#1 and uglas#11 bearing the ascarosyl moiety at the 6′ position instead of the 2′ position, was not abolished but rather slightly increased in cest-1.1(null) (Figure 3d–e). These results indicate that CEST-1.1 is required for the formation of the ester bond specifically between ascr#1 (5) and the 2′-hydroxyl group in gluric#1. As in the case of cest-2.2, biosynthesis of uglas#1 and uglas#11 was fully recovered in cest-1.1 mutant worms in which the cest-1.1 sequence had been restored to wild type using CRISPR/Cas9 (Figure 3f, Figure 3—figure supplement 3a).

Sequence alignment with human AChE suggested that serine 213 is part of the conserved catalytic serine-histidine-glutamate triad of CEST-1.1 (Figure 4—figure supplement 1). To test whether disruption of the catalytic triad would affect production of cest-1.1-dependent metabolites, we generated a point mutant, cest-1.1(S213A). As in cest-1.1(null), production of uglas#1 (30) and uglas#11 (3) was fully abolished in cest-1.1(S213A), whereas production of gluric#1 was not affected (Figure 3g).

Previous work implicated cest-1.1 with longevity phenotypes associated with argonaute-like gene 2 (alg-2) (Aalto et al., 2018). alg-2 mutant worms are long lived compared to wild type and their long lifespan was further shown to require daf-16, the sole ortholog of the FOXO family of transcription factors in C. elegans, as well as cest-1.1. Moreover, uglas#11 biosynthesis is significantly increased in mutants of the insulin receptor homolog daf-2, a central regulator of lifespan in C. elegans upstream of daf-16 (Curtis et al., 2020). These findings suggest the possibility that the production of uglas ascarosides underlies the cest-1.1-dependent extension of adult lifespan in C. elegans.

In contrast to our results for cest-1.1 and cest-2.2 mutants, comparative metabolomic analysis of the cest-4 mutant strains did not reveal any defects in the biosynthesis of known ascarosides. Instead, we found that the levels of a specific subset of modular anthranilic acid (33) bearing indole glucosides, including iglu#3 (34) and its phosphorylated derivative iglu#4 (35) were abolished in the cest-4 mutant worms (Figure 3h). Abundances of the putative precursor glucosides, iglu#1 (15) and iglu#2 (16), were not significantly changed in cest-4 (Figure 3i, Figure 3—figure supplement 2c). Notably, production of other indole glucosides, e.g. iglu#6 (36) and iglu#8 (37), was not significantly reduced in cest-4 worms (Figure 3j, Figure 3—figure supplement 4). Biosynthesis of iglu#3 and iglu#4 was restored to wild-type levels in genetic revertant strains for cest-4 (Figure 3i, Figure 3—figure supplement 3c). Therefore, it appears that cest-4 is specifically required for attachment of anthranilic acid to the 6′ position of glucosyl indole precursors, whereas attachment of tiglic acid, nicotinic acid, and other moieties is cest-4-independent (Figure 3j, Figure 3—figure supplement 4). The role of cest-4 in the biosynthesis of the iglu family of modular glucosides thus parallels that of cest-1.1 in the biosynthesis of the uglas ascarosides: whereas cest-4 appears to be required for the attachment of anthranilic acid (33) to the 6’ position of a range of indole glucosides, cest-1.1 appears to be required for attaching the ascr#1 side chain to the 2′ position in uric acid glucosides.

### CEST-2.2 localizes to intestinal granules

All cest homologs selected for this study exhibit domain architectures typical of the α/ß-hydrolase superfamily of proteins, including a conserved catalytic triad, and further contain a predicted disulfide bridge, as in mammalian AChE (Soreq and Seidman, 2001; Figure 4—figure supplement 1). The cest genes also share homology with neuroligin, a membrane bound member of the α/ß-hydrolase fold family, that mediates the formation and maintenance of synapses between neurons (Bemben et al., 2015). Sequence analysis suggests that five of the seven CEST homologs studied here are membrane anchored, given the presence of a predicted C-terminal transmembrane domain (Krogh et al., 2001) (consisting of ~20 residues), with the N terminus on the luminal side of a vesicle or organelle (Figure 4—figure supplement 2). Since the production of all so far identified cest-dependent metabolites is abolished in glo-1 mutants, it seemed likely that the CEST proteins localize to intestinal granules. To test this idea, we created a mutant strain that express cest-2.2 C-terminally tagged with mCherry at the native genomic locus to avoid potentially confounding effects of overexpression. The red fluorescent mCherry was chosen because of the strong green autofluorescence of the LROs (Coburn and Gems, 2013). We confirmed that production of all cest-2.2-dependent metabolites, including ascr#8 (2), ascr#81 (27), and ascr#82 (28) was not significantly altered in cest-2.2-mCherry mutants (Figure 4a), indicating that CEST-2.2 remained functional. Imaging of wild-type adult worms revealed strong green and weaker red autofluorescence in circular features in intestinal cells, consistent with LROs. In addition, cest-2.2-mCherry-tagged worms showed red fluorescence in a distinct set of intestinal granules that showed little if any autofluorescence (Figure 4b, Figure 4—figure supplements 3–4). It is unclear whether mCherry also localizes to the strongly autofluorescent granules, as we cannot distinguish the mCherry signal from the red component of the autofluorescence, given relatively low CEST-2.2-mCherry expression in this non-overexpressing strain. Taken together, it appears that CEST-2.2-mCherry localizes to a subset of intestinal organelles that is partly distinct from the autofluorescent LROs. Further studies are required to determine if CEST-2.2-mCherry co-localizes with other intestinal granule markers, specifically GLO-1 and the lysosomal marker LMP-1.

![Figure 4.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig4-v2.jpg)

**Figure 4.:** (a) Relative amounts of cest-2.2-dependent metabolites in worms expressing C-terminally mCherry-tagged CEST-2.2. (b) Red fluorescence in intestinal granules in wild-type and cest-2.2-mCherry gravid adults. Top, wild-type (N2) control; bottom, cest-2.2-mCherry worms.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig4-figsupp1-v2.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Predictions were performed by the TMHMM, as described previously.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Images in the two bottom rows are from younger worms closer to young adult stage.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig4-figsupp4-v2.jpg)

### Glo-1-dependent metabolites in C. briggsae

In addition to C. elegans and P. pacificus, modular ascarosides have been reported from several other Caenorhabditis species (Dong et al., 2020; Kanzaki et al., 2018), including C. briggsae (Dong et al., 2016; von Reuss, 2018). To assess whether the role of LROs in the biosynthesis of modular metabolites is conserved across species, we created two Cbr-glo-1 (CBG01912.1) knock-out strains using CRISPR/Cas9. As in C. elegans, Cbr-glo-1 mutant worms lacked autofluorescent LROs, which are prominently visible in wild-type C. briggsae (Figure 5—figure supplement 1). Comparative metabolomic analysis of the endo- and exo-metabolomes of wild-type C. briggsae and the Cbr-glo-1 mutant strains revealed that biosynthesis of all known modular ascarosides is abolished in Cbr-glo-1 worms, including the indole carboxy derivatives icas#2 (35) and icas#6.2 (36), which are highly abundant in wild-type C. briggsae (Figure 5a; Dong et al., 2016). In addition, the C. briggsae MS2 networks included several large Cbr-glo-1-dependent clusters representing modular glucosides, including many of the compounds also detected in C. elegans, for example iglu#4 and angl#4. As in C. elegans, production of unmodified glucoside scaffolds, e.g. iglu#1 (15) and angl#1 (17), was not reduced or increased in Cbr-glo-1 mutants, whereas biosynthesis of most modular glucosides derived from attachment of additional moieties to these scaffolds was abolished (Figure 5b). Taken together, these results indicate that the role of LROs as a central hub for the assembly of diverse small molecule architectures, including modular glucosides and ascarosides, may be widely conserved among nematodes (Figure 5c).

![Figure 5.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig5-v2.jpg)

**Figure 5.:** n.d., not detected. (c) Model for modular metabolite assembly. CEST proteins (membrane-bound in the LROs, red) mediate attachment of building blocks from diverse metabolic pathways to glucose scaffolds and peroxisomal β-oxidation-derived ascarosides via ester and amide bonds. Some of the resulting modular ascarosides may undergo additional peroxisomal β-oxidation following activation by acs-7 (Dolke et al., 2019).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) C. briggsae WT AF16 has gut granules similar to C. elegans which are also both birefringent and easily tagged by Lysotracker Red (see arrows). Gut granule loss is evident in both (b) Cbr-glo-1(sy1382) and (c) Cbr-glo-1(sy1383).

## Discussion

Our results indicate that in C. elegans the Rab-GTPase glo-1, which is required for formation of intestinal LROs, plays a central role in the biosynthesis of several large compound families derived from modular assembly via cest homologs. Formation of the autofluorescent LROs via glo-1 is reminiscent of the roles of its human orthologs RAB32 and RAB38, which are required for the formation of melanosomes, and perhaps other LROs (Wasmeier et al., 2006; Marks et al., 2013). Lysosomes and LROs are generally presumed to function in autophagy, phagocytosis, and the hydrolytic degradation of proteins, and Rab32 family GTPases have been shown to be required for these processes in diverse organisms (Morris et al., 2018). Consistent with the notion that lysosomes and LROs are degradation hotspots, many of the building blocks of the identified modular ascarosides and glucosides are derived from catabolic pathways, for example, anthranilic acid is derived from tryptophan catabolism, uric acid stems from purine metabolism, and the short chain ascarosides are the end products of peroxisomal β-oxidation of very long-chain precursors. Importantly, although our results indicate that carboxylesterases participate in glo-1-dependent modular metabolite assembly, additional studies are required to clarify whether the intestinal compartments that carboxylesterases localize to also contain GLO-1 and the lysosomal marker LMP-1, as is the case for the autofluorescent LROs (Tanji et al., 2016).

Further, our results demonstrate that the modular assembly paradigm extends beyond ascarosides. The modular glucosides represent a previously unknown family of nematode metabolites. In contrast to the well-established role of modular ascarosides as pheromones, it is unknown whether modular glycosides serve specific biological functions, for example as signaling molecules; however, their specific biosynthesis via cest-4 as well as their life-stage-dependent production strongly supports this hypothesis (Figure 2—figure supplement 8). Like the ascaroside pheromones, some modular glucosides are excreted into the media, suggesting that they could be involved in inter-organismal communication. Identifying developmental and environmental conditions that affect modular glucoside production, as well as a more comprehensive understanding of their biosyntheses, may help uncover potential signaling and other biological roles. In particular, the apparent peroxisomal origin of the ascaroside scaffolds suggests a link between peroxisome and gut granule activity, perhaps via pexophagy (Sakai et al., 2006), and characterization of the role of autophagy for gut granule-dependent metabolism may contribute to uncovering the functions of modular glucoside and ascarosides. A connection to autophagy is also suggested by our previous finding (Panda et al., 2017) that production of modular ascarosides is reduced in mutants of atg-18 (Palmisano and Meléndez, 2019), which is essential for autophagy.

The high degree of selectivity in which different building blocks are combined in the modular ascarosides and glucosides strongly suggests that these compounds, despite their numbers and diversity, represent products of dedicated enzymatic pathways, as has recently been established for 4′-acylated ascarosides. Our results revealed a wider range of biosynthetic functions associated with cest homologs, including esterification and amide formation at the carboxy terminus of ascarosides and acylation of glucosides (Figure 5c). Notably, all cest null mutants whose metabolomes have been characterized so far are defective in the biosynthesis of one or a few compounds sharing a specific structural feature, further supporting the view that these selectively assembled molecular architectures serve dedicated functions.

All CEST proteins that so far have been associated with modular metabolite assembly contain membrane-anchors and exhibit domain architectures typical of serine hydrolases of the AChE family, including an α/β-hydrolase fold, a conserved catalytic serine-histidine-glutamate triad, and bridging disulfide cysteines (Figure 4—figure supplement 1; Soreq and Seidman, 2001). While our efforts at heterologous expression of CEST proteins were unsuccessful, the finding that mutation of the catalytic serine in cest-1.1(S213A) abolished production of all cest-1.1-dependent compounds suggests that CEST enzymes directly participate in the biosynthesis of modular metabolites. Therefore, we hypothesize that CEST proteins, after translating from the endomembrane system to glo-1-dependent intestinal organelles, partake in the assembly of diverse ascaroside or glucoside-based architectures via acyl transfer from corresponding activated intermediates, e.g. CoA or phosphate esters (Soreq and Seidman, 2001; Vaz and Wanders, 2002). α/β-hydrolase fold enzymes are functionally highly diverse (Rauwerdink and Kazlauskas, 2015) and include esterases, peptidases, oxidoreductases, and lyases, serving diverse biosynthetic roles in animals, plants (Mindrebo et al., 2016), and bacteria (Zheng et al., 2016). While acyltransferase activity is often observed as a side reaction for esterases and lipases, α/β-hydrolase fold enzymes can function as dedicated acyltransferases, for example in microbial natural product biosyntheses (Rauwerdink and Kazlauskas, 2015; Lejon et al., 2008). Additional biochemical studies will be required to delineate the exact mechanisms by which cest homologs contribute to modular metabolite assembly in nematodes.

Finally, although our results indicate that glo-1 is required for the biosynthesis of most modular metabolites we have detected so far, it is notable that some modular ascarosides, e.g. iglas#1 (13), and modular glucosides, e.g. iglu#6 (20) and iglu#8 (21), do not appear to be glo-1-dependent (Figure 2—figure supplement 7). This suggests that diverse cell compartments contribute to modular metabolite biosynthesis and may also indicate that not all CEST proteins are delivered to the same cellular compartment. Similarly, glo-1 mutants continue to generate the simple glucosides and ascarosides that serve as scaffolds for further elaboration via CEST proteins, which may be derived from UDP-glycosyltransferases (Mackenzie et al., 2005).

Reminiscent of the role of AChE for neuronal signal transduction in animals, it appears that, in C. elegans, carboxylesterases with homology to AChE have been co-opted to establish additional signal transduction pathways that are based on a modular chemical language, for inter-organismal communication, and perhaps also intra-organismal signaling. The biosynthetic functions of most of the 200 serine hydrolases in C. elegans, including more than 30 additional cest homologs, remain to be assessed, and it seems likely that this enzyme family contributes to the biosynthesis of a large number of additional, yet unidentified compounds. Similarly, the exact enzymatic roles of many families of mammalian serine hydrolases have not been investigated using HRMS-based untargeted metabolomics. Our results may motivate a systematic characterization of metazoan cest homologs and other serine hydrolases, with regard to their roles in metabolism and small molecule signaling, associated enzymatic mechanisms, and cellular localization.

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
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>N2</td>
      <td>Caenorhabditis Genetics Center (CGC)</td>
      <td></td>
      <td>Wild type</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>GH10</td>
      <td>David Gems</td>
      <td></td>
      <td>glo-1(zu437)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>RB811</td>
      <td>Caenorhabditis Genetics Center (CGC)</td>
      <td></td>
      <td>glo-4(ok623)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>RB2053</td>
      <td>Caenorhabditis Genetics Center (CGC)</td>
      <td></td>
      <td>ges-1(ok2716)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8031</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(sy1180)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8032</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(sy1181)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>DP683</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(dp683) (S213A)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8259</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(sy1180 sy1250)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8260</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(sy1180 sy1251)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8261</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(sy1181 sy1252)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8262</td>
      <td>This work</td>
      <td></td>
      <td>cest-1.1(sy1181 sy1253)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8008</td>
      <td>This work</td>
      <td></td>
      <td>cest-2.2(sy1170)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8009</td>
      <td>This work</td>
      <td></td>
      <td>cest-2.2 (sy1171)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8236</td>
      <td>This work</td>
      <td></td>
      <td>cest-2.2(sy1170 sy1236)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8238</td>
      <td>This work</td>
      <td></td>
      <td>cest-2.2(sy1171 sy1238)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>FCS02</td>
      <td>SunyBiotech</td>
      <td></td>
      <td>cest-2.2-mCherry</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8116</td>
      <td>This work</td>
      <td></td>
      <td>cest-4(sy1192)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8117</td>
      <td>This work</td>
      <td></td>
      <td>cest-4(sy1193)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8781</td>
      <td>This work</td>
      <td></td>
      <td>cest-4(sy1192)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8782</td>
      <td>This work</td>
      <td></td>
      <td>cest-4(sy1193)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8783</td>
      <td>This work</td>
      <td></td>
      <td>cest-4(sy1194)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8784</td>
      <td>This work</td>
      <td></td>
      <td>cest-4(sy1195)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>RB1804</td>
      <td>Caenorhabditis Genetics Center (CGC)</td>
      <td></td>
      <td>cest-6(ok2338)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8029</td>
      <td>This work</td>
      <td></td>
      <td>cest-19(sy1178)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8030</td>
      <td>This work</td>
      <td></td>
      <td>cest-19(sy1179)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8033</td>
      <td>This work</td>
      <td></td>
      <td>cest-33(sy1182)</td>
    </tr>
    <tr>
      <td>Strain, strain background Caenorhabditis elegans</td>
      <td>PS8034</td>
      <td>This work</td>
      <td></td>
      <td>cest-33(sy1183)</td>
    </tr>
    <tr>
      <td>Strain (Caenorhabditis briggsae)</td>
      <td>PS8515</td>
      <td>This work</td>
      <td></td>
      <td>CBR-glo-1(sy1382)</td>
    </tr>
    <tr>
      <td>Strain (Caenorhabditis briggsae)</td>
      <td>PS8516</td>
      <td>This work</td>
      <td></td>
      <td>CBR-glo-1(sy1383)</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Proteinase K</td>
      <td>New England Biolabs</td>
      <td></td>
      <td>New England Biolabs: P8107S</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Metaboseek</td>
      <td>Metaboseek (metaboseek.com)</td>
      <td></td>
      <td>Version 0.9.6</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad Prism (graphpad.com)</td>
      <td></td>
      <td>Version 8.4.3</td>
    </tr>
  </tbody>
</table>

### General information

Unless noted otherwise, all reagents were purchased from Sigma-Aldrich. All newly identified compounds were assigned four letter 'SMID's (a search-compatible, Small Molecule IDentifier) for example ‘icas#3’ or ‘ascr#10’. For a list of all compounds referred to in the text and figures, see Appendix 1—table 9. The SMID database (www.smid-db.org) is an electronic resource maintained in collaboration with WormBase (www.wormbase.org). A complete list of SMIDs can be found at www.smid-db.org/browse, and example structures for different SMIDs at www.smid-db.org/smidclasses.

### BLAST analysis of uar-1

Amino acid sequence of Ppa-UAR-1 was used as previously published (Falcke et al., 2018). BLASTp was run from the WormBase engine at (https://wormbase.org/tools/blast_blat). E-value threshold was set to 1E0. Database was set to WS269 and species was set to C. elegans. Results of BLASTp search are listed in Appendix 1—table 2.

### Amino acid sequence alignment

hAChE was aligned with Ppa-UAR-1, CEST-1.1, CEST-2.2, and CEST-4 was done using T-Coffee Multiple Sequence alignment (Notredame et al., 2000). Protein sequences for C. elegans CEST proteins are from WormBase. The AChE sequence was obtained from NCBI (accession number P22303). Amino acids were colored based on chemical properties: AVFPMILW = red (small + hydrophobic), DE = blue (acidic), RHK = magenta (basic), STYHCNGQ = green (hydroxyl + sulfhydryl + amine + glycine). See Figure 4—figure supplement 1 for results.

### Phylogenetic tree

The protein sequence of Ppa-UAR1 was submitted to an NCBI BLASTp search (Altschul et al., 2005) (restricted to species C. elegans, conditional compositional BLOSUM62, gap open cost:11, gap extension cost: 1, word size: 6) using Geneious software (Biomatters Inc). The top BLAST hits by E-value up to and including ace-3 were selected, and only the best scoring transcript variant was kept for each protein sequence hit. A total of 28 sequences were then imported into MEGA7 (Kumar et al., 2016) and aligned using MUSCLE (Edgar, 2004) (settings: gap open penalty: −2.9, gap extend 0, hydrophobicity multiplier 1.2, max. iterations 8, clustering method for all iterations: UPGMB, minimal diagonal length: 24). From this alignment, an Maximum Likelihood tree was built based on the JTT matrix-based model (Jones et al., 1992). Initial trees were built by applying Neighbor-Join and BioNJ algorithms to a matrix of pairwise distances estimated using a JTT model assuming uniform substitution rates across positions. Phylogeny confidence was tested using 200 bootstrap replications. The tree with the highest log likelihood (−22299.9282) is shown. At each branch, the percentage of bootstrap replicates containing the same branching event is denoted. The tree is drawn to scale, with branch lengths measured in the number of substitutions per site. The evolutionary history was inferred by using the Maximum Likelihood method based on the JTT matrix-based model (Jones et al., 1992). The tree with the highest log likelihood (−22299.9282) is shown. The percentage of trees in which the associated taxa clustered together is shown next to the branches. Initial tree(s) for the heuristic search were obtained automatically by applying Neighbor-Join and BioNJ algorithms to a matrix of pairwise distances estimated using a JTT model, and then selecting the topology with superior log likelihood value. The tree is drawn to scale, with branch lengths measured in the number of substitutions per site. The analysis involved 28 amino acid sequences. All positions containing gaps and missing data were eliminated. There were a total of 427 positions in the final dataset. Evolutionary analyses were conducted in MEGA7 (Kumar et al., 2016; Felsenstein, 1985).

### Nematode strains

Wild-type (N2) and glo-1(zu437) null animals were provided by the Caenorhabditis Genetics Center (CGC), which is funded by NIH Office of Research Infrastructure Programs (P40 OD010440). cest-2.2 mutant strains integrating N-terminal (mCherry-cest-2.2) or C-terminal mCherry (cest-2.2-mCherry) were generated by SunyBiotech. Generation of C. elegans and C. briggsae null mutants and revertants as well as generation of the cest-1.1 point mutant is described below. See Appendix 1—table 3 for a complete list of strains used in this study.

### C. elegans CRISPR mutagenesis for generation of cest null mutants

CRISPR/Cas9 mutagenesis was performed as in Wang et al., 2018. Briefly, C. elegans strain N2 was gene-edited by insertion of a 43-base-pair insertion that disrupts translation Appendix 1—table 8. Independent homozygous mutants were picked among the progeny of heterozygous F1 progeny of injected hermaphrodites and given distinct unique allele names. Reversion of mutants was accomplished in the same way.

### C. briggsae CRISPR mutagenesis for generation of glo-1 null mutants

The C. briggsae glo-1 mutants sy1382 and sy1383 were both created using the briggsae adaptation of the STOP-IN cassette method as described in Cohen and Sternberg, 2019 and Wang et al., 2018. Both strains were made using a successful insertion of the STOP-IN cassette into the middle of the first exon using the guide AACAAATCTCCGGATGATTG. To detect the insertion, we used forward primer GGGTGACCGCCCATTTATTG and reverse primer AAAGGCGCACATCTTGCTTC.

### C. elegans CRISPR mutagenesis for generation of the cest-1.1(dp683) allele encoding the S213A catalytic mutant

cest-1(dp683) was generated as previously described (Paix et al., 2015). Briefly, daf-2(e1368) mutant animals were injected with in-vitro-assembled Cas9-crRNA-tracrRNA complexes targeting cest-1.1 and the dpy-10 co-CRISPR gene and two 100 bp repair oligonucleotides containing the desired cest-1.1 mutation and the dpy-10(cn64) co-CRISPR mutation (Arribere et al., 2014). Sequences of the cest-1.1 crRNA and repair oligonucleotide are 5’ acctacCGCTACTATCATAC 3’ and 5’ GAAATTGAAAACTTTGGAGGAAATAAAAACAGAATTACATTGGCAGGGCATGCCGCTGGAGCAAGTATGATAGTAGCGgtaggtcacataaatgatacatttttg 3’, respectively. F1 Rol progeny of injected animals were picked and screened for the presence of the cest-1.1(dp683) mutation after egglay. F2 broods of F1 Rol animals that were heterozygous for cest-1.1(dp683) were screened for animals that were homozygous for cest-1.1(dp683) and either wild-type or heterozygous for cn64 at the dpy-10 locus. Subsequent broods were screened for wild-type dpy-10 animals to remove the co-CRISPR mutation.

### Nematode imaging

To image, gravid adult C. elegans were transferred to an agarose pad on a glass slide with 10 µM of levamisole to immobilize the worms. Microscopic analysis was performed using a Leica TCS SP5 Laser Scanning Confocal Microscope. Green autofluorescence was excited at 488 nm and the emission detector was set to 490–540 nm. mCherry was excited with 561 nm and the emission detector was set to 590–650 nm. Worms were imaged using the 100x objective.

### C. briggsae imaging

0.5 mL of 2 µM Lysotracker Deep Red (Thermo Fisher 1 mM stock in DMSO) was added to a 6 cm NGM plate seeded with 0.1 mL of E. coli OP50 and incubated in the dark for 24 hr at 20°C. L4 larvae of C. briggsae were added to the plate and allowed to grow in the dark for 24 hr at 20°C. To image, C. briggsae were transferred to an agarose pad on a glass slide with 10 µM of levamisole to immobilize the worms. Microscopic analysis was performed using a Zeiss Axio Imager Z2 florescence microscope with Apotome.

### Nematode cultures, mixed stage

Culturing began by chunking C. elegans or C. briggsae onto 10 cm NGM plates (each seeded with 800 µL of OP50 E. coli grown to stationary phase in Lennox Broth) and incubated at 22°C. Once the food was consumed, the cultures were incubated for an additional 24 hr. Each plate was then washed with 25 mL of S-complete medium into a 125 mL Erlenmeyer flask, and 1 mL of OP50 E. coli was added (E. coli cultures were grown to stationary phase in Terrific Broth, pelleted and resuspended at 1 g wet mass per 1 mL M9 buffer), shaking at 220 RPM and 22°C. After 70 hr, cultures were centrifuged at 5000 G for 1 min. After discarding supernatant, 24 mL H2O was added, along with 6 mL bleach, 900 µL 10 M NaOH and the mixture was shaken for 3 min to prepare eggs. Eggs were centrifuged at 5000 G, the supernatant was removed, and the egg pellet washed with 35 mL M9 buffer twice and then suspended in a final volume of 5 mL M9 buffer in a 50 mL centrifuge tube. Eggs were counted and placed on a rocker and allowed to hatch as L1 larvae for 24 hr at 22°C. 70,000 L1 larvae were seeded in 25 mL cultures of S-complete with 1 mL of OP50 and incubated at 220 RPM and 22°C in a 125 mL Erlenmeyer flask. After 72 hr, cultures were fed an additional 1 mL of OP50 and incubation continued. After an additional 48 hr, worms were spun at 1000 G 5 min and spent medium was separated from worm body pellet. Separated medium and worm pellet were flash frozen over liquid nitrogen until further processing. At least three biological replicates were grown for all mutant strains. Mutants were grown with parallel wildtype controls, and biological replicates were started on different days.

### Metabolite extraction

Lyophilized pellet and media samples were crushed and homogenized by shaking with 2.5 mm steel balls at 1300 rpm for 3 min in 30 s pulses while chilled with liquid nitrogen (SPEX sample prep miniG 1600). Thus powdered media and pellet samples were extracted with 15 mL methanol in 50 mL centrifuge tubes, rocking overnight at 22°C. Extractions were pelleted at 5000 g for 10 min at 4°C, and supernatants were transferred to 20 mL glass scintillation vials. Samples were then dried in a SpeedVac (Thermo Fisher Scientific) vacuum concentrator. Dried materials were resuspended in 1 mL methanol and vortexed for 1 min. Samples were pelleted at 5000 g for 5 min and 22°C, and supernatants were transferred to 2 mL HPLC vials and dried in a SpeedVac vacuum concentrator. Samples were then resuspended in 200 μL of methanol, transferred into 1.7 mL Eppendorf tubes, and centrifuged at 18,000 G for 20 min at 4°C. Clarified extracts were transferred to fresh HPLC vials and stored at −20°C until analysis.

### Preparation of exo-metabolome samples from staged starved and fed cultures

40,000 synchronized L1 larvae were added to 125 mL Erlenmeyer flasks containing 30 mL of S-complete medium. Worms were fed with 4 mL of concentrated OP-50 and incubated at 20°C with shaking at 160 RPM for: 12 hr (L1), 24 hr (L2), 32 hr (L3), 40 hr (L4) and 58 hr (gravid adults). For preparation of starved samples, each of the stages was starved for 24 hr after reaching their desired developmental stage in S-complete without OP-50. After incubation for the desired time, liquid cultures were centrifuged (1000 x g, 22°C, 1 min) and supernatants were collected. Supernatant was separated from intact OP-50 cells by centrifuging (3000 x g, 22°C, 5 min) and the resulting supernatants (exo-metabolome) were lyophilized. Lyophilized samples were homogenized with a dounce homogenizer in 10 mL methanol and extracted on a stirring plate (22°C, 12 hr). The resulting suspension was centrifuged (4000 g, 22°C, 5 min) to remove any precipitate before carefully transferring to an LC-MS sample vial. Three biological replicates were started on different days.

### Mass spectrometric analysis

High resolution LC-MS analysis was performed on a Thermo Fisher Scientific Vanquish Horizon UHPLC System coupled with a Thermo Q Exactive HF hybrid quadrupole-orbitrap high-resolution mass spectrometer equipped with a HESI ion source. 1 μL of extract was injected and separated using at water-acetonitrile gradient on a Thermo Scientific Hypersil GOLD C18 column (150 mm x 2.1 mm 1.9 um particle size 175 Å pore size, Thermo Scientific) and maintained at 40°C. Solvents were all purchased from Fisher Scientific as HPLC grade. Solvent A: 0.1% formic acid in water; solvent B: 0.1% formic acid in acetonitrile. A/B gradient started at 1% B for 5 min, then from 1% to 100% B over 20 min, 100% for 5 min, then down to 1% B for 3 min. Mass spectrometer parameters: 3.5 kV spray voltage, 380°C capillary temperature, 300°C probe heater temperature, 60 sheath flow rate, 20 auxiliary flow rate, one spare gas; S-lens RF level 50.0, resolution 240,000, m/z range 100–1200 m/z, AGC target 3e6. Instrument was calibrated with positive and negative ion calibration solutions (Thermo-Fisher) Pierce LTQ Velos ESI pos/neg calibration solutions.

### Feature detection and characterization

LC−MS RAW files from each sample were converted to mzXML (centroid mode) using MSConvert (ProteoWizard), followed by analysis using the XCMS (Smith et al., 2006) analysis feature in METABOseek (metaboseek.com). Peak detection was carried out with the centWave algorithm (Tautenhahn et al., 2008), values set as: 4 ppm, 320 peakwidth, 3 snthresh, 3100 prefilter, FALSE fitgauss, 1 integrate, TRUE firstBaselineCheck, 0 noise, wMean mzCenterFun, −0.005 mzdiff. XCMS feature grouping values were set as: 0.2 minfrac, 2 bw, 0.002 mzwid, 500 max, 1 minsamp, FALSE usegroup. METABOseek peak filling values set as: 5 ppm_m, 5 rtw, TRUE rtrange. Resulting tables were then processed with the METABOseek Data Explorer. Molecular features were filtered for each particular null mutant against all other mutants. Filter values were set as: 10 to max minFoldOverCtrl, 15000 to max meanInt, 120 to 1500 rt, 0.95 to max Peak Quality as calculated by METABOseek. Features were then manually curated by removing isotopic and adducted redundancies. Remaining masses were put on the inclusion list for MS/MS (ddMS2) characterization. Positive and negative mode data were processed separately. In both cases we checked if a feature had a corresponding peak in the opposite ionization mode, since fragmentation spectra in different modes often provide complementary structural information. To acquire MS2 spectra, we ran a top-10 data dependent MS2 method on a Thermo QExactive-HF mass spectrometer with MS1 resolution 60,000, AGC target 1 × 10^6, maximum IT (injection time) 50 ms, MS2 resolution 45,000, AGC target 5 × 10^5, maximum IT 80 ms, isolation window 1.0 m/z, stepped NCE (normalized collision energy) 25, 50, dynamic exclusion 3 s.

### Statistical analysis

Peak integration data from HPLC-MS analysis were log-transformed (Karpievitch et al., 2012) prior to statistical analysis. Significance of differences between average peak areas were then assessed using unpaired t-tests.

### MS2-based molecular networking

For the differential featuresidentified above, MS2 data was acquired. To generate the MS2 molecular network, Metaboseek version 0.9.6 was used. Using the MS2scans function, differential features were matched with their respective MS2 scan, using an m/z window of 5 ppm, and a retention time window of 15 s. To construct the molecular network, tolerance of the fragment peaks was set to m/z of 0.002 or 5 ppm, minimum number of peaks was set to 5, with a 2% noise level. Once the network was constructed, a cosine value of 0.8 was used, and the number of possible connections was constrained to 5.

### Serine hydrolase dendrogram

The serine hydrolase list was reported previously (Chen et al., 2019). From this list, sequences were inputted into Geneious Prime (version 2020.1.2 Biomatters). Sequences were aligned using Clustal Omega, neighbor joining alignment. Dendrogram tree was generated using the Geneious Tree Builder; Genetic distance model Jukes-Cantor, Tree build method UPGMA, no outgroup, Bootstrap resampling, random seed 508,949, 300 interactions, support threshold of 1. CEST enzymes were colored red and PPA-UAR-1 was colored blue (Figure 1—figure supplement 1).

### Synthetic procedures

![Scheme 1.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig6-v2.jpg)

To a solution of anthranilic acid (33, 300 mg, 2.18 mmol) in 4 mL of THF and H2O (1:1), Boc-anhydride (521 mg, 2.39 mmol) was added, and 2 M NaOH was added to the mixture until pH 10 was reached. The reaction mixture was stirred at room temperature. After 23 hr, the solution was concentrated in vacuo, and 15% citric acid aqueous solution was added until pH 4 was reached. The white precipitate was filtered off and dried under vacuum to provide 2-((tert-butoxycarbonyl)amino)benzoic acid (SI-1, 497 mg, 96%) as a white solid. 1H NMR, 600 MHz, chloroform-d: δ (ppm) 10.06 (s, 1H), 8.47 (dd, J = 8.7, 0.9 Hz, 1H), 8.08 (dd, J = 7.9, 1.5 Hz, 1H), 7.57 (dt, J = 7.9, 1.5 Hz, 1H), 7.03 (dt, J = 7.2, 1.2 Hz, 1H), 1.55 (s, 9H).

![Scheme 2.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig7-v2.jpg)

To a stirred solution of N-(tert-butoxycarbonyl)anthranilic acid (Krueger et al., 2008) (SI-1, 10 mg, 0.042 mmol) in dimethylformamide, 1-(3-dimethylaminopropyl)−3-ethylcarbodiimide hydrochloride (EDC·HCl, 20.1 mg, 0.105 mmol) was added. The mixture was stirred at room temperature for 5 min, and 4-dimethylaminopyridine (DMAP, 18.1 mg, 0.105 mmol) and N-β-glucopyranosyl indole (iglu#1, 15, 9.8 mg, 0.0351 mmol) were added. The reaction mixture was stirred at room temperature. After 5 hr, the mixture was concentrated in vacuo to yield a viscous oil, which was dissolved in 1.4 mL of a 5:2 mixture of dichloromethane and methanol. Trifluoroacetic acid (TFA, 0.5 mL) was added slowly and the reaction mixture was stirred at room temperature. After 3 hr, the mixture was concentrated in vacuo. Preparative HPLC provided a pure sample of iglu#3 (34, 0.8 mg, 5.7%). See Appendix 1—table 4 for NMR spectroscopic data of iglu#3.

HRMS (ESI) m/z: [M - H]- calcd for C21H21N2O6- 397.13938; found 397.14017.

![Scheme 3.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig8-v2.jpg)

To a stirred solution of nicotinic acid (7.3 mg, 0.059 mmol) in a mixture of dimethylformamide and dichloromethane (1:1), EDC·HCl (28.4 mg, 0.148 mmol) was added. The mixture was stirred at room temperature for 30 min, before DMAP (18.1 mg, 0.148 mmol) and N-β-glucopyranosyl indole (iglu#1, 15, 13.8 mg, 0.0494 mmol) were added. The reaction mixture was stirred at room temperature for 20 hr, the mixture was concentrated in vacuo, and flash column chromatography on silica using a gradient of 0–25% methanol in dichloromethane afforded iglu#5 (SI-2, 2.5 mg, 13.9%) as a colorless oil. See Appendix 1—table 5 for NMR spectroscopic data of iglu#5.

HRMS (ESI) m/z: [M + H]+ calcd for C20H21N2O6+ 385.13941; found 385.14038.

![Scheme 4.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig9-v2.jpg)

To a stirred solution of tiglic acid (5.0 mg, 0.050 mmol) in a 1:1 mixture of dimethylformamide and dichloromethane, EDC·HCl (23.9 mg, 0.125 mmol) was added. The mixture was stirred at room temperature for 30 min, and DMAP (15.2 mg, 0.125 mmol) and N-β-glucopyranosyl indole (iglu#1, 15, 11.6 mg, 0.0416 mmol) were added. The reaction mixture was stirred at room temperature for 22 hr and then concentrated in vacuo. Flash column chromatography on silica using a gradient of 0–30% methanol in dichloromethane afforded iglu#7 (SI-3, 2.5 mg, 11.3%) as a colorless oil. See Appendix 1—table 6 for NMR spectroscopic data of iglu#7.

HRMS (ESI) m/z: [M + H]+ calcd for C19H24NO6+ 362.15981; found 362.16025.

![Scheme 5.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig10-v2.jpg)

To a suspension of pyrrole-2-carboxylic acid (6.0 mg, 0.054 mmol) in dichloromethane, oxalyl chloride (14 µL, 0.163 mmol) was added slowly, followed by dimethylformamide (1 µL, 0.0129 mmol). The mixture was stirred at room temperature for 18 hr and then concentrated to dryness in vacuo. The residue was re-dissolved in dimethylformamide (2 mL) containing N-β-glucopyranosyl indole (iglu#1, 15, 10.8 mg, 0.0387 mmol). Triethylamine (45 µL, 0.324 mmol) was added, and the reaction was stirred at 35°C for 7 days. Subsequently the mixture was concentrated in vacuo, and flash column chromatography on silica using a gradient of 0–30% methanol in dimethylformamide afforded iglu#9 (SI-4, 1.5 mg, 10.4%) as a colorless oil. See Appendix 1—table 7 for NMR spectroscopic data of iglu#9.

HRMS (ESI) m/z: [M + H]+ calcd for C19H21N2O6+ 373.13941; found 373.14026.

![Scheme 6.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig11-v2.jpg)

To a stirred solution of Boc-AA (2 mg, 0.00 84 mmol) in dimethylformamide, 1-(3-dimethylaminopropyl)−3-ethylcarbodiimide hydrochloride (3.9 mg, 0.0203 mmol) was added. The mixture was stirred at room temperature for 5 min, and 4-dimethylaminopyridine (2.5 mg, 0.0203 mmol) and angl#1 (17, 2 mg, 0.0068 mmol) were added. The reaction mixture was stirred at room temperature. After 5 hr, the mixture was concentrated in vacuo. The crude product was dissolved in 0.55 mL dichloromethane and methanol (10:1), and trifluoroacetic acid (500 µL) was added slowly. The reaction mixture was stirred at room temperature for 3 hr and then was concentrated in vacuo, affording angl#3 (SI-5).

HRMS (ESI) m/z: [M + H]+ calcd for C20H23N2O7+ 403.14998; found 403.15100.

![Scheme 7.](https://cdn.elifesciences.org/articles/61886/elife-61886-fig12-v2.jpg)

p-Aminobenzoic acid (Chem-Impex) (8) was dissolved in warm dichloromethane (DCM) containing triethylamine (0.1 eq). EDC·HCl (Amresco Biochemicals) (1 eq), and di-tert-butyl glutamate (1 eq) was added to the reaction mixture. N,N-Dimethylaminopyridine (1.1 eq) was then added and the resulting mixture was stirred at room temperature for 24 hr and then extracted with ethyl acetate. The combined extractswere dried with sodium sulfate and evaporated to dryness in vacuo. The crude product was dissolved in DCM, and trifluoroacetic acid was added (100 eq). The reaction was then stirred for 6 hr at room temperature. TFA and DCM were evaporated off to yield crude PABA-glutamate (29). 1H NMR, 600 MHz, methanol-d4: δ (ppm) 7.93 (d, J = 8.6 Hz, 2H), 7.37 (d, J = 8.5 Hz, 2H), 4.61 (dd, J = 5.0, 9.3 Hz, 1H), 2.09–2.28 (m, 4H).

NMR spectra appendix. NMR spectra of synthetic intermediates and newly identified metabolites.
