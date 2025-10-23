# Peer review - Round 1

Reviewers:
- Jesse D Bloom, Fred Hutchinson Cancer Research Center , United States

## Review text

DOI: [10.7554/eLife.23156.026](https://doi.org/10.7554/eLife.23156.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Measuring the sequence-affinity landscape of antibodies with massively parallel titration curves" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Claudia Bank and Dmitriy Chudakov (peer reviewers).

I regret that after careful discussion with the reviewers, we have come to the decision to reject the manuscript in its current form.

All of us believe that your new approach is extremely exciting and potentially powerful. However, the reviewers identified a number of shortcomings that led us to decide against recommending acceptance of the manuscript. In particular, the manuscript as written clearly is fundamentally a methodology paper rather than a paper reporting a novel new biological result. However, many of the standards necessary to establish the robustness and reproducibility of a new method are not adequately met.

The policy of eLife is to not require revisions that would involve large amounts of new work, and as you will see below it would require substantial new work to address the concerns raised by the reviewers. We recognize that you may therefore either prefer to submit the paper elsewhere, or make extensive changes and re-submit to eLife. Below I outline what I consider to be the main points so that you are aware of them if you choose the latter route. In addition, the full reviewer comments are pasted below.

An experimental replicate is needed to assess reproducibility of the method. While we appreciate the effort to develop an error model using synonymous counts, for a new high-throughput methodology, the only robust ways to assess errors is to perform an independent replicate of the experiment and assess the variation between replicates. Replicates are a standard in recent deep mutational scanning studies (e.g. PMID 25723163, 25006036), and we would require one before accepting the paper. It is not essential that the replicates have perfect correlations (we don't expect that they will), but it is necessary to have some independent means of assessing the noise and validating which findings are robust to this noise.

Reviewer 2's point about what "experimental details" constrained the use of ligand values outside the KD range must be addressed – is the method inapplicable to antibodies with higher affinities? If so, that would be a very important limitation. This same point applies to the low-throughput assays. In the original Wittrup paper (cited in this manuscript), low-throughput replicates yielded KD estimates that varied by no more than 2-fold. Here, the KD estimates vary by two orders of magnitude. The reason appears to be that the range of ligand concentrations does not contain the KD, which is a basic requirement of a proper titration curve.

eLife's policy is to encourage making data and computer code available. We encourage you to do this regardless of whether you re-submit to eLife or elsewhere.

The reviews list a variety of other easy-to-fix points, such as better citations of the literature and clarification of unclear points.

Reviewer #1:

In this manuscript the authors present a new method called Tite-Seq to assess the effect of mutations in an antibody on antigen-binding affinity in a high-throughput fashion. They use their method on two regions of the scFv antibody and report a correlation between the number of contacts of a wt residue inside the antibody and its sensitivity to mutations.

Although my expertise in this area is limited, I am generally fascinated by novel high-throughput approaches, and I believe that the presented approach may prove useful to study antigen binding affinities on a large scale. However, I have several concerns regarding the validation of the approach and the appeal of the biological results.

Most importantly, I would like to see a true replicate experiment in order to get an idea of the correlation between measured values on a larger scale than just a couple of low-throughput comparisons. As far as I know, this is common practice when presenting a new approach like this, and it would (1) allow for a better idea of the error (which, in my opinion, is calculated in a highly optimistic way), and (2) allow for a much better quantification of the results. E.g., is the difference of 56% vs. 41% of mutations above the detection limit (in subsection “E. Differing effects of mutations in CDR1H and CDR3H”, first paragraph) a large one, or maybe not even distinguishable given the accuracy of the experiment? Even if the same library was used, a replicate of the subsequent steps would be highly informative, and, in my opinion, necessary for validation of the approach.

I do not see a striking biological result from the analysis. What occurs to me as the main result of the paper (the correlation between contacts of wt residue with sensitivity to mutations at that position) is not too surprising to me, given many studies that have shown protein stability to be an important determinant of its function (and, as I understand, the sensitivity is measured on an absolute scale). Other reported findings seem suspicious and vague, especially considering my main concern expressed above.

As I understand, 1850 mutations per region were surveyed. Such a high number introduces a lot of noise due to sampling by FACS and sequencing, even if the initial library is large and evenly distributed (and especially if the number of sequences is not large for some data points, cf. Figure 2—figure supplement 2B). I may have missed this, but is the distribution of the mutations in the initial library known, and what was the distribution of absolute reads per mutant at each data point?

Reviewer #2:

The authors present Tite-Seq, a method that uses high-throughput DNA sequencing of yeast-displayed antibody libraries to assess mutant KD and surface expression at a large scale. In general, the experiments and analysis are well executed, and the paper is mostly well written. My enthusiasm is restrained for two main reasons. First, the authors fail to cite and discuss substantially similar work. Their elucidation of KD values for a large library of variants does represent an advance, but it's incremental. The work must be discussed in the context of what has come before. Second, several of the analyses are poorly described and, if I understood them correctly, will inflate the reader's confidence in the method. In particular, the method for estimating error for each KD value is insufficient. Both of these points are particularly important because the manuscript is focused on the method itself rather than an important/exciting application. I therefore do not recommend publication of the manuscript in its current form.

Specific comments:

Introduction – The authors should be more thorough in discussing the strengths and weaknesses of prior deep mutational scanning work. In particular, the fact that yeast display has been coupled to deep mutational scanning and that affinity ranking of variants has been achieved is something readers should know before they get to the end of the Discussion (PMID 25311858). Mammalian antibody display has also been coupled to deep mutationals canning (PMID 23765106). Ribosome antibody display and deep mutational scanning using varying ligand concentrations has also been done (PMID 23103372). Of course, the existence of a substantially similar paper (PMID 26296891) should also be acknowledged and the work discussed in that context.

Subsection “C. Low-throughput validation experiments” – The authors show low-throughput validation data for three clones and compare this data to Tite-Seq results. In the subsection “A. Overview of Tite-Seq”, the authors make the point that, if curve fitting is to be successful, the KD value must fall within the range of ligand values used. However, for the validation data shown, the fit KD values are generally at the very low end of the ligand concentration range. In Figure 3, most of the titration curves more closely resemble flat lines. This can be explained by the fact that the KD of the WT is 0.7e-9 M whereas the lowest concentration of ligand used was 1e-8.5 M. I am puzzled as to why the authors chose to employ a ligand concentration range that did not include the known KD of the WT sequence. In the Discussion they mention "experimental details," that constrained them, but I'd suggest a fuller and earlier disclosure of these limitations. Given that most antibody-antigen interactions have KDs at least as low as the one studied, I wonder whether the method could really be generally applied.

Subsection “C. Low-throughput validation experiments” – Pursuant to the previous comment, the authors' simulations (Figure 1) are done using two hypothetical interactions whose KDs are substantially higher than the experimental case considered. They should do simulations using the actual KD and ligand concentrations employed.

Subsection “C. Low-throughput validation experiments” – The low-throughput validation experiments do not themselves look particularly robust. The KD values inferred from these experiments range over two orders of magnitude. The authors state "Although individual data points can be noisy, fitting curves to multiple data points nevertheless provide reasonably accurate measurements of affinity. The accuracy of these measurements is increase by averaging over replicates." This is a vague statement. How noisy? How much does replication help? A key problem, I think, is that the low throughput flow validation data looks as noisy as the Tite-Seq data. These experiments should be improved and repeated. Even better, an orthogonal method of validation should be employed.

Figure 2D – This panel and accompanying figure legend is vague. The text makes it clear that the numbers show the diversity of each library, but it would be helpful to clarify the legend.

Figure 4A/subsection “D. Tite-Seq can measure dissociation constants” – In the figure legend the authors state "Error bars on flow KD values are the same for all data points; they show the average mean squared error computed computed using three replicate measurements for each clone." In the text, they state "Error bars on flow cytometry KD values were computed using the average variance observed in replicate measurements." I have a few problems here. First, neither statement makes totally clear what the authors did/what is shown in Figure 4A. Furthermore, MSE usually used when the parametric value of an estimator is known. For the flow data, we don't have parametric values, just three replicates. So, a confidence interval would be more appropriate. Finally, and most troublingly, the authors have elected to present the mean variance/MSE of all three clones rather than the variance (or CI, or whatever) of each clone independently. I can't think of a good reason to do this. Because the WT replicates happened to look great while the two clones didn't, using the mean of all three is misleading. The authors should improve this analysis and then better explain it. Also, note the repeated "computed."

Figure 4B/Subsection “D. Tite-Seq can measure dissociation constants” – The error estimation procedure for Tite-Seq, based on a single experiment, uses synonymous variants to estimate the standard deviation of each measurement. Variants are binned based on read depth and then a regression is performed to determine the error in each bin. If I understood the procedure, the error is assumed to be wholly dependent on read depth. The read depth vs. signal to noise/error plot (Figure 4B) is really noisy, which suggests that the read depth alone does not capture all of the error. Many factors are known to impact experiment-to-experiment variability (e.g. PCR bias, experimenter error, etc.) in these types of experiments. Replication would enable much more robust error estimation, and would considerably strengthen the work.

Subsection “D. Tite-Seq can measure dissociation constants” – The authors state: "We note that…measurements for the WT scFV are about a factor of 10 larger than the previously measured value of KD". I wonder if this is due to the lack of data points at lower concentrations rather than any differences in buffer/etc. Again, a gold-standard, non flow-based assay would help here.

Figure 6A – Because of the two-dimensional heatmap it is somewhat difficult to appreciate the relationship between expression and binding. Two separate panels with individual color schemes might be easier to comprehend.

Appendix C – The authors say they used custom microarray nucleotides to generate the library, but the nature of the sequences on the array is unclear. A supplementary data file containing the sequences ordered should be included.

Appendix F – The authors used the 10% lowest fluorescence values to estimate autofluorescence/background. This is a curious choice, if the library contained mutations to stop codons (see comment above). Stop codons, particularly early ones, virtually guarantee loss of function.

Reviewer #3:

I could hardly evaluate the mathematical aspects of the work. However, it looks like the previous expertise of this team ensures the high mathematical quality.

Concerning the whole idea of the work – I believe it is brilliant.

The approach allows studying the aspects of dependence of antibody affinity and potentially cross-reactivity (with several antigens used) on the sequence landscape, which is beautiful.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your heavily revised manuscript "Measuring the sequence-affinity landscape of antibodies with massively parallel titration curves" for consideration by eLife. The manuscript was evaluated by three reviewers who are experts in the field: two were also reviewers for the original submission, and one is a new reviewer. The evaluation has been overseen by Jesse Bloom as the Reviewing Editor and Aviv Regev as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Timothy A Whitehead (Reviewer #1) and Claudia Bank (Reviewer #2).

We anticipate that we can accept your manuscript for publication provided that you make revisions that address the comments below.

First, we appreciate your careful attention to addressing the issues raised in the in the initial review, particularly adding replicates and extending the antigen range. We recognize that these were time-consuming changes, and the seriousness with which you took those critiques has greatly improved this paper. Your study now represents an impressive use of deep sequencing to obtain fairly rigorous KD values.

Specific points:

1) Please make sure that your deep sequencing data is available on the SRA and relevant computer code is available as supporting file or on a publicly accessible repository. If this is already the case, please clearly indicate in the manuscript where these can be found.

2) There are a few additional papers that you should consider discussing in the context of prior work:

Doolan KM, Colby DW: Conformation-dependent epitopes recognized by prion protein antibodies probed using mutational scanning and deep sequencing. J. Mol. Biol. 2015, 427:328-340.

Van Blarcom T, Rossi A, Foletti D, Sundar P, Pitts S, Bee C, Melton Witt J, Melton Z, Hasa-Moreno A, Shaughnessy L, et al.: Precise and efficient antibody epitope determination through library design, yeast display and next-generation sequencing. J. Mol. Biol. 2015, 427:1513-1534.

3) Your approach estimates fairly accurate KD at the cost of more experiments (multiple binds, multiple expression levels). For certain applications where precise KD values are overkill, it may be more efficacious to use the simpler designs like those used in some of the references that you cite – perhaps worth mentioning. Also, do you have any comments on the trade-off between sequencing depth and the accuracy of the inferred KD? Similarly for the number of sorting bins? Right now it isn't clear how these were chosen. Clearly your choices worked fine, but it would be nice to explain if there was rigorous rationale for choosing these (alternatively, you could just say that exploring the effects of these parameters is interesting for future work).

