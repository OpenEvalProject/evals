# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53638.sa1](https://doi.org/10.7554/eLife.53638.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Ordered patterning of the sensory system is susceptible to stochastic features of gene expression" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

Generally, the reviewers agreed this is a very interesting paper dealing with a very important topic. As you will see below, reviewer #1 and #3 only request a number of editorial changes which are important and straight-forward to implement.

Reviewer #2 has been much more critical, raising a total of nine points. In ensuing discussions, reviewer #1 and #3 have looked over these nine points and engaged with reviewer #2 in discussions about what exactly should be done in regard to these nine points. Here are the conclusions that we hope you can all address. The numbering matches the numbering of reviewer #2:

1) Transcript counting: We do not request that you do mRNA measurements. However, please do discuss either the Result or Discussion considerations about mRNA vs protein measurements. One reviewer notes that there is an extensive literature of using protein measurements coupled with modeling to deduce transcriptional bursting parameters and, from one reviewer's perspective, when mRNA FISH and MS2 measurements when subsequently done on systems that had previously had only protein reporter measurements, the RNA data on the whole supported what was deduced from protein reporter measurements.

2) Automated cell ID approach: All reviewers agree that you need to provide a validation of your automated cell ID system comparing manual and automated scoring.

3) Indeed, please explain the total molecule counts between these two experiments (Figure 2). If the dual reporter is not double the single reporter, the authors should provide an explanation. Biologically, I think this is a very important point for their system and should be addressed clearly and directly.

4) Indeed, please explain the quantitative differences between the data and their model.

5) The authors argue that Sens levels are the same at site 22A3 and 57F5: This is not clear. The levels look quite different. This is critical for many of the authors' conclusions, especially that the phenotypic differences are a result of noise, not levels. The authors must provide a compelling quantitative argument that these levels are the same.

6) The HiC data should be moved to the Supplement.

7/8) No experimentation required. Reviewer #1 and reviewer #3 – and then eventually also reviewer #2 – agreed that the most important thing is here is a clarification of the limitations of the assay. Please add sentences to address the ectopic reporter and correlation concerns.

9) Please address the point raised by reviewer #2.

Again, as stated, above those are the nine points raised by reviewer #2. Please also address the points raised by reviewer #1 and reviewer #3.

Reviewer #1:

This is an interesting and technically accomplished study from the Carthew lab. The paper shows, using protein count estimates in live embryos, that transcriptional bursts can have an effect on protein level biology, that expression noise can be sensitive to chromosome position (even in contexts where the protein is effectively functional. The study then shows that somatic pairing effects can affect protein noise, but these effects depend again on the genome context. Finally the paper shows how an enhanced level of noise can affect the lateral inhibition process. My main critique about the paper is related more to the way it is presented:

"We contribute to this effort by providing the first study on the impact of stochastic expression in a developmental process involving complex cell-cell signaling. "

This is overstated, there are several other examples where this issue has been directly addressed in embryos, for example, Raj et al., 2010 and Lagha et al. Cell. 2013 153:976-87. In any kind of tissue, there is complex cell-cell signalling, even in an otherwise cell-autonomous specification system (which you could argue the bristles are, at least from the perspective of initiating the decision)

"However, the process of cell differentiation frequently begins with a fate-determining protein expressed transiently at low levels, and expression then either greatly increases or decreases, corresponding to divergent fate adoption".

I think this may also be misleading, especially in developmental contexts. Accurate quantitation in the cells making the decisions is comparatively rare. I know there is the urban myth that TFs are low abundance, but there are many contradictory examples. Please feel free to cite something that proves me wrong.

I'm not sure about Figures 1D and 1E. It may just be the language used, but why would deterministic gene expression follow a single line, is it even useful to make this distinction here. 1E looks more like an Elowitz intrinsic vs. extrinsic noise plot. It is just confusing to change the language, unless this is adequately justified, and there is little in the text around these figures to justify this. The language becomes easier later on, when dealing with the Fano factor.

Subsection “Counting Sens Proteins to Measure Expression Noise”- in the double labeled line, is the fly still mutant for the endogenous sens allele? Please make this clear to the reader.

Figure 2: measuring the technical contribution using the double tag, does this involve a number of assumptions such as equivalence in turnover times, folding times etc.? Or by technical, do you just mean any removing any non-linearity in microscope detection? These things should be more openly discussed.

Figure 3: this is an unusual formulation for the burst frequency. It is usually expressed as just the kon, or kon.τ, where τis the RNA lifetime. Please justify this. Does this matter in your later inferences, for example, subsection “Sens Protein Noise Displays a Signature Arising from Transcription Bursts”.

Discussion paragraph two. I think the implied argument that pairing is important in humans should be softened. Somatic pairing effects may have been picked up, but this is far from mainstream. The standard view is more along the lines of stochastic repositioning of chromosomes with respect to each other and nuclear compartments each cell division. Yes, there may be opportunistic interactions forming between accidentally opposed loci, but I would avoid making too much of these anecdotal papers on pairing in mammalian cells (which were all before the large scale expansion in field using current methods of studying chromosome organization).

References to Nanog should probably be removed. in vivo, Nanog does not fluctuate much. It turns on, stays on for a couple of days, then turns off (Hadjantonakis lab). Most of the culture studies also see very slow fluctuations (6-7 cell divisions before a high cell will revert to the mean) which is longer than the gene is on in vivo.

Reviewer #2:

In this paper, the authors investigated how noise in the expression of the transcription factor Sens affects sensory bristle patterning of the fly wing. They generated tagged sens BAC transgenes labeled with scGFP or mCherry. They evaluated noise from these two alleles inserted into the 22A3 insert site. Since these transgenes are translational fusions that include the Sens protein, the noise could arise from transcription and/or translation. They examine expression when miRNA binding sites are knocked out, and find that noise increased as predicted if the main source of noise was transcription. They then examine expression at the 57F6. They find similar noise if there is a single copy at 57F6 and a single copy at 22A3. However, they find a different noise pattern if there are two copies at 57F6, which they argue is evidence that allele pairing and transvection generates noise at this locus. They then examine expression in the wing and argue that the levels are similar between transgenes inserted at 22A3 and 57F6, but the noise is different. Flies with two copies of 57F6 have wing phenotypes and the authors argue that this is due to the change in noise.

This is a very interesting topic. However, there are many technical and conceptual issues with the paper.

Major Comments

1) Translational fusion reporter genes complicate the conclusion that transcription is the source of noise: It is not clear why the authors examined protein noise. This complicates the system greatly (see points below), as they are looking downstream of transcription. The authors should examine transcription directly by conducting either 1. RNA FISH on GFP and cherry and evaluating variability in their experimental conditions, and/or 2. Generate transcriptional reporters and examine expression.

