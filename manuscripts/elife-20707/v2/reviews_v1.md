# Peer review - Round 1

Editors:
- Marianne Bronner, California Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20707.024](https://doi.org/10.7554/eLife.20707.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Novel adverse outcome pathways revealed by chemical genetics in a developing marine fish" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have extensively discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you will see from the individual reviews below, all of the reviewers had extensive issues with the analysis and lack of detail in the description of method. Even more importantly, however, they also felt that the there was a great deal of over-interpretation and "overselling of the work", rendering many statements unsupported by the data. We feel that this is fixable but will require considerable rewriting and re-review. If you feel you are able to revise the paper accordingly, we would be willing to consider a significantly revised version for re-review.

Reviewer #1:

In this article the authors expand on previous experiments, where developing haddock are exposed to low levels of crude oil, to test for impacts on sensitive developmental endpoints. Developmental impacts are described in detail in previous reports, and this study reports transcriptomic changes during development following three oil exposure regimes.

I have two main difficulties with this paper. First, there is insufficient description of methods for gene expression analyses. Second, there is much speculation and unsupported statements such that much of the manuscript reads as over-statement.

Gene expression analysis:

Though the experimental design includes three different exposure regimes, specific gene transcriptional responses are not correlated in any way to dosing regime (high, low, pulse). The authors ought to show gene expression dose responses, at least for the genes for which they are trying to build cause-effect relationships with adverse outcomes. More convincing arguments for cause-effect would be supported by data showing that dysregulation of the gene precedes the appearance of the phenotype, and that dysregulation is more pronounced in treatments with more pronounced phenotypic effects (e.g., higher doses). The lack of detail reported here could make a reader concerned that perhaps interpretation of gene-specific responses are not as clear-cut as represented in the text. Are Figures 4, 5, 6, 7 showing data from any dose, or just high dose? Furthermore, there is no description of how emergence of phenotypes varied with dosing regime. Text (starting paragraph two of the Results section) that describes developmental phenotypes does not distinguish between effects that differ between doses, and all of the images from exposed animals in Figure 1 appear to be only from the high dose.

Other aspects of gene expression analysis that are problematic:

There is no description of the statistical model. What was compared to what? How many tests were there? Was there multiple test correction given the size of the gene set (e.g., false discovery rate correction)? Was this experiment analyzed as a fully specified statistical model, or were individual treatments compared to individual control treatments separately from others, and if so was there multiple test correction for that? There is insufficient information provided here to be able to evaluate the quality and robustness of the gene expression analysis. Given that gene expression analysis is a focus of the paper this is a problem.

41.9 million reads (subsection “Extraction of mRNA, RNA sequencing and bioinformatics”) – is this per sample?

32.69% mapping efficiency (subsection “Extraction of mRNA, RNA sequencing and bioinformatics”) – this is extremely low! Why is this so low if sequence similarity between haddock and reference (cod) genome is so high? How was successful mapping assessed – how were mapping parameters set? This should be a red flag that something went wrong in the mapping, or that there was significant contamination issues.

After mapping, this left 31.51 million reads "for each group". I'm not sure what this means "for each group". It is generally accepted that a minimum of ~10M reads PER SAMPLE (that is, per experimental unit) is adequate for RNA-seq.

"three biological replicates per stage” – section "Total RNA and cDNA preparation" states that RNA was from pools of embryos. So are these more accurately 3 replicate pools?

KEGG analysis: what were the criteria used to include a KEGG pathway in figures S4/S5? At least one of the criteria should be statistically significant enrichment. From my look at these figures, there are no obvious pathway-level connections to the phenotypes/physiological pathways on which the authors hang their hat. E.g., these figures do not have any terms that obviously relate to cholesterol homeostasis. Nor does Figure 3—figure supplement 1 indicate any enrichment of pathways having to do with ionoregulation, or craniofacial development. So what is the analysis here?

Selected gene sets: The authors make assertions about physiological mechanisms given responses of specific genes with inferred functions that make a nice story. However it is unclear what is the null expectation from this type of analysis.

E.g. Subsection “Genes associated with defects in cardiac function and morphogenesis”: "We therefore focused on genes associated with cardiomyocyte membrane potential and intracellular Ca2+ cycling" – how were these genes selected?

In the same section: "The expression of a few E-C coupling genes" – was there an unbiased collection of E-C coupling genes, then test for significant enrichment of these genes?

In the same section: "genes involved in cardiac morphogenesis" – again, how were these collected/curated as a gene set? Please provide the query gene set.

Subsection “Genes associated with craniofacial abnormalities”: "We therefore interpreted developmental changes in haddock gene expression in the context of these well-characterised zebrafish mutants." – so the "tester" set here was all genes shown in zebrafish mutants to be involved in neural crest cell or muscle development? Please include this set of genes. The 12 genes indicated below this section – is this a significant enrichment?

Subsection “Genes associated with ion and water regulatory imbalance”: "Our analysis focused on key ionoregulatory proteins in MRCs and their associated genes, including Na+/K+ ATPase subunits (at1 genes, e.g. at1a1-a4, at1b1-b4), a urea transporter (ut1), a Na+/K+/2Cl- co-transporter (s12a2), the sodium hydrogen exchanger Nhe3 (slc9a3), and a chloride channel" – this is clearly not a complete or objective curation of ionoregulatory genes.

Is there an unbiased query gene set for any of these analyses? This whole "genes associated with phenotypes" section – is there objective analysis? What makes this anything more than just story telling given some cherry-picked genes? The authors should at least use language that proposes some hypotheses, rather than writing text so as to imply strong conclusions of cause-effect adverse outcome pathways. This is a problem that permeates the reporting of results and discussion, and contributes in a large way to overstatement of the results that are expanded on below.

Unsupported claims and overstatement issues:

There are pervasive issues throughout the manuscript, often associated with claims or conclusions that are (or should be) in fact stated as hypotheses. It is often unclear whether certain statements are supported by their data, supported by the literature, or are speculation or informed hypotheses. Some examples follow:

Subsection “Genes associated with defects in cardiac function and morphogenesis”: "Overall, the transcriptional response to disrupted E-C coupling was not a simple pattern of compensation" – how do they know that this is a transcriptional response to E-C coupling? Is expression not being measured in whole animals? What proportion of overall tissue mass is accounted for by the heart? I think the authors are drawing conclusions where they ought to be proposing hypotheses. This is an issue in MANY places throughout the manuscript

Subsection “Genes associated with craniofacial abnormalities”: "Overall, the genes identified above for both neural crest and muscle lineages represent a more complex pattern of dysregulation than previously been reported for any of the individual zebrafish craniofacial mutants. This suggests that crude oil is acting on novel developmental processes." – It is unclear what is supporting this assertion (1st sentence), and how the assertion leads to the conclusion (2nd sentence)

Subsection “Genes associated with ion and water regulatory imbalance”: "and they should therefore lose water along a diffusion gradient if osmoregulation is disrupted as a consequence of heart and circulatory failure." – Does oil exposure cause ionoregulatory dysfunction and/or water loss in developing marine fish? Are these statements speculation/hypotheses, or are they supported in the literature? There are several prominent studies on the effects of oil exposure on osmoregulation in fish, but none of these are referred to.

In the same section: "a third distinct oil-induced adverse outcome pathway." – how do they know that this is a pathway distinct from cardiac dysfunction? E.g., rather than just a secondary manifestation of circulatory failure?

"Crude oil exposures therefore appear to cause osmotic stress in the developing embryonic nervous system" – the authors are implying an overall impact on ionoregulatory abilities? Is there any support for this here or in the literature? E.g., any studies showing dysfunction of net sodium or chloride flux upon oil exposure? Do the authors mean to propose this as a hypothesis?

Subsection: "A novel adverse outcome pathway: disruption of cholesterol homeostasis" – this subheading, and the following paragraphs, claim novelty, and appear to claim precedent for this discovery. Has oil exposure impacts on yolk utilization not previously been reported in the literature? I can find a publication from the 1990s after just a couple minutes searching. Furthermore, the studies presented here do not provide direct evidence for impacts on yolk mobilization or cholesterol homeostasis. E.g., how do the authors know that the apparently increased yolk size in Figure 1K isn't just a result of fluid accumulation stemming from observed edema?

In the same section: "Pathway analysis was also consistent with a significant effect on cholesterol homeostasis” – The associated figure is is missing. Also, staring at Figure 3—figure supplement 1, I see no pathways that include any terms obviously related to cholesterol homeostasis. Nor for that matter does Figure 3—figure supplement 1 indicate any enrichment of pathways having to do with ionoregulation, or craniofacial development,

Subsection “Unaltered gene expression in relation to visibly normal organs: lateral line and liver.”: "Similarly, the related KEGG pathways that are inclusive of these genes were relatively unaffected by oil exposure at all time points" – but what does this really mean? KEGG pathways (Figure 3—figure supplements 1 and 2), as far as I can tell, don't implicate many (any?) of the mechanisms that the authors are building their story on – e.g., ionoregulation, cholesterol homeostasis, craniofacial development. If this paragraph was intended to serve as a test or confirmation that their conclusions/assertions in preceding paragraphs have merit, then this is unconvincing – and problematic for supporting the assertions that the other functions (ionoregulation, cholesterol homeostasis, craniofacial development) ARE supported by pathway-level analysis.

Discussion section:

"We identified specific changes in the expression of key genes involved in the function or morphogenesis of individual tissues and organs with visible abnormalities. Given unaltered gene expression associated with apparently unaffected structures such as the liver, the DEGs in oil-exposed haddock indicate a disruption of specific developmental processes, as opposed to non-specific effects (e.g., general developmental delay)." – this appears to me as a gross overstatement. There was no organ-specific analysis of gene expression. The authors measured gene expression in whole animals. They therefore are not in a position to make assertions about expression in the heart or liver, though of course they are free to propose hypotheses.

"Our data demonstrate a transcriptional cascade that is tightly linked to these defects in cardiac function (cardiomyocyte intracellular calcium cycling) and form (heart chamber growth)." – there are 4 genes that are slightly down-regulated at one timepoint preceding the emergence of altered cardiac phenotypes (6 dpf), and none deferentially expressed immediately post-organogenesis (10 dpf) when the proposed E-C uncoupling should be apparent. Does this represent the discovery/demonstration of a "transcriptional cascade"?

"Crude oil likely disrupts normal MRC function" – what is the evidence for this?

"MRC function could be impaired by a high metabolic cost of PAH degradation." – why? Evidence or rationale to support this?

"In haddock embryos, fluid moves from the dorsal subdermal space to the yolk sac. At the larval stage, the permeable yolk sac membrane is replaced by the more resistant peritoneal cavity and body wall, causing fluid to move into the dorsal finfold and adjacent tissues." – I assume that the authors mean to write this as a proposal or hypothesis that is consistent with their observations?

Discussion section paragraph nine: much of this is highly speculative. There are plenty of transcriptomics studies of oil exposure during fish development, that include edema as an endpoint. If the authors want to make these assertions perhaps they should check those other studies for altered regulation of VEGF-C.

Discussion paragraph ten: This entire paragraph reads as excessive speculation

Discussion paragraph eleven: "but tissue localization during craniofacial development in embryonic fish is needed to confirm a role in this adverse outcome pathway" – look up Planchart & Mattingly 2010 TCDD upregulates FOXQ1 in zebrafish jaw primordium

Discussion section: "First, we used known spatial mRNA distributions in model species (primarily zebrafish) to more accurately phenotypically anchor the transcriptome data for crude oil-exposed haddock" – this sounds fancy but there is no description of this in the methods

Reviewer #2:

In their manuscript "Novel adverse outcome pathways revealed by chemical genetics in a developing marine fish", Sorhus et al. characterize the impact on the transcriptome of PAHs during embryonic/larval development of Atlantic haddock. The authors examined gene expression profiles from fish exposed using three different exposure paradigms, two chronic (low =.58 µg/L & high = 6.7 µg/L) and one intermittent (6.1 µg/L per pulse). The authors examine genes that underlie one of four phenotypes observed in exposed embryos/larvae and show that changes in these genes may lead to the phenotypes observed. The authors' results will be of interest to the readership of eLife. However, several concerns exclude publication of the manuscript in its current form.

Major concerns:

1) Given that haddock is not a model system, better explanation of the developmental time windows will be critical for most readers to understanding the context of the embryonic and larval developmental stages. In zebrafish 50% epiboly occurs at 5.5 hpf while in haddock it occurs at 3 dpf.

