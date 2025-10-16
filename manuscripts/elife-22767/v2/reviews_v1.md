# Peer review - Round 1

Editors:
- David N Arnosti, Michigan State University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22767.035](https://doi.org/10.7554/eLife.22767.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A high-resolution map of transcriptional repression" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, David N Arnosti (Reviewer #1), served as Guest Editor, and the evaluation has been overseen by Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Three reviewers have read your manuscript, and we agree that this work is potentially suitable for publication in eLife, after you have addressed points raised in the review process.

Essential revisions:

1) Data reproducibility. A major point raised in the review process was whether the ChIP data shown represents biologically independent measurements or technical replicates from single preparations of chromatin. A number of experiments (Figure 2, 3, 4, 5, 6) show detailed measurements about protein occupancy or histone modification, but in some cases, the authors do not provide enough information about the data presented to allow the reader to judge if the changes measured are convincing demonstrations of biological processes. Specifically, for most of the ChIP measurements, the figure legend notes n=3; is that three measurements of single chromatin preparation, or three independent preparations, independently measured? Certain experiments (e.g. 4D) are described as "independent experiments", thus, the former cases may represent a single biological experiment (chromatin prep), with independent chromatin IP measurements. One line of evidence supporting this view is that individual figures have fairly tight error bars, yet vary quite a bit between experiments, e.g. RNAP drop in Figure 3B,C is 3-5 fold, while in Figure 4C the change is ~2 fold. The paper should clearly distinguish technical from biological replicates, and indicate if the results are supported by more than one experiment. Clearly, the strength of the conclusions is related to the reproducibility of the effects from separate observations.

2) Relationship of findings to prior knowledge about Ikaros. A second point from the review was need to set the authors' findings in a more general context, to show how information about HDAC, NuRD, and chromatin structure in regulation of Myc and Ipll1 supports or contradicts previous studies on Ikaros action. For instance, earlier work from Georgopoulos showed that on the CD4 intronic enhancer, Ikaros and NuRD appear to antagonize each other's activity, such that loss of CHD4 results in enhanced, not reduced Ikaros, activity. Similarly, previous studies have implicated basal factor pTefb-Ikaros interactions, as well as polycomb. Other studies have shown concomitant binding of Ikaros and Ebf1 at the Igll1 promoter in large pre-B cells where the gene is expressed, raising the question of whether Ikaros activates in this context. The paper would be much more valuable to the community if the authors integrate their findings better with previous work, and in the Discussion propose how similarities or differences are to be reconciled. As it stands, the main summary concluding the paper is rather superficial.

3) Presentation and use of genome-wide data. The reviewers found that the integration of genome-wide information was potentially useful but incomplete; the quality of genome-wide information should be indicated with standard statistical measures (e.g. how much agreement is found among the triplicate MNase experiments? reproducibility of peaks etc.), even if the analysis of the entire dataset is being prepared in a separate study. MNase digestion patterns at two loci discussed, but overall significance is difficult to assess; is variation indicative of a change in nucleosome position, occupancy or other aspect of the individual experiments? It is not clear if the RNA pol II genome-wide study was similarly performed in triplicate. A related point to consideration of genome-wide data is related to point 2; it is reported that out of the 924 genes repressed upon increase in Ikaros expression, 372 show a reduction in RNAP2. How are the other 550 genes regulated? Are these not directly repressed by the Ikaros-NuRD complex? It would help this paper to provide enough information to understand Table 1 and Supplementary Data Table 1, which enumerate and list genes affected by Ikaros. For instance, the two genes studied in detail here are direct targets of Ikaros, and show a loss of RNA Pol II. A large number, but not the majority of other repressed genes also show a loss of Pol II; which of these are expected to be direct targets? An additional point regarding the table is the lack of clarity of how genes are assigned to it – is for example a log2 value of 0.05 even a significant change?

4) Modeling. The reviewers had differing opinions about the modeling; some asked for further validation through additional measurements of actual nucleosome positioning and Ikaros occupancy at individual sites, while another view was that the models are useful enough to point toward future studies of mechanism. A justification of the application of the modeling would strengthen this aspect of the study. In addition, a clarification of the actual mechanism suggested is requested: Ikaros has been variously described as a recruiter of NuRD, or an antagonist, or binding in an overlapping manner at promoters but not enhancers. The kinetics of binding shown in 4D indicate that a model with simple, stable recruitment of NuRD by Ikaros is too simple. But it is not clear what mechanism the authors are proposing, based on their findings.

5) Endogenous Ikaros vs. induced form. An increase in Ikaros nuclear localization is assumed from the immunofluorescence data but this is not a very quantitative method. A western blot analysis for Ikaros in the nuclear vs, cytoplasmic fractions at the different time points should be performed. The way the ChIP data is presented, it is not clear how much endogenous Ikaros is already present at the target promoters before the induction of the tamoxifen-regulated protein, and how this compares with the induced levels. Previous studies have already noted that Ikaros is present at these genes, so how much of the modifications are due to overexpression of the protein? Why would nucleosome changes results only from overexpression; is this a function of rapid interconversion between active and inactive states on the genes with only endogenous Ikaros? In addition, the paper is silent about the Ikaros-like Aiolos protein; is it present at these genes, and does it play a role in regulation under these conditions?

