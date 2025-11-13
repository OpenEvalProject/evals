# Metabolic co-dependence drives the evolutionarily ancient Hydra–Chlorella symbiosis

## Authors

- Mayuko Hamada<sup>1</sup> ([ORCID: 0000-0001-7306-2032](https://orcid.org/0000-0001-7306-2032))
- Katja Schröder<sup>3</sup> ([ORCID: 0000-0003-1158-2598](https://orcid.org/0000-0003-1158-2598))
- Jay Bathia<sup>3</sup>
- Ulrich Kürn<sup>3</sup>
- Sebastian Fraune<sup>3</sup> ([ORCID: 0000-0002-6940-9571](https://orcid.org/0000-0002-6940-9571))
- Mariia Khalturina<sup>1</sup>
- Konstantin Khalturin<sup>1</sup> ([ORCID: 0000-0003-4359-2993](https://orcid.org/0000-0003-4359-2993))
- Chuya Shinzato<sup>1</sup> ([ORCID: 0000-0001-7843-3381](https://orcid.org/0000-0001-7843-3381))
- Nori Satoh<sup>1</sup> ([ORCID: 0000-0002-4480-3572](https://orcid.org/0000-0002-4480-3572))
- Thomas CG Bosch<sup>3</sup> ([ORCID: 0000-0002-9488-5545](https://orcid.org/0000-0002-9488-5545)) †

### Affiliations

1. Marine Genomics Unit Okinawa Institute of Science and Technology Graduate University Okinawa Japan
2. Ushimado Marine Institute Okayama University Okayama Japan
3. Interdisciplinary Research Center, Kiel Life Science Kiel University Kiel Germany
4. Zoological Institute, Kiel Life Science Kiel University Kiel Germany
5. Atmosphere and Ocean Research Institute The University of Tokyo Tokyo Japan

† Corresponding author

## Abstract

Many multicellular organisms rely on symbiotic associations for support of metabolic activity, protection, or energy. Understanding the mechanisms involved in controlling such interactions remains a major challenge. In an unbiased approach we identified key players that control the symbiosis between Hydra viridissima and its photosynthetic symbiont Chlorella sp. A99. We discovered significant up-regulation of Hydra genes encoding a phosphate transporter and glutamine synthetase suggesting regulated nutrition supply between host and symbionts. Interestingly, supplementing the medium with glutamine temporarily supports in vitro growth of the otherwise obligate symbiotic Chlorella, indicating loss of autonomy and dependence on the host. Genome sequencing of Chlorella sp. A99 revealed a large number of amino acid transporters and a degenerated nitrate assimilation pathway, presumably as consequence of the adaptation to the host environment. Our observations portray ancient symbiotic interactions as a codependent partnership in which exchange of nutrients appears to be the primary driving force.

## Introduction

Symbiosis has been a prevailing force throughout the evolution of life, driving the diversification of organisms and facilitating rapid adaptation of species to divergent new niches (Moran, 2007; Joy, 2013; McFall-Ngai et al., 2013). In particular, symbiosis with photosynthetic symbionts is observed in many species of cnidarians such as corals, jellyfish, sea anemones and hydra, contributing to the ecological success of these sessile or planktonic animals (Douglas, 1994; Davy et al., 2012). Among the many animals dependent on algal symbionts, inter-species interactions between green hydra Hydra viridissima and endosymbiotic unicellular green algae of the genus Chlorella have been a subject of interest for decades (Muscatine and Lenhoff, 1963; Roffman and Lenhoff, 1969). Such studies not only provide insights into the basic ‘tool kit’ necessary to establish symbiotic interactions, but are also of relevance in understanding the resulting evolutionary selective processes (Muscatine and Lenhoff, 1965a; 1965b; Thorington and Margulis, 1981).

The symbionts are enclosed in the host endodermal epithelial cells within perialgal vacuoles called ‘symbiosomes’. The interactions at play here are clearly metabolic: the algae depend on nutrients that are derived from the host or from the environment surrounding the host, while in return the host receives a significant amount of photosynthetically fixed carbon from the algae. Previous studies have provided evidence that the photosynthetic symbionts provide their host with maltose, enabling H. viridissima to survive periods of starvation (Muscatine and Lenhoff, 1963; Muscatine, 1965; Roffman and Lenhoff, 1969; Cook and Kelty, 1982; Huss et al., 1994). Chlorella-to-Hydra translocation of photosynthates is critical for polyps to grow (Muscatine and Lenhoff, 1965b; Mews, 1980; Douglas and Smith, 1983; 1984). Presence of symbiotic algae also has a profound impact on hydra´s fitness by promoting oogenesis (Habetha et al., 2003; Habetha and Bosch, 2005).

Pioneering studies performed in the 1980 s (McAuley and Smith, 1982; Rahat and Reich, 1984) showed that there is a great deal of adaptation and specificity in this symbiotic relationship. All endosymbiotic algae found in a single host polyp are clonal and proliferation of symbiont and host is tightly correlated (Bossert and Dunn, 1986; McAuley, 1986a). Although it is not yet known how Hydra controls cell division in symbiotic Chlorella, Chlorella strain A99 is unable to grow outside its polyp host and is transmitted vertically to the next generation of Hydra, indicating loss of autonomy during establishment of its symbiotic relationship with this host (Muscatine and McAuley, 1982; Campbell, 1990; Habetha et al., 2003).

Molecular phylogenetic analyses suggest that H. viridissima is the most basal species in the genus Hydra and that symbiosis with Chlorella was established in the ancestral viridissima group after their divergence from non-symbiotic Hydra groups (Martínez et al., 2010; Schwentner and Bosch, 2015). A recent phylogenetic analysis of different strains of green hydra resulted in a phylogenetic tree that is topologically equivalent to that of their symbiotic algae (Kawaida et al., 2013), suggesting these species co-evolved as a result of their symbiotic relationship. Although our understanding of the factors that promote symbiotic relationships in cnidarians has increased (Shinzato et al., 2011; Davy et al., 2012; Lehnert et al., 2014; Baumgarten et al., 2015; Ishikawa et al., 2016), very little is known about the molecular mechanisms allowing this partnership to persist over millions of years.

Recent advances in transcriptome and genome analysis allowed us to identify the metabolic interactions and genomic evolution involved in achieving the Hydra-Chlorella symbiotic relationship. We present here the first characterization, to our knowledge, of genetic complementarity between green Hydra and Chlorella algae that explains the emergence and/or maintenance of a stable symbiosis. We also provide here the first report of the complete genome sequence from an obligate intracellular Chlorella symbiont. Together, our results show that exchange of nutrients is the primary driving force for the symbiosis between Chlorella and Hydra. Subsequently, reduction of metabolic pathways may have further strengthened their codependency. Our findings provide a framework for understanding the evolution of a highly codependent symbiotic partnership in an early emerging metazoan.

## Results

### Discovery of symbiosis-dependent Hydra genes

As tool for our study we used the green hydra H. viridissima (Figure 1A) colonized with symbiotic Chlorella sp. strain A99 (abbreviated here as Hv_Sym), aposymbiotic H. viridissima from which the symbiotic Chlorella were removed (Hv_Apo), as well as aposymbiotic H.viridissima, which have been artificially infected with Chlorella variabilis NC64A (Hv_NC64A). The latter is symbiotic to the single-cellular protist Paramecium (Karakashian and Karakashian, 1965). Although an association between H. viridissima and Chlorella NC64A can be maintained for some time, both their growth rate (Figure 1B) and the number of NC64A algae per Hydra cell (Figure 1—figure supplement 1) are significantly reduced compared to the symbiosis with native symbiotic Chlorella A99.

![Figure 1.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig1-v2.jpg)

**Figure 1.:** (A) Hydra viridissima strain A99 used for this study. Scale bar, 2 mm. (B) Growth rates of polyps grown with native symbiotic Chlorella A99 (Hv_Sym, dark green), Aposymbiotic polyps from which Chlorella were removed (Hv_Apo, orange) and aposymbiotic polyps reinfected with Chlorella variabilis NC64A (Hv_NC64A, light green). Average of the number of hydra in each experimental group (n = 6) is represented. Error bars indicate standard deviation. (C) Graphic representation of differentially expressed genes identified by microarray. The transcriptome of Hv_Sym is compared with that of Hv_Apo and Hv_NC64A with the number of down-regulated contigs in Hv_Sym shown in red and those up-regulated in green. Genes differentially expressed in Hv_Sym compared to both Hv_Apo and Hv_NC64A are given as ‘A99-specific’, those differentially expressed between Hv_A99 and Hv_Apo but not Hv_NC64A as ‘Symbiosis-regulated’. (D) GO distribution of Biological Process at level two in all contigs (All), up-regulated contigs (Hv_Sym > Hv_Apo) and down-regulated contigs (Hv_Sym < Hv_Apo) in Hv_Sym. (E) Overrepresented GO terms in up-regulated contigs (Hv_Sym > Hv_Apo) and down-regulated contigs (Hv_Sym < Hv_Apo). Category, F: molecular function, C: cellular component, P: biological process. P-values, probability of Fisher’s exact test. #Test, number of corresponding contigs in differentially expressed contigs. #Ref, number of corresponding contigs in all contigs.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Average number of algae per Hydra cell, for native Chlorella sp. A99 (Hv_Sym) and aposymbiotic Hydra re-infected with Chlorella variabilis NC64A (Hv_NC64A). P: p-value of student t-test. (B) Endodermal epithelial cells of Hv_Sym showing intracellular algae (C) Endodermal epithelial cells of Hv_NC64A. Scale bar, 20 µm.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Distribution of well-conserved Hydra viridissma genes (pink), Hydra viridissima-specific genes (green) and other genes (shared by some but not all metazoans, gray) among eight metazoans: Hydra magnipapillata, Acropora digitifera, Nematostella vectensis, Strongylocentrotus pupuratus, Branchiostoma floridae, Homo sapiens and Drosophila melanogaster and Hydra viridissima A99. Pie charts are shown for all contigs (All), up-regulated contigs (Hv_Sym > Hv_Apo) and down-regulated contigs (Hv_Sym < Hv_Apo).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Phylogenetic tree of the GS gene of four species in Cnidarians. While anthozoans (Nematostella vectensis, Acropora digitifera) have a single GS gene, Hydra magnipappilata (Hma) has five genes and Hydra viridissima A99 has three genes, Hv_1046 (GS-1), Hv_315 (GS-2) and Hv_4671 (GS-3). (B) Average of relative expression level of the three GS genes in Hv_Sym, Hv_NC64A and Hv_Apo as determined by microarray analysis. Error bars indicate standard deviation. P-value of t-test, *<0.05.

H.H. viridissima genes involved in the symbiosis with Chlorella algae were identified by microarray based on the contigs of H. viridissima A99 transcriptome (NCBI GEO Platform ID: GPL23280). For the microarray analysis, total RNA was extracted from the polyps after light exposure for six hours. By comparing the transcriptomes of Hv_Sym and Hv_Apo, we identified 423 contigs that are up-regulated and 256 contigs that are down-regulated in presence of Chlorella A99 (Figure 1C). To exclude genes involved in oogenesis and embryogenesis, only contigs differently expressed with similar patterns in both sexual and asexual Hv_Sym were recorded. Interestingly, contigs whose predicted products had no discernible homologs in other organisms including other Hydra species were overrepresented in these differentially expressed contigs (Chi-squared test p<0.001) (Figure 1—figure supplement 2). Such taxonomically restricted genes (TRGs) are thought to play important roles in the development of evolutionary novelties and morphological diversity within a given taxonomic group (Khalturin et al., 2009; Tautz and Domazet-Lošo, 2011).

We further characterized functions of the differentially expressed Hydra genes by Gene Ontology (GO) terms (Ashburner et al., 2000) and found the GO term ‘localization’ overrepresented among up-regulated contigs (Hv_Sym > Hv_Apo), whereas the GO term ‘metabolic process’ was enriched among down-regulated contigs (Hv_Sym < Hv_Apo) (Figure 1D). More specifically, the up-regulated contigs included many genes related to ‘transmembrane transporter activity’, ‘transmembrane transport’, ‘transposition’, ‘cilium’ and ‘protein binding, bridging’ (Figure 1E). In the down-regulated contig set, the GO classes ‘cellular amino acid metabolic process’, ‘cell wall organization or biogenesis’ and ‘peptidase activity’ were overrepresented (Figure 1E). These results suggest that the Chlorella symbiont affects core metabolic processes and pathways in Hydra. Particularly, carrier proteins and active membrane transport appear to play a prominent role in the symbiosis.

As next step, we used GO terms, domain search and similarity search to further analyze the differentially expressed contigs between Hv_Sym and Hv_Apo (Supplementary file 1). As the genes with GO terms related to localization and transport, we identified 27 up-regulated contigs in Hv_Sym (Table 1). Interestingly, this gene set included a contig showing sequence similarity to the glucose transporter GLUT8 gene, which was previously reported to be up-regulated in the symbiotic state of the sea anemone Aiptasia (Lehnert et al., 2014; Sproles et al., 2018). Thus, a conserved mechanism may be responsible for photosynthate transport from the symbiont into the host cytoplasm across the symbiosome membrane. Further, a contig encoding a carbonic anhydrase (CA) enzyme was up-regulated in Hv_Sym (Table 1). CA catalyzes the interconversion of HCO3 and CO2. Similar to the GLUT8 gene, carbonic anhydrase also appears to be up-regulated in symbiotic corals and anemones (Weis et al., 1989; Grasso et al., 2008; Ganot et al., 2011; Lehnert et al., 2014). It appears plausible that for efficient photosynthesis in symbiotic algae, the host may need to convert CO2 to the less freely diffusing inorganic carbon (HCO3) to maintain it in the symbiosome (Lucas and Berry, 1985; Weis et al., 1989; Barott et al., 2015). We also observed up-regulation of contigs encoding proteins involved in vesicular and endosomal trafficking, such as spe-39 protein, otoferlin, protein fam194b and V-type proton ATPase 21 kda proteolipid, which may have a function in nutrition exchange between host and symbiont and maintenance of proper condition in the symbiosome. Upregulated genes also include genes encoding rhamnospondin and fibrillin, known to be involved in cell adhesion and extracellular matrix, and retention of the symbiont at the proper site in the Hydra cells.

**Table 1.**
 List of differentially expressed genes between Hv_Sym and Hv_Apo, which are likely to be involved in symbiotic relationship


<table>
  <thead>
    <tr>
      <th rowspan="2">Probename</th>
      <th colspan="3">Fold change</th>
      <th rowspan="2" colspan="2">Human_BestHit</th>
      <th rowspan="2">blast2GO_Description</th>
    </tr>
    <tr>
      <th>Hv_Sym /Hv_Apo</th>
      <th>Hv_Sym_sexy /Hv_Apo</th>
      <th>Hv_NC64A /Hv_Sym</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">Localization and Transport</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &gt; Hv_Apo</td>
    </tr>
    <tr>
      <td>rc_6788</td>
      <td>9.87</td>
      <td>8.00</td>
      <td>1.01</td>
      <td colspan="2"></td>
      <td>helicase conserved c-terminal domain containing protein</td>
    </tr>
    <tr>
      <td>rc_10246</td>
      <td>8.26</td>
      <td>5.15</td>
      <td>1.82</td>
      <td colspan="2"></td>
      <td>protein</td>
    </tr>
    <tr>
      <td>rc_6298</td>
      <td>7.10</td>
      <td>4.73</td>
      <td>0.99</td>
      <td colspan="2">hypothetical protein LOC220081</td>
      <td>protein fam194b</td>
    </tr>
    <tr>
      <td>2268</td>
      <td>6.96</td>
      <td>3.58</td>
      <td>1.26</td>
      <td colspan="2">protein Daple</td>
      <td>viral a-type inclusion protein</td>
    </tr>
    <tr>
      <td>10548</td>
      <td>6.74</td>
      <td>6.89</td>
      <td>0.73</td>
      <td colspan="2">transient receptor potential cation channel subfamily M member three isoform d</td>
      <td>transient receptor potential cation channel subfamily m member 3-like</td>
    </tr>
    <tr>
      <td>rc_1290</td>
      <td>6.44</td>
      <td>7.18</td>
      <td>0.99</td>
      <td colspan="2">tetratricopeptide repeat protein eight isoform B</td>
      <td>tetratricopeptide repeat protein 8</td>
    </tr>
    <tr>
      <td>18736</td>
      <td>6.04</td>
      <td>6.34</td>
      <td>1.03</td>
      <td colspan="2">BTB/POZ domain-containing protein KCTD9</td>
      <td>btb poz domain-containing protein kctd9-like; unnamed protein product</td>
    </tr>
    <tr>
      <td>rc_9270</td>
      <td>5.96</td>
      <td>10.03</td>
      <td>1.37</td>
      <td colspan="2">PREDICTED: hypothetical protein LOC100131693</td>
      <td>eukaryotic translation initiation factor 4e</td>
    </tr>
    <tr>
      <td>NPNHRC_15697</td>
      <td>3.85</td>
      <td>2.74</td>
      <td>0.62</td>
      <td colspan="2"></td>
      <td>major facilitator superfamily domain- containing protein 1</td>
    </tr>
    <tr>
      <td>290</td>
      <td>3.68</td>
      <td>3.73</td>
      <td>1.32</td>
      <td colspan="2">splicing factor, arginine/ serine-rich 6</td>
      <td>splicing arginine serine-rich 4</td>
    </tr>
    <tr>
      <td>rc_9596</td>
      <td>3.56</td>
      <td>4.19</td>
      <td>1.62</td>
      <td colspan="2">BTB/POZ domain-containing protein KCTD10</td>
      <td>btb poz domain-containing adapter for cul3-mediated degradation protein 3</td>
    </tr>
    <tr>
      <td>rc_6774</td>
      <td>3.34</td>
      <td>3.32</td>
      <td>1.31</td>
      <td colspan="2">solute carrier family 43, member 2</td>
      <td>large neutral amino acids transporter small subunit 4</td>
    </tr>
    <tr>
      <td>rc_26218</td>
      <td>3.29</td>
      <td>2.91</td>
      <td>0.41</td>
      <td colspan="2">sodium-dependent phosphate transport protein 2A isoform 1</td>
      <td>sodium-dependent phosphate transport protein 2b</td>
    </tr>
    <tr>
      <td>NPNHRC_26094</td>
      <td>3.20</td>
      <td>3.98</td>
      <td>1.31</td>
      <td colspan="2">SPE-39 proteinid="T5"</td>
      <td>spe-39 protein</td>
    </tr>
    <tr>
      <td>9096</td>
      <td>3.10</td>
      <td>2.20</td>
      <td>0.69</td>
      <td colspan="2">otoferlin isoform d</td>
      <td>otoferlin</td>
    </tr>
    <tr>
      <td>rc_21349</td>
      <td>2.89</td>
      <td>4.25</td>
      <td>0.78</td>
      <td colspan="2">5'-AMP-activated protein kinase catalytic subunit alpha-2</td>
      <td>5 -amp-activated protein kinase catalytic subunit alpha-2</td>
    </tr>
    <tr>
      <td>npRC_14488</td>
      <td>2.88</td>
      <td>2.65</td>
      <td>0.71</td>
      <td colspan="2">solute carrier family 2, facilitated glucose transporter member 8</td>
      <td>solute carrier family facilitated glucose transporter member 8-like</td>
    </tr>
    <tr>
      <td>8863</td>
      <td>2.75</td>
      <td>2.70</td>
      <td>0.81</td>
      <td colspan="2">ATP-binding cassette, sub-family B, member 10 precursor</td>
      <td>abc transporter b family protein</td>
    </tr>
    <tr>
      <td>rc_11896</td>
      <td>2.49</td>
      <td>2.56</td>
      <td>1.52</td>
      <td colspan="2">ATP-binding cassette, sub-family B, member 10 precursor</td>
      <td>abc transporter b family member 25-like</td>
    </tr>
    <tr>
      <td>rc_6842</td>
      <td>2.41</td>
      <td>3.35</td>
      <td>1.59</td>
      <td colspan="2">hypothetical protein LOC112752 isoform 2</td>
      <td>intraflagellar transport protein 43 homolog</td>
    </tr>
    <tr>
      <td>5242</td>
      <td>2.36</td>
      <td>3.35</td>
      <td>1.22</td>
      <td colspan="2">growth arrest-specific protein 8</td>
      <td>growth arrest-specific protein 8</td>
    </tr>
    <tr>
      <td>5815</td>
      <td>2.23</td>
      <td>2.47</td>
      <td>0.78</td>
      <td colspan="2">plasma membrane calcium- transporting ATPase 4 isoform 4a</td>
      <td>plasma membrane calcium atpase</td>
    </tr>
    <tr>
      <td>8765</td>
      <td>2.22</td>
      <td>3.25</td>
      <td>0.91</td>
      <td colspan="2">growth arrest-specific protein 8</td>
      <td>growth arrest-specific protein 8</td>
    </tr>
    <tr>
      <td>NPNH_14052</td>
      <td>2.19</td>
      <td>2.17</td>
      <td>0.79</td>
      <td colspan="2">V-type proton ATPase 21 kDa proteolipid subunit isoform 2</td>
      <td>v-type proton atpase 21 kda proteolipid subunit-like</td>
    </tr>
    <tr>
      <td>rc_2499</td>
      <td>2.18</td>
      <td>2.03</td>
      <td>1.47</td>
      <td colspan="2">endoplasmic reticulum-Golgi intermediate compartment protein three isoform a</td>
      <td>endoplasmic reticulum-golgi intermediate compartment protein 3 isoform 2</td>
    </tr>
    <tr>
      <td>rc_13969</td>
      <td>2.08</td>
      <td>3.09</td>
      <td>0.97</td>
      <td colspan="2"></td>
      <td>major facilitator superfamily</td>
    </tr>
    <tr>
      <td colspan="7">(IPR023561) Carbonic anhydrase, alpha-class</td>
    </tr>
    <tr>
      <td>rc_24825</td>
      <td>2.49</td>
      <td>2.38</td>
      <td colspan="2">0.83</td>
      <td>protein tyrosine phosphatase, receptor type, G precursor</td>
      <td>receptor-type tyrosine-protein phosphatase gamma</td>
    </tr>
    <tr>
      <td colspan="7">Cell Adhesion and extracelluar matrix</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &gt; Hv_Apo</td>
    </tr>
    <tr>
      <td>7915</td>
      <td>4.01</td>
      <td>5.09</td>
      <td>0.94</td>
      <td colspan="2">fibrillin-2 precursor</td>
      <td>fibrillin-1- partial</td>
    </tr>
    <tr>
      <td>npRC_24163</td>
      <td>glutamate3.69</td>
      <td>3.59</td>
      <td>1.32</td>
      <td colspan="2">semaphorin 5A precursor</td>
      <td>rhamnospondin 1</td>
    </tr>
    <tr>
      <td colspan="7">Immunity, apoptosis and recognition</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &gt; Hv_Apo</td>
    </tr>
    <tr>
      <td colspan="7">(IPR000157) Toll/interleukin-1 receptor homology (TIR) domain</td>
    </tr>
    <tr>
      <td>5168</td>
      <td>9.28</td>
      <td>4.92</td>
      <td>0.61</td>
      <td colspan="2"></td>
      <td>protein; PREDICTED: uncharacterized protein LOC100893943</td>
    </tr>
    <tr>
      <td>12749</td>
      <td>5.13</td>
      <td>3.35</td>
      <td>1.26</td>
      <td colspan="2"></td>
      <td>PREDICTED: uncharacterized protein LOC100893943 [Strongylocentrotus purpuratus]</td>
    </tr>
    <tr>
      <td colspan="3">(IPR011029) DEATH-like</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
    </tr>
    <tr>
      <td>6508</td>
      <td>6.70</td>
      <td>5.10</td>
      <td>0.64</td>
      <td colspan="2"></td>
      <td>PREDICTED: hypothetical protein [Hydra magnipapillata]</td>
    </tr>
    <tr>
      <td>rc_2417</td>
      <td>5.39</td>
      <td>2.70</td>
      <td>1.01</td>
      <td colspan="2"></td>
      <td>nod3 partial; PREDICTED: uncharacterized protein LOC100206003</td>
    </tr>
    <tr>
      <td colspan="7">(IPR002398) Peptidase C14, caspase precursor p45</td>
    </tr>
    <tr>
      <td>NPNH_21275</td>
      <td>2.36</td>
      <td>3.53</td>
      <td>1.18</td>
      <td colspan="2">caspase seven isoform alpha precursor</td>
      <td>caspase d</td>
    </tr>
    <tr>
      <td colspan="7">(IPR016187) C-type lectin fold</td>
    </tr>
    <tr>
      <td>11411</td>
      <td>2.93</td>
      <td>2.98</td>
      <td>0.75</td>
      <td colspan="2">C-type mannose receptor 2</td>
      <td>PREDICTED: similar to predicted protein, partial [Hydra magnipapillata]</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &lt; Hv_Apo</td>
    </tr>
    <tr>
      <td colspan="7">(IPR000488) Death</td>
    </tr>
    <tr>
      <td>7319</td>
      <td>0.45</td>
      <td>0.31</td>
      <td>1.10</td>
      <td colspan="2">probable ubiquitin carboxyl- terminal hydrolase CYLD isoform 2</td>
      <td>ubiquitin carboxyl-terminal hydrolase cyld</td>
    </tr>
    <tr>
      <td colspan="7">(IPR001875) Death effector domain</td>
    </tr>
    <tr>
      <td>RC_FV81RT001CSTY</td>
      <td>0.31</td>
      <td>0.39</td>
      <td>0.93</td>
      <td colspan="2">astrocytic phosphoprotein PEA-15</td>
      <td>fadd</td>
    </tr>
    <tr>
      <td colspan="7">Chitinase</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &gt; Hv_Apo</td>
    </tr>
    <tr>
      <td colspan="7">(IPR001223) Glycoside hydrolase, family 18, catalytic domain</td>
    </tr>
    <tr>
      <td>rc_4450</td>
      <td>2.78</td>
      <td>3.83</td>
      <td>0.66</td>
      <td colspan="2"></td>
      <td>chitinase 2</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &lt; Hv_Apo</td>
    </tr>
    <tr>
      <td colspan="7">(IPR000726) Glycoside hydrolase, family 19, catalytic</td>
    </tr>
    <tr>
      <td>FPVQZVL01EAWBY</td>
      <td>0.21</td>
      <td>0.16</td>
      <td>1.78</td>
      <td colspan="2"></td>
      <td>endochitinase 1-like</td>
    </tr>
    <tr>
      <td>1028</td>
      <td>0.23</td>
      <td>0.18</td>
      <td>1.47</td>
      <td colspan="2"></td>
      <td>endochitinase 1-like</td>
    </tr>
    <tr>
      <td colspan="7">Oxidative Stress Response</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &gt; Hv_Apo</td>
    </tr>
    <tr>
      <td>np_1276</td>
      <td>5.99</td>
      <td>7.16</td>
      <td>0.78</td>
      <td colspan="2">glutaredoxin-2, mitochondrial isoform 2</td>
      <td>cpyc type</td>
    </tr>
    <tr>
      <td>10926</td>
      <td>3.9</td>
      <td>2.3</td>
      <td>0.8</td>
      <td colspan="2">hydroxysteroid dehydrogenase- like protein 2</td>
      <td>hydroxysteroid dehydrogenase-like protein 2</td>
    </tr>
    <tr>
      <td>469</td>
      <td>2.97</td>
      <td>3.53</td>
      <td>0.76</td>
      <td colspan="2">cytochrome P450 3A7</td>
      <td>cytochrome p450</td>
    </tr>
    <tr>
      <td>FV81RT001DCTAQ</td>
      <td>2.69</td>
      <td>2.50</td>
      <td>0.75</td>
      <td colspan="2">oxidoreductase NAD-binding domain-containing protein one precursor</td>
      <td>oxidoreductase nad-binding domain- containing protein 1</td>
    </tr>
    <tr>
      <td>696</td>
      <td>2.30</td>
      <td>3.24</td>
      <td>0.69</td>
      <td colspan="2">methionine-R-sulfoxide reductase B1</td>
      <td>selenoprotein 1; methionine-r-sulfoxide reductase b1-a-like</td>
    </tr>
    <tr>
      <td>6572</td>
      <td>2.23</td>
      <td>2.15</td>
      <td>1.06</td>
      <td colspan="2">L-xylulose reductase</td>
      <td>l-xylulose reductase</td>
    </tr>
    <tr>
      <td>13298</td>
      <td>2.10</td>
      <td>3.49</td>
      <td>0.64</td>
      <td colspan="2">eosinophil peroxidase preproprotein</td>
      <td>peroxidase</td>
    </tr>
    <tr>
      <td>npRC_6975</td>
      <td>2.04</td>
      <td>2.77</td>
      <td>1.42</td>
      <td colspan="2">methionine-R-sulfoxide reductase B1</td>
      <td>selenoprotein 1; methionine-r-sulfoxide reductase b1-a-like</td>
    </tr>
    <tr>
      <td colspan="7">(IPR024079) Metallopeptidase, catalytic domain</td>
    </tr>
    <tr>
      <td>Hv_array_4952</td>
      <td>4.77</td>
      <td>13.31</td>
      <td>0.72</td>
      <td colspan="2">meprin A subunit beta precursor</td>
      <td>zinc metalloproteinase nas-4-like</td>
    </tr>
    <tr>
      <td>Hv_array_rc_3992</td>
      <td>2.66</td>
      <td>2.23</td>
      <td>1.27</td>
      <td colspan="2">matrix metalloproteinase seven preproprotein</td>
      <td>matrix metalloproteinase-24-like</td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &lt; Hv_Apo</td>
    </tr>
    <tr>
      <td>RC_FWZAEML02HKSC</td>
      <td>0.255</td>
      <td>0.153</td>
      <td>1.444</td>
      <td colspan="2"></td>
      <td>ascorbate peroxidase</td>
    </tr>
    <tr>
      <td>np_14962</td>
      <td>0.293</td>
      <td>0.455</td>
      <td>1.390</td>
      <td colspan="2">tryptophan 5-hydroxylase 2</td>
      <td>phenylalanine hydroxylase</td>
    </tr>
    <tr>
      <td>rc_4151</td>
      <td>0.318</td>
      <td>0.463</td>
      <td>1.693</td>
      <td colspan="2">phenylalanine-4-hydroxylase</td>
      <td>phenylalanine hydroxylase</td>
    </tr>
    <tr>
      <td>2835</td>
      <td>0.384</td>
      <td>0.344</td>
      <td>1.787</td>
      <td colspan="2"></td>
      <td>u1 small nuclear ribonucleoprotein 70 kda</td>
    </tr>
    <tr>
      <td>rc_11426</td>
      <td>0.413</td>
      <td>0.458</td>
      <td>1.591</td>
      <td colspan="2">short-chain dehydrogenase/ reductase family 9C member 7</td>
      <td>uncharacterized oxidoreductase -like</td>
    </tr>
    <tr>
      <td>FWZAEML02IC34R</td>
      <td>0.427</td>
      <td>0.448</td>
      <td>1.159</td>
      <td colspan="2">aldehyde dehydrogenase 5A1 isoform two precursor</td>
      <td>succinate-semialdehyde mitochondrial-like</td>
    </tr>
    <tr>
      <td>FWZAEML02HKSCO</td>
      <td>0.454</td>
      <td>0.307</td>
      <td>0.833</td>
      <td colspan="2"></td>
      <td>ascorbate peroxidase</td>
    </tr>
    <tr>
      <td colspan="7">(IPR004045) Glutathione S-transferase, N-terminal</td>
    </tr>
    <tr>
      <td>RC_FWZAEML02GGHN</td>
      <td>0.09</td>
      <td>0.07</td>
      <td>1.81</td>
      <td colspan="2">hematopoietic prostaglandin D synthase</td>
      <td>glutathione s-transferase family member (gst-7)</td>
    </tr>
    <tr>
      <td colspan="7">(IPR024079) Metallopeptidase, catalytic domain</td>
    </tr>
    <tr>
      <td>rc_11270</td>
      <td>0.14</td>
      <td>0.20</td>
      <td>1.33</td>
      <td colspan="2">meprin A subunit beta precursor</td>
      <td>protein; zinc metalloproteinase nas-4-like</td>
    </tr>
    <tr>
      <td>rc_RSASM_15059</td>
      <td>0.22</td>
      <td>0.29</td>
      <td>1.42</td>
      <td colspan="2"></td>
      <td>---NA---</td>
    </tr>
    <tr>
      <td>2111</td>
      <td>0.37</td>
      <td>0.43</td>
      <td>1.74</td>
      <td colspan="2">meprin A subunit beta precursor</td>
      <td>zinc metalloproteinase nas-4-like</td>
    </tr>
    <tr>
      <td>12451</td>
      <td>0.50</td>
      <td>0.39</td>
      <td>0.78</td>
      <td colspan="2">meprin A subunit alpha precursor</td>
      <td>zinc metalloproteinase nas-13- partial</td>
    </tr>
    <tr>
      <td colspan="7">(IPR013122) Polycystin cation channel, PKD1/PKD2</td>
    </tr>
    <tr>
      <td>28854</td>
      <td>0.37</td>
      <td>0.28</td>
      <td>0.94</td>
      <td colspan="2">polycystin-2</td>
      <td>receptor for egg jelly partial</td>
    </tr>
    <tr>
      <td>15774</td>
      <td>0.40</td>
      <td>0.26</td>
      <td>0.76</td>
      <td colspan="2">polycystic kidney disease protein 1-like two isoform a</td>
      <td>protein</td>
    </tr>
  </tbody>
</table>

Photosynthesis by symbiotic algae imposes Reactive Oxygen Species (ROS) that can damage lipids, proteins and DNA in the host cells (Lesser, 2006). Therefore, in symbiosis with photosynthetic organisms an appropriate oxidative stress response of the host is required for tolerance of the symbiont. Indeed, an increase of antioxidant activities in symbiotic states of cnidarians has been reported previously (Richier et al., 2005) and it has been suggested that ROS produced by stress could be the major trigger of symbiosis breakdown during coral bleaching (Lesser, 2006; Weis, 2008). To understand the oxidative stress response in green hydra, we searched the differentially expressed genes with the GO terms ‘response to oxidative stress’, ‘oxidation-reduction process’ and ‘oxidoreductase activity’. In Hv_Sym, contigs for peroxidase, methionine-r-sulfoxide reductase/selenoprotein and glutaredoxin, which are known to be related to oxidative stress response were up-regulated (Table 1). On the other hand, some contigs encoding glutathione S-transferase and ascorbate peroxidase were down-regulated in Hv_Sym. In addition, two contigs encoding polycystin were down-regulated in Hv_Sym. Polycystin is an intracellular calcium release channel that is inhibited by ROS (Montalbetti et al., 2008) and is also down-regulated in a different strain of symbiotic green hydra (Ishikawa et al., 2016). In addition, six contigs encoding metalloproteinases showed differential expression between Hv_Sym and Hv_Apo. Although metalloproteinases have many functions such as cleavage of cell surface proteins and remodeling of the extracellular matrix, in a previous study they also were found to play a role in the oxidative stress response (Császár et al., 2009). A key antioxidant in the oxidative stress response in symbiotic cnidarians turns out to be glutathione (Sunagawa et al., 2009; Meyer and Weis, 2012). The gene encoding glutathione S-transferase was previously observed to be downregulated in corals, sea anemones, different strains of green hydra and Paramecium (Kodama et al., 2014; Lehnert et al., 2014; Ishikawa et al., 2016; Mohamed et al., 2016). Our study supports this view (Table 1) and may point to a conserved feature of oxidative stress response in algal-animal symbiosis.

Previous studies have suggested that during establishment of coral–algal symbiosis the host immune response may be partially suppressed (Weis et al., 2008; Mohamed et al., 2016). Our observations in Hydra together with previous findings in corals indicate that regulation of symbiosis by innate immunity pathways indeed may be a general feature of cnidarian symbiosis. Among the differentially expressed contigs we identified a number of genes involved in innate immunity and apoptosis. Pattern recognition receptors (PRRs) and the downstream innate immunity and apoptosis pathways are thought to play important roles in various symbiotic interactions including cnidarian-dinoflagellate symbiosis (Davy et al., 2012). In Hv_Sym we found two up-regulated contigs that contain a Toll/interleukin-1 receptor (TIR) domain (Table 1). TIR is a known PRR that is inserted in the host cell membrane and plays an important role in the innate immune system by specifically recognizing microbial-associated molecular patterns, such as flagellin, lipopolysaccharide (LPS) and peptidoglycan (Hoving et al., 2014). Furthermore, we found one up-regulated contig with similarity to a mannose receptor gene with C-type lectin domain (Table 1). This is worth noting since C-type lectin receptors bind carbohydrates and some of them are known to function as PRRs. Host lectin-algal glycan interactions have been proposed to be involved in infection and recognition of symbionts in some cnidarians including green hydra, sea anemones and corals (Meints and Pardy, 1980; Lin et al., 2000; Wood-Charlson et al., 2006). Interestingly, up-regulation of C-type lectin genes was also observed during onset of cnidarian–dinoflagellate symbiosis (Grasso et al., 2008; Schwarz et al., 2008; Sunagawa et al., 2009; Mohamed et al., 2016).

Furthermore, contigs encoding chitinase enzymes also were differentially expressed between Hv_Sym and Hv_Apo (Table 1). Chitinases are involved in degradation of chitin, which is a component of the exoskeleton of arthropods and the cell wall of fungi, bacteria and some Chlorella algae (Kapaun and Reisser, 1995), and also might play a role in host-defense systems for pathogens which have chitinous cell wall. Chitinases are classified into two glycoside hydrolase families, GH18 and GH19, with different structures and catalytic mechanisms. In Hv_Sym two contigs encoding GH18 chitinases were up-regulated, while one contig encoding a GH19 chitinase was down-regulated, suggesting that the enzymes involved in chitin degradation are sensitive to the presence or absence of symbiotic Chlorella.

To narrow down the number of genes specifically affected by the presence of the native symbiont Chlorella A99, we identified 12 contigs that are differentially expressed in symbiosis with Chlorella A99, but not in presence of foreign Chlorella NC64A (Figure 1C A99-specific). Independent qPCR confirmed the differential expression pattern for 10 of these genes (Table 2). The genes up-regulated by the presence of the symbiont encode a Spot_14 protein, a glutamine synthetase (GS) and a sodium-dependent phosphate (Na/Pi) transport protein in addition to a H. viridissima specific gene (rc_12891: Sym-1) and a Hydra genus specific gene (rc_13570: Sym-2) (Table 2). Hydra genes down-regulated by the presence of Chlorella A99 were two H. viridissima-specific genes and three metabolic genes encoding histidine ammonia-lyase, acetoacetyl-CoA synthetase and 2-isopropylmalate synthase (Table 2). Of the up-regulated genes, Spot_14 is described as thyroid hormone-responsive spot 14 protein reported to be induced by dietary carbohydrates and glucose in mammals (Tao and Towle, 1986; Brown et al., 1997). Na/Pi transport protein is a membrane transporter actively transporting phosphate into cells (Murer and Biber, 1996). GS plays an essential role in the metabolism of nitrogen by catalyzing the reaction between glutamate and ammonia to form glutamine (Liaw et al., 1995). Interestingly, out of the three GS genes H. viridissima contains only GS-1 was found to be up-regulated by the presence of the symbiont (Figure 1—figure supplement 3). The discovery of these transcriptional responses points to an intimate metabolic exchange between the partners in a species-specific manner.

**Table 2.**
 List of genes differentially expressed in Hv_Sym compared to both Hv_Apo and Hv_NC64A (‘A99-specific’)Fold change of expression level determined by microarray analysis and qPCR analysisTable 2—source data 1.Expression level of ‘A99-specific’ genes and ‘Symbiosis related’ genes examined by microarray and qPCR.


<table>
  <thead>
    <tr>
      <th colspan="7">Hv_Sym &gt; Hv_Apo, Hv_NC64A</th>
    </tr>
    <tr>
      <th rowspan="2">Probe name (gene ID)</th>
      <th colspan="2">Microarray</th>
      <th colspan="2">qPCR</th>
      <th rowspan="2">Gene annotation</th>
      <th rowspan="2">InterProScan</th>
    </tr>
    <tr>
      <th>Sym/Apo</th>
      <th>Sym/NC64A</th>
      <th>Sym/Apo</th>
      <th>Sym/NC64A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rc_13579</td>
      <td>12.8</td>
      <td>4.0</td>
      <td>11.2</td>
      <td>4.0</td>
      <td>(Hydra specific)</td>
      <td></td>
    </tr>
    <tr>
      <td>rc_12891</td>
      <td>9.0</td>
      <td>2.9</td>
      <td>14.6</td>
      <td>6.9</td>
      <td>(Hydra viridis specific)</td>
      <td></td>
    </tr>
    <tr>
      <td>27417</td>
      <td>4.5</td>
      <td>4.8</td>
      <td>3.0</td>
      <td>3.0</td>
      <td></td>
      <td>IPR009786 Spot_14</td>
    </tr>
    <tr>
      <td>rc_26218</td>
      <td>3.3</td>
      <td>2.4</td>
      <td>2.5</td>
      <td>2.3</td>
      <td>sodium-dependent phosphate transport protein</td>
      <td>PTHR10010 Sodium-dependent phosphate transport protein 2C</td>
    </tr>
    <tr>
      <td>1046</td>
      <td>3.1</td>
      <td>2.1</td>
      <td>2.2</td>
      <td>1.6</td>
      <td>glutamine synthetase</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="7">Hv_Sym &lt; Hv_Apo, Hv_NC64A</td>
    </tr>
    <tr>
      <td rowspan="2">Probe name (gene ID)</td>
      <td colspan="2">Microarray</td>
      <td colspan="2">qPCR</td>
      <td rowspan="2">Gene Annotation</td>
      <td rowspan="2">InterProScan</td>
    </tr>
    <tr>
      <td>Apo/Sym</td>
      <td>NC64A/Sym</td>
      <td>Apo/Sym</td>
      <td>NC64A/Sym</td>
    </tr>
    <tr>
      <td>NPNHRC_26859</td>
      <td>83.2</td>
      <td>9.7</td>
      <td>∞</td>
      <td>∞</td>
      <td>(Hydra viridis specific)</td>
      <td></td>
    </tr>
    <tr>
      <td>RC_FVQRUGK01AXSJ</td>
      <td>13.7</td>
      <td>2.6</td>
      <td>2.1</td>
      <td>1.5</td>
      <td>acetoacetyl-CoA synthetase</td>
      <td></td>
    </tr>
    <tr>
      <td>rc_14793</td>
      <td>7.2</td>
      <td>4.1</td>
      <td>9.4</td>
      <td>4.8</td>
      <td>2-isopropylmalate synthase</td>
      <td>IPR013785 Aldolase_TIM,</td>
    </tr>
    <tr>
      <td>FV81RT002HT2FL</td>
      <td>2.8</td>
      <td>2.0</td>
      <td>3.1</td>
      <td>1.8</td>
      <td>histidine ammonia-lyase</td>
      <td>IPR001106 Aromatic_Lyase IPR008948 L-Aspartase-like</td>
    </tr>
    <tr>
      <td>NPNHRC_12201</td>
      <td>2.7glutamate</td>
      <td>2.3</td>
      <td>2.6</td>
      <td>2.5</td>
      <td>(Hydra viridis specific)</td>
      <td></td>
    </tr>
  </tbody>
</table>

To better understand the specificity of Hydra´s response to the presence of the foreign symbiont, we also identified the genes differentially expressed in Hydra polyps hosting a non-native Chlorella NC64A (Hv_NC64A) compared to both polyps hosting the obligate symbiont Chlorella A99 (Hv_A99) and aposymbiotic Hydra (Hv_Apo). We found 19 contigs that were up-regulated and 45 contigs that were down-regulated in presence of NC64A, which strikingly did not include any genes related to immunity or oxidative stress response (Supplementary file 1). Instead, the differentially expressed contigs showed similarity to methylase genes involved in ubiquinone menaquinone biosynthesis and secondary metabolite synthesis such as n-(5-amino-5-carboxypentanoyl)-l-cysteinyl-d-valine synthase and non-ribosomal peptide synthase. Four differentially expressed contigs specifically up-regulated in Hv_NC64A encoded ubiquitin carboxyl-terminal hydrolases, (Table 3).

**Table 3.**
 List of annotated genes up-regulated in Hv_NC64A compared to Hv_Sym


<table>
  <thead>
    <tr>
      <th>Probename</th>
      <th>Hv_NC64A/ Hv_Sym</th>
      <th>Hv_Apo/ Hv_Sym</th>
      <th>Hv_Sym_sexy/ Hv_Sym</th>
      <th>Blast2GO description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rc_1623</td>
      <td>4.57</td>
      <td>1.64</td>
      <td>5.98</td>
      <td>methylase involved in ubiquinone menaquinone biosynthesis</td>
    </tr>
    <tr>
      <td>28947</td>
      <td>3.52</td>
      <td>1.59</td>
      <td>0.63</td>
      <td>non-ribosomal peptide synthetase</td>
    </tr>
    <tr>
      <td>1353</td>
      <td>3.13</td>
      <td>1.63</td>
      <td>0.10</td>
      <td>nuclear protein set</td>
    </tr>
    <tr>
      <td>14347</td>
      <td>2.69</td>
      <td>2.40</td>
      <td>0.54</td>
      <td>n-(5-amino-5-carboxypentanoyl)-l -cysteinyl-d-valine synthase</td>
    </tr>
    <tr>
      <td>SSH_397</td>
      <td>2.67</td>
      <td>2.39</td>
      <td>0.50</td>
      <td>n-(5-amino-5-carboxypentanoyl)-l -cysteinyl-d-valine synthase</td>
    </tr>
    <tr>
      <td>RC_FWZAEML01C7BP</td>
      <td>2.28</td>
      <td>0.82</td>
      <td>0.41</td>
      <td>ubiquitin carboxyl-terminal hydrolase family protein</td>
    </tr>
    <tr>
      <td>RC_FVQRUGK01EOXS</td>
      <td>2.25</td>
      <td>1.52</td>
      <td>0.53</td>
      <td>ubiquitin carboxyl-terminal hydrolase family protein</td>
    </tr>
    <tr>
      <td>rc_11710</td>
      <td>2.15</td>
      <td>1.26</td>
      <td>0.31</td>
      <td>ubiquitin carboxyl-terminal hydrolase family protein</td>
    </tr>
    <tr>
      <td>1677</td>
      <td>2.10</td>
      <td>1.19</td>
      <td>0.38</td>
      <td>ubiquitin carboxyl-terminal hydrolase family protein</td>
    </tr>
    <tr>
      <td>rc_363</td>
      <td>2.21</td>
      <td>1.04</td>
      <td>0.76</td>
      <td>gcc2 and gcc3 family protein</td>
    </tr>
  </tbody>
</table>

### Symbiont-dependent Hydra genes are up-regulated by photosynthetic activity of Chlorella A99

To test whether photosynthetic activity of the symbiont is required for up-regulation of gene expression, Hv_Sym was either cultured under a standard 12 hr light/dark alternating regime or continuously in the dark for 1 to 4 days prior to RNA extraction (Figure 2A). Interestingly, four (GS1, Spot14, Na/Pi and Sym-1) of five genes specifically activated by the presence of Chlorella A99 showed significant up-regulation when exposed to light (Figure 2B), indicating the relevance of photosynthetic activity of Chlorella. This up-regulation was strictly dependent on presence of the algae, as in aposymbiotic Hv_Apo the response was absent (Figure 2B). On the other hand, symbiosis-regulated Hydra genes not specific for Chlorella A99 (Figure 1C Symbiosis-regulated, Table 4) appear to be not up-regulated in a light-dependent manner (Figure 2—figure supplement 1). These genes are involved in Hydra´s innate immune system (e.g. proteins containing Toll/interleukin-1 receptor domain or Death domain) or in signal transduction (C-type mannose receptor, ephrin receptor, proline-rich transmembrane protein 1, ‘protein-kinase, interferon-inducible double stranded RNA dependent inhibitor, repressor of (p58 repressor)’). That particular transcriptional changes observed in Hydra rely solely on the photosynthetic activity of Chlorella A99 was confirmed by substituting the dark incubation with selective chemical photosynthesis inhibitor DCMU (Dichorophenyl-dimethylurea) (Vandermeulen et al., 1972), which resulted in a similar effect (Figure 2C,D).

![Figure 2.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig2-v2.jpg)

**Figure 2.:** (A) Sampling scheme. Hv_Sym (green) and Hv_Apo (orange) were cultured under a standard light-dark regime (Light: L) and in continuous darkness (Dark: D), and RNA was extracted from the polyps at the days indicated by red arrows. (B) Expression difference of five A99-specific genes in Hv_Sym (green bars) and Hv_Apo (orange bars) between the light-dark condition and darkness. The vertical axis shows log scale (log2) fold changes of relative expression level in Light over Dark. (C) Sampling scheme of inhibiting photosynthesis. (D) Differential expression of the five A99-specific genes under conditions allowing (Control) or inhibiting photosynthesis (DCMU). The vertical axis shows log scale (log2) fold changes of relative expression level in Control over DCMU treated. T-tests were performed between Light and Dark (B), and DCMU and Control (D). For each biological replicate (n = 3) 50 hydra polyps were used for total RNA extraction. Error bars indicate standard deviation. P-value of t-test, *<0.05, **<0.01.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Sampling scheme. Hv_Sym was cultured in the light-dark condition (Light: L) and in the continuous dark (Dark: D). Gene expression levels were examined by qPCR at 1, 2, 4 days for each condition (red arrows). (B) Expression difference of the genes in Hv_A99 between the two conditions. DEATH-1 and DEATH-2: Death domain containing proteins (gene ID: 6508 and rc_2417), TIR: Toll/interleukin-1 receptor domain containing protein (gene ID: 5168), PRKRIR: protein-kinase interferon-inducible double stranded RNA dependent inhibitor, repressor of (p58 repressor) (gene ID: rc_9398), ephrinR: ephrin receptor (gene ID: 26108), CLEC: C-type mannose receptor (gene ID: 11411), PRRT1: proline-rich transmembrane protein 1 (gene ID: rc_24563). For each biological replicate (n = 3) 50 hydra polyps were used for total RNA extraction. The vertical axis shows log scale (log2) fold change of relative expression levels in the light condition over the dark condition. Error bars indicate standard deviation. Pvalue of t-test, *<0.05, **<0.01.

**Table 4.**
 List of the genes differentially expressed between Hv_Sym and Hv_ApoFold change of expression level determined by microarray analysis and qPCRTable 4—source data 1.Expression level of 'Symbiosis related' genes examined by microarray and qPCR.


<table>
  <thead>
    <tr>
      <th colspan="5">Hv_Sym &gt; Hv_Apo</th>
    </tr>
    <tr>
      <th rowspan="2">Probe name (gene ID)</th>
      <th>Microarray</th>
      <th>qPCR</th>
      <th rowspan="2">Gene annotation</th>
      <th rowspan="2">InterProScan</th>
    </tr>
    <tr>
      <th>Sym/Apo</th>
      <th>Sym/Apo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5168</td>
      <td>9.3</td>
      <td>7.4</td>
      <td></td>
      <td>IPR000157 TIR_dom PTHR23097 Tumor necrosis factor receptor superfamily member</td>
    </tr>
    <tr>
      <td>6508</td>
      <td>6.7</td>
      <td>2.9</td>
      <td></td>
      <td>IPR011029:DEATH-like_dom</td>
    </tr>
    <tr>
      <td>11411</td>
      <td>2.9</td>
      <td>2.0</td>
      <td>C-type mannose receptor 2</td>
      <td>IPR000742 EG-like_dom IPR001304 C-type_lectin</td>
    </tr>
    <tr>
      <td>26108</td>
      <td>7.2</td>
      <td>7.2</td>
      <td>ephrin type-A receptor six isoform a</td>
      <td></td>
    </tr>
    <tr>
      <td>rc_2417</td>
      <td>5.4</td>
      <td>3.5</td>
      <td></td>
      <td>IPR000488 Death_domain</td>
    </tr>
    <tr>
      <td>rc_24563</td>
      <td>6.1</td>
      <td>6.7</td>
      <td>Proline-rich transmembrane protein 1</td>
      <td>IPR007593 CD225/Dispanin_fam PTHR14948 NG5</td>
    </tr>
    <tr>
      <td>rc_9398</td>
      <td>6.2</td>
      <td>5.4</td>
      <td>protein-kinase, interferon-inducible double stranded RNA dependent inhibitor, repressor of (P58 repressor)</td>
      <td>PTHR11697 general transcription factor 2-related zinc finger protein</td>
    </tr>
    <tr>
      <td colspan="5">Hv_Sym &lt; Hv_Apo</td>
    </tr>
    <tr>
      <td rowspan="2">Probe name (gene ID)</td>
      <td>Microarray</td>
      <td>qPCR</td>
      <td rowspan="2">Gene Annotation</td>
      <td rowspan="2">InterProScan</td>
    </tr>
    <tr>
      <td>Apo/Sym</td>
      <td>Apo/Sym</td>
    </tr>
    <tr>
      <td>rc_10789</td>
      <td>2.5</td>
      <td>3.7</td>
      <td>endoribonuclease Dicer</td>
      <td>IPR000999 RNase_III_dom PTHR1495 helicase-related</td>
    </tr>
    <tr>
      <td>rc_12826</td>
      <td>3.0</td>
      <td>2.3</td>
      <td>interferon regulatory factor 1</td>
      <td>IPR001346 Interferon_reg_fact_DNA-bd_dom; IPR011991 WHTH_DNA-bd_dom PTHR11949 interferon regulatory factor</td>
    </tr>
    <tr>
      <td>rc_8898</td>
      <td>6.1</td>
      <td>4.1</td>
      <td>leucine-rich repeat-containing protein 15 isoform b</td>
      <td>IPR001611 Leu-rich_rp PTHR24373 Toll-like receptor 9</td>
    </tr>
    <tr>
      <td>FV81RT001CSTY</td>
      <td>3.2</td>
      <td>2.0</td>
      <td>astrocytic phosphoprotein PEA-15</td>
      <td>IPR001875 DED, IPR011029 DEATH-like_dom</td>
    </tr>
    <tr>
      <td>RSASM_17752</td>
      <td>4.0</td>
      <td>2.1</td>
      <td>CD97 antigen isoform two precursor</td>
      <td>IPR000832 GPCR_2_secretin-like PTHR12011 vasoactive intestinal polypeptide receptor 2</td>
    </tr>
  </tbody>
</table>

### Symbiont-dependent Hydra genes are expressed in endodermal epithelial cells and up-regulated by sugars

To further characterize the symbiont induced Hydra genes, we performed whole mount in situ hybridization (Figure 3A–F) and quantified transcripts by qPCR using templates from isolated endoderm and ectoderm (Figure 3—figure supplement 1), again comparing symbiotic and aposymbiotic polyps (Figure 3G–I). The GS-1 gene and the Spot14 gene are expressed both in ectoderm and in endoderm (Figure 3A,B) and both genes are strongly up-regulated in the presence of the symbiont (Figure 3G,H). In contrast, the Na/Pi gene was expressed only in the endoderm (Figure 3C) and there it was strongly up-regulated by the symbiont (Figure 3I). Since Chlorella sp. A99 colonizes endodermal epithelial cells only, the impact of algae on symbiosis-dependent genes in both the ectodermal and the endodermal layer indicates that photosynthetic products can be transported across these two tissue layers or some signals can be transduced by cell-cell communication.

![Figure 3.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig3-v2.jpg)

**Figure 3.:** (A-F); Whole mount in situ hybridization using antisense (A–C) and sense probes (D-F; negative controls) for glutamine synthetase-1 (GS-1; left), Spot 14 (center) and Na/Pi-transporter (NaPi; right). Inserts show cross sections of the polyp’s body. (G–I) Relative expression levels of whole animal (whole), isolated endoderm (End) and isolated ectoderm (Ect) tissue of Hv_Sym (green bars) and Hv_Apo (orange bars). For each biological replicate (n = 3) 10–20 hydra polyps were used for total RNA extraction of endodermal and ectodermal tissue. T-test was performed between Hv_Sym and Hv_apo. Pvalue, *<0.05, **<0.01. (J) Expression change of genes GS-1, Spot14, NaPi, Sym-1 and Sym-2 following exposure to 25, 50 and 100 mM maltose in Hv_Apo. For each biological replicate (n = 3) 50 hydra polyps were used for total RNA extraction The vertical axis shows log scale (log2) fold changes of relative expression level of maltose-treated over the untreated Hv_Apo control. T-test was performed between maltose-treated in each concentration and control (*: p value <0.05) and Kruskal-Wallis test (†: p value <0.05) in the series of 48 hr treatment were performed. Error bars indicate standard deviation.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Isolated endoderm (left) and isolated ectoderm (right). Scale bar, 1 mm. Expression levels of an endoderm-specific gene finalASM_15403 (B) and that of an ectoderm specific gene finalASM_344 (C) in whole hydra (Whole) and isolated endoderm (End) and ectoderm (Ect) were examined to confirm whether tissue isolation had performed properly. For each biological replicate (n = 3) 10–20 hydra polyps were used for total RNA extraction of endodermal and ectodermal tissue. Error bars indicate standard deviation.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Effects of growth in presence of maltose (A), glucose (B), sucrose (C) and galactose (D) on gene expression of GS-1, Spot14 and NaPi. Hv_Apo were cultured in medium containing 10, 25, 50 or 75 mM of each sugar for 48 hr, and 75 mM maltose (orange) and glucose (blue) for 6 hr (E). RNA was extracted from the polyps in the light condition. Expression difference of the genes was examined by qPCR. For each biological replicate (n = 3) 50 hydra polyps were used for total RNA extraction. The vertical axis is log scale (log2) fold change of relative expression level of sugar-treated hydras over controls. T-test (*: p-value<0.05) in each concentration and Kruskal-Wallis test (†: pvalue <0.05) in the series of 48 hr treatment were performed. Error bars indicate standard deviation.

To more closely dissect the nature of the functional interaction between Hydra and Chlorella and to explore the possibility that maltose released from the algae is involved in A99-specific gene regulation, we cultured aposymbiotic polyps (Hv_Apo) for 2 days in medium containing various concentrations of maltose (Figure 3J). Of the five A99 specific genes, GS-1 and the Spot14 gene were up-regulated by maltose in a dose-dependent manner; the Na/Pi gene was only up-regulated in 100 mM maltose and the Hydra specific genes Sym-1 and Sym-2 did not show significant changes in expression by exposure to maltose (Figure 3J). This provides strong support for previous views that maltose excretion by symbiotic algae contributes to the stabilization of this symbiotic association (Cernichiari et al., 1969). When polyps were exposed to glucose instead of maltose, the genes of interest were also transcriptionally activated in a dose-dependent manner, while sucrose had no effect (Figure 3—figure supplement 2A–D). Exposure to low concentrations of galactose increased transcriptional activity but at high concentration it did not, indicating a substrate inhibitor effect for this sugar. That the response to glucose is similar or even higher compared to maltose after 6 hr of treatment (Figure 3—figure supplement 2E), suggests that Hydra cells transform maltose to glucose as a source of energy. In animals including cnidarians, several glucose transporters have been identified (Sproles et al., 2018), but yet no maltose transporters. This is consistent with the view that maltose produced by the symbiont is digested to glucose in the symbiosome and translocated to the host cytoplasm through glucose transporters.

### The Chlorella A99 genome records a symbiotic life style

To better understand the symbiosis between H. viridissima and Chlorella and to refine our knowledge of the functions that are required in this symbiosis, we sequenced the genome of Chlorella sp. strain A99 and compared it to the genomes of other green algae. The genome of Chlorella sp. A99 was sequenced to approximately 211-fold coverage, enabling the generation of an assembly comprising a total of 40.9 Mbp (82 scaffolds, N50 = 1.7 Mbp) (Table 5). Chlorella sp. A99 belongs to the family Chlorellaceae (Figure 4A) and of the green algae whose genomes have been sequenced it is most closely related to Chlorella variabilis NC64A (NC64A) (Merchant et al., 2007; Palenik et al., 2007; Worden et al., 2009; Blanc et al., 2010; Prochnik et al., 2010; Blanc et al., 2012; Gao et al., 2014; Pombert et al., 2014). The genome size of the total assembly in strain A99 was similar to that of strain NC64A (46.2 Mb) (Figure 4B). By k-mer analysis (k-mer = 19), the genome size of A99 was estimated to be 61 Mbp (Marçais and Kingsford, 2011). Its GC content of 68%, is the highest among the green algae species recorded (Figure 4B). In the A99 genome, 8298 gene models were predicted. As shown in Figure 4C, about 80% of these predicted genes have extensive sequence similarity to plant genes, while 13% so far have no similarity to genes of any other organisms (Figure 4C). It is also noteworthy that 7% of the A99 genes are similar to genes of other kingdoms but not to Hydra, indicating the absence of gene transfer from Hydra to the symbiont genome (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig4-v2.jpg)

**Figure 4.:** (A) Phylogenetic tree of eight genome sequenced chlorophyte green algae including Chlorella sp. A99. The NJ tree is based on sequences of the 18S rRNA gene, ITS1, 5.8S rRNA gene, ITS2 and 28S rRNA gene. (B) Genomic features and taxonomy of the sequenced chlorophyte green algae. Hel: Helicosporidium sp. ATCC50920. (C) The proportion of similarity of Chlorella A99 gene models to those of other organisms.

**Table 5.**
 Summary of sequence data for assembling Chlorella sp. A99 genome sequences


<table>
  <tbody>
    <tr>
      <td>Number of reads</td>
      <td colspan="2">85469010</td>
    </tr>
    <tr>
      <td>Number of reads assembled</td>
      <td colspan="2">61838513</td>
    </tr>
  </tbody>
</table>

### The Chlorella A99 genome provides evidences for extensive nitrogenous amino acid import and an incomplete nitrate assimilation pathway

Several independent lines of evidence demonstrate that nitrogen limitation and amino-acid metabolism have a key role in the Chlorella–Hydra symbiosis and that symbiotic Chlorella A99 depends on glutamine provided by its host (Rees, 1986; McAuley, 1987a; 1987b; McAuley, 1991; Rees, 1991;1989). To identify Chlorella candidate factors for the development and maintenance of the symbiotic life style, we therefore used the available genome information to assess genes potentially involved in amino acid transport and the nitrogen metabolic pathway.

When performing a search for the Pfam domain ‘Aa_trans’ or ‘AA_permease’ to find amino acid transporter genes in the A99 genome, we discovered numerous genes containing the Aa_trans domain (Table 6A). In particular, A99 contains many orthologous genes of amino acid permease 2 and of transmembrane amino acid transporter family protein (solute carrier family 38, sodium-coupled neutral amino acid transporter), as well as NC64A (Table 6B, Supplementary file 2). Both of these gene products are known to transport neutral amino acids including glutamine. This observation is supporting the view that import of amino acids is an essential feature for the symbiotic way of life of Chlorella.

**Table 6.**
 Amino acid transporter genes in Chlorella sp. A99 (A99), Chlorella variabilis NC64A (NC64A), Coccomyxa subellipsoidea C-169 (C169), Volvox carteri (Vc), Micromonas pusilla (Mp) and Ostreococcus tauri (Ot) and Chlamydomonas reinhardtii (Cr)


<table>
  <tbody>
    <tr>
      <td colspan="8">A. The number of Pfam domains related to amino acids transport</td>
    </tr>
    <tr>
      <td>Pfam domain name</td>
      <td>A99</td>
      <td>NC64A</td>
      <td>c169</td>
      <td>Cr</td>
      <td>Vc</td>
      <td>Mp</td>
      <td>Ot</td>
    </tr>
    <tr>
      <td>Aa_trans</td>
      <td>30</td>
      <td>38</td>
      <td>21</td>
      <td>9</td>
      <td>7</td>
      <td>9</td>
      <td>8</td>
    </tr>
    <tr>
      <td>AA_permease</td>
      <td>4</td>
      <td>6</td>
      <td>15</td>
      <td>5</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td colspan="8">B. Ortholog groups including Aa_trans domain containing genes overrepresented in symbiotic Chlorella</td>
    </tr>
    <tr>
      <td>Ortholog group ID: Gene annotation</td>
      <td>A99</td>
      <td>NC64A</td>
      <td>c169</td>
      <td>Cr</td>
      <td>Vc</td>
      <td>Mp</td>
      <td>Ot</td>
    </tr>
    <tr>
      <td>OG0000040: amino acid permease 2</td>
      <td>12</td>
      <td>12</td>
      <td>6</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>OG0000324: transmembrane amino acid transporter family protein (solute carrier family 38, sodium-coupled neutral amino acid transporter)</td>
      <td>6</td>
      <td>7</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

In symbiotic organisms, loss of genes often occurs due to the strictly interdependent relationship (Ochman and Moran, 2001; Wernegreen, 2012), raising the possibility that Chlorella A99 might have lost some essential genes. To test this hypothesis, we searched the Chlorella A99 genome for genes conserved across free-living green algae Coccomyxa subellipsoidea C169 (C169), Chlamydomonas reinhardtii (Cr) and Volvox carteri (Vc). In a total of 9851 C169 genes, we found 5701 genes to be conserved in Cr and Vc (Supplementary file 3). Of these, 238 genes did not match to any gene models and genomic regions in Chlorella A99 and thus were considered as gene loss candidates. Interestingly, within these 238 candidates, genes with the GO terms ‘transport’ in biological process and ‘transporter activity’ in molecular function were overrepresented (Figure 5). In particular, the 28 genes annotated to these GO terms encoded nitrate transporter, urea transporter and molybdate transporter, which are known to be involved in nitrogen metabolism (Table 7). Beside ammonium, nitrate and urea are major nitrogen sources for plants, whereas molybdate is a co-factor of the nitrate reductase, an important enzyme in the nitrate assimilation pathway. These transporter genes are conserved across green algae including Chlorella NC64A (Sanz-Luque et al., 2015; Gao et al., 2014) and appear to be lost in the Chlorella A99 genome.

![Figure 5.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig5-v2.jpg)

**Figure 5.:** Functional categorization of genes present in Coccomyxa subellipsoidea C169 (A, C) and genes missing in Chlorella A99 (B, D) by GO terms using Bast2GO. Multilevel pie charts show enrichment of GO’ Biological Process’ terms (A, B) and GO ‘Molecular Function’ terms (C, D) on the lowest level, which cover at least 10% of the total amount of annotated sequences.

**Table 7.**
 List of Coccomyxa subellipsoidea C169 (C169) genes, which are present in Chlamydomonas reinhardtii and Volvox carteri, but missing in the genome of Chlorella A99


<table>
  <thead>
    <tr>
      <th>UniProt ID in C169</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>F1DPL8_9CHLO</td>
      <td>ATP synthase F0 subunit 6 (mitochondrion)</td>
    </tr>
    <tr>
      <td>F1DPL7_9CHLO</td>
      <td>cytochrome c oxidase subunit 3 (mitochondrion)</td>
    </tr>
    <tr>
      <td>I0YZU4_9CHLO</td>
      <td>equilibrative nucleoside transporter 1</td>
    </tr>
    <tr>
      <td>I0Z311_9CHLO</td>
      <td>equilibrative nucleoside transporter family</td>
    </tr>
    <tr>
      <td>I0YZC9_9CHLO</td>
      <td>high affinity nitrate transporter</td>
    </tr>
    <tr>
      <td>I0Z2L2_9CHLO</td>
      <td>hypothetical protein COCSUDRAFT_28432</td>
    </tr>
    <tr>
      <td>I0YJ99_9CHLO</td>
      <td>hypothetical protein COCSUDRAFT_34498</td>
    </tr>
    <tr>
      <td>I0YKQ1_9CHLO</td>
      <td>hypothetical protein COCSUDRAFT_45098</td>
    </tr>
    <tr>
      <td>I0YYD3_9CHLO</td>
      <td>hypothetical protein COCSUDRAFT_65897</td>
    </tr>
    <tr>
      <td>I0YYP5_9CHLO</td>
      <td>importin-4 isoform X1</td>
    </tr>
    <tr>
      <td>I0YQQ1_9CHLO</td>
      <td>low-CO2-inducible membrane</td>
    </tr>
    <tr>
      <td>I0YJD4_9CHLO</td>
      <td>MFS transporter</td>
    </tr>
    <tr>
      <td>I0YTY0_9CHLO</td>
      <td>molybdate transporter 2</td>
    </tr>
    <tr>
      <td>F1DPM0_9CHLO</td>
      <td>NADH dehydrogenase subunit 3 (mitochondrion)</td>
    </tr>
    <tr>
      <td>F1DPM4_9CHLO</td>
      <td>NADH dehydrogenase subunit 6 (mitochondrion)</td>
    </tr>
    <tr>
      <td>F1DPM8_9CHLO</td>
      <td>NADH dehydrogenase subunit 9 (mitochondrion)</td>
    </tr>
    <tr>
      <td>I0Z357_9CHLO</td>
      <td>plasma membrane phosphate transporter Pho87</td>
    </tr>
    <tr>
      <td>I0Z9Y1_9CHLO</td>
      <td>pre translocase subunit</td>
    </tr>
    <tr>
      <td>I0YPT2_9CHLO</td>
      <td>transcription and mRNA export factor ENY2-like</td>
    </tr>
    <tr>
      <td>I0Z976_9CHLO</td>
      <td>transport SEC23</td>
    </tr>
    <tr>
      <td>I0Z3Q6_9CHLO</td>
      <td>tyrosine-specific transport -like isoform X1</td>
    </tr>
    <tr>
      <td>I0YXU9_9CHLO</td>
      <td>urea active transporter</td>
    </tr>
    <tr>
      <td>I0YRT0_9CHLO</td>
      <td>urea active transporter</td>
    </tr>
    <tr>
      <td>I0YRL4_9CHLO</td>
      <td>urea-proton symporter DUR3</td>
    </tr>
    <tr>
      <td>I0YUF9_9CHLO</td>
      <td>urea-proton symporter DUR3</td>
    </tr>
    <tr>
      <td>I0YJS6_9CHLO</td>
      <td>urea-proton symporter DUR3</td>
    </tr>
    <tr>
      <td>I0YQ78_9CHLO</td>
      <td>urea-proton symporter DUR3-like</td>
    </tr>
    <tr>
      <td>I0YIH7_9CHLO</td>
      <td>Zip-domain-containing protein</td>
    </tr>
  </tbody>
</table>

In nitrogen assimilation processes, plants usually take up nitrogen in the form of nitrate (NO3-) via nitrate transporters (NRTs) or as ammonium (NH4+) via ammonium transporters (AMT) (Figure 6A). In higher plants, two types of nitrate transporters, NRT1 and NRT2, have been identified (Krapp et al., 2014). Some NRT2 require nitrate assimilation-related component 2 (NAR2) to be functional (Quesada et al., 1994). NO3- is reduced to nitrite by nitrate reductase (NR), NO2- is transported to the chloroplast by nitrate assimilation-related component1 (NAR1), and NO2- is reduced to NH4+ by nitrite reductase (NiR). NH4+ is incorporated into glutamine (Gln) by glutamine synthetase (GS), and Gln is incorporated into glutamate (Glu) by NADH-dependent glutamine amide-2-oxoglutarate aminotransferase (GOGAT), also known as glutamate synthase. This pathway is highly conserved among plants and all of its major components, including NRT1 and NRT2, NAR1 and NAR2, NR, NiR, AMT, GOGAT and GS, are present in the 10 green algae species that have been genome-sequenced so far (with the exception of NRT1, which is absent in Micromonas pusilla) (Sanz-Luque et al., 2015). In Symbiodinium, the photosynthetic symbiont of marine invertebrates, all these components of the nitrogen assimilation pathway were also observed (Supplementary file 4) (Shoguchi et al., 2013; Lin et al., 2015; Aranda et al., 2016; Sproles et al., 2018).

![Figure 6.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig6-v2.jpg)

**Figure 6.:** (A) Schematic diagram of the nitrogen assimilation pathway in plants showing the function of nitrate transporters NRT1 (peptides/nitrate transporter) and NRT2 (nitrate/nitrite transporter), nitrate assimilation-related components NAR1 and NAR2, nitrate reductase NR, nitrite reductase NiR, ammonium transporter AMT, glutamate synthetase GOGAT and glutamine synthetase GS. Genes shown in red boxes (NRT2, NAR2 and NiR) were not found in the Chlorella sp. A99 genome. (B) Table showing the number of nitrogen assimilation genes in Chlorella sp. A99 (A99), Chlorella variabilis NC64A (NC64A), Coccomyxa subellipsoidea C169 (C169), Volvox carteri f. nagariensis (Vc), Chlamydomonas reinhardtii (Cr), Ostreococcus tauri (Ot) and Micromonas pusilla (Mp). (C) Gene clusters of nitrate assimilation genes around the shared NR genes (blue) in the genomes of NC64A, C169 and A99. Red boxes show nitrate assimilation genes absent in A99 and gray boxes depict other genes. Numbers below the boxes are JGI protein IDs of NC64A and C169. Numbers below the genes of A99 are JGI protein IDs of the best hit genes in NC64A and C169 and their gene name.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** PCR amplification of genomic DNA corresponding to the genes NRT2, NiR and NR (positive control) was performed in Chlorella sp. A99 (A99), Chlorella variabilis NC64A (NC64A), Coccomyxa subellipsoidea C169 (C169) and Chlamydomonas reinhardtii (Cr).

Based on the annotation by Sanz-Luque et al. (Sanz-Luque et al., 2015), we searched these nitrogen assimilation genes in the Chlorella A99 genome, using ortholog grouping and a reciprocal BLAST search using the protein sequences from other green algae (Figure 6B, Supplementary file 5). As expected, the Chlorella A99 genome contains many homologues of the genes involved in nitrogen assimilation in plants including genes encoding NRT1, NAR1, NR, AMT, GS and GOGAT (Figure 6B). Intriguingly, our systematic searches failed to identify representative genes for NRT2, NAR2 and NiR in the Chlorella A99 genome (Figure 6B). We confirmed the absence of the NRT2 and NiR genes by PCR using primers designed for the conserved regions of these genes and which failed to produce a product with genomic DNA as a template (Figure 6—figure supplement 1). Due to the weak sequence conservation of the NAR2 gene in the three algae genomes, PCR of that gene was not performed. Taken together, our observations indicate that Chlorella A99 algae appears to lack NRT2, NAR2 and NiR.

Since in many fungi, cyanobacteria and algae species, nitrate assimilation genes are known to act in concert and a gene cluster of NR and NiR genes is conserved between different green algae (Sanz-Luque et al., 2015), we next investigated the level of genomic clustering of the nitrate assimilation pathway genes in the Chlorella genome. Comparing the genomes of NC64A and C169 revealed the presence of a cluster of NR and NiR genes (Figure 6C). In NC64A, two NRT2 genes, together with genes for NAR2, NR and NiR are clustered on scaffold 21. In C169, one of the NR genes and NiR are clustered together, whereas the second NR gene is separate. Interestingly, analysis of the sequences around the NR gene in the Chlorella A99 genome provided no evidence for the presence of a co-localized NiR gene or any other nitrate assimilation genes, nor any conserved gene synteny to NC64A and C169 (Figure 6C). Therefore, our comparative genomic analyses points to an incomplete and scattered nitrogen metabolic pathway in symbiotic Chlorella A99, which lacks essential transporters and enzymes for nitrate assimilation as well as the clustered structure of nitrate assimilation genes.

### Supplementing the medium with glutamine allows temporary in vitro growth of symbiotic Chlorella A99

The absence of genes essential for nitrate assimilation in the Chlorella A99 genome (Figure 6) is consistent with its inability to grow outside the Hydra host cell (Habetha and Bosch, 2005) and indicates that Chlorella symbionts are dependent on metabolites provided by their host. We hypothesized that Chlorella is unable to use nitrite and ammonium as a nitrogen source, and that it relies on Hydra assimilating ammonium to glutamine to serve as the nitrogen source. To test this hypothesis and to examine utilization of nitrogen compounds of A99, we isolated Chlorella A99 from Hv_Sym and cultivated it in vitro using modified bold basal medium (BBM) (Nichols and Bold, 1965) containing the same amount of nitrogen in the form of NO3-, NH4+, Gln or casamino acids (Figure 7). As controls, Chlorella variabilis NC64A (NC64A) isolated from Hv_NC64A and free-living C169 were used. To confirm that the cultured A99 is not contamination, we amplified and sequenced the genomic region of the 18S rRNA gene by PCR (Figure 7—figure supplement 1) and checked this against the genomic sequence of A99. Kamako et al. reported that free-living alga Chlorella vulgaris Beijerinck var. vulgaris grow in media containing only inorganic nitrogen compounds as well as in media containing casamino acids as a nitrogen source, while NC64A required amino acids for growth (Kamako et al., 2005). Consistent with these observations, C169 grew in all tested media and NC64A grew in media containing casamino acids and Gln, although its growth rate was quite low in presence of NH4+ and NO3- (Figure 7). Remarkably, Chlorella A99 increased in cell number for up to 8 days in media containing casamino acids and Gln (Figure 7). Similar to NC64A, A99 did not grow in presence of NH4+ and NO3-. The growth rates of both A99 and NC64A were higher in medium containing a mixture of amino acids (casamino acids) than the single amino acid Gln. In contrast to NC64A, A99 could not be cultivated permanently in casamino acids or glutamine supplemented medium, indicating that additional growth factors are necessary to maintain in vitro growth of this obligate symbiont. Thus, although in vitro growth of A99 can be promoted by adding Glu and amino acids to the medium, A99 cannot be cultured permanently in this enriched medium, indicating that other host derived factors remain to be uncovered.

![Figure 7.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig7-v2.jpg)

**Figure 7.:** The growth rate of Chlorella A99 (A99), Chlorella variabilis NC64A (NC64A) and Coccomyxa subellipsoidea C-169 (C169) by in vitro culture was assessed for different nitrogen sources with casamino acids (blue), glutamine (orange), ammonium (gray) and nitrate (yellow). Mean number of algae per ml were determined at 4, 8, 12 days after inoculation with 106 cell/ml. Error bars indicate standard deviation.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** PCR amplification of genomic DNA of the 18S rRNA gene was performed in Chlorella A99 shortly after isolation from H. viridissima A99 (Isolated A99), cultured in medium containing glutamine (Glu) and in medium with casamino acids for 12 days, with cultured NC64A and C169 added for comparison.

## Discussion

### Metabolic co-dependence in Hydra-Chlorella symbiosis

Sequencing of the Chlorella A99 genome in combination with the transcriptome analyses of symbiotic, aposymbiotic and NC64A-infected H. viridissima polyps has enabled the identification of genes with specific functions in this symbiotic partnership. The Hydra-Chlorella symbiosis links carbohydrate supply from the photosynthetic symbiont to glutamine synthesis by the host. Characteristics of the symbiont genome obviously reflect its adaptation to this way of life, including an increase in amino acid transporters and degeneration of the nitrate assimilation pathway. This conclusion is based on six observations: (i) Expression of some genes including GS-1, Spot 14 and NaPi is specifically up-regulated in the presence of Chlorella A99 (Figure 1C, Table 2), and (ii) they are induced by both, photosynthetic activity of Chlorella and by supplying exogenous maltose or glucose (Figures 2 and 3J, Figure 3—figure supplement 2). Maltose produced by the symbiont is likely to be digested to glucose in symbiosome and translocated to the host cytoplasm through glucose transporters (Figure 8A). Upregulation of a GLUT8 gene in the symbiotic state of green hydra may reflect activation of sugar transport (Table 1). These results indicate that maltose release by photosynthesis of the symbiont enhances nutrition supply including glutamine by the host (Figure 8A). (iii) Symbiotic Chlorella A99 cannot be cultivated in vitro in medium containing a single inorganic nitrogen source (Figure 7). Since medium containing glutamine supports in vitro growth of A99, this organism appears to depend on glutamine provided by the Hydra host. (iv) The genome of Chlorella A99 contains multiple amino acid transporter genes (Table 6), but lacks genes involved in nitrate assimilation (Figure 6), pointing to amino acids as main source of nitrogen and a degenerated nitrate assimilation pathway. As for ammonium, which is one of the main nitrogen sources in plants, previous studies have reported the inability of symbiotic algae to take up ammonium because of the low peri-algal pH (pH 4–5) that stimulates maltose release (Douglas and Smith, 1984; Rees, 1989; McAuley, 1991; Dorling et al., 1997). Since Chlorella apparently cannot use nitrite and ammonium as a nitrogen source, it seems that Hydra has to assimilate ammonium to glutamine and provides it to Chlorella A99 (Figure 8A).

![Figure 8.](https://cdn.elifesciences.org/articles/35122/elife-35122-fig8-v2.jpg)

**Figure 8.:** (A) Summary of symbiotic interactions between Hydra and Chlorella A99. During light conditions, Chlorella A99 performs photosynthesis and produces maltose (Mal), which is secreted into the Hydra symbiosome where it is possibly digested to glucose (Gluc), shown in red. The sugar induces expression of Hydra genes encoding glutamine synthetase (GS), Na/Pi transporter (NaPi) and Spot14. GS catalyzes the condensation of glutamate (Glu) and ammonium (NH4+) to form glutamine (Gln), which is used by Chlorella as a nitrogen source. Since the sugar also up-regulates the NaPi gene, which controls intracellular phosphate levels, it might be involved in the supply of phosphorus to Chlorella as well (blue broken line). The sugar is transported to the ectoderm (red broken line) and there induces the expression of GS and Spot14. In the Chlorella A99 genome, degeneration of the nitrate assimilation system and an increase of amino acid transporters was observed (green balloon). (B, C) Comparison between Hydra-Chlorella symbiosis and coral-Symbiodinium symbiosis. Red indicates transfer of photosynthesis products from the symbiont to the host, and blue indicates transfer of nitrogen sources from the host to the symbiont. While the host organisms Hydra and coral can assimilate NH4+ to Gln (B, C), assimilation of inorganic nitrogen by Symbiodinidium plays an important role for the symbiotic system in coral (C).

(v) While polyps with native symbiont Chlorella A99 grew faster than aposymbiotic ones, symbiosis with foreign algae NC64A had no effect on the growth of polyps at all (Figure 1B). (vi) Hydra endodermal epithelial cells host significantly fewer NC64A algae than A99 (Figure 1—figure supplement 1) providing additional support for the view of a tightly regulated codependent partnership in which exchange of nutrients appears to be the primary driving force. Previous studies have reported that symbiotic Chlorella in green hydra releases significantly larger amounts of maltose than NC64A (Mews and Smith, 1982; Rees, 1989). In addition, Rees reported that Hydra polyps containing high maltose releasing algae had a high GS activity, whereas aposymbiotic Hydra or Hydra with a low maltose releasing algae had lower GS activity (Rees, 1986). Although the underlying mechanism of how maltose secretion and transportation from Chlorella is regulated is still unclear, the amount of maltose released by the symbiont could be an important symbiont-derived driver or stabilizer of the Hydra–Chlorella symbiosis.

### More general lessons for animal-algal symbiosis

Transcriptome comparison between symbiotic and aposymbiotic H. viridissima demonstrated that symbiosis-regulated genes are involved in oxidative stress response and innate immunity. The fact that PRRs and apoptosis-related genes, are also differentially expressed in a number of other symbiotic cnidarians (Table 1), suggests innate immunity as conserved mechanism involved in controlling the development and maintenance of stable symbiotic interactions. Furthermore, the exchange of nitrogenous compounds and photosynthetic products between host and symbiont observed here in the Hydra-Chlorella symbiosis is also observed in marine invertebrates such as corals, sea anemones and giant clams associated with Symbiodinium algae (Figure 8B,C). Despite these similarities, however, there are also conspicuous differences among symbiotic cnidarians in particular with respect to the nutrients provided by the symbiont to the host. For example, symbiotic Chlorella algae in green hydra, Paramecium and fresh water sponges provide their photosynthetic products in form of maltose and glucose (Figure 8B) (Brown and Nielsen, 1974; Wilkinson, 1980; Kamako and Imamura, 2006). In contrast, Symbiodinium provides glucose, glycerol, organic acids, amino acids as well as lipids to its marine hosts (Figure 8C) (Muscatine and Cernichiari, 1969; Lewis and Smith, 1971; Trench, 1971; Kellogg and Patton, 1983). A former transcriptome analysis of amino acid biosynthetic pathways suggested that Symbiodinium can synthesize almost all amino acids (Shinzato et al., 2014). Gene loss in cysteine synthesis pathway in the coral host Acropora digitifera seems to reflect the dependency on the amino acids provided by the Symbiodinium symbiont (Shinzato et al., 2011). In contrast to Symbiodinium which can assimilate inorganic nitrogen such as nitrate and ammonium (Lipschultz and Cook, 2002; Grover et al., 2003; Tanaka et al., 2006; Yellowlees et al., 2008), the symbiotic Chlorella algae in Hydra and Paramecium can only use amino acids as a nitrogen source (Figure 6) (Kamako et al., 2005).

In efforts to explain the metabolic efficiency of nitrogen use in symbiotic organisms, two models have been proposed: the ‘nitrogen conservation’ and the ‘nitrogen recycling’ hypothesis. The nitrogen conservation hypothesis suggests that photosynthetic carbon compounds from the symbiont are used preferentially by the host respiration, which reduces catabolism of nitrogenous compounds (Rees and Ellard, 1989; Szmant et al., 1990; Wang and Douglas, 1998). The ‘nitrogen recycling’ hypothesis suggests that symbionts assimilate nitrogenous waste (ammonium) of the host into valuable, organic compounds, which then are translocated back to the host (Figure 8C Symbiont nitrogen assimilation) (Lewis and Smith, 1971; Muscatine and Porter, 1977; Falkowski et al., 1993; Wang and Douglas, 1998). Our observation that in symbiotic green hydra many genes involved in amino acid metabolism are down-regulated (Figure 1E) is consistent with the assumption of reduction of amino acid consumption by respiration.

In addition to the nitrogen recycling hypothesis, it has been proposed that also corals, sea anemones, Paramecium and green hydra hosts can assimilate ammonium into amino acids (Figure 8B,C Host nitrogen assimilation) (Miller and Yellowlees, 1989; Rees, 1989; Szmant et al., 1990; Rees, 1991; Wang and Douglas, 1998; Lipschultz and Cook, 2002). Ammonia assimilation by the host implies that the host controls the nitrogen status to regulate metabolism of the symbionts, which may be involved in controlling the number of symbionts within the host cell. For organisms such as corals living in oligotrophic sea, inorganic nitrogen assimilation and recycling may be necessary to manage the nitrogen sources efficiently. In contrast, for Hydra and Paramecium living in a relatively nutrient-rich environment may be advantageous in terms of metabolic efficiency that the symbiont abandons its ability to assimilate inorganic nitrogen and specializes in the supply of photosynthetic carbohydrate to the host.

### Genome evolution in symbiotic Chlorella sp. A99

Metabolic dependence of symbionts on host supply occasionally results in genome reduction and gene loss. For example, symbiotic Buchnera bacteria in insects are missing particular genes in essential amino acid pathways (Shigenobu et al., 2000; Hansen and Moran, 2011). The fact that the corresponding genes of the host are up-regulated in the bacteriocyte, indicates complementarity and syntrophy between host and symbiont. Similarly, in Chlorella A99 the nitrogen assimilation system could have been lost as a result of continuous supply of nitrogenous amino acids provided by Hydra.

Compared to Chlorella NC64A, the closest relative to Chlorella A99 among the genome-sequenced algae, genome size and total number of genes in Chlorella A99 were found to be smaller (Figure 4B). Although both A99 and NC64A cannot be cultivated using inorganic nitrogen sources (Figure 7) (Kamako et al., 2005), NC64A, unlike A99, obtains all major nitrogen assimilation genes and their cluster structure on the chromosome (Figure 6) (Sanz-Luque et al., 2015). NR and NiR activities were found to be induced by nitrate in free-living Chlorella, but not in Chlorella NC64A, indicating mutations in the regulatory region (Kamako et al., 2005). Considering the phylogenetic position of NC64A and the symbiotic Chlorella of green hydra (Kawaida et al., 2013), the disability of nitrate assimilation in A99 and NC64A seems to have evolved independently, suggesting convergent evolution in a similar symbiotic environment.

Although our findings indicate that genome reduction in Chlorella A99 is more advanced than in Chlorella NC64A, genome size and total number of genes do not differ much between the Trebouxiophyceae (A99, NC64A and C169) (Figure 4B). By contrast, the parasitic algae Helicosporidium and Auxochlorella have significantly smaller genome sizes and number of genes indicating extensive genome reduction (Gao et al., 2014; Pombert et al., 2014). The apparently unchanged complexity of the Chlorella A99 genome suggests a relatively early stage of this symbiotic partnership. Thus, gene loss in metabolic pathways could occur as a first step of genome reduction in symbionts caused by the adaptation to continuous nutrient supply from the host. Taken together, our study suggests metabolic-codependency as the primary driving force in the evolution of symbiosis between Hydra and Chlorella.

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
      <td>Strain, strain background (Hydra viridissima A99)</td>
      <td>Hydra viridissima A99</td>
      <td>PMID: 16351895</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Chlorella sp. A99)</td>
      <td>Chlorella sp. A99</td>
      <td>PMID: 16351895</td>
      <td>NCBI BioProject ID: PRJNA412448</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Chlorella variabilis NC64A)</td>
      <td>Chlorella variabilis NC64A</td>
      <td>Microbial Culture Collection at the National Institute for Environmental Studies</td>
      <td>NIES-2541</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Coccomyxa subellipsoidea C-169)</td>
      <td>Coccomyxa subellipsoidea C-169</td>
      <td>Microbial Culture Collection at the National Institute for Environmental Studies</td>
      <td>NIES-2166</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Chlamydomonas reinhardtii)</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Microbial Culture Collection at the National Institute for Environmental Studies</td>
      <td>NIES-2235</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TruSeq DNA LT Sample Prep Kit</td>
      <td>Illumina</td>
      <td>FC-121–2001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Nextera Mate Pair Sample Preparation Kit</td>
      <td>Illumina</td>
      <td>FC-132–1001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Miseq reagent kit v3</td>
      <td>Illumina</td>
      <td>MS-102–3003</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>HiSeq SBS kit v4</td>
      <td>Illumina</td>
      <td>FC-401–4003</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>BigDye Terminator v3.1 Cycle Sequencing Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>4337454</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>4 × 44K Hydra viridissima A99 Custom-Made Microarray</td>
      <td>Agilent Technologies</td>
      <td>NCBI GEO Platform ID: GPL23280</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GE Hybridization Kit and GE Wash Pack</td>
      <td>Agilent Technologies</td>
      <td>5188–5242, 5188–5327</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>High Sensitivity DNA Kit</td>
      <td>Agilent Technologies</td>
      <td>5067–4626</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNA6000 nano kit</td>
      <td>Agilent Technologies</td>
      <td>5067–1511</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Low Input Quick Amp Labeling Kit</td>
      <td>Agilent Technologies</td>
      <td>5190–2305</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PureLink RNA Mini Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>12183018A</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Fermentas First Strand cDNA Synthesis Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>K1621</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trizol reagent</td>
      <td>Thermo Fisher Scientific</td>
      <td>15596026</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>AmpliTaq Gold 360 Master Mix</td>
      <td>Thermo Fisher Scientific</td>
      <td>4398901</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ISOPLANT II</td>
      <td>Nippon Gene</td>
      <td>316–04153</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GoTaq qPCR Master Mix</td>
      <td>Promega</td>
      <td>A6002</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KOD FX Neo</td>
      <td>TOYOBO</td>
      <td>KFX-201</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Feature Extraction Software</td>
      <td>Agilent Technologies</td>
      <td>RRID:SCR_014963</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Newbler</td>
      <td>454 Life Sciences, Roche Diagnostics</td>
      <td>RRID:SCR_011916</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SSPACE</td>
      <td>PMID: 21149342</td>
      <td>RRID:SCR_005056</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GapCloser</td>
      <td>PMID: 23587118</td>
      <td>RRID:SCR_015026</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NCBI BLAST</td>
      <td>PMID: 2231712</td>
      <td>RRID:SCR_004870</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CEGMA</td>
      <td>PMID: 17332020</td>
      <td>RRID:SCR_015055</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Augustus: Gene Prediction</td>
      <td>PMID: 16845043</td>
      <td>RRID:SCR_008417</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Blast2GO</td>
      <td>PMID: 16081474</td>
      <td>RRID:SCR_005828</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Hmmer</td>
      <td>PMID: 9918945</td>
      <td>RRID:SCR_005305</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CLUSTALX2</td>
      <td>PMID: 17846036</td>
      <td>RRID:SCR_002909</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BioEdit</td>
      <td>Nucleic Acid Symposium Series 41, 95–98</td>
      <td>RRID:SCR_007361</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Njplot</td>
      <td>Biochimie 78, 364–369</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OrthoFinder</td>
      <td>PMID: 26243257</td>
      <td>NA</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Biological materials and procedures

Experiments were carried out with the Australian Hydra viridissima strain A99, which was obtained from Dr. Richard Campbell, Irvine. Polyps were maintained at 18°C on a 12 hr light/dark cycle and fed with Artemia two or three times a week. Aposymbiotic (algae free) polyps were obtained by photobleaching using 5 μM DCMU (3-(3,4-dichlorophenyl)−1,1-dimethylurea) as described before (Pardy, 1976; Habetha et al., 2003). Experiments were carried out with polyps starved for 3–6 days. Isolation of endodermal layer and ectodermal layer was performed as described by Kishimoto et al. (Kishimoto et al., 1996). Symbiotic Chlorella were isolated as described before by Muscatine and McAuley (Muscatine, 1983; McAuley, 1986). Chlorella variabilis NC64A (NIES-2541), Coccomyxa subellipsoidea C-169 (NIES-2166) and Chlamydomonas reinhardtii (NIES-2235) were obtained from the Microbial Culture Collection at the National Institute for Environmental Studies (Tsukuba, Japan).

### Nucleic acid preparation

Total RNA of Hydra was extracted by use of the Trizol reagent and PureLink RNA Mini Kit (Thermo Fisher Scientific) after lysis and removal of algae by centrifugation. The genomic DNA of green algae was extracted using ISOPLANT II (Nippon Gene, Tokyo, Japan) following DNase I treatment to degrade contaminant DNA. Quantity and quality of DNA and RNA were checked by NanoDrop (Thermo Scientific Inc., Madison, USA) and BioAnalyzer (Agilent Technologies, Santa Clara, USA).

### Microarray analysis

Total RNA for synthesis of cRNA targets was extracted from about 100 green hydra for each experimental group. Experiments were carried out using three biological replicates. cRNA labeled with cyanine-3 were synthesized from 400 ng total Hydra RNA using a Low Input Quick Amp Labeling Kit for one color detection (Agilent Technologies). A set of fluorescently labeled cRNA targets was employed in a hybridization reaction with 4 × 44K Custom-Made Hydra viridissima Microarray (Agilent Technologies) contributing a total of 43,222 transcripts that was built by mRNA-seq data (NCBI GEO Platform ID: GPL23280) (Bosch et al., 2009). Hybridization and washing were performed using the GE Hybridization Kit and GE Wash Pack (Agilent Technologies) after which the arrays were scanned on an Agilent Technologies G2565BA microarray scanner system with SureScan technology following protocols according to the manufacturer's instructions. The intensity of probes was extracted from scanned microarray images using Feature Extraction 10.7 software (Agilent Technologies). All algorithms and parameters used in this analysis were used with default conditions. Background-subtracted signal-intensity values (gProcessedSignal) generated by the Feature Extraction software were normalized using the 75th percentile signal intensity among the microarray. Those genes differentially expressed between two samples were determined by average of fold change (cut of >2.0) and Student's t-test (p<0.1). The data series are accessible at NCBI GEO under accession number GSE97633.

### Quantitative real time RT-PCR

Total RNA was extracted from 50 green hydra polyps for each biological replicate independently. For reverse transcription of total RNA First Strand cDNA Synthesis Kit (Fermentas, Ontario, Canada) was used. Real-time PCR was performed using GoTaq qPCR Master Mix (Promega, Madison, USA) and ABI Prism 7300 (Applied Biosystems, Foster City, USA). All qPCR experiments were performed in duplicate with three biological replicates each. Values were normalized using the expression of the tubulin alpha gene. Primers used for these experiments are listed in Supplementary file 6A.

### Whole mount in situ hybridization

Expression patterns of specific Hydra genes were detected by whole mount in situ hybridization with digoxigenin (DIG)-labelled RNA probes. Specimens were fixed in 4% paraformaldehyde. Hybridization signal was visualized using anti-DIG antibodies conjugated to alkaline phosphatase and NBT/BCIP staining solution (Roche). DIG-labeled sense probes (targeting the same sequences as the antisense probes) were used as a control. Primers used for these experiments are listed in Supplementary file 6B.

### Genome sequencing and gene prediction

For genome sequencing of Chlorella sp. A99, Chlorella sp. A99 was isolated from H. viridissima A99 and genomic DNA was extracted. Paired-end library (insert size: 740 bp) and mate-pair libraries (insert size: 2.2 and 15.2 kb) were made using Illumina TruSeq DNA LT Sample Prep Kit and Nextera Mate Pair Sample Preparation Kit respectively (Illumina Inc., San Diego, USA), following the manufacturer's protocols. Genome sequencing was performed using Illumina Miseq and Hiseq 2000 platforms. Sequence reads were assembled using Newbler Assembler version 2.8 (Roche, Penzberg, Germany) and subsequent scaffolding was performed by SSPACE (Boetzer et al., 2011). Gaps inside the scaffolds were closed with the paired-end and mate-pair data using GapCloser of Short Oligonucleotide Analysis Package (Luo et al., 2012). To overcome potential assembly errors arising from tandem repeats, sequences that aligned to another sequence by more than 50% of the length using blastn (1e-50) were removed from the assembly. The completeness of the genome was evaluated using CEGMA v2.4 (Core Eukaryotic Genes Mapping Approach) based on mapping of the 248 most highly conserved core eukaryotic genes (CEGs) on the assembled genome (Parra et al., 2007). The completeness of complete and partial CEGs in the A99 scaffolds was 80 and 88%, respectively. The fraction of repetitive sequences was 12%. Gene model was predicted by AUGUSTUS 3.0.1 using model parameters for NC64A (Stanke et al., 2006). This Whole Genome Shotgun project has been deposited at DDBJ/ENA/GenBank under the accession PCFQ00000000 (BioProject ID: PRJNA412448). Genome sequences and gene models are also accessible at the website of OIST Marine Genomics Unit Genome Project (http://marinegenomics.oist.jp/chlorellaA99/viewer/info?project_id=65).

### Analysis of genes in Hydra viridissima and Chlorella

Annotation of transcriptome contigs and prediction of gene models was performed by use of BLAST, Gene Ontology (Ashburner et al., 2000) and blast2go (Conesa et al., 2005). To examine the conservation of H. viridissima contigs among metazoans, homology searches by blastx (evalue 1E-5) were performed using protein databases obtained from NCBI for Drosophila melanogaster and Homo sapiens, from the JGI genome portal (http://genome.jgi.doe.gov/) for Branchiostoma floridae, Nematostella vectensis, from Echinobase (http://www.echinobase.org/EchinoBase/) for Strongylocentrotus pupuratus, from Compagen for Hydra magnipapillata, and from the OIST marine genomics Genome browser ver.1.1 (http://marinegenomics.oist.jp/coral/viewer/info?project_id=3) for Acropora digitifera.

For comparative analysis of gene models of Chlorella sp. A99 and other algae, domain searches against the Pfam database (Pfam-A.hmm) were performed using HMMER (Eddy, 1998; Finn et al., 2016), and ortholog gene grouping was done using OrthoFinder (Emms and Kelly, 2015). The sequences of the reference genes and genomes were obtained from the database of the JGI genome portal for Chlorella variabilis NC64A, Coccomyxa subellipsoidea C-169, Volvox carteri, Micromonas pusilla, and Ostreococcus tauri, from NCBI for Auxenochlorella protothecoides 0710, from Phytozome (http://phytozome.jgi.doe.gov/pz/portal.html) for Chlamydomonas reinhardtii, from OIST Marine Genomics (http://marinegenomics.oist.jp/symb/viewer/info?project_id=21) for Symbiodinium minutum, Symbiodinium kawagutti genome, from Dinoflagellate Resources (http://web.malab.cn/symka_new/) for Symbiodinium kawagutti and Reefgenomics (http://reefgenomics.org/) for Symbiodinium microadriaticum) (Merchant et al., 2007; Palenik et al., 2007; Worden et al., 2009; Blanc et al., 2010; Prochnik et al., 2010; Blanc et al., 2012)

Nitrogen assimilation genes in Chlorella A99 were identified by orthologous gene groups and reciprocal blast searches. The number of genes for nitrate assimilation genes, glutamine synthetase and glutamate synthetase, and clustering of such genes were systematically reported by (Sanz-Luque et al., 2015). We used these data as reference for searches of nitrogen assimilation genes, and further nitrogen assimilation genes were searched by Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway (Kanehisa and Goto, 2000). JGI genome browsers of Chlorella variabilis NC64A and Coccomyxa subellipsoidea C-169 were also used for retrieving genes and checking gene order on the scaffolds.

### Phylogenetic analysis

For a phylogenetic tree of chlorophyte green algae, the sequences of 18S rRNA gene, ITS1, 5.8S rRNA gene, ITS2 and 28S rRNA gene were obtained from scaffold20 of Chlorella A99 genome sequence, and from NCBI nucleotide database entries for Chlorella variabilis NC64A (FM205849.1), Auxenochlorella protothecoides 0710 (NW_011934479.1), Coccomyxa subellipsoidea C169 (AGSI01000011.1), Volvox carteri f. nagariensis (NW_003307662.1), Chlamydomonas reinhardtii (FR865576.1), Ostreococcus tauri (GQ426340.1) and Micromonas pusilla (FN562452.1). Multiple alignments were produced with CLUSTALX (2.1) with gap trimming (Larkin et al., 2007). Sequences of poor quality that did not well align were deleted using BioEdit (Hall, 1999). Phylogenetic analyses were performed using the Neighbor-Joining method by CLUSTALX with the default parameters (1000 bootstrap tests and 111 seeds). Representative phylogenetic trees were drawn by using NJ plot (Perrière and Gouy, 1996).

### PCR amplification of nitrate assimilation genes in green algae

Primers were designed based on the conserved region of the NRT2 gene, NiR and NR genes (positive control) identified by comparison of genes from Chlorella variabilis NC64A (NC64A), Coccomyxa subellipsoidea C169 (C169), and Chlamydomonas reinhardtii (Cr) which belongs to Chlorophyceae class of green algae. Primers for NAR2 could not be designed because of insufficient conservation. As positive controls, amplicons were produced for NR of all the green algae examined and of NRT2 and NiR from NC64A, C169 and Cr, after which their sequences were checked. KOD FX Neo (TOYOBO, Tokyo, Japan) was used under the following conditions: an initial denaturation phase (94°C for 120 s) followed by 36 cycles of (98°C for 30 s, 69°C for 100 s) for NiR, (98°C for 30 s, 58°C for 30 s and 68°C for 210 s) for NRT2 and (98°C for 30 s, 59°C for 30 s and 68°C for 60 s) for NR. In each case, 10 ng gDNA was used as a template. The primers used are described in Supplementary file 6C. PCR products were sequenced to confirm amplification of the target genes using ABI PRISM 3100 Genetic Analyzer (Thermo Fisher Scientific Inc., Madison, USA) using BigDye Terminator v3.1 Cycle Sequencing Kit (Thermo Fisher Scientific).

### In vitro culture of algae

To isolate symbiotic algae, polyps were quickly homogenized in 0.25% sodium dodecyl sulfate (SDS) solution and centrifuged at 3000 g for 1 min. The pellet was resuspended in 0.05% SDS and centrifuged at 500 g for 5 min. Isolated A99, NC64A and C169 were washed by sterilized Bold Basal Medium (Bischoff and Bold, 1963) modified by the addition of 0.5% glucose, 1.2 mg/L vitamine B1 (Thiaminhydrochloride), 0.01 mg/L vitamine B12 (Cyanocobalamin) (Supplementary file 7) and incubated for two days in modified Bold Basal Medium with 50 mg/l ampicillin and streptomycin. The algae were cultivated in 5 ml of modified Bold Basal Medium (BBM) with the same amount of nitrogen (2.9 mM NaNO3, NH4Cl, glutamine or 426 mg/l casamino acids) and 5 mg/l Carbendazim (anti-fungal) with fluorescent illumination (12 hr light, 12 hr dark) at 20˚C. Mean numbers of algae per ml were calculated from three tubes enumerated at 4, 8, and 12 days after inoculation with 106 cell/sml using a hemocytometer. After cultivation, gDNA was isolated from the A99 cultured in Gln-containing BBM and casamino acid-containing BBM and A99 was isolated from green hydra directly. A partial genomic region of the 18S rRNA gene was amplified by PCR and sequenced to confirm absence of contamination by other algae. PCR was performed using AmpliTaq Gold (Thermo Fisher Scientific). Sequencing was performed as described above. The primers used are described in Supplementary file 6D.