4) The relatively large unsigned error on two variants in Figure 4C (approximately 2 orders of magnitude in KD) should be commented on. Why is there such a discrepancy (Subsection “D. Tite-Seq can measure dissociation constants”; Figure 4C)?

5) Are the mutations outside of the dynamic range (KD > 10 μM) being used in determining correlation coefficients (Figure 4C; Figure 4—figure supplement 1; Figure 4—figure supplement 2)?

6) Please quantify the error in precision and accuracy of the method. In particular, the poorer correspondence between replicates in the binding range between 10-1000 nM KD should be mentioned.

7) Can you quantify error within replicates by inferring KD for synonymous mutations?

8) How big is the benefit of controlling for active surface-displayed protein? While it is clear that yeast surface expression and folded surface displayed protein varies between variants (Burns et al., 2014), it has been shown (yet still surprising!) that surface expression (and proper folding) effects are modest for yeast surface display experiments, particularly for residues that are reasonably surface-exposed (Kowalsky and Whitehead, 2016).

Burns, Michael L., et al. Directed evolution of brain-derived neurotrophic factor for improved folding and expression in Saccharomyces cerevisiae. Applied and environmental microbiology 2014, 80:5732-5742.

Kowalsky CA, Whitehead TA Determination of binding affinity upon mutation for type I dockerin-cohesin complexes from Clostridium thermocellum and Clostridium cellulolyticum using deep sequencing. PROTEINS 2016 84: 1914-1928
