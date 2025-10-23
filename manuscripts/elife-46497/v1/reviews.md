# Peer review - Round 1

Editors:
- Paul B Rainey, Max Planck Institute for Evolutionary Biology Germany

Reviewers:
- Paul B Rainey, Max Planck Institute for Evolutionary Biology Germany
- Fred Cohan, Wesleyan

## Review text

DOI: [10.7554/eLife.46497.040](https://doi.org/10.7554/eLife.46497.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "The global biogeography of a single SAR11 population is governed by natural selection" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Paul Rainey as the Reviewing Editor, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The outside reviewers have opted to remain anonymous.

Our decision has been reached after extensive consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication at this time. However, we do see the potential for worthy eLife publication, provided all the issues raised by the reviewers can be addressed. Any resubmission would need to be a very substantial revision and would be treated as a new submission.

All reviewers agree that the topic is of considerable interest. They also indicate that your methods appear to have many strengths, but at the same time all are in agreement that much more needs to be done to justify your approaches. For example, Reviewer 3 requests calibration against standard population genetic approaches. Additional problems concern the main claims of the paper such as selective sweeps, the effect of selection, and so forth, which are stated, but not evidently backed by data. Further issues surround use and understanding of terms in population biology/ecology: Reviewer 2 points out the problems with refereeing to diversification within a population when the "population" of interest is really a substantial portion of a genus.

Reviewer #1:

This deals with the causes of patterns of diversity in a widespread marine microbe. The data come from a set of contigs assembled from shot gun sequencing of 21 genomes onto which are read-mapped metagenomic data from 103 samples. The focus is a particular clone that is particularly abundant in southern samples. A core genome is assembled from the metagenomic data and this is interrogated for signatures of selection using a curious approach based on physico-chemical properties of amino acids. A further step looks for correlations with water currents.

At first glance I found the paper reasonably clear, but the closer I read, the more murky things became. In fact I am not too sure what the authors have really done and I am not persuaded that their main claim, that selection is responsible for biogeography in S-LLPA, is supported by their data. Overall the level of explanation is insufficient to allow the reader to understand what has been done.

Among the difficulties:

Title/Abstract: The title states that biogeography is governed by selection, but in the Abstract the authors use more temperate language. So I guess they are not so sure. The Abstract claims that systematic purifying selection and adaptive mechanisms governing non-synonymous variation have been identified, but at best what they have are signatures consistent with expectations. I disagree that analysis of sequence data reveals different niches (it may reveal the existence of ecotypes that may be indicative of distinct niches). What is a proteotype?

Place of isolation of the focal 21 SAR11 genomes is important in a study of biogeography, but no attention has been given to this.

There are many challenges in drawing conclusions from metagenomic data via read-mapping to a reference. Particularly problematic is the fact that diversity of closely related organisms within a sample is not known. Thus when many SNPs are detected is this indicative of a diverse population, or is it a signature that comes from a single over-represented clone that is rather divergent? Similarly, the authors take high similarity as signature of a recent sweep, but this might reflect a single over-represented genome from a closely related organism. I'm not sure how the authors dealt with these and similar problems.

With regard to selective sweeps, the results of the analysis appear not to be given (subsection “SNVs to SAAVs: Accurate characterization of non-synonymous variation”, gives the conditions that need to be fulfilled in order for a protein to have undergone a sweep, but not the results).

Patterns of amino acid substitution types seems an interesting way to go, but this needs to be unpacked, explained and justified.

Partitioning of SAAV between warm and cold currents: there seems to be a correlation with clustering based on SAAVs, but as above, I need to have more explanation. Much relies on the robustness of the SAAV profile clustering (Figure 3A) and there is no indication of its statistical likelihood.

The crunch of the paper is rejection of the neutral model, but this is done by simply saying that neutral models could not explain the observed patters of amino acid substitutions, but no evidence is provided. Also, Figure 4, which I hoped would enlighten me, does not exist.

In general I found the figures overly dense and very difficult to understand given the paucity of explanation in the captions. Take Figure 1: latitudinal gradient, I presume north is at the top? Colouring seems inconsistent and so on.

Reviewer #2:

It's hard to tell who this paper is written for. The bioinformatics applications are the most interesting: identifying the core genome of a lineage of interest from metagenomics data, using a novel algorithm for (somehow) identifying significant subclades within the lineage, and finding a surprisingly high frequency of certain amino acid substitutions that are not predicted by Blosum. There are also interesting implications for ecological diversification, but this aspect of the paper is written without enough explanation or interpretation of data, as I will detail. Also, I think most microbial ecologists would be amazed to see a paper on diversification within "a single population" that is actually not a population at all, but rather a fair chunk of a genus.

It is so inappropriate to call the S-LLPA lineage a "single population," since it has nearly 20% sequence divergence within it, and because there is clearly profound ecological diversification within this group. (Given that the Eren group has made tremendous progress toward discovering newly divergent, ecologically distinct populations of bacteria with their MED algorithm, it seems ironic that the group is now calling this phylogenetically huge group a single population.) Calling this group a population seems to have led to the conclusion that "their broad geographic prevalence suggest<s> dispersion is not a limiting factor for SAR11 in surface seawater…." But this conclusion is based on a false reification of all the various true populations within what the authors are calling a population.

The authors talk about S-LLPA offers "a unique opportunity to study the genomic diversity and evolutionary genomics of a single marine microbial population…." Not so unique when the "population" is a huge chunk of a genus.

The authors do justify their calling this clade a population because it constitutes what is recruited by a single isolate from various metagenomes. But their own work clearly shows, to my mind, that this is not a good way to discover populations.

The authors have used their Deep Learning algorithm for demarcating six phylogenetic groups, which they call proteotypes, from their S-LLPA lineage. It is frustrating that the authors neglected to give any rationale for their approach. Is it based on sequence clustering of shared genes? Is it based on genome content sharing? Or both? (Even though the algorithm has been published, they should say something briefly about what the inputs are and how it works.)

On two occasions the authors write about protein sweeps. They state that the sweeps are "rare." I think most evolutionary ecologists of bacteria would want to know how rare, and in which genes. Also, it would be important to indicate whether the sweeps traveled across ecologically distinct groups. In the first paragraph of the Discussion, the authors mention that there are more sweeps in warm currents, but this should be fleshed out and made clearer.

Subsection “Purifying selection governs the identity of amino acid substitution types”, first paragraph. It wasn't clear to me whether the authors were claiming that their focus group was unique in having a stable proportion of amino acids on a global scale, or whether other groups are showing the same pattern.

In the subsection “Purifying selection governs the identity of amino acid substitution types”, I don't see how the authors are finding evidence of purifying selection. Rather, it seems they are finding the constraints on adaptive substitutions of amino acids. That's different from purifying selection, which is usually the evolutionary stability of a particular sequence.

It's interesting that there are two clades within S-LLPA that are associated with different temperature regimes. And it's interesting that the subclades within these clades are different in the geographic regions where they are most abundantwith similar temperatures. The interpretation of this result depends on whether different cold-adapted subclades are never found together (meaning that they may have no adaptation differences) or whether they sympatric to some extent (meaning that they are coexisting based on ecological differences other than temperature partitioning). It seems that the latter is the case, but the authors should have made this clearer. For example, pie charts showing the relative abundances of the subclades in each region would be useful.

Reviewer #3:

The work by Delmont et al. describes a large-scale and thorough analysis of an important marine bacterium population, SAR111. They use multiple approaches to identify signals of selection to understand the evolution and ecology of these microbes. The authors deserve credit for their very clear presentation of data and methods. However, I have multiple concerns regarding the analysis and interpretation of the data:

1) The nature, and strength of, selection pressures acting on this bacterial population are not clearly defined.

