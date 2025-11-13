# Saccharomyces cerevisiae goes through distinct metabolic phases during its replicative lifespan

## Authors

- Simeon Leupold<sup>1</sup> ([ORCID: 0000-0002-7186-7061](https://orcid.org/0000-0002-7186-7061))
- Georg Hubmann<sup>1</sup>
- Athanasios Litsios<sup>1</sup> ([ORCID: 0000-0003-3588-4988](https://orcid.org/0000-0003-3588-4988))
- Anne C Meinema<sup>1</sup> ([ORCID: 0000-0002-0002-3486](https://orcid.org/0000-0002-0002-3486))
- Vakil Takhaveev<sup>1</sup> ([ORCID: 0000-0002-3474-5241](https://orcid.org/0000-0002-3474-5241))
- Alexandros Papagiannakis<sup>1</sup> ([ORCID: 0000-0002-6363-804X](https://orcid.org/0000-0002-6363-804X))
- Bastian Niebel<sup>1</sup>
- Georges Janssens<sup>2</sup>
- David Siegel<sup>3</sup>
- Matthias Heinemann<sup>1</sup> ([ORCID: 0000-0002-5512-9077](https://orcid.org/0000-0002-5512-9077)) †

### Affiliations

1. Molecular Systems Biology, Groningen Biomolecular Sciences and Biotechnology Institute University of Groningen Groningen Netherlands
2. European Research Institute for the Biology of Ageing University of Groningen, University Medical Centre Groningen Groningen Netherlands
3. Analytical Biochemistry, Groningen Research Institute of Pharmacy University of Groningen Groningen Netherlands

† Corresponding author

## Abstract

A comprehensive description of the phenotypic changes during cellular aging is key towards unraveling its causal forces. Previously, we mapped age-related changes in the proteome and transcriptome (Janssens et al., 2015). Here, employing the same experimental procedure and model-based inference, we generate a comprehensive account of metabolic changes during the replicative life of Saccharomyces cerevisiae. With age, we found decreasing metabolite levels, decreasing growth and substrate uptake rates accompanied by a switch from aerobic fermentation to respiration, with glycerol and acetate production. The identified metabolic fluxes revealed an increase in redox cofactor turnover, likely to combat increased production of reactive oxygen species. The metabolic changes are possibly a result of the age-associated decrease in surface area per cell volume. With metabolism being an important factor of the cellular phenotype, this work complements our recent mapping of the transcriptomic and proteomic changes towards a holistic description of the cellular phenotype during aging.

## Introduction

Cellular aging is a complex multifactorial process affected by an intertwined network of effectors such as protein translation, protein quality control, mitochondrial dysfunction and metabolism (Barzilai et al., 2012; Kennedy et al., 1994; Lagouge and Larsson, 2013; Webb and Brunet, 2014). Disentangling cause and effect is a major challenge in aging research (McCormick and Kennedy, 2012). A key requisite towards unraveling the causal forces of cellular aging is a comprehensive account of the concomitant phenotypic changes. In the replicatively aging budding yeast Saccharomyces cerevisiae, a common model for mitotic aging (Eisenberg et al., 2007), unfortunately, the application of cell ensemble-based omics methods has been difficult due to the rapid outgrowth of aging mother cells by the newly formed daughter cells. Through a novel cultivation technique, allowing us to generate large amounts of aged cells, we could recently perform proteome and transcriptome profiling throughout the whole lifespan of S. cerevisiae. There, on the basis of an identified gradually increasing uncoupling between protein and transcript levels of biogenesis-related genes, we conjectured that this uncoupling is one of the causal forces of aging (Janssens et al., 2015). Furthermore, we found changes in expression of enzymes and, consistent with an earlier report (Lin et al., 2001), in metabolic genes, suggesting an altered metabolism with increasing replicative age. Here, exploiting our novel cultivation technique (recently also adopted by others; Hendrickson et al., 2018), metabolomics and model-based inference methods (Niebel et al., 2019), we identified a metabolic shift during the replicative lifespan of S. cerevisiae. With this work, we complement our recent proteome and transcriptome profiling data with the corresponding metabolome and fluxome, and generate a description of the functional phenotypic changes accompanied with cellular aging which ultimately lead to senescence and cell cycle arrest.

## Results

### Column-based cultivation to enrich aged mother cells

To generate large quantities of aged cells, required for the metabolic profiling, we used our earlier developed column-based cultivation technique. Here, biotinylated cells attached to streptavidin-conjugated iron beads are immobilized inside a column positioned in the center of a ring magnet. A continuous nutrient flow through the column removes emerging daughter cells, while largely retaining mother cells (Janssens et al., 2015). Several columns operated in parallel, allowed harvesting cells at different time points, corresponding to cell age. In order to be able to infer data for aged cells from the harvested samples (which still contained a fraction of daughter cells), we generated at each harvesting time point three samples differently enriched with aged mother cells; (1) from the column effluent, (2) from the column after an additional washing step, and (3) from the washing solution (in the following referred to as mix 1, 2 and 3) (Figure 1). The exact sample compositions (i.e. the fraction of mother, daughter and dead cells) were determined by flow cytometry using a combined dye-staining with propidium iodide and avidin–FITC. We then determined the cell population-averaged intracellular metabolite concentrations and, to assess physiological parameters, measured the change in extracellular metabolites concentrations due to cell growth over a period of 3 hr. To infer the aged mother cells’ metabolite levels, physiological parameters and intracellular metabolic fluxes from the mixed-sample measurements, we employed different mathematical model-based methods (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig1-v2.jpg)

**Figure 1.:** Samples were harvested at various time points (corresponding to different cell ages) from a column-based cultivation system (Janssens et al., 2015), designed to enrich aged mother cells. The fractional abundance of mother, daughter and dead cells in each sample was determined by flow cytometry and a combined dye-staining with propidium iodide and avidin–FITC. Aliquots were used to determine the intracellular metabolite concentrations, c̄i, by LC-MS/MS and the cell count, ncell(t), by flow cytometry, extracellular metabolites (i.e. substrates and products), cS(t) and cP(t), by HPLC and the integral of oxygen and carbon transfer rates, OTR and CTR (i.e. total consumed oxygen and produced carbon dioxide) by a Respiration Activity Monitoring System (RAMOS), in the mixed population samples. Next, the age-dependent intracellular metabolite concentrations (ci) were inferred from the acquired population-average data using non-negative least square regression (NNLS) and the physiological parameters (growth (µ) and metabolite exchange rates (q)) of mother (mo) and daughter (da) cells) from an ordinary differential equation (ODE) model. The inferred physiological parameters and intracellular metabolite levels of aged mother cells were then analyzed using a combined stoichiometric-thermodynamic metabolic model and regression analysis to obtain the intracellular metabolic flux distribution.

### Intracellular metabolite concentrations decrease with cell age

The intracellular concentrations of 18 metabolites, mainly located in central carbon metabolism, were quantified by LC-MS/MS in the differently mixed samples (i.e. mix 1, 2 and 3), taken at various time points (after 10, 20, 44 and 68 hr). As these concentration measurements resembled the average concentration of metabolites originating from mother and daughter cells, we used non-negative linear regression to infer the metabolite concentration in each individual population (i.e. aged mother and young daughter cells), using the determined fractional abundances of each population and the age-dependent cell volumes, which we determined with microfluidics and microscopy (Figure 2—figure supplement 1). To confirm the validity of the regression approach, where in general a good fitting was achieved (R2 = 0.89) (Figure 2—figure supplement 2), we compared the concentrations for daughter cells, inferred from the mixed population samples, with metabolite concentrations independently determined from a culture of young streptavidin-labeled cells. Here, we found an excellent agreement between mathematically inferred and directly determined concentrations (R2 = 0.99) (Figure 2—figure supplement 3).

Focusing on the intracellular metabolite dynamics in aging mother cells, we found that the concentrations of all quantified metabolites already at a relatively young age start to decrease on average to about half of their initial values (Figure 2a and Figure 2—figure supplement 4). Previously, also other phenotypic changes have been observed at a young age (Janssens and Veenhoff, 2016). Remarkably, despite the drop in ATP levels, the adenylate energy charge was maintained between 0.8 and 0.95 (Figure 2—figure supplement 5), which corresponds to values of exponentially growing cultures (Ditzelmüller et al., 1983). The drop in metabolic concentrations suggests that metabolic activities are globally decreased in aged cells and, as many metabolites have also regulatory function (Huberts et al., 2012; Litsios et al., 2018), the observed concentration changes are expected to lead to metabolic rearrangements.

![Figure 2.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-v2.jpg)

**Figure 2.:** (a) The intracellular metabolite concentrations of 18 metabolites at various cell ages were inferred from LC-MS/MS measurements, cell volume measurements and the fractional abundances of each cell population using non-linear least square regression. Grey dashed lines depict the change of intracellular metabolite concentrations relative to concentrations determined from streptavidin-labeled cells (i.e. young cells at an age of 0 hr). The change in ATP concentration is highlighted in red, and FBP (fructose-1,6-bisphosphate) in blue. Figure 2—figure supplement 4 shows the data for each metabolite in absolute units. Figure 2—source data 1 contains the data. (b) The growth (µ), metabolite uptake and production rates at various cell ages were obtained by measuring the evolution of cell count and extracellular metabolites (including produced carbon dioxide and consumed oxygen) and fitting the acquired data to an ordinary differential equation model. A positive value indicates metabolite production and a negative uptake. To assess the validity of the inference approach physiological rates were independently determined from unlabeled and streptavidin-labeled cell cultures (time point 0 hr), consisting of predominantly young cells. The shading reflects the inverse of the relative uncertainty of the estimation (i.e. values which are depicted with a higher transparency are more uncertain). Figure 2—source data 2 contains the data.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Individual cells of Saccharomyces cerevisiae were tracked in a microfluidics device (Huberts et al., 2013; Lee et al., 2012) and bright field images were recorded throughout their whole lifespan. The cellular volume was subsequently determined from the acquired microscopic data using the ImageJ plugin BudJ.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The intracellular concentration of 18 metabolites in daughter and aging mother cells was inferred from data obtained in various mixed population samples using non-negative least square regression where we obtained an excellent fit.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** To confirm the validity of inference method for intracellular metabolite concentrations, we determined the metabolite concentration of young streptavidin-labeled cells and compared them to the inferred metabolite concentrations of daughter cells, which, by definition, should have the same phenotype. Here, we found a good consensus, confirming our approach.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** We found a drastic decrease of metabolite concentrations with cell age (starting from young daughter cells (da)) of all 18 metabolites: adenosindiphosphat (ADP), adenosinmonophosphat (AMP), aspartic acid (Asp), adenosintriphosphat (ATP), citric acid (Cit), dihyroxy acetone phosphate (DHAP), fructose 1,6-bisphosphate (FBP), fructose-6-phosphate (F6P), glucose-1-phosphate (G1P), glucose-6-phosphate (G6P), glutamic acid (Glu), malic acid (Mal), phenylalanine (Phe), phosphoenolpyruvic acid (PEP), ribose-5-phosphate (R5P), ribulose-5-phosphate (Ru5P), sedoheptulose-7-phosphate (S7P) and succinic acid (Succ). The standard errors were determined by leave-one-out cross-validation, where we one-by-one removed data points from the set and repeated the estimation procedure.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Despite the vast decrease of the inferred concentrations of all three adenosin nucleotides with cell age, the energy charge was maintained between 0.8 and 0.95, which corresponds to values of exponentially growing cultures (Ditzelmüller et al., 1983).

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** At each time point (after 10, 20, 44 and 68 hr), we measured the evolution of cell count (which was converted to dry weight (i.e. biomass)) and extracellular concentrations of acetate, ethanol, glycerol, pyruvate and glucose over a period of three hours in the harvested sample mix 1. The dry mass specific fractional abundance of each cell population was determined before and after that period. We used a second set of aliquots to measure the evolution of produced carbon dioxide and consumed oxygen using a Respiration Activity Monitoring System (RAMOS) (Hansen et al., 2012). To infer the population-specific physiological rates from the mixed-population samples, we fitted the acquired dynamic data to an ordinary differential equation model, describing the changes of the biomass and extracellular metabolite concentrations in the samples, due to mother and daughter cell growth and their respective metabolism.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** At each time point (after 10, 20, 44 and 68 hr), we measured the evolution of cell count (which was converted to dry weight (i.e. biomass)) and extracellular concentrations of acetate, ethanol, glycerol, pyruvate and glucose over a period of three hours in the harvested sample mix 2. The dry mass specific fractional abundance of each cell population was determined before and after that period. We used a second set of aliquots to measure the evolution of produced carbon dioxide and consumed oxygen using a Respiration Activity Monitoring System (RAMOS) (Hansen et al., 2012). To infer the population-specific physiological rates from the mixed-population samples, we fitted the acquired dynamic data to an ordinary differential equation model, describing the changes of the biomass and extracellular metabolite concentrations in the samples, due to mother and daughter cell growth and their respective metabolism.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp8-v2.jpg)

**Figure 2—figure supplement 8.:** At each time point (after 10, 20, 44 and 68 hr), we measured the evolution of cell count (which was converted to dry weight (i.e. biomass)) and extracellular concentrations of acetate, ethanol, glycerol, pyruvate and glucose over a period of three hours in the harvested sample mix 3. The dry mass specific fractional abundance of each cell population was determined before and after that period. We used a second set of aliquots to measure the evolution of produced carbon dioxide and consumed oxygen using a Respiration Activity Monitoring System (RAMOS) (Hansen et al., 2012). To infer the population-specific physiological rates from the mixed-population samples, we fitted the acquired dynamic data to an ordinary differential equation model, describing the changes of the biomass and extracellular metabolite concentrations in the samples, due to mother and daughter cell growth and their respective metabolism.

![Figure 2—figure supplement 9.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp9-v2.jpg)

**Figure 2—figure supplement 9.:** Fructose-1,6-bisphosphate is a glycolytic flux-signaling metabolite and its concentration strictly correlates with the carbon flow through the glycolysis or the sugar uptake rate (Huberts et al., 2012). The independently inferred rate of glycolysis and FBP concentration in aging cells follows this correlation, providing evidence for the validity of the two independently generated data sets, that is physiological rates and metabolite levels. Black dots (Christen and Sauer, 2011), grey dots (de Assis Souza, 2016) and red dots inferred for aging cells.

![Figure 2—figure supplement 10.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp10-v2.jpg)

**Figure 2—figure supplement 10.:** The decreasing growth rate inferred with cell age was confirmed using microfluidics and microscopy. Cells from an exponentially growing batch culture were loaded onto a microfluidics device and monitored for >70 hr. The doubling time (time from bud emergence to next bud emergence) was measured for each cell in bright-field images, and the budding rate for each doubling event (ln(2) td−1) was calculated. Budding rates within 6 hr windows were averaged. Note, that the growth rate in Figure 2b was inferred from the increase of biomass in the culture while here the growth rate is determined from the budding rate of individual cells. Because of the prolonged G1 phase of newborn cells and the asymmetric division, both values are not identical, however, show both a decreasing trend.

![Figure 2—figure supplement 11.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp11-v2.jpg)

**Figure 2—figure supplement 11.:** Proteomes of yeast (YSBN6 strain on 2% glucose) obtained at 12 consecutive replicative ages (gradient gray circles) were compared to proteomes of fermenting (KOY WT on 1% glucose) and respiring (KOY TM6 on 1% glucose; Elbing et al., 2004) cells derived from 12 and 13 replicate batch cultures, respectively (blue and red circles). We focused on 396 metabolic proteins present in all proteome data sets and, within each proteome, normalized their abundances by the total one. Next, we centered the 25 proteomes of fermenting and respiring cells together on the origin and performed a principal component analysis (PCA) using the module Sklearn (v0.19.1) in Python (v3.4.3). Next, we centered the proteomes of ageing cells and projected them on two principal components PC1 and PC2 that explain most of the variance among the proteomes of fermenting and respiring cells. PC1 can be interpreted as the fermentation-respiration dimension, that is, the dimension summarizing almost all the differences between the fermentation- and respiration-associated states of the yeast metabolic proteome. Here, we found that the yeast proteome during aging progressively transforms form a fermentation- to a respiration-associated state, similarly as inferred from our physiological analysis (Figures 2b and 3).

![Figure 2—figure supplement 12.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig2-figsupp12-v2.jpg)

**Figure 2—figure supplement 12.:** The replicative lifespan of S. cerevisiae is assessed in a microfluidic dissection platform in 0.5% glucose with and without 0.1% ethanol. The curves represent the survival estimates obtained by the Kaplan-Meier procedure considering the numbers of buds produced by the indicated amount of cells (including the cells that were washed out by the medium flow prior death, that is right censoring of the data; these cells are denoted as “washed”). The shaded area demarks the 95 % confidence intervals. The survival estimates were summarized using the median values and their 95 % confidence intervals (CI). Note that the mean survival with its standard error are 22.32 ± 0.76 in the absence of ethanol and 26.44 ± 1.67 in the presence of ethanol. However, as the right censoring of the data biases the calculation of the mean survival, the median is more robust. The survival curves are compared in the log-rank test whose p-value is given.

### Cells switch from a fermentative to a respiratory metabolism with age

To assess changes on the level of metabolic fluxes, we next determined the physiological rates, that is growth, metabolite uptake and excretion rates of aging cells. At each time point (after 10, 20, 44 and 68 hr), we measured the evolution of cell count and extracellular concentrations of glucose, pyruvate, acetate, glycerol and ethanol over a period of three hours in each harvested sample (i.e. mix 1, 2 and 3). The fractional abundance of each cell population was determined before and after that period. We used a second set of aliquots to measure the evolution of produced carbon dioxide and consumed oxygen using a Respiration Activity Monitoring System (RAMOS) (Hansen et al., 2012). To infer the population-specific physiological rates from the mixed-population samples, we fitted the acquired dynamic data to an ordinary differential equation model, describing the changes of the biomass and extracellular metabolite concentrations in the samples, due to mother and daughter cell growth and their respective metabolism (Figure 2—figure supplements 6–8). To assess the validity of the inference approach, we compared the physiological rates inferred for daughter cells to physiological rates independently determined from unlabeled as well as from streptavidin-labeled cell cultures, both consisting of predominantly young cells. Here, we found a good agreement between the rates mathematically inferred for daughter cells and the rates directly obtained from these cultures containing young cells (Figure 2b).

In aging cells, we found that the specific glucose uptake rate (GUR) decreased drastically towards the end of their lifespan to almost 10% of the value of young cells (Figure 2b), which is in line with the simultaneously decreasing concentration of fructose-1,6-bisphosphate (Figure 2—figure supplement 9) and its function as a glycolytic flux-signaling metabolite (Huberts et al., 2012). This decrease in GUR was accompanied by a reduction of growth rate, which we qualitatively confirmed with single-cell measurements (Figure 2—figure supplement 10). Furthermore, while at a young age, cells showed a fermentative metabolic phenotype indicated by ethanol production and a low oxygen uptake rate (although oxygen was sufficiently available in the setup; Janssens et al., 2015), with increasing age cells shifted towards a respiratory phenotype as indicated by an increase in oxygen uptake and reduced ethanol excretion (Figure 2b). Using principle component analysis, we found a similar shift on the level of protein expression data (Figure 2—figure supplement 11). However, unlike a normal respiratory metabolism, where no byproducts would be excreted, up to half of the carbon influx was directed to glycerol and acetate excretion. Acetate metabolism has been linked to apoptosis (Giannattasio et al., 2013) and the production of glycerol indicates a stress response (Albertyn et al., 1994). This stress response might be crucial for survival at a high replicative age as a gpd1Δ (rate limiting step in the synthesis of glycerol) mutant shows a significant reduced lifespan (Kaeberlein et al., 2002). At the end of their lifespan (starting from time point 44 hr), cells started to co-consume ethanol, produced by surrounding daughter cells, for which we obtained independent evidence from microfluidics experiments (Figure 2—figure supplement 12). The identified stress responsive metabolism and decreased glucose uptake rate are consistent with signatures related to starvation and oxidative stress, as foundin our earlier proteome and transcriptome analysis (Janssens et al., 2015).

### Metabolic changes are accompanied by drastic intracellular flux rearrangements

To infer the normalized intracellular flux distributions (i.e. metabolic rates normalized by GUR) from the acquired physiological data, we used a recently developed computational method (Niebel et al., 2019). This method rests on a thermodynamic and stoichiometric model of cellular metabolism (as a function of metabolite concentration and metabolic flux) and was shown to yield predictions in good agreement with 13C based metabolic flux analysis, while not relying on labelling data (Niebel et al., 2019). The model consists of a mass balanced metabolic reaction network, including glycolysis, gluconeogenesis, tricarboxylic acid cycle, amino acid-, nucleotide-, sterol-synthesis and two reactions accounting for the NAD(P)H demand required for scavenging of reactive oxygen species (ROS). The reaction directionalities are constrained by the associated changes in Gibbs energy, and the Gibbs energy dissipated by the sum of all metabolic processes is balanced with the Gibbs energy exchanged with the environment through exchange processes (i.e. the production and consumption of extracellular metabolites). Using this model and regression analysis, we analysed the inferred metabolite concentrations (Figure 2a) and physiological rates (Figure 2b) (Figure 3—figure supplement 1). Subsequently, we assessed the solution space of the regression solution by minimizing the ‘absolute sum of fluxes’ (Holzhütter, 2004) to obtain the normalized intracellular flux distributions during aging.

The inferred intracellular metabolic rearrangements with age echo our findings from the extracellular physiology. Up until an age of 20 hr the intracellular physiology depicted a fermentative phenotype with a low normalized flux into the pentose phosphate pathway and a low normalized flux in an incomplete tricarboxylic acid cycle as the majority of carbon was leaving glycolysis through the pyruvate decarboxylase towards ethanol. After 20 hr, cells began to gradually shift towards a respiratory phenotype, where an increasing proportion of the incoming carbon flux was directed into the pentose phosphate pathway and half of the carbon flux leaving the upper glycolysis going each towards glycerol excretion and through the lower glycolysis in the tricarboxylic acid cycle, while part of the carbon loss was compensated by the uptake of ethanol and pyruvate (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig3-v2.jpg)

**Figure 3.:** The normalized flux distributions (i.e. metabolic rates normalized by GUR) were obtained by minimizing the ‘absolute sum of fluxes’ within the solution space of the regression analysis of the inferred intracellular metabolite concentrations and physiological rates. The thickness of the arrows corresponds to the absolute value of the fluxes, normalized to the glucose uptake rate. The grey dots show the intracellular metabolite concentrations inferred for cells of the respective age where the diameter corresponds to the natural logarithm of the respective concentration. Note, that this figure does not show the complete model stoichiometry of the metabolic network. The numeric values of the respective normalized fluxes can be found in Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The inferred extracellular metabolic rates (normalized by the respective glucose uptake rate) and intracellular metabolite concentrations of mother cell at an age of 0, 10, 20, 44 and 68 hr were analyzed using regression analysis and a combined thermodynamic and stoichiometric metabolic network model. Fitted values from this regression analysis versus inferred values; (a) extracellular rates and (b) intracellular metabolite concentrations.

This switch in metabolic operation was accompanied by an increased redox nucleotide turnover (Figure 4). Up until an age of 20 hr, the majority of NADH was generated in glycolysis and regenerated through the alcohol dehydrogenase. After the switch to respiration, the tricarboxylic acid cycle became the major source of NADH, which in turn was regenerated in the respiratory chain. During the first 20 hr, NADPH turnover was low but after the switch towards respiration NADPH was produced in the pentose phosphate pathway and through the aldehyde dehydrogenase. The increase in redox nucleotide turnover can be attributed to increased demands to combat emerging reactive oxygen species (ROS) (Figure 4). Despite these dramatic changes in cofactor turnover, cells managed to maintain a constant NAD(P)H levels, as observed in age-spanning time-lapse analysis in single cells (Figure 4—figure supplement 1).

![Figure 4.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig4-v2.jpg)

**Figure 4.:** The redox cofactor production and consumption rates (normalized by the respective glucose uptake rate) were obtained by minimizing the absolute sum of fluxes within the solution space of the regression analysis of the inferred intracellular metabolite concentrations and physiological rates. Reactions with a maximal turnover of <0.5 mol molglc−1 were combined and depicted as various. A positive turnover means that the cofactor is produced and a negative turnover that the cofactor is consumed. Note, that we did not enforce the emergence of ROS, however, the model could fit the experimental data the best by using cofactors for ROS scavenging.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/41046/elife-41046-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Individual cells of Saccharomyces cerevisiae were tracked in a microfluidics device and fluorescence images were recorded throughout their whole lifespan. The NAD(P)H concentration was inferred from the acquired autofluorescence (Papagiannakis et al., 2017). Assuming that this measurement mostly reflects the NADH concentration, and assuming that there is a Sirtuin inhibiting effect of NADH, then this effect would be constant through age.

## Discussion

Here, employing again the same experimental setup and procedures, we complement our earlier generated transcriptome and proteome account during the replicative aging of the budding yeast Saccharomyces cerevisiae (Janssens et al., 2015), with the metabolic phenotype, inferred from cell ensemble measurements. Next to globally decreased metabolite levels, we found that cells shift with age from a fermentative towards a respiratory phenotype accompanied by a decrease in growth and glucose uptake rate. The increase in cellular volume (and the accompanying decrease in surface area per cell volume) with age (cf. Figure 2—figure supplement 1) could be in part responsible for the observed decrease in the volumetric (i.e. dry weight specific) substrate influx, next to possibly altered hexose transporter expression with age (Kamei et al., 2014). Such decreased substrate influx will lead to decreased glycolytic fluxes, which trigger a switch towards a respiratory metabolism (Huberts et al., 2012). Increased respiratory activity (Figures 2b and 3) could then lead to an increased generation of reactive oxygen species (Drakulic et al., 2005) necessitating an increase in redox cofactor turnover (Figure 4) for ROS scavenging. This cascade of metabolic changes, likely in part induced by the non-homeostatic volume increases and the concomitant collapse in substrate uptake rate, might not only cause detrimental effects due to for example ROS production, but the reduced metabolic rates might also be responsible for the entry into senescence, as it was recently shown that sufficiently high enough metabolic rates are necessary for cells to pass cell cycle start (Papagiannakis et al., 2017).

## Materials and methods

### Method 1 | strain and cultivation conditions

The haploid prototrophic Saccharomyces cerevisiae strain, YSBN6 (MATa, FY3 ho::HphMX4) (Canelas et al., 2010), which is derived from S288c, was used in this study. All cultivations were performed using yeast nitrogen base (YNB) without amino acids (ForMedium, Norfolk, UK) supplemented with 2% glucose at 30°C and 300 rpm, unless indicated differently.

#### Column-based cultivation of yeast cells and sampling

To generate large quantities of aged yeast cells, necessary to perform bulk measurements, we used a method, in which cells were immobilized on iron beads and trapped inside a column (Janssens et al., 2015). Briefly, cells were labelled with biotin and linked to streptavidin-coated iron beads. This iron bead bound cell culture was then grown in a column, equipped with an iron grid, in which the beads (and the cells attached to them) were trapped by a magnet. A continuous medium flow through the column washed out most emerging daughter cells and kept the mother cells in a constant, nutrient-rich environment. With the used flow rate of 170 mL h−1, the glucose concentration stayed almost constant (only dropped from 21.7 to 20.1 g L−1) and the concentration of major byproducts (pyruvate, succinate, glycerol, acetate and ethanol) never exceeded 1 g L−1. Furthermore, the dissolved oxygen saturation never dropped below 75%. The precise instrumental as well as experimental setup for the column-based cultivation and harvest can be found in Janssens et al. (2015).

As samples harvested from the column still resembled a mixture of mother, daughter and dead cells and any subsequent sorting step, aiming at an absolutely pure mother cell fraction would have inherently led to a distortion of the metabolic phenotype, we opted for an approach also followed in our previous study (Janssens et al., 2015), to computationally infer the phenotype of each subpopulation. Specifically, we generated at each aging time point three samples with different proportions of mothers, daughter and dead cells (i.e. (1) from the column effluent, (2) from the column after an additional washing step, (3) from the washing solution (in the following referred to as mix 1, 2 and 3)). After harvesting and before the respective analysis (and for the physiological characterization additionally at the end of the growth experiment), the cell count specific fractional abundance of each subpopulation in each sample was determined by flow cytometry and a combined dye-staining with propidium iodide and avidin – FITC. Later the metabolite concentrations and the cellular physiologies of each individual cell population (i.e. mother, daughter and dead cells) were mathematically inferred from data originating from the mixed samples and the determined fractional abundance.

### Method 2 | inference of intracellular metabolite concentrations

#### Regeneration

To allow the cells to recover from any possible stress during the sampling procedure, all samples were transferred in an Erlenmeyer flask containing 10 mL medium, adjusted to a cell density of 2 × 107 cells mL−1 and incubated for 20 min at 30°C and 300 rpm prior analysis.

#### Sample preparation

A sample of 3 × 107 cells was taken from the Erlenmeyer flask and immediately quenched in 10 mL −40°C methanol. The cells were separated from the organic solvent by centrifugation (5 min, 21’000 g, 4°C), washed with 2 mL −40°C methanol, separated again by centrifugation and stored at −80°C. For the following analysis, the cell pellet was re-suspended in 900 µL −40°C extraction buffer (methanol, acetonitrile and water, 4:4:2 v/v/v supplemented with 0.1 M formic acid) and an internal standard of 13C-labeled metabolites was added to the extraction. This standard was obtained and quantified from exponentially growing cell cultures prior to the experiment (Wahl et al., 2014). The extraction solution was agitated for 10 min at room temperature and thereafter centrifuged at maximum speed. The supernatant was transferred to a new vial and the cell pellet re-suspended in 900 µL −40°C extraction buffer and the extraction procedure was repeated a second time. The supernatants from both steps were combined and centrifuged for 45 min at 4°C and 21’000 g to remove any remaining non soluble parts. Thereafter, the supernatant was vacuum-dried at 45°C for approximately 1.5 hr and prior to the further analysis dissolved in 200 µL water.

#### Measurement of intracellular metabolites

The extracted metabolite samples were analyzed using a UHPLC-MS/MS system. The chromatographic separation was performed on a Dionex Ultimate 3000 RS UHPLC (Dionex, Germering, Germany) equipped with a Waters Acquity UPLC HSS T3 ion pair column with precolumn (dimensions: 150 × 2.1 mm, particle size: 3 μm; Waters, Milford, MA, USA). The injection volume was 10 μL and the samples were permanently cooled at 4°C. A binary solvent gradient was employed (0 min: 100% A; 5 min: 100% A 10 min: 98% A; 11 min: 91% A; 16 min: 91% A; 18 min: 75% A, 22 min: 75% A; 22 min: 0% A; 26 min: 0% A; 26 min: 100% A; 30 min: 100% A) at a flow rate of 0.35 mL min−1 where solvent A was composed of 5% methanol in water v/v supplemented with 10 mM tributylamine, 15 mM acetic acid and 1 mM 3,5-heptanedione and isopropanole as solvent B. The detection was done using multiple reaction monitoring (MRM) on a MDS Sciex API365 tandem mass spectrometer, upgraded to EP10+ (Ionics, Bolton, Ontario, Canada) and equipped with a Turbo-Ionspray source (MDS Sciex, Nieuwerkerk aan den Ijssel, Netherlands) with the following source parameter: NEB (nebulizing gas, N2): 12 a.u., CUR (curtain gas, N2): 12 a.u., CAD (collision activated dissociation gas): 4 a.u., IS (ion spray voltage): −4,500 V, TEM (temperature): 500°C.

#### Mathematical inference of intracellular metabolite concentrations of mother and daughter cells using non-negative least squares regression

The concentrations of intracellular metabolites were determined from samples harvested after 10, 20, 44, and 68 hr. The samples were measured in six replicates and the average of this replicates was used for the mathematical inference. To validate the interference approach we independently determined the intracellular metabolite concentrations of biotin labeled cells before loading them onto the column.

The general idea of the in the following described mathematical inference rests on the concept that a system of linear equations can be solved if the number of independent equations is greater or equal than the number of unknowns. This was implemented by generating at each time point three samples (i.e. mix 1, 2 and 3, cf. Methods 1). The measured concentration in each of these three samples is constituted as the sum of the two unknown concentrations in mother and daughter cells, weighted by their respective known fractional abundance.

Specifically, the in each sample (with ncell cells) measured amount of metabolite, nmeas, contains metabolites originating from mother (mo) and daughter (da) cells. As dead cells were considered to be lysed and their metabolite content accordingly leaked into the medium, we assumed that their contribution to the total metabolite pool can be neglected. With taking the respective volumes of mother and daughter cells (Method 5 and Figure 2—figure supplement 1), and the fractional abundance of each population into account, the amount of substance of each metabolite in each cell is given by,

$$
\frac{n_{i,j,k}^{meas}}{n_{j,k}^{cell}}=\alpha_{j,k}V_{k}^{mo}c_{i,k}^{mo}+\beta_{j,k}V_{}^{da}c_{i}^{da},
$$

where nmeasi,j,k is the measured amount of substance (unit mol) of the metabolite i in the sample j (i.e. mix 1, 2 or 3) at the aging time point k (i.e. 10, 20, 44 or 68 hr), ncellj,k the total amount of cells in the respective sample, αj,k and βj,k the cell count specific fractional abundance of mother and daughter cells, Vmok and Vda the cell volume (unit L cell−1) of mother and daughter cells and cmoi,k and cdai the unknown metabolite concentration (unit M) in mother and daughter cells. Note that cdai and Vda are not indexed over the aging time points k, as we assumed that the daughter cell phenotype does not change over time (i.e. daughter cells produced by young mothers are identical with daughter cells produced by old mothers). To infer the intracellular metabolite concentrations cmo and cda from the measurements, nmeas, we formulated a non-negative least square regression problem of the form,

$$
minx‖Ac−n‖_{2}^{2}, c\geq0,
$$

where the matrix A contains all fractional volumes αj,k Vmok and βj,k Vda in every sample j at every aging time point k, the vector c the unknown concentrations cmoi,k and cdai of the metabolite i in mother and daughter cells at every aging time point k and the vector n all metabolite measurements, nmeasi,j,k, normalized by the total amount of cells in the sample, ncellj,k, in every sample j at every aging time point k.

The regression problem in Equation 2 was implemented in MATLAB (Release R2013, MathWorks, Inc, Massachusetts, USA) and the unknown metabolite concentrations, c, in mother and daughter cells were identified using the function ‘lsqnonneg’. The uncertainty of the estimation was then determined by leave-one-out cross-validation, where we one-by-one removed data points from the set and repeated the estimation procedure (Figure 2—figure supplement 4).

### Method 3 | inference of growth, metabolite uptake and production rates

The physiological parameters (i.e. growth, metabolite uptake and production rates) were determined from two independent experimental campaigns. In campaign I, samples were harvested after 20, 44 and 68 hr and in campaign II after 10, 20, 44, and 68 hr where the samples from campaign II were split and analyzed in duplicates. The three data sets of both campaigns were combined for the inference. Additionally, we determined the physiologies of biotin labeled cells (referred to as ‘0 hr’) and unlabeled cells (referred to as ‘unlabeled’).

#### Batch cultivation conditions in minimal medium

The three samples obtained from the cultivation column (i.e. mix 1, 2 and 3) as well as the two reference samples (i.e. 0 hr and unlabeled) were transferred each in a 250 mL Erlenmeyer flask (or RAMOS flasks) containing 25 mL medium, adjusted to a cell density of 2 × 107 cell mL−1, and incubated at 300 rpm and 30°C.

#### Determination of cell dry weight from cell count

The cell count was measured every 20 min between 1 and 3 hr after inoculation using a BD Accuri C6 flow cytometer (Becton, Dickinson and Company, Franklin Lakes, NJ). The samples were diluted with PBS at pH seven to <106 cell mL−1 and 20 µL sample were counted at 'medium' flow. The FSC-H thresholds was set to 80’000 in order to cut off most of the electronic noise. To correct the measured dry weight for the mass of iron beads in the sample, the iron beads were gated separately and counted as well. The data were analyzed using the Accuri CFlow Plus software.

As the cell volume and thus the cell specific dry weight (i.e. the weight of one cell) of mother cells changes with age, towards converting the measured cell counts to dry weight (biomass), we first determined the cell specific dry weight of mother/dead, mmo/de, and daughter cells, mda. After 3 hr, at the end of each batch cultivation, 20 mL of culture were filtered through a pre-weighed nitrocellulose filter with a pore size of 0.2 µm. The filter was washed once with distilled water, dried at 80°C for two days and afterwards weighed again. The total weight of iron beads attached to mother cells (here we assumed that one mother cell is attached to one iron bead; Janssens et al., 2015) and free beads, which was determined from the counted number of iron beads in the sample and the weight of one individual bead, was subtracted from the total dry weight of each sample. The bead weight had been determined to be 8.49 × 10−13 g per bead by filtration and weighting of a known amount of beads. Next, the cell specific dry weight of mother/dead and daughter cells was inferred from the measured population-average dry weight in the samples, mmeas, by following an in principle similar approach as done for the intracellular metabolite concentrations. Specifically, we assumed that dead cells (i.e. died mother cells) and mother cells have the same dry mass and that the dry mass of newly formed daughter cells does not change over the aging time points. Taking the fractional abundances of each cell population into account, the measured cell specific dry mass in each sample is given as,

$$
\frac{m_{j,k}^{meas}}{n_{j,k}^{cell}}=(\alpha_{j,k}+\gamma_{j,k})m_{k}^{mo/de}+\beta_{j,k}m_{}^{da},
$$

where mmeasj,k is the measured population-average dry mass (unit g) after 3 hr cultivation in the sample j at the aging time point k, ncellj,k the total amount of cells in the respective sample, αj,k the cell count specific fraction of mother cells, γj,k the cell count specific fraction of dead cells, mmo/dek the unknown cell specific dry mass (unit g) of mother or dead cells, βj,k the cell count specific fraction of daughter cells and mda the unknown cell specific dry mass (unit g) of daughter cells. Next, we formulated a least square regression problem of the form,

$$
minx‖Am−n‖_{2}^{2},
$$

where the matrix A contains all fractional abundances αj,k + γj,k and βj,k in every sample j at every aging time point k, the vector m the unknown cell specific dry weights mmo/dek and mda at every aging time point k and the vector n all measured cell dry weights, mmeasj,k, normalized by the total amount of cells in the sample, ncellj,k, in every sample j at every aging time point k. The regression problem in Equation 4 was implemented in R (Release 3.2.0) and the unknown cell specific dry weights, m, of mother/dead and daughter cells were identified using the function ‘lm’.

The inferred cell specific dry weights of mother/dead and daughter cells were then used to convert the measured cell counts to dry weight. At the beginning of each cultivation (t = 0) the total dry weight, Xtt=0, is constituted of mother/dead and daughter cells, taking their fractional abundance into account, while in the following all new emerging cells are daughter cells. The total dry weight at every time t, Xt, is then given as,

$$
X_{t,j,k}=(\alpha_{t=0,j,k}+\gamma_{t=0,j,k})n_{t=0,j,k}m_{k}^{mo/de}+\beta_{t=0,j,k}n_{t=0,j,k}m^{da}⏟X_{t=0,j,k}+(n_{t,j,k}−n_{t=0,j,k})m^{da},
$$

where Xt,j,k is the dry weight of the mixed population sample j of the aging time point k at time t, αt=0,j,k + γt=0,j,k and βt=0,j,k the cell count specific fractional abundances of mother/dead and daughter cells at the beginning of the cultivation, nt=0,j,k the cell count at the beginning of the cultivation and nt,j,k the cell count at the time t. Note that k refers to the cell age (i.e. aging time point) and t refers to the cultivation time at each aging time point (between 0 and 3 hr).

Additionally, the inferred cell specific dry weights of mother/dead and daughter cells were used to convert the cell count specific fractional abundances, αj,k, βj,k, and γj,k, in the dry mass specific fractional abundances of mother, daughter and dead cells, αdwj,k, βdwj,k, and γdwj,k, in every sample j at every aging time point k:

$$
\alpha_{j,k}^{dw}=\frac{\alpha_{j,k}m_{k}^{mo/de}}{(\alpha_{j,k}+\gamma_{j,k})m_{k}^{mo/de}+\beta_{j,k}m^{da}},
$$



$$
\beta_{j,k}^{dw}=\frac{\beta_{j,k}m_{k}^{mo/de}}{(\alpha_{j,k}+\gamma_{j,k})m_{k}^{mo/de}+\beta_{j,k}m^{da}},
$$



$$
\gamma_{j,k}^{dw}=\frac{\gamma_{j,k}m_{k}^{mo/de}}{(\alpha_{j,k}+\gamma_{j,k})m_{k}^{mo/de}+\beta_{j,k}m^{da}},
$$

#### Determination of glucose and extracellular metabolite concentration

0.3 mL samples were taken every 20 min from 1 to 3 hr after inoculation. To separate the cells from the medium, the samples were centrifuged at maximum speed for 3 min, the supernatant transferred onto a filter column (SpinX, pore size 0.22 µm), again centrifuged at maximum spend and the flow through was further analyzed. The glucose, pyruvate, glycerol, acetate and ethanol concentration was detected using an Agilent 1290 LC HPLC system equipped with a Hi-Plex H column and 5 mM H2SO4 as eluent at a constant flow rate of 0.6 mL min−1. The injection volume was 10 µL and the column temperature was kept constant at 60°C. Glucose, glycerol, ethanol and acetate were detected by refractive index and pyruvate by UV (constant wave length of 210 nm) and the respective concentrations were determined using an external standard with known concentrations. The data were analyzed using the Agilent Open Lab CDS software.

#### Determination of total consumed oxygen and produced carbon dioxide

The oxygen transfer rate (OTR) and carbon dioxide transfer rate (CTR) were determined from exhaust gas analysis using a respiration activity monitoring system (RAMOS) (Hansen et al., 2012). The RAMOS measurement flask, containing 25 mL medium, was inoculated with 2 × 107 cell mL−1 and the cultivation conditions were identical to the batch cultures used to determine the other physiological parameters. One RAMOS measurement cycle encompassed a 10 min measuring phase and a 20 min rinsing phase. The total consumption of oxygen and the production of carbon dioxide in a time interval were calculated from the mean of two consecutive OTR and CTR measurement cycles multiplied by the time.

#### Inference of growth, metabolite uptake and production rates of mother and daughter cells

To infer the physiological parameter of mother (mo), daughter (da) and dead (de) cells from the mixed population measurements, we formulated an ordinary differential equation model describing the dynamic change of biomass and extracellular metabolites during the 3 hr cultivation in each sample. To this end, we assumed that the physiology of daughter cells stays constant over all aging time points and that within the 3 hr cultivation the physiology of the mother cells stays constant. Finally, due to the short experiment time the evaporation of water and metabolites was neglected.

The total biomass in the sample is constituted of mother, dead and daughter cells and thus the differential mass balance can be formulated as,

$$
0=\frac{d}{dt}\alpha_{j,k}^{dw}+\frac{d}{dt}\beta_{j,k}^{dw}+\frac{d}{dt}\gamma_{j,k}^{dw}.
$$

Due to the short experiment time (3 hr) compared to their life span (>50 hr), we assumed that the amount of initial mother and dead cells stays constant (i.e. no new mother cells emerge and no mother cells die during the experiment). Thus,

$$
\frac{d}{dt}X_{j,k}^{mo}=\frac{d}{dt}(\alpha_{j,k}^{dw}X_{j,k})=0,
$$

and

$$
\frac{d}{dt}X_{j,k}^{de}=\frac{d}{dt}(\gamma_{j,k}^{dw}X_{j,k})=0,
$$

where Xj,k is the total biomass and Xmoj,k and Xdej,k the biomass of mother and dead cells in sample j at the aging time point k.

From Equation 9, 10 and 11, and follows that the change in total biomass is only due to the change in daughter cell biomass, Xdaj,k, which in turn can be either due to the emergence of new daughter cells originating from mother cells (i.e. budding of mother cells) or originating from daughter cells (i.e. budding of daughter cells). Thus, the change of the total biomass is given as,

$$
\frac{d}{dt}X_{j,k}^{}=\frac{d}{dt}X_{j,k}^{da}=\frac{d}{dt}(\beta_{j,k}^{dw}X_{j,k})=\mu_{k}^{mo}\alpha_{j,k}^{dw}X_{j,k}+\mu^{da}\beta_{j,k}^{dw}X_{j,k},
$$

where µmok is the growth rate (unit h−1) of mother cells and µda is the growth rate (unit h−1) of daughter cells.

Reformulating the partial derivatives in Equations 10 and 11 and adding Equation 12 yields the change in dry mass specific fractional abundance of mother and dead cells as,

$$
\frac{d}{dt}\alpha_{j,k}^{dw}=\frac{\alpha_{j,k}^{dw}}{X_{j,k}}\frac{d}{dt}X_{j,k}=−\alpha_{j,k}^{dw}(\alpha_{j,k}^{dw}\mu_{k}^{mo}+\beta_{j,k}^{dw}\mu_{}^{da}),
$$

and

$$
\frac{d}{dt}\gamma_{j,k}^{dw}=\frac{\gamma_{j,k}^{dw}}{X_{j,k}}\frac{d}{dt}X_{j,k}=−\gamma_{j,k}^{dw}(\alpha_{j,k}^{dw}\mu_{k}^{mo}+\beta_{j,k}^{dw}\mu^{da}),
$$

and plugging Equations 13 and 14 and in the differential biomass balance (Equation 9) yields the change in fractional abundance of daughter cells due to budding of mother and daughter cells as,

$$
\frac{d}{dt}\beta_{j,k}^{dw}=(\alpha_{j,k}^{dw}+\gamma_{j,k}^{dw})(\alpha_{j,k}^{dw}\mu_{k}^{mo}+\beta_{j,k}^{dw}\mu^{da}).
$$

Next, the change in glucose concentration in the medium can be due to the uptake by mother and daughter cells as in,

$$
\frac{d}{dt}c_{glc,j,k}=−X_{j,k}(\alpha_{j,k}^{dw}\frac{\mu_{k}^{mo}}{Y_{XS,k}^{mo}}⏟q_{S,k}^{mo}+\beta_{j,k}^{dw}\frac{\mu^{da}}{Y_{XS}^{da}}⏟q_{S}^{da}),
$$

where cglc,j,k is the measured glucose concentration (unit g L−1) in sample j at the aging time point k, qSmok and qSda the specific uptake rates of mother and daughter cells and YXSmok and YXSda the biomass yields (unit g gGLU−1) of mother and daughter cells.

In a similar way, the mass balance for oxygen, carbon dioxide and other fermentation products can be formulated:

$$
\frac{d}{dt}c_{O_{2},j,k}=−X_{j,k}(\alpha_{j,k}^{dw}Y_{O_{2}S,k}^{mo}\frac{\mu_{k}^{mo}}{Y_{XS,k}^{mo}}⏟q_{O_{2},k}^{mo}+\beta_{j,k}^{dw}Y_{O_{2}S}^{da}\frac{\mu^{da}}{Y_{XS}^{da}}⏟q_{O_{2}}^{da}),
$$



$$
\frac{d}{dt}c_{P,j,k}=X_{j,k}(\alpha_{j,k}^{dw}Y_{PS,k}^{mo}\frac{\mu_{k}^{mo}}{Y_{XS,k}^{mo}}⏟q_{P,k}^{mo}+\beta_{j,k}^{dw}Y_{PS}^{da}\frac{\mu^{da}}{Y_{XS}^{da}}⏟q_{P}^{da}),
$$

where qO2mok, qO2da, qPmok and qPda are the biomass specific oxygen uptake and product (including carbon dioxide) excretion rates (unit g gDW−1 h−1) of mother and daughter cells at the aging time point k and YO2Smok, YO2Sda, YPSmok and YPSda the respective oxygen and product yields (unit g gGLU−1) of mother and daughter cells.

To increase robustness in the estimation, we stated that the mother and daughter cell physiology needs to fulfill the carbon balance within a certain range.

$$
0.5\leq\frac{\sumq_{P}^{C}}{q_{S}^{C}}\leq1.5,
$$

where qCS and qCP are the specific carbon uptake and excretion rates (unit C-mol gDW−1 h−1) of mother and daughter cells.

All three datasets were combined into one parameter estimation problem subject to the Equations 12–19. All parameters (including initial conditions) as well as the associated uncertainties were estimated using Maximum Likelihood estimation implemented in the software gPROMS ModelBuilder (Release 4.0, PSE software systems) with the MINLP solver SRQPD where a constant variance (error model) was assumed for all measurements.

### Method 4 | inference of intracellular metabolic fluxes

#### Computational model of cellular metabolism

To determine the intracellular fluxes at different cell ages from the inferred metabolite concentrations and physiologies, we made use of a recently published computational inference method (Niebel et al., 2019). This method rests on a combined thermodynamic and stoichiometric network model of cellular operation, M(v,lnc)≤0 (Equation 20), consisting of a mass balanced metabolic reaction network, in which the reaction directionalities are constraint by the associated changes in Gibbs energy – as a function of the metabolite concentrations c – through the 2nd law of thermodynamics. Additionally, the Gibbs energy, which is dissipated through metabolic operation (i.e. the sum of all metabolic processes, MET) is balanced with the Gibbs energy exchanged with the environment through exchange processes (i.e. the production and consumption of metabolites, EXG),

$$
{M(v,ln⁡c)\leq0}={\sumj\inMETS_{ij}v_{j}=v_{i\inEXG}∀iΔ_{r}G^{′}(ln⁡c_{j})v_{j}\leq0∀j\inMET\sumj\inMETΔ_{r}G^{′}(ln⁡c_{j})v_{j}=\sumi\inEXGΔ_{f}G^{′}(ln⁡c_{i})v_{i}},
$$

where Sij is the stoichiometric coefficient of the ith reactant (i.e. metabolite) in reaction j, vj the rate of the reaction j (i.e. the flux through this reaction), ΔrG’(ln cj) the Gibbs free energy of reaction of the metabolic process j and ΔfG’(ln ci) the Gibbs free energy of formation of the reactant i.

The published, and here used, model for Saccharomyces cerevisiae encompasses the metabolic processes of glycolysis, gluconeogenesis, tricarboxylic acid cycle, amino acid-, nucleotide-, sterol-synthesis and considers the processes’ location in the cytosol, mitochondria and extracellular space. To account for cofactor turnover due to the combatting of reactive oxygen species, which is known to occur at high replicative ages (Ayer et al., 2014), the model was extended by reactions describing the oxidation of NADH and NADPH through glutathione in the cytoplasm as well as the glutathione exchange (i.e. a sink and a source). This exchange does not represent any direct metabolic process but needed to be included since the glutathione metabolism is not part of this model.             nadh[c] + gthox[c] => nad[c] + (2) gthrd[c]
             nadh[c] + gthox[c] => nad[c] + (2) gthrd[c]
                               gthox[c] <=>
                               gthrd[c] <=>

A more detailed description of this model and its implementation can be found in Niebel et al. (2019).

#### Regression analysis

Using this model and the inferred age-dependent metabolite concentrations and physiologies, we formulated a regression problem minimizing the weighted residual sum of squares, RSS(y) (Equation 21). As data we used (i) the inferred yields, $Y~_{i}^{(k)}$ (i∈PY… physiological yield), (ii) the inferred metabolite concentrations $c~_{i}^{(k)}$ (i∈MC1∪i∈MC2… metabolite concentration set 1 or 2 (see below)), both of daughter and aged mother cells at a replicate age of 0, 10, 20, 44 and 68 hr and (iii) standard Gibbs energies of reaction, $Δ_{r}G~_{j}^{′o}$. The later were determined (including uncertainty) using the component contribution method (Noor et al., 2013) and as this was not possible for all standard Gibbs energies, to prevent overfitting, the regression was regularized by the Lasso method (Hastie et al., 2011).

To ensure the same thermodynamic reference state (i.e. the same standard Gibbs energies of reactions) in all experimental conditions, we bundled all datasets in on regression problem and indexed the model (Equation 20) over the experimental conditions k.

$$
RSS¯(y)=\frac{1}{#n_{Y}}\sumk,i\inPY(\frac{\frac{v_{i}^{(k)}}{v_{glc−D_EX}^{(k)}}−Y~_{i}^{(k)}}{Y~_{i}^{(k),SE}})^{2}+\frac{1}{#n_{c}}[\sumk,i\inMC1(\frac{e^{lnc_{i[c]}^{(k)}}−c~_{i}^{(k)}}{c~_{i}^{(k),SE}})^{2}+\sumk,i\inMC2(\frac{0.9e^{lnc_{i[c]}^{(k)}}+0.1e^{lnc_{i[m]}^{(k)}}−c~_{i}^{(k)}}{c~_{i}^{(k),SE}})],+\frac{1}{#n_{CCM}}\sumj\inCC(\frac{Δ_{r}G_{j}^{′o}−Δ_{r}G~_{j}^{′o}}{Δ_{r}G~_{j}^{′o,SE}})^{2}+\frac{0.05}{#n_{unk}}|Δ_{r}G_{j}^{′o}|
$$

where #nY and #nc are the number of inferred yields and metabolite concentrations, #nCCM the number of standard Gibbs energies of reaction, which could be estimated by the component contribution method and #nunk the number of reactions where no standard Gibbs energy of reaction could be calculated. The residuals were weighted by the respective prediction uncertainty, indicated by the superscript SE. Metabolites can occur in the cytoplasm and/or in the mitochondrial space (MC1… metabolites occurring in one compartment and MC2… metabolites occurring in two compartments). Thus, we stated that the sum of the metabolite concentrations in the respective compartments, weighted by the fractional compartmental volume (0.9 for the cytoplasm and 0.1 for the mitochondrial space), had to be equal to the inferred (cell-averaging) concentration. Last, to facilitate the convergence of the optimization and for an easy conversion of reaction rates to yields, the glucose uptake rate, vglc-D_EX, was constraint to a value of 1 mmol gDW-1 h-1.

The regression analysis was implemented in the mathematical programming system GAMS (GAMS Development Corporation; General Algebraic Modeling System (GAMS) Release 24.2.2. Washington, DC, USA).

#### Evaluation of the solution space

To obtain a picture of the intracellular flux distribution, we formulated the solution space, Ωreg (Equation 22), of the optimal regression solution, indicated by an *,

$$
Ω^{reg}={(v^{(k)},ln⁡c^{(k)},Δ_{r}G^{′o})|M^{(k)}(v^{(k)},ln⁡c^{(k)},Δ_{r}G^{′o})∧(\frac{v_{i}^{(k)}}{v_{glc−D_EX}^{(k)}}=Y_{i}^{(k)∗} ∀i\inPY)∧(ln⁡c_{i}^{(k)}=ln⁡c_{i}^{(k)} ∀i\inMC1)∧(0.9e^{ln⁡c_{i[c]}^{(k)}}+0.1e^{ln⁡c_{i[m]}^{(k)}}=0.9e^{ln⁡c_{i[c]}^{(k)∗}}+0.1e^{ln⁡c_{i[m]}^{(k)∗}} ∀i\inMC2)∧(Δ_{r}G^{′o}=Δ_{r}G^{′o∗})}.
$$

Within this solution space we then minimized the ‘absolute sum of fluxes’,

$$
min{\sumj|v_{j}|:(v,ln⁡c)\inΩ_{}^{reg}}.
$$

The optimization problem in Equation 23 was implemented in the mathematical programming system GAMS (GAMS Development Corporation; General Algebraic Modeling System (GAMS) Release 24.2.2. Washington, DC, USA).

### Method 5 | determination of NAD(P)H concentration, budding rate, cell size and replicative lifespan using single cell analysis

#### Microscopy

For microscopy experiments, cells from exponentially growing batch cultures were used to load a microfluidic device (Huberts et al., 2013; Lee et al., 2012). Individual cells were monitored using an inverted fluorescence microscope (Eclipse Ti-E; Nikon) housed in an custom-made microscope incubator (Life Imaging Services GmbH) that retained at a constant temperature of 30°C. During the experiment, cells were continuously fed with fresh medium. An LED-based excitation system (pE2; CoolLED) was used for illumination, and images were recorded using an Andor 897 Ultra EX2 EM-CCD camera. NAD(P)H autofluorescence (excitation at 365 nm using a 357/44 nm filter and a 409 nm beam-splitter, 200 ms exposure time, 15 % light intensity, 435/40 nm emission, EM gain 1) was recorded every 60 min to minimize phototoxic effects, and brightfield images every 10 min to reliably track individual cells and determine their division times. A CSI S Fluor 40x Oil (NA = 1.3; Nikon) objective was used for NAD(P)H. Automated hardware (PFS, Nikon) was used for correction of axial focus fluctuations during imaging.

#### Image and data analysis

Cell segmentation for estimation of cell volume and fluorescence intensity took place in a semi-automated manner using the ImageJ plugin BudJ (Ferrezuelo et al., 2012). For cell volume estimation, brightfield images captured with the 60x objective were used. Fluorescent intensity measurements were corrected for background fluorescence using the Rolling Ball Radius algorithm of ImageJ. For budding rate estimations on the basis of single-cells, the doubling time, td, (time from bud emergence to bud emergence) was measured for each cell in 60x brightfield images, and the budding rate for each doubling event (ln(2) td-1) was calculated.

#### Replicative lifespan

Cells from an exponentially growing culture (minimal medium; Verduyn et al., 1992) supplemented with 1 % (w/v) glucose were loaded in two identical microfluidic devices located on one cover glass. Minimal media supplemented with 0.5 % (w/v) glucose with and without 0.1 % (v/v) ethanol were constantly supplied into the two microfluidic devices, respectively. The cells in the microfluidic devices were monitored simultaneously by taking bright-field images every 10 minutes for more than 5 days (halogen lamp with a UV-blocking filter, 60x objective). The time points of budding, death and washout loss were recorded for individual cells using a custom macro in ImageJ. The number of budding events and fate (death or washed) of the individual cells in both microfluidic devices were used to assess the replicative age-associated survival via the Kaplan-Meier estimator. The analysis was implemented using the Lifelines (0.9.4) module in Python (2.7.13). The mean survival and its standard error were calculated using the Survival (2.43-3) package in R (3.4.1) integrating the survival curves until 44 buds (the maximal number of buds per cell in two conditions).
