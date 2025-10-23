# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- Nir Ben-Tal, Tel Aviv University Israel

## Review text

DOI: [10.7554/eLife.39705.034](https://doi.org/10.7554/eLife.39705.034)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "Molecular function limits divergent protein evolution on planetary timescales" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nir Ben-Tal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The other reviewers remain anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

Summary:

The manuscript analyzes clusters of orthologue enzymes of the same function, defined as sharing the same 4-digits EC number, to examine the limitation of function preservation on evolutionary divergence. The results seem to indicate that function confines divergence, which is not surprising. The potential novelty here is the time dependence of the process, where phylogenetic time of species divergence is used as natural time scale "clock". The data shows that proteins diverse from each other rapidly during the first ~1.5 billion years, but saturate after that.

Opinion: The manuscript addresses an important and interesting topic, but it should be revised significantly to clarify what exactly was computed and why, what was measured and why, and how the results are related to previous studies. In view of the amount and nature of the issues raised, the authors should consider withdrawing the manuscript.

Major concerns:

(pretty much copy-pasted from the individual reports)

1) This study poses the question about the extent to which function constrains sequence divergence. The answer given is that for orthologous enzymes 25% sequence identity is the approximate limit. The major critique, is that the authors did not make an attempt to provide a clear mechanistic explanation for such phenomenon. Is it simply because a significant fraction of positions is invariant? Is it because there are various constraints on various sites? Is it because only a small subsets of amino acids are tolerated at some sites? Why not take several enzyme families with very thick alignments and analyze them position-by-position to shed light on this question? Without such deep analysis, the paper, while interesting in its general idea, reads superficial and underdeveloped, despite some experimental results.

2) The authors premise their study on the assertion made by Rost in a 1997 review that proteins of the same fold can diverge up to random sequence ID of 3-5%, i.e., that structural similarity does not impose constraint on sequence ID. As a consequence the authors attribute in their analysis all sequence identity constraints to functional similarity. However, this premise is highly problematic. While anecdotally one can find two proteins of similar fold with very low sequence ID, typically proteins with similar structure (not necessarily orthologues) have sequence ID at or above 25% – this is the essence of the famous cusp in sequence-structure relationship first reported by Lesk and Chothia in the eighties. In fact a careful analysis of structural/stability constraints on sequence divergence has been published in recent paper (Biophys J v.112, p.1350-65, 2017) where it was shown that in divergent evolution scenario protein structure is maintained up to 25-30% sequence ID and quickly deteriorates beyond that. Incidentally it is very close to 25% ID which the authors claim to stem from functional constraints. Furthermore, the above mentioned BJ paper presents a detailed analytical estimate of sequence divergence dynamics akin to exponential fits used in this PAPER. The authors should make themselves familiar with this theory and consider using it to fit their divergence curves rather than ad hoc exponential fits.

3) The high throughput experimental data is potentially interesting but its description is so cryptic and incomplete that it is very hard to assess what actually has been done there. In particular there is no assessment of noise in deep sequencing to assess fitness, of the effects of synonymous substitutions, etc. How is the data binned and why binning? The use of LB as a medium for the folA experiment is unfortunate because in LB DHFR is much less essential than in minimal media and therefore the results could be skewed by very permissive conditions. In addition the standing genetic variation is not taken into account – fitness effects could be a result of hitchhiking (i.e. originate from the variation of the background into which the mutations are introduced). These concerns aside, it is not entirely clear what does comparison with experiment tell us beyond the obvious that sites where deleterious fitness effects are greatest evolve more slowly. Was the sole purpose of the experiment to bin positions by their fitness effects? If so, what new insight is gained from slower divergence of sites with more profound fitness effects compared to faster divergence of sites that are more tolerant to substitutions in experiments. Isn't this effect expected? Maybe quantification of the effect may have some novelty, but such quantification has not been done. The obvious thing to do is to compare their alleged fitness effects with dN/dS assessment for the rates but that has not been done.

4) The word "protein" should be replaced with "enzyme" in the title. "We focused on enzymes because their molecular function is usually well defined," doesn't sound quite true. Reading the manuscript, it seems that the goal of this work is to investigate divergence of enzymes. The divergence of non-enzymes will most likely follow a different pattern and will generally be much lower than 25% identity. If the authors want to generalize to non-enzymes, they need to perform appropriate analyses. Currently, only one experiment is dedicated to a non-enzyme. It is not fair to the readers to generalize beyond the scope of analysis that was carried out.

