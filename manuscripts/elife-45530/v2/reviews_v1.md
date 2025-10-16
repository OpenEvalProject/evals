# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45530.sa1](https://doi.org/10.7554/eLife.45530.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides a comprehensive search for proteins whose evolutionary emergence can be dated to the last common ancestor of the Bilateria. The main aim of this study is to shed light on the genetic changes that underlie account of key innovations in the bilaterian body plan. For this purpose, the authors have compiled an impressive data collection comprising protein coding genes from pre-annotated data, a filtered collection of genomic ORFs stemming from a six-frame translation of entire genome sequences, and eventually transcriptome data for taxa lacking a genome sequence. The key asset of this data collection, when compared to existing ortholog databases, is the-according to contemporary standards comprehensive-sampling of non-bilaterian metazoan species. The much more comprehensive inclusion of non-bilaterian datasets in this study allows a more accurate orthogroup clustering than previous studies. Moreover, this database of sequences presented is a rich resource for reconstructing gene content at any metazoan node.

Decision letter after peer review:

Thank you for submitting your article "The genetic factors of bilaterian evolution" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor.

The following individuals involved in review of your submission have agreed to reveal their identity: Ingo Ebersberger (Reviewer #2). The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary:

In their manuscript, Heger et al. present a comprehensive search for proteins whose evolutionary emergence can be dated to the last common ancestor of the Bilateria. The main aim of this study is to shed light on the genetic changes that underlie account of key innovations in the bilaterian body plan. For this purpose, the authors have compiled an impressive data collection comprising protein coding genes from pre-annotated data, a filtered collection of genomic ORFs stemming from a six-frame translation of entire genome sequences, and eventually transcriptome data for taxa lacking a genome sequence. The key asset of this data collection, when compared to existing ortholog databases, is the-according to contemporary standards comprehensive-sampling of non-bilaterian metazoan species. For the ortholog search, they present a modified version of the orthoMCL algorithm. The resulting orthologous groups are then subjected to a number of intuitive, yet largely ad hoc, filters to identify a set of 157 orthologous groups the authors date to the last common ancestor of the Bilateria. The remainder of the manuscript is then dedicated to discuss these 157 orthologous in the context of bilaterian evolution.

BigWenDB, a new database maximising resolution at the bilaterian origin, building on opisthokont sequences from GenBank, as well as transcriptomes available for non-bilaterian animals, is an important contribution for the field. Orthogroups are identified using a modified the OrthoMCL pipeline, and validated against an external benchmark set of 70 manually curated orthogroups. An HMM-HMM comparison step evaluates orthogroup completeness. The main value of this studies lies in the much more comprehensive inclusion of non-bilaterian datasets in BigWenDB, allowing a more accurate orthogroup clustering than with previous efforts. This database is a rich resource for reconstructing gene content at any metazoan node. Clustering reveals a clear pattern of enrichment among the 157 bilaterian-specific genes, with transcription factors and membrane proteins of various kinds dominating – in contrast to other nodes of the bilaterian tree. Also, the identification of monoamine neurotransmitter reception and nodal signalling as bilaterian-specific innovation is a valuable step forward in our understanding of bilaterian evolution.

Essential revisions:

1) The authors present a way of compiling orthologous groups from their data, which deviates from currently available methods. In particular, the hmm-hmm comparison is, to my knowledge, unprecedented. This pipeline is presented as a main methodological innovation of this manuscript. Although I appreciate that the authors are concerned about the performance of their method, the data set used for method validation is way too small to thoroughly benchmark the method. I strongly suggest that the authors make use of the public benchmark service for ortholog search tools at https://orthology.benchmarkservice.org (Altenhoff et al., 2016) for this purpose.

2) The authors do not consider the limited sensitivity of Blast based ortholog search tools, which leads to an underestimation of gene age (e.g. Elhaik et al., 2006; Luz et al., 2006; Moyers and Zhang, 2015, 2016, 2017; Jain et al., 2019). In this context, it is a bit worrying, that proteins involved in regulatory functions (transcription factors), and proteins located in the membrane appear enriched in the set of Bilateria-specific proteins. Evidence exists for both kinds of proteins that their particular rates and mode of evolution increases the risk of missing distantly related orthologues (Jain et al., 2019). Although the reciprocal hmm-based search could ameliorate this problem, it is likely to be not helpful. This is, because the high evolutionary rate of such proteins paired with the presence of very common functional domains, e.g. a Zn-Finger, probably results in rather uninformative hidden Markov models.

