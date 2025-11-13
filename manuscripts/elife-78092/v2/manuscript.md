# Differentiation signals from glia are fine-tuned to set neuronal numbers during development

## Authors

- Anadika R Prasad<sup>1</sup> ([ORCID: 0000-0003-4067-1784](https://orcid.org/0000-0003-4067-1784))
- Inês Lago-Baldaia<sup>1</sup>
- Matthew P Bostock<sup>1</sup>
- Zaynab Housseini<sup>1</sup>
- Vilaiwan M Fernandes<sup>1</sup> ([ORCID: 0000-0002-1991-7252](https://orcid.org/0000-0002-1991-7252)) †

### Affiliations

1. Department of Cell and Developmental Biology, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))

† Corresponding author

## Abstract

Neural circuit formation and function require that diverse neurons are specified in appropriate numbers. Known strategies for controlling neuronal numbers involve regulating either cell proliferation or survival. We used the Drosophila visual system to probe how neuronal numbers are set. Photoreceptors from the eye-disc induce their target field, the lamina, such that for every unit eye there is a corresponding lamina unit (column). Although each column initially contains ~6 post-mitotic lamina precursors, only 5 differentiate into neurons, called L1-L5; the ‘extra’ precursor, which is invariantly positioned above the L5 neuron in each column, undergoes apoptosis. Here, we showed that a glial population called the outer chiasm giant glia (xgO), which resides below the lamina, secretes multiple ligands to induce L5 differentiation in response to epidermal growth factor (EGF) from photoreceptors. By forcing neuronal differentiation in the lamina, we uncovered that though fated to die, the ‘extra’ precursor is specified as an L5. Therefore, two precursors are specified as L5s but only one differentiates during normal development. We found that the row of precursors nearest to xgO differentiate into L5s and, in turn, antagonise differentiation signalling to prevent the ‘extra’ precursors from differentiating, resulting in their death. Thus, an intricate interplay of glial signals and feedback from differentiating neurons defines an invariant and stereotyped pattern of neuronal differentiation and programmed cell death to ensure that lamina columns each contain exactly one L5 neuron.

## Introduction

Many sensory systems consist of repeated circuit units that map stimuli from the outside world onto sequential processing layers (Luo and Flanagan, 2007). It is critical that both absolute and relative neuronal numbers are carefully controlled for these circuits to assemble with topographic correspondence across processing layers. Neuronal numbers can be set by controlling how many progeny a neural stem cell produces, or by regulating how many neural progeny survive (Hidalgo and ffrench-Constant, 2003; Miguel-Aliaga and Thor, 2009). To investigate other developmental strategies that set neuronal numbers, we used the highly ordered and repetitive Drosophila melanogaster visual system. Like vertebrate visual systems, the fly visual system is organised retinotopically into repeated modular circuits that process sensory input from unique points in space spanning the entire visual field (Hadjieconomou et al., 2011; Malin and Desplan, 2021).

Retinotopy between the compound eye and the first neuropil in the optic lobe, the lamina, is built during development. Photoreceptors are born progressively in the eye imaginal disc as a wave of differentiation sweeps across the tissue from posterior to anterior. Newly born photoreceptors express Hedgehog (Hh), which promotes further wave propagation (Treisman, 2013). They also express the epidermal growth factor (EGF), Spitz (Spi), which recruits additional photoreceptors into developing ommatidia (Treisman, 2013). As photoreceptors are born, their axons project into the optic lobe and induce the lamina, such that there is a corresponding lamina unit (or cartridge) for every ommatidium (Figure 1A; Hadjieconomou et al., 2011). Each cartridge is composed of five interneurons (L1-L5; named for the medulla layers they project to) and multiple glial subtypes (Fischbach and Dittrich, 1989; Hadjieconomou et al., 2011).

![Figure 1.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of the developing lamina. Photoreceptors (blue) drive lamina precursor cell (LPC; purple) birth from neuroepithelial cells (NEs; grey) and their assembly into columns of ~6 LPCs, which differentiate into the L1-L5 neurons (yellow) following an invariant spatio-temporal pattern. The ‘extra’ LPC is cleared by apoptosis (red X). Several glial types (magenta) associate with the lamina. (B) A cross-sectional view of an early pupal (0–5 hr after puparium formation; APF) optic lobe where hh-Gal4 drives UAS-CD8::GFP expression in photoreceptors (cyan). The pan-glial driver repo-QF2 drives QUAS-m.Cherry (magenta) in all glia. Embryonic lethal abnormal vision (Elav) (yellow) marks all neurons. (C) A cross-sectional view of an optic lobe with pan-glial expression of CD8::GFP stained for GFP (cyan), Dachshund (Dac) (magenta), Elav (yellow), and Horseradish Peroxidase (HRP; axons; white). (D) Pan-glial expression of two copies of EGFRDN stained for Dac (magenta), Elav (yellow), and HRP (white). (E) xgO-specific expression of CD8::GFP stained for GFP (cyan), Dac (magenta), Elav (yellow), and HRP (white). (F) xgO-specific expression of two copies of EGFRDN and CD8::GFP stained for GFP (cyan), Dac (magenta), Elav (yellow), and HRP (white). The number of Elav+ cells in proximal row (L5s) decreased (empty arrowhead) relative to control (E). (G,H) HRP (white) and L-neuron-type-specific markers Sloppy paired 2 (Slp2) (cyan), Brain-specific homeobox (Bsh) (yellow), and Seven-up (Svp) (magenta) in (G) control xgO>lacZ optic lobe and (H) xgO>2xEGFRDN. L2s and L3s express Slp2; L1s express Slp2 and Svp; L4s express Bsh and L5s express Bsh and Slp2. (I) Quantification of the number of L-neuron types per column for control and xgO>2xEGFRDN. Only L5 neurons were decreased significantly (pL5<0.0001; Mann-Whitney U-test. Ns indicated in parentheses. Boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median). Scale bar = 20 μm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic of the developing lamina and associated glial types (green; labelled). (B) A perineurial glia-specific Gal4 drives expression of myr.GFP stained for GFP (cyan), Dachshund (Dac) (magenta), and Horseradish Peroxidase (HRP) (white). (C) Perineurial glia-specific expression of EGFRDN stained for Embryonic lethal abnormal vision (Elav) (yellow) and HRP (white). L5 differentiation was not affected. (D) A subperineurial glia-specific Gal4 drives expression of myr.GFP stained for GFP (cyan), Dac (magenta), and HRP (white). (E) Suberineurial glia-specific expression of EGFRDN stained for Elav (yellow) and HRP (white). L5 differentiation was not affected. (F) A cortex glia-specific Gal4 drives expression of myr.GFP stained for GFP (cyan), Dac (magenta), and HRP (white). (G) Cortex glia-specific expression of EGFRDN stained for Elav (yellow) and HRP (white). L5 differentiation was not affected. (H) An epithelial and marginal glia (eg+mg) specific Gal4 drives expression of myr.GFP stained for GFP (cyan), Dac (magenta), and HRP (white). (I) Epithelial and marginal glia-specific expression of EGFRDN stained for Elav (yellow) and HRP (white). L5 differentiation was not affected. (J) A wrapping glia- and xgO-specific Gal4 drives expression of myr.GFP stained for GFP (cyan), Dac (magenta), and HRP (white). (K) Wrapping glia- and xgO-specific expression of EGFRDN stained for Elav (yellow) and HRP (white). L1-L4 and L5 differentiation were disrupted as observed by the lack of Elav+ cells in the lamina. (L) A chiasm glia (xgO and xginner) specific Gal4 drives expression of myr.GFP stained for GFP (cyan), Dac (magenta), and HRP (white). (M) Chiasm glia-specific expression of EGFRDN stained for Elav (yellow) and HRP (white). L1-L4 differentiation proceeded normally but L5 differentiation was disrupted as observed by the lack of Elav+ cells in the proximal lamina. (N) Gal80ts-restricted Gal4 expression in xgO, driving EGFRDN during lamina development (see Figure 3—source data 1) stained for Dac (magenta), Elav (yellow), and HRP (white). L5 neurons were dramatically reduced. (O,P) LifeAct-GFP expression driven in xgO in (O) controls and (P) when two copies of EGFRDN are co-expressed. In both conditions, the fine processes from the xgO are present. (Q) Quantification of xgO numbers in control xgO>LifeAct-GFP+2xlacZ and xgO>LifeAct GFP+2xEGFRDN. p>0.05; Mann-Whitney U-test. Ns indicated in parentheses. (R) Quantification of the length of xgO fine processes in control xgO>LifeAct-GFP+2xlacZ and xgO>LifeAct GFP+2xEGFRDN. p>0.05; Unpaired t-test. Ns indicated in parentheses. (S) Wild-type adult optic lobe stained for POU domain motif 3 (Pdm3) (L5 marker) (Tan et al., 2015), Bruchpilot (Brp; marks neuropils) and Elav (yellow). (T) xgO>2xEGFRDN adult optic lobe stained for Pdm3 (L5 marker) (Tan et al., 2015), Bruchpilot (Brp; marks neuropils) and Elav (yellow). Pdm3+ cells (L5s) are reduced dramatically. Scale bar = 20 μm. For all quantifications boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median.

Lamina induction is a multi-step process triggered by photoreceptor-derived signals. Photoreceptor-derived Hh converts neuroepithelial cells into lamina precursor cells (LPCs), promotes their terminal divisions and drives the assembly of lamina pre-cartridges referred to as columns, that is, ensembles of ~6 post-mitotic LPCs stacked together and associated with photoreceptor axon bundles (Figure 1A and B; Huang and Kunes, 1998; Huang and Kunes, 1996; Sugie et al., 2010; Umetsu et al., 2006). Once assembled into columns, LPCs are diversified by graded Hh signalling along the distal-proximal axis of young columns (Bostock et al., 2022). They then differentiate into neurons following an invariant spatio-temporal pattern whereby the most proximal (bottom) and most distal (top) cells differentiate first into L5 and L2, respectively; differentiation then proceeds in a distal-to-proximal (top-to-bottom) sequence, L3 forming next, followed by L1, then L4 (Fernandes et al., 2017; Huang et al., 1998; Tan et al., 2015). The sixth LPC, located between L4 and L5, does not differentiate but instead is fated to die by apoptosis and is later cleared (Figure 1A; Apitz and Salecker, 2014). This spatio-temporal pattern of neuronal differentiation is driven in part by a population of glia called wrapping glia, which ensheathes photoreceptor axons and which induces L1-L4 neuronal differentiation via insulin/insulin-like growth factor signalling in response to EGF from photoreceptors (Fernandes et al., 2017). Intriguingly, L1-L4 neuronal differentiation can be disrupted by manipulating wrapping glia without affecting L5 differentiation (Fernandes et al., 2017). Indeed, the mechanisms that drive L5 differentiation are not known. Importantly, we do not understand how exactly five neuron types differentiate from six LPCs; in other words, how are lamina neuronal numbers set?

Here, we sought to determine the mechanisms that drive L5 differentiation as well as those that set neuronal numbers in the lamina. We found that a population of glia located proximal to the lamina, called the outer chiasm giant glia (xgO), induces L5 neuronal differentiation in response to EGF from photoreceptors. We showed that the xgO secrete multiple signals, including the EGF Spi and a type IV Collagen, Collagen type IV alpha 1 (Col4a1), which activate mitogen-activated protein kinase (MAPK) signalling in the most proximal row of LPCs (i.e., the row of LPCs nearest to xgO), thus driving their differentiation into L5s and promoting their survival. Further, we found that the ‘extra’ LPCs normally fated to die are specified with L5, but not L1-L4, identity. Since the most proximal row of LPCs are in closest proximity to the xgO, they receive differentiation cues from xgO first and differentiate into L5s. In turn, these newly induced L5s secrete high levels of Argos (Aos), an antagonist of Spi (Freeman et al., 1992), to limit MAPK activity in the ‘extra’ LPCs thus preventing their differentiation, and leading to their death and clearance. Thus, we highlight a new mode by which neuronal numbers can be set – not only by regulating the number of neurons born or the number that survive, but also by regulating the number induced to differentiate from a larger pool of precursors. Altogether, our results indicate that the sterotyped pattern of neuronal differentiation and programmed cell death in the lamina are determined by the architecture of the developing tissue together with feedback from newly differentiating neurons.

## Results

### L5 neuronal differentiation requires EGF receptor activity in xgO

We showed previously that wrapping glia induce L1-L4 neuronal differentiation in response to EGF from photoreceptors, but that L5 differentiation was regulated independently by an unknown mechanism (Fernandes et al., 2017). We speculated that another glial population may be involved in inducing L5 differentiation in response to EGF from photoreceptors. To test this hypothesis, we blocked EGF receptor (EGFR) signalling in all glia using a pan-glial driver to express a dominant negative form of EGFR (Repo>EGFRDN). Although LPCs (Dac+ cells) still formed and assembled into columns, there was a complete block in lamina neuron differentiation as seen by the absence of the pan-neuronal marker, Embryonic lethal abnormal vision (Elav); that is, L5 differentiation was disrupted in addition to the differentiation of L1-L4 as expected (Figure 1C and D). Thus, EGFR activity in a glial population other than the wrapping glia is required for L5 neuronal differentiation.

Many glial types infiltrate the lamina (Figure 1—figure supplement 1A; Chotard and Salecker, 2007; Edwards et al., 2012). Therefore, we performed a screen using glia subtype-specific Gal4s to block EGFR signalling and determined what effect this manipulation had on L5s using Elav expression in the proximal lamina (Figure 1—figure supplement 1B-M; summarised in Supplementary file 1). Blocking EGFR signalling in the xgO led to a dramatic reduction in the number of L5s (Figure 1E and F). To rule out early developmental defects, we used a temperature-sensitive Gal80 (Gal80ts) and shifted animals from the permissive temperature to the restrictive temperature to limit EGFRDN expression in xgO to begin from the third larval instar, when lamina development initiates. This resulted in a similar loss of Elav positive cells in the proximal lamina as when EGFRDN was expressed continuously in the xgO, indicating that this phenotype is not due to an early defect in xgO (Figure 1—figure supplement 1N). XgO are located below the lamina plexus, often with just one or two glial cells spanning the entire width of the lamina. While xgO extend fine processes towards the lamina, they do not appear to contact LPCs or L5 neurons (Figure 1—figure supplement 1O). Importantly, blocking EGFR signalling in the xgO did not affect xgO numbers or morphology (Figure 1E and F, Figure 1—figure supplement 1O-R).

Since our screen used Elav expression in the proximal lamina to assess for the presence of L5s, we next examined lamina neuron-type markers to assess whether blocking EGFR activity in xgO affected L5 neurons specifically. We used antibodies against Sloppy paired 2 (Slp2), Brain-specific homeobox (Bsh), and Seven-up (Svp) in combination to distinguish lamina neuron types: L2s and L3s express Slp2 alone, L1s co-express Svp and Slp2, L4s express Bsh alone, and L5s co-express Bsh and Slp2 (Figure 1G; Fernandes et al., 2017; Hasegawa et al., 2013; Tan et al., 2015). We found that the number of L5 neurons decreased specifically, while the number of all the other neuron types were unaffected (Figure 1G–I; pL5 <0.0001, Mann-Whitney U-test). Finally, to test whether the absence of L5s simply reflected a developmental delay in differentiation, we examined adult optic lobes using a different L5 neuronal marker, POU domain motif 3 (Pdm3) (Tan et al., 2015). Similar to our results in the developing lamina, L5s were mostly absent in the adult lamina when EGFR was blocked in xgO compared with controls (Figure 1—figure supplement 1S, T; Nexp = 10; Nctrl = 11), indicating that the loss of L5s observed during development is not due to delayed induction. Thus, EGFR activity in xgO is required for L5 neuronal differentiation.

### LPCs that fail to differentiate as L5s are eliminated by apoptosis

The loss of L5 neurons when EGFR was blocked in xgO could be explained either by a defect in neuronal differentiation or by an earlier defect in LPC formation or recruitment to columns. To distinguish between these possibilities, we counted the number of LPCs per column when EGFR signalling was blocked in xgO compared to controls (Figure 2A–C). For these and later analyses we considered the youngest column located adjacent to the lamina furrow to be the first column, with column number (and age) increasing towards the posterior side (Figure 1A). In columns 1–4, there were no differences in the number of LPCs when EGFR was blocked in xgO, indicating that LPC formation and column assembly occurred normally (Figure 2C), supporting the hypothesis that in response to EGFR activity, xgO induce proximal LPCs to differentiate as L5s. Interestingly, the number of LPCs began to decrease in older columns (column 5 onwards) when EGFR signalling was blocked in xgO (Figure 2C; *p<0.05, ***p<0.0002, Mann-Whitney U-test). This observation suggested that undifferentiated LPCs in older columns were being eliminated. We wondered whether LPCs that failed to differentiate into L5s underwent apoptosis, similar to the ‘extra’ LPCs that undergo apoptosis in controls. We used an antibody against the cleaved form of Death caspase-1 (Dcp-1), an effector caspase, to detect apoptotic cells (Akagawa et al., 2015) and, indeed, observed a significant increase in the number of Dcp-1 positive cells in the lamina when EGFR signalling was blocked in the xgO (132.8 cells/unit volume±19.48 standard error of the mean) compared to controls (49.14 cells/unit volume±4.53) (Figure 2A–B and D, p<0.0005, Mann-Whitney U-test). Importantly, we observed Dcp-1 positive cells in the proximal row of the lamina (Figure 2B; Nexp = 20/20), which we never observed in controls (Figure 2A, Nctrl = 19/19). Altogether these results showed that EGFR activity in xgO induces the differentiation of L5 neurons, and proximal LPCs that fail to receive appropriate cues from xgO die by apoptosis.

![Figure 2.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig2-v2.jpg)

**Figure 2.:** (A) Control xgO>lacZ optic lobe stained for Death caspase-1 (Dcp-1) (cyan), Embryonic lethal abnormal vision (Elav) (yellow), and Horseradish Peroxidase (HRP) (white). Dcp-1+ cells were always observed just distal to the most proximal row of cells (L5s). (B) xgO>EGFRDN stained for Dcp-1 (cyan), Dachshund (Dac) (magenta), Elav (yellow), and HRP (white). Dcp-1 positive cells were observed in the most proximal row of LPCs as well as the row just distal to these. (C) Quantification of the number of LPCs/column (i.e., Dac+ cells/column) for control and xgO>EGFRDN. *p<0.05, ****p<0.0002; Mann-Whitney U-test. Ns indicated in parentheses. (D) Quantification of the number of Dcp-1 positive cells in (A) compared to (B). ***p<0.0005, Mann-Whitney U-test. Ns indicated in parentheses. Boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median. Scale bar = 20 μm.

### xgO respond to EGF from photoreceptors and secrete multiple ligands to induce MAPK-dependent neuronal differentiation of L5s

Since EGF from photoreceptors triggers EGFR activity in wrapping glia (Fernandes et al., 2017), we tested whether photoreceptor-derived EGF contributed to activating EGFR in xgO also. Spi is initially produced as an inactive transmembrane precursor (mSpi) that needs to be cleaved into its active secreted form (sSpi) (Tsruya et al., 2002). This requires the intracellular trafficking protein Star and Rhomboid proteases (Tsruya et al., 2002; Urban et al., 2002; Yogev et al., 2008). We took advantage of a mutant for rhomboid 3 (rho3) in which photoreceptors are specified but cannot secrete EGF from their axons (Yogev et al., 2010), resulting in failure of L1-L4 neurons to differentiate along with a significant decrease in the number of L5s (Figure 3A and C; prho3 <0.0001; one-way ANOVA with Dunn’s multiple comparisons test) (Fernandes et al., 2017; Yogev et al., 2010). This result suggested that EGFR signalling in the xgO could be activated by EGF secreted by photoreceptor axons. To test this hypothesis, we restored expression of wild-type Rho3 only in photoreceptors in rho3 mutant animals using a photoreceptor-specific driver (GMR-Gal4). Rho3 function in photoreceptors was sufficient to fully rescue not only L1-L4 neuronal differentiation, as previously reported (Yogev et al., 2010), but also L5 neuronal differentiation (Figure 3B and C; one-way ANOVA with Dunn’s multiple comparisons test). Since photoreceptor-derived EGF was insufficient to induce L5 neuronal differentiation when EGFR signalling was blocked in xgO (Figure 1F and H), together these results suggest that xgO likely respond to EGF from photoreceptors and relay these signals to induce differentiation of proximal LPCs into L5 neurons.

![Figure 3.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig3-v2.jpg)

**Figure 3.:** (A) GMR-Gal4-driven CD8::GFP expression in photoreceptors in a rho3PLLb background stained for GFP (white), Dachshund (Dac) (magenta), Embryonic lethal abnormal vision (Elav) (yellow). Few proximal Elav+ cells (L5s) were recovered in older columns only as previously published (Fernandes et al., 2017). (B) GMR-Gal4-driven Rho3 and CD8::GFP in a rho3PLLb background stained for GFP (white), Dac (magenta), Elav (yellow) showed that L5 neuronal differentiation was rescued (Elav+ cells in the proximal lamina). (C) Quantifications for number of L5 neurons/column in (A) and (B) compared to rho3PLLb heterozygotes (rho3/+). ****p<0.0001, one-way ANOVA with Dunn’s multiple comparisons test. Ns indicated in parentheses. (D,E) Control xgO>GFP optic lobes stained for (D) Dac (magenta), Elav (yellow), and Horseradish Peroxidase (HRP) (white) or (E) HRP (white) and L-neuron-specific markers Sloppy paired 2 (Slp2) (cyan) and Brain-specific homeobox (Bsh) (yellow). (F,G) Gal4 titration control xgO>GFP + EGFRDN stained for (F) Dac (magenta), Elav (yellow), and HRP (white) or (G) HRP (white) and L-neuron-specific markers Slp2 (cyan) and Bsh (yellow). (H,I) Wild-type Spitz (Spi) (Spiwt) co-expression with EGFRDN specifically in xgO stained for (H) Elav (yellow) and HRP (white) or (I) HRP (white) and L-neuron-specific markers Slp2 (cyan) and Bsh (yellow). (J,K) Col4a1 co-expression with EGFRDN specifically in xgO stained for (J) Elav (yellow) and HRP (white) or (K) HRP (white) and L-neuron-specific markers Slp2 (cyan) and Bsh (yellow). (L,M) Gal4 titration control xgO>EGFRDN + 2xlacZ stained for (L) Elav (yellow) and HRP (white) or (M) HRP (white), Slp2 (cyan), and Bsh (yellow). (N,O) Wild-type Spiwt and Col4a1 co-expression with EGFRDN specifically in xgO. (N) stained for Elav (yellow) and HRP (white) or (O) HRP (white) and L-neuron-specific markers Slp2 (cyan) and Bsh (yellow). (P) Quantification of the number of L5s/column for the genotypes indicated compared to the appropriate titration control. For pntP1, spiwt, and Col4a1 co-expression with EGFRDN, the titration control is xgO>EGFRDN + GFP (**p<0.005, ***p<0.0005; ****p<0.0001; one-way ANOVA with Dunn’s multiple comparisons test. Ns indicated in parentheses). For spiwt and Col4a1 simultaneous co-expression with EGFRDN, the titration control is xgO>EGFRDN + 2xLacZ (****p<0.0001, Mann-Whitney U-test. Ns indicated in parentheses). (Q,R) Optic lobes stained for Slp2 and Bsh when xgO overexpress (Q) spiwt or (R) Col4a1. (S) Quantification of the number of L-neuron types/column in (Q) and (R) compared to controls, xgO>lacZ. (*p<0.05; **p<0.005; ***p<0.001; one-way ANOVA with multiple comparisons test). (T, U, V) Optic lobes stained for Slp2, Bsh, and HRP when xgO co-express Dcr-2 with (T) spiRNAi, (U) Col4a1RNAi, and (V) SpiRNAi and Col4a1RNAi simultaneously. (W) Quantifications of the number of L5s/column for genotypes indicated compared to the titration control xgO>Dcr-2+lacZ (*p<0.05, ****p<0.0001, one-way ANOVA with Dunn’s multiple comparisons test. Scale bar = 20 µm. For all quantifications boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A,B) Optic lobes stained for Embryonic lethal abnormal vision (Elav) (yellow), Repo (magenta), and double phosphorylated MAPK (dpMAPK) (cyan) in (A) xgO>lacZ controls and (B) with EGFRDN and lacZ expressed in xgO. dpMAPK levels decreased in the xgO (indicated by asterisk) and in cells in the proximal row of the lamina (indicated by arrowhead) when compared with xgO>lacZ controls. (C) Quantification of the number of L5s/column (based on Elav expression) when different ligands that can activate MAPK signalling were co-expressed with EGFRDN in the xgO (*p<0.05; **p<0.01; ***p<0.0005; ****p<0.0001; one-way ANOVA with Dunn’s multiple comparison test. Ns indicated in parentheses). (D) bnl>CD8::GFP showed GFP (cyan) expression in all cells in the optic lobe; Horseradish Peroxidase (HRP) (white). (E) ths>CD8::GFP showed GFP (cyan) expression in photoreceptors; HRP (white). (F) Collagen>CD8::GFP drove GFP (cyan) expression in xgO (arrowhead); Elav (yellow). (G) spiNP0289>CD8::GFP drove GFP (cyan) expression in xgO (arrowhead); Elav (yellow). (H, I) xgO>GFP lobes stained for GFP (cyan) and (H) spi mRNA (magenta) and (I) Col4a1 mRNA (magenta) by in situ hybridisation chain reaction (HCR). (J) xgO>EGFRDN + s.spi lobes stained for Elav (yellow), Repo (magenta), and dpMAPK (cyan). Inset shows a magnified view of the xgO nucleus. (K) Quantifications of nuclear:cytoplasmic ratios of dpMAPK mean fluorescence intensity (MFI) in the xgO in indicated genotypes (p<0.0005, one-way ANOVA with Dunn’s multiple comparisons test. Ns indicated in parentheses). (L) spi mRNA (magenta) detected by HCR in xgO>GFP + 2xEGFRDN lobes. (M) Quantification of spi MFI (arbitrary units) for (H and L). (p<0.05; Mann-Whitney U-test.). (N) Col4a1 mRNA (magenta) detected by HCR in xgO>GFP + 2xEGFRDN lobes. (O) Quantification of Col4a1 MFI (arbitrary units) for (I and N) (p<0.005; Mann-Whitney U-test). (P) Ddr>lacZ showed β-Galactosidase (β-Gal; cyan) expression in the lamina; HRP (white). (Q) Ddr mRNA (magenta) detected by HCR in wild-type lobes; DAPI (white). (R,S) Lobes stained for Dac (magenta), Elav (yellow), and dpMAPK (cyan) when (R) Spiwt is co-expressed with EGFRDN in xgO or (S) Col4a1 is co-expressed with EGFRDN in xgO. Arrowheads indicate Elav+ cells in the most proximal row. (T) Quantifications of nuclear:cytoplasmic ratios of dpMAPK MFI in the most proximal row of lamina precursor cells (LPCs) in indicated genotypes (**p<0.005, ****p<0.0001; one-way ANOVA with Dunn’s multiple comparisons test). Scale bar = 20 μm. For all quantifications boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) xgO>lacZ lobes stained for Death caspase-1 (Dcp-1) (cyan), Dachshund (Dac) (magenta), Embryonic lethal abnormal vision (Elav) (yellow), and Horseradish Peroxidase (HRP) (white). Dcp-1 positive cells (indicated by arrowhead) were located between L4s and L5s and corresponds to ‘extra’ LPCs which undergo apoptosis. (B) xgO>SpiRNAi + Col4aRNAi + Dcr-2 lobes stained for Dcp-1 (cyan), Dac (magenta), Elav (yellow), and HRP (white). Dcp-1 positive cells were observed in the proximal row of L5s (indicated by arrowhead) which were never observed in controls.

We next asked what signal(s) the xgO secrete to induce L5 differentiation. Previously, we showed that MAPK signalling is necessary and sufficient for neuronal differentiation in the lamina (Fernandes et al., 2017). Therefore, we reasoned that xgO-derived differentiation signal(s) must activate MAPK signalling through a receptor tyrosine kinase (RTK) in the proximal lamina. Indeed, blocking EGFR signalling in xgO led to reduced levels of double phosphorylated MAPK (dpMAPK) specifically in the proximal lamina (Figure 3—figure supplement 1A, B). The Drosophila genome encodes 22 ligands which activate 10 RTKs upstream of MAPK signalling (Sopko and Perrimon, 2013). To identify the signal(s) secreted by xgO, we misexpressed candidate ligands and screened for their ability to rescue the loss of L5s caused by blocking EGFR activity in the xgO. To validate this approach, we tested whether autonomously restoring transcriptional activity downstream of MAPK in xgO while blocking EGFR activity could rescue L5 differentiation. While blocking EGFR in xgO resulted in laminas containing 0.063±0.014 L5s per column, co-expressing PntP1 with EGFRDN in xgO rescued the number of L5s per column to 0.213±0.025 (Figure 3F, Figure 3—figure supplement 1C ****p<0.0001 compared to EGFRDN alone). We then screened 18 RTK ligands based on available reagents (Figure 3—figure supplement 1C). Four ligands, Spi, Branchless (Bnl), Thisbe (Ths), and Col4a1, produced statistically significant rescues when compared with the xgO>EGFRDN + CD8::GFP (Gal4 titration control) (Figure 3—figure supplement 1C; *p<0.05, **p<0.005, ***p<0.0005, ****p<0.0001 one-way ANOVA with Dunn’s multiple comparisons test). To eliminate false positive hits, we determined whether these ligands were expressed in xgO under physiological conditions. Using a previously validated bnl-Gal4 (Chen and Krasnow, 2014; Kamimura et al., 2006; Spéder and Brand, 2014; Tamamouna et al., 2021), we drove CD8::GFP expression and found that it was expressed in all cells of the optic lobe (Figure 3—figure supplement 1D), making it unlikely to be a viable hit. We found that a previously validated ths-Gal4 (Anllo and DiNardo, 2022; Wu et al., 2017) drove CD8::GFP expression in photoreceptors but not xgO (Figure 3—figure supplement 1E) consistent with previous reports (Franzdóttir et al., 2009). However, when we examined Col4a1 expression using a previously validated Gal4 enhancer trap (Hennig et al., 2006), we found that it drove CD8::GFP expression in xgO (Figure 3—figure supplement 1F). We also found that a spi-Gal4 (NP0289-Gal4; not previously validated) drove CD8::GFP expression in xgO, but not photoreceptors or other cell types where spi is also known to be expressed, suggesting that this Gal4 line may report spi expression partially (Figure 3—figure supplement 1G). To further substantiate these results we performed fluorescence in situ hybridisation chain reaction (HCR), a form of fluorescent in situ hybridisation (Choi et al., 2018; Choi et al., 2016; Duckhorn et al., 2022), and confirmed that spi and Col4a1 mRNAs were present in the xgO under physiological conditions (Figure 3—figure supplement 1H and I; see Materials and methods). This enabled us to narrow down our hits to two ligands: the EGF Spi and Col4a1, a type IV Collagen, which both rescued L5 differentiation resulting in laminas with 0.147±0.024 and 0.17±0.0197 L5s per column, respectively (Figure 3F–K and P pspi-wt <0.01 and pCol4a1 <0.0005, one-way ANOVA with Dunn’s multiple comparisons test; Figure 3—figure supplement 1C). Note that expressing either sSpi or wild-type (unprocessed) mSpi (referred to as Spiwt) in xgO rescued L5 numbers (Figure 3—figure supplement 1C), indicating that xgO are capable of processing mSpi into the active form (sSpi).

We ruled out the trivial explanation that the rescue of L5 numbers by Spi was caused by autocrine EGFR reactivation in the xgO, as Spi expression in xgO did not autonomously rescue dpMAPK nuclear localisation in xgO when EGFR signalling was blocked (Figure 3—figure supplement 1A, B, J, K). We then tested whether xgO express spi and Col4a1 downstream of EGFR activity. We measured spi and Col4a1 transcript levels using in situ HCR in controls and when we blocked EGFR signalling in xgO. Disrupting EGFR signalling in xgO resulted in a significantly reduced fluorescence signal for spi and Col4a1 transcripts in xgO compared with controls (Figure 3—figure supplement 1H and I, 1L-O; pspi <0.01, pCol4a1<0.005; Mann-Whitney U-test). Thus, xgO express spi and Col4a1 in response to EGFR activity.

Col4a1 is thought to activate MAPK signalling through its putative receptor, the Discoidin domain receptor (Ddr) (Sopko and Perrimon, 2013). We used a Gal4 enhancer trap in the Ddr locus (not previously validated) to drive CD8::GFP expression and observed that GFP was expressed in all LPCs (Figure 3—figure supplement 1P). We confirmed these results using in situ HCR, which also detected Ddr expression throughout the lamina (Figure 3—figure supplement 1Q). Spi activates EGFR (Sopko and Perrimon, 2013), which was shown to be expressed in LPCs previously (Huang et al., 1998). Thus, LPCs express the RTKs that make them competent to respond to the EGF Spi and Col4a1 produced by xgO. Moreover, expressing spi or Col4a1 in xgO in which EGFR signalling was blocked rescued dpMAPK signal in L5s, indicating that, when expressed in xgO, these ligands were sufficient to activate MAPK signalling in the proximal lamina (Figure 3—figure supplement 1R-T; **p<0.005, ****p<0.0001; one-way ANOVA with Dunn’s multiple comparisons test). Co-expressing Spi and Col4a1 in the xgO>EGFRDN background led to an enhanced and statistically significant rescue relative to individual ligand rescues alone, resulting in laminas with 0.267±0.025 L5s per column (Figure 3L–P; p<0.0001, Mann-Whitney U-test). We also tested whether these ligands could induce ectopic L5 differentiation when overexpressed in the xgO. Overexpressing either Spi or Col4a1 resulted in a 19%±1.8 (p<0.05) and a 24%±4 (p<0.005) increase in the number of L5s per column relative to controls, respectively (Figure 3Q–S). Thus, Spi and Col4a1 from xgO are sufficient to induce L5 differentiation.

Next, to test whether xgO-derived Spi and Col4a1 are normally required to induce L5 neuronal differentiation, we disrupted their expression specifically in xgO. We used RNA interference (RNAi) to knock down spi and Col4a1 expression both individually and simultaneously in xgO using previously validated lines (Chen et al., 2016; Csordás et al., 2020; Louradour et al., 2017; Morante et al., 2013; Pastor-Pareja and Xu, 2011). While knocking down spi led to a mild decrease in L5 numbers, which was not statistically significant, knocking down Col4a1 in the xgO led to a statistically significant decrease in L5s (0.78±0.03 L5s per column) relative to controls (0.92±0.02 L5s per column) (Figure 3T, U and W; *p<0.05 one-way ANOVA with Dunn’s multiple comparisons test). However, knocking down both spi and Col4a1 simultaneously in xgO led to a strong decrease in L5s (0.61±0.02 L5s per column; Figure 3V–W; ****p<0.0001, one-way ANOVA with Dunn’s multiple comparisons test). Under these conditions we also observed Dcp-1 positive apoptotic cells in the most proximal row of the lamina, which were never observed in controls (Figure 3—figure supplement 2) but were observed when L5 differentiation was blocked above (Figure 2B). Thus, xgO-derived Spi and Col4a1 are both necessary and sufficient to induce L5 differentiation. Altogether, we found that xgO secrete multiple factors that lead to activation of the MAPK cascade in the proximal lamina to induce differentiation of L5s.

### The ‘extra’ LPCs are specified as L5s though fated to die

We recently showed that a gradient of Hh signalling activity in lamina columns specifies L1-L5 identities such that high levels specify L2 and L3 (distal cell) identities, intermediate levels specify L1 and L4 (intermediate cell) identities, and low levels specify L5 (proximal cell) identity (Bostock et al., 2022). Since overexpressing spi and Col4a1 in the xgO resulted in ectopic L5 neurons, we wondered what the source of these ectopic cells was. We quantified other lamina neuron types when either spi or Col4a1 was overexpressed in xgO and found no decrease in the number of L1-L3s (Slp2-only expressing cells) or L4s (Bsh-only expressing cells) per column compared to controls (Figure 3S). Thus, ectopic L5s were not produced at the expense of other lamina neuron types. In wild-type optic lobes, each lamina column contains an ‘extra’ LPC, which is located immediately distal to the LPC fated to differentiate as an L5. These ‘extra’ LPCs do not differentiate but instead undergo apoptosis and are eliminated (Figures 2A and 4A). We hypothesised that though fated to die, ‘extra’ LPCs are specified with L5 identity through low Hh signalling activity in the proximal lamina, and that the overexpression of Spi and Col4a1 in xgO generated ectopic L5s by inducing differentiation and survival of the ‘extra’ LPCs. To test this hypothesis, we forced neuronal differentiation throughout the lamina by expressing an activated form of MAPK (MAPKACT) (Figure 4—figure supplement 1A-D) or by overexpressing the MAPK transcriptional effector, Pointed P1 (PntP1), in the lamina (Figure 4A–D) . As reported previously, hyperactivating MAPK signalling in the lamina led to premature neuronal differentiation: instead of sequential differentiation of L1-L4, seen as a triangular front, most lamina columns differentiated simultaneously ( (Figure 4) , Figure 4—figure supplement 1A, C; Fernandes et al., 2017). We observed no LPCs that remained undifferentiated (Dac+ and Elav-) past lamina column 5, including the row of cells that normally correspond to the ‘extra’ LPCs (Figure 4C, Figure 4—figure supplement 1A, C). Importantly, we also observed a concomitant decrease in cleaved Dcp-1 positive cells (Figure 4C and E ; p<0.0001, Mann-Whitney U-test), suggesting that forcing the ‘extra’ LPCs to differentiate blocked their death.

![Figure 4.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig4-v2.jpg)

**Figure 4.:** (A) Wild-type optic lobes stained for Dachshund (Dac) (magenta), Horseradish Peroxidase (HRP) (white), Embryonic lethal abnormal vision (Elav) (yellow), and cleaved Death caspase-1 (Dcp-1) (cyan). (B) Wild-type optic lobes stained for HRP (white) and L-neuron-type-specific markers sloppy paired 2 (Slp2) (cyan) and brain-specific homeobox (Bsh) (yellow). (C, D) Optic lobes with lamina-specific overexpression of PntP1 stained as in (A) and (B), respectively. (C) Fewer Dcp-1 positive cells were recovered compared with controls. (D) Roughly two rows of Slp2 and Bsh co-expressing cells (L5s) were recovered (arrowheads). (E) Quantification of the number of Dcp-1 positive cells in (B) compared with control Laminats>lacZ (Figure 4—figure supplement 1A) (p<0.0001; Mann-Whitney U-test). (F) Quantification of the number of L-neuron types per column based on Slp2 and Bsh expression from column 7 onwards shows an increase in the number of L5s/column in Laminats>PntP1 compared with controls; p<0.0001; Mann-Whitney U-test. (G) Same as (F) but normalised to the mean of the control. The number of L5s/column in Laminats>PntP1 increase ~1.2-fold relative to controls; p<0.0001; Mann-Whitney U-test. Ns indicated in parentheses. Scale bar = 20 µm. For all quantifications boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A,B) Control Laminats>lacZ optic lobes stained for (A) Dachshund (Dac) (magenta), Horseradish Peroxidase (HRP) (white) and Embryonic lethal abnormal vision (Elav) (yellow), and (B) and L-neuron-type-specific markers Sloppy paired 2 (Slp2) (cyan) and Brain-specific homeobox (Bsh) (yellow). (C,D) Laminats>MAPKACT optic lobes stained for (C) Dac (magenta), HRP (white), and Elav (yellow), and (D) L-neuron-type-specific markers Slp2 (cyan) and Bsh (yellow). Ectopic Slp2 and Bsh co-expressing cells (L5s) were observed (arrowheads). (E) Quantification of the number of Elav+ cells per lamina column as a function of column number (age) in wild-type animals. Columns were fully differentiated (five Elav+ cells) by column 7. Boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median. Scale bar = 20 μm.

Next, we examined the distribution of lamina neuron types when we forced neuronal differentiation. We often observed two rows of cells co-expressing Slp2 and Bsh in the proximal lamina (Figure 4B and D, Figure 4—figure supplement 1B, D), indicating the presence of ectopic L5s. To distinguish between premature and ectopic differentiation, we quantified the number of lamina neuron types (L1-L3, L4, and L5) per column in older columns (column 7 onwards, once mature columns were observed in controls, Figure 4—figure supplement 1E). While there was no significant difference between the average number of L1-L3s or L4s per column, the average number of L5s per column was ~1.4-fold higher in laminas in which differentiation was ectopically induced compared with controls, that is, they contained 1.4±0.08 L5s per column compared to 1.00±0.05 L5s per column in controls (Figure 4B, D and F–G; p<0.0001, Mann-Whitney U-test). Thus, hyperactivating MAPK signalling in the lamina drove ectopic differentiation of L5 neurons. Importantly, ectopic L5s were only observed in the proximal but never in the distal lamina (Figure 4D, N=18/18; Figure 4—figure supplement 1D, N=9/9). Taken together, the absence of cell death in the row distal to L5s and the presence of ectopic L5s in this row indicate that hyperactivating MAPK signalling induces the ‘extra’ LPCs to differentiate into L5s. Thus, the ‘extra’ LPCs are specified as L5s though fated to die normally. These data are consistent with our work showing that lamina precursors are specified by Hh signalling prior to differentiation and that the most proximal cells, which experience the lowest levels of Hh pathway activity and are specified as L5s (Bostock et al., 2022). Importantly, the presence of ectopic L5s when differentiation is induced demonstrates that more LPCs are specified as L5s than differentiate normally.

### Newly born L5 neurons inhibit differentiation of distal neighbours to set neuronal number

If the two most proximal cells in each lamina column are both specified as L5s, how then is L5 differentiation limited to only the most proximal row in response to diffusible signals secreted by xgO? We tested whether the ‘extra’ LPCs differentiated as L5s when apoptosis was blocked in animals mutant for Death regulator Nedd2-like caspase (Dronc), an initiator caspase essential for caspase-dependent cell death (Fuchs and Steller, 2011). Cleaved Dcp-1 was absent in homozygous DroncI24 animals confirming that apoptosis was blocked (Figure 5A; N=26/26; with full penetrance). Indeed, we detected cells that were positive for the lamina marker Dachshund (Dac) but negative for the pan-neuronal marker Elav between L1-L4 and L5 neurons past column 5, which were never observed in controls (Figure 5A compared to Figure 4A; N=13/13; with full penetrance). These cells did not express lamina neuron-type markers Slp2 or Bsh, which L5s co-express and which individually label L1-L3s and L4s, respectively (Figure 5B and C). Thus, although the ‘extra’ LPCs were retained when apoptosis was blocked, they did not differentiate into neurons.

![Figure 5.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig5-v2.jpg)

**Figure 5.:** (A) DroncI24 optic lobes stained for Death caspase-1 (Dcp-1) (cyan), Dachshund (Dac) (magenta), Embryonic lethal abnormal vision (Elav) (yellow), and Horseradish Peroxidase (HRP) (white). No Dcp-1 positive cells were recovered and Dac positive cells between L1-L4s and L5s persisted into the oldest columns (asterisk). (B) DroncI24 optic lobes stained for L-neuron-type-specific markers Sloppy paired 2 (Slp2) (cyan) and Brain-specific homeobox (Bsh) (yellow). A space (negative for both markers; asterisk) was present between L4s and L5s. (C) Quantifications for number of L5s/column in DroncI24 optic lobes compared to controls (DroncI24/+) (p>0.05, Mann-Whitney U-test. Ns indicated in parentheses). (D,E) aos-lacZ expression in the lamina with (D) β-Galactosidase (β-Gal) (cyan), Repo (magenta), Elav (yellow), HRP (white), and with (E) β-Gal (magenta) and L-neuron-type-specific markers Slp2 (cyan), Bsh (yellow), as well as HRP (white). (F) An L5-specific Gal4 was used to drive expression of Dcr-2 and lacZ in control lobes stained for Slp2 (cyan), Bsh (yellow), and HRP (white). (G) Optic lobes stained for HRP (white), Slp2 (cyan), and Bsh (yellow) when Dcr-2 and aosRNAi were expressed in developing L5 neurons specifically, which led to an increase in the number of Slp2 and Bsh co-expressing cells (L5s; asterisks). (H) Quantification of the number of L5s/column for (F) and (G). ***p<0.0005; Mann-Whitney U-test. Ns indicated in parentheses. For all quantifications boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median. Scale bar = 20 µm.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) An L5-specific driver was used to drive the expression of GFP (magenta) in the lamina; Horseradish Peroxidase (HRP) (white) and L-neuron-type-specific markers Sloppy paired 2 (Slp2) (cyan) and Brain-specific homeobox (Bsh) (yellow). (B) β-Galactosidase (β-Gal) mean fluorescence intensity (MFI) quantifications in the proximal row of L5s as a function of column number (age) in aos-lacZ lobes. β-Gal MFI is low in young columns and increases in older columns (from column 5). Boxes indicate the lower and upper quartiles; the whiskers represent the minimum and maximum values; the line inside the box indicates the median. Scale bar = 20 μm.

