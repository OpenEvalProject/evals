# Human T cell receptor occurrence patterns encode immune history, genetic background, and receptor specificity

## Authors

- William S DeWitt<sup>1</sup> ([ORCID: 0000-0002-6802-9139](https://orcid.org/0000-0002-6802-9139))
- Anajane Smith<sup>3</sup>
- Gary Schoch<sup>3</sup>
- John A Hansen<sup>3</sup>
- Frederick A Matsen<sup>1</sup> ([ORCID: 0000-0003-0607-6025](https://orcid.org/0000-0003-0607-6025))
- Philip Bradley<sup>1</sup> ([ORCID: 0000-0002-0224-6464](https://orcid.org/0000-0002-0224-6464)) †

### Affiliations

1. Public Health Sciences Division Fred Hutchinson Cancer Research Center Seattle United States
2. Department of Genome Sciences University of Washington Seattle United States
3. Clinical Division Fred Hutchinson Cancer Research Center Seattle United States
4. Department of Medicine University of Washington Seattle United States
5. Institute for Protein Design University of Washington Seattle United States

† Corresponding author

## Abstract

The T cell receptor (TCR) repertoire encodes immune exposure history through the dynamic formation of immunological memory. Statistical analysis of repertoire sequencing data has the potential to decode disease associations from large cohorts with measured phenotypes. However, the repertoire perturbation induced by a given immunological challenge is conditioned on genetic background via major histocompatibility complex (MHC) polymorphism. We explore associations between MHC alleles, immune exposures, and shared TCRs in a large human cohort. Using a previously published repertoire sequencing dataset augmented with high-resolution MHC genotyping, our analysis reveals rich structure: striking imprints of common pathogens, clusters of co-occurring TCRs that may represent markers of shared immune exposures, and substantial variations in TCR-MHC association strength across MHC loci. Guided by atomic contacts in solved TCR:peptide-MHC structures, we identify sequence covariation between TCR and MHC. These insights and our analysis framework lay the groundwork for further explorations into TCR diversity.

## Introduction

T cells are the effectors of cell-mediated adaptive immunity in jawed vertebrates. To control a broad array of pathogens, massive genetic diversity in loci encoding the T cell receptor (TCR) is generated somatically throughout an individual’s life via a process called V(D)J recombination. All nucleated cells regularly process and present internal peptide antigens on cell surface molecules called major histocompatibility complex (MHC). Through the interface of TCR and MHC, a T cell with a TCR having affinity for a peptide antigen complexed with MHC (pMHC) is stimulated to initiate an immune response to an infected (or cancerous) cell. The responding T cell proliferates clonally, and its progeny inherit the same antigen-specific TCR, constituting long-term immunological memory of the antigen. The diverse population of TCR clones in an individual (the TCR repertoire) thus dynamically encodes a history of immunological challenges.

Advances in high-throughput TCR sequencing have shown the potential of the TCR repertoire as a personalized diagnostic of pathogen exposure history, cancer, and autoimmunity (Thomas et al., 2014; Kirsch et al., 2015; Friedensohn et al., 2017; Ostmeyer et al., 2017). Public TCRs—defined as TCR sequences seen in multiple individuals and perhaps associated with a shared disease phenotype—have been found in a range of infectious and autoimmune diseases and cancers including influenza, Epstein-Barr virus, and cytomegalovirus infections, type I diabetes, rheumatoid arthritis, and melanoma (Venturi et al., 2008; Li et al., 2012; Madi et al., 2017; Pogorelyy et al., 2017; Dash et al., 2017; Glanville et al., 2017; Chu et al., 2018; Pogorelyy et al., 2018). By correlating occurrence patterns of public TCR$\beta$ chains with cytomegalovirus (CMV) serostatus across a large cohort of healthy individuals, Emerson et al. identified a set of CMV-associated TCR chains whose aggregate occurrence was highly predictive of CMV seropositivity (Emerson et al., 2017). Staining with multimerized pMHC followed by flow cytometry has been used to isolate and characterize large populations of T cells that bind to defined pMHC epitopes (Dash et al., 2017; Glanville et al., 2017), providing valuable data on the mapping between TCR sequence and epitope specificity. We and others have leveraged these data to develop learning-based models of TCR:pMHC interactions, using TCR distance measures (Dash et al., 2017), CDR3 sequence motifs (Glanville et al., 2017) and k-mer frequencies (Cinelli et al., 2017), and other techniques.

MHC proteins in humans are encoded by the human leukocyte antigen (HLA) loci and are among the most polymorphic in the human genome (Robinson et al., 2015). Within an individual, six major antigen-presenting proteins are each encoded by polymorphic alleles. The set of these alleles comprise the individual’s HLA type, which is unlikely to be shared with an unrelated individual and which determines the subset of peptide epitopes presented to T cells for immune surveillance. Specificity of a given TCR for a given antigen is biophysically modulated by MHC structure: MHC binding specificity determines the specific antigenic peptide that is presented, and the TCR binds to a hybrid molecular surface composed of peptide- and MHC-derived residues. Thus, population-level studies of TCR-disease association are severely complicated by a dependence on individual HLA type.

Here we report an analysis of the occurrence patterns of public TCRs in a cohort of 666 healthy volunteer donors, in which information on only TCR sequence and HLA association guide us to inferences concerning disease history. To complement deep TCR$\beta$ repertoire sequencing available from a previous study (Emerson et al., 2017), we have assembled high-resolution HLA typing data at the major class I and class II HLA loci on the same cohort, as well as information on age, sex, ethnicity, and CMV serostatus. We focus on statistical association of TCR occurrence with HLA type, and show that many of the most highly HLA-associated TCRs are likely responsive to common pathogens: for example, eight of the ten TCR$\beta$ chains most highly associated with the HLA-A*02:01 allele are likely responsive to one of two viral epitopes (influenza M1$_{58}$ and Epstein-Barr virus BMLF1$_{280}$). We introduce new approaches to cluster TCRs by primary sequence and by the pattern of occurrences among individuals in the cohort, and we identify highly significant TCR clusters that may indicate markers of immunological memory. Four of the top five most significant clusters appear linked with common pathogens (parvovirus B19, influenza virus, CMV, and Epstein-Barr virus), again highlighting the impact of viral pathogens on the public repertoire. We also find HLA-unrestricted TCR clusters, some likely to be mucosal-associated invariant T (MAIT) cells, which recognize bacterial metabolites presented by non-polymorphic MR1 proteins, rather than pMHC (Kjer-Nielsen et al., 2012). Our global analysis of TCR-HLA association identifies striking variation in association strength across HLA loci and highlights trends in V(D)J generation probability and degree of clonal expansion that illuminate selection processes in cellular immunity. Guided by structural analysis, we used our large dataset of HLA-associated TCR$\beta$ chains to identify statistically significant sequence covaration between the TCR CDR3 loop and the DRB1 allele sequence that preserves charge complementarity at the TCR:pMHC interface. These analyses help elucidate the complex dependence of TCR sharing on HLA type and immune exposure, and will inform the growing number of studies seeking to identify TCR-based disease diagnostics.

## Results

### The matrix of public TCRs

Of the 80 million unique TCR$\beta$ chains (defined by V-gene family and CDR3 sequence) in the 666 cohort repertoires, about 11 million chains are found in at least two individuals and referred to here as public chains (for a more nuanced examination of TCR chain sharing see [Elhanati et al., 2018]). The occurrence patterns of these public TCR$\beta$s—the subset of subjects in which each distinct chain occurs—can be thought of as forming a very large binary matrix $M$ with about 11 million rows and 666 columns. Entry $M_{i,j}$ contains a one or a zero indicating presence or absence, respectively, of TCR $i$ in the repertoire of subject $j$ (ignoring for the moment the abundance of TCR $i$ in repertoire $j$; Figure 1 depicts two illustrative sub-matrices of $M$). (Emerson et al., 2017) demonstrated that this binary occurrence matrix $M$ encodes information on subject genotype and immune history: they were able to successfully predict HLA-A and HLA-B allele type and CMV serostatus by learning sets of public TCR$\beta$ chains with occurrence patterns that were predictive of these features. Specifically, each feature—such as the presence of a given HLA allele (e.g. HLA-A*02:01) or CMV seropositivity—defines a subset of the cohort members positive for that feature, and can be encoded as a vector of 666 binary digits. This phenotype occurrence pattern of zeros and ones can be compared to the occurrence patterns of all the public TCR$\beta$ chains to identify similar patterns, as quantified by a p-value for significance of co-occurrence across the 666 subjects; thresholding on this p-value produces a subset of significantly associated TCR$\beta$ chains whose collective occurrence in a repertoire was found by Emerson et al. to be predictive of the feature of interest (in cross-validation and, for CMV, on an independent cohort). Generalizing from these results, it is reasonable to expect that other common immune exposures may be encoded in the occurrence matrix $M$, and that these encodings could be discovered if we had additional phenotypic data to correlate with TCR occurrence patterns. In this study, we set out to discover these encoded exposures de novo, without additional phenotypic correlates, by learning directly from the structure of the occurrence matrix $M$ and using as well the sequences of the TCR$\beta$ chains (both their similarities to one another and to TCR sequences characterized in the literature). We hypothesized that patterns of TCR co-occurrence (correlations between rows in the matrix $M$) might indicate shared responses to unknown immune exposures, that co-occurrence between TCR chains and HLA alleles (correlations between rows in $M$ and rows in the HLA allele occurrence matrix) could be used to help identify functional TCR chains, and that clustering TCR$\beta$ chains by co-occurrence and sequence could highlight functional associations (Figure 1). To support this effort we assembled additional HLA typing data for the subjects, now at 4-digit resolution (e.g., A*02:01 rather than A*02) and including MHC class II alleles, and we compiled a dataset of annotated TCR$\beta$ chains by combining online TCR sequence databases, structurally characterized TCRs, and published studies (see Materials and methods; [Shugay et al., 2018; Tickotsky et al., 2017; Berman et al., 2000; Dash et al., 2017; Glanville et al., 2017; Song et al., 2017; Kasprowicz et al., 2006]). Here we describe the outcome of this discovery process, and we report a number of intriguing general observations about the role of HLA in shaping the T cell repertoire.

![Figure 1.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig1-v2.jpg)

**Figure 1.:** As described in detail in the following sections, we used covariation analysis to identify clusters of co-occurring TCR$\beta$ chains. Here we provide a graphical introduction to these results by depicting occurrence patterns of clustered TCRs over the full cohort and over a cohort subset defined by a single HLA allele (HLA-A*01:01). TCR clusters over the full cohort are largely driven by the occurrence patterns of specific HLA alleles (compare the occurrence patterns of the top five global clusters to those of the top 5 HLA alleles, respectively), whereas HLA-restricted clusters may reflect shared immune exposures, as illustrated here by a CMV-associated TCR cluster (the pink cluster in the bottom panels). In the top left panels, occurrence patterns of HLA alleles and TCR$\beta$ chains (rows) are indicated for each of the cohort subjects (columns) by filled (black) matrix elements. The TCR$\beta$ chains chosen for depiction in the occurrence matrix are the members of the $28$ global co-occurrence clusters identified in section 'Globally co-occurring TCR pairs form clusters defined by shared associations'. The TCRs (rows) are ordered by cluster membership as indicated by colored bands to the left of the matrix. The selected HLA alleles correspond to the strongest associations for the top $10$ clusters (two of which are not HLA-associated). The cohort subjects are ordered by column similarity so as to emphasize block structure present in the matrix. The bottom left panels similarly show occurrence patterns for HLA-A*01:01-associated TCR$\beta$ chain clusters over the subset of subjects carrying this allele, alongside an indicator of cytomegalovirus seropositivity for each subject (red). In-depth analysis of these (and other) HLA-associated TCR$\beta$ clusters is presented in section 'HLA-restricted TCR clusters'. For visualization purposes, two-dimensional embeddings of the TCR$\beta$ chains based on their occurrence patterns (binary strings representing presence/absence in the subjects) are depicted in the right panels, with the TCR chains colored by cluster assignment and annotated by known associations.

The results of our analysis are organized in the remaining five sections as follows. We begin with an examination of TCR co-occurrence patterns across the full cohort (first section, Figures 2–3). In the next section we examine patterns of TCR-HLA association (Table 1 and Figures 4–5). In the third section we analyze TCR co-occurrence within subsets of the cohort positive for specific HLA alleles, and we identify TCR clusters that may be reflective of shared immune exposures (Figures 6–8). In the fourth section we use our dataset of HLA-associated TCR$\beta$ chains to identify covariation between HLA and the TCR$\beta$ CDR3 sequence (Table 2 and Figure 9). In the final section we focus on CMV-responsive TCR$\beta$ chains, examining their degree of HLA-restriction and the extent to which they may be responding to other antigens (Figure 10). Figure 1 provides a graphical overview of the co-occurrence analysis.

### Globally co-occurring TCR pairs form clusters defined by shared associations

We hypothesized that we could identify unknown immune exposures encoded in the public repertoire by comparing the occurrence patterns of individual TCR$\beta$ chains to one another. A subset of TCR$\beta$ chains that strongly co-occur across the 666 cohort subjects might correspond to an unmeasured immune exposure that is common to a subset of subjects. Since shared HLA restriction could represent an alternative explanation for significant TCR co-occurrence, we also compared the TCR occurrence patterns to the occurrence patterns for class I and class II HLA alleles. We began by analyzing TCR occurrence patterns over the full set of cohort members. For each pair of public TCR$\beta$ chains $t_{1}$ and $t_{2}$ we computed a co-occurrence p-value $P_{CO}(t_{1},t_{2})$ that reflects the probability of seeing an equal or greater overlap of shared subjects (i.e., subjects in whose repertoires both $t_{1}$ and $t_{2}$ are found) if the occurrence patterns of the two TCRs had been chosen randomly (for details, see Materials and methods and Figure 12). In a similar manner we computed, for each HLA allele $a$ and TCR $t$, an association p-value $P_{HLA}(a,t)$ that measures the degree to which TCR $t$ tends to occur in subjects positive for allele $a$. Finally, for each pair of strongly co-occurring ($P_{CO}<1\times10^{−8}$) TCR$\beta$ chains $t_{1}$ and $t_{2}$, we looked for a mutual HLA association that might explain their co-occurrence, by finding the allele having the strongest association with both $t_{1}$ and $t_{2}$, and noting its association p-value:

$$
P_{HLA}(t_{1},t_{2})=mina\inAmaxt\in{t_{1},t_{2}}P_{HLA}(a,t),
$$

where $A$ denotes the set of all HLA alleles. In words, we take the p-value of the strongest HLA allele association with the TCR pair, where the association of an HLA allele with a TCR pair is defined by the weakest association of the allele among the individual TCRs.

Based on this analysis, we identified two broad classes of strongly co-occurring TCR pairs (Figure 2): those with a highly significant shared HLA association, where the co-occurrence of the two TCRs can be explained by a shared HLA allele association (i.e. a common HLA restriction), and those with only modest shared HLA-association p-value, for which another explanation of co-occurrence must be sought. Points above the dashed $y=x$ line correspond to pairs of TCRs for which there exists an HLA allele whose co-occurrence with each of the TCRs is stronger than their mutual co-occurrence, while for points below the line no such HLA allele was present in the dataset.

![Figure 2.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig2-v2.jpg)

**Figure 2.:** The co-occurrence p-value $P_{CO}$ for each pair of public TCRs is plotted ($x$-axis) against the HLA-association p-value $P_{HLA}$ for the HLA allele with the strongest mutual association with that TCR pair ($y$-axis). There are $6092$ TCR-pairs above the diagonal ($y=x$) and $4713$ pairs below the diagonal.

We used a neighbor-based clustering algorithm, DBSCAN (Ester et al., 1996), to link strongly co-occurring TCR pairs together to form larger correlated clusters (see Materials and methods), and then investigated phenotype associations with these clusters. At an approximate family-wise error rate of $0.05$ (see Materials and methods), we identified 28 clusters of co-occurring TCRs, with sizes ranging from 7 to 386 TCRs (Figure 3). Given one of these clusters of co-occurring TCRs, we can count the number of cluster member TCRs found in each subject’s repertoire. The aggregate occurrence pattern of the cluster can be visualized as a rank plot of this cluster TCR count over the subjects (the black curves in Figure 3C–D). This ranking can also be compared with other phenotypic or genotypic features of the same subjects. In particular, by comparing this aggregate occurrence pattern to a control pattern generated by repeatedly choosing equal numbers of subjects independently at random (dotted green lines in Figure 3C–D), we can identify a subset of the cohort with an apparent enrichment of cluster member TCRs and look for overlap between this subset and other defined cohort features. Performing this comparison against the occurrence patterns of class I and class II HLA alleles revealed that the majority of the TCR clusters were strongly associated with at least one HLA allele (as depicted for a DRB1*15:01-associated cluster in Figure 3C and summarized in Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig3-v2.jpg)

**Figure 3.:** Clustering public TCR$\beta$ chains by co-occurrence over the full cohort identifies associations with HLA and TRBJ alleles as well as an invariant T cell subset.(A) Graphical representations of the TCR$\beta$ chain occurrence matrix (lower left) and the HLA-allele occurrence matrix (upper left), restricted to members of the $28$ global co-occurrence TCR clusters and the associated HLA alleles for the top $10$ clusters, respectively. TCR$\beta$ chains (rows) are ordered by cluster membership and subjects (columns) are ordered by column similarity (Jaccard distance of TCR sets) to emphasize block structure present in the matrix. (B) Cluster size ($x$-axis) versus the p-value of the most significant HLA allele association ($y$-axis), with markers colored according to the locus of the associated allele. Dashed line indicates random expectation based on the total number of alleles, assuming independence. (C) Count of cluster member TCRs found in each subject for the cluster labeled ‘2’ in panel (B) (top right). The dotted line represents an averaged curve based on randomly and independently selecting subject sets for each member TCR. Red and blue dots indicate the occurrence of the DRB1*15:01 allele in the cohort. (D) Count of cluster member TCRs found in each subject for the cluster labeled ‘7’ in panel (B) (center bottom). The dotted line again represents a control pattern, and the red and blue dots indicate the occurrence of the TRBJ2-7*02 allele.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** TCRdist tree of the members of the TRBJ2-7*02-associated cluster. Average-linkage dendrogram of TCRdist receptor clusters colored by generation probability ($P_{gen}$), with TCR logos for selected receptor subsets (the branches of the tree enclosed in dashed boxes labelled with size of the TCR clusters). Each logo depicts the V- (left side) and J- (right side) gene frequencies, CDR3 amino acid sequences (middle), and inferred rearrangement structure (bottom bars coloured by source region, light grey for the V-region, dark grey for J, black for D, and red for N-insertions) of the grouped receptors.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** TCRdist tree of the members of the putative MAIT cell cluster. Average-linkage dendrogram of TCRdist receptor clusters colored by generation probability ($P_{gen}$), with TCR logos for selected receptor subsets (the branches of the tree enclosed in dashed boxes labelled with size of the TCR clusters). Each logo depicts the V- (left side) and J- (right side) gene frequencies, CDR3 amino acid sequences (middle), and inferred rearrangement structure (bottom bars coloured by source region, light grey for the V-region, dark grey for J, black for D, and red for N-insertions) of the grouped receptors.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** More details on the MAIT cell cluster: subject age and N-nucleotide insertion distributions; TCR$\alpha$ chains paired with cluster member TCR$\beta$ chains in the pairSEQ dataset of (Howie et al., 2015).Further details on the putative MAIT cell TCR cluster. (A) Distribution of N-nucleotide insertions for TCR$\beta$ chains in the MAIT cluster (red), in the DRB1*15-associated cluster (green), and in the union of the members of the top 10 clusters (excluding the members of the MAIT cluster, blue). MAIT cell cluster members have very few N-insertions relative to the members of the other clusters. (B) Subjects enriched for MAIT cluster TCRs (red curve) are younger than the cohort as a whole (blue curve), a trend that is further strengthened in the top half of the enriched subjects by member-TCR count (the ‘high-count subjects’, magenta curve). (C) TCR$\alpha$ chains paired with MAIT cluster TCR$\beta$ chains in the pairSEQ dataset of (Howie et al., 2015). Ten of the 36 paired TCR$\alpha$ chains match the MAIT sequence consensus (TRAV1-2, TRAJ20 or TRAJ33, and a 12 residue CDR3, enclosed in the blue box).

In addition, there were two large clusters of TCRs which were not strongly associated with any of the typed HLA alleles (clusters $6$ and $7$ in Figure 3). Visual inspection of the CDR3 regions of TCRs in one of these clusters revealed a distinctive ‘YV’ C-terminal motif that is characteristic of the TRBJ2-7*02 allele (Figure 3—figure supplement 1), and indeed the 41 subjects whose repertoires indicated the presence of this genetic variant were exactly the 41 subjects enriched for members of this TCR cluster (Figure 3D). This demonstrated that population diversity in germline allele sets manifests as occurrence pattern clustering. The other large, non-HLA associated TCR cluster had a number of distinctive features as well: strong preference for the TRBV06 family, followed by TRBV20 and TRBV04 (Figure 3—figure supplement 2); low numbers of inserted ‘N’ nucleotides; and a skewed age distribution biased toward younger subjects (Figure 3—figure supplement 3). These features, together with the lack of apparent HLA restriction, suggested that this cluster represented an invariant T cell subset, specifically MAIT (mucosal-associated invariant T) cells (Kjer-Nielsen et al., 2012; Venturi et al., 2013; Pogorelyy et al., 2017). Since MAIT cells are defined primarily by their alpha chain sequences, we searched in a recently published paired dataset (Howie et al., 2015) for partner chains of the clustered TCR$\beta$ chain sequences, and found a striking number that matched the MAIT consensus (TRAV1-2 paired with TRAJ20/TRAJ33 and a 12 residue CDR3, Figure 3—figure supplement 3D). We also looked for these clustered TCRs in a recently published MAIT cell sequence dataset (Howson et al., 2018) and found that 93 of the 138 cluster member TCRs occurred among the 31,654 unique TCRs from this dataset; of these 93 TCR$\beta$ chains, 27 were found among the 78 most commonly occurring TCRs in the dataset (the TCRs occurring in at least 7 of the 24 sequenced repertoires), a highly significant overlap ($P<2\times10^{−52}$ in a one-sided hypergeometric test). These concordances indicate that our untargeted approach has detected a well-studied T cell subset de novo through analysis of occurrence patterns.

### HLA-associated TCRs

These analyses suggested to us that TCR co-occurrence patterns across the full cohort of subjects are strongly influenced by the distribution of the HLA alleles, in accordance with the expectation that the majority of $\alpha\beta$ TCRs are HLA-restricted. Covariation between TCRs responding to the same HLA-restricted epitopes would only be expected in subjects positive for the restricting alleles, with TCR presence and absence outside these subjects likely introducing noise into the co-occurrence analysis. We therefore decided to analyze patterns of TCR co-occurrence within subsets of the cohort positive for specific HLA alleles, and to restrict our co-occurrence analysis to TCRs having a statistically significant association with the specific allele defining the cohort subset. To begin, we performed a comprehensive analysis of TCR-HLA association.

At a false discovery rate of 0.05 (estimated from shuffling experiments; see Materials and methods), we were able to assign 16,951 TCR$\beta$ sequences to an HLA allele (or alleles: DQ and DP alleles were analyzed as $\alpha\beta$ pairs, and there were 5 DR/DQ haplotypes whose component alleles were so highly correlated across our cohort that we could not assign TCR associations to individual DR or DQ components; see Materials and methods). Table 1 lists the top 50 HLA-associated TCR sequences by association p-value and top 10 associated TCRs for the well-studied A*02:01 allele.

**Table 1.**
 The top 50 most significant HLA-associated public TCR$\beta$ chains and the top 10 for A*02:01 (indicated in bold).


<table>
  <thead>
    <tr>
      <th>Association p-value</th>
      <th>Overlap*</th>
      <th>TCR Subjects †</th>
      <th>HLA subjects‡</th>
      <th>Total subjects§</th>
      <th>V-family</th>
      <th>CDR3</th>
      <th>HLA allele#</th>
      <th>Epitope annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3.7e-90</td>
      <td>231</td>
      <td>267</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV19</td>
      <td>CASSIRSSYEQYF</td>
      <td>A*02:01</td>
      <td>Influenza virus</td>
    </tr>
    <tr>
      <td>2.4e-72</td>
      <td>179</td>
      <td>191</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV29</td>
      <td>CSVGTGGTNEKLFF</td>
      <td>A*02:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>3.8e-66</td>
      <td>107</td>
      <td>124</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV20</td>
      <td>CSARNRDYGYTF</td>
      <td>DRB1*03:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>1.9e-65</td>
      <td>92</td>
      <td>95</td>
      <td>151</td>
      <td>630</td>
      <td>TRBV05</td>
      <td>CASSLVVSPYEQYF</td>
      <td>DRB1*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>6.7e-64</td>
      <td>91</td>
      <td>94</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV30</td>
      <td>CAWSRDSGSGNTIYF</td>
      <td>DRB1*15:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>7.5e-59</td>
      <td>51</td>
      <td>53</td>
      <td>66</td>
      <td>630</td>
      <td>TRBV15</td>
      <td>CATSREEGDGYTF</td>
      <td>B*35:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.6e-57</td>
      <td>89</td>
      <td>96</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV11</td>
      <td>CASSPGQGPGNTIYF</td>
      <td>DRB1*15:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>7.4e-56</td>
      <td>57</td>
      <td>57</td>
      <td>95</td>
      <td>630</td>
      <td>TRBV02</td>
      <td>CASSENQGSQPQHF</td>
      <td>DRB1*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.5e-52</td>
      <td>86</td>
      <td>87</td>
      <td>184</td>
      <td>629</td>
      <td>TRBV06</td>
      <td>CASSYDSGTGELFF</td>
      <td>C*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.3e-52</td>
      <td>136</td>
      <td>143</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV19</td>
      <td>CASSIRSAYEQYF</td>
      <td>A*02:01</td>
      <td>Influenza virus</td>
    </tr>
    <tr>
      <td>1.2e-51</td>
      <td>71</td>
      <td>96</td>
      <td>94</td>
      <td>630</td>
      <td>TRBV27</td>
      <td>CASSLGGQNYGYTF</td>
      <td>B*44:02</td>
      <td></td>
    </tr>
    <tr>
      <td>1.8e-50</td>
      <td>52</td>
      <td>52</td>
      <td>94</td>
      <td>630</td>
      <td>TRBV28</td>
      <td>CASSSSPLNYGYTF</td>
      <td>DRB1*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.8e-49</td>
      <td>69</td>
      <td>71</td>
      <td>142</td>
      <td>630</td>
      <td>TRBV04</td>
      <td>CASSPGQGEGYEQYF</td>
      <td>B*08:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>6.3e-49</td>
      <td>92</td>
      <td>98</td>
      <td>189</td>
      <td>629</td>
      <td>TRBV11</td>
      <td>CASSFGQMNTEAFF</td>
      <td>A*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.3e-48</td>
      <td>73</td>
      <td>75</td>
      <td>156</td>
      <td>630</td>
      <td>TRBV18</td>
      <td>CASSPPTESYGYTF</td>
      <td>B*07:02</td>
      <td></td>
    </tr>
    <tr>
      <td>3.2e-48</td>
      <td>79</td>
      <td>87</td>
      <td>151</td>
      <td>630</td>
      <td>TRBV14</td>
      <td>CASSQAGMNTEAFF</td>
      <td>DRB1*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>8.7e-47</td>
      <td>49</td>
      <td>49</td>
      <td>95</td>
      <td>630</td>
      <td>TRBV11</td>
      <td>CASSLDQGGSSSYNEQFF</td>
      <td>DRB1*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.2e-46</td>
      <td>50</td>
      <td>51</td>
      <td>95</td>
      <td>630</td>
      <td>TRBV20</td>
      <td>CSAQREYNEQFF</td>
      <td>DRB1*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.3e-46</td>
      <td>68</td>
      <td>69</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV05</td>
      <td>CASSFWGRDTQYF</td>
      <td>DRB1*03:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>3.3e-46</td>
      <td>54</td>
      <td>59</td>
      <td>94</td>
      <td>630</td>
      <td>TRBV05</td>
      <td>CASSWTGGGGANVLTF</td>
      <td>DRB1*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.1e-45</td>
      <td>54</td>
      <td>60</td>
      <td>94</td>
      <td>630</td>
      <td>TRBV02</td>
      <td>CASSEARGAGQPQHF</td>
      <td>DRB1*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.4e-44</td>
      <td>41</td>
      <td>42</td>
      <td>69</td>
      <td>630</td>
      <td>TRBV14</td>
      <td>CASSPLGPGNTIYF</td>
      <td>DRB1*11:01</td>
      <td></td>
    </tr>
    <tr>
      <td>2.4e-43</td>
      <td>92</td>
      <td>121</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV07</td>
      <td>CASSPTGLQETQYF</td>
      <td>DRB1*03:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>4.1e-43</td>
      <td>43</td>
      <td>52</td>
      <td>61</td>
      <td>630</td>
      <td>TRBV19</td>
      <td>CASSPTGGIYEQYF</td>
      <td>B*44:03</td>
      <td>Multiple sclerosis</td>
    </tr>
    <tr>
      <td>4.5e-43</td>
      <td>39</td>
      <td>40</td>
      <td>66</td>
      <td>629</td>
      <td>TRBV10</td>
      <td>CASSESPGNSNQPQHF</td>
      <td>C*12:03</td>
      <td></td>
    </tr>
    <tr>
      <td>6.7e-43</td>
      <td>76</td>
      <td>86</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV28</td>
      <td>CASRGRPEAFF</td>
      <td>DRB1*15:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>7.5e-43</td>
      <td>50</td>
      <td>54</td>
      <td>94</td>
      <td>630</td>
      <td>TRBV19</td>
      <td>CASSPTQNTEAFF</td>
      <td>DRB1*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.7e-42</td>
      <td>84</td>
      <td>110</td>
      <td>142</td>
      <td>630</td>
      <td>TRBV07</td>
      <td>CASSSGPNYEQYF</td>
      <td>B*08:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.7e-42</td>
      <td>61</td>
      <td>81</td>
      <td>95</td>
      <td>630</td>
      <td>TRBV05</td>
      <td>CASSFPGEDTQYF</td>
      <td>DRB1*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.3e-41</td>
      <td>47</td>
      <td>49</td>
      <td>95</td>
      <td>630</td>
      <td>TRBV18</td>
      <td>CASSPPAGAAYEQYF</td>
      <td>DRB1*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.5e-41</td>
      <td>75</td>
      <td>87</td>
      <td>151</td>
      <td>630</td>
      <td>TRBV28</td>
      <td>CASSLTSGGQETQYF</td>
      <td>DRB1*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>2.3e-41</td>
      <td>64</td>
      <td>67</td>
      <td>151</td>
      <td>630</td>
      <td>TRBV07</td>
      <td>CASSLGQGFYNSPLHF</td>
      <td>DRB1*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>8.2e-40</td>
      <td>77</td>
      <td>92</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV19</td>
      <td>CASSISVYGYTF</td>
      <td>DRB1*15:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>2.4e-39</td>
      <td>43</td>
      <td>54</td>
      <td>66</td>
      <td>630</td>
      <td>TRBV10</td>
      <td>CAISTGDSNQPQHF</td>
      <td>B*35:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>3.4e-39</td>
      <td>115</td>
      <td>193</td>
      <td>156</td>
      <td>630</td>
      <td>TRBV09</td>
      <td>CASSGNEQFF</td>
      <td>B*07:02</td>
      <td></td>
    </tr>
    <tr>
      <td>9.5e-39</td>
      <td>151</td>
      <td>260</td>
      <td>189</td>
      <td>629</td>
      <td>TRBV19</td>
      <td>CASSIRDSNQPQHF</td>
      <td>A*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.2e-38</td>
      <td>100</td>
      <td>103</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV20</td>
      <td>CSARDGTGNGYTF</td>
      <td>A*02:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>1.3e-38</td>
      <td>56</td>
      <td>60</td>
      <td>130</td>
      <td>629</td>
      <td>TRBV25</td>
      <td>CASSEYSLTDTQYF</td>
      <td>C*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>2.1e-38</td>
      <td>109</td>
      <td>116</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV20</td>
      <td>CSARDRTGNGYTF</td>
      <td>A*02:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>2.3e-38</td>
      <td>102</td>
      <td>106</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV19</td>
      <td>CASSVRSSYEQYF</td>
      <td>A*02:01</td>
      <td>Influenza virus</td>
    </tr>
    <tr>
      <td>6.4e-38</td>
      <td>54</td>
      <td>54</td>
      <td>151</td>
      <td>630</td>
      <td>TRBV10</td>
      <td>CAISESQDLNTEAFF</td>
      <td>DRB1*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.1e-37</td>
      <td>43</td>
      <td>45</td>
      <td>94</td>
      <td>630</td>
      <td>TRBV07</td>
      <td>CASSLAGPPNSPLHF</td>
      <td>DRB1*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>1.2e-37</td>
      <td>44</td>
      <td>60</td>
      <td>66</td>
      <td>630</td>
      <td>TRBV09</td>
      <td>CASSARTGELFF</td>
      <td>B*35:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>3.3e-37</td>
      <td>79</td>
      <td>88</td>
      <td>189</td>
      <td>629</td>
      <td>TRBV19</td>
      <td>CASSIDGEETQYF</td>
      <td>A*01:01</td>
      <td></td>
    </tr>
    <tr>
      <td>5.4e-37</td>
      <td>64</td>
      <td>70</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV05</td>
      <td>CASSLESPNYGYTF</td>
      <td>DRB1*03:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>2.0e-36</td>
      <td>38</td>
      <td>43</td>
      <td>69</td>
      <td>630</td>
      <td>TRBV06</td>
      <td>CASGAGHTDTQYF</td>
      <td>DRB1*11:01</td>
      <td></td>
    </tr>
    <tr>
      <td>2.9e-36</td>
      <td>54</td>
      <td>55</td>
      <td>151</td>
      <td>630</td>
      <td>TRBV05</td>
      <td>CASSLVVQPYEQYF</td>
      <td>DRB1*07:01</td>
      <td></td>
    </tr>
    <tr>
      <td>3.3e-36</td>
      <td>57</td>
      <td>81</td>
      <td>95</td>
      <td>630</td>
      <td>TRBV11</td>
      <td>CASSPGQDYGYTF</td>
      <td>DRB1*04:01</td>
      <td></td>
    </tr>
    <tr>
      <td>2.4e-35</td>
      <td>50</td>
      <td>53</td>
      <td>109</td>
      <td>522</td>
      <td>TRBV27</td>
      <td>CASNRQGPNTEAFF</td>
      <td>DQB1*03:01-DQA1*05:05</td>
      <td></td>
    </tr>
    <tr>
      <td>5.7e-35</td>
      <td>75</td>
      <td>95</td>
      <td>134</td>
      <td>522</td>
      <td>TRBV18</td>
      <td>CASSGQANTEAFF</td>
      <td>DRB1*03:01-DQ</td>
      <td></td>
    </tr>
    <tr>
      <td>2.2e-33</td>
      <td>86</td>
      <td>88</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV14</td>
      <td>CASSQSPGGTQYF</td>
      <td>A*02:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
    <tr>
      <td>1.8e-32</td>
      <td>84</td>
      <td>86</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV10</td>
      <td>CASSEDGMNTEAFF</td>
      <td>A*02:01</td>
      <td></td>
    </tr>
    <tr>
      <td>4.3e-32</td>
      <td>86</td>
      <td>89</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV05</td>
      <td>CASSLEGQASSYEQYF</td>
      <td>A*02:01</td>
      <td>Melanoma</td>
    </tr>
    <tr>
      <td>4.3e-32</td>
      <td>86</td>
      <td>89</td>
      <td>268</td>
      <td>629</td>
      <td>TRBV29</td>
      <td>CSVGSGGTNEKLFF</td>
      <td>A*02:01</td>
      <td>Epstein-Barr virus</td>
    </tr>
  </tbody>
</table>

_*Number of subjects positive for both the TCRβ chain and the indicated HLA allele.†Number of subjects positive for the TCRβ chain with available HLA typing at the corresponding locus.‡Number of subjects positive for the indicated HLA allele.§Total number of subjects with available HLA typing at the corresponding locus.#The following DR-DQ haplotype abbreviations are used: DRB1*03:01-DQ (DRB1*03:01-DQA1*05:01-DQB1*02:01) and DRB1*15:01-DQ (DRB1*15:01-DQA1*01:02-DQB1*06:02)._

We find that 8 of the top 10 A*02:01-associated TCRs have been previously reported and annotated as being responsive to viral epitopes, specifically influenza M1$_{58}$ and Epstein-Barr virus (EBV) BMLF1$_{280}$ (Shugay et al., 2018; Tickotsky et al., 2017). Moreover, each of these 8 TCR$\beta$ chains is present in a recent experimental dataset (Dash et al., 2017) that included tetramer-sorted TCRs positive for these two epitopes; each TCR has a clear similarity to one of the consensus epitope-specific repertoire clusters identified in that work, with the EBV TRBV20, TRBV29, and TRBV14 TCRs, respectively, matching the three largest branches of the BMLF1$_{280}$ TCR tree, and the three influenza M1$_{58}$ TCRs all matching the dominant TRBV19 ‘RS’ motif consensus (Figure 4—figure supplement 2). TCRs with annotation matches are sparser in the top 50 across all other alleles, which is likely due in part to a paucity of experimentally characterized non-A*02 TCRs, however we again see EBV-epitope responsive TCRs (with B*08:01 and B*35:01 restriction).

A global comparison of TCR feature distributions for HLA-associated versus non-HLA-associated TCRs provides further evidence of functional selection. As shown in Figure 4A, HLA-associated TCRs are on average more clonally expanded than a set of background, non-HLA associated TCRs with matching frequencies in the cohort. They also have lower generation probabilities—are harder to make under a simple random model of the VDJ rearrangement process—which suggests that their observed cohort frequencies may be elevated by selection (Figure 4B, see Materials and methods for further details on the calculation of clonal expansion indices and generation probabilities; also see (Pogorelyy et al., 2018)). Examination of two-dimensional feature distributions suggests that these shifts are correlated, with HLA-associated TCRs showing an excess of lower-probability, clonally expanded TCRs (Figure 4C); this trend appears stronger for class-I associated TCRs than for class II-associated TCRs (Figure 4—figure supplement 1).

![Figure 4.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig4-v2.jpg)

**Figure 4.:** (A) Comparison of clonal expansion index distributions for the set of HLA-associated TCRs (blue) and a cohort-frequency matched set of non HLA-associated TCRs (green). (B) Comparison of VDJ-rearrangement TCR generation probability ($P_{gen}$) distributions for the set of HLA-associated TCRs (blue) and a cohort-frequency matched set of non HLA-associated TCRs (green). (C) Two-dimensional probability density function (PDF) for the distribution of $P_{gen}$ versus clonal expansion index for HLA-associated TCRs. Contours indicate level sets of the PDF. (D) Two-dimensional probability density function (PDF) for the distribution of $P_{gen}$ versus clonal expansion index for background (non HLA-associated) TCRs whose cohort frequencies match the TCRs in (C).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Two-dimensional distributions of TCR generation probability ($x$-axis, $P_{gen}$) and clonal expansion index ($y$-axis) for TCRs with the indicated HLA associations (panel headers), and for a background set of non-HLA associated, cohort-frequency matched TCRs.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** TCRdist trees of experimentally determined pathogen-responsive TCR$\beta$ chains for two immunodominant epitopes, EBV BMLF1$_{280}$ and influenza M1$_{58}$, for comparison with TCR$\beta$ chains listed in Table 1.TCRdist trees of experimentally determined pathogen-responsive TCR$\beta$ chains for two immunodominant epitopes, EBV BMLF1$_{280}$ and influenza M1$_{58}$. TCR beta chain sequences were taken from the dataset of (Dash et al., 2017). On the right-hand side are average-linkage dendrograms of TCRdist receptor clusters colored by generation probability ($P_{gen}$). TCR logos for selected receptor subsets (the branches of the tree enclosed in dashed boxes labelled with size of the TCR clusters) are shown on the left. Each logo depicts the V- (left side) and J- (right side) gene frequencies, CDR3 amino acid sequences (middle), and inferred rearrangement structure (bottom bars coloured by source region, light grey for the V-region, dark grey for J, black for D, and red for N-insertions) of the grouped receptors.

To give a global picture of TCR-HLA association, we counted the number of significant TCR associations found for each HLA allele in the dataset, and plotted this number against the number of subjects in the cohort with that allele (Figure 5). As expected, the more common HLA alleles have on average greater numbers of associated TCRs (since greater numbers of subjects permit the identification of more public TCRs, and the statistical significance assigned to an observed association of fixed strength grows as the number of subjects increases). What was somewhat more surprising is that the slope of the correlation between cohort frequency and number of associated TCRs varied dramatically among the HLA loci, with HLA-DRB1 alleles having the largest number of associated TCRs for a given allele frequency and HLA-C alleles having the smallest. The best-fit slope for the five DR/DQ haplotypes (12.2) was roughly the sum of the DR (7.99) and DQ (3.39) slopes, suggesting as expected that these haplotypes were capturing TCRs associated with both the DR and DQ component alleles. The smaller rate of TCR association observed at the HLA-C locus could be explained by a relatively lower level of cell surface expression of HLA-C alleles as well as their greater tendency to interact with killer cell immunoglobulin-like receptors (KIR) on natural killer (NK) cells (Kaur et al., 2017).

![Figure 5.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig5-v2.jpg)

**Figure 5.:** The number of HLA-associated TCRs ($y$-axis) is plotted as a function of allele frequency in the cohort ($x$-axis). Best fit lines are shown for each locus and also for the set of five DR/DQ haplotypes (‘DRDQ’) which could not be separated into component alleles in this cohort. The following DR-DQ haplotype abbreviations are used: DRB1*03:01-DQ (DRB1*03:01-DQA1*05:01-DQB1*02:01), DRB1*15:01-DQ (DRB1*15:01-DQA1*01:02-DQB1*06:02), and DRB1*13:01-DQ (DRB1*13:01-DQA1*01:03-DQB1*06:03).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** HLA class associations are concordant with CD4/CD8 assignments based on independent repertoire data. For each HLA-associated TCR$\beta$ chain, we counted the number of times it was seen in CD4+ versus CD8+ T cell repertoires from independent datasets (see Materials and methods). Given a threshold on the difference between these two counts, we assign as CD4+ (CD8+) all TCR$\beta$s whose CD4+ (CD8+) count exceeds its CD8+ (CD4+) count by at least that threshold and then calculate the fraction of TCR$\beta$s assigned to the ‘correct’ class (CD8+ for class I-associated TCR$\beta$s and CD4+ for class II-associated TCR$\beta$s). We can further stratify these accuracies by conditioning on the p-value of the HLA-association and plot them according to this p-value threshold (vertical axis; $7.5\times10^{−6}$ corresponds to the approximate FDR threshold of $0.05$ used to define HLA-associated TCRs) and the threshold on the CD4 vs CD8 counts difference (horizontal axis). In total, $6808$ HLA-associated TCR$\beta$ chains occurred in at least one of the independent repertoire datasets.

We assessed the accuracy of our TCR:HLA associations in two ways. First, we compared our HLA allele assignments to those given in the VDJdb database (which provides the peptide:MHC target and hence a putative HLA restriction for all entries; [Shugay et al., 2018]) and found that 90% of the VDJdb assignments for TCR$\beta$ chains present in both sets matched our associations. This agreement increases to 96% after filtering for the highest level of supporting evidence (VDJdb score of 3). Interestingly, two of the mismatches with VDJdb score three were from the protein structural database: the allo-complex between the B*08-restricted LC13 TCR and HLA-B*44:05 (Macdonald et al., 2009), and the structure of the A*02-restricted JM22 TCR bridged to a class II allele by a staphylococcal superantigen (Saline et al., 2010). In both of these cases, our data predict the canonical association: B*08 for the LC13 TCR$\beta$ chain and A*02 for the JM22 TCR$\beta$ chain. Second, we looked for HLA-associated public TCR$\beta$ chains in sequenced repertoires from T cell populations that were sorted for the presence of CD4/CD8 surface markers. One would expect that TCR$\beta$ chains associated with class I MHC molecules should be preferentially found in CD8+ populations, while class II-associated TCRs should be found in CD4+ populations. We selected four repertoire datasets (Emerson et al., 2013; Rubelt et al., 2016; Li et al., 2016; Oakes et al., 2017) with matched CD4+ and CD8+ repertoires from a total of $63$ individuals, and we analyzed the occurrence patterns of our HLA-associated TCR$\beta$ chains in these sequence datasets, producing for each TCR$\beta$ counts of the number of CD4+ and CD8+ repertoires it was observed in. Figure 5—figure supplement 1 shows that if we assign each TCR$\beta$ to the class (CD4+ or CD8+) with the higher count, these assignments are largely concordant with the MHC class of its associated HLA allele, and moreover this agreement increases as we increase either the stringency of HLA association or the stringency of the CD4/CD8 assignment (i.e., the minimum absolute difference between the CD4 and CD8 repertoire counts; see Materials and methods).

### HLA-restricted TCR clusters

Having identified a set of HLA-associated TCR$\beta$ chains, we next sought to identify TCR clusters that might represent HLA-restricted responses to shared immune exposures. We performed this analysis for each HLA allele individually, restricting our clustering to the set of TCR chains significantly-associated with that allele and comparing occurrence patterns only over the subset of subjects positive for that allele. To reduce spurious co-occurrence signals driven by the presence/absence of other HLA alleles, we excluded TCR chains that were more strongly associated with a different HLA allele (i.e., not the one defining the cohort subset). The smaller size of many of these allele-positive cohort subsets reduces our statistical power to detect significant clusters using co-occurrence information. To counter this effect, we used the TCRdist similarity measure (Dash et al., 2017) to leverage the TCR sequence similarity which is often present within epitope-specific responses (Dash et al., 2017; Glanville et al., 2017) (see for example the A*02:01 TCRs in Table 1 and Figure 4—figure supplement 2). We augmented the probabilistic similarity measure used to define neighbors for DBSCAN clustering to incorporate information about TCR sequence similarity (as measured by TCRdist), in addition to cohort co-occurrence (see Materials and methods). We independently clustered each allele’s associated TCRs and merged the clustering results from all alleles; using the Holm multiple testing criterion (Holm, 1979) to limit the approximate family-wise error rate to 0.05, we found a total of $78$ significant TCR clusters.

We analyzed the sequences and occurrence patterns of the TCRs belonging to these 78 clusters in order to assess their potential biological significance and prioritize them for further study (Table 3). Each cluster was assigned two scores (Figure 6): a size score ($S_{size}$, $x$-axis), reflecting the significance of seeing a cluster of that size given the total number of TCRs clustered for its associated allele, and a co-occurrence score ($Z_{CO}$, $y$-axis), reflecting the degree to which the TCRs in that cluster co-occur within its allele-positive cohort subset (see Materials and methods). In computing the co-occurrence score, we defined a subset of individuals with an apparent enrichment for the member TCRs in each cluster; the size of this enriched subset of subjects is given in the ‘Subjects’ column in Table 3. We rank ordered the 78 clusters based on the sum of their size and co-occurrence scores (weighted to equalize dynamic range); the top five clusters are presented in greater detail in Figure 7 and Figure 8. HLA associations, member TCR and enriched subject counts, cluster center TCR sequences, scores, and annotations for all 78 clusters are given in Table 3.

![Figure 6.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig6-v2.jpg)

**Figure 6.:** Many HLA-restricted TCR clusters contain TCR$\beta$ chains annotated as pathogen-responsive.Each point represents one of the $78$ significant HLA-restricted TCR clusters, plotted based on a normalized cluster size score ($S_{size}$, $x$-axis) and an aggregate TCR co-occurrence score for the member TCRs ($Z_{CO}$, $y$-axis). Markers are colored by the locus of the restricting HLA allele and sized based on the strength of the association between cluster member TCRs and the HLA allele. The database annotations associated to TCRs in each cluster are summarized with text labels using the following abbreviations: B19 = parvovirus B19, INF = influenza, EBV = Epstein Barr Virus, RA = rheumatoid arthritis, MS = multiple sclerosis, MELA = melanoma, T1D = type one diabetes, CMV = cytomegalovirus. Clusters labeled ‘coCMV’ are significantly associated ($P<1\times10^{−5}$) with CMV seropositivity (see main text discussion of cluster #3). Clusters labeled 1–5 are discussed in the text and examined in greater detail in Figure 7 and Figure 8.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Smoothed distributions of cluster co-occurrence scores on the two validation cohorts. Gaussian kernel density estimation (KDE)-smoothed distributions of the cluster member TCR co-occurrence scores ($Z_{CO}$) for the two validation cohorts. A standard normal distribution is shown as an approximate null expectation for these Z-scores.

![Figure 7.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig7-v2.jpg)

**Figure 7.:** Details on the TCR sequences, occurrence patterns, and annotations for the five most significant clusters (labeled 1–5 in Figure 6) based on size and TCR co-occurrence scores. Each panel consists of a TCRdist dendrogram (left side, labeled with annotation, CDR3 sequence, and occurrence counts for the member TCRs) and a per-subject TCR count profile (right side) showing the aggregate occurrence pattern of the member TCRs (blue curve) and a control pattern (green curve) produced by averaging occurrence counts from multiple independent randomizations of the subject set for each TCR. The numbers in the two ‘Counts’ columns represent the number of HLA+ (left) and HLA- (right) subjects whose repertoire contained the corresponding TCR, where HLA± means positive/negative for the restricting allele (for example, A*24:02 in the case of cluster 1). Annotations use the following abbreviations: B19 (parvovirus B19), INF (influenza virus), YFV (yellow fever virus), MELA (melanoma), T1D (type 1 diabetes), EBV (Epstein-Barr virus), RA (rheumatoid arthritis). In cases where the peptide epitope for the annotation match is known, the first three peptide amino acids are given after ‘-p’. Non-germline CDR3 amino acids with 2 or 3 non-templated nucleotides in their codon are shown in uppercase, while amino acids with only a single non-templated coding nucleotide are shown in lowercase.

![Figure 8.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig8-v2.jpg)

**Figure 8.:** Clusters 3–5; see preceding legend for details.

**Table 2.**
 Covariation between HLA allele charge and average CDR3 charge of HLA-associated TCRs for HLA positions frequently contacted by CDR3 amino acids in solved TCR:pMHC crystal structures.


<table>
  <thead>
    <tr>
      <th rowspan="2">MHC Class</th>
      <th rowspan="2">Position*</th>
      <th rowspan="2">Contact frequency†</th>
      <th colspan="2">Full CDR3</th>
      <th colspan="2">Non-germline CDR3‡</th>
      <th rowspan="2">AAs§</th>
    </tr>
    <tr>
      <th>R-value</th>
      <th>p-value</th>
      <th>R-value</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>II-β</td>
      <td>70</td>
      <td>1.48</td>
      <td>−0.47</td>
      <td>3.3e-04</td>
      <td>−0.52</td>
      <td>6.1e-05</td>
      <td>DEGQR</td>
    </tr>
    <tr>
      <td>II-α</td>
      <td>64</td>
      <td>1.09</td>
      <td>−0.15</td>
      <td>0.33</td>
      <td>−0.07</td>
      <td>0.64</td>
      <td>ART</td>
    </tr>
    <tr>
      <td>I</td>
      <td>152</td>
      <td>0.47</td>
      <td>0.00</td>
      <td>0.99</td>
      <td>−0.04</td>
      <td>0.72</td>
      <td>AERTVW</td>
    </tr>
    <tr>
      <td>I</td>
      <td>151</td>
      <td>0.46</td>
      <td>0.08</td>
      <td>0.50</td>
      <td>0.06</td>
      <td>0.59</td>
      <td>HR</td>
    </tr>
    <tr>
      <td>I</td>
      <td>69</td>
      <td>0.26</td>
      <td>−0.13</td>
      <td>0.28</td>
      <td>−0.14</td>
      <td>0.24</td>
      <td>ART</td>
    </tr>
    <tr>
      <td>I</td>
      <td>76</td>
      <td>0.21</td>
      <td>−0.08</td>
      <td>0.49</td>
      <td>−0.14</td>
      <td>0.25</td>
      <td>AEV</td>
    </tr>
    <tr>
      <td>I</td>
      <td>70</td>
      <td>0.12</td>
      <td>0.02</td>
      <td>0.86</td>
      <td>0.08</td>
      <td>0.50</td>
      <td>HKNQS</td>
    </tr>
  </tbody>
</table>

_*Only positions whose charge varies across alleles are included.†Total number of CDR3 residues contacted (using a sidechain heavyatom distance threshold of 4.5 Å) divided by number of structures analyzed.‡CDR3 charge is calculated over amino acids with at least one non-germline coding nucleotide.§Amino acids present at this HLA position._

We found that a surprising number of the most significant HLA-restricted clusters had links to common viral pathogens. For example, the top cluster by both size and co-occurrence (Figure 7, upper panels) is an A*24:02-associated group of highly similar TCR$\beta$ chains, five of which can be found in a set of 12 TCR$\beta$ sequences reported to respond to the parvovirus B19 epitope FYTPLADQF as part of a highly focused CD8+ response to acute B19 infection (Kasprowicz et al., 2006). The subject TCR-counts curve for this cluster (Figure 7, top right panel) shows a strong enrichment of member TCRs in roughly 30% of the A*24:02 repertoires, which is on the low end of prevalence estimates for this pathogen (Heegaard and Brown, 2002) and may suggest that, if cluster enrichment does correlate with B19 exposure, there are likely to be other genetic or epidemiologic factors that determine which B19-exposed individuals show enrichment. The second most significant cluster by both measures is an A*02:01-associated group of TRBV19 TCRs with a high frequency of matches to the influenza M1$_{58}$ response (41/43 TCRs, labeled ‘INF-pGIL’ for the first three letters of the GILGFVFTL epitope). Notably, the cluster member sequences recapitulate many of the core features of the tree of experimentally identified M1$_{58}$ TCRs (Figure 4—figure supplement 2): a dominant group of length 13 CDR3 sequences with an ‘RS’ sequence motif together with a smaller group of length 12 CDR3s with the consensus CASSIG.YGYTF.

Rounding out the top five, the third and fifth most significant clusters also appear to be pathogen-associated. Cluster #3 brings together a diverse set of DRB1*07:01-associated TCR$\beta$ chains (Figure 8, top dendrogram), none of which matched our annotation database. However, it was strongly associated with CMV serostatus: As is evident in the subject TCR-counts panel for this cluster (Figure 8, top right), there is a highly significant ($P<3\times10^{−19}$) association between CMV seropositivity (blue dots at the bottom of the panel) and cluster enrichment (here defined as a subject TCR count $\geq3$). Finally, the B*08:01-associated cluster #5 (bottom panels in Figure 8) appears to be EBV-associated: four of the TCR$\beta$ chains in this cluster match TCRs annotated as binding to EBV epitopes (two matches for the B*08:01-restricted FLRGRAYGL epitope and two for the B*08:01-restricted RAKFKQLL epitope). The fact that this cluster brings together sequence-dissimilar TCRs that recognize different epitopes from the same pathogen supports the hypothesis that at least some of the observed co-occurrence may be driven by a shared exposure.

As a preliminary validation of the clusters identified here, we examined the occurrence patterns of cluster member TCRs in two independent cohorts: a set of 120 individuals (‘Keck120’) that formed the validation cohort for the original Emerson et al. study, and a set of 86 individuals (‘Brit86’) taken from the aging study of (Britanova et al., 2016). Whereas the Keck120 repertoires were generated using the same platform as our 666-member discovery cohort, the Brit86 repertoires were sequenced from cDNA libraries using 5’-template switching and unique molecular identifiers. In the absence of HLA typing information for these subjects, we simply evaluated the degree to which each cluster’s member TCRs co-occurred over the entirety of each of these validation cohorts, using the co-occurrence score described above ($Z_{CO}^{Keck120}$ and $Z_{CO}^{Brit86}$ columns in Table 3). Although rare alleles and cluster-associated exposures may not occur with sufficient frequency in these smaller cohorts to generate co-occurrence signal, co-occurrence scores support the validity of the clusterings identified on the discovery cohort: 94% of the Keck120 scores and 92% of the Brit86 scores are greater than 0, indicating a tendency of the clustered TCRs to co-occur (smoothed score distributions are shown in Figure 6—figure supplement 1).

### Covariation between CDR3 sequence and HLA allele

Given our large dataset of HLA-associated TCR$\beta$ sequences, we set out to look for correlations between CDR3 sequence and HLA allele sequence. Previous studies have identified correlations between TCR V-gene usage and HLA alleles (Sharon et al., 2016; Blevins et al., 2016); these correlations are consistent with a picture of TCR:peptide:MHC interactions in which the CDR1 and CDR2 loops (whose sequence is determined by the V gene) primarily contact the MHC while the CDR3 loops contact the peptide. To complement these studies and leverage our large set of HLA-associated sequences, we set out to look for correlations between the CDR3 sequence itself and the HLA allele. In our previous work on epitope-specific TCRs (Dash et al., 2017), we identified a significant negative correlation between CDR3 charge and peptide charge, suggesting a tendency toward preserving charge complementarity across the TCR:pMHC interface. Although the CDR3 loop primarily contacts the MHC-bound peptide, computational analysis of solved TCR:peptide:MHC structures in the Protein Data Bank (Berman et al., 2000) (see Materials and methods) identified a number of HLA sequence positions that are frequently contacted by CDR3 amino acids (Table 2). For each frequently-contacted HLA position with charge variability among alleles we computed the covariation between HLA allele charge at that position and average CDR3 charge for allele-associated TCRs. Since portions of the CDR3 sequence are contributed by the V- and J-gene germline sequences, and covariations are known to exist between HLA and V-gene usage, we also performed a covariation analysis restricting to ‘non-germline’ CDR3 sequence positions whose coding sequence is determined by at least one non-templated insertion base (based on the most parsimonious VDJ reconstruction; see Materials and methods). We found a significant negative correlation ($R=−0.47,P<4\times10^{−4}$ for the full CDR3 sequence; $R=−0.52,P<7\times10^{−5}$ for the non-germline CDR3 sequence) between CDR3 charge and the charge at position 70 of the class II beta chain (correcting these p-values for the fact that we considered $7$ positions yields $2.3\times10^{−3}$ and $4.3\times10^{−4}$). We did not see a significant correlation for the frequently contacted position on the class II alpha chain, perhaps due to the lack of sequence variation at the DR$\alpha$ locus and/or the more limited number of DQ$\alpha$ and DP$\alpha$ alleles. None of the five class I positions showed significant correlations, which could be due to their lower contact frequencies, a smaller average number of associated TCRs ($51$ for class I versus $309$ for class II), bias toward A*02 in the structural database, or noise introduced from multiple contacted positions varying simultaneously. Further analysis of the class II correlation suggested that it was driven largely by HLA-DRB1 alleles: position 70 correlations were $−0.56$ versus $−0.10$ for DR and DQ, respectively, over the full CDR3 and $−0.64$ vs $−0.38$ for the non-germline CDR3. Figure 9 provides further detail on this DRB1-TCR charge anti-correlation, including a structural superposition showing the proximity of position 70 to the TCR$\beta$ CDR3 loop.

![Figure 9.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig9-v2.jpg)

**Figure 9.:** (A–B) Allele charge ($x$-axis) versus average CDR3 charge of allele-associated TCR$\beta$ chains ($y$-axis) for 30 HLA-DRB1 alleles. Charge of the CDR3 loop was calculated over the full CDR3 sequence (A) or over the subset of CDR3 amino acids with at least one non-germline coding nucleotide (B). Correlation p-values correspond to a 2-sided test of the null hypothesis that the slope is zero, as implemented in the function scipy.stats.linregress ($N=30$ alleles). (C–D) CDR3 charge distributions for TCRs associated with alleles having defined charge at position 70 ($x$-axis) using the full (C) or non-germline (D) CDR3 sequence (mean values shown as white pluses). (E) Superposition of five TCR:peptide:HLA-DR crystal structures (PDB IDs 1j8h, 2iam, 2wbj, 3o6f, and 4e41; [Hennecke and Wiley, 2002; Deng et al., 2007; Harkiolaki et al., 2009; Yin et al., 2011; Deng et al., 2012]) showing the DR$\alpha$ chain in green, the DR$\beta$ chain in cyan, the peptide in magenta, the TCR$\beta$ chain in blue with the CDR3 loop colored reddish brown. The TCR$\alpha$ chain is omitted for clarity, and position 70 is highlighted in yellow.

### CMV-associated TCRβ chains are largely HLA-restricted

We analyzed the HLA associations of strongly CMV-associated TCR$\beta$ chains to gain insight into their predictive power across genetically diverse individuals. Here we change perspective somewhat from earlier sections, in that we select TCRs based on their CMV association and then evaluate HLA association, rather than the other way around. In their original study, Emerson et al. identified a set of TCR$\beta$ chains that were enriched in CMV seropositive individuals and showed that by counting these CMV-associated TCR$\beta$ chains in a query repertoire they could successfully predict CMV serostatus both in cross-validation and on an independent test cohort. The success of this prediction strategy across a diverse cohort of individuals raises the intriguing question of whether these TCR$\beta$s are primarily HLA-restricted in their occurrence and in their association with CMV, or whether they span multiple HLA types. To shed light on this question we focused on a set of $68$ CMV-associated TCR$\beta$ chains whose co-occurrence with CMV seropositivity was significant at a p-value threshold of 1.5e-5 (corresponding to an FDR of $0.05$; see Materials and methods). For each CMV-associated TCR$\beta$ chain, we identified its most strongly associated HLA allele and compared the p-value of this association to the p-value of its association with CMV (Figure 10A). From this plot we can see that the majority of the CMV-associated chains do appear to be HLA-associated, having p-values that exceed the FDR $0.05$ threshold for HLA association. The excess of highly significant HLA-association p-values for these CMV-associated TCR$\beta$s can be seen in Figure 10B, which compares the observed p-value distribution to a background distribution of HLA association p-values for randomly selected frequency-matched public TCR$\beta$s.

![Figure 10.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig10-v2.jpg)

**Figure 10.:** CMV-associated TCR$\beta$ chains are largely HLA-restricted.(A) Comparison of CMV-association ($x$-axis) and HLA-association ($y$-axis) p-values for 68 CMV-associated TCR$\beta$ chains shows that the majority are also HLA associated. (B) Smoothed densities comparing HLA-association p-value distributions for the $68$ CMV-associated chains (blue) and a cohort-frequency matched set of $6800$ randomly selected public TCR$\beta$ chains. CMV-associated TCRs are much more strongly HLA-associated than would be expected based solely on their cohort frequency. (C) CMV-association p-values computed over subsets of the cohort positive ($x$-axis) or negative ($y$-axis) for the HLA allele most strongly associated with each TCR. For most of the TCR chains, CMV association is restricted to the subset of the cohort positive for their associated HLA allele. (D) HLA-association p-values computed over CMV-positive ($x$-axis) or CMV-negative ($y$-axis) subsets of the cohort suggest that for these $68$ CMV-associated TCR$\beta$ chains, HLA-association is driven solely by response to CMV (rather than generic affinity for their associated allele, for example, or additional self or viral epitopes). In panels (A), (C), and (D), points are colored by CMV-association p-value; in all panels we use a modified logarithmic scale based on the square root of the exponent when plotting p-values in order to avoid compression due to a few highly significant associations.

As a next step we looked to see whether these HLA associations fully explained the CMV association, in the sense that the CMV association was only present in subjects positive for the associated allele. For each of the $68$ CMV-associated TCRs, we divided the cohort into subjects positive for its most strongly associated HLA allele and subjects negative for that allele. Here we considered both 2- and 4-digit resolution alleles when defining the most strongly associated allele, to allow for TCRs whose association extends beyond a single 4-digit allele. We computed association p-values between TCR occurrence and CMV seropositivity over these two cohort subsets independently and compared them (Figure 10C). We see that the majority of the points lie below the $y=x$ line—indicating a stronger CMV-association on the subset of the cohort positive for the associated allele—and also below the line corresponding to the expected minimum of $68$ uniform random variables (i.e. the expected upper significance limit in the absence of CMV association on the allele-negative cohort subsets). There are however a few TCR$\beta$s which do not appear strongly HLA-associated and for which the CMV-association remains strong in the absence of their associated allele (the points above the line $y=x$ in Figure 10C). For example, the public TCR$\beta$ chain defined by TRBV07 and the CDR3 sequence CASSSDSGGTDTQYF (which corresponds to the highest point in Figure 10C) is strongly CMV-associated ($22/23$ subjects with this chain are CMV positive; $P<3\times10^{−7}$) but does not show evidence of HLA association in our dataset. TCRs with HLA promiscuity may be especially interesting from a diagnostic perspective, since their phenotype associations may be more robust to differences in genetic background.

Finally, we looked to see whether CMV association completely explained the observed HLA associations, in the sense that a response to one or more CMV epitopes was likely the only driver of HLA association, or whether there might be evidence for other epitope-specific responses by these TCR$\beta$ chains or a more general affinity for the associated allele, perhaps driven by common self antigens. Put another way, do we see evidence for pre-existing enrichment of any of these TCR$\beta$ chains when their associated allele is present, even in the absence of CMV, which might suggest that the CMV response recruits from a pre-selected pool enriched for TCRs with intrinsic affinity for the restricting allele? To approach this question we split the cohort into CMV seropositive and seronegative subjects and computed, for each of the $68$ CMV-associated TCRs, the strength of its association with its preferred allele over these two subsets separately. Figure 10D compares these HLA-association p-values computed over the subsets of the cohort positive (289 individuals, $x$-axis) and negative (352 individuals, $y$-axis) for CMV. We can see in this case that all of the associations on the CMV-positive subset are stronger than those on the CMV-negative subset, and indeed the CMV-negative p-values do not appear to exceed random expectation given the number of comparisons performed. Thus, the apparent lack of any significant HLA-association on the CMV-negative cohort subset suggests that the HLA associations of these CMV-predictive chains are largely driven by CMV exposure. A limitation of this analysis is that, although the CMV-negative subset of the cohort is larger than the CMV-positive subset, the number of TCR occurrences in the CMV-negative subset is likely lower than in the CMV-positive subset for these CMV-associated chains, which will limit the strength of the HLA associations that can be detected.

## Discussion

Each individual’s repertoire of circulating immune receptors encodes information on their past and present exposures to infectious and autoimmune diseases, to antigenic stimuli in the environment, and to tumor-derived epitopes. Decoding this exposure information requires an ability to map from amino acid sequences of rearranged receptors to their eliciting antigens, either individually or collectively. One approach to developing such an antigen-mapping capability would involve collecting deep repertoire datasets and detailed phenotypic information on immune exposures for large cohorts of genetically diverse individuals. Correlation between immune exposure and receptor occurrence across such datasets could then be used to train statistical predictors of exposure, as demonstrated by Emerson et al. for CMV serostatus. The main difficulty with such an approach, beyond the cost of repertoire sequencing, is likely to be the challenge of assembling accurate and complete immune exposure information.

For this reason, we set out to discover potential signatures of immune exposures de novo, in the absence of phenotypic information, using only the structure of the public repertoire—its receptor sequences and their occurrence patterns. By analyzing co-occurrence between pairs of public TCR$\beta$ chains and between individual TCR$\beta$ chains and HLA alleles, we were able to identify statistically significant clusters of co-occurring TCRs across a large cohort of individuals and in a variety of HLA backgrounds. Indirect evidence from sequence matches to experimentally-characterized receptors suggests that some of these TCR clusters may reflect hidden immune exposures shared among subsets of the cohort members; indeed, several of the most significant clusters appear linked to common viral pathogens (parvovirus B19, influenza, CMV, and EBV).

The results of this paper demonstrate the potential for a productive dialog between statistical analysis of TCR repertoires and immune exposure analysis. Specifically, sequences from the statistically-inferred clusters defined here could be tested for antigen reactivity or combined with immune exposure data to infer the driver of TCR expansion, as was done here for the handful of CMV-associated clusters based on CMV serostatus information. In either case our clustering approach will reduce the amount of independent data required, since the immune phenotype data is used for annotation of a modest number of defined TCR groupings rather than direct discovery of predictive TCRs from the entire public repertoire. We can also look for the presence of specific TCRs and TCR clusters identified here in other repertoire datasets, for example from studies of specific autoimmune diseases or pathogens, as a means of assigning putative functions. However the answer may not be entirely straightforward: it remains possible that enrichment for other cluster TCRs, rather than being associated with an exposure per se, is instead associated with some subject-specific genetic or epigenetic factor that determines whether a specific TCR response will be elicited by a given exposure.

The finding by Emerson et al.—now replicated and extended in this work—that there are large numbers of TCR$\beta$ chains whose occurrence patterns (independent of potential TCR$\alpha$ partners) are strongly associated with specific HLA alleles, raises the question of what selective forces drive these biased occurrence patterns. Our observations point to a potential role for responses to common pathogens in selecting some of these chains in an HLA-restricted manner. Self-antigens (presented in the thymus and/or the periphery) may also play a role in enriching for specific chains, as suggested by (Madi et al., 2017) in their work on TCR similarity networks formed by the most frequent CDR3 sequences. Our conclusions diverge somewhat from this previous work, which may be explained by the following factors: our use of HLA-association rather than intra-individual frequency as a filter for selecting TCRs, our inclusion of information on the V-gene family in addition to the CDR3 sequence when defining TCR sharing and computing TCR similarity, and our use of TCR occurrence patterns, rather than CDR3 edit distance, to discover TCR clusters. We also find it interesting that class II loci appear on average to have greater numbers of associated TCR$\beta$ chains than class I loci (Figure 5): presumably this reflects differences in selection and/or abundance between the CD4+ and CD8+ T cell compartments (Sinclair et al., 2013), but the underlying explanation for this trend is unclear, although a similar bias was observed by Sharon et al., 2016. One caveat is that it can be difficult to reliably assign TCR associations to individual members of groups of highly correlated HLA alleles; perfectly correlated alleles have been collapsed into haplotypes in our analysis, but there remain allele pairs (particularly between the HLA-DR and HLA-DQ loci) that strongly co-occur across the cohort. In addition, TCR$\beta$ chains associated with multiple HLA alleles (for example, because they recognize the same peptide presented by several different alleles) might be missed in our approach; although our analysis of HLA-association for CMV-associated TCR chains did not detect a substantial degree of HLA promiscuity, it remains to be seen whether this extends to other classes of functional TCRs. Alternative approaches that focus on other features, such as clonal abundance, to select TCR chains for clustering and downstream analysis are worth pursuing. It is also worth pointing out that our primary focus on presence/absence of TCR$\beta$ chains (rather than abundance) assumes relatively uniform sampling depths across the cohort; in the limit of very deep repertoire sequencing, pathogen-associated chains may be found (presumably in the naive pool) even in the absence of the associated immune challenge, while shallow sampling reliably picks out only the most expanded T cell clones. Here the use of clusters of responsive TCRs rather than individual chains lessens stochastic fluctuations in TCR occurrence patterns, providing some measure of robustness.

We look forward to the accumulation of new data sets, which will enable future researchers to move beyond the limitations of the study presented here. An ideal study would perform discovery on repertoire data from multiple large cohorts, rather than the single large cohort generated with a single sequencing platform. Although we do validate TCR clusters on two independent datasets, with one from a different immune profiling technology, performing discovery on multiple large cohorts would presumably give more robust results. Future analyses of independent, HLA-typed cohorts will provide additional validation of trends seen here. The lack of sequenced TCR$\alpha$ or paired $\alpha$/$\beta$ repertoires for this cohort limits the features we can detect and may introduce bias into some of our conclusions. Certain T cell subsets, such as MAIT and invariant natural killer T cells, are more easily recognized from $\alpha$ chain sequence data. It is likely that many TCRs that are associated with specific immune exposures when considered as paired TCR chains are not detectably associated with those exposures (or with other TCRs responding to those exposures) when analyzing only the $\alpha$ or $\beta$ chain alone: indeed it is somewhat surprising that we find as many apparent associations and co-occurring clusters as we do given that we are considering only the TCR$\beta$ chain. Greater sequencing depth and/or analysis of sorted T cell populations will likely be required of future studies that aim to examine the impact of HLA on the composition of the naive T cell repertoire. We also hope that future studies will have rich immune exposure data beyond CMV serostatus: although the cohort members were all nominally healthy at the time of sampling, it is likely that there are a variety of immune exposures, some presaging future pathologies, that can be observed in a diverse collection of 650+ individuals. As an example, two of our EBV-annotated clusters contain TCR$\beta$ chains also seen in the context of rheumatoid arthritis: cross-reactivity between pathogen and autoimmune epitopes may mean that TCR clusters discovered on the basis of common infections also provide information relevant in the context of autoimmunity.

## Materials and methods

### Datasets

TCR$\beta$ repertoire sequence data for the 666 members of the discovery cohort was downloaded from the Adaptive biotechnologies website using the link provided in the original (Emerson et al., 2017) publication (https://clients.adaptivebiotech.com/pub/Emerson-2017-NatGen). The repertoire sequence data for the 120 individuals in the ‘Keck120’ validation set was included in the same download. Repertoire sequence data for the 86 individuals in the ‘Brit86’ validation set was downloaded from the NCBI SRA archive using the Bioproject accession PRJNA316572 (Britanova et al., 2016) and processed using scripts and data supplied by the authors (https://github.com/mikessh/aging-study) in order to demultiplex the samples and remove technical replicates. Repertoire sequence data for TCR$\beta$ chains from MAIT cells was downloaded from the NCBI SRA archive using the Bioproject accession PRJNA412739 (Howson et al., 2018). Repertoire sequence data for TCR$\beta$ chains from T cells sorted for CD4/CD8 surface markers were taken from the following studies: (Emerson et al., 2013), available for download at https://clients.adaptivebiotech.com/pub/emerson-2013-jim; (Rubelt et al., 2016), downloaded from the NCBI SRA archive using the Bioproject accession PRJNA300878; (Li et al., 2016), downloaded from the NCBI SRA archive using the Bioproject accession PRJNA348095; and (Oakes et al., 2017), downloaded from the NCBI SRA archive using the Bioproject accession PRJNA390125.

V and J genes were assigned by comparing the TCR nucleotide sequences to the IMGT/GENE-DB (Giudicelli et al., 2005) nucleotide sequences of the human TR genes (sequence data downloaded on 9/6/2017 from http://www.imgt.org/genedb/). CDR3 nucleotide and amino acid sequences and most-parsimonious VDJ recombination scenarios were assigned by the TCRdist pipeline (Dash et al., 2017) (the most parsimonious recombination scenario, used for identifying non-germline CDR3 amino acids, is the one requiring the fewest non-templated nucleotide insertions). To define the occurrence matrix of public TCRs and assess TCR-TCR, TCR-HLA and TCR-CMV association, a TCR$\beta$ chain was identified by its CDR3 amino acid sequence and its V-gene family (e.g., TRBV6-4*01 was reduced to TRBV06). TCR sequence reads for which a unique V-gene family could not be determined (due to equally well-matched V genes from different families, a rare occurrence in this dataset) were excluded from the analysis. The matrix $M$ of public TCR$\beta$ occurrences across the discovery cohort, HLA allele occurrence patterns, and other associated data needed to reproduce the findings of this study have been deposited in the Zenodo database (doi:10.5281/zenodo.1248193).

### Eliminating potential cross-contamination

A preliminary analysis of TCR sharing at the nucleotide level was conducted to identify potential cross-contamination in the discovery cohort repertoires. Each TCR$\beta$ nucleotide sequence that was found in multiple repertoires was assigned a generation probability ($P_{gen}$, see below) in order to identify nucleotide sequences with suspiciously high sharing rates among repertoires. Visual comparison of the sharing rate (the number of repertoires in which each TCR$\beta$ nucleotide sequence was found) to the generation probability (Figure 11) showed that the majority of highly-shared TCRs had correspondingly high generation probabilities; it also revealed a cluster of TCR chains with unexpectedly high sharing rates. Examination of the sequences of these highly-shared TCRs revealed them to be variants of the consensus sequence CFFKQKTAYEQYF (coding sequence: tgttttttcaagcagaagacggcatacgagcagtacttc). Consultation with scientists at Adaptive Biotechnologies confirmed that these sequences were likely to represent a technical artifact of the sequencing pipeline. We elected to remove all TCR$\beta$ nucleotide sequences whose sharing rates put them outside the decision boundary indicated by the black line in Figure 11, which eliminated the vast majority of the artifactual variants as well as a handful of other highly shared, low-probability sequences ($592$ nucleotide sequences in total were removed).

![Figure 11.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig11-v2.jpg)

**Figure 11.:** Each point represents a TCR$\beta$ nucleotide sequence that occurs in more than one repertoire, plotted according to its generation probability ($P_{gen}$, $x$-axis) and the number of repertoires in which it was seen ($N_{repertoires}$, $y$-axis). Very low probability nucleotide sequences that are shared across many repertoires represent potential cross-contamination, as confirmed for one large cluster of artifactual sequences (see the main text). We excluded all TCR$\beta$ nucleotide sequences lying above the boundary indicated by the black line ($N=592$).

### Measuring clonal expansion

Each public TCR$\beta$ chain was assigned a clonal expansion index ($I_{exp}$) determined by its frequencies in the repertoires in which it was found. First, the unique TCR$\beta$ chains present in each repertoire were ordered based on their inferred nucleic acid template count (Carlson et al., 2013), and assigned a rank ranging from $0$ (lowest template count) to $S−1$ (highest template count), where $S$ is the total number of chains present in the repertoire. TCRs with the same template count were assigned the same tied rank equal to the midpoint of the tied group. In order to compare across repertoires, the ranks for each repertoire were then normalized by dividing by the number of unique sequences in the repertoire. The clonal expansion index for a given public TCR $t$ was taken to be its average normalized rank for the repertoires in which it occurred:

$$
I_{exp}(t)=\frac{1}{m}\sumi=1m \frac{r_{i}}{S_{i}−1},
$$

where the sum is taken over the $m$ repertoires in which $t$ is found, $r_{i}$ is the template-count rank of TCR $t$ in repertoire $i$, and $S_{i}$ is the total size of repertoire $i$.

### HLA typing

HLA genotyping was performed and confirmed by molecular means, including sequence specific oligonucleotide probe typing (SSOP), Sanger sequencing (SBT) or next generation sequencing (NGS) (Smith et al., 2014). Independently, HLA alleles were imputed using data generated by high density single-nucleotide polymorphism arrays as previously described (Martin et al., 2017). Imputed alleles were compared with HLA typing data from SBT and NGS, and used to resolve ambiguous HLA codes generated by SSOP and provide a uniform set of four digit allele assignments. HLA typing data availability varied across loci as follows: HLA-A ($629$ subjects), HLA-B ($630$ subjects), HLA-C ($629$ subjects), HLA-DRB1 ($630$ subjects), HLA-DQA1 ($522$ subjects), HLA-DQB1 ($630$ subjects), HLA-DPA1 ($606$ subjects), and HLA-DPB1 ($472$ subjects). When calculating the association p-values between TCR$\beta$ chains and HLA alleles reported in Table 1, the cohort was restricted to the subset of subjects with available HLA typing at the relevant locus. For comparing TCR association rates across loci in Figure 5, associations were calculated over the cohort subset ($522$ subjects) with typing data at all compared loci (A, B, C, DRB1, DQA1, and DQB1) in order to avoid spurious differences in association strengths arising from differential data availability among the loci. Due to their very strong linkage on our cohort, five DR-DQ haplotypes were treated as single allele units for association calculations and clustering: DRB1*03:01-DQA1*05:01-DQB1*02:01, DRB1*15:01-DQA1*01:02-DQB1*06:02, DRB1*13:01-DQA1*01:03-DQB1*06:03, DRB1*10:01-DQA1*01:05-DQB1*05:01, and DRB1*09:01-DQA1*03:02-DQB1*03:03.

### TCR generation probability

We implemented a version of the probabilistic model proposed by Walczak and co-workers (Murugan et al., 2012) in order to assign to each public TCR$\beta$ chain (defined by a V-gene family and a CDR3 amino acid sequence) a generation probability, $P_{gen}$, which captures the probability of seeing that TCR$\beta$ in the preselection repertoire. $P_{gen}$ is calculated by summing the probabilities of the possible VDJ rearrangements that could have produced the observed TCR:

$$
P_{gen}(V_{family},CDR3_{aa})=\sums\inS P(s)
$$

where $S$ represents the set of possible VDJ recombination scenarios capable of producing the observed TCR V family and CDR3 amino acid sequence. To compute the probability of a given recombination scenario $s$, we use the factorization proposed by Marcou et al. (2018), which captures observed dependencies of V-, D-, and J-gene trimming on the identity of the trimmed gene and of inserted nucleotide identity on the identity of the preceding nucleotide:

$$
P(s)=P(V_{s})P(D_{s}|J_{s})P(J_{s})\timesP(del_{s}V|V_{s})P(del_{s}D5^{′},del_{s}D3^{′}|D_{s})P(del_{s}J|J_{s})\timesP(Ins_{s}VD)\prodiIns_{s}VD P(n_{i}|n_{i−1})\timesP(Ins_{s}DJ)\prodiIns_{s}DJ P(m_{i}|m_{i−1})
$$

Here the recombination scenario $s$ consists of a choice of V gene ($V_{s}$), D gene ($D_{s}$), J gene ($J_{s}$), number of nucleotides trimmed back from the end of the V gene ($del_{s}V$) or J gene ($del_{s}J$) or D gene ($del_{s}D5^{′}$ and $del_{s}D3^{′}$), number of nucleotides inserted between the V and D genes ($Ins_{s}VD$) and between the D and J genes ($Ins_{s}DJ$) and the identities of the inserted nucleotides (${n_{i}}$ and ${m_{i}}$ respectively). At the start of the calculation, the CDR3 amino acid sequence is converted to a list of potential degenerate coding nucleotide sequences (here degenerate means that nucleotide class symbols such as W (for A and T) and R (for A and G) are allowed). Since each amino acid other than Leucine, Serine, and Arginine has a single degenerate codon (P=CCN, N = AAY, K = AAR, etc.) and these three amino acids have two such codons (S={TCN,AGY}, R={CGN,AGR}, L={CTN,TTR}), this list of nucleotide coding sequences is generally not too long. The generation probability is then taken to be the sum of the probabilities of these degenerate nucleotide sequences. Since the total number of possible recombination scenarios is in principle quite large, we make a number of approximations to speed the calculation: we limit excess trimming of genes to at most three nucleotides, where excess trimming is defined to be trimming back a germline gene nucleotide which matches the target CDR3 nucleotide (therefore requiring non-templated reinsertion of the same nucleotide); at most two palindromic nucleotides are allowed; sub-optimal D gene alignments are only considered up to a score gap of 2 matched nucleotides relative to the best match. The parameters of the probability model are fit by a simple iterative procedure in which we generate rearranged sequences using an initial model, compare the statistics of those sequences to statistics derived from observed out-of-frame rearrangements in the dataset, and adjust the probability model parameters to iteratively improve agreement. We compared the nucleotide sequence generation probabilities computed using our software with those computed using the published tool IGoR (Marcou et al., 2018) and found good overall agreement: a linear regression analysis of the $log_{10}⁡(P_{gen})$ values gives a correlation coefficient $R=0.97$ with slope of $0.98$ and an intercept of $0.22$ for a set of $800$ randomly selected TCR$\beta$ chains.

### Co-occurrence calculations

We performed an analysis of covariation across the cohort for pairs of TCR chains and for TCR chains and HLA alleles (Figure 12). We used the hypergeometric distribution to assess the significance of an observed overlap between two subsets of the cohort (for example, the subset of subjects positive for a given HLA allele and the subset of subjects with a given TCR$\beta$ chain in their repertoires), taking our significance p-value to be the probability of seeing an equal or greater overlap if the two subsets had been chosen at random:

$$
P_{overlap}(k,N_{1},N_{2},N)=\sumj\geqk \frac{(N_{1}j)(N−N_{1}N_{2}−j)}{(NN_{2})}
$$

where $k$ is the size of the overlap, $N_{1}$ and $N_{2}$ are the sizes of the two subsets, and $N$ is the total cohort size (i.e., the number of individuals in the cohort). We use $P_{overlap}$ to assess the significance of an overlap $C_{a}∩C_{t}$ between an HLA allele $a$ found in the cohort subset $C_{a}$ and a TCR$\beta$ chain $t$ found in the cohort subset $C_{t}$ as follows:

$$
P_{HLA}(a,t)=P_{overlap}(|C_{a}∩C_{t}|,|C_{a}|,|C_{t}|,N)
$$

where $|C|$ denotes the cardinality of the set $C$. A complication arises when assessing TCR-TCR co-occurrence in the presence of variable-sized repertoires: TCRs are more likely to come from the larger repertoires than the smaller ones, which violates the assumptions of the hypergeometric distribution and leads to inflated significance scores. In particular, when we use the hypergeometric distribution to model the overlap between the sets of subjects in which two TCR chains are found, we implicitly assume that all subjects are equally likely to belong to a TCR chain’s subject set. If the subject repertoires vary in size, this assumption will not hold. For example, in the limit of a subject with an empty repertoire, no TCR subject sets will contain that subject, which will inflate all the overlap p-values since we are effectively overstating the size $N$ of the cohort by $1$. On the other hand, if one of the subject repertoires contains all the public TCR chains, then each TCR-TCR overlap will automatically contain that subject, again inflating the p-values since we are artificially adding $1$ to each of $k$, $N_{1}$, $N_{2}$, and $N$. We developed a simple heuristic to correct for this effect using a per-subject bias factor by defining

$$
b_{i}=\frac{S_{i}N}{\sum_{j=1}^{N} S_{j}},
$$

where $S_{i}$ is the size of repertoire $i$ and $N$ is the cohort size. To score an overlap between the occurrence patterns of two TCR$\beta$ chains $t$ and $t^{′}$, where $t$ is found in the subset $C_{t}$ of the cohort, $t^{′}$ is found in the subset $C_{t^{′}}$, and their overlap $C_{t}∩C_{t^{′}}$ contains the $k$ subjects $s_{1},...,s_{k}$, we adjust the overlap p-value ($P_{overlap}$) by the product of the bias factors of the subjects in the overlap:

$$
P_{CO}(t,t^{′})=(\prodj=1k b_{s_{j}})P_{overlap}(|C_{t}∩C_{t^{′}}|,|C_{t}|,|C_{t^{′}}|,N)
$$

Here we are multiplying the hypergeometric p-value ($P_{overlap}$) by a term that corrects for the fact that not all overlaps of size $k$ are equally likely (the product of the $k$ bias factors captures the relative bias toward the observed overlap). This has the effect of decreasing the significance assigned to overlaps involving larger repertoires, yet remains fast to evaluate, an important consideration given that the all-vs-all TCR co-occurrence calculation involves about $10^{14}$ pairwise comparisons (and this calculation is repeated multiple times with shuffled occurrence patterns to estimate false-discovery rates). When clustering by co-occurrence, we augmented this heuristic p-value correction by also eliminating repertoires with very low (fewer than 30,000) or very high (more than 120,000) numbers of public TCR$\beta$ chains (nonzero entries in the occurrence matrix $M$), as well as five additional repertoires which showed anomalously high levels of TCR nucleotide sharing with another repertoire—all with the goal of reducing potential sources of spurious TCR-TCR co-occurrence signal.

![Figure 12.](https://cdn.elifesciences.org/articles/38358/elife-38358-fig12-v2.jpg)

**Figure 12.:** Co-occurrence p-values are calculated to assess TCR-TCR ($P_{CO}$) and TCR-HLA ($P_{HLA}$) covariation across the cohort. Shared response to unknown immune exposures may explain strongly co-occurring TCR pairs, while significant HLA association can highlight functional TCRs. TCR$\beta$ chains are compared to a set of previously characterized TCRs for annotation purposes.

### Estimating false-discovery rates

We used the approach of (Storey and Tibshirani, 2003) to estimate false-discovery rates for detecting associations between TCRs and HLA alleles and between TCRs and CMV seropositivity. Briefly, for a fixed significance threshold $P$ we estimate the false-discovery rate (FDR) by randomly permuting the HLA allele or CMV seropositivity assignments $20$ times and computing the average number of significant associations discovered at the threshold $P$ in these shuffled datasets. The estimated FDR is then the ratio of this average shuffled association number to the number of significant associations discovered in the true dataset at the same threshold. In order to estimate a false-discovery rate for TCR-TCR co-occurrence over the full cohort, we performed $20$ co-occurrence calculations on shuffled occurrence matrices, preserving the per-subject bias factors during shuffling by resampling each TCR’s occurrence pattern with the bias distribution ${b_{i}}$ determined by the subject repertoire sizes.

### Assigning CD4+/CD8+ status to public TCRs

We assessed the accuracy of our TCR:HLA associations by looking for HLA-associated public TCR$\beta$ chains in sequenced repertoires from T cell populations that were sorted for the presence of CD4/CD8 surface markers. We selected four repertoire datasets with matched CD4+ and CD8+ repertoires from a total of $63$ individuals (see the section Datasets for access details; [Emerson et al., 2013; Rubelt et al., 2016; Li et al., 2016; Oakes et al., 2017]). We analyzed the occurrence patterns of HLA-associated TCR$\beta$ chains in these sequence datasets, producing for each TCR$\beta$ counts of the number of CD4+ and CD8+ repertoires it was observed in ($N_{CD4}$ and $N_{CD8}$). TCR$\beta$ abundance levels within the individual repertoires were ignored; each occurrence in a repertoire contributed a single count to the respective CD4 or CD8 total (which therefore range between $0$ and $63$). Given a threshold $\delta$ on the CD4/CD8 counts difference, we assign to the CD4 compartment all TCRs for which $N_{CD4}−N_{CD8}\geq\delta$, and we assign to the CD8 compartment all TCRs for which $N_{CD8}−N_{CD4}\geq\delta$. Figure 5—figure supplement 1 shows the concordance between these assignments and inferences based on the HLA class of the most strongly associated HLA allele, for all significantly associated TCR$\beta$ chains and for various threholds $\delta$.

### TCR clustering

We used the DBSCAN (Ester et al., 1996) algorithm to cluster public TCR$\beta$ chains by their occurrence patterns. DBSCAN is a simple and robust clustering procedure that requires two input parameters: a similarity/distance threshold ($T_{sim}$) at which two points in the dataset are considered to be neighbors, and a minimum number of neighbors ($N_{core}$) for a point to be considered a core, as opposed to a border, point. DBSCAN clusters consist of the connected components of the neighbor-graph over the core points, together with any border point neighbors the core cluster members have. To prevent the discovery of fictitious clusters, $T_{sim}$ and $N_{core}$ can be selected so that core points (points with at least $N_{core}$ neighbors) are unlikely to occur by chance. There is a trade-off between the two parameter settings: as $T_{sim}$ is relaxed, points will tend to have more neighbors on average and thus $N_{core}$ should be increased, which biases toward discovery of larger clusters; conversely, more stringent settings of $T_{sim}$ are compatible with smaller values for $N_{core}$ which permits the discovery of smaller, more tightly linked clusters.

For clustering TCRs by co-occurrence over the full cohort, we used a threshold of $T_{sim}$$=10^{−8}$ and chose a value for $N_{core}$ ($6$) such that no core points were found in any of the $20$ shuffled datasets. In other words, two TCRs $t_{1}$ and $t_{2}$ were considered to be neighbors for DBSCAN clustering if $P_{CO}(t_{1},t_{2})<10^{−8}$; a TCR was considered a core point if it had at least $6$ neighbors. Choosing parameters for HLA-restricted TCR clustering was slightly more involved due to the variable number of clustered TCRs for different alleles, and the more complex nature of the similarity metric, whose dependence on TCR sequence makes shuffling-based approaches more challenging. To begin, we transformed the TCRdist sequence-similarity measure into a significance score $P_{TCRdist}$ which captures the probability of seeing an observed or smaller TCRdist score for two randomly selected TCR$\beta$ chains. Since public TCR$\beta$ chains are on average shorter and closer to germline than private TCRs, we derived the $P_{TCRdist}$ CDF by performing TCRdist calculations on randomly selected public TCRs seen in at least $5$ repertoires. We identified neighbors for DBSCAN clustering using a similarity score $P_{sim}$ that combines co-occurrence and TCR sequence similarity:

$$
P_{sim}(t_{1},t_{2})=f(P_{TCRdist}(t_{1},t_{2})⋅P_{CO}(t_{1},t_{2}))
$$

where the transformation by $f(x)=x−xlog⁡(x)$ corrects for taking the product of two p-values because $f(x)$ is the cumulative distribution function of the product of two uniform random variables. Thus, if $P_{TCRdist}$ and $P_{CO}$ are independent and uniformly distributed, the same will be true of $P_{sim}$.

For HLA-restricted clustering using this combined similarity measure we set a fixed value of $T_{sim}$$=10^{−4}$ and adjusted the $N_{core}$ parameter as a function of the total number of TCRs clustered for each allele. As in global clustering, our goal was to choose $N_{core}$ such that core points were unlikely to occur by chance (more precisely, had a per-allele probability less than $0.05$). We estimated the probability of seeing core points by modeling neighbor number using the binomial distribution, assuming that the observed neighbor number of a given TCR during clustering is determined by $M−1$ independent Bernoulli-distributed neighborness tests with rate $r$, where $M$ is the number of clustered TCRs. Rather than assuming a fixed neighbor-rate $r$ across TCRs, we captured the observed variability in neighbor-rate (due, for example, to unequal V-gene frequencies and variable CDR3 lengths) by using a mixture of 20 rates ${r_{j}}$ estimated from similarity comparisons on randomly chosen public TCRs. More precisely, we choose the smallest value of $N_{core}$ for which the following inequality holds (where $M$ is the number of clustered TCRs for the allele in question):

$$
\frac{M}{20}\sumj=120 \sumi=N_{core}M−1 (M−1i)r_{j}^{i}(1−r_{j})^{M−1−i}< 0.05
$$

We also used this neighbor-number model to assign a p-value ($P_{size}$) to each cluster reflecting the likelihood of seeing the observed degree of clustering by chance. Since DBSCAN clusters are effectively single-linkage-style partitionings of the core points (together with any neighboring border points), they can have a variety of shapes, ranging from densely interconnected graphs, to extended clusters held together by local neighbor relationships (Ester et al., 1996). Modeling the total size of these arbitrary groupings is challenging, so we took the simpler and more conservative approach of assigning p-values based on the size of the largest TCR neighborhood (set of neighbors for a single TCR) contained within each cluster. We identified the member TCR with the greatest number of neighbors in each cluster (the cluster center) and computed the likelihood of seeing an equal or greater neighbor-number under the mixture model described above. This significance estimate is conservative in that it neglects clustering contributions from TCRs outside the neighborhood of the cluster center, however in practice we observed that the majority of TCR clusters were dominated by a single dense region of repertoire space and therefore reasonably well-captured by a single neighborhood. To control false discovery when combining DBSCAN clusters from independent clustering runs for different HLA alleles, we used the Holm method (Holm, 1979) applied to the sorted list of cluster $P_{size}$ values, with a target family-wise error rate (FWER) of $0.05$ (i.e., we attempted to limit the overall probability of seeing a false cluster to $0.05$). In the Holm FWER calculation we set the total number of hypotheses equal to the total number of TCRs clustered across all alleles minus the cumulative neighbor-count of the cluster centers (we exclude cluster center neighbors since their neighbor counts are not independent of the neighbor count of the cluster center). When performing HLA-restricted clustering, each TCR$\beta$ chain was assigned to its most strongly associated HLA allele. Where two alleles had identical or nearly identical (within a factor of $1.25$) association p-values, the TCR chain was included in the clustering analysis for both alleles.

### Analyzing TCR clusters

For each (global or HLA-restricted) TCR cluster, we analyzed the occurrence patterns of the member TCRs in order to identify a subset of the (full or allele-positive) cohort enriched for those TCRs. We counted the number of cluster member TCRs found in each subject’s repertoire and sorted the subjects by this TCR count (rank plots in Figure 3B–C and in the right panels of Figure 7). For comparison, we generated control TCR count plots by independently resampling the subjects for each member TCR, preserving the frequency of each TCR and biasing by subject repertoire size. Each complete resampling of the cluster member TCR occurrence patterns produced a subject TCR rank plot; we repeated this resampling process $1000$ times and averaged the rank plots to yield the green (‘randomized’) curves in Figure 3B–C and Figure 7. To compare the observed and randomized curves, we took a signed difference

$$
D_{CO}=max1\leqi\leqN(\sumj\leqi (C_{j}−R_{j})+\sumj>i (R_{j}−C_{j}))
$$

between the observed counts $C_{j}$ and the randomized counts $R_{j}$, where the value of the subject index $i=i_{max}$ that maximizes the right-hand side in the equation above represents a switchpoint below which the observed counts generally exceed the randomized counts and above which the reverse is true (both sets of counts are sorted in decreasing order). We take this switchpoint $i_{max}$ as an estimate of the number of enriched subjects for the given cluster (this is the value given in the ‘Subjects’ column in Table 3).

**Table 3.**
 HLA-restricted TCR clusters with size ($S_{size}$) and co-occurrence ($Z_{CO}$) scores, annotations (abbreviated as in Figure 6), and validation scores.


<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>HLA allele</th>
      <th>Allele frequency</th>
      <th>TCRs</th>
      <th>Subjects</th>
      <th>Cluster center</th>
      <th>Ssize</th>
      <th>ZCO</th>
      <th>Annotations</th>
      <th>ZCOKeck120</th>
      <th>ZCOBrit86</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>A*24:02</td>
      <td>102</td>
      <td>32</td>
      <td>29</td>
      <td>TRBV05,CASSGSGGYNEQFF</td>
      <td>8.95</td>
      <td>17.64</td>
      <td>B19</td>
      <td>10.38</td>
      <td>6.74</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A*02:01</td>
      <td>218</td>
      <td>43</td>
      <td>66</td>
      <td>TRBV19,CASSGRSTDTQYF</td>
      <td>6.47</td>
      <td>13.01</td>
      <td>INF, T1D</td>
      <td>12.28</td>
      <td>4.28</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DRB1*07:01</td>
      <td>119</td>
      <td>17</td>
      <td>36</td>
      <td>TRBV09,CASSGQGAYEQYF</td>
      <td>4.08</td>
      <td>12.91</td>
      <td>coCMV</td>
      <td>9.46</td>
      <td>6.40</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DRB1*15:01-DQ</td>
      <td>112</td>
      <td>16</td>
      <td>27</td>
      <td>TRBV19,CASSPDRSSYNEQFF</td>
      <td>4.25</td>
      <td>12.13</td>
      <td></td>
      <td>1.65</td>
      <td>1.72</td>
    </tr>
    <tr>
      <td>5</td>
      <td>B*08:01</td>
      <td>115</td>
      <td>30</td>
      <td>34</td>
      <td>TRBV07,CASSQGPAYEQYF</td>
      <td>5.97</td>
      <td>8.12</td>
      <td>EBV, RA</td>
      <td>3.83</td>
      <td>1.83</td>
    </tr>
    <tr>
      <td>6</td>
      <td>C*04:01</td>
      <td>104</td>
      <td>7</td>
      <td>24</td>
      <td>TRBV19,CASSPGGDYNEQFF</td>
      <td>3.94</td>
      <td>11.58</td>
      <td></td>
      <td>4.48</td>
      <td>2.01</td>
    </tr>
    <tr>
      <td>7</td>
      <td>C*04:01</td>
      <td>104</td>
      <td>11</td>
      <td>20</td>
      <td>TRBV04,CASSHSGTGETYEQYF</td>
      <td>4.91</td>
      <td>9.03</td>
      <td></td>
      <td>7.52</td>
      <td>1.66</td>
    </tr>
    <tr>
      <td>8</td>
      <td>B*15:01</td>
      <td>55</td>
      <td>23</td>
      <td>27</td>
      <td>TRBV19,CASSTTSGSYNEQFF</td>
      <td>5.43</td>
      <td>7.51</td>
      <td></td>
      <td>10.31</td>
      <td>4.01</td>
    </tr>
    <tr>
      <td>9</td>
      <td>DRB1*03:01-DQ</td>
      <td>108</td>
      <td>26</td>
      <td>39</td>
      <td>TRBV29,CSVAPGWGMNTEAFF</td>
      <td>4.49</td>
      <td>8.61</td>
      <td></td>
      <td>10.96</td>
      <td>7.09</td>
    </tr>
    <tr>
      <td>10</td>
      <td>A*01:01</td>
      <td>154</td>
      <td>8</td>
      <td>44</td>
      <td>TRBV24,CATSDGDTQYF</td>
      <td>3.47</td>
      <td>10.21</td>
      <td>CMV, coCMV</td>
      <td>3.80</td>
      <td>2.42</td>
    </tr>
    <tr>
      <td>11</td>
      <td>B*35:01</td>
      <td>56</td>
      <td>18</td>
      <td>24</td>
      <td>TRBV10,CATGTGDSNQPQHF</td>
      <td>4.98</td>
      <td>6.13</td>
      <td>EBV, RA</td>
      <td>4.50</td>
      <td>5.42</td>
    </tr>
    <tr>
      <td>12</td>
      <td>DRB1*03:01-DQ</td>
      <td>108</td>
      <td>11</td>
      <td>35</td>
      <td>TRBV07,CASSLSLAGSYNEQFF</td>
      <td>3.09</td>
      <td>8.15</td>
      <td></td>
      <td>5.35</td>
      <td>1.40</td>
    </tr>
    <tr>
      <td>13</td>
      <td>A*02:01</td>
      <td>218</td>
      <td>10</td>
      <td>84</td>
      <td>TRBV20,CSARDRTGNGYTF</td>
      <td>3.81</td>
      <td>6.66</td>
      <td>EBV</td>
      <td>7.14</td>
      <td>3.50</td>
    </tr>
    <tr>
      <td>14</td>
      <td>DRB1*15:01-DQ</td>
      <td>112</td>
      <td>15</td>
      <td>38</td>
      <td>TRBV05,CASSLRGVRTDTQYF</td>
      <td>3.05</td>
      <td>8.08</td>
      <td></td>
      <td>8.73</td>
      <td>3.31</td>
    </tr>
    <tr>
      <td>15</td>
      <td>A*01:01</td>
      <td>154</td>
      <td>6</td>
      <td>30</td>
      <td>TRBV10,CAISESRASGDYNEQFF</td>
      <td>3.14</td>
      <td>7.67</td>
      <td></td>
      <td>11.31</td>
      <td>2.99</td>
    </tr>
    <tr>
      <td>16</td>
      <td>DRB1*13:01-DQ</td>
      <td>43</td>
      <td>7</td>
      <td>7</td>
      <td>TRBV20,CSASAGESNQPQHF</td>
      <td>3.14</td>
      <td>7.64</td>
      <td></td>
      <td>−0.55</td>
      <td>−0.35</td>
    </tr>
    <tr>
      <td>17</td>
      <td>DRB1*03:01-DQ</td>
      <td>108</td>
      <td>16</td>
      <td>32</td>
      <td>TRBV20,CSARGGGRSYEQYF</td>
      <td>3.31</td>
      <td>6.95</td>
      <td></td>
      <td>2.57</td>
      <td>3.09</td>
    </tr>
    <tr>
      <td>18</td>
      <td>DRB1*11:01</td>
      <td>58</td>
      <td>14</td>
      <td>20</td>
      <td>TRBV06,CASSYSVRGRYSNQPQHF</td>
      <td>3.26</td>
      <td>7.02</td>
      <td></td>
      <td>8.72</td>
      <td>3.44</td>
    </tr>
    <tr>
      <td>19</td>
      <td>C*08:02</td>
      <td>37</td>
      <td>6</td>
      <td>15</td>
      <td>TRBV28,CASSLGIHYEQYF</td>
      <td>3.53</td>
      <td>6.37</td>
      <td></td>
      <td>1.82</td>
      <td>4.37</td>
    </tr>
    <tr>
      <td>20</td>
      <td>DRB1*15:01-DQ</td>
      <td>112</td>
      <td>13</td>
      <td>51</td>
      <td>TRBV12,CASSLAGTEKLFF</td>
      <td>3.27</td>
      <td>6.64</td>
      <td></td>
      <td>4.61</td>
      <td>3.01</td>
    </tr>
    <tr>
      <td>21</td>
      <td>DRB1*03:01-DQ</td>
      <td>108</td>
      <td>11</td>
      <td>23</td>
      <td>TRBV05,CASSSTGLRSYEQYF</td>
      <td>3.09</td>
      <td>6.92</td>
      <td></td>
      <td>4.73</td>
      <td>5.81</td>
    </tr>
    <tr>
      <td>22</td>
      <td>A*02:01</td>
      <td>218</td>
      <td>7</td>
      <td>64</td>
      <td>TRBV04,CASSQGTGRYEQYF</td>
      <td>3.51</td>
      <td>6.07</td>
      <td></td>
      <td>2.79</td>
      <td>3.23</td>
    </tr>
    <tr>
      <td>23</td>
      <td>C*03:04</td>
      <td>72</td>
      <td>5</td>
      <td>13</td>
      <td>TRBV09,CASSVAYRGNEQFF</td>
      <td>3.39</td>
      <td>6.14</td>
      <td></td>
      <td>6.26</td>
      <td>3.23</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DQB1*03:01-DQA1*05:05</td>
      <td>84</td>
      <td>10</td>
      <td>39</td>
      <td>TRBV09,CASSVGTVQETQYF</td>
      <td>2.97</td>
      <td>6.73</td>
      <td></td>
      <td>3.02</td>
      <td>3.54</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DRB1*04:01</td>
      <td>78</td>
      <td>25</td>
      <td>35</td>
      <td>TRBV05,CASSRQGAGETQYF</td>
      <td>3.00</td>
      <td>6.31</td>
      <td></td>
      <td>5.82</td>
      <td>1.55</td>
    </tr>
    <tr>
      <td>26</td>
      <td>B*08:01</td>
      <td>115</td>
      <td>7</td>
      <td>30</td>
      <td>TRBV12,CASSFEGLHGYTF</td>
      <td>2.67</td>
      <td>6.67</td>
      <td></td>
      <td>3.77</td>
      <td>2.95</td>
    </tr>
    <tr>
      <td>27</td>
      <td>C*04:01</td>
      <td>104</td>
      <td>6</td>
      <td>25</td>
      <td>TRBV06,CASRTGLAGTDTQYF</td>
      <td>3.58</td>
      <td>4.78</td>
      <td></td>
      <td>3.53</td>
      <td>3.76</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DRB1*07:01</td>
      <td>119</td>
      <td>9</td>
      <td>42</td>
      <td>TRBV14,CASSLAGMNTEAFF</td>
      <td>3.15</td>
      <td>5.54</td>
      <td></td>
      <td>6.99</td>
      <td>5.58</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DQB1*03:01-DQA1*05:05</td>
      <td>84</td>
      <td>7</td>
      <td>36</td>
      <td>TRBV02,CASSELENTEAFF</td>
      <td>2.97</td>
      <td>5.76</td>
      <td></td>
      <td>5.25</td>
      <td>3.24</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DPB1*03:01-DPA1*01:03</td>
      <td>42</td>
      <td>7</td>
      <td>16</td>
      <td>TRBV30,CAWSADSNQPQHF</td>
      <td>3.56</td>
      <td>4.16</td>
      <td></td>
      <td>2.42</td>
      <td>1.73</td>
    </tr>
    <tr>
      <td>31</td>
      <td>B*15:01</td>
      <td>55</td>
      <td>18</td>
      <td>27</td>
      <td>TRBV29,CSVETRDYEQYF</td>
      <td>3.54</td>
      <td>3.94</td>
      <td></td>
      <td>13.81</td>
      <td>4.29</td>
    </tr>
    <tr>
      <td>32</td>
      <td>A*01:01</td>
      <td>154</td>
      <td>4</td>
      <td>26</td>
      <td>TRBV09,CASSVGVDSTDTQYF</td>
      <td>2.39</td>
      <td>6.24</td>
      <td></td>
      <td>−0.31</td>
      <td>2.17</td>
    </tr>
    <tr>
      <td>33</td>
      <td>C*07:02</td>
      <td>142</td>
      <td>4</td>
      <td>14</td>
      <td>TRBV25,CASSPGDEQYF</td>
      <td>2.94</td>
      <td>5.11</td>
      <td>coCMV</td>
      <td>6.37</td>
      <td>3.69</td>
    </tr>
    <tr>
      <td>34</td>
      <td>B*08:01</td>
      <td>115</td>
      <td>6</td>
      <td>38</td>
      <td>TRBV29,CSVGSGDYEQYF</td>
      <td>3.01</td>
      <td>4.85</td>
      <td>EBV</td>
      <td>2.73</td>
      <td>0.75</td>
    </tr>
    <tr>
      <td>35</td>
      <td>A*01:01</td>
      <td>154</td>
      <td>6</td>
      <td>37</td>
      <td>TRBV20,CSAPGQGAVEQYF</td>
      <td>2.79</td>
      <td>5.24</td>
      <td></td>
      <td>2.42</td>
      <td>3.00</td>
    </tr>
    <tr>
      <td>36</td>
      <td>A*23:01</td>
      <td>22</td>
      <td>5</td>
      <td>7</td>
      <td>TRBV06,CASSDGNSGNTIYF</td>
      <td>3.38</td>
      <td>4.02</td>
      <td></td>
      <td>1.91</td>
      <td>4.11</td>
    </tr>
    <tr>
      <td>37</td>
      <td>DQB1*03:01-DQA1*05:05</td>
      <td>84</td>
      <td>7</td>
      <td>29</td>
      <td>TRBV15,CATSRDPGGNQPQHF</td>
      <td>2.97</td>
      <td>4.82</td>
      <td></td>
      <td>5.00</td>
      <td>2.67</td>
    </tr>
    <tr>
      <td>38</td>
      <td>DPB1*04:01-DPA1*01:03</td>
      <td>274</td>
      <td>5</td>
      <td>65</td>
      <td>TRBV19,CASSIKGDTEAFF</td>
      <td>3.31</td>
      <td>4.14</td>
      <td></td>
      <td>4.89</td>
      <td>3.42</td>
    </tr>
    <tr>
      <td>39</td>
      <td>DPB1*04:01-DPA1*01:03</td>
      <td>274</td>
      <td>4</td>
      <td>55</td>
      <td>TRBV19,CASRLSGDTQYF</td>
      <td>2.84</td>
      <td>4.95</td>
      <td>COLO</td>
      <td>3.80</td>
      <td>1.25</td>
    </tr>
    <tr>
      <td>40</td>
      <td>B*07:02</td>
      <td>125</td>
      <td>7</td>
      <td>37</td>
      <td>TRBV02,CASRGETQYF</td>
      <td>2.73</td>
      <td>4.88</td>
      <td></td>
      <td>3.20</td>
      <td>2.11</td>
    </tr>
    <tr>
      <td>41</td>
      <td>B*44:03</td>
      <td>41</td>
      <td>9</td>
      <td>20</td>
      <td>TRBV19,CASSATGGIYEQYF</td>
      <td>3.35</td>
      <td>3.41</td>
      <td>MS</td>
      <td>6.61</td>
      <td>8.76</td>
    </tr>
    <tr>
      <td>42</td>
      <td>A*24:02</td>
      <td>102</td>
      <td>6</td>
      <td>31</td>
      <td>TRBV30,CAWSPGTGDYEQYF</td>
      <td>3.05</td>
      <td>3.91</td>
      <td></td>
      <td>3.56</td>
      <td>2.99</td>
    </tr>
    <tr>
      <td>43</td>
      <td>DRB1*07:01</td>
      <td>119</td>
      <td>13</td>
      <td>31</td>
      <td>TRBV18,CASSPSVRNTEAFF</td>
      <td>2.89</td>
      <td>4.20</td>
      <td></td>
      <td>5.32</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>44</td>
      <td>B*57:01</td>
      <td>27</td>
      <td>5</td>
      <td>14</td>
      <td>TRBV12,CASSPPEGETQYF</td>
      <td>3.22</td>
      <td>3.47</td>
      <td></td>
      <td>6.31</td>
      <td>1.94</td>
    </tr>
    <tr>
      <td>45</td>
      <td>C*06:02</td>
      <td>74</td>
      <td>4</td>
      <td>14</td>
      <td>TRBV02,CASSAGTASTDTQYF</td>
      <td>2.81</td>
      <td>4.27</td>
      <td>coCMV</td>
      <td>4.76</td>
      <td>3.06</td>
    </tr>
    <tr>
      <td>46</td>
      <td>A*11:01</td>
      <td>47</td>
      <td>5</td>
      <td>7</td>
      <td>TRBV09,CASSPKGVGYEQYF</td>
      <td>2.75</td>
      <td>4.31</td>
      <td></td>
      <td>2.43</td>
      <td>3.32</td>
    </tr>
    <tr>
      <td>47</td>
      <td>DRB1*01:01</td>
      <td>82</td>
      <td>9</td>
      <td>21</td>
      <td>TRBV19,CASSIPGLAYEQYF</td>
      <td>2.58</td>
      <td>4.63</td>
      <td></td>
      <td>0.96</td>
      <td>−0.49</td>
    </tr>
    <tr>
      <td>48</td>
      <td>B*07:02</td>
      <td>125</td>
      <td>7</td>
      <td>21</td>
      <td>TRBV09,CASSDRRGYTF</td>
      <td>2.73</td>
      <td>4.34</td>
      <td></td>
      <td>4.57</td>
      <td>0.45</td>
    </tr>
    <tr>
      <td>49</td>
      <td>B*08:01</td>
      <td>115</td>
      <td>6</td>
      <td>22</td>
      <td>TRBV07,CASSSTGAGNQPQHF</td>
      <td>2.67</td>
      <td>4.24</td>
      <td>EBV</td>
      <td>1.00</td>
      <td>2.85</td>
    </tr>
    <tr>
      <td>50</td>
      <td>B*18:01</td>
      <td>46</td>
      <td>5</td>
      <td>6</td>
      <td>TRBV27,CASSPTSEDTQYF</td>
      <td>2.57</td>
      <td>4.26</td>
      <td></td>
      <td>5.79</td>
      <td>−0.23</td>
    </tr>
    <tr>
      <td>51</td>
      <td>B*27:05</td>
      <td>36</td>
      <td>7</td>
      <td>13</td>
      <td>TRBV06,CASSLRLAGLYEQYF</td>
      <td>2.64</td>
      <td>3.81</td>
      <td></td>
      <td>9.25</td>
      <td>1.08</td>
    </tr>
    <tr>
      <td>52</td>
      <td>B*35:01</td>
      <td>56</td>
      <td>4</td>
      <td>7</td>
      <td>TRBV07,CASSQGPGRTYEQYF</td>
      <td>2.46</td>
      <td>4.10</td>
      <td></td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>53</td>
      <td>B*35:03</td>
      <td>16</td>
      <td>4</td>
      <td>7</td>
      <td>TRBV10,CAISVGNEQFF</td>
      <td>2.78</td>
      <td>3.42</td>
      <td></td>
      <td>1.50</td>
      <td>0.73</td>
    </tr>
    <tr>
      <td>54</td>
      <td>A*02:01</td>
      <td>218</td>
      <td>5</td>
      <td>126</td>
      <td>TRBV29,CSVGTGGTNEKLFF</td>
      <td>2.82</td>
      <td>3.32</td>
      <td>EBV, MELA</td>
      <td>5.65</td>
      <td>2.37</td>
    </tr>
    <tr>
      <td>55</td>
      <td>DRB1*03:01-DQ</td>
      <td>108</td>
      <td>6</td>
      <td>18</td>
      <td>TRBV02,CASSAGAGTEAFF</td>
      <td>2.36</td>
      <td>4.17</td>
      <td></td>
      <td>0.98</td>
      <td>2.79</td>
    </tr>
    <tr>
      <td>56</td>
      <td>B*44:02</td>
      <td>79</td>
      <td>4</td>
      <td>18</td>
      <td>TRBV02,CASSADSSYNEQFF</td>
      <td>2.57</td>
      <td>3.65</td>
      <td></td>
      <td>2.09</td>
      <td>2.12</td>
    </tr>
    <tr>
      <td>57</td>
      <td>C*03:04</td>
      <td>72</td>
      <td>3</td>
      <td>8</td>
      <td>TRBV27,CASSPRPYNEQFF</td>
      <td>2.35</td>
      <td>4.08</td>
      <td></td>
      <td>1.36</td>
      <td>3.22</td>
    </tr>
    <tr>
      <td>58</td>
      <td>A*24:02</td>
      <td>102</td>
      <td>4</td>
      <td>12</td>
      <td>TRBV20,CSAREDGHEQYF</td>
      <td>2.62</td>
      <td>3.54</td>
      <td></td>
      <td>0.83</td>
      <td>2.94</td>
    </tr>
    <tr>
      <td>59</td>
      <td>A*01:01</td>
      <td>154</td>
      <td>12</td>
      <td>65</td>
      <td>TRBV19,CASSIRDHNQPQHF</td>
      <td>2.79</td>
      <td>3.17</td>
      <td></td>
      <td>8.44</td>
      <td>2.33</td>
    </tr>
    <tr>
      <td>60</td>
      <td>B*27:05</td>
      <td>36</td>
      <td>4</td>
      <td>12</td>
      <td>TRBV07,CASSPPGGSAYNEQFF</td>
      <td>2.64</td>
      <td>3.23</td>
      <td></td>
      <td>1.13</td>
      <td>2.12</td>
    </tr>
    <tr>
      <td>61</td>
      <td>C*14:02</td>
      <td>23</td>
      <td>4</td>
      <td>9</td>
      <td>TRBV02,CASSGDTSTNEKLFF</td>
      <td>2.48</td>
      <td>3.50</td>
      <td></td>
      <td>6.23</td>
      <td>-</td>
    </tr>
    <tr>
      <td>62</td>
      <td>B*27:05</td>
      <td>36</td>
      <td>9</td>
      <td>12</td>
      <td>TRBV27,CASSSGTSGNNEQFF</td>
      <td>2.64</td>
      <td>3.16</td>
      <td></td>
      <td>4.32</td>
      <td>3.24</td>
    </tr>
    <tr>
      <td>63</td>
      <td>C*12:03</td>
      <td>53</td>
      <td>6</td>
      <td>25</td>
      <td>TRBV15,CATSRENEKLFF</td>
      <td>2.90</td>
      <td>2.51</td>
      <td></td>
      <td>1.88</td>
      <td>3.08</td>
    </tr>
    <tr>
      <td>64</td>
      <td>A*68:01</td>
      <td>29</td>
      <td>4</td>
      <td>16</td>
      <td>TRBV05,CASSLIATNEKLFF</td>
      <td>2.71</td>
      <td>2.88</td>
      <td></td>
      <td>3.67</td>
      <td>1.23</td>
    </tr>
    <tr>
      <td>65</td>
      <td>B*51:01</td>
      <td>53</td>
      <td>6</td>
      <td>20</td>
      <td>TRBV04,CASSQDYPGGSYEQYF</td>
      <td>2.76</td>
      <td>2.73</td>
      <td></td>
      <td>6.43</td>
      <td>5.18</td>
    </tr>
    <tr>
      <td>66</td>
      <td>B*35:01</td>
      <td>56</td>
      <td>4</td>
      <td>8</td>
      <td>TRBV27,CASSLGAATGELFF</td>
      <td>2.46</td>
      <td>3.32</td>
      <td></td>
      <td>4.52</td>
      <td>3.01</td>
    </tr>
    <tr>
      <td>67</td>
      <td>B*15:01</td>
      <td>55</td>
      <td>4</td>
      <td>20</td>
      <td>TRBV06,CASSAGTGRYEQYF</td>
      <td>2.44</td>
      <td>3.18</td>
      <td></td>
      <td>2.40</td>
      <td>2.23</td>
    </tr>
    <tr>
      <td>68</td>
      <td>B*44:03</td>
      <td>41</td>
      <td>7</td>
      <td>14</td>
      <td>TRBV07,CASSSGESGANVLTF</td>
      <td>2.97</td>
      <td>2.01</td>
      <td></td>
      <td>3.92</td>
      <td>4.81</td>
    </tr>
    <tr>
      <td>69</td>
      <td>DRB1*04:02</td>
      <td>14</td>
      <td>4</td>
      <td>6</td>
      <td>TRBV03,CASSQASGGANEQFF</td>
      <td>2.44</td>
      <td>3.04</td>
      <td></td>
      <td>2.04</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td>70</td>
      <td>B*15:01</td>
      <td>55</td>
      <td>4</td>
      <td>10</td>
      <td>TRBV19,CASSHRGGNEQFF</td>
      <td>2.44</td>
      <td>3.03</td>
      <td></td>
      <td>0.92</td>
      <td>3.58</td>
    </tr>
    <tr>
      <td>71</td>
      <td>B*15:01</td>
      <td>55</td>
      <td>5</td>
      <td>7</td>
      <td>TRBV05,CASSLGVSAGELFF</td>
      <td>2.44</td>
      <td>2.98</td>
      <td></td>
      <td>−0.32</td>
      <td>−0.12</td>
    </tr>
    <tr>
      <td>72</td>
      <td>A*32:01</td>
      <td>34</td>
      <td>3</td>
      <td>5</td>
      <td>TRBV12,CASSYGPGNQPQHF</td>
      <td>2.45</td>
      <td>2.84</td>
      <td></td>
      <td>5.76</td>
      <td>3.18</td>
    </tr>
    <tr>
      <td>73</td>
      <td>A*02:01</td>
      <td>218</td>
      <td>4</td>
      <td>23</td>
      <td>TRBV19,CASSTGTATNEKLFF</td>
      <td>2.42</td>
      <td>2.89</td>
      <td></td>
      <td>0.84</td>
      <td>-</td>
    </tr>
    <tr>
      <td>74</td>
      <td>DRB1*15:01-DQ</td>
      <td>112</td>
      <td>7</td>
      <td>51</td>
      <td>TRBV28,CASSLLGGQPQHF</td>
      <td>2.58</td>
      <td>2.35</td>
      <td></td>
      <td>0.66</td>
      <td>1.89</td>
    </tr>
    <tr>
      <td>75</td>
      <td>B*18:01</td>
      <td>46</td>
      <td>5</td>
      <td>15</td>
      <td>TRBV27,CASSFPGKEQYF</td>
      <td>2.57</td>
      <td>2.22</td>
      <td></td>
      <td>−0.35</td>
      <td>5.62</td>
    </tr>
    <tr>
      <td>76</td>
      <td>B*49:01</td>
      <td>16</td>
      <td>3</td>
      <td>8</td>
      <td>TRBV29,CSVERGYNEQFF</td>
      <td>2.38</td>
      <td>2.14</td>
      <td></td>
      <td>1.03</td>
      <td>0.43</td>
    </tr>
    <tr>
      <td>77</td>
      <td>A*23:01</td>
      <td>22</td>
      <td>3</td>
      <td>6</td>
      <td>TRBV20,CSARDREGAGYGYTF</td>
      <td>2.35</td>
      <td>2.14</td>
      <td></td>
      <td>−0.16</td>
      <td>−0.12</td>
    </tr>
    <tr>
      <td>78</td>
      <td>B*55:01</td>
      <td>13</td>
      <td>3</td>
      <td>10</td>
      <td>TRBV19,CASRGGNQPQHF</td>
      <td>2.36</td>
      <td>2.09</td>
      <td></td>
      <td>0.95</td>
      <td>−0.28</td>
    </tr>
  </tbody>
</table>

Since the raw $D_{CO}$ values are not comparable between clusters of different sizes and for different alleles, we transformed these values to a Z-score ($Z_{CO}$) by generating, for each cluster, $1000$ additional random TCR count curves and computing the mean ($\mu_{D}$) and standard deviation ($\sigma_{D}$) of their $D_{CO}^{rand}$ score distribution:

$$
Z_{CO}=\frac{D_{CO}−\mu_{D}}{\sigma_{D}}
$$

We used this co-occurrence score $Z_{CO}$ together with a log-transformed version of the cluster size p-value,

$$
S_{size}=\sqrt{−log_{10}⁡(P_{size})}
$$

for visualizing clustering results in Figure 6 ($S_{size}$ on the $x$-axis and $Z_{CO}$ on the $y$-axis) and prioritizing individual clusters for detailed follow-up.

### TCR annotations

We annotated public TCRs in our dataset by matching their sequences against two publicly available datasets: VDJdb (Shugay et al., 2018), a curated database of TCR sequences with known antigen specificities (downloaded on 3/29/18; about $17,000$ human TCR$\beta$ entries) and McPAS-TCR (Tickotsky et al., 2017), a curated database of pathogen-associated TCR sequences (downloaded on 3/29/18; about $9,000$ human TCR$\beta$ entries). VDJdb entries are associated with a specific MHC-presented epitope, whereas McPAS-TCR also includes sequences of TCRs isolated from diseased tissues whose epitope specificity is not defined. We added to this merged annotation database the sequences of structurally characterized TCRs of known specificity (see below), as well as literature-derived TCRs from a handful of primary studies (Dash et al., 2017; Glanville et al., 2017; Song et al., 2017; Kasprowicz et al., 2006). For matches between HLA-associated TCRs and database TCRs of known specificity, we filtered for agreement (at 2-digit resolution) between the associated HLA allele in our dataset and the presenting allele from the database. In other words, TCRs belonging to B*08:01-restricted clusters were not annotated with matches to database TCRs that bind to A*02:01-presented peptides.

### Structural analysis

We analyzed a set of experimentally determined TCR:peptide-MHC structures to find MHC positions frequently contacted by the CDR3$\beta$ loop. Crystal structures of complexes involving human TCRs and human class I or class II HLA alleles (Table 4) were identified using BLAST (Altschul et al., 1997) searches against the RCSB PDB (Berman et al., 2000) sequence database (ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt). Structural coverage of HLA loci and alleles is sparse and highly biased toward well studied alleles such as HLA-A*02. Given the high degree of structural similarity among class I and among class II MHC structures solved to date, we elected to share contact information across loci using trans-locus sequence alignments. For class I we used the merged alignment (ClassI_prot.txt) available from the IPD-IMGT/HLA (Robinson et al., 2015) database. Starting with multiple sequence alignments for individual class II loci from the IPD-IMGT/HLA database, we inserted gaps as needed in order to created merged alignments for the class II $\alpha$ and $\beta$ chains. These alignments provided a common reference frame in which to combine residue-residue contacts from the TCR:peptide-MHC structures. We considered two amino acid residues to be in contact if they had a side chain heavyatom contact distance less than or equal to $4.5$Å. The CDR3$\beta$ contact frequency for an alignment position (class I, class II-$\alpha$, or class II-$\beta$) was defined to be the total number of contacted CDR3$\beta$ amino acids observed for that position, divided by the total number of structures analyzed. Redundancy in the structural database was assessed at the level of TCR and HLA sequence, ignoring the sequence of the peptide. Contacts from a set of $n$ structures all containing the same TCR and HLA were given a weight of $1/n$ when computing the residue contact frequencies. The statistical significance of correlations between HLA allele charge and average HLA-associated TCR CDR3 charge were computed using a 2-sided test as implemented in the function scipy.stats.linregress.

**Table 4.**
 PDB structures analyzed.


<table>
  <thead>
    <tr>
      <th>PDB ID*</th>
      <th>HLA allele</th>
      <th>Vα</th>
      <th>Jα</th>
      <th>CDR3α</th>
      <th>Vβ</th>
      <th>Jβ</th>
      <th>CDR3β</th>
      <th>Peptide</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5bs0</td>
      <td>A*01</td>
      <td>TRAV21*01</td>
      <td>TRAJ28*01</td>
      <td>CAVRPGGAGPFFVVF</td>
      <td>TRBV5-1*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSFNMATGQYF</td>
      <td>ESDPIVAQY</td>
    </tr>
    <tr>
      <td>3qdj</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ23*01</td>
      <td>CAVNFGGGKLIF</td>
      <td>TRBV6-4*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASSLSFGTEAFF</td>
      <td>AAGIGILTV</td>
    </tr>
    <tr>
      <td>4l3e</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ23*01</td>
      <td>CAVNFGGGKLIF</td>
      <td>TRBV6-4*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASSWSFGTEAFF</td>
      <td>ELAGIGILTV</td>
    </tr>
    <tr>
      <td>5e9d</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ24*02</td>
      <td>CAVTKYSWGKLQF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASRPGWMAGGVELYF</td>
      <td>ELAGIGILTV</td>
    </tr>
    <tr>
      <td>3qfj</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ24*02</td>
      <td>CAVTTDSWGKLQF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASRPGLAGGRPEQYF</td>
      <td>LLFGFPVYV</td>
    </tr>
    <tr>
      <td>4ftv</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ24*02</td>
      <td>CAVTTDSWGKLQF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASRPGLMSAQPEQYF</td>
      <td>LLFGYPVYV</td>
    </tr>
    <tr>
      <td>3hg1</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ27*01</td>
      <td>CAVNVAGKSTF</td>
      <td>TRBV30*01</td>
      <td>TRBJ2-2*01</td>
      <td>CAWSETGLGTGELFF</td>
      <td>ELAGIGILTV</td>
    </tr>
    <tr>
      <td>4eup</td>
      <td>A*02</td>
      <td>TRAV12-2*01</td>
      <td>TRAJ45*01</td>
      <td>CAVSGGGADGLTF</td>
      <td>TRBV28*01</td>
      <td>TRBJ2-1*01</td>
      <td>CASSFLGTGVEQYF</td>
      <td>ALGIGILTV</td>
    </tr>
    <tr>
      <td>5c0c</td>
      <td>A*02</td>
      <td>TRAV12-3*01</td>
      <td>TRAJ12*01</td>
      <td>CAMRGDSSYKLIF</td>
      <td>TRBV12-4*01</td>
      <td>TRBJ2-4*01</td>
      <td>CASSLWEKLAKNIQYF</td>
      <td>RQFGPDWIVA</td>
    </tr>
    <tr>
      <td>5eu6</td>
      <td>A*02</td>
      <td>TRAV21*01</td>
      <td>TRAJ53*01</td>
      <td>CAVLSSGGSNYKLTF</td>
      <td>TRBV7-3*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSFIGGTDTQYF</td>
      <td>YLEPGPVTV</td>
    </tr>
    <tr>
      <td>2p5e</td>
      <td>A*02</td>
      <td>TRAV21*01</td>
      <td>TRAJ6*01</td>
      <td>CAVRPLLDGTYIPTF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSYLGNTGELFF</td>
      <td>SLLMWITQC</td>
    </tr>
    <tr>
      <td>2bnq</td>
      <td>A*02</td>
      <td>TRAV21*01</td>
      <td>TRAJ6*01</td>
      <td>CAVRPTSGGSYIPTF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSYVGNTGELFF</td>
      <td>SLLMWITQV</td>
    </tr>
    <tr>
      <td>4mnq</td>
      <td>A*02</td>
      <td>TRAV22*01</td>
      <td>TRAJ40*01</td>
      <td>CAVDSATALPYGYIF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASSYQGTEAFF</td>
      <td>ILAKFLHWL</td>
    </tr>
    <tr>
      <td>5men</td>
      <td>A*02</td>
      <td>TRAV22*01</td>
      <td>TRAJ40*01</td>
      <td>CAVDSATSGTYKYIF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASSYQGTEAFF</td>
      <td>ILAKFLHWL</td>
    </tr>
    <tr>
      <td>5isz</td>
      <td>A*02</td>
      <td>TRAV24*01</td>
      <td>TRAJ27*01</td>
      <td>CAFDTNAGKSTF</td>
      <td>TRBV19*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSIFGQREQYF</td>
      <td>GILGFVFTL</td>
    </tr>
    <tr>
      <td>5d2l</td>
      <td>A*02</td>
      <td>TRAV24*01</td>
      <td>TRAJ49*01</td>
      <td>CAFITGNQFYF</td>
      <td>TRBV7-2*02</td>
      <td>TRBJ2-5*01</td>
      <td>CASSQTQLWETQYF</td>
      <td>NLVPMVATV</td>
    </tr>
    <tr>
      <td>3gsn</td>
      <td>A*02</td>
      <td>TRAV24*01</td>
      <td>TRAJ49*01</td>
      <td>CARNTGNQFYF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ1-2*01</td>
      <td>CASSPVTGGIYGYTF</td>
      <td>NLVPMVATV</td>
    </tr>
    <tr>
      <td>5d2n</td>
      <td>A*02</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ43*01</td>
      <td>CILDNNNDMRF</td>
      <td>TRBV7-6*01</td>
      <td>TRBJ1-4*01</td>
      <td>CASSLAPGTTNEKLFF</td>
      <td>NLVPMVATV</td>
    </tr>
    <tr>
      <td>5euo</td>
      <td>A*02</td>
      <td>TRAV27*01</td>
      <td>TRAJ37*02</td>
      <td>CAGAIGPSNTGKLIF</td>
      <td>TRBV19*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSIRSSYEQYF</td>
      <td>GILGFVFTL</td>
    </tr>
    <tr>
      <td>5hho</td>
      <td>A*02</td>
      <td>TRAV27*01</td>
      <td>TRAJ42*01</td>
      <td>CAGAGSQGNLIF</td>
      <td>TRBV19*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSIRSSYEQYF</td>
      <td>GILEFVFTL</td>
    </tr>
    <tr>
      <td>2vlr</td>
      <td>A*02</td>
      <td>TRAV27*01</td>
      <td>TRAJ42*01</td>
      <td>CAGAGSQGNLIF</td>
      <td>TRBV19*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSSRASYEQYF</td>
      <td>GILGFVFTL</td>
    </tr>
    <tr>
      <td>1oga</td>
      <td>A*02</td>
      <td>TRAV27*01</td>
      <td>TRAJ42*01</td>
      <td>CAGAGSQGNLIF</td>
      <td>TRBV19*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSSRSSYEQYF</td>
      <td>GILGFVFTL</td>
    </tr>
    <tr>
      <td>1bd2</td>
      <td>A*02</td>
      <td>TRAV29/DV5*01</td>
      <td>TRAJ54*01</td>
      <td>CAAMEGAQKLVF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSYPGGGFYEQYF</td>
      <td>LLFGYPVYV</td>
    </tr>
    <tr>
      <td>5e6i</td>
      <td>A*02</td>
      <td>TRAV35*01</td>
      <td>TRAJ37*02</td>
      <td>CAGPGGSSNTGKLIF</td>
      <td>TRBV27*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSLIYPGELFF</td>
      <td>GILGFVFTL</td>
    </tr>
    <tr>
      <td>3qeq</td>
      <td>A*02</td>
      <td>TRAV35*01</td>
      <td>TRAJ49*01</td>
      <td>CAGGTGNQFYF</td>
      <td>TRBV10-3*01</td>
      <td>TRBJ1-5*01</td>
      <td>CAISEVGVGQPQHF</td>
      <td>AAGIGILTV</td>
    </tr>
    <tr>
      <td>4zez</td>
      <td>A*02</td>
      <td>TRAV38-2/DV8*01</td>
      <td>TRAJ30*01</td>
      <td>CAYGEDDKIIF</td>
      <td>TRBV25-1*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASRRGPYEQYF</td>
      <td>KLVALVINAV</td>
    </tr>
    <tr>
      <td>5jhd</td>
      <td>A*02</td>
      <td>TRAV38-2/DV8*01</td>
      <td>TRAJ52*01</td>
      <td>CAWGVNAGGTSYGKLTF</td>
      <td>TRBV19*01</td>
      <td>TRBJ1-2*01</td>
      <td>CASSIGVYGYTF</td>
      <td>GILGFVFTL</td>
    </tr>
    <tr>
      <td>3o4l</td>
      <td>A*02</td>
      <td>TRAV5*01</td>
      <td>TRAJ31*01</td>
      <td>CAEDNNARLMF</td>
      <td>TRBV20-1*01</td>
      <td>TRBJ1-2*01</td>
      <td>CSARDGTGNGYTF</td>
      <td>GLCTLVAML</td>
    </tr>
    <tr>
      <td>3vxs</td>
      <td>A*24</td>
      <td>TRAV21*01</td>
      <td>TRAJ12*01</td>
      <td>CAVRMDSSYKLIF</td>
      <td>TRBV7-9*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSSWDTGELFF</td>
      <td>RYPLTLGWCF</td>
    </tr>
    <tr>
      <td>3vxm</td>
      <td>A*24</td>
      <td>TRAV8-3*01</td>
      <td>TRAJ28*01</td>
      <td>CAVGAPSGAGSYQLTF</td>
      <td>TRBV4-1*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSPTSGIYEQYF</td>
      <td>RFPLTFGWCF</td>
    </tr>
    <tr>
      <td>3sjv</td>
      <td>B*08</td>
      <td>TRAV12-1*01</td>
      <td>TRAJ23*01</td>
      <td>CVVRAGKLIF</td>
      <td>TRBV6-2*01</td>
      <td>TRBJ2-4*01</td>
      <td>CASGQGNFDIQYF</td>
      <td>FLRGRAYGL</td>
    </tr>
    <tr>
      <td>3ffc</td>
      <td>B*08</td>
      <td>TRAV14/DV4*01</td>
      <td>TRAJ49*01</td>
      <td>CAMREDTGNQFYF</td>
      <td>TRBV11-2*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSFTWTSGGATDTQYF</td>
      <td>FLRGRAYGL</td>
    </tr>
    <tr>
      <td>1mi5</td>
      <td>B*08</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ52*01</td>
      <td>CILPLAGGTSYGKLTF</td>
      <td>TRBV7-8*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSLGQAYEQYF</td>
      <td>FLRGRAYGL</td>
    </tr>
    <tr>
      <td>4qrp</td>
      <td>B*08</td>
      <td>TRAV9-2*01</td>
      <td>TRAJ43*01</td>
      <td>CALSDPVNDMRF</td>
      <td>TRBV11-2*01</td>
      <td>TRBJ1-5*01</td>
      <td>CASSLRGRGDQPQHF</td>
      <td>HSKKKCDEL</td>
    </tr>
    <tr>
      <td>4g9f</td>
      <td>B*27</td>
      <td>TRAV14/DV4*02</td>
      <td>TRAJ21*01</td>
      <td>CAMRDLRDNFNKFYF</td>
      <td>TRBV6-5*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASREGLGGTEAFF</td>
      <td>KRWIIMGLNK</td>
    </tr>
    <tr>
      <td>4jrx</td>
      <td>B*35</td>
      <td>TRAV19*01</td>
      <td>TRAJ34*01</td>
      <td>CALSGFYNTDKLIF</td>
      <td>TRBV6-1*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASPGETEAFF</td>
      <td>LPEPLPQGQLTAY</td>
    </tr>
    <tr>
      <td>2ak4</td>
      <td>B*35</td>
      <td>TRAV19*01</td>
      <td>TRAJ34*01</td>
      <td>CALSGFYNTDKLIF</td>
      <td>TRBV6-1*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASPGLAGEYEQYF</td>
      <td>LPEPLPQGQLTAY</td>
    </tr>
    <tr>
      <td>3mv7</td>
      <td>B*35</td>
      <td>TRAV20*01</td>
      <td>TRAJ58*01</td>
      <td>CAVQDLGTSGSRLTF</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSARSGELFF</td>
      <td>HPVGEADYFEY</td>
    </tr>
    <tr>
      <td>4jry</td>
      <td>B*35</td>
      <td>TRAV39*01</td>
      <td>TRAJ33*01</td>
      <td>CAVGGGSNYQLIW</td>
      <td>TRBV5-6*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSRTGSTYEQYF</td>
      <td>LPEPLPQGQLTAY</td>
    </tr>
    <tr>
      <td>3dxa</td>
      <td>B*44</td>
      <td>TRAV26-1*01</td>
      <td>TRAJ13*02</td>
      <td>CIVWGGYQKVTF</td>
      <td>TRBV7-9*01</td>
      <td>TRBJ2-1*01</td>
      <td>CASRYRDDSYNEQFF</td>
      <td>EENLLDFVRF</td>
    </tr>
    <tr>
      <td>3kpr</td>
      <td>B*44</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ52*01</td>
      <td>CILPLAGGTSYGKLTF</td>
      <td>TRBV7-8*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSLGQAYEQYF</td>
      <td>EEYLKAWTF</td>
    </tr>
    <tr>
      <td>4mji</td>
      <td>B*51</td>
      <td>TRAV17*01</td>
      <td>TRAJ22*01</td>
      <td>CATDDDSARQLTF</td>
      <td>TRBV7-3*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSLTGGGELFF</td>
      <td>TAFTIPSI</td>
    </tr>
    <tr>
      <td>2ypl</td>
      <td>B*57</td>
      <td>TRAV5*01</td>
      <td>TRAJ13*01</td>
      <td>CAVSGGYQKVTF</td>
      <td>TRBV19*01</td>
      <td>TRBJ1-2*01</td>
      <td>CASTGSYGYTF</td>
      <td>KAFSPEVIPMF</td>
    </tr>
    <tr>
      <td>4p4k</td>
      <td>DPA1*01/DPB1*352</td>
      <td>TRAV9-2*01</td>
      <td>TRAJ28*01</td>
      <td>CALSLYSGAGSYQLTF</td>
      <td>TRBV5-1*01</td>
      <td>TRBJ2-5*01</td>
      <td>CASSLAQGGETQYF</td>
      <td>QAFWIDLFETIG</td>
    </tr>
    <tr>
      <td>4may</td>
      <td>DQA1*01/DQB1*05</td>
      <td>TRAV13-1*01</td>
      <td>TRAJ48*01</td>
      <td>CAASSFGNEKLTF</td>
      <td>TRBV7-3*01</td>
      <td>TRBJ2-3*01</td>
      <td>CATSALGDTQYF</td>
      <td>QLVHFVRDFAQL</td>
    </tr>
    <tr>
      <td>5ks9</td>
      <td>DQA1*03/DQB1*03</td>
      <td>TRAV20*01</td>
      <td>TRAJ39*01</td>
      <td>CAVALNNNAGNMLTF</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSVAPGSDTQYF</td>
      <td>APSGEGSFQPSQENPQ</td>
    </tr>
    <tr>
      <td>4gg6</td>
      <td>DQA1*03/DQB1*03</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ45*01</td>
      <td>CILRDGRGGADGLTF</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSVAVSAGTYEQYF</td>
      <td>QQYPSGEGSFQPSQENPQ</td>
    </tr>
    <tr>
      <td>4z7u</td>
      <td>DQA1*03/DQB1*03</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ49*01</td>
      <td>CILRDRSNQFYF</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-5*01</td>
      <td>CASSTTPGTGTETQYF</td>
      <td>APSGEGSFQPSQENPQGS</td>
    </tr>
    <tr>
      <td>4z7v</td>
      <td>DQA1*03/DQB1*03</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ54*01</td>
      <td>CILRDSRAQKLVF</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSAGTSGEYEQYF</td>
      <td>APSGEGSFQPSQENPQGS</td>
    </tr>
    <tr>
      <td>4z7w</td>
      <td>DQA1*03/DQB1*03</td>
      <td>TRAV8-3*01</td>
      <td>TRAJ36*01</td>
      <td>CAVGETGANNLFF</td>
      <td>TRBV6-1*01</td>
      <td>TRBJ2-1*01</td>
      <td>CASSEARRYNEQFF</td>
      <td>APSGEGSFQPSQENPQGS</td>
    </tr>
    <tr>
      <td>4ozh</td>
      <td>DQA1*05/DQB1*02</td>
      <td>TRAV26-1*01</td>
      <td>TRAJ32*01</td>
      <td>CIVWGGATNKLIF</td>
      <td>TRBV7-2*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSVRSTDTQYF</td>
      <td>APQPELPYPQPGS</td>
    </tr>
    <tr>
      <td>4ozg</td>
      <td>DQA1*05/DQB1*02</td>
      <td>TRAV26-1*01</td>
      <td>TRAJ45*01</td>
      <td>CIVLGGADGLTF</td>
      <td>TRBV7-2*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSFRFTDTQYF</td>
      <td>APQPELPYPQPGS</td>
    </tr>
    <tr>
      <td>4ozf</td>
      <td>DQA1*05/DQB1*02</td>
      <td>TRAV26-1*01</td>
      <td>TRAJ54*01</td>
      <td>CIAFQGAQKLVF</td>
      <td>TRBV7-2*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSFRALAADTQYF</td>
      <td>APQPELPYPQPGS</td>
    </tr>
    <tr>
      <td>4ozi</td>
      <td>DQA1*05/DQB1*02</td>
      <td>TRAV4*01</td>
      <td>TRAJ4*01</td>
      <td>CLVGDGGSFSGGYNKLIF</td>
      <td>TRBV20-1*01</td>
      <td>TRBJ2-5*01</td>
      <td>CSAGVGGQETQYF</td>
      <td>QPFPQPELPYPGS</td>
    </tr>
    <tr>
      <td>5ksa</td>
      <td>DQA1*05/DQB1*03</td>
      <td>TRAV20*01</td>
      <td>TRAJ33*01</td>
      <td>CAVQFMDSNYQLIW</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-7*01</td>
      <td>CASSVAGTPSYEQYF</td>
      <td>QPQQSFPEQEA</td>
    </tr>
    <tr>
      <td>5ksb</td>
      <td>DQA1*05/DQB1*03</td>
      <td>TRAV20*01</td>
      <td>TRAJ6*01</td>
      <td>CAVQASGGSYIPTF</td>
      <td>TRBV9*01</td>
      <td>TRBJ2-3*01</td>
      <td>CASSNRGLGTDTQYF</td>
      <td>GPQQSFPEQEA</td>
    </tr>
    <tr>
      <td>4e41</td>
      <td>DRA*01/DRB1*01</td>
      <td>TRAV22*01</td>
      <td>TRAJ18*01</td>
      <td>CAVDRGSTLGRLYF</td>
      <td>TRBV5-8*01</td>
      <td>TRBJ2-5*01</td>
      <td>CASSQIRETQYF</td>
      <td>GELIGILNAAKVPAD</td>
    </tr>
    <tr>
      <td>2iam</td>
      <td>DRA*01/DRB1*01</td>
      <td>TRAV22*01</td>
      <td>TRAJ54*01</td>
      <td>CAALIQGAQKLVF</td>
      <td>TRBV6-6*01</td>
      <td>TRBJ1-3*01</td>
      <td>CASTYHGTGYF</td>
      <td>GELIGILNAAKVPAD</td>
    </tr>
    <tr>
      <td>1fyt</td>
      <td>DRA*01/DRB1*01</td>
      <td>TRAV8-4*01</td>
      <td>TRAJ48*01</td>
      <td>CAVSESPFGNEKLTF</td>
      <td>TRBV28*01</td>
      <td>TRBJ1-2*01</td>
      <td>CASSSTGLPYGYTF</td>
      <td>PKYVKQNTLKLAT</td>
    </tr>
    <tr>
      <td>3o6f</td>
      <td>DRA*01/DRB1*04</td>
      <td>TRAV26-2*01</td>
      <td>TRAJ32*01</td>
      <td>CTVYGGATNKLIF</td>
      <td>TRBV20-1*01</td>
      <td>TRBJ1-6*01</td>
      <td>CSARGGSYNSPLHF</td>
      <td>FSWGAEGQRPGFGSGG</td>
    </tr>
    <tr>
      <td>1j8h</td>
      <td>DRA*01/DRB1*04</td>
      <td>TRAV8-4*01</td>
      <td>TRAJ48*01</td>
      <td>CAVSESPFGNEKLTF</td>
      <td>TRBV28*01</td>
      <td>TRBJ1-2*01</td>
      <td>CASSSTGLPYGYTF</td>
      <td>PKYVKQNTLKLAT</td>
    </tr>
    <tr>
      <td>2wbj</td>
      <td>DRA*01/DRB1*15</td>
      <td>TRAV17*01</td>
      <td>TRAJ40*01</td>
      <td>CATDTTSGTYKYIF</td>
      <td>TRBV20-1*01</td>
      <td>TRBJ2-1*01</td>
      <td>CSARDLTSGANNEQFF</td>
      <td>MDFARVHFISALHGSGG</td>
    </tr>
    <tr>
      <td>4h1l</td>
      <td>DRA*01/DRB3*03</td>
      <td>TRAV8-3*01</td>
      <td>TRAJ37*01</td>
      <td>CAVGASGNTGKLIF</td>
      <td>TRBV19*01</td>
      <td>TRBJ2-2*01</td>
      <td>CASSLRDGYTGELFF</td>
      <td>QHIRCNIPKRISA</td>
    </tr>
    <tr>
      <td>1zgl</td>
      <td>DRA*01/DRB5*01</td>
      <td>TRAV9-2*01</td>
      <td>TRAJ12*01</td>
      <td>CALSGGDSSYKLIF</td>
      <td>TRBV5-1*01</td>
      <td>TRBJ1-1*01</td>
      <td>CASSLADRVNTEAFF</td>
      <td>VHFFKNIVTPRTPGG</td>
    </tr>
  </tbody>
</table>

_*If there are multiple structures with the same TCR and HLA allele, only the ID of the highest-resolution structure is given. During CDR3β contact analysis, however, we combined the contacts from all redundant structures, downweighting so as to equalize the contribution from all TCR/HLA pairs._

### Software availability

C++ source code implementing the clustering, generation probability, and correlation algorithms described here is available at https://github.com/phbradley/pubtcrs (copy archived at https://github.com/elifesciences-publications/pubtcrs [Bradley, 2018]).
