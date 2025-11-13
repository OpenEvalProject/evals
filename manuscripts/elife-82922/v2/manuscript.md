# Single amino acid residue mediates reciprocal specificity in two mosquito odorant receptors

## Authors

- Flavia P Franco<sup>1</sup> ([ORCID: 0000-0003-3739-8625](https://orcid.org/0000-0003-3739-8625))
- Pingxi Xu<sup>1</sup>
- Brandon J Harris<sup>2</sup>
- Vladimir Yarov-Yarovoy<sup>2</sup> ([ORCID: 0000-0002-2325-4834](https://orcid.org/0000-0002-2325-4834))
- Walter S Leal<sup>1</sup> ([ORCID: 0000-0002-6800-1240](https://orcid.org/0000-0002-6800-1240)) †

### Affiliations

1. Department of Molecular and Cellular Biology, University of California, Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
2. Department of Physiology and Membrane Biology, University of California, Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
3. Department of Anesthesiology and Pain Medicine, University of California, Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))

† Corresponding author

## Abstract

The southern house mosquito, Culex quinquefasciatus, utilizes two odorant receptors, CquiOR10 and CquiOR2, narrowly tuned to oviposition attractants and well conserved among mosquito species. They detect skatole and indole, respectively, with reciprocal specificity. We swapped the transmembrane (TM) domains of CquiOR10 and CquiOR2 and identified TM2 as a specificity determinant. With additional mutations, we showed that CquiOR10A73L behaved like CquiOR2. Conversely, CquiOR2L74A recapitulated CquiOR10 specificity. Next, we generated structural models of CquiOR10 and CquiOR10A73L using RoseTTAFold and AlphaFold and docked skatole and indole using RosettaLigand. These modeling studies suggested space-filling constraints around A73. Consistent with this hypothesis, CquiOR10 mutants with a bulkier residue (Ile, Val) were insensitive to skatole and indole, whereas CquiOR10A73G retained the specificity to skatole and showed a more robust response than the wildtype receptor CquiOR10. On the other hand, Leu to Gly mutation of the indole receptor CquiOR2 reverted the specificity to skatole. Lastly, CquiOR10A73L, CquiOR2, and CquiOR2L74I were insensitive to 3-ethylindole, whereas CquiOR2L74A and CquiOR2L74G gained activity. Additionally, CquiOR10A73G gave more robust responses to 3-ethylindole than CquiOR10. Thus, we suggest the specificity of these receptors is mediated by a single amino acid substitution, leading to finely tuned volumetric space to accommodate specific oviposition attractants.

## Introduction

Insects perceive the world with a sophisticated olfactory system essential for survival and reproduction. Their antennae are biosensors par excellence, allowing detection of a plethora of compounds, some with extraordinary sensitivity and selectivity (Kaissling, 2014). The insect olfactory system is comprised mainly of odorant-binding proteins, odorant-degrading enzymes, ionotropic receptors, and the ultimate gatekeepers of selectivity (Leal, 2013; Leal, 2016; Leal, 2020) – the odorant receptors (ORs) (Clyne et al., 1999; Gao and Chess, 1999; Vosshall et al., 1999). The ORs are the binding units in functional heteromeric cation channels (Neuhaus et al., 2005) formed with an odorant receptor coreceptor (Orco) (Larsson et al., 2004). Unlike mammalian olfactory receptors, insect ORs and Orco have inverse topologies compared to G-protein-coupled receptors (GPCRs), with a cytosolic N-terminus and an extracellular C-terminus (Benton et al., 2006; Lundin et al., 2007). One of the major breakthroughs in the fields of insect olfaction in the last two decades since the discovery of ORs (Leal, 2020) was the determination of the cryo-electron microscopy (cryo-EM) structure of the Orco homomer from the parasitic fig wasp, Apocrypta bakeri, AbakOrco (Butterwick et al., 2018). Subsequently, the structure for a promiscuous OR from the evolutionarily primitive (Apterygota, wingless) jumping bristletail, Machilis hrabei, MhraOR5, was solved (DelMarmol et al., 2021). Although structures of ORs from winged insects (Pterygota) have not been solved to date, amino acid residues critical for OR specificity have been reported (Auer et al., 2020; Cao et al., 2021; Hughes et al., 2014; Leary et al., 2012; Pellegrino et al., 2011; Yang et al., 2017; Yuvaraj et al., 2021). These studies focused on one-way alteration of specificity but did not examine how an insect detects two odorants with reverse specificity.

Mosquitoes are vectors of pathogens that cause tremendous harm to public health. Male and female mosquitoes visit plants to obtain nutrients for flight. For reproduction and survival of the species, females must acquire a blood meal to fertilize their eggs and, subsequently, oviposit in an aquatic environment suitable for the offspring to flourish. While feeding on hosts, females transmit viruses and other pathogens. The southern house mosquito, Culex quinquefasciatus, transmits pathogens causing filariasis and various encephalitis (Nasci and Miller, 1996). In the United States, mosquitoes belonging to the Culex pipiens complex transmit the West Nile virus (Andreadis, 2012). Due to its opportunistic feeding on avian and mammalian hosts, Cx. quinquefasciatus is a significant bridge vector in urbanized centers in the Western United States, particularly southern California (Andreadis, 2012; Syed and Leal, 2009). Female mosquitoes rely on multiple sensory modalities, including olfaction, to find plants, vertebrate hosts, and suitable environments for oviposition.

The genome of the southern house mosquito, Cx. quinquefasciatus (Arensburger et al., 2010), has the most extensive repertoire of OR genes (Leal et al., 2013) among mosquito species. The genomes of Anopheles darlingi, the malaria mosquito, Anopheles gambiae, the yellow fever mosquito, Aedes aegypti, the Asian tiger mosquito, Aedes albopictus, and the southern house mosquito contain 18 (Marinotti et al., 2013), 79 (Hill et al., 2002), 117–131 (Bohbot et al., 2007; Nene et al., 2007), 158 (Chen et al., 2015), and 180 (Arensburger et al., 2010) OR genes, respectively. Of those, 61 transcripts were found in An. gambiae (Pitts et al., 2011), 107 in Ae. aegypti (Matthews et al., 2018), and 177 in Cx. quinquefasciatus (Leal et al., 2013). Given that the number of odorants in the environment is larger than the number of OR genes even in Cx. quinquefasciatus, it is not surprising that many ORs from insects are promiscuous (Leal, 2013; Pask, 2020). However, ORs detecting behaviorally critical compounds (semiochemicals) may be narrowly tuned (Hughes et al., 2010; Nakagawa et al., 2005; Stensmyr et al., 2012).

ORs narrowly tuned to 3-methylindole (=skatole) and indole have been found in mosquito species in the subfamilies Culicinae and Anophelinae. Specifically, OR10 and OR2 have been de-orphanized in the southern house mosquito (Hughes et al., 2010; Pelletier et al., 2010), the yellow fever mosquito (Bohbot et al., 2011), and the malaria mosquito (Carey et al., 2010; Wang et al., 2010). Recently, these so-called indolergic receptors Bohbot and Pitts, 2015 have also been found in the housefly, Musca domestica (Pitts et al., 2021). Skatole and indole are fecal products that have been identified as oviposition attractants for the southern house mosquito (Blackwell et al., 1993; Mboera et al., 2000; Millar et al., 1992). Skatole is a potent oviposition attractant in minute doses, whereas indole is active only at high doses (Millar et al., 1992). To the human nose, skatole has a pungent fecal odor. In contrast, indole has an almost floral odor when highly purified and presented at low doses (Fenaroli, 1975), but a fecal odor at high doses. Remarkably, in all mosquito species and the housefly, OR10s are narrowly tuned to skatole and respond with lower sensitivity to indole, whereas indole is the most potent ligand for OR2s, which give lower responses to skatole. In Cx. quinquefasciatus, these receptor genes were initially named CquiOR10 and CquiOR2, respectively, renamed CquiOR21 and CquiOR121, but a proposition to restore the original names is under consideration (Carolyn McBride, personal communication). Here, we refer to these receptors from Cx. quinquefasciatus as CquiOR10 (VectorBase and GenBank IDs, CPIJ002479 and GU945397, respectively) and CquiOR2 (CPIJ014392, GU945396.1).

These oviposition attractant-detecting (Chen and Luetje, 2014) receptors in Cx. quinquefasciatus, CquiOR10 and CquiOR2, provide a suitable model to identify specific determinants as they respond to skatole and indole with reverse specificity. CquiOR10 and CquiOR2 proteins have 377 and 375 amino acid residues, respectively, and share only 49.5% amino acid identity, whereas 61.9% of the amino acids in the predicted transmembrane domains are identical (Supplementary file 1, Table 1). To identify the specificity determinants of these receptors, we swapped transmembrane (TM) domains and tested the chimeric receptors using the Xenopus oocyte recording system. Given that CquiOR10 is the second most sensitive Cx. quinquefasciatus OR (second only to CquiOR36; Choo et al., 2018), we replaced the predicted (Reynolds et al., 2008) transmembrane domains from CquiOR2 into CquiOR10 and measured the specificity of the chimeric receptors. With this approach, we identified TM2 as a specificity determinant. Next, we tested mutations of chimeric CquiOR10 and identified a single amino acid residue in TM2 (Ala-73) that determines the receptor’s specificity. We then directly mutated the wildtype receptor and observed that CquiOR10A73L is specific to indole as CquiOR2. Additionally, CquiOR2L74A emulated the response profile of CquiOR10. To better understand the structural basis of this single-point specificity determinant, we generated structural models of CquiOR10 and CquiOR10A73L using RoseTTAFold (Baek et al., 2021) and AlphaFold (Jumper et al., 2021). We identified the binding poses for skatole and indole using RosettaLigand molecular docking and observed a finely tuned volumetric space to accommodate specific oviposition attractants.

## Results

### Chimeric OR with reversed specificity

We envisioned that studying a pair of ORs with reverse specificities, like CquiOR10 and CquiOR2, could lead us to specificity determinants. CquiOR10 is activated by the oviposition attractant skatole (Blackwell et al., 1993; Mboera et al., 2000; Millar et al., 1992) with high specificity (Figure 1A), whereas CquiOR2 is specific to indole (Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig1-v2.jpg)

**Figure 1.:** (A) CquiOR10 and (B) CquiOR2. Lines were obtained with nonlinear fit. Bars represent SEM. n = 4–5.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) CquiOR10M3; (B) CquiOR10M4; (C) CquiOR10M5; (D) CquiOR10M6; (E) CquiOR10M7; (F) CquiOR10M3,4,5,6,7; (G) CquiOR10M3,4,5,6; (H) CquiOR10M4,5,6; (I) CquiOR10M3,5,6; (J) CquiOR10M3,4,6; (K) CquiOR10M3,4,5; (L) CquiOR10M3,4; (M) CquiOR10M3,5; (N) CquiOR10M3,6; (O) CquiOR10M3,7; (P) CquiOR10M4,5; (Q) CquiOR10M4,6; (R) CquiOR10M4,7; (S) CquiOR10M5,6; (T) CquiOR10M5,7; and (U) CquiOR10M6,7. Lines were obtained with nonlinear fit. Barsrepresent SEM. n = 3.

Our approach was designed to swap TM domains using the more sensitive receptor, CquiOR10, as the acceptor. Specifically, we generated chimeric receptors by replacing CquiOR10 TM domains with related domains from CquiOR2 (Figure 2A). During the life of this project, the cryo-EM structure of an odorant receptor coreceptor AbakOrco from the parasitic fig wasp, Aprocrypta bakeri, was reported (Butterwick et al., 2018). We then compared the experimental structure (Butterwick et al., 2018) with the predicted topology for AbakOrco using the same OCTOPUS method (Viklund and Elofsson, 2008) we used to identify CquiOR10 and CquiOR2 TMs (Figure 2A; Viklund and Elofsson, 2008). The almost perfect overlap between OCTOPUS prediction and the AbakOrco structure (Figure 2B) validated not only our TM predictions (Figure 2A), but also the 21 chimeric ORs already tested when the structure of the coreceptor AbakOrco (Butterwick et al., 2018) was reported.

![Figure 2.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig2-v2.jpg)

**Figure 2.:** (A) CqOR10 and CqOR2 are abbreviations for CquiOR10 and CquiOR2, respectively. The TM domains, predicted by OCTOPUS, are displayed in red and blue for CquiOR10 and CquiOR2, respectively. The sequences of the N-terminus and the intracellular loops are displayed in black, and the C-terminus and extracellular loops in green. (B) Left: the cryo-EM structure of AbakOrco (PDB, 6C70) displayed in rainbow color using UCSF Chimera (Pettersen et al., 2004). Right: the predicted TM domains (right) are displayed in gray. The dashed lines represent the membrane boundaries.

We referred to these chimeric receptors as CquiOR10Mx, where Mx refers to TMx from CquiOR2. We performed functional assays of these CquiOR10Mx receptors using the Xenopus oocyte recording system. This long-term project could require as many as 127 possible chimeric receptors. We started by swapping all seven TM domains. We envisioned that this chimeric receptor would have a reverse specificity. If so, we would restore one TM at a time to identify critical domains. It turned out that CquiOR10M1,2,3,4,5,6,7 was silent (see Appendix 1, Supplementary file 1, Table 2). To minimize the number of tested mutants, we changed the strategy to start from single mutations to obtain educated guess for the subsequent design of mutants. With this approach, we generated and tested only 8 of the required 99 mutants with 7–3 TMs swapped. We tested 36 chimeric receptors (see Supplementary file 1, Table 2, and Figure 1—figure supplement 1). Fourteen chimeric receptors did not respond to skatole or indole, and 21 receptors retained the specificity to skatole (Supplementary file 1, Table 2, and Figure 1—figure supplement 1). Lastly, CquiOR10M2,7/CquiOrco-expressing oocytes responded to both skatole and indole with a reverse profile (Figure 3A). This dataset shows that CquiOR10M2,7 emulated the profile of the indole receptor CquiOR2 (Figure 1B).

![Figure 3.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig3-v2.jpg)

**Figure 3.:** (A) CquiOR10M2,7; (B) CquiOR10M2,5,6,7; (C) CquiOR10M2,5,6,7_Outer; (D) CquiOR10M2,5,6,7_Mid;Inner; (E) CquiOR10M2,5,6,7_Inner; (F) CquiOR10M2,5,6,7T78I; (G) CquiOR10M2,5,6,7L73A; (H) CquiOR10M7A73L; (I) CquiOR10A73L; (J) CquiOR2L74A. Lines were obtained with nonlinear fit. Bars represent SEM. The number of replicates (n) were 7, 4, 5, 5, 4, 3, 9, 7, 6, and 5, respectively.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig3-figsupp1-v2.jpg)

#### A single-point mutation that reverses the specificity of the skatole and indole receptors

We proceeded to identify the amino acid residues in the swapped domains of CquiOR10M2,7, directly affecting the specificity of the chimeric and wildtype receptors. Given the observation that, by and large, chimeric receptors with TM5 and TM6 from CquiOR2 gave stronger responses (Figure 1—figure supplement 1), we asked whether CquiOR10M2,7 responses with these two additional TM domains swapped would give more robust responses while keeping the same specificity to indole. CquiOR10M2,5,6,7/CquiOrco-expressing oocytes were indeed more sensitive while maintaining the selectivity to indole (Figure 3B). We then used CquiOR10M2,5,6,7 and designed various mutants to rescue single or multiple residues in TM2 at a time (Figure 4). We focused on TM2 because swapping TM7 did not affect the specificity of the receptor (Figure 1—figure supplement 1E). We divided TM2 into outer, middle, and inner segments based on the topology predicted by OCTOPUS (Viklund and Elofsson, 2008).

![Figure 4.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig4-v2.jpg)

**Figure 4.:** The two last residues of the extracellular loop-1 (Ile-57 and Asp-58) appear in the N-terminus. The TM2 was divided into the arbitrary segments outer, middle (mid), and inner to identify specificity determinants.

It has been postulated that the extracellular halves of TM domains form an odorant-binding pocket (Guo and Kim, 2010); thus, we first examined a mutant (CquiOR10M2,5,6,7_Outer) having the residues in the outer segment at 59, 60, 63, and 64 restored to Glu, Val, Asn, and Ala, respectively, as in the wildtype receptor (Figure 4). CquiOR10M2,5,6,7_Outer/CquiOrco-expressing oocytes retained the specificity of CquiOR10M2,5,6,7 with a more robust response to indole than skatole (Figure 3C). These findings indicated that the residues in the outer segment of TM2 are not specificity determinants. After that, we tested a chimeric receptor with the residues in the middle and inner part of the TM2 domain rescued to match those in the wildtype receptor (Figure 4). CquiOR10M2,5,6,7_Mid;Inner restored the skatole-specific profile of CquiOR10 (Figure 3D), thus suggesting that amino acid residues in these segments are specificity determinants. Then, we tested CquiOR10M2,5,6,7_Inner (=CquiOR10M2,5,6,7L73A;T78I), which had only residues at 73 and 78 rescued to the wildtype Ala and Ile, respectively. Oocytes co-expressing CquiOR10M2,5,6,7_Inner and CquiOrco reverted the specificity to skatole (Figure 3E). As a result, we concluded that residues in the predicted inner part of TM2 are critical for the chimeric receptor’s specificity. We further probed the chimeric receptor CquiOR10M2,5,6,7 with single-point mutations to identify the residue(s) determining specificity. CquiOR10M2,5,6,7T78I/CquiOrco-expressing oocytes showed the same specificity as the chimeric receptor CquiOR10M2,5,6,7 (Figure 3F). Specifically, CquiOR10M2,5,6,7T78I gave a more robust response to indole than skatole, suggesting that rescuing the residue at 78 did not affect CquiOR10M2,5,6,7 specificity. By contrast, CquiOR10M2,5,6,7L73A/CquiOrco-expressing oocytes reverted the specificity to skatole (Figure 3G), thus behaving like the wildtype receptor CquiOR10 (Figure 1A). To further examine the role of Ala-73 as a specificity determinant residue, we obtained a single-point mutation of CquiOR10M7, which is specific to skatole (Figure 1—figure supplement 1E). The responses recorded from CquiOR10M7A73L/CquiOrco-expressing oocytes showed a reverse, indole-specific profile (Figure 3H), like the CquiOR2 profile (Figure 1B). Having identified a single amino acid residue in the chimeric receptor that switches the skatole/indole specificity, we tested the effect of single-point mutation on the specificity of the wildtype receptor CquiOR10 (EC50: skatole, 3.6 µM; indole 29.9 µM). CquiOR10A73L showed a reverse specificity, with dose-dependent responses to indole (Figure 3I) (EC50: indole, 3.4 µM; skatole 53.7 µM). Collectively, these findings suggest that a single amino acid residue in CquiOR10 determines the specificity of this receptor. Additionally, we obtained an equivalent single-point mutation in the indole-specific CquiOR2 (Figure 1B) (EC50: indole, 7.7 µM; skatole 16.4 µM). Thus, CquiOR2L74A/CquiOrco-expressing oocytes gave robust and specific responses to skatole (Figure 3J) (EC50: skatole, 8.5 µM; indole 27.6 µM).

As summarized in a graphical representation (Figure 3—figure supplement 1), these findings demonstrate that these two mosquito odorant receptors, CquiOR10 and CquiOR2, have reciprocal specificity mediated by a single amino acid residue, Ala-73 and Leu-74, respectively.

We also recorded the response of these ORs to other phenolic ligands that activate indolic receptors, albeit generating small currents. While CquiOR10 and CquiOR2 responded to phenol, 3,5-dimethylphenol activated only CquiOR10 (Figure 5A). A single-point mutation in CquiOR10 rendered the chimeric receptor insensitive to 3,5-dimethylphenol. By contrast, an equivalent mutation in CquiOR2 recapitulated the profile of CquiOR10 (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig5-v2.jpg)

**Figure 5.:** (A) Each receptor was co-expressed with CquiOrco in Xenopus oocytes and stimulated with the phenolic compounds at 1 mM. n = 3–5. (B) CquiOR10/CquiOrco-, (C) CquiOR2/CquiOrco-, and (D)-CquiOR2L74A-expressing oocytes were stimulated with 100 µM of the specified methylindoles. n = 9–11. Bars represent SEM.

Additionally, we recorded responses elicited by methylindoles. Specifically, we challenged oocytes with 1-methylindole, 2-methylindole, 4-methylindole, 5-methylindole, 6-methylindole, and 7-methylindole. In these analyses, we did not stimulate the oocyte preparations with 3-methylindole to avoid possible desensitization. CquiOR10/CquiOrco-expressing oocytes elicited stronger responses when challenged with 1-methylindole and 5-methylindole than when stimulated with the other methylindoles (Figure 5B). By contrast, CquiOR2/CquiOrco-expressing oocytes elicited similarly lower responses when stimulated with methylindoles (Figure 5C). CquiOR2L74A with a single-point mutation to mimic OR10 receptor recapitulated CquiOR10 response profile (Figure 5D). These data suggest that a single amino acid residue determines a receptor’s specificity toward ligands eliciting robust or small responses.

### CquiOR10 computational modeling suggests space-filling constraints for indole-based odorants around A73

To structurally hypothesize the above-described reciprocal specificity, we generated structural models of CquiOr10, CquiOR2, CquiOR10A73L, and CquiOR2L74A using RoseTTAFold (Baek et al., 2021) and a structural model of CquiOR10 using AlphaFold (Jumper et al., 2021; Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig6-v2.jpg)

**Figure 6.:** Structural models of CquiOR10 (A, B), CquiOR10A73L (C), CquiOR2 (D), and CquiOR2L74A (E) with AlphaFold (A) and RoseTTAFold (B–E) structure prediction methods. Superposition of all RoseTTAFold models (F) resulted in transmembrane helix root mean square deviation (RMSD) of 0.8 Å when aligned with RoseTTAFold CquiOR10. (G) The transmembrane helix RMSD of CquiOR10 RoseTTAFold (rainbow) vs. AlphaFold (gray) was 1.7 Å. Loops were not included in RMSD calculation due to inherent flexibility during structure prediction.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig6-figsupp1-v2.jpg)

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) RoseTTAFold and (B) AlphaFold models for CquiOR10.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig6-figsupp3-v2.jpg)

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig6-figsupp4-v2.jpg)