We observed ectopic L5s only when all LPCs were forced to differentiate, bypassing the need for differentiation signals from glia, but not when apoptosis was blocked (Figure 4, Figure 4—figure supplement 1A-D, and Figure 5A–C). This suggests that the ‘extra’ LPCs, though specified as L5s, did not receive differentiation signals from xgO in Dronc mutants or in the wild-type, where failing to differentiate they were eliminated by apoptosis. How are only half of the LPCs specified as L5s chosen to differentiate in an invariant manner? The most proximal row of LPCs fated to differentiate into L5s is the row nearest to xgO, and therefore, the first to receive differentiation signals. We speculated that newly induced L5s may then limit the ability of more distal LPCs to differentiate, by preventing MAPK activation in neighbouring cells. Aos is a transcriptional target of MAPK signalling and a secreted antagonist of the EGF Spi (Freeman et al., 1992; Golembo et al., 1996). We wondered if newly induced L5s secrete Aos to limit differentiation signals from xgO. To test this hypothesis, we examined argos (aos) expression with an enhancer trap in the aos locus, aosW11. aos-lacZ (aosW11/+) was expressed in xgO and differentiating lamina neurons, with the highest levels detected in L5s (Figure 5D–E). Interestingly, we also noted ectopic L5s in the laminas of aosW11 heterozygotes, which could be the result of decreased Aos expression, as aosW11 is a hypomorphic loss-of-function allele (Figure 5E). These observations suggested that Aos could act in L5s as a feedback-induced sink for Spi to limit further differentiation in columns. To test this hypothesis, we knocked down aos by RNAi using a driver expressed specifically in developing L5s (Jenett et al., 2012; Figure 5G). We observed a statistically significant ~1.2-fold increase in the number of L5s relative to controls, that is, 0.99±0.02 L5s per column compared to 0.83±0.01 L5s per column in controls (Figure 5F–H; p<0.0005, Mann-Whitney U-test). Altogether, our data indicate a model in which xgO induce MAPK activity in the most proximal LPCs, resulting in their differentiation and in the production of the feedback inhibitor Aos. In turn, Aos limits further differentiation in the column by fine-tuning the availability of the differentiation signal Spi, which ensures that only one L5 differentiates per column, and determines the final number of neurons in each lamina column.

