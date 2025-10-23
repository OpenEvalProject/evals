# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50895.sa1](https://doi.org/10.7554/eLife.50895.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Partial loss of CFIm25 causes aberrant alternative polyadenylation and learning deficits" for consideration by eLife. Your article has been reviewed by Eve Marder as the Senior Editor, Sacha Nelson as the Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Erin Schuman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have followed up on a prior human genetics study implicating copy number variation in Nudt21, which encodes the polyadenylation factor CFIm25, in intellectual disability and seizure disorder. In this advance, they create a mouse model of the disorder and demonstrate that heterozygous loss of function results in learning deficits, EEG abnormalities, altered polyadenylation of many genes and altered abundance of associated proteins. The study is important both because it illuminates the pathophysiology of a human neuropsychiatric disorder and because it highlights the importance of dosage regulation (here only a 30% reduction in protein results from the heterozygous loss) especially when the affected gene is critical for regulating the abundance or function of many other gene products, in this case by regulating alternative polyadenylation.

Essential revisions:

The reviewers and editors were enthusiastic about the importance of the study, but several key concerns about the ability of the data to support the conclusions were raised. These centered mainly on the issue of sequencing and proteomics data quality and analysis. The concerns were mainly that some of the poly(A) ClickSeq reads may be erroneous and need to be removed. False positive peaks can lead to miscalculation of genes with non-stop decay. Both reviewers noted the large variation among control samples shown in Figure 4—figure supplement 1. The PCA plot showed variability among controls (PC2) that was nearly as large as the experimental effect. There were also concerns about the statistical validity of the assessment of protein abundance. One reviewer suggested repeating the RNA-seq for expression analysis. The other suggested performing northern blots to confirm identified 3'UTR isoforms and their differential regulation in the mutant animals. They also suggested the following quality controls and metrics:

- What algorithm was used to identify peaks?

- What measures were taken (filtering steps) to prevent internal priming (false poly(A) peaks)?

- How many reads/peaks per gene feature (5'UTR/CDS/3'UTR/introns) were detected?

- What is the number of peaks per known poly(A) signal (how many peaks do not have known poly(A) signals)?

- What is the peak distance from known poly(A) signals?

- What is the replica correlation between poly(A) peak counts?

- Are the detected peaks conserved in other species?

- What is the fraction of sequenced reads that fall into poly(A) peaks after filtering? (It would be an issue if more reads are filtered, than reads contributing to poly(A) peaks.)

Reviewer #1:

In this manuscript by Alcott et al., the authors report learning deficits in mice with reduced CFIm25 expression. The authors claim that the phenotype is attributable to mis-regulation of alternative polyadenylation and resultant protein expression changes. This work extends the previous work from the Zoghbi lab where they found copy number variations of genomic segments spanning CFIm25 led to intellectual disability and seizures in patients. Overall, the current work was well carried out, especially the phenotype part, and the results are important. However, there are several concerns the authors should address before the paper can be accepted for publication.

1) The authors claim that 15% of genes with altered APA may undergo non-stop decay. This is quite a substantial number. Can they rule out the possibility that this is due to technical artefact of the sequencing method? Can they verify these non-stop decay-causing poly(A) sites, either by 3'RACE (for some) or comparing their data to those from other sequencing methods?

2) They also observed a non-stop decay isoform for NUDT21. However, this does not appear congruent with the fact that there is 30% reduction of protein level but 50% mRNA reduction. Non-stop decay should reduce both mRNA and protein expression levels. Therefore, the mRNA reduction should be more than 50%. Also, how can they explain the increase protein production per mRNA?

Reviewer #2:

In this manuscript the authors examine in mice heterozygous for NUDT21 to mimic the loss of the human protein associated with various copy number variations. NUDT21 mRNA encodes CFIm25, a component of mammalian cleavage factor I which regulates polyadenylation. The authors show in a variety of standard learning and memory tasks (auditory fear conditioning and performance in the water maze) that the NUDT21+/- mice perform significantly less well than the WT mice, to different degrees, depending on the task. The authors also perform a basic analysis of "spiking" activity, based on EEG recordings and find an elevated "spiking" in one brain area. The authors then go on to analyze the effect of NUDT21+/- on polyadenylation of mRNAs from human embryonic stem cells that are differentiated into excitatory neurons. The authors have previously published (Gennarino et al., eLife 2015) that NUDT21 is associated with the usage of longer 3'UTRs in patient-derived lymphoblastoid cells.

1) Figure 4—figure supplement 1. Principal component analysis.

The principal component analysis is able to separate the control and the shRNA samples for both methodologies, 3'end sequencing and mass spectrometry. However, the 3'end sequencing control samples seem to have strong batch effects, as PC2 and PC1 are very similar. This casts doubts on the quality of the data and the validity of the results.

2) Figure 4D and Figure 4Cv.

A substantial fraction of genes (233) show an increase of mRNA length upon NUDT21 KD. The example of KIF9 shows an internal APA peak in the second CDS-exon under the control condition. How many of the 233 (or more) genes show the same characteristics? The authors should provide more information about their detected 3'UTR isoforms. How many of the detected peaks in the control condition correspond to known 3'UTR isoforms? What is the relative distance of all detected APA events to the known stop codon? Is there a established APA signal in the proximal upstream region of the identified peaks? Furthermore, the isoforms and their change upon NUDT21 KD should be additionally validated by northern blot or 3'RACE for both scenarios, shortening and lengthening.

3) Figure 4E.

This figure compares the change in protein abundance (shRNA vs. control) with the change in mRNA length (shRNA vs. control). However, there is no measure of significance for the protein foldchange. The authors should show the LFQ fold changes and highlight whether the expression differences are significant or not. Furthermore, the increase/decrease in protein abundance could also be the result of changes in RNA abundance or changes in translation. This should also be addressed. How many of the 87 genes in quadrant one can be explained by the gain of a stop codon that prevents the degradation by non-stop decay?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Partial loss of CFIm25 causes learning deficits and aberrant neuronal alternative polyadenylation" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and Sacha Nelson (Reviewing Editor) and two peer reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

After review and further discussion, the reviewers and editors agree that the remaining two points raised by reviewer #2 need to be addressed. In the event that the statistical test suggested in point 2 is negative, the conclusions linking 3'UTR shortening to protein up-regulation should be softened or qualified.

Reviewer #1:

The authors have addressed all my concerns. I have no more comments.

Reviewer #2:

We still have a few remaining concerns:

1) Figure 4 and 6. T-SNE analysis.

We disagree with the use of t-SNE over PCA as a quality control. Both PCA and t-SNE are dimensionality reduction techniques. PCA aims to reduce dimensions, but preserves sample variance information. This is also the idea of the control plot, to visualize the variance between sequencing samples, where distances on the PCA components will correspond to differences in sample variance.

t-SNE uses a probabilistic approach to maximize sample distances to define clear sample clusters, during this process it will distort the sample variance information due to its non-linear characteristics. In the context of a control plot to visualize sample variance, t-SNE is not the right dimensionality reduction technique to use. It will artificially create better sample clusters.

2) Figure 4E and 6D. Protein analysis.

We disagree. The authors should provide a statistical analysis to test whether candidates in quadrant 2 of Figure 6D are significantly overrepresented. As is, no meaningful conclusions can be drawn about a possible relation between 3'UTR shortening and protein upregulation. Also, there are some data points (shown plotted in red) missing from their plot.