2) Authors need to add Alcian images of the new facial phenotypes not listed in their previous work, the upper jaw is not shown in previously nor is the basicranium.

3) The authors need to be more explicit in their logic in moving from a broad overview of the transcriptome and to genes that directly impact the phenotypes listed when those genes are not the most highly responsive. Why discuss the broader transcriptional changes (subsection “General patterns of gene regulation in response to crude oil”)?

4) Without the ability to create genetic chimeras or cell-type specific transgenics to directly test the tissue target of PAHs effect on facial development, the authors need to soften their stance that PAH disrupts muscle development thereby affecting skeletal development. Crump and Schilling have shown that in zebrafish edn1 is expressed in and required in NCCs. The authors cannot rule out a direct NCC-PAH impact based only on their data (Discussion section).

5) What do the authors mean by the "transcriptional response to disrupted E-C coupling was not a simple pattern of compensation" (subsection “Genes associated with defects in cardiac function and morphogenesis”)?

6) Several the figures need to be reviewed. Two figure supplements are missing from the manuscript, though they are described in the text (subsection “A novel adverse outcome pathway: disruption of cholesterol homeostasis”). Figure 6B shows that myh1 is down regulated at 0 dph not 11 dpf as described in the text (subsection “Genes associated with craniofacial abnormalities”). The supporting datasets need to be organized with the supplemental table 1 for readability. It is difficult to relate these datasets with the table in the current form.

