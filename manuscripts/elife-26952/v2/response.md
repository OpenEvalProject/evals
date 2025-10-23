# Author response - Round 1

Authors:
- Martin Borch Jensen ([ORCID: 0000-0002-8875-0345](https://orcid.org/0000-0002-8875-0345))
- Yanyan Qi
- Rebeccah Riley
- Liya Rabkina
- Heinrich Jasper ([ORCID: 0000-0002-6014-4343](https://orcid.org/0000-0002-6014-4343))

## Response text

DOI: [10.7554/eLife.26952.025](https://doi.org/10.7554/eLife.26952.025)

Essential revisions:

(major concerns):

The key weakness regards the study's (implied) inference on the role of lasting FoxO activation as the longevity mechanism. Epistasis analysis is needed to test this idea.

The important required study is to conduct mtUPR (in any way) in FoxO-null epistasis. Alternatively, the authors could test the effect of co-expression of the OTC construct and RNAi to FoxO, using the gene-switch system. This approach allows the genotype without RU to serve as its own co-isogenic control. One needs to measure the longevity of the OTC expression alone, using geneswitch again, to confirm there is a longevity benefit in that period. And, one should do the same by driving the FoxO RNAi with the same geneswitch (which should do very little to the survival).

We agree that this is an important experiment. Per the reviewer’s suggestions, we have now carried out duplicate lifespan experiments where DaGS was used to drive ΔOTC expression in a FoxO null background (the foxoΔ94/21 transheterozygotes already described in the manuscript). In parallel, we replicated the DaGS x ΔOTC lifespan experiment already included in the paper. In support of our model, developmental mitochondrial stress leads to a significant shortening of lifespan in FoxO null flies, in sharp contrast to the lifespan extension observed in normal flies. The FoxO null data is presented in the revised Figure 2D, alongside statistics for the positive control in 2G. The graph for the positive control is shown in Figure 2—figure supplement 2. Combined with our observations of drastically reduced survival through developmental mitochondrial stress in FoxO nulls (now in Figure 2—figure supplement 1), this solidifies FoxO activity as a necessary factor for the lifespan extension elicited by developmental mitochondrial stress.

Essential revisions:

(other concerns):

1) Are phenotypes due to a UPRmt stress response per se? How much is due to a more general response caused by mitochondrial dysfunction. This is unclear because of the nature of mitochondrial stressors. ND75 knockdown will cause mitochondrial dysfunction (possibly affecting ATP, Ca2+, ROS, NADH, NAD+ etc.). The ΔOTC mutant in flies also severely impacts mitochondrial function (ATP, oxygen consumption etc.). Therefore, it is not clear that a UPRmt or some other type of mitochondrial stress response is being studied. Presumably studies in worms, where chaperone up-regulation has clear linkage to UPRmt provides the inspiration, but this is not yet in flies. For example, ΔOTC causes ETC dysfunction in flies (Pimenta de Castro et al. 2012). If this is not true for this system, then some functional data are required, or the description of the model should be modified.

We agree that distinguishing general mitochondrial stress from a more specific UPRmt is difficult in any organism. In our original manuscript, we decided to follow the nomenclature of previous studies (Pimenta de Castro et al. 2012, Owusu-Ansah et al. 2013). However, to our knowledge (and as suggested by the reviewers), all methods of inducing the UPRmt in any organism leads to mitochondrial dysfunction of some sort. It does not yet seem clear whether and which such dysfunctions should be classified as causative or part of the UPRmt. For example, some parts of the UPRmt have been characterized as ROS-dependent. We originally chose to define the UPRmtas any response occurring in two distinct types of mitochondrial proteostatic stress, but we agree with the reviewers’ point that the Drosophila UPRmt remains imperfectly described. We have thus rewritten several parts of the manuscript to refer to ‘mitochondrial stress’ rather than UPRmt.

2) Is the PGAM5/ASK/JNK signaling pathway a bona fide UPRmt pathway (analogous to the ATFS-1)? If a chaperone important in the UPRmt response affecting proteostasis directly was chosen as a marker rather than a gene involved in the immune response, then the relation of this new signaling pathway to UPRmt could be better assessed. Either a more specific UPRmt output marker should be used, or discussion of UPRmt should be reserved for the Discussion.

3) In the same vein, it is unclear whether the canonical markers of the UPRmt, such as Hsp60, Hsp10, mortalin (mt-Hsp70) and the ClpP protease are induced under the conditions used to activate the UPRmt in this study. The authors should comment on this, and provide a possible explanation for this apparent disparity.

Although the fluorescent reporters available for hsp-6 and hsp-60 in C. elegans respond strongly to induction of the UPRmt, Drosophila studies (Pimenta de Castro et al. 2012, Owusu-Ansah et al. 2013) have shown only moderate (~1.5-fold) induction of these genes. For this reason, the markers mentioned by reviewers were not included in the set of 3-fold upregulated genes in Figure 1A, and we chose metchnikowin as our marker for subsequent screens due to its higher dynamic range of induction.

To address the pertinent comments by the reviewers, we have added a supplement to Figure 1 (Figure 1—figure supplement 1) showing that expression of ΔOTC using the regime reported in Owusu-Ansah et al. leads to a similar upregulation of hsp60, hsc70-5 and hsp10. We further show that this induction is blocked in the absence of PGAM5, bsk or FoxO.

4) The exact dosages of RU456 used in the gene-switch experiments should be listed in the figure legends.

200 μm RU486 was used throughout, and this has now been added to figure legends.

5) The link between UPRmt and longevity is not yet settled, and while this work provides important advancements, the authors will do well to tone down the enthusiasm with which they link expression of the OTC construct with UPRmt induction. OTC induces other genes as well (such as antimicrobial peptides). Therefore several bold statements such as the subheading "UPRmt-mediated longevity is not caused by improved adult immune function, or by changes to the microbiome" and "Developmental UPRmt affects the metabolic state of adult flies and leads to persistent FoxO" or (based on point 1 above), "Of the two methods initially used to induce the UPRmt, we opted to use ΔOTC for further experiments to avoid potential secondary effects of inducing ETC dysfunction" should be modified to reflect the fact that the results observed are due to OTC expression and not necessarily all due to the UPRmt.