CquiOR10 models of one homotetramer subunit were generated with AlphaFold and RoseTTAFold, each producing five models. RoseTTAFold models of CquiOR10, CquiOR10A73L, CquiOR2, and CquiOR2A73L produced a transmembrane helix root mean square deviation (RMSD) between α-Carbon atoms less than 1 Å across all 20 models (five models per odorant receptor); this suggests that the homologous CquiOR10 and CquiOR2 are structurally similar and that single-point mutations should not cause great structural deviation from wildtype. Comparing CquiOR10 models, RoseTTAFold and AlphaFold produced a transmembrane helix RMSD of 1.7 Å, with the transmembrane helices at the extracellular membrane face having the largest structural deviation. Considering there is little structural knowledge of insect odorant receptors, their binding mechanisms, and their conformational changes, we suspected that homologous odorant receptors would have similar binding modes. Further, pairwise sequence alignment suggests that a series of residues in MhraOR5 TM4 aligns with CquiOR10 TM2, which contains CquiOR10A73 (CquiOR10: 59EVI-INAYFAMIFFNAV74. MhraOR5: 199EVIAIYEAVAMIFLITA215.; Figure 6—figure supplement 1) while AlphaFold and RoseTTAFold models of CquiOR10 were broadly similar to MhraOR5 (Figure 6—figure supplement 2). Using transmembrane helix 7b (TM7b), we superimposed the top-ranking CquiOR10 RoseTTAFold and AlphaFold models with an experimentally resolved structure, M. hrabei (MhraOR5) in complex with eugenol (PDB ID: 7LID; DelMarmol et al., 2021) to identify which of our models resembled an odorant-bound conformation. With this selection criteria, we proceeded with RoseTTAFold models of the odorant receptors for Rosetta-based small-molecule docking method RosettaLigand (Davis and Baker, 2009; DeLuca et al., 2015) as the structural similarity around the hypothesized binding pocket was greater than the AlphaFold models of the odorant receptors compared with the MhraOR5 structure. We chose to select conformationally similar models over modeling and docking an apo structure into a bound conformation because it is a more cautious approach when there is little structural information. We perceived modeling an apo structure into a bound conformation to potentially yield more biologically implausible conformations than docking of a structurally comparative model.

