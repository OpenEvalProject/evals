# Peer review - Round 1

Editors:
- Nicholas Dopkins, Northwell Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104441.3.sa0](https://doi.org/10.7554/eLife.104441.3.sa0)

This important study substantially expands observations of HERV expression in the clinical settings. The evidence provided by the authors that HERV activity is an underlying etiological factor in ME/CFS and fibromyalgia is compelling and suggests further investigation into mechanisms. This work will be of broad interest to clinicians and researchers alike.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104441.3.sa1](https://doi.org/10.7554/eLife.104441.3.sa1)

Summary:

Giménez-Orenga et al. investigate the origin and pathophysiology of myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS) and fibromyalgia (FM). Using RNA microarrays, the authors compare the expression profiles and evaluate the biomarker potential of human endogenous retroviruses (HERV) in these two conditions. Altogether, the authors show that HERV expression is distinct between ME/CFS and FM patients, and HERV dysregulation is associated with higher symptom intensity in ME/CFS. HERV expression in ME/CFS patients is associated with impaired immune function and higher estimated levels of plasma cells and resting CD4 memory T cells. This work provides interesting insights into the pathophysiology of ME/CFS and FM, creating opportunities for several follow-up studies.

Strengths:

(1) Overall, the data is convincing and supports the authors' claims. The manuscript is clear and easy to understand, and the methods are generally well-detailed. It was quite enjoyable to read.

(2) The authors combined several unbiased approaches to analyse HERV expression in ME/CFS and FM. The tools, thresholds, and statistical models used all seem appropriate to answer their biological questions.

(3) The authors propose an interesting alternative to diagnosing these two conditions. Transcriptomic analysis of blood samples using an RNA microarray could allow a minimally invasive and reproducible way of diagnosing ME/CFS and FM.

Weakness:

(1) While this work makes several intriguing observations, some results will need to be validated in future studies using experimental approaches.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104441.3.sa2](https://doi.org/10.7554/eLife.104441.3.sa2)

Summary:

Giménez-Orenga carried out this study to assess whether human endogenous retroviruses (HERVs) could be used to improve the diagnosis of Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS) and Fibromyalgia (FM). To this end, they used the HERV-V3 array developed previously, to characterize the genome-wide changes in expression of HERVs in patients suffering from ME/CFS, FM or both, compared to controls. In turn, they present a useful repertoire of HERVs that might characterize ME/CFS and FM. For most part, the paper is written in a manner that allows a natural understanding of the workflow and analyses carried out, making it compelling. The figures and additional tables presents solid support for the findings. However, some statements made by the authors seem incomplete and would benefit by a more thorough literature review. Overall, this work will be of interest to the medical community seeking in better understanding the co-occurrence of these pathologies, hinting at a novel angle by integrating HERVs, which are often overlooked, into their assessment.

Strengths:

- The work is well-presented, allowing the reader to understand the overall workflow and how the specific aims contribute to filling the knowledge gap in the field.

- The analyses carried out to understand the potential impact on gene expression mediated by HERVs are in line with previous works, making it solid and robust in the context of this study.

Weaknesses:

- The authors claim to obtain genome-wide HERV expression profiles. However, the array used was developed using hg19, while the genomic analysis of this work are carried out using a liftover to hg38. It would improve the statement and findings to include a comparation of the differences in HERVs available in hg38, and how this could impact the "genome-wide" findings.

- The authors in some points are not thorough with the cited literature. Two examples are:

(1) Lines 396-397 the authors say "the MLT1, usually found enriched near DE genes (Bogdan et al., 2020)". I checked the work by Bogdan, and they studied bacterial infection. A single work in a specific topic is not sufficient to support the statement that MLT1 is "usually" in close vicinity to differentially expressed genes. More works are needed to support this.

(2) After the previous statement, the authors go on to mention "contributing to the coding of conserved lncRNAs (Ramsay et al., 2017)". First, lnc = long non-coding, so this doesn't make sense. Second, in the work by Ramsay they mention "that contributed a significant amount of sequence to primate lncRNAs whose expression was conserved", which is different to what the authors in this study are trying to convey. Again, additional work and a rephrasing might help to support this idea.

- When presenting the clusters, the authors overlook the fact that cluster 4 is clearly control-specific, and fail to discuss what this means. Could this subset of HERV be used as bona fide markers of healthy individuals in the context of these diseases? Are they associated with DE genes? What could be the impact of such associations?

Appraisals on aims:

The authors set specific questions and presented the results to successfully answer them. The evidence is solid, with some weaknesses discussed above that will methodologically strengthen the work.

Likely impact of work on the field:

This work will be of interest to the medical community looking for novel ways to improve clinical diagnosis. Although future works with a greater population size, and more robust techniques such as RNA-Seq, are needed, this is the first step in presenting a novel way to distinguish these pathologies.

It would be of great benefit to the community to provide a table/spreadsheet indicating the specific genomic locations of the HERVs specific to each condition. This will allow proper provenance for future researchers interesting in expanding on this knowledge, as these genomic coordinates will be independent of the technique used (as was the array used here).

Comments on revisions:

When addressing the comments made in the previous round, there are some answers that lack substance and don't seem to be incorporated in the manuscript. For example, the authors say:

Authors' response: This is an important point. However, the low number of probes (less than 100) that were excluded from our analysis by lack of correspondence with hg38 among the 1,290,800 probesets was interpreted as insignificant for "genome-wide" claims. An aspect that will be explained in the revised version of this manuscript.

I checked the revised manuscript with tracked changes, and there doesn't seem to be an updated explanation to this. In which lines is this explained?

For the other response:

Authors' response: Using control DE HERV as bona fide markers of healthy individuals seems like an interesting possibility worth exploring. Control DE HERV (cluster 4) associate with DE genes involved in apoptosis, T cell activation and cell-cell adhesion (modules 1 and 6). The impact of which deserves further study.

I couldn't find an updated mention of this in the discussion.

Another point that I raised was regarding the decision of using an FDR of 0.1 instead of 0.05. The authors only speculate about the impacts in their answer, while I believe that this could have been rigorously addressed. Since this was done in R, and DE analysis are relatively fast, I don't see a reason as to why this part was not repeated and discussed accordingly.

For other analyses, there doesn't seem to be a problem with using 0.05 as threshold. Examples of this are the "Overrepresentation functional analysis", or the "Statistical analysis" part of the methods they say "we used a Fisher exact test to calculate p-value, considering enriched in the provided list if an adjusted p-value (FDR) was less than 0.05".

Just to make this point clear: I'm not asking the authors to repeat all the work using the 0.05 FDR threshold, but rather that they are aware and conscious about the impact of this, and give an idea to the audience on how it would change the DE numbers. This would put in perspective the findings to any future reader.

I think that most of the other answers to both my previous concerns and the other reviewer's concerns are ok. My last outstanding concern is that the probe coordinates apparently can't be shared, which undermines a lot this study reproducibility, and its use by future researches which won't be able to compare their results to this study.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104441.3.sa3](https://doi.org/10.7554/eLife.104441.3.sa3)

Summary:

The authors find that HERV expression patterns can be used as new criteria for differential diagnosis of FM and ME/CFS and patient subtyping. The data are based on transcriptome analysis by microarray for HERVs using patient blood samples, followed by differential expression of ERVs and bioinformatic analyses. This is a standard and solid data processing pipeline, and the results are well presented and support the authors' claim.

Strengths:

It provides an innovative diagnostic approach using ERV profiles to subtype patients and distinguish FM and ME/CFS.

Comments on revisions:

This is a revised manuscript which addresses the comments well.
