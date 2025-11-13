# Cdc48 regulates a deubiquitylase cascade critical for mitochondrial fusion

## Authors

- Tânia Simões<sup>1</sup> ([ORCID: 0000-0002-5971-4935](https://orcid.org/0000-0002-5971-4935))
- Ramona Schuster<sup>1</sup>
- Fabian den Brave<sup>2</sup>
- Mafalda Escobar-Henriques<sup>1</sup> ([ORCID: 0000-0002-0879-3119](https://orcid.org/0000-0002-0879-3119)) †

### Affiliations

1. Institute for Genetics, Cologne Excellence Cluster on Cellular Stress Responses in Aging-Associated Diseases University of Cologne Cologne Germany
2. Department of Molecular Cell Biology Max Planck Institute of Biochemistry, Am Klopferspitz 18 Martinsried Germany

† Corresponding author

## Abstract

Cdc48/p97, a ubiquitin-selective chaperone, orchestrates the function of E3 ligases and deubiquitylases (DUBs). Here, we identify a new function of Cdc48 in ubiquitin-dependent regulation of mitochondrial dynamics. The DUBs Ubp12 and Ubp2 exert opposing effects on mitochondrial fusion and cleave different ubiquitin chains on the mitofusin Fzo1. We demonstrate that Cdc48 integrates the activities of these two DUBs, which are themselves ubiquitylated. First, Cdc48 promotes proteolysis of Ubp12, stabilizing pro-fusion ubiquitylation on Fzo1. Second, loss of Ubp12 stabilizes Ubp2 and thereby facilitates removal of ubiquitin chains on Fzo1 inhibiting fusion. Thus, Cdc48 synergistically regulates the ubiquitylation status of Fzo1, allowing to control the balance between activation or repression of mitochondrial fusion. In conclusion, we unravel a new cascade of ubiquitylation events, comprising Cdc48 and two DUBs, fine-tuning the fusogenic activity of Fzo1.

## Introduction

Mitochondria are dynamic organelles constantly undergoing fusion and fission events, modulated by a variety of post-translational modifiers including ubiquitin (Escobar-Henriques and Langer, 2014; Komander and Rape, 2012). Due to their pathological relevance, e.g. for Parkinson’s disease, these processes are subject to intense investigation. For example, Parkin-dependent ubiquitylation of mitochondrial outer membrane (OM) proteins modulates the elimination of the damaged organelles by mitophagy, or via mitochondrial-derived vesicles (MDV) that fuse with the late endosome (Pickrell and Youle, 2015; Sugiura et al., 2014). Most fusion processes, including the Parkin-MDV pathway, rely on SNAREs (McLelland et al., 2016). In contrast, fusion of the endoplasmic reticulum (ER) and of mitochondria depend on large dynamin-related GTPases (Escobar-Henriques and Anton, 2013; Hu and Rapoport, 2016). In mitochondria, they are named mitofusins (Mfn1/Mfn2 in mammals, Fzo1 in yeast). Deficiencies in Mfn2 cause the type 2 subset of the Charcot-Marie-Tooth disease (CMT), the most common degenerative disorder of the peripheral nervous system (Züchner et al., 2004).

The ubiquitin-specific chaperone Cdc48/p97 is required to maintain mitochondrial morphology (Esaki and Ogura, 2012). However, the underlying molecular mechanism of how Cdc48 regulates mitochondrial dynamics is not understood. Cdc48 is an essential AAA-ATPase and one of the most abundant proteins in the cell, which recognizes many ubiquitylated substrates and is involved in a myriad of biological processes (Franz et al., 2014; Meyer and Weihl, 2014). Cdc48 segregates ubiquitylated substrates from protein complexes, or from membranes, thus allowing their proteolysis by the proteasome (Franz et al., 2014). For example, Cdc48 is important for ER-associated protein degradation (ERAD), modulates the turnover of mitochondrial OM proteins (OMMAD), participates in apoptosis responses (Laun et al., 2001) and mediates clearance of damaged lysosomes by autophagy (Avci and Lemberg, 2015; Heo et al., 2010; Papadopoulos et al., 2017; Tanaka et al., 2010; Wu et al., 2016; Xu et al., 2011; Zattas and Hochstrasser, 2015). On the other hand, Cdc48 also binds E3 ubiquitin ligases and deubiquitylases (DUBs) thereby regulating substrate ubiquitylation (Meyer and Weihl, 2014).

DUBs are proteases that catalyze the reversion of the ubiquitylation reaction (Love et al., 2007), critically contributing to ubiquitin homeostasis (Amerik and Hochstrasser, 2004; Kimura and Tanaka, 2010; Park and Ryu, 2014; Swatek and Komander, 2016). DUBs activate ubiquitin by releasing it from ubiquitin precursor polypeptides but are also determinants for the modification status of ubiquitylated substrates, allowing to dampen ubiquitin-mediated events (Clague et al., 2013). Importantly, DUBs are associated with a number of human diseases and represent promising drug targets, whose regulation and mechanism of action need to be explored (Heideker and Wertz, 2015; Sahtoe and Sixma, 2015). Two deubiquitylases, Ubp2 and Ubp12, were found to have opposite effects on mitochondrial morphology (Anton et al., 2013). Ubiquitin chains on Fzo1 that are recognized and cleaved by Ubp12 activate mitochondrial fusion. In contrast, other ubiquitin chains on Fzo1 that instead are recognized and cleaved by Ubp2 target Fzo1 for proteasomal degradation and inhibit mitochondrial fusion. Therefore, although it is clear that ubiquitin is a double-faced regulator of mitochondrial fusion (Escobar-Henriques and Langer, 2014), how Ubp2 and Ubp12 exert opposite effects on Fzo1 and mitochondrial fusion remained poorly studied.

Here, we identify a role of Cdc48 in mitochondrial fusion, as part of a novel enzymatic cascade consisting of Cdc48, Ubp12 and Ubp2. Cdc48 negatively regulates Ubp12, which negatively regulates Ubp2, explaining why these two DUBs exert opposite effects on their targets and on ubiquitin homeostasis.

## Results

### Cdc48 promotes mitochondrial fusion and prevents Fzo1 turnover

Although it is clear that Cdc48 affects mitochondrial dynamics (Esaki and Ogura, 2012), the underlying mechanisms are unclear. The role of Cdc48 for mitochondrial morphology was investigated in the hypomorphic mutant cdc48-2, expressing GFP targeted to mitochondria. In this allele, Cdc48 is mutated for A547T, in its ATPase domain D2, whereas in the most commonly used cdc48-3 strain, Cdc48 is instead mutated in R387K, in the D1 ATPase (C. Hickey and M. Hochstrasser, p. communication). Both cdc48-3 and cdc48-2 mutations impair typical Cdc48-dependent processes for transmembrane proteins, like ERAD (Bays et al., 2001; Hitchcock et al., 2001; Latterich et al., 1995). We observed that cdc48-2 cells presented fragmented mitochondria (Figure 1A), consistent with the mitochondrial phenotypes observed upon impairment of the ATPase activity of Cdc48 (Esaki and Ogura, 2012). This suggested problems in mitochondrial fusion and prompted us to evaluate the role of Cdc48 on Fzo1, present at the outer membrane of mitochondria. Mitochondrial fusion is abolished in the absence of Fzo1 ubiquitylation (Anton et al., 2013). Consistent with mitochondrial fragmentation, we observed a decrease of Fzo1 ubiquitylation in cdc48-2 mutant cells, when compared to wild-type (wt) cells (Figure 1B, black arrows). We have previously shown that pro-fusion ubiquitylation of Fzo1 increases its stability (Anton et al., 2013). Accordingly, the steady state levels of Fzo1 and its ubiquitylated forms were decreased in cdc48-2 cells (compare Figure 1C and B), to a similar and not significantly different extent (data not shown). Consistent with the cdc48-2 allele, the levels of Fzo1 were slightly decreased in the cdc48-3 mutant or in cells deleted for the Cdc48 co-factors Npl4, Ufd1 and Ufd3/Doa1 (Figure 1—figure supplement 1A–C). It was previously shown that Ubc6, an endoplasmic reticulum (ER) membrane protein, is degraded by the proteasome via ERAD, a process dependent on Cdc48 (Lenk et al., 2002). Therefore, we also analyzed the steady state levels of Ubc6 in the same CDC48 mutant strains. As expected, and in contrast to Fzo1, the steady state levels of Ubc6 were increased upon impairment of Cdc48 activity (Figure 1C and Figure 1—figure supplement 1A–C). This suggested that Cdc48 regulates Fzo1 by a mechanism different from OMMAD or ERAD. Since both Fzo1 and Ubc6 were mostly affected in the cdc48-2 mutant, we decided to use this strain for further analysis. However, it is unclear why cdc48-2 affects Ubc6 and Fzo1 stronger than cdc48-3. We investigated why cdc48-2 mutant cells have lower levels of Fzo1, by testing with cycloheximide (CHX) chase experiments if Cdc48 regulates Fzo1 stability. Moreover, to simultaneously test the role of the proteasome, we deleted the efflux pumps Snq2 and Pdr5. We observed that Fzo1 degradation was inhibited by the presence of the proteasome inhibitor MG132, indicating that the decreased levels of Fzo1 observed in cdc48-2 cells were due to proteasome-dependent turnover of Fzo1 (Figure 1D). In contrast, proteasome inhibition did not affect Fzo1 turnover in wt cells consistent with previous observations (Anton et al., 2013; Escobar-Henriques et al., 2006). Importantly, all these phenotypes could be rescued by expression of the wt Cdc48 protein but not by expression of the Cdc48A547T variant, mimicking the specific mutation in cdc48-2 (Figure 1—figure supplement 2A–C). In conclusion, Cdc48 is required to maintain the Fzo1 protein, thus promoting mitochondrial fusion events.

![Figure 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig1-v2.jpg)

**Figure 1.:** (A) Mitochondrial morphology of CDC48 mutant cells. Wild-type (wt) or cdc48-2 mutant cells were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid. Cellular (Nomarski) and mitochondrial (GFP) morphology were visualized by fluorescence microscopy. Bottom panel, quantification of four independent experiments (with more than 200 cells each) including mean and standard deviation (SD), as described (Cumming et al., 2007). (B) Ubiquitylation of Fzo1 upon mutation of CDC48. Crude mitochondrial extracts from wt or cdc48-2 mutant cells expressing HA-Fzo1, or the corresponding empty vector, were solubilized and analyzed by SDS-PAGE and immunoblotting using HA-specific antibodies. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated by a black arrowhead or black arrows, respectively. Ubiquitylated forms of Fzo1 are labeled with Ub. Bottom panel, quantification of three independent experiments, normalized to PoS and including SD. **, p≤0.01 (paired t-test). (C) Steady state levels of Fzo1 upon mutation of CDC48. Total cellular extracts of wt or cdc48-2 mutant cells were analyzed by SDS-PAGE and immunoblotting using Fzo1- or Ubc6-specific and, as a loading control, Tom40-specific antibodies. Bottom panels, quantification of three independent experiments, including SD. (D) Proteasome dependence of Fzo1 degradation in cdc48-2 mutant cells. The turnover of endogenous Fzo1 expressed in Δpdr5 Δsnq2 and Δpdr5 Δsnq2 cdc48-2 cells was assessed after inhibition of cytosolic protein synthesis with cycloheximide (CHX), for the indicated time points in exponentially growing cultures in absence or presence of the proteasomal inhibitor MG132. Samples were analyzed by SDS-PAGE and immunoblotting using Fzo1-specific, Ubc6-specific (as an unstable protein control) and Sec61-specific (as a loading control) antibodies. Right panel, quantification of five independent experiments, including SD. PoS, PonceauS staining.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Steady state levels of Fzo1 upon mutation of CDC48. Total cellular extracts of Δfzo1 or wt cells or different CDC48 mutant cells were analyzed by SDS-PAGE and immunoblotting using Fzo1-, Ubc6- and Tom40-specific antibodies. Bottom panels, quantification of five independent experiments, including SD. ns, p>0.05; *, p≤0.05; ***, p≤0.001 (One-way ANOVA, Tukey’s multiple comparison test). (Β) Role of Cdc48 cofactors in the steady state levels of Fzo1. Total cellular extracts of wt cells or ufd1-2 and npl4-1 mutant cells were analyzed by SDS-PAGE and immunoblotting using Fzo1- or Ubc6-specific antibodies. Bottom panels, quantification of seven (ufd1-2) or nine (npl4-1) independent experiments, including SD. **p≤0.01; ***p≤0.001 (paired t-test). (C) Steady state levels of Fzo1 upon deletion of DOA1. Total cellular extracts of Δfzo1, wt or Δdoa1 cells were analyzed by SDS-PAGE and immunoblotting using Fzo1-, Ubc6- and Tom40-specific antibodies. Bottom panel, quantification of five independent experiments, including SD. *p≤0.05 (paired t-test). PoS, PonceauS staining.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Rescue analysis of Fzo1 steady state levels in cdc48-2 cells. Total cellular extracts of wt or cdc48-2 mutant cells expressing Cdc48, Cdc48A547T or the corresponding empty vector were analyzed by SDS-PAGE and immunoblotting using an HA-specific antibody. (B) Rescue analysis of Fzo1 ubiquitylation in cdc48-2 cells. Crude mitochondrial extracts from wt or cdc48-2 mutant cells, additionally expressing HA-Fzo1 and Cdc48, Cdc48A547T or the corresponding empty vector, as indicated, were lysed and HA-tagged Fzo1 was precipitated using HA-coupled beads. Samples were analyzed by SDS-PAGE and immunoblotting using an HA-specific antibody. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in Figure 1B. (C) Rescue analysis of mitochondrial morphology in cdc48-2 cells. Wt or cdc48-2 mutant cells expressing Cdc48 or Cdc48A547T or the corresponding empty vector as indicated were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Quantification from three different experiments (with more than 200 cells each), including SD, as described (Cumming et al., 2007). IP, immunoprecipitation. PoS, PonceauS staining.

### Cdc48 binds and regulates ubiquitylated Fzo1

We further investigated how Cdc48 affected Fzo1. Given that stress conditions disrupt mitochondrial tubulation (Knorre et al., 2013), it was important to show that Cdc48 directly regulates Fzo1 and mitochondrial morphology. First, co-immunoprecipitation experiments revealed that Cdc48 physically interacted with Fzo1 (Figure 2A). We previously showed that the formation of ubiquitin chains on Fzo1 (Figure 2A, black arrows), which are linked to lysine 398, requires previous ubiquitylation of its lysine 464 (Anton et al., 2013). Therefore, Fzo1 ubiquitylation is lost in the mutant Fzo1K464R (Figure 2A). We observed that the interaction between Cdc48 and the non-ubiquitylated variant Fzo1K464R was impaired (Figure 2A), in agreement with ubiquitin being recognized by Cdc48. To assess the specificity of the cdc48-2 effect on Fzo1 protein levels, we tested if this depended on Fzo1 ubiquitylation. Thus, the non-ubiquitylated variant Fzo1K464R was used. We observed that the steady state levels of Fzo1K464R were largely insensitive to the cdc48-2 mutation (Figure 2—figure supplement 1). This points to a direct regulatory role of Cdc48 on Fzo1, only after its ubiquitylation. These pro-fusion ubiquitin forms on Fzo1 are recognized by Ubp12. In addition, we previously identified other ubiquitin forms on Fzo1, that inhibit fusion. They are removed by Ubp2 and can be detected only in the presence of the catalytically inactive variant Ubp2C745S (Anton et al., 2013) (Figure 2B, Input, red arrows). Therefore, we investigated binding of Cdc48 to Fzo1 under these conditions, where both pro-fusion and anti-fusion forms are present. We noticed that despite the clear increase in ubiquitylation of Fzo1 upon Ubp2C745S expression (2.44 times), Cdc48 binding to Fzo1 was not increased (Figure 2B). Therefore, the additional presence of ubiquitin chains inhibiting fusion does not increase Cdc48 binding. Consistently, for the Fzo1K464R variant, which in the presence of Ubp2C745S is ubiquitylated to a similar level as the wt protein (0.96 times, despite the absence of pro-fusion ubiquitylation), no binding to Cdc48 above background can be detected. Thus, similar to Ubp12, Cdc48 recognizes specifically the pro-fusion ubiquitylated forms of Fzo1.

![Figure 2.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig2-v2.jpg)

**Figure 2.:** (A) Physical interaction between Cdc48 and ubiquitylated Fzo1. HA-Fzo1, HA-Fzo1K464R or the corresponding vector were expressed in ∆fzo1 cells. Crude mitochondrial extracts were lysed and HA-tagged Fzo1 was precipitated using HA-coupled beads and analyzed by SDS-PAGE and immunoblotting using HA- and Cdc48-specific antibodies. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in 1B. (B) Effect of the anti-fusion ubiquitylation of Fzo1 on its interaction with Cdc48. HA-Fzo1 or HA-Fzo1K464R, expressed in the presence of Ubp2 (∆fzo1 cells plus empty vector) or Ubp2C745S (∆ubp2 ∆fzo1 cells plus Ubp2C745S-Flag), or the corresponding vector control (the empty vectors corresponding to HA-Fzo1 and Ubp2C745S-Flag, expressed in ∆ubp2 ∆fzo1 cells), were analyzed for Cdc48 interaction, as in 2A. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated by a black arrowhead or black arrows, respectively. Red arrows with no fill indicate Fzo1 ubiquitylated species specifically accumulating upon expression of Ubp2C745S. PoS, PonceauS staining; IP, immunoprecipitation; WB, western blot.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Steady state levels of HA-Fzo1K464R upon mutation of CDC48. Total cellular extracts of ∆fzo1 or ∆fzo1 cdc48-2 mutant cells expressing HA-Fzo1 or HA-Fzo1K464R were analyzed by SDS-PAGE and immunoblotting using Fzo1-,Ubc6- and Tom40-specific antibodies. Bottom panel, quantification of four independent experiments, including SD. PoS, Ponceau S staining.

### Cdc48 supports turnover of ubiquitylated Ubp12

Given the specific interaction of both Cdc48 (Figure 2B) and Ubp12 (Anton et al., 2013) with ubiquitin chains on Fzo1 promoting fusion, we tested if Cdc48 regulated Ubp12. To analyze if Ubp12 is an unstable protein, wt and cdc48-2 cells were transformed with an episomal plasmid expressing Ubp12 under the ADH1 promoter (Anton et al., 2013). CHX chase experiments revealed that Ubp12 is degraded in a Cdc48- and proteasome-dependent manner (Figure 3—figure supplement 1A and B). Similarly, chromosomally tagged Ubp12 is an unstable protein and its turnover depends on Cdc48 (Figure 3A). To analyze if Ubp12 is ubiquitylated, the DUB was immunoprecipitated and analyzed by immunoblotting for Ubp12-Flag or for ubiquitin (Figure 3B). We observed slower migrating forms of Ubp12 with the Flag-specific antibody, which were also detected by a ubiquitin-specific antibody. These studies demonstrated that Ubp12 is modified by ubiquitin. We next tested whether Cdc48 could be co-immunoprecipitated with Ubp12, from solubilized crude mitochondrial extracts. We observed that Ubp12 physically interacted with Cdc48 (Figure 3C), suggesting that Cdc48 directly supports degradation of ubiquitylated Ubp12.

![Figure 3.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig3-v2.jpg)

**Figure 3.:** (A) Stability of the Ubp12 protein. The turnover of Ubp12 endogenously Flag tagged (Ubp12-Flagint), in wt or cdc48-2 cells, was assessed with CHX chase, as in 1D. Samples were analyzed by SDS-PAGE and immunoblotting using a Flag-, Tom40- and, as an unstable protein control, a Ubc6-specific antibody. Bottom panel, quantification of three independent experiments, including SD. (B) Ubiquitylation of Ubp12. The Ubp12C372S-Flag inactive variant, expressed from an episomal plasmid, was immunoprecipitated from total soluble extracts using Flag-coupled beads. After elution, Ubp12 was analyzed by western blot using Flag- or ubiquitin (Ub - P4D1)-specific antibodies. Ubiquitylated forms of Ubp12C372S-Flag are labeled with Ub. (C) Physical interaction between Cdc48 and Ubp12. The catalytically inactive Ubp12C372S-Flag variant, expressed from an episomal plasmid, or the corresponding empty vector, were expressed in Δubp12 (CDC48) or Δubp12 cdc48-2 (cdc48-2) mutant cells and analyzed for Cdc48 interaction. Crude mitochondrial extracts were lysed, Flag-tagged Ubp12 was precipitated using Flag-coupled beads, and the eluate analyzed by SDS-PAGE and immunoblotting using Flag- and Cdc48-specific antibodies. PoS, Ponceau S staining; IP, immunoprecipitation; WB, western blot.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Turnover of episomal Ubp12 in wt or cdc48-2 cells. Ubp12-Flag stability was assessed after inhibition of cytosolic protein synthesis with cycloheximide (CHX), for the indicated time points in exponentially growing cultures. Samples were analyzed by SDS-PAGE and immunoblotting using Flag-, Ubc6- and Tom40-specific antibodies. Bottom panel, quantification of three independent experiments, including SD. (B) Proteasome dependence of Ubp12-Flag degradation. The turnover of Ubp2-Flag, expressed from an episomal plasmid, was assessed as in 1D. Samples were analyzed by SDS-PAGE and immunoblotting using Flag-, Ubc6- and Ssc1-specific antibodies. (C) Ubp12 expression levels. Expression levels of endogenously Flag-tagged Ubp12 (Ubp12-Flagint), Ubp12-Flag expressed from an episomal plasmid and endogenously Flag-tagged Ubp12 under the control of a pGAL promoter (pGAL-Ubp12-Flagint) (grown in glucose or galactose as indicated) were analyzed by SDS-PAGE and immunoblotting using Flag- and Ssc1-specific antibodies. Pos, PonceauS staining.

### Cdc48 regulation of Fzo1 depends on Ubp12

Our results show that Cdc48 and Ubp12 have opposing roles on Fzo1 ubiquitylation levels (Figure 1B and [Anton et al., 2013]). Consistently, Ubp12 and Cdc48 also present opposing phenotypes regarding mitochondrial tubulation (Figure 1A and [Anton et al., 2013]). Given that Cdc48 controls Ubp12 levels, we speculated that Cdc48 regulates mitochondrial morphology and Fzo1 via Ubp12. We monitored mitochondrial morphology in cdc48-2 cells in presence or absence of UBP12, expressing mitochondrial-targeted GFP. Strikingly, deletion of UBP12 in cdc48-2 cells rescued mitochondrial tubulation, resembling Δubp12 cells (Figure 4A). Importantly, the mitochondrial hypertubulation of Δubp12 cells depended on Fzo1 (Figure 4—figure supplement 1A–C). Even in Δfzo1 Δdnm1 cells, resembling wt cells in mitochondrial shape, further deletion of UBP12 did not induce hypertubulation, confirming that Ubp12 regulates mitochondrial morphology via Fzo1 (Figure 4—figure supplement 1D). Mitochondrial fusion is also required to maintain the cellular growth on respiratory media, i.e. media containing the non-fermentable carbon sources glycerol or lactate (Hermann et al., 1998). Therefore, to further support the physiological importance of Cdc48 and Ubp12, we analyzed the respiratory capacity of cdc48-2 in presence or absence of UBP12. In agreement with restored tubulation of mitochondria, we observed that the growth defect of cdc48-2 cells at 37°C on lactate media could be improved upon deletion of UBP12 (Figure 4B). Given that Δfzo1 cells irreversibly loose mitochondrial DNA, we investigated if this is also the case for cdc48-2 cells. Consistent with the respiratory reversibility of cdc48-2 cells upon further deletion of UBP12, we observed that cdc48-2 cells did not lose mitochondrial DNA (Figure 4—figure supplement 2A and B). Importantly, the respiratory defect of cdc48-2 cells could be complemented by expression of Cdc48 but not of Cdc48A547T (Figure 4—figure supplement 2C). Finally, cdc48-2Δubp12 cells also showed improved ubiquitylation of Fzo1 (Figure 4C). Together, these results show that Cdc48 maintains Fzo1 ubiquitylation and activates mitochondrial fusion by downregulating Ubp12. However, two pieces of evidence suggest that Cdc48 might have other functions in this pathway, apart from regulating Ubp12. First, we observed that the physical interaction between Fzo1 and Cdc48 is not mediated by Ubp12 (Figure 4—figure supplement 2D), suggesting that Cdc48 directly recognizes ubiquitylated Fzo1. Second, deletion of UBP12 in cdc48-2 cells did not restore the steady state levels of Fzo1 (Figure 4—figure supplement 2E). Notably, this is consistent with our previous observation that mitochondrial fusion depends on ubiquitylated rather than on the steady state levels of Fzo1 (Anton et al., 2013).

![Figure 4.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig4-v2.jpg)

**Figure 4.:** (A) Mitochondrial morphology upon deletion of UBP12 and/or mutation of CDC48. The indicated mutant cells were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Right panel, quantification from three different experiments (with more than 200 cells each), including SD, as described (Cumming et al., 2007) (B) Respiratory capacity of cells upon deletion of UBP12 and/or mutation of CDC48. Fivefold serial dilutions of exponentially growing cells of wt or the mutant strains Δubp12, cdc48-2, and Δubp12 cdc48-2 were spotted on YP media supplemented with lactate (YPLac) and incubated at 30°C for two days or 37°C for five days. (C) Ubiquitylation levels of Fzo1 upon deletion of UBP12 and/or mutation of CDC48. Crude mitochondrial extracts from the indicated strains additionally expressing HA-Fzo1, or the corresponding empty vector, were analyzed by SDS-PAGE and immunoblotting using an HA-specific antibody. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in Figure 1B. Bottom panel, quantification of four independent experiments, normalized to PoS and including SD. ns, p>0.05. *, p≤0.05, **, p≤0.01 (One-way ANOVA, Tukey’s multiple comparison test). PoS, PonceauS staining.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Mitochondrial morphology upon deletion of UBP12 in Δfzo1 cells. The indicated mutant cells were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Quantification from three different experiments (with more than 200 cells each), including SD, as described (Cumming et al., 2007). (B) Mitochondrial morphology upon expression of HA-Fzo1 in Δfzo1 Δubp12 cells. The indicated mutant cells were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Quantification from three different experiments (with more than 200 cells each), including SD, as described (Cumming et al., 2007). (C) Mitochondrial morphology upon endogenous expression of HA-Fzo1 or HA-Fzo1K464R in Δubp12 cells. The indicated mutant cells were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Quantification from one experiment (with more than 200 cells each). (D) Mitochondrial morphology upon deletion of UBP12 in Δfzo1 Δdnm1 cells. The indicated mutant cells were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Quantification from three different experiments (with more than 200 cells each), including SD, as described (Cumming et al., 2007).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Analysis of mtDNA content in cdc48-2 cells using RT-PCR. mtDNA content in Δfzo1, wt and cdc48-2 cells was analyzed by measuring COX3 and ACT1 (as housekeeping gene) RNA levels using RT-PCR. Quantification of six independent experiments, including SD. *p≤0.05 (paired t-test). (B) Analysis of mtDNA content in cdc48-2 cells using the Cox2 protein amount. Total cellular extracts of Δfzo1, wt and cdc48-2 cells were analyzed by SDS-PAGE and immunoblotting using Cox2- (as mtDNA marker) or Ubc6-specific antibodies. Bottom panel, quantification of five independent experiments, including SD. *p≤0.05 (paired t-test). (C) Respiratory capacity of cdc48-2 cells upon expression of wt or mutant Cdc48. A spot assay was performed as described in Figure 4B with the indicated cells but using YPLac, grown at 30°C for 1 day and at 37°C for 3 days. (D) Physical interaction between Cdc48 and Fzo1 in Δubp12 cells. HA-Fzo1 or the corresponding empty vector was expressed in wt or Δubp12 cells and analyzed for Cdc48 interaction, as in 2A. Crude mitochondrial extracts were lysed, HA tagged Fzo1 was precipitated using HA-coupled beads, and the eluate was analyzed by SDS-PAGE and immunoblotting using HA- and Cdc48-specific antibodies. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in Figure 1B. (E) Steady state levels of Fzo1 upon deletion of UBP2 and/or mutation of CDC48. Total cellular extracts of wt cells or Δubp12, cdc48-2 and Δubp12 cdc48-2 mutant cells were analyzed by SDS-PAGE and immunoblotting using HA-, Ubc6- and Tom40-specific antibodies. Bottom panel, quantification of six independent experiments, including SD. ns, p>0.05 (One-way ANOVA; Tukey’s multiple comparison test). PoS, Ponceau S staining; IP, immunoprecipitation; WB, western blot.

### Ubp12 mediates deubiquitylation of Ubp2

We noticed that increased levels of Fzo1, present in ∆ubp12 cells, specifically depended on Ubp2 (Figure 5A). Therefore, Ubp12 and Ubp2, which affect the stability of Fzo1 in opposite manners, are also interdependent. Next, we analyzed if Ubp2 and Ubp12 also presented other opposing and interdependent phenotypes related to ubiquitin. First, we analyzed cellular growth of cells lacking UBP2, UBP12 or both, in the presence of sub-lethal doses of CHX, a phenotype commonly tested to monitor imbalances in ubiquitin homeostasis (Gerlinger et al., 1997; Hanna et al., 2003; Rumpf and Jentsch, 2006). Second, we directly quantified the levels of free ubiquitin vs. substrate-conjugated ubiquitin in the same strains. We observed that indeed Ubp2 and Ubp12 had opposite phenotypes (Figure 5—figure supplement 1). In addition, the consistent interdependence of these two enzymes suggested a DUB hierarchy, which prompted us to test a possible regulation of the Ubp2 protein by Ubp12. We tested if Ubp2 is an unstable protein and whether Ubp12 is involved in its degradation, after inhibition of protein synthesis with CHX. The levels of genomically tagged Ubp2 decreased over time and Ubp2-turnover was regulated by Ubp12 (Figure 5B) and by the proteasome (Figure 5—figure supplement 2A). Moreover, co-immunoprecipitation experiments revealed that Ubp2 interacted with Ubp12, suggesting a direct regulation between both DUBs (Figure 5—figure supplement 2B). We therefore investigated if Ubp2 could be ubiquitylated, in a Ubp12-dependent manner. After immunoprecipitation of Ubp2-Flag, and consistent with recent observations (Cavellini et al., 2017), we observed the presence of slowly migrating forms of Ubp2 during electrophoresis, in wt cells (Figure 5—figure supplement 2C) but mostly in Δubp12 cells (Figure 5C, left panel). Importantly, we show that these forms could also be detected using a ubiquitin-specific antibody, demonstrating that they represent ubiquitylated Ubp2 (Figure 5C and Figure 5—figure supplement 2C, right panels). This indicates that Ubp12 mediates deubiquitylation of Ubp2 and suggests that Ubp2 acts downstream of Ubp12, thus revealing a hierarchical cascade between DUBs, of relevance for the protein levels of Fzo1 and for ubiquitin homeostasis.

![Figure 5.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig5-v2.jpg)

**Figure 5.:** (A) Interdependent role of Ubp2 and Ubp12 for the steady state levels of Fzo1. Total cellular extracts of wt or Δubp2, Δubp12, and Δubp2 Δubp12 mutant cells expressing HA-Fzo1 and also expressing either Ubp2-Flag or the corresponding empty vector, as indicated, were analyzed by SDS-PAGE and immunoblotting using HA- and Tom40-specific antibodies. Bottom panel, quantification of four independent experiments, including SD. (B) Turnover of endogenous Ubp2 in wt or Δubp12 cells. The turnover of endogenously 3xHA-tagged Ubp2 (Ubp2-3xHAint) was assessed as in 3A. Samples were analyzed by SDS-PAGE and immunoblotting using antibodies against HA, Ubc6 and Ssc1. Right panel, quantification of four independent experiments, including SD. For the statistical analysis of the degradation kinetics of each strain, a paired t-test was used; for the statistical analysis of the difference in steady state levels of both strains at the indicated time points (t1h, t3h) an unpaired t-test was used. ns, p>0.05; *, p≤0.05; **, p≤0.01. (C) Ubiquitylation of Ubp2. The Ubp2C745S-Flag inactive variant, expressed in wt or Δubp12 cells, was immunoprecipitated from total soluble extracts using Flag-coupled beads. Eluted Ubp2 was analyzed by western blot using Flag- or ubiquitin (Ub - P4D1)-specific antibodies. Ubiquitylated forms of Ubp2C745S-Flag are labeled with Ub. PoS, Ponceau S staining; IP, immunoprecipitation; WB, western blot.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Opposing roles of Ubp2 and Ubp12 for CHX resistance. A spot assay was performed, as described in Figure 4B, but on synthetic media supplemented with glucose (SCD) in the absence or presence of 0.5 µg/ml CHX and incubated at 30°C for one or five days, respectively. (B) Distinct roles of Ubp2 and Ubp12 for cellular ubiquitylation. Total cellular extracts of the indicated strains were analyzed by SDS-PAGE and immunoblotting using ubiquitin (Ub; αP4D1) and Tpi1-specific antibodies, used as loading control. Free ubiquitin or ubiquitylated conjugates are labeled with Ub. Right panels, quantification of three independent experiments showing the levels of free Ub or Ub conjugates, including SD.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Proteasome dependence of Ubp2-Flag degradation in Δpdr5 Δsnq2 mutant cells. The turnover of ectopically expressed Ubp2-Flag was assessed as in Figure 1D. Samples were analyzed by SDS-PAGE and immunoblotting using Flag- and Ubc6-specific antibodies. (B) Physical interaction between Ubp2 and Ubp12. Catalytically inactive variants ectopically expressed Ubp2C745S-Flag and non-tagged Ubp12C372S, or their corresponding empty vectors, were expressed in Δubp2 Δubp12 cells. Total soluble extracts were prepared and Ubp12C372S was precipitated using Sepharose beads in the presence or absence of a Ubp12-specific antibody, as indicated. The eluates were analyzed by SDS-PAGE and immunoblotting using Flag- and Ubp12-specific antibodies. (C) Ubiquitylation of Ubp2. The Ubp2C745S-Flag inactive variant, expressed in wt, Δubp12 and Δubp12Δmdm30 cells, was immunoprecipitated from total soluble extracts using Flag-coupled beads. Eluted Ubp2 was analyzed by western blot using antibodies specific for Flag or ubiquitin (Ub; αP4D1). Ubiquitylated forms of Ubp2C745S-Flag are labeled with Ub. PoS, PonceauS staining; IP, immunoprecipitation; WB, western blot.

### Ubp12 recognizes short K48-linked ubiquitin chains on Fzo1

In contrast to numerous proteins that are destabilized in absence of DUBs, deletion of UBP12 stabilizes Fzo1 (Figure 6—figure supplement 1) and Ubp2 (Figure 5B). Consistently, the two other known substrates of Ubp12 – Rad23 (Gödderz et al., 2017) and Gpa1 (Wang et al., 2005) are also not destabilized in Δubp12 cells. To characterize the deubiquitylation reaction of Ubp12 in more detail, we analyzed the ubiquitin linkages on Fzo1 and Ubp2 accumulating in Δubp12 cells. Overexpression of ubiquitin mutated in K48R strongly decreased Fzo1 and Ubp2 ubiquitylation, revealing that their ubiquitin chains are linked via K48 (Figure 6A and C). However, the ubiquitin chains on Fzo1 that destabilize it and inhibit fusion, which are not bound by Ubp12, are also K48-linked (Figure 6B) (Anton et al., 2013). Thus, differences in ubiquitin chains cannot explain why Ubp12 stabilizes its substrates. To further analyze Ubp12, its ubiquitin chain preference was tested using in vitro deubiquitylation assays (Hospenthal et al., 2015). As a substrate, we used either K48-linked or K63-linked ubiquitin, present in the form of either di-ubiquitin (Figure 6D) or ubiquitin chains (Figure 6E). However, in all cases, Ubp12 revealed no chain preference (Figure 6D,E). This suggested that it is not Ubp12 but rather the chains themselves on the substrates that prevent their turnover. Thus, we determined the number of ubiquitin moieties present on Fzo1, upon co-expression of tagged and non-tagged ubiquitin molecules. We observed that co-expression of ubiquitin and Myc-ubiquitin decomposed the first ubiquitylated form of Fzo1, i.e running closest to non-modified Fzo1, into two bands (Figure 6F). This corresponds to the presence of either ubiquitin or Myc-ubiquitin attached to Fzo1 and confirms that this form corresponds to mono-ubiquitylated Fzo1. Interestingly, however, for the two other ubiquitylated forms with lower electrophoretic mobility, we observed that only two additional bands could be observed above each of them. They correspond to either the presence of two Myc-ubiquitin molecules or one ubiquitin and one Myc-ubiquitin conjugated to Fzo1. These results suggest that the K48 chains on Fzo1 consist of two ubiquitin moieties. In conclusion, Ubp12 recognizes ubiquitylated chains on Fzo1 composed of a very small number of ubiquitin moieties. We therefore propose that Ubp12 does not stabilize its substrates because their ubiquitin chains are too short to target proteasomal turnover.

![Figure 6.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig6-v2.jpg)

**Figure 6.:** (A) Analysis of ubiquitin chain-type composition of Fzo1. Crude mitochondrial extracts from wt or Δubp12 mutant cells expressing HA-Fzo1, and over-expressing either wt ubiquitin (Ub) or ubiquitin with a K48R mutation (UbK48R), were solubilized, subjected to HA-immunoprecipitation and analyzed by SDS-PAGE and immunoblotting using an HA-specific antibody. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in 1B. (B) Ubiquitin chain-type analysis of Fzo1 upon Ubp2C745S expression. Crude mitochondrial extracts from wt or Δubp2 (expressing Ubp2C745S) cells expressing HA-Fzo1 endogenously, and overexpressing either wt ubiquitin (Ub) or UbK48R, were analyzed as in A. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in 2B (C) Analysis of Ubp2 ubiquitin chain composition in Δubp12 cells. Soluble extracts from Δubp12 cells expressing Ubp2C745S-Flag and different ubiquitin variants (as indicated) were prepared and Flag-tagged Ubp2C745S was precipitated using Flag-coupled beads. The eluate was analyzed by SDS-PAGE and immunoblotting using antibodies against Flag and ubiquitin (Ub; αP4D1). (D) Deubiquitylation (DUB) assay using Ub2 chains. Purified di-ubiquitin chains (Ub2) composed of either only K48- or K63-linkages were treated with the purified DUBs Ubp12, USP21 and USP2. Treated chains were analyzed by SDS-PAGE and immunoblotting using a ubiquitin-specific antibody (Ub; αP4D1). Mono-ubiquitin or di-ubiquitin chains are labeled with Ub1 or Ub2, respectively. (E) DUB assay using Ub-chains. Purified poly-ubiquitin chains (Ub-chains) composed of either only K48- or K63-linkages were treated with the purified DUBs Ubp12, USP21 or USP2. Treated chains were analyzed by SDS-PAGE and immunoblotting as in C. Ubiquitin chains were labeled as in D with the subscript value indicating the amount of ubiquitin moieties in the respective chain. (F) Ubiquitylation pattern of Fzo1. Wt cells expressing HA-Fzo1 were analyzed for Fzo1 ubiquitylation upon the expression of Myc-ubiquitin, or the respective empty vector. HA-Fzo1 was immunoprecipitated from mitochondrial extracts using HA-coupled beads. Eluted Fzo1 was split into two and samples were analyzed by SDS-PAGE and immunoblotting using HA- or Myc-specific antibodies. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in 1B. The composition of the additional species apparent upon co-expression of Myc-tagged ubiquitin is explained in the inset. PoS, PonceauS staining.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Opposite effects of Ubp12 and Ubp2 in Fzo1 stability. The turnover of HA-Fzo1 in wt, Δubp12, Δubp2 or Δubp12 Δubp2 cells was assessed after inhibition of cytosolic protein synthesis with cycloheximide (CHX), for the indicated time points in exponentially growing cultures. Samples were analyzed by SDS-PAGE and immunoblotting using a HA- and Hsp70-specific antibodies. Left panel, quantification of three independent experiments, including SD.

### Ubp12-Ubp2 cascade activity impinges on Fzo1 ubiquitylation

Both Ubp12 and Ubp2 deubiquitylate Fzo1, but they clearly bind different forms of ubiquitylated Fzo1 (Anton et al., 2013). Ubp12 binds ubiquitylated forms of Fzo1 that stabilize Fzo1 and promote mitochondrial fusion. In turn, Ubp2 recognizes other ubiquitylated forms of Fzo1, that instead signal Fzo1 turnover thus preventing mitochondrial fusion. Given that Ubp12 acts upstream of Ubp2, we speculated that the pro-fusion ubiquitylated forms of Fzo1, Ubp12-specific, would also precede its Ubp2-specific anti-fusion forms. This predicts an impairment of anti-fusion forms in the absence of pro-fusion forms. Therefore, as previously, the mutant Fzo1K464R was chosen as a tool, because it loses the pro-fusion ubiquitylation (Figure 7A, inset, black arrows, compare lanes 1 and 2). Moreover, as in Figure 2B, the catalytically-inactive Ubp2C745S protein was expressed additionally. This allows visualization of the Ubp2-specific anti-fusion forms as well (Figure 7A, inset, red arrows, lane 3), resulting in a massive increase in overall ubiquitylation of Fzo1 (compare lanes 1 and 3). As predicted by our hypothesis, much of this increase was lost when K464 was mutated to R (compare lanes 3 and 4). This shows that Ubp2-dependent ubiquitylation largely requires previous K464-dependent ubiquitylation . Therefore, pro-fusion ubiquitylation, which stabilizes Fzo1, primes Fzo1 for the formation of anti-fusion ubiquitylation. These anti-fusion forms, instead, signal Fzo1 for proteasomal degradation, so that in Δubp2 cells Fzo1 is less abundant (Anton et al., 2013). Taking this into consideration, the steady state levels of Fzo1 were used as a read-out for the presence of anti-fusion ubiquitylation on Fzo1. We noticed that whereas the steady state levels of Fzo1 decreased by 91% inΔubp2 cells, as expected, the steady state levels of Fzo1K464R only decreased by 47% (Figure 7B). This shows that Fzo1K464R is much less sensitive to the deletion of UBP2 than wt Fzo1, consistent with a lower abundance of the anti-fusion ubiquitylation. To confirm this result, the levels of Fzo1 were also tested upon further deletion of MDM30 inΔubp2 cells, which encodes the E3 ligase-component responsible for pro-fusion ubiquitylation on Fzo1 (Cohen et al., 2008; Escobar-Henriques et al., 2006; Fritz et al., 2003). Indeed, we could observe a rescue of Fzo1 steady state levels inΔubp2 Δmdm30 cells, confirming that pro-fusion precedes anti-fusion ubiquitylation on Fzo1 (Figure 7C). We conclude that Ubp2-specific ubiquitylation of Fzo1 largely depends on Ubp12-specific ubiquitylation of Fzo1, indicating a regulatory cascade of Ubp12 and Ubp2 on Fzo1.

![Figure 7.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig7-v2.jpg)

**Figure 7.:** (A) Effect of Ubp2C745S on Fzo1K464R ubiquitylation. HA-Fzo1 or HA-Fzo1K464R were expressed in the presence of Ubp2 (∆fzo1 cells plus empty vector) or instead in the presence of Ubp2C745S (∆ubp2 ∆fzo1 plus Ubp2C745S-Flag), as indicated. Crude mitochondrial extracts were solubilized and HA-tagged Fzo1 was analyzed by SDS-PAGE and immunoblotting using an HA-specific antibody. Unmodified and ubiquitylated forms of HA-Fzo1 are indicated as in 2B. (B) Effect of UBP2 deletion on the steady state levels of Fzo1K464R. Total cellular extracts of indicated strains expressing HA-Fzo1 or HA-Fzo1K464R as indicated were analyzed by SDS-PAGE and immunoblotting using HA- and Tom40-specific antibodies. Bottom panel, quantification of five independent experiments, including SD. (C) Effect of Ubp2 and Mdm30 on the steady state levels of Fzo1. Total cellular extracts of wt, Δubp2 and Δubp2 Δmdm30 cells expressing HA-tagged Fzo1 endogenously (HA-Fzo1int) were analyzed by SDS-PAGE and immunoblotting using HA- and Tom40-specific antibodies. Bottom panel, quantification of three independent experiments, including SD. PoS, Ponceau S staining.

### Cdc48 mitochondrial phenotypes depend on Ubp2

To challenge the Cdc48-DUBs regulatory cascade, we first tested if the role of Cdc48 on Fzo1 steady state levels depended on Ubp2 and Ubp12. Indeed, and in contrast to wt cells, in ∆ubp2 ∆ubp12 cells the steady state levels of Fzo1 were insensitive to further mutating Cdc48 (Figure 8A). Moreover, ∆ubp2 cells and ∆ubp2 ∆ubp12 were similarly insensitive to the presence of the cdc48-2 allele (Figure 8B), consistent with the UBP2 UBP12 epistasis results (Figure 5A and Figure 5—figure supplement 1A and B). Next, we tested if overexpression of Ubp2 could rescue cdc48-2 phenotypes. This was to be expected because deletion of UBP12 rescues CDC48 mutant phenotypes but also leads to increased levels of Ubp2. Consistently, mitochondrial tubulation was significantly improved under these conditions (Figure 8C). Moreover, Ubp2 overexpression improved the growth defect of cdc48-2 cells on lactate media at the non-permissive temperature of 37°C, supporting the physiological impact of the Ubp2 levels in cdc48-2 cells (Figure 8D). Therefore, the respiratory capacity of the cdc48-2 cells could be improved not only by UBP12 deletion but also by overexpression of Ubp2. Finally, a physical interaction between Ubp2 and Cdc48 could be observed (Figure 8—figure supplement 1). Together our results highlight a model in which Cdc48, Ubp12 and Ubp2 orchestrate a multilayered cascade regulation, culminating on Fzo1 ubiquitylation and mitochondrial fusion.

![Figure 8.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig8-v2.jpg)

**Figure 8.:** (A) Steady state levels of Fzo1 in Δubp2 Δubp12 upon mutation of CDC48. Total cellular extracts of wt, cdc48-2, Δubp2 Δubp12 and Δubp2 Δubp12 cdc48-2 cells were analyzed by SDS-PAGE and immunoblotting using Fzo1- and Tom40-specific antibodies. Bottom panel, quantification of five independent experiments, including SD. (B) Steady state levels of Fzo1 in Δubp2 cells upon deletion of CDC48. Total cellular extracts of wt, cdc48-2, Δubp2 and Δubp2 cdc48-2 cells were analyzed by SDS-PAGE and immunoblotting using Fzo1- and Tom40-specific antibodies. Bottom panel, quantification of five independent experiments, including SD. (C) Mitochondrial morphology of cdc48-2 cells upon overexpression of Ubp2. Wt or cdc48-2 mutant cells expressing Ubp2 or the corresponding empty vector were analyzed for mitochondrial tubulation after expressing a mitochondrial-targeted GFP plasmid, as in Figure 1A. Quantification from three different experiments (with more than 200 cells each), including SE, as described (Cumming et al., 2007). ns, p>0.05. **p≤0.01, ***p≤0.001 (One-way ANOVA, Tukey’s multiple comparison test). (D) Role of Ubp2 overexpression on the respiratory capacity of CDC48-deficient cells. A spot assay was performed as described in Figure 4B with the indicated cells but using synthetic media supplemented with lactate (SCLac) and incubated for 4 days. PoS, Ponceau S staining.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** Physical interaction between Ubp2 and Cdc48. The catalytically inactive variant Ubp2C745S-Flag or the corresponding empty vector were expressed in Δubp12 cells and analyzed for Cdc48 interaction, as in 2A. Crude mitochondrial extracts were lysed and Flag-tagged Ubp2C745S was precipitated using Flag-coupled beads. The eluate was analyzed by SDS-PAGE and immunoblotting using Flag- and Cdc48-specific antibodies. PoS, Ponceau S staining; IP, immunoprecipitation; WB, western blot.

## Discussion

Precise regulation of cellular processes by protein ubiquitylation requires a tight control of the enzymes involved. We reveal a new mode of DUB regulation by Cdc48 for Fzo1 and mitochondrial fusion (Figure 9). This is likely of broader relevance for the regulation of DUBs and ubiquitin homeostasis.

![Figure 9.](https://cdn.elifesciences.org/articles/30015/elife-30015-fig9-v2.jpg)

**Figure 9.:** Cdc48 supports turnover of Ubp12, stabilizing ubiquitylation on Fzo1 that promotes mitochondrial fusion (green ubiquitins). Moreover, degradation of Ubp12 stabilizes Ubp2, facilitating the removal of ubiquitin chains on Fzo1 inhibiting mitochondrial fusion (red ubiquitins). Thereby, Cdc48 activates mitochondrial fusion via Ubp12 and Ubp2. In contrast, Cdc48 impairment blocks progression of mitochondrial fusion by actively preventing Ubp12 turnover. Ubp12 then leads to a cascade of events inhibiting mitochondrial fusion: A) removal of the pro-fusion ubiquitylated forms and B) inhibition of Ubp2, consequently leading to the accumulation of the anti-fusion ubiquitylated forms. This cascade allows a synergistic effect of Cdc48, via a DUB regulatory cascade, to effectively promote or inhibit mitochondrial fusion.

### Synergistic function of Cdc48 in Fzo1 ubiquitylation

Cdc48 promotes degradation of Ubp12, controlling Fzo1 ubiquitylation. Ubp12 prevents mitochondrial fusion by two means. On the one hand, it removes the ubiquitylation on Fzo1 that is required for fusion. On the other hand, it promotes degradation of Ubp2. This leaves the anti-fusion ubiquitylation of Fzo1 unopposed, resulting in Fzo1 degradation. Therefore, by supporting turnover of Ubp12, Cdc48 dually preserves mitochondrial fusion events. In contrast, when only a non-functional variant of the protein is present, as is the case in cdc48-2 cells, Cdc48 cannot protect the pro-fusion ubiquitylation of Fzo1. In this case, the cascade will synergistically converge in degradation of Fzo1 and thus inhibition of mitochondrial fusion will occur. The interdependence between these two pathways contributes to a coordinated cellular decision by Cdc48 to either fuse mitochondria or instead prevent it by degrading Fzo1. Moreover, the Cdc48-Ubp12-Ubp2 cascade allows fine-tuning of substrate ubiquitylation and modulation of the biological processes thereof, as exemplified for Fzo1 and mitochondrial fusion (Figure 9).

### Roles of Cdc48 on mitochondrial dynamics

Cdc48/p97 extracts ubiquitylated substrates from membranes, thus allowing their recognition and degradation by the proteasome (Franz et al., 2014; Rape et al., 2001). This is exemplified with the ER protein Ubc6, and was also shown for mitochondrial OM proteins (Neutzner et al., 2007), including mitofusins under damaging conditions (Tanaka et al., 2010). Therefore, Cdc48/p97 and ubiquitin regulate mitochondrial fusion in both yeast and mammals. Moreover, eukaryotes present a similar ubiquitin pattern of mitofusins, suggesting that the new function of Cdc48 presented here could be conserved in mammals under non-damaging conditions.

### Critical role of the DUB cascade for mitochondrial fusion

Mitochondrial fusion is a complex multistep process dependent on sequential events involving GTP binding and hydrolysis by Fzo1, Fzo1 oligomerization and finally ubiquitylation of Fzo1 (Anton et al., 2011; Brandt et al., 2016; Cohen et al., 2011; Ishihara et al., 2004). Although it is clear that ubiquitin critically determines mitochondrial fusion events, the underlying mechanisms are largely unknown (Anton et al., 2013). The DUBs Ubp12 and Ubp2 cleave different ubiquitylated forms of Fzo1 that either promote or repress mitochondrial fusion, respectively (Anton et al., 2013). Here, given that Ubp12 regulates Ubp2, we show that these two ubiquitylation pathways are connected. Consistently, on Fzo1, Ubp12-specific ubiquitylation also precedes Ubp2-specific ubiquitylation. In fact, unopposed anti-fusion ubiquitylation, as it is the case in Δubp2 cells, disrupts mitochondrial tubulation. This renders the role of Ubp2 in mitochondrial dynamics quite clear, namely protecting mitochondrial fusion. In contrast, the need for a dedicated DUB that removes the pro-fusion ubiquitylation forms, i.e. the need for Ubp12, remained unclear. Now, the Ubp12-Ubp2 cascade allows to understand the purpose of Ubp12, solving the paradox of why inhibition of the pro-fusion ubiquitylation on Fzo1 is required: in fact, too much pro-fusion ubiquitylation also means too much anti-fusion ubiquitylation, a problem counteracted by the deubiquitylation activity of Ubp12 on Fzo1. We conclude that this cascade ensures a tight control of Fzo1 ubiquitylation at levels sufficient to allow mitochondrial fusion but preventing unnecessary ubiquitylation that instead targets Fzo1 for proteasomal turnover.

### Which E3 ligases and DUBs modify Fzo1?

The cascade between Ubp12 and Ubp2 also allows revising recent results linking Ubp2 and Mdm30 (Cavellini et al., 2017). Mdm30 catalyzes the formation of the pro-fusion ubiquitin forms on Fzo1 (Cohen et al., 2008). The pro-fusion forms are bound and cleaved by Ubp12, depend on lysine 464 of Fzo1, and are essential for mitochondrial fusion (Anton et al., 2013). As to the anti-fusion ubiquitin forms on Fzo1, two types could now be observed: low molecular weight, K464-independent, anti-fusion ubiquitylation (as seen in Figure 7A, lane 4), consistent with previous results (Anton et al., 2013), but mostly high molecular weight anti-fusion ubiquitylation, instead K464-dependent (as seen in Figure 7A, lane 3). This shows that the anti-fusion ubiquitin forms on Fzo1 largely depend on its pro-fusion forms. Therefore, it is not surprising that anti-fusion, Ubp2-specific, ubiquitylation on Fzo1 also largely depends on Mdm30. Nevertheless, future studies are required to clarify if Mdm30 itself catalyzes the formation of this high molecular weight fraction of the anti-fusion ubiquitylation on Fzo1. Moreover, it is clear that Mdm30 is not the ligase responsible for the anti-fusion low molecular weight forms on Fzo1 (Anton et al., 2013), which therefore remains to be identified.

### Novel DUB cascade controlling ubiquitin homeostasis

Our results unravel for the first time a regulatory cascade of two DUBs, Ubp12 and Ubp2, with opposing functions in ubiquitin homeostasis. A 20–40% depletion in ubiquitin levels leads to cellular growth defects under various stress conditions in yeast, to lethality or infertility in mice, and to neurological diseases like ataxia, gracile axonal dystrophy or Parkinson’s disease (Kimura and Tanaka, 2010; Park and Ryu, 2014). The level of free ubiquitin is adjusted to the cellular needs, and is critically regulated by deubiquitylase activity (Chernova et al., 2003; Swaminathan et al., 1999). Here, we reveal distinct roles of two DUBs - Ubp2 and Ubp12 - for the maintenance of ubiquitin homeostasis. Δubp12 cells are hyperresistant to cycloheximide (CHX), a chemical inhibitor of protein translation. Similar observations were previously reported in proteasome mutants, with impaired proteolysis (Gerlinger et al., 1997). Consistently, just like proteasome mutants, also Δubp12 cells accumulate conjugated ubiquitin, without affecting the levels of free ubiquitin. In turn, Δubp2 cells showed a 40% depletion of free ubiquitin and hypersensitivity to CHX, consistent with similar observations in strains presenting decreased free ubiquitin levels (Hanna et al., 2003). Nevertheless, along with reduced free ubiquitin, deletion of UBP2 also clearly led to increased levels of ubiquitin conjugates, as observed upon DmUsp5 depletion in the fruit fly (Kovács et al., 2015). In fact, the importance of free ubiquitin pools versus ubiquitin conjugates for cellular growth is not well understood. Our analysis of Δubp2 cells sheds light on this question, demonstrating that depletion of free ubiquitin is epistatic over the accumulation of ubiquitylated conjugates for cellular growth.

### Differences in DUB behavior

What could justify the opposite behavior of Ubp2 and Ubp12 in ubiquitin homeostasis and substrate turnover? The removal of ubiquitin from a substrate is generally expected to increase its stability, as observed for Fzo1 in Δubp2 cells. Consistently, Ubp2 appears as a general quality control deubiquitylase recognizing both K48- and K63-linked ubiquitin chains that signal for turnover, both by the UPS and by the lysosome (Anton et al., 2013; Fang et al., 2016; Ho et al., 2017; Silva et al., 2015). In contrast, the turnover of both Fzo1 and Ubp2 is decreased in Δubp12 cells. Moreover, Ubp12 does not stabilize Rad23 (Gödderz et al., 2017) and Gpa1 (Wang et al., 2005), i.e. its two other known substrates. Ubp12 exhibits a broad substrate specificity in vitro recognizing both K48- and K63-linked chains, consistent with previous observations (Schaefer and Morgan, 2011). Thus, it is not Ubp12 but the substrate that behaves unexpectedly. Notably, the ubiquitin signals that accumulate in Fzo1, Ubp2, Rad23 and Gpa1 are all composed of a limited number of discrete bands, instead of the high molecular weight smear, typical for polyubiquitylated substrates. For Fzo1, we find that Ubp12 recognizes ubiquitylated forms that only contain two ubiquitin moieties that are linked via K48. We propose that the presence of a short number of ubiquitin molecules on the ubiquitin chains recognized by Ubp12 could explain why they do not serve as a good signal for proteasomal degradation. The protein Met4 was also shown to be ubiquitylated with a a limited number of discrete bands (Flick et al., 2004; Kuras et al., 2002). In this case, intramolecular association with a ubiquitin binding domain in Met4 shields the ubiquitin chains, thus preventing their elongation and protecting Met4 against proteasomal degradation (Flick et al., 2006; Tyrrell et al., 2010).

### Regulation of DUB activity by ubiquitin

How deubiquitylation is controlled is poorly understood. Our findings suggest that this involves ubiquitylation of the DUBs themselves, because both Ubp2 and Ubp12 are regulated by ubiquitylation. This consequently renders DUBs interdependent, as exemplified with Ubp12 being the DUB of Ubp2. Interestingly, several examples in the literature illustrate a big diversity of DUB regulation (Michel et al., 2017). Therefore, additional mechanisms to proteolysis for the atypical function of Ubp2 ubiquitylation can be proposed. For example, Ubp2 ubiquitylation could induce a conformational change favouring catalytic activity, as observed for the DUB ATXN3 (Todi et al., 2010). This is supported by the observation that Ubp2 is among the largest yeast DUBs. In addition, several residues of Ubp2 were found to be phosphorylated (Swaney et al., 2013), suggesting that coordinated ubiquitylation/phosphorylation events could increase its activity. Finally, given that many DUBs often act as part of protein complexes, Ubp2 ubiquitylation could favor its interaction with Ubp12 and/or Cdc48. This could release autoinhibition by a conformational change, as observed for the DUB Ubp6 upon binding to the proteasome, i.e. a AAA+ ATPase like Cdc48 (Hanna et al., 2006). In fact, Cdc48 has been shown to associate with several DUBs (Ossareh-Nazari et al., 2010; Papadopoulos et al., 2017; Rumpf and Jentsch, 2006; Uchiyama et al., 2002) but also recognizes ubiquitylated proteins, consistent with its interaction with both Ubp12 and Ubp2. Therefore, DUB ubiquitylation could allow recruitment of Cdc48 and provide a platform guiding DUBs to their relevant substrates. This would also justify the need for Fzo1-Cdc48 physical interaction. In fact, a local regulation of Fzo1 by Cdc48 could allow increased efficiency of the Cdc48-DUB cascade on Fzo1 regulation.

In conclusion, our results suggest that Cdc48 serves as a binding platform allowing cross-talk regulation between DUBs, bringing new insights into the knowledge of ubiquitin biology. These general findings open new perspectives to address some poorly understood questions, e.g. how Cdc48 regulates homotypic fusion events and how DUBs are interdependently regulated, possibly accounting for the multitude of DUBs present in a cell.

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
      <td>strain (Saccharomyces cerevisiae)</td>
      <td>∆fzo1</td>
      <td>PMID: 9483801</td>
      <td>Escobar_lab_stock_number: FA2</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-1</td>
      <td>PMID: 21441928</td>
      <td>Escobar_lab_stock_number: FA230</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-2</td>
      <td>PMID: 21441928</td>
      <td>Escobar_lab_stock_number: FA231</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-3</td>
      <td>PMID: 21441928</td>
      <td>Escobar_lab_stock_number: FA232</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆ubp2</td>
      <td>PMID: 9483801</td>
      <td>Escobar_lab_stock_number: FA260</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆ubp12</td>
      <td>PMID: 9483801</td>
      <td>Escobar_lab_stock_number: FA269</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆fzo1 ∆ubp2</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: FA362</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆ubp2 ∆ubp12</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: FA382</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆ubp12 ∆mdm30</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: FA390</td>
      <td>UBP12::kanMX4; MDM30::kanMX4;obtained by crossing</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>HA-Fzo1int in wt</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: FA407</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>HA-Fzo1int in ∆ubp2</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: FA415</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>HA-Fzo1int in ∆ubp2 ∆mdm30</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: FA427</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆fzo1 ∆ubp12</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: FA432</td>
      <td>FZO1::kanMX4; UBP12::kanMX4;obtained by crossing</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>HA-Fzo1-K464Rint in wt</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: FA451</td>
      <td>HA-Fzo1K464R genomically integrated with NatNT2 into RS140</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>wt (BY4741)</td>
      <td>PMID: 9483801</td>
      <td>Escobar_lab_stock_number: RS140</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-2 ∆fzo1</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS430</td>
      <td>FZO1::natNT2 in FA231</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-2 ∆ubp12</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS466</td>
      <td>FZO1::hphNT1 in FA231</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-2 ∆ubp2 ∆ubp12</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS499</td>
      <td>UBP12::natNT2; UBP2::hphNT1 in FA231</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆doa1</td>
      <td>PMID: 9483801</td>
      <td>Escobar_lab_stock_number: RS518</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆pdr5 ∆snq2</td>
      <td>other</td>
      <td>Escobar_lab_stock_number: RS527</td>
      <td>gift by J. Dohmen (YGA58): MATa, ADE2 his3-D200 leu2-3,112 lys2-801, trp1D63 ura3-52 PDR5::hphNT1 SNQ2::kanMX4</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>Ubp12-Flagint in cdc48-2</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS546</td>
      <td>Ubp12-Flag genomically integrated with NatNT2 into FA231</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>Ubp12-Flagint in wt</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS547</td>
      <td>Ubp12-Flag genomically integrated with NatNT2 into BY4741</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆pdr5 ∆snq2</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS554</td>
      <td>PDR5::NatNT2; SNQ2::hphNT1 in RS140</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆fzo1 ∆dnm1 ∆ubp12</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS556</td>
      <td>UBP12::NatNT2 in TS1028</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆pdr5 ∆snq2 cdc48-2</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: RS559</td>
      <td>PDR5::NatNT2; SNQ2::hphNT1 in FA231</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>cdc48-2 ∆ubp2</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: TS686</td>
      <td>UBP2::hphNT1 in FA231</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>∆fzo1 ∆dnm1</td>
      <td>other</td>
      <td>Escobar_lab_stock_number: TS1028</td>
      <td>gift by B. Westermann (SB95): FZO1::kanMX4; DNM1::kanMX4; obtained by crossing</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>wt (DF5)</td>
      <td>PMID: 11007476</td>
      <td>Escobar_lab_stock_number: TS1124</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>ufd1-2</td>
      <td>PMID: 11847109</td>
      <td>Escobar_lab_stock_number: TS1125</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>npl4-1</td>
      <td>PMID: 8930904</td>
      <td>Escobar_lab_stock_number: TS1126</td>
      <td></td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>Ubp2-9Mycint in wt</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: TS1134</td>
      <td>Ubp2-9Myc genomically integrated with NatNT2 into RS140</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>Ubp2-3HAint in wt</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: TS1144</td>
      <td>Ubp2-3HA genomically integrated with hphNT1 in RS140</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>Ubp2-3HAint in ∆ubp12</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: TS1147</td>
      <td>Ubp2-3HA genomically integrated with hphNT1 in FA269</td>
    </tr>
    <tr>
      <td>strain (S. cerevisiae)</td>
      <td>pGAL-Ubp12-Flagint in wt</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: TS1153</td>
      <td>pGAL-Ubp12-Flag genomically integratedwith kanMX4 into RS544</td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>pRS316 (plasmid)</td>
      <td>PMID: 2659436</td>
      <td>Escobar_lab_stock_number: p8</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>HA-Fzo1 on pRS316 (plasmid)</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: p10</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>HA-Fzo1-K464R on pRS316 (plasmid)</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: p14</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>YEplac181 (plasmid)</td>
      <td>PMID: 3073106</td>
      <td>Escobar_lab_stock_number: p58</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ubp2-Flag on YEplac181(plasmid)</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: p59</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ubp2-C745S-Flag on YEplac181(plasmid)</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: p60</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ubp12-Flag on YEplac181(plasmid)</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: p61</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ubp12-C372S-Flag on YEplac181(plasmid)</td>
      <td>PMID: 23317502</td>
      <td>Escobar_lab_stock_number: p62</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>YEplac195 (plasmid)</td>
      <td>PMID: 3073106</td>
      <td>Escobar_lab_stock_number: p63</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ubp12C372S on YEplac195 (plasmid)</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: p65</td>
      <td>Ubp12C372S (non-tagged) on YEplac195, 2µ, Ura3</td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>mt-GFP on pYX142 (plasmid)</td>
      <td>PMID: 11054823</td>
      <td>Escobar_lab_stock_number: p70</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Cdc48 wt on pRS313 (plasmid)</td>
      <td>PMID: 22580068</td>
      <td>Escobar_lab_stock_number: p75</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>pRS313 (plasmid)</td>
      <td>PMID: 2659436</td>
      <td>Escobar_lab_stock_number: p79</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Cdc48-A547T on pRS313 (plasmid)</td>
      <td>this study</td>
      <td>Escobar_lab_stock_number: p150</td>
      <td>Cdc48A547T on pRS313, cen, His3</td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ub on pKT10 (plasmid)</td>
      <td>PMID: 2164637</td>
      <td>Escobar_lab_stock_number: p341</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ub-K48R on pKT10 (plasmid)</td>
      <td>PMID: 2164637</td>
      <td>Escobar_lab_stock_number: p342</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ub-K63R on pKT10 (plasmid)</td>
      <td>PMID: 2164637</td>
      <td>Escobar_lab_stock_number: p343</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Ub-K48R,K63R on pKT10 (plasmid)</td>
      <td>PMID: 2164637</td>
      <td>Escobar_lab_stock_number: p344</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>Myc-Ub on pRS426 (plasmid)</td>
      <td>PMID: 25620559</td>
      <td>Escobar_lab_stock_number: p356</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>pRS426 (plasmid)</td>
      <td>PMID: 25620559</td>
      <td>Escobar_lab_stock_number: p375</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Cdc48</td>
      <td>other</td>
      <td></td>
      <td>gift by T. Sommer; (1:1,000/1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Cox2</td>
      <td>other</td>
      <td></td>
      <td>gift by W. Neupert; (1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Flag M2</td>
      <td>Sigma</td>
      <td>Sigma: F1804</td>
      <td>(1:1,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Fzo1</td>
      <td>this study</td>
      <td></td>
      <td>Produced by GenScript using the peptide CHGDRKPDDDPYSSS; (1:1,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-HA</td>
      <td>Roche</td>
      <td>Roche: 11867423001</td>
      <td>(1:1,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Myc</td>
      <td>Cell Signaling</td>
      <td>Cell_Signaling: #2276</td>
      <td>(1:1,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Sec61</td>
      <td>other</td>
      <td></td>
      <td>gift by T. Sommer; (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ssc1</td>
      <td>Fölsch et al., 1998</td>
      <td></td>
      <td>(1:40,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Tom40</td>
      <td>other</td>
      <td></td>
      <td>gift by W. Neupert; (1:40,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Tpi1</td>
      <td>other</td>
      <td></td>
      <td>gift by J. Dohmen; (1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ub (P4D1)</td>
      <td>Cell Signaling</td>
      <td>Cell_Signaling: #3936</td>
      <td>(1:1,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ubc6</td>
      <td>other</td>
      <td></td>
      <td>gift by T. Sommer; (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ubp12</td>
      <td>this study</td>
      <td></td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>software</td>
      <td>Microsoft Office 2010</td>
      <td>Micosoft Corporation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software</td>
      <td>Adobe Photoshop CS6</td>
      <td>Adobe</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software</td>
      <td>Adobe Illustrator CS6</td>
      <td>Adobe</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software</td>
      <td>Clone Manager</td>
      <td>Sci-Ed Software</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software</td>
      <td>Image Quant</td>
      <td>GE Healthcare Life Sciences</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software</td>
      <td>Axiovision</td>
      <td>Zeiss</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software</td>
      <td>StepOne System</td>
      <td>Thermo Fisher Scientific</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>kit</td>
      <td>NucleoSpin RNA</td>
      <td>Machery Nagel</td>
      <td>REF:740955</td>
      <td></td>
    </tr>
    <tr>
      <td>kit</td>
      <td>SuperScript III First-Strand Synthesis System</td>
      <td>Invitrogen</td>
      <td>Catalogue_number:18080051</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Yeast strains and growth media

See Table 1 for details of all yeast strains used. Except for Δpdr5 Δsnq2 (YGA58, from J. Dohmen) and ufd1-2, npl4-1 and their corresponding wild type (DF5, from S. Jentsch) all other yeast strains are isogenic to the S288c (Euroscarf). They were grown according to standard procedures to the exponential growth phase at 30°C (unless stated otherwise) on complete (YP) or synthetic (SC) media supplemented with 2% (w/v) glucose (D), 2% (w/v) galactose or 2% (w/v) lactate (Lac). Cycloheximide (CHX) (Sigma, Germany) (100 µg/ml for protein shut-down, or 0.5 μg/ml when indicated, from a stock of 10 mg/ml in H2O) or MG132 (Calbiochem) (50 or 100 μM from a stock of 10 mM in DMSO) was added when indicated.

**Table 1.**
 Yeast strains used in this study.


<table>
  <thead>
    <tr>
      <th>Strain #</th>
      <th>Strain name</th>
      <th>Genotype</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FA2</td>
      <td>∆fzo1</td>
      <td>FZO1::kanMX4 in BY4741</td>
      <td>Brachmann et al., 1998</td>
    </tr>
    <tr>
      <td>FA230</td>
      <td>cdc48-1</td>
      <td>cdc48-1::KanMX4 in BY4741</td>
      <td>Li et al. (2011)</td>
    </tr>
    <tr>
      <td>FA231</td>
      <td>cdc48-2</td>
      <td>cdc48-2::KanMX4 in BY4741</td>
      <td>Li et al. (2011)</td>
    </tr>
    <tr>
      <td>FA232</td>
      <td>cdc48-3</td>
      <td>cdc48-3::KanMX4 in BY4741</td>
      <td>Li et al. (2011)</td>
    </tr>
    <tr>
      <td>FA260</td>
      <td>∆ubp2</td>
      <td>UBP2::kanMX4 in BY4741</td>
      <td>Brachmann et al., 1998</td>
    </tr>
    <tr>
      <td>FA269</td>
      <td>∆ubp12</td>
      <td>UBP12::kanMX4 in BY4741</td>
      <td>Brachmann et al., 1998</td>
    </tr>
    <tr>
      <td>FA362</td>
      <td>∆fzo1 ∆ubp2</td>
      <td>FZO1::kanMX4; UBP2::kanMX4; obtained by crossing</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>FA382</td>
      <td>∆ubp2 ∆ubp12</td>
      <td>UBP12::kanMX4; UBP2::kanMX4; obtained by crossing</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>FA390</td>
      <td>∆ubp12 ∆mdm30</td>
      <td>UBP12::kanMX4; MDM30::kanMX4; obtained by crossing</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>FA407</td>
      <td>HA-Fzo1int in wt</td>
      <td>HA-Fzo1 genomically integrated with NatNT2 into RS140</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>FA415</td>
      <td>HA-Fzo1int in ∆ubp2</td>
      <td>HA-Fzo1 genomically integrated with NatNT2 into FA260</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>FA427</td>
      <td>HA-Fzo1int in ∆ubp2 ∆mdm30</td>
      <td>HA-Fzo1 genomically integrated with NatNT2 into ∆ubp2 ∆mdm30</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>FA432</td>
      <td>∆fzo1 ∆ubp12</td>
      <td>FZO1::kanMX4; UBP12::kanMX4; obtained by crossing</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>FA451</td>
      <td>HA-Fzo1-K464Rint in wt</td>
      <td>HA-Fzo1K464R genomically integrated with NatNT2 into RS140</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS140</td>
      <td>wt</td>
      <td>BY4741; S288C isogenic yeast strain; MATa, his3Δ1, leu2Δ0, met15Δ0, ura3Δ0</td>
      <td>Brachmann et al., 1998</td>
    </tr>
    <tr>
      <td>RS430</td>
      <td>cdc48-2 ∆fzo1</td>
      <td>FZO1::natNT2 in FA231</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS466</td>
      <td>cdc48-2 ∆ubp12</td>
      <td>FZO1::hphNT1 in FA231</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS499</td>
      <td>cdc48-2 ∆ubp2 ∆ubp12</td>
      <td>UBP12::natNT2; UBP2::hphNT1 in FA231</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS518</td>
      <td>∆doa1</td>
      <td>DOA1::kanMX4 in BY4741</td>
      <td>Brachmann et al., 1998</td>
    </tr>
    <tr>
      <td>RS527</td>
      <td>∆pdr5 ∆snq2</td>
      <td>MATa, ADE2 his3-D200 leu2-3,112 lys2-801, trp1D63 ura3-52 PDR5::hphNT1 SNQ2::kanMX4</td>
      <td>J. Dohmen (YGA58)</td>
    </tr>
    <tr>
      <td>RS546</td>
      <td>Ubp12-Flagint in cdc48-2</td>
      <td>Ubp12-Flag genomically integrated with NatNT2 into FA231</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS547</td>
      <td>Ubp12-Flagint in wt</td>
      <td>Ubp12-Flag genomically integrated with NatNT2 into BY4741</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS554</td>
      <td>∆pdr5 ∆snq2</td>
      <td>PDR5::NatNT2; SNQ2::hphNT1 in RS140</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS556</td>
      <td>∆fzo1 ∆dnm1 ∆ubp12</td>
      <td>UBP12::NatNT2 in TS1029</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RS559</td>
      <td>∆pdr5 ∆snq2 cdc48-2</td>
      <td>PDR5::NatNT2; SNQ2::hphNT1 in FA231</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>TS686</td>
      <td>cdc48-2 ∆ubp2</td>
      <td>UBP2::hphNT1 in FA231</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>TS1029</td>
      <td>∆fzo1 ∆dnm1</td>
      <td>FZO1::kanMX4; DNM1::kanMX4; Mat α, BY background, obtained by crossing</td>
      <td>B. Westermann (#94)</td>
    </tr>
    <tr>
      <td>TS1124</td>
      <td>wt (DF5)</td>
      <td>MATα, trp1-1(am), ura3-52, his3∆200, leu2-3, lys2-801</td>
      <td>Hoppe et al. (2000)</td>
    </tr>
    <tr>
      <td>TS1125</td>
      <td>ufd1-2</td>
      <td>ufd1-2ts in TS1124</td>
      <td>Braun et al. (2002)</td>
    </tr>
    <tr>
      <td>TS1126</td>
      <td>npl4-1</td>
      <td>npl4-1ts in TS1124</td>
      <td>DeHoratius and Silver (1996)</td>
    </tr>
    <tr>
      <td>TS1134</td>
      <td>Ubp2-9Mycint in wt</td>
      <td>Ubp2-9Myc genomically integrated with NatNT2 into RS140</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>TS1144</td>
      <td>Ubp2-3HAint in wt</td>
      <td>Ubp2-3HA genomically integrated with hphNT1 in RS140</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>TS1147</td>
      <td>Ubp2-3HAint in ∆ubp12</td>
      <td>Ubp2-3HA genomically integrated with hphNT1 in FA269</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>TS1153</td>
      <td>pGAL-Ubp12-Flagint in wt</td>
      <td>pGAL-Ubp12-Flag genomically integrated with kanMX4 into RS544</td>
      <td>this study</td>
    </tr>
  </tbody>
</table>

### Plasmids

All plasmids used in this study are described in Table 2. Plasmid #65, encoding a non-tagged Ubp12C372S variant, expressed under the control of the ADH1 promoter, was amplified from Ubp12C372S-Flag and cloned with Pst1, Sal1 into the same sites of YEplac195. Plasmid #150, encoding Cdc48A547T was generated by point mutagenesis using plasmid #75.

**Table 2.**
 Plasmids used in this study.


<table>
  <thead>
    <tr>
      <th>Plasmid #</th>
      <th>Plasmid name</th>
      <th>Description</th>
      <th>Bacterial selection</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8</td>
      <td>pRS316</td>
      <td>pRS316, cen, Ura3</td>
      <td>Amp</td>
      <td>Sikorski and Hieter, 1989</td>
    </tr>
    <tr>
      <td>10</td>
      <td>HA-Fzo1 on pRS316</td>
      <td>HA-Fzo1 on pRS316, Fzo1 prom, cen, Ura3</td>
      <td>Amp</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>14</td>
      <td>HA-Fzo1-K464R on pRS316</td>
      <td>HA-Fzo1K464R on pRS316, Fzo1 prom, cen, Ura3</td>
      <td>Amp</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>58</td>
      <td>YEplac181</td>
      <td>YEplac181, 2µ, Leu2</td>
      <td>Amp</td>
      <td>Gietz and Sugino, 1988</td>
    </tr>
    <tr>
      <td>59</td>
      <td>Ubp2-Flag on YEplac181</td>
      <td>Ubp2-Flag on YEplac181, Adh1 prom, 2µ, Leu2</td>
      <td>Amp</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>60</td>
      <td>Ubp2-C745S-Flag on YEplac181</td>
      <td>Ubp2C745S-Flag on YEplac181, Adh1 prom, 2µ, Leu2</td>
      <td>Amp</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>61</td>
      <td>Ubp12-Flag on YEplac181</td>
      <td>Ubp2-Flag on YEplac181, Adh1 prom, 2µ, Leu2</td>
      <td>Amp</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>62</td>
      <td>Ubp12-C372S-Flag on YEplac181</td>
      <td>Ubp2C372S-Flag on YEplac181, Adh1 prom, 2µ, Leu2</td>
      <td>Amp</td>
      <td>Anton et al. (2013)</td>
    </tr>
    <tr>
      <td>63</td>
      <td>YEplac195</td>
      <td>YEplac195, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Gietz and Sugino, 1988</td>
    </tr>
    <tr>
      <td>65</td>
      <td>Ubp12C372S on YEplac195</td>
      <td>Ubp12C372S (non-tagged) on YEplac195, 2µ, Ura3</td>
      <td>Amp</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>70</td>
      <td>mt-GFP on pYX142</td>
      <td>mt-GFP on pYX142, cen, Leu2</td>
      <td>Amp</td>
      <td>Westermann and Neupert, 2000</td>
    </tr>
    <tr>
      <td>75</td>
      <td>Cdc48 wt on pRS313</td>
      <td>Cdc48 wt on pRS313, cen, His3</td>
      <td>Amp</td>
      <td>Esaki and Ogura (2012)</td>
    </tr>
    <tr>
      <td>79</td>
      <td>pRS313</td>
      <td>pRS313, cen, His3</td>
      <td>Amp</td>
      <td>Sikorski and Hieter, 1989</td>
    </tr>
    <tr>
      <td>150</td>
      <td>Cdc48-A547T on pRS313</td>
      <td>Cdc48A547T on pRS313, cen, His3</td>
      <td>Amp</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>341</td>
      <td>Ub on pKT10</td>
      <td>Ub on pK10, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Tanaka et al., 1990</td>
    </tr>
    <tr>
      <td>342</td>
      <td>Ub-K48R on pKT10</td>
      <td>UbK48R on pK10, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Tanaka et al., 1990</td>
    </tr>
    <tr>
      <td>343</td>
      <td>Ub-K63R on pKT10</td>
      <td>UbK63R on pK10, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Tanaka et al., 1990</td>
    </tr>
    <tr>
      <td>344</td>
      <td>Ub-K48R,K63R on pKT10</td>
      <td>UbK48R,K63R on pK10, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Tanaka et al., 1990</td>
    </tr>
    <tr>
      <td>356</td>
      <td>Myc-Ub on pRS426</td>
      <td>pCup1-Myc-Ub on pRS426, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Li et al., 2015</td>
    </tr>
    <tr>
      <td>375</td>
      <td>pRS426</td>
      <td>pRS426, 2µ, Ura3</td>
      <td>Amp</td>
      <td>Li et al., 2015</td>
    </tr>
  </tbody>
</table>

### Antibodies

All antibodies used in this study are described in Table 3.

**Table 3.**
 Antibodies used in this study.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Dilution</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cdc48</td>
      <td>1:1000/1:10,000</td>
      <td>T. Sommer</td>
    </tr>
    <tr>
      <td>Cox2</td>
      <td>1:5000</td>
      <td>W. Neupert</td>
    </tr>
    <tr>
      <td>Flag M2</td>
      <td>1:1000</td>
      <td>Sigma (F1804)</td>
    </tr>
    <tr>
      <td>Fzo1</td>
      <td>1:1000</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>HA</td>
      <td>1:1000</td>
      <td>Roche (11867423001)</td>
    </tr>
    <tr>
      <td>Myc</td>
      <td>1:1000</td>
      <td>Cell Signaling (#2276)</td>
    </tr>
    <tr>
      <td>Sec61</td>
      <td>1:10,000</td>
      <td>T. Sommer</td>
    </tr>
    <tr>
      <td>Ssc1</td>
      <td>1:40,000</td>
      <td>Fölsch et al., 1998</td>
    </tr>
    <tr>
      <td>Tom40</td>
      <td>1:40,000</td>
      <td>W. Neupert</td>
    </tr>
    <tr>
      <td>Tpi1</td>
      <td>1:5000</td>
      <td>J. Dohmen</td>
    </tr>
    <tr>
      <td>Ub (P4D1)</td>
      <td>1:1000</td>
      <td>Cell Signaling (#3936)</td>
    </tr>
    <tr>
      <td>Ubc6</td>
      <td>1:10,000</td>
      <td>T. Sommer</td>
    </tr>
    <tr>
      <td>Ubp12</td>
      <td>1:200</td>
      <td>this study</td>
    </tr>
  </tbody>
</table>

### Spot tests

For growth assays, serial 1:5 dilutions of exponentially growing cells using a starting OD600 of 0.5 or 0.005 were spotted on YP or SC media containing glucose or lactate and were grown at 30°C or 37°C, as indicated.

### Protein steady state levels and synthesis shutoff

For analysis of protein steady state levels, total proteins from 3 OD600 exponentially growing cells were extracted at alkaline pH (Escobar-Henriques et al., 2006) and analyzed by SDS-PAGE and immunoblotting. To monitor protein turnover, cycloheximide (100 µg/ml) was added to exponential cells. Samples of 3 OD600 cells were collected at the indicated time points and total proteins were extracted and analyzed as described above. For monitoring proteasome-dependent degradation of endogenous Fzo1 in wt and cdc48-2 cells, additionally deleted for SNQ2 and PDR5, YPD media was used (Liu et al., 2007), and cells were treated with 50 μM MG132, 30 min before adding cycloheximide. For monitoring proteasome-dependent degradation of Ubp2, expressed from plasmid #59, SCD media was used, and 50 μM MG132 was added 1 hr before starting the cycloheximide chase. Western blots were quantified using Image Quant (GE Healthcare, Illinois, USA). Levels of the protein of interest at time zero were set to 1. Mean values are shown and the error bars reflect the standard deviation (SD).

### Analysis of free ubiquitin and ubiquitin-conjugates

Total proteins were extracted as described above for the analysis of protein steady state levels but solubilized in LDS buffer (Thermo Fisher Scientific, Massachusetts, USA). Samples were run on precast 4–12% bis-tris gels (Thermo Fisher Scientific) using MES buffer (50 mM MES, 50 mM Tris Base, 0.1% SDS, 1 mM EDTA, pH 7.3) and transferred to PVDF membranes. Membranes were treated with denaturing solution (6 M guanidium chloride, 20 mM Tris pH 7.5, 1 mM PMSF, 5 mM β-mercaptoethanol) for 30 min and then washed before blocking. Proteins were detected with a ubiquitin-specific antibody (P4D1; Cell Signaling, Massachusetts) and a Tpi1-specific antibody, as a loading control. Quantifications were performed using Image Quant (GE Healthcare). Wt values were set to one and the mutants are shown in relation to the wt. Mean values are shown and the error bars reflect the standard deviation (SD).

### Analysis of Ubp12 ubiquitylation

Immunoprecipitation of Ubp12C372S-Flag was performed as follows: 160 OD600 of yeast cells grown in SCD media to the exponential growth phase were disrupted with glass beads (0.4–0.6 µm) in TBS. After centrifugation, at 16000 g for 10 min, the supernatant was employed to perform an overnight precipitation of Ubp12C372S-Flag, using Flag-coupled beads (Sigma-Aldrich). Elution was performed for 2 hr shaking at 4°C with the 3xFlag-peptide (Sigma; 200 µg/ml final concentration) in the following buffer: 50 mM Tris-HCl pH 7.5, 50 mM NaCl. After adding Laemmli buffer, the eluate was split in two, proteins were then resolved in 7% Tris-acetate gels as described (Cubillos-Rojas et al., 2012). After transfer, the nitrocellulose membrane was divided in two: one half was immunoblotted with a Flag-specific (Sigma) and the other half with a ubiquitin-specific antibody (P4D1; Cell Signaling).

### Analysis of Ubp2 ubiquitylation

Immunoprecipitation of Ubp2C745S-Flag was performed as follows: 160 OD600 of yeast cells grown in SCD media to the exponential growth phase were disrupted with glass beads (0.4–0.6 µm) in RIPA buffer without detergents (HEPES-KOH 40 mM pH 7.6, NaCl 150 mM, EDTA 5 mM). After centrifugating at 16000 g for 10 min, the supernatant was diluted in an equal volume of RIPA buffer containing 2X detergents, so that the final composition was HEPES-KOH 40 mM pH 7.6, NaCl 150 mM, EDTA 5 mM, Triton X100 1%, SDS 0.1%, sodium deoxycholate 0.5%. After sonication for 15 min at 4°C in a water bath, denatured cytosolic fractions were employed to precipitate Ubp2C745S-Flag. Flag-coupled beads (Sigma-Aldrich) were used for overnight immunoprecipitation and protein elution was performed with Laemmli buffer for 20 min shaking at 40°C. The eluate was split in two and resolved in 8% Tris-glycine gels. After transfer, the nitrocellulose membrane was divided in two: one half of the eluate was immunoblotted with a Flag-specific (Sigma) and the other half with a ubiquitin-specific antibody (P4D1; Cell Signaling).

### Analysis of Fzo1 ubiquitylation

Fzo1 ubiquitylation was analyzed as follows: 160 OD600 cell pellets of exponentially growing cultures were used to obtain crude mitochondrial extracts as described (Anton et al., 2013). After solubilization with 0.2 % NG310 (Lauryl Maltose Neopentyl Glycol; Anatrace) for 1 hr rotating at 4°C, samples were centrifuged and 10% of the supernatant was kept as input material. After denaturing in Laemmli buffer for 20 min shaking at 40°C samples were resolved by SDS-PAGE. If necessary, the remaining 90% of the supernatant was incubated with HA-coupled beads (Sigma-Aldrich) overnight rotating at 4°C. Three washes were performed with 0.2 % NG310 in TBS. HA-Fzo1 was eluted in 50 µl of Laemmli buffer for 20 min shaking at 40°C and analyzed by SDS-PAGE. Proteins were transferred onto nitrocellulose membranes and subsequently immunoblotted using an HA-specific antibody (Roche, Switzerland).

### Co-immunoprecipitations

#### Interaction between Ubp12-Flag and Cdc48

160 OD600 of yeast cells grown in complete media to the exponential growth phase were disrupted with glass beads (0.4–0.6 µm) in TBS. After centrifugation at 16000 g for 10 min, the crude membrane fraction was solubilized using 0.5% digitonin for 1 hr rotating at 4°C. Ubp12C372S-Flag was immunoprecipitated using Flag-coupled beads (Sigma-Aldrich) for 2 hr rotating at 4°C. Beads were washed three times with 0.1% digitonin in TBS and Ubp12C372S-Flag was eluted in Laemmli buffer for 20 min shaking at 40°C. 10% of the input and 100% of the eluate fractions were analyzed by SDS-PAGE and immunoblotting using Flag-specific (Sigma) and Cdc48-specific antibodies.

#### Interaction between HA-Fzo1 and Cdc48

Performed as described above for the Ubp12-Cdc48 interaction, with the following modifications: solubilization was performed with 0.2 % NG310; immunoprecipitation was performed for 2 hr using HA-coupled beads (Sigma-Aldrich) pre-blocked with PVPK30 (Polyvinylpyrrolidone; Fluka); washes were performed with 0.2 % NG310 in TBS. 4% of the input and 50% of the eluate fractions were analyzed by SDS-PAGE and immunoblotting using HA-specific (Roche) and Cdc48-specific antibodies.

#### Interaction between Ubp2-Flag and Ubp12

Immunoprecipitation of Ubp12C372S was performed as follows: 160 OD600 of yeast cells grown in SCD media to the exponential growth phase were disrupted with glass beads (0.4–0.6 µm) in TBS. After centrifugation at 16000 g for 10 min, the cytosolic fraction was used to precipitate Ubp12C372S by using an Ubp12-specific antibody and the affinity resin with protein G immobilized (Protein G Sepharose 4 Fast Flow; GE Healthcare). After 3 hr rotating at 4°C, beads were washed three times in TBS. Protein elution was performed with Laemmli buffer for 20 min shaking at 40°C. 1% of the input and 100% of the eluate were analyzed by SDS-PAGE and immunoblotting using Flag- and Ubp12-specific antibodies.

### Mitochondrial morphology

Yeast strains were transformed with mitochondrial-targeted GFP, grown on YPD or SC media to the exponential phase and analyzed as described (Escobar-Henriques et al., 2006) by epifluorescence microscopy (Axioplan 2; Carl Zeiss MicroImaging, Inc., Germany) using a 100x oil-immersion objective. Images were acquired with a camera (AxioCam MRm, Carl Zeiss MicroImaging, Inc.) and processed with Axiovision 4.7 (Carl Zeiss MicroImaging, Inc.).

### Analysis of mtDNA content using RT-PCR

RNA was isolated from 2 OD600 exponentially growing yeast cells using the NucleoSpin RNA kit (Macherey Nagel, Germany). cDNA was synthesized using the SuperScript III First-Strand Synthesis System (Invitrogen, Massachusetts, USA). mtDNA was quantified by the amplification of COX3 and normalized to ACT1 (as housekeeping gene). Essentially, a dilution of 1:100 of the cDNA was used for the amplification of COX3 (fw: TTGAAGCTGTACAACCTACC; rv: CCTGCGATTAAGGCATGATG) and ACT1 (fw: CACCCTGTTCTTTTGACTGA; rv: CGTAGAAGGCTGGAACGTTG) by RT-PCR using the Power SYBR Green Master Mix (AppliedBioSystems) and three technical replicates for each of the six biological replicates. The ∆CT was calculated using the Livak/2-∆∆CT method (Livak and Schmittgen, 2001) and the fold change of COX3 RNA content in ∆fzo1 and cdc48-2 was calculated in relation to wt.

### DUB assay

In vitro deubiquitylation assays were performed as described (Hospenthal et al., 2015), Essentially, purified K48 or K63 multi-Ub (BostonBiochem) or di-Ub chains (kindly gifted by Thomas Hermanns) were treated with the DUBs USP2 (BostonBiochem), USP21 (kindly gifted by Selver Altin) or Ubp12. Ubp12 was purified as described above, for the analysis of Ubp12 ubiquitylation, but glycerol to the final concentration of 10% was added, instead of Laemmli. Aliquots of 18 µl, corresponding to 80 OD600 yeast cells, were frozen in liquid nitrogen and stocked at −80°C until further use. For the DUB assay, per reaction, one aliquot of purified Ubp12-flag, 3 µM USP2 or 5 µM USP21 were pre-incubated with 1x DUB dilution buffer (25 mM Tris pH 7.5, 10 mM DTT, 150 mM NaCl) for 10 min at RT.

After pre-incubation, the DUBs were mixed with di- or multi-Ub chains to a final concentration of 5 µM in 1x DUB buffer (10x DUB buffer: 500 mMTris pH 7.5, 500 mMNaCl, 50 mM DTT). Different incubation conditions were used: Ubp12 was incubated with the Ub chains for 45 min at 30°C, USP2 and USP21 for 30 min at 37°C. The reactions were stopped by adding 4x Laemmli buffer. These mixtures were incubated for 20 min at 40°C shaking and further run on an 11% Tris-Tricine SDS-PAGE and transferred onto a PVDF membrane. Ponceau S was used to stain the membrane and after destaining with methanol for 5 min, the membrane was incubated in denaturing solution (6M guanidium chloride, 20 mMTris pH 7.5, 1 mM PMSF, 5 mMβ-mercaptoethanol) for 30 min. Extensive washing was done in TBS-T before blocking the membrane over night with 5% milk in TBS. Results were analyzed by immunoblotting using a Ub-specific antibody.
