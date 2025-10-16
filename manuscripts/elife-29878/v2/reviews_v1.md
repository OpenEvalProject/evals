# Peer review - Round 1

Editors:
- Ali Shilatifard, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29878.014](https://doi.org/10.7554/eLife.29878.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "CRISPRi is not strand-specific and redefines the transcriptional landscape" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by James Manley as the Senior Editor. We have attached the reviewers' comments for you below.

As you will see, the reviewers find your study of great interest to the community, but have also suggested that the paper is technical in nature and somewhat lacks mechanistic insight. We are willing to consider a revised version of your manuscript addressing the comments/concerns of the reviewers, specifically reviewer 2.

Reviewer #1:

In recent years, transcriptional interference by antisense RNA transcription has been recognized as a relatively frequent means to regulate mRNA expression. Tools enabling antisense transcription arrest without directly affecting sense transcription are required to study the mechanism mediating this effect. The recently reported CRISPRi system, using a modified, partially defective, Cas9 (dCas9) appeared as ideally suited for this since it has been shown to be able to trigger transcription termination in a site specific and, most importantly, strand specific manner, without altering the genomic sequence.

This short report shows that this strand specificity is actually not true at all loci. In addition, it describes an example in which the binding of the guide RNA actually induces spurious transcription initiation, suggesting that it markedly perturbs the local chromatin environment.

I think that the data are suitably convincing. Note, by the way, that this referee has made the similar (unpublished) observations that the termination by this system was not strand specific at yet another locus.

Although one could argue that the main results presented in this manuscript are negative results, I personally think that they are well worth being published to warn further investigators who would wish to use this system and a short report in eLife might seem appropriate for that.

The position of the 5'-end of SUT650 seems incorrectly assigned. Indeed, if one refers to the TIF-seq data from the original Pelechano paper, the main transcription start site for SUT650 (position 705244 on the Crick strand of chromosome X; this is also consistent with the data from Malabat et al., eLife, 2015) would be located about 60 nucleotides DOWNSTREAM of the AS-44NT sgRNA binding site (position 705184). Thus, as the other SUT650 sgRNA targeting sequences, AS-44NT would actually be located within the SUT650 transcribed region, downstream from its TSS and not upstream. It could thus not be considered as a "control" sgRNA. Could the authors verify this point and, if this is correct, modify the text, Figure 2E and Figure 2—figure supplement 1 accordingly? This would in no way modify the conclusions of the manuscript.

Reviewer #2:

In this paper by Howe et al., the authors assess the potential of CRISPRi for strand-specific transcriptional perturbation in budding yeast. They study two genes in depth – GAL1 and HMS2 – and compare the effectiveness of CRISPRi to previous approaches (for example deletion of cis-acting motifs such as the TATA box) in wt and Xrn1 deletion strains. Their primary conclusion is that CRISPRi works well in some cases and not in others and requires careful controls. For example, the authors show that the system does repress antisense transcription, but at one of the two studied loci (HMS2), an additional antisense transcript appears from a new initiation site, and the sense transcript is prematurely terminated. In addition, they present a clever tool based on click chemistry for quickly making gRNA. Although I don't find the main conclusion revelatory, I commend the authors for their thoroughness. Certainly, this message is one that bears reporting, although I am not quite convinced this result clears the bar for an eLife paper.

1) The authors show that CRISPRi represses the antisense transcript at a GAL1 model gene. They then check whether this repression has transcriptional effects on GAL1 sense transcription and they conclude there is no difference in galactose. However, previous work has shown that antisense at the GAL locus works mostly under repressive conditions. Have the authors repeated this experiment in glucose or raffinose?

2) The authors show that CRISPRi repression at the HMS2 locus results in a changed transcriptional landscape. Replacement of the HMS locus by URA does not have the same effect, and they suggest that CRISPRi binding causes these additional transcripts. However, it is unclear whether the new transcripts at HMS2 appear because of removal of the antisense, which in itself could change the chromatin landscape and thus the transcriptional landscape, or whether it arises because of binding of dCas9. The same authors have previously published that removal of the GAL10 ncRNA by genetic methods (point mutations of the transcription factor binding sites) also results in additional transcripts not visible in the wildtype (Murray et al., 2015, supplementary figure S5C). Given these findings, it remains unclear whether the new antisense transcript indeed results from the CRISPRi binding. Moreover, it is noteworthy that additional transcripts are also found in some genetic mutants. Control experiments are therefore required for both methods.

