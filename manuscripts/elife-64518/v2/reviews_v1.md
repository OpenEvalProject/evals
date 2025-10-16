# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64518.sa1](https://doi.org/10.7554/eLife.64518.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Antibiotic resistance evolves rapidly in response to treatment. Resistance sometimes evolves predictably through the accumulation of specific mutations. One way to limit evolution is to develop other molecular compounds that target the WT protein and that remain efficient against these resistance mutations while exploiting the deep knowledge of the traditionally targeted pathways. Here, the authors use this strategy to identify potential compounds that help delay the evolution of antibiotic resistance in bacteria using a combination of computational, biochemical and experimental evolution approaches.

Decision letter after peer review:

Thank you for submitting your article "Development of evolution drugs -antibacterial compounds that block pathways to resistance" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by George Perry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Antibiotic resistance can evolve rapidly and thus reduces the usefulness of many drugs that are otherwise effective. The development of new drugs that could slow down adaptation to antibiotics would significantly extend the life expectancy of current treatment strategies. Here, the authors identify, through computational analyses and experimental work, new chemical compounds that target the dihydrofolate reductase of E. coli, the known target of the common antibiotic trimethoprim. Contrary to trimethoprim, a new lead appears to lead very slowly to resistance. The authors present their strategy and findings as a way to develop 'evolution drugs'.

Essential revisions:

The reviewers raised many points that would need to be addressed for the manuscript to be considered further. I outline here the critical elements that are essential to address.

1) The new compounds are presented as new antibiotics in the context of medical application but they are active against the human DHFR and thus lack selectivity, which is a major issue in antibiotic development. The reviewers agree that because of this, this work could not be published under the theme of inhibitor development. It could potentially be rewritten as a model system for the examination strategies to delay the onset of resistance.

2) The number of mutants sequenced is not large enough to rule out the possibility that resistance can emerge through mutations in folA. In addition, some of the mutants come from the same adapted populations, which means that they are not an independent sampling of resistance mutants. The claim that resistance mechanisms are different from that of Trimethoprim and do not involve folA itself is therefore not supported.

3) Some of the information that would have been useful for the interpretation and evaluation of the current manuscript is to be published in an upcoming publication. It would be important for the reviewers to have access to this information. This would be possible for instance by providing a link to a preprint with this other paper.

4) The concept of evolution drug needs to be better defined to make sure the reader understands its scope and what it is bringing to the field.

We also transmit the detailed comments below.

Reviewer #1:

I cannot comment on the sections of the manuscript related to compound search and identification.

My general comment is about what makes an evolution drug exactly. From the definition given, it is a drug that works on mutants that are resistant to other drugs. Most antibiotics that interact slightly differently with the same target, or that have other modes of action altogether would therefore be evolution drugs? Since this is the aspect of the paper that makes it very original, I would need to better understand what this concept is, what it is not, and what novelty it brings.

My second critical comment regards the evolution experiment. I could not find exactly how many independent lines were evolved to resist the novel compound and how many were sequenced. The methods mention evolution in 96 well plates but from the results, it seems that only two mutants were sequenced. I believe that this is not enough to claim that this drug will not select for mutations in fola. To be able to show this, enough independent clones have to be sampled and sequenced to show that the space of resistance mutations has been completely sampled.

My third critical comment is that it seems that CD15-3 selects for mechanisms that lead to resistance to TMP as well, which is not something that you want for an evolution drug. This means that resistance to CD15-3 brings resistance to TMP as well if I understand well. How does this fit within the concept of evolution drugs? This would seem to make it a rather inefficient one.

Detailed comments: Panels of Figure 7 would need to be better labelled.

Many barplots are used to show estimates, for instance in figure 4. This is a representation that poorly represents the data. (https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128). I recommend alternatives are used and all data points are shown in addition to error bars (which are not defined here).

Reviewer #2:

The authors present a computational workflow that convincingly demonstrates the design and optimization of inhibitors to a key antibiotic target, such that the development of inhibitor resistance is clearly delayed. The experimental determination of inhibition in vitro, in cells and during the course of one month under evolutionary pressure with the new compounds was convincing. Unfortunately, the new inhibitors inhibit human DHFR more strongly. They would be toxic/lethal.

The authors could examine the inclusion of negative design (against inhibition of the human enzyme) in their workflow.

