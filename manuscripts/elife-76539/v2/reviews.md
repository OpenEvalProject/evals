# Peer review - Round 1

Editors:
- Jeremy J Day, https://ror.org/008s83205 University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76539.sa0](https://doi.org/10.7554/eLife.76539.sa0)

Neurons use activity-responsive gene programs to shape cell-specific identity and respond appropriately to environmental stimuli. By combining elegant protein degradation and cell-specific knockout approaches with transcriptional profiling and chromatin structure analysis, this manuscript delineates the contributions of cohesin (a key protein responsible for genome structure and organization), in developmental and activity-dependent gene expression programs as well as chromatin reorganization. These results demonstrate that cohesin is required for the full expression of key genes required for the maturation and activation of cortical excitatory neurons, and reveal a tight correlation between cohesin effects and the genomic distance of higher-order chromatin loops.


---

# Peer review - Round 1

Editors:
- Jeremy J Day, https://ror.org/008s83205 University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76539.sa1](https://doi.org/10.7554/eLife.76539.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Reliance of neuronal gene expression on cohesin scales with chromatin loop length" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All reviewers agreed that there is somewhat of a disconnect between effects of Rad21 depletion on activity-dependent gene expression and activity-dependent loop formation. While the manuscript presents some solid evidence that Rad21 contributes to SRG expression, it was not clear that this was due to prevention of new loops formed after stimulation, as the authors only report effects at constitutive loops. The manuscript would benefit from a more systematic comparison of the effects of RAD21 on inducible vs. constitutive loops, similar to the analysis that was performed with inducible vs. constitutive genes.

2) The conceptual framing of the manuscript could be improved by focusing more on developmental aspects of Rad21 depletion in neurons, and less on activity-dependent aspects. Given that many of the effects reported here at SRGs alter both basal and inducible gene expression, and the strong constitutive role for Rad21 in maintenance of chromatin architecture in neurons, this reframing would be a better fit for the results presented here.

3) The manuscript should include more thorough discussion to place the present work in context with prior work, as outlined in the individual reviews provided below.

4) A revised manuscript should address the individual concerns raised by reviewers to specify which gene sets are used for different analyses, clarify the terms IEG and SRG as used in the manuscript, and provide further analysis on the contribution of loop length to Rad21 effects.

Reviewer #1 (Recommendations for the authors):

1. Figure 5 convincingly shows that genes that are downregulated in RAD21 depleted neurons have longer HiC loop length, for both activity regulated genes and constitutive neuronal genes. However, in order to conclude that RAD21 effects on chromatin looping "scales with the genomic distance traversed by their chromatin contacts", it would seem to be necessary to conduct a more detailed analysis showing that the effects of RAD21 depletion directly correlate with the genomic distance of HiC contacts. By binning HiC lengths and showing average effects of RAD21 depletion on mRNA by bin classes (e.g,. 0-50, 50-100, 100-500, 500+kb loop lengths), it may be possible to address this question. As it stands, we only know that RAD21 downregulated genes tend to have lengthier loops, not that RAD21 effects scale with chromatin loop lengths.

2. The incorporation of 5C to show the lack of effect for RAD21 depletion on Fos enhancer-promoter looping (Figure 6) is encouraging and confirms the overall model of cohesin-dependent gene expression. However, the observations at Bdnf (a defined SRG, Supp. Figure 11) resemble those at Fos – only constitutive loops are lost following RAD21 depletion, with variable effects on gene basal levels and inducibility. Were the authors able to specifically examine activity-dependent loops that are formed involving SRGs as a result of stimulation? It does not appear that 5C at a more delayed timepoint (e.g. after 6hr of KCl stimulation) was conducted. This would have provided an opportunity to examine the stimulus-dependent loops formed at the Bdnf locus, previously identified by Beagan, et al., (PMID: 32451484). Either way, the manuscript could be improved by addition of the Bdnf figure (Supp. Figure 11) as a main figure in the text.

3. Prior work demonstrates that AP1 transcription factors serve as a key regulator of stimulus-activated enhancers in cortical neurons (PMID: 25195102). Similarly, evidence from ATAC-seq experiments suggests that IEG enhancers are already fully accessible prior to stimulation (PMID: 32810208). In contrast, AP1 members that comprise part of the IEG program are thought to serve as pioneer transcription factors (in combination with cell-selective TFs) to open chromatin at SRG enhancers. This manuscript would benefit from a more systematic comparison of the effects of RAD21 on inducible vs. constitutive loops, similar to the analysis that was performed with inducible vs. constitutive genes.

4. Many constitutive neuronal genes are also long genes, and these may be more likely to be disrupted after RAD21 depletion and resulting changes in genome structure and organization. This manuscript should include a supplementary analysis to determine whether RAD21 effects scale with gene length itself, in addition to chromatin loop length.

Reviewer #2 (Recommendations for the authors):

