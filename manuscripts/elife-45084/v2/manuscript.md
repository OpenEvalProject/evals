# Heterogeneity in surface sensing suggests a division of labor in Pseudomonas aeruginosa populations

## Authors

- Catherine R Armbruster<sup>1</sup> ([ORCID: 0000-0003-0795-802X](https://orcid.org/0000-0003-0795-802X))
- Calvin K Lee<sup>2</sup> ([ORCID: 0000-0001-6789-0317](https://orcid.org/0000-0001-6789-0317))
- Jessica Parker-Gilham<sup>1</sup>
- Jaime de Anda<sup>2</sup>
- Aiguo Xia<sup>5</sup>
- Kun Zhao<sup>6</sup>
- Keiji Murakami<sup>8</sup>
- Boo Shan Tseng<sup>9</sup> ([ORCID: 0000-0001-7563-0232](https://orcid.org/0000-0001-7563-0232))
- Lucas R Hoffman<sup>1</sup>
- Fan Jin<sup>5</sup> ([ORCID: 0000-0003-2313-0388](https://orcid.org/0000-0003-2313-0388))
- Caroline S Harwood<sup>1</sup>
- Gerard CL Wong<sup>2</sup>
- Matthew R Parsek<sup>1</sup> ([ORCID: 0000-0003-2932-7966](https://orcid.org/0000-0003-2932-7966)) †

### Affiliations

1. Department of Microbiology University of Washington Seattle United States
2. Department of Bioengineering University of California, Los Angeles Los Angeles United States
3. Department of Chemistry and Biochemistry University of California, Los Angeles Los Angeles United States
4. California NanoSystems Institute University of California, Los Angeles Los Angeles United States
5. Hefei National Laboratory for Physical Sciences at the Microscale University of Science and Technology of China Hefei China
6. Key Laboratory of Systems Bioengineering (Ministry of Education), School of Chemical Engineering and Technology Tianjin University Tianjin China
7. Collaborative Innovation Centre of Chemical Science and Engineering Tianjin University Tianjin China
8. Department of Oral Microbiology, Institute of Biomedical Sciences Tokushima University Graduate School Tokushima Japan
9. School of Life Sciences University of Nevada Las Vegas United States
10. Department of Pediatrics University of Washington Seattle United States
11. Institute of Synthetic Biology Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences Shenzhen China
12. Integrative Microbiology Research Centre South China Agricultural University Guangzhou China

† Corresponding author

## Abstract

The second messenger signaling molecule cyclic diguanylate monophosphate (c-di-GMP) drives the transition between planktonic and biofilm growth in many bacterial species. Pseudomonas aeruginosa has two surface sensing systems that produce c-di-GMP in response to surface adherence. Current thinking in the field is that once cells attach to a surface, they uniformly respond by producing c-di-GMP. Here, we describe how the Wsp system generates heterogeneity in surface sensing, resulting in two physiologically distinct subpopulations of cells. One subpopulation has elevated c-di-GMP and produces biofilm matrix, serving as the founders of initial microcolonies. The other subpopulation has low c-di-GMP and engages in surface motility, allowing for exploration of the surface. We also show that this heterogeneity strongly correlates to surface behavior for descendent cells. Together, our results suggest that after surface attachment, P. aeruginosa engages in a division of labor that persists across generations, accelerating early biofilm formation and surface exploration.

## Introduction

Pseudomonas aeruginosa is an opportunistic pathogen that engages in a range of surface-associated behaviors and is a model bacterium for studies of surface-associated communities called biofilms. Biofilms are dense aggregates of cells producing extracellular matrix components that hold the community together. The biofilm mode of growth is beneficial for bacteria in that it allows cells to maintain close proximity to nutrients, promotes exchange of genetic material, and confers cells protection from a variety of chemical and environmental stresses (e.g. nutrient limitation, desiccation, and shear forces), as well as engulfment by protozoa in the environment or by phagocytes in a host (Davey and O'toole, 2000). Collectively, these advantages make biofilm formation integral to prokaryotic life.

The secondary messenger signaling molecule cylic diguanylate monophosphate (c-di-GMP) controls the transition between the planktonic to the biofilm mode of growth. In many bacterial species, including P. aeruginosa, elevated c-di-GMP results in repression of flagellar motility genes, while promoting expression of genes involved in producing a biofilm matrix (Römling et al., 2013). The P. aeruginosa biofilm matrix is composed of a combination of polysaccharides (including Pel and Psl), proteins (including the adhesin CdrA), and extracellular DNA (Ma et al., 2009). Biofilm matrix production is an energetically costly process that is regulated at multiple levels (Wei and Ma, 2013). The cdrA, pel and psl genes are all transcriptionally induced under conditions of high c-di-GMP (Starkey et al., 2009).

For many species, the initial step in biofilm formation involves adherence of free swimming planktonic cells to a surface and the initiation of surface sensing. P. aeruginosa has at least two distinct surface sensing systems, the Wsp and the Pil-Chp systems, that when activated, lead to biofilm formation. The Wsp system senses an unknown surface-related signal (recently proposed to be membrane perturbation [Chen et al., 2014]) through WspA, a membrane-bound protein homologous to methyl-accepting chemotaxis proteins (MCPs). Activation of this system stimulates phosphorylation of the diguanylate cyclase WspR, which leads to the formation of aggregates of phosphorylated WspR (WspR-P) in the form of visible subcellular clusters. This aggregation of WspR-P potentiates its activity, increasing c-di-GMP synthesis (Huangyutitham et al., 2013). In comparison, the Pil-Chp chemosensory-like system initiates a hierarchical cascade of second messenger signaling in response to a surface (Luo et al., 2015). First, an increase in cellular cAMP levels occurs through activation of the adenylate cyclase CyaB by the Pil-Chp complex. This increases expression of genes involved in type IV pilus biogenesis, including PilY1. PilY1 is associated with the type IV pilus and harbors a Von Willebrand motif, which is involved in mechanosensing in eukaryotic systems (Kuchma et al., 2010). Thus, it has been proposed that this protein may be involved in the mechanosensing of surfaces (Persat et al., 2015). The output of this second signal is through the diguanylate cyclase, SadC, resulting in an increase in cellular c-di-GMP levels. Unlike the Wsp system, which localizes laterally along the cell (O'Connor et al., 2012), PilY1 is required to be associated with polarly-localized type IV pili in order to stimulate c-di-GMP production (Luo et al., 2015; Kuchma et al., 2010), suggesting that P. aeruginosa deploys both polar and laterally localized systems to promote c-di-GMP synthesis in response to a surface.

Bacteria in biofilms have long been appreciated to exhibit phenotypic heterogeneity due to chemical variation within the biofilm itself, including gradients of oxygen (Wessel et al., 2014), nutrients (Schreiber et al., 2016), and pH (Vroom et al., 1999). These environmental conditions are sensed by individual bacterial cells, leading to differential gene expression and metabolic activities even within a genetically homogeneous population (Stewart and Franklin, 2008). Specifically, the term ‘division of labor’ refers to cases where genetic or phenotypic heterogeneity results in subpopulations of cells cooperating to perform distinct tasks that provide an overall fitness benefit to the population (West and Cooper, 2016). Through task allocation, subpopulations of cells can engage in behaviors that are impossible to perform simulataneously (e.g. bet-hedging strategies between biofilm and planktonic cells [Lowery et al., 2017]), energetically costly to switch between (e.g. task-switching [Goldsby et al., 2012]), or are metabolically incompatible (e.g. photosynthesis and nitrogen fixation in cyanobacteria ([Rossetti et al., 2010]). In particular, there is a rich body of literature demonstrating that genetic (Kim et al., 2016; Dragoš et al., 2018; Klausen et al., 2003) and phenotypic variation (Klauck et al., 2018; Serra et al., 2015; Haagensen et al., 2007) in surface motility and polysaccharide production among individual bacterial cells within a biofilm can represent a division of labor that is required to achieve the architecture and structural integrity of the biofilm matrix (van Gestel et al., 2015).

Beyond heterogeneity as a result of variation in environmental signals, recent single-cell analyses have revealed that c-di-GMP signaling can drive phenotypic heterogeneity among populations of single cells exposed to the same environmental inputs. Planktonic P. aeruginosa have been shown to achieve heterogeneity among very low levels of c-di-GMP through assymetrical partitioning of a diguanylate cyclase during cell division, leading to diverse swimming molitity behaviors (Kulasekara et al., 2013). More recently, this same assymetrical cell division mechanism was shown to generate two populations of P. aeruginosa, one piliated and one flagellated, that are each required for efficient tissue colonization (Laventie et al., 2019). Together, these studies support a role for c-di-GMP heterogeneity in generating diverse bacterial behaviors during both biofilm and planktonic growth.

Here, we examined the dynamics of c-di-GMP production and bacterial surface motility at the single-cell level during early stages of biofilm formation. We used a plasmid-based, transcriptional reporter of intracellular c-di-GMP to follow the downstream fate of cells producing varying levels of c-di-GMP in response to surface attachment. Within a clonal population of P. aeruginosa, we found that levels of c-di-GMP vary among individual cells as they sense a surface, leading to a division of labor between two energetically costly behaviors associated with early biofilm formation: surface exploration and polysaccharide production.

## Results

### Cellular c-di-GMP levels rapidly increase upon surface attachment

We initially compared levels of c-di-GMP between P. aeruginosa PAO1 cells growing attached to a silicone surface and subjected to constant flow for 4 hr to those grown planktonically for 4 hr. As expected, we observed that PAO1 cellular c-di-GMP levels are 4.4-fold higher (±0.78 SD, N = 3, p≤0.05) after 4 hr of growth attached to a surface compared to planktonic growth (Figure 1A). Because direct measurement of c-di-GMP by LC-MS/MS is limited by our ability to generate enough biomass at earlier time points, we used qRT-PCR to monitor pel transcript levels as a readout of c-di-GMP. We found that after just 30 min of surface attachment, pelA transcript levels had increased almost 10-fold compared to planktonically grown cells (Figure 1—figure supplement 1). This is consistent with previously published literature showing that transcription of the pel operon is directly and positively controlled by high cellular levels of c-di-GMP (Hickman and Harwood, 2008; Baraquet et al., 2012).

![Figure 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-v2.jpg)

**Figure 1.:** (A) c-di-GMP levels are elevated rapidly upon association of P. aeruginosa PAO1 cells with a surface. Relative levels of intracellular c-di-GMP in wild type PAO1 cells grown either planktonically or after 4 hr of attachment to a silicone tube. Values are normalized to the average concentration of c-di-GMP in planktonic cells, in pmol c-di-GMP/mg total protein as determined by LC-MS/MS, and presented as mean and SD. *p<0.05 by T-test, N = 3. Figure 1—figure supplement 1 shows the Pel polysaccharide operon is transcriptionally activated almost 10-fold compared to planktonic cells within 30 min of surface attachment. (B) Two commonly studied P. aeruginosa lab strains, PAO1 and PA14, differentially activate the c-di-GMP reporter during surface sensing. Wild type PAO1 or PA14 cells harboring the c-di-GMP reporter (pPcdrA::gfpASV) were grown to mid-log phase in planktonic culture, then inoculated into a flow cell and supplied with 1% LB medium. Surface attached cells were imaged immediately after inoculation (time 0 hr), and hourly for 12 hr. The c-di-GMP reporter is activated in a subset of wild type PAO1 cells within 1 hr of surface attachment and remains activated in approximately 60% of PAO1 cells during the first 6 hr of attachment. In PA14, the c-di-GMP reporter is activated in a smaller proportion of attached cells compared to PAO1. Data points are mean percentage of reporter activated cells from each time point across at least three biological replicates, with standard deviation. Figure 1—figure supplement 4 shows an additional c-di-GMP responsive transcriptional reporter (using the siaA promoter) is also responsive to Wsp-dependent changes in cellular levels of c-di-GMP. (C) Wild type PAO1 cells display heterogeneity in c-di-GMP reporter activity after 6 hr of surface attachment. Confocal microscopy image of wild type PAO1 PcdrA::gfpASV grown in 1% LB after 6 hr of surface attachment during a time course flow cell experiment. Bright field (gray) and GFP (green) channels are merged. Wild type PAO1 PcdrA::gfpASV was grown in 1% LB and imaged by CSLM. Figure 1—figure supplement 2 shows additional representative timecourse images of PAO1. (D) Psl exopolysaccharide production is enriched in the population of cells with high c-di-GMP. Representative scatterplot of reporter activity versus Psl lectin binding in wild type PAO1 harboring the pPcdrA::gfpASV reporter grown for four hours in LB before surface attached cells were harvested, stained with the lectin, washed, and counted by flow cytometry. (E) Subpopulations of PAO1 cells with high and low c-di-GMP reporter activity are physiologically distinct. Cells with higher c-di-GMP reporter activity have increased expression of Pel and Psl biosynthetic machinery genes. After 4 hr of attachment to glass, wild type PAO1 cells were separated by flow-assisted cell sorting (FACS) into a population of cells with high (on) and low (off) c-di-GMP reporter activity, then qRT-PCR was performed to quantify expression of Pel and Psl exopolysaccharide biosynthesis genes. Levels of expression of Pel or Psl mRNA were normalized to the off population. *p<0.05 by T-test, N = 3 biological replicates. Figure 1—figure supplement 3 shows controls for validating the protocol to monitor pPcdrA::gfpASV by flow cytometry. Figure 1—source data 2 shows by flow cytometry that Psl and Pel polysaccharide production is highest in cells with high pPcdrA::gfpASV reporter activity.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** qRT-PCR was performed to detect pelA transcript levels in silicone tube biofilm cells compared to planktonic cells (red). Biofilm transcript levels were normalized to planktonic levels at each time point. Colony forming units (CFU) of biofilm attached cells is plotted in yellow at each time point.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** A strain harboring the vector control, which encoded gfpASV, but lacks the PcdrA promoter was imaged alongside each reporter strain (in the appropriate genetic background) to confirm that GFP fluorescence was not due to random expression from the plasmid. Wild type PAO1 PcdrA::gfpASV was grown in 1% LB and imaged by CSLM. bf = bright field, merge = bright field and GFP channels combined.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Each dot represents background-subtracted fluorescence intensity of a single cell. The median and interquartile range is overlaid onto each time point. The dotted line depicts the cut-off for ‘on’ vs. ‘off’ cells used throughout the study, which reliably categorizes all promotor-less vector control cells as ‘off’.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp4-v2.jpg)

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Brackets indicate gates for ‘on’ (GFP above 1.7 × 102 RFU) or ‘off’ (GFP below 1.7 × 102 RFU) reporter cells and the number above the bracket indicates the percentage of cells that fall within that gate. (a) Wild type PAO1 cells were used to determine the background level of fluorescence on the BD Aria III for GFP measurements. The population of cells falls below 103 RFU. (b) A P. aeruginosa strain constitutively expressing stable GFP (PAO1 Tn7::P(A1/04/03)::GFPmut) was used to determine gating for cells with high GFP, with the population ranging from 103 to 105 RFU. (c) Surface grown PAO1 ΔwspFΔpelΔpsl harboring the pPcdrA::gfpASV was used to validate the gate for collection of cells with high reporter activity (103 to 105 RFU; 91.6% of the population). (d) Example of gating for reporter ‘on’ cells from wild type PAO1 pPcdrA::gfpASV cells that had been attached to glass in LB medium for 4 hr. Approximately 56.6% of the population falls into the reporter ‘on’ population. (e) Example of gating for ‘on’ cells from wild type PA14 pPcdrA::gfpASV cells that had been attached to glass in LB medium for 4 hr prior to FACS sorting. Approximately 12.8% of the population falls into the reporter ‘on’ population. (f) Example of gating for ‘on’ cells from wild type PA14 pPcdrA::gfpASV cells that had been attached to glass in Jensen’s media (a condition in which Pel is more abundantly produced than in LB) for 4 hr. Approximately 31.9% of the population falls into the reporter ‘on’ population.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** Wild type PAO1 and PAO1 mutants harboring the pPsiaA::gfp reporter (or the pPcdrA::gfp reporter as controls) were grown for 20 hr on an LB agar surface with 100 μg/mL gentamycin, resuspended in PBS, and their GFP fluorescence and absorbance at OD600 was measured immediately in a spectrophotometer. Data are normalized to reporter activity of the wild type PAO1 strain. Asterisk indicates a statistically significant difference in pPsiaA::gfp reporter activity relative to wild type PAO1 (p<0.05, N = 6, ANOVA with post-hoc Dunnett).

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** Brackets indicate gates for polysaccharide-producing, TRITC lectin bound cells (TRITC above 103 RFU) or cells without lectin bound (TRITC below 103 RFU) on an LSR II flow cytometer and numbers above the brackets indicate the percentage of total cells that fall within the gate. (a) Determination of the background level of TRITC autofluorescence in wild type PAO1 that had not been stained with a TRITC-conjugated lectin. (b) Determination of the a high level of TRITC-conjugated Psl-specific lectin binding in PAO1 PBAD-psl grown in shaken liquid culture for 4 hr with 1% arabinose before staining with the TRITC-HHA lectin and extensive washing. Approximately 60% of the cells have TRITC-HHA lectin bound to their surface. (c) Determination of the a high level of TRITC-conjugated Pel-specific lectin binding in PAO1 PBAD-pel grown in shaken liquid culture for 4 hr with 1% arabinose before staining with the TRITC-WFL lectin and extensive washing. Approximately 18.1% of the cells have TRITC-HHA lectin bound to their surface. (d) A scatterplot of pPcdrA::gfpASV reporter activity (GFP) on the x axis and Psl production (as measured by binding of TRITC-HHA lectin to the cell surface) demonstrating the specificity of GFP and TRITC gating in a negative control condition. Wild type PAO1 cells that do not contain the reporter and had not been stained with lectin mostly fall into the lower left quadrant of ‘off’ GFP and no TRITC-lectin binding. The purple numbers in each quadrant represent the percentage of the total population that falls within that quadrant. Quadrants were drawn based on gating of pPcdrA::gfpASV reporter activity ‘on’ vs. ‘off’ and lectin bound vs. unbound. (e) Psl polysaccharide production is enriched in the population of cells with high c-di-GMP. Representative scatterplot of reporter activity versus Psl lectin binding in wild type PAO1 harboring the pPcdrA::gfpASV reporter grown for four hours in LB before surface attached cells were harvested, lectin stained, washed, and counted by flow cytometry. (f) Pel polysaccharide production is enriched in the population of cells with high c-di-GMP. Representative scatterplot of reporter activity versus Pel lectin binding in wild type PA14 harboring the pPcdrA::gfpASV reporter grown for four hours in Jensen’s minimal media plus glucose before surface attached cells were harvested, lectin stained, washed, and counted by flow cytometry.

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp8-v2.jpg)

**Figure 1—figure supplement 8.:** Brackets indicate gates for ‘on’ (GFP above 1.1 × 102 RFU) or ‘off’ (GFP below 102 RFU) reporter cells on a BD Aria III flow cytometer and the number above the bracket indicates the percentage of cells that fall within that gate. (a) Wild type PAO1 cells were used to determine the background level of fluorescence on the BD Aria III for GFP measurements. The population of cells centers around zero RFU. (b) A P. aeruginosa strain constitutively expressing stable GFP (PAO1 Tn7::P(A1/04/03)::GFPmut) was used to determine gating for cells with high GFP, with the population centering around 103 RFU. (c) PAO1 ΔwspFΔpelΔpsl harboring the pPcdrA::gfpASV was used to draw a gate for collection of cells with high reporter activity (80% of the population). (d) Example of gating for reporter ‘off’ and ‘on’ cells from wild type PAO1 pPcdrA::gfpASV cells that had been grown on a surface for 4 hr prior to FACS sorting. Approximately 30% of the population falls into the reporter ‘on’ population. A gap was left between the sorted ‘off’ and ‘on’ populations to increase the stringency of the sorting. (e) Example of the ‘off’ and ‘on’ gates drawn on wild type PAO1 pPcdrA::gfpASV cells that were grown planktonically to mid-log, demonstrating that the surface dependent nature of PcdrA reporter activity can be detected by flow cytometry.

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig1-figsupp9-v2.jpg)

**Figure 1—figure supplement 9.:** A strain that does not produce Psl, PAO1 ΔwspF Δpel Δpsl, was grown for four hours in LB before cells were harvested, lectin stained, washed, and counted by flow cytometry. Using the same gates as determined in Figure 1—figure supplements 8b 1.14% of cells were misclassified as producing Psl.

### The PcdrA::gfp reporter suggests heterogeneity in c-di-GMP levels during surface sensing

Next, we sought to visualize early c-di-GMP signaling events at the single cell level. To this end we used a plasmid-based, c-di-GMP responsive transcriptional reporter, pPcdrA::gfpASV (Rybtke et al., 2012) in two commonly-studied P. aeruginosa strains, PAO1 and PA14. Planktonic cells (a condition where the reporter is inactive due to low c-di-GMP levels) were used to inoculate flow cell chambers. We imaged individual cells of each reporter strain hourly for up to 6 hr after surface attachment (Figure 1B and Figure 1—figure supplement 2). As expected, we saw minimal GFP fluorescence at the 0 hr time point (right after surface attachment). However, by 1 hr, the reporter was activated in a subset of surface attached cells, as defined by background subtracted GFP fluorescence ≥321 fluorescence units (referred to as reporter ‘on’ subpopulations). Interestingly, between 4 and 6 hr post inoculation, we consistently observed that the c-di-GMP reporter was only active in a subset of cells in both strains (Figure 1C). In PA14, the reporter was activated in 10% of the population over 6 hr, whereas PAO1 displayed greater reporter activity, with 40–60% of the cells displaying reporter activity through 12 hr (Figure 1B). An analysis of single cell fluorescence supported these observations. We plotted each cell’s individual fluorescence values over time and observed populations of cells with low and high c-di-GMP reporter activity at each timepoint after the 0 hr (Figure 1—figure supplement 3). We also observed long tails of high GFP fluorescence, particularly at 2 and 4 hr. This suggests that the reporter ‘on’ subpopulation represents cells with a range of high c-di-GMP levels. This wide range of high reporter activity cells between 2 and 4 hr could be indicative of an early ‘spike’ in c-di-GMP production that levels off over time (Figure 1—figure supplement 3).

We next examined the change in distribution of fluorescence intensity over time for single cells by bootstrap sampling of the single cell fluorescence intensity values (Figure 1—figure supplement 4). The purpose of this bootstrapping analysis is to examine whether the distributions of fluorescence intensity differ at each time point. We found that the median fluorescence intensity was significantly different at every time point except between 4 and 6 hr, and between 8, 10, and 12 hr (Figure 1—source data 2). Together, these single cell analyses support a model in which c-di-GMP signaling is initiated rapidly upon surface attachment in the first 4–6 hr for a subpopulation of attached cells, while the rate of c-di-GMP increase tends to level off at later timepoints.

We confirmed the microscopy results from comparing PAO1 and PA14 reporter fluorescence using flow cytometry to assess the proportion of attached cells that were fluorescent (Figure 1—figure supplement 5D, E). To be sure that the promoter of cdrA is representative of c-di-GMP-regulated gene expression, we replaced PcdrA with the promoter of siaA, a gene that is also highly expressed under conditions of elevated c-di-GMP (Starkey et al., 2009; Baraquet and Harwood, 2016). We found that pPsiaA::gfpASV reporter activity resembled that of pPcdrA::gfpASV in response to a surface (Figure 1—figure supplement 6). Thus, reporter activity is indeed linked to cellular levels of c-di-GMP.

### Cyclic di-GMP heterogeneity leads to phenotypic diversification at early stages of biofilm formation

We then wanted to confirm that subpopulations of surface-attached P. aeruginosa cells with high and low c-di-GMP reporter activity are truly physiologically distinct from one another. We used TRITC-labeled lectins to stain for two c-di-GMP-induced exopolysaccharides, Psl and Pel (Zhao et al., 2013; Jennings et al., 2015), the presence of which is indicative of biofilm formation by PAO1 and PA14, respectively. After 4 hr of attachment to glass, we observed an enrichment of TRITC-conjugated lectin staining in the population of cells with high c-di-GMP reporter activity (Figure 1D and Figure 1—figure supplement 7), demonstrating that the subpopulation of cells with high c-di-GMP is producing more exopolysaccharide than their low c-di-GMP counterparts. This correlation was weaker for Psl than Pel, probably due to the fact planktonic populations can make low levels of Psl (though not the case for Pel) (Wei and Ma, 2013). As a complementary approach, we separated 4 hr surface-grown cells of the reporter strain into reporter ‘on’ and ‘off’ subpopulations using flow-assisted cell sorting (FACS; Figure 1—figure supplements 8 and 9). We then applied qRT-PCR to compare Pel and Psl transcript levels in these two populations. Both the pel and psl operon transcripts were elevated in the reporter ‘on’ subpopulation, relative to the reporter ‘off’ subpopulation (Figure 1E). These data support that, with respect to c-di-GMP signaling, there are at least two distinct subpopulations that arise shortly after surface attachment.

### The Wsp system is required for surface sensing

We next evaluated the relative contributions of the Wsp and Pil-Chp surface sensing systems to surface-induced c-di-GMP production. Strains with mutations in the Pil-Chp chemosensory system were not significantly defective in surface sensing activity. Deletion of the diguanylate cyclase activated through the Pil-Chp system (PAO1 ΔsadC) and the gene encoding the putative sensor PilY1 (PAO1 ΔpilY1) did not significantly influence reporter activity in response to a surface (Figure 2—figure supplement 1A,B). Whereas both the SadC and PilY1 mutants displayed wild type levels of reporter activity, a mutant lacking the main Type IV pilus filament protein (PAO1 ΔpilA) did show a statistically significant defect in reporter activity by 6 hr (Figure 2—figure supplement 1B; p<0.05 by T-test). We then mutated the c-di-GMP cyclase gene, wspR, to inactivate the Wsp system. In addition, we deleted the gene encoding the methylesterase wspF, which locks the system into the active state, regardless of whether cells are surface-associated. We found that the PAO1 ΔwspR strain exhibited extremely low levels of reporter activity during the first 6 hr after surface attachment (Figure 2A and Figure 2—figure supplement 2). Complementation of PAO1 ΔwspR restored wild type levels of activity at all time points (Figure 2—figure supplement 3). As expected, PAO1 ΔwspF had a high proportion of reporter active cells (Figure 2A). We repeated these experiments in the lab strain PA14 and saw a similar trend for Wsp mutants (Figure 2—figure supplement 4). Kulesekara et al. (Kulasekara et al., 2013) used a FRET-based c-di-GMP reporter to show that planktonic P. aeruginosa has heterogeneous, albeit very low, concentrations of c-di-GMP which it achieves through assymetrical partitioning of a phosphodiesterase (PA5017, also called Pch or DipA) to the flagellated cell pole during cell division. However, we found no evidence of heterogeneity in c-di-GMP within the planktonic cell inoculum contributing to our observations. We ruled out the phosphodiesterase (PA5017) as responsible for the heterogeneity we see during surface sensing by examining a deletion mutant of PA5017 and showing that this strain still exhibited heterogeneity during surface sensing (Figure 2—figure supplement 5).

![Figure 2.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig2-v2.jpg)

**Figure 2.:** (A) The Wsp system is required for activation of the pPcdrA::gfpASV reporter during surface sensing. Six hour time course plot of the average percentage of surface-attached cells from either wild type PAO1 (green), PAO1 ΔwspR (red), or PAO1 ΔwspF (black) in which the pPcdrA::gfpASV reporter had turned ‘on’ at each hour. Cells were identified as ‘on’ if their average GFP fluorescence was greater than twice the average background GFP fluorescence of the image. Error bars = standard deviation. N ≥ 3 biological replicates. See Figure 2—figure supplement 1 for the same timecourse using mutants in the Pil-Chp surface sensing system. Figure 2—figure supplement 2 shows representative images from Figure 2A. Figure 2—figure supplement 3 shows that complementing the wspR mutant restores wild type levels of reporter activity. Figure 2—figure supplement 4 shows that the lab strain PA14 also displays Wsp-dependent c-di-GMP heterogeneity. Figure 2—figure supplement 5 shows that PA5017 (Pch) is not required for heterogeneity during surface sensing. (B) Laterally attached cells have higher c-di-GMP levels than polarly attached cells. Five hour time course plot depicting, on the left axis, the percentage of pPcdrA::gfpASV reporter ‘on’ cells that were either polarly (blue) or laterally (red) attached to the surface of a glass coverslip in a flow cell at each hour. The right axis depicts the total number of polar (green) and laterally attached (purple) cells at each time point. Cells were identified as pPcdrA:gfpASV reporter ‘on’ if their average GFP fluorescence was greater than 321 fluorescence units. Error bars = standard deviation. N = 4 biological replicates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Representative images from wild type PAO1, PAO1 ΔsadC, PAO1 ΔpilY1, and PAO1 ΔpilA after 6 hr of surface attachment. bf = bright field, merge = bright field and GFP channels combined. (b) Six hour time course plot of the average percentage of cells from either wild type PAO1 (green), PAO1 ΔsadC (red), PAO1 ΔpilY1 (black), or PAO1 ΔpilA (blue) in which the pPcdrA::gfpASV reporter had turned ‘on’ at each hour. PAO1 ΔpilA is significantly different from wild type PAO1 from 2 to 6 hr (T-test, p<0.05). Cells were identified as ‘on’ if their average GFP fluorescence was greater than twice the average background GFP fluorescence of the image. Plotted values are the mean of at least three biological replicates and error bars are standard deviation.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Representative images from wild type PAO1, PAO1 ΔwspR, and PAO1 ΔwspFΔpelCΔpslD after 6 hr of surface attachment. bf = bright field, merge = bright field and GFP channels combined.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** PAO1 ΔwspR and PAO1 ΔsadC were complemented at a neutral site on the chromosome under control of their native promoters. (a) Representative images from wild type PAO1, PAO1 ΔwspR attCTX::wspR (ΔwspR::wspR), and PAO1 ΔsadC Tn7::sadC (PAO1 ΔsadC::sadC) after 6 hr of surface attachment. bf = bright field, merge = bright field and GFP channels combined. (b) Six hour time course plot of the average percentage of cells from either wild type PAO1 (green), PAO1 ΔwspR attCTX::wspR (blue), or PAO1 ΔsadC Tn7::sadC in which the pPcdrA::gfpASV reporter had turned ‘on’ at each hour. Cells were identified as ‘on’ if their average GFP fluorescence was greater than twice the average background GFP fluorescence of the image. Error bars = standard deviation, n ≥ 3 biological replicates.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (a) Representative images from wild type PA14, PA14 ΔwspR, and PA14 ΔwspF after 6 hr of surface attachment. bf = bright field, merge = bright field and GFP channels combined. (b) Six hour time course plot of the average percentage of cells from either wild type PA14 (green), PA14 ΔwspR (red), or PA14 ΔwspF (black) in which the pPcdrA::gfpASV reporter had turned ‘on’ at each hour. Cells were identified as ‘on’ if their average GFP fluorescence was greater than twice the average background GFP fluorescence of the image. Error bars = standard deviation, n ≥ 3 biological replicates.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig2-figsupp5-v2.jpg)

Since the Pil-Chp surface sensing apparatus is polarly localized and the Wsp system is localized laterally along the length of the cell body, we examined whether reporter activity correlated with polar versus lateral attachment to the surface. We found that reporter activity was very low in polarly attached cells, while cells attached along the entire length of the cell body displayed a higher proportion of reporter-activated cells at that same time point (Figure 2B). (Our analysis does not account for the time period each cell spends in either the polarly or non-polarly attached states.) This finding is consistent with the localization of the Wsp system and its role for early c-di-GMP signaling during surface sensing.

### Heterogeneity in c-di-GMP levels among cells correlates with Wsp system activity

The specific activity of purified WspR increases as a function of WspR concentration when the protein is treated with beryllium fluoride to mimic phosphorylation, supporting the idea that formation of subcellular clusters of WspR-P potentiates its diguanylate cyclase activity and leads to elevated c-di-GMP (Huangyutitham et al., 2013). Fewer than 1% of wild-type cells grown in broth have a visible WspR-YFP cluster. However, after a short period of growth on an agar surface, WspR-YFP clusters were visible in 30–40% of wild type PAO1 cells, and this is dependent on sensing by the membrane-bound protein WspA, which is laterally distributed in cells (Kuchma et al., 2010). To directly link WspR cluster formation with diguanylate cyclase activity at the cellular level and with surface sensing, we constructed a version of the c-di-GMP reporter that expresses mTFP1 instead of GFP (pPcdrA::mTFP1) to avoid the issue of spectral overlap with WspR-YFP. We monitored reporter activity in two point mutants of WspR (L170D and E253A) that are driven by an inducible promoter, translationally fused to eYFP, and have been previously shown to form large subcellular WspR clusters in a higher percentage of cells than wild-type WspR. The WspR[L170D] protein is highly active for c-di-GMP production, and it forms subcellular clusters in about 75% of agar surface-grown cells. A WspR[E253A] point mutation abolishes diguanylate cyclase activity, but this protein still forms clusters in about 70% of surface-grown cells (Huangyutitham et al., 2013). As expected, in the presence of inducer, we observed a large increase in c-di-GMP reporter activity in WspR[L170D], but not WspR[E253A] (Figure 3A,B). We then asked whether the heterogeneity in reporter activity in response to surface attachment correlates with WspR clustering in the WspR[L170D] strain. We found that pPcdrA::mTFP1 activity was significantly higher in cells with at least one subcellular WspR-eYFP focus in the WspR[L170D] strain compared to cells without a WspR-eYFP focus (Figure 3C and Figure 3—figure supplement 1). These data indicate that the heterogeneity observed in c-di-GMP signaling after surface attachment is due to the heterogeneity in the activity of the Wsp system, as reflected by subcellular clustering of active WspR-P.

![Figure 3.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig3-v2.jpg)

**Figure 3.:** (A) The pPcdrA::mTFP1 reporter is active in surface grown cells with functional, arabinose-inducible alleles of WspR when arabinose is added to the media. Wild type WspR represents the strain PAO1 ΔwspR attCTX::wspR-eYFP. wspR[L170D] represents the strain PAO1 ΔwspR attCTX::wspR[L170D]-eYFP, which produces large subcellular clusters of WspR and grows as rugose small colonies on LB with 1% arabinose, a phenotype that is indicative of high intracellular c-di-GMP. wspR[E253A] represents the strain PAO1 ΔwspR attCTX::wspR[L170D]-eYFP cells, which forms large subcellular WspR clusters, but does not produce c-di-GMP via WspR due to the point mutation located in its active site. Cells were grown on LB agar plates with 100 μg/mL gentamicin, and in the presence or absence of 1% arabinose. Cells were resuspended in PBS and mTFP1 fluorescence and OD600 were measured. Relative pPcdrA::mTFP1 reporter activity is the level of mTFP1 fluorescence normalized to OD600. Asterisk indicates statistical significance by Student’s t-test (p<0.001) in six technical replicates. Error bars = standard deviation. (B) The pPcdrA::mTFP1 reporter displays heterogeneity in a strain with a functional WspR (wspR[L170D]) and is consistently dark in a strain with inactive WspR. Histogram displaying the distribution of average cellular levels of mTFP1 fluorescence from expression of the pPcdrA::mTFP1 reporter in either the PAO1 ΔwspR attCTX::wspR[L170D]-eYFP (blue) or PAO1 ΔwspR attCTX::wspR[E253A]-eYFP (red) backgrounds. (C) Cells with subcellular clusters of functional WspR have higher levels of c-di-GMP reporter activity than cells without a WspR focus or cells without a functional WspR. L170D refers to a point mutant in WspR that forms large subcellular clusters and retains diguanylate cyclase activity: WspR[L170D]-eYFP in the strain PAO1 ΔwspR attCTX::wspR[L170D]-eYFP. E253A refers to a point mutant in WspR that forms large subcellular clusters but does not retain diguanylate cyclase activity: WspR[E253A]-eYFP in the strain PAO1 ΔwspR attCTX::wspR[E253A]-eYFP. Asterisk indicates statistical significance by Student’s t-test (p<0.001) in four replicates, n.s. = not significant. Error bars = standard deviation. See Figure 3—figure supplement 1 for a representative image of WspR[L170D]-eYFP foci.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Cells with visible subcellulars clusters of WspR[L170D]-eYFP (strain PAO1 ΔwspR attCTX::wspR[L170D]-eYFP) also have high levels of c-di-GMP reporter activity. bf, bright field; YFP, wspR-YFP foci; mTFP1 = pPcdrA::mTFP1 activity; and merge, merged YFP and TFP channels. PAO1 ΔwspR attCTX::wspR[L170D]-eYFP cells harboring the pPcdrA::mTFP1 reporter were grown on LB agar plates with 1% arabinose and 100 μg/mL gentamicin, then spotted onto an agar pad and imaged immediately.

For phenotypic heterogeneity to represent a division of labor, it must result in a fitness benefit to the population. Therefore, we next asked whether the observed heterogeneity in c-di-GMP signaling in response to a surface has a meaningful influence on biofilm formation. This was particularly important since previously published results indicated that a wspR mutation had only a small impact on biofilm production (Kulasakara et al., 2006). However, these studies assessed biofilm formation at later stages of biofilm growth that were well beyond initial surface attachment. Therefore, we chose to compare a wspR mutant to wild type at earlier biofilm stages. We performed in vitro biofilm assays and observed that a PAO1 ΔwspR mutant was defective for biofilm formation relative to wild type PAO1 at 2, 4, and 6 hr post-attachment (Figure 4A). However, at later stages of development (24 hr), the wspR mutant caught up and produced similar amounts of biofilm biomass relative to wild type . Complementation of the ΔwspR strain in trans restored wild type levels of biofilm formation at all time points (Figure 4A). These data suggest that the Wsp system rapidly responds to surface contact to generate elevated levels of c-di-GMP in a subpopulation of cells, which accelerates biofilm production. Given the importance of c-di-GMP signaling in biofilm production, the fact that the ΔwspR strain can ultimately attain wild-type levels of biofilm biomass suggests that one of the many other known c-di-GMP cyclases present in P. aeruginosa may ultimately compensate for c-di-GMP production in the absence of WspR.

![Figure 4.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig4-v2.jpg)

**Figure 4.:** (A) The Wsp surface sensing system is involved in the early stages of biofilm formation in PAO1. Static biofilm assay performed in wild type PAO1, a single deletion mutant of wspR, and the PAO1 ΔwspR mutant complemented with wspR. Between 4 and 6 hr, PAO1 ΔwspR shows a defect in surface attachment and biofilm formation relative to the wild type. However, after 24 hr, PAO1 ΔwspR formed equal biofilm biomass compared to wild type. Plotted values are the mean of 6 technical replicates and error is standard deviation. Asterisk indicates a statistically significant change in biomass relative to wild type PAO1 at each time point (Student’s t test; p<0.05). (B) Plot of Ic-di-GMP vs Fmotile for individual wild type PAO1 families. Ic-di-GMP is the relative normalized c-di-GMP reporter intensity averaged across all members of a family. Fmotile is the fraction of time that cells in a family are motile (specifically surface translational motility). Each circle represents an individual family (N = 35) with at least four tracked generations. Solid lines represent the 95% probability bounds and dashed lines represent the 50% probability bounds, calculated via kernel density estimation. Spearman correlation: ρ = −0.53, p=0.0012. (C) Plot of Ic-di-GMP vs tree asymmetry λ for individual wild type PAO1 families. Colored numbers indicate the same three families from (B) and (D). Tree asymmetry λ quantifies the detachment behavior of family trees as follows. λ = 0 corresponds to ideal trees with purely ‘two-legged’ division-branching, when both daughter cells remain attached to the surface. λ = 1 corresponds to ideal trees with purely ‘one-legged’ division-branching when one daughter cell detaches or travels outside the field of view. Points here are the same families as in (B). Solid lines represent the 95% probability bounds and dashed lines represent the 50% probability bounds, calculated via kernel density estimation. Spearman correlation: ρ = −0.45, p=0.0068. (D) Family trees of the same three representative wild type PAO1 families indicated in (B) and (C). Time 0 hr is the start of the dataset recording. Lengths of horizontal lines on the plots are proportional to time spent in each generation. Horizontal lines that end with arrows are detachment events, lines that intersect with a vertical line are division events, and lines that end without a marker are out-of-bound events where we lose track of the bacterium (moving out of the field of view or reaching the end of the recording; represented as moving outside the XYT limits of the dataset boundaries). Vertical lines are arbitrarily spaced to show all the descendants. Colors represent the families in (B) and (C). (E) Spatial trajectories of the three representative families. Asterisks (*) represent the initial location of the founder cell. Scale bar 10 μm. The families are color coded as in the previous panels.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Plot of Ic-di-GMP vs Fmotile for individual ΔwspR families. Each marker represents an individual family (N = 10) with at least four tracked generations. Solid (dashed) lines represent the 95% (50%) probability bounds calculated via kernel density estimation. Spearman correlation: ρ = −0.078, p=0.84. (B) Plot of Ic-di-GMP vs tree asymmetry λ for the same families as in (A). Spearman correlation: ρ = −0.32, p=0.37.

### Cyclic di-GMP heterogeneity leads to diversification in surface exploration at the lineage level

We hypothesized that heterogeneity in c-di-GMP signaling dictated by the Wsp complex could impact the surface behavior of the two observed subpopulations. We predicted that the subpopulation of cells with high c-di-GMP after surface attachment would produce biofilm matrix exopolysaccharides and contribute to initial microcolony formation, while the cells with low c-di-GMP would exhibit increased surface motility and detachment, which is known to be inhibited by exopolysaccharide production. To test this hypothesis, we tracked both reporter activity and surface behavior for cells within a single field of view for 40 hr. From our single-cell tracking data, we generated family trees across at least four generations of cells, using a previously described technique (Lee et al., 2018). We tracked the time-averaged PcdrA::gfpASV reporter activity (Ic-di-GMP), surface motility behavior (Fmotile, defined as the fraction of time that cells are motile), and detachment behavior (tree asymmetry λ, where λ = 0 represents both daughter cells remaining attached to the surface and λ = 1 represents when one daughter cell detaches or travels outside the field of view).

In P. aeruginosa, surface exploration is mainly accomplished by type IV pili-mediated twitching motility, and does not appear to be influenced by levels of intracellular c-di-GMP when analyzing single cells (Ribbe et al., 2017). Interestingly, when analyzing correlations between c-di-GMP and motility for entire lineages in family trees, we found clear inverse correlations between Ic-di-GMP and Fmotile (Figure 4B, ρ = −0.53, p=0.0012) and between Ic-di-GMP and λ (Figure 4C, ρ = −0.45, p=0.0068), suggesting that c-di-GMP levels are strongly inversely correlated with surface motility behavior and detachment behavior over multiple generation of cells. Analyzing these correlations across multiple cell divisions is important because it tells us when and how bacteria respond to c-di-GMP signaling events in terms of their surface motility and detachment. When looking at correlations between c-di-GMP and surface motility, the time between seeing a signaling event (i.e., rise or drop in reporter fluorescence intensity) and seeing a response (i.e., change in motility) can span a broad range (from a few minutes to well over a cell division time). Using a cell’s entire lineage history (i.e., tracking daughter cells across cell divisions) will capture all of these events, whereas using single cell history (i.e., within one generation) will only capture a portion of them. For example, this lineage-level tracking of the influence of signaling events on bacterial behavior was recently shown for correlations between cyclic AMP signaling and P. aeruginosa surface motility (Lee et al., 2018). In this study, Lee et al. found that correlations between cell motility and signaling activity were stronger when they took into account lineage history, rather than using single cell history. However, if there are enough instances where the time between a signaling event and a cell’s corresponding behavioral response are within a single generation, then correlations can still be found when using single cell history. For wild type PAO1 (WT), we observe weaker correlations when looking at individual cells in these lineages. Ic-di-GMP vs Fmotile for single cells had a Spearman correlation value ρ = −0.40 (p<0.0001), which is smaller than the lineage-level correlation value, suggesting that lineage-level correlations are stronger.

To illustrate these correlations, we chose three representative families, with either high, intermediate, or low Ic-di-GMP and plotted their family trees (Figure 4D) and spatial trajectories (Figure 4E). Families with the highest Ic-di-GMP had the lowest Fmotile and λ (Family 1, Figure 4B–E). In these families, daughter cells remained attached following cell division, exhibited continuously elevated c-di-GMP, did not move appreciable distances on the surface, and ultimately produced small microcolonies. In contrast, families of cells with low Ic-di-GMP had the highest Fmotile and λ. For these families, daughter cells frequently detached or traveled outside the field of view, had lower c-di-GMP levels, traveled larger distances on the surface, and ultimately did not form microcolonies (Family 3, Figure 4B–E).

Tracking and lineage analyses were also performed on a PAO1 mutant with the Wsp system inactivated (PAO1 ΔwspR). We observed that the range of tree asymmetry values is like that of WT and that the ΔwspR mutant eventually reaches WT c-di-GMP levels despite initially being lower, which is consistent with the observation that the mutant eventually forms WT-like biofilms. What our analysis revealed about the ΔwspR strain was quite unexpected: The WspR mutant has overall lower surface motility and, importantly, lacks correlations between c-di-GMP, surface motility, and detachment behavior (both at the level of lineages and at the level of single cells). For single cell surface motility, 23% of ΔwspR mutant cells (48 of 210 cells) have non-zero Fmotile (the metric for surface motility) compared to 44% of WT cells (251 of 565 cells; Figure 4—figure supplement 1). The overall lowered surface motility and the lack of correlations between c-di-GMP and surface motility in the ΔwspR mutant suggest that the Wsp system is involved in translating the heterogeneous c-di-GMP signaling events into the corresponding motility-related responses for cells and their progeny. Therefore, the Wsp system’s multi-generational temporal propagation of surface sensing signaling and behavior is important for the generation of heterogeneous populations of surface motile and immotile cells during early biofilm formation.

### Use of an optogenetic reporter to control bacterial surface behavior at the single-cell level

One important question is what happens to early biofilm development if we were to effectively remove heterogeneity in c-di-GMP output rooted in the WspR surface sensing system. To address this question, we used a strain in which c-di-GMP production could be easily controlled using an optogenetic system. The precise control of c-di-GMP expression in individual cells was made possible by the use of a chimeric protein that fused a diguanylate cyclase domain to a bacteriophytochrome domain. Flow chambers were seeded with the optogenetic strain encoding a heme oxygenase (bphO) and light-responsive diguanylate cyclase (bphS) (Ryu and Gomelsky, 2014). We initially characterized the optogentic strain and verified the reporter activity increased with exposure of the optogentic strain to red light (Figure 5—figure supplement 1) and that the laser light did not impact growth or motility (data not shown). Following validation of the strain, cells inoculated on a glass surface were tracked and continuously stimulated with red-light over ~8 hr using adaptive tracking illumination microscopy (ATIM), which allows for precise stimulation of the initial attached cells and their offspring and ensures sustained intracellular c-di-GMP production for a fixed number of surface cell generations (Figure 5—figure supplement 2). Cellular lineages (a cell and all of its offspring) and c-di-GMP reporter activity were continually monitored for at least 12 hr. Families that were not stimulated with light demonstrated a heterogeneous surface response (Video 1 and Figure 5B,D) similar to that of Families 1–3 in Figure 4B–E. Some lineages were dominated by surface explorers, whereas others were seen to commit to microcolony formation. In contrast, in families stimulated with light for more than one generation, the resulting c-di-GMP production artificially forced lineages to have low surface motility and commit to microcolony production (Video 1 and Figure 5A,C) similar to that of Family one in Figure 4B–E. Families stimulated with light in this manner had higher Ic-di-GMP and lower λ values than those that were not stimulated (Figure 5—figure supplement 3). We also found that optogenetic control of c-di-GMP results in phenotypes that are consistent with the wild-type behavior presented in Figure 4, with illuminated cells (high c-di-GMP) displaying the least motility and control (non-illuminated) cells displaying comparatively greater surface motility (Figure 5—figure supplement 3). Interestingly, families stimulated with light for one generation or less are not significantly different from un-illuminated controls (data not shown). Our data show that the generation of c-di-GMP can deterministically lead to the creation of an entire lineage of sessile cells with post-division surface persistence, low motility, and initiation of microcolony formation. Altogether, these results show that c-di-GMP levels, surface motility, and detachment are inversely correlated at the lineage level, and that the time scale for this occurs over multiple generations.

![Figure 5.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig5-v2.jpg)

**Figure 5.:** (A,B) Spatiotemporal plot of 3 illuminated families (A) and three control families (B). The individual cell tracks in the 3D plot are projected onto the XY plane as spatial trajectories. As in Figure 4, λ is a measure of tree asymmetry, with higher values indicating more cells traveling outside the field of view or detaching. In A, the illuminated families tend to be sessile, as expected for cells with high c-di-GMP. In B, control cells are more motile than the illuminated cells in A. (C,D) Family trees of a single corresponding family in (A) and (B), where the color corresponds to the same family. Illuminated cells (C) tend to stay adhered across multiple generations, whereas control cells (D) display more surface motility and detachments. See Video 1 for a representative video of the optogenetic reporter experiment. Figure 5—figure supplement 1 is a control experiment showing that c-di-GMP levels increase in response to red light intensity in the optogenetic reporter strain. Figure 5—figure supplement 2 shows a schematic of the ATIM apparatus. See Figure 5—figure supplement 3 for the data from Figure 5 overlayed onto Figure 4C, showing that ptogenetic-controlled families follow the trend of family behavior observed in wt PAO1 cells.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** FG/FR refers to the ratio of GFP fluorescence (reporter activity) over mCherry fluorescence (constitutive fluorescence). Density refers to the intensity of red light illumination. The strains PAO1-bphS -PcdrA-GFP-mCherry were grown on an agar pad surface with red light illumination at a range of intensities. We found that c-di-GMP levels had increased approximately 2-fold at 6 hr when strains were illuminated at 0.015 mW/cm2. Error bars represent standard deviation.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (a) Schematic drawing of the ATI system. A high-throughput bacterial tracking algorithm was employed for analyzing cells’ behavior in real time and the information was immediately fed back to an adaptive microscope equipped with a digital micromirror device (DMD). (b) Example depicting one cell of interest being tracked and projected in real time. (c) The feedback illumination can generate projected patterns to exactly follow the daughter cells after the tracked cell divides. Scale bar for all images is 5 μm.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/45084/elife-45084-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Families plotted in Figure 5 (plus one additional control family) are plotted on top of Figure 4C (Ic-di-GMP vs λ). Red triangles and blue triangles represent the illuminated and control families, respectively, while the original data from Figure 4C is grayed out. Illuminated families have higher Ic-di-GMP and lower λ than the control families.

![Video 1.](https://cdn.elifesciences.org/articles/45084/elife-45084-video1.mp4.jpg)

**Video 1.:** The left panel shows the merged images of gfpASV and mCherry fluorescence microscopy images over time. The right panel shows the merged images of red LED projected patterns and bright field images corresponding to the left panel. The fluorescence intensity of gfpASV in the illuminated cells and their offspring (colored red in right panel) is significantly increased after using ATI for 460 mins. In contrast, the gfpASV fluorescence intensity of the un-illuminated cells remains low and these cells remain motile.

## Discussion

Collectively, our data show that heterogeneity in cellular levels of c-di-GMP generated by the Wsp system in response to surface sensing, leads to two physiologically distinct subpopulations that each contribute to surface colonization. Phenotypic heterogeneity of single cells is a common phenomenon in bacteria that can be beneficial at the population level by allowing a single genotype to survive sudden environmental changes. Sources of phenotypic heterogeneity among genetically homogeneous populations include bistability (Dubnau and Losick, 2006) and stochasticity (Elowitz et al., 2002) of gene expression, unequal partitioning of proteins during cell division due to low abundance (Elowitz et al., 2002), epigenetic modifications resulting in phase variation (Casadesús and Low, 2006), or through asymmetrical cell division (Kulasekara et al., 2013; Laventie et al., 2019). In this study, we show that the Wsp system generates heterogeneity in c-di-GMP signaling, and it is never fully activated in 100% of wild-type, surface-attached cells. One possible outcome of phenotypic heterogeneity is a division of labor between costly behaviors that support the growth and survival of the population (Ackermann, 2015). We found that abolishing c-di-GMP heterogeneity through inactivation of WspR leads to defects in early biofilm formation. This suggests that the subpopulations of high c-di-GMP, polysaccharide producers and low c-di-GMP, surface explorers are both required for efficient biofilm formation and that they represent a division of labor during early biofilm formation.

The data show that Wsp-generated c-di-GMP heterogeneity results in phenotypic changes for entire family lineages of cells. It is interesting that correlations between c-di-GMP, surface motility, and surface detachment probability are stronger when considered for an entire lineage in a bacterial family tree, but weaker when considered at the individual cell level. We think that this difference in the strength of correlations between c-di-GMP and bacterial behavior at the lineage versus single cell level is biologically meaningful and likely reflects the complex relationship between c-di-GMP signaling and type IV pili-mediated motility (Ribbe et al., 2017; Jain et al., 2012; Jain et al., 2017). The time between initiation of a signaling event (i.e., increased intracellular c-di-GMP) and the associated response (i.e., attenuation of motility or initiation of polysaccharide production) can span a large range, depending on the behavior. When examining polysaccharide production, signal propagation appears to be quick, with high c-di-GMP cells initiating exopolysaccharide production within minutes of P. aeruginosa encountering a surface. However, when examining a different bacterial behavior—surface motility—we found the strongest correlation between c-di-GMP signaling and cellular behavior at the lineage level. For many cells, there was a lag between when c-di-GMP first increased and surface motility decreased. While a mother cell may still be surface motile upon initiating c-di-GMP signaling, we found that following cell division, daughter cells with high c-di-GMP eventually became immotile. Thus, whereas an increase in c-di-GMP relatively quickly results in increased biofilm matrix production, this same increase in c-di-GMP likely indirectly influences surface motility. Supporting this, P. aeruginosa is known to produce Psl polysaccharide while engaging in type IV pili mediated motility across a surface, leaving behind a trail of Psl (Zhao et al., 2013). Finally, this apparent multigenerational influence of c-di-GMP signaling on bacterial behavior resembles the recently observed multigenerational memory of cAMP signaling in P. aeruginosa (Lee et al., 2018). Additional work is needed to determine whether surface-naïve daughter cells have any ‘memory’ of surface attachment by a mother cell, through the maintenance of elevated c-di-GMP across one or more cell divisions. Another future direction of this work is to examine whether other bacterial signaling modalities, including other nucleotide or non-nucleotide signaling systems (e.g. ppGpp or quorum sensing), may exhibit similar multigenerational features.

We observed that the Pil-Chp surface sensing system did not play a role in early c-di-GMP signaling in our experimental system. There are numerous potential explanations for this. For example, it is possible that the Pil-Chp system is the dominant surface sensing mechanism under different environmental conditions than the ones we used for this study. Alternatively, the Pil-Chp system might not contribute to general cytoplasmic pools of c-di-GMP (for which the reporter is sensitive) and instead participates in specific localized c-di-GMP signaling events. In support of this notion, inactivation of individual diguanylate cyclases is well known to lead to distinct changes in c-di-GMP-regulated behaviors (Kulasakara et al., 2006; Merritt et al., 2010). It is interesting to note that whereas the other Pil-Chp inactivation mutants tested did not have a phenotype, the pilA deletion mutant strain displayed a slight defect in surface sensing in our study, although why is currently unknown.

If we overwhelm WspR-generated c-di-GMP heterogeneity by using optogentically-induced sustained c-di-GMP production, we find that phenotypic heterogeneity is lost, and that illuminated cells deterministically become sessile and form microcolonies. Interestingly, our optogenetic experiments show that sustained c-di-GMP production for more than one generation is required before commitment to the sessile lifestyle. This observation is consistent with the fact that we see stronger correlations between c-di-GMP levels and motility behavior at the lineage level compared to the individual cell level. Moreover, since the Wsp surface sensing system generates heterogeneous c-di-GMP levels, this requirement of sustained c-di-GMP production for more than one generation is inherently difficult for wild-type cells to meet, and virtually guarantees the simultaneous existence of motile and sessile subpopulations.

The heterogeneity we observed in Wsp signaling shares many similarities with phenotypic heterogeneity generated from other c-di-GMP signaling (Petersen et al., 2019) and quorum sensing systems (Grote et al., 2015; Ramalho et al., 2016). Nucleotide second messenger and quorum sensing (QS) signaling systems are traditionally thought to coordinate cellular behavior in response to information regarding the cell’s environment. However, rather than functioning to initiate a completely homogeneous response at the population level to environmental conditions, a growing body of literature suggests that a common theme of these signaling systems is that they introduce some level of behavioral heterogeneity (Grote et al., 2015). For example, QS-induced phenotypic heterogeneity in Vibrio harveyi is attributable to variability in the phosphorylation state of LuxO and influences bioluminencence and biofilm formation (Anetzberger et al., 2009). In P. aeruginosa and Caulobacter crescentus, heterogeneity in the very low levels of c-di-GMP present during planktonic growth is achieved through asymmetrical cell division and influences swimming motility (Kulasekara et al., 2013). Thus, P. aeruginosa appears to have at least two distinct mechanisms of generating c-di-GMP heterogeneity, which it employs during different modes of growth. In the case of the Wsp system, this phenotypic heterogeneity, which has been ‘hardwired’ into the structure of the Wsp surface sensing network, allows for a division of the labor during early biofilm formation, with one subpopulation committing to initiating the protective biofilm lifestyle, while the other subpopulation is free to explore the surface and potentially colonize distant, perhaps more favorable, locations.

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
      <td>Strain, strain background (Pseudomonas aeruginosa)</td>
      <td>PAO1</td>
      <td>PMID: 111024</td>
      <td></td>
      <td>The version of PAO1 used in this study can be obtained from Matthew Parsek's laboratory.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pPcdrA::gfpASV</td>
      <td>PMID: 22582064</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PAO1 attCTX::bphS attMiniTn7:: mCherry pPcdrA::gfpASV</td>
      <td>This study</td>
      <td>NA</td>
      <td>This strain can be obtained from Fan Jin's laboratory.</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QuikChange Lightning Site-Directed Mutagenesis Kit</td>
      <td>Agilent Technologies</td>
      <td>210519</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Gateway BP Clonase II Enzyme mix</td>
      <td>ThermoFisher Scientific</td>
      <td>11789020</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>LR Clonase II Plus enzyme</td>
      <td>ThermoFisher Scientific</td>
      <td>12538120</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QIAquick gel extraction kit</td>
      <td>Qiagen</td>
      <td>28115</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QIAquick PCR purification kit</td>
      <td>Qiagen</td>
      <td>28104</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Antarctic phosphatase</td>
      <td>New England BioLabs</td>
      <td>M0289S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TRIzol LS</td>
      <td>ThermoFisher Scientific</td>
      <td>10296010</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RQ1 RNase-Free DNase</td>
      <td>Promega</td>
      <td>M6101</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>iTaq Universal SYBR Green One-Step kit</td>
      <td>Bio-rad</td>
      <td>172–5150</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRITC Conjugated Wisteria floribunda lectin</td>
      <td>EY laboratories</td>
      <td>R-3101–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRITC Conjugated Hippeastrum hybrid Lectin (Amaryllis)</td>
      <td>EY laboratories</td>
      <td>R-8008–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Volocity Image Analysis Software</td>
      <td>Quorum Technologies Inc</td>
      <td>Version 6.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NIS-Elements AR</td>
      <td>Nikon</td>
      <td>Version 4.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB code for tracking experiments</td>
      <td>This study</td>
      <td>Version R2015a</td>
      <td>The code and datasets are available to download as source data files associated with Figures 1, 4 and 5.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Statistics and Machine Learning Toolbox for MATLAB</td>
      <td>MathWorks</td>
      <td>Version R2015a</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Flow cell for time course experiments</td>
      <td>University of Iowa Machine Shop</td>
      <td>Standard dimension flow cell</td>
      <td>Flow cell dimensions: 5 mm x 35 mm x 1 mm</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Flow cell for cell tracking experiments</td>
      <td>PMID: 18770573</td>
      <td>Standard dimension flow cell</td>
      <td>This flow cell can be ordered from Department of Systems Biology, Technical University of Denmark.</td>
    </tr>
  </tbody>
</table>

### Bacterial strains and growth conditions

The strains, plasmids, and primers used in this study are listed in Table 1. Escherichia coli and P. aeruginosa strains were routinely grown in Luria–Bertani (LB) medium and on LB agar at 37°C. For the flow cell experiments, P. aeruginosa was grown in either LB or FAB minimal medium supplemented with 10 mM or 0.6 mM glutamate at room temperature (Zhao et al., 2013). For flow cytometry experiments, P. aeruginosa was grown in either LB medium or in Jensen’s defined medium with glucose as the carbon source (a growth medium in which Pel is more abundantly produced than in LB) (Jennings et al., 2015). For the tube biofilm and c-di-GMP measurements, P. aeruginosa strains were grown in Vogel-Bonner Minimal Medium (VBMM; Vogel and Bonner, 1956). Antibiotics were supplied where necessary at the following concentrations: for E. coli, 100 μg/mL ampicillin, 10 μg/mL gentamicin, and 10 or 60 μg/mL tetracycline; for P. aeruginosa, 300 μg/mL carbenicillin, 100 μg/mL gentamicin, and 100 μg/mL tetracycline. PcdrA::gfpASV reporter and vector control plasmids were selected with 100 µg/mL gentamicin for P. aeruginosa strains and 10 µg/mL gentamicin for E. coli.

**Table 1.**
 Strains, primers, and plasmids used in this study.


<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>P. aeruginosa strains</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>PAO1</td>
      <td>wild-type</td>
      <td>Holloway et al., 1979</td>
    </tr>
    <tr>
      <td>PA14</td>
      <td>wild-type</td>
      <td>Rahme et al., 1997</td>
    </tr>
    <tr>
      <td>PAO1ΔwspF</td>
      <td>markerless, in frame deletion of WspF</td>
      <td>Hickman et al., 2005</td>
    </tr>
    <tr>
      <td>PAO1ΔwspFΔpelAΔpslBCD</td>
      <td>markerless, in frame deletions of WspF, PelA, and PslBCD genes</td>
      <td>Rybtke et al., 2012</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR</td>
      <td>markerless, in frame deletion of WspR</td>
      <td>Hickman, 2005</td>
    </tr>
    <tr>
      <td>PAO1ΔpilY1</td>
      <td>markerless, in frame deletion of PilY1</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔsadC</td>
      <td>markerless, in frame deletion of SadC</td>
      <td>Irie et al., 2012</td>
    </tr>
    <tr>
      <td>PAO1ΔpilA</td>
      <td>markerless, in frame deletion of PilA</td>
      <td>Shrout et al., 2006</td>
    </tr>
    <tr>
      <td>PAO1ΔdipA</td>
      <td>markerless, in frame deletion of DipA</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PwspA::wspR</td>
      <td>PAO1ΔwspR complemented with WspR under control of the Wsp operon promoter and including intergenic region upstream of WspR</td>
      <td>Gift from Yasuhiko Irie</td>
    </tr>
    <tr>
      <td>PAO1ΔsadC attCTX::sadC</td>
      <td>PAO1ΔsadC complemented with SadC under control of its native promoter</td>
      <td>Gift from Yasuhiko Irie</td>
    </tr>
    <tr>
      <td>MPAO1 attTn7::P(A1/04/03)::GFPmut</td>
      <td>wild type MPAO1 constitutively expressive stable GFP</td>
      <td>this sudy</td>
    </tr>
    <tr>
      <td>PA14 ΔwspF</td>
      <td>markerless, in frame deletion of WspF</td>
      <td>Gift from Caroline Harwood</td>
    </tr>
    <tr>
      <td>PA14 ΔwspR</td>
      <td>markerless, in frame deletion of WspR</td>
      <td>Gift from Caroline Harwood</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PBAD-wspR-eYFP</td>
      <td>markerless, in frame deletion of WspR with arabinose-inducible, C-terminally eYFP-tagged wild type WspR allele</td>
      <td>Huangyutitham et al., 2013</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PBAD-wspR[L170D]-eYFP</td>
      <td>markerless, in frame deletion of WspR with arabinose-inducible, C-terminally eYFP-tagged WspR[L170D] allele</td>
      <td>Huangyutitham et al., 2013</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PBAD-wspR[E253A]-eYFP</td>
      <td>markerless, in frame deletion of WspR with arabinose-inducible, C-terminally eYFP-tagged WspR[E253A] allele</td>
      <td>Huangyutitham et al., 2013</td>
    </tr>
    <tr>
      <td>P. aeruginosa reporter strains</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>PAO1 pMH489</td>
      <td></td>
      <td>Rybtke et al., 2012</td>
    </tr>
    <tr>
      <td>PAO1 pPcdrA::gfpASV</td>
      <td></td>
      <td>Rybtke et al., 2012</td>
    </tr>
    <tr>
      <td>PAO1 pPsiaA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14 pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14 pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspF pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspF pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspF pPsiaA::gfp</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspFΔpelCΔpslD pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspFΔpelCΔpslD pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR pPsiaA::gfp</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔpilY1 pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔpilY1 pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔsadC pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔsadC pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔpilA pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔpilA pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔdipA pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔdipA pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PwspA::wspR pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PwspA::wspR pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔsadC att::sadC pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔsadC att::sadC pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14 ΔwspF pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14 ΔwspF pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14 ΔwspR pMH489</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14 ΔwspR pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PBAD-wspR-eYFP pPcdrA::mTFP1</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PBAD-wspR[L170D]-eYFP pPcdrA::mTFP1</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1ΔwspR attCTX::PBAD-wspR[E253A]-eYFP pPcdrA::mTFP1</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1 attCTX:: bphS attMiniTn7::mCherry pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1 attMiniTn7:: mCherry pPcdrA::gfpASV</td>
      <td></td>
      <td>this study</td>
    </tr>
    <tr>
      <td>E. coli strains</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E. coli S17.1 pENTRPEX18Gm::ΔpilY1</td>
      <td>conjugation proficient E. coli harboring pilY1 deletion allele</td>
      <td>Gift from Joe Harrison</td>
    </tr>
    <tr>
      <td>E. coli S17.1 pENTRPEX18Gm::ΔdipA</td>
      <td>conjugation proficient E. coli harboring dipA deletion allele</td>
      <td>Gift from Joe Harrison</td>
    </tr>
    <tr>
      <td>E. coli DH5α pUC18-miniTn7T2-PcdrA-RBSg10L-gfpAGA</td>
      <td>source of PcdrA-RBSg10L</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>E. coli DH5α pBBR1MCS5- PcdrA::RBSg10L::mTFP1</td>
      <td>referred to as ‘pPcdrA::mTFP1’</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>E. coli DH5α pPsiaA::gfp</td>
      <td>plasmid-based, fluorescent siaA transcriptional reporter</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>Primers</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>PAO1pilY1-SEQ-F</td>
      <td>CTACTACGAGACCAATAGCGTC</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1pilY1-SEQ-R</td>
      <td>GTCGATGTCCACCAGGTTCTTC</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1dipA-SEQ-F</td>
      <td>GATACGCTTAACTTGGGCCCTG</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PAO1dipA-SEQ-R</td>
      <td>CTTTTCTTGGTGAGGATTTCAGAAC</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14wspR-SEQ-F</td>
      <td>GCTTCCTCACCATCGCCC</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14wspR-SEQ-R</td>
      <td>CAGGTCGTCCAGGGTTTCC</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14wspF-SEQ-F</td>
      <td>CTCACGGTGCGTGAGCTG</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>PA14wspF-SEQ-R</td>
      <td>GGTCCTGGAGGATCACCG</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>SacI – PcdrA - F</td>
      <td>GGGGAGCTC GTATGGAAGGTTCCTTGGCGG</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>SOE-PcdrA-RBSg10L - R</td>
      <td>ctcctcgcccttgctcaccat GGATATATCTCCTTCTTAAAG</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>mTFP1 - F</td>
      <td>atggtgagcaagggcgaggag</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>KpnI - mTFP1 – R</td>
      <td>GGGGTACC ttacttgtacagctcgtcc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>BamH1-Psia-F</td>
      <td>GGG GGATCC GGCAGCGGCAACCGCCTCTG</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>SiaA-BamH1-R</td>
      <td>CCC GGATCC CAACCCCCAGTTCGCCGCCAT</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>M13F(−21)</td>
      <td>TGTAAAACGACGGCCAGT</td>
      <td>GeneWiz</td>
    </tr>
    <tr>
      <td>M13R</td>
      <td>CAGGAAACAGCTATGAC</td>
      <td>GeneWiz</td>
    </tr>
    <tr>
      <td>ampR-F-qPCR</td>
      <td>GCG CCA TCC CTT CAT CG</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>ampR-R-qPCR</td>
      <td>GAT GTC GAC GCG GTT GTT G</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>pslA-F-qPCR</td>
      <td>AAG ATC AAG AAA CGC GTG GAA T</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>pslA-R-qPCR</td>
      <td>TGT AGA GGT CGA ACC ACA CCG</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>pelA-F-qPCR</td>
      <td>CCT TCA GCC ATC CGT TCT TCT</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>pelA-R-qPCR</td>
      <td>TCG CGT ACG AAG TCG ACC TT</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>rplU-F-qPCR</td>
      <td>CGC AGT GAT TGT TAC CGG TG</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>rplU-R-qPCR</td>
      <td>AGG CCT GAA TGC CGG TGA TC</td>
      <td>Colvin et al., 2011</td>
    </tr>
    <tr>
      <td>OBT268</td>
      <td>GGGGACAACTTTTGTATACAAAGTTGTACTATAGAGGGACAAACTCAAGGTCATTCGCAAGAGTGGCCTTTATGATTGACCTTCTTCCGG TTAATACGACCGGGATAACTCCACTTGAGACGTGAAAAAAGAGGAGTA TTCATGCGTAAAGGAGAAGAACTTTTCACTGGAG</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>OBT269</td>
      <td>GGGGACAAGTTTGTACAAAAAAGCA GGCTCGGCTTATTTGTATAGTTCATCCATGCCATGTGTAATC</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>OBT314</td>
      <td>CAGGTCGACTCTAGAGGATCCCCATCAGAAAATTTATCAAAAAGAGTGTTGACTTGTGAGCGGATAACAATGATACTTAGATTCAATTGTGAGCGGATAACAATTTCACA CATCTAGAATTAAAGAGGAGAAATTAA GCATGGTGAGCAAGGGCGAGGAG</td>
      <td>Zhao et al., 2013</td>
    </tr>
    <tr>
      <td>OBT315</td>
      <td>CTCCTCGCCCTTGCTCACCATGCTTAA TTTCTCCTCTTTAATTCTAGATGTGT GAAATTGTTATCCGCTCACAATTGAATCTAAGTATCATTGTTATCCGCTCACAAGTCAACACTCTTTTT GATAAATTTTCTGATGGGGAT CCTCTAGAGTCGACCTG</td>
      <td>Zhao et al., 2013</td>
    </tr>
    <tr>
      <td>pPcdrA::gfpASV</td>
      <td>PcdrA reporter with short halflife GFP</td>
      <td>Rybtke et al., 2012</td>
    </tr>
    <tr>
      <td>pENTRPEX18Gm::ΔpilY1</td>
      <td>suicide plasmid containing pilY1 deletion construct for use in PAO1</td>
      <td>Gift from Joe Harrison</td>
    </tr>
    <tr>
      <td>pENTRPEX18Gm::ΔdipA</td>
      <td>suicide plasmid containing dipA deletion construct for use in PAO1</td>
      <td>Gift from Joe Harrison</td>
    </tr>
    <tr>
      <td>pBBR1MCS5</td>
      <td>broad host range vector that is stable in P. aeruginosa, GentR</td>
      <td>Elzer et al., 1995</td>
    </tr>
    <tr>
      <td>pUC18-miniTn7T2-PcdrA-RBSg10L-gfpAGA</td>
      <td>source plasmid containing promoter of cdrA with enhanced ribosomal binding site</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>pNCS-mTFP1</td>
      <td>source plasmid containing mTFP1</td>
      <td>Allele Biotech</td>
    </tr>
    <tr>
      <td>pBBR1MCS5-PcdrA::RBSg10L::mTFP1</td>
      <td>teal fluorescent protein version of PcdrA reporter</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>pPsiaA::gfp</td>
      <td>PsiaA reporter expressing stable GFP, constructed using pMH487 plasmid</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>pBT270</td>
      <td>miniTn7 transposon with gfpmut3 driven by the A1/04/03 promoter; Apr, Gmr</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pTNS2</td>
      <td>T7 transposase expression vector</td>
      <td>Choi and Schweizer, 2006</td>
    </tr>
    <tr>
      <td>pBT223</td>
      <td>miniTn7 transposon with gfpmut3 driven by the trc promoter; Apr, Gmr</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pBT212</td>
      <td>A GateWay compatible plasmid containing gfpmut3 flanked by attR5 and attL1 recombination sites; Kmr</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pBT200</td>
      <td>A GateWay compatible plasmid containing the trc promoter flanked by attL2 and attL5 recombination sites; Knr</td>
      <td>Zhao et al., 2013</td>
    </tr>
    <tr>
      <td>pUC18-miniTn7T2-Gm-GW</td>
      <td>A GateWay compatible mini-Tn7 based vector; Cmr, Apr and Gmr;</td>
      <td>Zhao et al., 2013</td>
    </tr>
    <tr>
      <td>AKN66</td>
      <td>source for gfpmut3</td>
      <td>Lambertsen et al., 2004</td>
    </tr>
    <tr>
      <td>pDONR221 P1-P5r</td>
      <td>A GateWay compatible vector with attP1 and attP5r recombination sites and ccdB; Knr and Cmr</td>
      <td>Invitrogen</td>
    </tr>
  </tbody>
</table>

PAO1 ΔpilY1 was constructed using two-step allelic exchange following conjugation of wild type PAO1 with E. coli S17.1 harboring pENTRPEX18Gm::ΔpilY1 (a gift from Joe Harrison) as previously described (Hmelo et al., 2015). PAO1 ΔpilY1 was identified by colony PCR using primers PAO1pilY1-SEQ-F and PAO1pilY1-SEQ-R. PAO1 ΔdipA was constructed similarly by conjugation of wild type PAO1 with E. coli S17.1 harboring pENTRPEX18Gm::ΔdipA (a gift from Joe Harrison). PAO1 ΔdipA was identified by colony PCR using primers PAO1dipA-SEQ-F and PAO1dipA-SEQ-R. PA14 ΔwspR and ΔwspF deletion mutants were confirmed by PCR using primers PA14wspR-SEQ-F and PA14wspR-SEQ-R or PA14wspF-SEQ-F and PA14wspF-SEQ-R, respectively.

To create MPAO1 attTn7::P(A1/04/03)::GFPmut, the miniTn7 from pBT270 was integrated into the chromosome of P. aeruginosa PAO1 with the helper plasmid pTNS2, as previously described (Choi and Schweizer, 2006). pBT270 was created by introducing the constitutive A1/04/03 promoter (Lanzer and Bujard, 1988) and removing the trc promoter from pBT223 using the QuikChange Lightning Kit (Agilent Technologies) and the oligonucleotides OBT314 and OBT315. pBT223 was constructed via recombineering of pBT200, pUC18-miniTn7T2-Gm-GW, and pBT212 using Multisite Gateway technology (Invitrogen). pBT212 was constructed by cloning the gfpmut3 from AKN66 using OBT268 and OBT269, and recombining the PCR product with pDONR221 P1-P5r.

### Construction of optogenetic, c-di-GMP reporter strain in P. aeruginosa

Chromosomal insertion of bphS was achieved using the mini-CTX system and these strains were marked with different fluorescent proteins by mini-Tn7 site-specific transposition essentially as previously described (Choi and Schweizer, 2006; Hoang et al., 2000). First, a bphS fragment obtained from the plasmid pIND4 was cloned into the vector mini-CTX2 with the PA1/O4/O3 promoter upstream of the MCS via a two-piece ligation. The constructed plasmid was electroporated into PAO1 and the corresponding recombinant strain was identified by screening on LB agar plates containing 1 mM IPTG and 100 μg/mL tetracycline. Then, the strains were electroporated with a pFLP2 plasmid and distinguished on LB agar plates containing 5% (w/v) sucrose for the excision of the resistance marker. The c-di-GMP reporter plasmid and mCherry/EGFP marked bphS mutants were constructed as described above. The c-di-GMP reporter plasmid (PcdrA::gfpASV) was electroporated into the mCherry-marked strain harboring bphS to monitor the intracellular c-di-GMP level.

To validate the optogenetic reporter strain in Figure 5—figure supplement 1, strains were grown on LB agar plates at 37°C for 24 hr from frozen stocks. Monoclonal colonies were inoculated and cultured with a minimal medium (FAB) at 37°C overnight, adding 1 uM FeCl3 and 30 mM glutamate as the carbon source, until the culture reached an OD600 of approximately 2.1. Then, the bacterial culture was further diluted (1:100) in fresh FAB medium to OD600 0.5. When required, gentamicin was added to medium at 30 μg/mL. Plates and tubes were wrapped with aluminum foil to achieve a dark condition. Finally, the culture was diluted (1:50) in fresh FAB medium and 6 μL diluted culture was spotted onto an FAB agarose (2%) pad, with 30 mM glutamate and 1 μM FeCl3. The agarose pad was pressed on a coverglass before cells were illuminated.

### Cyclic di-GMP measurement and qRT-PCR of tube biofilms

Measurement of c-di-GMP in tube biofilm cells was performed as previously described (Colvin et al., 2011). Transcriptional analysis of PelA expression in tube biofilms was performed as described in the ‘FACS and qRT-PCR of c-di-GMP reporter cells’ section.

### Crystal violet attachment assays

Crystal violet assays were performed essentially as previously described to measure biofilm biomass, except using gentle washing after 2–6 hr of static incubation (Armbruster et al., 2016). To measure biofilm biomass at 24 hr, the crystal violet assay was performed as previously described without gentle washing (Colvin et al., 2012).

### Flow cell time course experiments and confocal microscopy

P. aeruginosa cells harboring the pPcdrA::gfpASV reporter plasmid or a promotorless vector control (pMH489) were grown to mid-log in LB with 100 µg/mL gentamicin (Gm100) from LB Gm100 plates or from overnight broth cultures in FAB +10 mM glutamate. Mid-log cells were back diluted into 1% LB or FAB +0.6 mM glutamate and flow chambers were inoculated at a final OD600 0.1 and inverted for 10 min to allow cells to attach before induction of flow. Clean media was used to wash non-attached cells by flow at 40 mL per hour for 20 min. Flow was then reduced to a final constant flow rate of 3 mL per hour and bacteria were imaged immediately on a Zeiss LSM 510 scanning confocal laser microscope (t = 0 hr). Flow cells were incubated at a constant flow rate at room temperature and imaged hourly for up to 24 hr. For every strain and time point, 5 fields of view and a minimum of 300 cells were captured using identical microscope settings to image GFP fluorescence across all experiments. Images were analyzed using using Volocity software (Improvision, Coventry, UK). We binned cells by their mean GFP fluorescence intensity per pixel, in incremints of 20 fluorescence units, and determined the cut-off bin that corresponded to cells clearling produced GFP when images were examined by eye. Therefore, cells were counted as pPcdrA::gfpASV reporter ‘on’ if their mean GFP fluorescence intensity per pixel was ≥321 fluorescence units. For all summary figures depicting the percentage of cells with the reporter ‘on’, data are presented in terms of the percentage of cells with an average GFP fluorescence per pixel of ≥321 fluorescence units (pPcdrA::gfpASV reporter ‘on’). Microscopy images were artificially colored to display GFP fluorescence as green.

### Construction of pPsiaA::gfp

A region 259 bp upstream through 21 bp into the coding sequence of siaA was amplified from PAO1 genomic DNA using primers BamH1-Psia-F and SiaA-BamH1-R, then gel purified using a QIAquick gel extraction kit (Qiagen, Hilden, Germany) digested with BamH1, then column purified with a QIAquick PCR purification kit (Qiagen, Hilden, Germany) to remove BamH1. The GFP expression vector pMH487, which contains the gfpmut3 gene with an RNase III splice site and lacking a promoter (Borlee et al., 2010), was digested with BamH1, treated with Antarctic phosphatase (New England Biolabs, Ipswich, MA), then column purified with a QIAquick PCR purification kit (Qiagen, Hilden, Germany) to remove BamH1. The PsiaA allele was ligated into digested pMH487, then transformed into E. coli DH5α, purified, and sequenced using primer M13F(−21) (Genewiz). The reporter pPsiaA::gfp was electroporated into P. aeruginosa as previously described and maintained under gentamycin selection at 100 μg/mL.

### Multi-generation single cell tracking of type IV motility and c-di-GMP reporter activity

Wild type PAO1 harboring the pPcdrA::gfpASV reporter was grown shaking for 20 hr in FAB media with 6 mM glutamate. The flow cell inoculum was prepared by diluting the culture to a final OD600 of 0.01 in FAB with 0.6 mM glutamate. The flow cell inoculum was injected into the flow cell (Department of Systems Biology, Technical University of Denmark) and allowed to incubate for 10 min at 30°C prior to flushing with media at 30 mL/h for 10 min. Experiments were performed under a flow rate of 3 mL/hour for a total of 40 hr.

Images were acquired with an Olympus IX81 microscope equipped with a Zero Drift Correction autofocus system, a 100 × oil objective with a 2 × multipler lens, and an Andor iXon EMCCD camera using Andor IQ software. Bright-field images were recorded every 3 s and GFP fluorescence every 15 min. Acquisition continued for a total recording time of 40 hr, which resulted in approximately 48000 bright-field images, and 160 fluorescence images.

Images were analyzed in MATLAB to track bacterial family trees, GFP fluorescence, and surface motility essentially as previously described (Lee et al., 2018) with the following modifications. Image analysis, family tracking and manual validation, family tree plotting, and tree asymmetry λ calculations were performed as previously described (Lee et al., 2018) without modification. GFP fluorescence intensities were normalized by calculating the distribution of intensities per cell per frame (extracted by using the binary image as a mask) and then setting the minimum and maximum intensities to the 1st and 99th percentiles of this distribution for each dataset. Ic-di-GMP (relative normalized c-di-GMP reporter intensity) was calculated by averaging the normalized fluorescence intensities across all members of a family. Fmotile (fraction of time that cells in a family are motile) was calculated as follows. For each family, every cell trajectory in the family was divided into time intervals. For each time interval, presence or absence of motility was determined using a combination of metrics, including Mean Squared Displacement (MSD) slope, radius of gyration, and visit map. MSD slope quantifies the directionality of movement relative to diffusion. Radius of gyration and visit map are different metrics for quantifying the average distance traveled on the surface. Fmotile was then calculated by the fraction of these time intervals that have motility. This calculation was modified from the ‘TFP activity metric’ previously described (Lee et al., 2018).

### Setup of Adaptive Tracking Illumination Microscopy

Figure 5—figure supplement 2 shows a schematic of the Adaptive Tracking Illumination Microscopy (ATIM) setup. An inverted fluorescent microscope (Olympus, IX71) was modified to build the ATIM. The modification includes: 1) a commercial DMD-based LED projector (Gimi Z3) was used to replace the original bright-field light source, in which the original lenses in the projector were removed and three-colored (RGB) LEDs were rewired to connect to an external LED driver (ThorLabs) controlled by a single chip microcomputer (Arduino UNO r3); 2) the original bright-field condenser was replaced with an air objective (40× NA = 0.6, Leica); and 3) an additional 850 nm LED light (ThorLabs) was coupled to the illumination optical path using a dichroic mirror (Semrock) for the bright-field illumination. The 850 nm LED bright field light source does not affect optogenetic manipulation. An inverted fluorescent microscope (Olympus, IX71) equipped with a 100× oil objective and a sCMOS camera (Zyla 4.2 Andor) was used to collect bright-field images with 0.2 frame rate. The bright-field images were further analyzed to track multiple single cells in real time using a high-throughput bacterial tracking algorithm coded by Matlab. The projected contours of selected single cells were sent to the DMD (1280 × 760 pixels) that was directly controlled by a commercial desktop through a VGA port. The manipulation lights were generated by the red-color LED (640 nm), and were projected on the single selected cells in real time through the DMD, a multi-band pass filter (446/532/646, Semrock) and the air objective. Our results indicated that feedback illuminations could generate projected patterns to exactly follow the cell movement (Figure 5 – Supplemental 2B) or single cells divisions (Figure 5 – Supplemental 2C) in real time.

### Manipulation of c-di-GMP expression in single initial-attached cells

The bacterial strain PAO1-bphS-PcdrA-GFP-mCherry was inoculated into a flow cell (Denmark Technical University) and continuously cultured at 30.0 ± 0.1 °C by flowing FAB medium (3.0 mL/h). The flow cell was modified by punching a hole with a 5 mm diameter into the channel, and the hole was sealed by a coverslip that allows the manipulation light to pass through. An inverted fluorescent microscope (Olympus, IX71) equipped with a 100× oil objective and a sCMOS camera (Zyla 4.2 Andor) was used to collect bright field or fluorescent images with 0.2 or 1/1800 frame rate respectively. The power density of the manipulation lights was determined by measuring the power at the outlet of the air objective using a power meter (Newport 842-PE). GFP or mCherry was excited using a 480 nm or 565 nm LED lights (ThorLabs) and imaged using single-band emission filters (Semrock): GFP (520/28 nm) or mCherry (631/36 nm). Initial-attached cells were selected to be manipulated using ATIM with the illumination at 0.05 mW/cm2, which allowed us to compare the results arising from illuminated or un-illuminated mobile cells in one experiment. The c-di-GMP levels in single cells were gauged using the ratio of GFP and mCherry intensities.

### Lectin staining and flow cytometry

Glass culture tubes were inoculated with 1 mL of P. aeruginosa in LB or Jensen’s minimal media at an OD600 0.8 and incubated statically at 37°C for 4 hr. Non-adhered cells were removed by washing three times with 2 mL sterile phosphate buffered saline (PBS). Biofilm cells were harvested by vortexing in 1 mL PBS with tetramethylrhodamine (TRITC) conjugated lectins (TRITC-labeled WFL lectin (100 μg/mL; Vector Laboratories) for Pel, TRITC-labeled HHA (100 μg/mL; EY Laboratories) for Psl) and incubated on ice for 5 min. Cells were washed 3 times to remove non-adhered lectin, resuspended in PBS, and immediately analyzed for GFP and TRITC fluorescence on a BD LSRII flow cytometer (BD Biosciences). Events were gated based on forward and side scatter to remove particles smaller than a single P. aeruginosa cell and large aggregates.

We used PAO1 cells that did not express GFP (wild type PAO1; Figure 1—source data 2) or constitutively expressed GFP (PAO1 Tn7::P(A1/04/03)::GFPmut; Figure 1—source data 2) to define a gate for high GFP fluorescence. We validated this gate using a strain in which we expect very high levels of reporter activity (surface grown PAO1 ΔwspFΔpelAΔpslBCD harboring pPcdrA::gfpASV) and saw that 91.6% of cells had high GFP levels (Figure 1—source data 2), in agreement with our flow cell characterization of this strain (Figure 2A). We determined gating for TRITC using cells that had not been stained with TRITC-conjugated lectin (Figure 1—figure supplement 6A), as well as two strains that overproduced either Psl (Figure 1—figure supplement 6B) or Pel (Figure 1—figure supplement 6C) that were stained with the appropriate TRITC-conjugated lectin. Our flow cytometry gating procedure accurately gated 99.7% of wild type PAO1 cells (without the PcdrA reporter or lectin-staining) as low GFP and low TRITC (Figure 1—figure supplement 6D).

### FACS and qRT-PCR of c-di-GMP reporter cells

Static biofilm reporter cells were grown as described above and harvested without lectin staining. Cells were fixed with 6% paraformaldehyde for 20 min on ice, then rinsed once with sterile PBS prior to analysis with a FACSAriaII (BD Biosciences, San Jose, CA). Events were gated first to remove debris and large cellular aggregates, and then gated into cells with low and high GFP fluorescence intensity. The low GFP gate was drawn using wild type PAO1 cells without the gfp gene (Figure 1—figure supplement 7A) and the high GFP gate was drawn using both PAO1 Tn7::P(A1/04/03)::GFPmut (Figure 1—figure supplement 7B) and PAO1 ΔwspF ΔpelA ΔpslBCD PcdrA::gfpASV reporter (Figure 1—figure supplement 7C). As expected, wild type PAO1 pPcdrA::gfpASV reporter cells that had been harvested after 4 hr of surface attachment to glass in static LB liquid culture displayed subpopulations of high GFP, reporter ‘on’ cells (30.8% of the population) and ‘off’ (57.2%) cells (Figure 1—figure supplement 7D), whereas this same strain grown to mid-log planktonically in LB displayed mostly reporter ‘off’ cells (Figure 1—figure supplement 7E). Cells were sorted at 4°C by flow assisted cell sorting (FACS) to collect 100,000 events into TRIzol LS (Thermo Fisher Scientific, Waltham, MA). RNA was extracted from sorted cells by boiling immediately for 10 min and following the manufacturer’s instructions for RNA isolation. DNA was digested by treating with RQ1 Dnase I (Promega, Madison, WI) and samples were checked for genomic DNA contamination by PCR to detect rplU. Expression of pelA, pslA, and ampR was measured by quantitative Reverse Transcriptase PCR (qRT-PCR) using the iTaq Universal SYBR Green One-Step kit (Biorad, Hercules, CA) and a CFX96 Touch Real-Time PCR detection system (Bio-Rad, Hercules, CA). The ΔΔCq was calculated for three independent samples of sorted wild type PAO1 PcdrA::gfpASV reporter biofilm cell populations by normalizing PelA and PslA to relative levels of AmpR expression. Data were presented as the average fold change in PelA or PslA expression in the PcdrA::gfpASV sorted ‘on’ population (high GFP) relative to the ‘off’ population (low GFP) for the three biological replicates.

### WspR-YFP foci and pPcdrA::mTFP1 reporter

A version of the pPcdrA reporter was constructed in the pBBR1MCS5 plasmid to express mTFP1 instead of GFP, for use with YFP-tagged WspR proteins. The PcdrA promoter and an enhanced ribosomal binding site from the gene 10 leader sequence of the T7 phage (g10L) was amplified from pUC18-miniTn7T2-PcdrA-RBSg10L-gfpAGA using primers SacI-PcdrA-F and SOE-PcdrA-RBSg10L-R. The primers mTFP1-F and KpnI-mTFP1-R were used to amplify the mTFP1 gene from plasmid pNCS-mTFP1 (Allele Biotech, San Diego, CA). The PcdrA::RBSg10L::mTFP1 allele was constructed by SOE-PCR using primers SacI-PcdrA-F and Kpn1-mTFP1-R, then pBBR1MCS5 and the SOE PCR product were doubly digested with SacI/KpnI. Digested pBBR1MCS5 was treated with Antarctic phosphatase, then both digests were gel purified and ligated. The ligation was transformed into E. coli DH5α, and plasmid from clones growing on LB with 10 μg/mL gentamycin were sequenced with primers M13F and M13F(−21) (GeneWiz). Fluorescence of the pPcdrA::mTFP1 reporter was measured in Wsp mutants in a fluorimeter (BioTek Synergy H1 Hybrid Reader, BioTek Instruments, Inc, Winooski, VT, USA) and in flow cells to confirm its activity resembled that of pPcdrA::gfpASV. The pPcdrA::mTFP1 reporter was electroporated into P. aeruginosa strains with the native WspR deleted and harboring an arabinose-inducible copy of WspR-YFP on its chromosome (Huangyutitham et al., 2013). Cells were grown on LB agar plates with 100 μg/mL gentamycin and 1% arabinose for 10 hr, then transferred to an agar pad for imaging of Differential Interference Contrast (DIC), YFP, and TFP. WspR-YFP foci and mTFP1 fluorescence was imaged using a Nikon Ti-E inverted wide-field fluorescence microscope with a large-format scientific complementary metal-oxide semiconductor camera (sCMOS; NEO, Andor Technology, Belfast, United Kingdom) and controlled by NIS-Elements. WspR-YFP foci were detected and pPcdrA::mTFP1 reporter activity were analyzed using NIS-Elements AR software (Nikon Instruments, Melville, NY, USA). Regions of interest (ROI) corresponding to individual cells were determined using DIC images and the average mTFP1 fluorescence was measured within these ROIs. Next, we used essentially the same protocol as previously described for detecting WspR-eYFP foci (Huangyutitham et al., 2013), by examining the ratio of the maximum eYFP signal to the mean eYFP signal for each ROI. We verified by eye that the previously determined cut-off ratio of 1.7 accurately represented cells with at least one visible WspR-eYFP focus (Huangyutitham et al., 2013).
