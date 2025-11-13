# Viral genome sequence datasets display pervasive evidence of strand-specific substitution biases that are best described using non-reversible nucleotide substitution models

## Authors

- Rita Sianga-Mete<sup>1</sup> ([ORCID: 0000-0001-6626-4007](https://orcid.org/0000-0001-6626-4007)) †
- Penelope Hartnady<sup>1</sup>
- Wimbai Caroline Mandikumba<sup>1</sup>
- Kayleigh Rutherford<sup>1</sup>
- Christopher Brian Currin<sup>2</sup> ([ORCID: 0000-0002-4809-5059](https://orcid.org/0000-0002-4809-5059))
- Florence Phelanyane<sup>3</sup>
- Sabina Stefan<sup>4</sup>
- Steven Weaver<sup>5</sup>
- Sergei L Kosakovsky Pond<sup>5</sup> ([ORCID: 0000-0003-4817-4029](https://orcid.org/0000-0003-4817-4029))
- Darren P Martin<sup>6</sup> ([ORCID: 0000-0002-8785-0870](https://orcid.org/0000-0002-8785-0870))

### Affiliations

1. Division of Computational Biology, Institute of Infectious Diseases and Molecular Medicine, Department of Integrative Biomedical Sciences, Faculty of Health Sciences, University of Cape Town Rondebosch South Africa ([ROR:03p74gp79](https://ror.org/03p74gp79))
2. Department of Human Biology, Faculty of Health Sciences, University of Cape Town Rondebosch South Africa ([ROR:03p74gp79](https://ror.org/03p74gp79))
3. Centre for Infectious Disease and Epidemiology Research, School of Public Health and Family Medicine, University of Cape Town Rondebosch South Africa ([ROR:03p74gp79](https://ror.org/03p74gp79))
4. Centre for Biomedical Engineering, School of Engineering, Brown University Providence United States ([ROR:05gq02987](https://ror.org/05gq02987))
5. Institute for Genomics and Evolutionary Medicine, Department of Biology, Temple University Philadelphia United States ([ROR:00kx1jb78](https://ror.org/00kx1jb78))
6. Wellcome Center for Infectious Diseases Research in Africa, Institute of Infectious Disease and Molecular Medicine and Department of Medicine, University of Cape Town Rondebosch South Africa ([ROR:03p74gp79](https://ror.org/03p74gp79))

† Corresponding author

## Abstract

Most phylogenetic trees are inferred using time-reversible evolutionary models that assume that the relative rates of substitution for any given pair of nucleotides are the same regardless of the direction of the substitutions. However, there is no reason to assume that the underlying biochemical mutational processes that cause substitutions are similarly symmetrical. We consider two non-reversible nucleotide substitution models: (1) a 6-rate non-reversible model (NREV6) that is applicable to analysing mutational processes in double-stranded genomes, in that complementary substitutions occur at identical rates and (2) a 12-rate non-reversible model (NREV12) that is applicable to analysing mutational processes in single-stranded (ss) genomes, in that all substitution types are free to occur at different rates. Using likelihood ratio and Akaike information criterion-based model tests, we show that, surprisingly, NREV12 provided a significantly better fit than the general time reversible (GTR) and NREV6 models to 21/31 dsRNA and 20/30 dsDNA datasets. As expected, however, NREV12 provided a significantly better fit to 24/33 ssDNA and 40/47 ssRNA datasets. We tested how non-reversibility impacts the accuracy with which phylogenetic trees are inferred. As simulated degrees of non-reversibility (DNRs) increased, the tree topology inferences using both NREV12 and GTR became more accurate, whereas inferred tree branch lengths became less accurate. We conclude that while non-reversible models should be helpful in the analysis of mutational processes in most virus species, there is no pressing need to use these models for routine phylogenetic inference.

## Introduction

Modelling the nucleotide substitution processes that underlie the diversification of virus genome sequences lies at the heart of many viral evolutionary analyses. The most widely used nucleotide substitution models belong to the general time reversible (GTR) family (Tavaré, 1986) and assume that the Markov process of evolution is time-reversible (Hoff et al., 2016; Liò and Goldman, 1998; Tavaré, 1986).

The GTR model is defined by its instantaneous rate matrix $Q_{ij}$ (Equation 1), where $Q_{ij}$ defines the instantaneous rate of change from nucleotide $i\in{A,C,G,T}$ to nucleotide $j$; subject to the detailed balance condition: $q_{ji}\pi_{i}=q_{ji}\pi_{j}$, with rates q and equilibrium frequencies π (Squartini and Arndt, 2008; Posada, 2003). The instantaneous rate matrix of the GTR model includes six rate parameters (a, b, c, d, e, and f). Because only products of substitution rates and evolutionary times can be estimated, one of the rate parameters is set to 1 (e.g. b), or the entire matrix is normalised to yield one expected substitution per unit time.

$$
Q={q_{ij}}=(−a\pi_{C}b\pi_{G}d\pi_{T}a\pi_{A}−c\pi_{G}e\pi_{T}b\pi_{A}c\pi_{C}−f\pi_{T}d\pi_{A}e\pi_{C}f\pi_{G}−)
$$

The rate matrix in Equation 1 is symmetrical, e.g., the relative rate at which A changes to G is the same as the relative rate at which G changes to A.

Time-reversible nucleotide substitution models such as GTR form the basis of almost all nucleotide sequence-focused evolutionary analyses (including those involving eukaryotes, prokaryotes, and viruses) (Lefort et al., 2017; Posada and Crandall, 2001a; Posada and Crandall, 2001b; Minin et al., 2003).

The reliability of a phylogenetic tree constructed using a particular nucleotide sequence dataset should be maximised when the evolutionary models used to construct the tree accurately reflect the important aspects of the evolutionary process (Buckley and Cunningham, 2002; Ripplinger and Sullivan, 2008; Hoff et al., 2016). The suitability of different models for describing the evolution of DNA or RNA sequences is, therefore, expected to depend to some degree on the biological and environmental contexts of the sequences being analysed.

Mutations in viral genomes arise due to diverse biotic (such as replication enzyme infidelities, RNA/DNA editing enzymes) and abiotic (such as ionising radiation, inorganic oxidisers, and chemical mutagens) factors (Sanjuán and Domingo-Calap, 2016). Mutagenic chemical reactions or types of radiation that, for example, cause G to A or C to U mutations in DNA or RNA are not the same as those that cause A to G or U to C mutations (Cheng et al., 1992;⁠ Nguyen et al., 1992; Chelico et al., 2006; Sharma et al., 2016). It should not be expected, therefore, that the relative rates of G to A substitution will equal the relative rates of A to G substitution. Instead, in evolving double-stranded (ds) DNA and dsRNA molecules where both strands of the genome are in existence for similar amounts of time, both G to A and C to T substitutions should occur at relatively similar rates. Therefore, for nucleotide sequence datasets derived from any organisms with dsDNA or dsRNA genomes, a non-reversible nucleotide substitution model with a different relative substitution rate category for each of the six possible pairs of complementary nucleotide substitutions (e.g. NREV6 in Equation 2), with $q_{AC}=q_{TG},q_{AG}=q_{TC},q_{AT}=q_{TA},q_{CG}=q_{GC},q_{CT}=q_{GA},q_{GT}=q_{CA}$, might plausibly provide a better description of mutational processes than GTR (Baele et al., 2010; Wickner, 1993).

$$
Q={q_{ij}}=(−a\pi_{C}b\pi_{G}c\pi_{T}f\pi_{A}−d\pi_{G}e\pi_{T}e\pi_{A}d\pi_{C}−f\pi_{T}c\pi_{A}b\pi_{C}a\pi_{G}−)
$$

In the case of ssRNA viruses, ssDNA viruses, retroviruses, and dsRNA/dsDNA viruses where the two complementary genome strands do not exist for equal amounts of time (Yu et al., 2004), a model where all 12 different substitutions occur at different rates might be best. Specifically, with ssRNA viruses, ssDNA viruses, and retroviruses, only one of the genome strands (called the virion strand) is packaged into viral particles for transmission and, in many dsRNA viruses, the genome strand that is translated into proteins (called the + strand) exists for longer during the life cycle than does the complementary (or –) strand (Bruslind, 2020; Onwubiko et al., 2020). In all these viruses, some degree of strand-specific substitution bias is expected to occur (van der Walt et al., 2008; Polak and Arndt, 2008) such that NREV6 might be anticipated to provide a poorer description of mutational processes than a model such as NREV12 (Equation 3), where each of the 12 different types of substitution has a separate rate (Baele et al., 2010).

$$
Q={q_{ij}}=(−a\pi_{A}b\pi_{A}c\pi_{A}g\pi_{C}−d\pi_{C}e\pi_{C}h\pi_{G}i\pi_{G}−f\pi_{G}j\pi_{T}k\pi_{T}l\pi_{T}−)
$$

Because non-reversible models consider the directionality of evolution, they could, in some cases, be used to identify root nodes of phylogenetic trees (Yap and Speed, 2005; Boussau and Gouy, 2006). It is, however, unclear whether non-reversible models might, in certain situations at least, perform better than reversible models in the context of phylogenetic inference. Although it is possible to use non-reversible nucleotide substitution models such as NREV6 and NREV12 during maximum likelihood-based phylogenetic inference with computer programs such as IQ-TREE (Nguyen et al., 2015), these models are not routinely used for phylogenetic inference. This is in part because non-reversible models render several commonly used algorithmic techniques for efficient likelihood computation inapplicable, making inference slower. It is also in part because it remains undetermined whether, under conditions where strand-specific substitution biases are evident, non-reversible models consistently yield substantially more accurate phylogenetic trees than reversible models.

Here, we present evidence that strand-specific nucleotide substitution biases are common within virus genomic sequence datasets such that NREV12 generally provides a significantly better fit than both GTR and NREV6 for such datasets. We then use simulations to demonstrate that whereas strand-specific nucleotide substitution biases reduce the accuracy of phylogenetic inference under both GTR and NREV12, when these biases become extreme, use of NREV12 can yield significantly more accurate phylogenetic trees than GTR.

## Results and discussion

### Non-reversible nucleotide substitution models generally provide a better fit than reversible models to virus sequence datasets

We tested for evidence of non-reversibility of the nucleotide substitution process in 141 virus sequence datasets (33 ssDNA virus datasets, 30 dsDNA virus datasets, 31 dsRNA virus datasets, and 47 ssRNA virus datasets), all consisting of either full genome sequences (for unsegmented viruses) or complete genome component sequences (for viruses with segmented genomes). Specifically, for each dataset, we compared the goodness-of-fit of the GTR+G, NREV6+G, and NREV12+G models (where G represents gamma-distributed nucleotide substitution rates among sites; Yang, 1994).

Given that dsDNA viruses such as adenoviruses, papillomaviruses, and herpesviruses have both their DNA strands in existence for similar amounts of time before DNA-dependent-DNA polymerase enzymes copy both their + and – DNA strands during replication (Hanson, 2009), we had anticipated that the best fitting substitution model for sequence datasets of these viruses would be NREV6. Using weighted small sample corrected Akaike information criterion (AIC-c) scores to reveal trends of model support (Figure 1), it is surprising that NREV12 was overall the best-supported model (illustrated by the redder hues around the top corner of the dsDNA plot in Figure 2). Out of the 30 dsDNA datasets considered, we found that NREV6 provided the best fit to five datasets (HPV18, HPV45, HPV16, BPV, and SV40) and GTR provided the best fit to five (Alphapapillomavirus 6, JC polyomavirus, DPV, RTBV, and DBAV). NREV12 was the best fitting model for the remaining 20 datasets (Table 1). Further, likelihood ratio tests (LRTs) revealed strong overall support for NREV12, with this model providing a significantly better fit (p<0.05) than NREV6 for 25/30 of the dsDNA datasets and a significantly better fit than GTR for 24/30 of the datasets.

![Figure 1.](https://cdn.elifesciences.org/articles/87361/elife-87361-fig1-v1.jpg)

**Figure 1.:** These plots were produced using the Akaike weights function with an overlaid density function (implemented in the qpcR package of RStudio; Ritz and Spiess, 2008) to indicate point densities. Each model is represented by a corner of the triangles, and each circle represents the relative fit of each of the three models to a single nucleotide sequence dataset. The sides of the triangle represent model support axes ranging from 0% to 100%, with the position of a circle in relation to each of the sides of the triangle indicating the probability of models best describing the nucleotide sequence dataset that is represented by that point. Red colours represent a very high density of nucleotide sequence datasets that favour a particular model, blue colours indicate a lower, but still substantial, density of datasets that favour a particular model.

![Figure 2.](https://cdn.elifesciences.org/articles/87361/elife-87361-fig2-v1.jpg)

**Figure 2.:** ‘ns’ above a pair of box and whisker plots indicates a paired t-test adjusted p-value of ≥0.05 and ‘*’ indicates a paired t-test adjusted p-value of <0.05.

**Table 1.**
 Akaike information criterion (AIC) scores and likelihood ratio test (LRT) results for double-stranded DNA virus datasets.The lowest small sample corrected AIC (AIC-c) scores indicating the best fitting models are in bold.


<table>
  <thead>
    <tr>
      <th>Virus family</th>
      <th>Dataset</th>
      <th>AIC score GTR</th>
      <th>AIC score NREV-6</th>
      <th>AIC score NREV-12</th>
      <th>p-Value GTR vs NREV-12</th>
      <th>p-Value NREV-6 vs NREV-12</th>
      <th>DNR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10">Papillomaviridae</td>
      <td>APPV 6</td>
      <td>35099.5</td>
      <td>35108.0</td>
      <td>35102.2</td>
      <td>&gt;0.05</td>
      <td>0.007</td>
      <td>0.089</td>
    </tr>
    <tr>
      <td>HPV18_2</td>
      <td>25202.9</td>
      <td>25174.6</td>
      <td>25179.2</td>
      <td>&lt;0.001</td>
      <td>&gt;0.05</td>
      <td>0.323</td>
    </tr>
    <tr>
      <td>HPV45_2</td>
      <td>23600.6</td>
      <td>23599.0</td>
      <td>23602.9</td>
      <td>&gt;0.05</td>
      <td>&gt;0.05</td>
      <td>0.285</td>
    </tr>
    <tr>
      <td>HPV16_2</td>
      <td>29734.0</td>
      <td>29664.5</td>
      <td>29665.4</td>
      <td>&lt;0.001</td>
      <td>&gt;0.05</td>
      <td>0.371</td>
    </tr>
    <tr>
      <td>HPV31</td>
      <td>24681.4</td>
      <td>24677.3</td>
      <td>24672.8</td>
      <td>0.002</td>
      <td>0.01</td>
      <td>0.165</td>
    </tr>
    <tr>
      <td>HPV6_1</td>
      <td>31199.1</td>
      <td>31150.0</td>
      <td>31141.2</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.451</td>
    </tr>
    <tr>
      <td>LPV</td>
      <td>67165.7</td>
      <td>67188.1</td>
      <td>67145.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.42</td>
    </tr>
    <tr>
      <td>DPV</td>
      <td>69829.7</td>
      <td>69889.2</td>
      <td>69835.1</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.056</td>
    </tr>
    <tr>
      <td>XPV</td>
      <td>95455.6</td>
      <td>95617.1</td>
      <td>95452.2</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.072</td>
    </tr>
    <tr>
      <td>BATV</td>
      <td>134821</td>
      <td>134511</td>
      <td>133322</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.402</td>
    </tr>
    <tr>
      <td rowspan="4">Polyomaviridae</td>
      <td>JC_2</td>
      <td>51806.7</td>
      <td>51819.6</td>
      <td>51812.0</td>
      <td>&gt;0.05</td>
      <td>0.003</td>
      <td>0.089</td>
    </tr>
    <tr>
      <td>BK_2</td>
      <td>21472.6</td>
      <td>21472.7</td>
      <td>21471.1</td>
      <td>0.03</td>
      <td>0.03</td>
      <td>0.244</td>
    </tr>
    <tr>
      <td>SV40</td>
      <td>16859.8</td>
      <td>16858.0</td>
      <td>16858.4</td>
      <td>0.037</td>
      <td>&gt;0.05</td>
      <td>0.567</td>
    </tr>
    <tr>
      <td>BPV</td>
      <td>148614.9</td>
      <td>148573.8</td>
      <td>148585.2</td>
      <td>&lt;0.001</td>
      <td>&gt;0.05</td>
      <td>0.064</td>
    </tr>
    <tr>
      <td rowspan="6">Caulimoviridae</td>
      <td>CMV</td>
      <td>124083.9</td>
      <td>124221.0</td>
      <td>123888.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.351</td>
    </tr>
    <tr>
      <td>CSSV</td>
      <td>145327.0</td>
      <td>146575</td>
      <td>145202</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.158</td>
    </tr>
    <tr>
      <td>SVBV</td>
      <td>138575</td>
      <td>138488.1</td>
      <td>138464.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.174</td>
    </tr>
    <tr>
      <td>DBAV</td>
      <td>46495.5</td>
      <td>46514.1</td>
      <td>46502.0</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.0335</td>
    </tr>
    <tr>
      <td>RTBV</td>
      <td>54987.9</td>
      <td>55350.1</td>
      <td>54991</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.082</td>
    </tr>
    <tr>
      <td>BDV</td>
      <td>376325.2</td>
      <td>376647.6</td>
      <td>376029.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.140</td>
    </tr>
    <tr>
      <td>Siphoviridae</td>
      <td>CLV</td>
      <td>237362.3</td>
      <td>237351.8</td>
      <td>237348.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.01</td>
      <td>0.070</td>
    </tr>
    <tr>
      <td>Tectiviridae</td>
      <td>TTIV</td>
      <td>913864.9</td>
      <td>913915.4</td>
      <td>913773.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.279</td>
    </tr>
    <tr>
      <td rowspan="8">Adenoviridae</td>
      <td>FAV_C</td>
      <td>3074086.7</td>
      <td>3074207.5</td>
      <td>3073739.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.169</td>
    </tr>
    <tr>
      <td>FAV_E</td>
      <td>103482.3</td>
      <td>103222.7</td>
      <td>102636.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.357</td>
    </tr>
    <tr>
      <td>FAV_D</td>
      <td>2326925.6</td>
      <td>2325719.4</td>
      <td>2324784.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.551</td>
    </tr>
    <tr>
      <td>FAV_A</td>
      <td>705328.5</td>
      <td>705436.5</td>
      <td>705197.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.645</td>
    </tr>
    <tr>
      <td>HMAV_B</td>
      <td>103796.7</td>
      <td>103937.44</td>
      <td>103753.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>10.890</td>
    </tr>
    <tr>
      <td>HMAV_D</td>
      <td>1748635.2</td>
      <td>1749769</td>
      <td>1748119.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.646</td>
    </tr>
    <tr>
      <td>HMAV_C</td>
      <td>2851144.5</td>
      <td>2851357.1</td>
      <td>2851133</td>
      <td>0.006</td>
      <td>&lt;0.001</td>
      <td>0.0225</td>
    </tr>
    <tr>
      <td>HMAV_E</td>
      <td>1915044.8</td>
      <td>1915065.3</td>
      <td>1914998</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.049</td>
    </tr>
  </tbody>
</table>

As NREV6 was not the best fitting model for most of the dsDNA virus datasets, we infer that, in most dsDNA virus species, strand-specific substitution biases are not ignorable. Further, the datasets where NREV6 was not the best fit are from species in families containing other species where NREV6 was the best fit, indicating that such strand-specific substitution biases are unlikely to be a consequence of some broadly conserved feature of viral life cycles in these families (such as ssDNA replicative intermediates). It is instead plausible that these differences may relate to:

Similarly, and equally surprising, we found that NREV12 was overall the best supported model for dsRNA viruses (illustrated by the redder hues around the top corner of the dsRNA plot in Figure 1).

NREV6 fit only 2 of the 31 dsRNA datasets better than both NREV12 and GTR (Human rotavirus A set H and Fiji virus). NREV12 was found to be the best fitting model for 21/31 datasets and GTR was the best fitting of 8/31 (Table 2). In all three Birnaviridae family datasets (which contain virus species with two genome segments) and in 17/22 of Reoviridae family datasets (which contain virus species with 10–12 genome segments), the NREV12 model provided the best fit. Based on the LRTs, strong overall support for NREV12 was found, with this model providing a significantly better fit (p<0.05) in 27/31 dsRNA virus datasets relative to NREV6 and 23/31 datasets relative to GTR.

**Table 2.**
 Akaike information criterion (AIC) scores and likelihood ratio test (LRT) results for double-stranded RNA datasets.The lowest small sample corrected AIC (AIC-c) scores indicating the best fitting models are in bold.


<table>
  <thead>
    <tr>
      <th>Virus family</th>
      <th>Dataset</th>
      <th>AIC score GTR</th>
      <th>AIC score NREV-6</th>
      <th>AIC score NREV-12</th>
      <th>GTR vs NREV-12</th>
      <th>NREV-6 vs NREV-12</th>
      <th>DNR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Birnaviridae</td>
      <td>AQBV</td>
      <td>31754.9</td>
      <td>31853.3</td>
      <td>31721.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.219</td>
    </tr>
    <tr>
      <td>GBV_A</td>
      <td>47176.9</td>
      <td>47347.2</td>
      <td>47154.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.142</td>
    </tr>
    <tr>
      <td>IPNV</td>
      <td>79186.2</td>
      <td>79221.9</td>
      <td>79182.4</td>
      <td>0.0145</td>
      <td>&lt;0.001</td>
      <td>0.162</td>
    </tr>
    <tr>
      <td>GBV_B</td>
      <td>39313.7</td>
      <td>39062.8</td>
      <td>38938.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.201</td>
    </tr>
    <tr>
      <td rowspan="22">Reoviridae</td>
      <td>BTV_A</td>
      <td>34803.5</td>
      <td>34895.1</td>
      <td>34801.3</td>
      <td>0.03</td>
      <td>&lt;0.001</td>
      <td>0.042</td>
    </tr>
    <tr>
      <td>BTV_B</td>
      <td>48849.9</td>
      <td>48893.</td>
      <td>48837.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.043</td>
    </tr>
    <tr>
      <td>BTV_C</td>
      <td>28350.9</td>
      <td>28386.5</td>
      <td>28350.8</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.061</td>
    </tr>
    <tr>
      <td>BTV_D</td>
      <td>24969.1</td>
      <td>24947.3</td>
      <td>24894.0</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.191</td>
    </tr>
    <tr>
      <td>BTV_F</td>
      <td>20622.7</td>
      <td>20708.5</td>
      <td>20610.2</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.067</td>
    </tr>
    <tr>
      <td>BTV_G</td>
      <td>63349.9</td>
      <td>63485.0</td>
      <td>63345.9</td>
      <td>0.00426</td>
      <td>&lt;0.001</td>
      <td>0.040</td>
    </tr>
    <tr>
      <td>BTV_H</td>
      <td>20596.7</td>
      <td>20685.5</td>
      <td>20586.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.118</td>
    </tr>
    <tr>
      <td>BTV_I</td>
      <td>17592.7</td>
      <td>17622.5</td>
      <td>17588.8</td>
      <td>0.01</td>
      <td>&lt;0.001</td>
      <td>0.095</td>
    </tr>
    <tr>
      <td>BRVA_C</td>
      <td>41206.7</td>
      <td>41187.4</td>
      <td>41137.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.128</td>
    </tr>
    <tr>
      <td>HRVA_A</td>
      <td>17030.5</td>
      <td>17043.2</td>
      <td>17035.5</td>
      <td>&gt;0.05</td>
      <td>0.003</td>
      <td>0.036</td>
    </tr>
    <tr>
      <td>HRVA_B</td>
      <td>8275.1</td>
      <td>8280.3</td>
      <td>8281.7</td>
      <td>&gt;0.05</td>
      <td>&gt;0.05</td>
      <td>0.087</td>
    </tr>
    <tr>
      <td>HRVA_C</td>
      <td>12815.1</td>
      <td>12842.6</td>
      <td>12807.6</td>
      <td>0.003</td>
      <td>&lt;0.001</td>
      <td>0.132</td>
    </tr>
    <tr>
      <td>HRVA_D2</td>
      <td>8036.8</td>
      <td>8041.0</td>
      <td>8043.7</td>
      <td>&gt;0.05</td>
      <td>&gt;0.05</td>
      <td>0.057</td>
    </tr>
    <tr>
      <td>HRVA_E</td>
      <td>7045.9</td>
      <td>7056.1</td>
      <td>7053.3</td>
      <td>&gt;0.05</td>
      <td>0.02</td>
      <td>0.102</td>
    </tr>
    <tr>
      <td>HRVA_F</td>
      <td>7046.0</td>
      <td>7056.7</td>
      <td>7053.4</td>
      <td>&gt;0.05</td>
      <td>0.02</td>
      <td>0.0710</td>
    </tr>
    <tr>
      <td>HRVA_G</td>
      <td>18424.2</td>
      <td>18434.0</td>
      <td>18425.1</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.123</td>
    </tr>
    <tr>
      <td>HRVA_H</td>
      <td>20431.4</td>
      <td>20413.87</td>
      <td>20420.5.6</td>
      <td>0.002</td>
      <td>&gt;0.05</td>
      <td>0.163</td>
    </tr>
    <tr>
      <td>PRVA_A</td>
      <td>28540.7</td>
      <td>28441.9</td>
      <td>28398.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.204</td>
    </tr>
    <tr>
      <td>PRVA_B</td>
      <td>14757.7</td>
      <td>14775.5</td>
      <td>14732.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.351</td>
    </tr>
    <tr>
      <td>HRVC_A</td>
      <td>6713.2</td>
      <td>6718.2</td>
      <td>6712.3</td>
      <td>0.045</td>
      <td>0.007</td>
      <td>0.124</td>
    </tr>
    <tr>
      <td>PTOV</td>
      <td>202011.3</td>
      <td>202106.5</td>
      <td>201878.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.039</td>
    </tr>
    <tr>
      <td>FJV_B</td>
      <td>9274.1</td>
      <td>9250.0</td>
      <td>9250.9</td>
      <td>&lt;0.001</td>
      <td>&gt;0.05</td>
      <td>0.194</td>
    </tr>
    <tr>
      <td rowspan="2">Endornaviridae</td>
      <td>EDV</td>
      <td>1771992.8</td>
      <td>1772689.1</td>
      <td>1771950.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.121</td>
    </tr>
    <tr>
      <td>BPAV</td>
      <td>70386.5</td>
      <td>70540.2</td>
      <td>70390.7</td>
      <td>&gt;0.05</td>
      <td>0.00</td>
      <td>0.047</td>
    </tr>
    <tr>
      <td rowspan="2">Totiviridae</td>
      <td>TTV</td>
      <td>617302.6</td>
      <td>617462.6</td>
      <td>617172.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.052</td>
    </tr>
    <tr>
      <td>GDV</td>
      <td>80435.8</td>
      <td>80396.5</td>
      <td>80387.7</td>
      <td>&lt;0.001</td>
      <td>0.002</td>
      <td>0.109</td>
    </tr>
    <tr>
      <td>Hypoviridae</td>
      <td>HPV</td>
      <td>66859.8</td>
      <td>66899.8</td>
      <td>66857.8</td>
      <td>0.03</td>
      <td>&lt;0.001</td>
      <td>0.057</td>
    </tr>
  </tbody>
</table>

We anticipated that NREV12 might fit many of these dsRNA datasets better than NREV6 simply because, during their infection cycles, the coding +strand of dsRNA viruses (the one from which protein translation occurs) tends to exist for longer periods within an infected cell than the non-coding –strand. Specifically, there are two main steps during double-stranded RNA virus replication (Wickner, 1993). Firstly, synthesis of the viral +strands from a dsRNA template occurs in the cytoplasm within viral particles. These +strands exist within the cell for prolonged periods in the absence of complementary –strands and are used as templates for translation of viral proteins. In the second step, the +strands remaining after translation act as templates for –strand synthesis, resulting in the formation of new dsRNA molecules. The +strands of dsRNA viruses are therefore likely more impacted by mutational processes, which in turn could explain the pervasive strand-specific substitution biases seen in this group of viruses.

For the ssRNA and ssDNA viruses where one genome strand exists during the virus life cycle for far longer periods of time than the other such that complementary substitutions would not be expected to occur at similar rates, we anticipated that NREV12 should provide a better fit than both NREV6 and GTR. Indeed, for ssRNA viruses, NREV12 was a better fit than NREV6 and GTR for 40/47 of the ssRNA datasets and 24/33 of the ssDNA virus datasets (Figure 1). Of the nine ssDNA virus datasets where NREV12 was not the best fitting model, GTR fit 7/9 better and NREV6 fit 2/9 better (Table 3). Of the seven ssRNA datasets where NREV12 was not the best fitting model, GTR fit 6/7 better and NREV6 fit 1/7 better.

**Table 3.**
 Small sample corrected Akaike information criterion (AIC-c) scores and likelihood ratio test (LRT) results for single-stranded DNA datasets.The lowest AIC-c scores indicating the best fitting models are in bold.


<table>
  <thead>
    <tr>
      <th>Virus family</th>
      <th>Dataset</th>
      <th>AIC score GTR</th>
      <th>AIC score NREV-6</th>
      <th>AIC score NREV-12</th>
      <th>p-Value GTR vs NREV-12</th>
      <th>p-Value NREV-6 vs NREV-12</th>
      <th>DNR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">Nanoviridae</td>
      <td>BBTV M</td>
      <td>15044.3</td>
      <td>15207.9</td>
      <td>14984.4</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.662</td>
    </tr>
    <tr>
      <td>BBTV N</td>
      <td>10605.6</td>
      <td>10686.2</td>
      <td>10595.2</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.533</td>
    </tr>
    <tr>
      <td>BBTV R</td>
      <td>18484.5</td>
      <td>18544</td>
      <td>18480.8</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.609</td>
    </tr>
    <tr>
      <td>BBTV S</td>
      <td>12718.9</td>
      <td>12757.2</td>
      <td>12707.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.728</td>
    </tr>
    <tr>
      <td>CCDV</td>
      <td>38622.7</td>
      <td>38632.0</td>
      <td>38630.5</td>
      <td>&gt;0.05</td>
      <td>0.03</td>
      <td>0.050</td>
    </tr>
    <tr>
      <td>MDV</td>
      <td>36232.8</td>
      <td>36063</td>
      <td>36064</td>
      <td>&lt;0.001</td>
      <td>&gt;0.05</td>
      <td>0.142</td>
    </tr>
    <tr>
      <td>PYDV</td>
      <td>56138.4</td>
      <td>56076.6</td>
      <td>56056.4</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.187</td>
    </tr>
    <tr>
      <td>FBNS</td>
      <td>100153.6</td>
      <td>100135.6</td>
      <td>100120.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.098</td>
    </tr>
    <tr>
      <td rowspan="8">Geminiviridae</td>
      <td>Begomo 5</td>
      <td>28192.1</td>
      <td>28311.9</td>
      <td>28192.5</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.1995</td>
    </tr>
    <tr>
      <td>Begomo 6</td>
      <td>16743.0</td>
      <td>16722.6</td>
      <td>16724.1</td>
      <td>&lt;0.001</td>
      <td>&gt;0.05</td>
      <td>0.214</td>
    </tr>
    <tr>
      <td>Begomo 9</td>
      <td>8517.6</td>
      <td>8540.8</td>
      <td>8515.6</td>
      <td>0.03</td>
      <td>&lt;0.001</td>
      <td>0.312</td>
    </tr>
    <tr>
      <td>Dicot 1</td>
      <td>44730.7</td>
      <td>44594.3</td>
      <td>44583.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.200</td>
    </tr>
    <tr>
      <td>Dicot 2</td>
      <td>39909.9</td>
      <td>39919.8</td>
      <td>39917.9</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.100</td>
    </tr>
    <tr>
      <td>MSV</td>
      <td>252645.3</td>
      <td>254347.5</td>
      <td>254347.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.144</td>
    </tr>
    <tr>
      <td>PanSV</td>
      <td>94601.2</td>
      <td>94600.3</td>
      <td>94593.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.182</td>
    </tr>
    <tr>
      <td>WDV</td>
      <td>35301.7</td>
      <td>35313.2</td>
      <td>35253.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.1033</td>
    </tr>
    <tr>
      <td rowspan="7">Circoviridae</td>
      <td>BFDV</td>
      <td>17256.7</td>
      <td>17262.7</td>
      <td>17246.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.224</td>
    </tr>
    <tr>
      <td>DG_CV</td>
      <td>12754.8</td>
      <td>12779.5</td>
      <td>12758.3</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.116</td>
    </tr>
    <tr>
      <td>PiCV</td>
      <td>19180.5</td>
      <td>19192.5</td>
      <td>19191.0</td>
      <td>&gt;0.05</td>
      <td>0.04</td>
      <td>0.117</td>
    </tr>
    <tr>
      <td>CCCC</td>
      <td>84435.7</td>
      <td>84377.4</td>
      <td>84315.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.132</td>
    </tr>
    <tr>
      <td>BTC</td>
      <td>262910.4</td>
      <td>262060.1</td>
      <td>261985.4</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.178</td>
    </tr>
    <tr>
      <td>POCV2</td>
      <td>24940.9</td>
      <td>24953.8</td>
      <td>24915.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.162</td>
    </tr>
    <tr>
      <td>CCV</td>
      <td>90307.9</td>
      <td>90301.5</td>
      <td>90285.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.114</td>
    </tr>
    <tr>
      <td rowspan="2">Anelloviridae</td>
      <td>TTV_1</td>
      <td>825811</td>
      <td>826800</td>
      <td>825292</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.513</td>
    </tr>
    <tr>
      <td>TTSV</td>
      <td>332287.9</td>
      <td>332397.4</td>
      <td>332258.2</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>1.560</td>
    </tr>
    <tr>
      <td rowspan="5">Parvoviridae</td>
      <td>MVM</td>
      <td>26756.3</td>
      <td>26743.9</td>
      <td>26686.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.148</td>
    </tr>
    <tr>
      <td>HPV</td>
      <td>67051.2</td>
      <td>67080.1</td>
      <td>67001.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.235</td>
    </tr>
    <tr>
      <td>CPV</td>
      <td>85731</td>
      <td>85695</td>
      <td>85689.3</td>
      <td>&lt;0.001</td>
      <td>0.007</td>
      <td>0.062</td>
    </tr>
    <tr>
      <td>PPV</td>
      <td>163006.8</td>
      <td>163090.7</td>
      <td>162995.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.143</td>
    </tr>
    <tr>
      <td>CAV_P</td>
      <td>37073.3</td>
      <td>37115.5</td>
      <td>37065.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.162</td>
    </tr>
    <tr>
      <td>Microviridae</td>
      <td>BMV</td>
      <td>31175.3</td>
      <td>31164.8</td>
      <td>31147.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.188</td>
    </tr>
    <tr>
      <td rowspan="2">Pleolipoviridae</td>
      <td>APV</td>
      <td>85700.2</td>
      <td>85617.4</td>
      <td>85402.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.204</td>
    </tr>
    <tr>
      <td>BPV</td>
      <td>204797.5</td>
      <td>204802.3</td>
      <td>204796.7</td>
      <td>0.04</td>
      <td>0.007</td>
      <td>0.064</td>
    </tr>
  </tbody>
</table>

Based on the LRTs, strong overall support for NREV12 was found with this model providing a significantly better fit (p<0.05) than NREV6 for 45/47 of the ssRNA virus datasets (Table 4) and 31/33 of the ssDNA virus datasets (Table 3). Similarly, based on LRTs, NREV12 provided a significantly better fit than GTR for 27/33 of the ssDNA virus datasets (Table 3) and 40/47 of the ssRNA virus datasets (Table 4).

**Table 4.**
 Small sample corrected Akaike information criterion (AIC-c) scores and likelihood ratio test (LRT) results for single-stranded RNA datasets.The lowest AIC-c scores indicating the best fitting models are in bold.


<table>
  <thead>
    <tr>
      <th>Virus family</th>
      <th>Dataset</th>
      <th>AIC score GTR</th>
      <th>AIC score NREV-6</th>
      <th>AIC score NREV-12</th>
      <th>p-Value GTR vs NREV-12</th>
      <th>p-Value NREV-6 vs NREV-12</th>
      <th>DNR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Astroviridae</td>
      <td>HAV</td>
      <td>94580.7</td>
      <td>94926.3</td>
      <td>94548.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.096</td>
    </tr>
    <tr>
      <td>BAV</td>
      <td>188307.1</td>
      <td>188572.9</td>
      <td>188144.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.108</td>
    </tr>
    <tr>
      <td>MMV</td>
      <td>281072.2</td>
      <td>281094.5</td>
      <td>281076.9</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.072</td>
    </tr>
    <tr>
      <td>PAV</td>
      <td>150626.88</td>
      <td>150827.6</td>
      <td>150609.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.069</td>
    </tr>
    <tr>
      <td>CKV</td>
      <td>90902.3</td>
      <td>91233.1</td>
      <td>90873.0</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.083</td>
    </tr>
    <tr>
      <td>GA</td>
      <td>64998.5</td>
      <td>65223.9</td>
      <td>64975.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.110</td>
    </tr>
    <tr>
      <td>CAV_A</td>
      <td>85558.8</td>
      <td>85617.4</td>
      <td>85547.3</td>
      <td>&lt;0.01</td>
      <td>&lt;0.001</td>
      <td>0.076</td>
    </tr>
    <tr>
      <td rowspan="5">Bromoviridae</td>
      <td>CMV RNA1</td>
      <td>34197.5</td>
      <td>34198.8</td>
      <td>34147.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.124</td>
    </tr>
    <tr>
      <td>CMV RNA2</td>
      <td>31398.2</td>
      <td>31455.9</td>
      <td>31388.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.091</td>
    </tr>
    <tr>
      <td>CMV RNA3</td>
      <td>24337.2</td>
      <td>24360.3</td>
      <td>24343.9</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.073</td>
    </tr>
    <tr>
      <td>AMS</td>
      <td>24337.2</td>
      <td>24360.3</td>
      <td>24343.9</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.073</td>
    </tr>
    <tr>
      <td>PSV</td>
      <td>67707</td>
      <td>67786.5</td>
      <td>67691</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.048</td>
    </tr>
    <tr>
      <td rowspan="3">Caliciviridae</td>
      <td>LAV</td>
      <td>73042.8</td>
      <td>73102.4</td>
      <td>72984.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.120</td>
    </tr>
    <tr>
      <td>NoV</td>
      <td>207667.2</td>
      <td>207777.5</td>
      <td>207660</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.047</td>
    </tr>
    <tr>
      <td>VSV</td>
      <td>235936.4</td>
      <td>236051.4</td>
      <td>235913.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.046</td>
    </tr>
    <tr>
      <td>Closteroviridae</td>
      <td>CTV</td>
      <td>30062.2</td>
      <td>29980.4</td>
      <td>29960.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.272</td>
    </tr>
    <tr>
      <td rowspan="2">Flaviviridae</td>
      <td>DGV_T1</td>
      <td>69771.9</td>
      <td>70030.5</td>
      <td>69776.2</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.063</td>
    </tr>
    <tr>
      <td>JEV</td>
      <td>146920.8</td>
      <td>148101.5</td>
      <td>146885.5</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.091</td>
    </tr>
    <tr>
      <td rowspan="2">Hepeviridae</td>
      <td>HPVE1</td>
      <td>200439.5</td>
      <td>200863.8</td>
      <td>200179.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.073</td>
    </tr>
    <tr>
      <td>HPVE2</td>
      <td>155709.1</td>
      <td>155983.8</td>
      <td>155518.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.088</td>
    </tr>
    <tr>
      <td rowspan="8">Picornaviridae</td>
      <td>ENV_A</td>
      <td>552287.9</td>
      <td>553535.5</td>
      <td>551794.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.061</td>
    </tr>
    <tr>
      <td>HRV_A</td>
      <td>102218.7</td>
      <td>102267.0</td>
      <td>101550.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.285</td>
    </tr>
    <tr>
      <td>AIV</td>
      <td>101073.1</td>
      <td>101136.7</td>
      <td>101052.2</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.093</td>
    </tr>
    <tr>
      <td>AHP</td>
      <td>139635.7</td>
      <td>140119.6</td>
      <td>139506.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.170</td>
    </tr>
    <tr>
      <td>ECV</td>
      <td>82078.9</td>
      <td>82181.0</td>
      <td>82065.8</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.066</td>
    </tr>
    <tr>
      <td>CDV</td>
      <td>130551.3</td>
      <td>130896.7</td>
      <td>130478.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.086</td>
    </tr>
    <tr>
      <td>TCV</td>
      <td>53027.3</td>
      <td>53029</td>
      <td>53023</td>
      <td>0.0151</td>
      <td>0.0422</td>
      <td>0.033</td>
    </tr>
    <tr>
      <td>FMDV</td>
      <td>455180.6</td>
      <td>455582.6</td>
      <td>454806.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.117</td>
    </tr>
    <tr>
      <td>Fusariviridae</td>
      <td>FRV</td>
      <td>52413.1</td>
      <td>52470.6</td>
      <td>52418.4</td>
      <td>&gt;0.05</td>
      <td>&lt;0.001</td>
      <td>0.076</td>
    </tr>
    <tr>
      <td rowspan="11">Retroviridae</td>
      <td>HIV1_setA</td>
      <td>344014.4</td>
      <td>344295.1</td>
      <td>343669.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.237</td>
    </tr>
    <tr>
      <td>HIV1_M</td>
      <td>80764.1</td>
      <td>80829.5</td>
      <td>80668.1</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.442</td>
    </tr>
    <tr>
      <td>HIV1_setC</td>
      <td>180575.0</td>
      <td>180702.3</td>
      <td>180494.4</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.107</td>
    </tr>
    <tr>
      <td>HIV1_setD</td>
      <td>298489.9</td>
      <td>298695.3</td>
      <td>298260.6</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.133</td>
    </tr>
    <tr>
      <td>HIV1_setE</td>
      <td>289111.3</td>
      <td>289292.1</td>
      <td>288941.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.112</td>
    </tr>
    <tr>
      <td>HIV1_setF</td>
      <td>214375.9</td>
      <td>214692.2</td>
      <td>214289.4</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.148</td>
    </tr>
    <tr>
      <td>EIV</td>
      <td>126149</td>
      <td>126365.4</td>
      <td>125300</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.192</td>
    </tr>
    <tr>
      <td>BIV</td>
      <td>24505.2</td>
      <td>24506.9</td>
      <td>24513.2</td>
      <td>&gt;0.05</td>
      <td>&gt;0.05</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>FIV</td>
      <td>164542.1</td>
      <td>164487.9</td>
      <td>164260.4</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.114</td>
    </tr>
    <tr>
      <td>CAV</td>
      <td>351329.9</td>
      <td>351871.5</td>
      <td>350721.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.174</td>
    </tr>
    <tr>
      <td>SIV</td>
      <td>110731.2</td>
      <td>110816</td>
      <td>110663.3</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.144</td>
    </tr>
    <tr>
      <td>Filoviridae</td>
      <td>Ebola_2</td>
      <td>53147.3</td>
      <td>53143.0</td>
      <td>53149.9</td>
      <td>&gt;0.05</td>
      <td>&gt;0.50</td>
      <td>0.264</td>
    </tr>
    <tr>
      <td rowspan="2">Orthomyxo-viridae</td>
      <td>Flu A 2</td>
      <td>82872.8</td>
      <td>83010.2</td>
      <td>82849.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>Flu B 1</td>
      <td>50090.4</td>
      <td>50144.1</td>
      <td>50060.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.311</td>
    </tr>
    <tr>
      <td rowspan="4">Coronaviridae</td>
      <td>SARS-COV1</td>
      <td>214715.3</td>
      <td>214968.5</td>
      <td>214644.39</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.198</td>
    </tr>
    <tr>
      <td>SARS-COV2</td>
      <td>15715.4.2</td>
      <td>15715.6</td>
      <td>15696.7</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>1.536</td>
    </tr>
    <tr>
      <td>SARB</td>
      <td>573966.3</td>
      <td>573815.1</td>
      <td>572517.0</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.301</td>
    </tr>
    <tr>
      <td>MERS-COV</td>
      <td>516683.2</td>
      <td>516983.4</td>
      <td>516608.9</td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.169</td>
    </tr>
  </tbody>
</table>

We found that the degree of non-reversibility (DNR) estimates alone did not cleanly differentiate between datasets for which NREV12 was or was not best supported (Tables 1–4). For the 107 nucleotide sequence datasets with a model preference of NREV12, 10 had estimated DNRs that were greater than 0.5, 13 had DNRs between 0.25 and 0.5, and 84 had DNRs between 0.0225 and 0.25. For the 10 nucleotide sequence datasets with a model preference of NREV6, one had an estimated DNR greater than 0.5, four had estimated DNRs between 0.25 and 0.5, and five had estimated DNRs between 0.064 and 0.25 (Figure 1). For the 24 nucleotide sequence datasets with a model preference of GTR, none had estimated DNRs greater than 0.5, one had an estimated DNR between 0.25 and 0.5, and the remainder had estimated DNRs between 0.0335 and 0.25.

The dsDNA virus dataset with the highest DNR was Human mastadenovirus D (DNR = 0.646), the dsRNA virus dataset with the highest estimated DNR was Porcine_rotavirus_B (0.351), the ssRNA virus dataset with the highest DNR was SARS-CoV-2 (DNR = 1.536), and the ssDNA virus dataset with the highest DNR was Torque teno sus virus (DNR = 1.56).

Therefore, while NREV12 appears to be generally more appropriate than either NREV6 or GTR for describing mutational processes in ssRNA, ssDNA, dsDNA, and dsRNA viruses, this might only be particularly relevant from a practical perspective when datasets of these viruses yield DNR estimates that are greater than 0.25. For such datasets, NREV12 (and possibly NREV 6 in some instances) might be especially useful for both determining the direction of evolution across phylogenetic trees (i.e. it could potentially be used to root these trees) and for quantifying genomic strand-specific nucleotide substitution biases (Harkins et al., 2009).

### Assessing the impacts of model misspecification on phylogenetic tree inference

To determine whether it is worthwhile to use NREV12 rather than GTR for phylogenetic inference when NREV12 is the best fitting nucleotide substitution model, we used simulated datasets to compare the accuracy of phylogenetic trees inferred using these models.

We found that, regardless of dataset diversity and the nucleotide substitution model used, phylogenetic inference tended to become less accurate (i.e. weighted Robinson-Foulds [wRF] scores increased) as DNR increased (Figure 2). This tendency was, however, more pronounced when using a (mis-specified) GTR model than when using a (correctly specified) NREV12 model with, for any given dataset having DNR>0, the use of NREV12 tending to yield more accurate phylogenetic trees than when GTR was used. There were, however, only statistically significant improvements (p<0.05, paired t-test) in the accuracy of phylogenetic trees inferred using NREV12 relative to those inferred using GTR in lower diversity datasets (i.e. those with average pairwise nucleotide sequence identities (APIs) of 85%, 90%, and 95%) and then only for DNR>8. It is noteworthy that the highest estimated DNR in any of the empirical datasets that we analysed was 1.56 more than fourfold lower than the point where statistically significant differences in phylogenetic inference accuracies became apparent in the simulated datasets.

## Materials and methods

### Virus sequence datasets and phylogenetic trees

We obtained viral nucleotide sequences from the National Centre for Biotechnology Information Taxonomy database (http://www.ncbi.nlm.nih.gov/taxonomy) and the Los Alamos National Laboratory HIV sequence database (https://www.hiv.lanl.gov/content/index). These included gene and whole-genome sequences for viruses with ssRNA, ssDNA, dsRNA, and dsDNA genomes (datasets are summarised in Supplementary file 1). An outgroup sequence from a closely related virus species was added to each dataset to help root phylogenetic trees. The sequences in each of the datasets were aligned using MUSCLE (Edgar, 2004) implemented in Aliview (Larsson, 2014)⁠, and maximum likelihood phylogenetic trees were constructed from each alignment using RAxML v8.2 (Stamatakis, 2016)⁠.

### Model testing

We evaluated the fit of NREV12, NREV6, and GTR to the 141 individual sequence datasets using a previously published model test (Harkins et al., 2009) implemented as a HyPhy package module (Pond and Muse, 2005). This script (https://github.com/veg/hyphy-analyses/tree/master/NucleotideNonREV; Delport and Kosakovsky Pond, 2023) is also available as a module in the Datamonkey web server (Weaver et al., 2018), which takes as input a rooted maximum likelihood phylogenetic tree (minus the rooting sequence) and its corresponding nucleotide sequence alignment. The three models described above: GTR, NREV6, and NREV12 are then fitted to the data using maximum likelihood (ML). The equilibrium frequencies (EF) of the GTR model match those empirically observed in the alignment, while EFs for NREV6 and NREV12 are inferred by the model, satisfying the condition $\piQ=0$. An additional model NREV12 + F is estimated, where the distribution of nucleotides at the root of the tree is estimated by maximum likelihood, instead of being set to the empirical frequencies. Nested models were compared by the LRT with significance evaluated using the $χ_{d}^{2}$  distribution with d=difference in degrees of freedom. For all models, we also computed the small AIC-c score.

### Quantification of non-reversibility

We further defined the DNR as the absolute difference between the relative rate differences of two nucleotide pairs; i.e., for two nucleotides, x and y, there exists a relative rate of x to y substitutions that we will refer to as m, and a relative rate of y to x substitutions that we will refer to as n. Under the NREV12 model, the DNR between x and y is defined simply as the absolute difference between m and n: (|m-n|) and will hereby be referred to as $ij_{DNR}$, where $i$ and $j$ are two nucleotides. We use DNR as a mathematical representation of the degree to which the rates of all pairs of reverse substitutions differ from one another. For each of the 140 individual viral alignments, we calculated the average DNR of the six $ij_{DNR}$ estimates inferred using the NREV12 model.

### Simulations for testing the impact of non-reversible evolution on phylogenetic inference

We tested the accuracy of phylogenetic tree inference under reversible and non-reversible models using simulated datasets with varying APIs evolved under the NREV12 model with different DNRs. The goal of these tests was not to exhaustively evaluate model misspecification issues during phylogenetic tree inference, but rather to check, in instances where viral taxa are known to be evolving in a detectably non-reversible manner (i.e. where NREV12 or NREV6 fits the data better than GTR), whether not accounting for this might decrease the accuracy of phylogenetic inference. Using IQ-TREE, a phylogenetic inference program that has the option to apply an NREV12-like model (referred to in IQ-TREE as the UNREST model), a phylogenetic tree was inferred from an alignment of real sequences (Avian Leukosis virus) (Figure 3) with an API of ~90%. The branch lengths on this tree were then scaled to create four other phylogenetic trees representing sequences with approximately 95%, 85%, 80%, and 75% API. These five trees are hereafter referred to as ‘true’ trees, and each individual tree was used as the starting point of a different set of simulations.

![Figure 3.](https://cdn.elifesciences.org/articles/87361/elife-87361-fig3-v1.jpg)

**Figure 3.:** The alignment of Avian Leukosis virus had an average sequence identity (API) of ~90%, and the branches of this tree were scaled to produce four other trees reflecting branch tip sequences with approximate pairwise identities of ~75%, ~80%, ~85%, and~95%.

Phylogenetic trees were inferred from these 5500 simulated datasets and compared to the phylogenetic trees used to simulate the datasets (i.e. the true trees) using wRF distances to assess the impact of varying DNR on the accuracy of phylogenetic inference. We further tested whether the accuracy of phylogenetic inference could be improved for sequences that had evolved under DNR >0 by using NREV12 instead of GTR. Specifically, for every simulated dataset, a phylogenetic tree was inferred using GTR, and another using NREV12 and the wRF distances of each of these trees to the true tree was determined. For each of the analysed DNRs, a paired t-test was then used to compare the wRF scores of trees inferred using GTR and NREV12. We were particularly interested in determining whether trees inferred using a mis-specified model (i.e. GTR in this case) would be less accurate than trees inferred with a correctly specified model (i.e. NREV12).

To test whether failure to account for non-reversibility might decrease the accuracy of phylogenetic inference, we simulated the evolution of 5500 nucleotide sequence alignments evolved non-reversibly under varying DNR along the five true phylogenetic trees: 100 datasets per true tree per simulated DNR. Specifically, simulations were done using HyPhy (Pond and Muse, 2005), with relative rates ranging from a completely reversible matrix (Equation 4)

$$
Q={q_{ij}}=(−0.16610.140.166−0.1311.10110.131−0.1880.141.1010.188−)
$$

representing DNR = 0 – through matrices with DNR = 2, 4, 6, 8, 10, 12, 14, 16, 18, and 20 (Table 5). These baselines-simulated substitution rates are reflective of those seen in empirical viral nucleotide sequence datasets.

**Table 5.**
 Relative rate change for C to A, G to A, A to T, G to C, T to G, and C to T mutations under the 11 degrees of non-reversibility alongside the maintained rates for A to C, A to G, T to A, C to G, G to T, and T to C.


<table>
  <thead>
    <tr>
      <th rowspan="2">Degree of non-reversibility (DNR)</th>
      <th colspan="12">Relative rates of different nucleotide substitution types (from-to)</th>
    </tr>
    <tr>
      <th>C-A</th>
      <th>A-C</th>
      <th>G-A</th>
      <th>A-G</th>
      <th>A-T</th>
      <th>T-A</th>
      <th>G-C</th>
      <th>C-G</th>
      <th>T-G</th>
      <th>G-T</th>
      <th>C-T</th>
      <th>T-C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.166</td>
      <td>0.166</td>
      <td>1</td>
      <td>1</td>
      <td>0.14</td>
      <td>0.14</td>
      <td>0.131</td>
      <td>0.131</td>
      <td>0.118</td>
      <td>0.118</td>
      <td>1.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2.166</td>
      <td>0.166</td>
      <td>3</td>
      <td>1</td>
      <td>2.14</td>
      <td>0.14</td>
      <td>2.131</td>
      <td>0.131</td>
      <td>2.118</td>
      <td>0.118</td>
      <td>3.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4.166</td>
      <td>0.166</td>
      <td>5</td>
      <td>1</td>
      <td>4.14</td>
      <td>0.14</td>
      <td>4.131</td>
      <td>0.131</td>
      <td>4.118</td>
      <td>0.118</td>
      <td>5.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6.166</td>
      <td>0.166</td>
      <td>7</td>
      <td>1</td>
      <td>6.14</td>
      <td>0.14</td>
      <td>6.131</td>
      <td>0.131</td>
      <td>6.118</td>
      <td>0.118</td>
      <td>7.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>8</td>
      <td>8.166</td>
      <td>0.166</td>
      <td>9</td>
      <td>1</td>
      <td>8.14</td>
      <td>0.14</td>
      <td>8.131</td>
      <td>0.131</td>
      <td>8.118</td>
      <td>0.118</td>
      <td>9.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10.166</td>
      <td>0.166</td>
      <td>11</td>
      <td>1</td>
      <td>10.14</td>
      <td>0.14</td>
      <td>10.131</td>
      <td>0.131</td>
      <td>10.118</td>
      <td>0.118</td>
      <td>11.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>12</td>
      <td>12.166</td>
      <td>0.166</td>
      <td>13</td>
      <td>1</td>
      <td>12.14</td>
      <td>0.14</td>
      <td>12.131</td>
      <td>0.131</td>
      <td>12.118</td>
      <td>0.118</td>
      <td>13.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>14</td>
      <td>14.166</td>
      <td>0.166</td>
      <td>15</td>
      <td>1</td>
      <td>14.14</td>
      <td>0.14</td>
      <td>14.131</td>
      <td>0.131</td>
      <td>14.118</td>
      <td>0.118</td>
      <td>15.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>16</td>
      <td>16.166</td>
      <td>0.166</td>
      <td>17</td>
      <td>1</td>
      <td>16.14</td>
      <td>0.14</td>
      <td>16.131</td>
      <td>0.131</td>
      <td>16.118</td>
      <td>0.118</td>
      <td>17.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>18</td>
      <td>18.166</td>
      <td>0.166</td>
      <td>19</td>
      <td>1</td>
      <td>18.14</td>
      <td>0.14</td>
      <td>18.131</td>
      <td>0.131</td>
      <td>18.118</td>
      <td>0.118</td>
      <td>19.101</td>
      <td>1.101</td>
    </tr>
    <tr>
      <td>20</td>
      <td>20.166</td>
      <td>0.166</td>
      <td>21</td>
      <td>1</td>
      <td>20.14</td>
      <td>0.14</td>
      <td>20.131</td>
      <td>0.131</td>
      <td>20.118</td>
      <td>0.118</td>
      <td>21.101</td>
      <td>1.101</td>
    </tr>
  </tbody>
</table>

At each DNR, the relative rates used conformed to standard measures of non-reversibility under the Kolmogorov conditions according to which non-reversibly evolving sequence datasets should yield three irreversibility indices (IRI1, IRI2, and IRI3) that are all non-zero (Squartini and Arndt, 2008). It should be noted that all simulations under NREV12 were performed under the stationarity criterion: $\pie^{Qt}=\pi$ (where Q is the rate matrix, π is the nucleotide frequency distribution, and t≥0).

### Quantifying the accuracy of phylogenetic inferences

We used the wRF (implemented in the R phangorn package; Schliep, 2011⁠) to quantify differences between the true trees used to simulate datasets and the trees inferred from these datasets using the GTR or NREV12 models. wRF considers differences between both the topology and branch lengths of actual and inferred trees (Kuhner and Yamato, 2015; Robinson and Foulds, 1981).

### Conclusion

The non-reversible nucleotide substitution model, NREV12, provides a substantially better fit to most virus nucleotide sequence datasets than does the widely used reversible substitution model, GTR. NREV12 also provides a better fit to most virus nucleotide sequence datasets than does NREV6; a non-reversible model that would be expected to best describe the evolution of double-stranded genome sequences that display no strand-specific nucleotide substitution biases. This suggests that, contrary to our expectations, substantial strand-specific nucleotide substitution biases (i.e. estimated DNRs>0.25) are common during viral evolution irrespective of genome type. Such biases should be expected for any viruses where one genome strand either is in existence for substantially longer periods of time than the other, or is more exposed to mutagenic processes than the other during transmission, replication, or gene expression.

We had anticipated that, given evidence of sequences evolving both non-reversibly and with strand-specific substitution biases, inferring trees using a model such as NREV12 that appropriately accounts for this might: (1) minimise the impact of increasing DNR on the accuracy of phylogenetic inference (i.e. wRF scores presented in blue in Figure 2 might have been expected to not increase with increasing DNR) and (2) yield significantly more accurate phylogenetic inferences than when using GTR for all datasets where NREV12 was the most appropriate model and DNRs were greater than zero. However, increasing DNR clearly decreased the accuracy of phylogenetic inference even when using NREV12, and, for datasets where DNRs were greater than zero, using GTR did not consistently yield significantly less accurate phylogenetic inferences than those attained using NREV12. From a practical perspective, choosing a non-reversible nucleotide substitution model to construct phylogenetic trees from virus genome sequences that display strand-specific nucleotide substitution biases is not guaranteed to yield more accurate phylogenetic trees. Nevertheless, in instances where strand-specific substitution biases are higher than ~0.5 (such as are found in our SARS-CoV-2, Torque teno sus virus, and Banana bunchy top virus datasets), it may be prudent to select a model such as NREV12 (such as is implemented in programs like IQ-TREE) over GTR as the better of two suboptimal choices.

The lack of available data regarding the proportions of viral life cycles during which genomes exist in single- and double-stranded states makes it difficult to rationally predict the situations where the use of models such as GTR, NREV6, and NREV12 might be most justified: particularly in light of the poor overall performance of NREV6 and GTR relative to NREV12 with respect to describing mutational processes in viral genome sequence datasets. We therefore recommend case-by-case assessments of NREV12 vs NREV6 vs GTR model fit when deciding whether it is appropriate to consider the application of non-reversible models for phylogenetic inference and/or phylogenetic model-based analyses such as those intended to test for evidence of natural selection or the existence of molecular clocks.

### Declarations

#### Ethics

The University of Cape Town ethics committee declared that this research did not need ethics approval due to the use of freely accessible nucleotide sequences obtained from the National Centre for Biotechnology Information Taxonomy database (https://www.ncbi.nlm.nih.gov/taxonomy) and the Los Alamos National Laboratory HIV sequence database (https://www.hiv.lanl.gov/content/index).