3) I miss the definition of clear-cut evolutionary scenarios. For example, it is unclear what it means when a gene emerges in the LCA of the Bilateria. Is it a de-novo gene birth? Or do the authors also take into account lineage specific gene duplications, probably in combination with domain gain or loss? From what I see in the data I have the impression that the authors consider both. I will exemplify my concern using Figure S14. It shows a phylogeny comprising both FoxH1-an alleged bilaterian invention-and the older FoxD. The way how the tree is drawn implies that it is rooted. If so, it can only be interpreted in the following way: A gene duplication at the root of the metazoa gave rise to FoxH1 and to FoxD. While FoxD is still seen in metazoa, which branched off prior to bilaterian diversification, FoxH1 is nowadays retained only in the Bilateria, and the corresponding orthologs were lost in earlier branching taxa. If this were true, then FoxD would be as old as the animals. Alternatively, one could consider an outgroup rooting. Then FoxD and FoxH1 diversified only at the root of the Bilateria. This diversification would then be the true innovation, but then FoxD and FoxH1 would be co-orthologous to the proteins in the early branching animals. I think the authors have to be way more specific here.

4) The authors use phylogenetic trees to support, or more often to reject an orthology relationship, e.g. subsection “Changes in axon guidance accompany bilaterian evolution”. I am missing topology tests, e.g. the Shimodaira Hasegawa test, to show that a gene tree indeed differs significantly from the species tree. This is necessary, because the phylogenetic information within one orthologous group is, in many cases, not sufficient for accurately resolving the evolutionary history of the corresponding proteins.

5) The resampling approach to show that bilaterian genes are significantly more connected in PPI networks than it is expected by chance is likely to be confounded with gene age. There is evidence that evolutionarily older genes are more central in PPI networks than younger ones (Kim and Marcotte, 2008). Any resampling method that also selects young genes is therefore likely to result in less connected networks.

6) The reciprocal best hit approach, which is used in the final filtering of the candidates is problematic. Reason is, that the initial Blast against non-redundant genbank can have any paralog as a best hit, since the assumption that the entire proteome of each species is represented in the data base is probably not valid.

7) Based on what evidence do the authors consider five independent losses unlikely? And what is an “undetermined orthology”. Can the authors reject that the poriferan sequence is an ortholog of Eomes, and if so again based on what evidence?

8) To consider: one reviewer found the data set overly complex. Because the story is pretty complex, they thought it would do very little harm to omit the genomic ORFs from the analysis.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The genetic factors of bilaterian evolution" for further consideration by eLife. Your revised article has been evaluated by Patricia Wittkopp (Senior Editor), and two reviewers, including the guest Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined in the comments from the re-review below.

Reviewer #1:

This is an interesting and important manuscript dealing with the identification and reconstruction of the ancestral pool of bilaterian genes and bilaterian innovations.

Different authors used different approaches, and the story is ongoing. I consider the manuscript as a next step to decipher the complex story of the amazing diversification among bilaterians.

In my opinion, it is also a valuable reference paper, and this study would be used by the biological research community for future efforts to reconstruct the set of genes underlying bilaterians innovations.

The paper is supported by an extensive supplement, which is an additional and beneficial reference source of specific information about hundreds of genes.

The authors performed a very careful revision of the manuscript and clarified the previously raised questions. The authors identified a subset of about 150 genes as bilaterian-specific innovations and provided a solid argument to support their gene selection criteria.

In general, the paper advances the field and will be an important web resource of comparative data for future investigations.

One of the major critical points: The authors mainly provide the description of identified genes and relatively little critical analyses. I understand that the selected design of the manuscript might reflect the nature of the complex bioinformatic study and reflect a limited knowledge about the functions of many genes in different bilaterian lineages. Nevertheless, I would recommend to critically reread the manuscript and carefully think about generalized statements, when they use references to the vertebrate/arthropod data vs. other lineages.

There are some moderate and minor comments, which might improve this manuscript.

1) Introduction: "In contrast, the evolutionary relationships of non-bilaterian metazoans are still a matter of debate, in particular the relative positions of placozoans, ctenophores, and sponges (Brooke and Holland, 2003; Ryan et al., 2013; Pisani et al., 2015; Simion et al., 2017; Feuda et al., 2017). "

– It is a biased reference list with three references stressing one point; the alternative reconstruction of the animal phylogeny should also be presented (e.g., Whelan et al., 2015 – PNAS; Whelan et al., 2017)