a) The description of the substitution analysis "suggests a powerful influence of purifying selection", while also "suggesting a role for adaptive processes for functional diversification of S-LLPA proteins". Which of these dominates? Could this just be noisy neutral evolution – what is the expected variation of the S statistic, and the SAAV patterns, under a neutral scenario?

b) The neutral model of Hellweger et al. still predicts geographic separation of strains, which should be made clear in the Introduction. A falsification of this would be a repeated association of bacterial strains with ecological niche. This appears to be the case at the highest level of the hierarachy inferred with "deep learning", but at lower levels, predictors are genetic, not ecological, and therefore likely represent characteristics that were identified by the clustering algorithm itself. This might be expected under a neutral model.

2) The authors have opted against traditional population genetics methods. It is possible that the new methods are a substantial improvement, but they need to be justified. Some examples:

a) The authors justify using the "S" statistic rather than d(N)/d(S) based on there being many instances of multiple substitutions within the same codon. But this is exactly what d(N)/d(S) is meant to correct for, and S does not capture – there may be many synonymous substitutions on an evolutionary pathway, but if only one of them is non-synonymous, then S will only count this only as a non-silent change, underestimating purifying selection. What is the neutral expectation for S?

b) The BLOSUM matrices are used as "as a proxy to assess the functional difference between the pairs of amino acids", which are then compared to the substitution frequencies – but this is circular reasoning, as these matrices are calculated from substitution frequencies. The versions used in the paper are also inappropriate for this dataset, as they were calculated using more closely-related sequences than are compared in this paper.

