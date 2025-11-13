# Ribosomal RNA (rRNA) sequences from 33 globally distributed mosquito species for improved metagenomics and species identification

## Authors

- Cassandra Koh<sup>1</sup> ([ORCID: 0000-0003-2466-6731](https://orcid.org/0000-0003-2466-6731)) †
- Lionel Frangeul<sup>1</sup>
- Hervé Blanc<sup>1</sup>
- Carine Ngoagouni<sup>2</sup>
- Sébastien Boyer<sup>3</sup>
- Philippe Dussart<sup>4</sup> ([ORCID: 0000-0002-1931-3037](https://orcid.org/0000-0002-1931-3037))
- Nina Grau<sup>5</sup>
- Romain Girod<sup>5</sup>
- Jean-Bernard Duchemin<sup>6</sup>
- Maria-Carla Saleh<sup>1</sup> ([ORCID: 0000-0001-8593-4117](https://orcid.org/0000-0001-8593-4117)) †

### Affiliations

1. Institut Pasteur, Université Paris Cité, CNRS UMR3569, Viruses and RNA Interference Unit, F-75015 Paris France ([ROR:02feahw73](https://ror.org/02feahw73))
2. Institut Pasteur de Bangui, Medical Entomology Laboratory Bangui Central African Republic ([ROR:01ee94y34](https://ror.org/01ee94y34))
3. Institut Pasteur du Cambodge, Medical and Veterinary Entomology Unit Phnom Penh Cambodia ([ROR:03ht2dx40](https://ror.org/03ht2dx40))
4. Institut Pasteur du Cambodge, Virology Unit Phnom Penh Cambodia ([ROR:03ht2dx40](https://ror.org/03ht2dx40))
5. Institut Pasteur de Madagascar, Medical Entomology Unit Antananarivo Madagascar ([ROR:03fkjvy27](https://ror.org/03fkjvy27))
6. Institut Pasteur de la Guyane, Vectopôle Amazonien Emile Abonnenc Cayenne French Guiana ([ROR:01fp8z436](https://ror.org/01fp8z436))

† Corresponding author

## Abstract

Total RNA sequencing (RNA-seq) is an important tool in the study of mosquitoes and the RNA viruses they vector as it allows assessment of both host and viral RNA in specimens. However, there are two main constraints. First, as with many other species, abundant mosquito ribosomal RNA (rRNA) serves as the predominant template from which sequences are generated, meaning that the desired host and viral templates are sequenced far less. Second, mosquito specimens captured in the field must be correctly identified, in some cases to the sub-species level. Here, we generate mosquito rRNA datasets which will substantially mitigate both of these problems. We describe a strategy to assemble novel rRNA sequences from mosquito specimens and produce an unprecedented dataset of 234 full-length 28S and 18S rRNA sequences of 33 medically important species from countries with known histories of mosquito-borne virus circulation (Cambodia, the Central African Republic, Madagascar, and French Guiana). These sequences will allow both physical and computational removal of rRNA from specimens during RNA-seq protocols. We also assess the utility of rRNA sequences for molecular taxonomy and compare phylogenies constructed using rRNA sequences versus those created using the gold standard for molecular species identification of specimens—the mitochondrial cytochrome c oxidase I (COI) gene. We find that rRNA- and COI-derived phylogenetic trees are incongruent and that 28S and concatenated 28S+18S rRNA phylogenies reflect evolutionary relationships that are more aligned with contemporary mosquito systematics. This significant expansion to the current rRNA reference library for mosquitoes will improve mosquito RNA-seq metagenomics by permitting the optimization of species-specific rRNA depletion protocols for a broader range of species and streamlining species identification by rRNA sequence and phylogenetics.

## Introduction

Mosquitoes top the list of vectors for arthropod-borne diseases, being implicated in the transmission of many human pathogens responsible for arboviral diseases, malaria, and lymphatic filariasis (WHO, 2017). Mosquito-borne viruses circulate in sylvatic (between wild animals) or urban (between humans) transmission cycles driven by different mosquito species with their own distinct host preferences. Although urban mosquito species are chiefly responsible for amplifying epidemics in dense human populations, sylvatic mosquitoes maintain the transmission of these viruses among forest-dwelling animal reservoir hosts and are involved in spillover events when humans enter their ecological niches (Valentine et al., 2019). Given that mosquito-borne virus emergence is preceded by such spillover events, continuous surveillance and virus discovery in sylvatic mosquitoes is integral to designing effective public health measures to pre-empt or respond to mosquito-borne viral epidemics.

Metagenomics on field specimens is a powerful method in our toolkit to understand mosquito-borne disease ecology through the One Health lens (Webster et al., 2016). With next-generation sequencing becoming more accessible, such studies have provided unprecedented insights into the interfaces among mosquitoes, their environment, and their animal and human hosts. As mosquito-associated viruses are mostly RNA viruses, RNA sequencing (RNA-seq) is especially informative for surveillance and virus discovery. However, working with lesser studied mosquito species poses several problems.

First, metagenomics studies based on RNA-seq are bedevilled by overabundant ribosomal RNAs (rRNAs). These non-coding RNA molecules comprise at least 80% of the total cellular RNA population (Gale and Crampton, 1989). Due to their length and their abundance, they are a sink for precious next-generation sequencing reads, decreasing the sensitivity of pathogen detection unless depleted during library preparation. Yet the most common rRNA depletion protocols require prior knowledge of rRNA sequences of the species of interest as they involve hybridizing antisense oligos to the rRNA molecules prior to removal by ribonucleases (Fauver et al., 2019; Phelps et al., 2021) or by bead capture (Kukutla et al., 2013). Presently, reference sequences for rRNAs are limited to only a handful of species from three genera: Aedes, Culex, and Anopheles (Ruzzante et al., 2019). The lack of reliable rRNA depletion methods could deter mosquito metagenomics studies from expanding their sampling diversity, resulting in a gap in our knowledge of mosquito vector ecology. The inclusion of lesser studied yet medically relevant sylvatic species is therefore imperative.

Second, species identification based on morphology is notoriously complicated for members of certain species subgroups. This is especially the case among Culex subgroups. Sister species are often sympatric and show at least some competence for a number of viruses, such as Japanese encephalitis virus, St Louis encephalitic virus, and Usutu virus (Nchoutpouen et al., 2019). Although they share many morphological traits, each of these species have distinct ecologies and host preferences, thus the challenge of correctly identifying vector species can affect epidemiological risk estimation for these diseases (Farajollahi et al., 2011). DNA molecular markers are often employed to a limited degree of success to distinguish between sister species (Batovska et al., 2017; Zittra et al., 2016).

To address the lack of full-length rRNA sequences in public databases, we sought to determine the 28S and 18S rRNA sequences of a diverse set of Old and New World sylvatic mosquito species from four countries representing three continents: Cambodia, the Central African Republic, Madagascar, and French Guiana. These countries, due to their proximity to the equator, contain high mosquito biodiversity (Foley et al., 2007) and have had long histories of mosquito-borne virus circulation (Desdouits et al., 2015; Halstead, 2019; Héraud et al., 2022; Jacobi and Serie, 1972; Ratsitorahina et al., 2008; Saluzzo et al., 2017; Zeller et al., 2016). Increased and continued surveillance of local mosquito species could lead to valuable insights on mosquito virus biogeography. Using a unique score-based read filtration strategy to remove interfering non-mosquito rRNA reads for accurate de novo assembly, we produced a dataset of 234 novel full-length 28S and 18S rRNA sequences from 33 mosquito species, 30 of which have never been recorded before.

We also explored the functionality of 28S and 18S rRNA sequences as molecular markers by comparing their performance to that of the mitochondrial cytochrome c oxidase subunit I (COI) gene for molecular taxonomic and phylogenetic investigations. The COI gene is the most widely used DNA marker for molecular species identification and forms the basis of the Barcode of Life Data System (BOLD) (Hebert et al., 2003; Ratnasingham and Hebert, 2007). Presently, full-length rRNA sequences are much less represented compared to other molecular markers. However, given the availability of relevant reference sequences, 28S and concatenated 28S+18S rRNA sequences can be the better approach for molecular taxonomy and phylogenetic studies. We hope that our sequence dataset, with its species diversity and eco-geographical breadth, and the assembly strategy we describe would further facilitate the use of rRNA as markers. In addition, this dataset enables the design of species-specific oligos for cost-effective rRNA depletion for a broader range of mosquito species and streamlined molecular species identification during RNA-seq.

## Results

### Poor rRNA depletion using a non-specific depletion method

During library preparations of mosquito samples for RNA-seq, routinely used methods for depleting rRNA are commercial kits optimised for human or mice samples (Belda et al., 2019; Bishop-Lilly et al., 2010; Chandler et al., 2015; Kumar et al., 2012; Weedall et al., 2015; Zakrzewski et al., 2018) or through 80–100 base pair antisense probe hybridisation followed by ribonuclease digestion (Fauver et al., 2019; Phelps et al., 2021). In cases where the complete reference rRNA sequence of the target species is not known, oligos would be designed based on the rRNA sequence of the closest related species (25, this study). These methods should deplete reads from the conserved regions of rRNA sequences. However, reads from the variable regions remain at abundances high enough to compromise RNA-seq output. In our hands, we have found that using probes designed for the Ae. aegypti rRNA sequence followed by RNase H digestion according to the protocol published by Morlan et al., 2012, produced poor depletion in Aedes albopictus, and in Culicine and Anopheline species (Figure 1), in which between 46% and 94% of reads post-depletion were ribosomal. Additionally, the lack of full-length reference rRNA sequences compromises the in silico clean-up of remaining rRNA reads from sequencing data, as reads belonging to variable regions would not be removed. To solve this and to enable RNA-seq metagenomics on a broader range of mosquito species, we performed RNA-seq to generate reference rRNA sequences for 33 mosquito species representing 10 genera from Cambodia, the Central African Republic, Madagascar, and French Guiana. Most of these species are associated with vector activity for various pathogens in their respective ecologies (Table 1). In parallel, we sequenced the mitochondrial COI gene to perform molecular species identification of our samples and to comparatively evaluate the use of rRNA as a molecular marker (Figure 2).

![Figure 1.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig1-v2.jpg)

**Figure 1.:** Pools of five individual mosquitoes from genera Aedes (Ae), Culex (Cx), Mansonia (Ma), and Anopheles (An) were ribodepleted by probe hybridisation followed by RNase H digestion according to the protocol by Morlan et al., 2012. Y-axis depicts percentages of remaining rRNA reads calculated as the number of rRNA reads over total reads per sample pool. Depletion efficiency decreases with taxonomic distance from Ae. aegypti underlining the need for reference sequences for species of interest.

**Table 1.**
 Mosquito species represented in this study and their vector status.


<table>
  <thead>
    <tr>
      <th>Mosquito taxonomy‡</th>
      <th>Origin*</th>
      <th>Collection site (ecosystem type)</th>
      <th>Vector for†</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aedes (Fredardsius) vittatus</td>
      <td>CF</td>
      <td>Rural (village)</td>
      <td>ZIKV, CHIKV, YFV</td>
      <td>Diallo et al., 2020</td>
    </tr>
    <tr>
      <td>Aedes (Ochlerotatus) scapularis</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>YFV</td>
      <td>Vasconcelos et al., 2001</td>
    </tr>
    <tr>
      <td>Aedes (Ochlerotatus) serratus</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>YFV, OROV</td>
      <td>Cardoso et al., 2010; Romero-Alvarez and Escobar, 2018</td>
    </tr>
    <tr>
      <td>Aedes (Stegomyia) aegypti</td>
      <td>CF</td>
      <td>Urban</td>
      <td>DENV, ZIKV, CHIKV, YFV</td>
      <td>Kraemer et al., 2019</td>
    </tr>
    <tr>
      <td>Aedes (Stegomyia) albopictus</td>
      <td>CF, KH</td>
      <td>Rural (village, nature reserve)</td>
      <td>DENV, ZIKV, CHIKV, YFV, JEV</td>
      <td>Auerswald et al., 2021; Kraemer et al., 2019</td>
    </tr>
    <tr>
      <td>Aedes (Stegomyia) simpsoni</td>
      <td>CF</td>
      <td>Rural (village)</td>
      <td>YFV</td>
      <td>Mukwaya et al., 2000</td>
    </tr>
    <tr>
      <td>Anopheles (Anopheles) baezai</td>
      <td>KH</td>
      <td>Rural (nature reserve)</td>
      <td>Unreported</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Anopheles (Anopheles) coustani</td>
      <td>MG, CF</td>
      <td>Rural (village)</td>
      <td>RVFV, malaria</td>
      <td>Mwangangi et al., 2013; Nepomichene et al., 2018; Ratovonjato et al., 2011</td>
    </tr>
    <tr>
      <td>Anopheles (Cellia) funestus</td>
      <td>MG, CF</td>
      <td>Rural (village)</td>
      <td>ONNV, malaria</td>
      <td>Lutomiah et al., 2013; Tabue et al., 2017</td>
    </tr>
    <tr>
      <td>Anopheles (Cellia) gambiae</td>
      <td>MG, CF</td>
      <td>Rural (village)</td>
      <td>ONNV, malaria</td>
      <td>Brault et al., 2004</td>
    </tr>
    <tr>
      <td>Anopheles (Cellia) squamosus</td>
      <td>MG</td>
      <td>Rural (village)</td>
      <td>RVFV, malaria</td>
      <td>Ratovonjato et al., 2011; Stevenson et al., 2016</td>
    </tr>
    <tr>
      <td>Coquillettidia (Rhynchotaenia) venezuelensis</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>OROV</td>
      <td>Travassos da Rosa et al., 2017</td>
    </tr>
    <tr>
      <td>Culex (Culex) antennatus</td>
      <td>MG</td>
      <td>Rural (village)</td>
      <td>RVFV</td>
      <td>Nepomichene et al., 2018; Ratovonjato et al., 2011</td>
    </tr>
    <tr>
      <td>Culex (Culex) duttoni</td>
      <td>CF</td>
      <td>Rural (village)</td>
      <td>Unreported</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Culex (Culex) neavei</td>
      <td>MG</td>
      <td>Rural (village)</td>
      <td>USUV</td>
      <td>Nikolay et al., 2011</td>
    </tr>
    <tr>
      <td>Culex (Culex) orientalis</td>
      <td>KH</td>
      <td>Rural (nature reserve)</td>
      <td>JEV</td>
      <td>Kim et al., 2015</td>
    </tr>
    <tr>
      <td>Culex (Culex) perexiguus</td>
      <td>MG</td>
      <td>Rural (village)</td>
      <td>WNV, USUV</td>
      <td>Vezenegho et al., 2022</td>
    </tr>
    <tr>
      <td>Culex (Culex) pseudovishnui</td>
      <td>KH</td>
      <td>Rural (nature reserve)</td>
      <td>JEV</td>
      <td>Auerswald et al., 2021</td>
    </tr>
    <tr>
      <td>Culex (Culex) quinquefasciatus</td>
      <td>MG, CF, KH</td>
      <td>Rural (village, nature reserve)</td>
      <td>ZIKV, JEV, WNV, DENV, SLEV, RVFV, Wuchereria bancrofti</td>
      <td>Bhattacharya and Basu, 2016; Maquart et al., 2021; Ndiaye et al., 2016; Serra et al., 2016</td>
    </tr>
    <tr>
      <td>Culex (Culex) tritaeniorhynchus</td>
      <td>MG, KH</td>
      <td>Rural (village, nature reserve)</td>
      <td>JEV, WNV, RVFV</td>
      <td>Auerswald et al., 2021; Hayes et al., 1980; Jupp et al., 2002</td>
    </tr>
    <tr>
      <td>Culex (Melanoconion) spissipes</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>VEEV</td>
      <td>Weaver et al., 2004</td>
    </tr>
    <tr>
      <td>Culex (Melanoconion) portesi</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>VEEV, TONV</td>
      <td>Talaga et al., 2021; Weaver et al., 2004</td>
    </tr>
    <tr>
      <td>Culex (Melanoconion) pedroi</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>EEEV, VEEV, MADV</td>
      <td>Talaga et al., 2021; Turell et al., 2008</td>
    </tr>
    <tr>
      <td>Culex (Oculeomyia) bitaeniorhynchus</td>
      <td>MG, KH</td>
      <td>Rural (village, nature reserve)</td>
      <td>JEV</td>
      <td>Auerswald et al., 2021</td>
    </tr>
    <tr>
      <td>Culex (Oculeomyia) poicilipes</td>
      <td>MG</td>
      <td>Rural (village)</td>
      <td>RVFV</td>
      <td>Ndiaye et al., 2016</td>
    </tr>
    <tr>
      <td>Eretmapodites intermedius</td>
      <td>CF</td>
      <td>Rural (village)</td>
      <td>Unreported</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Limatus durhamii</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>ZIKV</td>
      <td>Barrio-Nuevo et al., 2020</td>
    </tr>
    <tr>
      <td>Mansonia (Mansonia) titillans</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>VEEV, SLEV</td>
      <td>Hoyos-López et al., 2015; Turell, 1999</td>
    </tr>
    <tr>
      <td>Mansonia (Mansonioides) indiana</td>
      <td>KH</td>
      <td>Rural (nature reserve)</td>
      <td>JEV</td>
      <td>Arunachalam et al., 2004</td>
    </tr>
    <tr>
      <td>Mansonia (Mansonioides) uniformis</td>
      <td>MG, CF, KH</td>
      <td>Rural (village, nature reserve)</td>
      <td>RVFV, Wuchereria bancrofti</td>
      <td>Lutomiah et al., 2013; Ughasi et al., 2012</td>
    </tr>
    <tr>
      <td>Mimomyia (Etorleptiomyia) mediolineata</td>
      <td>MG</td>
      <td>Rural (village)</td>
      <td>Unreported</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Psorophora (Janthinosoma) ferox</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>ROCV</td>
      <td>Mitchell et al., 1986</td>
    </tr>
    <tr>
      <td>Uranotaenia (Uranotaenia) geometrica</td>
      <td>GF</td>
      <td>Rural (village)</td>
      <td>Unreported</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_*Dengue virus, DENV; Zika virus, ZIKV; chikungunya virus, CHIKV; Yellow Fever virus, YFV; Oropouche virus, OROV; Japanese encephalitis virus, JEV; Rift Valley Fever virus, RVFV; O’Nyong Nyong virus, ONNV; Usutu virus, USUV; West Nile virus, WNV; St Louis encephalitis virus, SLEV; Venezuelan equine encephalitis virus, VEEV; Tonate virus, TONV; Eastern equine encephalitis virus, EEEV; Madariaga virus, MADV; Rocio virus, ROCV.†Origin countries are listed as their ISO alpha-2 codes: Central African Republic, CF; Cambodia, KH; Madagascar, MG; French Guiana, GF.‡Subgenus indicated in brackets._

![Figure 2.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of sequencing and bioinformatics analyses performed in this study to obtain full-length 18S and 28S rRNA sequences as well as cytochrome c oxidase I (COI) DNA sequences. Nucleic acids were isolated from mosquito specimens for next-generation (for rRNA) or Sanger (for COI) sequencing. Two in-house libraries were created from the SILVA rRNA gene database: Insecta and Non-Insecta, which comprises 8,585 sequences and 558,185 sequences, respectively. Following BLASTn analyses against these two libraries, each RNA-sequencing (RNA-seq) read is assigned a ratio of BLASTn scores to describe their relative nucleotide similarity to insect rRNA sequences. Based on these ratios of scores, RNA-seq reads can then be filtered to remove non-mosquito reads prior to assembly with SPAdes to give full-length 18S and 28S rRNA sequences. Image created with https://biorender.com/. (B) Based on their ratio of scores, reads can be segregated into four categories, as shown on this ratio of scores versus number of reads plot for the representative specimen ‘CF S27’: (i) reads with hits only in the Insecta library (shaded in green), (ii) reads with a higher score against the Insecta library (shaded in blue), (iii) reads with a higher score against the Non-Insecta library (shaded in yellow), and (iv) reads with no hits in the Insecta library (shaded in red). We applied a conservative threshold at 0.8, indicated by the black horizontal line, where only reads above this threshold are used in the assembly with SPAdes. For this given specimen, 175,671 reads (96.3% of total reads) passed the ≥0.8 cut-off, 325 reads (0.18% of total reads) had ratios of scores <0.8, while 6,423 reads (3.52%) did not have hits against the Insecta library.

### rRNA reads filtering and sequence assembly

Assembling Illumina reads to reconstruct rRNA sequences from total mosquito RNA is not a straightforward task. Apart from host rRNA, total RNA samples also contain rRNA from other organisms associated with the host (microbiota, external parasites, or ingested diet). As rRNA sequences share high homology in conserved regions, Illumina reads (150 bp) from non-host rRNA can interfere with the contig assembly of host 28S and 18S rRNA.

Our score-based filtration strategy, described in detail in the Materials and methods section, allowed us to bioinformatically remove interfering rRNA reads and achieve successful de novo assembly of 28S and 18S rRNA sequences for all our specimens. Briefly, for each Illumina read, we computed a ratio of BLAST scores against an Insecta library over scores against a Non-Insecta library (Figure 2A). Based on their ratio of scores, reads could be segregated into four categories (Figure 2B): (i) reads mapping only to the Insecta library, (ii) reads mapping better to the Insecta relative to Non-Insecta library, (iii) reads mapping better to the Non-Insecta relative to the Insecta library, and (iv) reads mapping only to the Non-Insecta library. By applying a conservative threshold at 0.8 to account for the non-exhaustiveness of the SILVA database, we removed reads that likely do not originate from mosquito rRNA. Notably, 15 of our specimens were engorged with vertebrate blood, a rich source of non-mosquito rRNA (Appendix 1—table 1). The successful assembly of complete 28S and 18S rRNA sequences for these specimens demonstrates that this strategy performs as expected even with high amounts of non-host rRNA reads. This is particularly important in studies on field-captured mosquitoes as females are often sampled already having imbibed a blood meal or captured using the human landing catch technique.

We encountered challenges for three specimens morphologically identified as Mansonia africana (Specimen ID S33–S35) (Appendix 1—table 1). COI amplification by PCR did not produce any product, hence COI sequencing could not be used to confirm species identity. In addition, the genome assembler SPAdes (Bankevich et al., 2012) was only able to assemble partial length rRNA contigs, despite the high number of reads with high scores against the Insecta library. Among other Mansonia specimens, these partial length contigs shared the highest similarity with contigs obtained from sample ‘Ma uniformis CF S51’. We then performed a guided assembly using the 28S and 18S sequences of this specimen as references, which successfully produced full-length contigs. In two of these specimens (Specimen ID S34 and S35), our assembly initially produced two sets of 28S and 18S rRNA sequences, one of which was similar to mosquito rRNA with low coverage and another with 10-fold higher coverage and 95% nucleotide sequence similarity to a water mite of genus Horreolanus known to parasitize mosquitoes. Our success in obtaining rRNA sequences for mosquito and water mite shows that our strategy can be applied to metabarcoding studies where the input material comprises multiple insect species, provided that appropriate reference sequences of the target species or of a close relative are available.

Altogether, we were able to assemble 122 28S and 114 18S full-length rRNA sequences for 33 mosquito species representing 10 genera sampled from four countries across three continents. This dataset contains, to our knowledge, the first records for 30 mosquito species and for seven genera: Coquillettidia, Mansonia, Limatus, Mimomyia, Uranotaenia, Psorophora, and Eretmapodites. Individual GenBank accession numbers for these sequences and specimen information are listed in Appendix 1—table 1.

### Comparative phylogeny of novel rRNA sequences relative to existing records

To verify the assembly accuracy of our rRNA sequences, we constructed a comprehensive phylogenetic tree from the full-length 28S rRNA sequences generated from our study and included relevant rRNA sequences publicly available from GenBank (Figure 3). We applied a search criterion for GenBank sequences with at least 95% coverage of our sequence lengths (~4000 bp), aiming to represent as many species or genera as possible. Although we rarely found records for the same species included in our study, the resulting tree showed that our 28S sequences generally clustered according to their respective species and subgenera, supported by moderate to good bootstrap support at terminal nodes. Species taxa generally formed monophyletic clades, with the exception of An. gambiae and Cx. quinquefasciatus. An. gambiae 28S rRNA sequences formed a clade with closely related sequences from Anopheles arabiensis, Anopheles merus, and Anopheles coluzzii, suggesting unusually high interspecies homology for Anophelines or other members of subgenus Cellia (Figure 3, in purple, subgenus Cellia). Meanwhile, Cx. quinquefasciatus 28S rRNA sequences formed a taxon paraphyletic to sister species Culex pipiens (Figure 3, in coral, subgenus Culex).

![Figure 3.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig3-v2.jpg)

**Figure 3.:** A rooted phylogenetic tree based on full-length 28S sequences (3,900 bp) from this study and from GenBank was inferred using the maximum-likelihood method and constructed to scale in MEGA X (Kumar et al., 2018) using an unknown Horreolanus species found among our samples as an outgroup. Values at each node indicate bootstrap support (%) from 500 replications. Sequences from GenBank are annotated with filled circles and their accession numbers are shown. For sequences from this study, each specimen label contains information on taxonomy, origin (in two-letter country codes), and specimen ID number. Some specimens produced up to two consensus 28S sequences; this is indicated by the numbers 1 or 2 at the beginning of the specimen label. Specimen genera are indicated by colour: Culex in coral, Anopheles in purple, Aedes in dark blue, Mansonia in dark green, Culiseta in maroon, Limatus in light green, Coquillettidia in light blue, Psorophora in yellow, Mimomyia in teal, Uranotaenia in pink, and Eretmapodites in brown. Scale bar at 0.05 is shown.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The phylogenetic tree presented in Figure 3 based on 28S sequences from this study and from GenBank (annotated with filled circles) is depicted here in radial format to illustrate how the branch lengths separating Anopheline taxa are longer relative to other members of family Culicidae. An unknown Horreolanus species found among our samples serves as an outgroup. For sequences from this study, each specimen label contains information on taxonomy, origin (in two-letter country codes), and specimen ID number. Some specimens produced up to two consensus 28S sequences; this is indicated by the numbers 1 or 2 at the beginning of the specimen label. Specimen genera are indicated by colour: Culex in coral, Anopheles in purple, Aedes in dark blue, Mansonia in dark green, Limatus in light green, Coquillettidia in light blue, Psorophora in yellow, Mimomyia in teal, Uranotaenia in pink, and Eretmapodites in brown. Scale bar at 0.05 is shown.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Multiple sequence alignment was performed on 28S rRNA sequences, 3,900 bp in length. Each bar represents a 25 bp sliding window of the 28S rRNA sequence alignment where the y-axis values are the lowest percentage nucleotide identity found.

28S rRNA sequence-based phylogenetic reconstructions (Figure 3, with GenBank sequences; Figure 4—figure supplement 1, this study only) showed marked incongruence to that of 18S rRNA sequences (Figure 4—figure supplement 2). Although all rRNA trees show the bifurcation of family Culicidae into subfamilies Anophelinae (genus Anopheles, in purple) and Culicinae (all other genera), the recovered intergeneric phylogenetic relationships vary between the 28S and 18S rRNA trees and are weakly supported. The 18S rRNA tree also exhibited several taxonomic anomalies: (i) the lack of definitive clustering by species within the Culex subgenus (in coral); (ii) the lack of distinction between 18S rRNA sequences of Cx. pseudovishnui and Cx. tritaeniorhynchus (in coral); (iii) the placement of Ma sp.3 CF S35 (in dark green) within a Culex clade; and (iv) the lack of a monophyletic Mimomyia clade (in teal) (Figure 4—figure supplement 2). However, 28S and 18S rRNA sequences are encoded by linked loci in rDNA clusters and should not be analysed separately.

Indeed, when concatenated 28S+18S rRNA sequences were generated from the same specimens (Figure 4), the phylogenetic tree resulting from these sequences more closely resembles the 28S tree (Figure 3) with regard to the basal position of the Mimomyia clade (in teal) within the Culicinae subfamily with good bootstrap support in either tree (84% in 28S rRNA tree, 100% in concatenated 28S+18S rRNA tree). For internal nodes, bootstrap support values were higher in the concatenated tree compared to the 28S tree. Interestingly, the 28S+18S rRNA tree formed an Aedini tribe-clade encompassing taxa from genera Psorophora (in yellow), Aedes (in dark blue), and Eretmapodites (in brown), possibly driven by the inclusion of 18S rRNA sequences. Concatenation also resolved the anomalies found in the 18S rRNA tree and added clarity to the close relationship between Culex (in coral) and Mansonia (in dark green) taxa. Of note, relative to the 28S tree (Figure 3) the Culex and Mansonia genera are no longer monophyletic in the concatenated 28S+18S rRNA tree (Figure 4). Genus Culex is paraphyletic with respect to subgenus Mansonoides of genus Mansonia (Figure 3). Ma. titillans and Ma sp.4, which we suspect to be Mansonia pseudotitillans, always formed a distinct branch in 28S or 18S rRNA phylogenies, thus possibly representing a clade of subgenus Mansonia.

![Figure 4.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig4-v2.jpg)

**Figure 4.:** This phylogenetic tree based on concatenated 28S+18S rRNA sequences (3,900+1,900 bp) generated from this study was inferred using the maximum-likelihood method and constructed to scale using MEGA X (Kumar et al., 2018) using an unknown Horreolanus species found among our samples as an outgroup. Values at each node indicate bootstrap support (%) from 500 replications. Each specimen label contains information on taxonomy, origin (as indicated in two-letter country codes), and specimen ID number. Some specimens produced up to two consensus 28S+18S rRNA sequences; this is indicated by the numbers 1 or 2 at the beginning of the specimen label. Specimen genera are indicated by colour: Culex in coral, Anopheles in purple, Aedes in dark blue, Mansonia in dark green, Limatus in light green, Coquillettidia in light blue, Psorophora in yellow, Mimomyia in teal, Uranotaenia in pink, and Eretmapodites in brown. Scale bar at 0.05 is shown.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** This tree was inferred using maximum-likelihood method and constructed to scale in MEGA X (Kumar et al., 2018) using an unknown Horreolanus species found among our samples as an outgroup. Values at each node indicate bootstrap support (%) from 500 replications. For sequences from this study, each specimen label contains information on taxonomy, origin (in two-letter country codes), and specimen ID number. Some specimens produced up to two consensus 28S rRNA sequences; this is indicated by the numbers 1 or 2 at the beginning of the specimen label. Specimen genera are indicated by colour: Culex in coral, Anopheles in purple, Aedes in dark blue, Mansonia in dark green, Limatus in light green, Coquillettidia in light blue, Psorophora in yellow, Mimomyia in teal, Uranotaenia in pink, and Eretmapodites in brown. Scale bar at 0.05 is shown.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** This tree was inferred using maximum-likelihood method and constructed to scale in MEGA X (Kumar et al., 2018) using an unknown Horreolanus species found among our samples as an outgroup. Values at each node indicate bootstrap support (%) from 500 replications. For sequences from this study, each specimen label contains information on taxonomy, origin (in two-letter country codes), and specimen ID number. One 18S rRNA sequence was obtain for each specimen. Specimen genera are indicated by colour: Culex in coral, Anopheles in purple, Aedes in dark blue, Mansonia in dark green, Limatus in light green, Coquillettidia in light blue, Psorophora in yellow, Mimomyia in teal, Uranotaenia in pink, and Eretmapodites in brown. Scale bar at 0.05 is shown.

The concatenated 28S+18S rRNA tree (Figure 4) recapitulates what is classically known about the systematics of our specimens, namely (i) the early divergence of subfamily Anophelinae from subfamily Culicinae, (ii) the division of genus Anopheles (in purple) into two subgenera, Anopheles and Cellia, (iii) the division of genus Aedes (in dark blue) into subgenera Stegomyia and Ochlerotatus, (iv) the divergence of the monophyletic subgenus Melanoconion within the Culex genus (in coral) (Harbach, 2007; Harbach and Kitching, 2016).

### rRNA as a molecular marker for taxonomy and phylogeny

We sequenced a 621 bp region of the COI gene to confirm morphological species identification of our specimens and to compare the functionality of rRNA and COI sequences as molecular markers for taxonomic and phylogenetic investigations. COI sequences were able to unequivocally determine the species identity in most specimens except for the following cases. An. coustani COI sequences from our study, regardless of specimen origin, shared remarkably high nucleotide similarity (>98%) with several other Anopheles species such as An. rhodesiensis, An. rufipes, An. ziemanni, An. tenebrosus, although An. coustani remained the most frequent and closest match. In the case of Ae. simpsoni, three specimens had been morphologically identified as Ae. opok although their COI sequences showed 97–100% similarity to that of Ae. simpsoni. As GenBank held no records of Ae. opok COI at the time of this study, we instead aligned the putative Ae. simpsoni COI sequences against two sister species of Ae. opok: Ae. luteocephalus and Ae. africanus. We found they shared only 90% and 89% similarity, respectively. Given this significant divergence, we concluded these specimens to be Ae. simpsoni. Ambiguous results were especially frequent among Culex specimens belonging to the Cx. pipiens or Cx. vishnui subgroups, where the query sequence differed with either of the top two hits by a single nucleotide. For example, between Cx. quinquefasciatus and Cx. pipiens of the Cx. pipiens subgroup, and between Cx. vishnui and Cx. tritaeniorhynchus of the Cx. vishnui subgroup.

Among our three specimens of Ma. titillans, two appeared to belong to a single species that is different from but closely related to Ma. titillans. We surmised that these specimens could instead be Ma. pseudotitillans based on morphological similarity but were not able to verify this by molecular means as no COI reference sequence is available for this species. These specimens are hence putatively labelled as ‘Ma sp.4’.

Phylogenetic reconstruction based on the COI sequences showed clustering of all species taxa into distinct clades, underlining the utility of the COI gene in molecular taxonomy (Figure 5; Hebert et al., 2003; Ratnasingham and Hebert, 2007). However, species delineation among members of Culex subgroups were not as clear-cut, although sister species were correctly placed as sister taxa (Figure 5, in coral). This is comparable to the 28S+18S rRNA tree (Figure 4, in coral) and is indicative of lower intraspecies distances relative to interspecies distances.

![Figure 5.](https://cdn.elifesciences.org/articles/82762/elife-82762-fig5-v2.jpg)

**Figure 5.:** A phylogenetic tree based on COI sequences (621–699 bp) was inferred using the maximum-likelihood method and constructed to scale using MEGA X (Kumar et al., 2018) with three water mite species to serve as outgroups. Outgroup sequences obtained from GenBank are annotated with filled circles and their accession numbers are shown. Values at each node indicate bootstrap support (%) from 500 replications. Each specimen label contains information on taxonomy, origin (as indicated in two-letter country codes), and specimen ID. Specimen genera are indicted by colour: Culex in coral, Anopheles in purple, Aedes in dark blue, Mansonia in dark green, Limatus in light green, Coquillettidia in light blue, Psorophora in yellow, Mimomyia in teal, Uranotaenia in pink, and Eretmapodites in brown. Scale bar at 0.05 is shown.

To evaluate the utility of 28S and 18S rRNA sequences for molecular taxonomy, we used the 28S+18S rRNA tree to discern the identity of six specimens for which COI sequencing could not be performed. These specimens include three unknown Mansonia species (Specimen ID S33–S35), a Ma. uniformis (Specimen ID S51), an An. gambiae (Specimen ID S47), and a Ur. geometrica (Specimen ID S113) (Appendix 1—table 1). Their positions in the 28S+18S rRNA tree relative to adjacent taxa confirms the morphological identification of all six specimens to the genus level and, for three of them, to the species level (Figure 4; Mansonia in dark green, Anopheles in purple, Uranotaenia in pink).

The phylogenetic relationships indicated by the COI tree compared to the 28S+18S rRNA tree present only few points of similarity, with key differences summarised in Table 2. COI-based phylogenetic inference indeed showed clustering of generic taxa into monophyletic clades albeit with very weak bootstrap support, except for genera Culex and Mansonia (Figure 5; Culex in coral, Mansonia in dark green). Contrary to the 28S+18S rRNA tree (Figure 4), Culex subgenus Melanoconion was depicted as a polyphyletic taxon with Cx. spissipes being a part of the greater Culicini clade with members from subgenera Oculeomyia and Culex while Cx. pedroi and Cx. portesi formed a distantly related clade. Among the Mansonia specimens, the two unknown Ma sp.4 specimens were not positioned as the nearest neighbours of Ma. titillans and instead appeared to have diverged earlier from most of the other taxa from the Culicidae family. Notably, the COI sequences of genus Anopheles (Figure 5, in purple) is not basal to the other members of Culicidae and is instead shown to be sister to Culex COI sequences (8% bootstrap support). This is a direct contrast to what is suggested by the rRNA phylogenies (Figures 3 and 4, Figure 4—figure supplements 1 and 2; Anopheles in purple), which suggests Culex (in coral) rRNA sequences to be among the most recently diverged. Bootstrap support for the more internal nodes of the COI trees were remarkably low compared to those of rRNA-based trees.

**Table 2.**
 Summary of differences between rRNA and cytochrome c oxidase I (COI) phylogenies.


<table>
  <thead>
    <tr>
      <th>Taxa</th>
      <th>28S+18S rRNA phylogeny (Figure 4)</th>
      <th>COI phylogeny (Figure 5)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>The Anopheles genus</td>
      <td>Forms a clade that is basal to the all other members of family Culicidae; interspecies branch lengths are notably long</td>
      <td>Forms a sister clade to the Culex genus, and is depicted to have diverged more recently; interspecies branch lengths are comparable to that of other genera</td>
    </tr>
    <tr>
      <td>The Ur. geometrica species</td>
      <td>Forms a clade within the Culicinae subfamily lineage</td>
      <td>Forms a clade that is basal to the all other members of family Culicidae</td>
    </tr>
    <tr>
      <td>The Aedini tribe</td>
      <td>Forms a monophyletic clade comprising the genera Aedes, Eretmapodites, and Psorophora, with the latter being an early divergent lineage</td>
      <td>Does not form a monophyletic clade; the Psorophora clade is placed among Aedes taxa and the Eretmapodites clade is sister to a Culex subgenus Melanoconion clade</td>
    </tr>
    <tr>
      <td>The Culex genus</td>
      <td>Splits into two monophyletic clades with the three French Guyanese species forming a closely related minor clade</td>
      <td>Splits into two clades with two out of three French Guyanese species (Cx. pedroi and Cx. portesi) forming a distantly related minor clade, while the third (Cx. spissipes) is a part of the greater clade</td>
    </tr>
    <tr>
      <td>The Mansonia genus</td>
      <td>Is a polyphyletic group comprising two clades with the two French Guyanese taxa forming a distantly related minor clade; the major clade is placed among Culex taxa</td>
      <td>Forms a subgenus Mansonoides clade as per the 28S+18S rRNA tree but the French Guyanese taxa do not cluster together; is depicted to have diverged earlier relative to other taxa in the assemblage</td>
    </tr>
    <tr>
      <td>The Ma sp.4 species</td>
      <td>Forms a sister clade to Ma. titillans as part of a minor French Guyanese Mansonia clade</td>
      <td>Does not form a sister clade to Ma. titillans; instead is shown to have diverged earlier than all other members of family Culicidae after Ur. geometrica</td>
    </tr>
  </tbody>
</table>

In all rRNA trees, it is clear that the interspecific and intersubgeneric evolutionary distances within the genus Anopheles are high relative to any other genera, indicating a greater degree of divergence (Figure 3, Figure 3—figure supplement 1, Figure 4, Figure 4—figure supplements 1 and 2; Anopheles in purple). This is evidenced by the longer branch lengths connecting Anopheline species-clades to the node of the most recent common ancestor for subgenera Anopheles and Cellia. This feature is not evident in the COI tree, where the Anopheline interspecies distances are comparable to those within the Culex, Aedes, and Mansonia taxa (Figure 5; Anopheles in purple, Culex in coral, Aedes in dark blue, Mansonia in dark green).

### On Culex subgroups

Culex (subgenus Culex) specimens of this study comprise several closely related sister species belonging to the Cx. vishnui and Culex univittatus subgroups, which are notoriously difficult to differentiate based on morphology. Accordingly, in the 28S+18S rRNA (Figure 4, in coral) and COI (Figure 5, in coral) trees these species and their known sister species were clustered together within the Culex (subgenus Culex) clade: Cx. tritaeniorhynchus with Cx. pseudovishnui (Cx. vishnui subgroup); Cx. perexiguus with Cx. neavei (Cx. univittatus subgroup).

The use of the COI sequence to distinguish between members of the Culex subgroups was limited. For example, for the two Cx. quinquefasciatus samples in our taxonomic assemblage (Specimen ID S74 and S75) (Appendix 1—table 1), BLAST analyses of their COI sequences revealed they are a single nucleotide apart from Cx. pipiens or Cx. quinquefasciatus COI sequences (Appendix 2—table 1). In the 28S rRNA tree with GenBank sequences (Figure 3), two Cx. pipiens GenBank sequences formed a clade sister to another containing three Cx. quinquefasciatus GenBank sequences and the ‘Cx quinquefasciatus MG S74’ sequence with 78% bootstrap support. This is in accordance with other studies examining mitochondrial sequences (Sun et al., 2019) and morphological attributes (Harbach et al., 2017). This shows that the 28S rRNA sequence can distinguish the two species and confirms that ‘Cx quinquefasciatus MG S74’ is indeed a Cx. quinquefasciatus specimen. However, ‘Cx quinquefasciatus MG S75’ is shown to be basal from other sequences within this Cx. pipiens subgroup-clade with 100% bootstrap support. Given that Cx. quinquefasciatus and Cx. pipiens are known to interbreed, it is plausible that this individual is a hybrid of the two species (Farajollahi et al., 2011).

## Discussion

RNA-seq metagenomics on field-captured sylvatic mosquitoes is a valuable tool for tracking mosquito viruses through surveillance and virus discovery. However, the lack of reference rRNA sequences hinders good oligo-based depletion and efficient clean-up of RNA-seq data. Additionally, de novo assembly of rRNA sequences is complicated due to regions that are highly conserved across all distantly related organisms that could be present in a single specimen, that is, microbiota, parasites, or vertebrate blood meal. Hence, we established a method to bioinformatically filter out non-host rRNA reads for the accurate assembly of novel 28S and 18S rRNA reference sequences.

We found that phylogenetic reconstructions based on 28S sequences or concatenated 28S+18S rRNA sequences were able to correctly cluster mosquito taxa according to species and corroborate current mosquito classification. This demonstrates that our bioinformatics methodology reliably generates bona fide 28S and 18S rRNA sequences, even in specimens parasitized by water mites or engorged with vertebrate blood. Further, we were able to use 28S+18S rRNA sequence taxonomy for molecular species identification when COI sequences were unavailable or ambiguous, thus supporting the use of rRNA sequences as a molecular marker. In RNA-seq metagenomics applications, they have the advantage of circumventing the need to additionally isolate and sequence DNA from specimens, as RNA-seq reads can be directly mapped against reference sequences. In our hands, there are sufficient numbers of remaining reads post-depletion (5–10% of reads per sample) to assemble complete rRNA contigs (unpublished data).

Phylogenetic inferences based on 28S or 18S rRNA sequences alone do not recover the same interspecific relationships (Figure 4—figure supplements 1 and 2). Relative to 28S sequences, we observed more instances where multiple specimens have near-identical 18S rRNA sequences. This can occur for specimens belonging to the same species, but also for conspecifics sampled from different geographic locations, such as An. coustani, An. gambiae, or Ae. albopictus. More rarely, specimens from the same species subgroup, such as Cx. pseudovishnui and Cx. tritaeniorhynchus, also shared 18S rRNA sequences. This was surprising given that the 18S rRNA sequences in our dataset is 1,900 bp long. Concatenation of 28S and 18S rRNA sequences resolved this issue, enabling species delineation even among sister species of Culex subgroups, where morphological identification meets its limits.

In Cambodia and other parts of Asia, the Cx. vishnui subgroup includes Cx. tritaeniorhynchus, Cx. vishnui, and Cx. pseudovishnui, which are important vectors of JEV (Maquart and Boyer, 2022). The former two were morphologically identified in our study but later revealed by COI sequencing to be a sister species. Discerning sister species of the Cx. pipiens subgroup is further complicated by interspecific breeding, with some populations showing genetic introgression to varying extents (Cornel et al., 2003). The seven sister species of this subgroup are practically indistinguishable based on morphology and require molecular methods to discern (Farajollahi et al., 2011; Zittra et al., 2016). Indeed, the 621 bp COI sequence amplified in our study did not contain enough nucleotide divergence to allow clear identification, given that the COI sequence of Cx. quinquefasciatus specimens differed from that of Cx. pipiens by a single nucleotide. Batovska et al., 2017, found that even the Internal Transcribed Spacer 2 (ITS2) rDNA region, another common molecular marker, could not differentiate the two species. Other DNA molecular markers such as nuclear Ace-2 or CQ11 genes (Aspen and Savage, 2003; Zittra et al., 2016) or Wolbachia pipientis infection status (Cornel et al., 2003) are typically employed in tandem. In our study, 28S rRNA sequence-based phylogeny validated the identity of specimen ‘Cx quinquefasciatus MG S74’ (Figure 3, in coral) and suggested that specimen ‘Cx quinquefasciatus MG S75’ might have been a pipiens-quinquefasciatus hybrid. These examples demonstrate how 28S rRNA sequences, concatenated with 18S rRNA sequences or alone, contain enough resolution to differentiate between Cx. pipiens and Cx. quinquefasciatus. rRNA-based phylogeny thus allows for more accurate species identification and ecological observations in the context of disease transmission. Additionally, tracing the genetic flow across hybrid populations within the Cx. pipiens subgroup can inform estimates of vectorial capacity for each species. As only one or two members from the Cx. pipiens and Cx. vishnui subgroups were represented in our taxonomic assemblage, an explicit investigation including all member species of these subgroups in greater sample numbers is warranted to further test the degree of accuracy with which 28S and 18S rRNA sequences can delineate sister species.

Our study included French Guianese Culex species Cx. spissipes (group Spissipes), Cx. pedroi (group Pedroi), and Cx. portesi (group Vomerifer). These species belong to the New World subgenus Melanoconion, section Spissipes, with well-documented distribution in North and South Americas (Sirivanakarn, 1982) and are vectors of encephalitic alphaviruses EEEV and VEEV among others (Talaga et al., 2021; Turell et al., 2008; Weaver et al., 2004). Indeed, our rooted rRNA and COI trees showed the divergence of the three Melanoconion species from the major Culex clade comprising species broadly found across Africa and Asia (Auerswald et al., 2021; Farajollahi et al., 2011; Nchoutpouen et al., 2019; Takhampunya et al., 2011). The topology of the concatenated 28S+18S rRNA tree places the Cx. portesi and Cx. pedroi species-clades as sister groups (92% bootstrap support), with Cx. spissipes as a basal group within the Melanoconion clade (100% bootstrap support) (Figure 4, in coral). This corroborates the systematics elucidated by Navarro and Weaver, 2004, using the ITS2 marker, and those by Sirivanakarn, 1982 and Sallum and Forattini, 1996 based on morphology. Curiously, in the COI tree, Cx. spissipes sequences were clustered with unknown species Cx. sp.1, forming a clade sister to another containing other Culex (Culex) and Culex (Oculeomyia) species, albeit with very low bootstrap support (Figure 5, in coral). Previous phylogenetic studies based on the COI gene have consistently placed Cx. spissipes or the Spissipes group basal to other groups within the Melanoconion subgenus (Torres-Gutierrez et al., 2016; Torres-Gutierrez et al., 2018). However, these studies contain only Culex (Melanoconion) species in their assemblage, apart from Cx. quinquefasciatus to act as an outgroup. This clustering of Cx. spissipes with non-Melanoconion species in our COI phylogeny could be an artefact of a much more diversified assemblage rather than a true phylogenetic link.

Taking advantage of our multi-country sampling, we examined whether rRNA or COI phylogeny can be used to distinguish conspecifics originating from different geographies. Our assemblage contains five of such species: An. coustani, An. funestus, An. gambiae, Ae. albopictus, and Ma. uniformis. Among the rRNA trees, the concatenated 28S+18S and 28S rRNA trees were able to discriminate between Ma. uniformis specimens from Madagascar, Cambodia, and the Central African Republic (in dark green), and between An. coustani specimens from Madagascar and the Central African Republic (in purple) (100% bootstrap support). In the COI tree, only Ma. uniformis was resolved into geographical clades comprising specimens from Madagascar and specimens from Cambodia (in dark green) (72% bootstrap support). No COI sequence was obtained from one Ma. uniformis specimen from the Central African Republic. The 28S+18S rRNA sequences ostensibly provided more population-level genetic information than COI sequences alone with better support. The use of rRNA sequences in investigating the biodiversity of mosquitoes should therefore be explored with a more comprehensive taxonomic assemblage.

The phylogenetic reconstructions based on rRNA or COI sequences in our study are hardly congruent (Table 2), but two principal differences stand out. First, the COI phylogeny does not recapitulate the early divergence of Anophelinae from Culicinae (Figure 5). This is at odds with other studies estimating mosquito divergence times based on mitochondrial genes (Logue et al., 2013; Lorenz et al., 2021) or nuclear genes (Reidenbach et al., 2009). The second notable feature in the rRNA trees is the remarkably large interspecies and intersubgeneric evolutionary distances within genus Anopheles relative to other genera in the Culicinae subfamily (Figure 3, Figure 3—figure supplement 1, Figure 4, Figure 4—figure supplements 1 and 2; Anopheles in purple) but this is not apparent in the COI tree. The hyperdiversity among Anopheles taxa may be attributed to the earlier diversification of the Anophelinae subfamily in the early Cretaceous period compared to that of the Culicinae subfamily—a difference of at least 40 million years (Lorenz et al., 2021). The differences in rRNA and COI tree topologies indicate a limitation in using COI alone to determine evolutionary relationships. Importantly, drawing phylogenetic conclusions from short DNA markers such as COI has been cautioned against due to its weak phylogenetic signal (Hajibabaei et al., 2006). The relatively short length of our COI sequences (621–699 bp) combined with the 100-fold higher nuclear substitution rate of mitochondrial genomes relative to nuclear genomes (Arctander, 1995) could result in homoplasy (Danforth et al., 2005), making it difficult to clearly discern ancestral sequences and correctly assign branches into lineages, as evidenced by the poor nodal bootstrap support at genus-level branches. Indeed, in the study by Lorenz et al., 2021, a phylogenetic tree constructed using a concatenation of all 13 protein-coding genes of the mitochondrial genome was able to resolve ancient divergence events. This affirms that while COI sequences can be used to reveal recent speciation events, longer or multi-gene molecular markers are necessary for studies into deeper evolutionary relationships (Danforth et al., 2005).

In contrast to Anophelines where 28S rRNA phylogenies illustrated higher interspecies divergence compared to COI phylogeny, two specimens of an unknown Mansonia species, ‘Ma sp.4 GF S103’ and ‘Ma sp.4 GF S104’, provided an example where interspecies relatedness based on their COI sequences is greater than that based on their rRNA sequences in relation to ‘Ma titillans GF S105’. While all rRNA trees placed ‘Ma titillans GF S105’ as a sister taxon with 100% bootstrap support, the COI tree placed M sp.4 basal to all other species except Ur. geometrica (Figure 5; Mansonia in dark green, Uranotaenia in pink). This may hint at a historical selective sweep in the mitochondrial genome, whether arising from geographical separation, mutations, or linkage disequilibrium with inherited symbionts (Hurst and Jiggins, 2005), resulting in the disparate mitochondrial haplogroups found in French Guyanese Ma sp.4 and Ma. titillans. In addition, both haplogroups are distant from those associated with members of subgenus Mansonoides. To note, the COI sequences of ‘M sp.4 GF S103’ and ‘M sp.4 GF S104’ share 87.12% and 87.39% nucleotide similarity, respectively, to that of ‘Ma titillans GF S105’. Interestingly, the endosymbiont Wo. pipientis has been detected in Ma. titillans sampled from Brazil (de Oliveira et al., 2015), which may contribute to the divergence of ‘Ma titillans GF S105’ COI sequence away from those of Ma sp.4. This highlights other caveats of using a mitochondrial DNA marker in determining evolutionary relationships (Hurst and Jiggins, 2005), which nuclear markers such as 28S and 18S rRNA sequences may be immune to.

### Conclusions

Total RNA-seq is a valuable tool for surveillance and virus discovery in sylvatic mosquitoes but it is impeded by the lack of full-length rRNA reference sequences. Here, we presented an rRNA sequence assembly strategy and a dataset of 234 newly generated mosquito 28S and 18S rRNA sequences. Our work has expanded the current mosquito rRNA reference library by providing, to our knowledge, the first full-length rRNA records for 30 species in public databases and paves the way for the assembly of many more. These novel rRNA sequences can improve mosquito metagenomics based on RNA-seq by enabling physical and computational removal of rRNA from specimens and streamlined species identification using rRNA markers.

Given that a reference sequence is available, rRNA markers could serve as a better approach for mosquito taxonomy and phylogeny than COI markers. In analysing the same set of specimens based on their COI and rRNA sequences, we showed that rRNA sequences can discriminate between members of a species subgroup as well as conspecifics from different geographies. Phylogenetic inferences from a tree based on 28S rRNA sequences alone or on concatenated 28S+18S rRNA sequences are more aligned with contemporary mosquito systematics, showing evolutionary relationships that agree with other phylogenetic studies. While COI-based phylogeny can reveal recent speciation events, rRNA sequences may be better suited for investigations of deeper evolutionary relationships as they are less prone to selective sweeps and homoplasy. The advantages and disadvantages of rRNA and COI sequences as molecular markers are summarised in Table 3. Further studies are necessary to reveal how rRNA sequences compare against other nuclear or mitochondrial DNA marker systems (Batovska et al., 2017; Beebe, 2018; Behura, 2006; Ratnasingham and Hebert, 2007; Reidenbach et al., 2009; Vezenegho et al., 2022).

**Table 3.**
 Comparison of 28S or concatenated 28S+18S rRNA and cytochrome c oxidase I (COI) sequences as molecular markers.


<table>
  <thead>
    <tr>
      <th colspan="2">28S+18S rRNA</th>
    </tr>
    <tr>
      <th>Advantages</th>
      <th>Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>In RNA-seq metagenomics studies, molecular taxonomy of specimens based on rRNA sequences can be done from RNA-seq data without additional sample preparation or sequencing.28S rRNA and concatenated 28S+18S rRNA sequences can resolve the identity of specimens where COI sequences were ambiguous, particularly between members of species subgroups.28S rRNA and concatenated 28S+18S rRNA sequences can distinguish conspecifics from different geographies for certain species.Phylogenetic inferences based on 28S rRNA and concatenated 28S+18S rRNA sequences show relationships that are more concordant to contemporary mosquito systematics elucidated by other studies and may be a more suitable marker to study deep evolutionary relationships.Being longer and nuclear-encoded, 28S or concatenated 28S+18S rRNA sequences are immune to homoplasy or to selective sweeps that may affect genomes of inherited symbionts such as mitochondria.</td>
      <td>RNA-seq costs more than Sanger sequencing.Reference rRNA sequences are currently much more limited in breadth compared to other established molecular markers.</td>
    </tr>
    <tr>
      <td colspan="2">COI</td>
    </tr>
    <tr>
      <td>Advantages</td>
      <td>Disadvantages</td>
    </tr>
    <tr>
      <td>With a larger reference database, the COI is a versatile marker for molecular taxonomy.Being a shorter DNA marker, the COI gene is cost- and time-effective to amplify, sequence, and characterise.Universal primer sets to amplify the COI marker have been developed and tested for many diverse species.</td>
      <td>All species taxa clustered into distinct clades but with weaker bootstrap support at internal nodes relative to those of the 28S+18S rRNA tree.For An. coustani, and members of Culex species subgroups such as Cx. quinquefasciatus and Cx. tritaeniorhynchus, COI sequences are unable to unequivocally confirm species identity as species can differ by just one nucleotide. Other molecular markers are often used in tandem.</td>
    </tr>
  </tbody>
</table>

## Materials and methods

### Sample collection

Mosquito specimens were sampled from 2019 to 2020 by medical entomology teams from the Institut Pasteur de Bangui (Central African Republic, Africa; CF), Institut Pasteur de Madagascar (Madagascar, Africa; MG), Institut Pasteur du Cambodge (Cambodia, Asia; KH), and Institut Pasteur de la Guyane (French Guiana, South America; GF). Adult mosquitoes were sampled using several techniques including CDC light traps, BG sentinels, and human-landing catches. Sampling sites are sylvatic locations including rural settlements in the Central African Republic, Madagascar, and French Guiana and national parks in Cambodia. Mosquitoes were morphologically identified using taxonomic identification keys (Edwards, 1941; Grjebine, 1966; Huang and Ward, 1981; Oo et al., 2006; Rattanarithikul et al., 2007; Rattanarithikul et al., 2010; Rattanarithikul et al., 2005a; Rattanarithikul et al., 2005b; Rattanarithikul et al., 2006a; Rattanarithikul et al., 2006b; Rueda, 2004) on cold tables before preservation by flash freezing in liquid nitrogen and transportation in dry ice to Institut Pasteur Paris for analysis. A list of the 112 mosquito specimens included in our taxonomic assemblage and their related information are provided in Appendix 1—table 1. To note, specimen ID S53, S80, and S81 were removed from our assemblage as their species identity could not be determined by COI or rRNA sequences.

### RNA and DNA isolation

Nucleic acids were isolated from mosquito specimens using TRIzol reagent according to the manufacturer’s protocol (Invitrogen, Thermo Fisher Scientific, Waltham, MA, USA). Single mosquitoes were homogenised into 200 µL of TRIzol reagent and other of the reagents within the protocol were volume-adjusted accordingly. Following phase separation, RNA were isolated from the aqueous phase while DNA were isolated from the remaining interphase and phenol-chloroform phase. From here, RNA is used to prepare cDNA libraries for next-generation sequencing while DNA is used in PCR amplification and Sanger sequencing of the mitochondrial COI gene as further described below.

### Probe depletion of rRNA

We tested a selective rRNA depletion protocol by Morlan et al., 2012 on several mosquito species from the Aedes, Culex, and Anopheles genera. We designed 77 tiled 80 bp DNA probes antisense to the Ae. aegypti 28S, 18S, and 5.8S rRNA sequences. A pool of probes at a concentration of 0.04 µM were prepared. To bind probes to rRNA, 1 µL of probes and 2 µL of Hybridisation Buffer (100 mM Tris-HCl and 200 mM NaCl) were added to rRNA samples to a final volume of 20 µL and subjected to a slow-cool incubation starting at 95°C for 2 min, then cooling to 22°C at a rate of 0.1°C per second, ending with an additional 5 min at 22°C. The resulting RNA:DNA hybrids were treated with 2.5 µL Hybridase Thermostable RNase H (Epicentre, Illumina, Madison, WI, USA) and incubated at 37°C for 30 min. To remove DNA probes, the mix was treated with 1 µL DNase I (Invitrogen) and purified with Agencourt RNAClean XP Beads (Beckman Coulter, Brea, CA, USA). The resulting RNA is used for total RNA-seq to check depletion efficiency.

### Total RNA-seq

To obtain rRNA sequences, RNA samples were quantified on a Qubit Fluorometer (Invitrogen) using the Qubit RNA BR Assay kit (Invitrogen) for concentration adjustment. Non-depleted total RNA was used for library preparation for next-generation sequencing using the NEBNext Ultra II RNA Library Preparation Kit for Illumina (New England Biolabs, Ipswich, MA, USA) and the NEBNext Multiplex Oligos for Illumina (Dual Index Primers Set 1) (New England Biolabs). Sequencing was performed on a NextSeq500 sequencing system (Illumina, San Diego, CA, USA). Quality control of fastq data and trimming of adapters were performed with FastQC and cutadapt, respectively.

### 28S and 18S rRNA assembly

To obtain 28S and 18S rRNA contigs, we had to first clean our fastq library by separating the reads representing mosquito rRNA from all other reads. To achieve this, we used the SILVA RNA sequence database to create two libraries: one containing all rRNA sequences recorded under the ‘Insecta’ node of the taxonomic tree, the other containing the rRNA sequences of many other nodes distributed throughout the taxonomic tree, hence named ‘Non-Insecta’ (Quast et al., 2013). Each read was aligned using the nucleotide Basic Local Alignment Search Tool (BLASTn, https://blast.ncbi.nlm.nih.gov/) of the National Center for Biotechnology Information (NCBI) against each of the two libraries and the scores of the best high-scoring segment pairs from the two BLASTns are subsequently used to calculate a ratio of Insecta over Non-Insecta scores (Altschul et al., 1990). Only reads with a ratio greater than 0.8 were used in the assembly. The two libraries being non-exhaustive, we chose this threshold of 0.8 to eliminate only reads that were clearly of a non-insect origin. Selected reads were assembled with the SPAdes genome assembler using the ‘-rna’ option, allowing more heterogeneous coverage of contigs and kmer lengths of 31, 51, and 71 bases (Bankevich et al., 2012). This method successfully assembled rRNA sequences for all specimens, including a parasitic Horreolanus water mite (122 sequences for 28S and 114 sequences for 18S).

Initially, our filtration technique had two weaknesses. First, there is a relatively small number of complete rRNA sequences in the Insecta library from SILVA. To compensate for this, we carried out several filtration cycles, each time adding in the complete sequences produced in previous cycles to the Insecta library. Second, when our mosquito specimens were parasitized by other insects, it was not possible to bioinformatically filter out rRNA reads belonging to the parasite. For these rare cases, we used the ‘ --trusted-contigs’ option of the SPAdes assembler (Bankevich et al., 2012), giving it access to the 28S and 18S rRNA sequences of the mosquito closest in terms of taxonomic distance. By doing this, the assembler was able to reconstruct the rRNA of the mosquito as well as the rRNA of the parasitizing insect. All assembled rRNA sequences from this study have been deposited in GenBank with accession numbers OM350214–OM350327 for 18S rRNA sequences and OM542339–OM542460 for 28S rRNA sequences.

### COI amplicon sequencing

The mitochondrial COI gene was amplified from DNA samples using the universal ‘Folmer’ primer set LCO1490 (5’- GGTCAACAAATCATAAAGATATTGG -3’) and HCO2198 (5’-TAAACTTCAGGGTGACCAAAAAATCA-3’), as per standard COI marker sequencing practices, producing a 658 bp product (Folmer et al., 1994). PCRs were performed using Phusion High-Fidelity DNA Polymerase (Thermo Fisher Scientific). Every 50 µL reaction contained 10 µL of 5× High Fidelity buffer, 1 µL of 10 mM dNTPs, 2.5 µL each of 10 mM forward (LCO1490) and reverse (HCO2198) primer, 28.5 µL of water, 5 µL of DNA sample, and 0.5 µL of 2 U/µL Phusion DNA polymerase. A three-step cycling incubation protocol was used: 98°C for 30 s; 35 cycles of 98°C for 10 s, 60°C for 30 s, and 72°C for 15 s; 72°C for 5 min ending with a 4°C hold. PCR products were size-verified using gel electrophoresis and then gel-purified using the QIAquick Gel Extraction Kit (Qiagen, Hilden, Germany). Sanger sequencing of the COI amplicons were performed by Eurofins Genomics, Ebersberg, Germany.

### COI sequence analysis

Forward and reverse COI DNA sequences were end-trimmed to remove bases of poor quality (Q score <30). At the 5’ ends, sequences were trimmed at the same positions such that all forward sequences start with 5’-TTTTGG and all reverse sequences start with 5’-GGNTCT. Forward and reverse sequences were aligned using BLAST to produce a 621 bp consensus sequence. In cases where good quality sequences extends beyond 621 bp, forward and reverse sequences were assembled using Pearl (https://www.gear-genomics.com/pearl/) and manually checked for errors against trace files (Rausch et al., 2019; Rausch et al., 2020). We successfully assembled a total of 106 COI sequences. All assembled COI sequences from this study have been deposited in GenBank with accession numbers OM630610–OM630715.

### COI validation of morphology-based species identification

We analysed assembled COI sequences with BLASTn against the nucleotide collection (nr/nt) database to confirm morphology-based species identification. BLAST analyses revealed 32 cases where top hits indicated a different species identity, taking <95% nucleotide sequence similarity as the threshold to delineate distinct species (Appendix 2—table 1). In these cases, the COI sequence of the specimen was then BLAST-aligned against a GenBank record representing the morphological species to verify that the revised identity is a closer match by a significant margin, that is, more than 2% nucleotide sequence similarity. All species names reported hereafter reflect identities determined by COI sequence except for cases where COI-based identities were ambiguous, in which case morphology-based identities were retained. In cases where matches were found within a single genus but of multiple species, specimens were indicated as an unknown member of their genus (e.g., Culex sp.). Information of the highest-scoring references for all specimens, including details of ambiguous BLASTn results, are recorded in Appendix 2—table 1.

Within our COI sequences, we found six unidentified Culex species (including two that matched to GenBank entries identified only to the genus level), four unidentified Mansonia species, and one unidentified Mimomyia species. For An. baezai, no existing GenBank records were found at the time this analysis was performed.

### Phylogenetic analysis

Multiple sequence alignment (MSA) were performed on assembled COI and rRNA sequences using the MUSCLE software (Edgar, 2004; Madeira et al., 2019). As shown in Figure 3—figure supplement 2, the 28S rRNA sequences contain many blocks of highly conserved nucleotides, which makes the result of multiple alignment particularly evident. We therefore did not test other alignment programs. The multiple alignment of the COI amplicons is even more evident since no gaps are necessary for this alignment.

Phylogenetic tree reconstructions were performed with the MEGA X software using the maximum-likelihood method (Kumar et al., 2018). Default parameters were used with bootstrapping with 500 replications to quantify confidence level in branches. For rRNA trees, sequences belonging to an unknown species of parasitic water mite (genus Horreolanus) found in our specimens served as an outgroup taxon. In addition, we created and analysed a separate dataset combining our 28S rRNA sequences and full-length 28S rRNA sequences from GenBank totalling 169 sequences from 58 species (12 subgenera). To serve as outgroups for the COI tree, we included sequences obtained from GenBank of three water mite species, Horreolanus orphanus (KM101004), Sperchon fuxiensis (MH916807), and Arrenurus sp. (MN362807).