5) The sentence in the Abstract "divergence rates of orthologous enzymes decrease substantially after ~1-2 billion years of independent evolution" is confusing. "Rate" means number of amino acid substitutions per site per unit of time. Moreover, the authors write in the Introduction "a divergence limit does not imply that the rate of amino acid substitutions slows down in evolution," thus contradicting the Abstract. The Abstract should be edited and the misleading sentence corrected. From the context of the paper is seems like by "divergence rate" the author mean the rate of decrease in pairwise sequence identity with time. This definition poses additional question. This "divergence rate" will always decrease due to multiple and back substitutions and it is trivial. The authors need to make it clear that what they mean goes beyond a trivial curvilinear relationship between time and sequence identity.

6) Further on this, evolutionary rate is much more than simply a count of changes in the identity of the amino acids. To measure it properly one needs to rely on the phylogeny. Indeed, since the study is based on several clusters of orthologous proteins, why not do just that? For example, why not use the dN/dS formalism?

7) "billion years of evolution, we observed a significant decrease in mutual divergence rates," see item 5 above. Also, shouldn't "significant" be quantified is some way?

8) "Species' divergence times were used to estimate the times of divergence between corresponding orthologous proteins": How reliable is this time estimate?

9) Discussion "The presented results demonstrate that, in contrast to proteins with the same fold [Rost, 1997], the requirement to maintain the same molecular function significantly constrains the long-term divergence of protein orthologs": This difference is surprising. Maybe it has to do with how changes were estimated in the two studies? To state it with confidence direct comparison is needed, where the exact same methodology is used.

10) Finally, the manuscript should be edited for clarity by a professional scientific editor.

Separate reviews (please respond to each point):

Reviewer #1:

Summary of paper:

The manuscript analyzes clusters of orthologue enzymes of the same function, defined as sharing the same 4-digits EC number, to examine the limitation of function preservation on evolutionary divergence. The results seem to indicate that function confines divergence, which is anticipated- perhaps also shown before. The potential novelty here is the time dependence of the process. The data shows (to the best of my understanding) that proteins diverse from each other rapidly during the first ~1.5 billion years, but saturate after that. The data further suggests (again, assuming that I understood correctly) that the rapid evolutionary phase mostly reflects random drift, i.e., amino acid sites that can freely mutate, and that the saturation value reflects their relative fraction of the entire enzyme sequence.

Opinion: The manuscript could be important but it should be revised significantly to clarify what exactly was computed and why, what was measured and why, and how the results are related to previous studies. I also believe the manuscript should be edited for clarity by a professional scientific editor.

Major issues:

1) Results "In the first model, all protein sites have equal and independent substitution rates; see Equation 1": Equation 1 obviously represents an unrealistic evolutionary model because it is well known that the evolutionary rates are not equal at all amino acid sites. For example, catalytic residues hardly change.

2) Where does Equation 2 come from? It also doesn't look particularly realistic.

3) Equation 3 is the commonly used evolutionary model I think. So why not start with it?

4) "Species' divergence times were used to estimate the times of divergence

between corresponding orthologous proteins": How reliable is this time estimate?

5) Figure 2: How is "fitness cost" defined?

6) "phylogenetically independent pairs of species": What does it mean and how is "independent" defined? Is the pair A-B in Figure 3A phylogenetically independent? And the pair D-H?

7) "Notably, the probability that a protein site is identical, and thus contributes to the divergence limit, first increases linearly with increasing fitness effects at the site, and then begins to saturate for sites with high (>30%) fitness effects (Figure 3B)." This is perhaps true for FolA but I do not see saturation for InfA.

8) The distributions of the probability of identical sites in FolA and InfA (Figures 4A and B) are very different, but they are discussed together without reference to the difference.

9) Discussion "The presented results demonstrate that, in contrast to proteins with the same fold [Rost, 1997], the requirement to maintain the same molecular function significantly constrains the long-term divergence of protein orthologs": I am surprised about this difference. Maybe it has to do with how changes were estimated in the two studies? To state it with confidence I would have liked to see direct comparison where the exact same methodology is used.

10) Evolutionary rate is much more than simply a count of changes in the identity of the amino acids. To measure it properly one needs to rely on the phylogeny. Indeed, since the study is based on several clusters of orthologous proteins, why not do just that?

Reviewer #2:

This study poses the question about the extent to which function constrains sequence divergence. The answer given is that for orthologous enzymes 25% sequence identity is the approximate limit. The major critique, is that the authors did not make an attempt to provide a clear mechanistic explanation for such phenomenon. Is it simply because a significant fraction of positions is invariant? Is it because there are various constraints on various sites? Is it because only a small subsets of amino acids are tolerated at some sites? Why not take several enzyme families with very thick alignments and analyze them position-by-position to shed light on this question? Without such deep analysis, the paper, while interesting in its general idea, reads superficial and underdeveloped, despite some experimental results.