c) "Deep learning" is applied to cluster populations together through a method designed without genetic data in mind. This does not mean it is wrong, but as it is not an intuitive approach, it would be helpful to see validation against a more standard method, such as the fixation index, F(ST). This would help understand the distinct properties of the six subclusters – for instances, proteotype D looks to be a single successful "strain" – is this expected to be picked up as a signal by the "deep learning"?

3) Quality of read mapping. Many of the sequences being compared are highly divergent, but most mapping software is intended to align reads to highly similar reference sequences. While there is a promising correlation between the SNP densities identified by BWA and BOWTIE2, there is a greater than two-fold difference in the absolute densities. This suggests a very high false positive or false negative rate, depending on the method. The authors need to validate the performance of these algorithms when using highly divergent reads. Additionally, what is the justification for using the "the base-5 logarithm of the mean coverage of a gene remained within {plus minus}1 of that for the mean coverage across all genes" for assessing consistency of coverage?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Single-amino acid variants reveal evolutionary processes that shape the biogeography of a global SAR11 lineage" for consideration by eLife. Your article has been further reviewed by three peer reviewers, including Paul B Rainey as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Fred Cohan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a further revised submission.

All reviewers appreciate and acknowledge the significant work that has gone into the paper during the course of the revision, the reviewers are all equally enthusiastic about the paper. However, there remain issues that need attention in order for the paper achieve the impact that it deserves. The reviewers' comments are pasted below, with the collective comments boiling down to a request to supplement the deep learning analysis with a more standard evolutionary approach in order for the reader to know whether the results are consistent with what most people in the field know. Here it is important to clearly distinguish between neutral evolution, purifying selection, and adaptive divergence. It is the latter that is particularly relevant to addressing the question of the possible ecological distinctions among populations.

Collected reviewer comments:

The paper is vastly improved since the original version. It is now much clearer and more compelling, and the paper deals with the issue of populations better.

The paper is fascinating for showing that whatever cohesion occurs at >95% ANI in pretty much every other bacterial group does not occur here in SAR11. The paper is also really interesting for giving a robust and sensitive way to identify ecologically distinct metagenome groups from sequence data.

My concerns are mostly focused on what the authors have found out about ecological diversity within the 1a.3.V lineage.