Since trimethoprim resistance is at the center of this research, and that the authors aim to develop an "evolution drug", TMP-specific resistance should be described in greater depth. The specific context and reference given in the 2nd/3rd paragraphs of the introduction are: "However, due to rapid emergence of resistant mutations in DHFR, the development of drug resistance to antifolate antibiotics belonging to any of the above-mentioned classes presents a significant challenge (Huovinen et al., 1995). Both clinical and in vitro studies have shown that accumulation of point mutations in critical amino acids residues of the binding cavity represent an important mode of trimethoprim resistance. Mutations conferring resistance in bacteria to anti-DHFR compounds are primarily located in the folA locus that encodes DHFR in E. coli (Oz et al., 2014; Tamer et al., 2019; Toprak et al., 2012) making DHFR an appealing target to develop evolution antibiotic drugs. » This view is now known to be incomplete. Crucially, the folA-related DfrA enzyme family should be introduced (as comprehensively described in Sánchez-Osuna et al., Microbial Genomics 2020;6) because clinical TMP resistance is more complex than point mutations to FolA as described by Huovinen. The intrinsically TMP-resistant DfrB family of DHFRs should also be mentioned as being part of the problem, although this work would not directly apply to it.

As a result of the new finding that TMP resistance is very diverse and does not result only from the recent evolution of point mutations as was previously thought, the approach presented here should be qualified. In the introduction (3rd paragraph): "In this work, we developed an integrative computational modeling and biological evaluation workflow to discover novel DHFR inhibitors that are active against WT and resistant variants. » should qualify the resistant variants as being specifically directed to the point-mutated variants only, not all resistant variants that are genetically diverse.

It thus follows that the premise, as currently stated, is somewhat misleading. The introduction discusses clinical observation of antibiotic evolution. However, the point mutations under study are not particularly relevant to the natural evolution of TMP resistance (prior to introduction of TMP), or even its clinical evolution. This is clearly shown by the modest TMP resistance offered (Figure 2C). As described under Methods, section "Construction of binding affinity prediction model": "An evolutionary study (Oz et al., 2014; Toprak et al., 2012) of TMP resistance found that three key resistance mutations P21L, A26T, L28R, and their combinations constitute a set that recurrently occurred in two out of five independent evolution experiments, and their order of fixation in both cases was similar." This set of mutations constitutes a simple model system of in vitro evolution. This does not remove from the success of the inhibitor discovery and delay of onset of resistance, but it must be made clear that the premise is limited to in vitro evolution as a model of natural evolution, from the Abstract and throughout the body of the work.

Following Figure 1: "…Listeria grayi (L. grayi) and Chlamydia muridarum (C. muridarum) again showing highly significant correlation between predicted and experimental values (Figure S7), demonstrating broad predictive power of the method". To highlight the relevance of the study, the choice of Listeria grayi and Chlamydia muridarum should be rationalized. The native resistance of L. grayi should be expressed; the choice of C. muridarum is not so clear. Importantly, what is their evolutionary distance with E. coli FolA? Therefore, do they demonstrate broad predictive power, as stated, and does it suggest that they are broadly efficient potential antibacterial leads (above Figure 3, regarding inhibition by CD15 and CD17)?

The authors chose to characterize the in vivo IC50 of the compounds. Since the role of compounds is to inhibit bacterial growth completely, minimal inhibitory concentration (MIC) and minimal bactericidal concentration (MBC) might be more relevant in this context and could be determined for the most interesting compounds, and different targets.

Suggestions and typographical:

– A recent review on 'classical' searches for inhibitors could be cited in the 2nd paragraph of the introduction: Wróbel, Arciszewska, Maliszewski and Drozdowska The Journal of Antibiotics volume 73, pages5-27(2020)

– Confusion in describing the activity test in vitro: in the body the authors describe fluorescence at 340 nm (Figure 2) whereas Methods describe the decrease in absorbance at 340 nm. Figure 2A: Which is the curve of TMP?

– Table 1: significant digits on values are not uniform – should be two.

– E. coli and in vitro are not routinely italicized.

– CD15-3 or CD15.3.

– Table 1: Ki of TMP should be included for comparative purposes.

– Table 2: IC50 values should have no more than 2 significant digits. TMP should have STD.

– Figure 7C: Concentration in µM, not µm.

– Figure 9. The order of the panels should be the same as the order of the E. coli variants presented in panel E. In each DIC image, there should be a size bar (ex. 5 µm).

Reviewer #3:

In this manuscript, the authors present a strategy to identify new antibiotic compounds that block DHFR -- the target of trimethoprim -- in a way that should still work in DHFR variants carrying common trimethoprim resistance mutations. Their strategy consists of a computational approach to select promising candidates from known databases, followed by an experimental optimization and validation of the identified compounds. Interestingly, the first computational steps already narrowed down large chemical databases into a few relevant compounds, which are then shown to be efficient DHFR inhibitors in the experimental tests. Moreover, evolution of resistance to the resulting compound is shown to be much slower than resistance to trimethoprim.

The authors should address the following points (roughly in order of importance):

– An upcoming publication, in which a second molecular target of compound CD15-3 is revealed, is mentioned several times. It is slightly frustrating that these results, which may be key to understanding some of the phenomena reported in the present work (see below), are not included in this work. Why can this information not be included in the current article?