3) The Xrn1 sensitivity is a confounding factor, and I am not sure that strain should be the gold standard for CRISPRi not working. The whole point is that one can get blocking or perturbation in the absence of genetic manipulation. So, for example one concluding sentence "CRISPRi is not as effective as a genetic mutation in reducing levels of either the GAL1 or HMS2 AS transcripts" should end with "[…] in the Xrn1 deletion."

4) In a related point, Figure 4C is a critical part of the argument. The lower panel needs to have significance calculated between the TATA mutant and AS+112NT, since these bars look pretty similar to this referee. Moreover, the similarity between these measurements suggests that the lower panel in Figure 4B is not quite a representative image.

5) Lastly, given that CRISPRi does represses the antisense transcript in both loci tested in the study in a strand-specific manner, the title is a bit misleading.

In summary, despite technical issues, I nevertheless find their argument that CRISPRi can have locus-specific effects to be convincing. However, the manuscript is mostly of a technical nature. Most experiments described are control experiments that should be done anyways when using a new method. The observations that CRISPRi can result in different transcripts is good to know when designing such experiments, but there is no proposed mechanistic insight, nor new biology that is learned from this study.

Reviewer #3:

In this manuscript Howe and collaborators in the Mellor and Brown labs explore the molecular basis of CRISPRi transcriptional interference in the context of yeast anti-sense transcription. This reviewer agrees with the authors that understanding the basis of CRISPRi in anti-sense transcription (and non-coding RNA transcription in general) is an important area of research because it is extremely difficult to establish direct causality with regard to these particular RNAs using genetic perturbations.

In the first section of their manuscript, Howe et al., describe synthesis of sgRNA constructs using "click-chemistry" to couple sgRNA variable regions to the constant region. The author's then use knock-in yeast strains generated using these constructs to evaluate the effects of CRISPRi on anti-sense transcription at the GAL1 and HMS2 genes. The authors observe that contrary to behaving as a transcriptional road-block when targeted to the non-template strand, dCas9 CRISPRi complexes result in unpredictable changes in chromatin and transcription, resulting in pre-mature termination of sense transcripts and shifting anti-sense transcription initiation sites. Collectively, these results clearly demonstrate that CRISPRi effects are more complex than previously reported and likely depend on locus-specific chromatin context. These observations have broad implications with respect to design of CRISPRi strategies and argue a strong case for careful characterization of transcript isoforms and promoter/termination sites before and after deploying CRISPRi. However, there are some fundamental issues with controls and some of the conclusions drawn that should be addressed before publication.

1) The authors observe that only a subset of sgRNAs targeting the non-template strand are capable of mediating repression, however, the reasons for this phenomenon are unclear. A simple explanation is that some sgRNAs are not capable of mediating stable dCAS9 interaction with chromatin. The author's should test this by performing Chromatin-Immunoprecipitation (ChIP) for dCas9 in their various sgRNA expressing lines to test if dCas9 chromatin occupancy correlates with repression. In my opinion this is an absolutely essential control for interpreting the authors' experiments.

2) This reviewer feels that increasing the sgRNA coverage across the sense/antisense transcripts in question would greatly strengthen the manuscript. In its current state, the authors test only 2 sgRNAs towards the GAL1-AS and SUT650 non-template strands, from which they obtain a single functional repressive sgRNA for each anti-sense transcript. As a strand specificity control they test 3 sgRNAs targeting the sense transcript HMS2 and show that none of these has an effect on sense or anti-sense. However, with a hit rate of ~1 in 2, this reviewer is not convinced by authors' claim that sgRNAs targeting the sense transcript have no effect on antisense transcription. Perhaps the coverage was simply too low to obtain a functional repressive sgRNA. The authors should perform high-density sgRNA tiling experiments (targeting both template and non-template) for either GAL1-AS or SUT650 (not necessary to do both loci). I feel this experiment will dramatically improve the manuscript and instill clarity into the context requirements for CRISPRi mediated repression.