First, I appreciate that the authors are trying to be more careful about using the concept of population, but there are still places where they are still unclear about what they mean. The authors write of "remarkable intra-population genomic diversity…." It's not clear exactly what the authors mean by "population" here, but in this context what they mean is very important. If there isn't a good definition of population being used, then how can one talk about one population's intra-population genomic diversity being higher than another? It all depends on what you mean by population, and that's not clear here.

Figure 2 purports to show that there are not sequence-discrete populations within 1a.3.v, at least not in the sense that Kostas Konstantinidis demonstrates them in his studies, most recently in Jain et al., 2018. It is really interesting that all the SAR11 clades (with just this one clade shown in Figure 2) do not show the drop-off in recruitment of metagenome sequences below about 95% ANI. The authors argue that part of the great sequence diversity of what is recruited into this lineage (that is with much lower ANI) emerges from there being ecological diversity within the lineage (adaptations to different temperatures among different sublineages). I don't think this is a reasonable explanation, as almost every species taxon, nearly all obeying the 95% ANI drop-off rule, is also ecologically heterogeneous. I have suggested, in an interpretation of the recent Jain et al. paper, that the cohesion holding a species taxon together stems from an ability of recombination to act frequently at >95% ANI, plus the possibility of adaptive genes passing between ecologically distinct populations that are >95% ANI (Cohan, 2019) I'd argue that there is more potential for either recurrent recombination to limit divergence among ecologically distinct populations in SAR11, or greater opportunities for a single gene to be adaptive across different populations.

I'd like to add that whatever cohesion occurs at >95% ANI in most species taxa does not address the ecological diversity within species taxa, or whether there are sequence-discrete populations within each taxon. In fact, most species taxa have sequence-discrete and sequence-discoverable ecologically distinct populations. (This is the point of the second half of my Current Biology dispatch I mentioned.) So, I don't think that Figure 2 makes an argument that there are not sequence-discrete, ecologically distinct populations within the focus lineage.

The authors have noted that there is a small minority of genes that are invariant at the amino acid level across a given metagenome. In the earlier version, they interpreted these observations as evidence of sweeps, but here they have chosen not to address the dynamics that can be inferred by these invariant genes. I think that such single-gene sweeps are very interesting, and have been the topic of discussion of some very interesting papers, including papers by Jesse Shapiro and by Rex Malmstrom. I'd encourage the authors to bring this discussion back. I'll mention that these instances provide evidence that a generally adaptive gene has passed by recombination across all the ecologically distinct populations within a lineage, but I wouldn't expect the authors to necessarily buy in to that interpretation.

I found the authors' partitioning of metagenomes into ecologically distinct groups fascinating. And it's particularly interesting that these groups could not be revealed (at least entirely) by analyzing single reads (as shown in Figure 4—figure supplement 3). I'll encourage the authors to venture from their interpretation regarding whole metagenomes to inferring that there appear to be multiple ecologically distinct populations that cause these metagenomes to hold different niches. What might be the ecological distinctions of the populations? Clearly they are different for their temperature adaptation, as revealed by Figure 4 (mislabeled Figure 5). Perhaps the authors could glean something about what is different about the constituent populations from their Figure 4—figure supplement 3, that is by comparing the clusters that they do find with known environmental parameters.

Re the concluding statement about "everything is everywhere," I'd temper that by saying 'at least for marine bacteria'. This is because the statement does talk about "everything," so I think there needs to be some limitation to the conclusion.

Concerns about evolutionary analyses:

In response to point (1), the authors state:

"Simply, we observed that certain amino acids (mostly hydrophilic), and most notably, few AASTs (e.g., alanine/isoleucine) predominated in our SAAV table."

It has been well-established for decades that hydrophobic amino acids in solvent-inaccessible positions are more conserved (e.g. see reviews cited in the Introduction to Ramsey et al. 2011 Genetics 188(2):478-88). Reproducing this observation in the SAR11 dataset simply confirms that purifying selection can be observed over long timescales. It does not help identify what the changes are that enable ecological adaptation.

