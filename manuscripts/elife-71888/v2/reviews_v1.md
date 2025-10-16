# Peer review - Round 1

Editors:
- Pekka Lappalainen, University of Helsinki Finland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71888.sa1](https://doi.org/10.7554/eLife.71888.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study is of interest to researchers studying the actin cytoskeleton, cell adhesion, migration and morphogenesis. Through a combination of experiments and mathematical modelling, the authors provide interesting insights into the roles of three non-muscle myosin isoforms in cellular morphodynamics and force generation.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Distinct roles of nonmuscle myosin II isoforms for establishing tension and elasticity during cell morphogenesis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission have agreed to reveal their identity: James R Sellers (Reviewer #1).

Our decision has been reached after consultation between the two reviewers and based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

This paper is of interest for scientists studying cell migration, adhesion, and mechanosensing. The work provides interesting new information on the roles of non-muscle myosin II paralogs (NMIIA and NMIIB) in the mechanics of contractile actomyosin bundles. Through generating NMIIA, NMIIB and NMIIC knockout cell-lines, and analyzing their phenotypes on homogeneous and micropatterned substrates, the authors provide evidence that NMIIA is responsible for the generation of intracellular tension, whereas NMIIB elastically stabilizes the NMIIA-generated tension. They also performed fluorescence-recovery-after-photobleaching experiments, combined with mathematical modeling, to elucidate the role of different exchange kinetics of NMIIA and NMIIB in myosin minifilaments.

The data presented in the manuscript are of good technical quality. However, some conclusions presented in the manuscript are not particularly strongly supported by the experiments, and thus the study is somewhat preliminary at this stage. The detailed comments by the two reviewers can be found below. In the discussions among the reviewers it was also considered that, although the manuscript certainly provides new information on the different roles of NMIIA and NMIIB, this study does not present such fundamental new insight into the functions of NMII paralogs that would make it a strong candidate for publication in eLife.

Reviewer #1:

This manuscript examines the role of nonmuscle myosin IIA and IIB in establishing tension and elasticity in cells. They use CRISPR/Cas9 technology to ablate the specific paralogs and grow cells on micropatterned surfaces.

An unaddressed point, both experimentally and in the discussion and modeling, is what are the relative amounts of NM IIA and NM IIB in the U2OS cells? Also does the level of expression of one paralog change in response to ablation of the other?

On homogeneous substrates the authors show the localization of stress fibers and focal adhesions in both wild type and in the myosin paralog-specific KOs. They show the localizations of the myosin paralogs in the WT cells, but do not show the localizations of the remaining myosins in the paralog-specific KO cells. It would be informative to see this.

Line 190: I think there needs to be more discussion regarding the word "circular" as a description of arc shape.

Lines 195-197: Describe the origin of the values given for λ and σ.

NM IIA KO cells. The images shown in Figure 2—Figure supplement 1 does not appear to back up the statement that "only a few NM IIB minifilaments co-localize". It also makes me return to the first point made above about relative amounts of the myosins.

Modeling: The authors might want to use the term "duty ratio" to explain the difference in load bearing ability. Also, they do not mention the possibility of load-induced changes in the kinectis of these myosins. In this regard they should reference Kovacs et al. (2007)( doi: 10.1073/pnas.0701181104) which showed that the kinetics of both NM IIA and IIB are affected by load, but that NM IIB is more sensitive.

Lines 332-334. If the NM IIB filaments in the NM IIA KO cells are not phosphorylated, you might expect that blebbistatin might have little or no effect on these cells. Could this be tested?

Figure 3—figure supplement 2. I do not think these experiments add anything to the manuscript, unless more supporting information is provided. First of all, the details of this are not mentioned very prominently in the results. Second, the various mutants are used without any corroboration that they are actually behaving in the manner that is referenced. The authors should show (and quantify) the myosin filament localizations for these mutants.

Figure 5. Would you like to speculate on the "immobile" fraction of the myosin paralogs in the FRAP experiments? Do you envision that, perhaps, the myosin hexamers in the core of the filaments do not exchange? If so, that might not be consistent with your interpretations that these filaments can dissemble and form rapidly.

Line 388: There is actually quite a bit of controversy as to which kinetic step is correlated with force generation for myosins. Several studies suggested that force generation is associate with either ADP release or an isomerization of myosin-ADP states.

Blebbistatin inhibits the ability of myosin to enter a strongly bound state. In the presence of blebbistatin myosin binds only weakly to actin. If it inhibited the force-generating step then you would expect myosin to be strongly bound to actin in the presence of blebbistatin. Essentially, blebbistatin converts a phosphorylated, active NM II to a state that mimics unphosphorylated, inactive myosin.

Line 422. The Kovacs et al. (2007) paper mentioned above supports the notion that attachment lifetime of NM IIB is more force dependent than is that for NM IIA.

Reviewer #2:

This study investigates individual roles of three nonmuscle myosin II paralogs in U2OS cells using CRISPR/Cas9-mediated knockouts of each paralog. A novel aspect of this study is that the authors use cross-shaped fibronectin patterns to culture cells, which allowed them to evaluate quantitative aspects of the resulting phenotypes. As key metrics, they used a relationship [R(d)] between the curvature and the length of the lateral actin arcs formed on such patterns. The underlying hypothesis is that these parameters are defined by a competition between the surface tension all over the cell and the line tension in the arc. The authors also developed mathematical models to evaluate the ideas that the differences in both R(d) and the exchange rate of two myosins, NM IIA and NMIIB, result from distinct kinetics of their motors. These data reveal certain aspect about individual functions of NMII paralogs, although additional clarifications about underlying biology would be very helpful. Besides this main line of investigations, authors also present other observations, from which they draw conclusions, which are not sufficiently well justified.

1. The benefits of R(d) as the main parameter to characterize the differences in KO phenotypes are not obvious. Indeed, the difference between the IIA KO and IIB KO phenotypes is visually quite obvious, but it is not revealed by R(d). Can this parameter inform us about how the surface tension and/or the line tension changes in each case?

2. On the patterns, actin and myosin localize not only to arcs, where they apparently generate the line tension, but also to the cytoplasm over the passivated substrate, where they might generate surface tension. After IIB KO, more actin (Figure 2C) seems to move to the cytoplasm relative to how much remains in the arcs. Can it mean that these cells have higher surface tension and lower line tension relative to wild type? In this is the case, according to the proposed model, such redistribution should result in a higher curvature of the arcs, but the actual result was opposite – straighter arcs, which should mean that the line tension overwhelms surface tension. Does it mean then that IIB is mainly responsible for the surface tension? Is there a biological explanation for this result?

3. The assumption of a slower inflow from focal adhesions in the absence of IIA predicts straighter arcs. Conversely, a faster inflow in the absence of IIB should lead to more curved arcs. However, the results are opposite. Why do these intuitive considerations conflict with the conclusions of the model?

4. While interpreting the IIA KO phenotype, authors need to take into account that total amount of myosin II is significantly reduced in KO cells, as IIA is the major isoform in U2OS cells, suggesting that the phenotype could be well explained by a lower quantity, not by a different quality of the remaining myosin. A proper control would be to use cells that express IIB in the IIA KO cells at approximately the same level as total myosin II in WT cells.

5. The conclusion that IIA is necessary to initiate assembly of IIB filament is not supported by the data, which show that peripheral myosin II filaments in the cells have 75% of IIA subunits and 25% of IIB subunits (Figure 4-s2F), thus suggesting that all filaments initially contain both IIA and IIB, but their ratio changes over time and distance from the cell edge. No homotypic IIA filaments have been demonstrated in the study. Despite the conclusion saying "we found that all heterotypic minifilaments arise from homotypic NM IIA minifilaments" (p. 15, ll. 349-350). Available data in the literature show that IIB can polymerize by itself both in vitro and in cells lacking IIA. The claim that IIA or IIAΔIQ "restore" IIB filaments is not validated quantitatively. In fact, in figure 4-s1A, a NM IIA-KO cell that does not express GFP-NM IIA-WT has abundant NM IIB filaments. Moreover, the authors show that overexpression of IIB also restores NMIIB filaments (Figure 4-s1D), suggesting that a low levels of IIB is likely responsible for the low amount of IIB filaments in IIA KO cells, rather than their inability to form filaments in the absence of IIA.

6. The conclusions that IIA triggers RLC phosphorylation and that IIB can form filaments with unphosphorylated RLC are so extreme that their validation requires comprehensive analyses, extensive quantifications using proper normalizations to myosin levels, as well as alternative approaches. At the present state of knowledge, it is hard to imagine that myosin filaments would form without RLC phosphorylation. The idea that myosin II can somehow trigger a feedback loop to activate RLC phosphorylation is theoretically possible, but requires solid evidence, which is not provided here. The observations instigating the above conclusion are more likely explained by some technical issues. For example, IIB filaments may contain double-phosphorylated RLC, which is not recognized by the used antibody, or the amount of IIB is too low, or there is a problem with signal detection. The authors show that the pRLC level does increase linearly with overexpression of IIB although with a different slope compared with IIA. However, data in Figure 4-s1B and 4-s1E must come from different experiments, thus making pRLC staining intensities incomparable.

7. The significance of using the IIA mutants is hard to understand. First, it is not clear what mutants are meant in different statements, e.g. mutants with "prolonged NM IIA dwell times in the minifilaments" (p. 14, l. 313), or "mutants, in which the disassembly of the NM IIA hexamers was blocked" (p. 14, l. 315), or "constitutively active NMHC IIA construct" (p. 14, l. 317). They all seem to refer to mutants with impaired disassembly (ΔIQ2, ΔNHT and 3xA). Yet, they are contrasted to each other (p. 14, ll. 315-317 and in Figure 3-s2). Second, what is the idea behind using the ΔACD mutant? What does it reveal? Third, none of these mutations affects motor activity of IIA. They only affect its polymerization. Given that the mathematical model considers only motor activities of IIA and IIB, how do these experiments test the model? Finally, since IIB was not a part of these experiments, how did authors arrive to the following conclusions from these data: "This demonstrates that spatially and temporally balanced ratios of active NM IIA and NM IIB hexamers in heterotypic minifilaments are mandatory to adjust the contractile output in SFs and the relation between tension and elasticity. Therefore, the specific biochemical features of the isoforms and not their overall expression are important for the generation of tension and elastic stability, respectively." (p. 14, ll. 318-322) and "the specific intracellular force output is precisely tuned by the ratio and dwell time of individual NM IIA and NM IIB hexamers in the heterotypic minifilaments." (p.22, ll. 518-520)?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Distinct roles of nonmuscle myosin II isoforms for establishing tension and elasticity during cell morphodynamics" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission have agreed to reveal their identity: James R Sellers (Reviewer #1). Please note that because the original reviewer #2 was unable to evaluate the new submission, the manuscript was reviewed by another expert in the field.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the reviewer #1 found the revised manuscript significantly improved, the reviewer #2 stated that large part of the data are confirmatory and that the most novel findings were not sufficiently well presented in the manuscript. Thus, the manuscript should be extensively rewritten to address the points raised by reviewer #2.

1). The study should be put better into a context of earlier work on NMII isoforms. The parts of the manuscript presenting confirmatory data should be shortened, and the most novel findings should be better explained to make them also accessible for a non-specialist reader. Making the manuscript shorter and more focused will increase its impact.

