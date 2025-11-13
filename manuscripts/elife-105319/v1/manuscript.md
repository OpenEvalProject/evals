# Molecular dynamics of the matrisome across sea anemone life history

## Authors

- Bruno Gideon Bergheim<sup>1</sup>
- Alison G Cole<sup>2</sup> ([ORCID: 0000-0002-7515-7489](https://orcid.org/0000-0002-7515-7489))
- Mandy Rettel<sup>3</sup> ([ORCID: 0000-0002-8304-3385](https://orcid.org/0000-0002-8304-3385))
- Frank Stein<sup>3</sup>
- Stefan Redl<sup>4</sup>
- Michael W Hess<sup>5</sup> ([ORCID: 0000-0002-5154-3553](https://orcid.org/0000-0002-5154-3553))
- Aissam Ikmi<sup>3</sup>
- Suat Özbek<sup>1</sup> ([ORCID: 0000-0003-2569-3942](https://orcid.org/0000-0003-2569-3942)) †

### Affiliations

1. University of Heidelberg, Centre for Organismal Studies, Department of Evolutionary Neurobiology Heidelberg Germany ([ROR:038t36y30](https://ror.org/038t36y30))
2. Department of Neurosciences and Developmental Biology, Faculty of Life Sciences, University of Vienna Vienna Austria ([ROR:03prydq77](https://ror.org/03prydq77))
3. European Molecular Biology Laboratory Heidelberg Germany ([ROR:03mstc592](https://ror.org/03mstc592))
4. Institute of Neuroanatomy, Medical University of Innsbruck Innsbruck Austria ([ROR:03pt86f80](https://ror.org/03pt86f80))
5. Institute of Histology and Embryology, Medical University of Innsbruck Innsbruck Austria ([ROR:03pt86f80](https://ror.org/03pt86f80))

† Corresponding author

## Abstract

The evolutionary expansion of extracellular matrix (ECM) molecules has been crucial for the establishment of cell adhesion and the transition from unicellular to multicellular life. Members of the early diverging metazoan phylum Cnidaria offer an exceptionally rich perspective into the metazoan core adhesome and its original function in developmental and morphogenetic processes. Here, we present the ensemble of ECM proteins and associated factors for the starlet sea anemone Nematostella vectensis based on in silico prediction and quantitative proteomic analysis of decellularized mesoglea from different life stages. The integration of the matrisome with single-cell transcriptome atlases shows that gastrodermal cells are the primary producers of Nematostella’s complex ECM, confirming the homology of the cnidarian inner cell layer with bilaterian mesoderm. The transition from larva to polyp is marked by an upregulation of metalloproteases and basement membrane components including all members of an unusually diversified SVEP1/Polydom family, suggesting massive epithelial remodeling. The enrichment of Wnt/PCP pathway factors during this process further indicates directed cell rearrangements as a key contributor to the polyp’s morphogenesis. Mesoglea maturation in adult polyps involves wound response proteins indicating shared molecular patterns in growth and regeneration. Our study identifies conserved matrisomal networks that coordinate transitions in Nematostella’s life history.

## Introduction

The evolution of extracellular matrix, a complex network of secreted, typically modular proteins, is closely linked to the emergence of metazoan life forms (Hynes, 2009; Hynes, 2012; Naba, 2024; Ozbek et al., 2010; Rokas, 2008). While some ECM components, such as integrins and cadherin receptors, can be traced back to unicellular organisms (Nichols et al., 2012; Sebé-Pedrós et al., 2010), early diverging cnidarians (hydroids, jellyfish, corals, and sea anemones) are believed to possess one of the most complete adhesomes among non-bilaterian clades (Ozbek et al., 2010; Tucker and Adams, 2014). Cnidarians, the sister group to bilaterians, are characterized by a simple body plan with a central body cavity and a mouth opening surrounded by tentacles. They are diploblastic organisms, consisting of an outer epithelium and an inner gastrodermis separated by a complex ECM called mesoglea (Bergheim and Özbek, 2019; Sarras, 2012). The mesoglea, which is best studied in the freshwater polyp Hydra, forms a flexible, tri-laminar structure. It is composed of a central, amorphous interstitial matrix (IM) interspersed with collagenous fibrils, sandwiched between two thin layers of basement membrane (BM) (Aufschnaiter et al., 2011; Bergheim and Özbek, 2019; Sarras et al., 1991; Shimizu et al., 2008). Studies in Hydra have shown that the mesoglea can be separated intact from the epithelial cell sheets by a freeze-thaw technique (Day and Lenhoff, 1981; Veschgini et al., 2023). Previously, we analyzed the proteome of decellularized Hydra mesoglea and identified 37 unique protein sequences (Lommel et al., 2018), including most of the described core matrisome components (Sarras, 2012). Among medusozoans (jellyfish and hydroids), hydras stand out for having lost the free-swimming medusa form. They also lack a planula larva stage from which anthozoans (corals and sea anemones) typically produce sessile polyps. We therefore hypothesized that a cnidarian species with a complex life cycle could offer a more comprehensive picture of the non-bilaterian ECM repertoire. Here, we analyzed the matrisome of the anthozoan starlet sea anemone Nematostella vectensis by employing in silico predictions of ECM proteins that were partially confirmed by a subsequent proteomic analysis of decellularized mesoglea. We detected a rich collection of matrisome proteins, comparable in its core matrisome complexity to vertebrate species (Naba et al., 2012). Furthermore, mapping of our matrisome data onto a previously established single-cell transcriptome dataset (Cole et al., 2024; Steger et al., 2022) revealed a prominent role of the gastroderm in ECM production. Cnidocytes, which produce the cnidarian stinging organelle, are characterized by a distinct set of ECM proteins that significantly contribute to the complexity of the cnidarian matrisome. Quantitative proteomics of mesoglea samples from different life stages (larva, primary, and adult polyp) showed that, while the larval mesoglea contained only a few exclusively enriched factors, the transition from the larval stage to primary polyp was marked by an upregulation of a large fraction of the matrisome. This set of proteins included many metalloproteases and basement membrane factors, indicating significant epithelial reorganization. Remarkably, all members of an unusually diverse SVEP1/Polydom family were upregulated during this morphogenetic process, implicating a conserved role of this protein family for epithelial morphogenesis. Additionally, a significant enrichment of Wnt/planar cell polarity (PCP) signaling components, such as ROR2 and protocadherin Fat4, supports that directed cell movements underlie the axial elongation and morphogenesis of the polyp (Stokkermans et al., 2022). The final transition to the adult animal involves an increased addition of elastic fiber components to the mesoglea and matricellular factors associated with wound healing, indicating common ECM-associated mechanisms in regeneration, growth, and tissue differentiation.

## Results

### Molecular composition and structure of the Nematostella ECM

To investigate the components and dynamics of the ECM throughout various life stages of Nematostella vectensis, we employed a protocol for obtaining decellularized mesoglea, originally developed for Hydra (Day and Lenhoff, 1981; Lommel et al., 2018; Veschgini et al., 2023). We isolated mesogleas from larvae at three days post-fertilization (3 dpf), primary polyps at 10 dpf, and from small adult polyps that were at least 1 year old. Protein extraction was performed under strongly reducing conditions and at high temperatures (90°C) to solubilize the cross-linked protein network of the ECM. The extracted proteins were digested with trypsin and analyzed using quantitative mass spectrometry (Figure 1A). Extensive studies in both vertebrates and invertebrates have identified specific characteristics of ECM proteins, typically based on conserved domains and domain arrangements (Engel, 1996; Hohenester and Engel, 2002; King et al., 2008; Naba et al., 2012; Ozbek et al., 2010; Tucker and Adams, 2014). Building on this knowledge and a de novo annotation of all predicted Nematostella protein models using InterProScan (Jones et al., 2014), we identified 1812 potential ECM proteins (Figure 1B). These were further classified into orthogroups based on similarity using OrthoFinder (Emms and Kelly, 2019). To refine this analysis, we also predicted in silico matrisomes from protein models of several early-branching metazoan species, including two choanoflagellates, two sponges, three ctenophores, nine additional representative cnidarians, and two placozoan species. SignalP (Teufel et al., 2022) was used to confirm the presence of signal peptides, while DeepLoc (Thumuluri et al., 2022) was employed to predict the cellular localization of the matrisome draft. Additionally, we explored the closest BLAST hits in the NCBI and SwissProt databases. After manually excluding duplicates and sequencing artifacts, we narrowed down the number of high-confidence ECM genes defined by the possession of a bona fide ECM domain (Hynes and Naba, 2012) to 829 (Figure 1B). Each protein sequence was manually reviewed, with annotations assigned based on domain predictions, UniProt identifiers, and comparisons to known ECM proteins. Our subsequent mass spectrometry analysis initially identified a total of 5286 proteins. However, we suspected that a significant portion might be cellular contaminants originating from residual amoebocytes within the mesoglea (Tucker et al., 2011), which could not be completely removed during the isolation procedure. To address this, we used our curated in silico list of 829 candidate ECM genes as a filter and identified 287 ECM components in the isolated Nematostella mesogleas, of which 210 belonged to the matrisome (Figure 1B, Supplementary files 1 and 2). This number exceeds the previously reported 37 matrisomal proteins in Hydra (Lommel et al., 2018), suggesting a greater compositional diversity in Nematostella. A comparison of mesoglea samples of both species resolved by protein gel electrophoresis confirmed the higher complexity of the Nematostella mesoglea, particularly in the lower molecular weight fraction (Figure 1—figure supplement 1). The discrepancy between the number of predicted ECM proteins and those confirmed by mass spectrometry can be attributed to the exclusion of nematocysts from the mesoglea isolates, despite their substantial contribution to the matrisome (as shown below). Furthermore, soluble factors and transmembrane receptors are likely underrepresented in the mesoglea isolates. We further organized our curated dataset following the classification proposed by Hynes and Naba, who introduced the concept of a ‘core’ matrisome, characterized by 55 signature InterPro domains, including EGF, LamG, TSP1, vWFA, and collagen (Hynes and Naba, 2012). Within this core matrisome, we identified 241 proteins, including collagens, proteoglycans, and ECM glycoproteins (e.g. laminins; Fahey and Degnan, 2012) and thrombospondins (Shoemark et al., 2019; Tucker et al., 2013; Figure 1C, Supplementary file 1). Additionally, we identified a set of 310 ‘matrisome-associated’ factors. This group includes molecules that (i) have structural or functional associations with the core matrisome, (ii) are involved in ECM remodeling (e.g. metalloproteases), or (iii) are secreted proteins, including growth factors. In summary, the Nematostella matrisome comprises 551 proteins, representing approximately 3% of its proteome (Artamonova and Mushegian, 2013) and roughly half the size of the human matrisome with 1056 proteins (Naba et al., 2012). While the Nematostella core matrisome is comparable to that of bilaterians, vertebrate species exhibit a dramatic expansion in ECM-associated factors (Figure 1D). The remaining non-matrisomal 278 proteins, identified through negative selection based on exclusive domain lists for each ECM category (Naba et al., 2012), were assigned to the ‘adhesome’ category primarily comprising transmembrane adhesion receptors (e.g. cadherins and IgCAM-like molecules) or categorized as ‘other’ ECM domain-containing proteins including proteins with specialized functions, such as venoms or stress and injury response proteins (Figure 1B and C, Supplementary file 1). Additionally, 17 proteins could not be confidently assigned to any category but were retained in the dataset as candidates for future functional characterization.

![Figure 1.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig1-v1.jpg)

**Figure 1.:** (A) Mesoglea from larvae, primary polyps, and adults was decellularized and analyzed by mass spectrometry. In parallel, an in silico matrisome was predicted using a computational approach and curated manually. (B, C) 1812 potential ECM proteins were predicted bioinformatically. The manually curated list of ECM factors consists of 829 proteins. The curated ECM proteins were sorted into core matrisome and matrisome-associated groups, which together constitute the Nematostella matrisome (551 proteins). The remaining non-matrisomal proteins are categorized as ‘adhesome’ that include transmembrane receptors, and ‘other’ ECM domain-containing proteins, which include adhesive proteins, venoms, enzymes, ion channels, stress and injury response factors, and diverse uncharacterized proteins (see Supplementary file 1 for detailed annotations and sub-categories). In total, 287 ECM proteins were confirmed by mass spectrometry analysis, 210 of which belong to the matrisome and 47 to the ‘adhesome’. (D) Comparison of the Nematostella matrisome size with published matrisomes of other species. While the complexity of the Nematostella core matrisome is comparable to that of vertebrates, the number of ECM-associated proteins is disproportionally lower. The Drosophila core matrisome is characterized by significant secondary reduction. (E) Laminin antibody stains the bilaminar structure of the BL (magenta) at the base of the epithelial cell layers, while the pan-Collagen antibody (yellow) detects the central IM. Scale bar, 10 μm. The three life stages of Nematostella before (F–H) and after (I–K) decellularization. The mesoglea is stained with Laminin antibody to demonstrate its structural preservation and by DAPI (cyan) to visualize residual nuclei and nematocysts. The decellularized mesoglea retains morphological structures such as tentacles (t) and mesenteries (m). Scale bars: F, G, I, J, 100 µm; H, K, 1 mm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Mesogleas were prepared from adult animals and dissolved in lithium dodecylsulfate buffer containing 1 M DTT. After heating at 90°C for 30 min, 130 mg of each sample was loaded on a 4–12% gradient gel. The molecular mass of marker proteins (M) is as indicated. Uncropped gel images are provided in Figure 1—figure supplement 1—source data 1 and 2.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) The laminin antibody was raised against a peptide sequence of the Nv laminin gamma-1 chain indicated by the boxed area. (B) The collagen antibodies were raised against an epitope representing a consensus sequence of fibrillar collagens (NvPanCol) and unique sequences in NvCol4b and NvCol2c as indicated. Mark that in the consensus sequence, the central cysteine residue was replaced by a serine to prevent disulfide formation.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Electron microscopy of the larvae with ectoderm (ec), gastroderm (ga), and an only 0.5-μm-thick mesoglea (asterisk) in between. (B) The IM of cryofixed larval mesoglea displays scarce, quite thin filaments, embedded in amorphous compounds. The basement membrane (BM: arrows) appears rather delicate at this developmental stage, measuring about 70 nm. (C) The mesoglea thickens into a triangular shape at the septa branching points. (D) Cross section of a larva stained with DAPI (cyan) and laminin antibody (magenta). DAPI hardly enters the gastroderm. The mesoglea and developing septa are shown by laminin staining. (E) The triangular expansion of the mesoglea at the septa branch is lined with laminin staining while the central region does not show any signal. (F) Electron micrograph of the septa branch. The BM is overlaid in magenta. The central region of the septa triangle is filled with loose fibrillar material. (Scale bars: A, F=1 μm, B=0.5 μm, D=100 μm, E=10 μm). (G, H) EM of the primary polyp mesoglea (asterisk) and adjacent epithelia (ec, ga). The mesoglea is now about 1.5 μm thick with numerous, haphazardly arranged about 13 nm thick and 6 nm thin fibrils in the IM. The BM (arrows) has thickened, thus, matured as well, and forms distinct, dense, about 130-nm-thick meshworks lining the epithelia. (I) Whole mount staining of a tentacle bud stage stained with DAPI and laminin antibody. (J) At the aboral end, the BM is expanded (asterisk) into the ectodermal layer forming a knot-like structure. (K-L’) Scheme and electron micrographs of the ECM fiber orientation at different sites of the primary polyps’ body (ec highlighted in rose, ga in blue, ECM in gray/green). (L) The filaments/fibrils in the region of the body column are loosely oriented along the oral-aboral (o–a) axis following the overall orientation of the mesoglea. (L’) At the aboral end, the fibrils are densely packed forming a plug-like structure parallel to the o-a axis (overlaid in green). Scale bars: G=1 μm; H=0.5 μm; I=100 μm, J=10 μm. L, L’=1 μm. (M–P) Immunoelectron microscopy of mesoglea compounds, performed on thawed cryosections. (M) Laminin immunogold label (arrows) along the plasma membrane of the ECM lining muscle cells (m). (N) Col4 label located at the BM. (O) PanCol is predominantly found throughout the IM. (P) Col2c label in the IM. Scale bars: M-P=0.25 μm.

To validate the preservation of the isolated ECM, we generated polyclonal antibodies targeting unique peptide sequences in laminin gamma 1 (anti-Lam), type IV collagen NvCol4b (anti-Col4), a specific fibrillar collagen NvCol2c (anti-Col2), and a consensus motif for several Nematostella fibrillar collagens (anti-PanCol; Figure 1—figure supplement 2). We then performed immunofluorescence confocal microscopy on Nematostella whole mounts and decellularized mesoglea from all life stages (Figure 1E–K). Consistent with recent findings in Hydra (Veschgini et al., 2023), the in vivo and ex vivo images exhibited similar patterns along the polyp’s body, indicating the structural integrity of the mesoglea after decellularization (Figure 1F–K). In cross-sections, the laminin antibody stained the thin double layer of the basement membrane (BM) lining the two epithelia, while the PanCol antibody detected the intervening fibrous layer of the interstitial matrix (IM; Figure 1E). Both antibodies also showed diffuse staining at the apical surface of ectodermal cells, likely due to the sticky nature of the glycocalyx. Ultrastructural examination of the mesoglea revealed a mean thickness of approximately 0.5 µm in larvae and 1.5 µm in primary polyps (Figure 1—figure supplement 3A–B, G–H, Supplementary file 3). In the triangular areas at the base of the gastrodermal mesenteric folds, the mesoglea was expanded (Figure 1—figure supplement 3C–F). The BM lining the epithelia of larvae was very delicate, measuring only 70 nm, and the IM appeared as a loose array of thin fibrils (Figure 1—figure supplement 3B). Primary polyps possessed a distinct BM, with a thickness of approximately 130 nm, appearing as a dense meshwork of fibrils (Figure 1—figure supplement 3H, Supplementary file 3). Previous reports (Tucker et al., 2011) indicated that the IM in older primary polyps was interspersed with thin fibrils of about 5 nm and extended thick fibrils of about 20–25 nm. Our samples from younger primary polyps (Figure 1—figure supplement 3H) showed thin fibrils of approximately 6 nm and thick ones of about 13 nm, with occasional fibrils of up to 27 nm (Supplementary file 3). Immunostainings with the laminin antibody revealed a thickened mesoglea at the aboral pole of the polyp, forming an unusual knot-like structure (Figure 1—figure supplement 3J). Ultrastructural analysis showed that the fibrils in this region were densely packed and aligned along the oral-aboral axis (Figure 1—figure supplement 3K–L), possibly providing a rigid attachment site for the mesentery retractor muscles. Immunoelectron microscopy confirmed the observations from immunofluorescence: anti-Lam immunogold labeling was primarily localized along the plasma membrane of ECM-lining cells, anti-Col4 labeling was found at the BM (Figure 1—figure supplement 3M–N), and anti-PanCol labeling was predominantly distributed throughout the IM, with a similar pattern observed for the anti-Col2 antibody (Figure 1—figure supplement 3O–P).

### Cell-type specificity of matrisome expression

Recently, single-cell RNA sequencing has been applied to identify the origin of neuroglandular cell lineages in Nematostella (Steger et al., 2022), hypothesize on the origin of muscle cell types (Cole et al., 2023), and catalog the distribution of cell states associated within all tissue types (Cole et al., 2024). We made use of this developmental cell type atlas to determine the cell-type specificity of matrisomal gene expression. Expression profiles for all ECM genes across the entire life cycle are available in the supplementary data (Supplementary file 4). We calculated an average expression score for each of the ECM gene sets (core and associated matrisome, adhesome/other) and found above average scores for the core matrisome associated with the mature gastrodermis and developing cnidocytes, and to a lesser extent also for the other two categories (Figure 2A and B). Core matrisome genes also showed additional high expression scores within an uncharacterized gland cell type (GD.1), matrisome-associated genes within the digestive gland set, and adhesome/other genes within the maturing cnidocytes (Figure 2A and B). We looked specifically at the distribution of core matrisome genes across all cell states and generated a list of differentially up-regulated genes (Supplementary file 5; Figure 2—figure supplement 1). Of note is the absence of any differentially expressed core matrisome factors within the ectodermal tissues, and contrastingly, a large set that are specific to either the mesoendodermal inner cell layer (gastrodermis) or cnidocytes (Figure 2B). We also find sets of core matrisome genes that are specific to different secretory gland cell types, including mucin-producing, digestive-enzyme producing, and uncharacterized S2-class cell types. Interestingly, the gland cell-specific matrisome genes include several of the Polydom family members upregulated during larva-to-primary polyp transition (see below). Altogether, these expression profiles suggest that core components of the mesoglea (collagens, laminins) are produced from the inner cell layer, and that a large set of ECM glycoproteins and all of the minicollagens David et al., 2008; Zenkert et al., 2011 have been recruited into the formation of the cnidarian synapomorphy, the cnidocytes.

![Figure 2.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig2-v1.jpg)

**Figure 2.:** (A) Dimensional reduction cell plot (UMAP) highlighting cell clusters showing over-abundant expression of the core matrisome, matrisome-associated, and adhesome/other gene sets. Expression values correspond to gene module scores for each set of genes. (B) Dotplot expression profiles of upregulated genes of the core matrisome across cell type partitions, separated across phases of the life cycle. Illustrated are the top 5 genes with expression in at least 20% of any cell state cluster, calculated to be upregulated with a p-value of ≤ 0.001. See Supplementary file 5 for a full list of differentially expressed core matrisome genes. Larva (red colour scale) = 18 hr:4 day samples; Primary Polyp (orange colour scale) = 5:16 day samples; Adult (blue colour scale) = tissue catalog from juvenile and adult specimens. (C) Nematostella collagens. Domain organization of matrisome proteins containing a collagen triple helix as core element. The proteins are categorized into fibrillar and basement membrane collagens, short-chain collagens, and nematocyte-specific minicollagens.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Dotplot expression profiles across all cell-state clusters, separated across phases of the life cycle. Cell states are grouped and colored according to tissue-type partitions, and genes are grouped by category. Expression scale is the same as in Figure 2. Abbreviations for cell state identities are explained in the Supplementary file 8.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Dot plot expression profiles of all identified collagen-coding genes across cell type partitions, separated across phases of the life cycle. Cell states are grouped and colored according to tissue-type partition. Expression scale is the same as in Figure 2. Abbreviations for cell identities are explained in the Supplementary file 8.

Collagens constitute the primary structural components of the animal ECM and, being a highly diverse family of triple helical proteins (Fidler et al., 2018), form a significant part of the core matrisome. Vertebrate collagens consist of 28 types (I-XXVIII) categorized as fibril-forming, network or beaded filament-forming, and transmembrane collagens (Kadler et al., 2007). Type IV collagen, a major constituent of basement membranes, is considered to be a primordial component of the animal ECM based on studies in ctenophores that lack fibrillar collagens but display a remarkable diversity of collagen IV genes (Draper et al., 2019; Fidler et al., 2017). Our analysis revealed 12 bilaterian-type collagens (Figure 2C) with conserved C-terminal non-collagenous trimerization domains (NC1) and extended triple helical stretches of ~1000 residues, including two sequences for type IV collagen (NvCol4a/b) together with a peroxidasin homolog (NV2.13306), indicating the presence of sulfilimine cross-links that stabilize the Nematostella BM (Fidler et al., 2014). In Hydra, which lacks this specific post-translational modification, six collagen genes have been identified through cDNA cloning and proteomic analysis (Deutzmann et al., 2000; Fowler et al., 2000; Lommel et al., 2018; Zhang et al., 2007). We have classified the collagens according to the Hydra nomenclature (Zhang et al., 2007) and identified three isoforms of NvCol1, each comprising an isolated minor triple helical domain at the N-terminus (Figure 2C, upper panel). In addition, we detected four NvCol2 paralogs, which contain an additional whey acidic protein 4 disulfide core (WAP) domain at the N-terminus. However, our dataset lacks a Hcol3-like collagen with alternating N-terminal WAP and vWFA domains, although it includes a protein with extensive WAP/vWFA repeats but lacking a collagen triple helix or NC1 domain (NV2.11346). NvCol5 consists of a continuous collagen domain with two minor interruptions following the signal peptide and is otherwise similar to NvCol1. We have not found sequences resembling Hcol6, which is characterized by triple helical sequences interrupted by multiple vWFA domains. Collagen XVIII-like, which is predicted to contain an unrelated Mucin-like insertion, includes an N-terminal Laminin-G/TSPN motif followed by a discontinuous central collagenous domain, similar to the BM-associated vertebrate α1(XVIII) collagen chains (Heljasvaara et al., 2017) and Drosophila Multiplexin (Meyer and Moussian, 2009). NvCol7 shares a similar domain organization but differs by having only a single interruption of the triple helix near the N-terminus. According to Exposito et al., the Nematostella fibrillar collagen sequences are phylogenetically related to A clade collagens that in mammalians possess a vWFC module in their N-propeptide supposed to have evolved from the cnidarian WAP domain (Exposito et al., 2008). NvCol7 is an exception and belongs to B clade collagens characterized by the possession of an N-terminal Laminin-G/TSPN domain.

Most of the Nematostella collagens show a broad expression in diverse gastrodermal cell populations throughout all life stages (Figure 2—figure supplement 2). NvCol2c is an exception, as it is predominantly expressed in neuronal cells of larvae, indicating a specialized function in neurogenesis. NvCol7 is distinguished by showing an expression both in gastrodermal cells and two small cnidocyte cell populations described by Steger et al. to be exclusive for planula larvae (Steger et al., 2022). Unlike the IM collagens, NvCol4a is additionally expressed during embryogenesis, emphasizing the pivotal role of the BM in organizing the epithelial tissue architecture during early development. In addition to these bilaterian-type collagens, we have identified four spongin-like proteins, which are short-chain collagens with derived NC1 domains (Figure 2C, middle panel). These molecules have been described as truncated variants of collagen IV with a wide distribution in several invertebrate phyla (Aouacheria et al., 2006). Except for NvSpongin-like-2, their expression is not aligned with that of fibrillar collagens, but is mostly restricted to neuroglandular cells (Figure 2—figure supplement 2). An additional set of ‘collagen-like’ sequences that comprise short triple helical stretches without additional domain motifs (Figure 2C, middle panel) is broadly expressed across cell types and developmental stages (Figure 2—figure supplement 2, Supplementary file 4). In contrast, the large set of minicollagens (Figure 2C, lower panel) is strictly aligned with the cnidocyte lineage as detailed below.

### A specialized cnidocyte matrisome

Cnidocytes, the stinging cells of cnidarians, are a key synapomorphy of this clade. Previous studies have demonstrated that, from a transcriptomic perspective, nematocyst capsule formation is distinct from the mature profile (Chari et al., 2021; Steger et al., 2022). We filtered the dataset of the 829 curated ECM protein-coding sequences for genes expressed within cnidocytes and found 298 genes that are detectable above average in at least 5% of any cnidocyte transcriptomic state (Figure 3—figure supplement 1, Supplementary file 6). We further separated this list of genes into those that are absent from non-cnidocyte states (101 genes: ‘exclusive’) or are also detected within more than 50% of the non-cnidocyte transcriptomic states (41 genes: ‘ubiquitous’; Figure 3A). We consider the remaining genes shared across cnidocyte and non-cnidocyte profiles (156: ‘shared’). Of the cnidocyte-specific genes, we examined the proportion of genes specific to either the capsule-building specification profiles (79: ‘specification’) or the maturation phase of cnidogenesis (24: ‘maturation’). Most of these genes are restricted to the specification phase, with a smaller subset associated with the mature transcriptomic profile (Figure 3A). The latter group includes several members of a vastly expanded family of Fibrinogen-related proteins (FREPs; Supplementary file 1), which have been implicated in innate immunity across various phyla (Zhou et al., 2024) and may function as venom components. In the ’shared' gene set, most genes are associated with the mature cnidocyte profile and overlap with various neuroglandular subtypes (Figure 3—figure supplement 1). This observation supports the hypothesis that the cnidocytes arose from an ancestral neuronal population (Richards and Rentzsch, 2014; Tournière et al., 2020). We then calculated a gene module score for each gene set to estimate specificity across the dataset, summarizing the specificity of each gene set (Figure 3B). Further examination of the gene lists reveals cnidocyte specificity of nematogalectins and minicollagens that serve as structural components for cnidocysts (Hwang et al., 2010; Kurz et al., 1991). Minicollagens, which have served as important phylum-specific genes (Holland et al., 2011), comprise a short collagen domain (about 15 Gly-X-Y repeats) flanked by proline-rich regions and terminal cysteine-rich domains (CRDs; David et al., 2008). We identified all five previously described Nematostella minicollagen sequences (Steger et al., 2022; Zenkert et al., 2011) (NvCol-1,–3, −4,–5, –6) along with four additional proteins with incomplete minicollagen sequence features, which we termed ‘minicollagen-like’ (Figure 2C). Intriguingly, we also identified a protein that combines features of both minicollagens and extended ECM-type collagens, suggesting a possible evolutionary origin of minicollagens from this gene family. This protein, NvNCol-7, contains a minicollagen pro-peptide sequence, proline-rich regions, and canonical N- and C-terminal CRDs (Tursch et al., 2016). Unlike previously described minicollagens, it includes an extended discontinuous collagen sequence of ~1000 residues, comprising 25 alternating blocks of mostly 12 or 15 Gly-X-Y repeats. These blocks are interrupted by either a single alanine or MPP/SPPSPP sequences, resembling degenerated collagen triplets. The presence of a minicollagen pro-peptide in this collagen suggests its expression in the cnidocyte lineage and secretion into the nematocyst vesicle as a structural component of cnidocyst walls or tubules (Adamczyk et al., 2010; Garg et al., 2023). This is confirmed by the single cell expression data, which show prominent and exclusive expression in cnidocyte lineages (Figure 2—figure supplement 2, Figure 3—figure supplement 1). Interestingly, Nematostella minicollagens exhibit differential expression across different cnidocyte subtypes, nematocytes, and spirocytes (Figure 3C). Spirocytes express NvCol-5 and NvNcol-like-3 and 4, while NvCol-1, 4, and 6 and NvNCol-7 are expressed within the nematocytes and NvCol-3 is expressed in both. Other cnidocyte-specific genes also show differential paralog expression between cnidocyte types, including the four NOWAs (Engel et al., 2002; Garg et al., 2023), and the vWFA domain proteins (Figure 3C). NvTSR-2 vs NvTSR-3 distinguish between the two nematocyte lineages, nem.1 and nem.2. These are postulated to be basitrichous haplonemas/isorhizas based on abundance and distribution across the adult tissue libraries, although these identities have not been validated. In summary, a significant fraction (32%) of matrisomal genes (176 of 551, Supplementary file 6) are expressed within the cnidocyte lineage. The proportion of cnidarian-specific factors in this subset is increased (85 of 176, 48%) as compared to the full matrisome (234 of 551, 42%, Supplementary file 1), supporting the notion that the cnidocyte proteome represents a specialized ECM adapted to the unique assembly process and biophysical requirements of the cnidarian stinging organelle (Balasubramanian et al., 2012; Ozbek, 2011).

![Figure 3.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig3-v1.jpg)

**Figure 3.:** (A) The distribution of cnidocyte-expressed genes categorized as ‘ubiquitous’ (blue: 41), ‘shared’ (red: 27), ‘mature-specific’ (green: 38), or ‘specification-specific’ (purple: 88). (B) Expression of the module scores of each gene subset across the main tissue-type data partitions, illustrated on UMAP dimensional reduction. (C) Sequential gene expression activation illustrated on a dot plot of top 5 differentially expressed genes (p-value ≤ 0.001) for each cnidocyte cell state. Nematocyte specification shares many genes, while spirocyte specification uses a distinct gene set. Nep.8, nematocyst-expressed protein 8 categorized as venom protein.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Dot plot expression profiles of matrisome genes expressed within the cnidocytes, plotted across all cell-type states. Genes are grouped according to degree of overlapping expression with other cell types, with ‘ubiquitous’ expression on top, followed by ‘shared’ expression, and then cnidocyte-specification specific genes, and mature cnidocyte-specific genes.

### Larva-to-polyp transition is marked by factors of basement membrane remodeling and Wnt/PCP signaling

Larva-polyp morphogenesis in Nematostella involves significant changes in body shape including the elongation of the body axis and the development of oral tentacles and internal mesenteries (Stokkermans et al., 2022). We performed quantitative proteomics using tandem mass tag labeling (TMT; see Figure 4—figure supplement 1 for normalization steps) to examine whether this process is accompanied by stage-specific variations of matrisome components. As shown above, 38% (210 of 551) of the matrisomal factors were detected by our mass spectrometry analysis (Figure 1B). We identified stage-specific mesoglea components by assigning hits (>twofold change and <0.05 false discovery rate [fdr]) using a modified t-test limma for each of the three life stage comparisons (Supplementary file 7). Globally, collagens and basement membrane proteoglycans constitute the bulk of the ECM in the core matrisome across all life stages, while secreted factors are the most abundant subcategory among matrisome-associated proteins (Figure 4A). As illustrated in the heat map in Figure 4B, the transition from larvae to primary polyp is characterized by a general increase of mesoglea components. 94 proteins were differentially upregulated in primary polyps while only four, including vitellogenin and its receptor that are crucial for lipid transport from the ECM into the oocyte (Lebouvier et al., 2022), were differentially abundant in larvae. The proteins enriched in primary polyps as compared to larvae include, in addition to various factors involved in general cell adhesion (e.g. cadherin-1, coadhesin-like proteins), two major functional groups (Figure 4C, Supplementary file 7): (1) factors involved in BM establishment and remodeling and (2) components of the Wnt/PCP signaling pathway. Both groups are indicative of a massive epithelial rearrangement, rather than cell proliferation, as a driver of larva-to-polyp transition (Stokkermans et al., 2022). Notably, in addition to laminins, the BM proteoglycan perlecan and numerous astacin, ADAMTS, and MMP family metalloproteases (see Figure 4—figure supplement 2 for an overview), the first group contained all members of an unusually expanded Polydom protein family (Figure 4E). Polydom/SVEP1 is a secreted multidomain ECM protein initially discovered in a murine bone-marrow stromal cell line (Gilgès et al., 2000). In humans, it is composed of eight different domains including an N-terminal vWFA domain, followed by a cysteine-rich ephrin receptor motif, Sushi/CCP and hyalin repeat (HYR) units, EGF-like domains, a central pentraxin domain, and a long tail of 28 Sushi domains terminating in three EGF repeats (Figure 4E). Polydom has recently been shown to be a ligand for the orphan receptor Tie1 and induce lymphatic vessel remodeling via PI3K/Akt signaling (Sato-Nishiuchi et al., 2023). Earlier studies have shown basement membrane deposition of Polydom and a role in epithelial cell-cell adhesion via integrin binding (Samuelov et al., 2017; Sato-Nishiuchi et al., 2012). The Hydractinia homolog has been characterized as a factor specific to i-cells and to be potentially involved in innate immunity (Schwarz et al., 2008). In comparison to vertebrate Polydoms, Hydractinia Polydom contains additional Pan/Apple, FA58C, and CUB domains, but has a reduced number of terminal Sushi repeats (Figure 4E). In our study, we identified a Nematostella Polydom homolog (NvPolydom1) that shares high similarity with the Hydractinia and Hydra proteins, suggesting a conserved arrangement of domains in cnidarians (Figure 4E). This includes a pentraxin-PAN/Apple-FA58C core structure, a tail consisting of six Sushi repeats, and 1–2 terminal CUB domains. Two additional paralogs, NvPolydom2 and NvPolydom3, exhibit differences in their central region, with NvPolydom2 lacking the PAN/Apple domain and NvPolydom3 lacking both PAN/Apple and FA58C domains. Furthermore, we discovered four shorter Polydom-like sequences that share a common EGF-Sushi-HYR-TKE structure but lack vWFA and Pentraxin domains, as well as the terminal Sushi repeats. These Polydom-like proteins, resembling a truncated N-terminal part of canonical Polydoms, possess additional domains at the N- or C-termini, such as thrombospondin type-1 repeat (TSR) or Ig-like domains. The shortest member, referred to as Polydom-related, lacks EGF-like modules and consists of the central Sushi, HYR, and TKE domains found in all Polydom-like sequences, suggesting that this core motif may be essential for biological function. All Polydom and Polydom-like paralogs are expressed within the putative digestive cell state GD.1, with two of these showing additional expression within the uncharacterized secretory cell type S2.tll.2&3 (Figure 4—figure supplement 3). This, together with the exceptionally high isoform diversity, indicates a requirement for genetic robustness to account for perturbations of the developmental process regulated by the Nematostella Polydoms. Given that mouse Polydom is essential for endothelial cell migration in a Tie-dependent manner (Sato-Nishiuchi et al., 2023), it is plausible that the Nematostella homologs could serve a similar function for rearrangement of epithelial cells along the BM during primary polyp morphogenesis. Interestingly, the top differentially abundant factor in the primary polyp mesoglea is a secreted integrin-alpha-related protein (sIntREP) containing three integrin-alpha N-terminal domains followed by a stretch of EGF repeats. It is an attractive hypothesis that sIntREP modulates integrin-dependent cell adhesion by Polydoms and other factors to facilitate cell migration. The second group of proteins that contains several components of the Wnt/PCP pathway, including ROR2, protocadherin Fat4-like, and hedgling, further supports the assumption of epithelial cell migration as a main driver of primary polyp morphogenesis. Wnt/PCP signaling, originally described in Drosophila melanogaster (Adler, 2002; Gubb and García-Bellido, 1982), has a well-established role in convergent extension movements of cells during gastrulation to facilitate the elongation of the embryo along its oral-aboral axis (Gao, 2012). Its ‘core’ factors include the transmembrane proteins Frizzled, Van Gogh/Strabismus, Flamingo, and the intracellular components Dishevelled, Prickle, and Diego (Simons and Mlodzik, 2008). An additional level of PCP within tissues is regulated by the unusually large protocadherins Fat and Dachsous that interact in a heterophilic manner and display cellular asymmetries (Matakatsu and Blair, 2004). Recently, the Hydra Fat-like homolog has been reported to be polarized along the oral-aboral axis and to organize epithelial cell alignment via organization of the actin cytoskeleton (Brooun et al., 2020). Hedgling is an ancestral, non-bilaterian member of the cadherin superfamily with high similarity to FAT and Flamingo cadherins (Adamska et al., 2007). It has a gastrodermal expression in the Nematostella primary polyp (Adamska et al., 2007), which it shares with Wnt5a and ROR2 (Supplementary file 4). ROR2, a highly conserved receptor tyrosine kinase, is the principal transducer of PCP signaling via Wnt5a in the Xenopus embryo (Hikasa et al., 2002; Schambony and Wedlich, 2007). It has also been reported to induce directional cell movements in mammals (He et al., 2008) and to induce filopodia formation as a prerequisite for directed cell migration (Nishita et al., 2006). Taken together, the molecular dynamics of the mesoglea revealed by quantitative mass spectrometry suggest that massive epithelial rearrangement and directed cell migration underlie axial elongation during primary polyp morphogenesis. Interestingly, IM components such as fibrillar collagens do not appear to contribute largely to this process. In contrast, the adult mesoglea is significantly enriched in elastic fiber components, such as fibrillins and fibulin. This compositional shift likely adds to the visco-elastic properties (Gosline, 1971a; Gosline, 1971b) of the growing body column (Figure 4B and D, Supplementary file 7). In addition, the adult mesoglea contains several matricellular factors associated with different aspects of wound healing in vertebrate organisms (Cárdenas-León et al., 2022). These include SPARC-related follistatin domain proteins, uromodulin, and periostin. The Nematostella uromodulin gene was previously reported to be highly upregulated in the wound ectoderm, likely contributing to the innate immune response (DuBuc et al., 2014). The same study showed a circular upregulation of the MMP inhibitor NvTIMP around the wound site. Indeed, while metalloproteases are similarly upregulated in adults and primary polyps, we observed a noticeable increase of diverse classes of protease inhibitors in adults (7 vs 2 in primary polyps), including TIMP, Kunitz and Kazal-type protease inhibitors, as well as thyroglobulin repeat proteins (Novinec et al., 2006; Supplementary file 7). This is indicative of a high degree of protease activity regulation in tissue morphogenesis during growth, as also observed during Nematostella whole-body regeneration (Schaffer et al., 2016). Taken together, the transition from the primary polyp to the adult is characterized by an increase of elastic fibrillar IM components contributing to the long-range elasticity and resilience of the mesoglea, and a recruitment of wound response factors that together with a complex network of proteases and protease inhibitors likely regulate growth, organogenesis, and tissue differentiation.

![Figure 4.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig4-v1.jpg)

**Figure 4.:** (A) Boxplot representation of normalized log2 TMT reporter ion intensities for different protein subgroups of the matrisome. ‘All’ represents all proteins in each respective dataset. A horizontal line indicates median TMT intensity in the complete dataset. (B) 2-log transformed median abundances of proteins across different life stages. The curated ECM proteins were filtered for proteins with a twofold change in any of the life stages and a false discovery rate of 0.05 using a moderated t-test (limma). The heatmap shows the 2-log transformed median abundance of 4 samples per life stage. Most proteins are upregulated in only one of the life stages. Notably, BM factors including all polydoms are upregulated in the primary polyp. Most ECM protein categories can be clearly divided into adult-specific and primary polyp-specific proteins underscoring the differential composition of the mesoglea at different life stages. (C, D) Volcano plots showing the differential abundance of proteins in the mesoglea extracts of the three different life stages. (C) Proteins involved in BM organization including all polydoms and in Wnt/PCP signaling are upregulated during larva-to-primary polyp transition as highlighted. (D) The adult mesoglea compared to primary polyps is characterized by an enrichment of elastic fibril components and matricellular glycoproteins involved in wound response and regeneration. gray = non-matrimonial background, orange = insignificant, magenta = differentially abundant matrisome proteins. (E) Domain organization of bilaterian and cnidarian polydoms. The Nematostella matrisome contains an expanded group of polydoms and polydom-like proteins, including three cnidarian-type polydom paralogs, four shorter polydom-like sequences, and a polydom-related protein, which contains only the core Sushi-HYR-TKE motif. Domain symbols: vWFA (light blue), EGF-like (purple), Sushi/SCR/CCP (orange), Hyalin repeat (red), Pentraxin (yellow), CUB (light green), Tyrosine-protein kinase ephrin (dark green), PAN/Apple (olive green), Ricin B-like (pink), Thrombospondin type-1 repeat (brown), Coagulation factor 5/8 (dark purple), Ig-like (dark grey).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Boxplot overview of data normalization steps for mesoglea samples. Raw TMT reporter ion intensities (left) were first cleaned for batch effects (middle) and further normalized using variance stabilization normalization (vsn - right). Due to low starting material in early cell stages, protein concentration was not adjusted before mass spec measurement and only accounted for in the normalization step to achieve equal protein amounts.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Metalloproteases comprise an N-terminal signal-peptide for secretion (S), a propeptide or prodomain conferring latency (PRO), and a catalytic zinc-dependent metallopeptidase domain (CD). Additional domains were listed using Interproscan-5.57 codes: (Kringle) Kringle (IPR000001), (CD) Catalytic domain (IPR024079), (PGBD) Peptidoglycan binding-domain (IPR002477), (MAM) MAM-domain (IPR000998), (PRO) Propeptide, (ShKT) ShKT domain (IPR003582), (M12B-GON) M12B-GON-ADAMTS (IPR012314), (WAP) WAP-type 'four-disulfide core' domain (IPR008197), (LDL) Low-density lipoprotein (IPR002172), (EGF) EGF-like (IPR000742), (Ricin) Ricin B-like (IPR035992), (TSR) Thrombospondin type-1 repeat (IPR000884), (mem-prox) ADAM17, membrane-proximal domain (IPR032029), (M12B-PRO) M12B-propeptide (IPR002870), (TM) Transmembrane domain, (Ig) Immunoglobulin-like (IPR013783), (Serine-protease) Serine protease (IPR001254), (PLAC/PLAT/LH2) PLAC / PLAT/LH2 (IPR001304/IPR001024), (vHL) von Hippel-Lindau domain (IPR036208), (CUB) CUB domain (IPR000859), (CLEC) C-lectin like (IPR001304), (Hemopexin) Hemopexin-like repeat (IPR018487), (CRD) ADAMTS/ADAMTS-like, Cysteine-rich domain (IPR045371I), (FA58C) Coagulation factor 5/8(IPR000421), (Fib) Fibrinogen-like (IPR036056), (FN) Fibronectin type II (IPR036943), (Disintegrin) Disintegrin domain (IPR001762), and ADAMTS/ADAMTS-like (IPR010294). All metalloproteases were identified based on manual sequence and domain analysis. The identified proteases were categorized as MASP-like (1), M28-like (1), ADAM-like (4), MMP (6), ADAMTS-like (15), and Astacin (27). The latter can be further divided into three subgroups: Meprin-like (9), BMP/Tolloid-like (2), and other Astacins (16). Based on the identified hierarchical phylogenetic orthogroups, we identified sequences that are specific to cnidarians, as indicated.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** All Nematostella polydoms are expressed from GD.1 neurogland cells supposed to have a digestive function. Polydom-like-2 and Polydom-related show additional expression within the uncharacterized secretory cell type. S2.tll.2&3.

## Discussion

The evolution of the ECM, a complex proteinaceous network that connects cells and organizes their spatial arrangement in tissues, has been a key innovation driving the emergence of multicellular life forms (Brunet and King, 2017; Rokas, 2008). Although ctenophores have recently been identified as the sister group to all other animals (Schultz et al., 2023), the hitherto available genomic evidence suggests that they possess only a minimal repertoire of conserved ECM and ECM-affiliated proteins, limiting comparative studies with bilaterians (Draper et al., 2019). In contrast, cnidarian genome data have offered broad evidence for conserved matrisomes anticipating the complexity of mammalian species (Tucker and Adams, 2014). Here, we identified 551 ECM proteins that comprise the matrisome of the sea anemone Nematostella vectensis through in silico prediction using transcriptome databases and analyzed the dynamics of 287 ECM factors by TMT labeling and LC-MS/MS of decellularized mesoglea samples from different life stages. Utilizing cell-type-specific atlases, we showed that the inner gastroderm is the major source of the Nematostella ECM, including all 12 collagen-encoding genes. This finding supports the model of germ layer evolution proposed by Steinmetz et al., 2017 where, based on both transcription factor profiles and structural gene sets, the cnidarian inner cell layer (endoderm) is homologous to the bilaterian mesoderm that gives rise to connective tissues. It also contrasts the situation in Hydra where both germ layers contribute to the synthesis of core matrisome proteins (Epp et al., 1986; Zhang et al., 2007). The primacy of the gastrodermis in ECM synthesis might be related to the anthozoan-specific mesenteries, which represent extensions of the mesoglea into the body cavity sandwiched by two endodermal layers. Discrete endo- and ectodermal ECM transcript repertoires would result in a restricted composition of the mesoglea in these mesenteric folds. Whether a gastroderm-based matrisome represents an ancestral state of the cnidarian phylum can only be resolved by the inclusion of omics data from a larger diversity of cnidarian species. While anthozoans such as Nematostella have previously been considered a basal group among cnidarians (Bridge et al., 1992; Miller et al., 2000), more recent phylogenomic studies consider them as a sister clade to medusozoans (DeBiasse et al., 2024). To evaluate the complexity of Nematostella’s matrisome across cnidarians and other metazoan phyla, we plotted matrisome sizes from published databases and newly generated in silico matrisomes of representative species against orthogroup counts (Figure 5). For the in silico matrisomes, only orthogroups shared with at least one found in published matrisomes were counted. Interestingly, anthozoan species generally exhibit a higher complexity than medusozoans and populate a transitory region between bilaterians and non-bilaterians in the evolutionary trajectory. This indicates that the acquisition of complex life cycles in medusozoa, that are distinguished by the pelagic medusa stage, was not accompanied by a diversification of the matrisome repertoire. This is in line with findings from genome data in Aurelia, a cnidarian with a medusa stage, that questioned the hypothesis of the medusozoan body plan being derived. Rather, the authors found a redeployment of the existing genetic repertoire (Gold et al., 2019). The reduced complexity of the medusozoan ECM might therefore represent a strategy to minimize the cost for ECM remodeling during metamorphosis and rely on a restricted set of conserved genes to form the expanded jellyfish mesoglea.

![Figure 5.](https://cdn.elifesciences.org/articles/105319/elife-105319-fig5-v1.jpg)

**Figure 5.:** Matrisome sizes of published and newly generated in silico matrisomes of representative cnidarians and other metazoan species were plotted against their respective orthogroup count. Only proteins from orthogroups shared with at least one published matrisome were counted. Anthozoans generally show a higher matrisome complexity than medusozoan species populating a transitory region between bilaterians and non-bilaterians in the evolutionary trajectory.

A significant fraction of Nematostella’s exceptionally rich matrisome is devoted to the formation of the cnidocyst, a unique cellular novelty of the cnidarian clade (Babonis et al., 2023; Jékely et al., 2015). Cnidocyst-specific proteins follow an unusual secretion route into the lumen of the growing cnidocyst vesicle, which topologically represents extracellular space (Ozbek, 2011). It has therefore been speculated that they originated from neurosecretory vesicles used for predation in early metazoans (Balasubramanian et al., 2012). The recent finding that cnidocysts are instrumental for the predatory lifestyle of the Aiptasia larvae (Maegele et al., 2023) supports the hypothesis of a deeply rooted extrusive mechanism for prey capture in metazoan evolution. In this context, it is intriguing that the majority of Nematostella cnidocyte genes shared with other cell types is expressed within neuroglandular subtypes (Figure 3—figure supplement 1). In addition, the cnidocyst-specific matrisome contains diverse proteins with repetitive ECM domains that likely have general bioadhesive or fibrous properties that might play a role in entangling and ingesting prey organisms. These include several fibropellin-like and other EGF repeat proteins (poly-EGF) as well as thrombospondin type-1 repeat (TSR) proteins, such as properdin-likes.

The changes in the matrisome profiles across Nematostella’s major life stages suggest a highly dynamic epithelial rearrangement during primary polyp morphogenesis. The involvement of Wnt/PCP factors in this process indicates similar cell migration and reorientation events as during convergent extension processes in gastrulation. Kumburegama et al. have shown that primary archenteron invagination and apical constriction of bottle cells in Nematostella is dependent on the PCP components strabismus (Kumburegama et al., 2011) and Fzd10 (Wijesena et al., 2022). Mesentery formation in primary polyps, which involves sequential folding events of the endodermal epithelium (Berking, 2007), likely involves similar molecular pathways. As already observed by Appelöf, 1900, mesoglea synthesis follows invagination during this process. The molecular network composed of Wnt/PCP and basal membrane factors that our data revealed might therefore indicate an actomyosin-controlled invagination of the endodermal layer followed by BM production to re-align the cells in their apico-basal architecture. The upregulation of wound response factors in the adult animal might indicate a transient loss of tissue integrity during collective cell migration, which could entail an actin-based purse-string mechanism as during wound healing (Begnaud et al., 2016; Bischoff et al., 2021). Future work will further decipher the gene-regulatory network controlling polyp morphogenesis in this anthozoan model.

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
      <td>Biological sample (Nematostella vectensis)</td>
      <td>Larvae (3 dpf), primary polyps (10 dpf), adults (≥1 year)</td>
      <td>Mark Q. Martindale, Whitney Lab; Putnam et al., 2007</td>
      <td></td>
      <td>Cultured in lab conditions; used for mesoglea isolation, immunostaining, proteomics. Mixed sex animals used in all experiments</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Laminin (rabbit polyclonal)</td>
      <td>This paper</td>
      <td></td>
      <td>Custom polyclonal antibody produced by eurogentec, epitope in Nv Laminin γ1 chain (1:100 for IF, 1:2 for EM)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Collagen IV(guinea pig polyclonal)</td>
      <td>This paper</td>
      <td></td>
      <td>Custom polyclonal antibody produced by eurogentec, epitope in NvCol4b (1:10 for EM)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Collagen II-like (rat polyclonal)</td>
      <td>This paper</td>
      <td></td>
      <td>Custom polyclonal antibody produced by eurogentec, epitope in NvCol2c (1:10 for EM)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Pan-Collagen (rat polyclonal)</td>
      <td>This paper</td>
      <td></td>
      <td>Custom polyclonal antibody produced by eurogentec, consensus fibrillar collagen motif (1:100 for IF, 1:2 for EM)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488 goat anti-rat IgG (H+L) (goat polyclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# A-11006RRID:AB_2534074</td>
      <td>Secondary antibody (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 568 goat anti-rabbit IgG (H+L) (goat polyclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# A-11011RRID:AB_143157</td>
      <td>Secondary antibody (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit IgG (10 nm colloidal gold) (goat polyclonal)</td>
      <td>British Biocell</td>
      <td>Cat# EM.GAR10/1RRID:AB_2715527</td>
      <td>Immunogold EM (1:150)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rat IgG (10 nm colloidal gold) (goat polyclonal)</td>
      <td>British Biocell</td>
      <td>Cat# EM.GAT10/1RRID:AB_2715527</td>
      <td>Immunogold EM (1:150)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Nanogold-IgG Goat anti-Guinea Pig IgG (goat polyclonal)</td>
      <td>Nanoprobes</td>
      <td>Cat# 2054RRID:AB_3711173</td>
      <td>Immunogold EM (1:150)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Nanogold-IgG Goat anti-Rat IgG (H+L) (goat polyclonal)</td>
      <td>Nanoprobes</td>
      <td>Cat# 2007RRID:AB_3711173</td>
      <td>Immunogold EM (1:150)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Chymotrypsin, sequencing grade</td>
      <td>Promega</td>
      <td>Cat# V1061</td>
      <td>Mass spectrometry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cysteine</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# C7352</td>
      <td>Egg dejellying</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAPI</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# D9542</td>
      <td>Nuclear stain</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dithiothreitol</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# D9779</td>
      <td>Mesoglea preparation</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EGTA</td>
      <td>Sigma Aldrich</td>
      <td>Cat# 324626</td>
      <td>Electron microscopy</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Formaldehyde solution min. 37%</td>
      <td>Merck KGaA</td>
      <td>Cat# 252549</td>
      <td>Electron microscopy</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutaraldehyde</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# G5882</td>
      <td>Electron microscopy</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HEPES</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# H3375</td>
      <td>Mesoglea preparation</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HQ-Silver</td>
      <td>Nanoprobes Yaphank</td>
      <td>Cat# 2012</td>
      <td>Electron microscopy</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Magnesium chloride</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# M8266</td>
      <td>Immunocytochemistry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-lauryl-sarcosinate</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# L5125</td>
      <td>Mesoglea decellularization</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>OASIS HLB µElution Plate</td>
      <td>Waters</td>
      <td>Cat# 186001828BA</td>
      <td>Mass spectrometry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Osmium tetroxide</td>
      <td>Sigma Aldrich</td>
      <td>Cat# O5500</td>
      <td>Electron microscopy</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Precast 4–12% gradient gels</td>
      <td>Carl Roth</td>
      <td>Cat# 3673.2</td>
      <td>SDS-PAGE</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TMT10plex Isobaric Label Reagent</td>
      <td>ThermoFisher</td>
      <td>Cat# 90110</td>
      <td>Mass spectrometry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trichloroacetic acid</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# T6399</td>
      <td>Mesoglea preparation</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton X-100</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# T8787</td>
      <td>Immunocytochemistry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tween-20</td>
      <td>Roche</td>
      <td>Cat# 11332465001</td>
      <td>Immunocytochemistry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Uranyl acetate</td>
      <td>Electron Microscopy Sciences</td>
      <td>Cat# 541-09-3</td>
      <td>Electron microscopy</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BLAST</td>
      <td>Altschul et al., 1990</td>
      <td>RRID:SCR_004870</td>
      <td>Database searches</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Custom Python scripts</td>
      <td>This paper</td>
      <td>RRID:SCR_024202</td>
      <td>For domain and orthogroup analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DeepLoc-2</td>
      <td>Thumuluri et al., 2022</td>
      <td>RRID:SCR_026503</td>
      <td>Protein localization prediction</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji (ImageJ)</td>
      <td>Schindelin et al., 2012</td>
      <td>RRID:SCR_003070</td>
      <td>Image processing</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>IsobarQuant</td>
      <td>Franken et al., 2015</td>
      <td>RRID:SCR_016732</td>
      <td>MS data analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>limma (R package)</td>
      <td>Ritchie et al., 2015</td>
      <td>RRID:SCR_010943</td>
      <td>Proteomics analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Mascot</td>
      <td>Matrix Science</td>
      <td>RRID:SCR_014322</td>
      <td>MS data analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NIS elements Imagine software</td>
      <td>Nikon Instruments Inc.</td>
      <td></td>
      <td>Image processing. https://www.microscope.healthcare.nikon.com/products/software/nis-elements</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OrthoFinder v2.5.4</td>
      <td>Emms and Kelly, 2019</td>
      <td>RRID:SCR_017118</td>
      <td>Orthogroup prediction</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat package</td>
      <td>Stuart et al., 2019</td>
      <td>RRID:SCR_016341</td>
      <td>Single cell expression analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SignalP-6.0</td>
      <td>Teufel et al., 2022</td>
      <td>RRID:SCR_015644</td>
      <td>Signal peptide prediction</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SMART</td>
      <td>Schultz et al., 1998</td>
      <td>RRID:SCR_005026</td>
      <td>Protein domain analysis</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Single-cell RNA atlas</td>
      <td>Cole et al., 2024</td>
      <td></td>
      <td>Expression data</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Nikon A1R Confocal Laser Scanning Microscope</td>
      <td>Nikon, Tokyo, Japan</td>
      <td>RRID:SCR_020317</td>
      <td>Confocal microscopy</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Nikon Eclipse 80i microscope</td>
      <td>Nikon, Tokyo, Japan</td>
      <td>RRID:SCR_015572</td>
      <td>Fluorescence microscopy</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Gemini C18 column (3 μm, 110 Å, 100 × 1.0 mm)</td>
      <td>Phenomenex</td>
      <td>Cat# 00D-4439-A0</td>
      <td>Mass spectrometry</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Agilent 1200 Infinity high-performance liquid chromatography system</td>
      <td>Agilent</td>
      <td>RRID:SCR_018018</td>
      <td>Mass spectrometry</td>
    </tr>
  </tbody>
</table>

### Nematostella culture

Animals used in this study were sea anemones of mixed sex and originally obtained from Mark Q. Martindale, The Whitney Laboratory for Marine Bioscience (Putnam et al., 2007). For all experiments, animals were randomly selected. Adult Nematostella were kept in plastic boxes at 18°C in 1/3 artificial sea water (~11 ppt; Nematostella medium) in the dark. They were fed with freshly hatched Artemia nauplii and cleaned once per week. To induce spawning, animals were transferred to 27°C Nematostella medium in light for 8 hr and then washed with 18°C Nematostella medium. The egg patches were collected and dejellied in 5% cysteine solution for 15 min. Unless otherwise stated, the embryos were left to develop in Nematostella medium at room temperature (RT) in normal day/night cycles.

### Immunocytochemistry

Larvae on 3 dpf, primary polyps on 10 dpf, and small adult polyps were collected and left to relax at 27°C in direct light for 30 min. A solution of 7% MgCl2 in seawater was slowly added, and the animals were anesthetized for 20 min. Fixation was performed with Lavdovsky’s fixative (50% ethanol, 36% H2O, 10% formaldehyde, 4% acetic acid) for 30 min at RT after which the samples were incubated in 150 mM Tris, pH 9.0, 0.05% Tween-20, for 10 min. An incubation step at 70°C for 10 min and a subsequent cooling to RT was followed by three 10 min washing steps in PBS, PBS, 0.1% Tween-20, and PBS, 0.1% Triton-X100, respectively. Primary antibody incubation (rabbit anti-Laminin, rat anti-Pan-Collagen) was performed at 1:100 in 0.5% milk powder overnight at 4°C. The samples were washed 3 times for 10 min in PBS, 0.1% Tween-20, and incubated with secondary antibodies (Alexa Fluor 488 goat anti-rat IgG (H+L), Thermo Fisher Scientific; Alexa Fluor 568 goat anti-rabbit IgG (H+L), Thermo Fisher Scientific) at 1:400 for 2.5 hr at RT. Prior to mounting on object slides with Mowiol, DAPI was added at 1:1000 for 30 min. Decellularized mesogleas were transferred onto a microscopy slide lined with liquid blocker. The mesogleas of larvae and primary polyps were carefully stuck to the slide using an eyelash. The staining protocol followed the whole mount immunocytochemistry protocol with 10 min fixation and only one washing step per wash to avoid washing off of the mesogleas. The antibodies were incubated on the slides in a Petri dish with a wet paper towel to prevent evaporation. Images were acquired with an A1R microscope at the Nikon Imaging Facility Heidelberg. Further image processing was performed with Fiji ImageJ v1.53t.

### Mesoglea decellularization

All samples were prepared as biological triplicates. About 500,000 larvae (3 dpf) and primary polyps (10 dpf), and four adult animals were collected. The adult polyps were cut open along the oral-aboral axis using a scalpel to ease the decellularization of the endoderm. All samples were incubated in 0.5% N-lauryl-sarcosinate for 5 min and then frozen in liquid nitrogen. After thawing at RT, the samples were transferred to ddH2O using a 70 µm sieve for larvae and primary polyps. The mesogleas were decellularized in ddH2O by repeated pipetting with a flamed glass pipette and frequent water changes. The progress of decellularization was checked repeatedly by phase contrast microscopy at 60x magnification using a Nikon 80i microscope. As a final quality control, a few sample mesogleas were stained with DAPI for 10 min in PBS to visualize residual cells or nematocysts. Decellularized mesogleas were then picked individually for further analysis. For SDS-PAGE analysis, isolated mesogleas (40 µg) were dissolved in 1 M dithiothreitol (DTT), boiled at 90°C for 2 hr, and loaded on a precast 4–15% gradient gel (Carl Roth) after a quick spin.

### Sample preparation for SP3 and TMT labeling

Isolated mesogleas (larvae and primary polyps, N=150, adults, N=4) were dissolved in 1 M DTT for 30 min at 90°C and protein extraction was performed using trichloroacetic acid (TCA) precipitation. TCA pellets were resuspended in 50 µL 1% SDS, 50 mM HEPES pH 8.5. Reduction of disulfide bridges in cysteine-containing proteins was performed with DTT (56°C, 30 min, 10 mM in 50 mM HEPES, pH 8.5). Reduced cysteines were alkylated with 2-chloroacetamide (RT, in the dark, 30 min, 20 mM in 50 mM HEPES, pH 8.5). Samples were prepared using the SP3 protocol (Hughes et al., 2014; Hughes et al., 2019) and trypsin was added in an enzyme to protein ratio of 1:50 for overnight digestion at 37°C. Then, peptide recovery was performed in HEPES buffer by collecting the supernatant on a magnet and combining it with the second elution wash of beads with HEPES buffer. Peptides were labeled with TMT10plex (Werner et al., 2014) Isobaric Label Reagent according to the manufacturer’s instructions. For further sample clean up, an OASIS HLB µElution Plate was used for each sample separately. A control run was performed to be able to mix equal peptide amounts based on the MS signal in each run, and samples were combined for TMT9plex accordingly. Offline high pH reverse phase fractionation was carried out on an Agilent 1200 Infinity high-performance liquid chromatography system, equipped with a Gemini C18 column (3 μm, 110 Å, 100 × 1.0 mm, Phenomenex; Reichel et al., 2016).

### Mass spectrometry and data analysis

Each biological sample was subjected to analysis in technical triplicates. LC-MS/MS, Liquid Chromatography (LC) was performed as previously described for Hydra mesoglea (Veschgini et al., 2023). IsobarQuant (Franken et al., 2015) and Mascot (v2.2.07) were used to process the acquired data, which was searched against the Nematostella vectensis NV2 (wein_nvec200_tcsv2) protein models (https://simrbase.stowers.org/starletseaanemone) containing common contaminants and reversed sequences. The following modifications were included in the search parameters: Carbamidomethyl (C) and TMT10 (K) (fixed modification), Acetyl (Protein N-term), Oxidation (M) and TMT10 (N-term) (variable modifications). For the full scan (MS1), a mass error tolerance of 10 ppm and for MS/MS (MS2) spectra of 0.02 Da was set. Further parameters were: trypsin as protease with an allowance of a maximum of two missed cleavages, a minimum peptide length of seven amino acids, and at least two unique peptides were required for a protein identification. An inclusion of lysine and proline hydroxylation as variable modifications did not increase the detection of bona fide collagens, prompting us to omit these parameters. The false discovery rate on peptide and protein level was set to 0.01. The raw output files of IsobarQuant (protein.txt – files) were processed using R. Contaminants were filtered out and only proteins that were quantified with at least two unique peptides were considered for the analysis. 5056 proteins passed the quality control filters. Log2-transformed raw TMT reporter ion intensities (‘signal_sum’ columns) were first cleaned for batch effects using limma (Ritchie et al., 2015) and further normalized using variance stabilization normalization (Huber et al., 2002; see Figure 4—figure supplement 1 for an overview of these steps). Proteins were tested for differential expression using the limma package. The replicate information was added as a factor in the design matrix given as an argument to the ‘lmFit’ function of limma. A protein was annotated as a hit with a false discovery rate (fdr) smaller than 5% and a fold-change of at least 2. For the heatmap shown in Figure 4B, the log2-transformed median abundance of all samples for each life stage was calculated.

### In silico matrisome prediction

Domains for the protein models of the SIMRbase Nematostella vectensis NV2 (wein_nvec200_tcsv2) transcriptome (https://simrbase.stowers.org/starletseaanemone) were de novo annotated using InterProScan (Jones et al., 2014). The proteins were then filtered positively using a list of known ECM protein domains and negatively by the presence of the respective exclusive domains according to Naba et al., 2012. Signal peptides were predicted using SignalP-6.0 (Teufel et al., 2022) and DeepLoc-2 (Thumuluri et al., 2022). The latter was also used to predict the cellular localization of proteins. In addition, OrthoFinder vers. 2.5.4 was used with default settings to predict orthogroups from all predicted matrisomes and published matrisomes from M. musculus, H. sapiens (Naba et al., 2012), B. taurus (Listrat et al., 2023), C. japonica (Huss et al., 2019), D. melanogaster (Davis et al., 2019), D. rerio (Nauroy et al., 2018), S. mediterranea (Cote et al., 2019) and C. elegans (Teuscher et al., 2019). Finally, all Nematostella sequences were manually annotated by comparing their domain architecture to published protein groups. Domain and orthogroup analysis were performed using custom python scripts (See data availability statement). For the orthogroup analysis, the phylogenetically hierarchical orthogroups predicted by OrthoFinder were analyzed. To prevent domain redundancy, we restricted the analysis to SMART domains for the domain comparison, as domain comparisons for other domain databases showed similar results. To achieve a better orthogroup definition, we predicted additional in silico matrisomes for a number of available protein model datasets in non-bilaterian species using the same bioinformatic pipeline as for Nematostella: Choanoflagellata: Monosiga brevicollis, Salpingoeca rosetta; Porifera: Amphimedon queenslandica, Ephydatia muelleri; Ctenophora: Mnemiopsis leidyi, Pleurobrachia bachei, Beroe ovata (http://ryanlab.whitney.ufl.edu/bovadb), Pleurobrachia bachei (Moroz et al., 2014); Placozoa: Tricoplax adhaerens, Tricoplax spec; Cnidaria: Aurelia aurita (Gold et al., 2019), Clytia hemispherica (http://marimba.obs-vlfr.fr), Exaiptasia diaphana (Oakley et al., 2016), Hydra vulgaris, Acropora digitifera (Shinzato et al., 2021), Stylophora pistillata, Calvadosia cruxmelitensis (Ohdera et al., 2019), Morbakka virulenta (Khalturin et al., 2019), Thelohanellus kitauei, Acropora digitifera, Porites asteroides (Kenkel et al., 2013), Xenia spec. (Hu et al., 2020), Chordata: Branchiostoma belcheri, Branchiostoma floridae, Branchiostoma lanceolatum (Uniprot Reference Proteomes). To identify orthogroups specific to cnidarians, we filtered the OrthoFinder-derived orthogroups and phylogenetic hierarchies, selecting only those that exhibited cnidarian exclusivity. To identify potential venoms in our matrisome dataset, we performed BLAST searches against the ToxProt database of known animal toxins (Jungo et al., 2012). We categorized as ‘putative venoms’ (Supplementary file 1) candidates that exhibited significant matches in this database (E>1e–03).

### Single-cell RNA expression

The expression matrix corresponding to the predicted ECM genes was extracted from the updated single cell atlas (Cole et al., 2024). To generate expression data, the dataset was first separated into three life-cycle stages: samples from 18 hr gastrula until 4 d planula were classified as ‘larva’, samples from 5 d through 16 d primary polyps were classified as ‘primary polyp’, and all samples derived from juvenile or adult tissues were classified as ‘adult’. The full gene matrix was filtered down to only the 829 models corresponding to the curated list of ECM genes. For plotting expression values, the principal tissue-type annotations were further collapsed to cluster together early and late ectodermal clusters, specification and mature cnidocyte states, and to collapse the primary germ cells and putative stem cells into a single data partition. Differentially expressed genes were calculated across all annotated cell-type states using the Seurat vs.4 function Seurat::FindAllMarkers, requiring a return-threshold of 0.001, and a minimum detection in 20% of any cluster. Module expression scores for different gene sets (core, associated, and other for the full dataset, and ‘ubiquitous’, ‘shared’, ‘specification-specific’ and ‘mature-specific’ for the cnidocyte subset) were calculated using the Seurat function Seurat:: AddModuleScore. The cnidocyte genes were binned as described above according to summarized expression data generated by the Seurat::DotPlot function, in the ‘data’ matrix of the resulting ggplot.

### Electron microscopy

For morphology, Nematostella larvae and primary polyps were processed as previously described for Hydra (Böttger et al., 2012; Garg et al., 2023). Briefly, animals were subjected to cryofixation (high-pressure freezing, freeze-substitution, and epoxy resin embedding: HPF/FS: Figure 1—figure supplement 3A, B, G, H) or to standard chemical fixation (glutaraldehyde, followed by OsO4, resin embedding: CF: Figure 1—figure supplement 3F, L). Ultrathin sections were optionally stained with uranyl acetate and lead for general contrast enhancement or with periodic acid, thiocarbohydrazide, and silver proteinate to highlight periodic acid-Schiff-positive constituents (Figure 1—figure supplement 3H). For Tokuyasu-immunoelectron microscopy (Tokuyasu, 1973) samples were either fixed for >3 days at RT with 4 % w/v formaldehyde solution in PHEM (5 mM HEPES, 60 mM PIPES, 10 mM ethylene glycol tetraacetic acid (EGTA), 2 mM MgCl2), pH 7.0 (TOK: Figure 1—figure supplement 3M, O) or by using a new modification of established HPF/FS-sample rehydration methods (Ripper et al., 2008; Schmiedinger et al., 2013); this modification included freeze substitution with methanol containing 3.2 % w/v formaldehyde, 0.08 % w/v uranyl acetate, and 8.8% H2O, removal of uranyl acetate at 4°C (on ice) and partial sample rehydration and postfixation through incubation in Lavdovsky’s fixative for 1 hr at RT (HPF/FS/RH-Lav: Figure 1—figure supplement 3N, P). Fixed samples were rinsed with PHEM buffer and further processed for thawed cryosection immunogold labeling (Tokuyasu, 1973) as previously described (Garg et al., 2023). Anti-Lam and anti-PanCol label on standard TOK-sections were visualized with goat anti-rabbit or goat anti-rat secondary antibodies coupled to 10 nm colloidal gold. Anti-Col4 and anti-Col2c labeling was performed on HPF/FS/RH-Lav samples by using Nanogold-IgG Goat anti-Guinea Pig IgG or Nanogold-IgG Goat anti-Rat IgG (H+L), respectively, followed by silver enhancement with HQ silver.
