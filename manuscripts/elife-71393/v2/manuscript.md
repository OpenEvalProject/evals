# Binding affinity landscapes constrain the evolution of broadly neutralizing anti-influenza antibodies

## Authors

- Angela M Phillips<sup>1</sup> ([ORCID: 0000-0002-9806-7574](https://orcid.org/0000-0002-9806-7574))
- Katherine R Lawrence<sup>1</sup>
- Alief Moulana<sup>1</sup>
- Thomas Dupic<sup>1</sup>
- Jeffrey Chang<sup>5</sup>
- Milo S Johnson<sup>1</sup> ([ORCID: 0000-0003-0169-2494](https://orcid.org/0000-0003-0169-2494))
- Ivana Cvijovic<sup>6</sup> ([ORCID: 0000-0002-6272-2979](https://orcid.org/0000-0002-6272-2979))
- Thierry Mora<sup>7</sup> ([ORCID: 0000-0002-5456-9361](https://orcid.org/0000-0002-5456-9361))
- Aleksandra M Walczak<sup>7</sup> ([ORCID: 0000-0002-2686-5702](https://orcid.org/0000-0002-2686-5702))
- Michael M Desai<sup>1</sup> ([ORCID: 0000-0002-9581-1150](https://orcid.org/0000-0002-9581-1150)) †

### Affiliations

1. Department of Organismic and Evolutionary Biology, Harvard University Cambridge United States
2. NSF-Simons Center for Mathematical and Statistical Analysis of Biology, Harvard University Cambridge United States
3. Quantitative Biology Initiative, Harvard University Cambridge United States
4. Department of Physics, Massachusetts Institute of Technology Cambridge United States
5. Department of Physics, Harvard University Cambridge United States
6. Department of Applied Physics, Stanford University Stanford United States
7. Laboratoire de physique de ÍÉcole Normale Supérieure, CNRS, PSL University, Sorbonne Université, and Université de Paris Paris France

† Corresponding author

## Abstract

Over the past two decades, several broadly neutralizing antibodies (bnAbs) that confer protection against diverse influenza strains have been isolated. Structural and biochemical characterization of these bnAbs has provided molecular insight into how they bind distinct antigens. However, our understanding of the evolutionary pathways leading to bnAbs, and thus how best to elicit them, remains limited. Here, we measure equilibrium dissociation constants of combinatorially complete mutational libraries for two naturally isolated influenza bnAbs (CR9114, 16 heavy-chain mutations; CR6261, 11 heavy-chain mutations), reconstructing all possible evolutionary intermediates back to the unmutated germline sequences. We find that these two libraries exhibit strikingly different patterns of breadth: while many variants of CR6261 display moderate affinity to diverse antigens, those of CR9114 display appreciable affinity only in specific, nested combinations. By examining the extensive pairwise and higher order epistasis between mutations, we find key sites with strong synergistic interactions that are highly similar across antigens for CR6261 and different for CR9114. Together, these features of the binding affinity landscapes strongly favor sequential acquisition of affinity to diverse antigens for CR9114, while the acquisition of breadth to more similar antigens for CR6261 is less constrained. These results, if generalizable to other bnAbs, may explain the molecular basis for the widespread observation that sequential exposure favors greater breadth, and such mechanistic insight will be essential for predicting and eliciting broadly protective immune responses.

## Introduction

Vaccination harnesses the adaptive immune system, which responds to new pathogens by mutating antibody-encoding genes and selecting for variants that bind the pathogen of interest. However, influenza remains a challenging target for immunization: most antibodies elicited by vaccines provide protection against only a subset of strains, largely due to the rapid evolution of the influenza surface protein hemagglutinin (HA) (Wiley et al., 1981; Smith et al., 2004). After nearly two decades of studies, numerous broadly neutralizing antibodies (bnAbs) have been isolated from humans, with varying degrees of cross-protection against diverse strains (Corti et al., 2017; Throsby et al., 2008; Dreyfus et al., 2012; Corti et al., 2011; Schmidt et al., 2015). Still, we do not fully understand many factors affecting how and when bnAbs are produced. In particular, affinity is acquired through a complex process of mutation and selection (Victora and Nussenzweig, 2012), but the effects of mutations on binding affinity to diverse antigens are not well characterized.

For example, consider two well-studied influenza bnAbs that display varying levels of breadth: CR9114 is one of the broadest anti-influenza antibodies ever found, neutralizing strains from both groups of influenza A and strains from influenza B, while CR6261 is limited to neutralizing strains from Group 1 of influenza A (Throsby et al., 2008; Dreyfus et al., 2012; Ekiert et al., 2009; Lingwood et al., 2012). Both antibodies were isolated from vaccinated donors, derive from very similar germline sequences (IGHV1 –69 and IGHJ6), and bind the conserved HA stem epitope (Figure 1—figure supplement 3; Throsby et al., 2008; Dreyfus et al., 2012; Ekiert et al., 2009). Each antibody heavy chain has many mutations (18 amino acid changes for CR9114, 14 for CR6261, Figure 1A), including seven positions that are mutated in both, yet the contributions of these mutations to affinity against different antigens remain unclear (Dreyfus et al., 2012; Avnir et al., 2014).

![Figure 1.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-v2.jpg)

**Figure 1.:** (A) Sequence alignment comparing somatic heavy chains to reconstructed germline sequences. Mutations under study (purple, numbered) and excluded mutations (black) are indicated; residues are numbered by IMGT unique numbering. (B) Influenza hemagglutinin phylogenetic tree with selected antigens and breadth of CR9114 (black box) and CR6261 (gray box) indicated. (C, E), Scatterplots of the (C) CR9114 library binding affinities against three antigens, with 2D planes shown below, and (E) CR6261 library binding affinities against two antigens. (D, F) Distributions of library binding affinities for (D) CR9114 and (F) CR6261 for each antigen (gray histogram, right) separated by number of somatic mutations (boxplots, left). Numbers and percentages of variants with measurable binding are indicated at right. (G), Force-directed graph of CR9114 H1 –logKD. Each variant (node) is connected to its 16 single-mutation neighbors (edges not shown for clarity); edges are weighted such that variants with similar genotypes and –logKD tend to cluster. Nodes are colored by binding affinity to H1 (top; showing all 65,091 nodes), H3 (lower left inset; showing only the region containing nodes with –logKD > 6), and Flu B (lower right inset; showing only the region containing nodes with –logKD > 6).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Experimental design and Tite-Seq workflow. (A) Experimental design. Amino acid sequence percent identity of the entire HA ectodomain and the stem epitope (Dreyfus et al., 2012) are shown between each pair of antigens tested for both antibodies. (B) Tite-Seq assay. Surface display single-chain variable fragment (scFv) libraries are transformed into yeast and labeled with fluorescent antigen, followed by FACS into bins and sequencing. Dissociation constants are inferred from changes in mean bin fluorescence across 12 antigen concentrations, see Materials and methods.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A, C) Correlation of (A) CR9114 and (C) CR6261 KD measurements between biological replicates. (B, D) Validation of (B) CR9114 and (D) CR6261 Tite-Seq KD measurements by isogenic flow cytometry measurements for a subset of variants and antigens.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Alignment of co-crystal structure of CR9114 with H5 (light hues; PDB ID 4FQI) and CR9114 with H3 (dark hues; PDB ID 4FQY). Mutated residues shown as gray spheres. (B) Co-crystal structure of CR6261 with H1 (PDB ID 3GBN); mutated residues shown as gray spheres.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Force-directed graph for CR6261. (A, B) Force-directed graph for CR6261 H1 –logKD, as in Figure 1G. Nodes are colored by binding affinity to (A) H1 and (B) H9.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Correlation of mean expression across Tite-Seq biological replicates for CR9114 library (left, red) and CR6261 library (right, blue). (B) Correlation between Tite-Seq mean expression and isogenic expression fluorescence for select CR9114 (left, red) and CR6261 (right, blue) variants. (C) Change in expression upon mutation for a given number of background somatic mutations. (D) Correlation between mean expression and –logKD. Average values across biological replicates (N logKD = 3) are plotted. (E) Change in expression upon mutation at a specific site. Violin plots (left) and residues in co-crystal structure (right) are colored by mean change in expression for each site. Asterisks above violins indicate p-values for two-sided t-test between the distribution means and zero ($p<0.01$ (*), < 0.001 (**), < 0.0001 (***); $N_{9114}=32,768$, $N_{6261}=1,024$). (F) Correlation between mean change in expression and mean change in –logKD (summed across all antigens) by mutation position. Select mutations with large impacts on expression and –logKD are labeled; all points are colored by mean change in expression, as in (F). Dark gray line indicates best-fit linear regression (95% confidence intervals in light gray).

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** First, single yeast cells were gated by forward scatter (FSC) and side scatter (SSC) (step 1). Single cells were then either gated by scFv expression or HA binding. For the expression sort (step 2B), single cells were gated into eight bins along the log(FITC-A) axis, each containing 12.5% of the population. For the binding sort (steps 2A and 3A), scFv-expressing (scFv+) single cells were sorted into four bins along the log(PE-A) axis, with bin one comprising all HA- cells, and bins 2–4 each comprising 33% of the HA+ population.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** (A) Reversion of A24S and E46D in CR9114 (somatic-16) does not substantially impact binding affinity compared to the fully somatic version of CR9114 (somatic-18) to either H1 (orange) or H3 (turquoise); these mutations are thus excluded from the CR9114 library. (B) Reversion of Q6E, L50P, and V101M in CR6261 (somatic-11) does not substantially impact binding affinity compared to the fully somatic version of CR6261 (somatic-14) to either H1 (orange) or H9 (purple); these mutations are thus excluded from the CR6261 library. Measurements made in biological duplicate; mean +/- standard error shown.

Beyond single mutational effects, it remains unknown whether there are correlated effects or strong trade-offs between binding to different antigens (pleiotropy), or non-additive interactions between mutations (epistasis). Such epistatic and pleiotropic effects can constrain the mutational pathways accessible under selection, as has been observed for other proteins (Weinreich et al., 2006; Starr et al., 2017; Ortlund et al., 2007; Podgornaia and Laub, 2015; Gong et al., 2013; Sailer and Harms, 2017b; Miton and Tokuriki, 2016; Poelwijk et al., 2019; Bank et al., 2015). Epistasis in antibody-antigen interactions remains significantly understudied (Adams et al., 2019; Pappas et al., 2014; Braden et al., 1998) and most deep mutational scanning studies have focused on antigens (Doud et al., 2018; Wu et al., 2020; Starr et al., 2021). In contrast to typical protein evolution, antibody affinity maturation proceeds by discrete rounds of mutation and selection (Victora and Nussenzweig, 2012), typically with more than one nucleotide mutation occurring between selective rounds (Unniraman and Schatz, 2007). In addition, antibodies are inherently mutationally tolerant (Braden et al., 1998; Chen et al., 1999; Burks et al., 1997; Corti and Lanzavecchia, 2013; Klein et al., 2013), generating opportunities for interactions that scale combinatorially. Thus, if epistatic and pleiotropic constraints exist for antibodies, they could affect the likelihood of producing bnAbs under different antigen selection regimes (Pappas et al., 2014) and may account for the low frequencies of bnAbs in natural repertoires (Corti et al., 2017). Characterizing the prevalence of these constraints on bnAb evolution may provide valuable insight for improving vaccination strategies (Yewdell, 2013; Henry et al., 2018).

To date, studies of antibody binding have been limited to small numbers of individual sequences, deep mutational scans of single mutations, and mutagenesis of small regions (Pappas et al., 2014; Braden et al., 1998; Burks et al., 1997; Adams et al., 2016; Koenig et al., 2017; Forsyth et al., 2013; Wu et al., 2017; Xu et al., 2015; Madan et al., 2021; Schmidt et al., 2015), due in part to practical constraints on library scale and the throughput of affinity assays. This has limited our ability to comprehensively characterize binding landscapes for naturally isolated bnAbs, which often involve many mutations spanning framework (FW) and complementarity-determining regions (CDR) (Corti et al., 2017; Corti and Lanzavecchia, 2013; Klein et al., 2013).

We overcome these challenges by generating combinatorially complete libraries of up to ∼105 antibody sequences and assaying their binding affinities in a high-throughput yeast-display system (Adams et al., 2016). This approach enables us to infer the contributions of individual mutations as well as hundreds of pairwise and higher order interactions between mutations, revealing that these interactions can restrict evolutionary pathways leading to greater breadth. In particular, we find that mutational effects on binding affinity to diverse antigens display a nested structure, where increasingly large groups of specific mutations are required to gain affinity to divergent antigens, resulting in highly constrained paths to broad affinity. This pattern is not observed for more similar antigens, where many mutational paths to broad affinity are accessible. Further, these nested patterns of mutational effects provide new molecular insight into why sequential exposure to diverse antigens often favors greater breadth (Wang et al., 2010; Krammer et al., 2012; Wang et al., 2015; Wang, 2017; Sachdeva et al., 2020; Molari et al., 2020; Sprenger et al., 2020). Together, this work provides the first comprehensive characterization of antibody affinity landscapes and advances our understanding of the molecular constraints on bnAb evolution.

## Results

### Binding affinity landscapes of CR9114 and CR6261

Here, we characterize the binding affinity landscapes of the two well-studied bnAbs noted above: CR9114 and CR6261. Specifically, we made all combinations of a set of mutations separating the germline and somatic sequences for CR9114 (16 mutations totaling 65,536 variants) and CR6261 (11 mutations totaling 2048 variants). These libraries include all heavy-chain mutations in these antibodies, except a few select mutations distant from the paratope (Figure 1, Figure 1—figure supplement 7, and see Materials and methods). Both antibodies engage antigens solely through their heavy-chain regions (Dreyfus et al., 2012; Ekiert et al., 2009), and thus are well-suited for yeast display as single-chain variable fragments (see Materials and methods) (Boder and Wittrup, 1997).

We use the Tite-Seq method (Adams et al., 2016), which integrates flow cytometry and sequencing (Figure 1—figure supplement 1), to assay equilibrium binding affinities of each scFv sequence in these libraries against select antigens that span the breadth of binding for each antibody (Figure 1B). For CR6261, we chose two divergent group 1 HA subtypes (H1 and H9; see Figure 1—figure supplement 1), while for CR9114, we chose the three highly divergent subtypes present in the vaccine (H1 from group 1, H3 from group 2, and influenza B; see Figure 1—figure supplement 1, Throsby et al., 2008). Inferred affinities outside our titration boundaries (10−11–10−6 M for H3 and influenza B, 10−12–10−7 M for H1 and H9) are pinned to the boundary, as deviations beyond these boundaries are likely not physiologically relevant (Batista and Neuberger, 1998). Antibody expression is not strongly impacted by sequence identity, although some mutations have modest effects that may be inversely correlated with their effect on affinity (Figure 1—figure supplement 5). Affinities obtained by Tite-Seq are reproducible across biological triplicates (Figure 1—figure supplement 2; average standard error of 0.047 -logKD units across antibody-antigen pairs) and are highly accurate as verified for select variants by isogenic flow cytometry (Figure 1—figure supplement 2) and by solution-based affinity measurements made by others (Throsby et al., 2008; Dreyfus et al., 2012; Lingwood et al., 2012; Pappas et al., 2014).

We begin by examining the distribution of binding affinities across antigens for each antibody library (Figure 1). We observe that most CR9114 variants have measurable affinity to H1 (97%), fewer to H3 (11%), and still fewer to influenza B (0.3%) (Figure 1C,D). For H1, only a few mutations are needed to improve from the germline affinity. In contrast, variants are not able to bind H3 unless they have several more mutations, and many more for influenza B. This hierarchical structure is in striking contrast to the CR6261 library, in which most variants can bind both antigens (92% for H1, 81% for H9), variants have a similar KD distribution, and many variants display intermediate affinity to both antigens (Figure 1E,F). To visualize how genotypes give rise to the hierarchical structure of CR9114 binding affinities, we represent the binding affinities for H1 as a force-directed graph. Here, each variant is a node connected to its 16 single-mutation neighbors, with edge weights inversely proportional to the change in H1 binding affinity, such that variants with similar genotype and KD tend to form clusters (Figure 1G, Figure 1—figure supplement 4). Coloring this genotype-to-phenotype map by the –logKD to each of the three antigens, we see that sequences that bind H3 and influenza B are highly localized and overlapping, meaning that they share specific mutations. Thus, while many CR9114 variants strongly bind H1, only a specific subset bind multiple antigens.

### Mutational effects on binding to diverse antigens

To dissect how mutations drive the structure of these binding landscapes, we next infer specific mutational effects. We first log-transform binding affinities such that they are proportional to free energy changes ($Δ⁢G_{binding}$), which should combine additively under the natural null expectation (Wells, 1990; Olson et al., 2014). We then define a linear model with single mutational effects and interaction terms up to a specified order (defined relative to the unmutated germline sequence, see Appendix 2 for alternatives), and fit coefficients by ordinary least squares regression. We use cross-validation to identify the maximal order of interaction for each antigen and report coefficients at each order from these best-fitting models (CR9114: fifth order for H1, fourth for H3, first for influenza B; CR6261: fourth order for H1 and H9; see Materials and methods). We note that the maximum order of interactions is affected by our inference power, particularly by the number of sequences with appreciable binding, and so we interpret these models as showing strong evidence of epistasis at least up to the order indicated. We explored the possibility of ‘global’ epistasis by inferring a nonlinear transformation of the -logKD values (Sailer and Harms, 2017a; Otwinowski et al., 2018), but found that this approach did not significantly reduce the order or number of specific interaction coefficients needed to explain the data (see Appendix 2). We also explored inferring epistasis up to full order using Walsh-Hadamard transformations; results are qualitatively similar but less conservative than cross-validated regression (see Appendix 2).

Examining the effect of individual mutations on the germline background (Figure 2A,B), we observe several mutations that enhance binding to all antigens (e.g. S83F for CR9114), and mutations that confer trade-offs for binding distinct antigens (e.g. F30S in CR9114 reduces affinity for H1 but enhances affinity for influenza B). Generally, large-effect mutations are at sites that contact HA (Figure 2C, Figure 2—figure supplement 1, Dreyfus et al., 2012; Ekiert et al., 2009). Consistent with prior biochemical and structural work, mutations essential for CR9114 breadth are spread throughout FW3 and the CDRs, forming hydrophobic contacts and hydrogen bonds with residues in the conserved HA stem epitope (Dreyfus et al., 2012; Avnir et al., 2014). We observe three specific mutations that are required for binding to H3 (present at over 90% frequency in the set of binding sequences), likely because they form hydrophobic contacts with HA (K82I and S83F) and reorient the CDR2 loop (I57S), which interacts with residues and a glycan in H3 that are distinct from those in H1 (Dreyfus et al., 2012). We also observe eight specific mutations that are required for binding to influenza B. Many of these breadth-conferring mutations are absent in CR6261, particularly those in CDR2 (Dreyfus et al., 2012; Ekiert et al., 2009). Notably, these sets of required mutations in CR9114 exhibit a nested structure: mutations beneficial for H1 are required for H3, and mutations required for H3 are required for influenza B, giving rise to the hierarchical structure of the binding landscape (Figure 1C).

![Figure 2.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig2-v2.jpg)

**Figure 2.:** (A, B) First-order effects inferred in best-fitting epistatic interaction models for (A) CR9114 and (B) CR6261. Mutations required for binding (present at over 90% frequency in binding sequences) have effect sizes denoted as ‘R’ and are removed from inference. Error bars indicate standard error. (C) First order effects for each site plotted against the contact surface area between the corresponding somatic residue and HA (left, CR9114; right, CR6261). Sites with notable contact area or effect size are labeled. Cocrystal structures are also shown; mutations are colored by first-order effect size. (D) Significant second-order epistatic interaction coefficients for CR9114 mutations (bottom left, H3; top right, H1). Interactions involving required mutations are shown in dark red. (E) Significant second-order coefficients for CR6261 mutations (bottom left, H9; top right, H1). Significance in (D), (E) indicates Bonferroni-corrected p-value < 0.05, see Materials and methods. (F) Second-order coefficients for H1 –logKD plotted against the distance between the respective $\alpha$-carbons in the crystal structures.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Left: first-order effects for each site, colored by effect size and plotted against the contact surface area between the corresponding somatic residue and HA (top, CR9114 with H3; bottom, CR6261 with H9); Right: co-crystal structures with mutation sites colored by first-order effects, as in Figure 2C. (B) Second-order coefficients for CR9114 with H3 (top) and CR6261 with H9 (bottom) plotted against the distance between the respective $\alpha$-carbons in the crystal structures, as in Figure 2F.

Beyond these exceptionally synergistic interactions between required mutations, we find that epistasis is widespread, accounting for 18–33% of explained variance depending on the antibody-antigen pair (except influenza B, see Materials and methods, Appendix 2). Pairwise interactions are dominated by a few mutations (e.g. F30S for CR9114 and S35R for CR6261) that exhibit many interactions, both positive and negative, with other mutations (Figure 2D,E). Overall, mutations with strong pairwise interactions tend to be close in the crystal structure, although there are long-range pairwise interactions that are likely mediated by interactions with the antigen or conformational rearrangements (Figure 2F, Figure 2—figure supplement 1, Dreyfus et al., 2012; Ekiert et al., 2009; Avnir et al., 2014).

### High-order epistasis is dominated by a subset of mutations

Our dataset also allows us to resolve higher order epistasis. In addition to the required mutations, our models identify numerous strong third to fifth order interactions, with a subset of mutations participating in many mutual interactions at all orders. For CR9114 binding to H1, this subset consists of five mutations, distributed across three different regions of the heavy chain (Figure 3A,B). Some of these mutations likely generate (K82I, S83F) or abrogate (F30S) contacts to HA, and others (I57S, A65T) may indirectly impact HA binding by reorienting contact residues in CDR2 (Dreyfus et al., 2012; Avnir et al., 2014). Within this set of five residues, we first illustrate two examples of third-order epistasis by grouping sequences by their genotypes at these five sites (Figure 3C). Intriguingly, some mutations that are deleterious in the germline background ('–' annotations) are beneficial in doubly-mutated backgrounds ('+' annotations). For example, mutation F30S is significantly less deleterious in backgrounds with S83F than in the germline background, suggesting that new hydrophobic contacts in FW3 may be able to compensate for the potential loss of contacts in CDR1. Yet F30S unexpectedly becomes beneficial after an additional mutation I57S in CDR2, indicating more complex interactions between flexible CDR and FW loop regions (Figure 3B,C; Dreyfus et al., 2012).

![Figure 3.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig3-v2.jpg)

**Figure 3.:** (A) Total higher order epistatic contributions of CR9114 mutation pairs for binding H1. Color bar indicates the sum of absolute values of significant higher order interaction coefficients involving each pair of mutations; key epistatic residues indicated by arrows. Significance is given by Bonferroni-corrected p-value < 0.05, see Materials and methods. (B) Location of key epistatic residues in the CR9114 –HA co-crystal structure colored by region. (C) –logKD distributions for genotypes grouped by their identity at the five residues indicated in (A), (B), with means indicated as white dots ($N=8,192$ genotypes per violin). Annotations indicate notable deleterious ('−') and beneficial ('+') mutational effects. (D) CR9114 force-directed graph from Figure 1G, colored as in (C) by the genotype at the five sites indicated in (A), (B). Genotypes not shown in (C) are shown in light gray. Data are also available in an interactive data browser at https://yodabrowser.netlify.app/yoda_browser/. (E), Third-order interaction involving site 64 accounts for distinct clusters (teal) corresponding to genotypes with mutations 57 and 65 in (D). Colors correspond to mutation groups in (C), (D) ($N=4,096$ genotypes per violin). (F), Epistatic interaction coefficients among the five key sites from (A), (B). Colors for certain groups as in (C), (D); other groups denoted in gray, with notable terms labeled.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) CR9114 force-directed graph, as in Figure 3D, colored by mutation groups of sites 30, 57, 65, 82, and 83 (32 total groups). The dashed line emphasizes the observed separation of genotypes with S83F (upper right) from those without S83F (lower left). (B) Coefficients for terms in the epistatic interaction model corresponding to mutation groups of sites 30, 57, 65, 82, and 83 (31 total groups, excluding the germline), colored according to (A) and grouped by order. Error bars indicate standard error. (C) Distribution of the number of significant coefficients for mutation groups in every possible set of five sites chosen from the 16 sites (up to 31 terms for each group, for 4368 groups). Significance is given by Bonferroni-corrected p-value lt0.05, see Materials and methods. The value for the group illustrated in (A), (B) is indicated in red (26 significant terms, empirical p-value $<10^{-3}$).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) CR9114 force-directed graph, as in Figure 3D, but colored by mutation groups of a different set of five sites with fewer strong epistatic interactions (35, 36, 64, 66, and 85). (B) CR9114 force-directed graph, colored by mutation groups of a different set of five sites with no strong linear contributions or epistatic interactions (79, 84, 92, 95, and 103).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) Higher order significant epistatic contributions of CR9114 mutation pairs, as in Figure 3A, for binding H3. Light yellow columns indicate required mutations (sites 57, 82, and 83). Significance is given by Bonferroni-corrected p-value < 0.05, see Methods.

To see how these high-order interactions drive the overall structure of the binding affinity landscape, we return to the force-directed graph, now colored by genotype at these five key sites (Figure 3D; only points corresponding to genotypes shown in Figure 3C are colored). We see that these five sites largely determine the overall structure of the map: points of the same color tend to cluster together, despite varying in their genotypes at the other 11 sites. However, we observe that interactions with other mutations do exist, as evidenced by separate clusters with the same color (e.g. the two clusters in teal for 57,65 are distinguished by a positive third-order interaction with site 64, Figure 3E). These patterns are not confined to the genotypes shown in Figure 3C; if we color all 32 possible genotypes at the five key sites, we observe the same general patterns (Figure 3—figure supplement 1; an interactive data browser for exploring these patterns of epistasis in CR9114 is available at: https://yodabrowser.netlify.app/yoda_browser/). Interactions between these five sites are also enriched for significant epistatic coefficients ($p<10^{-3}$; 26 of 31 possible terms are significant, compared to an average of 4 terms among all sets of five sites, Figure 3—figure supplement 1), including the fifth order interaction between all five residues (Figure 3F). Remarkably, these five mutations underlie significant high-order epistasis for other antigens as well: all five are either required for binding or participate extensively in interactions for H3 and influenza B (Figure 3—figure supplement 3).

Higher order epistasis in CR6261 is similarly dominated by a subset of mutations in CDR1 and FW3, at identical or neighboring positions as some key sites for CR9114 (Figure 4A). These mutations exhibit strong diminishing returns epistasis at third and fourth order, counteracting their synergistic pairwise effects, in a similar manner across both antigens (Figure 4B, Figure 4—figure supplement 1, Figure 4—figure supplement 2). Many fourth-order combinations of these mutations display interaction coefficients of similar magnitude (Figure 4—figure supplement 1), though they may be signatures of even higher order interactions that we are underpowered to infer.

![Figure 4.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig4-v2.jpg)

**Figure 4.:** (A) Total significant epistatic contributions of CR6261 mutation pairs for binding H1, as in Figure 3A. Significance is given by Bonferroni-corrected p-value < 0.05, see Materials and methods. (B) Third-order interaction for CR6261 H1 binding between mutations T29P, S35R, and S83F ($N=256$ genotypes per violin).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) CR6261 force-directed graph, as in Figure 1—figure supplement 4, colored by mutation groups of sites 29, 35, 82, and 83 (16 total groups). (B) Top, coefficients for terms in the epistatic interaction model corresponding to the mutation groups illustrated in (a) (15 total groups, excluding the germline), colored according to (a) and grouped by order. Bottom, the largest fourth-order coefficients observed in the epistatic interaction model, with sites indicated. In both, error bars indicate standard error. (C) CR6261 force-directed graph, colored by a different set of four sites with the fewest strong linear effects and epistatic interactions (65, 66, 69, and 112.1).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Higher order significant epistatic contributions of CR6261 mutation pairs, as in Figure 4A, for binding H9. (B) Scatterplot of significant epistatic interaction model coefficients for binding to H1 and H9. Terms at different orders are colored and sized as indicated. Selected coefficients are annotated. Significance in (A), (B) is given by Bonferroni-corrected p-value < 0.05, see Methods.

A common approach to quantify how epistasis constrains mutational trajectories is to count ‘uphill’ paths (i.e. where affinity improves at every mutational step from the germline to the somatic sequence). We find that only a small fraction of potential paths are uphill (0.00005% +/- 0.00004% for CR9114 binding H1, and 0.2% +/- 0.04% for CR6261 binding H1, as estimated by bootstrap, see Materials and methods). However, we note that for all antibody-antigen combinations, the somatic sequence is not the global maximum of the landscape (the best-binding sequence) and some mutations have deleterious effects on average. Hence, strictly uphill paths are only possible due to sign epistasis, where normally deleterious mutations have beneficial effects in specific genetic backgrounds.

Overall, we see that mutational effects and interactions between them explain the affinity landscapes we observe. For CR9114, binding affinity to H1 can be achieved through different sets of few mutations with complex interactions. In contrast, a specific set of many mutations with strong synergistic interactions is required to bind H3, and to an even greater extent, influenza B (Figure 2A), giving rise to the landscape's hierarchical structure (Figure 1C). For CR6261, the higher order interactions are more similar between H1 and H9, which is consistent with the more correlated patterns of binding affinities between these two antigens (Figure 1E).

### Affinity to diverse antigens was likely acquired sequentially

The hierarchical nature of the CR9114 landscape suggests that this lineage developed affinity to each antigen sequentially. Considering the maximum –logKD achieved by sequences with a given number of mutations (a proxy for time), we see that improvements in H1 binding can be realized early on, whereas improvements in H3 binding are not possible until later, and even later for influenza B (Figure 5A). In fact, the nested structure of affinity-enhancing mutations forces improvements in binding affinity to occur sequentially. If selection pressures were also experienced in this sequence, mutations that improve binding to the current antigen would lead to the genotypes required to begin improving binding to the next. Indeed, we find that for CR9114, there are more uphill paths leading to the somatic sequence if selection acts first on binding to H1 and later to H3 and influenza B (Figure 5C). In contrast, for CR6261, improvements in binding can occur early on for both antigens (Figure 5B) and the number of uphill paths is more similar across single-antigen and sequential selection pressures (Figure 5D).

![Figure 5.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig5-v2.jpg)

**Figure 5.:** (A, B) Maximum binding affinity achievable for sequences with a given number of mutations. For each antigen for (A) CR9114 and (B) CR6261, the maximum observed (circles) and model-predicted (triangles) affinity for each number of somatic mutations is shown. (C, D) Total number of 'uphill' paths for select antigen selection scenarios (colored bars) for (C) CR9114 and (D) CR6261. Error bars indicate standard error obtained through bootstrap, see Materials and methods. (E, F) Total log probability (in arbitrary units) of mutational trajectories from germline to somatic sequence for (E) CR9114 and (F) CR6261 under different antigen selection scenarios, in a moderate selection model. Error bars indicate standard error obtained through bootstrap, see Materials and methods. (G, H) 25 most likely paths for (G) CR9114 and (H) CR6261, from select scenarios in (E, F); –logKD plotted for each antigen. For the random mixed scenario ('R'), a representative case is shown. ’A’ indicates the average mixed scenario; ’O’ indicates the optimal scenario. (I, J) Probability of mutation order under optimal antigen selection scenario ‘O' for CR9114 (I) and H1 for CR6261 (J). Selection scenarios are as in (E, F) and shown in colored bar at top; the total probability (through all possible paths) for each mutation to occur at each mutational step is shown as stacked colored bars.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Functional form of mutation step probability, illustrated for parameters chosen to represent strong, moderate, and weak selection models. (B, C) Total log probability of the mutational trajectories between germline and somatic sequences for (B) CR9114 and (C) CR6261 under different antigen selection scenarios, assuming strong (left) or weak (right) selection, as shown for moderate selection in Figure 5E,F. Strong selection scenarios are shown on a linear scale, as total probability is equal to the number of uphill paths. The ‘average’ mixed scenario is not evaluated for strong selection, as the quantitative effect of averaging is undone by the binarizing effect of the transition probability. Error bars indicate standard errors obtained through bootstrap, see Materials and methods.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Histogram of the total probability of all pathways passing through each variant in the optimal selection scenario, divided by the total probability in a model with no selection, transformed to log10 scale (see Materials and methods). Dotted line indicates the 11% of variants favored in the selective model (log probability ratio greater than zero). (B) Favored variants are shown on the force-directed graph for CR9114 H1 –logKD, as in Figure 1G, with darker color according to the log probability ratio. Other variants with log probability ratio less than zero are shown in light yellow.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/71393/elife-71393-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** H1 (A) and 'R' (B) for CR9114 and 'O' (C) and 'R' (D) for CR6261, as in Figure 5I,J. For the random mixed scenario 'R', the representative cases from Figure 5G,H are shown.

To compare antigen selection scenarios more generally, we developed a framework that evaluates the total probability of all possible mutational pathways from germline to somatic, under an array of antigen selection scenarios (individual, sequential, and mixed). Our framework assumes that the probability of any mutational step is higher if –logKD increases, but does not necessarily forbid neutral or deleterious steps; we evaluate a variety of specific forms of this step probability and find that our major results are consistent (Figure 5—figure supplement 1A, see Materials and methods). We assume that each amino acid substitution occurs in a single mutational step; though there are amino acid substitutions that must proceed by multiple nucleotide mutations that may occur in a single round, or over multiple rounds, of somatic hypermutation (Spisak et al., 2020; Unniraman and Schatz, 2007). Mixed antigen regimes approximate exposure to a cocktail of antigens. We model these with two approaches: (1) ‘average’, using the average –logKD across all antigens, and (2) 'random', using –logKD for a randomly selected antigen at each step (note that using the maximum –logKD across antigens would always be trivially favored) (Wang et al., 2015). While these models simplify the complexities of affinity maturation in vivo (Victora and Nussenzweig, 2012), especially how affinity relates to B cell lineage dynamics and the mutational bias at the nucleotide level (Spisak et al., 2020), they provide insight into the relative probabilities of mutational paths under distinct antigen selection scenarios.

Again we find that the vast majority of likely antigen selection scenarios for CR9114 involve first H1, followed by H3, followed by influenza B (Figure 5E, Figure 5—figure supplement 1B). These results are underscored by examining improvement in –logKD along the most likely mutational paths for each scenario (Figure 5G): in the optimal sequential scenario, –logKD can improve substantially for each antigen in turn, while in an H1-only scenario, the improvements in H1 binding at each step are much more gradual, reducing the likelihood. The average mixed scenario shows qualitatively similar paths to the optimal sequential scenario, although with lower overall probability. In the random mixed scenario, even the best pathways are often unable to improve affinity to the randomly selected antigen, and affinity to antigens not under selection often declines, making these scenarios much less likely.

Given the optimal sequential selection scenario, the vast majority of genotypes are unlikely evolutionary intermediates to the somatic sequence (Figure 5—figure supplement 2). We visualize the impact of epistasis on mutational order by considering the probability of each mutation to occur at each mutational step (Figure 5I; Figure 5—figure supplement 3). The three antigen exposure epochs exhibit clear differences in favored mutations. Mutations I57S, K82I, and S83F must occur early, due to their strong synergistic interactions for all three antigens. In addition, we see that F30S is unlikely to happen very early (due to its sign epistasis under H1 selection) as well as unlikely to happen very late (due to its strong benefit under influenza B selection).

In contrast, for CR6261, all selection scenarios have relatively similar likelihood (Figure 5F, Figure 5—figure supplement 1C). Among sequential scenarios, however, those beginning with H1 are more likely than those beginning with H9, as the first two mutational steps can improve affinity to H1 more than H9, and mutations late in maturation can improve affinity to H9 more than H1 (Figure 1F, Figure 5B). Still, unlike CR9114, in both single antigen and mixed scenarios, there are many likely paths that continually improve in binding to both antigens (Figure 5H). Initially the order of mutations is highly constrained due to strong synergistic epistasis, and differences between selection scenarios reflect differences in mutational effects between antigens (Figure 5J, Figure 5—figure supplement 3). We note that T29P is highly likely to occur first in scenarios that begin with H1, as this is the only single mutation that can improve H1 affinity, albeit rather modestly.

## Discussion

Overall, we find that evolutionary pathways to bnAbs can be highly contingent on epistatic and pleiotropic effects of mutations. Specifically, the acquisition of breadth for CR9114 is extremely constrained and is likely to have occurred through exposure to diverse antigens in a specific order, due to the structure of correlations and interactions between mutational effects. In contrast, CR6261 could have acquired affinity to H1 and H9 in a continuous and simultaneous manner, perhaps because these antigens are more similar; since H9 is not a commonly circulating strain, this breadth was likely acquired by chance (Pappas et al., 2014).

We note that we cannot conclusively determine how CR9114 and CR6261 evolved in vivo. The isolation of these specific antibodies from phage display libraries (Throsby et al., 2008; Dreyfus et al., 2012) was likely biased by the HA subtypes used for screening, and although unlikely, may have introduced mutations during PCR amplification. Regardless, these antibody sequences occupy regions of sequence space that are useful for understanding the relationship between sequence, affinity, and breadth. By characterizing their binding landscapes, we find that epistasis and trade-offs constrain the mutational pathways to these specific somatic sequences and their associated breadth. Indeed, we find that not all of the observed mutations are required to confer broad affinity, and future work is needed to explore what alternative pathways to breadth might be accessible through other mutations. It is also worth noting that selection pressure to bind the HA stem epitope on virions may be different from pressure to bind soluble recombinant HA, although several studies have found anti-stem antibody affinity to recombinant HA to be indicative of viral neutralization (Dreyfus et al., 2012; Corti et al., 2011; Lingwood et al., 2012). Further, stem-targeting bnAbs and their germline precursors have been characterized as polyreactive (Bajic et al., 2019; Guthmiller et al., 2020) and thus likely experience additional selection pressures that are not captured by our measurements and models, such as negative selection against autoreactivity. Although we cannot determine which specific antigens were involved in the selection of these antibodies in vivo, the diverse HA subtypes we employ capture variation representative of circulating influenza strains and thus serve as useful probes of varying levels of breadth (Corti et al., 2017). Future work integrating these measurements of affinity and breadth with measurements of stability and polyreactivity will provide important insight into the molecular constraints of bnAb evolution.

Notably, the landscapes characterized here are among the largest combinatorially complete collections of mutations published to date. In some respects, our observations of high-order interactions are consistent with earlier work in other proteins. In particular, epistasis has been found to affect function and constrain evolutionarily accessible pathways across functionally and structurally distinct proteins (Weinreich et al., 2006; Starr et al., 2017; Ortlund et al., 2007; Podgornaia and Laub, 2015; Gong et al., 2013; Sailer and Harms, 2017b; Miton and Tokuriki, 2016; Poelwijk et al., 2019; Bank et al., 2015). Further, pairwise and high-order epistasis appear to be common features of binding interfaces, such as enzyme-substrate and receptor-ligand interactions (Weinreich et al., 2006; Starr et al., 2017; Ortlund et al., 2007; Podgornaia and Laub, 2015; Sailer and Harms, 2017b; Miton and Tokuriki, 2016), and interacting mutations are often spaced in both sequence and structure, underscoring the complexity of protein-protein interfaces (Podgornaia and Laub, 2015; Adams et al., 2019; Braden et al., 1998; Esmaielbeiki et al., 2016; Rotem et al., 2018). On the other hand, the strongly synergistic, nested mutations crucial for CR9114 breadth are unusual, perhaps due to the nature of antibody-antigen interfaces or to the unique dynamics of affinity maturation (Victora and Nussenzweig, 2012). Together, these observations suggest that interactions between multiple mutations, such as those we characterize here, could play a substantial role in affinity maturation and may contribute to the rarity of bnAbs in natural repertoires.

Our findings provide molecular insight into the emerging picture of how selection can elicit broad affinity, illustrated by a substantial recent body of work ranging from in vivo experimental approaches (Krammer et al., 2012; Wang et al., 2010) to quantitative modeling of immune system dynamics (Wang et al., 2015; Wang, 2017; Sachdeva et al., 2020; Molari et al., 2020; Sprenger et al., 2020). These diverse studies often find that mixed-antigen regimens are less effective than sequential regimens at eliciting bnAbs. Our results demonstrate that, at least in part, this may be due to the intrinsic structure of the mutational landscape, defined by the complex interactions of mutational effects across antigens. With more studies of binding landscapes for diverse antibodies, we could better understand how such features generalize between different germline sequences, somatic mutation profiles, and antigen molecules. These insights will be valuable for leveraging germline sequence data and antigen exposure information to predict, design, and elicit bnAbs for therapeutic and immunization applications.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>EBY100</td>
      <td>ATCC</td>
      <td>Cat#:MYA-4941</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>Sf9</td>
      <td>ThermoFisher</td>
      <td>Cat#:B82501</td>
      <td>Cell line for production of baculovirus</td>
    </tr>
    <tr>
      <td>Cell line (Trichoplusia ni)</td>
      <td>High-Five</td>
      <td>ThermoFisher</td>
      <td>Cat#:B85502</td>
      <td>Cell line for HA expression</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-cMyc-FITC (Mouse monoclonal)</td>
      <td>Miltenyi Biotec</td>
      <td>Cat#:130-116-485</td>
      <td>FACS (1:50)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCT302 (plasmid)</td>
      <td>Addgene</td>
      <td>Cat#:41845</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCT302_CR9114 _germline (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid map in Supplementary file 4</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCT302_CR9114 _somatic (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid map inSupplementary file 5</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCT302_CR6261 _germline (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid map inSupplementary file 6</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCT302_CR6261 _somatic (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid map inSupplementary file 7</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET21a-BirA (plasmid)</td>
      <td>Addgene</td>
      <td>Cat#:20857</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CR9114 golden gate dsDNA fragments</td>
      <td>IDT</td>
      <td></td>
      <td>Sequences listed inSupplementary file 2</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CR6261 Golden Gate primers</td>
      <td>IDT</td>
      <td></td>
      <td>Sequences listed inSupplementary file 3</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Illumina sequencing primers</td>
      <td>IDT</td>
      <td></td>
      <td>Sequences listed inSupplementary file 1</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Streptavidin-RPE</td>
      <td>ThermoFisher</td>
      <td>Cat#:S866</td>
      <td>FACS (1:100)</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Biotinylated A/New Caledonia/99 (H1) ectodomain</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid sequence inSupplementary file 8</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Biotinylated A/Hong Kong/99 (H9) ectodomain</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid sequence inSupplementary file 9</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Biotinylated A/Wisconsin/05 (H3) ectodomain</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid sequence inSupplementary file 10</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Biotinylated B/Ohio/05 (Flu B) ectodomain</td>
      <td>This paper</td>
      <td></td>
      <td>Plasmid sequence inSupplementary file 11</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Bac-to-Bac Kit</td>
      <td>ThermoFisher</td>
      <td>Cat#:10359016</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Zymo Yeast Plasmid Miniprep II</td>
      <td>Zymo Research</td>
      <td>Cat#:D2004</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Custom code</td>
      <td>This paper</td>
      <td></td>
      <td>https://github.com/klawrence26/bnab-landscapes (copy archived at swh:1:rev:61c1673a101ea739d5b7e9b282f6bcfad41d7e90, Phillips, 2021)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Interactive CR9114 data browser</td>
      <td>This paper</td>
      <td></td>
      <td>https://yodabrowser.netlify.app/yoda_browser/</td>
    </tr>
  </tbody>
</table>

### Antibody library production

#### Germline sequence reconstructions

For CR9114, we obtained the somatic heavy chain nucleotide sequence from Dreyfus et al., 2012 (GenBank JX213639.1) and reconstructed the germline nucleotide sequence using IMGT (Giudicelli et al., 2006) and IgBLAST (Ye et al., 2013). Both methods assigned the same V-gene and J-gene alleles (IGHV1-69*06 and IGHJ6*02), but there is ambiguity in the D-gene assignment and at the V-D junction, particularly at site 109. The preferred IMGT junction alignment assigns a mutation here, S109N, while a different junction alignment from IgBLAST does not. Because of the inherent difficulty of reconstructing mutations in the junction region, especially in antibodies with a short D region, we chose the alignment without the mutation at site 109. Our reconstructed germline nucleotide sequence is available in Supplementary file 12. We then took the resulting germline and somatic amino acid sequences, as shown in Figure 1A, and constructed new nucleotide sequences codon-optimized for yeast.

For CR6261, the somatic and reconstructed germline heavy chain amino acid sequences were published in Lingwood et al., 2012. We used these sequences, similarly constructing codon-optimized nucleotide sequences for expression in yeast. The original somatic nucleotide sequence is also available (GenBank HI919029.1).

We note that all antibody libraries and clonal strains were constructed using somatic forms of the light chain, as these antibodies were isolated by combinatorial phage display (Throsby et al., 2008; Dreyfus et al., 2012), and so it is not possible to infer the naturally paired germline light chain sequence. Additionally, the CR9114 and CR6261 light chains were previously determined not to impact binding (Lingwood et al., 2012; Dreyfus et al., 2012; Ekiert et al., 2009). The somatic light chain sequence for CR9114 was obtained from Dreyfus et al., 2012 (GenBank JX213640.1), and that for CR6261 was obtained from Throsby et al., 2008 (GenBank HI919031.1).

#### Mutation selection

CR9114 contains a total of 18 amino acid substitutions between the somatic variant and the reconstructed germline sequence. However, a library of $2^{18}=262,144$ variants would be costly and time-consuming to produce and assay via our methods. We therefore identified two mutations that were distant from antigen contacts in the crystal structure: A25S and E51D (Dreyfus et al., 2012). We measured binding affinities for somatic sequences with and without these two mutations, and found that these variants had comparable affinities for both H1 and H3 (Figure 1—figure supplement 7). Although these mutations may have some small impact on binding, especially in combination with others, excluding them allowed for a simpler cloning strategy and a more manageable library size.

Similar to the CR9114 library design, we reduced the number of mutations present in the CR6261 library by excluding three mutations that were distant from antigen contacts in the crystal structure: 6QE, L50P, and V101M (Ekiert et al., 2009). We validated the marginal contribution of these mutations to binding by measuring the binding affinities for the somatic sequence with and without these mutations reverted to the respective germline residue (Figure 1—figure supplement 7).

#### Yeast display plasmid and strains

To generate clonal yeast display strains and libraries for CR9114, we cloned scFv constructs (VL -Ser(Gly4Ser)5-VH-Myc) into the pCT302 plasmid (Midelfort et al., 2004) (kind gift from Dane Wittrup; Addgene, Watertown, MA, #41845). For the clonal CR9114 somatic and germline strains, gene blocks corresponding to the somatic or inferred germline sequences were cloned into pCT302 by Gibson Assembly (Gibson et al., 2009) (plasmid maps in Supplementary files 4–5). For producing the plasmid backbone required for Golden Gate library generation (described below), we removed an existing Bsa-I site from the pCT302 plasmid by site-directed mutagenesis (Agilent, Santa Clara, CA, #200521) and replaced the VH domain with the ccdB gene. To generate clonal yeast strains, Gibson Assembly products were transformed into electrocompetent DH10B E. coli cells, and the resulting plasmids were mini-prepped and Sanger sequenced. Following sequence confirmation, plasmids were transformed into EBY100 yeast cells (ATCC #MYA-4941) as described in the high-efficiency yeast transformation protocol (Gietz and Schiestl, 2007). Transformants were plated on SDCAA-agar (1.71 g/L YNB without amino acids and ammonium sulfate [Sigma-Aldrich #Y1251], 5 g/L ammonium sulfate [Sigma-Aldrich #A4418], 2% dextrose [VWR #90000–904], 5 g/L Bacto casamino acids [VWR #223050], 100 g/L ampicillin [VWR #V0339], 2% Difco Noble Agar [VWR #90000–774]) and incubated at 30°C for 48 hr, single colonies were restruck on SDCAA-agar and again incubated at 30°C for 48 hr, and the resulting clonal yeast strains were verified to have the construct of interest by colony PCR. Construction of the yeast libraries is described below. All yeast strains were grown to saturation in SDCAA at 30°C, supplemented with 5% glycerol, and stored at −80°C.

CR6261 clonal yeast display strains and libraries were generated in an identical manner to that of CR9114, except where noted below (see Supplementary files 6–7 for plasmid maps corresponding to the germline and somatic sequences).

#### Golden gate assembly

For CR9114, due to the number of mutations required and their positions along the heavy chain coding sequence, we designed a library cloning strategy using Golden Gate combinatorial assembly (Engler et al., 2008). We divided the heavy chain coding region into five roughly equal fragments, ranging from 79 to 85 bp and each containing between 1 and 5 mutations. We added BsaI sites and additional overhangs to both ends of each fragment sequence, with cut sites carefully chosen so that the five fragments will assemble uniquely in their proper order within the plasmid backbone. For each fragment with $n$ mutations, we then ordered $2^{n}$ individual DNA duplexes with each possible combination of mutations (ranging from 2 to 32 versions for each fragment, a total of 66 fragments) from IDT (Coralville, IA) (see Supplementary file 2). By pooling the versions of each fragment in equal volumes, then pooling the five fragment pools in equimolar ratios, we obtained a randomized fragment mix containing all 216 sequences present at approximately equal frequencies.

In addition to the fragment mix, we prepared the plasmid backbone for the Golden Gate reaction. We created a version of the yeast display plasmid with the counter-selection marker ccdB in place of the heavy chain sequence, with flanking BsaI sites (see above). We performed Golden Gate cloning using BsaI-HFv2 (NEB, Ipswich, MA, #R3733) following the manufacturer recommended protocol, with a 5:1 molar ratio of the fragment insert pool to plasmid backbone.

We transformed the assembly mix into electrocompetent E. coli (DH10B) via electroporation in 10 x 50 μL cell aliquots. We recovered each transformation in 5 mL SOC (2% tryptone, 0.5% yeast extract, 10 mM NaCl, 2.5 mM KCl, 10 mM MgCl2, 10 mM MgSO4, 20 mM glucose) at 37°C for 1 hr, and then transferred each to 100 mL of molten LB (1% tryptone, 0.5% yeast extract, 1% NaCl) containing 0.3% SeaPrep agarose (VWR, Radnor, PA #12001–922) spread into a thin layer in a 1L baffled flask (about 1 cm deep). The mixture was allowed to set on ice for an hour, after which it was kept for 18 hr at 37C to allow for dispersed growth of colonies in 3D. We observed $∼3\times10^{5}$ colonies per aliquot, for a total of $∼3$ million transformants. After mixing the flasks by shaking for 1 hr, we pelleted the cells and prepared plasmid by standard midiprep (Zymo Research, Irvine, CA, D4201), from which we obtained >120 μg of purified plasmid.

For CR6261, we designed a library cloning strategy also using Golden Gate combinatorial assembly, but with fragments created by PCR instead of purchased. We divided the heavy chain coding region into three roughly equal fragments, each containing between 2 and 5 mutations. We designed these fragments such that the mutations they contain are close to the 3’ or 5’ ends and can thus be easily incorporated by PCR. PCR primers included mutations, BsaI sites, and unique overhangs chosen so that the three fragments would assemble uniquely in their proper order within the plasmid backbone. For each version of the three fragments, we generated dsDNA by PCR (52 PCR reactions in total; see Supplementary file 3 for primer sequences). By pooling all versions of each fragment in equal volumes, then pooling the three fragment pools in equimolar ratios, we obtain a randomized fragment mix that, when ligated in the Golden Gate reaction, produces all of the 211 sequences present at approximately equal frequencies.

In addition to the fragment mix, we prepared the plasmid backbone for the Golden Gate reaction. We created a version of the yeast display plasmid with the counter-selection marker ccdB in place of the three-fragment sequence, with flanking BsaI sites. We performed Golden Gate cloning using BsaI-HFv2 (NEB #R3733) following the manufacturer recommended protocol, with a 7:1 molar ratio of fragment inserts to plasmid backbone.

The transformation of the CR6261 library into E. coli was conducted in a similar fashion to that of CR9114, except that 8x50 μL cell aliquots were transformed, and 600,000 colonies were pooled for plasmid midiprep.

#### Yeast library production

We then transformed the CR9114 plasmid library into EBY100 cells by standard high-efficiency protocols (Gietz and Schiestl, 2007). We recovered transformants in molten SDCAA (1.71 g/L YNB without amino acids and ammonium sulfate (Sigma-Aldrich #Y1251), 5 g/L ammonium sulfate (Sigma-Aldrich, St. Louis, MO, #A4418), 2% dextrose (VWR #90000–904), 5 g/L Bacto casamino acids (VWR #223050), 100 g/L ampicillin (VWR # V0339)) containing 0.35% SeaPrep agarose (VWR #12001–922) spread into a thin layer (about 1 cm deep). The mixture was allowed to set on ice for an hour, after which it was kept for 48 hr at 30°C to allow for dispersed growth of colonies in 3D. From five such flasks, we obtained ∼700,000 colonies (>10 times the library diversity). After mixing the flasks thoroughly by shaking for 1 hr, we grew cells in 5 mL tubes of liquid SDCAA for five generations and froze the saturated culture in 1 mL aliquots with 5% glycerol.

The CR6261 yeast library was generated in a manner identical to that of CR9114, except that ∼60,000 colonies were pooled due to the smaller library size.

#### Isogenic strain production

In addition to the full library, for both CR9114 and CR6261 we assayed a small number of variants by low-throughput flow cytometry for Tite-Seq validation. Any individual variant in the library can be produced in the same manner as described above: we simply selected the DNA duplex fragments corresponding to each desired variant and set up an individual Golden Gate reaction. The resulting assembled plasmid was transformed into E. coli, mini-prepped, and transformed into EBY100 in the same manner as described above. We verified the sequence identity of each variant by Sanger sequencing the entire scFv sequence.

We also constructed isogenic strains for validation experiments with genotypes that are not present in the full library. For CR9114, to test the impact of excluding mutations A24S and E46D, we constructed a strain containing the remaining 16 somatic mutations by cloning a gene block of the corresponding VH sequence into the germline CR9114 pCT302 plasmid via Gibson Assembly (Figure 1—figure supplement 7). For CR6261, we similarly constructed a strain with the Q6E, L50P, and V101M mutations reverted.

### Antigen production

#### Choice of HA antigens

CR9114 was isolated from pooled PBMC from three donors who had received the trivalent 2006 influenza vaccine (Throsby et al., 2008; Dreyfus et al., 2012), which contained A/New Caledonia/20/1999 (H1N1), A/Wisconsin/67/2005 (H3N2), and B/Malaysia/2506/2004 (Victoria lineage) (Ekiert et al., 2011). CR6261 was isolated from pooled PBMC from the same three donors, plus an additional seven donors who did not receive the vaccine (Throsby et al., 2008). Because PBMC were isolated only 7 days after vaccination, although it is possible that CR6261 and CR9114 matured in response to these specific antigens, it is more likely that the vaccine elicited memory recall of these antibodies (Victora and Nussenzweig, 2012). Here, we chose to measure binding affinities to diverse antigens spanning the range of breadth for both CR9114 and CR6261. CR9114 neutralizes strains across influenza A (groups 1 and 2) and influenza B, so we measured affinities to one strain from each of these groups, and selected vaccine-like strains: A/New Caledonia/20/1999 (H1N1), A/Wisconsin/67/2005 (H3N2), and B/Ohio/1/2005 (Victoria lineage). CR6261 neutralizes strains across influenza A group 1, thus we measured affinities to two strains from distinct subtypes within group 1: A/New Caledonia/20/1999 (H1N1) and A/Hong Kong/1073/1999 (H9N2). We note that CR9114 indeed binds A/Hong Kong/1073/1999 (H9N2) (Dreyfus et al., 2012), but CR9114 variant affinities for this strain were not measured here, as we prioritized measurements to antigens that span the breadth of each antibody.

#### HA cloning, expression, and purification

Trimeric hemagglutinin (HA) antigen was produced as previously described (Ekiert et al., 2011; Dreyfus et al., 2012; Margine et al., 2013). Briefly, the HA ectodomain (Influenza A: residues 11–329 of HA1 and 1–176 of HA2 (H3 numbering); Influenza B: residues 1–523) of Influenza A/New Caledonia/1999 H1, Influenza A/Hong Kong/1999 H9, Influenza A/Wisconsin/2005 H3, and Influenza B/Ohio/2005, with N-terminal gp67 signal peptide and C-terminal biotinylation site (GGGLNDIFEAQKIEWHE), thrombin cleavage site, trimerization domain and His6 tag, were cloned into pFastbac (plasmid maps in Supplementary files 8–11). Recombinant bacmid was generated using the ThermoFisher Bac-to-Bac kit (ThermoFisher, Waltham, MA, #10359016). Sf9 cells (ThermoFisher #B82501, not authenticated but verified to be mycoplasma-negative) were then transfected (ThermoFisher #A38915, not authenticated but verified to be mycoplasma-negative) with the resulting bacmids, and P0 HA-baculovirus was harvested 7 days post-transfection by clarifying viral supernatant at 1000 x g for 10 min. HA-baculovirus was then amplified twice by successively infecting 187 million Sf9 cells with 100 μL of viral supernatant and incubating in a humidified incubator at 28°C for 12 days. To induce HA expression, 105 million High-Five cells (ThermoFisher #B85502) were resuspended with 15 mL P2 HA-baculovirus, incubated for 20 min at room temperature, and then transferred to a 1 L non-baffled flask with 200 mL Corning Express-Five media (ThermoFisher #10486025) supplemented with 18 mM L-glutamine (VWR #45000–676). Expression cultures were incubated in a shaking incubator at 28C and 110 rpm for 48 hr, after which HA-containing media was clarified by spinning first at 1000 x g for 5 min at 4°C, and then by spinning the resulting supernatant again at 4000 x g for 20 min at 4C. The clarified media was then dialyzed into PBS (VWR #45000–448) by performing 4 x 2 hr 10-fold buffer exchanges to remove metal chelators from culture media. Dialyzed media was then combined with 10 mL equilibrated NiNTA resin (ThermoFisher #R90101), gently shaken for 3 hr at 4°C, and loaded onto a column. The resin was washed first with 15 column volumes Wash Buffer 1 (50 mM Tris pH 8 at 4C, 300 mM KCl, 10 mM imidazole) and subsequently with 15 column volumes Wash Buffer 2 (50 mM Tris pH 8 at 4C, 300 mM KCl, 20 mM imidazole). HA was eluted from the resin after 10 min incubation with Elution Buffer (50 mM Tris pH 8 at 4°C, 300 mM KCl, 250 mM imidazole). HA was then buffer exchanged into PBS using 10 KDa Amicon Ultra Centrifugal Filters (Millipore Sigma, Burlington, MA #UFC901008) and concentrated to at least 1 mg/mL for downstream biotinylation.

#### BirA expression and purification

BirA was expressed and purified as previously described (Ekiert et al., 2011). Briefly, pET21a-BirA expression plasmid (Howarth et al., 2005) (kind gift from Alice Ting; Addgene #20857) was transformed into BL21 (DE3). Transformed BL21 cells were grown in 4 L baffled flasks with 1 L low-salt LB medium (5 g/L NaCl, 5 g/L yeast extract (VWR #90000–722), 10 g/L tryptone (VWR #90000–286)) at 37°C to an OD (600 nm) of ∼0.8. The culture was then moved into cold water to bring it to 23°C, IPTG was added to a final concentration of 1 mM, and the culture was incubated at 23C for ∼16 hr. The culture was then harvested by centrifugation (3000 x g, 10 min), resuspended in 30 mL lysis buffer (50 mM Tris pH 8 at 4C, 300 mM KCl, 10 mM imidazole, EDTA-free protease inhibitor cocktail tablet (Millipore Sigma #4693159001)), lysed by sonication (Branson Sonifier 450), and shaken at 4°C for 30 min. Lysate was clarified by spinning at 25,000 x g for 1 hr, and then the supernatant was incubated with 5 mL NiNTA resin at 4°C for 3 hr with gentle shaking. The resin was pelleted by spinning at 500 x g for 5 min and washed twice by gentle shaking with 35 mL lysis buffer at 4°C for 30 min. Protein was eluted with 20 mL Elution Buffer (50 mM Tris pH 8 at 4°C, 300 mM KCl, 250 mM imidazole), buffer exchanged into Storage Buffer (50 mM Tris pH 7.5 at 4°C, 200 mM KCl, 5% glycerol) using 10 KDa Amicon Ultra Centrifugal Filters (Millipore Sigma #UFC901008), flash frozen in liquid nitrogen, and stored in single-use aliquots at −80°C.

#### Biotinylation and HA-biotin quality control

Purified hemagglutinin was biotinylated as previously described (Fairhead and Howarth, 2015; Ekiert et al., 2011). Briefly, 100 μL HA (> 1 mg/mL) was incubated with 0.5 μL 1 M MgCl2, 2 μL 100 mM ATP, 0.5 μL 50 mM biotin, and 2.5 μL BirA (10 mg/mL). This was mixed by gentle pipetting and incubated at 30C with gentle rocking. After 1 hr incubation, equivalent amounts of ATP, BirA, and biotin were added to the reaction, which was incubated for an additional hour at 30°C. Following the 2 hr incubation, the 100 μL reaction was exchanged thrice into 15 mL PBS using a 50 KDa MWCO buffer exchange column (Millipore Sigma #UFC905008). The degree of biotinylation was then assessed by a streptavidin gel-shift assay, as previously described (Fairhead and Howarth, 2015). Briefly, 10-fold molar excess streptavidin (Millipore Sigma #189730) was added to 4 μg biotinylated HA and incubated at room temperature for 5 min prior to running on SDS-PAGE. Gels were transferred to nitrocellulose membranes and probed with mouse anti-His monoclonal antibodies (ThermoFisher #R930-25) and Goat-anti-mouse secondary antibodies (LiCor, Lincoln, NE, Cat#925–32210). HA was verified to be > 80% biotinylated by densitometry.

### Tite-Seq assays

Tite-Seq was performed essentially as previously described (Adams et al., 2016), with some modifications as detailed below. For each antibody-antigen pair, three replicate Tite-Seq assays were performed on different days.

#### Induction of antibody expression

On day 1, yeast scFv libraries, as well as germline and somatic clonal strains, were thawed by inoculating 5 mL SDCAA (1.71 g/L YNB without amino acids and ammonium sulfate (Sigma-Aldrich #Y1251), 5 g/L ammonium sulfate (Sigma-Aldrich #A4418), 2% dextrose (VWR #90000–904), 5 g/L Bacto casamino acids (VWR #223050), 100 g/L ampicillin (VWR # V0339)) with 150 μL glycerol stock (saturated culture with 5% glycerol) and rotated at 30°C for 20 hr. On day 2, yeast cultures were back-diluted to OD600 = 0.2 in 5 mL SDCAA and rotated at 30°C for approximately 4 hr, or until reaching log phase (OD600 = 0.4–0.8). 1.5 mL log-phase cells were then pelleted, resuspended in 4 mL SGDCAA (1.71 g/L YNB without amino acids and ammonium sulfate (Sigma-Aldrich #Y1251), 5 g/L ammonium sulfate (Sigma-Aldrich #A4418), 0.2% dextrose (VWR #90000–904), 1.8% galactose (Sigma-Aldrich #G0625), 5 g/L Bacto casamino acids (VWR #223050), 100 g/L ampicillin (VWR #V0339)), and rotated at room temperature for 20–22 hr.

#### Primary antigen labeling

On day 3, 20–22 hr post-induction, yeast cultures were pelleted, washed twice with 0.1% PBSA (VWR #45001–130; GoldBio, St. Louis, MO, #A-420–50), and resuspended to an OD600 of 1. A total of 700 μL of OD1 yeast cells were labeled with biotinylated HA at each of eleven antigen concentrations (half-log increments spanning 1 pM – 100 nM for H1 and H9, and 10 pM – 1 μM for H3 and influenza B, as well as no HA), with volumes adjusted such that the number of antigen molecules was in 10-fold excess of antibody molecules (assuming 50,000 scFv/cell). Yeast-HA mixtures were rocked at 4°C for 24 hr.

#### Secondary labeling

On day 4, yeast-HA complexes were pelleted by spinning at 3000 x g for 10 min at 4°C, washed twice with 5% PBSA + 2 mM EDTA, and simultaneously labeled with Streptavidin-RPE (1:100, Thermo Fisher #S866) and anti-cMyc-FITC (1:50, Miltenyi Biotec, Somerville, MA, #130-116-485) at 4°C for 45 min. Following secondary labeling, yeast were washed twice with 5% PBSA + 2 mM EDTA, and left on ice in the dark until sorting.

#### Sorting and recovery

Yeast were sorted on a BD FACS Aria Illu, equipped with 405 nm, 440 nm, 488 nm, 561 nm, and 635 nm lasers, and an 85 micron fixed nozzle. Prior to sorting, single-color controls were used to compensate for the minimal FITC overlap with PE. Single cells were gated by FSC vs SSC, and then this population was sorted either by expression (FITC) or by expression and binding (PE). For all sorts, at least ten-fold excess of the library diversity was sorted (∼1.6 million cells for CR9114; ∼500,000 cells for CR6261). For the expression sorts, singlets were sorted into eight equivalent FITC log-spaced gates. For the binding sorts, FITC-positive cells were sorted into 4 PE bins (the PE-negative population comprised bin 1, and the PE-positive population was split into three equivalent log-spaced bins 2–4; see Figure 1—figure supplement 6). Polypropylene collection tubes were coated and filled with 1 mL YPD supplemented with 1% BSA and placed on ice until recovery. Sorted cells were pelleted by spinning at 3000 x g for 10 min, and supernatant was removed by pipette to avoid disturbing the pellets. Pellets were then resuspended in 4 mL SDCAA, a small amount was plated on SDCAA-agar to quantify recovery efficiency, and cultures were rocked at 30°C until reaching late-log phase (OD600 = 0.6–1.2).

#### Sequencing library preparation

A total of 1.5 mL of late-log yeast cultures were pelleted and scFv plasmid was extracted using Zymo Yeast Plasmid Miniprep II (Zymo Research # D2004), per the manufacturer’s instructions, and eluted in 10 μL elution buffer. Heavy-chain amplicon sequencing libraries were prepared by a two-step PCR as previously described (Nguyen Ba et al., 2019). In the first PCR, unique molecular identifiers (UMI), inline indices, and partial Illumina adapters were appended to the heavy chain through 3–5 amplification cycles to minimize PCR amplification bias. In the second PCR, the remainder of the Illumina adapter and sample-specific Illumina i5 and i7 indices were appended through 35 amplification cycles (see Supplementary file 1 for primer sequences). The first PCR used 5 μL plasmid DNA as template in a 25 μL reaction volume, with Q5 polymerase according to the manufactuer’s instructions (NEB # M0491L), and was incubated in a thermocycler with the following program: 1. 60 s at 98°C, 2. 10 s at 98°C, 3. 30 s at 66°C, 4. 30 s at 72°C, 5. GOTO 2, 2-4x, 6. 60 s at 72°C. PCR products were then combined with carrier RNA and purified by 1.1X Aline beads (Aline Biosciences #C-1003–5), and eluted in 35 μL elution buffer. 33 μL of the elution was used as input for the second PCR, in a total volume of 50 μL using Kapa polymerase (Kapa Biosystems #KK2502) according to the manufacturer’s instructions, and incubated in a thermocycler with the following program: 1. 30 s at 98°C, 2. 20 s at 98°C, 3. 30 s at 62°C, 4. 30 s at 72°C, 5. GOTO 2, 34x, 6. 300 s at 72°C. The resulting sequencing libraries were purified by 0.85X Aline beads, amplicon size was verified to be ∼500 bp by running on a 1% agarose gel, and amplicon concentration was quantified by a fluorescent DNA-binding dye (Biotium, Fremont, CA, #31068, per manufacturer’s instructions). Amplicons were then pooled for each gate according to the number of sorted cells to ensure even sequencing coverage. The pool was further size-selected by a two-sided Aline bead cleanup (0.55–0.85X), and the final pool size was verified by Tapestation 5000 HS and 1000 HS. Final sequencing library concentration was determined by Qubit fluorometer and sequenced on an Illumina NovaSeq S2 or Miseq v3 (2x150) with 5% PhiX.

#### Sequencing data processing

We first processed our raw sequencing reads to identify and extract the indexes and mutational sites, discarding priming regions and the constant regions between mutations. To do so, we developed custom Python scripts using the approximate regular expression library regex (Barnett, 2013), which allowed us to handle complications in sequence parsing that arise from the irregular lengths of the indices and from sequencing errors. We accept sequences that match the entire read (with no restrictions on bases at mutational sites) within the following mismatch tolerances: two mismatches in the multiplexing index, two mismatches in the priming site, and 15 substitution mismatches within the 170 bases of constant antibody sequence.

We then examine the mutational sites to call germline or somatic alleles, producing binary genotypes (‘0’ for germline or ‘1’ for somatic at each position). We require the exact germline or somatic sequence at every site: if there are any substitution errors in any of the mutation sites, the entire read is rejected. While it is possible to perform error correction based on Hamming distance to rescue reads with a few substitution errors, we find that on average only <8% of reads per sample contain any errors, and so we adopt the conservative approach of requiring perfect matching.

We next discarded sequencing reads with any mismatched indices (four total indices from the two PCR reactions), as well as reads with duplicate UMI sequences. Counts for each genotype were then tabulated, producing the final counts used for binding affinity inference (see below). On average, across all antigens and replicates, we obtain a mean coverage of ∼350 for CR9114 and ∼950 for CR6261, and a median coverage of ∼250 for CR9114 and ∼900 for CR6261.

#### Isogenic validation

Induction of scFv surface display, primary labeling, and secondary labeling of isogenic strains were performed identically to the Tite-Seq assay, except yeast cell and antigen volumes were scaled down by a factor of 10. Yeast cell FITC (scFv expression) and R-PE (HA binding) fluorescence intensity was assayed on a BD LSR Fortessa equipped with four lasers (440, 488, 561, and 633 nm). The equilibrium binding affinities ($K_{D}$) for each variant are inferred by fitting the log of a Hill function to the mean log R-PE fluorescence of scFv-expressing (FITC+) singlet yeast cells:

$$
meanlogfluorescence=log_{10}⁡(A_{s}\frac{c}{c+K_{D,s}}+B_{s}),
$$

where $c$ is the antigen concentration in molar units, $A_{s}$ is the increase in fluorescence due to saturation with antigen, $B_{s}$ is the background fluorescence, and $K_{D,s}$ is the equilibrium binding affinity. All isogenic measurements were performed in two to three biological replicates; see Figure 1—source data 3 for isogenic $-log_{10}⁡K_{D}$.

### Tite-Seq binding affinity inference

#### Mean-bin approach

To infer binding affinities using a simple mean-bin approach (Peterman and Levine, 2016), we incorporate sequencing data (the unique read counts of each genotype sequence $s$ in bin $b$ at concentration $c$, $R_{b,s,c}$) with flow cytometry data (the mean and standard deviation of log10-fluorescence of sorted cells in each bin $b$ at concentration $c$, $F_{b,c}$ and $\sigma_{F_{b,c}}$ respectively, and cell counts for each bin $b$ at each concentration $c$, $C_{b,c}$).

The mean log-fluorescence of each genotype sequence at each of the 12 antigen concentrations is calculated as:

$$
F¯_{s,c}=\sumbF_{b,c}⁢p_{b,s|c},
$$

where $p_{b,s|c}$ is the probability a cell with sequence $s$ would be sorted into bin b at concentration c is estimated from the sequencing read counts as:

$$
p_{b,s|c}=\frac{\frac{R_{b,s,c}}{\sums^{′}R_{b,s^{′},c}}⋅C_{b,c}}{\sumb^{′}(\frac{R_{b^{′},s,c}}{\sums^{′}R_{b^{′},s^{′},c}}⋅C_{b^{′},c})},
$$

in other words, the fraction of total reads in the bin corresponding to sequence $s$, scaled by the number of sorted cells in that bin, normalized over the four bins for each concentration.

The uncertainty in the mean bin inference was propagated as:

$$
\delta⁢F¯_{s,c}=\sqrt{\sumb(\delta⁢F_{b,c}^{2}⁢p_{b,s|c}^{2}+F_{b,c}^{2}⁢\delta⁢p_{b,s|c}^{2})}.
$$

Here, $\delta⁢F_{b,c}$ represents the spread in log-fluorescence values of cells sorted into the same bin $b$. While we could estimate this value using the bin width, in practice we find that the distribution of cell log-fluorescence values in a bin is far from uniform across the bin width. The distribution is often not normal either, but we find that approximating $\delta⁢F_{b,c}≈\sigma_{F_{b,c}}$, or the standard deviation in log10-fluorescence of cells sorted into bin $b$ at concentration $c$, adequately captures the typical variation. The error in $p_{b,s|c}$ arises largely from the sampling process of sequencing, which can be approximated as a Poisson process when read counts are relatively high. This gives

$$
\deltap_{b,s|c}=\frac{p_{b,s|c}}{\sqrt{R_{b,s,c}}}.
$$

Thus, $\delta⁢F¯_{s,c}$ can be written as

$$
\delta⁢F¯_{s,c}=\sqrt{\sumb(\sigma_{F_{b,c}}^{2}⁢p_{b,s|c}^{2}+F_{b,c}^{2}⁢\frac{p_{b,s|c}^{2}}{R_{b,s,c}})}.
$$

The equilibrium binding affinities ($K_{D}$) for each variant are inferred by fitting the logarithm of a Hill function to the resulting mean log10-fluorescence across the twelve antigen concentrations:

$$
F¯_{s,c}=log_{10}⁡(A_{s}⁢\frac{c}{c+K_{D,s}}+B_{s}),
$$

where $c$ is the antigen concentration in molar units, $A_{s}$ is the increase in fluorescence due to saturation with antigen, $B_{s}$ is the background fluorescence, and $K_{D,s}$ is the binding affinity. Fitting was performed with the curve_fit function of the Python package scipy.optimize. Reasonable bounds on the values of A(103-105), B(100-103) and KD(10-14-10-5) were imposed. Sequences leading to a failed optimization were deemed ‘non-binding’.

Inferred $K_{D}$ outside of the titration boundaries were then pinned to the boundaries ($10^{-12}$ and $10^{-7}$ for H1 and H9; $10^{-11}$ and $10^{-6}$ for H3 and FluB). Inferred $K_{D}$ with high error (standard deviation of $log_{10}⁡K_{D}>1.0$) or resulting from a poor fit ($r^{2}<0.8$) were removed from the data set prior to averaging $-log_{10}⁡K_{D}$ values across biological replicates.

We also explored an alternative maximum-likelihood framework for inferring binding affinities (see Appendix 1), but found it to be less accurate than the mean-bin approach when compared to isogenic flow cytometry measurements. Thus, we restricted our analysis to the simpler and more robust mean-bin inference presented here.

#### Force-directed layouts

To represent the high-dimensional binding affinity landscape in two dimensions, we use a force-directed graph layout approach. Each sequence in the antibody library is a node, connected by edges to its single-mutation neighbors (sequences that can be reached by one additional somatic mutation). An edge between two sequences $s$ and $t$ is given the weight

$$
w_{s,t}=\frac{1}{0.01+|log_{10}⁡(K_{D,s}^{ag})−log_{10}⁡(K_{D,t}^{ag})|},
$$

where $K_{D}^{ag}$ represent binding affinities to a particular antigen, ag. In the layouts shown in the main text, we use binding affinities to H1 for both CR6261 and CR9114. In force-directed layouts, edge weights correspond to the effective spring constant that tends to pull nodes closer together. Thus, a mutation from sequence $s$ to $t$ that has little impact on binding will cause that edge weight to be large, and the nodes will be pulled strongly together. A mutation from sequence $s$ to $t$ that causes a large difference in binding affinity (positive or negative) to the antigen will reduce the edge weight, moving those nodes further apart. After assigning all edge weights, we use the layout function layout_drl from the Python package iGraph, with default settings, to obtain the layout coordinates for each variant.

#### Expression data

As noted above, antibody libraries were sorted into eight bins along the FITC-A fluorescence axis (where FITC-A fluorescence is proportional to expression), each comprising 12.5% of the total singlet population (Figure 1—figure supplement 6). The mean expression log-fluorescence was computed for each variant using the corresponding variant counts and fluorescence data, as described above for the mean-bin $K_{D}$ inference. These expression values were then averaged across all biological replicates for each antibody (nine replicates for CR9114, six replicates for CR6261), and correlation between biological replicates, as well as with $-log_{10}⁡K_{D}$ values, are illustrated in Figure 1—figure supplement 5. For the isogenic flow cytometry measurements, variant expression was computed as the mean log FITC-A fluorescence.

### Epistasis analysis

#### Linear interaction models

To infer specific mutational effects, we begin with simple linear models where the effects of mutations (and mutation combinations) add to produce phenotypes. Our log-transformed phenotypes for each variant $s$, $y_{s}=-log_{10}⁡(K_{D,s})$, are proportional to free-energy changes, and thus a natural null expectation is that they combine additively (Wells, 1990; Olson et al., 2014) (although we also consider nonadditive epistatic interactions between individual loci here, and analyze the effects of an overall nonlinear transformation of this data in Appendix 2). Our additive-only model is

$$
y_{s}=\beta_{0}+\sumi=1L\beta_{i}⁢x_{i,s}+\epsilon,
$$

where $L$ is the number of mutations for a given antibody, $\beta_{0}$ is an intercept term, $\beta_{i}$ is the effect of the mutation at site $i$, $x_{i,s}$ is the genotype of variant $s$ at site $i$, and $\epsilon$ represents independently and identically distributed errors. Our general linear interaction models are

$$
y_{s}=\beta_{0}+\sumi\beta_{i}⁢x_{i,s}+\sumi<jL\beta_{i⁢j}⁢x_{i,s}⁢x_{j,s}+\sumi<j<kL\beta_{i⁢j⁢k}⁢x_{i,s}⁢x_{j,s}⁢x_{k,s}+…+\epsilon
$$

where $\beta_{i⁢j}$ represent second-order interaction coefficients between distinct sites $i$ and $j$, $\beta_{i⁢j⁢k}$ represent third-order interaction coefficients, and so on up to the desired maximum order of interaction.

There are multiple alternative coding systems for the binary genotypes $x_{i,s}$ that affect the values of inferred effects $\beta$ as well as their interpretation. Two common choices are (1) $x_{i,s}\in{0,1}$, often called ‘biochemical’ or ‘local’ epistasis, and (2) $x_{i,s}\in{-1,1}$, often called ‘statistical’ or ‘ensemble’ epistasis (Poelwijk et al., 2016). These frameworks are equivalent and related by a simple linear transformation, but the values of the coefficients vary between frameworks and have different interpretations. For ease of interpretation, in the Main Text and Figures we always show results obtained from inference in the biochemical epistasis framework. In Appendix 2, we discuss the differences between these two frameworks, and present results from inference in the statistical epistasis framework.

For an antibody with $L$ mutations, there are $L$ possible orders of interactions, with a total of $2^{L}$ epistatic coefficients $\beta$. From a measurement of $y$ for all $2^{L}$ possible sequences, there is a simple linear transformation to calculate the resulting $2^{L}\beta$ parameters (Poelwijk et al., 2016). This is a simple and fast approach to the calculation of epistasis that is widely used (Sailer and Harms, 2017b; Poelwijk et al., 2019), and we explore this approach in Appendix 2. However, we may instead wish to restrict our model to a lower order and examine whether it can explain the data with far fewer than $2^{L}$ parameters, as a conservative approach to detecting high-order epistasis.

Specifically, we truncate the model above at a maximum order $n$ and then fit and evaluate the resulting model. We begin with $n=1$ and continue to increase $n$ until the optimal model has been identified. There are multiple strategies for selecting between models with different numbers of parameters, such as AIC and BIC; here we take a cross-validation approach. For each fold, we hold out 10% of the dataset, train models at each maximum order on the remaining 90%, and evaluate the prediction performance ($R^{2}$) of the model on the held-out test set. After averaging the performances across all 10 folds for each truncated model, we choose the order that maximizes the test set performance as the optimal maximal order of interaction. We then re-train the model truncated at this order on the full dataset to obtain the final coefficients. We find that the optimal model identified by cross-validation for each antibody-antigen pair satisfies $p<N$ by ∼1 order of magnitude, where $p$ is the total number of model coefficients and $N$ the number of data points with measurable binding affinity. This gives confidence that our parameter estimates are well constrained by the data, even in the absence of other regularization (such as Lasso or Ridge regularization approaches).

To train a model of given order on a set of sequences, we use ordinary least squares (OLS) regression with the Python package statsmodels. From this, we obtain the coefficient values $\beta$ with their standard errors and p-values. To define significance of coefficients, we use a p-value cutoff of 0.05 with Bonferroni correction by the total number of model parameters. Coefficients, standard errors, p-values, and Bonferroni-corrected 95% confidence intervals are reported in Figure 1—source data 1 and 2. We also predict phenotypes $y^$ for each sequence from the coefficients and use these values in Figure 5A,B.

For CR9114 binding to influenza B, the number of sequences used for inference is far fewer than other antibody-antigen pairs ($N=256$), due to the large number of required mutations. We therefore use a fivefold rather than 10-fold split to reduce the test set noise. Nevertheless, the cross-validation procedure identifies a first-order (additive) model as optimal, due to the smaller sample size.

#### Structural analysis of epistatic coefficients

To examine the structural context of linear and pairwise coefficients, we performed three simple analyses. (1) First, we used ChimeraX (Pettersen et al., 2021) to calculate the buried surface area between HA and each mutated residue in CR9114 and CR6261, using the measure buriedarea function and the default probeRadius of 1.4 angstroms to approximate a water molecule. We plot this ‘contact surface area’ vs the linear effect of the corresponding mutation on HA binding (Figure 2C; Figure 2—figure supplement 1A). (2) We used PyMol (Schrodinger, LLC, 2015) to count the number of HA residues within six angstroms of each antibody mutation site. Six angstroms was chosen as an upper limit to capture potential antibody-antigen interactions (Bondi, 1964; Baker and Hubbard, 1984; Israelachvili and Pashley, 1982; Ekiert et al., 2009; Dreyfus et al., 2012), although we note that this analysis is robust to other distance thresholds. (3) We also used PyMol to measure the distances between $\alpha$-carbons for all mutation pairs, and plotted these distances against the corresponding pairwise epistatic terms (Figure 2F; Figure 2—figure supplement 1B). We note that each of these analyses were performed with co-crystal structures of the somatic antibodies with HA (PDB ID: 4FQI (CR9114 –H5; CR9114 –H1 crystal structure not available) Dreyfus et al., 2012; 4FQY (CR9114 –H3) Dreyfus et al., 2012; 3GBN (CR6261 –H1) Ekiert et al., 2009).

### Pathway analysis

#### Selection models

To study the likelihood of various mutational pathways leading from the germline to the somatic sequence, we must assume a selection model. Selection in germinal centers is considerably more complex than in classical population genetics models, involving spatial structure, changing population sizes, and T-cell-mediated selection, among other factors (Mesin et al., 2016). Capturing these aspects in quantitative models is an active field of research (Amitai et al., 2017). However, here we wish to adopt an extremely simple model of selection as a first step in understanding the impacts of the binding affinity landscape on antibody selection, with the goal of understanding the implications of the expectation that mutational steps become more probable as their effect on binding affinity becomes more positive. Combining the more realistic models of immune selection with our detailed characterization of mutational effects on antigen binding affinity remains an interesting avenue for future work.

Here, we restrict to the weak-mutation regime where mutation fixation events occur independently of one another. Selection proceeds as a Markov process, where the population is characterized by a single sequence that acquires a single mutation at each discrete step (McCandlish, 2011). We choose a simple form for the fixation probability of a mutation from sequence $s$ to sequence $t$, as discussed below. This then determines the transition probability for the population to move from $s$ to $t$. We assume that sequences cannot back-mutate (i.e. a residue changing from the somatic allele to the germline allele), and do not acquire multiple mutations in the same step. The absence of back-mutation is justified by the relatively large number of possible mutation sites compared to the total number of mutation events.

We define the transition probability of a single mutational step from the classical fixation probability for a mutation with selection coefficient $\sigma$ in a population of size $N$(Kimura, 1962):

$$
p_{step}(\sigma,N)=\frac{1−e^{−\sigma}}{1−e^{−N\sigma}}.
$$

Here, we define the selection coefficient $\sigma$ to be proportional to the difference in log binding affinities to a particular antigen between the two sequences $s$ and $t$:

$$
\sigma=\gamma⁢Δ_{s,t}^{ag}=\gamma⁢(-log_{10}⁡K_{D,t}^{ag}-(-log_{10}⁡K_{D,s}^{ag})).
$$

This model has two tunable parameters: $N$ represents the effective population size and $\gamma$ represents how strongly differences in binding affinity impact fitness. We chose three parameter values to span a range of selection strengths (see Figure 5—figure supplement 1): moderate, with $N=1000$ and $\gamma=1$; weak, with $N=20$ and $\gamma=0.5$; and strong, with $N→∞$ and $\gamma→∞$ such that $p_{step}$ reduces to a step function (one if $Δ>0$ and 0 otherwise). These three models all show similar results, with differences between selection scenarios becoming more exaggerated with stronger selection and less exaggerated with weaker selection, as expected (see Figure 5—figure supplement 1).

From the fixation probabilities for a given parameter regime, we have the transition probability (up to a constant factor) for all sequences $s,t$ over all antigens ag,

$$
P_{s,t}^{ag}={p_{step}⁢(Δ_{s,t}^{ag},\gamma,N)if thas one more somatic mutation than s0otherwise,
$$

which we use for all the calculations described below for results presented in Figure 5 and supplements.

#### Scenario, mutation, and variant probabilities

It is particularly useful to store the probabilities $P_{s,t}^{ag}$ as (sparse) transition matrices $P^{ag}$ of dimension $2^{N}\times2^{N}$ for each antigen, where entries are nonzero only where sequence $t$ has one more somatic mutation than $s$.

First, we wish to obtain a measure of total probability for a particular antigen scenario, as shown in Figure 5E,F. We calculate this by computing the matrix product over all mutational steps $i$ for a particular sequence of antigen contexts ${ag_{1},…,ag_{L}}$:

$$
𝒫_{t⁢o⁢t}=\sumpaths(\prodstepsP_{step})=[\prodi=1LP^{ag_{i}}]_{s_{g},s_{s}},
$$

where $[⋅]_{s,s^{′}}$ corresponds to taking the matrix element in the row corresponding to variant $s$ and column corresponding to variant $s^{′}$. In the right-most term, the products are matrix operations and $s_{g}$, $s_{s}$ are respectively the indices of the germline and somatic variants.

We note that the transition probabilities $P^{ag_{i}}$ are not normalized at each step. In practice, this means that mutations are optional: many outcomes will not reach the somatic sequence and the likelihood encodes the probability of reaching the somatic state. This makes it possible to compare different scenarios, as some scenarios are more likely than others to reach the somatic state. However, because these values do not represent true probabilities — the units are arbitrary — they cannot be compared between antibodies or between selection models. The exception is for the strong scenario, where the total probability for each path is one if all steps are uphill ($Δ_{s,t}^{ag}>0$) and 0 otherwise. Thus, here $𝒫_{t⁢o⁢t}$ has a natural interpretation as the total number of uphill paths. When we present results from the strong model (Figure 5C,D, Figure 5—figure supplement 1, and numbers of uphill paths for H1-only scenarios as discussed in the text), we represent uphill path numbers on a linear scale without log-transforming.

Although there are many possible antigen exposure scenarios, we restrict our analysis to several classes. First, in single-antigen scenarios, all steps $i$ use the same antigen. Second, for sequential scenarios, antigen exposures must occur in non-repeating segments (for example, H1 - H3 - H1 is not allowed), although we consider all possible lengths and orders of segments.

Mixed scenarios are more complicated, as we do not fully understand the nature of B cell interactions with multiple antigens in the same germinal center (Wang et al., 2015; Wang, 2017; Kuraoka et al., 2016). One option is to assume that the B cell engages the antigen for which it has the highest affinity and define $Δ$ by the maximum binding affinity across all possible antigens at each step, but this definition would trivially imply that the mixed scenario has the highest probability. Instead, we choose two alternatives: first, ‘average’ mixed, where we assume the B cell engages all antigens and use the average binding affinity change over all three (for CR9114) or two (for CR6261) antigens, $Δ_{mixed}=\frac{1}{N_{ag}}⁢\sum_{ag}Δ_{ag}$; and second, ‘random’ mixed, where we assume the B cell randomly engages a single antigen and hence the antigen at each mutational step is chosen randomly. For the latter definition, we calculate $𝒫_{t⁢o⁢t}$ as described above for 1000 randomly drawn scenarios and average the resulting log probability. When we illustrate mutational paths and mutation orders, we choose a representative scenario (with close to median probability) from the 1000 random draws.

We estimate the error of these probabilities by bootstrapping. Specifically, for 10 bootstrap iterations, we resample each binding affinity $-log_{10}⁡K_{D,s}^{ag}$ from a normal distribution according to its value and standard deviation. We then recalculate the total probability $𝒫_{t⁢o⁢t}$, average over the 10 values to obtain mean and s.e.m. values, and transform by the natural log for plotting, as shown in Figure 5 and Figure 5—figure supplement 1. We note that for the strong selection scenario (where probabilities represent total numbers of uphill paths), values are not log-transformed, and many scenarios have total path numbers of exactly zero. We refrain from studying the ‘average’ mixed scenario for strong selection because it is essentially equivalent to choosing the antigen with maximum improvement: the quantitative effect of averaging is undone when the transition probability is binarized. For CR6261, all mutations at the first mutational step are neutral (with the exception of one mutation that improves affinity for H1 only), and so we allow all mutations with equal probability for the first step in the strong selection model.

Next, to identify the most likely paths under a given exposure scenario, we reframe this Markov process as a directed weighted graph. Each sequence $s$ is a node, and a directed edge exists toward all sequences $t$ that can be reached by one additional somatic mutation. The edge weight is calculated from the transition probability, $w_{s→t}=-log⁡(P_{s,t}^{ag}+ϵ)$, where $ϵ$ is an extremely small value to ensure weights are finite. In this graph framework, we can use fast algorithms to obtain the ‘shortest’ paths from the germline to the somatic node (those for which the sum of weights is lowest, that is the total probability is highest). Specifically, we use the shortest_simple_paths function from the Python package networkx (Hagberg et al., 2008) to compute the $k$ shortest paths, as shown in Figure 5G,H. This method is exact and uses the algorithm described in Yen, 1971.

Next, we wish to obtain the probability that a mutation at site $m$ happened at a specific step $j$ (Figure 5I,J). As we are focusing on one antigen context, we can normalize the transition matrices and define:

$$
P~_{s,t}^{ag}=P_{s,t}^{ag}\times(\sumtP_{s,t}^{ag})^{-1},
$$

if $P_{s,t}^{ag}\neq0$ and 0 otherwise. We can further restrict the transition matrix at step $j$, $P~^{ag_{j}}$, to have nonzero the mutation that occurs is at a particular residue $\alpha$, $P~_{\alpha}^{ag_{j}}$. The total relative probability for that site at that mutational step under an antigen exposure scenario is then

$$
℘_{j,\alpha}=[(\prodi=1j−1P~^{ag_{i}})⋅P~_{\alpha}^{ag_{j}}⋅(\prodi=j+1LP~^{ag_{i}})]_{s_{g},s_{s}},
$$

where, again, products are matrix operations. Because a sequence of $L$ steps starting from the germline can only lead to the somatic state, $P~$ verifies $[\prod_{i=1}^{L}P~^{ag_{i}}]_{s_{g},s_{s}}=1$. With the relation $\sum_{\alpha}P~_{\alpha}^{ag_{j}}=P~^{ag_{j}}$ this implies that these probabilities are already normalized: $\sum_{\alpha}𝒫_{j,\alpha}=1$.

Finally, we wish to determine the total probability of each variant (Figure 5—figure supplement 2), that is the sum of probabilities of all paths passing through that variant, for a given selection scenario. For a variant $s$ that contains $j$ somatic mutations, we calculate

$$
𝒫_{s}=([\prodi=1jP~^{ag_{i}}]_{s_{g},s})⋅([\prodi=j+1LP~^{ag_{i}}]_{s,s_{s}}),
$$

where the first term is the probability of reaching sequence $s$ at mutational step $j$, and the second term is the probability of reaching the somatic sequence after passing through sequence $s$. When representing this number we add an additional normalisation factor, $𝒫_{s}^{′}=𝒫_{s}\timesn_{j}$, where $n_{j}=(\frac{L}{j})$ is the number of sequences with $j$ mutations, so that variants with different numbers of mutations have comparable values. $𝒫_{s}^{′}$ thus represents the ratio of the probability in a selective model to the probability in a neutral model (which is $1/n_{j})$. Thus, sequences with $log_{10}⁡(𝒫_{s}^{′})>0$ are favored by the given selection scenario, and those with $log_{10}⁡(𝒫_{s}^{′})<0$ are disfavored, as shown in Figure 5—figure supplement 2 for moderate selection under the optimal sequential scenario.
