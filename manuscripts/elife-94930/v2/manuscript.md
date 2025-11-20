# Rab10 regulates neuropeptide release by maintaining Ca2+ homeostasis and protein synthesis

## Authors

- Jian Dong<sup>1</sup> ([ORCID: 0009-0002-5201-0748](https://orcid.org/0009-0002-5201-0748))
- Miao Chen<sup>2</sup>
- Jan RT van Weering<sup>3</sup> ([ORCID: 0000-0001-5259-4945](https://orcid.org/0000-0001-5259-4945))
- Natalia Domínguez<sup>1</sup>
- Ka Wan Li<sup>2</sup> ([ORCID: 0000-0001-6983-5055](https://orcid.org/0000-0001-6983-5055))
- August B Smit<sup>2</sup>
- Ruud F Toonen<sup>1</sup> ([ORCID: 0000-0002-9900-4233](https://orcid.org/0000-0002-9900-4233))
- Matthijs Verhage<sup>1</sup> ([ORCID: 0000-0002-6085-7503](https://orcid.org/0000-0002-6085-7503)) †

### Affiliations

1. Department of Functional Genomics, Center for Neurogenomics and Cognitive Research (CNCR), Vrije Universiteit (VU) Amsterdam Amsterdam Netherlands ([ROR:008xxew50](https://ror.org/008xxew50))
2. Department of Molecular and Cellular Neurobiology, Center for Neurogenomics and Cognitive Research (CNCR), Vrije Universiteit (VU) Amsterdam Amsterdam Netherlands ([ROR:008xxew50](https://ror.org/008xxew50))
3. Department of Clinical Genetics, Center for Neurogenomics and Cognitive Research (CNCR), University Medical Center Amsterdam Amsterdam Netherlands ([ROR:05grdyy37](https://ror.org/05grdyy37))

† Corresponding author

## Abstract

Dense core vesicles (DCVs) transport and release various neuropeptides and neurotrophins that control diverse brain functions, but the DCV secretory pathway remains poorly understood. Here, we tested a prediction emerging from invertebrate studies about the crucial role of the intracellular trafficking GTPase Rab10, by assessing DCV exocytosis at single-cell resolution upon acute Rab10 depletion in mature mouse hippocampal neurons, to circumvent potential confounding effects of Rab10’s established role in neurite outgrowth. We observed a significant inhibition of DCV exocytosis in Rab10-depleted neurons, whereas synaptic vesicle exocytosis was unaffected. However, rather than a direct involvement in DCV trafficking, this effect was attributed to two ER-dependent processes, ER-regulated intracellular Ca2+ dynamics, and protein synthesis. Gene Ontology analysis of differentially expressed proteins upon Rab10 depletion identified substantial alterations in synaptic and ER/ribosomal proteins, including the Ca2+ pump SERCA2. In addition, ER morphology and dynamics were altered, ER Ca2+ levels were depleted, and Ca2+ homeostasis was impaired in Rab10-depleted neurons. However, Ca2+ entry using a Ca2+ ionophore still triggered less DCV exocytosis. Instead, leucine supplementation, which enhances protein synthesis, largely rescued DCV exocytosis deficiency. We conclude that Rab10 is required for neuropeptide release by maintaining Ca2+ dynamics and regulating protein synthesis. Furthermore, DCV exocytosis appeared more dependent on (acute) protein synthesis than synaptic vesicle exocytosis.

## Introduction

Dense core vesicles (DCVs) transport and release neuromodulators (neuropeptides, neurotrophic factors, and catecholamines) that play crucial roles in modulating diverse brain functions, including sleep, mood, memory, and learning (e.g. Cawley et al., 2016; Malva et al., 2012; Poo, 2001; Salio et al., 2006). Deficits in neuropeptide signaling pathways have been associated with several human disorders and diseases, including anxiety, depression, and obesity (Beck, 2000; Sah and Geracioti, 2013; Barde et al., 2022). Neuropeptides are synthesized in the endoplasmic reticulum (ER) and subsequently packaged into immature DCVs in the Golgi complex (Tooze et al., 2001). DCVs are transported along the neurites and undergo activity-dependent membrane fusion with the plasma membrane to release their content (Farina et al., 2015; Heidelberger et al., 1994; Nassal et al., 2022; Thomas et al., 1993; van de Bospoort et al., 2012). Despite the critical role of neuropeptides in brain functions, the regulatory mechanisms governing their secretion are not fully understood. We have shown previously that Rab3 is an essential regulator in the last steps of the DCV secretory pathway in mammalian neurons (Persoon et al., 2019). However, studies in invertebrates have also implicated other Rab proteins, including Rab2, Rab5, and Rab10, in the DCV secretory pathway (Ailion et al., 2014; Azouz et al., 2014; Edwards et al., 2009; Hannemann et al., 2012; Lund et al., 2020; Sasidharan et al., 2012; Sumakovic et al., 2009).

Among these Rab proteins, Rab10 deficiency produces the strongest inhibition of neuropeptide release in Caenorhabditis elegans (Sasidharan et al., 2012). With its subcellular localization in many vesicular organelles, such as plasmalemmal precursor vesicles, GLUT4 transport vesicles, and recycling endosomes, Rab10 regulates various aspects of intracellular membrane trafficking, including vesicle formation, transport, and fusion (Chen et al., 2006; Larance et al., 2005; Mîinea et al., 2005; Sano et al., 2007; Taylor et al., 2015). Rab10 deficiency leads to deficits in these pathways, resulting in impaired neuronal outgrowth and disrupted retrograde axonal transport of signaling factors (Lazo and Schiavo, 2023). How these deficits relate to the strong inhibition of DCV exocytosis remains unknown.

Deletion of Rab10 expression or inhibiting its functions by overexpression of an inactive mutant (Rab10T23N) leads to abnormal ER morphology (English and Voeltz, 2013; Lv et al., 2015; Shih and Hsueh, 2016). Since the ER is a crucial organelle involved in protein synthesis, Ca2+ buffering, and lipid metabolism, alterations in its structure and function can directly or indirectly affect neuronal secretory pathways. Indeed, several studies have suggested the roles of the ER in the DCV pathway, such as the involvement of ER stress and lipid levels in DCV production in C. elegans (Laurent et al., 2018; Valadas et al., 2018), and the roles of ER Ca2+ as an internal Ca2+ source regulating somatodendritic dopamine release in mouse substantia nigra neurons (Patel et al., 2009). Additionally, Rab10 mutations, altered expression levels, or phosphorylation states are firmly associated with CNS disorders (Agola et al., 2011; Cheng et al., 2005; Kiral et al., 2018). Hence, the strong inhibition of neuropeptide accumulation in coelomocytes in nematode Rab10 mutants may be a direct or indirect effect of Rab10 loss of function on DCV exocytosis and Rab10-dependent disease processes may (in part) be explained by DCV exocytosis impairment.

In the present study, we investigated the involvement of Rab10 in regulated secretion of neuropeptides in mammalian neurons. We directly assessed DCV exocytosis at single-cell resolution in mouse hippocampal neurons and confirmed that Rab10 is a crucial regulator of DCV exocytosis also in mammalian systems, while not affecting synaptic vesicle (SV) exocytosis. However, instead of having a direct role in the DCV secretory pathway, we observed that Rab10 is involved in DCV exocytosis through ER-dependent processes, especially reduced ER Ca2+ homeostasis and impaired global protein synthesis. Supplementation with leucine known to boost protein synthesis rescued the defects in DCV exocytosis. We therefore conclude that Rab10 plays a central role in regulating DCV exocytosis by maintaining Ca2+ homeostasis and protein synthesis.

## Results

### Rab10 regulates neuronal outgrowth but is dispensable for synaptogenesis and SV exocytosis under intense stimulation

To study the role of Rab10 in regulated secretion, we utilized a knockdown strategy since complete knockout of Rab10 results in lethality at cell and organismal levels (Lv et al., 2015). We selected two specific shRNA sequences, shRNA#9 and shRNA#11, to deplete Rab10 expression and a scrambled sequence as control. In mouse cortical neurons infected with either shRNA#9 or shRNA#11 at day in vitro 0 (DIV0), we observed a 75–95% decrease in Rab10 expression at DIV14 (Figure 1A). Previous studies have shown that Rab10 regulates neuronal outgrowth (Wang et al., 2011; Xu et al., 2014). Consistent with these findings, we observed a significantly reduced dendrite and axon length in neurons infected with shRNA#9 at DIV0 (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig1-v2.jpg)

**Figure 1.:** (A) Representative immunoblotting showing knockdown and rescue of Rab10 expression in cultured primary neurons infected with shRNA against Rab10 or rescue constructs (upper) and quantification of Rab10 levels (bottom). (B) Example images of control or Rab10 KD hippocampal neurons (days in vitro [DIV]14) stained for the dendrite marker MAP2 (blue), the synapse marker Syp1 (red), and the axonal marker SMI312 (green). Scale bar: 50 μm (upper) and 10 μm (bottom). (C) Quantification of the dendritic length (MAP2). (D) Quantification of the axonal length (SMI312). (E) Quantification of Syp1 intensity per synapse per neuron. (F) Quantification of the Syp1-positive synapse density in MAP2-positive dendrites. (G) Sholl analysis showing the mean number of dendritic branches against the distance from the soma. (H) Example neurons infected with the SV fusion marker SypHy (upper), typical kymographs of neurites showing SypHy intensity increase during stimulation and upon NH4Cl superfusion (bottom). (I) The average signal SypHy from active synapses, normalized from baseline to maximum fluorescence upon NH4Cl superfusion. (J) SV exocytosis determined as the ratio of the maximum SypHy intensity during stimulation to the maximum during NH4Cl stimulation. (K) SV endocytosis determined as the SypHy signal decay time constant τ in the 60 s after field stimulation. All data are plotted as mean ± s.e.m. (A) N=4, n=4, one-sample t-test. (C–G) Control: N=3, n=35; ShRNA#9: N=3, n=32. (J, K) Control: N=3, n=47; ShRNA#9: N=3, n=56. (C–F, J, K) A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, **=p<0.01, ns=not significant.

To test the effects of Rab10 depletion on synaptogenesis, SVs were quantified using the endogenous marker synaptophysin 1 (Syp1). Syp1 staining exhibited a punctate distribution at DIV14, indicating the accumulation of SVs in boutons/synapses, and no changes in the number of puncta per µm neurite or the intensity of Syp1 puncta (Figure 1E and F). These data confirm that Rab10 regulates neurite outgrowth, but we found no evidence for a role in synaptogenesis.

To test whether Rab10 depletion affects SV exocytosis, hippocampal neurons were infected with the SV exocytosis reporter Synaptophysin-pHluorin (SypHy; Figure 1H; Granseth et al., 2006). SV exocytosis was triggered by high-frequency electrical stimulation (HFS, 5 s 40 Hz). The total vesicle pool was measured by briefly superfusing Tyrode’s solution containing 50 mM NH4Cl. The fraction of fused SVs, determined by the ratio of SypHy intensity upon HFS to the maximum intensity upon NH4Cl superfusion, was comparable in the two groups (Figure 1I and J). In addition, SV endocytosis, measured by the fluorescence decay of SypHy after HFS, was unaffected by Rab10 depletion (Figure 1K). Therefore, we conclude that Rab10 is dispensable for SV exocytosis under intense stimulation.

### Rab10 is a major regulator of DCV exocytosis

To investigate the role of Rab10 in neuropeptide release, we depleted Rab10 levels at DIV0, expressed the DCV exocytosis reporter NPY-pHluorin at DIV9-10, and performed live-cell imaging at DIV14. Our previous studies have demonstrated that NPY-pHluorin almost exclusively localizes to DCVs as indicated by its strong co-localization with endogenous markers of DCVs, such as BDNF and the chromogranins CHGA and CHGB (Arora et al., 2017; Dominguez et al., 2018; Persoon et al., 2019; Persoon et al., 2018). To achieve single-vesicle resolution analysis of DCV exocytosis, we used single cultured hippocampal neurons on glial micro-islands. Neurons were stimulated by 16 trains of 50 action potentials (APs) at 50 Hz, a protocol known to trigger robust DCV exocytosis (Balkowiec and Katz, 2002; Emperador-Melero et al., 2018; Gärtner and Staiger, 2002; Hartmann et al., 2001; Moro et al., 2021; Persoon et al., 2019). Fusion events were detected as a rapid appearance of fluorescent puncta (Figure 2—figure supplement 1A and B). DCV exocytosis in Rab10 KD neurons was significantly reduced by 60% compared to control neurons (Figure 2—figure supplement 1C and D). Furthermore, the total number of DCVs was reduced by 30% in Rab10 KD neurons (Figure 2—figure supplement 1E). The fusion fraction, which represents the number of DCV fusion events relative to the remaining DCV pool after stimulation, was also significantly decreased by 50% in Rab10 KD neurons (Figure 2—figure supplement 1F). Overexpression of wild-type (WT), knockdown-resistant Rab10 rescued DCV exocytosis deficits in Rab10 KD neurons (Figure 2—figure supplement 1C–F).

To overcome the potential confounding effects of impaired neurite outgrowth (Figure 1) and reduced total DCV pool (Figure 2—figure supplement 1) upon Rab10 depletion starting at DIV0, we adopted a more acute approach to interfere with Rab10 function, and late enough not to affect neuronal morphology and the total DCV pool. Neurons were transfected with shRNA against Rab10 at DIV7, fixed at DIV14, and stained with markers for dendrites (MAP2), axons (SMI312), and SVs (Syp1). Rab10 expression was reduced by 70% after 7 days of infection (Figure 3—source data 1). No significant alterations in total dendrite length, axon length (Figure 2A–C and E), or synapse density (Figure 2D) were observed in Rab10 KD neurons under these conditions. Therefore, to eliminate confounding effects on morphological parameters, we reevaluated DCV exocytosis and all further experiments in neurons infected with shRNA at DIV7. DCV exocytosis in Rab10 KD neurons remained significantly lower by 50% compared to control neurons (Figure 2F–I). The fusion fraction was also significantly reduced by 65% in Rab10 KD neurons (Figure 2K). Overexpression of WT Rab10 rescued DCV exocytosis deficits. No significant differences in the total number of DCVs (Figure 2J), DCV transport (Figure 2—figure supplement 2A, B, and E), or cargo loading (Figure 2—figure supplement 2F–K) were observed. Moreover, only 10% of DCVs co-transport with Rab10 (Figure 2—figure supplement 3). Thus, these data indicate that Rab10 depletion specifically inhibits activity-dependent neuropeptide release in hippocampal neurons, without effects on DCV biogenesis, cargo loading, and transport and independent of Rab10’s established role in neuronal outgrowth.

![Figure 2.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig2-v2.jpg)

**Figure 2.:** (A) Example images of control and Rab10 KD hippocampal neurons (days in vitro [DIV]14) stained for MAP2 (blue), Syp1 (red), and SMI312 (green). Scale bar: 30 μm. (B) Quantification of the dendritic length (MAP2). (C) Quantification of the axonal length (SMI312). (D) Quantification of the Syp1-positive synapse density in MAP2-positive dendrites. (E) Sholl analysis showing the mean number of dendritic branches against the distance from the soma. (F) Schematic representation of DCV fusion assay. DCVs are labeled with NPY-pHluorin, and neurons are stimulated with one train of 16 bursts of 50 action potentials (APs) at 50 Hz (light blue bars). (G) Representative neurons during electrical stimulation superimposed with NPY-pHluorin fusion events (green dots). Scale bar: 5 μm. (H) Cumulative plot of DCV fusion events per cell. Light blue bars represent the stimulation trains. (I) Summary graph of DCV fusion events per cell. (J) The total number of DCVs (total pool) of neurons analyzed in H, measured as the number of NPY-pHluorin puncta upon NH4Cl perfusion. (K) Fraction of NPY-pHluorin-labeled DCV fusing during stimulation. All data are plotted as mean ± s.e.m. (B–D) Control: N=3, n=31; ShRNA#9: N=3, N=28; ShRNA#11: N=3, n=31. (I–K) Control: N=4, n=36; shRNA#9: N=4, N=37; shRNA#11: N=4, n=30; Rescue: N=4, n=34. A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, ***=p<0.001, **=p<0.01, *=p<0.05, ns=not significant.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Schematic representation of DCV fusion assay. DCVs are labeled with NPY-pHluorin, and neurons are stimulated with one train of 16 bursts of 50 action potentials (APs) at 50 Hz (light blue bars). (B) Representative neurons during electrode stimulation superimposed with NPY-pHluorin fusion events (green dots). Scale bar: 10μm. (C) Cumulative plot of DCV fusion events per cell. (D) Summary graph of DCV fusion events per cell. (E) Total number of DCVs (total pool) of neurons, measured as the number of NPY-pHluorin puncta upon NH4Cl perfusion. (F) Fraction of NPY-pHluorin-labeled DCV fusing during stimulation. All data are plotted as mean ± s.e.m. (D–F) Control: N=3, n=26; Rab10 KD: N=3, n=47; Rescue: N=3, n=22. (D–F) A one-way ANOVA tested the significance of adding experimental group as a predictor. ***=p<0.001, **=p<0.01, *=p<0.05.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Representative kymographs illustrating the transport of NPY-mCherry-labeled DCVs in control and Rab10 KD neurons. (B) Quantification of average velocity (µm/s) of control and Rab10 KD neurons. (C) Quantification of average distance moved from the start (µm) of control and Rab10 KD neurons. (D) Histogram of average velocity (µm/s) of control and Rab10 KD neurons. (E) Histogram of average distance moved from the start (µm) of control and Rab10 KD neurons. (F) Typical neurite expressing NPY-pHluorin during baseline (b) and during stimulation (s). Scale bar: 10μm. (G) Average traces of NPY-pHluorin fusion events aligned at the moment of fusion (0 s). (H) Quantification of NPY-pHluorin baseline fluorescence before stimulation. (I) Quantification of average NPY-pHluorin fusion intensity per cell. All data are plotted as mean ± s.e.m. (B, C) Control: N=3, n=18; Rab10 KD: N=3, n=17. (H, I) Control: N=3, n=37; Rab10 KD: N=3, n=35. A one-way ANOVA tested the significance of adding experimental group as a predictor. ns=not significant.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Representative kymographs of neurons co-infected with Rab10-GFP and NPY-mCherry. (B) Percentage moving DCVs that co-transport with Rab10. Data are plotted as mean ± s.e.m. (N=3, n=22). Data are plotted as mean ± s.e.m.

### Proteins involved in synaptic transmission and translation are severely dysregulated upon Rab10 depletion

To comprehensively investigate Rab10 function in mature neurons, mass spectrometry proteomics was performed on Rab10 KD and control neurons at DIV14. A total of approximately 5400 unique proteins were identified and quantified in two biological replicates. The complete list of proteins quantified in this study is presented in Figure 3—source data 1. Only differentially expressed proteins detected with high confidence characterized by a log2(fold change)>0.56 and q-value<0.01 were included in the subsequent analysis. Among the dysregulated proteins, 71% were upregulated, while 29% were downregulated, resulting in a significant dysregulation of 19% of the total protein pool in Rab10 KD neurons. These data indicate that Rab10 depletion leads to major neuronal proteome dysregulation within 7 days after initiating knockdown (Figure 3A).

![Figure 3.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig3-v2.jpg)

**Figure 3.:** (A) Volcano plots showing significantly dysregulated proteins in Rab10-depleted neurons. (B) Gene Ontology (GO) enrichment analysis of functional pathways of the significant hits with ClueGO. Shown are the Bonferroni corrected p-values. (C) GO enrichment analysis of subcellular localization of the significant hits with ClueGO. Shown are the Bonferroni corrected p-values. (D) Sunburst plot showing the annotation in synaptic function of the altered proteins in Rab10-depleted neurons. (E) Sunburst plot showing the annotation in synaptic location of the altered proteins in Rab10-depleted neurons. (F) Log2 fold changes of synaptic proteins within SynGO terms. Downregulated proteins are shown in blue and upregulated proteins are shown in black. (G) Examples of proteins that are significantly affected by Rab10 depletion grouped by their subcellular localization. Heat maps represent the degree of up- or downregulation. (H) Selective MS data analysis of ER-related proteins in Rab10 KD neurons. Bars show the fold change of the indicated peptides compared to the control.

To gain insights into the functional consequences of Rab10 depletion, we performed Gene Ontology (GO) analysis using ClueGO (Bindea et al., 2009). This analysis revealed that biological processes related to chemical synaptic transmission were notably affected by Rab10 depletion (Figure 3B). In addition, several biological processes related to protein synthesis, such as cytoplasmic translation and ribosomal large subunit biogenesis, were among the top 5 terms with the lowest p-values (Figure 3B). Subcellular localization analysis of these dysregulated proteins upon Rab10 depletion showed that cytosolic ribosomal proteins were the most significantly affected, followed by dendritic proteins (Figure 3C). Further characterization of the dysregulated synaptic proteins was performed using SynGO (Koopmans et al., 2019). Among the 391 significantly dysregulated proteins annotated in SynGO, 205 were classified as presynaptic proteins and 237 as postsynaptic proteins. GO enrichment analysis revealed that biological processes in metabolism were most dysregulated upon Rab10 depletion. Among them, both pre- and postsynaptic translation were significantly dysregulated (Figure 3D). Consistent with the ClueGO analysis, SynGO highlighted a significant dysregulation of presynaptic (34 of 391) and postsynaptic ribosomal proteins (44 of 391), supporting the involvement of Rab10 in the regulation of neuronal protein synthesis (Figure 3E). Interestingly, all dysregulated ribosomal proteins were upregulated upon Rab10 depletion, which contrasts with the mostly downregulated expression observed in the other classes of proteins (such as synaptic and cytoskeletal proteins) (Figure 3F–G). Taken together, GO analysis with both ClueGO and SynGO indicates a dysfunction of protein translation in Rab10 KD neurons.

Loss of Rab10 expression has been associated with altered ER morphology in mouse embryonic cells (Lv et al., 2015), which may explain the selective upregulation of proteins involved in ribosome function in our proteomics data. Indeed, ER proteins were dysregulated substantially upon Rab10 depletion. Specifically, several rough ER (RER) proteins showed differential regulation, with SEC61A1 being upregulated, SEC61G being downregulated, and CLIMP remaining unchanged (Figure 3H). Most tubular ER proteins, such as RTN3/4 and VAPB, were robustly decreased. Interestingly, one of the ER membrane Ca2+ channels, SERCA2, showed a 50% reduction upon Rab10 depletion (Figure 3H).

Taken together, these analyses reveal that Rab10 depletion leads to major changes in protein expression, especially synaptic and ribosomal proteins, the latter all upregulated in Rab10-depleted neurons which suggests that protein synthesis is dysregulated, potentially due to altered ER function.

### Rab10 regulates ER morphology and ribosomal protein levels

Given the substantial dysregulation of synapse and ribosome/ER proteins, we investigated synapses and ER further using electron microscopy (Figure 4). These analyses revealed an apparently normal synapse morphology in Rab10-depleted neurons with many SVs clustered at the active zone, while DCVs were sparsely distributed along neurites and near the active zone (Figure 4A). The length of the active zone and postsynaptic density were both decreased by 10% upon Rab10 depletion (Figure 4C and D). However, other parameters of synaptic ultrastructure, such as the diameter of SVs or DCVs, and the number of SVs per synapse, remain unchanged in Rab10 KD neurons (Figure 4E–H). Hence, despite substantial dysregulation of synaptic proteins, overall synapse morphology was hardly affected.

![Figure 4.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig4-v2.jpg)

**Figure 4.:** (A) Representative electron microscopy (EM) pictures showing the ultrastructure of synapses. Scale bar: 100 nm. Synaptic ER is indicated by red dotted lines. (B) Representative EM pictures showing the ultrastructure of soma. Rough ER (rER) is indicated by red dotted lines. M: mitochondrion, G: Golgi. Scale bar: 100 nm. (C) Quantification of the length of active zone and postsynaptic density (PSD). (D) Quantification of the length of PSD. (E) Quantification of synaptic vesicle (SV) number per synapse and SV diameter. (F) Quantification of SV diameter. (G) Quantification of dense core vesicle (DCV) diameter. (H) Frequency distribution of DCVs by diameter. (I) Quantification of the diameter of rER. Data are plotted with superplot (C–G, I), where averages from three independent cultures are shown as large circles and single observations are shown as dots. Horizontal lines represent the means of the averages from 3 weeks. Data from different cultures are grouped with different colors. (C–D) Control: N=3, n=184; shRNA#9: N=3, n=187. (E) Control: N=3, n=189; shRNA#9: N=3, n=188. (F) Control: N=3, n=1770; shRNA#9: N=3, n=1803. (G) Control: N=3, n=137; shRNA#9: N=3, n=122. (I) Control: N=3, n=63; shRNA#9: N=3, n=64. (C–G, I) Linear mixed model analysis. ***=p<0.001, *=p<0.05, ns=not significant.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Example images of control or Rab10 KD hippocampal neurons (days in vitro [DIV]14) stained for the dendrite marker MAP2 (green), two ER markers KDEL (red) and RTN4 (magenta). Scale bar: 50 μm. (B) Quantification of RTN4 intensity in MAP2-positive dendrites. (C) Quantification of KDEL intensity in MAP2-positive dendrites. (D) The ratio of neuritic to somatic RTN4 intensity (N/S). (E) The ratio of neuritic to somatic KDEL intensity (N/S). All data are plotted as mean ± s.e.m. (B–D) Control: N=3, n=18; Rab10 KD: N=3, n=18. (B–D) A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, ***=p<0.001, **=p<0.01, *=p<0.05.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Representative time-lapse of ER-mCherry3 signal before (upper), upon (middle), and after (bottom) photobleaching. Scale bar: 20 μm. (B) Average normalized ER-mCherry3 fluorescence recovery after photobleaching in control and Rab10 KD hippocampal neurons. (C) Normalized ER-mCherry3 fluorescence recovery after photobleaching at T=220 s in control and Rab10 KD hippocampal neurons. All data are plotted as mean ± s.e.m. (B, C) Control: N=3, n=23; Rab10 KD: N=3, n=23. (B, C) A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Representative images of wild-type (WT) neurons treated with vehicle (top) or tunicamycin (TM, middle) and Rab10 KD neurons treated with vehicle (bottom). Neurons were stained for ATF4 and MAP2. Scale bar: 50μm. (B) Quantification of ATF4 intensity in soma from each condition. All data are presented as mean ± s.e.m. WT+vehicle: N=2, n=25; WT+vehicle: N=2, n=30; Rab10 KD+vehicle: N=2, n=14. A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, ns=not significant.

Tubular ER was also observed in some presynaptic sections, consistent with previous studies (Deng et al., 2021; Droz et al., 1975; Wu et al., 2017). The percentage of synaptic sections containing tubular ER was decreased by 24% (37% in control versus 28% in Rab10 KD). rER was also studied in the somata of Rab10-depleted and control neurons (Figure 4I). The diameter of rER tubes was reduced by 15% in Rab10 KD neurons. Hence, the substantial dysregulation of ribosomal and ER proteins in Rab10-depleted neurons was accompanied by changes in the abundance of synaptic ER and small changes in ER morphology in the soma.

To study these effects on ER abundance and morphology further, we performed immunofluorescence staining for two endogenous ER markers, KDEL and RTN4. The average fluorescence intensity of RTN4 and KDEL staining was significantly decreased by 35% and 25% respectively in Rab10 KD neurons (Figure 4—figure supplement 1A–C). The relative distributions of RTN4 and KDEL in neurites, as calculated by the intensity ratio of these two proteins in neurites over their somatic intensity, were reduced by 25% and 13%, respectively (Figure 4—figure supplement 1D and E). In conclusion, the ultrastructural changes in ER abundance and morphology upon Rab10 depletion were accompanied by altered distribution of axonal ER, without affecting the ultrastructure of SVs and DCVs.

Finally, given the dynamic nature of ER tubular networks and the involvement of Rab10 in ER tubule extension in COS-7 cells (English and Voeltz, 2013), we tested ER dynamics in Rab10 KD and control neurons expressing the luminal ER marker mCherry-ER3 using live-cell imaging at DIV8, and performed FRAP experiments at DIV14. The recovery of mCherry-ER3 intensity after photobleaching was significantly slower in Rab10 KD neurons with only 50% recovery within 3 min, compared to 80% recovery in control neurons (Figure 4—figure supplement 2C). Collectively, these data indicate that Rab10 depletion leads to reduced levels of ER-resident proteins altered ER abundance and morphology, and impaired ER dynamics.

### Rab10 regulates SERCA2 levels and ER Ca2+ homeostasis

The ER is the largest internal Ca2+ source in neurons and plays a crucial role in maintaining neuronal Ca2+ homeostasis (Karagas and Venkatachalam, 2019). The maintenance of ER Ca2+ primarily relies on the Sarco Endoplasmic Reticulum Calcium ATPase (SERCA), a Ca2+ pump. Among the three major paralogs of SERCA, SERCA2 is particularly enriched in neurons (Britzolaki et al., 2018; Periasamy and Kalyanasundaram, 2007; Xu and Van Remmen, 2021). Consistent with the proteomic analysis which revealed a reduced SERCA2 expression upon Rab10 depletion (Figure 3), immunoblotting confirmed the reduction of SERCA2 levels, showing a 50% reduction in Rab10 KD neurons (Figure 5A and B). Therefore, ER alternations in Rab10 KD neurons may disrupt Ca2+ homeostasis, which is essential for DCV exocytosis.

![Figure 5.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig5-v2.jpg)

**Figure 5.:** (A) Typical immunoblot showing reduced SERCA2 levels in Rab10 KD hippocampal neurons. (B) Quantification of protein levels in Rab10 KD neurons normalized to control. (C) Quantification of somatic ER Ca2+ concentration. (D) Quantification of dendritic ER Ca2+ concentration. (E) Representative image of a neuron infected with ER-GCaMP6-150 displayed with a pseudo line. Scale bar: 3 μm. (F) Typical kymographs of the somatic intensity of ER-GCaMP6-150 showing the intensity decrease upon caffeine superfusion (red line) and the recovery in intensity after caffeine washout. Scale bar: 10 s. (G) Average normalized ER-GCaMP6-150 fluorescence recovery after caffeine treatment. (H) Normalized ER-GCaMP6-150 fluorescence recovery after caffeine treatment at T=190 s. All data are plotted as mean ± s.e.m. (B) Control: N=4, n=4; Rab10 KD: N=4, n=4; (C-D) Control: N=3, n=17; Rab10 KD: N=3; n=17; Rescue: N=3, n=17; (H) Control: N=3, n=23; Rab10 KD: N=3; n=24; GDP-Rab10: n=3, n=10; Rescue: N=3, n=24. A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, ***=p<0.001, **=p<0.01, ns=not significant.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Left: representative cytosolic Fluo-5 AM signals upon caffeine perfusion. Right: representative kymographs of cytosolic Fluo-5 AM signals upon caffeine perfusion in somas. (B) Average traces of Fluo-5 AM signals. (C) Quantification of the peak values of the Fluo-5 AM fluorescence traces upon caffeine perfusion. (D) Quantification of the area under the curve (AUC) of the Fluo-5 AM fluorescence traces upon caffeine perfusion. All data are plotted as mean ± s.e.m. (C, D) Control: N=3, n=44; Rab10 KD: N=3, n=35. (C, D) A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, **=p<0.01.

To test this, we next measured the Ca2+ concentration in ER ([Ca2+]ER) using the ER Ca2+ indicator ER-GCaMP6 (de Juan-Sanz et al., 2017). We observed a reduction in [Ca2+]ER in soma from 130 μM in control neurons to about 70 μM in Rab10-depleted neurons (Figure 5C). [Ca2+]ER in neuritis was also reduced by 15% in Rab10 KD neurons (Figure 5D). The reduction of [Ca2+]ER was rescued by the expression of a knockdown-resistant Rab10 construct. To validate this observation, we assessed ER Ca2+ homeostasis indirectly by measuring the effect of caffeine on cytosolic Ca2+ concentration. As expected, in the absence of extracellular Ca2+, caffeine application (1 μM) triggered an increase in cytosolic Ca2+ due to Ca2+ release from the ER in both WT and Rab10-depleted neurons. However, the peak and the area of the caffeine-induced Ca2+ response curves were both reduced by 30% in Rab10 KD neurons (Figure 5—figure supplement 1).

Furthermore, we examined ER Ca2+ dynamics following a 10 min caffeine treatment. Caffeine activates the ryanodine receptor (RyR), leading to the depletion of ER Ca2+ (Endo, 1975; Fujimoto et al., 1980). As expected, perfusion with caffeine induced ER Ca2+ depletion, followed by recovery toward pre-stimulation levels (Figure 5F and G). In WT neurons, Ca2+ levels were recovered by 90% at T=190 s. However, the refilling of ER Ca2+ was significantly delayed in Rab10 KD neurons or GDP-Rab10 expressing neurons. Ca2+ levels were only recovered by 50% at T=190 s (Figure 5G and H) in these neurons.

Finally, to investigate the consequence of the ER Ca2+ depletion on neuronal Ca2+ homeostasis in Rab10 KD neurons, we measured cytosolic Ca2+ responses triggered by APs using the Ca2+ indicator Fluo5F (Figure 6A–C) and the genetically encoded Synaptophysin-GCaMP6 (Figure 6D–F). The AP-induced Ca2+ responses in the soma, as measured by Fluo5F, were reduced by 40% upon Rab10 depletion (Figure 6C). Similarly, the AP-induced Ca2+ responses in presynaptic nerve terminals, measured by Synaptophysin-GCaMP6, were also reduced (20%, Figure 6F), although this effect was smaller than the effects of Rab10 KD on ER Ca2+ levels and caffeine-induced ER Ca2+ depletion (Figure 5). Taken together, these data suggest that Rab10 knockdown leads to ER Ca2+ depletion and impairs neuronal Ca2+ homeostasis, which may be attributed to the reduced levels of SERCA2 level and slower ER Ca2+ refilling and may contribute to the impaired DCV exocytosis.

![Figure 6.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig6-v2.jpg)

**Figure 6.:** (A) Representative time-lapse of cytosolic Fluo-5 AM upon electrical stimulation (16 action potentials [APs], 50 Hz) in somas of hippocampal neurons. Scale bar: 10 μm. (B) Average normalized response of somatic Fluo-5 AM fluorescence upon stimulation (16 APs, 50 Hz) in hippocampal neurons. (C) Quantification of the area under the curve (AUC) of the Fluo-5 AM fluorescence traces. (D) Typical neurons infected with Synaptophysin-GCaMP6 (upper), typical kymograph of a neurite (bottom) showing Synaptophysin-GCaMP6 intensity increase upon electrical stimulation (16 APs, 50 Hz, blue bars). Scale bar: 5 μm. (E) Average normalized response of Synaptophysin-GCaMP6 fluorescence intensity at presynaptic boutons upon stimulation (16 APs, 50 Hz) in hippocampal neurons. (F) Quantification of the AUC of the Synaptophysin-GCaMP6 fluorescence traces in control and Rab10 KD neurons. All data are plotted as mean ± s.e.m. (C) Control: N=4, n=24; Rab10 KD: N=4, n=30; Rescue: N=4, n=27. (F) Control: N=3, n=33; Rab10 KD: N=3; n=27. A one-way ANOVA tested the significance of adding experimental group as a predictor. **=p<0.01, *=p<0.05, ns=not significant.

### Rab10 depletion impairs ionomycin-induced DCV exocytosis

To determine whether the impaired Ca2+ signaling explains the DCV exocytosis deficiency in Rab10 KD neurons, we stimulated DCV exocytosis using the Ca2+ ionophore ionomycin. This approach bypasses cellular Ca2+ homeostasis and artificially increases the intracellular Ca2+ concentration enough to trigger DCV exocytosis (Persoon et al., 2019). Unexpectedly, DCV exocytosis was still reduced in Rab10 KD neurons (Figure 7A and B). Although the reduction was substantial, 45%, this impairment was not as substantial as observed for AP-induced DCV exocytosis (65%, Figure 2K). The total number of DCV was nearly identical between control and Rab10 KD neurons (Figure 7D). Thus, although a minor fraction of the DCV exocytosis deficits may be explained by impaired Ca2+ signaling (difference between 45% and 65%), other deficits explain most of the DCV exocytosis deficiency in Rab10 KD neurons.

![Figure 7.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig7-v2.jpg)

**Figure 7.:** (A) Representative neurons during electrical stimulation superimposed with NPY- pHluorin fusion events (green dots). Scale bar: 10 μm. (B) Cumulative plot of DCV fusion events per cell. (C) Fraction of NPY-pHluorin-labeled DCVs fusing during stimulation. (D) The total number of DCVs (total pool) of neurons analyzed in B, measured as the number of NPY-pHluorin puncta upon NH4Cl perfusion. All data are plotted as mean ± s.e.m. (C, D) Control: N=3, n=20; Rab10 KD: N=3, n=21. (C, D) A one-way ANOVA tested the significance of adding experimental group as a predictor. *=p<0.05, ns=not significant.

### Rab10 regulates neuronal protein synthesis

Since significant dysregulation of ER markers and ribosomal proteins was observed upon Rab10 depletion, we investigated the effects of Rab10 on protein synthesis using SUnSET to detect nascent peptides formed during puromycin pulse labeling (Schmidt et al., 2009). SUnSET analysis revealed that global protein synthesis was reduced by 30% upon Rab10 depletion (Figure 8A and B).

![Figure 8.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig8-v2.jpg)

**Figure 8.:** (A) Representative western blot showing puromycinilated proteins as a measure for de novo protein synthesis in each condition. (B) Quantification of puromycin intensity in each condition. (B) Representation of the dense core vesicle (DCV) fusion assay. Leucine (5 μM) was added to the culture media and incubated for 72 hr before DCV fusion assay. DMSO (1‰) was used as a control. (C) Cumulative plot of DCV fusion events per cell. (D) Fraction of NPY-pHluorin-labeled DCVs fusing during stimulation. (E) The total number of DCVs (total pool) of neurons analyzed in D, E, measured as the number of NPY-pHluorin puncta upon NH4Cl perfusion. All data are plotted as mean ± s.e.m. (B) All: N=3, n=3; (E, F) Control: N=3, n=47; Control+leu: N=3, n=45; Rab10 KD: N=3; n=61; Rab10+leu: N=3, n=54. Rab10 KD+Rab10: N=3, n=24. (B) One-sample t-test. (E, F) A one-way ANOVA tested the significance of adding experimental group as a predictor. **=p<0.01, *=p<0.05, ns=not significant.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) Typical immunoblot showing pS6K1 levels in each condition. (B) Quantification of relative pS6K1 levels in each condition. All data are plotted as mean ± s.e.m. (C) Control, Control+Leu: N=2, n=2, Rab10 KD, Rab10 KD+Leu: N=2, n=4.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** (A) Typical examples showing the KDEL signals in each condition. Scale bar: 50 μm. (B) Quantification of RTN4 intensity in MAP2-positive dendrites. (C) The ratio of neuritic to somatic RTN4 intensity (N/S). All data are plotted as mean ± s.e.m. (B, C) Control: N=3, n=10; Rab10 KD: N=3, n=11; Rab10 KD+Leu: N=3; n=11. A one-way ANOVA tested the significance of adding experimental group as a predictor. ****=p<0.0001, ns=not significant.

![Figure 8—figure supplement 3.](https://cdn.elifesciences.org/articles/94930/elife-94930-fig8-figsupp3-v2.jpg)

**Figure 8—figure supplement 3.:** (A) Typical examples showing the SERCA2 signals in each condition. Scale bar: 50 μm. (B) Cumulative plot of DCV fusion events per cell. (C) Summary graph of DCV fusion events per cell. (D) Total number of DCVs (total pool) of neurons, measured as the number of NPY-pHluorin puncta upon NH4Cl perfusion. (E) Fraction of NPY-pHluorin-labeled DCV fusing during stimulation. All data are plotted as mean ± s.e.m. (C–E) Control: N=2, n=10; Rab10 KD: N=2, n=13; SERCA2 OE: N=2; n=15. A one-way ANOVA tested the significance of adding experimental group as a predictor. ***=p<0.001, **=p<0.01, ns=not significant.

Protein synthesis impairments may be rescued by supplementation with leucine, a branched-chain amino acid, that promotes protein synthesis by activating the mTOR pathway (Ananieva et al., 2016). To test this in Rab10 KD neurons, additional L-leucine was added to the culture medium to increase the concentration to 5 mM for 3 days. Indeed, 5 mM leucine supplementation significantly restored global protein synthesis deficits caused by Rab10 depletion (Figure 8A and B).

Finally, a similar impairment in global protein synthesis was observed when a loss-of-function mutant of Rab10 (Rab10T23N) was overexpressed in WT neurons (Figure 8A and B). The deficit in protein translation is unlikely attributable to the upregulated mTORC1 signaling as the relative phosphorylation level of pS6K1 was unaffected in Rab10 KD neurons (Figure 8—figure supplement 1). Thus, Rab10 depletion or Rab10T23N expression reduces global protein synthesis in neurons, probably by dysregulation of ER and ribosomal function.

### Leucine supplementation restores normal DCV exocytosis

We hypothesized that protein synthesis deficits in Rab10-depleted neurons explain most of the impaired DCV exocytosis (in addition to a minor fraction explained by disturbed Ca2+ homeostasis, see above) and tested whether leucine supplementation could rescue the DCV exocytosis deficits in Rab10 KD neurons. Rab10-depleted neurons expressing NPY-pHluorin were treated with 5 mM leucine 3 days before live-cell imaging or with dimethyl sulfoxide (DMSO) as a control. Leucine supplementation restored DCV exocytosis by 80% caused by Rab10 depletion but did not alter DCV exocytosis in control neurons (Figure 8C–F). However, leucine supplementation failed to rescue the defects in ER morphology in Rab10 KD neurons (Figure 8—figure supplement 2).

These results suggest that impaired protein synthesis is a major factor contributing to DCV exocytosis deficits in Rab10-depleted neurons.

## Discussion

In this study, we investigated the function of Rab10 in neuropeptide release in mature mouse hippocampal neurons. We found that DCV exocytosis triggered by AP trains was reduced by 65% upon Rab10 depletion, whereas SV exocytosis was unaffected. In addition, we observed a depleted ER Ca2+ pool and an impaired AP-induced Ca2+ response in Rab10 KD neurons. However, DCV exocytosis triggered by Ca2+ ionophore ionomycin, a triggering method independent of Ca2+ channels and internal Ca2+ stores, was also impaired, albeit to a lesser extent. Furthermore, ribosomal proteins were massively dysregulated, and protein synthesis was impeded upon Rab10 depletion. Finally, the DCV exocytosis deficit in Rab10 KD neurons was largely rescued by leucine supplementation. We conclude that the strong inhibition of DCV exocytosis upon Rab10 depletion is mostly due to protein synthesis deficiency and to a lesser extent by dysregulation of Ca2+ channels or internal Ca2+ stores.

### Rab10 regulates neurite outgrowth but not membrane homeostasis in mature neurons

Rab10 is highly enriched in neurons and plays crucial roles in neuronal development (Taylor et al., 2015; Wang et al., 2011; Xu et al., 2014). Consistent with these previous findings, we observed a reduction of axonal and dendritic outgrowth in Rab10-depleted neurons. Also consistent with previous findings in invertebrates (Sasidharan et al., 2012), we observed that the endogenous levels of SV markers remain unchanged, indicating that SV biogenesis was unaffected. However, morphological characterization of neurons infected with shRNAs after the first week in culture did not identify changes in the total length of dendrites or axons, indicating that membrane homeostasis in mature neurons was unaffected by Rab10 knockdown. Therefore, the strong deficit in neuropeptide release in DIV7-infected neurons is unlikely to be confounded by Rab10-dependent aspects of neuronal development.

### Rab10 is crucial for DCV exocytosis

In C. elegans, neuropeptide release was abolished in Rab10 deletion mutants (Sasidharan et al., 2012). We observed a 60% reduction in neuropeptide release in Rab10-depleted mature mouse hippocampal neurons. The difference in effect size could be explained by the incomplete Rab10 depletion with shRNA silencing or by redundant pathways in mammals, e.g., Rab10 and Rab8 are closely related paralogs and share many common effectors (Homma et al., 2021).

Unlike Rab3, which travels together DCVs and exhibits a reduction of over 90% in DCV exocytosis in its quadruple knockout neurons (Persoon et al., 2019), Rab10 does not typically travel with DCVs (Figure 2—figure supplement 3). In addition, no changes in DCV size, puncta intensity, puncta distribution, travel velocity, or distance were detected in Rab10 KD neurons. We conclude that DCV exocytosis deficiency in Rab10-depleted neurons is not caused by alterations in DCV biogenesis or transport and that Rab10 is not required for DCV trafficking.

Although Rab10 is found in subcellular fractions enriched in SVs (Takamori et al., 2006; Taoufiq et al., 2020), it is dispensable for SV exocytosis. Evoked postsynaptic currents were unaffected in Rab10 mutants in C. elegans (Sasidharan et al., 2012). In line with this, SV exocytosis was unaffected in Rab10-depleted hippocampal neurons. These results indicate that Rab10 is selectively required for DCV exocytosis, not for SV exocytosis. Strikingly, many synaptic proteins, including many involved in SV exocytosis, are among the most severely dysregulated proteins upon Rab10 depletion. SV exocytosis may be more resilient to acute protein changes (Sinha et al., 2011) than DCVs. In addition, vesicle secretion properties are different for DCVs and SVs. Unlike SVs, which are secreted upon a single electrical stimulation, DCVs need prolonged or more intense stimulation for the induction of fusion. Thus, the regulatory effects of Rab10 on DCV exocytosis might be amplified under prolonged stimulation.

### Ca2+ homeostasis deficits contribute to DCV exocytosis deficits in Rab10 KD neurons

Rab10 KD neurons showed depleted ER Ca2+ and impaired cytosolic Ca2+ responses. These effects may contribute to the observed DCV exocytosis deficits. Ca2+ released from the ER promotes DCV mobility and potentiates neuropeptide release via activating the CaMKII pathway in Drosophila (Shakiryanova et al., 2007). However, this might not be the case in mouse neurons since most axonal ER takes Ca2+ up from cytosol, instead of releasing it (de Juan-Sanz et al., 2017). Second, triggering Ca2+ release from the ER did not alter DCV transport and fusion (unpublished data from our lab). Finally, a previous study from our lab has shown that CaMKII deficiency does not alter DCV exocytosis (Moro et al., 2020). Hence, dysregulation of ER Ca2+ dynamics may not directly explain the observed DCV exocytosis deficits in Rab10-depleted neurons. However, ER Ca2+ also regulates Ca2+ influx by modulating L-type voltage-gated Ca2+ channels at the plasma membrane via an STIM1-based feedback loop (de Juan-Sanz et al., 2017). Given the importance of Ca2+ influx for DCV exocytosis, dysregulation of ER Ca2+ dynamics may indirectly explain DCV exocytosis deficiency upon Rab10 depletion. However, ionomycin-triggered DCV exocytosis, which bypasses voltage-gated Ca2+ channels, was still reduced, albeit to a lesser extent compared to AP trains. This difference in effect size is consistent with a limited contribution for dysregulation of Ca2+ dynamics and voltage-gated Ca2+ channels to explain the impaired DCV exocytosis in Rab10 KD neurons, while the majority of this phenotype is explained by deficits downstream of protein synthesis.

### A role of Rab10 in protein synthesis largely explains DCV exocytosis deficiency in Rab10 KD neurons

In line with the previous study (Lv et al., 2015), which indicated alteration in ER morphology in Rab10 KO embryonic cells. We observed impaired ER morphology and upregulated ribosomal proteins upon Rab10 depletion. The upregulation of ribosomal proteins might be a compensatory response to altered ER structure as mutation of other ER-shaping proteins, such as VCP and ALT1, causes similar ribosomal abnormalities as Rab10 depletion (Shih and Hsueh, 2016). Protein homeostasis is vital for neuronal function, and deficiency in protein translation is related to several CNS disorders (Cajigas et al., 2010; Holt et al., 2019; Koga et al., 2011; Laguesse and Ron, 2020).

Dysregulation of ribosomes and ER is probably sufficient to explain the impaired protein translation in Rab10 KD neurons. Depleted ER Ca2+ may induce ER stress (Arruda and Hotamisligil, 2015; Fu et al., 2011), which may also contribute to protein translation inhibition, but ATF4 levels are unaffected in Rab10 KD neurons, suggesting that ER stress is at best limited (Figure 4—figure supplement 3A and B). In addition, Rab10 regulates the retrograde transport of TrkB signaling endosomes (Lazo and Schiavo, 2023), which may activate the CREB/mTOR pathway and promote protein synthesis (Moya-Alvarado et al., 2023). Hence, impaired TrkB transport may also contribute to impaired protein translation in addition to dysregulated ribosomes in Rab10 KD neurons. We found that restoring protein synthesis with leucine efficiently increased protein synthesis and largely restored DCV exocytosis deficiency in Rab10-depleted neurons. We conclude that dysregulation of protein synthesis results in DCV exocytosis deficits in these neurons.

In conclusion, our data demonstrate the importance of Rab10 in neuropeptide release and ER homeostasis. We observed altered ER morphology, reduced ER Ca2+ concentration, impaired protein synthesis, and impaired neuropeptide release in Rab10-depleted neurons. These observations shed light on the pathogenesis of Rab10-related disease. In addition, we have shown that leucine can largely rescue deficiency in protein synthesis and neuropeptide release in Rab10-depleted neurons, providing a potential treatment for disorders associated with neuropeptide abnormalities such as depression and anxiety.

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
      <td>Gene (Mus musculus)</td>
      <td>Rab10</td>
      <td>NCBI</td>
      <td>74173</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>C57BL/6J</td>
      <td>Charles River</td>
      <td>Strain code 631</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Rattus norvegicus)</td>
      <td>Wistar (Crl:WI)</td>
      <td>Charles River</td>
      <td>Strain code 003</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>MAP2 (chicken polyclonal)</td>
      <td>Abcam</td>
      <td>ab5392RRID:AB_2138153</td>
      <td>1:200 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>SMI312 (mouse polyclonal)</td>
      <td>Eurogentec</td>
      <td>SMI-312P-050</td>
      <td>1:500 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Synaptophysin 1 (guinea pig polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>101004RRID:AB_1210382</td>
      <td>1:500 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>KDEL (mouse monoclonal)</td>
      <td>Enzo Life Sciences</td>
      <td>ADI-SPA-827-DRRID:AB_2039327</td>
      <td>1:200 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>RTN4 (rabbit polyclonal)</td>
      <td>Novus Biologicals</td>
      <td>NB100-56681RRID:AB_838641</td>
      <td>1:200 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>SERCA2 (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>sc-376235RRID:AB_10989947</td>
      <td>1:200 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rab10 (rabbit polyclonal)</td>
      <td>Protein Tech</td>
      <td>11808-1-APRRID:AB_2173442</td>
      <td>1:2000 (WB)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rab10 (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Ab104859RRID:AB_10711207</td>
      <td>1:2000 (WB)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Actin (mouse monoclonal)</td>
      <td>Chemicon</td>
      <td>MAB1501RRID:AB_2223041</td>
      <td>1:4000 (WB)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Puromycin (mouse monoclonal)</td>
      <td>Bio Connect</td>
      <td>MABE343RRID:AB_2566826</td>
      <td>1:2500 (WB)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Phospho-p70 S6 Kinase (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>9234SRRID:AB_2269803</td>
      <td>1:1000 (WB)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>p70 S6 kinase (rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>9202SRRID:AB_331676</td>
      <td>1:1000 (WB)</td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>shRNA#9</td>
      <td>This paper</td>
      <td>–</td>
      <td>Lentiviral construct to transfect and express the shRNA (see Materials and methods)</td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>shRNA#11</td>
      <td>This paper</td>
      <td>–</td>
      <td>Lentiviral construct to transfect and express the shRNA (see Materials and methods)</td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>Control</td>
      <td>This paper</td>
      <td>–</td>
      <td>Lentiviral construct to transfect and express the control (see Materials and methods)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-NPY-pHluorin</td>
      <td>PMID:31679900</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-NPY-mCherry</td>
      <td>PMID:31679900</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-Synaptophysin-pHluorin</td>
      <td>PMID:34020952</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-Synaptophysin-GCaMP6</td>
      <td>This paper</td>
      <td>–</td>
      <td>Generation of this reagent is described in Materials and methods</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ER-GCaMP6-150</td>
      <td>Addgene</td>
      <td>RRID:Addgene_86918</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>mCherry-ER3</td>
      <td>Addgene</td>
      <td>RRID:Addgene_55041</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>EGFP-Rab10T23N</td>
      <td>Addgene</td>
      <td>RRID:Addgene_86918</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>pLenti-Syn(pr)- Rab10-EGFP</td>
      <td>This paper</td>
      <td>–</td>
      <td>Generation of this reagent is described in Materials and methods</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>2.5% trypsin</td>
      <td>Gibco</td>
      <td>15090046</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Poly-L-ornithine</td>
      <td>Worthington Biochemical Corporation</td>
      <td>LS003127</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Laminin</td>
      <td>Sigma-Aldrich</td>
      <td>L2020</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Poly-D-lysine</td>
      <td>Sigma-Aldrich</td>
      <td>P6407</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>L-Leucine</td>
      <td>Sigma-Aldrich</td>
      <td>L8000</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Tunicamycin</td>
      <td>Sigma-Aldrich</td>
      <td>T7765-10MG</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Puromycin</td>
      <td>Merck/Millipore</td>
      <td>540222-25MG</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ionomycin</td>
      <td>Fisher Emergo</td>
      <td>10429883</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TCE</td>
      <td>Sigma-Aldrich</td>
      <td>115-20-8</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>RRID:SCR_001622</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad</td>
      <td>RRID:SCR_002798</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fiji/ImageJ</td>
      <td>NIH</td>
      <td>RRID:SCR_002285</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_WB: western blot; IF: immunofluorescence._

### Laboratory animals and primary cultures

All animals were bred and housed according to Institutional and Dutch governmental guidelines and regulations. The primary neuronal culture was done as described before (Moro et al., 2021; Persoon et al., 2019). Briefly, hippocampi or cortices were extracted from E18 WT embryos in Hanks’ Balanced Salt Solution (Sigma-Aldrich), supplemented with 10 mM HEPES (Gibco) and were digested with 0.25% trypsin (Gibco) for 20 min at 37°C. Neurons were washed three times and dissociated with fire-polished Pasteur pipettes. Dissociated neurons were spun down at 1000 rpm for 5 min and resuspended in Neurobasal Medium (Gibco) supplemented with 2% B-27 (Gibco), 1.8% HEPES, 0.25% GlutaMAX (Gibco), and 0.1% penicillin/streptomycin. For continental culture, hippocampal neurons were plated at a density of 30,000 on pre-grown rat glia cells, generated by adding 25,000 glia cells on 18 mm glass coverslips coated with 0.1 mg/ml poly-d-lysine (Sigma-Aldrich) in 12-well plates. For island culture, a density of 1500 hippocampal neurons was plated on pre-grown microglia islands, generated by plating 6000 glia cells on 18 mm glass coverslips coated with agarose and stamped with a solution of 0.1 mg/ml poly-d-lysine (Sigma-Aldrich) and 0.7 mg/ml rat tail collagen (BD Biosciences). For western blot (WB), cortical neurons were plated at a density of 300,000 on six-well plates coated with a solution of 0.0005% poly-l-ornithine and laminin (2.5 μg/ml) (Sigma-Aldrich). Neurons were kept in supplemented Neurobasal at 37°C and 5% CO2 for 14–16 days (DIV14–16).

### Plasmid and lentiviral infection

NPY-pHluorin, NPY-mCherry, and Synaptophysin-pHluorin plasmids have been described (Persoon et al., 2019). Synaptophysin-GCaMP6 was generated by adding GCaMP6 to the C-terminus of the mouse sequence of synaptophysin as previously reported (de Juan-Sanz et al., 2017). ER-GCaMP6-150, mCherry-ER3, and Rab10T23N were purchased from Addgene (ER-GCaMP6-150: #86918; mCherry-ER3: #55041; Rab10T23N: #49545). Rab10-EGFP construct was obtained from a mouse cDNA library by PCR and labeled with EGFP at the C-terminus. The target sequences of shRNA are as follows: CGATGCCTTCAATACCACCTT (shRNA#9), GAGAGTTGTACCGAAAGGCAA (shRNA#11), TTC TCCGAACGTGTCACGT (control, scramble), CGATGCATTTAACACAACCTT (Rab10 resistant to shRNA#9).

All plasmids were sequence-verified and packed into lentiviral particles as described previously (Naldini et al., 1996).

### Immunocytochemistry

Neurons were fixed at DIV14–16 in freshly prepared 3.7% paraformaldehyde (EMS) for 20 min at room temperature and permeabilized with 0.5% Triton X-100 (Fisher Chemical) for 5 min, blocked with 0.1% Triton X-100 and 2% normal goat serum for 30 min. Incubation with primary antibodies was done at room temperature for 2 hr or overnight at 4°C. After three times of phosphate-buffered saline (PBS) washing, neurons were incubated with Alexa Fluor-conjugated secondary antibodies (1:1000; Invitrogen) for 1 hr at room temperature. Coverslips were mounted in Mowiol (Sigma-Aldrich) and imaged on a Zeiss LSM 510 confocal laser-scanning microscope (×40 objective; NA 1.3) with LSM510 software (version 3.2 Zeiss) or on an A1R Nikon confocal microscope with LU4A laser unit (×40 objective; NA 1.3) with NIS-Elements software (version 4.60, Nikon). Images were acquired as Z-stack at a step of 0.5 μm. All acquisition settings were kept constant for scans within each experiment. All solutions were in PBS (137 mM NaCl, 2.7 mM KCl, 10 mM Na2HPO4, 1.8 mM KH2PO4, pH 7.4). Primary antibodies used were: MAP2 (Abcam 1:200), SMI312 (Eurogentec, 1:500), synaptophysin 1 (SySy, 1:500), KDEL (Enzo Life Sciences, 1:200), RTN4 (NB100-56681, 1:200), ATF4 (CST, 1:200). To measure ATF4 intensity, neurons were treated with 5 μg/ml tunicamycin (TM; Sigma-Aldrich) or DMSO as vehicle for 24 hr before fixation. Analysis of staining intensity was done with ImageJ. Analysis of neuronal morphology, synapses, or DCV number was performed using the custom-made software SynD (Schmitz et al., 2011).

### Western blotting

Cortical neurons were lysed at DIV14. Lysates were run on a 10% SDS-PAGE gel and transferred to a polyvinylidene difluoride membrane (Bio-Rad). Membranes were blocked with 5% milk (Merck) in PBS with 0.1% Tween 20 for 1 hr at room temperature and incubated in primary antibodies overnight at 4°C. Secondary alkaline phosphatase-conjugated antibodies (1:10,000; Jackson ImmunoResearch) were incubated for 50 min at room temperature. Membranes were visualized with AttoPhos (Promega) and scanned with an FLA-5000 fluorescent image analyzer (Fujifilm). Band intensities of interests were analyzed using Fiji and normalized to the intensity of a loading control (actin).

For de novo-synthesized proteins quantification, surface sensing of translation (SUnSET) was performed as previously described (Schmidt et al., 2009). In brief, neurons were incubated with 2 μM puromycin (InvivoGen) for 30 min before harvesting lysates. Puromycinylated proteins were detected with the anti-puromycin antibody by WB. To measure the total protein level, 2,2,2-trichloroethanol (TCE, Lot # BCBK5461V, Sigma-Aldrich) was dissolved in the gel buffer (0.5%) and gels were scanned with Gel Doc EZ Imager (Bio-Rad).

Antibodies used for WB: actin (1:4000; Chemicon), SERCA2 (Santa Cruz, 1:1000), Rab10 (Proteintech, 1:2000), Rab10 (Abcam, 1:2000), Puromycin (Bio Connect, 1:2500), Phospho-p70 S6 kinase (Cell Signaling Technology, 1:1000), p70 S6 kinase (Cell Signaling Technology, 1:1000).

### Proteomics

DIV14 cortical neurons were prepared as previously described (Gonzalez-Lozano et al., 2019). In brief, neurons were washed three times with ice-cold PBS. Then, 500 μl PBS supplemented with a protease inhibitor cocktail (Roche) was added to each well and neurons were collected by gentle scraping. Neurons were centrifuged for 5 min at 3000×g at 4°C and the pellet was collected and lysed in Laemmli Loading Buffer (4% SDS, 100 mM Tris pH 6.8, 200 mM DTT, 20% glycerol, 0.04% bromophenol blue). In-gel digestion was performed overnight at 37°C with MS grade endo Trypsin/LysC (Promega). The digested peptides were dried using a SpeedVac and stored at − 20°C until further processing. An SDS-PAGE LC-MS/MS approach was used for peptide identification as previously reported. SWATH data were analyzed using Spectronaut 8.0. The spectral library was created from the merging of two data-dependent analyses of non-transfected hippocampal neuron culture and hippocampal synaptosomes containing spike-in iRT peptides from Biognosys. The retention time prediction was set to dynamic iRT; the cross-run normalization based on total peak areas was enabled. Peptide abundances were exported and analyzed using R language for statistical computation. Only peptides present in both control and transfected groups and quantified with high confidence were included (i.e. q-value≤10−3 over all samples in either group, allowing for one outlier within each condition). Protein abundances were computed using Spectronaut normalized peak area, and Loess normalized using the ‘normalizeCyclicLoess’ function from the limma R package (fast method and 10 iterations). Proteins with an adjusted FDR≤0.01 and log2 fold change≥0.56 were defined as significant hints. The proteomics experiment presented in Figure 3 was conducted with two independent cultures with four technical replicates for each condition. For the analysis, we only included peptides that were consistently detected across all samples.

### Bioinformatics

GO analysis on proteomics data was performed with Cytoscope plug-in ClueGO (Bindea et al., 2009). The following settings were used for the biological process analysis in ClueGO: Biological process (update: May 25, 2022), GO term grouping, GO tree interval was set 6–10, GO term consists of min. 3 genes and min. 3% of the term. The GO fusion option was set as true with a threshold of 50%. GO terms were grouped with a Kappa score threshold of 0.4 and named after the most significant GO term. Cellular component analysis: Cellular component analysis (update: May 25, 2022), GO term grouping, GO tree interval was set 6–8, GO term consists of min. 5 genes and min. 5% of the term. The GO fusion option was set as true with a threshold of 50%. GO terms were grouped with a Kappa score threshold of 0.5 and named after the most significant GO term. All detected proteins were input as background. GO analysis of synaptic proteins was done with SynGO as previously described (Koopmans et al., 2019).

### Electron microscopy

Hippocampal neurons plated on coated plates were infected with control or shRNA#9 at DIV7 and fixed at DIV14 with 2.5% glutaraldehyde in 0.1 M cacodylate buffer (pH 7.4). Samples were post-fixed for 1 hr at room temperature in 1% osmium/1% ruthenium. After dehydration by increasing ethanol concentrations (30%, 50%, 70%, 90%, 96%, and 100%), cells were embedded in EPON solution and polymerized for 72 hr at 65°C. Glass coverslips were removed by heating the sample with hot water. Regions with a high density of neurons were selected under light microscopy and mounted on pre-polymerized EPON blocks. Ultrathin sections (70–90 nm) were cut parallel to the cell monolayer and collected on single-slot, formvar-coated copper grids, and stained in uranyl acetate and lead citrate (Leica EM AC20). Sections were imaged in a JEOL1010 transmission electron microscope (JEOL) at 60 kV while being blinded for the experimental conditions. Synapses, somas, and DCV-rich areas were photographed by a side-mounted Modera camera (EMSIS GmbH). For all synaptic analyses, only synapses with intact synaptic plasma membranes with a recognizable pre- and postsynaptic density and clear SV membranes were selected. DCV and ER diameters were measured in iTEM software (Olympus) and synapse parameters were quantified in a custom-written software running in MATLAB (MathWorks) while being blinded for the experimental conditions.

### Live-cell imaging

Neurons at DIV14–16 were transferred to an imaging chamber and perfused with Tyrode’s solution (2 mM CaCl2, 2.5 mM KCl, 119 mM NaCl, 2 mM MgCl2, 30 mM glucose, 25 mM HEPES; pH 7.4). Imaging was acquired on a custom-build microscope (AxioObserver.Z1, Zeiss) with ×40 oil objective (NA 1.3) and an EM-CCD camera (C9100-02; Hamamatsu, pixel size 200 nm) unless otherwise specified. Electrode field stimulation was applied using a stimulus generator (A-385, World Precision Instruments) controlled by a Master-8 (AMPI) to deliver 1 ms pulses of 30 mA. Experiments were performed at room temperature.

For SypHy experiments, neurons were imaged for 30 s as a baseline and then stimulated with electrical field stimulation for 5 s at 40 Hz. After 90 s, neurons were superfused with modified Tyrode’s solution containing NH4Cl (2 mM CaCl2, 2.5 mM KCl, 119 mM NaCl, 2 mM MgCl2, 30 mM glucose, 25 mM HEPES, and 50 mM NH4Cl (pH 7.4)) delivered by gravity flow through a capillary placed above the neurons.

SV fusion analysis was performed as described previously (Moro et al., 2021). Briefly, regions of interest (ROIs) consisting of 6×6 pixels were placed on individual synapses identified as increased signals after the NH4Cl perfusion. Individual traces were analyzed using a custom-made MATLAB (MathWorks) script. Synapses were quantified as active if the maximum ΔF/F0 value upon stimulation was ≥3 * StD(F0). Active synapses were pooled per neuron. SV fusion fraction was calculated as the ΔFstimulation/ΔF NH4Cl.

For DCV fusion experiments, the imaging included 30 s of baseline recording and then stimulated with electrical field stimulation for 16 pulses of 50 AP at 50 Hz. Chemical stimulation of 5 μM ionomycin (Fisher Emergo), dissolved in modified Tyrode’s solution, was applied through glass capillaries placed near the neuron by gravity flow. After 90 s, neurons were superfused with modified Tyrode’s solution containing NH4Cl. For the leucine rescue experiment, neurons expressing NPY-pHluorin were treated with 5 mM leucine 3 days before live-cell imaging or with DMSO as a control.

DCV fusion events were analyzed as described previously (Persoon et al., 2019). Briefly, DCV fusion events were detected by a rapid increase in fluorescence intensity. ROIs consisting of 3×3 pixels were placed on the time-lapse recordings using a custom-made script in Fiji. Resulting traces were evaluated using a custom-made script in MATLAB, and only events with F/F0≥2 SD and a rise time of less than 1 s were recorded. F0 was calculated by averaging the first 10 frames of the time-lapse recording. The total intracellular DCV pool was determined as the number of fluorescent puncta after the superfusion of Tyrode’s solution containing 50 mM NH4Cl. The released fraction was calculated by dividing the number of fusion events per neuron by the total intracellular pool of DCVs.

For DCV transport experiments, neurons were imaged at DIV14 in time-lapse recordings (2 Hz) at room temperature. Stacks were divided into 10×10 regions with the Grid function in ImageJ, and transport was measured in five random regions (coordinates generated by random number generation in MATLAB). Kymographs were generated in ImageJ (MultipleKymograph, line width 3) and were analyzed with a deep learning-based software (KymoButler) as previously described (Jakobs et al., 2019).

### Ca2+ imaging

For cytosolic Ca2+ imaging, neurons were incubated with 1 µM Fluo-5F AM (Molecular Probes, F14222; stock in DMSO) for 10 min at 37°C. For data shown in Figure 6D, E, and F, neurons were perfused with normal Tyrode’s solution and stimulated with the same pattern used for DCV experiments.

For the caffeine-induced Ca2+ responses (Figure 5), neurons were perfused with Tyrode’s solution without Ca2+. Fluorescent intensity in soma was measured with ImageJ. Normalized ΔF/F0 data was calculated per neuron after background subtraction.

For synaptic Ca2+ imaging, neurons were infected with Synaptophysin-GCaMP6 at DIV8 and imaged at DIV14. Neurons were perfused with normal Tyrode’s solution and stimulated with the same pattern used for DCV experiments. 20 neurite-located ROIs (6×6 pixels) and a background ROI were measured per cell. Normalized ΔF/F0 data was calculated per neuron after background subtraction.

For ER Ca2+ measurement, neurons were infected with ER-GCAMP6-150 at DIV8 and were imaged at DIV14 at room temperature. As previously described (de Juan-Sanz et al., 2017), 500 µM or 50 µM ionomycin was applied to saturate the ER-GCAMP6-150 signal in soma or neurite, respectively. [Ca2+]ER were calculated as follows: [Ca2+]ER=Kd((Fr/Fmax−1/Rf)/(1−Fr/Fmax)1/n). Kd is the affinity constant of the indicator (150 μM), Fr is the measured fluorescence at rest, Rf is the dynamic range (45), and n is the Hill coefficient (1.6). Fmax values were not corrected for pH changes.

All Ca2+ imaging experiments were performed in an imaging buffer with an epifluorescence microscope (Nikon Eclipse Ti) equipped with a ×40 oil objective. Quantitative analysis and image processing were performed using ImageJ.

### Fluorescence recovery after photobleaching

Neurons were infected with mCherry-ER3 at DIV9 and imaged at DIV14 on a Nikon Ti-E Eclipse inverted microscope controlled by NIS-Elements software. The acquisition was performed with a ×40 oil objective. After acquiring 10 pre-FRAP images (every 8.5 s), an 80-pixel long ROI on the proximal axon was photobleached with maximal laser power (10 iterations). Images were acquired for 300 s. The post-bleaching fluorescence intensity was normalized to the baseline fluorescence (F0), which was defined as the average intensity of 10 frames before the onset of photobleaching.

### Statistics

All data are presented as mean ± s.e.m. Datasets on single neuron measurements consist of several neuronal cultures (N=number of independent cultures). Within each culture, different coverslips are infected with various viruses to create distinct experimental groups, from which multiple observations (n=individual neurons) are taken. To account for the nested nature of our datasets, a fixed linear regression was performed, in which culture was included as a linear predictor. Possible outliers were identified using the ROUT method using GraphPad Prism software and were excluded from the statistical analysis. A fixed linear regression model was then fitted to the data using the lm() function in R. A one-way ANOVA (analysis of variance) was used to assess whether including the experimental group as a second linear predictor (formula = y ~ Group + Culture) statistically improved the fit of a model without group information (formula = y ~ 1 + Culture). Post hoc analysis was performed using emmeans() function with Turkey adjustment when more than two experimental groups were present. Full statistical information, including exact p-values, is provided in Table 1.

**Table 1.**
 Summary of statistical analyses.


<table>
  <thead>
    <tr>
      <th>Figure</th>
      <th>Dataset</th>
      <th>Groups</th>
      <th>n-number*</th>
      <th>Statistical test</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 A</td>
      <td>Band intensity of Rab10</td>
      <td>Control ShRNA#9 ShRNA#11 Rescue</td>
      <td>4 cultures</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>PshRNA#9=0.0046 (**) PshRNA#11&lt;0.0001 (****) Prescue = 0.5034 (ns)</td>
    </tr>
    <tr>
      <td>1 C</td>
      <td>Dendritic length (MAP2)</td>
      <td>Control ShRNA#9</td>
      <td>3 (35) 3 (32)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.0093 (**)</td>
    </tr>
    <tr>
      <td>1D</td>
      <td>Axonal length (SMI312)</td>
      <td>Control ShRNA#9</td>
      <td>3 (35) 3 (32)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>1E</td>
      <td>Syp1 intensity per synapse per neuron</td>
      <td>Control ShRNA#9</td>
      <td>3 (35) 3 (32)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.4975 (ns)</td>
    </tr>
    <tr>
      <td>1 F</td>
      <td>Syp1-positive synapse density in MAP2-positive dendrites</td>
      <td>Control ShRNA#9</td>
      <td>3 (35) 3 (32)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.4975 (ns)</td>
    </tr>
    <tr>
      <td>1 J</td>
      <td>SypHy fused fraction</td>
      <td>Control ShRNA#9</td>
      <td>3 (47) 3 (56)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.9496 (ns)</td>
    </tr>
    <tr>
      <td>1 K</td>
      <td>Decay content</td>
      <td>Control ShRNA#9</td>
      <td>3 (47) 3 (56)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.2910 (ns)</td>
    </tr>
    <tr>
      <td rowspan="2">2B</td>
      <td rowspan="2">Dendritic length (MAP2)</td>
      <td rowspan="2">Control ShRNA#9 ShRNA#11</td>
      <td rowspan="2">3 (31) 3 (28) 3 (31)</td>
      <td>One-way ANOVA</td>
      <td>P=0.1818 (ns)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs ShRNA#9=0.9771 (ns); pControl vs ShRNA#11=0.3004 (ns); p ShRNA#9 vs ShRNA#11=0.2276 (ns);</td>
    </tr>
    <tr>
      <td rowspan="2">2 C</td>
      <td rowspan="2">Axonal length (SMI312)</td>
      <td rowspan="2">Control ShRNA#9 ShRNA#11</td>
      <td rowspan="2">3 (31) 3 (28) 3 (31)</td>
      <td>One-way ANOVA</td>
      <td>P=0.0936 (ns)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs ShRNA#9=0.5037 (ns); pControl vs ShRNA#11=0.5313 (ns); p ShRNA#9 vs ShRNA#11=0.0823 (ns);</td>
    </tr>
    <tr>
      <td rowspan="2">2D</td>
      <td rowspan="2">Syp1-positive synapse density in MAP2-positive dendrites</td>
      <td rowspan="2">Control ShRNA#9 ShRNA#11</td>
      <td rowspan="2">3 (31) 3 (28) 3 (31)</td>
      <td>One-way ANOVA</td>
      <td>P=0.2126 (ns)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs ShRNA#9=0.3405 (ns); pControl vs ShRNA#11=0.9788 (ns); p ShRNA#9 vs ShRNA#11=0.2503 (ns);</td>
    </tr>
    <tr>
      <td rowspan="2">2I</td>
      <td rowspan="2">DCV fusion events/neuron</td>
      <td rowspan="2">Control ShRNA#9 ShRNA#11 Rescue</td>
      <td rowspan="2">3 (36) 3 (37) 3 (30) 3 (34)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs ShRNA#9=0.0450 (*); pControl vs ShRNA#11=0.0105 (**); p ShRNA#11vs Rescue=0.0021 (**); pShRNA#9 vs Rescue=0.0100 (*);</td>
    </tr>
    <tr>
      <td rowspan="2">2 J</td>
      <td rowspan="2">Total DCV pool/neuron</td>
      <td rowspan="2">Control ShRNA#9 ShRNA#11 Rescue</td>
      <td rowspan="2">3 (36) 3 (37) 3 (30) 3 (34)</td>
      <td>One-way ANOVA</td>
      <td>P=0.1014 (ns)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs ShRNA#9=0.7669 (ns); pControl vs ShRNA#11=0.0584 (ns); p ShRNA#11vs Rescue=0.4978 (ns); pShRNA#9 vs Rescue=0.9969 (ns);</td>
    </tr>
    <tr>
      <td rowspan="2">2 K</td>
      <td rowspan="2">DCV fusion fraction</td>
      <td rowspan="2">Control ShRNA#9 ShRNA#11 Rescue</td>
      <td rowspan="2">3 (36) 3 (37) 3 (30) 3 (34)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs ShRNA#9=0.0014 (**); pControl vs ShRNA#11=0.0001 (****); pControl vs Rescue=0.9902 (ns); pShRNA#9 vs Rescue&gt;0.0048 (**);</td>
    </tr>
    <tr>
      <td rowspan="2">2 suppl 1D</td>
      <td rowspan="2">DCV fusion events/neuron</td>
      <td rowspan="2">Control Rab10 KD Rescue</td>
      <td rowspan="2">3 (26) 3 (47) 3 (22)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD = 0.001 (***); pControl vs Rescue&gt;0.9999 (ns); pRab10 KD vs Rescue=0.0008 (***);</td>
    </tr>
    <tr>
      <td rowspan="2">2 suppl 1E</td>
      <td rowspan="2">Total DCV pool/neuron</td>
      <td rowspan="2">Control Rab10 KD Rescue</td>
      <td rowspan="2">3 (26) 3 (47) 3 (22)</td>
      <td>One-way ANOVA</td>
      <td>P=0.0021</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD = 0.0098(**); pControl vs Rescue=0.9699 (ns); pRab10 KD vs Rescue=0.0138 (*);</td>
    </tr>
    <tr>
      <td rowspan="2">2 suppl 1 F</td>
      <td rowspan="2">DCV fusion fraction</td>
      <td rowspan="2">Control Rab10 KD Rescue</td>
      <td rowspan="2">3 (26) 3 (47) 3 (22)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.002 (**)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.0435 (*); pControl vs Rescue=0.6189 (ns); pRab10 KD vs Rescue=0.0031 (**);</td>
    </tr>
    <tr>
      <td>2 suppl 2B</td>
      <td>DCV transport velocity</td>
      <td>Control Rab10 KD</td>
      <td>3 (18) 3 (17)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.8028(ns)</td>
    </tr>
    <tr>
      <td>2 suppl 2 C</td>
      <td>DCV transport distance</td>
      <td>Control Rab10 KD</td>
      <td>3 (18) 3 (17)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.9131 (ns)</td>
    </tr>
    <tr>
      <td>2 suppl 2 H</td>
      <td>Baseline NPY-phluorin intensity</td>
      <td>Control Rab10 KD</td>
      <td>3 (37) 3 (35)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.2734 (ns)</td>
    </tr>
    <tr>
      <td>2 suppl 2I</td>
      <td>NPY-phluorin fusion intensity</td>
      <td>Control Rab10 KD</td>
      <td>3 (37) 3 (35)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.3385 (ns)</td>
    </tr>
    <tr>
      <td>4 C</td>
      <td>Active zone length</td>
      <td>Control Rab10 KD</td>
      <td>3 cultures</td>
      <td>Linear mixed model</td>
      <td>P=0.023 (*)</td>
    </tr>
    <tr>
      <td>4D</td>
      <td>PSD length</td>
      <td>Control Rab10 KD</td>
      <td>3 cultures</td>
      <td>Linear mixed model</td>
      <td>P=0.020 (*)</td>
    </tr>
    <tr>
      <td>4E</td>
      <td>SV number per synapse</td>
      <td>Control Rab10 KD</td>
      <td>3 cultures</td>
      <td>Linear mixed model</td>
      <td>P=0.746 (ns)</td>
    </tr>
    <tr>
      <td>4 F</td>
      <td>SV diameter</td>
      <td>Control Rab10 KD</td>
      <td>3 cultures</td>
      <td>Linear mixed model</td>
      <td>P=0.612 (ns)</td>
    </tr>
    <tr>
      <td>4 G</td>
      <td>DCV diameter</td>
      <td>Control Rab10 KD</td>
      <td>3 cultures</td>
      <td>Linear mixed model</td>
      <td>P=0.260 (ns)</td>
    </tr>
    <tr>
      <td>4I</td>
      <td>rER diameter</td>
      <td>Control Rab10 KD</td>
      <td>3 cultures</td>
      <td>Linear mixed model</td>
      <td>P&lt;0.001 (***)</td>
    </tr>
    <tr>
      <td>4 suppl 1B</td>
      <td>RTN4 intensity</td>
      <td>Control Rab10 KD</td>
      <td>3 (18) 3 (18)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>4 suppl 1 C</td>
      <td>KDEL intensity</td>
      <td>Control Rab10 KD</td>
      <td>3 (18) 3 (18)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>4 suppl 1D</td>
      <td>Relative N/S intensity of RTN4</td>
      <td>Control Rab10 KD</td>
      <td>3 (18) 3 (18)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.01551 (*)</td>
    </tr>
    <tr>
      <td>4 suppl 1E</td>
      <td>Relative N/S intensity of KDEL</td>
      <td>Control Rab10 KD</td>
      <td>3 (18) 3 (18)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>4 suppl 2 C</td>
      <td>Recovery intensity of mCherry-ER3 after photobleaching at T=220 s</td>
      <td>Control Rab10 KD</td>
      <td>3 (23) 3 (23)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>4 suppl 3B</td>
      <td>ATF4 intensity</td>
      <td>Control Rab10 KD TM</td>
      <td>2 (25) 2 (30) 2 (14)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.1874 (ns); pControl vs TM&lt;0.0001 (****); pRab10 KD vs TM&lt;0.0001 (****);</td>
    </tr>
    <tr>
      <td>5B</td>
      <td>Band intensity of SERCA2</td>
      <td>Control Rab10 KD</td>
      <td>4 cultures</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>P=0.0017 (**)</td>
    </tr>
    <tr>
      <td rowspan="2">5 C</td>
      <td rowspan="2">Somatic ER Ca2+</td>
      <td rowspan="2">Control Rab10 KD Rescue</td>
      <td rowspan="2">3 (17) 3 (17) 3 (17)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD&lt;0.0001 (****); pControl vs Rescue&gt;0.5242 (ns); pRab10 KD vs Rescue&lt;0.0001 (****);</td>
    </tr>
    <tr>
      <td rowspan="2">5D</td>
      <td rowspan="2">Neuritic ER Ca2+</td>
      <td rowspan="2">Control Rab10 KD Rescue</td>
      <td rowspan="2">3 (17) 3 (17) 3 (17)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD&lt;0.0001 (****); pControl vs Rescue&gt;0.5360 (ns); pRab10 KD vs Rescue&lt;0.0001 (****);</td>
    </tr>
    <tr>
      <td rowspan="2">5 H</td>
      <td rowspan="2">Recovery intensity of Fluo-5 AM</td>
      <td rowspan="2">Control Rab10 KD GDP-Rab10 Rescue</td>
      <td rowspan="2">3 (23) 3 (24) 3 (10) 3 (24)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0002 (***)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.0005 (****); pControl vs Rescue&gt;0.9999 (ns); pRab10 KD vs Rescue=0.0013 (****); pControl vs GDP-Rab10=0.0307 (*);</td>
    </tr>
    <tr>
      <td>5 suppl 1 C</td>
      <td>ER Ca2+ release triggered by caffeine (peak)</td>
      <td>Control Rab10 KD</td>
      <td>3 (44) 3 (35)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>5 suppl 1D</td>
      <td>ER Ca2+ release triggered by caffeine (area)</td>
      <td>Control Rab10 KD</td>
      <td>3 (44) 3 (35)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.0025 (**)</td>
    </tr>
    <tr>
      <td>6 C</td>
      <td>Evoked cytosolic Ca2+ influx</td>
      <td>Control Rab10 KD Rescue</td>
      <td>3 (24) 3 (30) 3 (27)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.0062 (**); pControl vs Rescue=0.9891 (ns); pRab10 KD vs Rescue=0.0128 (*);</td>
    </tr>
    <tr>
      <td>6 F</td>
      <td>Evoked presynaptic Ca2+ influx</td>
      <td>Control Rab10 KD</td>
      <td>3 (33) 3 (27)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.0146 (*)</td>
    </tr>
    <tr>
      <td>7 C</td>
      <td>Ionomycin-induced DCV fused fraction</td>
      <td>Control Rab10 KD</td>
      <td>3 (20) 3 (21)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.0009 (****)</td>
    </tr>
    <tr>
      <td>7D</td>
      <td>Total DCV pool/neuron</td>
      <td>Control Rab10 KD</td>
      <td>3 (20) 3 (21)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>P=0.8821 (ns)</td>
    </tr>
    <tr>
      <td>8B</td>
      <td>Band intensity of puromycin</td>
      <td>Control Rab10 KD Rab10T23N KD +Leucine</td>
      <td>3 cultures</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>PRab10 KD=0.0354 (*) PRab10 T23N=0.0053 (**) pKD+Leucine=0.1486 (ns)</td>
    </tr>
    <tr>
      <td rowspan="2">8E</td>
      <td rowspan="2">DCV fused fraction</td>
      <td rowspan="2">Control Control +Leu Rab10 KD Rab10+Leu Rab10 KD +Rab10</td>
      <td rowspan="2">3 (47) 3 (45) 3 (61) 3 (54) 3 (24)</td>
      <td>One-way ANOVA</td>
      <td>P&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD&lt;0.0001 (****); pControl + Leu vs Rab10 KD&lt;0.0001 (****); pRab10 KD vs Rab10 KD + Rab10&lt;0.0001 (****); pRab10 KD vs Rab10 KD + Leu&lt;0.0001 (****); pcontrol vs Rab10 KD + Leu=0.577 (ns)</td>
    </tr>
    <tr>
      <td rowspan="2">8 F</td>
      <td rowspan="2">Total DCV pool/neuron</td>
      <td rowspan="2">Control Control +Leu Rab10 KD Rab10+Leu Rab10 KD +Rab10</td>
      <td rowspan="2">3 (47) 3 (45) 3 (61) 3 (54) 3 (24)</td>
      <td>One-way ANOVA</td>
      <td>P=0.1035</td>
    </tr>
    <tr>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.2484 (ns); pControl + Leu vs Rab10 KD&gt;0.9999 (****); pRab10 KD vs Rab10 KD + Rab10&gt;0.9999 (ns); pRab10 KD vs Rab10 KD + Leu&gt;0.9999 (ns); pcontrol vs Rab10 KD + Leu&gt;0.9999 (ns)</td>
    </tr>
    <tr>
      <td>8 suppl 2B</td>
      <td>KDEL intensity</td>
      <td>Control Rab10 KD Rab10+Leu</td>
      <td>3 (10) 3 (11) 3 (11)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD&lt;0.0001 (****); pcontrol vs Rab10 KD + Leu&lt;0.0001 (****); pRab10 KDvs Rab10 KD + Leu=0.9970(ns);</td>
    </tr>
    <tr>
      <td>8 suppl 2 C</td>
      <td>Relative N/S intensity of KDEL</td>
      <td>Control Rab10 KD Rab10+Leu</td>
      <td>3 (10) 3 (11) 3 (11)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD&lt;0.0001 (****); pcontrol vs Rab10 KD + Leu&lt;0.0001 (****); pRab10 KDvs Rab10 KD + Leu=0.9293(ns);</td>
    </tr>
    <tr>
      <td>8 suppl 3 C</td>
      <td>DCV fusion events/neuron</td>
      <td>Control Rab10 KD SERCA2</td>
      <td>2 (10) 2 (13) 2 (15)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.0084 (**); pControl vs SERCA2 = 0.0095 (**); prab10 KD vs SERCA2 = 0.0095 (**);</td>
    </tr>
    <tr>
      <td>8 suppl 3D</td>
      <td>Total DCV pool/neuron</td>
      <td>Control Rab10 KD SERCA2</td>
      <td>2 (10) 2 (13) 2 (15)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.9988 (ns); pControl vs SERCA2 = 0.9813 (ns); prab10 KD vs SERCA2 = 0.9655 (ns);</td>
    </tr>
    <tr>
      <td>8 suppl 3E</td>
      <td>DCV fused fraction</td>
      <td>Control Rab10 KD SERCA2</td>
      <td>2 (10) 2 (13) 2 (15)</td>
      <td>ANOVA model comparison for nested linear models</td>
      <td>pControl vs Rab10 KD=0.0003 (***); pControl vs SERCA2 = 0.0001 (****); prab10 KD vs SERCA2 = 0.9711 (ns);</td>
    </tr>
  </tbody>
</table>
