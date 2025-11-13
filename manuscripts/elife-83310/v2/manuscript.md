# Synchronization of oscillatory growth prepares fungal hyphae for fusion

## Authors

- Valentin Wernet<sup>1</sup> ([ORCID: 0000-0002-3747-6171](https://orcid.org/0000-0002-3747-6171))
- Marius Kriegler<sup>1</sup> ([ORCID: 0009-0004-4395-4784](https://orcid.org/0009-0004-4395-4784))
- Vojtech Kumpost<sup>2</sup>
- Ralf Mikut<sup>2</sup>
- Lennart Hilbert<sup>3</sup> ([ORCID: 0000-0003-4478-5607](https://orcid.org/0000-0003-4478-5607))
- Reinhard Fischer<sup>1</sup> ([ORCID: 0000-0002-6704-2569](https://orcid.org/0000-0002-6704-2569)) †

### Affiliations

1. Karlsruhe Institute of Technology - South Campus Institute for Applied Biosciences Dept. of Microbiology Karlsruhe Germany ([ROR:04t3en479](https://ror.org/04t3en479))
2. Karlsruhe Institute of Technology – North Campus Institute for Automation and Applied Informatics Eggenstein-Leopoldshafen Germany ([ROR:04t3en479](https://ror.org/04t3en479))
3. Karlsruhe Institute of Technology – North Campus Institute of Biological and Chemical Systems – Biological Information Processing Eggenstein-Leopoldshafen Germany ([ROR:04t3en479](https://ror.org/04t3en479))
4. Karlsruhe Institute of Technology – South Campus Zoological Institute Dept. of Systems Biology / Bioinformatics Eggenstein-Leopoldshafen Germany ([ROR:04t3en479](https://ror.org/04t3en479))

† Corresponding author

## Abstract

Communication is crucial for organismic interactions, from bacteria, to fungi, to humans. Humans may use the visual sense to monitor the environment before starting acoustic interactions. In comparison, fungi, lacking a visual system, rely on a cell-to-cell dialogue based on secreted signaling molecules to coordinate cell fusion and establish hyphal networks. Within this dialogue, hyphae alternate between sending and receiving signals. This pattern can be visualized via the putative signaling protein Soft (SofT), and the mitogen-activated protein kinase MAK-2 (MakB) which are recruited in an alternating oscillatory manner to the respective cytoplasmic membrane or nuclei of interacting hyphae. Here, we show that signal oscillations already occur in single hyphae of Arthrobotrys flagrans in the absence of potential fusion partners (cell monologue). They were in the same phase as growth oscillations. In contrast to the anti-phasic oscillations observed during the cell dialogue, SofT and MakB displayed synchronized oscillations in phase during the monologue. Once two fusion partners came into each other’s vicinity, their oscillation frequencies slowed down (entrainment phase) and transit into anti-phasic synchronization of the two cells’ oscillations with frequencies of 104±28 s and 117±19 s, respectively. Single-cell oscillations, transient entrainment, and anti-phasic oscillations were reproduced by a mathematical model where nearby hyphae can absorb and secrete a limited molecular signaling component into a shared extracellular space. We show that intracellular Ca2+ concentrations oscillate in two approaching hyphae, and depletion of Ca2+ from the medium affected vesicle-driven extension of the hyphal tip, abolished the cell monologue and the anti-phasic synchronization of two hyphae. Our results suggest that single hyphae engage in a ‘monologue’ that may be used for exploration of the environment and can dynamically shift their extracellular signaling systems into a ‘dialogue’ to initiate hyphal fusion.

## Introduction

Oscillations are common phenomena in biology with periods from seconds to hours, to days, to years (Damineli et al., 2022; in ’t Zandt et al., 2021; Dunlap and Loros, 2017). In fungi, oscillations are a well-described feature of hyphal tip extension, where calcium ions control vesicle accumulation, actin depolymerization, and vesicle fusion with the tip membrane (Takeshita et al., 2017). In addition, signal oscillations have been described at the hyphal tips during the fusion of hyphal cells of Neurospora crassa, Fusarium oxysporum, Botrytis cinerea, and Arthrobotrys flagrans (Fischer et al., 2018; Fleißner and Herzog, 2016; Fleissner et al., 2009; Youssar et al., 2019; Palos-Fernández et al., 2022; Roca et al., 2012). These signal oscillations were named cell-to-cell dialogue and are probably based on a conserved diffusible signaling molecule, which remains to be discovered (Goryachev et al., 2012; Haj Hammadeh et al., 2022; Daskalov et al., 2017). The nematode-trapping fungus A. flagrans can switch from a saprotrophic to a predatory lifestyle, and sophisticated signaling regimes between the fungus and its prey, Caenorhabditis elegans, control trap formation, attraction of the prey, and attack of the nematode (Hsueh et al., 2017; Yu et al., 2021; Wernet et al., 2021; Fischer and Requena, 2022a). Once captured A. flagrans penetrates the cuticle of the nematode and colonizes the worm body. There is first evidence that small-secreted proteins play important roles in the fungal attack (Youssar et al., 2019; Wernet et al., 2021; Fischer and Requena, 2022b). Nematode-trapping fungi have also the potential to be applied as biocontrol agents against animal and plant-pathogenic nematodes (Wernet and Fischer, 2023; Rodrigues et al., 2022).

Two of the hallmark proteins during the cell-to-celll dialogue of fungal hyphae are the soft protein, SofT, and the mitogen-activated protein (MAP) kinase MakB which show anti-phasic, oscillatory recruitment to the plasma membrane and the nuclei of interacting cells, respectively (Fleissner et al., 2009; Haj Hammadeh et al., 2022). Although its molecular function remains elusive, SofT is thought to be involved in generating a signal during the cell-to-cell dialogue. It is essential for cell fusion in filamentous fungi and acts as a scaffold protein of the cell wall integrity pathway (Fischer and Glass, 2019; Teichert et al., 2014; Fleissner et al., 2005; Serrano et al., 2022). Besides the nature of the signaling compound, another important open question is the onset and coordination of the communication process. If people want to communicate, they may use their vision to approach each other, before the start of an acoustic conversation. However, if now the scene changes to a dark room where visual information is not available, the initiation and coordination of the conversation appears to be difficult. As the cell-to-cell dialogue in fungal hyphae appears to be based on a single, chemical communication channel, it is proposed that the two involved cells undergo oscillatory secretion of a signaling compound with a refractory period that prevents self-stimulation and can contribute to overcoming critical threshold concentrations (Damineli et al., 2022). Here, we investigated the onset and coordination of that cell-to-cell dialogue and found that single hyphae show the same signaling events at the hyphal tip as during the cell-to-cell dialogue. Once hyphae meet, the ‘monologue’ of each hypha transits into a dialogue.

## Results

An open question is if and how cell-to-cell communication is activated once a hyphal fusion partner appears in the vicinity. To address this question, we monitored SofT-GFP in A. flagrans growing on low-nutrient agar (LNA) and observed oscillatory recruitment of SofT to single hyphal tips with a mean period of 137±17 (SD) seconds (n=164 in 18 hyphae) without other hyphae in their vicinity (Figure 1a, d, and e, Video 1). We measured SofT-GFP signals at hyphal tips and found that 85 ± 4% (mean ± SD) showed fluorescence without a fusion partner (n=50) hyphal tips, experiment repeated three times, (Figure 1—figure supplement 1a). Hyphae without SofT-GFP recruitment at their tips were unable to fuse, suggesting that they could not recognize each other (Figure 1—figure supplement 1b, Video 2). However, these cells were still able to undergo cell fusion if other hyphae induced hyphal fusion (Figure 1—figure supplement 1b). Recruitment of SofT-GFP to the hyphal tip and cell fusion were also observed on potato dextrose agar (PDA), suggesting that nutrient availability would not be the sole cause of inducing the observed dynamics (Figure 1—figure supplement 1c). The observed SofT-GFP dynamics resembled oscillating tip growth described in Aspergillus nidulans and raised the question whether and how these two processes might be connected in A. flagrans (Takeshita et al., 2017). Therefore, we monitored the mCherry-tagged orthologue of A. nidulans chitin synthase B (DFL_009443) in A. flagrans, which acts as a cargo marker for intracellular transport and is crucial for polarized growth (Zhou et al., 2018; Hernández-González et al., 2018). The fluorescent fusion protein oscillated at growing hyphal tips with a mean period of 125±37 (SD) seconds (n=50 in 7 hyphae) (Figure 1b, d, and e, Video 3). To compare the oscillations of SofT and ChsB, we created a strain with both proteins labeled. SofT-GFP localized at the same time at growing tips as mCherry-ChsB (Figure 1e, Video 4). However, mCherry-ChsB showed a wider frequency distribution and shorter periods. Thus, the localization of mCherry-ChsB appears to be independent of SofT (Figure 1f). Indeed, localization and oscillation of mCherry-ChsB at the tip were not affected by deletion of sofT (Figure 1f). Deletion of chsB in A. nidulans is detrimental for hyphal growth and was therefore not analyzed in A. flagrans (Borgia et al., 1996; Fukuda et al., 2009). To further analyze its molecular role, we generated three truncated versions of the A. flagrans SofT protein and performed rescue experiments of the ∆sofT mutant (Figure 1—figure supplement 2, Youssar et al., 2019). SofT consists of 1213 amino acids with a predicted N-terminal disordered region (AA1–540), a WW domain (AA505–533), and a putative C-terminal phosphatase domain (AA676–1213) (Figure 1—figure supplement 2a). A fragment containing the N-terminal region and the WW domain was sufficient to restore aerial mycelia formation and hyphal fusion, while the N-terminal disordered region or the C-terminus was not, emphasizing the significance of SofT-interacting proteins in cell communications (Figure 1—figure supplement 2b, c). Our results show that most A. flagrans hyphae are constantly sending signals in a form of constant ‘self-talk’, or monologue, possibly to explore the environment for a fusion partner.

![Figure 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig1-v2.jpg)

**Figure 1.:** (a, b) Time course of SofT-GFP and mCherry-ChsB localization at hyphal tips. Arrows indicate the accumulation of the proteins at the hyphal tips. Dotted circles indicate an area of 6×6 pixels which was used to measure the fluorescent intensity over time depicted in (c) of GFP-SofT at the lower edge of the plasma membrane or of mCherry-ChsB at the apex. (b) is a maximum-intensity projection of the time-lapse sequence. A kymograph was created for each time course by drawing a line (pixel width 5) along the growth axis of the respective hypha. The numbers represent the count of oscillating accumulations of each fusion protein during the growth of each hypha in the corresponding time course. (c) Relative fluorescent intensity (RFI, y-axis, arbitrary units) at the hyphal tips of a–b was measured over the time course (x-axis in minutes). (d) The interval between two peaks at hyphal tips was counted and depicted as relative frequency (y-axis) over the time (in seconds). GFP-SofT n=164 in 8 hyphae. mCherry-ChsB n=50 in 7 hyphae. (e) Localization of GFP-SofT (depicted in green) and mCherry-ChsB (depicted in magenta) during hyphal tip growth. Numbers indicate the time in minutes. (f) Localization of ChsB-mCherry at the hyphal tip of the A. flagrans ∆sofT-mutant strain. The relative fluorescent intensity at the hyphal tip (y-axis, arbitrary units) was measured over the time course.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) SofT-GFP is present in three of the four hyphae. Dashed lines outline the shape of one hypha without SofT-GFP recruitment. The arrow indicates an accumulation of SofT-GFP near the nucleus of one hypha. (b) Time course of SofT-GFP during a hyphal fusion event. The arrow indicates the hyphal tip of hypha T1. No apparent accumulation of SofT-GFP was observed during the initial phase of the time course. The star indicates accumulation of SofT-GFP in hyphae T1 and T3 at later stages of the time course. See Video 2. (c) SofT-GFP localization in a A. flagrans hypha grown on potato dextrose agar (PDA) for 24 hr.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (a) Domain structure of the A. flagrans SofT and prediction of disordered protein regions using iupred2a (https://iupred2a.elte.hu). The protein contains 1213 amino acids and harbors a WW domain (AA505–533) and a putative C-terminal phosphatase domain (AA676–1213). (b) Complementation experiment of the ∆sofT mutant with three truncated sofT fragments. The first fragment encoded for the N-terminal region of the protein (1–504 AA) without the conserved WW domain. The second fragment encoded for the N-terminal region with the conserved WW domain (1–540 AA). The third fragment encoded the C-terminal region of the protein containing the putative phosphatase domain (534–1213 AA). We individually transformed the three constructs into the ∆sofT strain and observed the growth of the mutants after genotyping on potato dextrose agar (PDA) after 6 days of incubation at 28°C. The ∆sofT deletion shows a strong growth phenotype on solid media (Youssar et al., 2019) with the absence of aerial mycelium. (c) Micrographs showing hyphal growth of the different rescued ∆sofT strains on low-nutrient agar (LNA) after 24 hr of incubation at 28°C. Stars indicate hyphal fusion events. A rescue with the full-length sofT construct was used as a control.

![Video 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-video1.mp4.jpg)

![Video 2.](https://cdn.elifesciences.org/articles/83310/elife-83310-video2.mp4.jpg)

![Video 3.](https://cdn.elifesciences.org/articles/83310/elife-83310-video3.mp4.jpg)

![Video 4.](https://cdn.elifesciences.org/articles/83310/elife-83310-video4.mp4.jpg)

To understand how the signal oscillations in a single hypha (monologue) might transit into the anti-phasic, cell-to-cell dialogue once a partner cell appears in the vicinity, we constructed a mathematical model. Specifically, we extended an existing model of cell-to-cell communication based on anti-phasic oscillations so as to explicitly account for the uptake of signaling components from the surrounding media (Goryachev et al., 2012). This model requires that not one, but two species in the cell undergo a conversion, with the second species’ conversion requiring the first species’ transition to have completed to a large extent. The reason behind this is that, without this sequential conversion, there is no delay between receiving and secreting signal, and that the secreting cell would not become non-receptive to its own signal (Goryachev et al., 2012). The concentration of signaling components in the immediate proximity of the wall of cell 1 and cell 2 is represented by two model variables, $Z_{1}$ and $Z_{2}$ , respectively (Figure 2a, Figure 2—figure supplement 1). As the signaling component is taken up into a cell, activating components (modeled as variables $A_{1}$ and $A_{2}$) become more concentrated in this cell. These activating components, in turn, stimulate the docking of cytoplasmic signaling components ($X_{1}$ and $X_{2}$) to the inside of the cell membrane ($Y_{1}$ and $Y_{2}$). The release of membrane-docked vesicles to the extracellular space is initially blocked by high levels of activator ($A_{1}$ and $A_{2}$). Secretion ultimately occurs when some of the activating components are converted into an auto-inhibitory component ($I_{1}$ and $I_{2}$), reducing levels of activating components, thereby allowing secretion of signaling components into the extracellular compartments ($Z_{1}$ and $Z_{2}$). The main novelty of our model is the addition of the variables $Z_{1}$ and $Z_{2}$ to explicitly represent the information exchange between hyphae via the shared extracellular medium. Among the abstract model variables, SofT as a signaling component located inside of a hyphal cell connects most closely to variables X1,2 and Y1,2 (Figure 2a). ChsB is also located inside the hyphal cells, but localizes differently from SofT and likely does not act as a signaling component, so that ChsB can be related to the variables A1,2, and I1,2.

![Figure 2.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig2-v2.jpg)

**Figure 2.:** (a) In the model, each hyphal cell contains an excitatory system with an activator ($A_{1,2}$) and inhibitor ($I_{1,2}$). This excitatory system is triggered by extracellular signaling molecules ($Z_{1,2}$) and, in turn, regulates the docking and subsequent release of vesicles ($X_{1,2}$ and $Y_{1,2}$), which contain the signaling protein, into the extracellular space. (b) At long distances (here, $d=10$), the cells operate as independent oscillator units. (c) At short distances (here, $d=0$), cells synchronize and oscillate in anti-phase. (d) Decreasing the distance between the two cells increases the magnitude of the anti-correlation (negative Pearson correlation coefficient) between the activator concentrations of the individual cells. (e) Upon continuous reduction of the distance between the cells, anti-synchrony emerges (noticeable at around 15 min).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** To illustrate the time course of all model variables, a simulation with a single cell was implemented by setting the cell distance to infinity ($d=∞$).

In simulations containing only a single cell, similar to the experimental results monitoring the components in a single hypha, oscillations in these different components could be observed (Figure 1—figure supplement 1). When placing two cells in the simulation at different distances ($d$) from each other, oscillations of these two cells appear uncoordinated at long distances (monologue), and anti-phasic at short distances (dialogue) (Figure 2b–d). The role of the signaling component in the dialogue at a short distance can be seen in our simulations: high extracellular concentrations ($Z_{1}$ and $Z_{2}$) are attained only briefly, when one cell has secreted the component, and the other cell has not yet taken it up again (Figure 2c). This back-and-forth exchange of signaling component via secretion into and uptake from the extracellular space represents a physically credible mechanism to establish the cell-to-cell dialogue at a short distance. When we implement a simulation that mimics the growth of two hyphae toward each other in the form of a distance that decreases over time, a transitory phase where the uncoordinated oscillations (two monologues) become mutually entrained into anti-phasic oscillations (dialogue) can be seen (Figure 2e). As seen in these simulation results, the same regulatory mechanism, based on a signaling component that is exchanged via the extracellular space, can explain the transition from single-cell oscillatory growth to anti-phasic synchronization between two approaching cells. Crucially, these simulations also imply a transitory phase, during which both cells’ dynamics slow down, just before entering into the dialogue and speeding up again (Figure 2e). This ‘critical slowing down’ is typical in phases where a system transitions from one type of dynamic behavior to another type of dynamic behavior, due to being ‘caught in between’ two types of behavior during the transition (Damineli et al., 2022; Quail et al., 2015).

To experimentally assess the transition from two ‘monologues’ to a coordinated ‘dialogue’, we monitored SofT in two approaching hyphae. Initially, the oscillations in the two hyphae appeared uncoordinated (orientation phase) but then transitioned to anti-phasic oscillations characteristic of the cell-to-cell dialogue (Figure 3a and b, Video 5). The frequency of SofT oscillations during the cell-to-cell dialogue (mean period of 104±28 [SD] seconds, n=173 in 18 hyphae) was comparable to the frequency in single hyphae and was not influenced by the presence of nematodes (Figure 3c). As expected from our simulations of a dynamic transition into coordinated oscillations, oscillations in both hyphae slowed down during the transitory phase that precedes the coordinated cell-to-cell dialogue (Figure 3b). To further validate the findings obtained with SofT, we investigated the behavior of the MAP kinase MakB, which is central for the cell dialogue and exhibits anti-phasic oscillations with SofT (Haj Hammadeh et al., 2022). We monitored the localization of MakB tagged with mCherry and observed oscillatory recruitment of MakB to the nuclei of hyphae with a mean period of 130±33 (n=45 in 8 hyphae) in the absence of neighboring hyphae and a mean period of 117±19 (n=57 in 8 hyphae) during the cell-to-cell dialogue (Figure 3c, Figure 3—figure supplement 1, Video 6). Interestingly, co-localization of SofT-GFP and MakB-mCherry in the same hyphae revealed that both proteins were oscillating in the same phase without other hyphae in their vicinity (Figure 3d and e, Video 7), which is opposite to the so far observed anti-phasic oscillations observed during the cell dialogue (Fleissner et al., 2009; Haj Hammadeh et al., 2022). Additionally, we observed that decoupling of SofT-GFP and MakB-mCherry oscillations into the anti-phasic cell dialogue occurred during the transitory phase where the growth slowed down (Figure 3f, Video 8). These results indicate that the transition from a ‘monologue’ to a ‘dialogue’ include the decoupling of SofT and MakB oscillations.

![Figure 3.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig3-v2.jpg)

**Figure 3.:** (a, b) Time course of SofT-GFP during a hyphal fusion event. Selective micrographs of the time course are shown and are divided into an orientation phase (orange frame) and a cell-to-cell dialogue phase (blue frame). An area of 3×3 pixels at each hyphal apex was used to measure the fluorescent intensity depicted in (b) (y-axis, arbitrary units). T1=left tip; T2=right tip. (c) The interval between two peaks of SofT-GFP or MakB-mCherry at each hyphal tip during the cell dialogue was counted and the distribution is depicted as relative frequency (y-axis) over the time (in seconds). SofT-GFP n=178 in 18 hyphae. MakB-mCherry n=57 in 8 hyphae. (d) Co-localization of GFP-SofT (depicted in green) and MakB-mCherry (depicted in magenta) during hyphal tip growth. Arrows indicate the accumulation of the proteins at the hyphal tips. The circles indicate an area of 15×4 (SofT) and 10×10 (MakB) pixels which were used to measure the fluorescent intensity over time depicted in (e) of GFP-SofT at the upper edge of the plasma membrane or of MakB-mCherry in the nucleus. Single channels are depicted as inverted grayscale. (e) Relative fluorescent intensity (RFI, y-axis, arbitrary units) at the hyphal tips of (d) was measured over the time course (x-axis in minutes). (f) Time course of SofT-GFP and MakB-mCherry during a hyphal fusion event. Selective micrographs of the time course are shown and are divided into a monologue phase (orange frame) and cell-to-cell dialogue phase (blue frame). T1=left tip; T2=right hypha. Arrows indicate the accumulation of the proteins in the hyphae. An area of 21×21 pixels was used to measure the fluorescent intensity of MakB-mCherry, an area of 10×6 pixels was used to measure the fluorescent intensity of SofT-GFP depicted in the lower graphs (y-axis, arbitrary units). Each graph shows the fluorescence of one hypha.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Time course of MakB-mCherry at a hyphal tip. Arrows indicate the accumulation of the protein at the nucleus. The circle indicates an area of 15×15 pixels which was used to measure the fluorescent intensity over time. The representative images are a maximum-intensity projection of the time-lapse sequence. The relative fluorescent intensity (RFI, y-axis, arbitrary units) at the region of interest was measured over the time course (x-axis in minutes) and is depicted as graph. The interval between two peaks at the region of interest was counted and depicted as relative frequency (y-axis) over the time (in seconds). n=45 in 8 hyphae. See Video 6.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (a) Time course of mCherry-ChsB during a hyphal fusion event. A maximum-intensity projection was generated from the time-lapse sequence. It was further bleach-corrected using the bleach correction plugin (correction method: simple ratio) of Fiji. The relative fluorescent intensity (RFI) of an area (y-axis, arbitrary units) of 6×6 pixel was measured at each hyphal apex over time (x-axis in minutes) to generate the graph. The boxed area depicts the selected micrographs of the time course. The interval between two peaks of ChsB at each hyphal tip during the cell-to-cell dialogue was counted and the distribution is depicted as relative frequency (y-axis) over the time (in seconds). n=105 in 11 hyphae. (b) Maximum-intensity projections of two time courses of Lifeact-GFP during hyphal fusion events. A maximum-intensity projection was generated from each time-lapse sequence. Arrows indicate the accumulation of the protein in the hyphae. Kymographs were created of the time courses by drawing a line (pixel width 5) along the growth axis of the respective hyphae. The boxed area of the kymograph is enlarged and displays the phase of the cell-to-cell dialogue. The interval between two peaks of Lifeact-GFP at each hyphal tip during the cell-to-cell dialogue was counted and the distribution is depicted as relative frequency (y-axis) over the time (in seconds). n=106 in 10 hyphae. See Video 9.

![Video 5.](https://cdn.elifesciences.org/articles/83310/elife-83310-video5.mp4.jpg)

![Video 6.](https://cdn.elifesciences.org/articles/83310/elife-83310-video6.mp4.jpg)

![Video 7.](https://cdn.elifesciences.org/articles/83310/elife-83310-video7.mp4.jpg)

![Video 8.](https://cdn.elifesciences.org/articles/83310/elife-83310-video8.mp4.jpg)

The underlying hypothesis that the same oscillation mechanism acts during the monologue- and dialogue-type dynamics is further substantiated by the observation that, similar to single hyphal growth, not only SofT and MakB but also ChsB and actin filaments visualized by Lifeact-GFP showed oscillating recruitment to the tips of interacting cells with mean periods of 103±26 (SD) seconds (n=105 in 11 hyphae) and 103±27 (n=106 in 10 hyphae), respectively (Figure 3—figure supplement 2a, b, Video 9).

![Video 9.](https://cdn.elifesciences.org/articles/83310/elife-83310-video9.mp4.jpg)

A central assumption underlying the cell-to-cell dialogue in our model is that hyphae communicate by passing back and forth a shared signaling component, $Z$. Considering the central role of Ca2+ in many types of cellular excitatory dynamics, and previous results that suggest that Ca2+ is involved in the cell-to-cell dialogue (Palma-Guerrero et al., 2013; Simonin et al., 2010; Fu et al., 2011; Fu et al., 2014), we monitored intracellular Ca2+ concentrations using the genetically encoded fluorescent reporter R-GECO. The fluorescent signals showed robust oscillations that were coordinated between two approaching hyphae (Figure 4a and b, Video 10; Zhao et al., 2011). The mean oscillation period of 104±33 (SD) seconds (n=160 in 24 hyphae) was comparable to the other markers during the cell-to-cell dialogue (Figure 3c, Figure 3—figure supplement 2a,b). Indeed, simultaneous visualization of R-GECO and GFP-ChsB showed synchronized oscillation with similar periods, indicating the anti-phasic oscillations of growth during the chemotropic interaction of the two hyphae (Figure 4d and e, Video 11). This phenomenon was coordinated in anti-phase in interacting hyphae. These results indicate that signaling and growth during the cell-to-cell dialogue are highly synchronized and possibly mediated by the uptake of Ca2+.

![Figure 4.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig4-v2.jpg)

**Figure 4.:** Maximum-intensity projection of a time course of R-GECO during a hyphal fusion event. Stars indicate the fluorescent excitation of R-GECO in the presence of Ca2+ inside the hyphae. The changes in fluorescent intensity are color-coded as Fire LUT using Fiji, depicting high pixel values as white and yellow color, and low pixel values as blue and magenta. The relative fluorescent intensity (RFI) (y-axis, arbitrary units) was measured at each hyphal tip over the time course (x-axis in minutes). The RFI of an area of 12×12 pixels was measured at each hyphal tip to generate the graph. The boxed area depicts the selected micrographs of the time course. (c) The interval between two peaks of R-GECO at each hyphal tip during the cell-to-cell dialogue was counted and the distribution is depicted as relative frequency (y-axis) over the time (in seconds). n=160 in 24 hyphae. (d) Maximum-intensity projection of a time course of GFP-ChsB and R-GECO during a hyphal fusion event. Single channels are depicted as inverted grayscale. Arrows indicate the localization of GFP-ChsB at hyphal tips. Stars indicate the fluorescent excitation of R-GECO in the presence of Ca2+ inside the hyphae. The RFI (y-axis) was measured of an area of 6×6 pixels at each hyphal apex over the time course (x-axis in minutes, y-axis, arbitrary units). The boxed area of the selected micrographs represents the enlarged area in (e). (e) A kymograph was created of the time course in (d) drawing a line (pixel width 5) along the growth axis of both hyphae. The boxed area is enlarged and displays one cycle of the cell-to-cell dialogue. (f) Compared to the control (low-nutrient agar [LNA] containing 1 µM CaCl2), mCherry-ChsB did not accumulate at the Spitzenkörper on LNA containing 5 mM EGTA. (g) Compared to the control, GFP-SofT did not accumulate at hyphal tips on LNA containing 5 mM EGTA. Scale bars in (f, g) depict 1 µm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Hyphae showed close physical contact without hyphal fusion after incubation with the Ca2+ chelating agent EGTA (5 mM). (b) No pulses of R-GECO were observed in hyphae on low-nutrient agar (LNA) containing 5 mM EGTA.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** In a simulation containing only a single cell, at a Ca2+ concentration of 0 ($C_{media}=0$), no oscillations are observed. Around a Ca2+ concentration of 1 ($C_{media}=1$), the cell generates regular oscillations (as shown in Figure 1), evidenced by an increasing standard deviation of the activator level ($StdA_{1}$). Increasing the Ca2+ concentration further leads again to the gradual loss of oscillatory behavior. The standard deviation was calculated over a simulation that represented 800 min of cellular dynamics.

![Video 10.](https://cdn.elifesciences.org/articles/83310/elife-83310-video10.mp4.jpg)

To further test the role of Ca2+, we depleted Ca2+ from the media by adding the Ca2+ chelating agent EGTA to LNA containing 1 µM CaCl2. At an EGTA concentration of 5 mM, cell-fusion events were never observed after incubation for 16 up to 72 hr (Figure 4—figure supplement 1a). In addition, hyphal growth of A. flagrans was reduced, but germination of spores was unaffected. Fluorescence of R-GECO was not detectable in these Ca2+-depleted conditions (Figure 4—figure supplement 1b). mCherry-ChsB still localized at hyphal tips, however, no obvious oscillating dynamic recruitment was observed (Figure 4f). mCherry-ChsB localized directly to the plasma membrane at the tip, without prior accumulation at the Spitzenkörper, confirming with previous reports the importance of Ca2+ for well-regulated pulsatile secretion (Kurian et al., 2022). The localization of GFP-SofT to hyphal tips was abolished after the addition of 5 mM EGTA, indicating Ca2+-dependent recruitment to the plasma membrane (Figure 4g). In line with these experimental results, reducing the external media concentration of signaling components in our simulations also abolished oscillations (Figure 4—figure supplement 2). On the other hand, external Ca2+ concentrations of up to 100 mM did not influence hyphal fusion. Taken together, these results indicate that extracellular Ca2+ is important in the signaling mechanism that underlies the monologue implicated in pulsatile cell extension as well as the synchronization of oscillations into a cell-to-cell dialogue (Figure 5). An estimate calculation indicates that particles of diameter of approximately 3 nm or less can traverse the distance at which two hyphae synchronize at a sufficiently short time to support synchronization (for details, see Materials and methods). This diameter would include Ca2+ ions as well as Ca2+-binding proteins, but not secretory vesicles as the component that is exchanged between the hyphae.

![Video 11.](https://cdn.elifesciences.org/articles/83310/elife-83310-video11.mp4.jpg)

![Figure 5.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig5-v2.jpg)

**Figure 5.:** (a) Cell fusion of two hyphal cells is mediated by the synchronization of oscillatory growth. Vesicles needed for hyphal growth and communication accumulate at the hyphal tip and are released to the surroundings upon an influx of Ca2+. If two cells are in close proximity, the uncoordinated, stepwise growth shifts after transitory entrainment to a synchronized anti-phasic cell dialogue and subsequent cell fusion. (b) During stepwise cell extension, a Ca2+-dependent signaling component is released with a refractory period to prevent self-stimulation. Entrainment of two cells in close proximity initiates a cell dialogue mediated by a so far unknown Ca2+-dependent signaling component. Refractory periods after secretion prevent self-stimulation.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Arrows indicate accumulations of Soft-GFP inside hyphae. (Top) Dashed lines outline the hypha grown on low-nutrient agar (LNA) for 16 hr at 37°C. (Bottom) Hyphae were grown on Aspergillus minimal medium for 16 hr at 37°C.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (a) The A. flagrans ∆figA gene deletion mutant can perform vegetative hyphal fusion and trap C. elegans. (b) The A. flagrans ∆figB gene deletion mutant can perform vegetative hyphal fusion and trap C. elegans. The growth of both mutants on potato dextrose agar (PDA) is shown after 7 days at 28°C.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/83310/elife-83310-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (a) Growth of the A. flagrans ∆hamA gene deletion mutant grown on potato dextrose agar (PDA) after 7 days at 28°C. (b) Deletion of hamA leads to loss of vegetative hyphal fusion. (c) Kymograph of a time course depicts the recruitment of mCherry-ChsB the hyphal tip of a ∆hamA hypha. (d) Localization of mCherry-RimA at the hyphal tip. A maximum-intensity projection was generated from the time-lapse sequence. It was further bleach-corrected using the bleach correction plugin (correction method: simple ratio) of Fiji. A kymograph was created by drawing a line (pixel width 5) along the growth axis of the hypha. See Video 12.

During our study we identified and localized the SofT orthologue in A. nidulans. While we observed punctate localization throughout the hyphae resembling that seen in A. flagrans, we did not observe any tip oscillations in A. nidulans during various cultivation conditions (Figure 5—figure supplement 1). Furthermore, we did not observe any hyphal fusion events. It is worth noting that Aspergillus species are known to rarely undergo vegetative cell fusion under laboratory conditions, compared to other fungi (Macdonald et al., 2019). This raises interesting questions for future research, such as investigating the presence of similar signaling dynamics during hyphal growth and sexual development in other fungi and investigating the factors that induce or regulate these dynamics in species like A. nidulans.

In order to further investigate the role of extracellular Ca2+ during fungal communication, we concentrated on proteins which potentially play a role in incorporating the Ca2+ signal into hyphal growth and the cell dialogue. Initially, we focused on orthologues of the protein FIG1 (mating factor induced gene 1) which is part of the low-affinity calcium uptake system in Saccharomyces cerevisiae and is essential for mating (Muller et al., 2003). We identified the orthologues FigA and FigB in the genome of A. flagrans. figA single gene deletion resulted in a colony phenotype, however, both gene deletion mutants still performed cell fusions and trapped nematodes (Figure 5—figure supplement 2). We were unable to generate a double-deletion strain, suggesting at least one protein to be essential for growth.

## Discussion

Fungal hyphae communicate with each other before they fuse and alternate between signal sender and signal perceiver functions, or between talking and listening if compared to people. Interestingly, the same signal oscillations occur in hyphae without any other hyphae in the vicinity. We named this phenomenon ‘monologue’ and show that - upon appearance of a fusion partner - the monologue transits into a dialogue. In comparison to people’s conversations this means that people in a dark room walk around and whisper constantly until they meet a conversation partner. Now the two monologues need a transition phase that talking alternates with listening. For two hyphae trying to start a dialogue, the model predicted such a transitory phase, which we were able to monitor experimentally. At the molecular level the phenomenon may be explained by an interference of the signaling molecules of two approaching hyphae. The threshold concentrations for the switch between sending and receiving could be reached too early to be processed by the downstream components and hence the machinery would be disturbed until both hyphae respond to the common signal concentrations between the hyphal tips.

The growing tip of filamentous fungi is an example of apical-growing cells and therefore our results may have an impact on the understanding of other highly polarized cells such as plant pollen tubes or root hairs, or axons and dendrites (Damineli et al., 2022). Interestingly, the Soft protein exhibits weak homology to mammalian proteins of the aczonin/piccolo family, which are involved in synaptic vesicle release regulated by Ca2+ (Goryachev et al., 2012). We screened for PRO40 (Soft)-interacting proteins with calcium-dependent functions in the fungus Sordaria macrospora identifying HAM-10, an orthologue of Unc13/Munc13 in higher eukaryotes (Teichert et al., 2014). HamA, the A. flagrans orthologue, contains a calcium-dependent C2 domain similar to other fungal orthologues. Deletion of ∆hamA resulted in a cell fusion mutant phenotype, as observed in the ∆ham-10 mutant in N. crassa (Fu et al., 2011; Figure 5—figure supplement 3). Interestingly, in the ∆ham-10 mutant, neither Soft nor MAK-2 localized at the tip of germ tubes (Fu et al., 2014). We localized mCherry-ChsB in the ∆hamA mutant and observed oscillating recruitment of the protein to the hyphal tip (Figure 5—figure supplement 3), indicating that HamA could play a role at the interface of combining cell dialogue signaling and growth dynamics. RIM1 is another Munc13-interacting protein, which plays a role in linking vesicle fusion and calcium influx. In S. macrospora, the orthologue of RIM1 was identified as PRO40-interacting protein (Teichert et al., 2014). In N. crassa the orthologous Syt1 is involved in cell fusion, but not essential (Palma-Guerrero et al., 2013). The orthologue RimA in A. flagrans localized at the hyphal tip without noticeable oscillations during our time series (Figure 5—figure supplement 3, Video 12). Calmodulin and a calcium/calmodulin-dependent protein kinase were identified as PRO40 interaction partners (Teichert et al., 2014), indicating intriguing similarities between the rapid secretion of the cell-to-cell dialogue in fungi and synaptic vesicle release in neurons. In the future, it will be interesting to study how other fusion-related proteins might be involved in the translation of the increase in intracellular Ca2+ concentrations and how this change relates to the secretion of a yet to be identified chemoattractive signal molecule.

![Video 12.](https://cdn.elifesciences.org/articles/83310/elife-83310-video12.mp4.jpg)

## Materials and methods

### Strains and culture conditions

A. flagrans strains (all derived from CBS349.94) were cultivated at 28°C on PDA (2.4% potato dextrose broth and 1.5% agar, Carl Roth). All fungal strains used in the study are listed in Table 1. Protoplast transformation was performed as described in Youssar et al., 2019. Chemically competent Escherichia coli Top10 cells were used for plasmid cloning. A. nidulans strains were cultivated at 37°C on Aspergillus minimal media and transformed as described in Szewczyk et al., 2006.

**Table 1.**
 A. flagrans and A. nidulans strains used in this study.


<table>
  <thead>
    <tr>
      <th>Strain number</th>
      <th>Genotype</th>
      <th>Origin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CBS 349.94</td>
      <td>Wild type</td>
      <td>Youssar et al., 2019</td>
    </tr>
    <tr>
      <td>sVW16</td>
      <td>tubA(p)::lifeact::GFP::gluC(t); trpC(p)::hph::trpC(t)</td>
      <td>Wernet et al., 2022</td>
    </tr>
    <tr>
      <td>sVW01</td>
      <td>sofT::hph (∆soft)</td>
      <td>Youssar et al., 2019</td>
    </tr>
    <tr>
      <td>sVW20</td>
      <td>∆sofT; sofT(p)::sofT::gluC(t); neo; makB(p)::makB::makB(t); ntc</td>
      <td>Haj Hammadeh et al., 2022</td>
    </tr>
    <tr>
      <td>sVW25</td>
      <td>tubA(p)::lifeact::GFP::gluC(t); trpC(p)::hph::trpC(t)</td>
      <td>Wernet et al., 2022</td>
    </tr>
    <tr>
      <td>sVW29</td>
      <td>sofT(p)::sofT::GFP::sofT(t); trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW40</td>
      <td>soft(p)::sofT (∆1–504 AA N-terminus) gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW41</td>
      <td>soft(p)::sofT (∆534–1213 AA C-terminus) gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW43</td>
      <td>soft(p)::sofT (∆1–540 AA N-terminus, no WW domain) gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW51</td>
      <td>tubA(p)::mCherry::chsB::chsB(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW52</td>
      <td>sofT(p)::GFP::sofT; tubA(p)::mCherry::chsB::chsB(t);trpC(p)::hph::trpC(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW65</td>
      <td>h2b(p)::r-GECO::gluC(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW69</td>
      <td>h2b(p)::r-GECO::gluC(t);tubA(p)::GFP::chsB::chsB(t); gpdA(p)::neo::trpC(t); trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW75</td>
      <td>sofT::hph (∆soft); tubA(p)::mCherry::chsB::chsB(t); gpdA(p)::neo::trpC(t); trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW76</td>
      <td>figA::hph (∆figA)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW77</td>
      <td>figB::hph (∆figB)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW78</td>
      <td>tubA(p)::mCherry::rimA::chsB(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW44</td>
      <td>hamA::hph (∆hamA), trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>sVW80</td>
      <td>sVW51,hamA::hph (∆hamA), trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RPA 33</td>
      <td>yA1, riboB2, pyrG89, pyroA4, pabaA1, nkuA::argB+</td>
      <td></td>
    </tr>
    <tr>
      <td>VW-a01</td>
      <td>yA1, riboB2, pyrG89, (AnSoft-GFP::Afpyro) pyroA4, pabaA1, nkuA::argB+</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

### Plasmid and strain construction

All plasmids and primers used in the study are listed in Tables 2 and 3. Chemically competent E. coli Top10 cells were used for plasmid cloning. A. flagrans SofT was tagged with GFP at the C-terminus and expressed under the native promoter at the sofT locus. A 1 kb region from the 3’-end of the sofT open reading frame (orf) and 0.6 kb of the terminator region were amplified by PCR from A. flagrans genomic DNA. A GFP::hph cassette was amplified from pNH57 and all three fragments were subsequently inserted into the linearized plasmid backbone pJET1.2 using Gibson assembly, resulting in plasmid pVW106. A. flagrans ChsB was tagged with either mCherry or GFP at the N-terminus and expressed under the alpha-tubulin tubA promoter. The chsB orf and the 0.9 kb 3’ region were amplified by PCR from A. flagrans gDNA and inserted into the plasmid backbone pVW92 using Gibson assembly, resulting in the tubA-mCherry-chsB plasmid pVW118. For a GFP-tagged ChsB variant, the mCherry cassette of pVW118 was replaced by GFP using Gibson assembly, resulting in pVW132.

**Table 2.**
 Plasmids used in this study.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description/genotype</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pVW57</td>
      <td>Plasmid backbone containing trpC(p)::hph::trpC(t)</td>
      <td>Wernet et al., 2022</td>
    </tr>
    <tr>
      <td>pVW92</td>
      <td>Plasmid backbone containing gpdA(p)::neo::trpC(t) and tubA(p)</td>
      <td>Wernet et al., 2021</td>
    </tr>
    <tr>
      <td>pNH57</td>
      <td>Plasmid containing GFP::hph</td>
      <td>Nicole Wernet (Karlsruhe)</td>
    </tr>
    <tr>
      <td>pVW106</td>
      <td>sofT(p)::sofT::GFP::sofT(t); trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW118</td>
      <td>tubA(p)::mCherry::chsB::chsB(t);gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW132</td>
      <td>tubA(p)::GFP::chsB::chsB(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW120</td>
      <td>tubA(p)::r-GECO::gluC(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW125</td>
      <td>h2b(p)::r-GECO::gluC(t); trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW131</td>
      <td>h2b(p)::r-GECO::trpC(t); trpC(p)::hph::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW132</td>
      <td>figA::hph (∆figA)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW133</td>
      <td>figB::hph (∆figB)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW134</td>
      <td>tubA(p)::mCherry::rimA::chsB(t); gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW113</td>
      <td>hamA::hph (∆hamA)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW-a68</td>
      <td>AnSoft-GFP::Afpyro</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW108</td>
      <td>soft(p)::sofT (∆1–504 AA N-terminus) gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW109</td>
      <td>soft(p)::sofT (∆534–1213 AA C-terminus) gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pVW112</td>
      <td>soft(p)::sofT (∆1–540 AA N-terminus, no WW domain) gpdA(p)::neo::trpC(t)</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Oligonucleotides used in this study.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Sequence (5’ to 3’)</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>chsB_fwd</td>
      <td>gaatggatgaactctacaaa atggcacagcaaggaggtt</td>
      <td>mCherry-ChsB</td>
    </tr>
    <tr>
      <td>chsB_rev</td>
      <td>aggagatcttctagaaagatgatggggcgttaaggtttc</td>
      <td>mCherry-ChsB</td>
    </tr>
    <tr>
      <td>pJet_fwd</td>
      <td>atctttctagaagatctcctacaatattc</td>
      <td>mCherry-ChsB</td>
    </tr>
    <tr>
      <td>mCherry_rev</td>
      <td>tttgtagagttcatccattccac</td>
      <td>mCherry-ChsB</td>
    </tr>
    <tr>
      <td>tubP_rev</td>
      <td>gatgaattatatttcgtcaagaag</td>
      <td>GFP-ChsB; tubA(p)::r-geco</td>
    </tr>
    <tr>
      <td>chsb_fwd</td>
      <td>atggcacagcaaggaggtt</td>
      <td>GFP-ChsB</td>
    </tr>
    <tr>
      <td>gfp_chsb_fwd</td>
      <td>ttgacgaaatataattcatcatggtttccaagggtgagg</td>
      <td>GFP-ChsB</td>
    </tr>
    <tr>
      <td>gfp_chsb_rev</td>
      <td>taacctccttgctgtgccatagcggccgctttgtaaagtt</td>
      <td>GFP-ChsB</td>
    </tr>
    <tr>
      <td>R_geco_pOL_fwd</td>
      <td>ttgacgaaatataattcatcatggtcgactcatcacgtc</td>
      <td>R-GECO (tubA(p))</td>
    </tr>
    <tr>
      <td>r-geco_tOL_rev</td>
      <td>atacatcttatctacatacgctacttcgctgtcatcatttg</td>
      <td>R-GECO (tubA(p))</td>
    </tr>
    <tr>
      <td>tgluC_gOL_fwd</td>
      <td>aaatgatgacagcgaagtagcgtatgtagataagatgtatgattag</td>
      <td>R-GECO (tubA(p))</td>
    </tr>
    <tr>
      <td>tgluC_geco_rev</td>
      <td>aggagatcttctagaaagatatcttgttggggggaaggg</td>
      <td>R-GECO (tubA(p))</td>
    </tr>
    <tr>
      <td>h2b_p_trpCOL_fwd</td>
      <td>ctttccctaaactccccccaggagaagaaaggagcaaaatc</td>
      <td>R-GECO (h2b(p))</td>
    </tr>
    <tr>
      <td>h2b_p_gecoOL_rev</td>
      <td>cgacgtgatgagtcgaccattttgaaatttgttttttgtttgggtag</td>
      <td>R-GECO (h2b(p))</td>
    </tr>
    <tr>
      <td>trpC_rev</td>
      <td>tggggggagtttagggaaag</td>
      <td>R-GECO (h2b(p))</td>
    </tr>
    <tr>
      <td>r_geco_fwd</td>
      <td>atggtcgactcatcacgtc</td>
      <td>R-GECO (h2b(p))</td>
    </tr>
    <tr>
      <td>soft_gfp_locus_fwd</td>
      <td>ctcgagtttttcagcaagattaccgtcctcagtacaacatg</td>
      <td>SofT-GFP</td>
    </tr>
    <tr>
      <td>soft_gfp_locus_rev</td>
      <td>acctcacccttggaaaccatatacccatactcgcatctgg</td>
      <td>SofT-GFP</td>
    </tr>
    <tr>
      <td>soft_GFPcas_fwd</td>
      <td>ccagatgcgagtatgggtatatggtttccaagggtgagg</td>
      <td>SofT-GFP</td>
    </tr>
    <tr>
      <td>soft_GFPcas_rev</td>
      <td>caaccgcccggacgaatcattggggggagtttagggaaag</td>
      <td>SofT-GFP</td>
    </tr>
    <tr>
      <td>soft_Term_fwd</td>
      <td>ctttccctaaactccccccaatgattcgtccgggcggtt</td>
      <td>SofT-GFP</td>
    </tr>
    <tr>
      <td>softterm_gfp_rev</td>
      <td>attgtaggagatcttctagaaagattgggacgagtgggatttaaaatgga</td>
      <td>SofT-GFP</td>
    </tr>
    <tr>
      <td>figA_lb_fwd</td>
      <td>ctcgagtttttcagcaagatTGTCGCTTGGGCTTGATAG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_lb_rev</td>
      <td>CCTCCACTAGCATTACACTTATCTGCTAACGTAACTAGACG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_hph_fwd</td>
      <td>GTCTAGTTACGTTAGCAGATAAGTGTAATGCTAGTGGAGG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_hph_rev</td>
      <td>CTAACAGGCCTATCGGAGTTTGGGGGGAGTTTAGGGAAAG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_rb_fwd</td>
      <td>CTTTCCCTAAACTCCCCCCAAACTCCGATAGGCCTGTTAG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_rb_rev</td>
      <td>aggagatcttctagaaagatCGGAGGTCGTCAAGAAGC</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_up_fwd</td>
      <td>AGGAAGACCGATTACGAAAC</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_down_rev</td>
      <td>CGATATACGATCCGAAGGTC</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_lb_g418_rev</td>
      <td>AATGCAATGTAATAGATACCATCTGCTAACGTAACTAGACG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figA_g418_fwd</td>
      <td>GTCTAGTTACGTTAGCAGATGGTATCTATTACATTGCATTGCG</td>
      <td>Deletion figA</td>
    </tr>
    <tr>
      <td>figB_lb_fwd</td>
      <td>ctcgagtttttcagcaagatGGCGAAGAGACTGGATTTATC</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_lb_rev</td>
      <td>CCTCCACTAGCATTACACTTTTTGAAGTTTTGCTGATGATGTGAG</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_hph_fwd</td>
      <td>ATCATCAGCAAAACTTCAAAAAGTGTAATGCTAGTGGAGGT</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_hph_rev</td>
      <td>TTGTTCAGCTTTTTTCCCATTGGGGGGAGTTTAGGGAAAG</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_rb_fwd</td>
      <td>CTTTCCCTAAACTCCCCCCAATGGGAAAAAAGCTGAACAAAAAAAATC</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_rb_rev</td>
      <td>aggagatcttctagaaagatCGCCTGTGTAACGGCTTTTG</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_up_fwd</td>
      <td>AGAGCCGCATGGTTTATTTAG</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>figB_down_rev</td>
      <td>AGCACAGAGTAACCTGGAC</td>
      <td>Deletion figB</td>
    </tr>
    <tr>
      <td>rimA_orf_fwd</td>
      <td>GAATGGATGAACTCTACAAAATGGAAACCCCAGCTCCAG</td>
      <td>mCherry-RimA</td>
    </tr>
    <tr>
      <td>rimA_rb_rev</td>
      <td>AGGAGATCTTCTAGAAAGATCGTTCTATGCCTGAAATCGG</td>
      <td>mCherry-RimA</td>
    </tr>
    <tr>
      <td>ham10_lb_fwd</td>
      <td>ctcgagtttttcagcaagatGGCGGATATCAATCTTATCTTG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_lb_rev</td>
      <td>CCTCCACTAGCATTACACTTGGTGACCGAAATCGCCTTAT</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_hph_fwd</td>
      <td>ATAAGGCGATTTCGGTCACCAAGTGTAATGCTAGTGGAGG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_hph_rev</td>
      <td>CACAAGGATGGCTTCCCATTTGGGGGGAGTTTAGGGAAAG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_rb_fwd</td>
      <td>CTTTCCCTAAACTCCCCCCAAATGGGAAGCCATCCTTGTG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_rb_rev</td>
      <td>aggagatcttctagaaagatCGTTCCGATTTACTCGTCG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_up_fwd</td>
      <td>GCCGAGACTACTAGCTAGG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>ham10_down_rev</td>
      <td>CTATATCGTTGGTTCGAGGG</td>
      <td>Deletion hamA</td>
    </tr>
    <tr>
      <td>soft_Nterm_tgluCOL_rev</td>
      <td>ATACATCTTATCTACATACGTTAAATACCGGTCTCCGGTGC</td>
      <td>N-terminal SofT truncation</td>
    </tr>
    <tr>
      <td>soft_ntermnoWW_tgluCol_rev</td>
      <td>ATACATCTTATCTACATACGTTATGGAAGAGGTGGGGGAGA</td>
      <td>N-terminal SofT truncation, no WW domain</td>
    </tr>
    <tr>
      <td>softProm_trpCOL_fwd</td>
      <td>CTTTCCCTAAACTCCCCCCACAGAGTTCGAATAGCGTTGC</td>
      <td>C-terminal SofT truncation</td>
    </tr>
    <tr>
      <td>softProm_CtermOL_rev</td>
      <td>ATACCGGTCTCCGGTGCCATTGTGGAGACGAAGGCAAAG</td>
      <td>C-terminal SofT truncation</td>
    </tr>
    <tr>
      <td>softCterm_fwd</td>
      <td>CCTTTGCCTTCGTCTCCACAATGGCACCGGAGACCGGTATT</td>
      <td>C-terminal SofT truncation</td>
    </tr>
    <tr>
      <td>softCterm_tgluC_rev</td>
      <td>ATACATCTTATCTACATACGTTAATACCCATACTCGCATCTG</td>
      <td>C-terminal SofT truncation</td>
    </tr>
    <tr>
      <td>VW230</td>
      <td>TTGTAAAACGACGGCCAGTGACACCAGAAATCTCTCCGAATG</td>
      <td>Soft-GFP, A. nidulans</td>
    </tr>
    <tr>
      <td>VW231</td>
      <td>GTGAAAAGTTCTTCTCCTTTCTTCCCATGCTCTAAACTCG</td>
      <td>Soft-GFP, A. nidulans</td>
    </tr>
    <tr>
      <td>VW232</td>
      <td>CGAGTTTAGAGCATGGGAAGAAAGGAGAAGAACTTTTCACTGG</td>
      <td>Soft-GFP, A. nidulans</td>
    </tr>
    <tr>
      <td>VW233</td>
      <td>TTAAAAAGACTCGGCATCAAgcgagtgtctacataatgaagg</td>
      <td>Soft-GFP, A. nidulans</td>
    </tr>
    <tr>
      <td>VW234</td>
      <td>ttcattatgtagacactcgcTTGATGCCGAGTCTTTTTAATGT</td>
      <td>Soft-GFP, A. nidulans</td>
    </tr>
    <tr>
      <td>VW235</td>
      <td>GACCATGATTACGCCAagctGGGTGACGGATTATTACCTCT</td>
      <td>Soft-GFP, A. nidulans</td>
    </tr>
  </tbody>
</table>

R-GECO was expressed under the histone h2b promoter. The R-GECO sequence was amplified from gDNA of SNT162 (Takeshita et al., 2017) and cloned into plasmid pVW92, resulting in pVW120. Subsequently, the tubA promoter was exchanged by the 1 kb sequence of the h2b promoter using Gibson assembly, resulting in plasmid pVW125. For co-localization experiments, the h2b(p)-R-GECO-fragment was cloned into pVW57, resulting in pVW131.

figA, figB, and hamA were deleted by homologous recombination. One kb flanks homologous to the 5’ and 3’ regions of the gene of interest were amplified by PCR with 25 bp overhangs homologous to either the hygromycin-B (hph) or geneticin sulfate (G418, neo) resistance cassette as well as to the pJET1.2 plasmid backbone. Verification of homologous recombination was performed as described in Wernet et al., 2022.

A. flagrans RimA was tagged with mCherry at the N-terminus and expressed under the tubA promoter. The rimA orf and 3’ region were amplified by PCR from A. flagrans gDNA and assembled into the plasmid backbone pVW82 using Gibson assembly.

Fragments of the sofT orf were amplified by PCR from A. flagrans gDNA and assembled into the plasmid backbone pJM16 using Gibson assembly for complementing the ∆sofT mutant with truncated versions of the protein. Each construct was expressed under the sofT promoter.

A. nidulans Soft was tagged with GFP at its endogenous locus with the endogenous promoter. Fragments were amplified by PCR from A. nidulans gDNA and assembled into the Blue Heron Biotechnology pUC vector.

### Microscopy

For microscopy, fungal strains were inoculated on thin LNA (1 g/l KCl, 0.2 g MgSO4 - 7H2O, 0.4 mg MnSO4 - 4H2O, 0.88 mg ZnSO4 - 7H2O, 3 mg FeCl3 - 6H2O, 15 g agar, pH 5.5) slides supplemented with 1 µM CaCl2. For calcium chelating experiments, EGTA (stock solution 0.5 M) was added at a final concentration of 5 mM. Around 1×104 A. flagrans spores were incubated on a 2×2 cm agar pad at 28°C in darkness for 12–72 hr.

Live cell imaging of A. flagrans was performed using a confocal microscope (LSM900, Carl Zeiss) with a 63× NA 1.4 oil objective lens (DIC M27). Time series were acquired with a gallium arsenide phosphide photomultiplier tube (GaAsP-PMT) detector, 488 or 561 nm excitation lasers were used. Live cell imaging of A. nidulans was performed using a Nikon Ti2 microscope mounted with a Yokogawa W1 spinning-disk confocal scan head and two Prime95B cameras. Images were acquired with the NIS Elements Advanced Research software (Nikon) with the 488 nm laser.

Image processing and analysis were performed in FIJI (Schindelin et al., 2012) and ZEN Blue. Datasets were analyzed in GraphPad Prism. Kymographs were generated with the FIJI Multi Kymograph tool using line widths 5. The dynamics of the fluorescent intensity over time were measured in each frame with a circular selection at the respective hyphal tip, specified in each figure legend. The interval between two accumulating peaks at hyphal tips was counted in ZEN Blue.

All raw images and data files resulting from the analyses are available at Zenodo (https://zenodo.org/record/6830734#.Ys_KmS2w1TY).

To quantify SofT-GFP at hyphal tips, spores were incubated on a 2×2 cm agar pads at 28°C for 24 hr and the fluorescence of 50 tips was counted three times.

### Mathematical model

Our model is based on the previous model of the dialogue-like communication between two Neurospora cells growing toward each other (Goryachev et al., 2012). The original model consists of eight ordinary differential equations, four representing each cell. Those equations represent an excitatory system that coordinates the docking and release of vesicles with chemoattractants. We extended this model by explicitly modeling the dynamics of the chemoattractants in the extracellular space at the tips of the individual cells. This is modeled by two coupled differential equations that represent the concentration of the signaling molecules in the proximity of the corresponding cells. Those two equations are linked with a coupling whose magnitude represents the coupling strength. The model was implemented in the Julia Programming Language as a set of stochastic differential equations and simulated using the Euler-Maruyama method with integration step dt = 0.001. The complete set of equations and parameter values can be found in the Supplementary Information. The simulation script is also available at https://github.com/vkumpost/cell-dialog (copy archived at Kumpošt, 2022).

The model was implemented in the form of stochastic differential equations as

$$
U˙=[A˙_{1}I˙_{1}X˙_{1}Y˙_{1}Z˙_{1}A˙_{2}I˙_{2}X˙_{2}Y˙_{2}Z˙_{2}]=\tauF(U)+\sqrt{\tau}\frac{1}{\sqrt{Ω}}G(U)
$$

where U is a vector of state variables that represent activator (A), inhibitor (I), free vesicle (X), docked vesicle (Y), and concentration of the extracellular signaling molecule at the tip of the cell (Z). The index (1, 2) indicates the specific cell. τ is a time-scaling constant to adjust the time scale without the loss of dynamics. Ω is the system size and controls the level of noise in the system. The drift function (F) reads

$$
F(U)=[a_{0}−\alphaA_{1}+\betaA_{1}^{2}−A_{1}^{3}−A_{1}I_{1}+A_{1}Z_{1}\epsilon(i_{0}+\gamma\frac{A_{1}^{2}}{A_{1}^{2}+k}−I_{1})x_{0}−k_{1}A_{1}^{2}X_{1}k_{1}A_{1}^{2}X_{1}−k_{2}\frac{1}{A_{1}^{3}+1}Y_{1}−k_{Cext}(Z_{1}−C_{media})+k_{2}\frac{1}{A_{1}^{3}+1}Y_{1}−A_{1}Z_{1}+k_{z}e^{−d}Z_{2}−k_{z}e^{−d}Z_{1}a_{0}−\alphaA_{2}+\betaA_{2}^{2}−A_{2}^{3}−A_{2}I_{2}+A_{2}Z_{2}\epsilon(i_{0}+\gamma\frac{A_{2}^{2}}{A_{2}^{2}+k}−I_{2})x_{0}−k_{1}A_{2}^{2}X_{2}k_{1}A_{2}^{2}X_{2}−k_{2}\frac{1}{A_{2}^{3}+1}Y_{2}−k_{Cext}(Z_{2}−C_{media})+k_{2}\frac{1}{A_{2}^{3}+1}Y_{2}−A_{2}Z_{2}+k_{z}e^{−d}Z_{1}−k_{z}e^{−d}Z_{2}]
$$

The noise function (G) is

$$
G(U)=[\sqrt{a_{0}}ξ_{1,1}+\sqrt{\alphaA_{1}}ξ_{1,2}+\sqrt{\betaA_{1}^{2}}ξ_{1,3}+\sqrt{A_{1}^{3}}ξ_{1,4}+\sqrt{A_{1}I_{1}}ξ_{1,5}+\sqrt{A_{1}Z_{1}}ξ_{1,6}\sqrt{\epsiloni_{0}}ξ_{1,7}+\sqrt{\epsilon\gamma\frac{A_{1}^{2}}{A_{1}^{2}+k}}ξ_{1,8}+\sqrt{\epsilonI_{1}}ξ_{1,9}\sqrt{x_{0}}ξ_{1,10}+\sqrt{k_{1}A_{1}^{2}X_{1}}ξ_{1,11}\sqrt{k_{1}A_{1}^{2}X_{1}}ξ_{1,12}+\sqrt{k_{2}\frac{1}{A_{1}^{3}+1}Y_{1}}ξ_{1,13}\sqrt{k_{Cext}Z_{1}}ξ_{1,14}+\sqrt{k_{Cext}C_{media}}ξ_{1,15}+\sqrt{k_{2}\frac{1}{A_{1}^{3}+1}Y_{1}}ξ_{1,16}+\sqrt{A_{1}Z_{1}}ξ_{1,17}+\sqrt{k_{z}e^{−d}Z_{2}}ξ_{1,18}+\sqrt{k_{z}e^{−d}Z_{1}}ξ_{1,19}\sqrt{a_{0}}ξ_{2,1}+\sqrt{\alphaA_{2}}ξ_{2,2}+\sqrt{\betaA_{2}^{2}}ξ_{2,3}+\sqrt{A_{2}^{3}}ξ_{2,4}+\sqrt{A_{2}I_{2}}ξ_{2,5}+\sqrt{A_{2}Z_{2}}ξ_{2,6}\sqrt{\epsiloni_{0}}ξ_{2,7}+\sqrt{\epsilon\gamma\frac{A_{2}^{2}}{A_{2}^{2}+k}}ξ_{2,8}+\sqrt{\epsilonI_{2}}ξ_{2,9}\sqrt{x_{0}}ξ_{2,10}+\sqrt{k_{1}A_{2}^{2}X_{2}}ξ_{2,11}\sqrt{k_{1}A_{2}^{2}X_{2}}ξ_{2,12}+\sqrt{k_{2}\frac{1}{A_{2}^{3}+1}Y_{2}}ξ_{2,13}\sqrt{k_{Cext}Z_{2}}ξ_{2,14}+\sqrt{k_{Cext}C_{media}}ξ_{2,15}+\sqrt{k_{2}\frac{1}{A_{2}^{3}+1}Y_{2}}ξ_{2,16}+\sqrt{A_{2}Z_{2}}ξ_{2,17}+\sqrt{k_{z}e^{−d}Z_{1}}ξ_{2,18}+\sqrt{k_{z}e^{−d}Z_{2}}ξ_{2,19}]
$$

where ξ are independent Wiener processes. The results presented in the manuscript were obtained for parameter values τ=8.48, ε=0.55, α=12.4, β=8.05, γ=8, k=6, a₀=5.6, i₀=0.1, x₀=1.0, k1=0.1, k2=1.0, kz = 10.0, kcext = 5, Cmedia = 1, d=10 (long distance), d=0 (short distance), Ω=1000. The initial conditions for the simulations were set to U(t=0) = [0.7065, 0.7145, 0, 0, 1.0, 0.7065, 0.7145, 0, 0, 1.0]. To minimize the effect of the initial conditions, the model was run for 200 min before any other analysis was performed.

### Particle size estimation for the signaling component

Assuming Brownian diffusion in three dimensions, the mean square distance ($L^{2}$) traveled by a particle is

$$
L^{2}=6Dt,
$$

where $D$ is the diffusion constant and $t$ the time for which the particle is followed. Inserting for the diffusion coefficient on the basis of the Stokes-Einstein relationship

$$
D=\frac{k_{B}T}{6\piηr}
$$

for a particle of radius $r$, with the Boltzmann constant $k_{B}$ , the water temperature T=298.15 K, the dynamic viscosity $η=0.89mPa⋅s$ of water at 25°C (The International Association for the Properties of Water and Steam, 2008), we obtain

$$
r≈1.5⋅10^{-18}\frac{m^{2}}{s}\frac{t}{L^{2}}.
$$

Inserting as approximate values a typical distance at which two hyphae enter into asynchronous dialogue ($L≈10\mum$) and an upper bound estimate of the time that is allowed to travel from one hypha to another and sustain oscillations with a period of $≈60s$ ($t≈10s$), we can calculate an upper bound on the particle radius: $r≲1.5nm$. This upper bound implies a maximal particle diameter of $≈3nm$, so that both ionic species (typical diameters $1nm$) as well as typical proteins (typical diameters $1−3nm$) might take the role of the signaling component, while achieving a fast enough transfer between the two hyphae by conventional Brownian diffusion. Secretory vesicles (typical diameters $\geq30nm$) exceed the upper bound, and would be unlikely to diffuse rapidly enough from one hypha to another.

### Materials availability statement

The manuscript includes a dedicated ‘materials availability statement’ providing transparent disclosure about availability of newly created materials including details on how materials can be accessed and describing any restrictions on access.