Reviewer #3:

Overall assessment: This is an interesting study that is well done overall and advances our understanding of oil impacts on developing marine fish. Strengths include the use of an environmental relevant non-model organism, the experimental design involving exposure at both embryonic and larval stages, use of multiple modes of exposure (two concentrations and a pulsed exposure), sampling at multiple time points, and a rich set of data on gene expression that is anchored to phenotypes.

Substantive concerns:

1) In the title, Abstract, and manuscript, the authors overreach when they invoke "chemical genetics" and "adverse outcome pathways" (AOPs). Chemical genetics involves high-throughput screening of libraries of individual compounds, a much more precise approach than the exposure to a complex chemical mixture performed here. Although nowhere defined by the authors, an AOP describes the entire sequence of events from a molecular initiating event, across multiple levels of biological organization, to an adverse outcome; it is synonymous with "mechanism of action" (see e.g. Ankley 2010 Envir. Tox. Chem. and Villeneuve 2011 Envir. Tox. Chem.). When the authors refer to AOPs they are actually referring only to adverse outcomes, not the pathways. Their gene expression data may help to inform our understanding of some AOPs associated with oil exposure, but they certainly have not "revealed novel AOPs." And contrary to the claim in the Abstract, it is not clear that they have "identified initiating events"-the specific chemical-protein interactions that lead to the gene expression and phenotypic changes that they report.

