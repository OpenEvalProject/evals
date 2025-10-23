# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78526.sa0](https://doi.org/10.7554/eLife.78526.sa0)

GENESPACE is a new and straightforward computational tool to include synteny information in the calculation of genome-wide sets of orthologs. The development of this tool is very timely as more and more complete chromosome-scale assembled genomes are becoming available. While the assembly problem has been solved, this is not the case for multiple genome comparisons, and GENESPACE is an important step to help remedy this gap in our comparative genomics toolbox.


---

# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78526.sa1](https://doi.org/10.7554/eLife.78526.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "GENESPACE: syntenic pan-genome annotations for eukaryotes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) While you will see that the reviewers generally liked the functionality of GENESPACE and support its publication in eLife, there were multiple concerns regarding unclear descriptions of its methodology. It is therefore necessary that you revise the manuscript very carefully and make it accessible to both experts (including details on the methods and more formal definitions) and non-experts (on the general way how GENESPACE works).

Reviewer #1 (Recommendations for the authors):

While I support the publication of the manuscript, I have doubts that the manuscript in its current form is explaining well what GENESPACE is doing and how this is performed. While I do appreciate that the Results section tries to give an overview of the methodology, it is still very hard to follow as it is full of jargon and leaves out some important information, which only can be found in the methods.

How is synteny defined (line 105), which is the basis for dropping graph edges (which I assume are BLAST hits) before running OrthoFinder (while in Figure S1 orthofinder is run before the synteny module)? Once the BLAST hits between non-syntenic regions are deleted OrthoFinder can be run without any adjustments, but still connect genes to OrthoGroup in syntenic regions only. However, the sentence in line 108 is not clear, how can BLAST hits in syntenic regions be merged with synteny-constrained OGs (where BLAST hits in syntenic regions are actually the basis for synteny-constrained OGs)? In this regard, it is not clear what the differences between synteny-constrained OGs and within-block OGs are.

Table 1. It is not clear what this table actually shows and requires guessing. (Why is this analysis done with nine chromosomes only?). It becomes more clear after rereading the later section that explains Table 1, but on the first occurrence of table 1 in the text, I got lost. The GENESPACE run using the tetraploid genome still relies on the synteny between the subgenomes in order to generate OG groups of size of 6? It is not fully clear what the differences between the tetraploid run and the split by subg. runs are when synteny information between the subgenomes is also needed in the tetraploid run. Besides the description of this approach is very hard to follow. I also do not see why this approach reveals sensitivity – for example in the pure OrthoFinder runs some of the OGs of size of 6 might be extended by in-paralogs which is (as far as I understand) the goal of OrthoFinder.

In a second paragraph, GENESPACE is also presented as a tool for the identification of syntenic regions (which presumably are the syntenic regions that the OG analysis are based on, however, this is not clear). GENESPACE goal is to filter BLAST hits in a way that regions are linked to only a single region in the other genome by "subsetting the BLAST hits to those 181 within the same orthogroups". This again is not clear, does this imply that OrthoFinder results are used to filter the BLAST hits? The blast hits are then extended. Though there is more about this in the methods, it is not clear to me, why this leads to non-overlapping syntenic regions, specifically, as connected orthologs do not need to be right next to each other.

I think the expression "concept of a pan-genome annotation" or just "pan-genome annotation" in itself is misleading. GENESPACE is a tool for ortholog identification and not for gene annotation. I see the point why it is called like this (all genes are projected on one reference genome), however, I actually expected that GENESPACE would annotate/correct gene structure annotations, which is the typical context of the term "annotation" in genomics.

It would be helpful to define (the differences of) synteny and collinearity (L49 and rest of manuscript).

How is the exact location defined when projecting non-reference OG to reference positions?

In multiple parts of the text, it is mentioned that tandem arrays are excluded or treated in a different way. Could this be clarified?

It is not clear how the "second proximity search step" in GENESPACE actually works. Where are the significant gains in single copy genes coming from? Why are they not already identified?

Reviewer #2 (Recommendations for the authors):

The code and data are available on GitHub.

The algorithm could be described more clearly. For this, it would probably help to introduce key definitions more formally. Below is a list of questions I was left with after reading the manuscript.

When you use 'syntenic regions', are regions in multiple genomes meant or always only in two genomes? If appropriate you could qualify the term according to the usage.

The riparian plot appears to use only n-1 pairs of genomes out of the n*(n-1) pairs of different genomes for which syntenic regions were computed. What is the formal criterion or algorithm for that choice that was made? The respective comments in the Figure captions are not clear to me.

