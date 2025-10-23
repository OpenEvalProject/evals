# Peer review - Round 1

Editors:
- Kevin J Verstrepen, VIB-KU Leuven Center for Microbiology Belgium

Reviewers:
- Hans Steenackers

## Review text

DOI: [10.7554/eLife.47951.026](https://doi.org/10.7554/eLife.47951.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Emergence of metabolic landscapes in yeast monolayer colonies" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

We appreciate how your study uses a microfluidics setup to study the behavior of S. cerevisiae in a glucose gradient. The combination of this setup with GFP tagged version of hexose transporters, a glucose sensitive transcription factor (MIG1), and other reporters of metabolic state (PDC1, SHD2) allows studying spatial patterning as a function of glucose availability. The results show that patterns of expression of hexose transporters with different affinities are spatially arranged in a manner consist with a gradient of glucose availability with highest amounts of glucose available near the "source" (i.e. periphery of the artificial colony), and lowest levels near the "sink" (i.e. center of the artificial colony). Perhaps more interestingly, interpretation of the data suggests a relatively sharp transition in the colony between zones of growth and slow/no-growth, which they ascribe to zones of fermentative and aerobic metabolism.

Overall, the reviewers agree that this is a particularly elegant study. As you can see in the individual reports (below), reviewer 1 is significantly more positive than reviewers 2 and 3. However, after discussing the individual reviews, all reviewers question the amount of novel biological insight that is presented in your paper.

As such, I am afraid that we are not able to offer publication in eLife (unless of course you believe that we missed the major message and its biological relevance). On the other hand, everyone also agrees that the experiments and results are beautiful, and that the setup may be usable for other studies. As such, we wonder whether it would be conceivable to re-write your paper as a "Tools and resources" paper? If so, you would need to emphasize the design and operation of the system, detail its use for a broad range of studies and compare it to other, existing systems such as the ones describes by Hornung et al., 2018, and Wilmoth et al., 2018. The Hornung et al. paper in particular seems to use a rather similar setup…

Reviewer #1:

The authors applied a microfluidic device to study how long-range metabolic interactions influence the internal structure of simple yeast cell monolayers asymmetrically exposed to an external nutrient source. They showed spatial variation in nutrient levels, cellular growth, and expression of several metabolic genes to self-emerge. Notably, the gene expression landscapes exhibited a high degree of spatial correlation over different levels of external nutrient level and were indicative of a clear spatial transition between fermentative and respirative growth.

I really enjoyed reading this work. Although the experimental set-up is simple and the conclusions intuitive and straightforward, the depth of the analyses and the clarity of the interpretations are impressive. The authors combined growth measurements, single cell tracking, fluorescence based expression analysis with FACS and microscopy and advanced data representation to study spatial relations between nutrients, growth and metabolism with an unprecedented level of detail. This work will therefore undoubtedly provide inspiration to many other researchers interested in spatial heterogeneity of microbial communities. I therefore recommend publication in eLife.

Reviewer #2:

Marinkovic et al. address single-cell response to glucose gradients within structured communities. They present an intriguing method to look at metabolic landscapes in a microbial community. However, I do believe the novelty of the results need to be clarified significantly better, and the conclusions drawn must be discussed more critically. Alternatively, the work may be more suitable for a methods focused publication, as using the gene expression of the transporters to gauge the extracellular concentration of glucose within a colony is an interesting tool.

Major concerns:

A) The glucose gradients emerge in the end artificially, due to the design of the microfluidic chamber and due to the fact the yeast's consume glucose, and not due to community action. The method of the author's pictures of how the cells respond to different glucose availability as a function of glucose concentration in different areas of the closed channels. But the effects are the same if one cultivates the cells in batch cultures, and tunes glucose availability in this way. One does hence not learn anything about yeast communities, only, that yeast in batch culture and in a microfluidic chamber respond similarly to glucose depletion. Hence, is there anything new in the study, other than nicely illustrating the well-established fact that yeast activates different glucose transporter at different glucose concentration?

B) Batch cultures are used to tune gene expression sensors. But, in batch culture, glucose is constantly and rapidly depleted, while gene expression, needs some time to adjust. At any given time, in batch culture, the glucose concentration in the media, and the gene expression programme, are hence asynchronous (i.e. gene expression lags behind the glucose concentration). Chemostat experiments would be needed, to have a glucose concentration that corresponds to the gene expression programme at a particular point in time.

Method:

