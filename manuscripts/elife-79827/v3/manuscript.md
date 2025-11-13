# A genetic and linguistic analysis of the admixture histories of the islands of Cabo Verde

## Authors

- Romain Laurent<sup>1</sup> ([ORCID: 0000-0003-0363-2954](https://orcid.org/0000-0003-0363-2954))
- Zachary A Szpiech<sup>2</sup> ([ORCID: 0000-0001-6372-8224](https://orcid.org/0000-0001-6372-8224))
- Sergio S da Costa<sup>1</sup>
- Valentin Thouzeau<sup>4</sup>
- Cesar A Fortes-Lima<sup>6</sup> ([ORCID: 0000-0002-9310-5009](https://orcid.org/0000-0002-9310-5009))
- Françoise Dessarps-Freichey<sup>1</sup>
- Laure Lémée<sup>7</sup>
- José Utgé<sup>1</sup>
- Noah A Rosenberg<sup>8</sup>
- Marlyse Baptista<sup>9</sup>
- Paul Verdu<sup>1</sup> ([ORCID: 0000-0001-6828-268X](https://orcid.org/0000-0001-6828-268X)) †

### Affiliations

1. UMR7206 Eco-anthropologie, CNRS-MNHN-Université Paris Cité Paris France ([ROR:02feahw73](https://ror.org/02feahw73))
2. Department of Biology, Pennsylvania State University University Park United States ([ROR:04p491231](https://ror.org/04p491231))
3. Institute for Computational and Data Sciences, Pennsylvania State University University Park United States ([ROR:04p491231](https://ror.org/04p491231))
4. UMR7534 Centre de Recherche en Mathématiques de la Décision, CNRS-Université Paris-Dauphine-PSL University Paris France ([ROR:013cjyk83](https://ror.org/013cjyk83))
5. Département d'Etudes Cognitives, Laboratoire de Sciences Cognitives et Psycholinguistique, ENS-PSL University-EHESS-CNRS Paris France ([ROR:013cjyk83](https://ror.org/013cjyk83))
6. Department of Organismal Biology, Sub-department of Human Evolution, Evolutionary Biology Centre, Uppsala University Uppsala Sweden ([ROR:048a87296](https://ror.org/048a87296))
7. Plateforme Technologique Biomics–Centre de Ressources et Recherches Technologiques (C2RT), Institut Pasteur Paris France ([ROR:0495fxg12](https://ror.org/0495fxg12))
8. Department of Biology, Stanford University Stanford United States ([ROR:00f54p054](https://ror.org/00f54p054))
9. Department of Linguistics, University of Michigan Ann Arbor United States ([ROR:00jmfr291](https://ror.org/00jmfr291))
10. Department of Afroamerican and African Studies, University of Michigan Ann Arbor United States ([ROR:00jmfr291](https://ror.org/00jmfr291))

† Corresponding author

## Abstract

From the 15th to the 19th century, the Trans-Atlantic Slave-Trade (TAST) influenced the genetic and cultural diversity of numerous populations. We explore genomic and linguistic data from the nine islands of Cabo Verde, the earliest European colony of the era in Africa, a major Slave-Trade platform between the 16th and 19th centuries, and a previously uninhabited location ideal for investigating early admixture events between Europeans and Africans. Using local-ancestry inference approaches, we find that genetic admixture in Cabo Verde occurred primarily between Iberian and certain Senegambian populations, although forced and voluntary migrations to the archipelago involved numerous other populations. Inter-individual genetic and linguistic variation recapitulates the geographic distribution of individuals’ birth-places across Cabo Verdean islands, following an isolation-by-distance model with reduced genetic and linguistic effective dispersals within the archipelago, and suggesting that Kriolu language variants have developed together with genetic divergences at very reduced geographical scales. Furthermore, based on approximate bayesian computation inferences of highly complex admixture histories, we find that admixture occurred early on each island, long before the 18th-century massive TAST deportations triggered by the expansion of the plantation economy in Africa and the Americas, and after this era mostly during the abolition of the TAST and of slavery in European colonial empires. Our results illustrate how shifting socio-cultural relationships between enslaved and non-enslaved communities during and after the TAST, shaped enslaved-African descendants’ genomic diversity and structure on both sides of the Atlantic.

## Introduction

Between the 15th and 19th centuries, European colonization and the Trans-Atlantic Slave-Trade (TAST) put into contact groups of individuals previously isolated genetically and culturally. These forced and voluntary migrations profoundly influenced the descent of numerous European, African, and American populations, creating new cultures, languages, and genetic patterns (Eltis and Richardson, 2015; Fortes-Lima and Verdu, 2021).

Population geneticists have extensively described genetic admixture patterns in enslaved-African descendants in the Americas, and mapped their genomes for regions of ancestry recently shared with continental Africa and Europe (Micheletti et al., 2020; Ongaro et al., 2019). This allowed for reconstructing their detailed possible origins, as this knowledge is often intractable with genealogical records alone (Eltis and Richardson, 2015). Furthermore, genetic admixture-mapping methods have been used to identify genetic variation underlying phenotypic variation (Winkler et al., 2010; Wojcik et al., 2019), and to identify post-admixture natural selection signatures (Patin et al., 2017), thus revealing how admixture shaped human populations’ recent evolution. Maximum-likelihood approaches based on linkage-disequilibrium (LD) patterns of admixed individuals Gravel, 2012; Hellenthal et al., 2014 have repeatedly highlighted the diversity of admixture processes experienced by populations historically related to the TAST. In particular, they identified different European, African, and American populations, respectively, at the source of genetic admixture patterns, sometimes consistent with the preferred commercial routes of each European empire (Gravel, 2012; Mathias et al., 2016). Furthermore, they identified variable timing of admixture events during and after the TAST, sometimes consistent with major socio-historical events such as the expansion of the plantation economic system or the abolition of slavery (Moreno-Estrada et al., 2013; Baharian et al., 2016). From a cultural perspective, linguists have shown that novel contact-languages, such as creole languages (Holm, 2000; Escure and Schwegler, 2004), emerged from recurring interactions between socio-economically dominant Europeans and Africans and Americans. Furthermore, they identified the languages of origin of numerous linguistic traits in several creole languages (Quint, 2000; Essegbey et al., 2013; Baptista, 2015), and emphasized the complex histories of contacts that shaped language diversity on both sides of the Atlantic.

Numerous questions remain unsolved and novel interrogations have emerged concerning the history of admixture during and after the TAST. (i) While the genetic history of enslaved-African descendants in the Americas has been extensively studied, the influence of the TAST on genetic admixture in Africa remains under-investigated. Studying these questions in Africa would provide invaluable information about the influence of the onset and early stages of the TAST and the subsequent expansion of European empires on genetic admixture patterns on both sides of the Atlantic. (ii) While admixture-LD inference methods have repeatedly brought novel insights into the admixture processes experienced by enslaved-African descendant populations, they could only explore historical models with one or two pulses of admixture, a methodological limitation (Gravel, 2012; Hellenthal et al., 2014). Complex admixture histories may be expected as a result of the recurring flows of enslaved-Africans forcibly displaced between and within continents, changes of social relationships among enslaved and non-enslaved communities, and variable assimilation of new migrants in pre-existing communities, during and after the TAST (Eltis, 2002; Berlin, 2009). (iii) Finally, while the comparison of genetic and linguistic diversities has been the focus of numerous evolutionary anthropology studies at large geographical scales (Creanza et al., 2015; Cavalli-Sforza et al., 1988), it has rarely been endeavored for creole-speaking populations at a local scale in the historical context of the TAST (Ansari-Pour et al., 2016; Verdu et al., 2017; Hagemeijer and Rocha, 2019).

Here, we propose to reconstruct the detailed genetic and linguistic admixture histories of Cabo Verde, as this archipelago represents an ideal case to address these three understudied aspects of TAST history. First, Cabo Verde is the first European settlement-colony in Sub-Saharan Africa, located 500 kms West of Senegal in Western Africa (Figure 1), and settled in the 1460s by Portuguese immigrants and enslaved-Africans forcibly removed from the continental mainland. After 1492, and in particular after the 17th century expansion of the plantation economy in the Americas, Cabo Verde served as a major slave-trade platform between continents (Carreira, 2000). Second, Cabo Verde forms an archipelago of nine inhabited islands that were settled over the course of three centuries due to the changing political, commercial, and migratory contexts (Albuquerque and Santos, 1991; Albuquerque and Santos, 1995; Albuquerque and Santos, 2007). Therefore, studying the admixture history of Cabo Verde will provide unique insights into the onset of the TAST before 1492, and into the history of slavery thereafter. This setting further promises to illustrate, at a micro-geographical scale, island-per-island, the fundamental socio-historical and serial founding migrations mechanisms having influenced genomic patterns in admixed populations throughout the TAST. Finally, Cabo Verdean Kriolu is the first creole language of the TAST, born from contacts between the Portuguese language and a variety of African languages (Quint, 2000; Baptista, 2015; Baptista, 2003; Lang, 2009). The archipelago thus represents a unique opportunity to investigate, jointly, genetic and linguistic admixture histories and their interactions since the mid-15th century.

![Figure 1.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig1-v3.jpg)

**Figure 1.:** Birth-location of 225 individuals within Cabo Verde are indicated in the bottom map-panel, and birth locations outside Cabo Verde for 6 individuals are indicated in Figure 1—source data 1. Linguistic and familial anthropology interview, and genetic sampling for Cabo Verde participants were conducted during six separate interdisciplinary fieldworks between 2010 and 2018. Further details about populations are provided in Figure 1—source data 1.

Previous genetic studies exploring, first, sex-specific genetic diversity, and, then, genome-wide markers from several islands of the archipelago (Brehm et al., 2002; Gonçalves et al., 2003; Beleza et al., 2012; Beleza et al., 2013), attested to the dual, sex-biased, origins of the Cabo Verdean gene-pool, resulting mainly from admixture between African females and European males. Furthermore, these studies described variable admixture patterns between mainland Africa and Europe across islands without distinguishing source populations from different sub-regions within continents. Another, more recent, study investigated which continental mainland European and African populations may have contributed to the Cabo Verde gene-pool without focusing on possible variation across islands (Micheletti et al., 2020). Interestingly, adaptive-introgression signals for malaria resistance in Santiago island were recently identified as a result of migrations and genetic admixture during the TAST (Hamid et al., 2021). Finally, while joint analyses of genetic and linguistic diversities from the island of Santiago showed that genetic and linguistic admixture histories possibly occurred in parallel (Verdu et al., 2017), these previous studies did not attempt to formally reconstruct the admixture processes and detailed demographic histories that influenced the observed patterns of genetic or linguistic diversity on the islands of Cabo Verde.

Based on these previous studies, we propose to first determine which continental African and European populations in fact contributed to the genetic landscape of each Cabo Verdean island today. Indeed, which enslaved-African populations only briefly transited through the archipelago, and which remained for longer periods is largely debated by historians (Carreira, 2000; Albuquerque and Santos, 1991; Albuquerque and Santos, 1995); and, while Portuguese influence is clear, further details about which European migrations genetically influenced Cabo Verde remain to be assessed (Soares, 2011). These aspects are often crucial for understanding the genetic history of enslaved-African descendant populations on either side of the Atlantic (Eltis and Richardson, 2015; Baharian et al., 2016; Berlin, 2010; Gouveia et al., 2020). Second, we propose to further evaluate the possible parallels between genetic and linguistic admixture histories at a micro-geographical scale within each island. We aim at better understanding how contacts shaped cultural variation during the TAST by deciphering the parent-offspring dispersal behaviors within and across islands which shaped the biological and cultural diversity in the archipelago (Verdu et al., 2017). This can be achieved indirectly by exploring the influence of isolation-by-distance mechanisms on the distribution of genetic and linguistic diversity at very reduced geographical scale (~50 km) within a population (Rousset, 1997; Barbujani, 1987; Malécot, 1975; Barbujani and Sokal, 1991; Cavalli-Sforza and Moroni, 2004; Verdu et al., 2010). Finally, we reconstruct the detailed history of admixture dynamics in each island since the 15th century, using statistical inference of possible complex admixture histories with Approximate Bayesian Computation (Fortes‐Lima et al., 2021). Altogether, this highlights the socio-historical mechanisms that shaped the genetic and linguistic diversity of the Cabo Verde population, the first to be born from the TAST.

## Results

We investigate genetic and linguistic variation in 233 family unrelated Kriolu speakers from the nine Cabo Verdean islands (Brava, Fogo, Santiago, Maio, Sal, Boa Vista, São Nicolau, São Vicente, Santo Antão, Figure 1, Figure 1—source data 1). With novel genome-wide genotyping autosomal data (Appendix 1—figure 1), we first describe genetic differentiation patterns in Cabo Verde and other enslaved-African descendants in the Americas from previous datasets, in particular with respect to continental Africa and Europe. Next, we deploy local-ancestry inferences and determine the best proxy source-populations for admixture patterns in each Cabo Verde island. We then describe runs of homozygosity and genetic isolation-by-distance patterns at reduced geographical scale within Cabo Verde. We also investigate Kriolu linguistic diversity with respect to geography and socio-cultural co-variates and, then, investigate jointly genetic and linguistic admixture patterns throughout the archipelago. Finally, we infer the detailed genetic admixture history of each island using the machine-learning MetHis-Approximate Bayesian Computation (ABC) approach (Fortes‐Lima et al., 2021).

### Cabo Verde and other TAST-related admixed populations in the worldwide genetic context

We explored genetic diversity patterns captured along the first three axes of the multi-dimensional scaling (MDS) projection of individual pairwise allele sharing dissimilarities (ASD Bowcock et al., 1994), computed from different individual subsets (Figure 1—source data 1). This ASD-MDS approach is mathematically analogous to PCA based on individual genotypes and therefore captures similar information about individual pairwise genetic differentiation (Hastie et al., 2009; Chap.-18.5.2). However, ASD-MDS allows to explore pairwise genetic differentiation for successive individual subsets much more efficiently computationally than classical PCA. Indeed, the individual pairwise ASD matrix only needs to be computed once and then simply subsampled before being projected, and successive subset of individual-pairwise ASD matrices are thus always several orders of magnitude smaller in dimensions than the genotype table to be projected with PCA which comprises, here, 455,705 SNPs in all cases. Detailed ASD-MDS decompositions are provided in Appendix 2 and Appendix 2—figures 1–4. Note that we considered seven geographical regions in Africa shown in Figure 1.

Figure 2 shows that the second ASD-MDS axis distinguishes West Western African Senegambian populations from East Western Africans, while Central Western Africans are at intermediate distances between these two clusters. Moreover, the third MDS axis separates Northern and Southern European populations; the British-GBR and USA-CEU individuals clustering at intermediate distances between the Finnish-FIN, and a cluster represented by Iberian-IBS and Tuscan-TSI Western Mediterranean individuals. Consistently with previous results (Micheletti et al., 2020; Verdu et al., 2017), on the first three MDS axes, Cabo Verdean individuals cluster almost exclusively along a trajectory from the Southern European cluster to Senegambia (Figure 2A–C), with little traces of affinity with other African or European populations. Instead, the USA African-American ASW (Figure 2—figure supplement 1 panels A-C) and Barbadian-ACB (Figure 2—figure supplement 1 panels D-F) cluster along a trajectory going from the GBR and CEU cluster to Central and East Western Africa; and Puerto Ricans-PUR cluster along a trajectory going from the Southern European cluster to the Central Western African cluster (Figure 2—figure supplement 1 panels G-I).

![Figure 2.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig2-v3.jpg)

**Figure 2.:** (A–C) Three-dimensional MDS projection of ASD computed among 233 unrelated Cabo Verdeans and other continental African and European populations using 445,705 autosomal SNPs. Cabo Verdean patterns in panels A–C can be compared to results obtained considering instead the USA African-Americans ASW, the Barbadians-ACB, and the Puerto Ricans-PUR in the same African and European contexts and presented in Figure 2—figure supplement 1. We computed the Spearman correlation between the matrix of inter-individual three-dimensional Euclidean distances computed from the first three axes of the MDS projection and the original ASD matrix, to evaluate the precision of the dimensionality reduction. We find significant (p<2.2 × 10–16) Spearman ρ=0.9635 for the Cabo Verde analysis (A–C). See Figure 1—source data 1 for the populations used in these analyses. Sample locations and symbols are provided in panel D.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Three-dimensional MDS projection of ASD computed using 445,705 autosomal SNPs among continental African and European populations and, respectively, the USA African-American ASW (panels A-C), the Barbadians-ACB (panels D-F), or the Puerto Ricans-PUR (panels G-I), in the same European and African contexts as explored in Figure 2 for Cabo Verdeans in the main text. We computed the Spearman correlation between Euclidean distances on the 3D-MDS projections and the original ASD matrix to evaluate the precision of the dimensionality reduction. We find Spearman ρ=0.9383 (p<2.2 × 10-16) for the ASW (A-C); 0.9306 (p<2.2 × 10-16) for the ACB (D-F); and 0.9437 (p<2.2 × 10-16) for the PUR (G-I). Each individual is represented by a single point. Sample locations and symbols are given in panel J (Figure 1—source data 1).

### Genetic structure in Cabo Verde and other TAST-related admixed populations

Based on these results, we further investigated patterns of individual genetic structure among Cabo Verde-born individuals, ASW, and ACB populations with respect to European and Western, Central, South-Western, and Southern African populations (Figure 1—source data 1), using ADMIXTURE (Alexander et al., 2009). Indeed, ASD-MDS decompositions allow to efficiently identify major genetic pairwise dissimilarities among numerous samples, but exploring multiple combinations of higher order axes remains extremely difficult with this multivariate method. Instead, ADMIXTURE results recapitulate the major axes of genetic variation with increasing values of the number of clusters K, which allows to explore individual pairwise genetic resemblances for numerous major axes of variation at once. Extended descriptions of the results are presented in Appendix 3.

At K=2, the orange genetic-cluster in Figure 3A is maximized in African individuals while the blue alternative cluster is maximized in Europeans. Cabo Verdean, ASW and ACB individuals exhibit intermediate genotype-membership proportions between the two clusters, consistently with patterns expected for European-African admixed individuals. Among the Cabo Verdean, ASW, and ACB populations, ACB individuals show, on average, the highest membership to the orange ‘African’ cluster (88.23%, SD = 7.33%), followed by the ASW (78.00%, SD = 10.88%), and Cabo Verdeans (59.01%, SD = 11.97%). Membership proportions for this cluster are highly variable across Cabo Verdean islands, with highest average memberships for Santiago-born individuals (71.45%, SD = 10.39%) and Maio (70.39%, SD = 5.26%), and lowest for Fogo (48.10%, SD = 6.89%) and Brava (50.61%, SD = 5.80%). Inter-individual membership variation within Cabo Verde islands, captured as Fst/Fstmax values (Morrison et al., 2022), are significantly different across pairs of islands for 32 out of 36 comparisons (Wilcoxon rank-sum test p<3.96 × 10−8), with variability across islands ranging from a lowest value of 0.010 in individuals from Santo Antão to a highest value of 0.0519 in Santiago (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig3-v3.jpg)

**Figure 3.:** (A) Unsupervised ADMIXTURE analyses using randomly resampled individual sets for populations originally containing more than 50 individuals (Figure 1—source data 1). 225 unrelated Cabo Verdean-born individuals in the analysis are grouped by birth island. Numbers of runs highly resembling one another using CLUMPP are indicated below each K-value. All other modes are presented in Appendix 3—figure 1. (B) SOURCEFIND results for each eleven target admixed populations (ASW, ACB, each of the nine Cabo Verde birth islands), considering respectively 4 or 6 possible source surrogate populations (abbreviated ‘surrog.’) among the 24 possible European, African, and East Asian populations considered in the ADMIXTURE analyses. The cumulated average African admixture levels in each admixed population was highly consistent between SOURCEFIND estimates and ADMIXTURE results at K=2 (Spearman ρ=0.98861, p<2 × 10–8 and 0.99772, p<8 × 10–12, for 4 or 6 surrogates, respectively). Furthermore, individual admixture levels estimated using an ASD-MDS-based approach (Material and Methods and Appendix 1—figure 2), were highly consistent with individual admixture estimates based on ADMIXTURE results at K=2 (ρ=0.99725; p<2.2 × 10–16 for Cabo Verde; ρ=0.99568; p<2.2 × 10–16 for ASW; ρ=0.99366; p<2.2 × 10–16 for ACB).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Fst/Fstmax values were computed using FSTruct (Morrison et al., 2022) with 1000 bootstrap replicates per population. All population pairwise distributions of bootstrap Fst/Fstmax values were significantly different from one another after Bonferroni correction (Wilcoxon two-sided rank sum test p<3.96 × 10−8), except the following pairwise comparisons: ACB-Santiago, Brava-Maio, Fogo-Sal, and Maio-Santo Antão.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** As mentioned in the main text of the article, we calculated f3-admixture (Patterson et al., 2012) considering as admixture targets each Cabo Verdean birth-island (panel A), the ASW (panel B), and the ACB (panel B) separately, with, as admixture sources, all 108 possible pairs of one continental European population (Source 1) and one continental African population (Source 2), or the East Asian CHB (Source 1) and one continental African population (Source2), using the same individuals, population groupings, and genotyping dataset as in the previous ADMIXTURE analyses (Figure 1—source data 1). Results for each pair of possible sources are plotted in diminishing values of f3-admixture obtained specifically with Cabo Verde individuals born on Santiago as targets. Target population symbols are indicated in the legend at the bottom-right of each panel.

At K=5, the new red cluster is maximized in the YRI, Igbo, and ESN populations, distinct from Western and Southern African orange and grey clusters, respectively. Note that the former orange cluster is almost completely replaced with red membership in the ACB and ASW populations, while it remains large for all Cabo Verdean-born individuals. Moreover, Cabo Verde-born individuals’ patterns of membership proportions to the orange, red or grey ‘African’ clusters differ here between individuals born on Santiago, Fogo, Brava, and Maio, and individuals born on Sal, Boa Vista, São Nicolau, São Vicente, and Santo Antão, respectively. The former group of islands exhibit an ‘African’ component resembling patterns of membership proportions found in West Western African individuals, with a majority of membership to the orange cluster and a minority to the red cluster. Instead, the ‘African’ component in individuals born in the latter islands is almost exclusively orange. This potentially indicates differences in shared ancestries with different continental African populations across islands in Cabo Verde, which remains to be formally tested (see the next Results section).

At K=6, these two groups of islands are now clearly differentiated, as the novel green cluster is maximized in numerous individuals born on Sal, Boa Vista, São Nicolau, São Vicente, and Santo Antão, but represented to a much lesser extent in Santiago, Fogo, and Brava. Instead, individuals in these latter islands retain a majority of membership to the orange ‘West Western African’ cluster, and Maio-born individuals are now found intermediately between the two groups with relatively even memberships to the orange and green clusters respectively. Interestingly, this new green cluster appears to be specific to Cabo Verdean genetic variation, as it is virtually absent from other populations in our dataset except for a small proportion in certain Wolof individuals from West Western Africa.

At K=10, the light-green cluster is maximized in Cabo Verdean individuals born on Maio, Boa Vista, Sal, and São Nicolau, distinct form the dark green cluster maximized in individuals born on Santo Antão and São Vicente, and hence producing three distinct ADMIXTURE patterns among Cabo Verdean birth-islands. Furthermore, an alternative mode at K=10 shows (Appendix 3—figure 1) that Cabo Verde-born individuals resemble more IBS and TSI patterns for their European-like membership than ASW and ACB individuals who, instead, resemble more CEU and GBR patterns, consistently with ASD-MDS results (Figure 2 and Figure 2—figure supplement 1).

While the modal results comprising the most ADMIXTURE runs for increasing values of K from 11 to 13 differentiate novel clustering patterns among continental African and/or European populations (Figure 3), alternative, minority, modes here highlight novel possible clustering solutions in turn maximized in different groups of Cabo Verdean islands (Appendix 3—figure 1). Ultimately, these alternative ADMIXTURE results are resolved at K=14 (Figure 3), with the emergence of the new bright yellow cluster maximized in individuals from Boa Vista, and in part in individuals from Maio, while virtually absent from the rest of our data set.

Finally, at K=15, the novel dark green cluster is maximized in individuals born on Fogo and substantially present in Brava-born individuals’ membership proportions, while virtually absent from all other populations in our data set. Note that alternative clustering solutions at K=15 disentangle resemblances across other West Central and South-West Central African populations, but do not further propose additional clusters specifically represented by Cabo Verdean variation (Appendix 3—figure 1).

Therefore, altogether, we identified at least five clustering patterns across Cabo Verdean islands of births nested in increasing values of K, where, respectively, individuals from Fogo and Brava, from Santiago, from Boa Vista, from Sal and São Nicolau, and from Santo Antão and São Vicente resembled more one another than other individuals from elsewhere in Cabo Verde. In this context, note that Maio individuals cluster intermediately between the Santiago, Boa Vista and São Vicente clusters.

Finally, we aim at describing potential genetic resemblances between the East Asian gene-pool, represented here by the Chinese CHB population, and the Cabo Verdean gene-pool, as a community from China is established in the archipelago since at least the 1950s. Note that for every value of K above 3, the light-pink cluster mainly represented by Chinese CHB individuals is found in three ASW and one ACB individuals, as previously identified (Mathias et al., 2016), but is virtually absent in the Cabo Verdean individuals that were included in our study without criteria of geographic origins nor community belonging (see also Appendix 3).

Altogether, these ADMIXTURE results, differentiating patterns of genetic resemblance across Cabo Verde and with respect to varied continental African and European populations, have been possible to uncover due to inclusion of varied reference populations from continental Atlantic Africa and Europe, treating all Cabo Verdean islands of birth as differentiated in the analyses (Micheletti et al., 2020; Verdu et al., 2017; Beleza et al., 2013).

### Local-ancestry in Cabo Verde and other TAST-related admixed populations

ASD-MDS and ADMIXTURE descriptive analyses do not formally test admixture and putative source populations of origins, they rather disentangle genetic resemblances among groups of individuals. The resulting ADMIXTURE patterns could be due either to admixture from populations represented in our dataset, to admixture from populations un-represented in our dataset, or to common origins and drift (Alexander et al., 2009; Pritchard et al., 2000; Rosenberg et al., 2002; Falush et al., 2003; Lawson et al., 2018). We further analyzed the observed ADMIXTURE results by computing f3-admixture tests (Patterson et al., 2012). We considered as admixture targets each Cabo Verdean birth-island, the ASW, and the ACB separately, with, as admixture sources, in turn all 108 possible pairs of one continental African population and one continental European population, or one continental African population and the East Asian CHB, using the same individuals, population groupings, and genotyping dataset as in the previous ADMIXTURE analyses.

For each Cabo Verdean birth island as a separate target population and for all pairs of possible sources tested, we obtain negative values of f3-admixture (Figure 3—figure supplement 2), indicative of possible admixture signals (50). Altogether for the admixture of each Cabo Verdean birth-island, f3-admixture tests do not allow us to clearly discriminate among possible African sources, nor among possible European sources, due to largely overlapping f3-admixture values across tests (Figure 3—figure supplement 2). Note that f3 and f4 statistics have been recently shown to be strongly geometrically related to MDS/PCA and that its results need not be due to admixture only (Peter, 2022), similarly to MDS/PCA or ADMIXTURE results (Alexander et al., 2009; Pritchard et al., 2000; Rosenberg et al., 2002; Falush et al., 2003; Lawson et al., 2018). Therefore, we conducted admixture-LD haplotypic local-ancestry inferences with the SHAPEIT2-CHROMOPAINTER-SOURCEFIND pipeline (Lawson et al., 2012; Delaneau et al., 2012; Chacón-Duque et al., 2018), to more precisely identify the possible European and African populations at the sources of genetic patterns observed in enslaved-African descendant populations and Cabo Verdeans in particular.

Figure 3B shows striking differences concerning both the European and the African source populations involved in the admixture history of ACB, ASW, and individuals born on different Cabo Verdean islands. We find that individuals from all Cabo Verdean islands share almost all their European haplotypic ancestry with the Iberian-IBS population rather than other European populations. Santiago-born individuals present the smallest (27%) average haplotypic ancestry shared with IBS, and Fogo-born the highest (51%). Conversely, the ASW and ACB both share haplotypic ancestries only with the USA-CEU of North-Western European origin (20% and 12% respectively).

Furthermore, we find that all Cabo Verdeans almost exclusively share African haplotypic ancestries with two Senegambian populations (Mandinka and Wolof) and very reduced to no shared ancestries with other regions of Africa. More specifically, we find that the Mandinka from Senegal are virtually the sole African population to share haplotypic ancestry with Cabo Verdeans born on Brava, Fogo, Santiago, Maio, and Boa Vista, and the majority of the African shared ancestry for Sal, São Nicolau, São Vicente, and Santo Antão. In individuals from these four latter islands, we find shared haplotypic ancestry with the Wolof population ranging from 4%–5% for individuals born on Sal (considering four or six possible sources, respectively), up to 16–22% for Santo Antão. Finally, we find limited (1–6%) shared haplotypic ancestry with East Western (Igbo, YRI, or Ga-Adangbe) or South-West Central (Kimbundu, Kongo, or Ovimbundu) African populations in all Cabo Verdean islands, except Fogo and Brava, and the specific populations identified and their relative proportions of shared haplotypic ancestries vary across analyses. Conversely, we find that the ASW and ACB populations share African haplotypic ancestries in majority with East Western African populations (YRI, Ga-Adangbe, and Igbo), and substantial shared ancestries with Senegambian populations (5–10%), the MSL from Sierra Leone in Central Western Africa (5–12%), and South-West Central African populations (3–18%), albeit variable depending on the number of putative sources considered.

### Runs of homozygosity (ROH) and admixture patterns within Cabo Verde

Runs of homozygosity (ROH) are Identical-By-Descent haplotypes resulting from recent parental relatedness and present in individuals as long stretches of homozygous genotypes. Their length and abundance can reflect demographic events, such as population bottlenecks and founder events, natural selection, and cultural preferences for endogamy (Thompson, 2013; Mooney et al., 2018; Szpiech et al., 2019); and ROH have not been seen to depend strongly on recombination or mutation rate variation across the genome (Pemberton et al., 2012).

We find higher levels of long ROH (≥1 cM) in Cabo Verdeans compared to most other analyzed populations, including ASW and ACB (Figure 4A and Appendix 4—figure 1). We find the highest levels of long-ROH in individuals born on Maio, Boa Vista, Sal, São Nicolau, São Vincente, and Santo Antão, with a mean individual length of long-ROHs around 3 cM (Figure 4B), and the lowest levels of long-ROH in Santiago and Brava-born individuals. Among long ROH (Appendix 4—figure 2C), we find little to no correlation with total non-ROH levels for African local-ancestry segments (Pearson ρ=−0.06689, p=0.3179), European (ρ=0.1551, p=0.01989), or East Asian (ρ=0.06239, p=0.3516). Of all ROH identified, the mean proportion of ROH that were long ranged from 0.065 to 0.280 (Figure 4—source data 1).

![Figure 4.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig4-v3.jpg)

**Figure 4.:** (A) The distribution of the sum of long-ROH (≥1 cM) lengths per person for each Cabo Verdean birth-island and other populations. (B) The length distribution (log-10 scale) of individual long-ROHs identified within samples for each Cabo Verdean birth-island and other populations (e.g. for a distribution with mass at 1.0, this suggests individual ROHs of length 10 cM were identified among samples from that group). (C) The length distribution of ancestry-specific and ancestry-spanning individual long-ROHs for each Cabo Verdean birth-island. (D) The distribution of differences between individuals’ long-ROH ancestry proportion and their global ancestry proportion, for African and European ancestries separately and for each Cabo Verdean birth-island. * indicates significantly (α < 1%) different proportions of ancestry-specific long-ROH, based on non-parametric permutation tests, see Material and Methods, Figure 4—source data 2, and Figure 4—figure supplement 2.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig4-figsupp1-v3.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** As mentioned in Material and Methods, for each individual in each island, we randomly permuted the location of all long ROH (ensuring that no permuted ROH overlap), re-computed the local AFR ancestry proportion falling within these permuted ROH, and then subtracted the global ancestry proportion. We then take the mean of this difference across all individuals for each island and repeat the process 10,000 times. As there is negligible ASN ancestry across these individuals, the AFR and EUR proportions essentially add to 1, and therefore we consider an over/under representation of AFR ancestry in long ROH to be equivalent to an under/over representation of EUR ancestry in long ROH. Observed values in the real data set are provided as a red vertical line for each island of birth separately. Permutation p-values are reported in Figure 4—source data 2.

In admixed populations, we expected that some of the long ROH spanned local ancestry breakpoint switches (see Material and Methods), indicating that the most recent common ancestor existed after the initial admixture event having generated local-ancestry patterns. Furthermore, we expected that these ‘spanning’ ROH would be among the longest ROH observed if admixture occurred only in the past few generations. We find that (Figure 4C), almost uniformly across Cabo Verde, the longest ROH identified indeed spanned at least one ancestry breakpoint, excluding the very few East Asian ancestry regions identified. Furthermore, correcting ancestry-specific long-ROH sizes (Figure 4—figure supplement 1) for individuals’ total ancestry fraction of that ancestry, we find that individuals born in Fogo have, on average, an overrepresentation of European ancestry (and a corresponding underrepresentation of African ancestry) in long-ROH (Figure 4D; permutation p<10–4; Figure 4—figure supplement 2, Figure 4—source data 2), and that individuals from Santo Antão and São Vincente have, conversely, an apparent overrepresentation of African ancestry and underrepresentation of European ancestry in long ROH (permutation p=10–4 and p<10–4, respectively; Figure 4—figure supplement 2, Figure 4—source data 2). Finally, we find that individuals from Brava, Santiago, Maio, Boa Vista, São Nicolau, and Sal have relatively similar long-ROH levels in African and European segments (permutation p>0.01; Figure 4—figure supplement 2, Figure 4—source data 2). This latter pattern may be consistent with these populations being founded by admixed individuals, while the former patterns could indicate, in addition to such admixture founding effects, more recent or recurring contributions from the sources (Mooney et al., 2018).

### Genetic and linguistic isolation-by-distance within Cabo Verde

The above ASD-MDS, ADMIXTURE, local-ancestry inferences, and ROH results suggest substantial genetic differentiation at a very reduced geographical scale within the archipelago across Cabo Verdean birth-islands of individuals. Following previous linguistic investigations highlighting Kriolu qualitative linguistic variation across islands within the archipelago (Quint, 2000; Baptista, 2015; Baptista, 2003; Lang, 2009), we aim at further characterizing possible patterns of joint genetic and linguistic isolation (Rousset, 1997) at very reduced geographical scale across islands as well as within islands. Indeed, while the geographic distribution of genetic diversity has been previously extensively explored across human populations to reveal population migration routes, in particular in island and archipelago contexts (e.g. Arauna et al., 2022; Hunley et al., 2008), the underlying parent-offspring genetic and linguistic dispersal mechanisms have been seldom explored in humans at extremely local scales to our knowledge (Rousset, 1997; Barbujani and Sokal, 1991; Cavalli-Sforza and Moroni, 2004; Verdu et al., 2010). Nevertheless, knowledge about such dispersal mechanisms can be built by exploring the influence of isolation-by-distance mechanisms on genetic and linguistic diversity distributions at very reduced geographical scales (~50 km) within a population (Rousset, 1997; Barbujani, 1987; Malécot, 1975). We thus explored both pairwise ASD and inter-individual variation in manners of speaking Kriolu (characterized as differences in the frequencies of use of Kriolu utterances among individual discourses; see Material and Methods), in the same set of 225 Cabo Verde-born individuals. To do so, we used MDS and Mantel testing of correlations between, respectively, genetic and linguistic pairwise differentiation, and socio-cultural and geographical covariates including age, duration of academic education, residence locations, birth-places, and parental birth-places (Figure 5, Table 1, and Table 1—source data 1).

![Figure 5.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig5-v3.jpg)

**Figure 5.:** (A–B) 3D MDS projection of Allele Sharing Dissimilarities computed among 225 unrelated Cabo-Verde-born individuals using 1,899,878 autosomal SNPs. Three-dimensional Euclidean distances between pairs of individuals in this MDS significantly correlated with ASD (Spearman ρ=0.6863; p<2.2 × 10–16). (C–D) 3D MDS projection of individual pairwise Euclidean distances between uttered linguistic items frequencies based on the 4831 unique uttered items obtained from semi-spontaneous discourses. Three-dimensional Euclidean distances between pairs of individuals in this MDS significantly correlated with the utterance-frequencies distances (Spearman ρ=0.8647; p<2.2 × 10–16). (E) Spearman correlation ρ=0.2070 (p=0.0018) between individual African utterance scores and individual genetic African admixture rates obtained with ADMIXTURE at K=2. (F) Birth-locations of 225 individuals in Cabo Verde. Symbols for individuals’ birth-island in panels A–E are shown in panel F. Panel A–D were Procrustes-transformed according to individual actual birth-places’ geographical locations in panel F (Wang et al., 2010).

**Table 1.**
 Mantel and partial-Mantel correlations between utterance frequency differences and covariables, and between genetic ASD and the same covariables, in 225 genetically unrelated Cabo Verde-born Kriolu-speaking individuals.Table 1—source data 1.Mantel correlations among individual birth-places, residence-places, maternal and paternal birth places, age, and academic education duration.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="2">Genetic ASD - 1,899,978 SNPs</th>
      <th colspan="2">Utterance-frequency Euclidean distances - 4831 uttered items</th>
    </tr>
    <tr>
      <th>Mantel variable</th>
      <th>Partial-Mantel control</th>
      <th>n</th>
      <th>Geographic scale</th>
      <th>Spearman rho</th>
      <th>10,000 Mantel two-sided permutation p</th>
      <th>Spearman rho</th>
      <th>10,000 Mantel two-sided permutation p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>abs(Age difference)</td>
      <td>--</td>
      <td>225</td>
      <td>within and between islands</td>
      <td>0.1303</td>
      <td>&lt;2.10–4</td>
      <td>0.2215</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>abs(Age difference)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>225</td>
      <td>within and between islands</td>
      <td>0.1348</td>
      <td>&lt;2.10–4</td>
      <td>0.2294</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>--</td>
      <td>225</td>
      <td>within and between islands</td>
      <td>0.2916</td>
      <td>&lt;2.10–4</td>
      <td>0.2794</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>abs(Age difference)</td>
      <td>225</td>
      <td>within and between islands</td>
      <td>0.2935</td>
      <td>&lt;2.10–4</td>
      <td>0.2855</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>--</td>
      <td>186</td>
      <td>within and between islands</td>
      <td>0.0168</td>
      <td>0.2730</td>
      <td>0.0962</td>
      <td>0.0024</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>186</td>
      <td>within and between islands</td>
      <td>–0.0023</td>
      <td>0.4900</td>
      <td>0.0834</td>
      <td>0.0071</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>--</td>
      <td>185</td>
      <td>within and between islands</td>
      <td>0.0159</td>
      <td>0.2825</td>
      <td>0.1001</td>
      <td>0.0014</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>log(Residence dist.)</td>
      <td>185</td>
      <td>within and between islands</td>
      <td>–0.0041</td>
      <td>0.4651</td>
      <td>0.0824</td>
      <td>0.0068</td>
    </tr>
    <tr>
      <td>log(Residence dist.)</td>
      <td>--</td>
      <td>224</td>
      <td>within and between islands</td>
      <td>0.1658</td>
      <td>&lt;2.10–4</td>
      <td>0.2145</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Residence dist.)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>224</td>
      <td>within and between islands</td>
      <td>–0.0488</td>
      <td>0.0005</td>
      <td>0.0306</td>
      <td>0.0682</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>--</td>
      <td>224</td>
      <td>within and between islands</td>
      <td>0.2889</td>
      <td>&lt;2.10–4</td>
      <td>0.2800</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>log(Residence dist.)</td>
      <td>224</td>
      <td>within and between islands</td>
      <td>0.2445</td>
      <td>&lt;2.10–4</td>
      <td>0.1863</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Father Birth-loc. dist.)</td>
      <td>--</td>
      <td>222</td>
      <td>within and between islands</td>
      <td>0.2424</td>
      <td>&lt;2.10–4</td>
      <td>0.1704</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Father Birth-loc. dist.)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>222</td>
      <td>within and between islands</td>
      <td>0.0846</td>
      <td>0.0014</td>
      <td>0.0066</td>
      <td>0.3915</td>
    </tr>
    <tr>
      <td>log(Mother Birth-loc. dist.)</td>
      <td>--</td>
      <td>224</td>
      <td>within and between islands</td>
      <td>0.2619</td>
      <td>&lt;2.10–4</td>
      <td>0.2634</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Mother Birth-loc. dist.)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>224</td>
      <td>within and between islands</td>
      <td>0.0748</td>
      <td>0.0057</td>
      <td>0.0853</td>
      <td>0.0071</td>
    </tr>
    <tr>
      <td>abs(Age difference)</td>
      <td>--</td>
      <td>225</td>
      <td>within islands only</td>
      <td>0.2124</td>
      <td>0.0006</td>
      <td>0.2727</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>abs(Age difference)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>225</td>
      <td>within islands only</td>
      <td>0.1648</td>
      <td>0.0041</td>
      <td>0.2546</td>
      <td>&lt;2.10–4</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>--</td>
      <td>225</td>
      <td>within islands only</td>
      <td>0.3460</td>
      <td>&lt;2.10–4</td>
      <td>0.1412</td>
      <td>0.0401</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>abs(Age difference)</td>
      <td>225</td>
      <td>within islands only</td>
      <td>0.3212</td>
      <td>&lt;2.10–4</td>
      <td>0.0990</td>
      <td>0.1030</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>--</td>
      <td>186</td>
      <td>within islands only</td>
      <td>–0.0370</td>
      <td>0.3077</td>
      <td>0.1287</td>
      <td>0.0440</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>186</td>
      <td>within islands only</td>
      <td>–0.0537</td>
      <td>0.2330</td>
      <td>0.1239</td>
      <td>0.0496</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>--</td>
      <td>185</td>
      <td>within islands only</td>
      <td>–0.0382</td>
      <td>0.3037</td>
      <td>0.1421</td>
      <td>0.0292</td>
    </tr>
    <tr>
      <td>abs(Education duration difference)</td>
      <td>log(Residence dist.)</td>
      <td>185</td>
      <td>within islands only</td>
      <td>–0.0491</td>
      <td>0.2566</td>
      <td>0.1202</td>
      <td>0.0546</td>
    </tr>
    <tr>
      <td>log(Residence dist.)</td>
      <td>--</td>
      <td>224</td>
      <td>within islands only</td>
      <td>–0.0667</td>
      <td>0.1907</td>
      <td>0.0982</td>
      <td>0.0911</td>
    </tr>
    <tr>
      <td>log(Residence dist.)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>224</td>
      <td>within islands only</td>
      <td>–0.0549</td>
      <td>0.2319</td>
      <td>0.1063</td>
      <td>0.0704</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>--</td>
      <td>224</td>
      <td>within islands only</td>
      <td>0.3465</td>
      <td>&lt;2.10–4</td>
      <td>0.1537</td>
      <td>0.0282</td>
    </tr>
    <tr>
      <td>log(Birth-loc. dist.)</td>
      <td>log(Residence dist.)</td>
      <td>224</td>
      <td>within islands only</td>
      <td>0.3446</td>
      <td>&lt;2.10–4</td>
      <td>0.1589</td>
      <td>0.0230</td>
    </tr>
    <tr>
      <td>log(Father Birth-loc. dist.)</td>
      <td>--</td>
      <td>222</td>
      <td>within islands only</td>
      <td>0.2660</td>
      <td>0.0006</td>
      <td>0.0160</td>
      <td>0.4123</td>
    </tr>
    <tr>
      <td>log(Father Birth-loc. dist.)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>222</td>
      <td>within islands only</td>
      <td>0.2187</td>
      <td>0.0045</td>
      <td>–0.0111</td>
      <td>0.4546</td>
    </tr>
    <tr>
      <td>log(Mother Birth-loc. dist.)</td>
      <td>--</td>
      <td>224</td>
      <td>within islands only</td>
      <td>0.2240</td>
      <td>0.0034</td>
      <td>0.1283</td>
      <td>0.0423</td>
    </tr>
    <tr>
      <td>log(Mother Birth-loc. dist.)</td>
      <td>log(Birth-loc. dist.)</td>
      <td>224</td>
      <td>within islands only</td>
      <td>0.1563</td>
      <td>0.0303</td>
      <td>0.1000</td>
      <td>0.0925</td>
    </tr>
  </tbody>
</table>

The first ASD-MDS axis differentiates mainly individuals born on Brava and Fogo compared to Santiago (Figure 5A–B). The second axis mainly differentiates individuals from Santiago, Fogo, and Brava from all other islands, while the third axis differentiates individuals from Boa Vista, São Nicolau, Sal, and Maio from all other birth-islands. Furthermore, we find a significant positive correlation between ASD and actual individual birth-locations across Cabo Verde (Table 1; Spearman ρ=0.2916, two-sided Mantel p<2 × 10–4). This correlation increases when considering only within-islands pairwise comparisons and excluding all inter-island comparisons (Spearman ρ=0.3460, two-sided Mantel p<2 × 10–4), thus illustrating the strong signal of genetic isolation-by-distance (Rousset, 1997) within Cabo Verde at very reduced geographical scales.

Furthermore, the first utterance-MDS axis of pairwise inter-individual Euclidean distances between utterance frequencies mainly differentiates Santiago and Santo Antão/São Vicente-born individuals’ speech-varieties; all other Cabo Verdeans cluster intermediately (Figure 5C–D). The third axis further separates speech-varieties recorded in individuals from Fogo, Maio, and Brava. Analogously to genetic differentiation patterns, we find a positive correlation between differences in utterance frequencies and actual birth-places’ distances (Spearman ρ=0.2794, two-sided Mantel p<2 × 10–4), as well as paternal and maternal birth-places respectively (Table 1). However, unlike for to ASD, we find that utterance-frequencies differences stem from inter-birth-islands’ distances, rather than shorter distances within islands only. Extending previous results from Santiago only (Verdu et al., 2017), these results altogether show that speech-varieties are significantly transmitted from one generation to the next throughout Cabo Verde, anchored in individuals’ birth-places. Importantly, note, however, that this vertical transmission of manners of speaking Kriolu does not account for the majority of observed linguistic variation across individuals in our dataset. Indeed, we find that age-differences also substantially correlate with utterance-frequency differences even when correcting for individual birth-places (Spearman ρ=0.2294, two-sided partial-Mantel p<2 × 10–4). Finally, while we might intuitively expect that academic education influences idiolects, we find instead that differences in education-duration do not correlate with Kriolu utterance-frequencies differences, whether correcting for residence or birth-places distances, or not (Table 1). This shows the modest influence of academic education on Kriolu variation. Altogether, our results highlight strong genetic and linguistic isolation-by-distance patterns at reduced geographic distances within Cabo Verde.

Altogether, we find here genetic and linguistic isolation-by-distance anchored in inter-individual birth-places distances across, and sometimes within, Cabo Verdean islands. These results demonstrate the reduced dispersal of Cabo Verdeans at very local scales within the archipelago, both genetically and linguistically, a fundamental mobility-behavior mechanism likely explaining genetic and linguistic isolation across islands and sometimes even within islands despite the large self-reported exploration mobility of Cabo Verdeans.

### Geographic distribution of genetic and linguistic admixture within Cabo Verde

Based on these results of genetic and linguistic diversity isolation-by-distance patterns anchored in individual’s birth-places, we aim at investigating whether individual genetic and/or linguistic admixture levels also exhibit isolation-by-distance patterns across and within islands, beyond the qualitative observation that genetic and linguistic admixture patterns vary across different islands of Cabo Verde obtained above and in previous results (Verdu et al., 2017; Beleza et al., 2013). Interestingly, we find that absolute differences in inter-individual genetic admixture levels from Africa, estimated with ADMIXTURE or ASD-MDS, significantly correlate with actual birth-places distance across islands (Spearman ρ=0.1865, two-sided Mantel p<2 × 10–4 and ρ=0.1813, p<2 × 10–4, respectively), but not within-islands only (ρ=0.0342 p=0.3094 and ρ=0.0282 p=0.3385, respectively). This shows that two individuals born on far-away islands are likely to differ more in African genetic admixture levels, than two individuals born on close-by islands, a form of isolation-by-distance pattern for genetic admixture across Cabo Verdean islands.

We explored inter-individual variation in Kriolu utterance frequencies specifically for uttered items of clearly African and dual European-African origins (utterance categories A and B; see Material and Methods) providing an estimate of individual African linguistic-admixture scores (Verdu et al., 2017). We find that African linguistic-admixture score differences significantly correlate with actual birth-places’ distances throughout Cabo Verde (Spearman ρ=0.1297, two-sided Mantel p<2 × 10–4), and even marginally significantly correlate with birth-places’ distances at short distances within birth-islands (Spearman ρ=0.1209, two-sided Mantel p=0.0419).

Finally, we find a significant positive correlation (Spearman ρ=0.2070, p=0.0018) between genetic and linguistic admixture in Cabo Verde (Figure 5E), indicating that individuals who frequently use African-related utterances in their manner of speaking Kriolu are more likely to exhibit higher levels of African genetic-admixture. This correlation remains, respectively, marginally significant and significant when considering utterances of strictly African-origin (Category A) or utterances with a dual European-African etymology (Category B) separately (Spearman ρ=0.1631, p=0.0143, and ρ=0.1829, p=0.0059, respectively). These positive correlations between genetic and linguistic admixture generalize to the whole archipelago our previous results obtained in Santiago only (Verdu et al., 2017), and further suggest that genetic and linguistic admixture histories may have occurred in parallel all throughout Cabo Verde.

Therefore, not only we identify isolation-by-distance patterns within Cabo Verdean islands for genetic and linguistic diversities, but also identify a form of isolation-by-distance for genetic and linguistic admixture levels at very reduced geographical scales. This suggests that processes of reduced dispersal of individuals can also be identified in the genetic and linguistic admixture patterns, which has never been previously observed in human admixed populations to our knowledge, nor previously suspected whether genetically or linguistically in Cabo Verde (Micheletti et al., 2020; Quint, 2000; Baptista, 2015; Verdu et al., 2017; Lang, 2009; Beleza et al., 2012).

Together with the above LAI and ROH results, the various isolation-by-distance patterns here identified suggest that different founding events followed by local isolation due to reduced genetic and linguistic dispersal ranges, as well as different admixture histories, are at the root of patterns of genetic and linguistic diversity and admixture throughout Cabo Verde, anchored in individual birth places across islands, and even sometimes within islands.

### Genetic admixture histories in Cabo Verde inferred with MetHis-ABC

Highly complex admixture histories, with more than two separate pulses and/or periods of recurring admixture from each source population, are often impossible to infer from observed genetic data using maximum-likelihood approaches; whether the likelihood itself cannot be explicitly formulated or whether its maximization is computationally intractable for such high levels of complexity (Gravel, 2012; Hellenthal et al., 2014; Foll et al., 2015; Ni et al., 2019). Instead, Approximate Bayesian Computation allows, in principle, formal comparison of competing scenarios underlying the observed data and estimation of the posterior distribution of the parameters under the winning model (Tavaré et al., 1997; Beaumont et al., 2002). The user simulates numerous genetic datasets under competing scenarios, drawing randomly the parameter values of each simulation in prior distributions. ABC then allows to formally compare a set of summary statistics calculated on the observed data with the same set of summary statistics calculated on each simulated genetic dataset separately, in order to identify which of the competing scenarios produces simulations for which summary-statistics are closest to the observed ones. Under the winning scenario, ABC then estimates the joint posterior distribution of parameter values which produced simulations whose summary statistics most resemble the observed ones. Therefore, ABC allows, in principle, to infer arbitrarily complex demographic models underlying the data, provided that data can be efficiently simulated under these scenarios drawing randomly parameter values from prior distributions explicitly set by the user, and provided that calculated summary statistics are indeed informative about the scenarios’ parameters (Sisson et al., 2018).

We reconstruct the admixture histories of each Cabo Verde island separately using the MetHis-ABC framework (Fortes‐Lima et al., 2021; Pudlo et al., 2016; Csilléry et al., 2012). It was recently developed to investigate highly complex admixture histories using machine-learning ABC, by simulating independent autosomal SNPs forward-in-time in an admixed population under any two source-population versions of a general admixture model (Verdu and Rosenberg, 2011), and calculating, for each simulation, sets of summary statistics shown to be informative about the underlying admixture models’ parameters for ABC inferences (Fortes‐Lima et al., 2021). See Material and Methods and Appendix 1 for the detailed description of simulations and ABC machine-learning scenario-choice and posterior parameter estimation procedures.

#### MetHis–ABC prior checking

We considered four competing genetic-admixture scenarios described in Figure 6 and Table 2, tested separately for individuals born on each Cabo Verdean island and for the 225 Cabo Verde-born unrelated individuals grouped altogether, with MetHis–ABC machine-learning scenario-choice and posterior parameter inferences (Fortes‐Lima et al., 2021; Pudlo et al., 2016; Csilléry et al., 2012). ABC inferences are based on 42 summary statistics (Table 3), calculated for each simulation under each competing scenario separately using 60,000 independent autosomal SNPs in Cabo Verdean individuals, the African Mandinka and the European Iberian-IBS proxy source populations.

![Figure 6.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig6-v3.jpg)

**Figure 6.:** For all scenarios, the duration of the admixture process is set to 20 generations after the initial founding admixture event occurring at generation 0, which corresponds roughly to the initial peopling of Cabo Verde in the 1460s, considering 25 years per generation and sampled individuals born on average between the 1960s and 1980s. Scenario 1 Afr2Pulses-Eur2Pulses: after the initial founding pulse of admixture, the admixed population receives two separate introgression pulses from the African and European sources, respectively. Scenario 2 Afr2Pulses-EurRecurring: after the initial founding pulse of admixture, the admixed population receives two separate introgression pulses from the African source, and a period of monotonically constant or decreasing recurring introgression from the European source. Scenario 3 AfrRecurring-Eur2Pulses: after the initial founding pulse of admixture, the admixed population receives a period of monotonically constant or decreasing recurring introgression from the African source, and two separate introgression pulses from the European source. Scenario 4 AfrRecurring-EurRecurring: after the initial founding pulse of admixture, the admixed population receives a period of monotonically constant or decreasing recurring introgression from the African source, and, separately, a period of monotonically constant or decreasing recurring introgression from the European source. For all scenarios, we consider demographic models corresponding to either a constant reproductive population size Ng between the founding event and the present, or, instead, a linear or hyperbolic increase between N0 and N20, depending on the values of N0, N20, and uN used for each simulation respectively. Time for admixture pulses or time for the onset and offset of admixture periods are schematically represented as tSource,g. We define (Verdu and Rosenberg, 2011), sAfr,g, sEur,g, and hg as the proportion of parents of individuals in the admixed population at generation g coming from, respectively, the African source population, the European one, and the admixed population itself at the previous generation. Thus, for g=0, sAfr,0 + sEur,0 = 1, and for each value of g in [1,20], sAfr,g + sEur,g+ hg = 1. The number of ‘free’ scenario-parameters drawn randomly in prior distributions set by the user for simulations and subsequent Approximate Bayesian Computation inferences is indicated below the name of each scenario respectively. See Table 2 for parameter prior distributions, and Material and Methods for detailed descriptions of scenario-parameters.

**Table 2.**
 Prior distributions for the parameters of four competing scenarios for the admixture history of Cabo Verde islands.Parameters are presented in Figure 6 and described in Material and Methods.


<table>
  <thead>
    <tr>
      <th>Description</th>
      <th>Scenario</th>
      <th>Model parameter</th>
      <th>Prior</th>
      <th>Conditions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">African admixture-pulse times</td>
      <td rowspan="2">1, 2</td>
      <td>tAfr,p1</td>
      <td rowspan="2">Uniform [1 , 20] in discrete generations, a range corresponding to between ~1485 and~1960 in years CE</td>
      <td rowspan="2">tAfr,p1 &gt;tAfr,p2</td>
    </tr>
    <tr>
      <td>tAfr,p2</td>
    </tr>
    <tr>
      <td rowspan="2">European admixture-pulse times</td>
      <td rowspan="2">1, 3</td>
      <td>tEur,p1</td>
      <td rowspan="2">Uniform [1 , 20] in discrete generations, a range corresponding to between ~1485 and~1960 in years CE</td>
      <td rowspan="2">tEur,p1 &gt;tEur,p2</td>
    </tr>
    <tr>
      <td>tEur,p2</td>
    </tr>
    <tr>
      <td rowspan="2">African admixture period start and end times</td>
      <td rowspan="2">2, 4</td>
      <td>tAfr,t1</td>
      <td rowspan="2">Uniform [1 , 20] in discrete generations, a range corresponding to between ~1485 and~1960 in years CE</td>
      <td rowspan="2">tAfr,t1 &gt;tAfr,t2</td>
    </tr>
    <tr>
      <td>tAfr,t2</td>
    </tr>
    <tr>
      <td rowspan="2">European admixture period start and end times</td>
      <td rowspan="2">3, 4</td>
      <td>tEur,t1</td>
      <td rowspan="2">Uniform [1 , 20] in discrete generations, a range corresponding to between ~1485 and~1960 in years CE</td>
      <td rowspan="2">tEur,t1 &gt;tEur,t2</td>
    </tr>
    <tr>
      <td>tEur,t2</td>
    </tr>
    <tr>
      <td rowspan="2">African admixture-pulse intensities</td>
      <td rowspan="2">1, 2</td>
      <td>sAfr,tAfr,p1</td>
      <td rowspan="2">Uniform [0, 1]</td>
      <td rowspan="4">sAfr,g + sEur,g = 1 – hg, with hg in [0,1]</td>
    </tr>
    <tr>
      <td>sAfr,tAfr,p2</td>
    </tr>
    <tr>
      <td rowspan="2">European admixture-pulse intensities</td>
      <td rowspan="2">1, 3</td>
      <td>sEur,tEur,p1</td>
      <td rowspan="2">Uniform [0, 1]</td>
    </tr>
    <tr>
      <td>sEur,tEur,p2</td>
    </tr>
    <tr>
      <td rowspan="3">African admixture period intensity parameters</td>
      <td rowspan="3">2, 4</td>
      <td>sAfr,tAfr,t1</td>
      <td>Uniform [0, 1]</td>
      <td>sAfr,tAfr,t1 ≥sAfr,tAfr,t2</td>
    </tr>
    <tr>
      <td>sAfr,tAfr,t2</td>
      <td>Uniform [0, 1]</td>
      <td>sAfr,g + sEur,g = 1 – hg, with hg in [0,1]</td>
    </tr>
    <tr>
      <td>uAfr</td>
      <td>Uniform [0, 0.5]</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">European admixture period intensity parameters</td>
      <td rowspan="3">3, 4</td>
      <td>sEur,tEur,t1</td>
      <td>Uniform [0, 1]</td>
      <td>sEur,tEur,t1 ≥sEur,tEur,t2</td>
    </tr>
    <tr>
      <td>sEur,tEur,t2</td>
      <td>Uniform [0, 1]</td>
      <td>sAfr,g + sEur,g = 1 – hg, with hg in [0,1]</td>
    </tr>
    <tr>
      <td>uEur</td>
      <td>Uniform [0, 0.5]</td>
      <td></td>
    </tr>
    <tr>
      <td>Admixture pulse at the foundation</td>
      <td>1, 2, 3, 4</td>
      <td>sAfr,0</td>
      <td>Uniform [0, 1]</td>
      <td>sEur,0 = 1 – sAfr,0</td>
    </tr>
    <tr>
      <td>Founding reproductive population size</td>
      <td>1, 2, 3, 4</td>
      <td>N0</td>
      <td>Uniform [10, 1000]</td>
      <td>N0 ≤ N20</td>
    </tr>
    <tr>
      <td>Current reproductive population size</td>
      <td>1, 2, 3, 4</td>
      <td>N20</td>
      <td colspan="2">Uniform [100, 100,000]</td>
    </tr>
    <tr>
      <td>Steepness of the reproductive population size increase</td>
      <td>1, 2, 3, 4</td>
      <td>uN</td>
      <td colspan="2">Uniform [0, 0.5]</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Summary-statistics used for MetHis-machine-learning ABC inferences.All 42 statistics were computed using the summary-statistics computation tool embedded in MetHis (Fortes‐Lima et al., 2021).


<table>
  <thead>
    <tr>
      <th colspan="2">Summary Statistics for ABC inference</th>
      <th>Nunber of statistics</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>within population</td>
      <td>Mean ASD within population H</td>
      <td>1</td>
      <td>Bowcock et al., 1994</td>
    </tr>
    <tr>
      <td></td>
      <td>Mean Heterozygosity (SNP by SNP) within population H</td>
      <td>1</td>
      <td>Nei, 1978</td>
    </tr>
    <tr>
      <td></td>
      <td>Variance Heterozygosity (SNP by SNP) within population H</td>
      <td>1</td>
      <td>Nei, 1978</td>
    </tr>
    <tr>
      <td></td>
      <td>Mean inbreeding F within population H</td>
      <td>1</td>
      <td>Danecek et al., 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Variance inbreeding F within population H</td>
      <td>1</td>
      <td>Danecek et al., 2011</td>
    </tr>
    <tr>
      <td>admixture pattern</td>
      <td>Mode ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Mean ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Variance ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Skewness ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Kurtosis ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Min ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Max ASD-MDS African admixture proportions in population H</td>
      <td>1</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Deciles of ASD-MDS African admixture proportions in population H</td>
      <td>9</td>
      <td>Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011</td>
    </tr>
    <tr>
      <td></td>
      <td>Mode ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Mean ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Variance ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Skewness ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Kurtosis ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Min ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Max ASD-MDS ‘African-European angles’ in population H</td>
      <td>1</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td></td>
      <td>Deciles of ASD-MDS ‘African-European angles’ in population H</td>
      <td>9</td>
      <td>This study; Appendix 1—figure 2</td>
    </tr>
    <tr>
      <td>between populations</td>
      <td>Fst (African Source - Population H)</td>
      <td>1</td>
      <td>Weir and Cockerham, 1984</td>
    </tr>
    <tr>
      <td></td>
      <td>Fst (European Source - Population H)</td>
      <td>1</td>
      <td>Weir and Cockerham, 1984</td>
    </tr>
    <tr>
      <td></td>
      <td>Mean ASD (African Source - Population H)</td>
      <td>1</td>
      <td>Bowcock et al., 1994</td>
    </tr>
    <tr>
      <td></td>
      <td>Mean ASD (European Source - Population H)</td>
      <td>1</td>
      <td>Bowcock et al., 1994</td>
    </tr>
    <tr>
      <td></td>
      <td>f3 (Population H; European Source, African Source)</td>
      <td>1</td>
      <td>Patterson et al., 2012</td>
    </tr>
  </tbody>
</table>

Note that we did not explicitly simulate genotype data in the European and African source-populations. Instead, we built gamete reservoirs at each 21 generation of the forward-in-time admixture process, matching in frequency the observed allele frequencies at the 60,000 independent SNPs for the Iberian IBS and Mandinka populations, respectively. As in our previous MetHis-ABC investigation of the admixture history of the African-American ASW and Barbadian ACB populations (Fortes‐Lima et al., 2021), we therefore consider that the African and European proxy populations at the source of the admixture history of Cabo Verde are large and unaffected by mutation during the 21 generations of the admixture process; this assumption is reasonable provided that we consider only independent genotyped SNPs and the very recent demographic history of the archipelago, discovered un-inhabited and first settled in the 1460s. Therefore, although we cannot reconstruct the evolutionary history of the African and European source populations with our design, we nevertheless implicitly take the real demographic histories of these source populations into account in our simulations, as we use observed genetic patterns themselves, the product of this demographic history, to create the virtual source populations at the root of the admixture history of Cabo Verde.

We find that the summary-statistics calculated from the observed datasets fall well within the space of summary-statistics obtained from 10,000 simulated-datasets under each of the four competing scenarios (Appendix 1—figure 3, Appendix 1—figure 3—figure supplements 1–10), considering non-significant (α>5%) goodness-of-fit, visual inspection of summary-statistics PCA-projections, and each summary-statistic’s distribution, for each Cabo Verdean birth-island and for all Cabo Verde-born individuals grouped in a single population, separately. Prior-checks thus demonstrate that MetHis simulations are appropriate for further ABC scenario-choice and posterior parameter inferences using observed data in the African Mandinka and the European Iberian IBS source populations and each Cabo Verde islands separately or grouped altogether, as they allow to mimic the observed summary-statistics, despite the assumption that the European and African proxy source populations are at the drift-mutation equilibrium over the last 21 generations.

#### MetHis–Random Forest (RF)-ABC scenario-choices

Overall (Figure 7B), MetHis-RF-ABC scenario-choices indicate that multiple pulses of admixture from the European and African source populations (after the founding admixture pulse, two independent admixture pulses from both Africa and Europe: ‘Afr2Pulses-Eur2Pulses’ scenarios, Figure 6 – Scenario 1), best explain the genetic history of individuals born on six of nine Cabo Verdean islands. Furthermore, we find that even more complex scenarios involving a period of recurring admixture from either source best explain the history of the remaining three islands. Scenarios with periods of recurring admixture from both Africa and Europe (‘AfrRecurring-EurRecurring’, Figure 6 – Scenario 4) are the least favored across Cabo Verde.

![Figure 7.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig7-v3.jpg)

**Figure 7.:** Elements of the peopling-history of Cabo Verde islands are synthesized in Figure 7—source data 1, stemming from historical work cited therein. Islands are ordered from top to bottom in the chronological order of the first historical census perennially above 100 individuals within an island, indicated with the purple vertical lines. First historical records of the administrative, political, and religious, settlement of an island, are indicated with the red vertical lines. (A) Within-island birth-places of 225 Cabo-Verde-born individuals. (B) MetHis-Random Forest-ABC scenario-choice vote results for each island separately in histogram format. Posterior probabilities of correctly identifying a scenario if correct are indicated for the winning scenario as ‘Post. prob. Scen.’, above each histogram. (C) MetHis-Neural Network-ABC posterior parameter distributions with 50% Credibility Intervals for the reproductive population size history of each birth-island separately. (D) Synthesis of MetHis-NN-ABC posterior parameter median point-estimates and associated 50% CI, for the admixture history of each island under the winning scenario identified with RF-ABC in panel B. European admixture history appears in blue, African admixture history in orange. Horizontal bars indicate 50% CI for the admixture time parameters, vertical arrows correspond to median admixture intensity estimates with 50% CI in doted lines. For (C) and (D), posterior parameter distributions showing limited departure from their respective priors and large CI are greyed, as they were largely unidentifiable in our ABC procedures. Detailed parameter posterior distributions, 95% CI, and cross-validation errors are provided in Figure 7—figure supplements 1–3 and Appendix 5—Tables 1–9. Detailed results description for each island are provided in Appendix 5. (C–D) The period between the 1630s and the abolition of the TAST in the 1810s, when most enslaved-Africans were deported from Africa by European empires concomitantly to the expansion of the plantation economy (Eltis and Richardson, 2015; Fortes-Lima and Verdu, 2021), is indicated in light-pink. The period between the abolition of the TAST in the 1810s and the abolition of slavery enacted between 1856 and 1878 throughout the Portuguese empire is indicated in light-green (Carreira, 2000). The independence of Cabo Verde occurred in 1975.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** We considered, for each island separately, and for all 225 Cabo Verde-born individuals grouped in a single random mating population separately, Neural Network tolerance levels and number of neurons in the hidden layer, for each island and for Cabo Verde as a whole, separately, are chosen based on posterior parameter cross-validation error minimization procedures conducted on 1000 random simulations used in-turn, as pseudo observed data (see Appendix 1, and Appendix 1—table 1). For each island and for Cabo Verde as a whole, separately, posterior parameter distributions correspond to the solid lines and corresponding priors correspond to the doted black lines. Density distributions are based on the logit transformation of parameter values (see Appendix 1) using an Epanechnikov kernel between the corresponding prior bounds. See Results, Discussion, and Appendix 5 for descriptions and discussions of the results. Synthesis in Figure 7.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig7-figsupp2-v3.jpg)

**Figure 7—figure supplement 2.:** We considered, for each island separately, and for all 225 Cabo Verde-born individuals grouped in a single random mating population separately, Neural Network tolerance levels and number of neurons in the hidden layer, for each island and for Cabo Verde as a whole, separately, are chosen based on posterior parameter cross-validation error minimization procedures conducted on 1000 random simulations used in-turn, as pseudo observed data (see Appendix 1, and Appendix 1—table 1). For each island and for Cabo Verde as a whole, separately, posterior parameter distributions correspond to the solid lines and corresponding priors correspond to the doted black lines. Density distributions are based on the logit transformation of parameter values (see Appendix 1) using an Epanechnikov kernel between the corresponding prior bounds. See Results, Discussion, and Appendix 5 for descriptions and discussions of the results. Synthesis in Figure 7.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/79827/elife-79827-fig7-figsupp3-v3.jpg)

**Figure 7—figure supplement 3.:** We considered, for each island separately, and for all 225 Cabo Verde-born individuals grouped in a single random mating population separately, 100,000 simulations computed under the winning scenario obtained with RF-ABC scenario-choice procedures and provided on the left of the figure. Neural Network tolerance levels and number of neurons in the hidden layer, for each island and for Cabo Verde as a whole, separately, are chosen based on posterior parameter cross-validation error minimization procedures conducted on 1000 random simulations used in-turn, as pseudo observed data (see Appendix 1, and Appendix 1—table 1). For each island and for Cabo Verde as a whole, posterior parameter distributions correspond to the solid lines and corresponding priors correspond to the doted black lines. Density distributions are based on the logit transformation of parameter values (see Appendix 1) using an Epanechnikov kernel between the corresponding prior bounds. See Results, Discussion, and Appendix 5 for descriptions and discussions of the results. Synthesis in Figure 7.

RF-ABC cross-validation prior-errors for each of the 40,000 simulations used, in-turn, as pseudo-observed data indicate a reasonably good, albeit not perfect, discriminatory power of the RF (Appendix 1—figure 4A). RF-ABC scenario-choices identify the correct scenario in the majority of cross-validations for most scenarios and most islands. Furthermore, asymmetrical scenarios are the least confused with one-another (AfrRecurring-Eur2Pulses vs Afr2Pulses-EurRecurring, or Afr2Pulses-Eur2Pulses vs AfrRecurring-EurRecurring). As expected and previously shown empirically with MetHis-RF-ABC scenario-choice (Fortes‐Lima et al., 2021; Robert et al., 2010), these results are consistent with increased assignation-errors in the parts of the parameter-space where the different scenarios are highly nested and thus biologically equivalent. Finally (Appendix 1—figure 4B), the mean, variance, skewness, kurtosis, minimum, and maximum of individual admixture proportions’ distributions are systematically among the most informative summary-statistics for RF-ABC scenario-choice in every island or in Cabo Verde as a whole, consistently with theoretical expectations (Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011).

Finally, when considering all Cabo Verde-born individuals as a single random-mating population without distinguishing birth-islands, our MetHis-RF-ABC scenario-choice identifies the Afr2Pulses-Eur2Pulses scenario as the winning scenario (Appendix 1—figure 4B), thus consistent with the scenario most often found as the winner among Cabo Verde islands considered as the target admixed population in nine separate MetHis-RF-ABC analyses.

#### MetHis–Neural Network (NN)-ABC posterior parameter estimations

For individuals on each Cabo Verdean birth island separately, we performed NN-ABC joint posterior parameter estimation based on 100,000 MetHis simulations under the winning scenario (Fortes‐Lima et al., 2021): Afr2Pulses-Eur2Pulses in Santiago, Fogo, Santo Antão São Nicolau, Brava, and Maio; Afr2Pulses-EurRecurring in Boa Vista and Sal; and AfrRecurring-Eur2Pulses in São Vicente (Figure 7B). For each island separately, detailed posterior parameters’ distributions, Credibility Intervals (CI), and cross-validation errors are provided in Figure 7—figure supplements 1–3 and Appendix 5—Tables 1–10. We synthesized our results considering median point-estimates and 50% CI for each scenario parameter in the admixture history of each island in Figure 7C–D. We detailed our results and discussion for admixture history inferences for each island separately in Appendix 5, in the light of historical data about the peopling of Cabo Verde (Figure 7—source data 1).

Figure 7C shows that the reproductive population size of Cabo Verde islands remained very low until a strong increase in the last three generations for all islands but Santiago and Brava. In Santiago the population expansion was more linear since the founding of Cabo Verde in the 1460s, while the reproductive size of Brava remained almost constant and low until today.

In summary, Figure 7D shows that European and African admixture events throughout the archipelago occurred first during the early peopling history of each island, before the mid-17th century massive expansion of the TAST due to the expansion of the plantation economy (Eltis and Richardson, 2015). We find that other admixture events from Europe or Africa, or both, likely occurred much later during, or immediately after, the 19th century abolition of the TAST and of slavery in European colonial empires. Altogether our MetHis-ABC results support limited historical admixture having occurred in Cabo Verde during the most intense periods of the TAST between the mid-17th and early 19th centuries. Furthermore, note that we find admixture events often earlier than, or concomitant with, the first perennial peopling of an island. For the islands of Santiago, Fogo, Santo Antão and, to a lesser extent, São Nicolau, initial historical admixture events occurred synchronously to the first perennial settlement of the island. For the islands of Brava, Maio, Boa Vista, and São Vicente, early admixture events occurred long before their first perennial peopling, thus showing that their founding was already largely composed of already admixed individuals. Importantly, note that our MetHis-NN-ABC posterior parameter inferences cannot infer all scenario-parameters accurately, as some parameters hardly depart from their respective priors (Figure 7—figure supplements 1–3), and the admixture history of the island of Sal remains overall poorly inferred.

Interestingly, MetHis-NN-ABC posterior parameter inference results obtained for the 225 Cabo Verde-born individuals grouped in a single random-mating population instead of separately for each island of birth, are largely undifferentiated from their prior distributions, and have very wide CI and large cross-validation errors, for all admixture-history parameters except for the two parameters associated with the most recent pulse of admixture from the African source (Figure 7—figure supplements 1–3; Appendix 5—table 10). This contrasts with the substantial number of informative posterior-parameter estimations obtained for all islands of birth separately except Sal (Figure 7, Figure 7—figure supplements 1–3; Appendix 5—tables 1–9), despite the much smaller sample sizes used in each one of these separate analyses compared to the analysis considering Cabo Verde as a single population. These results further show that the history of admixture substantially differs across Cabo Verde islands and that considering the Cabo Verde archipelago as a single random mating population is inadequate to successfully infer the parameters of its admixture history, consistently with our results from ADMIXTURE, LAI, ROH, and Isolation-By-Distance analyses.

## Discussion

### Which African and European populations contributed genetically to Cabo Verde?

#### The genetic heritage of continental Africa in Cabo Verde

Numerous enslaved-African populations from Western, Central, and South-Western Central Africa were forcibly deported during the TAST to both Cabo Verde and the Americas, as shown by historical demographic records (Eltis and Richardson, 2015; Carreira, 2000). There is still extensive debate about whether enslaved-Africans remained or more briefly transited in Cabo Verde during the most intense period of the TAST, in the 18th and 19th centuries, when the archipelago served as a slave-trade platform between continents (Carreira, 2000; Patterson, 1988; Brooks, 2006); the question of the duration of stay of enslaved individuals at a given location being also of major interest throughout the Americas during the TAST (Eltis, 2002; Berlin, 2010). In this context, previous genetic studies considering a relatively limited number of populations from mainland Europe and Africa, and/or limited numbers of Cabo Verdean islands of birth, suggested that mainly continental West Africans and South Europeans were at the root of Cabo Verde genetic landscape (Micheletti et al., 2020; Verdu et al., 2017; Beleza et al., 2013).

In this context, our genetic results favor scenarios where mostly certain West Western African Senegambian populations only (Mandinka and Wolof in our study) contribute to the genetic makeup of Cabo Verde (Figures 2–3). Other Western, Central, and South-Western African populations historically also forcibly deported during the TAST seem to have had very limited contributions to the genomic diversity of most Cabo Verde islands, and virtually no contribution to that of Brava, Fogo, and Santiago.

This could be due to Cabo Verde being only a temporarily waypoint for these latter enslaved-African populations between Africa, the Americas, and Europe, but would also be consistent with additional socio-historical processes (see below). Interestingly, and further echoing these genetic results, the Cabo Verdean Kriolu language carries specific signatures mainly from the Mande language-family, and Wolof and Temne languages from Western Africa, and largely more limited signatures of Kikongo and Kimbundu Bantu languages from Central and South-Western Africa (Quint, 2000; Lang, 2009).

These results contrast with the admixture patterns identified in other enslaved-African descendant populations in the Americas in our dataset (African-American and Barbadian, Figures 2–3), and in previous studies (Micheletti et al., 2020; Ongaro et al., 2019; Mathias et al., 2016; Gouveia et al., 2020; Martin et al., 2017). Indeed, the origins of African ancestries in numerous populations throughout the Caribbean and the Americas traced to varied continental African regions, from Western to South-Western Africa, thus qualitatively consistent with the known diversity of slave-trade routes used between continents and within the Americas after the Middle Passage.

#### The genetic heritage of continental Europe in Cabo Verde

After the initial settlement of Cabo Verde by Portuguese migrants, temporary changes of European dominion in certain islands, newly developing commercial opportunities, and intense piracy during the 16th and 17th centuries have triggered different European populations to migrate to the archipelago (Albuquerque and Santos, 1991; Albuquerque and Santos, 1995; Soares, 2011).

Nevertheless, these latter historical events do not seem to have left a major signature in the genetic landscape of Cabo Verde (Figures 2–3). Instead, we find that Cabo Verdean-born individuals in our dataset share virtually all their European genetic ancestry with Iberian populations, with extremely limited evidence of contributions from other European regions, consistent with previous studies (Micheletti et al., 2020; Verdu et al., 2017). Interestingly, the reduced diversity of European populations’ contributions to the genomic landscape of Cabo Verde is also identified in other enslaved-African descendant populations in our study, as well as in previous studies in Caribbean and American populations (Moreno-Estrada et al., 2013; Baharian et al., 2016; Gouveia et al., 2020). Our results thus show that European admixture in enslaved-African descendant populations on both sides of the Atlantic, as represented here by Cabo Verde, the Barbadians ACB and the African American ASW, mainly stem from the gene-pool of the European empires historically and socio-economically dominant locally, rather than subsequent European migrations (Fortes-Lima and Verdu, 2021).

Altogether, note that, in our local-ancestry inferences, we considered as reference source populations varied existing populations from continental mainland Africa and Europe, categorized as such from sampling information and geographic location only, prior to any genetic investigation. Therefore, in these analyses, we cannot disentangle the fraction of European admixture in Cabo Verdean genomes stemming directly from European migrations after the 1460s, from the fraction stemming from the European genetic legacy in continental African source populations acquired whether during more ancient migrations which occurred before the peopling of Cabo Verde (e.g. Busby et al., 2016), or since then during the European colonial expansion in Sub-Saharan Africa. Symmetrically, we cannot disentangle the fraction of African admixture in Cabo Verde stemming directly from continental Africa after the 1460s, from the fraction inherited from Africa-Europe admixture events that may have occurred in Europe prior to the peopling of Cabo Verde or during the colonial era until today. Disentangling both genetic heritages will require, in future studies, the explicit modelling of such possible admixture histories within African and European ancestral populations at the source of the Cabo Verde genetic landscape, and would also benefit from including data from North-African populations in our reference panels.

### Genetic and linguistic isolation-by-distance and recent demographic expansion in Cabo Verde

A scenario of island peopling via a series of founding events followed by slow-growing population sizes and local isolation due to reduced genetic and linguistic parent-offspring dispersal would consistently explain the increasing differentiation of island-specific patterns with increasing values of K found with ADMIXTURE, ASD-MDS, and isolation-by-distance results (Figures 2—5, Table 1), as well as MetHis-ABC demographic inferences (Figure 7C).

Indeed, MetHis-ABC results (Figure 7C) show the long period of small relatively constant reproductive sizes until the very recent strong, hyperbolic, increases in most Cabo Verdean islands; with the notable exceptions of, (i) the linear increase in Santiago, the political and commercial center of Cabo Verde throughout the colonial history of the archipelago, and (ii) the relatively constant reduced reproductive sizes in Brava until today. Altogether, this result was expected as the dry Sahelian climate of Cabo Verde with scarcely accessible water resources, recurring famines and epidemic outbreaks, and the Portuguese crown maintaining a strong control over population movements within Cabo Verde, rendered difficult the perennial peopling of most islands (see Figure 7—source data 1 and references therein, Appendix 5). Furthermore, such demographic scenarios are also consistent with long-ROH patterns reflecting isolation on each Cabo Verdean islands, whereas elevated shorter ancestry-specific ROH patterns likely stemmed from admixture (Figure 4), similarly to our results in the ASW and ACB populations and as previously identified (Szpiech et al., 2019). Note, however, that while we explored and found, a posteriori, a different demographic regime for each Cabo Verde island separately, with constant, hyperbolic, or linear increases of reproductive sizes, we did not consider possible demographic bottlenecks which may also have occurred as a result of the difficult settlement history of Cabo Verde described above. Such possible bottleneck events will need to be explored in the future, a particularly challenging task given the extensive number of competing models to be considered and given that bottleneck intensities and duration parameters have to be co-estimated with admixture parameters over a very short history of 21 generations.

Investigating isolation-by-distance anchored in individual birth-places at a very reduced geographical scale (Rousset, 1997; Barbujani, 1987; Malécot, 1975) within a population and a language allowed us to reveal that effective dispersal from one generation to the next across Cabo Verde islands, and sometimes even within-islands, was surprisingly reduced compared to the large mobility self-reported by participants (Figure 5, Table 1). Patterns of parent-offspring dispersal at a very local scale ~50 km within populations has seldom been tested using genetics, to our knowledge, in human populations (Rousset, 1997; Barbujani and Sokal, 1991; Cavalli-Sforza and Moroni, 2004; Verdu et al., 2010), although isolation-by-distance genetic patterns have been extensively explored to investigate serial founding events and migrations across human populations at varied geographical scales, including in archipelagos contexts (Creanza et al., 2015; Arauna et al., 2022; Hunley et al., 2008; Ramachandran et al., 2005). Furthermore, while the geographic distribution of genetic admixture patterns have been explored at much larger geographical scales (e.g. Arauna et al., 2022; Bradburd et al., 2016; Gnecchi-Ruscone et al., 2017), and in particular in enslaved-African descendant populations (Moreno-Estrada et al., 2013; Baharian et al., 2016), isolation-by-distance patterns for inter-individual differences of genetic admixture fractions at very reduced geographical scales have never been reported to our knowledge.

We also found substantial signals of isolation-by-distance among Kriolu idiolects (i.e. individual manners of uttering Cabo Verdean Kriolu), also anchored in individual birth-places (Figure 5, Table 1), thus showing striking parallels between the history of biological and cultural dispersal and isolation in Cabo Verde at a micro-geographical scale. Our results show that linguistic admixture patterns were isolated-by-distance within the archipelago, similarly to genetic admixture patterns, which was previously unsuspected in both genetics and linguistic studies of Cabo Verde (Quint, 2000; Verdu et al., 2017; Baptista, 2003; Beleza et al., 2013).

Altogether, these joint genetic-linguistic patterns highlight the limited effective genetic and linguistic dispersal from one generation to the next within Cabo Verde, including for genetic and linguistic admixture levels, despite extended mobility of individuals within the archipelago. Both mechanisms may thus underline individual linguistic identity construction processes and the genetic relative isolation across and within Cabo Verdean islands.

Importantly, we considered only random mating processes in our inferences and interpretations. However, the almost complete lack of identifiability of the admixture-history parameters obtained when considering Cabo Verde as a single random-mating population in our ABC inferences (Figure 7—figure supplements 1–3, Appendix 5—Tables 1–9), and our ROH results together with recent work (Korunes et al., 2022), altogether suggest that non-random matting processes significantly influenced Cabo Verdean genetic patterns. Therefore, future studies will need to evaluate how possible deviations from random-mating in Cabo Verde, such as assortative mating (Korunes et al., 2022; Zaitlen et al., 2017), may have influenced our results and interpretations. Note that this is a conceptually particularly challenging task in a small census-size population with strong marital stratification where mate-choices have been, by definition, limited during most of the TAST (Versluys et al., 2021). Nevertheless, such complex processes may also underlie the joint genetic-linguistic isolation-by-distance patterns anchored in birth-place distances here observed for both diversity and admixture patterns; and would also explain that genetic and linguistic histories of admixture apparently occurred in parallel in Cabo Verde.

### Histories of genetic admixture in Cabo Verde

#### Early admixture in Cabo Verde, limited admixture during the plantation economy era

While we expected recurring African admixture processes due to the known history of regular forced migrations from Africa during most of Cabo Verde history (Carreira, 2000), our MetHis–ABC scenario-choices indicate that, qualitatively, these demographic migrations did not necessarily translate into clearly recurring gene-flow processes to shape genetic patterns in most of Cabo Verde islands (Figure 7B). Indeed, African admixture processes in all islands, except São Vicente, seem to have occurred during much more punctual periods of Cabo Verdean history. Our MetHis–ABC posterior parameter estimations further highlighted often largely differing admixture histories across Cabo Verde islands (Figure 7C–D and Appendix 5).

We find that admixture from continental Europe and Africa occurred first early during the TAST history, concomitantly with the successive settlement of each Cabo Verdean island between the 15th and the early 17th centuries (Figure 7D). Furthermore, we find that the most intense period of enslaved-African deportations during the TAST via Cabo Verde, between the mid-17th and early-19th centuries during the expansion of the plantation economic system in the Americas and Africa (Eltis and Richardson, 2015; Carreira, 2000; Albuquerque and Santos, 1991; Albuquerque and Santos, 1995), seem to have left a limited signature in the admixture patterns of most Cabo Verdean islands today. Interestingly, previous studies also highlighted that admixture in enslaved-African descendants in the Caribbean may have occurred first early in the European colonial expansion in the region in the 16th century, and then much later towards the end of the TAST at the end of the 18th century, and had thus been relatively limited during most of the plantation economy era (Moreno-Estrada et al., 2013; Fortes-Lima et al., 2018). Together with our results, this illustrates the apparent discrepancy between intense demographic forced migrations during the TAST and genetic admixture signatures at least in certain populations on both sides of the Atlantic. Indeed, in contrast with these results, numerous other enslaved-African populations in the Americas have, instead, shown substantial historical admixture inferred to have occurred during the plantation economy era, hence exemplifying the diversity of admixture histories experienced locally by enslaved-Africans descendant populations during the TAST (Ongaro et al., 2019; Baharian et al., 2016).

The inferred lack of admixture events in Cabo Verde during the height of the TAST could be due to newly deported enslaved-Africans being only transiting via Cabo Verde before being massively re-deported to other European colonies during this era (Carreira, 2000; Patterson, 1988; Brooks, 2006). Furthermore, and not mutually exclusive with this latter hypothesis, historians reported, in Cabo Verde and other European colonies in the Americas, that relationships between enslaved and non-enslaved communities largely changed with the expansion of plantation economy at the end of the 17th century. These changes are often referred to as the shift from Societies-with-Slaves to Slave-Societies (Eltis and Richardson, 2015; Berlin, 2009; Chaudenson, 2001). Slave-Societies legally enforced the socio-marital and economic segregation between communities, and coercively controlled relationships between new enslaved-African migrants and pre-existing enslaved-African descendant communities more systematically and violently than Societies-with-Slaves (Berlin, 2009)p.15-46,95-108,(Carreira, 2000)p.281-319. The high prevalence of segregation during the height of the plantation economy could have limited genetic admixture between enslaved-African descendants and non-enslaved communities of European origin, as well as admixture between new migrants, forced or voluntary, and pre-existing Cabo Verdeans; notwithstanding the known history of dramatic sexual abuses during and before this era. This could consistently explain our observations of a relative lack of diverse African or European origins in Cabo Verdean genomes despite the known geographical diversity of populations deported and emigrated to the archipelago throughout the TAST. Furthermore, with legally enforced segregation, we might expect more marital pairings than before to occur among individuals with common origins; i.e. between two individuals with the same continental African or European origin. Such ancestry-specific marriages triggered by socio-cultural segregation would be consistent with our ROH patterns (Figure 4), also depending on how long such mate-choice behaviors persisted after the end of legal segregation. We note, however, that we have not formally tested this influence on ROH and ancestry patterns and that a careful consideration of alternate explanations, such as temporally varying admixture contributions over time or a severe bottleneck in one of the ancestral populations, would be important to consider in such future analyses.

In this context, the diversified African ancestries here found in the Americas (Figures 2–3), consistently with previous studies showing admixture events occurring before or during the height of plantation economy in the Americas (Micheletti et al., 2020; Ongaro et al., 2019; Baharian et al., 2016), would suggest that the gene-pool of enslaved-Africans communities admixing with Europeans in the Americas since the 16th century often involved, at a local scale, multiple African source populations, thus reflecting the multiple slave-trade routes between continents and within the Americas. Conversely in Cabo Verde, the early onset of the TAST during the 15th century likely privileged commercial routes with nearby Senegambia (Carreira, 2000)p.31-54,281-319, thus favoring almost exclusively admixture events with individuals from this region and from certain populations only. Altogether, our results in Cabo Verde contrasting with certain other enslaved-African descendant populations in the Americas, highlight the importance of early admixture processes and socio-cultural constraints changes on intermarriages throughout the TAST, which likely durably influenced genomic diversities in descendant populations locally, on both sides of the Atlantic.

#### Admixture in Cabo Verde after the abolition of the TAST and of Slavery

Finally, we find that recent European and African admixture in Cabo Verde occurred mainly during the complex historical transition after the abolition of the TAST in European colonial empires in the 1800s and the subsequent abolition of slavery between the 1830s and the 1870s (Figure 7D). Historians have shown that these major historical shifts strongly disrupted pre-existing segregation systems between enslaved and non-enslaved communities (Eltis and Richardson, 2015)-p.271-290, (Carreira, 2000)-p.335-362, (Cooper et al., 2000). In addition, an illegal slave-trade flourished during this era, bringing numerous enslaved-Africans to Cabo Verde outside of the official routes (Carreira, 2000)-p.363-384 (Conrad, 1969). Altogether, our results indicate increased signals of European and African admixture events in almost every island of Cabo Verde during this period, and were thus consistent with a change of the social constraints regarding admixture and forced displacements of enslaved-descendants that had prevailed over the preceding 200 years of the TAST. These results were largely consistent with previous studies elsewhere in the Caribbean (Moreno-Estrada et al., 2013; Fortes-Lima et al., 2018), and Central and South America (Ongaro et al., 2019; Gouveia et al., 2020); showing, at a local scale, the major influence of this recent and global socio-historical change in inter-community relationships in European colonial empires on either sides of the ocean.

### Perspectives

Altogether, our results highlight both the unity and diversity of the genetic peopling and admixture histories of Cabo Verde islands, the first colony peopled by Europeans in Sub-Saharan Africa, resulting from the sociocultural and historical complexity of the Trans-Atlantic Slave Trade and European colonial expansions since the 15th century. Our results obtained at a micro-geographical scale reveal the fundamental importance of the early TAST history, before the expansion of the plantation economy, in durably shaping the genomic and cultural diversities of enslaved-African descendant populations in both Africa and the Americas.

Importantly, we considered only the genome-wide autosomal admixture history of Cabo Verde in this study, and therefore did not explore possible sex-biased admixture processes. However, previous studies demonstrated the strong sex-biased admixture processes involved in Cabo Verde using sex-specific genetic markers (Gonçalves et al., 2003; Beleza et al., 2012), similarly as in other enslaved-African descendant populations in the Americas (Fortes-Lima and Verdu, 2021). Furthermore, previous theoretical work considering sex-specific mechanistic admixture models showed that sex-biased admixture processes may possibly bias historical inferences based only on autosomal data (Goldberg et al., 2014). It will thus be important, in future studies, to explore how this sex-biased admixture history may have influenced the ABC inferences here conducted; for instance, via sex-specific developments of MetHis-ABC.

Future work will need to formally test the serial-founder hypothesis here proposed to be at the root of the observed genetic and linguistic patterns within Cabo Verde, and thus compare the numerous possible routes for such a peopling history across islands within the archipelago. In particular, it will be of interest to investigate, then, the series of bottlenecks concomitant to each genetic and linguistic founding event; a much needed but challenging task considering the very recent history of the archipelago founded only 21 generations ago, and the historically-known small census sizes echoed in the relatively small reproductive sizes here identified in almost every island until the 20th century.

Our novel results together with their methodological limitations massively beg for future work further complexifying the admixture models here considered, as well as incorporating other summary-statistics such as admixture-LD and sex-specific statistics. This will allow to further dissect the admixture processes that gave birth to enslaved-African descendant populations, on both sides of the Atlantic.

## Materials and methods

### Cabo Verde genetic and linguistic datasets

We conducted joint sampling of anthropological, genetic, and linguistic data in Cabo Verde with the only inclusion criteria that volunteer-participants be healthy adults with Cabo Verdean citizenship and self-reporting speaking Kriolu (Verdu et al., 2017). Between 2010 and 2018, six interdisciplinary sampling-trips were conducted to interview 261 participants from more than thirty interview-locations throughout the archipelago (Figure 1).

#### Familial anthropology and geography data

The 261 Cabo Verdean individuals were each interviewed to record a classical familial anthropology questionnaire on self-reported life-history mobility. In particular, we recorded primary residence location, birth location, parental and grand-parental birth and residence locations, and history of islands visited in Cabo Verde and foreign experiences (Verdu et al., 2017). Furthermore, we also recorded age, sex, marital status, and cumulative years of schooling and higher education (for 211 individuals only), and languages known and their contexts of use.

GPS coordinates for each reported location were acquired on site during field-work, supplemented by paper maps and Google Earth for non-Caboverdean locations and islands that we did not visit (Sal and Maio). While participants’ birth-locations were often precise, increasing levels of uncertainty arose for the reported parental and grand-parental locations. We arbitrarily assigned the GPS coordinates of the main population center of an island when only the island of birth or residence could be assessed with some certainty by participants. All other uncertain locations where recorded as missing data. Figure maps were designed with the software QuantumGIS v3.10 ‘București’ and using Natural Earth free vector and raster map data (https://www.naturalearthdata.com).

#### Genome-wide genotyping data

The 261 participants each provided 2 mL saliva samples collected with DNAGenotek OG-250 kits, and complete DNA was extracted following manufacturer’s recommendations. DNA samples were genotyped using an Illumina HumanOmni2.5Million-BeadChip genotyping array following manufacturer’s instructions. We followed the quality-control procedures for genotypic data curation using Illumina’s GenomeStudio Genotyping Module v2.0 described in Verdu et al., 2017. Genotype-calling, population-level quality-controls, and merging procedures are detailed in Appendix 1—figure 1.

In summary, we extracted a preliminary dataset of 259 Cabo Verdean Kriolu-speaking individuals, including relatives, genotyped at 2,118,835 polymorphic di-allelic autosomal SNPs genome-wide. We then merged this dataset with 2504 worldwide samples from the 1000 Genomes Project Phase 3 Auton et al., 2015; with 1307 continental African samples from the African Genome Variation Project (Gurdasani et al., 2015; Network et al., 2019) (EGA accession number EGAD00001000959); and with 1235 African samples (Patin et al., 2017; Perry et al., 2014) (EGA accession number EGAS00001002078). We retained only autosomal SNPs common to all data sets, and excluded one individual for each pair of individuals related at the 2nd degree (at least one grand-parent in common) as inferred with KING (Manichaikul et al., 2010), following previous procedures (Verdu et al., 2017).

After merging all datasets (Appendix 1—figure 1), we considered a final working-dataset of 5157 worldwide unrelated samples, including 233 unrelated Cabo Verdean Kriolu-speaking individuals, of which 225 were Cabo-Verde-born, genotyped at 455,705 autosomal bi-allelic SNPs (Figure 1; Figure 1—source data 1). Note that, for this working-dataset, the fraction of missing genotypes was very low and equaled 7.0 × 10–4 on average within Cabo Verdean islands of birth (SD = 3.0 × 10–4 across islands).

#### Individual utterances of Kriolu

We collected linguistic data for each of the 261 Cabo Verdean individuals using anthropological linguistics questionnaires, and semi-directed interviews. Each participant was shown a brief (~6 min) speech-less movie, ‘The Pear Story’ (Chafe, 1980), after which they were asked to narrate the story as they wanted in ‘the Kriolu they speak every day at home’. Discourses were fully recorded without interruption, whether individuals’ discourses were related to the movie or not. Then each discourse was separately fully transcribed using the orthographic convention of the Cabo Verdean Kriolu official alphabet “Alfabeto Unificado para a Escrita da Língua Cabo-verdiana (ALUPEC)” (Decreto-Lei n° 67/98, 31 de Dezembro 1998, I Série n° 48, Sup. B. O. da República de Cabo Verde).

Building on the approach of Verdu et al., 2017, we were interested in inter-individual variation of “ways of speaking Kriolu” rather than in a prescriptivist approach to the Kriolu language. Thus, we considered each utterance as defined in Croft, 1996p.107: “a particular instance of actually-occurring language as it is pronounced, grammatically structured, and semantically interpreted in its context”. Transcripts were parsed together and revealed 4831 (L=4831) unique uttered items among the 92,432 uttered items transcribed in total from the 225 discourses from the genetically-unrelated Cabo Verde-born individuals. To obtain these counts, we considered phonetic, morphological, and syntactic variation of the same lexical root items that were uttered/pronounced differently, and we excluded from the utterance-counts onomatopoeia, interjections, and names. Note that we were here interested in the diversity of realizations in the Kriolu lexicon, including within the same individuals. In other words, we are interested in both between-speaker and within-speaker variation. Also note that a very limited number of English words were pronounced by particular individuals (10 utterances each occurring only once), and were kept in utterance-counts.

#### Individual Kriolu utterance frequencies

The list of unique uttered items was then used to compute individual’s specific vectors of uttered items’ relative frequencies as, for each genetically unrelated Cabo Verde-born individual i (in [1, 225]) and each unique uttered item l (in [1, L=4831]), $f_{i,l}=n_{i,l}/\sum_{j=1}^{L}n_{i,j}$, where ni,l is the absolute number of times individual i uttered the unique item l over her/his entire discourse, fi being the vector $f_{i,1},f_{i,2},…,f_{i,L}$. We compared vectors of individuals’ utterance-frequencies by computing the inter-individual pairwise Euclidean distance matrix as, for all pairs of individuals i and j, $df_{i},f_{j}=\sqrt{\sum_{l=1}^{L}f_{i,l}-f_{j,l}^{2}}$, (Verdu et al., 2017).

#### African origin of Kriolu utterances

We categorized each of the 4831 unique uttered items separately into five linguistic categories (Verdu et al., 2017). Category A included only unique utterances directly tracing to a known African language and comprised 88 unique items occurring 3803 times out of the 92,432 utterances. Category B included only items with a dual African and European etymology, that is items of a European linguistic origin strongly influenced in either meaning, syntax, grammar, or form by African languages or vice versa, attesting to the intense linguistic contacts at the origins of Cabo Verdean Kriolu, and comprised 254 unique items occurring 6960 times. Category C included 4432 items (occurring 73,799 times) with strictly Portuguese origin and not carrying identifiable traces of significant African linguistic origin or influence. Category D included 26 items occurring 6762 times with potential, not attested by linguists, traces of African languages’ phonetic or morphologic influences. Finally, Category U included the 10 English utterances occurring 10 times and the 21 unique Kriolu utterances occurring 1089 times of unknown origin as they could not be traced to African or European languages.

Following (Verdu et al., 2017), we defined an ‘African-utterances score’ based, conservatively, on the utterance frequencies obtained separately for items in Category A, Category B, and merging Categories A and B, as, for individual i and the set of utterances in each category denoted Cat (in [A; B; A&B]), $Z_{i,Cat}=\suml=1L_{Cat}f_{i,l}$, with LCat the number of uttered items in the corresponding category, and fi,l defined as previously.

### Population genetics descriptions

#### Allele Sharing Dissimilarities, Multidimensional Scaling, and ASD-MDS admixture estimates

We calculated pairwise Allele Sharing Dissimilarities (Bowcock et al., 1994) using the asd software (v1.1.0a; https://github.com/szpiech/asd; Szpiech, 2020), among the 5157 individuals in our worldwide dataset (Figure 1; Figure 1—source data 1), using 455,705 autosomal SNPs, considering, for a given pair of individuals, only the SNPs with no missing data. We then projected this dissimilarity matrix in three dimensions with metric Multidimensional Scaling using the cmdscale function in R (R Development Core Team, 2020). We conducted successive MDS analyses on different individual subsets of the original ASD matrix, by excluding, in turn, groups of individuals and recomputing each MDS separately (Appendix 2—figures 1–4; Figure 2—figure supplement 1). Lists of populations included in each analysis can be found in Figure 1—source data 1. 3D MDS animated plots in gif format for Figure 2, Figure 2—figure supplement 1, and Appendix 2—figures 1–4 were obtained with the plot3d and movie3d functions from the R packages rgl and magick.

Recently admixed individuals are intuitively expected to be at intermediate distances between the clusters formed by their putative proxy source populations on ASD-MDS two-dimensional plots. A putative estimate of individual admixture rates can then be obtained by projecting admixed individuals orthogonally on the line joining the respective centroids of each proxy-source populations and, then, calculating the distance between the projected points and either centroid, scaled by the distance between the two centroids (Appendix 1—figure 2; Fortes‐Lima et al., 2021; Paschou et al., 2007). We estimated such putative individual admixture rates in Cabo Verdean, ASW, and ACB individuals, considering sets of individuals for the putative proxy-source populations identified visually and resulting from our ASD-MDS decomposition (Appendix 2).

#### ADMIXTURE-CLUMPP-DISTRUCT and f3-admixture analyses

Based on ASD-MDS explorations, we focused on the genetic structure of individuals born in Cabo Verde compared to that of other admixed populations related to TAST migrations. Therefore, we conducted ADMIXTURE analyses (Alexander et al., 2009) using 1,100 individuals from 22 populations: four from Europe, 14 from Africa, the USA-CEU, the African-American ASW, the Barbadian-ACB populations, and the North Chinese-CHB population as an outgroup (Figure 1—source data 1). To limit clustering biases due to uneven sampling, we randomly resampled without replacement 50 individuals, once, for each one of these 22 populations. Furthermore, we also included all 44 Angolan individuals from four populations in the analyses, as no other samples from the region were available in our dataset. In addition to the 1100 individuals hence obtained, we included the 225 Cabo Verde-born individuals.

Following constructor recommendations, we pruned the initial 455,705 SNPs set for low LD using plink (Purcell et al., 2007) function --indep-pairwise for a 50 SNP-window moving in increments of 10 SNPs and a r2 threshold of 0.1. We thus conducted all subsequent ADMIXTURE analyses considering 1,369 individuals genotyped at 102,543 independent autosomal SNPs.

We performed 30 independent runs of ADMIXTURE for values of K ranging from 2 to 15. For each value of K separately, we identified groups of runs providing highly similar results (ADMIXTURE ‘modes’), with Symmetric Similarity Coefficient strictly above 99.9% for all pairs of runs within a mode, using CLUMPP (Jakobsson and Rosenberg, 2007). We plotted each modal result comprising two ADMIXTURE runs or more, for each value of K separately, using DISTRUCT (Rosenberg, 2003). We evaluated within-population variance of individual membership proportions as Fst/Fstmax values using FSTruct (Morrison et al., 2021) with 1000 Bootstrap replicates per population, for the ADMIXTURE mode result at K=2 (Figure 3—figure supplement 1).

Finally, we computed, using ADMIXTOOLS (Patterson et al., 2012; Maier et al., 2022), f3-admixture tests considering as admixture targets each Cabo Verdean birth-island, the ASW, and the ACB separately, with, as admixture sources, in turn all 108 possible pairs of one continental European population (Source 1) and one continental African population (Source 2), or the East Asian CHB (Source 1) and one continental African population (Source 2). For all tests, we used the same individuals, population groupings, and genotyping dataset as in the previous ADMIXTURE analyses (Figure 3—figure supplement 2), and considered the no-inbreeding option in ADMIXTOOLS.

### Local-ancestry inferences

To identify all populations sharing a likely common ancestry with the Cabo Verdean, ASW, or ACB individuals in our dataset using local-ancestry haplotypic inferences, we considered the same sample-set as for the ADMIXTURE analysis (Figure 1—source data 1), including all 455,705 SNPs from the merged dataset.

#### Phasing with ShapeIT2

We first phased individual genotypes using SHAPEIT2 (Delaneau et al., 2012) for the 22 autosomal chromosomes separately using the joint Hap Map Phase 3 Build GRCh38 genetic recombination map (The International HapMap 3 Consortium, 2010). We considered default parameters using phasing windows of 2 Mb and 100 states per SNP. We considered by default 7 burn-in iterations, 8 pruning iterations, 20 main iterations, and missing SNPs were imputed as monomorphic. Finally, we considered a ‘Ne’ parameter of 30,000, and all individuals were considered unrelated.

#### Chromosome painting with ChromoPainter2

We determined the possible origins of each Cabo Verdean, ASW, and ACB individual pair of phased haplotypes among European, African, USA-CEU, and Chinese-CHB populations using CHROMOPAINTER v2 (Lawson et al., 2012) with the same recombination map used for phasing. Following authors’ recommendations, we conducted a first set of 10 replicated analyses on a random subset of 10% of the individuals for chromosomes 2, 5, 12, and 19, which provided a posteriori Ne = 233.933 and θ=0.0004755376, on average by chromosome weighted by chromosome sizes, to be used in the subsequent analysis. We then conducted a full CHROMOPAINTER analysis using these parameters to paint all individuals in our dataset, in turn set as Donor and Recipient, except for Cabo Verde, ACB, and ASW individuals set only as Recipient. Finally, we combined painted chromosomes for each individual in the Cabo Verdean, ASW, and ACB population, separately.

#### Estimating possible source populations for the Cabo Verde gene-pool using SOURCEFIND

We used CHROMOPAINTER results aggregated for each Cabo Verdean, ACB, and ASW individual separately and conducted two SOURCEFIND (Chacón-Duque et al., 2018) analyses using all other populations in the dataset as a possible source, separately for four or six possible source populations (‘surrogates’), to allow a priori for symmetric or asymmetric numbers of African and European source populations for each target admixed population. We considered 400,000 MCMC iteration steps (including 100,000 burn-in) and kept only one MCMC step every 10,000 steps for final likelihood estimation. Each individual genome was divided in 100 slots with possibly different ancestry, with an expected number of surrogates equal to 0.5 times the number of surrogates, for each SOURCEFIND analysis. We aggregated results obtained for all individuals in the ACB, ASW, and each Cabo Verdean birth-island, separately. We present the highest likelihood results across 20 separate iterations of the SOURCEFIND analysis in Figure 3B. The second-best results were highly consistent and thus not shown.

### Runs of homozygosity (ROH)

#### Calling ROHs

Considering the same sample and SNP set as in the above local-ancestry analyses (Figure 1—source data 1), we called ROH with GARLIC (Szpiech et al., 2017). For each population separately, we ran GARLIC using the weighted logarithm of the odds (wLOD) score-computation scheme, with a genotyping-error rate of 10–3 (a likely overestimate), and using the same recombination map as for phasing, window sizes ranging from 30 to 90 SNPs in increments of 10 SNPs, 100 resampling to estimate allele frequencies, and all other GARLIC parameters set to default values. We only considered results obtained with a window size of 40 SNPs, which was the largest window size associated with a bimodal wLOD score distribution and a wLOD score cutoff between the two modes, for all populations.

For each population and Cabo Verdean island separately, we considered three classes of ROH that correspond to the approximate time to the most recent common ancestor of the IBD haplotypes, which can be estimated from the equation g=100/2l, where l is the ROH length in cM and g is the number of generations to the most recent common ancestor of the haplotypes (Thompson, 2013). Short ROH are less than 0.25 cM, reflecting homozygosity of haplotypes from more than 200 generations ago; medium ROH are between 0.25 cM and 1 cM reflecting demographic events having occurred between approximately 200 and 50 generations ago; and long ROH are longer than 1 cM, reflecting haplotypes with a recent common ancestor less than 50 generations ago. In Figure 4A–B and Appendix 4—figure 1, we plot the distribution of the summed length of ROH per individual per size-classes.

#### Intersecting ROH and local ancestry painting

Using the same phasing results as described above, we conducted 10 EM iterations of the RFMIX2 (Maples et al., 2013) algorithm to assign, for each Cabo Verdean individual and each SNP on each chromosome, separately, its putative source population of origin among the 24 African, European, Chinese-CHB, and USA-CEU populations. We collapsed the local ancestry assignments for each SNP in each Cabo Verdean individual hence obtained into three continental regions, representing broadly African, broadly European, and broadly East Asian ancestries respectively. Any ancestry call that was assigned a population from the African continent was assigned a category of AFR, any ancestry call that was assigned a population from the European continent was assigned a category of EUR, and any ancestry call that was assigned a population from the East Asian continent was assigned a category of ASN. We considered an approach similar to previous work (Szpiech et al., 2019), and intersected local ancestry calls with ROH calls (Figure 4C–D).

RFMIX2 only makes local ancestry calls at loci that are present in the dataset. Therefore, a gap of unclassified ancestry exists where inferred ancestry switches between two successive genotyped loci as called by RFMIX2. These gaps necessarily each contain an odd number of ancestry switch points (≥1) absent from our marker set. Therefore, when computing the total ancestry content of an ROH that overlaps one of these ancestry breakpoints, we assign half of the length of this gap to each ancestry classification, effectively extending each local ancestry segment to meet at the midpoint.

We then plotted the length distribution of long ROH for each island and we break out the distributions by ancestral haplotype background: those with only African ancestry, those with only European ancestry, and those that span at least one ancestry breakpoint (Figure 4C). We excluded long ROH in East Asian ancestry segments from this and the following analyses, as we found such ancestry overall very limited in the samples (Appendix 4—figure 2). We also excluded ROH called with heterozygous ancestry calls (e.g. called with one haplotype called as AFR and the other as EUR). These regions were also rare (Figure 4—source data 3).

Finally, we explored how total African/European ancestry in long ROH varies between islands. For each individual, we summed the total amount of each ancestry in long-ROH and plot the distributions across islands (Figure 4—figure supplement 1). High levels of a given ancestry in long ROH could stem from an overall high level of that ancestry in that individual. Therefore, for each individual, we computed their global ancestry proportions by summing up the total length of the genome inferred as a given ancestry and dividing by the length of the genome. We then plotted (Figure 4D), the difference of an individual’s long-ROH ancestry proportion and their global ancestry proportion, for African and European ancestries separately. Values above zero indicated that a given ancestry is overrepresented in long-ROH relative to genome-wide proportions of that ancestry.

To assess the significance of these deviations, we performed a non-parametric permutation test. For each individual in each island, we randomly permuted the location of all long ROH (ensuring that no permuted ROH overlap), re-computed the local AFR ancestry proportion falling within these permuted ROH, and then subtracted the global ancestry proportion. We then took the mean of this difference across all individuals for each island and repeated the process 10,000 times. As there is negligible ASN ancestry across these individuals, the AFR and EUR proportions essentially add to 1, and therefore we consider an over/under representation of AFR ancestry in long ROH to be equivalent to an under/over representation of EUR ancestry in long ROH. Permutation distributions with observed values are plotted in Figure 4—figure supplement 2 and permutation p-values are given in Figure 4—source data 2.

### Isolation-by-distance: genetic and linguistic diversity within Cabo Verde

We explored genetic pairwise levels of differentiation calculated with ASD as previously, considering the 1,899,878 non-monomorphic SNPs within Cabo Verde obtained after QC Stage 3 (Appendix 1—figure 1). We projected the matrix for the 225 unrelated Cabo Verde-born individuals using metric MDS as above. Note that pruning this data set for very low LD using plink function --indep-pairwise for a 50 SNPs window moving in increments of 10 SNPs and a r2 threshold of 0.025 resulted in 85,425 SNPs for which the ASD matrix was highly correlated with the one using all SNPs (Spearman ρ=0.8745, p<2.2 × 10–16). In parallel, we described the diversity of Kriolu idiolects (i.e. individuals’ manners of speaking Kriolu) among the 225 genetically unrelated Cabo Verde-born individuals by projecting, with metric MDS, the matrix of pairwise Euclidean distances between vectors of individuals’ utterance-frequencies (see Material and Methods section "Individual Kriolu utterance frequencies"), considering the 4831 unique uttered items.

We then conducted a series of Mantel and partial Mantel correlation tests (Legendre and Legendre, 1998), using the partial.mantel.test function in the R package ncf, with Spearman correlation and 10,000 Mantel permutations, to explore possible isolation-by-distance (Rousset, 1997) patterns as well as correlations with other variables of interest. We conducted correlation tests between either the pairwise Euclidean distances between vectors of individuals’ utterance-frequencies or genetic ASD separately, and individual pairwise matrices of (i) absolute age differences, (ii) absolute differences in academic education duration, (iii) geographic distances between residence-locations (logarithmic scale), (iv) between birth-locations, (v) between mothers’ birth-locations, (vi) between fathers’ birth-locations (Table 1, Table 1—source data 1). All pairwise geographic distances were calculated with the Haversine great-circle distance formulation (Snyder, 1987), taking 6371 km for the radius of the Earth, using the rdist.earth function in the R package fields. Before computing logarithmic distances, we added 1 km to all pairwise distances.

### Isolation-by-distance: genetic and linguistic admixture within Cabo Verde

We further explored isolation-by-distance patterns within Cabo Verde specifically for African genetic and linguistic individual admixture levels. We considered African genetic admixture levels estimated from ADMIXTURE at K=2 or ASD-MDS approaches (see Material and Methods section ‘Population genetics descriptions’, Figure 3, Appendix 1—figure 2), and individual African linguistic admixture as ‘African-utterances scores’ $Z_{i,Cat}$ as defined in Material and Methods section ‘African origin of Kriolu utterances’ for utterance lists contained in Category A, Category B, or Category A&B, respectively (Verdu et al., 2017). For genetic or linguistic admixture levels separately, we computed the pairwise matrix of individual absolute admixture levels differences, and conducted Mantel testing with the different geographical distance matrices as above. Finally, we compared African genetic and linguistic admixture scores using Spearman correlations, throughout Cabo Verde and within all birth-islands, separately.

### Inferring genetic admixture histories in Cabo Verde with MetHis-ABC

We aimed at reconstructing the detailed genetic admixture history of each Cabo Verde island separately. To do so, we first design MetHis v1.0 (Fortes‐Lima et al., 2021) forward-in-time simulations of four competing complex admixture scenarios. We then couple MetHis simulation and summary-statistics calculation tools with ABC Random-Forest scenario-choice implemented in the R package abcrf (Pudlo et al., 2016), followed by Neural-Network posterior parameter estimation with the R package abc (Csilléry et al., 2012), under the winning scenario for each island separately.

#### Simulating four competing scenarios of complex historical admixture for each Cabo Verde island

ABC inference relies on simulations conducted with scenario-parameter values drawn randomly within prior distributions set explicitly by the user. We used MetHis v1.0 (Fortes‐Lima et al., 2021) to simulate 60,000 independent autosomal SNP markers in the admixed population H, forward-in-time and individual centered, under the four competing scenarios presented in Figure 6 and Table 2 and explicated below. In all four scenarios (Figure 6; Table 2), we considered, forward-in-time, that the admixed population (Population H) is founded at generation 0, 21 generations before present. Generation 0 thus roughly corresponds to the 15th century when considering an average generation-time of 25 years and sampled individuals born on average between the 1960s and the 1980s and no later than 1990 in our dataset. This is reasonable as historical records showed that Cabo Verde was likely un-inhabited before its initial colonial settlement established in the 1460s on Santiago (Albuquerque and Santos, 1991). Due to the recent admixture history of Cabo Verde and as we considered only independent genotyped SNPs, we neglected mutation in our simulations for simplicity.

Following our descriptive analyses results, we considered scenarios with only one ‘European’ and one ‘African’ source population, and each Cabo Verde island, separately, as the ‘Admixed’ recipient population H. This corresponds to the ‘two-source’ version of the general admixture model from Verdu and Rosenberg, 2011, also explored with MetHis previously (Fortes‐Lima et al., 2021).We therefore considered a single African and European population at the source of all admixture in Cabo Verde, and further considered that both source populations were very large and at the drift-mutation equilibrium during the 21 generations of the admixture process until present. Furthermore, we considered that these source populations were accurately represented, respectively, by the Mandinka from Senegambia and the Iberian-IBS populations in a random genotyping dataset of 60,000 independent autosomal SNPs (see Results).

In brief (see below), at each generation, MetHis performs simple Wright-Fisher (Fisher, 1922; Wright, 1931) forward-in-time discrete simulations, individual-centered, in a randomly mating (without selfing) admixed population of Ng diploid individuals. Separately for each Ng individual in the admixed population at generation g, MetHis draws parents randomly from the source populations and the admixed population itself at the previous generation according to given parameter-values drawn from prior distributions separately for each simulation.

##### Hyperbolic increase, linear increase, or constant reproductive population size in the admixed population

We considered, for the admixed population H, a reproductive population size of N0 diploid individuals at generation 0, with N0 in [10,1000], and N20 in [100,100,000] at generation 20, such that N0 < N20. In between these two values, we considered for the Ng values at each generation the discrete numerical solutions of an increasing rectangular hyperbola function of parameter uN in [0,1/2] (Fortes‐Lima et al., 2021). Therefore, values of the demographic parameters N0 ~ N20 correspond to simulations with a constant admixed-population H reproductive population size of N0 diploid individuals during the entire 21 generations of the admixture process, whichever the value of uN. Instead, parameter values N0 ≠ N20 necessarily correspond to simulations with an increase in reproductive size between N0 and N20, steeper with values of uN closer to 0. Note, thus, that parameter values N0 ≠ N20 and uN close to 0 correspond to simulations where the reproductive size of the admixed population H is roughly constant and equal to N0 at each generation until a very sharp increase to reach N20 at the last generation before present. Instead, parameter values N0 ≠ N20 and uN close to 1/2 correspond to simulations with a linear increase in reproductive size between N0 and N20.

Therefore, while we do not formally compare competing scenarios with different demographic regimes in this work, each scenario comprises simulations whose parameter values correspond to a variety of constant, hyperbolic increase, or linear increase in reproductive size over the course of the admixture history of each Cabo Verdean island separately. Therefore, ABC parameter estimation of the demographic parameters N0, N20, and uN should determine, a posteriori, which of the three demographic regimes best explain our data, whichever is the winning admixture scenario among the four in competition.

##### Founding the admixed population

At generation 0 (Figure 6), the admixed population of size N0 diploid individuals drawn in [10, 1000] is founded with a proportion sEur,0 of admixed individuals’ parents originating from the European source drawn in [0,1], and a proportion of sAfr,0 parents from the African source drawn in [0,1], with sEur,0 + sAfr,0=1. Note that parameter-values of sAfr,0, or sEur,0, close to 0 correspond to simulations where the ‘admixed’ population is initially founded by only one of the sources, and that genetic admixture per se may only occur at the following admixture event.

After the founding of the admixed population H, we considered two different admixture scenarios for either source population’s contribution to the gene-pool of population H. In all cases, for all generations g in [1,20] after the initial founding of the admixed population at g=0, MetHis randomly draws parents from the African source, the European source and the admixed population H respectively in proportions sAfr,g, sEur,g, and hg, each in [0,1] and satisfying sAfr,g + sEur,g + hg = 1. Then, the software randomly builds gametes for each parent and randomly pairs them, without selfing, to produce Ng diploid individuals in the admixed population.

##### Two admixture pulses after foundation

For a given source population hereafter designated ‘Source’ (‘European’ or ‘African’ in our case), after founding at generation 0, we considered scenarios with two additional pulses of admixture (‘Source’–2Pulses scenarios). The two pulses occur, respectively, at generation tSource,p1 and tSource,p2 in [1,20], with tSource,p1 ≠ tSource,p2; and with intensity sSource,tSource,p1 and sSource,tSource,p2 in [0,1], respectively.

Note that simulations considering values of parameters tSource,p1 = tSource,p2 +1, and simulations with either sSource,tSource,p1 or sSource,tSource,p2 close to 0, may strongly resemble those expected under scenarios with only one pulse of admixture after the founding of the admixed population H.

##### A period of recurring admixture after foundation

For a given Source population, after founding at generation 0, we considered scenarios with a possible period of recurring admixture, where, during this period, admixture intensity followed a monotonically decreasing trend (“Source”-Recurring scenarios). The period of admixture occurs between times tSource,t1 and tSource,t2 in [1,20] with tSource,t2 ≥tSource,t1 +1. The beginning of the admixture period at tSource,t1 is associated with admixture intensity sSource,tSource,t1 in [0,1]. The end of the admixture period at tSource,t2 is associated with intensity sSource,tSource,t2 in [0,1] such that sSource,tSource,t1 ≥sSource,tSource,t2. In between, the admixture intensity values at each generation of the admixture period are the discrete numerical solutions of a decreasing rectangular hyperbola function of parameter uSource in [0,1/2] (Fortes‐Lima et al., 2021).

Intuitively, a u parameter value close to 0 corresponds to a sharp pulse of admixture occurring at the beginning of the admixture period of intensity sSource,tSource,t1, followed at the next generation by constant recurring admixture of intensity sSource,tSource,t2 until the end of the admixture period. Alternatively, a u parameter value close to 1/2 corresponds to a linearly decreasing admixture at each generation of the admixture period, from sSource,tSource,t1 to sSource,tSource,t2.

Note that in the limit when sSource,tSource,t1 ~sSource,tSource,t2, Recurring scenarios correspond to constant recurring admixture of that intensity. Furthermore, simulations with u and sSource,tSource,t2 parameter values both close to 0 correspond to scenarios with a single pulse of admixture from a given source after the founding pulse, occurring at time tSource,t1 and with intensity sSource,tSource,t1.

##### Four competing scenarios of admixture from two-source populations in each Cabo Verde island

Finally, we combined the 2Pulses and Recurring scenarios from either the African and European Source populations in order to produce four competing scenarios of admixture for the genetic history of Cabo Verde (Figure 6), with the only constraint that at each generation g between 1 and 20, sAfr,g + sEur,g=1 – hg, where hg is the contribution of the admixed population H to itself at the following generation in [0,1].

##### Simulating the admixed population from source-populations for 60,000 independent SNPs with MetHis

As introduced previously, our results showed that the Mandinka from West Western Africa and the Iberian IBS from South West Europe were reasonable proxies of the main source populations for the gene-pool of Cabo Verde, at least when considering a relatively small number of independent autosomal SNPs. We decided to consider both populations as very large and at the drift-mutation equilibrium since the 1460s and the initial founding of Cabo Verde. We thus chose not to explicitly simulate the evolutionary history of the two European and African populations at the source of the genetic history of the Cabo Verde islands.

Instead, we first randomly drew 60,000 independent SNPs, avoiding singletons, from the LD-pruned 102,543 independent SNPs employed for the ADMIXTURE analyses. We then built a single reservoir of ‘African’ gametes comprising 20,000 haploid genomes of 60,000 independent SNP-sites each, where each allele at each site of a gamete was randomly drawn in the site frequency spectrum observed for the corresponding SNP in the Mandinka proxy source population. Separately, we proceeded similarly to build a reservoir of 20,000 European gametes matching instead the site-frequency spectrum observed in the Iberian IBS at the 60,000 SNPs.

For a given simulation with, at generation 0, given parameter values sAfr,0 and sEur,0, each in [0,1] such that sAfr,0 + sEur,0 = 1, and a given value (in [10, 1000]) of N0 diploid individuals in the admixed population H, MetHis randomly draws two different gametes in the African gamete-reservoir and randomly pairs them to produce one parent from the African source and repeats the process sAfr,0 x 2N0 times to obtain that number of African parents. In parallel and using the same procedure, MetHis randomly builds sEur,0 x 2N0 parents from the European gamete-reservoirs. For each of N0 individuals in the admixed population separately, MetHis then draws randomly a pair of parents among the European and African parents hence obtained, and for each parent separately, builds one haploid gamete by randomly drawing one allele for each 60,000 genotypes. Finally, MetHis pairs both hence obtained gametes to create the novel individual in the admixed population at the following generation, and repeats the procedure (replacing the pair of parents after each random draw in the parental pool) for each of N0 individuals separately.

Then, for the same given simulation, admixture from a source population is set to occur at a given generation g (in [1,20]) associated with a given intensity ssource,g, keeping in mind that at all g in [1,20], sAfr,g + sEur,g + hg = 1. MetHis then builds anew ssource,g x 2Ng reproductive parents from this source population’s gamete-reservoir as previously, and in parallel randomly draws hg x 2Ng parents from the admixed population H itself at the previous generation. Then, for each of Ng individuals in the admixed population separately, MetHis randomly draws a pair of different parents (replacing the pair of parents after each random draw in the parental pool), randomly builds haploid gametes from each parent, and pairs them similarly as previously to obtain a new individual at the following generation.

Thus, note that while our source-populations’ gamete reservoirs were fixed during the admixture process, the African or the European diploid parents possibly contributing to the gene-pool of the admixed population are randomly built anew, and each produce novel gametes, at each generation and in each simulation separately. Importantly, note that recombination is thus not a parameter in MetHis simulations as all SNPs are considered statistically independent.

##### Sampling simulated source and admixed populations

At the end of each simulation, we randomly drew individual samples from each source and the admixed population H matching observed sample sizes. We randomly sampled 60 individuals in the African source gamete reservoirs, 60 individuals in the European source, and the number of admixed individuals corresponding to the sample size of each Cabo Verde island of birth of individuals or to all 225 Cabo Verde-born individuals grouped in a single random mating population, in turn (Figure 1—source data 1). We sampled individuals without grand-parents in common, as allowed in MetHis by explicit genealogical flagging of individuals during the last two generations of the admixture process, hence mimicking our observed family unrelated dataset within Cabo Verde.

##### Number of simulations and scenario-parameter priors for ABC inference

We performed 10,000 such MetHis simulations under each of four admixture scenarios for each of the nine birth-islands of Cabo Verde and for all Cabo Verde-born individuals grouped in a single population, separately. Each simulation was performed under a vector of scenario parameters drawn from prior distributions described above and in Table 2, using MetHis parameter generator tools. Separately for each island and for Cabo Verde as a single population, we used this set of simulations to determine which scenario best explained the observed data using Random-Forest ABC (see below). Under the winning scenario for each birth-island and separately for Cabo Verde as a whole, we then performed an additional 90,000 simulations each corresponding to a different vector of parameter values drawn randomly from the priors set by the user for this scenario, to produce a total of 100,000 simulations to be used for Neural-Network ABC posterior parameter estimation, for each ten – 9 islands and Cabo Verde as a whole, separately – analysis separately.

### MetHis-ABC Random Forest scenario-choice and Neural Network posterior parameter estimations

To reconstruct highly complex admixture histories in Cabo Verde using genetic data, we conducted machine-learning Approximate Bayesian Computation inferences based on the simulations produced with MetHis as described above under the four competing admixture history scenarios. We performed Random-Forest ABC scenario-choice (Pudlo et al., 2016), and Neural Network ABC posterior parameter inferences (Csilléry et al., 2012), for each Cabo Verde island and for all Cabo Verde-born individuals grouped in a single population, separately. We followed the MetHis-ABC approach proposed in Fortes‐Lima et al., 2021 for summary-statistics calculation, prior-checking, out-of-bag cross-validation, machine-learning ABC predictions and inferences parameterization, and posterior parameter cross-validation error calculations.

All the details and results of these ABC procedures can be found in corresponding Appendix 1, Appendix 1—table 1, Appendix 5—tables 1–10, Appendix 1—figures 3 and 4, Appendix 1—figure 3—Figure supplements 1–10, and Figure 7—figure supplements 1–3. Briefly, we performed 10,000 simulations of 60,000 independent SNPs under each of the four competing scenarios described above, drawing parameter values in prior distributions detailed in Table 2. As listed in Table 3 and described in details in Appendix 1, we then computed 42 summary-statistics separately for each simulated dataset comprising 60,000 independent SNPs, by drawing randomly 60 parents in the African and European source populations, and randomly drawing sample-sets matching the observed sample-sizes of each Cabo Verde birth-island or all Cabo Verde-born individuals as a single population, separately. Note that we considered summary-statistics specifically aiming at describing the distribution of individual admixture fractions in the sample set, known theoretically and empirically to be highly informative about complex admixture history parameters (Fortes‐Lima et al., 2021; Verdu and Rosenberg, 2011). We thus performed RF-ABC scenario-choices using 40,000 vectors of 42 summary-statistics (10,000 under each four competing scenarios), each corresponding to a vector of parameter values randomly drawn in prior distributions and used for MetHis simulations, for each nine birth-island and for Cabo Verde as a whole, separately. We then performed NN-ABC joint posterior parameter inferences of all scenario-parameters under the winning scenarios obtained with RF-ABC, using 100,000 vectors of 42 summary statistics obtained from additional MetHis simulations under the winning scenarios respectively for each nine birth-island and for Cabo Verde as a whole, separately.

### Software availability

MetHis is an open source C software available with user manual on GitHub at https://github.com/romain-laurent/MetHis (Fortes‐Lima et al., 2021).
