# Peer review - Round 1

Editors:
- Lindsay Cowell, https://ror.org/05byvp690 The University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86181.sa0](https://doi.org/10.7554/eLife.86181.sa0)

This fundamental study provides a new, high-performance algorithm for B-cell clonal family inference. The new algorithm is highly innovative and based on a rigorous probabilistic analysis of the relevant biological processes and their imprint on the resulting sequences. The strength of evidence regarding the algorithm's performance is convincing, as the algorithm has been benchmarked against two state-of-the-art methods for clonal family inference on two synthetic data sets generated with two independent, state-of-the-art methods for B cell repertoire simulation. This work will be fundamental to immunologists and important to any researcher or clinician utilizing B cell receptor repertoires in their field.


---

# Peer review - Round 1

Editors:
- Lindsay Cowell, https://ror.org/05byvp690 The University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86181.sa1](https://doi.org/10.7554/eLife.86181.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Combining mutation and recombination statistics to infer clonal families in antibody repertoires" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Frederick A Matsen (Reviewer #2); Kenneth B Hoehn (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Provide clarification regarding how different data sets (synthetic versus real) were used for different steps during algorithm development and validation, perhaps by including a flow chart of inputs/outputs/dependencies.

2) Conduct an evaluation that is not circular, such as using additional simulated data sets beyond the one based on the same data used to develop the method.

3) Provide details about the versions and settings of the competitor programs included in the benchmarking, as well as other general information such as: what type of machine was used? Was the use of multiple threads enabled for all programs? When multiple methods are available within a single program (e.g., scoper), indicate which were used and justify the choice. Etc.

4) Make the synthetic data publicly available as well as the scripts used for the benchmarking analysis.

5) Define "precision" prominently and use it in that sense consistently throughout the manuscript.

Reviewer #1 (Recommendations for the authors):

Regarding point 1 in the public review, examples of more specific questions along these lines are included below. A flow chart figure showing the steps, data inputs, and parameter outputs would clarify the presentation and may in turn resolve any concerns about the strength of evidence.

Additional Major Comments/Questions

1) The data in reference [1] derive from RNA-seq. The authors mention the use of UMIs to correct PCR amplification, but how do they deconvolute clonal expansion from transcript abundance? This is a major issue when using RNA-seq data for which cells were not barcoded.

2) It is not clear what data is being used for which procedures. When is real data being used versus when is synthetic data being used?

a) Page 3: "Fitting is performed with an expectation-maximization algorithm which finds maximum-likelihood estimates of the prevalence ˆρ and mean intrafamily distance ˆµ for each VJl class." Was the fit with synthetic data generated using soNNia, as indicated for P0(x)? Or real data from [1], as indicated in Figure 1A?

b) Page 3: What data were used for Figures 1B-1I? Data from reference [1] are used in A, and the dashed lines in J are from synthetic data. What about the rest? All from [1]?

c) Similar questions persist throughout.

3) The authors need to be clear when they are drawing conclusions from real data versus from synthetic data. And in general, real data should be used as much as possible, since synthetic data is limited due to the generation process being based only on what we think we already know. On the other hand, I understand that for real data, we don't ever have gold standard labels, so a careful balance of the two is needed.

a) Page 3: "P0(x) = P0(x|l) is computed for each length l by generating a large number of unrelated, same-length sequences with the soNNia model of recombination and selection [19], and calculating the distribution of their pairwise distances." How does this compare to using real data? What if you, e.g., take all singletons in a real dataset? Wouldn't that also approximate P0(x)? Figure 2G shows the peak of the distribution of x at 0.5, half of all nucleotide positions differ; assuming this is from simulated data, is this what you would get with real data? Or vice versa.

b) Page 3: "The results of the fit show that ˆµ varies little between VJl classes, around ˆµ ∼ 4%." Is this based on real or synthetic data? If synthetic data, does this just depend on how you wrote the generation process? This may be related to the questions below regarding how mutations were identified and characterized and then applied in the data generation process.

