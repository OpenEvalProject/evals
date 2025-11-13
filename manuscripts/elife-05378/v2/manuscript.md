# Unprecedented genomic diversity of RNA viruses in arthropods reveals the ancestry of negative-sense RNA viruses

## Authors

- Ci-Xiu Li<sup>1</sup>
- Mang Shi<sup>1</sup>
- Jun-Hua Tian<sup>4</sup>
- Xian-Dan Lin<sup>5</sup>
- Yan-Jun Kang<sup>1</sup>
- Liang-Jun Chen<sup>1</sup>
- Xin-Cheng Qin<sup>1</sup>
- Jianguo Xu<sup>1</sup>
- Edward C Holmes<sup>1</sup>
- Yong-Zhen Zhang<sup>1</sup> †

### Affiliations

1. State Key Laboratory for Infectious Disease Prevention and Control National Institute for Communicable Disease Control and Prevention, Chinese Center for Disease Control and Prevention Beijing China
2. Collaborative Innovation Center for Diagnosis and Treatment of Infectious Diseases Hangzhou China
3. Marie Bashir Institute for Infectious Diseases and Biosecurity Charles Perkins Centre, School of Biological Sciences and Sydney Medical School, The University of Sydney Sydney Australia
4. Wuhan Center for Disease Control and Prevention Wuhan China
5. Wenzhou Center for Disease Control and Prevention Wenzhou China

† Corresponding author

## Abstract

Although arthropods are important viral vectors, the biodiversity of arthropod viruses, as well as the role that arthropods have played in viral origins and evolution, is unclear. Through RNA sequencing of 70 arthropod species we discovered 112 novel viruses that appear to be ancestral to much of the documented genetic diversity of negative-sense RNA viruses, a number of which are also present as endogenous genomic copies. With this greatly enriched diversity we revealed that arthropods contain viruses that fall basal to major virus groups, including the vertebrate-specific arenaviruses, filoviruses, hantaviruses, influenza viruses, lyssaviruses, and paramyxoviruses. We similarly documented a remarkable diversity of genome structures in arthropod viruses, including a putative circular form, that sheds new light on the evolution of genome organization. Hence, arthropods are a major reservoir of viral genetic diversity and have likely been central to viral evolution.

## Introduction

Negative-sense RNA viruses are important pathogens that cause a variety of diseases in humans including influenza, hemorrhagic fever, encephalitis, and rabies. Taxonomically, those negative-sense RNA viruses described to date comprise at least eight virus families and four unassigned genera or species (King et al., 2012). Although they share (i) a homologous RNA-dependent RNA polymerase (RdRp), (ii) inverted complementary genome ends, and (iii) an encapsidated negative-sense RNA genome, these viruses display substantial diversity in terms of virion morphology and genome organization (King et al., 2012). One key aspect of genome organization is the number of distinct segments, which is also central to virus classification. Among negative-sense RNA viruses, the number of segments varies from one (order Mononegavirales; unsegmented) to two (family Arenaviridae), three (Bunyaviridae), three-to-four (Ophioviridae), and six-to-eight (Orthomyxoviridae) and is further complicated by differences in the number, structure, and arrangement of the encoded genes.

Despite their diversity and importance in infectious disease, the origins and evolutionary history of the negative-sense RNA viruses are largely obscure. Arthropods harbor a diverse range of RNA viruses, which are often divergent from those that infect vertebrates (Marklewitz et al., 2011, 2013; Cook et al., 2013; Ballinger et al., 2014; Qin et al., 2014; Tokarz et al., 2014a, 2014b). However, those arthropod viruses sampled to date are generally those that have a relationship with vertebrates or are known to be agents of disease (Junglen and Drosten, 2013). To determine the extent of viral diversity harbored by arthropods, as well as their evolutionary history, we performed a systematic survey of negative-sense RNA viruses using RNA sequencing (RNA-seq) on a wide range of arthropods.

## Results

### Discovery of highly divergent negative-sense RNA viruses

We focused our study of virus biodiversity and evolution on 70 potential host species from four arthropod classes: Insecta, Arachnida, Chilopoda, and Malacostraca (Table 1 and Figure 1). From these samples, 16 separate cDNA libraries were constructed and sequenced, resulting in a total of 147.4 Gb of 100-base pair-end reads (Table 1). Blastx comparisons against protein sequences of negative-sense RNA virus revealed 108 distinct types of complete or nearly complete large (L) proteins (or polymerase protein 1 (PB1) in the case of orthomyxoviruses) that encode the relatively conserved RdRp (Tables 2–4). Four additional types of previously undescribed RdRp sequence (>1000 amino acids) were identified from the Transcriptome Shotgun Assembly (TSA) database. Together, these proteins exhibited an enormous diversity in terms of sequence variation and structure. Most notably, this data set of RdRp sequences is distinct from both previously described sequences and from each other, with the most divergent showing as little as 15.8% amino acid sequence identity to its closest relatives (Tables 2–4). Overall, these data provide evidence for at least 16 potentially new families and genera of negative-sense RNA viruses, defined as whose RdRp sequences shared less than 25% amino acid identity with existing taxa.

**Table 1.**
 Host and geographic information and data output for each pool of arthropod samples


<table>
  <thead>
    <tr>
      <th>Pool</th>
      <th>No of units</th>
      <th>Order</th>
      <th>Species</th>
      <th>Locations</th>
      <th>Data generated (bases)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mosquitoes—Hubei</td>
      <td>24</td>
      <td>Diptera</td>
      <td>Aedes sp, Armigeres subalbatus, Anopheles sinensis, Culex quinquefasciatus, Culex tritaeniorhynchus</td>
      <td>Hubei</td>
      <td>26,606,799,000</td>
    </tr>
    <tr>
      <td>Mosquitoes—Zhejiang</td>
      <td>26</td>
      <td>Diptera</td>
      <td>Aedes albopictus, Armigeres subalbatus, Anopheles paraliae, Anopheles sinensis, Culex pipiens, Culex sp, Culex tritaeniorhynchus</td>
      <td>Zhejiang</td>
      <td>7,233,954,480</td>
    </tr>
    <tr>
      <td>True flies</td>
      <td>24</td>
      <td>Diptera</td>
      <td>Atherigona orientalis, Chrysomya megacephala, Lucilia sericata, Musca domestica, Sarcophaga dux, S. peregrina, S. sp</td>
      <td>Hubei</td>
      <td>6,574,954,320</td>
    </tr>
    <tr>
      <td>Horseflies</td>
      <td>24</td>
      <td>Diptera</td>
      <td>Unidentified Tabanidae (5 species)</td>
      <td>Hubei</td>
      <td>8,721,642,060</td>
    </tr>
    <tr>
      <td>Cockroaches</td>
      <td>24</td>
      <td>Blattodea</td>
      <td>Blattella germanica</td>
      <td>Hubei</td>
      <td>6,182,028,000</td>
    </tr>
    <tr>
      <td>Water striders</td>
      <td>12</td>
      <td>Hemiptera</td>
      <td>Unidentified Gerridae (2 species)</td>
      <td>Hubei</td>
      <td>3,154,714,200</td>
    </tr>
    <tr>
      <td>Insects mix 1</td>
      <td>6</td>
      <td>Diptera, Coleoptera, Lepidoptera, Neuroptera</td>
      <td>Abraxas tenuisuffusa, Hermetia illucens, unidentified Chrysopidae, unidentified Coleoptera, Psychoda alternata, unidentified Diptera, unidentified Stratiomyidae</td>
      <td>Zhejiang</td>
      <td>7,745,172,660</td>
    </tr>
    <tr>
      <td>Insects mix 2</td>
      <td>4</td>
      <td>Diptera, Hemiptera</td>
      <td>Unidentified Hippoboscidae (2 species), Cimex hemipterus</td>
      <td>Hubei</td>
      <td>5,916,431,520</td>
    </tr>
    <tr>
      <td>Insects mix 3 (insect near water)</td>
      <td>10</td>
      <td>Odonata, Hemiptera, Hymenoptera, Isopoda</td>
      <td>Pseudothemis zonata, unidentified Nepidae (2 species), Camponotus japonicus, Diplonychus sp, Asellus sp</td>
      <td>Hubei</td>
      <td>11,973,368,200</td>
    </tr>
    <tr>
      <td>Insects mix 4 (insect in the mountain)</td>
      <td>12</td>
      <td>Diptera, Orthoptera, Odonata, Hymenoptera, Hemiptera</td>
      <td>Psychoda alternata, Velarifictorus micado, Crocothemis servilia, unidentified Phoridae, unidentified Lampyridae, Aphelinus sp, Hyalopterus pruni, Aulacorthum magnolia</td>
      <td>Hubei</td>
      <td>6,882,491,800</td>
    </tr>
    <tr>
      <td>Ticks</td>
      <td>16</td>
      <td>Ixodida</td>
      <td>Dermacentor marginatus, Dermacentor sp, Haemaphysalis doenitzi, H. longicornis, H. sp, H. formosensis, Hyalomma asiaticum, Rhipicephalus microplus, Argas miniatus</td>
      <td>Hubei, Zhejiang, Beijing, Xinjiang</td>
      <td>24,708,479,580</td>
    </tr>
    <tr>
      <td>Ticks Hyalomma asiaticum</td>
      <td>1</td>
      <td>Ixodida</td>
      <td>Hyalomma asiaticum</td>
      <td>Xinjiang</td>
      <td>2,006,000,100</td>
    </tr>
    <tr>
      <td>Spiders</td>
      <td>32</td>
      <td>Araneae</td>
      <td>Neoscona nautica, Parasteatoda tepidariorum, Plexippus setipes, Pirata sp, unidentified Araneae</td>
      <td>Hubei</td>
      <td>11,361,912,300</td>
    </tr>
    <tr>
      <td>Shrimps</td>
      <td>48</td>
      <td>Decapoda</td>
      <td>Exopalaemon carinicauda, Metapenaeus sp, Solenocera crassicornis, Penaeus monodon, Litopenaeus vannamei</td>
      <td>Zhejiang</td>
      <td>5,365,359,900</td>
    </tr>
    <tr>
      <td>Crabs and barnacles</td>
      <td>35</td>
      <td>Decapoda, Scalpelliformes</td>
      <td>Capitulum mitella, Charybdis hellerii, C. japonica, Uca arcuata</td>
      <td>Zhejiang</td>
      <td>5,833,269,360</td>
    </tr>
    <tr>
      <td>Millipedes</td>
      <td>12</td>
      <td>Polydesmida</td>
      <td>Unidentified Polydesmidae (2 species)</td>
      <td>Hubei, Beijing</td>
      <td>7,176,702,400</td>
    </tr>
  </tbody>
