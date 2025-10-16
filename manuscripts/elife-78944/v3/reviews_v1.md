# Peer review - Round 1

Editors:
- Jerry L Workman, https://ror.org/04bgfm609 Stowers Institute for Medical Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78944.sa0](https://doi.org/10.7554/eLife.78944.sa0)

In this manuscript the authors have conducted native elongation transcript sequencing on yeast strains deleted for one of 41 different transcription, chromatin modifying and RNA processing factors. They find that a large fraction of these deletions affect transcription elongation and RNA Pol II pausing indicating that elongation is carefully regulated by many factors.


---

# Peer review - Round 1

Editors:
- Jerry L Workman, https://ror.org/04bgfm609 Stowers Institute for Medical Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78944.sa1](https://doi.org/10.7554/eLife.78944.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Dynamics of transcription elongation are finely tuned by dozens of regulatory factors" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jerry L Workman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided to reject this manuscript. There are technical issues noted in the review below that would need to be resolved to support many of the conclusions. If these issues can be addressed in a satisfactory way we would welcome submission of a new version of the manuscript.

In this study, "Dynamics of transcription elongation are finely tuned by dozens of regulatory factors" the authors present an impressive amount of native elongating transcript sequencing (NET-Seq) data and perform in-depth analysis of the dataset. Overall, the focus of this work was to determine the contributions of 41 transcription/chromatin related non-essential gene products to RNA Polymerase II transcription at different phases of transcription. This includes in-depth characterization of RNA Polymerase II pausing in each deletion strain and an analysis of sense and antisense transcription events. The introduction, which sets up the goals of the study, was very descriptive of transcription in general and lacked some focus discussing events that occur in multiple biological systems although this study was performed using yeast as the sole model system. It is stated that it is currently unknown how Pol II pausing contributes to gene expression levels however it could also be argued that Pol II pausing is, by nature, inhibitory to transcript production. Antisense transcription in yeast has also been shown by others to be inhibitory to sense transcription in multiple contexts including different yeast deletion backgrounds.

The Churchman lab are leading experts in NET-Seq method development and data analysis and it is likely that the data produced for this study are of high quality. The major weakness in the context of this current study is that this study is NET-Seq focused with a lack of follow up experiments. This concern is partially mitigated by the breadth of the work that was performed. However, some data focuses on the reproducibility of specific events, such as Pol II pausing, and only two replicates were performed for each mutant. In fact, Figure S5A suggests that pausing reproducibility across the two replicates may be poor. Figures 4-7 focus on this pause data so lack of reproducibility of this measurement is a major concern.

The data presented covers many of the 41 mutant strains that were used in the study. It does a nice job of describing both extremes of changes for each aspect that is discussed relative to the parental yeast strain. The study often references data from other studies to suggest potential interpretation of the results but no major follow up studies were performed to provide strength to these interpretations or glean new mechanism. Many of the findings support prior studies by others making this a useful resource yet not necessarily providing many novel insights. The uncertainly regarding the pause site reproducibility limits the potential impact of that portion of the work.

Recommendations for the author:

The manuscript by Couvillion, Harlen, Lachance et al., describes the effect of deleting a set of elongation-related factors on Pol II pausing and Pol II antisense transcription using NET-seq in budding yeast. Pausing and antisense transcription were extensively compared between genes/regions and between strains. Overall, the work generated mainly expected results but did not highlight any clearly new concept or finding. One unexpected observation is that deletion of subunits of the CAF-I histone chaperone led to increased pausing near splice sites but this observation was not pursued further.

Although no major breakthrough came out of this work, the dataset generated in this study represents a valuable resource for the "transcription community" (notwithstanding a concern described below).

Besides the lack of a major breakthrough, enthusiasm for the work in its current form is dampened mainly by the first two issues detailed below:

1) I am concerned that the conclusions about pausing might be mitigated by noise in the pause site calls. First, I was surprised to see that in most cases, deleting elongation factor genes led to decreased pausing. Intuitively, I would have expected elongation factors to help suppress pauses, not promote them. This is notably unexpected for the spt4 mutant since Spt4 has been clearly shown to suppress pausing, yet the NET-seq data suggest the opposite.

This peculiar observation (which is not commented on by authors) raised some suspicions about the pause site calls. Scrutinizing the NET-seq literature quickly revealed that NET-seq peaks can often occur consequent to technical artifacts (RNA processing intermediates, PCR duplicates, products of mispriming during RT, etc.). The Mayer lab recently published a version of NET-seq that limits these artifacts (https://doi.org/10.1093/nar/gkab208). Using this protocol, the Mayer lab found that mammalian Pol II pauses every 3,000-30,000 nucleotides. This is far less frequent than the 31 nucleotides suggested in the current work. While this may reflect differences between species, this reinforced my suspicions about these pause site calls. The sequence bias around paused sites is also different in the current study compared to previous work in mammals and E. coli, further suggesting that the current study might include a large number of artifactual pause site calls.

Can the authors comment on the possibility that some (perhaps a lot) of their called pause sites are not bona fide, and to what extent this might have affected their conclusions? Is it possible for them to leverage some of the improvements described in the Mayer paper to test whether this would affect some of their key conclusions?

2) I am concerned about the use of the antisense/sense ratio as a measure of antisense transcription. This is a convoluted measure that is affected both by changes in sense and antisense transcription. Hence, a change in the antisense/sense ratio simply can not be assimilated to an effect on antisense transcription; it may just as well reflect effects on sense transcription or a combination of both sense and antisense.