c) Page 3: "In contrast, the prevalence ˆρ varies widely across classes". Again, real or synthetic data? If synthetic, doesn't this depend on the generation process? If real data, is there any association with l?

d) Similar questions persist throughout.

4) Page 4: "it is expected to fail when the prevalence and the CDR3 length are both low." A single value rho can encompass a large number of small clones or a small number of large clones, but rho seems to be treated in the model as a repertoire level rho, the proportion of all pairs that are related. How does this impact the interpretation/expectation of the approach's performance across different tissue types or B cell subsets that may be expected to have very different clonal distributions that are averaged out to a single rho in the model?

5) Page 4: "We first estimated the distribution of clonal family sizes from the data of [1] by applying the CDR3-based clustering method with adaptive threshold.… to VJl classes for which.… the predicted sensitivity was >90%." Does this mean VJl classes with e.g., l>30? (inferring from Figure 2I) Or what does this mean? Could focusing only on these clusters bias the estimated distribution of clone sizes?

6) Page 4: "For each lineage we draw a random progenitor using soNNia". I assume these are lineages for the synthetic data, but it isn't clear from the text that you aren't sampling from the lineages created for [1]. Similarly, on page 10: "To generate synthetic data we make use of the lineages identified in the high-sensitivity and high-precision regime of CDR3-based inference (Figure 3F), we denote the set of these lineages by L." That means you use the lineages identified in the data from [1]? And should the figure reference be 3E?

7) Page 4: "Mutations are then randomly drawn on each sequence of the lineage in a way that preserves the mutation sharing patterns observed in families of comparable size from the partitioned data". What partitioned data? Data from reference [1]? And how were the mutation patterns characterized so they could be replicated? From page 10: "We then identify all unique mutations in the true lineage and for each mutation denote the labels of members of the lineage that carry it." How are "all unique mutations in the true lineage" identified at scale? And how is the "true lineage" identified? Using the approach being developed, I think, so this all seems a bit circular.…

8) Page 11: "We compute the expected distributions of the CDR3 Hamming distance n, and the number of shared mutations n0, under a uniform mutation rate assumption. In other words, we assume that the probability that a given position was mutated, given a mutation happened somewhere in a sequence of length L, equals L^{-1}." I think it is well-known that this is not the case. What are the implications for the evaluation of model performance?

Reviewer #2 (Recommendations for the authors):

Please add line numbers: they make reviewing much easier.

Overall it would be helpful to understand how "precision" is used. "High-precision" comes up a lot, including in the HILARy acronym, and it seems that sometimes it's used as a synonym for accuracy. Or is it literally "precision" in the technical sense, i.e. contrasted to recall/sensitivity?

The mathematical exposition is nicely laid out. However, the choices of symbols can make it difficult to follow, and the reader has to keep a lot of arbitrarily-chosen notation in their head to follow and read figures. A notation table would help, as would more self-explanatory naming choices for key variables like x, y, n, and n_0. For example, it would make things easier to read to use something like P_F rather than P_0, and P_T rather than P_1. 0 and 1 subscripts are used in a different context when used as a subscript in equation (4), which makes this equation difficult to parse: sometimes 1 means the number of mutations in sequence 1, and sometimes it means the same-lineage assumption.

Results

A

- "which consists in" suggest "which consists of"

- prevalence is a key definition, and right now it's tacked onto the end of a sentence. Suggest making it a stand-alone definition for clarity.

- "share the same V and J gene usage" suggest "share the same V and J genes"

- "The signature of the VDJ rearrangement is largely encoded by the CDR3 alone" this statement seems over-strong-- the parts of V genes within the CDR3 are frequently identical.

- Productive sequences are often defined as not only cdr3 length divisible by 3, but also V and J in frame (indels could change that).

- "same-length sequences with the soNNia model": do these include mutation?

- If I understand correctly the Poisson distribution models the distribution of distances within a clonal family, and so mu is a function of the distribution of the number of somatic hypermutations. If this is correct, it would be helpful to include this interpretation.

- "μ varies little between VJl classes, around ˆμ ∼ 4%": suggest using $\simeq$ for approximate as done below