1) I suggest replacing the word "protein" with "enzyme" in the title. "We focused on enzymes because their molecular function is usually well defined," doesn't sound quite true. Reading the manuscript, it seems that the goal of this work is to investigate divergence of enzymes. I am positive that the divergence of non-enzymes will follow a different pattern and will generally be much lower than 25% identity. If the authors want to generalize to non-enzymes, they need to perform appropriate analyses. Currently, only one experiment is dedicated to a non-enzyme. It is not fair to the readers to generalize beyond the scope of analysis that was carried out.

2) I think that the sentence in the Abstract "divergence rates of orthologous enzymes decrease substantially after ~1-2 billion years of independent evolution" is confusing. "Rate" usually means number of amino acid substitutions per site per unit of time. Moreover, the authors write in the Introduction "a divergence limit does not imply that the rate of amino acid substitutions slows down in evolution," thus contradicting the Abstract. I suggest to edit the Abstract and correct the misleading sentence. From the context of the paper is seems like by "divergence rate" the author mean the rate of decrease in pairwise sequence identity with time. This definition poses additional question. This "divergence rate" will always decrease due to multiple and back substitutions and it is trivial. The authors need to make it clear that what they mean goes beyond a +trivial curvilinear relationship between time and sequence identity.

3) "billion years of evolution, we observed a significant decrease in mutual divergence rates," see item 2 above. Also, shouldn't "significant" be quantified is some way?

4) It was not made clear why these experiments were performed and how they integrate with the rest of the study. Addition of these experiments seems preliminary and no confident conclusions follow. Was the sole purpose of the experiment to bin positions by their fitness effects? If so, what new insight is gained from slower divergence of sites with more profound fitness effects compared to faster divergence of sites that are more tolerant to substitutions in experiments. Isn't this effect expected? Maybe quantification of the effect may have some novelty, but such quantification has not been done.

Reviewer #3:

In this paper the authors aim to assess how does the requirement of conserved function (i.e. orthology) constraints sequence evolution. The author premise their study on the assertion made by Rost in 1997 review that proteins of the same fold can diverge up to random sequence ID of 3-5% i.e. that structural similarity does not impose constraint on sequence ID. As a consequence the authors attribute in their analysis all sequence identity constraints to functional similarity. To that end they analyze sequence divergence of orthologs using phylogenetic time of species divergence as natural time scale "clock". They observed saturating time dependencies of sequence divergence with time and conclude that the rate of sequence divergence decreases with decreasing divergence time. Further, they carried out a high throughput mutational experiment on fitness effects of substitutions in 2 genes – folA and InfA – in E. coli and find, perhaps unsurprisingly, that sites where mutational effects on fitness are stronger are less constrained in evolution.

While the paper contains some interesting bioinformatics observations and analysis I have serious concerns about its premise and interpretation of the results. Apparently some issues stem from author's apparent gaps in knowledge of modern literature on biophysical determinants of protein evolution.

1) The premise that structural similarity does not constraint sequence identity is highly problematic. While anecdotally one can find two proteins of similar fold with very small sequence ID typically proteins with similar structure (not necessarily orthologues) have sequence ID at or above 25% – this is the essence of the famous cusp in sequence-structure relationship first reported by Lesk and Chothia in the eighties. In fact a careful analysis of structural/stability constraints on sequence divergence has been published in recent paper (Biophys J v.112, p.1350-65 (2017) where it was shown that in divergent evolution scenario protein structure is maintained up to 25-30% sequence ID and quickly deteriorates beyond that. Incidentally it is very close to 25% ID which the authors claim to stem from functional constraints Furthermore, the above mentioned BJ paper presents a detailed analytical estimate of sequence divergence dynamics akin to exponential fits used in this PAPER. The authors should make themselves familiar with this theory and use it to for their divergence curves rather ad hoc exponential fits.

2) The high throughput experimental data is potentially interesting but its description is so cryptic and incomplete that it is very hard to assess what actually has been done there. In particular there is no assessment of noise in deep sequencing to assess fitness., of the effects of synonymous substitutions etc. How is the data binned and why binning? The use of LB as a medium for the folA experiment is unfortunate because in LB DHFR is much less essential than in minimal media and therefore the results could be skewed by very permissive conditions. In addition the standing genetic variation is not taken into account – fitness effects could be a result of hitchhiking (i.e. originate from the variation of the background into which the mutations are introduced).These concerns aside, it is not entirely clear what does comparison with experiment tell us beyond the obvious that sites where deleterious fitness effects are greatest evolve more slowly. The obvious thing to do is to compare their alleged fitness effects with dN/dS assessment of the rates but that has not been done.

