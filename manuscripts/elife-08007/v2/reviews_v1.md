# Peer review - Round 1

Editors:
- Bing Ren, University of California, San Diego School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08007.018](https://doi.org/10.7554/eLife.08007.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Genome-wide DNA hypomethylation and RNA:DNA hybrid accumulation in Aicardi-Goutières syndrome” for peer review at eLife. Your submission has been favorably evaluated by James Manley (Senior editor), and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individuals responsible for the peer review of your submission have agreed to reveal their identity: Bing Ren (Reviewing editor); Paula Vertino (peer reviewer #3). A further reviewer remains anonymous.

The Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The work reports a number of interesting findings linking mutations of AGS1-5 to the symptoms displayed by a class of rare genetic disorders. Overall, the manuscript is well written, with most conclusions well supported by evidence presented. However, a number of over-interpretations or over-statements were made, where causal relationships were drawn based on insufficient data. The authors are encouraged to thoroughly revise the manuscript by toning down the statements or provide more objective statements.

Essential revisions:

1) Thoroughly revise the conclusions, where unwarranted causal relationship was drawn, as noted by both reviewers #2 and #3 (below). For example, “This study identifies global epigenetic perturbations and accumulation of RNA:DNA hybrids as two novel hallmarks that may drive the powerful immune response responsible for...”

2) Provide clearer description of the datasets. For example, provide information upfront regarding the WGBS sequence depth and resolution.

3) The RNAseq data only weakly support the idea of immune activation as a phenptype that is enriched in AGS fibroblasts. There were nearly as many downregulated genes...any patterns there? The data should be fully discussed.

4) The data in Figure 3E, F seem to suggest that the accumulation of RNA:DNA hybrids is confined to retroelements, and further, to specific classes (LINE,LTR) implying some specificity to the effect. Please discuss this trend and biological implications.

5) The Drip-seq data need to be better presented so that a reader can fully appreciate how the patterns change, and the spatial relationship to other genomic features (see Reviewer #3 comment below).

6) The DNA methylation data and RNA-DNA hybrid datasets also need to be presented more clearly, so that the spatial relationship between DNA methylation changes and accumulation of RNA:DNA hybrid can be better appreciated.

7) Experiments from the RNASEH2A k/o fibroblasts have revealed only a modest impact of RNASEH2A KO on DNA methylation at certain retroelements. Deeper analysis of this cell system would allow the investigator to determine the hierarchical nature of the genomic phenomena observed, and strength the causality statement.

8) Proper statistics needs to be used and documented when the enrichment/depletion characteristics and overlapping features are discussed.

Reviewer #1:

Aicardi-Goutières Syndrome (AGS) is caused by mutations in several genes involved in ribonucleotide metabolism and is characterized by an overt native immuneresponse, but the molecular causes of the symptoms remain unidentified. In this study, the authors profiled transcriptome, DNA methylome and RNA-DNA hybrids in fibroblasts from patients with AGS, and identified global DNA hypo-methylation and increased RNA:DNA hybrids as the most likely drivers of the inflammatory response in AGS patients. Importantly they highlight a potential epigenetic contribution to this syndrome (hypomethylation) specifically the reactivation of retrotransposon elements in the human genome, due to genome hypomethylation in the cells. The results are pretty compelling and the conclusions are well supported by the data provided.

1) Figure 1. It appears that for some genes, the normalized RNA-seq data for some of the samples (AGS4-P2, AGS5-P2, AGS2-P1) varies a lot between replicates in the same patient. Could you provide information showing the correlation between replicates?

2) Figure 3A) This figure is confusing. It would help to explain how the right hand vertical axis corresponds to the left hand vertical axis. Figure 3C is much more easily interpretable and a cleaner presentation of the data.

3) The authors show that in AGS2 and AGS4 patients, regions containing RNA:DNA hybrids largely correspond with hypomethylated regions, but this is not true in AGS1 and AGS5 patients. Additionally, the authors mention that AGS1 and AGS5 patients have decrease hypomethylation. Patients AGS2 and AGS4 have RNASEH2a/2b mutations, and the authors show how RNASEH2a mutations trigger DNA hypomethylation. Is it possible to show the same for the RNASEH2b mutation corresponding with the AGS2 patient?

4) Figure 6E/F) By focusing on only two LINE elements it seems too small of a set to “suggest a direct role of RNASEH2a in triggering DNA hypomethylation.” Perhaps you can suggest that it plays a role at these LINE elements. It is likely that if you focused on other areas you could see hypermethylation. Additionally in Figure 6E/F on cpg13, there are four reads supporting 50 % methylation level in the scramble, and two reads supporting a 0% methylation level in the KO. There are too few reads covering this cpg to make any claims regarding changes in methylation at cpg13.

Reviewer #2:

The study focuses on a potential mechanism connecting genetic mutations in TREX1, RNase H2 and SAMHD1 to inflammation-related problems in Aicardi-Goutières syndrome (AGS) in children. AGS involves the accumulation of incompletely metabolized nucleic acids resulting from the mutations. In this study, a variety of epigenome and transcriptome profiling, and a cutting-edge genetic engineering method are used to identify the source of immunogenic nucleic acids. The main conclusion is global epigenetic alterations and accumulation of RNA-DNA hybrids are involved in AGS, both shown here for the first time, and these alterations may drive immune responses that cause the inflammation.

Overall this is a novel study that provides a new evidence of two types of molecular changes that are variably associated with AGS, as shown in fibroblasts from AGS patients and controls.

