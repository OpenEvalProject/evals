# Hair follicle dermal condensation forms via Fgf20 primed cell cycle exit, cell motility, and aggregation

## Authors

- Leah C Biggs<sup>1</sup> ([ORCID: 0000-0002-4990-8664](https://orcid.org/0000-0002-4990-8664))
- Otto JM Mäkelä<sup>1</sup> ([ORCID: 0000-0001-6852-9814](https://orcid.org/0000-0001-6852-9814))
- Satu-Marja Myllymäki<sup>1</sup>
- Rishi Das Roy<sup>1</sup> ([ORCID: 0000-0002-3276-7279](https://orcid.org/0000-0002-3276-7279))
- Katja Närhi<sup>1</sup>
- Johanna Pispa<sup>1</sup>
- Tuija Mustonen<sup>1</sup> ([ORCID: 0000-0002-2429-5064](https://orcid.org/0000-0002-2429-5064))
- Marja L Mikkola<sup>1</sup> ([ORCID: 0000-0002-9890-3835](https://orcid.org/0000-0002-9890-3835)) †

### Affiliations

1. Developmental Biology Program Institute of Biotechnology, University of Helsinki Helsinki Finland

† Corresponding author

## Abstract

Mesenchymal condensation is a critical step in organogenesis, yet the underlying molecular and cellular mechanisms remain poorly understood. The hair follicle dermal condensate is the precursor to the permanent mesenchymal unit of the hair follicle, the dermal papilla, which regulates hair cycling throughout life and bears hair inductive potential. Dermal condensate morphogenesis depends on epithelial Fibroblast Growth Factor 20 (Fgf20). Here, we combine mouse models with 3D and 4D microscopy to demonstrate that dermal condensates form de novo and via directional migration. We identify cell cycle exit and cell shape changes as early hallmarks of dermal condensate morphogenesis and find that Fgf20 primes these cellular behaviors and enhances cell motility and condensation. RNAseq profiling of immediate Fgf20 targets revealed induction of a subset of dermal condensate marker genes. Collectively, these data indicate that dermal condensation occurs via directed cell movement and that Fgf20 orchestrates the early cellular and molecular events.

## Introduction

The mesenchymal condensation, first recognized in limb bud condensations and named ‘precartilage condensates’ by Dame Honor Fell (Fell, 1925), is a tissue-level structure preceding organ development. Since then, mesenchymal condensations have been described in the precursors of several organs, occurring in most ectodermal appendages (tooth, hair, mammary gland, feather, scales) as well as in bone and muscle (Widelitz and Chuong, 1999; Hall and Miyake, 2000; Newman and Bhat, 2007; da Rocha-Azevedo and Grinnell, 2013; Biggs and Mikkola, 2014). The condensation has been suggested to be the basic cellular unit of a tissue, and to function as the driver of morphogenesis (Atchley and Hall, 1991), yet the underlying molecular and cellular mechanisms remain largely unknown. Condensations are morphologically distinguishable and are defined as a local increase in cell density. Characteristics of condensing mesenchymal cells include a change in cell shape, close surface contact between adjacent cells, and increased nucleus-to-cytoplasm ratio (Thorogood and Hinchliffe, 1975; Searls et al., 1972) (for review see [Hall and Miyake, 2000]). Signals from the epithelium are critical for mesenchymal cell condensation. The question of how a local increase in cell density is achieved remains to be addressed. Several modes of cell condensation have been proposed, including i) increase in mitotic activity, ii) active migration of cells, and iii) failure of cells to disperse due to changes in cell-cell and/or cell-extracellular matrix (ECM) interactions (Hall and Miyake, 1992).

The hair follicle (HF) is an excellent model to study the early attributes of mesenchymal condensation. HFs of the mouse dorsum develop in three waves as a result of reciprocal epithelial-mesenchymal signaling events with the first subset initiating morphogenesis at embryonic day (E) E13.5 and eventually producing guard hairs (Hardy, 1992). Within 24 hr, the previously homogenous epidermis exhibits discrete, focal thickenings, known as placodes, which are accompanied by condensation of the adjacent mesenchyme (Biggs and Mikkola, 2014). Coincident with dermal fibroblast condensation, their transcriptome profoundly alters. In particular, genes involved in cell-cell signaling such as Bmp4 and Wnt pathway components, p75 neurotrophin receptor, and many transcription factors including Sox2, one of the earliest markers of incipient dermal condensates (DC), are upregulated (Driskell et al., 2009; Sennett et al., 2015; Jones et al., 1991; Botchkareva et al., 1999). Another hallmark of DC formation is the differential expression of ECM molecules including tenascin, NCAM, and chondroitin sulfate proteoglycan, as well as syndecan-1 (Richardson et al., 2009). As HF morphogenesis continues, the DCs become enveloped by the down-growing follicular epithelium and subsequently mature into the permanent, mesenchymal component of the HF termed the dermal papilla (DP) (Morgan, 2014). The DP directs HF cycling throughout life and its miniaturization or absence results in a thinner or absent hair shaft (Chi et al., 2013; Rompolas et al., 2012). Of note, the DP has inductive capacity demonstrated by transplantation of freshly isolated or cultured (low passage) rodent DP cells under glabrous epithelium, which results in induction of hair follicle development (Oliver, 1970; Jahoda et al., 1984). By comparison, human DP cells lose their inductive capacity even faster in vitro but some activity can be sustained in 3D culture in aggregates (Higgins et al., 2013), suggesting that cellular condensation is tightly linked with DP cell fate specification and maintenance.

The molecular regulators of DC/DP morphogenesis have slowly begun to emerge. Absence of platelet-derived growth factor A (Pdgf-A) results in smaller DPs (Karlsson et al., 1999); however, the entire dermis is thinner, likely accounting for the DP phenotype as indicated by more recent studies in which the PDGF receptors were conditionally deleted in the dermis (Rezza et al., 2015). Another placode-derived factor implicated in DC formation is Sonic hedgehog (Shh) (Karlsson et al., 1999; St-Jacques et al., 1998; Chiang et al., 1999). However, conditional dermal deletion of Shh receptor Smoothened indicates a role in DC maintenance rather than induction (Woo et al., 2012). Several other known DC markers such as Sox2 (Clavel et al., 2012), Tbx18 (Grisanti et al., 2013a), Cxcr4 (Sennett et al., 2014), and Enpp2/autotaxin (Grisanti et al., 2013b) have also been conditionally ablated, but none of them results in absence of the DC.

Perhaps surprisingly, the most informative genetic studies uncovering the molecular basis of DC formation have been those targeting the epithelium. Wnt signaling is believed to be the at the top of the hierarchy of signaling factors guiding HF morphogenesis, and expression of stabilized β-catenin in the epidermis results in broad adoption of placode fate as well as condensed mesenchyme concomitant with DC marker expression throughout the upper dermis (Närhi et al., 2008; Zhang et al., 2008; Suzuki et al., 2009). The ectodysplasin (Eda)/Edar pathway is another essential pathway for placode morphogenesis: in its absence only rudimentary primary hair placodes form transiently and DCs are missing (Headon and Overbeek, 1999; Laurikkala et al., 2002; Schmidt-Ullrich et al., 2006). Downstream of Wnt and Eda signaling, placodal factor Fgf20 is expressed early during HF morphogenesis (Huh et al., 2013; Lefebvre et al., 2012). Deletion of Fgf20 results in absent DC in guard hairs and many secondary (awl and auchene) hairs as shown by morphological and molecular analyses, as well as failure in placode invagination, and ultimately, absent hairs (Huh et al., 2013). Moreover, the condensed mesenchyme observed in embryos expressing stabilized epithelial β-catenin was ablated in the absence of Fgf20 further confirming the indispensable function of Fgf20 in DC induction.

Although these molecular players have been investigated, the cellular mechanism of DC development and the role that Fgf20 plays in DC morphogenesis remain unknown. We therefore aimed to define the hallmarks of DC morphogenesis and the function that Fgf20 plays in this process. We applied a multifaceted approach to determine the cellular and molecular changes leading to DC morphogenesis using murine back skin primary hair follicle as the model due to its feasibility for manipulation and ex vivo imaging (Ahtiainen et al., 2014). We identify cell shape changes and cycle exit as early hallmarks of DC morphogenesis. Live confocal imaging and lineage tracing showed that fibroblasts were recruited from the near vicinity and not from a pre-specified pool of Sox2+ cells, and migrate toward placodal epithelium. Further, Fgf20 induced fibroblast migration and cell shape change, as well as transcriptional responses that suggest its involvement in cell cycle exit. Collectively, our data show that Fgf20 governs multiple cellular and molecular events critical for DC formation.

## Results

### Dermal fibroblasts condense and change shape below the developing hair follicle placode

To determine to what extent the fibroblasts within the dermal condensate are more densely packed than the interfollicular fibroblasts, we examined primary HFs in E14.5 whole skin in 3D using confocal microscopy. The volume of the DC was determined by using a transgenic Sox2-GFP reporter (Figure 1A, left panel), whose expression correlates well with endogenous Sox2 ([Driskell et al., 2009]; Figure 1A), and the same volume was used on an interfollicular area of the upper dermis. Quantification of nuclei confirmed that cells were nearly twice as dense within the DC than in the interfollicular area (p=0.000106) (Figure 1B). We have previously shown that Fgf20β-Gal/β-Gal (hereafter Fgf20-/-) mice lack all molecular signs of primary DC formation including Sox2 (Huh et al., 2013) (Figure 1A, right panel), and quantification of dermal fibroblast density directly underneath the Fgf20-/- placode revealed that these fibroblasts exhibit density similar to that of the wild-type interfollicular dermis (p=0.962425) (Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig1-v2.jpg)

**Figure 1.:** (A) Confocal microscopy immunofluorescent optical sections (planar and sagittal views) of E14.5 control (Fgf20+/-;Sox2-GFP) and Fgf20-/-;Sox2-GFP (green) embryonic skin labelled with antibodies against Sox2+ (white) and β-galactosidase (β-gal, red) to visualize DC and placodes, respectively. Note the absence of Sox2 antibody staining and Sox2-GFP reporter in Fgf20-/- HFs. (B) Quantification of fibroblasts in E14.5 Sox2-GFP DC volume in Fgf20+/- DC and interfolliclular upper dermis (IF) as well as in Fgf20-/- dermis immediately adjacent to placodes (SPD), (n = 5 placodes from two skins Fgf20+/-; n = 6 placodes from two skins Fgf20-/-) unpaired Student’s T-test. (C) Confocal microscopy immunofluorescent optical sections (planar and sagittal views) of Fgf20+/- HF between E13.5 and E14.5, labeled with antibodies against Sox2 (white) and β-Gal (red). Placode morphogenesis was divided into four categories based on advancing development (I–IV). (D) Quantification of Sox2+ cells at each stage of placode morphogenesis (one-way ANOVA, n = 11, 7, 11, 13 placodes from 6, 4, 11, and 8 skins for stages I – IV, respectively). (E) Quantification of the median distance of Sox2+ cells to the nearest placode surface (one-way ANOVA, n = 11, 7, 11, 13 placodes from 6, 4, 11, and eight skins for stages I – IV, respectively) (F) Transmission electron micrographs of E14.5 wild-type skin dermal condensation (DC) and an interfollicular (IF) region. Note the convex nuclei and lack of space between the cells in the DC compared to the non-DC region. (G) Confocal optical sections (sagittal view) of advancing HF morphogenesis (stages I-IV); Sox2+ nuclei (red) are contrasted with Sox2- nuclei (blue); white outlines provide an example of cells compared. (H) Quantification of sphericity of Sox2+ and Sox2- nuclei; significance was assessed using Student’s T-test (nI = 92 and 162 (6 placodes, three skins), nII = 253 and 163 (6 placodes, two skins), nIII = 332 and 217 (6 placodes, two skins), nIV = 125 and 137 (8 placodes, three skins) DC and IF cells, respectively). A, anterior; P, posterior; SPD, sub-placodal dermis. Error bars represent standard deviation (SD). *p≤0.05; **p≤0.01; ***p≤0.001; ****p≤0.0001. Scale bar = 10 µm. See also Figure 1—video 1 and Figure 1—source data 1.

Next, we wanted to quantify DC formation in more detail. Primary hair placode induction is a continuous process first occurring near the mammary line and proceeding dorsally and caudally (Dhouailly et al., 2004), and hence the same embryo contains hair placodes in different developmental stages. To better capture the dynamic nature of DC formation, we categorized hair placodes in four developmental stages. Follicular epithelium was identified by the Fgf20β-gal knock-in allele, one of the earliest placode markers ([Huh et al., 2013]; Figure 1C). Stage I was defined as a single layered placode, and stage II as a multilayered placode. Stage III is a placode that has invaginated into the dermis, and stage IV placodes have an anterior pocket where DC cells reside (Figure 1C). The number and distance from placodes of Sox2+ cells was analyzed in 3D. Throughout these stages, the number of Sox2+ cells associated with each placode increased significantly (p<0.0001) (Figure 1D). Quantification of their distance from the placode revealed a progressive decrease in median distance (p<0.0001) (Figure 1E). At stage I, some dispersed Sox2+ cells were observed, which by stage II were preferentially oriented on the anterior side of the placode. By stage III, the cells appeared to be closer to the placode, and at stage IV, the Sox2+ cells maintained their proximity but increased in number (Figure 1D,E).

Mesenchymal cell condensation is often accompanied by cell shape changes (Ray and Chapman, 2015; Mammoto et al., 2011). Our 3D analysis (Figure 1A,C) also suggested that DC formation correlates with cell shape changes. Transmission electron microscopy (TEM) revealed that E14.5 DC cells have an elongated, convex shape and display a characteristic alignment next to each other (Figure 1F). 3D rendering of nuclear shapes in whole mount and subsequent quantifications of nuclear sphericity during DC formation showed that the change in nuclear shape is an early indicator of DC formation (all stages p<0.0001) (Figure 1G,H). Consistent with the TEM and nuclear data, 3D rendering of cell shapes based on a ubiquitous cell membrane marker confirmed that Sox2+ DC cells exhibited a convex shape, whereas the non-DC fibroblasts were relatively spherical (Figure 1—video 1).

### Dermal condensate cells acquire Sox2 expression de novo

Given that the number of Sox2+ cells increased while their distance to placode decreased over time, and that the dermis contains Sox2+ Schwann cell precursors (Jessen and Mirsky, 2005), we next asked whether the DC cells were recruited from a pre-existing pool of Sox2+ cells or whether they acquired Sox2 expression de novo. To this end, we utilized Sox2creERT2;R26RtdTomato/+ embryos and analyzed tdTomato expression after 24 or 48 hr of tamoxifen (TAM) exposure beginning at E12.5 (before morphological and molecular appearance of HF), E13.5 (earliest molecular sign of HF), and at E14.5 (placode stage of HF) (Figure 2A−F). To minimize the effect of variation in HF development, we examined hair follicles from the same region in all embryos (ventro-lateral skin) and quantified the total number of Sox2+ cells using Sox2 antibody and analyzed the proportion of tdTomato-labeled cells amongst them (Figure 2G,H). When labeling was induced at E14.5 and cells analyzed 24 hr later, 65% of Sox2+ cells were tdTomato+, indicating that the TAM dosage used results in a relatively high labeling efficiency (Figure 2D,G). Strikingly, when TAM was administered at E13.5, only 20% of Sox2+ cells were tdTomato 24 hr later (Figure 2C,G). This proportion, however, increased substantially when mice were analyzed at E15.5 (Figure 2F,G). Finally, when TAM was administered at E12.5 and DC cells analyzed at E13.5 and 14.5, only 5% and 8% of Sox2+ cells were tdTomato+, respectively (Figure 2B,E,G) indicating that there is no pre-specified pool of Sox2+ cells. Analysis of secondary hair placodes (that form at E15.5) in mice injected with TAM at E13.5 or E14.5 revealed that 5% and 12% of Sox2+ cells were labeled, respectively, further confirming that DC cells acquire Sox2 expression de novo (Figure 2—figure supplement 1).

![Figure 2.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig2-v2.jpg)

**Figure 2.:** (A) Scheme of tamoxifen (TAM) injection and analysis. A single labeling dose of TAM was administered to pregnant dams at E12.5, E13.5, or E14.5. (B–F) Confocal microscopy immunofluorescent optical sections (planar view) of Sox2creERT;R26RtdTomato skins immunolabeled with Sox2 (white), tdTomato label (red), and EpCAM (green) at 24 or 48 hr after TAM administration (n > 4 injections; E12.5 + 24 hr, n = 23 DCs from nine skins; E12.5 + 48 hr, n = 23 DCs from seven skins; E13.5 + 24 hr, n = 33 DCs from 11 skins; E13.5 + 48 hr, n = 23 DCs from eight skins; E14.5 + 24 hr, n = 21 DCs from nine skins). (B) E12.5 + 24 hr resulted in very few labeled Sox2 cells. (C) E13.5 + 24 hr showed increased labeling of Sox2+ cells. (D) TAM induction at E14.5 resulted in a majority of Sox2+ cells labeled within 24 hr. (E) E12.5 + 48 hr resulted in a low number of tdTomato+, Sox2+ cells. (F) E13.5 + 48 hr resulted in a large number of Sox2+ cells labeled with tdTomato. (G) Quantification of Sox2+ cells positive for tdTomato label at indicated time points; significance was assessed with one-way ANOVA. (H) Quantification of the average number of tdTomato+ cells as part of the whole Sox2+ cell population (E12.5 + 24 hr=2 of 33 cells; E12.5 + 48 hr=5 of 63 cells; E13.5 + 24 hr=14 of 67 cells; E13.5 + 48 hr=40 of 74 cells; E14.5 + 24 hr=53 of 82 cells). (I) Quantification of the distance of tdTomato+ and tdTomato- (n = 11 placodes from four skins) Sox2+ cells from placode surface, significance was assessed with Student’s T-test. (J) Nearest neighbor analysis of Sox2+ cells for tdTomato label (87.7%) vs unlabeled (12.2%) at E15.5 (n = 635), significance was assessed with Chi-square test. Error bars represent SD. *p≤0.05; ****p≤0.0001. Scale bar = 10 µm. See also Figure 2—source data 1 and Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Scheme of tamoxifen (TAM) injection and analysis. A single labeling dose of TAM was administered to pregnant dams at E13.5, or E14.5. (B, C) Confocal optical section of secondary DCs from Sox2CreERT;R26RtdTomato/+ skins at E15.5; tdTomato (red), and labelled with antibodies against Sox2 (white), EpCAM (green) from E13.5 (B), and E14.5 (C) tamoxifen injection. E13.5 + 48 hr resulted in very few labeled Sox2 cells. (C) E14.5 + 24 hr showed labeling of more Sox2 cells. (D) Quantification of percent tdTomato labeled Sox2+ cells (n = 2 injections per time point, E13.5 + 48 hr, n = 8 DCs from five skins and E14.5 + 24 hr, n = 10 DCs from six skins). Error bars represent SD. Scale bar = 10 µm. See also Figure 2—figure supplement 1—source data 1 and Figure 2.

While quantifying the Sox2+;tdTomato+ cells in the DC, we noticed that they exhibited a preferential location adjacent to the placode, while cells that recently acquired DC fate (Sox2+, tdTomato-) appeared further away from the epithelium (Figure 2). We quantified this phenomenon in E15.5 HFs labeled at E14.5 (where 65% of the Sox2+ were tdTomato+) (Figure 2G,H) and measured the median distance of the tdTomato+ cells to the center of the placode surface. Our analysis revealed that the Sox2+;tdTomato+ cells were significantly closer to the placode than Sox2+;tdTomato- cells (p=0.0105) (Figure 2I). Nearest neighbor analysis showed that 87% of tdTomato positive cells had a tdTomato+ neighbor and hence were not randomly distributed (p<0.0001) (Figure 2J). Together, these data indicate that DC cells gain Sox2 expression just prior to becoming a DC cell. Further, we find that cells do not randomly assort after entering the DC, thus the ‘oldest’ DC cells are most likely to be located closest to the placode.

### Dermal condensate formation is associated with cell cycle exit

An increase in cell number can be achieved in a number of ways. Our quantifications revealed that when TAM was administered at E13.5, on average 20% and 53% of Sox2+ cells were tdTomato+ at E14.5 and 15.5, respectively (Figure 2G). Given that the average number of Sox2+ DC cells increased only by seven cells (from 67 to 74) from E14.5 to E15.5 in the same dataset (Figure 2H), our findings suggest that either TAM remains active for longer than 24 hr as previously suggested (Hayashi and McMahon, 2002), or that Sox2+ cells labeled between E13.5 and E14.5 increase in number by proliferation. To test whether locally enhanced proliferation could drive DC formation, we assessed cell cycle dynamics during DC morphogenesis with the aid of a bitransgenic cell cycle indicator Fucci mouse model (Sakaue-Sawano et al., 2008) in which mKusabira Orange (mKO) is expressed during the G1/G0 phase (hereafter G1) and mAzami Green (mAG) during the S/G2/M phase (Figure 3A). The interfollicular dermal cells (Sox2-) were equally distributed between G1 and S/G2/M phases at all stages of placode morphogenesis analyzed (Figure 3B). In contrast, the Sox2+ cells showed progressive exit from the cell cycle. At stage I, the Sox2+ cells were nearly evenly distributed between proliferative and non-proliferative phases. By stage II, the majority of Sox2+ cells were in G1, which persisted through stages III and IV (pI = 0.0166, pII = 0.002, pIII, IV < 0.001, Figure 3B). Further, the percent non-proliferating cells in the stage I DC was significantly lower than the following stages (pIvsII = 0.0211), suggesting that DC fate acquisition occurs before cell cycle exit. This cell cycle exit was not transient as the vast majority of DC cells remained in G1 through E15.5 (Figure 3B,C). To determine whether this cell cycle exit is dependent on Fgf20, we analyzed the cell cycle status of E14.5 Fgf20-/- fibroblasts. Immediately below the placode, in a volume equivalent to a wild-type stage IV DC, the proportion of G1 and S/G2/M cells did not differ from that of the interfollicular dermal cells (p=0.473, Figure 3B and D). To further substantiate our findings, we examined the cell cycle distribution in mice overexpressing Eda under the Keratin14 promoter (K14-Eda), a model of enlarged DC. Not only are the placodes bigger at E14.5 than in the wild type (Mustonen et al., 2004; Ahtiainen et al., 2014), but there are also more Sox2+ cells (Huh et al., 2013). Similar to control DC, about 95% of the Sox2+ DC cells were in the G1 phase (Figure 3B,E) indicating that increased DC size can be achieved without enhancing cellular proliferation. Similar findings were observed with the R26Fucci2aR cell cycle indicator mouse model (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig3-v2.jpg)

**Figure 3.:** (A, C–E) Confocal microscopy optical planar sections of Fgf20+/-;Fucci (G1 red; S/G2/M green) skins at indicated stages of HF placode morphogenesis (I–IV) were labeled with antibodies against β-Gal (cytoplasmic white) and Sox2 (nuclear white). (A) The Sox2+ nuclei were scored as red, green, both, or neither and compared to the interfollicular Sox2- fibroblasts (n = eight placodes per stage from seven, four, five, and five skins in stages I, II, III, and IV, respectively). (B) Quantification of percent Sox2+ (DC) cells and Sox2- (IF) fibroblasts in G0/G1 phase during HF placode morphogenesis (I–IV), in E14.5 K14-Eda (Eda), in E14.5 Fgf20-/- (KO), and in E15.5 Fgf20+/- (E15.5), paired Student’s T-test. (C–E) Expression of Fucci transgenes in (C) E15.5 control DCs (n = nine placodes from four skins), (D) E14.5 Fgf20-/- dermis immediately adjacent to the placode (n = seven placodes from three skins), and (E) E14.5 K14-Eda (n = six placodes from two skins) DCs. (F) Confocal microscopy optical planar sections of Fgf20+/- skins at indicated stages of HF placode morphogenesis (I–IV). Embryos were subjected to 2 hr EdU pulse in utero prior to sacrifice. Skins were treated with Click-It detection to visualize EdU-positive cells (green) and immunolabeled with Sox2 (white) and β-gal (red, not shown). (G) Quantification of EdU-positive Sox2 DC cells (nI = 11 placodes from three skins, nII = 10 placodes from five skins, nIII = 10 placodes from five skins, nIV = 11 placodes from five skins). *, p≤0.05; ***, p≤0.001 ****, p≤0.0001. Error bars represent SD. Scale bar = 10 µm. See also Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Confocal optical section of DC during DC morphogenesis (stages I-IV) from R26Fucci2aR;Fgf20+/- skins immunolabeled with Sox2 (white). Red represents G0/G1 phase while green represents S/G2/M phase of the cell cycle.

To confirm our observations, we further assessed cell proliferation using a uridine-analogue EdU incorporation assay at different stages of DC development (Figure 3F). Concordantly with the Fucci-reporter analysis, at stage I we observed that 18% of the Sox2+ DC cells were EdU positive, but at stage II the proportion of EdU-positive cells dropped significantly to 5.2% (pIvsII = 0.003) and remained unchanged through stage IV (pIIvsIII = 0.277, pIIIvsIV = 0.591). Collectively, these data suggest that cell cycle exit is a hallmark of dermal condensate morphogenesis.

### Directed migration of fibroblasts drives dermal condensate formation

Having ruled out proliferation as a mechanism for the increased cell density in DC cells, we next assessed the contribution of cellular migration by using live, confocal 3D imaging. We utilized Sox2-GFP;FuccimKO skins to monitor the behavior of DC-forming cells and as a control, tracked interfollicular, non-DC fibroblasts (Sox2-GFP−) at the corresponding cell cycle phase (FuccimKO+ cells). Cultures were initiated at E13.75, a time point when incipient DCs were visible (Figure 4A and Video 1).

![Figure 4.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig4-v2.jpg)

**Figure 4.:** (A) Maximum intensity projections of indicated time points from live confocal imaging of E13.75 Sox2-GFP; FuccimKOskins. (B) Representative 2D plots of movement tracks of condensate forming (left) or IF (right) cells that are initially >30 µm (grey) and <30 µm (red) from the DC center. (C) Vectors of escape angles (the angle between cell trajectory in respect to center of the DC/interfollicular area and endpoint of trajectory) of cells that were initially >30 µm (left, n = 49 cells from eight placodes, images from six skin explants) and <30 µm (center, n = 127 cells from eight placodes, images from six skin explants) from the DC center, and interfollicular cells (right, n = 97 cells from eight placodes, images from six skin explants). Condensate-forming cells initially >30 µm from condensate center preferentially migrate toward condensate center (median 22°) whereas condensate-forming cells initially <30 µm from the center (median 48°) and interfollicular (median 68°) cells show no preferential direction of movement. Watson’s U2 test shows a significant difference in escape angles in DC cells initially further away (>30 µm) from DC center versus interfollicular cells (p<0.001) or DC cells initially close (<30 µm) to the DC center (p<0.05). (D–F) Distribution of (D) cell velocity, (E) straightness, and (F) net velocity during DC formation. Significance was assessed with Mann-Whitney test. Condensate forming cells migrating initially >30 µm away from the DC center migrate faster than condensate-forming cells initially close (<30 µm) to the DC center (p=0.0022) and interfollicular cells (0.0051), but no difference was observed in track straightness (p=0.8945 and p=0.2376, respectively) or net velocity (p=0.5949 and p=0.139, respectively) between the groups. n.s., not significant; *p≤0.05; **p≤0.01; ***p≤0.001. Error bars represent SD. See also Video 1, Figure 4—source data 1, and Figure 4—figure supplement 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) 2D plot of escape angles of condensate-forming cells until entry to DC. Cell movement showed preferential movement toward condensate center (median 27.7°) and this directionality was significantly different from the IF cell migration (see Figure 4) (ncells = 80 and 97 DC and IF, respectively, from eight placodes images from six skin explants, Watson’s U2 test). (B) Distribution of straightness of cell tracks. Condensate-forming cells migrate on a straighter track than interfollicular cells (Mann-Whitney test). (C) Distribution of net velocities. Condensate-forming cells display higher net velocity than interfollicular cells (Mann-Whitney). *, p≤0.05; ***, p≤0.001. Error bars represent SD. See also Figure 4—figure supplement 1—source data 1 and Figure 4.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Maximum intensity projections of F-actin in Sox2-GFP-positive cells (cyan) and dermal fibroblasts (grey). Placode position is marked by magenta dashed line. (B) Quantification of F-actin signal in DC and non-DC Sox2-GFP-positive cells and in Sox2-GFP-negative dermal fibroblasts (nSox2-GFP+DC = 49, nSox2-GFP+non-DC=76, and nIF = 76 cells, eight placodes from two skins). (C) Confocal microscopy immunofluorescent optical sections (planar and sagittal views) of Fgf20+/-HF between E13.5 and E14.5, labeled with antibodies against Sox2 and β-Gal (magenta) and phalloidin for F-actin (heatmap). Placode morphogenesis was divided into four categories based on advancing development (I–IV). (D) Quantification of F-actin signal inside DC selection (magenta dashed line) and dermal selection (yellow dashed line) at each stage of placode morphogenesis (nI = six placodes, nII = eight placodes, nIII = six placodes, nIV = eight placodes; two skins analyzed for each stage). **, p≤0.01; ***, p≤0.001, ****, p≤0.0001. Error bars represent SD. See also Figure 4—figure supplement 2—source data 1 and Figure 4.

![Video 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-video1.mp4.jpg)

**Video 1.:** Dorsal skin from E13.75 Fucci-mKO;Sox2-GFP was explanted into Trowell culture set up and imaged with Leica TCS SP5 confocal microscope for 13 hr. Tracks of manually traced DC cells (Sox2-GFP+, green; Fucci-mKO+, red) and non-DC fibroblasts (Sox2-GFP-; Fucci-mKO+, red cells) are shown. See also Figure 4 and Figure 4—figure supplement 1.

To characterize cell movement in detail, we quantified velocity, net velocity, straightness, and directionality. We initially tracked all Sox2-GFP+ DC cells (Figure 4A−C), but observed that many of the cells that were present in the condensates at the beginning of tracing displayed low velocity suggesting that their movement is restricted (Figure 4D). However, cells that were initially further than 30 µm (the average DC diameter) from the center of the condensate at the beginning of tracing behaved differently. Notably, these cells showed a preferential movement direction towards the condensate center, while interfollicular cells exhibited no directionality (Figure 4B,C). We observed that the condensate-forming fibroblasts also moved at a significantly higher velocity than interfollicular cells (p=0.0051) (Figure 4D) yet there was no significant difference between the straightness of cell movement or net velocity (p=0.8945 and p=0.1390, respectively) (Figure 4E,F). Furthermore, when we analyzed migration of condensate-forming fibroblasts only until they enter the dermal condensate, not only were they preferentially moving toward the DC center but also migrated on a significantly straighter track (p=0.0232) and had higher net velocity than the interfollicular cells (p=0.0006) (Figure 4—figure supplement 1).

As cell migration is associated with remodeling of the actin cytoskeleton (for review see [Svitkina, 2018]), we investigated whether Sox2-GFP cells presumably en route to the DC could be distinguished from other dermal fibroblasts or Sox2-GFP cells already present in the DC based on the organization of their actin cytoskeleton. The non-DC Sox2-GFP cells displayed a slightly higher intensity of F-actin than dermal fibroblasts, which may be indicative of their migratory status (Figure 4—figure supplement 2A,B). However, the Sox2-GFP cells within the DC displayed even higher levels of F-actin intensity compared to non-DC Sox2-GFP cells (Figure 4—figure supplement 2A,B). Further, the intensity of F-actin increased as the DC progressed through morphogenesis (Figure 4—figure supplement 2D,E). As these cells exhibited reduced motility, this suggests that the F-actin is involved in maintaining the 3D configuration of the DC. Together, these results suggest that directed migration of the dermal fibroblasts is driving DC formation, but once the cells have entered the DC, their motile behavior changes, likely due to limitations posed by increased cell density, a finding in line with our lineage tracing/nearest neighbor analysis (Figure 2I,J).

### Transcriptional responses of Fgf20 in the dermis

In order to address the function of Fgf20 in DC formation, we first aimed to identify its immediate transcriptional targets. Isolated E13.5 Fgf20-/- dermises were cut into two pieces: one half was incubated in recombinant FGF20 for 3 hr, and the other half in BSA. RNA sequencing was carried out on five pairs of biological replicates (Figure 5A). Differential gene expression analysis revealed 40 protein-coding genes including many known Fgf/MAPK pathway target genes and feedback regulators (Ornitz and Itoh, 2015; Murphy et al., 2010), such as those within the Dual-specificity phosphatase (Dusp), Sprouty and Sprouty-related Spred gene families (Table 1). We validated the RNAseq by qRT-PCR analysis of a subset of these genes in independently generated samples (Figure 5B). Of the 31 upregulated genes, 7 belong to the recently identified DC signature, and an additional 5 genes were >2 x more highly expressed in DC compared to non-DC fibroblasts in the same study (Sennett et al., 2015). Notably, several genes implicated in cell cycle regulation such as Bcl6 and Cdkn1a (p21), a cyclin-dependent kinase inhibitor, which we previously identified as an early DC marker (Huh et al., 2013), were among the upregulated genes (Table 1).

![Figure 5.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig5-v2.jpg)

**Figure 5.:** (A) Schematic of the experimental setup. E13.5 Fgf20-/- dermises were separated into halves along the dorsal midline, each half was cultured for 3 hr in the presence of either 1 µg/ml FGF20 or with 0.1% BSA vehicle control. RNA was extracted and processed for RNA sequencing. (B) qRT-PCR was carried out on replicate samples for Spry4 (n = 8), Dusp6 (n = 7), Etv5 (n = 7), Spred1 (n = 6), and Bcl6 (n = 7). Significance was assessed with one-sample T-test, **=p < 0.01. Error bars represent SD. (C) Skins from E15.5 Fgf20+/- (control), K14-Edar;Fgf20+/-, and K14-Edar;Fgf20-/- embryos (n = 6 embryos each) were assayed for β-galactosidase activity to assess the expression of the Fgf20β-Gal knock-in allele (top). Note the follicular localization of β-Gal activity in Fgf20+/- embryos, which is localized throughout the epidermis in K14-Edar;Fgf20+/-, and K14-Edar;Fgf20-/- embryos. Radioactive in situ hybridization was utilized to detect Cdkn1a (p21) (middle) and Sox2 (bottom) at E16.5. Note that Cdkn1a was restricted to the DC in the dermis in control embryos, but was localized throughout the upper dermis in K14-Edar embryos in an Fgf20-dependent manner. Cdkn1a was also strongly expressed in the differentiating epidermis and the panniculus carnosus muscle. See also Table 1, Figure 5—source data, and Figure 5—figure supplement 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) In situ hybridization for Edar at E16.5. (n = 5 embryos) (B) E16.5 skins from Fgf20+/-, K14-Edar;Fgf20+/-, and K14-Edar;Fgf20-/- embryos (n = 6 embryos) were used to determine the density of cells 30 µm below the epidermis, excluding the Sox2+ DCs (K14, green; Sox2, red; nuclei, white). (C) Quantification of fibroblast density in the upper dermis (One-way ANOVA). n.s., not significant. Error bars indicate SD. Scale bar = 100 µm. See also Figure 5—figure supplement 1—source data 1 and Figure 5.

**Table 1.**
 Differentially expressed genes after 3 hr FGF20 treatment.Genes in red: Fold DC vs. Fb is >2 x in Sennett et al., 2015; * indicates a DC signature gene. Genes in blue: Fold Fb vs. DC is >2 x in Sennett et al., 2015; # indicates a Fibroblast signature gene. See also Figure 5 and Figure 5—figure supplement 1.


<table>
  <thead>
    <tr>
      <th>Ensembl gene ID</th>
      <th>Gene symbol</th>
      <th>Log2 fold change</th>
      <th>q-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ENSMUSG00000024427</td>
      <td>Spry4</td>
      <td>1,24306661</td>
      <td>2,87958E-14</td>
    </tr>
    <tr>
      <td>ENSMUSG00000040276</td>
      <td>Pacsin1</td>
      <td>1,117757314</td>
      <td>0,005409828</td>
    </tr>
    <tr>
      <td>ENSMUSG00000000938</td>
      <td>Hoxa10</td>
      <td>1,067306677</td>
      <td>4,89962E-05</td>
    </tr>
    <tr>
      <td>ENSMUSG00000022484</td>
      <td>Hoxc10</td>
      <td>1,055122804</td>
      <td>0,000135006</td>
    </tr>
    <tr>
      <td>ENSMUSG00000037580</td>
      <td>Gch1</td>
      <td>0,953581456</td>
      <td>0,001623219</td>
    </tr>
    <tr>
      <td>ENSMUSG00000039628</td>
      <td>Hs3st6*</td>
      <td>0,9259377</td>
      <td>0,048932785</td>
    </tr>
    <tr>
      <td>ENSMUSG00000013089</td>
      <td>Etv5</td>
      <td>0,904428558</td>
      <td>3,51931E-06</td>
    </tr>
    <tr>
      <td>ENSMUSG00000019960</td>
      <td>Dusp6</td>
      <td>0,768627588</td>
      <td>2,59873E-05</td>
    </tr>
    <tr>
      <td>ENSMUSG00000000435</td>
      <td>Myf5</td>
      <td>0,741106812</td>
      <td>0,021043062</td>
    </tr>
    <tr>
      <td>ENSMUSG00000022508</td>
      <td>Bcl6*</td>
      <td>0,71492512</td>
      <td>0,001178264</td>
    </tr>
    <tr>
      <td>ENSMUSG00000014813</td>
      <td>Stc1</td>
      <td>0,70075808</td>
      <td>8,12534E-07</td>
    </tr>
    <tr>
      <td>ENSMUSG00000022367</td>
      <td>Has2</td>
      <td>0,688772195</td>
      <td>0,000329738</td>
    </tr>
    <tr>
      <td>ENSMUSG00000046223</td>
      <td>Plaur</td>
      <td>0,680287177</td>
      <td>0,019395279</td>
    </tr>
    <tr>
      <td>ENSMUSG00000037211</td>
      <td>Spry1*</td>
      <td>0,668125166</td>
      <td>0,000252705</td>
    </tr>
    <tr>
      <td>ENSMUSG00000020023</td>
      <td>Tmcc3</td>
      <td>0,652897112</td>
      <td>0,017991893</td>
    </tr>
    <tr>
      <td>ENSMUSG00000045671</td>
      <td>Spred2</td>
      <td>0,646652707</td>
      <td>0,021043062</td>
    </tr>
    <tr>
      <td>ENSMUSG00000032020</td>
      <td>Ubash3b*</td>
      <td>0,608057108</td>
      <td>0,025457783</td>
    </tr>
    <tr>
      <td>ENSMUSG00000022114</td>
      <td>Spry2#</td>
      <td>0,604959493</td>
      <td>3,29426E-05</td>
    </tr>
    <tr>
      <td>ENSMUSG00000039680</td>
      <td>Mrps6</td>
      <td>0,587495288</td>
      <td>0,048932785</td>
    </tr>
    <tr>
      <td>ENSMUSG00000043099</td>
      <td>Hic1</td>
      <td>0,58156032</td>
      <td>7,06147E-06</td>
    </tr>
    <tr>
      <td>ENSMUSG00000021567</td>
      <td>Nkd2</td>
      <td>0,574323421</td>
      <td>0,048932785</td>
    </tr>
    <tr>
      <td>ENSMUSG00000025402</td>
      <td>Nab2</td>
      <td>0,573087974</td>
      <td>0,001623219</td>
    </tr>
    <tr>
      <td>ENSMUSG00000026064</td>
      <td>Ptp4a1</td>
      <td>0,560735472</td>
      <td>0,049490799</td>
    </tr>
    <tr>
      <td>ENSMUSG00000026655</td>
      <td>Fam107b*</td>
      <td>0,552834404</td>
      <td>0,000598789</td>
    </tr>
    <tr>
      <td>ENSMUSG00000046324</td>
      <td>Ermp1</td>
      <td>0,545018197</td>
      <td>0,004713961</td>
    </tr>
    <tr>
      <td>ENSMUSG00000015957</td>
      <td>Wnt11#</td>
      <td>0,521839644</td>
      <td>0,030834254</td>
    </tr>
    <tr>
      <td>ENSMUSG00000023067</td>
      <td>Cdkn1a*</td>
      <td>0,509994166</td>
      <td>0,048932785</td>
    </tr>
    <tr>
      <td>ENSMUSG00000027351</td>
      <td>Spred1*</td>
      <td>0,501328957</td>
      <td>0,017546304</td>
    </tr>
    <tr>
      <td>ENSMUSG00000053716</td>
      <td>Dusp7</td>
      <td>0,498184179</td>
      <td>0,017991893</td>
    </tr>
    <tr>
      <td>ENSMUSG00000007029</td>
      <td>Vars</td>
      <td>0,396158628</td>
      <td>0,048932785</td>
    </tr>
    <tr>
      <td>ENSMUSG00000018001</td>
      <td>Cyth3</td>
      <td>0,388676591</td>
      <td>0,017546304</td>
    </tr>
    <tr>
      <td>ENSMUSG00000029563</td>
      <td>Foxp2</td>
      <td>−0,555487269</td>
      <td>0,028254118</td>
    </tr>
    <tr>
      <td>ENSMUSG00000046743</td>
      <td>Fat4#</td>
      <td>−0,569844598</td>
      <td>0,006906967</td>
    </tr>
    <tr>
      <td>ENSMUSG00000036995</td>
      <td>Asap3</td>
      <td>−0,763477567</td>
      <td>0,021457852</td>
    </tr>
    <tr>
      <td>ENSMUSG00000028036</td>
      <td>Ptgfr#</td>
      <td>−0,85391079</td>
      <td>6,19325E-06</td>
    </tr>
    <tr>
      <td>ENSMUSG00000035352</td>
      <td>Ccl12</td>
      <td>−0,855627781</td>
      <td>0,01168856</td>
    </tr>
    <tr>
      <td>ENSMUSG00000026163</td>
      <td>Sphkap</td>
      <td>−1,030633182</td>
      <td>0,001174907</td>
    </tr>
    <tr>
      <td>ENSMUSG00000070304</td>
      <td>Scn2b</td>
      <td>−1,038110113</td>
      <td>0,009838673</td>
    </tr>
    <tr>
      <td>ENSMUSG00000042604</td>
      <td>Kcna4#</td>
      <td>−1,228592873</td>
      <td>0,000211934</td>
    </tr>
    <tr>
      <td>ENSMUSG00000029394</td>
      <td>Cdk2ap1</td>
      <td>−1,589028583</td>
      <td>0,011081145</td>
    </tr>
  </tbody>
</table>

_Genes in red: Fold DC vs. Fb is >2 x in Sennett et al., 2015; * indicates a DC signature gene.Genes in blue: Fold Fb vs. DC is >2 x in Sennett et al., 2015; # indicates a Fibroblast signature gene._

To assess whether Fgf20 could also drive the expression of the potential transcriptional target genes in vivo we attempted to create a gain-of-function mouse line expressing Fgf20 under the K14 promoter. Unfortunately, we were unsuccessful in generating K14-Fgf20 lines that would display detectable Fgf20 overexpression, and we therefore took advantage of a mouse model overexpressing Edar, the upstream regulator of Fgf20, under the K14 promoter (Pispa et al., 2004). We confirmed upregulation of Edar expression in the entire basal epithelium by in situ hybridization (Figure 5—figure supplement 1). Accordingly, Fgf20, visualized by the Fgf20β-gal knock-in reporter, was ectopically expressed in the basal layer from E15.5 onwards (Huh et al., 2013) (Figure 5C). Consistent with our RNAseq analysis, we observed ectopic Cdkn1a expression in the mesenchyme immediately adjacent to the Fgf20-expressing epithelium on the K14-Edar background, whereas in the control dermis its expression was confined to the DC (Figure 5C), as reported previously (Huh et al., 2013). Importantly, Cdkn1a upregulation was Fgf20-dependent, as shown by its absence on the K14-Edar;Fgf20-/- background (Figure 5C). Further, Sox2 which was not upregulated by Fgf20 in our RNAseq data, was not detected in the K14-Edar or K14-Edar;Fgf20-/- embryos, but was readily observed in control embryos (Figure 5C and Figure 5—figure supplement 1). Collectively, these data suggest that Fgf20 regulates a subset of DC genes including Cdkn1a, a well-characterized inducer of G1 arrest of the cell cycle.

### Dermal fibroblasts migrate in vitro and condense ex vivo in response to Fgf20

Our analyses of 3D live imaging data showed that directional migration drives dermal condensate morphogenesis. This observation led us to ask whether Fgf20 signaling plays a role in this process. First, we analyzed the effect of Fgf20 signaling on migration of a monolayer of growth-arrested E13.5 primary dermal fibroblasts in a scratch wound healing assay over 24 hr. FGF20 induced significantly faster wound closure compared to control fibroblasts (p=0.0177), an effect that was abolished in the presence of an Fgfr inhibitor, SU5402 (p=0.6100), confirming the specificity of the response to FGF20 (Figure 6A and B). SU5402 alone had no significant effect on wound closure (p=0.2056) (Figure 6A and B). Similar observations were made when cells were treated with FGF9, a member of the same Fgf subfamily as Fgf20 (Figure 6—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig6-v2.jpg)

**Figure 6.:** (A, C) E13.5 cell cycle inhibited wild-type primary fibroblasts were utilized in scratch wound and transwell assays. (A) Phase-contrast images of scratch wounds (border denoted by dashed lines) at 0 hr (top) and 24 hr (bottom) post-wounding. The following treatments were added immediately prior to scratch induction: control (left) FGF20 (center left, 200 ng/ml), SU5402 (center right, 20 µM), or FGF20 +SU5402 (right). (B) Quantification of wound closure. At 24 hr, FGF20-treatment induced significantly faster wound healing relative to baseline control (closures 93.9 ± 5.73 and 67.3 ± 16.13% respectively, Student’s t-test), and this effect was suppressed with SU5402 (closure 63.2 ± 4.22%). SU5402 alone had no effect on wound closure (all treatments n = 5 experiments each performed with freshly extracted primary dermal fibroblast cell population). (C) Transwell migration assay. Migration was significantly increased when Fgf20 (200 ng/ml) was added to lower or both upper and lower chambers (n = 7 experiments each performed with freshly extracted primary dermal fibroblast cell population, one-sample T-test). No statistical difference was observed between the two FGF20-treatments (Student’s T-test). (D, F) Confocal images of E13.5 dermal explants cultured 3 hr with beads loaded with FGF20 or 0.1% BSA vehicle control and counterstained with Hoechst33342. Dashed line marks 30 µm radius from bead; nuclei within 15 µm (red) and 15–30 µm (blue) radii from beads. (E) Quantification of cell density from a single optical slice at mid-bead. FGF20 bead induced an increase in density within 15 µm radius from the bead relative to BSA control (paired Student’s t-test,), but not between 15 and 30 µm radius (one-sample t-test, n = 9 beads). (G) Quantification of nuclear sphericity. Within 15 µm from the bead nuclear shapes of Fgf20 treated samples are significantly less spherical than control (data are from eight beads; n BSA 0-15µm= 124; n BSA 15-30µm = 85; n Fgf20 0-15µm=136; n Fgf20 15-30µm = 69 cells), significance was assessed with Mann-Whitney test. (H) Whole-mount RNA in situ hybridization of dermal samples cultured with FGF20 or 0.1% BSA control beads for 3, 8, or 16 hr. Induction of Spry4 and Dusp6, but not Sox2 expression (purple) was observed around the bead at 3 hr. n indicates induction/total samples, induction was tested in two independent experiments with skin samples derived from ≥2 different litters. n.s., not significant *, p≤0.05; **, p≤0.01; ***, p≤0.001. Error bars represent SD. Scale bars: A = 100 µm; D, F, and H = 30 µm. See also Figure 6—source data and Figure 6—figure supplement 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Quantification of scratch wound closure of E13.5 growth-arrested primary dermal fibroblasts treated with FGF9 (200 ng/ml) or FGF9 and SU5402 (20 µM). At 24 hr, FGF9 treatment resulted in greater wound-closure at 8 hr (36.17 ± 5.04%, p=0.0490) and at 24 hr (97.11 ± 3.09%, p=0.0133) compared to DMSO control (all treatments n = 5 experiments, each performed with freshly extracted primary dermal fibroblast cell population). Wound closure was not altered when cells were treated with both FGF9 and SU5402 inhibitor (p=0.2563). (B) Quantification of transwell migration assay of E13.5 primary dermal fibroblasts. Migration was significantly increased when FGF9 (200 ng/ml) was added to lower or both upper and lower chambers (p=0.0003 and p=0.0010, respectively; for both n = 6 experiments, each performed with freshly extracted primary dermal fibroblast cell population). No statistical difference was observed between FGF9 treatments (p=0.4033). (C) Quantification of nuclei density in E13.5 dermis explants treated for 3 hr with beads loaded with FGF9 (100 µg/ml) or 0.1% BSA vehicle control. Density measured from a single optical slice at mid-bead. FGF9 bead induces an increase in density within 15 µm radius from the bead relative to BSA control (p=0.033, n = 7 explants), but not between 15 and 30 µm radius (p=0.236, n = 7 explants). (D) Whole-mount RNA in situ hybridization of dermal samples treated with FGF9 beads for 3, 8, and 16 hr. Induction of Spry4 and Dusp6, but not Sox2 expression (purple) was observed around the bead at all time points (n indicates induction/total samples, induction was tested in two independent experiments with skin samples derived from at least two different litters.). (E) 2 hr EdU incorporation into dermis organ cultures after overnight incubation with BSA (left), FGF20 (center), FGF9 (right) loaded beads. Note the increased number of proliferating cells around the FGF9 bead (n = 5 explants). Error bars represent SD. *, p≤0.05; **, p≤0.01; ***, p≤0.001. Scale bar = 30 µm. See also Figure 6—figure supplement 1—source data 1 and Figure 6.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** 3 hr incubation of BSA-, FGF20- or FGF9-loaded beads with E13.5 wildtype (A, B, C) or FuccimKO (D) dermises. Cdkn1a expression was assayed in these samples using (A) whole-mount RNA in situ hybridization of dermal samples. Cdkn1a expression (purple) was not observed around the bead (0/20 each condition, in four independent experiments with skin samples derived from four different litters.) (B) section radioactive in situ hybridization (0/5 each condition in two independent experiments with skin samples from two different litters), and (C) section in situ hybridization (0/5 each condition in two independent experiments with skin samples from two different litters). (D) Cell cycle exit was assessed using FuccimKO reporter allele (representing G0/G1 cell cycle phase) in the 30 µm surrounding the center of the bead (0/10 each condition in two independent experiments with skin samples from two different litters). (E) Quantification of percent total cells surrounding the bead positive for Fucci-mKO. No significant difference was observed between any of the groups. Error bars represent SD. Scale bar = 50 µm. See also Figure 6—figure supplement 2—source data 1 and Figure 6.

The scratch wound healing assay, however, does not distinguish between directional (chemotaxis) and non-directional cell migration (chemokinesis). To assess whether Fgf20 could function as a chemotactic factor, we analyzed migration of growth-arrested E13.5 primary dermal fibroblasts in a transwell assay. When FGF20 was present in the lower chamber only, the number of migrating cells was significantly higher than in control wells (p=0.0003) (Figure 6C). When the FGF20 gradient was abolished by adding FGF20 also to the upper chamber, again a significantly higher number of cells migrated to the lower chamber (p<0.0001), however, there was no difference between the two types of FGF20 treatments (p=0.2256) (Figure 6C). Similar data was obtained when FGF9 was used instead of FGF20 (Figure 6—figure supplement 1). Taken together, these data indicate that Fgf20 induces migration of embryonic dermal fibroblasts in vitro and that this effect is likely chemokinetic.

Next, we wanted to test the impact of Fgf20 in a more physiological setting. To this end, we introduced FGF20 locally via a bead on E13.5 dermis explants to mimic the in vivo situation in which Fgf20 is produced locally in the placode. First, we investigated the activity of FGF20 in this context by assessing its ability to upregulate the expression of Spry4 and Dusp6, two known Fgf pathway feedback inhibitors also differentially expressed in our RNAseq data (Figure 5), using whole-mount RNA in situ hybridization. While we observed a robust induction of both genes after a 3 hr treatment, no consistent responses were detected after 8- and 16 hr treatments (Figure 6H), suggesting that the FGF20 protein loses its activity in intact dermal explants over this period of time. Vehicle-loaded control beads showed no induction of gene expression after any treatment period (Figure 6H). We further analyzed whether FGF20 bead incubation results in upregulation of Sox2, but observed no induction at any time point analyzed (Figure 6H). FGF9 beads led to a prominent induction of Spry4 and Dusp6 after all analyzed treatment periods (Figure 6—figure supplement 1). However, an overnight treatment also led to a robust increase in cell proliferation around the FGF9 bead (Figure 6—figure supplement 1). This response is in contrast to what we observed during dermal condensate formation in vivo (Figure 3) indicating that this experimental set-up may not represent a physiologically relevant model to study DC cell behavior and thus we concentrated on FGF20.

We next used the bead assay to test the impact of FGF20 on fibroblast cell behavior. To do this, we quantified the density of nuclei in E13.5 dermal explants cultured 3 hr with FGF20 or BSA vehicle control beads (Figure 6D,E). We observed a significant, 35% increase in cell density 15 µm around the FGF20 bead compared to the control bead (p=0.002), indicating that a localized Fgf20 source can induce aggregation of mesenchymal cells. We observed a similar increase in cell density upon treatment with FGF9 bead (p=0.033) (Figure 6—figure supplement 1). Nuclear shape analysis showed that cells in the immediate vicinity of the FGF20 bead displayed a significant decrease in nuclear sphericity compared to control bead (p<0.0001) (Figure 6F,G), similarly to DC cells in vivo (Figure 1G,H). We also tested whether cell cycle exit was induced upon local addition of FGF20. We could not detect Cdkn1a induction and no significant increase in Fucci-mKO+ cells were observed around the bead (Figure 6—figure supplement 2). Together this data suggests that Fgf20 can induce some of the cellular changes observed during DC morphogenesis. Finally, we analyzed whether ectopic expression of Fgf20 could also lead to condensation of the mesenchyme in the K14-Edar model. We did not detect any significant difference in the cell density in the upper dermis between control, K14-Edar, and K14-Edar;Fgf20-/- genotypes (p>0.115) (Figure 5—figure supplement 1). However, given that Cdkn1a was expressed throughout the upper dermis in K14-Edar embryos, a lack of condensation in this model could be due to a lack of supply of cells available to condense.

### Inhibition of Fgf signaling impairs both recruitment and maintenance of DC cells ex vivo

The Fgf20-/- mouse model lacks all molecular and cellular signs of DC formation (Huh et al., 2013) (Figure 1A,B) and therefore offers limited tools to assess the effect of Fgf20 on cellular mechanisms governing DC formation. Therefore, we decided to inhibit Fgf signaling using SU5402 ex vivo which allows precise temporal manipulation of pathway activity followed by DC analysis in 3D. The same concentration of SU5402 that blocked the ability of Fgf20 to induce migration of E13.5 fibroblasts (Figure 6), also fully suppressed DC formation when applied to E13.5 skin cultured for 24 hr (Figure 7—figure supplement 1). Yet, it led to the expansion of Fgf20β-Gal knock-in allele expression into a stripe-like pattern (Figure 7—figure supplement 1), as also observed in E14.5 Fgf20-/- embryos in vivo (Huh et al., 2013) confirming the applicability of this approach. SU5402 can also inhibit VEGFR and thus we used an inhibitor more specific to VEGFR, XL184, to test the effects of VEGFR-inhibition on DC formation. We added XL184 at an equivalent dose to inhibit VEGFR as 20 µM SU5402 (Figure 7—figure supplement 2 and Figure 7—figure supplement 2—source data 1) as well as at five-times higher concentration and observed normal DC formation (Figure 7—figure supplement 2D,E). Finally, we confirmed that the absence of DCs in the SU5402-treated samples was due to inhibition of FGFR-signaling by using BGJ398, an inhibitor more specific to FGFR (Figure 7—figure supplement 2). An equivalent dose to inhibit FGFR as 20 µM SU5402 and a 2.5-times higher dose blocked formation of the DCs in the skins and altered the Fgf20β-Gal knock-in allele expression similar to the Fgf20-/- animals (Figure 7—figure supplement 2), confirming the effects of the SU5402 to be due to FGFR-inhibition.

Next, we applied SU5402 slightly later, when DC formation had initiated. Skin explants were divided into two halves: one was used as the control and the other one treated with SU5402 (Figure 7A and Figure 7—figure supplement 1). At this stage, the inhibitor did not result in absence of dermal condensates, but the number of Sox2+ cells was significantly lower in the SU5402-treated samples compared to the controls (p=0.0061) (Figure 7B), indicating that Fgf signaling is necessary for further addition of Sox2+ cells. Analysis of the average distances of DC cells to their nearest neighbor, however, showed no difference between control and SU5402 treated samples (p=0.7319) (Figure 7C) suggesting that inhibition of Fgf signaling does not affect the density of the existing DC. To assess whether Fgf20 could also play a role in the maintenance of DC cells, we compared dermal condensates at the start (T0) of experiment with condensates after 12 hr SU5402 treatment (Figure 7D and Figure 7—figure supplement 1). A significant reduction in the number of Sox2+ DC cells was observed (p=0.0036) (Figure 7E). Again, Sox2+ DC cell density was not affected by SU5402 treatment (p=0.3010) (Figure 7F). Taken together, these results highlight the role of Fgf signaling both in recruitment and maintenance of DC cells.

![Figure 7.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig7-v2.jpg)

**Figure 7.:** (A) Confocal optical sections of paired E14.25 Fgf20+/- skins explants cultured for 12 hr with SU5402 (20 µM) or DMSO vehicle control. Samples were stained for β-Gal (red) and Sox2 (white). (B) Quantification of Sox2+ DC cell numbers in control and SU5402-treated samples relative to DMSO control (n = 14 DCs each from six skins). (C) Quantification of the distance of Sox2+ DC cells to their nearest neighbor in control and SU5402-treated samples (n = 14 DCs each from six skins). (D) Confocal optical sections of E14.25 paired skin explants either fixed at T0 or cultured 12 hr with SU5402 (20 µM). Samples were stained for β-gal (red) and Sox2 (white). (E, F) Quantification of Sox2+ DC cell numbers and distance to neighbor (n = 11 DCs from four skins). Significance was assessed with Student’s T-test. n.s., not significant; **, p≤0.01. Error bars represent SD. See also Figure 7—source data and Figure 7—figure supplement 1.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A–C) Maximum intensity projections of confocal image stacks of Fgf20+/- skins explants labeled with antibodies against β-gal (red) and Sox2 (white). (A) E13.5 skin explants were halved and cultured for 24 hr in the presence of DMSO vehicle control (left) or 20 µM SU5402 (right) (n = 7 skins). In the DMSO-treated samples, dermal condensates are readily observed (Sox2+ cells), whereas SU5402-treated samples are devoid of Sox2+ cells and display altered epithelial Fgf20 expression. (B) E14.25 Fgf20+/- skins explants were divided into two halves: one was cultured in the presence of DMSO (vehicle control, left) for 12 hr and the other in the presence of 20 µM SU5402 (right) (n = 8 skins). (C) E14.25 Fgf20+/- skins explants were divided into two halves: one was fixed immediately (T0, left) while the other was cultured for 12 hr with 20 µM SU5402 (right) (n = 5 skins). Scale bar = 50 µm. See also Figure 7.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/36468/elife-36468-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** E13.5 Fgf20+/- skins was cultured for 24 hr in the presence of DMSO vehicle control (A) (n = 14 skins), 50 nM and 250 nM XL184 to inhibit VEGFR signaling (B,C) (n = 7 and 13 skins, respectively), as well as 0.6 µM and 1.5 µM BGJ398 (D,E) (n = 11 and 12 skins, respectively). First image column shows representative maximum intensity projections of 10x confocal stacks (scale bar = 50 µM) and the second and third columns show representative 63x confocal optical sections of single DCs as top and side views (scale bar = 10 µM). See also Figure 7—figure supplement 2—source data 1..

## Discussion

Mesenchymal (dermal) condensation is a common phenomenon occurring during organogenesis including most ectodermal appendages such as tooth, mammary gland, feather, and hair follicle (Biggs and Mikkola, 2014). Despite the critical role of dermal condensation for organ development, the underlying mechanisms have remained elusive (Hall and Miyake, 2000; Widelitz and Chuong, 1999; Newman and Bhat, 2007; da Rocha-Azevedo and Grinnell, 2013). Here, we have used 3D and 4D imaging to study DC morphogenesis in murine pelage primary hair follicles. The data presented here support two key conclusions. First, our findings show that early morphogenesis of the HF DC is characterized by cell shape changes, exit of the cell cycle, and directed migration. Second, our data indicate that Fgf20 regulates these processes, further corroborating the critical role of Fgf20 in HF dermal condensation. Our results reveal ~2-fold higher cell density in the DC compared to the interfollicular dermis. Ablation of Fgf20 results in the absence of all the DC markers analyzed thus far (Huh et al., 2013), and here, we show by 3D analysis that the cells below the primary placode show no evidence of condensation. These data confirm that DC marker expression and fibroblast condensation are closely associated, although whether DC fate and condensation can be uncoupled remains unclear. Furthermore, this finding supports our previous conclusions (Huh et al., 2013) that hair follicle patterning is governed by and first arises in the epithelium rather than the mesenchyme.

### DC does not form from a pre-existing pool of Sox2+ cells

The origin of the DC/DP population is poorly understood. Tissue recombination and mouse mutant studies (reviewed in [Biggs and Mikkola, 2014; Morgan, 2014]) together with the ex vivo Fgf inhibitor experiments (this study) show that early DC fate is plastic and reversible. Yet, these findings do not preclude the existence of a predetermined pool of DC cells. Previous studies have shown that DPs of the dorsum largely derive from the early fibroblast precursor population marked by expression of Delta-like homologue 1 (Dlk1) (Driskell et al., 2013), and are polyclonal in origin (Collins et al., 2012). Dlk1 lineage tracing from E12.5 (when all dermal fibroblasts are Dlk1+), but not after E16.5, reveal a contribution to post-natal DP (Driskell et al., 2013). Lineage tracing of neural crest cells with Wnt1-Cre or Ht-PA-Cre reveals that the whisker DP (along with non-DC head/facial fibroblasts) is neural crest-derived, but that neural crest cells or their progeny are rare in back skin DP (Fernandes et al., 2004; Wong et al., 2006). Our short-term lineage-tracing experiments show that Sox2 expression is de novo acquired in DC cells, confirming that the dorsal DCs do not arise from a pre-existing pool of Sox2+ cells, for example the neural crest-derived Schwann cell lineage of the skin (Adameyko et al., 2012; Sennett et al., 2015). Studies in an adult model of ectopic hair follicles via forced epithelial β-catenin also argue against a pre-specified DC/DP subpopulation of dermal fibroblasts (Collins et al., 2012). Hence, all available data suggest that the unique attributes of DC/DP cells do not reflect a distinct fibroblast lineage but are induced by placode-derived signals.

### Cell shape change and cell cycle exit are early hallmarks of HF dermal condensation

We show in 3D that HF DCs exhibit a less spherical shape in vivo, and that this shape change is an early event during DC morphogenesis. Previous studies in other organs (bone, tooth, feather) have also revealed an altered cell shape in condensed mesenchyme when compared to the adjacent non-condensed tissue (Thorogood and Hinchliffe, 1975; Ray and Chapman, 2015; Mammoto et al., 2011; Wessells, 1965). However, these analyses were conducted in 2D and thus their similarity or difference with the HF DC is not apparent. What is of note is that the cells within condensed mesenchyme display a distinct morphology. Indeed, a critical role for actomyosin contractility has been proposed to drive cytoskeletal rearrangements, and that the resulting cell shape changes are required for mesenchymal condensation (Ray and Chapman, 2015). Here, we show that in the hair follicle DC the intensity of F-actin is increased in the DC compared to the surrounding mesenchyme, likely playing a critical role in maintaining cell shape. We show that in hair follicle DC, the cell shape changes depend on and can be induced by Fgf20. The utility of this cell shape change along with cell compaction could be manifold, including increased cell-cell contacts to foster cell-cell communication and further to maintain the structure of the DC. Transcriptomic analysis has indicated the expression of cell-cell adhesion factor R-cadherin and cadherin11 (encoded by Cdh4 and Cdh11, respectively) in the DC (Sennett et al., 2015) and cadherin-based junctions were detected between DP cells at E17 (Nanba et al., 2003), but their functional importance for condensation remains to be tested.

During DC morphogenesis, Sox2+ cells were found to exhibit a rapid exit from the cell cycle and maintain the G0/G1 status through E15.5, a finding in line with a previous study showing that morphologically distinct DC cells fail to incorporate H3-thymidine (Wessells and Roessner, 1965). Even as the size of the DC is increased by genetic means (K14-Eda), the DC cells remain quiescent supporting the idea that the increase in DC cell number is not a result of proliferation. Further, mitotic inactivity is a prominent feature of the mature HF DP (Pierard and de la Brassinne, 1975). During the growth (anagen) and rest (telogen) phases of the hair cycle, however, the DP dynamically increases and decreases in cell number. Yet, the increase in DP cell number upon reentering anagen phase does not arise via proliferation but instead DP cells are recruited from the proximal dermal sheath cells (Tobin et al., 2003; McElwee et al., 2003; Chi et al., 2010). Furthermore, hair reconstitution experiments show that mitotically inhibited cells are fully competent to generate the DP (Collins et al., 2012) indicating that proliferation is not necessary for DC/DP formation.

We have previously shown that expression of Cdkn1a is an early marker of DCs (Huh et al., 2013), and recent transcriptome profiling study showed that Cdkn1c (a.k.a. p57), another cyclin dependent kinase inhibitor, is also expressed at high levels in the DC (Sennett et al., 2015). Interestingly, Fgf20 target transcriptome analysis displayed upregulation of cell-cycle-related genes, such as Cdkn1a and Bcl6, which suggests that Fgf signaling could provide the cue for the G0-arrest observed in the DC fibroblasts. Despite this, FGF20 was unable to induce cell cycle arrest in the dermis in a short-term experiment when supplied in a localized manner. However, Cdkn1a was ectopically expressed in our model of Fgf20 overexpression (K14-Edar) in an Fgf20-dependent manner. Similarly, Fgf signaling induces Cdkn1a-mediated cell cycle arrest in chondrocytes (Aikawa et al., 2001) and further, ectopic Fgf20 induces growth arrest of rat chondrosarcoma cells in vitro (Buchtova et al., 2015). Bcl6 is also a DC signature gene (Sennett et al., 2015) and although its function is context-dependent, it has been shown to suppress proliferation of many primary cells including fibroblasts (Ranuncolo et al., 2008).

### Directed cell migration drives dermal condensate morphogenesis

Our confocal time-lapse imaging of developing HF revealed that dermal fibroblasts initially outside of the future condensate migrate toward the placode, indicating directed migration as a mechanism of DC formation. A recent study tracking movements of Wnt-responsive cells using TCF/Lef::H2B-GFP reporter (Glover et al., 2017) is consistent with our findings. In vitro scratch wound assay revealed that Fgf20 enhances cell motility. Although transwell assays did not support a chemotactic role for Fgf20, we showed that local delivery of FGF20 via beads on dermal explants induces an increase in cell density, suggesting that Fgf20 induces directed migration and in a tissue context, dermal condensation. Further, we find that inhibition of Fgfr signaling ex vivo blocks accumulation of Sox2+ fibroblasts in the DC while Fgf20 does not appear to directly regulate Sox2 expression. These data support the conclusion that Fgf20 signaling regulates directed movement of dermal fibroblasts. An additional factor that we did not test but may play a role in DC morphogenesis is the contribution of differential ECM composition surrounding the hair follicle (Kaplan and Holbrook, 1994; Pflieger et al., 2006). It is possible that Fgf20 induces migration of fibroblasts and simultaneously, differential ECM composition around the hair follicle holds the DC cells in place.

Previous studies have shown that Fgf signaling induces migration, both chemotactic and chemokinetic, in several different developmental contexts (Mammoto et al., 2011; Delfini et al., 2005; Attia et al., 2012). Indeed, a general role for Fgf signaling in regulating dermal condensation via cell migration is an appealing idea. Our ex vivo manipulation experiments showed that inhibition of Fgfr signaling suppresses accumulation of new Sox2+ cells, but also compromises maintenance of nascent DC. The latter finding is suggestive for a role also in DC maintenance. In odontogenic mesenchyme, attractive Fgf8 and repellent Sema3f are thought to act in concert to induce migration-driven cell compaction (Mammoto et al., 2011). Involvement of Fgf signaling in mammary mesenchyme condensation is an intriguing hypothesis, but has not been examined. Fgf20 is expressed in the epithelium of the mammary buds during the period of mesenchymal condensation (Elo et al., 2017) yet it seems to be dispensable for this process, but other epithelially expressed Fgfs may compensate for the loss of Fgf20. In contrast, Fgf20 is necessary for feather development (Houghton et al., 2007; Wells et al., 2012). Although the exact function of Fgf20 in feather morphogenesis has not been studied, the ability of exogenous Fgfs to induce dermal cell aggregation ex vivo (Lin et al., 2009; Song et al., 2004) and to elicit feather formation in Fgf20-deficient skin explants (Song and Sawyer, 1996) argue for a conserved role for Fgf20 in DC induction.

### Fgf20 signaling induces partial DC fate

Although the transcriptional profile of the DC has been described (Sennett et al., 2015), the molecular regulation of DC fate acquisition is not well understood. Fgf20 is necessary for DC marker expression (Huh et al., 2013) and here we show that Fgf20 is also necessary for dermal cell condensation. However, our RNAseq profiling of genes induced in the dermis upon short Fgf20 treatment revealed only a few DC signature genes (Sennett et al., 2015), and for example Sox2, was not upregulated by Fgf20 ex vivo, nor in our in vivo over-expression model of ectopic Fgf20 signaling. These data suggest that Fgf20 alone is sufficient to induce only a subset of DC markers. It is possible that other cues, molecular or mechanical, together with Fgf20 determine DC fate, and studies in dental and cartilage mesenchyme show that cellular condensation contributes to fate acquisition (Mammoto et al., 2015; Mammoto et al., 2011; Ray and Chapman, 2015). Alternatively, it is possible that Fgf20 functions mainly to regulate cell behaviors rather than fate.

In conclusion, we show here that cell shape change, cell cycle exit and directed migration define HF DC formation. While altered cell shape and directed mesenchymal cell movement may be a shared characteristic, cell cycle exit appears to be a hair follicle specific feature, as cells within the condensing mammary (Lee et al., 2011) and tooth mesenchyme exhibit proliferation (Mammoto et al., 2011) at the same rate as the surrounding non-condensed mesenchyme. However, the function of DC cell cycle exit in hair follicle morphogenesis remains unknown. It appears not to be sufficient to induce DC fate, but it remains open whether it is necessary. To date, culturing methods for maintaining the hair-follicle inductive capacity of DC/DP remain elusive, and after a few passages, DP populations completely lose their inductive abilities. Although speculative, the obligate proliferation under in vitro culture may compromise DC fate maintenance. The challenge in future therapeutic efforts to generate hair inductive fibroblasts is to uncover culture conditions that induce DC cell fate de novo.

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
      <td>Strain, strain background (Mus musculus, C57/Bl6)</td>
      <td>Fgf20+/-</td>
      <td>PMID: 23431057</td>
      <td>RRID:MGI:5425887</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>Fgf20-/-</td>
      <td>PMID: 23431057</td>
      <td>RRID:MGI:5425887</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>K14-Eda</td>
      <td>PMID: 12812793</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>R26RtdTomato</td>
      <td>Jackson Laboratory</td>
      <td>Stock 007914, RRID:IMSR_JAX:007914</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>R26RmT/mG</td>
      <td>Jackson Laboratory</td>
      <td>Stock 007576, RRID:IMSR_JAX:007576</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>Sox2creERT</td>
      <td>Jackson Laboratory</td>
      <td>Stock 017593, RRID:IMSR_JAX:017593</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, mixed)</td>
      <td>Fucci</td>
      <td>PMID: 18267078</td>
      <td>RRID:IMSR_RBRC02892</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>R26Fucci2aR</td>
      <td>EMMA</td>
      <td>EM:08395, RRID:IMSR_EM:08395</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>Sox2-GFP</td>
      <td>PMID: 12923297</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57/Bl6)</td>
      <td>K14-Edar</td>
      <td>PMID: 15366021</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Beta-galactosidase rabbit</td>
      <td>MP Biomedicals</td>
      <td>0855976, RRID:AB_2334934</td>
      <td>1:1500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Beta-galactosidase chicken</td>
      <td>Abcam</td>
      <td>ab9361, RRID:AB_307210</td>
      <td>1:1500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>EpCAM rat monoclonal</td>
      <td>BD Pharmingen</td>
      <td>552370, RRID:AB_394370</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Krt14 rabbit monoclonal</td>
      <td>Thermo Fisher Scientific</td>
      <td>RB-9020-P, RRID:AB_149790</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Sox2 goat polyclonal</td>
      <td>Santa Cruz</td>
      <td>SC-17320, RRID:AB_2286684</td>
      <td>1:500 sections, '1:200 wholemount</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Sox2 rabbit polyclonal</td>
      <td>Stemgent</td>
      <td>09–0024, RRID:AB_2195775</td>
      <td>1:300</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Cdkn1a rabbit monoclonal</td>
      <td>Abcam</td>
      <td>ab188224, RRID:AB_2734729</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Dusp6 RNA probe</td>
      <td>PMID: 11960712</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cdkn1a RNA probe</td>
      <td>PMID: 9486790</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Spry4 RNA probe</td>
      <td>PMID: 11731251</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Sox2 RNA probe</td>
      <td>PMID: 15240551</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Edar RNA probe</td>
      <td>PMID: 11203701</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hprt probe</td>
      <td>BioRad</td>
      <td>qMmuCEP0054164</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Dusp6 probe</td>
      <td>BioRad</td>
      <td>qMmuCIP0029423</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Eef1 probe</td>
      <td>BioRad</td>
      <td>qMmuCEP0057829</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Spred1 probe</td>
      <td>BioRad</td>
      <td>qMmuCEP0055028</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Gapdh probe</td>
      <td>BioRad</td>
      <td>qMmuCEP0039581</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Etv5 probe</td>
      <td>BioRad</td>
      <td>qMmuCIP0034710</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Spry4 probe</td>
      <td>BioRad</td>
      <td>qMmuCEP0054507</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bcl6 qPCR primers</td>
      <td>this study</td>
      <td>template NM_001348026.1</td>
      <td>F: CGCGAACCTTGATCTCCAGT, R: CAGGGACCTGTTCACGAGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hprt qPCR primers</td>
      <td>this study</td>
      <td>template NM_013556.2</td>
      <td>F: CAGTCCCAGCGTCGTGATTA, R: TCGAGCAAGTCTTTCAGTCCT</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FGF20 human recombinant protein</td>
      <td>PeproTech</td>
      <td>100–41</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FGF9 human recombinant protein</td>
      <td>R and D Systems</td>
      <td>273-F9</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Rneasy plus micro kit</td>
      <td>Qiagen</td>
      <td>ID: 74004</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Quantitect reverse transcription kit</td>
      <td>Qiagen</td>
      <td>ID: 205311</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TruSeq Stranded Total RNA Library Prep Kit with Ribo-Zero Mouse</td>
      <td>illumina</td>
      <td>RS-122–2202</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SU5402</td>
      <td>Calbiochem</td>
      <td>572630</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BGJ398</td>
      <td>Selleckchem.com</td>
      <td>S2183</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>XL184</td>
      <td>Selleckchem.com</td>
      <td>S4001</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>AfterQc</td>
      <td>PMID: 28361673</td>
      <td>RRID:SCR_016390</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SortMeRNA</td>
      <td>PMID: 23071270</td>
      <td>RRID:SCR_014402</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR</td>
      <td>PMID: 23104886</td>
      <td>RRID:SCR_015899</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Htseq-count</td>
      <td>PMID: 25260700</td>
      <td>RRID:SCR_011867</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DEseq2</td>
      <td>PMID: 25516281</td>
      <td>RRID:SCR_015687</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Ethics statement

All mouse studies were approved and carried out in accordance with the guidelines of the Finnish national animal experimentation board.

### Mouse lines

The following mice were maintained on C57Bl/6 background. Fgf20β-Gal mice harbor an Fgf20-β-Galactosidase knock-in allele (Huh et al., 2013); Sox2CreER was obtained from Jackson Laboratory (Stock 017593); R26RtdTomato was obtained from Jackson Laboratory (Stock 007914); R26RmT/mG was obtained from Jackson Laboratory (Stock 007576). R26Fucci2aR mice (Mort et al., 2014) were obtained from the European Mouse Mutant Archive (EM:08395) and upon derivation mated with ubiquitous cre line, Pgk1-cre (Jackson Laboratory; Stock 020811) in order to obtain mice which heritably and constitutively express the Fucci2a construct in every cell. Sox2-EGFP, K14-Eda, and K14-Edar have been described (Mustonen et al., 2003; Pispa et al., 2004, D'Amour and Gage, 2003). Fucci cell cycle indicator mice (Sakaue-Sawano et al., 2008) were maintained on a mixed background.

Mice were kept in 12 hr light-dark cycles and food and water were available ad libitum. To label Sox2-expressing cells, pregnant wild-type dams mated with Sox2CreER/wt; R26RtdTomato/tdTomato males were given one intraperitoneal injection of 3 mg tamoxifen (Sigma-Aldrich, Saint Louis, MO) dissolved in corn oil (Sigma-Aldrich) at 12pm on the indicated day of pregnancy (appearance of a vaginal plug was taken as embryonic (E) 0). All embryos used in the study were staged according to limb and other external morphological criteria.

### Transmission electron microscopy

Samples were fixed in 2.5% glutaraldehyde at room temperature for 2 hr, washed in 0.1 M NaPO4, and subsequently fixed in 2% PFA in 0.1 M NaPO4. The samples were then dehydrated through a graded series of ethanol and acetone before embedding in Epon. Ultra-thin sections were generated. Images were acquired with Jeol JEM-1400 electron microscope (Jeol Ltd., Tokyo, Japan).

### In situ hybridization

For whole-mount RNA in situ hybridization, cultured dermal explants were fixed to their filter with cold methanol for 2 min and then fixed in 4% PFA in PBS overnight at 4°C, washed with PBS and then dehydrated in a series of methanol. The hybridization was performed using InSitu Pro robot (Intavis AG, Cologne, Germany) as described before (Fliniaux et al., 2008; Huh et al., 2013). Briefly, the samples were rehydrated in a methanol series, treated with 10 µg/ml Proteinase K (Roche, Mannheim, Germany) for 5 min and post fixed with 4% PFA. The hybridization was performed with digoxigenin-labeled antisense RNA probes: Dusp6 (Dickinson et al., 2002), Cdkn1a (Jernvall et al., 1998), Spry4 (Zhang et al., 2001), and Sox2 (Ferri et al., 2004), 1 µg/ml in hybridization buffer at 65°C for 14 hr. After hybridization, the excess probe was removed in stringent washes, samples were blocked, the probe was detected with an alkaline phosphatase conjugated anti-digoxigenin antibody (Roche, Mannheim, Germany), and a subsequent reaction with precipitating alkaline phosphatase substrate BM purple (Roche, Mannheim, Germany). Samples were fixed with 4% PFA and imaged using Lumar.V12 stereomicroscope with 1.2x objective and AxioCam ICc camera (Zeiss, Oberkochen, Germany).

For radioactive section in situ hybridization, E16.5 embryos were collected, fixed in 4% PFA in PBS and processed into paraffin blocks using standard protocols and cut into 5 µm sagittal sections. Radioactive in situ hybridization with 35S-UTP-labeled probes: Edar (Laurikkala et al., 2001), Sox2 (Ferri et al., 2004), and Cdkn1a (Jernvall et al., 1998), was performed as previously described (Huh et al., 2013). Sections were imaged using Axio Imager M.2 widefield microscope equipped with Plan-Neofluar 20x/0.5 objective and AxioCam HRc camera (Zeiss) using bright and dark field microscopy. The dark field images were inverted, thresholded linearly and superimposed on the bright field images using Adobe Photoshop software (Adobe, San Jose, CA).

### X-gal staining

Fgf20β-Gal/+ embryos were pre-fixed for 2 hr in 2% PFA, 0.2% glutaraldehyde (Sigma-Aldrich, St. Louis, MO) in PBS, 4°C and then rinsed with PBS and washed 3 × 15 min with PBS, 2 mM MgCl2 (Merck, Darmstadt, Germany), 0.02% NP-40 (Sigma-Aldrich), 4°C. Subsequently, the samples were stained for 10 hr at RT, in dark with 1 mg/ml X-Gal (Thermo Fischer Scientific, Vilnius, Lithuania), 5 mM K3Fe(CN)6 (Merck, Darmstadt, Germany), 5 mM K4Fe(CN)6 (Merck, Darmstadt, Germany), 2 mM MgCl2, 0.1 % NP-40 (Calbiochem, San Diego, CA), 0.2% Na-deoxycholate (Sigma-Aldrich, St. Louis, MO) in PBS. The embryos were washed 3 × 10 min with PBS and fixed with 4% PFA in PBS at RT. After imaging, the samples were processed for paraffin blocks using standard protocols and sectioned into 5 µm sagittal sections. The sections were deparaffinized and counter stained with Nuclear Fast Red (Sigma-Aldrich, Steinheim, Germany) for 5 min, dehydrated and mounted. The sections were imaged using Axio Imager M.2 wide field microscope equipped with Plan-Neofluar 10X/0.3 objective and AxioCam HRc camera (Zeiss).

### In vitro fibroblast scratch wound healing assay, and transwell migration assay

Primary dermal fibroblasts were extracted from E13.5 wild-type NMRI mouse embryos. Briefly, the back skin was dissected and treated with 2.5 mg/ml Pancreatin (Sigma-Aldrich), 22.5 mg/ml Trypsin (Difco, Sparks, MD) in Tyrode’s solution for 8 min at RT, followed by an incubation with 10% FBS in DMEM (Gibco by Life Technologies, Paisley, UK) for 1 hr at RT. The tissues were manually separated; epidermis was discarded and the mesenchyme was gently dissociated by pipetting in 0.2% FBS in DMEM. For scratch wound healing assay, the fibroblasts were seeded on fibronectin-coated plates (1 µg/cm2, R and D Systems, Minneapolis, MN) at the density of 125,000 /cm2 and cultured for 16 hr in 0.2% FBS, 1% penicillin-streptomycin (Life Technologies, Eugene, OR) in DMEM. Cell cycle inhibition was achieved by a 2 hr treatment with 5 ng/ml aphidicolin (Sigma-Aldrich, Jerusalem, Israel). Scratches were induced with a pipette tip and the cells were treated with human recombinant FGF20 (200 ng/ml, Peprotech, Rocky Hill, NJ), human recombinant FGF9 (200 ng/ml, R and D Systems), SU5402 (20 µM, Calbiochem, Darmstadt, Germany) or BSA (0.1%). 4 µg/ml heparin (Sigma-Aldrich, St. Louis, MO) was added with the FGF proteins. Conditions were carried out in duplicate in five independent experiments. Wounds were imaged at 0, 4, 8, and 24 hr using Leica DM IRB phase contrast microscope (Leica Microsystems), and ImageJ (http://rsbweb.nih.gov/ij/) was used to manually measure the open area at the indicated time points in two locations. Proportion of closure was determined as the ratio of open area at each time point compared to 0 hr. For transwell migration assay, 50,000 freshly isolated cells were seeded in 300 µl of DMEM, 1% FBS in cell culture inserts for 24-well plates (Millicell, Basel, Switzerland) and cultured overnight. The cells were then treated with 200 ng/ml FGF20, FGF9 or 0.1% BSA vehicle control (baseline) in DMEM containing 1% FBS and 5 ng/ml aphidicolin; conditions were carried out in duplicate in six independent experiments. The proteins were introduced either in the receiving compartment or both receiving and seeding compartments and cells were allowed to migrate for 8 hr. The seeding compartment side of the membrane was mechanically cleared of cells; the remaining cells were fixed with methanol 5 min, and the membrane was stained with 0.1% Crystal violet (Sigma-Aldrich, St. Louis, MO), 70% ethanol in RO-water. Absolute cell number was counted at five positions on each membrane. Relative migration was determined as the average number of cells in the duplicate inserts divided by average number of cells in the duplicate inserts.

### Hanging drop culture, RNA sequencing, and qRT-PCR

E13.5 skins were dissected from Fgf20-/- embryos and enzymatically separated using 2.5 U/ml Dispase II (Roche by Godo Shusei, Tokyo, Japan) in 4°C and 30 min resting in culture medium, followed by mechanical separation. Each dermis was cut into two halves along the midline and one half was incubated in FGF20 (1 µg/ml) and the other half was incubated in 0.1% BSA vehicle control in 0.1% FBS, heparin (2 µg/ml), 1% penicillin-streptomycin in DMEM. The tissues were incubated in hanging drops of the indicated media for 3 hr at 37°C, 5% CO2. For RNAseq, five biological replicates were used. The samples were stored in RNAlater (Qiagen GmbH, Hilden, Germany). RNA was extracted using RNeasy Plus micro kit (Qiagen GmbH, Hilden, Germany), according to manufacturer’s instructions. RNA quality was assessed with 2100 Bioanalyzer (Agilent, Santa Clara, CA) and RIN values averaged 9.6. The cDNA libraries were prepared with TruSeq Stranded Total RNA with RiboZero (Illumina, San Diego, CA), and sequenced with NextSeq500 (Illumina, San Diego, CA). The Illumina-seq reads produced around 35 million reads for each sample. The quality of each sample was assessed with FastQC and processed with AfterQC (Chen et al., 2017). The ribosomal RNAs were filtered out with SortMeRNA (Kopylova et al., 2012). Thereafter the reads that passed the QC threshold were mapped to mouse genome (GRCm38/mm10/Ensembl release 79 - March 2015) using STAR mapping tool (Dobin et al., 2013) and on average 81% reads uniquely mapped. The expression of genes and differentially expressed genes (adjusted p value<0.05) were measured by HTseq-count (Anders et al., 2015) and DEseq2 (Love et al., 2014). Access to the data set is found at https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE110459.

For qRT-PCR, 1 µg of RNA was used for cDNA synthesis with the QuantiTect Reverse Transcription Kit (Qiagen), according to manufacturer’s instructions. cDNA was diluted to 10 ng/µl and 40 ng was used for one qPCR reaction. Probe-based multiplex RT-qPCR reactions were prepared in 1X iTaq Universal Probes Supermix (Bio-Rad, Hercules, CA) using a validated combination of gene-specific PrimePCR Probe Assays (Bio-Rad, Hercules, CA) in a 20 µl volume. The probe combinations are listed in Supplementary file 1. Reactions from all samples were run in triplicate wells with the CFX96 Real-Time System (Bio-Rad, Hercules, CA) using the following cycling protocol: Initial denaturation 3 min at 95°C, followed by 45 cycles of denaturation 10 s at 95°C and annealing/extension 50 s at 60°C. Fold changes were calculated with the ∆∆CT method (Livak and Schmittgen, 2001). These were normalized to reference genes as follows: Etv5 and Spry4 were normalized to Gapdh, Cdkn1a and Dusp6 were normalized to Hprt, and Spred1 was normalized to Eef. Primer-based RT-qPCR reactions were prepared in Fast SYBR Green Master Mix (Thermo Fisher Scientific). Bcl6 qPCR primers were designed using template NM_001348026.1, Forward primer: CGCGAACCTTGATCTCCAGT, Reverse primer: CAGGGACCTGTTCACGAGAT. Hprt qPCR primers were designed using template NM_013556.2, Forward primer: CAGTCCCAGCGTCGTGATTA, Reverse primer: TCGAGCAAGTCTTTCAGTCCT

### Whole skin explant culture

Embryonic back skin was dissected from E13.0 - E14.25 embryos as indicated and cultured in a Trowell-type tissue culture setup (liquid-air interface) as previously described (Närhi and Thesleff, 2010). For dermis cultures, back skins were obtained after treatment with Pancreatin-Trypsin or Dispase II as described above. The culture medium (DMEM, 1X Glutamax, 10% FBS, 1% penicillin-streptomycin) was supplemented where indicated with 20 µM SU5402 (Calbiochem), 600 nM or 1.5 µM BGJ398 (Selleckchem.com, Houston, TX), 50 nM or 250 nM XL184 (Selleckchem.com, Houston, TX), or with 0.1% DMSO only. Explants were fixed in 4% PFA for immunostaining (see below).

### FGF bead treatment of embryonic dermises

Heparin-agarose beads (Ø=70–100 µm, MCLAB, San Francisco, CA) were loaded with 100 µg/ml FGF9 or FGF20 or 0.1% BSA for 2 hr at room temperature and subsequently washed with PBS. Dermises from E13.0–13.5 wild-type NMRI embryos were pooled for gene expression analysis, cell shape, and EdU incorporation assay. Dermises from E13.0 – E13.5 Fgf20-/- embryos were used in pairs for density analysis to compare treatment with control.

### EdU incorporation

To label proliferating cells, pregnant dams mated with Fgf20-/- males were given one intraperitoneal injection of 25 mg/kg body weight EdU (Life Technologies, Eugene, OR) dissolved in saline 2 hr prior to sacrifice. To label cultured dermises,NMRI E13.5 dermises cultured with FGF20- or FGF9-loaded beads for 18 hr as described above. During the last 2 hr, 10 µM EdU (Life Technologies, Eugene, OR) was introduced in the medium. The samples were then fixed with 4% PFA and EdU detection was performed with Click-iT kit (Life Technologies, Eugene, OR) according to manufacturer’s protocol. Briefly, samples were permeabilized with 3% BSA, 0.5% Triton X-100 (MP Biomedicals, Solon, OH) for 1 hr, stained with Click-iT reaction cocktail containing Alexa488-azide for 2 hr protected from light, washed thoroughly for 2 hr with PBS and mounted in Vectashield and imaged using Lumar.V12 stereomicroscope with 1.2x objective and AxioCam ICc camera (all Zeiss).

### Immunostaining and whole mount confocal microscopy

The following antibodies and reagents were used: Sox2 (goat polyclonal, Santa Cruz, SC-17320, Dallas, TX) 1:500 for sections and 1:200 for whole-mounts, Sox2 (rabbit polyclonal, Stemgent, 09–0024, Glasgow, UK) 1:300 for whole-mounts, β-galactosidase (β-gal, rabbit polyclonal, MP Biomedicals, 55976, Solon, OH) 1:1500, β-galactosidase (β-gal, chicken polyclonal, Abcam, ab9361, Cambridge, UK) 1:1500, EpCAM (rat monoclonal, BD Pharmingen, 552370, San Diego, CA) 1:500, Keratin 14 (rabbit monoclonal, Thermo Fisher Scientific, RB-9020-P, Runcorn, UK) 1:500, and Cdkn1a (rabbit monoclonal, Abcam, ab188224, Cambridge, UK) 1:1000. Alexa 488, 568, or 647-conjugated secondary antibodies (Life Technologies) were used at 1:500 for sections and 1:400 for whole-mount samples for staining. For labeling of multiple antigens, the primary antibodies and secondary antibodies were incubated simultaneously.

For immunostaining tissue sections, microscope slides were deparaffinized and washed with PBS for 10 min. Antigen retrieval was performed by incubation with 10 mM Na-citrate acid at 100°C for 10 min and the sections were allowed to cool to room temperature slowly. For fluorescent labeling, sections were permeabilized with 0.1% Triton X-100, 10 min and blocked with 10% normal donkey serum, 0.1% Triton X-100 for 30 min. The sections were stained with primary antibodies overnight at 4°C and washed with PBS at room temperature. Slides were incubated with Alexa Fluor-conjugated secondary antibodies at room temperature for 2 hr, washed with PBS, and mounted with Vectashield containing DAPI (Vector Laboratories, Burlingame, CA). For immunohistochemical labeling, slides were stained using BrightVision Poly-HRP-AntiRB-kit (DVPR110HRP, ImmunoLogic, Duiven, The Netherlands) according to manufacturer’s instructions. Briefly, slides were blocked using Pre-Antibody Blocking solution, 5 min, RT and washed with PBS. Then primary antibody was diluted in Pre-Antibody Blocking and the slides were stained overnight, 4°C, before washing with PBS. The slides were then stained with secondary goat, anti-rabbit-Poly-HRP antibody 30 min, RT and washed with PBS. The slides were then treated with DAB-solution (BS04-110, ImmunoLogic, Duiven, The Netherlands) according to maunfacturer’s instructions, 8 min, RT, washed in de-ionized water, and mounted with ImmuMount (ThermoScientific, Kalamazoo, MI). Images were acquired with Axio Imager M.2 microscope equipped with Plan-Neofluar 20x/0.5 objective and AxioCam HRc.

For whole-mount confocal microscopy, embryonic skin was spread onto 0.1 µm nucleopore filters and fixed for 2 hr at room temperature. Tissues were washed in large volumes of PBS and subsequently blocked in 10% normal donkey serum, 0.4% Triton X-100 for 1 hr, 4°C. Blocking solution was changed directly for primary antibody incubation in blocking solution 12–48 hr. The samples were washed in several changes of large volumes of PBS over 6–24 hr. Secondary antibody and Hoechst33342 (Life Technologies, Eugene, OR) were incubated for 6–24 hr, followed by washing. In the case of Fucci reporter samples and cell shape analysis of DC and IF cells, given the differential localization of Sox2 (nuclear) and Fgf20-β-Gal (cytosolic, epithelial) we used the same secondary Alexa fluor in order to reduce imaging time. Otherwise, different fluorophores were used. Optical sections of skin were obtained using Leica TCS SP5 confocal microscope equipped with HCX APO 63x/1.30 glycerol-immersion objective (Leica, Wetzlar, Germany) at 0.5 µm intervals for bead-treated dermis and for confocal imaging of in vivo cell shape analysis using Zeiss LSM 780 confocal microscope equipped with 63x/1.40 Plan-Apochromat oil-immersion objective at 0.5 µm intervals. Otherwise, images were acquired using an upright laser scanning confocal microscope LSM700 Axio Imager.M2 (Zeiss) using LCI Plan-Neofluar 63x/1.30 glycerol-immersion objective at 0.4–0.5 µm intervals and using Plan-Apochromat 10X/0.45 air objective at 0.8 µm intervals.

### Image analysis

Z-stacks were analyzed in 3D using Imaris software (Bitplane, Zurich, Switzerland), unless stated otherwise. To analyze the number of Sox2-positive cells, co-localization of Fucci and R26R-tomato reporters and their distances to each other and the placode, surfaces of Sox2 nuclei were generated based on Sox2 immunostaining using local intensity measures. The parameters were as follows: surface level detail 0.5 µm, local contrast background subtraction (seed point diameter 4.25 µm). In the analyses of interfollicular cells, sub-placodal cells of the Fgf20-/- skin, and the quantification of cell shapes, Hoechst 33342 staining was exploited for surface rendering as above (surface level detail 0.6 µm, local background subtraction (seed point diameter 5 µm). To generate surfaces based on cytoplasmic GFP in Sox2-GFP cells, surface detail was 0.6 µm with local background substraction (seed point diameter 8 µm). All nuclear surfaces were manually corrected. In all analyses, center of nuclear surface was used as a marker for cell position. For reporter studies, average intensity of the reporter channel within Sox2 or Hoechst 33342 surfaces was used as a measure for a cell’s reporter activity. A cut-off value was manually determined, where a cell could be distinctly identified as reporter positive. To determine the distance from placode, a placodal surface was created as above, with surface level detail of 1.5 µm.

In description of DC morphogenesis and analysis of Fgfr inhibition on DC cells, number of Sox2+ cells and their distances from the placode were determined from Fgf20+/- and Fgf20-/- skin samples immunostained for β-gal and Sox2. Cell density of the DC was determined from Sox2-EGFP;Fgf20+/- as the number of Sox2+ surfaces inside the area distinguished by Sox2-EGFP reporter surface (created as above), the density of the interfollicular cells and sub-placodal cells of the Fgf20-/- samples was determined as the number of Hoechst33342 surfaces within a corresponding volume of the interfollicular tissue. Density of sub-placodal dermal cells of the Fgf20-/- skin was determined as the number of Hoechst33342 surfaces underneath a manually adjusted region of interest underlying the placode (β-gal). F-actin intensities in the DC and in the interfollicular dermis were determined from Fgf20+/- skins mount skin samples stained with A568-phalloidin (LifeTechnologies, Eugene, OR) and antibodies against Sox2 and β-gal. A surface was drawn around the Sox2-positive cells beneath placode marked by β-gal and copied to a Sox2-negative interfollicular area of the dermis at approximately the same depth to measure the mean intensity of A568-phalloidin staining. F-actin intensity in DC Sox2-positive cells and non-DC Sox2-positive cells in relation to Sox2-negative dermal fibroblasts was determined from E13.75 Sox2-EGFP;Fgf20+/- back skin samples stained with A568-phalloidin and β-gal antibody. Sox2-GFP surfaces demarcating individual cells were classified as DC or non-DC based on the proximity to the placode and mean F-actin intensities inside the surfaces measured. Dermal fibroblast surfaces were drawn based on phalloidin-staining at locations close to the non-DC Sox2-GFP cells. Distance of Sox2+ surfaces to placode, were measured as the shortest distance to β-gal surface. Distance to nearest neighbor was determined based on Sox2 surface center coordinated using R software and nabor package (version 0.4.7) and median distances of each cell group within each placode were analyzed using Mann-Whitney test. For lineage tracing analysis, Sox2CreERT/+;R26RtdTomato/+;Fgf20+/- skin immunostained for Sox2 and β-gal were used. DC cell number, tdTomato positivity and position were determined by Sox2 surfaces as described above. Distance to placode was determined as the distance to a manually designated point on the center of placode surface and the identity of the nearest neighbor was determined based on Sox2 surface coordinates using R software with nabor package (version 0.4.7). For cell cycle analysis, confocal stacks of Fgf20+/-;Fucci reporter skins immunostained for Sox2 and β-gal were used. Sox2 surfaces were used for DC cells and Hoechst33342 surfaces were used for interfollicular cells of Fgf20+/- skin and sub-placodal cells of the Fgf20-/- skin. Reporter positivity was determined as above.

DC and IF nuclear shapes were determined from Hoechst33342 staining using Imaris software sphericity measurement. Non-adjacent cells were selected for analysis in order to avoid bias introduction from manual surface editing. IF control cells were selected at ~70 µm distance from condensate center. Cell shape was also determined using Fgf20+/-;R26RmTmG skins immunostained for Sox2 and β-gal. Cell shapes were analyzed with ImageJ software based on membrane-bound tdTomato signal with rolling ball background subtraction (5 µm diameter), 3D Gaussian filtering (0.4 µm diameter) and Gamma correction (0.6 value). The mT-negative region containing the cytoplasm was segmented using the Wand-tracing tool in the Segmentation Editor of Image J. The generated objects were automatically detected with the 3D Objects Counter, exported into the 3D ROI Manager (Ollion et al., 2013) and visualized/animated with the 3D Viewer.

For studies with FGF-loaded beads, Fgf20-/- dermises were used. A region within a 30 µm distance from the bead surface at its midsection was analyzed from confocal stacks for cell density and nuclear shape. Cell density was measured by manual counting from optical sections and nuclear shapes were derived from Hoechst33342 surfaces. Nuclear surfaces of cells surrounding the middle third of the bead height were used for analysis and cells at 0–15 µm and 15–30 µm distances from the bead surface were analyzed.

### Live confocal imaging and image analysis

E13.5 Sox2-EGFP;Fucci-mKO back skins were explanted into Trowell-type culture with DMEM/F12 (no phenol red), 10% FBS, 1% penicillin-streptomycin as previously described (Ahtiainen et al., 2014). Briefly, explants were allowed to recover a minimum of 2 hr after dissection and then imaged with Leica SP5 laser scanning confocal microscope using HC PL APO 10x/0.4 objective and equipped with an incubation chamber (LifeImagingServices) to maintain 5% CO2 humidified atmosphere at 37°C. Confocal image stacks were acquired at 3.25 µm intervals with 10% laser power, 700 Hz scanning speed, and sub-optimal sampling every 20 min to minimize laser-induced damage.

Time-lapse videos were analyzed using Imaris software. Tissue drift was corrected by manually tracing a minimum of seven non-motile cells over time and using the software’s translational drift correction algorithm. Sox2-GFP+ cell movements were manually traced back in time based on Fucci-mKO signal for as long as cell tracking could be reliably done. DC center was determined as the center of the Sox2-GFP signal of the DC. Similar tracking was performed on interfollicular dermal fibroblasts around an arbitrary migration center. Variables of cell movement were as follows:

Velocity = track length/track duration

Net velocity = track displacement length/track duration

Track straightness = displacement length/track length

$$
cos\alpha=\frac{a-b-}{a-∙b-}
$$

where α is the escape angle, $a-$ is cell trajectory, and $b-$ is a vector between cell’s starting position and DC center or migration center for DC and IF cells, respectively.

### Statistical testing

The normality of distributions of data were analyzed using the Shapiro-Wilk test (confidence interval 95%). Normally-distributed data was analyzed using two-tailed Student’s T-test or One-Way Anova, while a non-parametric Mann-Whitney U test was performed to analyze statistical difference of data that failed Shapiro-Wilk test. When data was normalized, a one-sample T-test was performed. χ2-test was used to analyze randomness of cell neighbor distribution in lineage-tracing analysis. Rayleigh’s Z-test was conducted to test normal distribution of cell movement direction, followed by Watson’s U2 test to analyze significance of cell movement direction distributions in live imaging experiments.