2) Introduction: Genomic sequencing of non-bilaterian animals revealed that essentially all signalling pathways and developmentally important genes from bilaterians are also present in non-bilaterians, indicating that these genes evolved before the advent of bilaterians.….

– "…all…important genes" is an incorrect and biased statement. Frankly, we do not know all important genes for most of the bilaterian lineages. Regarding all signaling pathways, many genes related to neuronal signaling and immune systems, for example, are absent in some non-bilaterian metazoans (see for examples in Moroz and Kohn, 2016)

3) Result subsection “Bilaterian G protein-coupled receptors and the control of physiological state through circulatory flow”, paragraphs one and two.

– Discussion about the monoaminergic reward system, as a generalized statement for bilaterians, is highly speculative. I would recommend using more careful wordings since the functions of many GPCRs are putative and speculative.

-

4) Result subsection “Bilaterian G protein-coupled receptors and the control of physiological state through circulatory flow”, paragraph three .

– Speculations about the peptidergic reception. There are many uncertainties about GPCRs in the majority of bilaterians, and it is difficult to say about functions and ligands of putative (neuro)peptide receptors. I suggest using more careful wording.

Reviewer #2:

In their revised version, the authors have addressed many of my initial concerns, and I trust that this is a relevant study, in principle.

However, some issues remain, which I think can be addressed by carefully re-working the argumentation.

1) I asked in my initial review about a benchmark of the new ortholog assignment method making use of the QfO reference proteome set. The authors chose to not follow this up and justified this with two arguments.

a) First, they stated that their core method is basically a re-implementation of OrthoMCL, and use the times the OrthoMCL paper has been cited as kind of a quality criterion. Needless to say that I am not happy with this argument. OrthoMCL has been shown to have, compared to other methods, a very high false positive rate of 16% (Chen et al., 2007). Thus, it is probably not the number of citations for OrthoMCL, but rather the performance of this tool, the authors should use in their argumentation. I strongly encourage to adapt the discussion in this direction. If they have the feeling that a high false positive rate does not matter, which of course is the case when a high sensitivity is desired, and false positives are either sorted out at a later curation step, or false positive make the analysis more conservative, and thus are ok, then they should explain this to the reader.

b) As a second argument, the authors state that the key advantage „(...) is not the core method (OrthoMCL), but the inclusion of several steps for error correction after orthology clustering, including a new HMM-HMM reciprocal best hit test for orthogroup completion (see, e.g., Supplementary file 1—supplementary table 7). These additional steps (together with careful sampling) distinguish our pipeline from the original OrthoMCL and from other orthology pipelines and influence the interpretation of cluster/orthogroup origin. The additional steps are computationally demanding and require, at present, extensive manual processing. We performed them, as proof-of-principle, for the 157 orthogroups with assumed bilaterian ancestry, but this approach is not yet scalable. Applying the steps for error correction to all clustered outputs for reference proteomes from a public database is therefore not feasible."

I am a bit puzzled reading this response. If I understand the answer correctly then the authors state that they perform a semi-automated curation of orthologous groups predicted by orthoMCL, which is absolutely fair. In their manuscript, however, the authors advertise their method as "A unique orthology pipeline for the identification of bilaterian-specific genes", which creates the (untested) impression that the pipeline outperforms existing ortholog search tools. I see two possibilities. Either, the authors present their method as a curation step without the claim of having developed a new ortholog search pipeline. Or, alternatively, they perform a comprehensive benchmark comparing it to existing and state of the art “orthology pipelines”. As a last aspect to consider, part of the QfO benchmark analyses are independent of the QfO reference proteomes. For example, tree discordance tests can be, in principle performed with any underlying set of proteomes.

To sum it up, my main concern is not necessarily the method itself, except the orthologous group completion step using hmm-hmm searches, of course. Rather, I am very much worried about the fact that the authors generate the impression of having developed a new pipeline for orthologous group compilation, which apparently performs better than existing software.

2) My second concern was the limited sensitivity of Blast in ortholog searches. I very much appreciate that the authors have considered this now in the Discussion. In my opinion, some aspects require further attention. Moyers and Zhang, as well as Jain et al. have shown that the sensitivity of Blast can become limiting even when searching for orthologs in the same kingdom. I think it would be a good idea to openly discuss the issue of limited sensitivity ignoring the fact that you “only” search within the same kingdom. It is then straightforward to propose extensive taxon sampling together with the very sensitive hmm-hmm comparisons as a way out of this problem. The shift to a different search method comes then at the cost of a substantially decreased specificity in the ortholog assignment (see my point above). The authors can then explain why they think that an elevated rate of false positive either do not harm, or how they get rid of them in a downstream curation.

