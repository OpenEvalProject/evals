# Peer review - Round 1

Editors:
- Daniel R Matute, https://ror.org/0130frc33 University of North Carolina, Chapel Hill United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78775.sa0](https://doi.org/10.7554/eLife.78775.sa0)

This piece presents a new method, ANOSPP, that uses cheap sequencing to infer genealogical relationships between Anopheles individuals, including the possibility of species-level identification. The method is versatile and will be useful to vector biology researchers. The proof-of-principle presented in the manuscript is convincing and will serve as a blueprint for future studies in Anopheles.


---

# Peer review - Round 1

Editors:
- Daniel R Matute, https://ror.org/0130frc33 University of North Carolina, Chapel Hill United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78775.sa1](https://doi.org/10.7554/eLife.78775.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "High resolution species assignment of Anopheles mosquitoes using k-mer distances on targeted sequences" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Dominique Soldati-Favre as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. In general all reviewers saw merit in the submission but had some concerns regarding the scope of the work and the interest the findings can elicit in general audience not specialized in vectors. You will see that the reviewers had several comments that can make the manuscript a stronger piece. Collectively, all reviewers agreed on two improvements that would make the manuscript potentially suitable for eLife. I am looking forward to a resubmission of the piece.

Essential revisions:

1) All reviewers agree that the findings from this piece has the potential to benefit the vector community. The common comment from all reviewers was the need to more carefully delineate the scope and impact of the work. One way to do this is to be more straightforward on what instances this method can and should be used. This is of particular importance for the eLife audience which extends beyond anopheline researchers.

2) The main claim of the manuscript is that the method the authors are presenting is a major advance in species compared to the tools available in the field. This needs to be either further demonstrated by providing a comparison to other sequencing methods (MSG, RAD-Seq, etc), and computational tools (Structure, ADMIXTURE), or by tempering the claims.

Reviewer #2 (Recommendations for the authors):

First: this manuscript will be of interest to entomologists and vector biologists who do not have a background in machine learning. With that in mind, I commend the authors for their clear efforts in making the algorithmic and technical details of this manuscript understandable to a lay audience.

Three suggestions along those lines follow. First, the idea of a kmer table may not be immediately intuitive to someone who is not already familiar with them. I suggest making explicit (or more prominent, if I have missed this in the text) that the kmer table contains ALL possible kmers of that length. This is readily apparent in retrospect, but was not immediately clear.

Second, again, the authors have done a good job making what little math is present in this paper accessible to a wide audience, without resorting to jargon. However, considering this audience, it would be good to have the specific formal meaning of the vertical bars in both equations defined for those who are not familiar with set notation. At the first equation seems like a natural place for it.

Lastly on this topic, the kmer table contains the occurrence counts, and kmer distance is calculated based on the number of non-matching kmers. Is a matching kmer defined by shared presence, or an identical number of occurrences? Ie, if 8mer CCTGAAAT occurs twice in q1 and four times in q2, is this counted as a match for this entry in the table?

In addition, after reading the manuscript, I was curious about the potential effect of chromosomal inversions in the gambiae complex. The authors mention this as a type of variation that should be well-represented in the reference database. If the reference and validation sets naturally contain a reasonably polymorphic assortment of the inversions, it would appear that the method is robust to these, but this may be a strong assumption. Do the authors have any predictions about the potential consequences of inversions that could help researchers applying this method, or interpreting the resulting data, be wary of "edge cases?" Do a substantial proportion of amplicons overlap a common inversion in this complex?

Finally, in the discussion of An. nili and An. hyrcanus, as well as other relabeled specimens discussed in the supplement, the authors show how this tool can also generate phylogenetic questions. This is very interesting! However, given the known history of introgression in the gambiae and funestus complexes, and the probable history of such introgression elsewhere, it is also worth very briefly touching on the potential for this method to suggest patterns of relatedness between species that do not reflect the true phylogeny. This simply follows from interrogating markers genome-wide, and is not a drawback or criticism of the method; however, the clarification may be worthwhile for the sake of those interested in applying this method or re-using the resulting data.

Reviewer #3 (Recommendations for the authors):

My main concerns come from not being entirely certain what the proper scope is for such an investigation – I will elaborate a bit below, and I am totally happy to defer to the editor or other reviewers on what they feel is best here. But as a reader, I was particularly interested to get more detail on the advantages and disadvantages of different approaches (since the amplicon panel itself is already published elsewhere). Currently, it reads as a bit path dependent – the authors develop their nearest-neighbor scheme, show that it performs well at coarser scales but not finer scales, and then develop the VAE approach to assign within coarser groups.

In particular, I think it would be quite valuable to see what factors determine the best approach here. My understanding is that the regularization approach used by VAE leads to more continuous distributions in a space that tends towards the origin. For species assignment, this could be a good or a bad thing, I suppose – it might perform better for ambiguous samples but worse for well defined but subtly differentiated lineages? UMAP, in contrast, would be expected to yield more compact and spaced apart clusters, I believe – this might have different advantages and disadvantages. In Makunin 2022 UMAP doesn't seem to work particularly well – is the improvement here from the kmer approach or the VAE? It would be helpful to know what are the key advances that make things work so much better here.

I am sensitive to the desire to develop a practical tool here, so I am happy to hear if others disagree with this assessment. But if the goal is to more generally translate recent advances in clustering high-dimensional data to the species assignment context, I think a slightly broader scope in the presentation of results would help substantially. These recommendations are premised on potentially providing a broadened comparison of species assignment approaches for this specific context (i.e. large numbers of moderately divergent amplicons) – just suggestions of what I think would more helpfully contextualize this work, not preconditions for my recommendation to accept this manuscript.

I would be very curious to see something like a summary at the end with a more direct comparison of assignment accuracy with:

1. Read alignment with traditional nearest neighbor assignment – doesn't perform perfectly.

2. kmer tables with nearest neighbor performs incrementally better.

2a. Are 8mer tables actually the best tradeoff between robustness and sensitivity?

3. Machine learning approaches can improve on this.

3a. VAE

3b. UMAP or t-SNE?

This could provide more general guidelines that could be translated into other systems, increasing the utility of the work for the community.
