# Peer review - Round 1

Editors:
- C Titus Brown, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67667.sa0](https://doi.org/10.7554/eLife.67667.sa0)

In this paper, the authors develop a sensitive and specific computational workflow for comprehensively summarizing known and unknown gene content across large collections of genomes and metagenomes. In addition to clustering and categorizing genes on a large scale, the authors show how to use their approach to both explore lineage-specific genes and generate hypotheses for the function of unknown genes.


---

# Peer review - Round 1

Editors:
- C Titus Brown, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67667.sa1](https://doi.org/10.7554/eLife.67667.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Unifying the known and unknown microbial coding sequence space" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including C Titus Brown as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Gisela Storz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Byron Smith (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) We request that the authors restructure the results significantly. In particular, the results need more fine-grained paragraphs with more clarity about the results presented in each paragraph. Please see Reviewer 1 for many suggestions here!

2) Discuss the rationale for prioritizing metagenome-derived sequence clustering over clustering the reference-derived sequences. Similarly, please describe the reason for post-hoc annotation of clusters with UniProt and MGnify, rather than incorporation up front.

3) Please provide a rationale for choosing only two "sources" of metagenomes.

4) Please discuss the parameter selections, and/or cross-compare parameters with other kinds of analysis systems.

5) Add the Schloss and Handelsman reference as appropriate.

6) Please describe the broken-stick model in a bit more detail, focusing on how thresholds were chosen.

7) Consider further expanding the contribution of AGNOSTOS in relation to existing gene family frameworks (COG/EggNOG, etc.) that already capture the high-specificity side of the spectrum, vs the high-sensitivity/distant-homology issues tackled here.

8) Version the code and put it in Zenodo or some other archive.

Reviewer #1 (Recommendations for the authors):

I do think this paper is ground-breaking, but it is not clear to me that readers will be able to navigate clearly through the paper to understand that; although highly motivated readers will probably push through, my guess is that the impact will be greatly improved by substantial reorganization of the Results section.

Starting at the top,

I think the Introduction is quite good and have no big comments!

Results – need restructuring.

In general terms, I think the Results need more paragraphs, with better structure. Moreover, starting from a perspective of optimism and interest, I really struggled to move between the abundance of detailed results and some kind of understanding of their slightly broader meaning within the Results sections.

Conceptual framework:

Perhaps this first half of this could be better split between the bottom of the introduction and the beginning of the discussion? Many of the concepts introduced here only become clear after you've read later Results, which is not (in my quite strong view) not how Results should work.

There is a frequent and slightly frustrating tendency of the authors in this section to use …florid language in preparing us for their work; to my mind, I would prefer to be less prepared for how awesome the work is going to be, and experience it in the results and discussion and then be reminded of it in the Conclusions. Specifically, comments like these could be reconsidered as part of the Results and perhaps moved later:

– "subtle change of paradigm".

– "conceptual and technical foundations".

– "pushing search space beyond twilight zone of seq similarity".

Partitioning section:

I really appreciate the (excellent and expert) triage method.

This section was confusing – it seems like one long run-on paragraph?

One specific question – "72% of genes from GTDB already found, 22% created new GCs, 6% singletons." Question: does this tell us anything? If so, what?

(I have many similar questions; this is a common frustration of mine with the details in the Results. I can guess and think and intuit, but it requires an awful lot of effort to read each sentence! Which is not good.)

Beyond the twilight zone section:

I think this section should start with something like, "We next grouped GCs into gene cluster communities." As it is, the process and motivation is not clearly laid out, and I had to guess. (It looks great once you understand it!)

The results are clear, however!

Line 191, "One Known GCC." Is this a category, "Known"? I'm assuming so, because it's in italics? and capitalized? And while it definitely seems good that one GCC contains almost all of the PR, it would be good to state that clearly.

Paragraph breaks would be good here, too.

A smaller but highly diverse … section:

Lots of numbers. Little in the way of structure to help walk me through them.

