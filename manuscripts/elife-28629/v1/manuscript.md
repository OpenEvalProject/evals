# Inferring genetic interactions from comparative fitness data

## Authors

- Kristina Crona<sup>1</sup> ([ORCID: 0000-0003-1819-474X](https://orcid.org/0000-0003-1819-474X))
- Alex Gavryushkin<sup>2</sup> ([ORCID: 0000-0001-6299-8249](https://orcid.org/0000-0001-6299-8249))
- Devin Greene<sup>1</sup> ([ORCID: 0000-0002-4889-9225](https://orcid.org/0000-0002-4889-9225))
- Niko Beerenwinkel<sup>2</sup> ([ORCID: 0000-0002-0573-6119](https://orcid.org/0000-0002-0573-6119)) †

### Affiliations

1. Department of Mathematics and Statistics American University Washington, DC United States
2. Department of Biosystems Science and Engineering ETH Zurich Basel Switzerland
3. SIB Swiss Institute of Bioinformatics Basel Switzerland

† Corresponding author

## Abstract

10.7554/eLife.28629.001 Darwinian fitness is a central concept in evolutionary biology. In practice, however, it is hardly possible to measure fitness for all genotypes in a natural population. Here, we present quantitative tools to make inferences about epistatic gene interactions when the fitness landscape is only incompletely determined due to imprecise measurements or missing observations. We demonstrate that genetic interactions can often be inferred from fitness rank orders, where all genotypes are ordered according to fitness, and even from partial fitness orders. We provide a complete characterization of rank orders that imply higher order epistasis. Our theory applies to all common types of gene interactions and facilitates comprehensive investigations of diverse genetic interactions. We analyzed various genetic systems comprising HIV-1, the malaria-causing parasite Plasmodium vivax , the fungus Aspergillus niger , and the TEM-family of -lactamase associated with antibiotic resistance. For all systems, our approach revealed higher order interactions among mutations. β

## Introduction

The fitness of an individual with a particular genotype is a measure of its expected contribution to the next generation of the population. The collection of all fitness values for all genotypes, referred to as the fitness landscape, is a central concept in evolutionary biology (Wright, 1932; Orr, 2009). The fitness landscape can have a strong impact on the fate of the evolving population, such as, for example, the risk of a pathogen population to develop drug resistance and to survive under drug treatment (de Visser and Krug, 2014).

Genetic interactions, or epistasis, are abundant in nature. They can have many causes and occur at various scales, for instance, among mutations of a protein-coding sequence or between sequences coding for different genes. Unless there are genetic interactions, we assume that fitness is additive, that is, the fitness effects of individual mutations sum. An additive fitness landscape is determined by the wild-type and single-mutant fitness values.

If the fitness landscape is determined by the wild-type, single-mutant, and double-mutant fitness values, then we say that it has no higher order epistasis. Intuitively, higher order epistasis means that the fitness of a multiple mutant is unexpected given the fitness of the wild type and all single and double mutants. For example, Weinreich et al. (2006) showed that five mutations jointly increase antibiotic resistance considerably more than expected.

Measuring fitness experimentally is challenging. Fitness measurements tend to come with high uncertainty and they are often obtained only for a subset of genotypes. Moreover, fitness can sometimes not be measured directly at all. Instead, phenotypes are considered that can be measured and are believed to approximate fitness well. For instance, antimicrobial drug resistance is the dominating survival factor for a bacterial population under drug exposure, so that the degree of resistance is a good substitute measure of fitness. Several such fitness proxies are used in microbiology, including survival as measured by disc diffusion tests. Although it is possible to study epistasis of the proxy data, in general, presence or absence of epistasis in the proxy landscape does not imply presence or absence of epistasis in the fitness landscape itself.

Experimentally, epistatic interactions have been measured in several genetic systems, including E. coli (Khan et al., 2011; Weinreich et al., 2006; Poelwijk et al., 2007), HIV-1 (da Silva et al., 2010; Segal et al., 2004), and other viruses (Wylie and Shakhnovich, 2011; Sanjuán, 2010). These and similar studies involve the analysis of standing genetic variation or spontaneous mutations (Bonhoeffer et al., 2004; Bershtein et al., 2006), engineered site-directed mutations (Sanjuán et al., 2004; Weinreich et al., 2006), and combinations of both (Sanjuán et al., 2005; Poon and Chao, 2006). Competition experiments are also frequently employed to learn mutational fitness effects. For example, Sanjuán et al. (2004) studied the distribution of deleterious mutational effects in RNA viruses using this approach. Such experiments are typically run on single-nucleotide substitution mutants produced by site-directed mutagenesis. The data produced in competition experiments is informative about pairwise comparisons of genotypes with respect to their fitness. However, little is known about whether or not it is possible to learn higher order genetic interactions from such fitness comparison data.

Due to the rapid growth of the number of possible interactions with the number of loci, all interactions can exhaustively be studied only for a small number of loci. At the human genome scale, for example, a complete study of only pairwise gene interactions would already require hundreds of millions of experiments. On the other hand, for smaller organisms, such as yeast, all pairwise and several three-way gene interactions have been measured experimentally (Costanzo et al., 2010). Only when restricting to a small set of preselected loci, can one assess all combinations of mutations and hence all epistatic interactions. This approach has been pursued, for example, by Weinreich et al. (2006) for a five-locus system associated with bacterial drug resistance.

Historically, the study of genetic interactions was mostly restricted to pairwise epistasis. According to Crow and Kimura, 1970 (p. 224) higher order interactions were generally believed not to be significant in nature, with references to Fisher, Haldane, and Wright. More recent arguments for the same view have been stated in the context of protein folding (Gupta and Adami, 2016). On the other hand, empirical findings suggest that the opposite is true for many other systems (Szendro et al., 2013; Neidhart et al., 2013; Sailer and Harms, 2017a). For example, Weinreich et al. (2013) argue that three-way and four-way interactions can be as strong as pairwise epistasis referring to various empirical fitness studies, and Knies et al. (2017) find many epistatic interactions in a numerically near-additive fitness landscape, reducing dramatically the number of accessible evolutionary trajectories. Although the significance of higher order interactions may vary between systems, the topic has not been thoroughly investigated. This is partly due to lack of adequate methodology to quantitatively assess the interactions underlying an observed empirical fitness landscape. Improved mathematical and statistical tools for detecting higher order interactions, as well as more empirical results, are necessary for more conclusive answers regarding the importance of higher order interactions.

In this paper, we consider fitness data that comes in the form of pairwise comparisons. Such data are frequent in practice and can arise in different ways. First, some assays rely on comparing the fitness of two genotypes, for example, by letting them grow in direct competition. Each competition experiment is informative about which of the two genotypes has higher fitness, without estimating the fitness values themselves. Second, direct but uncertain fitness measurements are also often summarized as pairwise fitness relations by recording only whether two genotypes displayed significantly different fitness values or not. Third, rather than fitness itself, a fitness proxy, that is, a phenotype closely related to fitness, may be considered. Fitness proxies cannot be used directly to measure epistasis, because they generally do not preserve fitness linearity (Gong et al., 2013), but if proxy data preserves pairwise comparisons, they may be used instead. Lists of mutants found in a new environment, such as, for example, a new host for a pathogen or a drug environment can be utilized similarly. Assuming that the capability to transition to and survive in the new environment is an indication of higher fitness, this type of observational data also provides pairwise fitness comparisons. Similarly, the population frequency of genotypes can sometimes be used to draw conclusions about fitness. For example, by employing a specific model of viral evolution, fitness was inferred computationally from deep sequencing data of an HIV-1 population, and pairwise credible fitness differences were reported (Seifert et al., 2015).

Irrespective of how they were obtained, any consistent set of pairwise fitness relations can be regarded as a partial order of the genotypes with respect to fitness. Two specific types of partial orders play important roles for fitness landscapes. First, if comparisons are available for all pairs of genotypes, then the partial order is a total order, or rank order. In this case, all genotypes are ordered according to fitness. Second, several studies compare fitness only between mutational neighbors, that is, genotypes which differ at exactly one locus. The resulting partial orders are referred to as fitness graphs and have recently been used extensively (Ogbunugafor et al., 2016; Wu et al., 2016; Smith and Cobey, 2016; Mira et al., 2015).

The question addressed in the present study is whether higher order interactions can be inferred from rank orders, fitness graphs, and general partial orders. Connections between rank orders and fitness graphs to epistasis and global properties of fitness landscapes have been observed repeatedly (Greene and Crona, 2014; Crona et al., 2013; Poelwijk et al., 2011; Weinreich et al., 2006; Weinreich et al., 2005). Most recently, Wu et al. (2016) discussed an example of a fitness graph that implies higher order epistasis. The significance of rank orders of genotypes for epistasis was recognized by Weinreich et al. (2005). The authors introduced the concept of sign epistasis. By definition, a system has sign epistasis if the sign of the effect of a mutation, whether positive or negative, depends on genetic background. Importantly, sign epistasis implies that the rank order of the genotypes is not compatible with additive fitness. In this paper, we develop a related approach based on rank orders that applies to higher order epistasis as well as other measures of gene interactions. For instance, if the rank order of the genotypes implies three-way epistasis for a three-locus system, then one has a signed variant of three-way epistasis. Similarly, one can consider signed variants of almost any type of gene interaction. The theory of sign epistasis stands as a model for development in the area, and there is a potential for understanding global properties of fitness landscapes in terms of (local) signed interactions, similar to results for sign epistasis.

In addition to the theoretical work mentioned above, rank order arguments have been used for developing antimicrobial treatment strategies (Smith and Cobey, 2016; Nichol et al., 2015; Mira et al., 2015; Goulart et al., 2013). However, the full potential of rank order consideration for the comprehensive analysis of epistatic gene interactions in general n-locus genetic systems has not been exploited. Furthermore, to the best of our knowledge the general case of arbitrary partial fitness orders has yet to be considered.

Here, we develop quantitative tools to detect any type of gene interactions measured by linear forms, including epistasis as described by Fourier coefficients, Walsh coefficients, and circuits (Beerenwinkel et al., 2007; Weinreich et al., 2013). In particular, our approach applies to total n-way epistasis, conditional epistasis, and marginal epistasis. We used our approach to analyze genetic interactions in HIV-1, the parasite Plasmodium vivax, the fungus Asbergillus niger, and β-lactamase antibiotic resistance systems. In all cases, we detect higher order interactions based only on partial information about the fitness order of genotypes, without knowing or estimating the actual fitness values.

## Results

We consider genetic systems consisting of n biallelic loci. A genotype can then be represented as a binary string of zeros and ones of length n, where 0 denotes the wild-type allele and 1 the alternative allele. We assume that fitness is additive in the absence of epistasis. The fitness of a genotype g is denoted by wg, and we assume that the fitness landscape w is generic in the sense that no two genotypes have exactly the same fitness.

A complete analysis of all epistatic interactions would require fitness measurements of all 2n genotypes. However, this level of completeness is rarely available in empirical data sets due to experimental design or an infeasible number of genotypes. To address this limitation, we developed methods that are applicable to partial orders of genotypes according to fitness. For example, the two fitness relations w01>w00 and w10>w11 together define a partial order. One can always extend a partial order to a rank order, that is, a total order of the genotypes in the system from highest to lowest fitness. For example, the total order w10>w11>w01>w00 extends the partial order above. Our goal is to understand what fitness rank orders and more generally partial fitness orders of genotypes reveal about gene interactions.

## Two-locus case

We first consider epistasis for a biallelic two-locus population consisting of the unmutated genotype, or wild type, 00, the two single mutants 01 and 10, and the double mutant 11. In this case, epistasis is denoted by ε2, where the index two refers to the number of loci. It is defined as the deviation from additivity,(1)ε2=(w00+w11)-(w01+w10).

The system has no epistasis if ε2=0, positive epistasis if ε2>0 and negative epistasis if ε2<0.

We first assume that the available information on fitness is a rank order of the genotypes (Figure 1). The rank order is sometimes sufficient for determining that the system has epistasis. For instance, the rank order w11>w00>w10>w01 (Figure 1 rank order 3), implies w00+w11>w01+w10, so ε2>0. It follows that the rank order alone allows one to detect positive epistasis without knowledge of the actual fitness values. There are 24 rank orders of the biallelic two-locus system. Among these, eight imply positive epistasis, eight imply negative epistasis, and eight do not permit any inference regarding epistasis. In total two thirds of the rank orders imply epistasis. Each rank order that implies epistasis also determines the sign of ε2 (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig1-v1.jpg)

**Figure 1.:** rank orders of the biallelic two-locus system, where the 24 colored rank orders imply epistasis.16Red (top row) indicates positive epistasis and blue (middle row) negative epistasis.

Sometimes even a partial order of the genotypes is sufficient for determining that the system has epistasis. For instance, if we know that w01>w00 and w10>w11, then we can infer that the system has negative epistasis (Figure 2a). To see this, we consider all rank orders that extend the partial order. There are six such total extensions, namely rank orders 9, 10, 12, 13, 14, and 16 in Figure 1, and all imply negative epistasis. We conclude that the partial order implies epistasis, based on only two fitness comparisons and without knowing any of the actual fitness values. This observation holds in general: If all total extensions imply epistasis then the same is true for the partial order. We will use this argument repeatedly.

![Figure 2.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig2-v1.jpg)

**Figure 2.:** a) A partial fitness order of genotypes.The rank orders that extend this partial order are orders (9 , 10 , 12 , 13 , 14), and (16) in Figure 1. All of them imply negative epistasis (). (ε2<0b) A partial order of genotypes with all its total extensions shown on the right. The first extension shown in red implies positive epistasis (), while the second one in black does not.ε2>0

A partial order can also be compatible with several rank orders, some of which might imply epistasis while others do not. In this case, the information is not sufficient to detect epistasis from the partial order alone. For example, the partial order w00>w01>w10,w11 is compatible with the two rank orders w00>w01>w11>w10 and w00>w01>w10>w11 (Figure 2b). The first rank order implies positive epistasis, but the other one does not. Consequently, the partial order does not reveal whether or not the system has epistasis, and further comparisons are needed for a conclusion. A more detailed treatment of partial fitness orders can be found in Lienkaemper et al. (2017).

Fitness graphs constitute an important subclass of partial orders, as they often are the reported result of experiments, and because of their relevance for evolutionary processes (Figure 3). Briefly, the nodes of a fitness graph represent genotypes and for each pair of mutational neighbors, that is, genotypes which differ at exactly one locus, an arrow points toward the genotype of higher fitness (Section Partial orders and fitness graphs).

![Figure 3.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig3-v1.jpg)

**Figure 3.:** has the lowest fitness, there are four fitness graphs.00The graph (a) is compatible with additive fitness, whereas the remaining graphs imply negative epistasis.

A fitness graph implies epistasis exactly when all rank orders compatible with the graph do, as is the case for partial orders in general. For example, Figure 3 shows the four fitness graphs where genotype 00 has lowest fitness in the in the system. The graphs (b), (c) and (d) imply epistasis, whereas (a) is compatible with additive fitness.

A couple of observations from Figure 3 are useful for determining if a system is compatible with additive fitness. First, any rank order compatible with the graph (a) has the following property: For each genotype, replacing 0 by 1 results in a genotype of higher fitness. If the genotype 00 has minimal fitness in the system, then rank orders are compatible with graph (a) exactly if they satisfy this property. The second observation is that a fitness graph where 00 has minimal fitness is compatible with additive fitness exactly if all arrows point up. Both observations generalize to any number of loci, and can be phrased in full generality (one can reduce the general problem to the case when 0⁢…⁢0 has lowest fitness in the system by a relabeling argument). In particular, only 384 out of (23)! = 40,320 rank orders are compatible with fitness graphs with all arrows up (after relabeling) for the three-locus system, which we consider next (Materials and methods, Section Partial orders and fitness graphs).

## Three-locus case

The biallelic three-locus system consists of the eight genotypes 000, 001, 010, 011, 100, 101, 110, and 111. The system has total three-way epistasis if(2)ε3=(w000+w011+w101+w110)-(w001+w010+w100+w111)≠0.

For the three-locus system, we distinguish between fitness landscapes with no epistasis (fitness is additive), with pairwise but not higher order epistasis (fitness is not additive but ε3=0), and with three-way epistasis (ε3≠0).

Some rank orders imply three-way epistasis, similar to our observation of epistasis in the two-locus case. The condition for when a rank order implies three-way epistasis is remarkably simple, and we demonstrate it with an example. Consider the rank order (3)w110>w111>w101>w011>w100>w010>w000>w001.

We can represent this rank order by a word in the letters e and o using the following procedure. The genotype 110 with the highest fitness is represented by e because it has an even number of 1’s, the genotype 111 with the second highest fitness is represented by o because it has an odd number of 1’s, and so forth. Working from highest to lowest fitness, we obtain the word (4)e⁢o⁢e⁢e⁢o⁢o⁢e⁢o.

If one reads the word letter by letter from left to right, then one has never encountered more o’s than e’s. This property means that e⁢o⁢e⁢e⁢o⁢o⁢e⁢o is a Dyck word (Stanley, 1999).

For a biallelic three-locus system, a rank order implies three-way epistasis exactly if its associated word (where the role of e and o can be interchanged) is a Dyck word (Proposition 1). This simple rule allows us to conclude that an empirical system has three-way epistasis. As in the two-locus case, a landscape may have three-way epistasis even if the rank order does not imply it. For biallelic three-locus systems, there are in total 40,320 rank orders, of which 16,128 (40%) imply three-way epistasis (Proposition 1).

Fitness graphs can be analyzed by using our results on rank orders as in the two-locus case. Figure 4 shows three fitness graphs for three-locus systems. The fitness graph (a) implies three-way epistasis, the graph (b) pairwise but not higher order epistasis, and the graph (c) is compatible with additive fitness.

![Figure 4.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig4-v1.jpg)

**Figure 4.:** a) implies three way epistasis, the graph (b) implies epistasis, but not higher order epistasis, and (c) does not imply epistasis, since all arrows point up.

There are in total 1,862 fitness graphs for the biallelic three-locus system, of which 698 graphs (37%) imply three-way epistasis. In principle one can check a particular three-locus system for higher order epistasis using this result. However, it is not convenient to work with a list of over one thousand graphs. In order to make the problem more tractable, we can utilize the fact that some fitness graphs are isomorphic (Figure 5). There are 54 distinct isomorphism classes of graphs for the three-locus system, of which 20 imply higher order epistasis (Mathematical framework and proofs, Section Partial orders and fitness graphs). Consequently, to detect three-way epistasis, one can find the isomorphism class and then check 54 graphs, namely one for each isomorphism class (Figure 6 ).

![Figure 5.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig5-v1.jpg)

**Figure 5.:** The horizontal axis is labeled by the four interaction coordinates , u110, … and twenty circuits u111, a, …. The boxplots show the distributions of the various interactions induced by the empirical fitness distribution. The red star indicates whether the interaction has been detected by our rank order method. Specifically, a star with vertical coordinate t, 0, and one means negative, no, and positive interaction, respectively.-1

![Figure 6.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig6-v1.jpg)

**Figure 6.:** -lactamase contributes to antibiotic resistance problems in hospitals.βThe fitness graph shows a four-locus system consisting of the wild type, TEM-1, the quadruple mutant, TEM-50, and all intermediate mutants, including six clinically found mutants in the TEM family. The mutation M69L corresponds to , E104K to 1000, G238S to 0100, and N276D to 0010. Growth rates were measured for the 16 genotypes under exposure to the antibiotic FEP Cefepime, and the fitness graph was determined accordingly (0001Mira et al., 2015). The graph reveals higher order epistasis.

![Figure 7.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig7-v1.jpg)

**Figure 7.:** Aspergillus Niger.The system consists of all combinations of the four individually deleteriouis mutations fwnA1, leuA1, oliC2 and crnB12. The landscape has in total four peaks, labeled  and 0000,1100,0011.1001

![Figure 8.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig8-v1.jpg)

![Figure 9.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig9-v1.jpg)

**Figure 9.:** Here, the allele labels ‘0’ and ‘1’ in the first locus have been interchanged, as well as the second and third loci.

We complete the consideration of the three-locus case by analyzing partial orders. Again, in favorable cases one can infer three-way epistasis. Indeed, if there exists a partition of all eight genotypes into four pairs (ge,go), where e and o are as above, and wge>wgo for each pair, then one can conclude three-way epistasis ( Proposition 7).

## General n-locus case

The results on rank orders and higher order epistasis for n=3 generalize to any number of loci. The definition of n-way epistasis in an n-locus system is analogous to the three-locus case, as is the condition for when rank orders imply n-way epistasis. Accordingly, a characterization of rank orders that imply n-way epistasis can be phrased in terms of Dyck words (Proposition 1). From this result it follows that the fraction of rank orders that imply n-way epistasis is 2/(2n-1+1) ( Corollary 2) and that it can be determined in a computationally efficient manner whether or not a rank order implies n-way epistasis.

Rank order methods are useful for analyzing the total n-way epistasis for an n-locus system, as demonstrated. However, a single quantity cannot capture all possible gene interactions. Rank order approaches have the capacity to reveal finer interactions as well.

We start with a general description of gene interactions before exploring what rank orders can reveal about these interactions. We define an additive dependence relation as a linear form that is zero on additive fitness landscapes. Interaction coordinates and circuits (Beerenwinkel et al., 2007), as well as Walsh coefficients of order two or more (Weinreich et al., 2013), are additive dependence relations. For simplicity, we restrict our analysis to the three-locus system, although the arguments used are readily extendable to any number of loci n.

First, we consider additive dependence relations that directly correspond to the two-locus case by fixing one allele at the third locus. For example, if we fix the third locus at 0, then a=w000+w110-w010-w100

measures pairwise epistasis between the first and second locus. Similarly, if we set the third locus to 1, thenb=w001+w111-w011-w101

measures pairwise epistasis between the first and second locus.

An example of an additive dependence relation with no correspondence in the two-locus setting ism=w001+w010+w100-w111-2⁢w000,

which compares the fitness of the triple mutant 111 to the three single mutants. This expression is negative if the triple mutant has higher fitness than one would expect based on the fitness effects of the three single mutations. An example of an additive dependence relation with eight non-zero terms isu110=w000-w100-w010+w001+w110-w101-w011+w111.

One can verify that u110 is twice the average of a and b. For a systematic approach to a comprehensive set of gene interactions, one can take advantage of circuits, that is, minimal additive dependence relations. In contrast, u110 is not minimal, because it can be derived from a and b. There are 20 circuits for the three-locus system, including a, b, and m (Mathematical framework and proofs, Section Circuits).

The interactions described by a and b are referred to as conditional epistasis, that is, interactions that measure the total epistasis of subsystems obtained by fixing some loci at 0 or 1. If the interactions a and b differ substantially, it may be important to consider both of them. However, if we are rather interested in the average interaction for the first two loci over all genetic backgrounds, then u110 is the right measure.

In general, relations that measure average effects, such as u110, are referred to as interaction coordinates. The interaction coordinates u110 differs from the Walsh coefficient E110 (Weinreich et al., 2013) only by a constant scaling factor. Provided that average effects are sufficient for the purpose of a study, one can analyze higher order epistasis by considering interaction coordinates, or Walsh coefficients, (Weinreich et al., 2013) (Mathematical framework and proofs).

One interesting class of circuits compares the effect of replacing pairs of loci with different backgrounds. For instance, k=w000-w001-w110+w111

compares the effect of replacing 00 by 11 if the third coordinate is fixed at 0, versus if the third coordinate is fixed at 1. We refer to k as a circuit measuring marginal epistasis between two pairs of loci as in Beerenwinkel et al. (2007).

Arguments based on Dyck words can be used for analyzing rank orders and additive dependence relations in general. The letters are determined by the signs of the coefficients in the linear form, as for three-way epistasis (Theorem 3).

For each circuit and interaction coordinate, we identify all rank orders that determine its sign. The characterization is given in terms of general Dyck word conditions. We found that for each interaction coordinate, 2/5 of all rank orders determine its sign; for each circuit corresponding to either conditional two-way interaction or marginal epistasis between two pairs of loci, 2/3 of all rank orders determine its sign; and for each circuit relating the three-way interaction to the total two-way epistasis, 1/2 of all rank orders determine its sign ( Corollary 4 and 6).

Importantly, if a rank order implies that the sign of an additive dependence relation, such as a circuit or an interaction coordinates, is determined, then the system has sign epistasis.

One can ask if it possible to decompose the word obtained for analyzing n-way epistasis into subunits, so as to learn about circuits or properties for subsystems of the genotypes. In general, no such decompositions are possible unless one has information in addition to the word itself. For instance, suppose that a rank order is mapped to o⁢o⁢e⁢e⁢e⁢o⁢o⁢e. The first half of the word, namely o⁢o⁢e⁢e, does not necessarily reveal any interesting information about the system. (Mathematical framework and proofs, Section Circuits).

The signs of all twenty circuits determines the polyhedral shape of the fitness landscape (Beerenwinkel et al., 2007). The shape combines the circuit information into a more manageable object. However, no rank order determines a shape for n=3 (Mathematical framework and proofs, Section Circuits).

Our tools for detecting gene interactions work for total n-way epistasis, interaction coordinates and circuits. Moreover, our approach applies to any type of gene interaction that can be expressed by a linear form (Theorem 3), such as Fourier coefficients (Beerenwinkel et al., 2007) and Walsh coefficients (Weinreich et al., 2013). We have implemented algorithms for detecting the gene interactions described in this section, both for rank orders and partial orders, specifically, algorithms for n-way epistasis, three-way and four-way interaction coordinates, and three-way circuit interactions (https://github.com/gavruskin/fitlands#fitlands). The most computationally demanding task of our algorithms is reading the rank order from disk. The run time complexity is proportional to the number of non-zero coefficients in the linear form.

## Analysis of empirical fitness data

As proof of principle, we applied our tools to fitness data from a diverse set of biological systems, ranging from HIV-1 (Segal et al., 2004), malaria (Ogbunugafor and Hartl, 2016), antibiotic resistance (Mira et al., 2015), to the fungus Aspergillus Niger (Franke et al., 2011). Our approach reveals higher order epistasis for all of these systems, only by considering rank orders and partial orders of genotypes, without the need to access direct fitness measurements or estimates.

Our first application is to the HIV-1 data published by Segal et al., 2004. Following Beerenwinkel et al. (2007), we consider the three-locus biallelic system that consists of the mutation L90M in the protease and mutations M184V and T215Y in the reverse transcriptase of HIV-1. Fitness was measured as the number of offspring in a single replication cycle of the virus in the original study, and was reported relative to the wild-type strain NL4-3 on a logarithmic scale. The data consist of 288 fitness measurements, including between 5 and 214 replicates per genotype.

The following rank order was obtained by comparing the mean fitness of the eight genotypes:w000>w100>w011>w110>w101>w001>w010>w111,

where 000 corresponds to the sequence of amino acids LMT and 111 to MVY comprising the three selected loci. This rank order implies positive three-way epistasis because the associated worde⁢o⁢e⁢e⁢e⁢o⁢o⁢o

is a Dyck word. It follows that the three mutations under consideration together have a stronger effect on fitness than one would predict from single and double mutants. A closer inspection of the word reveals more information. If we swap any two adjacent letters in the word, then we still have a Dyck word, with the single exception of the first two letters. In other words, only one pair of adjacent genotypes in the rank order, namely 000 and 100, could violate the conclusion if transposed.

If the experiment was to continue, our analysis could be used to direct the data collection process. Indeed, the argument above suggests that the position of the genotype 100 may violate the conclusion of positive three-way epistasis. To quantify the uncertainty in the ranking of 100 with respect to the wild type 000, we employed the Wilcoxon rank sum test on the replicate fitness measurements. The p-value of the test is 0.47 for the relation w000>w100, which implies considerable uncertainty and justifies our recommendation of further experiments to clarify the position of 100. Importantly, the suggested experiment reduces the number of measurements required to make a more robust conclusion about epistasis considerably, namely to one out of 28 possible comparisons.

We proceeded by considering other types of gene interactions in this data set. When considering all 20 circuits, the rank order implies interactions for 55% of the circuits, with positive sign for 30% and negative for 25% of the circuits. This result is consistent with the conventional statistical approaches that use direct fitness measurements. Indeed, since the empirical study of Segal et al., 2004 provided multiple fitness measurements of each genotype, it was possible to compare our conclusion based on rank orders with statistical tests based on fitness estimates.

The results for fitness measurements were confirmed by the conventional Wilcoxon rank sum test. We computed interaction coordinates and circuit interactions for the summary statistics reported in (Beerenwinkel et al., 2007). Figure 7 shows that our rank order methods detected the majority of circuit interactions identified by using the summary statistics. Specifically, both approaches detected three-way epistasis. Furthermore, 11 of the 20 circuit interactions have been detected by our method and confirmed by Wilcoxon rank sum test.

We also applied Student’s t-test to detect interactions and quantify the significance of the estimates. In addition to the 11 interactions, the t-test found 6 circuit interactions as significant (Table 2). We emphasize that the rank order approach required much less information to arrive at the same conclusions, thus demonstrating the power of the method.

We conclude that the three sites in the HIV-1 genome under consideration are prone to a diverse set of interactions. Specifically, the strong support for the three-way epistasis, along with the 55% of informative circuit interactions, imply that the three loci together interact in a complex manner, meaning that the interactions cannot be explained using pairwise interactions alone. Thus, in this data set, higher order interactions have a strong impact on the fitness landscape.

Our second application is to a study of antimicrobial drug resistance in malaria (Ogbunugafor and Hartl, 2016). The authors measured growth rates for several mutants of Plasmodium vivax under exposure to the antimalarial drug pyrimethamine. We identified higher order epistasis by analyzing rank orders. More precisely, we considered a three-locus sub-system of the study that consists of mutations N50I, S58R, and S117N, in the context of T173L, a fixed mutation, under nine different concentrations of pyrimethamine. The genotypes comprising positions 50, 58, and 117 are labeled 000 (NSS), 100, 010, 001, 110, 101, 011, and 111 (IRN). The three highest concentrations of the drug resulted in the following rank orders: w111>w011>w001>w101>w010>w100>w110>w000w111>w011>w001>w010>w100>w101>w110>w000w111>w011>w010>w001>w100>w110>w101>w000.

The corresponding words are o⁢e⁢o⁢e⁢o⁢o⁢e⁢e for the first rank order, obtained under the highest concentration of the drug, and o⁢e⁢o⁢o⁢o⁢e⁢e⁢e for the second and third rank orders. Since we obtain Dyck words in all cases, the system has negative three-way epistasis for the three highest concentrations of the drug. This consistency among pyrimethamine concentrations shows that the result is robust.

Using our software, we also analyzed all interaction coordinates for this data set (https://github.com/gavruskin/fitlands/blob/master/Four-way_interaction_coordinates_and_total_n-way_interaction.ipynb). Our analysis revealed that for the two highest concentrations of the drug, the rank order implies that the interaction coordinate denoted u0111(Mathematical framework and proofs) is negative.

Next, we applied our tools to a study of the TEM-family of β-lactamase, associated with antibiotic resistance (Mira et al., 2015). The study measured growth rates for 16 genotypes exposed to 15 different antibiotics. Specifically, all 16 genotypes that combine subsets of the four amino acid substitutions M69L, E104K, G238S, N276D found in TEM-50, including eight known enzymes, were created using site-directed mutagenesis. We considered the fitness graph obtained when the system was exposed to the antibiotic FEP Cefepime at a concentration of 0.0156 μg/ml (Figure 8). The fitness graph implies higher order epistasis (Proposition 7), that is, the fitness of TEM-50 cannot be predicted even with complete knowledge of the fitness values of the remaining genotypes in the system. The fitness graphs for the other 14 antibiotics do not share this property. We conclude that even though some of the single and triple mutants confer low antibiotic resistance, a large population of triple mutants alone is more prone to become antibiotic resistant due to the epistatic fitness advantage of TEM-50, as compared to a setting with no higher order epistasis.

Finally, we investigated a study of the filamentous fungus Aspergillus Niger (Franke et al., 2011). We considered a system consisting of the wild type and all combinations of the four individually deleterious mutations fwnA1, leuA1, oliC2 and crnB12 (Figure 9). Fitness was estimated with two-fold replication by measuring the linear mycelium growth rate in the original study. The fitness graph implies higher order epistasis (Proposition 7).

All four arrows incident to 0000 point towards the genotype, so that the genotype 0000 is a peak in the landscape. The same is true for the genotypes 1100, 0011, and 1001. Because of the four peaks, it is possible that the fungus population gets stranded at a suboptimal peak during the course of evolution (we do not necessarily assume that the starting point for an evolutionary process is at 0000). In contrast, an additive fitness landscape is single peaked. This example illustrates that epistasis may have an impact on the evolutionary dynamics. Several peaks can make the evolutionary process less predictable, depending also on other factors such as population size, mutation rate, etc. More generally, for three-locus fitness graphs, we analyzed the impact of higher order epistasis versus only pairwise epistasis systematically. We found that higher order epistasis correlates with more peaks as well as other features that can lead to involved evolutionary dynamics (Mathematical framework and proofs, Section Graph theoretical aspects).

We completed our analysis of this data set by considering the 5-locus system of mutations fwnA1, argH12, pyrA5, leuA1, and pheA1, conditioning on mutations lysD25, oliC2, and crnB12 all being absent. The original study does not contain any measurements for the two genotypes 11010 and 10111. Furthermore, two pairs of genotypes in the system have identical ranks, namely (11000, 10010) and (10011, 11101). We obtained the following word for the total five-way epistasis u11111, e⁢e⁢o⁢e⁢e⁢x⁢x⁢o⁢o⁢o⁢o⁢e⁢o⁢o⁢o⁢e⁢o⁢y⁢y⁢e⁢e⁢e⁢o⁢e⁢o⁢e⁢o⁢e⁢o⁢o

where the two x’s correspond to genotypes 11000 and 10010, the y’s to 10011 and 11101, and two letters are missing. Whether one can draw conclusions about five-way epistasis or not, depends on the positions of the two missing genotypes, as well as the genotypes represented by y’s, whereas it is independent of the genotypes represented by x’s. Specifically, if genotype 11101 has higher fitness than 10011, genotype 10111 has rank between 1 and 15, and genotype 11010 has rank between 20 and 32, then the resulting rank order implies positive five-way epistasis, that is, u11111>0, for both possible options to resolve the ranking of genotypes 11000 and 10010 (Table 3).

## Discussion

Gene interactions play a critical role in evolutionary processes. Important features of fitness landscapes, such as the number of peaks, and accessible evolutionary trajectories, depend on epistatic gene interactions. The importance of higher order versus pairwise epistasis, within and among genes or in non-coding regions, as well as the impact of higher order epistasis on evolutionary dynamics, remains a central research topic (Sailer and Harms, 2017b; Wu et al., 2016; Weinreich et al., 2013). Progress in all of these areas requires adequate mathematical and statistical approaches, in addition to empirical studies.

Here, we have developed new quantitative tools for detecting gene interactions from empirical data. The main advantage of our tools is that they can reveal gene interactions from the types of data frequently generated in empirical studies, specifically rank orders, fitness graphs, and general partial orders of genotypes. The reasons why, in practice, these types of data are available more often than precise fitness measurements for each genotype are manifold. They include restricted comparative experimental designs and known and unknown confounding factors in measuring fitness that can result in uncertain and biased estimates. The methods presented here allow for studying epistatic interactions even when direct fitness measurements are lacking or only a subset of pairwise fitness comparisons is available, either as the immediate outcome of the experiment or the reported summary.

We provide a complete characterization of rank orders that imply higher order epistasis, along with precise results for fitness graphs of three-locus systems. In principle, our approach applies to general partial orders as well, and we have implemented algorithms accordingly. However, because of the increasing computational complexity it would be desirable to have theoretical results for handling large systems. In particular, a characterization of fitness graphs that imply higher order epistasis is of independent mathematical interest.

We found that for biallelic three-locus systems, 40% of all possible rank orders and 37% of all possible fitness graphs imply higher order epistasis. These fractions suggest that our methods have a good capacity to detect higher order epistasis among three loci, even if exact and complete fitness measurements or estimates are not available.

The fraction of rank orders that imply n-way epistasis decreases rapidly with increasing number of loci, n. However, many rank orders are informative regarding other additive dependence relations, for instance some circuits measuring conditional epistasis. This is clear from the observation that the proportion of rank orders that are compatible with additive fitness decreases rapidly with n.

Moreover, the power of our methods was demonstrated for a diverse set of biological systems. We detected higher order epistasis for HIV, malaria, the fungus Aspergillus Niger, and antibiotic resistance systems. Our findings suggest that genetic interactions beyond two-way epistasis shape the fitness landscapes of these genetic systems and may play an important role in determining their evolutionary trajectories. We also exhaustively investigated various types of higher order interactions in HIV-1 and discovered a complex pattern of interactions, confirming that our approach is powerful enough to detect finer gene interactions. Specifically, we identified over twenty interactions by conventional approaches, and rank order methods detected about half of them.

Another important application of our method is to experimental design. When the information available in the data does not contradict an interaction, but is not conclusive enough to claim the interaction, for example because the number of performed competition experiments is too small, then the method allows for prioritizing further experiments by suggesting additional comparisons of genotypes. This feature may prove useful in guiding fitness experiments that aim for testing specific interactions and allow for iteration. We have developed this idea further in Lienkaemper et al. (2017), where we consider partial fitness orders of genotypes and develop efficient algorithms to detect genetic interactions, as well as study the geometry of such partial orders. Evolutionary aspects of partial orders and gene interactions are studied in Crona and Luo, 2017.

Genetic interactions, especially those of higher order, are particularly difficult to detect in high-dimensional systems, where complete fitness measurements of all genotypes are infeasible. Human genome-wide association studies (GWAS) are a prime example. Here, already the number of loci, n, and certainly the number of possible genotypes, 2n, is much larger than the actual number of genotyped and phenotyped individuals, even if the genotype data is summarized on the level of genes or haplotype blocks. Since most diseases are polygenic, rather than monogenic, genetic interactions play an important role, and accounting for them may explain some of the missing heritability and improve genetic disease models. Several methods have been proposed for detecting pairwise interactions in GWAS, most of them relying on scanning all or a prioritized subset of pairs of loci (Wei et al., 2014), but little is known about higher order interactions in these landscapes.

The methods presented in the present study may help addressing this challenge as they can sometimes reveal higher order interactions from a small number of comparisons, and the choice of genotypes to compare can be optimized if particular interactions are to be tested. Another advantage is the flexibility of our approach regarding the type of epistatic interaction analyzed. While we have focused on analyzing complete genetic systems, that is, n-dimensional hypercubes, for small values of n in this work, genotype spaces consisting of subsets of the 2n possible genotypes have different sets of interactions, such as circuits, that are natural to consider. Towards this end, Huggins et al. (2007) have explored circuits and their sign patterns for genotype data from the HapMap project in two ENCODE regions. The Dyck word approach will be particularly useful if quantitative data on the phenotype is difficult to obtain, but rank order information is more accessible, for example by considering disease indicators, rather than the condition itself.

For a more theoretical perspective, we emphasize the distinction between rank order-induced gene interactions, and interactions that do not change the rank order of genotypes. This distinction was pointed out by Weinreich et al., 2005 who introduced the term sign epistasis. If a system has sign epistasis, then the rank order of the genotypes is not compatible with additive fitness. Rank order-induced gene interactions of any type can thus be regarded as analogues to sign epistasis.

There exist a number of possible ways to quantify and interpret higher order interactions (Weinreich et al., 2013; Beerenwinkel et al., 2007; Hallgrímsdóttir and Yuster, 2008), and our rank order approach applies to any type of gene interactions measured by linear forms. In particular, we can detect interactions as described by Fourier coefficients and Walsh coefficients. From our general argument based on Dyck words we investigated three-locus systems, and determined the number of rank orders that imply circuit interactions, including conditional and marginal epistasis, and similarly for interactions coordinates. The method works equally well for other interactions.

Further investigation of rank order-induced interaction has the potential to relate global and local properties of fitness landscapes, similarly to results on sign epistasis (Weinreich et al., 2005; Poelwijk et al., 2011; Crona et al., 2013). Global properties concern peaks and mutational trajectories in the fitness landscape, whereas local properties concern, for instance, fitness graphs for small system. The relation between global and local properties is important since only local properties can be easily observed in experiments or nature.

A very useful feature of sign epistasis is that one can identify, or rule out, sign epistasis in a system from inspection of two-locus subsystems only. The theoretical significance and applicability of sign epistasis depends on its local nature. Fortunately, the signed versions of other gene interactions are sometimes local as well. For instance, it seems plausible that the absence of rank order induced conditional epistasis of specified orders (a local property) correlates with few peaks and good peak accessibility. In this spirit we explore some evolutionary consequences of higher order epistasis in Crona and Luo, 2017. Theory for sign epistasis stands as a model for further development in this area.

Although we have applied our method here only to fitness, any other continuous phenotype of interest can be analyzed in exactly the same manner. The fitness landscape w is then replaced by a more general genotype-to-phenotype map. For example, rather than using it as a fitness proxy, one may be concerned about the drug resistance phenotype itself and its genetic architecture.

In summary, rank order methods have potential for the interpretation of empirical data, as well as for relating higher order gene interactions and evolutionary dynamics. Our approach facilitates detecting higher order epistasis from a very broad range of empirical data, and will therefore contribute to enhancing our general understanding of empirical fitness landscapes and epistatic gene interactions.

## Materials and methods

## Mathematical framework and proofs

Here we provide proofs for the results in the main text, and give a brief background on the discrete Fourier transform, Dyck words, and Catalan numbers. Catalan numbers (Stanley, 1999) have rarely been used in biology, so we describe them briefly without assuming any knowledge. Several arguments in the Materials and methods depend on elementary combinatorics, and the reader may consult a general text, such as Grimaldi (2006).

We start with rank orders and the total n-way epistasis, followed by more general results on rank orders, circuits and other linear forms. The next topic is epistasis and fitness graphs, including some related graph theory. Finally we provide a few observations on epistasis and partial orders.

Gene interactions for a biallelic n-locus system can be described in terms of the Fourier transform for (ℤ2)n defined as ui1⁢i2⁢…⁢in=12n-1⋅∑j1=01∑j2=01⋯⁢∑jn=01(-1)i1⁢j1+i2⁢j2+…+in⁢jn⁢wj1⁢j2⁢…⁢jn.

By abuse of notation we will ignore the scaling factor 12n-1. We define interaction coordinates as the elements ui1⁢i2⁢…⁢in such that at least two entries in i1⁢i2⁢…⁢in are 1. The interaction coordinate u1⁢…⁢1 measures the total n-way epistasis, u1⁢…⁢1=∑j1=01∑j2=01⋯⁢∑jn=01(-1)j1+j2+…+jn⁢wj1⁢j2⁢…⁢jn.

In particular,u11=w00-w10-w01+w11=ε2

andu111=w000-w100-w010-w001+w110+w101+w011-w111=ε3

as defined in Equations 1 and 2 in the main text. A biallelic three-locus system has three-way epistasis exactly if u111≠0. Otherwise the system has only pairwise interactions. Similarly, a biallelic n-locus system has (total) n-way epistasis exactly if u1⁢…⁢1≠0.

The remaining interaction coordinates of the three-locus system areu110=w000-w100-w010+w001+w110-w101-w011+w111,u101=w000-w100+w010-w001-w110+w101-w011+w111,u011=w000+w100-w010-w001-w110-w101+w011+w111.

Weinreich et al. (2013) characterize epistatic interactions using Walsh coefficients, which are closely related to interaction coordinates. Specifically, the Walsh coefficients E111, E110, E101, E011 differ from the interaction coordinates u111, u110, u101, u011 only by a scalar. Here we ignore scalars, since we focus on the signs of the interactions coordinates only. It follows that all our results on interaction coordinates hold for Walsh coefficients as well.

## Rank orders

We will determine the number of rank orders which imply n-way epistasis. The proof depends on Catalan numbers and Dyck words (Stanley, 1999). Let Ci denote the ith Catalan number for i≥0, that is, Ci=(2⁢i)!(i+1)!⁢i!. In particular, C0=C1=1,C2=5, C3=14 and C4=42. A Dyck word of length 2⁢n in the letters X and Y is a string consisting of nX’s and nY’s such that no initial segment of the string has more Y’s than X’s. For instance, the Dyck words of length 4 are X⁢X⁢Y⁢Y and X⁢Y⁢X⁢Y. The initial segments of X⁢X⁢Y⁢Y are X, X⁢X, X⁢X⁢Y, and X⁢X⁢Y⁢Y.

Proposition 1. Consider a biallelic n-locus system. The number of rank orders which imply n-way epistasis is(2n)!×22n-1+1

Proof. There are (2n)! rank orders in total. Let ei denote the fitnesses of genotypes with an even number of 1’s in the subscripts (w0⁢…⁢0, w110⁢…⁢0, and so forth) and oi the fitnesses of genotypes with an odd number of 1’s, ordered in such a way that ei>ei+1 and oi>oi+1 for all i. We will refer to even and odd elements from now on. Let u1⁢…⁢1 denote the interaction coordinate as defined above. Notice that u1⁢…⁢1=0 exactly if ∑iei-∑ioi=0. Consequently a rank order implies positive n-way epistasis (u1⁢…⁢1>0) when the sum ∑i(ei-oi) is positive for all fitness landscapes compatible with the rank order. It is therefore sufficient to count such rank orders.

We define a map from fitness rank orders to words in the alphabet {e,o} as follows: ei↦e,oi↦o. For instance, the order w00>w11>w10>w01 is mapped to e⁢e⁢o⁢o. We claim that a rank order satisfies ∑i(ei-oi)>0 exactly when it is mapped to a Dyck word (where e precedes o).

It is immediate that ∑i(ei-oi)>0 holds if the rank order is mapped to a Dyck word. Conversely, suppose that a rank order is not mapped to a Dyck word. Let s be the least number such that the number of o’s exceeds the number of e’s for an initial segment of length s (note that s has to be odd in this case) and let j=s+12. Clearly one can make the sum of ∑i=1j(ei-oi) negative for a particular choice of ei and oi. By choosing the remaining numbers ei,oi sufficiently small, we get ∑i(ei-oi)<0, which proves the claim.

It remains to count the rank orders where ∑i(ei-oi)>0. Such rank orders are mapped to Dyck words (where e precedes o) consisting of 2n−1X’s and 2n−1Y’s. There are C2n-1 such Dyck words (Stanley, 1999). For each word there are (2n-1)!×(2n-1)! fitness rank orders which map to the word. Indeed, one can choose the ordering of even and odd elements each in (2n-1)! different ways.

In total there are C2n-1×(2n-1)!×(2n-1)! fitness rank orders such that ∑i(ei-oi)>0 for all landscapes. By symmetry, the same number of fitness rank orders satisfy the negative epistasis condition ∑i(ei-oi)<0. One verifies thatC2n-1×(2n-1)!×(2n-1)!×2=(2n)!×2(2n-1+1),

which completes the proof.□

A few observations in the proof of Proposition 1 are of interest. Importantly, the proof gives a computationally efficient method (linear in the number of genotypes) for checking if a rank order implies n-way epistasis. Indeed, the rank order implies higher order epistasis exactly if it is mapped to a Dyck word. Moreover, the proposition states that (2n)!×2(2n-1+1) orders imply n-way epistasis. From the proof it is clear that half of these orders imply positive n-way epistasis (u1⁢…⁢1>0) and the other half negative n-way epistasis (u1⁢…⁢1<0). Also, the proof points out some symmetries. If a rank order implies epistasis, then the same is true for rank orders obtained by (i) any permutation of the even elements, (ii) any permutation of the odd elements, and (iii) the flip obtained by replacing every “<” by “>” in the rank order. It follows that each rank order that implies three-way epistasis belongs to a class of 1152(=4!⋅4!⋅2) elements, which differ by the operations (i)–(iii) only.

Corollary 2. The fraction of rank orders that imply n-way epistasis among all rank orders is22n-1+1.

Proof. Since the number of all rank orders is (2n)!, the result follows. □

The results on rank orders and epistasis for 2≤n≤4 are summarized in Table 1. Notice that the expression in the corollary approaches 12n-2 for large n.

Interestingly, no integer sequence that starts with 16, 16 128, … is available at The On-Line Encyclopedia of Integer Sequences (2016).

## Circuits

The proof of Proposition 1 depends on the map defined from the rank orders to words in the alphabet {e,o}. We will use a generalization of the map in subsequent proofs. The starting point is a given linear form. The form determines a map from rank orders to words. Although the idea is closely related to the previous proof, we will work with positive and negative coefficients in the linear forms. For that reason, we will use P and N rather than e and o (even and odd is no longer meaningful).

We start with a clarifying example. Assume that a given linear form has integer coefficients and that the sum of its coefficients is zero. For instance, the formm=w001+w010+w100-w111-2⁢w000

defines a map φm as follows: Each of the variables w001,w010,w100 corresponds to the letter P (for positive), and the variable w111 corresponds to N (for negative). The variable w000 corresponds to N⁢N, because of the coefficient -2. In this case, the rank order w111>w001>w000>w100>w010>w110>w101>w011

is mapped to N⁢P⁢N⁢N⁢P⁢P under φm. Specifically, starting from left w111 corresponds to N, w001 to P, w000 to N⁢N, w100 to P, and w100 to P. The remaining variables w110,w101,w011 do not impact the word, since their coefficients are zero for the form m.

Definition 1. Let f be a linear form with integer coefficients. Assume that the sum of its coefficients is zero. Let φf denote the map from a total order on the variables (a rank order) to words in the alphabet {P,N} defined as follows: Each variable of f with a positive integer coefficient c corresponds to a substring of c letters P. Each variable in f with a negative integer coefficient c′ corresponds to a substring of |c′| letters N. A rank order of the variables is mapped to the word consisting of the substrings obtained for each variable with non-zero coefficient in f. Specifically, the substrings (from left to right) of the word correspond to the variables in the rank order (from highest to lowest fitness).

The proof of Proposition 1 uses e and o instead of P and N. However, notice that the map from rank orders to words in e’s and o’s is exactly φu1⁢…⁢1 (modulo the labeling). The next result is a generalization of Proposition 1. The proof is similar in every step with the modification that φu1⁢…⁢1 is replaced by φf for an arbitrary form f, so we omit the details.

Theorem 3. Let f be a linear form with integer coefficients. Assume that the sum of its coefficients is zero. Then a rank order implies that f is not zero if and only if it is mapped to a Dyck word by φf.

We define additive dependence relations as linear forms that are zero for all additive landscapes. Theorem 3 applies to all additive dependence relations, because the coefficients of an additive dependence relation sum to zero. This fact explains why our Dyck word-based method applies broadly. All we require is that an epistasis measure is defined by linear forms, as any such measure is zero on additive fitness landscapes. In particular, Theorem 1 applies to n-way epistasis, interaction coordinates, and circuits. However, some approaches to epistasis are of a completely different type, for instance the approach based on Shannon entropy (Moore et al., 2006), in which case rank order methods may not apply.

Recall from the main text that a=w000-w010-w100+w110 is a circuit. In particular, a=0 for all additive fitness landscapes. Moreover, a is minimal with this property, in the sense that no linear form in a proper subset of {w000, w010, w100, w110} equals zero for all additive landscapes. In general, circuits are defined as minimal (additive) dependence relations, in the sense that the set of wg which appear with non-zero coefficient is minimal with respect to inclusion.

There are 20 circuits a,…,t for the three-locus system (Beerenwinkel et al., 2007), namely a:=w000-w010-w100+w110b:=w001-w011-w101+w111c:=w000-w001-w100+w101d:=w010-w011-w110+w111e:=w000-w001-w010+w011f:=w100-w101-w110+w111g:=w000-w011-w100+w111h:=w001-w010-w101+w110i:=w000-w010-w101+w111j:=w001-w011-w100+w110k:=w000-w001-w110+w111l:=w010-w011-w100+w101m:=w001+w010+w100-w111-2w000n:=w011+w101+w110-w000-2w111o:=w010+w100+w111-w001-2w110p:=w000+w011+w101-w110-2w001q:=w001+w100+w111-w010-2w101r:=w000+w011+w110-w101-2w010s:=w000+w101+w110-w011-2w100t:=w001+w010+w111-w100-2w011

Before describing applications of Theorem 3 in more detail, we will compare different approaches to epistasis. As already noted, interaction coordinates (Beerenwinkel et al., 2007) and Walsh coefficients of order two or more (Weinreich et al., 2013) differ only by a scalar. However, circuits provide information of a different type. To see this, we consider the two circuits a=w000-w010-w100+w110b=w001-w011-w101+w111

which measure epistasis between the first and the second locus conditional on the third locus being fixed to 0 and 1, respectively. If a=-b for a system, then u110=0 (and the Walsh coefficient E110=0 as well), because u110=a+b. If, in addition, |a|=|b| is a large number, then the first and second loci have substantial interactions as measured by a and b, yet the interaction coordinate u110 captures only the average effect which is zero and would indicate no interaction.

Even if one knows the signs of all interaction coordinates u111, u110, u101, and u011, one may still be ignorant about important gene interactions. In contrast, the signs of all 20 circuits provide a more complete description of the gene interactions from a qualitative point of view. In this sense, it is natural to say that two fitness landscapes have similar gene interactions if their circuit sign patterns agree.

One type of circuits measures conditional epistasis, and they relate to interaction coordinates in an interesting way. More precisely, conditional epistasis concerns subsystem obtained by fixing a subset of coordinates at 0 or 1 and varying the remaining loci. Conditional epistasis for an n-locus subsystem agrees with the total n-way epistasis for the subsystem. In particular, the circuits a and b measure conditional epistasis. The circuit a measures epistasis for the two-locus subsystem of genotypes with last coordinate 0, and the circuit b measures epistasis for the two-locus subsystem of genotypes with last coordinate at 1. As mentioned, the interaction coordinate u110 is the average of a and b (modulo a constant).

The relation between interaction coordinates and circuits is similar for larger systems. For instance, the circuit w0000-w0100-w1000+w1100,

measures conditional epistasis for the two-locus subsystem obtained by fixing the last two coordinates at zero. The interaction coordinate u1100 measures the average effect of four different circuits that measure conditional epistasis. In summary, all interaction coordinates can be interpreted as averages of circuits expressing conditional epistasis.

Technically, the 20 circuits can be obtained as linear combinations of the interaction coordinates u111, u110, u101, and u011. However, none of the interaction coordinates are themselves circuits, since they do not satisfy the condition of being minimal.

The circuits a,…,f all measure conditional two-way epistasis between two loci when the allele at the third locus is fixed. But there are other types of circuits. The circuits g,…,l relate marginal epistasis of two pairs of loci, and the circuits m,…,t relate the three-way interaction to the total two-way epistasis (Beerenwinkel et al., 2007).

For a given circuit, some rank orders imply that the circuit is positive, that is, the circuit is positive for all fitness values compatible with the rank order. Similarly, some rank orders imply that the circuit is negative, whereas the sign cannot be determined from other rank orders. We will use Theorem 3 to check whether a rank order determines the sign of a circuit or not.

Corollary 4. For the circuits a,…⁢l, two thirds of all possible rank orders determine the sign of the circuit. For the circuits m,…,t, one half of all possible rank orders determine the sign of the circuit.

Proof. Fix one of the circuits from a to l and a rank order. The circuit has exactly four variables with non-zero coefficients (for instance, for the circuit a the variables are w000, w100, w010, w110, so that φa maps rank orders to four-letter words). By Theorem 3, the rank order implies that the circuit differs from zero when it is mapped to one of the Dyck words P⁢P⁢N⁢N, P⁢N⁢P⁢N, N⁢N⁢P⁢P or N⁢P⁢N⁢P under φ, whereas the sign of the circuit is not determined when the word is P⁢N⁢N⁢P or N⁢P⁢P⁢N. One concludes that the sign of a given circuit from a to l is determined for 2/3 of the rank orders.

Using a similar argument, we consider words of length 6 for the circuits labeled m to t. There are in total 20 words consisting of 3P’s and 3N’s. Ten of them are Dyck words. We conclude that the sign of a given circuit from m to t is determined for 1/2 of the rank orders. □

In general, it is not possible to decompose the word obtained for analyzing n-way epistasis into informative subunits. For example, as mentioned in the main text, the first half of the word o⁢o⁢e⁢e⁢e⁢o⁢o⁢e is o⁢o⁢e⁢e, and it does not appear to reveal any interesting information about the system. On the other hand, if one knows that the word o⁢o⁢e⁢e⁢e⁢o⁢o⁢e was obtained from the rank orderw010>w111>w110>w101>w011>w100>w001>w000,

then one can identify meaningful parts of the word. For instance, consider the subsystem of genotypes with last coordinate 0. The corresponding letters (the first, third, sixth and eighth letter of the word o⁢o⁢e⁢e⁢e⁢o⁢o⁢e) form the four-letter word o⁢e⁢o⁢e, which implies that the corresponding subsystem has sign epistasis. Moreover, there is no connection between words used for analyzing three-way epistasis and the words representing Walsh-coefficients. For instance, in order to analyze u110 one maps the rank order above to N⁢P⁢P⁢N⁢N⁢N⁢P⁢P, but the two words o⁢o⁢e⁢e⁢e⁢o⁢o⁢e and N⁢P⁢P⁢N⁢N⁢N⁢P⁢P are unrelated.

The gene interactions for a biallelic three-locus system can be classified in terms of shapes of the fitness landscape, or triangulations of the 3-cube (Beerenwinkel et al., 2007). There are 74 shapes for the 3-cube. The shape of the fitness landscapes is determined by the signs of the 20 circuits. It follows that rank orders provide some information about possible shapes. However, the following result shows that rank orders do not determine shapes.

Proposition 5. Consider a three-locus biallelic system. No rank order determines the shape of a fitness landscape.

Proof. The result follows from the characterization of shapes for the 3-cube in (Beerenwinkel et al., 2007), where each shape is described in terms of a circuit sign pattern. We verified computationally that no rank order implies that all the circuits have the signs which describe a particular shape (https://github.com/gavruskin/fitlands#analysis-of-rank-orders) . More precisely, for every circuit a,…,t, we determined the set of all rank orders that imply that the circuit is positive or negative.

For every rank order, we then considered the circuit signs determined by the order. In no case did a rank order determine all the circuit signs necessary for describing a particular shape.□

The fact that rank orders do not determine the shape of a fitness landscape over a three-locus system is not surprising. Shapes reflect interactions in a very fine scaled way, whereas rank orders provide only coarse information.

Corollary 6. For each of the interaction coordinates u110, u101, and u011, the number of rank orders which determines its sign is 16,128.

Proof. The linear form for each interaction coordinate consists of 8 elements, 4 with positive signs and 4 with negative signs. Notice that 16,128 rank orders imply three-way epistasis, by Proposition 1. By Theorem 3 the problem can be reduced to counting Dyck words of length 8. It follows that the number of rank orders is 16,128 for each interaction coordinate.□

Note that the sign of a given interaction coordinate is determined for 16,128 out of 40,320 rank orders, that is 2/5 or all rank orders. As mentioned, the Walsh coefficients E110, E101, E011 differ from the interaction coordinates u110, u101, u011 only by a scalar, so that Corollary 6 applies to the coefficients as well.

## Partial orders and fitness graphs

We now consider partial orders, for instance,w111>w110,w100,w010,w001>w000>w101,w011

for a three-locus system. Arguing as in the proof of Proposition 1, the (unknown) total order is mapped to the word o⁢x⁢x⁢x⁢x⁢e⁢e⁢e under φu1⁢…⁢1, where x⁢x⁢x⁢x is some permutation of e⁢o⁢o⁢o. For any such permutation we get a Dyck word. It follows that the system has three-way epistasis. This condition can be stated and proved in a more general form.

Proposition 7. Consider an n-locus biallelic system. Let ei and oi be defined as in the proof of Proposition 1. If there exists a partition of the total set of fitness values into pairs (ei,oi), where ei>oi for all i, then one can conclude n-way epistasis. By symmetry, the same is true for a partition where ei<oi for each pair.

Proof. We will verify that the existence of a partition as described is equivalent to the order being mapped to a Dyck word under the map φu1⁢…⁢1. It is immediate that the existence of such a partition implies that the order is mapped to a Dyck word. Conversely, if the rank order is mapped to a Dyck word under φu1⁢…⁢1, then one can construct a partition as follows. One pair in the partition corresponds to the first e and the first o in the Dyck word, a second pair corresponds to the second e and the second o in the word, and so forth. This partition has the desired property.□

A fitness graph is a directed acyclic graph where each node represents a genotype, and arrows connect each pair of mutational neighbors, directed toward the node representing the genotype of higher fitness. Moreover, fitness graphs are structured so that the node labeled 0⁢…⁢0 is at the bottom, genotypes with exactly one 1 on the level above, and so forth (see Figure 6).

Our systematic analysis of fitness graphs takes advantage of the fact that some graphs are isomorphic, that is, there exists an edge preserving bijection between the nodes of the graphs. In biological terms, an isomorphism can be considered a relabeling of the genotypes such that mutational neighbors stay neighbors and the direction of arrows indicating higher fitness is preserved. For example, Figure 5 shows two isomorphic fitness graphs.

The analysis of the two-locus case is straightforward. An arbitrary fitness graph is isomorphic to a graph where 00 has the lowest fitness. There are four fitness graphs satisfying the assumption. Indeed, two of the arrows point up, so that there are in total 2×2=4 possible fitness graphs depending on the directions of the remaining arrows (Figure 3). By inspection, two of the graphs in the figure are isomorphic. Consequently, there are three different fitness graphs for two-locus systems up to isomorphism.

Some fitness graphs imply epistasis, whereas other fitness graphs are compatible with additive fitness. As illustrated in the two-locus case, a fitness graph is compatible with additive fitness if all arrows point up, that is toward a higher level. More generally, a fitness graph implies epistasis unless it is isomorphic to a graph where all arrows point up. Indeed, the graph implies sign epistasis unless such an isomorphism exists. (Weinreich et al., 2005; Crona et al., 2013).

Accordingly, we can characterize rank orders that are compatible with fitness graphs with all arrows up. After relabeling genotypes, we can assume that the genotype 0⁢…⁢0 has the lowest fitness in the system. Then a rank order is compatible with a fitness graph with all arrows up, exactly if for each genotype replacing 0 by 1 results in higher fitness. For instance, w00<w10<w01<w11 is compatible with such a graph whereas the rank order w00<w11<w01<w10 is not.

If 000 has the lowest fitness in the system, one can verify that exactly 48 rank orders are compatible with the fitness graph with all arrows up. It follows that in total 8×48=384 rank orders are compatible with such graphs since there are eight genotypes in a three-locus system, each of which can have lowest fitness.

Interestingly, the same result can be obtained from theory on house-of-cards landscapes. Since all rank orders are equally likely under this statistical fitness landscape model, the fraction of rank orders that imply sign epistasis agrees with the probability of sign epistasis. This probability is 104105 (Schmiegelt and Krug 2014, Table 2). It follows that 8!×1105=384 rank orders are compatible with fitness graphs with all arrows up, that is, the total number of rank orders multiplied by the fraction of rank orders compatible with such graphs.

As we have already seen, rank orders have potential far beyond detecting whether or not there is epistasis in a system. The same is true for fitness graphs, and we proceed with higher order interactions. In order to analyze fitness graphs and three-way epistasis, we consider the set of rank orders compatible with a given fitness graphs. For instance, the fitness graph in Figure 10 is compatible with the following two rank orders:(5)w111>w000>w100>w010>w001>w110>w101>w011,(6)w000>w111>w100>w010>w001>w110>w101>w011.

The first order implies three-way epistasis (it is mapped to o⁢e⁢o⁢o⁢o⁢e⁢e⁢e under φu1,…,1) and the second does not (it is mapped to e⁢o⁢o⁢o⁢o⁢e⁢e⁢e under φu1,…,1). We conclude that in this case, the fitness graph does not imply higher order epistasis. However, if every rank order compatible with the fitness graph implies higher order epistasis, then the fitness graph itself does imply higher order epistasis. More generally, the same observation holds for any partial order.

![Figure 10.](https://cdn.elifesciences.org/articles/28629/elife-28629-fig10-v1.jpg)

**Figure 10.:** Those depicted in red imply three-way epistasis.

Remark. A partial order implies higher order epistasis exactly if all its total extensions imply higher order epistasis.

Indeed, if all total extensions imply higher order epistasis, then in particular the (unknown) rank order does. The converse holds by definition.

Consequently, one can in principle determine if a fitness graph implies higher order epistasis by checking all of the compatible rank orders. For a systematic study of the three-locus case, it is convenient to reduce the problem to isomorphic graphs. Figure 5 shows two isomorphic fitness graphs.

As mentioned in the main text, there are in total 1,862 fitness graphs for three-locus systems, and the number of fitness graphs that imply higher order epistasis is 698 (37 percent). Up to isomorphism there are in total 54 fitness graphs, and 20 graphs imply higher order epistasis. This result was verified by reducing the study of all 1,862 graphs for three-locus systems to a non-redundant list of 54 graphs, such that no two graphs in the list are isomorphic. The fact that the total number of graphs is 1,862 follows from general theory on acyclic graphs (Stanley, 2006), or can be verified computationally (see below).

Isomorphisms between three-locus systems have a geometric interpretation. The fitness graph can be regarded as a three-dimensional cube, with vertices corresponding to genotypes and edges corresponding to arrows. The group of isomorphisms (see below) then corresponds to the symmetry group of the three dimensional cube (Coxeter, 1973). Indeed, it was by way of this equivalence that we carried out the enumeration described above.

For clarity, we give a more explicit description of the cube isomorphisms. Any isomorphism can be constructed as a composition of the following two transformations: (i) interchange of labels of the pair of alleles at a locus, and (ii) change of order of the loci in the bitstring representation of a genotype. There are in total forty-eight isomorphisms of the cube, including the identity transformation which leaves the cube unchanged. Figure 5 is an example of such a transformation, where at the first locus the labels 0 and 1 have been swapped, and the second and third loci have been interchanged. The code used for verifying the isomorphisms is available at https://github.com/devingreene/3-cube-partial-order-count.git.

A cube has 12 edges, so that the total number graphs on the cube (graphs similar to fitness graphs, but cycles are allowed) is 212=4096. After exclusion of graphs with cycles, 1,862 graphs remain. An arbitrary graph is isomorphic to a graph where 000 has the lowest fitness. This relabeling reduces the number of graphs one has to consider substantially, as in the two-locus case. The list of remaining graphs can be reduced further using the isomorphisms described above to finally obtain 54 graphs (Figure 3).

## Graph theoretical aspects

As mentioned in the main text, the 20 graphs which imply higher order epistasis (see Figure 6) constitute a diverse category. We analyzed the category from a graph theoretical point of view, but could not see that the graphs have any property which singles them out.

Recall that a unique sink orientation is a graph where each face has no more than one sink. Equivalently, there is no subsystems with reciprocal sign epistasis (Crona et al., 2013; Poelwijk et al., 2007). The category of 20 graphs includes unique sink orientations (also called USO or AOF graph s), as well as non-USO’s. Moreover, in the terminology of Gärtner and Kaibel, 1998, the category includes separable and non-separable graphs, as well as realizable and non-realizable graphs.

There were some indications of higher complexity for the category, but only in a statistical sense. Indeed, as can be verified from Figure 6, the graphs in the category have on average 1.8 sinks (a sink corresponds to a peak in the landscape), whereas the average number of sinks for all graphs is 1.6. Moreover, 5 out of the 20 graphs (25 percent) in the category are unique sink orientations, whereas in total 19 out of the 54 graphs (35 percent) are unique sink orientations.

Even though the category of fitness graphs which implies epistasis is diverse, it is still possible that a characterization exists. This is an open problem.

## Software and HIV-1 study

We have implemented algorithms based on our theoretical results in an open source software package (https://github.com/gavruskin/fitlands#fitlands). The package provides software for detecting gene interactions as described in the main text for two- and three-locus systems. Furthermore, algorithms for detecting total n-way epistasis, three- and four-way interaction coordinates and three-way circuit interactions have been implemented. The documentation also explains how to reproduce results for our application to HIV-1 data described in the main text.

The results of Student’s t-test explained in the main text are summarized in Table 1, and for related code see https://github.com/gavruskin/fitlands/blob/master/HIV_2007_conventional_analysis.ipynb
