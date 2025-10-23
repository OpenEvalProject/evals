# Peer review - Round 1

Editors:
- Benny Chain, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68605.sa0](https://doi.org/10.7554/eLife.68605.sa0)

This paper introduces and validates a novel concept which will be of great interest to all those interested in T cell immunity and especially the T cell receptor repertoire. The concept builds on the idea that TCRs to the same antigen often share sequence similarities, which they quantify using a bespoke tool tcrdist3. Using this tool they develop the idea of a meta-clone, a set of TCRs sharing biochemical similarities and potentially recognising the same antigen. In this paper they further show that such clonotypes may show increased sharing between HLA-related individuals, and explore the use of such clonotypes in characterising antigen-specific immune response across cohorts of individuals.


---

# Peer review - Round 1

Editors:
- Benny Chain, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68605.sa1](https://doi.org/10.7554/eLife.68605.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "TCR meta-clonotypes for biomarker discovery with tcrdist3 enabled identification of public, HLA-restricted, SARS-CoV-2 associated TCR features" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Benny Chain as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tahel Ronel (Reviewer #3).

The reviewers are all agreed that the content of the paper is of interest to the readership of the journal. However, they are also agreed that significant revisions are necessary to increase the impact of the paper, and we would like to invite you to submit a revised version of the manuscript.

Please address the detailed comments from all three reviewers and provide a point-by-point response. In particular, the emphasis of the paper needs to be shifted from COVID to the idea of the meta-clonotype. In order to achieve this, and to make the maximum impact, the paper must be thoroughly revised, to provide much more detail and clarity on the definition/construction of meta-clones, and how they can be used to define antigen-specific responses.

Reviewer #1 (Recommendations for the authors):

The authors should sharpen the manuscript to focus it exclusively on evaluating their new concept of a meta-clonotype, and not on evaluating the MIRA-based SARS-Cov-2 data set. For example, Lines 302-325 – what is the relevance of this section ? It analyses the MIRA dataset, and suggests the peptide-specific responses show HLA preference (hardly surprising) but doesn't say anything about the meta clonotypes.

The extension of TCRdist to gamma/delta cells seems irrelevant to this paper. No gamma-delta data are evaluated.

I found the section 560-574 (the details of generating the meta-clonotypes) very hard to follow. This is surely the crux of the whole paper, and the method for generating meta-clonotypes needs to be crystal clear. For example what does "With each candidate centroid, a meta-clonotype was engineered by selecting the maximum distance radius that still controlled the number of neighboring TCRs in the weighted unenriched background to 1 in 106". How do you reach 106 with only 200000 background TCRs?

Critically , in order to increase the impact of this study, it would be important to show that meta-clonotypes perform better than public clonotypes in identifying COVID-infected individuals (as done for clonotypes for CMV in Emerson et al. Nature Genetics 49,659).

Reviewer #2 (Recommendations for the authors):

Title: It's a bit strange to refer to meta-clonotypes as features (especially since machine learning was not performed). Also. the term feature does not have the same meaning throughout the manuscript. Can you adjust the title to be a bit more direct and less confusing?

Abstract: "As the mechanistic basis of adaptive cellular antigen recognition, T cell receptors (TCRs) encode" → this sentence doesn't make sense. There are many mechanisms involved in immune recognition (binding, proliferation etc…), TCR sequences are certainly a part of it but I would hardly call them the "mechanistic basis" – can you rephrase? I would like the term "mechanistic" to go – this paper is not mechanistic in any way.

"17 SARS-CoV-2 antigen-enriched repertoires" → antigen-enriched doesn't mean what you think it means. Can you please rephrase throughout the manuscript? What you mean is antigen-annotated/antigen-specific/etc…

Introduction: The introduction seems a bit verbose (the entire paper is quite verbose…more streamlining by making text and captions more precise would greatly enhance readability). This is not a covid-centric paper – please dramatically reduce the SARS-CoV-2 section. Also, the first paragraph can be written in 5 instead of 35 lines. Please try to get closer to one page overall.

Results Figure 1A: what does "searchable public meta-clonotype" mean? It's not mentioned anywhere else in the text.

I think it would be much more useful to the reader if you illustrate how tcrdist calculates tdus, how they are to be interpreted (you mention in the text: 1 aa mismatch is 12 tdus – this is great and would be nice to see in Figure 1A for example).

Figure 1B In my opinion, the figure does not reflect what you want it to say (quantification of the frequency of putative meta-clonotypes). Please adjust the figure accordingly.

Figure 2A "As the radius about a TCR centroid expands, the number of TCRs it encompasses naturally increases; the rate of increase is more rapid in the antigen-enriched 167 repertoires compared to the unenriched repertoires" → can you quantify this rate? How does the rate depend on sequencing depth? Can you also add the OLGA-generated data to this plot? Is your assumption that the OLGA-generated data would perform close to that of the cord blood data?

For all figures: can you change the bold text of the caption to the main result of the figure. As of now, the bold text doesn't really say much.

If I do a text search in the main text for "Dash BMLF", I don't find anything. Please define all named datasets in the methods/main text.

Regarding the antigen-specific data – is the higher rate in antigen-specific data due to the fact that you are focusing on only a few peptides here? Would the rate be similar to the baseline data if you somehow normalized for that? Like for example only taking one tcr per peptide? Probably not possible, right, given the sparsity of the data..?

How does Tcrdist3 normalize for length differences? Do these curves differ across tcr length, germline genes?

Figure 2B

Can you explain in the main text and the methods what MIRA M48 means –specifically, what do each of the numbers mean?

Figure 3

"This suggests that TCRs within sparse neighborhoods represent less common modes of antigen recognition and highlights the broad heterogeneity of neighborhood densities even among TCRs recognizing a single pMHC." → to what extent can TCRs with sparse neighborhood be a result of undersampling?

Can you add OLGA-generated data to Figure 3 as well?

Figure 4

Can you mention in the caption how many TCRs you are investigating in this subfigure? Please also check for all other figures where relevant.

"We also noted that TCRs with 191 empty neighborhoods tended to have longer CDR3 loops (Figure 4C)" Where and how do I see this in Figure 4C?

"To be useful, a meta-clonotype definition should be broad enough 206 to capture multiple biochemically similar TCRs" → what do you mean by biochemically similar? I think, in the AIRR field, when people speak of biochemically similar, they mean something related to Atchley/Kidera factors. I don't think this is what you mean here, right? Maybe rephrase to avoid misunderstandings?

"This is similar to previous approaches taken by tools like ALICE and TCRNET, except that we employ a biochemically informed distance measure (TCRdist)" → this statement is a bit indirect for my taste. Can you rephrase and make it really clear in what respect tcrdist3 differs from Alice et al.?

How did you decide on the number of 100000 IGOR and cord blood TCRs?

"One part consisted of 100,000 synthetic TCRs whose TRBV- and TRBJ-gene frequencies matched those in the antigen-enriched repertoire; TCRs were generated using the software OLGA" → how did you make sure that frequencies matched?

"Using this approach, we are able to estimate the abundance of TCRs similar to a centroid TCR in an unenriched background repertoire of effectively ~1,000,000 TCRs," → Where does the number of 1M TCRs come from? Can you show that calculations don't change if you sample another 100000? To what extent do you think it plays a role that the cord blood data has been generated with a completely different experimental protocol than the MIRA data?

Figure 5

Can you please add to "HLA genotype inferences" section in Methods the prediction accuracies for HLA-B alleles used in Figure 5A? If prediction accuracies are low, please remove those data also from Figure 5A.

Is the HLA-classifier publicly available? Does a package for it exist as well? Which HLA alleles other than those mentioned are quite safe to predict from sequencing data?

Independently of Figure 5, is there a Figure where I see how much meta-clonotypes make up of a repertoire in terms of sequences and sequencing reads? Basically, how much more of the antigen-specific portion of a repertoire does one capture if looking at meta-clonotypes?

Furthermore, how do you compare meta-clonotypes across individuals (publicity)? Can a TCR be part of several meta-clonotypes? Can you explain all of this more in Figure 1 and the main text?

Figure 7

To what extent is this figure needed in the main text?

Since your approach is actually quite similar to Alice, especially, since you include in your analysis pgens, wouldn't it be more interesting to relate in depth to Alice than to GLIPH?

GLIPH2 was used with the default TCR background (line 629). Would this give the TCRdist3 meta-clonotypes an advantage, since the used background for TCRdist3 has been more densely sampled around the biochemical neighborhoods of interest (line 563)?

In the comparison to k-mer based CDR3 features, were meta-clonotypes defined by RADIUS or RADIUS +MOTIF? Please also mention this in Figure 7.

More general comments:

The paper presents meta-clonotypes as a novel approach to comparing similar TCRs across repertoires and mainly compares the meta-clonotypes approach to the use of public exact TCRs. This comparison seems a bit trivial since any sequence similarity clustering approach is expected to perform better than exact TCR matches. I think it's very interesting to show that meta-clonotype spaces differ between antigen-specific and non-specific repertoires. It would have been nice to focus the analysis more on this and to actually discover something cool about the repertoire biology than trying to relate exclusively to covid.

How does your method compare to this recently published approach based on TCR sub-repertoires shared across individuals? https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-021-04087-7

Reviewer #3 (Recommendations for the authors):

The methodology proposed in this manuscript (tcrdist3) has been made publicly available through GitHub. The application to COVID-19 is based on public datasets and is clearly referenced. Data derived in the analysis, such as NetMHCpan predictions and the set of derived meta-clonotypes are included as supplementary material, which is helpful and adheres to eLife's policies.

The dataset of derived COVID-19 related meta-clonotypes is a valuable resource for the analysis of other bulk repertoire COVID-19 datasets, and the proposed method should be applicable in a variety of antigenic settings. This dataset could be further characterised, perhaps as a supplementary/additional figure: the distribution of optimal radii, distribution of number of TCRs conforming to each meta-clonotype, number of people contributing TCRs to the meta-clonotype, are these different between the strong HLA meta-clonotypes and weak HLA meta-clonotypes? This would help when applying the method in other contexts.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "TCR meta-clonotypes for biomarker discovery with tcrdist3 enabled identification of public, HLA-restricted clusters of SARS-CoV-2 TCRs" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor.

The reviewers agree that the manuscript has been considerably improved but there are a few remaining issues of clarity that need to be addressed, as outlined below by reviewer 3.

Specifically:

1. Please include a clear and consistent definition of a meta-clone in the Discussion. If in fact there are multiple alternative definitions, please clearly set these out, with an indication of when each would be used.

2. Clearly indicate which background set is used in each figure/section of the paper.

3. Further sharpen the Discussion around comparing the meta-clonotype approach to other existing methods. Specifically, please clarify the relative importance to the novel meta-clonotype defining which derives from the new TCRdist3 metric, the motif, and the novel approach to establishing background comparisons.

The comments of the reviewers are listed below.

Reviewer #2 (Recommendations for the authors):

The authors have addressed all of my comments.

Reviewer #3 (Recommendations for the authors):

The authors have placed more focus in the revised manuscript on the definition and generation of meta-clonotypes, as suggested, with the covid data used as an example application. They have included a couple of new analyses to this effect (background sets 'sensitivity analysis', logo sequence characterisation). While I still think that the idea of meta-clonotypes is both interesting and potentially useful, I find some of the paper a bit long and difficult to follow.

For example, it looks to me like the definition of meta-clonotype changes along the paper: e.g. In Figure 1/Figure 6 a meta-clonotype is centroid (TRBV + CDR3) + radius +/- motif; in Figure 10 it also includes what I think is an identifier for the set it comes from; and in Figure 12 it is TRBV + TRBJ + CDR3 + radius. As this is the main focus of the paper I think this definition should be made clear, consistent and explained somewhere.

Secondly, it was unclear to me when the authors use which set for background: e.g. does Figure 1 and caption 'synthetic set' refer to the set of 100k OLGA V-J biased + 100k cord used later? cf Lines 535-537 "background CDR3s that were sampled from cord blood and constrained to use the same V and J genes", and elsewhere unadjusted cord blood is used without the OLGA adjusted set.

I also think that the advantage / unique usage of the proposed meta-clonotype method over existing methods for grouping antigen-specific TCRs should be further clarified and emphasised: I personally don't find the Results section 'Comparison to k-mer based CDR3 features' or Figures 11 and 12 very convincing to this effect, and think this message should be made clearer in the paper before the sentence in the discussion "Our framework is designed for a different task than these algorithms…".

I do think the meta-clonotype method is useful, these changes are addressable and the paper has the potential to be made more readable and more impactful, if the authors streamline the definition and explanations, remove repetitive sections, and cross-reference to the relevant places in the text where things are referred to in the text before their explanations.
