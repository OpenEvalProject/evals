# Peer review - Round 1

Editors:
- Adèle L Marston, University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59889.sa1](https://doi.org/10.7554/eLife.59889.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study examines the structure of budding yeast chromosomes in mitosis using the high resolution chromosome capture technique, Micro-C XL. By analysis of specific mutants, high quality datasets are presented to unequivocally show that yeast chromosomes are organised into loops that are defined by cohesin. A model is presented for cohesin-dependent loop formation.

Decision letter after peer review:

Thank you for submitting your article "Cohesin residency determines chromatin loop patterns" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Adèle L Marston as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript describes the generation and analysis of chromosome conformation changes in synchronised populations of budding yeast, S. cerevisiae, using a high-resolution method termed micro-C (an evolution of Hi-C) that was recently developed by one of the authors (Hsieh et al., 2015; Hsieh et al., 2016).

The authors describe a punctate interaction pattern that arises in metaphase-arrested cells, is dependent on the cohesin subunit Mcd1, and is altered upon depletion of the cohesin regulators Wpl1 and Pds5. The authors propose a modification of prior models of loop extrusion with barrier elements to interpret the microC patterns, specifically proposing that the stable binding of cohesin acts as a barrier to loop extrusion by dynamic cohesin.

The datasets themselves are informative, and will be of great use to the research community. It should be noted that some of the key findings were described in earlier work by Schalbetter et al., (2019) and (Dauban et al., 2020). The paper is technically impressive, the beautiful interaction patterns are compelling and the increased resolution of the micro-C both reinforces and extends conclusions from earlier work. However, there are a number of concerns related to how the analysis was done and how the findings are interpreted. The general perception of this manuscript would also be boosted by a small amount of additional analysis.

Essential revisions:

1) Though the data quality in the current study is unmatched, others have convincingly shown the presence of loops in budding yeast by Hi-C (Schalbetter et al., 2017, 2019; Dauban et al., 2020) and these studies need to be appropriately acknowledged throughout. Credit should be given to Dauban et al., 2020 for cohesin-dependent domains in G1, demonstrating cohesion-independent chromosome looping.

2) The authors must substantially rephrase and rewrite the text to avoid confusing the presence/absence of the punctate/grid-like focal interactions detected by Hi-C/micro-C with the presence/absence of "loops". The importance of this point cannot be overstated.

Critically, whilst it is correct to interpret focal matrix signals to represent the higher-order polymer interactions that can arise at loop bases, it is incorrect to infer that the lack of such focal interactions in a matrix indicates the lack of loops. Rather, the latter simply means that there are no "well-positioned" loops within the population of cells assayed.

Fundamentally, looped chromatin can be inferred from the relationship between the decay rate of interactions over distance (P(s)) without any explicit need to observe focal interactions-be this either because the dataset being studied lacks resolution to resolve such interactions (low-resolution HiC/binning, or low depth sequencing), or because loops may not arise at preferred locations (across the population). Indeed, prior mitotically-arrested yeast datasets were able to estimate both average loop length, and average loop number (per cell), despite the lower spatial resolution of the data analysed (Schalbetter et al., 2017).

3) A brief sentence subsection “Chromosome domains in mitosis” states that the boundaries of CAR domains are enriched at terminators (Figure 6—figure supplement 1C), where CARs are preferentially located. This point may be far from trivial. I indeed wonder whether the anchors of the loops presented in this paper overall correspond with terminators. A recent bioRxiv piece by the Cees Dekker and Uhlmann labs raises serious doubt as to whether yeast cohesin (in contrast to human cohesin) can in fact extrude loops. Yeast cohesin may still act as a topological anchor that when pushed along DNA enables the enlargement of a loop, but cohesin itself might not act as the motor. Of course the current manuscript does not need to fully address this point, but it would be relatively straightforward to assess whether the loop anchors genome-wide appear to correspond with terminators in general and/or with sites of convergent transcription in particular. Such an analysis could for sure add to the impact and the novelty of the current paper.

4) Do those CARs that act as boundaries then maybe correspond with convergent genes? If cohesin were pushed to these sites by transcription from two sides, this would also explain why these CARs have higher cohesin peaks by ChIP. It would be good to then also place these findings in the context of a recent paper by Paldi et al., on how convergent transcription shapes pericentromeres.