## Discussion

Appropriate circuit formation and function require that neuronal numbers are tightly regulated. This is particularly important for the visual system, which is composed of repeated modular circuits spanning multiple processing layers. In Drosophila, photoreceptors induce their target field, the lamina, thus, establishing retinotopy between the compound eye and the lamina (Huang and Kunes, 1996). Each lamina unit or column in the adult is composed of exactly five neurons; however, columns initially contain six LPCs. The sixth, or ‘extra’, LPC, invariantly located immediately distal to the differentiating L5 neuron, is fated to die by apoptosis. These ‘extra’ LPCs did not differentiate when apoptosis was blocked (Figure 5A and B) but generated ectopic L5s when forced to differentiate (Figure 4D and Figure 4—figure supplement 1D). Although we cannot rule out that preventing death using Dronc mutants may mis-specify the ‘extra’ cells and prevent them from differentiating, it is more likely that these ‘extra’ cells are specified as L5s, but that other mechanisms restricted their differentiation in Dronc mutants, as other lamina neuron types differentiated normally (Figure 5B). Thus, twice as many LPCs appear to be specified as L5s than undergo differentiation normally, which implies that a selection process to ensure that the correct number of L5s develop is in place.

The developmental strategies described thus far for setting neuronal number do so by regulating proliferation of precursors and/or survival of differentiated neurons (Hidalgo and ffrench-Constant, 2003). Here, we have defined a unique strategy whereby L5 neuronal numbers are set by regulating how many precursors from a larger pool are induced to differentiate, followed by programmed cell death of the excess precursors. We showed that a glial population called xgO, which are located proximal to the lamina, secrete at least two ligands (Spi, Col4a1) that activate MAPK signalling in LPCs to induce their differentiation (Figure 3, Figure 3—figure supplement 1). The tissue architecture is such that secreted signals from the xgO reach the most proximal row of LPCs first, and therefore these precursors differentiate first. Upon differentiation, these newly induced neurons secrete the Spi antagonist Aos to limit the available pool of Spi. As a result, the MAPK pathway is not activated in the ‘extra’ L5 LPCs, preventing them from differentiating into L5 neurons (Figure 6). Intriguingly, L5 neuronal differentiation in the youngest columns of the lamina proceeds despite Aos secretion by newly induced L5s. We noted that differentiating L5s expressed aos (based on aos-lacZ) at low levels initially and increased expression gradually till it plateaued from column 5 onwards (Figure 5E and Figure 5—figure supplement 1B). This delay in high aos expression may thus enable differentiation of the youngest LPCs, while still inhibiting differentiation of the row immediately distal. In sum, the structure of the tissue together with feedback from newly induced neurons set neuronal number by limiting which and, therefore, how many LPCs are induced to differentiate.

