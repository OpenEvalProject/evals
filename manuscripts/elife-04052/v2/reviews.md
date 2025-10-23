# Peer review - Round 1

Editors:
- Vivek Malhotra, Center for Genomic Regulation , Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04052.023](https://doi.org/10.7554/eLife.04052.023)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Importin-β Modulates the Permeability of the Nuclear Pore Complex in a Ran-dependent Manner” for consideration at eLife. Your article has been favorably evaluated by Vivek Malhotra (Senior editor and Reviewing editor) and 2 reviewers.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

1) Show raw data for the Imp-YFP experiment that is a part of Figure 1.

2) Figure 3. Display the raw data. It is very crucial that you explain how the data was generated and normalized.

3) Figure 4. This figure also suffers from suboptimal presentation. It should be revised and clarified for the readers.

4) Figure 6. Show the exact concentration of the reagents for the procedures used and include an experiment to test the effect of Ran on Nup153G-tranportin complex. This is an important control and will help rationalize the data on Nup153-Impbeta.

The detailed comments of the reviewers follow.

Reviewer #1:

The work by Lowe et al. uses a set of fluorescence assays on permeabilized cells to study the permeability barrier of the NPC. A major conclusion from this work is that Ran itself can modulate directly the permeability barrier, by modulating two (novel) Imp-beta populations that are located at the NPC. They use siRNA knockdowns and in vitro binding studies, to argue that this modulation can occur via Nup153. The manuscript is rich in experiments, and covers many interesting aspects that will appeal to a broad readership. There are several places though, that I find confusing, or where simple experiments to rule out alternative conclusions have not been made. I will go through these partially minor, partially severe concerns in the order the Figures are presented in the paper.

Figure 1: Panel A-C) visualize a trivial concept, that cargo distribution changes once transport can be completed. What I find is missing is the raw data for the Imp-YFP experiment, which should be added somewhere. The observations in panel D-E) form the basis for many of their conclusions, and it is good to see that two different methods (FRAP, and photoconversion based FLAP) support their conclusion. With Ran, there is an enriched fast equilibrating pool of Imp-beta. This effect is then analyzed in Figure 2 with STORM based superresolution.

Figure 3: The claimed resolution of 12 nm is very high, and the analysis of positions provided makes this in principle credible (see below as well). What is clearly visible is that also two spatially separated populations of labelled Imp-beta along the transport axis can be found. This is certainly a very fascinating result, which also forms the basis for their conclusions. Convincingly (based also on the Nup358 analysis), one populations seems to be rather cytoplasmic, while the other is more nucleoplasmic. However, I have also some trouble following all conclusion and interpretations on this figure, as well as with some of the raw data and how it is displayed. In A) left panel, the Imp-beta is shown saturated (white color in the glow over low under representation), and the difference between the plus/minus Ran case is not that easily visible from the images (brightness is very different, and this is confusing, see below). The line profiles or projections (whatever it is) show a bigger difference, but conceptually I do not think this effect is that strong, that all types of definitive conclusions can be drawn from this. The apparent number of localizations went down, in line with Figure 1, but distribution change is less obvious in the raw data. This is also particular notable with respect to the data displayed in panel E and G. Here, the color coding show abundance levels, but in the white drawn box in (F), there are more abundant species (more yellow and red) than in the same box in E. This seems quite in contrast to the image panels shown in A. How was the data normalized and displayed? The difference between panel plus/minus Ran could also arise from different localization precision in the tow measurements. dSTORM is sensitive to high concentrations of dye, as multiple emitters could get activated, and then in the higher concentrated Imp-beta case, the clear bimodal distribution could get blurred. This technical issue could also explain the minor difference between the plus/minus Ran case. I do agree however, that in the Nup153 knockdown the distribution is clearly different. What does surprise me though is that I would have expected to see much less Imp-beta in the delta-Nup153 case, in line with the counting results from Figure 3. However, the image here looks at least as bright as the Imp-beta minus Ran case. Either the authors were not careful with normalizations/averaging or contrast/brightness adjustments, or something odd is going on here in the entire Figure 3. In the latter case, this would be a concern for a larger set of conclusions drawn in this paper.

Also, only in panel A) the localization data for Imp-beta no Ran and delta Nup153 seems to smear substantially into the nucleoplasm, while the nucleocytoplasmic fraction of Imp-beta should be enriched in particular in the Imp-beta plus Ran case, why?