2). Also the 'Introduction' should be shortened and focused only on the published literature. Instead of extensively discussing new findings in the 'Introduction', these should be only briefly mentioned in the end of 'Introduction'.

Reviewer #1:

I am satisfied with the presentation of the data.

Reviewer #2:

This manuscript, previously revised in eLife, but not by this reviewer, describes the different effects of NMII isoforms in mechanical adaptation to different microenvironments. The approach consists of U2OS cells depleted of each specific isoform by CRISPR/CAS9. Based on the rebuttal, the authors had, in their previous version, data on NMIIA mutants as well as FRAP data, which have been removed from this iteration. Instead, the authors provide modeling to show that NMIIA is the "first responder" in generating tension; whereas NMIIB stabilizes elastic tension. The authors propose a novel role for NMIIC in establishing tensional homeostasis.

This manuscript contains important information regarding the role of NMII isoforms in cellular responses. The manuscript seems have changed mightily from its previous incarnation. Insomuch as this reviewer did not see the previous version, what follows is an appraisal on the current version.

Overall, the manuscript is well done, and experimentation is of high caliber. However, the study takes a long time getting into actually novel data, and its amount is limited. A significant part of the manuscript is confirmatory, including the role of NMIIA in force generation (Jorrisch et al., 2013, PMID 23616920, for example), adhesion elongation (many reports); and of NMIIB in adhesion "consolidation". The other reviewers asked about the relative amount of NMII isoforms, which was a good point. The authors have solved this by overexpressing NMIIB in NMIIA KO cells, which does not restore any effect observed in these cells, which actually confirms that the ability of NMIIB filaments to form is limited in these cells.