2) The authors have not validated their automated cell ID approach: The efficiency and accuracy of the automated system is not reported. The authors should validate the cell IDs manually and report the accuracy including the percentage of false positives and false negatives.

3) The dual tag experiment in Figure 2B should have twice as many molecules of GFP and mCherry as in Figure 2A. The authors compare singly tagged GFP and mCherry reporters to doubly tagged reporters. Their results suggest that the total number of molecules is equivalent (Compare Figure 2B to 2A). However, the number of molecules for the double tag should be double that of the singly tagged reporters. This result suggests that there are major issues with the cell ID, expression quantification, and/or analysis. Alternatively, these results could be explained if the reporters hit a biological maximum for these molecules. This possibility is also a concern. The authors must explain this result.

4) The model does not match the data: The authors suggest that the model presented in Figure 3C, 3E matches their data best. However, the absolute quantities of molecules does not match the data in Figure 2C. The authors should present how well the data fits their model.

5) The authors argue that Sens levels are the same at site 22A3 and 57F5: This is not clear. The levels look quite different. This is critical for many of the authors' conclusions, especially that the phenotypic differences are a result of noise, not levels. The authors must provide a compelling quantitative argument that these levels are the same.

6) The TAD and chromatin is overinterpreted and unnecessary: The authors provide analysis in Figure 6 to show that the two insert sites are different. These data do not make a compelling argument, the analysis is incomplete, and the conclusion is fairly obvious. The authors argue that their analysis shows that the two insert sites have different chromatin environments. Wouldn't this be true of any two sites in the genome? The authors suggest that the TADs are different, but they do not conduct a proper analysis. The authors should provide and examine directionality indices to make their TAD calls. Also, the HiC is from embryos. Though TADs are generally similar across tissues, this is not absolute. For the authors to make this point, they should conduct hiC on wing discs. In general, this section does not add to the paper. The conclusion that insert sites have different chromatin environments is generally agreed upon.

7) The authors do not conduct an in-depth analysis of pairing or transvection: The authors conclude that interactions/transvection between the two sens alleles at 57F5 cause the increase in noise. However, there are problems with this argument. First, do the loci pair differently at 22A3 and 57F5? The authors should conduct DNA FISH at the site with and without the transgene to answer this question. Second, do these sites pair/loop to the other insert site and/or endogenous sens? The authors should conduct DNA FISH with and without the transgenes to test for these chromatin interactions.