Figure 1: I have not found the mention of the exact number of dead-end chambers within one microfluidic chip (I'm guessing 16 from the figures?). However, looking at the n in different experiments (e.g. Figure 1, n=12, n>5 and n=9) I am wondering in how many separate experiments these were done, and how much of the collected data was discarded and for which reasons?

Was it excluded that nutrient concentrations from the previous chamber affected the later ones? Especially in the stages when the chambers were already filling up/cells were being carried away?

Results and Conclusion:

Subsection “Cellular metabolic activity creates gene expression landscapes”: "Both patterns demonstrate the formation and maintenance of a glucose gradient that emerges from cellular metabolic activity." The pattern of the gene expression demonstrates that the cells adapt to the glucose gradient that emerges through supply of fresh media from only one side. "Formation and maintenance by cellular metabolic activity" in the sense that, yes, the cells close to the opening do import the glucose they require seems a weak point to make. In other words, there is evidence for the contrary – there seems no different action of cells in the community as in the batch culture, when it comes to the expression of the transporters.

Discussion paragraph four: What is the dependence/independence of the different gene expression looked at here? Can we talk about synchronicity between networks if the studied genes are known to dependent on the same external factor?

Figure 6: Landscapes of gene expression is not shown at all glucose concentrations for all genes, why?

Reviewer #3:

This manuscript details the results of a study using a microfluidic system to study growth and gene regulation in monolayers of yeast cells. This system is presented as a tractable model for studying pattern formation in microbial colonies, via spatial and temporal measurement of cell division rates and measurement of gene expression via fluorescently tagged reporters.

The authors use this experimental setup, in combination with GFP tagged version of hexose transporters, a glucose sensitive transcription factor (MIG1), and other reporters of metabolic state (PDC1, SHD2) to study spatial patterning as a function of glucose availability.

Unsurprisingly, they find that patterns of expression of hexose transporters with different affinities are spatially arranged in a manner consist with a gradient of glucose availability with highest amounts of glucose available near the "source" (i.e. periphery of the artificial colony), and lowest levels near the "sink" (i.e. center of the artificial colony). Perhaps more interestingly, their interpretation of their data suggest a relatively sharp transition in the colony between zones of growth and slow/no-growth, which they ascribe to zones of fermentive and aerobic metabolism.

While I appreciate the elegance of the microfluidic colony model that is presented, the key findings are rather modest -- i.e. there are gradients of nutrient availability in microbial colonies. This doesn't really have the impact I expect from eLife papers.

Below I detail a number of concerns/comments about the study, the analyses, and whether the authors have adequate related their work to the larger literature in this area.

Detailed comments:

1) Several other recent papers (Hornung et al., 2018,; Wilmoth et al., 2018) have used microfluidic setups to study microbial colonies. The Hornung et al. paper is the most similar to the current experimental design.

2) If goal was to measure the rate of glucose uptake and availability it seems like there may be other more direct approaches than inferring this from hexose transporter expression, such as the use of 2-NBDG, a non-metabolizable, fluorescent glucose analog (Roy et al. 2015, doi: 10.1371/journal.pone.0121985).

3) The following paper, while not at the fine spatial scale provided by the microfluidics, presents a more complete and compelling view of metabolic differentiation in yeast colonies: Maršíková et al., 2017.

4) The spatial analyses focus primarily on peaks of maximum expression, but the data is potentially much richer and more interesting if the authors consider not only the global maxima but more complex spatial patterns. For example, in Figure 4B MIG1 nuclear localization appears to be multimodal. What is going on here?

5) There is very little effort to contextualize this work in the larger body of studies of yeast colony structure, physiology, or regulation of glucose responsive TFs. Illustrative of this, there are only three citations total in the entire discussion. There is only a single reference to the regulation of hexose transporters in the entire manuscript. Specific examples:

- Subsection “Cellular metabolic activity creates gene expression landscapes”: " HXT1 is a low-affinity glucose transporter mainly expressed under high-glucose conditions, while HXT7 is a high-affinity glucose transporter expressed under low-glucose conditions only" Citations?

- Subsection “Gene expression landscapes depend on the glucose source concentration”: "As HXT1 is mainly expressed under high-glucose conditions (> 1% w/vol glucose) in batch culture…" Citation?

- Subsection “Gene expression landscapes of other genes and transcription factor activity confirm the inferred glucose gradients”: "MIG1 is a key transcription factor involved in glucose repression that localizes to the nucleus in the presence of glucose, to repress genes that participate in parallel carbon metabolic pathways (e.g., galactose)." Citation?

- and in the same subsection: "…we examined the expression of PDC1 and SDH2, which are overexpressed in fermenting and respiring cells, respectively" Citation?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "A microfluidic device for inferring metabolic landscapes in yeast monolayer colonies" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior Editor), a Reviewing Editor, and three reviewers.

We really appreciate the efforts of re-writing this manuscript as a "resource" paper. We feel that the paper has been much improved, but there are some remaining issues that need to be addressed through textual changes before acceptance, as outlined below:

1) We ask that the authors make it clear to the reader that what they call a "community action" does not imply that cells are responding differently in the community than they would as single cells in planktonic growth. The observed effects (gradients and response to these gradients) are merely the consequence of a high concentration of more or less static cells. So, perhaps calling it "population effect" would be more appropriate?