3) The interpretation of the experimental fitness effects in terms of function is also questionable. The authors are apparently unaware of series of experimental works from Shakhnovich lab where determinants of fitness effects of mutations are addressed. In particular it has been shown using both point mutations and orthologous chromosomal replacements for folA gene (PLOS Genetics 2015 DOI:10.1371/journal.pgen.1005612) and adk gene (Nature Ecology Evolution, 2017 http://dx.doi.org/10.1038/s41559-017-0149) that fitness is determined by product of folded protein abundance A and activity kcat/KM. Mutations may affect stability and through that parameter A (by changing the balance between protein production and degradation, see Mol Cell v.49, pp133-44 (2013). Therefore interpretation of the experimental trends entirely in functional terms is not warranted.

A minor comment: The concept and metaphor of expanding protein universe has been introduced 10 years before Kondrashov's work in the paper "Expanding protein universe and its origin from biological big bang" PNAS 2002, v.99 pp. 14132-6.

[Editors' note: further revisions were suggested before publication, as described below.]

Thank you for resubmitting your work entitled "Molecular function limits divergent protein evolution on planetary timescales" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz as the Senior Editor, a Reviewing Editor, and two reviewers.

As you can see from the reports below, the reviewers appreciated the revisions. However, there are still major outstanding issues. While some of these can be resolved by changes in the presentation, others are fundamental. We would strongly encourage you to address all of these prior to publication.

Reviewer #2:

I find that the authors did a thorough revision of the manuscript. At least now I think I understood the main conclusion of the paper. In enzymes and other proteins with very strong functional conservation, the number of different amino acids acceptable at a position is about 4. It is not because many sites are invariant and some are variable (not a dirty trick of average temperature in a hospital), but because most sites (except the invariant ones) are constrained to use a library of 3 to 5 different amino acids, not more than that. If this is not the bottom line, then the authors need to do better job at crystallizing their main claim and result.

If it is, I think it is a meaningful finding that could be explained better to the readers. I guess the second claim is that 3-5 amino acid limit is universal to all enzymes and (conserved!) non-enzymes. I do doubt (as in the original review) the validity of such a strong claim, which could be a result of the authors' bias in selecting families for their analysis. At least for non-enzymes, they selected most conserved proteins (like ribosomal proteins), so of course such selection is biased to get proteins that saturate easily in evolution. The authors try to justify this biased selection suggesting that it is difficult to find orthologs. But that statement by itself totally discredits this study. Why? Because if you cannot find your orthologs, wouldn't it mean that they already diverged beyond (lower than) your claimed 25% identity as the universal limit, and the author's conclusions do not apply to such families? Maybe for the enzymes too, the 25% limit is simply a reflection of the search methods the authors used to find orthologs, that fail to find more distant ones.

To improve the presentation and make this paper quite interesting (well, reviewers are not supposed to direct the study, but the authors seem passionate about their work and also seem rather inexperienced in both logical thinking and putting a paper together, so maybe this recommendation could be helpful), I would suggest to base it on two plots.

1) Between-protein variability.

The first plot is the histogram of the average estimated number of amino acids allowable per site (without invariant sites, or with) for enzyme families and other protein families. Well, the authors would have to try harder to find orthologs for proteins that manage to diverge below 25%, even my rotation students can do that. This histogram would be expected to have a maximum around 3 to 5, and for some variable proteins it could be around 10 or 15? Right? Then protein families with very low and very high numbers could be discussed with an attempt to give explanations about their uniqueness.

2) Within-protein variability.

