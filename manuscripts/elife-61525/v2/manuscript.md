# Real-time monitoring of peptidoglycan synthesis by membrane-reconstituted penicillin-binding proteins

## Authors

- Víctor M Hernández-Rocamora<sup>1</sup> ([ORCID: 0000-0003-2517-5707](https://orcid.org/0000-0003-2517-5707))
- Natalia Baranova<sup>2</sup> ([ORCID: 0000-0002-3086-9124](https://orcid.org/0000-0002-3086-9124))
- Katharina Peters<sup>1</sup>
- Eefjan Breukink<sup>3</sup>
- Martin Loose<sup>2</sup> ([ORCID: 0000-0001-7309-9724](https://orcid.org/0000-0001-7309-9724)) †
- Waldemar Vollmer<sup>1</sup> ([ORCID: 0000-0003-0408-8567](https://orcid.org/0000-0003-0408-8567)) †

### Affiliations

1. Centre for Bacterial Cell Biology, Biosciences Institute, Newcastle University Newcastle upon Tyne United Kingdom
2. Institute for Science and Technology Austria (IST Austria) Klosterneuburg Austria
3. Membrane Biochemistry and Biophysics, Bijvoet Centre for Biomolecular Research, University of Utrecht Utrecht Netherlands

† Corresponding author

## Abstract

Peptidoglycan is an essential component of the bacterial cell envelope that surrounds the cytoplasmic membrane to protect the cell from osmotic lysis. Important antibiotics such as β-lactams and glycopeptides target peptidoglycan biosynthesis. Class A penicillin-binding proteins (PBPs) are bifunctional membrane-bound peptidoglycan synthases that polymerize glycan chains and connect adjacent stem peptides by transpeptidation. How these enzymes work in their physiological membrane environment is poorly understood. Here, we developed a novel Förster resonance energy transfer-based assay to follow in real time both reactions of class A PBPs reconstituted in liposomes or supported lipid bilayers and applied this assay with PBP1B homologues from Escherichia coli, Pseudomonas aeruginosa, and Acinetobacter baumannii in the presence or absence of their cognate lipoprotein activator. Our assay will allow unravelling the mechanisms of peptidoglycan synthesis in a lipid-bilayer environment and can be further developed to be used for high-throughput screening for new antimicrobials.

## Introduction

Peptidoglycan (PG) is a major cell wall polymer in bacteria. It is composed of glycan strands of alternating N-actetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues interconnected by short peptides. PG forms a continuous, mesh-like layer around the cell membrane to protect the cell from bursting due to the turgor and maintain cell shape (Vollmer et al., 2008). The essentiality and conservation of PG in bacteria make PG metabolism an ideal target of antibiotics.

Class A penicillin-binding proteins (PBPs) are bifunctional PG synthases which use the precursor lipid II to polymerize glycan chains (glycosyltransferase [GTase] reactions) and crosslink peptides from adjacent chains by DD-transpeptidation (Goffin and Ghuysen, 1998). Moenomycin inhibits the GTase and β-lactams the transpeptidase function of class A PBPs (Sauvage and Terrak, 2016; Macheboeuf et al., 2006). In Escherichia coli, PBP1A and PBP1B account for a substantial proportion of the total cellular PG synthesis activity (Cho et al., 2016) and are tightly regulated by interactions with multiple proteins (Egan et al., 2015; Typas et al., 2012; Egan et al., 2020; Egan et al., 2017), including the outer membrane-anchored activators LpoA and LpoB (Egan et al., 2018; Typas et al., 2010; Jean et al., 2014).

Historically, in vitro PG synthesis assays have been crucial to decipher the biochemical reactions involved in PG synthesis and determine the mode of action of antibiotics (Izaki et al., 1968). However, these studies were limited by the scarcity of lipid II substrate and the inability to purify a sufficient quantity of active enzymes. Lipid II can now be synthesized chemically (VanNieuwenhze et al., 2002; Schwartz et al., 2001; Ye et al., 2001) or semi-enzymatically (Breukink et al., 2003; Egan et al., 2015), or isolated from cells with inactivated MurJ (Qiao et al., 2017). Radioactive or fluorescent versions of lipid II are also available to study PG synthesis in a test tube. However, there are several drawbacks with currently available PG synthesis assays. First, most assays are end-point assays that rely on discrete sampling and therefore do not provide real-time information about the enzymatic reaction. Second, some assays involve measuring the consumption of lipid II or analysing the reaction products by SDS-PAGE (Egan et al., 2015; Barrett et al., 2007; Qiao et al., 2014; Sjodt et al., 2018) or high-pressure liquid chromatography (HPLC) after digestion with a muramidase (Bertsche et al., 2005; Born et al., 2006). These laborious techniques make assays incompatible with high-throughput screening and hinder the determination of kinetic parameters. A simple, real-time assay with dansyl-labelled lipid II substrate overcomes these problems but is limited to assay GTase reactions (Schwartz et al., 2001; Offant et al., 2010; Egan et al., 2015).

Recently, two types of real-time TPase assays have been described. The first uses non-natural mimics of TPase substrates such as the rotor-fluorogenic 470 D-lysine probe Rf470DL, which increases its fluorescence emission upon incorporation into PG (Hsu et al., 2019). The second assay monitors the release of D-Ala during transpeptidation in coupled enzymatic reactions with D-amino acid oxidase, peroxidases, and chromogenic or fluorogenic compounds (Frére et al., 1976; Gutheil et al., 2000; Catherwood et al., 2020). Coupled assays are often limited in the choice of the reaction conditions, which in this case must be compatible with D-amino acid oxidase activity. Hence, each of the current assays has its limitations and most assays exclusively report on either the GTase or TPase activity, but not both activities at the same time.

Another major drawback of many of the current assays is that they include detergents and/or high concentration (up to 30%) of the organic solvent dimethyl sulfoxide (DMSO) to maintain the PG synthases in solution (Offant et al., 2010; Biboy et al., 2013; Huang et al., 2013; Lebar et al., 2013; Qiao et al., 2014; Egan et al., 2015; Catherwood et al., 2020). However, both detergents and DMSO have been shown to affect the activity and interactions of E. coli PBP1B (Egan and Vollmer, 2016). Importantly, a freely diffusing, detergent-solubilized membrane enzyme has a very different environment compared to the situation in the cell membrane where it contacts phospholipids and is confined in two dimensions (Gavutis et al., 2006; Zhdanov and Höök, 2015). Here, we sought to overcome the main limitations of current PG synthesis assays and establish a system with more physiological experimental conditions. We used sensitive Förster resonance energy transfer (FRET) detection for simultaneous monitoring of GTase and TPase reactions. The real-time assay reports on PG synthesis in phospholipid vesicles or planar lipid bilayers. We successfully applied this assay to several class A PBPs from pathogenic Gram-negative bacteria, demonstrating its robustness and potential use in screening assays to identify PBP inhibitors.

## Results

### Real-time assay for detergent-solubilized E. coli PBP1B

To develop a FRET-based real-time assay for PG synthesis using fluorescently labelled lipid II, we prepared lysine-type lipid II versions with high quantum yield probes, Atto550 (as FRET donor) and Atto647n (as FRET acceptor), linked to position 3 (Figure 1—figure supplement 1A, B; Mohammadi et al., 2014; Egan et al., 2015). For assay development, we used E. coli PBP1B (PBP1BEc) (Egan et al., 2015; Bertsche et al., 2005; Biboy et al., 2013) solubilized with Triton X-100 and a lipid-free version of its cognate outer membrane-anchored lipoprotein activator LpoB (Typas et al., 2010; Egan et al., 2014; Egan et al., 2018; Lupoli et al., 2014; Catherwood et al., 2020).

PBP1BEc can utilize fluorescently labelled lipid II to polymerize long glycan chains only when unlabelled lipid II is also present in the reaction (Van't Veer et al., 2016). We therefore included unlabelled meso-diaminopimelic acid (mDAP)-type lipid II into reactions of PBP1BEc with lipid II-Atto550 and lipid II-Atto647n (Figure 1A). Both probes were incorporated into the produced PG or glycan chains as indicated by SDS-PAGE analysis (Figure 1B, I). After the reaction, fluorescence spectra taken at the excitation wavelength of the donor fluorophore (Atto550, λabs=552 nm) showed a reduced donor emission intensity (λfl=580 nm) and an increased emission of the acceptor fluorophore (Atto647n, λfl=665 nm) (Figure 1C, I) indicative of FRET between the two fluorophores. Analysis of the fluorescence spectra allowed to calculate FRET efficiencies which we found to be 29 ± 6% (Figure 1D, Figure 1—figure supplement 2). Ampicillin, which inhibits the TPase, blocked the formation of crosslinked PG (Figure 1B, II) and reduced the FRET efficiency to one third (Figure 1C, II, D). Moenomycin, which blocks the GTase, and, indirectly, TPase activities completely abolished the incorporation of fluorescent lipid II and the associated signal (Figure 1B, III, D; Bertsche et al., 2005). These results demonstrate that incorporation of the labelled probes into PG by PBP1BEc results in fluorescence energy transfer that depends on the GTase and TPase activity, with the latter being the major contributor.

![Figure 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig1-v2.jpg)

**Figure 1.:** (A) Scheme of the reactions of a class A penicillin-binding protein (PBP) (GTase-TPase) with unlabelled lipid II and the two versions of labelled lipid II, yielding a peptidoglycan (PG) product that shows FRET. (B) SDS-PAGE analysis of PG products by PBP1BEc (0.5 µM) reactions with unlabelled lipid II, Atto550-labelled lipid II, and Atto647n-labelled lipid II at a 1:1:1 molar ratio (each 5 µM), in the absence of antibiotics (I, red) or in the presence of 1 mM ampicillin (II, blue) or 50 µM moenomycin (III, yellow). Samples were incubated for 1 hr at 37°C and boiled for 5 min. (C) Representative fluorescence emission spectra taken after reactions performed as described in B and following the same labelling pattern. (D) FRET efficiency for PBP1BEc reactions carried out as indicated in B, calculated using the (ratio)A method (see Materials and methods). Values are mean ± SD of at least three independent samples. (E) Representative reaction curves from FRET assays of detergent-solubilized PBP1BEc. The same components as indicated in B were incubated in the presence or absence of 2 µM LpoB(sol). Reactions were performed in the absence of antibiotic (left), with 1 mM ampicillin (Amp) or 50 µM moenomycin (Moe) (middle), or by omitting unlabelled lipid II (right). The numbers indicate the corresponding lane of the gel in Figure 1—figure supplement 2D. Samples were incubated for 1 hr at 25°C. (F) Averaged initial slopes from reaction curves obtained by the FRET assay for detergent-solubilized E. coli PBP1B in the presence (blue) or absence (red) of LpoB, and in the presence or absence of ampicillin. Values are normalized relative to the slope in the absence of activator for each condition and are mean ± SD of 2–3 independent experiments.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Chemical structures of lipid II analogues used for the Förster resonance energy transfer assay. R corresponds to Atto550n (donor) or Atto647n (acceptor) in the corresponding analogue. The chemical structures of alkyne versions of Atto550 and Atto647n probes that were used for derivatization are not published. Therefore, the carboxylic variants are depicted here with an asterisk indicating where the alkyne versions diverge. (B) Absorbance (dashed lines) and fluorescence emission (solid lines) spectra for Atto550 (red lines) and Atto647n (blue lines).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Examples of deconvolution of the fluorescence spectra of peptidoglycan samples prepared in the presence of lipid II-Atto550, Lipid II-Atto647n, and unlabelled lipid II, obtained from a reaction without antibiotics (A) or in the presence of ampicillin (B) or moenomycin (C). FRET efficiencies were calculated using the (ratio)A method, in which the enhancement of emission of the acceptor due to the donor is calculated by comparing the emission of (only) the acceptor when exciting at the donor excitation with the emission of the acceptor when exciting only the acceptor (Vámosi and Clegg, 1998). For this, two spectra were taken for every sample, either exciting at 552 nm (donor excitation) or at 650 nm (acceptor excitation). To process the spectra and separate the emission of the acceptor from that of the donor in the spectra taken at the donor excitation, reference spectra were measured from (1) reactions containing lipid II-Atto550 and unlabelled lipid II (donor reference), (2) reactions containing lipid II-Atto647n and unlabelled lipid II (acceptor references at both excitation wavelengths), and (3) reactions containing only unlabelled lipid II (background references at both excitation wavelengths). Reference samples were prepared for every antibiotic condition measured. The reference spectra were then used to analyse the spectrum containing both donor and acceptor probes (black dots). Spectra taken with donor excitation were deconvolved into three components: donor (blue), acceptor (yellow), and background (black), while the spectrum taken with acceptor excitation was deconvolved into two components: acceptor (yellow) and background (black). The fitted spectra are shown in red, and the residuals of the fit are shown below each spectrum.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Fluorescence emission spectra taken at the end (t = 1 hr) of the reactions of E. coli PBP1B shown in Figure 1E (t = 60 min). (B) Aliquots at the end of the reactions shown in Figure 1E were boiled and analysed by SDS-PAGE using fluorescence detection, and lanes are labelled with the reaction numbers as in Figure 1E.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** FI at the acceptor and donor emission wavelengths (590 and 680 nm, respectively) only changed significantly when there was peptidoglycan synthesis activity, and both lipid II-Atto647n and lipid II-Atto550 were added to reactions. Moreover, these changes were indicative of Förster resonance energy transfer (decrease at the donor wavelength and increase at the acceptor wavelength). (A) PBP1BEc reactions in the presence of unlabelled lipid II plus different combinations of labelled substrates (lipid II-Atto550, yellow; lipid II-Atto647n, red; or a mixture of both, blue) were monitored in real time by measuring FI at 590 nm (bottom row) and 680 nm (top row). Reactions without lipid II-Atto550 were monitored at 680 nm only. Reactions were performed at four conditions (left to right): with no antibiotics, with 1 mM ampicillin, with 100 µM moenomycin, or omitting unlabelled lipid II. Changes in FI were normalized by calculating the ratio FI(ti)/FI(t = 0). (B) Same reactions as in A, but performed in the presence of activator LpoB. In both A and B, the final concentration of each labelled lipid II was 5 µM and the total concentration of lipid II (labelled plus unlabelled) was made 15 µM by adding unlabelled lipid II.

Next, we monitored reactions in real time by measuring fluorescence emission of the donor and acceptor fluorophores (FIdonor and FIacceptor, respectively) after excitation of the donor (540 nm) in a microplate reader for 60 min (Figure 1E, Figure 1—figure supplement 3A). As controls, we also performed reactions containing unlabelled lipid II plus only one of the labelled lipid II versions (lipid II-Atto550 or lipid II-Atto647n) in parallel (Figure 1—figure supplement 4). Changes in FIdonor and FIacceptor were much higher when both fluorescent lipid II versions were present, in agreement with energy transfer. Thus, we used the ratio between both signals (FIacceptor/FIdonor) as a real-time readout for FRET and PG synthesis. Without LpoB, FRET appeared after ~5 min and slowly increased until it plateaued after 50–60 min (Figure 1E, left). By contrast, reactions with LpoB(sol) showed an immediate and rapid increase in FRET which reached the plateau after 10–20 min, consistent with faster PG synthesis (Figure 1E, left). In agreement with the end-point analysis described above, we found no FRET in samples containing moenomycin (Figure 1E, middle), and ampicillin generally reduced the final fluorescence ratio level by approximately threefold (Figure 1E, middle). Analysis of reaction products by SDS-PAGE also confirmed that crosslinked PG was only produced in the absence of antibiotics, while the presence of ampicillin still allowed the formation of glycan chains (Figure 1—figure supplement 3B).

The GTase reaction began after a lag phase, consistent with previously published data (Schwartz et al., 2002; Egan et al., 2014), which is likely caused by a slower initiation of glycan chain synthesis compared to the rate of polymerization. We measured the slope of FRET reaction curves during the linear raise in signal after the lag phase (when present) and compared the slopes with or without activator. Slopes with LpoB were approximately ten- or twentyfold higher than without the activator, in the absence or presence of ampicillin, respectively (Figure 1F). Although this result is comparable to the approximately tenfold activation of the GTase rate by LpoB measured with dansyl-lipid II (Egan et al., 2014; Egan et al., 2018), a quantification of the individual GTase and TPase reaction rates would require a more exact knowledge of how these two activities contribute to the final FRET signal, which is currently not available (see Discussion).

### Intra-chain versus inter-chain FRET

Because ampicillin substantially reduced the FRET signal, we hypothesized that FRET arises mainly between fluorophores on different glycan chains of a crosslinked PG product (Figure 1A). To determine the relative contribution of intra-chain versus inter-chain FRET, we digested PG produced in the presence of labelled lipid II with either the DD-endopeptidase MepM, which cleaves crosslinks between glycan chains (Singh et al., 2015; Singh et al., 2012), or the muramidase cellosyl, which cleaves the β-(1,4)-glycosidic bond between MurNAc and GlcNAc-producing muropeptides (structures 1–3 in Figure 2C; Rau et al., 2001; Figure 2A, B). As a control, glycan chains produced by PBP1BEc in the presence of ampicillin were also digested with both hydrolases. SDS-PAGE analysis confirmed that MepM substantially reduced the amount of crosslinked PG in the samples while cellosyl digested the PG into muropeptides (Figure 2A). Next, we measured the FRET efficiency after digestion. MepM digestion had a negligible effect on the FRET efficiency of glycan chains produced in the presence of ampicillin but reduced the FRET efficiency by approximately twofold for crosslinked-PG samples (Figure 2B). This confirms that inter-chain FRET is a major contributor to the final FRET signal. MepM did not reduce FRET efficiency to the same value as ampicillin, presumably because of incomplete digestion of the labelled PG. Finally, cellosyl completely abolished FRET for both glycan chains and crosslinked PG (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig2-v2.jpg)

**Figure 2.:** (A) Peptidoglycan (PG) synthesized in reactions of PBP1BEc in the presence or absence of 1 mM ampicillin was incubated with no PG hydrolase (U), DD-endopeptidase MepM (M), or muramidase cellosyl (C), and aliquots were analysed by SDS-PAGE. Reaction conditions were the same as indicated in Figure 1B–D. (B) FRET efficiency for samples prepared as indicated in A, calculated using the (ratio)A method (see Materials and methods). Values are mean ± SD of at least three independent experiments. (C) PBP1BEc (0.5 µM) was incubated with 5 µM each of lipid II-Atto647n, lipid II-Atto550, and 14C-labelled lipid II. At indicated time points, aliquots were taken and reactions were stopped by addition of moenomycin. After measuring fluorescence (see D), the PG was digested with the muramidase cellosyl, and the resulting muropeptides were reduced with sodium borohydride and separated by HPLC. The structures of muropeptides corresponding to peaks 1–3 are shown below the chromatograms. (D) Fluorescence spectra taken with excitation at 522 nm for the samples described in C. (E) Quantification of peak 2 (GTase product, blue), peak 3 (GTase+TPase, black), or the sum of both 2 and 3 (yellow) from chromatograms in C, along with the FRET signal (red) calculated as the ratio of acceptor emission over donor emission from data in D.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Triton X-100-solubilized PBP1BEc with or without LpoB were incubated with mixtures of lipid II substrates (14C-lipid II, lipid II-Atto550, and lipid II-Atto647) with increasing molar proportions of fluorescently labelled lipid II over the total amount of substrate. Reactions were monitored by fluorescence measurements, and each version of lipid II was quantified at the end. The total concentration of lipid II was kept at 15 µM while the molar ratio of lipid II-Atto550 to lipid II-Atto647n was always 1:1. (A) Consumption of each version of lipid II, monitored as described in Materials and methods, was higher in the presence of LpoB and decreased slightly with higher amounts of labelled lipid II. In all cases, the consumption of 14C-lipid II was slightly higher than that of fluorescent lipid II substrates. (B) The proportion of fluorescent material incorporated into peptidoglycan, calculated based on the consumption data in A, did not deviate significantly from the proportion of fluorescent substrates at the start of reactions. (C) A higher proportion of fluorescent lipid II increased the final FIacceptor/FIdonor ratio, but the increase was higher in the presence of LpoB. (D) The initial slope of Förster resonance energy transfer reaction curves increased significantly with the proportion of labelled lipid II in the presence of LpoB but not in its absence. (E) Table listing the data represented in B and D. The real-time slope represents the increase in FIacceptor/FIdonor per minute at the start of reactions. All values are ± SD of three technical replicates.

To confirm that the formation of peptide crosslinks is required to produce substantial FRET in the absence of LpoB, we analysed the PG synthesized by PBP1BEc from radioactively labelled mDAP-type lipid II and the two fluorescent lipid II analogues (Figure 2C–E). We monitored the reaction at different time points by fluorescence spectroscopy (FRET measurements) and digested aliquots with cellosyl before separating the resulting muropeptides by HPLC. The monomers and crosslinked muropeptide dimers were quantified by scintillation counting using an in-line radiation detector attached to the HPLC column (Figure 2C). FRET increased over time and correlated well with the formation of crosslinked muropeptide dimers, but not the rate of lipid II consumption (peak 2) (Figure 2D, E). Overall, we conclude that, in the absence of LpoB, FRET can arise from GTase activity alone (intra-chain FRET), but the overall contribution from the TPase activity (inter-chain FRET) is dominant.

To study in more detail the contribution of intra-chain FRET, we varied the molar fraction of fluorescent lipid II and measured the activity of PBP1BEc in the presence or absence of activator. Confirming a previous study (Van't Veer et al., 2016), PBP1BEc alone was unable to use lipid II-Atto550 and lipid II-Atto647n for polymerization when unlabelled lipid II was not present (Figure 1E, right). Surprisingly, addition of LpoB allowed PBP1BEc to produce short, non-crosslinked individual PG chains (Figure 1E, Figure 1—figure supplement 3B) that gave rise to a slow but large increase in FRET (Figure 1E, right, Figure 1—figure supplement 3A), indicating that polymerization of labelled lipid II occurred in the absence of unlabelled lipid II. To investigate this effect further, we varied the proportion of fluorescent lipid II over non-fluorescent (but radioactive) lipid II and measured the reaction slopes and, at the end of the reaction time, the final FIacceptor/FIdonor ratio and amounts of unused lipid II versions, in the presence or absence of activator (Figure 2—figure supplement 1). LpoB slightly increased consumption of all versions of lipid II by PBP1BEc (Figure 2—figure supplement 1A) but did not affect the proportion of fluorescent material that was incorporated into PG, which reflected the initial percentage of fluorescent lipid II (Figure 2—figure supplement 1B). In the absence of LpoB, the final FIacceptor/FIdonor ratio increased with increasing proportions of labelled lipid II, but this increase was steeper in the presence of LpoB (Figure 2—figure supplement 1C). As similar proportions of fluorescent material were incorporated into PG with or without activator, the difference in the final FRET must arise by fluorophores located closer together within the PG produced when LpoB is present. Finally, the reaction slopes did not change significantly with increasing proportions of labelled lipid II in the absence of LpoB but increased in its presence up to 50% of fluorescent lipid II, and then plateaued (Figure 2—figure supplement 1A). Overall, these results suggest that LpoB stimulates the incorporation of fluorophores in consecutive positions along the glycan chain and thus increases the contribution of intra-chain FRET. Thus, the increase in slopes observed with activator (Figure 1F) reflects not only a higher PG synthesis rate but also a higher contribution of intra-chain FRET.

### FRET assay to monitor PG synthesis in liposomes

To establish the FRET assay for membrane-embedded PG synthases, we reconstituted a version of PBP1BEc with a single cysteine at the cytoplasmic N-terminus into liposomes prepared from E. coli polar lipids (EcPL) (Figure 3—figure supplement 1A). The liposome-reconstituted PBP1BEc became accessible to a sulfhydryl-reactive fluorescent probe only after disrupting the liposomes with detergent (Figure 3A), showing that virtually all PBP1B molecules were oriented with the N-terminus inside the liposomes. This suggests that the large, extracellular portion of PBP1BEc is not transferred through the membrane during the reconstitution into liposomes (Rigaud and Lévy, 2003). Next, we reconstituted unmodified PBP1BEc and tested its activity by adding radioactive lipid II. In contrast to the detergent-solubilized enzyme, the liposome-reconstituted PBP1BEc required the absence of NaCl from the reaction buffer for improved activity (Figure 3—figure supplement 1B–E), suggesting that ionic strength affects either the structure of PBP1BEc in the membrane, the properties of EcPL liposomes, or the delivery of lipid II into the liposomes.

![Figure 3.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-v2.jpg)

**Figure 3.:** (A) Class A penicillin-binding proteins (PBPs) were reconstituted in E. coli polar lipid (EcPL) liposomes. To assess the orientation of the liposome-reconstituted PBPs, MGC-64PBP1B-his C777S C795S containing a single cysteine in the N-terminal region was reconstituted as in A. The accessibility of the cysteine was determined by staining with sulfhydryl-reactive fluorescent probe, Alexa Fluor555-maleimide, in the presence or absence of Triton X-100 (TX). Samples were analysed by SDS-PAGE with fluorescence scanning to detect labelled protein followed by Coomassie staining. (B) To perform activity assays in liposomes, class A PBPs were reconstituted along a 1:1 molar ratio mixture of Atto550-labelled lipid II and Atto647n-labelled lipid II in liposomes as in A. Reactions were started by addition of unlabelled lipid II in the presence or absence of lipoprotein activators (lpo). Using this methodology, we monitored the activity of PBP1BEc (C, D), PBP1BAb (E, F), and PBP1BPa (G, H). Representative reaction curves are shown. Reactions were carried out in the presence (blue lines) or absence (red lines) of the lipoprotein activators (LpoB(sol) for PBP1BEc, LpoPAb(sol) for PBP1BAb, and LpoPPa(sol) for PBP1BPa), and either in the absence of antibiotic (left) or presence of 1 mM ampicillin (Amp) or 50 µM moenomycin (Moe, black and yellow lines) (middle). For PBP1BEc, control reactions in the absence of unlabelled lipid II (right) are also shown. Products were analysed by SDS-PAGE followed by fluorescence scanning at the end of reactions (right side). Curves are numbered according to the corresponding lane on the SDS-PAGE gels. PBP1BEc, PBP1BAb, and PBP1BPa were reconstituted in EcPL liposomes containing labelled lipid II (0.5 mol% of lipids, 1:1 molar ratio mixture of Atto550-labelled lipid II and Atto647n-labelled lipid II), at protein-to-lipid molar ratios of 1:3000, 1:2000, and 1:3000, respectively. Reactions were started by adding unlabelled lipid II (final concentration 12 µM) and incubated at 37°C for 60 min (PBP1BEc and PBP1BAb) or 90 min (PBP1BPa) while monitoring fluorescence at 590 and 680 nm with excitation at 522 nm. (D), (F), and (H) show averaged initial slopes from reaction curves obtained by the FRET assay for liposome-reconstituted PBP1BEc, PBP1BAb, and PBP1BPa, respectively, in the presence (blue) or absence (red) of lipoprotein activators and in the presence or absence of ampicillin. Values are normalized relative to the slope in the absence of activator and are mean ± variation of two independent experiments.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Representative SDS-PAGE analysis of the reconstitution of PBP1BEc in liposomes made of E. coli polar lipids at a 1:3000 mol:mol protein:lipid ratio. After reconstitution, proteoliposome samples (lane 1) were centrifuged at low speed to remove aggregates and both pellet and supernatant samples were analysed (lanes 2 and 3, respectively). The supernatant was subsequently used for peptidoglycan (PG) synthesis reactions. A gradient of PBP1BEc (0.25, 0.41, 0.62, 0.82, 1.23, and 1.65 µg) was loaded as a standard to estimate protein concentration by densitometry. (B–D) Representative chromatograms showing the muropeptide analysis of PG produced by detergent-solubilized PBP1BEc (B) or liposome-reconstituted PBP1BEc in the presence or absence of NaCl (C and D, respectively). The concentration of PBP1BEC was 0.5 µM and, if added, that of LpoB(sol) was 2 µM LpoB(sol). The reaction buffer contained 150 mM NaCl in B and C. Samples were incubated at 37°C for 60 min in B and 90 min in C and D. The labelled peaks correspond to the muropeptides shown in Figure 1E. (E) Quantification of the total amount of radioactivity incorporated into PG (left) or the ratio between the radioactivity of peaks 3 and 2 (indicative of the degree of crosslinking of the PG, right) for activity assays for PBP1BEc in liposomes in the same conditions as in D. Values are mean ± SD (or variation) of at least two reactions.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Comparison of the two possible outcomes of FRET curves for reactions of PBP1BEc liposomes assayed in the presence of LpoB and ampicillin (left) and the final SDS-PAGE analysis of the same reactions (right). A third of assays in this condition resulted in curves similar to reaction I. Reaction conditions were the same as in Figure 3C. (B) The same gels depicted in Figure 3C, but scanned using the donor fluorescence (Atto550n). (C) Spectra corresponding to E. coli PBP1B reactions shown in Figure 3C, taken at t = 60 min. (D) Spectra corresponding to A. baumannii PBP1B reactions shown in Figure 3E, taken at t = 60 min. (E) Spectra corresponding to P. aeruginosa PBP1B reactions shown in Figure 3G, taken at t = 90 min.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) E. coli polar lipids liposomes incorporating an equimolar amount of lipid II-Atto550 and lipid II-Atto647n at 0.5% mol of the total lipid contents were incubated in the presence of 12 µM lipid II and in the presence (black line) or absence (red line) of 50 µM moenomycin for 60 min at 37°C while monitoring FRET as indicated in Materials and methods. (B) Fluorescence spectra for the samples described in A at the end of the incubation period (t = 60 min).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** FI at the acceptor and donor emission wavelengths (590 and 680 nm, respectively) only changed significantly when there was peptidoglycan synthesis activity in liposomes and both lipid II-Atto647n and lipid II-Atto550 were co-reconstituted in the same liposomes. Moreover, these changes were indicative of Förster resonance energy transfer (decrease at the donor wavelength and increase at the acceptor wavelength). (A) Reactions with PBP1BEc reconstituted in liposomes along different combinations of labelled substrates (lipid II-Atto550, yellow; lipid II-Atto647n, red; or a mixture of both, blue) were monitored in real time by measuring fluorescence intensity at 590 nm (bottom row) and 680 nm (top row). Reactions with lipid II-Atto647n only were monitored at 680 nm only. Reactions were performed in four conditions (left to right): with no antibiotics, with 1 mM ampicillin, with 100 µM moenomycin, or omitting unlabelled lipid II. Changes in FI were normalized by calculating the ratio FI(ti)/FI(t = 0). (B) Same reactions as in A, but performed in the presence of activator LpoB. In both A and B, reactions were started by addition of 12 or 24 µM non-fluorescent lipid II (for reactions with both fluorescent lipid II variants or reactions with variants, respectively), except in the indicated control condition.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (A) In the genomes of A. baumannii and P. aeruginosa, the gene encoding LpoP is present within the same operon as the gene encoding their cognate PBP1B. Both LpoP proteins are predicted lipoproteins with a disordered region between the N-terminal Cys and the C-terminal globular domain containing the tetratricopeptide repeats (TPRs). LpoPAb has a shorter disordered linker than LpoPPa. (B) Sequence comparison between the globular regions of LpoPAb (Ab) and LpoPPa (Pa). Proteins sequences (minus the signal peptides) were aligned using T-COFFEE EXPRESSO, and the resulting alignment was visualized using JALVIEW. Residues conserved in both proteins are highlighted in a darker colour.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** (A) Real-time glycosyltransferase activity assays using dansyl-lipid II and detergent-solubilized A. baumannii PBP1B (PBP1BAb). PBP1BAb (0.5 µM) was mixed with 10 µM dansyl-lipid II in the presence or absence of soluble 0.5 µM A. baumannii LpoP (LpoPAb(sol)). A control was performed by adding 50 µM moenomycin (black). Each data point represents mean ± SD of three independent experiments. (B) Averaged initial slopes from reaction curves in A. Values are normalized relative to the slope in the absence of activator and are mean ± SD of three independent experiments. (C) Time-course GTase assay by SDS-PAGE followed by fluorescence detection. Detergent-solubilized PBP1BAb was incubated with 5 µM lipid II-Atto550 and 25 µM unlabelled lipid II in the presence or absence of 1.5 µM LpoPAb(sol). Reactions contained 1 mM ampicillin to block transpeptidation. Aliquots were taken at the indicated times (in min), boiled, and analysed by SDS-PAGE. A control in which only LpoPAb(sol) was present is also shown.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** (A) Representative FRET curves for activity assays using detergent-solubilized A. baumannii PBP1B (PBP1BAb). PBP1BAb (0.5 µM) was mixed with unlabelled lipid II, Atto550-labelled lipid II, and Atto647n-labelled lipid II at a 1:1:1 molar ratio (5 µM of each) in the presence or absence of 2 µM soluble A. baumannii LpoP (LpoPAb(sol)). Controls were performed by adding 50 µM moenomycin in the absence (black) or presence (yellow) of LpoPAb(sol). Reactions were performed without antibiotic (left), with 1 mM ampicillin (middle), or in the absence of unlabelled lipid II (right). The numbers indicate the corresponding lane of the gel in C. Samples were incubated for 60 min at 30°C. (B) Averaged initial slopes from reaction curves obtained by the FRET assay for detergent-solubilized PBP1BAb in the presence (blue) or absence (red) of LpoP and in the presence or absence of ampicillin. Values are normalized relative to the slope in the absence of activator for each condition and are mean ± SD of two independent experiments. (C) Aliquots after reactions in A were boiled and analysed by SDS-PAGE followed by fluorescence detection. (D) Fluorescence emission spectra taken after reactions in A (t = 60 min).

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig3-figsupp8-v2.jpg)

**Figure 3—figure supplement 8.:** (A) Representative FRET curves for activity assays using detergent-solubilized P. aeruginosa PBP1B (PBP1BPa). PBP1BPa (0.5 µM) was mixed with unlabelled lipid II, Atto550-labelled lipid II, and Atto647n-labelled lipid II at a 1:1:1 molar ratio (5 µM of each) in the presence or absence of 2 µM soluble P. aeruginosa LpoP (LpoPPa (sol)). Controls were performed by adding 50 µM moenomycin in the absence (black) or presence (yellow) of LpoPPa(sol). Reactions were performed without antibiotic (left), with 1 mM ampicillin (middle), or in the absence of unlabelled lipid II (right). The numbers indicate the corresponding lane of the gel in C. Samples were incubated for 90 min at 37°C. (B) Averaged initial slopes from reaction curves obtained by the FRET assay for detergent-solubilized PBP1BPa in the presence (blue) or absence (red) of LpoP and in the presence or absence of ampicillin. Values are normalized relative to the slope in the absence of activator for each condition and are mean ± SD of 2–3 independent experiments. (C) Aliquots after reactions in A were boiled and analysed by SDS-PAGE followed by fluorescence detection. (D) Fluorescence emission spectra taken after reactions in A (t = 90 min).

We next aimed to adapt the FRET assay to study PG synthesis on liposomes to mimic the situation in the cell (Figure 3, Figure 3—figure supplement 2). As PBP1BEc did not accept Atto550- or Atto647-derivatized lipid II for GTase reactions in the absence of unlabelled lipid II (Figure 1E), we reconstituted PBP1BEc in liposomes along both Atto-labelled substrates and initiated the reaction by adding unlabelled lipid II (Figure 3B). PBP1BEc reaction rates in liposomes were slower than in the presence of Triton X-100 for all conditions tested (compare curves in Figure 3C, measured at 37°C, with the ones in Figure 1E, measured at 25°C), and there was a longer lag time before FRET started to increase (Figure 3C, left). Moenomycin blocked the increase in FRET, while ampicillin reduced the final FRET levels (Figure 3C, middle). For unknown reasons, the FRET signal with moenomycin was initially higher than without moenomycin and then decreased to initial values without moenomycin (Figure 3C, middle), independent of the class A PBP used (see below) but not in empty liposomes (Figure 3—figure supplement 3). LpoB(sol) produced an approximately tenfold increase in the initial slope, measured as explained above (Figure 3D), and the resulting final FRET was much higher (Figure 3C, left). In some experiments with PBP1BEc liposomes in the presence of ampicillin and LpoB(sol), we noticed a slow decrease in FRET after a fast initial increase, and the production of short glycan chains instead of the long chains produced normally (Figure 3—figure supplement 2A). As in detergents, without unlabelled lipid II membrane-bound PBP1B produced a FRET signal only in the presence of LpoB(sol) (Figure 3C, right). The analysis of the final products by SDS-PAGE confirmed that both Atto550 and Atto647n were incorporated into glycan chains or crosslinked PG during the reaction in liposomes (Figure 3C, right, Figure 3—figure supplement 2B). As expected, controls with PBP1BEc liposomes reconstituted with only lipid II-Atto550 or only lipid II-Atto647n showed significantly lower changes in FIdonor and FIacceptor than when both fluorescent versions were present together (Figure 3—figure supplement 4).

In summary, using our FRET-based assay we demonstrated real-time monitoring PG synthesis in membrane by PBP1BEc and showed that the FRET signal was sensitive to the presence of PG synthesis inhibitors (moenomycin and ampicillin).

### Activities of other membrane-bound class A PBPs

To demonstrate the usefulness of the FRET assay to study class A PBPs of potential therapeutic interest, we next tested two PBP1B homologues from Gram-negative pathogens, Acinetobacter baumannii (PBP1BAb) and Pseudomonas aeruginosa (PBP1BPa). We set up reactions in the presence or absence of a soluble version of the lipoprotein activator LpoPPa(sol) for PBP1BPa (Greene et al., 2018). There is currently no reported activator of PBP1BAb, but next to the gene encoding PBP1BAb we identified a hypothetical gene encoding a lipoprotein containing two tetratricopeptide repeats (Uniprot code D0C5L6) (Figure 3—figure supplement 5) which we subsequently found to activate PBP1BAb (see below, Figure 3—figure supplement 6). We named this protein LpoPAb and purified a version without its lipid anchor, called LpoPAb(sol). We were able to monitor PG synthesis activity by FRET for both PBPs in the presence or absence of their (hypothetical) activators using the Triton X-100-solubilized (Figure 3—figure supplements 7 and 8) or liposome-reconstituted proteins (Figure 3E–H, Figure 3—figure supplement 2D–E). Our experiments revealed the differences in the activities and the effect of activators between both PBP1B-homolgoues which we discuss in the following paragraphs.

PBP1BAb showed GTase activity in the presence of Triton X-100 (Figure 3—figure supplement 6A) and was stimulated ~3.3-fold by LpoPAb(sol) (Figure 3—figure supplement 6B); LpoPAb(sol) also accelerated the consumption of lipid II-Atto550 and glycan chain polymerization (Figure 3—figure supplement 6C). We measured a low FRET signal for PG produced by the detergent-solubilized enzyme in the FRET assay (Figure 3—figure supplement 7A) and poor production of crosslinked PG (Figure 3—figure supplement 7C), unlike in the case of the other PBPs. However, the liposome-reconstituted PBP1BAb displayed a higher TPase activity than the detergent-solubilized enzyme (compare gels in Figure 3E, right, and Figure 3—figure supplement 7C). In addition, the final FRET signal was substantially higher in liposomes than in detergents (Figure 3E, Figure 3—figure supplement 7A). Moenomycin completely blocked FRET development, while ampicillin had a negligible effect on the final FRET levels in detergents and only a small effect in liposomes (~1.2-fold reduction), indicating that intra-chain FRET is the major contributor to FRET (Figure 3E, Figure 3—figure supplement 7A). LpoPAb(sol) stimulated PBP1BAb, with a higher effect in detergents (12.3-fold increase) than liposomes (~2.5-fold increase) (Figure 3E, F, Figure 3—figure supplement 7A, B).

PBP1BPa displayed robust TPase activity in detergents and liposomes (Figure 3G, right, Figure 3—figure supplement 8C), and ampicillin reduced the final FRET signal by ~1.8-fold in Triton X-100 and ~1.5-fold in liposomes, indicating a substantial contribution of inter-chain FRET to the FRET signal (Figure 3G, Figure 3—figure supplement 8A). The addition of LpoPPa(sol) resulted in an increase in the final FRET by ~2.2-fold in the membrane and ~2.1-fold in detergents (Figure 3G, Figure 3—figure supplement 8A), and accelerated initial slopes by ~4.2-fold in the membrane and ~11.5-fold in detergents (Figure 3H, Figure 3—figure supplement 8B); lipid II consumption was increased under both conditions (Figure 3G, right, Figure 3—figure supplement 8C). Overall, these results indicate that LpoPPa(sol) stimulates both GTase and TPase activities in agreement with a recent report (Caveney et al., 2020).

### PG synthesis on supported lipid bilayers

As we were able to successfully reconstitute active class A PBPs in membranes and monitor their activity in real time, we next aimed to characterize the behaviour of these enzymes in the membrane in more detail by reconstituting them on supported lipid bilayers (SLBs). SLBs are phospholipid bilayers formed on top of a solid support, usually a glass surface, and they allow for studying the spatial organization of transmembrane proteins and their diffusion along the membrane by fluorescence microscopy at high spatiotemporal resolution.

We optimized the reconstitution of PBP1BEc in SLBs formed with EcPL and used the optimized buffer conditions for activity assays on liposomes. To support lateral diffusion and also improve stability of the proteins incorporated into SLBs, we employed glass surfaces coated with polyethylene glycol (PEG) end-functionalized with a short fatty acid (Roder et al., 2011) to anchor the EcPL bilayer (Figure 4A). We noticed a decrease in membrane diffusivity and homogeneity at a high surface density of PBP1BEc (Figure 4—figure supplement 1). To maintain the integrity of the SLB, we reduced the density of PBP1BEc on SLBs from ~10−3 mol protein/mol lipid in liposomes to a range of 10−6 to 10−5 mol protein/mol lipid. Using a fluorescently labelled version of PBP1BEc reconstituted in SLBs, we were able to track the diffusion of single PBP1B molecules in the plane of lipid membrane in the presence or absence of substrate lipid II by total internal reflection fluorescence (TIRF) microscopy (Figure 4B, D, Video 1). PBP1BEc diffused on these supported bilayers with an average Dcoef of 0.23 ± 0.06 µm2/s. Addition of lipid II slowed down PBP1BEc diffusion (Figure 4C), resulting in a lower average Dcoef of 0.10 ± 0.06 µm2/s. Upon addition of lipid II, we could not detect a prolonged confined motion within particle tracks (Figure 4D); however, the average length of displacements between two sequential frames was reduced (Figure 4E). Thus, we successfully reconstituted diffusing PBP1BEc in SLBs and observed that lipid II binding slowed down the diffusion of the synthase.

![Figure 4.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig4-v2.jpg)

**Figure 4.:** (A) Schematic illustration of the approach (not to scale). A single-cysteine version of PBP1BEc (MGC-64PBP1B-his C777S C795S) labelled with fluorescent probe Dy647 in its single Cys residue (PBP1BEc-Dy647) was reconstituted into a polymer-supported lipid membrane formed with E. coli polar lipids, and its diffusion was monitored using TIRF microscopy in the presence or absence of substrate lipid II. (B) Single-molecule TIRF micrograph of PBP1BEc-Dy647 diffusing in the lipid membrane in the presence of 1.5 µM lipid II (corresponding to Video 1). Calculated particle tracks are overlaid. (C) Histograms of diffusion coefficients (Dcoef) of PBP1BEc-Dy647 particles in the presence (red) or absence (black) of lipid II. The average Dcoef decreased from 0.23 ± 0.06 µm2/s to 0.1 ± 0.04 µm2/s upon addition of lipid II. Values are mean ± SD of tracks from three independent experiments. (D) Representative tracks for diffusing PBP1BEc-Dy647 particles in the absence (black, top) or presence of lipid II (red, bottom), showing the absence of confined motion in the presence of lipid II. (E) Displacement distributions of PBP1BEc-Dy647 particles (solid lines) in the absence (left) or presence (right) of lipid II were analysed using a Rayleigh model incorporating two populations of particles, a fast-diffusing one (grey dashed lines) and a slow-diffusing one (black dashed lines). In the absence of lipid II, only 8 ± 5% of the steps were classified into the slow fraction (121 ± 6 nm average displacement), while the majority of steps were of 257 ± 6 nm (fast fraction). The slow fraction increased upon addition of lipid II to 37 ± 5% of the steps, with an average displacement of 132 ± 16 nm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) The fluidity of supported lipid bilayers (SLBs) is reduced when increasing PBP1BEc density. The diffusion of phospholipid probe DOPE-rhodamine in the polymer-supported SLB was monitored by fluorescence recovery after photobleaching (FRAP) at different densities of PBP1B. The fluidity of the membrane decreased (black line) while the immobile fraction increased (orange line) with higher protein densities.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A, B) PBP1BEc was reconstituted on supported lipid bilayers prepared with E. coli polar lipid extract in 1.1 cm2 chambers. The protein-to-lipid ratio was 1:105 (mol:mol). Reactions were started by adding 1 nmol of radiolabelled lipid II per chamber in the presence of LpoB(sol) (4 µM) moenomycin (100 µM). Three chambers were prepared for each condition, and samples were combined before the analysis. Chambers were incubated overnight at 37°C, and the reaction was stopped by adding moenomycin. Cellosyl and Triton X-100 were added to solubilize the membranes and digest the peptidoglycan (PG) product. The resulting muropeptide samples were concentrated, reduced with sodium borohydride, and analysed by HPLC. Full chromatograms are shown in A, while zoomed-in chromatograms are shown in B. (C, D) PG synthesis occurs only in the membrane fraction of SLBs. PBP1BEc was reconstituted on SLBs as in A and B. In addition, control chambers were prepared without PBP1B. Chambers were incubated overnight to allow for PG synthesis and then washed with fresh buffer. The washes and chambers (membranes) were treated and analysed as described for A and B. Five chambers were combined for reactions with PBP1BEc and four chambers for control reactions. Full chromatograms are shown in C, while zoomed-in chromatograms are shown in D. The labelled peaks in all chromatograms correspond to the muropeptides shown in Figure 1F.

![Video 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-video1.mp4.jpg)

**Video 1.:** PBP1BEc-Dy647 was reconstituted in E. coli polar lipids SLBs at a 1:106 (mol:mol) protein-to-lipid ratio and was tracked using single-molecule TIRF before or after the addition of 1.5 µM lipid II. Images were taken with a rate of 62 ms per frame.

Next, we wanted to confirm that PBP1BEc remained active to produce planar bilayer-attached PG. We incubated SLBs containing PBP1BEc with radioactive lipid II and digested any possible PG produced with a muramidase and analysed the digested material by HPLC. Due to the low density and amount of PBP1BEc on each SLB chamber, we expected a small amount of PG product; hence, we included LpoB(sol) to boost the activity of PBP1BEc. Under these conditions, about 12% of the added radiolabelled lipid II was incorporated into PG after an overnight incubation (Figure 4—figure supplement 2A). However, products of both the GTase and TPase activities of PBP1BEc were detected, and these products were absent in the presence of moenomycin (Figure 4—figure supplement 2B). After overnight PG synthesis reactions with radioactive lipid II, about 32% of the radioactivity remained in the membrane fraction after washing (PG products and unused lipid II) and 68% was in the supernatant. The analysis of the membrane and wash fractions by HPLC (Figure 4—figure supplement 2C, D) revealed that SLB-reconstituted PBP1BEc produced crosslinked PG while, importantly, the wash fraction contained no PG products, confirming that the PG synthesis occurred on the SLBs and this PG remained attached to the bilayer. The fraction of membrane-attached radioactivity was almost the same (33%) when PBP1BEc was not present in the bilayer, indicating that PBP1BEc did not affect lipid II binding to the bilayer.

### FRET assay on supported bilayers

Next, we adapted the FRET assay to SLBs and TIRF microscopy, taking advantage of the photostability and brightness of the Atto550 and Atto647n probes. Our aim was to visualize PG synthesis by class A PBPs at high resolution as a first step towards understanding PG synthesis at a single molecule level. We used a similar approach as for liposomes, where both Atto550- and Atto647n-labelled lipid II were co-reconstituted with PBP1BEc on SLBs and PG synthesis was triggered by the addition of unlabelled lipid II (Figure 3A). To measure any change in FRET due to PG synthesis, we took advantage of the fact that upon photobleaching of the acceptor probe in a FRET pair the emitted fluorescence intensity of the donor increases as absorbed energy cannot be quenched by a nearby acceptor (Loose et al., 2011; Verveer et al., 2006). Indeed, we detected an increase in lipid II-Atto550 fluorescence intensity upon photobleaching of the Atto647n probe after the addition of unlabelled lipid II and LpoB(sol), indicating the presence of FRET (Figure 5A, Figure 5—figure supplement 1A). When we bleached the acceptor at different time points of the reaction, we found the FRET signal to increase after a lag phase of ~8 min. Importantly, there was no FRET increase in the presence of ampicillin (Figure 5B, Figure 5—figure supplement 1A, Video 2) or when a GTase-defective PBP1BEc version (E233Q) was used (Figure 5C). In addition, the FRET signal was abolished when the muramidase cellosyl was added after the PG synthesis reaction (Figure 5C). These results imply that the FRET signal detected by microscopy is primarily due to the transpeptidase activity of PBP1BEc, in agreement with the results obtained on liposomes (Figure 5C).

![Figure 5.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig5-v2.jpg)

**Figure 5.:** (A) FRET acquisition by TIRF microscopy. PBP1BEc was reconstituted into a polymer-supported lipid membrane to preserve its lateral diffusion. A supported lipid membrane was formed from E. coli polar lipid extract supplemented with 0.5 mol% of labelled lipid II (Atto550 and Atto647n at 1:1 ratio). To initiate peptidoglycan (PG) polymerization, unlabelled lipid II (10 µM) and LpoB(sol) (4 µM) were added from the bulk solution. An increase in FRET efficiency was recorded by dual-colour TIRF microscopy: the acceptor (lipid II-Atto647n) was photobleached, and the concomitant increase in the donor intensity (lipid II-Atto550) was recorded within a delay of 1 s. (B) FRET kinetics of PG polymerization and crosslinking. Inhibition of PBP1BEc TPase activity with 1 mM ampicillin did not produce any changes in the donor intensity, confirming that FRET signal is specific to crosslinked PG. A sigmoid (straight lines) was fitted to the data to visualize the lag in the increase of FRET signal. (C) FRET efficiency was measured after a round of PG synthesis before and after digestion with the muramidase cellosyl. After cellosyl digestion, FRET efficiency decreased by 2.5-fold, resulting in a FRET signal comparable to the one of a control surface with a GTase-defective PBP1BEc(E233Q), performed in parallel. Each dot corresponds to a different surface area within the same sample. (D) Quantification of the diffusion coefficient of lipid II-Atto647n over the time course of PG polymerization (left) from the experiment presented in B, calculated from the dynamics of the recovery of lipid II-Atto647n signal within the photobleached region of interest (ROI). (E) Quantification of the fraction of immobile lipid II-Atto647n from several experiments as the one depicted in B; each dot represents the value from a different experiment. (F) Diffusion of lipid II-Atto647n or a phospholipid bound probe labelled with Alexa 488 (supported lipid bilayer) was recorded in a FRAP assay using a 1 s delay and dual-colour imaging, 30 min after initiation of PG synthesis by addition of lipid II and LpoB(sol). Only the diffusion of lipid II, but not of a fluorescently labelled, His6-tagged peptide attached to dioctadecylamine-tris-Ni2+-NTA, was affected by the presence of ampicillin during the PG synthesis reaction.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Fluorescence intensity profiles 1 s after photobleaching taken from the images depicted in Figure 4B. (B) Montage comparing the recovery of fluorescence after photobleaching of a tracer (DODA-tris-Ni-NTA plus a His6-tagged peptide labelled with Alexa Fluor 488) with the one of lipid II-Atto647n on a supported lipid bilayer containing PBP1B at a 1:105 protein:lipid (mol:mol) ratio. The assay was performed after a peptidoglycan synthesis reaction was carried out for 1.5 hr. The fact that fluorescence is recovered for both indicates that the membrane remains fluid while lipid II stays diffusive after the synthesis reaction.

![Video 2.](https://cdn.elifesciences.org/articles/61525/elife-61525-video2.mp4.jpg)

**Video 2.:** PBP1BEc was reconstituted in E. coli polar lipids SLBs at a 1:105 (mol:mol) protein-to-lipid ratio along lipid II-Atto647 and lipid II-Atto550. Membranes were incubated with 5 µM lipid II in the presence or absence of 1 mM ampicillin. To detect FRET, the fluorescence of the acceptor Atto647n was bleached within a region. In the subsequent frame, the fluorescence of Atto550 increased, indicating the presence of FRET. In the presence of ampicillin, this increase did not happen.

### PG synthesized on SLBs

As our experiments confirmed that the PG synthesized by PBP1BEc on SLBs remained attached to the bilayer, we next analysed the lateral diffusion of lipid II-Atto647n and its products during PG synthesis reactions. We first analysed the recovery of fluorescence intensity after photobleaching to monitor the diffusion of lipid II-Atto647n during PG synthesis (Figure 5D). Only when crosslinking was permitted (absence of ampicillin), the diffusion coefficient of lipid II-Atto647n decreased two- to threefold in a time-dependent manner. The time needed to reach the minimum diffusivity value (~10 min) was similar to the lag detected in the increase of FRET efficiency (Figure 5B). The fraction of immobile lipid II-Atto647n did not change significantly in the presence or absence of ampicillin (13 ± 2% or 18 ± 6%, respectively, p-value=0.15) (Figure 5E), indicating that the crosslinked PG was still mobile under these conditions, but diffused more slowly. We also compared the diffusion of lipid II-Atto647n during the PG synthesis reaction with that of an Alexa Fluor 488-labelled membrane-anchored peptide in the presence or absence of ampicillin (Figure 5F, Figure 5—figure supplement 1B). The inhibition of TPase by ampicillin only affected the diffusivity of lipid II (2.9 ± 0.4 µm2/s with ampicillin and 0.67 ± 0.1 µm2/s without), while that of the lipid probe remained unchanged (1.6 ± 0.65 µm2/s with ampicillin and 1.94 ± 0.62 µm2/s without). This shows that the membrane fluidity was not altered by the PG synthesis reaction and therefore was not the cause of the change in lipid II diffusivity upon transpeptidation. As the immobile fraction of labelled lipid II did not increase after PG synthesis and the diffusion was reduced only two- to threefold, we concluded that lipid II-Atto647n was incorporated into small groups of crosslinked glycan chains which can still diffuse on the bilayer.

In summary, we report the incorporation of active PBP1BEc into SLBs, where we could track a decrease in the diffusion of the protein and its substrate during PG synthesis reactions. Using this system, we detected an increase in FRET upon initiation of PG synthesis, only occurring when transpeptidation was not inhibited.

## Discussion

Although class A PBPs are membrane proteins and PG precursor lipid II is embedded in the bilayer, few studies have provided information about the activity of these important enzymes in a membrane environment. Here, we developed a new assay that reports on PG synthesis by these enzymes in detergents, on liposomes, or on SLBs.

### Intra-chain vs. inter-chain FRET

For all PBPs and conditions tested, FRET increased when only the GTase domain was active (i.e., when FRET occurred between probes incorporated along the same strand), but the FRET signal was always higher when transpeptidase was active (Figures 1–3, Figure 3—figure supplements 7 and 8). For detergent-solubilized PBP1BEc, the FRET curve closely followed the rate of the production of crosslinked PG as determined by HPLC analysis of the products (Figure 2C–E), and the FRET of PBP1BEc-produced labelled PG decreased substantially upon digestion with an endopeptidase (Figure 2A, B). These results indicate that inter-chain FRET (arising from both fluorophores present on different, adjacent glycan chains) was a main component of the total FRET signal. Why is this the case? FRET depends on the distance and orientation of the two probes. It might be sterically unfavourable that two large Atto550 and Atto647n containing lipid II molecules simultaneously occupy the donor and acceptor sites in the GTase domain (Van't Veer et al., 2016), preventing the incorporation of probes (and high FRET) at successive subunits on a single glycan chain. Indeed, for all PBPs tested either in detergents or liposomes, the incorporation of labelled lipid II into glycan chains was more efficient when unlabelled lipid II was present, and, for most enzymes, an activator was required to polymerize glycan chains using labelled lipid II in the absence of unlabelled lipid II. We thus hypothesize that the TPase activity brings glycan chains to close proximity, reducing the distance between probes sufficiently to produce high levels of FRET (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/61525/elife-61525-fig6-v2.jpg)

**Figure 6.:** (A) A mixture of Atto550-lipid II, Atto647n-lipid II, and unlabelled lipid II is utilized by a class A penicillin-binding protein (PBP) with or without inhibition of the TPase activity by a β-lactam. FRET can only occur between fluorophores within the same glycan strand in linear glycan chains produced in the presence of a β-lactam (left reaction, dashed arrows). When the TPase is active (right reaction), FRET can occur either between probes within the same strand (dashed arrows) or between probes on different strands of the crosslinked PG product (solid arrows). We hypothesize that at any time only one labelled lipid II molecule occupies the two binding sites in the GTase domain and that therefore two probes within the same strand are separated by at least one subunit. As a result, average distances between probes in different strands may be shorter than between probes within the same strand, and thus inter-chain FRET contributes stronger to the total FRET signal than intra-chain FRET. (B) Lipoprotein-stimulated PBPs produced short chains when labelled lipid II versions were incubated in the absence of unlabelled lipid II (e.g., Figure 1B, Figure 1—figure supplement 1C). In this situation, crosslinking does not occur due to the attachment of the probe to the mDAP residue in the pentapeptide. Within these short strands, intra-chain FRET is stronger than within the long glycan strands depicted in (A) due to a shorter average distance between the probes.

### Limitation of the FRET assay

The FRET assay is sensitive and currently the only method that allows to follow PG synthesis continuously in the membrane. Naturally, there are also limitations with the assay. First, the overall FRET signal is a combination from intra-chain and inter-chain FRET, which both depend on the average distances and orientation of the fluorophore molecules on the growing glycan chains. We currently do not have a method to measure these parameters individually and determine whether and how they change during the process of PG synthesis, preventing the determination of absolute rates for GTase and TPase reactions. Second, different class A PBPs may produce slightly different distribution and density of fluorophores in the PG synthesized, hence differences in FRET signals may not always reflect different reaction rates. Third, an activator can potentially enhance the ability of a class A PBP to incorporate the fluorescent lipid II analogues, as we observed for LpoBEc and PBP1BEc, leading to an increase in intra-chain FRET. Due to these limitations, the assay is inherently semi-quantitative, but with appropriate control samples (β-lactams; only labelled lipid II) it is possible to determine whether the FRET signal follows more the GTase (intra-chain FRET) or TPase (inter-chain FRET) reaction.

### Coupled reactions in class A PBPs and their activation

Our assay revealed the effect of Lpo activators on PBP1B analogues from three bacteria. P. aeruginosa uses LpoP to stimulate its PBP1B (Greene et al., 2018; Caveney et al., 2020). Here, we identified an LpoP homologue in A. baumannii and showed that it stimulated its cognate PBP1B. All three PBP1B homologues started the reaction after a lag phase, which was abolished by the addition of the cognate activator (Egan et al., 2014; Caveney et al., 2020) Considering the recently described role of PBP1B in repairing cell wall defects (Vigouroux et al., 2020; Morè et al., 2019), the slow start in polymerization and its acceleration by Lpo activators could be an important mechanism to start PG synthesis at gaps in the PG layer where the activators can contact the synthase.

To distinguish the effects of an activator on the TPase and GTase rates requires to use different assays to measure GTase only or GTase/TPase because ongoing glycan chain polymerization is required for transpeptidation to occur (Bertsche et al., 2005; Gray et al., 2015). An elegant recent report (Catherwood et al., 2020) described the use of a coupled D-Ala release assay to determine the kinetic parameters of the TPase activity of PBP1BEc and the effect of LpoB on this rate. Based on their observation that PBP1BEc had barely any TPase activity in the absence of LpoB, the authors concluded that the LpoB-mediated TPase activation explains the essentiality of LpoB for PBP1B function in the cell (Catherwood et al., 2020). However, the assay used an enzyme concentration that is too low to support GTase activity in the absence of LpoB, as demonstrated previously (Pazos et al., 2018; Müller et al., 2007). Therefore, the essentiality of LpoB can be readily explained by its primary effect, the greater than tenfold stimulation of the GTase rate (Egan et al., 2014). Our results provide an alternative explanation for PBP1BEc essentiality. Activation by LpoB was much more needed when PBP1B was embedded in the membranes of liposomes and supported bilayers, compared to detergent-solubilized enzyme, supporting the idea that cellular PBP1B strictly requires LpoB for GTase activity. In vitro, LpoB also stimulated the TPase causing PBP1BEc to produce a hyper-crosslinked PG (Typas et al., 2010; Egan et al., 2018) and the same was observed for LpoPPa and PBP1BPa (Caveney et al., 2020). The GTase and TPase contribute both to the signal in our FRET assay, and the relative contribution of intra-chain FRET (due to the GTase) and inter-chain FRET (due to the TPase) can be modified by an activator that enables the incorporation of two adjacent probe molecules on the same glycan chain. Therefore, to untangle the effects of activators on each of the activities requires a single quantitative model accounting for the GTase and TPase rates and including parameters for the initiation, elongation, and termination of glycan chain synthesis of membrane-embedded enzymes. Currently, such a model is not available and our assay could help to develop such a model in the future.

### Class A PBP activities in the membrane

Remarkably, we found slower reaction rates in liposomes than in detergents for all enzymes tested. Several possible factors can explain this, including a slow incorporation of the added unlabelled lipid II into liposomes, a limited capacity of the liposomes to incorporate the unlabelled lipid II, or the accumulation of the undecaprenyl pyrophosphate by-product that has been showed to inhibit PBP1B activity (Hernández-Rocamora et al., 2018). None of these factors should change in the presence of LpoB. Hence, we favour the alternative explanation that the membrane-embedding of PBP1B hinders lipid II binding, slowing down the reaction. Remarkably, PBP1BAb showed higher TPase activity in liposomes than in detergents. This observation highlights again that detergents can affect the activity of membrane proteins and that experimental conditions in PG synthesis assays should be as close as possible at the physiological conditions.

### Towards single-molecule PG synthesis

We also adapted the FRET assay to SLBs and super resolution microscopy to study how PBP1BEc polymerizes PG on SLBs (Figure 5). As with the liposome assays, we detected an increase in FRET signal upon triggering PG synthesis that correlated with transpeptidation. Importantly, we could follow the diffusion of the reaction products, which indicates that PBP1BEc does not completely cover the surfaces with a layer of PG but instead produced smaller patches of crosslinked glycan chains. We attribute this to the fact that PBP1BEc was reconstituted at a very low density in order to ensure the homogeneity and stability of the SLBs. Remarkably, we detected a reduction of PBP1BEc diffusivity in the presence of lipid II (Figure 4). Previous in vivo single-molecule tracking of fluorescent-protein tagged class A PBPs reported the presence of two populations of molecules, a fast diffusing one and an almost immobile one with a near-zero diffusing rate, which was assumed to be the active population (Cho et al., 2016; Lee et al., 2016; Vigouroux et al., 2020). Our result supports this interpretation, although more experiments are required to further explore this point.

Several real-time methods to study PG synthesis in vitro are described in the literature. However, most of these report on either the GTase or TPase reaction, but not both at the same time, and most available methods are not applicable to the membrane. The scintillation proximity assay by Kumar et al. reports on PG production in a membrane environment and in real time, but it is rather crude in that it uses membrane extract instead of purified protein and relies on the presence of lipid II-synthesizing enzymes present in the extract (Kumar et al., 2014). Moreover, it uses radioactivity detection and is not amenable to microscopy, in contrast to methods based on fluorescently labelled substrates. An important advantage of our new assay over other real-time PG synthesis assays is that it uses natural substrates for transpeptidation, that is, nascent glycan strands, instead of mimics of the pentapeptide, and its ability to measure the activities in a natural lipid environment.

Our new FRET assay can potentially be adopted to assay PG synthases in the presence of interacting proteins, for example, monofunctional class B PBPs in the presence of monofunctional GTases (cognate SEDS proteins or Mtg proteins) or interacting class A PBPs (Meeske et al., 2016; Bertsche et al., 2006; Sjodt et al., 2020; Derouaux et al., 2008; Banzhaf et al., 2012; Sjodt et al., 2018; Taguchi et al., 2019). In addition, our assay has the potential to be adopted to high-throughput screening for new antimicrobials.

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
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3)</td>
      <td>New England Biolabs</td>
      <td>C2527</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pDML219</td>
      <td>Bertsche et al., 2006</td>
      <td></td>
      <td>Expression of N-terminal His-tagged E. coli PBP1B</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKPWV1B</td>
      <td>This paper</td>
      <td></td>
      <td>Expression of N-terminal His-tagged Acinetobacter baumannii19606 (ATCC) PBP1B</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAJFE52</td>
      <td>Caveney et al., 2020</td>
      <td></td>
      <td>Expression of N-terminal His-tagged Pseudomonas aeruginosa PBP1B</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMGCPBP1BCS1CS2</td>
      <td>This paper</td>
      <td></td>
      <td>Expression of E. coli PBP1B version with a single Cys residue in the N-terminus and C-terminal His-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET28His-LpoB(sol)</td>
      <td>Egan et al., 2014</td>
      <td></td>
      <td>Expression of soluble version of E. coli LpoB with an N-terminal His-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKPWVLpoP</td>
      <td>This paper</td>
      <td></td>
      <td>Expression of N-terminal His-tagged A. baumannii 19606 (ATCC) LpoP</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAJFE57</td>
      <td>Caveney et al., 2020</td>
      <td></td>
      <td>Expression of soluble version of P. aeruginosa LpoP with an N-terminal His-tag</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PBP1B.Acineto-NdeI_f</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>AGATATCATATGATGAAGTTTGAACGTGGTATC GGTTTCTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PBP1B.Acineto-BamHI_r</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>GCGGGATCCTTAGTTGTTATAACTACCACTTGA AATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Seq1_rev_PBP1B_Acineto</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>AGGTTCTAAACGGGCAACTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Seq2_fwd_PBP1B_Acineto</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>TGGTTATGGATTGGCCTCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Seq3_fwd_PBP1B_Acineto</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>CTGGGCAAGCCAGATTGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Seq4_fwd_PBP1B_Acineto</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>ACAATTACGCCAGACACCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PBP1B-MGC-F</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>CATCATCCATGGGCTGTGGCTGGCTATGGCTACTGCTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PBP1B-CtermH-R</td>
      <td>This paper</td>
      <td>PCR cloning primers</td>
      <td>CATCATCTCGAGATTACTACCAAACATATCCTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>C777S-D</td>
      <td>This paper</td>
      <td>PCR mutagenesis primers</td>
      <td>AACTTTGTTTCCAGCGGTGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>C777S-C</td>
      <td>This paper</td>
      <td>PCR mutagenesis primers</td>
      <td>GCCACCGCTGGAAACAAAGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>C795S-D</td>
      <td>This paper</td>
      <td>PCR mutagenesis primers</td>
      <td>CAATCGCTGTCCCAGCAGAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>C795S-C</td>
      <td>This paper</td>
      <td>PCR mutagenesis primers</td>
      <td>GCTCTGCTGGGACAGCGATTG</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>[14C]GlcNAc-labelled lipid II (mDAP)</td>
      <td>Breukink et al., 2003 Bertsche et al., 2005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lipid II (mDAP)</td>
      <td>Egan et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lipid II (Lys)</td>
      <td>Egan et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lipid II-dansyl</td>
      <td>Egan et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lipid II-Atto550</td>
      <td>Mohammadi et al., 2014 Van't Veer, 2016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lipid II-Atto647n</td>
      <td>Mohammadi et al., 2014 Van't Veer, 2016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Polar lipid extract from E. coli (EcPL)</td>
      <td>Avanti Polar Lipids</td>
      <td>100600P</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>1,2-Dioleoyl-sn-glycero-3-phosphocholine (DOPC)</td>
      <td>Avanti Polar Lipids</td>
      <td>850375P</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>1-Palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (POPG)</td>
      <td>Avanti Polar Lipids</td>
      <td>840457P</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Tetraoleoyl cardiolipin</td>
      <td>Avanti Polar Lipids</td>
      <td>710335P</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Dy647P1-maleimide probe</td>
      <td>Dyomics</td>
      <td>647P1-03</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Alexa Fluor 488 C5 Maleimide</td>
      <td>ThermoFisher Scientific</td>
      <td>A10254</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Alexa Fluor 555 C2 maleimide</td>
      <td>ThermoFisher Scientific</td>
      <td>A20346</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Triton X-100</td>
      <td>Roche</td>
      <td>10789704001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Moenomycin</td>
      <td>Sigma</td>
      <td>32404</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Ampicillin</td>
      <td>Sigma</td>
      <td>A9518</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Methyl-β-cyclodextrin</td>
      <td>Sigma-Aldrich</td>
      <td>332615</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Poly(ethylene glycol) Mn8000</td>
      <td>Sigma-Aldrich</td>
      <td>1546605</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>1,2-dioleoyl-sn-glycero-3-phosphoethanolamine-N-(lissamine rhodamine B sulfonyl) (DOPE-Rhodamine)</td>
      <td>Avanti Polar Lipids</td>
      <td>810150C</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Dioctadecylamine (DODA)-tris-Ni-NTA</td>
      <td>Beutel et al., 2014</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>cOmplete, EDTA-freeProtease Inhibitor Cocktail</td>
      <td>Roche Molecular Biochemicals</td>
      <td>5056489001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Phenylmethylsulfonylfluoride (PMSF)</td>
      <td>Sigma-Aldrich</td>
      <td>P7626</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Ni-NTA superflow resin</td>
      <td>Qiagen</td>
      <td>1018142</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Bio-Beads SM-2 resin</td>
      <td>Bio-Rad</td>
      <td>1523920</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Pierce BCA Protein Assay Kit</td>
      <td>ThermoFisher Scientific</td>
      <td>23227</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>HiTrap SP HP column, 1 mL</td>
      <td>GE biosciences</td>
      <td>17115101</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>HiTrap Desalting column, 5 mL</td>
      <td>GE biosciences</td>
      <td>17140801</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Prontosil 120–3 C18 AQ reversed-phase column</td>
      <td>BISCHOFF Chromatography</td>
      <td>1204F184P3</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>DNase</td>
      <td>ThermoFisher Scientific</td>
      <td>90083</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Cellosyl</td>
      <td>Hoechst (Germany)</td>
      <td></td>
      <td>Mutanolysin from Sigma (M9901) can also be used</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>MepM</td>
      <td>Federico Corona, following protocol in Singh et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>His6-tagged (on the C-terminus) neutral peptide</td>
      <td>BioMatik</td>
      <td></td>
      <td>CMSQAALNTRNSEEEVSSRRNNGTRHHHHHH</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td></td>
      <td>https://fiji.sc</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>MathWorks</td>
      <td>https://www.mathworks.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>frap_analysis</td>
      <td>Jönsson, 2020</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Chemicals

[14C]GlcNAc-labelled lipid II and the lysine or mDAP forms of lipid II were prepared as published (Breukink et al., 2003; Egan et al., 2015). Lipid II-Atto550 and Lipid II-Atto647n were prepared from the lysine form of lipid II, as described previously (Egan et al., 2015), and Atto550-alkyne or Atto647n-alkyne (Atto tec, Germany) in two steps: (1) conversion of lysine form of lipid II to azidolysine form and (2) labelling of azidolysine lipid II via click-chemistry. The protocol is extensively detailed elsewhere (Mohammadi et al., 2014). The advantage of using this methodology over directly attaching the probes to the amine group is the higher yield of click-chemistry reactions, allowing the use of a smaller excess of the reactive florescent probes (Van't Veer et al., 2016). All lipid II variants were kept in 2:1 chloroform:methanol at −20°C. Before enzymatic assays, the required amounts of lipid II were dried in a speed-vac and resuspended in water (for assays in detergents) or the appropriate buffer (for liposome and SLB assays). Polar lipid extract from E. coli (EcPL), 1,2-dioleoyl-sn-glycero-3-phosphocholine (DOPC), 1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (POPG), and tetraoleoyl cardiolipin (TOCL) were obtained from Avanti Polar Lipids (USA). Lipids were resuspended in chloroform:methanol (2:1) at a concentration of 20 g/L, aliquoted, and stored at −20°C. Triton X-100, ampicillin, phenylmethylsulfonyl fluoride (PMSF), protease inhibitor cocktail (PIC), and β-mercaptoethanol were from Merck. n-Dodecyl-beta-D-maltopyranoside was purchased from Anatrace (USA). Moenomycin was purchased from Hoechst, Germany. All other chemicals were from Merck.

### Cloning

#### Construction of overexpression vector pKPWV1B

The plasmid pKPWV1B was constructed for overexpression of full-length A. baumannii PBP1B (PBP1BAb: aa 1–798) with a cleavable N-terminal oligo-histidine tag (His6 tag). Therefore, the gene mrcB was amplified using the Phusion high-fidelity DNA polymerase and the oligonucleotides PBP1B.Acineto-NdeI_f and PBP1B.Acineto-BamHI_r and genomic DNA of A. baumannii 19606 (ATCC) as template. The resulting PCR fragment and the plasmid DNA of the overexpression vector pET28a(+) (Novagen) were digested with NdeI and BamHI, ligated, and transformed into chemical-competent E. coli DH5α cells with kanamycin selection. Plasmid DNA of transformants was isolated and sent for sequencing using the following oligonucleotides: Seq1_rev_PBP1B_Acineto, Seq2_fwd_PBP1B_Acineto, Seq3_fwd_PBP1B_Acineto, and Seq4_fwd_PBP1B_Acineto.

#### Construction of overexpression vector pKPWVLpoP

The sequence of the hypothetical PBP1B activator of A. baumannii 19606 (LpoPAb: NCBI reference number: WP_000913437.1) contains a TPR fold and was found by blast analysis through its homology to P. aeruginosa LpoP (30% identity). The plasmid pKPWVLpoP was purchased from GenScript. The gene was synthesized without the first 51 nucleotides (encoding the 17 amino acids of the signal peptide) and with codon optimization for overexpression in E. coli. The codon-optimized gene was subcloned in the overexpression vector pET28a(+) using the cloning sites NdeI and BamHI, enabling the overexpression of the protein with an N-terminal oligo-histidine tag.

#### MGC-64PBP1B-his C777S/C795S

This fusion protein contains PBP1B with the substitution of the N-terminal cytoplasmic tail for residues MGC and the addition of a hexahistine tag at the C-terminus. To obtain this construct, the regions coding for amino acids 64 to 844 of PBP1B were amplified from genomic DNA using oligonucleotides PBP1B-MGC-F and PBP1B-CtermH-R. The resulting product was cloned into pET28a+ vector (EMD Biosciences) after digestion with NcoI and XhoI. C777S and C795S mutations were introduced using the QuikChange Lightning mutagenesis kit (Agilent) through oligonucleotide primers C777S-D, C777S-C, C795S-D, and C795S-C. The resulting plasmid was called pMGCPBP1BCS1CS2.

### Purification and labelling of proteins

The following proteins were purified following published protocols: PBP1BEc (Bertsche et al., 2006), LpoB(sol) (Egan et al., 2014), PBP1BPa (Caveney et al., 2020), LpoPPa(sol) (Caveney et al., 2020), and MepM (Singh et al., 2012). All chromatographic steps were performed using an AKTA PrimePlus system (GE Healthcare).

#### E. coli PBP1B

The protein was expressed as a fusion with an N-terminal hexahistidine tag in E. coli BL21(DE3) pDML924 grown in 4 L of autoinduction medium (LB medium supplemented with 0.5% glycerol, 0.05% glucose, and 0.2% α-lactose) containing kanamycin at 30°C for ~16 hr. Cells were harvested by centrifugation (10,000 × g, 15 min, 4°C) and the pellet resuspended in 80 mL of buffer I (25 mM Tris-HCl, 1 M NaCl, 1 mM EGTA, 10% glycerol, pH 7.5) supplemented with 1× PIC (Sigma-Aldrich), 100 µM PMSF (Sigma-Aldrich), and DNase I. After disruption by sonication on ice, membrane fraction was pelleted by centrifugation (130,000 × g for 1 hr at 4°C) and resuspended in buffer II (25 mM Tris-HCl, 1 M NaCl, 10% glycerol, 2% Triton X-100, pH 7.5) by stirring at 4°C for 24 hr. Extracted membranes were separated from insoluble debris by centrifugation (130,000 × g for 1 hr at 4°C) and incubated for 2 hr with 4 mL of Ni2+-NTA beads (Novagen) equilibrated in buffer III (25 mM Tris-HCl, 1 M NaCl, 20 mM imidazole, 10% glycerol, pH 7.5). Beads were washed 10 times with 10 mL of buffer III, and the protein was eluted with 3 mL buffer IV (25 mM Tris-HCl, 0.5 M NaCl, 20 mM imidazole, 10% glycerol, pH 7.5). His-PBP1B-containing fractions were pooled and treated with 2 U/mL of thrombin (Novagen) for 20 hr at 4°C during dialysis against dialysis buffer I (25 mM Tris-HCl, 0.5 M NaCl, 10% glycerol, pH 7.5). Protein was then dialyzed in preparation for ion exchange chromatography, first against dialysis buffer II (20 mM sodium acetate, 0.5 M NaCl, 10% glycerol, pH 5.0), then against dialysis buffer II with 300 mM NaCl, and finally against dialysis buffer II with 100 mM NaCl. Finally, the sample was applied to a 1 mL HiTrap SP column (GE Healthcare) equilibrated in buffer A (20 mM sodium acetate, 100 mM NaCl, 10% glycerol, 0.05% reduced Triton X-100, pH 5.0). The protein was eluted with a gradient from 0% to 100% buffer B (as A, with 2 M NaCl) over 14 mL PBP1B-containing fractions that were pooled and dialyzed against storage buffer (20 mM sodium acetate, 500 mM NaCl, 10% glycerol, pH 5.0) and stored at −80°C.

#### A. baumannii 19606 PBP1B

The protein was expressed in E. coli BL21 (DE3) freshly transformed with plasmid pKPWV1B using the same protocol as PBP1BEc. Cells were harvested by centrifugation (6,200 × g for 15 min at 4°C) and resuspended in 120 mL of PBP1BAb buffer I (20 mM NaOH/H3PO4, 1 M NaCl, 1 mM EGTA, pH 6.0) supplemented with DNase I, PIC (1:1000 dilution), and 100 µM PMSF. After disruption by sonication on ice, the membrane fraction was pelleted by centrifugation (130,000 × g for 1 hr at 4°C) and resuspended in PBP1BAb extraction buffer (20 mM NaOH/H3PO4, 1 M NaCl, 10% glycerol, 2% Triton X-100, pH 6.0) supplemented with PIC and PMSF by stirring at 4°C for 16 hr. Extracted membranes were separated from insoluble debris by centrifugation (130,000 × g for 1 hr at 4°C) and incubated with 4 mL of Ni2+-NTA beads equilibrated in PBP1BAb extraction buffer containing 15 mM imidazole. Beads were washed 10 times with 10 mL of PBP1BAb wash buffer (20 mM NaOH/H3PO4, 10% glycerol, 0.2% Triton X-100, 1 M NaCl, 15 mM imidazole, pH 6.0), and the protein was eluted with 3 mL buffer IV PBP1BAb elution buffer (20 mM NaOH/H3PO4, 10% glycerol, 0.2% Triton X-100, 1 M NaCl, 400 mM Imidazole, pH 6.0).

PBP1BAb-containing fractions were pooled and dialyzed in preparation for ion exchange chromatography, first against PBP1BAb dialysis buffer I (20 mM sodium acetate, 1 M NaCl, 10% glycerol, pH 5.0), then against PBP1BAb dialysis buffer II (20 mM sodium acetate, 300 mM NaCl, 10% glycerol, pH 5.0), and finally against PBP1BAb dialysis buffer III (10 mM sodium acetate, 100 mM NaCl, 10% glycerol, pH 5.0). The sample was centrifuged for 1 hr at 130,000 × g and 4°C, and the supernatant was applied to a 5 mL HiTrap SP HP column equilibrated in PBP1BAb buffer A (20 mM sodium acetate, 100 mM NaCl, 10% glycerol, 0.2% Triton X-100, pH 5.0). The protein was eluted from 0% to 100% PBP1BAb buffer B (20 mM sodium acetate, 2 M NaCl, 10% glycerol, 0.2% Triton X-100, pH 5.0) over 70 mL. PBP1BAb-containing fractions were pooled and dialyzed against PBP1BAb storage buffer (10 mM sodium acetate, 500 mM NaCl, 0.2% Triton X-100, 20% glycerol, pH 5.0) and stored at −80°C.

#### P. aeruginosa PBP1B

The protein was expressed on E. coli BL21(DE3) freshly transformed with plasmid pAJFE52, which encodes PBP1BPa as a fusion with an N-terminal hexahistidine tag in E. coli BL21(DE3). Cells were grown in 4 L of LB at 30°C, and expression was induced for 3 hr with 1 mM isopropyl β-D-1-galactopyranoside (IPTG) when the culture reached an OD578 of 0.6. PBP1BPa was extracted and purified using the same protocol as for E. coli PBP1B, with the exception that only 2 mL of Ni2+ beads were used.

#### MGC-64PBP1B-his C777S/C795S

This protein was expressed in E. coli BL21(DE3) freshly transformed with plasmid pMGCPBP1BCS1CS2 and subsequently purified using the same protocol as for the WT protein, except for the addition of 1 mM tris(2-carboxyethyl)phosphine (TCEP) to all purification buffers. The protein was labelled with Dy647-maleimide probe (Dyomics, Germany) following the manufacturer's instructions. Briefly, 10.2 µM protein was incubated with 100 µM probe and 0.5 mM TCEP for ~20 hr at 4°C, and free probe was removed by desalting using a 5 mL HiTrap desalting column (GE Healthcare).

#### LpoB(sol)

The protein was expressed on E. coli BL21(DE3) transformed with pET28His-LpoB(sol). Cells were grown in 1.5 L of LB plus kanamycin at 30°C to an OD578 of 0.4–0.6, and expression was induced with 1 mM of IPTG for 3 hr at 30°C. Cells were pelleted and resuspended in buffer I (25 mM Tris-HCl, 10 mM MgCl2, 500 mM NaCl, 20 mM imidazole, 10% glycerol, pH 7.5) plus DNase, PIC, and PMSF. Cells were disrupted by sonication on ice and centrifuged (130,000 × g, 1 hr, 4°C) to remove debris. The supernatant was applied to a 5 mL HisTrap HP column (GE Healthcare) equilibrated in buffer I. After washing with buffer I, the protein was eluted with a stepwise gradient with buffer II (25 mM Tris-HCl, 10 mM MgCl2, 500 mM NaCl, 400 mM imidazole, 10% glycerol, pH 7.5). Fractions containing the protein were pooled and the His-tag was removed by addition of 2 U/mL of thrombin while dialyzing against buffer IEX-A (20 mM Tris-HCl, 1000 mM NaCl, 10% glycerol, pH 8.3). Digested protein was applied to a 5 mL HiTrap Q HP column (GE Healthcare) at 0.5 mL/min. LpoB(sol) was collected in the flow through, concentrated, and applied to size exclusion on a Superdex200 HiLoad 16/600 column (GE Healthcare) at 1 mL/min in a buffer containing 25 mM HEPES-NaOH, 1 M NaCl, 10% glycerol at pH 7.5. Finally, the protein was dialyzed against storage buffer (25 mM HEPES-NaOH, 200 mM NaCl, 10% glycerol at pH 7.5) and stored at −80°C.

#### A. baumannii 19606 LpoP(sol)

The protein was expressed on E. coli BL21(DE3) transformed with plasmid pKPWVLpoP. Cells were grown overnight at 30°C in 4 L of autoinduction medium. Cells were pelleted by centrifugation (6200 × g for 15 min at 4°C) and resuspended in 80 mL of buffer I (25 mM Tris/HCl, 10 mM MgCl2, 1 M NaCl, 20 mM imidazole, pH 7.5) supplemented with DNase I, PIC (1:1000 dilution), and 100 µM PMSF. Cells were disrupted by sonication on ice and centrifuged (130,000 × g for 1 hr at and 4°C) to removed debris. The supernatant was incubated for 1 hr with 6 mL Ni-NTA beads preequilibrated in buffer I at 4°C with gentle stirring. The resin was split in two columns, each washed 10 times with 5 mL wash buffer (25 mM Tris/HCl, 10 mM MgCl2, 1 M NaCl, 20 mM imidazole, pH 7.5), and the protein was eluted 7 times with 2 mL of elution buffer (25 mM Tris/HCl, 10 mM MgCl2, 1 M NaCl, 400 mM imidazole, pH 7.5). The best fractions according to SDS-PAGE analysis were pooled and dialyzed stepwise against increasing percentage of dialysis buffer I (25 mM HEPES/NaOH, 10 mM MgCl2, 200 mM NaCl, 10% glycerol, pH 7.5). Thrombin (nine units) was added to the protein to cleave the N-terminal His6 tag overnight at 4°C. The successful cleavage of the N-terminal His6 tag was confirmed by SDS-PAGE. The protein was diluted 2× with 25 mM HEPES/NaOH, 10 mM MgCl2, 10% glycerol, pH 7.5 to reduce the amount of NaCl down to 100 mM. The protein was applied to a 5 mL HiTrap SP HP column and washed with buffer A (25 mM HEPES/NaOH, 10 mM MgCl2, 100 mM NaCl, 10% glycerol, pH 7.5). The protein was then eluted with a gradient of 100 mM to 1 M NaCl over 50 mL at 1 mL/min using increasing percentage of buffer B (25 mM HEPES/NaOH, 10 mM MgCl2, 1 M NaCl, 10% glycerol, pH 7.5). Fractions were collected and analysed by SDS-PAGE. The best fractions were pooled, dialyzed against 25 mM HEPES/NaOH, 200 mM NaCl, 10% glycerol, 10 mM MgCl2, pH 7.5, and the protein was stored at −80°C.

#### P. aeruginosa LpoP(sol)

The protein was expressed on E. coli BL21(DE3) freshly transformed with plasmid pAJFE57, encoding His6-LpoPPa(sol). Cells were grown on 1.5 L LB at 30°C to an OD578 of 0.5, and expression was induced for 3 hr by addition of 1 mM IPTG. After harvesting, cells were resuspended in 80 mL of 25 mM Tris-HCl, 500 mM NaCl, 20 mM imidazole, 10% glycerol at pH 7.5. After addition of PIC and 100 µM PMSF, cells were disrupted by sonication on ice. Debris was removed by centrifugation (130,000 × g, 1 hr, 4°C) and the supernatant was applied to a 5 mL HisTrap column equilibrated in resuspension buffer. After washing with 25 mM Tris-HCl, 1 M NaCl, 40 mM imidazole, 10% glycerol at pH 7.5, the protein was eluted with 25 mM Tris-HCl, 500 mM NaCl, 400 mM imidazole, 10% glycerol at pH 7.5. Fractions containing His-LpoPPa(sol) were pooled and the His-tag was removed by addition of 4 U/mL of thrombin while dialyzing against 20 mM Tris-HCl, 200 mM NaCl, 10% glycerol at pH 7.5 for 20 hr at 4°C. The sample was concentrated and further purified by size exclusion column chromatography at 0.8 mL/min using a HiLoad 16/600 Superdex 200 column equilibrated in 20 mM HEPES-NaOH, 200 mM NaCl, 10% glycerol at pH 7.5. LpoPPa-containing fractions that were pooled, concentrated, aliquoted, and stored at −80°C.

### PG synthesis assays in the presence of detergents

#### In vitro PG synthesis assay using radiolabelled lipid II in detergents

To assay the in vitro PG synthesis activity of PBP1BEc with radiolabelled lipid II substrate in the presence of detergents, we used a previously published assay (Banzhaf et al., 2012; Biboy et al., 2013). Final reactions included 10 mM HEPES/NaOH pH 7.5, 150 mM NaCl, 10 mM MgCl2, and 0.05% Triton X-100. The concentration of PBP1BEc was 0.5 µM. Reactions were carried out for 1 hr at 37°C. Reactions were stopped by boiling for 5 min. Digestion with cellosyl, reduction with sodium borohydride, and analysis by HPLC were performed as described (Biboy et al., 2013).

#### FRET-based in vitro PG synthesis assay in detergents

For assays in detergents, samples contained 50 mM HEPES/NaOH pH 7.5, 150 mM NaCl, 10 mM MgCl2, and 0.05% Triton X-100 in a final volume of 50 µL. PBP1BEc, PBP1BAb, or PBP1BPa were added at a concentration of 0.5 µM. When indicated, activators LpoB(sol), LpoPAb(sol), or LpoPPa(sol) were added at a concentration of 2 µM. Reactions were started by the addition of an equimolar mix of lipid II, lipid II-Atto550, and lipid II-Atto647n, each at 5 µM and monitored by measuring fluorescence using a Clariostar plate reader (BMG Labtech, Germany) with excitation at 540 nm and emission measurements at 590 and 680 nm. In controls containing unlabelled lipid II plus only one of the labelled lipid II versions (lipid II-Atto550 or lipid II-Atto647n) (Figure 1—figure supplement 4), the labelled lipid II was added at 5 µM along 10 µM of unlabelled lipid II. Reactions were incubated at the indicated temperature for 60 or 90 min. After the reaction, emission spectra from 550 to 740 nm were taken in the same plate reader with excitation at 522 nm. When indicated, ampicillin was added at 1 mM and moenomycin was added at 50 µM. After plate reader measurements, reactions were stopped by boiling for 5 min, vacuum-dried using a speed-vac desiccator, and analysed by Tris-Tricine SDS-PAGE as described previously (Van't Veer et al., 2016).

FRET reactions in the presence of radiolabelled lipid II described in Figure 1E, F were performed using the same buffer and substrate and enzyme concentrations as for the plate reader assay but in a final volume of 350 µL. Samples were incubated at 25°C with shaking using an Eppendorf Thermomixer. Also, 50 µL aliquots were taken out at the indicated times and reactions were stopped by addition of 100 µM moenomycin. Samples were then transferred to a 96-well plate to measure FRET as described above. Finally, samples were transferred back to Eppendorf tubes, digested with cellosyl, and reduced with sodium borohydride as described previously (Biboy et al., 2013).

#### Quantification of lipid II consumption after the FRET assay in detergents

For the assay in Figure 2—figure supplement 1, reactions were performed in the same conditions as described for the FRET assay in detergents, but four different molar proportions of fluorescent lipid II over the total amount of lipid II were used: 80%, 66.7%, 50%, and 20%. Radiolabelled lipid II was included to allow for quantification of non-fluorescent lipid II consumption at the end of reactions. The total concentration of lipid II was kept at 15 µM, and the molar ratio of lipid II-Atto550 to lipid II-Atto647n was 1:1. At each proportion of fluorescent lipid II, PBP1BEc reactions were measured in triplicate with and without LpoB (2 µM), and two control reactions with substrate but no enzyme were prepared to determine the amount of each type of lipid II consumed. Reactions were monitored using a plate reader for 1 hr at 25°C as described above and then stopped by boiling for 10 min. Next, 5 µL aliquots were taken from each reaction, dried in a speed-vac, and analysed by SDS-PAGE with fluorescent scanning as described previously (Van't Veer et al., 2016). Fluorescent lipid II consumption was calculated by comparing the intensity of the lipid II bands on reaction lanes and control lanes. To quantify the consumption of radiolabelled lipid II, the unused lipid II was extracted from the remaining aliquot of the reactions with butanol:pyridine (2:1, vol:vol) at pH 4.2, and the radioactivity was quantified by scintillation counting as described previously (Egan et al., 2015).

#### Analysis of FRET reaction curves

Reaction curves were obtained by calculating the ratio between fluorescence intensity at 680 and 590 nm monitored at every well. This maximizes the amount of information captured from the change in the spectrum due to FRET and normalizes the intensity removing any non-specific jumps in the signal due to bubbles in the reaction well or lamp instability. The slope of reaction curves obtained by the FRET assay was calculated when the ratio started to rise, avoiding the lag phase when present. Only the linear phase of each curve was used. For example, for PBP1BEc in detergents, slopes were calculated from 10 to 15 min in the absence of LpoB and within the first minute in the presence of activator. To compare our results with prior reports, we report the fold-change in the slope in the presence of the corresponding Lpo activator, that is, the ratio between the slope in a condition with activator and the slope at the same condition without activator.

#### Determination of FRET efficiency

For the determination of FRET efficiency, reactions were prepared in the same conditions as for the plate reader assays but they were incubated at 37°C for 1 hr in Eppendorf tubes instead and boiled for 5 min afterwards. For every antibiotic condition, four samples were prepared: sample 1 (DA reaction) contained 5 µM each of unlabelled lipid II, lipid II-Atto550, and lipid II-Atto647n; sample 2 (D reaction) contained 10 µM unlabelled lipid II plus 5 µM lipid II-Atto550; sample 3 (A reaction) contained 10 µM unlabelled lipid II plus 5 µM lipid II-Atto647n; and sample 4 (BG reaction) contained 15 µM unlabelled lipid II. For digestion with hydrolases, 50 µL of the PG synthesis reactions were prepared as described above and split into three aliquots. Either 5 µM MepM, 0.05 mg/mL cellosyl, or buffer was added to a final volume of 20 µL, and samples were incubated overnight at 37°C and boiled for 5 min to stop reactions.

Samples were measured in Cary Varian fluorimeter using a 1.5 mm light-path quartz cuvette. For samples 1, 3, and 4, two spectra were measured, one with excitation at 552 nm ($\lambda_{ex}^{D}$) and emission collected from 560 to 750 nm (ds spectrum) and the other with excitation at 650 nm ($\lambda_{ex}^{A}$) and emission collected from 660 to 750 nm (as spectrum). For sample 2, only the ds spectrum was measured. All spectra were taken with 5 nm slits for emission and excitation at the same detector voltage settings (850 V).

FRET efficiency (E) was calculated according to the (ratio)A method described in Vámosi and Clegg, 1998. Briefly, (ratio)A is a normalized measure of the enhancement of the acceptor emission due to FRET,

$$
ratio_{A}=\frac{F_{A}\lambda_{ex}^{D},\lambda_{em}}{F_{A}\lambda_{ex}^{A},\lambda_{em}}=\frac{[ϵ_{D}\lambda_{ex}^{D}E+ϵ_{A}\lambda_{ex}^{D}]Φ^{A}(\lambda_{em})}{ϵ_{A}\lambda_{ex}^{A}Φ^{A}(\lambda_{em})}=\frac{ϵ_{D}\lambda_{ex}^{D}E+ϵ_{A}\lambda_{ex}^{D}}{ϵ_{A}\lambda_{ex}^{A}}
$$

where $Φ^{A}(\lambda_{em})$ is a shape function of the acceptor emission spectrum, $F_{A}(\lambda_{ex}^{D},\lambda_{em})$ is the emission of the acceptor (only the acceptor) when excited at $\lambda_{ex}^{D}$, and $F_{A}(\lambda_{ex}^{A},\lambda_{em})$ is the emission of the acceptor when excited at $\lambda_{ex}^{D}$, both in the sample containing both donor and acceptor. FRET efficiency is normalized by the extinction coefficients of the donor at $\lambda_{ex}^{D}$ ($ϵ_{D}\lambda_{ex}^{D}$ = 120,000 M−1 cm−1) and of the acceptor at both $\lambda_{ex}^{D}$ and $\lambda_{ex}^{A}$ ($ϵ_{A}\lambda_{ex}^{D}$ = 6000 M−1 cm−1, and $ϵ_{A}\lambda_{ex}^{A}$ = 150,000 M−1 cm−1, respectively).

In order to calculate (ratio)A from the ds spectrum, three spectral contributions ($\delta^{ds}$, $\alpha^{ds}$, and $\beta^{ds}$) were fitted in the ds spectra, $F^{ds}\lambda$, and two spectral contributions ($\alpha^{as}$ and $\beta^{as}$) were fitted in the as spectra, $F^{as}\lambda$:

$$
F^{ds}\lambda=\delta^{ds}F_{Dref}^{ds}\lambda+\alpha^{ds}F_{Aref}^{ds}\lambda+\beta^{ds}F_{Bref}^{ds}(\lambda)
$$



$$
F^{as}\lambda=\alpha^{as}F_{Aref}^{as}\lambda+\beta^{as}F_{Bref}^{as}(\lambda)
$$

where $F_{Dref}^{ds}\lambda$ is the background-free spectra from the donor-only reference sample exited at $\lambda_{ex}^{D}$; $F_{Aref}^{ds}\lambda$ is the background-free spectra from the acceptor-only reference sample exited at $\lambda_{ex}^{D}$; $F_{Aref}^{as}\lambda$ is the background-free spectra from the acceptor-only reference sample exited at $\lambda_{ex}^{A}$; and $F_{Bref}^{ds}\lambda$ and $F_{Bref}^{as}\lambda$ are the background spectra obtained at $\lambda_{ex}^{D}$ and $\lambda_{ex}^{A}$, respectively. (ratio)A was then calculated from Equation 4, integrating at wavelengths common in both $F_{Aref}^{ds}\lambda$ and $F_{Aref}^{ds}\lambda$ (from 660 to 750 nm).

$$
(ratio)_{A}=\frac{\alpha^{ds}F_{Aref}^{ds}\lambda}{\alpha^{as}F_{Aref}^{as}\lambda}
$$

All calculations were implemented in Excel.

#### Continuous GTase assay using dansylated lipid II

Continuous fluorescence GTase assays using dansylated lipid II and A. baumannii PBP1B were performed as described previously (Schwartz et al., 2001; Offant et al., 2010; Egan and Vollmer, 2016). Samples contained 50 mM HEPES/NaOH pH 7.5, 105 mM NaCl, 25 mM MgCl2, 0.039% Triton X-100, and 0.14 µg/µL cellosyl muramidase in a final volume of 60 µL. PBP1BAb was added at a concentration of 0.5 µM. When indicated, LpoPAb(sol) was added at a concentration of 0.5 µM. Reactions were started by addition of dansylated lipid II to a final concentration of 10 µM and monitored by following the decrease in fluorescence over 60 min at 37°C using a FLUOstar OPTIMA plate reader (BMG Labtech, Germany) with excitation at 330 nm and emission at 520 nm. The fold-increase in GTase was calculated against the mean rate obtained with PBP1BAb alone at these reaction conditions, at the fastest rate.

#### Time-course GTase assay by SDS-PAGE followed by fluorescence detection

PBP1BAb at a concentration of 0.5 µM was incubated with 5 µM lipid II-Atto550 and 25 µM unlabelled lipid II in the presence or absence of 1.5 µM LpoPAb(sol). Reactions contained 20 mM HEPES, 150 mM NaCl, 10 mM MgCl2, 0.06% TX-100, and 1 mM ampicillin to block transpeptidation. Aliquots were taken after 0, 2, 5, 10, 30, and 60 min incubation at 37°C, boiled for 10 min to stop reactions, and analysed by Tris-Tricine SDS-PAGE followed by fluorescence detection as described previously (Van't Veer et al., 2016).

#### Fluorescence scanning of SDS-PAGE gels with PG synthesis products

SDS-PAGE gels were scanned using either a Typhoon FLA9500 (GE) or a Typhoon 9400 (Amersham) fluorescence scanner. Atto550 fluorescence was scanned using a 532 nm laser and either a 590 nm, 30 nm-bandwidth bandpass filter (9400) or a 575 nm long-pass filter (FLA9500). Atto647n fluorescence was scanned using a 635 nm laser and either a 670 nm, 30 nm-bandwidth bandpass filter (9400) or a 665 nm long-pass filter (FLA9500). Voltage of the photodetector was carefully adjusted to avoid saturated pixels in the resulting images. For quantification, ImageJ was used utilizing the original files produced by the scanner. For visualization, images were exported using ImageQuant software (GE Healthcare). During this conversion, ImageQuant automatically adjusts contrast so that tenuous bands are easier to visualize. Unfortunately, this adjustment makes the most intense bands (unused lipid II, wells) appear saturated, which can be misleading when interpreting the images. Thus, we provide the original gel files produced by the scanner as source data files.

### PG synthesis in liposomes

#### Reconstitution of class A PBPs in liposomes

Proteoliposomes containing class A PBPs were prepared as described previously with some modifications (Egan et al., 2015; Rigaud and Lévy, 2003; Hernández-Rocamora et al., 2018). The appropriate lipid or mixture of lipids was dried in a glass test tube under stream of N2 to form a lipid film followed by desiccation under vacuum from 2 hr. When labelled lipid II was co-reconstituted with the indicated class A PBP, they were added at 1:200 mol:mol phospholipid to each lipid II-Atto550 and lipid II-Atto647n. Resuspension into multilamellar vesicles (MLVs) was achieved by addition of 20 mM Tris/HCl, pH 7.5 with or without 150 mM NaCl as indicated in each experiment and several cycles of vigorous mixing and short incubations in hot tap water. The final lipid concentration was 5 g/L. To form large unilamellar vesicles (LUVs), MLVs were subjected to 10 freeze–thaw cycles and then extruded 10 times through a 0.2 µm filter. LUVs were destabilized by the addition of Triton X-100 to an effective detergent:lipid ratio of 1.40 and mixed with proteins in different protein-to-lipid molar ratios (1:3000 for PBP1BEc and PBP1BPa, and 1:2000 for PBP1BAb). After incubation at 4°C for 1 hr, prewashed adsorbent beads (Biobeads SM2, BioRad, USA; 100 mg per 3 µmol of Triton X-100) were added to the sample to remove detergents. Biobeads were exchanged after 2 and 16 hr, followed by incubation with fresh Biobeads for a further 2 hr. After removal of Biobeads by short centrifugation at 4000 × g, liposomes were pelleted at 250,000 × g for 30 min at 4°C. The pellet containing proteoliposomes was resuspended using the appropriate buffer. The resuspension was done in a 43% smaller volume than the volume added of lipid II, so that the final concentration of lipids was 11.6 g/L. Samples were then centrifuged for 5 min at 17,000 × g and 4°C to remove any possible aggregates. The supernatant was then used in the appropriate assays. Liposomes were analysed by SDS-PAGE and, only for liposomes without labelled lipid II, also by bicinchoninic acid assay (Pierce BCA Assay Kit, ThermoFisher Scientific, USA) to determine protein concentration. The concentration of protein for liposomes with labelled lipid II was calculated by densitometry of the samples in SDS-PAGE gels after reactions were carried out.

#### PBP1BEc orientation assay

To assess the orientation of liposome-reconstituted PBP1BEc, MGC-64PBP1B-his C777S C795S mutant containing a single cysteine in the N-terminal region was reconstituted in liposomes with EcPL as described above. The accessibility of the cysteine was determined using sulfhydryl-reactive fluorescent probe Alexa Fluor555-maleimide. Reactions containing 0.5 µM protein, 10 µM Alexa Fluor555-maleimide, and 0.2 mM TCEP were incubated for 16 hr at 4°C in the presence or absence 0.5% Triton X-100. Reactions were stopped by addition of 5 mM DTT and boiling for 5 min. Samples were loaded in a 10% acrylamide gel and, after electrophoresis, gels were first scanned using an Amersham Typhoon Trio with excitation at 533 nm and a 40 nm-wide band-pass emission filter at 580 nm. The gel was then stained by Coomassie.

#### In vitro PG synthesis assay using radiolabelled lipid II in liposomes

The same methodology as in detergents was used to assay the in vitro PG synthesis activity of PBP1BEc in liposomes, with minor modifications. To start reactions, 1.5 nmol [14C]-labelled lipid II were dried in a 0.5 mL glass tube using a vacuum concentrator, resuspended in 5 µL of the appropriate liposome buffer, and mixed with liposomes, buffer, and MgCl2 to a total volume of 50 µL. Final reactions contained 0.5 µM PBP1BEc, 30 µM lipid II, and 1 mM MgCl2 in 20 mM Tris/HCl pH 7.5 with or without 150 mM NaCl as indicated for each experiment. Samples were incubated for 90 min at 37°C with shaking at 800 rpm. Reactions were stopped by boiling for 5 min. Digestion with cellosyl, reduction with sodium borohydride, and analysis by HPLC were performed as described (Biboy et al., 2013).

#### FRET-based in vitro PG synthesis assay in liposomes

For assays with liposomes, samples contained 20 mM Tris pH 7.5, 1 mM MgCl2 in a final volume of 50 µL. In this case, the same volume for each liposome preparation was added to the reactions, 10 µL, so that the total amount of labelled lipid II was present in every reaction. In these conditions, concentration of lipid II-Atto550 and lipid II-Atto647n would be 14.5 µM each, assuming no loss of lipids during sample preparation. The final concentrations of enzymes for the reactions shown in Figure 3, determined by densitometry of SDS-PAGE gels, were ~0.59 µM for PBP1BEc, ~0.81 µM for PBP1BAb, and ~0.53 µM for PBP1BPa. When indicated, activators LpoB(sol), LpoPAb(sol), or LpoPPa(sol) were added at a concentration of 2 µM. Reactions were started by the addition of lipid II at 12 µM and monitored by measuring fluorescence over a period of 60 min (or 90 min for PBP1BPa liposomes) at 37°C using a Clariostar plate reader (BMG Labtech, Germany), with emission measurements at 590 and 680 nm after excitation at 522 nm. When indicated, ampicillin was added at 1 mM and moenomycin was added at 50 µM. Activity assays were performed immediately after preparation of liposomes was finished as we noticed that some proteins could slowly start polymerization using the labelled lipid II. After reactions, samples were analysed by Tris-Tricine SDS-PAGE as indicated for detergents.

#### Analysis of FRET reaction curves

Slopes were calculated as indicated in the FRET assay in the presence of detergent. As it is not possible to precisely adjust the final amount of enzyme in different liposome preparations, there could be differences in activities measured due to different enzyme amounts. Therefore, we calculated the ratio of the slope with activator over the slope without activator for every liposome preparation and then averaged the values (instead of averaging the different measurements from every sample). At least two independent liposome preparations were prepared for every class A PBP.

### Assays in SLBs

#### Preparation of small unilamellar vesicles (SUVs) and proteoliposomes for SLB formation

Liposomes of EcPL lipids and proteoliposomes with reconstituted PBP1BEc were prepared as described previously by addition of β-cyclodextrin to the solution of lipids and Triton X-100 detergent (Degrip et al., 1998; Roder et al., 2011). Briefly, a thin lipid film of EcPL extract was prepared by N2-assisted chloroform evaporation. After 2 hr of drying under vacuum, the lipid film was rehydrated to 5 mM (total phosphorus concentration) in 150 mM NaCl, 10 mM Tris-HCl, pH 7.4 supplemented with 20 mM Triton X-100. The suspension of lipids/detergent was extensively vortex, freeze/thawed for five cycles, and sonicated using a water-bath sonicator for 10 min (on ice, to avoid lipids overheating upon sonication). To prepare proteoliposomes, full-length PBP1B produced as described above and containing 0.05% Triton X-100 was mixed with a lipid–detergent suspension at the indicated ratio, usually 1:25,000 (protein:lipids), and incubated for 10 min at room temperature (RT). Incorporation of PBP1BEc into liposomes was achieved by addition of 2× excess of β-cyclodextrin solution for 5 min (at RT) with subsequent twentyfold dilution in 20 mM HEPES, pH 7.4. The rapid depletion of detergent by addition of β-cyclodextrin leads to the formation of very small unilamellar vesicles with an average diameter of 18–25 nm and narrow size distribution (Roder et al., 2011).

To prepare liposomes with fluorescently labelled lipid II, the extract of EcPL was supplemented with 2 mol% solution of either lipid II-Atto550 or lipid II-Atto647n. The lipid film was treated similarly as the film for the preparation of proteoliposomes. Liposomes were also prepared by cyclodextrin-assisted extraction of Triton X-100.

#### Formation of polymer-SLBs and reconstitution of PBP1BEc into a supported lipid membrane

To form polymer-supported lipid membranes, the coverslips were functionalized beforehand with a dense PEG film, where the ends of the polymer brush were covalently modified with palmitic acid, which served as a linker to capture liposomes as described elsewhere (Roder et al., 2011). To perform a FRET assay on supported lipid membrane, empty EcPL liposomes (1), liposomes with 2 mol% of either lipid II-Atto550 (2) or lipid II-Atto647n (3), and PBP1BEc proteoliposomes (4) were mixed at equimolar ratio and diluted by twentyfold with the 10 mM Tris pH 7.5 buffer directly in the reaction chamber. After 30 min of incubation at 37°C, the reaction chamber was washed five times by solution exchange. Proteoliposomes adsorbed on the surface were fused by the addition of 10% (w/v) PEG 8 kDa solution (in water). The fusion reaction was carried out for 15 min at 37°C, afterwards PEG solution was rigorously washed out. Fluidity and homogeneity of the lipid membrane were checked either with PE-Rhodamine dye (Avanti) or by addition of a His6-tagged (on the C-terminus) neutral peptide (CMSQAALNTRNSEEEVSSRRNNGTRHHHHHH) labelled with a single Alexa 488 fluorophore on its only Cys residue at the N-terminus to the EcPL membrane containing 0.1 mol% dioctadecylamine (DODA)-tris-Ni-NTA (Beutel et al., 2014).

#### FRET-based in vitro PG synthesis assay in SLBs using TIRF microscopy

PG synthesis reactions were carried out at 10 mM Tris pH 7.5 supplemented with 1 mM MgCl2, with or without 1 mM ampicillin and in the presence of 4 µM LpoB(sol). The reaction was started by addition of 4 µM of unlabelled lipid II. TIRF microscopy, using a set up described elsewhere (Baranova et al., 2020), was used to monitor an increase in FRET efficiency and spatial reorganization of FRET signal over the time course of PG synthesis. To detect real-time FRET on supported lipid membranes, we used the so-called ‘acceptor photobleaching approach’ where a region of interest of about 10 × 10 µm was photobleached in the acceptor channel (lipid II-Atto647n) and the increase in fluorescence intensity of the donor (lipid II-Atto550) was recorded within a delay of 1 s. We found that in our experiments photobleaching of the acceptor dye was the only process that contributed to the recorded increase in the donor fluorescence signal. Accordingly, the relative increase in donor fluorescence can be used as a direct readout for the FRET efficiency and could therefore be calculated as described (Loose et al., 2011; Verveer et al., 2006). Briefly, donor intensity levels were calculated before (ID) and after photobleaching (ID,pb) using intensity measurements in ImageJ. FRET efficiency was calculated using Equation 5:

$$
E=(I^{D,pb}−I^{D})/I^{D,pb}
$$

For time-course measurements (Figure 4D), the acceptor signal (lipid II-Atto647n) was photobleached every minute after the initiation of the reaction (the data point at time 0 corresponds to the addition of unlabelled lipid II). For each time point, a new region of interest in the same chamber was photobleached, and the change in the donor intensity was recorded to calculate FRET efficiency using Equation 1.

To have a control on the lipid membrane integrity during PG synthesis, the phospholipid DODA-tris-Ni-NTA (Beutel et al., 2014) was included during reconstitution at a 0.1 mol% ratio. DODA-tris-Ni-NTA was then visualized using a His6-containing peptide (CMSQAALNTRNSEEEVSSRRNNGTRHHHHHH) labelled with Alexa488 on its single Cys residue, which we added in the same experiment in which we performed FRET analysis. To compare the fluidity and immobile fraction of lipid II-Atto647n before and after 1 hr of the synthesis reaction with the fluidity of phospholipids in the lipid membrane, the same region of interest was photobleached with a laser first at 640 nm and afterwards at 480 nm.

#### In vitro PG synthesis assay using radiolabelled lipid II on SLBs

To assay PG synthesis on SLBs using radioactively labelled lipid II, we first reconstituted PBP1BEc on SLBs containing EcPL extract and a 1:105 PBP1BEc to lipid molar ratio, as described above. Due to the low density of the enzyme, several 1.1 cm2 chambers were assayed for every condition in order to accumulate a measurable signal. In every chamber, reactions were started by addition of 10 µM [14C]-labelled lipid II and 4 µM LpoB(sol) in a total volume of 100 µL per chamber. The synthesis reaction was carried out in 10 mM Tris pH 7.5, 1 mM MgCl2. The chambers were incubated overnight (~16 hr) at 37°C and covered with parafilm. Reactions were stopped by addition of 100 µM moenomycin. To digest the produced PG, cellosyl was added at 0.05 g/L in the presence of 0.3% Triton X-100. After 1 hr incubation at 37°C, samples from six chambers were pooled in an Eppendorf tube, concentrated using a speed-vac evaporator, reduced using sodium borohydride, and analysed by HPLC as described above. For the experiment to determine lipid II incorporation and the localization of the produced PG, before addition of moenomycin, chambers were washed by removal of 50 µL of buffer and addition of 50 µL of fresh buffer while mixing. This was repeated five times. The removed volume from each wash was pooled and treated the same as the samples left in the chamber.

#### Single-molecule tracking and analysis

To perform single-molecule tracking, MGC-64PBP1B-his C77S C795S was labelled with the photostable far-red dye Dy647N as described above and then reconstituted into a polymer-supported lipid membrane as described elsewhere (Roder et al., 2011; Roder et al., 2014). Single-molecule tracking experiments were performed at a low protein-to-lipid molar ratio (1:10−6). At this ratio, supported lipid membrane was largely homogeneous with the lowest immobile fraction from all the ratios tested (Figure 3—figure supplement 1). The single-molecule motion of PBP1B was measured prior to and after the addition of 1.5 µM lipid II after 15 min ex situ incubation in the presence of 10 mM HEPES pH 7.4, 150 mM NaCl, 1 mM MgCl2 buffer and in the absence of LpoB(sol). The localization and tracking of PBP1B particles were performed by the SLIMfast software (Roder et al., 2014). To ensure that non-specifically stuck PBP1B particles did not contribute to the measured diffusion coefficient, the immobile particles were excluded using the DBSCAN spatial clustering algorithm (Sander et al., 1998) with the following clustering parameters: a search area of 100 nm and a minimal time window of 30 frames at 65 ms/frame acquisition time. The displacement distribution for active PBP1B (in the presence of lipid II) was compared to the displacement distribution of PBP1B before lipid II addition by fitting the two-component Rayleigh distribution and comparing the weighted contribution of each population. The mean-squared displacement (MSD) was fitted to each individual trajectory longer than 650 ms (10 frames). Each MSD curve was fitted with a linear fit considering max 30% of the lag time for each trajectory.

#### FRAP analysis

To control membrane fluidity upon the reconstitution of the transmembrane PBP1B (Figure 3—figure supplement 1, Figure 4—figure supplement 1) and fluidity of lipid II Atto-647n during PG synthesis (Figure 4E, F), we used a Matlab-based GUI frap_analysis (Jönsson, 2020) in details described elsewhere (Jönsson et al., 2008). This code allows to quantify the contribution of the immobile fraction to the estimated diffusion coefficient and is particularly suitable for the analysis of 2D diffusion with the photobleaching contribution during the recovery.