As noted in our response to comment #1, we have rewritten parts of the manuscript to refer to mitochondrial stress rather than UPRmt. In response to the comment that “OTC induces other genes as well (such as antimicrobial peptides).”, we note that Pellegrino et al. 2014 showed that AMPs are induced by ATFS-1 activation even absent mitochondrial stress, and were thus described as part of the core UPRmt in C. elegans.

6) ADaGSxOTC itself yields less than 50% eclosion. Survivors of this cohort may live longer because of frailty selection: weak larvae that would produce shorter-lived adults do not eclose. Some rescue-type data (Figure 2C) argues against this potential confound, but the evidence is thin.

This is an important concern, and indeed activation of the UPRmt by constitutively active ATFS-1 in C. elegans also leads to reduced survival through development (Cole Haynes, personal communication). However, our new FoxO null lifespan data shows that FoxO activity not only correlates with, but is required for lifespan extension. It is pertinent to this specific concern that while FoxO null mutants show strongly reduced survival through developmental ΔOTC expression (Figure 2—figure supplement 1), even the survivors showed reduced adult lifespan (Figure 2D). The same is true for PGAM5 nulls (Figure 2C and Figure 2—figure supplement 1).

7) UPRmt induced in adults activates FoxO, but such cohorts are not long-lived when RU is constantly applied. That FoxO is only transiently activated when RU is given for just one week is not a satisfactory explanation.

We apologize for not making this clear in the original manuscript, as indeed the transience of FoxO activation by mitochondrial stress does not explain why continuous mitochondrial stress in adults does not extend lifespan. Our interpretation is that the negative effects of chronically impairing mitochondrial function through expression of ΔOTC has detrimental effects that overshadow the improved proteostasis conferred by activating the FoxO pathway. This is consistent with observations by Pimenta-Castro et al. 2012, who show impaired mitochondrial function and survival with chronic adult ΔOTC expression. In the case of developmentally expressed ΔOTC, on the other hand, the mitochondrial stress is eliminated in adults while FoxO activation is retained chronically.

8) The data with HPD is unclear. Presumably, HPD resets both this TF and the lifespan, and this is used to infer causality between the induced longevity and FoxO activation. But in the sole survival experiment to this point (Figure 5F), the shape of the plots is a concern: they are too linear, suggesting that age-independent mortality is the overriding cause of death. This can mask any potential impact on age-dependent mortality; and there are no data to rule this out (or in). Perhaps the HPD is toxic, and all flies die for reasons besides aging. There are no other data to address the relevance of activated FoxO (by any of the interesting, observed mechanisms) as relevant to the larval UPRmt impact on adult longevity.

As mentioned above, we have now obtained additional evidence that FoxO activity is required for lifespan extension by developmental ΔOTC expression (new lifespan data for null mutants). We have edited the manuscript to merely note that the lack of extension on HPD is consistent with our demonstration that HPD blocks FoxO activation and with the fact that FoxO is required for lifespan extension by developmental mitochondrial stress.
