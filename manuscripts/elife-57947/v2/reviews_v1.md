# Peer review - Round 1

Editors:
- Vaughn S Cooper, University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57947.sa1](https://doi.org/10.7554/eLife.57947.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study shows that deletion of a non-essential single-copy tRNA gene in Pseudomonas alters the cellular tRNA pool and reduces fitness, especially when conditions enable rapid growth. During experimental evolution in the laboratory, they find that the tRNA deletion can be compensated by repeated, large duplications of a part of the genome, which include a near cognate tRNA gene. This work demonstrates effects of tRNA gene redundancy on fitness and the means by which genomes can rapidly compensate for the loss of redundancy.

Decision letter after peer review:

Thank you for submitting your article "The birth of a bacterial tRNA gene" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This well-written manuscript demonstrates that deletion of a non-essential single-copy tRNA gene in Pseudomonas fluorescens (ser-tRNA CGA) alters the cellular tRNA pool and reduces fitness. During experimental evolution in the laboratory, the authors find that the tRNA deletion is compensated by repeated, large duplications of a part of the genome, which include a near cognate tRNA gene (tRNA TGA). The duplications are associated with increased tRNA TGA expression and increased fitness. The authors suggest that this is a novel evolutionary response to overcome translational inefficiency. These results are framed by a simple model of translation dynamics to understand the initial fitness effects of the gene deletion, and the observed evolutionary response. Overall, the reported experimental work is well done and presents interesting results. The manuscript is also clearly written. However, all reviewers raised questions about the presented mathematical/verbal model and agree that the novelty and breadth of the findings are overstated. Evolution via gene duplication is a well-known phenomenon in evolutionary biology, has been observed in many experimental evolution studies, and is the most likely outcome of the experimental design. The repeated observation of duplications of a region containing tRNA-TGA as well as other tRNAs is a worthwhile finding but the generality of this result for our broader understanding of the evolution of tRNAs requires further exploration.

Essential revisions:

1) Please consider more of the literature on tRNA pool evolution and clarify how this study represents a significant advance. There has been much discussion of gene loss and duplication as key features (e.g. Withers et al., 2006; Wald and Margalit 2014; Tremblay-Savard et al., 2015), and the resulting evolutionary flexibility of tRNA gene sets (e.g. Ikemura, 1985; Rocha, 2004; Higgs and Ran, 2008; Diwan et al., 2018). This paper provides experimental support for these ideas, arising from the deletion of a single bacterial tRNA gene. This is a valuable result, being the first such demonstration in bacteria. However (contrary to the projection in the manuscript), this is not an unexpected result, and is not sufficient to generalize broadly. The reported adaptation of YAMAT-seq to measure bacterial tRNAs is very useful. Prior models of tRNA gene set evolution have demonstrated the importance of codon usage bias for translation rate (e.g. Bulmer, 1991; Berg et al., 1997; Higgs and Ran, 2008).

2) The initial model is overly simplistic and ignores much of the advances made in our understanding from prior work showing the importance of codon usage (see references above). The model does not explicitly include links between tRNA set and translation rate, and between translation rate and fitness; these are instead left as verbal arguments. Equation 1 is odd, because it suggests that codon B is translated by both alpha and beta (whereas only one tRNA can decode a codon at a time) and perhaps only works when alpha is limiting. The meaning of Equation 3 is unclear. The calculated translation times (Equation 4) should probably be clearly discussed as relative (not absolute) times. Finally, none of the model predictions are novel (see references above). Citing and discussing prior work may be sufficient to clearly set up the basic premise here (instead of the model), allowing a deeper focus on the experimental work.

3) We are not convinced that a key assumption of the model is reasonable: " the rate of translation by an anticodon-codon pair is determined solely by the proportion of the anticodon in the tRNA pool". I would think that the rate-limiting step in the translation of a codon is determined by the stochastic search for the cognate ternary complex (aminoacyl-tRNA+EF-Tu and GTP) to the A-site (Varenne et al., 1984). I cannot see that this is directly related to the proportion in the tRNA pool, but mainly to the concentration of each cognate ternary complex at steady-state. Reducing the concentration drastically by deleting a tRNA gene is likely to be limiting for growth, but this can be compensated for by increasing the concentration by a duplication. If the authors assume that competition with non-cognate and near-cognate ternary complexes are of major importance for the rate of translation of a codon this should be clearly stated. The authors find that tRNA proportions vary almost 100,000-fold; does this mean that translation rates are also expected to vary 100,000-fold and is there any experimental support for this? Please provide a clear explanation for why proportion of the anticodon in the tRNA pool is expected to be rate-limiting, supported by proper references.