To verify that RosettaLigand could effectively sample odorants in receptors homologous to CquiOR10 and CquiOR2, we used the structure of eugenol in complex with the insect odorant receptor OR5 from MhraOR5 (PDB ID: 7LID) as a control (DelMarmol et al., 2021). Rosetta protein-ligand docking employs energy-based analyses, such as the interface energy between protein and ligand, to select the representative models (Bidula et al., 2022). With this selection method, the RMSD of our MhraOR5-eugenol models relative to the experimental structure ranged from 0.5 to 5.0 Å (Supplementary file 1, Table 3). RMSD values equal or below 2.0 Å are considered an appropriate range for validation (Park et al., 2021). After using hdbscan cluster analysis (McInnes et al., 2017) to group structurally similar models, the largest cluster had a RMSD of 0.75 Å while the lowest interface-energy model had a RMSD of 2.4 Å. Collectively, these data demonstrate that RosettaLigand paired with the hdbscan clustering method can recapitulate the MhraOR5 structure and blindly select a near-native model, thus is suitable for structural predictions of odorants with CquiOR10A73L and CquiOR2L74A (Figure 6—figure supplements 3 and 4).

For each receptor–ligand complex (CquiOR10-skatole, CquiOR10A73L-skatole, CquiOR10-indole, and CquiOR10A73L-indole), we generated 100,000 docking models using RosettaLigand, clustered the 10,000 lowest interface-energy models, and selected the lowest interface-energy model from the 10 largest clusters, resulting in 10 models per receptor–ligand complex from which to draw structural hypotheses (Supplementary file 1, Tables 4 and 5). Our modeling suggests that both indole and skatole can readily reorient themselves in a similar pore depth near residue 73, regardless of mutant or wildtype receptor. Comparing the lowest interface-scoring model from each receptor–ligand complex, indole and skatole are positioned in the membrane-embedded pore, flanked by transmembrane helices S2, S4, S5, and S6, and show positional overlap in both and CquiOR10-A73L CquiOR10 (Figure 7, Figure 7—figure supplements 1–5).

