# Peer review - Round 1

Editors:
- Niema Moshiri, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85794.sa0](https://doi.org/10.7554/eLife.85794.sa0)

This important work presents a novel tool for performing phylogenetic assignment of DNA sequences. The manuscript is convincing, and the authors perform a standard benchmark experiment against current state-of-the-art tools using real + simulated datasets to demonstrate where the novel tool stands in the context of existing methods. This paper will be of great interest to bioinformaticians and evolutionary biologists interested in massively-scalable phylogenetic assignment.


---

# Peer review - Round 1

Editors:
- Niema Moshiri, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85794.sa1](https://doi.org/10.7554/eLife.85794.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A rapid phylogeny-based method for accurate community profiling of large-scale metabarcoding datasets" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Niema Moshiri as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nick Goldman (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) There were some concerns that the data sets that were chosen in the manuscript might not be well-aligned with real-world use cases for the tool, and that other data sets could be included that better represent real-world use cases; see Reviews below for specific comments. The realism of the chosen data sets should be justified, and/or datasets more representative of real-world scenarios could be included.

2) The manuscript includes some comparisons between Tronko and pplacer, and it excludes pplacer from the benchmark experiment due to pplacer's inability to scale to the necessary dataset sizes (which is perfectly reasonable). However, a recently published tool named APPLES (Balaban et al., 2020; https://doi.org/10.1093/sysbio/syz063) seems to be able to perform taxonomic classification using phylogenetic placement in a similar manner as pplacer (i.e., by feeding the output phylogenetic placement file to guppy to output taxonomic classifications). The following tutorial by the authors of APPLES seems to present this "APPLES to guppy" workflow:

https://github.com/smirarab/tutorials/blob/master/Skmer-APPLES-tutorial.md#run-actual-placement

The Reviewers were unsure about whether or not APPLES (as a potential substitute for pplacer) would be a reasonable alternative for Tronko. If APPLES is a reasonable alternative for Tronko, we request that it be included in any existing benchmarks in which Tronko was compared against pplacer. If APPLES is not a reasonable alternative for Tronko (and should thus not be included in the existing comparison), we request additional details in the introduction of the manuscript describing why APPLES is inappropriate for this task.

3) Some choices were made without clear justification (e.g. the use of specific dependency tools as well as parameter selection for those tools), and these choices require some form of justification and/or discussion/exploration; see Reviews below for specific comments.

4) There were technical issues/errors with the distribution of the tool that need to be fixed; see Reviews below for specific errors/scenarios as well as some potential suggestions.

5) There are minor issues with the writing of the manuscript itself that should be updated/corrected; see Reviews below for specific comments/suggestions.

Reviewer #1 (Recommendations for the authors):

First, some technical questions about the methodology:

How is the accuracy impacted by potential errors in the multiple sequence alignment (MSA) and phylogenetic inference procedure? For example, what if someone were to use e.g. MAFFT (Katoh et al., 2002) for MSA followed by FastTree 2 (Price et al., 2010) or IQ-TREE (Nguyen et al., 2015) or matOptimize (Ye et al., 2022) for phylogenetic inference instead of the Tronko-build approach? Or perhaps existing joint MSA + tree inference tools like PASTA (Mirarab et al., 2015)?

Why were existing phylogenetic placement tools excluded, such as UShER (Turakhia et al., 2021), APPLES (Balaban et al., 2019), SEPP (Mirarab et al., 2012), TIPP (Nguyen et al., 2014), or UPP (Nguyen et al., 2015)? The authors exclude pplacer due to runtime + memory intensity, but they did not provide rationale for providing the many other existing phylogenetic placement methods. My understanding is that UShER is supposed to be *extremely* fast and quite memory-efficient.

Tronko currently supports two BWA-MEM modes (Needleman-Wunsch and Wavefront Alignment), but rather than just supporting BWA-MEM, what about other potential aligners? For example, if one were to use Minimap2 to perform alignment instead, how would the results + runtime + memory requirements change?

