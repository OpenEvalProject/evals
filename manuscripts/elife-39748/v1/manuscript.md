# The mlpt/Ubr3/Svb module comprises an ancient developmental switch for embryonic patterning

## Authors

- Suparna Ray<sup>1</sup>
- Miriam I Rosenberg<sup>2</sup> ([ORCID: 0000-0001-5348-8247](https://orcid.org/0000-0001-5348-8247)) †
- Hélène Chanut-Delalande<sup>3</sup>
- Amélie Decaras<sup>4</sup>
- Barbara Schwertner<sup>1</sup>
- William Toubiana<sup>4</sup>
- Tzach Auman<sup>2</sup> ([ORCID: 0000-0002-2233-4234](https://orcid.org/0000-0002-2233-4234))
- Irene Schnellhammer<sup>1</sup>
- Matthias Teuscher<sup>1</sup> ([ORCID: 0000-0003-2340-5716](https://orcid.org/0000-0003-2340-5716))
- Philippe Valenti<sup>3</sup>
- Abderrahman Khila<sup>4</sup> ([ORCID: 0000-0003-0908-483X](https://orcid.org/0000-0003-0908-483X))
- Martin Klingler<sup>1</sup> ([ORCID: 0000-0001-8859-1965](https://orcid.org/0000-0001-8859-1965))
- François Payre<sup>3</sup> ([ORCID: 0000-0002-8144-6711](https://orcid.org/0000-0002-8144-6711)) †

### Affiliations

1. Department of Biology, Developmental Biology University of Erlangen-Nuremberg Erlangen Germany
2. Department of Ecology, Evolution and Behavior Hebrew University of Jerusalem Jerusalem Israel
3. Centre de Biologie du Développement, Université Paul Sabatier de Toulouse Toulouse France
4. Institut de Génomique Fonctionelle de Lyon Lyon France

† Corresponding author

## Abstract

Small open reading frames (smORFs) encoding ‘micropeptides’ exhibit remarkable evolutionary complexity. Conserved peptides encoded by mille-pattes (mlpt)/polished rice (pri)/tarsal less (tal) are essential for embryo segmentation in Tribolium but, in Drosophila, function in terminal epidermal differentiation and patterning of adult legs. Here, we show that a molecular complex identified in Drosophila epidermal differentiation, comprising Mlpt peptides, ubiquitin-ligase Ubr3 and transcription factor Shavenbaby (Svb), represents an ancient developmental module required for early insect embryo patterning. We find that loss of segmentation function for this module in flies evolved concomitantly with restriction of Svb expression in early Drosophila embryos. Consistent with this observation, artificially restoring early Svb expression in flies causes segmentation defects that depend on mlpt function, demonstrating enduring potency of an ancestral developmental switch despite evolving embryonic patterning modes. These results highlight the evolutionary plasticity of conserved molecular complexes under the constraints of essential genetic networks.Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed (see decision letter).

## Introduction

Animal genomes transcribe a variety of long-non-coding RNAs, whose functions are not yet fully understood (Cech and Steitz, 2014; Guttman and Rinn, 2012; Perry and Ulitsky, 2016). A large body of evidence increasingly supports translation of so called ‘micropeptides’ from small open reading frames < 100 amino acids (also called small ORFs, smORFs or sORFs) encoded in long ‘non-coding’ RNAs (Couso and Patraquim, 2017; Plaza et al., 2017). Owing to their relatively recent discovery and experimental validation, micropeptides represent an overlooked reservoir of evolutionary and regulatory material. Identification of their developmental functions has hitherto been limited to a handful of cases and their putative contribution to animal evolution is unknown.

One of the best-known cases of smORF-encoded peptides called mille-pattes/tarsal less/polished rice (10 to 32 amino acids; hereafter referred to as mlpt), are conserved across arthropods, a taxon representing over 400 million years of evolutionary time (Galindo et al., 2007; Kondo et al., 2007; Savard et al., 2006). It has been shown that Drosophila embryos lacking mlpt function develop with proper segment patterning, but exhibit strong defects in epidermal differentiation, notably the absence of cuticular trichomes (Galindo et al., 2007; Kondo et al., 2007). In the fly epidermis, Mlpt peptides act through post-translational control of Ovo/Shavenbaby (Svb)(Kondo et al., 2010), a transcription factor well-established as the key regulator of trichomes (Payre et al., 1999). Svb is translated as a transcriptional repressor (Kondo et al., 2010) and Mlpt peptides bind to and activate an E3 ubiquitin ligase, Ubr3, enabling its interaction with Svb (Zanet et al., 2015). Formation of the Mlpt/Ubr3/Svb complex leads to proteasome degradation of the Svb N-terminal repression domain thereby, releasing a shorter Svb protein that functions as a transcriptional activator (Kondo et al., 2010; Zanet et al., 2015). Upon processing, Svb activates the expression of cellular effectors (Chanut-Delalande et al., 2006; Fernandes et al., 2010; Menoret et al., 2013), comprising a gene network deeply conserved throughout arthropods (Chanut-Delalande et al., 2006; Li et al., 2016; Spanier et al., 2017). Hence, a central function of Mlpt peptides during Drosophila development is to provide temporal control of Svb transcriptional activity, exemplified by their role in epidermal differentiation (Chanut-Delalande et al., 2014; Zanet et al., 2016).

Independently, Savard et al. (2006) discovered an essential function for this locus in the formation of abdominal segments in the flour beetle, Tribolium castaneum (Savard et al., 2006). In beetles, RNAi knockdown of mlpt caused posterior truncation of the embryo, with a loss of abdominal segments, as well as the transformation of remaining anterior abdominal segments to thoracic fate, leading to a distinctive phenotype of extra pairs of legs (mille-pattes is French for centipede). Additional work established that mlpt acts as a gap gene in Tribolium (Boos et al., 2018; Ribeiro et al., 2017; Savard et al., 2006; van der Zee et al., 2006; Zhu et al., 2017), where more limited homeotic transformations often accompany loss of gap gene function (Bucher and Klingler, 2004; Cerny et al., 2005; Marques-Souza et al., 2008). Unlike Drosophila which has evolved a derived mode of segmentation (called ‘long germ’) in which all segments are formed nearly simultaneously in the syncytial environment of the blastoderm, Tribolium is more representative of the ancestral mode of segmentation in insects (Peel et al., 2005). Most insects, like beetles, develop as short/intermediate germband embryos where only head and thorax are patterned in the blastoderm, whereas most or all posterior segments are added from a posterior ‘growth zone’ (Davis and Patel, 2002; Liu and Kaufman, 2005; Rosenberg et al., 2009). In spite of the striking absence of embryonic patterning defects in Drosophila mlpt mutants, the strong phenotype of mlpt in beetles suggested an ancestral function of the peptides in segmentation, a hypothesis we set out to investigate through their functional analysis across insect species.

## Results

### Identification of mlpt partners Svb and Ubr3 in Tribolium segmentation

We sought to identify functional partners for Mlpt peptides that explain their function in Tribolium segmentation. The genome-wide iBeetle RNAi screen in Tribolium (Dönitz et al., 2018; Dönitz et al., 2015; Schmitt-Engel et al., 2015) allowed a large-scale search for patterning genes leading to a mlpt-like mutant phenotype, as a means of identifying candidate partners.

Knockdown of >5000 genes revealed only a few candidates sharing such a segmentation phenotype (Supplementary file 1A). Further analyses validated a gene producing a reproducible phenotype that is highly similar to that of mlpt. Unexpectedly, this candidate was Tc-ubr3, the E3 ubiquitin ligase now known to be the molecular target of Mlpt peptides for epidermal differentiation in flies. In Tribolium, the Tc-ubr3 RNAi phenocopies mlpt RNAi with severely shortened larvae due to the absence of many abdominal segments as well as telson appendages (Figure 1A–C and Figure 1—figure supplement 1). Furthermore, as in mlpt RNAi, the remaining ‘abdominal’ segments appear to be transformed to a thoracic fate since they bear extra legs and often spiracles resembling those present on the second thoracic segment (Figure 1A–C and Figure 1—figure supplements 1 and 2). The Tc-Ubr3 phenotype can exceed mlpt RNAi in severity, with strongly affected legs developing shorter and poorly differentiated segments (Figure 1F,G and Figure 1—figure supplements 1 and 2). However, the overall similarity between mlpt and Tc-Ubr3 phenotypes (Table 1) suggested that the complete fly epidermal module may be conserved for Tribolium segmentation.

![Figure 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig1-v1.jpg)

**Figure 1.:** Cuticle phenotypes of Tribolium first instar larvae from following genotypes: wild type (A), mlpt RNAi (B), Tc-ubr3 RNAi (C), Tc-svb RNAi (D), and Tc-svb CRISPR mutant (E). Depletion of mlpt, Tc-svb, and Tc-ubr3 causes highly similar segmentation phenotypes, characterized by a reduction in segment number, the presence of extra-legs (arrows) suggestive of transformation of abdominal segments towards a thoracic fate (red asterisks), and the frequent absence of terminal structures. (F) Knockdown of each of the three genes leads to shortened ‘true-thoracic’ legs, with rounded and often poorly separated distal segments. The scheme represents a larval leg with corresponding segments; pictures portray an example of prothoracic leg (T1) in wildtype, mlpt, Tc-ubr3 and Tc-svb inactivation. (G) Quantification of the reduction in leg length, estimated by the distance between coxa/trochanter boundary to the pretarsus tip. Data were analyzed by one-way ANOVA using multiple comparison tests against wild-type values. *, p-value<0,05; ****, p-value<0,0001. Source data for Figure 1G are found in Source Data File 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A–D) Knockdown larvae have strong segmentation phenotypes, with drastically antero-posteriorly shortened bodies. Posterior abdominal segments are missing and the remaining ones appear to be transformed to thoracic identity, with ectopic legs (yellow arrows) and/or spiracles resembling those normally present in T2 segments (white arrows). The leg-bearing transformed segments are marked by red asterisks. Legs are shortened and rounded, with reduced pretarsi. (E) A magnified image of the legs. Leg segments sometimes appear double- jointed (black arrow). coxa (c); trochanter (t); femur (f); tibiotarsus (tt); pretarsus (pt). (F) Magnified image of the head showing the shortened, rounded and bulbous head appendages in Tc-ubr3, when compared to wild type. Setae are usually missing on the antennae.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) A mlpt knockdown larva with four pairs of legs on transformed abdominal segments. The leg-bearing transformed segments are marked by red asterisks. (B) A mlpt knockdown with a strong segmentation phenotype, with one pair of ectopic legs and only two remaining abdominal segments. (C) A weak Tc-ubr3 knockdown phenotype, that resembles the mlpt phenotype in (A), with three pairs of ectopic legs and fused remaining abdominal segments. (D) A drastically shortened Tc-ubr3 knockdown larva, apparently lacking all abdominal segments.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A–D) In larvae with weaker segmentation phenotypes, bodies are shortened along the anterior-posterior axis. While most of the abdominal segments are often present, segment boundaries are less distinct especially in the latter abdominal segments where they may be fused, and telson appendages are usually missing. Thoracic legs display shorter leg segments (See Figure 1). (E–G) Stronger phenotypes are more antero-posteriorly shortened and the last abdominal segment and the telson may either be absent or fused with the anterior segments beyond distinction. Leg segments get progressively shorter and more rounded, and the pretarsi reduced. Sometimes urogomphi (u) are present (G). Irrespective of body size and phenotypic strength, segments with extra legs are always A1 and A2 (red asterisks). One or more of these ectopic legs are often reduced to stumps. (H) Magnified ventral view of a svb knockdown showing transformed abdominal segments bearing legs (red asterisks) and fused abdominal segments.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** The mutagenic cassette is inserted into exon 2, that is within the open reading frame upstream of the region encoding the DNA-binding zinc finger domain. Gene disruption leads to mRNA truncation after the insertion site, since Tc-svb expression is absent in homozygous mutants. In addition to segmentation defects and transformation toward thoracic identity, other phenotypes observed in Tc-svbCRISPR mutants include incipient spiracles (possibly a secondary effect of cuticle thinning leading to a defect in the development of tracheal rings); sensory bristles that are shorter and thicker; leg segment boundaries that are not clearly defined; missing leg bristles; unsclerotized pretarsi with soft, rounded apices; and antennae lacking the terminal setae. Therefore, late functions of Tc-svb in epidermal and appendage differentiation are strongly affected in Tc-svbCRISPR mutant embryos, while the segmentation phenotype is milder that Tc-svb-RNAi knockdown due to maternal contribution of Tc-svb (Ray et al., in preparation).

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** (A) Schematic representation of Drosophila (Dm-Svb) and Tribolium (Tc-Svb) proteins, highlighting conserved regions. These include the N-terminus (blue), stretches of charged amino acids in the repressor region (orange), Mlpt-dependent proteolytic maturation site (red arrow) followed by a glycine/serine-rich region (light green), poly-glutamine/histidine stretch (green) and the zinc finger DNA-binding domain (blue). (B) Sequence conservation of the Svb protein across insects. The heat map represents percentages of sequence identity and similarity. (C) Disorder disposition of each protein was evaluated using PONDR-FIT (http://www.disprot.org/pondr-fit.php). Svb proteins share intrinsic disorder disposition at their N-termini compared to their DNA binding and transactivation domains (blue shade). The red line indicates the maturation site in each protein. (D) Evolutionary conservation of the N-terminal degron, with three key lysine residues required for Ubr3-mediated processing of Svb. (E) A highly conserved AAGHGR motif flanks the maturation site (red arrow). (F) The zinc finger domain is also highly conserved across Svb proteins.

**Table 1.**
 Summary of Tribolium phenotypes resulting from RNAi-mediated depletion of mlpt, Tc-Ubr3, Tc-Svb, as well as those observed in Tc-Svb CRISPR mutants.In each case, a total of 20 animals were scored. Data show the average number of deleted abdominal segments, missing terminal appendages (urogomphi) and number of pairs of extra legs. Cuticle defects were scored as normal-looking (-), mild (+) and strong (+++) thinning. For leg length, the distance from coxa/trochanter joint to leg tip (see Figure 1) was measured in segment T3.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Deleted abdominal segments</th>
      <th>Urogomphi missing</th>
      <th>Thoracic leg length (µm)</th>
      <th>Extra legs</th>
      <th>Cuticle thinning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wild type</td>
      <td>0</td>
      <td>0</td>
      <td>183</td>
      <td>0</td>
      <td>-</td>
    </tr>
    <tr>
      <td>mlpt-RNAi</td>
      <td>3.8</td>
      <td>2</td>
      <td>170</td>
      <td>4.3</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Tc-ubr3 RNAI</td>
      <td>5.1</td>
      <td>2</td>
      <td>112</td>
      <td>3.9</td>
      <td>+</td>
    </tr>
    <tr>
      <td>Tc-svb RNAi</td>
      <td>0.5</td>
      <td>1.5</td>
      <td>102</td>
      <td>3.2</td>
      <td>+</td>
    </tr>
    <tr>
      <td>Tc-svb CRISPR</td>
      <td>1.0</td>
      <td>1.7</td>
      <td>122</td>
      <td>1.65</td>
      <td>+++</td>
    </tr>
  </tbody>
</table>

In support of this hypothesis, we found that RNAi knockdown of Tc-svb also leads to a highly penetrant abdominal truncation and homeotic transformation phenotype that resembles that of mlpt and Tc-ubr3 knockdowns (Figure 1D and Figure 1—figure supplement 3). Knockdown Tc-svb larvae are characterized by the presence of legs on the first two ‘abdominal’ segments, even in the weaker segmentation phenotypes, wherein legs on segment ‘A1’ are often reduced to mere stumps (Figure 1D and Figure 1—figure supplement 3). Presence of T2-like spiracles on ‘A1’ and the absence of spiracles on ‘A2’ in Tc-svb knockdowns suggest their transformation into thoracic segments, T2 and T3, respectively. In the stronger phenotypes, the body (including the head) is very compact and the posterior abdominal segments are fused (Figure 1D and Figure 1—figure supplement 3). Although the extent of abdominal segment loss is weaker than for mlpt and Tc-ubr3 RNAi, all Tc-svb RNAi larvae are clearly shortened compared to the wild type. As with mlpt and Tc-ubr3 knockdown, leg segments are severely shortened and rounded, and pretarsi are reduced in Tc-svb knockdowns (Figure 1F,G and Figure 1—figure supplement 3).

In summary, in spite of some phenotypic differences, Tc-ubr3, mlpt, and Tc-svb larvae share several critical similarities, including some degree of posterior truncation, transformation of remaining abdominal segments towards thoracic identity, shortened leg segments with a ‘bubble-like’ terminus, and missing telson appendages (Table 1). The fact that the three functional partners identified in the fly epidermis share similar phenotypes in beetle embryonic patterning led us to hypothesize that they may act as a functional module for control of Tribolium segmentation. We accumulated several lines of evidence that support this view.

First, we generated a Tc-svb mutant using CRISPR/cas9 genome editing (see Materials and methods). Molecular characterization of the Tc-svb locus in wild-type and CRISPR-mutants indicated that this allele was a strong hypomorph, if not a null (Figure 1—figure supplement 4). CRISPR knockout of Tc-svb phenocopies the observed RNAi defects (Figure 1A–E), and highlights an additional phenotype consisting of a considerable thinning of the epidermal cuticle, similar to what has been observed in the fly (Andrew and Baker, 2008). As in Tc-svb RNAi, ectopic legs or leg rudiments are present on A1 and A2. Additional phenotypes observed in mutants include shorter and misdifferentiated legs (Figure 1A,E–G).

Second, if Tc-Svb functions molecularly via the Mlpt/Ubr3 complex, it should bear the same characteristic protein features. We therefore compared the sequence and predicted characteristics of the Tc-Svb protein to that of the fly protein (Figure 1—figure supplement 5). In flies, limitation of Ubr3-mediated proteasome degradation to the N-terminal domain of Svb has been linked to intrinsically disordered disposition of this region (Zanet et al., 2015), as opposed to the C-terminal transactivation and DNA-binding domains that resist proteasome degradation. Despite rapid evolution of Svb protein sequence outside the zinc-finger region (Kumar et al., 2012), this predicted disordered disposition pattern remains strikingly conserved for Svb in Tribolium and other insects (Figure 1—figure supplement 5A–C). Tc-Svb also displays strong conservation of the protein motifs identified in flies as required for Svb processing: the maturation site (Kondo et al., 2010) and the N-terminal region (Figure 1—figure supplement 5D–F) bound and ubiquitinated by Ubr3 to target Svb to the proteasome (Zanet et al., 2015). Indeed, other top hits detected by the iBeetle screen correspond to factors involved in ubiquitin proteasome degradation (Supplementary file 1A).

Third, we examined mRNA expression of all three components during Tribolium embryogenesis. As in flies, Tc-Ubr3 is expressed ubiquitously in the beetle embryo, as expected for an enzyme with additional widespread functions, including in DNA repair (Meisenberg et al., 2012) and apoptosis (Huang et al., 2014). In contrast, Tc-svb and mlpt display a dynamic pattern during both blastoderm and germband stages of Tribolium embryogenesis (Figure 2 and Figure 2—figure supplement 1). Importantly, Tc-svb is co-expressed with mlpt within the pre-growth zone at the onset of gastrulation (Figure 2B,B'). The posterior Tc-svb domain evolves into a strong anterior band flanking the serosa and a more diffuse posterior expression (Figure 2C’), while mlpt has much stronger posterior expression (Figure 2C). As the embryo extends, Tc-svb forms two distinct expression domains flanking the strong mlpt expression domain (Figure 2D,D’), suggesting that high levels of mlpt and Tc-svb expression may be mutually repressive (Figure 2—figure supplement 2). Subsequently, Tc-svb and mlpt expression domains shift, wave-like, anteriorly, while anterior Tc-svb expression fades and its posterior expression detaches from the posterior end (Figure 2E,E’). The interaction at such interfaces of the complementary domains may be critical for patterning of the abdominal segments.

![Figure 2.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig2-v1.jpg)

**Figure 2.:** (A–E’) Whole mount in-situ hybridization of Tribolium embryo showing mRNA expression of mlpt and Tc-svb from late blastoderm (A,A’) through extending germband stages (B,B’, C,C’, D,D’, E,E’), highlighting their complementary expression pattern (F–I) Wingless (wg) expression in wild type (F), mlpt-RNAi (G), Tc-svb- RNAi (H) and Tc-ubr3- RNAi (I) Tribolium embryos. Abdominal segments are highlighted with red arrow. ln all three knockdown conditions, wg segmental stripes are disrupted right after the last (T3) thoracic stripe. Thoracic segments (T1–T3) are indicated by green arrows.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Tc-svb is expressed at the posterior end in the blastoderm and primitive pit stage embryos (A). In the germ rudiment, the posterior expression assumes a composite pattern with strong expression in an anterior band abutting the serosa window (arrowhead) and diffuse expression posteriorly (B and C). In the early germband, the diffuse expression clears out anteriorly, and concentrates as a distinct domain at the posterior end giving rise to two distinct domains, 1 and 2 (D and E). Domain one gradually fades but remains spread out over a large area (F, G). Domain two detaches from the posterior end but remains close to it (H–K). Tc-svb also appears as dots in the head lobe in the extending germband (H) assuming a complex pattern in neuronal cells at the end of segmentation (I–L). Tc-svb is expressed in the gnathal and thoracic appendages as segmental dots, and as dots along the ventral midline, after the completion of segmentation (K and L). In old embryos, Tc-svb is strongly expressed in the presumptive antennae, gnathal and thoracic appendages, and on the pleuropods on the first abdominal segment (M).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A,B) Wild-type expression of Tc-svb in Tribolium embryos. (A) Early germ rudiment expression of Tc-svb begins as a posterior cap, with a strong stripe of expression near the anterior boundary, and a more diffuse posterior expression. In the early to mid germband stages, Tc-svb expression fades somewhat anteriorly the diffuse posterior expression clears resolving into two distinct domains, a fading anterior and a newly emerging posterior (B). (A’,B’) Expression of Tc-svb in mlpt RNAi Tribolium embryos. (A’) Germ rudiment expression of Tc-svb in mlpt RNAi embryos keeps strong in the posterior and the anterior band of expression is lost. (B’) Early to extending germband stages in mlpt RNAi show a similar absence of the anterior band and a strong persistent posterior expression, significantly stronger than in wild type embryos, suggesting de-repression of Tc-svb expression due to reduced mlpt levels. (C–D) Wild-type expression of Of-svb in Oncopeltus embryos. (C) Early germband expression of Of-svb is restricted to the growth zone, where a strong central stripe and a fainter anterior stripe of expression can be seen. (D) Late germband expression of Of-svb is seen in a single strong domain of posterior growth zone expression, in the limb buds, and in neurons in the head lobes. (C’–D’) Expression of Of-svb in mlpt RNAi Oncopeltus embryos. Of-mlpt RNAi germband embryos display distal limb bud expression of Of-svb, and exhibit ectopic svb expression throughout the distorted germband, in the head, and throughout the growth zone (red arrows).

The co-expression of mlpt and Tc-svb in the posterior growth zone helps explain why they share similar segmentation phenotypes. Examination of the segmental marker wg confirms that abdominal segments are specifically disrupted in mlpt, Tc-svb, and Tc-ubr3 RNAi embryos, while thoracic segments are formed normally (Figure 2F–I). This is of interest since in the short germ embryo of Tribolium, the head and the first thoracic segment form in the syncytial blastoderm, while after cellularization, subsequent segments continue to arise in a sequential manner from the posterior growth zone (Liu and Kaufman, 2005; Rosenberg et al., 2009).

In summary, patterns of mlpt and Tc-svb expression during Tribolium embryonic development are often complementary, and at times, overlapping. Loss of function phenotypes of mlpt, Tc-svb and Tc-ubr3 suggest that a functional module for mlpt discovered in Drosophila trichome patterning also works in concert in embryonic segmentation, leg patterning and cuticle formation in Tribolium.

### Complementarity of expression of mlpt and svb is deeply conserved in insects

Our data revealed a surprising and essential role for this gene module in controlling posterior segment formation and identity in Tribolium. To determine whether this tripartite module may function in embryonic development of other insects, we investigated the expression patterns of mlpt, ubr3 and svb in additional, more basal insect species: the water strider, Gerris buenoi (Gb; Hemiptera, Gerridae) and the milkweed bug, Oncopeltus fasciatus (Of; Hemiptera, Lygaeidae).

Figure 3 highlights the expression patterns of these genes throughout embryogenesis. The early development of the milkweed bug and the water strider are quite similar. Ubr3 expression is ubiquitous in both Oncopeltus and Gerris and was not examined further. mlpt and svb expression in the early hemipteran embryo are observed in strong domains at the anterior of the blastoderm embryo (e.g., Oncopeltus, Figure 3A,A’), with additional posterior Of-svb expression at the future site of invagination which becomes broad expression throughout the early growth zone (Figure 3A and Figure 3—figure supplement 1). This pattern persists, until a transition to a transient overlap in the early growth zone (Figure 3—figure supplement 1). Subsequently, expression of svb and mlpt resolve into complementary /overlapping domains within the growth zone (Figure 3B–E’ and Figure 3—figure supplement 1). Of-mlpt expression is also diffusely expressed through recently added segments anterior to the growth zone (Figure 3C’). Later expression in both species is seen in presumptive neurons in the central nervous system, as well as in the limb buds and mouth parts (Figure 3C–F’ and Figure 3—figure supplement 1), consistent with a function in patterning the leg and head appendages.

![Figure 3.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig3-v1.jpg)

**Figure 3.:** Whole mount in situ hybridization of svb and mlpt mRNA in Oncopeltus (A–C) and Gerris (D–F) embryos at early, mid-germ and late embryonic stages. (A–C) Oncopeltus embryonic expression. At early stages, Of-svb expression is mainly expressed in two domains (anterior head and thoracic segments) (A) Of-mlpt is restricted to a single strong stripe in presumptive head segments (A’). Then, Of-svb is expressed faintly in the head lobes and strongly in two growth zone stripes (B) while Of-mlpt is exclusively expressed in the posterior of the growth zone (B’). Late embryos express Of-svb expression in a strong stripe in the middle of the growth zone, as well as in putative head neurons and limb buds (C). At this stage, faint Of-mlpt mRNA expression is detected in the head appendages, putative head and thoracic segments, and strong but diffuse expression throughout the growth zone (C’). (D–F) Gerris embryonic expression. In early embryos, Gb-svb is faintly expressed in the head and thorax, with stronger expression in the abdomen of the early germ band (D), when Gb-mlpt expression is restricted to a thoracic stripe and two distinct abdominal domains, abutting Gb-svb expression (D’). Mid germ band embryos have more restricted Gb-svb expression, in a stripe in the growth zone, in putative neurons in the head, and faintly in limb buds (E) while they exhibit strong expression of Gb-mlpt in the limb buds, and in the posterior of the growth zone, immediately adjacent to strong Gb-svb expression. Late stage embryos exhibit faint banded expression of Gb-svb in the legs and head appendages, and in foci in the head (F) whereas they exhibit strong Gb-svb expression in the mature limbs, and in foci of expression along the embryo midline (F’).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A–J) Expression of Of-mlpt. (A) Blastoderm expression of Of-mlpt includes an anterior stripe and emergent expression adjacent to, and underlying, the invagination at the onset of gastrulation. (B–E) Early germband embryos exhibit moderate staining in the head lobes, and a broadening anterior domain in thoracic segments, which moves posteriorly as the germband extends. Of-mlpt expression is also evident in the posterior growth zone (D). As the anterior domain fades (F), the posterior domain broadens and darkens. As germband growth continues (G–H), this domain moves anteriorly from the growth zone. Of-mlpt expression is seen in developing limb buds and in head appendages. Towards the end of embryogenesis, Of-mlpt is broadly expressed throughout the unsegmented posterior germband (H–I), and exhibits banded expression in the limbs and strong head staining (J). (A’–J’) Expression of Of-Svb. (A’) Blastoderm Of-svb is expressed in two broad domains at the anterior and posterior of the embryo, with a clearing in the blastoderm middle. Strong expression is seen at the invagination when gastrulation begins. (B’–E’) In the early germband, Of-svb mRNA is seen in a strong domain covering the entire embryo posterior, with low levels throughout the embryo anterior. This clears before limb bud formation (D’), when the posterior domain becomes restricted to the posterior of the growth zone (E’). Posterior expression matures into low level expression throughout the growth zone, with a strong stripe in the middle third adjacent to more posterior Of-mlpt expression (G’), and with low level expression overlapping Of-mlpt (F’). This stripe becomes two stripes that move anteriorly within the growth zone (G’) before emergence of a second growth zone stripe (H’), concomitant with expression in the nascent limb buds and in the head lobes in discrete spots; the unsegmented germband contains several concurrent stripes of svb expression (H’). The new, most posterior domain of Of-svb darkens during limb bud growth (I’), and eventually disappears at the end of germband elongation (J’).

These data hint at a surprising role for this gene module in controlling segment formation and identity in representatives of the Coleoptera and Hemiptera, but not Diptera.

### Conserved function of mlpt/ubr3/svb gene module in insect segmentation

We next tested whether and how broadly mlpt, svb, and ubr3 may functionally cooperate during embryogenesis in these additional short germ insects. RNAi against each of these genes caused severe segmentation and patterning defects both in Gerris and Oncopeltus.

Embryos of hemimetabolous insects, including water striders and milkweed bugs, complete embryogenesis and undergo a series of molts through which they reach adulthood. These intermediate nymph stages or hatchlings exhibit the full complexity of adult structures. In Gerris and Oncopeltus, the wild type hatchling possesses three long pairs of legs, which extend along the ventral side, curling around the posterior, as well as a long pair of antennae that extend posteriorly along the ventral midline (Figure 4A,A’; E,E’). mlpt RNAi in both Gerris and Oncopeltus resulted in the loss of posterior abdominal segments and fusion of thoracic segments, with shortened rounded legs that terminate proximal to the trunk; reduction and fusion of head appendages is also apparent ( and Figure 4—figure supplement 1,2). In Oncopeltus, severely affected embryos fail to gastrulate, resulting in an everted gut (Figure 4—figure supplement 1A”,B”). Gb- and Of-svb RNAi also resulted in the loss of abdominal segments and rounding of more distally truncated legs (Figure 4C,C’; G,G’). Following Gb-svb RNAi, even mildly affected prenymphs exhibited significant reduction in leg length (Figure 4—figure supplement 3). Examination of molecular markers confirmed strong defects in embryonic segmentation and appendage formation in both Gerris (Figure 4– figure supplement 4,5) and Oncopeltus (Figure 4—figure supplement 6). ubr3 RNAi in both species gave the most severe phenotype, reflecting its presumed additional functions independent of svb and mlpt (Figure 4D,D’; H,H’). In Oncopeltus, severe ubr3 RNAi embryos were almost completely ablated, leaving unidentifiable ectodermal tissue connected to everted presumptive visceral tissue (Figure 4—figure supplement 1). More mildly affected embryos showed some apparent segment identity, with head and eyes, but no appendages and limited evidence for correct axial polarity (Figure 4H,H’ and Figure 4—figure supplement 1). As observed in Tribolium, RNAi, knockdown of mlpt, svb, and ubr3 in hemiptera also leads to strong cuticle defects including the loss of trichomes (Figure 4—figure supplement 7).

![Figure 4.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-v1.jpg)

**Figure 4.:** Hatchlings are presented in lateral (A–D, E–H) and ventral (A’–D’ and E’–H’) views. Wild type Gerris pre-nymphs possess red pigmented eyes, and antennae that extend along the ventral side of the embryo, terminating between long legs which wrap around the embryo (A–A’). Both Gb-mlpt and Gb-svb RNAi embryos display posterior truncation, as well as loss and/or fusion of legs and head appendages (B–C’). Gb-mlpt embryos show altered eye morphology. Gb-ubr3 embryos exhibit more severe posterior, leg and eye phenotypes (D,D’). (E–H’) Phenotypes of wild type Oncopeltus (E–E’) hatchlings alongside Of-mlpt (F–F’), Of-svb (G–G) and Of-ubr3 (H–H’) RNAi. Of-mlpt and Of-svb RNAi causes posterior truncation, with the fusion/loss of thoracic segments, shortened legs and head appendages, and a reduced eye. Of-ubr3 RNAi displays similar phenotypes but stronger than Of-mlpt and Of-svb RNAi, with an apparent loss of axial polarity in severely affected Of-ubr3 RNAi embryos. Source data for Figure 4—figure supplements 1–3 are found in Source Data 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A–A”) Of-mlpt RNAi results in posterior truncation of the embryo. Mild phenotypes include abdominal shortening and weak limb defects (A), while moderate phenotypes cause strong abdominal truncation and thoracic segment fusions (A’). Severe Of-mlpt RNAi phenotypes result in loss of most abdominal segments, as well as thoracic and head appendages, and anterior segment loss (A’’). (B–B”) Weak phenotypes observed upon Of-svb RNAi knockdown include thoracic segment fusions and mild posterior abdominal segment loss (B); moderate phenotypes show severe posterior truncation, leg fusion and patterning defects (B’). Severe Of-svb RNAi phenotypes result in loss of most abdominal and thoracic segments and reduction of remaining head appendages (B”). Ofas ubr3 RNAi (C–C”) causes severe patterning defects. The mildest Of-ubr3 RNAi phenotypes, even at low dsRNA concentrations, result in loss of most abdominal segments and severe reduction or loss of leg segments (C). Moderate Of-ubr3 RNAi phenotypes cause further embryo reduction and appendage loss (C’), and severe Of-ubr3 RNAi phenotypes results in near ablation of the embryo; only limited ectodermal tissue remains, which may include a severely reduced head and loosely connected body segments of uncertain identity (C’’). (D) Quantification of Ofas RNAi embryo truncation phenotypes. Wild type (wt) as well as RNAi hatchlings from knockdown of each gene were measured from head to most distal point along the midline. Measurements were grouped for each genotype and compared using one-way ANOVA. ****, p-value<10E-9. N = 22 (wt), 48 (Of-mlpt), 106 (Of-svb) and 54 (Of-ubr3).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Dorsal view of control (A), Gb-svb RNAi (B), Gb-mlpt RNAi (C) and Gb-ubr3 RNAi (D) Gerris buenoi prenymphs. (A) Morphological landmarks highlight the three thoracic (T1–T3) and abdominal (A1–A8) segments; the long T2 legs wrap around the dorsal surface in wild type. (B) A moderately affected Gb-svb RNAi hatching displays posterior truncation (segments posterior to A5 appear fused, if present). Note also strong defects in the dorsal midline. (C,D) Severe Gb-mlpt RNAi and Gb-ubr3 RNAi phenotypes, where most normal posterior structures are absent and/or fused. In all cases, RNAi embryos show alteration of thoracic appendages (red asterisks). (E) Frequency of phenotype strength observed following treatment with Gb-svb RNAi, Gb-mlpt RNAi and Gb-ubr3 RNAi. N = 146, 169 and 59 prenymphs, respectively.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** In most cases, legs are missing or fused (A). In mildest phenotypes where the three legs (L1–L3) remain individualized, they appear rounded and shorter, as seen on bisected control (YFP-RNAi, (B) and Gb-svb RNAi (C). (D) Quantification of individual leg length in the water strider Gerris. Twenty late embryos from females injected with Gb-svb ds-RNA and 22 embryos from females injected with YFP negative control were dissected and their legs measured. Gb-svb RNAi induces shortening of all legs. Data were analyzed using unpaired t tests. ****, p-value<0,0001; **, p-value<0,01; * p-value<0,05. Ant, antenna.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** Embryos show fusion of segments along the body axis as revealed by staining of sex-combs-reduced (Scr, (A, B), and Wingless (Wg, (A’, B’).

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** Developmental defects in Gerris buenoi embryos following Gb-mlpt RNAi (B,B’) and Gb-svb RNAi (C,C’) treatment. Both RNAi affects legs, antennae and mouth parts (black arrows), as shown by immunostaining against Distal-less (Dll) (A, C) and Ultrabithorax/Abdominal A (Ubx/AbdA) expression (A’,C’). Ant, antenna, L1-L3, legs.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp6-v1.jpg)

**Figure 4—figure supplement 6.:** Of-engrailed is expressed in the posterior compartment of each segment in the early (A) and late (B) germband embryos. Knockdown of Of-svb by RNAi results in segment fusion and abnormal segmentation, which is evident in the early germband (A’) and is more pronounced in the late germband (B’) where thoracic segments T2 and T3 are often fused and adjacent abdominal segments appear disordered. The germband is reduced in length, significantly broader in width, and appears incompletely differentiated. Knockdown of Of-mlpt by RNAi also causes disordered patterning, evident in the early germband (C), which is often twisted within the egg shell and exhibits disordered posterior expression. Late germband embryos (C’) exhibit anterior segment loss, frequent T2-T3 fusion, and loss of most abdominal segments. Many embryos appear to lack midline fusion, and exhibit apparent loss of directed embryo elongation, and incomplete differentiation of the germband. An, antennal; Mn, mandibular; Mx, maxillary; Lb, labial segments.

![Figure 4—figure supplement 7.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig4-figsupp7-v1.jpg)

**Figure 4—figure supplement 7.:** (A) Detailed view of cuticle and bristles in a wildtype Gerris embryo. (B) Thinning cuticle with missing trichomes in an embryo with reduced Gb-svb. (C) Lateral view of a wild type Oncopeltus hatchling showing characteristic cuticle aspect and pigmentation. Thin, uneven cuticle is observed in knockdown embryos from Of-mlpt RNAi (D), Of-svb RNAi (E) and Of-ubr3 RNAi (F).

Taken together, these data highlight deep conservation of the Mlpt/Ubr3/Svb module in basal, ‘short germ’ insects, both in patterns of embryonic expression and in segmentation function.

### Functional conservation of Mlpt/Ubr3/Svb module in alternative long-germ insects

Since all basally branching insect species examined showed evidence of conserved function of this module in segmentation, we assayed the expression and putative function of the tripartite gene module in the jewel wasp Nasonia vitripennis, an insect species with a derived segmentation mode.

Like Drosophila, Nasonia has evolved long germ embryogenesis, in which the embryo is mostly patterned in the context of the syncytial blastoderm, and which has evolved independently several times in the insect phylum (Liu and Kaufman, 2005; Misof et al., 2014; Rosenberg et al., 2009). Previous work has identified the key role of maternal determinants and gap genes in Nasonia, which largely resemble that of Drosophila where most segmentation occurs in the blastoderm (Brent et al., 2007; Lynch et al., 2006), with some residual character of delayed segment patterning of the most posterior segments after cellularization (Rosenberg et al., 2009).

In Drosophila, whereas svb early expression is absent from posterior segments and restricted to two stripes in the head (Mével-Ninio et al., 1995) (Figure 5A,B), tal/mlpt is expressed more broadly throughout the blastoderm (Figure 5D,E) with a striped pattern evoking that of the pair-rule gene hairy (Galindo et al., 2007). Consistent with previous studies, we confirmed that the absence of tal/mlpt, svb or Ubr3 does not alter segmentation, as deduced from analysis of mutant embryos lacking both maternal and zygotic contribution for each of the three genes (Figure 5M–P and Figure 5—figure supplement 1).

![Figure 5.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig5-v1.jpg)

**Figure 5.:** (A–F) In situ hybridization of Drosophila embryo to svb (A–C) and tal/mlpt (D–F) mRNA. In blastoderm and gastrula embryos, svb mRNA is restricted to two stripes in the head (A,B) while tal is expressed in seven thin stripes in the presumptive abdomen (D,E). At late embryonic stages, svb and tal are expressed in epidermal trichome cells (C,F). (G–L) Expression of Nv-svb (G–I) and Nv-mlpt (J–L) in Nasonia embryo. Nv-svb is expressed in the mid (G) blastoderm in a single broad stripe, and in the late (H) blastoderm in two stripes. Early Nv-mlpt mRNA expression is observed as an anterior cap and a stronger posterior domain (J); anterior expression fades with enrichment of a strong stripe at the posterior as embryogenesis progresses (K). Late Nasonia embryos exhibit widespread Nv-svb and Nv-mlpt expression, with enrichment in a segmental pattern similar to the pattern of trichomes (I, L). (M–P) Cuticles of Drosophila young larvae. (M) Wild type larva showing typical pattern of ventral and dorsal trichomes. Embryos lacking maternal and zygotic tal (O), svb (N), and ubr3 (P) completely lack embryonic trichomes, and exhibit general cuticle defects. (Q–T) Cuticles of Nasonia larvae. (Q) Wild type larva with 4 pairs of spiracles (yellow arrowheads), on thoracic segment T2, and abdominal segments A1, A2 and A3. Cuticles of Nv-mlpt (S) and Nv-svb (R) RNAi larvae are extremely truncated with loss/fusion of most abdominal segments. Fusion of remaining anterior segments are also detected in Nv-mlpt embryos with only one remaining spiracle, Nv-svb larva shows fusion of thoracic segments. Nv-ubr3 RNAi larva exhibit dramatic phenotypes with little or no cuticle. Milder phenotype (T) includes a shortened larva with a thin cuticle decorated with few denticles on the anterior side.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Immunostaining for the Wg protein shows the segmentation profile of stage-10 embryos and highlights the correct pattern for tal (B), svb (C) and ubr3 (D) mutant embryos compared to control (A).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Maternal Nv-svb is broadly expressed in freshly laid embryos, with obvious posterior enrichment. (B) During blastoderm stages, posterior expression resolves into a broad band, detached from the posterior and clear behind the stripe. (C, D) Broad low-level blastoderm expression clears, leaving strong central Nv-svb expression resembling that of Nv-Kr. (E–F) At cellularization, the central domain is refined and sharpened, and a faint posterior band begins to emerge, at approximately the same position as an Nv-eve posterior stripe, which demarcates the anlage that will give rise to six posterior segments. At gastrulation, a dorsal stripe of Nv-svb emerges as the central stripe of Nv-svb fades and the posterior stripe darkens (H–J) and eventually splits into two discrete stripes (J). At germband retraction, strong staining is evident in the head and in spots along the ventral side of the embryo (K). During dorsal closure, epidermal expression starts as ventral segmental stripes, which extend dorsally and prefigure the pattern of cuticle trichomes; head expression remains strong throughout the remainder of embryogenesis (L–O).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Maternal expression of Nv-mlpt is strong (A), persisting for several nuclear divisions in syncytium (B). This expression clears approaching cellularization (C), leaving a wedge shaped posterior domain that is slightly withdrawn from the posterior pole. Slightly later, an anterior domain arises, and the stronger posterior domain extends to the posterior end (seen from both lateral (D) and dorsal (E) view). At cellularization, anterior expression remains, while posterior expression has resolved into two distinct stripes: an anterior broad stripe, and a thin posterior stripe at the extreme posterior (F, G). At gastrulation, dorsal expression of Nv-mlpt is apparent, as well as two lateral stripes of expression (H); dorsal expression persists through germband extension, when new ectodermal stripes arise (I). At germband retraction, strong spots of expression are evident in the head and ventrally surface, in nearly every segment (J; dorsal view K). As dorsal closure begins (L), expression is restricted to these spots, while at the end of dorsal closure, expression is seen throughout the embryo, including segmental stripes prefiguring ventral trichome belts, and in strong spots in the head (M–O).

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** (A–E). Embryonic expression of Nv-dusky-like (Nv-dyl) mRNA. Nv-dyl is faintly expressed in freshly laid embryos (A) then disappears (B, C). Nv-dyl is observed again only at dorsal closure with strong expression in discrete structures bilaterally in the head (D,D’) (‘SG’- salivary gland). Later embryos exhibit staining in segmental stripes with additional puncta prefiguring the bristles of the larval cuticle (E). (F–K) Embryonic expression of Nv-singed (Nv-sn). Nv-sn mRNA maternal expression is strong, with ubiquitous staining in freshly laid embryos (F). Signal rapidly fades at cellularization (G) and through gastrulation (H). At germband retraction (I), dots of Nv-sn expression are seen in the head, in the most posterior segment, and along the ventral side, prefiguring segmental dots that darken during dorsal closure (J). Dots correspond to nervous system (ventral) and putative mesodermal derivatives (dorsally). At the end of embryogenesis (K), segmental stripes are seen along the ventral epidermis with strong staining in the head.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** (A–A”) Cuticle phenotypes of Nv-mlpt RNAi embryos. Mild RNAi phenotypes from Nv-mlpt knockdown result in loss of posterior abdominal segments, which can be seen as reduction in larval cuticle length and loss of posterior trichomes (A). Moderate RNAi phenotypes cause more severe posterior truncation and segment fusions (A’). Severe RNAi phenotypes from Nv-mlpt RNAi (A”) cause loss of most posterior segments, fusion of remaining abdominal segments, and anterior fusions in thoracic segments. (B–B”) Cuticle phenotypes of Nv-svb RNAi embryos. (B) Mild RNAi phenotypes from Nv-svb RNAi result in shortened larval cuticles with missing posterior trichomes; occasionally, ectopic spiracles (normally restricted to T2 and A1-A3) are apparent on A4 (blue arrowhead). Moderate phenotypes (B’) are even more truncated, with loss of posterior structures. Severe phenotypes (B”) to dramatically truncated embryos, with loss of all posterior abdominal segments, fusions of remaining anterior abdominal segments, but normal anterior terminal structures. Yellow arrowheads indicate remaining T2 spiracle and single remaining spiracle associated with likely fused A1-A3 abdominal segments. Nv-ubr3 RNAi resulted in severe defects in cuticle secretion, and very fragile embryos which were impossible to recover intact. Rare mildest phenotypes are shown (C’–C”) compared to mock RNAi (C) for normal morphology reference. Wild type and mock RNAi larval cuticles possess four spiracles on segments T2, A1, A2 and A3 (yellow arrowheads), and stereotypic bands of trichomes on thoracic and abdominal segments. Mild RNAi phenotype of Nv-ubr3 knockdown causes posterior truncation of the embryo, and loss of posterior trichomes (posterior to A3). Anterior terminal structures appear intact.

In contrast, in Nasonia, both Nv-mlpt and Nv-svb are expressed in the early embryo, in adjacent prominent stripes at the posterior region of embryo (Figure 5G–K) that acts as the progenitor of the late-forming segments (Rosenberg et al., 2014). Nv-svb is also expressed in a prominent stripe in the middle of the embryo (Figure 5G–H and Figure 5—figure supplement 2), similar to expression of the thoracic gap gene, Nv-krüppel (Brent et al., 2007), while Nv-mlpt expression has an anterior cap, and broad expression posterior to the Nv-svb domain (Figure 5J–K and Figure 5—figure supplement 3). In both Nasonia and Drosophila, later expression of svb and mlpt after germband extension prefigures the pattern of epidermal trichomes (Figure 5C,F; I,L and Figure 5—figure supplements 2 and 3). Consistent with this observation, we find that several Svb target genes encoding trichome effectors in flies are also expressed with a similar pattern in late Nasonia embryos (Figure 5—figure supplement 4). Thus, in a wide range of insects, complementary and/or overlapping expression of svb and mlpt in the embryo correlates with an essential role in embryonic segmentation.

The stereotyped pattern of trichomes (also known as denticles, hairs or microtrichia) is distinctive along the anterior-posterior and dorso-ventral axes, providing a readout for correct segmentation. In flies, although trichomes are severely reduced (hence, ‘shaven’) in the thin cuticles of mutants for svb, tal, or ubr3 (Figure 5M–P), all segments are still formed (Figure 5—figure supplement 1). In the cuticle of Nasonia, the trichome pattern highlights three thoracic segments and 10 abdominal segments; four spiracles (located on thoracic segment T2 and abdominal segments A1- A3) provide landmarks for segment identification (Pultz et al., 2000). Nv-mlpt RNAi causes posterior truncation and segment fusions, evident as severely shortened larvae, with two remaining trichome belts that likely correspond to thoracic and anterior abdominal segments (Figure 5Q,S and Figure 5—figure supplement 5A–A’’). Similarly, Nv-svb RNAi causes severe posterior truncation and loss of most abdominal segments, with only one or two pairs of spiracles left (Figure 5R and Figure 5—figure supplement 5B–B’’). Larvae from Nv-ubr3 RNAi were almost uniformly too fragile to recover (not shown), likely owing to the observed absence/thinning of cuticle. Mildly affected Nv-ubr3 RNAi larvae exhibit thin cuticle, devoid of trichomes on the posterior (Figure 5T and Figure 5—figure supplement 5D,D’).

Altogether, our data support conserved functions for mlpt, svb and ubr3 in embryonic segmentation of Nasonia vitripennis, a long germ insect, leaving only Drosophila from among species tested without such an early patterning function.

### Restoring svb expression in the early Drosophila embryo disrupts segmentation

Since we find this functional module to be ancestral and deeply conserved in both short and long germ insects, we sought to investigate how the module lost its segmentation role in flies. Drosophila ubr3 is ubiquitous and tal is expressed in pair-rule like stripes, but svb expression is absent in the abdomen at early embryonic stages (see Figure 5). We therefore hypothesized that the loss of the segmentation function of this module may have involved the loss of svb expression during early embryogenesis in the lineage leading to Drosophila.

To test this hypothesis, we added back svb expression to the early embryo to mimic svb early expression that is observed in Tribolium, Oncopeltus, Gerris, and Nasonia, using the Gal4/UAS system (Brand and Perrimon, 1993). Strikingly, ectopic expression of svb in the early embryo (using nullo-Gal4) resulted in strong segmentation defects, with no detectable effects on tal expression (Figure 6A–B”). We also noticed dramatically increased cell death, as also recently reported in activation of segmentation genes (Crossman et al., 2018). Similar defects were also observed following maternal ectopic svb expression (Figure 6—figure supplement 1), albeit with stronger induction of lethality. These results suggest that the loss of svb expression prevents segmentation function of the trio during early embryogenesis in flies, and thus indicates that the function of the tal/svb/ubr3 module in segmentation is contingent upon expression of all three partners.

![Figure 6.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig6-v1.jpg)

**Figure 6.:** Top panels show in situ hybridization of svb (A–D) and tal (A’–D’) mRNA and anti-Wingless (Wg) immunostaining (A”–D”) at gastrulation stage in control conditions (nullo >GFP) and following the ectopic expression (driven by nullo-Gal4) of wild type Svb (B–B”), Svb-ACT (C–C”) and Svb-3Kmut (D–D”), which mimics or prevents Pri/Ubr3-mediated processing of Svb, respectively. (A’’’–D’’’) show cuticle preparations of control (A’’’), nullo >Svb (B’’’), nullo >Svb ACT (C’’’) and nullo >Svb-3Kmut (D’’’) embryos. (E–F’) panels show immunostaining for the Wingless protein and cuticle preparations of control (E–E’) and svb ectopic expression (nullo >Svb) (F–F’) in a tal null genetic background. tal mutant embryos display characteristic trichome loss and cuticle defects. (G) Quantification of segmental defects for each genotype. Data were analyzed by one-way ANOVA. ***, p-value<0,002; ns, non-significant. Total numbers of embryos are 177 (ctrl), 62 (Svb), 621(Act), 413 (3Kmut), 223 (tal-/-) and 138 (tal-/-, Svb). Source data for Figure 6G are found in Source Data File 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Expression of svb from oogenesis using mat-Gal4 (B,B’) and nanos-Gal4 (C–C’), or from blastoderm stage using nullo-Gal4 (D,D’), alters segmentation as seen on embryos stained with anti-Engrailed (En) antibody (A–D) and by cuticle analysis (A’–D’).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/39748/elife-39748-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** UAS-GFP (control) (A,A’), UAS-Svb-ACT (B,B’) and UAS-Svb-3Kmut (C,C’) were expressed in the embryonic epidermis under the control of the ptc-Gal4 driver. Top rows show whole embryo cuticles (A–C), the bottom row shows close-ups in the ventral region of the third abdominal segment (A’–C’). Svb-ACT, which lacks the N-terminal repressor domain and thus mimics the processed form of Svb, acts as a constitutive activator of transcription and triggers the production of ectopic trichomes. In contrast, Svb-3Kmut -bearing mutations on the 3 Lysines ubiquitinated by Ubr3 in response to Tal peptides- behaves as a repressor and counteracts endogenous Svb activity, resulting in loss of trichomes.

To further evaluate this conclusion, we tested whether the segmentation defects resulting from Svb ectopic expression involved the function of naturally expressed tal and ubr3 members of the module. To do this, we generated a transgene encoding an N-terminal truncated Svb protein, lacking the N-terminal repression domain, thereby mimicking the shorter Svb activator form (Svb-ACT) that otherwise results from Tal/Ubr3-mediated processing (Kondo et al., 2010; Zanet et al., 2015). Reciprocally, we engineered a transgenic Svb variant insensitive to processing (Zanet et al., 2015), by mutating the 3 Lysine residues that are recognized and ubiquitinated by Ubr3 (Svb-3Kmut). As expected, the expression of Svb-ACT and Svb-3Kmut in the embryonic epidermis leads to ectopic trichomes and trichome loss, respectively (Figure 6—figure supplement 2). When expressed in the early embryo, Svb-Act causes segmentation defects that are reminiscent of those obtained by Svb over-expression, albeit at higher frequency (Figure 6C–C”). In contrast, expression of Svb-3Kmut, which is insensitive to Tal/Ubr3, in the early embryo did not cause segmentation defects (Figure 6D–D”). These results indicate that the segmentation defects observed upon Svb ectopic expression in early embryos rely on its processing into the activator form, and that, in this context, ectopic Svb can be regulated by endogenous Tal peptides. To further reinforce this conclusion, we assayed the consequences of Svb ectopic expression in early Drosophila embryos lacking tal function. Compared to otherwise wild-type embryos, the ectopic expression of Svb in the absence of tal failed to cause any detectable defects in segmentation (Figure 6E–G), while impaired epidermal differentiation is obvious.

Taken together, these data support the conclusion that the cooperativity of this gene module has remained intact throughout evolution, and that the inactivation of its function in Drosophila segmentation involved abrogation of early expression of Svb, an essential component of the module.

## Discussion

Our experiments reveal how a cooperative trio of molecules, initially discovered within a more restricted capacity during terminal epidermal differentiation in Drosophila, possesses important ancestral functions in insect embryonic segmentation. These findings represent a significant addition to the anterior-posterior patterning network in insects and provide novel insights into how conserved molecular complexes may contribute to organismal evolution.

Together with the conserved protein structural signature motifs underlying regulatory interactions between Mlpt peptides and Ubr3/Svb proteins, we present evidence for several conserved functions of this module across considerable evolutionary distances. Upon the inactivation of any of the three functional partners, all insects representing both ancestral and derived segmentation modes exhibit strong epidermal defects, evident both in trichome differentiation and in the thinning of the cuticle. The epidermal functions of the module, the most well-described in flies, likely involve the conservation of a similar set of target genes. Several Svb epidermal targets identified in Drosophila melanogaster (Chanut-Delalande et al., 2006; Fernandes et al., 2010; Menoret et al., 2013) and sister species (Chanut-Delalande et al., 2006) are indeed similarly regulated in Tribolium (Li et al., 2016). Expression patterns of Svb epidermal target genes in Nasonia support a similar conclusion.

A second shared function across all species examined is the importance of Mlpt/Ubr3/Svb for leg specification and patterning, as initially reported in flies (Galindo et al., 2007; Pueyo and Couso, 2008; Pueyo and Couso, 2011). Analysis of more basal insects shows that inactivation of any of the three partners leads to shortened and misdifferentiated legs, often with missing/fused segments, in particular in their distal parts. The conserved outputs of this module highlight transcriptional networks downstream of Svb whose connectivity also appears largely intact over large evolutionary distances (Spanier et al., 2017). Together, these data underscore the ancestral conservation of a functional tripartite molecular complex, of its target transcriptional networks and roles in embryonic/post-embryonic development, dating to early in the radiation of arthropods.

Outside of Drosophila, we demonstrate function of the module in the formation of posterior segments in all species tested, delineating a key module for insect embryonic segmentation. A strong domain of svb expression in the growth zone is observed in all short germ species examined, often adjacent to a strong mlpt expression domain. In the long germ wasp embryo, Nv-mlpt and Nv-svb are also expressed in adjacent/partly-overlapping domains, at the time they function in segmentation. The existence of mlpt/svb boundaries may result from mutual exclusivity between svb and mlpt expression. Such abutting stripes of mlpt (tal in flies) and svb have been described in formation of adult leg joints in flies (Pueyo and Couso, 2011). It is worth mentioning that the Mlpt/Svb function in leg joint formation in flies involves Notch-mediated signaling (Pueyo and Couso, 2011), a pathway required for coordination of the segmentation clock from basal arthropods (Chipman and Akam, 2008; Eriksson et al., 2013; Stollewerk et al., 2003) to mammals (Hubaud and Pourquié, 2014). The Svb/Mlpt expression boundaries at the interface between blastoderm and (oscillation-driven) growth zone in insects thus invites further study, for example to assay whether it might constitute a retracting wavefront (regulated by a speed regulator (Zhu et al., 2017)) which is smoothened by Mlpt diffusion and may serve to sharpen and polish expression boundaries of pair-rule genes or other gap genes, a role comparable to that of Notch during somitogenesis (Dequéant and Pourquié, 2008).

Beyond insects, Svb (also known as Ovo or OvoL) is conserved in all animals, and predates bilateria (Kumar et al., 2012). In addition to the germline and epidermis (Dai et al., 1998; Lee et al., 2014; Nair et al., 2006), recent studies have uncovered a broader role of OvoL/Svb in epithelial organization and regulation of Epithelial-Mesenchymal Transition (Bai et al., 2018; Kitazawa et al., 2016; Lee et al., 2014; Nieto et al., 2016; Watanabe et al., 2014). Although the sequential nature of segmentation and posterior segment addition – in both invertebrates and vertebrates – is well known from classical embryology, the cellular mechanisms integrated in the function of the growth zone, that is the contribution of cell division, cell movement, and cytoskeletal reorganization, remain only incompletely understood, including in insects (Williams and Nagy, 2017). As in germband elongation of the Drosophila embryo (Collinet et al., 2015; Munjal et al., 2015), which occurs after segmentation in this derived species, the elongation of short germ embryos likely also relies heavily on cytoskeletal rearrangements (Mao and Lecuit, 2016). Interestingly, basal insect embryos with reduced mlpt or svb often appear deficient in convergent extension (Figure 2 and Figure 4—figure supplement 4), suggesting that this module may be involved in the control of cytoskeletal rearrangement during segmentation. The development of suitable tools for live-imaging of cell/cytoskeleton dynamics in a growing number of species (Auman and Chipman, 2017; Benton, 2018) will offer new ways to investigate the cellular mechanisms of segment addition and to decipher the role of the Mlpt/Ubr3/Svb module therein.

Recent advances in mapping protein-protein interactions at a proteome-wide scale show the unexpected prevalence of ancestral macromolecular complexes, highly conserved across metazoans (Wan et al., 2015). Multi-protein complexes appear to evolve more slowly than gene regulatory networks (Tan et al., 2007), mirroring deep conservation of protein-protein interaction domains across orthologues. How might ancient protein complexes that are evolutionarily stable throughout animals nevertheless undergo phenotypic diversification and incorporate novelty? Our data show that Ubr3 is required for the activity of the complex, but its function is clearly permissive, as seen by ubiquitous expression across species. In contrast, the dynamic patterns of mlpt/tal and svb highlight the key aspect of the control of their expression. Evolutionary changes in enhancers and associated trans-acting factors of these two instructive members of the module likely underlie evolution of their function in segmentation. Svb enhancers are well-documented for their modifications across Tephritidae and Drosophilidae, which are causal for the evolution of trichome pattern (Frankel et al., 2011; Frankel et al., 2012; Khila et al., 2003; McGregor et al., 2007; Preger-Ben Noon et al., 2016; Sucena et al., 2003). A similar change in promoter control of Svb expression may be sufficient to bring segment patterning potency on- or off-line in the insect embryo. The phylogenetic distribution within insects of short/long germ modes of development implies that evolution has repeatedly sampled these modes (Misof et al., 2014). Recent data support a model in which segmentation mechanisms in short and long germ insects are more similar than initially thought (Benton, 2018; Clark, 2017), and mostly differ in the specifics of their timing (Zhu et al., 2017). Our data suggest one mechanism by which delayed posterior segment formation may be switched on/off via Svb/Mlpt/Ubr3.

Together, our data suggest how integration of a post-translational mechanism involving a micropeptide like Mlpt can be used in combination with transcriptional control to regulate Svb, both in protein activity and expression timing, to broadly regulate phenotypic plasticity during embryogenesis. This suggests future research directions integrating insights from evolution of transcriptional regulation and micropeptide discovery into the functional study of multi-protein complexes, to facilitate the elucidation of mechanisms of and constraints upon organismal evolution.

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
      <td>Gene (Drosophila melanogaster)</td>
      <td>ovo/svb</td>
      <td>NA</td>
      <td>FLYB:FBgn0003028</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>tal</td>
      <td>NA</td>
      <td>FLYB:FBgn0087003</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Ubr3</td>
      <td>NA</td>
      <td>FLYB:FBgn0260970</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Tribolium castaneum)</td>
      <td>Tc-svb</td>
      <td>this paper</td>
      <td>Genbank: MG913606</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Tribolium castaneum)</td>
      <td>mlpt</td>
      <td>NA</td>
      <td>GenBank: AM269505.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Tribolium castaneum)</td>
      <td>Tc-Ubr3</td>
      <td>NA</td>
      <td>NCBI Ref Seq: XM_964327</td>
      <td>beetlebase: TC005949</td>
    </tr>
    <tr>
      <td>Gene (Oncopeltus fasciatus)</td>
      <td>Of-svb</td>
      <td>this paper</td>
      <td>GenBank: MH181832</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Oncopeltus fasciatus)</td>
      <td>Of-mlpt</td>
      <td>this paper</td>
      <td>GenBank: MH181830</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Oncopeltus fasciatus)</td>
      <td>Of-Ubr3</td>
      <td>this paper</td>
      <td>GenBank: MH181827</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Gerris buenoi)</td>
      <td>Gb-svb</td>
      <td>this paper</td>
      <td>GenBank: MH011417</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Gerris buenoi)</td>
      <td>Gb-mlpt</td>
      <td>this paper</td>
      <td>GenBank: MH699965</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Gerris buenoi)</td>
      <td>Gb-Ubr3</td>
      <td>this paper</td>
      <td>GenBank: MH011418</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Nasonia vitripennis)</td>
      <td>Nv-svb</td>
      <td>this paper</td>
      <td>GenBank: MH181831</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Nasonia vitripennis)</td>
      <td>Nv-mlpt</td>
      <td>this paper</td>
      <td>GenBank: MH181829</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Nasonia vitripennis)</td>
      <td>Nv-Ubr3</td>
      <td>this paper</td>
      <td>GenBank: MH181828</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Nasonia vitripennis)</td>
      <td>AsymCx</td>
      <td>PMID: 20075255</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>FM7C, Kr &gt; GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 5193; FLYB: FBst0005193; RRID:BDSC_5193</td>
      <td>FlyBase symbol: Df(1)JA27/FM7c, P{w[+mC]=GAL4 Kr.C}DC1, P{w[+mC]=UAS GFP.S65T}DC5, sn[+]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>TM6B, ubi-GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 4887; FLYB: FBst0004887; RRID:BDSC_4887</td>
      <td>FlyBase symbol: w[1118]; Df(3L)Ly, sens[Ly-1]/TM6B, P{w[+mW.hs]=Ubi GFP.S65T}PAD2, Tb[1]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>TM3, twist-GAL4 &gt; GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 6663; FLYB: FBst0006663; RRID:BDSC_6663</td>
      <td>FlyBase symbol: w[1118]; Dr[Mio]/TM3, P{w[+mC]=GAL4 twi.G}2.3, P{UAS-2xEGFP}AH2.3, Sb[1] Ser[1]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>nullo-GAL4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:26875; FLYB:FBtp0018484; RRID:BDSC_26875</td>
      <td>FlyBase symbol: P{nullo-GAL4.G}5.20</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>nos-GAL4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:4937; FLYB:FBtp0001325; RRID:BDSC_4937</td>
      <td>FlyBase symbol: P{GAL4::VP16- nos.UTR}CG6325MVD1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ptc-GAL4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:2017; FLYB:FBti0002124; RRID:BDSC_2017</td>
      <td>FlyBase symbol: P{GawB}ptc559.1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>pri[1]</td>
      <td>PMID:17486114</td>
      <td>FLYB:FBal0198099</td>
      <td>Flybase symbol: talS18</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>tal[S18.1]</td>
      <td>PMID:17486114</td>
      <td>FLYB:FBal0241050</td>
      <td>Flybase symbol: talpri-1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>pri[4]</td>
      <td>gift from Y. Kageyama</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>pri[5]</td>
      <td>gift from Y. Kageyama</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>svb[R9]</td>
      <td>PIID: 12915226</td>
      <td>FLYB:FBal0151651</td>
      <td>Flybase symbol: ovo[svb-R9]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ovo[D1]</td>
      <td>PMID: 17246182</td>
      <td>BDSC: 23880; FLYB: FBst0023880; RRID:BDSC_23880</td>
      <td>Flybase symbol: ovo[D1]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>svb[PL107]</td>
      <td>PMID: 11744370</td>
      <td>DGGR:106675; FLYB: FBst0305341; RRID:DGGR_106675</td>
      <td>Flybase symbol: ovo[PL107]</td>
    </tr>
    <tr>
      <td>Genetic reagent  (D. melanogaster)</td>
      <td>Ubr3B</td>
      <td>PMID: 26383956</td>
      <td>FLYB:FBal0013375</td>
      <td>Flybase symbol: Ubr3[B]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>FLYB:FBal0129171</td>
      <td>FlyBase symbol: w[*]; P{w[+mC]=UAS GFP .S65T}Myo31DF[T2]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-svb::GFP</td>
      <td>PMID: 20647469</td>
      <td>FLYB: FBal0319860</td>
      <td>FlyBase symbol: ovoUAS.svb.GFP</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-pri</td>
      <td>PMID: 17486114</td>
      <td>BDSC: 1521; FLYB:FBti0003040; RRID:BDSC_1521</td>
      <td>FlyBase symbol: talUAS.cKa</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-svbACT::GFP</td>
      <td>this paper</td>
      <td>FLYB:FBal0248431</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-svb-3Kmut::GFP</td>
      <td>this paper</td>
      <td>FLYB:FBal0241056</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Wingless</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td></td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ubx-AbdA</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td></td>
      <td>(1:5)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Dll abbit polyclonal</td>
      <td></td>
      <td>DSHB Cat# 4d4; RRID:AB_528512</td>
      <td>(1:200) r</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Dig AP Fap (polyclonal sheep)</td>
      <td>Roche</td>
      <td>DSHB Cat# UBX/ABD-A FP6.87; RRID:AB_10660834</td>
      <td>(1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse-HRP (rabbit polyclonal)</td>
      <td>Promega</td>
      <td></td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit-HRP (donkey polyclonal)</td>
      <td>Jackson Immuno Research</td>
      <td>Roche Cat# 11093274910; RRID:AB_514497</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse biotinylated (goat polyclonal)</td>
      <td>Vector Laboratories</td>
      <td>Promega Cat# W4011; RRID:AB_430833</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pUASp-Svb::GFP (plasmid)</td>
      <td>PMID:17486114</td>
      <td>Jackson ImmunoResearch Labs Cat# 711-035-152; RRID:AB_10015282</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pUASp-SvbAct::GFP (plasmid)</td>
      <td>this paper</td>
      <td>Vector Laboratories Cat# BA-9200; RRID:AB_2336171</td>
      <td>Progenitors: PCR, pUASp-Svb::GFP</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pUASp-Svb-3Kmut::GFP (plasmid)</td>
      <td>this paper</td>
      <td></td>
      <td>Progenitors: pAc-SvbK7; pUASp-Svb::GFP</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCR-Topo (plasmid)</td>
      <td>Qiagen</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBluescript (plasmid)</td>
      <td>Stratagene</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pGEM-Teasy (plasmid)</td>
      <td>Promega</td>
      <td>Quiagen Cat#: 231122</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBac (3xP3-EGFPafm) (plasmid)</td>
      <td>gift from E. Wimmer</td>
      <td>Stratagene Cat#: 212205</td>
      <td>Flybase symbol: PBac{3xP3-EGFPafm}</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBME(TcU6b-BsaI) (plasmid)</td>
      <td>gift from A. Giles</td>
      <td>Promega Cat#: A1360</td>
      <td>Original gRNA expression vector with Bsa1 sites</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSLfa(Hsp-p-nls-Cas9-3’UTR)fa (plasmid)</td>
      <td>gift from A. Giles</td>
      <td>FLYB: FBtp0014061</td>
      <td>Cas9 expression vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Tc-U6b-sim ZS1 (plasmid)</td>
      <td>Rode and Klingler, unpublished</td>
      <td></td>
      <td>sim gRNA expression vector</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>seeSupplementary file 1B for a complete list of oligonucleotides used in this paper</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DIG RNA Labeling kit</td>
      <td>Roche</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NBT-BCIP solution</td>
      <td>Roche</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>In-Fusion HD Cloning Kit</td>
      <td>Clontech</td>
      <td>Roche Cat#: 11 277 073 910</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MEGAscript RNA kit</td>
      <td>ThermoFischer</td>
      <td>Sigma Cat#: 72091</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Blocking reagent</td>
      <td>Roche</td>
      <td>Takara Cat#: 21416</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3,3′-Diaminobenzidine tetrahydrochloride hydrate</td>
      <td>Sigma</td>
      <td>ThermoFischer Cat#: AM1626</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Next-RNAi</td>
      <td>http://www.nextrnai.org</td>
      <td>Roche Cat#: 11 096 176 001</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Primer3</td>
      <td>https://primer3plus.com</td>
      <td>Sigma Cat#:32750</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MacVector</td>
      <td>https://macvector.com</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 8</td>
      <td>https://www.graphpad.com/</td>
      <td>Primer3Plus; RRID:SCR_003081</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Photoshop CC 2019</td>
      <td>https://www.adobe.com/</td>
      <td>MacVector; RRID:SCR_015700</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Illustrator CC 2019</td>
      <td>https://www.adobe.com/</td>
      <td>GraphPad Prism; RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Acrobat Pro DC</td>
      <td>https://www.adobe.com/</td>
      <td>Adobe Photoshop; RRID:SCR_014199</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Axiovision 4.6.3.SP1</td>
      <td>Zeiss</td>
      <td>Adobe Illustrator; RRID:SCR_010279</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Tribolium castaneum

Insects were reared at ambient temperature of 25°C. Embryos were collected and whole-mount in situ hybridization performed as previously described (Patel et al., 1989; Schinko et al., 2009; Tautz and Pfeifle, 1989). Digoxigenin- labelled RNA probes were detected using alkaline phosphatase-conjugated anti-DIG antibodies (1:2000; Roche) and NBT/BCIP substrates (Roche), as per manufacturer's instructions. Sequence of all oligonucleotides used in this study (for the five insect species) is given in Supplementary file 1B.

Double-stranded RNA synthesis and parental injection were performed as described previously (Bucher and Klingler, 2004; Bucher et al., 2002). dsRNAs were injected into female pupae or virgin adult females at a concentration of 1–3 µg/µl. RNAi phenotypes were confirmed by using non-overlapping dsRNA fragments for each gene. First instar larval cuticles were cleared in Hoyer’s medium/lactic acid (1:1) overnight at 60°C. Cuticle auto-fluorescence was detected on a Zeiss Axiophot microscope. Z stacks and projections were created with a Zeiss ApoTome microscope using the Axiovision 4.6.3.SP1 Software. Color images were taken by (ProgResC14) using the ProgResC141.7.3 software and maximum projection images were created from z stacks using the Analysis D software (Olympus).

For Tribolium svb, all primer pairs shown were used to generate template for dsRNA synthesis. Amplicons generated by the last four pairs were also used for antisense RNA probe synthesis. dsRNA fragments corresponding to different regions of the svb transcript were used for gene knockdown by RNAi. All dsRNA fragments resulted in similar knockdown phenotypes with high penetrance. Primers were designed based on the Next-RNAi software, Primer3 or MacVector. The nucleotides shown in red indicate tags of parts of T7 (3’ primer) and SP6 (5’ primer) promoter sequences attached to gene-specific sequences in the manner described by Schmitt-Engel et al. (2015).The products were used for a second PCR using T7 and SP6-T7 primers for generating a double stranded template for in vitro transcription by T7 polymerase. For in situ RNA probes, the second PCR was done using the complete T7 and SP6 promoter sequences and subsequently in vitro transcription was performed to generate a Digoxigenin-labelled antisense RNA probe with the appropriate polymerase. Amplicons that were cloned into pBluescript vector were amplified with T7 and T3-T7 primers for subsequent dsRNA synthesis or T7 and T3 primers for subsequent antisense RNA probe synthesis using either T3 or T7 RNA polymerase. The primer design was based on the RNAseq data (Tcas au5 prediction) for Tc-svb available on iBeetle-Base. For mlpt dsRNA and probe synthesis, a full-length mlpt cDNA cloned into pBluescript was obtained from Dr. Michael Schoppmeier. For Tc-ubr3, all primer pairs shown were used for dsRNA synthesis. All dsRNA fragments resulted in similarly strong knockdown phenotypes with very high penetrance. The fragments generated with the primers containing iBeetle numbers were also used as probes.

To generate a Tc-svb mutant using CRISPR/Cas9, gRNAs were directed to the putative transactivation domain in exon 2 of Tc-svb. The sequence of primers used is given in Supplementary file 1C, with the G (required by the U6 promoter for transcription initiation) marked in green, the PAM sequence in blue, and the sequences in orange representing the complementary overhangs generated by Bsa1 digestion. A fourth gRNA was directed to the Tribolium single-minded gene (Tc-sim, Rode and Klingler, unpublished). Embryonic injection mix consisted of 125 ng each of the four gRNA expression vectors, 500 ng of the donor eGFP vector containing the sim target sequence, and 500 ng of the Cas9 expression vector. Non-homologous end joining (NHEJ) method was employed for directed knock-in of an eGFP containing donor marker plasmid (Supplementary file 1D) into the exon2 of the endogenous Tc-svb gene. The sim gRNA was used to target the sim sequence in the marker plasmid leading to its Cas9-induced linearization. This was followed by insertion of the linearized plasmid into one or more target sites in the Tc-svb genome. A successful knock-in of the marker plasmid was obtained only at gRNA target site 3. This insertion site was present in all Tc-svb transcripts and was also downstream from a putative second start codon, thus increasing the chances of obtaining a Tc-svb null phenotype.

### Oncopeltus fasciatus

Wild-type Oncopeltus embryos were collected on cotton from mated females, and aged, as needed, in a 25°C incubator. Embryos were first boiled for 1 to 3 min in a microfuge tube in water, followed by a 1 min incubation on ice, before further processing. Embryos were fixed in 12% heptane-saturated formaldehyde/1X PBS for 20 min with shaking. The heptane was replaced by methanol, and the embryos either stored under methanol at −20°C or processed immediately. Embryos were then rehydrated to 1X PBT through a methanol/PBT series, and dechorionated, before further fixation for 90–120 min in 4% formaldehyde/1X PBT. Embryos were then transferred to and stored in 100% methanol.

In situ hybridizations were carried out (as described for Nasonia in Rosenberg et al., 2014) on embryos peeled and stored under 100% methanol, and rehydrated through an methanol/1x PBS, 0.1%Tween (1xPBT) series. Briefly, rehydrated embryos were washed several times in 1x PBT before a 5 min post-fix in 5% formaldehyde/1X PBT, followed by 3 five minutes washes in 1X PBT. Embryos were briefly treated with Proteinase K (4 µg/ml final concentration) in 1X PBT for 5 min, followed by 3 five minute washes in 1X PBT, and an additional 5 min post-fix in 5% formaldehyde/1X PBT. Following 3 x three minute washes in 1X PBT, embryos were incubated in hybridization buffer for 5 min at room temperature, followed by incubation in fresh hybridization buffer for a 1 hr pre-hybridization step at 65°C. RNA probes were prepared and added to a fresh portion of hybridization buffer and incubated at 85°C for 5 min, then one minute on ice, before replacing pre-hybridization with hybridization buffer containing denatured RNA probe. Tubes were incubated overnight at 65°C. After washes in formamide wash buffer, embryos were washed in several changes of 1X MABT buffer, before incubation in 1X MABT +2% Blocking Reagent (BBR; Roche) for 1 hr, and then 1X MABT/2%BBR/20% sheep serum for an additional hour, before addition of fresh 1X MABT/2%BBR/20% sheep serum containing anti-DIG AP Fab fragments (1:2000; Roche) for overnight incubation at 4°C. In the morning, extensive 1X MABT washes were carried out before equilibration of embryos with AP staining buffer and then staining with AP staining buffer containing NBT/BCIP (Roche; as per manufacturer's instructions). After staining, three 1X PBT washes were carried out before a final post-fixation step (5% formaldehyde/1xPBT), and then one PBT wash before sinking in 50% glycerol/1xPBS, and then 70% glycerol/1xPBS, which was also used for mounting before imaging.

dsRNA templates were amplified from target gene fragments which had been cloned into either pCR-Topo (Qiagen) or pGEM (Invitrogen), using T7 promoter-containing oligos, as described previously (Lynch and Desplan, 2006). Purified PCR product was used for dsRNA transcription using Megascript RNAi (Ambion) according to manufacturer’s instructions. dsRNA was injected into newly eclosed virgin female milkweed bugs, at a concentration of 1–3 µg/µl. After injection, females were mated to uninjected males, and embryos were collected for the duration of egg laying. Embryos for phenotypic evaluation were incubated at 28°C for 8 days, and unhatched embryos were dissected from their membranes and imaged for phenotypes.

### Gerris buenoi

Wild type Gerris buenoi were collected from a pond in Toronto, Ontario, Canada and established in the lab. Stocks were maintained in aquaria at 25°C with a 14 hr light/10 hr dark cycle, and fed with fresh crickets. Styrofoam float pads were provided to females as substrate for egg laying. Embryos were collected and incubated at 20–25°C until desired developmental time points, at which time they were dissected in 1x PBS with 0.05% tween-20 (‘PTW’). Once dissected, embryos were fixed in 4% paraformaldehyde and stored under 100% Methanol at −20°C until use.

In situ hybridizations in Gerris were performed as previously described (Refki et al., 2014). Briefly, embryos were rehydrated to 1X PBT, through a MeOH/PTW series, and then washed 3 times in PTW to eliminate residual methanol. Embryos were then permeabilized in PBT 0.3% and PBT 1% (1X PBS; 0.3% or 1% Triton X100) for 1 hr. Following these washes, embryos were rinsed once for 10 min in a 1:1 mixture of PBT 1% and hybridization buffer (50% Formamide; 5% dextran sulfate; 100 mg/ml yeast tRNA; 10X salts). The 10X salt mix contains 3 M NaCl; 100 mM Trizma Base; 60 mM NaH2PO4; 50 mM Na2HPO4; 5 mM Ficoll; 50 mM PVP; and 50 mM EDTA. RNA probes corresponding to each gene were transcribed from cDNA templates cloned into pGEM-T (Promega), and then transcribed in vitro using either T7 or Sp6 RNA polymerase (Roche) and labelled with Digoxigenin-RNA labelling mix (Roche). Pre-incubation of embryos was carried out in hybridization buffer for 1 hr at 60°C before adding Digoxigenin-labelled RNA probes overnight at 60°C. The next day, embryos were washed in decreasing concentrations of hybridization buffer diluted with PBT 0.3% (with 3:1, 1:1, 1:3) and then rinsed three times 5 min each in PBT 0.3% and then once for 20 min in blocking solution (1X PBS; 1% Triton X100; 1% BSA) at room temperature before adding alkaline phosphatase conjugated anti-DIG antibody (Roche). Embryos were incubated with primary antibody for 2 hr at room temperature. Following primary antibody, embryos were washed for 5 min in PBT 0.3% and then 5 min in PTW 0.05%. Color enzymatic reaction was carried out using NBT/BCIP substrate (Roche) in alkaline phosphatase buffer (0.1M Tris/HCl pH 9.5; 0.05M MgCl2; 0.1M NaCl; 0.1% Tween-20), according to manufacturer’s instructions. Upon completion, the reaction was stopped with several washes of PBT 0.3% and PTW 0.1% (1xPBS; 0.1% Tween-20). Stained embryos were stored in 50% Glycerol/1x PBS at 4°C or −20°C until mounting on slides in 80% glycerol for imaging.

For immunostaining, embryos were cleaned with four times diluted bleach solution and washed in PTW 0.05%. After dissection, embryos were fixed for 20 min in 4% Formaldehyde/1X PTW 0.05%. Embryos were then permeabilized with PBT 0.3% for 30 min and incubated in antibody blocking solution (1X PBS; 0.1% Triton X100; 0.1% BSA; 10% NGS) at room temperature for 1 hr. Embryos were transferred to blocking solution containing primary antibody: mouse anti-Ubx-AbdA, Hybridoma Bank (1:5); rabbit anti-Dll (1:200) and incubated overnight at 4°C. The next day embryos were washed in PTW 0.05% (two quick rinses, then two washes of 10 min each) and incubated for 30 min in blocking solution at room temperature with shaking, before adding the secondary antibody (Rabbit anti-mouse-HRP [1:1000] from Promega or donkey anti-Rabbit-HRP [1:500] from Jackson Immuno research) diluted in PTW. All secondary antibodies were incubated with embryos for 2 hr at room temperature with shaking. Following antibody incubation, embryos were rinsed in PBT 0.3% and PTW 0.05% three times each for 10 min at room temperature. Before enzymatic developing with DAB with color enhancer (DiAminoBenzidine tetrahydro-chloride from Sigma), embryos were briefly incubated with DAB solution for 5 min at room temperature. Upon completion, staining was stopped by washing the embryos briefly in PBT 0.3%, followed by 5 times, five minute washes in PBT 0.3%. Five more washes of 5 min in PTW 0.1% followed. Embryos were transferred to 30% glycerol/1X PBS for 5 min, and then 50% Glycerol/1X PBS for 5 min, before sinking in 80% glycerol/1X PBS at 4°C until mounting in 80% glycerol under coverslips for imaging.

dsRNA template preparation and injections were carried out as described in Refki et al. (2014) and Santos et al. (2015). Briefly target gene fragments were first cloned into pGEM-T vector then amplified using forward and reverse primers tagged with T7 promoter. The resulting PCR product was used for dsRNA transcription using Megascript RNAi (Ambion) according to manufacturer’s instructions. dsRNA was injected into adult females at a concentration of 1–3 µg/µl. After injection, females were kept in water containers to lay eggs. Embryos were collected for phenotypic evaluation and imaged for phenotypes.

### Nasonia vitripennis

Wild type Nasonia embryos were collected from virgin AsymCx (Werren et al., 2010) females host fed on Sarcophaga bullata pupae (Carolina Biological), aged as needed at 25°C, and fixed for 28 min in 4% heptane-saturated formaldehyde/1X Phosphate Buffered Saline (PBS), with vigorous shaking. Embryos were hand-peeled under 1X PBT using 1 ml insulin needles (Becton-Dickinson), and were transferred to 100% methanol for storage, or further processed. For staining, embryos were then rehydrated to 1X PBS with 0.1% Tween (PBT) through a methanol/PBT series.

In situ hybridizations were carried out as described previously (Pultz et al., 2005; Rosenberg et al., 2014). Briefly, fixed embryos that had been stored under methanol were gradually brought up to 1X PBT in a PBT/MeOH series, and washed three times in 1x PBS + 0.1% tween-20 (PBT) before a 30 min post-fixation in 5% formaldehyde/1XPBT. The embryos were then washed three times in 1X PBT, and digested in Proteinase K (final concentration of 4 µg/ml) for five minutes, before three PBT washes. Embryos were blocked for 1 hr in hybridization buffer before probe preparation (85°C, 5 min; ice 1 min) and addition for overnight incubation at 65°C. The next day, embryos were washed in formamide wash buffer three times, and then 1X MABT buffer three times, before blocking in 2% Blocking Reagent (BBR; Roche) in 1X MABT for 1 hr, then in 10% horse serum/2% BBR/1XMABT for 2 hr. Embryos were incubated overnight at 4°C with primary antibody (anti-DIG-AP Fab fragments; Roche, 1:2000). The third day, embryos were washed in 1X MABT for ten x 20 min washes before equilibrating the embryos in AP staining buffer and developing in AP buffer with NBT/BCIP solution (Roche). After staining, embryos were washed in 1x PBT three times for five minutes each before a 25 min post-fix step in 5% formaldehyde/1XPBT. Embryos were then washed several times with 1X PBT, and allowed to sink in 50% glycerol/1XPBS and then 70% glycerol/1XPBS, which was subsequently used for mounting.

dsRNA template was amplified from target gene fragments that had been previously cloned into pCR-Topo (Qiagen) or directly from embryo cDNA, using standard T7 promoter-containing oligos, as described previously (Lynch and Desplan, 2006). Purified PCR product was used for dsRNA transcription using Megascript RNAi (Ambion) according to manufacturer’s instructions, and purified product diluted to 1–3 µg/µl for injection. pRNAi for Nv-mlpt and Nv-svb resulted in sterility. Therefore, embryos laid by unmated host-fed virgin Nasonia females were microinjected with dsRNA using a Femto-Jet micro-injector (Eppendorf), and transferred to a slide to develop in a humid chamber at 28°C for 36 hr. Unhatched larvae were dissected from extraembryonic membranes and cleared in freshly prepared Lacto:Hoyer’s medium overnight at 65°C, and imaged for cuticle organization the following day.

### Drosophila melanogaster

The following Drosophila lines were used in this study: w, pri1/TM6B-Ubi-GFP (Kondo et al., 2007), svbR9/FM7-Kr::GFP (Delon et al., 2003), nullo-Gal4 (from the Gehring lab), mat-Gal4, nos-Gal (gift from N. Dostatni). talpri4, FRT82B/TM6B and talpri5, FRT82B/TM6B, bearing a deletion of the tal/pri gene, were kindly provided by Y. Kageyama (Kobe, Japan). UAS constructs used in this study are as follows: UAS-svb::GFP (Kondo et al., 2010), UAS-GFP (Bloomington stock center), UAS-pri (Kondo et al., 2007), and UAS-svb-ACT::GFP and UAS-svb3Kmut::GFP (this study).

Ubr3 mutant embryos deprived of maternal and zygotic contribution were generated using the Ubr3B allele according to (Zanet et al., 2015). Embryos lacking both maternal and zygotic contribution of pri/tal were collected from adult females of the following genotype hsFlp; talS18.1, FRT82B/OvoD1, FRT82B that received one pulse of heat shock at 37°C for 40 min, during L1-L2 larval stage, and crossed to males talpri4, FRT82B/TM6B-Twist-Gal4,UAS-GFP. Mutant embryos, identified by the lack of GFP, were sorted and further analyzed. svb mutant embryos lacking maternal contribution and/or zygotic contribution were generated by crossing svbPL107, FRT19A/ovoD1, FRT19A, hsFlp adult females that were heat-shocked one hour at 37°C at L1-L2 larval stage to wild type adult males.

To test the effect of svb ectopic expression in early embryos lacking mlpt/pri/tal function (talpri5/talS18 trans-heterozygote condition), we generated the following recombinants lines: talpri5, nullo-Gal4/TM3, Twist-Gal4, UAS-GFP; talS18, nullo-Gal4/TM3, Twist-Gal4, UAS-GFP; talpri5, UAS-svb/TM3, Twist-Gal4, UAS-GFP; talS18, UAS svb/TM3, Twist-Gal4, UAS-GFP. Homozygous pri/tal mutant embryos were identified by the lack of balancer chromosome (marked with GFP). Sibling controls and mutant embryos were in all cases processed in the same batch; a typical collection includes >400 embryos in total. Expression of UAS-svb constructs using Gal4 drivers were conducted at 29°C.

### DNA constructs and transgenics

To generate the transformation vector pUASp-SvbAct::GFP, a fragment without the exon1S and the 5' of the exon2A to the proteolytic cleavage site was amplified by PCR from pUASp-Svb::GFP (Kondo et al., 2010) and cloned into the pUASp-Svb::GFP, linearized with SpeI and EcoRI, using the In-Fusion HD Cloning kit (Clontech). To obtain the pUASp-Svb-3Kmut-GFP, the EcoRI fragment with the 3 K mutated from pAc-SvbK7 (Zanet et al., 2015) was cloned into the pUASp-Svb::GFP, linearized with EcoRI. All constructs have been verified by sequencing. Transformation vectors have been used to establish PhiC31-mediated transgenic lines, using standard procedures (Bischof et al., 2007).

For embryo staining, staging of mutant embryos, subjected to in situ hybridization or immunohistochemistry, was determined according to the age of embryo collections. Staining was performed as previously described (Chanut-Delalande et al., 2014) using: anti-Wg (1/100 mouse monoclonal antiserum, 4D4 Developmental Studies Hybridoma Bank, Iowa City, IA), biotinylated goat anti-mouse (1/500, Vector Laboratories). DIG-labeled RNA antisense probes were synthesized in vitro from cDNA clones and processed for in situ hybridization.

### Data and materials availability

Sequences presented in this paper can be found in Genbank, with accession numbers as follows: Tc-svb MG913606, Nv-mlpt MH181829, Nv-Svb MH181831, Nv-Ubr3 MH181828, Of-mlpt MH181830, Of-svb MH181832, Of-Ubr3 MH181827, Gb-svb MH011417, Gb-mlpt MH699965, Gb-Ubr3 MH011418.