– Apart from non-synonymous mutations in folA, a common alternative way to evolve trimethoprim resistance is to overexpress DHFR. This happens in typical evolution experiments and in the clinic, for example through mutations that affect the folA promoter (see e.g. Toprak et al., Nature Genetics, 2012); this could also happen via duplication (or further amplification) of the folA gene. Figure 6 shows that, indeed, for the CD15-3 compound, overexpressing DHFR would actually allow the cell to recover from the effect of the compound. It is thus quite striking that no overexpression of DHFR seems to occur in the evolution experiments shown in figure 7A, where no mutation in folA fixes. The authors should comment on this in more detail. Could the other (mysterious) target of the drug explain this?

– How does the absolute value of the IC50 of the new compound compare with that of trimethoprim?

– The manuscript has a considerable amount of technical details in the main text, which makes it unnecessarily long and sometimes difficult to follow the main ideas. A shorter main text with fewer figures would considerably increase the clarity and accessibility of this work for non-experts (the details could be shifted to a supplement or appendix).

– In figure 3, a more explicative caption title would help the reader to quickly grasp the main conclusion from this figure.

– It is not completely clear in how far the approach presented in this work can be extended to other antibiotics and their resistance targets. It would be interesting to discuss this in more detail in the manuscript.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Development of antibacterial compounds that block evolutionary pathways to resistance" for further consideration by eLife. Your revised article has been evaluated by George Perry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers and I appreciate the numerous modifications that were made to the manuscript. You will find below some comments from the reviewers. I will not reproduce them here because I believe they are all important and would need to be addressed. Also, I appreciated the additional experiment to isolate resistant mutants (Line 464). However, all mutants isolated come from the same culture, so it is not possible to know whether they are independent mutants. This experiment suffers from the same limitation as the previous experiment. Mutants from independent cultures would need to be isolated for them to be truly independent. The claim that resistance to CD15-3 does not evolve through mutations in folA would need to be expressed as < resistance to CD15-3 is less likely to evolve through mutations in folA> rather than <does not evolve through mutations in folA>. Saying that it does not happen would require a comprehensive analysis of mutants. The first comment of reviewer #3 also relates to this point.

Reviewer #2:

The authors made important improvements to the manuscript, addressing many key issues. In particular, demonstration of lack of inhibition of the human DHFR by CD15-3 is encouraging. This point should be highlighted by including the maximal concentration tested in footnote (b) of Table 1. The overall strategy is now better contextualized and has been strengthened by the additional data included in this version of the manuscript.

It is indeed interesting that (lines 712…) "the CD15-3 inhibitory activity extends beyond the DHFR variants that were initially selected as targets for structure-based design and that "unplanned" D27E and W30 mutants get inhibited with WT like efficacy." The design strategy included known single/double mutations at positions 21, 26 and 28, indicated in Table 1; in the case of CD15-3 only one point mutant Ki was assessed. The Ki of CD15-3 for the other mutants used in the design strategy (Table 1) must be included, otherwise, there is no direct validation of the strategy. This is made obvious by the unclear conclusions of the cellular inhibition results, where the authors go to great lengths to attempt to isolate the effect of the inhibitors on DHFR in the cells (Section 'Target validation in vivo'). Therefore, validation of the strategy on the direct targets used in the design, the mutant DHFRs, should be done.

Reviewer #3:

The authors made a substantial effort and addressed most critical points in the revision. It is also very helpful that they made the preprint of the related article available online. However, there are a few remaining points that still need to be addressed:

– In their response, the authors speculate that, because of the second target of the compound, overexpression of folA would be a less optimal evolutionary solution. This is vague and still not clear because the data show that overexpression of folA is an easy way to increase resistance, irrespective of any other drug target. Moreover, in the second article they show that overexpressing the other target (folK) leads to even higher resistance to the drug. Thus, there is a similar issue: Why do solutions that overexpress this target (which should be easily accessible by promoter mutations or gene amplification) do not appear in the evolution experiments? I understand that it may not be possible to elucidate this in a reasonable time frame, but it should be clearly stated and discussed in detail in the manuscript (not just in the response to the reviewer comments). This point is important because it changes the main take-home message from "It is not possible to evolve resistance to the new compound" to "There are the same straightforward ways to evolve resistance to the new compound as for trimethoprim but (for unknown reasons) they are not followed in evolution experiments."

– Another point that is addressed in the response to reviewers but still needs to be transparently stated and discussed in the revised manuscript is how the IC50 of the new compound compares to that of trimethoprim. The most helpful would be to show the dose-response curves for the new compound and for trimethoprim in the same plot with absolute concentrations on the x-axis. A similar plot that directly compares the effect of overexpressing folA on both dose-response curves would also help.
