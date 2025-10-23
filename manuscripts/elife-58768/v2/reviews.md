# Peer review - Round 1

Editors:
- Mohan K Balasubramanian, University of Warwick United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58768.sa1](https://doi.org/10.7554/eLife.58768.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your paper using genetics and imaging (with an embedded computational framework) very nicely examines how the number of polarity sites are established, using yeast as a model. The dissection of competition mechanism and the novel equalization that you describe will fuel further work in this field both in yeast and in other organisms, especially those which contain multiple polarity sites in normal physiology.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "How cells determine the number of polarity sites" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The referees are enthusiastic about the topic and the question you are addressing, i.e. how polarity sites and their numbers are chosen. They also found a number of observations in the work interesting. However, all the three independent referees have raised a number of questions, both concerning the modeling as well as with the experiments, and also in citation of past work. In light of all these concerns, we are unable to publish this work in eLife. The referees comments are provided verbatim below.

Reviewer #1:

The manuscript entitled "How cells determine the number of polarity sites" by Chiou et al., compares theoretical models for polarity establishment in budding yeast, specifically their regulatory mechanisms, with experimental observations, in particular those that can lead to polarity cluster coexistence or equalization. After examining the implications of several models of increasing complexity the predictions of specific aspects of these models are explored, in particular alteration of cell size and polarity protein levels. While the findings presented are interesting, the overall message is not sufficiently clear and hence this obscures the significance of the work. Substantial rewriting is necessary together with refocusing to make the work more accessible to a broad audience.

1. The main findings of this work are not evident from the title, introduction and first paragraph of the Discussion. The Discussion talks about several classes of models, but does not indicate clearly which model best describes the observed behaviour. The title and abstract are somewhat general, overall appear descriptive and do not clearly indicate the findings. For example, in the Discussion section, page 25, it states, "Here we propose a novel mechanism for equalization that does not require negative feedback, but can account for the behavior of the more complex models that incorporate negative feedback," however it is not evident what this mechanism is.

2. Reference to and discussion of finding from several relevant and recent studies are lacking. For example, 3 studies, which use optogenetic systems to alter levels and/or clusters of active Cdc42 in fungi are not discussed, these findings are likely to be relevant to mechanism of polarity cluster control, see

-Witte et al., eLife 2017 e26722

-Lamas et al., Plos Biol 2020 18: e3000600

-Silva et al., Cell Rep 2019 28: 2231

Note that while the latter two are carried out in different yeast, the approaches involve temporal recruitment of active Cdc42 to the plasma membrane and hence are relevant to this work.

Furthermore the Discussion section (to some extent also the Introduction section, see also below), including the last subsection of "Implications for other systems" unfortunately does not put this study into the context of what is known about polarity determination outside of the budding yeast perspective, which limits its general interest. For example, I am surprised there is no mention or discussion of the recent work from the Goehring laboratory entitled "A Cell Size Threshold Limits Cell Polarity and Asymmetric Division Potential" (Hubatsch et al., Nat Phys 2019 15:1075) which would appear to be very relevant.

Similarly, the introduction seems to be overly focused on budding yeast with little indication of other systems and the more recent findings, including those from fission yeast (as opposed to cursory mention of an old S. pombe review) and other fungi, such as Neurospora crassa, among others. Furthermore, other reviews cited are quite old.

3. Throughout, the terminology 'protein content' is used which is imprecise. Are the authors referring to total protein amount or amount divided by volume, i.e. an effective concentration? This ambiguity is confusing, in particular in the Discussion section. It is unclear whether larger cells (page 20) have a higher amount or effective concentration of polarity proteins. It is surprising that this aspect of polarity would be cell size dependent given different sizes of haploid and diploid yeast cells.

4. Figures should be organised more clearly, with panels in left to right, top to bottom order (Figure 1-3), graph axes indicated (lacking in many panels including 1D, 2D, E, G, H), color schemes unclear (1G and 1H compared to 1I and 1J; green color used for different species), what is shown in different panels is not indicated (2D, 2H), in some scatter plots means and standard deviation should be indicated (3G, 5A, 5G), in several graphs error bars should be indicated (5B, 5E, 5I) and Figure 6 can be substantially simplified with at most 2 examples of each behaviour shown in A, together with an indication of what the lines refer to (the rest can go in the supporting figure). In addition, it is not clear in 6A if competed (note mix of past tense verbs and nouns for description, better to indicate 'competition, coexistence and equal) is actually different than equalized, in which the initial intensities are inversed, i.e. red higher than blue (A, i).

5. The analysis and interpretation of the cytoplasmic connection in Figure 3D-F and presented on page 14 (and mentioned again on pages 21 and 23) appears over-simplified. Firstly, diffusion of relatively small cytoplasmic GFP is unlikely to be directly relevant with respect to larger proteins and complexes, as well as those which can associate with membranes. Indeed this same septin mutant allele (cdc12-6) has been used to show that septins play an important role in cell cortex compartmentalization (Barral et al., 2000 Mol Cell 5:8410). Secondly, the photobleaching experiments were single photon, i.e. not limited to a small focal volume and hence a substantial region above and below the focal plane was bleached. It is unclear, in this situation, how differences between bud and mother cell geometry affects fluorescence recovery. As a result, attributing the outcomes to cell size appears to be an overly strong conclusion (page 14 and bottom of 15). Indeed the word cell geometry may be more appropriate than size. In the data presented in Figure 3H do the 2-budded cells form buds simultaneously or subsequently? This should be indicated and shown in a supporting figure.

Reviewer #2:

In this manuscript the authors study the concepts and cellular mechanisms that allow formation of multiple polarization sites. They focus on the S. cerevisiae model system and combine theoretical models with quantitative image data as validation of their predictions. They interpret formation of multiple polarization sites as a shift from competition to co-existence in a mass conserved reaction-diffusion system (MCAS). They conclude that a key feature in this scenario is the amount of available substrate in the system, determined by parameters such as cell size and expression levels.

My key conceptual criticism is that while the authors discuss several variants of reaction diffusion models in detail they completely ignore two fundamental aspects of cellular polarity systems: the cycling of the GTPase and in particular the link between activity cycling and physical cycling via GDI, and the role of vesicular transport in recycling of membrane-bound proteins and in supporting the polarization process. This is particularly striking as the role of these parameters has been studied in detail regarding their effects on formation of multiple polarization sites. As one key conclusion from previous work was that yeast cell were not able to form multiple polarization sites in the absence of actin I would have expected a convincing argument to ignore this point in the current study. Previous data also showed that the levels of active Cdc42 (by overexpressing Cdc24 or using a slow cycling mutant) directly increased the number of polarization sites formed through its limiting effect on GDI-based recycling. By ignoring those fundamental aspects of the polarity system the authors made it very hard for me to accept or follow the arguments provided in this study.

1. All citations for interactions between Cdc42, PAK Bem1 and Cdc24 are very selective – several of the postulated interactions are far from being established and open questions should be clearly stated. Lacks all referrals to pertinent studies by Li, McCusker and Wedlich-Söldner labs.

2. Page 6 third paragraph: in scenarios of two linked substrates isn't it obvious that the one with lower abundance will be limiting? Not really fitting to a Results section in my mind.

3. Page 10, third paragraph: Freisigner et al. is cited for the lack of effect of Cdc42 OE, but all the results in this study showing that OE of Cdc24 or increasing the activity of Cdc42 (deletion of Bem2 or fast cycling mutant of Cdc42) leads to formation of multiple polarization sites are ignored – those would be far more relevant here.

4. The image series in Figure 3A does not show two buds growing simultaneously from one cell segment – does this ever happen or are the buds only formed from distant segments? If diffusion is indeed not limiting shouldn't the distance between two forming buds be random – hence also occur within a single segment?

5. In general I have fundamental issues with the chosen method of generating larger cells – the cdc12 defective cells have not been sufficiently characterized and have man additional parameter changes beyond the simple increase in volume. Effects on cell cycle, attachment of formins (Bnr1 is recruited through septins), PM organization (what happens to eisosomes, lipid composition etc.) and many more. The cell is simply too complex to use such crude methods to validate mechanistic models. I didn't understand why they did not simply go with cell cycle arrest and larger cells. Even with the reported cytosolic dilution they could perform tests where they relate their conditions to the corresponding controls.

6. They should definitely show how actin is distributed in the cell chains and perform the basic tests of polarization in LatA treated cells. While Bem1 or Cdc24 might not be limited by diffusion – actin nucleators, vesicles or actin filaments will likely be. Of course bud formation will be stopped but polarized patches should still be able to form. The effect of 37{degree sign}C shift is also of particular relevance in this context as it has been linked to actin disruption in previous studies.

7. Please provide the bud-number analysis for the correct test strain with Drsr1 and expressed polarity marker – is this equivalent to the numbers in 3B? Please provide images for bud scars to exclude effects of those (even in rsr1D) on polarization.

8. Formation of Bem1-clusters will likely depend on local lipid composition – images often not good enough to distinguish between local micro clusters and polarized accumulation but the clusters often seem to be at the base of the bud and not at the bud tip – please clarify.

9. Panels in Figure 4 are too small – nearly impossible to follow. Blue patch in lower series of 4B seems to move from right to left – possible issues with projection or deconvolution? Why is patch not at bud tip? Same in lower series of 4C: patch seems to be at base of bud – very confusing.

10. Figure 5I: those three proteins cannot be thrown together – OE of Cdc42 and Cdc24 should result in very different outcomes (change in substrate or activator) – provide effects for each protein separately and show actual images as well as quantification of protein levels (western or GFP fluorescence). Again, this has been done in similar way in Freisinger et al. and showed link between Cdc42 GTPase cycle and number of polarity sites.

Reviewer #3:

This is a dense and quite technical manuscript pertaining to the mechanism of cell polarization in budding yeast which relies on a Rho family GTPase, Cdc42, that is known to exhibit positive feedback and in wild-type cells. The focus of this work is to identify whether these same biochemical circuit can also generate two foci that do not undergo competition as is the norm in this pathway, and if so, to identify such conditions and to provide a conceptual framework for the absence of competition.

In its present state, I do not find that this manuscript provides compelling evidence to support the underlying conceptual argument, namely that patch saturation can allow to foci to co-exist. Furthermore, the manuscript is challenging to follow, the figures are sparsely annotated so they are not self-explanatory and the text, while readable, is to lengthy (almost 10K words) not well organized, diluting the authors message.

Comments related to modeling:

1. It is not clear why the authors discuss the minimalistic model in this paper. It is discussed in their earlier work, which is probably essential for many readers to understand this manuscript (or superfluous for those fully conversant in these models). I understand that it is for simplicity, but it is a distraction that does not apply to the in vivo situation. In addition, in figure 2C, the indirect substrate is a theoretical construct that alters the behavior of the model but lacks a mechanistic counterpart. Along these lines, there is some overlap with the Chiou, 2018 PLOS comp bio paper.

2. Does the authors model predict that equivalent cells would form variable numbers of patches (eg Figure 5B)? And that these patches would resolve with different outcomes (eg Figure 5E)? If not, what are the implications of this mismatch?

3. There is no direct experimental evidence to suggest the existence of an "indirect substrate" with differential mobility.

Comments related to experimental data:

1. The coexistence of multiple sites is predicated on the concept of saturation which has been shown to exist in simplified computational models. Based on that model, the authors explore some of the predictions of this model, namely that cell size and protein levels will enhance co-existence of multiple sites. However, the authors do not directly document saturation, which is the key predicate of the model. The predictions that are tested to support this model may not be unique to the proposed model.

2. The use of GFP and its diffusion as a model for all the relevant species in the model is not well substantiated. The relevant proteins are much larger, in variably stable protein-protein complexes, and associate with cortical factors, lipids, proteins etc. This is a critical point, because slower diffusion of key components could prevent patches positioned at a distance from effectively competing with one another. The diffusion rates of the relevant proteins would need to be measured directly, when expressed at their normal levels. Perhaps the authors could FRAP Bem1 at one patch and measure the rate at which the other patch dims.

3. Related to the previous point, in Figure 6 in the author's 2018 modeling paper, they suggest that when saturation is operative, an increase in cell size rapidly limits competition between patches (black curve). The change in behavior with increasing cell size is far less striking in vivo than would be predicted.

4. The authors provide evidence that the situation in vivo is far more complex that their model would predict. Pools of "cytokinetic Bem1" are documented and the position of bud sites is not random ("the locations at which patches formed were non-random, with a preference for bud tips and mother cell locations (Figure 5C)"). These phenomena indicate that distinct mechanisms may be operable in vivo raising doubts that the in silico version can be directly applied in vivo.

5. In the model, the authors appear to assume that all Bem1 is bound to Cdc24 and Cla4? This is not well supported by the evidence in the literature (page 14 refs).

6. The authors "utilized cytokinesis-defective yeast mutants to obtain large connected cells that continue cycling and presumably retain a normal overall protein composition." the underlying presumption is important for the analysis of the data, yet it is assumed, not tested.

7. For some of the cells in the second row of figure 6A, the linear "interpolation" does not match the data well. What is the basis for this "interpolation"?

It would be useful to indicate the distance between the patches for the 20 cells in Figure 6.

8. Inhibition of actin polymerization could be used to inhibit budding and cytokinesis and might allow the authors to obtain cells that continue to cycle but retain a simple geometry.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "How cells determine the number of polarity sites" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and a Reviewing Editor (Mohan Balasubramanian).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. Please note that one experiment has been suggested (point 5 below). If you have the data readily available, please do add it.

The rest of the points raised can be addressed through rewriting.

1. The text related to the portion regarding saturation requires further editing:

Line 76 "However, recent studies have shown that the growth rate of a peak "saturates" as the activator in the peak exceeds a threshold." Given that saturation is not shown empirically, this sentence should refer to "modeling studies".

This paragraph also refers to the possibility of equalization and explicitly states on line 83 "it has not yet been determined whether equalization occurs in cells". Given that saturation has also not been empirically demonstrated in cells, this too should be explicitly stated.

2. The authors observe that some cells also exhibit equalization, which the authors indicate is not possible in the "mechanistic model" as written. They further show that this becomes possible if an "indirect substrate" is incorporated into the model. This is an interesting finding even though the "indirect substrate" remains hypothetical/speculative. However, it does reveal that the mechanistic model based on MCAS does not provide a fully accurate description of the in vivo situation. Given that the reader was previously led to believe that the mechanistic MCAS model was supported by the available data, this apparent shortcoming is a bit jarring. The authors state (line 333) "Our conclusions from analysis of the simple indirect substrate model can explain the outcomes from all of the models discussed above and in previous studies (Figure 5-Figure supp. 1)." This sentence suggests that models with an indirect substrate would also predict that the increase in protein concentration would also lead to multibudding in this regime and figure 5 supports this interpretation. Nevertheless, it would help the reader to even more explicitly state that indirect substrate models is fully consistent with the findings up to that point in the manuscript.

More broadly, this manuscript begins as a Figure 1 Theory paper in the Phillips vernacular (PMID 26584768), but transitions to a "Figure 7 Theory paper". It would behove the reader to more clearly foreshadow the revision to the model in a subsequent figure.

3. Moreover, the description of the indirect substrate is unclear: line 280ff "The GAP and the inhibited GEFi are neither substrates nor activators, and appear to play different roles in the polarity circuit. However, we noticed that they both provide a source of substrate: the GAP converts local GTP-Cdc42 into the substrate GDP-Cdc42, while the inhibited GEFi turns into the substrate GEF upon dephosphorylation. Thus, in both cases a new species produced by the activator is highly mobile and generates a substrate in the cytoplasm."

In particular, the phrase "the inhibited GEFi turns into the substrate GEF upon dephosphorylation" is unclear. While it is evident that the inhibited GEF turns into a GEF upon dephosphorylation, this active GEF is not a substrate and thus does not fit the descriptor of being "highly mobile and generates a substrate in the cytoplasm." particularly as the GEF is unlikely to be active until it reaches the membrane. The confusion appears to arise from a conflation of the minimalistic model with a semi-mechanistic one. Whereas the activator and substrate are interconvertible in the minimalistic model, the same is not true in the semi-mechanistic one. This requires clarification.

4. Along these lines, it would be appropriate for the authors to discuss in this context the paper from Rodriguez et al., PMID 28781174 which demonstrates that the anterior PAR complex proteins PAR-6 and aPKC are induced to dissociate from PAR-3 by Cdc42 binding, which is analogous to this principle.

5. This study also raises the question as to whether the presence of multiple initial polarity sites described in Howell, 2012 and subsequent papers from the lab results from the hydroxyurea treatment which, by creating a cell cycle delay, would be expected to increase the amount of polarity proteins that exist in cells, thereby facilitating such behavior as shown here. It would be quite interesting to determine whether the strain overexpressing Bem1, Cdc42, and Cdc24 generate more nascent sites in otherwise unperturbed G1 cells as compared to their WT counterparts.