The manuscript explains that the high memory usage is because of all of the things Tronko needs to store in memory the entire time, but (1) do all of those things really need to be stored in memory simultaneously, and (2) could some form of compressive encoding (e.g. 2-bit encoding for reference genomes) be used to reduce memory usage? 50 GB is reasonable for high-end modern servers, but I think it can be dramatically reduced with clever optimizations. I think the discussion of the peak memory requirements would benefit from more thorough exploration of what exactly is contributing to the large memory consumption (e.g. what proportion of it is from storing the trees, or the reference genomes, or the posterior probabilities, etc.).

Now, general comments about the paper:

The paper is generally well-written and reads fairly clearly, but my main concern is about some choices in the methodology that were (seemingly) somewhat arbitrarily chosen without providing justification. For example, BWA-MEM was chosen for mapping; why that choice rather than other mappers? And why are the default parameters appropriate? RAxML was chosen for phylogenetic inference; why that choice rather than other tree inference tools? And why default parameters with GTR+Γ model (rather than GTR+Γ+Invariant, or GTR+CAT, or GTR+CAT+Invariant, etc.)? In addition to my technical questions above about how changing these choices would impact results, my general comment here is that all choices should be motivated in some way within the text.

Both panels of Figure 6 should be log-scale: as they're currently presented in linear-scale, it's impossible to meaningfully discern differences between the smaller lines.

Reviewer #2 (Recommendations for the authors):

## Overall comments

The manuscript is hard to read top-to-bottom, and would be easier if you gave a little more of an overview of the method before giving results. The figure 1 caption, for example, can't really be understood without getting to P14. Figure 1 itself can't really be understood without understanding the cutoff parameter.

Please make it clear from the get-go that this is amplicon sequencing and not true metagenomics. The tool is compared to Kraken which does true metagenomics.

If I am understanding correctly, the database input for the method requires a tree annotated with taxonomic labels at all nodes of the tree. If that's right, what is the process for doing this labeling? What if the taxonomy and the tree disagree?

The paper doesn't compare to APPLES (reference 8) which is phylogenetic but distance-based and therefore should be faster, but is probably less accurate. This isn't necessary for a revision, but it would be interesting to understand if performance gaps are due to phylogeny or likelihood-based phylogeny.

## Details

Please number lines. This makes reviewing much easier.

P2 "There are three…": I suggest using (1), (2), (3) in this sentence to make it clearer rather than just rely on commas.

P3 Tandy Warnow has worked on a number of approaches to scaling likelihood-based phylogenetic placement, e.g. https://www.biorxiv.org/content/10.1101/2022.10.26.513936v1.full.pdf which also uses a collection of trees.

P7 It seems like you are using a different cutoff for the different comparisons. Can you justify that?

P12 "lenghts" typo

P12 The two-pass algorithm is linear time, and this seems to me like the standard two-pass algorithm. We can get the required posterior probabilities from the upward and downward partial likelihood vectors. What am I missing? If there is something subtle, some more explanation and notation is needed.

P12 To get an assignment to node i, does i and its children need to get a given taxonomic assignment? The text reads as if only the children need taxonomic assignments.

P13 Why I and V? I know they are arbitrary but it seems like an odd choice.

P13 What is the intuition for the definition of variance? If we were to try to write this as the variance of a random variable, what would it be? It seems like this definition is similar to that for the centroid of the tree. If that's the case, why not use that more common object?

P14 Perhaps "written" rather than "printed"? Is there a specific format to this file, like JSON, or is it fully custom?

P15 Notation would be cleaner if you just used a single P for posterior probability, or \mathbb{P}. use "\log". Suggest display equation for phylogenetic likelihood.

P16 Interesting that this classifies N as a gap. Sometimes Ns are ambiguous sequencing calls.

P16 What is m(1)?

