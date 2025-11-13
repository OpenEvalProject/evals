# Axonal injury signaling is restrained by a spared synaptic branch

## Authors

- Laura J Smithson<sup>1</sup> ([ORCID: 0000-0003-1529-3005](https://orcid.org/0000-0003-1529-3005))
- Juliana L Zang<sup>1</sup> ([ORCID: 0000-0002-5738-8355](https://orcid.org/0000-0002-5738-8355))
- Lucas Junginger<sup>1</sup>
- Thomas J Waller<sup>1</sup> ([ORCID: 0000-0002-3098-9070](https://orcid.org/0000-0002-3098-9070))
- Lauren Reilly-Jankowiak<sup>2</sup> ([ORCID: 0000-0002-7496-6866](https://orcid.org/0000-0002-7496-6866))
- Sophia A Khan<sup>2</sup> ([ORCID: 0009-0004-1416-5022](https://orcid.org/0009-0004-1416-5022))
- Ye Li<sup>3</sup> ([ORCID: 0000-0002-8647-384X](https://orcid.org/0000-0002-8647-384X))
- Dawen Cai<sup>3</sup> ([ORCID: 0000-0003-4471-2061](https://orcid.org/0000-0003-4471-2061))
- Catherine A Collins<sup>1</sup> ([ORCID: 0000-0002-1608-6692](https://orcid.org/0000-0002-1608-6692)) †

### Affiliations

1. Department of Molecular, Cellular and Developmental Biology, University of Michigan Ann Arbor United States ([ROR:00jmfr291](https://ror.org/00jmfr291))
2. Department of Neurosciences, Case Western Reserve University Cleveland United States ([ROR:051fd9666](https://ror.org/051fd9666))
3. Department of Cell and Developmental Biology, University of Michigan Ann Arbor United States ([ROR:00jmfr291](https://ror.org/00jmfr291))

† Corresponding author

## Abstract

The intrinsic ability of injured neurons to degenerate and regenerate their axons facilitates nervous system repair; however, this ability is not engaged in all neurons and injury locations. Here, we investigate the regulation of a conserved axonal injury response pathway with respect to the location of damage in branched motoneuron (MN) axons in Drosophila larvae. The dileucine zipper kinase (DLK; also known as MAP3K12 in mammals and Wallenda (Wnd) in Drosophila) is a key regulator of diverse responses to axonal injury. In three different populations of MNs, we observed the same striking result that Wnd/DLK signaling becomes activated only in response to injuries that remove all synaptic terminals. Injuries that spared even a small part of a synaptic terminal were insufficient to activate Wnd/DLK signaling, despite the presence of extensive axonal degeneration. The regulation of injury-induced Wnd/DLK signaling occurs independently of its previously known regulator, the Hiw/PHR ubiquitin ligase. We propose that Wnd/DLK signaling regulation is linked to the trafficking of a synapse-to-nucleus axonal cargo and that this mechanism enables neurons to respond to impairments in synaptic connectivity.

## Introduction

Repair of nervous system damage requires an ability of neurons to regenerate axons and synaptic connections. However, this ability is not universally induced following injury, most notably following spinal cord injury. While many studies have identified extrinsic factors that influence or inhibit axonal regeneration, several studies have noted that the location of damage can influence the intrinsic ability of the neuron to mount a transcriptional response to the damage (Fernandes et al., 1999; Lorenzana et al., 2015; Mason et al., 2003; Wang et al., 2024). Some studies have noted an effect of distance from the cell body for long axons in the spinal cord (Fernandes et al., 1999; Mason et al., 2003; Wang et al., 2024). Other studies have noted that the location of injury with respect to an axonal branching point also strongly influences the response (Lorenzana et al., 2015; Wu et al., 2007). Even in a strongly inhibitory environment to regeneration, dorsal column sensory axons show robust axonal growth when injured proximal to their bifurcation in the spinal cord (Lorenzana et al., 2015).

Here, we investigate the regulation of a conserved axonal injury response pathway with respect to the location of axonal injury. The dileucine zipper kinase (DLK; known as MAP3K12 in mammals and Wallenda (Wnd) in Drosophila) is a key regulator of diverse responses to axonal injury. These include an essential role in the ability of damaged neurons to initiate axonal regeneration in worm and fly models (Chen et al., 2011; Hammarlund et al., 2009; Stone et al., 2014; Xiong et al., 2010; Yan et al., 2009), synaptic repair and recovery following CCR5 inhibition in a stroke model (Joy et al., 2019), and enhanced regeneration and mechanical allodynia following PNS nerve damage in mice (Hu et al., 2019; Wlaschin et al., 2018). Dichotomously, DLK is also required for the death of retinal ganglion cells following optic nerve damage (Watkins et al., 2013; Welsbie et al., 2017; Welsbie et al., 2013). In mammalian as well as in fly neurons, this kinase associates with vesicles that are physically transported in axons (Holland et al., 2016; Xiong et al., 2010), while downstream nuclear signaling requires functional axonal transport machinery (Xiong et al., 2010). DLK is therefore considered to function as a ‘sensor’ of axonal damage, whose activation can confer responses of repair or death, depending upon the cellular context (Asghari Adib et al., 2018).

While the responses gated by DLK are impactful for neurons and their circuits, the mechanism(s) that lead to DLK signaling activation are still poorly understood. A number of observations have documented DLK signaling activation in neurons that are not mechanically damaged but have experienced some form of cellular stress. These include the presence of cytoskeletal mutations (Bounoutas et al., 2011; Chen et al., 2014; Kurup et al., 2015; Valakh et al., 2013) and the presence of chemotherapy agents (Bhattacharya et al., 2012; DeVault et al., 2024; Valakh et al., 2015) known to impair axonal cytoskeleton integrity and transport. DLK activation is also responsible for phenotypes associated with mutations in the unc-104/KIF1A kinesin (Li et al., 2017), a major carrier of synaptic vesicle precursors in axons (Guedes-Dias and Holzbaur, 2019; Petzoldt, 2023). Inhibition of DLK is protective in mouse models of Amyotrophic Lateral Sclerosis (ALS) and Alzheimer’s disease (Le Pichon et al., 2017; Patel et al., 2017). These observations have fostered growing interest in DLK as a potential therapeutic target and in understanding the mechanisms that control DLK signaling activation in neurons.

Here, we test the hypothesis that DLK/Wnd signaling is tuned to the synaptic connectivity of a neuron. A shared feature of nerve injuries and stressors that disrupt axonal cytoskeleton and transport is a loss in downstream connections. A conserved regulator of DLK/Wnd, the E3-ubiquitin ligase PAM/Highwire/Rpm-1/Phr1 (Collins et al., 2006; Huntwork-Rodriguez et al., 2013; Nakata et al., 2005), is hypothesized to function at synaptic terminals (Abrams et al., 2008; Opperman and Grill, 2014; Xiong et al., 2012; Zhen et al., 2000). This led us to ask whether interactions at an intact synaptic terminal are responsible for restraining Wnd signaling in uninjured neurons. We probed this hypothesis through injuries to branched motoneuron (MN) axons in Drosophila larvae, which allowed us to compare injuries that leave spared synaptic terminals to injuries that lead to complete denervation. In three different populations of MNs, we observed the same striking result that Wnd signaling becomes activated only in response to injuries that remove all synaptic terminals. Injuries that spared even a small part of a synaptic terminal did not activate Wnd signaling, despite the presence of extensive axonal degeneration. Surprisingly, removal of all synapses led to additive induction of Wnd signaling in hiw mutants. These observations suggest the existence of a mechanism that restrains Wnd signaling at synaptic terminals independently of the Hiw ubiquitin ligase.

## Results

### The presence of a spared synaptic branch restrains Wnd-mediated injury signaling in SNc MNs

To determine whether synaptic connections influence injury signaling by Wnd/DLK, we established methods to injure single synaptic branches of defined larval MNs. The m12 (5053A)-Gal4 driver line (Ritzenthaler et al., 2000) that we have used in previous nerve injury studies (Xiong et al., 2010; Xiong and Collins, 2012), drives expression in two single MNs that project closely fasciculated axons to innervate body wall muscles 26, 27, and 29 (Figure 1A). This pattern was previously attributed to an MN named MNSNc, which was noted to have ‘two cell bodies’ (Kim et al., 2009). We used the Bitbow2 (Li et al., 2021) multi-colored cell labeling approach to resolve the two neurons and observed an invariable pattern that one MNSNc neuron innervates muscles 26 and 29, while the other innervates muscle 27. Figure 1B shows two examples: the neuron that innervates muscle 27 (middle images) expresses a set of colors that distinguish it from the terminals on muscles 26 and 29. We therefore refer to these two neurons labeled by the m12Gal4 driver as MNSNc-26/29 and MNSNc-27 (Figure 1A, B, Figure 1—figure supplement 1). MNSNc-26/29 (cartooned in blue in Figure 1A) has three collateral branches: two branches innervate muscle 26, and a single branch innervates muscle 29. MNSNc-27 (cartooned in red in Figure 1A) has two collateral branches that innervate muscle 27: these two branches most often remain together and occasionally bifurcate separately onto muscle 27 (Figure 1—figure supplement 1A). This innervation is stereotyped across segments and animals. As previously noted (Kim et al., 2009), the paired cell bodies of the MNSNc neurons are found on the lateral sides of the abdominal region of the ventral nerve cord (VNC). Bitbow2 expression revealed that the MNSNc-27 cell somas are positioned more ventrally compared to the cell somas of MNSNc-26/29 in the VNC (Figure 1—figure supplement 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig1-v1.jpg)

**Figure 1.:** (A) Schematic representation of the two SNc motoneurons innervating muscles 26 and 29 (MNSNc-26/29, red) and muscle 27 (MNSNc-27, blue), which are labeled by expression of the m12-Gal4 driver. (B) Example images of NMJ terminals from m12-Gal4/+; UAS-BitBow2 (Li et al., 2021)/+third instar larvae, used to define the connectivity shown in A. The neuron that innervates muscle 27 (MNSNc-27) expresses a distinct set of colors from the Bitbow2 (Li et al., 2021) reporter than the neuron that innervates muscles 26 and 29 (MNSNc-26/29). (C) Confirmation of puc-lacZ induction following laser axotomy. The cartoons on the top row show the location used to injure both axons; this location removes all of the synaptic branches from both MNSNc-26/29 and MNSNc-27. The middle row shows example injuries (versus uninjured, right) at the indicated location in m12-Gal4, UAS-mCD8GFP/puc-lacZ larvae. The bottom row shows examples of puc-lacZ expression (red channel) in the MNSNc cell bodies 24 hr following injury. (D) Example MNSNc-26/29 (blue) and MNSNc-27 (red) neurons injured at different locations. (E) Quantification of puc-lacZ intensity measurements in MNSNc-26/29 (blue) and MNSNc-27 (red) following injuries that remove all synaptic branches versus injuries that leave a spared synaptic branch. Injury location (a) removes the small number of boutons on muscle 29 while sparing the boutons on muscle 26. Injury location (b) removes boutons from muscle 29 and the posterior sub-branch on muscle 26. Injury location (c) removes all branches except for the small number of boutons on muscle 29. Note that all injuries that leave spared boutons (hatched shading) show no puc-lacZ induction, regardless of the number of boutons lost or spared. A one-way ANOVA with Tukey test for multiple comparisons was performed for each neuron. ****p < 0.0001; ***p < 0.001; **p < 0.01; ns = not significant.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Cartoon denoting nomenclature of MNSNc-26/29 (red) and MNSNc-27 (blue) branches. (B) Example images of nerve terminals and cell bodies of m12-Gal4; UAS-Bitbow2 labeled MNSNc neurons, used to confirm the anatomy. (C) Similarly to laser axotomy in Figure 1C, nerve crush injury (24 hr) induces puc-lacZ expression in both MNSNc neurons, but not in MNSNc neurons that co-express wnd-RNAi. (D) Synaptic terminals (top row) and cell bodies (bottom row) of aCC motoneurons on muscle 1, labeled in Dpr4-Gal4, UAS-mCD8-GFP larvae. puc-lacZ expression (red) is induced following injuries that result in loss of all synaptic boutons but not following injuries to one branch that leave the other branch intact. (E) Quantification of puc-lacZ intensities in aCC neurons. A one-way ANOVA with Tukey test for multiple comparisons was performed. ****p < 0.0001; ns = not significant. Full (F) but not partial (G) removal of synaptic branches induces stability and trafficking ectopically expressed kinase-dead GFP-Wnd-KD (in UAS-GFP-Wnd-KD; m12-Gal4, UAS-mCD8-RFP animals). Synaptic branches from muscle 27 (F), or muscle 29 (G) were axotomized by laser surgery and imaged following 24 hr. The white asterisk (*) marks the injury location. (F) GFP-Wnd-KD protein accumulates at the proximal tip of axons that have lost all synaptic boutons. (G) GFP-Wnd-KD is barely detectable in axons following injuries that leave spared synaptic branches. Not shown, GFP-Wnd-KD levels in G are similar in uninjured MNSNc axons.

We used a pulsed dye laser to carry out axotomies of MNSNc axons at different locations in intact immobilized larvae (described in methods, Smithson et al., 2025). Successful injuries were confirmed by the degeneration of distal stumps within 24 hr post-injury. To assess the activation of Wnd signaling, we probed for the induction of puckered expression from the puc-lacZ enhancer trap (Martin-Blanco et al., 1998). Previous studies using this reporter line have shown that expression of nuclear localized lacZ is strongly induced following nerve injury, requiring Wnd, JNK, and the Fos transcription factor (Xiong et al., 2010). We confirmed this is the case for MNSNc neurons; axotomy of the m12-Gal4 labeled neurons upstream of the synaptic branches led to a fourfold induction of puc-lacZ expression in both neurons 24 hr after injury; this was abolished in neurons that co-express double-stranded RNAi targeting wnd (Figure 1C). Similar results were observed for nerve crush injuries (Figure 1—figure supplement 1C).

In contrast to axotomies that removed all synaptic branches, laser injury to single collateral branches of MNSNc-26/29, including branches innervating either muscle 26 or 29 and resulting in spared synaptic branches, did not induce puc-lacZ expression (Figure 1D, E). In addition, laser ablation of the anterior branch of MNSNc-27 was also insufficient to activate Wnd signaling (Figure 1D, E). We note that the induction of puc-lacZ did not correlate with the number of boutons that were lost or spared. MNSNc-26/29 forms fourfold more boutons on muscle 26 (17 ± 3.8) than 29 (4 ± 1.3). However, injuries that spared any of the branches, even the small number on muscle 29, showed equivalent puc-lacZ levels to uninjured neurons (Figure 1E; compare injury locations a, b, and c). We carried out similar experiments in aCC MNs, which can be labeled with the Dpr4-Gal4 driver (Pérez-Moreno and O’Kane, 2019). Laser axotomies that removed all of the synaptic branches resulted in a fourfold increase in puc-LacZ levels, while injuries that left spared synaptic boutons did not induce puc-lacZ expression (Figure 1—figure supplement 1D, E). These observations suggested that even a small number of remaining boutons was sufficient to restrain the activation of puc-lacZ expression.

Despite the small distance from the disconnected muscle, none of the injured MNSNc synaptic branches were able to re-innervate the muscle. We think this is due to an absence of axon growth-promoting cues, since MNSNc axons did show robust but misdirected axonal growth into the segmental nerve SNa following injuries in locations upstream of the synaptic branches (data not shown). However, we did notice differences in the trafficking of proteins to injured proximal stumps. An example of this is shown for ectopically expressed kinase-dead Wnd transgenic protein, GFP-Wnd-KD in Figure 1—figure supplement 1F, G. We were only able to track kinase-inactive Wnd since overexpression of Wnd causes dramatic morphological defects to neurons (Collins et al., 2006; Feoktistov and Herman, 2016; Xiong et al., 2010). GFP-Wnd-KD was strongly induced and accumulated at the proximal stump following injuries that removed all synaptic branches but was barely detectable following injuries that left spared synaptic branches (Figure 1—figure supplement 1F, G). Collectively, these observations suggest that the presence of spared synaptic branches affects the subsequent events that occur in the injured axon. These include the stability and/or trafficking of Wnd protein in injured axons and the activation of Wnd-regulated signaling in the neuron soma.

### Restraint of Wnd-dependent injury signaling in bifurcated axons of type II VUM MNs

A more extreme example of axonal branching is illustrated by the ventral unpaired median neurons, which project symmetric bifurcated axons through separate nerves to innervate multiple body wall muscles on both left and right sides of the larva (Figure 2A, Figure 2—figure supplement 1; Koon et al., 2011; Monastirioti et al., 1995; Vömel and Wegener, 2008). VUM neurons can be specifically labeled based on their expression of tyrosine decarboxylase 2 using the Tdc2-Gal4 driver. Each abdominal segment has three VUM neurons, each of which sends a single axon dorsally which then bifurcates in the midline VNC (Figure 2—figure supplement 1; Vömel and Wegener, 2008). The two bifurcations then project through separate nerves to symmetrically innervate both left and right halves of the larval body. Through nerve crush injuries to only one ventral side of the animal, we were able to injure one bifurcation while leaving the other bifurcation intact. Successful injuries were determined based on the degeneration of the distal axon and synaptic terminals at 24 hr post-crush (Figure 2B). Whether both bifurcations, a single bifurcation, or neither bifurcation was injured was scored for each VUM neuron by tracing the Tdc2-Gal4, UAS-mCD8GFP labeled axons from the nerve to the cell body.

![Figure 2.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig2-v1.jpg)

**Figure 2.:** (A) Cartoon of ventral unpaired median (VUM) neurons, which have bifurcated axons that symmetrically innervate body wall muscles on both the left and right sides of the animal. Nerve crush to either left or right side of the animal can axotomize a single bifurcation while leaving the other bifurcated axon intact. (B) Example images of VUM axons (visualized in Tdc2-Gal4, UAS-mCD8-GFP larvae) in segmental nerves on the uninjured and injured sides following nerve crush to a single side. (C) Example images of puc-lacZ expression in the VNC (ventral nerve cord) of larvae following nerve crush to a single side (half crush) versus crush to all the segmental nerves (full crush). puc-lacZ expression (red) is induced in VUM neurons (white) only after full crush. In contrast, other motoneurons, which innervate a single side, are induced by both half and full crush injuries. Co-expression of UAS-wnd-RNAi in VUM neurons cell autonomously inhibits puc-lacZ induction. (D) Quantification of puc-lacZ intensity measurements in VUM neurons. A one-way ANOVA with Tukey test for multiple comparisons was performed. ****p < 0.0001; ns = not significant. Scale bars = 20 µm.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A–E) Views of Tdc2-Gal4, UAS-mCD8-GFP expressing VUM neurons to illustrate their anatomy. (A) Individual confocal plane that shows three cell bodies in individual segments, which lie in the middle of the nerve cord. (B) Side view and (C) top view that show the locations of the bifurcations. (D) Cartoon of the three neurons from one segment, showing their bifurcations to symmetrical sides of the animal. (E) Composite and camera lucida views of the NMJ terminals for the three neurons on one abdominal hemisegment. The three Tdc2 neurons each form stereotyped branches to innervate a unique group of muscles. (F) Example results from laser axotomies to individual Tdc2/VUM neurons (24 hr after injury) on either one side or both sides of the animal. Surgeries were carried out at the indicated locations which lie upstream of the final synaptic branches (at the transition zone between the segmental nerve and abdominal muscles). The stereotyped anatomy allows for identification of each VUM neuron (labeled 1, 2, and 3). Injured branches are marked with an asterisk while spared branches are marked with squares. For each neuron, only injuries to both bifurcations allowed for induction of puc-lacZ. Scale bars = 20 um.

Similarly to other MNs (Xiong et al., 2010), puc-lacZ expression is barely detectable in uninjured VUM MNs and, compared to uninjured VUM neurons, is induced almost threefold at 24 hr following complete/full nerve crush injuries that damage both bifurcations and remove all synaptic connections (Figure 2C, D). This induction is abolished in VUM neurons that co-express wnd-RNAi (Figure 2C, D). Note that wnd-RNAi is only expressed in the VUM neurons and does not affect the other MNs which do not express Tdc2-Gal4. In contrast to full nerve crushes, injuries to nerves on a single side of the animal that the other bifurcation was intact (‘half crush’ injuries) did not induce puc-lacZ expression in VUM neurons (Figure 2C, D). Most MNs make ipsilateral and not bilateral projections; in ‘half-crush’ injuries, puc-lacZ is induced in most non-VUM MNs on the side of the crush, but is not induced in VUMs. These combined observations suggest that in Drosophila MNs, Wnd signaling is not tuned to detect axonal damage per se, but is instead uniquely tuned to detect a complete loss of innervation, which occurs following some injuries but not others.

### Restraint of Wnd signaling at spared branches does not require synaptic transmission

Since the presence of intact synaptic boutons restrains Wnd signaling activation, we considered whether cellular events associated with evoked or spontaneous synaptic transmission are associated with this mechanism. Summarized, we tested a total of 22 genetic manipulations expected to inhibit synaptic transmission, but none led to a change in puc-lacZ expression. These include electrical silencing of SNc MNs by Gal4/UAS-mediated expression of the Drosophila open rectifier K+ channel (dORK) (Nitabach et al., 2002), silencing of transmission using temperature-sensitive mutations in dynamin (Kitamoto, 2001), and light-induced silencing of neurons expressing Guillardia theta anion channelrhodopsin 1 (gtACR1) (Mohammad et al., 2017; Supplementary file 1). Consistent with these negative results, we noted that previous studies have described many genetic manipulations that perturb evoked and/or spontaneous synaptic transmission (Choi et al., 2014; Daniels et al., 2006; DiAntonio and Schwarz, 1994; Han et al., 2022; Kim et al., 2012; Mosca et al., 2005; Pittendrigh et al., 1997) do not yield synaptic phenotypes (of synaptic overgrowth or decreased VGlut expression levels) associated with Wnd activation (Collins et al., 2006; Li et al., 2017).

### Restraint of Wnd-mediated axon injury signaling is independent of the Highwire ubiquitin ligase

We then asked whether a known upstream regulator of Wnd signaling, the Pam/Hiw/Rpm-1 (PHR) ubiquitin ligase, functions to restrain Wnd at synaptic branches. PHR is a large protein with multiple evolutionarily conserved domains, inducing a RING-finger domain, which regulates DLK/Wnd in invertebrate (C. elegans and Drosophila) (Collins et al., 2006; Nakata et al., 2005) and vertebrate (Huntwork-Rodriguez et al., 2013) model organisms. PHR is an attractive candidate since it localizes to synaptic terminals (Abrams et al., 2008; Opperman and Grill, 2014; Zhen et al., 2000) and loss of PHR function leads to increased levels of Wnd/DLK at synapses (Collins et al., 2006; Nakata et al., 2005). This hypothesis predicts that removal of all synaptic branches would be equivalent to a genetic loss in PHR function. We tested this in null mutants for the Drosophila ortholog of PHR, Highwire (Hiw). The hiwΔN mutation deletes the entire N-terminal half of the hiw gene and abolishes expression of the Hiw protein (Wu et al., 2005). Since hiwΔN animals are viable, we were able to carry out injury assays in neurons that completely lack Hiw function.

Consistent with previously reported phenotypes for hiw in other MN types (Collins et al., 2006; Wan et al., 2000; Wu et al., 2005), uninjured MNSNc neurons in male hiwΔN mutants have an increased number of axon collateral and terminal branches at muscles 26, 29, and 27 NMJs (Figure 3A, Figure 3—figure supplement 1). Also consistent with previous observations, uninjured neurons show elevated expression of puc-lacZ in hiwΔN mutants compared to control animals (Figure 3, Figure 3—figure supplement 1). Strikingly, injuries that removed all synaptic terminals led to an even further elevation of puc-lacZ expression in hiwΔN mutant neurons. This was the case for laser axotomies that removed all synaptic branches from either MNSNc-26/29 and/or MNSNc-27 neurons (Figure 3A, right column, and Figure 3B), and also for VUM neurons following nerve crush injuries (Figure 3C). Injuries to a single synaptic branch (on muscle 29) of MNSNc-26/29 in hiwΔN mutants had a similar level of puc-lacZ expression as uninjured hiwΔN neurons (Figure 3A, B). Collectively, these observations suggest that the presence of a spared synapse is capable of restraining Wnd signaling independently of Hiw’s function.

![Figure 3.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig3-v1.jpg)

**Figure 3.:** (A) Laser axotomy is carried out to MNSNc neurons at a location (indicated by asterisk (*)) that completely removes the synaptic terminal of MNSNc-27 (red neuron). The injury also leads to loss of the MNSNc-26/29 (blue) terminal on muscle 29 but not 26, hence leaves a spared synaptic branch. The final column shows an axotomy that fully removes the terminals for both MNSNc neurons. These injuries were repeated in control animals versus the background of a hiw null mutant, hiwΔN. (B) Quantification of puc-lacZ expression for individual MNSNc neurons after full versus spared axotomies, compared to uninjured neurons. Basal puc-lacZ expression is already elevated in uninjured hiwΔN neurons compared to control. This can be further elevated in axotomies that remove all synapses, but not in axotomies that leave spared branches. (C) Quantification of puc-lacZ in VUM neurons (labeled by Tdc-2-Gal4; UAS-mCD8-GFP) 24 and 48 hr following full nerve crush in control versus hiwΔN mutants. A two-way ANOVA with Tukey test for multiple comparisons was performed. ****p < 0.0001; ***p < 0.001; **p < 0.01; ns = not significant.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Top row shows puc-lacZ expression (red) together with a marker for nuclei (Draq5, gray). Control (lexA)-RNAi or wnd-RNAi UAS lines are driven by the BG380Gal4 driver in the background of control versus hiwΔN. Bottom row shows example NMJs in these genotypes. Scale bars = 20 µm. (B) Quantification of puc-lacZ expression in A. A one-way ANOVA with Tukey test for multiple comparisons was performed. ****p < 0.0001; ns = not significant.

## Discussion

### Axonal branches and spared synaptic connections influence the ability of injured axons to regenerate

Since the foundational observations of Ramon y Cajal, we have known that the ability of axons to regrow following damage varies strongly according to the location of damage (Ramón y Cajal, 1928). Most widely considered are differences in extrinsic factors that influence the ability of axons to grow following PNS injuries, and the impediments to axonal regeneration in the CNS that inhibit repair following spinal cord injuries (Huebner and Strittmatter, 2009). A less well-studied but important intrinsic determinant of regeneration ability is the location of the injury with respect to axonal branches. For C. elegans PLM mechanosensory neurons, robust regeneration occurs following injuries that remove both the synaptic and sensory branches, but not following injuries that leave a synaptic branch intact (Wu et al., 2007). In the mammalian spinal cord, an elegant study following responses to laser-induced microsurgery to ascending and descending central projections of sensory neurons observed that remarkable regeneration occurred following injuries proximal to the branching point (which led to removal of all branches) but not distal (which left one branch intact) (Lorenzana et al., 2015). Studies in mice have also implicated synaptic proteins alpha2-delta, Munc13, and RIM in restraining regenerative ability of axons (Hilton et al., 2022; Tedeschi et al., 2016). These observations are consistent with the possibility that spared afferent synaptic connections that remain following injuries distal to the branch point inhibit the regeneration ability of centrally projecting axons in the spinal cord.

It is noteworthy that many of the axons that project over great distances in the spinal cord have at least one synaptic branch. Neurons that project through the corticospinal tract (CST), whose poor regeneration ability following spinal cord injury is most widely studied, form synaptic branches in the red nucleus, brainstem, and throughout the spinal cord (Raineteau and Schwab, 2001). A recent study has profiled the responses of CST neurons at different injury locations (Wang et al., 2024). Strikingly, regeneration-associated genes (RAGs) and phosphorylated cJun, a marker of DLK signaling activation, are not induced in CST neurons following spinal cord injury but are robustly induced following intracortical injuries close to CST cell bodies (Mason et al., 2003; Wang et al., 2024). Since the latter may be the only form of injury that removes all synaptic branches from the CST neurons, we propose that restraint of DLK signaling activation by spared synaptic branches could be a prominent feature of the poor intrinsic regeneration capacity of neurons following spinal cord injury.

### Restraint of Wnd/DLK signaling at synaptic terminals

Using genetic manipulations that inhibit or perturb synaptic transmission and/or neuronal excitability, we did not detect a requirement for synaptic transmission in the restraint of Wnd by spared synaptic branches. The PHR ubiquitin ligase, known as Hiw in Drosophila, was a logical candidate to regulate Wnd at synapses, since studies in multiple model organisms have shown that loss of this enzyme leads to increased levels of Wnd/DLK in axons (Collins et al., 2006; Huntwork-Rodriguez et al., 2013; Nakata et al., 2005). The puc-lacZ reporter implies that Wnd signaling is elevated in hiw mutants. However, the restraint conferred by spared synaptic branches is still active in the absence of Hiw, since Wnd signaling can be further elevated by axotomy of all synapses in hiw null mutants (Figure 3). In a previous study, we noted that the nerve crush injury led to a rapid down-regulation of an ectopically expressed Hiw-GFP transgene and speculated that impairment of restraint by Hiw leads to activation of Wnd signaling in injured axons (Xiong et al., 2010). Our current data do not rule out a role for Hiw but suggest the existence of additional mechanisms that restrain Wnd signaling at intact synapses. This has also been suggested from developmental studies of photoreceptor growth cone termination, in which Hiw-independent downregulation of Wnd protein occurs concomitantly with the development of presynaptic boutons (Feoktistov and Herman, 2016).

We speculate that the regulation of Wnd is linked to the trafficking of organelles between the synaptic terminal and cell body, akin to neurotrophin signaling, which relies on retrograde trafficking of signaling endosomes in axons (Cosker et al., 2008). Consistent with this idea, DLK signaling becomes activated following nerve growth factor withdrawal from distal axons (Ghosh et al., 2011; Larhammar et al., 2017). Previous studies of Wnd signaling have documented its dependence on retrograde axonal transport machinery (Xiong et al., 2010). Moreover, mutations that disrupt axonal cytoskeleton and the unc-104/kif1A kinesin also lead to Wnd/DLK signaling activation (Li et al., 2017; Valakh et al., 2015; Valakh et al., 2013). Both Wnd and its homologue DLK in mice show regulated association with organelle membranes via palmitoylation, and disruption of its palmitoylation abolishes DLK’s signaling ability (Holland et al., 2016; Kim et al., 2024; Niu et al., 2022). Palmitoylation and depalmitoylation are dynamically regulated in axons (Ramzan et al., 2023; Zhang et al., 2024), hence comprise an attractive mechanism for mediating restraint of DLK at synaptic branches. Future delineation of the organelle(s) that Wnd/DLK associates with may provide important clues to its mechanism of regulation.

Our observations that Wnd signaling could be restrained by an intact axonal bifurcation suggest that at least one level of regulation could occur in the cell body. Consistent with this idea, a recent study has shown that Wnd signaling can be ectopically activated in the cell body when its transport to distal synapses is impaired in rab11 mutants (Kim et al., 2024). Given the many factors that have been documented thus far that regulate DLK/Wnd protein or signaling (Asghari Adib et al., 2018), we think that this kinase must be tightly regulated both at synapses and cell bodies (Figure 4). Regulation at both locations gives the neuron a way to monitor the state of its entire axon and restrict signaling activation to scenarios where all efferent connections of the axon are disrupted.

![Figure 4.](https://cdn.elifesciences.org/articles/104896/elife-104896-fig4-v1.jpg)

**Figure 4.:** In green, Wnd signaling may be regulated in the cell body downstream of a retrogradely transported signal (e.g., neurotrophin signaling). In blue, Wnd signaling activation is restrained locally at synaptic terminals, perhaps by regulating the levels or activation of Wnd itself. Activated Wnd or a downstream signaling factor is then retrogradely transported to the cell body. Previous observations that inhibition of retrograde transport blocks the induction of Wnd signaling following axonal injury favor the latter (blue) possibility. However, the restraint conferred by a physically separate bifurcation suggests that an inhibitor of Wnd signaling activation can be retrogradely transported (green). We speculate that both mechanisms act as dual checkpoints to restrain Wnd signaling activation in the context of healthy circuits.

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
      <td>Gene (Drosophila melanogaster)</td>
      <td>wnd (wallenda)</td>
      <td>Flybase</td>
      <td>FBgn0036896</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>puc (puckered)</td>
      <td>Flybase</td>
      <td>FBgn0243512</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>hiw (highwire)</td>
      <td>Flybase</td>
      <td>FBgn0030600</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>UAS-mCD8-GFP</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_5137</td>
      <td>Lee and Luo, 1999</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>m12-gal4 (P(Gal4)5053A)</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_2702</td>
      <td>Ritzenthaler et al., 2000</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>BG380-Gal4</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_42736</td>
      <td>Budnik et al., 1996; Sanyal, 2009</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>puc-lacZ[E69]</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_98329</td>
      <td>Martin-Blanco et al., 1998</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>puc-GFP</td>
      <td>Melissa Rolls</td>
      <td></td>
      <td>Rao and Rolls, 2017</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>hiwΔN</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_51637</td>
      <td>Wu et al., 2005</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>UAS-Bitbow2</td>
      <td>Dawen Cai</td>
      <td></td>
      <td>Li et al., 2021</td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>Tdc2-Gal4</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_9313</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>UAS-wnd-RNAi</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_35369</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td>UAS-lexA -RNAi</td>
      <td>Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDSC_67947</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent(Drosophila melanogaster)</td>
      <td colspan="3">Additional Drosophila lines are summarized in Supplementary file 1</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-lacZ</td>
      <td>DSHB Cat# 40-1a</td>
      <td>RRID:AB_528100</td>
      <td>1:100 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-DsRed</td>
      <td>Takara Bio Cat# 632496</td>
      <td>RRID:AB_10013483</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>A488 rabbit polyclonal anti-GFP</td>
      <td>Molecular Probes Cat# A-21311</td>
      <td>RRID:AB_221477</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>AlexFluor 568 goat polyclonal anti-mouse</td>
      <td>Thermo Fisher, A11004</td>
      <td>RRID:AB_2534072</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>AlexFluor 488 goat polyclonal anti-mouse</td>
      <td>Thermo Fisher A32723</td>
      <td>RRID:AB_2633275</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>AlexFluor 568 goat polyclonal anti-rabbit</td>
      <td>Thermo Fisher A-11011</td>
      <td>RRID:AB_143157</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Paraformaldehyde Aqueous Solution EM Grade</td>
      <td>Electron Microscopy Sciences</td>
      <td>Cat #15710</td>
      <td>16% aqueous solution diluted to 4% in PBS. Used within 1 week of dilution.</td>
    </tr>
    <tr>
      <td>Biological sample (goat)</td>
      <td>Normal goat serum (NGS)</td>
      <td>Fisher Scientific</td>
      <td>Cat #16210064</td>
      <td>Diluted to 5% in PBS</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Prolong Diamond Antifade media</td>
      <td>Thermo Fisher Scientific, P36970</td>
      <td>Cat #P36970</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PDMS microfluidic chip for immobilizing larvae</td>
      <td>MicroKosmos</td>
      <td>‘Mechanical Immobilization Chip' for Drosophila larvae</td>
      <td>(specialized equipment) Larva chip is available for purchase from https://www.ukosmos.com</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Dumont #5 fine forceps</td>
      <td>Roboz Surgical</td>
      <td>Cat #RS4978</td>
      <td>(specialized equipment) Forceps for carrying out the peripheral nerve crush assay</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Volocity software 6.2</td>
      <td>Improvision, PerkinElmer</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Drosophila stocks/genetics

All fly crosses were raised at 25°C in a 12-hr light/dark cycle on standard sucrose and yeast food. Both male and female larvae were used unless otherwise stated. Strains used are listed above in the Key Resources Table. Additional stocks are listed in Supplementary file 1.

### Immunohistochemistry

Wandering second and third instar larvae were dissected in ice-cold 1x PBS, fixed in 4% paraformaldehyde (16% diluted in 1X PBS, Electron microscopy Labs) for 20 min at room temperature and washed thrice in 1X PBS. Tissues were blocked for a minimum of 30 min in 5% normal goat serum (NGS) in 0.25% Triton X-100 in 1X PBS (PBST). Primary antibodies were incubated overnight in 5% NGS in 0.25% PBST at room temperature unless otherwise stated. Tissues were washed thrice in 1x PBS and mounted onto superfrost plus slides (Fisher Scientific) and coverslipped with ProLong Diamond Antifade media (Thermo Fisher Scientific, P36970). Antibodies and concentrations are listed in the Key Resources Table. All experimental and control larval groups were processed (dissected, fixed, stained, and images captured) together using identical confocal settings.

### Nerve crush assays

Peripheral nerve crushes in wandering second instar larvae were performed as previously described (Waller et al., 2025; Xiong et al., 2010). Briefly, with the ventral side facing upwards, anesthetized larvae (taken from 1X PBS and placed on CO2 pad for ~3–5 min) had a small region of the cuticle (around abdominal segment 2) with underlying segmental nerves gently pinched with a pair of Dumont #5 fine forceps (Roboz Surgical RS4978). After injury, larvae were placed in small dishes containing standard fly food and kept at 25°C (12 hr light/dark) for 24 hr. Injuries were confirmed by the presence of posterior tail paralysis. For the new spared nerve crush assay, we performed injuries on wandering 2nd instar larvae with labeled type II octopaminergic neurons driven by Tdc2-gal4. The Tdc2-gal4 drives expression in three ventrally located midline neurons that send one axon to the left side and one axon to the right side of larvae. Similarly to complete nerve crushes, anesthetized larvae (ventral side up) were gently pinched with fine forceps on the left side (around abdominal segment 2), injuring nerves on one side while sparing nerves on the other side. Animals were placed in small dishes containing standard fly food and kept at 25°C (12 hr light/dark) for 24–72 hr.

### Axon/synaptic branch laser injury

As previously described (Ghannad-Rezaie et al., 2012; Mishra et al., 2014; Smithson et al., 2024; Waller et al., 2025), single wandering second instar larva were taken from a dish containing 1X PBS and gently placed onto a kim wipe to remove excess PBS and then dipped into halocarbon oil 700 (H8898, Sigma). Each larva was then placed onto a glass coverslip dorsal side up (for inverted confocal) with an anterior to posterior (left to right) orientation. A PDMS microfluidic chip (https://www.ukosmos.com/) was placed on top of the larvae applying light force. A tight seal was created by applying gentle suction from a 30-ml syringe plunger. This vacuum suction immobilizes the intact larvae. The coverslip containing the microfluidic chip and larvae was mounted onto an Improvision spinning disk confocal system (PerkinElmer) connected to a Micropoint Laser Illumination and Ablation System (Andor Technology). The method for laser-induced microsurgery is described in Smithson et al., 2025. Prior to injury, the laser strength and region of interest were calibrated and optimized. Individual axonal branches (membrane GFP labeled) were identified and laser ablated. Confirmation of injury was demonstrated by a small absence of membrane GFP and degeneration of the proximal axon was detected as early as 8 hr after laser injury.

### Imaging, quantification, and analysis

Both experimental and control larvae were imaged on an Improvision spinning disk confocal system (PerkinElmer) and quantified using identical confocal settings by an independent experimenter blinded to the genotype/experiment. Injured m12-gal4 and Tdc2-gal4 axons were traced back to identify corresponding cell bodies in the lateral and medial VNC. Only the neurons whose identity and injury location could be clearly identified were used for analysis. To quantify puc-lacZ levels, the mean intensity of lacZ immunolabeling was measured in specific injury-confirmed neurons. Puc-lacZ contains an NLS sequence fused to lacZ, resulting in nuclear expression of puc. The mean lacZ intensity was measured per neuron and normalized to uninjured control neurons. All imaging, image contrast/color adjustments, and quantification were conducted using Volocity software 6.2 (Improvision, PerkinElmer). GraphPad Prism software was used for both selection and calculation of appropriate statistical tests. The methods used and n for each figure are reported in individual figure legends. p values are reported for 95% confidence intervals, and graphs are plotted with mean ± SD (standard deviation).
