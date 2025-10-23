# Peer review - Round 1

Editors:
- Stephen C Kowalczykowski, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33402.021](https://doi.org/10.7554/eLife.33402.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Rev7 and 53BP1/Crb2 prevent RecQ helicase-dependent hyper-resection of DNA double-strand breaks" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The overall findings with regard to Crb2 and Rev7 inhibiting the Rqh1 pathway are interesting, but there were many concerns with how the data are collected and analyzed. The manuscript presents novel data based on an assay that is not fully substantiated. Many controls are still needed to support the validity of the underlying assay.

There were unanimous reservations and many discussions about the assay which, in turn, undermined the confidence in, and significance of, the conclusions. Although most of the conclusion were consistent with existing facts, there were some specific inconsistencies noted by the reviewers. Overall, the results seem incomplete or preliminary.

Essential revisions:

Reviewer #1:

This is an interesting paper with potentially important conclusions. The results depend entirely on the assay, which seems to be reliable, but some questions remain:

1) There are no graphs showing the quality of the kinetic data. The authors need to show graphs of intensity vs time, for each assay, with fitting statistics.

2) It's a bit surprising that the array of 256 copies of lac repressor protein doesn't affect the measured rate. The authors need to show overlaid graphs of intensity vs time for the arrays; the PCR data for the arrays with lac repressor; and PCR data for the DNA arrays without lac repressors.

3) In the experiments with tagged RAD52, I don't understand why the foci persist. I would have expected RAD51 to replace the RAD52. Although the intensity does decrease (maybe just from photobleaching), it seems to be slower than the observations from the Rothstein lab on Rad52 in S. cerevisiae.

As stated above, the results are interesting and informative. However, the results rely entirely on the validity of the assay. In the current version, the authors don't present enough analysis and comparisons of the kinetic data to convincingly establish the assay. Presumably, they have the data; they need to provide it.

Reviewer #2:

DNA end resection is essential for homologous recombination, but excessive end resection can be detrimental to genome integrity. Long-range resection is catalyzed by either Exo1 or by a RecQ family helicase in collaboration with Dna2. The relative contribution of these two mechanisms and how they are regulated is not well understood. Here, the authors use a cytological approach to study end resection in single cells. An HO cut site was inserted 3.4-kb from a 10.3-kb lacO array located on Ch 2 of S. pombe. DSB formation/early resection was detected by the appearance of Rad52-mCherry foci that co-localize with the lacO array marked with LacI-GFP. Resection of the entire lacO array results in loss of the GFP signal while the mCherry signal remains. Consistent with a previous study using population based qPCR to measure resection (Langerak et al., 2011), the authors report that most resection is due to Exo1 activity and not Rqh1. Two years ago, several groups reported that Rev7 acts with 53BP1 to inhibit resection in mammalian cells. Here, the authors show that Rev7 and Crb2/53BP1 have a conserved role in preventing long-range resection in S. pombe. Furthermore, they show that Rev7 and Crb2 specifically block resection by Rqh1.

Overall, the authors demonstrate that live cell imaging can be used to study end resection in single cells, and their studies show considerable cell-to-cell variation in the initiation of resection, a feature missed by population-based DNA analysis. However, I'm not convinced that the microscopy-based single-cell assay is the best way to monitor resection. The generated data imply that resection speed can be measured accurately but that relies on some assumptions. In subsection “Image analysis” the authors write "The time between the first frame with an on-target Rad52-mCherry focus and the first frame with complete disappearance of the LacO/LacI-GFP focus is the duration of resection through 3.57 kb (between the HO cut site and the start of the LacO repeats) plus the full 10.3 kb LacO array". Is resection through the complete LacO array necessary for disappearance of the GFP focus? I could imagine that the GFP focus disappears before the complete LacO array is degraded. What is the minimum number of detectable LacO repeats? The authors could integrate LacO arrays of different lengths and check what the detection limit is. Or they should at least confirm the timing of the GFP focus disappearance with the qPCR assay (According to Figure 1—figure supplement 1 they could use HincII for this).