![Figure 7.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-v2.jpg)

**Figure 7.:** Each model shown is the lowest interface-energy model from the 10 largest clusters of each docking study. CquiOR10 – skatole (forest green), CquiOR10 – indole (brown), CquiOR10A73L – skatole (light blue), and CquiOR10A73L – indole (purple). Atoms that are not indole/skatole carbon atoms are color-coded by atom type: carbon (gray), nitrogen (dark blue), and oxygen (red). Ala-73 and Leu-73 indicated with space-filling representation. (A, B) and (C, D) Mebrane and extracellular views for CquiOR10 and CquiOR10A73L, respectively.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp1-v2.jpg)

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp2-v2.jpg)

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp3-v2.jpg)

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** OR: odorant receptor.

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp5-v2.jpg)

**Figure 7—figure supplement 5.:** (A) CquiOR10 and (B) CquiOR10A73L.

![Figure 7—figure supplement 6.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp6-v2.jpg)

**Figure 7—figure supplement 6.:** The representative is the lowest interface-scoring energy model from the 10 most frequent clusters of each test case. Hydrogen bond andpi-stacking interactions were filtered by previously reported bond distances (Bissantz et al., 2010).

![Figure 7—figure supplement 7.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp7-v2.jpg)

![Figure 7—figure supplement 8.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig7-figsupp8-v2.jpg)