2) We would appreciate if you could insert a succinct discussion of the difference between a batch culture and this steady-state (where in principle, the cells could be better adapted as they are not always "running behind" in their response to a variable environment, as they would be in batch). (see reviewer 2's comments below for more details)

3) We again ask to include more references and to not overstate the advantage of the presented device (see reviewer 3's comment below).

4) Please provide more details about the reproducibility/variability and statistics of the results and analyses.

The above points summarize what we believe to be essential changes, and we only ask for textual changes instead of further experiments. We are including the full reviews for your reference below.

Reviewer #1:

In this revised manuscript, the authors – as requested- presented their work as a tool that can be generally applied to quantitatively and dynamically study growth landscapes, metabolic landscapes and gene expression landscapes within extended monolayers of cells. They extensively elaborated on the similarities and differences of their approach compared to other studies that applied agar colony models or microfluidics devices to study spatiotemporal patterns in colonies, and clearly pinpointed advantages of their approach. A figure was added to clarify the experimental set-up. Also my other (minor) comments were addressed to a sufficient extent. I therefore recommend publication.

Reviewer #2:

Although the authors have put efforts in their revision, they have not addressed my two main points. I'm hence wondering if I have not expressed myself clearly enough, so it's perhaps my own fault – or it also could be a different use of language between disciplines, so that the authors did simply not understand my questions. Long story short, I don't want to sound negative as it may be my own use of language, but the revision has not addressed the two simple concerns I had. Perhaps the other reviewers could comment if they agree or disagree with me, I'm happy if my comments are ignored, in case my concerns are not shared.

I think both points still are relevant, though. The first one could be fixed simply in writing. 'Community action' implies to me, and I guess to many others in the field, that there are interactions between the cells that emerge in the community – implying that cells would behave differently in the community as if they are not in the community. When it comes to glucose consumption, this seems not to be the case – there seems nothing which indicates that the individual cell's glucose import would be depending on interaction terms between the cells. The manuscript is written as if glucose gradients would emerge because of 'community action', but in fact, they emerge from cells that consume the glucose, in a way that does not require a different action as if cells would act independently to one another. In other words, the cells deplete the glucose in the MF channels, and within the channel, this creates a gradient, to which the cells respond. This alone does not indicate that cells act differently in the community. as they would act in Isolation.

The second point may remain relevant, however. The sensors are tuned in batch culture. But in batch culture, one expects a time differential, between the glucose concentration present at a point in time, and the average gene expression program activated at that same moment (as gene expression needs time to adjust, but glucose is constantly depleted. I.e. if gene expression needs 30mins to adjust to a changed glucose concentration, the gene expression program reflects the glucose concentration that was in the batch 30mins earlier before the timepoint was taken). I had suggested the authors to control this in chemostats, where gene expression and concentration are a time-wise aligned. I agree this would have been time-consuming to do and could hence be difficult for the authors to do. But it would have been great if they could have come up at least with some idea, and quantify how big this effect is; One would assume the differential between glucose concentration and gene expression are strongest in the early and late exponential phase. If chemostats are too difficult, one could suggest also much simpler surrogate experiment, for instance. One could, for instance, re-supplement exhausted media with glucose, perform a time-course, and estimate in this way the time needed until the gene expression has re-adjusted to the supplied glucose level. The sensor data would need to be adjusted by the time differential.

Reviewer #3:

This revised manuscript has been appropriately rewritten as a "Tools and Resource" article.

1) The authors overstate the uniqueness of their approach. For example, in the Introduction in reference to previous studies using similar microfluidics designs:

" While the use of microfluidics gave rise to the discovery of interesting collective properties of microbial assemblies, such attempts were too specific and had to deal with some of the limitations like small device dimensions (<100 100 μm), use of low nutrient concentrations (<1 mM), limited scope of nutrient types, inability to access single cell level – and therefore cannot be transposed to the general case of the study of a large monolayer of cells in standard range and scope of nutrients employed in biological research."

Few of these critiques hold up. For example, low nutrient concentrations and limited scope of nutrient types are simply specifics factors applied to the different organisms study. This critique applies equally to the system presented here. Furthermore, the Hornung et al. article certainly allows access to the single cell level. The text should be revised to reflect a more accurate summary of this earlier related work.

2) The rebuttal states "We agree that more contextualization was necessary so we expanded our Introduction and Discussion part, as well as provided additional citations, including all the ones proposed by the reviewer" I can find no references our discussion of prior literature at the line numbers provided.

3) One of the points the authors make several times regards the reproducibility of their assays. For example: "We demonstrate a novel capacity to reproduce and

quantify…" and "…we found the growth pattern was highly reproducible across parallel chambers.." However in the eLife "transparent reporting form" the authors state "We did not use statistical inference or comparison between data sets." How then did the authors estimate reproducibility/repeatability?
