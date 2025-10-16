# Peer review - Round 1

Reviewers:
- Avigdor Eldar, Tel Aviv University , Israel

## Review text

DOI: [10.7554/eLife.18657.031](https://doi.org/10.7554/eLife.18657.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cell wall remodeling drives engulfment during Bacillus subtilis sporulation" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

We find the manuscript interesting, insightful and well written. The experimental data provide a wealth of novel insights and the synthesis provided by the modeling scheme nicely fit engulfment dynamics of the wild-type and mutant phenotypes. Nevertheless, there are multiple points which need further clarifications both on the experimental and theoretical sides. We therefore recommend acceptance with major revisions that will answer the concerns of the reviewers and the Reviewing Editor.

Overview of the manuscript:

Previous works showed that peptidoglycan (PG) production occur at the leading edge of the engulfing membrane and that this leading edge of the mother-cell (MC) membrane seem to invade below the old cell wall made prior to asymmetric septation (Tocheva et al., 2013). In addition, reduced PG synthesis was also shown to affect engulfment (Meyer et al., 2010). The current work goes beyond the previous works and show that: 1) A block of PG synthesis halts engulfment completely. 2) PG synthesis at the leading edge (LE) is primary guided by PBPs localized to the leading edge at the forespore side. 3) SpoIIP localization to the LE is dependent on PG synthesis.

The authors present a biophysical model of PG synthesis which recapitulates the observed membrane dynamics of wild-type and mutant phenotypes by assuming that PG synthesis from the forespore (FS) is followed by degradation of the links between the old (pre-septation) and new (forespore dependent) PG layers, allowing the MC membrane to fill this gap.

Essential revisions:

The comments are both on the experimental and modeling parts of the manuscript.

Experimental work:

The major requests of the reviewers and the Reviewing Editor are the following:

1) PBP localization. Reviewer #1 expressed concerns regarding the mechanism of localization of PBPs. One of the options is that this localization is guided by other forespore specific proteins which interact with the leading edge. Specifically, as was raised during the discussion, we ask that the localization of PBPs will be studied in mutants of the FS-MC channel composed of spoIIQ, spoIIIAH and GerM.

2) Reviewer #2 suggests that real time monitoring of PBPs processive activity as was done for MreB (Domínguez-Escobar et al., 2011; Garner et al., 2011) would enable direct comparison with the model predictions.

Modeling:

The mathematical model has multiple underlying assumptions. We ask that you will further discuss these assumptions and extend the modeling scheme to further understand which of those is necessary. The major specific concerns raised are:

1) How does the model fit to the Gram positive envelope with its multiple layers, the presence of techioic acid and the unclear arrangement of PG strands (Reviewer #1)? Specifically, the model is very different than the one presented in Nguyen et al., 2015. Can the authors discuss these differences?

2) Discuss and simulate the validity of the assumption that the forespore-dependent synthesis of PG results in a difference between the new and old PG structure that enable specific breakage of the connecting peptide bond (Reviewer #1 and Reviewing Editor).

3) The presence of a tight insertion-degradation complex (IDC) is speculative. Compare simulation results of tight IDC activity (shown now) with simulations where synthesis and degradation are not coupled into a complex but are more weakly associated (as in Figure 2G).

4) Further illuminate the functional importance of the 'make before break' model for this process (see further elaboration of this point below in the section "Comments on modeling raised during discussion").

Comments on modeling raised during discussion:

1) 'Make before break' and cell wall integrity. It is not clear to me whether the make before break process in the model is really needed for maintaining cell-wall integrity, as the model anyway assumes that the DMP complex is not effective in breaking the old cell wall and therefore does not jeopardize its integrity. It seems to me that the 'make' part is only necessary to ensure the specificity of the 'break' part. That is, to ensure that a forespore specific layer will be produced that allows the specific degradation of its connections with the old pre-forespore layer above it.

2) "Make just before break" vs. "make before break". Is localization to the LE critical or just more economic? It is not clear to me that the process would not have worked if the new layer would have been produced everywhere and then hydrolyzed specifically at the LE. It would be illuminating to see a simulation where it is assumed that there is no localization and the difference between cases discussed.

3) The role of the DMP complex in the simulations. The simulations seem only to show the making of the forespore inner layer of PG, but does not say anything about the interaction between this layer and the old layer and the corresponding mechanism of degradation of links between the two layers by the DMP complex. In effect, it seems that the DMP complex has no role in the IDC in the simulation. This might be OK, if one assumes that there is an IDC, but the authors claim in the Discussion that similar behavior would be observed if the two are not tightly linked. Can the authors present a more general model where spatial association is not tight (as shown in Figure 2G and discussed in the Discussion section)?

Reviewer #1:

The manuscript by Ojkic et al. presents a wealth of data on the mechanisms of endosporulation in Bacillus subtilis. In particular, they used fluorescence microscopy to observe the process of engulfment in the presence and absence of drugs inhibiting peptidoglycan synthesis. The data confirm previous studies concluding that both, peptidoglycan synthesis and hydrolysis are needed for membrane migration during engulfment. Multiple PBPs localized to the leading edge of engulfment. They present a model of how a biosynthetic complex and hydrolytic enzymes together facilitate engulfment by remodelling the peptidoglycan layer. Although a lot of data are presented in this impressive work I do have problems with the modelling. In my view the modelling goes too far and is quite speculative. Key aspects of the model are not supported by experimental data.

