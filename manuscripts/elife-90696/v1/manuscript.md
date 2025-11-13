# Novel sterol binding domains in bacteria

## Authors

- Liting Zhai<sup>1</sup> ([ORCID: 0000-0003-3566-3472](https://orcid.org/0000-0003-3566-3472))
- Amber C Bonds<sup>2</sup>
- Clyde A Smith<sup>3</sup>
- Hannah Oo<sup>1</sup>
- Jonathan Chiu-Chun Chou<sup>1</sup>
- Paula V Welander<sup>2</sup> ([ORCID: 0000-0002-9502-6902](https://orcid.org/0000-0002-9502-6902))
- Laura MK Dassama<sup>1</sup> ([ORCID: 0000-0002-0851-6373](https://orcid.org/0000-0002-0851-6373)) †

### Affiliations

1. Department of Chemistry and Sarafan ChEM-H, Stanford University Stanford United States ([ROR:00f54p054](https://ror.org/00f54p054))
2. Department of Earth System Science, Stanford University Stanford United States ([ROR:00f54p054](https://ror.org/00f54p054))
3. Department of Chemistry and Stanford Synchrotron Radiation Lightsource, Stanford University Stanford United States ([ROR:00f54p054](https://ror.org/00f54p054))
4. Department of Microbiology and Immunology, Stanford University School of Medicine Stanford United States ([ROR:00f54p054](https://ror.org/00f54p054))

† Corresponding author

## Abstract

Sterol lipids are widely present in eukaryotes and play essential roles in signaling and modulating membrane fluidity. Although rare, some bacteria also produce sterols, but their function in bacteria is not known. Moreover, many more species, including pathogens and commensal microbes, acquire or modify sterols from eukaryotic hosts through poorly understood molecular mechanisms. The aerobic methanotroph Methylococcus capsulatus was the first bacterium shown to synthesize sterols, producing a mixture of C-4 methylated sterols that are distinct from those observed in eukaryotes. C-4 methylated sterols are synthesized in the cytosol and localized to the outer membrane, suggesting that a bacterial sterol transport machinery exists. Until now, the identity of such machinery remained a mystery. In this study, we identified three novel proteins that may be the first examples of transporters for bacterial sterol lipids. The proteins, which all belong to well-studied families of bacterial metabolite transporters, are predicted to reside in the inner membrane, periplasm, and outer membrane of M. capsulatus, and may work as a conduit to move modified sterols to the outer membrane. Quantitative analysis of ligand binding revealed their remarkable specificity for 4-methylsterols, and crystallographic structures coupled with docking and molecular dynamics simulations revealed the structural bases for substrate binding by two of the putative transporters. Their striking structural divergence from eukaryotic sterol transporters signals that they form a distinct sterol transport system within the bacterial domain. Finally, bioinformatics revealed the widespread presence of similar transporters in bacterial genomes, including in some pathogens that use host sterol lipids to construct their cell envelopes. The unique folds of these bacterial sterol binding proteins should now guide the discovery of other proteins that handle this essential metabolite.

## Introduction

Sterol lipids are ubiquitous and essential components of eukaryotic life, playing vital roles in intra- and intercellular signaling, stress tolerance, and maintaining cell membrane integrity (Bi and Liao, 2010; Bloch, 1991; Huang et al., 2016; Miao et al., 2002). Although sterol synthesis is often considered to be a strictly eukaryotic feature, several bacteria have been shown to also produce sterols (Bloch, 1991; Ourisson et al., 1987). Bacterial sterols were first discovered in Methylococcus capsulatus more than 40 years ago (Bird et al., 1971) and initially, were only observed in a few isolated aerobic methanotrophs (γ-Proteobacteria) and a few myxobacteria (δ-Proteobacteria) (Bode et al., 2003; Kohl et al., 1983; Patt and Hanson, 1978; Schouten et al., 2000). Subsequent comparative genomics analyses have revealed the potential to produce sterol in a variety of bacterial groups including Planctomycetes, α-Proteobacteria, and Bacteroidetes (Bode et al., 2003; Pearson et al., 2003; Wei et al., 2016). Sterols produced by bacteria, however, tend to differ from eukaryotic sterols in both structure and in their biosynthetic pathways.

Sterol synthesis in both bacteria and eukaryotes requires the cyclization of the linear substrate oxidosqualene by an oxidosqualene cyclase (Osc) to generate either lanosterol or cycloartenol (Abe, 2014). However, fungi, vertebrates, and plants further modify these initial cyclization products to synthesize ergosterol, cholesterol, and stigmasterol, respectively (Desmond and Gribaldo, 2009). These biochemical transformations include demethylations, isomerizations, saturations, and desaturations that are essential for sterols to function properly in eukaryotes (Nes et al., 1993; Xu et al., 2005). Although bacterial production of fully modified sterols such as cholesterol is rare (Lee et al., 2023), some bacteria, including several aerobic methanotrophs and myxobacteria, do modify their sterols. For example, M. capsulatus produces sterols that are demethylated once at the C-4 and C-14 positions and contain a unique desaturation between C-8 and C-14 (Bouvier et al., 1976; Figure 1A). In addition, studies have revealed that bacterial proteins required to modify sterols can differ from the canonical eukaryotic sterol modifying proteins. Examples are the recently identified sterol demethylase proteins, SdmA and SdmB, in M. capsulatus that use O2 to remove one methyl group at the C-4 position; the enzymes are mechanistically distinct from the eukaryotic C-4 demethylase enzymes (Gachotte et al., 1998; Lee et al., 2018; Rahier, 2011).

![Figure 1.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig1-v1.jpg)

**Figure 1.:** (A) Structures of C-4 methylated sterols synthesized by Methylococcus capsulatus. (B) Operon of sterol biosynthesis and transport genes and (top) and schematic description of their localization. OM: outer membrane; CM: cytoplasmic membrane.

Although there is a better grasp of the taxonomic distribution of sterol synthesis in bacteria and of the distinct bacterial proteins involved in their biosynthesis, the function of these lipids in bacteria remains a mystery. It has been posited that bacterial sterols play a role in modulating the fluidic properties of the cytoplasmic membrane, similar to what is observed for cholesterol and ergosterol in eukaryotic cells (Miao et al., 2002; Parks et al., 1995; Summons et al., 2006). However, studies in M. capsulatus have demonstrated that the distribution of sterols differs considerably from what occurs in eukaryotes. Approximately 90% of the free sterol pool in eukaryotic cells is found in the cytoplasmic membrane (Jacquier and Schneiter, 2012) while in M. capsulatus, 75% of sterols are localized to the outer membrane (Jahnke et al., 1992). The outer membrane is the external asymmetric membrane of Gram-negative bacteria and differs from the cytoplasmic membrane in that its outer leaflet is composed of lipopolysaccharides (LPS) in addition to phospholipids (Ruiz et al., 2006). Additionally, sterols that differ by only a single methylation in the core structure can produce significantly different effects in terms of membrane fluidity and stability (Bacia et al., 2005). Given that M. capsulatus primarily produces sterols with one or two C-4 methyl groups, any sterol-membrane interactions in M. capsulatus could differ significantly from what is observed in eukaryotic membranes with cholesterol and ergosterol, which lack methyl groups at the C-4 position.

Interestingly, the 4,4-dimethyl sterols and 4-monomethyl sterols found in M. capsulatus also exist as precursors of pathway end-products in eukaryotes and accumulation of C-4 methylated sterols has been associated with a variety of eukaryotic processes. The accumulation of C-4 methylated intermediates is considered to be the cause of human genetic diseases known as sterolosis (He et al., 2011; König et al., 2000; McLarren et al., 2010) and 4,4-dimethyl sterols such as lanosterol in the brain are implicated in Parkinson’s disease (Lim et al., 2012). In a variety of yeast species, C-4 methylated intermediates can regulate cellular processes associated with hypoxia and other conditions of cellular stress (Hughes et al., 2007; Serratore et al., 2018; Todd et al., 2006). Although the function of 4,4-dimethyl sterols and 4-monomethyl sterols in bacteria is still elusive, a functional role for these specific sterols beyond maintaining membrane fluidity and integrity seems plausible.

To better understand the significance of sterol utilization in the bacterial domain, a fuller understanding of the molecular mechanisms controlling sterol production and localization is needed. Given the observed distribution of sterols in the outer membrane of M. capsulatus, we hypothesized that transporters specific for C-4 methylated sterols must exist that can shuttle these substrates to the outer membrane. Trafficking of sterols to various organelles in eukaryotic cells is not fully understood (Jacquier and Schneiter, 2012) and impaired sterol transport is related to a variety of defects including lysosomal storage diseases (Vance and Peake, 2011). Identifying and characterizing bacterial proteins that transport sterol could reveal novel sterol binding motifs and folds and will provide meaningful insights into protein-sterol interactions and lipid trafficking more broadly.

In this study, we present three putative bacterial sterol transport proteins in M. capsulatus that exhibit remarkable specificity for C-4 methylated sterols. We first used bioinformatics to identify a cytoplasmic membrane protein (BstA), periplasmic protein (BstB), and outer membrane associated protein (BstC). Their ability to recognize and bind sterols was confirmed using protein-lipid pull down assays, where they showed selective binding to C-4 methylated sterols when in the presence of total lipid extracts from M. capsulatus. Quantitative assessment of ligand binding using Microscale Thermophoresis (MST) confirmed their preference for 4-monomethyl sterol, which they bind with equilibrium dissociation constants that are 30–90-fold lower than the 4,4-dimethyl sterol. High-resolution crystallographic structures of BstB and BstC reveal their pronounced divergence from eukaryotic sterol transporters. Docking studies and molecular dynamics simulations with sterol substrates reveal putative substrate binding sites and recognition mechanisms. Collectively, these data provide evidence for a novel system for sterol binding and possibly transport within the bacterial domain and advances our understanding of bacterial sterol lipids.

## Results

### Bioinformatic identification of sterol transport proteins in M. capsulatus

In a previous study, we used the Joint Genome Institute (JGI) Integrated Microbial Genomes (IMG) Phylogenetic Profiler to identify seventeen candidate genes in M. capsulatus that are unique to C-4 demethylating methanotrophs (Lee et al., 2018). Among them, a putative operon that contains five genes was found to localize next to three sterol biosynthesis genes. Two (sdmA/sdmB) have been characterized as demethylases involved in sterol demethylation at the C-4 position. Homologs of the other three hypothetical genes we have named bstA, bstB and bstC (bacterial sterol transporter), are found in all other aerobic methanotroph genomes that contain sdmA/sdmB. In some of these species, these three genes are also seen to be adjacent to other sterol synthesis genes such as the oxidosqualene cyclase (osc) and squalene monooxygenase (smo), implying they may be functionally related to sterol physiology (Figure 1B).

To obtain additional insights into the proteins encoded by these genes, we performed more refined bioinformatic analyses including protein sequence similarity network (SSN) (Atkinson et al., 2009) and structure prediction with Phyre2 (Kelley et al., 2015) and I-TASSER (Yang et al., 2015). BstA is predicted to belong to the Resistance Nodulation Division (RND) superfamily of transporters, which comprises inner membrane proteins that facilitate drug and heavy metal efflux, and protein secretion, amongst others. They are widespread in gram negative bacteria, but homologs are also found in archaea and eukaryotes. Interestingly, the human Newman Pick Type C1, a transporter of sterols, also contains a transmembrane RND domain (Nikaido, 2018). The SSN of this superfamily shows that BstA is grouped into a single cluster containing five nodes (where sequences with >50% identity are merged into a single node). Structural prediction shows that BstA shares a high homology with a membrane-bound hopanoid transporter, HpnN (PDB 5KHS, Burkholderia multivorans), a RND transporter that moves hopanoids from the cytoplasm or cytoplasmic membrane (Doughty et al., 2011). In the SSN, HpnN is clustered separately from BstA, suggesting a possible functional divergence (Figure 2A, Table 1).

![Figure 2.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig2-v1.jpg)

**Figure 2.:** (A–C): Protein sequence similarity networks (SSN) of BstA, BstB and BstC with the cutoff of 35%, 40%, and 40% sequence identity, respectively. Taxonomic distribution of Bst protein families showing their presence in bacterial (green), eukaryotic (purple), and archaeal (orange) genomes. (D) Genome neighborhood network of Bst proteins. Shown in circles and ovals are genes within 10 genes of BstC; colored in orange are those with identified or predicted roles in sterol synthesis and trafficking.

**Table 1.**
 Available structural information in the SSN of different pfam members.


<table>
  <thead>
    <tr>
      <th>Superfamily</th>
      <th>Pfam</th>
      <th>Protein</th>
      <th>PDB</th>
      <th>Organism</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MMPL</td>
      <td>PF03176</td>
      <td>HpnN</td>
      <td>5khs</td>
      <td>Burkholderia multivorans</td>
    </tr>
    <tr>
      <td>MMPL</td>
      <td>PF03176</td>
      <td>MmpL3</td>
      <td>6ajf</td>
      <td>Mycobacterium smegmatis</td>
    </tr>
    <tr>
      <td>MMPL</td>
      <td>PF03176</td>
      <td>MmpL11</td>
      <td>4y0l</td>
      <td>Mycobacterium tuberculosis</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>AioX</td>
      <td>6esk</td>
      <td>Pseudorhizobium banfieldiae</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>PhnD</td>
      <td>5lq5</td>
      <td>Prochlorococcus marinus</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>PtxB</td>
      <td>5lv1</td>
      <td>Prochlorococcus marinus</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>PtxB</td>
      <td>5o2k</td>
      <td>Pseudomonas stutzeri</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>PtxB</td>
      <td>5jvb</td>
      <td>Trichodesmium erythraeum</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>PA3383</td>
      <td>3n5l</td>
      <td>Pseudomonas aeruginosa</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>PhnD</td>
      <td>3qk6</td>
      <td>Escherichia coli</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>XAC2383</td>
      <td>5ub3</td>
      <td>Xanthomonas axonopodis pv. citri</td>
    </tr>
    <tr>
      <td>Phosphonate-bd</td>
      <td>PF12974</td>
      <td>HtxB</td>
      <td>5me4</td>
      <td>Pseudomonas stutzeri</td>
    </tr>
    <tr>
      <td>TatT</td>
      <td>PF16811</td>
      <td>Tp0956</td>
      <td>3u64</td>
      <td>Treponema pallidum (strain Nichols)</td>
    </tr>
  </tbody>
</table>

BstB belongs to a family of periplasmic/substrate binding proteins (SBPs/PBPs) known to traffic bacterial metabolites such as phosphonate. BstB proteins are grouped into a single cluster consisting of 16 sequences, with most of the sequences belonging to the Methylococcaceae family. Notably, the BstB proteins cluster separately even under stringent cutoffs of sequence identity (as low as 20%), hinting at a distinction of function compared with homologs (Figure 2B, Table 1). Structure prediction of BstB shows homology to PhnD (PDB 3QK6), a periplasmic solute-binding protein of the phosphonate uptake system in E. coli (Alicea et al., 2011). All structurally characterized PhnD homologs are distributed into different clusters in the SSN.

Finally, BstC is predicted to be a T-component member of the tripartite ATP-independent periplasmic component superfamily, which comprises periplasmic lipoproteins implicated in the cytoplasmic import of small molecules. The SSN of BstC reveals that the protein and its closest homologs are also grouped into a separate cluster even under a sequence identity cutoff of 20%. The cluster consists of 13 sequences, with most from Methylococcaceae and Deltaproteobacteria families. At the time of analysis, only one protein in the entire superfamily had structural or biochemical information: Tp0956 from Treponema pallidum (PDB 3U64) is found in the second largest cluster of the network (Figure 2C, Table 1). Compared with the SSNs of BstA and BstB, that of BstC shows the family is predominantly bacterial, with only 1 and 5 sequences from eukaryotes and archaea, respectively (Figure 2A–C).

In summary, sequence and predicted structural homology analyses reveal BstA, BstB, and BstC to be highly similar to transporters involved in disparate bacterial transport systems. However, their separation into distinct clusters in the SSNs imply their functions, including potential substrates, are not identical to their homologs. Because the Bst genes always co-localize with sterol synthesis genes (osc, sdmA and sdmB) in methanotrophs that produce sterols, we hypothesize that BstA/BstB/BstC represent a novel transport system for sterols in bacteria (Figure 1B and Figure 2D).

### Sterol interaction with transporters

To determine whether BstA, BstB, and BstC are sterol transporters, we first attempted gene deletion in M. capsulatus (data not shown). The deletion of these genes, along with others that are required for sterol synthesis (e.g. osc) were not successful, hinting that sterol synthesis and proper localization might be essential in this organism. Because these proteins share homology with well-known bacterial transporters, we reasoned that they are transporters and focused on determining their substrate preference by conducting pull-down assays to assess the binding of sterols from M. capsulatus lipid extracts. In these studies, an excess of recombinantly produced pure proteins was incubated with either the total lipid extract (TLE) from M. capsulatus or a specific polar fraction enriched for native hydroxy-lipids/sterols (HS). Using the HisPur Ni-NTA resin, proteins were isolated from the protein-lipid mixtures, and the protein-bound lipids were extracted and identified by GC-MS. In the presence of the TLE and HS fraction, BstAPD (the periplasmic domain of BstA; details in method), BstB, and BstC bound to 4-monomethyl and 4,4-dimethyl sterols (Figure 3A, Figure 3—figure supplement 1, Table 2). In contrast, neither the 4-monomethyl sterol, the 4,4-dimethyl sterol, nor any other lipids were present when the proteins were incubated with the DMSO negative control, suggesting that the recombinantly produced proteins did not co-purify with any lipids from the expression host. These results indicate that BstAPD, BstB, and BstC preferentially bind C-4 methylated sterols in a mixture of native M. capsulatus sterols, hopanoids, and fatty acids.

![Figure 3.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig3-v1.jpg)

**Figure 3.:** (A) GC chromatograms of sterols bound to purified (40 µM) M. capsulatus BstAPD, BstB, and BstC during protein-lipid pull-down assays. The proteins preferentially bind 4-monomethyl (I) and 4,4-dimethyl (II) sterols when incubated with the total lipid extract (TLE) and hydroxy lipid (HS) fraction from M. capsulatus. (B) MST analysis of the proteins (50 nM) binding to C-4 methylated sterols (3.8 nM –1125 mM). Equilibrium dissociation constants (Kd) and Hill coefficients (nH) are reported on the plots.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) SDS-PAGE gel of pure BstAPD, BstB, and BstC. All proteins are estimated to be more than 90% pure. (B) GC chromatograms of protein-lipid pull down control experiments (DMSO-treated samples) reveal that the proteins do not contain C4-methylsterols when M. capsulatus lipids (TLE or HS fraction) are not present. (C) SDS PAGE gels demonstrating that the samples analyzed in the protein-lipid pull down assays did contain BstAPD, BstB, and BstC.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The data were acquired using the same conditions as reported for Figure 2. Each measurement was performed 3 times, but the average value reported as points and the standard deviation shown as error bars.

**Table 2.**
 Protein sequences and primers.


<table>
  <thead>
    <tr>
      <th>NAME</th>
      <th>SEQUENCE</th>
      <th>PRIMERS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BstA</td>
      <td>MNIPHLAALAAERFARRPWRVLALAMALSALSLWAVSRLPVHTSRQALLPHDNAVAQRFDAFLDKFGAASDLIVVLEGAPPDELKPFADELATALAAEPEIAQATARLDLRFVLEHAYLAVTPERLGTLAGVLEKFGAGAIPEDSSQVDATLGRLLQWLEGAPAMPAAGIDLPTVEVGLKLLGASLDEWHRWLSAGEVPAALDWTRLLAGLGGSEIANDGYFVSRDGRMYFLFVHPASASEDFTAIGPFVEKVRTVAADRAARARAAGRTAPKVGLTGLPAIEYEEHVSIRHDIALVVGSAAGLIVLLILVVVRSWRWALVIFVPMGLGVLWSLGLALVTIGHLTLITASFIAVLFGLGADYGIFTSARIAEERRRGKPLTEAIGAGMGASFQAVFTAGGASVVIFGALATVDFPGFSELGLVAAKGVMLILVSTWLVQPALYALLPPKLAPLPAAASAGAIEPGRMPFRGSVAVILVAGALATAAFGIGSGYELPFDYDVLSLLPKDSESAYYQNRMVAESDYQAEVVIFTAPDLEEARRIAAEAGRLGSVAKVQSLMDLFPPDADARALEARRIGELADDGYAVRLARLAAIGLPEGTFGRVRTILEKGGDFIDQSQELAFSAGHSGLVAALEDVRGRLDAVRSAIEADPVQARERSERFFRMLLSAAERGVALLAEWRQARPITPAQLPPALRDRFFAADGTVAVYAFPAKTVYDPANLDRLMQEIYGVSPDATGFPATHQVFSKSVVESFTHGTREAVTVCLLWLALVLRNWRGFVLASMPLLIGGGWMLGLMALCGIRYNYANIIALPLVIALAVDYGVWFSQRWFDLKDRSLTQINRVAGGVIGLAAGTELAGLGAITLANYRGVSSLGVNITVGLLCCLAATLWVAPAIGQLLDSRKKP</td>
      <td>pET20b-Forward: GAAGGAGATATACATATGAACATCCCCCATTTGGCCGCTCpET20b-Reverse: GTGGTGGTGGTGCTCGAGTGGTTTCTTTCTTGAATCGAGAAGCpET28a-Forward: AGAATCTTTATTTTCAGGGCCATAACATTCCGCACCTGGCGGCpET28a-Reverse: CTCAGTGGTGGTGGTGGTGGTGCTCGAGCTTAGGTTTCTTACGGCTGTCCAG</td>
    </tr>
    <tr>
      <td>BstAPD</td>
      <td>MAVAQRFDAFLDKFGAASDLIVVLEGAPPDELKPFADELATALAAEPEIAQATARLDLRFVLEHAYLAVTPERLGTLAGVLEKFGAGAIPEDSSQVDATLGRLLQWLEGAPAMPAAGIDLPTVEVGLKLLGASLDEWHRWLSAGEVPAALDWTRLLAGLGGSEIANDGYFVSRDGRMYFLFVHPASASEDFTAIGPFVEKVRTVAADRAARARAAGRTAPKVGLTGSGSGSGSESAYYQNRMVAESDYQAEVVIFTAPDLEEARRIAAEAGRLGSVAKVQSLMDLFPPDADARALEARRIGELADDGYAVRLARLAAIGLPEGTFGRVRTILEKGGDFIDQSQELAFSAGHSGLVAALEDVRGRLDAVRSAIEADPVQARERSERFFRMLLSAAERGVALLAEWRQARPITPAQLPPALRDRFFAADGTVAVYAFPAKTVYDPANLDRLMQEIYGV</td>
      <td>pET28a-Forward1: CTTTATTTTCAGGGCCATATGGCGGTGGCGCAACGTTTCGACpET28a-Reverse1: AGTACGCGCTCTCGCTACCGCTACCGCTGCCGCTACCGGTCAGACCAACTTTCGGCpET28a-Forward2: GTTGGTCTGACCGGTAGCGGCAGCGGTAGCGGTAGCGAGAGCGCGTACTATCAGAACpET28a-Reverse2: CTCAGTGGTGGTGGTGGTGGTGCTCGAGTCACACACCATAAATTTCCTG</td>
    </tr>
    <tr>
      <td>BstB</td>
      <td>MTDKITCFSLLAALLAPFVPAQAGAPAPVVVCYPGGAVNERDADQAMDAMLRVVERVGQWPEKSFSSVFTAKVADCGKLMAEMKPAFAITSLALYLDMRGQYDLVPVVQPRIDGRTSERYRVVAKQGRFHDMDELKGRTLGGTMLDEPAFLGKIVFAGKYDPEKDFALQPSRQAIRALRSLDKGELDAVVLNEQQFAGLSALQLASPVETVFTSAEIPLMGVVANARLTSAQERARFAQALETLCADPEGRKLCDLFGIQSFVAVDPTVFDPMARLWLARN</td>
      <td>pET20b-Forward: GAAGGAGATATACATATGGGCGCCCCCGCACCGpET20b-Reverse: GTGGTGGTGGTGCTCGAGGTTCCGCGCCAGCCApET28a-Forward: CGAGAATCTTTATTTTCAGGGCCATGGCGCCCCCGCACCGGTGGTCpET28a-Reverse: CTCAGTGGTGGTGGTGGTGGTGCTCGAGTTAGTTCCGCGCCAGCCAGAG</td>
    </tr>
    <tr>
      <td>BstC</td>
      <td>MRLFAAGILAGVLAGCGGLHRDGTPAGPSAGCPRLTAAALSAGQDALGPSSETQELECALDFLRGSDDPALRRSSLGSRICLHLAERNSDPAERARFAREGVERAEAALAQGGEDDGAVHYYLAANLGLAVRDDMTAALANLHRLEHESEAAVKLSPDFDDGGPLRLLGMLYLKAPAWPAGMGDGDKALDLLGQAVERHPGHPLNHLFYAEALWEVNGESESRRVEEEMAAGWRLLESGSWGYNKQIWKREFADLRQEIGAPAR</td>
      <td>pET20b-Forward: GAAGGAGATATACATATGTGCGGCGGTCTTCACpET20b-Reverse: GTGGTGGTGGTGCTCGAGCCTAGCGGGCGCCCCpET28a-Forward: ATCTTTATTTTCAGGGCCATTGCGGCGGTCTTCACCGCGATGpET28a-Reverse: CTCAGTGGTGGTGGTGGTGGTGCTCGAGTTACCTAGCGGGCGCCCCGAT</td>
    </tr>
  </tbody>
</table>

_The signal peptides in BstB and BstC are shown in bold._

### Quantitative analyses of protein-sterol interactions

The data from the pull-down assays demonstrated that C-4 methylated sterols have affinity for these putative sterol transporters. We next used microscale thermophoresis (MST) to determine the equilibrium binding affinities for these substrates. Binding curves were generated upon titration of the labeled proteins with serially diluted sterol substrates, and the equilibrium dissociation constants were calculated by fitting the curves with different kinetic models (Figure 3B, methods). The ‘Kd’ model applies to binding events with a single binding site or multiple independent binding sites, while the Hill model is invoked in instances where multiple binding sites that exhibit cooperativity are present, with Hill coefficients (nH) greater than 1 signaling positive cooperativity. The average equilibrium dissociation (Kd) constant for BstAPD binding to 4-monomethyl sterol was determined to be 4.41±0.14 μM (nH = 4.0) and ≥203 ± 155 μM for the interaction with 4,4-dimethyl sterol. For BstB, the Kd value of 2.43±0.13 μM (nH of 2.4) was determined for 4-monomethyl sterol; and ≥232 ± 84.3 μM for 4,4-dimethyl sterol. With BstC, the determined values were 2.50±0.39 μM and ≥80.9 ± 14.2 μM for 4-monomethyl sterol and 4,4-dimethyl sterol, respectively. All Kd values for the 4,4-dimethyl sterol could not be accurately determined due to large errors caused by non-saturation even at the highest substrate concentration. In all three proteins, we measured clear binding to C-4 methylated sterols, with marked preference for the 4-monomethyl substrate. Additionally, BstAPD and BstB exhibit cooperativity for binding to 4-monomethyl substrate, indicating that multiple binding sites are plausible.

To further define the specificity of Bst proteins for sterols, we again used MST to detect their interactions with cholesterol and lanosterol, a lipid and precursor that differ in their methylation at the C-4 and C-14 positions, as well as their unsaturation patterns in the core ring structure. The MST results revealed no interaction between BstAPD and BstB with either cholesterol or lanosterol. However, BstC did bind to cholesterol with a Kd value of 3.6±0.64 μM and to lanosterol with a value of 17.3±3.92 μM (Figure 3—figure supplement 2). These data hint that BstC is more tolerant to non-native substates.

### Crystallographic structure of BstB

To understand the molecular details that govern sterol recognition and binding, we crystallized BstB and obtained crystals of the apo form (Table 3). The 1.6 Å-resolution structure of was determined by experimental phasing, producing electron density that allowed the unambiguous building of a model of BstB (except for one disordered loop spanning residues 202–204). The structure comprises two globular α/β domains (Figure 4A, domains A and B) that form a cleft at the middle. Domain A contains six β-strands while domain B contains five. All the β-strands are flanked by αhelices. The domains are connected by two loops: one 9-residue loop that runs from β4 in domain A to β5 in domain B, and a second 8-residue loop that connects β9 in domain B and β10 in domain A. These two long loops could work as a hinge to allow a bending motion of two domains to induce a conformational change upon substrate binding; this is often observed with SBPs/PBPs (de Boer et al., 2019). In addition, an α-helix formed by the C-terminal residues lies behind the cleft and may also allow flexibility of the two domains. Several extend loops are found on the domain-domain interface. The loops (residues 34–38 and residues 171–177) exhibit poor electron densities, suggesting conformational sampling of more than one state (Figure 4—figure supplement 1A).

![Figure 4.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig4-v1.jpg)

**Figure 4.:** (A) Cartoon representation of BstB with the α-helixes and β-strands colored in red and magenta, respectively. (B) Hydrophobicity representations of BstB show a cleft in the middle and a cavity in domain A. The cavity is dominatingly hydrophobic and open only to one side. (C) Comparison of the cleft between the two domains of BstB, apo-PhnD (3S4U), and liganded PhnD (3P7I). BstB displays a similar but narrower opening (~10 Å) compared to non-ligand PhnD (~22 Å). (D) Docking model of the structures of BstB with 4-monomethyl sterol. Left, the docking model is shown in surface representation with 80% transparency. Sterol is shown in sphere and colored in green with the hydroxyl group is colored in red; Right, docking complex of MonoA. The surrounding residues are shown in stick and ball. Hydrogen bonds between the hydroxyl group of the sterol and Tyr120 is shown in the red dashed line.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Loops (residues 34–38 and 171–177) are shown in red boxes. The poor density of these loops could be due to protein flexibility. (B) The modeled chloride forms polar interactions with the surrounding Glu118, Tyr120, and Phe150. (C) Unmodeled density found in the cavity where the aliphatic tail of the sterol is positioned in the docking model.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** The pocket (circled) has an area of 172 Å2 and a volume of 117 Å3 and may function as a second substrate binding site. The surface in red box is the potential interface after substrate binding.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A–C) Energetically favored poses of 4-monomethylsterol. (D–F) Energetically favored poses of 4,4-dimethylsterol. Sterols are shown in ball and stick with the hydroxyl group is colored in red; the surrounding residues are shown in sticks and colored in tan. Hydrogen bonds between the hydroxyl group of the sterol and surrounding residues are shown as red dashed lines.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig4-figsupp4-v1.jpg)

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** (A) RMSD vs time plot for the MD simulation on the apo-BstB and docking complex with 4-monomethyl sterol. The trajectory of apo-BstB is in black while that of the docking complex is depicted in green. (B) Superposition of the apo-BstB structure with the monomethyl sterol-docked complex.

**Table 3.**
 Data collection and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>apo-BstB(SeMet)</th>
      <th>apo-BstC(SeMet)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Resolution range</td>
      <td>38.4–1.6 (1.657–1.6)</td>
      <td>28.63–1.91 (1.978–1.91)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P 21 21 21</td>
      <td>P 1 21 1</td>
    </tr>
    <tr>
      <td>Unit cell (a, b, c; a, b, g)</td>
      <td>39.882, 40.355, 142.263; 90, 90, 90</td>
      <td>55.083, 57.257, 85.825; 90, 97.26, 90</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>606476 (60185)</td>
      <td>200826 (19731)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>31071 (3061)</td>
      <td>41329 (4084)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>19.5 (19.7)</td>
      <td>4.9 (4.8)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>97.81 (93.74)</td>
      <td>99.91 (99.98)</td>
    </tr>
    <tr>
      <td>Mean I/sigma(I)</td>
      <td>30.96 (2.07)</td>
      <td>11.09 (2.78)</td>
    </tr>
    <tr>
      <td>Wilson B-factor</td>
      <td>22.86</td>
      <td>15.59</td>
    </tr>
    <tr>
      <td>R-merge</td>
      <td>0.07677 (1.462)</td>
      <td>0.1267 (0.6131)</td>
    </tr>
    <tr>
      <td>R-meas</td>
      <td>0.07881 (1.501)</td>
      <td>0.1423 (0.6891)</td>
    </tr>
    <tr>
      <td>R-pim</td>
      <td>0.01755 (0.3345)</td>
      <td>0.06419 (0.3117)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>1 (0.745)</td>
      <td>0.994 (0.762)</td>
    </tr>
    <tr>
      <td>CC*</td>
      <td>1 (0.924)</td>
      <td>0.999 (0.93)</td>
    </tr>
    <tr>
      <td>Reflections used in refinement</td>
      <td>30,554 (2873)</td>
      <td>41,317 (4084)</td>
    </tr>
    <tr>
      <td>Reflections used for R-free</td>
      <td>1964 (184)</td>
      <td>1996 (198)</td>
    </tr>
    <tr>
      <td>R-work</td>
      <td>0.2038 (0.2892)</td>
      <td>0.174 (0.2389)</td>
    </tr>
    <tr>
      <td>R-free</td>
      <td>0.2234 (0.2749)</td>
      <td>0.207 (0.2675)</td>
    </tr>
    <tr>
      <td>CC(work)</td>
      <td>0.955 (0.786)</td>
      <td>0.948 (0.879)</td>
    </tr>
    <tr>
      <td>CC(free)</td>
      <td>0.948 (0.725)</td>
      <td>0.939 (0.834)</td>
    </tr>
    <tr>
      <td>Number of non-hydrogen atoms</td>
      <td>2117</td>
      <td>4036</td>
    </tr>
    <tr>
      <td>macromolecules</td>
      <td>1974</td>
      <td>3546</td>
    </tr>
    <tr>
      <td>solvent</td>
      <td>142</td>
      <td>355</td>
    </tr>
    <tr>
      <td>Protein residues</td>
      <td>257</td>
      <td>464</td>
    </tr>
    <tr>
      <td>RMS(bonds)</td>
      <td>0.010</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>RMS(angles)</td>
      <td>1.03</td>
      <td>1.28</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>99.21</td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>Ramachandran allowed (%)</td>
      <td>0.79</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.97</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>2.28</td>
      <td>1.39</td>
    </tr>
    <tr>
      <td>Average B-factor</td>
      <td>33.82</td>
      <td>19.33</td>
    </tr>
    <tr>
      <td>macromolecules</td>
      <td>33.84</td>
      <td>18.22</td>
    </tr>
    <tr>
      <td>ligands</td>
      <td>30.00</td>
      <td>27.28</td>
    </tr>
    <tr>
      <td>solvent</td>
      <td>33.49</td>
      <td>27.44</td>
    </tr>
    <tr>
      <td>Number of TLS groups</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

_Statistics for the highest-resolution shell are shown in parentheses._

The cleft between domains A and B forms a bulky cavity with an area of ~1179.5 Å2 and a volume of ~1009.6 Å3 that extends into domain A and is only accessible to solvent from one side of the structure. The cavity is predominantly hydrophobic, suggesting large and hydrophobic substrates like sterols are favorable for binding (Figure 4B, Table 4). Additionally, a second pocket (area of ~172 Å2; volume of ~117 Å3) is found in domain B and close to the central cleft. This pocket is localized behind the unmodeled loop (residues 202–204), with the extremely poor density in this part implying high flexibility. This pocket is highly hydrophobic, but its role (if any) in ligand binding is unexplored (Figure 4B; Figure 4—figure supplement 2). Other separate hydrophobic areas are also observed on the protein surface and a new hydrophobic interface could be formed by two hydrophobic areas across the cleft upon conformational change induced by substrate binding (Figure 4—figure supplement 2). These areas may be helpful for mediating the protein-protein interactions with BstA or BstC to facilitate the substrate transfer.

**Table 4.**
 Residues involved in forming the cavity of BstB.


<table>
  <thead>
    <tr>
      <th>Domain</th>
      <th>SeqID</th>
      <th>AA</th>
      <th>Domain</th>
      <th>SeqID</th>
      <th>AA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>29</td>
      <td>Val</td>
      <td>A</td>
      <td>115</td>
      <td>Arg</td>
    </tr>
    <tr>
      <td>A</td>
      <td>31</td>
      <td>Val</td>
      <td>A</td>
      <td>117</td>
      <td>Ser</td>
    </tr>
    <tr>
      <td>A</td>
      <td>33</td>
      <td>Tyr</td>
      <td>A</td>
      <td>118</td>
      <td>Glu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>34</td>
      <td>Pro</td>
      <td>B</td>
      <td>120</td>
      <td>Tyr</td>
    </tr>
    <tr>
      <td>A</td>
      <td>35</td>
      <td>Gly</td>
      <td>B</td>
      <td>143</td>
      <td>Thr</td>
    </tr>
    <tr>
      <td>A</td>
      <td>36</td>
      <td>Gly</td>
      <td>B</td>
      <td>144</td>
      <td>Met</td>
    </tr>
    <tr>
      <td>A</td>
      <td>37</td>
      <td>Ala</td>
      <td>B</td>
      <td>146</td>
      <td>Asp</td>
    </tr>
    <tr>
      <td>A</td>
      <td>38</td>
      <td>Val</td>
      <td>B</td>
      <td>147</td>
      <td>Glu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>39</td>
      <td>Asn</td>
      <td>B</td>
      <td>150</td>
      <td>Phe</td>
    </tr>
    <tr>
      <td>A</td>
      <td>40</td>
      <td>Glu</td>
      <td>B</td>
      <td>171</td>
      <td>Ser</td>
    </tr>
    <tr>
      <td>A</td>
      <td>43</td>
      <td>Ala</td>
      <td>B</td>
      <td>172</td>
      <td>Arg</td>
    </tr>
    <tr>
      <td>A</td>
      <td>44</td>
      <td>Asp</td>
      <td>B</td>
      <td>173</td>
      <td>Gln</td>
    </tr>
    <tr>
      <td>A</td>
      <td>46</td>
      <td>Ala</td>
      <td>B</td>
      <td>174</td>
      <td>Ala</td>
    </tr>
    <tr>
      <td>A</td>
      <td>47</td>
      <td>Met</td>
      <td>B</td>
      <td>175</td>
      <td>Ile</td>
    </tr>
    <tr>
      <td>A</td>
      <td>48</td>
      <td>Asp</td>
      <td>B</td>
      <td>192</td>
      <td>Asn</td>
    </tr>
    <tr>
      <td>A</td>
      <td>49</td>
      <td>Ala</td>
      <td>B</td>
      <td>193</td>
      <td>Glu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>50</td>
      <td>Met</td>
      <td>B</td>
      <td>194</td>
      <td>Gln</td>
    </tr>
    <tr>
      <td>A</td>
      <td>51</td>
      <td>Leu</td>
      <td>B</td>
      <td>195</td>
      <td>Gln</td>
    </tr>
    <tr>
      <td>A</td>
      <td>53</td>
      <td>Val</td>
      <td>B</td>
      <td>217</td>
      <td>Ile</td>
    </tr>
    <tr>
      <td>A</td>
      <td>54</td>
      <td>Val</td>
      <td>A</td>
      <td>218</td>
      <td>Pro</td>
    </tr>
    <tr>
      <td>A</td>
      <td>67</td>
      <td>Ser</td>
      <td>A</td>
      <td>219</td>
      <td>Leu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>69</td>
      <td>Phe</td>
      <td>A</td>
      <td>221</td>
      <td>Gly</td>
    </tr>
    <tr>
      <td>A</td>
      <td>71</td>
      <td>Ala</td>
      <td>A</td>
      <td>222</td>
      <td>Val</td>
    </tr>
    <tr>
      <td>A</td>
      <td>73</td>
      <td>Val</td>
      <td>A</td>
      <td>223</td>
      <td>Val</td>
    </tr>
    <tr>
      <td>A</td>
      <td>89</td>
      <td>Ile</td>
      <td>A</td>
      <td>237</td>
      <td>phe</td>
    </tr>
    <tr>
      <td>A</td>
      <td>90</td>
      <td>Thr</td>
      <td>A</td>
      <td>241</td>
      <td>Leu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>91</td>
      <td>Ser</td>
      <td>A</td>
      <td>244</td>
      <td>Leu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>92</td>
      <td>Leu</td>
      <td>A</td>
      <td>253</td>
      <td>Leu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>93</td>
      <td>Ala</td>
      <td>A</td>
      <td>254</td>
      <td>Cys</td>
    </tr>
    <tr>
      <td>A</td>
      <td>94</td>
      <td>Leu</td>
      <td>A</td>
      <td>256</td>
      <td>Leu</td>
    </tr>
    <tr>
      <td>A</td>
      <td>95</td>
      <td>Tyr</td>
      <td>A</td>
      <td>257</td>
      <td>Phe</td>
    </tr>
    <tr>
      <td>A</td>
      <td>106</td>
      <td>Pro</td>
      <td>A</td>
      <td>258</td>
      <td>Gly</td>
    </tr>
    <tr>
      <td>A</td>
      <td>108</td>
      <td>Val</td>
      <td>A</td>
      <td>259</td>
      <td>Ile</td>
    </tr>
    <tr>
      <td>A</td>
      <td>109</td>
      <td>Gln</td>
      <td>A</td>
      <td>262</td>
      <td>Phe</td>
    </tr>
    <tr>
      <td>A</td>
      <td>110</td>
      <td>Pro</td>
      <td>A</td>
      <td>270</td>
      <td>Phe</td>
    </tr>
    <tr>
      <td>A</td>
      <td>112</td>
      <td>Ile</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

A DALI structural homology search (Holm and Rosenström, 2010) suggests the structure of BstB closely resembles that of PBPs that share a bi-lobe architecture and undergo conformational change upon substrate binding to the central cavity (Quiocho and Ledvina, 1996). A comparison of the BstB structure with the phosphonate-binding protein PhnD from E. coli with and without its substrate (2-aminoethyl phosphonate, 2AEP, PDB 3P7I and 3S4U) was performed (Alicea et al., 2011). The comparison revealed that BstB adopts an intermediate conformation between the unliganded PhnD (3S4U) and liganded one (3P7I, Figure 4C). The cleft in BstB is less open (~10 Å) than that in apo-PhnD (~22 Å). There are several possible explanations for this: (1) compared with apo-PhnD structure, the cleft of BstB is deeper and more hydrophobic. Given that BstB binds to sterols (which have a nearly planar architecture and are more hydrophobic than phosphonates), the different architecture of the cleft in BstB may be related to its functional role; (2) it is known that binding of non-substrate ligands can at times trigger a conformational change in PBPs (de Boer et al., 2019). Although no obvious ligand density is observed in the BstB structure, weak unmodeled densities were observed inside the central cavity. Most of these are small patches that cannot be satisfactorily modeled with water and do not closely correspond to any reagent used for crystallization. One of these patches in the central cleft could be modeled with a chloride ion engaging in polar interactions with the surrounding Glu118, Tyr120, and Phe150. Additionally, more unmodeled positive density is observed in further into the cavity in domain A (Figure 4—figure supplement 1B–C). It is plausible that the binding of ligands co-purified with the protein triggered a conformational change leading to a ‘partially-open’ state. A third possibility is that BstB is structurally distinct from the PhnD homologs in that its cleft is much smaller.

### Substrate docking and molecular dynamics simulation of BstB

To obtain greater insights into the mechanism of substrate recognition and binding in the absence of a substrate-bound structure, we used ICM-Pro (Abagyan et al., 1994b; Abagyan and Totrov, 1994a) to generate docking models of C-4 methylated sterol binding to BstB. A three-dimensional model of 4α-monomethyl sterol was constructed from the structure of cholesterol using the Molecular Editor in ICM-Pro and then docked to the BstB structure. In the first iteration, the protein was held rigid, and the ligand allowed to dock flexibly. In this docking model, the sterol was positioned in the hydrophobic cavity in domain A with the polar head pointing toward the central cleft and domain B, adjacent to three residues: Glu118, Tyr120, and Asn192. In subsequent replicate docking iterations, the side chains of these three residues were allowed to be flexible along with the ligand. There are three energetically favored poses: two (MonoA and MonoB) form a single hydrogen bond to Tyr120, while pose MonoC where the hydroxyl makes two hydrogen bonds to Tyr120 and Asn192 (Figure 4D and Figure 4—figure supplement 3A–C, Table 5).

**Table 5.**
 Docking and molecular dynamics results for BstB.


<table>
  <thead>
    <tr>
      <th rowspan="2" colspan="2"></th>
      <th colspan="4">ICM docking results</th>
      <th colspan="3">Hydrogen bonds in docked poses</th>
      <th colspan="3">Hydrogen bonds after MD</th>
    </tr>
    <tr>
      <th colspan="4">energies (kcal/mol)*</th>
      <th colspan="3">distance (Å)</th>
      <th colspan="3">bond persistence (%)</th>
    </tr>
    <tr>
      <th>Ligand</th>
      <th>Pose</th>
      <th>Score†</th>
      <th>Hbond</th>
      <th>Hphob</th>
      <th>VwInt</th>
      <th>Glu118</th>
      <th>Tyr120</th>
      <th>Asn192</th>
      <th>Glu118</th>
      <th>Tyr120</th>
      <th>Asn192</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Mono</td>
      <td>A</td>
      <td>–17.7</td>
      <td>–0.94</td>
      <td>–9.62</td>
      <td>–25.60</td>
      <td>-</td>
      <td>3.18</td>
      <td>-</td>
      <td>95</td>
      <td>3</td>
      <td>-</td>
    </tr>
    <tr>
      <td>B</td>
      <td>–20.4</td>
      <td>–0.69</td>
      <td>–9.50</td>
      <td>–26.10</td>
      <td>-</td>
      <td>3.49 ‡</td>
      <td>-</td>
      <td>95</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>C</td>
      <td>–16.9</td>
      <td>–2.77</td>
      <td>–9.32</td>
      <td>–23.73</td>
      <td>-</td>
      <td>2.83</td>
      <td>3.17</td>
      <td>85</td>
      <td>-</td>
      <td>11</td>
    </tr>
    <tr>
      <td rowspan="3">Di</td>
      <td>A</td>
      <td>–20.3</td>
      <td>–4.53</td>
      <td>–9.48</td>
      <td>–23.22</td>
      <td>2.94</td>
      <td>2.74</td>
      <td>2.89</td>
      <td>12</td>
      <td>12</td>
      <td>57</td>
    </tr>
    <tr>
      <td>B</td>
      <td>–27.8</td>
      <td>–4.64</td>
      <td>–9.74</td>
      <td>–28.74</td>
      <td>2.84</td>
      <td>2.83</td>
      <td>-</td>
      <td>94</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <td>C</td>
      <td>–17.2</td>
      <td>–1.99</td>
      <td>–9.94</td>
      <td>–24.13</td>
      <td>-</td>
      <td>3.18</td>
      <td>-</td>
      <td>-</td>
      <td>- §</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

_*Energies for hydrogen bonding (Hbond), hydrophobic interactions (Hphob) and van der Waals interactions (VwInt).†The score has no units. More negative numbers are indicative of stronger binding.‡This distance could be considered too long to be a hydrogen bond.§This pose loses the hydrogen bond with Tyr120 but gains a hydrogen bond with the carbonyl oxygen of Pro34 which then persists for 95% of the MD simulation._

To probe the dynamics of the BstB structure during substrate binding, we performed multiple 20 ns molecular dynamics (MD) simulations using Desmond (Schrodinger) on each docked poses for monomethyl sterol from ICM-Pro. In all cases, analysis of the resultant MD trajectories indicated that the simulations became stable after the first few picoseconds. In the three poses where there was initially an interaction with Tyr120, that interaction is lost and replaced with a new hydrogen bond with Glu118, which persists for 85–95% of the simulation. Pose MonoC also has an intermittent interaction with Asn192 for approximately 11% of the simulation. In all simulations, whether there is a hydrogen bonding interaction with the ligand or not, the amide group of Asn192 is flipped.

To better probe the protein’s substrate preference, docking models and MD simulations with the 4,4-dimethy sterol were also generated. In these models, the 4,4-dimethyl sterol also docks to the cavity in domain A with three poses of roughly equal energies (Figure 4—figure supplement 3D–F, Table 5). In one (pose DiA), hydrogen bonds to Glu118, Tyr120 and Asn192 are possible; in a second (DiB), hydrogen bonds to Glu118 and Tyr120 are possible; the third (DiC) has a hydrogen bond to Tyr120 only. The 4,4-dimethyl sterol showed interesting behavior during the 20 ns simulations. Pose DiA, which had three hydrogen bonds after ICM-Pro docking, retained all three interactions (although those with Glu118 and Tyr120 are intermittent and persist for only 12% of the simulation). Pose DiB retained both interactions from the docking model, although the hydrogen bond to Tyr120 was only present for 10% of the simulation. The third pose, DiC, showed the largest structural changes, losing the one interaction it had with Tyr120. In this pose, the head group of the sterol moved out of the binding pocket delineated by Glu118, Tyr120 and Asn192 and a new hydrogen bond with the carbonyl oxygen of Pro34 formed, persisting for the duration of the simulation (Table 5). It is possible that these differences, although subtle, explain the reduction in affinity for the dimethyl sterol substrate.

The aliphatic tails of all docked sterols reside in a hydrophobic cavity in domain A lined by the side chains of Tyr33, Pro34, Ala46, Met47, Met50, Ile89, Ser91, Leu92, Pro110, Ile112, Leu219, Met220, Val222, Leu244, Leu253, Cys254, Phe257, Ile259, and Phe262 in domain A. Sequence alignment shows that these residues are highly conserved between proteins in the same SSN cluster, implying their significance in forming the substrate binding pocket. Mutagenesis to remove or reduce the potential interactions with the polar head and the aliphatic tail showed subtle influences (<twofold) on the sterol binding affinity, indicating that the interaction between the protein and sterol is extensive and principally depends on hydrophobic interactions that are not easily disrupted (Figure 4—figure supplement 4). Moreover, the conformational dynamics of PBPs could mask the identity of additional residues that might be involved substrate binding and stabilization. Regardless, the determination of the sterol binding site in BstB remains to be experimentally verified.

To investigate whether BstB can undergo conformational change (as most PBPs do upon substrate binding), a 150 ns molecular dynamics simulation on apo-BstB was performed (Video 1). Plotting the RMSD of the simulated structure against the initial crystal structure at 25 ps intervals during the MD trajectory shows that for the first ~90 ns the protein showed some degree of flexibility (Figure 4—figure supplement 5A). During this part of the trajectory, the RMSD oscillates between 2.0 and 3.1 Å (average RMSD = 2.6 Å). At ~90 ns, there was a distinct conformational change in the structure giving rise to conformations with RMSDs ranging from 2.7 to 4.5 (average RMSD = 3.3 Å). Visual analysis of the MD trajectory shows that at ~90 ns the two domains open by approximately 20° (Figure 4—figure supplement 5B, Video 1). In contrast, the simulation (150 ns) on the MonoC docked complex which had a RMSD of 2.6 Å for the entire length of the trajectory and did not show the same conformational change as the apo-BstB simulation, which supports the idea that the apo-BstB structure represents a ‘partially-open’ form of the protein (Video 2).

![Video 1.](https://cdn.elifesciences.org/articles/90696/elife-90696-video1.mp4.jpg)

![Video 2.](https://cdn.elifesciences.org/articles/90696/elife-90696-video2.mp4.jpg)

### Crystallographic structure of BstC

The structure of BstC was also determined by experimental phasing to a resolution of 1.9 Å. Two monomers (RMSD of 0.656 Å for all Cαs) in the asymmetric unit form a dimer with 180 rotational symmetry. Each monomer adopts an all-α-helical structure with 12 α-helices in total, designated with H1 to H12; 9 antiparallel arranged helices (H4-H12) form an irregular ring with a pore running through the center. The H4, H6, H8, H10, H12 constitute the inside wall of the pore, while the others form the outside wall. Two helices (H1-H2) at the N-terminus sit on the side-top of the ring with a short helical turn (H3) connecting the two (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-v1.jpg)

**Figure 5.:** (A) Cartoon representation of BstC. The two α-helixes at the N-terminus are colored in green. Two monomers (RMSD of 0.656 Å for all Cαs) with 180 rotational symmetry exist in the asymmetric unit. (B) A representation of cavities BstC (left, with Tunnel 1 colored in green, Cavity 1 in red, and Cavity 2 in blue) alongside hydrophobicity representation of the cavities (right). (C) Docking model of the structures of BstC with 4-monomethyl sterol. Left, the docking model is shown in surface representation with 80% transparency. Sterol is shown in sphere and colored in green with the hydroxyl group is colored in red; Right, docking complex before and after MD simulation. The surrounding residues are shown in stick and ball. The sterol prior to the MD simulation is colored in grey and while green shows its position after the simulation. A hydrogen bond between the hydroxyl group of the sterol and Glu86 is shown as a red dashed line.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** TN1 exhibits hybrid hydrophobicity, with the sides horizontal to cavities being hydrophobic while the vertical sides are more hydrophilic.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-figsupp2-v1.jpg)

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** (A) Cartoon depiction of Tp0956 (PDB 3U64), the structural homolog of BstC. The protein contains four helical hairpins that are similar to tetratricopeptide repeat (TPR) motifs, which are hallmarks of proteins that engage in protein–protein interactions. The TPR motif was colored in grey. (B) Superposition of the BstC structure with Tp0956 (RMSD of 3.491 Å for all Cαs). BstC is colored in orange.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** Two peaks are observed in the SEC chromatogram, with SEC-MALS revealing that they correspond to monomeric and dimeric BstC.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** (A) Energetically favored poses of 4-monomethyl sterol. The sterol is colored in green. (B) Energetically favored poses of 4,4-dimethylsterol. The sterol is colored in orange (C) Docking complex of 4,4-dimethylsterol before and after MD simulation. The sterol prior to the MD simulation is colored in grey and while orange shows its position after the simulation. Sterols are shown in ball and stick with the hydroxyl group is colored in red; the surrounding residues are shown in sticks and colored in tan. Water-mediated hydrogen bonding between the hydroxyl group of the sterol and E86 is highlighted.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig5-figsupp6-v1.jpg)

**Figure 5—figure supplement 6.:** (A) The E86G and E86W variants bind to C4-mono-methyl sterol with Kds of 11.2±2.93 μM and 250.4±538.4 μM (B, C) No interaction was detected between BstC E86 variants and other sterols.

Hydrophobicity analysis shows that BstC has a predominantly hydrophilic exterior surface (Figure 5—figure supplement 1A). Three cavities are found in the center of the structure. We annotated them as Tunnel 1 (TN1), Cavity 1 (CA1) and Cavity 2 (CA2), with total area of ~597.1 Å2 and total volume of ~447 Å3. TN1 is closer to the N-terminal face of the structure, while CA1 and CA2 are proximal to the C-terminal face and form two open hydrophobic pockets; TN1 exhibits a mixture of hydrophobic and hydrophilic amino acids (Figure 5B and Figure 5—figure supplement 1B, Table 6). The extensive hydrophobic environment inside the BstC structure suggests it can accommodate large hydrophobic substrates. Notably, electrostatic calculation shows that most of the surface of BstC, especially the C-terminal face, exhibits strong negative charge (Figure 5—figure supplement 2). These charged surfaces may mediate protein-protein interactions, perhaps with BstB.

**Table 6.**
 Residues involved in forming the hydrophobic cavity in BstC.


<table>
  <thead>
    <tr>
      <th>Tunnel1</th>
      <th>Chamber2</th>
      <th>Chamber3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ASP 45</td>
      <td>GLY 128</td>
      <td>LEU 129</td>
    </tr>
    <tr>
      <td>PRO 49</td>
      <td>LEU 129</td>
      <td>ARG 132</td>
    </tr>
    <tr>
      <td>LEU 82</td>
      <td>ARG 132</td>
      <td>LEU 167</td>
    </tr>
    <tr>
      <td>HIS 83</td>
      <td>MET 135</td>
      <td>MSE 170</td>
    </tr>
    <tr>
      <td>GLU 86</td>
      <td>ALA 138</td>
      <td>LYS 174</td>
    </tr>
    <tr>
      <td>TYR 121</td>
      <td>LEU 139</td>
      <td>LEU 207</td>
    </tr>
    <tr>
      <td>TYR 122</td>
      <td>LEU 142</td>
      <td>PHE 208</td>
    </tr>
    <tr>
      <td>LEU 129</td>
      <td>LEU 145</td>
      <td>GLU 211</td>
    </tr>
    <tr>
      <td>ARG 132</td>
      <td>LEU 167</td>
      <td>GLU 251</td>
    </tr>
    <tr>
      <td>ASP 160</td>
      <td>MSE 170</td>
      <td>ASP 254</td>
    </tr>
    <tr>
      <td>ARG 166</td>
      <td>LEU 171</td>
      <td>LEU 255</td>
    </tr>
    <tr>
      <td>LEU 167</td>
      <td>LYS 174</td>
      <td></td>
    </tr>
    <tr>
      <td>LEU 204</td>
      <td>PHE 208</td>
      <td></td>
    </tr>
    <tr>
      <td>TRP 241</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ASN 244</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TRP 248</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

A structure similarity search using the DALI server revealed high homology to Tp0956 (PDB 3U64, Treponema pallidum strain Nichols). Tp0956 is the T-component protein of a subfamily of TRAP (tripartite ATP-independent periplasmic) transporters known as TPATs (tetratricopeptide repeat-protein associated TRAP transporters), which are implicated in the transport of organic acid ligands in bacteria (Brautigam et al., 2012). The true physiological substrate of Tp0956 has not been determined, but Treponema is a spirochete known to rely on import of host lipids and fatty acids to construct its cell envelope (Radolf et al., 2016).Tp0956 contains four helical hairpins that are similar to tetratricopeptide repeat (TPR) motifs, which are hallmarks of proteins that are involved in protein-protein interactions (D’Andrea and Regan, 2003). Comparison of the structures show that two antiparallel α-helices exist in Tp0956 are missing in the structure of BstC (between H5-H6), as well as a shorter H4 and H5. But the TPR-like substructure is also observed in BstC and forms part of the pore and lateral surface of the protein, hinting that BstC might engage with itself or other proteins (Figure 5—figure supplement 3). Size-exclusion chromatography coupled with multiangle light scattering (SEC-MALS) analysis shows that indeed the purified BstC exists both as a monomer and a dimer in solution with a ratio ~3:1 (Figure 5—figure supplement 4). However, the role of the dimerization in this protein is not clear and its determination will require additional studies.

### Substrate docking and molecular dynamics simulations with BstC

To assess substrate-binding, we performed the docking of 4-monomethyl sterol and 4,4-dimethyl sterol into the BstC structure using ICM-Pro. The final docking model was obtained by choosing the one with the most negative ICM-Pro score. All the sterols were found embedded in the hydrophobic cavity (CA1) lined by Gly128, Val131, Arg132, Met135, Ala138, Leu139, Leu142, Leu145, Leu167, Met170, Leu171, Lys174, Ala175, Pro176, and Phe208, with the hydroxyl group pointing inwards and the aliphatic tail pointed out (Figure 5C and Figure 5—figure supplement 5A–B). Residues involved in sterol interaction are located on H6, H7, H8 and H10 and are all highly conserved in a sequence alignment of the closest BstC homologs. No hydrogen bond is anticipated between the sterol and protein in the docking models.

We then performed multiple 20 ns molecular dynamics simulations on the docked models of 4-monomethyl sterol from ICM-Pro. The simulations reveal that the substrate moves approximately 8–9 Å further into the binding site and the polar head makes a hydrogen bonding contact with the side chain of Glu86 (Figure 5C). This movement takes place almost immediately and the hydrogen bond persists for 94% of the total time. In both the docking models and MD simulations, the sterol is positioned near the entrance of CA1 from the C-terminal side. Next to the entrance is an extended loop that consists of highly conserved hydrophobic and neutral residues (residues 175–184).

Intriguingly, simulations with the 4,4-dimethyl sterol revealed that it behaves differently in that it moves slowly inwards and does not get as deep (~2.6 Å) into the pocket as the monomethyl sterol (Figure 5 – figure supplement 5C). A water-mediated contact is formed between the polar head and the side chain of Glu86 but persist for only 2% of the time. This lack of additional movement and H-bonding interaction may explain the binding data, where the protein has a Kd for the monomethyl sterol that is ~30 × lower than for the dimethyl sterol substrate.

Mutagenesis to convert Glu86 to Gly and Trp to remove or reduce the potential interactions with the polar head of the sterols leads to ~4.5 and 100-fold decrease in the equilibrium affinity for 4-monomethyl sterol (Figure 5—figure supplement 6A). Meanwhile, the mutagenesis eliminates the binding to 4,4-dimethyl sterol, cholesterol and lanosterol (Figure 5—figure supplement 6B and C). These findings indicate that Glu86 plays a critical role in interacting with and stabilizing the sterols.

### Comparison to eukaryotic sterol transporters

In most eukaryotic cells, lipid transfer proteins (LTPs) are used to transfer sterols between subcellular membranes by non-vesicular transport to maintain sterol homeostasis in different sub-cellular organelles (Baumann et al., 2005). The most-studied family in mammals is the steroidogenic acute regulatory protein (StAR)-related lipid transfer (START) domain (STARD) proteins. All fifteen STARD proteins identified to date possess lipid-harboring START domains that can be divided into six subfamilies based on sequence similarity and ligand specificity. In addition to STARD proteins, a novel yet evolutionarily conserved family that contains the START-like domains called the GRAMD1s/Lam/Ltc family (GRAMD1s in mammals and Lam/Ltc in yeast) was shown to mediate non-vesicular sterol transport from the plasma membrane to the endoplasmic reticulum to maintain sterol homeostasis (Gatta et al., 2015). A third family consists of the Osh/ORP/OSBP proteins (Oxysterol-binding homology in yeast and Oxysterol-binding Protein/OSBP-Related Protein in mammals), which are considered to be either sterol-sensing and/or sterol-transfer proteins (Raychaudhuri and Prinz, 2010). Besides these, two Niemann-Pick type C proteins, NPC1 and NPC2, were also reported to directly bind and transport cholesterols and various oxysterols; defective NPC proteins causes NPC disease, a fetal neurodegenerative disorder where sterols aberrantly accumulate in the lysosome (Carstea et al., 1997).

To better understand the differences between eukaryotic and bacterial sterol transport, we compared the structures of BstB and BstC with well-studied eukaryotic sterol transporters from different families. Human STARD4 (PDB 6L1D), yeast Lam4 (PDB 6BYM), yeast Osh4 (PDB 1ZI7 and 1ZHY), yeast NPC2 (PDB 6R4M and 6R4N), as well as a non-specific cytosolic sterol carrier protein, rabbit SCP2 (PDB 1C44) were chosen for the comparison. The crystal structures of STARD4, Lam4 and Osh4 show that they share a similar fold in that they are dominated by β-sheet motifs, which wrap around the longest α-helix and fold into a half-barrel/groove structure with the other side (or two) packed with several α-helices (Figure 6A–D). A central hydrophobic cavity can accommodate sterols. In most cases, the sterols are positioned proximal to the tunnel entrance with the hydroxyl end oriented towards the inside of the tunnel. Also, a ‘lid’ comprising a flexible ‘Ω1’ loop is observed near the entrance of tunnel in STARD4 and sterol-bound Lam4. This loop is replaced by an N-terminal α-helix in Osh4, which serves a similar function. The SCP2 structure also exhibits an α/β-fold with a ‘lid’-like α-helix observed close to the N-terminus (Figure 6E). The sterol-bond NPC2 adopts an immunoglobulin-like β-sandwich fold with seven strands arranged into two β-sheets with a loosely packed hydrophobic cavity formed between the two sheets. The sterol is positioned at the entrance of the cavity with the hydroxyl end pointing out; no ‘lid’-like structure is observed in NPC2 structure (Figure 6F–G).

![Figure 6.](https://cdn.elifesciences.org/articles/90696/elife-90696-fig6-v1.jpg)

**Figure 6.:** (A) Apo human STARD4 (PDB 6L1D). (B) Yeast Lam4 bound to 25-hydroxycholesterol (PDB 6BYM). The Ω1-loop is depicted in structures that possess it. (C–D) Yeast apo- (C), PDB 1ZI7 and cholesterol-bound (D), PDB 1ZHY Osh4. The N-terminal helix α7 in Osh4, which is missing in the apo-Osh4 structure, may work similar to the Ω1-loop. (E) The non-specific LTP, rabbit SCP2 (PDB 1C44); (F) apo- (PDB 6R4M) and (G) ergosterol-bound (PDB 6R4N) NPC2. All structures are shown in cartoon representation with the α-helixes and β-strands colored in red and magenta, respectively. The bound sterol substrates are depicted in grey spheres with the hydroxyl group(s) colored in red. (H) The Ω1-like loop in BstC docked complex with monomethyl sterol.

Our comparative analysis shows that the eukaryotic sterol transporters share very little resemblance with BstB and BstC. The bilobed architecture of BstB is pronounced in its divergence from eukaryotic sterol transporters, suggesting that this protein evolved separately and may work in a distinct manner. For the all-helical BstC, the only similarities are the presence of a hydrophobic tunnel formed in the center of the protein that can accommodate sterols, and a loop next to the tunnel’s entrance that may also be used as a ‘lid’ to restrict access to the substrate binding site (Figure 6H).

## Discussion

Since their discovery more than 40 years ago, the function of bacterial sterols has remained a mystery. Recent identification of bacterial sterol demethylase enzymes that diverge from their eukaryotic counterparts provided renewed enthusiasm for deciphering the molecular machinery involved in bacterial sterol synthesis and trafficking (Lee et al., 2018). The aerobic methanotroph M. capsulatus is known to synthesize 4-monomethyl sterol from 4,4-dimethyl sterol and to accumulate these sterols in its outer membrane. Until now, the transport process remained elusive owing to lack of knowledge of transporters that facilitate the trafficking. We now fill this gap with the identification of potential transporters of C-4 methyl sterols in M. capsulatus: BstA, BstB, and BstC.

Bioinformatic analyses revealed that BstA, BstB, and BstC belong to well-studied families of bacterial metabolite transporters. High resolution structures of BstB and BstC show that their large ligand binding sites display a dichotomy of hydrophobic and hydrophilic amino acids whose sidechains interact with the sterol hydrophobic tail and hydrophilic head. For BstC, this is especially interesting, as the only other family member characterized, Tp0956 from Treponema pallidum, displays a similar dichotomous ligand site. Treponema pallidum, the causative agent of syphilis, is a spirochete known to acquire and use host lipids– it is possible that Tp0956, and perhaps other T-component proteins, are involved in lipid trafficking.

In summary, the Bst proteins share sequence and structural homology with bacterial transporters involved in the trafficking of essential nutrients such as sugars, amino acids, vitamins, solutes, and metal ions (Davidson et al., 2008; Higgins, 1992). Their implication in the transport of sterols expands the substrate repertoire for their respective families. The substrate binding sites detected in BstB and BstC should now enable the curation of functionally homologous sites in bacterial proteins, including in those from human pathogens known to traffic host lipids.

## Materials and methods

### Bioinformatic analyses

The SSNs were generated using EFI-EST sever (https://efi.igb.illinois.edu/efi-est/). Proteins are represented by nodes. Only the nodes that share pairwise sequence alignments greater than the user-specified value will be connected by edges to create a network that reveals potential functional relationships among the proteins (Atkinson et al., 2009). HMMER webserver (https://www.ebi.ac.uk/Tools/hmmer/) was used to predict the superfamilies of Bst proteins. BstA is predicted to be a member of MMPL family (pfam03176 or IPR004869). Because some homologs are not annotated in the pfam family, we first used the Blast function to identify proteins sharing homology with BstA in UniProtKB (https://www.uniprot.org/). Homologs within the cutoff value of 5.3×10–80 were also used in the SSN creation. The SSN was generated using the EFI-EST online tool (Gerlt et al., 2015) with an E-value threshold of 10–60 (~35% sequence identity); with this threshold, BstA proteins were grouped into a single cluster. UniRef50 (>50% sequence identity merged into a single node) was used to facilitate the calculation and save time during the SSN creation. BstB belongs to a family of ABC transporter phosphonate periplasmic substrate-binding proteins (pfam12974); this Pfam was selected to create an SSN at E-value threshold of 10–50 (~40% sequence identity). Homologous proteins found in the UniprotKB (cutoff at 1.6×10–62) were added to the network as well. UniRef90 standard (≥90% sequence identity merged into a single node) was used to create the BstB SSN. BstC is classified as a member of the TRAP transporter T-component superfamily (IPR038537), which are thought to facilitate the import of small molecules into the cytoplasm (Radolf et al., 2016). An SSN was constructed with this dataset and the homologous genes found in UniprotKB (cut-off at 6.1×10–39) at E-value threshold of 10–55 (~40% sequence identity). Cystoscape software (Shannon et al., 2003) was used to visualize the SSNs with the ‘organic’ layout. The genome neighborhood network and diagram were generated using the Enzyme Function Initiative-Genome Neighborhood Tool (EFI-GNT; https://efi.igb.illinois.edu/efi-gnt/) with the SSNs generated above. The neighborhood reading frame was set to 10 frames and the minimal co-occurrence was set to 20%.

### Attempted deletion of M. capsulatus Texas H156DRAFT_2759-2757

In attempts to generate the M. capsulatus Texas H156DRAFT_2759–2757 mutant, a linear DNA fragment was PCR-amplified from a plasmid containing a kanamycin resistance gene flanked by 1 kb M. capsulatus chromosomal sequence upstream of H156DRAFT_2759 and 1 kb downstream of H156DRAFT_2757. Electrocompetent M. capsulatus cells were prepared via the following protocol: a 300 mL culture was grown to mid-exponential phase, washed three times in 5% cold sterile glycerol and resuspended in 300 µL cold sterile 10% glycerol. The electrocompetent cells were mixed with 2.5 µL of the linear DNA fragment (1000 ng total) and shocked using various electroporation settings (Bacteria 1,2,3, and 5) on the Bio-Rad Pulser Xcell and the Ec1 setting on the Bio-Rad Micropulser [parameters were a combination of different cuvette gaps (0.1 cm or 0.2 cm), voltages (1.8–3.0 kV), resistances (200–400 Ω)]. Electroporated cells were grown up for 24 hr in 500 µL of media made with nitrate mineral salts (NMS) and methane; following this, the cells were plated on NMS-agar plates supplemented with kanamycin. No colonies were ever observed, suggesting that depletion of these transporters is toxic to the cells.

### Protein expression and purification

The genomic DNA of M. capsulatus Texas (ATCC 19069) was subjected to several rounds of PCR to isolate the genes encoding BstB and BstC without their respective signal peptides (cleavage sites determined by the SignalP 5.0 server; Almagro Armenteros et al., 2019). The final gene products were assembled into pET-28a vectors containing TEV-cleavable N-terminal hexa-histidine (His-) tags or pET-20b vectors containing C-terminal His-tags. DNA sequencing of the plasmids confirmed the correct insertion of the genes. The BstAPD gene was synthesized and inserted into pET-28a after codon optimization for expression in E. coli. The soluble periplasmic domain of BstA (BstAPD) was designed based on the structure predicted by AlphaFold (Jumper et al., 2021). Briefly, two fragments spanning residues 54–277 and 510–732 were connected by a GSGSGSGS linker to replace the membrane-spanning sequence. The DNA encoding BstAPD was cloned into pET28a. All the protein sequences and primers are listed in Table 6.

BstAPD, BstB (residues 24–281) and BstC (residues 16–264) proteins were expressed in E. coli BL21(DE3) cells and grown at 37 °C until OD600nm of 0.6. Protein expression was induced upon the addition of 0.25 mM isopropyl β-D-1thiogalactopyranoside (IPTG) while shaking at 18 °C for 12 hr. Cells were harvested through centrifugation at 8000×g for 15 min and resuspended in lysis buffer containing 25 mM Tris-HCl (pH 8.0), 100 mM NaCl, 2 mM 2-mercaptoethanol, and 1 mM phenylmethylsulfonyl fluoride (PMSF). Cells were lysed by microfluidization and centrifuged at 11,000×g for 40 min to remove cell debris. The supernatant was applied to a Ni-NTA affinity column (HiTrap IMAC FF, Cytiva product # 17092104), washed with lysis buffer supplemented with 15 mM imidazole to remove weakly bound proteins, and eluted with lysis buffer containing 300 mM imidazole. The eluate was concentrated and applied to a size-exclusion column (HiLoad 16/600 Superdex 200 pg, Cytiva product # 28989335) to remove additional contaminants, and purity was assessed through gel electrophoresis.

Selenium-methionine (Se-Met) labeled BstB and BstC were produced by supplementing the endogenous methionine synthesis of the expression host with Se-Met. The cells were cultured in M9 minimal media until OD600nm of 0.4. L-lysine (100 mg/L), L-phenylalanine (100 mg/L), L-threonine (100 mg/L), L-isoleucine (50 mg/L), L-leucine (50 mg/L) and L-valine (50 mg/L) and L-Se-Met (60 mg/L) were added to the media. 0.25 mM IPTG was added after 1 hr to commence induction and cells were cultured for an additional 12 hr at 18 °C before harvesting. The proteins were purified by the protocol described above.

The N-terminal His-tags of proteins were removed during overnight incubation at room temperature with TEV protease at a molar ratio of 1:100 (TEV: protein). Proteins without tags were further purified by size-exclusion chromatography. The molecular weight of proteins was determined by SEC-MALS (Wyatt Technology). The purity of all purified proteins was assessed using SDS-PAGE stained with Coomassie Brilliant Blue, after which aliquots of the purest fractions were flash-cooled in liquid nitrogen and stored at –80  °C.

### Size-exclusion chromatography (SEC)-coupled multi-angle light scattering (MALS)

SEC-MALS was performed using an in-line Superdex 200 Increase 3.2/300 GL SEC column (GE Healthcare) combined with a miniDawn Multi-Angle Light Scattering (MALS) detector coupled with an Optilab refractive index detector (Wyatt Technology, Santa Barbara, CA, USA). A total of 15 μL (~200 ng) protein was centrifuged at 13000 × g for 10 min before being injected into the pre-equilibrated SEC column with buffer (25 mM Tris-HCl (pH 8.0), 100 mM NaCl and 2 mM 2-mercaptoethanol). Proteins were separated at a flow rate of 0.15 mL/min at room temperature. Molecular masses were calculated using the Astra6.1 software (Wyatt Technology).

### Sterols extraction from M. capsulatus

Lipids were extracted from cell pellets of 2 L M. capsulatus cultures using a modified Bligh-Dyer extraction method as previously described.(Lee et al., 2018) Cells were re-suspended in 10:5:4 (vol:vol:vol) methanol: dichloromethane (DCM):water and sonicated for 1 hr. The organic phase was separated with 1:1 (vol:vol) DCM:water, later washed three times with DCM and then transferred to a clean vial and dried with N2 to yield the total lipids extraction (TLE). The TLE was further purified using Silica column chromatography to isolate the alcohol soluble lipids.(Summons et al., 2013) The TLE was added to a hand-packed silica column and lipids were eluted using solvent solutions of different polarities (Hexane, 8:2 Hexane:DCM, DCM, 1:1 DCM:Ethyl Acetate, Ethyl acetate). The alcohol soluble lipids (HS fraction) were eluted with 1:1 DCM:Ethyl Acetate. The HS fraction was then dried with N2 and dissolved in DMSO. The 4-methylsterol and 4,4-dimethylsterol were purified from the alcohol soluble lipids by liquid-chromatography (LC) using an Agilent 1260 Infinity II LC System. Briefly, lipids were run through a InfinityLab Poroshell120 EC-C18 column (4.6x150 mm, 2.7 Micron). The solvent system consisted of Solvent A: MeOH (with.04% formic acid and 0.1% ammonia), Solvent B: acetonitrile, and Solvent C: Water (with.04% formic acid and 0.1% ammonia). The solvent gradient started with 84% Solvent A, 1% Solvent B, and 15% Solvent C and ended with 100% Solvent A over the course of 50 min. Isolated sterols were derivatized to trimethylsilyl ethers with 1:1 (vol:vol) Bis(trimethylsilyl)trifluoroacetamide: pyridine and confirmed using GC-MS analysis as described in Lee et al., 2018.

### Protein-lipid pull down assay

Recombinantly expressed and purified proteins (BstAPD, BstB, BstC) were incubated with two different M. capsulatus lipid extracts: total lipid extractions (TLE) or the enriched sterol fraction of the TLE (HS), both dissolved in DMSO. The TLE (139.5 µg total) contained 65.7 ng of 4-monomethyl sterol and 338.9 ng of 4,4-dimethyl sterol. The HS fraction (99.5 µg total) contained 313.8 ng and 967 ng of 4-monomethyl sterol and 4,4-dimethyl sterol, respectively. The experimental reaction conditions are as follows: 40 µM protein (BstAPD, BstB, BstC) was incubated with 7.5 µL of either the TLE or HS lipids. The reactions were carried out in reaction buffer of 200 mM HEPES pH 8.0, 100 mM NaCl and 0.05% Triton X-100. During the negative control reactions, the proteins were incubated with DMSO that did not contain any lipids. This serves as (1) a vehicle control since the M. capsulatus TLE and HS fractions were dissolved in DMSO and (2) to determine whether C4-methylsterols were bound to the Bst proteins as a result of protein expression in E. coli. The reactions (both control and experiment) were incubated at 25 °C for 20 hr. The proteins were purified from the reactions using HisPur Ni-NTA resin (Thermos Fisher), lipids from the eluted protein fractions were extracted using a modified Bligh Dyer protocol (Ekiert et al., 2017; Lee et al., 2018) and lipid samples were analyzed by GC-MS as previously described. HisPur Ni-NTA wash buffer: 25 mM Tris pH 8.0, 100 mM NaCl elution buffer: 25 mM Tris pH 8.0,100 mM NaCl, 300 mM imidazole. SDS PAGE electrophoresis was conducted to demonstrate that the fractions analyzed did in fact contain protein.

### GC-MS analysis of M. capsulatus lipids

Derivatized lipids were separated with an Agilent 7890B Series GC equipped with 2 Agilent DB-17HT columns in tandem (each 30 m x 0.25 mm i.d. x 0.15 μm film thickness) with helium as the carrier gas at a constant flow of 1.1 ml/min. The program was as follows: 100 °C for 2 min, then 12 °C/min to 250 °C and held for 10 min, then 10 °C/min to 330 °C and held for 17.5 min. Two µL of each sample was injected in splitless mode at 250 °C. The GC was coupled to an Agilent 5977 A Series MSD with the ion source at 230 °C and operated at 70 eV in EI mode scanning from 50 to 850 Da in 0.5 s. Lipids were identified based on their retention time and compared to previously published spectra (Wei et al., 2016).

### Microscale thermophoresis

Microscale thermophoresis (MST) experiments were performed with NanoTemper Monolith NT.115 instrument according to the manufacturer’s instructions (NanoTemper Technologies). In brief, His-tagged BstAPD, BstB and BstC were fluorescently labeled with Monolith His-Tag Labeling Kit RED-tris-NTA 2nd Generation according to the manufacturer’s instructions. The 4-methylsterol and 4,4-dimethylsterol were extracted from M. capsulatus, while lanosterol (CAS:79630, Sigma-Aldrich) and cholesterol (CAS: AAA1147018, Fisher Scientific) were prepared in DMSO with a final stock concentration of 3.9 mM and 7.76 mM, respectively.

Fifty nM each of labeled proteins was diluted in assay buffer (20 mM HEPES pH 8.0, 100 mM NaCl, and 0.05% Tween 20), in the presence of 16-step serial dilution of 4-methylsterols or 4,4-dimethylsterols (ligand solubilized in DMSO at a final constant concentration of 5%). After incubation, samples were loaded into Monolith NT.115 Premium Capillaries (NanoTemper Technologies) and measurements were taken at a constant temperature of 23 °C. MST traces were collected with an LED excitation power of 40% and an MST laser power of 40%. The MO. Control Analysis software (NanoTemper) was used to analyze the interaction affinity and the equilibrium dissociation constant (Kd) for each ligand using the Kd fit model or Hill fit model. The data was exported and plotted in Prism.

Equation of Kd -model fitting:

$$
f(c)=\frac{c+c_{T}+K_{d}−\sqrt{(c+c_{T}+K_{d})^{2}}+4cc_{T}}{2c_{T}}
$$

f(c) is the fraction bound at a given ligand concentration c. Kd is the equilibrium dissociation constant and cT is the final concentration of target in the assay.

Equation for Hill-model fits:

$$
f(c)=Unbound+\frac{Bound−Unbound}{1+(\frac{EC_{50}}{C})^{n_{Hill}}}
$$

f(c) is the fraction bound at a given ligand concentration c. Unbound is the Fnorm signal of the target. Bound is the Fnorm signal of the complex. EC50 is the half-maximal effective concentration and nHill is the Hill coefficient. The Hill coefficient nHill describes the degree of cooperativity of an interaction: nHill >1 indicates positive cooperativity, while nHill <1 indicates negative cooperativity.

### Crystallization of BstB and BstC

Sparse-matrix crystallization screens were performed with purified proteins at concentrations of about 5 mg/mL for each. All crystals were obtained by the sitting-drop vapor diffusion method by mixing 0.5 μL protein and 0.5 μL precipitant solution at 20 °C. Native and Se-met BstB crystals appeared in the MCSG1-C12 condition containing 25% (v/v) PEG3500 and 0.1 M Bis-tris pH 6.5 after 1 week of incubation at 20 °C. Crystals were cryoprotected in the same conditions with the addition of 20% (v/v) PEG400 before being flash-cooled and stored in liquid nitrogen. Native and Se-Met BstC crystals appeared in the MCSG2-B3 condition containing 20% (v/v) PEG3500 and 0.2 M ammonium citrate dibasic after 2 weeks of incubation at 20 °C. Crystals were cryoprotected in the same conditions with the addition of 33% (v/v) PEG400 before being flash-cooled and stored in liquid nitrogen. Dimer-BstC crystals are obtained in the MCSG2-A12 condition containing 40% (v/v) PEG 600 and 0.1 M Sodium Citrate: Citric Acid, pH 5.5 after 2 weeks of incubation at 20 °C. Crystals were flash-cooled and stored in liquid nitrogen.

### Data collection, processing, and structure determination

All the diffraction datasets were collected at 100 K at the Stanford Synchrotron Rdaiation Lightsource (SSRL, Stanford, CA, USA). BstB and dimer-BstC datasets were collected used a Pilatus 6 M detector at beamline BL9-2, while BstC datasets were collected at beamline BL14-1 with a MARCCD325 detector. Native datasets were collected at a fixed wavelength at 0.97946 Å. MAD datasets were collected on ligand-free SeMet-substituted crystals at three wavelengths near the Se K-edge (0.97896 Å, 0.91837 Å, and 0.97930 Å). All diffraction datasets were indexed and processed by XDS (Kabsch, 2010a; Kabsch, 2010b) and HKL3000 packages (Minor et al., 2006) The structures of BstB and BstC were phased by the MAD method with Phenix AutoSol using the Se-anomalous diffraction (Liebschner et al., 2019). Subsequent density modiﬁcation gave excellent electron-density maps, which allowed the building of the models. Iterations of refinement were carried out with Phenix-Refine, and model building was performed in Coot. The statistics of data collection and refinement are listed in Table 3.

All structural figures were prepared using PyMOL (Schrödinger and DeLano, 2023) or UCSF Chimera (Pettersen et al., 2004). Cavities in BstB were assessed using CASTp (Tian et al., 2018) with a probe radius of 1.4 Å, equivalent to the radius of water. The tunnel through BstC was identified with MOLE2.0 (Pravda et al., 2018) using default settings and a probe radius of 1.4 Å.

### Docking of substrate to BstB and BstC

Molecular docking studies were performed using ICM-Pro 3.8–6 a (Abagyan et al., 1994b; Abagyan and Totrov, 1994a). Briefly, chain A of the BstB and BstC crystal structure was used as the rigid receptor. Each protein molecule was converted to an ICM object, with optimization of hydrogen atom placement. Potential binding site were identified using the pocketfinder feature of ICM-Pro (Abagyan and Kufareva, 2009; An et al., 2005); for BstB and BstC the largest pockets had volumes of 1050 A3 and 670 A3, respectively. The coordinates of the C-4 methylated sterols (4-monomethylsterol and 4,4-dimethylsterol) were generated using the ICM-Pro ligand editing tools, based upon the structure of cholesterol. The ligands were docked into the binding pockets in both protein receptors. The MA-1–206 docking runs were performed multiple times, results were ranked in order to the overall score, and the most energetically favored binding modes were extracted from ICM-Pro as PDB files. Additional docking runs with BstB were carried out where three residues (Glu118, Tyr120 and Asn192) were allowed to have rotationally flexible side chains to simulate induced fit docking, using the explicit group docking feature of ICM-Pro, while the rest of the protein remained rigid. Result analyses and figure rendering were performed using PyMOL (Schrödinger and DeLano).

### Molecular dynamics simulations of BstB and BstC

Molecular dynamics (MD) simulations were performed in triplicate on models comprising BstB and BstC docked with 4-monomethylsterol and 4,4-dimethylsterol, using Desmond (Bowers et al., 2006) in the Schrodinger 2019–2 release. The docked complexes were prepared with Maestro (Schrodinger) using the OPLS3e force field (Roos et al., 2019). The pre-defined TIP3P water model (Neria et al., 1996) was used to build the system. The overall charge of the complexes was calculated as –1 and –10 for BstB and BstC respectively and neutralized with Na+ ions. Prior to building in system for both complexes, 0.15 M salt (NaCl) was added, and the ions were restricted from coming within 20 Å of the ligand. The systems were minimized prior to the final 20 ns production step runs at 300  K and 1 atm pressure, using the Nosé–Hoover chain coupling scheme for the temperature control and the Martyna–Tuckerman–Klein chain coupling scheme with a coupling constant of 2.0 ps for pressure control (Martyna et al., 1992). Nonbonded forces were calculated using an r-RESPA integrator. The trajectories were saved at 10 ps intervals for analysis. For the 150 ns simulation on apo-BstB, the same protein preparation steps and variable settings were used except the trajectories were saved every 25 ps for analysis. Maestro and Desmond were run on the SHERLOCK 3.0 HPC cluster at Stanford University.
