# Peer review - Round 1

Editors:
- Gene Yeo, University of California, San Diego , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10288.029](https://doi.org/10.7554/eLife.10288.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "An Extensive Program of Periodic Alternative Splicing Linked to Cell Cycle Progression" for peer review at eLife. Your submission has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing editor (Gene Yeo), and three reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors identify widespread periodic changes in alternative splicing (AS) (>1000 AS events) that are coordinated with stages of the cell cycle, noticing that periodically regulated intron retention is prominent. The authors discover that SR protein kinase CLK1 is subject to cell cycle-dependent changes and appears to play a central role in the control of AS during cell cycle.

Essential revisions:

1) There were major concerns with regards to the poor overlap of the two pipelines (VAST and MISO) in the identification of AS events. While the reviewers and myself appreciate that the point of the manuscript is not a systematic comparison of both software, the authors are expected to explain the rationale for decisions taken which likely impact the interpretation of the results. Greater detail in the bioinformatics analysis is expected in the revision. Also, why are both tools used? And given the relatively poor overlap, is the use of either or both of these tools justified?

2) A more complete treatment of the contribution of other splicing factors to cell cycle AS is necessary. I do not believe it has to be exhaustive, but in its present form, the manuscript led to concerns by the reviewers that CLK1 is not necessarily a clear outlier (and therefore candidate) in terms of its regulation, compared to other factors. CLK4 modification and levels should be certainly verified by Western blot analysis. Based on these new results (in the revision), the authors are encouraged to alter/broaden their title (as suggested by Reviewer 3 as well).

3) The authors should address the major concerns of Reviewers 1 and 2 with regards to why is the CLK1 inhibitor used (rather than depletion) and address clearly their interpretation of specificity since the inhibitors also target CLK4.

4) The authors should address queries with regards to the PTC-induced degradation of AURKB (Reviewer 1) and known IR events (Reviewer 3).

Reviewer #1:

In this interesting paper, the Blencowe and Wang labs investigate the role of Alternative splicing (AS) during cell cycle progression.

First, Dominguez and co-authors carried out a sequence analysis of the human transcriptome during two continuous cell cycles. This analysis resulted in the identification of widespread periodic changes in AS that are coordinated with specific stages of the cell cycle. In particular, they identified 1,747 AS cell cycle-dependent AS events in 1,293 genes. They found that periodically regulated intron retention is the predominant event.

The authors next focused on the SR protein kinase, CLK1 and found that its expression also fluctuates during the cell cycle. These and other results suggested that CLK1 might have a specific role in regulating cell cycle-dependent AS. Following this, the authors went on to identify endogenous CLK1 AS targets using an RNA-Seq approach. Altogether, these data suggests that temporal regulation of splicing by CLK1 is critical for cell cycle progression. Finally, the authors conclusively show that CLK1 is indeed required for normal mitosis and cell proliferation. The authors put forward a model whereby CLK1 has an essential role in controlling cell cycle-dependent AS.

Defining a central role for CLK1 in the regulation of AS during cell cycle is of importance. The authors also nicely show that the levels of CLK1 are indeed self-regulated and depend on its own catalytic activity. The main targets of CLK1 are SR proteins, yet only in the case of CHEK2 pre-mRNA splicing, it is shown that the effect of CLK1 operates via SRSF1. It would be important to show some evidence that links the role of CLK1 in cell cycle regulated splicing with a particular SR protein/s.

In summary, this is a very good study that represents and important contribution to our understanding of Alternative splicing and cell cycle progression.

Specific comments:

1) In the Abstract and again in paragraph two of the Introduction, the authors refer to periodic regulation of gene function at the levels of transcription, protein modification and degradation, etc.; however, they ignore the role of mRNA translation. There are several papers describing the regulation of mRNA translation during mitosis, which would enrich the Discussion section. Some of these include:

Stumpf et al. (2013) The translational landscape of the mammalian cell cycle. Mol Cell. 2013 Nov 21;52(4):574-82. PubMed PMID: 24120665.

Maslon et al. (2014) The translational landscape of the splicing factor SRSF1 and its role in mitosis. eLife. 2014 May 6:e02028. doi: 10.7554/eLife.02028. PubMed PMID: 24842991.

2) Is there any overlap in those genes found here to be regulated at the AS level and those previously reported to be regulated by mRNA translation?