My specific points are as follows:

1) Introduction, statement about the "Gram-negative like PG layers in Bacillus subtilis" and modelling of the peptidoglycan. The architecture of PG is still a matter of debate, most data are available for E. coli and these support a single disordered layer made of relatively short glycan chains connected by peptide cross-links. However, although the Jensen lab hypothesized based on cryo-EM imaging that Gram-positive species stack multiple of such layers, there is not really good evidence that this model is correct. Other models have been proposed for example the one presented in Nguyen et al., 2015, which is quoted only for the glycan chain length but not for the Bacillus peptidoglycan model. The model presented in Nguyen et al., 2015 presents a more complicated arrangement of glycan chain bundles and was based on AFM images (Foster lab). The peptidoglycan from B. subtilis has significantly longer glycan chains than that from E. coli, and in B. subtilis the peptidoglycan is loaded with a significant amount of wall teichoic acid. Hence, we currently do not know the precise architecture of the peptidoglycan-wall teichoic acid in B. subtilis. The model presented here for the peptidoglycan architecture at the site of engulfment cannot be tested with any current technology and has therefore limited value.

2) Subsection “PG synthesis is essential for membrane migration”, first paragraph. Because fosfomycin and D-cycloserine failed to completely block polar division, they concluded that peptidoglycan might be obtained by recycling during starvation conditions. However, this is a quite speculative assumption which does not seem to be logical, because recycling requires peptidoglycan turnover, which occurs to significant extent only in growing bacteria. Does the mother cell grow during asymmetric septation, or where would the recycling material come from?

3) Discussion, first paragraph. It is not clear what is meant by the 'unique chemical composition of the peptide bridges' that are recognized by DMP. This would imply that the same PBPs, which were found at the leading edge of engulfment and which synthesize the peptidoglycan of the lateral wall or septum during vegetative growth, produce peptide bridges with different composition when they are active during engulfment. This is a highly speculative assumption.

4) Discussion, second paragraph. The PG-insertion-degradation complex (IDC). This is another speculation that is not based on evidence, as they do not present any interaction data between the different peptidoglycan enzymes (PBPs and hydrolases) and other engulfment proteins.

Reviewer #2:

The manuscript describes several experimental findings that advance understanding of engulfment during Bacillus sporulation. The new insights are used to formulate a mathematical model that reproduces experimentally observed engulfment phenotypes. Together, the experimental and modeling results are an important contribution since engulfment is crucial for endospore formation but a mechanistic understanding has been lacking.

The main experimental findings are 1) peptidoglycan synthesis appears to be essential for migration of the leading edge (LE) of the engulfing mother cell membrane and for localization of SpoIIP (a protein in a peptidoglycan degradation complex) to the LE, based on results obtained with inhibitors of peptidoglycan synthesis, and 2) peptidoglycan-binding proteins (PBPs), which synthesize peptidoglycan, localize to the LE, in most cases only if the PBP is expressed in the forespore. Based on these findings, the authors propose that peptidoglycan synthesis and degradation by forespore PBPs and the mother cell SpoIIP-containing complex, respectively, causes the junction between septal peptidoglycan and the lateral cell wall to move, creating space into which the LE of the mother cell membrane moves by entropic forces.

The authors formulate a model based on the "template mechanism" of vegetative cell growth, in which existing glycan strands serve as a "template" for synthesis and peptide cross-linking of a new glycan strand prior to degradation of "old" peptide cross-links and perhaps some of the "old" glycan strands. Dynamic simulations with the model produce engulfment with timing, and with forespore area and volume, that match the experimental observations. Simulations in which the probability of the modeled "insertion-degradation complex" initiating and continuing polymerization at glycan ends is too low result in asymmetric engulfment, as observed experimentally when inhibitors of peptidoglycan synthesis are added.

I support publication in eLife based on the fundamental biological insight provided, the convincing data, and the excellent presentation which is suitable for a broad audience.

That said, the manuscript could be strengthened as follows:

1) Provide direct evidence for peptidoglycan synthesis at the LE (e.g., using fluorescent D-amino acids). The data do not completely rule out a mechanism involving only degradative remodeling of the lateral cell wall to create the germ cell wall, if the peptidoglycan synthesis inhibitors used unexpectedly inhibit degradation.

2) Track forespore-expressed GFP-PBP fusions (as for GFP fusions to MreB isoforms in Domínguez-Escobar et al., 2011and Garner et al., 2011). If the predicted circumferential motions were observed, and, if it were possible to measure their number and speed, predictions of the modeling made in the last paragraph of Results could be tested.

3) For completeness, do parallel experiments on localization of SpoIID and SpoIIM, to those reported on SpoIIP, since the three proteins are expected to form a complex.

4) Clarify whether the probability of initiating glycan polymerization from an end defect (pdef in subsection “A biophysical model to describe leading edge migration”) is different from the probability of inserting new glycan from an old glycan end and repairing the end defect (prep in Figure 3B legend).