Also, to my eye the Rad52 focus appearance and LacI-GFP focus disappearance are not easily identified (based on the microscopy images shown). The authors should mark the frames they define as "Rad52 focus appearance" and "LacI-GFP focus disappearance". In the Materials and methods section, they don't say how they define these events. Do they do it manually or using some image analysis software? What is the threshold? More details are necessary here to judge the accuracy of the method. Also, the restriction of the assay to 5 hours by photobleaching seems to be a considerable drawback, which limits the number of "usable" cell trajectories (as shown in Figure 2—figure supplement 2B). Perhaps by changing the imaging period and number of z-stacks they could extend the time window for monitoring resection. Other approaches, such as using more photostable fluorescent proteins (e.g. LacI-mKate2, Rad52-monomeric NeonGreen), LEDs as light sources, or switching to an enzyme that cuts more efficiently than HO (I-PpoI has been successfully used in S. pombe and the efficiency of cutting is better than HO) would involve considerable more effort and time.

The authors stress that they use a single cell assay. But it is not clear what the advantage of single cell data is in their work. In the end they are comparing population medians, which could also be generated with bulk experiments. The low DSB formation efficiency might be a motivation to use a single cell assay to restrict the analysis to the few cells with a DSB. However, bulk experiments generally take the cutting efficiency into account, e.g. the qPCR-based assay described by Zierhut and Diffley, (2008) considers the HO cut fraction.

Rad52 foci are used as a read out for DSB formation and initiation of resection. Can these two steps be separated, for example, by measuring DSB formation by qPCR using primers flanking the HO cut site on the same samples used for the ApoI protection assay, or possibly using Mre11-mCherry instead of Rad52? It appears from Figure 1B (upper panel) that resection through most of the lacO array is required for a strong Rad52 signal.

In theory, the HO-induced DSB is unrepairable, but because the HO cutting efficiency is quite low, and S. pombe cells are in G2 most of the time, if one sister chromatid was cut and engaged in repair with the uncut sister it could result in an underestimation of resection. Were cells with a transient Rad52 focus detected? The exo1 example in Figure 1 appears to have a Rad52 focus that appears early and then goes away. Does elimination of Rad51 change the number of cells resecting or rate of resection? At late times, when the mCherry signal is very bright, are both sister chromatids cut and resected?

Langerak et al., used a qPCR assay to measure end resection and reported no defect in resection initiation (35 nt from HO cut site) in the exo1 mutant or exo1 rqh1 double mutant. Is the failure to detect Rad52 foci in most exo1 cells because resection tracts are <90 nt or because the amount of ssDNA required to support a Rad52 focus is much longer than 90 nt? Given that the Rad52 single is quite weak until the lacO array disappears, I think the authors might be under-estimating the amount of ssDNA to visualize a Rad52 focus. Does the exo1 mutant show normal DSB formation (measured with primers flanking the HOcs) and resection to the ApoI site located 168 nt from HOcs? Similarly, is DSB formation normal in the rev7 mutant and can early resection be detected by the qPCR assay?

Why does rqh1 suppress the early resection defect of rev7? An odd result that is not discussed in the text.

While the overall findings on the role of Rev7 and Crb2 repressing the Rqh1 resection pathway are certainly of interest to the field, the data analysis needs to be improved.

Reviewer #3:

DNA end resection is a process that initiates recombination-based DNA double strand break repair. As resection also generally inhibits non-homologous end-joining, regulation of DNA end resection is an important process. The human 53BP1 protein, though its various effectors, has been found to be an inhibitor of DNA end resection, although mechanistic insights are lacking. These processes appear to be at least partially conserved in low eukaryotes.

The authors are using a S. pombe as a model system, where they developed an assay allowing the monitoring of resection in live cells (Figure 1). The assay is based on the disappearance of GFP-LacI and appearance of Rad52-mCherry signal next to HO-endonuclease induced DSB. This is an interesting method that will be useful for high throughput microscopy-based screenings. However, the method has certain limitations in contrast to established southern blotting, PFGE or RTPCR-based methods:

a) The assay measures Rad52 accumulation, which is a step after resection. Rad52 is a mediator that loads Rhp51 on RPA-coated resected DNA. Using RT-PCR based assay, the authors established that there is a correlation between both processes (resection and RAD52 loading). However, this was only done in wt background, and it is possible RAD52 loading might differ in the mutants analyzed, and Rad52 might be loaded with different kinetics dependent on the resection pathway. The authors calculate resection rates making the assumption that there is no difference.

b) The assay measures resection of DNA bound by GFP-LacI, a non-physiologic binder. Therefore, the resection proteins must displace LacI for resection to occur. Under physiologic conditions, DNA near DSBs will likely be chromatinized and subsequently remodeled allowing resection. This is especially a concern when analyzing the role of chromatin binders such as 53BP1/Crb2. Also, the individual resection pathways may be affect by LacI binder to a different degree, which complicates interpretation.

The most interesting finding is that Rev7 and 53BP1/Crb2 appear to repress long-range resection dependent on Rqh1 (Figure 2): In the absence of Rev7 and Crb2, long-range resection is accelerated, which is independent of Exo1 and depends on Rqh1.

1) This observation should be verified using a previously established assay, given the concerns listed above. Related to this point, it remains a formal possibility that the action of Rqh1 is not specific to resection, but to strip LacI, allowing resection through another process. Performing resection with the same mutants in an established setup (with no LacI) will address this concern as well.

The authors then go on to demonstrate differential effects of Rev7 and Crb2 on early resection steps, based on timing of Rad52 foci appearance upon break induction (Figure 3). I am concerned about these results: using Rad52 (a protein with a function downstream of resection) does not appear to be correct as a marker of "early" resection.

2) The results should be analyzed in an established assay where the readout is clearly early resection. Also, to make claims on early resection, the analysis should include mutants deficient in short-range resection (e.g. mre11) and mutants in long-range resection, where both pathways have been inactivated (e.g. exo1 rqh1).

3) In Figure 2, the authors demonstrate that rev7 mutants have accelerated long-range resection, which is dramatically decreased when rqh1 is additionally mutated (rev7 rqh1), supporting the hypothesis that resection in rev7 mutants is Rqh1 dependent. In contrast however, the in Figure 3, the "early" resection is increased when rqh1 is mutated in rev7 background, a completely opposite effect. This is very confusing. The authors comment that "early" resection is a combination of Mre11 and Exo1/Rqh1 dependent processes. This dichotomy reinforces my concerns about the robustness of the experimental setup.

In summary, the manuscript presents an interesting assay and interesting pieces of data, but it seems rather preliminary at this point.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Rev7 and 53BP1/Crb2 prevent RecQ helicase-dependent hyper-resection of DNA double-strand breaks" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The biological findings of this manuscript are interesting, particularly the role of Rev7 in suppressing resection by the Rqh1 pathway, but there are significant concerns over the reliability of the assays used. The authors place equal importance on the fluorescence-based resection presented; however, the reliability of the assay is questionable and the weak point of this work. The conceptual idea of the assay is good, but there are reservations about its implementation and use to quantify resection speed. The authors have, for the most part, established the utility of their assay for the analysis of long-range resection, although they still need to provide a graphical example of their quantification. They discovered interesting roles of Rev7 and Crb2 in Rqh1-dependent resection. As both a methods contribution and a contribution to the recombination field, these findings could justify publication of a revised manuscript.

However, the manuscript then goes on to dissect the roles of these proteins in proximal recombination. Here the work is both incomplete and internally inconsistent. It would appear that the data in Figure 4A and Figure 4C are inconsistent with one another: 4A show a reduction in "Cell cycles with Rad52 foci" for rev7delta, whereas 4C shows no change, within error, for rev7delta at 300 bps (The figure legend, as well as the associated text in the main body of the manuscript, is not justified: "The extent of resection 300 bps and 3 kb from the HO cut site as assessed by the restriction enzyme/qPCR method supports less efficient resection initiation in rev7Δ cells compared to WT at 300 bp…").