**Figure 7—figure supplement 8.:** (A) Odorants docked to CquiOR (grey) were positioned relative to eugenol from MhraOR5 (PDB 7LID) and then randomlyrotated/translated within 7 Å as a starting position for docking. The green sphere represents the 7 Å sampling boundary. (B) An example demonstrating thesampling of skatole (green) docked to CquiOR10 after docking with eugenol (yellow) as a positional reference. Red: extracellular membrane boundary. Blue: cytosplasmic membrane boundary.

In most models, skatole and indole form contacts with CquiOR10 and CquiOr10A73L in a similar plane about a center of rotation. These observations are supported by skatole and indole not containing rotatable bonds, thus relying on rigid translational movements and rotation to form favorable contacts with the rotatable and repackable receptor residues. Additionally, our models position indole and skatole within a series of nonpolar, polar-uncharged, and aromatic amino acids. Protein–ligand interaction profiler (PLIP) analysis (Adasme et al., 2021) suggests that the bulk of favorable interactions are nonpolar, occasional hydrogen bonding with the odorant NH group, and occasional parallel pi stacking, with the ligand-binding pocket formed by TMs 2, 4, 5, and 6 (Figure 7—figure supplement 6). Akin to eugenol forming hydrophobic contacts with MhraOR5/Ile-213 from TM4 (Figure 6—figure supplement 3), skatole and indole formed hydrophobic contacts with CquiOR10/Asn-72 from TM2 (Supplementary file 1, Table 8), which are matched pairs form Needleman–Wunsch pairwise alignment (Figure 6—figure supplement 1). We find of most importance skatole and indole not forming contacts with Ala-73 in CquiOR10 models (Supplementary file 1, Tables 6–14). By contrast, in the CquiOR17A73L models, skatole formed hydrophobic contacts with Leu-73 in 5 of the 10 representative models, while indole formed contacts with Leu-73 in 2 representative models (Supplementary file 1, Table 8). This suggests that Ala-73 may indirectly affect specificity by modulating the volume of the binding pocket (see Appendix 3).

Structurally aligning CquiOR10 and CquiOR10A73L receptors by TM7b (Supplementary file 1, Table 15), demonstrates approximately a 1 Å α-carbon outward shift of A73L (Supplementary file 1, Table 16), suggesting a tightly constrained space in CquiOR10 and an expanded space in CquiOR10A73L relative to the protein backbone (Figure 8).

![Figure 8.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig8-v2.jpg)

**Figure 8.:** An approximate 1 Å α-carbon outward shift of Leu-73 (forest green) in CquiOR10 model relative to Ala-73 (light blue) in CquiOR10A73L model. Models were superimposed using the TM7b region. Residue 73 amino nitrogen is colored in dark blue, and carboxyl oxygen is colored in red in each model.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A-C) CquiOR10 mutants. (D-F) CquiOR2 mutants.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig8-figsupp2-v2.jpg)

This difference in binding pocket volume is not ligand-induced, but rather independent of skatole or indole binding. Consistent with our structural hypothesis of space constraints, mutation of Ala-73 in CquiOR10 to Ile or Val negatively affected receptor function, whereas CquiOR10A73G retained specificity and showed higher sensitivity. Specifically, CquiOR10A73I/CquiOrco- and CquiOR10A73V/CquiOrco-expressing oocytes did not respond to skatole or indole (Figure 8—figure supplement 1A and B). We concluded that mutations with these bulkier residues caused loss of binding to indole or skatole, given that these receptors were functional, as indicated by the potent responses elicited by the Orco ligand candidate OLC12, 2-{[4-Ethyl-5-(4-pyridinyl)–4 H-1,2,4-triazol-3-yl]sulfanyl}-N-(4-isopropylphenyl)acetamide (Chen and Luetje, 2012), also known as VUAA-3 (Taylor et al., 2012). As previously demonstrated, OR-Orco complexes are more sensitive to activation by Orco agonists than are the Orco homomers (Chen and Luetje, 2012; Chen and Luetje, 2013; Choo et al., 2018; Hughes et al., 2017; Chen and Luetje, 2014). It is, therefore, conceivable that the complexes (Figure 8—figure supplement 1A, B) were expressed but the binding sites were defective.

On the other hand, CquiOR10A73G/CquiOrco-expressing oocytes showed the same skatole specificity as the wildtype receptor (Figure 8—figure supplement 1C). Interestingly, skatole elicited stronger currents recorded from CquiOR10A73G than the wildtype receptor CquiOR10 (Figure 8—figure supplement 2), further implying a higher affinity for skatole when there is a reduced constraint, or increased volume, of the binding pocket.

Since CquiOR2 is homologous to CquiOR10, we also propose that our space constraint structural hypothesis can be applied to CquiOR2. CquiOR2 has 49.5% sequence identity and 71.7% sequence similarity to CquiOR10. CquiOR2 also has physiochemically matched pairs to CquiOR10 residues speculated to form contacts with skatole/indole in our study (Supplementary file 1, Table 17). While we did not perform CquiOR2 docking, we indirectly examined space constraints in CquiOR2 by mutating Leu-74 to Ile, Val, or Gly. We then tested oocytes co-expressing CquiOrco with CquiOR2L74I, CquiOR2L74V, or CquiOR2L74G (Figure 8—figure supplement 1D–F). Consistent with the relaxation of the space constraints, CquiOR2L74I retained the specificity of the wildtype receptor to indole, whereas CquiOR2L74G showed a reverse specificity profile (Figure 8—figure supplement 1F), that is, more robust response to skatole than indole. Interestingly, CquiOR2L74V/CquiOrco-expressing oocytes generated nearly equal, albeit small, currents when stimulated with the two oviposition attractants (skatole, 8.7 ± 2.7 nA; indole, 9.0 ± 2.5 nA at 100 µM; n = 3, p>0.9999, Wilcoxon matched-pairs signed-rank test).

Next, we tested the space constraints hypothesis with a bulkier ligand, 3-ethylindole. A CquiOR10 mutant with a less space-filling residue, CquiOR10A73G, elicited responses to 3-ethylindole (526 ± 110 nA) higher than the responses to indole (205 ± 81 nA, at 100 µM), although less robust than the skatole responses (1939 ± 142 nA; all at 100 µM) (Figure 9—figure supplement 1). By contrast, receptors with a bulkier residue (CquiOR2WT, CquiO10A73L, and CquiOR2L74I) did not respond to 3-ethylindole (Figure 9). However, CquiOR2 mutant with less space-filling residues, CquiOR2L74A and CquiOR2L74G, responded to 3-ethylindole in a dose-dependent manner (Figure 9). Additionally, CquiOR10A73G elicited dose-dependent strong responses to 3-ethylindole than CquiOR10 (Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig9-v2.jpg)

**Figure 9.:** Bars represent SEM (n = 4–10).

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/82922/elife-82922-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** (A) Representative trace recorded after challenging an oocyte with the three odorants at the same dose (100 µM). (B) Quantification of responses from six different oocytes. Columns with the same letter are not significantly different (Repeated measures, one-way ANOVA).

In summary, the findings that a bulkier, non-natural ligand, elicited more robust responses when CquiOR10 and CquiOR2 residues at 73 and 74, respectively, were mutated into Gly are consistent with the space constraints hypothesis.

## Discussion