The main issue I see with this manuscript is the overstatement of causality where only modest associations are shown. For example, I would agree with “This study identifies global epigenetic perturbations and accumulation of RNA:DNA hybrids as two novel hallmarks” but do not see adequate support for the remainder of the conclusion “that may drive the powerful immune response responsible for...” I also suggest adding additional caveat/caution about the first phrase as this study analyzed a very limited number of AGS samples, and they are heterogeneous in terms of the underlying mutation. Another example of overstatement is “our results indicate that AGS mutations in TREX1, RNASEH2A, RNASEH2B, and SAMHD1 lead to the accumulation of RNA:DNA hybrids over retrotransposon-rich intergenic regions.” The data do not support “lead to”, but perhaps better described as “associated with”.

The WGBS data is quite interesting and the Circos display allows a reasonable visual comparison and highlights global differences. I have minor concerns about the data. The coverage is quite low, 3x to 7x, which defeats the main benefit of this method, base resolution. While the overall conclusion is probably correct, it would be better for the reader to know this is very low pass sequencing upfront, rather than putting it in a supplemental table only. It is also not clear how the C to T conversion was calculated. I could not find an explanation in the table or methods.

Reviewer #3:

The manuscript by Lim et al. makes some very interesting observations regarding the molecular basis of Aicardi-Goutieres syndrome, an autoimmune disorder of uncertain molecular origin despite well described loss of function mutations in several nucleic acid processing enzymes. The authors find that loss of function of AGS genes is associated, to varying degrees, with widespread hypomethylation of DNA as well as the selective accumulation of RNA:DNA hybrids in intergenic regions and over repetitive elements, and modest changes in gene expression. How these three observations are molecularly linked is less clear. The manuscript is well written and the experiments appropriately controlled. For the most part (exceptions noted below, the conclusions drawn are supported by the data provided.

1) The authors appear to favor the idea that RNA:DNA hybrid accumulation is the culprit behind activation of the immune response in AGS cells, though the data at hand are such that a direct causal link cannot be established. How this might be achieved is unclear, but the Discussion proposes a number of ‘sensing’ mechanisms, some of which would require a mechanism in cis (e.g. detection of hybrids as they are formed) whereas others (TLR, GAS-STING etc. ) require cytoplasmic accumulation of duplexes. Is there any evidence in the AGS fibroblasts or in the RNASeH2 K/O fibroblasts of non-genomic accumulation of DNA:RNA duplexes in AGS cells?

2) The RNAseq data only weakly support the idea of immune activation as a phenptype that is enriched in AGS fibroblasts. There were nearly as many downregulated genes...any patterns there? The data should be fully discussed.

3) The DNA damage known to accompany defects in the AGS genes is proposed as intermediates that could mediate and/or cause the RNA:DNA hybrids or DNA hypomethylation. Do RNA:DNA hybrids accumulate at the sites of ectopic DNA damage ? This is something that could be addressed in the RNAseH2 k/o cells which exhibit by co-localization studies with gamma H2Ax.

4) It is suggested that the relationship of RNA:DNA hybrid accumulation to retroelements might be circumstantial, due to the enrichment of these structures in intragenic regions... however, the data in Figure 3E, F, if representative, seem to suggest the opposite; that the accumulation of RNA:DNA hybrids is confined to retroelements, and further, to specific classes (LINE,LTR) implying some specificity to the effect. Are the unique drip seq signals by and large confined to retroelements as shown in Figure 3E, F? Is it possible that you are detecting some intermediate in piRNA-mediated transposon silencing?

5) The Drip-seq data are presented in a very general way (as total # of peaks, distance covered etc.) making it difficult to fully appreciate how the patterns change, and the spatial relationship to other genomic features. Both and increase in burden and size is implied. Statements like “...Drip-seq peaks were 3-4 fold larger in size” are unclear. Do you mean that existing Drip-seq peaks in control cells spread / expand laterally in AGS cells, or is the trend for new peaks to form in patient cells? Figure 3D – the ‘raw’ data on common and unique sites would be more informative rather than “fold change” e.g. what fraction of common and unique peaks overlap each genomic feature? This would provide not only a comparison between unique and common sites, but also an indication of the relative distribution of Dripseq peaks across genomic features in each setting.

6) Likewise, it is hard to appreciate the spatial relationship between DNA methylation changes and accumulation of RNA:DNA hybrids, given that the former are very broad and might encompass multiple retroelements some of which change and others that don't. If one looks specifically at those AGS specific DRIP-seq peaks, what fraction are overlapping retroelements, and what is the average DNA methylation level of these in control and AGS cells?

7) The lack of overlap between AGS unique DRIP seq peaks and regions of GC skew/ annotated TSSs is taken as an indication that the aberrant RNA:DNA hybrids detected do not arise co-transcriptionally. Barring a direct test of the role of transcription on RNA: DNA hybrids in AGS cells, I'm not sure one can rule out a transcription-dependent mechanism at this juncture.

8) The authors interpret the data from the RNASEH2A k/o fibroblasts as evidence that “...RNAse H2 defects directly drive these epigenetic perturbations”. Thus far they have only observed a modest impact on DNA methylation at certain retroelements. Whether there is a measurable global (bulk) effect on DNA methylation as in AGS cells is not clear, nor has the impact on RNA:DNA hybrid formation been studied. This could be a powerful system as it might allow the investigator to determine the hierarchical nature of the genomic phenomena observed.

9) Why/what are the missing bubbles in the bisulfite sequencing data in Figure 6E? Depending on the nature of these CpGs (unmethylated/methylated) would change the magnitude of the methylation change significantly.