2) The authors' approach, which is stated explicitly (Results section), is to interpret changes in haddock gene expression in relation to known zebrafish mutants, i.e. they focused only on specific genes known to be involved in development of the tissues affected by oil. While this is valuable, is there a more objective approach that might be used to identify unexpected associations between changes in gene expression and specific phenotypes? It seems as though they have not taken full advantage of the unbiased RNA-seq dataset in this regard.

3) The authors over-interpret the connections between gene expression patterns and phenotypes, claiming cause-effect relationships in haddock from what are only associations. For example, Discussion section paragraph two claims a "tight linkage" between gene expression and cardiac defects. Whether the gene expression changes are causal or are secondary to the phenotypic changes is not clear. The authors could strengthen their arguments by being more explicit about the temporal and concentration-dependent associations between gene expression patterns and phenotypes, e.g. by adding a measure of phenotypic progression to Figures 4–7.

4) The experimental design is not described sufficiently. The methods (paragraph one) refer to a previous paper, but it is not clear whether these samples are from the same experiment described in that paper, or just used similar exposures. Indeed, the oil concentrations in that paper are expressed differently than in the current manuscript. Even if the methods are the same, this paper should be a description of the experimental design, including exposure conditions, numbers of replicates, numbers of pooled embryos in each replicate, etc.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Novel adverse outcome pathways revealed by chemical genetics in a developing marine fish" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers are generally happy with your revisions but request some clarifications in methodology and also raise some minor comments. I ask you to correct these points prior to passing on your manuscript for production. Individual reviews are below.