6) MNase interpretation. The purported identification of "fragile" sites by MNase tests was not viewed as very strong, for a number of reasons. To identify such changes as an alternatively-bound form of the nucleosome, one would wish for a titration of MNase, not just a single digestion. In addition, it would be important to know if the change is due to a nucleosome shifting in position, rather than being weakly bound. Finally, the differential amplification in 6B with "short" and "long" amplicons may or may not be significant – it is not clear if the n=3 is a technical replicate, in which case, the support is weak.

A number of technical points relating to reagents, methods, and data presentation should be addressed:

7) The antibodies for Ikaros and EBF1 are not described; in the Materials and methods, a reference is made to Ferreiros-Vidal 2013, but EBF1 is not used there. What is the measure of specificity for these reagents? Is there other data to support the EBF1 binding shown here?

8) In Figure 1B, "enrichment" is the measure of chromatin binding for Ikaros and EBF1. The Materials and methods don't describe how these calculations were performed. One way might be to measure the signal at some non-bound site, and divide the ChIP signal% input by this background control. If so, what is their defined background? What were the% input values for these promoters and other locations?

9) For Pol II and TFIIB measurements, the manuscript shows directly the% input recovered from ChIP, which is a preferable approach for chromatin aficionados (their values ~1% are quite credible). The Y-axis is labeled "enrichment", however, which is confusing, because presumably the% input was not normalized to signal at another locus.

10) In Figure 3—figure supplement 1, part B, using the TEV-activated Ikaros system, depletion of Pol II does further affect MNase sensitivity, which is different from the system with 4-OHT induced Ikaros. The authors don't comment on this, though they previously make the point that Pol II eviction is not causing the changes in MNase sensitivity.

11) Figure 5—figure supplement A: TSA treatment apparently induces a decrease in histone acetylation levels? Please comment.

12) The differences for pericentric chromatin localization +/- TSA (6D) and loading of Ikaros with or without CHD4 (7B) may or may not be significant; it is not clear how reproducible these differences are in independent experiments. (See Point 1). In 6D, apparently two experiments were conducted; is this data from one?

13) It is not clear why the KinTec modeling used the specific parameters indicated in Materials and methods. Have these been measured in a particular system?

14) In subsection “Loss of RNAP2, reduced promoter accessibility, and transcriptional repression are early and near-simultaneous events” the authors state that they use primer pairs that span introns as a means to measure unspliced transcripts. They presumably mean primers that span individual exon/intron junctions? The primers used should be included in Materials and methods.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A high-resolution map of transcriptional repression" for further consideration at eLife. Your revised article has been favorably evaluated by Jessica Tyler as Senior editor and a Reviewing editor.

The manuscript has been improved but there are four remaining issues that need to be addressed before acceptance, as outlined below:

In this revision of Liang et al., the authors have addressed the points raised in the first round of review. Regarding data reproducibility, the authors have indicated in figure legends which datasets are averages of multiple biological experiments, and which are representative. Additional experiments were performed for 3D FISH, and a Figure 2—figure supplement 1 shows the reproducibility of ChIP and MNase experiments. Regarding previous observations about Ikaros action in different cell types and promoters, they clarify that their findings for c-myc and Igll1 promoters may represent just one side of this protein's regulatory activities, which includes activation at Zfp36.

The reviewers had asked for more specific analysis of genome-wide gene expression, since only a minority of genes showed the Pol II decrease found at the two promoters of interest. In the response to the reviewers, the authors reanalyze the data, and conclude that for a majority of promoters, it appears that Pol II decrease at the promoter is the trend, and that differences in sensitivity of measuring mRNA vs. Pol II occupancy may explain some of the discrepancy.

1) In addition to having this information in the letter of response, the manuscript should indicate that they believe the majority of genes are showing reductions in Pol II, but that differential sensitivity may be an issue. Otherwise it seems the authors are content to ignore what might be a mechanism that impacts the majority of repressed genes.

The use and interpretation of the models were questioned; in response, the authors provide more information on modeling, and emphasize that their many biological measurements point away from the simple two-state model, where Ikaros directly dislodges EBF1. This conclusion seems to be strongly supported by the data. They emphasize the failure to find reasonable parameters for the simple model, rather than over-interpreting specific parameters for more complex models, which seems a reasonable conclusion.

The nature and quality of experiments from genome-wide experiments is better explained and illustrated by the additional supplemental figure noted above, by correlation analyses in the response letter, and data deposited in GEO.

In response to the question about how endogenous Ikaros figures into this system, the authors note that they find similar responses in CRISPR'd cells lacking endogenous Ikaros, and show preliminary data in the letter. As asked, they also carry out a Western blot showing the levels of native and induced Ikaros over the time course, showing that the levels of the inducible form is approximately the same as that of the endogenous protein.

2) The Western blot data should be included in the manuscript as part of, or attached to, Figure 1, where the system is introduced.

The interpretation of a "fragile" nucleosome state was questioned, based on the limited probing with one concentration of MNase. The authors carry out a titration, showing a similar trend, but also soften their conclusion, noting that it appears that it is either nucleosome depletion or movement that is affecting the repressed promoter.

A number of minor points were addressed including provenance of antibodies, figure labeling, and explanation in the figure legend that nascent RNA was measured with intron-exon boundary spanning primers.

3) The text still refers to "intron-spanning primers" – that needs to be fixed.

4) Typo Figure 7 Average nuceosome profile
