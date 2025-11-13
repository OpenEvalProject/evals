# Hsp70-associated chaperones have a critical role in buffering protein production costs

## Authors

- Zoltán Farkas<sup>1</sup> ([ORCID: 0000-0002-5085-3306](https://orcid.org/0000-0002-5085-3306)) †
- Dorottya Kalapis<sup>1</sup>
- Zoltán Bódi<sup>1</sup>
- Béla Szamecz<sup>1</sup>
- Andreea Daraba<sup>1</sup>
- Karola Almási<sup>1</sup>
- Károly Kovács<sup>1</sup>
- Gábor Boross<sup>1</sup>
- Ferenc Pál<sup>1</sup>
- Péter Horváth<sup>1</sup>
- Tamás Balassa<sup>1</sup>
- Csaba Molnár<sup>1</sup>
- Aladár Pettkó-Szandtner<sup>2</sup>
- Éva Klement<sup>3</sup>
- Edit Rutkai<sup>4</sup>
- Attila Szvetnik<sup>4</sup>
- Balázs Papp<sup>1</sup>
- Csaba Pál<sup>1</sup> ([ORCID: 0000-0002-5187-9903](https://orcid.org/0000-0002-5187-9903)) †

### Affiliations

1. Synthetic and Systems Biology Unit, Institute of Biochemistry Biological Research Centre of the Hungarian Academy of Sciences Szeged Hungary
2. Institute of Plant Biology Biological Research Centre of the Hungarian Academy of Sciences Szeged Hungary
3. Laboratory of Proteomic Research Biological Research Centre of the Hungarian Academy of Sciences Szeged Hungary
4. Division for Biotechnology Bay Zoltán Nonprofit Ltd Budapest Hungary

† Corresponding author

## Abstract

Proteins are necessary for cellular growth. Concurrently, however, protein production has high energetic demands associated with transcription and translation. Here, we propose that activity of molecular chaperones shape protein burden, that is the fitness costs associated with expression of unneeded proteins. To test this hypothesis, we performed a genome-wide genetic interaction screen in baker's yeast. Impairment of transcription, translation, and protein folding rendered cells hypersensitive to protein burden. Specifically, deletion of specific regulators of the Hsp70-associated chaperone network increased protein burden. In agreement with expectation, temperature stress, increased mistranslation and a chemical misfolding agent all substantially enhanced protein burden. Finally, unneeded protein perturbed interactions between key components of the Hsp70-Hsp90 network involved in folding of native proteins. We conclude that specific chaperones contribute to protein burden. Our work indicates that by minimizing the damaging impact of gratuitous protein overproduction, chaperones enable tolerance to massive changes in genomic expression.

## Introduction

Optimal allocation of cellular resources is a central concept in cell biology (Basan et al., 2015; Hui et al., 2015). Protein biosynthesis consumes a huge amount of energy: an estimated 30–50% of the energy consumption of dividing cells is dedicated to translation of the proteome (Buttgereit and Brand, 1995; Russell and Cook, 1995). Therefore, surplus protein production incurs a substantial fitness cost. As the ratio of unneeded protein reaches 30% of total protein in bacteria, ribosomes are destructed and growth is completely inhibited (Dong et al., 1995). Protein burdens (i.e. protein overexpression costs) are most relevant shortly after an environmental change, and are subsequently reduced once the translation has adjusted to their novel steady-state level (Shachrai et al., 2010). Deciphering the key molecular mechanisms that shape protein burden is an important challenge for systems biology. Moreover, this problem has biotechnological relevance as well. Protein engineering efforts towards microbial production of a single heterologous protein are often problematic, as full induction of the engineered constructs frequently yields bacteria with limited or no growth (Kurland and Dong, 1996).

Gene expression costs are frequently not due to the detrimental activity of unnecessary proteins, as reduced viability was observed with the overexpression of proteins with no apparent cellular activities (Andrews and Hegeman, 1976; Dong et al., 1995; Kurland and Dong, 1996; Stoebel et al., 2008; Scott et al., 2010). Most notably, a recent systematic study in baker’s yeast (Saccharomyces cerevisiae) measured the copy number limit of gene overexpression across all protein coding genes (Makanae et al., 2013). Dosage sensitive genes were generally highly expressed, and replacement of the open reading frame of these genes with a green fluorescent protein (GFP) left the fitness cost largely unaltered. Studies in bacteria (Stoebel et al., 2008) and yeast (Kafri et al., 2016) demonstrated that growth impairment results from the process of protein production and not due to accumulating the unneeded protein product per se.

Protein production of an unneeded protein consumes nutrients and has a high energetic demand. Associated costs may arise at the level of transcription due to waste of nucleotides incorporate into RNA or occupation of RNA polymerases. Translation of the unneeded proteins may be especially costly, as it wastes amino acids, charged tRNAs and occupies ribosomes. It has been shown that these two major limiting factors of protein production vary across environments, depending on the availability of nutrients (Kafri et al., 2016). Transcription dominates protein burden in low phosphate, while translation dominates costs in low nitrogen conditions. Hypothetically, unneeded proteins may also overload the cellular systems involved in protein folding and degradation. Yet, the role of chaperone networks in contributing to protein burden has remained unexplored.

In this work, we show that accumulation of an unneeded protein in yeast (S. cerevisiae) has a relatively mild impact on fitness when nutrients are in excess and no internal or external stresses are present. However, impairment of specific molecular chaperones rendered yeast cells sensitive to gratuitous protein overproduction.

## Results

### Impact of protein burden on fitness

Recent works showed that the fitness costs associated with expressing unneeded fluorescent proteins do not result from protein toxicity or impaired metabolic processes, indicating that it is the outcome of a limitation in the protein production process itself (Makanae et al., 2013; Kafri et al., 2016). In this paper, we employ yEVenus, a rapidly folding and non-toxic YFP (yellow fluorescent protein) variant (Sheff and Thorn, 2004) to study protein burden. Using this protein has several advantages for our study: the amino acid composition of yEVenus and the yeast proteome are highly similar to each other (Pearson’s correlation, r = 0.6477, p<0.01) and it is codon optimized specifically for yeast studies. Accordingly, toxicity of yEVenus due to misfolding is negligible. We expressed yEVenus in S. cerevisiae from single, low and high-copy-number plasmids, respectively, (Gietz et al., 1988) all of which are under the control of a strong constitutive promoter (pHSC82, see Materials and methods). The control strain carried the same vector backbone without the yEVenus open reading frame. Fitness of each genotype was determined by measuring colony size on synthetic selection medium agar plates (for further details, see Materials and methods). Cost is defined as the reduction in fitness of yEVenus overexpressing genotype relative to fitness of control cells in the same synthetic drop-out medium. When expressed from a single copy plasmid, yEVenus had no detectable fitness cost, while it caused a small, but significant 2.5% fitness decline expressed from a high-copy (2 µ) plasmid (Figure 1A). A denaturing polyacrylamide gel electrophoresis analysis (PAGE) indicated that when expressed from the high-copy plasmid, yEVenus constitutes ~3.7% of the total cellular proteome (Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/29845/elife-29845-fig1-v1.jpg)

**Figure 1.:** (A) Protein burden changes with copy number. The bar plot shows the relative fitness of yEVenus overexpressing and control genotypes as a function of plasmid copy number, a proxy of gene expression level. From a single copy plasmid, yEVenus has no detectable fitness cost (t-test, p=not significant), while it confers around 2.5% fitness disadvantage from a high-copy plasmid (t-test, p<0.001). Absolute fitness was estimated by measuring colony size after 48 hr of growth on solid medium. Relative fitness was calculated by normalizing to the absolute fitness of the genotypes with the corresponding empty vectors, respectively. The bars indicate mean ±95% confidence interval, based on at least 12 technical and 10 biological replicates each. Source file is available as Supplementary file 5. (B) PAGE analysis of whole cell protein extracts. The figure shows the PAGE (polyacrylamide gel electrophoresis) separation of whole cell protein extracts (10 µg, 20 µg, and 30 µg) from both the control and the yEVenus overexpressing strains in denaturing conditions (4–20% gradient Tris-Glycine SDS-PAGE). To create a standard curve, a bovine serum albumin (BSA) dilution series (100–800 ng) was loaded onto the same gel. On the basis of a densitometry analysis using the standard curve, the yEVenus (band at 27 kDa) constitutes 3.7% of the total cellular proteome when expressed from a high-copy plasmid (for further details, see Materials and methods). (C) Distribution of genetic interaction scores (ε) across the haploid yeast knock-out collection. The ε value for the vast majority of the knock-out strains is approximately zero, indicating no specific genetic interaction of the corresponding gene with yEVenus overexpression. The dashed lines on the y axis represent cutoff values for ε (0.05 and −0.05, respectively). Negative/positive interactions are color-coded as magenta/green. For the calculation of genetic interaction score, see Materials and methods. Source file is available as Supplementary file 1. (D) Scatterplot of the genetic interaction scores and biomass-normalized fluorescence levels of the deletion strains from the haploid yeast knock-out collection. On the x axis, one represents the wild type fluorescence level (dashed line). The dashed lines on the y axis represent the previously defined interaction value cutoffs (0.05 and −0.05, respectively). The fluorescence level of the genotypes shows only very weak correlation with the strength of the interaction (Pearson’s correlation test, r = 0.05, p<0.001). Negative/positive interactions are color-coded as magenta/green. For the calculation of genetic interaction score and for the evaluation of fluorescence level, see Materials and methods. Source file is available as Supplementary file 1. Additional analysis of genetic interaction scores and fluorescence levels are shown in Figure 1—figure supplement 1A and B. (E) Examples on negative genetic interactions between single gene deletions and yEVenus overexpression. The bar plots show the relative fitness values (normalized to wild type) of single mutants (yEVenus overexpression or single gene deletions), and double mutants (deletion +yEVenus overexpression), based on six replicates. Negative deviation of the observed double mutant fitness from the expected value (designated as dashed line, calculated by the multiplicative model using the two single mutant fitness values) is referred to as negative interaction. Absolute fitness was estimated by measuring colony size after 48 hr of growth on solid medium. The deleted genes (Δcrp7, Δfes1, Δgim5, Δpfd1) are selected members of the chaperone system. Source file is available as Supplementary file 1. An example of positive genetic interaction is shown in Figure 1—figure supplement 1C. (F) Scatterplot of the genetic interaction scores and the fitness of the deletion strains from the haploid yeast knock-out collection. On the x axis, one represents the wild type fitness (dashed line). The dashed lines on the y axis represent the previously defined interaction value cutoffs (0.05 and −0.05, respectively). Negative/positive interactions are color-coded as magenta/green. The fitness of the deletion strains shows only a weak positive correlation with the strength of interaction (Pearson’s correlation test, r = 0.12, p<0.001). For the calculation of fitness and genetic interaction score, see Materials and methods. Source file is available as Supplementary file 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/29845/elife-29845-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Scatterplot of the genetic interaction scores and biomass-normalized fluorescence levels using knock-out strains with wild type cell size only. A prior systematic study (Jorgensen et al., 2002) classified the yeast knock-out collection into three mains classes: genotypes with large, small and normal (i.e. wild type) cell sizes, respectively. Using data from Figure 1D, we focused on genotypes with normal cell size only. Reassuringly, the correlation between genetic interaction score and biomass normalized fluorescence remains very weak and non-significant (Pearson’s correlation test: r = 0.035, p=0.02, blue line represents linear regression line). As a final test, we used another systematic data set that treats knock-out cell size as a continuous variable (Ohya et al., 2005). Partial correlation analysis revealed no significant correlation between genetic interaction score and biomass normalized fluorescence (adjusted R2 = 0.0031) after control for cell size. Negative/positive interactions are color-coded as magenta/green. For the calculation of genetic interaction score and for the evaluation of fluorescence level, see Materials and methods. Source file is available as Supplementary file 1. (B) Scatterplot of the genetic interaction scores and biomass-normalized fluorescence levels of the deletion strains from the haploid yeast knock-out collection. Genotypes with impairment in protein folding (FES1, SSE1, STI1, YDJ1, PFD1, GIM5), transcriptional processes (HPR1, DST1, CDC73, ELP3), translational fidelity (CTK2, CTK3), and mitochondrial processes (MMM1, MDM38) are marked. On the x axis, 1 represents the wild type fluorescence level (dashed line). The dashed lines on the y axis represent the previously defined interaction value cutoffs (0.05 and −0.05, respectively). Negative/positive interactions are color-coded as magenta/green. For the calculation of genetic interaction score and for the evaluation of fluorescence level, see Materials and methods. Source file is available as Supplementary file 1. (C) An example on positive genetic interaction between single gene deletion and yEVenus overexpression. The bar plots show the relative fitness values (normalized to wild type) of single mutants (yEVenus overexpression or Δrpi1), and double mutants (Δrpi1 + yEVenus overexpression), based on 6 replicates. The deleted gene (RPI1) is Ras-cAMP pathway inhibitor. Positive deviation of the observed double mutant fitness from the expected value (designated as dashed line, calculated by the multiplicative model using the two single mutant fitness values) is referred to as positive interaction. The bottom panel shows the same data after zooming into the 0.9–1.1 relative fitness range. Absolute fitness was estimated by measuring colony size after 48 hr of growth on solid medium. Source file is available as Supplementary file 1.

### Genome-wide mapping of genes that mitigate protein burden

The above results indicate that accumulation of an unneeded protein in the cell has a relatively mild impact on fitness when nutrients are in excess and no internal or external stresses are present. However, such robustness to protein burden may be restricted to certain conditions: many genetic and environmental factors could potentially shape the associated fitness costs. To identify genes modulating protein burden, we performed a genetic interaction screen using the synthetic genetic array (SGA) approach (Tong and Boone, 2006) with the query strain carrying the yEVenus multi-copy plasmid. The screen involved construction of high-density arrays of double mutants by crossing the query mutation (yEVenus overexpression plasmid) against an array of ~5000 viable null mutants. We simultaneously measured yEVenus fluorescence intensity and fitness in all genotypes studied. Using a robotized replicating system, fitness was estimated by measuring colony size on solid agar media. Digital images were processed to calculate colony sizes, and potential systematic biases in colony growth were eliminated (see Materials and methods). Deviation of the double-mutant fitness from the product of the corresponding single-mutant fitness values was used to assess genetic interaction scores (ε, Figure 1C, Supplementary file 1). Biomass-normalized fluorescence level had no major impact on the distribution of genetic interaction scores (Figure 1D). This pattern was not due to any major deviation from wild type cell size (Figure 1—figure supplement 1A). This indicates that genetic interactions reflect a change in the fitness cost, but not in the extent of protein overexpression.

As the aim of this study was the identification of genes that mitigate the fitness costs of yEVenus overexpression, we focused on negative genetic interactions (ε < 0), i.e. when the double mutant has a lower fitness than would be expected from the product of the single-mutant fitness values. At an ε = - 0.05 cutoff value (and using a p<0.05 cutoff based on bootstrap analysis), 184 genes showed such interactions with yEVenus. By definition, lack of these genes substantially increased the fitness cost of yEVenus overexpression (Figure 1E). A functional enrichment analysis revealed that these genes are preferentially involved in translation, transcriptional control (e.g. transcription termination and elongation), mitochondria-related processes, and protein folding (Table 1, Figure 1—figure supplement 1B). Remarkably, deletion of genes encoding specific chaperones caused a 2–4 fold increment in the fitness costs of yEVenus overexpression (Figure 1E).

**Table 1.**
 Functional enrichment analysis of genes showing synergistic interactions with yEVenus overexpression.At an ε = - 0.05 cutoff value (and using a p<0.05 cutoff based on bootstrapping), 184 genes showed negative interactions with yEVenus. This gene set was tested for GO Slim category enrichment. A GO category was termed as enriched significantly, if the genes annotated to a particular GO term were significantly overrepresented (Fisher's exact test, odds ratio >1, p<0.05, FDR-corrected p<0.1) in the given gene set using the complete list of screened genes as background. N indicates the number of negative interacting genes belonging to the corresponding GO Slim category. Source file is available as Supplementary file 1.


<table>
  <thead>
    <tr>
      <th>Go.id</th>
      <th>Term</th>
      <th>N</th>
      <th>Odds ratio</th>
      <th>P value</th>
      <th>FDR corrected P value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GO:0002181</td>
      <td>cytoplasmic translation</td>
      <td>11</td>
      <td>2.27</td>
      <td>1.52E-02</td>
      <td>1.69E-01</td>
    </tr>
    <tr>
      <td>GO:0006325</td>
      <td>chromatin organization</td>
      <td>15</td>
      <td>1.70</td>
      <td>4.65E-02</td>
      <td>2.93E-01</td>
    </tr>
    <tr>
      <td>GO:0006353</td>
      <td>DNA-templated transcription, termination</td>
      <td>3</td>
      <td>4.17</td>
      <td>4.60E-02</td>
      <td>2.93E-01</td>
    </tr>
    <tr>
      <td>GO:0006354</td>
      <td>DNA-templated transcription, elongation</td>
      <td>16</td>
      <td>8.43</td>
      <td>2.73E-09</td>
      <td>2.73E-07</td>
    </tr>
    <tr>
      <td>GO:0006360</td>
      <td>transcription from RNA polymerase I promoter</td>
      <td>6</td>
      <td>5.86</td>
      <td>1.24E-03</td>
      <td>3.10E-02</td>
    </tr>
    <tr>
      <td>GO:0006366</td>
      <td>transcription from RNA polymerase II promoter</td>
      <td>29</td>
      <td>2.29</td>
      <td>2.01E-04</td>
      <td>6.71E-03</td>
    </tr>
    <tr>
      <td>GO:0006397</td>
      <td>mRNA processing</td>
      <td>9</td>
      <td>2.84</td>
      <td>7.77E-03</td>
      <td>1.11E-01</td>
    </tr>
    <tr>
      <td>GO:0006414</td>
      <td>translational elongation</td>
      <td>5</td>
      <td>3.31</td>
      <td>2.45E-02</td>
      <td>2.34E-01</td>
    </tr>
    <tr>
      <td>GO:0006457</td>
      <td>protein folding</td>
      <td>10</td>
      <td>3.06</td>
      <td>3.26E-03</td>
      <td>5.43E-02</td>
    </tr>
    <tr>
      <td>GO:0007005</td>
      <td>mitochondrion organization</td>
      <td>28</td>
      <td>2.59</td>
      <td>4.13E-05</td>
      <td>2.07E-03</td>
    </tr>
    <tr>
      <td>GO:0009408</td>
      <td>response to heat</td>
      <td>7</td>
      <td>3.17</td>
      <td>1.05E-02</td>
      <td>1.31E-01</td>
    </tr>
    <tr>
      <td>GO:0009451</td>
      <td>RNA modification</td>
      <td>7</td>
      <td>2.53</td>
      <td>2.91E-02</td>
      <td>2.34E-01</td>
    </tr>
    <tr>
      <td>GO:0016570</td>
      <td>histone modification</td>
      <td>8</td>
      <td>2.33</td>
      <td>3.05E-02</td>
      <td>2.34E-01</td>
    </tr>
    <tr>
      <td>GO:0032543</td>
      <td>mitochondrial translation</td>
      <td>12</td>
      <td>2.96</td>
      <td>1.78E-03</td>
      <td>3.55E-02</td>
    </tr>
    <tr>
      <td>GO:0048308</td>
      <td>organelle inheritance</td>
      <td>5</td>
      <td>3.23</td>
      <td>2.68E-02</td>
      <td>2.34E-01</td>
    </tr>
  </tbody>
</table>

Enrichment of the above functional categories was not found in the set of genes showing positive genetic interactions with yEVenus overexpression. It is worth noting however a specific case, where positive genetic interaction was especially strong. Deletion of RPI1, a specific repressor of the Ras-cAMP pathway removed protein burden (Supplementary file 1, Figure 1—figure supplement 1C). The underlying molecular mechanisms need further investigation.

Protein synthesis is frequently limited by the availability of free ribosomes (Vind et al., 1993). Therefore, excess proteins occupy free ribosomes, which could be better used for the translation of native proteins. Therefore, impairment of genes involved in translation should increase protein burden. We investigated this issue further by measuring fitness in the presence of a translation inhibitor chemical agent. Cycloheximide binds the ribosome and inhibits eEF2 mediated translocation during translation (Obrig et al., 1971). In agreement with expectation, partial inhibition of translation elongation by cycloheximide treatment elevated protein burden (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/29845/elife-29845-fig2-v1.jpg)

**Figure 2.:** (A) Impact of translation inhibition on protein burden in wild type yeast. The bar plot shows the cost of yEVenus in wild type strain as a function of increasing cycloheximide concentration. Cycloheximide is a widely used chemical agent to inhibit translation. Treatment of cells with sub-inhibitory concentration (0.18 µg/ml) of this chemical agent leads to a 3.7-fold increase in protein burden (t-test, p<0.001). For the calculation of fitness cost of yEVenus, see Materials and methods. The bars indicate mean ±95% confidence interval, based on four technical measurements of 17 biological replicates for each concentration. Source file is available as Supplementary file 5. (B) Impact of transcription inhibition on protein burden in wild type yeast. The bar plot shows the cost of yEVenus in wild type strain in response to mycophenolic acid (MPA) stress. MPA is a well-known transcription elongation inhibitor. Treatment of cells with sub-inhibitory concentration (30 µg/ml) of this chemical agent leads to a two-fold increase in protein burden (Mann Whitney U-test, p<0.001). For the calculation of fitness cost of yEVenus, see Materials and methods. The bars indicate mean ±95% confidence interval, based on at least 12 technical measurements of 15 biological replicates for each concentration. Source file is available as Supplementary file 5. (C) Impact of amino acid availability on protein burden. The bar plot shows the cost of yEVenus in wild type strain as a function of amino acid concentration. Auxotrophic amino acids were supplied at normal concentration to the medium, while non-auxotrophic amino acids were serially diluted from the regular one. Arbitrary units are relative concentrations normalized to the regular amino acid level. Total depletion of non-essential amino acids (0 arbitrary unit) from the growth medium resulted in a 2.5-fold increase in protein burden, compared to the regular one (t-test, p<0.001). For the calculation of fitness cost of yEVenus, see Materials and methods. The bars indicate mean ±95% confidence interval, based on at least five technical measurements of 12 biological replicates for each condition. Source file is available as Supplementary file 5. (D) The impact of protein burden across different carbon sources. The left panel shows the cost of yEVenus in wild type strain on different carbon sources. The right panel shows the absolute fitness (arbitrary units estimated by measuring colony size on solid agar media) of the yEVenus overexpressing wild type strain on different carbon sources. Growth media with alternative carbon sources (respirato-fermentative galactose, respirative raffinose) led to a reduction of absolute fitness by 27–32% (right panel, t-test, p<0.001), compared to that on the standard carbon source (fermentative glucose). However, the relative fitness cost of yEVenus overexpression (left panel) was not affected by the change of carbon source. Specifically, the cost of yEVenus on glucose is comparable to that on galactose (t-test, p=0.14) or raffinose (t-test, p=0.07). For the calculation of absolute fitness and fitness cost of yEVenus, see Materials and methods. The bars indicate mean ±95% confidence interval, based on at least 12 technical measurements of 15 biological replicates for each of the genotype. Source file is available as Supplementary file 5.

Similarly, inactivation of genes involved in transcriptional elongation (HPR1, DST1, CDC73, ELP3) significantly increased protein burden. To validate this result, we tested the effect of a transcriptional elongation inhibitor on protein burden. Mycophenolic acid interferes with nucleotide biosynthesis (Costa and Arndt, 2000), through inhibiting IMP dehydrogenase (IMPDH). It thereby reduces the endogenous GTP/UTP and stalls RNA polymerases. Treatment of cells with sub-inhibitory concentration of this chemical agent significantly enlarged protein burden (Figure 2B).

Another source of protein burden may arise due to wastes of cellular resources, including ATP and amino acids needed for protein synthesis. Indeed, inactivation of amino acid metabolism genes (AAT2, BAT2, CYS3, PRS3, LEU3) influenced protein burden (Supplementary file 1), suggesting that protein burden depends on the availability of amino acids in the environment. It was indeed so: depletion of amino acids in the growth medium increased the fitness cost (Figure 2C). Moreover, genes with mitochondria-related functions, including mitochondrial translation (e.g. MRPS9, MRPL22), mitochondrial DNA replication and growth (e.g. MMM1), mitochondrial distribution and morphology (e.g. MDM38) are on the gene list identified by the SGA analysis (Supplementary file 1).

Taken together, results of genetic and chemical perturbations of specific cellular subsystems demonstrate that impairment of transcription, translation and amino acid availability increase protein burden.

Finally, one may argue that growth rate reduction per se - irrespective of the exact nature of the environmental or genetic perturbation - may imply elevated protein burden upon overexpression. However, this is unlikely to be so, for three reasons. First, the functional roles of genes that showed genetic interactions were far from being random (Table 1). Second, and more generally, the correlation between the fitness of the deletion strains and the strength of the genetic interaction was very weak (Figure 1F). Finally, despite major differences in growth rates of yeast grown on glucose, galactose or raffinose as sole carbon sources, the relative fitness costs of protein burden remained unchanged (Figure 2D).

### Molecular chaperones shape protein burden

The genetic interaction screen revealed that molecular chaperones are overrepresented in the list of genes that influence protein burden. Most notably, the list includes several members of the Hsp40-70-110 complex (FES1, SSE1 and YDJ1), and an Hsp70-90 scaffold protein (STI1). These Hsp70-associated proteins are functionally highly related (Rizzolo et al., 2017), and all play critical roles in the ATPase activation and the nucleotide exchange regulation of the Hsp70 class Ssa chaperones. Accordingly, impairment of these proteins decreases the activity of Ssa chaperones and thereby perturbs the recognition and clearance of misfolded proteins. As a consequence, aggregated proteins accumulate in the cell (Mayer, 2013; Clerico et al., 2015).

Based on these findings we hypothesized that molecular chaperones have a critical role in buffering protein burden. Several further observations support the hypothesis. First, we tested the impact of temperature stress on protein burden, not least because genes (e.g. CPR7, YDJ1) involved in the GO term ‘response to heat’ were on the list of negative genetic interactions. Subjecting yeast cells to high temperature causes a severe proteotoxic stress as it induces protein misfolding of nascent proteins and perturbs proteome homeostasis (Trotter et al., 2002). As expected, protein burden significantly increased with rising temperature (Figure 3A). Reassuringly, these results are insensitive to the exact promoter employed for the expressional control of yEVenus (Figure 3—figure supplement 1A, Figure 3—figure supplement 1B, Figure 3—figure supplement 1C, Supplementary file 2).

![Figure 3.](https://cdn.elifesciences.org/articles/29845/elife-29845-fig3-v1.jpg)

**Figure 3.:** (A) Impact of heat stress on protein burden. The bar plot shows the fitness cost of yEVenus in wild type strain as a function of increasing temperature. Protein burden significantly increased with rising temperature, resulting in a 2.8-fold difference when colonies were subjected to 40°C, in comparison to the optimal incubation temperature (30°C; t-test, p<0.001) The bars indicate mean ±95% confidence interval, based on at least 12 technical measurements of 15 biological replicates for each condition. Source file is available as Supplementary file 5. Additional analysis of protein burden across five different yEVenus plasmids are shown in Figure 3—figure supplement 1A–C (B) Impact of proteotoxic stress on protein burden. The bar plot shows the fitness cost of yEVenus in wild type strain as a function of azetidine-2-carboxylic acid (AZC) concentration. AZC is a toxic analog of proline, incorporation of this compound into newly synthesized proteins leads to misfolding in consequence of reduced protein stability. Incubation with sub-lethal dosage of AZC (2.5 mM) leads to a more than 4-fold increase in protein burden (t-test, p<0.001). For the calculation of fitness cost of yEVenus, see Materials and methods. The bars indicate mean ±95% confidence interval, based on at least 12 technical measurements of 15 biological replicates for each concentration. Source file is available as Supplementary file 5. (C) Protein aggregation propensity in yEVenus overexpressing genotypes. The bar plot shows the aggregation frequency in the wild type and in four deletion mutant strains, with (yEVenus) or without (control) protein burden. The deleted genes are selected members of the chaperone system. Protein burden by yEVenus promotes protein aggregation further in the chaperone deficient backgrounds. Aggregation frequency is 5–670% larger in the chaperone deletion mutants under protein burden, in comparison with the corresponding isogenic control strain with empty vector, respectively. The aggregation propensity in the wild type is at the same level either with or without protein burden. The frequency of cells with aggregated foci corresponds to the level of protein aggregation. Aggregation frequency was calculated as follows: the number of cells containing fluorescent foci was divided by the number of fluorescent cells in total, monitoring at least 2000 cells. For further details, see Materials and methods. The bars indicate mean ±95% confidence interval, based on at least five technical measurements for each of the genotype. Student t-test was used to assess difference in aggregation frequency between control and yEVenus overexpressing genotypes. */**/*** indicates p<0.05/0.01/0.001; n.s indicates p=not significant. Source file is available as Supplementary file 5. Representative images of VHL-mCherry localization in yeast cells are shown in Figure 3—figure supplement 1D. (D) Changes of Sti1p interaction partners in response to protein burden. The figure shows the scatterplot of the log(2) protein-binding affinity of 18 putative interaction partners (Cherry et al., 2012) of Sti1p under low- and high protein burden, respectively. Protein-binding affinity to Sti1p was estimated by calculating the peptide count fold change of Sti1p IP samples relative to the negative control IP samples both under low and high protein burden (see Materials and methods). The red points mark proteins that specifically associate with Sti1p under low protein burden. The continuous line represent x = y. Source file is available as Supplementary file 4.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/29845/elife-29845-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) Monitoring yEVenus fluorescence intensity in wild type cells across five different yEVenus plasmids. The figure shows fluorescence histograms of wild type cells with different plasmids. The plasmids differ only in the exact promoter used for the control of yEVenus expression The control plasmid did not contain the yEVenus coding sequence. Flow cytometry was used to establish the fluorescence level of wild type yeast overexpressing yEVenus under the control of different promoters. Single yeast colonies were picked from agar plates and incubated in liquid leucine-dropout SC-MSG medium. After reaching stationary phase, 1% of the population was serially transferred into fresh synthetic drop-out medium. Cell cultures from the exponential phase were diluted to approximately 5 × 102 cells/ml, and fluorescence intensity values (logarithmic scale) were estimated by a Guava flow cytometer. Gating was applied based on forward scatter data (logarithmic scale), to exclude extrinsic noise. During each run, a minimum of 5000 events were recorded. Fluorescence was calculated by normalizing the measured fluorescent intensity to the forward scatter values (both log10-scaled). The fluorescence histograms are based on eight biological replicates for each plasmid. Source file is available as Supplementary file 5. (B) Protein burden as a function of temperature across five different yEVenus plasmids. The plasmids differ only in the exact promoter used for the control of yEVenus expression. Regardless of the plasmids employed, protein burden increased significantly with rising temperature. Center lines indicate the median of yEVenus cost based on four technical measurements of 10 biological replicates for each plasmid. Student’s t-test was used to assess cost difference between 30°C and 40°C. **** indicate p<0.0001. Source file is available as Supplementary file 5. (C) Genetic interactions between single gene deletions and yEVenus overexpression. The bar plot shows the interaction score of central regulators (STI1 and YDJ1) of the Hsp70 complex across five different yEVenus plasmids. The plasmids differ only in the exact promoter (pTDH3, pPDC1, pHSC82, pGPP1, pTAL1) used for the control of yEVenus expression. The dashed lines on the x axis represent the previously defined interaction value cutoffs (0.05 and −0.05, respectively). Although there are some variations in the quantitative values of the interaction score, the overall negative sign remains. Source file is available as Supplementary file 2. (D) Representative images of VHL-mCherry localization in yeast cells (wild type and Δsse1) with (yEVenus plasmid) and without (control plasmid) protein burden. Cell fluorescence was detected by high content microscopy (Operetta, Perkin Elmer), using 60x high numerical aperture objective and the following filter sets: mCherry channel (excitation: 560–580 nm, emission: 590–640 nm) and yEVenus channel (excitation: 490–510 nm, emission: 520–560 nm). N/A indicates not available microscopic image from the given channel.

Second, as mistranslation during protein synthesis promotes misfolding and protein aggregation (Lee et al., 2006; Yang et al., 2010; Paredes et al., 2012), reduction of translation fidelity should also exacerbate the fitness deficit caused by protein overproduction. Reassuringly, CTK2 and CTK3, two genes involved in controlling the fidelity of translation elongation (Röther and Strässer, 2007) were on the list of genes showing negative genetic interaction with yEVenus overexpression (Supplementary file 1).

Third, induction of protein misfolding by a chemical agent enhanced protein burden. We studied the cellular response to misfolded proteins generated by azetidine-2-carboxylic acid (AZC) stress (Shichiri et al., 2001). AZC is a toxic analog of proline, and incorporation of this chemical agent into proteins causes misfolding (Trotter et al., 2002; Albanèse et al., 2006). Application of sub-lethal dosages of AZC elevated the fitness costs associated with yEVenus overproduction (Figure 3B).

The fourth piece of evidence comes from monitoring cellular aggregation. An established method (Kaganovich et al., 2008) was utilized to measure the misfolding propensity of a fluorescently-tagged reporter protein (VHL-mCherry). Active quality-control machinery in the wild type yeast prevents misfolding of the reporter protein, leading to its uniform distribution in the cell. However, when the protein folding machinery is impaired or becomes overloaded, the reporter protein misfolds and becomes spatially sequestered. As the fluorescent tag of the reporter protein remains fully functional, protein aggregation spots within the cell become easily visible as fluorescent foci (Kaganovich et al., 2008).

In wild type cells, protein misfolding propensity did not increase significantly upon protein burden (Figure 3C). This is in line with expectation, as the fitness cost of protein overexpression in wild type was only around 2.5% (Figure 1A). The situation was very different when genotypes impaired in protein folding (Δfes1, Δsse1, Δsti1, Δydj1, Δpfd1, Δgim5, Δcpr7) were considered, all of which showed negative genetic interactions with yEVenus overexpression. In these genotypes, protein burden elevated the propensity of protein misfolding (Figure 3C, Figure 3—figure supplement 1D).

### Protein burden perturbs the Sti1p interaction network

The above results indicate a crucial role of the Hsp70-associated molecular chaperones in mitigating protein burden. Why should this be so? One possibility is that the unneeded proteins bind to key regulators of the Hsp70-associated chaperones which otherwise would be used to navigate folding of native proteins within the cell. To investigate the feasibility of this idea, we performed a GFP co-immunoprecipitation (co-IP) assay to identify weak in vivo physical interactions between yEVenus and native cellular proteins.

In order to extract cellular proteins without disturbing physical interactions, we used an established protocol (Visweswaraiah et al., 2011) specifically designed for the identification of weak protein-protein interactions. Total protein extracts from mid-exponential growth phase were immunopurified (IP) using anti-GFP antibody coupled magnetic beads and the IP-purified proteins were then subjected to LC-MS/MS analysis (see Materials and methods). Relative abundance of individual proteins in the samples was estimated by retrieving peptide counts of the individual proteins.

After applying several filtering steps (see Materials and methods), we identified 34 proteins that bind to yEVenus (Supplementary file 3). Altogether, the list of putative interacting partners includes five proteins with chaperone-related functions (Supplementary file 3). Notably, Sti1p and Ydj1p not only binds to yEVenus, but were identified also in the genetic interaction assay. Both proteins are involved in the activation of Ssa proteins, key components of the Hsp70 complex.

The above results indicate that as a globular protein, yEVenus binds weakly, but significantly to certain molecular chaperones and to Sti1p in particular (Supplementary file 3). This raises the possibility that the protein burden is linked to perturbation of the native physical interactions of Sti1p by yEVenus. To investigate this issue, we performed a reciprocal co-IP assay with the aim to identify quantitative changes in physical interactions of Sti1p in response to protein burden. Accordingly, we used a strain that expresses a C-terminally epitope-tagged Sti1p (Sti1p-3xFLAG) and investigated it both under low and high protein burden. Total protein extracts from mid-exponential growth phase were immunopurified (IP) using anti-FLAG antibody coupled beads and the IP-purified proteins were then subjected to LC-MS/MS analysis, as previously (Materials and methods).

The analysis focused on 18 proteins, all of which have been described to physically interact with Sti1p in prior studies (Cherry et al., 2012). Our method confirmed half of these 18 protein interactions under low protein burden, that is when yEVenus was expressed from a single-copy plasmid (Figure 3D, Supplementary file 4). Remarkably, we observed a significant drop in protein-binding affinity of Sti1p with as many as 8 out of the nine detected interaction partners under high protein burden (Figure 3D, Supplementary file 4). Most notably, protein-binding affinity decreased by 70%, 75% and 55% in the cases of Ssa1, Ssa2p and Hsp90p, respectively. This is all the more significant, as these proteins are exceptionally important and well-characterized interaction partners of Sti1p (Chen and Smith, 1998; Song and Masison, 2005; Balchin et al., 2016). Finally, protein-binding between yEVenus and Sti1p was detectable under high protein burden only (Supplementary file 4). We speculate that promiscuous binding of Sti1p with certain globular proteins (such as yEVenus) has no functional consequences unless the cellular dosage of the partner protein exceeds a critical threshold. Collectively, these data suggest that protein burden promotes a partial disassociation of interaction partners from Sti1p, putatively leading to partial disassociation of the Hsp70-Hsp90 chaperone complex.

## Discussion

Our work demonstrates that even gross accumulation of an unneeded gratuitous protein in the cell has a relatively mild impact on fitness when no internal or external stresses are present (Figure 1A). However, such robustness to protein burden was restricted to specific conditions only. We explored the molecular mechanisms underlying robustness to protein overproduction. Our main findings are as follows.

First, deletion of genes involved in translation, transcriptional control, and mitochondria-related processes rendered yeast cells hypersensitive to protein overexpression. Our observation that translational and transcriptional perturbations modulate protein burden was validated further by chemical and environmental stress screens, and is also consistent with prior studies (Kafri et al., 2016). Therefore, protein burden varied substantially across genetic backgrounds and environmental stresses. We note that mutants with impaired mitochondria exhibit reduced respiratory growth, and therefore they have to rely on less efficient modes of ATP production. However, beyond ATP production, mitochondria are involved in the synthesis of certain amino acids as well (Ahn and Metallo, 2015; Zong et al., 2016). Therefore, future works should elucidate the exact molecular mechanisms underlying the elevated protein burden in cells deficient in mitochondrial functions.

Second, prior studies suggested that expression of an unneeded protein effectively decreases the fraction of proteome allocable to ribosomes and useful biosynthetic proteins, thereby causing a growth defect (Scott et al., 2010). In principle, mutations could therefore modulate protein burden by simply increasing the proteome fraction of the unneeded protein. However, the fractional contribution of yEVenus to the total proteome was not elevated in gene knock-out strains (Figure 1D, Figure 1—figure supplement 1A). This indicates that allocation models that rely on transcription and translation only cannot fully account for protein burden.

Third, and most significantly, an interacting chaperone network shapes protein burden (Figure 4). The Hsp70 complex is a key player in the maintenance of normal proteostasis. The soluble Ssa proteins (members of the Hsp70 family) recognize and associate transiently with exposed hydrophobic patches of misfolded proteins in the cytosol and prevent protein aggregation (Mayer, 2013; Clerico et al., 2015). Deletion of specific activators (YDJ1, STI1, FES1 or SSE1) of Ssa proteins substantially elevated protein burden, and resulted in protein aggregation. Indeed, Ssa protein’s capacity to bind and release client proteins heavily depends on these activators (Wegele et al., 2003). In particular, the nucleotide exchange factors (Sse1p and Fes1p) are responsible for client-release and thereby support the refolding or the proteasomal degradation of misfolded proteins (Gowda et al., 2013). It is worth noting that due to partial functional redundancy of Ssa proteins (Hasin et al., 2014), the corresponding SSA genes did not emerge in the screen. In agreement with expectation, temperature stress, elevated mistranslation rate and a chemical misfolding agent all substantially enhanced protein burden. We conclude that molecular chaperones have an important role in buffering protein burden.

![Figure 4.](https://cdn.elifesciences.org/articles/29845/elife-29845-fig4-v1.jpg)

**Figure 4.:** Malfunction of the protein quality control system impairs the proteome balance by driving cellular proteins into toxic metastable (partially folded or misfolded) conformations from their correctly folded native state (Balchin et al., 2016). Accumulation of these folding intermediates could further overload this surveillance system and could lead to the collapse of the proteostasis network. Hypothetically, overexpression of a gratuitous protein (such as the yEVenus) might not be tolerated in a misfolding sensitized background, as it could add an extra-layer of threat to the cell. Our genome-wide genetic interaction screen (SGA) revealed the importance of a central regulatory complex to buffer overexpression costs. This complex maintains the normal activity of the Ssa chaperones (members of the Hsp70 family) that act on misfolded proteins. In addition, one member of this complex also acts on the ribosome-associated complex (RAC). Inactivation of the constituent members (Hsp70-90 scaffold Sti1p, Hsp40-Ydj1p, NEF-Sse1p, and NEF-Fes1p, color-coded as red) of this complex exacerbated the cost of yEVenus overexpression. In such genetic backgrounds, the clearance of misfolded proteins by protein refolding or proteasomal degradation is affected. In agreement with the genetic perturbation screen, conditional induction of proteotoxic stress in the yEVenus overexpressing wild type strain also exaggerated the cost of the overexpression. Remarkably, based on physical interaction assays, we found evidences that protein burden perturbs the interaction network of Sti1p, putatively leading to a dysfunctional Hsp70-Hsp90 chaperone complex. As a consequence, downregulation of the proteostasis network is expected, which would have serious fitness consequences in times of proteotoxic stress.

Finally, we found evidence that yEVenus - a typical, globular fluorescent protein binds to Sti1p, one of the key regulators of the Hsp70-Hsp90 complex (Song and Masison, 2005; Wolfe et al., 2013). We hypothesize that Sti1p may be especially prone to promiscuous protein binding, as it has an over 2-fold higher fraction of unstructured residues than the proteome average (data not shown). Approximately, half of Sti1p putative physical interacting partners (Cherry et al., 2012) are involved in the maintenance of normal proteostasis. The list includes members of the Hsp70-Hsp90 complex, Hsp104 disaggregase, proteasome subunits and ubiquitin-associated proteins. Therefore, one might expect that perturbation of Sti1p interactions by a highly abundant, weakly interacting protein (Figure 3D) would have serious fitness consequences in times of proteotoxic stress. Future works should elucidate this hypothesis further and specifically the role of promiscuous peptide binding in protein burden.

Our work has important implications for future studies. The distribution of genomic expression generally follows a highly skewed power-law like distribution with a small number of exceptionally highly expressed genes (Ueda et al., 2004; Lu and King, 2009). Highly expressed genes contain various cost-minimizing gene architectures (Frumkin et al., 2017). Such genes are under especially severe selective constraints, possibly to avoid misfolding and consequent formation of protein aggregates (Geiler-Samerotte et al., 2011). Even though highly expressed proteins are not particularly prone to misfolding, they may still indirectly influence protein aggregation in the cell. Specifically, our work raises the possibility that highly expressed proteins bind to key components of the chaperone network which otherwise would be used to navigate folding of other native proteins within the cell. As a consequence, the availability of active chaperone molecules decreases, leading to increased propensity for damaging protein aggregation, especially in times of proteotoxic stress. It is important to emphasize that yEVenus is a codon optimized fluorescent protein (Sheff and Thorn, 2004), and is not particularly prone to misfolding and consequent toxicity (Kafri et al., 2016). Therefore, this hypothesis is conceptually distinct and complementary to the issue of whether aggregation-prone proteins impose a fitness cost through toxicity (Plata et al., 2010; Geiler-Samerotte et al., 2011).

More generally, several molecular chaperones can buffer the damaging effects of protein mutations (Csermely, 2001; Queitsch et al., 2002; Cowen and Lindquist, 2005; Paaby and Rockman, 2014). Chaperone overload by highly expressed proteins may influence this process. In a similar vein, it appears that protein burden depends on genetic variation and environmental conditions as well. Therefore, the cellular capacity to tolerate major fluctuations in genomic expression heavily depends on the genetic makeup: the associated fitness costs should vary extensively across microbial species occupying different environmental niches. Finally, we anticipate that our genome-wide approach uncovering the determinants of protein burden will help the design of improved host strains for the efficient overproduction of recombinant proteins.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species)or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain (Saccharomyces cerevisiae)</td>
      <td>Y7092</td>
      <td>PMID: 16118434</td>
      <td></td>
      <td>SGA query strain, mat alpha</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>non-essential gene deletion collection (BY4741, MATa)</td>
      <td>PMID:12140549</td>
      <td>YSC1053</td>
      <td>Open BioSystem (Dharmacon)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>synthetic genetic array (SGA) technique</td>
      <td>PMID: 16118434</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ software</td>
      <td>PMID: 22930834</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Gene Onthology term enrichment with topGO (version 2.28)</td>
      <td>PMID: 16606683</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>org.Sc.sgd.db (version 3.3.0) packages in R</td>
      <td>Core Team, 2017</td>
      <td></td>
      <td>http://www.R-project.org</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Machine learning-based phenotypic analysis</td>
      <td>PMID: 21807964</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Advanced Cell Classifier</td>
      <td>PMID: 28647475</td>
      <td></td>
      <td>http://www.cellclassifier.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Proteome Discoverer (v 1.4)</td>
      <td>Thermo Fisher Scientific (Germany)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNAreagent</td>
      <td>pKT0090 plasmid</td>
      <td>PMID: 15197731</td>
      <td>Addgene:Plasmid #8714</td>
      <td>contains yEVenus</td>
    </tr>
    <tr>
      <td>Recombinant DNAreagent</td>
      <td>YEplac181 plasmid</td>
      <td>PMID: 3073106</td>
      <td>Addgene:Plasmid #8628</td>
      <td>high copy plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNAreagent</td>
      <td>YCplac111 plasmid</td>
      <td>PMID: 3073106</td>
      <td>Addgene:Plasmid #53249</td>
      <td>single copy plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNAreagent</td>
      <td>pRS315 plasmid</td>
      <td>PMID: 2659436</td>
      <td>ATCC 77144</td>
      <td>low copy plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNAreagent</td>
      <td>pFA6a-TEV-6xGly-3xFlag-HphMX plasmid</td>
      <td>Tim Formosa</td>
      <td>Addgene:Plasmid #44083</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNAreagent</td>
      <td>pGAL-VHL-mCherry</td>
      <td>PMID: 18756251</td>
      <td></td>
      <td>galactose inducible VHL-mCherry</td>
    </tr>
    <tr>
      <td>Commercial assayor kit</td>
      <td>µMACS GFP Isolation Kit</td>
      <td>Miltenyi Biotec (Germany)</td>
      <td>130-091-125</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assayor kit</td>
      <td>μMACS DYKDDDDK Isolation Kit</td>
      <td>Miltenyi Biotec (Germany)</td>
      <td>130-101-591</td>
      <td>*DYKDDDDK is also known as FLAG tag</td>
    </tr>
  </tbody>
</table>

### Yeast strains and plasmids

All strains used in this study were derived from the Y7092 Saccharomyces cerevisiae parental strain (SGA query strain: MAT alpha; can1delta::STE2pr-Sp_his5, lyp1delta, his3delta1 leu2delta0, ura3delta0, met15delta0). The fluorescent yEVenus protein was transformed into the parental Y7092 strain on a high copy number plasmid (YEplac181, [Gietz et al., 1988]) by a standard protocol (Gietz and Schiestl, 2007). The transformants were selected on leucine dropout synthetic complete medium (SC-MSG, 1 g/l monosodium glutamate (Sigma-Aldrich, Germany), 1.7 g/l Yeast Nitrogen Base (BD, Germany), supplemented by amino-acid mix without leucine).

### Plasmid construction

To measure the fitness cost of protein overexpression, yEVenus, a non-toxic protein with no enzymatic activity and optimized codon usage was selected (Sheff and Thorn, 2004). The corresponding gene was integrated into a high copy expression vector. Heterologous promoters frequently perturb the transcription of other genes, by binding/titrating essential transcription factors, causing a skewed distribution of transcription factors. To minimize this problem, expression of yEVenus was driven by the native promoter of Hsc82p. Hsc82p is one of the most abundant cellular proteins in yeast (Borkovich et al., 1989; Ghaemmaghami et al., 2003). In contrast to many other chaperones (such as Hsp82p), it is expressed constitutively and shows only minor variation across stress conditions.

The high copy hc-Venus plasmid was constructed in three steps. First, the genomic HSC82 gene of the Saccharomyces cerevisiae strain BY4741 including its promoter sequence was amplified from genomic DNA using restriction site containing oligonucleotides (B_HSC_promoter, B_HSC82_terminator). The product was cut with BamHI and PstI endonucleases, and was ligated to BamHI and PstI digested YEplac181 (Gietz et al., 1988) plasmid, generating the hc HSC82 construct. The promoter region was also PCR amplified with B_HSC_promoter primer and HSC-promoter-HSP-orf-reverse primer, which product was BamHI digested and ligated into a BamHI and StuI digested hc_HSC82 plasmid. The resulting plasmid (pHSC_promoter plasmid) was designed to facilitate the insertion of virtually any ORF using its NheI and PstI restriction sites. The yEVenus ORF along with the ADH1 terminator was amplified from the pKT0090 plasmid (Sheff and Thorn, 2004) using NheI-Venus_ATG and Adh1_term_primer_pst1 oligonucleotides. The given PCR product was NheI and PstI digested and ligated to the identically digested pHSC_promoter plasmid. The generated plasmid (hc_Venus) was used to express yEVenus in S. cerevisae, under the control of the strong constitutive HSC82 promoter. For the selection of the plasmid, LEU2 marker was used in a leucine dropout synthetic medium. The control strains carry the original backbone plasmid (YEplac181) without the fluorescent protein.

To investigate the effect of plasmid copy number variation on protein burden, was inserted both into the BamHI-PstI digested single (YCplac111, [Gietz et al., 1988]) and low copy plasmid (pRS315, [Sikorski and Hieter, 1989]).

Finally, to ensure that the key results are insensitive to the exact promoter used for controlling the expression of yEVenus, we constructed four extra isogenic plasmids with different, naturally occurring promoters in the yeast genome. These promoters drive the expression of cytosolic proteins (Gpp1p, Tal1p, Pdc1p, and Tdh3p), all which are as highly abundant as the constitutively expressed Hsp90p (HSC82, source: PeptideAtlas 2013 dataset [Wang et al., 2012]). Specifically, the pHSC82 region was eliminated from the hc_Venus plasmid after SacI-NheI digestion. Next, the promoter regions of GPP1, TAL1, PDC1, and TDH3 were amplified from wild type genomic DNA using restriction site-containing oligonucleotides (frw_SacI, rev_NheI). Finally, the PCR products (pGPP1, pTAL1, pPDC1, and pTDH3) were inserted into the SacI-NheI digested hc_Venus plasmid backbone. Fluorescence level showed only minor variation across the five high copy plasmid constructs (Figure 3—figure supplement 1A).

### Cellular quantification of yEVenus protein

To quantify the yEVenus protein within the proteome, whole cell extracts were prepared from wild type cells, in the presence and absence of the yEVenus plasmid. Single colonies were inoculated into leucine dropout SC-MSG liquid medium, and were grown until saturation at 30°C. The saturated cultures were diluted and grown to mid-exponential phase (OD600 = 0.8), and 108–109 cells were used to extract total protein using established protocol (Visweswaraiah et al., 2011). Whole cell extract (WCE) concentration was determined by using Bicinchoninic Acid Kit (Sigma-Aldrich), according to the manufacturer's instructions. Whole cell extracts from the control and overexpression strain were separated on a 4–20% gradient Tris-Glycine gel (Lonza, Germany) under denaturing (SDS, sodium dodecyl sulfate) conditions, along with a dilution series (100–800 ng) of a standard protein (1 mg/ml bovine serum albumin, BSA, Sigma-Aldrich). Densitometry analysis of the protein bands on SDS-polyacrylamide gel was conducted by ImageJ software (Schneider et al., 2012). A standard curve was established by plotting the pixel numbers of BSA dilution series bands versus BSA concentrations. The yEVenus band (27 kDa) intensity was corrected by subtracting the intensity of the equal-sized protein band in the control strain. Based on the standard curve, the pixel number of the yEVenus band (27 kDa) was converted into concentration, and the ratio of the quantified yEVenus protein to the loaded whole cell extract was calculated.

### Synthetic genetic array analysis

To identify genes mediating yEVenus burden, we performed a synthetic genetic array (SGA) screen (Tong and Boone, 2006). The query mutation (in our case the yEVenus carrying plasmid) was crossed to an ordered array of ~5000 viable, non-essential gene deletion mutants (MATa; YKO collection, Open BioSystem, Dharmacon Inc, Lafayette, Colorado, United States, [Giaever et al., 2002]). The method applies a series of replica pinning steps onto solid medium in an automated manner, using the following series of steps: (a) selection for MATa/α diploids (SC-MSG medium (1 g/l monosodium glutamate, 1.7 g/l Yeast Nitrogen Base, supplemented by amino-acid mix) with G418 (200 µg/ml, Sigma-Aldrich) was used), (b) induced sporulation by reducing carbon and nitrogen levels in the nutrient, (c) selection for MATα meiotic progeny (can1∆::MFA1pr-HIS3, lyp1∆) using canavanine (50 mg/L, Sigma-Aldrich) and thialysine (S-(2-Aminoethyl)-L-cysteine hydrochloride, 50 mg/L, Sigma-Aldrich) containing medium, (d) selection for the query mutation (leucine dropout medium), and finally selection for the gene deletions (G418 containing medium; KanMX4 cassette confers resistance against G418). Finally, the array of meiotic progeny harboring both mutations (yEVenus plasmid and gene deletion) was scored for fitness (see below). To evaluate genetic interactions, an array of ‘single’ mutants was also constructed, where the query strain harbors the control high copy plasmid (YEplac181), without the fluorescent protein ORF.

The HIS3 (YOR202W) deletion strain (his3::KanMX4) was used as wild type control, for the following reasons: (1) fitness of this strain is indistinguishable from the BY4741 parental wild type strain (Qian et al., 2012); (2) it possesses the same selection marker (required for the SGA method) as all other single gene deletion strains; (3) it carries the KanMX4 cassette in the nonfunctional his3Δ1 allele.

### Quantitative fitness measurements

We developed a robust high-throughput and precise workflow for fitness measurements based on colony size. Solid media were prepared using 2% agar (2% was previously found to be optimal for reproducible colony size measurement, data not shown). The ordered arrays of strains at 384-density were replicated onto solid medium with a robotized replicating system. The system consists of a Microlab Starlet liquid-handling workstation (Hamilton Bonaduz AG, Switzerland), equipped with a 384-pin replicating-tool (S&P Robotics Inc, Toronto, Ontario, Canada) and a custom-made sterilization station for the replicating-tool. After 48 hr of acclimatization to the medium at 30°C, plates were replicated again onto the same medium and photographed after 48 hr of incubation at 30°C. Digital images were processed to calculate colony sizes. We took special care to control for potential systematic biases in colony growth, such as uneven media composition, changes in physical parameters of incubation, or competition for nutrients between neighboring colonies (Szamecz et al., 2014). Colonies located next to the edges/corners of the plates and colonies with low circularity (i.e. circularity <0.8) were removed from further analysis. Genotype fitness was estimated by the mean fitness of six replicate colonies. The replicate number used is comparable to (eight replicates for Kuzmin et al, in preparation) or even higher than the number of replicates other studies (four replicates for ([Hoke et al., 2008; Baryshnikova et al., 2010; Costanzo et al., 2010]) used to estimate fitness based on colony size.

Genetic interactions score was calculated as ε = fab − (fa ×fb), where fa and fb are quantitative fitness measures of the two single (deletion or yEVenus overexpression) mutants, while fab is the fitness of the double mutant (deletion and yEVenus overexpression). Negative (ε <0) and positive (ε >0) interaction scores indicate that the fitness defect of the double mutant is higher and lower than expected by the multiplicative model, respectively. We applied the confidence threshold of |ε|>0.05 and p<0.05 to define significantly interacting gene pairs. p-values were calculated using the bootstrap method (Efron and Tibshirani, 1994), resampling fa, fb, and fab separately. We tested the null hypothesis that ε = 0.

### Functional enrichment analysis

Based on the systematic genetic-genetic interaction screen, the list of genes showing negative interaction with the yEVenus overexpression (i.e. their deletions increased the fitness effect of overexpression) were retrieved and tested for Gene Onthology term enrichment with topGO (version 2.28) (Alexa et al., 2006) and org.Sc.sgd.db (version 3.3.0, [Carlson, 2016]) packages in R programming environment (Core Team, 2017). To focus on the important GO terms, we restricted our search to the GOSlim categories maintained by the SGD project (Cherry et al., 2012). A GO category was termed as enriched significantly, if the genes annotated to a particular GO term were significantly overrepresented (Fisher's exact test, odds ratio >1, p<0.05, FDR-corrected p<0.1) in the given gene set using the complete list of screened genes as background.

### Fitness estimates under environmental stress

Genotype fitness was estimated under control (no-stress) and different stress environments, as above. Unless otherwise indicated, all conditions used leucine dropout SC-MSG medium. The following non-lethal stress conditions were used: translation inhibition (0.0018–0.18 µg/ml cycloheximide, AppliChem GmbH, Germany), transcription inhibition (0.30 µg/ml mycophenolic acid (MPA), Santa Cruz Biotechnology, Germany), heat stress (37°C and 40°C), proteotoxic stress (1–2.5 mM azetidine-2-carboxylic acid (AZC), Santa Cruz Biotechnology), amino acid limitation (auxotrophic amino acids were supplied at normal concentration to the medium, while the non-auxotrophic amino acids were serially diluted (i.e. 0x - 2x of the regular concentration)). Fitness cost of yEVenus protein overproduction (proxy for protein burden) is defined by 1 - WV/WC, where WV and WC indicate absolute fitness values (i.e. colony sizes) of the genotypes with yEVenus and control plasmids, respectively.

### Evaluation of fluorescence level across genotypes

The fluorescence level of the final SGA array strains was evaluated by measuring yEVenus signal in liquid medium. Briefly, the array of colonies were inoculated into liquid leucine dropout SC-MSG medium, and kinetic runs were initiated in a Synergy 2 fluorescence plate reader (Biotek, Winooski, Vermont, United States) for 48 hr, using the following filters: 500/27 (excitation), 528/20 (emission). During the kinetic run, the absorbance (OD600) and yEVenus fluorescence (λex515 nm / λem528 nm) of the growing cultures were monitored simultaneously, with time points taken every 1.5 min. For each time points, the OD600 normalized yEVenus fluorescence (FLOD) was calculated. The fluorescence of a given strain was assessed by calculating the median of the five highest FLOD values.

### Quantitative aggregation assay

In order to quantitatively measure and compare the level of protein aggregation in the double mutants to the corresponding single mutants (i.e. deletion), an established method (Kaganovich et al., 2008) was applied. This method examines the condition of the protein quality-control machinery of the cell, based on the aggregation of a fluorescently tagged (mCherry, λex587nm/λem610nm) human protein (von-Hippel-Lindau, VHL). This human protein is prone to misfolding in the absence of its cofactor (elongin BC), which is not present in S. cerevisiae. Fully functional quality-control machinery can stop aggregation of VHL-mCherry, leading to disperse cytosolic localization of the fluorescence. On the other hand, an overload of the control machinery promotes VHL protein aggregation, while leaving the fluorescent tag functional. In this case, the red fluorescence appears as a puncta inside the cell, due to the sequestration of aggregated proteins into dedicated compartments. All mutants carrying the plasmid (pGAL-VHL-mCherry-Ura) were grown until saturation in leucine and uracil dropout SC-MSG medium, containing 2% raffinose as carbon source. To induce VHL-mCherry production, the saturated cultures were diluted into leucine and uracil dropout SC-MSG medium, containing 1% raffinose and 2% galactose. After 14 hr of induction, cell fluorescence was detected by high content microscopy, using the following filter sets: excitation: 560–580 nm, emission: 590–640 nm. Images were acquired by employing an Operetta high-content screening microscope (PerkinElmer, Waltham, Massachusetts, United States). Samples were grown and images were acquired in black optical 96-well plates (Greiner Bio-One, Austria) using a 60x high-numerical aperture objective. Five image stacks were made in each well, each of which consists of 7 z-stacks ranging from −1.5 µm to 1.5 µm relative to the focal plane with 0.5 µm step size. The following custom developed image and data analysis pipeline was used. First, an image filter was applied to amplify spots and project a z-stack. Images were corrected for illumination inhomogeneities (Smith et al., 2015), single cells were segmented and 118 cellular features were measured based on morphology, shape and intensities. Machine learning-based phenotypic analysis was performed (Horvath et al., 2011; Piccinini et al., 2017) using supervised learning and the ratio of phenotypic classes was determined. The ratio of cells containing aggregation loci was calculated using at least 2000 cells.

### Identification of protein–protein interactions

To reveal the in vivo physically interacting protein partners of yEVenus, whole cell extracts were prepared from wild type cells in both the presence and absence of the yEVenus overexpression plasmid, and then a GFP co-immunoprecipitation (GFP co-IP) assay was performed. First, single colonies were inoculated into leucine-dropout SC-MSG liquid medium, and were grown until saturation at 30°C. The saturated cultures were diluted and grown to mid-exponential phase (OD600 = 0.8), and 108–109 cells were collected, flash frozen and used to extract total protein using an established protocol (Visweswaraiah et al., 2011). Protein concentration of the whole cell extract (WCE) was determined by using Bradford Protein Assay (Bio-Rad, Hercules, California, USA), according to the manufacturer's instructions. Total protein extracts (2 mg) were immunopurified (IP) using 40 µl anti-GFP antibody-coupled 50 nm superparamagnetic beads (µMACS GFP Isolation Kit, Miltenyi Biotec, Germany). The unbound material was removed by washing the beads with 2 ml (equal to 50x beads volume) detergent-free buffers as follows: three times with 1x TBS and once with 25 mM ABC(NH4HCO3) buffer. The immunopurified proteins were desalted (Hubner et al., 2010) after on-bead-digestion with trypsin (Promega, Germany). The LC-MS/MS analysis was performed by using a nanoflow RP-HPLC on-line coupled to a linear ion trap-Orbitrap (Orbitrap-Elite, Thermo Fisher Scientific, Germany) mass spectrometer as in a previous study (Kobayashi et al., 2015) with the following modification: the 20 most abundant, multiply charged ions were selected from each MS survey for MS/MS analysis.

Raw data were converted into peak lists using Proteome Discoverer (v 1.4, Thermo Fisher Scientific). First, we performed a search against the Swissprot and Uniprot databases (Pundir et al., 2017), taking into consideration of the sequence of yEVenus. Search parameters and acceptance criteria were set as previously published (Kobayashi et al., 2015). Close homologues were only reported if at least three unique peptides matched to the protein.

Spectral counting was used to estimate relative abundance of individual proteins in the samples: peptide counts of the individual proteins were normalized to the total number of peptide identifications in each sample (Horvath et al., 2017). Proteins (i) with reproducible detection (|log2fold-change| < 0.67 between biological replicates), (ii) with at least two identified peptides, (iii) with at least 5% coverage and (iv) with a median-normalized protein binding affinity score above a previously defined cutoff value (2 according to [Li et al., 2016]) were considered as proteins that specifically associate with yEVenus. Protein-binding affinity to yEVenus was estimated by calculating the peptide count fold change of yEVenus IP (wild type strain with yEVenus plasmid) samples relative to the negative control IP samples (wild type strain with control plasmid).

Reciprocal co-immunoprecipitation (co-IP) was performed in order to investigate physical interaction partners of Sti1p. First, a PCR-based C-terminal epitope-tagging of Sti1p was performed using established protocols (Funakoshi and Hochstrasser, 2009). Briefly, the transformation cassette was amplified from the pFA6a-TEV-6xGly-3xFlag-HphMX plasmid (a gift from Tim Formosa, Addgene plasmid # 44083) with primers containing homology to the C-terminal of STI1. Transformants were selected on YPD containing 300 µg/ml hygromycin (Santa Cruz Biotechnology). Correct clones were verified by colony-PCR and subsequent capillary sequencing of the C-terminal of STI1. Next, the single copy (low protein burden) or high copy (high protein burden) yEVenus plasmid was transformed into the Sti1p-FLAG-tagged strain. Finally, the yEVenus expressing strains were subjected to co-IP assay.

Whole cell extraction (WCE), immunoprecipitation (IP) and washing steps were performed as above, with the following modification: to reduce the effect of protein burden, a more stringent washing step was applied using the manufacturer’s (μMACS DYKDDDDK Isolation Kit, Miltenyi Biotec) ‘Wash 1’ buffer (150 mM NaCl, 1% Igepal CA-630, 0.5% sodium deoxycholate, 0.1% SDS, 50 mM Tris-HCl, pH 8.0). The LC-MS/MS and raw data analysis were the same as above. Close homologues were only reported if at least three unique peptides matched to the protein. The effect of protein burden on Sti1p interacting partners was investigated by comparing the protein binding affinity of these partners under low and high protein burden. Binding affinity scores below the cutoff value indicate weaker, non-specific associations of proteins with Sti1p. Protein-binding affinity to Sti1p was estimated by calculating the peptide count fold change of Sti1p IP (IP with specific antibody to FLAG) samples relative to the negative control IP (IP without specific antibody (protein A)) samples both under low and high protein burden. Proteins i) with at least two identified peptides; ii) with at least 5% coverage and iii) with a median-normalized protein-binding affinity score above a previously defined cutoff value (two according to [Li et al., 2016]) were considered as proteins that specifically associate with Sti1p under low protein burden.
