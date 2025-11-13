# A complex peripheral code for salt taste in Drosophila

## Authors

- Alexandria H Jaeger<sup>1</sup>
- Molly Stanley<sup>1</sup>
- Zachary F Weiss<sup>1</sup>
- Pierre-Yves Musso<sup>1</sup>
- Rachel CW Chan<sup>3</sup> ([ORCID: 0000-0003-1009-6379](https://orcid.org/0000-0003-1009-6379))
- Han Zhang<sup>3</sup>
- Damian Feldman-Kiss<sup>1</sup>
- Michael D Gordon<sup>1</sup> ([ORCID: 0000-0002-5440-986X](https://orcid.org/0000-0002-5440-986X)) †

### Affiliations

1. Department of Zoology University of British Columbia Vancouver Canada
2. Graduate Program in Neuroscience University of British Columbia Vancouver Canada
3. Engineering Physics Program University of British Columbia Vancouver Canada

† Corresponding author

## Abstract

Each taste modality is generally encoded by a single, molecularly defined, population of sensory cells. However, salt stimulates multiple taste pathways in mammals and insects, suggesting a more complex code for salt taste. Here, we examine salt coding in Drosophila. After creating a comprehensive molecular map comprised of five discrete sensory neuron classes across the fly labellum, we find that four are activated by salt: two exhibiting characteristics of ‘low salt’ cells, and two ‘high salt’ classes. Behaviorally, low salt attraction depends primarily on ‘sweet’ neurons, with additional input from neurons expressing the ionotropic receptor IR94e. High salt avoidance is mediated by ‘bitter’ neurons and a population of glutamatergic neurons expressing Ppk23. Interestingly, the impact of these glutamatergic neurons depends on prior salt consumption. These results support a complex model for salt coding in flies that combinatorially integrates inputs from across cell types to afford robust and flexible salt behaviors.

## Introduction

Sodium is essential to survival, but its intake must be carefully regulated to maintain ionic homeostasis. It is therefore unsurprising that taste systems have evolved robust mechanisms for detecting salt, and that salt palatability depends on its concentration. In general, sodium concentrations below 100 mM tend to be attractive, while any salt present at higher concentrations becomes increasingly aversive (Chandrashekar et al., 2010; Lindemann, 2001; Oka et al., 2013)

Although there is considerable debate about modes of central taste coding, there is strong evidence that most taste modalities activate a single, molecularly defined, population of peripheral taste receptor cells (Yarmolinsky et al., 2009). However, research in both mammals and insects has favoured a dual-pathway model for salt taste: a low-threshold sodium-specific population of ‘low salt’ cells mediates attraction, which is overridden at higher concentrations by ion non-specific ‘high salt’ cells that drive avoidance (Ishimoto and Tanimura, 2004; Lindemann, 2001; Marella et al., 2006; Oka et al., 2013; Zhang et al., 2013). Moreover, two distinct aversive taste receptor cell (TRC) types (bitter and sour) contribute to high salt taste in mammals (Oka et al., 2013). Thus, peripheral coding of salt taste appears more complex than other primary taste modalities.

The Drosophila labellum contains three types of gustatory sensilla, each of which harbors 2–4 gustatory receptor neurons (GRNs) (Singh, 1997; Stocker, 1994)(Figure 1A). Short (S-type) and long (L-type) sensilla have four molecularly and physiologically distinct GRNs, while intermediate (I-type) sensilla have only two (Freeman and Dahanukar, 2015; Scott, 2018; Stocker, 1994). Extracellular ‘tip-recordings’ of different sensilla have identified four GRN types: a water (W) cell that responds to low osmolarity; a sugar (S) cell that responds to sweet compounds; a low salt (L1) cell that is sodium-specific; and a high salt (L2) cell that responds to high ionic concentrations (>250 mM) (Fujishiro et al., 1984; Hiroi et al., 2002; Ishimoto and Tanimura, 2004). S- and L-type sensilla are thought to have one of each GRN type, with S-type L2 cells responding to bitter compounds in addition to high salt (Meunier et al., 2003)(Figure 1B). I-type sensilla were shown to have an S/L1 hybrid cell that responds to sugars and low salt, and an L2 cell that responds to bitters and high salt (Hiroi et al., 2004)(Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig1-v1.jpg)

**Figure 1.:** (A) A schematic of sensillum identities in the fly labellum. (B) A summary of how GRN identities are currently viewed across the three sensillum types, with each color representing a GRN class with its most notable molecular label (if known) and its ascribed response properties. (C–H) Single labellar palps immunolabelled for VGlut-Gal4 driving UAS-tdTomato (magenta) alone (C) or in combination with LexAop-CD2::GFP (green) under the control of ChAT-LexA (D), Ppk28-LexA (E), Gr64f-LexA (F), Gr66a-LexA (G), or Ppk23-LexA (H). (I) Ppk23-LexA (green) and Gr66a-Gal4 (magenta) label partially overlapping populations. Arrows indicate sensilla where two Ppk23 GRNs exist, one of which co-expresses Gr66a. (J–K) Ppk23 subpopulations displayed by restricting Ppk23-Gal4 expression with VGlut-Gal80 (J), or Gr66a-LexA and LexAop-Gal80 (K). (L–N) IR94e-Gal4 labellum expression (magenta), co-labelled with Ppk28-LexA (L), Gr64f-LexA (M), and Ppk23-LexA (N). (O) Summary of newly defined GRN types following our mapping experiments. (P) Detailed map of each sensillum. Colors of ‘+' in chart indicate cell type. Grey denotes unknown identity. The VGlut +GRNs observed in I-type sensilla were sporadic and small, which is why they are not considered in the summary.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Labellum expression of Ppk23-Gal4 restricted with ChAT-Gal80. Arrow indicates an S-type sensillum with two Ppk23 +GRNs, indicating incomplete elimination of Ppk23chat expression. (B) Ppk23-Gal4 (magenta) and Ppk23-LexA (green) label nearly identical labellar GRN populations. (C–F) IR76b-Gal4 expression (magenta) in labella co-labelled with markers for different GRN populations (green): Ppk28-LexA (C), Gr64f-LexA (D), Gr66a-LexA (E), and Ppk23-LexA (F). (G) IR94e projections to the brain revealed by IR94e-Gal4 driving UAS-CsChrimson (green). Neuropil is labelled with nc82 (magenta).

The early physiological recordings have been mostly borne out by molecular characterization of GRN types (Freeman and Dahanukar, 2015; Scott, 2018)(Figure 1B). S- and L-type sensilla each have a single GRN that expresses the low osmolarity sensor Pickpocket28 (Ppk28) and corresponds to the W cell (Cameron et al., 2010; Chen et al., 2010; Inoshita and Tanimura, 2006). The S cell is labelled by the sugar receptor Gr64f, along with other members of the gustatory receptor (GR) family (Dahanukar et al., 2007; Fujii et al., 2015; Jiao et al., 2007; Slone et al., 2007; Thorne et al., 2004; Wang et al., 2004). Similarly, Gr66a is co-expressed with other Grs in a single bitter responsive neuron per S-type and I-type sensillum, corresponding to the L2 cell (Marella et al., 2006; Thorne et al., 2004; Wang et al., 2004; Weiss et al., 2011). The degenerin/epithelial sodium channel (Deg/ENaC) family member Ppk23, which is required for pheromone detection in leg gustatory sensilla, is known to be expressed in a labellar neuron population that partially overlaps with Gr66a/bitter GRNs (Thistle et al., 2012). Ppk23 neurons are necessary for calcium avoidance, but details of the labellar Ppk23 expression map, as well as the physiology and function of these neurons are largely unknown (Lee et al., 2018).

In contrast to water, sweet, and bitter tastes, the principles of peripheral salt coding in flies remain unclear. Early calcium imaging experiments revealed low salt responses in Gr5a-Gal4 GRNs, suggesting that sweet neurons may mediate low salt attraction (Marella et al., 2006). However, Gr5a-Gal4 was later shown to label additional GRNs outside the sweet class (Fujii et al., 2015), and the Ionotropic receptor (IR) family member IR76b was proposed to specifically mediate low salt taste via a dedicated low salt cell distinct from sweet GRNs (Zhang et al., 2013). This view was challenged by the recent demonstration that IR76b is also required for high salt taste, raising questions about its utility as a marker for one defined GRN population (Lee et al., 2017). Moreover, although Gr66a GRNs showed calcium responses to high salt concentrations and electrophysiology suggested that bitter and high salt are encoded by the same sensory neurons, genetically eliminating these cells left behavioral aversion to high salt largely intact (Marella et al., 2006; Wang et al., 2004).

Here, we probe the logic of salt coding across the labellum by systematically characterizing the physiological and behavioral roles of molecularly-defined GRN types covering the entire labellar GRN map. We find that all GRN types show dose-dependent excitation or inhibition by salt, indicating a complex model for salt coding. Of particular interest is that, like mammals, flies have two distinct high salt cells. In addition to activating canonical bitter neurons, high salt concentrations excite a glutamatergic GRN population expressing Ppk23. Salt responses of these ‘Ppk23glut’ GRNs require IR76b, whereas those of bitter GRNs do not. Both bitter and Ppk23glut GRNs are necessary for behavioral avoidance of high salt when flies have been reared on a salt-containing diet. However, salt deprivation reduces high salt avoidance by specifically suppressing the impact of Ppk23glut neurons, suggesting that these GRNs mediate internal state-dependent modulation of salt consumption. Consistent with this idea, closed-loop optogenetic activation of Ppk23glut neurons reduces feeding by salt-fed flies, but not those that have been salt deprived. Our results support a model where the combinatorial excitation and inhibition of various taste pathways mediates the behavioral valence of salt, with one pathway conferring the ability to specifically modulate salt consumption based on internal state.

## Results

### A comprehensive map of GRN classes in the labellum

Although several studies have mapped the expression of different receptors across the labellum (Freeman and Dahanukar, 2015), a comprehensive map covering all GRN types was still lacking. We began by asking whether the vesicular glutamate transporter (VGlut) may define a functionally distinct population of GRNs. An enhancer trap upstream of VGlut, OK371-Gal4, labels an uncharacterized population of putatively glutamatergic neurons in the labellum, and a subset of pheromone-responsive GRNs in the legs (Kallman et al., 2015; Mahr and Aberle, 2006). VGlutMI04979-Gal4, which is a gene-trap inserted within a VGlut exon, showed expression in a single cell per S-type and L-type sensillum in the labellum (Figure 1C). These cells do not overlap with those expressing a similar gene trap for choline acetyltransferase (ChAT), supporting the idea that VGlutMI04979-Gal4 labels a bona fide population of glutamatergic GRNs (Figure 1D).

Co-labelling of VGlutMI04979-Gal4 with LexA reporters for known sensory neuron populations revealed that VGlut is not expressed in water (Ppk28), sweet (Gr64f), or bitter (Gr66a) GRNs (Figure 1E–G). However, all VGlut+ cells were positive for Ppk23 (Figure 1H). Further examination of Ppk23 expression revealed that Ppk23 GRNs are comprised of two distinct subsets: most S-type and all L-type sensilla contain a single GRN that expresses Ppk23 and VGlut; and six S-type sensilla, roughly corresponding to those designated as ‘S-a’ sensilla (Freeman and Dahanukar, 2015; Weiss et al., 2011), have a second Ppk23 GRN that is positive for Gr66a and ChAT (Figure 1I). We will refer to these two populations as Ppk23glut and Ppk23chat, respectively. We then used gene trap insertions of Gal80 into VGlut and ChAT to isolate Ppk23chat and Ppk23glut GRNs. While this restriction largely agreed with our co-expression data, it was not perfect: VGlut-Gal80 restricted Ppk23-Gal4 expression to four S-type GRNs instead of the expected six (Figure 1J); and ChAT-Gal80 suppressed Ppk23-Gal4 expression in most, but not all, Ppk23chat GRNs, leaving 1 – 2 s-type sensilla with two Ppk23 neurons (Figure 1—figure supplement 1A). We suspect these results reflect minor differences between expression of the Gal4, LexA, and Gal80 reporters, although we confirmed that Ppk23-Gal4 and Ppk23-LexA labelled the same population of GRNs (Figure 1—figure supplement 1B). To create a more conservative representation of Ppk23glut, we constrained Ppk23-Gal4 activity using Gr66a-LexA and LexAop-Gal80 (Figure 1K). This manipulation faithfully restricted expression to only Ppk23glut GRNs, but also globally reduced expression levels. Thus, we retained both methods of isolating Ppk23glut cells for functional characterization.

Our analysis of Ppk23 expression nearly completed the labellar GRN map: s-type sensilla generally have one Ppk28 (water), one Gr64f (sweet), one Gr66a (bitter, some of which are Ppk23chat), and one Ppk23glut GRN; I-type sensilla have one Gr64f and one Gr66a GRN; and L-type sensilla have one Ppk28, one Gr64f, one Ppk23glut, and one unidentified GRN that has been proposed to express IR76b and respond to low salt concentrations (Freeman and Dahanukar, 2015; Zhang et al., 2013). To identify a marker for the last GRN class in L-type sensilla, we first examined IR76b. However, IR76b-Gal4 is expressed in many neurons from all four known classes of labellar GRNs, limiting its utility as a marker (Figure 1—figure supplement 1C–F). We therefore visually screened the Vienna Tile (VT) and Janelia Rubin Gal4 collections for lines that sparsely label GRN projections in the brain, and identified VT046252-Gal4, which drives Gal4 expression under the control of the genomic region upstream of the IR94e locus. Because the labellar projections to the subesophageal zone (SEZ) labeled by VT046252-Gal4 (Figure 1—figure supplement 1G) appear identical to those of a previously published reporter for IR94e expression (Koh et al., 2014), we will henceforth simply refer to it as IR94e-Gal4. IR94e-Gal4 is expressed in one cell per L-type sensillum, and does not overlap with Ppk28, Gr64f, or Ppk23 (Figure 1L–N). This driver is therefore specific for the fourth GRN class found in L-type sensilla and completes our molecular map of the labellum (Figure 1O–P).

### All labellar GRN classes respond to salt

With a complete labellar GRN map in hand, we examined the salt responses across all identified GRN classes. We expressed GCaMP6f under the control of each GRN class-specific Gal4 line and performed imaging of GRN axon terminals in the SEZ while stimulating the labellum with a series of tastants (Figure 2A–D). As expected, known GRN classes responded strongly to their cognate modality – Ppk28 to water, Gr64f to sugar (sucrose), and Gr66a to bitter (lobeline) (Figure 2C–D). As previously demonstrated, Ppk28 neurons show dose-dependent inhibition by salt, as with any osmolyte (Cameron et al., 2010). In contrast, Gr64f and Gr66a both showed dose-dependent excitation by salt, with Gr64f GRNs activated at a lower threshold. Moreover, Gr64f responses were sodium-specific, while Gr66a also responded to potassium chloride (Figure 2C–D). These results are consistent with Gr64f operating as a ‘low salt’ cell type, and Gr66a acting as a ‘high salt’ cell type.

![Figure 2.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig2-v1.jpg)

**Figure 2.:** (A) Schematic of calcium imaging preparation. Taste neurons are stimulated on the proboscis, while GCaMP6f fluorescence is recorded at the synaptic terminals in the SEZ. (B) Representative heat map showing activation of Ppk23 GRNs with 1 M NaCl. (C) GCaMP6f fluorescence changes over time, following stimulation of each GRN class with the indicated tastants. Lines and shaded regions represent mean ±SEM, with stimulation occurring at 5 s. In each case, UAS-GCaMP6f is expressed under the control of the indicated GRN-Gal4, with the exception of Ppk28, which is from Ppk28-LexA and LexAop-GCaMP6f. (D) Peak fluorescence changes during each stimulation. Bars represent mean ±SEM. n = 8 – 37. Open circles indicate values that were higher than the y-axis maximum. Asterisks indicate significant difference from water by one-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Time curves of GCaMP6f signal in IR94e GRNs following stimulation with indicated tastants. Lines and shaded regions indicate mean ±SEM. (B) Peak changes during stimulation of IR94e neurons with each tastant. Bars represent mean ±SEM, n = 29. Asterisks indicate significant difference from water by one-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Time curves of GCaMP6f activation in Ppk23 GRNs following stimulation with 1 M solutions of various salts and sucrose. Lines and shaded regions indicate mean ±SEM. (B) Peak changes during stimulation with each tastant. Bars represent mean ±SEM, n = 15. Asterisks indicate significant difference from water by one-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001. (C) Time curves of GCaMP6f activation in Ppk23 GRNs following stimulation with male or female pheromone mixtures. Lines and shaded regions indicate mean ±SEM. Female pheromone mixture is 7,11 HD plus 7,11 ND; male mixture is 7 T and cVA. (D) Peak changes during stimulation with each pheromone mix. Bars represent mean ±SEM, n = 9–10. Asterisks indicate significant difference from vehicle stimulations by one-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001.

Strikingly, we found that the two relatively uncharacterized labellar GRN types – IR94e and Ppk23 – also showed salt-evoked activity (Figure 2C–D). IR94e displayed weak activation by 50 mM NaCl, but no responses to higher concentrations. Further testing of different salts at 100 mM revealed sodium-selective tuning, indicating that IR94e labels a second low salt cell type (Figure 2—figure supplement 1A–B). The weak responses in IR94e neurons suggest a limited role in salt coding, but it is possible that they account for the previously observed peak response to low salt in L-type sensilla (Zhang et al., 2013). On the other hand, Ppk23 neurons showed very strong dose-dependent salt responses that were ion non-selective. In addition to sodium chloride, we observed robust activation by 1 M solutions of potassium chloride, sodium bromide, potassium bromide, cesium chloride, and calcium chloride (Figure 2—figure supplement 2A–B). As confirmation that the observed activity is salt-evoked and not a response to high osmolality, we found that Ppk23 GRNs do not respond to 1 M concentrations of sucrose (Figure 2—figure supplement 2A–B).

Since Ppk23 neurons on the leg are known to sense pheromones, we also tested labellar Ppk23 GRN responses to male and female cuticular hydrocarbons. We observed only very weak activation of Ppk23 neurons in female flies to a mixture of two male pheromones, and no significant responses in male flies (Figure 2—figure supplement 2C–D). Together, these data suggest that a primary function of labellar Ppk23 GRNs is to mediate a high salt response, and position Ppk23 and Gr66a as markers of two high salt GRN classes.

### Functional subdivision of Ppk23 GRNs

Our expression mapping revealed that Ppk23 GRNs encompass two subsets based on neurotransmitter expression: Ppk23chat and Ppk23glut. Given that Ppk23chat GRNs also express Gr66a, we suspected that this subpopulation may confer bitter responses to the Ppk23 population when measured as a whole. Although we did not observe Ppk23 activation in response to 0.3 mM lobeline (Figure 2C–D), we did see strong responses to caffeine (Figure 3A). Interestingly, we observed a marked difference in the synaptic calcium signals in response to salt and bitter stimuli. While salt stimulation of Ppk23 GRNs resulted in predominantly lateral activation of Ppk23 projections, bitter stimulation activated medial ring-like projections characteristic of Gr66a (Figure 3A)(Kwon et al., 2014; Thorne et al., 2004; Wang et al., 2004). These activation patterns matched closely with the projections of the Ppk23glut and Ppk23chat subsets, revealed by restricting Ppk23-Gal4 activity with Gr66a-LexA and LexAop-Gal80 (Ppk23glut) or VGlut-Gal80 (Ppk23chat)(Figure 3B). This suggests that Ppk23glut and Ppk23chat both respond to salt, but that only Ppk23chat responds to bitter compounds.

![Figure 3.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig3-v1.jpg)

**Figure 3.:** (A) Representative heat maps showing the activation Ppk23 GRNs in a single fly stimulated with 1 M NaCl and 100 mM caffeine. Salt primarily results in lateral activation, while bitter activates medial projections. (B) The projections of Ppk23 subsets targeting the SEZ, as revealed by immunofluorescent detection of GFP (green). Neuropil is labeled by nc82 (magenta). The full Ppk23 population targets both medial and lateral regions (left panel). Ppk23glut GRNs, revealed by restriction of Ppk23-Gal4 with Gr66a-LexA and LexAop-Gal80, target only lateral areas (middle panel). Ppk23chat projections, revealed by restriction of Ppk23-Gal4 with VGlut-Gal80, project to medial targets (right panel). (C) GCaMP6f fluorescence changes over time, following stimulation of each Ppk23 subset with the indicated tastants. Each fly has Ppk23-Gal4 driving UAS-GCaMP6f, restricted by either Gr66a-LexA and LexAop-Gal80 (top row) or Vglut-Gal80 (bottom row). Lines and shaded regions represent mean ±SEM, with stimulation occurring at 5 s. (D) Peak fluorescence changes during each stimulation. Bars represent mean ±SEM, n = 10–17. Asterisks indicate significant difference from water by one-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) GCaMP6f expression was primarily restricted to Ppk23glut GRNs using Ppk23-Gal4 in combination with ChAT-Gal80. Lines and shaded regions represent mean ±SEM of responses over time, with stimulation occurring at 5 s. (B) Peak fluorescence changes during each stimulation. Bars represent mean ±SEM, n = 17. Asterisks indicate significant difference from water by one-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001.

To confirm this and reveal any functional differences in salt coding between the Ppk23 subpopulations, we measured the tuning of Ppk23glut and Ppk23chat using calcium imaging. As expected, Ppk23chat, but not Ppk23glut, GRNs exhibited bitter responses; however, both subpopulations showed strong dose-dependent excitation by salt (Figure 3C–D). The salt responses in Ppk23glut GRNs appeared smaller than those of Ppk23chat, but we suspected this was due to very low GCaMP6f expression in Ppk23glut, which reduced the signal-to-noise in those measurements. We therefore repeated the Ppk23glut imaging by restricting Ppk23-Gal4 expression with ChAT-Gal80. Consistent with the imperfect restriction we observed in the labellum (Figure 1—figure supplement 1A), these flies had small, although insignificant, caffeine responses (Figure 3—figure supplement 1A–B). However, this primarily Ppk23glut population exhibited very strong activation by salt (Figure 3—figure supplement 1A–B).

Taken together, our anatomical and functional studies support a salt coding model with two functionally distinct high salt GRN populations: Gr66a and Ppk23glut. We currently lack evidence of any functional distinctions between Gr66a GRNs that are positive or negative for Ppk23. Therefore, for the purposes of salt coding, we will consider Gr66a GRNs as a uniform population that includes Ppk23chat.

### IR76b is necessary for low and high salt responses

A previous report suggested that IR76b is specifically required for low salt responses in an L-type GRN class distinct from Gr64f (Zhang et al., 2013). However, more recent evidence points to a role in both high and low salt taste (Lee et al., 2017). Since we observed widespread IR76b-Gal4 expression in many GRN classes, we sought clarity on the role of IR76b in salt taste responses across the labellum.

Calcium imaging in IR76b mutants revealed that IR76b is absolutely required for salt-evoked activity in Gr64f GRNs (Figure 4A–B). By contrast, the salt responses of Gr66a GRNs were only mildly decreased in the mutants, showing that these neurons have a mostly IR76b-independent mechanism for detecting high salt. Ppk23 salt responses had a much stronger dependence on IR76b, with significantly decreased peak values, compared to controls, at all concentrations tested (Figure 4—figure supplement 1A–B).

![Figure 4.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig4-v1.jpg)

**Figure 4.:** (A) GCaMP6f fluorescence changes over time for each indicated GRN type, following stimulation with the denoted tastants. Black lines are for control genotypes (IR76b1/+ background), red lines for IR76b1/IR76b2 mutants. ‘20%’ scale bar refers to all curves except for the Gr66a caffeine curves, which are scaled by the ‘60%’ bar. For Ppk23glut, GCaMP6f was expressed under the control of Ppk23-LexA, but only the lateral regions corresponding to Ppk23glut projections were quantified. The pre-stimulus and post-stimulus periods were truncated in all curves to more clearly illustrate stimulus phase. (B) Peak fluorescence changes during each stimulation. Bars represent mean ±SEM, n = 15 for each stimulus. Filled grey circles (control), open red circles (IR76b mutants), and filled red circles (cell-specific IR76b rescue in imaged GRN population) indicate values for individual replicates. Asterisks indicate significant difference between control and mutant or mutant and rescue responses for each stimulus by two-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001. (C) Representative heat maps of salt-evoked activity in Ppk23 neurons from control (top) and IR76b mutant (bottom) animals. Activation is predominantly lateral in controls and medial in mutants. Dotted line demarks representative area quantified to measure Ppk23glut-specific response (see Materials and methods). (D) Low salt attraction of IR76b mutants, heterozygous controls, and cell-specific rescue of IR76b in Gr64f sweet neurons. Preference measured in binary choice assay with 50 mM NaCl plus 2 mM sucrose versus 2 mM sucrose alone. Bars represent mean ±SEM. n = 30 – 40 groups of 10 flies each, with filled grey circles (controls), open red circles (IR76b mutants), or filled red circles (rescues) indicating values for individual groups. Asterisks denote significance by one-way ANOVA with Bonferroni post hoc test, ***p<0.001. (E) High salt avoidance of IR76b mutants, heterozygous controls, and cell-specific rescue of IR76b in Gr66a bitter neurons or Ppk23 neurons. Preference measured in binary choice assay with 250 mM NaCl plus 25 mM sucrose versus 5 mM sucrose alone. Bars represent mean ±SEM. n = 22 – 52 groups of 10 flies each, with filled grey circles (controls), open red circles (IR76b mutants), or filled red circles (rescues) indicating values for individual groups. Asterisks denote significance by one-way ANOVA with Bonferroni post hoc test, ***p<0.001.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) GCaMP6f fluorescence changes over time for full Ppk23 projections. Black lines are for control genotypes (IR76b1/+ background), red lines for IR76b1/IR76b2 mutants. (B) Peak fluorescence changes during each stimulation. Bars represent mean ±SEM, n = 15. Filled grey circles (control), open red circles (IR76b mutants), and filled red circles indicate values for individual replicates. Asterisks indicate significant difference between control and mutant responses for each stimulus by two-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Peak values of GCaMP6f fluorescence changes for each GRN type in heterozygous controls (filled grey circles), IR25a mutants (open red circles), and rescues (filled red circles), following stimulation with the indicated tastants. Bars represent mean ±SEM, n = 15. Asterisks indicate significant difference between control and mutant or mutant and rescue responses for each stimulus by two-way ANOVA with Bonferroni post hoc test, *p<0.05, **p<0.01, ***p<0.001.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A–B) Response curves (A) and peak values (B) for Ppk23 calcium responses in a Ppk23, Ppk29 mutant background. Values represent mean ±SEM, n = 14. Asterisks denote significant different from water stimulus by one-way ANOVA with Bonferroni post hoc test. ***p<0.001.

Given the IR76b-independent salt responses in Gr66a GRNs, it was unsurprising that IR76b mutants showed some Ppk23 GRN activity in the medial region targeted by Ppk23chat (Gr66a-positive) projections (Figure 4C). We therefore reanalyzed the Ppk23 dataset by quantifying fluorescence change in a region-of-interest restricted to the lateral areas characteristic of Ppk23glut projections (Figures 3B and 4C). IR76b mutants exhibited essentially no salt-evoked activity in this target region, suggesting that IR76b is necessary for both the sodium and potassium salt responses of the Ppk23glut population (Figure 4A–B).

Since IR25a is expressed in GRNs and thought to be another broadly acting co-receptor (Ahn et al., 2017a; Benton et al., 2009; Cameron et al., 2010; Chen and Amrein, 2017; Lee et al., 2018), we also tested its involvement in salt taste. We found that IR25a mutants have GRN response profiles similar to those of IR76b mutants, suggesting that perhaps IR25a and IR76b act in a complex to mediate gustatory salt responses (Figure 4—figure supplement 2). However, in contrast to IR76b and IR25a, mutations in Ppk23 and the related ENaC Ppk29 had no observable effect on the salt-evoked calcium responses of Ppk23 GRNs, consistent with previously reported behavioral tests (Figure 4—figure supplement 3A–B, [Thistle et al., 2012]). Thus, the Ppk23 gene marks a salt-responsive GRN population but does not appear to be involved in salt detection.

The fact that IR76b mutants lack salt responses in the primary low salt GRN class and one of two high salt GRN classes provides an explanation for observed defects in both low salt attraction and high salt avoidance (Lee et al., 2017; Zhang et al., 2013). Before further dissecting the cellular contributions of different GRN classes to salt behaviors, we wanted to establish behavioral assays that replicated these phenotypes. To test low salt attraction, we used a binary choice assay where flies were given the option to feed on either 50 mM salt mixed with low sugar (2 mM sucrose), or the same concentration of sugar alone (LeDue et al., 2015; Tanimura et al., 1982; Zhang et al., 2013). As previously reported, control flies are strongly attracted to the salt-containing option, while IR76b mutants lose this attraction (Figure 4D). We used a similar assay to probe high salt avoidance. In this case, control flies avoid 250 mM salt mixed with 25 mM sucrose in favor of plain sucrose at a lower concentration (5 mM). Much like their defects in low salt attraction, IR76b mutants are severely impaired in high salt aversion (Figure 4E).

### The cellular basis for salt attraction and avoidance

To probe the cellular basis of salt behaviors, we conditionally silenced different GRN populations using Kir2.1 expression temporally restricted with Gal80ts. As expected, both Ppk23glut and Ppk28 GRNs were dispensable for low salt attraction (Figure 5A). Focusing on the two GRN classes with low salt tuning properties, we found that Gr64f GRN activity is necessary for attraction to 50 mM NaCl, but expression of Kir2.1 in IR94e GRNs had no effect (Figure 5A). Further, silencing Gr64f and IR94e neurons together resulted in behavior indistinguishable from Gr64f silencing alone. Puzzled by the apparent lack of a role for IR94e GRNs in salt attraction, we expressed a different effector – tetanus toxin (TNT) – in these neurons without any temporal restriction with Gal80ts, and observed reduced low salt attraction (Figure 5—figure supplement 1). Moreover, attraction was virtually eliminated when TNT was expressed in both Gr64f and IR94e GRNs (Figure 5—figure supplement 1). Thus, we conclude that sweet GRNs likely mediate the bulk of low salt attraction, with additional input from the IR94e class.

![Figure 5.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig5-v1.jpg)

**Figure 5.:** (A) Low salt attraction in binary choice assay, following silencing of different GRN populations with Kir2.1. Positive values indicate preference for 50 mM NaCl plus 2 mM sucrose; negative values indicate preference for 2 mM sucrose alone. Bars represent mean ±SEM. n = 40 groups of 10 flies each for all genotypes except the UAS-Kir2.1/+ control, where n = 200. Filled grey circles indicate values for individual groups. Asterisks denote significant difference from both UAS-Kir2.1/+ and corresponding Gal4/+ controls by one-way ANOVA with Bonferroni post hoc test, ***p<0.001. (B) Low salt attraction tested in the absence of sugar. Bars represent mean ±SEM. n = 40 groups of 10 flies each. Asterisks denote significant difference from both UAS-Kir2.1/+ and corresponding Gal4/+ controls by one-way ANOVA with Bonferroni post hoc test, ***p<0.001. (C–D) Requirements of aversive GRNs in high salt avoidance under salt fed (C) or salt deprived (D) conditions. Positive values indicate preference for 250 mM NaCl plus 25 mM sucrose; negative values indicate preference for 5 mM sucrose. Bars represent mean ±SEM. n = 25 (C) or 30 (D) groups of 10 flies each for all genotypes except the UAS-Kir2.1/+ control in (D), where n = 60. Filled grey circles indicate values for individual groups. Asterisks denote significant difference from both UAS-Kir2.1/+ and corresponding Gal4/+ controls by one-way ANOVA with Bonferroni post hoc test, ***p<0.001. For all panels, ‘Ppk23glut-Gal4’ indicates Ppk23-Gal4 with Gr66a-LexA and LexAop-Gal80; and ‘>' denotes indicated Gal4 driving UAS-Kir2.1 with temporal restriction by tub-Gal80ts.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Low salt attraction in binary choice assay, following silencing of different GRN populations with Tetanus toxin (TNT). Positive values indicate preference for 50 mM NaCl plus 2 mM sucrose; negative values indicate preference for 2 mM sucrose alone. Bars represent mean ±SEM. n = 40 groups of 10 flies each for all genotypes. Filled grey circles indicate values for individual groups. Asterisks denote significant difference from UAS-TNT/+ and corresponding Gal4/+ and impTNT controls by one-way ANOVA with Bonferroni post hoc test, ***p<0.001.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A–B) High salt inhibition of PER in salt fed (left) or salt deprived (right) flies following silencing of Ppk23glut (A) or Gr66a (B) GRNs. Labellar PER was measured to 100 mM sucrose plus the indicated salt. Flies were either salt fed or salt deprived prior to the experiment. Values indicate mean ±SEM. n = 4 groups of 10 flies for each genotype. Asterisks denote significance from both control groups by two-way ANOVA with Bonferroni post hoc test, **p<0.01, ***p<0.001. ‘Ppk23glut-Gal4’ indicates Ppk23-Gal4 with Gr66a-LexA and LexAop-Gal80; and ‘>' denotes Gal4 driving UAS-Kir2.1 with temporal restriction by tub-Gal80ts.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** GCaMP imaging of Ppk23glut GRN responses in flies that have been salt fed (filled grey circles) or salt deprived (open grey circles). Bars represent mean ±SEM of peak fluorescence changes during each stimulation, n = 13 – 15. No significant differences were observed between the fed and deprived groups.

Interestingly, Kir2.1 expression in IR76b-Gal4 GRNs had a similar effect to Gr64f silencing, suggesting that Gr64f mediates the bulk of IR76b-dependent low salt attraction. However, this phenotype appears less severe than that of IR76b mutants, which display mild low salt avoidance (Figure 4D). This could reflect incomplete silencing from Kir2.1, as suggested by the lack of observable effects in IR94e GRNs, or weak IR76b-independent low salt responses in Gr66a (bitter/high salt) GRNs that further reduce salt preference in IR76b mutants. In any case, restoring IR76b selectively to Gr64 neurons rescues low salt attraction in IR76b mutants, further supporting the role of sweet neurons in salt attraction (Figure 4D).

Since Gr64f neurons are necessary for sugar detection, we sought verification that the Gr64f salt attraction phenotype was not from an inability to sense the low concentration of sucrose in both food options. Indeed, Gr64f silencing caused a similar reduction in salt attraction in the absence of sugar (Figure 5B).

We then tested the role of each high salt GRN class in high salt avoidance and found that Gr66a and Ppk23glut GRNs are both necessary for this behavior (Figure 5C). To confirm the novel role for Ppk23glut in behavioral salt avoidance, we tested its impact on the Proboscis Extension Reflex (PER), which is an acute measure of gustatory palatability. Consistent with our binary choice assay, silencing Ppk23glut GRNs severely impaired the inhibition of PER by high salt (Figure 5—figure supplement 2A). Moreover, rescue of IR76b expression in either Gr66a or Ppk23glut GRNs partially restores high salt avoidance to IR76b mutants (Figure 4E).

### Ppk23glut mediates state-dependent modulation of salt behaviors

Fly gustatory responses are frequently modulated by need for specific nutrients (Kim et al., 2017). However, modulating salt behaviors presents a complex problem because two of the three GRN classes exhibiting strong salt-evoked activity – Gr64f (sweet) and Gr66a (bitter) – have prominent roles in the detection of other modalities. These are therefore poor candidates for need-dependent modulation of salt responses, unless plasticity is achieved by regulating a salt-specific receptor. We therefore speculated that Ppk23glut GRNs, which to our knowledge specifically respond to salt, may tune the fly’s salt behaviors based on need.

The high salt assay shown in Figure 5C was performed on flies under salt fed conditions (three days with food containing 10 mM NaCl) to maximize salt avoidance. We subsequently repeated this experiment with flies deprived of salt for three days and observed the expected weakening of salt aversion in controls (Figure 5D; p<0.0001 compared to Figure 5C). Strikingly, while silencing Gr66a GRNs further reduced salt avoidance, silencing Ppk23glut GRNs had no effect (Figure 5D). This suggests that the aversiveness of Ppk23glut GRN activation is suppressed by salt deprivation. To verify this result, we again turned to PER and found that salt deprivation reduced high salt inhibition of PER and suppressed the role of Ppk23glut GRNs (Figure 5—figure supplement 2A). Interestingly, Gr66a GRN silencing produced only weak effects on PER inhibition by high salt, which were significantly manifested only in the salt deprived state (Figure 5—figure supplement 2B).

We next asked whether the observed behavioral modulation by salt deprivation would be evident in the calcium responses of these neurons; however, salt deprivation led to only a very mild and statistically insignificant reduction in Ppk23glut salt responses (Figure 5—figure supplement 3). Therefore, modulation is likely to occur downstream of GRN output.

To further explore this idea, we built a closed-loop system for real-time optogenetic activation of neurons during feeding behavior. Developed as an add-on to the fly Proboscis and Activity Detector (FlyPAD; [Itskov et al., 2014]), our system triggers illumination of a red LED immediately upon detecting a fly’s interaction with one of the two food sources (Figure 6A). We call this system the Sip-TRiggered Optogenetic Behavior Enclosure (STROBE). The STROBE is similar in concept to another recently described optogenetic FlyPAD (Steck et al., 2018), but implements sip detection and light triggering in a different way to minimize latency and achieve illumination during sips, with LED activation tightly locked to sip onset and offset.

![Figure 6.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig6-v1.jpg)

**Figure 6.:** (A) Schematic of closed-loop optogentic feeding assay, called the ‘sip triggered optogenetic behavior enclosure’ (STROBE). Each food is presented as a small drop containing 1% agar. Interactions with Food 1 that are recorded as ‘sips’ trigger illumination of an LED in the roof of the enclosure, above Food 1. Light triggering is temporally coupled to sip onset with minimal latency. Sips on Food 2 are recorded, but no light is triggered. (B) STROBE results for optogenetic stimulation of each salt-responsive GRN class. CsChrimson was expressed in each indicated GRN class, and the preference for Food 1 (light triggering) vs Food 2 (no light triggered) is plotted. Food 1 and Food 2 were otherwise the same in each experiment: plain agar (‘water’) for Gr64f and IR94e activation, and 1M sucrose for Gr66a and Ppk23glut activation. 1 M sucrose was used for aversive GRN tests because we observe more robust avoidance in this context. Bars represent mean ±SEM. Colored bars represent flies fed retinal (active CsChrimson) and gray bars represent flies not fed retinal (inactive controls). n = 19 – 24 for Gr64f, IR94e and Gr66a experiments, and n = 34 – 42 for Ppk23glut experiment. Filled (retinal fed) or open (not retinal fed) circles indicate values for individual flies. Asterisks indicate significant differences between retinal and no retinal groups for each condition by two-way ANOVA with Bonferroni post hoc test, ***p<0.001. Asterisks between fed and deprived conditions for Ppk23glut experiment represent a significant interaction between salt feeding and ±retinal conditions, ***p<0.001.

As expected, sip-induced triggering of Gr64f GRN activation makes a tasteless food source attractive compared to the same food without light stimulation, and this effect is independent of salt deprivation (Figure 6B). Similarly, Gr66a activation is strongly aversive for both salt fed and salt deprived flies. Consistent with their lack of a strong phenotype when silenced, activation of IR94e neurons did not produce a detectable phenotype in either condition. However, stimulating Ppk23glut GRNs is aversive, but only when flies have been pre-fed on a salt-containing diet (Figure 6B). This supports a model where salt need modulates salt avoidance downstream of Ppk23glut GRN activation.

## Discussion

Our results suggest a complex model for how the fly peripheral gustatory system encodes salt taste. In contrast to other known taste modalities, which typically activate a single, molecularly defined population of sensory neurons, salt taste is encoded by the combined activity of most to all GRN classes (Figure 7). By identifying markers that cumulatively cover virtually every labellar GRN, we find that two cell types – Gr64f and IR94e – display low salt tuning properties and mediate salt attraction. Although Gr64f neurons are also activated by higher concentrations of salt, their relatively low threshold for activation and specificity for sodium are consistent with a low salt GRN identity. Two other cell types – Gr66a and Ppk23glut – act as high salt GRNs, responding ion non-selectively to high concentrations of salt and driving avoidance. Moreover, the impact of Ppk23glut activation is suppressed upon salt deprivation, providing a means to reduce salt avoidance when need is elevated.

![Figure 7.](https://cdn.elifesciences.org/articles/37167/elife-37167-fig7-v1.jpg)

**Figure 7.:** Line thickness indicates strength of the excitatory (arrows) or inhibitory (bars) effects of high and low salt on each GRN class, as well as the impact of each cell type on behavior.

Prior salt coding models have primarily relied on correlations between neural activity and behavioural responses to different salt stimuli, as well as changes to those properties in mutants that may have wide ranging effects (Ishimoto and Tanimura, 2004; Lee et al., 2017; Zhang et al., 2013). These studies led to the important idea that there are distinct low salt and high salt cells present, and that at increasing salt concentrations, the aversive high salt cell progressively dominates over the attractive low salt cell. However, without the molecular tools to identify and manipulate individual GRN classes, the identity and number of salt-responsive cell types were unclear. Our examination of salt coding across a comprehensive set of molecularly defined GRN classes provides new insight into the complexity of salt coding in flies, but is not without limitations. Most notably, we cannot detect possible heterogeneity within defined GRN classes. For example, a Gr64f (sweet) neuron is present in each bristle of all sensillum types. Because we looked at the population as a whole, we cannot confidently conclude that every Gr64f cell acts as a low salt cell; we know only that there are sodium-specific salt responses from the Gr64f population, and that this population drives low salt attraction.

### Ppk23 labels a new high salt cell

Electrophysiological recordings of individual labellar taste sensilla identified high salt responses in the bitter-sensing neurons of S- and I-type sensilla, and previous GRN calcium imaging confirmed that Gr66a neurons respond to 1 M NaCl and KCl (Marella et al., 2006; Meunier et al., 2003). However, two key results suggested that bitter GRNs did not account for all high salt taste. First, high salt neurons have been identified in L-type sensilla (which don’t have Gr66a neurons) via tip recordings, although this has subsequently been debated (Hiroi et al., 2002; Ishimoto and Tanimura, 2004; Zhang et al., 2013). Second, genetically ablating Gr66a GRNs did not block the inhibition of PER by high salt (Wang et al., 2004). The existence of Ppk23glut high salt cells likely explains both of these observations and provides a mechanism by which flies can specifically modulate their salt behavior in response to need.

In addition to the modulation of their behavioral impact, Ppk23glut neurons display some notable characteristics, the most conspicuous being they are the only GRN class to express a marker for glutamatergic, rather than cholinergic, neurons. This adds a potential new dimension to the gustotopic GRN map formed in the fly brain and may be a key mechanism by which the output of Ppk23glut neurons remains functionally distinct from other GRN classes targeting postsynaptic neurons in the same area. Indeed, the aversive nature of Ppk23glut output stands in contrast to what one would predict from their projection morphology, which looks qualitatively similar to known appetitive (Gr64f, Ppk28), rather than aversive (Gr66a) GRNs. It is possible that Ppk23glut aversiveness is mediated through inhibition of appetitive taste pathways, as glutamate can have excitatory or inhibitory postsynaptic effects, depending on the receptor present (Liu and Wilson, 2013).

Although Ppk23glut defines a novel high salt cell, it is important to note that the Ppk23 channel is not required for its salt responsiveness. This raises questions about what Ppk23-dependent responses these cells may exhibit. Since Ppk23 is required for leg GRN pheromone-evoked activity that regulates courtship, a related function for Ppk23 labellar GRNs cannot be excluded. Indeed, weak, but significant Ppk23-dependent pheromone responses have been observed in labellar GRNs, although it’s unclear whether these were from Ppk23glut or Ppk23chat cells (Thistle et al., 2012). Moreover, the interaction between salt taste and mating suggests that perhaps there is a need to co-modulate salt and social cues based on salt diet (Walker et al., 2015).

In contrast to the strong salt responses in Ppk23glut cells, the other uncharacterized GRN class we identified, IR94e, displayed only weak salt-evoked activity. We therefore expect that this class primarily responds to other, yet unidentified, taste ligands. Given the lack of strong effects we observe upon activation of IR94e GRNs in the STROBE, we also suspect that the behavioral impact of IR94e activation is, like Ppk23glut, state- or context-dependent.

### IR76b has widespread roles in chemosensation

To date, IR76b has been shown to be necessary for gustatory responses to low salt, high salt, calcium, acids, amino acids, fatty acids, and polyamines (Ahn et al., 2017b; Chen and Amrein, 2017; Hussain et al., 2016b; Lee et al., 2017; Zhang et al., 2013). Consistent with these widespread roles in the taste system, we find expression of IR76b-Gal4 in every GRN type tested. Nonetheless, we felt it important to clarify the role of IR76b in salt taste, given the apparent complexities in salt responses across labellar GRN types, and the previous demonstration that IR76b can function as a sodium leak channel (Zhang et al., 2013).

We find that Gr64f salt responses are completely dependent on IR76b, consistent with its proposed role in low salt taste. Ppk23glut salt responses also require IR76b, but those in Gr66a GRNs do not, indicating two different salt transduction mechanisms in these two high salt cells. This may explain why prior reports differed on whether high salt responses remain intact in IR76b mutants (Lee et al., 2017; Zhang et al., 2013). Interestingly, the IR76b-dependent salt responses in Ppk23glut GRNs are not sodium specific, as we see loss of high sodium and potassium salt-evoked activity. This suggests that, although IR76b is primarily permeable to sodium when expressed in heterologous cells (PNa: PK = 1: 0.4), it may function in complexes with other subunits that confer different ion selectivity in different GRN classes (Zhang et al., 2013).

Recently, Ppk23 GRNs were identified as underlying IR76b-dependent calcium taste avoidance (Lee et al., 2018). Although it isn’t clear whether Ppk23glut or Ppk23chat (or both) subpopulations are responsible, our results indicate that this effect is not specific to calcium, but rather a general salt avoidance mechanism. Indeed, Ppk23 GRNs respond to high concentrations of all salts tested. Moreover, we find that IR25a, which was implicated in Ppk23-mediated calcium taste (Lee et al., 2018), is necessary for salt responses in Gr64f and Ppk23glut GRNs, similar to the requirements for IR76b. This stands in contrast to results reported by Zhang et al. (2013), which suggested that IR25a did not play a role in sodium taste. The similar requirements for IR76b and IR25a also suggest that these two receptors may act in a complex to mediate salt taste, which is consistent with previous evidence that IR25a is a broadly expressed coreceptor (Ahn et al., 2017a; Benton et al., 2009; Cameron et al., 2010; Chen and Amrein, 2017; Lee et al., 2018).

### Modulation of salt avoidance by internal state

Changes in gustatory sensitivity based on internal state are a widespread feature of the fly taste system: starvation potentiates sweet GRN sensitivity and suppresses bitter GRN responses; mating increases taste peg GRN sensitivity to polyamines and behavioral sensitivity to low salt in females; and protein deprivation sensitizes taste peg GRNs to yeast and increases behavioral sensitivity to amino acids (Hussain et al., 2016a; Inagaki et al., 2012; Inagaki et al., 2014; LeDue et al., 2016; Steck et al., 2018; Toshima and Tanimura, 2012; Walker et al., 2015). Although modulation of salt taste has not been previously examined in flies, salt depletion in humans increases salt palatability (Beauchamp et al., 1990). In line with all these results, we observe significant modulation of fly salt taste behavior by salt deprivation.

In contrast to most taste modalities, which activate a single GRN population, modulation of salt taste presents a complicated problem, because tuning the gain of Gr64 or Gr66a GRN output would have side effects on sweet and bitter taste sensitivity that may be situationally inappropriate. Here, we have presented evidence that the fly gustatory system solves this problem by specifically modulating the effects downstream of Ppk23glut activation. Salt deprivation suppresses the aversiveness of these neurons, allowing the fly to be less repulsed (or more attracted) to salty foods.

Thus, the fly taste system appears to encode salt as a complex mixture of attractive and repulsive sensory responses. Two GRN classes – Gr64f and Gr66a – provide a baseline level of attraction or avoidance, and this response is then adjusted to need via modulation of a third class of salt-responsive GRNs, Ppk23glut. The apparent specificity of labellar Ppk23glut GRNs to salt may also provide an important neural substrate for discrimination between salt and other taste modalities. Continued exploration of how salt, and other, taste signals are integrated higher in the brain will provide insight into how an apparently low-dimensional sensory system can successfully encode a variety of diverse chemical cues.

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
      <td>Genetic reagent (D. melanogaster)</td>
      <td>vGlutMI04979-Gal4</td>
      <td>Diao et al. (2015)</td>
      <td>BDSC: 60312; RRID:BDSC_60312</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ChATMI04508-Gal4</td>
      <td>Diao et al. (2015)</td>
      <td>BDSC: 60317; RRID:BDSC_60317</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>vGlutMI04979-LexA::QFAD</td>
      <td>Diao et al. (2015)</td>
      <td>BDSC: 60314; RRID:BDSC_60314</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ChATMI04508- LexA::QFAD</td>
      <td>Diao et al. (2015)</td>
      <td>BDSC: 60319; RRID:BDSC_60319</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>vGlutMI04979-Gal80</td>
      <td>Diao et al. (2015)</td>
      <td>BDSC: 60316; RRID:BDSC_60316</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ChATMI04508-Gal80</td>
      <td>Diao et al. (2015)</td>
      <td>BDSC: 60321; RRID:BDSC_60321</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ΔPpk23</td>
      <td>Thistle et al. (2012)</td>
      <td>Flybase: FBal0277047</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ΔPpk29</td>
      <td>Thistle et al. (2012)</td>
      <td>Flybase: FBal0277049</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Gr66a-LexA</td>
      <td>Thistle et al. (2012)</td>
      <td>Flybase: FBal0277069</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ppk28-LexA</td>
      <td>Thistle et al. (2012)</td>
      <td>Flybase: FBal0277050</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ppk23-Gal4</td>
      <td>Thistle et al. (2012)</td>
      <td>Flybase: FBal0277044</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Gr64fLexA</td>
      <td>Miyamoto et al. (2012)</td>
      <td>Flybase: FBti0168176</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ppk23-LexA</td>
      <td>Toda et al. (2012)</td>
      <td>Flybase: FBst0051311</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>IR76b-Gal4</td>
      <td>Zhang et al. (2013)</td>
      <td>Flybase: FBtp0085485</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>IR76b1</td>
      <td>Zhang et al. (2013)</td>
      <td>Flybase: FBst0051309</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>IR76b2</td>
      <td>Zhang et al. (2013)</td>
      <td>Flybase: FBst0051310</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-IR76b</td>
      <td>Zhang et al. (2013)</td>
      <td>Flybase: FBtp0085485</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>IR25a1</td>
      <td>Benton et al. (2009)</td>
      <td>Flybase: FBst0041736</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>IR25a2</td>
      <td>Benton et al. (2009)</td>
      <td>Flybase: FBst0041737</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-IR25a</td>
      <td>Abuin et al., 2011</td>
      <td>Flybase: FBst0041747</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Gr66a-Gal4</td>
      <td>Wang et al. (2004)</td>
      <td>Flybase: FBtp0014660</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Gr64f-Gal4</td>
      <td>Dahanukar et al. (2007)</td>
      <td>Flybase: FBti0162678</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Gr64f-Gal4</td>
      <td>Dahanukar et al. (2007)</td>
      <td>Flybase: FBtp0057275</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Ppk28-Gal4</td>
      <td>Cameron et al. (2010)</td>
      <td>Flybase: FBtp0054514</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>LexAop-CD2::GFP</td>
      <td>Lai and Lee (2006)</td>
      <td>Flybase: FBti0186090</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Kir2.1</td>
      <td>Baines et al. (2001)</td>
      <td>Flybase: FBti0017552</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>tub-Gal80ts</td>
      <td>McGuire et al. (2004)</td>
      <td>Flybase: FBti0027797</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>IR94e-Gal4</td>
      <td>Tirián and Dickson, 2017</td>
      <td>VDRC: v207582</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w1118</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 3605; RRID:BDSC_3605</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>LexAop-Gal80</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 32214; RRID:BDSC_32214</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>LexAop-GCaMP6f</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 44277; RRID:BDSC_44277</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-GCaMP6f</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 42747; RRID:BDSC_42747</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-GCaMP6f</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 52869; RRID:BDSC_52869</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-CsChrimson</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 55135; RRID:BDSC_55135</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-TNT</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 28838; RRID:BDSC_28838</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-impTNT</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC: 28840; RRID:BDSC_28840</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GFP</td>
      <td>Abcam, Cambridge, UK,</td>
      <td>#13970; RRID:AB_300798</td>
      <td>(1:1000 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-RFP</td>
      <td>Rockland Immunochemicals, Pottstown, PA,</td>
      <td>#600-401-379; RRID:AB_2209751</td>
      <td>(1:200 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-chicken Alexa 488</td>
      <td>Abcam</td>
      <td>#150169; RRID:AB_2636803</td>
      <td>(1:200 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit Alexa 647</td>
      <td>Thermo Fisher Scientific, Waltham, MA,</td>
      <td>#A21245; RRID:AB_2535813</td>
      <td>(1:200 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-brp</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>#nc82; RRID:AB_2314866</td>
      <td>(1:50 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit Alexa 568</td>
      <td>Thermo Fisher Scientific, Waltham, MA,</td>
      <td>#A11036; RRID:AB_10563566</td>
      <td>(1:200 dilution)</td>
    </tr>
    <tr>
      <td>Chemical  compound, drug</td>
      <td>All trans-Retinal</td>
      <td>Sigma-Aldrich</td>
      <td>#R2500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sucrose</td>
      <td>Sigma-Aldrich</td>
      <td>#S7903</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NaCl</td>
      <td>Sigma-Aldrich</td>
      <td>#S7653</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KCl</td>
      <td>Sigma-Aldrich</td>
      <td>#P9541</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NaBr</td>
      <td>Sigma-Aldrich</td>
      <td>#S4547</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KBr</td>
      <td>Sigma-Aldrich</td>
      <td>#221864</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CsCl</td>
      <td>Sigma-Aldrich</td>
      <td>#289329</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CaCl2</td>
      <td>BDH chemicals</td>
      <td>#BDH4524</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lobeline hydrochloride</td>
      <td>Sigma-Aldrich</td>
      <td>#141879</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Caffeine</td>
      <td>Sigma-Aldrich</td>
      <td>#C0750</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>7,11-heptacosadiene (7,11-HC)</td>
      <td>Caymen chemical company</td>
      <td>#10012567</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>7,11-nonacosadiene (7,11-NC)</td>
      <td>Caymen chemical company</td>
      <td>#9000314</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>7-tricosene (7 T)</td>
      <td>Caymen chemical company</td>
      <td>#9000313</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cis-vaccenyl acetate (c-VA)</td>
      <td>Caymen chemical company</td>
      <td>#10010101</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Erioglaucine</td>
      <td>Spectrum chemical</td>
      <td>#FD110</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Amaranth</td>
      <td>Sigma-Aldrich</td>
      <td>#A1016</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STROBE executable</td>
      <td>Chan, 2018a</td>
      <td>github: https://github.com/rcwchan/STROBE_software/ (copy archived at https://github.com/elifesciences-publications/STROBE_software)</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STROBE post- processing</td>
      <td>Chan, 2018a</td>
      <td>github: https://github.com/rcwchan/STROBE_software/ (copy archived at https://github.com/elifesciences-publications/STROBE_software)</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STROBE VHDL code</td>
      <td>Chan, 2018b</td>
      <td>github: https://github.com/rcwchan/STROBE-fpga (copy archived at https://github.com/elifesciences-publications/STROBE-fpga)</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>Schneider et al. (2012)</td>
      <td>https://imagej.nih.gov/ij; RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 6</td>
      <td>Graphpad</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Photoshop</td>
      <td>Adobe</td>
      <td>RRID:SCR_014199</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Illustrator</td>
      <td>Adobe</td>
      <td>RRID:SCR_010279</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Fly genotype table

<table>
  <thead>
    <tr>
      <th>Figure panel</th>
      <th>Genotype</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1C</td>
      <td>+/+; vGlutMI04979-Gal4/+; UAS-CD8::tdTomato/+</td>
    </tr>
    <tr>
      <td>Figure 1D</td>
      <td>+/+; vGlutMI04979-Gal4/LexAop-CD2::GFP ; UAS-CD8::tdTomato/ChATMI04508- LexA::QFAD</td>
    </tr>
    <tr>
      <td>Figure 1E</td>
      <td>+/+; vGlutMI04979-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Ppk28-LexA</td>
    </tr>
    <tr>
      <td>Figure 1F</td>
      <td>+/+; vGlutMI04979-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Gr64fLexA</td>
    </tr>
    <tr>
      <td>Figure 1G</td>
      <td>+/+; vGlutMI04979-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Gr66a-LexA</td>
    </tr>
    <tr>
      <td>Figure 1H</td>
      <td>+/+; vGlutMI04979-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Ppk23-LexA</td>
    </tr>
    <tr>
      <td>Figure 1I</td>
      <td>+/+; Gr66a-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Ppk23-LexA</td>
    </tr>
    <tr>
      <td>Figure 1J</td>
      <td>+/+; vGlutMI04979-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 1K</td>
      <td>Gr66a-LexA/+; LexAop-Gal80/UAS-GCaMP6f;  Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 1L</td>
      <td>+/+; UAS-CD8::tdTomato /LexAop-CD2::GFP; IR94e-Gal4/ppk28-LexA</td>
    </tr>
    <tr>
      <td>Figure 1M</td>
      <td>+/+; UAS-CD8::tdTomato /LexAop-CD2::GFP; IR94e-Gal4/Gr64fLexA</td>
    </tr>
    <tr>
      <td>Figure 1N</td>
      <td>+/+; UAS-CD8::tdTomato/LexAop-CD2::GFP; IR94e-Gal4/ppk23-LexA</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1A</td>
      <td>+/+; ChATMI04508-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1B</td>
      <td>+/+; UAS-CD8::tdTomato/LexAop-CD2::GFP; Ppk23-Gal4/Ppk23-LexA</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1C</td>
      <td>+/+; IR76b-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Ppk28-LexA</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1D</td>
      <td>+/+; IR76b-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Gr64fLexA</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1E</td>
      <td>+/+; IR76b-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Gr66a-LexA</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1F</td>
      <td>+/+; IR76b-Gal4/LexAop-CD2::GFP; UAS-CD8::tdTomato/Ppk23-LexA</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1G</td>
      <td>+/+; UAS-CsChrimson/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 2C and D</td>
      <td>+/+; LexAop-GCaMP6f/+; Ppk28-LexA/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-GCaMP6f/Gr64f-Gal4; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-GCaMP6f/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-GCaMP6f/Gr66a-Gal4; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-GCaMP6f/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1A–D</td>
      <td>+/+; UAS-GCaMP6f/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 2</td>
      <td>+/+; UAS-GCaMP6f/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 3A</td>
      <td>+/+; UAS-GCaMP6f/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 3B</td>
      <td>+/+; UAS-GCaMP6f/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; vGlutMI04979-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 3C and D</td>
      <td>Gr66a-LexA/+; LexAop-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; vGlutMI04979-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 1A and B</td>
      <td>+/+; ChATMI04508-Gal80/UAS-GCaMP6f; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 4A and B</td>
      <td>+/+; Gr64f-Gal4/UAS-GCaMP6f; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/UAS-GCaMP6f; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4, UAS-GCaMP6f/UAS-IR76b; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/UAS-GCaMP6f; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/UAS-GCaMP6f; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4, UAS-GCaMP6f/UAS-IR76b; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Ppk23-LexA/LexAop-GCaMP6f; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Ppk23-LexA/LexAop-GCaMP6f; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-GCaMP6f/UAS-IR76b; IR76b1, Ppk23-Gal4/IR76b2</td>
    </tr>
    <tr>
      <td>Figure 4C</td>
      <td>+/+; Ppk23-LexA/LexAop-GCaMP6f; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Ppk23-LexA/LexAop-GCaMP6f; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td>Figure 4D</td>
      <td>+/+; +/+; IR76b1/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/UAS-IR76b; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/UAS-IR76b; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td>Figure 4E</td>
      <td>+/+; +/+; IR76b1/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/UAS-IR76b; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/+; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/UAS-IR76b; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; Ppk23-Gal4,  IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/UAS-IR76b; Ppk23-Gal4, IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td>Figure 4—figure supplement 1A and B</td>
      <td>+/+; Ppk23-LexA/LexAop -GCaMP6f; IR76b2/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Ppk23-LexA/LexAop-GCaMP6f; IR76b1/IR76b2</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-GCaMP6f/ UAS-IR76b; IR76b1, Ppk23-Gal4/IR76b2</td>
    </tr>
    <tr>
      <td>Figure 4—figure supplement 2</td>
      <td>+/+; IR25a1/+; Gr64f- Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR25a1/IR25a2; Gr64f-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-IR25a, IR25a1/IR25a2; Gr64f-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR25a1/+; Gr66a-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR25a1/IR25a2; Gr66a-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-IR25a, IR25a1/IR25a2; Gr66a-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR25a1/+;  Ppk23-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR25a1/IR25a2; Ppk23-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-IR25a, IR25a1/IR25a2;  Ppk23-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td>Figure 4—figure supplement 3A and B</td>
      <td>ΔPpk23/ΔPpk23; ΔPpk29/ΔPpk29; Ppk23-Gal4/UAS-GCaMP6f</td>
    </tr>
    <tr>
      <td>Figure 5A</td>
      <td>+/+; +/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; IR94e-Gal4/UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+;  LexAop-Gal80/+; Ppk23-Gal4/UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; Ppk28-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; Ppk28-Gal4/ UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR76b-Gal4/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; IR76b-Gal4/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+;  IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; IR94e-Gal4/UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td>Figure 5B</td>
      <td>+/+; +/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td>Figure 5C</td>
      <td>+/+; +/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+;  LexAop-Gal80/+; Ppk23-Gal4/UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td>Figure 5D</td>
      <td>+/+; +/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/+; Ppk23-Gal4/UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td>Figure 5—figure supplement 1</td>
      <td>+/+; UAS-impTNT/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-TNT/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-impTNT/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-TNT/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr64f-Gal4/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-impTNT/Gr64f-Gal4; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-TNT/Gr64f-Gal4; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 5—figure supplement 2A</td>
      <td>Gr66a-LexA/+; LexAop-Gal80/+; Ppk23-Gal4/UAS-Kir2.1, tub-Gal80ts</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td>Figure 5—figure supplement 2B</td>
      <td>+/+; Gr66a-Gal4/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; Gr66a-Gal4/+; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; +/+; UAS-Kir2.1, tub-Gal80ts/+</td>
    </tr>
    <tr>
      <td>Figure 5—figure supplement 3</td>
      <td>+/+; UAS-GCaMP6f/+; Ppk23-Gal4/+</td>
    </tr>
    <tr>
      <td>Figure 6B</td>
      <td>+/+; UAS-CsChrimson/Gr64f-Gal4; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-CsChrimson/+; IR94e-Gal4/+</td>
    </tr>
    <tr>
      <td></td>
      <td>+/+; UAS-CsChrimson/Gr66a-Gal4; +/+</td>
    </tr>
    <tr>
      <td></td>
      <td>Gr66a-LexA/+; LexAop-Gal80/UAS-CsChrimson; Ppk23-Gal4/+</td>
    </tr>
  </tbody>
</table>

### Flies

Flies were raised on standard cornmeal fly food at 25°C in 70% humidity. The following genotypes were used: vGlutMI04979-Gal4, ChATMI04508-Gal4, vGlutMI04979-LexA::QFAD, ChATMI04508- LexA::QFAD, vGlutMI04979-Gal80, ChATMI04508-Gal80 (Diao et al., 2015); Gr66a-LexA, ppk28-LexA, ppk23-Gal4, UAS-CD8::tdTomato (Thistle et al., 2012); Gr64fLexA (Miyamoto et al., 2012); ppk23-LexA (Toda et al., 2012); IR76b-Gal4, IR76b1, IR76b2, UAS-IR76b (Zhang et al., 2013); IR25a1, IR25a2 (Benton et al., 2009); UAS-IR25a (Abuin et al., 2011); Gr66a-Gal4 (Wang et al., 2004); Gr64f-Gal4 (Dahanukar et al., 2007); Ppk28-Gal4 (Cameron et al., 2010); LexAop-CD2::GFP (Lai and Lee, 2006); UAS-Kir2.1 (Baines et al., 2001); tub-Gal80ts (McGuire et al., 2004); IR94e-Gal4 (Tirián and Dickson, 2017)(Vienna Drosophila Resource Center: v207582); LexAop-Gal80 (32214), LexAop-GCaMP6f (44217), UAS-GCaMP6f (42747 and 52869), UAS-CsChrimson (55135), UAS-TNT (28838), UAS-impTNT (28840) (Bloomington Stock Center).

### Tastants

The following tastants were used: Sucrose, NaCl, KCl, NaBr, KBr, CsCl, CaCl2, Lobeline hydrochloride, Caffeine (Sigma-Aldrich); 7,11-heptacosadiene (7,11-HC), 7,11-nonacosadiene (7,11-NC), 7-tricosene (7 T), and cis-vaccenyl acetate (c-VA) (Cayman Chemical Company, Ann Arbor, MI). Tastants were mostly kept as 1 M stocks and diluted as needed. Lobeline hydrochloride was kept as a 1.25 mM stock. 7,11-heptacosadiene (7,11-HC), 7,11-nonacosadiene (7,11-NC), and 7-tricosene (7 T) were diluted in water to desired 0.0001 mg/ul. Cis-vaccenyl acetate (c-VA) was diluted to stock solution of 0.01 mg/ul in EtOH, and then diluted in water. All hydrocarbons stocks were kept at −20°C, diluted as needed, and stored at 4°C for up to seven days. 1% of each Ethanol and Hexanol were diluted in a mix with water and kept at 4°C as control solution for pheromone imaging.

### Immunohistochemistry

Immunofluorescence on labella was carried out as described (Jeong et al., 2016). Labella were dissected and fixed for 25 min in 4% paraformaldehyde in PBS + 0.2% Triton. After washing with PBS + triton (0.2%; PBST), labella were blocked in 5% NGS diluted with PBST for 40 min. The following primary antibodies were applied and incubated at 4°C overnight: chicken anti-GFP (1:1000, Abcam, Cambridge, UK, #13970) and rabbit anti-RFP (1:200, Rockland Immunochemicals, Pottstown, PA, #600-401-379). After washing for 1 hr, the following secondary antibodies were added for 2 hr: goat anti-chicken Alexa 488 (1:200, Abcam #150169) and goat anti-rabbit Alexa 647 (1:200, Thermo Fisher Scientific, Waltham, MA, #A21245). Labella were washed again for 40 min, placed on slides in SlowFade gold (Thermo Fisher Scientific), with small #1 coverslips as spacers.

Brain immunofluorescence was carried out as described previously (Chu et al., 2014). Primary antibodies used were chicken anti-GFP (1:1000, Abcam #13970) and mouse anti-brp (1:50, DSHB #nc82). Secondary antibodies used were goat anti-chicken Alexa 488 (1:200, Abcam #150169) and goat anti-rabbit Alexa 568 (1:200, Thermo Fisher Scientific #A11036).

All images were acquired using a Leica SP5 II Confocal microscope with a 25x water immersion objective. Images were processed in ImageJ (Schneider et al., 2012) and Adobe Photoshop.

### Labellar expression map annotation

To annotate the expression of different markers in the labellum, each sensillum was analyzed in 4 – 8 labella stained for each combination of markers. Confocal z-stacks were examined to identify how many neurons in each sensillum were positive for the different drivers, and which neurons overlapped with the respective co-labelled population. The most common result for each neuron in each sensillum was reported. Sensilla S0, I0, I9, and I10 were the most difficult to score because of viewing difficulties. At times there were duplications of specific sensilla on a labellum, in which case both sensilla were considered.

### GCaMP imaging

For calcium imaging experiments, female or male flies were aged from 2 to 10 days in groups of both sexes. Females were used for all experiments except where indicated (pheromones). Prior to imaging, flies were briefly anesthetized using CO2, legs amputated for full access to the proboscis, and placed in custom chamber suspended from their cervix. To ensure immobilization, a small drop of nail polish was applied to the back of the neck and the proboscis was pulled to extension and waxed out on both sides. A modified dental waxer was used to apply wax on each side of the chamber rim, making little contact with the feeding structure. Flies were left to recover in a humidified chamber for 1 hr. The antenna were removed from the fly and a small window of cuticle was removed from the top of the head, exposing the SEZ. Adult Hymolymph Like (AHL) buffer was immediately applied to the preparation (108 mM NaCl, 5 mM KCl, 4 mM NaHCO3, 1 mM NaH2PO4, 5 mM HEPES, 15 mM ribose, pH 7.5). The air sacs, fat, and esophagus were clipped and removed to allow clear visualization on the SEZ. Once ready to image, AHL buffer was added that includes Mg2+ and Ca2+ (108 mM NaCl, 5 mM KCl, 4 mM NaHCO3, 1 mM NaH2PO4, 5 mM HEPES, 15 mM ribose, 2 mM Ca2+, and 8.2 mM Mg2+).

GCaMP6f fluorescence was observed using a Leica SP5 II Confocal microscope with a 25x water immersion objective. The relevant area of the SEZ was visualized at a zoom of 4x, a line speed of 8000 Hz, a line accumulation of 2, and resolution of 512 × 512 pixels. The pinhole was opened to 2.98 AU. For each taste stimulation, data was acquired during a baseline of 5 s prior to stimulation, 1 s during tastant application, and 9 s following the stimulation.

Tastant stimulations were done using a pulled capillary pipette that was filed down to match the size of the proboscis and fit over all taste sensilla on both labellar palps. The pipette was filled with 1 – 2 μl of a tastant and positioned close to the proboscis labellum. At 5 s a micromanipulator was used to apply the tastant to the labellum manually. Between taste stimulations of differing solutions, the pipette was washed with water. All NaCl solutions were applied in the order of increasing concentration, finishing with 1M KCl. All other solutions were applied in random order to control for potential inhibitory effects between modalities.

The maximum change in fluorescence (ΔF/F) was calculated using the peak intensity (average of 3 time points) minus the average intensity at baseline (10 time points), divided by the baseline. Quantification of fluorescence changes was performed in ImageJ and graphed in GraphPad Prism6.

For quantification of Ppk23glut projections, the caffeine response for each fly was used to create a region of interest starting below the ‘bitter ring’ and extending across to encompass the lateral projections. This same region of interest was applied to the salt responses of that fly to exclude the Ppk23chat population overlapping with Gr66a in this ‘bitter ring’.

### Salt deprivation

Flies were placed in one of two conditions for 2 – 3 days: 1% agar, 5% sucrose, and 10 mM NaCl (salt fed); or 1% agar and 5% sucrose (salt deprived).

### Behavioral assays

Binary choice preference tests were similar to those previously described (LeDue et al., 2015). Female flies aged 2–5 days were sorted into groups of 10 and placed in conditions of either salt feeding or salt deprivation (see above) and shifted to 29°C for 48 hr to induce expression of Kir2.1 in the cells of interest. For the low salt assay, salt deprived flies were then tested directly. Flies for the high salt assay were subjected to a subsequent 12 hr on medium without sugar (but with the same salt content) to increase sugar attraction. For both assays, flies were then transferred into testing vials containing six 10 μL dots of agar that alternated in color. For most low salt attraction assays, the food choices were: 1% agar with both 2 mM sucrose and 50 mM NaCl (Food 1), and 1% agar with 2 mM sucrose (Food 2). The experiment in Figure 5B was done without sucrose. For the high salt avoidance assays, the food choices were: 1% agar with both 25 mM sucrose and 250 mM NaCl (Food 1), and 1% agar with 5 mM sucrose (Food 2). Each choice contained either 0.125 mg/mL blue (Erioglaucine, FD and C Blue#1) or 0.5 mg/mL red (Amaranth, FD and C Red#2) dye, and half the replicates for each experiment were done with the dyes swapped to control for any dye preference. Flies were allowed to feed for 2 hr in the dark at 29°C and then frozen and scored for abdomen color. Preference index (PI) was calculated as ((# of flies labeled with Food 1 color) – (# of flies labeled with Food 2 color))/(total number of flies that fed).

For PER, 2 – 5 day old females were collected and treated exactly as described above for salt fed and deprived conditions. Flies were then mounted inside pipette tips that were cut to size so that only the head was exposed. The tubes were sealed at the end with tape, positioned on a glass slide with double-sided tape. After a 1 – 2 hr recovery, flies were stimulated with water and allowed to drink until satiated. Each fly was then stimulated on the labellum with increasing concentrations of salt (0 mM salt, 250 mM NaCl, 500 mM NaCl, 1 M NaCl, and 1 M KCl) mixed with 100 mM sucrose using a 20 μL pipette attached to a 1 mL syringe. Stimuli were presented three times each per fly. Four groups of 10 flies for each genotype were tested over four days. The order of genotypes tested on each day was randomized.

### STROBE system

The STROBE builds on the FlyPAD system’s hardware (Itskov et al., 2014) by adding a lighting circuit and opaque curtain (to prevent interference from outside lighting) to each of 16 FlyPAD arenas. Thus, together, a functioning STROBE system consists of a field programmable gate array (FPGA) controller attached to a multiplexor board, adaptor boards, fly arenas equipped with capacitive sensors, and lighting circuits.

The arrangement of the STROBE chambers mirrors the design of the FlyPAD, except each of the eight adaptor boards connects to two FlyPAD arenas and two lighting units instead of the original four FlyPAD arenas. These adaptor boards link the chambers to the FPGA, which is a Terasic DEV0-Nano mounted onto a custom multiplexor board with a FTDI module allowing data transfer over serial communications with a computer. The multiplexor board has eight 10-pin ports, each of which connects to an adaptor board that splits the 10-pin line into four 10-pin ports connecting to two fly arenas and two lighting circuits. The fly arena consists of two annulus shaped capacitive sensors and a CAPDAC chip (AD7150BRMZ) that the main multiplexer board communicates with to initiate and collect data (and ultimately stop collecting data). The CAPDAC interprets data from the two capacitive sensors on the fly-arena (Itskov et al., 2014).

The lighting circuit consists of connectors for power from an external power supply and for signaling from the FPGA controller via the intermediate components, a 617 nm light emitting diode (LUXEON Rebel LED – 127lm @ 700mA; Luxeon Star LEDs #LXM2-PH01-0060), two power resistors (TE Connectivity Passive Product SMW24R7JT) for LED current protection, and two metal oxide semiconductor field effect transistors (MOSFETs; from Infineon 634 Technologies, Neubiberg, Germany, IRLML0060TRPBF) allowing for voltage signal switching of the LEDs.

When the signal from a capacitive sensor rises during a fly sip (or other food interaction), the CAPDAC on the fly arena propagates a signal through the adaptor board via the multiplexor to the FPGA controller. The FPGA processes the capacitive sensor signal using code built atop the original VHDL code from the FlyPAD (Itskov et al., 2018). The STROBE VHDL code (Chan, 2018b) implements a running minima filter that operates in real-time to detect when a fly is feeding or otherwise interacting with the food. The filter determines the minimum signal value in the last 100 ms and compares the current signal value with this minimum. If the current signal value is greater than the minimum, and the difference between them is greater than a threshold set to exceed noise (100 units for all experiments), this is considered a rising edge and the filter will prompt the lighting activation system to activate the LED (or keep it on if it is already on). By design, this means that the control system will send a signal to deactivate the lighting upon the falling edge of the capacitance signal, or if the capacitance signal has plateaued for 100 ms, whichever comes sooner. At this point, a low signal is sent to the MOSFET which pinches off the current flowing through the lighting circuit, turning off the light. The signal to lighting response transition times are on the order of tens of milliseconds, providing a nearly instantaneous response.

The system automatically records the state of the lighting activation system (on/off) and transmits this information through USB to the PC, where it is received and interpreted by a custom end-user program (built using Qt framework in C++) which can display both the activation state and signal measured by the STROBE system in each fly arena in real-time.

All STROBE software is available for download from Github:

FPGA code: https://github.com/rcwchan/STROBE-fpga

All other code: https://github.com/rcwchan/STROBE_software/

### STROBE experiments

Flies were place in vials for three days under ‘salt fed’ or ‘salt deprived’ conditions described above. All flies were 5 – 9 days old at the time of the assay. For retinal groups, food was supplemented with all trans-Retinal at a final concentration of 1 mM (Sigma-Aldrich).

Both channels of STROBE chambers were loaded with 4 μl of 1% agar (GR64f and IR94e experiments) or 1M sucrose mixed in 1% agar (Gr66a and Ppk23glut experiments). Acquisition on the STROBE software was started and then single flies were transferred into each arena by mouth aspiration. Experiments were run for 60 min, and the preference index for each fly was calculated as: (sips from Food 1 – sips from Food 2)/(sips from Food 1 + sips from Food 2).

### Statistical analysis

Statistical tests were performed using GraphPad Prism six software. Descriptions and results of each test are provided in the figure legends. Sample sizes are indicated in the figure legends. Sample sizes were determined prior to experimentation based on the variance and effect sizes seen in prior experiments of similar types. Whenever possible, all experimental conditions were run in parallel and therefore have the same or similar sample sizes. However, in some cases this was impossible, due to the concurrent availability of different genotypes or the size of the experiment. These situations account for instances where some control genotypes have very large sample sizes, since they were run in parallel with multiple experimental groups (e.g. Figure 5A).

All replicates were biological replicates using different flies. Data for all quantitative experiments were collected on at least three different days, and behavioral experiments were performed with flies from at least two independent crosses. Specific definitions of replicates are as follows. For calcium imaging, each data point represents the response of a single fly to the indicated stimulus. A given fly was stimulated with a specific tastant only once. For binary choice behavioral tests, each data point represents the calculated preference for a group of 10 flies. For PER, each replicate is composed of 10 independent flies tested in parallel. For STROBE experiments, each data point is the calculated preference of an individual fly over the course of the experiment.

Outliers were occasionally observed but were not removed from the datasets. For example, in Figure 2D, two flies had strong water responses in Gr64f sweet neurons. Although these appear to be outliers, we left them in the dataset because there was no other justification for removing them.

There were two conditions where data were excluded that were determined prior to experimentation and applied uniformly throughout. First, in calcium imaging experiments, all the data from a fly were removed if either: a) there was too much movement during stimulation to reliably quantify the response; or b) there was no response to a known, robust, positive control (rare). Second, for STROBE experiments, the data from individual flies were removed if the fly did not pass a set minimum threshold of sips (15), or the data showed hallmarks of a technical malfunction (rare).

A third condition for data exclusion arose during pilot experiments and was then applied subsequently: A subset of flies expressing GCaMP in IR94e neurons (~20%) showed a large response to water alone. These flies were removed from the analysis.

All the quantitative data used for statistical tests can be found as supplements for each figure.