3) There seems to be independent regulation of transcriptionally and AS-regulated genes during the cell cycle. Are those genes that show an overlap (133) more likely to be regulated by the kinetic control mode of AS regulation? In other words, are those genes preferentially regulated by the processivity of RNA pol II?

4) On Figure 1E, has the PTC-induced degradation of AURKB been experimentally determined?

5) On Figure 3, why is a CLK1 inhibitor preferred to a depletion of CLK1 (either via CRISPR or siRNA approach)?

6) On Figure 3, is the CENPE AS also regulated by SRSF1, as is the case with the CHEK2 pre-mRNA?

Reviewer #2:

This manuscript by Dominguez et al., describes a thorough and important analysis of transcriptome changes during the cell cycle, with particular emphasis on alternative splicing. This analysis then motivates the authors to investigate a potential role of the kinase CLK1 in regulating cell cycle splicing and progression, and its possible link to cancer. If fully substantiated, this work would add tremendously to the growing body of knowledge regarding how different cellular growth conditions impact splicing. However, some additional analysis and important controls are required for this manuscript to achieve its full impact.

Firstly, much of the analysis of the RNA-Seq data is poorly defined. Why were VAST-TOOLs and MISO both used and what is the advantage of this? What is "Periodic score" in Figure 1—figure supplement 1B and C? The authors may feel these are readily apparent, but readers should not have to dig deeply through the Methods to understand the first figure. More importantly, Figure 1A should either be replaced with a version that gives raw PSI, or a version with raw PSI should be included in the supplement. Use of the "row normalized" method raises concerns that many of the changes observed in AS events are modest and potentially not of biologic significance.

Secondly, the justification for focusing on CLK1 is not clear. While Figure 3 and Figure 4 certainly support a role of the CLK family in cell cycle splicing, Figure 2 is not convincing that CLK1 is a clear outlier in terms of its regulation. A quick glance through the GE values in supplemental table 1 indicates that genes encoding several SR proteins vary throughout the cell cycle. Have SR proteins other than SRSF1 been analyzed by Western? Moreover, CLK4 should be certainly tested by Western – due to it being a target of TG003 and KHCB-19 (see next point).

Finally, there is significant concern that both the inhibitors used target CLK4 as well as (or more potently than) CLK1. The authors should either conclusively rule out a role for CLK4, or broaden their conclusions to acknowledge a potential role for this family member.

Reviewer #3:

In this work the authors create a genome wide map of oscillating alternative splicing events, and identify CLK1 as a major regulator of a subset of these oscillating events. Roughly, two thirds the paper are focused on exploring the regulatory role of CLK1 through a series of elaborate and thoughtful experiments after establishing it plays a major role in regulating oscillating AS. We found relatively few and mostly minor concerns regarding these later sections. Most critical concerns regard the first, genome wide, analysis.

1) The two pipelines used, based on VAST and MISO, are basically in severe disagreement with respect to which AS events are oscillating. Figure 1—figure supplement 1F shows that not only is the number of events detected very different (244 vs 513) but the overlap of those is a mere 27% or 12%(!). This is coming from two pipelines that use the same downstream procedure to check for oscillation and differ only in their approach to quantify the raw PSI values fed into the pipeline. This poor overlap puts the entire genome wide mapping presented here into questioning. Figure 1—figure supplement 1G may have been added to address this concern (it's not explained) but actually does little to alleviate this concern: Figure 1—figure supplement 1G basically shows that the correlation between VAST and MISO based PSI values are much better for the same condition (diagonal) than for different conditions when looking across the >4K events quantified. That is actually to be expected: most events are either highly included or highly excluded. Such highly included/excluded events would (a) make the extreme values dominating the correlation coefficient and (b) would make the majority of cases that are generally not changing and thus both methods agree on. In fact, a closer look at Figure 1—figure supplement 1G shows the average PSI correlation between VAST and MISO for the same condition (diagonal) is ~0.55 which is again troubling (btw, setting the dark red color for 0.55 is misleading). Some suggestions that may help alleviate the discrepancies between the two pipelines are given below.

Related to this: why does Figure 1—figure supplement 1D contain only 513 events but Figure 1A contains 1747 events? If Figure 1—figure supplement 1D is VAST's list why does Figure 1—figure supplement 1F show 513 for MISO?

2) Basic "normalized PSI" (subheading “Identification of periodic AS”) means we are only looking at relative changes of PSI. This may introduce a lot of variability/noise to the analysis and may contribute to the substantial differences between the results from the two analysis pipelines (see above). The authors may be better off screening for events for which (a) min(max(PSI) > VAL1) and (b) max(PSI) – min(PSI) > VAL2. Similarly, increasing the threshold on number of reads per event to be included could help. For example, using VAL1=VAL2 = 20% could help avoid fluctuations that may just appear as periodic or changing dramatically in a relatively small/insignificant range.