Also, the conclusion that of Rev7 promotes early resection is based entirely on how quickly a Rad52 focus forms after break induction, and how many cells have visible Rad52 foci. It was suggested that the authors use a more direct measurement of break induction by qPCR using primers flanking the HO cut site. This has not been done and is a significant concern. If one compares the qPCR data for resection 168-bp from the HO cut site shown in Figure 1D and Figure 1—figure supplement 3B there are vast differences – 3% resection at 120 min in one figure compared with 15% resection at 120 min in the other. If there is this much variability between populations of cells then it could explain why the rev7 mutant looks different to wild type, and why rqh1 appears to suppress the early resection defect of rev7. How many independent inductions were performed for image analysis? The authors need a reliable method to assess DSB formation independent of Rad52 focus formation before drawing conclusions about a role for Rev7 in promoting early resection.

Furthermore, In Figure 1D, the authors use a qPCR assay to detect formation of ssDNA 168 and 14,253 bp from the HO cut site. From this assay, very few (2%) cells exhibit resection to the end of the lacO array 360 min after HO induction. This would appear to contradict the microscopy assay, which shows resection through the array takes ~150 minutes. Also, data should really be from biological replicas, not technical replicates of qPCR.

Consequently, whether or not Rev7 has a role in proximal resection is not clear from the authors' data.

There was agreement that manuscript needs to be revised:

1) It is essential that the confusing data on short range resection are clarified or removed from the manuscript. If the proximal resection data are retained, then the comments raised above need to be addressed. In addition, in the review of the prior version of this manuscript, reviewer #3 commented on this part in the original submission: "Also, to make claims on early resection, the analysis should include mutants deficient in short-range resection (e.g. mre11) and mutants in long-range resection, where both pathways have been inactivated (e.g. exo1 rqh1)." The authors did not address this previous request for clarification of this unexpected finding in this revised manuscript, using the analyses described for proximal resection (i.e., Figure 4).

It is unclear whether the authors can make these revision within the timeframe given. If not, then these data on proximal resection would need to be removed, and the conclusions of the manuscript refocused. One major finding is the effect of Crb2 on long-range resection: while this is new in S. pombe, it is well-described in S. cerevisiae (Rad9). The second major finding is the effect of Rev7 on long-range resection: this was only shown in humans, but not in the microbial eukaryotes. Although significant, the impact of the current manuscript is diminished without the proximal resection data; consequently, the author would need to make the contributions of their sound work much clearer in an expanded Discussion section of their work in relation to the existing literature (in any event, the existing Discussion section is inadequate.).

2) The authors use appearance of a Rad52-mCherry focus to identify onset of resection and disappearance of a lacO/LacI-GFP focus to identify resection past a site some 14 kb away from the DSB site. The problem is that both signals are rather fuzzy in many of the image series shown. This is especially true for the Rad52-mCherry focus (see e.g. the lower image series in Figure 1B, the first three image series in Figure 1—figure supplement 2, Figure 2A). The decision if a signal is judged as a focus or not is crucial, as it is the basis to calculate resection speed. This decision is made manually. Although the authors try to "equalize" the error by randomizing the image series prior to analysis, it seems to be a quite ambiguous approach of questionable reliability. What is their criterion to judge if a focus is present or not? Do they compare with background control strains? Why don't the authors use software to quantify the fluorescence signals and generate intensity trajectories? There are several non-commercial image analysis software packages available dedicated to exactly this purpose. Based on thresholds defined by appropriate control strains, appearance and disappearance of the signals could then be identified in a more controlled and rational way. A minimal requirement is that the author provides an x-y graph of foci fluorescent intensity vs time for each their examples of time-lapse video data in the manuscript.

If the authors submit another revised version, then the decision to accept or reject will be final, and no subsequent revisions will be considered.