Figure 2: I found "error/polymorphism" confusing, as at first I thought it was the ratio of the two. Suggest just "error" in the figure and caption, and note in the text that it could be in fact polymorphism. Also, there are lots of triangles for Tronko. Please introduce in the text what the cut-off is. You state that there is a cut-off on P4, and hopefully in one additional sentence you could give an intuition. Font is too small.

Figure 3: These "rainbow" schemes are now not in favor compared to color schemes like viridis and variants; see https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0199239

Figure 6: Please consider color scheme, the yellow is basically invisible.

Figure S4. I'm not sure what "assignment rate" is. Is the fraction of time the program produced any result? Could you label the Tronko lines with Tronko?

All Figure legends should identify the gene target and data set.

Reviewer #3 (Recommendations for the authors):

We have divided most of our considerations into three areas, regarding (a) the methods that this ms. introduces, (b) the results that they produce and (c) the Tronko software.

(a) The methods take familiar ground as their starting point, and then take a new direction in terms of approximations and shortcuts to implement something resembling a full probabilistic (maximum likelihood) inference technique, but fast enough and with low-enough memory requirement to be practical for modern-sized datasets (reference and sample). We need no convincing that this is a valid approach, and is sufficient for the methods proposed to be of value if they produce good-enough results.

That said, there were a few instances of other relevant work not being quoted that I think would be of interest to some readers. We don't think this ms. needs to address all these points in a detailed manner, but where other relevant work has not been cited then readers can reasonably ask whether Pipes and Nielsen are unaware or have simply decided not to incorporate some other existing ideas; or whether they tried to incorporate ideas that ultimately did not work; whether some alternative concepts are somehow incompatible with the approach they did take; or whether there is some other reason. Some specific examples we are curious about and would like to see discussed in this manuscript:

* what about methods that combine composition-based (kmer) and phylogenetic approaches, essentially replacing likelihood calculations with kmer statistics in a phylogenetic framework? See work like https://academic.oup.com/bioinformatics/article/35/18/3303/5303992 and others from that group, including recent work by Romashchenko

* since the ms. argues so strongly for the benefits of phylogenetic methods, it would be interesting to see how the authors consider Tronko to compare to phylogeny-based methods other than pplacer, for example papara and PAGAN and others e.g. mentioned in https://www.frontiersin.org/articles/10.3389/fbinf.2022.871393/full

(b) The results seem convincing and reasonable metrics were used for evaluation. However,

* since the method's highlight is incorporating phylogeny, it would be interesting to see some comparisons of results using a metric that takes phylogeny into account. For example, while calculating accuracy of taxonomic assignment, instead of using a binary score (correct/incorrect), could you calculate a distance between assignment and real value? A measure of how wrong incorrect assignments could be of relevance to many users in terms of biological interpretations. Arguably, a tool that misassigns to close species would be preferable over another that misassigns to further species

* very poor performances of some tools in mock community analyses might make readers ask if the default parameters of the tools were right or not for this comparison. For example, for Braukmann et al. data the authors say "MEGAN did not assign any reads at the species or genus level"

* some claims about other methods' results being dominated by Tronko based on the convex hull seem a bit overstated, when there has been no investigation of how the other methods' recall/misclassification response curves could appear if other parameter settings were used

(c) Tronko software is publically available on GitHub with clear documentation, example files, and working example commands. Nevertheless there is room for improvement for Tronko to be widely utilised by the community:

* The software installation and execution can be tested on a few different computers and ideally operating systems. We failed to install the software from the source but Singularity installation works fine.

* tronko-build input files are preprocessed with multiple softwares. Although the authors provide example files, there is not a guide on how to create those files for our own gene of interest. A couple of sentences (or maybe more, for users who are not so familiar with the data types and analyses involved) about how those files were prepared would be very helpful.

* tronko-build example files include some files with double extensions (e.g..fasta.ann). These are not mentioned in the readme. It is not clear what they are. They are not mentioned in the inputs of the command nor did they appear in the output directory when we ran it.