Delmont et al: "These points are interesting, but they do not favor natural selection over neutral evolution. Instead they provide information regarding permissible versus non-permissible diversification"

I assume "permissible" refers to purifying selection? Which is an example of natural selection – rather than random, neutral diversification. It is distinct from the adaptive/Darwinian evolution that allows the ecological differentiation of the bacteria. Not separating neutrality, purifying selection and adaptive evolution plagues the whole manuscript. The authors have a strain distribution that appears to reflect ecological differentiation, rather than neutral diffusion. They have a mutation distribution that mainly seems to reflect purifying selection, rather than neutral evolution. Some analyses (e.g. below) suggest adaptive evolution, which is potentially very interesting, but the overall trend is consistent with purifying selection. The authors need to clearly distinguish their different conclusions.

Delmont et al: "we determined that thousands of 1a.3.V allele frequency trajectories correlated with in situ temperature, in line with the biogeography of proteotypes"

It is not surprising that many of the variable sites correlate with temperature, because the proteotypes are defined using the variable sites, and the proteotypes correlate with temperature. The authors should seek to synthesize these data – do the variable sites have properties that suggest selection between niches? Do they concentrate in particular genes that might drive adaptation to different niches? Or do they simply correlate with the population structure?

Overall, I return to my original point from the first round of reviews: is the diversification mainly neutral; dominated by purifying selection; or dominated by adaptive evolution? The most interesting signals may not be from the dominant evolutionary process, of course.

In response to point 2, the authors state:

Delmont et al: "As far as we know, there is no published study that effectively takes into account multiple SNVs per codon without calculating the exact codon frequencies to estimate synonymity accurately…SNV density was high for 1a.3.V and many SNVs co-occurred in the same codon, rendering classical d(N)/d(S) analyses limited, which had never been challenged with extremely complex environments, if not completely irrelevant."

Yang (2007) MBE 24(8):1586-91 – with over 6,000 citations – describes how baseml can be used to calculate d(N)/d(S) using base substitution, rather than codon substitution, models. This accounts for multiple substitutions per codon, and provides a statistical test for evidence of selection versus neutrality, unlike the methods presented in the current version. It does not matter how complex the environments are – indeed, d(N)/d(S) has been applied to the question of SAR11 adaptation to different ecologies by Brown et al., 2012 and Luo and Hughes, 2012 Mol. Syst. Biol. 8:625. The authors should at least apply standard methods to the assembled genomes, based on the ecological separation they have determined. Methods also exist for calculation of this statistic from metagenomic data, and might be more informative.

Delmont et al: "The significant shift in SAAVs/SNVs ratio between cold currents and warm currents is of relevance to our study, especially in light of other insights (especially, the linkage between allele frequency trajectories and in situ temperature, and the biogeography of proteotypes), favors the predominant role of natural selection acting on the permissible amino acid diversification traits of this global SAR11 lineage."

The correlation between allele frequencies and temperature, and proteotype and temperature, is confounded by the correlation between proteotypes and allele frequencies. This should be explained (if this is wrong, please also make that clear in the text). The authors need to make clear whether the natural selection they are referring to is stronger/weaker purifying selection changing the SAAV/SNV ratio; or positive selection driving adaptive diversification increasing the SAAV/SNV in some populations.

Delmont et al: "Regarding the fixation index, we agree with the reviewer that this would have been a valuable addition to our work…We believe the significant amount of methodological development in this work that offers descriptions of the biogeography of the most abundant lineage in surface oceans conveys a story that will not benefit from the inclusion of additional analyses. "

I don't understand how this statistic can be "a valuable addition", yet the story "will not benefit from the inclusion of additional analyses.". The deep learning analysis is still not intuitively explained in the new version (not the authors' fault, as these methods are designed to be complex). It should be complemented by fixation index calculations, which are simple, and would allow the readers a much greater insight into the basis of the results.