The authors engaged in an argument with the previous reviewers on the importance of the levels of NMII isoforms. While I'm convinced by the argument of the authors (NMIIB overexpression in NMIIA KOs is a good experiment), I'm curious as to more NMIIC has effects on the elastic recoil observed in the last experiment of the paper. Also, include mass spec data as in Ma et al. (2010) would be useful.

The novel part starts in figure 3, in which the authors observe a subtle change in the bending of actin bundles in cross-shaped patterns. The graph is quite counterintuitive. A and D look similar, and the graphs look similar. This is understandable. However, B and C (NMIIA and NMIIB Kos) are somewhat similar, yet the graphs are opposite, with dTEM converging on Rmin on NMIIA KOs; and away from Rmin in NMIIB KOs. The text explanation (pages 10 and 11) works, but the representative cell is head scratching.

I haven't seen the RLC phosphorylation data, but I'm intrigued. The manner the previous reviewers wrote about it makes it hard to understand what was going on. I'm guessing the authors will pursue this in future work.

In Figure 4, the authors propose a model that correlates dynamic tension and elasticity with actomyosin crossbridging. They propose that the short duty ratio of NMIIA correlates with the generation of dynamic tension; and the higher duty ratio of NMIIB explains the elastic behavior of the actomyosin arches. While it is entirely possible this may be true, the cellular behavior of myosin II chimeras (e.g. as published by Tony Means and Rick Horwitz) is not dominated by the duty ratio (which depends entirely on actin-myosin binding); but by myosin filamentation, which depends on the tail domains of the heavy chains. I would require the authors to integrate this in their model, which may be correct theoretically, but would hardly explain the behavior of the cell outside a cross-shaped pattern.

The most interesting argument is the potential role of NMIIC in the mechanical response of cells. The authors seem to consider NMIIC as an oscillatory dampener that controls force relaxation. However, this is a very undeveloped part of the manuscript, which merits further exploration. I don't think this is particularly easy.

In summary, while I find a lot of merit in this paper, I find that more than half the study is confirmatory, and the novel part will appeal only to hardcore specialists in the field. Thus, I am not convinced it represents a sufficient general advance for publication in eLife.