Line 232, for example. Is this good? Bad? Interesting? Unexpected? (I can guess, but I want to know what you think it could mean, in fairly cut and dry terms.)

Ecological distribution section -

"Compared to what is reported by traditional genomic and metagenomic analysis approaches" – citation? numbers? comparison?

Paragraphs would be good here.

Unknown coding sequence space -

Meandering structure. I'm not sure what I'm supposed to understand from the specific sample analysis. Phages are responsible for all weirdness?

Fascinating observations in lines 304-307; good to leave as result.

Section – unknown coding space is lineage specific:

I have hard time grasping line 319. Perhaps flip sentence? "Fors GCs that are lineage specific and phylogenetically conserved, they are less conserved if they are unknown…" ok I still can't understand it. clarify?

Not really sure of implication of line 323.

The last paragraph here shows how powerful this is as an organizing principle.

Section – structured coding sequence space augments the interp of experimental data.

Really nice example of how to use this to dig into potential gene specific stuff. GETTING HERE is one (major) point of this paper! Nicely done.

Discussion –

line 414 is nice and clear.

line 422 – implemented?

The language is great, maybe using paragraphs or section headers would be good.

Separate into headers, give main point of each header.

Have "looking forward" in discussion.

Suggest organizing results to tie more clearly into points made in discussion?

Methods – please version the code and put it in Zenodo or some other archive, thanks!

Reviewer #2 (Recommendations for the authors):

– The choice to prioritize clustering of metagenomic sequences above references is surprising. If there is a computational reason not to cluster both together, that could be justified in the text.

– The impact of this work would be increased by extending the reference sequence corpus to which it is applied. Rather than post-hoc annotation of clusters with UniProt and MAGnify, these reference sets could be included in the initial clustering, "unifying" clustering and homology detection in these databases and simplifying the overall pipeline.

– Likewise, the availability of many additional metagenomes from a huge diversity of environments presents an opportunity to greatly extend this work, making the resulting database of broad interest across numerous fields. While the authors may have considered this and decided that it was out of scope, the possibility and its limitations should be explicitly discussed in the manuscript.

– Expanded comparisons of AGNOSTOS to traditional analyses and across parameters, or at least discussing parameter selections, would help readers to understand the decisions that were made.

– The manuscript as it is currently written ignores previous applications of de novo sequence clustering in the analysis of metagenomes (e.g. Schloss and Handelsman, 2008, "A statistical toolbox for metagenomics: assessing functional diversity in microbial communities"). Citing these and putting the current work in the context of other approaches to protein families (COGs, KOs, etc.) would be valuable for readers.

– I did not find the four-class (K/KWP/GU/EU) conceptual framework to be particularly helpful. I think it conflates two orthogonal concepts: (1) the existence of homologues in reference genomes, and (2) homology to sequences with characterized function. As such, it complicated explanations of downstream analyses that focused on just one of those two axes.

– I found many of the explanations in the associated blog post to be easier to follow than those in the introduction. Presenting some of the major concepts earlier and in a more explicit way would be helpful. For instance:

– Replacing "CDS" with "protein" throughout (and clarifying early that these are predicted from DNA sequences using prodigal) and replace "CDS-space" with "proteins" or "protein sequences".

– Explicitly state that "gene clusters" refer to homologous groups. There is a risk that readers will instead think of e.g. "biosynthetic gene clusters" or other groupings of genes based on proximity in a linear sequence.

Clarify ambiguous explanations with simpler phrasing. E.g.:

– "This inability to handle shades of the unknown is an immense impediment to realizing the potential for discovery of microbiology and molecular biology at large […]" (lines 69-71)

– "[…] adds context to vast amounts of unknown biology, providing an invaluable resource to understand the unknown functional fraction better and boost the current methods for its experimental characterization." (lines 87-89)