Reviewer #1:

Details of the experimental design and analysis are still not adequate. The authors refer the reader to the Sorhus 2016b publication for all aspects of experimental design. The authors should provide in the current manuscript at least the basics of experimental design in the methods section, including the number of doses, the specific developmental stages examined within each dose, and the number of biological replicates (replicate pools) within each dose*stage treatment. Furthermore, I have read Sorhus 2016b and it is not obvious WHAT were the exact contrasts without much effort on the part of the reader. The authors should make it easy to understand the basic of the experimental design.

Also, it is still not clear to me what was the unit of replication. I asked for clarification on the nature of replication previously. The revised manuscript reads "cDNA library preparation and sequencing was performed by the Norwegian Sequencing Centre (NSC, Oslo, Norway) on one pool from three replicate tanks per stage for each dose (low, pulse and high) plus control using the Illumina TruSeq RNA Sample Preparation Kit".

A treatment is a dose*stage. Were there replicate pools of embryos assayed per treatment? As far as I can tell, six developmental stages were profiled at each of 3 doses and a control, resulting in 24 treatments. I find 24 "samples" sequenced in the SRA (https://www.ncbi.nlm.nih.gov/Traces/study/?acc=SRP060012). This would suggest one pool per treatment, unless there are multiple samples embedded within each SRA entry. If there is just one sequenced pool per dose*stage treatment, then I recommend rejection of the manuscript for lack of replication of experimental units. If I misunderstand this, and there is in fact replication of pools of embryos within each dose*stage treatment, then I recommend the following:

Subsection “Structure of pelagic larvae and visible phenotypes associated with crude oil exposure”: "with 96% of high dose animals showing abnormal phenotypes, ranging to ~ 60% for pulse dose and ~ 35% for the low dose."

The authors should consider preparing a visual that summarizes this distribution of phenotypes across doses. E.g., stacked bar chart (or pie chart), including proportion of animals showing each phenotype, with dose as series. And perhaps separate plots for different developmental stages.

Subsection “Oil-induced changes in gene expression during embryonic development.”: "p > 0.05" Is it not more standard to notate as p<0.05?

Subsection “General patterns of gene expression in response to crude oil”: "At all stages, the subcategory of Organismal Development or Embryonic Development (henceforth combined as Development) was in the top 5 Diseases and Bio Functions category under Physiological System Development and Function with p values ranging from 10-3 to 10-19 " Are categories/subcategories of functions from IPA? Authors should state this.

In the same subsection: "Pathway enrichment was dose-dependent and clearly associated with the frequencies of abnormal phenotypes (Supplementary file 1C)." It would appear that reviewers do not have access to these supplementary files. This is frustrating.

Subsection “Genes associated with defects in cardiac function and morphogenesis”: "overexpression of bmp10, nkx25, or tbx3 is associated with serious heart defects in other vertebrates." This needs a citation

Discussion section: "Two major initiating events for crude oil-associated cardiac defects during fish development are chemical blockade of IKr repolarizing potassium currents, (encoded by kcnh2) and disruption of intracellular calcium handling, the latter culminating in sarcoplasmic reticulum (SR) calcium depletion through effects on either RyR or SERCA2 (encoded by ryr2 and at2a2, respectively). In the fully formed heart, these pharmacologic effects impair cardiac function by inducing arrhythmia and reducing contractility." Citations are needed in this section.

Subsection “Extraction of mRNA, RNA sequencing and bioinformatics”: "150 key genes involved in cardiac and craniofacial development and cardiac function were assembled." Please provide a table of these genes, and relevant citations describing their relationships to key phenotypes. The authors state in their rebuttal "The lists are provided in a new table, Supplementary file 1E." It would appear that I unfortunately do not have access to review these files (or I'm somehow just looking in the wrong place?). If not already done, authors please make sure these files are detailed with the phenotype relationship and citations to all relevant literature (e.g., defend criteria for including a gene in your curated set).

In the same subsection: "The contigs" is this the reference cod sequence, or the haddock RNA-seq read sequences?

The authors state in their rebuttal "Although the effects of oil exposure on salt and water balance in fish embryos have not been examined," This is perhaps true, but it has been examined in adults, and this may be worth noting in the manuscript. E.g.: Kennedy CJ, Farrell AP (2005) Ion homeostasis and interrenal stress responses in juvenile Pacific herring, Clupea pallasi, exposed to the water-soluble fraction of crude oil. Journal of Experimental Marine Biology and Ecology 323, 43-56.

Regarding the author's rebuttal "As for direct evidence of disrupted cholesterol homeostasis, we are not sure what is more direct than up-regulation of HMG-CoA-reductase" Up regulation of a gene is not a direct measure of altered cholesterol homeostasis.

Reviewer #2:

In their revised manuscript "Novel adverse outcome pathways revealed by chemical genetics in a developing marine fish", Sorhus et al. characterize the impact on the transcriptome of PAHs during embryonic/larval development of Atlantic haddock. The authors examined gene expression profiles from fish exposed using three different exposure paradigms, two chronic (low =.58 µg/L & high = 6.7 µg/L) and one intermittent (6.1 µg/L per pulse). The authors examine genes that underlie one of four phenotypes observed in exposed embryos/larvae and show that changes in these genes may lead to the phenotypes observed. The authors have addressed concerned all concerns raised, therefore the results in the revised manuscript will be of interest to the readership of eLife and is ready for publishing in its current form.

Reviewer #3:

I would quibble with a few of the responses to my original comments, but I don't view these issues as serious enough to derail publication of the paper. Nevertheless, I point them out for the authors' consideration.

1) Regarding what is an "initiating event" in an adverse outcome pathway (AOP), I disagree with the authors' claim (response to reviewer #3, point 1) that bmp10 upregulation is such an initiating event. It is an early event, certainly. But the true initiating event is the chemical-protein interaction that causes bmp10 to be upregulated. That event has not been identified in this paper.

2) With regard to my questioning of their statement claiming that it has not been clear that oil influences mRNA levels as part of a developmental phenotype (Discussion section): The authors pointed out that the several previous papers I noted as showing oil affecting mRNA expression in fish did not involve measurements made in embryos. However, they did not provide this explanation in the revised manuscript, despite the fact that two of the three reviewers raised the same question. In addition, in their response the authors mention a more recent paper, published (27 June) prior to the original submission of this manuscript (30 Aug), that does include transcriptomic analysis of fish embryos exposed to oil (Xu et al. ES&T). It is unfortunate that the authors did not take advantage of the opportunity to better explain their original statement or compare their results with the prior work in embryos.