I feel that a revised version of the paper should address my comments listed here:

There should be a discussion on whether cohesin dependence is scaling with loop length in other cell types as well. For example, the Cuartero et al., 2018 study by some of the same authors, using approaches similar to the ones presented here in immune cells, and may be good dataset to compare with their findings in neurons.

Based on Figure 4a, only a tiny fraction of transcribed genes are immediate early genes IEGs (N=18) and only N=107 genes are secondary response genes. To me, it is not entirely clear how the Authors arrived at these numbers. The number of activity regulated genes should be in the several hundreds, based on the literature (including the Kim et al., 2010 paper that the Authors cite). In any case, one wonders what type of conclusion can be drawn from such a small set of N-18 IEG genes.

The Authors , if I understood correctly, probed multiple genomic loci with 5C, but specific information on the sequences and loci probed is hard to find in the paper. From reading the paper, it is clear that c-Fos and BDNF and Arc gene loci (Figures S9-11) were probed with 5C. Please be more specific on the area of genome interrogated with 5C.

The sensitivity of chromosome conformation capture techniques to detect loops and contacts declines with increasing linear genome distance between the anchors. There should be a discussion and if necessary, a control experiment (I believe in silico may suffice) whether or not the reported cohesion- sensitivity of longer range chromatin loopings could be reflective of the overall lower baseline signal of longer range chromosomal loopings. If so, this would be a significant confound for the Authors conclusion of cohesion dependence scaling with loop length.

Reviewer #3 (Recommendations for the authors):

My questions about the study fall in two parts.

First, I am left wondering about the significance of the observations and the way they are presented. The relationship between Rad21 dependence and longer loop length is supported by the data, but I struggled to understand what that might mean. Is there anything else the authors can add about why this might be the case? Is this special in neurons and other postmitotic cells and if so what might that mean? More importantly, the authors include a paragraph in the discussion about how promoter-enhancer interactions might work independent of cohesin, which is interesting, and perhaps it is a major finding of the study that those enhancers do not require Rad21. If this is the most important finding then the fact that this study reaches a different conclusion that Yamada 2019 needs to be directly addressed. That study also knocked out Rad21 in postmitotic neurons (CGNs) but did report disruption of promoter-enhancer loops and activity-induced gene expression. These data may well be stronger than those, but the authors should directly address the differences in the findings.

Second, given that the authors find the expression of many ion channels and synaptic proteins impacted by the loss of Rad21, they need to consider that any changes they see in impaired induction of activity-regulated genes – such as the reduced activation of Bdnf IV in Suppl Figure 11 – may arise from impaired intracellular signaling rather than a specific effect of Rad21 on the architecture of the Bdnf gene. Controls for the activation of signaling cascades and transcription factors could be added to address this concern. The demonstration that much of the effect of Rad21 knockout on activity-regulated genes is their reduction at baseline is certainly consistent with this idea of reduced synaptic drive to these genes, which is ongoing in cultures. KCl addition may largely overcome those deficits by providing such a strong drive through LVGCCs.

A few other questions:

1) When the authors refer to "activity-regulated genes" for example in Figure 2C, do they include only genes induced by neuronal activity or also those repressed by neuronal activity? This distinction is important because the meaning of those genes begin "Up" or "Down" in the Rad21 cKO is very different depending on the sign of their response to neuronal stimulation. This should be explicitly stated.

2) The data in Figure 3a on the distribution of different cell types in the cortex of Rad21 cKO mice is entirely anecdotal as presented. If the data are to be included they should be quantified and analyzed with appropriate statistics.

3) The terms IEG and SRG for the ARG classes are used here in a way that is not consistent with the literature. The division between the terms as the authors use them here seems to be time (IEGs early and SRGs late) whereas in the past the terms had more to do with mechanism – IEGs did not require stimulus-induced protein synthesis before they could be turned on whereas SRGs did. (Basically cycloheximide does not block IEG induction but it does block SRG induction). The Tyssowski paper referenced by the authors uses the language PRG for primary response genes that do not require protein synthesis for their induction, and then divide them into early and delayed PRGs for the reflection of time. BDNF is a delayed PRG and following the stimuli used here it does not require protein synthesis for its induction. The authors may want to consider clarifying their use of their terms depending on whether time or mechanism of transcription is their main focus to match other literature.

4) There is a paper from Kim Nasmyth's lab that knocked out Rad21 in postmitotic neurons of the fly with relatively severe phenotypes. By contrast at least the morphological phenotypes in the images in Suppl Figure 4 seem quite mild. This might be an important point of discussion if it is the case that the consequences of Rad21 function are different by species?

5) It is a little surprising that all the data from the final paragraphs on activity-regulated genes are in the supplementary figures. This points to evidence that the authors do not consider these to be the most important of their findings, which is slightly out of balance with the attention paid to activity-dependent genes in the text. Perhaps a rewrite of the paper would make the significance of the findings more obvious.
