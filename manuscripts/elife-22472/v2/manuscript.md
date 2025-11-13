# Codon optimization underpins generalist parasitism in fungi

## Authors

- Thomas Badet<sup>1</sup>
- Remi Peyraud<sup>1</sup>
- Malick Mbengue<sup>1</sup>
- Olivier Navaud<sup>1</sup>
- Mark Derbyshire<sup>2</sup>
- Richard P Oliver<sup>2</sup>
- Adelin Barbacci<sup>1</sup> ([ORCID: 0000-0003-3156-272X](https://orcid.org/0000-0003-3156-272X))
- Sylvain Raffaele<sup>1</sup> ([ORCID: 0000-0002-2442-9632](https://orcid.org/0000-0002-2442-9632)) †

### Affiliations

1. LIPM, Université de Toulouse, INRA, CNRS Castanet-Tolosan France
2. Centre for Crop and Disease Management, Department of Environment and Agriculture Curtin University Perth Australia

† Corresponding author

## Abstract

The range of hosts that parasites can infect is a key determinant of the emergence and spread of disease. Yet, the impact of host range variation on the evolution of parasite genomes remains unknown. Here, we show that codon optimization underlies genome adaptation in broad host range parasites. We found that the longer proteins encoded by broad host range fungi likely increase natural selection on codon optimization in these species. Accordingly, codon optimization correlates with host range across the fungal kingdom. At the species level, biased patterns of synonymous substitutions underpin increased codon optimization in a generalist but not a specialist fungal pathogen. Virulence genes were consistently enriched in highly codon-optimized genes of generalist but not specialist species. We conclude that codon optimization is related to the capacity of parasites to colonize multiple hosts. Our results link genome evolution and translational regulation to the long-term persistence of generalist parasitism.

## Introduction

The host range of a parasite has a central influence on the emergence and spread of disease (Woolhouse and Gowtage-Sequeria, 2005). There is a clear demarcation between specialist parasites that can only infect one or a few closely related host species and generalists that can infect more than a hundred unrelated host species (Woolhouse et al., 2001; Barrett et al., 2009). The host range is a trait constrained by ecological and physiological factors and determined by the evolutionary history of a parasite and its potential hosts (Poulin and Keeney, 2008). Host specialization is a frequent pattern in living systems that was proposed to result from tradeoffs in performance on multiple hosts (Joshi and Thompson, 1995). At the molecular level, optimization by natural selection of parasite proteins functioning in the interaction with a given host may be detrimental to their function in another species (Dodds and Rathjen, 2010; Dong et al., 2014). Nevertheless, generalists able to thrive on a broad range of hosts are found in most parasite lineages. The molecular mechanisms associated with the evolution of generalist parasitism remain, however, elusive. Notably, the extent to which interaction with multiple hosts affects the evolution of parasite genomes remains unknown.

Genomic analyses of obligate specialist parasites revealed massive losses of enzymes unnecessary for growth and reproduction on living hosts (Schirawski et al., 2010; Spanu et al., 2010). Instead, such specialists rely largely on a sets of small secreted protein (SSPs) subverting host cell function. For instance, the genome of the powdery mildew pathogen Blumeria graminis f. sp. hordei harbors 180 SSPs of about 100–150 amino acids (Pedersen et al., 2012). SSPs of specialist fungi often show evidence of diversifying-selection leading to extensive changes in their protein sequence (Stukenbrock et al., 2011; Pedersen et al., 2012; Hacquard et al., 2013). By contrast, the secretion of a battery of degrading enzymes is crucial for the parasitic success of generalists (Hu et al., 2014; Kubicek et al., 2014). The genomes of generalist fungi notably contain in average ~3 times more carbohydrate activity enzymes (CAZYmes) than specialist fungi (Zhao et al., 2013). For instance, Rhizoctonia solani AG2-2IIIB contains over 1000 CAZYme genes (Wibberg et al., 2016). Protein translation is the largest consumer of energy during cellular proliferation, and because secreted proteins are not recycled like other cellular proteins, strong constraints exist to reduce the synthetic cost of secreted proteins in microbes (Smith and Chapman, 2010). Considering the distinct properties of secreted proteins in specialist and generalist parasites, the impact of protein translation efficiency on the cost of secreted protein synthesis likely differ in these organisms.

The differential use of synonymous codons in a genome, or codon usage bias, affects gene expression level, protein folding, translation efficiency and accuracy (Plotkin and Kudla, 2011). In particular, the co-evolution of codons with the genomic tRNA complement, leading to codon optimization, results from the combination of neutral processes and selection for the optimization of protein translation (Hershberg and Petrov, 2008; Shah and Gilchrist, 2011). Natural selection for the optimization of protein translation, through ribosome pausing time, translation error rates and co-translational protein folding, has been widely associated with codon usage biases (Drummond and Wilke, 2008; Tuller et al., 2010; Shah and Gilchrist, 2011). Because the probability of protein translation error increases with protein length, selection for translation accuracy can be higher in genes encoding long proteins, as was observed in E. coli (Eyre-Walker, 1996). Codon usage bias also increases with the evolutionary age of genes, the frequency of codons optimal for translation being significantly higher at codons for conserved amino acids (Marais and Duret, 2001; Prat et al., 2009). Considering that highly expressed secreted proteins are often longer and more conserved in generalist than in specialist parasites, we expect natural selection on the optimization of codons to be stronger in generalist parasites than in host specialists.

The cost of protein translation leads to a tradeoff between protein production and cell growth rate (Scott et al., 2010; Shah et al., 2013; Kafri et al., 2016). Codon optimization therefore impacts cell growth in selective environments (Botzman and Margalit, 2011; Krisko et al., 2014), and could positively impact on the performances of parasites regardless of the host they encounter. This hypothesis would be consistent with generalist lineages performing better on average on their set of available hosts than co-occurring specialist competitors to persist in the biota, as predicted by the 'jack of all trades, master of none' theoretical model (Futuyma and Moreno, 1988). Here, we have examined the strength of natural selection on the optimization of codons in parasites with contrasted host range across the fungal kingdom. Because the genomes of broad host range parasites generally encode longer proteins, an in silico model of the cell translation machinery predicts that natural selection on codon optimization should be stronger in these species. Consistent with this prediction, we found that codon optimization at the genome scale correlates with fungal parasites host range. High codon optimization and broad host ranges co-evolved multiple times independently through fungal phylogeny. To document the molecular bases of codon optimization at the species level in generalist fungi, we compared single-nucleotide polymorphism (SNP) patterns in natural populations of a generalist and a specialist fungal parasite. We detected signatures of purifying natural selection acting on optimal codons in the generalist parasite only. Finally, we show that genes associated with virulence are better codon-optimized in generalist than in specialist parasite genomes supporting codon optimization as an adaptation to the colonization of multiple hosts. Together, our results reveal patterns of adaptive genome evolution associated with generalism that are conserved through the fungal Kingdom. Furthermore, we establish a link between translational regulation and host range variation through genomic patterns of codon optimization, contributing to our understanding of the dynamics of disease epidemics.

## Results

### Long proteins encoded by the genome of generalist fungi likely increase natural selection on codon optimization

The efficiency and accuracy of protein translation constrains cell growth rate and depends on sequence properties of expressed proteins (Ingolia et al., 2009; Kafri et al., 2016). To evaluate the impact of translation efficiency on cell growth during host colonization, we calculated theoretical maximal growth rates for cells of generalist and specialist fungal parasites. For this, we designed an in silico model of the cell translation machinery describing the accumulation over time of ribosomal proteins, other intracellular proteins and secreted proteins from which the maximal cell growth rate can be deduced (see ‘Materials and methods’, Figure 1—source data 1). To calculate the typical protein synthesis rate, the model uses the median length of ribosomal, intracellular and secreted proteins as input. We determined these values in the complete predicted proteomes of 13 host-specialist fungi (less than four host genera) and 15 generalist fungi (over 10 host genera) all belonging to different genera and covering most major fungal clades (Figure 1A, Figure 1—source data 1). In average, secreted proteins were ~14.8% longer in generalists than in specialists (365 and 318 codons respectively; Welch’s t-test p<10−08). Intracellular proteins were also longer in average in generalists than in specialists (~10.1% longer with 381 and 346 codons respectively; Welch’s t-test p<10−08), whereas ribosomal proteins were slightly shorter in average in generalists than in specialists (~1.2% shorter with 189 and 192 codons respectively; Welch’s t-test p<10−04). In yeast, codon decoding rate varies from 10 to 28 codons per second, with an average of 20 codons per second (Gardin et al., 2014). We tested the impact of varying the average codon decoding rate from 10 to 28 codons per second on the maximal cell growth rate predicted by our model for generalist and specialist fungal cells (Figure 1B). Cells of specialists achieved higher maximal growth rates than cells of generalists at a given codon decoding rate. Reciprocally, cells of generalists require higher codon decoding rate to reach maximal growth rates similar to cells of specialists. For instance, in order to achieve a growth rate of 4000 cells per 24 hr, the codon decoding rate should be 21.7 codons per second in generalists but only 19.9 codons per second in specialists.

![Figure 1.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig1-v2.jpg)

**Figure 1.:** (A) Distribution of length (number of codons) in the ribosomal, intracellular and predicted secreted proteomes of 13 specialist fungal parasites and 15 generalist fungal parasites. (B) Relationship between codon decoding rate (number of codons translated per second) and cell growth rate of typical specialist and generalist fungi predicted by a cellular model of protein translation. Dotted lines highlight the higher codon decoding rate required in generalist fungi compared to specialist fungi to achieve a growth rate of 4000 cells produced per day. (C) Distribution of length in the proteomes (left) and relationship between codon decoding rate and cell growth rate (right) in related specialist and generalist fungi from the Basidiomycetes, Ascomycetes and Basal Fungi. The width of boxplots is proportional to the number of values. Spe., specialist (green); Gen., generalist (brown). Welch’s t-test p: *<10−01, **<10−04, ***<10−08.

To test the robustness of these observations across the fungal phylogeny, we compared related specialist and generalist species from three major fungal groups: Basidiomycetes, Ascomycetes and Basal Fungi (Figure 1C). In all three groups, secreted proteins were longer in average in generalist species than in specialist species. For instance, secreted proteins of the generalist Botrytis cinerea were in average ~73% longer (394 amino acids) than secreted proteins of the specialist Blumeria graminis f. sp. tritici (228 amino acids; Welch’s t-test p<10−08). Length differences in ribosomal and other intracellular proteins were not consistent through all three clades. Overall, our cell translation machinery model showed in all three cases that generalist species require higher codon decoding rates to achieve similar growth rates as their specialist relatives.

The in silico cell model used here suggests that longer proteins, especially secreted proteins, encoded in the genome of generalist fungi limits maximal cell growth rates compared to specialist fungi. It also shows that codon optimization, leading to higher codon decoding rates, can support the secretion of more complex proteins with limited growth penalty. Although additional factors may contribute, we show that longer protein pools are sufficient to increase the constraints on codon optimization in generalist fungi. We therefore expect natural selection on the optimization of codons to be stronger in generalist parasites than in host specialists.

### Codon optimization correlates with fungal parasites host range

To test this hypothesis, we analyzed patterns of codon optimization in the genomes of 36 fungal parasite species, including the 15 generalist parasites and 13 specialists analyzed previously, as well as 8 species with intermediate host range (between 4 and 10 host genera) (Table 1). For this, we first used a model that infers the degree ‘S’ of coadaptation between codon usage and the genomic tRNA complement at the whole genome scale (dos Reis et al., 2004). S values ranged from −0.032 (Puccinia graminis) to 0.843 (Cryptococcus neoformans), with an average of 0.374. We performed a correlation analysis and found that codon optimization at the whole genome scale increased with host range (Spearman rho = 0.82, p=7.1 10−10, Figure 2A). Generalist species had an average S of 0.58, whereas the average S was 0.23 for specialists. We verified the significance of the correlation between host range and genome scale codon optimization using Felsenstein’s phylogenetic independent contrasts, and obtained Spearman rho of 0.6 (p=1.5 10−05).

![Figure 2.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig2-v2.jpg)

**Figure 2.:** Genome-scale codon optimization correlates with host range in 36 parasites across the kingdom Fungi. Species considered as specialists (less than four host genera) are shown in green, species considered as generalists (over 10 host genera) are shown in brown. Error bars show 95% confidence interval, dotted line shows logarithmic regression of the data. Codon optimization calculated based on knowledge on the tRNA pool (A), on codon usage in ribosomal protein genes (B) and on self-consistent relative codon adaptation (C) correlated with host range at Spearman ρ≥0.59 (p≤2.7 10−05) under phylogenetic independent contrasts. (D) Codon optimization is stronger in core orthologs from generalist fungal parasites than in core orthologs from specialist fungal parasites. Left: Distribution of tRNA adaptation indices in 1620 core ortholog genes show significantly higher values in generalist fungi (**, Welch’s t-test p<0.01). Right: Codon optimization calculated as the degree of coadaptation of core ortholog genes to the genomic tRNA pool is significantly higher in generalist fungi (***, Welch’s t-test p<10−04).

**Table 1.**
 List of fungal species analyzed in this work, their host range and genome-scale codon optimization values. Genome-scale codon optimization was calculated using tRNA adaptation indiced (S), codon adaptation indices (SCAI) or self-consistent normalized relative codon adaptation indices (SscnRCA).


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Host range</th>
      <th>Class*</th>
      <th>S</th>
      <th>SCAI</th>
      <th>SscnRCA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cryptococcus neoformans</td>
      <td>800</td>
      <td>Gen.</td>
      <td>0.843</td>
      <td>0.870</td>
      <td>0.860</td>
    </tr>
    <tr>
      <td>Rhizoctonia solani</td>
      <td>690</td>
      <td>Gen.</td>
      <td>0.432</td>
      <td>0.624</td>
      <td>0.583</td>
    </tr>
    <tr>
      <td>Botrytis cinerea</td>
      <td>556</td>
      <td>Gen.</td>
      <td>0.597</td>
      <td>0.675</td>
      <td>0.653</td>
    </tr>
    <tr>
      <td>sclerotinia sclerotiorum</td>
      <td>332</td>
      <td>Gen.</td>
      <td>0.524</td>
      <td>0.583</td>
      <td>0.553</td>
    </tr>
    <tr>
      <td>Beauveria bassiana</td>
      <td>269</td>
      <td>Gen.</td>
      <td>0.616</td>
      <td>0.619</td>
      <td>0.747</td>
    </tr>
    <tr>
      <td>Metarhizium acridum</td>
      <td>228</td>
      <td>Gen.</td>
      <td>0.647</td>
      <td>0.595</td>
      <td>0.712</td>
    </tr>
    <tr>
      <td>Aspergillus fumigatus</td>
      <td>175</td>
      <td>Gen.</td>
      <td>0.609</td>
      <td>0.643</td>
      <td>0.684</td>
    </tr>
    <tr>
      <td>Batrachochytrium dendrobatidis</td>
      <td>153</td>
      <td>Gen.</td>
      <td>0.545</td>
      <td>0.521</td>
      <td>0.602</td>
    </tr>
    <tr>
      <td>Verticilium dahliae</td>
      <td>78</td>
      <td>Gen.</td>
      <td>0.537</td>
      <td>0.426</td>
      <td>0.627</td>
    </tr>
    <tr>
      <td>Fusarium graminearum</td>
      <td>72</td>
      <td>Gen.</td>
      <td>0.788</td>
      <td>0.818</td>
      <td>0.819</td>
    </tr>
    <tr>
      <td>Colletotrichum graminicola</td>
      <td>59</td>
      <td>Gen.</td>
      <td>0.572</td>
      <td>0.444</td>
      <td>0.644</td>
    </tr>
    <tr>
      <td>Rhizopus oryzae</td>
      <td>28</td>
      <td>Gen.</td>
      <td>0.625</td>
      <td>0.563</td>
      <td>0.691</td>
    </tr>
    <tr>
      <td>Penicillium digitatum</td>
      <td>17</td>
      <td>Gen.</td>
      <td>0.545</td>
      <td>0.602</td>
      <td>0.630</td>
    </tr>
    <tr>
      <td>Alternaria brassicicola</td>
      <td>16</td>
      <td>Gen.</td>
      <td>0.400</td>
      <td>0.592</td>
      <td>0.628</td>
    </tr>
    <tr>
      <td>Pyrenophora tritici-repentis</td>
      <td>11</td>
      <td>Gen.</td>
      <td>0.419</td>
      <td>0.569</td>
      <td>0.570</td>
    </tr>
    <tr>
      <td>Pseudogymnoascus destructans</td>
      <td>8</td>
      <td></td>
      <td>0.484</td>
      <td>0.513</td>
      <td>0.505</td>
    </tr>
    <tr>
      <td>Encephalitozoon intestinalis</td>
      <td>7</td>
      <td></td>
      <td>0.313</td>
      <td>0.558</td>
      <td>0.528</td>
    </tr>
    <tr>
      <td>Melampsora larici-populina</td>
      <td>7</td>
      <td></td>
      <td>0.194</td>
      <td>0.142</td>
      <td>0.055</td>
    </tr>
    <tr>
      <td>Stagonospora nodorum</td>
      <td>7</td>
      <td></td>
      <td>0.155</td>
      <td>0.431</td>
      <td>0.462</td>
    </tr>
    <tr>
      <td>Colletotrichum higginsianum</td>
      <td>6</td>
      <td></td>
      <td>0.393</td>
      <td>0.295</td>
      <td>0.480</td>
    </tr>
    <tr>
      <td>Sporisorium reilianum</td>
      <td>5</td>
      <td></td>
      <td>0.476</td>
      <td>0.200</td>
      <td>0.429</td>
    </tr>
    <tr>
      <td>Taphrina deformans</td>
      <td>4</td>
      <td></td>
      <td>0.403</td>
      <td>0.679</td>
      <td>0.671</td>
    </tr>
    <tr>
      <td>Magnaporthe oryzae</td>
      <td>4</td>
      <td></td>
      <td>0.437</td>
      <td>0.424</td>
      <td>0.575</td>
    </tr>
    <tr>
      <td>Puccinia graminis</td>
      <td>2</td>
      <td>Spe.</td>
      <td>−0.032</td>
      <td>0.344</td>
      <td>0.249</td>
    </tr>
    <tr>
      <td>Wolfiporia cocos</td>
      <td>2</td>
      <td>Spe.</td>
      <td>0.217</td>
      <td>0.266</td>
      <td>0.316</td>
    </tr>
    <tr>
      <td>Moniliophthora roreri</td>
      <td>2</td>
      <td>Spe.</td>
      <td>0.406</td>
      <td>0.530</td>
      <td>0.551</td>
    </tr>
    <tr>
      <td>Passalora fulva</td>
      <td>2</td>
      <td>Spe.</td>
      <td>−0.011</td>
      <td>0.513</td>
      <td>0.514</td>
    </tr>
    <tr>
      <td>Rozella allomycis</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.236</td>
      <td>0.096</td>
      <td>0.259</td>
    </tr>
    <tr>
      <td>Nosema ceranae</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.021</td>
      <td>−0.155</td>
      <td>−0.085</td>
    </tr>
    <tr>
      <td>Puccinia triticina</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.204</td>
      <td>0.501</td>
      <td>0.472</td>
    </tr>
    <tr>
      <td>Dothistroma septosporum</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.211</td>
      <td>0.447</td>
      <td>0.354</td>
    </tr>
    <tr>
      <td>Pseudocercospora fijiensis</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.227</td>
      <td>0.495</td>
      <td>0.490</td>
    </tr>
    <tr>
      <td>Zymoseptoria tritici</td>
      <td>1</td>
      <td>Spe.</td>
      <td>−0.019</td>
      <td>0.355</td>
      <td>0.248</td>
    </tr>
    <tr>
      <td>Blumeria graminis</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.116</td>
      <td>−0.187</td>
      <td>0.164</td>
    </tr>
    <tr>
      <td>Erysiphe necator</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.174</td>
      <td>−0.092</td>
      <td>0.117</td>
    </tr>
    <tr>
      <td>Ophiocordyceps unilateralis</td>
      <td>1</td>
      <td>Spe.</td>
      <td>0.166</td>
      <td>0.268</td>
      <td>0.458</td>
    </tr>
    <tr>
      <td>Gonapodya prolifera</td>
      <td>0</td>
      <td>np</td>
      <td>0.115</td>
      <td>0.311</td>
      <td>0.363</td>
    </tr>
    <tr>
      <td>Rhodotorula toruloides</td>
      <td>0</td>
      <td>np</td>
      <td>0.344</td>
      <td>0.385</td>
      <td>0.470</td>
    </tr>
    <tr>
      <td>Serpula lacrymans</td>
      <td>0</td>
      <td>np</td>
      <td>−0.001</td>
      <td>0.379</td>
      <td>0.395</td>
    </tr>
    <tr>
      <td>Laccaria bicolor</td>
      <td>0</td>
      <td>np</td>
      <td>−0.026</td>
      <td>0.237</td>
      <td>0.155</td>
    </tr>
    <tr>
      <td>Agaricus bisporus</td>
      <td>0</td>
      <td>np</td>
      <td>0.361</td>
      <td>0.432</td>
      <td>0.400</td>
    </tr>
    <tr>
      <td>Tuber melanosporum</td>
      <td>0</td>
      <td>np</td>
      <td>0.230</td>
      <td>0.319</td>
      <td>0.349</td>
    </tr>
    <tr>
      <td>Oidiodendron maius</td>
      <td>0</td>
      <td>np</td>
      <td>0.147</td>
      <td>0.442</td>
      <td>0.388</td>
    </tr>
    <tr>
      <td>Myceliophthora thermophila</td>
      <td>0</td>
      <td>np</td>
      <td>0.246</td>
      <td>0.123</td>
      <td>0.323</td>
    </tr>
    <tr>
      <td>Chaetomium globosum</td>
      <td>0</td>
      <td>np</td>
      <td>0.148</td>
      <td>0.204</td>
      <td>0.342</td>
    </tr>
  </tbody>
</table>

_*The class column indicates whether species were considered as generalist (Gen.), specialist (Spe.) or non-parasitic (np)._

Comparing genes codon usage with codon usage for a reference set of highly expressed genes is a classical approach for estimating codon usage bias independently of knowledge of the tRNA repertoire. We determined the codon adaptation index (CAI) (Sharp and Li, 1987) using ribosomal protein genes as a reference set. To allow comparisons of codon optimization across species, we calculated for each species the degree ‘SCAI’ of correlation between codon usage and CAI at the whole genome scale. SCAI ranged from −0.187 (Blumeria graminis f. sp. tritici) to 0.87 (Cryptococcus neoformans), with an average of 0.438 (Figure 2B). SCAI increased with host range (Spearman rho = 0.61, p=9.0 10−06 under phylogenetic independent contrasts) and generalist species had an average SCAI of 0.61, whereas the average SCAI was 0.26 for specialists. O’Neill et al. recently developed the self-consistent normalized Relative Codon Adaptation index (scnRCA) as a measure of codon usage bias that does not rely on a reference gene set and corrects for mutational biases (O'Neill et al., 2013). We calculated for each species the degree ‘SscnRCA’ of correlation between codon usage and scnRCA at the whole genome scale. SscnRCA ranged from −0.085 (Nosema ceranae) to 0.853 (Cryptococcus neoformans), with an average of 0.495 (Figure 2C). SscnRCA increased with host range (Spearman rho = 0.59, p=2.7 10−05 under phylogenetic independent contrasts) and generalist species had an average SscnRCA of 0.67, whereas the average SscnRCA was 0.32 for specialists.

To control for the confounding effects of heterogeneity in the completeness of genome assemblies, we first verified that codon optimization was related to the number of hosts but not genome assembly parameters at ANOVA p<0.01 (Figure 2—source data 1). Comparing codon usage bias for gene sets conserved across species is another established method to compare codon optimization across species independent of genome completeness. We identified a set of 1620 core ortholog genes (COGs) conserved across all the 36 fungal parasite species (Figure 2—source data 2). The tRNA adaptation indices (tAIs) were significantly higher in the orthologs of generalist genomes (median value is 0.361) than in orthologs of specialist genomes (median value is 0.337; Welch’s t-test p<0.01) (Figure 2D). We calculated S for COGs in each genome and found that S is significantly higher for COGs in generalist genomes (median is 0.774) than in specialist genomes (median is 0.167; Welch’s t-test p=9.9 10−06) (Figure 2D). These different analyses converge toward the conclusion that codon optimization at the whole genome scale correlates with fungal parasites host range.

### Codon optimization and host range co-evolved multiple times across fungal phylogeny

To document the evolution of codon optimization in fungi, we reconstructed the ancestral state of codon optimization in fungal phylogeny. To this end, we built a phylogeny of our 36 fungal parasites and 9 non-parasitic fungi distributed among all major clades covered in our study (Figure 3A, Figure 3—source data 1 and 2). We determined the degree of codon optimization in non-parasitic fungal genomes and found that codon optimization was generally lower in non-parasitic fungi than in their generalist relatives (average values for non parasitic fungi were S = 0.157, SCAI = 0.315 and SscnRCA = 0.354). This does not exclude that some lineages of non-parasitic fungi could have evolved high codon optimization, but supports the view that codon optimization increased after the divergence of generalist parasites. To support this conclusion, we inferred the ancestral degree of codon optimization at internal nodes of fungal phylogeny using ML ancestral state estimation (Revell, 2012) (Figure 3A). The fungal parasites species used in this work represented four independent evolutionary paths to extreme generalism (over 100 host genera) with non-parasitic or specialists in the same clade, in the Chytridiomycota, the Agaricomycotina, the Leotiomycetes and the Sordariomycetes (Figure 3A). In all four clades, generalism was associated with an increase in genomic codon adaptation compared to related non-parasitic or specialist species and to the reconstructed ancestral state. For instance, in the Leotiomycetes, the generalist parasites Botrytis cinerea and Sclerotinia sclerotiorum (>300 host genera) both had S > 0.5, whereas the non-parasitic Oidiodendron maius and the host specialists Erysiphe necator and Blumeria graminis f. sp. tritici had S < 0.2. The reconstructed ancestral state for this clade was S = 0.37.

![Figure 3.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig3-v2.jpg)

**Figure 3.:** (A) Phylogeny, genome-scale codon optimization and host range in 36 parasites across the kingdom Fungi. Nine non-pathogenic species belonging to the major branches of Fungi are shown for comparison. The phylogenetic tree was generated using the TimeTree database (Hedges et al., 2015) and PATHd8 (Britton et al., 2007). Codon optimization shown as the size of terminal nodes corresponds to the degree S of coadaptation of all genes to the genomic tRNA pool (dos Reis et al., 2004). Terminal nodes are sized according to genome-scale codon optimization and colored according to host range (grey was used for non pathogen species). Internal nodes are sized according to reconstructed ancestral genome-scale codon optimization, with ancestral S value indicated as a blue label. (B) Correlogram of genome-scale codon optimization and phylogenetic distance along the tree shown in A. Dotted lines delimit 95% confidence interval.

To test for the robustness of the association between host range and codon optimization across fungal phylogeny, we tested whether it could be detected at the sub-Kingdom level. The correlation coefficient between genome-scale codon optimization and host range were between 0.64 and 0.84 for S, SCAI and SscnRCA at the Phylum level in Basidiomycetes and Ascomycetes, and across phyla in non-Dikarya fungi. To unambiguously exclude the impact of phylogeny on the correlation between host range and codon optimization, we calculated Blomberg’s K and Pagel’s λ as two quantitative measures of phylogenetic signal in genome scale codon optimization along the fungal tree (Pagel, 1999; Blomberg et al., 2003). We obtained Blomberg’s K = 0.28 and Pagel’s λ = 0.62. Both measures indicated that evolution of codon optimization is not correlated with the phylogeny along the tree at p<0.01. Then, we used phylosignal (Keck et al., 2016) to build a correlogram between phylogenetic distance and codon optimization (Figure 3B). Correlations were insignificant (in the range −0.05 to 0.1) along the whole tree. These results support the view that codon optimization is associated with host range in fungal parasites.

### Biased SNP patterns underpin with codon optimization in the generalist parasite Sclerotinia sclerotiorum

To get insights into the molecular bases of codon optimization in generalists, we searched for patterns of genome evolution associated with codon optimization at the species level in natural populations of generalist parasites. To this end, we generated genome-wide SNPs data by sequencing five field isolates of the plant pathogenic fungus Sclerotinia sclerotiorum (24,344 coding SNPs). S. sclerotiorum is the causal agent of Sclerotinia rot disease, is notorious for its broad host range encompassing several hundreds of plant genera, and shows strong signatures of codon optimization (S = 0.52). As expected under strong codon optimization, tRNA concentrations determined by small RNA sequencing strongly correlated with the number of tRNA genomic copies, tRNA adaptive values (calculated according to [dos Reis et al., 2004]) and codon usage in S. sclerotiorum (Figure 4—figure supplement 1). We used 131,138 genome-wide coding SNPs of nine isolates of the host-specific plant pathogenic fungus Zymoseptoria tritici (Croll et al., 2013) as a reference species with weak codon optimization (S = −0.02). Overall, the SNP frequency was higher in the Z. tritici population (1.196 SNP.Kb−1.isolate−1) compared to S. sclerotiorum (0.416 SNP.kb−1.isolate−1). To search for signatures of codon optimization in these populations, we determined the frequency of variants for each codon type. We compared frequency of codon variants to the number of cognate tRNA genomic copies, allowing for wobble pairing (Crick, 1966). Frequency of codon variants negatively correlated with the number of tRNA genomic copies in S. sclerotiorum (Pearson = −0.60, p = 4.6 10−07) but not in Z. tritici (Pearson = 0.06, p = 0.62) (Figure 4A, Figure 4—source data 1).

![Figure 4.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig4-v2.jpg)

**Figure 4.:** (A) Genome-wide frequencies of variant codons in local populations of the host generalist Sclerotinia sclerotiorum and the host specialist Zymoseptoria tritici, according to the number of genomic copies of cognate tRNAs. The number of cognate tRNAs for each codon type was determined using wobble rules for codon-anticodon pairing. Dotted lines show linear regression of the data (Z. tritici: Pearson ρ = 0.06; p=0.62; S. sclerotiorum ρ = −0.60; p=4.6 10−07). (B) Adjusted variant frequencies for intergenic nucleotide triplets, optimal and non-optimal codons. Synonymous and non-synonymous SNPs are shown separately. Differences between optimal and non-optimal codon rates were assessed by Welch’s t-test (***p<0.001). (C) Predicted evolution of genome-wide content in optimal codons in S. sclerotiorum and Z. tritici based on observed and random mutation patterns.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The accumulation of tRNA transcripts was determined by sequencing small RNAs of S. sclerotiorum grown in vitro and in planta. (A) Normalized read depth correlated exponentially with tRNA copy number for each tRNA species both in vitro and in planta. (B) A comparison of tRNA transcripts accumulation in vitro and in planta. Correlation of tRNA transcripts accumulation with codon usage (C) and tRNA adaptive value (D) calculated as described in dos Reis et al. (2004). The exponential regression of the data is shown as a dotted line. The Spearman rank correlation coefficient ρ and the p-value for Spearman’s test are given.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) IGS-based phylogeny of the S. sclerotiorum isolates re-sequenced in this work. (B) Frequency of SNPs according to codon position and SNP type. (C) SNPs in coding regions do not show significant bias toward enrichment in A or T nucleotides as shown by the rate of AT conversion. (D) Frequency of each substitution type among synonymous, non-synonymous and intergenic SNPs shows higher transition rate among synonymous substitutions. (E) Transition/transversion ratio per SNP type shows ~threefold increase in synonymous substitutions. (B–E) Error bars show the standard deviation of means for each isolate. Distribution of non-synonymous (F) and synonymous (G) SNPs among the five re-sequenced isolates.

To further document the molecular bases of codon optimization at the species level, we compared SNP patterns in optimal, intermediate, and non-optimal codons for each amino acid in S. sclerotiorum and Z. tritici populations. In the Z. tritici population, SNP frequencies were not significantly different between optimal and non-optimal codons. By contrast, synonymous SNP frequencies were on average ~1.7-fold lower in optimal codons than in non-optimal codons in S. sclerotiorum (Welch’s t-test p=1.3 10−03) (Figure 4B). These findings identify biased synonymous substitutions as a link between generalism and codon optimization. This analysis is independent of codon usage indices and shows that selection for average performances on multiple hosts is reflected in global trends of genome evolution.

### Natural selection drives codon optimization in generalist fungal parasites

Codon bias in a genome can be selectively neutral due to non-randomness in the mutation process. For instance, the identity of favored codons tracks the GC content of the genomes (Chen et al., 2004; Hershberg and Petrov, 2009). Although S. sclerotiorum genome is AT-rich (41.8% GC), synonymous SNPs showed no bias toward AT conversion, suggesting that synonymous SNPs deviated from neutral patterns (Figure 4—figure supplement 2). Furthermore, adjusted variant frequencies in S. sclerotiorum were similar in intergenic nucleotide triplets and in non-optimal codons but significantly lower in optimal codons (~1.53-fold lower, Welch’s t-test p= 1.0 10−11) (Figure 4B), suggesting that synonymous SNPs in optimal codons may be counter-selected in this species, providing evidence of purifying selection acting on optimal codons. To unambiguously demonstrate that observed SNP patterns lead to codon optimization in S. sclerotiorum and are unlikely to result from neutral processes, we simulated the evolution of optimal codon frequencies in S. sclerotiorum and Z. tritici genomes over 1000 generations (Figure 4C). In these simulations, we used either random SNP patterns, or the SNP patterns determined experimentally (Figure 4—source data 2). This demonstrated that the codon SNP patterns determined experimentally converge toward increased codon optimality in S. sclerotiorum genome, whereas SNP patterns observed in Z. tritici genome and random mutation patterns do not. Thus, patterns of evolution toward increased codon optimality were detected in S. sclerotiorum but not in Z. tritici populations, and deviate significantly from neutral evolution.

To estimate the likelihood that observed codon biases result from selective rather than neutral processes in other fungal genomes, we used permutation tests on the number of genomic tRNA copies to calculate probability distribution of S under no selection (dos Reis et al., 2004). A total of 14 species showed signatures of selection for codon optimization with a p<0.1, among which one was a specialist (M. roreri) and one had eight host genera (P. destructans). Twelve out of 15 (80%) generalist species showed selection for codon optimization with a p<0.1, confirming that adaptive translation is stronger in generalist species. We conclude that natural selection on protein translation efficiency or accuracy drives evolution toward codon optimization in generalist parasites through biased synonymous SNPs. These evolutionary patterns are consistent with an improvement of average performances on multiple hosts for generalist parasites.

### Codon optimization signatures associate with host colonization

To further support the link between codon optimization and the ability to colonize multiple hosts, we analyzed signatures of codon optimization in host-induced genes of 15 fungal parasite species from multiple families of the Ascomycetes and Basidiomycetes (Figure 5—source data 1) (Amselem et al., 2011; Duplessis et al., 2011a, 2011b; Gao et al., 2011; Morton et al., 2011; O'Connell et al., 2012; Xiao et al., 2012; Zhang et al., 2012; Hacquard et al., 2013; Bailey et al., 2014; Chen et al., 2014; Kellner et al., 2014; de Bekker et al., 2015; Bradshaw et al., 2016). We found that host-induced genes were enriched ~3.1-fold among the top 10% codon-adapted genes in generalist parasites but not in specialists. Overall, genes induced during host colonization distributed predominantly among genes with high codon adaptation indices in generalist but not in specialist parasites (Figure 5A, Figure 5—source data 2). Parasites use secreted proteins to facilitate infection of their hosts. We therefore analyzed codon optimization in secretome genes of 45 fungal species (Figure 5—source data 3). We found that secretome genes were enriched over 1.6-fold among the top 10% codon-adapted genes in generalist parasites but only ~1.2-fold in specialists and non-parasitic fungi. Overall, predicted secretome genes distributed predominantly among genes with high codon adaptation indices in generalist parasites but not in specialist and non parasitic fungi (Figure 5B). We calculated S in each genome for secreted and non-secreted protein genes (Figure 5C, Figure 5—source data 4). In our genome set, non-parasitic fungi had similar S for secreted and non-secreted proteins. The average S for secreted proteins (0.212) was slightly higher than for non-secreted proteins (0.137) in specialists (Student’s paired t-test p=0.054). In generalists, the average S for secreted proteins (0.661) was significantly higher than for non secreted proteins (0.558, Student’s paired t-test p=1.12 10−03). Increased codon optimization in generalists was not only clear for genes encoding secreted proteins and host-induced genes, but also across their entire genome (‘other genes’ in Figure 5C). To get a global overview of cellular functions enriched in codon optimized genes in generalists, we analyzed normalized tRNA adaptation indices for genes annotated with Gene Ontologies (GO) in generalist and specialist genomes (Figure 5D, Figure 5—source data 5). Together with secreted enzymes, GOs related to translation and central metabolism showed higher codon optimization in generalists than in specialists. Conversely, GOs related to transcription, transposable elements and phosphorelay signal transduction were better optimized in specialists than in generalists. These results suggest that high codon optimization is an adaptation to host colonization and particularly to the colonization of multiple hosts.

![Figure 5.](https://cdn.elifesciences.org/articles/22472/elife-22472-fig5-v2.jpg)

**Figure 5.:** (A) Genes induced during host infection are enriched among high tRNA adaptation index genes in generalist but not specialist parasite genomes. Error bars show standard error of the mean. (B) Genes encoding predicted secreted proteins are more strongly enriched among high tRNA adaptation index genes in generalist parasite genomes compared to specialist and non-parasitic fungi genomes. Error bars show standard error of the mean. (C) Degree of coadaptation of secreted protein genes and other genes to the genomic tRNA pool in non parasitic, specialist and generalist fungi (*** Student’s paired t-test p<0.002). (D) Distribution of tRNA adaptation indices according to gene functions in generalist and specialist fungal parasites. For each Gene Ontology (GO), the average normalized tRNA adaptation indices in all genes from generalist and specialist genomes are shown. Bubbles are sized according to the total number of genes, and colored according to the percentage of predicted secreted proteins when values for generalists and specialists differ by over 10%. Selected GOs are labeled.

## Discussion

Our study reveals that codon optimization through biased synonymous substitutions is a common feature in the evolution of generalist parasites and is associated with the colonization of multiple hosts. Because host colonization by generalist often requires diverse and relatively complex secreted proteins, these organisms are expected to require higher protein translation efficiency to compete with co-occuring specialist microbes. In agreement with this model, we found that natural selection for codon optimization correlates with host range in fungal parasites. We describe patterns of purifying selection acting on optimal codons in generalist parasites, providing a molecular basis for genome scale adaptation to the colonization of multiple hosts.

The increasing amount of genome sequences available for specialist fungal parasites revealed massive losses of enzymes associated with the ability to thrive and reproduce on living hosts (Schirawski et al., 2010; Spanu et al., 2010). Specialists rely largely on SSPs subverting host cell functions. Functional analyses have shown that SSPs from filamentous pathogens can function as effectors, facilitating the colonization of susceptible hosts while triggering resistance in some host genotypes by activating resistance (R) proteins (Dodds and Rathjen, 2010). In specialist species, the one-to-one relationship, either direct or indirect, between effectors and R proteins favors evolution through non-synonymous mutations, to increase effector diversity and escape R protein recognition (Raffaele and Kamoun, 2012). By contrast, pathogen populations exposed to weaker host selection, caused by quantitative resistance genes, or disruptive selection due to heterogeneity in the host population, are expected to evolve adapted genetic variants less rapidly (McDonald and Linde, 2002; Roux et al., 2014). Our analyses indeed support the view that selection driven by multiple hosts is associated with relatively low rates of evolution of protein variants but instead associates with the directional evolution of synonymous genetic variants. Translational selection may, nevertheless, be active in the genome of specialists but on limited gene sets only, resulting in a low signal in genome-scale analyses (dos Reis et al., 2004).

We noted a trend toward longer proteins encoded in the genome of generalist fungi, notably secreted proteins, consistent with the abundance of SSPs in specialists (Spanu et al., 2010) and previous comparative analyses (Kim et al., 2016). We associated longer proteomes in generalists with higher selection on codon optimization at the whole genome scale. The relative strength of translational selection on individual genes may, however, vary significantly within a given genome. Gene length increases in relation to evolutionary age, with conserved genes under purifying selection generally being longer and harboring higher frequency of optimal codons (Prat et al., 2009; Wolf et al., 2009). Neofunctionalization in duplicated genes has also been associated with increased gene length (He and Zhang, 2005). Duplications frequently underlie domain loss and gain in eukaryotic proteins, which is an important mechanism for the evolution of new functions (Buljan et al., 2010; Peisajovich et al., 2010). Natural selection may promote protein domains recombination to increase the versatility of fungal proteins functions, and thereby contribute to host range expansion.

The adaptive evolution of effectors that increase the colonization of one host species also increases the risk of detection in other host species by triggering their immune system. Furthermore, natural selection that maximizes parasite fitness on one particular host species might result in decreased fitness on an alternative host, leading to specialization (reduced host range) or host shift (Dong et al., 2014). The evolution of generalism has been associated to hybridization events (McMullan et al., 2015; Menardo et al., 2016), horizontal transfer of genetic elements (Ma et al., 2010; Hu et al., 2014), and an overall increase in the repertoire of protein-coding genes (Hu et al., 2014). This observation is consistent with the prominent role in pathogenic success of large repertoires of host-degrading enzymes encoded by the genome of generalist parasites (King et al., 2011; Zhao et al., 2013). Catalytic efficiency of these enzymes is crucial to perform in host environment. Although the catalytic activity of enzymes is typically modulated by adaptation of protein sequences, high reaction rates for efficient host colonization may be reached by modulating the amount of protein synthesized during colonization. However, an increase in proteins production may lead to a metabolic or structural burden of the translation machinery. For instance, the massive production of virulence factors by the generalist bacterial pathogen Ralstonia solanacearum reduces its metabolic versatility and thus its host colonization capacity (Perrier et al., 2016; Peyraud et al., 2016). Natural selection for the optimization of protein translation, through ribosome pausing time, translation error rates and co-translational protein folding, has been widely associated with codon usage biases (Drummond and Wilke, 2008; Tuller et al., 2010; Shah and Gilchrist, 2011). The adaptive evolution of the translation machinery described here is predicted to favor generalists’ performances in heterogeneous host populations, by reducing the cost of large and diverse sets of secreted enzymes production on proliferation. The mitigation of the tradeoff between cell proliferation and protein synthesis (Li et al., 2014) by codon optimization could explain how generalist lineages have maintained or gained the ability to produce diverse sets of secreted enzymes, allowing the colonization of genetically diverse hosts. Codon optimization may affect the expression of effectors and other virulence factors, modifying the degree of infection or enabling the colonization of new hosts opposing quantitative disease resistance mechanisms. These findings reveal that parasite host range variation is a prime example of an adaptive phenotype related to codon optimality and translational regulation.

## Materials and methods

### Simulation of codon optimization effect on protein biosynthesis

We designed a mathematical model of the cell translation machinery in order to undertake the analysis of the impact of codon optimization parameters on the cell physiology (Figure 1—source data 1). The model describes the variation of intracellular concentration, P(i), of three proteins sets (i): the free ribosomal proteins P(r), the proteins destined to be secreted P(s) and intracellular non-secreted proteins P(n), depending on their synthesis rate and the dilution rate due to cell growth. Crowding effect (Beg et al., 2007), that is the maximal number of proteins that a finite cell can contain, was modeled by adding a limitation function to the elongation rate which is asymptotic to the maximal proteins content. The ordinary differential equations were solved numerically using the COPASI software (RRID:SCR_014260) (Hoops et al., 2006) until a steady-state was reached. mRNA(i) concentrations were assumed to be stable with no dilution due to cell growth. The initiation constants between mRNA and ribosomes were set to a non-limiting value, similar for the three kinds of proteins sets (r, n and s). A stoichiometric constrain of 79 ribosomal proteins bound per mRNA(i) was added in the COPASI model. The initial parameters used for the different analysis are listed in Figure 1—source data 1. These parameters were set to be in the physiological range of a cell accordingly to data from Bremer and Dennis (2008). The concentrations of the biomolecules in the model are in mmol∙ml−1. The maximal growth rate was defined as the dilution rate (µ) above which the rate of the proteins biosynthesis is lower than the dilution rate, leading to the collapse of the proteins concentration. We considered situations in which 14.5% of total mRNAs corresponded to mRNAs for secreted proteins and 12% corresponded to mRNAs for ribosomal proteins, and analyzed the impact of varying codon decoding rate on protein production under our cellular model.

### Codon optimization across the kingdom fungi

Genome assemblies and CDS files for 45 fungal species were downloaded from the repositories given in Figure 2—source data 1. For every species, the repertoire of tRNA genes was determined using the tRNAscan-SE 1.21 server (RRID:SCR_010835) (Schattner et al., 2005) with the ‘Source’ parameter set as ‘Eukaryotic’ and ‘Search Mode’ set as ‘Default’. For 42 species, only predicted full length CDS were considered for codon optimization analysis. For this, CDS lacking a start and a stop codon were filtered out. For Puccinia graminis, Serpula lacrymans and Colletotrichum higginsianum, since >15% of CDS lacked a predicted stop codon in these genomes, we filtered out CDS lacking a start codon only. tRNA adaptation indices (tAIs) were calculated for a total of 569,744 genes using the get.tai function in R (dos Reis et al., 2004) with the ‘sking’ parameter set to ‘0’ (Eukaryote) for the get.ws function. The degree of codon optimization in each genome was determined using the get.s function in R (dos Reis et al., 2004). Confidence intervals were determined using the CI function from the package ‘psychometric’ in R. For each genome, the probability of selection acting on codon optimization was determined using the ts.test function in R (dos Reis et al., 2004) with sample size = 500 and n = 1000 and p values were adjusted using Bonferroni correction. The repertoire of ribosomal proteins was identified based on interproscan annotation or de novo gene annotation performed with Blast2GO version 3.3 (RRID:SCR_005828) (Conesa et al., 2005). For each genome, the CDS of full length ribosomal proteins were used to compute a codon usage table with the CUSP function in EMBOSS (RRID:SCR_008493) (Rice et al., 2000) to calculate codon adaptation indices (CAI) for every gene in the corresponding genome, using the CAI function in EMBOSS. The degree of codon optimization at the whole genome scale was determined using the get.s function in R with gene CAI or scnRCA instead of tAI. Host range was determined according to sources listed in Figure 2—source data 2. For most plant pathogens, the Systematic Mycology and Microbiology Laboratory Fungus-Host Database of the United States Department of Agriculture was used (Farr and Rossman, 2016). For Cryptococcus neoformans, Aspergillus fumigatus, Beauveria bassiana, and Metarhizium acridum, a list of infected Orders were retrieved. We collected the list of Genera recorded in these Orders through various sources (Figure 2—source data 2). The likelihood that a parasite can infect two host species decreases continuously with phylogenetic distance between the hosts (Gilbert and Webb, 2007). In their study, Gilbert and Webb reported that the proportion of hosts colonized was about ~20% at a 300 Mya phylogenetic distance, decreasing logarithmically. We considered that 8% of Genera in a given Order were likely to be host for the above-mentioned pathogens to reach a conservative estimate. Core orthologous genes were identified through a BlastP search against a database of 36 complete fungal proteomes, using the CEGMA set downloaded from http://korflab.ucdavis.edu as a query. Only orthologous groups containing a single hit in all fungal species were selected for further analysis. tRNA adaptation indices for each genome were median-normalized before analyzing their distribution in COGs. We used the TimeTree database (Hedges et al., 2015) to obtain ages for a maximum of nodes of the tree (calibration points). Then, we ultrametricized the tree using PATHd8 (Britton et al., 2007). We tested for a potential presence of a phylogenetic signal estimated by Blomberg's K, Pagel's λ and autocorrelogram with the phylosignal R-package (Keck et al., 2016). We calculated phylogenetic independent contrasts (Felsenstein, 1985) and verified the significance of trait correlations using the pic function from the ape package in R.

### Sequencing of S. sclerotiorum isolates

Isolates C014, P163, P314 and C104 were provided by Bruno Grezes-Besset (Biogemma, Mondonville, France) and were collected from infected rapeseed fields near Blois (France) in 2010. Isolate FrB5, collected from clover seed lot in Dijon (France) in 2010, was obtained from Vleugels et al. (2013). Isolate 1980 (ATCC18683) was collected in prior 1970 on bean pods near New York (Maxwell and Lumsden, 1970) and was provided by Martin Dickman (Texas A and M University, USA). For IGS phylogeny, Intergenic sequences (IGS) were retrieved on sequenced genomes with the Blast tool of CLC Genomics software (RRID:SCR_011853). The sequences were aligned with MAFFT v7 (RRID:SCR_011811) (Katoh and Standley, 2013), and the phylogenetic tree was build with PhyML 3 (Guindon et al., 2010) with SH-like approximate likelihood ratio test (aLRT) as support statistics. The tree was mid-point rooted using MEGA6 software (RRID:SCR_000667) (Tamura et al., 2013). Sclerotinia sclerotiorum isolates were grown in liquid potato dextrose medium (P6685 - Sigma) for 4 days at 24°C under shaking at 180 rpm. Cultures were filtered using vacuum and a fritted glass column protected with a doubled miracloth membrane and ground in liquid nitrogen. One gram of mycelium powder was used for DNA extraction using a DNA Maxi Kit (Quiagen) and following manufacturer’s instructions. DNA sequencing was outsourced to Fasteris SA (Switzerland) to produce Illumina paired-end reads (2 × 100 bp) using a HiSeq 2500 instrument. Paired-end reads for each S. sclerotiorum isolate were mapped to version 2 of the S. sclerotiorum 1980 reference strain genome (Derbyshire et al., 2017) using the mapping function of the CLC Genomics software. Variant call was performed on mapped reads with the Fixed Ploidy Variant Detection function of the CLC Genomics software. The resulting total variants for each strain were further filtered for homozygous single nucleotide variants.

### Analysis of codon polymorphisms in plant pathogen populations

SNPs in gene coding sequences were extracted and mapped to the corresponding codons using R scripts to calculate the percentage of polymorphic codons of each type. The number of tRNAs able to decode each codon type is given as a percentage of the genomic tRNA pool that was determined based on tRNA gene predictions obtained through tRNAscan-SE. Whenever isoacceptor codons had no cognate tRNA predicted, the number of tRNA copies was divided evenly among isoacceptor codons according to general codon-anticodon wobble rules as described in dos Reis et al. (2004). We considered that the 11 codons that did not have isodecoder tRNAs in Zymoseptoria tritici were decoded evenly by the four tRNA genes that had no accepting codons identified by tRNAscan-SE. Codons with the highest percentage of decoding tRNAs were considered as optimal. In cases where the highest percentage of decoding tRNA was shared among several synonymous codons, codons having the highest number of cognate tRNA copies in the genome or codons with the highest usage in the genome were optimal. Codons with the lowest percentage of decoding tRNAs were considered as non-optimal. In cases where the lowest percentage of decoding tRNA was shared among several synonymous codons, codons with the lowest usage in the genome were considered non-optimal. Other codons were considered as intermediate.

Variant frequencies (in % of codons) were calculated by counting the number of codons harboring a SNP divided by the total number of this codon type in the genome. These raw variant frequencies were used in simulation of the evolution of codon optimality. A random base change within a codon is more likely to result in a nonsynonymous or stop-gain mutation than a synonymous mutation, hence we expect the frequency of non-synonymous codon variants to be higher than the frequency of synonymous codon variants under neutral selection. Therefore, to compare synonymous and non-synonymous variant frequencies, we adjusted non-synonymous variant frequencies dividing them by their likelihood to occur if changes were random. Variant frequencies in intergenic nucleotide triplets were used as an estimate for neutral patterns of evolution. For this, we extracted for each intergenic SNP the corresponding triplets. Variant frequencies (% of nucleotide triplets) were calculated by counting the number of triplets of a given type harboring a SNP divided by the total number of this triplet type in intergenic regions of the genome, determined using the COMPSEQ function in EMBOSS. Frequencies of variants in intergenic triplets were adjusted to compare to synonymous and non-synonymous variant frequencies. For this, we use as a correction factor the ratio between the adjusted total codon variant rate (synonymous variant rate + adjusted non-synonymous variant rate) over the unadjusted total codon variant rate (synonymous variant rate + non-synonymous variant rate). SNP frequencies in genes (in Kbp−1) were calculated counting the number of SNPs per genes and divided by the length of gene coding sequence in Kbp.

### Determination of tRNA genes expression

Small RNAs were obtained from samples of Arabidopsis thaliana Col-0 ecotype plants infected by S. sclerotiotum strain 1980 and samples of S. Sclerotiorum strain 1980 grown in Potato Dextrose Broth as previously described. Small RNA were prepared using the NucleoSpin miRNA kit (Macherey-Nagel) following instructions of the manufacturer. Small RNAs sequencing was outsourced to Fasteris SA (Switzerland) to produce Illumina reads using a HiSeq 2500 instrument (small RNA libraries with expected insert size from 18 to 30 bp). Reads were imported into CLC Genomics Workbench 8.5 (QUIAGEN), and sequences were mapped on version 2 of the S. sclerotiorum strain 1980 genome (Derbyshire et al., 2017). Read counts at predicted tRNA loci were obtained using the Small RNA Analysis toolkit of the CLC Genomics Workbench 8.5 software. Only perfect matches to the S. sclerotiorum tRNA genomic loci on the correct strand were accepted, and inserts less than 15pb were discarded. Reads collected in planta or in vitro and aligned to the different copies of a given tRNA type in the genome were summed up and compared to tRNA gene copy numbers, codon usage or tRNA adaptive values.

### Simulations of the evolution of codon optimality

Codons were classified as optimal, intermediate and non-optimal as described previously, unadjusted variant frequencies were used. The initial state in simulations corresponded to codon usage measured in S. sclerotiorum and Z. tritici reference genomes. To simulate the long-term evolution of codon optimality in S. sclerotiorum and Z. tritici, we developed two python scripts. The ‘observed’ simulator uses the frequencies of all 64x64 = 4096 possible codon substitutions measured in S. sclerotiorum and Z. tritici natural populations, kept constant over the simulation. At each evolutionary step, the frequencies of the 64 codons in each genome are mutated according to the codon substitution frequencies table. The total proportion of optimal, intermediate and non-optimal codons in each genome is computed after all measured codon substitutions have been accounted for (designated as one ‘generation’). To test if the observed long-term evolution of codon optimality deviated significantly from random mutation patterns, a ‘random’ simulator was implemented. In these simulations, bulk frequencies of triplets toward synonymous and not synonymous mutations were kept constant, whereas the outcome of mutations was determined randomly at each iteration. The number of mutations at each generation also varied randomly in order to obtain an uneven distribution. Simulations were repeated until an asymptotic behavior was apparent. The Python source code for these two simulators is provided in Figure 4—source code 1.

### Codon optimization and genes function

To normalize tAIs across multiple genomes, tAI values were ordered in ascending order in each genome, and their rank given as a percentage (0 for lowest rank corresponding to the lowest tAI in a given genome up to 1 for the highest rank corresponding to the highest tAI in this genome). The source of data and pipelines used to identify genes significantly induced are listed in (Figure 5—source data 1). The predicted secreted protein genes were determined using SignalP 4.0 (Petersen et al., 2011) with default parameters. For each genome, genes were classified into secreted protein genes (signal peptide identified by SignalP 4.0) and non-secreted protein genes (all other genes). The degree of codon optimization in these two gene subsets were computed for each genome using the get.s function in R (dos Reis et al., 2004). The average normalized tAI for all genes annotated with a given Gene Ontology was computed for generalist and specialist genomes. GO mapping was retrieved from the repositories given in Figure 2—source data 1 or performed de novo with Blast2GO software. Only GOs associated with 200 genes or more were analyzed.