3) The manuscript would be improved by a clearer summary of the experimental design so that the readers don't have to dig out the other paper. And the point about replication is important – this needs clarification.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Novel adverse outcome pathways revealed by chemical genetics in a developing marine fish" for further consideration at eLife. Your revised article has been favorably evaluated by Marianne Bronner as the Senior editor, a Reviewing editor, and one reviewer.

The manuscript is in principle ready for publication pending a minor but critical revision which is to include relevant information rather than referring the readers to other papers. The reviewers have asked for this repeatedly and I am only prepared to accept your paper with the inclusion of this additional information. This is an easy change and I hope you will make it quickly. Below is the comment from the reviewer.

Reviewer #1:

The revisions, in general are fine. However, I should note that I have been generally frustrated by the struggle with the authors to include all relevant information, accessibly, within this manuscript. Far too many papers are published these days that have incomplete description of methods. Also, many papers refer the reader to other papers to find out details of the methods. This results in un-necessary additional work for the reader – especially un-necessary since all journals these days have supplemental sections that allow authors to include all relevant information, without cluttering up the main manuscript. The authors are still insisting on sending the review on a hunt through their previous papers to find relevant information ("A thorough functional description of the genes including citations are provided in Sørhus et al. 2016a."). This is not too much to ask. We should all strive to make our research more transparent, and more reproducible.
