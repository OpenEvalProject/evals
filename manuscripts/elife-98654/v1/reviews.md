# Peer review - Round 1

Editors:
- Vincent J Lynch, University at Buffalo, State University of New York United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98654.3.sa0](https://doi.org/10.7554/eLife.98654.3.sa0)

This important study explores the relationship between the sequence of prokaryotic promoter elements and their activity using mutagenesis to generate thousands of mutant sequences. The evidence supporting these findings is convincing. This work will appeal to those interested in bacterial genetics, genome evolution, and gene regulation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98654.3.sa1](https://doi.org/10.7554/eLife.98654.3.sa1)

Summary:

This study by Fuqua et al. studies the emergence of sigma70 promoters in bacterial genomes. While there have been several studies to explore how mutations lead to promoter activity, this is the first to explore this phenomena in a wide variety of backgrounds, which notably contain a diverse assortment of local sigma70 motifs in variable configurations. By exploring how mutations affect promoter activity in such diverse backgrounds, they are able to identify a variety of anecdotal examples of gain/loss of promoter activity and propose several mechanisms for how these mutations are interacting within the local motif landscape. Ultimately, they show how different sequences have different probabilities of gaining/losing promoter activity and may do so through a variety of mechanisms.

Major strengths and weaknesses of the methods and results:

This study uses Sort-Seq to characterize promoter activity, which has been adopted by multiple groups and shown to be robust. Furthermore, they use a slightly altered protocol which allows measurements of bi-directional promoter activity. This combined with their pooling strategy allows them to characterize expression of many different backgrounds in both directions in extremely high-throughput which is impressive! A second key approach this study relies on is the identification of promoter motifs using position weight matrices (PWMs). While these methods are prone to false positives, the authors implement a systematic approach which is standard in the field. However, drawing these types of binary definitions (is this a motif? yes/no) should always come with the caveat that gene expression is quantitative traits that we oversimplify when drawing boundaries.

Their approach to randomly mutagenize promoters allowed them to find many examples of different types of evolutions that may occur to increase or decrease promoter activity. They have supported these with validations in more controlled backgrounds which convincingly support their proposed mechanisms for promoter evolution.

An appraisal of whether the authors achieved their aims, and whether the results support their conclusions:

The authors express a key finding that the specific landscape of promoter motifs in a sequence affect the likelihood that local mutations create or destroy regulatory elements. The authors have described many examples, including several that are non-obvious, and show convincingly that different sequence backgrounds have different probabilities for gaining or losing promoter activity. This overarching conclusion is supported by trend and mechanistic data which show differences in probabilities of evolving promoters, as well as the mechanisms underlying these evolutions. Furthermore, these mutations are well described and presented, showing the strength of emergent promoter motifs and their specific spacings from existing motifs within the sequence.

Impact of the work on the field, and the utility of the methods and data to the community:

This study enhances our understanding of the diverse mechanisms by which promoters can evolve or devolve, potentially improving models that predict mutational outcomes. While this study reveals complex mutational patterns, modeling them could significantly advance our ability to predict bacterial evolutionary trajectories and interpret genomes, bringing us closer to that goal.

Recent work in the field of bacterial gene regulation has raised interest in bidirectional promoter regions. While the authors do not discuss how mutations that raise expression in one direction may affect another, they have created an expansive dataset which may enable other groups to study this interesting phenomenon. Also, their variation of the Sort-Seq protocol will be a valuable example for other groups who may be interested in studying bidirectional expression. Lastly, this study may be of interests to groups studying eukaryotic regulation as it can inform how the evolution of transcription factor binding sites influences short-range interactions with local regulator elements.

Any additional context to understand the significance of the work:

Predicting whether a sequence drives promoter activity is a challenging task. By learning the types of mutations that create or destroy promoters, this study provides valuable insights for computational models aimed at predicting promoter activity.

Comments on revised version:

I am satisfied with the extensive changes made by the author. This manuscript is excellent.

I very much like the change in figures to incorporate the sequence information. It is great to see clear representations of the emergent sigma70 motifs and their spacing relative to existing motifs. This addition significantly improves the clarity of the findings.

The validation of mutations on a clean background is well-executed, and the results are convincing. I appreciate the effort put into validating their results. The additional analyses that include TGn and UP-element motifs are also well done and highly relevant, as these elements are known to compensate for weaker or absent -35 sequences.

Most or all perceived inconsistencies from the previous version have been resolved. While I don't think the fluorescence threshold of 1.5 a.u. for promoter activity is justified, the authors do acknowledge this shortcoming, and even empirically-derived thresholds are still technically arbitrary.

I particularly enjoyed Figure 1E, thank you for entertaining my analysis request! Also, the H-NS story is a nice addition showing how transcription factors influence this evolution

Overall, this revised manuscript is an excellent contribution to the field, and I have no further recommendations for improvement.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98654.3.sa2](https://doi.org/10.7554/eLife.98654.3.sa2)

Summary:

Fuqua et al investigated the relationship between prokaryotic box motifs and the activation of promoter activity using a mutagenesis sequencing approach. From generating thousands of mutant daughter sequences from both active and non-active promoter sequences they were able to produce a fantastic dataset to investigate potential mechanisms for promoter activation. From these large numbers of mutated sequences, they were able to generate mutual information with gene expression to identify key mutations relating to the activation of promoter island sequences.

Strengths:

The data generated from this paper is an important resource to address this question of promoter activation. Being able to link promoter modulated gene expression to mutational changes in previously nonactive promoter regions is exciting. This approach allows future large-scale studies to investigate evolutionary processes relating to changes in gene regulation in a statistically robust manner. Here there is a focus on the -10 and -35 boxes but other elements and interactions were explored including; H-NS binding, UP-element and TGn. Alongside this, the method of identifying key mutations using mutual information in this paper is well done and should be a standard in future studies for identifying regions of interest.

Weaknesses:

While the generation of the data is superb, as the authors have stated clearly themselves, there is a lot of scope for future studies to understand both causal relationships and utilise the data more effectively. The authors look at changes in regulatory expression based on a few observations that are treated independently but occur concurrently. While this study has backed up findings experimentally this may not always be possible. Previously this reviewer had suggested addressing this using complementary approaches such as analysis focusing on identifying important motifs, using something like a glm lasso regression to identify significant motifs, and then combining with mutational hotspot information would be more robust. The authors tried to implement such an approach in response to the review, but its complexity became beyond the scope. I look forward to the development of such methods that allow more complete exploration of similar datasets.

Comments on revised version:

The authors addressed all my previous comments. I believe the study is much improved and thank them for the time and effort they put into addressing the comments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98654.3.sa3](https://doi.org/10.7554/eLife.98654.3.sa3)

This work brings a computational approach to the study of promoters and transcription. The paper is improved but there are still factual errors and implausible explanations. I am not convinced by the response from the authors, concerning the promoter -35 element, in their rebuttal.

Comments on author rebuttal:

- We respectfully but strongly disagree that our analysis has misrepresented the true nature of -35 boxes. First, accounting for more A's at position 5 in the PWM is not going to lead to a "critical error." This is because positions 4-6 of the motif barely have any information content (bits) compared to positions 1-3 (see Fig 1A).

The analysis does misrepresent the consensus -35 element, which is, unequivocally, TTGACA. I agree that positions 4-6 of the element are less well-conserved.

- This assertion is not just based on our own PWM, but based on ample precedent in the literature. In PMID 14529615, TTG is present in 38% of all -35 boxes, but ACA only in 8%.

This does not mean that TTGACA is not the consensus, or that "ACA" is not important at promoters where it's present.

- In PMID 29388765, with the -10 instance TATAAT, the -35 instance TTGCAA yields stronger promoters compared to the -35 instance TTGACA (See their Figure 3B).

This is a known phenomenon and results from "perfect" promoters being limited at the point of RNA polymerase promoter escape (because the RNAP struggles to "let go" of perfect promoters). This does not mean the TTGACA is not the consensus. Indeed, and this is a key point, it is evident in the figure the authors refer to that TTGACA stimulates more transcription than alternative -35 sequences when -10 elements are not perfect.

- In PMID 29745856 (Figure 2), the most information content lies in positions 1-3, with the A and C at position 5 both nearly equally represented, as in our PWM.

The motif shown in this paper suffers from exactly the same issue as the paper under review; the variable spacing between the -35 hexamer and -10 element isn't taken into account by MEME.

- In PMID 33958766 (Figure 1) an experimentally-derived -35 box is even reduced to a "partial" -35 box which only includes positions 1 and 2, with consensus: TTnnnn.

This paper does not show an "experimentally-derived -35 box" in Figure 1 (or anywhere else, as far as I can see).

- In addition, we did not derive the PWMs as the reviewer describes. The PWMs we use are based on computational predictions that are in excellent agreement with experimental results. Specifically, the PWMs we use are from PMID 29728462, which acquired 145 -10 and -35 box sequences from the top 3.3% of computationally predicted boxes from Regulon DB.

The paper mentioned states "for the genomic RNAP logo, sequences were taken from computationally predicted RNAP binding sites on RegulonDB" so these are not experimentally defined promoters? It's not obvious from the paper, or regulon DB, which sequences these are or how they were predicted.

- Thank you for pointing out that our original submission was incomplete in this regard. We address these concerns by new analyses, including some new experiments. First, Rho dependent termination is associated with the RUT motif, which is very rich in Cytosines (PMID: 30845912). Given that our sequences confer between 65%-78% of AT-content, canonical rho dependent termination is unlikely. However, we computationally searched for rho-dependent terminators using the available code from PMID: 30845912, but the algorithm did not identify any putative RUTs. Because this analysis was not informative, we did not include it in the paper.

I don't believe it is the case that Rho absolutely requires a RUT sequence. My understanding is that, if an RNA is not translated, Rho will intervene (e.g. see PMID: 18487194).

- We respectfully disagree that the reviewer's point is pertinent because what the reviewer is referring to is the likelihood that the sequence is a promoter, which indeed increases with AT content, but we are focused on the likelihood that a sequence becomes a promoter through DNA mutation

I disagree that this distinction is relevant. An AT-rich sequence will much more closely resemble a promoter by chance than a GC rich sequence. As an extreme example, the sequence TTTTTT can be converted into a reasonable -10 element by one change (to TATTTT) but the sequence GGGGGG can't.
