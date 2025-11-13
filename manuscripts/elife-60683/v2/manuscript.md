# Vascular dimorphism ensured by regulated proteoglycan dynamics favors rapid umbilical artery closure at birth

## Authors

- Sumeda Nandadasa<sup>1</sup> ([ORCID: 0000-0002-4954-6376](https://orcid.org/0000-0002-4954-6376))
- Jason M Szafron<sup>2</sup> ([ORCID: 0000-0001-9476-5175](https://orcid.org/0000-0001-9476-5175))
- Vai Pathak<sup>3</sup>
- Sae-Il Murtada<sup>2</sup>
- Caroline M Kraft<sup>1</sup>
- Anna O'Donnell<sup>1</sup>
- Christian Norvik<sup>4</sup>
- Clare Hughes<sup>5</sup> ([ORCID: 0000-0003-4726-5877](https://orcid.org/0000-0003-4726-5877))
- Bruce Caterson<sup>5</sup>
- Miriam S Domowicz<sup>6</sup> ([ORCID: 0000-0001-7860-4427](https://orcid.org/0000-0001-7860-4427))
- Nancy B Schwartz<sup>6</sup>
- Karin Tran-Lundmark<sup>4</sup>
- Martina Veigl<sup>3</sup>
- David Sedwick<sup>7</sup>
- Elliot H Philipson<sup>1</sup>
- Jay D Humphrey<sup>2</sup> ([ORCID: 0000-0003-1011-2025](https://orcid.org/0000-0003-1011-2025)) †
- Suneel S Apte<sup>1</sup> ([ORCID: 0000-0001-8441-1226](https://orcid.org/0000-0001-8441-1226)) †

### Affiliations

1. Department of Biomedical Engineering, Cleveland Clinic Lerner Research Institute Cleveland United States
2. Department of Biomedical Engineering, Yale University New Haven United States
3. Case Comprehensive Cancer Center, Case Western Reserve University Cleveland United States
4. Department of Experimental Medical Science and Wallenberg Center for Molecular Medicine, Lund University Lund Sweden
5. The Sir Martin Evans Building, School of Biosciences, Cardiff University Cardiff United Kingdom
6. Department of Pediatrics, University of Chicago Chicago United States
7. Department of Medicine, Case Western Reserve University Cleveland United States
8. The Women's Health Institute, Department of Obstetrics and Gynecology, Cleveland Clinic Cleveland United States

† Corresponding author

## Abstract

The umbilical artery lumen closes rapidly at birth, preventing neonatal blood loss, whereas the umbilical vein remains patent longer. Here, analysis of umbilical cords from humans and other mammals identified differential arterial-venous proteoglycan dynamics as a determinant of these contrasting vascular responses. The umbilical artery, but not the vein, has an inner layer enriched in the hydrated proteoglycan aggrecan, external to which lie contraction-primed smooth muscle cells (SMC). At birth, SMC contraction drives inner layer buckling and centripetal displacement to occlude the arterial lumen, a mechanism revealed by biomechanical observations and confirmed by computational analyses. This vascular dimorphism arises from spatially regulated proteoglycan expression and breakdown. Mice lacking aggrecan or the metalloprotease ADAMTS1, which degrades proteoglycans, demonstrate their opposing roles in umbilical vascular dimorphism, including effects on SMC differentiation. Umbilical vessel dimorphism is conserved in mammals, suggesting that differential proteoglycan dynamics and inner layer buckling were positively selected during evolution.

## Introduction

The umbilical cord, typically containing two arteries and one vein in humans, is a crucial fetal structure in placental mammals. Umbilical arteries carry fetal blood to the placental vascular bed, whereas the umbilical vein returns oxygenated blood to the fetus. Neonatal respiration at birth renders the maternal oxygen supply redundant. Umbilical arteries commence closure rapidly after delivery of the newborn whereas the veins remain open longer. The cord is routinely clamped following delivery and divided between the clamps in modern obstetric practice. Timing of cord clamping after birth, whether early or late, is extensively debated (Niermeyer, 2015; Tarnow-Mordi et al., 2017). A recent recommendation suggested clamping no earlier than 30–60 s after birth to facilitate the placental transfusion (TACoOaG, 2017). Although the necessity of clamping is rarely questioned, it appears to be a modern practice (Downey and Bewley, 2012). Cord clamping is rarely practiced in domesticated animals and certainly not in wild animals, yet all current mammalian species have survived evolutionarily. We hypothesized that intrinsic design characteristics of mammalian umbilical arteries prevent blood loss at birth without clamping.

Prior histological work revealed that umbilical arteries have a bilaminar structure (Meyer et al., 1978) but lack elastic lamellae, which endow large arteries with resilience during cyclic loading (Wagenseil and Mecham, 2009). However, the molecular mechanism underlying the bilayered structure and its relationship to arterial occlusion remains obscure. Here, we used a multi-disciplinary approach integrating a variety of morphologic approaches with mechanical testing, computational analysis and mouse mutants to demonstrate the molecular and biomechanical basis for rapid umbilical artery closure. The findings emphasize the dual importance of extracellular matrix proteoglycans in regulation of cell differentiation and conferment of desirable tissue mechanical characteristics.

## Results

### The umbilical artery has a bilaminar wall

Three-dimensional imaging of term human umbilical cords, using synchrotron-based phase contrast micro-CT with effective pixel size 1.63 × 1.63 μm2 (Norvik et al., 2020) and histology, identified a much thicker tunica media (TM) in the umbilical artery than in the vein, with a visibly different structure (Figure 1a–c, Figure 1—figure supplement 1a–c, Figure 1—videos 1, 2). Most umbilical arteries were occluded at birth independent of delivery method or cord region analyzed, whereas umbilical veins remained patent (Figure 1b, Figure 1—figure supplement 1b). Smooth muscle cell (SMC) markers showed similar staining intensities within inner and outer TM of the umbilical arteries and TM of the vein with alternating layers of longitudinal and circumferentially oriented SMCs (Figure 1—figure supplement 1c,d). The veins showed fewer layers of SMCs compared to the arteries (Figure 1—figure supplement 1c,d).

![Figure 1.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig1-v2.jpg)

**Figure 1.:** (a) Synchrotron imaging of umbilical vessels at birth illustrates a bilayered arterial wall comprising an inner buckled tunica media (TM) (red) and outer TM (purple) but no distinct inner layer or buckling in the vein. X-Y and Y-Z image planes are indicated by red dashed lines (n = 3 umbilical cords). (b) Quantitation of luminal cross-sectional area at birth shows that the umbilical arteries are occluded whereas the veins remain patent (top) and have significantly thicker walls (bottom) (n = 20 cords, error bars indicate mean ± S.E.M., whiskers indicate minimum and maximum values. ***, p<0.001). (c) Alcian blue, eosin (pink) and nuclear fast red staining of umbilical vessel cross-sections shows a proteoglycan-rich (blue) inner TM in the umbilical artery but not the vein. Quantified staining intensity is shown on the right (n = 6 umbilical cords, whiskers indicate minimum and maximum values, ***, p<0.001). (d) Chondroitin sulfate (CS), heparan sulfate (HS), aggrecan and versican immunofluorescence (n = 4 cords for each antibody) showing that CS staining corresponds with aggrecan and versican staining and alcian blue in (c). (e) Volcano plots illustrating differential gene expression between human umbilical artery (red) and vein (green) (top, n = 4 umbilical arteries and veins) and differential gene expression between human umbilical artery inner TM (red) and the outer TM (green) (bottom, n = 2). (f) RNA in situ hybridization shows robust ACAN and VCAN expression (red signal) in the inner artery TM and weak expression in the vein (n = 3 umbilical cords for each in situ probe). * marks the vessel lumen. Brackets in c,d,f mark the TM. Wj, Wharton’s jelly. Scale bars = 100 μm in c,d,f.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) Synchrotron image from Figure 1a without red and purple shading illustrates contrast between inner and outer arterial tunica media (TM) as well as inner TM buckling, compared with a uniform appearance of venous TM and lack of buckling (n = 3 umbilical cords). (b) Hematoxylin and eosin stained human umbilical artery cross-sections collected from the placental and fetal ends show occlusion of the umbilical artery with buckling of its interior, while the vein remains patent and lacks buckling (n = 25 umbilical cords). (c) Hematoxylin and eosin stained cross-sections show multiple cell layers composed of alternating circumferentially (C) or longitudinally (L) oriented smooth muscle cells (SMC) in the umbilical artery. Curved white arrows indicate internal protrusion of the inner TM of the umbilical artery arising from buckling. (d) α-SMA (α-smooth muscle actin, red) and DAPI (blue) staining of the umbilical artery and vein shows distinct orientation of the SMC layers as in (c) (n = 3 umbilical cords). (e) (Left) Alcian blue staining shows intense staining of the inner arterial TM, with radially-oriented rounded cells contrasting with outer TM cells having elongated morphology. Eosin (pink) and nuclear fast red counterstaining. (Right) Sox9 immunostaining shows nuclear staining of SMCs of the inner umbilical artery TM (n = 6 umbilical cords, * marks the vessel lumen in panels (c,d,e). White brackets in (c,d and e) mark the TM. Tm, tunica media). Scale bars = 200 μm in (b) and c, 100 μm in d and 50 μm in e.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (a) Heat map of a subset of differentially expressed genes (1.9 fold-change) from umbilical artery vs vein (n = 4 umbilical cords). (b) Ingenuity pathway analysis (IPA) summary of the most significantly different pathways (n = 4 umbilical cords).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (a) Heat map of a subset of differentially expressed genes (1.9 fold-change) (n = 2 umbilical arteries, two inner TM samples matched to two outer TM samples). (b) Ingenuity pathway analysis (IPA) showing significantly different pathways in the umbilical artery inner and outer tunica media (n = 2 umbilical arteries, two inner TM samples matched to two outer TM samples).

Alcian blue, which binds sulfated glycosaminoglycans (GAGs), intensely stained the inner layer of the bilayered arterial TM but only the innermost three to four cell layers of the venous TM (Figure 1c). SMCs in this GAG-rich region of the arteries were radially oriented and round, with nuclear-localized Sox9, a chondrogenic factor (Figure 1—figure supplement 1e; Ng et al., 1997). The distribution of chondroitin sulfate (CS) coincided with Alcian blue staining (Figure 1c–d, Figure 1—figure supplement 1e), whereas heparan sulfate was more abundant in the outer arterial TM (Figure 1d), suggesting that the inner TM was enriched in CS-proteoglycans (CSPGs). RNA microarray data from matched human umbilical arteries and veins showed, among many differentially expressed genes (Figure 1e, Figure 1—figure supplement 2, Sup. array data-1), arterial prevalence of mRNAs for ACAN and VCAN encoding CSPGs bearing the most CS-chains, aggrecan and versican, respectively (Figure 1e). Microarray analysis of the inner versus outer arterial TM identified stronger ACAN and VCAN expression in the inner TM, among other differences (Figure 1e, Figure 1—figure supplement 3, Sup. array data-2). RNA in situ hybridization (RNA-ISH) localized strong ACAN and VCAN expression in inner arterial TM SMC, and immunostaining showed versican and aggrecan core proteins in a similar distribution as alcian blue and anti-CS staining (Figure 1c,d,f). Versican is a well-characterized vascular component (Wight and Merrilees, 2004), and aggrecan, which is known as a cartilage and neural proteoglycan (Lauing et al., 2014; Schwartz and Domowicz, 2014), is emerging as a significant CSPG in vascular disease (reviewed in Koch et al., 2020).

### ADAMTS proteoglycanases are differentially expressed in the umbilical artery and vein

Aggrecan and versican are proteolytically cleaved by ADAMTS1, 4, 5, and 9 (Dancevic et al., 2016). ADAMTS1 and ADAMTS4 mRNAs had higher levels in the venous wall in microarrays (Figure 1e, Sup. Array data-1), and RNA-ISH demonstrated stronger expression of ADAMTS1, ADAMTS4, ADAMTS5, and ADAMTS9 in the veins (Figure 2a). ADAMTS1 was the most strongly expressed, localizing to venous endothelium and TM, with stronger umbilical artery expression seen in the outer than inner TM (Figure 2a). ADAMTS9 was similarly expressed as ADAMTS1, whereas ADAMTS4 and ADAMTS5 mRNAs were restricted to umbilical vein endothelium and some venous SMC (Figure 2a). Neo-epitope antibodies detecting ADAMTS-cleaved aggrecan and versican (anti-NITEGE and anti-DPEAAE, respectively) (Lark et al., 1995; Sandy et al., 1992; Sandy et al., 2001) showed strong staining throughout the venous TM and in the outer arterial TM, but not the inner arterial TM (Figure 2b). Thus, proteoglycan accumulation in the inner TM of the umbilical artery may result from higher ACAN and VCAN expression and less proteolysis. In contrast, lower ACAN and VCAN expression and greater ADAMTS levels within the umbilical vein may preclude proteoglycan accumulation.

![Figure 2.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig2-v2.jpg)

**Figure 2.:** (a) RNA in situ hybridization shows robust ADAMTS1 and ADAMTS9 expression in umbilical vein endothelium and tunica media (TM) and in outer arterial TM. Robust ADAMTS4 and ADAMTS5 expression was confined to the venous endothelium, with moderate ADAMTS4 expression and minimal ADAMTS5 expression in SMC (n = 3 umbilical cords for each probe). (b) ADAMTS-cleaved aggrecan (anti-NITEGE, red) and versican (anti-DPEAAE, red) both showed strong ADAMTS proteolytic activity throughout the venous wall and the outer artery TM. Unlike aggrecan, extensive versican proteolysis is seen in the arterial intima and sub-intima (n = 4 umbilical cords for each antibody). Wj, Wharton’s jelly. The brackets mark TM boundaries. Scale bars in a-b = 100 μm.

### ADAMTS-mediated differential proteoglycan abundance in the umbilical artery and vein is evolutionarily conserved

We postulated that abundant hydrated proteoglycans in the inner arterial TM provided compressive stiffness that could not only prevent kinking and premature occlusion but could potentially facilitate rapid umbilical artery closure at birth. If so, similar adaptations should be present in other mammals. Analysis of umbilical cords from nine large primate and non-primate mammals disclosed similar dimorphism, namely, umbilical arteries were occluded and had thicker walls with similar infolding of the inner arterial TM (Figure 3a) and strong Alcian blue and CS-staining, contrasting with veins (Figure 3a,b). Anti-aggrecan and anti-NITEGE stained several animal species, confirming aggrecan abundance in the inner arterial TM and robust aggrecan cleavage resulting from ADAMTS protease activity in the outer TM of the artery and the TM of the vein (Figure 3c–d, Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig3-v2.jpg)

**Figure 3.:** (a) Alcian blue-eosin staining of umbilical cord sections shows proteoglycan enrichment (blue) in the inner arterial tunica media (TM). The elephant umbilical vein was unavailable. (b) Anti-CS immunofluorescence (7D4, green) shows enrichment in the inner arterial TM. Bonobo cords lacked 7D4 reactivity. (c,d) Aggrecan and anti-NITEGE immunostaining from reactive species showed aggrecan enrichment in the inner arterial TM and aggrecan proteolysis in the vein and outer artery TM. n = 3 for Gazelle and n = 1 for other mammals. Triplicate sections were stained from each animal cord. Scale bars = 100 μm and 200 μm. * indicates the vessel lumen.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The cleavage site location is shown over the sequence alignment by scissors, and the critical Glu(E) residue essential for cleavage is shown by red highlighting. Bold text identifies the cleavage-revealed neo-epitope NITEGE. Residue numbers are indicated for human and mouse aggrecan only.

### Aggrecan and ADAMTS1 are necessary for normal umbilical cord morphogenesis

Mouse umbilical cords also demonstrated vascular dimorphism (Figure 4a), suggesting that genetically modified mice would provide mechanistic insights into proteoglycan dynamics and its impact. Aggrecan and versican immunofluorescence showed strong staining in the mouse umbilical artery inner TM and adventitia, with weaker staining in the veins (Figure 4b). Acan, Vcan and Adamts1,4,5,9 RNA-ISH at early (E12.5) and late (E18.5) gestational stages showed that Acan and Vcan were strongly expressed in the umbilical arteries (Figure 4—figure supplement 1a). Adamts1 was the most highly expressed proteoglycanase in the mouse umbilical vein just prior to parturition (E18.5) (Figure 4—figure supplement 1a), evidenced by strong β-gal staining in venous TM, adventitia and endothelium; the inner umbilical artery TM and endothelium of Adamts1lacZ/+ embryos lacked β-gal staining (Figure 4c). Although Adamts9 mutant embryos were previously observed to have short umbilical cords, abnormal umbilical artery development, and to die by 14.5 days of gestation (Nandadasa et al., 2015), umbilical cord development was not previously investigated in mutants of the two genes implicated here as potentially critical for umbilical cord vascular dimorphism, Acan and Adamts1.

![Figure 4.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig4-v2.jpg)

**Figure 4.:** (a) H and E staining of E18.5 wild-type cords showing thicker umbilical arterial (A) and thinner venous (V) wall (n = 6 umbilical cords). (b) Aggrecan and versican localization (red, DAPI counterstain blue) in E18.5 wild-type cords showing staining in the arterial inner tunica media (TM) and adventitia but not the vein (n = 3 umbilical cords). (c) β-gal (blue) and eosin (red) staining of E18.5 Adamts1LacZ/+ (Adamts1+/-) cord showing strong Adamts1 expression in venous endothelium and TM and outer artery TM (n = 3 umbilical cords). (d) Short umbilical cords in E18.5 Adamts1-/- and Acan-/- embryos compared to wild type. Red arrowhead indicates an omphalocele in Adamts1-/- embryos. (e) H & E staining of E18.5 wild type, Acan-/- and Adamts1-/- cord cross-sections showing thinner walls in Acan-/- umbilical vessels and thicker walls in Adamts1-/- umbilical vessels. (f–g) Cord length, TM thickness and vessel luminal area quantifications for Adamts1-/- (f) and Acan-/- mice (g) at E18.5 compared to wild-type littermates. Acan-/- umbilical cords show larger lumens and Adamts1-/- vessels show smaller lumens in (n = 7–11 umbilical cords each, whiskers indicate minimum and maximum values, *, p<0.05; **, p<0.01; ***, p<0.001; ****, p<0.0001). (h) Phospho-histone H3 (pHH3) staining shows significantly fewer proliferating cells (white arrowheads) in Acan-/- umbilical vessels. Dotted white lines mark the boundaries of vessel lumens (n = 4 cords each, whiskers indicate minimum and maximum values, **, p<0.001; *, p<0.05). Scale bars = 100 μm in (a), 25 μm in (c), 100 μm and 50 μm in (e).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) RNA in situ hybridization analysis of E12.5 and E18.5 mouse umbilical cord sections Acan, Vcan and relevant ADAMTS genes (n = 3 umbilical cords for each probe). (b) E12.5 and E14.5 wildtype and Acan-/- embryos have a comparable umbilical cord length (n = 2 Acan-/- at E12.5 and n = 3 at E14.5). (c) Observed and expected genotype ratios at different embryonic stages from Acan+/- and Adamts1+/- intercrosses. (d) Hematoxylin and eosin staining of E14.5 wild type and Acan-/- umbilical cords shows completion of longitudinal to circumferential reorientation of smooth muscle cells in the mutant arterial tunica media (TM). Upper panels show tangential longitudinal sections whereas the lower panels are taken through the approximate center of each vessel (n = 3 umbilical cords of each genotype). Adv, adventitia; Tm, tunica media. Scale bars in a = 100 μm, 3 mm and 7 mm in (b) and 50 μm in (d).

The Adamts1-/- mutant is an insertion of an IRES lacZ-bearing cassette into intron 1 of the gene (Oller et al., 2017). This insertion reveals Adamts1 expression via staining for ß-galactosidase activity, and eliminated expression from the targeted allele but in its hemizygous state, the insertion led to reduction in both mRNA and protein (Oller et al., 2017). The Acancmd-Bc allele is a spontaneous mutation found in a BALB/C colony (Bell et al., 1986) and resulted from deletion of exon 2 through exon 18 (Krueger et al., 1999). Acan-/- embryos do not survive past birth (Krueger et al., 1999; Lauing et al., 2014) and few surviving Adamts1-/- mice were identified at the time of weaning (Oller et al., 2017). Acan mutants are thought to succumb to respiratory failure resulting from soft tracheal cartilages and ribs, whereas the cause of Adamts1-/- lethality is unknown. At E18.5, Acan-/- and Adamts1-/- mutants each had significantly short umbilical cords (Figure 4d) demonstrating their requirement for proper umbilical cord development. Umbilical cord histology showed thinner vascular walls in Acan-/- umbilical vessels, and conversely, thicker vascular walls in Adamts1-/- umbilical vessels (Figure 4e–g). At earlier developmental stages (E12.5 to E14.5), lack of aggrecan did not affect either umbilical cord length or circumferential SMC reorientation (Figure 4—figure supplement 1b–d), which occurs around E13.5 and is defective in Adamts9 mutants (Nandadasa et al., 2015). Furthermore, lack of aggrecan did not impair the survival of mouse embryos until parturition, since Acan-/- embryos were observed at the expected Mendelian ratio at E18.5 (Figure 4—figure supplement 1c). Thus, Acan and Adamts1 appear to be involved in umbilical vessel development from early gestation, but their functions manifest near parturition.

### Contrasting SMC phenotypes in Acan and Adamts1-deficient umbilical cords

The arterial and venous lumina were smaller in Adamts1-/- mice relative to wild-type, indicating that their thicker vascular walls compromised luminal diameter, and larger in Acan-/- mice (Figure 4e–g). Phospho-histone H3 staining revealed fewer proliferating cells in Acan-/- umbilical cords at E18.5 (Figure 4h). Immunostaining for SMC markers smooth muscle α-actin (SMA), smooth muscle myosin heavy chain (SMMHC), and phosphorylated myosin light chain (pMLC) showed weaker intensity in Acan-/- umbilical arteries compared to wild-type (Figure 5a,b). In contrast, Adamts1-/- umbilical vessels showed stronger SMA, SMMHC and pMLC staining than wild-type littermates and apparent overgrowth of the arterial and venous walls (Figure 5c). Intriguingly, endomucin, a venous endothelium-specific marker (dela Paz and D'Amore, 2009), also stained Adamts1-/- umbilical arterial endothelium (Figure 5c) suggesting that ADAMTS1 may have a role in specifying artery/vein identity. Immunostaining of E17.5 Adamts1-/- umbilical cords indicated a crucial role for ADAMTS1 in regulating proteoglycan dynamics in the mouse umbilical cord. Specifically, we observed robust aggrecan and versican accumulation in the Adamts1-/- umbilical vein and in the outer TM of the Adamts1-/- umbilical artery (Figure 6a–d) with severe reduction of aggrecan and versican neo-epitope staining (Figure 6a–d).

![Figure 5.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig5-v2.jpg)

**Figure 5.:** (a) Aggrecan (green) and α-SMA staining (red) in E18.5 umbilical cords show loss of aggrecan and weak α-SMA staining in Acan-/- vessels (n = 3 umbilical cords each genotype). (b) Smooth muscle myosin heavy chain (SMMHC, red) and phosphorylated myosin light chain (pMLC, green) staining in E18.5 umbilical cords showing dramatic signal attenuation in the Acan-/- vessels (n = 3 umbilical cords each genotype) (c) pMLC (green), endomucin (red), α-SMA (red, center panels) and SMMHC (red, right-hand panels) staining shows blunted dimorphism of Adamts1-/- umbilical artery and vein with stronger expression of differentiated SMC markers in Adamts1-/- umbilical vessels and acquisition of endomucin, a venous endothelium marker, by arterial endothelium (n = 3 umbilical cords each genotype) Scale bars = 100 μm in (a–c).

![Figure 6.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig6-v2.jpg)

**Figure 6.:** (a,b) E17.5 Adamts1-/- umbilical vessels show increased aggrecan staining and reduced anti-NITEGE staining in (a), quantified in (b) (n = 3 cords each genotype, error bars indicate mean ±S.D.*, p<0.05; **, p<0.01; ***, p<0.001). (c,d) Adamts1-/- umbilical vessels show increased versican (c) and reduced anti-DPEAAE staining quantified in (d) (n = 3 cords each genotype, error bars indicate mean ±S.D. *, p<0.05; **, p<0.01). Scale bars = 50 μm in (a–c).

### Differential SMC contraction in the bilayered umbilical arteries

Despite uniform staining with SMC markers in human umbilical vascular SMC, co-staining with serine20-phosphorylated myosin light chain (pMLC) marking contractile SMCs (Dougherty et al., 2014) revealed that human umbilical arteries had more contractile SMCs than the vein, predominantly in the outer TM (Figure 7a,b). This suggests that outer umbilical artery SMCs are principally responsive to vasoconstriction stimuli at birth, whereas inner SMCs are relatively non-contractile. We hypothesized that an outer ring of contracting SMCs could drive the CSPG-rich inner arterial TM centripetally, occluding the lumen, and addressed this possibility initially using ex vivo biomechanical testing of late-gestation mouse umbilical vessels (Figure 7c, Figure 7—figure supplement 1). Mouse umbilical arteries had a smaller lumen, as expected at E18.5, and deformed less when loaded mechanically, namely, they exhibited lower (circumferential) distensibility and especially (axial) extensibility under passive conditions compared to the umbilical veins (Figure 7—figure supplement 1a–d). Umbilical arteries constricted significantly (30–50% reduction in measured outer diameter at 25 mm Hg fixed pressure), causing complete luminal occlusion verified by optical coherence (OCT) imaging, which was not observed in the umbilical veins (Figure 7c). Cross-sectional area measurements at fixed lengths revealed wall volume reductions during vasoconstriction (Figure 7—figure supplement 1e), less in the umbilical vein (~35%) than the umbilical artery (~50%), suggesting fluid exudation from the wall under forceful SMC contraction.

![Figure 7.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig7-v2.jpg)

**Figure 7.:** (a) Smooth muscle myosin heavy chain (SMMHC-red) and serine-20 phosphorylated myosin light-chain (pMLC-green) show more contraction-primed SMCs in the outer arterial tunica media (TM, white brackets) than the umbilical vein. Scale bars are 100 µm. (b) Quantitation of pMLC+ SMCs in the artery (red) and vein (blue) (top, n = 5 arteries, four veins, whiskers indicate minimum and maximum values, *, p<0.05) and inner and outer TM of both reveal similar distributions but more pMLC+ SMC in the outer artery TM (bottom, n = 3 arteries, four veins, error bars indicate mean ±S.D. *, p<0.05; **, p<0.01). (c) Differential contraction of murine umbilical artery and vein stimulated by 100 mM potassium chloride (KCl) under biaxial loading confirms greater contractility in the artery, with OCT images prior to and following contraction-induced arterial closure (n = 4 arteries and n = 4 veins). (d) Computational simulations of a bilayered artery with contractile SMCs in the outer layer and swollen inner layer: critical contractile stress values leading to buckling for (left) different numbers of folds for a normalized inner layer volume of 0.5 and (right) decreasing values of normalized volume of the inner layer for seven folds. (e) Normalized inner radius as a function of contractile stress for inner layer volume change of 0.5 and 7 folds. The states for the inflection (square) and critical active stress (star) are illustrated by the schematics; complete closure achieved with contraction-induced buckling. All simulations were run for 25 mmHg pressure. Due to the linear stability analysis, the amplitude of the folds in the buckled schematics is illustrative. (f) Number of buckles observed in human (top, indicated as umbilical cord (UC)1–25) and other large mammalian (bottom) umbilical arteries. Both arteries per cord were included. Open vessel lumens are indicated where observed.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Biaxial structural (a,b) and material (c,d) behaviors exhibited by umbilical arteries and veins harvested from wild type E18.5 umbilical cords. The curves show model predicted results for the mean behaviors based on best-fit parameters determined from seven different testing protocols performed individually on n = 4 arteries and n = 4 veins. Though based on data from all seven protocols, for illustrative purposes results are shown for pressure-diameter behaviors during quasi-static pressurization at a fixed vessel-specific in vivo length and quasi-static axial extension at fixed pressures (25 mmHg for the arteries, and 5 mmHg for the veins). Grey-shaded regions show S.D. (e) Change in normalized cross-sectional area for the umbilical vein at 5 mm Hg and for the umbilical artery at 25 mm Hg during isobaric contraction. Error bars indicate S.E.M, **, p<0.01.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (a) Normalized inner radius as a function of normalized volume of the inner layer alone for different fixed values of the active stress parameter Tact and (b) inner radius as a function of the active stress parameter Tact for different fixed values of normalized volume in the inner layer. Loaded inner radius a was normalized by the unloaded inner radius A; the current volume of the vessel v was normalized by the original volume of the vessel V. (c) Critical value of the active stress parameter Tact as a function of the normalized volume in the inner layer for different numbers of buckling-induced luminal folds n. (d) Mean circumferential stress tθθ across the umbilical artery wall for varying normalized volumes: (i) and (ii) show circumferential stress for the case of shrinkage of the inner layer alone with v/V = 0.5 while (iii) and (iv) show the case of no swelling with v/V = 1.0. All simulations use the loading conditions, luminal pressure p=25 mmHg and fixed axial stretch λz=1.28.

### Computational modeling of arterial occlusion

These biomechanical tests of mouse umbilical cords, together with histological and immunostaining findings from human cords, motivated and informed a novel computational model of the umbilical artery incorporating its complex bilayered, multi-constituent structure (GAG-rich inner layer and contractile SMC-rich outer layer; Figure 7d) and multiaxial mechanical loading: axial extension, luminal pressurization, active contraction by SMCs, and intramural swelling of the inner layer that regulates tissue volume locally based on GAG content. Nonlinear regression of biaxial mechanical data from passive tests of the murine vessels identified best-fit values of the material parameters in the baseline constitutive model, while data from active contraction studies guided the selection of the associated active constitutive parameters (Table 1). Model-based parametric studies examined combinations of different levels of GAG-driven swelling and SMC-generated active stress to identify their roles in umbilical artery closure at different levels of fixed luminal pressure. Increasing inner layer swelling in the absence of active outer layer stress narrowed the lumen at a fixed pressure, as expected given the constraining effect of the outer stiff passive matrix (Figure 7—figure supplement 2a). This trend reversed in the presence of active stresses, with increasing inner layer GAGs able to oppose vasoconstriction if overall wall volume remained constant (Figure 7—figure supplement 2b). Thus, increased inner layer swelling attenuates the ability of SMC contraction to prematurely reduce luminal radius, as revealed by varying the active stress parametrically for different fixed values of inner layer swelling. Importantly, the model predicted a sharp transition from a widely patent to a narrowed lumen due to small changes in active stress at lower values of swelling whereas radius changes were more gradual at higher values of swelling (Figure 7—figure supplement 2b). This transition, at which a decrease in volume of the inner layer associates with larger or smaller luminal radii for values of active stress below or above $T_{act}≅50$ kPa (a key parameter of active stress generation) appears to be close to the in vivo value. Hence, consistent with ex vivo findings (Figure 7—figure supplement 1), it appears that inner layer volume loss during increased SMC contraction aids vessel narrowing. Regardless, the inner radius reached nearly constant values for increasing levels of active stress (Figure 7—figure supplement 2b). Thus, contraction alone is insufficient to occlude the vessel.

**Table 1.**
 Model parameters fixed for all simulations of the umbilical artery, determined primarily from the biaxial biomechanical data and histological findings.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Description</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A, B, C</td>
      <td>Unloaded inner, interface, outer radius</td>
      <td>161.77, 206.86, 236.92 µm</td>
    </tr>
    <tr>
      <td>λz</td>
      <td>Loaded axial stretch</td>
      <td>1.28</td>
    </tr>
    <tr>
      <td>μ1, μ2</td>
      <td>GAG/matrix shear modulus inner, outer layer</td>
      <td>3.0 kPa, 0.1 kPa</td>
    </tr>
    <tr>
      <td>c11,c21</td>
      <td>Axial fiber family material parameters</td>
      <td>0.013 kPa, 11.65</td>
    </tr>
    <tr>
      <td>c12,c22</td>
      <td>Circumferential fiber family material parameters</td>
      <td>2.66 kPa, 1.20</td>
    </tr>
    <tr>
      <td>c13,4,c23,4</td>
      <td>Diagonal fiber families’ material parameters</td>
      <td>3.04 kPa, 4.23</td>
    </tr>
    <tr>
      <td>η3,η4</td>
      <td>Diagonal fiber families’ alignment parameter</td>
      <td>41.92°, −41.92°</td>
    </tr>
    <tr>
      <td>λm,λ0</td>
      <td>Maximum, minimum contractile stretch</td>
      <td>2.5, 0.2</td>
    </tr>
  </tbody>
</table>

### Folding of the arterial inner layer is necessary for vascular occlusion

Given the consistent histological finding of inner arterial TM infolding following birth, we modeled the biomechanics of superimposed inner layer buckling in the bilayered arterial model. Buckling can release energy stored in the inner layer during vasoconstriction-induced compression, thereby reducing the structural stiffness and resistance to SMC contraction. This analysis parametrically considered possible perturbations to the cylindrical geometry achieved at various levels of fixed luminal pressure and different values of swelling and actively generated wall stress. Examining the influence of the number of inner layer folds for different values of swelling disclosed higher inward buckling probability with more folds (Figure 7d). Since $T_{act}$ needed to cause buckling tended to plateau at 7 folds, we used 7 folds subsequently for illustrative purposes. $T_{act}$ needed to cause buckling decreased for a more swollen inner layer Figure (7dFigure 7—figure supplement 2c) and increased exponentially with inner layer volume loss. This finding was likely due to the less negative values of circumferential wall stress in the inner layer occurring with shrinkage (Figure 7—figure supplement 2d). We found that an arterial wall consisting solely of SMCs and uniform matrix maintained a mean positive circumferential stress in the inner layer during contraction, that prevented buckling. Thus, a delicate biomechanical balance exists – reduced inner layer volume allows a smaller radius to be achieved via SMC contraction prior to buckling (Figure 7—figure supplement 2b), thus aiding closure, yet excess volume reduction of the inner layer increases the active stress requirement for buckling and achieving complete vessel closure (Figure 7d). The umbilical artery can reduce its cylindrical radius dramatically at $T_{act}$ near a basal value of ~50 kPa, progressing to buckling and closure via a subsequent near-maximal contraction (Figure 7e). In agreement with the computational modeling, 20/25 of human umbilical arteries had 4 or more buckles, whereas those with no buckles in the area analyzed by histology were patent (Figure 7f). Other large mammalian species analyzed showed a similar phenomenon (Figure 7f). Thus, buckling of the proteoglycan-rich inner tunica media may be a crucial and evolutionarily conserved mechanism employed by all mammals for rapid arterial occlusion at birth.

## Discussion

We report two distinct umbilical cord blood vessel specializations that may facilitate rapid umbilical artery occlusion at birth: a distinct proteoglycan-rich inner arterial TM, generating a bilayered arterial wall, and selective contraction of SMCs in the outer layer (Figure 8). The rounded SMCs of the inner TM may be specialized for CSPG production rather than contraction, consistent with nuclear Sox9 staining, a function they exert prior to delivery. During delivery, lack of pMLC staining suggests that despite differentiated SMC marker expression, the inner cells play a passive role. Biomechanical testing and computational analysis confirm that selective proteoglycan enrichment in the inner arterial TM ensures that contracting SMCs in the outer TM can effectively occlude the arterial lumen at birth (Figure 8). Histologic and computational analysis showed buckling of the inner TM and fluid redirection into the resulting TM protrusions as critical mechanisms resulting from specialization of the inner and outer arterial TM. By in silico simulations of umbilical arteries with modulation of the contractile outer layer and proteoglycan-rich inner core, we demonstrate that complete occlusion can be achieved.

![Figure 8.](https://cdn.elifesciences.org/articles/60683/elife-60683-fig8-v2.jpg)

**Figure 8.:** (a) Differential expression of ADAMTS proteases and large CS-proteoglycans during development results in a bilayered artery with a hydrated proteoglycan-rich inner layer and most contractile SMCs located in the outer layer, contrasting with the umbilical vein (see key at top of figure identifying the illustrated major elements). (b) At birth, SMC contraction in the outer layer and fluid movement-induced inner layer buckling redirects the inner layer into the lumen. The single-layered vein does not undergo buckling. (c) Umbilical artery occlusion at birth prevents neonatal exsanguination, whereas the patent vein allows a final transfusion from the placenta.

Our work suggests that a principal mechanism governing umbilical cord vascular dimorphism resides in extracellular matrix, namely, differentially regulated dynamics of aggrecan and versican, which may then modulate SMC development and differentiation. Other mammalian umbilical vessels examined, from animals as large as the walrus and elephant to as small as the mouse, showed similar CSPG and aggrecan modulation as in humans. Although Vcan mutant mice die before umbilical cord development is completed (Yamamura et al., 1997) and could not be studied, Acan and Adamts1 mutants demonstrated their mechanistic contributions to the observed dimorphism. Our emphasis on aggrecan in the inner layer, with its abundant GAGs and their high fixed charge density, was relevant to the computational findings of the importance of inner layer swelling and buckling in response to SMC contraction. The umbilical vein contains fewer contractile SMCs and has scant aggrecan and versican. Hence, SMC activation in the umbilical vein does not occlude the lumen to the same degree as in the arteries, a contention supported by computational analysis. Given the evolutionary pressure to achieve hemostasis urgently in the artery rather than the vein, these findings suggest a highly evolved mechanism for preventing exsanguination of the newborn that is potentially relevant to other embryonic shunts that occlude rapidly at birth.

The computational model was built on a long history of studying murine arteries and veins (Ferruzzi et al., 2013), but was specialized to the GAG-rich inner layer and SMC-rich outer layer of the umbilical artery. Modeling the dynamics of associated volume changes would have required a mixture or poroelastic model and significantly more experimental data, including measurement of layer-specific permeabilities and fixed-charge densities. Instead, we modeled the quasi-equilibrated states using a well-accepted approach wherein the degree of swelling can be adjusted for each simulation (Demirkoparan and Pence, 2007; Szafron et al., 2017). Interestingly, prior results by others showed that swelling of an initially unloaded, unilayered cylindrical tube consisting of a neo-Hookean material (which we used to model GAG-rich tissue) increases luminal diameter if the tube is unconstrained (Demirkoparan and Pence, 2007). The tube must be constrained, such as by a stiff outer layer surrounding the swollen layer if swelling is to decrease luminal diameter (Szafron et al., 2017). The abundance of contractile SMCs in the stiffer outer layer and their basal tone may in fact enhance outer layer stiffness contributed by extracellular matrix and hence buckling appears to be essential to augment contraction-induced closure of the umbilical artery (cf [Moulton and Goriely, 2011]).

This observed architecture of the umbilical cord is likely to have supported survival of mammalian species, humans included, well before formal obstetric involvement in labor. Cord clamping is the default practice today and has the sanction of convention, offering the option of immediate neonatal resuscitation if needed. In regard to the umbilical artery, it would replicate the effect of a natural and apparently conserved physiologic process that interrupts its blood flow during transition from fetal to neonatal life. The latest recommendation to clamp the cord later rather than immediately after birth appears to align better with the delayed closure of the umbilical vein. The present studies in humans and other mammals show that evolution has devised an umbilical cord-intrinsic mechanism that facilitates rapid arterial occlusion at birth, leaving the vein patent and permitting a placental infusion. This unfailing sequence ensures continuation of mammalian species without other formal intervention, since evolutionary success is not about minimizing poor outcomes, but ensuring survival of a significant majority.

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
      <td>Gene (Homo sapiens)</td>
      <td>ACAN</td>
      <td>GenBank</td>
      <td>RRID:HGNC:319</td>
      <td>Chondroitin sulphate proteoglycan 1</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>VCAN</td>
      <td>GenBank</td>
      <td>RRID:HGNC:2464</td>
      <td>Chondroitin sulphate proteoglycan 2</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>ADAMTS1</td>
      <td>GenBank</td>
      <td>RRID:HGNC:217</td>
      <td>ADAM metallopeptidase with thrombospondin type 1 motif 1</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>ADAMTS4</td>
      <td>GenBank</td>
      <td>RRID:HGNC:220</td>
      <td>ADAM metallopeptidase with thrombospondin type 1 motif 4</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>ADAMTS5</td>
      <td>GenBank</td>
      <td>RRID:HGNC:221</td>
      <td>ADAM metallopeptidase with thrombospondin type 1 motif 5</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>ADAMTS9</td>
      <td>GenBank</td>
      <td>RRID:HGNC:13202</td>
      <td>ADAM metallopeptidase with thrombospondin type 1 motif 9</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Acancmd-Bc (C57BL/6J background)</td>
      <td>Krueger et al., 1999</td>
      <td>RRID:MGI:1855999</td>
      <td>Acan null allele</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Adamts1tm1Dgen (C57BL/6J background)</td>
      <td>Oller et al., 2017</td>
      <td>RRID:MGI:5427602</td>
      <td>Adamts1 null and LacZ reporter allele</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal smooth muscle α-actin (α-SMA) Cy3 conjugated</td>
      <td>Millipore Sigma C6198</td>
      <td>RRID:AB_476856</td>
      <td>IF (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal smooth muscle myosin heavy chain (SMMHC)</td>
      <td>Kamiya Biomedical MC352</td>
      <td>RRID:AB_1241986</td>
      <td>IF (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal Serine-20 phosphorylated myosin light chain (pMLC)</td>
      <td>Abcam Ab2480</td>
      <td>RRID:AB_303094</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-serine-10 phosphorylated histone H3 (pHH3)</td>
      <td>Millipore Sigma 06–570</td>
      <td>RRID:AB_310177</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-chondroitin sulfate (7D4) antibody</td>
      <td>Bruce Caterson/Clare Hughes laboratory (Sorrell et al., 1990)</td>
      <td>RRID:AB_2864328</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal FITC-conjugated anti-heparan sulfate (10E4) antibody</td>
      <td>US Biological H-1890</td>
      <td>RRID:AB_10013601</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal Anti-versican (pVC)</td>
      <td>Apte laboratory (Foulcer et al., 2014)</td>
      <td>RRID:AB_2864327</td>
      <td>IF (1:400) human tissue</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-versican GAG-beta</td>
      <td>Millipore Sigma AB1033</td>
      <td>RRID:AB_90462</td>
      <td>IF (1:400) mouse tissue</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-versican V0/V1 neo epitope DPEAAE</td>
      <td>Invitrogen PA1-1748A</td>
      <td>RRID:AB_2304324</td>
      <td>IF (1:200) human/mouse</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-aggrecan</td>
      <td>Millipore Sigma AB1031</td>
      <td>RRID:AB_90460</td>
      <td>IF (1:400) all species</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-aggrecan neo epitope NITEGE</td>
      <td>Invitrogen PA1-1746</td>
      <td>RRID:AB_2242021</td>
      <td>IF (1:200) all species</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-endomucin antibody (clone eBioV.7C7)</td>
      <td>Invitrogen 14-5851-85</td>
      <td>RRID:AB_891531</td>
      <td>IF (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SOX9 antibody</td>
      <td>Millipore Sigma AB5535</td>
      <td>RRID:AB_2239761</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ACAN RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>506841</td>
      <td>Human probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Acan RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>439101</td>
      <td>Mouse probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>VCAN-E8 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>452241</td>
      <td>Human probe detects exon 8</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Vcan-E8 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>428321</td>
      <td>Mouse probe detects exon 7</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ADAMTS1 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>524501</td>
      <td>Human probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Adamts1 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>463361</td>
      <td>Mouse probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ADAMTS4 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>537341</td>
      <td>Human probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Adamts4 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>497161</td>
      <td>Mouse probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ADAMTS5 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>427611</td>
      <td>Human probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Adamts5 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>427621</td>
      <td>Mouse probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ADAMTS9 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>445321</td>
      <td>Human probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Adamts9 RNAscope In situ probe</td>
      <td>ACD bio</td>
      <td>400441</td>
      <td>Mouse probe</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAscope 2.5 HD Red In situ detection kit</td>
      <td>ACD bio</td>
      <td>322350</td>
      <td>Used for detecting all probes in this study</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Affymetrix Transcriptome Analysis Console, RMA-SST sketch algorithm</td>
      <td>Affymetrix TAC 4.0</td>
      <td>RRID:SCR_018718</td>
      <td>Used for gene expression analysis for all microarray experiments in the study</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R</td>
      <td>Bell Laboratories/R Foundation for Statistical Computing Ver. 3.5.2.</td>
      <td>RRID:SCR_001905</td>
      <td>Used for statistical computing of microarray data</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad</td>
      <td>RRID:SCR_002798</td>
      <td>Used for statistical computing of other experimental data</td>
    </tr>
  </tbody>
</table>

_Abbreviations, IF, Immunofluorescence._

### Human and large mammal cords

Twenty-five human umbilical cords were obtained from uncomplicated term pregnancies either after vaginal birth (n = 13) or Cesarean section for obstetric indications (n = 12), that is, malpresentation or repeat Cesarean section. The samples were collected under an IRB exemption from Cleveland Clinic (EX-0118) for use of discarded tissue without patient identifiers. These cords were used for histological/immunohistologic analysis, synchrotron imaging, RNA in situ hybridization, and transcriptomics of inner versus outer umbilical artery TM. Animal cord sections were provided by Disease Investigations, Institute for Conservation Research, San Diego Zoo Global from the Benirschke archive.

### Mutant mice

The Adamts1 transgenic allele (Adamts1tm1Dgen), referred to herein as Adamts1-/-, was produced by insertion of an IRES-lacZ cassette into intron 1 of Adamts1 using homologous recombination in mouse embryonic stem cells (Oller et al., 2017). The Acancmd-Bc allele was previously described (Krueger et al., 1999) and is referred to herein as Acan-/-. Mice were handled under standard conditions under approved IACUC protocols at the Cleveland Clinic (IACUC protocol nos. 18–1996 and 18–2045) and University of Chicago (IACUC protocol no. 43751). Mutant mouse embryos were collected by timed matings of heterozygous mice by the detection of copulation plugs (taken as day 0.5 of gestation). Embryos were dissected out immediately following CO2 mediated euthanasia and cervical dislocation of pregnant mice. Dissected whole embryos, with umbilical cords and placentas attached, were fixed in 4% paraformaldehyde at 4°C overnight. Umbilical cords were dissected out the following day and washed thrice in PBS and embedded in paraffin or in 4% agarose for vibratome sectioning as previously described (Nandadasa et al., 2015).

### Biomechanical and computational analysis

The umbilical artery and vein were obtained at E18.5 from mouse embryos (n = 4) following approval by the Yale University IACUC (protocol no 2018–11508), then mounted within a custom computer-controlled biaxial device designed specifically for biomechanical testing of murine vessels (Gleason et al., 2004). Vessel maintenance, pre-conditioning, biaxial loading protocols and data collection are described in Appendix 1. The umbilical artery was modeled computationally as a thick-walled, bilayered cylindrical tube subjected to swelling of the GAG-rich inner layer and active contraction of the smooth muscle-rich outer layer; the model also included a passive contribution of extracellular matrix as revealed by biomechanical tests.

### Statistical analysis

Statistical analyses were carried out using GraphPad Prism analytical software (versions 6–8, GraphPad, San Diego, CA) in determining statistical significance using two-tailed Student’s t-test. Statistical details including N and p values are provided in each corresponding figure legend. Statistical analyses for microarray gene expression were performed using Affymetrix’s Transcriptome Analysis Console (TAC 4.0) through the RMA-SST sketch algorithm and R version 3.5.2. Fold changes were calculated by an empirical Bayes ANOVA method through the TAC 4.0 software. Details of these and additional methods are provided in Appendix 1.