Figure 4: While I do believe that overall reproducibility may be sufficient to make comparative analysis, I discourage of giving specific numbers in the text with only using the “approximate” sign, as true numbers might be off several fold. Stepwise bleaching analysis suffers from many problems that make determination of absolute abundance levels very, very difficult.

A) Optical sectioning in HILO is not sufficient enough, to have no contribution from out of focus NPCs in the field of view.

B) YFP, can go into dark states and return spontaneously, as every FP (leading to overcounting when just counting bleaching steps). Even conversion of YFP into CFP has been debated in a set of Nature Methods papers between 2005-2006.

C) Maturation time of FP is also an issue, that can further yield wrong numbers. Corrections for all those parameters were not done, and are also difficult to do. A few procedures on how to do this have been established by Annibale et al. and Lee et al. e.g. for photoswitchable proteins, because traditional FPs have all these issues, of which the contribution is much harder to estimate then for well characterized real “switchable” proteins.

D) Due to crowding, Homo FRET might affect overall brightness, when ∼ 70 YFP get squeezed onto a small volume of an NPC transport channel. The effect cannot be easily estimated, and can contribute to substantial imprecision. An “approximate sign” does not seem to sufficiently account for this in my eyes.

Again, the overall conclusion might not be affected, but the true number of Imp-beta at the pore might easily be several folds off. This should be clarified for the reader, as otherwise they simplify a big problem in quantitative proteomics: Getting abundance levels from fluorescence images is not as easy as just bleaching the sample, especially not for high abundant proteins, where the initial brightness is very high.

Figure 6: I have trouble following the logic of the motivation and description of these experiments in relation to the in vivo experiments, while at the same time I find the result intriguing, which is, that the Importin beta cross links Nup. Overall, this does not come very much as a surprise, since Imp-beta has several binding sites for FG repeats and this will lead to aggregation (the authors need to report the exact concentration in the methods part, and not just “micromolar for both”). I assume, the same experiments can be shown to work with most transport receptors of this type and larger FG Nups. I would speculate, transportin will give the same effect, and they could easily do such an experiment. If also Ran can solubilize Nup153FG-transportin complexes, I wonder how such a generic mechanisms can be rationalized in line with i) their finding that in vivo the Imp-beta and transportin are doing different things (and how this in vitro experiment is then supporting their conclusions) ii) with their model of specific relevance's of certain proteins (Nup153 and Imp-beta).

Much of my criticism can be addressed with simple experiments that could be performed in a timely manner, and should thus be possible within a major revision.

Minor comments:

As a minor comment, in the Discussion, they speculate also about the potential role of Imp-beta structure, in light of a similar architecture of some scaffold Nups. How do they rationalize this, since transportin is also similar in structure, but is apparently not doing the same as Imp-beta.

Also, with Figure 6 and Figure 7, the authors use the words “reminiscent” in terms of “gels”, a topic of particular relevance in the transport field. Besides not every aggregate necessarily also being a gel (their structures could be, but this would need different assay to confirm) their potential gels are conceptually very different than the ones originally introduced by the Gorlich lab. In their gels, the Nup is crosslinked by Imp-beta, while the Gorlich gels is based on homotypic interactions between Nups only. I think using the term “reminiscent” as used by the authors is not pointing enough to the fundamental difference of their model. It also remains open, to what extend Nup153 is the only Nup that would cause such an effect. Other factors might certainly be important as well, but naturally, not everything can be addressed in a single study. E.g., a previous single molecule study that has directly shown that Nup50 is important for cargo dissociation of Importin complexes is neither cited nor discussed.

Reviewer #2: Nuclear pore complexes mediate traffic between the nucleus and the cytoplasm. The selectivity and efficiency of transport through the nuclear pore complex is not fully understood. In current models, Ran in its GTP or GDP bound form gives direction to transport by modulating the interaction of Impβ with its cargo's on either side of the NPC. The current manuscript provides proof that RanGTP influences the permeability of the NPC itself. Based on modern microscopy techniques that reveal the number, localization and mobility of Impβ molecules in the NPC the authors propose that impβ and Nup153 interact at the nuclear side of the NPC where they form a Ran-regulated meshwork. Transport experiments show that modulation by Ran alters both passive and active transport.

The manuscript thus presents new interesting insights into the transport mechanism of the NPC. Future studies will have to resolve if in vivo modulation of the Ran gradient is an important mechanism to fine-tune NPC permeability; it is an exciting possibility.

I find this an exciting an impressive piece of work on an important topic that should be accepted for publication in eLife.