Our mutation studies demonstrated that a single amino acid residue substitution in two narrowly tuned ORs from the southern house mosquito can revert their specificity to the oviposition attractants skatole and indole. Amino acid residues leading to one-way alterations of insect ORs have been previously reported (Auer et al., 2020; Cao et al., 2021; Hughes et al., 2014; Leary et al., 2012; Pellegrino et al., 2011; Yang et al., 2017; Yuvaraj et al., 2021). Here, we demonstrated that switching a single amino acid residue in two mosquito ORs reverses the specificity of these receptors to two physiologically and ecologically significant odorants. Understanding how mosquito odorant receptors detect oviposition attractants may lead to the development of potent lures. Trapping female that already had a blood meal is an invaluable tool for surveillance given that these gravid females are likely to carry virus circulating in an area.

It has been proven challenging to obtain cryo-EM structure of insect ORs. Hitherto, the only experimentally solved structures of insect receptors are AbakOrco, a co-receptor from the parasitic fig wasp, A. bakeri (Butterwick et al., 2018), and MhraOR5, an OR from the jumping bristle, M. hrabei (DelMarmol et al., 2021). While structures of ORs from more evolved winged insects (Pterygota) are yet to be experimentally determined, the most accurate structural modeling methods, such as Rosetta, RoseTTAFold, and AlphaFold, allow us to get a better understanding on how these receptors interact with ligands. Here, we obtained unambiguous experimental evidence that Ala-73 plays a crucial role in CquiOR10 specificity to skatole. We then resorted to modeling to put forward structural hypotheses that can be tested using available experimental approaches and validated by high-resolution structures in the future. Using RoseTTAFold and AlphaFold, we generated models of CquiOR10 followed by RosettaLigand docking of skatole and indole to generate structural hypotheses (Figure 6, Figure 7, Figure 7—figure supplements 1–8). RoseTTAFold (Baek and Baker, 2022) and AlphaFold (Jumper et al., 2021) are highly accurate and state-of-the-art tools for protein structure prediction. On the other hand, RosettaLigand (Davis and Baker, 2009, DeLuca et al., 2015) is a competitive protein docking method (Smith and Meiler, 2020) that has been used previously to predict the binding position of ligands within protein pores (Craig et al., 2020; Nguyen et al., 2017; Nguyen et al., 2019; Pressly et al., 2022). Of note, a structure of an OR-Orco heterocomplex has yet to be elucidated. It has been postulated that they adopt the same overall architecture as the Orco homomeric channel (Butterwick et al., 2018), with one or more Orco subunits being replaced by an OR. Additionally, the structure of the ‘stand alone’ MhraOR5 is remarkably similar in the fold of the helical subunits and the quaternary structure formed by the four subunits within the membrane plane (DelMarmol et al., 2021). Therefore, it is reasonable to assume that ligand–receptor interactions analyzed with homomers reflect the same interactions with heteromers.

RoseTTAFold modeling and RosettaLigand docking studies suggest that the specificity determinant amino acid residue (Ala-73) did not form direct contacts with ligands but rather provided a finely tuned, sensitive volumetric space to accommodate odorants. Interpreting CquiOR10-A73L as an expanded space is counterintuitive compared with our oocyte recordings; the wild-type CquiOR10 receptor responded better to the bulkier skatole (Figure 1A), while CquiOR10-A73L responded better to the smaller indole (Figure 2I).

Considering both experimental and modeling data, the reason for differing receptor responses at residue 73 could be due to the repacking of this position to accommodate more carbon sidechain atoms that are reducing the binding pocket volume, or shift key, nearby residues required for receptor response. The fact that indole is a rigid molecule, and that the methyl group of skatole is the only rotamer, could also suggest that the binding pocket around position 73 is tightly regulated. The addition of a methyl group could prevent skatole from occupying the appropriate configuration for receptor response with Leu-73 constrained volume (Appendix 4). Combined, our results suggest that the residue at 73 provides a finely tuned volumetric space to accommodate specific oviposition attractants. Future structures can test the space constraints hypothesis proposed here by validating the specific residues interacting with odorants, quantifying the binding pocket volume, and providing structural insight into how position 73 modulates receptor response to specific odorants.

Taken together, our findings shed light on a possible path to design more potent oviposition attracts to trap mosquitoes, which may pave the way to novel strategies for vector-borne virus surveillance and, possibly, mosquito control.

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
      <td>Recombinant DNA reagent</td>
      <td>Stellar competent cell</td>
      <td>Takara Bio, USA (San Jose, CA)</td>
      <td>Cat# 636766</td>
      <td>https://bit.ly/3Dowpe2</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pGEMHE (plasmid)</td>
      <td>Liman et al., 1992</td>
      <td>https://doi.org/10.1016/0896-6273(92)90,239a</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Xenopus oocytes</td>
      <td>EcoCyte Bioscience (Austin, TX)</td>
      <td>https://bit.ly/3Ud8OTo</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>XmaI</td>
      <td>New England Biolabs (Ipswich, MA)</td>
      <td>Cat# R0180S</td>
      <td>https://www.neb.com/products/r0180-xmai</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>XbaI</td>
      <td>New England Biolabs (Ipswich, MA)</td>
      <td>Cat# R0145S</td>
      <td>https://www.neb.com/products/r0145-xbai</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Gentamycin sulfate</td>
      <td>Abcam (Cambridge, UK)</td>
      <td>Cat# ab146573</td>
      <td>https://www.abcam.com/ab146573.html</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NaCl</td>
      <td>Fisher Scientific (Waltham, MA)</td>
      <td>Cat# S271-3</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KCl</td>
      <td>Fisher Scientific (Waltham, MA)</td>
      <td>Cat# P217-500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NaHCO3</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>Cat# S6014-500G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MgSO4</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>Cat# M-7634</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Ca(NO3)2</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>Cat# 237124-500G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CaCl2</td>
      <td>Fisher Scientific (Waltham, MA)</td>
      <td>Cat# S71924</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HEPES</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>Cat# H4034-500G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>OLC12</td>
      <td>Vanderbilt Institute of Chemical Biology</td>
      <td>Chemical Synthesis Core, VUAA 3</td>
      <td>https://medschool.vanderbilt.edu/syncore/</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Skatole</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 83-34-1, Cat# W301912</td>
      <td>98%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Indole</td>
      <td>ACROS Organics (Geel, Belgium)</td>
      <td>CAS# 120-72-9, Cat# 122150100</td>
      <td>98%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3-Ethylindole</td>
      <td>AmBeed (Arlington hts, IL)</td>
      <td>CAS# 1484-19-1, Cat# AMBH96F1079C</td>
      <td>97%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phenol</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 108-95-2</td>
      <td>99.5%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3,5-Dimethylphenol</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 108-68-9</td>
      <td>99%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-Methylindole</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 603-76-92</td>
      <td>97%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-Methylindole</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 95-20-5</td>
      <td>98%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4-Methylindole</td>
      <td>ACROS Organics (Geel, Belgium)</td>
      <td>CAS# 16096-32-5</td>
      <td>99%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>5-Methylindole</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 614-96-0</td>
      <td>99%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>6-Methylindole</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 3420-02-8</td>
      <td>97%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>7-Methylindole</td>
      <td>Sigma-Aldrich (Milwaukee, WI)</td>
      <td>CAS# 933-67-5</td>
      <td>97%</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>Pettersen et al., 2004</td>
      <td>https://doi.org/10.1002/jcc.20084; UCSF</td>
      <td>https://bit.ly/3S7OdOF; ver. 1.15</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Rosetta</td>
      <td>Leman et al., 2020</td>
      <td>https://doi.org/10.1038/s41592-020-0848-2</td>
      <td>https://www.rosettacommons.org/software/license-and-download; ver 2021.07.61567</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Avogadro</td>
      <td>Hanwell et al., 2012</td>
      <td>https://doi.org/10.1186/1758-2946-4-17</td>
      <td>https://avogadro.cc/; ver 1.2.0 (Git revision: c1fcc5b)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>AmberTools</td>
      <td>Case et al., 2021</td>
      <td>https://ambermd.org/index.php</td>
      <td>https://ambermd.org/doc12/Amber21.pdf</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OpeneEye Omega</td>
      <td>Hawkins et al., 2010</td>
      <td>https://doi.org/10/1021/ci100031x</td>
      <td>https://www.eyesopen.com/omega</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HDBSCAN</td>
      <td>McInnes et al., 2017</td>
      <td>https://doi.org/10.21105/joss.00205</td>
      <td>https://github.com/scikit-learn-contrib/hdbscan; McInnes and Healy, 2017</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BioMol2Clust</td>
      <td>https://biokinet.belozersky.msu.ru/Biomol2Clust</td>
      <td>Timonina et al., 2021</td>
      <td>ver 1.3</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Protein Ligand Interaction Profiler</td>
      <td>Salentin et al., 2015</td>
      <td>https://doi.org/10.1093/nar/gkv315</td>
      <td>https://plip-tool.biotec.tu-dresden.de/plip-web/plip/index; software repository: https://github.com/pharmai/plip; ver 2.2.1, Salentin et al., 2015</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EMBOSS Needle</td>
      <td>Madeira et al., 2022</td>
      <td>https://doi.org/10.1093/nar/gkac240</td>
      <td>https://www.ebi.ac.uk/Tools/psa/emboss_needle/</td>
    </tr>
  </tbody>