4) A number of factors relevant to understand translation rates and tRNA gene evolution are not discussed in sufficient depth, and as early in the manuscript as is necessary. For instance, codon usage doesn't feature in the Results section until much later. So the experimental results seem puzzling until it is clear that the non-essential tRNA gene actually recognizes a codon that is very abundant in the genome. In the Discussion section (subsection “Retention of serCGA in P. fluorescens SBW25 wild type”), selection due to codon bias should be considered as a 4th hypothesis for the retention of tRNA(CGA) (perhaps in combination with hypotheses 1 or 3). Prior work also shows that tRNA modifications can alter the accuracy and efficiency of translation (Grosjean et al., 2010; Bjork and Hagervall, 2014; Manickam et al., 2015). These details are mentioned in passing, but deserve more prominence because they are really critical to set expectations and interpret the results. The focal tRNA species are expected to be modified by cmoAB; if the Pseudomonas strain used here has this modification system, it could explain the observed results: modified tRNA(UGA) can compensate tRNA(CGA) function, whereas the other near cognate tRNAs cannot (it is unclear whether G-U wobble works when G is in the codon and U is in the anticodon). I suggest that the details about codon usage, gene copy numbers of all cognate and near-cognate tRNAs, and relevant modification systems should be presented and clearly discussed at the outset.

5) We agree that the increase in tRNA(UGA) levels probably drove the large duplications observed during evolution. However, there are some points of concern here.

a) Given that the deletions were large, it would be useful to be able to estimate the contribution of tRNA(UGA) to increased fitness. Does deleting the duplicated tRNA(UGA) in evolved isolates reduce fitness, and by how much? Related to this, it was not clear whether there were any other mutations in the evolved lines, and their identity; e.g. were there any promoter mutations in the native copy of the tRNA(UGA) gene?

b) What is the level of overexpression of the tRNA gene on the plasmid (Figure 4)? If this is much more than the 2-fold increase due to gene duplication, it means that we do not know if a 2-fold increase is sufficient to increase fitness. On a related note, I could not see information on the sensitivity of the tRNA-seq method (I might have missed this); this is necessary to know how much confidence to place in the measured fold change values.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "The birth of a bacterial tRNA gene by large-scale, tandem duplication events" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The reviewers are mostly satisfied with the response to the prior set of reviews and appreciate the well-written presentation. A few points remain to be addressed to clarify assumptions and discuss caveats of your conclusions.

Revisions:

1) Please specify your assumption that all tRNAs are fully charged, maybe with reference that this is not always the case and description of what YAMAT-Seq measures. We are not quite satisfied with the response to Essential revision point 3 where the authors were asked to explain and justify the assumptions made to be able to say that the translation rate of a codon is determined solely by the proportion of anticodon in the tRNA pool. In the revised version the envisaged translation system is explained more clearly and key assumptions, such that EF-Tu binds all types of tRNA with equal affinity, are explicitly stated. However, the process of charging of tRNAs by aminoacyl-tRNA synthetases/tRNA-ligases and assumptions about charging levels of tRNAs remains incompletely considered. The authors only refer to mature tRNAs in the text, but I am not sure if this includes both charged (aa-tRNA) and uncharged tRNAs. This leads to a number of questions about experimental data, assumptions and what is included in the model:

a) Does YAMAT-seq measure both charged and uncharged tRNAs?

b) Do you assume that all tRNAs are fully charged? This might be reasonable in minimal media (for example Kimberly A Dittmar, Michael A Sørensen, Johan Elf, Måns Ehrenberg, Tao Pan. Selective charging of tRNA isoacceptors induced by amino-acid starvation. EMBO Rep 2005 Feb;6(2):151-7 and references therein).

The focus on serine is potentially problematic. Serine is one of the most toxic amino acids and it is possible that the reduction in growth rate in the deletion mutants are mainly due to this toxicity rather than a reduced translation rate, which would provide an alternative explanation for why the effect on growth is much smaller in minimal media. The proteose peptone 3 used in KB medium is high in serine (about 12% of total amino acids) suggesting that this might cause toxicity due to the inability of L-serine-deaminase to degrade excess serine after a reduction in ser-tRNA concentration. Addressing this in the final manuscript would make readers aware of this issue, even while pointing out that this explanation may be insufficient because adding a plasmid with the amplified tRNA increases fitness.

2) Related to this point, in rich media it has been seen that charging levels for serine tRNAs can be very low at below 10% although serine concentration is high (Avcilar-Kucukgoze et al., 2016). This work is new to this reviewer, but this might be of interest to the authors and readers of the article.