- "that the positive mode P1(x) of the distribution varies little," suggest "… the mode of the positive distribution P_1(x)"

B

- Suggest mentioning that the results here depend on the level of SHM.

C

- "verify that these performance predictions hold in real inference tasks": I would recommend "realistic" rather than "real", the latter of which sounds like you mean real data.

D

- Below (4), _1 should be _1.

- Suggest using more precise language to define n rather than "divergence", describing that this is about pairs of sequences.

- "computationally expansive" should be "computationally expensive"

Figure 3

- What causes the three bent stripes in C?

- It would be really interesting to know how this plot changes with SHM: in C, higher SHM will result in more divergence among positive CDR3s (more density at higher x).

Perhaps this will be offset by more shared mutation (i.e. maybe new high-SHM points will stay above your straight line x'-y=t'), but it would be really great to find out.

- I don't think it's clear either here or in the text what is actually done with the high-precision and high-sensitivity partitions.

The bottom right of p5 (in Results) partially explains a use for the high-sensitivity one (but not high-precision), and the D section of Methods describes how to calculate them (but not what is done with them).

F

- How was dN/dS calculated? Traditionally this has been done in a maximum-likelihood setting to calculate rates, but is this more of a counting approach?

Methods

A

- "remplates" – "templates"

- I can't seem to find in reference [32] any measurement of how incorrect V and J assignments affect initial VJl partitioning, could you clarify which figure this is from?

C

- "In case of l class": is there a typo here? I'm not sure what this means.

- two equal signs in (10)

D

- The sentences following "This crude method suffers from inaccuracy as it loses precision in the case of highly-mutated sequences and junctions of short length" describe how your prefix tree implementation speeds up this crude approach, but not how it improves on the accuracy.

- "standard methods [use a] fixed threshold on Hamming distance divergence"

The standard methods use a threshold on the fraction of differing CDR3 bases, i.e. the threshold on divergence depends on (is proportional to) CDR3 length.

- Could you make more explicit how the increased speed allows for an "adaptive threshold"?

The text after equation (17) seems to suggest that several reruns are involved, but it could be made more clear.

- I don't understand the purpose of constructing these various partitions.

Ostensibly they seem to be to help calculate a threshold, but the section seems to finish having just constructed the partitions, without telling me either how they've helped you arrive at a threshold, or why that threshold is so much better than what other methods have used.

F

(24) I think there should also be an approximate equals sign in the first line in this equation because we are substituting in the approximate value of p

(25) Suggest pointing out that this follows because we are approximating the distribution as Poisson

- suggest "analogously" rather than "analogically" https://english.stackexchange.com/questions/112149/analogous-vs-analogical

- "is chosen based on the prevalence, analogically to adaptive threshold"

I think you're missing a prime after the t in the inequality in this sentence

- "and further assume n0 ∼ n1n2 L to compute the new null distribution"

I think that this tilde means "is distributed as" because n_1 and n_2 are random variables. A little clarification would help here.

Reviewer #3 (Recommendations for the authors):

In addition to the recommendations in the public review, we had the following more questions and recommendations:

P. 2 "Low prevalence is usually due to a high frequency of singletons" Can the authors demonstrate this, or provide a citation?

P. 2 "In addition, we restrict our analysis to CDR3 lengths between 15 and 105: shorter or longer junctions have comparable frequencies to nonproductive junctions, suggesting that they are nonfunctional." This should be shown somewhere or given a citation.

P. 3 It is not clear how mu can vary so little but rho can vary so much

P. 3 use of rho_hat and p_hat is confusing

It would be helpful to see more descriptive statistics of the simulated data, such as the level of somatic hypermutation.

Figure 1 B. From the coloring of the tree/cluster, it looks like two sequences are left out of the tree.

P. 9 Throughout the paper, does "distance" always refer to Hamming distance?

P. 11 Uniform mutation probabilities across BCRs is not biologically realistic, given SHM hotspots as well as CDR and FWR regions. We understand this was a simplifying assumption, but it should be discussed.