![Figure 6.](https://cdn.elifesciences.org/articles/78092/elife-78092-fig6-v2.jpg)

**Figure 6.:** In our model of lamina neuronal differentiation, lamina precursor cells (LPCs) are prepatterned with unique identities based on their positions within a column, such that the two most proximal cells are specified with L5 identity. Epidermal growth factor (EGF) from photoreceptors activates EGF receptor (EGFR) signalling in wrapping glia, which induce L1-L4 differentiation, and in xgO, which induce L5 differentiation. Only a subset of the LPCs specified as L5s differentiate (i.e., those in the proximal row). We propose that this selective neuronal induction of L5s is due to tissue architecture and feedback from the newly born L5s, which limit available EGF (Spitz [Spi]) by secreting the antagonist Argos (Aos).

### Coordinating development through glia

We have shown that in addition to the wrapping glia (Fernandes et al., 2017), another population of glia, the xgO, also receive and relay signals from photoreceptors to induce neuronal differentiation in the lamina (Figure 1E–F). This is the first functional role ascribed to xgO. Remarkably, xgO are born from central brain DL1 type II neuroblasts and migrate into the optic lobes to positions below the developing lamina (Ren et al., 2018; Viktorin et al., 2013). This underscores an extraordinary degree of coordination and interdependence between the compound eye, optic lobe, and central brain. Photoreceptor signals drive wrapping glial morphogenesis and infiltration into the lamina (Franzdóttir et al., 2009), thus setting the pace of L1-L4 neuronal differentiation (Fernandes et al., 2017). Defining the signals that enable xgO to navigate the central brain and optic lobe will be a critical contribution to our understanding of how development is coordinated across brain regions.

### Tissue architecture sets up stereotyped programmed cell death

In both vertebrate and invertebrate developing nervous systems, programmed cell death is thought to come in two broad flavours: first as an intrinsically programmed fate whereby specific lineages or identifiable progenitors, neurons, or glia undergo stereotyped clearance (Hidalgo and ffrench-Constant, 2003; Miguel-Aliaga and Thor, 2009; Pinto-Teixeira et al., 2016; Yamaguchi and Miura, 2015) and second as an extrinsically controlled outcome of competition among neurons for limited target-derived trophic factors, which adjust overall cell numbers through stochastic clearance (also known as the neurotrophic theory) (Davies, 2003; Hidalgo and ffrench-Constant, 2003; Miguel-Aliaga and Thor, 2009; Yamaguchi and Miura, 2015). In the lamina, although the LPCs eliminated by programmed cell death are identifiable and the process stereotyped, it does not appear to be linked to an intrinsic programme. Rather, the predictable and stereotyped nature of apoptosis and differentiation are a consequence of stereotyped responses to extrinsic signalling determined by the architecture of the tissue. Thus, our work highlights that stereotyped patterns of apoptosis can arise from extrinsic signalling, suggesting a new mode to reliably pattern development of the nervous system.

In many contexts, neurotrophic factors promote cell survival by activating MAPK signalling (Ballif and Blenis, 2001; Park and Poo, 2013). In the lamina, MAPK-induced neuronal differentiation and cell survival appear intimately linked. LPCs that do not activate MAPK signalling sufficiently do not differentiate and are eliminated by apoptosis, likely through regulation of the proapoptotic factor Head involution defective, which has been described extensively in flies (Bergmann et al., 2002; Bergmann et al., 1998; Kurada and White, 1998). Thus, here the xgO-secreted ligands Spi and Col4a1, which activate MAPK, appear to be functioning as differentiation signals as well as trophic factors. Col4a1, in particular, may perform dual roles by promoting MAPK activity directly through its receptor Ddr, and perhaps also by limiting Spi diffusivity to aid in localising MAPK activation.

It will be interesting to determine whether the processes described here represent conserved strategies for regulating neuronal number. Certainly, given the diversity of cell types and structural complexity of vertebrate nervous systems, exploiting tissue architecture would appear to be an effective and elegant strategy to regulate cell numbers reliably and precisely.

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
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Canton S</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 64349</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Bacc-GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 36349</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>ey-Gal80</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 35822</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Gal80ts</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 7108</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>DroncI24</td>
      <td>PMID:15800001</td>
      <td></td>
      <td>Gift from M Amoyel</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>R27G05-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 48073</td>
      <td>Lamina Gal4</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>R25A01-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 49102</td>
      <td>xgO Gal4</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>R64B07-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 71106</td>
      <td>Larval L5 Gal4</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>hh-gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 67493</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Repo-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 7415</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-CD8::GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 32187</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-nls.lacZ</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 3956</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>GMR-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 9146</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Repo-QF</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 66477</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>NP6293-Gal4</td>
      <td>Kyoto Stock Center</td>
      <td>DGRC: 105188</td>
      <td>Perineural Glia</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>NP2276-Gal4</td>
      <td>Kyoto Stock Center</td>
      <td>DGRC: 112853</td>
      <td>Subperineur-al Glia</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>R54H02-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 45784</td>
      <td>Cortex Glia</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>R10C12-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 47841</td>
      <td>Epithelial and marginal glia</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Mz97-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 9488</td>
      <td>Wrapping glia and xgO</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>R53H12-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 50456</td>
      <td>Chiasm glia</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>spiNP0289-Gal4</td>
      <td>Kyoto Stock Center</td>
      <td>DGRC: 112828</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Cg-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 7011</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>bnlNP2211-Gal4</td>
      <td>Kyoto Stock Center</td>
      <td>DGRC: 112825</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>thsMI07139-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 77475</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>rho3PLLb, UAS-CD8::GFP</td>
      <td>PMID:20957186</td>
      <td></td>
      <td>Gift from B Shilo</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-rho3-3xHA</td>
      <td>PMID:20957186</td>
      <td></td>
      <td>Gift from B Shilo</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>aosw11</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 2513</td>
      <td>aos-lacZ</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>BaccGFP;10xQUAS-6xmCherry-HA</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 55270</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>10xUAS-myrGFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 32197</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-LifeAct-GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 35544</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Dicer2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 24650</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>;UAS-EGFRDN; UAS-EGFRDN</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 5364</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-rlSEM</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 59006</td>
      <td>rlSEM = MAPKACT</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-PntP1</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 869</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-jeb</td>
      <td>PMID:21816278</td>
      <td></td>
      <td>Gift from A Gould</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Col4a1EY11094</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 20661</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Cg25cRFP</td>
      <td>PMID:26090908</td>
      <td></td>
      <td>Gift from A FranzCg25c=Col4a1</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-wnt5</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 64298</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-s.spi</td>
      <td>PMID:7601354</td>
      <td></td>
      <td>Gift from B Shilo</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-m.spi::GFP-myc (II)</td>
      <td>PMID:11799065</td>
      <td></td>
      <td>Gift from B Shilom.spi=spiwt</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-m.spi::GFP-myc (III)</td>
      <td>PMID:11799065</td>
      <td></td>
      <td>Gift from B Shilom.spi=spiwt</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-grk.sec</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 58417</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-vnEPgy</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 58498</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-krn-3xHA</td>
      <td>FlyORF</td>
      <td>F002754</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-bnl</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 64232</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Ilp1</td>
      <td>PMID:12176357</td>
      <td></td>
      <td>Gift from P Leopold</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Ilp6</td>
      <td>PMID:20059956</td>
      <td></td>
      <td>Gift from P Leopold</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Pvf1XP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 19632</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Pvf2XP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 19631</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-Wnt4EPgy2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 20162</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-boss-3xHA</td>
      <td>FlyORF</td>
      <td>F001365</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>SAM.dCas9.Trk</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 81322</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>SAM.dCas9.Pvf3</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 81346</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>SAM.dCas9.ths</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 81347</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>SAM.dCas9.pyr</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 81330</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>DdrCR01018-Gal4</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 81157</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>spiRNAi</td>
      <td>Vienna Drosophila Stock Center</td>
      <td>GD3922</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Col4a1RNAi</td>
      <td>Vienna Drosophila Stock Center</td>
      <td>GD28369</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>aosRNAi</td>
      <td>Vienna Drosophila Stock Center</td>
      <td>GD47181</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Dac2-3(mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>mAbdac2-3</td>
      <td>1:20</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Repo(mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>8D12</td>
      <td>1:20</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Elav(rat monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>7E8A10</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Elav(mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>9F8A9</td>
      <td>1:20</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Svp(mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>6F7</td>
      <td>1:50</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Slp2(guinea pig polyclonal)</td>
      <td>PMID:23783517</td>
      <td>C Desplan</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Bsh (Rabbit polyclonal)</td>
      <td>PMID:33149298</td>
      <td>C Desplan</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Dcp-1(Rabbit polyclonal)</td>
      <td>Cell Signaling</td>
      <td>9578</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Brp(guinea pig polyclonal)</td>
      <td></td>
      <td>C Desplan</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-phospho-p44/42-MAPK (Thr202/Tyr204)(Rabbit polyclonal)</td>
      <td>Cell Signaling</td>
      <td>9101</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-β-galactosidase(mouse monoclonal)</td>
      <td>Promega</td>
      <td>#Z3781</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-β-galactosidase(chicken polyclonal)</td>
      <td>abcam</td>
      <td>9361</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP(chicken polyclonal)</td>
      <td>EMD Millipore</td>
      <td>GFP-1010</td>
      <td>1:400</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Pdm3(rat polyclonal)</td>
      <td>PMID:22190420</td>
      <td>C Desplan</td>
      <td>1:20</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-RFP(chicken polyclonal)</td>
      <td>Rockland</td>
      <td>#600-901-379s</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP (rabbit polyclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>#A6455</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>AlexaFluor405-conjugated Goat Anti-HRP (goat polyclonal)</td>
      <td>Jackson Immunolabs</td>
      <td>123-475-021</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>AlexaFluorCy3- conjugated Goat Anti-HRP (goat polyclonal)</td>
      <td>Jackson Immunolabs</td>
      <td>11 23-165-021</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>AlexaFluor647- conjugated Goat Anti-HRP (goat polyclonal)</td>
      <td>Jackson Immunolabs</td>
      <td>123-605-021</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Antisense probe pairs for in situ Hybridisation chain reaction</td>
      <td>This study. ‘Prasad et al. HCR Probe Sequences.xls’</td>
      <td>DNA Oligos</td>
      <td>Figure 3—source data 1</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RStudio</td>
      <td>RStudio</td>
      <td>R version 4.0.3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism 9</td>
      <td>GraphPad Prism 9</td>
      <td>GraphPad Prism version 9.4.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Photoshop</td>
      <td>Adobe Photoshop</td>
      <td>Adobe Photoshop 2021</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Illustrator</td>
      <td>Adobe Illustrator</td>
      <td>Adobe Illustrator 2021</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Imaris</td>
      <td>Imaris</td>
      <td>Imaris ×64-9.5.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FiJi, ImageJ</td>
      <td>PMID:22743772</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Amplification Buffer</td>
      <td>Molecular Instruments</td>
      <td>BAM02224</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Wash Buffer</td>
      <td>Molecular Instruments</td>
      <td>BPW02124</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Hybridisation Buffer</td>
      <td>Molecular Instruments</td>
      <td>BPH02224</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Amplifier B3-H1-546</td>
      <td>Molecular Instruments</td>
      <td>S030724</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Amplifier B3-H2-546</td>
      <td>Molecular Instruments</td>
      <td>S031024</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Amplifier B3-H1-647</td>
      <td>Molecular Instruments</td>
      <td>S040124</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCR Amplifier B3-H2-647</td>
      <td>Molecular Instruments</td>
      <td>S040224</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Para-formaldehyde</td>
      <td>Thermo Fisher Scientific</td>
      <td>28908</td>
      <td>4% solution</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAPI stain</td>
      <td>Sigma</td>
      <td>D9542-1MG</td>
      <td>(1 µg/mL)</td>
    </tr>
  </tbody>
</table>

### Drosophila stocks and maintenance

Drosophila melanogaster strains and crosses were reared on standard cornmeal medium and raised at 25°C or 29°C or shifted from 18°C to 29°C for genotypes with temperature-sensitive Gal80, as indicated in Supplementary file 2.

We used the following mutant and transgenic flies in combination or recombined in this study (see Supporting File 2 for more details; {} enclose individual genotypes, separated by commas).

{y,w,hsflp122; sp/Cyo; TM2/TM6B}, {y,w; sp/Cyo, Bacc-GFP; Dr/TM6C}, (from BDSC: 36349).

{ey-Gal80; sp/Cyo;} (BDSC: 35822), {;Gal80ts; TM2/TM6B} (BDSC: 7108), {w1118;; R27G05-Gal4} (BDSC: 48073), {w1118;;25A01-Gal4} (BDSC: 49102), {y,w; R64B07-Gal4;} (larval L5-Gal4), {y,w; hh-Gal4/TM3} (BDSC: 67493), {;tub-Gal80ts; repo-Gal4/TM6B}, {w1118;GMR-Gal4/Cyo;} (BDSC: 9146), {y,w;Pin/Cyo;repo-QF/TM6B} (BDSC: 66477), {y,w; NP6293-Gal4/Cyo,UAS-lacZ;} (perineurial glia; Kyoto Stock Center: 105188), {w; NP2276-Gal4/Cyo; } (subperineurial glia; Kyoto Stock Center: 112853), {w1118;; R54H02-Gal4} (cortex glia; BDSC: 45784), {w1118;; R10C12-Gal4} (epithelial and marginal glia; BDSC: 47841), {w;Mz97-Gal4, UAS-Stinger/Cyo;} (wrapping and xgO; BDSC: 9488), {w1118;; R53H12-Gal4} (chiasm glia; BDSC: 50456), {y,w; spiNP0289-Gal4/Cyo, UAS-lacZ;} (Kyoto Stock Center: 112128), {w1118; Cg-Gal4;} (BDSC: 7011), {w;; bnlNP2211-Gal4} (Kyoto Stock Center: 112825), {w; thsMI07139-Gal4/Cyo; MKRS/TM6B} (BDSC: 77475), {;;rho3PLLb, UAS-CD8::GFP/TM6B}, {;UAS-rho3-3xHA;} (gifts from B Shilo), {;;aosw11/TM6B} (aos-lacZ; BDSC: 2513), {y,w; sp/Cyo, Bacc-GFP; 10xQUAS-6xmCherry-HA} (BDSC: 52270), {y,w;;10xUAS-myrGFP} (BDSC: 32197), {;UAS-CD8::GFP;}, {;;UAS-CD8::GFP} (gifts from C Desplan), {y,w;;UAS-nls.lacZ}, (BDSC: 3956), {y,w; UAS-LifeAct-GFP/Cyo;} (BDSC: 35544), {w1118;UAS-Dcr-2;} (BDSC: 24650), {w1118;;UAS-Dcr-2} (BDSC: 24651), {;UAS-EGFRDN; UAS-EGFRDN} (BDSC: 5364), {;UAS-aopACT;} (Kyoto Stock Center: 108425), {y,w;UAS-rlsem;} (rlsem = MAPKACT; BDSC: 59006), {w1118;;UAS-PntP1} (BDSC: 869), {w1118;UAS-aosRNAi;} (VDRC47181), {w;UAS-jeb;} (a gift from A Gould), {y,w, UAS-Col4a1EY11094/(Cyo);} (BDSC: 20661), {;;UAS-Cg25c-RFP} (Zang et al., 2015) (Col4a1=Cg25c), {;UAS-Wnt5;} (BDSC: 64298), {;;UAS-s.spi} (a gift from B Shilo), {;UAS-m.spi::GFP-myc;} (a gift from B Shilo), {;;UAS-m.spi::GFP-myc} (a gift from B Shilo), {w, UAS-grk.sec/Cyo;} (BDSC: 58417), {;UAS-vnEPgy/Cyo;} (BDSC: 58498), {;;UAS-krn-3xHA} (FlyORF: F002754), {;UAS-bnl/Cyo; MKRS/TM6C} (BDSC: 64232), {;UAS-Ilp1;}, {;UAS-Ilp6;} (gifts from P Leopold), {w1118, UAS-Pvf1XP;;} (BDSC: 19632), {w1118; UAS-Pvf2XP;} (BDSC: 19631), {;UAS-Wnt4EPgy2/Cyo;} (BDSC: 20162), {;;UAS-boss-3xHA} (FlyORF: F001365), {y,sev; SAM.dCas9.Trk;} (BDSC: 81322), {y,sev; SAM.dCas9.Pvf3;} (BDSC: 81346), {y,sev; SAM.dCas9.ths;} (BDSC: 81347), {y,sev; SAM.dCas9.pyr;} (BDSC: 81330), {w1118; DdrCR01018-Gal4;} (BDSC: 81157).

### Immunocytochemistry, antibodies, and microscopy

We dissected eye-optic lobe complexes from early pupae (0–5 hr after puparium formation) in ×1 phosphate-buffered saline (PBS), fixed in 4% formaldehyde for 20 min, blocked in 5% normal donkey serum, and incubated in primary antibodies diluted in block for two nights at 4°C. Samples were then washed in ×1 PBS with 0.5% Triton-X (PBSTx), incubated in secondary antibodies diluted in block, washed in PBSTx and mounted in SlowFade (Life Technologies).

When performing phospho-MAPK stains, dissections were performed in a phosphatase inhibitor buffer as detailed in Amoyel et al., 2016.

We used the following primary antibodies in this study: mouse anti-Dac2-3 (1:20, Developmental Studies Hybridoma Bank [DSHB]), mouse anti-Repo (1:20, DSHB), rat anti-Elav (1:100, DSHB), mouse anti-Elav (1:20, DSHB), rabbit anti-Dcp-1 (1:100; Cell Signalling #9578), chicken anti-GFP (1:400; EMD Millipore), mouse anti-Svp (1:50, DSHB), rabbit anti-Slp2 (1:100; a gift from C Desplan), rabbit-Bsh (1:500; a gift from C Desplan), Rat anti-Pdm3 (1:1000; a gift from C Desplan), guinea pig anti-Brp (1:100; a gift from C Desplan), rabbit anti-Phospho-p44/42 MAPK (Erk1/2) (Thr202/Tyr204) (1:100, Cell Signaling #9101), chicken anti-RFP (1:500; Rockland #600-901-379s), mouse anti-β-galactosidase (1:500; Promega #Z3781), chicken anti-β-galactosidase (1:500; abcam #9361), rabbit-anti-GFP (1:500; Thermo Fisher Scientific #A6455), AlexaFluor405 conjugated Goat Anti-HRP (1:100; Jackson Immunolabs), AlexaFluor405-, Cy3-, or AlexaFluor647-conjugated Goat Anti-HRP (1:200; Jackson Immunolabs). Secondary antibodies were obtained from Jackson Immunolabs or Invitrogen and used at 1:800. Images were acquired using Zeiss 800 and 880 confocal microscopes with ×40 objectives.

### In situ hybridisation chain reaction

To determine if spi, Col4a1, and Ddr transcripts were present in the xgO, we performed HCR as detailed in Duckhorn et al., 2022. We designed 20–21 probe pairs against target genes, excluding regions of strong similarity to other transcripts, with corresponding initiator sequences for amplifiers B3 (Choi et al., 2018). HCR probes (sequences included as source data; see Figure 3—source data 1) were purchased as DNA Oligos from Thermo Fisher Scientific (100 µm in water and frozen).

Eye-optic lobe complexes were dissected, fixed, and washed as detailed above. Samples were incubated in Probe Hybridisation Buffer for 30 min at 37°C followed by incubation with probes (0.01 µM) at 37°C overnight. The samples were then washed four times for 15 min each with probe wash buffer at 37°C followed by two washes for 5 min each with ×5 saline sodium citrate solution (20XSSCT solution in distilled water – 58.44 g/mol sodium chloride, 294.10 g/mol 560 sodium citrate, pH adjusted to 7 with 14 N hydrochloric acid, with 0.001% Tween 20) at room temperature. Samples were then incubated with amplification buffer for 10 min at room temperature. 12 pmol of hairpins H1 and H2 were snap-cooled (95°C for 90 s and then cooled to room temperature for 20 min) separately to avoid oligomerisation. The snap-cooled hairpins were then added to the samples in the amplification buffer (protected from light) and incubated overnight at room temperature. The samples were then washed with 5XSSCT for 15 min before being incubated in darkness with 1:15 dilution of DAPI (Sigma D9542) for 90 min. Samples were washed with ×1 PBS for 30 min and then mounted as detailed above.

### Quantification and statistical analyses

We used Fiji-ImageJ (Schindelin et al., 2012) or Imaris (version x64-9.5.1) to process and quantify confocal images as described below. We used Adobe Photoshop and Adobe Illustrator software to prepare figures. We used GraphPad Prism 8 to perform statistical tests. In all graphs, whiskers indicate the standard error of the mean (SEM).

### Dcp-1 quantifications

We used the surfaces tool in Imaris to manually select the lamina region (based on Dac expression). We then used the spots tool to identify Dcp-1 positive cells (cell diameter = 5 μm) within the selected region using the default thresholding settings, and plotted these values normalised to the volume of the selected lamina region in GraphPad Prism 8.

### Cell-type quantifications

#### LPCs per column

Column number was identified by counting HRP-labelled photoreceptor axon bundles. We considered the youngest column located adjacent to the lamina furrow to be the first column, with column number (age) increasing towards the posterior (right) of the furrow. We counted the number of Dac+ cells per column by quantifying 10 optical slices (step size = 1 μm) located centrally in the lamina.

#### Control vs. Laminats>PntP1

We quantified the lamina neuron types per column using the following markers to identify L-neuron types: Elav+ and Slp2+ cells were counted as L1-L3s; Elav+ and Bsh+ cells were counted as L4s and Elav+, Bsh+, and Slp2+ cells were counted as L5s. We quantified 10 optical slices (step size = 1 μm) located centrally in the lamina. Column number was identified by counting HRP-labelled photoreceptor axon bundles. These quantifications were done blind.

#### Ligand receptor screen

We quantified the number of L5s based on Elav expression in the proximal lamina. Column number was identified by counting HRP-labelled photoreceptor axon bundles. We quantified 30 optical slices (step size = 1 μm) located centrally in the lamina.

### Ligand overexpression quantifications

We quantified the number of L-neuron types per column using Elav, Bsh, and Slp2. We quantified 30 optical slices (step size = 1 μm) located centrally in the lamina. Column number was identified by counting HRP-labelled photoreceptor axon bundles.

### Spi and Col4a1 probe intensity quantifications

In Fiji-ImageJ we used the free hand selection tool to draw a region of interest (ROI) around the xgO (marked by the xgO>CD8::GFP). We then measured the mean fluorescence intensity (MFI) of spi and Col4a1 transcripts labelled by HCR within each ROI. We quantified 30 optical slices (step size = 1 μm) located centrally in the lamina and then plotted the average for each optic lobe.

### Number of xgO

We quantified the number of xgO (Figure 1—figure supplement 1Q) by manually counting the number of Repo positive nuclei within LifeAct-GFP positive xgO per 40 μm optical section in Fiji-ImageJ. We used a step size of 1 μm while acquiring the z-stacks and centred each 40 μm optical section in the middle of the lamina using photoreceptor axons (HRP), and the lobula plug (Dac expression) as landmarks. Quantifications were performed blind.

### Length of xgO processes

We quantified the lengths of the fine glial processes that extend distally from the xgO towards the lamina plexus (Figure 1—figure supplement 1O,P,R) by using the straight-line selection and measuring tools in Fiji-ImageJ to measure xgO process lengths in a 10 μm optical section centred in the middle of the lamina. Quantifications were performed blind.

### Quantifications of nuclear to cytoplasmic dpMAPK MFI

Using Fiji we manually drew ROIs with the free hand selection tool around the xgO nucleus (based on Repo) and LPCs in the most proximal row of the lamina (based on Dac expression) and added these to the ROI manager. We then enlarged the ROIs (Edit > Selection > Enlarge) by 3.00 pixel units to include the cytoplasm. We then used the XOR function in the ROI Manager to only select the cytoplasm of the xgO. We then measured the MFI of dpMAPK in the nucleus and the cytoplasm of the xgO in 20 centrally located optical slices (corresponding to 20 μm) for each optic lobe. We plotted the nuclear:cytoplasmic ratios of dpMAPK MFI in GraphPad Prism 8.

### aos-lacZ intensity quantifications

Using Fiji we manually drew regions of interest around L5s (based on Slp2+Bsh co-expression) in each column. We then measured the MFI of β-Galactosidase in the ROIs. We quantified 10 optical slices (step size = 1 μm) for each optic lobe and plotted the average values as a function of column (age).