5) In Figure 2D, depletion of Mcd1 leads to the loss of focal loops. Yet, one can still observe domains. Also, here, it would be good to link these structures to the presence of genes. I would actually recommend that the authors throughout plot the genes above the matrices. A comparison of these domains with the Mcd1-independent domains observed in the previously published Micro-C work from asynchronous cells would also be useful here.

6) Figure 5—figure supplement 1: The plots in panels B and F suggest that loss of Wapl or Pds5 yields similar results, while e.g. panels A and E suggest that loss of these two factors yields very different results. Please explain.

7) The authors appear to conclude that it is non-random cohesin binding that defines the non-random location of loops (last sentence of Abstract for example). How do they exclude that it is not the non-random position of loops (generated by SMCs at their bases) that creates the non-random cohesin pattern?

8) Please specify in the text (for all experiments) for how long cells were arrested, and for the depletion experiments, how long after auxin was added were specific samples harvested? Have the authors confirmed depletion of AID-tagged proteins by western blotting in each experiment?

9) Critically, it is far from clear what genotypes and conditions are being compared. For example, is the wild type nocodazole sample also treated with auxin (as a control) when compared to the mcd1-AID, pds5-AID, and wpl1-AID mutants? Or are the AID strains processed {plus minus}auxin? Were durations of nocodazole arrest identical in the comparisons presented?

10) Please provide flow cytometry profiles to help demonstrate the homogeneity (or otherwise) of the samples/timepoints being analysed for each dataset in every figure. This is relevant for all data samples – especially when auxin may have been added for an unspecified time after the initial nocodazole arrest. Moreover, this is especially important for the S-phase timecourse presented in Figure 4. For these experiments, please explain why t = 0 minutes is not included as the starting state.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Cohesin residency determines chromatin loop patterns" for further consideration by eLife. Your revised article has been evaluated by Jessica Tyler (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Although it is now clearer what had been shown in previous studies and how the current study advances the field, there are still instances where more context is required and there are some points that need revision to improve clarity.

Subsection “Micro-C XL reveals prevalent chromatin loops with a defined position in mitotic chromosomes”: The sentence should read "The pervasive presence of positions loops shown…."

Subsection “Micro-C XL reveals prevalent chromatin loops with a defined position in mitotic chromosomes”: "These positioned loops were mostly absent in contact maps using datasets from previously published Hi-C maps of mitotic cells (Figure 1C, bottom rows; Figure 1—figure supplement 1A)". This is not completely accurate – though there is no doubt that the Micro-C XL offers improved resolution, the positioned loops can be seen in the Schalbetter et al., data and are clearly present in the Paldi, 2020 data, just less distinct. This statement should be revised to "" These positioned loops were less obvious in contact maps using datasets from previously published Hi-C maps of mitotic cells (Figure 1C, bottom rows; Figure 1—figure supplement 1A)".

Subsection “Cohesin complex mediates loop formation”. As a general comment about the role of cohesin in loop formation in budding yeast, this should include a reference to Schalbetter, 2019. "To assess if cohesin was also needed for the formation of positioned loops in budding yeast…". The yeast meiotic observations (referenced in the Introduction) clearly demonstrate cohesin-dependence for loop positioning in yeast. To avoid confusion, it is suggested to write "whilst cohesin-dependent positioned loops have been clearly demonstrated in yeast meiosis, whether or not the same is true in mitotically-dividing yeast cells is unclear."

Subsection “Cohesin complex mediates loop formation”. These two paragraphs confirm conclusions already reported by others and this should be made clear. Schalbetter et al., 2017 already demonstrated that looping was mostly cohesin rather than condensin-dependent – this was the main conclusion of that study. Similarly, this point is confirmed in Daubain et al., 2020. Please preface these two paragraphs as confirming the previous findings in these studies, rather than presenting this as a new finding.

Subsection “Cohesin complex mediates loop formation”. A comparison to the meiotic result would provide better context and make it clear that this general concept has already been clearly demonstrated in the same organism albeit under different growth conditions. e.g. "Thus, we conclude, as in yeast meiosis (Schalbetter, 2019), that cohesin is required for positioned loop formation genome wide.".

Figure 2B. What are the units of the scale bar in B? How is this calculated? Is it a ratio? Is it a linear scale? Please specify in the legend.

Figure 2—figure supplement 2 and subsection “Cohesin complex mediates loop formation”. The main conclusion from this figure is that the increased resolution of the microC-XL allows the authors to draw the conclusion that the short distance interactions are also dependent on cohesin. Otherwise the datasets broadly similar and this point should be explicitly stated.