</table>

### Construction of chimeric receptors

We used a previously obtained pGEMHE-CquiOR10 (Hughes et al., 2010) plasmid to amplify the sequences of the desired chimeric receptors. To obtain the full length of chimeric OR genes, we used specific primers, with overlapping sequences at each end to target sequences (adaptor underlined) for cloning into pGEMHE vector, which was linearized at restriction sites XmaI (5′-CCCGGG-3') and XbaI (5′-TCTAGA-3'):CqOR10_Fw 5′-GATCAATTCCCCGGGACCATGACCGCGGCACCCATTTT-3' and CqOR10_Rv 5′-CAAGCTTGCTCTAGATCAATTATAAACGCGTCTCAGCAGGGT-3'. To generate a chimeric OR by PCR amplification, we designed specific primers for the desired CquiOR2 TM domain. Simultaneously, we prepared the recipient fragments of CquiOR10 to receive the CquiOR2 TM domains. The fragments were then assembled using In-Fusion HD cloning kit (Clontech) to obtain the desired chimeric OR. Each CquiOR2 TM domain was divided into two parts, each part was synthesized with a specific primer, except for CquiOR2 TM7 domain, which used only one primer with the full domain. These primers contained an overlap with CquiOR10 sequence followed by one part of the CquiOR2 TM sequence and an overlap with the other part of the CquiOR2 TM domain sequence, which was synthesized in another PCR. The underlined sequences represent CquiOR2 TM domains and, unless otherwise specified, sequences in italic are overlaps for CquiOR2 TM domains. CqOR10M1_Fw: 5′-GGTGACCGTGCTGAACGTGTTCCAGTTTATGAACCTGTTTCGAGCCTGGGGCAACATC-3′; CqOR10M1_Rv: 5′-TCAGCACGGTCACCGGAATGCAGCCGAGGAGGTAACTGAGGACGTTGCCTACTGTGATCTCAAGG-3′; CqOR10M2_Fw: 5′-CCGTGCTGTACTTCAACCTTGTGTTGAGAACCACGTTTATACTGTGCAATCGTCAGGATTATGAGG-3′; CqOR10M2_Rv: 5′- AAGTACAGCACGGTGAAATATCCGTCGATGATGATTTTGTCGATGTTGCCCCAGGCT-3′; CqOR10M3_Fw: 5′- GTTCATCAGTGCGTGCTTCGTGACGTATCCGCTTTTTTCACCGACACGTAGCCTCCCGTACG-3′; CqOR10M3_Rv: 5′- ACGCACTGATGAACGCTCCCAGCCAGAGGTTCGATTTGGACAGCAGTCGGGCACGTTTGGTGA-3′; CqOR10M4_Fw: 5′- CACGTTTCCGGCGTGCTGCATGTACATTCCGTTTACCAGCTTCTTCGCCACGACTACTTTG-3′; CqOR10M4_Rv: 5′- ACGCCGGAAACGTGAGGTACACTTGCAGAAAAAACACAACCTGGTACAGGGGCGTC-3′; CqOR10M5_Fw: 5′- GCTATGCGCCTTGCTGTTTCTACTTAGCACCAGCAATAATCCCGCGCAAATTATCATCGTGG-3′; CqOR10M5_Rv: 5′- GCAAGGCGCATAGCATCATCCCAAACGATAGCAACTCAATCAGACAGATGTAGGTCACCAGCG-3′; CqOR10M6_Fw: 5′- TCTTTATGATTCTGTCCCAGATGTACGCCCTGTACTGGCACGCCAACGAGCTGCG-3′; CqOR10M6_Rv: 5′- AGAATCATAAAGATGTACGATCCGATCATCACCATCTGCGCGGGATTTTCGATAATGTTCAGC-3′; CqOR10M7_Rv: 5′- CAAGCTTGCTCTAGATCAATTATAAACGCGTCTCAGCAACGTAAAGTACGAATACGAGGCATTGATCAACTTTTGAAACATTTCCAAGGTCATCGGATAGACGTTGCCTACTGTGATCTCAAGG-3′ (here the italic represents the pGEMHE adaptor). The two fragments were amplified using a combination of CqOR10_Fw with CqOR10Mx_Rv primers and CqOR10_Rv with CqOR10Mx_Fw primers. Then, we cloned the two fragments amplified by PCR into pGEMHE vector using the In Fusion system as described below. Chimeric plasmid with a single TM swapped was used as a template to generate chimeric OR with two TM swapped and subsequently chimeric ORs with multiple CquiOR2 TM domains.

### Chimeric OR cloning and subcloning into pGEMHE