Related to this: the authors do not explain how events are screened for coverage across the experiments.

3) The method for detecting the oscillating AS events and its effect on their results is not discussed or evaluated. Specifically, the authors use 7 previously characterized profiles from GE analysis. It's not clear whether the same kind of profiles is the best choice for analyzing periodic AS. For example, profiles 3,4 are similar in phase but one has a wider shape – why would that be the best fit for AS profiles? It seems reasonable to at least compare the results from this approach to an unbiased approach where the entire set of AS events are clustered with no specific periodic profiles and then the most prominent periodic profiles are extracted or executing a more directed search against theoretical periodic profiles.

4) More convincing/exhaustive search of RBPs that may contribute to cell cycle AS:

While there's significant overlap between CLK1 inhibitor AS events and periodic cell cycle events, this only explains a fraction of all the periodic events they find. It would be good to acknowledge at least that there are likely other factors out there that contribute to this program of AS. The authors should discuss how much of the oscillation signal is explained by CLK1. The WB data from Figure 2A is not exhaustive, but it is convincing for those factors tested. It should be straightforward to supplement this analysis by applying their pipelines and RNA-seq data to report known/suspected splicing factors and/or RBPs that change at the level of GE or AS. Any changes found in this analysis could potentially contribute to the large AS program they observe beyond CLK1 regulation.

5) Analysis on IR/AS-PTC introducing events:

Figure 1D/E suggests that periodic IR can affect transcript expression levels (probably by the introduction of PTCs) in the case of AURKB and some other genes they examined by qRT-PCR that are important for cell cycle progression. However Figure 1B argues little overlap between splicing regulation and mRNA expression levels, save for 133 overlapping events. Are the events in the overlap of periodic AS and periodic gene expression overrepresented for IR like in their example for AURKB and/or other PTC-introducing AS? The same could be done with CLK1 regulated AS and gene expression that is mentioned in the text later (paragraph one, subheading “CLK1 regulates AS events in genes with critical roles in cell cycle control”).

6) Blot for phospho-SR proteins: Figure 2A shows that CLK1 seems to be unique among splicing factors tested in periodic protein expression level changes. An obvious mechanism that likely contributes to the observed periodic splicing changes is altered SR protein phosphorylation, particularly since SRSF1 doesn't change protein expression (Figure 2A). Can the authors use a phospho-RS-specific antibody (1H4?) to see if the phosphorylation state of any SR proteins is altered through the cell cycle and, if so, if any of these phosphorylation changes are deadened upon CLK1 inhibition with TG003?

7) Experimentally test known IR event identified in their analysis in CLK1: Figure 2—figure supplements 1A and B show neither CLK1 mRNA levels nor inclusion of exon 4 changes significantly through the cell cycle. Boutz et al. (2014) and others cited within have described regulated intron retention (or "detained introns") of the upstream and downstream introns flanking CLK1 exon 4 that affects the transcript's localization and stability. Since periodic IR is suggested to be a common point of AS regulation through the cell cycle in this paper, showing that these introns are or are not retained across the cell cycle using additional primer sets, as was done for exon 4 skipping in Figure 2—figure supplements 1B, could further rule out splicing regulation or add another interesting layer of regulation controlling CLK1 in the context of the cell cycle. Indeed, the MISO analysis in Supplementary file 1 calls IR in this region as one of the 1747 periodic splicing events (event: chr2:201726189-201725961:-@chr2:201724469-201724403:-) so this may very well be an additional layer of regulation upstream of the kinase-dependent, ubiquitin-mediated turnover that the authors convincingly demonstrated in Figure 2—figure supplements 1C and Figure 2C–E. Similarly, the authors could test and report results for variations of CLK1's 3'UTR.