Subsection “Cohesin complex mediates loop formation”. It is not clear why this sentence was changed from the original. The revised text is now incorrect. Whilst it is true that cohesin is responsible for chromosome individualisation, cohesin activity leads to a *reduction* in interchromosomal contacts.

Subsection “Cohesin and condensin shape the rDNA locus in mitosis”: should be a single sentence "……(Guacci et al., 1994), while…" Also, please remove the comma within the text: "…loci (RDN37 and RDN5), spaced by two non-transcribed regions (NTS1 and NTS2)."

Subsection “Cohesin and condensin shape the rDNA locus in mitosis”: Schalbetter et al., 2017 also looked at the rDNA by Hi-C in the absence of cohesin and condensin with similar conclusions and should be cited here.

Subsection “Cohesin organizes chromosomal loops genome-wide”. For clarity, it is important to make it clear that the analysis of inter-anchor distances described here is only considering adjacent (+1) distances.

Subsection “Cohesin organizes chromosomal loops genome-wide” "While we detected…". As written, this sentence doesn't make sense grammatically. Please clarify what is meant.

Subsection “Cohesin organizes chromosomal loops genome-wide”. Without a direct test of causality, "confirming" is an overstatement. Please revise to "suggesting", or "supporting a model where.".

Subsection “Chromosome loops form during S-phase”. Please explain int the main text why two different temperatures were performed. The data are nice, but it is entirely unclear what conclusion the reader is expected to draw from the two-temperatures without further guidance.

Subsection “Chromosome loops form during S-phase”. "wild type cells" is stated, but do the authors mean 'wild-type cells arrested at mitosis with nocodazole'?

Subsection “Chromosome loops form during S-phase”. An alternative explanation is that there could be an increase in cohesin occupancy on chromosomes in mitotic arrested cells?

Subsection “Chromosome loops form during S-phase”: To make clear that this is speculation: "Loop extrusion may be mediated by a different pool of cohesin that is activated later in S phase.

Subsection “Cohesin regulators affect the size and location of chromosomal loops”. To improve readability, please add commas around the central clause as indicated here: "This paradox can be explained if Wpl1p, by dissociating randomly bound cohesin from chromosomes, allows efficient accumulation of cohesin at CARs (Bloom et al., 2018; Rolef Ben-Shahar et al., 2008)."

Subsection “Cohesin regulators affect the size and location of chromosomal loops”. What is the analysis that lead to the conclusion that the amount of cohesin detected at CARs was reduced 50%. The ChIP-seq data themselves are not calibrated. If analysis has not been done to determine this point, please revise the text accordingly. This also applies to the description for the data in pds5 mutant.

Subsection “Chromosome domains in mitosis”. To aid the reader, please provide a reference to Figure 7—figure supplement 1A here. However…the presented figure does not allow the reader to reach the conclusion that: "A visual inspection pointed out that most cohesin-depleted domains have a roughly similar boundary distribution to the ones detected in asynchronous cell populations." The few patterns that can be seen at this scale scale look to be quite different when comparing the mcd1-AID to the asynchronous Hsieh dataset.

Subsection “Chromosome domains in mitosis”. Where do these numbers come from? Is there a relevant graph that has been omitted?

Subsection “Chromosome domains in mitosis”. The authors should be wary of their conclusions drawn in this analysis. It is very likely that the domains detected by the algorithms in the wild type are almost entirely driven by the loop signals at the apex (and edge). (e.g. look at the patterns of signal enrichment in Figure 7B for wild type). Thus, obviously, if loops disappear, so will the ability to detect these domains bioinformatically.

Discussion section. Since this point has already clearly been demonstrated for preferred Rec8 sites in meiosis, Schalbetter, 2019 should be both mentioned and referenced here to avoid overstating the novelty of the findings.

Discussion section. Similarly, this finding was also demonstrated, clearly, by the meiotic yeast data, and thus should be described and cited.

Discussion section: As above, the conclusion that cohesin defines the loops is not entirely novel and previous work showing this should be cited here.

Discussion section. The model that is described is entirely congruent with the finding of the simulations employed by Schalbetter, 2019, which employed a stochastic model of loop expansion driven by extruders that could be blocked by barriers at preferred cohesin-binding sites (Rec8 in this case). As such, it would be entirely relevant to mention the congruence of the author's data (and model) with the findings of the polymer simulations developed by others.