– Flesh out the distinction between classes more clearly in the introduction, for instance replace lines 101-103 with: 'Only a fraction of sequences predicted to code for proteins possess homology to domains of known function described by Pfam, here we refer to this class as the "Known" (K) fraction. A portion of sequences without Pfam domains of known function can nonetheless be annotated based on homology to characterized proteins, and are classified as "Known without Pfam" (KWP). Finally, sequences not annotated by either of these criteria may be either found in the sequenced genome of an (isolated) bacterium: "Genomic Unknown" (GU), or may have only been observed in environmental samples: "Environmental Unknown" (EU). These four reflect a hierarchy of increasingly "unknown" classifications.'

– Several results are reported as comparisons, but where the "other" is not explicit. E.g. "is phylogenetically more conserved" (line 92). Phylogenetically more conserved than what?

– Similarly: "is smaller than expected" (line 91) and "creating more GCs than expected" (line 482-483). Expected by whom?

– Several references to cluster thresholding using the "broken-stick model" need better explanations. I was not familiar with this approach, and would benefit from a clear description of how thresholds were chosen using this method.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Unifying the known and unknown microbial coding sequence space" for further consideration by eLife. Your revised article has been evaluated by Gisela Storz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

(1) The abstract should be revised somewhat. The sentence starting with the "We quantify the extent…" could be fleshed out with a bit more detail and numbers – perhaps some highlights of the quantification? The next sentence on Patescibacteria stands out because this result seems to be only cursorily discussed in the paper – at the very least the same number (283k) should be mentioned in the Results. Please adjust.

(2) The phrase "lineage-specific at the Species level" is used a few times and is unclear to me – e.g. Line 100: is the intent to say that the unknown fraction of genes is largely restricted to multiple members of individual species? Also, around line 493. Please clarify.

3) Some of the subjective language commented on by both reviewers in initial reviews remains and is not adequately supported by the results. For instance, line 98-101 "By contextualizing the different categories with information from several sources (Figure 1C), we provide an invaluable resource […]". While this may prove true with time, I don't believe that the authors have justified this degree of elevation. Phrasing such as, "We hope that this will prove an invaluable resource […]" would be more appropriate.

(4) Please consider how to improve the description of the pipeline. Some questions we had:

(A) Is this a data product, an analysis tool (slash pipeline), a conceptual framework, or a biological result? In their response to reviews it seems that it is primarily an analysis pipeline with a small number of biological results used to demonstrate its utility; This is not immediately apparent to readers, nor do the authors spend much text explaining to a reader why they should apply it to their own data.

(B) Which of the steps described in the results is built into the AGNOSTOS pipeline and which is applied post-hoc to the results of that pipeline? Clean delineation between the featured tool and additional analyses would improve reader understanding.

(C) Are the hyperparameters arrived at by the authors intended to be used on future users' data as well? If not, are the methods used by the authors for hyper-parameter selection built into the software, or would users need to re-build those themselves?

(D) In Figure 3, panels B and C, which of the K, KWP, GU, or EU categories are included under each of the "Known" and "Unknown" labels? Are both K and KWP combined under known and both GU and EU under unknown? This is one example of where the four-category conceptual framework feels like it might be better described as two axes.

We also suggest the authors consider addressing the following two questions in their revisions:

1. While I now understand the justification for picking the MCL hyperparameter for super-clusters based on the Known fraction alone, it would nonetheless be valuable to use this higher-order clustering to further the search for distant homology. Given that the authors prioritize sensitivity over specificity everywhere else in the paper, this feels like a missed opportunity.

2. In their response to reviewers, the authors express confidently that, "The results of clustering both data sets together or updating the existing gene clusters will be almost identical, but by doing it in two steps, one can track the dynamics of the singletons, the stability of the gene clusters and many other interesting processes that can provide a better understanding of the data." If this is true, I'd be very interested to see it demonstrated. The ability to "stream" in additional genes to the analysis and get the same result has major (positive) implication for the computational scalability of this analysis. Given the size of both current and future metagenomic datasets, this would indeed be a ‘very’ valuable feature of the pipeline.