8) The authors conclude that transvection increases noise, yet these experiments are completely heterologous: The authors examine transvection and noise at two sites and make their conclusions. There are problems with this rationale. First, is this a general principle for sens? Which is the general rule: transvection independent noise (as seen at 22A3) or transvection dependent noise (as seen at 57F5)? The authors should conduct these experiments at several additional locations to answer this question. Also, variable transvection at different sites has been described (ex: King, et al., 2019).

Second, what does this conclusion mean/why is it important? It is well known that transgenes can cause strange effects dependent on position. To address this issue, the authors should use CRISPR to insert reporters into endogenous sens and examine noise. However, I'm still not sure what conclusion about biology can be concluded from the transgene experiments.

Third, the differences at 22A3 and 57F5 could be due to local transcription changes (aka chromatin) or local pairing/transvection differences. The authors say that local pairing/transvection differences drive the difference but provide no evidence. To address this issue, the authors should test the transvection ability of each locus using canonical transvection assays involving the white or yellow genes.

9) The authors argue that noise drives the phenotypic differences at 22A3 and 57F5 yet the protein levels are the same – this is not a coherent argument: In Figure 7, the authors argue that the levels of Sens protein are the same at 22A3 and 57F5. This is not convincing. The authors should provide a quantitative analysis of the position and expression of Sens in these cells. The position is critical. For example, the central cells could be higher and outer cells could be lower for 22A3 compared to 57F5. This would cause the similarity in quantification of total expression seen in Figure 5C (which is not convincing, as discussed above), yet the spatial differences could cause the phenotype.

A bigger issue is the argument that noise drives the phenotype. If the protein levels are identical, it should not matter which allele provides the protein. In other words, if there needs to be 10 units of Sens in a cell, it does not matter if the less noisy 22A3 provide 5 and 5 from each allele whereas the noisier 57F5 provides 4 and 6 from each allele (or 3 and 7, etc.). At the end of the day, the absolute protein quantity should drive the phenotype, not the ratio of protein generated from each allele. The only exception would be if the alleles were different in some way. The only source of difference here would be the tags. If the tags are generating the phenotype, this is also problematic.

The authors must provide an explanation to justify this main conclusion of their paper.

Reviewer #3:

Overall, we found the manuscript by Giri et al. to be interesting and exceptionally well done, one of the cleanest analyses in the noise field in some time. The only substantial critique that one can make is the lack of single-cell RNA measurements of noise (e.g., by single-molecule RNA FISH) to validate the modeling predictions which are based on single-cell protein noise measurements. However previous studies in the field have also relied only on protein measurements (see below) and in the spirit of eLife, we feel this validation can be left for future work as long as it is stated in the Discussion as a basis for future work.

The comments we present below are intended solely to improve readability, help support the authors' claims, and avoid potential confusion.

Major comments:

1) In the last paragraph of subsection “Allele Pairing at 57F5 Generates Trans Regulation and Enhanced Noise” and Discussion paragraph two, the authors claim that the noise peak for paired sens alleles at 57F5 results from altered bursting kinetics, specifically an enhanced burst size. Although their modelling supports this claim, there is no direct measurement of RNA bursting kinetics through techniques such as single molecule RNA-FISH. Previous results support the hypothesis of transcriptional burst size modulation (PMID: 24903562) but the authors should also address alternate potential mechanisms (i.e., PMIDs 27153498, 26760529, 26544860), for example the role of alternative splicing (PMIDs: 29986741, 31222776), even if for contrast, as such mechanisms may not be functioning for sens. It should be made clear in the Discussion section that the lack of mRNA quantification is a limitation, and despite existing precedent for burst size modulation, such RNA measurements will be important experiments in future work.

Substantive remarks:

1) In Figures 4B and 5D the authors have overlaid scatterplots from separate measurements. In regions of high density, there is a loss of information as to where the center of mass lies. The authors should consider using a contour plot or shading to convey density.

2) Introduction paragraph three the authors list nuclear retention of transcripts as a mechanism for reducing protein noise that may arise from transcriptional bursts. We suggest the authors exercise caution here as the cited papers did not measure protein noise and there is now direct competing evidence indicating that nuclear export amplifies RNA/protein noise in the cytoplasm (PMIDs: 30243562, 30359620). Some might argue that the evidence in this report (increasing protein Fano factor) contradicts the papers cited which claim that nuclear export attenuates noise from transcriptional bursts to minimal Poisson levels.

3) In the final paragraph, the authors may want to mention and cite the evidence of other examples where stochastic transcriptional fluctuations appear to have evolved as a mechanism for influencing cell fate (PMIDs: 17379809, 16051143, 28607484).