The fragments amplification was performed using Platinum Taq DNA Polymerase High Fidelity (Thermo Fisher Scientific) with the following conditions: 95°C for 5 min, followed by 30 cycles of 95°C for 20 s, 57°C 30 s for annealing and 68°C for 1.5 min, and extension at 68°C for 5 min. PCR products were purified by QIAquick gel extraction kit (QIAGEN). The target pGEMHE plasmid was cut by XmaI and XbaI in separate reactions. Ligation was done with In Fusion (Takara Bio USA) system and the transformation was performed using Stellar competent cells (Takara Bio USA) in heat-shock. After selecting the cells, plasmids were extracted with QIAprep Spin Miniprep kit (QIAGEN). The cloned gene was verified by DNA sequencing (Berkeley Sequencing Facility).

### Site-directed point mutagenesis and fragment replacement

Phusion Site-Directed Mutagenesis Kit (Thermo Scientific, West Palm Beach, FL) was used to generate point mutations and TM fragment replacements. Mutations were created with mismatched 5′-phosphorylated mutagenic primers and PCR amplification. The chimeric sequences (CquiOR10M2,5,6,7) in pGEMHE vector were used as templates for rescues, whereas the wildtype sequences in pGEMHE vector served as templates for point-mutations. Rescue primers: CqOR10M2_M2567OUTERup: 5′-GATGATGACCTCGTCGATGTTGCCCCAGGC-3′; CqOr10M2_M2567OUTERdn: 5′-AACGCATATTTCACCGTGCTGTACTTCAACC-3′; CqOr10M2_M2567INNERup: 5′-cgcagcaccgcgttgaagtacagcacggtg-3′; CqOr10M2_M2567INNERdn: 5′-aacaattttcatactgtgcaatcgtcagga-3′; CqOR10M2_M2567MID-INNERup: 5′-catcgacggCtactttgcgatgattttcttcaacgcg-3′; CqOR10M2_M2567MID-INNERdn: 5′-atgattttgtcgatgttgccccaggctc-3′; CqOr10M2_M2567_L73Aup: 5′-CGTTGAAGTACAGCACGGTGAAATAT-3′; CqOr10M2_M2567_L73Adn: 5′-CTGTGTTGAGAACCACGTTTATACTGT-3′; CqOr10M2_M2567_T78Iup: 5′-ATGGTTCTCAACACAAGGTTGAAGTA-3′; CqOr10M2_M2567_T78Idn: 5′-CTTTATACTGTGCAATCGTCAGGATTATG-3′; point mutation primers: CqOR10A73up: 5′-Gttgaagaaaatcatcgcaaagta-3′; CqOR10A73Ldn: 5′-Ctggtgctgcgaacaattttc-3′; CqOR10A73Adn: 5′-Gcggtgctgcgaacaattttc-3′; CqOR10A73Gdn: 5′-Ggggtgctgcgaacaattttc-3′; CqOR10A73Vdn: 5′-Gtggtgctgcgaacaattttc-3′; CqOR10A73Idn: 5′-ATCgtgctgcgaacaattttc-3′; CqOR2L74up: 5′-gttgaagtacagcacggtgaaata-3′; CqOr2L74Adn: 5′-Gctgtgttgagaaccacgtttatac-3′; CqOr2L74Idn: 5′-atcGTGTTGAGAaccacgtttatac-3′; CqOr2L74Gdn: 5′-gggGTGTTGAGAaccacgtttatac-3′; CqOr2L74Vdn: 5′-gtgGTGTTGAGAaccacgtttatac-3′. The amplified linear PCR products containing the desired modification were ligated and transformed into Stellar Competent Cells (Takara Bio USA). All sequences were confirmed by DNA sequencing (UC Berkeley DNA Sequencing Facility).

### In vitro transcription, oocyte microinjection, and two-electrode voltage-clamp assay (TEVC)

Capped OR cRNA was prepared using mMESSAGE mMACHINE T7 Kit (Ambion) as previously described (Xu et al., 2019). Purified OR cRNA was resuspended in nuclease-free water at 200 ng/μL and microinjected into Xenopus laevis oocytes on stage V or VI (EcoCyte Bioscience) along with the same amount of CquiOrco. Injected oocytes were incubated at 18°C for 3–7 days in a modified Barth’s solution (88 mM NaCl, 1 mM KCl, 2.4 mM NaHCO3, 0.82 mM MgSO4, 0.33 mM Ca(NO3)2, 0.41 mM CaCl2, and 10 mM HEPES at pH 7.4) supplemented with 10 μg/mL gentamycin, 10 μg/mL streptomycin, and 1.8 mM sodium pyruvate. Two-electrode voltage-clamp technique (TEVC) was used to measure odorant-induced currents at a holding potential of −80 mV. Signals were amplified with an OC-725C amplifier (Warner Instruments), low-pass filtered at 50 Hz, and digitized at 1 kHz. Data acquisition and analysis were performed with Digidata 1440A and software pCLAMP 10 (Molecular Devices). Skatole (98%, CAS# 83-34-1), indole (98%, CAS# 120-72-9), and 3-ethylindole (97%, CAS# 1484-19-1) were provided by Sigma-Aldrich (Milwaukee, WI), ACROS Organics (Geel, Belgium), and AmBeed (Arlington Hts, IL), respectively. Phenol (99.5%, CAS# 108-95-2), 3,5-dimethylphenol (99%, CAS# 108-68-9), 1-methylindole (97%, CAS# 603-76-9), 2-methylindole (98%, CAS# 95-20-5), 5-methylindole (99%, CAS# 614-96-0), 6-methylindole (97%, CAS# 3420-02-8), and 7-methylindole (97%, CAS# 933-67-5) were acquired from Sigma-Aldrich, and 4-methylindole (99%, CAS# 16096-32-5) was provided by ACROS.

### Rosetta structural modeling and docking

We used RoseTTAFold (Baek et al., 2021) and AlphaFold (Jumper et al., 2021) to generate predicted structures of CquiOR10, CquiOR2, CquiOR10A73L, and CquiOR2L74A monomers. The OpenEye Omega toolkit (Hawkins et al., 2010) was used to generate conformer libraries. Molecular docking was performed using RosettaLigand (Davis and Baker, 2009; DeLuca et al., 2015). The top models were visually analyzed using UCSF Chimera (Pettersen et al., 2004).

To verify RosettaLigand could effectively sample homologous receptors in complex with odorants, we used the structure of eugenol in complex with the insect olfactory receptor OR5 from M. hrabei (MhraOR5) as a control test case (DelMarmol et al., 2021). After verifying RosettaLigand could recapitulate the MhraOR5–eugenol complex from structural studies, we docked indole and skatole to the RoseTTAFold monomer models of CquiOR10 and CquiOR10A73L receptors with the same method. Briefly, the initial placement of all ligands into respective structures was guided by the position of eugenol in a complex with MhraOR5 as a basis since it is the only homologous structure with an odorant. For an unbiased receptor sampling, an initial transformation was performed on the ligand relative to the receptor site using Rosetta’s Transform mover. Within a 7 Å sphere, the ligand underwent a Monte Carlo simulation, whereby the ligand was allowed to translate up to 0.2 Å and rotate up to 20°. This was performed 500 times on the ligand, with the lowest scoring pose used as the starting pose for docking. This form of docking is termed local docking and is commonplace when there is experimental evidence and homologous structures as templates. physiologically relevant binding modes can be identified with local, high-resolution ligand docking (Kaufmann et al., 2009). For additional methods, see Appendix 2.