3) The authors write in their response "Our primary intention was to generate molecular phylogenies as a means of validating orthogroup clustering, not for inferring specific evolutionary scenarios directly from the gene trees." I cannot follow this argumentation, and I am convinced that I misinterpret the answer. Phylogenetic trees are the basis for deriving evolutionary scenarios on the sequence level, and I cannot see how this cannot be the case. In this context, I regret to say that I find the sentence "The relationship between orthology clusters is imposed by the method and does not necessarily reflect the timing of evolutionary events" impossible to understand. A phylogenetic tree that does not reflect the timing of evolutionary events is either wrong or unrooted. If the latter is the case, then there has to exist the possibility to place the root such that the evolutionary scenario emerges that is proposed in the text. If this is not the case, then again either the tree or the proposed scenario is wrong.

Concerning the precise example of FoxH1: Given the tree shown in Figure 5—figure supplement 3, there is no way that FoxH1 is a bilaterian invention. The FoxH1 lineage split from its sister group (either FoxQ1 or FoxD) via a gene duplication prior to the diversification of the bilateria. If no FoxH1 sequences outside the Bilateria were found, then they were either lost-which still does not make FoxH1 a bilaterian invention-or the taxon sampling was not sufficient, and non-Bilaterian FoxH1 sequences await their detection. Alternatively, the tree is wrong, but then it should not be shown. I consider this a major issue.

4) As a response to my concern about missing topology tests, the authors have recomputed the trees and have added approximate SH-LRT support values. They write in their answer "Although the new phylogenies fully support the conclusions derived from the original analysis using RAxML, we acknowledge that some trees show high gene/species topology discordance within a given protein clade(orthogroup). We accept that this is, in part, the consequence of including mixed data types, such as the shorter ORF sequences, and sequence sets not optimized for phylogeny because they are often derived directly from the orthogroups obtained in our clustering." I do not get the point about why it is a problem of using sequences directly derived from orthogroups. Is this again an issue of missing specificity in the ortholog assignments?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "The genetic factors of bilaterian evolution" for consideration by eLife. Your article has been considered again by one of the original reviewers, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. While we found most of the reviewers’ prior concerns addressed satisfactorily, there was also one major concern not fully addressed. This concern must be addressed in an additional revision before we can consider this manuscript further.

This is a highly complex manuscript, and all conclusions essentially depend on the accuracy of the orthology assignment and the correct phylogenetic interpretation. This was pointed out in the previous round of reviews using the FoxH1 tree as an example. This tree suggests that FoxH1 is as old as the metazoa, and the same is true for EOMES (Figure 5—figure supplement 3 and 4). In the response, the authors state that there are several reasons why the trees shown might not accurately reflect the evolutionary history, and mainly mention heterotachy following gene duplication, which makes the gene look older than it is. This may or may not be correct. To further corroborate their argumentation, the authors state that independent gene loss, which would be required to explain the present day distribution of the respective genes is unlikely, and there is no report for such parallel losses in the literature. Previously published work, including https://www.biorxiv.org/content/10.1101/2020.04.23.058008v1 and https://www.nature.com/articles/s41467-018-03667-1 are at odds with this statement.

We recognize that reconstructing evolutionary relationships with individual sequences is hard. But if the tree is at odds with the conclusion, then this has to be addressed with analyses, and not just by saying “probably the tree is wrong”.

We see two ways out of this dilemma:

One is for you to perform additional analyses, which will take time. This would likely have to include the results of the ortholog searches in a well-defined set of species, such that presence/absence of orthologs can be interpreted along a (known species) tree. For example, at the moment, it is unclear why the tree of Nodal features about 30 vertebrate sequences, that of FoxH1 only about 20 sequences, and that of EOMES only 2. Although these numbers are not relevant when it comes to the age of the genes, they tell us something about the precision and rigor of the analysis.

The other possibility is that the authors could modify the manuscript to avoid the term “innovation” where it is not backed up by the data. If the tree argues for an evolutionarily old gene, which nowadays – and according to the analyses of the authors – is confined to the bilateria, why not simply call it a “bilaterian-specific” gene, leaving it for the moment open whether it was indeed an “innovation” or a selective retention of an older gene. In essence, the authors would then argue with their phylogenetic profiles, which seem to be comprehensive, and not with trees, which they indicate in the response might be wrong anyways. If the authors then wish, they could speculate that the gene is indeed a bilateral innovation, but it has to be clear that this is a speculation that would require more thorough analyses to be tested.
