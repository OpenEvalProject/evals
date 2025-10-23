# Peer review - Round 1

Editors:
- Frederik Graw, Heidelberg University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67092.sa1](https://doi.org/10.7554/eLife.67092.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The presented manuscript takes a very comprehensive and elaborated look at how T cell receptors (TCR) discriminate between self and non-self antigens. By combining experimental and analytical methods, the presented findings challenge commonly held notions and could be fundamental for our understanding of the T cell immune response, with implications for autoimmunity and immunity to cancer.

Decision letter after peer review:

Thank you for submitting your article "The discriminatory power of the T cell receptor" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tadatsugu Taniguchi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers appreciated the elaborated and thorough analyses presented in this paper. The detailed comments (see below) address some specific points that the reviewers noted. In particular this concerns the following main aspects that should be addressed in a revised version of this manuscript:

1. Please address some points regarding possible overfitting and parameter identification within the mathematical analyses.

2. Please comment on the ability of the current Kinetic proofreading model to explain antagonism

The detailed comments of the reviewers are as follows:

Reviewer #1 (Recommendations for the authors):

– The authors state that when fitting the 2-parameter Hill-function to the TCR binding curves, that different combinations of Bmax and KD are suggested to explain the data if Bmax was estimated. The coefficient of variance was used to assess this effect but wouldn't it be more straightforward to use methods such as Profile likelihood analysis to clearly address parameter non-identifiability?

Reviewer #2:

1. Please further clarify and explain the extrapolation of the connection between Bmax of the TRC-peptide binding curve and W6/32 binding curves based on Figure 1D.

1.1. Cosmetic – the color coding in 1B is a bit confusing because the same color palette denotes different concentrations of the same peptide here as the one denoting different peptides in 1D.

2. Please address the potential overfitting issue in the KPR model, and the parameter value spread in Figure S8.

3. Please comment on how the current model relates to antagonism, which is commonly considered a typical feature of TCR signaling

Reviewer #3:

As came probably through already in the other review sections I feel enthusiastic about the work presented as it combines a massive volume of bench work-related data with relatively simple math (with the exception of the section dealing with KP) and it leads to testable clear hypotheses. The latter may be the tasks of others (or not), and hence I consider the manuscript close to being appropriate for publishing.

Here are a few suggestions I consider useful for the reproducibility and readability by others.

i. A detailed description of the SPR-protocol including primary data would render the reading more complete. The methods section is already fairly detailed, but it would be more than helpful to understand how the streptavidin and pMHC-bio run, as well as the TCR-runs and the final W6/32 run were computed against one another to arrive a the Bmax of low affinity ligands. TCR-binding to pMHC (even if saturated) will result in a different SPR signal than antibody binding (given the different molecular masses). Since this methodology is central to the manuscript, I would argue in favor of introducing it more thoroughly in Figure 1A (and B, with representative raw data leading to corrected Bmax). This may also help to understand why the addition of W6/32 in both panels of figure 1B led to a much lower signal than the highest concentration of TCR.

ii. After lentiviral infection of primary T cells, how did the authors monitor the expression levels of the introduced TCRs? How did they verify the absence of mixed TCR dimers? Since TCR expression levels are clearly important in the overall scenario analyzed, I believe this is a fair question to ask.

iii. I find it somewhat unusual (if not irritating) to find already published data in main figures. An in my opinion better approach is to cite the work and show exclusively the processed data (taken from cited work, in the lower panel of Figure 3A, B,C etc.).

iv. The Discussion section would benefit from a short paragraph reflecting on work on TCR-pMHC binding as measured within the confines of the immunological synapse. Reasons are that binding constants (if there is such a thing in synapses) differ in some cases substantially from what has been measured via SPR for reasons that are still being debated. Clearly, one major strength of this manuscript is that cellular behavior correlates with SPR measurements of TCR-pMHC binding. Nonetheless scenarios, especially those involving KP, may turn out differently in case serial TCR engagement by few antigens is supported.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The discriminatory power of the T cell receptor" for further consideration by eLife. Your revised article has been evaluated by Tadatsugu Taniguchi as the Senior Editor and a Reviewing Editor, as well as the original reviewers of your paper.

They all appreciate the elaborated and thorough analyses presented in the paper, and also appreciate the additional work that had been done to address the previous comments of the reviewers. The manuscript has been improved, but there are some remaining issues that need to be addressed, as outlined below:

1. One remaining concern mainly addresses the interpretation of the relationship between the values of Bmax and the AB binding to pMHC in Figure 1D. The data suggest that this linear relationship could be extrapolated to very weak pMHC's but it does not need to be the case (see also comment reviewer 2). Although this is acknowledged in your statement (line 95-96), we recommend to discuss this in more detail. It seems that this assumption mainly drives the selection for the method to analyze the low affinities, with Bmax constrained by this relationship. We would recommend to acknowledge this in your discussion or provide additional evidence.

2. There are some issues with regard to the presentation in Figure 1D that should be addressed.

Please also see the specific comments of the reviewers below.

Reviewer #2 (Recommendations for the authors):

I am still somewhat confused about the correspondence between the TCR Bmax of binding to pMHCs in figure 1 B, but I think the importance of the results is compelling, and I am happy if this debate plays out in the literature rather than here. To summarize:

1. It still looks (to me) that the linear relationship between Ab binding to pMHC and the B-max of the TCR binding is just an empirical finding, and although the data does suggest it might continue for very weak pMHC's I don’t see why it would be guaranteed. On the same note, the authors say in their response, " W6/32 is a conformationally-sensitive antibody that does not depend on the precise peptide sequence" – which on its face contradicts the fact that the response to W6/32 is different to different peptides in figure 1 D.

Please discuss.

2. I am still confused about the legend in Figure 1D. For instance, black dot is supposed to be Tax WT pMHC for A6 TCR – why are there four different black dots in the plot, with completely different B-max? Same question for NYE 9V. Finally filled orange dots are supposed to be Tax 1M. So what are the empty orange circles – they are not indicated in the legend, as far as I can see? The open purple circles appear in the plot but not in the legend. By contrast, open pink circle is indicated in the legend but does not seem to appear in the plot. Etc. If this is just mis-labeling it should be corrected and better explained in the text/caption.

3. Figure 1C, left is supposed to show the binding curve for WT NY-ESO-1 pMHC but it is not shown in Figure 1B – why? Similarly, I could not find in the text what peptide is the Figure 1C, right for? In either case, it should be better explained in the text/caption

Reviewer #3 (Recommendations for the authors):

The authors have addressed all issues I have raised in my previous review in a satisfactory manner. I enthusiastically recommend publishing their work in eLife.