The second plot is the histogram of estimated number of amino acids allowable per site within a protein family. The authors could either normalize to the average per protein, or select a bin with the maximum count from previous plot (let's say 4). These histograms can be averaged for all families with mean and SD showing for each bin. I would assume there will be a large count for invariant sites for enzymes (at 1), counts for 2 amino acids used, 3, 4, etc. Will this histogram have a single mode? Maybe around 4? Several modes? Will there be sites using more than 10 amino acids? How are these distributed in spatial structure and relative to the active site? Discussion of these details could be quite insightful and interesting.

If these authors do not wish to make these plots, since this review will be published, maybe someone else will, and we will learn something interesting as a result.

Currently, there are so many plots in this paper and many of them are not particularly helpful to get the point across quickly. Also I still find the usage of non-standard terms (like divergence rate) confusing, not necessary, and not insightful about the mechanism. Yes, the terms are defined, but they are just masking the reality, which is simpler: constrained usage of amino acids in positions of enzyme molecules. Not all 20, not even 10, but 4! Why not state and illustrate this clearly? Don't you agree that the impact of the paper will increase because it will be easier to understand?

The Abstract is still very poor and misleading. For instance, the statement "The effective divergence limit (>25% sequence identity) is not primarily due to multiple substitutions at the same sites" is completely wrong. According to the authors' explanations, this "effective divergence limit" is exactly due to multiple substitutions at the same site! If you have only 4 amino acids acceptable at a site, due to multiple substitutions sequence identity will saturate are 25%. Like in DNA. Why not write a precise and clear Abstract about what this work presents? Due to so many logical flaws in the authors' thinking and presentation (as illustrated above), I would be scared to publish this paper without a careful read. One statement at a time. And trying to figure out why the statement is wrong. If clearly not wrong, then move on to the next one.

And, finally, why not compare your results with this paper more thoroughly PMID: 27138088? Isn't it a bit similar? I guess I don't understand the meaning behind "to investigate the temporal patterns of the long-term divergence."

Do the authors still claim that the sites are saturated at the usage of 3 to 5 amino acids because the time passed was not sufficient to gain more changes? Or the time was enough and protein of the same function simply cannot tolerate additional amino acids well and still keep the function? Which one is right? I got an impression it was the latter. And then what I said at the beginning of this review holds. If it is the former, it needs to be convincingly justified.

If the authors disagree with my review, then I did not understand the paper, which is possible, and still suggests that the authors need to improve the presentation.

Reviewer #3:

This version of the manuscript is a significant improvement over the previous version in terms of added details (e.g. experimental procedure of folA mutagenesis re now described in sufficient detail to be understandable and/or potentially reproducible).

The authors attempted to address my (and other reviewers) main concern by presenting the analysis in new Figure 5 that shows that full orthologues (all EC numbers coincide) are more sequence-constrained than partial orthologues (3 EC numbers coincide). However this analysis fails to control for different structural divergence between full and partial orthologues.

Therefore, the most problematic aspect of the analysis – that authors attribute observed sequence conservation in diverging clades to conservation of function between orthologues has not been fully addressed. A clear alternative explanation that such conservation is explained by maintenance of structure and stability regardless of function still stands.

The authors used a truism by pointing out that proteins of the same FOLD (i.e. topologically similar arrangement of elements of secondary structure) can diverge to 10% or less sequence ID again citing an old work with data collected on very limited number of structures available at that time.

However, their full functional orthologues are much more similar structurally than proteins sharing the same fold. The correct control which was suggested in my initial review has not been done satisfactorily. Specifically, the authors should compare their sets of proteins with sets that have similar degree of structural similarity (measured as distribution of TM-scores) but different function. There are such examples where structures are quite similar (TM-score-wise) but functions differ significantly. Good examples of that kind ate TIM-barrels which are almost exclusively enzymes with wide variety of specificity and Igfold proteins again with very conserved structures but broadly diverged functional annotations.

If the authors find that conservation of structure in functionally divergent proteins imposes less sequence divergence constraints than same degree of structural conservation in orthologues – that will be a clear demonstration of additional constraints imposed by functional conservation which is the main message of this work. In the absence of such analysis the current data does not justify the conclusion.

Minor point: The authors severely misquote Firnberg et al., 2016. They say: "Nevertheless, direct and comprehensive biochemical experiments demonstrated that the deleterious effects of protein mutations primarily result from changes in specific protein activity rather than decreases in protein stability and cellular abundance [Firnberg et al., 2016]". In fact, the authors of Firnberg et al., 2016, say directly the opposite: '… These DFEs provide insight into the inherent benefits of the genetic code's architecture, support for the hypothesis that mRNA stability dictates codon usage at the beginning of genes, an extensive framework for understanding protein mutational tolerance, and evidence that mutational effects on protein thermodynamic stability shape the DFE..…" (cited from the Abstract of Firnberg et al., 2016). The authors misrepresent the main result of Firnberg et al., 2016: According to Figure 5B of Firnberg et al., 2016, the product of abundance and catalytic activity shapes fitness effects in TEM1, not abundance alone. This is exactly what is established in Bershtein et al., 2015 and Adkar et al., 2017, and shows that abundance (which is a function of stability) enters fitness landscape on equal footing with catalytic activity, i.e. there is as much selection for abundance (i.e. stability) as it is for kcat/KM and related measures of activity. This misinterpretation somewhat undermines the major premise of the present paper that there is separate selection for activity/function and stability/structure. In reality one cannot disentangle the two because fitness landscape depends on the function (i.e. the product) of the two factors.
