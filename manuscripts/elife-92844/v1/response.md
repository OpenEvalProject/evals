# Author response - Round 1

Authors:
- Ruonan Zhao
- Emma L Moore ([ORCID: 0000-0003-4116-918X](https://orcid.org/0000-0003-4116-918X))
- Madelaine M Gogol ([ORCID: 0000-0002-8738-0995](https://orcid.org/0000-0002-8738-0995))
- Jay R Unruh ([ORCID: 0000-0003-3077-4990](https://orcid.org/0000-0003-3077-4990))
- Zulin Yu
- Allison R Scott
- Yan Wang
- Naresh K Rajendran
- Paul A Trainor ([ORCID: 0000-0003-2774-3624](https://orcid.org/0000-0003-2774-3624))

## Response text

DOI: [10.7554/eLife.92844.3.sa4](https://doi.org/10.7554/eLife.92844.3.sa4)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations For The Authors):

(1) More explanation/description of Fig 3C and 3D would be helpful for readers, including the color code of 3D and black lines shown in both panels.

We have added more description to the legend of Figure 3, and we have used the same color code as in Figure 2, which we now specifically note in the figure legend as well.

(2) Differences between cranial and trunk NCC could be experimentally shown or discussed. Fig 4C shows some differences between these two populations, but in situ, results using Dlc1/Sp5/Pak3 probes in the trunk region may be informative, like Fig 5 supplement 2 for cranial NCCs.

This is an important point. The focus of our study was on cranial neural crest cells, and the single cell sequencing data is therefore truly reflective of only cranial neural crest cells. We have not functionally tested for the roles of Dlc1/Sp5/Pak3 in trunk neural crest cells, however, based on the expression and loss-of-function phenotypes of Sp5 or Pak3 knockout mice, we predict they individually may not play a significant role. It remains plausible that Dlc1 could play an important role in the delamination of trunk neural crest cells, but we have not tested that definitively. Nonetheless, Sabbir et al 2010 showed in a gene trap mouse mutant that Dlc1 is expressed in trunk neural crest cells. Regarding the similarities and differences between cranial and trunk neural crest cells as noted by the reviewer with respect to Figure 4, it’s important to recognize the temporal differences illustrated in Figure 4. Neural crest cell delamination proceeds in a progressive wave from anterior to posterior, but also that the analysis was designed to quantify cell cycle status before and during neural crest cell delamination. We have compared cranial and trunk neural crest cells in more detail in the discussion and also speculate what might happen in the trunk based on what we know from other species.

(3) Discussion can be added about the potential functions of Dlc1 for NCC migration and/or differentiation based on available info from KO mice.

We have added specific details regarding the published Dlc1 knockout mouse phenotype to the discussion, particularly with respect to the craniofacial anomalies which included frontonasal prominence and pharyngeal arch hyperplasia, and defects in neural tube closure and heart development. Although the study didn’t investigate the mechanisms underpinning the Dlc1 knockout phenotype, the craniofacial morphological anomalies would be consistent with a deficit in neural crest cell delamination reducing the number of migrating neural crest cells, as we observed in our Dlc1 knockdown experiments.

Reviewer #2 (Recommendations For The Authors):

The authors used the (Tg(Wnt1-cre)11Rth Tg(Wnt1-GAL4)11Rth/J) line but work from the Bush lab (see Lewis et al., 2013) has demonstrated fully penetrant abnormal phenotypes that affect the midbrain neuroepithelium, increased CyclinD1 expression and overt cell proliferation as measured by BrdU incorporation. The authors should explain why they used this mouse line instead of the Wnt1-Cre2 mice (129S4-Tg(Wnt1-cre)1Sor/J) in the Jackson Laboratory (which lacks the phenotypic effects of the original Wnt1-Cre line), or a "Cre-only" control, or at a minimum explain the steps they took to ensure there were no confounding effects on their study, especially since cell proliferation was a major outcome measure.

This is an important point, and we thank the reviewer for raising it. Yes, it has been reported that the original Wnt1Cre mice exhibit a midbrain phenotype (Ace et al. 2013). However, it has also been noted that Wnt1Cre2 can exhibit recombination in the male germline leading to ubiquitous recombination (Dinsmore et al., 2022). Therefore, to avoid any potential for bias, we used an equal number of cells derived from the Wnt1 and F10N transgenic line embryos in our scRNA-seq, and this included multiple non-Cre embryos. Our scRNA-seq analysis was therefore not dependent upon Wnt1-Cre, but also because we used whole heads not fluorescence sorted cells. However, Wnt1-Cre lineage tracing was advantageous from a computational perspective to help define cells that were premigratory and migratory in concert with Mef2c-lacZ ¬based on their expression of YFP, LacZ or both. We note these specifics more clearly in the methods.

The Results section (line 122) states that scRNA-seq was performed on dissociated cranial tissues but the Methods section (lines 583-584) implies that whole E8.5 mouse embryos were dissociated. Which was dissociated, whole embryos or just cranial tissues? Obviously, the latter would be a better strategy to enrich for cranial neural crest, but the authors also examine the trunk neural crest. This should be clarified in the text.

We apologize that some of the details regarding the tissue isolation were confusing and we have clarified this in the methods and the text. For the record, after isolating E8.5 embryos, we then dissected the head from those embryos, and performed scRNA-seq on dissociated cranial tissues. As the reviewer correctly noted, this approach strategically enriches for cranial neural crest cells.

The authors do not justify why they chose a knockdown strategy, which has its limitations including its systemic injection into the amniotic cavity, its likely global and more variable effects, and its need to be conducted in culture. Why the authors did not instead use a Wnt1-Cre-mediated deletion of Dlc1, which would have been "cleaner" and more specific to the neural crest, is not clear (maybe so they could specifically target different Dcl1 isoforms?). Also, the authors use Sox10 as a marker to count neural crest cells, but Sox10 may only label a subset of neural crest cells and thus some unaffected lineages may not have been counted. The authors should mention what is known about the regulation of Dcl1 by Sox10 in the neural crest. Although the data are persuasive, a second marker for counting neural crest cells following knockdown would make the analysis more robust. Can the authors explain why they did not simply use the Mef2c-F10N-LacZ line and count LacZ-positive cells (if fluorescence signal was required for the quantification workflow, then could they have used an anti-beta Galactosidase antibody to label cells)?

We thank the reviewer for raising these important considerations. It has previously been noted that although Wnt1-Cre is the gold standard for conditional deletion analyses in neural crest cell development, especially migration and differentiation, it is not a good tool for functional studies of the specification and delamination of neural crest cells due to the timing of Wnt1 expression and Cre activation and excision (see Barriga et al., 2015). Therefore, we chose a knockdown strategy instead, and also because it allows us to more rapidly evaluate gene function. We agree that there are limitations to the approach with respect to variability, however, this is outweighed by the ability to repeatedly perform the knockdown at multiple and more relevant temporal stages such as E7.5 (which is prior to the onset of Wnt1-Cre activity), as well as target different isoforms, and also treat large numbers of embryos for quantitative analyses. The advantage of using Sox10 as a marker for counting neural crest cells is that at the time of analysis, cranial neural crest cells are still migrating towards the frontonasal prominences and pharyngeal arches, and the overwhelming majority of these cells are Sox10 positive. Moreover, we can therefore assay every Dlc1 knockdown embryo for Sox10 expression and count the number of migrating neural crest cells. The limitation of using the Mef2c-F10N-LacZ line is that this transgenic line is maintained as a heterozygote, and thus only half the embryos in a litter could reasonably be expected to be lacZ+. But combining Sox10 and Mef2c-F10N-LacZ fluorescent immunostaining for similar analyses in the future is a great idea.

Reviewer #3 (Recommendations For The Authors):

The putative intermediate cells differentially express mRNAs for genes involved in cell adhesion, polarity, and protrusion relative to bona fide premigratory cells (Fig. 2E). This is persuasive evidence, but only differentially expressed genes are shown. Discussing those markers that have not yet changed, e.g. Cdh1 or Zo1 (?), would be instructive and help to clarify the order of events.

We thank the author for this suggestion and we have provided more detail about adherens junction and tight junctions. Cdh1 is not expressed, and although Myh9 and Myh10 are expressed, we did not detect any significant changes. ZO1 is a tight junction protein encoded by the gene Tjp1, which along with other tight junctions protein encoding genes, is downregulated in intermediate NCCs as shown in the Figure 2E.

It is unclear whether the two putative intermediate state clusters differ other than their stage of the cell cycle. Based on the trajectory analysis in Fig. 3C-D, the authors state that these two populations form simultaneously and independently but then merge into a single population. However, without further differential expression, it seems more plausible that they represent a single population that is temporarily bifurcated due to cell cycle asynchrony.

We have addressed the cell cycle question in the discussion by noting that while it is possible the transition states represent a single population that is temporarily bifurcated due to cell cycle asynchrony, if this were true, then we should expect S phase inhibition to eliminate both transition state groups. Instead, our trajectory analyses suggest that the transition states are initially independent, and furthermore, S phase inhibition did not affect delamination of the other population of neural crest cells.

The authors do not present an in-depth comparison of these neural crest intermediate states to previously reported cancer intermediate states. This analysis would reveal how similar the signatures are and thus how extrapolatable these and future findings in delaminating neural crest are to different types of cancer.

We have also added more detail to the discussion to address the potential for similarities and differences in neural crest intermediate states compared to previously reported cancer intermediate states. The challenge, however, is that none of the cancer intermediate states have been characterized at a molecular level. Nonetheless, with the limited molecular markers available, we have not identified any similarities so far, but our datasets are now available for comparison with future cancer EMP datasets.

The reduction in SOX10+ cells may be in part or wholly attributable to inhibition of proliferation AFTER delamination. Showing that there are premigratory NCCs in G2/M at ~E8.0 would bolster the argument that this population is present from the earliest stages.

The presence of premigratory neural crest cells in G2/M is shown by the scRNA-seq data and cell cycle staining data in the neural plate border.

Lines 248-249: The pseudo-time analysis in Fig 3C/D does indicate that the two most mature cell clusters (pharyngeal arch and frontonasal mesenchyme) may arise from common or similar migratory progenitors. However, given the decades of controversy about fate restriction of neural crest cells, the statement that "EMT intermediate NCC and their immediate lineages are not fate restricted to any specific cranial NCC derivative at this timepoint" should be toned down so as to not give the impression that they have identified common progenitors of ectomesenchyme and neuro/glial/pigment derivatives.

We appreciate this comment, because as the reviewer noted, there has been considerable literature and debate about the fate restriction and plasticity of neural crest cells, and indeed we did not intend to imply we have identified common progenitors of ectomesenchyme and neuro/glial/pigment derivatives. That can only be truly functionally demonstrated by clonal lineage tracing analyses. Rather, we interpret our pseudo-time analyses to indicate that irrespective of cell cycle status at the time of delamination, these two populations come together with equivalent mesenchymal and migratory properties, but in the absence of fate determination in the collective of cells. This does not mean that individual cells are common progenitors of both ectomesenchyme and neuro/glial/pigment derivatives. The nuance is important, and we address this more carefully in the text.

Lines 320-321: "...this overlap in expression was notably not observed in older embryos in areas where EMT had concluded". It is unclear whether the markers no longer overlap in older embryos (i.e. segregate to distinct populations) or are simply no longer expressed.

The data in Figure 5 demonstrates the dynamic and overlapping expression of Dlc1, Sp5 and Pak3 in the different clusters of cells as they transition from being neuroepithelial to mesenchymal. In contrast to Sp5 and Pak3, Dlc1 is not expressed by premigratory neural crest cells but is expressed at high levels in all EMT intermediate stage neural crest cells. Later as Dlc1 continues to be expressed in migrating neural crest cells, Pak3 and Sp5 are downregulated. But the absence of overlapping expression in the dorsolateral neural plate at the conclusion of EMT coincides with their downregulation in that territory.

In the final results section on Dlc1, the previously published mutant mouse lines are referenced as having "craniofacial malformation phenotypes". The lack of detail given on what those malformations are (assuming descriptions are available) makes the argument that they may be related to insufficient delamination less persuasive. The degree of knockdown correlates so well with the percentage reduction in migratory neural crest (Fig. 6) that one would imagine a null mutant to have a very severe phenotype.

The inference from the reviewer is correct and indeed Dlc1 null mutant mice do have a severe phenotype. We have added more specific details regarding the craniofacial and other phenotypes of the Dlc1 mutant mice to the discussion. Of note the frontonasal prominences and the pharyngeal arches are hypoplastic in E10.5 Dlc1 mutant embryos, which would be consistent with a neural crest cell deficit. Although a deficit in neural crest cells can be caused my multiple distinct mechanisms, our Dlc1 knockdown analyses suggest that the phenotype is due to an effect on neural crest cell delamination which diminishes the number of migrating neural crest cells.

Use the same y-axis for Fig. 4C/D

This has been corrected.

Fig. 6C: Please note in the panel which gene is being measured by qPCR

This has been corrected to denoted Dlc1.

Lines 108-117: More concise language would be appropriate here.

As requested, we were more succinct in our language and have shortened this section.

The SABER-FISH images are very dim. I realize the importance of not saturating the pixels, but the colors are difficult to make out.

We thank the reviewer for pointing this out and have endeavored to make the SABER-FISH images brighter and easier to see.
