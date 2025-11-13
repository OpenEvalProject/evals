# Rapid changes in morphogen concentration control self-organized patterning in human embryonic stem cells

## Authors

- Idse Heemskerk<sup>1</sup> ([ORCID: 0000-0002-8861-7712](https://orcid.org/0000-0002-8861-7712))
- Kari Burt<sup>1</sup>
- Matthew Miller<sup>1</sup>
- Sapna Chhabra<sup>2</sup> ([ORCID: 0000-0002-2479-0911](https://orcid.org/0000-0002-2479-0911))
- M Cecilia Guerra<sup>1</sup>
- Lizhong Liu<sup>1</sup>
- Aryeh Warmflash<sup>1</sup> ([ORCID: 0000-0002-5679-2268](https://orcid.org/0000-0002-5679-2268)) †

### Affiliations

1. Department of Biosciences Rice University Houston United States
2. Systems, Synthetic and Physical Biology Program Rice University Houston United States
3. Department of Bioengineering Rice University Houston United States

† Corresponding author

## Abstract

During embryonic development, diffusible signaling molecules called morphogens are thought to determine cell fates in a concentration-dependent way. Yet, in mammalian embryos, concentrations change rapidly compared to the time for making cell fate decisions. Here, we use human embryonic stem cells (hESCs) to address how changing morphogen levels influence differentiation, focusing on how BMP4 and Nodal signaling govern the cell-fate decisions associated with gastrulation. We show that BMP4 response is concentration dependent, but that expression of many Nodal targets depends on rate of concentration change. Moreover, in a self-organized stem cell model for human gastrulation, expression of these genes follows rapid changes in endogenous Nodal signaling. Our study shows a striking contrast between the specific ways ligand dynamics are interpreted by two closely related signaling pathways, highlighting both the subtlety and importance of morphogen dynamics for understanding mammalian embryogenesis and designing optimized protocols for directed stem cell differentiation.Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed (see decision letter).

## Introduction

Mammalian development depends crucially on diffusible signaling molecules called morphogens, that are thought to determine cell fates in a concentration-dependent manner (Green et al., 1992; Wilson et al., 1997; Wolpert, 1969), and protocols for directed stem cell differentiation are based on this picture (Chambers et al., 2009; Loh et al., 2016; McLean et al., 2007; Mendjan et al., 2014). However, in the vertebrate embryo, expression patterns of these morphogens change rapidly, simultaneous with large-scale cell movements, and therefore individual cells experience substantial changes in morphogen levels during differentiation (Arnold and Robertson, 2009; Balaskas et al., 2012; Dessaud et al., 2007; Dubrulle et al., 2015; Kinder et al., 2001; van Boxtel et al., 2015). Duration of ligand exposure must logically be a relevant parameter, as was confirmed in a number of contexts, including Activin/Nodal signaling in early Zebrafish development and Sonic Hedgehog (Shh) signaling in the mouse neural tube (Dessaud et al., 2007; Sako et al., 2016). However, duration is only one of a large number of features of a dynamic signal. It is unknown whether the precise time course of ligand exposure plays a role in cell fate decisions, and if so, whether different pathways interpret signaling histories differently. In analogy with human speech, which enables sophisticated communication by relying on temporal modulation of a single mode of signaling (sound), it is possible that complex information is encoded in developmental signals by temporal modulation to enable a range of different responses to a single pathway. In addition to ligand concentration and duration (‘integral’), cells may also be sensitive to ligand rates of change (‘derivative’), and it has been suggested that adaptive signaling pathways allow cells to perform this derivative computation (Sorre et al., 2014; Yi et al., 2000).

These concepts have begun to be explored in mammalian cell culture systems. For the Nκfb pathway, an intricate relation between ligand dynamics, signaling response and target gene activation was found (Hoffmann et al., 2002; Kellogg et al., 2017; Selimkhanov et al., 2014). Further demonstrating the importance of changing ligand concentrations, a class of ERK target genes was recently shown to be activated more efficiently by pulses than sustained signaling in 3T3 cells (Wilson et al., 2017), and we have shown that the response to TGFβ in C2C12 mouse myoblasts reflects ligand rate of increase (Sorre et al., 2014; Warmflash et al., 2012). However, these ideas have not been applied to mammalian development or differentiation of pluripotent stem cells, and their relevance to developmental patterning remains unexplored.

Gastrulation is the first differentiation event of the embryo proper, when the germ layers are formed and the body axes are established. Nodal and BMP4 are morphogens crucial for gastrulation in vertebrates (Winnier et al., 1995). In the early mammalian embryo, BMP4 is required for both initiating gastrulation and specifying the dorsal-ventral axis, while Nodal maintains the pluripotent epiblast and is subsequently required for mesoderm and endoderm differentiation (Conlon et al., 1994). Each pathway has distinct receptor complexes that phosphorylate specific signal transducers, known as receptor-Smads, which then complex with the shared cofactor Smad4 and translocate to the nucleus to activate target genes (Figure 1a) (Zinski et al., 2018). Both Nodal and BMP4 have been claimed to act in a concentration-dependent manner based on classic Xenopus experiments (Green et al., 1992; Gurdon et al., 1994; Wilson et al., 1997). However, those experiments allow alternative interpretations (Heemskerk and Warmflash, 2016), and the role of BMP4 and Nodal ligand dynamics has not been investigated.

Micropatterned human embryonic stem cells (hESCs) self-organize into reproducible spatial domains corresponding to each of the germ layers and were recently established as a method to recapitulate human gastrulation in vitro (Warmflash et al., 2014). This system can be easily manipulated and observed. Further, in contrast to the micropatterned colonies, when hESCs are grown more sparsely, their response to exogenous signals is uniform and not dependent on secondary signals, allowing for dissection of the dynamics of response (Nemashkalo et al., 2017). Thus, the response of cells to dynamic signals can be systematically investigated in sparse culture, and this information can be used to unravel the complexity of self-organized pattern formation in micropatterned colonies. In this study, we take this approach and use hESCs to evaluate the role of changing concentrations of BMP4 and Activin/Nodal in cell-fate decisions associated with gastrulation. Unexpectedly, we find an important role for rapid concentration changes in Nodal pathway response, while the BMP pathway responds to concentration and duration of ligand exposure more directly.

## Results

### SMAD4 signaling response of hESCs to BMP4 is sustained but to Activin is adaptive

To investigate how sudden increases in BMP4 and Nodal levels are interpreted by hESCs, we performed live imaging of hESCs with GFP:SMAD4 in the endogenous locus (Nemashkalo et al., 2017), and quantified signaling strength as the ratio of nuclear and cytoplasmic SMAD4 intensity (Figure 1—figure supplement 1a). We found that a sudden increase in BMP4 leads to sustained SMAD4 signaling (Figure 1b,d), consistent with our previous work (Nemashkalo et al., 2017). In contrast, the response to addition of Nodal and its substitute Activin is strongly adaptive, that is transient, and returns to a signaling baseline of around 20% of the response peak (Figure 1c,d, Figure 1—figure supplement 1i, j), similar to the previously observed response to TGFβ in C2C12 cells (Sorre et al., 2014; Warmflash et al., 2012). The response to recombinant Nodal was weak at all doses, likely reflecting the low quality of recombinant Nodal. To elicit a response in Nodal required 2 μg/ml of recombinant protein, whereas the response to Activin was saturated by 5 ng/ml (Figure 1f, Figure 1—figure supplement 1i, j). However, when the responses to Nodal and Activin were normalized to their respective maxima, their dynamics were identical (Figure 1—figure supplement 1j). Given our focus on the dynamics of signaling, the extremely similar dynamics in response to Nodal and Activin, and the impracticality of performing experiments with Nodal given the concentrations required, we used Activin in all further experiments. The peak and baseline signaling levels, but not the timescale of adaptation, depended on the Activin dose (Figure 1f). For BMP4, there was a sharp response so that even low doses gave a nearly full initial response, however, the dose affected the duration of signaling in a way consistent with ligand depletion at low doses (Figure 1e, Appendix 1). Immunofluorescence staining for receptor-Smads revealed that SMAD1/5/8 activation mirrors the SMAD4 response to BMP4, while in response to Activin, SMAD2/3 nuclear localization adapts less than SMAD4 to about 60% of peak response (Figure 1—figure supplement 1e,g,h). In each case, the response was due to the added ligand and not to induced secondary signaling through the other pathway, as addition of the BMP inhibitor Noggin had no effect on the dynamics in response to Activin, while addition of the Activin inhibitor SB431542 slightly increased the response to BMP (Figure 1g,h). Thus, endogenous BMP has no effect on the Nodal response, while Nodal signaling has a repressive effect on BMP. We note that some target genes may respond to SMAD2/3 without SMAD4 (Levy and Hill, 2005), and that since the dynamics of SMAD2/3 and SMAD4 are different, care is required in interpreting the dynamics of individual genes. Hereafter, when we refer to Nodal signaling as reflected by the SMAD4 reporter, we mean ‘SMAD4-dependent Nodal signaling’.

![Figure 1.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig1-v1.jpg)

**Figure 1.:** (a) BMP and Nodal pathways share the signal transducer Smad4. (b, c) hESCs expressing GFP:SMAD4 at 0, 1 and 6 hr after treatment with BMP4 (b) or Activin (c). Scalebar 30 μm (d) GFP:SMAD4 average nuclear:cytoplasmic intensity ratio after treatment with BMP4 (blue) or Activin (red). Error bars represent standard error. Ncells ~ 700, distributions shown in (Figure 1—figure supplement 1b–c). (e) SMAD4 response to different doses of BMP4 shows decline at low doses with a dose-dependent time scale, suggesting ligand depletion. Doses in graph legend are in ng/ml. (f) SMAD4 signaling response to different doses of Activin shows fixed time scale of adaptation. (g) Quantification of GFP:SMAD4 nuclear to cytoplasmic ratio in response to either Activin alone or together with the BMP inhibitor Noggin (h) Quantification of GFP:SMAD4 nuclear to cytoplasmic ratio in response to either BMP alone or together with the Activin/Nodal inhibitor SB431542.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Quantification of SMAD4 signaling as nuclear to cytoplasmic intensity ratio using automated segmentation of the nuclei. For SMAD4 and SMAD2, signaling strength is measured by the nuclear to cytoplasmic intensity ratio. (b) Distribution of SMAD4 response to BMP4 at 0, 1, and 6 hr after treatment. (c) Distribution of SMAD4 response to Activin at 0, 1, and 6 hr. (d, e) Time courses of pSMAD1 (d) and SMAD2 (e) determined by immunofluorescence. Scalebar 25 μm. (f) Quantification of pSmad1 time course. (g) Quantification of SMAD2 and SMAD4 nuclear signaling (nuclear to cytoplasmic ratio). Error bars represent standard error. Ncells per time point ~103. (h) same data as (g) normalized so that the mean in SB431542 treated cells is zero and peak signaling is 1. The level of SMAD2 intensity at time 0 indicates baseline signaling which is repressed by SB431542.(i) Comparison of the response of GFP:SMAD4 to either Activin or Nodal. (j) Same data as in the (i) except that the baseline from the control BSA only condition was subtracted from each curve and each was then normalized to its maximum value. (k) Control for Figure 1g showing complete inhibition of response to 50 ng/ml BMP4 by 500 ng/ml Noggin.

### Adaptive signaling is caused by negative feedback controlling sequestration

Although TGFβ signaling through SMAD4 has been shown to adapt in C2C12 cells (Sorre et al., 2014; Warmflash et al., 2014), the molecular mechanisms remain unclear. A previous attempt to uncover relevant genes through a genome-wide siRNA screen uncovered a large number of potential regulators of signaling, but none of the knockdowns completely blocked adaptation, suggesting redundancy in adaptation mechanisms (Deglincerti et al., 2015). As an alternative approach, we used FRAP at different times after Activin treatment to better understand how cells modulate nuclear SMAD4 levels over the course of the signaling response (Figure 2a–c). In particular, we performed measurements before ligand treatment, after 1 hr of treatment when signaling peaks, and after 6 hr when signaling has adapted (Figure 2c). In all cases, we observed recovery on a timescale of minutes following nuclear photobleaching, which confirmed that SMAD4 continuously shuttles between the nucleus and cytoplasm even in the absence of ligand stimulation (Figure 2d). We also observed a reduced recovery rate after 1 hr of Activin treatment, consistent with previous work on TGFβ signaling which suggested that nuclear accumulation of SMAD4 is caused by reduced nuclear export (Nicolás et al., 2004; Schmierer and Hill, 2005). Importantly, however, we found that the recovery rate is not restored during adaptation (Figure 2d), showing that cells do not revert to a pre-signaling state. This excludes upstream mechanisms of adaptation as might be caused by secretion of extracellular feedback inhibitors or depletion of receptors or R-Smads (Vizán et al., 2013). Moreover, mathematical modeling showed that if adaptation is caused by depletion of an upstream component such as receptors, then the magnitude of adaptation is governed by the ratio of the degradation rates of active and inactive receptors (Appendix 1). These degradation rates also control the timescales for adaptation and recovery so that strong adaptation necessitates a large difference in timescales. However, we do not see these different time scales in our pulse experiments below (see Figure 5), which show that the refractory period after ligand exposure is similar to the time scale of adaptation. In contrast, models with negative feedback causing inhibition of downstream signaling are capable of explaining all features of our data including the observed time scales (Appendix 1).

![Figure 2.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig2-v1.jpg)

**Figure 2.:** (a) Photobleaching and recovery of nuclear Smad4 at 2 hr after Activin treatment. Scalebar 5 μm. (b) Exponential fit to recovery of nuclear fluorescence after bleaching yields amplitude A and recovery rate k. Intensity drop at t = 0 shows bleaching event. (c) Photobleaching was performed on untreated cells, at the peak response to Activin, and after adaptation. (d) Boxplot of distribution of recovery rates. Recovery rates at peak signaling and after adaptation are significantly smaller than for untreated cells (t-test p < 10−6), the difference in recovery rate between peak signaling and adapted state is not significant. N > 12 cells for each FRAP condition. (e) Boxplot of distribution of recovery amplitudes. (f) Nuclear to cytoplasmic intensity ratio after bleaching (R’) is systematically smaller than nuclear to cytoplasmic intensity ratio before bleaching (R). (g) Cartoon of mathematical model for Smad4 localization, with sequestered populations of Smad4 that are confined to either nucleus or cytoplasm, and free Smad4 shuttling with import/export rates kin/kout. (h) Cartoon demonstrating that this model explains results in (f). (i) Changes in Smad4 sequestration in nucleus (blue) and cytoplasm (red) determined through model fitting. Error bars in i and j represent error propagation of standard errors in measured parameters over N > 12 cells as described in Appendix 1. (j) Nuclear export rates, which given the fixed nuclear import rate of the model directly reflect the measured exchange rates k.

To understand the mechanism of this inhibition, we first considered fitting our FRAP data to a model in which the entire population of SMAD4 is free to shuttle between the nucleus and cytoplasm. In this case, bleaching reduces the total pool of observable GFP-SMAD4 molecules but the nuclear to cytoplasmic intensity ratio depends only on the kinetic constants, and therefore would recover to the same value following bleaching. However, we observed that this ratio systematically decreases after nuclear bleaching (Figure 2f). This suggests a more general model that includes sequestered SMAD4, which may move within but not between the nuclear and cytoplasmic compartments. Because production and degradation are slow compared to shuttling, recovery from bleaching comes only from redistribution of unbleached molecules. The nuclear sequestered population is not exported to the cytoplasm, while the cytoplasmic sequestered population is unavailable to enter the nucleus and replenish the population of unbleached molecules there, leading to a reduced nuclear to cytoplasmic ratio after equilibration of the free dark and fluorescent molecules through exchange (Figure 2g,h, Appendix 1). The parameters obtained from fitting this model to our data suggest that initial accumulation of SMAD4 in the nucleus reflects both a lower export rate and a reduction in cytoplasmic sequestration (Figure 2i,j). Adaptation, however, does not result from altering shuttling kinetics, but instead reflects reduced nuclear sequestration and increased cytoplasmic sequestration. Thus, taken together, our FRAP data and mathematical modeling suggest a mechanism of adaptation that relies on negative feedback and acts by modulating sequestration rather than nuclear exchange rates.

### Transcriptional dynamics of differentiation targets follows SMAD4 dynamics

Next, we evaluated transcriptional dynamics downstream of BMP4 and Activin using qPCR, which showed that BMP targets are stably induced (Figure 3a), while differentiation targets of Nodal show adaptive transcription on a timescale consistent with SMAD4 signaling (Figure 3b). Moreover, shared targets of the pathways were found to be transcribed adaptively in response to Activin and stably in response to BMP4 (Figure 3c, Figure 3—figure supplement 1a). In contrast, the transcription of NODAL, WNT3, and their inhibitors LEFTY1 and CER1 were sustained upon Activin treatment (Figure 3d). Molecularly, the two classes of transcriptional dynamics in response to Activin may reflect differential requirements for SMAD4 signaling levels with lower levels required to maintain the targets with sustained dynamics so that these are continuously transcribed due to the baseline signaling following adaptation. Alternatively, transcription of these genes may require only SMAD2/3 activation, which is more sustained than that of SMAD4 (Figure 1—figure supplement 1e,g,h). The differences in expression of these sets of targets are not due to differences in mRNA stability as mRNAs for stably expressed genes were found to decline rapidly upon pathway inhibition with SB431542 indicating a need for ongoing signaling to maintain expression (Figure 3—figure supplement 1g).

![Figure 3.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig3-v1.jpg)

**Figure 3.:** (a, b) qPCR measurements of transcriptional response to BMP4 treatment (a) and of differentiation targets to Activin (b) y-axes show relative CT values. (c) Transcription of the shared Activin/BMP4 target HAND1 after BMP4 (blue) or Activin (red) treatment. (d) Non-adaptive response to Activin of ligands and inhibitors involved in initiating the primitive streak. (e) Transcriptional response to Activin under pluripotency maintaining conditions (red) and mesendoderm differentiation conditions (blue) of Activin target LHX1 (e) and joint Activin/Wnt target EOMES (f). Error bars represent standard deviations over three replicates. Logarithms are base 2.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (a) Transcriptional response of NOGGIN to BMP4 (blue) and Activin (red) follows SMAD4 dynamics of respective pathways. (b-d) Genes in several functional classes show non-adaptive transcriptional response to Activin. (b) Non-cell fate related (TGF-β targets). (c) Differentiation genes, MIXL1 is an exception and responds non-adaptively to Activin, SOX17 does not respond in the pluripotent state. (d) Pluripotency genes. (e) CER1 is a non-adaptive target of Activin that behaves identically under under pluripotency (+FGF) and differentiation (+Wnt) conditions. (f) Like EOMES, BRA response is enhanced under differentiation conditions but the dynamics are qualitatively similar. (g) Decline in expression levels after SB treatment in mTeSR medium shows mRNA half lives of 1–4 hr.

The sustained transcription of Nodal and Wnt pathway ligands and inhibitors may be required to activate the positive feedbacks between the Nodal and Wnt pathways, which are known to be involved in establishing the primitive streak, the region of the mammalian embryo where mesoderm and endoderm form (Ben-Haim et al., 2006). This suggests a picture where stable transcription of the ligands and inhibitors allows for the establishment of signaling patterns in the embryo, while cells receiving these signals to differentiate interpret them according to their dynamics. Several other genes not related to mesendoderm differentiation were also found to be stably induced by Activin (Figure 3—figure supplement 1b–d).

The measurements above were performed by adding Activin to mTeSR1 media which contains high levels of FGF. Activin/Nodal signaling plays a dual role in the early embryo and is involved in both maintaining pluripotency, and differentiation to primitive streak fates. It maintains epiblast pluripotency in combination with FGF (James et al., 2005; Vallier et al., 2005), and while differentiation genes are transiently induced by Activin treatment in the presence of only FGF, cells do not robustly differentiate. In contrast, Activin induces primitive streak fates when Wnt is present. We asked whether target genes also respond adaptively to Activin/Nodal signaling during this differentiation. Initial transcriptional response was found to be qualitatively similar with or without Wnt activation, although shared targets of Wnt and Activin such as the mesendodermal markers EOMESODERMIN (EOMES) and BRACHYURY (BRA) showed a stronger response and were stably reactivated following adaptation on longer time scales (Figure 3e,f, Figure 3—figure supplement 1e,f).

### BMP4 response reflects concentration, Activin response reflects rate of concentration increase

Sustained response to BMP4 suggests sensing of ligand concentration. In contrast, adaptive response to Activin with dose-dependent amplitude suggests sensing of ligand rate of increase. We directly tested whether cells are sensitive to the rate of increase of Activin, but not BMP4, by slowly raising ligand concentrations (concentration ramp) and comparing the response with the response to a single step to the same final dose (Figure 4a,d). If cells are primarily sensitive to ligand doses, the step and ramp should eventually approach the same final activity, while if cells are sensitive to the rate of ligand increase, the response to the ramp should be reduced. As expected, BMP4 signaling responses to the ramp and step approached each other as ramp concentration increased, while Activin signaling was dramatically reduced in the case of the ramp (Figure 4b,e). Moreover, transcriptional dynamics of the shared target HAND1 matched the signaling pattern and showed dramatically reduced transcription in response to the Activin but not the BMP ramp (Figure 4c,f). As noted in the discussion of Figure 1e, the BMP response is switch-like with increasing dosage, and this was reflected by the ramp approaching the levels of the step within the first few increases. Similar results were obtained for other adaptive Activin targets, in contrast to non-adaptive Activin targets which, as expected, also showed sustained transcription in response to the ramp (Figure 4—figure supplement 1). Finally, we varied the rate of the ramp of Activin and found that intermediate rates of increase also yielded intermediate signaling responses (Figure 4g,h).

![Figure 4.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig4-v1.jpg)

**Figure 4.:** (a, d) Ligand concentration over time for slow ramp (blue) or sudden step (red) in BMP4 (a) or Activin (d). (b, e) SMAD4 signaling response to BMP4 (b) or Activin (e). (c, f) Transcriptional response of HAND1 to concentration ramp versus step for BMP4 (c) or Activin (f). Error bars in qRT-PCR data (c, f) represent standard deviations over three replicates. (g, h) Activin response to different ramp rates and step sizes. In (b, e, h) small hourly wiggles are artifacts of performing media changes and do not reflect actual signaling responses.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) Transcription of MIXL1, a non-adaptive Activin target reaches the same levels after Activin ramp and step. (b, c) Transcriptional response of MESP1 (b) and NOG (c) to Activin ramp and step shows reduced transcription for ramp. (d) Transcriptional response of ID2 to BMP4 ramp and step.

### Repeated rapid increases in Activin/Nodal enhance differentiation to primitive streak fate

Morphogens control cell fate, and the dependence of transcription of mesodermal and endodermal genes on Activin rate of increase suggests rapid Activin increase may boost differentiation to these fates. We hypothesized that exposing cells to repeated rapid increases by pulsing the level of Activin could enhance this effect. To rigorously test this hypothesis, we grew cells in differentiation conditions and compared pulses that switch between high and low doses of Activin with a sustained high Activin dose while performing media changes at the same times (‘dummy pulses’) (Figure 5a). Each pulse of Activin elicited a strong response in the translocation of SMAD4 to the cell nucleus, while no such responses were seen in response to the dummy pulses (Figure 5b). Differentiation to mesendooderm as marked by Bra expression was also enhanced under pulsed conditions (Figure 5c,d), despite the reduced integrated ligand exposure. Continuous exposure to lower doses of Activin and treating cells with Activin for the same total time as the three pulses but in a single pulse showed that the effect is specific to pulsed Activin and not a consequence of simply reducing the integrated Activin exposure (Figure 5e–g, Figure 5—figure supplement 1).

![Figure 5.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig5-v1.jpg)

**Figure 5.:** (a) Schematic of pulse experiment, graph shows ligand concentration, controls receive media changes at the same time as the pulsed well. (b) SMAD4 signaling profile in response to Activin pulses (red), high Activin (yellow), and no Activin (blue). (c) Immunofluorescence staining for BRA after high constant Activin or pulsed Activin. Scalebar 100 μm. (d) Distribution of BRA expression per cell (Ncells per condition ~6 × 103) determined from immunofluorescent images (c). (e, f, g) Dose response series showing BRA expression monotonically increases with Activin dose, and therefore the effect of pulses is not due to reduced average Activin exposure. (e) Immunofluorescence staining for BRA after 34 hr differentiation with different doses of Activin. (f) Distributions of BRA intensity per cell in the images containing (d). (g) Cumulative distributions of BRA intensity.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a-c) Comparison of BRA expression in hESCs exposed to either three short pulses of high Activin concentration or to a single pulse with same total duration, demonstrating that the effect of pulses is not simply due to reduced overall time in Activin. (a) Schematic of the protocol. (b) Immunofluorescence stainings for BRA. Scalebar 100 μm. (c) Quantification of the distribution of BRA intensities in single cells (Ncells per condition ~6 × 103).

### Rapid changes in endogenous Nodal signaling occur during self-organized patterning

To test whether rapid concentration increases are relevant to endogenous Nodal during embryonic patterning, we turned to micropatterned colonies of hESCs treated with BMP4. These colonies differentiate in a spatial pattern with reproducible rings of extraembryonic cells and all three germ layers, and represent a model for the patterning associated with gastrulation in the human embryo (Heemskerk and Warmflash, 2016; Warmflash et al., 2014). Nodal signaling is required for the formation of mesoderm and endoderm within these colonies, and both small molecule inhibition and genetic knockout of Nodal drastically reduce mesendoderm differentiation (Chhabra et al., 2018; Warmflash et al., 2014). For the dynamics described here to be relevant, Nodal signaling should evolve rapidly compared to the timescale for adaptation, and we should observe rapidly changing signaling patterns with the GFP:SMAD4 reporter. In contrast, if cells read a stable gradient of Nodal protein during patterning, as posited by classic models, we would expect correspondingly stable patterns in signaling and the adaptive dynamics would not be relevant.

To distinguish these hypotheses, we used live imaging to observe SMAD4 signaling in micropatterned colonies during the 42 hr in which these patterns form (Figure 6a-c). The cells initially respond uniformly to the BMP4 treatment. The response then is restricted to the colony edge by approximately 12 hr (Figure 6a,b), and this pattern is maintained until approximately 25 hr. Beginning at 25 hr, a wave of increased nuclear SMAD4 spreads inward again from the edge (Figure 6a,c). SMAD4 convolves the BMP and Nodal responses, and we hypothesized that the stable response at the edge of the colony represents BMP signaling while the inward moving wave results from Nodal signaling. To test this, we looked at the pathway specific SMAD1 and SMAD2/3 (Figure 6d-g). These confirmed that the BMP-specific active SMAD1 signaling remains restricted to the edge (Figure 6f), while the Nodal transducer SMAD2/3 activity spreads rapidly inward from the colony edge between 24 and 36 hr (Figure 6e). The SMAD2/3 and SMAD4 signal transducers reveal a rapidly evolving Nodal distribution with a wavefront that moves through the colony at approximately one-cell diameter (10 μm) per hour. The velocity of the Nodal wavefront suggests that individual cells see Nodal levels increase rapidly in 1 hr, consistent with the time scale of ligand increase required for strong response to exogenous ligand in the previous experiments. Importantly, this wave of signaling activates Bra expression in its wake (Figure 6g,h). This indicates that rapid increases in endogenous Nodal signaling are associated with mesoderm differentiation in this model of human gastrulation.

![Figure 6.](https://cdn.elifesciences.org/articles/40526/elife-40526-fig6-v1.jpg)

**Figure 6.:** (a) Average radial profile of SMAD4 signaling over time (kymograph) in micropatterned colonies after BMP4 treatment (N = 4 colonies). (b) SMAD4 signaling in single colony at 40 hr. (c) Radial SMAD4 signaling profiles at discrete times from 20 hr to 40 hr. (d) Immunofluorescence staining 40 hr after BMP4 treatment for pSMAD1, SMAD2/3 and BRA. (e, f, g) Normalized radial profiles of SMAD2/3 (e) pSMAD1 (f) and BRA (g) averaged over N > 5 colonies per time. (h) Half-maximum versus time for SMAD2/3 (blue), SMAD4 (purple) and pSMAD1 (red) and BRA expression domain defined by a threshold of at least 20% of maximal expression (yellow). In all panels, error bars represent standard deviations taken over different colonies.

## Discussion

Our work shows that morphogens in the mammalian embryo do not act in a purely concentration-dependent matter and has revealed an important role for Activin/Nodal rate of change in specifying cell fate as a consequence of adaptive signaling. Adaptive signaling could serve to restrict the response to a narrow competence window or to separate the multiple roles of a single morphogen by using distinct dynamics to selectively activate different target genes, effectively expanding the information content of the morphogen gradient (Selimkhanov et al., 2014). It is currently unclear whether adaptive signaling is an intrinsic feature of the Activin/Nodal pathway or is context dependent. A recent study found that Activin target genes are induced more stably when cells are also treated with Wnt, but that the dynamics of Smad2 translocation were not affected (Yoney et al., 2018). For Wnt, costimulation with Activin or BMP switches the dynamics of Wnt signaling from transient to sustained, and it will be interesting to determine whether Activin/Nodal signaling is sustained in some contexts (Massey et al., 2019).

Activin and Nodal are generally thought of as text-book morphogens acting in a concentration-dependent manner (Gilbert, 2014). This is based on experiments in which an artificial gradient is created by placing an Activin-soaked bead in an intact animal cap or in which dissociated Xenopus animal cap cells are exposed to a range of Activin concentrations (Green et al., 1992; Gurdon et al., 1994). It is important to note that these experiments are not inconsistent with our findings. In both cases, the highest concentration corresponds to the highest rate of concentration increase, and our results also show the peak of the transient signaling response induced by a step increase is dose-dependent. This fact could underlie the differences in cell fates observed in dissociated animal cap cells.

Our results are in contrast to those for another well-characterized system, the patterning of the neural tube by Shh, which has also been shown to be adaptive and regulates cell fate decisions through a described gene regulatory network (Balaskas et al., 2012). In that case, adaptation depends on upstream inhibition and results in a relatively constant integrated signaling output in which time and duration can be interchanged (Dessaud et al., 2007). This interchangeability between concentration and duration can be achieved by upstream feedback such as degradation of activated receptors. Intuitively, increasing ligand concentration increases the response but also leads to more rapid degradation of receptors limiting the response in time.

Several lines of reasoning argue that adaptation in Activin/Nodal signaling follows a different mechanism, with consequences for cell fate. The signaling behavior of our system is qualitatively different, as there is no tradeoff between concentration and duration of strong signaling. Longer exposure to ligand does not increase the duration of signaling because the system has already adapted, and reactivating the pathway can only be achieved by pulsing rather than extending the duration of ligand exposure. Interestingly, there is a low level of baseline signaling following adaptation which is maintained by continued ligand exposure. Given the distinct classes of target genes we found responding to each aspect of the signal (baseline and adaptive pulse), this may demonstrate the principle that dynamic signals relay more information through a single pathway, with one set of target genes responding to signal duration, and another to rapid signal increase.

In addition to the qualitative behavior being inconsistent with a system that integrates signal, like the neural tube, our quantitative data and mathematical modeling rule out the mechanism that would most naturally implement such a behavior, namely adaptation through degradation. First, our FRAP measurements show that the adapted state is kinetically distinct from the pre-signaling state, while the degradation model would predict a return to the same state. Second, we show analytically in Appendix 1 that a model based on upstream feedback cannot account for our dynamic measurements because in order to adapt through receptor degradation, the timescale for recovery must be slower than that for adaptation, which is not what we find in our pulsing experiments. It will be interesting to elucidate the genetic network that interprets adaptive Nodal signaling and to compare it with the one that interprets Shh.

Our conclusions regarding signaling dynamics rely on nuclear localization of Smads as a proxy for signaling activity. The validity of this measure is supported by strong correlation between SMAD2 nuclear localization and pSMAD2 levels, as well as the fact that transcriptional activity of a number of direct targets mirrors nuclear SMAD4 both in this paper and in previous work (Warmflash et al., 2012). Although some target genes do not follow this time course, it is important to note that target gene dynamics represent those of signaling filtered through a specific promoter (Dubrulle et al., 2015). For example, a promoter with high affinity for the signal transducer will saturate at low levels and will not reflect fluctuations in signaling that remain above these levels. Although it was shown that blocking nuclear export of Smad4 does not interfere with function of the pathway (Biondi et al., 2007), this does not invalidate our conclusions, as blocking nuclear export of Smad4 destroys the strong correlation between pathway activity and nuclear localization by artificially keeping Smad4 in the nucleus following the termination of transcription.

Although relatively unexplored in the context of development, adaptive signaling is a common feature of biological systems. Well-studied examples in bacteria include the chemotactic response where adaptive signaling allows cells to sense the rate of change and move to areas of higher nutrients (Block et al., 1983), and the σb response where it allows cells to sense the rate of increase of environmental stress (Young et al., 2013). In mammalian cells, stimulation with TNFα leads to a transient pulse of NFκB signaling, followed by a low, sustained baseline, and this has been suggested to allow specificity in target gene activation with different targets responding to different features of the dynamics (Hoffmann et al., 2002). Similarly, DNA damage has been shown to give rise to stereotyped pulses of p53 signaling due to negative feedback (Lahav et al., 2004).

It will be important to understand how our results fit with current protocols for directed stem cell differentiation which typically perform a single media change per day and therefore do not take advantage of potential enhancements resulting from optimizing ligand dynamics. Routinely, ranges of ligand concentration are explored to optimize differentiation protocols. Our results suggest a different approach that starts with characterizing the signaling dynamics during each cell fate decision and then optimizing the relevant dynamics of ligand presentation. As such, we believe the results presented here will serve as a basis for a dynamic understanding of embryonic patterning and stem cell differentiation.

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
      <td>Cell line (Homo sapiens)</td>
      <td>ESI017</td>
      <td>ESIBIO</td>
      <td>RRID:CVCL_B85</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>RUES2</td>
      <td>Ali Brivanlou (Rockefeller)</td>
      <td>RRID:CVCL_B810</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Brachyury</td>
      <td>R and D Systems</td>
      <td>RRID:AB_2200235</td>
      <td>(1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-Sox2</td>
      <td>Cell Signaling Technologies</td>
      <td>RRID:AB_1904142</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Nanog</td>
      <td>BD Biosciences</td>
      <td>RRID:AB_1645598</td>
      <td>(1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Smad2/3</td>
      <td>BD Biosciences</td>
      <td>RRID:AB_398162</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-pSmad1</td>
      <td>Cell Signaling Technologies</td>
      <td>RRID:AB_2493181</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Image processing and data analysis code</td>
      <td>This study</td>
      <td>https://github.com/idse/stemcells/ commit a5ee164</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell lines

The cell lines used were ESI017 and RUES2 GFP:Smad4 RFP:H2B. ESI017 cells were obtained directly from ESIBIO while RUES2 were a gift of Ali Brivanlou (Rockefeller University). The identity of these cells as pluripotent cells was confirmed via triple staining for pluripotency markers OCT4, SOX2, and NANOG. All cells were routinely tested for mycoplasma contamination and found negative.

### Cell culture and differentiation protocols

The cell lines and their maintenance are described in Nemashkalo et al. (2017). For all experiments except micropatterning, cells were seeded at a low density of 6 × 104 cells per cm2 and grown with rock-inhibitor Y27672 (10 uM; StemCell Technologies). This ensured uniform response to exogenous ligand and minimized the effect of secondary endogenous signaling. Unless otherwise indicated in the figures, experiments in Figures 1–3 were done in mTeSR1 medium (StemCell Technologies) (also referred to as pluripotency conditions), and cells were treated with 50 ng/ml Activin A (R and D Systems) or 50 ng/ml BMP4 (R and D Systems). Noggin was used at 500 ng/ml. SB431542 at 10 μM. Differentiation conditions in Figure 3e,f are defined as Essential six medium (Gibco) +3 μM CHIR99021 (StemCell technologies).

### Imaging and image analysis

Live imaging was done on an Olympus/Andor spinning disk confocal microscope with a 40×, NA 1.25 silicon oil objective. Immunofluorescence data for Figure 5 were collected using a 20×, NA 0.75 objective on an Olympus IX83 inverted epifluorescence microscope. Fixed micropatterned colonies for Figure 6 were imaged using an 30x NA 1.05 silicon oil objective on an Olympus FV1200 laser scanning confocal microscope. All image analysis used Ilastik (Sommer et al., 2011) for initial segmentation and custom written MATLAB code, available at https://github.com/idse/stemcells for further analysis (Heemskerk, 2019; copy archived at https://github.com/elifesciences-publications/stemcells). Figure 1—figure supplement 1a shows how Smad4 nuclear to cytoplasmic ratio, our measure for signaling intensity, is defined from the segmentation by subtracting the mean value in the background mask from nuclear and cytoplasmic masks for each cell. Smad2/3 signaling was similarly measured by nuclear to cytoplasmic ratio. Since pSmad1 and Bra are purely nuclear, these were measured by nuclear intensity, normalized by DAPI to correct for intensity variation due to optics.

### FRAP

FRAP experiments were done on an Olympus FV1200 laser scanning confocal microscope using a 100x NA 1.49 oil objective. To deal with cell movement recovery, curves were obtained by reading out a polygon defined by the interpolation between the initial bleach window and a manually defined polygonal nuclear mask in the final frame. Supplemental Information describes the mathematical model for nuclear localization of Smad4 which is shown schematically in Figure 2g,h, and the inference of model parameters shown in Figure 2i,j from the data.

### qPCR

For qPCR experiments, ESI017 cells were grown in 24-well plates. RNA was extracted using Ambion RNAqueous-Micro Total RNA Isolation Kit and cDNA synthesis was performed with Invitrogen SuperScript Vilo cDNA Synthesis Kit according to the manufacturer’s instructions. Measurements were performed with SYBR green and the primers in the Table 1. ATP5O was used for normalization in all experiments.

**Table 1.**
 qPCR primers used in this study.


<table>
  <tbody>
    <tr>
      <td>ATP5O</td>
      <td>ACTCGGGTTTGACCTACAGC</td>
      <td>AAAATGAACGGACAGAACCG</td>
    </tr>
    <tr>
      <td>BRA</td>
      <td>TGCTTCCCTGAGACCCAGTT</td>
      <td>GATCACTTCTTTCCTTTGCATCAAG</td>
    </tr>
    <tr>
      <td>CER</td>
      <td>ACAGTGCCCTTCAGCCAGACT</td>
      <td>ACAACTACTTTTTCACAGCCTTCGT</td>
    </tr>
    <tr>
      <td>GATA3</td>
      <td>TTCCTCCTCCAGAGTGTGGT</td>
      <td>AAAATGAACGGACAGAACCG</td>
    </tr>
    <tr>
      <td>HAND1</td>
      <td>GTGCGTCCTTTAATCCTCTTC</td>
      <td>GTGAGAGCAAGCGGAAAAG</td>
    </tr>
    <tr>
      <td>ID2</td>
      <td>GCAGCACCTCATCGACTACA</td>
      <td>AATTCAGAAGCCTGCAAGGA</td>
    </tr>
    <tr>
      <td>ID4</td>
      <td>CCCTCCCTCTCTAGTGCTCC</td>
      <td>GTGAACAAGCAGGGCGAC</td>
    </tr>
    <tr>
      <td>LEFTY1</td>
      <td>ACCTCAGGGACTATGGAGCTCAGG</td>
      <td>AGAAATGGCCAATTGAAGGCCAGG</td>
    </tr>
    <tr>
      <td>LHX1</td>
      <td>TCCCCAATGGTCCCTTCTC</td>
      <td>CGTAGTACTCGCTCTGGTAATCTCC</td>
    </tr>
    <tr>
      <td>MIXL1</td>
      <td>CCGAGTCCAGGATCCAGGTA</td>
      <td>CTCTGACGCCGAGACTTGG</td>
    </tr>
    <tr>
      <td>NANOG</td>
      <td>CCGGTCAAGAAACAGAAGACCAGA</td>
      <td>CCATTGCTATTCTTCGGCCAGTTG</td>
    </tr>
    <tr>
      <td>NODAL</td>
      <td>ATGCCAGATCCTCTTGTTGG</td>
      <td>AGACATCATCCGCAGCCTAC</td>
    </tr>
    <tr>
      <td>NOG</td>
      <td>CATGAAGCCTGGGTCGTAGT</td>
      <td>TCGAACACCCAGACCCTATC</td>
    </tr>
    <tr>
      <td>OCT4</td>
      <td>GGGCTCTCCCATGCATTCAAAC</td>
      <td>CACCTTCCCTCCAACCAGTTGC</td>
    </tr>
    <tr>
      <td>SOX2</td>
      <td>CCATGCAGGTTGACACCGTTG</td>
      <td>TCGGCAGACTGATTCAAATAATACAG</td>
    </tr>
    <tr>
      <td>TBR2/EOMES</td>
      <td>CACATTGTAGTGGGCAGTGG</td>
      <td>CGCCACCAAACTGAGATGAT</td>
    </tr>
    <tr>
      <td>WNT3</td>
      <td>CTCGCTGGCTACCCAATTT</td>
      <td>GAGCCCAGAGATGTGTACTGC</td>
    </tr>
  </tbody>
</table>

### Pulses

For pulse and dose response experiments in Figure 5, differentiation was done in Essential six medium +1 uM CHIR99021 +20 ng/ml bFGF (Life Technologies)+10 uM Y27672 with 30 ng/ml Activin added as indicated in the figures. Time between pulses was always 5 hr to allow the pathway to relax. Duration of individual pulses was chosen for experimental convenience and lengths of pulses shown in Figure 5 are 6, 10, and 8 hr. Controls were subjected to media changes at the same time. During media changes, cell were washed three times with PBS.

### Micropatterning

For micropatterned colonies, we followed the protocol in Deglincerti et al. (2016) using the chemically defined medium mTeSR1. For fixed micropatterns, we used the CYTOO Arena EMB chip and analyzed the 800 um colonies, while for live imaging we used a CYTOO 96-well plate RW DS-S-A, which has 700 um colonies. For the analysis in Figure 6, radial profiles of SMAD1 and SMAD2/3 were normalized to have the lowest signaling level be zero and the highest be one in at each time, as minimal and maximal levels were similar at each time and only their spatial distribution varied. SMAD4 was normalized such that its maximum over all positions interior in the colony to the most interior half-maximum of pSMAD1 intensity was equal to one. This position was chosen for normalization as it reflects the peak of Nodal-dependent SMAD4 signaling. Finally, because BRA levels change substantially, BRA at all times was normalized to the maximum of the latest time (48 hr).

### Immunostaining

Fixing and immunostaining of cells was done as described in Nemashkalo et al. (2017). Table 2 lists the antibodies that were used.

**Table 2.**
 Antibodies used for immunofluorescence in this study.


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Species</th>
      <th>Dilution</th>
      <th>Catalog no.</th>
      <th>Vendor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BRA</td>
      <td>Goat</td>
      <td>1:400</td>
      <td>AF2085</td>
      <td>R and D Systems</td>
    </tr>
    <tr>
      <td>SOX2</td>
      <td>Rabbit</td>
      <td>1:200</td>
      <td>5024S</td>
      <td>Cell Signaling Technology</td>
    </tr>
    <tr>
      <td>NANOG</td>
      <td>Mouse</td>
      <td>1:400</td>
      <td>560482</td>
      <td>BD Biosciences</td>
    </tr>
    <tr>
      <td>SMAD2/3</td>
      <td>Mouse</td>
      <td>1:100</td>
      <td>610842</td>
      <td>BD Biosciences</td>
    </tr>
    <tr>
      <td>pSMAD1</td>
      <td>Rabbit</td>
      <td>1:100</td>
      <td>13820</td>
      <td>Cell Signaling Technology</td>
    </tr>
  </tbody>
</table>

### Replicates, sample sizes, and error bars

All experiments were performed at least twice. Data shown are from representative experiments, except for FRAP data, where data from multiple experiments are pooled because of the difficulty of performing FRAP on a sufficient number of cells in a given experiment. Error bars on single-cell data (SMAD4 signaling dynamics, pSMAD1, SMAD2/3, BRA, and HAND1 immunostainings) are standard error over cells. Full distributions are also provided to show cell-to-cell variability. Error bars on qRT-PCR data are over technical replicates due to the difficulty of quantitatively comparing biological replicates, likely owing to differences in culture densities, timing between seeding and ligand stimulation, and other culture variables, however, multiple biological replicates were performed in all cases. Error bars in micropatterning experiments are standard deviation over colonies. For single-cell imaging experiments, at least 600 cells were measured for each condition, for FRAP experiments at least 12 cells were measured for each condition, and for micropatterning experiments at least five colonies were analyzed for each condition.

### Supplemental information

Supplemental information includes four figures, three movies, and an Appendix on mathematical modeling.