</table>

![Figure 1.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig1-v2.jpg)

**Figure 1.:** The taxonomic units in the tree correspond to the unit samples used in the RNA extraction. Species or genus information is marked to the left of the tree.

**Table 2.**
 Mononegavirales-related RdRp sequences discovered in this study


<table>
  <thead>
    <tr>
      <th>Virus name</th>
      <th>Length of RdRp</th>
      <th>Classification</th>
      <th>Pool</th>
      <th>Abundance</th>
      <th>Putative arthropod host</th>
      <th>Closest relative (aa identity)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bole Tick Virus 3</td>
      <td>2155</td>
      <td>Chuvirus</td>
      <td>Ticks</td>
      <td>202.35</td>
      <td>Hyalomma asiaticum</td>
      <td>Midway virus (17.1%)</td>
    </tr>
    <tr>
      <td>Changping Tick Virus 2</td>
      <td>2156</td>
      <td>Chuvirus</td>
      <td>Ticks</td>
      <td>185.73</td>
      <td>Dermacentor sp</td>
      <td>Midway virus (17.6%)</td>
    </tr>
    <tr>
      <td>Changping Tick Virus 3</td>
      <td>2209</td>
      <td>Chuvirus</td>
      <td>Ticks</td>
      <td>41.80</td>
      <td>Dermacentor sp</td>
      <td>Midway virus (16.5%)</td>
    </tr>
    <tr>
      <td>Lishi Spider Virus 1</td>
      <td>2180</td>
      <td>Chuvirus</td>
      <td>Spiders</td>
      <td>5.82</td>
      <td>Parasteatoda tepidariorum</td>
      <td>Midway virus (16.9%)</td>
    </tr>
    <tr>
      <td>Shayang Fly Virus 1</td>
      <td>2459</td>
      <td>Chuvirus</td>
      <td>True flies</td>
      <td>8.99</td>
      <td>Atherigona orientalis</td>
      <td>Maize mosaic virus (16.8%)</td>
    </tr>
    <tr>
      <td>Shuangao Fly Virus 1</td>
      <td>2097</td>
      <td>Chuvirus</td>
      <td>Insect mix 1</td>
      <td>23.63</td>
      <td>Unidentified Diptera</td>
      <td>Lettuce big-vein associated virus (16.3%)</td>
    </tr>
    <tr>
      <td>Shuangao Insect Virus 5</td>
      <td>2291</td>
      <td>Chuvirus</td>
      <td>Insect mix 1</td>
      <td>209.31</td>
      <td>Unidentified Diptera, Abraxas tenuisuffusa, unidentified Chrysopidae</td>
      <td>Potato yellow dwarf virus (16.3%)</td>
    </tr>
    <tr>
      <td>Shuangao Lacewing Virus</td>
      <td>2145</td>
      <td>Chuvirus</td>
      <td>Insect mix 1</td>
      <td>44.48</td>
      <td>Unidentified Chrysopidae</td>
      <td>Potato yellow dwarf virus (16.8%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 4</td>
      <td>2101</td>
      <td>Chuvirus</td>
      <td>Ticks</td>
      <td>137.22</td>
      <td>Argas miniatus</td>
      <td>Midway virus (17.5%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 5</td>
      <td>2201</td>
      <td>Chuvirus</td>
      <td>Ticks</td>
      <td>276.32</td>
      <td>Dermacentor marginatus</td>
      <td>Midway virus (16.8%)</td>
    </tr>
    <tr>
      <td>Wenzhou Crab Virus 2</td>
      <td>2208</td>
      <td>Chuvirus</td>
      <td>Crabs and barnacles</td>
      <td>4054.25</td>
      <td>Charybdis japonica, Charybdis lucifera, Charybdis hellerii</td>
      <td>Midway virus (15.8%)</td>
    </tr>
    <tr>
      <td>Wenzhou Crab Virus 3</td>
      <td>2077</td>
      <td>Chuvirus</td>
      <td>Crabs and barnacles</td>
      <td>169.21</td>
      <td>Charybdis japonica</td>
      <td>Midway virus (16.3%)</td>
    </tr>
    <tr>
      <td>Wuchang Cockroach Virus 3</td>
      <td>2203</td>
      <td>Chuvirus</td>
      <td>Cockroaches</td>
      <td>440.14</td>
      <td>Blattella germanica</td>
      <td>Midway virus (16.3%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 6</td>
      <td>2182</td>
      <td>Chuvirus</td>
      <td>Insect mix 2</td>
      <td>4.12</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Midway virus (16.4%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 7</td>
      <td>2174</td>
      <td>Chuvirus</td>
      <td>Insect mix 2</td>
      <td>99.83</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Midway virus (17.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 8</td>
      <td>2159</td>
      <td>Chuvirus</td>
      <td>Mosquito Hubei</td>
      <td>300.33</td>
      <td>Culex tritaeniorhynchus, C. quinquefasciatus, Anopheles sinensis, Armigeres subalbatus</td>
      <td>Midway virus (16.7%)</td>
    </tr>
    <tr>
      <td>Wuhan Tick Virus 2</td>
      <td>2189</td>
      <td>Chuvirus</td>
      <td>Ticks</td>
      <td>154.46</td>
      <td>Rhipicephalus microplus</td>
      <td>Midway virus (16.7%)</td>
    </tr>
    <tr>
      <td>Culex tritaeniorhynchus rhabdovirus</td>
      <td>2142</td>
      <td>Culex tritaeniorhynchus rhabdovirus</td>
      <td>Mosquito Hubei</td>
      <td>3517.32</td>
      <td>Culex tritaeniorhynchus, C. quinquefasciatus, Anopheles sinensis, Armigeres subalbatus, Aedes sp</td>
      <td>Isfahan virus (38.5%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 4</td>
      <td>2105</td>
      <td>Cytorhabdovirus</td>
      <td>Insect mix 4</td>
      <td>94.92</td>
      <td>Hyalopterus pruni OR Aphelinus sp</td>
      <td>Lettuce necrotic yellows virus (40.6%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 5</td>
      <td>2098</td>
      <td>Cytorhabdovirus</td>
      <td>Insect mix 4</td>
      <td>622.97</td>
      <td>Hyalopterus pruni OR Aphelinus sp</td>
      <td>Persimmon virus A (47.9%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 6</td>
      <td>2079</td>
      <td>Cytorhabdovirus</td>
      <td>Insect mix 4</td>
      <td>991.99</td>
      <td>Hyalopterus pruni OR Aphelinus sp</td>
      <td>Persimmon virus A (45.2)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 5</td>
      <td>2123</td>
      <td>Kolente virus like</td>
      <td>Insect mix 2</td>
      <td>98.92</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Kolente virus (54.5%)</td>
    </tr>
    <tr>
      <td>Yongjia Tick Virus 2</td>
      <td>2113</td>
      <td>Nishimuro virus like</td>
      <td>Ticks</td>
      <td>13.14</td>
      <td>Haemaphysalis hystricis</td>
      <td>Nishimuro virus (54.2%)</td>
    </tr>
    <tr>
      <td>Shayang Fly Virus 2</td>
      <td>2170</td>
      <td>Sigmavirus like</td>
      <td>True flies</td>
      <td>36.83</td>
      <td>Musca domestica, Chrysomya megacephala</td>
      <td>Isfahan virus (44.1%)</td>
    </tr>
    <tr>
      <td>Wuhan Fly Virus 2</td>
      <td>2134</td>
      <td>Sigmavirus like</td>
      <td>True flies</td>
      <td>18.37</td>
      <td>Musca domestica, Sarcophaga sp</td>
      <td>Vesicular stomatitis Indiana virus (43.4%)</td>
    </tr>
    <tr>
      <td>Wuhan House Fly Virus 1</td>
      <td>2098</td>
      <td>Sigmavirus like</td>
      <td>True flies</td>
      <td>31.04</td>
      <td>Musca domestica</td>
      <td>Isfahan virus (42.8%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 10</td>
      <td>2146</td>
      <td>Sigmavirus like</td>
      <td>Insect mix 2</td>
      <td>235.94</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Drosophila melanogaster sigmavirus (51.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 8</td>
      <td>2145</td>
      <td>Sigmavirus like</td>
      <td>Insect mix 2</td>
      <td>292.11</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Drosophila melanogaster sigmavirus (50.6%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 9</td>
      <td>2145</td>
      <td>Sigmavirus like</td>
      <td>Insect mix 2</td>
      <td>69.37</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Drosophila melanogaster sigmavirus (51.4%)</td>
    </tr>
    <tr>
      <td>Bole Tick Virus 2</td>
      <td>2171</td>
      <td>Unclassified dimarhabdovirus 1</td>
      <td>Ticks</td>
      <td>38.19</td>
      <td>Hyalomma asiaticum</td>
      <td>Isfahan virus (38.1%)</td>
    </tr>
    <tr>
      <td>Huangpi Tick Virus 3</td>
      <td>2193</td>
      <td>Unclassified dimarhabdovirus 1</td>
      <td>Ticks</td>
      <td>15.81</td>
      <td>Haemaphysalis doenitzi</td>
      <td>Eel virus European X (40%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 3</td>
      <td>2182</td>
      <td>Unclassified dimarhabdovirus 1</td>
      <td>Ticks</td>
      <td>96.30</td>
      <td>Dermacentor marginatus</td>
      <td>Eel virus European X (39.8%)</td>
    </tr>
    <tr>
      <td>Taishun Tick Virus</td>
      <td>2226</td>
      <td>Unclassified dimarhabdovirus 1</td>
      <td>Ticks</td>
      <td>24.56</td>
      <td>Haemaphysalis hystricis</td>
      <td>Vesicular stomatitis Indiana virus (36.6%)</td>
    </tr>
    <tr>
      <td>Wuhan Tick Virus 1</td>
      <td>2191</td>
      <td>Unclassified dimarhabdovirus 1</td>
      <td>Ticks</td>
      <td>119.92</td>
      <td>Rhipicephalus microplus</td>
      <td>Eel virus European X (38.3%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 7</td>
      <td>2120</td>
      <td>Unclassified dimarhabdovirus 2</td>
      <td>Insect mix 4</td>
      <td>241.7</td>
      <td>Hyalopterus pruni OR Aphelinus sp</td>
      <td>Isfahan virus (42.6%)</td>
    </tr>
    <tr>
      <td>Lishi Spider Virus 2</td>
      <td>2201</td>
      <td>Unclassified mononegavirus 1</td>
      <td>Spiders</td>
      <td>5.57</td>
      <td>Unidentified Araneae</td>
      <td>Maize fine streak virus (19.6%)</td>
    </tr>
    <tr>
      <td>Sanxia Water Strider Virus 4</td>
      <td>2108</td>
      <td>Unclassified mononegavirus 1</td>
      <td>Water striders</td>
      <td>4767.82</td>
      <td>Unidentified Gerridae</td>
      <td>Orchid fleck virus (20.5%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 6</td>
      <td>2068</td>
      <td>Unclassified mononegavirus 1</td>
      <td>Ticks</td>
      <td>17.92</td>
      <td>Argas miniatus</td>
      <td>Maize mosaic virus (20.6%)</td>
    </tr>
    <tr>
      <td>Shuangao Fly Virus 2</td>
      <td>1966</td>
      <td>Unclassified mononegavirus 2</td>
      <td>Insect mix 1</td>
      <td>25.94</td>
      <td>Psychoda alternata</td>
      <td>Midway virus (21.3%)</td>
    </tr>
    <tr>
      <td>Xincheng Mosquito Virus</td>
      <td>2026</td>
      <td>Unclassified mononegavirus 2</td>
      <td>Mosquito Hubei</td>
      <td>400.12</td>
      <td>Anopheles sinensis</td>
      <td>Midway virus (19.2%)</td>
    </tr>
    <tr>
      <td>Wenzhou Crab Virus 1</td>
      <td>1807</td>
      <td>Unclassified mononegavirus 3</td>
      <td>Crabs and barnacles</td>
      <td>382.29</td>
      <td>Capitulum mitella, Charybdis japonica, Charybdis lucifera</td>
      <td>Midway virus (22.2%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 7</td>
      <td>2215</td>
      <td>Unclassified rhabdovirus 1</td>
      <td>Ticks</td>
      <td>35.86</td>
      <td>Argas miniatus</td>
      <td>Orchid fleck virus (24.5%)</td>
    </tr>
    <tr>
      <td>Jingshan Fly Virus 2</td>
      <td>1970</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>True flies</td>
      <td>4.43</td>
      <td>Sarcophaga sp</td>
      <td>Maize fine streak virus (23.4%)</td>
    </tr>
    <tr>
      <td>Sanxia Water Strider Virus 5</td>
      <td>2264</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>Water striders</td>
      <td>4373.68</td>
      <td>Unidentified Gerridae</td>
      <td>Northern cereal mosaic virus (22.6%)</td>
    </tr>
    <tr>
      <td>Shayang Fly Virus 3</td>
      <td>2231</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>True flies</td>
      <td>27.73</td>
      <td>Chrysomya megacephala, Atherigona orientalis</td>
      <td>Maize fine streak virus (22.6%)</td>
    </tr>
    <tr>
      <td>Shuangao Bedbug Virus 2</td>
      <td>2207</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>Insect mix 2</td>
      <td>16.29</td>
      <td>Cimex hemipterus</td>
      <td>Maize fine streak virus (22.5%)</td>
    </tr>
    <tr>
      <td>Shuangao Insect Virus 6</td>
      <td>2088</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>Insect mix 1</td>
      <td>14.37</td>
      <td>Unidentified Diptera, Abraxas tenuisuffusa</td>
      <td>Potato yellow dwarf virus (21.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Ant Virus</td>
      <td>2118</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>Insect mix 3</td>
      <td>169.79</td>
      <td>Camponotus japonicus</td>
      <td>Lettuce necrotic yellows virus (21.4%)</td>
    </tr>
    <tr>
      <td>Wuhan Fly Virus 3</td>
      <td>2230</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>True flies</td>
      <td>6.00</td>
      <td>Musca domestica, Sarcophaga sp</td>
      <td>Maize fine streak virus (21.9%)</td>
    </tr>
    <tr>
      <td>Wuhan House Fly Virus 2</td>
      <td>2233</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>True flies</td>
      <td>221.04</td>
      <td>Musca domestica</td>
      <td>Northern cereal mosaic virus (23.4%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 9</td>
      <td>2260</td>
      <td>Unclassified rhabdovirus 2</td>
      <td>Mosquito Hubei</td>
      <td>56.19</td>
      <td>Culex tritaeniorhynchus, C. quinquefasciatus, Aedes sp</td>
      <td>Persimmon virus A (23.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 11</td>
      <td>2110</td>
      <td>Vesiculovirus like</td>
      <td>Insect mix 2</td>
      <td>6.11</td>
      <td>Unidentified Hippoboscidae</td>
      <td>Vesicular stomatitis Indiana virus (52.9%)</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Bunya-arenaviridae-related RdRp sequences discovered in this study


<table>
  <thead>
    <tr>
      <th>Virus name</th>
      <th>Length of RdRp</th>
      <th>Classification</th>
      <th>Pool</th>
      <th>Abundance</th>
      <th>Putative arthropod host</th>
      <th>Closest relative (aa identity)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Huangpi Tick Virus 1</td>
      <td>3914</td>
      <td>Nairovirus like</td>
      <td>Ticks</td>
      <td>11.32</td>
      <td>Haemaphysalis doenitzi</td>
      <td>Hazara virus (39.5%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 1</td>
      <td>3962</td>
      <td>Nairovirus like</td>
      <td>Ticks</td>
      <td>88.91</td>
      <td>Dermacentor marginatus</td>
      <td>Hazara virus (39.6%)</td>
    </tr>
    <tr>
      <td>Wenzhou Tick Virus</td>
      <td>3967</td>
      <td>Nairovirus like</td>
      <td>Ticks</td>
      <td>44.30</td>
      <td>Haemaphysalis hystricis</td>
      <td>Crimean-Congo hemorrhagic fever virus (39.1%)</td>
    </tr>
    <tr>
      <td>Shayang Spider Virus 1</td>
      <td>4403</td>
      <td>Nairovirus like</td>
      <td>Spiders</td>
      <td>90.95</td>
      <td>Neoscona nautica, Parasteatoda tepidariorum, Plexippus setipes</td>
      <td>Crimean-Congo hemorrhagic fever virus (26.2%)</td>
    </tr>
    <tr>
      <td>Xinzhou Spider Virus</td>
      <td>4037</td>
      <td>Nairovirus like</td>
      <td>Spiders</td>
      <td>3.79</td>
      <td>Neoscona nautica, Parasteatoda tepidariorum</td>
      <td>Erve virus (22.9%)</td>
    </tr>
    <tr>
      <td>Sanxia Water Strider Virus 1</td>
      <td>3936</td>
      <td>Nairovirus like</td>
      <td>Water striders</td>
      <td>26,483.38</td>
      <td>Unidentified Gerridae</td>
      <td>Hazara virus (23.4%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 1</td>
      <td>2250</td>
      <td>Orthobunyavirus</td>
      <td>Insect mix 2</td>
      <td>67.06</td>
      <td>Unidentified Hippoboscoidea</td>
      <td>La Crosse virus (57.8%)</td>
    </tr>
    <tr>
      <td>Shuangao Insect Virus 1</td>
      <td>2335</td>
      <td>Orthobunyavirus like</td>
      <td>Insect mix 1</td>
      <td>7.97</td>
      <td>Unidentified Chrysopidae, Psychoda alternata</td>
      <td>Khurdun virus (29.1%)</td>
    </tr>
    <tr>
      <td>Wuchang Cockroach Virus 1</td>
      <td>2125</td>
      <td>Phasmavirus like</td>
      <td>Cockroaches</td>
      <td>11,283.22</td>
      <td>Blattella germanica</td>
      <td>Kigluaik phantom virus (35.9%)</td>
    </tr>
    <tr>
      <td>GAQJ01007189</td>
      <td>1554</td>
      <td>Phasmavirus like</td>
      <td>Database</td>
      <td>N/A</td>
      <td>Ostrinia furnacalis</td>
      <td>Kigluaik phantom virus (35.9%)</td>
    </tr>
    <tr>
      <td>Shuangao Insect Virus 2</td>
      <td>1765</td>
      <td>Phasmavirus like</td>
      <td>Insect mix 1</td>
      <td>36.32</td>
      <td>Abraxas tenuisuffusa, unidentified Diptera</td>
      <td>Kigluaik phantom virus (31.9%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 1</td>
      <td>2095</td>
      <td>Phasmavirus like</td>
      <td>Mosquito Hubei, Mosquito Zhejiang</td>
      <td>3523.08</td>
      <td>Culex tritaeniorhynchus, Anopheles sinensis, Culex quinquefasciatus</td>
      <td>Kigluaik phantom virus (39.5%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 2</td>
      <td>2111</td>
      <td>Phasmavirus like</td>
      <td>Mosquito Hubei, Mosquito Zhejiang</td>
      <td>39.66</td>
      <td>Culex tritaeniorhynchus, Anopheles sinensis, Culex quinquefasciatus, Aedes sp</td>
      <td>Kigluaik phantom virus (39.6%)</td>
    </tr>
    <tr>
      <td>Huangpi Tick Virus 2</td>
      <td>2121</td>
      <td>Phlebovirus</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>Haemaphysalis sp</td>
      <td>Uukuniemi virus (49.3%)</td>
    </tr>
    <tr>
      <td>Bole Tick Virus 1</td>
      <td>2148</td>
      <td>Phlebovirus</td>
      <td>Ticks</td>
      <td>67.86</td>
      <td>Hyalomma asiaticum</td>
      <td>Uukuniemi virus (37.9%)</td>
    </tr>
    <tr>
      <td>Changping Tick Virus 1</td>
      <td>2194</td>
      <td>Phlebovirus</td>
      <td>Ticks</td>
      <td>335.25</td>
      <td>Dermacentor sp</td>
      <td>Uukuniemi virus (39.7%)</td>
    </tr>
    <tr>
      <td>Dabieshan Tick Virus</td>
      <td>2148</td>
      <td>Phlebovirus</td>
      <td>Ticks</td>
      <td>250.62</td>
      <td>Haemaphysalis longicornis</td>
      <td>Uukuniemi virus (39.2%)</td>
    </tr>
    <tr>
      <td>Lihan Tick Virus</td>
      <td>2151</td>
      <td>Phlebovirus</td>
      <td>Ticks</td>
      <td>60.40</td>
      <td>Rhipicephalus microplus</td>
      <td>Uukuniemi virus (38.6%)</td>
    </tr>
    <tr>
      <td>Tacheng Tick Virus 2</td>
      <td>2189</td>
      <td>Phlebovirus</td>
      <td>Ticks</td>
      <td>132.59</td>
      <td>Dermacentor marginatus</td>
      <td>Uukuniemi virus (39.0%)</td>
    </tr>
    <tr>
      <td>Yongjia Tick Virus 1</td>
      <td>2138</td>
      <td>Phlebovirus</td>
      <td>Ticks</td>
      <td>119.49</td>
      <td>Haemaphysalis hystricis</td>
      <td>Uukuniemi virus (40.5%)</td>
    </tr>
    <tr>
      <td>GAIX01000059</td>
      <td>2151</td>
      <td>Phlebovirus like</td>
      <td>Database</td>
      <td>N/A</td>
      <td>Pararge aegeria</td>
      <td>Cumuto virus (24.1%)</td>
    </tr>
    <tr>
      <td>GAKZ01048260</td>
      <td>1583</td>
      <td>Phlebovirus like</td>
      <td>Database</td>
      <td>N/A</td>
      <td>Procotyla fluviatilis</td>
      <td>Cumuto virus (22.8%)</td>
    </tr>
    <tr>
      <td>GAQJ01008681</td>
      <td>2261</td>
      <td>Phlebovirus like</td>
      <td>Database</td>
      <td>N/A</td>
      <td>Ostrinia furnacalis</td>
      <td>Gouleako virus (22.0%)</td>
    </tr>
    <tr>
      <td>Shuangao Insect Virus 3</td>
      <td>2050</td>
      <td>Phlebovirus like</td>
      <td>Insect mix 1</td>
      <td>339.41</td>
      <td>Unidentified Chrysopidae, unidentified Diptera</td>
      <td>Cumuto virus (23.7%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 2</td>
      <td>2327</td>
      <td>Phlebovirus like</td>
      <td>Insect mix 2</td>
      <td>3.57</td>
      <td>Unidentified Hippoboscoidea</td>
      <td>Uukuniemi virus (25.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 1</td>
      <td>2099</td>
      <td>Phlebovirus like</td>
      <td>Insect mix 3</td>
      <td>178.53</td>
      <td>Asellus sp, unidentified Nepidae, Camponotus japonicus</td>
      <td>Cumuto virus (24.8%)</td>
    </tr>
    <tr>
      <td>Huangshi Humpbacked Fly Virus</td>
      <td>2009</td>
      <td>Phlebovirus like</td>
      <td>Insect mix 4</td>
      <td>13.13</td>
      <td>Unidentified Phoridae</td>
      <td>Cumuto virus (18.1%)</td>
    </tr>
    <tr>
      <td>Yichang Insect Virus</td>
      <td>2100</td>
      <td>Phlebovirus like</td>
      <td>Insect mix 4</td>
      <td>71.50</td>
      <td>Aulacorthum magnoliae</td>
      <td>Gouleako virus (45.3%)</td>
    </tr>
    <tr>
      <td>Wuhan Millipede Virus 1</td>
      <td>1854</td>
      <td>Phlebovirus like</td>
      <td>Millipedes and insect mix 3</td>
      <td>825.66</td>
      <td>Unidentified Polydesmidae</td>
      <td>Cumuto virus (25.3%)</td>
    </tr>
    <tr>
      <td>Qingnian Mosquito Virus</td>
      <td>2243</td>
      <td>Phlebovirus like</td>
      <td>Mosquito Hubei</td>
      <td>17.09</td>
      <td>Culex quinquefasciatus</td>
      <td>Razdan virus (21.0%)</td>
    </tr>
    <tr>
      <td>Wutai Mosquito Virus</td>
      <td>2185</td>
      <td>Phlebovirus like</td>
      <td>Mosquito Hubei</td>
      <td>70.72</td>
      <td>Culex quinquefasciatus</td>
      <td>Rice stripe virus (26.4%)</td>
    </tr>
    <tr>
      <td>Xinzhou Mosquito Virus</td>
      <td>2022</td>
      <td>Phlebovirus like</td>
      <td>Mosquito Hubei</td>
      <td>98.95</td>
      <td>Anopheles sinensis</td>
      <td>Cumuto virus (24.7%)</td>
    </tr>
    <tr>
      <td>Zhee Mosquito Virus</td>
      <td>2443</td>
      <td>Phlebovirus like</td>
      <td>Mosquito Hubei, Mosquito Zhejiang</td>
      <td>308.98</td>
      <td>Anopheles sinensis, Armigeres subalbatus</td>
      <td>Cumuto virus (22.6%)</td>
    </tr>
    <tr>
      <td>Wenzhou Shrimp Virus 1</td>
      <td>2051</td>
      <td>Phlebovirus like</td>
      <td>Shrimps</td>
      <td>5859.37</td>
      <td>Penaeus monodon</td>
      <td>Uukuniemi virus (32.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Spider Virus</td>
      <td>2251</td>
      <td>Phlebovirus like</td>
      <td>Spiders</td>
      <td>17.71</td>
      <td>Neoscona nautica, Parasteatoda tepidariorum, Plexippus setipes</td>
      <td>Uukuniemi virus (21.7%)</td>
    </tr>
    <tr>
      <td>Wuhan Fly Virus 1</td>
      <td>2192</td>
      <td>Phlebovirus like</td>
      <td>True flies</td>
      <td>68.58</td>
      <td>Atherigona orientalis, Chrysomya megacephala, Sarcophaga sp, Musca domestica</td>
      <td>Grand Arbaud virus (27.8%)</td>
    </tr>
    <tr>
      <td>Wuhan Horsefly Virus</td>
      <td>3117</td>
      <td>Tenuivirus like</td>
      <td>Horseflies</td>
      <td>13.50</td>
      <td>Unidentified Tabanidae</td>
      <td>Uukuniemi virus (28.2%)</td>
    </tr>
    <tr>
      <td>Jiangxia Mosquito Virus 1</td>
      <td>1889</td>
      <td>Unclassified segmented virus 1</td>
      <td>Mosquito Hubei</td>
      <td>11.55</td>
      <td>Culex tritaeniorhynchus</td>
      <td>Gouleako virus (16.7%)</td>
    </tr>
    <tr>
      <td>Shuangao Bedbug Virus 1</td>
      <td>2015</td>
      <td>Unclassified segmented virus 2</td>
      <td>Insect mix 2</td>
      <td>12.71</td>
      <td>Cimex hemipterus</td>
      <td>Murrumbidgee virus (16.3%)</td>
    </tr>
    <tr>
      <td>Jiangxia Mosquito Virus 2</td>
      <td>1860</td>
      <td>Unclassified segmented virus 2</td>
      <td>Mosquito Hubei</td>
      <td>2.81</td>
      <td>Culex tritaeniorhynchus</td>
      <td>Hantavirus (18.9%)</td>
    </tr>
    <tr>
      <td>Shuangao Mosquito Virus</td>
      <td>1996</td>
      <td>Unclassified segmented virus 2</td>
      <td>Mosquito Zhejiang</td>
      <td>11.67</td>
      <td>Armigeres subalbatus</td>
      <td>Hantavirus (18.7%)</td>
    </tr>
    <tr>
      <td>Wenzhou Shrimp Virus 2</td>
      <td>2241</td>
      <td>Unclassified segmented virus 3</td>
      <td>Shrimps</td>
      <td>3824.55</td>
      <td>Penaeus monodon, Exopalaemon carinicauda</td>
      <td>La Crosse virus (19.0%)</td>
    </tr>
    <tr>
      <td>Shayang Spider Virus 2</td>
      <td>2165</td>
      <td>Unclassified segmented virus 4</td>
      <td>Spiders</td>
      <td>12.75</td>
      <td>Neoscona nautica, Pirata sp, Parasteatoda tepidariorum, unidentified Araneae</td>
      <td>Akabane virus (16.6%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 2</td>
      <td>2377</td>
      <td>Unclassified segmented virus 5</td>
      <td>Insect mix 4</td>
      <td>223.06</td>
      <td>Hyalopterus pruni OR Aphelinus sp</td>
      <td>Kigluaik phantom virus (19.2%)</td>
    </tr>
    <tr>
      <td>Sanxia Water Strider Virus 2</td>
      <td>2349</td>
      <td>Unclassified segmented virus 5</td>
      <td>Water striders</td>
      <td>707.09</td>
      <td>Unidentified Gerridae</td>
      <td>Kigluaik phantom virus (19.8%)</td>
    </tr>
    <tr>
      <td>Wuhan Millipede Virus 2</td>
      <td>3709</td>
      <td>Unclassified segmented virus 6</td>
      <td>Millipedes</td>
      <td>1513.41</td>
      <td>Unidentified Polydesmidae</td>
      <td>Dugbe virus (17.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Insect Virus 3</td>
      <td>2231</td>
      <td>Unclassified segmented virus 7</td>
      <td>Insect mix 3</td>
      <td>3.50</td>
      <td>Asellus sp</td>
      <td>Herbert virus (17.2%)</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Orthomyxoviridae-related RdRp sequences discovered in this study


<table>
  <thead>
    <tr>
      <th>Virus name</th>
      <th>Length of RdRp</th>
      <th>Classification</th>
      <th>Pool</th>
      <th>Abundance</th>
      <th>Putative arthropod host</th>
      <th>Closest relative (aa identity)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Jingshan Fly Virus 1</td>
      <td>795</td>
      <td>Quaranjavirus</td>
      <td>True flies</td>
      <td>21.93</td>
      <td>Atherigona orientalis, Chrysomya megacephala, Sarcophaga sp, Musca domestica</td>
      <td>Johnston Atoll virus (36.9%)</td>
    </tr>
    <tr>
      <td>Jiujie Fly Virus</td>
      <td>653</td>
      <td>Quaranjavirus</td>
      <td>Horseflies</td>
      <td>10.30</td>
      <td>Unidentified Tabanidae</td>
      <td>Johnston Atoll virus (39.7%)</td>
    </tr>
    <tr>
      <td>Sanxia Water Strider Virus 3</td>
      <td>789</td>
      <td>Quaranjavirus</td>
      <td>Water striders</td>
      <td>1101.03</td>
      <td>Unidentified Gerridae</td>
      <td>Johnston Atoll virus (36.7%)</td>
    </tr>
    <tr>
      <td>Shayang Spider Virus 3</td>
      <td>768</td>
      <td>Quaranjavirus</td>
      <td>Spiders</td>
      <td>1.95</td>
      <td>Neoscona nautica</td>
      <td>Johnston Atoll virus (38.5%)</td>
    </tr>
    <tr>
      <td>Shuangao Insect Virus 4</td>
      <td>793</td>
      <td>Quaranjavirus</td>
      <td>Insect mix 1</td>
      <td>59.90</td>
      <td>Unidentified Diptera, unidentified Stratiomyidae</td>
      <td>Johnston Atoll virus (36.9%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 3</td>
      <td>784</td>
      <td>Quaranjavirus</td>
      <td>Insect mix 2</td>
      <td>500.77</td>
      <td>Unidentified Hippoboscoidea</td>
      <td>Johnston Atoll virus (37.7%)</td>
    </tr>
    <tr>
      <td>Wuhan Louse Fly Virus 4</td>
      <td>783</td>
      <td>Quaranjavirus</td>
      <td>Insect mix 2</td>
      <td>96.80</td>
      <td>Unidentified Hippoboscoidea</td>
      <td>Johnston Atoll virus (38.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 3</td>
      <td>801</td>
      <td>Quaranjavirus</td>
      <td>Mosquito Hubei</td>
      <td>40.07</td>
      <td>Culex tritaeniorhynchus, Culex quinquefasciatus, Armigeres subalbatus</td>
      <td>Johnston Atoll virus (35.6%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 4</td>
      <td>792</td>
      <td>Quaranjavirus</td>
      <td>Mosquito Hubei</td>
      <td>86.21</td>
      <td>Culex tritaeniorhynchus, Culex quinquefasciatus, Armigeres subalbatus</td>
      <td>Johnston Atoll virus (34.8%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 5</td>
      <td>806</td>
      <td>Quaranjavirus</td>
      <td>Mosquito Hubei</td>
      <td>75.05</td>
      <td>Culex tritaeniorhynchus, Culex quinquefasciatus, Armigeres subalbatus</td>
      <td>Johnston Atoll virus (35.5%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 6</td>
      <td>800</td>
      <td>Quaranjavirus</td>
      <td>Mosquito Hubei</td>
      <td>56.30</td>
      <td>Culex quinquefasciatus</td>
      <td>Johnston Atoll virus (34.2%)</td>
    </tr>
    <tr>
      <td>Wuhan Mosquito Virus 7</td>
      <td>779</td>
      <td>Quaranjavirus</td>
      <td>Mosquito Hubei</td>
      <td>20.74</td>
      <td>Anopheles sinensis, Culex quinquefasciatus</td>
      <td>Johnston Atoll virus (34.1%)</td>
    </tr>
    <tr>
      <td>Wuhan Mothfly Virus</td>
      <td>710</td>
      <td>Quaranjavirus</td>
      <td>Insect mix 4</td>
      <td>14.47</td>
      <td>Psychoda alternata</td>
      <td>Johnston Atoll virus (39.7%)</td>
    </tr>
    <tr>
      <td>Wuchang Cockroach Virus 2</td>
      <td>671</td>
      <td>Unclassified orthomyxovirus 1</td>
      <td>Cockroaches</td>
      <td>4.01</td>
      <td>Blattella germanica</td>
      <td>Influenza C virus (27.0%)</td>
    </tr>
  </tbody>
</table>

Next, we measured the abundance of these sequences as the number transcripts per million (TPM) within each library after the removal of rRNA reads. The abundance of viral transcripts calculated in this manner exhibited substantial variation (Figure 2, Tables 2–4): while the least abundant L segment (Shayang Spider Virus 3) contributed to less than 0.001% to the total non-ribosomal RNA content, the most abundant (Sanxia Water Strider Virus 1) was at a frequency of 21.2%, and up to 43.9% if we include the matching M and S segments of the virus. The remaining viral RdRp sequences fell within a range (10–1000 TPM) that matched the abundance level of highly expressed host mitochondrial genes (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig2-v2.jpg)

**Figure 2.:** Abundance is calculated after the removal of ribosomal RNA reads. As a comparison, we show the abundance of the two well characterized (positive-sense) RNA viruses: Japanese encephalitis virus and Gill-associated virus found in the Mosquito-Hubei and Shrimp libraries, respectively, as well as the range of abundance of host mitochondrial COI genes in these same multi-host libraries.

### Evolutionary history of negative-sense RNA viruses

With this highly diverse set of RdRp sequences in hand we re-examined the evolution of all available negative-sense RNA viruses by phylogenetic analysis (Figure 3; Figure 3—figure supplement 3). These data greatly expand the documented diversity of four viral families/orders—the Arenaviridae, Bunyaviridae, Orthomyxoviridae, and Mononegavirales—as well as of three floating genera—Tenuivirus, Emaravirus, and Varicosavirus (King et al., 2012). Most of the newly described arthropod viruses fell basal to the known genetic diversity in these taxa: their diversity either engulfed that of previously described viruses, as in the case of phlebovirus, nairovirus, and dimarhabdovirus, or appeared as novel lineages sandwiched between existing genera or families, and hence filling in a number of phylogenetic ‘gaps’ (Figure 3; Figure 3—figure supplement 3). One important example was a large monophyletic group of newly discovered viruses that fell between the major groups of segmented and unsegmented viruses (Figure 4); we name this putative new virus family the ‘Chuviridae’ reflecting the geographic location in China where most of this family were identified (‘Chu’ is a historical term referring to large area of China encompassing the middle and lower reaches of the Yangzi River). Also of note was that some of the previously defined families no longer appear as monophyletic. For example, although classified as distinct families, the family Arenaviridae fell within the genetic diversity of the family Bunyaviridae and as a sister group to viruses of the genus Nairovirus. Furthermore, the floating genus Tenuivirus was nested within the Phlebovirus-like clade, and another floating genus, Emaravirus, formed a monophyletic group with the Orthobunyavirus and Tospovirus genera (Figure 3C; Figure 3—figure supplement 2). Hence, there are important inconsistencies between the current virus classification scheme and the underlying evolutionary history of the RdRp revealed here.

![Figure 3.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig3-v2.jpg)

**Figure 3.:** This is initially displayed in an unrooted maximum likelihood (ML) tree including all major groups of negative-sense RNA viruses (A). Separate and more detailed ML phylogenies are then shown for the Orthomyxoviridae-like (B), Bunya-Arenaviridae-like (C), and Mononegavirales-like viruses (D). In all the phylogenies, the RdRp sequences described here from arthropods are either shaded purple or marked with solid gray circles. The names of previously defined genera/families are labeled to the right of the phylogenies. Based on their host types, the branches are shaded red (vertebrate-specific), yellow (vertebrate and arthropod), green (plant and arthropod), blue (non-arthropod invertebrates), or black (arthropod only). For clarity, statistical supports (i.e., approximate likelihood-ratio test (aLRT) with Shimodaira–Hasegawa-like procedure/posterior probabilities) are shown for key internal nodes only.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The phylogeny is reconstructed using RdRp alignments. Statistical support from the approximate likelihood-ratio test (aLRT) is shown on each node of the tree. The names of the viruses discovered in this study are shown in red. The names of reference sequences, which contain both the GenBank accession number and the virus species name, are shown in black. The names of previously defined genera/families are shown to the right of the phylogenies.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** The phylogeny is reconstructed using RdRp alignments. Statistical support from the aLRT is shown on each node of the tree. The names of the viruses discovered in this study are shown in red. The names of reference sequences, which contain both the GenBank accession number and the virus species name, are shown in black. The names of previously defined genera/families are shown to the right of the phylogenies.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The phylogeny is reconstructed using RdRp alignments. Statistical support from the aLRT is shown on each node of the tree. The names of the viruses discovered in this study are shown in red. The names of reference sequences, which contain both the GenBank accession number and the virus species name, are shown in black. The names of previously defined genera/families are shown to the right of the phylogenies.

![Figure 4.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig4-v2.jpg)

**Figure 4.:** The segmented viruses are labeled with segment numbers and shaded red. The unsegmented viruses are shaded green. The Chuviridae, which exhibit a wide variety of genome organizations, are shaded cyan. Three major types of putative chuvirus genomes (circular, circular and segmented, and linear) are shown in the right panel and are annotated with predicted ORFs: putative RdRp genes are shaded blue, putative glycoprotein genes are shaded orange, and the remaining ORFs are shaded gray.

A key result of this study is that much of the genetic diversity of negative-sense RNA viruses in vertebrates and plants now appears to be contained within viruses that utilize arthropods as hosts or vectors. Indeed, it is striking that all vertebrate-specific segmented and unsegmented viruses (arenavirus, bornavirus, filovirus, hantavirus, influenza viruses, lyssavirus, and paramyxovirus) fall within the genetic diversity of arthropod-associated viruses (Figures 3, 5). Also nested with arthropod-associated diversity were plant viruses (emaravirus, tospovirus, tenuiviruses, nucleorhabdovirus, cytorhabdovirus, and varicosavirus) (Figures 3, 5). Surprisingly, our phylogeny similarly placed two non-arthropod invertebrate viruses, found in nematodes (Heterodera glycines) and flatworms (Procotyla fluviatilis), within arthropod-associated diversity (Figure 3C, Figure 3—figure supplement 2), indicating that the role of non-arthropod invertebrates should be explored further. Finally, it was striking that although individual arthropod species can harbor a rich diversity of RNA viruses, many viruses seemed to be associated with different arthropod species that share the same ecological niche (Tables 2–4). Interestingly, host species in the same niche had similar viral contents that were generally incongruent with the host phylogeny (Figure 6). Such a pattern is indicative of frequent cross-species and occasional cross-genus virus transmission in the context of ecological and geographic proximity.

![Figure 5.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig5-v2.jpg)

**Figure 5.:** Vertebrate-specific viruses are shaded red, those infecting both vertebrates and arthropods (or with unknown vectors) are shaded yellow, those infecting both plants and arthropods are shaded green, those infecting non-arthropod invertebrates are shaded blue, and the remainder (arthropod only) are shaded black.

![Figure 6.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig6-v2.jpg)

**Figure 6.:** The comparisons include (A) Wuhan Horsefly Virus, (B) Wuhan Fly Virus 1, (C) Wuhan Mosquito Virus 2, and (D) Wuhan Mosquito Virus 1. Different host species/genera are distinguished with different colors, which are then mapped onto virus phylogeny to assess the phylogenetic congruence. ML phylogenetic trees were inferred in all cases.

### Diversity and evolution of virus genome organizations

The diversity of genome structures in these virus data was also striking. This can easily be documented with respect to the evolution of genome segmentation. The number of genome segments in negative-sense RNA viruses varies from one to eight. Our phylogenetic analysis revealed no particular trend for this number to increase or decrease through evolutionary time (Figure 4). Hence, genome segmentation (i.e., genomes with >1 segment) has clearly evolved on multiple occasions within the negative-sense RNA viruses (Figure 4), such that it is a relatively flexible genetic trait. Although most segmented viruses were distantly related to those with a single segment (Figure 4), close phylogenetic ties were seen in other cases supporting the relatively recent evolution of multiple segments, with the plant-infecting varicosavirus (two segments) and orchid fleck virus (bipartite) serving as informative examples.

In this context, it is notable that the newly discovered chuviruses fell ‘between’ the phylogenetic diversity of segmented and the unsegmented viruses. Although monophyletic, the chuviruses display a wide variety of genome organizations including unsegmented, bi-segmented, and a circular form, each of which appeared multiple times in the phylogeny (Figures 4, 7). The circular genomic form, which was confirmed by ‘around-the-genome’ RT-PCR and by the mapping of sequencing reads to the genome (Figure 7C), is a unique feature of the Chuviridae and can be distinguished from a pseudo-circular structure seen in some other negative-sense RNA viruses including the family Bunyaviridae and the family Orthomyxoviridae. Furthermore, this circular genomic form was also present in both segments of the segmented chuviruses (Figure 7B). In addition, the chuviruses displayed a diverse number and arrangement of predicted open reading frames that were markedly different from the genomic arrangement seen in the order Mononegavirales even though these viruses are relatively closely related (Figures 4, 7). In particular, the chuviruses had unique and variable orders of genes: the linear chuvirus genomes began with the glycoprotein (G) gene, followed by the nucleoprotein (N) gene, and then the polymerase (L) gene, whereas the majority of circular chuviruses were most likely arranged in the order L-(G)-N (i.e., if displayed in a linear form) as the only low coverage point throughout the genome lay between the 5′ end of N gene and the 3′ end of L gene (Figure 7B). In addition, the genome organizations of the chuviruses were far more concise than those of the order Mononegavirales, with ORFs encoding only 2–3 major (>20 kDa) proteins (Figure 7), and hence showing more similarity to segmented viruses in this respect.

![Figure 7.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig7-v2.jpg)

**Figure 7.:** (A) ML trees of three main putative proteins conserved among the chuviruses. Viruses with circular genomes (Type I) are shaded blue, while those with segmented genomes (Type II) are shaded red. (B) Structures of all complete chuvirus genomes. Circular genomes are indicated with the arrow (blue) situated at the 3′ end, and the genome is drawn in a linear form for ease of comparison only, being broken at the region of variable sequence (refer to the ‘Materials and methods’). (C) An example showing mapping of sequencing reads to the circular chuvirus genome. The template for mapping contains two genomes connected head-to-tail. The two boxes magnify the genomic region containing abundant sequence variation.

Although our phylogenetic analysis focused on the relatively conserved RdRp, in the case of segmented viruses we searched for other putative viral proteins from the assembled contigs. Accordingly, we were able to find the segments encoding matching structural proteins (mainly glycoproteins and nucleoproteins) for many of the viral RdRp sequences (Figure 8), although extensive sequence divergence prevented this in some cases. Surprisingly, M segments were apparently absent in a group of tick phleboviruses whose RdRps and nucleoproteins showed relatively high sequence similarity to Uukuniemi virus (genus Phlebovirus; Table 3 and Figure 8). Genomes with missing glycoprotein genes were also found in the chuviruses (Changping Tick Viruses 3 and 5, Wuhan Louse Viruses 6 and 7, Figure 7) and the unsegmented dimarhabdovirus (Taishun Tick Virus, Wuhan Tick Virus 1, Tacheng Tick Virus 6, Figure 9). Although it is possible that the glycoprotein gene may have been replaced with a highly divergent or even non-homologous sequence, we failed to find any candidate G proteins within the no-Blastx-hit set of sequences under the following criteria: (i) structural resemblance to G proteins, (ii) similar level of abundance to the corresponding RdRp and nucleoprotein genes, and (iii) comparable phylogenies or levels of divergence (among related viruses) to those of RdRps and nucleoproteins. The cause and biological significance of these seemingly ‘incomplete’ virus genomes require further study. Finally, it was also of interest that a virus with four segments was discovered in the horsefly pool. Although the predicted proteins of all four segments showed sequence homology to their counterparts in Tenuivirus (Falk and Tsai, 1998), this virus lacked the ambisense coding strategy of tenuiviruses (Figure 10). While the capability of this virus to infect plants is unknown, it is possible that it represents a transitional form between plant-infecting and arthropod-specific viruses.

![Figure 8.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig8-v2.jpg)

**Figure 8.:** Predicted viral proteins homologous to known viral proteins are shown and colored according to their putative functions. The numbers below each ORF box give the predicted molecular mass.

![Figure 9.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig9-v2.jpg)

**Figure 9.:** Predicted ORFs encoding viral proteins with >10 kDa molecular mass are shown and colored according to their putative functions. The numbers below each ORF box give the predicted molecular mass.

![Figure 10.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig10-v2.jpg)

### Novel Endogenous Virus Elements (EVEs)

As well as novel exogenous RNA viruses, our metagenomic analysis also revealed a large number of potential EVEs (Katzourakis and Gifford, 2010) in more than 40 arthropod species; these resembled complete or partial genes of the major proteins—the nucleoprotein, glycoprotein, and RdRp—but without fully intact genomes (Table 5). As expected given their endogenous status, most of these sequences have disrupted reading frames and many are found within transposon elements, suggesting that transposons have been central to their integration. Interestingly, in some cases, such as the putative glycoprotein gene of chuviruses, the homologous EVEs from within a family (Culicidae) or even an order (Hymenoptera) form monophyletic groups (Figure 11). However, they are unlikely to be orthologous because they do not share homologous integration sites in the host genome as determined by an analysis of flanking sequences, which in turn limited the applicability of molecular-clock based dating techniques. Furthermore, phylogenetic analyses of those EVEs shared among different host species revealed extremely complex tree topologies which do not exhibit simple matches to the host phylogeny at both the species and genera levels (Figure 11B–C). In sum, these results suggest that EVEs are relative commonplace in arthropod genomes and have been often generated by multiple and independent integration events.

**Table 5.**
 Summary of Endogenous Virus Elements (EVEs) determined here


<table>
  <thead>
    <tr>
      <th>Host classification</th>
      <th>Host name</th>
      <th>Virus classification</th>
      <th>Gene(s) present</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Chelicerata</td>
      <td rowspan="5">Ixodes scapularis</td>
      <td>Chuvirus</td>
      <td>G, N</td>
    </tr>
    <tr>
      <td>Dimarhabdovirus</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Nairovirus like</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Phlebovirus</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Quaranjavirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Tetranychus urticae</td>
      <td>Dimarhabdovirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td rowspan="6">Crustacea</td>
      <td>Daphnia pulex</td>
      <td>Phlebovirus like</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td rowspan="2">Eurytemora affinis</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Dimarhabdovirus</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td rowspan="2">Hyalella azteca</td>
      <td>Chuvirus</td>
      <td>G, N</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 3</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Lepeophtheirus salmonis</td>
      <td>Phlebovirus like</td>
      <td>N, G</td>
    </tr>
    <tr>
      <td rowspan="3">Insecta: Coleoptera</td>
      <td rowspan="2">Dendroctonus ponderosae</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Phasmavirus</td>
      <td>G, N</td>
    </tr>
    <tr>
      <td>Tribolium castaneum</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td rowspan="15">Insecta: Diptera</td>
      <td rowspan="5">Aedes aegypti</td>
      <td>Chuvirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Dimarhabdovirus</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Phasmavirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Phlebovirus like</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Quaranjavirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td rowspan="5">Anopheles spp.</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Dimarhabdovirus</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Phasmavirus</td>
      <td>G, N</td>
    </tr>
    <tr>
      <td>Phlebovirus like</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Quaranjavirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td rowspan="2">Culex quinquefasciatus</td>
      <td>Chuvirus</td>
      <td>G, N</td>
    </tr>
    <tr>
      <td>Dimarhabdovirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td rowspan="3">Drosophila spp.</td>
      <td>Dimarhabdovirus</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Phasmavirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Unclassified rhabdovirus 2</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td>Insecta: Isoptera</td>
      <td>Zootermopsis nevadensis</td>
      <td>Chuvirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td rowspan="7">Insecta: Hemiptera</td>
      <td rowspan="5">Acyrthosiphon pisum</td>
      <td>Chuvirus</td>
      <td>G, N</td>
    </tr>
    <tr>
      <td>Dimarhabdovirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Phlebovirus like</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Quaranjavirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 1</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td rowspan="2">Rhodnius prolixus</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Phasmavirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td rowspan="14">Insecta: Hymenoptera</td>
      <td>Atta cephalotes</td>
      <td>Unclassified mononegavirus 2</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td rowspan="2">Acromyrmex echinatior</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 2</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td rowspan="4">Camponotus floridanus</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 1</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 3</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Unclassified rhabdovirus 2</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Harpegnathos saltator</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Linepithema humile</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Nasonia spp.</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Pogonomyrmex barbatus</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td rowspan="3">Solenopsis invicta</td>
      <td>Chuvirus</td>
      <td>G</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 1</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Unclassified mononegavirus 3</td>
      <td>RdRp, N</td>
    </tr>
    <tr>
      <td rowspan="7">Insecta: Lepidoptera</td>
      <td rowspan="3">Bombyx mori</td>
      <td>Chuvirus</td>
      <td>RdRp, G</td>
    </tr>
    <tr>
      <td>Quaranjavirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Unclassified rhabdovirus 2</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td rowspan="2">Melitaea cinxia</td>
      <td>Dimarhabdovirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Quaranjavirus</td>
      <td>RdRp</td>
    </tr>
    <tr>
      <td>Plutella xylostella</td>
      <td>Dimarhabdovirus</td>
      <td>N, G</td>
    </tr>
    <tr>
      <td>Spodoptera frugiperda</td>
      <td>Phlebovirus like</td>
      <td>G</td>
    </tr>
    <tr>
      <td rowspan="2">Myriapoda</td>
      <td rowspan="2">Strigamia maritima</td>
      <td>Chuvirus</td>
      <td>N</td>
    </tr>
    <tr>
      <td>Phlebovirus like</td>
      <td>G</td>
    </tr>
  </tbody>
</table>

![Figure 11.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig11-v2.jpg)

**Figure 11.:** The phylogeny is based on the glycoprotein of chuviruses in the context of exogenous members of this family (A), with subtrees magnified for (B) the Culicidae clade and (C) the Hymenoptera clade. The EVEs used in the phylogeny covered the complete or near complete length of the glycoprotein gene and are shown in red and labeled according to host taxonomy in the overall tree. For clarity, monophyletic groups are collapsed based on the host taxonomy. Only bootstrap values >70% are shown.

## Discussion

Our study suggests that arthropods are major reservoir hosts for many, if not all, of the negative-sense RNA viruses in vertebrates and plants, and hence have likely played a major role in their evolution. This is further supported by the high abundance of viral RNA in the arthropod transcriptome, as well as by the high frequencies of endogenous copies of these viruses in the arthropod genome, greatly expanding the known biodiversity of these genomic ‘fossils’ (Katzourakis and Gifford, 2010; Cui and Holmes, 2012). The often basal position of the arthropod viruses in our phylogenetic trees is also compatible with the idea that the negative-sense RNA viruses found in vertebrates and plants ultimately have their ancestry in arthropods, although this will only be confirmed with a far wider sample of virus biodiversity.

The rich genetic and phylogenetic diversity of arthropod RNA viruses may in part reflect the enormous species number and diversity of arthropods, and that they sometimes live in large and very dense populations that provide abundant hosts to fuel virus transmission. Furthermore, arthropods are involved in almost all ecological guilds and actively interact with other eukaryotes, including animals, plants, and fungi, such that it is possible that they serve as both sources and sinks for viruses present in the environment. In addition, not only were diverse viruses present, but they were often highly abundant. For example, in the pool containing 12 individuals (representing two species) from the Gerridae (Water striders) collected at the same site, we identified at least five negative-sense RNA viruses whose TPM values are well above 100, and where the viral RNA collectively made up more than 50% of the host total RNA (rRNA excluded). Determining why arthropods are able to carry such a large viral diversity and at such frequencies clearly merits further investigation.

The viruses discovered here also exhibited a huge variation in level of abundance. It is possible that this variation is in part due to the stage or severity of infection in individual viruses and may be significantly influenced by the process of pooling, since most of our libraries contain an uneven mixture of different host species or even genera. In addition, it is possible that some low abundance viruses may in fact be derived from other eukaryotic organisms present in the host sampled, such as undigested food or prey, gut micro flora, and parasites. Nevertheless, since the majority of the low abundance viruses appear in the same groups as the highly abundant ones in our phylogenetic analyses, these viruses are most likely associated with arthropods.

Viral infections in vertebrates and plants can be divided into two main categories: (i) arthropod-dependent infections, in which there is spill-over to non-arthropods but where continued virus transmission still requires arthropods, and (ii) arthropod-independent infections, in which the virus has shifted its host range to circulate among vertebrates exclusively (Figure 12). The first category of infections is often associated with major vector-borne diseases (Zhang et al., 2011, 2012). Given the biodiversity of arthropod viruses documented here, it seems likely that arthropod-independent viruses were ultimately derived from arthropod-dependent infections, with subsequent adaptation to vertebrate-only transmission (Figure 12).

![Figure 12.](https://cdn.elifesciences.org/articles/05378/elife-05378-fig12-v2.jpg)

**Figure 12.:** Three types of transmission cycle are shown: (i) those between arthropods and plants are shaded green; (ii) those between arthropods and vertebrates are shaded yellow; and (iii) those that are vertebrate-only are shaded red. Viruses associated with each transmission type are also indicated.

One of the most notable discoveries was that of a novel family, the Chuviridae. The identification of this diverse virus family provides a new perspective on the evolutionary origins of segmented and unsegmented viruses. In particular, the chuviruses occupy a phylogenetic position that is in some sense ‘intermediate’ between the segmented and unsegmented negative-sense RNA viruses and display genomic features of both. Indeed, our phylogenetic analysis reveals that genome segmentation has evolved multiple times within the diversity of chuviruses (Figure 7), such that this trait appears to be more flexible than previously anticipated. In addition, the majority of the chuviruses possess circular genomes. To date, the only known circular RNA virus is (hepatitis) deltavirus, although this potentially originated from the human genome (Salehi-Ashtiani et al., 2006) and requires hepatitis B virus for successful replication. As such, the chuviruses may represent the first report of autonomously replicating circular RNA viruses, which opens up an important line of future research.

Our results also provide insights into the evolution of genome segmentation. Within the bunya-arena-like viruses (Figures 3C, 4), the three-segment structure is the most common, with the viral polymerase, nucleoprotein, and surface glycoproteins present on different segments. Notably, our phylogenetic analysis seemingly revealed independent occurrences of both increasing (Tenuivirus and Emaravirus) and decreasing (Arenavirus) segment numbers from the three-segment form (Figure 4). Independent changes of genome segmentation numbers are also observed in the mononegavirales-like viruses (Figure 4) and, more frequently, in the chuviruses (Figure 7A). Consequently, the number of genome segments appears to be a relatively flexible trait at a broad evolutionary scale, although the functional relevance of these changes remains unclear. While the segmented viruses (bunya-arenaviruses, orthomyxoviruses, and ophioviruses) appear to be distinct from the largely unsegmented mononegavirales-like viruses in our phylogenetic analysis, this may be an artifact of under-sampling, especially given that only a tiny fraction of eukaryotes have been sampled to date. With a wider sample of eukaryotic viruses it will be possible to more accurately map changes in segment number onto phylogenetic trees and in so doing come to a more complete understanding of the patterns and determinants of the evolution of genome segmentation.

In sum, our results highlight the remarkable diversity of arthropod viruses. Because arthropods interact with a wide range of organisms including vertebrate animals and plants, they can be seen as the direct or indirect source of many clinically or economically important viruses. The viral genetic and phenotypic diversity documented in arthropods here therefore provides a new perspective on fundamental questions of virus origins, diversity, host range, genome evolution, and disease emergence.

## Materials and methods

### Sample collection

Between 2011 and 2013 we collected 70 species of arthropods from various locations in China (Table 1). Among these, ticks were either directly picked from wild and domestic animals or captured using a tick drag-flag method; mosquitoes were trapped by light-traps; common flies were captured by fly paper; horseflies were picked from infested cattle; bed bugs and cockroaches were trapped indoors; louse flies were plucked from the skin of bats; millipedes were picked up from the ground; spiders were collected from their webs; water striders were captured using hand nets from river surfaces; and crabs and shrimps were bought (alive) from local fisherman. In addition, three pools of mixed insect samples (Table 1) were collected from a rural area adjacent to rice fields (Insect Mix 1), from a lakeside (Insect Mix 3), and from a mountainous area near Wuhan (Insect Mix 4). After brief species identification by experienced field biologists, these samples were immediately stored in liquid nitrogen and were later put on dry ice for shipment to our laboratory.

### Total RNA extraction

The specimens were first grouped into several units (Table 1). Depending on the size of specimens, one unit could include from 1 to 20 individual arthropods belonging to the same species and sampling location. These units were first washed with phosphate-buffered saline (PBS) three times before homogenized with the Mixer mill MM400 (Restsch, Germany). The resultant homogenates were then subjected to RNA extraction using TRIzol LS reagent (Invitrogen, Carlsbad, CA). After obtaining the aqueous phase containing total RNA, we performed purification steps from the E.Z.N.A Total RNA Kit (OMEGA, Portugal) according to the manufacturer's instructions. The concentration and quality of final extractions were examined using a ND-1000 UV spectrophotometer (Nanodrop, Wilmington, DE). Based on host types and/or geographic locations, these extractions were further merged into 16 pools for RNA-seq library construction and sequencing (Table 1).

### Species identification

To verify the field species identification, we took a proportion of the homogenates from each specimen or specimen pool for genomic DNA extraction using E.Z.N.A. DNA/RNA Isolation Kit (OMEGA). Two genes were used for host identification: the partial 18S rRNA gene (∼1100 nt) which was amplified using primer pairs 18S#1 (5′-CTGGTGCCAGCGAGCCGCGGYAA-3′) and 18S#2RC (5′-TCCGTCAATTYCTTTAAGTT-3′) and partial COI gene (∼680 nt) using primer pairs LCO1490 (5′-GGTCAACAAATCATAAAGATATTGG-3′) and HCO2198 (5′-TAAACTTCAGGGTGACCAAAAAATCA-3′). PCRs were performed as described previously (Folmer et al., 1994; Machida and Knowlton, 2012). For taxonomic determination, the resulting sequences were compared against the nt database as well as with all COI barcode records on the Barcode of Life Data Systems (BOLD).

### RNA-seq sequencing and reads assembly

Total RNA was subjected to a slightly modified RNA-seq library preparation protocol from that provided by Illumina. Briefly, following DNase I digestion, total RNA was subjected to an rRNA removal step using Ribo-Zero Magnetic Gold Kit (Epicentre, Madison, WI). The remaining RNA was then fragmented, reverse-transcribed, ends repaired, dA-tailed, adaptor ligated, purified, and quantified with Agilent 2100 Bioanalyzer and ABI StepOnePlus Real-Time PCR System. Pair-end (90 bp or 100 bp) sequencing of the RNA library was performed on the HiSeq 2000 platform (Illumina, San diego, CA). All library preparation and sequencing steps were performed by BGI Tech (Shenzhen, China). The resulting sequencing reads were quality trimmed and assembled de novo using the Trinity program (Grabherr et al., 2011). All sequence reads generated in this study were uploaded onto NCBI Sequence Read Achieve (SRA) database under the BioProject accession SRP051790.

### Discovery of target virus sequences

The assembled contigs were translated and compared (using Blastx) to reference protein sequences of all negative-sense RNA viruses. Sequences yielding e-values larger than 1e−5 were retained and compared to the entire nr database to exclude non-viral sequences. The resulting viral sequences were merged by identifying unassembled overlaps between neighboring contigs or within a scaffold using the SeqMan program implemented in the Lasergene software package v7.1 (DNAstar, Madison, WI). To prevent missing highly divergent viruses, the newly found viral sequences were included in the reference protein sequences for a second round of Blastx.

### Sequence confirmation and repairing by Sanger methods

For each potential viral sequence, we first used nested RT-PCR to examine which unit contained the target sequence, utilizing primers designed based on the deep-sequencing results. In the case of segmented viruses this information was also used to determine whether and which of the segments recovered from the pool belonged to the same virus. We next designed overlapping primers to verify the sequence obtained from the deep sequencing and assembly processes. Based on the verified sequences, we determined the sequencing depth and coverage by mapping reads to target sequences using bowtie2 (Langmead and Salzberg, 2012). All virus genome sequences generated in this study have been deposited in the GenBank database under accession numbers KM817593–KM817764‏.

### Quantification of relative transcript abundances

Before quantification, we first removed the rRNA reads from the data sets to prevent any bias due to the unequal efficiency of rRNA removal steps during library preparation. To achieve this, we blasted the Trinity assembly results against the SILVER rRNA database (Quast et al., 2013) and then used the resulting rRNA contigs as a template for mapping using BOWTIE2 (Langmead and Salzberg, 2012). The remaining reads from each library were then mapped on to the assembled transcripts and analyzed with RSEM (Li et al., 2010), using the run_RSEM_align_n_estimate.pl scripts implemented in the Trinity program (Grabherr et al., 2011). The relative abundance of each transcript is presented as transcripts per million (TPM) which corrects for the total number of reads as well as for transcript length (Li et al., 2010).

### Genome walking

Some of the sequences obtained were substantially shorter than expected. To obtain longer sequences, we used a Genome walking kit (TaKaRa, Japan). Briefly, three gene-specific primers close to the end of the known sequence were designed. RNA from positive samples was used as input for reverse transcription primed by random primer N6. TAIL-PCR (thermal asymmetric interlaced PCR) was performed according to the manufacturer's protocol. The cDNA was used as a template for PCR with specific primers and the manufacturer-supplied degenerate primers. After three rounds of amplification, the products were analyzed on 1.0% agarose gels, and single fragments were recovered from the gels and purified using an agarose gel DNA extraction kit (TaKaRa). The purified products were then ligated into pMD19-T vector (TaKaRa) which contains the gene for ampicillin resistance. The vector was transformed into DH5α cells, which were spread on agar plates and incubated overnight at 37°C. A total of 10 clones were randomly selected and sequenced using M13 primers on ABI 3730 genetic analyzer (Applied Biosystems, Carlsbad, CA).

### Determination of genome/segment termini

The extreme 5′ sequences were recovered by performing a 5′-Full RACE kit with TAP (TaKaRa) according to the manufacturer's protocol. Briefly, two gene-specific primers close to the end of the known sequence were designed. The 5′ end of RNA was ligated to the 5′RACE adaptor (without 5′ end dephosphorylating and decapping) and then reverse-transcribed using random 9 mers. The resulting cDNA was used as a template for nested PCR with 5′ RACE primers provided by the kit and gene-specific reverse primers. The PCR products were separated on an agarose gel, cloned into pMD19-T cloning vector, and subsequently sequenced.

The extreme 3′ sequences were recovered by performing a 3′-full RACE Core Set with PrimeScript RTase (TaKaRa) according to the manufacturer's protocols. Because the RNA template lacks a polyadenylated tail, a Poly(A) Tailing Kit (Applied Biosystems) was used to add this to the RNAs prior to first-strand 3′-cDNA synthesis. 20 μl of the Poly(A)-tailing reaction mixture was prepared according to the manufacturer's instructions and was incubated at 37°C for 1 hr before reverse transcription using PrimeScript Reverse Transcriptase. The cDNA was then amplified by nested PCR using the 3′ RACE primers provided by the kit and gene-specific reverse primers. The PCR products were separated on agarose gels, cloned into pMD19-T cloning vector, and subsequently sequenced. The 5′ and 3′ ends of the genome fragment were also determined by RNA circularization. RT-PCR amplification was performed across the ligated termini and the resulting PCR products were subsequently cloned and sequenced.

### Phylogenetic analyses

Potential viral proteins identified from this study were aligned with their corresponding homologs of reference negative-sense RNA viruses using MAFFT version 7 and employing the E-INS-i algorithm (Katoh and Standley, 2013). The sequence alignment was limited to conserved domains, with ambiguously aligned regions removed using TrimAl (Capella-Gutierrez et al., 2009). The final alignment lengths were 224 amino acids (aa), 412aa, 727aa, and 364aa for data sets of overall, bunya-arena-like, mononega-like, and orthomyxo-like data sets, respectively. Phylogenetic trees were inferred using the maximum likelihood method (ML) implemented in PhyML version 3.0 (Guindon and Gascuel, 2003), with the WAG + Γ amino acid substitution model and a Subtree Pruning and Regrafting (SPR) topology searching algorithm. Phylogenetic trees were also inferred using a Bayesian method implemented in MrBayes version 3.2.2 (Ronquist and Huelsenbeck, 2003), with the same substitution model as used in ML tree inference. In the MrBayes analyses, we used two simultaneous runs of Markov chain Monte Carlo sampling, and the runs were terminated upon convergence (standard deviation of the split frequencies <0.01). The phylogeny was subsequently summarized from both runs with an initial 10% of trees discarded as burn-in.

### Prediction of protein domains and functions

For each of the putative viral protein sequences, we used TMHMM v2.0 (http://www.cbs.dtu.dk/services/TMHMM/) to predict the transmembrane domains, SignalP v4.0 (http://www.cbs.dtu.dk/services/SignalP/) to determine signal sequences, and NetNGlyc v1.0 (http://www.cbs.dtu.dk/services/NetNGlyc/) to identify N-linked glycosylation sites. For some of the highly divergent viruses belonging to the Mononegavirales and the Chuviridae, a protein was regarded as a potential glycoprotein if it contained (i) a N-terminal signal domain, (ii) a C-terminal transmembrane domain, and (iii) glycosylation sites in cytoplasmic domains.

### Identification and characterization of endogenous viruses

Endogenous copies of the exogenous negative-sense RNA viruses newly described here were detected using the tBlastn algorithm against arthropod genomes available in the Reference Genomic Sequences Database (refseq_genomic) and Whole Genome Shotgun Database (WGS) in GenBank, and using viral amino acid sequences as queries. The threshold for match was set to 1e−05 for the e-value and 50 amino acids for matched length. The query process was reversed for each potential endogenous virus to determine their corresponding phylogenetic group. Orthologous insertion events were determined by examining flanking gene sequences. Sequence alignment and phylogenetic analyses were carried out as described above.

### Characterization of bi-segmented viruses in the Chuviridae

Within the Chuviridae, Wuhan Louse Fly Virus 6 and 7, Wenzhou Crab Virus 2, Lishi Spider Virus 1, and Wuchang Cockroach Virus 3 possessed bi-segmented genomes.

Both segments were discovered using Blastx against pools of predicted proteins from unsegmented chuvirus or mononegavirales sequences. To determine that these sequences were indeed from separate segments, we performed all combinations of head-to-tail RT-PCR which allowed us to ascertain whether the sequence fragments came from a single genome. Furthermore, checking sequencing depth can help to eliminate the possibility of separate contigs being generated due to inadequate sequencing coverage. To prove that a pair of segments belonged to the same virus, we checked: (i) sequencing depth for both segments, (ii) the presence of conserved regulatory sequences at non-coding regions of the genome, (iii) whether there is match for PCR-positive units, and (iv) the phylogenetic positions of the different viral proteins (Figure 7A).

### Characterization of a circular genome form within the Chuviridae

The circular genome organization within the Chuviridae was identified after we found that their genome sequences were ‘over assembled’ (i.e., generating contigs that contained more than one genome connected head-to-tail). This circular genomic form was also observed in both segments of the segmented chuviruses (Figure 7B). In addition, RT-PCR and sequencing over the entire genome did not reveal any break-points. As a control, the same protocol failed to connect the genome termini within the Mononegavirales, suggesting the circular genomic form is unique to the chuviruses. To further validate that these genomes are circular, we mapped the high-throughput sequencing reads to these assembled genomes. The coverage and depth were adequate throughout the genome with the exception of one location upstream to the 3′ end of the ORF encoding RdRp (Figure 7C). This genomic location had only 0–20 X coverage depending on the virus, although all RT-PCRs were successful across this location. Interestingly, sequencing of the cloned PCR products revealed extensive sequence variation (i.e., insertions and deletions) (Figure 7C), which is the likely cause of the low sequence coverage in this location. Collectively, these data provide strong evidence for circular genomes in the chuviruses, although this does not exclude the potential presence of linear genomic forms.
