# MYC overrides HIF-1α to regulate proliferating primary cell metabolism in hypoxia

## Authors

- Courtney A Copeland<sup>1</sup>
- Benjamin A Olenchock<sup>1</sup>
- David Ziehr<sup>1</sup>
- Sarah McGarrity<sup>1</sup>
- Kevin Leahy<sup>1</sup>
- Jamey D Young<sup>5</sup>
- Joseph Loscalzo<sup>1</sup> ([ORCID: 0000-0002-1153-8047](https://orcid.org/0000-0002-1153-8047))
- William M Oldham<sup>1</sup> ([ORCID: 0000-0003-3029-4866](https://orcid.org/0000-0003-3029-4866)) †

### Affiliations

1. Department of Medicine, Brigham and Women’s Hospital Boston United States ([ROR:04b6nzv94](https://ror.org/04b6nzv94))
2. Department of Medicine, Harvard Medical School Boston United States
3. Department of Medicine, Massachusetts General Hospital Boston United States ([ROR:002pd6e78](https://ror.org/002pd6e78))
4. Center for Systems Biology, School of Health Sciences, University of Iceland Reykjavik Iceland ([ROR:01db6h964](https://ror.org/01db6h964))
5. Departments of Chemical & Biomolecular Engineering and Molecular Physiology & Biophysics, Vanderbilt University Nashville United States ([ROR:02vm5rt34](https://ror.org/02vm5rt34))

† Corresponding author

## Abstract

Hypoxia requires metabolic adaptations to sustain energetically demanding cellular activities. While the metabolic consequences of hypoxia have been studied extensively in cancer cell models, comparatively little is known about how primary cell metabolism responds to hypoxia. Thus, we developed metabolic flux models for human lung fibroblast and pulmonary artery smooth muscle cells proliferating in hypoxia. Unexpectedly, we found that hypoxia decreased glycolysis despite activation of hypoxia-inducible factor 1α (HIF-1α) and increased glycolytic enzyme expression. While HIF-1α activation in normoxia by prolyl hydroxylase (PHD) inhibition did increase glycolysis, hypoxia blocked this effect. Multi-omic profiling revealed distinct molecular responses to hypoxia and PHD inhibition, and suggested a critical role for MYC in modulating HIF-1α responses to hypoxia. Consistent with this hypothesis, MYC knockdown in hypoxia increased glycolysis and MYC over-expression in normoxia decreased glycolysis stimulated by PHD inhibition. These data suggest that MYC signaling in hypoxia uncouples an increase in HIF-dependent glycolytic gene transcription from glycolytic flux.

## Introduction

Cellular responses to hypoxia propel many physiologic and pathologic processes from wound healing and angiogenesis to vascular remodeling and fibrosis (Lee et al., 2019b; Semenza, 2012). These activities require cells to continue energetically demanding tasks, such as macromolecular biosynthesis and proliferation, despite limited oxygen availability. Since respiration is the most efficient way for cells to produce energy, cell metabolism must adapt to meet energy demands when oxygen supply is limiting. Understanding how these metabolic adaptations sustain critical cellular processes in hypoxia is fundamentally important to our understanding of human health and disease.

Cells typically respond to hypoxia by shifting energy production away from respiration and toward glycolysis. This response is mediated primarily by stabilization of the hypoxia-inducible transcription factor 1α (HIF-1α). HIF-1α activates the transcription of glucose transporters, glycolytic enzymes, and lactate dehydrogenase, while decreasing the expression of tricarboxylic acid (TCA) cycle and electron transport chain enzymes (Lee et al., 2020; Semenza, 2012). Although HIF-1α is constitutively expressed, it is hydroxylated by prolyl hydroxylase enzymes (PHDs) in normoxia and targeted for proteasomal degradation. PHDs are α-ketoglutarate-dependent dioxygenase enzymes that require molecular oxygen for their enzymatic activity. When oxygen tension falls, PHD activity decreases, leading to HIF-1α stabilization and activation of its downstream transcriptional program. Overall, this transcriptional program should increase glycolytic flux and lactate production while decreasing TCA cycle flux and oxidative phosphorylation.

In addition to metabolic changes designed to maintain energy supply, hypoxic cells also reduce energy demand through down-regulation of Na+/K+-ATPase, slowing protein translation, and decreasing cell proliferation (Hubbi and Semenza, 2015; Wheaton and Chandel, 2011). In particular, HIF-1α decreases cell proliferation by activating cyclin-dependent kinase inhibitor expression, inhibiting cell-cycle checkpoint progression (Gardner et al., 2001), and antagonizing pro-proliferative MYC signaling (Koshiji et al., 2004). Despite these canonical effects of HIF-1α activation, there are many examples where cells continue to proliferate despite hypoxic stress, including cancer cells, stem cells, and lung vascular cells (Hubbi and Semenza, 2015). How these cells meet the metabolic needs of sustained proliferation in hypoxia is an active area of investigation (Jain et al., 2020; Lee et al., 2020; Oldham et al., 2015). Since hypoxia is a prominent feature of cancer biology as tumor growth outstrips blood supply, most detailed metabolic studies of hypoxic cell metabolism have used tumor cell models, yielding important insights into the metabolic pathobiology of cancer (Garcia-Bermudez et al., 2018; Jiang et al., 2016; Lee et al., 2019a; Meléndez-Rodríguez et al., 2019; Metallo et al., 2011; Wise et al., 2011). For example, stable isotope tracing and metabolic flux analyses identified a critical role for the reductive carboxylation of glutamine-derived α-ketoglutarate for lipid biosynthesis in supporting tumor growth (Gameiro et al., 2013; Metallo et al., 2011; Scott et al., 2011; Wise et al., 2011), and metabolomic studies identified aspartate as a limiting metabolite for cancer cell proliferation under hypoxia (Garcia-Bermudez et al., 2018). By contrast, comparatively little is known about metabolic adaptations of primary cells to hypoxia. Indeed, the importance of reductive carboxylation or aspartate biosynthesis remains to be elucidated in primary cells. A more complete understanding of primary cell metabolic adaptations to hypoxia would provide an important context for understanding how metabolic reprogramming supports normal cellular responses to hypoxia, how these responses may be (mal)adaptive in a variety of disease contexts, and how the hypoxia metabolic program in primary cells differs from that observed in cancer cells.

To address these questions, we have developed models of bioenergetic carbon flux in human lung fibroblasts (LFs) and pulmonary artery smooth muscle cells (PASMCs) cultured in 21% or 0.5% oxygen. These cells may be exposed to a wide range of oxygen concentrations in vivo, continue to proliferate despite hypoxic culture conditions in vitro, and play important roles in the pathology of non-cancerous diseases in which tissue hypoxia features prominently, including pulmonary hypertension and pulmonary fibrosis. We found that hypoxia fails to increase glycolysis in these primary cells despite robust up-regulation of the HIF-1α transcriptional program. In normoxia, HIF-1α stabilization by the PHD inhibitor molidustat (BAY-85–3934, “BAY”) (Flamme et al., 2014) did increase glycolysis and lactate efflux; however, hypoxia blocked this response. These findings suggested that important hypoxia-dependent regulatory mechanisms override the metabolic consequences of HIF-1α-dependent increases in glycolytic gene expression. Transcriptomic profiling identified a critical role for the transcription factor MYC in the adaptive response to hypoxia. Using knockdown and over-expression approaches, we demonstrated that MYC attenuates HIF-driven glycolysis in hypoxia and following HIF stabilization in normoxia.

## Results

### Hypoxia uncouples HIF-dependent glycolytic gene expression from glycolytic metabolic flux

The goal of this study was to characterize hypoxia-induced metabolic changes in proliferating primary LFs and PASMCs. To accomplish this goal, we used metabolic flux analysis to model how cell metabolism supports cell proliferation. Metabolic flux analysis fits cell proliferation rate, extracellular flux measurements, and 13C isotope labeling patterns to a computational model of cell metabolism (Antoniewicz, 2018). This analysis reconstructs comprehensive flux maps that depict the flow of carbon from extracellular substrates through intracellular metabolic pathways into cell biomass and metabolic by-products (Young, 2014). These models assume that cells are at a metabolic pseudo-steady state over the experimental time course (Buescher et al., 2015). Exponential growth phase is thought to reflect metabolic pseudo-steady state as cells in culture steadily divide at their maximal condition-specific rate, provided nutrient supply does not become limiting (Ahn and Antoniewicz, 2011; Buescher et al., 2015). Thus, we first set out to define experimental conditions to capture exponential growth phase in normoxic and hypoxic cultures.

Cells were seeded and placed into hypoxia for 24 hr prior to sample collection to provide adequate time for activation of the hypoxia-dependent transcriptional program (Figure 1A). We selected 0.5% oxygen for hypoxia as this level yielded the most reproducible phenotypic differences compared to 21% oxygen, while being physiologically relevant and above the KM of cytochrome c oxidase (electron transport chain complex IV) for oxygen (Lee et al., 2020; Wenger et al., 2015). We identified the optimal cell seeding density and time course for exponential cell growth (Figure 1B). Hypoxia decreased cell proliferation rates (Figure 1C), but slower growth was not associated with decreased cell viability (Figure 1—figure supplement 1A). As anticipated, hypoxic cells demonstrated robust stabilization of HIF-1α associated with up-regulation of its downstream targets glucose transporter 1 (GLUT1) and lactate dehydrogenase A (LDHA; Figure 1D–H). These changes persisted for the duration of the experimental time course.

![Figure 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig1-v1.jpg)

**Figure 1.:** (A) Lung fibroblasts (LFs) were cultured in 21% or 0.5% oxygen beginning 24 hr prior to time 0. Samples were collected every 24 hr for 72 hr. (B) Growth curves of LFs in each experimental condition (n=8). (C) Growth rates from (B) were determined by robust linear modeling of log-transformed growth curves. (D) Representative immunoblot of LF protein lysates cultured as in (A). (E) Relative change in HIF-1α protein levels from (D) normalized to 21% oxygen at time 0 (n=4). (F) Relative change in GLUT1 mRNA levels normalized to 21% oxygen treatment at time 0 (n=4). (G) Relative change in LDHA mRNA levels as in (F). (H) Relative change in LDHA protein levels as in (E). (I) Extracellular fluxes of glucose (GLC) and lactate (LAC) (n=8). By convention, negative fluxes indicate metabolite consumption. (J) Extracellular fluxes of pyruvate (PYR) and amino acids. Data are mean ± SEM (* p<0.05).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Cell viability as assessed by live/dead cell staining with acridine orange plus propidium iodide did not differ between 21% and 0.5% oxygen culture conditions (n=3 technical replicates). (B) Predicted well volumes were estimated from the change in culture plate mass over the experimental time course. Evaporation rates differed depending on the culture conditions and treatment. Although the mean evaporation rate is depicted, experiment-specific evaporation rates were used to calculate fluxes for each biological replicate (C) Metabolite accumulation (positive values) and degradation (negative values) rates. Data are mean ± SEM of three to eight biological replicates. Rates significantly different from 0 (*) based on a probability value <0.05 using Student’s one-sample t-test were incorporated into flux calculations.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** Cells were cultured in MCDB131 supplemented with 8 mM [U-13C6]-glucose. Conditioned medium was collected, spiked with [D8]-ᴅʟ-valine internal standard, and analyzed by LC-MS. (A) A standard curve was generated from the peak area ratios of lactate and the internal standard prepared in unconditioned MCDB131 medium. (B) Lactate accumulates more slowly in the conditioned medium from hypoxic cells (n=3 biological replicates). (C) Lactate efflux was decreased in hypoxia, similar to the data obtained from enzymatic lactate assay. Data are mean ± SEM (* p<0.05).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Lung fibroblasts (LFs) were cultured in 21% or 0.2% oxygen beginning 24 hr prior to time 0. Samples were collected every 24 hr for 72 hr. (B) Growth curves of LFs in each experimental condition (n=4). (C) Growth rates from (B) were determined by robust linear modeling of log-transformed growth curves. (D) Representative immunoblot of LF protein lysates cultured as in (A). (E) Relative change in HIF-1α protein levels from (D) normalized to 21% oxygen at time 0 (n=4). (F) Relative change in GLUT1 mRNA levels normalized to 21% oxygen treatment at time 0 (n=4). (G) Relative change in LDHA mRNA levels as in (F). (H) Relative change in LDHA protein levels as in (E). (I) Extracellular fluxes of glucose (GLC) and lactate (LAC) (n=4). By convention, negative fluxes indicate metabolite consumption. (J) Extracellular fluxes of pyruvate (PYR) and amino acids. Data are mean ± SEM (* p<0.05).

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) Pulmonary artery smooth muscle cells (PASMCs) were cultured in 21% or 0.5% oxygen beginning 24 hr prior to time 0. Samples were collected every 24 hr for 72 hr. (B) Growth curves of LFs in each experimental condition (n=4). (C) Growth rates from (B) were determined by robust linear modeling of log-transformed growth curves. (D) Representative immunoblot of LF protein lysates cultured as in (A). (E) Relative change in HIF-1α protein levels from (D) normalized to 21% oxygen at time 0 (n=4). (F) Relative change in GLUT1 mRNA levels normalized to 21% oxygen treatment at time 0 (n=4). (G) Relative change in LDHA mRNA levels as in (F). (H) Relative change in LDHA protein levels as in (E). (I) Extracellular fluxes of glucose (GLC) and lactate (LAC) (n=4). By convention, negative fluxes indicate metabolite consumption. (J) Extracellular fluxes of pyruvate (PYR) and amino acids. Data are mean ± SEM (* p<0.05).

We next determined the extracellular fluxes of glucose (GLC), lactate (LAC), pyruvate (PYR), and amino acids (Figure 1I–J). Flux calculations incorporated cell growth rate, extracellular metabolite concentrations, metabolite degradation rates, and medium evaporation rate (see Materials and methods; Murphy and Young, 2013; Figure 1—figure supplement 1B–C). Interestingly, while we observed a modest increase in glucose uptake, we found that hypoxia actually decreased lactate efflux (Figure 1I). This finding was confirmed by measuring the rate of [U-13C3]-lactate produced from LFs cultured with [U-13C6]-glucose (Figure 1—figure supplement 2). Hypoxia decreased lactate efflux despite activating HIF-1α and increasing glycolytic enzymes expression (Figure 1D–H).

To test if more severe hypoxia would augment glycolysis, we cultured cells in 0.2% ambient oxygen (Figure 1—figure supplement 3). Under these conditions, we observed no change in glucose or lactate fluxes, similar to 0.5% oxygen culture. To test if this unexpected response was unique to LFs, we studied PASMCs under 0.5% oxygen conditions (Figure 1—figure supplement 4). Similar to LFs, we observed no change in glucose uptake and reduced lactate efflux in PASMCs. Together, these data suggest that hypoxia uncouples HIF-1α target gene expression and glycolytic flux in proliferating primary cells.

Since hypoxia did not increase glycolysis in LFs, we wanted to determine how these cells responded to HIF-1α stabilization in normoxia. To activate HIF-1α, LFs were treated with the PHD inhibitor molidustat (BAY, 10 μM) using a similar time course as our hypoxia experiments (Figure 2). Like hypoxia, BAY decreased cell growth rate (Figure 2B–C) and activated the HIF-1α transcriptional program (Figure 2D–H). Unlike hypoxia, HIF-1α stabilization in normoxia markedly increased glucose uptake and lactate efflux (Figure 2I). Although hypoxia and BAY treatments both increased HIF-1α, GLUT1, and LDHA to a similar degree, the glycolytic metabolic response differed markedly between these treatments.

![Figure 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig2-v1.jpg)

**Figure 2.:** (A) Lung fibroblasts (LFs) were treated with the prolyl hydroxlyase inhibitor molidustat (BAY, 10 μM) or DMSO beginning 24 hr prior to time 0. Samples were collected every 24 hr for 72 hr. (B) Growth curves of LFs in each experimental condition (n=8). (C) Growth rates from (B). (D) Representative immunoblot of LF protein lysates cultured as in (A). (E) Relative change in HIF-1α protein levels from (D) normalized to DMSO at time 0 (n=4). (F) Relative change in GLUT1 mRNA levels normalized to DMSO at time 0 (n=4). (G) Relative change in LDHA mRNA levels as in (F). (H) Relative change in LDHA protein levels as in (E). (I) Extracellular fluxes of glucose (GLC) and lactate (LAC) (n=8). By convention, negative fluxes indicate metabolite consumption. (J) Extracellular fluxes of pyruvate (PYR) and amino acids. Data are mean ± SEM (* p<0.05).

### Extracellular fluxes are treatment and cell-type dependent

In addition to glucose and lactate, we also determined the extracellular fluxes of pyruvate and amino acids (Figure 1J, Figure 1—figure supplement 3J, Figure 1—figure supplement 4J, Figure 2J). To our knowledge, this is the first comprehensive extracellular flux profiling of key metabolic substrates in primary cells. In LFs, changes in extracellular fluxes were modest overall, with hypoxia generally decreasing the fluxes of all measured metabolites. These findings were similar with 0.2% oxygen (Figure 1—figure supplement 3J).

Notably, we observed a significant decrease in glutamine consumption in hypoxic LFs. This finding contrasts with previous studies of cancer cell metabolism demonstrating increased glutamine uptake as a key feature of the metabolic response to hypoxia (Gameiro et al., 2013; Metallo et al., 2011; Wise et al., 2011). In these systems, glutamine-derived α-ketoglutarate was reductively carboxylated by isocitrate dehydrogenase enzymes to generate citrate for lipid biosynthesis. Glutamine has also been shown to support TCA cycling in hypoxia in a Burkitt lymphoma model (Le et al., 2012). Unlike LFs, PASMCs did exhibit a trend toward increased glutamine uptake (Figure 1—figure supplement 4J). To examine the relative importance of glucose and glutamine to the proliferation of these cells in hypoxia, we measured LF and PASMC growth rates in the absence of either substrate (Figure 3). In LFs, absence of either glucose or glutamine reduced cell proliferation to a similar extent (Figure 3A). In hypoxia, glucose deficiency decreased LF proliferation rate further, while glutamine deficiency had no additional impact. These findings are consistent with extracellular flux measurements demonstrating decreased glutamine consumption by LFs in hypoxia. Interestingly, neither glucose nor glutamine deficiency decreased PASMC proliferation (Figure 3B), suggesting a high degree of metabolic flexibility in these cells.

![Figure 3.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig3-v1.jpg)

**Figure 3.:** (A, B) Lung fibroblasts (n=8 biological replicates) (A) and pulmonary artery smooth muscle cells (n=4 biological replicates) (B) were cultured in MCDB131 medium lacking either glucose (-GLC) or glutamine (-GLN) for 72 hr. Growth rates were calculated from total DNA quantification. Data are mean ± SEM (* p<0.05; black compares 21% and 0.5% oxygen within a given treatment, red and blue compare substrate deficiency to replete medium in 21% and 0.5% oxygen, respectively.).

In LFs, among all of the measured amino acid fluxes, proline consumption uniquely increased (Figure 1J). Hypoxia increases collagen expression in these cells (Liu et al., 2013) and proline constitutes ~10% of the total amino acid content of collagens. Together, these data suggest an important contribution of extracellular proline to collagen production in hypoxic LFs as has been observed in other fibroblast cell lineages (Szoka et al., 2017).

In PASMCs, we observed increased consumption of the branched-chain amino acids (BCAAs) leucine and valine as well as arginine (Figure 1—figure supplement 4J), which was not observed in LFs. BCAAs are transaminated by branch chain amino transferase enzymes to branched chain α-keto acids (BCKAs). BCKAs are further metabolized to yield acyl-CoA derivatives for lipogenesis or oxidation (Crown et al., 2015; Mann et al., 2021). Previous studies have shown that hypoxia up-regulates arginase expression in hypoxic PASMCs (Chen et al., 2009; Xue et al., 2017) to support polyamine and proline synthesis required for cell proliferation (Li et al., 2001). Interestingly, activation of these metabolic pathways in hypoxia was not observed in LFs and suggests distinct metabolic dependencies of these different cell types.

Compared to hypoxia treatment, BAY demonstrated more modest effects on amino acid fluxes generally (Figure 2J). In particular, glutamate efflux was not affected by BAY treatment, while it was reduced by hypoxia. Alanine efflux was increased by BAY treatment, but decreased by hypoxia. In addition to the glucose and lactate fluxes noted above, these findings further highlight fundamental differences in the metabolic consequences of HIF-1α activation in normoxia and hypoxia.

### Isotope tracing reveals altered substrate utilization in hypoxia

To investigate intracellular metabolic reprogramming in hypoxic cells, we performed 13C stable isotope tracing with [U-13C6]-glucose, [1,2-13C2]-glucose, and [U-13C5]-glutamine. Isotopic enrichment of downstream metabolites in glycolysis and the TCA cycle were determined by LC-MS (Figure 4—figure supplement 1, Figure 4—figure supplement 2). Small changes in the patterns of isotope incorporation were observed following hypoxia or BAY treatment. The most substantial differences were observed in pyruvate (PYR), the terminal product of glycolysis, and citrate (CIT), a central metabolic node in TCA and fatty acid metabolism (Figure 4A–C). Both hypoxia and BAY treatments decreased incorporation of glucose-derived carbon into pyruvate (Figure 4A; i.e. the unlabeled, or M0, fraction was greater). This suggests an increased contribution from an unlabeled carbon source, such as extracellular pyruvate, lactate, or alanine to the intracellular pyruvate pool following PHD inhibition.

![Figure 4.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig4-v1.jpg)

**Figure 4.:** (A) Mass isotopomer distribution (MID) of pyruvate (PYR) following 72 hr labeling with [U-13C6]-glucose (GLC). (B) MID of citrate after 72 hr labeling with [U-13C6]-GLC (C) MID of citrate after 72 hr labeling with [U-13C5]-glutamine (GLN). Data are mean ± SEM (n=4, p<0.05 indicated as * 0.5% v. 21% oxygen, † BAY v. DMSO, ‡ Δoxygen v. ΔBAY). (D) Fraction of M5 citrate indicating reductive carboxylation after labeling with [U-13C5]-GLN in LFs and PASMCs (n=3–4, * p<0.05).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Lung fibroblasts (LFs) were labeled with the indicated tracers and intracellular metabolites were analyzed by LC-MS after 72 hr. Mass isotopomer distributions were adjusted for natural abundance. Data are the mean ± SEM of four biological replicates. Significant differences in labeling patterns between 21% and 0.5% oxygen (*), DMSO and BAY treatment (†), and 0.5% oxygen and BAY treatment (‡) for each combination of metabolite and tracer are highlighted.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Pulmonary artery smooth muscle cells (PASMCs) were labeled with the indicated tracers and intracellular metabolites were analyzed by LC-MS after 36 hr. Mass isotopomer distributions were adjusted for natural abundance. Data are the mean ± SEM of four biological replicates. Significant differences in labeling patterns between 21% and 0.5% oxygen (*) for each combination of metabolite and tracer are highlighted.

Total citrate labeling from [U-13C6]-glucose was unchanged across the treatment conditions (Figure 4B). We observed decreased M2 and M4 citrate isotopes, consistent with decreased pyruvate dehydrogenase activity in hypoxia. Interestingly, we observed increased M3 and M5 citrate isotopes. Pyruvate carboxylase catalyzes the carboxylation of pyruvate to oxaloacetate after which all three pyruvate carbons are incorporated into citrate by citrate synthase. Thus, this labeling pattern suggests a more prominent contribution of pyruvate carboxylase to sustain TCA cycle anaplerosis despite pyruvate dehydrogenase inhibition following HIF-1α activation. Compared to glucose, glutamine labeled a smaller fraction of citrate, and this labeling was decreased substantially by hypoxia or BAY treatment (Figure 4C), suggesting a less important contribution of glutamine to TCA anaplerosis under these conditions. In addition, the overall fraction of M5 citrate resulting from reductive carboxylation of glutamine-derived α-ketoglutarate was low (<7%) (Figure 4D). Although a hypoxia-mediated increase in M5 citrate was observed, the overall fraction was much less than the 10–20% levels previously reported in cancer cells (Metallo et al., 2011; Wise et al., 2011).

The stable isotope labeling patterns in PASMCs were generally similar to LFs (Figure 4—figure supplement 2). The most notable differences between LF and PASMC labeling were observed in citrate. Compared with LFs, a much lower fraction of total citrate was labeled by glucose in PASMCs. Less activity of pyruvate carboxylase in these cells was suggested by decreased M3 and M5 citrate isotopes after glucose labeling. Interestingly, the M5 citrate fraction in PASMCs was more consistent with previous reports from the cancer literature (Figure 4D), suggesting activation of glutamine anaplerosis for biomass synthesis in these cells.

### Glycolytic flux in hypoxia is closely coupled to cell growth rate

The mass isotopomer distribution for a given metabolite is determined by the complex relationship among the rate of isotope incorporation into the metabolic network, the contributions of unlabeled substrates, and fluxes through related pathways. To clarify how these labeling patterns reflect changes in intracellular metabolite fluxes, we next generated metabolic flux models incorporating the extracellular flux measurements and stable isotope tracing data described above. Preliminary labeling time courses indicated that, even after 72 hr of labeling, intracellular metabolites did not reach isotopic steady state (Figure 5—figure supplement 1). Thus, we performed isotopically non-stationary metabolic flux analysis as implemented by Isotopomer Network Compartment Analysis (INCA; Jazmin and Young, 2013; Murphy and Young, 2013; Young et al., 2014).

Overall, LF and PASMC metabolic fluxes were dominated by high rates of glucose uptake and glycolysis (Figure 5—figure supplement 2). In normoxia, approximately 10% of cytoplasmic pyruvate enters the TCA cycle with the balance converted to lactate. Consistent with the extracellular flux measurements and isotope labeling patterns described above, hypoxia significantly decreased glycolysis, the TCA cycle, and amino acid metabolism (Figure 5A). A significant increase in pentose phosphate pathway flux was also observed, although the absolute flux through this pathway is low. By contrast, HIF-1α activation by BAY in 21% oxygen increased glycolysis and lactate fermentation by nearly 50% (Figure 5B), but had a similar effect as hypoxia on decreasing serine and glutamine uptake. Metabolite fluxes in DMSO-treated cells were similar to 21% oxygen controls (Table 1, Table 2).

![Figure 5.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig5-v1.jpg)

**Figure 5.:** (A) Ratio of modeled metabolic fluxes in 0.5% oxygen compared to 21% oxygen. Fluxes with non-overlapping confidence intervals are highlighted with arrows colored according to the magnitude of the fold change. Arrow thickness corresponds to the absolute flux measured in hypoxia. (B) Ratio of metabolic fluxes in BAY-treated cells compared to DMSO-treated control. Arrows are colored as in (A) and arrow weights correspond to the absolute flux as measured in BAY-treated cells.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** LFs were cultured in 21% or 0.5% oxygen and labeled with the indicated tracers. Intracellular metabolites were analyzed by LC-MS (FBP, fructose-bisphosphate; PYR, pyruvate; CIT, citrate; MAL, malate). Mass isotopomer distributions were calculated and adjusted for natural abundance. Data show the total amount of metabolite labeling (i.e. 1 M0 fractional abundance). Data are the mean ± SEM of four biological replicates.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Metabolic flux model of LF metabolism in 21% oxygen. Arrows are colored by log10(flux). (B) Metabolic flux model of PASMC metabolism in 21% oxygen as in (A).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Ratio of metabolic fluxes in PASMCs compared to LFs. Fluxes with non-overlapping confidence intervals are highlighted with arrows colored according to the magnitude of the change. Arrow thickness corresponds to the absolute flux measured in LFs.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** Ratio of modeled metabolic fluxes in 0.5% oxygen compared to 21% oxygen. Fluxes with non-overlapping confidence intervals are highlighted with arrows colored according to the magnitude of the fold change. Arrow thickness corresponds to the absolute flux measured in hypoxia.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** LF fluxes were normalized to cell growth rate. Graph depicts the ratio of normalized metabolic fluxes in LFs cultured in 0.5% oxygen compared to 21% oxygen control. Fluxes with non-overlapping confidence intervals are highlighted to indicate significant changes.

**Table 1.**
 LF fluxes in 21% and 0.5% oxygen.


<table>
  <thead>
    <tr>
      <th rowspan="2">Type</th>
      <th rowspan="2">Pathway</th>
      <th rowspan="2">ID</th>
      <th rowspan="2">Reaction</th>
      <th colspan="3">21% *</th>
      <th colspan="3">0.5%†</th>
      <th rowspan="2">Ratio</th>
    </tr>
    <tr>
      <th>Flux</th>
      <th>LB</th>
      <th>UB</th>
      <th>Flux</th>
      <th>LB</th>
      <th>UB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="25">NET</td>
      <td rowspan="10">Transport</td>
      <td>GLUT</td>
      <td>GLC.x → GLC</td>
      <td>5.14E+02</td>
      <td>5.11E+02</td>
      <td>5.21E+02</td>
      <td>4.41E+02</td>
      <td>4.26E+02</td>
      <td>4.58E+02</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>PYRR</td>
      <td>PYR.x → PYR.c</td>
      <td>7.56E+01</td>
      <td>7.31E+01</td>
      <td>7.96E+01</td>
      <td>6.21E+01</td>
      <td>5.83E+01</td>
      <td>6.60E+01</td>
      <td>0.82</td>
    </tr>
    <tr>
      <td>MCT</td>
      <td>LAC ↔ LAC.x</td>
      <td>9.99E+02</td>
      <td>9.98E+02</td>
      <td>1.02E+03</td>
      <td>8.91E+02</td>
      <td>8.62E+02</td>
      <td>9.25E+02</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>ALAR</td>
      <td>ALA → ALA.x</td>
      <td>2.25E+00</td>
      <td>1.95E+00</td>
      <td>2.49E+00</td>
      <td>5.84E-01</td>
      <td>1.10E-03</td>
      <td>1.16E+00</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>GLNR</td>
      <td>GLN.x → GLN</td>
      <td>4.15E+01</td>
      <td>4.06E+01</td>
      <td>4.16E+01</td>
      <td>1.43E+01</td>
      <td>1.26E+01</td>
      <td>1.94E+01</td>
      <td>0.34</td>
    </tr>
    <tr>
      <td>GLUR</td>
      <td>GLU ↔ GLU.x</td>
      <td>1.62E+01</td>
      <td>1.58E+01</td>
      <td>1.68E+01</td>
      <td>7.55E+00</td>
      <td>6.88E+00</td>
      <td>8.15E+00</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>ASPR</td>
      <td>ASP → ASP.x</td>
      <td>2.57E+00</td>
      <td>2.53E+00</td>
      <td>2.68E+00</td>
      <td>1.08E+00</td>
      <td>4.17E-01</td>
      <td>1.69E+00</td>
      <td>0.42</td>
    </tr>
    <tr>
      <td>SERR</td>
      <td>SER.x → SER</td>
      <td>1.42E+01</td>
      <td>1.35E+01</td>
      <td>1.49E+01</td>
      <td>5.49E+00</td>
      <td>4.99E+00</td>
      <td>6.06E+00</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td>CYSR</td>
      <td>CYX.x → CYS +CYS</td>
      <td>4.41E+00</td>
      <td>4.23E+00</td>
      <td>4.58E+00</td>
      <td>1.65E+00</td>
      <td>1.32E+00</td>
      <td>2.08E+00</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>GLYR</td>
      <td>GLY → GLY.x</td>
      <td>2.05E+00</td>
      <td>1.90E+00</td>
      <td>2.15E+00</td>
      <td>2.60E-01</td>
      <td>2.00E-02</td>
      <td>4.92E-01</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td rowspan="11">Glycolysis</td>
      <td>HK</td>
      <td>GLC → G6P</td>
      <td>5.14E+02</td>
      <td>5.11E+02</td>
      <td>5.21E+02</td>
      <td>4.41E+02</td>
      <td>4.26E+02</td>
      <td>4.58E+02</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>PGI</td>
      <td>G6P ↔ F6P</td>
      <td>5.11E+02</td>
      <td>4.99E+02</td>
      <td>5.24E+02</td>
      <td>4.23E+02</td>
      <td>4.04E+02</td>
      <td>4.40E+02</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>PFK</td>
      <td>F6P → FBP</td>
      <td>5.09E+02</td>
      <td>5.00E+02</td>
      <td>5.12E+02</td>
      <td>4.32E+02</td>
      <td>4.17E+02</td>
      <td>4.49E+02</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>ALDO</td>
      <td>FBP ↔ DHAP +GAP</td>
      <td>5.09E+02</td>
      <td>5.00E+02</td>
      <td>5.12E+02</td>
      <td>4.32E+02</td>
      <td>4.17E+02</td>
      <td>4.49E+02</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>TPI</td>
      <td>DHAP ↔ GAP</td>
      <td>5.08E+02</td>
      <td>5.06E+02</td>
      <td>5.08E+02</td>
      <td>4.31E+02</td>
      <td>4.15E+02</td>
      <td>4.48E+02</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>GAP ↔ 3 PG</td>
      <td>1.02E+03</td>
      <td>9.96E+02</td>
      <td>1.04E+03</td>
      <td>8.69E+02</td>
      <td>8.35E+02</td>
      <td>9.03E+02</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>ENO</td>
      <td>3 PG → PEP</td>
      <td>1.01E+03</td>
      <td>9.99E+02</td>
      <td>1.03E+03</td>
      <td>8.68E+02</td>
      <td>8.36E+02</td>
      <td>9.00E+02</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>PK</td>
      <td>PEP → PYR.c</td>
      <td>1.04E+03</td>
      <td>9.95E+02</td>
      <td>1.04E+03</td>
      <td>8.78E+02</td>
      <td>8.36E+02</td>
      <td>9.21E+02</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>PYR.c ↔ LAC</td>
      <td>9.99E+02</td>
      <td>9.98E+02</td>
      <td>1.02E+03</td>
      <td>8.91E+02</td>
      <td>8.62E+02</td>
      <td>9.25E+02</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>GPT1</td>
      <td>PYR.c ↔ ALA</td>
      <td>1.19E+01</td>
      <td>9.12E+00</td>
      <td>1.19E+01</td>
      <td>5.55E+00</td>
      <td>–9.08E+02</td>
      <td>6.13E+00</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>GPT2</td>
      <td>PYR.m ↔ ALA</td>
      <td>–2.58E+00</td>
      <td>–4.56E+00</td>
      <td>2.87E+00</td>
      <td>–2.40E-03</td>
      <td>–3.22E+01</td>
      <td>9.11E+02</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">Pentose phosphate pathway</td>
      <td>G6PD</td>
      <td>G6P → P5P+CO2</td>
      <td>1.26E-07</td>
      <td>0.00E+00</td>
      <td>3.91E-01</td>
      <td>1.62E+01</td>
      <td>4.41E+00</td>
      <td>2.89E+01</td>
      <td>128571428.57</td>
    </tr>
    <tr>
      <td>TK1</td>
      <td>P5P+P5 P ↔ S7P+GAP</td>
      <td>–9.11E-01</td>
      <td>–9.29E-01</td>
      <td>–8.30E-01</td>
      <td>4.76E+00</td>
      <td>–1.22E-01</td>
      <td>9.62E+00</td>
      <td>–5.23</td>
    </tr>
    <tr>
      <td>TA</td>
      <td>S7P+GAP ↔ F6P+E4 P</td>
      <td>–9.11E-01</td>
      <td>–9.29E-01</td>
      <td>–8.30E-01</td>
      <td>4.76E+00</td>
      <td>–1.22E-01</td>
      <td>9.62E+00</td>
      <td>–5.23</td>
    </tr>
    <tr>
      <td>TK2</td>
      <td>P5P+E4 P ↔ F6P+GAP</td>
      <td>–9.11E-01</td>
      <td>–9.29E-01</td>
      <td>–8.30E-01</td>
      <td>4.76E+00</td>
      <td>–1.22E-01</td>
      <td>9.62E+00</td>
      <td>–5.23</td>
    </tr>
    <tr>
      <td rowspan="24"></td>
      <td rowspan="8">Anaplerosis</td>
      <td>PYRT</td>
      <td>PYR.c → PYR.m</td>
      <td>1.16E+02</td>
      <td>1.16E+02</td>
      <td>1.19E+02</td>
      <td>4.42E+01</td>
      <td>3.82E+01</td>
      <td>9.58E+02</td>
      <td></td>
    </tr>
    <tr>
      <td>PC</td>
      <td>PYR.m+CO2 → OAC</td>
      <td>1.88E+01</td>
      <td>1.74E+01</td>
      <td>1.91E+01</td>
      <td>1.37E+01</td>
      <td>9.82E+00</td>
      <td>2.69E+01</td>
      <td></td>
    </tr>
    <tr>
      <td>PEPCK</td>
      <td>OAC → PEP +CO2</td>
      <td>2.56E+01</td>
      <td>1.58E+01</td>
      <td>2.57E+01</td>
      <td>9.66E+00</td>
      <td>0.00E+00</td>
      <td>2.60E+01</td>
      <td></td>
    </tr>
    <tr>
      <td>ME2</td>
      <td>MAL → PYR.m +CO2</td>
      <td>2.05E+00</td>
      <td>9.51E-02</td>
      <td>2.68E+00</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.25E+01</td>
      <td></td>
    </tr>
    <tr>
      <td>ME1</td>
      <td>MAL → PYR.c +CO2</td>
      <td>2.78E-02</td>
      <td>0.00E+00</td>
      <td>2.63E+01</td>
      <td>8.71E-05</td>
      <td>0.00E+00</td>
      <td>2.52E+01</td>
      <td></td>
    </tr>
    <tr>
      <td>FAO</td>
      <td>FAO → AcCoA.m</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.13E+00</td>
      <td>6.58E-06</td>
      <td>0.00E+00</td>
      <td>7.73E-01</td>
      <td></td>
    </tr>
    <tr>
      <td>GLDH</td>
      <td>GLU ↔ AKG</td>
      <td>1.71E+01</td>
      <td>1.56E+01</td>
      <td>1.84E+01</td>
      <td>9.11E-01</td>
      <td>–6.16E-01</td>
      <td>7.27E+00</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>GLS</td>
      <td>GLN ↔ GLU</td>
      <td>3.78E+01</td>
      <td>3.60E+01</td>
      <td>3.86E+01</td>
      <td>1.17E+01</td>
      <td>1.01E+01</td>
      <td>1.70E+01</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td rowspan="8">Tricarboxylic acid cycle</td>
      <td>PDH</td>
      <td>PYR.m → AcCoA.m +CO2</td>
      <td>1.02E+02</td>
      <td>8.76E+01</td>
      <td>1.15E+02</td>
      <td>3.05E+01</td>
      <td>2.86E+01</td>
      <td>5.24E+01</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>CS</td>
      <td>AcCoA.m+OAC → CIT</td>
      <td>1.02E+02</td>
      <td>8.30E+01</td>
      <td>1.11E+02</td>
      <td>3.05E+01</td>
      <td>2.88E+01</td>
      <td>5.09E+01</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>IDH</td>
      <td>CIT ↔ AKG +CO2</td>
      <td>2.49E+01</td>
      <td>2.42E+01</td>
      <td>2.53E+01</td>
      <td>1.01E+01</td>
      <td>8.75E+00</td>
      <td>1.41E+01</td>
      <td>0.41</td>
    </tr>
    <tr>
      <td>OGDH</td>
      <td>AKG → SUC +CO2</td>
      <td>4.19E+01</td>
      <td>4.01E+01</td>
      <td>4.25E+01</td>
      <td>1.10E+01</td>
      <td>7.87E+00</td>
      <td>2.02E+01</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>SDH</td>
      <td>SUC ↔ FUM</td>
      <td>4.19E+01</td>
      <td>4.01E+01</td>
      <td>4.25E+01</td>
      <td>1.10E+01</td>
      <td>7.87E+00</td>
      <td>2.02E+01</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>FH</td>
      <td>FUM ↔ MAL</td>
      <td>4.19E+01</td>
      <td>4.01E+01</td>
      <td>4.25E+01</td>
      <td>1.10E+01</td>
      <td>7.87E+00</td>
      <td>2.02E+01</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>MDH</td>
      <td>MAL ↔ OAC</td>
      <td>1.17E+02</td>
      <td>1.08E+02</td>
      <td>1.24E+02</td>
      <td>3.14E+01</td>
      <td>2.62E+01</td>
      <td>5.70E+01</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>GOT</td>
      <td>OAC ↔ ASP</td>
      <td>8.11E+00</td>
      <td>8.06E+00</td>
      <td>8.23E+00</td>
      <td>4.98E+00</td>
      <td>4.32E+00</td>
      <td>5.64E+00</td>
      <td>0.61</td>
    </tr>
    <tr>
      <td rowspan="5">Amino acid metabolism</td>
      <td>PST</td>
      <td>3 PG → SER</td>
      <td>1.95E+00</td>
      <td>1.63E+00</td>
      <td>2.00E+00</td>
      <td>2.42E-01</td>
      <td>1.34E-01</td>
      <td>3.57E+01</td>
      <td></td>
    </tr>
    <tr>
      <td>SHT</td>
      <td>SER ↔ GLY +MEETHF</td>
      <td>6.38E+00</td>
      <td>6.22E+00</td>
      <td>6.43E+00</td>
      <td>3.91E+00</td>
      <td>3.71E+00</td>
      <td>4.10E+00</td>
      <td>0.61</td>
    </tr>
    <tr>
      <td>CYST</td>
      <td>SER ↔ CYS</td>
      <td>–7.12E+00</td>
      <td>–7.19E+00</td>
      <td>–6.81E+00</td>
      <td>–2.10E+00</td>
      <td>–2.97E+00</td>
      <td>–1.44E+00</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>SD</td>
      <td>SER → PYR.c</td>
      <td>1.17E+01</td>
      <td>1.04E+01</td>
      <td>1.20E+01</td>
      <td>2.82E-01</td>
      <td>0.00E+00</td>
      <td>1.47E+00</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>GLYS</td>
      <td>CO2 +MEETHF → GLY</td>
      <td>3.39E+00</td>
      <td>3.35E+00</td>
      <td>3.49E+00</td>
      <td>1.80E+00</td>
      <td>1.66E+00</td>
      <td>1.93E+00</td>
      <td>0.53</td>
    </tr>
    <tr>
      <td rowspan="3">Biomass</td>
      <td>BIOMASS</td>
      <td>1216*AcCoA.c+295.6*ALA +232.4*ASP +114.7*CO2 +71.43*CYS +57.14*DHAP +142.4*G6P+158.6*GLN +190.1*GLU +324.2*GLY +125.6*MEETHF +114.7*P5P+217.2*SER → biomass</td>
      <td>2.38E-02</td>
      <td>2.34E-02</td>
      <td>2.39E-02</td>
      <td>1.68E-02</td>
      <td>1.61E-02</td>
      <td>1.75E-02</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>ACL</td>
      <td>CIT → AcCoA.c +MAL</td>
      <td>7.74E+01</td>
      <td>6.29E+01</td>
      <td>1.04E+02</td>
      <td>2.04E+01</td>
      <td>1.95E+01</td>
      <td>3.71E+01</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>LIPS</td>
      <td>AcCoA.c → lipid</td>
      <td>4.84E+01</td>
      <td>4.55E+01</td>
      <td>4.84E+01</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.68E+01</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="3"></td>
      <td rowspan="3">Mixing</td>
      <td>cPYR</td>
      <td>0*PYR.c → PYR.ms</td>
      <td>1.00E+00</td>
      <td>8.47E-01</td>
      <td>1.00E+00</td>
      <td>1.42E-01</td>
      <td>0.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>mPYR</td>
      <td>0*PYR.m → PYR.ms</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.53E-01</td>
      <td>8.58E-01</td>
      <td>0.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>sPYR</td>
      <td>PYR.ms → PYR.fix</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="21">EXCH</td>
      <td rowspan="2">Transport</td>
      <td>MCT</td>
      <td>LAC ↔ LAC.x</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.05E-01</td>
      <td>1.52E+03</td>
      <td>1.35E+03</td>
      <td>2.41E+03</td>
      <td>15200000000</td>
    </tr>
    <tr>
      <td>GLUR</td>
      <td>GLU ↔ GLU.x</td>
      <td>5.10E+00</td>
      <td>4.77E+00</td>
      <td>5.23E+00</td>
      <td>1.54E+00</td>
      <td>1.11E+00</td>
      <td>2.54E+00</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td rowspan="7">Glycolysis</td>
      <td>PGI</td>
      <td>G6P ↔ F6P</td>
      <td>2.78E+05</td>
      <td>1.77E+05</td>
      <td>Inf</td>
      <td>2.46E+05</td>
      <td>0.00E+00</td>
      <td>Inf</td>
      <td></td>
    </tr>
    <tr>
      <td>ALDO</td>
      <td>FBP ↔ DHAP +GAP</td>
      <td>1.43E+02</td>
      <td>1.43E+02</td>
      <td>1.43E+02</td>
      <td>3.20E+02</td>
      <td>2.79E+02</td>
      <td>3.60E+02</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>TPI</td>
      <td>DHAP ↔ GAP</td>
      <td>4.33E+03</td>
      <td>4.33E+03</td>
      <td>1.09E+04</td>
      <td>1.70E+03</td>
      <td>1.06E+03</td>
      <td>3.06E+03</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>GAP ↔ 3 PG</td>
      <td>4.42E+02</td>
      <td>4.72E+00</td>
      <td>4.50E+02</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.39E+02</td>
      <td></td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>PYR.c ↔ LAC</td>
      <td>1.63E+03</td>
      <td>1.62E+03</td>
      <td>1.80E+03</td>
      <td>4.80E+00</td>
      <td>0.00E+00</td>
      <td>3.51E+02</td>
      <td>0</td>
    </tr>
    <tr>
      <td>GPT1</td>
      <td>PYR.c ↔ ALA</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.61E-01</td>
      <td>8.32E+02</td>
      <td>0.00E+00</td>
      <td>9.06E+02</td>
      <td></td>
    </tr>
    <tr>
      <td>GPT2</td>
      <td>PYR.m ↔ ALA</td>
      <td>4.21E-04</td>
      <td>0.00E+00</td>
      <td>2.92E+00</td>
      <td>1.28E-04</td>
      <td>0.00E+00</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">Pentose phosphate pathway</td>
      <td>TK1</td>
      <td>P5P+P5 P ↔ S7P+GAP</td>
      <td>9.97E+04</td>
      <td>6.27E+03</td>
      <td>Inf</td>
      <td>1.47E+02</td>
      <td>6.67E+01</td>
      <td>2.60E+02</td>
      <td>0</td>
    </tr>
    <tr>
      <td>TA</td>
      <td>S7P+GAP ↔ F6P+E4 P</td>
      <td>5.93E+00</td>
      <td>5.79E+00</td>
      <td>6.97E+00</td>
      <td>2.35E-04</td>
      <td>0.00E+00</td>
      <td>7.54E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>TK2</td>
      <td>P5P+E4 P ↔ F6P+GAP</td>
      <td>1.00E+07</td>
      <td>-Inf</td>
      <td>Inf</td>
      <td>9.05E+00</td>
      <td>4.10E+00</td>
      <td>1.43E+01</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Anaplerosis</td>
      <td>GLDH</td>
      <td>GLU ↔ AKG</td>
      <td>1.52E+03</td>
      <td>1.52E+03</td>
      <td>7.13E+03</td>
      <td>3.78E+02</td>
      <td>1.93E+02</td>
      <td>1.94E+03</td>
      <td></td>
    </tr>
    <tr>
      <td>GLS</td>
      <td>GLN ↔ GLU</td>
      <td>3.99E-01</td>
      <td>0.00E+00</td>
      <td>8.04E-01</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>3.84E-01</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="5">Tricarboxylic acid cycle</td>
      <td>IDH</td>
      <td>CIT ↔ AKG +CO2</td>
      <td>4.55E+00</td>
      <td>4.03E+00</td>
      <td>5.19E+00</td>
      <td>2.52E+00</td>
      <td>1.80E+00</td>
      <td>4.50E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>SDH</td>
      <td>SUC ↔ FUM</td>
      <td>1.22E+03</td>
      <td></td>
      <td>Inf</td>
      <td>7.60E+01</td>
      <td>2.57E+01</td>
      <td>Inf</td>
      <td></td>
    </tr>
    <tr>
      <td>FH</td>
      <td>FUM ↔ MAL</td>
      <td>3.66E+05</td>
      <td>1.95E+05</td>
      <td>Inf</td>
      <td>5.05E+05</td>
      <td>3.06E+02</td>
      <td>Inf</td>
      <td></td>
    </tr>
    <tr>
      <td>MDH</td>
      <td>MAL ↔ OAC</td>
      <td>1.11E+03</td>
      <td>7.88E+02</td>
      <td>2.38E+03</td>
      <td>1.33E+02</td>
      <td>7.22E+01</td>
      <td>3.25E+02</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>GOT</td>
      <td>OAC ↔ ASP</td>
      <td>1.00E+07</td>
      <td>-Inf</td>
      <td>Inf</td>
      <td>4.42E+01</td>
      <td>0.00E+00</td>
      <td>Inf</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Amino acid metabolism</td>
      <td>SHT</td>
      <td>SER ↔ GLY +MEETHF</td>
      <td>5.10E+00</td>
      <td>8.92E-01</td>
      <td>5.25E+00</td>
      <td>6.07E-07</td>
      <td>0.00E+00</td>
      <td>3.32E+02</td>
      <td></td>
    </tr>
    <tr>
      <td>CYST</td>
      <td>SER ↔ CYS</td>
      <td>1.52E-05</td>
      <td>0.00E+00</td>
      <td>2.55E-04</td>
      <td>1.46E-02</td>
      <td>0.00E+00</td>
      <td>Inf</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*SSR 391.7 [311.2‐416.6] (95% CI, 362 DOF).†SSR 334.3 [311.2‐416.6] (95% CI, 362 DOF)._

**Table 2.**
 LF fluxes following DMSO and BAY treatment.


<table>
  <thead>
    <tr>
      <th rowspan="2">Type</th>
      <th rowspan="2">Pathway</th>
      <th rowspan="2">ID</th>
      <th rowspan="2">Reaction</th>
      <th colspan="3">DMSO*</th>
      <th colspan="3">BAY†</th>
      <th rowspan="2">Ratio</th>
    </tr>
    <tr>
      <th>Flux</th>
      <th>LB</th>
      <th>UB</th>
      <th>Flux</th>
      <th>LB</th>
      <th>UB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="33">NET</td>
      <td rowspan="10">Transport</td>
      <td>GLUT</td>
      <td>GLC.x → GLC</td>
      <td>6.12E+02</td>
      <td>6.12E+02</td>
      <td>6.12E+02</td>
      <td>8.80E+02</td>
      <td>8.80E+02</td>
      <td>8.80E+02</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>PYRR</td>
      <td>PYR.x → PYR.c</td>
      <td>9.98E+01</td>
      <td>9.95E+01</td>
      <td>1.01E+02</td>
      <td>6.06E+01</td>
      <td>6.06E+01</td>
      <td>6.06E+01</td>
      <td>0.61</td>
    </tr>
    <tr>
      <td>MCT</td>
      <td>LAC ↔ LAC.x</td>
      <td>8.19E+02</td>
      <td>8.17E+02</td>
      <td>8.20E+02</td>
      <td>1.33E+03</td>
      <td>1.33E+03</td>
      <td>1.33E+03</td>
      <td>1.62</td>
    </tr>
    <tr>
      <td>ALAR</td>
      <td>ALA → ALA.x</td>
      <td>2.67E+00</td>
      <td>2.36E+00</td>
      <td>3.29E+00</td>
      <td>5.98E+00</td>
      <td>5.88E+00</td>
      <td>6.24E+00</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>GLNR</td>
      <td>GLN.x → GLN</td>
      <td>3.78E+01</td>
      <td>3.77E+01</td>
      <td>3.79E+01</td>
      <td>2.06E+01</td>
      <td>2.06E+01</td>
      <td>2.06E+01</td>
      <td>0.54</td>
    </tr>
    <tr>
      <td>GLUR</td>
      <td>GLU ↔ GLU.x</td>
      <td>1.61E+01</td>
      <td>1.56E+01</td>
      <td>1.62E+01</td>
      <td>1.68E+01</td>
      <td>1.68E+01</td>
      <td>1.68E+01</td>
      <td>1.05</td>
    </tr>
    <tr>
      <td>ASPR</td>
      <td>ASP → ASP.x</td>
      <td>2.36E+00</td>
      <td>2.32E+00</td>
      <td>2.49E+00</td>
      <td>1.80E+00</td>
      <td>1.80E+00</td>
      <td>1.81E+00</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td>SERR</td>
      <td>SER.x → SER</td>
      <td>1.03E+01</td>
      <td>1.03E+01</td>
      <td>1.06E+01</td>
      <td>2.50E+00</td>
      <td>2.50E+00</td>
      <td>2.50E+00</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>CYSR</td>
      <td>CYX.x → CYS+CYS</td>
      <td>2.79E+00</td>
      <td>2.79E+00</td>
      <td>2.95E+00</td>
      <td>3.07E-01</td>
      <td>3.06E-01</td>
      <td>3.07E-01</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>GLYR</td>
      <td>GLY → GLY.x</td>
      <td>2.52E+00</td>
      <td>2.30E+00</td>
      <td>2.73E+00</td>
      <td>5.52E-01</td>
      <td>4.30E-01</td>
      <td>7.45E-01</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td rowspan="11">Glycolysis</td>
      <td>HK</td>
      <td>GLC → G6P</td>
      <td>6.12E+02</td>
      <td>6.12E+02</td>
      <td>6.12E+02</td>
      <td>8.80E+02</td>
      <td>8.80E+02</td>
      <td>8.80E+02</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>PGI</td>
      <td>G6P ↔ F6P</td>
      <td>6.09E+02</td>
      <td>6.08E+02</td>
      <td>6.09E+02</td>
      <td>8.42E+02</td>
      <td>8.42E+02</td>
      <td>8.42E+02</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>PFK</td>
      <td>F6P → FBP</td>
      <td>6.07E+02</td>
      <td>6.07E+02</td>
      <td>6.07E+02</td>
      <td>8.65E+02</td>
      <td>8.65E+02</td>
      <td>8.65E+02</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td>ALDO</td>
      <td>FBP ↔ DHAP+GAP</td>
      <td>6.07E+02</td>
      <td>6.07E+02</td>
      <td>6.07E+02</td>
      <td>8.65E+02</td>
      <td>8.65E+02</td>
      <td>8.65E+02</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td>TPI</td>
      <td>DHAP ↔ GAP</td>
      <td>6.06E+02</td>
      <td>6.06E+02</td>
      <td>6.06E+02</td>
      <td>8.65E+02</td>
      <td>8.65E+02</td>
      <td>8.65E+02</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>GAP ↔ 3PG</td>
      <td>1.21E+03</td>
      <td>1.21E+03</td>
      <td>1.21E+03</td>
      <td>1.74E+03</td>
      <td>1.74E+03</td>
      <td>1.74E+03</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>ENO</td>
      <td>3PG → PEP</td>
      <td>1.21E+03</td>
      <td>1.21E+03</td>
      <td>1.21E+03</td>
      <td>1.57E+03</td>
      <td>1.57E+03</td>
      <td>1.57E+03</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>PK</td>
      <td>PEP → PYR.c</td>
      <td>1.23E+03</td>
      <td>1.19E+03</td>
      <td>1.23E+03</td>
      <td>1.65E+03</td>
      <td>1.65E+03</td>
      <td>1.65E+03</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>PYR.c ↔ LAC</td>
      <td>8.19E+02</td>
      <td>8.17E+02</td>
      <td>8.20E+02</td>
      <td>1.33E+03</td>
      <td>1.33E+03</td>
      <td>1.33E+03</td>
      <td>1.62</td>
    </tr>
    <tr>
      <td>GPT1</td>
      <td>PYR.c ↔ ALA</td>
      <td>9.62E+00</td>
      <td>9.44E+00</td>
      <td>9.62E+00</td>
      <td>9.36E+00</td>
      <td>9.32E+00</td>
      <td>9.42E+00</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>GPT2</td>
      <td>PYR.m ↔ ALA</td>
      <td>1.14E-01</td>
      <td></td>
      <td></td>
      <td>2.28E-07</td>
      <td>–1.22E-05</td>
      <td>6.41E-04</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">Pentose phosphate pathway</td>
      <td>G6PD</td>
      <td>G6P → P5P+CO2</td>
      <td>2.02E-02</td>
      <td>0.00E+00</td>
      <td>1.08E+00</td>
      <td>3.64E+01</td>
      <td>3.64E+01</td>
      <td>3.64E+01</td>
      <td>1801.98</td>
    </tr>
    <tr>
      <td>TK1</td>
      <td>P5P+P5P ↔ S7P+GAP</td>
      <td>–9.06E-01</td>
      <td>–9.28E-01</td>
      <td>–9.06E-01</td>
      <td>1.17E+01</td>
      <td>1.17E+01</td>
      <td>1.17E+01</td>
      <td>–12.89</td>
    </tr>
    <tr>
      <td>TA</td>
      <td>S7P+GAP ↔ F6P+E4P</td>
      <td>–9.06E-01</td>
      <td>–9.28E-01</td>
      <td>–9.06E-01</td>
      <td>1.17E+01</td>
      <td>1.17E+01</td>
      <td>1.17E+01</td>
      <td>–12.89</td>
    </tr>
    <tr>
      <td>TK2</td>
      <td>P5P+E4P ↔ F6P+GAP</td>
      <td>–9.06E-01</td>
      <td>–9.28E-01</td>
      <td>–9.06E-01</td>
      <td>1.17E+01</td>
      <td>1.17E+01</td>
      <td>1.17E+01</td>
      <td>–12.89</td>
    </tr>
    <tr>
      <td rowspan="8">Anaplerosis</td>
      <td>PYRT</td>
      <td>PYR.c → PYR.m</td>
      <td>4.99E+02</td>
      <td>4.97E+02</td>
      <td>4.99E+02</td>
      <td>5.50E+02</td>
      <td>5.50E+02</td>
      <td>5.50E+02</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>PC</td>
      <td>PYR.m+CO2 → OAC</td>
      <td>2.11E+01</td>
      <td>2.07E+01</td>
      <td>2.17E+01</td>
      <td>9.05E+01</td>
      <td>9.05E+01</td>
      <td>9.05E+01</td>
      <td>4.28</td>
    </tr>
    <tr>
      <td>PEPCK</td>
      <td>OAC → PEP+CO2</td>
      <td>1.36E+01</td>
      <td>1.36E+01</td>
      <td>1.37E+01</td>
      <td>8.58E+01</td>
      <td>8.58E+01</td>
      <td>8.58E+01</td>
      <td>6.31</td>
    </tr>
    <tr>
      <td>ME2</td>
      <td>MAL → PYR.m+CO2</td>
      <td>1.30E+01</td>
      <td>1.28E+01</td>
      <td>1.37E+01</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>9.49E-06</td>
      <td>0</td>
    </tr>
    <tr>
      <td>ME1</td>
      <td>MAL → PYR.c+CO2</td>
      <td>3.20E-03</td>
      <td>0.00E+00</td>
      <td>1.73E+00</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.15E-05</td>
      <td></td>
    </tr>
    <tr>
      <td>FAO</td>
      <td>FAO → AcCoA.m</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>3.48E+00</td>
      <td>1.09E-04</td>
      <td>8.34E-06</td>
      <td>4.14E-02</td>
      <td></td>
    </tr>
    <tr>
      <td>GLDH</td>
      <td>GLU ↔ AKG</td>
      <td>1.33E+01</td>
      <td>1.31E+01</td>
      <td>1.35E+01</td>
      <td>–2.46E-01</td>
      <td>–2.47E-01</td>
      <td>–2.46E-01</td>
      <td>–0.02</td>
    </tr>
    <tr>
      <td>GLS</td>
      <td>GLN ↔ GLU</td>
      <td>3.40E+01</td>
      <td>3.35E+01</td>
      <td>3.42E+01</td>
      <td>1.88E+01</td>
      <td>1.88E+01</td>
      <td>1.88E+01</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td rowspan="19"></td>
      <td rowspan="8">Tricarboxylic acid cycle</td>
      <td>PDH</td>
      <td>PYR.m → AcCoA.m+CO2</td>
      <td>4.90E+02</td>
      <td>4.90E+02</td>
      <td>4.92E+02</td>
      <td>4.60E+02</td>
      <td>4.60E+02</td>
      <td>4.60E+02</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>CS</td>
      <td>AcCoA.m+OAC → CIT</td>
      <td>4.90E+02</td>
      <td>4.84E+02</td>
      <td>4.91E+02</td>
      <td>4.60E+02</td>
      <td>4.60E+02</td>
      <td>4.60E+02</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>IDH</td>
      <td>CIT ↔ AKG+CO2</td>
      <td>2.70E+01</td>
      <td>2.70E+01</td>
      <td>2.76E+01</td>
      <td>1.45E+01</td>
      <td>1.45E+01</td>
      <td>1.45E+01</td>
      <td>0.54</td>
    </tr>
    <tr>
      <td>OGDH</td>
      <td>AKG → SUC+CO2</td>
      <td>4.03E+01</td>
      <td>3.99E+01</td>
      <td>4.04E+01</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>SDH</td>
      <td>SUC ↔ FUM</td>
      <td>4.03E+01</td>
      <td>3.99E+01</td>
      <td>4.04E+01</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>FH</td>
      <td>FUM ↔ MAL</td>
      <td>4.03E+01</td>
      <td>3.99E+01</td>
      <td>4.04E+01</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>MDH</td>
      <td>MAL ↔ OAC</td>
      <td>4.91E+02</td>
      <td>4.91E+02</td>
      <td>4.92E+02</td>
      <td>4.60E+02</td>
      <td>4.60E+02</td>
      <td>4.60E+02</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>GOT</td>
      <td>OAC ↔ ASP</td>
      <td>7.91E+00</td>
      <td>7.76E+00</td>
      <td>7.98E+00</td>
      <td>4.46E+00</td>
      <td>4.46E+00</td>
      <td>4.46E+00</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td rowspan="5">Amino acid metabolism</td>
      <td>PST</td>
      <td>3PG → SER</td>
      <td>4.03E-01</td>
      <td>3.74E-01</td>
      <td>5.04E-01</td>
      <td>1.73E+02</td>
      <td>1.73E+02</td>
      <td>1.73E+02</td>
      <td>429.83</td>
    </tr>
    <tr>
      <td>SHT</td>
      <td>SER ↔ GLY+MEETHF</td>
      <td>6.63E+00</td>
      <td>6.59E+00</td>
      <td>6.65E+00</td>
      <td>2.85E+00</td>
      <td>2.79E+00</td>
      <td>2.93E+00</td>
      <td>0.43</td>
    </tr>
    <tr>
      <td>CYST</td>
      <td>SER ↔ CYS</td>
      <td>–3.88E+00</td>
      <td>–3.91E+00</td>
      <td>–3.87E+00</td>
      <td>2.03E-01</td>
      <td>2.02E-01</td>
      <td>2.03E-01</td>
      <td>–0.05</td>
    </tr>
    <tr>
      <td>SD</td>
      <td>SER → PYR.c</td>
      <td>2.80E+00</td>
      <td>2.80E+00</td>
      <td>2.80E+00</td>
      <td>1.70E+02</td>
      <td>1.70E+02</td>
      <td>1.70E+02</td>
      <td>60.81</td>
    </tr>
    <tr>
      <td>GLYS</td>
      <td>CO2+MEETHF → GLY</td>
      <td>3.63E+00</td>
      <td>3.50E+00</td>
      <td>3.65E+00</td>
      <td>1.41E+00</td>
      <td>1.30E+00</td>
      <td>1.46E+00</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td rowspan="3">Biomass</td>
      <td>BIOMASS</td>
      <td>1216*AcCoA.c+295.6*ALA +232.4*ASP+114.7*CO2+71.43*CYS+57.14*DHAP+142.4*G6P+158.6*GLN+190.1*GLU +324.2*GLY+125.6*MEETHF+114.7*P5P+217.2*SER → biomass</td>
      <td>2.39E-02</td>
      <td>2.39E-02</td>
      <td>2.50E-02</td>
      <td>1.14E-02</td>
      <td>1.14E-02</td>
      <td>1.14E-02</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>ACL</td>
      <td>CIT → AcCoA.c+MAL</td>
      <td>4.63E+02</td>
      <td>4.63E+02</td>
      <td>4.66E+02</td>
      <td>4.45E+02</td>
      <td>4.45E+02</td>
      <td>4.45E+02</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>LIPS</td>
      <td>AcCoA.c → lipid</td>
      <td>4.34E+02</td>
      <td>4.29E+02</td>
      <td>4.34E+02</td>
      <td>4.32E+02</td>
      <td>4.32E+02</td>
      <td>4.32E+02</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">Mixing</td>
      <td>cPYR</td>
      <td>0*PYR.c → PYR.ms</td>
      <td>1.00E+00</td>
      <td>9.99E-01</td>
      <td>1.00E+00</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>mPYR</td>
      <td>0*PYR.m → PYR.ms</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>9.83E-04</td>
      <td>1.00E+00</td>
      <td>0.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>sPYR</td>
      <td>PYR.ms → PYR.fix</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="21">EXCH</td>
      <td rowspan="2">Transport</td>
      <td>MCT</td>
      <td>LAC ↔ LAC.x</td>
      <td>6.24E-04</td>
      <td>0.00E+00</td>
      <td>3.56E+00</td>
      <td>7.11E+02</td>
      <td>7.11E+02</td>
      <td>7.11E+02</td>
      <td>1139423.08</td>
    </tr>
    <tr>
      <td>GLUR</td>
      <td>GLU ↔ GLU.x</td>
      <td>5.06E+00</td>
      <td>4.82E+00</td>
      <td>5.75E+00</td>
      <td>3.48E+00</td>
      <td>3.48E+00</td>
      <td>3.48E+00</td>
      <td>0.69</td>
    </tr>
    <tr>
      <td rowspan="7">Glycolysis</td>
      <td>PGI</td>
      <td>G6P ↔ F6P</td>
      <td>1.40E+06</td>
      <td>1.39E+06</td>
      <td>Inf</td>
      <td>4.31E+06</td>
      <td>4.31E+06</td>
      <td>4.31E+06</td>
      <td></td>
    </tr>
    <tr>
      <td>ALDO</td>
      <td>FBP ↔ DHAP+GAP</td>
      <td>2.38E+02</td>
      <td>2.38E+02</td>
      <td>2.38E+02</td>
      <td>1.02E+03</td>
      <td>1.02E+03</td>
      <td>1.02E+03</td>
      <td>4.28</td>
    </tr>
    <tr>
      <td>TPI</td>
      <td>DHAP ↔ GAP</td>
      <td>9.99E+06</td>
      <td></td>
      <td>Inf</td>
      <td>7.57E+03</td>
      <td>7.57E+03</td>
      <td>7.57E+03</td>
      <td></td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>GAP ↔ 3PG</td>
      <td>5.81E+02</td>
      <td>5.81E+02</td>
      <td>7.25E+02</td>
      <td>1.09E+02</td>
      <td>1.07E+02</td>
      <td>1.09E+02</td>
      <td>0.19</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>PYR.c ↔ LAC</td>
      <td>2.65E+03</td>
      <td>2.58E+03</td>
      <td>2.65E+03</td>
      <td>4.92E+01</td>
      <td>4.91E+01</td>
      <td>4.94E+01</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>GPT1</td>
      <td>PYR.c ↔ ALA</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>5.60E-02</td>
      <td>2.45E+03</td>
      <td>2.45E+03</td>
      <td>2.45E+03</td>
      <td>24500000000</td>
    </tr>
    <tr>
      <td>GPT2</td>
      <td>PYR.m ↔ ALA</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>5.65E-02</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.20E-05</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">Pentose phosphate pathway</td>
      <td>TK1</td>
      <td>P5P+P5P ↔ S7P+GAP</td>
      <td>1.28E+06</td>
      <td>9.01E+03</td>
      <td>Inf</td>
      <td>1.00E+07</td>
      <td>-Inf</td>
      <td>Inf</td>
      <td></td>
    </tr>
    <tr>
      <td>TA</td>
      <td>S7P+GAP ↔ F6P+E4P</td>
      <td>8.89E+00</td>
      <td>8.88E+00</td>
      <td>9.53E+00</td>
      <td>5.10E+01</td>
      <td>5.10E+01</td>
      <td>5.10E+01</td>
      <td>5.74</td>
    </tr>
    <tr>
      <td>TK2</td>
      <td>P5P+E4P ↔ F6P+GAP</td>
      <td>6.93E+00</td>
      <td>5.12E+00</td>
      <td>6.98E+00</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.56E-04</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">Anaplerosis</td>
      <td>GLDH</td>
      <td>GLU ↔ AKG</td>
      <td>5.63E+03</td>
      <td>4.43E+03</td>
      <td>5.66E+03</td>
      <td>1.42E+03</td>
      <td>1.42E+03</td>
      <td>1.42E+03</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>GLS</td>
      <td>GLN ↔ GLU</td>
      <td>1.27E+00</td>
      <td>1.20E+00</td>
      <td>1.50E+00</td>
      <td>5.52E-01</td>
      <td>5.51E-01</td>
      <td>5.55E-01</td>
      <td>0.43</td>
    </tr>
    <tr>
      <td rowspan="5">Tricarboxylic acid cycle</td>
      <td>IDH</td>
      <td>CIT ↔ AKG+CO2</td>
      <td>3.36E+00</td>
      <td>3.24E+00</td>
      <td>3.92E+00</td>
      <td>4.66E+00</td>
      <td>4.66E+00</td>
      <td>4.66E+00</td>
      <td>1.39</td>
    </tr>
    <tr>
      <td>SDH</td>
      <td>SUC ↔ FUM</td>
      <td>4.30E+02</td>
      <td>4.30E+02</td>
      <td>1.46E+06</td>
      <td>1.04E+04</td>
      <td>1.04E+04</td>
      <td>1.04E+04</td>
      <td></td>
    </tr>
    <tr>
      <td>FH</td>
      <td>FUM ↔ MAL</td>
      <td>7.29E+06</td>
      <td>-Inf</td>
      <td>Inf</td>
      <td>4.56E+06</td>
      <td>4.56E+06</td>
      <td>4.56E+06</td>
      <td></td>
    </tr>
    <tr>
      <td>MDH</td>
      <td>MAL ↔ OAC</td>
      <td>5.49E+02</td>
      <td>5.47E+02</td>
      <td>5.49E+02</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>6.30E-03</td>
      <td>0</td>
    </tr>
    <tr>
      <td>GOT</td>
      <td>OAC ↔ ASP</td>
      <td>1.04E+02</td>
      <td>1.04E+02</td>
      <td>1.04E+02</td>
      <td>4.76E+05</td>
      <td>4.76E+05</td>
      <td>4.76E+05</td>
      <td>4576.92</td>
    </tr>
    <tr>
      <td rowspan="2">Amino acid metabolism</td>
      <td>SHT</td>
      <td>SER ↔ GLY+MEETHF</td>
      <td>1.39E+00</td>
      <td>1.37E+00</td>
      <td>1.41E+00</td>
      <td>1.86E+03</td>
      <td>1.86E+03</td>
      <td>1.86E+03</td>
      <td>1338.13</td>
    </tr>
    <tr>
      <td>CYST</td>
      <td>SER ↔ CYS</td>
      <td>1.25E-07</td>
      <td>0.00E+00</td>
      <td>4.22E-02</td>
      <td>1.33E-01</td>
      <td>1.33E-01</td>
      <td>1.33E-01</td>
      <td>1064000</td>
    </tr>
  </tbody>
</table>

_*SSR 393.5 [311.2–416.6] (95% CI, 362 DOF).†SSR 392.4 [308.4–413.4] (95% CI, 359 DOF)._

In normoxia, the magnitude of intracellular metabolite fluxes was similar in LFs and PASMCs (Figure 5—figure supplement 2, Table 1, Table 3). Compared to LFs, PASMCs had slower rates of glycolysis and faster rates of TCA metabolism driven, in part, by increased glutamine uptake (Figure 5—figure supplement 3). In hypoxia, PASMCs exhibited similar decreases in glycolytic flux as LFs but also a marked, and unexpected, increase in TCA flux (Figure 5—figure supplement 4). The increased TCA flux in PASMCs was driven by increased glutamine consumption. This finding is similar to a prior report of glutamine-driven oxidative phosphorylation in hypoxic cancer cells (Fan et al., 2013), where oxidative phosphorylation continued to provide the majority of cellular ATP even at 1% oxygen.

**Table 3.**
 PASMC fluxes in 21% and 0.5% oxygen.


<table>
  <thead>
    <tr>
      <th rowspan="2">Type</th>
      <th rowspan="2">Pathway</th>
      <th rowspan="2">ID</th>
      <th rowspan="2">Reaction</th>
      <th colspan="3">21%*</th>
      <th colspan="3">0.5%†</th>
      <th rowspan="2">Ratio</th>
    </tr>
    <tr>
      <th>Flux</th>
      <th>LB</th>
      <th>UB</th>
      <th>Flux</th>
      <th>LB</th>
      <th>UB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="33">NET</td>
      <td rowspan="10">Transport</td>
      <td>GLUT</td>
      <td>GLC.x → GLC</td>
      <td>4.28E+02</td>
      <td>4.28E+02</td>
      <td>4.28E+02</td>
      <td>3.65E+02</td>
      <td>3.65E+02</td>
      <td>3.65E+02</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>PYRR</td>
      <td>PYR.x → PYR.c</td>
      <td>1.04E+02</td>
      <td>1.02E+02</td>
      <td>1.09E+02</td>
      <td>4.53E+01</td>
      <td>4.31E+01</td>
      <td>4.57E+01</td>
      <td>0.44</td>
    </tr>
    <tr>
      <td>MCT</td>
      <td>LAC ↔ LAC.x</td>
      <td>8.01E+02</td>
      <td>8.01E+02</td>
      <td>8.04E+02</td>
      <td>6.49E+02</td>
      <td>6.49E+02</td>
      <td>6.49E+02</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>ALAR</td>
      <td>ALA → ALA.x</td>
      <td>1.43E+01</td>
      <td>1.43E+01</td>
      <td>1.46E+01</td>
      <td>7.83E+00</td>
      <td>7.83E+00</td>
      <td>8.24E+00</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td>GLNR</td>
      <td>GLN.x → GLN</td>
      <td>7.73E+01</td>
      <td>7.53E+01</td>
      <td>7.73E+01</td>
      <td>1.77E+02</td>
      <td>1.77E+02</td>
      <td>1.77E+02</td>
      <td>2.29</td>
    </tr>
    <tr>
      <td>GLUR</td>
      <td>GLU ↔ GLU.x</td>
      <td>2.53E+01</td>
      <td>2.52E+01</td>
      <td>2.54E+01</td>
      <td>1.19E+01</td>
      <td>1.19E+01</td>
      <td>1.22E+01</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>ASPR</td>
      <td>ASP → ASP.x</td>
      <td>7.01E+00</td>
      <td>6.99E+00</td>
      <td>7.02E+00</td>
      <td>6.92E+00</td>
      <td>6.84E+00</td>
      <td>7.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td>SERR</td>
      <td>SER.x → SER</td>
      <td>2.54E+00</td>
      <td>2.48E+00</td>
      <td>2.55E+00</td>
      <td>2.57E+00</td>
      <td>2.55E+00</td>
      <td>2.57E+00</td>
      <td>1.01</td>
    </tr>
    <tr>
      <td>CYSR</td>
      <td>CYX.x → CYS +CYS</td>
      <td>6.39E+00</td>
      <td>6.34E+00</td>
      <td>6.45E+00</td>
      <td>3.75E+00</td>
      <td>3.75E+00</td>
      <td>3.75E+00</td>
      <td>0.59</td>
    </tr>
    <tr>
      <td>GLYR</td>
      <td>GLY → GLY.x</td>
      <td>3.66E-01</td>
      <td>3.03E-01</td>
      <td>4.19E-01</td>
      <td>4.06E-01</td>
      <td>3.86E-01</td>
      <td>4.25E-01</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="11">Glycolysis</td>
      <td>HK</td>
      <td>GLC → G6P</td>
      <td>4.28E+02</td>
      <td>4.28E+02</td>
      <td>4.28E+02</td>
      <td>3.65E+02</td>
      <td>3.65E+02</td>
      <td>3.65E+02</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>PGI</td>
      <td>G6P ↔ F6P</td>
      <td>4.06E+02</td>
      <td>4.06E+02</td>
      <td>4.07E+02</td>
      <td>3.62E+02</td>
      <td>3.62E+02</td>
      <td>3.63E+02</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>PFK</td>
      <td>F6P → FBP</td>
      <td>4.17E+02</td>
      <td>4.17E+02</td>
      <td>4.18E+02</td>
      <td>3.61E+02</td>
      <td>3.60E+02</td>
      <td>3.61E+02</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>ALDO</td>
      <td>FBP ↔ DHAP +GAP</td>
      <td>4.17E+02</td>
      <td>4.17E+02</td>
      <td>4.18E+02</td>
      <td>3.61E+02</td>
      <td>3.60E+02</td>
      <td>3.61E+02</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>TPI</td>
      <td>DHAP ↔ GAP</td>
      <td>4.16E+02</td>
      <td>4.16E+02</td>
      <td>4.16E+02</td>
      <td>3.60E+02</td>
      <td>3.60E+02</td>
      <td>3.60E+02</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>GAP ↔ 3 PG</td>
      <td>8.39E+02</td>
      <td>8.39E+02</td>
      <td>8.41E+02</td>
      <td>7.21E+02</td>
      <td>7.21E+02</td>
      <td>7.21E+02</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>ENO</td>
      <td>3 PG → PEP</td>
      <td>8.36E+02</td>
      <td>8.35E+02</td>
      <td>8.53E+02</td>
      <td>7.20E+02</td>
      <td>7.20E+02</td>
      <td>7.20E+02</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>PK</td>
      <td>PEP → PYR.c</td>
      <td>9.31E+02</td>
      <td>9.30E+02</td>
      <td>9.31E+02</td>
      <td>9.24E+02</td>
      <td>9.24E+02</td>
      <td>9.24E+02</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>PYR.c ↔ LAC</td>
      <td>8.01E+02</td>
      <td>8.01E+02</td>
      <td>8.04E+02</td>
      <td>6.49E+02</td>
      <td>6.49E+02</td>
      <td>6.49E+02</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>GPT1</td>
      <td>PYR.c ↔ ALA</td>
      <td>1.64E+02</td>
      <td>1.62E+02</td>
      <td>1.92E+02</td>
      <td>–1.36E+01</td>
      <td>–1.39E+01</td>
      <td>–1.35E+01</td>
      <td>–0.08</td>
    </tr>
    <tr>
      <td>GPT2</td>
      <td>PYR.m ↔ ALA</td>
      <td>–1.43E+02</td>
      <td>–1.43E+02</td>
      <td>–1.42E+02</td>
      <td>2.62E+01</td>
      <td>2.51E+01</td>
      <td>2.65E+01</td>
      <td>–0.18</td>
    </tr>
    <tr>
      <td rowspan="4">Pentose phosphate pathway</td>
      <td>G6PD</td>
      <td>G6P → P5P+CO2</td>
      <td>1.89E+01</td>
      <td>1.57E+01</td>
      <td>1.93E+01</td>
      <td>1.16E-07</td>
      <td>0.00E+00</td>
      <td>1.10E-03</td>
      <td>0</td>
    </tr>
    <tr>
      <td>TK1</td>
      <td>P5P+P5 P ↔ S7P+GAP</td>
      <td>5.46E+00</td>
      <td>4.44E+00</td>
      <td>5.96E+00</td>
      <td>–6.15E-01</td>
      <td>–6.15E-01</td>
      <td>–5.77E-01</td>
      <td>–0.11</td>
    </tr>
    <tr>
      <td>TA</td>
      <td>S7P+GAP ↔ F6P+E4 P</td>
      <td>5.46E+00</td>
      <td>4.44E+00</td>
      <td>5.96E+00</td>
      <td>–6.15E-01</td>
      <td>–6.15E-01</td>
      <td>–5.77E-01</td>
      <td>–0.11</td>
    </tr>
    <tr>
      <td>TK2</td>
      <td>P5P+E4 P ↔ F6P+GAP</td>
      <td>5.46E+00</td>
      <td>4.44E+00</td>
      <td>5.96E+00</td>
      <td>–6.15E-01</td>
      <td>–6.15E-01</td>
      <td>–5.77E-01</td>
      <td>–0.11</td>
    </tr>
    <tr>
      <td rowspan="8">Anaplerosis</td>
      <td>PYRT</td>
      <td>PYR.c → PYR.m</td>
      <td>7.60E+01</td>
      <td>7.59E+01</td>
      <td>7.66E+01</td>
      <td>3.36E+02</td>
      <td>3.36E+02</td>
      <td>3.36E+02</td>
      <td>4.42</td>
    </tr>
    <tr>
      <td>PC</td>
      <td>PYR.m+CO2 → OAC</td>
      <td>6.30E+01</td>
      <td>6.29E+01</td>
      <td>6.59E+01</td>
      <td>2.37E+02</td>
      <td>2.36E+02</td>
      <td>2.37E+02</td>
      <td>3.76</td>
    </tr>
    <tr>
      <td>PEPCK</td>
      <td>OAC → PEP +CO2</td>
      <td>9.51E+01</td>
      <td>9.51E+01</td>
      <td>9.53E+01</td>
      <td>2.03E+02</td>
      <td>2.03E+02</td>
      <td>2.04E+02</td>
      <td>2.14</td>
    </tr>
    <tr>
      <td>ME2</td>
      <td>MAL → PYR.m +CO2</td>
      <td>1.20E-03</td>
      <td>0.00E+00</td>
      <td>5.20E-03</td>
      <td>1.82E+02</td>
      <td>1.81E+02</td>
      <td>1.82E+02</td>
      <td>151517.08</td>
    </tr>
    <tr>
      <td>ME1</td>
      <td>MAL → PYR.c +CO2</td>
      <td>3.29E-05</td>
      <td>0.00E+00</td>
      <td>1.15E+00</td>
      <td>5.91E-05</td>
      <td>0.00E+00</td>
      <td>8.06E-02</td>
      <td></td>
    </tr>
    <tr>
      <td>FAO</td>
      <td>FAO → AcCoA.m</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.32E-02</td>
      <td>1.15E-04</td>
      <td>0.00E+00</td>
      <td>1.56E-01</td>
      <td></td>
    </tr>
    <tr>
      <td>GLDH</td>
      <td>GLU ↔ AKG</td>
      <td>4.43E+01</td>
      <td>4.42E+01</td>
      <td>4.45E+01</td>
      <td>1.59E+02</td>
      <td>1.59E+02</td>
      <td>1.59E+02</td>
      <td>3.6</td>
    </tr>
    <tr>
      <td>GLS</td>
      <td>GLN ↔ GLU</td>
      <td>7.38E+01</td>
      <td>7.36E+01</td>
      <td>7.38E+01</td>
      <td>1.74E+02</td>
      <td>1.74E+02</td>
      <td>1.74E+02</td>
      <td>2.36</td>
    </tr>
    <tr>
      <td rowspan="19"></td>
      <td rowspan="8">Tricarboxylic acid cycle</td>
      <td>PDH</td>
      <td>PYR.m → AcCoA.m +CO2</td>
      <td>1.56E+02</td>
      <td>1.48E+02</td>
      <td>1.66E+02</td>
      <td>2.55E+02</td>
      <td>2.55E+02</td>
      <td>2.55E+02</td>
      <td>1.63</td>
    </tr>
    <tr>
      <td>CS</td>
      <td>AcCoA.m+OAC → CIT</td>
      <td>1.56E+02</td>
      <td>1.56E+02</td>
      <td>1.58E+02</td>
      <td>2.55E+02</td>
      <td>2.55E+02</td>
      <td>2.55E+02</td>
      <td>1.63</td>
    </tr>
    <tr>
      <td>IDH</td>
      <td>CIT ↔ AKG +CO2</td>
      <td>2.11E+01</td>
      <td>2.10E+01</td>
      <td>2.11E+01</td>
      <td>2.16E+01</td>
      <td>2.16E+01</td>
      <td>2.16E+01</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td>OGDH</td>
      <td>AKG → SUC +CO2</td>
      <td>6.54E+01</td>
      <td>6.51E+01</td>
      <td>6.59E+01</td>
      <td>1.81E+02</td>
      <td>1.80E+02</td>
      <td>1.81E+02</td>
      <td>2.77</td>
    </tr>
    <tr>
      <td>SDH</td>
      <td>SUC ↔ FUM</td>
      <td>6.54E+01</td>
      <td>6.51E+01</td>
      <td>6.59E+01</td>
      <td>1.81E+02</td>
      <td>1.80E+02</td>
      <td>1.81E+02</td>
      <td>2.77</td>
    </tr>
    <tr>
      <td>FH</td>
      <td>FUM ↔ MAL</td>
      <td>6.54E+01</td>
      <td>6.51E+01</td>
      <td>6.59E+01</td>
      <td>1.81E+02</td>
      <td>1.80E+02</td>
      <td>1.81E+02</td>
      <td>2.77</td>
    </tr>
    <tr>
      <td>MDH</td>
      <td>MAL ↔ OAC</td>
      <td>2.01E+02</td>
      <td>2.01E+02</td>
      <td>2.01E+02</td>
      <td>2.32E+02</td>
      <td>2.32E+02</td>
      <td>2.33E+02</td>
      <td>1.16</td>
    </tr>
    <tr>
      <td>GOT</td>
      <td>OAC ↔ ASP</td>
      <td>1.22E+01</td>
      <td>1.17E+01</td>
      <td>1.24E+01</td>
      <td>1.07E+01</td>
      <td>1.06E+01</td>
      <td>1.07E+01</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td rowspan="5">Amino acid metabolism</td>
      <td>PST</td>
      <td>3 PG → SER</td>
      <td>2.69E+00</td>
      <td>2.57E+00</td>
      <td>2.80E+00</td>
      <td>7.12E-01</td>
      <td>7.01E-01</td>
      <td>7.21E-01</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>SHT</td>
      <td>SER ↔ GLY +MEETHF</td>
      <td>5.19E+00</td>
      <td>5.15E+00</td>
      <td>5.20E+00</td>
      <td>3.82E+00</td>
      <td>3.81E+00</td>
      <td>3.86E+00</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>CYST</td>
      <td>SER ↔ CYS</td>
      <td>–1.12E+01</td>
      <td>–1.17E+01</td>
      <td>–1.11E+01</td>
      <td>–6.35E+00</td>
      <td>–6.35E+00</td>
      <td>–6.35E+00</td>
      <td>0.57</td>
    </tr>
    <tr>
      <td>SD</td>
      <td>SER → PYR.c</td>
      <td>6.39E+00</td>
      <td>6.23E+00</td>
      <td>6.44E+00</td>
      <td>2.33E+00</td>
      <td>2.33E+00</td>
      <td>2.33E+00</td>
      <td>0.36</td>
    </tr>
    <tr>
      <td>GLYS</td>
      <td>CO2 +MEETHF → GLY</td>
      <td>2.39E+00</td>
      <td>2.36E+00</td>
      <td>2.42E+00</td>
      <td>1.80E+00</td>
      <td>1.79E+00</td>
      <td>1.81E+00</td>
      <td>0.75</td>
    </tr>
    <tr>
      <td rowspan="3">Biomass</td>
      <td>BIOMASS</td>
      <td>978*AcCoA.c+237.8*ALA +187*ASP +92.3*CO2 +57.46*CYS +45.97*DHAP +114.5*G6P+127.6*GLN +153*GLU +260.8*GLY +101.1*MEETHF +92.3*P5P+174.8*SER → biomass</td>
      <td>2.77E-02</td>
      <td>2.70E-02</td>
      <td>2.79E-02</td>
      <td>2.00E-02</td>
      <td>2.00E-02</td>
      <td>2.00E-02</td>
      <td>0.72</td>
    </tr>
    <tr>
      <td>ACL</td>
      <td>CIT → AcCoA.c +MAL</td>
      <td>1.35E+02</td>
      <td>1.34E+02</td>
      <td>1.38E+02</td>
      <td>2.33E+02</td>
      <td>2.33E+02</td>
      <td>2.33E+02</td>
      <td>1.72</td>
    </tr>
    <tr>
      <td>LIPS</td>
      <td>AcCoA.c → lipid</td>
      <td>1.08E+02</td>
      <td>9.99E+01</td>
      <td>1.08E+02</td>
      <td>2.14E+02</td>
      <td>2.14E+02</td>
      <td>2.14E+02</td>
      <td>1.98</td>
    </tr>
    <tr>
      <td rowspan="3">Mixing</td>
      <td>cPYR</td>
      <td>0*PYR.c → PYR.ms</td>
      <td>5.77E-01</td>
      <td>5.64E-01</td>
      <td>5.92E-01</td>
      <td>1.00E+00</td>
      <td>9.96E-01</td>
      <td>1.00E+00</td>
      <td>1.73</td>
    </tr>
    <tr>
      <td>mPYR</td>
      <td>0*PYR.m → PYR.ms</td>
      <td>4.23E-01</td>
      <td>4.08E-01</td>
      <td>4.36E-01</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>4.40E-03</td>
      <td>0</td>
    </tr>
    <tr>
      <td>sPYR</td>
      <td>PYR.ms → PYR.fix</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td>1.00E+00</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="21">EXCH</td>
      <td rowspan="2">Transport</td>
      <td>MCT</td>
      <td>LAC ↔ LAC.x</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>1.36E+02</td>
      <td>1.64E+03</td>
      <td>1.63E+03</td>
      <td>1.65E+03</td>
      <td>16400000000</td>
    </tr>
    <tr>
      <td>GLUR</td>
      <td>GLU ↔ GLU.x</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.27E-02</td>
      <td>5.69E-05</td>
      <td>0.00E+00</td>
      <td>1.71E-02</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="7">Glycolysis</td>
      <td>PGI</td>
      <td>G6P ↔ F6P</td>
      <td>4.88E+06</td>
      <td>4.88E+06</td>
      <td>Inf</td>
      <td>9.92E+06</td>
      <td>9.85E+04</td>
      <td>Inf</td>
      <td></td>
    </tr>
    <tr>
      <td>ALDO</td>
      <td>FBP ↔ DHAP +GAP</td>
      <td>2.89E+02</td>
      <td>2.80E+02</td>
      <td>2.89E+02</td>
      <td>2.57E+02</td>
      <td>2.56E+02</td>
      <td>2.57E+02</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>TPI</td>
      <td>DHAP ↔ GAP</td>
      <td>9.86E+06</td>
      <td>-Inf</td>
      <td>Inf</td>
      <td>1.65E+03</td>
      <td>1.63E+03</td>
      <td>1.68E+03</td>
      <td></td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>GAP ↔ 3 PG</td>
      <td>1.12E+03</td>
      <td>0.00E+00</td>
      <td>5.88E+05</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>2.27E-01</td>
      <td></td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>PYR.c ↔ LAC</td>
      <td>1.47E+03</td>
      <td>1.39E+03</td>
      <td>1.47E+03</td>
      <td>4.49E+02</td>
      <td>4.49E+02</td>
      <td>4.49E+02</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>GPT1</td>
      <td>PYR.c ↔ ALA</td>
      <td>2.74E+02</td>
      <td>2.73E+02</td>
      <td>2.77E+02</td>
      <td>1.00E-07</td>
      <td>0.00E+00</td>
      <td>4.28E-02</td>
      <td>0</td>
    </tr>
    <tr>
      <td>GPT2</td>
      <td>PYR.m ↔ ALA</td>
      <td>1.38E+02</td>
      <td>1.38E+02</td>
      <td>1.49E+02</td>
      <td>9.64E+01</td>
      <td>0.00E+00</td>
      <td>1.01E+02</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td rowspan="3">Pentose phosphate pathway</td>
      <td>TK1</td>
      <td>P5P+P5 P ↔ S7P+GAP</td>
      <td>7.99E+02</td>
      <td>7.97E+02</td>
      <td>8.08E+02</td>
      <td>3.54E+01</td>
      <td>3.54E+01</td>
      <td>3.55E+01</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>TA</td>
      <td>S7P+GAP ↔ F6P+E4 P</td>
      <td>1.53E-01</td>
      <td>0.00E+00</td>
      <td>5.82E-01</td>
      <td>2.55E+00</td>
      <td>2.54E+00</td>
      <td>2.57E+00</td>
      <td>16.67</td>
    </tr>
    <tr>
      <td>TK2</td>
      <td>P5P+E4 P ↔ F6P+GAP</td>
      <td>3.33E+00</td>
      <td>2.62E+00</td>
      <td>3.35E+00</td>
      <td>1.29E+01</td>
      <td>1.29E+01</td>
      <td>1.29E+01</td>
      <td>3.88</td>
    </tr>
    <tr>
      <td rowspan="2">Anaplerosis</td>
      <td>GLDH</td>
      <td>GLU ↔ AKG</td>
      <td>5.36E+02</td>
      <td>5.34E+02</td>
      <td>8.37E+02</td>
      <td>1.23E+03</td>
      <td>1.23E+03</td>
      <td>1.23E+03</td>
      <td>2.29</td>
    </tr>
    <tr>
      <td>GLS</td>
      <td>GLN ↔ GLU</td>
      <td>3.20E-01</td>
      <td>0.00E+00</td>
      <td>2.74E+00</td>
      <td>1.12E+00</td>
      <td>1.07E+00</td>
      <td>1.74E+00</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="5">Tricarboxylic acid cycle</td>
      <td>IDH</td>
      <td>CIT ↔ AKG +CO2</td>
      <td>1.04E+01</td>
      <td>1.02E+01</td>
      <td>1.04E+01</td>
      <td>6.30E+01</td>
      <td>6.30E+01</td>
      <td>6.31E+01</td>
      <td>6.09</td>
    </tr>
    <tr>
      <td>SDH</td>
      <td>SUC ↔ FUM</td>
      <td>2.78E-01</td>
      <td>0.00E+00</td>
      <td>Inf</td>
      <td>3.34E+06</td>
      <td>3.34E+06</td>
      <td>3.34E+06</td>
      <td></td>
    </tr>
    <tr>
      <td>FH</td>
      <td>FUM ↔ MAL</td>
      <td>1.03E-04</td>
      <td>0.00E+00</td>
      <td>1.58E+01</td>
      <td>2.18E+02</td>
      <td>2.18E+02</td>
      <td>2.18E+02</td>
      <td>2114238.83</td>
    </tr>
    <tr>
      <td>MDH</td>
      <td>MAL ↔ OAC</td>
      <td>1.01E+03</td>
      <td>8.27E+02</td>
      <td>1.01E+03</td>
      <td>3.67E+03</td>
      <td>3.67E+03</td>
      <td>3.69E+03</td>
      <td>3.63</td>
    </tr>
    <tr>
      <td>GOT</td>
      <td>OAC ↔ ASP</td>
      <td>2.27E+02</td>
      <td>2.27E+02</td>
      <td>2.47E+02</td>
      <td>1.54E+01</td>
      <td>1.54E+01</td>
      <td>1.55E+01</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td rowspan="2">Amino acid metabolism</td>
      <td>SHT</td>
      <td>SER ↔ GLY +MEETHF</td>
      <td>3.55E+00</td>
      <td>3.52E+00</td>
      <td>3.59E+00</td>
      <td>1.60E-01</td>
      <td>1.36E-01</td>
      <td>1.70E-01</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>CYST</td>
      <td>SER ↔ CYS</td>
      <td>1.04E+03</td>
      <td>1.03E+03</td>
      <td>1.04E+03</td>
      <td>2.00E-03</td>
      <td>0.00E+00</td>
      <td>2.00E-03</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

_*SSR 575.6 [499.1–630.6] (95% CI, 563 DOF).†SSR 521.3 [482.2–611.6] (95% CI, 545 DOF)._

Given the global decrease in bioenergetic metabolic flux in hypoxic LFs, we hypothesized that these differences may be a consequence of decreased growth rate. After normalizing metabolite fluxes in normoxia and hypoxia to the cell growth rate, a modest increase (~10%) in glycolytic flux was observed (Figure 5—figure supplement 5). This finding suggests that, while glycolysis increases relative to growth rate in hypoxic cells, regulators of cell proliferation rate override the anti-proliferative effects of the HIF-1α transcriptional program. Indeed, even after adjusting for cell growth rate, the relative increase in glycolytic flux is modest compared to the marked up-regulation of glycolytic proteins and the glycolytic potential of these cells demonstrated by BAY treatment in normoxia. BAY treatment decreased cell proliferation rate (Figure 2B–C), indicating that, unlike hypoxia, PHD inhibition in normoxia uncouples cell proliferation and metabolic flux.

### Hypoxia and BAY treatment increase lactate oxidation

One important feature of metabolic flux analysis is its ability to determine the individual forward and backward fluxes of bidirectional reactions, or the so-called exchange fluxes. Although the metabolite exchange fluxes for bidirectional reactions tend to be poorly resolved by this method (Wiechert, 2007), two observations from our models are noteworthy (Table 1, Table 2, Table 3). First, consistent with the stable isotope tracing results, the modeled rate of reductive carboxylation through reverse flux by isocitrate dehydrogenase in LFs is low (~4 fmol/cell/h), unchanged by hypoxia, and modestly increased by BAY treatment. By contrast, the rate of reductive carboxylation increases sixfold in PASMCs in hypoxia, highlighting a potentially important role for this pathway in the metabolic response of PASMCs to decreased oxygen availability (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig6-v1.jpg)

**Figure 6.:** (A) Reductive carboxylation describes the converstion of α-ketoglutarate (AKG) to isocitrate by reverse flux through isocitrate dehydrogenase (IDH) (blue arrow). This yields M+5 citrate. (B) Exchange flux estimates for reductive carboxylation. Data show the model estimate with upper and lower bounds for LFs and PASMCs.

Second, PHD inhibition increases lactate transport exchange flux in LFs from ~0 to 1500 and 700 fmol/cell/h with 0.5% oxygen and BAY treatment, respectively, with similar results in PASMCs (Figure 7A). This observation suggests increased lactate uptake with hypoxia or BAY treatment. To investigate this hypothesis, LFs and PASMCs were treated with [U-13C3]-lactate (2 mM) and 13C incorporation into intracellular metabolites was analyzed by LC-MS (Figure 7B, Figure 4—figure supplement 1, Figure 4—figure supplement 2). Lactate labeled ~50% of citrate and ~20% of downstream TCA cycle metabolites (α-ketoglutarate, malate, aspartate) in both LFs and PASMCs, indicating that lactate may be an important respiratory fuel source in these cells even though lactate efflux is high. Although increased labeling of pyruvate was observed in hypoxic PASMCs, this increase did not flow through to TCA metabolites as observed in LFs (Figure 4—figure supplement 2). Lactate has been used less commonly than glucose and glutamine in stable isotope tracing studies. Faubert et al., 2017 demonstrated lactate incorporation in human lung adenocarcinoma in vivo. In this study, lactate incorporation corresponded to regions of high glucose uptake as determined by [¹⁸F]-fluorodeoxyglucose positron emission tomography, suggesting that lactate consumption can occur even in areas of high glucose utilization. Subsequently, investigators have demonstrated the importance of lactate as a metabolic fuel in vivo (Hui et al., 2020; Hui et al., 2017).

![Figure 7.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig7-v1.jpg)

**Figure 7.:** (A) Exchange flux estimates for lactate import presented as in (A). (C) Mass isotopomer distributions of lactate (LAC), fructose-bisphosphate (FBP), pyruvate (PYR), citrate (CIT), α-ketoglutarate (AKG), and malate (MAL) in LFs following 72 hr labeling with [U-13C3] lactate. Data are mean ± SEM (n=4, p<0.05 for the following comparisons: * 0.5% v. 21% oxygen, † BAY v. DMSO, ‡ Δoxygen v. ΔBAY).

In addition to downstream metabolites, we also observed hypoxia- and BAY-dependent increases in lactate incorporation in fructose bisphosphate (FBP) and 3-phosphoglycerate (3PG). This observation is consistent with prior reports describing hypoxia-mediated increases in gluconeogenesis and glycogen synthesis (Favaro et al., 2012; Owczarek et al., 2020; Pelletier et al., 2012). These data suggest that lactate also makes a small (~5% carbon) contribution to glycogen precursors. Together, these findings from stable isotope tracing of lactate reveal its important contribution to primary cell metabolism under standard culture conditions, and also reveal increased lactate uptake in hypoxia.

### Hypoxia prevents BAY from increasing glycolysis

To reconcile the differential effects of PHD inhibition by hypoxia and BAY, we next addressed whether hypoxia could suppress BAY-stimulated glucose and lactate fluxes (Figure 8). LFs cultured in standard growth medium were treated with BAY and placed in either 21% or 0.5% oxygen. Similar to previous experiments, BAY decreased cell growth rate, increased glucose uptake, and increased lactate efflux in 21% oxygen. However, when combined with 0.5% oxygen, BAY did not enhance lactate efflux. These data demonstrate that hypoxia antagonizes the effects of HIF-1α activation on glycolytic flux.

![Figure 8.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig8-v1.jpg)

**Figure 8.:** (A) LFs were cultured in standard growth medium and treated with molidustat (BAY, 10 μM) or vehicle (DMSO, 0.1%) in 21% or 0.5% oxygen conditions for 72 hr. Growth rates were determined by linear fitting of log-transformed growth curves. (B) Glucose uptake in LFs treated with BAY cultured in hypoxia (note reversed y-axis). (C) Lactate efflux in LFs treated with BAY cultured in hypoxia. Data are mean ± SEM (n=4, * p<0.05 BAY v. DMSO within a given oxygen exposure).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** LFs were treated with siRNA to knock down PHD2 expression. (A) Cell growth was not impacted by siPHD2 treatment. (B) Representative immunoblot of LF cell lysates at 72 hr demonstrating substantial PHD2 knockdown associated with stabilization of HIF-1α. (C) Relative change in LDHA protein levels from (B) normalized to 21% siCTL (n=4). (D) GLUT1 and (E) LDHA mRNA determined by RT-qPCR (n=5). (F) Lactate efflux in siPHD2-treated cells (n=5). Data are mean ± SEM (p<0.05 with black * indicating a significant effect of treatment within a given oxygen tension and colored * indicating a significant effect of oxygen within a given treatment denoted by the color).

We observed a similar effect of hypoxia on glycolysis when using RNA interference to silence PHD2 expression and activate HIF-1α gene transcription (Figure 8—figure supplement 1). As with BAY treatment, siPHD2 stabilized HIF-1α in normoxia and increased glycolytic gene expression (Figure 8—figure supplement 1B–E); however, hypoxia inhibited siPHD2-dependent increases in glycolysis (Figure 8—figure supplement 1F). These data indicate that the metabolic consequences of BAY treatment are a direct consequence of PHD inhibition and not simply an off-target effect.

To investigate these metabolic differences further, we performed metabolomic profiling of LFs treated for 72 hr with hypoxia or BAY separately or in combination. Both 0.5% oxygen and BAY treatment caused marked changes in intracellular metabolites (Figure 9—figure supplement 1). Of 133 total metabolites, 98 were differentially regulated by hypoxia and 54 were differentially regulated by BAY. Of these, 44 were modulated by both treatments (Figure 9—figure supplement 1C). Metabolite set enrichment analysis of KEGG biochemical pathways identified increased enrichment of fatty acid biosynthesis pathways with hypoxia (Figure 9—figure supplement 1D). By contrast, BAY treatment was enriched for metabolites involved in pentose/glucuronate interconversions and glycolysis (Figure 9—figure supplement 1E). Aspartate was the most significantly decreased metabolite with both treatments, consistent with prior reports demonstrating an important role for HIF-1 regulation of aspartate biosynthesis in cancer cells (Garcia-Bermudez et al., 2018; Meléndez-Rodríguez et al., 2019).

Principal component analysis revealed greater similarity among both treatment groups cultured in 0.5% oxygen than among the BAY-treatment groups (Figure 9A). Moreover, these hypoxia-treated cells were well-segregated from cells treated with BAY alone. These observations are consistent with our metabolic flux models demonstrating an overriding effect of hypoxia per se on cell metabolism and highlighting important differences between hypoxic and pharmacologic PHD inhibition. To identify the metabolic changes that depend on hypoxia rather than PHD inhibition, we identified differentially regulated metabolites in BAY-treated cells cultured in normoxia and hypoxia (Figure 9B). Of 133 metabolites, 83 were significantly differentially regulated by hypoxia in BAY-treated cells. An enrichment analysis of these metabolites demonstrated up-regulation of arginine and proline metabolism and down-regulation of the TCA cycle as the most impacted by hypoxia in BAY treated cells (Figure 9C). Leading edge analysis highlights negative enrichment scores associated with all of the TCA metabolites detected by our platform (Figure 9D). This result indicates better preservation of TCA cycle flux in normoxic BAY-treated cells than in hypoxic cells, as suggested by our metabolic flux models where hypoxia caused a 1.5- to 2-fold reduction of TCA flux compared to a 1.1–1.5-fold reduction with BAY treatment (Figure 5).

![Figure 9.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig9-v1.jpg)

**Figure 9.:** (A) Principal component analysis of intracellular metabolites following 72 hr of treatment suggests a dominant effect of hypoxia over pharmacologic PHD inhibition on the metabolome (n=7). (B) Volcano plot of intracellular metabolites of BAY-treated cells cultured in 21% or 0.5% oxygen. Filled circles indicate significantly increased (blue) and decreased (red) levels in hypoxia. (C) Metabolite set enrichment analysis of metabolites from (B). All KEGG pathways with p-values <0.05 are shown. (D) Leading edge analysis of the TCA cycle metabolite set. Negative values indicate the relative enrichment associated with BAY treatment alone compared to BAY plus hypoxia treatment. Abbreviations: PYR, pyruvate; SUC, succinate; PEP, phosphoenolpyruvate; CIT, citrate; AKG, α-ketoglutarate; MAL, malate; ACO, aconitate; FUM, fumarate.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig9-figsupp1-v1.jpg)

**Figure 9—figure supplement 1.:** (A) Volcano plot of differentially regulated metabolites following 0.5% oxygen culture. (B) Volcano plot of differentially regulated metabolites by BAY treatment in 21% oxygen. (C) Venn diagram illustrating the overlap among metabolites differentially regulated by hypoxia (blue) or BAY treatment (purple). (D) Metabolite enrichment in KEGG pathways following hypoxia. (E) Metabolite enrichment in KEGG pathways following BAY. Only significantly enriched metabolite sets with p<0.05 are shown. NES, normalized enrichment score.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig9-figsupp2-v1.jpg)

**Figure 9—figure supplement 2.:** (A) NAD+, (B) NADH, and (C) NADH/NAD+ from LFs cultured for 72 hr in 0.5% oxygen ±BAY (n=5).(D) NADP+, (E) NADPH, and (F) NADPH/NADP+ from LFs cultured for 72 hr in 0.5% oxygen ±BAY (n=4). Data are mean ± SEM (p<0.05 with black * indicating a significant effect of oxygen within a given treatment and colored * indicating a significant effect of treatment within a given oxygen tension as denoted by the color).

In addition to these differential effects on polar metabolite levels, we reasoned that another critical difference between hypoxia and BAY treatment is the impact of hypoxia on cellular redox state. We measured the impact of these treatments on intracellular NAD(H) and NADP(H) redox couples (Figure 9—figure supplement 2). Hypoxia increased the NADH/NAD+ ratio, driven primarily by a decrease in intracellular NAD+. Interestingly, while BAY treatment increased the levels of NADH, a concomitant increase in NAD+ resulted in preservation of the NADH/NAD+ ratio. As NADH accumulation is a putative inhibitor of glycolytic flux (Tilton et al., 1991), this may be one mechanism by which glycolytic flux is decreased in hypoxia but not following BAY treatment. Conversely, hypoxia decreased the NADPH/NADP+ ratio in both control and BAY-treated cells, primarily through decreasing NADPH. This finding is consistent with prior studies of bovine coronary artery smooth muscle cells (Gupte and Wolin, 2006). In hypoxia, NADPH is generated primarily by the pentose phosphate pathway (Liu et al., 2016), where it plays an important role in the detoxification of reactive oxygen species (Fessel and Oldham, 2018; Xiao et al., 2018). Although we modeled increased flux through the pentose phosphate pathway in hypoxia (Figure 5A), the overall flux was low and apparently inadequate to maintain the NADPH/NADP+ ratio.

### Transcriptomic analysis identifies metabolic regulators in hypoxia

To identify the upstream regulators of the observed metabolic changes, we next performed RNA-seq transcriptomic analysis of LFs treated with hypoxia or BAY, separately or together. As anticipated, both hypoxia and BAY treatment induced substantial changes in gene expression (Figure 10—figure supplement 1). Of the 10,686 differentially expressed genes across both conditions, 869 (4%) were unique to BAY treatment in normoxia, 4002 (19%) were shared by BAY and hypoxia, while 5052 (25%) were unique to 0.5% hypoxia (Figure 10—figure supplement 1C). Gene set enrichment analysis of these differentially regulated metabolites was performed using Molecular Signatures Database ‘Hallmark’ gene sets (Liberzon et al., 2015; Figure 10—figure supplement 1D–F). As expected, both treatments were associated with enrichment of the ‘hypoxia’ and ‘glycolysis’ gene sets.

Given the disparate effects of hypoxic and pharmacologic PHD inhibition on cellular metabolism described above, we focused our transcriptomic analyses on the differences between hypoxia and BAY treatments. Principal component analysis again demonstrated clear separation among the four treatment groups (Figure 10A). The first and second principal components correspond to 0.5% oxygen and BAY treatments, respectively. Consistent with our prior observations, the combination of 0.5% oxygen plus BAY was more similar to 0.5% oxygen alone than BAY treatment alone, supporting the hypothesis that hypoxia overrides the effects of BAY treatment. To identify the transcripts driving these differences, we identified genes differentially expressed following hypoxia in BAY-treated cells (Figure 10B). An enrichment analysis of these differentially expressed genes identified pro-proliferative gene sets like ‘E2F targets’, ‘G2/M checkpoint’, and ‘MYC targets’ associated with hypoxia (Figure 10C–E). These findings were further supported by a transcription factor enrichment analysis identifying enrichment of MYC transcription factor targets associated with hypoxia, but not BAY treatment (Figure 10F, Figure 10—figure supplement 1G–H).

![Figure 10.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig10-v1.jpg)

**Figure 10.:** (A) Principal component analysis of transcriptional changes in lung fibroblasts following 72 hr of treatment with 0.5% oxygen or molidustat (BAY), separately or together (n=4). (B) Volcano plot illustrating the effects of hypoxia in BAY-treated cells on gene expression. (C) Gene set enrichment analysis of transcripts from (B). (D) Volcano plot of those transcripts comprising the E2F Targets and G2/M Checkpoint Hallmark gene sets. (E) Volcano plot of those transcripts comprising the MYC Targets V1 and V2 Hallmark gene sets. (F) Volcano plot illustrating the results of a transcription factor enrichment analysis suggests mechanisms for differential regulation of gene expression following hypoxia or BAY treatment.

![Figure 10—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig10-figsupp1-v1.jpg)

**Figure 10—figure supplement 1.:** (A) Volcano plot of differentially expressed genes following 0.5% oxygen culture. (B) Volcano plot of differentially expressed genes following BAY treatment. (C) Venn diagram illustrating the number of differentially expressed transcripts following hypoxia (blue) or BAY treatment (purple). (D) Venn diagram illustrating the number of differentially enriched Hallmark gene sets with hypoxia (blue) or BAY treatment (purple). (E) Gene set enrichment results of hypoxia-treated cells. (F) Gene set enrichment results of BAY-treated cells. All gene sets listed were significantly enriched at FDR <0.05. NES, normalized enrichment score. (G) Volcano plot illustrating the results of a transcription factor enrichment analysis in hypoxia-treated cells. (H) Volcano plot illustrating the results of a transcription factor enrichment analysis in BAY-treated cells. (I) Venn diagram illustrating the overlap among enriched transcription factors following hypoxia or BAY treatment.

![Figure 10—figure supplement 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig10-figsupp2-v1.jpg)

**Figure 10—figure supplement 2.:** (A) Normalized mRNA counts from RNA-seq analysis of LFs treated with hypoxia ±BAY (n=4). (B) Relative CDKN1A expression by RT-qPCR in siPHD2-treated in normoxia and hypoxia (n=4). Data are mean ± SEM (p<0.05 with black * indicating a significant effect of treatment within a given oxygen tension and colored * indicating a significant effect of oxygen for a given treatment as denoted by the color).

As one example of MYC-dependent transcriptional regulation, MYC represses the transcription of CDKN1A, which encodes the cyclin-dependent kinase and cell-cycle inhibitor p21 (García-Gutiérrez et al., 2019). CDKN1A expression increases with BAY treatment in normoxia, but is decreased by hypoxia, consistent with hypoxia-induced MYC activation (Figure 10—figure supplement 2A). While we did not observe increased CDKN1A expression by RT-qPCR in siPHD2-treated cells in normoxia, we did observe hypoxia-mediated down-regulation in both siCTL- and siPHD2-treated cells (Figure 10—figure supplement 2B), consistent with MYC transcriptional activity.

Classically, hypoxia and HIF activation are thought to inhibit cell proliferation by inhibiting pro-proliferative MYC signaling (Koshiji et al., 2004). These results indicate that hypoxia-induced MYC activation may be sustaining proliferation in LFs. We reasoned that these pro-proliferative signals may also account for the unexpected effects of hypoxia on glycolysis that we observed.

### MYC antagonizes HIF-dependent glycolytic fluxes

To examine the role of hypoxia-induced MYC activation in the metabolic response to hypoxia in proliferating primary cells, we first measured MYC by immunoblot. Consistent with our bioinformatic results, we observed increased MYC in hypoxia-treated cells, but not with BAY-treatment alone, where MYC was decreased (Figure 11A–B). These findings were similar in siPHD2-treated cells (Figure 11—figure supplement 1). Together, these data suggest a model whereby hypoxia activates MYC and inhibits HIF-driven increases in glycolysis (Figure 11C, top). Inhibiting MYC in hypoxia, therefore, should increase glycolysis. Conversely, HIF-dependent glycolysis after BAY treatment in normoxia should be sensitive to inhibition by MYC over-expression (Figure 11C, bottom).

![Figure 11.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig11-v1.jpg)

**Figure 11.:** (A) Representative immunoblot of MYC protein expression in lung fibroblasts (LFs) following 72 hr of treatment with 0.5% oxygen or molidustat BAY, (B). (B) Quantification of band densities from (A). (C) Working hypotheses: (1) Hypoxia-induced MYC antagonizes HIF-dependent metabolic and transcriptional events (upper panel). Silencing MYC with siRNA (siMYC) should therefore increase lactate efflux in hypoxia. (2) HIF activation in normoxia decreases MYC activity and increases glycolysis (lower panel). Therefore, overexpressing MYC (AdMYC) should restore MYC signaling and inhibit lactate efflux. (D) Representative immunoblot of LFs treated with siRNA targeting MYC (M) demonstrating adequate protein knockdown. (E) Growth rates of MYC-knockdown cells cultured in hypoxia. (F) Lactate efflux rates of MYC-knockdown cells cultured in hypoxia. (G) Representative immunoblot of LFs treated with MYC adenovirus. (H) Growth rates of MYC overexpressing cells cultured with BAY. (I) Lactate efflux rates of MYC overexpressing cells cultured with BAY. Data are mean ± SEM (n=3–7, p<0.05 as indicated by black * for differences within groups and colored * for differences between groups defined by the x-axis).

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig11-figsupp1-v1.jpg)

**Figure 11—figure supplement 1.:** (A) Representative immunoblot of MYC protein levels in LFs treated with siPHD2 (P) or siCTL (C) and exposed to 0.5% oxygen for 72 hr. (B) Quantification of MYC band densities as in (A). Data are mean ± SEM n=3, p<0.05 as indicated by black * for differences within groups and colored * for differences between groups defined by the x-axis.

![Figure 11—figure supplement 2.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig11-figsupp2-v1.jpg)

**Figure 11—figure supplement 2.:** (A) Representative immunoblot of HIF-1α and LDHA protein levels in LFs treated with siMYC (M) or siCTL (C) and exposed to 0.5% oxygen for 72 hr. (B) Quantification of HIF-1α band densities as in (A). (C) Quanitification of LDHA band densities as in (A). (D) GLUT1 mRNA levels were analyzed by RT-qPCR expressed as fold change relative to 21% siCTL cells. (E) LDHA mRNA levels by RT-qPCR. (F) Representative immunoblot of HIF-1α and LDHA protein levels in LFs treated with MYC (M) or YFP (Y) adenovirus in combination with BAY. (G) Quantification of HIF-1α band densities as in (F). (H) Quanitification of LDHA band densities as in (F). (I) GLUT1 mRNA levels were analyzed by RT-qPCR expressed as fold change relative to 21% siCTL cells. (J) LDHA mRNA levels by RT-qPCR. Data are mean ± SEM n=3–5, p<0.05 as indicated by black * for differences within groups and colored * for differences between groups defined by the x-axis.

To test the hypothesis that hypoxia-induced MYC expression inhibits glycolysis in primary cells, we first combined MYC knockdown with hypoxia treatment (Figure 11C, top). As expected, MYC-deficient cells proliferated more slowly in normoxia, and MYC was essential for sustaining cell proliferation in hypoxia (Figure 11E). We did not observe any significant differences in HIF-1α stabilization or target gene expression with MYC knockdown in normoxia or hypoxia (Figure 11—figure supplement 2A–E). Consistent with our hypothesis, MYC-knockdown increased lactate efflux in hypoxia, unlike control siRNA-treated cells (Figure 11F).

We next performed the complementary experiment to determine whether MYC over-expression could attenuate the increase in glycolysis observed with BAY treatment in normoxia (Figure 11C, bottom). We did not observe any significant differences in cell growth rate with MYC over-expression (Figure 11H). Interestingly, MYC over-expression potentiated BAY-stimulated increases in HIF-1α stabilization and target gene expression (Figure 11—figure supplement 2F–J). In spite of these transcriptional changes, MYC over-expression attenuated BAY-stimulated lactate efflux in normoxia. Together, these data indicate that hypoxia-induced MYC expression may be one factor that uncouples the HIF transcriptional program from glycolytic flux in proliferating primary cells.

## Discussion

In this work, we used 13C metabolic flux analysis to identify hypoxia-mediated metabolic changes in proliferating human primary cells. Our principal finding was that hypoxia reduced, rather than increased, carbon flux through glycolysis and lactate fermentation pathways despite robust activation of the HIF-1α transcriptional program and up-regulation of glycolytic genes. The LFs studied here are certainly capable of augmenting glycolysis in response to HIF-1α stabilization, as demonstrated by experiments with the PHD inhibitor BAY; however, these effects are completely attenuated when BAY-treated cells are cultured in hypoxia. Together, these findings suggest that changes in enzyme expression alone are insufficient to alter metabolic flux in hypoxia and point to the importance of regulatory mechanisms that supersede the effects of HIF-dependent gene transcription in primary cells.

Our data indicate that hypoxia-induced MYC expression is one such regulatory mechanism. MYC is a transcription factor that regulates the expression of numerous genes involved in many biological processes, including metabolism, proliferation, apoptosis, and differentiation (Dang et al., 2006; Li et al., 2020; Stine et al., 2015). As deregulated MYC activity has been associated with the majority of human cancers (Vita and Henriksson, 2006), much of our understanding of MYC regulation comes from studies using cancer cell models (Dang, 2012; Li et al., 2020; Madden et al., 2021; Stine et al., 2015). The role of MYC in the biology of untransformed cells is less well understood. The literature describes a complex and reciprocal relationship between HIF and MYC that depends on both environmental (e.g. hypoxia) and cellular context (Li et al., 2020). Generally, HIF-1 has been observed to inhibit MYC through multiple mechanisms (Gordan et al., 2007; Koshiji et al., 2005; Koshiji et al., 2004; Zhang et al., 2007), and this previous work is consistent with our present observations that HIF stabilization following BAY treatment in normoxia decreased MYC protein and target gene expression. Conversely, MYC has been implicated in increased HIF activity through transcriptional and post-transcriptional mechanisms (Chen et al., 2013; Doe et al., 2012; Zhang et al., 2009), primarily in the context of malignant transformation. The observation that MYC may antagonize the transcriptional effects of HIF to sustain primary cell proliferation and metabolism in hypoxia suggests a substantially different regulatory relationship than has been previously described.

Understanding how MYC transcriptional activity affects hypoxic primary cell metabolism is imperative to our understanding of cellular adaptation to hypoxia. MYC stimulates the expression of nuclear-encoded mitochondrial genes and promotes mitochondrial biogenesis, both directly and through activation of mitochondrial transcriptional factor A (TFAM) (Li et al., 2005). Indeed, we found that the oxidative phosphorylation gene set was enriched in BAY-treated cells cultured in hypoxia (Figure 10C). In this way, hypoxic MYC activation may sustain energy production by oxidative phosphorylation, thereby decreasing the energetic demands that would otherwise drive increased glycolytic flux. Beyond oxidative phosphorylation, MYC regulates genes involved in many other intermediary metabolic pathways, including amino acids, nucleotides, and lipids (Stine et al., 2015), that may also impact the central pathways of carbon metabolism studied in this work.

Given the importance of MYC in regulating many aspects of cell biology, its intracellular concentration is closely regulated at multiple levels (Stine et al., 2015), including chromatin decompaction (Devaiah et al., 2016); gene transcription (Spencer and Groudine, 1990; Vita and Henriksson, 2006); mRNA stability (Bernstein et al., 1992; Lemm and Ross, 2002; Weidensdorfer et al., 2009) and translation (Wall et al., 2008); and protein degradation (Adhikary and Eilers, 2005; Farrell and Sears, 2014). MYC mRNA has a short half-life of less than 20 min (Dani et al., 1984) and hypoxia decreases MYC mRNA decay in immortalized cells by varied mechanisms (Carraway et al., 2017; Fortenbery et al., 2018; Fry et al., 2017; Zhang et al., 2019; Zhang et al., 2017). In HEK293T cells, 1% oxygen culture increased the half-life of MYC mRNA (Fortenbery et al., 2018). The authors also show that stabilizing HIF with pharmacologic prolyl hydroxylase inhibitors did not reproduce this effect. This differential effect of hypoxic and pharmacologic PHD inhibition resembles our data here describing metabolic differences between these conditions. Electron transport chain inhibitors and ebselen, an antioxidant and mimic of glutathione peroxidase, prevented the hypoxia-mediated increase in MYC mRNA half-life. These experiments suggest an important role for mitochondrially derived reactive oxygen species (ROS) in regulating MYC mRNA stability. Hypoxia also increases N6-methyladenosine modification of MYC mRNA, which decreases ribonucleoprotein binding. Less ribonucleoprotein binding may also contribute to MYC mRNA stabilization (Carraway et al., 2017; Fortenbery et al., 2018). MYC mRNA stability may also be enhanced by the hypoxia-induced down-regulation of micro RNAs miR-449a-5p and let-7g, which contribute to hypoxia-induced proliferation of PASMCs in vitro and pulmonary hypertension in vivo (Zhang et al., 2019; Zhang et al., 2017). MYC protein also has a short half-life of less than 30 min (Salghetti et al., 1999) and is degraded by the proteasome (Lutterbach and Hann, 1994). Two phosphorylation sites, S62 and T58, regulate its stability MYC stability. S62 phosphorylation promotes MYC stability (Lutterbach and Hann, 1994; Sears et al., 2000) and T58 phosphorylation by GSK-3β or BRD4 (Devaiah et al., 2020; Gregory et al., 2003) leading to S62 dephosphorylation, ubiquitination, and proteolysis. Identifying which of these many regulatory mechanisms are most important for sustaining MYC signaling in hypoxia will be critically important for understanding primary cell biology in variety of physiologic and pathophysiologic contexts.

Beyond MYC, the identification of other HIF-independent mechanisms regulating primary cell adaption to hypoxia is of critical importance. Cells express several oxygen-dependent enzymes in addition to PHD whose activities may be altered in hypoxia but not by PHD inhibition. For example, PHD is one of many α-ketoglutarate-dependent dioxygenase enzymes that rely on molecular oxygen for their catalytic activity (Islam et al., 2018). Jumonji-C (JmjC) domain-containing histone demethylases are other prominent members of this family whose inhibition by hypoxia has been shown to cause rapid and HIF-independent induction of histone methylation (Batie et al., 2019). Similarly, a recently described cysteamine dioxygenase has been shown to mediate the oxygen-dependent degradation of Regulators of G protein Signaling 4 and 5 and IL-32 (Masson et al., 2019). In addition to dioxygenase enzymes, electron transport chain dysfunction resulting from impaired Complex IV activity leads to increased ROS production in hypoxia (Chandel et al., 1998). Mitochondrial ROS increase the half-lives of several mRNAs in hypoxia, including MYC, independent of HIF stabilization (Guzy et al., 2005). Finally, hypoxia imposes a reductive stress on cells associated with an increase in the NADH/NAD+ ratio secondary to impaired electron transport (Figure 9—figure supplement 2A–C; Chance and Williams, 1955; Garofalo et al., 1988). NADH accumulation may slow glycolysis via feedback inhibition of GAPDH (Tilton et al., 1991). Any or all these molecular mechanisms may also contribute to uncoupling glycolytic enzyme expression from glycolytic flux as observed in the experiments described here.

In addition to its effects on cellular metabolism, another canonical role of HIF-1 activation is slowing of cellular proliferation rate in the face of limited oxygen availability (Hubbi and Semenza, 2015). The effects of HIF-1 on cell proliferation rate are mediated, in part, by increased expression of cyclin-dependent kinase inhibitor p21 (CDKN1A), inhibition of E2F targets (Gardner et al., 2001), and inhibition of pro-proliferative MYC signaling (Koshiji et al., 2004). These transcriptional effects are precisely what we observed in BAY treated LFs in normoxia. By contrast, hypoxia culture was associated with decreased expression of p21, consistent with a previous report (Mizuno et al., 2009), as well as increased expression of MYC protein and enrichment of MYC target genes. Indeed, the most marked differences between hypoxia and BAY treatment on LF gene transcription were the up-regulation of pro-proliferative gene sets containing E2F targets and G2/M checkpoint proteins. Much of this transcriptional response may be driven by hypoxia-induced up-regulation of MYC, which is known to stimulate cell cycle progression through its effects on the expression and activity of cyclins, cyclin-dependent kinases, and cyclin-dependent kinase inhibitors (Hydbring et al., 2017). Clarifying the complex interactions among HIFs, MYC, and cell proliferation will be important for understanding the cellular response of mesenchymal cells to tissue injury.

Taken together, these findings raise important questions regarding the cell-autonomous role of HIFs in the hypoxia response. On an organismal level, HIFs drive expression of angiogenic and erythropoietic factors to increase oxygen delivery to hypoxic tissues. Within individual cells, HIF-1α seems to be important for mitigating the adverse effects of ROS formation by dysfunctional electron transport in the mitochondria. Indeed, hypoxia increased oxygen consumption and ROS production in HIF-1α-null mouse embryonic fibroblasts (MEFs), which was associated with increased cell death (Zhang et al., 2008). Interestingly, these cells also had increased ATP levels compared to wild type, suggesting that mitochondrial function was adequate under 1% oxygen culture conditions to support oxidative phosphorylation and to meet the energy needs of the cells. Given the prominence of HIFs in mediating the transcriptional response to hypoxia, it is somewhat surprising that neither PHD, HIFs, nor their downstream targets were found to be selectively essential as a function of oxygen tension in a genome-wide CRISPR growth screen of K562 human lymphoblasts cultured in normoxia or hypoxia (Jain et al., 2020). Similarly, knockout of HIF signaling did not affect growth, internal metabolite concentrations, glucose consumption, or lactate production under hypoxia by human acute myeloid leukemia cells (Wierenga et al., 2019). Together with our results, these studies highlight the need for additional research linking hypoxia-induced metabolic changes to their transcriptional and post-transcriptional regulatory mechanisms, particularly in primary cells.

This work also highlights two specific metabolic features that appear to be important in the metabolic response of primary cells to hypoxia. First, both LFs and PASMCs demonstrated notable incorporation of lactate-derived carbon into intracellular metabolic pathways that increased with hypoxia and BAY treatments. This finding is consistent with increasing evidence suggesting an important role for lactate as a metabolic fuel in several organ systems (Faubert et al., 2013; Hui et al., 2017). Although typically considered a metabolic waste product (Rabinowitz and Enerbäck, 2020), an important contribution of lactate import in supporting metabolic homeostasis in the face of an ischemic insult, which is associated with increased extracellular lactate, is an evolutionarily attractive hypothesis that merits further investigation. Second, PASMCs, but not LFs, demonstrated significant rates of reductive carboxylation that increased in 0.5% oxygen. Reductive carboxylation was first identified in hypoxic tumor cells where stable isotope tracing revealed 13C incorporation from labeled glutamine into lipids (Gameiro et al., 2013; Metallo et al., 2011; Scott et al., 2011; Wise et al., 2011). Hypoxia drives PASMC proliferation in vivo, contributing to the development pulmonary hypertension in humans and animal models. Isocitrate dehydrogenase has previously been implicated in the pathobiology of this disease (Fessel et al., 2012), and our findings suggest that reductive carboxylation catalyzed by isocitrate dehydrogenase may be a metabolic vulnerability of hypoxic PASMCs associated with pulmonary vascular disease.

Our finding that hypoxia was associated with decreased glycolysis and lactate fermentation was unexpected. Several aspects of our experimental design may have contributed to this finding. First, our goal was to understand how metabolic reprogramming may support cell proliferation in hypoxia. Thus, we measured metabolite fluxes in cells during the exponential growth phase accounting for cell growth rate, metabolite degradation rates, and medium evaporation with multiple measurements over a 72 hr time course. Often, cells are studied near confluence, where metabolic contributions to biomass production are less and the rate of glycolysis in hypoxia may be higher. Second, we began our experimental treatments 24 hr prior to collecting samples to ensure that the hypoxia metabolic program was established prior to labeling. Similar studies (Grassian et al., 2014; Metallo et al., 2011) typically placed cells into hypoxia at the time of labeling. Third, and perhaps most importantly, these flux determinations were performed in human primary cell cultures rather than immortalized cell lines. Although both cell types used in this study were derived from lung, we anticipate that many of our findings will be generalizable to primary cells from different tissues.

In summary, in this metabolic flux analysis of proliferating human primary cells in vitro, we have demonstrated that MYC uncouples an increase in HIF-dependent glycolytic gene transcription from glycolytic flux in hypoxia. Indeed, the degree of metabolic reprogramming in hypoxia was modest and suggests close coupling between proliferation and metabolism. In light of our findings, additional studies are warranted to clarify the role of HIFs in mediating the metabolic response to hypoxia, to determine how MYC activity is regulated by hypoxia, and to identify other key regulators of hypoxic metabolic reprogramming in primary cells. Moreover, these data strongly caution investigators against drawing conclusions about metabolite flux from measures of gene transcription alone.

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
      <td>Antibody</td>
      <td>anti-HIF-1α (Mouse monoclonal)</td>
      <td>BD Biosciences</td>
      <td>610958</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-c-MYC (Rabbit monoclonal)</td>
      <td>Cell Signaling Technologies</td>
      <td>D84C12</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-LDHA (Rabbit polyclonal)</td>
      <td>Cell Signaling Technologies</td>
      <td>2012</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP-anti-Rabbit IgG (Goat polyclonal)</td>
      <td>Cell Signaling Technologies</td>
      <td>7074</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP-anti-Mouse IgG (Goat polyclonal)</td>
      <td>Cell Signaling Technologies</td>
      <td>7076</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>MYC</td>
      <td>Vector Biolabs</td>
      <td>1285</td>
      <td>adenovirus to express MYC</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>YFP</td>
      <td>Oldham et al., 2015</td>
      <td></td>
      <td>adenovirus control to express YFP</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[1,2–13 C2]-glucose</td>
      <td>Cambridge Isotope Labs</td>
      <td>CLM-504-PK</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[U-13C6]-glucose</td>
      <td>Cambridge Isotope Labs</td>
      <td>CLM-1396-PK</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[U-13C5]-glutamine</td>
      <td>Cambridge Isotope Labs</td>
      <td>CLM-1822-H-PK</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[U-13C3]-lactate</td>
      <td>Sigma</td>
      <td>485926</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BAY</td>
      <td>Cayman</td>
      <td>15297</td>
      <td>Molidustat (BAY-85–3934); 10 μM in DMSO</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Glucose colorimetric assay kit</td>
      <td>Cayman</td>
      <td>10009582</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ʟ-Lactate assay kit</td>
      <td>Cayman</td>
      <td>700510</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pyruvate assay kit</td>
      <td>Cayman</td>
      <td>700470</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NADP/NADPH-Glo Assay</td>
      <td>Promega</td>
      <td>G9081</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>LFs</td>
      <td>Lonza</td>
      <td>CC-2512</td>
      <td>Normal human lung fibroblasts</td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>PASMCs</td>
      <td>Lonza</td>
      <td>CC-2581</td>
      <td>Pulmonary artery smooth muscle cells</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>ACTB</td>
      <td>Life Technologies</td>
      <td>Hs03023943_g1</td>
      <td>qPCR probe</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>GLUT1</td>
      <td>Life Technologies</td>
      <td>Hs00892681_m1</td>
      <td>qPCR probe</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>LDHA</td>
      <td>Life Technologies</td>
      <td>Hs00855332_g1</td>
      <td>qPCR probe</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CDKN1A</td>
      <td>Life Technologies</td>
      <td>Hs00355782_m1</td>
      <td>qPCR probe</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>siMYC</td>
      <td>Dharmacon</td>
      <td>L-003282-02-0005</td>
      <td>ON-TARGETplus siRNA</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>siPHD2</td>
      <td>Dharmacon</td>
      <td>L-004276-00-0005</td>
      <td>ON-TARGETplus siRNA</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>siCTL</td>
      <td>Dharmacon</td>
      <td>D-001810-10-05</td>
      <td>ON-TARGETplus non-targeting control pool</td>
    </tr>
  </tbody>
</table>

### Cell culture

Primary normal human lung fibroblasts (LFs) were purchased from Lonza (CC-2512) and cultured in FGM-2 (Lonza CC-3132). Cells from three donors were used in these studies: #33652 (56 y.o., male), #29132 (19 y.o., female), and #41684 (37 y.o., male). Passages 3–6 were used for experiments. Primary human pulmonary artery smooth muscle cells were purchased from Lonza (CC-2581) and cultured in SmGM-2 (Lonza CC-3182). Cells from three donors were used in these studies: #30020 (64 y.o., male), #27662 (35 y.o., male), #26698 (51 y.o., male), #19828 (51 y.o., male) and #45518 (56 y.o., female). Passages 4–7 were used for experiments. Cell authentication was performed by the vendor. Cells were maintained in a standard tissue culture incubator in 5% CO2 at 37 °C.

### Metabolic flux protocol

For extracellular flux measurements, cells were seeded in either standard growth medium or MCDB131 medium lacking glucose, glutamine, and phenol red (genDEPOT) which was supplemented with 2% dialyzed fetal bovine serum (Mediatech) and naturally labeled glucose and glutamine (‘light’ labeling medium). For LFs, glucose was supplemented at 8 mM and glutamine was supplemented at 1 mM. For PASMCs, glucose was supplemented at 5.55 mM and glutamine was supplemented at 10 mM. These concentrations match the concentrations of these substrates determined in standard growth medium. Preliminary experiments were performed to identify the optimal cell seeding density, exponential growth phase, and labeling duration consistent with metabolic and isotopic steady state. On Day –1, 25,000 cells were seeded in a 35 mm dish in ‘light’ labeling medium. Hypoxia-treated cells were transferred to a tissue culture glovebox set at 0.5% oxygen and 5% CO2 (Coy Lab Products). Medium was supplemented with DMSO 0.1% or BAY (10 μM) for these treatment conditions. On Day 0, cells were washed with PBS and the medium was changed to either ‘light’ labeling medium for flux measurements or ‘heavy’ labeling medium containing [1,2-13C2]-glucose, [U-13C6]-glucose, [U-13C5]-glutamine, or [U-13C2]-lactate for tracer experiments. For LFs, samples were collected on Day 0 and every 24 hr for 72 hr. For PASMCs, samples were collected on Day 0 and every 12 hr for 48 hr. Medium and cell lysates were collected at each time point for intra- and extracellular metabolite measurements and total DNA quantification. Dishes without cells were weighed daily to correct for evaporative medium losses and to empirically determine degradation and accumulation rates of metabolites. Medium samples and cell lysates for DNA measurement were stored at –80 °C until analysis. Each individual experiment included triplicate wells for each treatment and time point, and each experiment was repeated 4–8 times.

### Cell count

Direct cell counts of trypsinized cell suspensions in PBS were obtained following staining with propidium iodide and acridine orange using a LUNA-FL fluorescence cell counter (Logos Biosystems). Indirect cell counts for flux measurements were interpolated from total DNA quantified using the Quant-iT PicoGreen dsDNA Assay Kit (Thermo). Cells were washed once with two volumes of PBS, lysed with Tris-EDTA buffer containing 2% Triton X-100, and collected by scraping. Total DNA in 10 μL of lysate was determined by adding 100 μL of 1 X PicoGreen dye in Tris-EDTA buffer and interpolating the fluorescence intensity with a standard curve generated using the λ DNA standard. Cell counts were interpolated from a standard curve of DNA obtained from known cell numbers seeded in basal medium (Figure 12A). No difference in total cellular DNA was identified between normoxia and hypoxia cultures (Figure 12B–C).

![Figure 12.](https://cdn.elifesciences.org/articles/82597/elife-82597-fig12-v1.jpg)

**Figure 12.:** (A) Standard curve of lung fibroblast (LF) cell count v. total DNA by PicoGreen measurement used to interpolate cell numbers from DNA measurements. Data are mean ± SEM of three biological replicates. (B) Standard curve of PASMC cell count v. total DNA as in (A).

### Immunoblots

Cells were washed with one volume of PBS and collected by scraping in PBS. Cell suspensions were centrifuged at 5000×g for 5 min at 4 °C. Pellets were lysed in buffer containing Tris 10 mM, pH 7.4, NaCl 150 mM, EDTA 1 mM, EGTA 1 mM, Triton X-100 1% v/v, NP-40 0.5% v/v, and Halt Protease Inhibitor Cocktail (Thermo). Protein concentrations were determined by BCA Protein Assay (Thermo). Lysates were normalized for protein concentration and subjected to SDS-PAGE separation on stain-free tris-glycine gels (Bio-Rad), cross-linked and imaged with the Chemidoc system (Bio-Rad), transferred to PVDF membranes with the Trans-Blot Turbo transfer system (Bio-Rad), imaged, blocked in 5% blocking buffer (Bio-Rad), blotted in primary and secondary antibodies, and developed using WesternBright ECL (Advansta). Band signal intensity was normalized to total protein per lane as determined from the stain-free gel or membrane images.

### RT-qPCR

Total RNA was isolated from cells with the RNeasy Mini Kit (Qiagen). cDNA was synthesized from 0.25 to 1.00 ng RNA with the High Capacity cDNA Reverse Transcription Kit (Applied Biosystems). RT-qPCR analysis was performed with an Applied Biosystems 7500 Fast Real Time PCR System with TaqMan Universal PCR Master Mix and pre-designed TaqMan gene expression assays (Life Technologies). Relative expression levels were calculated using the comparative cycle threshold method referenced to ACTB.

### Glucose assay

Medium samples were diluted 10-fold in PBS. Glucose concentration was determined using the Glucose Colorimetric Assay Kit (Cayman) according to the manufacturer’s protocol. Standards were prepared in PBS.

### Lactate assay

Medium samples were diluted 10-fold in PBS. Glucose concentration was determined using the ʟ-Lactate Assay Kit (Cayman). Medium samples did not require deproteinization, otherwise the samples were analyzed according to the manufacturer’s protocol. Standards were prepared in PBS.

### Pyruvate assay

Pyruvate was measured using either an enzymatic assay (most samples) or an HPLC-based assay (medium from 0.2% oxygen experiments). For the enzymatic assay, medium samples were diluted 20-fold in PBS. Pyruvate concentration was determined using the Pyruvate Assay Kit (Cayman). Medium samples did not require deproteinization, otherwise the samples were analyzed according to the manufacturer’s protocol. Standards were prepared in PBS. For the HPLC assay, 2-oxovaleric acid was added to medium samples as an internal standard. Samples were subsequently deproteinized with 2 volumes of ice-cold acetone. Supernatants were evaporated to <50% of the starting volume at 43 °C in a SpeedVac concentrator (Thermo Savant) and reconstituted to the starting volume with HPLC-grade water prior to derivatization. Samples were derivatized 1:1 by volume with o-phenylenediamine (25 mM in 2 M HCl) for 30 min at 80 °C. Derivatized pyruvate was separated with a Poroshell HPH C-18 column (2.1×100 mm, 2.7 μm) on an Infinity II high-performance liquid chromatography system with fluorescence detection of OPD-derivatized α-keto acids as described previously (Guarino et al., 2019).

### Amino acid assay

Medium amino acid concentrations were determined following the addition of norvaline and sarcosine internal standards and deproteinization with 2 volumes of ice-cold acetone. Supernatants were evaporated to <50% of the starting volume at 43 °C in a SpeedVac concentrator (Thermo Savant) and reconstituted to the starting volume with HPLC-grade water prior to analysis. Amino acids in deproteinized medium were derivatized with o-phthalaldehyde (OPA) and 9-fluorenylmethylchloroformate (FMOC) immediately prior to separation with a Poroshell HPH-C18 column (4.6×100 mm, 2.7 μm) on an Infinity II high-performance liquid chromatography system with ultraviolet and fluorescence detection of OPA- and FMOC-derivatized amino acids, respectively, according to the manufacturer’s protocol (Agilent; Long, 2017).

### RNA interference

Approximately 1.25 M LFs were reverse transfected in 6 cm dishes with 40 pmol siRNA or non-targeting siCTL pools (Dharmacon) and 20 μL RNAiMAX (Thermo) in 500 μL OptiMEM (Thermo). After 24 hr, cells were collected by trypsinization and re-seeded as described in Metabolic flux protocol above for growth rate and lactate efflux measurements.

### MYC overexpression

LFs were seeded at 25,000 cells per 35 mm dish on Day –2. On Day –1, cells were transduced with adenovirus for MYC (Vector Biolabs) or YFP overexpression (Oldham et al., 2015). After 24 hr, the medium was changed and samples were collected as described in Metabolic flux protocol above.

### Flux calculations

The growth rate (μ) and flux ($v$) for each measured metabolite were defined as follows Murphy and Young, 2013:

$$
\frac{dX}{dt}=\muX
$$



$$
\frac{dM}{dt}=−kM+vX
$$

where X is the cell density, k is the first-order degradation or accumulation rate, and M is the mass of the metabolite. These equations are solved as follows:

$$
X=X_{0}e^{\mut}
$$



$$
Me^{kt}=\frac{vX_{0}}{\mu+k}(e^{(\mu+k)t}−1)+M_{0}
$$

Growth rate (μ) and cell count at time 0 ($X_{0}$) were determined by robust linear modeling of the logarithm of cell count as a function of time ($t$). Metabolite mass was calculated from the measured metabolite concentrations and predicted well volume accounting for evaporative losses (Figure 1—figure supplement 1E). First-order degradation and accumulation rates were obtained from robust linear modeling of metabolite mass v. time in unconditioned culture medium. Rates that significantly differed from 0 by Student’s t-test were incorporated into the flux calculations. Final fluxes were obtained by robust linear modeling of $Me^{kt}$ versus $e^{\mu+kt}-1$ to determine the slope from which $v$ was calculated using Equation 4.

### Metabolomics

#### Metabolite extraction

Intracellular metabolites were obtained after washing cells with 2 volumes of ice-cold PBS and floating on liquid nitrogen. Plates were stored at –80 °C until extraction. Metabolites were extracted with 1 mL 80% MeOH pre-cooled to –80 °C containing 10 nmol [D8]-valine as an internal standard (Cambridge Isotope Labs). Insoluble material was removed by centrifugation at 21,000×g for 15 min at 4 °C. The supernatant was evaporated to dryness at 42 °C using a SpeedVac concentrator (Thermo Savant). Samples were resuspended in 35 μL LC-MS-grade water prior to analysis.

#### Acquisition parameters

LC-MS analysis was performed on a Vanquish ultra-high-performance liquid chromatography system coupled to a Q Exactive orbitrap mass spectrometer by a HESI-II electrospray ionization probe (Thermo). External mass calibration was performed weekly. Metabolite samples (2.5 μL) were separated using a ZIC-pHILIC stationary phase (2.1×150 mm, 5 μm; Merck). The autosampler temperature was 4 °C and the column compartment was maintained at 25 °C. Mobile phase A was 20 mM ammonium carbonate and 0.1% ammonium hydroxide. Mobile phase B was acetonitrile. The flow rate was 0.1 mL/min. Solvent was introduced to the mass spectrometer via electrospray ionization with the following source parameters: sheath gas 40, auxiliary gas 15, sweep gas 1, spray voltage +3.0 kV for positive mode and –3.1 kV for negative mode, capillary temperature 275 °C, S-lens RF level 40, and probe temperature 350 °C. Data were acquired and peaks integrated using TraceFinder 4.1 (Thermo).

#### Stable isotope quantification

All metabolites except fructose 2,6-bisphosphate (FBP) and 3-phosphoglycerate (3 PG) were measured using the following mobile phase gradient: 0 min, 80% B; 5 min, 80% B; 30 min, 20% B; 31 min, 80% B; 42 min, 80% B. The mass spectrometer was operated in selected ion monitoring mode with an m/z window width of 9.0 centered 1.003355-times half the number of carbon atoms in the target metabolite. The resolution was set at 70,000 and AGC target was 1×105 ions. Peak areas were corrected for quadrupole bias as in Kim et al., 2015. Mass isotope distributions for FBP and 3 PG were calculated from full scan chromatograms as described below. Raw mass isotopomer distributions were corrected for natural isotope abundance using a custom R package (mzrtools; https://github.com/wmoldham/mzrtools; Oldham, 2020) employing the method of Fernandez et al., 1996.

#### Metabolomic profiling

For metabolomic profiling and quantification of isotopic enrichment for FBP and 3 PG, the following mobile phase gradient was used: 0 min, 80% B; 20 min, 20% B; 20.5 min, 80% B; 28 min, 80% B; 42 min, 80% B. The mass spectrometer was operated in polarity switching full scan mode from 70 to 1000 m/z. Resolution was set to 70,000 and the AGC target was 1×106 ions. Peak identifications were based on an in-house library of authentic metabolite standards previously analyzed utilizing this method. For metabolomics studies, pooled quality control (QC) samples were injected at the beginning, end, and between every four samples of the run. Raw peak areas for each metabolite were corrected for instrument drift using a cubic spline model of QC peak areas. Low-quality features were removed on the basis of a relative standard deviation greater than 0.2 in the QC samples and a dispersion ratio greater than 0.4 (Broadhurst et al., 2018). Missing values were imputed using random forest. Sample peak areas were normalized using probabilistic quotient normalization (Dieterle et al., 2006). Differentially regulated metabolites were identified using limma (Ritchie et al., 2015). Metabolite set enrichment analysis was performed using the fgsea package (Korotkevich et al., 2021) with KEGG metabolite pathways (Kanehisa and Goto, 2000).

### Biomass determination

The dry weight of LFs was determined to be 493 pg/cell. The dry weight of PASMCs was determined to be 396 pg/cell. These values were estimated by washing 3×106 cells twice in PBS and thrice in ice-cold acetone prior to drying overnight in a SpeedVac. The composition of the dry cell mass was estimated from the literature (Quek et al., 2010; Sheikh et al., 2005), and stoichiometric coefficients were determined as described (Murphy and Young, 2013; Zamorano et al., 2010).

### Metabolic flux analysis

Metabolic flux analysis was performed using the elementary metabolite unit-based software package INCA (Young, 2014). Inputs to the model include the chemical reactions and atom transitions of central carbon metabolism, extracellular fluxes, the identity and composition of 13C-labeled tracers, and the MIDs of labeled intracellular metabolites. The metabolic network was adapted from previously published networks (Murphy and Young, 2013; Vacanti et al., 2014) and comprises 48 reactions representing glycolysis, the pentose phosphate pathway, the tricarboxylic acid cycle, anaplerotic pathways, serine metabolism, and biomass synthesis. The network includes seven extracellular substrates (aspartate, cystine, glucose, glutamine, glycine, pyruvate, serine) and five metabolic products (alanine, biomass, glutamate, lactate, lipid). Models were fit using three 13C-labeled tracers, [1,2-13C2] glucose, [U-13C6] glucose, and [U-13C5] glutamine. The MIDs of twelve metabolites (2-oxoglutarate, 3-phosphoglycerate, alanine, aspartate, citrate, fructose bisphosphate, glutamate, glutamine, lactate, malate, pyruvate, serine) were used to constrain intracellular fluxes. The following assumptions were made:

Flux estimation was repeated a minimum of 50 times from random initial values. Results were subjected to a χ2 statistical test to assess goodness-of-fit. Accurate 95% confidence intervals were computed for estimated parameters by evaluating the sensitivity of the sum-of-square residuals to parameter variations (Antoniewicz et al., 2006; Murphy and Young, 2013).

### NAD(H) and NADP(H) assays

Cellular NAD+ and NADH were measured using an enzymatic fluorometric cycling assay based on the reduction of NAD+ to NADH by alcohol dehydrogenase (ADH) and subsequent electron transfer to generate the fluorescent molecule resorufin (Oldham et al., 2015). Briefly, cells were washed twice with one volume PBS. Pyridine nucleotides were extracted on ice with buffer containing 50% by volume PBS and 50% lysis buffer (100 mM sodium carbonate, 20 mM sodium bicarbonate, 10 mM nicotinamide, 0.05% by volume Triton-X-100, 1% by mass dodecyltrimethylammonium bromide) and collected by scraping. Extracts were divided equally and 0.5 volume of 0.4 N HCl was added to one sample. Both extracts were heated at 65 °C for 15 min to degrade selectively either the oxidized (buffer) or reduced (HCl) nucleotides. The reaction was cooled on ice and quenched by adding 0.5 M Tris-OH to the acid-treated samples or 0.2 N HCl plus 0.25 M Tris-OH to the buffer samples. Samples were then diluted in reaction buffer (50 mM EDTA and 10 mM Tris, pH 7.06). Cell debris was pelleted by centrifugation, and 50 μL was incubated for 2 h with 100 μL reaction buffer containing 0.6 M EtOH, 0.5 mM phenazine methosulfate, 0.05 mM resazurin, and 0.1 mg/mL ADH. Fluorescence intensities were measured with a Spectramax Gemini XPS (Molecular Devices) with excitation 540 nm, emission 588 nm, and 550 nm excitation cut-off filter. Sample intensities were compared to a standard curve generated from known concentrations of NADH. The ratio of fluorescence in buffer-extracted to acid-extracted samples corresponds to the NADH/NAD+ ratio. Absolute NADH and NAD+ were normalized to estimated cell counts from total DNA quantification as described above.

Samples for NADP+ and NADPH quantification were prepared as described above and analyzed using the luminescence-based NADP/NADPH-Glo assay (Promega).

### RNA-seq

RNA was collected from LFs treated for three days ± hypoxia ± BAY as described above. Four biological replicates were analyzed. Library construction and sequencing was performed by BGI Genomics using 100 bp paired end analysis and a read depth of 50 M reads per sample. Sequences were deposited in the NIH SRA (PRJNA721596). Sequences were mapped to the human GRCh38 primary assembly and counts summarized using Rsubread (Liao et al., 2019). This data is available from the Oldham Lab GitHub repository (https://github.com/oldhamlab/rnaseq.lf.hypoxia.molidustat; Oldham, 2021 ). Differentially expressed transcripts were identified using DESeq2 (Love et al., 2014). Gene set enrichment and transcription factor enrichment was performed using the fgsea and DoRothEA R packages, respectively (Garcia-Alonso et al., 2019; Korotkevich et al., 2021).

### Quantification and statistical analysis

The raw data and annotated analysis code necessary to reproduce this manuscript are contained in an R package research compendium available from the Oldham Lab GitHub repository (https://github.com/oldhamlab/Copeland.2023.hypoxia.flux; Oldham, 2023). Data analysis, statistical comparisons, and visualization were performed in R (R Development Core Team, 2023). Experiments included technical and biological replicates as noted above. The number of biological replicates (n) is indicated in the figure legends. Summary data show the mean ± SEM. Outliers were identified using twice the median absolute deviation as a cutoff threshold. Comparisons were performed using linear mixed-effects models with oxygen, treatment, and their interaction as fixed effects and biological replicate as a random effect. Significant differences in estimated marginal means were identified by comparisons to the multivariate t distribution. Metabolomics and RNA-seq data were analyzed as described above. Probability values less than 0.05 were considered statistically significant.
