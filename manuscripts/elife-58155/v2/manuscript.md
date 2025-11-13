# Identification of ubiquitin Ser57 kinases regulating the oxidative stress response in yeast

## Authors

- Nathaniel L Hepowit<sup>1</sup> ([ORCID: 0000-0002-7614-2756](https://orcid.org/0000-0002-7614-2756))
- Kevin N Pereira<sup>1</sup> ([ORCID: 0000-0001-5377-397X](https://orcid.org/0000-0001-5377-397X))
- Jessica M Tumolo<sup>1</sup>
- Walter J Chazin<sup>2</sup> ([ORCID: 0000-0002-2180-0790](https://orcid.org/0000-0002-2180-0790))
- Jason A MacGurn<sup>1</sup> ([ORCID: 0000-0001-5063-259X](https://orcid.org/0000-0001-5063-259X)) †

### Affiliations

1. Department of Cell and Developmental Biology, Vanderbilt University Nashville United States
2. Department of Biochemistry, Vanderbilt University Nashville United States

† Corresponding author

## Abstract

Ubiquitination regulates many different cellular processes, including protein quality control, membrane trafficking, and stress responses. The diversity of ubiquitin functions in the cell is partly due to its ability to form chains with distinct linkages that can alter the fate of substrate proteins in unique ways. The complexity of the ubiquitin code is further enhanced by post-translational modifications on ubiquitin itself, the biological functions of which are not well understood. Here, we present genetic and biochemical evidence that serine 57 (Ser57) phosphorylation of ubiquitin functions in stress responses in Saccharomyces cerevisiae, including the oxidative stress response. We also identify and characterize the first known Ser57 ubiquitin kinases in yeast and human cells, and we report that two Ser57 ubiquitin kinases regulate the oxidative stress response in yeast. These studies implicate ubiquitin phosphorylation at the Ser57 position as an important modifier of ubiquitin function, particularly in response to proteotoxic stress.

## Introduction

Ubiquitin is a post-translational modifier that regulates diverse cellular processes in eukaryotic cells. The broad utility of ubiquitin as a regulatory modification is due to the high degree of complexity associated with ubiquitin polymers, which are added to substrate proteins by the activity of ubiquitin conjugation machinery (E1-E2-E3 cascades) and removed from substrates by deubiquitylases (DUBs). Ubiquitin can be conjugated recursively at any of seven internal lysines or the N-terminus to generate polymers with distinct topological features (Herhaus and Dikic, 2015; Yau and Rape, 2016; Swatek and Komander, 2016). Complexity is further enhanced by the formation of mixed and branched polymers (Ohtake et al., 2018; Meyer and Rape, 2014; Swatek et al., 2019) and by post-translational modifications that can occur on ubiquitin itself (Herhaus and Dikic, 2015). For example, PINK1-mediated phosphorylation of ubiquitin at the Ser65 position plays an important role in mitophagy by regulating parkin-mediated ubiquitination of mitochondrial membrane proteins (Wauer et al., 2015; Ordureau et al., 2015; Koyano et al., 2014; Kazlauskaite et al., 2014; Kane et al., 2014; Ordureau et al., 2014). Phosphorylation of ubiquitin at the Ser57 has also been reported (Peng et al., 2003; Swaney et al., 2015; Lee et al., 2017), but the kinases that produce this modification and its regulatory significance remain unknown.

Many proteotoxic stresses activate ubiquitin networks to promote protein quality control and protect the cell from damage associated with systemic protein misfolding. Oxidative stress is highly damaging to the cell, triggering deployment and re-distribution of existing ubiquitin pools and induction of ubiquitin biosynthesis to promote survival by activating a repertoire of ubiquitin-mediated responses (Cheng et al., 1994). During oxidative stress, many proteins become damaged and misfolded, resulting in a global increase in K48-linked ubiquitin conjugation that targets substrates for clearance by proteasome-mediated degradation (Finley, 2009; Shang and Taylor, 2011). Oxidative stress also triggers translation arrest (Grant, 2011), resulting in K63-linked polyubiquitylation on ribosomes to stabilize the 80S complex and the formation of polysomes (Silva et al., 2015). Furthermore, oxidative damage of DNA activates signaling and repair processes that are tightly regulated by K63 ubiquitylation and deubiquitylation activities (Demple and Harrison, 1994; Bergink and Jentsch, 2009; Ng et al., 2016; Croteau and Bohr, 1997; Thorslund et al., 2015). Thus, ubiquitin networks regulate many cellular processes critical for survival during conditions of oxidative stress.

Although ubiquitin networks play a critical role in the eukaryotic cellular response to proteotoxic stress, precisely how these networks are tuned to enhance protein quality control and other protective functions remain unclear. Given that Ser65 phosphorylation of ubiquitin regulates the clearance of damaged mitochondria (Wauer et al., 2015; Ordureau et al., 2015; Koyano et al., 2014; Kazlauskaite et al., 2014; Kane et al., 2014; Ordureau et al., 2014), we hypothesized that phosphorylation at other positions may regulate ubiquitin function, particularly in conditions that promote protein damage and misfolding. Since it is the most abundant phosphorylated form (Swaney et al., 2015), we examined the biological functions of Ser57 phosphorylated ubiquitin in yeast, aiming to identify and characterize the molecular events and signaling processes that regulate its production.

## Results

To probe potential biological functions of Ser57 ubiquitin phosphorylation in yeast, we generated yeast strains expressing exclusively wildtype, Ser57Ala (phosphorylation resistant, or S57A) or Ser57Asp (phosphomimetic, or S57D) ubiquitin. It is important to emphasize that such complete ubiquitin replacement may exaggerate effects associated with physiological ubiquitin phosphorylation, which occurs at very low stoichiometry (Swaney et al., 2015; Lee et al., 2017) and probably in a highly localized manner (as exemplified by PINK1-mediated Ser65 phosphorylation of ubiquitin on damaged segments of mitochondrial membrane [Pickrell and Youle, 2015]). With these limitations in mind, we examined the growth of these yeast strains in the context of various stressors, including heat stress, DNA damage and replication stress (hydroxyurea and arsenate), and protein misfolding stress (canavanine and thialysine, which are toxic analogs of arginine and lysine, respectively). We found that expression of S57A or S57D ubiquitin did not affect growth at ambient temperature (26°C) (consistent with previous reports [Peng et al., 2003; Lee et al., 2017; Sloper-Mould et al., 2001]) or sensitivity to arsenate (Figure 1A). However, expression of S57D ubiquitin conferred sensitivity to hydroxyurea and resistance to canavanine (which was reported previously [Lee et al., 2017]) and thialysine (Figure 1A). We also noticed that expression of S57D ubiquitin enhanced both long-term and acute tolerance of thermal stress (Figure 1B–D) while yeast expressing S57A ubiquitin exhibited thermal sensitivity (Figure 1E and Figure 1—figure supplement 1). These findings indicate that Ser57 phosphorylation of ubiquitin promotes cellular tolerance of various proteotoxic stressors.

![Figure 1.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig1-v2.jpg)

**Figure 1.:** Ubiquitin variants were shuffled into the SUB280 yeast background (as described in the Materials and Methods) to generate strains that express exclusively wildtype, S57A, or S57D ubiquitin. (A) Yeast strains expressing the indicated ubiquitin variants (wildtype, S57A or S57D) were plated in serial dilutions onto the indicated synthetic dextrose medium (SDM) agar plates. (B) Serial dilutions of yeast cells were plated onto YPD agar plates and incubated at 26°C, 37°C, or 39°C for 18 hr and shifted back to 26°C for recovery. (C) Fluorescence microscopy and (D) quantification of cells stained with propidium iodide (PI) after incubation at 65°C for 5 min. Dead cells are stained with PI. Results are means (n = 3) of % PI-positive cells ± SD (error bars). Double asterisk (**) indicates p value < 0.005 using a Student’s t-test. (E) With a starting OD600 of 0.1, cells were grown in liquid culture (-URA synthetic medium) at 39°C and OD600 was measured at different time points. Data was collected from four biological replicate experiments (n=4) and the mean OD600 ± SD (error bars) was calculated for each time point. Double asterisk (**) indicates p value < 0.005 using a Student’s t-test. For all statistical analysis associated with Figure 1, p values are reported in the Figure 1—source data 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Cells in liquid culture (-URA synthetic medium) were grown at 38°C with a starting OD600 of 0.1 and growth was measured after 24 hr of incubation. Values are means of OD600 from three replicates (n = 3) ± SD (error bars). Double asterisk (**) indicates p value < 0.005 using a Student’s t-test. For all statistical analysis associated with this figure supplement, p values are reported in the Figure 1—source data 1.

Next, we analyzed the role of Ser57 phosphorylation in the oxidative stress response. Wildtype yeast cells arrest growth in response to oxidative stress and activate responses that help cells cope with the proteotoxic and DNA damaging effects of oxidation (Silva et al., 2015; Shapira et al., 2004; Petti et al., 2011; Martindale and Holbrook, 2002). Interestingly, while yeast cells expressing wildtype or S57D ubiquitin arrested growth in response to moderate oxidative stress (>1 mM H2O2), cells expressing S57A ubiquitin were deficient in this response and only arrested growth in response to more severe oxidative stress (>2 mM H2O2) (Figure 2A). The failed growth arrest observed for cells expressing S57A ubiquitin correlated with decreased viability (Figure 2B). Since oxidative stress induces the production of both K48- and K63-linked ubiquitin conjugates (Shang and Taylor, 2011; Silva et al., 2015; Sun et al., 2009; Tsirigotis et al., 2001) we tested if the expression of S57A and S57D ubiquitin alters ubiquitin conjugation patterns in response to oxidative stress. We found that 30 min exposure to H2O2 (1.0 mM) resulted in an increased abundance of total ubiquitin conjugates (Figure 2C) as well as K48-linked polymers (Figure 2C–D), consistent with a previous report (Silva et al., 2015). Compared to cells expressing wildtype ubiquitin, we found that cells expressing S57D ubiquitin exhibited increased abundance of K48-linked polymers and decreased abundance of K63-linked polymers (Figure 2C–E). By contrast, cells expressing S57A ubiquitin did not exhibit a significant increase in the production of K48-linked polyubiquitin chains in response to oxidative stress (Figure 2C–D). Since substitutions at the Ser57 position of ubiquitin (S57A, S57D) might interfere with the recognition of ubiquitin polymers by linkage-specific antibodies, we used SILAC-MS to analyze how the expression of phosphomimetic (S57D) ubiquitin affects ubiquitin polymer linkage abundance compared to wildtype ubiquitin during conditions of oxidative stress. Consistent with the immunoblot results, this analysis revealed that S57D expression increases the production of K48-linked polymers by 39% during oxidative stress (Figure 2—figure supplement 1 and Supplementary file 1). (Notably, K63-linked polymers are a blind spot of this analysis, since the K63-linked ubiquitin remnant peptide also harbors the Ser57 position which is mutated to Asp in the light channel of this experiment.) It is worth noting that complete ubiquitin replacement in these cells exaggerates the impact physiological phosphorylation of ubiquitin is likely to have on global poly-ubiquitin linkage abundance. Indeed, we found that oxidative stress induced an approximately two-fold increase in phosphorylation of ubiquitin at the Ser57 position (Figure 2F and Figure 2—figure supplement 2). Based on previous measurements (Swaney et al., 2015; Lee et al., 2017), this stress-induced ubiquitin phosphorylation remains sub-stoichiometric and may have localized effects but is unlikely to alter global poly-ubiquitin linkage patterns. Ultimately, a deeper understanding of how Ser57 phosphorylated ubiquitin contributes to cellular stress responses will require the identification and characterization of the kinases that produce it.

![Figure 2.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig2-v2.jpg)

**Figure 2.:** (A) OD600 of yeast cells cultured in YPD with different concentrations of H2O2 for 48 hr (starting OD600 = 0.025). Data was collected for four biological replicate experiments (n=4) and the means ± SD (error bars) were calculated. Double asterisk (**) indicates p value < 0.005 between the range of 0.5 mM to 2.5 mM H2O2 using a Student’s t-test, which was only observed for yeast expressing S57A ubiquitin. (B) CFU count of cells treated with 1.5 mM H2O2 for 20 min. Untreated control was taken before H2O2 treatment. Data was collected for three bioloigcal replicate experiments (n = 3) and the means ± SD (error bars) were calculated. Double asterisk (**) indicates p value < 0.05 comparing untreated to H2O2 treated cells using a Student’s t-test, which revealed that only yeast expressing S57A ubiquitin experienced a significant loss of viability during H2O2 treatment in this experiment. (C) Western blot with anti-ubiquitin, anti-K48 ubiquitin, and anti-K63 ubiquitin antibodies of lysates from cells treated with 1 mM H2O2 for 30 min. (D and E) Quantification of results from the experiment shown in (C) is presented as the mean of four biological replicate experiments (n = 4) ± SD (error bars). Double asterisk (**) indicates p value < 0.005 comparing untreated to H2O2 treated cells using a Student’s t-test. Correspondingly, p values > 0.05 are labeled as not significant (n.s.). Cells used in A-E are SUB280-derived strains exclusively expressing WT, S57A, or S57D ubiquitin variants. (F) SILAC-MS of affinity purified 3XFLAG-ubiquitin from yeast cells (JMY1312) treated with 0.6 mM H2O2 for 30 minutes. The peptide corresponding to Ser57 phosphorylation is colored red, while peptides corresponding to K48- and K11-linked poly-ubiquitin are colored blue and green, respectively. All other ubiquitin-derived peptide measurements are represented with black dots. All individual measurements and p values derived from statistical tests associated with the data in this figure are reported in Figure 2—source data 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The left panel shows the chromatography of the heavy and light peptides, while the right panel shows the fragmentation pattern which confirms the identity of the peptide. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Cells were grown in SILAC media (supplemented with light or heavy lysine and arginine) to the mid-log phase (OD600 of 0.6–0.7) and treated with 0.6 mM H2O2 for 30 min. Chromosomally expressed 3xFLAG-tagged ubiquitin (from the RPS31 and RPL40B loci) was isolated by affinity purification and digested with trypsin. Phosphopeptides were enriched by immobilized metal affinity chromatography (IMAC), separated by a capillary reverse-phase analytical column, and analyzed on a Q Exactive mass spectrometer. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

To identify candidate ubiquitin kinases, we screened for Ser57 phosphorylation activity by co-expressing ubiquitin and yeast kinases in E. coli and immunoblotting lysates using an antibody specific for Ser57 phosphorylated ubiquitin. Initially, we focused on candidate kinases for which mutants exhibit phenotypes corresponding to those observed for cells expressing S57A or S57D ubiquitin. We found that co-expression of ubiquitin with the kinase Vhs1 resulted in immunodetection of Ser57 phosphorylated ubiquitin (Figure 3A and Figure 3—figure supplement 1). Vhs1 is part of the yeast family of Snf1-related kinases (Tumolo et al., 2020), and additional screening revealed three other kinases in this family that phosphorylated ubiquitin at the Ser57 position: Sks1 (which is 43% identical to Vhs1) (Figure 3B), Gin4 and Kcc4 (Figure 3—figure supplement 2). A previous study reported consensus phosphorylation motifs for Vhs1, Gin4, and Kcc4, and all bear similarity to the amino acid sequence surrounding Ser57 in ubiquitin (Supplementary file 2; Mok et al., 2010).

![Figure 3.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-v2.jpg)

**Figure 3.:** (A) Anti-phospho-Ser57 western blot of E. coli Rosetta 2 (DE3) lysates co-expressing ubiquitin and yeast kinases. (B) Anti-phospho-Ser57 western blot of E. coli Rosetta 2 (DE3) lysates co-expressing ubiquitin (wildtype, S57A, or S65A variants) and Sks1, a paralog of Vhs1. (C and D) In vitro reconstitution of ubiquitin Ser57 phosphorylation using purified recombinant Vhs1 (C) and Sks1 (D). Ubiquitin monomers as well as linear (M1-linked) dimers and trimers were included in equal amounts. Numerical values above each lane represent reaction time for the sample. (E and F) SILAC-MS of IP-enriched 3XFLAG ubiquitin from yeast cells (JMY1312 background) with either empty vector or with vector for overexpression of Sks1 (E) or Vhs1 (F). Black and red dots indicate resolved ubiquitin peptides and Ser57-phosphopeptides, respectively. All individual measurements are reported in Figure 3—source data 1. (G) In vitro activity assay of select human kinases of the AMPK family using equal amounts of mono-ubiquitin and M1-linked tetra-ubiquitin as substrates.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** This is an extension of the results shown in Figure 3A.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp3-v2.jpg)

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Vhs1 and ubiquitin of yeast were co-expressed in E. coli Rosetta two by IPTG induction. Ubiquitin was isolated using UBD-capture pull-down, digested with trypsin, and analyzed on a Q Exactive mass spectrometer. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** In vitro kinase activity assay was carried out using purified recombinant Sks1 and tetra-ubiquitin as described in the Materials and methods. Total peptide digests of the reaction mixture were separated by reverse-phase capillary column and analyzed on a Q Exactive mass spectrometer. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** In vitro reconstitution assay was carried out by mixing recombinant Vhs1 (top) or Sks1 (bottom) and tetra-ubiquitin with different linkage types (M1, K6, K11, K29, K33, K48, K63) as described in the Materials and methods. Ser57 phosphorylation was detected by western blot using an anti-phospho-Ser57 ubiquitin antibody.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** Cells were grown in SILAC media supplemented with light or heavy lysine and arginine. Chromosomally expressed 3xFLAG-tagged ubiquitin (from the RPS31 and RPL40B loci) was isolated by affinity purification and digested with trypsin. Phosphopeptides were enriched by immobilized metal affinity chromatography (IMAC), separated by a capillary reverse-phase analytical column, and analyzed on a Q Exactive mass spectrometer. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp8-v2.jpg)

**Figure 3—figure supplement 8.:** Cells were grown in SILAC media supplemented with light or heavy lysine and arginine. Chromosomally expressed 3xFLAG-tagged ubiquitin (from the RPS31 and RPL40B loci) was isolated by affinity purification and digested with trypsin. Phosphopeptides were enriched by immobilized metal affinity chromatography (IMAC), separated by a capillary reverse-phase analytical column, and analyzed on a Q Exactive mass spectrometer. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp9-v2.jpg)

**Figure 3—figure supplement 9.:** For the experiments shown in Figure 3F, the phosphorylation of Vhs1 was detected. A schematic of Vhs1 domain structure is shown [top] with the identified phosphopeptides listed [inset table, bottom]. Amino acids critical for kinase catalytic function – including the conserved lysine critical for ATP binding (K41) and the conserved aspartic acid (D185) critical for catalytic activity – are labeled in red.

![Figure 3—figure supplement 10.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp10-v2.jpg)

**Figure 3—figure supplement 10.:** Select kinases of different superfamilies were used for in vitro kinase activity assays using tetra-ubiquitin. Ubiquitin phosphorylation at the Ser57 residue was determined by Western blot using anti-phospho-Ser57 ubiquitin antibody.

![Figure 3—figure supplement 11.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp11-v2.jpg)

**Figure 3—figure supplement 11.:** In vitro phosphorylation experiment was performed using recombinant GST-MARK2 and 6×His-tetra-Ub as described in the Materials and methods. Theoretical masses of b/y ions are tabulated and MS-observed masses are shown in the spectra.

![Figure 3—figure supplement 12.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp12-v2.jpg)

**Figure 3—figure supplement 12.:** Ubiquitin phosphorylation at the Ser57 residue was determined by Western blot using an anti-phospho-Ser57 ubiquitin antibody.

![Figure 3—figure supplement 13.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig3-figsupp13-v2.jpg)

**Figure 3—figure supplement 13.:** Sequence alignment and phylogenetic neighboring of kinase domains were analyzed by Clustal Omega (EMBL-EBI) and the circular rooted phylogram was constructed using iTOL. Yeast Ub kinases (Sks1, Vhs1, Gin4, and Kcc4) are shown in red.

We further characterized the activity of Vhs1 and Sks1. Analysis of Vhs1 and Sks1 activity using Phos-tag acrylamide gels (Figure 3—figure supplement 3) confirmed the production of Ser57 phosphorylated ubiquitin. Using purified recombinant Vhs1 and Sks1, we reconstituted kinase activity toward Ser57 of ubiquitin and found that both kinases exhibited a preference for polymers (tri-ubiquitin > di ubiquitin > mono ubiquitin) although the activity of Sks1 was noticeably greater than that of Vhs1 (Figure 3C–D and Figure 3—figure supplement 4–5). Analysis of linkage specificity in the phosphorylation reaction revealed that Vhs1 is active toward linear (M1-linked), K29-, and K48-linked tetramers, while Sks1 is active toward linear, K48-, and K63-linked polymers (Figure 3—figure supplement 6). These differences in linkage-specific activities in vitro may underlie non-overlapping functions for these two kinases in vivo. To test if the observed in vitro activity correlated with in vivo activity, we used SILAC to quantify changes to ubiquitin modifications following over-expression of Vhs1 or Sks1. Importantly, we observed that overexpression of either Vhs1 or Sks1 increased ubiquitin phosphorylation at the Ser57 position (Figure 3E–F and Figure 3—figure supplement 7–8). Interestingly, this analysis also revealed a number of phosphopeptides derived from Vhs1 within its kinase domain (Ser86) and its Ser-rich C-terminus (Figure 3—figure supplement 9), suggesting that Vhs1 itself may be subject to complex phospho-regulation. Taken together our data indicate that Vhs1 and Sks1 are bona fide ubiquitin kinases that specifically phosphorylate the Ser57 position.

The family of Snf1-related kinases in yeast share homology with the human AMPK-related kinases (Tumolo et al., 2020). To test if human AMPK-related kinases exhibit activity toward ubiquitin, we performed in vitro kinase assays and found that a subset of this family phosphorylated ubiquitin at the Ser57 position specifically on tetramers (Figure 3G). This activity was apparent in the MARK kinases (MARK1-4) as well as related kinases SIK1 and SIK2. It is noteworthy that other candidate human ubiquitin kinases (initially identified by commercial screening services) did not exhibit Ser57 ubiquitin kinase activity in vitro (Figure 3—figure supplement 10). Mass spectrometry analysis confirmed production of Ser57 phosphorylated ubiquitin by MARK2 in vitro (Figure 3—figure supplement 11). Further analysis of MARK2 activity toward linkage-specific ubiquitin tetramers revealed a preference for linear, K11-, K29-, and K63-linked tetramers (Figure 3—figure supplement 12). Given that Ser57 ubiquitin phosphorylation activity was detected within yeast and human Snf1-related kinases (Figure 3—figure supplement 13), we propose that this is an evolutionarily conserved function for a subset of kinases within this family.

In an effort to understand the biological functions of Ser57-phosphorylated ubiquitin in yeast, we examined whether the deletion or overexpression of Ser57 ubiquitin kinases phenocopies expression of S57A or S57D ubiquitin, respectively (Figure 1A–B and Figure 2A). We did not observe heat tolerance phenotypes associated with deletion or overexpression of Ser57 ubiquitin kinases (Figure 4—figure supplement 1–2). However, yeast cells overexpressing VHS1 exhibited resistance to canavanine and thialysine (Figure 4A–B and Figure 4—figure supplement 3), reminiscent of canavanine and thialysine resistance conferred by S57D expression (Figure 1A; Lee et al., 2017). Overexpression of a catalytic dead variant (vhs1-K41R, which harbors a mutation in the conserved ATP binding pocket of the kinase domain) did not confer canavanine or thialysine resistance (Figure 4A–B and Figure 4—figure supplement 3). Importantly, the canavanine and thialysine resistance associated with VHS1 overexpression was suppressed in the presence of S57A ubiquitin (Figure 4C–D and Figure 4—figure supplement 4), indicating the phenotypes are driven by the production of Ser57-phosphorylated ubiquitin. We also observed that yeast cells overexpressing SKS1 exhibited hypersensitivity to hydroxyurea (Figure 4—figure supplement 5), consistent with the hydroxyurea sensitivity phenotype observed in yeast cells expressing S57D ubiquitin (Figure 1A). The hydroxyurea hypersensitivity associated with SKS1 overexpression was suppressed in the presence of S57A ubiquitin (Figure 4E), indicating the phenotype requires Ser57 phosphorylation of ubiquitin. Taken together, these phenotypic correlations suggest that Vhs1 and Sks1 exert stress phenotypes associated with the phosphorylation of ubiquitin at the Ser57 position.

![Figure 4.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig4-v2.jpg)

**Figure 4.:** (A) Analysis of yeast strains containing high copy plasmids (empty vector, VHS1, or a kinase dead (vhs1 K41R) variant) grown on the indicated synthetic media plates. (B) Analysis of the same yeast strains in (A) grown in liquid culture containing canavanine (4 µg/mL). Values in each time point are means of three biological replicates (n = 3) and ± SD (error bars). Double asterisk (**) indicates p value < 0.005 at the 14 and 24 hr time points using a Student’s t-test, which was only observed for yeast overexpressing wildtype VHS1. (C) Analysis of yeast strains (SUB280 background, expressing either WT or S57A ubiquitin) containing the indicated high copy plasmids (empty vector or harboring VHS1 or SKS1) grown on the indicated synthetic media plates. (D) Analysis of the same yeast strains in (C) grown in liquid culture containing canavanine (4 µg/mL). Values in each time point are means of three biological replicates (n = 3) and ± SD (error bars). Double asterisk (**) indicates p value < 0.005 at the 14 and 24 hr time points using a Student’s t-test, which was only observed for yeast overexpressing wildtype VHS1 and expressing wildtype ubiquitin. (E) Analysis of yeast strains (SUB280 background, expressing either WT or S57A ubiquitin) containing the indicated high copy plasmids (empty vector or harboring VHS1 or SKS1) grown on the indicated synthetic media plates. (F) Analysis of the growth response to oxidative stress in WT and Δsks1Δvhs1 double mutant cells, with indicated complementation expression vectors. OD600 of cells (n = 4; ± SD error bars) in dropout SM media in the absence or presence of 1.5 mM H2O2 after incubation at 24 hr or 48 hr, respectively. Starting OD600 of 0.025 and data was collected for four biological replicate experiments (n=4). Double asterisk (**) indicates p value < 0.001 compared to wildtype yeast treated with H2O2 using a Student’s t-test, which was observed for yeast expressing empty vector, VHS1 individually, or SKS1 individually but not for yeast expressing both VHS1 and SKS1. (G) Analysis of the growth response to oxidative stress in WT and Δsks1Δvhs1 double mutant cells, with indicated ubiquitin expression vectors. OD600 of cells (n = 4; ± SD error bars) in dropout SM media in the absence or presence of 1.5 mM H2O2 after incubation at 24 hr or 48 hr, respectively. Starting OD600 of 0.025 and data was collected for four biological replicate experiments (n=4). Double asterisk (**) indicates p value < 0.001 compared to wildtype yeast treated with H2O2 using a Student’s t-test, which was observed for yeast expressing empty vector, wildtype ubiquitin, or S57A ubiquitin but not S57D ubiquitin. (H) Chromatography data serving as the basis for quantification of Ser57 phosphorylation corresponding to Table 1. Yeast cells expressing endogenous FLAG-ubiquitin (JMY1312 [SEY6210 background] parent cells) were cultured in heavy (H; wildtype cells [blue trace]) or light (L, isogenic Δvhs1Δsks1 deletion [red trace]) SILAC media to the mid-log phase and cells were treated with 1 mM H2O2 for 30 min before harvesting. Following cell lysis and overnight tryptic digestion of affinity-purified FLAG-ubiquitin, phospho-peptides were enriched using IMAC chromatography (see Materials and Methods) and analyzed by mass spectrometry. The Ser57 phosphopeptide is represented in the right panel, while the corresponding unmodified peptide is depicted in the left panel. All individual measurements and p values derived from statistical tests associated with the data in this figure are reported in Figure 4—source data 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** SUB280 cells harboring the indicated kinases cloned into a 2µ multicopy plasmid pRS327 were serially diluted onto lysine-dropout synthetic media and grown at 26°C or 37°C for 3 days. KIN1 and KIN2 were included as control kinases in the Snf1-related family that did not exhibit Ser57 ubiquitin kinase activity in our screening (Figure 3—figure supplement 2).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Null-mutants derived from SEY6210 yeast strain were serially diluted onto YPD plates and incubated at 26°C or 39°C for 18 hr and shifted to 26°C for growth recovery.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** SUB280 cells expressing wildtype ubiquitin were transformed with VHS1 or vhs-K41R (in 2µ multicopy plasmid pRS327) and grown in lysine-dropout synthetic liquid media supplemented with 8 µg/mL thialysine. OD600 of cells were measured in different time points and the results were plotted as means of four biological replicates (n=4) with ± SD expressed as error bars. Double asterisk (**) indicates p value < 0.001 at the 12, 18, and 24 hr time points using a Student’s t-test, which was only observed for yeast overexpressing wildtype VHS1. For all statistical analysis associated with this figure supplement, p values are reported in the Figure 4—source data 1.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Vhs1 (cloned into a 2µ multicopy plasmid pRS327) was overexpressed in SUB280 cells expressing ubiquitin (exclusively wildtype or S57A). Cells were grown in lysine dropout synthetic liquid media supplemented with 8 µg/mL thialysine. Values at each time point are means of four biological replicates with ± SD expressed as error bars. Double asterisk (**) indicates p value < 0.001 at the 12, 18, and 24 hr time points using a Student’s t-test, which was only observed for yeast overexpressing wildtype VHS1 in the context of wildtype ubiquitin expression. For all statistical analysis associated with this figure supplement, p values are reported in the Figure 4—source data 1.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/58155/elife-58155-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** SUB280 cells harboring the indicated kinases (expressed from the 2µ multicopy plasmid pRS327) were serially diluted onto lysine-dropout synthetic media or equivalent media supplemented with 200 mM hydroxyurea and grown at 26°C. KIN1 and KIN2 were included as control kinases in the Snf1-related family that did not exhibit Ser57 ubiquitin kinase activity in our screening (Figure 3—figure supplement 2).

We also examined whether the deletion of Ser57 ubiquitin kinases phenocopied the oxidative stress response defect observed for yeast cells expressing S57A ubiquitin (Figure 2A). Notably, Δsks1Δvhs1 double mutant cells failed to arrest growth in response to oxidative stress, a phenotype that could only be complemented by the re-introduction of both VHS1 and SKS1 (Figure 4F). This phenotype of Δsks1Δvhs1 double mutant cells was also suppressed by the expression of S57D (but not WT or S57A) ubiquitin (Figure 4G) suggesting that the growth arrest defect in Δsks1Δvhs1 cells is linked to a deficiency in the production of ubiquitin phosphorylated at the Ser57 position. To explore this further, we used SILAC-MS to compare levels of Ser57 phosphorylated ubiquitin in untreated or H2O2-treated cells, however, this analysis did not reveal significant changes in Δsks1Δvhs1 cells (Figure 4H and Table 1). While these results indicate that Sks1 and Vhs1 are dispensable for production of Ser57 phosphorylated ubiquitin in the acute phase of the oxidative stress response, we cannot exclude roles for these kinases during prolonged exposure to oxidative stress or the possibility that they contribute to the phosphorylation of localized pools of ubiquitin.

**Table 1.**
 Corresponds to Figure 4H.Analysis of ubiquitin phosphorylation in Δvhs1Δsks1 mutants. Yeast cells expressing endogenous FLAG-ubiquitin (JMY1312 [SEY6210 background] parent cells) were cultured in heavy (H; wildtype cells) or light (L, isogenic Δvhs1Δsks1 deletion) SILAC media to the mid-log phase. In Experiment #1, cells were untreated, and in Experiment #2 cells were treated with 1 mM H2O2 for 30 min before harvesting cells. Following cell lysis and overnight digestion of lysates with trypsin, phospho-peptides were enriched using IMAC chromatography (see Materials and methods) and analyzed by mass spectrometry. Phosphorylated ubiquitin peptides resolved in these experiments are indicated and the values presented in the table represent the H:L SILAC ratio, which has been normalized to the total ubiquitin H:L ratio for each experiment and log-transformed (log2). ‘n.d.’ for Ser19 in Experiment #1 indicates that this peptide was identified but could not be quantified in this experiment due to poor quality of chromatographic data.


<table>
  <thead>
    <tr>
      <th rowspan="2">Peptide</th>
      <th rowspan="2">Phospho- site</th>
      <th colspan="2">log2 (H:L Ratio)</th>
    </tr>
    <tr>
      <th>Expt #1</th>
      <th>Expt #2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TITLEVE[pS]SDTIDNVK</td>
      <td>Ser19</td>
      <td>n.d.</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>TL[pS]DYNIQK</td>
      <td>Ser57</td>
      <td>0.06</td>
      <td>−0.06</td>
    </tr>
    <tr>
      <td>ES[pT]LHLVLR</td>
      <td>Thr66</td>
      <td>−0.22</td>
      <td>0.11</td>
    </tr>
  </tbody>
</table>

## Discussion

The data presented here provide evidence that Ser57 phosphorylated ubiquitin and the kinases that produce it play an important role in several yeast stress responses, but the low stoichiometry of this modification suggests its effects are likely limited and localized in a physiological context. To the best of our knowledge, this study reports the first Ser57 ubiquitin kinases, and the only known ubiquitin kinases besides PINK1. Importantly, PINK1 activity is tightly regulated and highly localized to the outer membrane of damaged mitochondria. One potential explanation of the genetic and biochemical data presented here is that Sks1 and Vhs1 phosphorylate a localized pool (or pools) of ubiquitin in response to stress. However, the data also indicate that Sks1 and Vhs1 are not required for the production of Ser57 phosphorylated ubiquitin during normal growth or oxidative stress (Figure 4H and Table 1). This may be due to redundancy of kinase activities, possibly with Gin4, Kcc4, or other as-yet-unidentified ubiquitin kinases. However, such redundancy cannot explain the phenotypes observed during oxidative stress, since Δsks1Δvhs1 double mutant cells exhibit oxidative stress phenotypes that are suppressed by expression of phosphomimetic (S57D) ubiquitin (Figure 4G). In this case, we propose that a localized pool of ubiquitin phosphorylated by Sks1 and Vhs1 is critical for the oxidative stress response but is not resolved in our proteomic analysis, or only contributes a small fraction to a larger pool. This interpretation reconciles the genetic and biochemical data presented here, and it is consistent with the precedent established with PINK1, which is subject to tight regulation and contributes to localized production of Ser65 phosphorylated ubiquitin. However, further characterization of the Ser57 ubiquitin kinases reported here and analysis of localized ubiquitin pools will be required to validate this interpretation.

Genetic experiments presented here reveal that ubiquitin replacement with phosphomimetic ubiquitin phenocopies kinase gain of function (as is the case with canavanine, thialysine, and hydroxyurea sensitivities) while replacement with phosphorylation resistant ubiquitin phenocopies kinase loss of function (as is the case with sensitivity to H2O2). An important limitation of this genetic analysis is the built-in assumption that ubiquitin variants (phosphomimetic or phosphorylation resistant) behave as expected and do not alter other biochemical properties of ubiquitin in a cellular context. Additionally, such phenotypes associated with ubiquitin variants are likely to over-estimate the physiological effects of ubiquitin phosphorylation. In the case of phospho-mimetic (S57D) ubiquitin, this is because physiological ubiquitin phosphorylation is sub-stoichiometric. In the case of phosphorylation resistant (S57A) ubiquitin, this may be due to redundancy of kinases. Such redundancy seems likely since we identified multiple Ser57 ubiquitin kinases (Vhs1, Sks1, Gin4, and Kcc4) and the deletion of two kinases did not decrease the production of Ser57 phosphorylated ubiquitin (Figure 4H and Table 1). Furthermore, we cannot exclude the possibility that mutation of Ser57 alters the biochemical properties of ubiquitin in such a way as to phenocopy the effects associated with kinase deletion and/or overexpression. Going forward, these limitations present formidable challenges for dissecting the biological functions of ubiquitin phosphorylation, which is why the identification and characterization of ubiquitin kinases is critical. Ultimately, deeper characterization of Ser57 ubiquitin kinases – particularly to understand their localization and regulation in the context of proteotoxic stress – will likely be critical to understanding how phosphorylation regulates the biology of the ubiquitin code.

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
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>SUB280</td>
      <td>D. Finley Lab; Finley et al., 1994 PMID:8035826 PMCID:PMC359070</td>
      <td></td>
      <td>MATa, lys2-801, leu2-3, 112, ura3-52, his3-D200, trp 1–1, ubi1-D1::TRP1, ubi2-D2::ura3, ubi3-Dub-2, ubi4-D2::LEU2 [pUB39 Ub, LYS2] [pUB100, HIS3]</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>SUB280 Ub (WT, S57A, S57D)</td>
      <td>Lee et al., 2017 PMID:29130884 PMCID:PMC5706963</td>
      <td></td>
      <td>MATa, SUB280 [RPS31 (WT, S57A, S57D; URA3)]</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY318</td>
      <td>This paper</td>
      <td></td>
      <td>MATa, SUB280 arg4::KANMX</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>SEY6210</td>
      <td>S. Emr Lab; Robinson et al., 1988 PMID:3062374 PMCID:PMC365587</td>
      <td>RRID:ATCC: 96099</td>
      <td>WT: MATα leu2-3,112 ura4-52 his3-D200 trp1-D901 lys2-801 suc2-D9</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>SEY6210.1</td>
      <td>S. Emr Lab; Robinson et al., 1988 PMID:3062374 PMCID:PMC365587</td>
      <td></td>
      <td>WT: MATa leu2-3,112 ura4-52 his3-D200 trp1-D901 lys2-801 suc2-D9</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY175</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 gin4::NATMX</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY117</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 sks1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY118</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 vhs1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY196</td>
      <td>This paper</td>
      <td></td>
      <td>MATa, SEY6210.1 sks1::TRP1 vhs1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY177</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 gin4::NATMX sks1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY179</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 gin4::NATMX vhs1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY181</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 gin4::NATMX sks1::TRP1 vhs1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>JMY1312</td>
      <td>This paper</td>
      <td></td>
      <td>MATα, SEY6210 arg4::KANMX FLAG-RPS3::TRP1, FLAG-RPL40B::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>NHY326</td>
      <td>This paper</td>
      <td></td>
      <td>MATa, JMY1312 sks1::TRP1 vhs1::TRP1</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>Rosetta 2 (DE3)</td>
      <td>Millipore (Burlington, MA)</td>
      <td>Cat# 71400</td>
      <td>F- ompT hsdSB(rB- mB-) gal dcm (DE3) pRARE2 (CamR) Competent Cells - Novagen</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>C41 (DE3)</td>
      <td>Lucigen Corporation (Middleton, WI)</td>
      <td></td>
      <td>F– ompT hsdSB (rB - mB -) gal dcm (DE3) Competent Cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pRS415</td>
      <td>Stratagene</td>
      <td></td>
      <td>(Empty Backbone) Yeast Centromere Plasmid (LEU2) GenBank: U03449</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pRS416</td>
      <td>Sikorski and Hieter, 1989</td>
      <td></td>
      <td>(Empty Backbone) Yeast Centromere Plasmid (URA3) GenBank: U03450</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1303</td>
      <td>This paper</td>
      <td></td>
      <td>pNative-Sks1 in pRS416 (URA3); yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1304</td>
      <td>This paper</td>
      <td></td>
      <td>pNative-Sks1 in pRS415 (LEU2); yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1280</td>
      <td>This paper</td>
      <td></td>
      <td>pTDH3-Sks1 in pRS415 (LEU2); yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1253</td>
      <td>This paper</td>
      <td></td>
      <td>pNative_Vhs1 in pRS415 (LEU2); yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pRS327</td>
      <td>PMID:14989082</td>
      <td>RRID:Addgene_51787</td>
      <td>(Empty Backbone) multicopy (YEp) vector with a 2 μm origin of replication (LYS2); yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1746</td>
      <td>This paper</td>
      <td></td>
      <td>pTDH3-Gin4 in pRS327; yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1749</td>
      <td>This paper</td>
      <td></td>
      <td>pTDH3-Kcc4 in pRS327; yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1743</td>
      <td>This paper</td>
      <td></td>
      <td>pTDH3-Sks1 in pRS327; yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1740</td>
      <td>This paper</td>
      <td></td>
      <td>pTDH3-Vhs1 in pRS327; yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1771</td>
      <td>This paper</td>
      <td></td>
      <td>pTDH3-Vhs1 K41R (kinase dead) in pRS327; yeast expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1240</td>
      <td>This paper</td>
      <td></td>
      <td>6XHis-Sks1 in pET15b, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1169</td>
      <td>This paper</td>
      <td></td>
      <td>Vhs1-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM983</td>
      <td>This paper</td>
      <td></td>
      <td>Gin4-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1116</td>
      <td>This paper</td>
      <td></td>
      <td>Hal4-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1118</td>
      <td>This paper</td>
      <td></td>
      <td>Hal5-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1120</td>
      <td>This paper</td>
      <td></td>
      <td>Kkq8-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1336</td>
      <td>This paper</td>
      <td></td>
      <td>Snf1-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM585</td>
      <td>This paper</td>
      <td></td>
      <td>6XHis-Npr1 in pCOLADuet, KmR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1270</td>
      <td>This paper</td>
      <td></td>
      <td>Ksp1-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1186</td>
      <td>This paper</td>
      <td></td>
      <td>GST-Slt2 in pGEX6p1; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1335</td>
      <td>This paper</td>
      <td></td>
      <td>Frk1-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM987</td>
      <td>This paper</td>
      <td></td>
      <td>Kcc4-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1306</td>
      <td>This paper</td>
      <td></td>
      <td>Kin1-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1307</td>
      <td>This paper</td>
      <td></td>
      <td>Kin2-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1272</td>
      <td>This paper</td>
      <td></td>
      <td>Ypl150w-6XHis in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1167</td>
      <td>This paper</td>
      <td></td>
      <td>6XHis-GST-UBD, AmpR;E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1235</td>
      <td>This paper</td>
      <td></td>
      <td>Ubiquitin in pBG100; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1236</td>
      <td>This paper</td>
      <td></td>
      <td>Ubiquitin S57A in pBG100; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM1237</td>
      <td>This paper</td>
      <td></td>
      <td>Ubiquitin S65A in pBG100; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM995</td>
      <td>This paper</td>
      <td></td>
      <td>di-Ub in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA</td>
      <td>pJAM996</td>
      <td>This paper</td>
      <td></td>
      <td>tri-Ub in pET23d, AmpR; E. coli expression</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-Flag (FLAG(R) M2) mouse monoclonal</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>RRID:AB_262044</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-Ubiquitin (VU101) mouse monoclonal; clone VU-1</td>
      <td>LifeSensors (Malvern, PA)</td>
      <td>Cat# VU101 RRID:AB_2716558</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-Glucose-6-Phosphate Dehydrogenase (G6PDH), yeast rabbit polyclonal</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat# A9521 RRID:AB_258454</td>
      <td>WB (1:10000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-pSer57 Ubiquitin rabbit polyclonal</td>
      <td>This paper</td>
      <td></td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>K48-linkage Specific Polyubiquitin rabbit monoclonal; clone D9D5</td>
      <td>Cell Signaling Technology (Danvers, MA)</td>
      <td>Cat# 8081 RRID:AB_10859893</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>K63-linkage Specific Polyubiquitin rabbit monoclonal; clone Apu3</td>
      <td>Millipore (Burlington, MA)</td>
      <td>Cat# 05–1308 RRID:AB_1587580</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IRDye 680RD-Goat anti-mouse polyclonal</td>
      <td>LI-COR Biosciences (Lincoln, NE)</td>
      <td>Cat# 926–68070 RRID:AB_10956588</td>
      <td>WB (1:10000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IRDye 800CW-Goat anti-rabbit polyclonal</td>
      <td>LI-COR Biosciences (Lincoln, NE)</td>
      <td>Cat# 926–32211 RRID:AB_621843</td>
      <td>WB (1:10000)</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>PTMScan Ubiquitin Remnant Motif (α-K-ε-GG)</td>
      <td>Cell Signaling Technology (Danvers, MA)</td>
      <td>RRID:Cat# 5562</td>
      <td>bead-conjugated for immunoprecipitation of –GG-εK-conjugated peptides</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EZ view Red Anti-FLAG M2 Affinity Gel</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat# F2426-1ML RRID:AB_2616449</td>
      <td>mouse-monoclonal; clone M2 bead-conjugated for immunoprecipitation of FLAG-conjugated proteins</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-Lysine-13C6,13N2hydrochloride</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat# 608041–1G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-Arginine-13C6,13N4hydrochloride</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat# 608033–1G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium arsenate dibasic heptahydrate</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat# A6756</td>
      <td>Synonym: arsenate</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrogen peroxide</td>
      <td>Fisher (Hampton, NH)</td>
      <td>Cat# H325-500</td>
      <td>Synonym: H2O2</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydroxyurea</td>
      <td>INDOFINE Chemical Company, Inc (Hillsborough, NJ)</td>
      <td>Cat# BIO-216</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>S-(2-Aminoethyl)-L-cysteine hydrochloride</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat# A2636-1G</td>
      <td>Synonym: L-4-Thialysine hydrochloride, thialysine</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-Canavanine</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat. # C1625</td>
      <td>Synonym: canavanine</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DL-2-Aminoadipic acid</td>
      <td>Sigma (St. Louis, MO)</td>
      <td>Cat. # A0637</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MG132</td>
      <td>Apexbio (Houston, TX)</td>
      <td>Cat. # A2585</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Protease inhibitor cocktail (cOmplete Tablets, Mini)</td>
      <td>Roche (Basel, Switzerland)</td>
      <td>Cat# 04693159001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PhosSTOP</td>
      <td>Roche (Basel, Switzerland)</td>
      <td>Cat# 04906837001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phos-tag Acrylamide</td>
      <td>NARD</td>
      <td>Cat# AAL-107</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MaxQuant Version 1.6.5.0</td>
      <td>Max Planck Institute of Biochemistry</td>
      <td>RRID:SCR_014485</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Skyline Version 20.1.0.155</td>
      <td>MacCoss Lab Software</td>
      <td>RRID:SCR_014080</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Illustrator CS5.1 Version 15.1.0</td>
      <td>Adobe (San Jose, CA)</td>
      <td>RRID:SCR_010279</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Image Studio Lite Version 5.2</td>
      <td>LI-COR Biosciences (Lincoln, NE)</td>
      <td>RRID:SCR_013715</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell strains and culture

All Saccharomyces cerevisiae strains and reagents used in this study are described in the Key Resources Table. SUB280 cells were used to shuffle different ubiquitin variants (wildtype, S57A, and S57D) by counterselection on URA-dropout SDM plates containing DL-2-aminoadipic acid as previously described (Lee et al., 2019; Sloper-Mould et al., 2001). Such SUB280-derived cells were used in growth sensitivity assays in different stress conditions. SEY6210 cells were used to generate gene-deletion strains by resistance marker-guided recombination and cross-mating methods. Yeast strains for mass spectrometry experiments were JMY1312 (with chromosomally tagged RPS31 and RPL40B) and its derivatives. Cells were cultured at 26°C in yeast-peptone-dextrose (YPD) or synthetic dextrose minimal medium (SDM: 0.67% yeast nitrogen base, 2% dextrose, and required amino acids) at 200 rpm agitation. SILAC media were supplemented with light lysine (12C614N2 L-Lys) and arginine (12C614N4 L-Arg), or heavy isotopes of lysine (13C615N2 L-Lys) and arginine (13C615N4 L-Arg). For spot plate dilution assay, cells were grown for 18–24 hr, normalized to OD600 of 1.0, and sequentially diluted at 1:10 dilution onto SDM agar plates containing amino acid dropout mixture in the absence or presence of 2.5 mM NaH2AsO4, 200 mM hydroxyurea, 2.0 µg/mL canavanine, and 6.0 µg/mL thialysine. For H2O2 sensitivity assay, yeast cells grown to the mid-log phase (OD600 of 0.7) were diluted to OD600 of 0.025 with 1.5 mM H2O2 in SDM and terminal OD600 of cells was measured after 1–3 days of incubation. For growth sensitivity assay of liquid cultures, cells were grown for 18 hr at 26°C, normalized to OD600 of 5.0, and subcultured into fresh media with a starting OD600 of 0.1. OD600 of cells was recorded at different time points until cells reach the stationary phase. For bacterial cultures, the yeast kinase and ubiquitin were heterologously co-expressed in E. coli Rosetta 2 (DE3) by 1 mM IPTG induction at 26°C for 16 hr.

### Protein preparation

#### Protein precipitation

Yeast proteins were precipitated by adding ice-cold 10% trichloroacetate in TE buffer (2 mM EDTA, 10 mM Tris-HCl, pH 8.0), washed with 100% acetone, and lyophilized by vacuum centrifugation. Desiccated protein was resolubilized in urea sample buffer.

#### Recombinant protein expression and purification of kinases

N-terminally tagged Vhs1 or Sks1 were produced in E. coli C41(DE3) cells cultured in LB Media. Cells were induced at an OD600 of 0.6 with 1 mM IPTG and allowed to express for 4 hr at 37°C. Cells were pelleted by centrifugation at 6000 × g for 25 min and flash-frozen with liquid nitrogen. Before purification, the cells were thawed on ice, resuspended in 5 mL of lysis buffer (50 mM Tris pH 8.0, 150 mM NaCl, 10 mM imidazole, 2 mM βME, complete protease inhibitors [Roche, Basel, Switzerland], 1 μg/mL DNase, 1 μg/mL lysozyme, and 1 mM PMSF) per 1 g of cells, and sonicated (21 min total, 5 s on and 10 s off). Cell lysates were cleared by centrifugation (50,000 × g for 30 min at 4°C) and filtered through a 0.45 μM filter. For purification, lysates were applied to Ni-NTA resin (Thermo Scientific, Rockford, IL) that had been equilibrated with lysis buffer containing 20 mM imidazole. The protein was eluted with lysis buffer containing 400 mM imidazole. Protein was buffer exchanged to remove imidazole (50 mM Tris pH 8.0, 100 mM NaCl, and 2 mM βME) and the purification tag was cleaved. The protein was loaded on a HiPrep Q FF Anion Exchange Column (GE Healthcare Life Sciences, Marlborough, MA) and eluted by buffer with 300 mM NaCl. Recombinant ubiquitin variants were purified using the Ni-NTA affinity protocol described above, followed by size exclusion chromatography using a HiLoad Superdex 75 pg column (GE Healthcare Life Sciences, Marlborough, MA). The protein was eluted in a buffer containing (50 mM Tris pH 7.5, 150 mM NaCl, and 2 mM DTT). Ubiquitin-containing fractions were pooled and concentrated by centrifugation to 1 mM.

### Western blotting

Proteins in Laemmli buffer (for E. coli lysates) or urea sample buffer (for TCA-precipitated yeast proteins) containing 10% β-mercaptoethanol were resolved in 12–14% Bis-Tris PAGE gel by electrophoresis. Separated proteins were transferred onto PVDF membrane (0.2 µm, GE Healthcare Amersham) and immunoblotting was performed using the following primary antibodies: anti-ubiquitin (1:10,000; LifeSensors; MAb; clone VU-1), anti-K48 (1:10,000; Cell Signaling; RAb; clone D9D5), anti-K63 (1:4000; EMD Millipore; RAb; clone apu3), and anti-G6PDH (1:10,000; Sigma; RAb). Anti-mouse (IRDye 680RD-Goat anti-mouse) or anti-rabbit (IRDye 800CW-Goat anti-rabbit) secondary antibodies were purchased from LI-COR. Blots were visualized using Odyssey CLx (LI-COR Biosciences) and signal intensity was quantified using Image Studio Lite (LI-COR Biosciences).

### Mass spectrometry

SILAC-based mass spectrometry for quantitation and mapping of ubiquitin phosphorylation sites was performed as previously described (Albuquerque et al., 2008; Lee et al., 2019). Briefly, an equal amount of JMY1312 cells (labeled with either light or heavy Arg and Lys) expressing endogenous 3XFLAG-RPS31 and 3XFLAG-RPL40B were harvested from the mid-log phase and disrupted by bead beating using ice-cold lysis buffer (50 mM Tris-HCl, pH 7.5, 150 mM NaCl, 5 mM EDTA, 0.2% NP-40, 10 mM iodoacetamide, 1 mM 1,10-phenanthroline, 1× EDTA-free protease inhibitor cocktail [Roche], 1 mM phenylmethylsulfonyl fluoride, 20 µM MG132, 1× PhosStop [Roche], 10 mM NaF, 20 mM BGP, and 2 mM Na3VO4). Lysate was clarified by centrifugation at 21,000 × g for 10 min at 4°C and supernatant was transferred into a new tube and diluted with three-fold volume of ice-cold TBS (50 mM Tris-HCl, pH 7.5, 150 mM NaCl). 3XFLAG-ubiquitin in 12 mL diluted lysate was enriched by incubation with 50 µL of EZview anti-FLAG M2 resin slurry (Sigma) for 2 hr at 4°C with rotation. The resin was washed three times with cold TBS and incubated with 90 µL elution buffer (100 mM Tris-HCl, pH 8.0, 1% SDS) at 98°C for 5 min. The collected eluate was reduced with 10 mM DTT, alkylated with 20 mM iodoacetamide, and precipitated with 300 µL PPT solution (50% acetone, 49.9% ethanol, and 0.1% acetic acid). Light and heavy protein pellets were dissolved with Urea-Tris solution (8 M urea, 50 mM Tris-HCl, pH 8.0). Heavy and light samples were combined, diluted four-fold with water, and digested with 1 µg MS-grade trypsin (Gold, Promega) by overnight incubation at 37°C. Phosphopeptides were enriched by immobilized metal affinity chromatography (IMAC) using Fe(III)-nitrilotriacetic acid resin as previously described (MacGurn et al., 2011) and dissolved in 0.1% trifluoroacetic acid. Peptides with K-ε-GlyGly remnant were isolated by immunoprecipitation as described in the PTMScan Ubiquitin Remnant Motif Kit (Cell Signaling Technologies) protocol. The GlyGly-peptide and phosphopeptide solutions were loaded on a capillary reverse-phase analytical column (360 μm O.D. × 100 μm I.D.) using a Dionex Ultimate 3000 nanoLC and autosampler and analyzed using a Q Exactive Plus mass spectrometer (Thermo Scientific). Data collected were searched using MaxQuant (ver. 1.6.5.0) and chromatograms were visualized using Skyline (ver. 20.1.0.31, MacCoss Lab).

### In vitro kinase activity

Kinase activity assays were performed in a reaction mixture containing 50 mM Tris (pH 7.4), 150 mM NaCl, 10 mM MgCl2, 0.1 mM ATP, 1 mM DTT, 0.5 µM ubiquitin, and 50 nM kinase. Reactions on linkage-specific ubiquitin polymers were carried out at 30°C for 30 min and quenched by adding an equal volume of Laemmli buffer with 10% β-mercaptoethanol and heating at 98°C for 10 min.