What does GENESPACE do if a gene or region is missing in reference genome?

How are the syntenic regions extracted and how is can this be adjusted by the user (line 620)?

I do not understand how 'collinear arrays' are defined (line 635). What does it mean for a group of genes to share an orthogroup?

How is the step done from pairwise synteny to synteny of multiple genomes? Is this done at all? The manuscript reads around line 108 as if OrthoFinder is (re)run on syntenic regions. This makes sense if there are in general multiple (>2) regions considered to be mutually syntenic with one another. If that is the case, how do you address the choice of having a few long syntenic regions versus many short syntenic regions when both are plausible and the choices share a subset of genes?

Can there be two genes in an orthogroup that GENESPACE outputs that are not syntenic within their pair of genomes?

Does GENESPACE scale quadratically with the number of genomes?

Why are for two genomes g1 and g2 both (g1, g2) and (g2, g1) contained, e.g. in Supplementary File 1?

(Why) is it not symmetric? What are the roles of first and second genomes?

Table 1: The row labels are hard to make sense of. Are any rows the results of GENESPACE?

Figure 1: The human Y chromosome is in the figure caption but not in the image. The same holds for Supplementary Figure 3.

OrthoFinder is inconsistently spelled as OrthoFinder, Orthofinder and orthofinder.

Description of Supplemental Data 1. There are no columns pgChr or pgOrd in Lovell_09-03-2022-TR-eLife-78526_Supplementary_File_1.txt

Apparently the order of files and descriptions is not consistent with each other.

Line items:

43: grammar

162: What does 'contrasted' mean here?

173: What does 'dosage' mean here?

713: Add 'of dotplots' as the link apparently does not contain all of GENESPACEs results.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "GENESPACE: syntenic pan-genome annotations for eukaryotes" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors have addressed many of my concerns by rewriting large parts of the manuscript, which significantly improved the description of what GENESPACE does and how it works. In particular the step-by-step descriptions in the methods worked well for me. I fully support publication of this manuscript, though there are some small suggestions below.

In the first Results section, I would have found it helpful to read one sentence on what OrthoFinder and MCScanX do (resp. what they output).

Line 71: This sentence was still not clear to me. What is the gene rank that is recalculated, and why would a recalculation make genes with PAV?

Table 2: no horizontal bars visible for me as indicated in the legend.

Reviewer #2 (Recommendations for the authors):

In the revision, the authors have made substantial changes. In particular the first two tables were removed from the original manuscript. Lovell et al., have added a new Table 1, in which they compare their tool GENESPACE to OrthoFinder and MCScanX on pairs of genome annotations, and an in-depth description of their implementation steps.

The example plots are convincing, not so the benchmark in its current form. I am missing a measure of sensitivity or coverage as well as a measure of how much the orthogroups respect synteny.

In the very important sentence in line 87 it is grammatically ambiguous to what ‘that’ refers to. It should be reformulated so that it is unambiguous even for readers not understanding the authors intention yet.

I assume ‘that’ in line 87 qualifies ‘orthogroup’. Under that assumption, a trivial and very insensitive bogus orthology finder that outputs in a genome-wide search for synteny a single orthogroup with (any) two genes in two different species would achieve 2/2=100% of what the authors refer to as "accuracy and precision". A little less bogus, a trivial filter method that randomly (and independent of synteny) reduces an orthogroup with multiple genes from different chromosomes of the same species to one with genes on at most one chromosome per species would perform better in this measure than its orthogroup input. The numbers of Table 1 can consequently by themselves not reasonably establish the ”outperformance” claimed in line 89.

Line 88 appears to refer to the same results of Table 1 but formulates “percentage of … orthogroups” as opposed to “percent of genes”, which is of course different. I strongly suggest the authors use a precise definition of their central measures of accuracy, e.g. with a formula in which all terms are themselves unambiguously defined.

The methods are now described at length and include coding details on pipelining, thresholding and implementation flow. Admittedly, this reviewer had requested details on thelgorithmm, but had ideally expected a concise and precise formulation of the formal objectives that GENESPACE achieves. Most readers would arguably appreciate a more succinct formulation that is specific about where the main ideas of the program lie and to which high-level design decisions are made. For example, is the decision which homologous genes are syntenic based on all-versus-all pairwise comparisons of coordinates, on pairwise comparisons of neighboring species in a user-specified order, in an order chosen by the program, are comparisons only done all-against-reference or even are comparisons between two genomes informed by third genomes?