This mitigates several of the conclusions made by the authors. For example, on p.11: "This result implies that strong antisense pausing suppresses antisense transcription, perhaps by promoting termination and thereby preventing antisense transcription deep into gene bodies". This conclusion is mitigated by the use of antisense/sense ratio as a measure of antisense transcription. It appears just as possible that strong antisense pausing stimulates sense transcription.

Similarly, on p.18: "Indeed, differentially transcribed genes showed pronounced changes in their antisense:sense transcription ratios, especially for a subset of sensitive genes that are differentially transcribed in many of the deletion strains". By definition "differentially transcribed genes" means that sense transcription is affected. This alone will affect the antisense:sense ratio.

A measure of the absolute antisense transcription levels in WT and mutant strains should be attempted. While it may be difficult to compare such measurement across strains, it would - in principle - be a more accurate measure of antisense transcription. I suspect that most conclusions will remain, but the current analysis is simply not sound.

3) Figures 1 and 2 are quite descriptive and have some presentation challenges. For instance Figure 2D, E, & F appear to show very subtle changes. In the scale used for those figures it is difficult to see the changes that are occurring. It is recommended that a smaller range be used so that the changes can be more clearly visualized. Many of the changes have been previously reported although not using NET-Seq analysis to my knowledge. In these cases the NET-Seq data could be used as a higher quality resource and perhaps that aspect could be discussed (advantages, etc.).

4) Figure 3 presents some interesting data that are novel to my knowledge. These novel findings, such as the contribution of CAF-I to Pol II density changes at splice sites, should be discussed in more depth to increase the novelty of the work.

Other comments:

a) The title seems inappropriate. "Dynamics of transcription elongation" suggest that elongation parameters (speed and processivity) were assayed, which is not the case. Instead, the paper focuses on pausing and anti-sense transcription. While these phenomena are linked to elongation, this does not justify the current title.

b) I am surprised that histone chaperones notoriously linked to elongation (e.g. Spt6, FACT, Spt2, etc.) were not included in this study.

c) The abstract mentions co-transcriptional processing (presumably RNA processing). Yet, I do not think that RNA processing was monitored in this study (except perhaps for analyzing a published dataset for CAF-I).

d) check spelling of all forms of the word (and processes related to) ubiquitin. There are multiple spellings/typos.

e) Features for the AI modeling are described as "chromatin features" but use features both within and outside of chromatin considerations. I would consider renaming.

f) There is a missed opportunity for more in-depth discussion of transcription factor contribution to potential pause sites and for discussion of potential RNA binding protein contributions.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Transcription elongation is finely tuned by dozens of regulatory factors" for further consideration by eLife. Your revised article has been evaluated by James Manley (Senior Editor) and a Reviewing Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As this is a complicated paper with varying effects of different deletions etc. the reviewers thought that some issues need to be clarified in the text to make absolutely clear what robust conclusions can be drawn from this study.

Essential revisions:

1) The revised manuscript by Couvillion, Harlen, Lachance et al. is vastly improved. The authors have adequately addressed my main concerns. The only aspect that remains unclear to me concerns the fact that mutants for elongation factors such as dst1D and spt4D lead to decreased number of paused sites (Figure 4). As stated by the authors, this is unexpected since these factors are known to prevent (or help alleviate) pausing. Consistent with this expected behavior (and in apparent contradiction with the analysis shown in Figure 4), dst1D cells harbor a clear increase in Pol II density in the 5' region. This was highlighted in my initial review and the authors have addressed this by adding some speculations on page 12. This explanation, however, is vague and not compelling. One possible explanation would be that, in strains such as dst1D, pause sites are fewer but stronger. In this scenario, Pol II would pause less often but have a harder time getting out of the pause state in dst1D (and others) cells. Does the data allow testing this possibility? I feel that the manuscript would benefit from straightening that aspect.

2) For the most part my major concerns have been addressed. The reproducibility of the experiments was carefully assessed (Figure S5A & B) and the use of the irreproducibility discovery rate (IDR) with clear cutoffs sets clear quantitative standards for each dataset. It is clear that some of the knockout strains have a low overall impact on pausing and this is discussed through comparison of the median TSS pausing index.

3) Much of my major concern is with the use of a discussion of machine learning being used for prediction of pausing location. The machine learning section appears to more clearly provide new models for the contribution of different DNA/chromatin features to changes in pausing observed in any individual elongation factor deletion strain. This point can be addressed through writing to clarify what the machine learning analysis actually provides rather than what it could potentially do (predict pause sites) but appeared to fall short of.

4) I appreciate the care taken to address the concerns raised about the sense/antisense ratio analysis from the initial manuscript. This clarity of this section is much improved. I have a comment regarding this specific statement:

"The factors whose deletions led to the largest increase in the antisense transcription were those involved in the regulation of histone acetylation, including members of the Rpd3S-Set2 pathway (Set2) and the major histone H4 acetyltransferase complex NuA4 (Eaf1), emphasizing the role of acetylation in antisense transcription (Carrozza et al., 2005; Churchman and Weissman, 2011; Krogan et al., 2003; Murray et al., 2015; Murray and Mellor, 2016)."

For this statement, the deletion of an acetyltransferase will decrease acetylation whereas the deletion of members of the Rpd3S-Set2 pathway increase acetylation. As a consequence it is recommended to state "emphasizing the role of acetylation / deacetylation in antisense transcription" for clarity.