P. 11 Potential typo: x' – y <= t. Should this be x' – y <= t'?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Combining mutation and recombination statistics to infer clonal families in antibody repertoires" for further consideration by eLife. Your revised article has been evaluated by Miles Davenport (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer 2

We thank the authors for their careful consideration of our comments, and for the many changes that they have implemented. Our main concerns have been addressed, although we have several minor comments.

The authors have made a huge improvement to the documentation and useability. A minor point, however, is that the result file seems to mostly be in AIRR format, except that the AIRR-standard 'clone_id' column for clonal family information seems to be either absent or copied from the input file, while an undocumented 'family' column appears to hold the inferred family information. This is confusing.

It would be wonderful if the authors chose to go for AIRR software certification as described in https://docs.airr-community.org/en/latest/swtools/airr_swtools_standard.html

We agree that HILARy makes a very real performance improvement in distinguishing similar, but unrelated, families, which is a substantial advance. However, in digging through things a bit more, the paper doesn't seem to clearly communicate how frequently settings arise in which HILARy is substantially different than existing software.

First, the performance plots in Figure 4 only show performance for half of CDR3 lengths (15-45, compared to 15-80 shown in the CDR3 distribution in Figure 6a).

Furthermore, the CDR3 lengths at which other methods perform significantly worse than HILARy (lengths 15-24) constitute less than one percent of a typical repertoire (see for instance Figure 6a). While it's true that it can make sense to emphasize challenging regions of parameter space, it would seem reasonable to clarify that this is what is being presented, as well as showing performance on typical repertoires in order to show the relevant context.

The simulation samples also seem to use a restricted set of J genes: 80% of sequences are from a single J allele, whereas repertoires more typically use around four J alleles with prevalences of perhaps 10% to 50%. This also has the effect of inflating the number of very similar but unrelated families. This is an example of the risks of focusing on a single data sample for validation.

We also have one small clarification in response to:

"We agree that testing the method on a differently generated dataset is a useful check. We should point out, however, that our synthetic dataset is not as biased as it may seem. In particular, it is based on trees from VJl classes that we predicted are very easy to cluster, which means that they are truly faithful to the data, and not dependent on the particular algorithm used to infer them. The big advantage over this synthetic dataset over others is that it recapitulates the power law statistics of clone size distribution, as well as the diversity of mutation rates. To us, it still represents a more useful benchmark than synthetic datasets generated by population genetics models, which miss most of this very broad variability."

We just want to clarify that our concern was not that the synthetic sample was biased, but rather that it is risky to rely on any single sample, whether data or simulation, to form the basis of a robust inference method. Any single sample represents only a single set of possible parameter values, whereas we generally want methods to work well on real data samples that exist at a huge variety of different parameter values.

Also, while deciding when to use synthetic vs real data is a challenging problem, and we don't in general find fault with the authors' choices about this, we do want to point out that the authors' suggestion here that simulation methods cannot mimic data-like clone size distributions or mutation variability (i.e. tree shape) is incorrect. There exist simulation methods that let the user configure these parameters arbitrarily (including using direct inference from data).

Reviewer 3

The authors have addressed the major points I brought up in my review, and the revision is definitely improved. With respect to their new benchmarking on single linkage hierarchical clustering (Figure 4, supplement 2), it's not clear to me why they used their own implementation rather than one of the existing tools, or why the thresholds of 0.76, 0.82, and 0.88 were chosen. However, I think these issues could be addressed with text edits. Personally, I'm trying to reconcile the results of this study with a recent and more comprehensive clonal benchmarking study which showed that single linkage clustering worked quite well: https://bmcimmunol.biomedcentral.com/articles/10.1186/s12865-024-00600-8. May be worth adding some discussion about.

I agree with Reviewer 2 above points about consistency with AIRR format and that (1) the method seems to perform well in a CDR3 space which represents a small fraction of typical repertoire space, so it's not terribly clear how much it improves overall performance, and (2) it's risky to rely on effectively a single dataset to base these conclusions on.
