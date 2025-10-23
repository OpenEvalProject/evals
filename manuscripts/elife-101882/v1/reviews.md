# Peer review - Round 1

Editors:
- Markus A Seeliger, Stony Brook University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101882.3.sa0](https://doi.org/10.7554/eLife.101882.3.sa0)

This manuscript provides an important overview of potential resistance mutations within MET Receptor Tyrosine Kinase. The evidence supporting the findings is convincing - it should be pointed out that the approach is comparatively new for the application of protein kinases and the results are therefore of potentially great value. The results will be of value for clinicians facing drug resistance mutations, computational biologists who are training models of drug resistance mechanisms and biologists with an interest in cell signaling.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101882.3.sa1](https://doi.org/10.7554/eLife.101882.3.sa1)

Summary:

This manuscript provides a comprehensive overview of potential resistance mutations within MET Receptor Tyrosine Kinase and defines how specific mutations affect different inhibitors and modes of target engagement. The goal is to identify inhibitor combinations with the lowest overlap in their sensitivity to resistant mutations and determine if certain resistance mutations/mechanisms are more prevalent for specific modes of ATP-binding site engagement. To achieve this, the authors measured the ability of ~6000 single mutants of MET's kinase domain (in the context of a cytosolic TPR fusion) to drive IL-3-independent proliferation (used as a proxy for activity) of Ba/F3 cells (deep mutational profiling) in the presence of 11 different inhibitors. The authors then used co-crystal and docked structures of inhibitor-bound MET complexes to define the mechanistic basis of resistance and applied a protein language model to develop a predictive model of inhibitor sensitivity/resistance.

Strengths:

The major strengths of this manuscript are the comprehensive nature of the study and the rigorous methods used to measure the sensitivity of ~6000 MET mutants in a pooled format. The dataset generated will be a valuable resource for researchers interested in understanding kinase inhibitor sensitivity and, more broadly, small molecule ligand/protein interactions. The structural analyses are systematic and comprehensive, providing interesting insights into resistance mechanisms. Furthermore, the use of machine learning to define inhibitor-specific fitness landscapes is a valuable addition to the narrative. Although the ESM1b protein language model is only moderately successful in identifying the underlying mechanistic basis of resistance, the authors' attempt to integrate systematic sequence/function datasets with machine learning serves as a foundation for future efforts.

Weaknesses:

The main limitation of this study is that the authors' efforts to define general mechanisms between inhibitor classes were only moderately successful due to the challenge of uncoupling inhibitor-specific interaction effects from more general mechanisms related to the mode of ATP-binding site engagement. However, this is a minor limitation that only minimally detracts from the impressive overall scope of the study.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101882.3.sa2](https://doi.org/10.7554/eLife.101882.3.sa2)

Summary:

In the manuscript 'Mapping kinase domain resistance mechanisms for the MET receptor tyrosine kinase via deep mutational scanning' by Estevam et al, deep mutational scanning is used to assess the impact of ~5,764 mutants in the MET kinase domain on the binding of 11 inhibitors. Analyses were divided by individual inhibitor and kinase inhibitor subtype (I,II, I 1/2, and III). While a number of mutants were consistent with previous clinical reports, novel potential resistance mutants were also described. This study has implications for the development of combination therapies, namely which combination of inhibitors to avoid based on overlapping resistance mutant profiles. While one suggested pair of inhibitors with least overlapping resistance mutation profiles was suggested, this manuscript presents a proof of concept toward a more systematic approach for improved selection of combination therapeutics. Furthermore, in a final part of this manuscript the data was used to train a machine learning model, the ESM-1b protein language model augmented with an XG Boost Regressor framework, and found that they could improve predictions of resistance mutations above the initial ESM-1b model.

Strengths:

Overall this paper is a tour-de-force of data collection and analysis to establish a more systematic approach for the design of combination therapies, especially in targeting MET and other kinases, a family of proteins significant to therapeutic intervention for a variety of diseases. The presentation of the work is mostly concise and clear with thousands of data points presented neatly and clearly. The discovery of novel resistance mutants for individual MET inhibitors, kinase inhibitor subtypes within the context of MET, and all resistance mutants across inhibitor subtypes for MET has clinical relevance. However, probably the most promising outcome of this paper is the proposal of the inhibitor combination of Crizotinib and Cabozantib as Type I and Type II inhibitors, respectively, with the least overlapping resistance mutation profiles and therefore potentially the most successful combination therapy for MET. While this specific combination is not necessarily the point, it illustrates a compelling systematic approach for deciding how to proceed in developing combination therapy schedules for kinases. In an insightful final section of this paper, the authors approach using their data to train a machine learning model, perhaps understanding that performing these experiments for every kinase for every inhibitor could be prohibitive to applying this method in practice.

Weaknesses:

This paper presents a clear set of experiments with a compelling justification. The content of the paper is overall of high quality. Below are mostly regarding clarifications in presentation.

Two places could use more computational experiments and analysis, however. Both are presented as suggestions, but at least a discussion of these topics would improve the overall relevance of this work. In the first case it seems that while the analyses conducted on this dataset were chosen with care to be the most relevant to human health, further analyses of these results and their implications of our understanding of allosteric interactions and their effects on inhibitor binding would be a relevant addition. For example, for any given residue type found to be a resistance mutant are there consistent amino acid mutations to which a large or small or effect is found. For example is a mutation from alanine to phenylalanine always deleterious, though one can assume the exact location of a residue matters significantly. Some of this analysis is done in dividing resistance mutants by those that are near the inhibitor binding site and those that aren't, but more of these types of analyses could help the reader understand the large amount of data presented here. A mention at least of the existing literature in this area and the lack or presence of trends would be worthwhile. For example, is there any correlation with a simpler metric like the Grantham score to predict effects of mutations (in a way the ESM-1b model is a better version of this, so this is somewhat implicitly discussed).

Indeed, this discussion relates to the second point this manuscript could improve upon: the machine learning section. The main actionable item here is that this results section seems the least polished and could do a better job describing what was done. In the figure it looks like results for certain inhibitors were held out as test data - was this all mutants for a single inhibitor, or some other scheme? Overall I think the implications of this section could be fleshed out, potentially with more experiments. As mentioned in the 'Strengths' section, one of the appealing aspects of this paper is indeed its potential wide applicability across kinases -- could you use this ML model to predict resistance mutants for an entirely different kinase? This doesn't seem far-fetched, and would be an extremely compelling addition to this paper to prove the value of this approach.

Another area in which this paper could improve its clarity is in the description of caveats of the assay. The exact math used to define resistance mutants and its dependence on the DMSO control is interesting, it is worth discussing where the failure modes of this procedure might be. Could it be that the resistance mutants identified in this assay would differ significantly from those found in patients? That results here are consistent with those seen in the clinic is promising, but discrepancies could remain. Furthermore a more in depth discussion of the MetdelEx14 results is warranted. For example, why is the DMSO signature in Figure 1 - supplement 4 so different from that of Figure 1? And finally, there is a lot of emphasis put on the unexpected results of this assay for the tivantinib "type III" inhibitor - could this in fact be because the molecule "is highly selective for the inactive or unphosphorylated form of c-Met" according to Eathiraj et al JBC 2011? These points are addressed in previous work (Estevam et al 2024) or in the detailed methods section, but are not obvious in the main text of the paper.

This paper is crisply written with beautiful figures, and the complexity of the data is easy to understand from an in depth discussion of the mutants that have been previously reported.

Finally, the potential impacts and follow-ups of this excellent study could be used as a resource for the community both as a dataset and as a proof of concept. It is exciting that his approach can be altered and/or improved in the future to facilitate the general application of this approach for combination therapies and the understanding of mechanism for other targets.

Comments on revisions:

Thank you for your additions and changes - they have improved the quality of this paper.
