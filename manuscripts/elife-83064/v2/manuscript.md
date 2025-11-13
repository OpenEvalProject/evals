# Succinate mediates inflammation-induced adrenocortical dysfunction

## Authors

- Ivona Mateska<sup>1</sup> ([ORCID: 0000-0001-6150-9175](https://orcid.org/0000-0001-6150-9175)) †
- Anke Witt<sup>1</sup>
- Eman Hagag<sup>1</sup>
- Anupam Sinha<sup>1</sup>
- Canelif Yilmaz<sup>1</sup> ([ORCID: 0000-0002-9676-9310](https://orcid.org/0000-0002-9676-9310))
- Evangelia Thanou<sup>2</sup> ([ORCID: 0000-0001-6843-4591](https://orcid.org/0000-0001-6843-4591))
- Na Sun<sup>3</sup>
- Ourania Kolliniati<sup>4</sup>
- Maria Patschin<sup>1</sup>
- Heba Abdelmegeed<sup>1</sup>
- Holger Henneicke<sup>5</sup>
- Waldemar Kanczkowski<sup>1</sup>
- Ben Wielockx<sup>1</sup>
- Christos Tsatsanis<sup>4</sup>
- Andreas Dahl<sup>7</sup> ([ORCID: 0000-0002-2668-8371](https://orcid.org/0000-0002-2668-8371))
- Axel Karl Walch<sup>3</sup>
- Ka Wan Li<sup>2</sup> ([ORCID: 0000-0001-6983-5055](https://orcid.org/0000-0001-6983-5055))
- Mirko Peitzsch<sup>1</sup> ([ORCID: 0000-0002-2472-675X](https://orcid.org/0000-0002-2472-675X))
- Triantafyllos Chavakis<sup>1</sup>
- Vasileia Ismini Alexaki<sup>1</sup> ([ORCID: 0000-0003-3935-8985](https://orcid.org/0000-0003-3935-8985)) †

### Affiliations

1. Institute of Clinical Chemistry and Laboratory Medicine, University Hospital, Technische Universität Dresden Dresden Germany ([ROR:042aqky30](https://ror.org/042aqky30))
2. Center of Neurogenomics and Cognitive Research (CNCR), Department of Molecular and 10 Cellular Neurobiology, Vrije Universiteit Amsterdam Netherlands ([ROR:008xxew50](https://ror.org/008xxew50))
3. Research Unit Analytical Pathology, German Research Center for Environmental Health, Helmholtz Zentrum München Munich Germany ([ROR:00cfam450](https://ror.org/00cfam450))
4. Department of Clinical Chemistry, Medical School, University of Crete Heraklion Greece ([ROR:00dr28g20](https://ror.org/00dr28g20))
5. Department of Medicine III & Center for Healthy Ageing, Technische Universität Dresden Dresden Germany ([ROR:042aqky30](https://ror.org/042aqky30))
6. Center for Regenerative Therapies, TU Dresden, Technische Universität Dresden Dresden Germany ([ROR:042aqky30](https://ror.org/042aqky30))
7. DRESDEN-concept Genome Center, Center for Molecular and Cellular Bioengineering, Technische Universität Dresden Dresden Germany ([ROR:042aqky30](https://ror.org/042aqky30))

† Corresponding author

## Abstract

The hypothalamus-pituitary-adrenal (HPA) axis is activated in response to inflammation leading to increased production of anti-inflammatory glucocorticoids by the adrenal cortex, thereby representing an endogenous feedback loop. However, severe inflammation reduces the responsiveness of the adrenal gland to adrenocorticotropic hormone (ACTH), although the underlying mechanisms are poorly understood. Here, we show by transcriptomic, proteomic, and metabolomic analyses that LPS-induced systemic inflammation triggers profound metabolic changes in steroidogenic adrenocortical cells, including downregulation of the TCA cycle and oxidative phosphorylation, in mice. Inflammation disrupts the TCA cycle at the level of succinate dehydrogenase (SDH), leading to succinate accumulation and disturbed steroidogenesis. Mechanistically, IL-1β reduces SDHB expression through upregulation of DNA methyltransferase 1 (DNMT1) and methylation of the SDHB promoter. Consequently, increased succinate levels impair oxidative phosphorylation and ATP synthesis and enhance ROS production, leading to reduced steroidogenesis. Together, we demonstrate that the IL-1β-DNMT1-SDHB-succinate axis disrupts steroidogenesis. Our findings not only provide a mechanistic explanation for adrenal dysfunction in severe inflammation, but also offer a potential target for therapeutic intervention.

## Introduction

Stress triggers the hypothalamic-pituitary-adrenal (HPA) axis, that is, the release of corticotropin-releasing hormone from the hypothalamus, followed by adrenocorticotropic hormone (ACTH) secretion from the anterior pituitary, which stimulates the synthesis of glucocorticoid hormones in the adrenal cortex, primarily cortisol in humans and corticosterone in rodents (Chrousos, 1995; Lightman et al., 2020; Payne and Hales, 2004). Similar to any other stress stimulus, inflammation activates the HPA axis leading to increased glucocorticoid release, which is required to restrain the inflammatory response (Alexaki, 2021a; Alexaki and Henneicke, 2021b; Kanczkowski et al., 2013a; Kanczkowski et al., 2013b; Kanczkowski et al., 2013c). Adrenalectomized rodents show increased mortality after induction of systemic inflammation, while glucocorticoid administration increases survival (Bertini et al., 1988; Butler et al., 1989). Essentially, severe inflammation in sepsis is associated with impaired adrenal gland function (Annane et al., 2000; Boonen et al., 2015; Boonen et al., 2014; den Brinker et al., 2005; Jennewein et al., 2016), but the mechanisms remain poorly understood.

In immune cells, such as macrophages, dendritic cells, and T cells, inflammation triggers cellular metabolic reprograming, enabling the cells to meet the increased demands for fast energy supply and anabolic processes (Geltink et al., 2018; O’Neill and Pearce, 2016; Ryan and O’Neill, 2020). How inflammation may affect cellular metabolism in other cell types and how this affects their function is less explored. Here, we show that LPS-induced inflammation profoundly changes the cellular metabolism of steroidogenic adrenocortical cells, perturbing the TCA cycle at the level of succinate dehydrogenase B (SDHB). This is coupled to succinate accumulation, which impairs oxidative phosphorylation and leads to reduced steroidogenesis. Mechanistically, IL-1β inhibits SDHB expression through DNA methyltransferase 1 (DNMT1)-dependent DNA methylation of the SDHB promoter.

## Results

### Metabolic reprograming of the adrenal cortex in inflammation

To explore inflammation-induced alterations in the adrenal cortex, we performed RNA-Seq in microdissected adrenal cortices from mice treated for 6 hr i.p. with 1 mg/kg LPS or PBS, which revealed 2,609 differentially expressed genes, out of which 1,363 were down- and 1,246 were upregulated (Figure 1A). Gene set enrichment analysis (GSEA) using the Molecular Signatures Database (MSigDB) hallmark gene set collection (Liberzon et al., 2015) showed a significant enrichment of inflammatory response-related gene sets in the adrenal cortex of LPS-treated mice (Figure 1B). In acute inflammation, leukocytes infiltrate the adrenal cortex (Kanczkowski et al., 2013b) and resident macrophages are activated (González-Hernández et al., 1994; Schober et al., 1998). In order to delineate the inflammatory response in the adrenocortical steroidogenic cells, CD31-CD45- cells were sorted: enrichment in steroidogenic cells was evidenced by high steroidogenic acute regulatory protein (Star) expression (Figure 1—figure supplement 1a), and purity was verified by the absence of Cd31 and Cd45 expression (Figure 1—figure supplement 1B and C). Moreover, we confirmed the absence of expression of the medullar markers tyrosine hydroxylase (Th) and phenylethanolamine N-methyltransferase (Pnmt) in isolated cortices and adrenocortical steroidogenic cells (Figure 1—figure supplement 1D and E). Proteomic analysis in the sorted CD31-CD45- adrenocortical cell population and GSEA of GO terms confirmed the enrichments of innate immune response-related proteins in adrenocortical cells of LPS-injected mice (Figure 1C), suggesting that steroidogenic adrenocortical cells respond to inflammatory stimuli.

![Figure 1.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig1-v2.jpg)

**Figure 1.:** (A) Volcano plot showing differentially expressed genes in the microdissected adrenal gland cortex of mice treated for 6 hr with PBS or LPS. (B) Gene set enrichment analysis (GSEA) for immune pathways in the adrenal cortex of LPS versus PBS mice. (C) GSEA for proteins associated with the innate immune response in CD31-CD45- adrenocortical cells of mice treated for 24 hr with PBS or LPS. (D) RNA-Seq-based GSEA for carbohydrate metabolism in the adrenal cortex of LPS versus PBS mice. (E) GSEA for proteins associated with carbohydrate metabolism in CD31-CD45- adrenocortical cells of LPS versus PBS mice. NES: normalized enrichment score. (A,B,D) n=3 mice per group, (C,E) n=6 mice per group, padj <0.05 was used as a cut-off for significance.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** mRNA expression of Star (A), Cd31 (B), and Cd45 (C) in sorted CD31-CD45-, CD45+, and CD31+ cell populations from adrenal glands of mice 6 hr post-injection of PBS or LPS (n=6 mice per group). mRNA expression of tyrosine hydroxylase (Th) (D) and phenylethanolamine N-methyltransferase (Pnmt) (E) in medulla, cortex, and CD31-CD45- cells (ACC) (n=4 mice per group). Data are presented as mean ± s.d. Statistical analysis was done with two-tailed Mann-Whitney U-test. *p<0.05, **p<0.01.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A–E) mRNA expression of steroidogenic enzymes (Star, Cyp11b1, Hsd3b2, Cyp21a1, and Cyp11a1) in adrenocortical cells of mice treated for 6 hr with PBS or LPS (n=6–8 mice per group, shown one from two experiments). (F) Representative immunofluorescence images of adrenal gland sections from PBS and LPS mice stained for steroidogenic factor 1 (SF-1) (magenta) and DAPI (blue). Scale bar, 300 μm. Quantification of the mean fluorescence intensity of SF-1 staining in the adrenal cortex (excluding the outer capsule region) (n=6 mice per group). Data are presented as mean ±s.d. Statistical analysis was done with two-tailed Mann-Whitney test. *p<0.05, **p<0.01.

LPS treatment leads to increased plasma corticosterone levels (Kanczkowski et al., 2013a; Kanczkowski et al., 2013b; Kanczkowski et al., 2013c). Numerous studies have shown that elevated glucocorticoid levels are primarily driven by activation of the HPA axis and coincide with increased circulating ACTH levels (Kanczkowski et al., 2013a; Kanczkowski et al., 2013b; Kanczkowski et al., 2013c). This is accompanied by increased expression of genes related to steroid biosynthesis (Chen et al., 2019b). We confirmed increased expression of the cholesterol transporter Star (Miller, 2007) and the terminal enzyme for glucocorticoid synthesis Cyp11b1 (Payne and Hales, 2004) in adrenocortical cells of LPS mice (Figure 1—figure supplement 2A and B). However, the expression of genes encoding for other steroidogenic enzymes, such as 3β-hydroxysteroid dehydrogenase 2 (Hsd3b2) and Cyp21a1, was reduced, while Cyp11a1 remained unchanged (Figure 1—figure supplement 2C–E). Similarly, protein levels of steroidogenic factor 1 (SF-1), a key inducer of steroidogenesis (Parker, 1999), were somewhat reduced after LPS injection (Figure 1—figure supplement 2F). Therefore, the observed changes in plasma glucocorticoid levels which accompany inflammation cannot be solely explained by the transcriptional changes in steroidogenic enzymes.

Next, we explored the cell metabolic changes induced by LPS in the adrenal cortex. By GSEA of the RNA-Seq data, we observed negative regulation of gene sets related to carbohydrate metabolism in the adrenal cortex of LPS-injected mice (Figure 1D). Proteomic analysis was performed in CD31-CD45- adrenocortical cells (Figure 1—figure supplement 1) to examine the effects of inflammation specifically on the metabolism of steroidogenic adrenocortical cells, evading the well-described inflammation-induced metabolic changes in immune cells (Geltink et al., 2018; O’Neill and Pearce, 2016; Ryan and O’Neill, 2020). Similarly to the RNA-Seq data, GSEA of the proteomic data showed significant negative enrichment of proteins associated with carbohydrate metabolism in the steroidogenic cells (Figure 1E). EGSEA pathway analysis of the RNA-Seq and proteomic data revealed that TCA cycle, oxidative phosphorylation, tyrosine metabolism, fatty acid degradation, D-glutamine and D-glutamate metabolism, glutathione metabolism, and other metabolic pathways were significantly enriched among the downregulated genes and proteins in the adrenal cortex and in steroidogenic cells of LPS mice (Table 1, Table 2).

**Table 1.**
 Cellular metabolic pathways transcriptionally regulated by inflammation in the adrenal cortex.The pathway analysis of differentially expressed genes was done with the software package EGSEA and queried against the KEGG pathways repository. Pathways with p<0.05 are shown.


<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Metabolic pathway</th>
      <th>Number of expressed genes</th>
      <th>p-Value</th>
      <th>padj</th>
      <th>avg.logfc</th>
      <th>Direction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mmu00190</td>
      <td>Oxidative phosphorylation</td>
      <td>132/134</td>
      <td>8.32E-15</td>
      <td>7.32E-13</td>
      <td>0.613034377</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00280</td>
      <td>Valine, leucine, and isoleucine degradation</td>
      <td>55/56</td>
      <td>1.16E-05</td>
      <td>0.001119154</td>
      <td>0.725758563</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00511</td>
      <td>Other glycan degradation</td>
      <td>18/18</td>
      <td>3.82E-05</td>
      <td>0.001119154</td>
      <td>0.29921956</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00980</td>
      <td>Metabolism of xenobiotics by cytochrome P450</td>
      <td>65/65</td>
      <td>0.000282456</td>
      <td>0.006214029</td>
      <td>0.650304677</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00350</td>
      <td>Tyrosine metabolism</td>
      <td>38/39</td>
      <td>0.001754788</td>
      <td>0.030884268</td>
      <td>0.305935415</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00640</td>
      <td>Propanoate metabolism</td>
      <td>31/31</td>
      <td>0.002151447</td>
      <td>0.031554563</td>
      <td>0.886410728</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00020</td>
      <td>Citrate cycle (TCA cycle)</td>
      <td>32/32</td>
      <td>0.003091828</td>
      <td>0.034636464</td>
      <td>0.21912487</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01200</td>
      <td>Carbon metabolism</td>
      <td>118/118</td>
      <td>0.003685749</td>
      <td>0.034636464</td>
      <td>0.715139933</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00471</td>
      <td>D-Glutamine and D-glutamate metabolism</td>
      <td>3/3</td>
      <td>0.003980826</td>
      <td>0.034636464</td>
      <td>0.338725016</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00300</td>
      <td>Lysine biosynthesis</td>
      <td>2/2</td>
      <td>0.004518807</td>
      <td>0.034636464</td>
      <td>0.156233777</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00630</td>
      <td>Glyoxylate and dicarboxylate metabolism</td>
      <td>29/29</td>
      <td>0.006079126</td>
      <td>0.034636464</td>
      <td>0.886410728</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00071</td>
      <td>Fatty acid degradation</td>
      <td>49/49</td>
      <td>0.006124673</td>
      <td>0.034636464</td>
      <td>0.401441917</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01210</td>
      <td>2-Oxocarboxylic acid metabolism</td>
      <td>19/19</td>
      <td>0.006297539</td>
      <td>0.034636464</td>
      <td>0.942661129</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00920</td>
      <td>Sulfur metabolism</td>
      <td>11/11</td>
      <td>0.006297539</td>
      <td>0.034636464</td>
      <td>0.601864913</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00480</td>
      <td>Glutathione metabolism</td>
      <td>58/59</td>
      <td>0.006297539</td>
      <td>0.034636464</td>
      <td>0.550257753</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00510</td>
      <td>N-Glycan biosynthesis</td>
      <td>49/49</td>
      <td>0.006297539</td>
      <td>0.034636464</td>
      <td>0.254426968</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00450</td>
      <td>Selenocompound metabolism</td>
      <td>17/17</td>
      <td>0.009115527</td>
      <td>0.047186259</td>
      <td>0.329118527</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00514</td>
      <td>Other types of O-glycan biosynthesis</td>
      <td>22/22</td>
      <td>0.010614958</td>
      <td>0.050693394</td>
      <td>0.204924928</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00440</td>
      <td>Phosphonate and phosphinate metabolism</td>
      <td>6/6</td>
      <td>0.010945165</td>
      <td>0.050693394</td>
      <td>0.291510253</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00120</td>
      <td>Primary bile acid biosynthesis</td>
      <td>16/16</td>
      <td>0.01193422</td>
      <td>0.052510566</td>
      <td>2.713591551</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00565</td>
      <td>Ether lipid metabolism</td>
      <td>44/44</td>
      <td>0.016711812</td>
      <td>0.061724814</td>
      <td>0.433837026</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00520</td>
      <td>Amino sugar and nucleotide sugar metabolism</td>
      <td>49/49</td>
      <td>0.018212661</td>
      <td>0.061724814</td>
      <td>0.652646241</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00790</td>
      <td>Folate biosynthesis</td>
      <td>14/14</td>
      <td>0.01821569</td>
      <td>0.061724814</td>
      <td>0.420000237</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00230</td>
      <td>Purine metabolism</td>
      <td>174/178</td>
      <td>0.018793387</td>
      <td>0.061724814</td>
      <td>0.830115541</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00603</td>
      <td>Glycosphingolipid biosynthesis – globo series</td>
      <td>16/16</td>
      <td>0.019832034</td>
      <td>0.061724814</td>
      <td>0.534287429</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00534</td>
      <td>Glycosaminoglycan biosynthesis – heparan sulfate/heparin</td>
      <td>24/24</td>
      <td>0.020491524</td>
      <td>0.061724814</td>
      <td>0.471378176</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00270</td>
      <td>Cysteine and methionine metabolism</td>
      <td>46/48</td>
      <td>0.020959507</td>
      <td>0.061724814</td>
      <td>0.601864913</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01100</td>
      <td>Metabolic pathways</td>
      <td>1303/1315</td>
      <td>0.022419002</td>
      <td>0.061724814</td>
      <td>0.683947211</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00531</td>
      <td>Glycosaminoglycan degradation</td>
      <td>21/21</td>
      <td>0.023139686</td>
      <td>0.061724814</td>
      <td>0.911753864</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00604</td>
      <td>Glycosphingolipid biosynthesis – ganglio series</td>
      <td>15/15</td>
      <td>0.023268716</td>
      <td>0.061724814</td>
      <td>0.457285673</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00250</td>
      <td>Alanine, aspartate, and glutamate metabolism</td>
      <td>36/37</td>
      <td>0.023685519</td>
      <td>0.061724814</td>
      <td>0.942661129</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00240</td>
      <td>Pyrimidine metabolism</td>
      <td>101/104</td>
      <td>0.024235887</td>
      <td>0.061724814</td>
      <td>0.308135641</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00130</td>
      <td>Ubiquinone and other terpenoid-quinone biosynthesis</td>
      <td>11/11</td>
      <td>0.024630584</td>
      <td>0.061724814</td>
      <td>0.40991964</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00330</td>
      <td>Arginine and proline metabolism</td>
      <td>49/50</td>
      <td>0.025088792</td>
      <td>0.061724814</td>
      <td>0.479554867</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00564</td>
      <td>Glycerophospholipid metabolism</td>
      <td>94/94</td>
      <td>0.025448859</td>
      <td>0.061724814</td>
      <td>0.498146256</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00910</td>
      <td>Nitrogen metabolism</td>
      <td>17/17</td>
      <td>0.025782601</td>
      <td>0.061724814</td>
      <td>1.765582115</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00982</td>
      <td>Drug metabolism – cytochrome P450</td>
      <td>67/67</td>
      <td>0.027201304</td>
      <td>0.061724814</td>
      <td>0.620562175</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00785</td>
      <td>Lipoic acid metabolism</td>
      <td>3/3</td>
      <td>0.027507553</td>
      <td>0.061724814</td>
      <td>0.133403173</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00051</td>
      <td>Fructose and mannose metabolism</td>
      <td>35/35</td>
      <td>0.029679889</td>
      <td>0.061724814</td>
      <td>0.652646241</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00561</td>
      <td>Glycerolipid metabolism</td>
      <td>59/59</td>
      <td>0.030468773</td>
      <td>0.061724814</td>
      <td>0.4155946</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00512</td>
      <td>Mucin type O-glycan biosynthesis</td>
      <td>28/28</td>
      <td>0.030540327</td>
      <td>0.061724814</td>
      <td>0.472458211</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00052</td>
      <td>Galactose metabolism</td>
      <td>32/32</td>
      <td>0.031376559</td>
      <td>0.061724814</td>
      <td>0.42838689</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01230</td>
      <td>Biosynthesis of amino acids</td>
      <td>78/78</td>
      <td>0.031800904</td>
      <td>0.061724814</td>
      <td>0.942661129</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00533</td>
      <td>Glycosaminoglycan biosynthesis – keratan sulfate</td>
      <td>14/14</td>
      <td>0.031872109</td>
      <td>0.061724814</td>
      <td>0.27544313</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00900</td>
      <td>Terpenoid backbone biosynthesis</td>
      <td>22/23</td>
      <td>0.032232321</td>
      <td>0.061724814</td>
      <td>0.320850492</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00730</td>
      <td>Thiamine metabolism</td>
      <td>15/15</td>
      <td>0.032265244</td>
      <td>0.061724814</td>
      <td>0.323024942</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00500</td>
      <td>Starch and sucrose metabolism</td>
      <td>33/33</td>
      <td>0.033413545</td>
      <td>0.062178073</td>
      <td>0.452533726</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00770</td>
      <td>Pantothenate and CoA biosynthesis</td>
      <td>18/18</td>
      <td>0.033915312</td>
      <td>0.062178073</td>
      <td>0.307590054</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00062</td>
      <td>Fatty acid elongation</td>
      <td>27/27</td>
      <td>0.035703854</td>
      <td>0.062200773</td>
      <td>0.536297353</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00592</td>
      <td>Alpha-linolenic acid metabolism</td>
      <td>25/25</td>
      <td>0.035861114</td>
      <td>0.062200773</td>
      <td>0.568488547</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00562</td>
      <td>Inositol phosphate metabolism</td>
      <td>70/70</td>
      <td>0.037060597</td>
      <td>0.062200773</td>
      <td>0.197317479</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00760</td>
      <td>Nicotinate and nicotinamide metabolism</td>
      <td>34/35</td>
      <td>0.037777703</td>
      <td>0.062200773</td>
      <td>0.44361797</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00740</td>
      <td>Riboflavin metabolism</td>
      <td>8/8</td>
      <td>0.038531607</td>
      <td>0.062200773</td>
      <td>0.336638606</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00670</td>
      <td>One carbon pool by folate</td>
      <td>19/19</td>
      <td>0.039807001</td>
      <td>0.062200773</td>
      <td>0.293141874</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00310</td>
      <td>Lysine degradation</td>
      <td>57/59</td>
      <td>0.040221284</td>
      <td>0.062200773</td>
      <td>0.409052131</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00010</td>
      <td>Glycolysis/gluconeogenesis</td>
      <td>66/66</td>
      <td>0.040372513</td>
      <td>0.062200773</td>
      <td>0.4474754</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00053</td>
      <td>Ascorbate and aldarate metabolism</td>
      <td>27/27</td>
      <td>0.040535303</td>
      <td>0.062200773</td>
      <td>0.319047565</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00030</td>
      <td>Pentose phosphate pathway</td>
      <td>32/32</td>
      <td>0.040995964</td>
      <td>0.062200773</td>
      <td>0.316347941</td>
      <td>Down</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Cellular metabolic pathways regulated on protein level by inflammation in adrenocortical cells.The pathway analysis of differentially expressed proteins was done with the software package EGSEA and queried against the KEGG pathways repository. Pathways with p<0.05 are shown.


<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Metabolic pathway</th>
      <th>Number of detected proteins</th>
      <th>p-Value</th>
      <th>padj</th>
      <th>avg.logfc</th>
      <th>Direction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mmu00534</td>
      <td>Glycosaminoglycan biosynthesis – heparan sulfate/heparin</td>
      <td>4/24</td>
      <td>1.50E-07</td>
      <td>1.29E-05</td>
      <td>0.13</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00280</td>
      <td>Valine, leucine, and isoleucine degradation</td>
      <td>37/57</td>
      <td>5.20E-07</td>
      <td>2.23E-05</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00983</td>
      <td>Drug metabolism – other enzymes</td>
      <td>25/92</td>
      <td>3.80E-05</td>
      <td>0.000856142</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00562</td>
      <td>Inositol phosphate metabolism</td>
      <td>19/72</td>
      <td>5.89E-05</td>
      <td>0.000856142</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00260</td>
      <td>Glycine, serine, and threonine metabolism</td>
      <td>19/40</td>
      <td>6.89E-05</td>
      <td>0.000856142</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00240</td>
      <td>Pyrimidine metabolism</td>
      <td>25/58</td>
      <td>6.98E-05</td>
      <td>0.000856142</td>
      <td>0.04</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00982</td>
      <td>Drug metabolism – cytochrome P450</td>
      <td>16/71</td>
      <td>7.76E-05</td>
      <td>0.000856142</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00230</td>
      <td>Purine metabolism</td>
      <td>44/133</td>
      <td>7.96E-05</td>
      <td>0.000856142</td>
      <td>0.04</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00790</td>
      <td>Folate biosynthesis</td>
      <td>9/26</td>
      <td>9.75E-05</td>
      <td>0.000931452</td>
      <td>0.09</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu01100</td>
      <td>Metabolic pathways</td>
      <td>593/1608</td>
      <td>0.000134694</td>
      <td>0.001151176</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00190</td>
      <td>Oxidative phosphorylation</td>
      <td>70/135</td>
      <td>0.000160368</td>
      <td>0.001151176</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00980</td>
      <td>Metabolism of xenobiotics by cytochrome P450</td>
      <td>19/73</td>
      <td>0.000175997</td>
      <td>0.001151176</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01240</td>
      <td>Biosynthesis of cofactors</td>
      <td>74/154</td>
      <td>0.000178113</td>
      <td>0.001151176</td>
      <td>0.04</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00730</td>
      <td>Thiamine metabolism</td>
      <td>5/15</td>
      <td>0.000187401</td>
      <td>0.001151176</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00020</td>
      <td>Citrate cycle (TCA cycle)</td>
      <td>30/32</td>
      <td>0.00020177</td>
      <td>0.001156812</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01200</td>
      <td>Carbon metabolism</td>
      <td>81/121</td>
      <td>0.000404805</td>
      <td>0.002175826</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00760</td>
      <td>Nicotinate and nicotinamide metabolism</td>
      <td>11/41</td>
      <td>0.000459649</td>
      <td>0.002325283</td>
      <td>0.04</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00860</td>
      <td>Porphyrin and chlorophyll metabolism</td>
      <td>19/43</td>
      <td>0.000549279</td>
      <td>0.002624333</td>
      <td>0.04</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00360</td>
      <td>Phenylalanine metabolism</td>
      <td>7/23</td>
      <td>0.000744591</td>
      <td>0.003370253</td>
      <td>0.01</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00630</td>
      <td>Glyoxylate and dicarboxylate metabolism</td>
      <td>20/32</td>
      <td>0.000794408</td>
      <td>0.003415956</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00480</td>
      <td>Glutathione metabolism</td>
      <td>28/72</td>
      <td>0.001037994</td>
      <td>0.004250832</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00061</td>
      <td>Fatty acid biosynthesis</td>
      <td>12/19</td>
      <td>0.00119934</td>
      <td>0.004323466</td>
      <td>0.04</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00052</td>
      <td>Galactose metabolism</td>
      <td>17/32</td>
      <td>0.001212032</td>
      <td>0.004323466</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00350</td>
      <td>Tyrosine metabolism</td>
      <td>12/40</td>
      <td>0.001275764</td>
      <td>0.004323466</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00900</td>
      <td>Terpenoid backbone biosynthesis</td>
      <td>8/23</td>
      <td>0.001283046</td>
      <td>0.004323466</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00140</td>
      <td>Steroid hormone biosynthesis</td>
      <td>12/92</td>
      <td>0.001307094</td>
      <td>0.004323466</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00511</td>
      <td>Other glycan degradation</td>
      <td>11/18</td>
      <td>0.001620057</td>
      <td>0.005160182</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00520</td>
      <td>Amino sugar and nucleotide sugar metabolism</td>
      <td>29/51</td>
      <td>0.001922509</td>
      <td>0.005904848</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00040</td>
      <td>Pentose and glucuronate interconversions</td>
      <td>9/35</td>
      <td>0.002291756</td>
      <td>0.006796243</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00620</td>
      <td>Pyruvate metabolism</td>
      <td>34/44</td>
      <td>0.004741112</td>
      <td>0.013428366</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00524</td>
      <td>Neomycin, kanamycin, and gentamicin biosynthesis</td>
      <td>3/5</td>
      <td>0.004840458</td>
      <td>0.013428366</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00053</td>
      <td>Ascorbate and aldarate metabolism</td>
      <td>9/31</td>
      <td>0.005220665</td>
      <td>0.013429037</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00830</td>
      <td>Retinol metabolism</td>
      <td>8/97</td>
      <td>0.005279453</td>
      <td>0.013429037</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00531</td>
      <td>Glycosaminoglycan degradation</td>
      <td>10/21</td>
      <td>0.005309154</td>
      <td>0.013429037</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00450</td>
      <td>Selenocompound metabolism</td>
      <td>9/17</td>
      <td>0.006951355</td>
      <td>0.017080471</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00250</td>
      <td>Alanine, aspartate, and glutamate metabolism</td>
      <td>17/39</td>
      <td>0.007955263</td>
      <td>0.019004239</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01230</td>
      <td>Biosynthesis of amino acids</td>
      <td>45/79</td>
      <td>0.008873164</td>
      <td>0.020624111</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu01212</td>
      <td>Fatty acid metabolism</td>
      <td>40/62</td>
      <td>0.009336325</td>
      <td>0.021129578</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00500</td>
      <td>Starch and sucrose metabolism</td>
      <td>14/34</td>
      <td>0.011170016</td>
      <td>0.024631316</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00514</td>
      <td>Other types of O-glycan biosynthesis</td>
      <td>15/43</td>
      <td>0.011876496</td>
      <td>0.025349557</td>
      <td>0.04</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu01210</td>
      <td>2-Oxocarboxylic acid metabolism</td>
      <td>11/20</td>
      <td>0.01227639</td>
      <td>0.025349557</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00650</td>
      <td>Butanoate metabolism</td>
      <td>13/28</td>
      <td>0.012404185</td>
      <td>0.025349557</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00670</td>
      <td>One carbon pool by folate</td>
      <td>9/19</td>
      <td>0.012674778</td>
      <td>0.025349557</td>
      <td>0.05</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00310</td>
      <td>Lysine degradation</td>
      <td>20/64</td>
      <td>0.01401052</td>
      <td>0.027384197</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00590</td>
      <td>Arachidonic acid metabolism</td>
      <td>9/86</td>
      <td>0.015253177</td>
      <td>0.029150517</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00770</td>
      <td>Pantothenate and CoA biosynthesis</td>
      <td>8/21</td>
      <td>0.016632522</td>
      <td>0.031095584</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00592</td>
      <td>Alpha-linolenic acid metabolism</td>
      <td>3/25</td>
      <td>0.017819371</td>
      <td>0.032605657</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00780</td>
      <td>Biotin metabolism</td>
      <td>3/3</td>
      <td>0.018650597</td>
      <td>0.033415653</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00640</td>
      <td>Propanoate metabolism</td>
      <td>25/31</td>
      <td>0.020182799</td>
      <td>0.035173564</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00290</td>
      <td>Valine, leucine, and isoleucine biosynthesis</td>
      <td>2/4</td>
      <td>0.02053428</td>
      <td>0.035173564</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00920</td>
      <td>Sulfur metabolism</td>
      <td>7/11</td>
      <td>0.021206387</td>
      <td>0.035173564</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00062</td>
      <td>Fatty acid elongation</td>
      <td>15/19</td>
      <td>0.021267736</td>
      <td>0.035173564</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00604</td>
      <td>Glycosphingolipid biosynthesis – ganglio series</td>
      <td>5/15</td>
      <td>0.022065753</td>
      <td>0.035804807</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00563</td>
      <td>Glycosylphosphatidylinositol (GPI)-anchor biosynthesis</td>
      <td>8/26</td>
      <td>0.023553511</td>
      <td>0.036186307</td>
      <td>0.04</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00750</td>
      <td>Vitamin B6 metabolism</td>
      <td>3/9</td>
      <td>0.023553511</td>
      <td>0.036186307</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00220</td>
      <td>Arginine biosynthesis</td>
      <td>7/20</td>
      <td>0.024245413</td>
      <td>0.036186307</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00270</td>
      <td>Cysteine and methionine metabolism</td>
      <td>29/53</td>
      <td>0.025410276</td>
      <td>0.036186307</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>mmu00051</td>
      <td>Fructose and mannose metabolism</td>
      <td>17/36</td>
      <td>0.02551991</td>
      <td>0.036186307</td>
      <td>0.04</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00071</td>
      <td>Fatty acid degradation</td>
      <td>30/52</td>
      <td>0.025667032</td>
      <td>0.036186307</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00330</td>
      <td>Arginine and proline metabolism</td>
      <td>23/54</td>
      <td>0.025667032</td>
      <td>0.036186307</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00561</td>
      <td>Glycerolipid metabolism</td>
      <td>23/62</td>
      <td>0.025667032</td>
      <td>0.036186307</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00010</td>
      <td>Glycolysis/gluconeogenesis</td>
      <td>40/67</td>
      <td>0.050728869</td>
      <td>0.068166917</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00030</td>
      <td>Pentose phosphate pathway</td>
      <td>17/33</td>
      <td>0.050728869</td>
      <td>0.068166917</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>mmu00410</td>
      <td>Beta-alanine metabolism</td>
      <td>19/32</td>
      <td>0.050728869</td>
      <td>0.068166917</td>
      <td>0.01</td>
      <td>Down</td>
    </tr>
  </tbody>
</table>

### Inflammation disrupts the TCA cycle in adrenocortical cells at the levels of isocitrate dehydrogenase and SDH

Inflammation downregulates the TCA cycle and oxidative phosphorylation in inflammatory activated macrophages (Ryan and O’Neill, 2020), however little is known about inflammation-induced metabolic changes in other cell types. We show that TCA cycle-related gene expression was downregulated in the adrenal cortex of LPS-treated mice (Figure 2A and B; Table 1). Expression of genes encoding key TCA cycle enzymes, including SDH Sdhb and Sdhc, isocitrate dehydrogenases 2 and 3 (Idh2 and Idh3b), and malate dehydrogenase 1 (Mdh1), was reduced in the adrenal cortex of LPS-injected mice (Figure 2B). Proteomic GSEA confirmed the TCA cycle downregulation in steroidogenic adrenocortical cells of LPS mice (Figure 2C, Table 2). Accordingly, CD31-CD45- adrenocortical cells from LPS-treated mice displayed reduced Idh1, Idh2, Sdhb, and Sdhc expression (Figure 2D and E) and LPS treatment attenuated the IDH and SDH enzymatic activities in the adrenal cortex (Figure 2F and G). Additionally, immunofluorescent staining showed that IDH2 and SDHB proteins are highly expressed in SF-1+ (steroidogenic) cells (Figure 2H, I). In endothelial and immune cells of the adrenal cortex of LPS-treated mice, Idh1 and Idh2 gene expression was reduced, Sdhb gene expression was increased, while expression of Sdhc was unaltered (Figure 2—figure supplement 1A and B). Collectively, these data indicate that the reduced activity of SDH in the adrenal cortex of LPS-treated mice is mainly due to its downregulated expression in steroidogenic adrenocortical cells.

![Figure 2.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig2-v2.jpg)

**Figure 2.:** (A,B) Transcriptome analysis in the microdissected adrenal gland cortex of mice treated for 6 hr with PBS or LPS (n=3 mice per group). (A) Gene set enrichment analysis (GSEA) for TCA cycle genes. (B) Heatmap of differentially expressed TCA cycle genes (padj <0.05). (C) GSEA analysis for TCA cycle proteins in CD31-CD45- adrenocortical cells of mice treated for 24 hr with PBS or LPS (n=6 mice per group). (D,E) mRNA expression of Idh1, Idh2, Sdhb, and Sdhc in adrenocortical CD31-CD45- cells of mice treated for 6 hr with PBS or LPS (n=8 mice per group, shown one from two experiments). (F,G) Quantification of IDH and SDH activities in the adrenal cortex of mice treated for 24 hr with LPS or PBS (n=6 mice per group). Values are normalized to the total protein amount in the adrenal cortex. (H,I) Immunofluorescence images of the adrenal gland, stained for IDH2 (red) or SDHB (red), SF-1 (magenta), Isolectin (staining endothelial cells, green), and DAPI (blue). Scale bar, 30 μm. (J–O) TCA cycle metabolites (isocitrate, α-ketoglutarate, succinate, fumarate) were measured by LC-MS/MS in adrenal glands of mice 24 hr after injection with PBS or LPS (n=4 mice per group, shown one from two experiments). (P,Q) MALDI-MSI for isocitrate and succinate in the adrenal cortex of mice treated for 24 hr with PBS or LPS (n=3 mice per group). Representative images and quantifications are shown. Scale bar, 500 μm. Data in (D–G,J–Q) are presented as mean ±s.d. Statistical analysis was done with two-tailed Mann-Whitney test (D–G) or one-tailed Mann-Whitney test (J–Q). *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001. NES: normalized enrichment score.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** mRNA expression of Idh1, Idh2, Sdhb, and Sdhc in endothelial (CD31+) (A) and immune (CD45+) cells (B) sorted from adrenal glands of mice treated for 6 hr with PBS or LPS (n=6–8 mice per group, shown one from two experiments). Data are presented as mean ± s.d. Statistical analysis was done with two-tailed Mann-Whitney test. *p<0.05, **p<0.01, ***p<0.001.

In order to confirm that inflammation disrupts the TCA cycle in adrenocortical cells, we profiled the changes in metabolite levels in the adrenal glands of PBS- and LPS-treated mice using liquid chromatography-tandem mass spectrometry (LC-MS/MS). The levels of isocitrate and succinate, as well as the ratios of isocitrate/α-ketoglutarate and succinate/fumarate were increased in the adrenal glands of LPS-treated mice (Figure 2J–O). Furthermore, MALDI mass spectrometry imaging (MALDI-MSI) confirmed the increased levels of isocitrate and succinate in the adrenal cortex of LPS mice (Figure 2P and Q). These data collectively demonstrate that inflammation disrupts IDH and SDH activities and increases the levels of their substrates isocitrate and succinate in adrenocortical cells.

### Inflammation reduces oxidative phosphorylation and increases oxidative stress in the adrenal cortex

Next, we investigated how inflammation affects mitochondrial oxidative metabolism in adrenocortical cells. GSEA of the RNA-Seq and proteomic data in the adrenal cortex and CD31-CD45- adrenocortical cells, respectively, revealed that oxidative phosphorylation was significantly enriched among the downregulated genes (Figure 3A) and proteins (Figure 3B), and expression of a large number of oxidative phosphorylation-associated genes was reduced in the adrenal cortex of LPS mice (Figure 3C). In accordance, ATP levels were reduced in the adrenal gland (Figure 3D) and the mitochondrial membrane potential of CD31-CD45- adrenocortical cells was decreased in mice treated with LPS (Figure 3E). In pro-inflammatory macrophages, a TCA cycle ‘break’ at the level of SDH is associated with repurposing of mitochondria from oxidative phosphorylation-mediated ATP synthesis to ROS production (Mills et al., 2016). EGSEA pathway analysis showed that upon LPS treatment several pathways involved in the regulation of and the cellular response to oxidative stress in the adrenal cortex were enriched at mRNA (Table 3) and protein level (Table 4). This was confirmed by increased 4-hydroxynonenal (4-HNE) staining, indicating higher oxidative stress-associated damage in the adrenal cortex of LPS-treated mice (Figure 3F). Antioxidant defense mechanisms are particularly important in the adrenal cortex, since electron leakage through the reactions catalyzed by CYP11A1 and CYP11B1 during glucocorticoid synthesis contributes significantly to mitochondrial ROS production (Prasad et al., 2014). Cells neutralize ROS to maintain their cellular redox environment by using the reducing equivalents NADPH and glutathione (Xiao and Loscalzo, 2020). In addition, NADPH serves as a cofactor for mitochondrial steroidogenic enzymes (Frederiks et al., 2007). NADPH levels and glutathione metabolism-related gene expression were significantly decreased in the adrenal glands of LPS mice (Figure 3G and H; Table 1, Table 2). These findings collectively suggest that inflammation in the adrenal cortex is associated with increased oxidative stress, perturbed mitochondrial oxidative metabolism, reduced antioxidant capacity, and increased ROS production.

![Figure 3.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig3-v2.jpg)

**Figure 3.:** (A) Gene set enrichment analysis (GSEA) for oxidative phosphorylation-related genes in the adrenal cortex of mice treated for 6 hr with PBS or LPS (n=3 mice per group). (B) GSEA for oxidative phosphorylation-associated proteins in CD31-CD45- adrenocortical cells of mice treated for 24 hr with PBS or LPS (n=6 mice per group). (C) Heatmap of differentially expressed genes related to oxidative phosphorylation (padj <0.05). (D) Measurement of ATP in adrenal glands of mice treated for 24 hr with PBS or LPS (n=10–11 mice per group, pooled from two experiments). (E) Measurement of mitochondrial membrane potential by TMRE staining and mitochondrial load by Mitotracker Green FM in CD31-CD45-adrenocortical cells of PBS or LPS mice. Data are presented as ratio of the median fluorescence intensities of TMRE to Mitotracker Green FM (n=6 mice per group). (F) Representative immunofluorescence images of adrenal gland sections from PBS- and LPS-treated mice (24 hr post-injection), stained for 4-hydroxynonenal (4-HNE) (magenta) and DAPI (blue). Scale bar, 300 μm. Quantification of the mean fluorescence intensity of 4-HNE staining in the adrenal cortex of PBS- or LPS-treated mice (n=6 mice per group). (G) NADPH measurement by liquid chromatography-tandem mass spectrometry (LC-MS/MS) in adrenal glands of mice treated with PBS or LPS for 24 hr (n=8 mice per group). Data are given as observed peak area intensities of NADPH. (H) GSEA for glutathione metabolism of RNA-Seq data in the adrenal cortex of LPS versus PBS mice (n=3 mice per group). Data in (D–G) present mean ± s.d. Statistical analysis was done with two-tailed Mann-Whitney test. *p<0.05, **p<0.01. NES: normalized enrichment score.

**Table 3.**
 ROS pathways are transcriptionally upregulated in the adrenal cortex of LPS-treated mice.The pathway analysis of differentially expressed genes was done with the software package EGSEA and queried against the GO gene sets repository. Pathways with padj. <0.05 are shown.


<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Gene set</th>
      <th>Number of expressed genes</th>
      <th>p-Value</th>
      <th>padj</th>
      <th>avg.logfc</th>
      <th>Direc tion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M13446</td>
      <td>GO Regulation of reactive oxygen species metabolic process</td>
      <td>271/275</td>
      <td>3.75E-08</td>
      <td>1.26E-06</td>
      <td>1.0100</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M13580</td>
      <td>GO Positive regulation of reactive oxygen species metabolic process</td>
      <td>182/186</td>
      <td>2.33E-07</td>
      <td>6.26E-06</td>
      <td>1.0100</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M16953</td>
      <td>GO Response to reactive oxygen species</td>
      <td>300/317</td>
      <td>0.003422132</td>
      <td>0.009035375</td>
      <td>0.8600</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M16581</td>
      <td>GO Cellular response to reactive oxygen species</td>
      <td>173/177</td>
      <td>0.002537297</td>
      <td>0.009035375</td>
      <td>0.7600</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M10618</td>
      <td>GO Negative regulation of response to reactive oxygen species</td>
      <td>24/24</td>
      <td>0.0072384</td>
      <td>0.010942115</td>
      <td>0.7100</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M15379</td>
      <td>GO Regulation of reactive oxygen species biosynthetic process</td>
      <td>145/148</td>
      <td>5.90E-05</td>
      <td>0.000770609</td>
      <td>0.7000</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M10827</td>
      <td>GO Positive regulation of reactive oxygen species biosynthetic process</td>
      <td>120/123</td>
      <td>0.000465606</td>
      <td>0.00454261</td>
      <td>0.7000</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M15990</td>
      <td>GO Reactive oxygen species metabolic process</td>
      <td>163/167</td>
      <td>0.008936465</td>
      <td>0.012568942</td>
      <td>0.6700</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M16764</td>
      <td>GO Regulation of response to reactive oxygen species</td>
      <td>43/43</td>
      <td>0.006753207</td>
      <td>0.010498628</td>
      <td>0.6200</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>M16007</td>
      <td>GO Negative regulation of reactive oxygen species biosynthetic process</td>
      <td>23/23</td>
      <td>0.016434387</td>
      <td>0.020274996</td>
      <td>0.6000</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M12185</td>
      <td>GO Reactive oxygen species biosynthetic process</td>
      <td>32/33</td>
      <td>0.006483259</td>
      <td>0.01024232</td>
      <td>0.5700</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>M10894</td>
      <td>GO Negative regulation of reactive oxygen species metabolic process</td>
      <td>59/59</td>
      <td>0.006538654</td>
      <td>0.010287661</td>
      <td>0.5500</td>
      <td>Up</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 ROS-related protein expression is upregulated in the adrenal cortex of LPS-treated mice.The pathway analysis of differentially expressed proteins was done with the software package EGSEA and queried against the GO gene sets repository. Pathways with padj. <0.05 are shown.


<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Protein set</th>
      <th>Number of detected proteins</th>
      <th>p-Value</th>
      <th>padj</th>
      <th>avg.logfc</th>
      <th>Direc-tion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M13446</td>
      <td>GO REGULATION OF REACTIVE OXYGEN SPECIES METABOLIC PROCESS</td>
      <td>62/275</td>
      <td>6.30E-06</td>
      <td>0.00012401</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M15379</td>
      <td>GO REGULATION OF REACTIVE OXYGEN SPECIES BIOSYNTHETIC PROCESS</td>
      <td>34/148</td>
      <td>9.43E-06</td>
      <td>0.00014372</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M13580</td>
      <td>GO POSITIVE REGULATION OF REACTIVE OXYGEN SPECIES METABOLIC PROCESS</td>
      <td>29/186</td>
      <td>1.11E-05</td>
      <td>0.00015778</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M10827</td>
      <td>GO POSITIVE REGULATION OF REACTIVE OXYGEN SPECIES BIOSYNTHETIC PROCESS</td>
      <td>20/123</td>
      <td>1.17E-05</td>
      <td>0.00016203</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M10894</td>
      <td>GO NEGATIVE REGULATION OF REACTIVE OXYGEN SPECIES METABOLIC PROCESS</td>
      <td>23/59</td>
      <td>5.29E-05</td>
      <td>0.00037856</td>
      <td>0.05</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>M16007</td>
      <td>GO NEGATIVE REGULATION OF REACTIVE OXYGEN SPECIES BIOSYNTHETIC PROCESS</td>
      <td>12/23</td>
      <td>0.00014126</td>
      <td>0.00073167</td>
      <td>0.07</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M16581</td>
      <td>GO CELLULAR RESPONSE TO REACTIVE OXYGEN SPECIES</td>
      <td>50/177</td>
      <td>0.00015378</td>
      <td>0.00077551</td>
      <td>0.03</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>M15990</td>
      <td>GO REACTIVE OXYGEN SPECIES METABOLIC PROCESS</td>
      <td>35/167</td>
      <td>0.00037436</td>
      <td>0.00150479</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
    <tr>
      <td>M16953</td>
      <td>GO RESPONSE TO REACTIVE OXYGEN SPECIES</td>
      <td>83/317</td>
      <td>0.00076076</td>
      <td>0.00262274</td>
      <td>0.03</td>
      <td>Up</td>
    </tr>
    <tr>
      <td>M12185</td>
      <td>GO REACTIVE OXYGEN SPECIES BIOSYNTHETIC PROCESS</td>
      <td>9/33</td>
      <td>0.00192844</td>
      <td>0.00545214</td>
      <td>0.02</td>
      <td>Down</td>
    </tr>
  </tbody>
</table>

### Increased succinate levels impair mitochondrial metabolism and steroidogenesis in adrenocortical cells

SDH is complex II of the electron transport chain (ETC), coupling succinate oxidation with the respiratory chain (Midzak and Papadopoulos, 2016). Inhibition of SDH function with dimethyl malonate (DMM), which is hydrolyzed to the competitive SDH inhibitor malonate (Mills et al., 2016; Moosavi et al., 2020), or treatment of adrenocortical cells with the cell-permeable succinate analog diethyl succinate (DES) increased the amount of succinate and the succinate/fumarate ratio in adrenal gland explants (Figure 4A) and human adrenocortical carcinoma cells NCI-H295R (Figure 4B). Additionally, both treatments decreased the oxygen consumption rate (OCR) and ATP production in adrenocortical cells (Figure 4C and D). This was associated with reduced mitochondrial membrane potential (Figure 4E), but not mitochondrial load (Figure 4F). Furthermore, DMM increased ROS (Figure 4G) and decreased the NADPH/NADP+ ratio (Figure 4H), suggesting that in adrenocortical cells, as in macrophages (Mills et al., 2016), succinate repurposes mitochondrial metabolism from oxidative phosphorylation toward ROS production. Such changes in the mitochondrial function were not observed when inhibiting IDH activity with enasidenib (AG221) (Yen et al., 2017; Figure 4I–K). AG221 increased isocitrate and the isocitrate/α-ketoglutarate ratio (Figure 4I), but did not affect OCR (Figure 4J) or the mitochondrial membrane potential (Figure 4K).

![Figure 4.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig4-v2.jpg)

**Figure 4.:** (A,B) Succinate and fumarate levels were measured by liquid chromatography-tandem mass spectrometry (LC-MS/MS) in adrenal gland explants (A) and NCI-H295R cells (B) treated with dimethyl malonate (DMM) or diethyl succinate (DES) for 24 hr (n=5 for (A) and n=4 for (B)). (C) Oxygen consumption rate (OCR) measurement with Seahorse technology in NCI-H295R cells treated with DMM or DES for 24 hr (n=6). (D) Measurement of ATP/ADP ratio in NCI-H295R cells treated with DMM or DES for 24 hr (n=4–12). (E,F) TMRE and Mitotracker Green FM staining assessed by flow cytometry in NCI-H295R cells treated with DES for 4 hr, MFI is shown (n=7 for (E) and n=4, one from two experiments for (F)). (G) ROS measurement in NCI-H295R cells treated with DMM or DES for 2 hr (n=10–12). (H) Measurement of NADPH/NADP+ ratio in NCI-H295R cells treated with DMM for 24 hr (n=3–4). (I) Isocitrate levels measured by LC-MS/MS in NCI-H295R cells treated for 24 hr with AG221 or DMSO (n=6). (J) OCR measurement in NCI-H295R cells treated for 24 hr with AG221 or DMSO (n=10). (K) TMRE staining and flow cytometry in NCI-H295R cells treated for 4 hr with AG221 or DMSO, MFI is shown (n=7). Data in (A–B,D–I,K) are presented as mean ± s.d. Data in (C,J) are presented as mean ± s.e.m. Statistical analysis was done with one-way ANOVA (A, G) or two-tailed (B,D,E,F,I,K) or one-tailed (H) Mann-Whitney test. *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001.

Key steps of steroidogenesis take place in the mitochondria (Midzak and Papadopoulos, 2016), thus, we asked whether disruption of SDH activity affects steroidogenic function. We inhibited SDH activity with DMM in human and mouse adrenocortical cells, and induced glucocorticoid production by forskolin or ACTH, respectively. SDH inhibition considerably impaired glucocorticoid and progesterone production in mouse primary adrenocortical cells (Figure 5A and B), adrenal gland explants (Figure 5C–E), and human adrenocortical NCI-H295R cells (Figure 5—figure supplement 1A and B). Similarly, DES diminished glucocorticoid production in mouse (Figure 5A and B) and human adrenocortical cells (Figure 5—figure supplement 1A and B). Confirming these data, Sdhb silencing (Figure 5—figure supplement 2A and B) impaired glucocorticoid synthesis in mouse (Figure 5F–H) and human adrenocortical cells (Figure 5—figure supplement 1C), implying that proper adrenocortical steroidogenesis relies on intact SDH activity. Recently it was shown that SDH activity and intracellular succinate are required for CYP11A1-mediated pregnenolone synthesis, the first step of steroidogenesis (Bose et al., 2020). Adding to this knowledge, our data demonstrate that increasing succinate concentrations impair steroidogenesis (Figure 5—figure supplement 1D–F). Moreover, the proton gradient uncoupler FCCP (Figure 5I) and the ATP synthase inhibitor oligomycin (Figure 5J–M) both strongly reduced steroidogenesis in adrenocortical cells (Figure 5I–M), demonstrating the well-established requirement of intact mitochondrial membrane potential and ATP generation for steroidogenic function (Bose et al., 2020; King et al., 1999). We also asked whether oxidative stress mediates the effect of SDH inhibition on steroidogenesis. Reducing ROS with the antioxidant analog of vitamin E Trolox (Figure 5N) partially reversed the effect of DMM on cortisol and 11-deoxycortisol production (Figure 5O–P), suggesting that increased ROS (Figure 4G) contributes to impairment of steroidogenesis upon SDH blockage. In accordance, DMM and DES downregulated the expression of Cyp11a1 and Cyp11b1 (Figure 5Q and R), that catalyze the conversion of cholesterol to pregnenolone and the final step of corticosterone/cortisol production, respectively (Midzak and Papadopoulos, 2016; Payne and Hales, 2004). However, the corticosterone/11-deoxycorticosterone ratio reflecting CYP11B1 activity was not affected by Sdhb silencing (Figure 5—figure supplement 1G). Importantly, treatment of adrenal gland explants with LPS reduced corticosterone secretion in response to ACTH, similar to DMM of DES (Figure 5S), albeit without affecting the corticosterone/11-deoxycorticosterone ratio (Figure 5—figure supplement 1H). In contrast to SDH blockage, inhibition of IDH activity with AG221 (Figure 4I) did not alter glucocorticoid production in mouse adrenocortical cells (Figure 5—figure supplement 3A and B), adrenal gland explants (Figure 5—figure supplement 3C and D), or human adrenocortical cells (Figure 5—figure supplement 3E and F), nor did Idh2 silencing in mouse adrenocortical cells (Figure 5—figure supplement 2C, figure supplement 3G,H). Taken together, these results imply that SDH but not IDH activity is required for adrenocortical steroidogenesis.

![Figure 5.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig5-v2.jpg)

**Figure 5.:** (A–E) Primary adrenocortical cells (A,B) and adrenal explants (C–E) were treated for 24 hr with dimethyl malonate (DMM) or diethyl succinate (DES) and for another 45 min with adrenocorticotropic hormone (ACTH) (10 ng/ml or 100 ng/ml, respectively) (n=5–6). (F–H) Primary adrenocortical cells were transfected with siSdhb or non-targeting siRNA (siCtrl) and 24 hr post-transfection they were treated for 45 min with ACTH (n=7–8). (I,J) NCI-H295R cells were treated for 24 hr with FCCP (I) or oligomycin (OM) (J) and for another 30 min with Forskolin (Fsk) (n=6). (K–M) Primary adrenocortical cells were treated for 24 hr with oligomycin (OM) and for another 45 min with ACTH (n=6). (N) ROS measurement in NCI-H295R cells pre-treated for 15 min with Trolox or control solution (DMSO) and then treated for 2 hr with DMM (n=3). (O,P) NCI-H295R cells pre-treated for 15 min with Trolox or DMSO were treated or not for 24 hr with DMM and Forskolin (n=6). (Q,R) Cyp11a1 and Cyp11b1 expression in primary adrenocortical cells treated for 24 hr with DMM or DES and for 45 min with ACTH (n=5–6). (S) Adrenal gland explants were treated for 24 hr with LPS and for 45 min with ACTH (n=4–5). Measurements of steroid hormones in (A–M,O,P,S) were performed in supernatants of primary adrenocortical cell cultures or adrenal gland explants by liquid chromatography-tandem mass spectrometry (LC-MS/MS). Data are presented as mean ± s.d. Statistical analysis was done with one-way ANOVA (A–E, I–M,S), Wilcoxon (F,G,H), one-tailed Mann-Whitney (N), or two-tailed Mann-Whitney test (O–R). *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001. BLD = below level of detection.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A,B) NCI-H295R cells were treated for 24 hr with dimethyl malonate (DMM) or diethyl succinate (DES) and for another 24 hr with Forskolin (Fsk) (n=6–12). (C) NCI-H295R cells were transfected with siSDHB or control siRNA (siCtrl) and 24 hr post-transfection they were treated for 24 hr with Forskolin (n=4). (D–F) NCI-H295R cells were treated for 24 hr with the indicated concentrations of DES and for another 24 hr with Forskolin (n=4). (G) Primary adrenocortical cells were transfected with siSdhb or non-targeting siRNA (siCtrl) and 24 hr post-transfection they were treated for 45 min with adrenocorticotropic hormone (ACTH) (n=8). (H) Adrenal gland explants were treated for 24 hr with LPS and for 45 min with ACTH (n=4–5). Measurements for indicated steroid hormones were performed in cell culture or adrenal explant supernatants by liquid chromatography-tandem mass spectrometry (LC-MS/MS). Data are presented as mean ± s.d. Statistical analysis was done with one-way ANOVA (A–C); two-way ANOVA (D–F), or two-tailed Mann-Whitney test (G,H). **p<0.01, ***p<0.001, ****p<0.0001. BLD = below level of detection.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Western blot analysis for SDHB in NCI-H295R cells transfected with 10, 30, or 50 nM siSDHB or siCtrl (24 hr post-transfection). α-TUBULIN was used as loading control. (B,C) mRNA expression of Sdhb and Idh2 in primary adrenocortical cells transfected for 24 hr with 10, 30, or 50 nM siSdhb, siIdh2, or siCtrl (n=3). (D) Dnmt1 expression in primary adrenocortical cells transfected for 24 hr with 30 nM siDnmt1 or siCtrl (n=5–6). (E) DNMT1 expression in NCI-H295R cells transfected for 48 hr with 30 nM siDNMT1 or siCtrl (n=2). (F) Western blot analysis for DNMT1 in NCI-H295R cells transfected with 30 nM siDNMT1 or siCtrl (48 hr post-transfection). β-Actin was used as loading control. Data in (B–E) are presented as mean ± s.d. Statistical analysis was done with two-way ANOVA (B,C) or one-way ANOVA (D). *p<0.05, **p<0.01, ****p<0.0001. Red boxes mark the concentrations with most efficient knock-down, which were chosen for further experiments. Full unedited blots for (A) and (F) are available in Figure 5—figure supplement 2—source data 1.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A,B) Primary adrenocortical cells were treated for 24 hr with AG221 or DMSO and for another 45 min with adrenocorticotropic hormone (ACTH) (n=2–6). (C,D) Adrenal gland explants were treated for 24 hr with AG221 or DMSO and for another 45 min with ACTH (n=2–4). (E,F) NCI-H295R cells were treated for 24 hr with AG221 or DMSO and for another 24 hr with Forskolin (n=4–6). (G,H) Primary adrenocortical cells were transfected with siIdh2 or siCtrl and 24 hr post-transfection they were treated for 45 min with ACTH (n=2–7). Measurements of steroid hormones were performed in supernatants of primary adrenocortical cell cultures, adrenal gland explants, or NCI-H295R cells by liquid chromatography-tandem mass spectrometry (LC-MS/MS). Data are presented as mean ± s.d. Statistical analysis was done with one-way ANOVA. ****p<0.0001. BLD = below level of detection.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A) mRNA expression of Acod1 in CD31-/CD45- and CD45+ cells sorted from adrenal cortex of mice treated for 6 hr with PBS or LPS (n=4–8 mice per group, shown one from two experiments). (B,C) Itaconate levels in CD31-/CD45- (B) and CD31+/CD45+ cells (C) sorted from adrenal glands of mice treated for 24 hr with PBS or LPS (n=8 mice per group, shown one from two experiments). (D–G) Itaconate, succinate, and fumarate levels and succinate/fumarate ratio in lysates of primary adrenocortical cells treated for 24 hr with 4-octyl itaconate (4-OI) (n=4). (H,I) Corticosterone and 11-deoxycorticosterone levels in the supernatant of primary adrenocortical cells treated for 24 hr with 4-OI (n=4). (J) Quantification of SDH activity in the adrenal cortex of Acod1-KO and wild-type mice treated for 16 hr with LPS (n=5–6 mice per group). Values are normalized to the total protein amount in the adrenal cortex. Data are presented as mean ± s.d. Statistical analysis was done with two-tailed Mann-Whitney test. *p<0.05, ***p<0.001.

### Itaconate is not responsible for reduced SDH activity and steroidogenesis in adrenocortical cells

In inflammatory macrophages, SDH function is inhibited by itaconate (Lampropoulou et al., 2016), a byproduct of the TCA cycle produced from cis-aconitate in a reaction catalyzed by aconitate decarboxylase 1 (ACOD1) (Michelucci et al., 2013). The expression of Acod1, the gene encoding for ACOD1, and itaconate levels are strongly upregulated in macrophages upon inflammation (Lampropoulou et al., 2016). We asked whether itaconate might affect SDH activity in the adrenal cortex. Acod1 expression was upregulated in the adrenal cortex of LPS-treated mice but this increase derived from CD45+ cells, while Acod1 was not expressed in CD31-CD45- adrenocortical cells (Figure 5—figure supplement 4A). Accordingly, LPS treatment significantly elevated itaconate levels in the CD31+CD45+ fraction, while it did not increase itaconate levels in CD31-CD45- adrenocortical cells (Figure 5—figure supplement 4B and C). Itaconate can be secreted from LPS-stimulated macrophages (Lampropoulou et al., 2016), and could thereby affect SDH activity in adrenocortical cells. Therefore, we tested whether exogenously given itaconate may affect steroidogenesis by treating primary adrenocortical cells with the cell-permeable itaconate derivative 4-octyl itaconate (4-OI). Adrenocortical cells internalized the added itaconate derivative (Figure 5—figure supplement 4D), which however did not alter succinate or fumarate levels or the succinate/fumarate ratio (Figure 5—figure supplement 4E–G), nor did it affect glucocorticoid production (Figure 5—figure supplement 4H–I). Additionally, SDH activity in the adrenal cortex of Acod1-KO mice injected with LPS was not different from that in their wild-type counterparts (Figure 5—figure supplement 4J). Hence, neither is itaconate produced nor does it affect SDH activity through paracrine routes in adrenocortical cells.

### IL-1β downregulates SDHB expression and steroidogenesis in a DNMT1-dependent manner

Systemic inflammation induces substantial leukocyte recruitment in the adrenal gland, accompanied by elevated production of pro-inflammatory cytokines (Chen et al., 2019a; Kanczkowski et al., 2013b). Among them, IL-1β is highly produced by inflammatory monocytes and macrophages (Netea et al., 2010). RNA-Seq in the adrenal cortex, including recruited immune cells, showed increased expression of Il1b in LPS- compared to PBS-injected mice (log2fold change [fc] = 1.46, padj = 0.019). Furthermore, there was significant positive enrichment of genes associated with IL-1β secretion in the adrenal cortex of mice treated with LPS (Figure 6A). The IL-1β receptor Il1r1 is expressed in CD31-CD45- adrenocortical cells and its expression was upregulated in adrenocortical cells sorted from LPS-treated mice (Figure 6B). In accordance, proteins related to IL-1β signaling were positively enriched in CD31-CD45- adrenocortical cells of LPS mice (Figure 6C). Essentially, IL-1β, but not IL-6 or TNFα, reduced SDHB expression in NCI-H295R cells (Figure 6D). Moreover, IL-1β decreased the ATP/ADP ratio (Figure 6E) and impaired ACTH-induced steroidogenesis in adrenocortical cells (Figure 6F–H), mimicking the effects of LPS (Figures 3D and 5S) and DMM/DES (Figures 4D and 5A–E).

![Figure 6.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig6-v2.jpg)

**Figure 6.:** (A) Gene set enrichment analysis (GSEA) for genes related to positive regulation of IL-1β secretion in the adrenal cortex of mice treated for 6 hr with PBS or LPS (n=3 mice per group). (B) Il1r1 expression in CD31-CD45- adrenocortical cells of mice 6 hr post-injection with PBS or LPS (n=6 mice per group). (C) GSEA for proteins related to IL-1β signaling in CD31-CD45- adrenocortical cells of mice treated for 24 hr with PBS or LPS (n=6 mice per group). (D) SDHB expression in NCI-H295R cells treated for 2 hr with IL-1β, IL-6, or TNFα (n=5–6). (E) Measurement of ATP/ADP ratio in NCI-H295R cells treated for 24 hr with IL-1β (n=5–6). (F–H) Primary adrenocortical cells were treated for 6 hr with IL-1β and for another 45 min with adrenocorticotropic hormone (ACTH) (10 ng/ml) (n=11–12). Steroid hormones were measured in the culture supernatant by liquid chromatography-tandem mass spectrometry (LC-MS/MS). (I) Western blot analysis for DNMT1 in CD31-CD45- adrenocortical cells 24 hr after injection of PBS (P) or LPS (L) (n=4 mice per group), α-TUBULIN was used as loading control. The asterisk (*) depicts an unspecific band. Quantification of the western blot is shown as relative intensity of DNMT1 to α-TUBULIN. (J) NCI-H295R cells were treated for 2 hr with IL-1β; representative gel electrophoresis images of bisulfite converted and non-treated DNA (M – methylated, U – unmethylated) are shown. The ratio of methylated to unmethylated SDHB promoter was assayed after bisulfite conversion (n=4). (K) NCI-H295R cells were transfected with siDNMT1 or siCtrl and 24 hr post-transfection they were treated for 2 hr with IL-1β. The ratio of methylated to unmethylated SDHB promoter was quantified (n=2–3). (L) Sdhb expression in primary adrenocortical cells transfected with siDnmt1 or siCtrl and 24 hr post-transfection treated for 6 hr with IL-1β (n=8). (M) Primary adrenocortical cells were transfected with siDnmt1 or siCtrl and 6 hr post-transfection they were treated for 18 hr with IL-1β (n=4). Succinate and fumarate were measured by LC-MS/MS. (N) Oxygen consumption rate (OCR) measurement in NCI-H295R cells transfected with siDNMT1 or siCtrl and 24 hr post-transfection treated for 24 hr with IL-1β (n=8). (O–Q) Primary adrenocortical cells were transfected with siDnmt1 or siCtrl, 6 hr post-transfection they were treated for 18 hr with IL-1β and subsequently they were stimulated for 45 min with ACTH (n=7–9). Steroid hormones were measured in the cell culture supernatant by LC-MS/MS. (R) Mice were simultaneously injected with Raleukin or control solution and LPS and 24 hr later SDH activity was measured in isolated adrenal cortices (n=3 mice per group). (S–T) Mice were treated with Raleukin or control solution together with LPS and 24 hr post-injection succinate and fumarate levels were determined in the adrenal glands (n=7 mice per group). (U) Mice were treated with Raleukin or control solution together with LPS and 6 hr later corticosterone plasma levels were determined by LC-MS/MS (n=7 mice per group). Data in (B,D–L,R–U) are presented as mean ± s.d. Statistical analysis was done with Mann-Whitney (B,D,I,J,N,R–U), unpaired t-test (E,K), paired t-test, (M) and Wilcoxon test (F–H,L,O–Q). *p<0.05, **p<0.01. NES: normalized enrichment score. Full unedited blots and gels are available in Figure 6—source data 1 (I,J).

One way of transcriptional gene repression is covalent attachment of methyl groups on the cytosine 5’ position within the gene promoter sequence, a reaction catalyzed by DNA methyltransferases (Suzuki and Bird, 2008). Proteomics revealed significant upregulation of DNMT1 in CD31-CD45- adrenocortical cells of LPS mice (log2fc = 0.421, padj = 0.015), which we confirmed by western blot analysis (Figure 6I). IL-1β increased DNA methylation of the SDHB promoter (Figure 6J) and the effect of IL-1β was blunted by DNMT1 silencing (Figure 6K, Figure 5—figure supplement 2D). In accordance, Dnmt1 repression restored Sdhb expression (Figure 6L) and reduced the succinate/fumarate ratio in IL-1β-treated adrenocortical cells (Figure 6M). Moreover, IL-1β decreased OCR in a DNMT1-dependent manner (Figure 4N). Accordingly, the inhibitory effect of IL-1β on steroidogenesis was restored by Dnmt1 silencing (Figure 6O–Q).

Lastly, we set out to validate the impact of IL-1β on adrenal gland function in vivo. To this end, LPS-challenged mice were treated with Raleukin, an IL-1R antagonist, or control solution. Raleukin increased SDH activity in the adrenal cortex (Figure 6R), reduced succinate levels and the succinate/fumarate ratio in the adrenal gland (Figure 6S, T), and increased corticosterone plasma levels in LPS-treated mice (Figure 6U), thereby validating the hypothesis that IL-1β negatively regulates SDH function and steroidogenesis in the inflamed adrenal cortex.

## Discussion

Glucocorticoid production in response to inflammation is essential for survival. The adrenal gland shows great resilience to damage induced by inflammation due to its strong regenerative capacity (Kanczkowski et al., 2013b; Lyraki and Schedl, 2021; Mateska et al., 2020). This maintains glucocorticoid release during infection or sterile inflammation, which is vital to restrain and resolve inflammation (Alexaki and Henneicke, 2021b; Chrousos, 1995). However, severe sepsis is associated with adrenocortical impairment (Annane et al., 2006; Annane et al., 2000; Boonen et al., 2015; Boonen et al., 2014; den Brinker et al., 2005; Jennewein et al., 2016). Here, we used an LPS mouse model to study the extent to which cell metabolic changes in the inflamed adrenal cortex affect adrenocortical function. Due to its reproducibility, LPS-induced systemic inflammation is a widely used model, which however comes with certain limitations. Being a component of gram-negative bacteria, LPS does not trigger immune reactions similar to these caused by gram-positive microorganisms or in polymicrobial sepsis. LPS is a single pathogen-associated molecular pattern (PAMP) which specifically triggers toll-like receptor 4, while sepsis is driven by a wide range of PAMPs. Moreover, LPS-induced systemic inflammation causes a rapid increase in cytokine levels followed by fast resolution of inflammation, while clinical sepsis is characterized by prolonged elevation of cytokine levels (Lewis et al., 2016). Despite its limitations, its high reproducibility compared to other models, such as the cecal slurry model, makes it suitable for mechanistic studies, such as the present.

Here, we show that the inflamed adrenal cortex undergoes cellular metabolic reprograming which involves perturbations in the TCA cycle and oxidative phosphorylation, leading to impaired steroidogenesis. Our findings provide a mechanistic explanation of inflammation-related impaired adrenocortical steroidogenesis through cell metabolic reprogramming of steroidogenic adrenocortical cells. Specifically, we demonstrate that IL-1β reduces SDHB expression through DNMT1-dependent DNA methylation of the SDHB promoter. Several studies have shown that inflammation promotes DNA methylation and thereby regulates gene expression (Koos et al., 2020; Li et al., 2020; Morante-Palacios et al., 2021; Rodriguez et al., 2019; Weiss et al., 2021). Particularly IL-1β was demonstrated to increase DNA methylation in different genes in a cell type-specific manner (Li et al., 2020; Seutter et al., 2020). In accordance, DNMT1 expression was shown to increase upon acute inflammation in human peripheral blood mononuclear cells or mouse spleens (Cao et al., 2020; Koos et al., 2020), as well as in fibroblasts treated with IL-1β (Seutter et al., 2020). Moreover, reduced SDH promoter methylation associates with enhanced SDHB expression and reduced succinate levels in villi from individuals with recurrent spontaneous abortion (Wang et al., 2021). These reports stand in accordance with our findings showing regulation of SDHB expression through its promoter methylation by an IL-1β-DNMT1 axis in steroidogenic adrenocortical cells. In contrast, itaconate, which was shown to reduce SDH activity in macrophages (Lampropoulou et al., 2016), does not regulate SDH in adrenocortical cells.

Accumulation of succinate leads to impaired oxidative phosphorylation and ATP synthesis, coupled to reduced steroidogenesis. Intact mitochondrial membrane potential and ATP generation are essential requirements for steroidogenic function (Bose et al., 2020; King et al., 1999). We confirmed this by treatment of adrenocortical cells with the mitochondrial uncoupler FCCP and the ATP synthase inhibitor oligomycin, both of which diminished steroidogenesis. Interestingly, a switch from the canonical toward a non-canonical TCA cycle, involving the metabolism of mitochondrially derived citrate to acetyl-CoA, was recently described and may be activated in inflammation (Arnold et al., 2022; Mateska and Alexaki, 2022). It remains to be elucidated whether a shift to the non-canonical TCA cycle might regulate steroidogenesis.

Intact SDH function was recently shown to be required for activation of the first steroidogenic enzyme, cytochrome P450-side-chain-cleavage (SCC, CYP11A1), which converts cholesterol to pregnenolone (Bose et al., 2020; King et al., 1999). Accordingly, we show that production of progesterone, the direct derivative of pregnenolone, is diminished upon SDH inhibition. These data suggest that impairment of SDH function may disrupt these first steps of steroidogenesis, thereby diminishing production of all downstream adrenocortical steroids.

SDH regulates ETC-mediated ROS formation: SDH inhibition or increased succinate levels augment ROS generation in tumors and macrophages (Guzy et al., 2008; Hadrava Vanova et al., 2020; Mills et al., 2016; Ralph et al., 2011; Selak et al., 2005). Similarly, we show that SDH inhibition or high succinate levels in adrenocortical cells lead to increased ROS levels at the expense of mitochondrial oxidative function and ATP production, while ROS scavenging partially restores steroidogenesis. Adrenocortical disorders such as triple A syndrome and familial glucocorticoid deﬁciency can be driven by increased oxidative stress in the adrenal cortex (Prasad et al., 2014). In fact, mutations in genes encoding for proteins conferring antioxidant protection were implicated in the development of adrenocortical deficiencies (Prasad et al., 2014). Hence, SDH dysfunction leading to oxidative stress may be an important component of the pathophysiology of adrenocortical insufficiency, a notion which merits further investigation.

In conclusion, we demonstrate that tight regulation of succinate levels is essential for normal steroidogenesis, while disruption of SDH expression through the IL-1β-DNMT1 axis contributes to adrenocortical dysfunction (Figure 7). This study expands the current knowledge on the regulation of glucocorticoid production and identifies potential targets for therapeutic interventions.

![Figure 7.](https://cdn.elifesciences.org/articles/83064/elife-83064-fig7-v2.jpg)

**Figure 7.:** IL-1β reduces SDHB expression through upregulation of DNA methyltransferase 1 (DNMT1) and methylation of the SDHB promoter. Consequently, increased succinate levels impair oxidative phosphorylation and increase ROS production, leading to reduced steroidogenesis.

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
      <td>Gene (Mus musculus)</td>
      <td>C57BL/6J</td>
      <td>The Jackson Laboratory</td>
      <td>Stock#000664 RRID:MGI:3028467</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>C57BL/6NJ-Acod1em1(IMPC)J/J</td>
      <td>The Jackson Laboratory</td>
      <td>Strain #:029340 RRID:IMSR_JAX:029340</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line(Homo sapiens)</td>
      <td>NCI-H295R</td>
      <td>ATCC</td>
      <td>CRL-2128</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ultrapure LPS, E. coli 0111:B4</td>
      <td>InVivoGen</td>
      <td>tlrl-3pelps</td>
      <td>For in vivo</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Raleukin</td>
      <td>MedChemExpress</td>
      <td>Art. -Nr.: HY-108841</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ultrapure lipopolysaccharide from E. coli K12</td>
      <td>InVivoGen</td>
      <td>tlrl-peklps</td>
      <td>For in vitro</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMM</td>
      <td>Sigma-Aldrich</td>
      <td>136441</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DES</td>
      <td>Sigma-Aldrich</td>
      <td>112402</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FCCP</td>
      <td>Agilent Technologies</td>
      <td>Seahorse XFp Cell Mito Stress Test Kit 103010-100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical Compound, drug</td>
      <td>Oligomycin</td>
      <td>Agilent Technologies</td>
      <td>Seahorse XFp Cell Mito Stress Test Kit 103010-100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Enasidenib (AG-221)</td>
      <td>Selleckchem</td>
      <td>S8205</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4-Octyl-itaconate</td>
      <td>Cayman Chemical</td>
      <td>25374</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trolox</td>
      <td>Abcam</td>
      <td>ab120747</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein (human)</td>
      <td>IL-1β</td>
      <td>PeproTech</td>
      <td>200-01B</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein (mouse)</td>
      <td>IL-1β</td>
      <td>PeproTech</td>
      <td>211-11B</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein (human)</td>
      <td>IL-6</td>
      <td>PeproTech</td>
      <td>200-06</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein (human)</td>
      <td>TNFα</td>
      <td>PeproTech</td>
      <td>300-01A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein (mouse)</td>
      <td>ACTH</td>
      <td>Sigma-Aldrich</td>
      <td>A0298</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Forskolin</td>
      <td>Sigma-Aldrich</td>
      <td>F3917</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>siRNA to SDHB(ON-TARGETplus siRNA SMARTpool)</td>
      <td>Dharmacon/Thermo Fisher Scientific</td>
      <td>L-011773-02-0005</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>siRNA to DNMT1(ON-TARGETplus siRNA SMARTpool)</td>
      <td>Dharmacon/Thermo Fisher Scientific</td>
      <td>L-004605-00-0005</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (mouse)</td>
      <td>siRNA to Sdhb(ON-TARGETplus siRNA SMARTpool)</td>
      <td>Dharmacon/Thermo Fisher Scientific</td>
      <td>L-042339-01-0005</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (mouse)</td>
      <td>siRNA to Dnmt1(ON-TARGETplus siRNA SMARTpool)</td>
      <td>Dharmacon/Thermo Fisher Scientific</td>
      <td>L-056796-01-0005</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>See Table 5</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>See Table 5</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-SDHB (Rabbit polyclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>HPA002868</td>
      <td>1:1000 for WB1:300 for IF</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-IDH2 (Rabbit polyclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>HPA007831</td>
      <td>1:50 for IF</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-DNMT1 (Rabbit monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#5032</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Tubulin (Mouse monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>T5186</td>
      <td>1:3000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-β-Actin (Rabbit polyclonal)</td>
      <td>Cell Signaling</td>
      <td>#4967</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-SF-1 (Mouse monoclonal)</td>
      <td>TransGenic Inc</td>
      <td>KO610</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ATP measurement</td>
      <td>Abcam</td>
      <td>ab83355</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ATP/ADP measurement</td>
      <td>Sigma-Aldrich</td>
      <td>MAK135</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DCFDA/H2DCFDA Cellular ROS Detection Assay Kit</td>
      <td>Abcam</td>
      <td>ab113851</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NADP/NADPH Assay</td>
      <td>Abcam</td>
      <td>ab176724</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SDH activity</td>
      <td>Sigma-Aldrich</td>
      <td>MAK197</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>IDH activity</td>
      <td>Abcam</td>
      <td>ab102528</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Seahorse XFp Cell Mito Stress Test Kit</td>
      <td>Agilent Technologies</td>
      <td>103010-100</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>EZ DNA Methylation Kit</td>
      <td>Zymo Research</td>
      <td>D5001</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ software</td>
      <td>ImageJ (http://imagej.nih.gov/ij/)</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism 7.04 software</td>
      <td>GraphPad Prism (https://graphpad.com)</td>
      <td>RRID:SCR_015807</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Morpheus</td>
      <td>Broad Institute</td>
      <td>https://software.broadinstitute.org/morpheus/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR Aligner</td>
      <td>Dobin et al., 2013</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Mouse Genome version GRCm38 (release M12 GENCODE)</td>
      <td>Anders et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2_1.8.1</td>
      <td>Anders and Huber, 2010</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ggplot2_1.0.1</td>
      <td>Wickham, 2009</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GSEA</td>
      <td>Subramanian et al., 2005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EGSEA</td>
      <td>Alhamdoosh et al., 2017</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Mass Spectrometry Downstream Analysis Pipeline (MS-DAP) (version beta 0.2.5.1) (https://github.com/ftwkoopmans/msdap)</td>
      <td>Hondius et al., 2021</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R/Bioconductor, ‘impute’ command running of ‘DEP’</td>
      <td>Zhang et al., 2018</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>TMRE</td>
      <td>Thermo Fisher</td>
      <td>T669</td>
      <td>2.5 μM for dissociated adrenocortical cells,100 nM for NCI-H295R cells</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Mitotracker Green</td>
      <td>Thermo Fisher</td>
      <td>M7514</td>
      <td>0.25 μM for dissociated adrenocortical cells,100 nM for NCI-H295R cells</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI stain</td>
      <td>Roche, Sigma-Aldrich</td>
      <td>10236276001</td>
      <td>1:10,000</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lectin Esculentum DyLight488</td>
      <td>Vector Laboratories</td>
      <td>DL-1174</td>
      <td>1:300</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>4-Hydroxynonenal</td>
      <td>Abcam</td>
      <td>ab48506</td>
      <td>1:200</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Primer sequences.


<table>
  <thead>
    <tr>
      <th>Gene name</th>
      <th>Forward sequence (5’ → 3’)</th>
      <th>Reverse sequence (5’ → 3’)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mouse 18S rRNA</td>
      <td>GTTCCGACCATAAACGATGCC</td>
      <td>TGGTGGTGCCCTTCCGTCAAT</td>
    </tr>
    <tr>
      <td>Mouse Idh1</td>
      <td>GTGGTGGAGATGCAAGGAGAT</td>
      <td>TGGTCATTGGTGGCATCACG</td>
    </tr>
    <tr>
      <td>Mouse Idh2</td>
      <td>GATGGACGGTGACGAGATGAC</td>
      <td>GGTCTGGTCACGGTTTGGA</td>
    </tr>
    <tr>
      <td>Mouse Sdhb</td>
      <td>GGACCTCAGCAAAGTCTCCAA</td>
      <td>TGCAGATACTGTTGCTTGCC</td>
    </tr>
    <tr>
      <td>Mouse Sdhc</td>
      <td>GCTAAGGAGGAGATGGAGCG</td>
      <td>AGAGACCCCTCCACTCAAGG</td>
    </tr>
    <tr>
      <td>Mouse Star</td>
      <td>CTGTCCACCACATTGACCTG</td>
      <td>CAGCTATGCAGTGGGAGACA</td>
    </tr>
    <tr>
      <td>Mouse Cyp11b1</td>
      <td>TCACCATGTGCTGAAATCCTTCCA</td>
      <td>GGAAGAGAAGAGAGGGCAATGTGT</td>
    </tr>
    <tr>
      <td>Mouse Hsd3b2</td>
      <td>GCGGCTGCTGCACAGGAATAAAG</td>
      <td>TCACCAGGCAGCTCCATCCA</td>
    </tr>
    <tr>
      <td>Mouse Cyp21a1</td>
      <td>TGGGGATGCAAGATGTGGTGGT</td>
      <td>GGTCGGCCAGCAAAGTCCAC</td>
    </tr>
    <tr>
      <td>Mouse Cyp11a1</td>
      <td>GGATGCTGGAGGAGATCGT</td>
      <td>GAAGTCTGGAGGCAGGTTGA</td>
    </tr>
    <tr>
      <td>Mouse Cd31</td>
      <td>TGCAGGAGTCCTTCTCCACT</td>
      <td>ACGGTTTGATTCCACTTTGC</td>
    </tr>
    <tr>
      <td>Mouse Cd45</td>
      <td>CCAGTCATGCTACCACAACG</td>
      <td>TGGACATCTTTGAGGTCTGCC</td>
    </tr>
    <tr>
      <td>Mouse Th</td>
      <td>AAGGGCCTCTATGCTACCCA</td>
      <td>GCCAGTCCGTTCCTTCAAGA</td>
    </tr>
    <tr>
      <td>Mouse Pnmt</td>
      <td>GCATCACATCACCACACTGC</td>
      <td>CGGACCTCGTAACCACCAAG</td>
    </tr>
    <tr>
      <td>Mouse Acod1</td>
      <td>CTCCCACCGACATATGCTGC</td>
      <td>GCTTCCGATAGAGCTGTGA</td>
    </tr>
    <tr>
      <td>Mouse Il1r1</td>
      <td>TGGAAGTCTTGTGTGCCCTT</td>
      <td>TCCGAAGAAGCTCACGTTGT</td>
    </tr>
    <tr>
      <td>Mouse Dnmt1</td>
      <td>CTGGAAGAGGTAACAGCGGG</td>
      <td>CGTCCAAGTGAGTTTCCGGT</td>
    </tr>
    <tr>
      <td>Human 18S</td>
      <td>TGCCCTATCAACTTTCGATG</td>
      <td>GATGTGGTAGCCGTTTCTCA</td>
    </tr>
    <tr>
      <td>Human SDHB</td>
      <td>CAAGGCTGGAGACAAACCTCA</td>
      <td>GGGTGCAAGCTAGAGTGTTG</td>
    </tr>
    <tr>
      <td>Human DNMT1</td>
      <td>GGAGGGCTACCTGGCTAAAG</td>
      <td>CTGCCATTCCCACTCTACGG</td>
    </tr>
    <tr>
      <td>Human methylated SDHB promoter</td>
      <td>AGTGGGTCCTCAGTGGATGTA</td>
      <td>GGCGATAGTTTGGTGGCAGA</td>
    </tr>
    <tr>
      <td>Human unmethylated SDHB promoter</td>
      <td>CGCGATGTTCGACGGGATA</td>
      <td>CTTCACACCCCGCAAATCTC</td>
    </tr>
  </tbody>
</table>

### Animal experiments

Eight- to twelve-week-old male C57BL/6J mice (purchased from Charles River) were injected i.p. with 1 mg/kg LPS (LPS-EB Ultrapure; InVivoGen) or PBS, and sacrificed after 6 hr (for gene expression analyses) or 24 hr (for all other analyses). In some experiments, mice were simultaneously i.p. injected with Raleukin (Anakinra, 10 mg/kg, MedChemExpress) or with same amount of control solution and LPS. Acod1-/- and littermate control mice were injected with 3 mg/kg LPS and sacrificed after 16 hr.

### Laser capture microdissection of adrenal cortex

Adrenal glands frozen in liquid nitrogen were cut in 25–30 μm thick sections, mounted on polyethylene naphthalate membrane slides (Zeiss), dehydrated in increasing concentrations of ice-cold ethanol (75%, 95%, 100%) for 45 s each, and air-dried at room temperature (RT). Laser capture microdissection was performed with a Zeiss PALM MicroBeam LCM system. The adrenal cortex from 8 to 12 sections was microdissected and the tissue was collected on Adhesive Caps (Zeiss).

### Bioinformatic analysis of RNA-Seq data

For transcriptome mapping, strand-specific paired-end sequencing libraries from total RNA were constructed using TruSeq stranded Total RNA kit (Illumina Inc). Sequencing was performed on an Illumina HiSeq3000 (1×75 basepairs). Low-quality nucleotides were removed with the Illumina fastq filter and reads were further subjected to adaptor trimming using cutadapt (Martin, 2011). Alignment of the reads to the Mouse Genome was done using STAR Aligner (Dobin et al., 2013) using the parameters: ‘–runMode alignReads –outSAMstrandField intronMotif –outSAMtype BAM SortedByCoordinate --readFilesCommand zcat’. Mouse Genome version GRCm38 (release M12 GENCODE) was used for the alignment. The parameters: ‘htseq-count -f bam -s reverse -m union -a 20’, HTSeq-0.6.1p1 (Anders et al., 2015) were used to count the reads that map to the genes in the aligned sample files. The GTF file (gencode.vM12.annotation.gtf) used for read quantification was downloaded from Gencode (https://www.gencodegenes.org/mouse/release_M12.html). Gene-centric differential expression analysis was performed using DESeq2_1.8.1 (Anders and Huber, 2010). The raw read counts for the genes across the samples were normalized using ‘rlog’ command of DESeq2 and subsequently these values were used to render a PCA plot using ggplot2_1.0.1 (Wickham, 2009).

Pathway and functional analyses were performed using GSEA (Subramanian et al., 2005) and EGSEA (Alhamdoosh et al., 2017). GSEA is a stand-alone software with a GUI. To run GSEA, a ranked list of all the genes from DESeq2-based calculations was created by taking the -log10 of the p-value and multiplying it with the sign of the fold change. This ranked list was then queried against MSigDB, Reactome, KEGG, and GO-based repositories. EGSEA is an R/Bioconductor-based command-line package. For doing functional analyses using EGSEA, a differentially expressed list of genes with parameters log2fc >0.3 and padj <0.05 was used. Same database repositories as above were used for performing the functional analyses.

For constructing pathway-specific heatmaps, the ‘rlog-normalized’ expression values of the significantly expressed genes (padj <0.05) were mapped on to the KEGG and GO pathways. These pathway-specific expression matrices were then scaled using Z-transformation. The resulting matrices were visually rendered using MORPHEUS.

### Cell sorting

The adrenal cortex was separated from the medulla under a dissecting microscope and was digested in 1.6 mg/ml collagenase I (Sigma-Aldrich) and 1.6 mg/ml BSA in PBS, for 25 min at 37°C while shaking at 900 rpm. The dissociated tissue was passed through a 22 G needle and 100 μm cell strainer and centrifuged at 300 × g for 5 min at 4°C. The cell suspension was washed in MACS buffer (0.5% BSA, 2 mM EDTA in PBS) and CD31+ and CD45+ cells were sequentially positively selected using anti-CD31 and anti-CD45 MicroBeads (Miltenyi Biotec), respectively, according to the manufacturer’s instructions. Briefly, pelleted cells resuspended in 190 μl MACS buffer were mixed with 10 μl anti-CD31 MicroBeads, incubated for 15 min at 4°C, washed with 2 ml MACS buffer, and centrifuged at 300 × g for 10 min at 4°C. Then, the cell pellet was resuspended in 500 μl MACS buffer, applied onto MS Columns placed on MACS Separator, and the flow-through (CD31- cells) was collected. CD31+ cells were positively sorted from the MS Columns. The flow-through was centrifuged at 300 × g for 5 min at 4°C, and the pelleted cells were subjected to the same procedure using anti-CD45 MicroBeads, collecting the flow-through containing CD31-CD45- adrenocortical cells. CD45+ cells were positively sorted from the MS Columns.

### MS/MS proteomic analysis

CD31-CD45- adrenocortical cells were sorted and snap-frozen. Samples were randomized and a gel-based sample preparation protocol was followed (Chen et al., 2011). In brief, cell pellets were resuspended in SDS loading buffer and 30% acrylamide, boiled at 98°C for 6 min, and 5 μg protein per sample were separated in 10% SDS gels (SurePAGE Bis-Tris gels, GenScript) for approximately 10 min at 120 V. The gels were fixed in 50% (vol/vol) ethanol and 3% (vol/vol) phosphoric acid and briefly stained with Colloidal Coomassie Blue. Sample containing lanes were sliced and cut into blocks of approximately 1 mm3, destained in 50 mM NH4HCO3 and 50% (vol/vol) acetonitrile, dehydrated using 100% acetonitrile, and rehydrated in 50 mM NH4HCO3 containing 10 μg/ml trypsin (sequence grade; Promega). After incubation overnight at 37°C peptides were extracted and collected in a new tube, dried using a SpeedVac (Eppendorf), and stored at -20°C until LC-MS analysis. Peptides were dissolved in 0.1% formic acid, and 75 ng were loaded into EvoTips (EV2003, Evosep) and washed according to the manufacturer’s guidelines. The samples were run on a 15 cm × 75 μm, 1.9 μm Performance Column (EV1112, Evosep) using the Evosep One liquid chromatography system with the 30 samples per day program. Peptides were analyzed by the TimsTof pro2 mass spectrometer (Bruker) with the diaPASEF method (Meier et al., 2020).

Data were analyzed using DIA-NN. The fasta database used was uniport mouse_UP000000589_10090. Deep learning was used to generate the in silico spectral library. Output was filtered at 0.01 FDR (Demichev et al., 2020). The Mass Spectrometry Downstream Analysis Pipeline (MS-DAP) (version beta 0.2.5.1) (https://github.com/ftwkoopmans/msdap) (Koopmans et al., 2022; Koopmans et al., 2023) was used for quality control and candidate discovery (Hondius et al., 2021). Differential abundance analysis between groups was performed on log transformed protein abundances. Empirical Bayes moderated t-statistics with multiple testing correction by FDR, as implemented by the eBayes functions from the limma R package, was used as was previously described (Koopmans et al., 2018).

### Bioinformatics analysis of proteomics data

From the proteomics data, the missing data was imputed using the ‘impute’ command running of ‘DEP’ (Zhang et al., 2018) package in R/Bioconductor (R Development Core Team, 2018) environment. The imputation was performed using ‘knn’ function. The resultant imputed matrix was used for further analyses. Pathway and functional analyses were performed using GSEA (Subramanian et al., 2005) and EGSEA (Alhamdoosh et al., 2017). CLI version of GSEA v4.1 was run using the imputed matrix. Different pathway sets from MSigDB v7.2 like HALLMARK, Biocarta, Reactome, KEGG, GO, and WIKIPATHWAYS were queried for functional enrichment. Gene set permutations were performed 1000 times to calculate the different statistical parameters. For doing functional analyses using EGSEA, imputed matrix was used. Same database repositories as above were used for performing the functional analyses.

### Quantitative RT-PCR

Total RNA was isolated from frozen adrenal glands with the TRI Reagent (MRC) after mechanical tissue disruption, extracted with chloroform and the NucleoSpin RNA Mini kit (Macherey-Nagel). Total RNA from sorted cells was isolated with the Rneasy Plus Micro Kit (QIAGEN) according to the manufacturer’s instructions. cDNA was synthesized with the iScript cDNA Synthesis kit (Bio-Rad) and gene expression was determined using the SsoFast Eva Green Supermix (Bio-Rad), with a CFX384 real-time System C1000 Thermal Cycler (Bio-Rad) and the Bio-Rad CFX Manager 3.1 software. The relative gene expression was calculated using the ΔΔCt method, 18S was used as a reference gene. Primers are listed in Table 5.

### Cell culture and in vitro treatments

CD31-CD45- adrenocortical cells were plated on 0.2% gelatin-coated wells of 96-well plates in DMEM/F12 medium supplemented with 1% fetal bovine serum (FBS), 50 U/ml penicillin, and 50 μg/ml streptomycin (all from Gibco), and let to attach for an hour before treatments. Cells from both adrenal glands from each mouse were pooled together and plated in two wells of a 96-well plate. Mouse adrenal explants were dissected from surrounding fat and left in DMEM/F12 medium with 1% FBS, 50 U/ml penicillin, and 50 μg/ml streptomycin for an hour before treatments. NCI-H295R cells (purchased from ATCC) were maintained in DMEM/F12 medium supplemented with 2.5% Nu-Serum type I (Corning), 1% Insulin Transferrin Selenium (ITS; Gibco), 50 U/ml penicillin, and 50 μg/ml streptomycin. NCI-H295R cells were tested mycoplasma-free.

Cells or explants were treated with DMM (20 mM; Sigma-Aldrich), DES (5 mM; Sigma-Aldrich), FCCP (1 μM; Agilent Technologies), OM (500 nM; Agilent Technologies), AG-221 (10 μM; Selleckchem), 4-OI (125 μM; Cayman Chemical), Trolox (20 μM, Abcam), mouse recombinant IL-1β (20 ng/ml, PeproTech), human recombinant IL-1β (20 ng/ml, PeproTech), human recombinant IL-6 (20 ng/ml, PeproTech), human recombinant TNFα (20 ng/ml, PeproTech), LPS (1 μg/ml; InVivoGen), ACTH (100 ng/ml; Sigma-Aldrich), or Forskolin (10 μM; Sigma-Aldrich). siRNA transfections were done with ON-TARGETplus SMARTpool siRNA against SDHB (10 nM), Sdhb (30 nM), Idh2 (30 nM), Dnmt1 (30 nM), or DNMT1 (30 nM) (all from Horizon Discovery), with Lipofectamine RNAiMAX transfection reagent (Invitrogen), using a reverse transfection protocol per manufacturer’s instructions.

### Steroid hormone measurement

Steroid hormones were analyzed by LC-MS/MS in cell culture or explant supernatants as described previously (Peitzsch et al., 2015). Fifty to hundred μL cell culture supernatants were extracted by solid phase extraction using positive pressure, followed by a dry-down under gentle stream of nitrogen. Residues were reconstituted in 100 μl of the initial LC mobile phase and 10 μl were injected for detection by the triple quadrupole mass spectrometer in multiple reaction-monitoring scan mode using positive atmospheric pressure chemical ionization. Quantification of steroid concentrations was done by comparisons of ratios of analyte peak areas to respective peak areas of stable isotope labeled internal standards obtained in samples to those of calibrators.

### Measurement of TCA cycle metabolites

TCA cycle metabolites were determined by LC-MS/MS as described before (Richter et al., 2019). Itaconate was included in the existing LC-MS/MS method using multi-reaction monitoring (MRM)-derived ion transition of 128.9→85.1. For quantification of itaconate ratios of analyte peak areas to respective peak areas of the stable isotope labeled internal standard (itaconic acid-13C5; Bio-Connect B.V., The Netherlands; MRM transition 133.9→89.1) obtained in samples were compared to those of calibrators.

### MALDI-FT-ICR-MSI

Tissue preparation steps for MALDI-MSI analysis was performed as previously described (Aichler et al., 2017; Sun et al., 2018). Frozen mouse adrenals were cryosectioned at 12 μm (CM1950, Leica Microsystems, Wetzlar, Germany) and thaw-mounted onto indium-tin-oxide-coated conductive slides (Bruker Daltonik, Bremen, Germany). The matrix solution consisted of 10 mg/ml 1,5-diaminonaphthalene (Sigma-Aldrich, Germany) in water/acetonitrile 30:70 (vol/vol). SunCollect automatic sprayer (Sunchrom, Friedrichsdorf, Germany) was used for matrix application. The MALDI-MSI measurement was performed on a Bruker Solarix 7T FT-ICR-MS (Bruker Daltonik, Bremen, Germany) in negative ion mode using 100 laser shots at a frequency of 1000 Hz. The MALDI-MSI data were acquired over a mass range of m/z 75–250 with 50 μm lateral resolution. Following the MALDI imaging experiments, the tissue sections were stained with hematoxylin and eosin and scanned with an AxioScan.Z1 digital slide scanner (Zeiss, Jena, Germany) equipped with a ×20 magnification objective. After the MALDI-MSI measurement, the acquired data underwent spectra processing in FlexImaging v. 5.0 (Bruker Daltonik, Bremen, Germany) and SciLS Lab v. 2021 (Bruker Daltonik, Bremen, Germany). The mass spectra were root-mean-square normalized. MS peak intensity of isocitrate and succinate of adrenal cortex regions were exported and applied for relative quantification analysis.

### ATP measurement

Total ATP was measured in adrenal glands using the ATP Assay Kit (ab83355, Abcam). Briefly, adrenal glands were collected, washed with PBS, and immediately homogenized in 100 μl ATP assay buffer. Samples were cleared using the Deproteinizing Sample Preparation Kit – TCA (ab204708, Abcam). Samples were incubated for 30 min with the ATP reaction mix and fluorescence (Ex/Em = 535/587 nm) was measured using the Synergy HT microplate reader. The recorded measurements were normalized to the weight of the adrenal gland.

### ROS measurement

ROS was detected using the DCFDA/H2DCFDA Cellular ROS Detection Assay Kit (ab113851, Abcam). NCI-H295R cells were plated at 80,000 cells/well in 96-well plate with black walls and clear bottom (Corning) and were incubated with 20 μM DCFDA Solution for 45 min at 37°C in dark. Fluorescence (Ex/Em = 485/535 nm) was measured using the Synergy HT microplate reader.

### ATP/ADP ratio measurement

Intracellular ATP/ADP ratio was determined with the ADP/ATP Ratio Assay Kit (MAK135, Sigma-Aldrich). NCI-H295R cells were plated at 80,000 cells/well in 96-well plate with white flat-bottom wells (Corning). Luminescence was measured using the Synergy HT microplate reader.

### NADPH/NADP+ and NADPH measurement

Intracellular NADPH/NADP+ ratio was measured with the NADP/NADPH Assay Kit (Fluorometric) (ab176724, Abcam). NCI-H295R cells were plated at 5×106 cells/10 cm – diameter dish. Fluorescence (Ex/Em = 540/590 nm) was measured using the Synergy HT microplate reader. NADPH levels in adrenal tissue homogenates were analyzed by LC-MS/MS using an adapted method as previously described (Yuan et al., 2012).

### Enzyme activity measurement

SDH and IDH activities were measured using respective colorimetric assay kits (MAK197, Sigma-Aldrich, ab102528, Abcam). Cortices from both adrenal glands of each mouse were pooled and processed together. Absorbance (at 600 nm for SDH or 450 nm for IDH) was detected using the Synergy HT microplate reader.

### Seahorse assay

OCR measurements were performed with a Seahorse XF96 Analyzer (Agilent Technologies). NCI-H295R cells were plated at 80,000 cells/well in 0.2% gelatin-precoated XF96 cell culture microplate (Agilent). The experimental medium used was XF Base Medium supplemented with glucose (10 mM), pyruvate (1 mM), and glutamine (2 mM).

### Measurement of mitochondrial load and membrane potential

The adrenal cortex was digested and dissociated cells were incubated with Mitotracker Green (0.25 μM; Thermo Fisher), TMRE (2.5 μM; Thermo Fisher), CD31-PeCy7 (1:100; eBioscience), and CD45-PeCy7 (1:100; eBioscience) for 30 min in FACS buffer (0.5% BSA, 2 mM EDTA in PBS) at 37°C in dark. Live cells were selected by Hoechst staining. NCI-H295R cells were incubated with MitotrackerGreen (100 nM) and TMRE (100 nM) for 30 min at 37°C in dark. FACS was performed using LSR Fortessa X20 ﬂow cytometer and data were analyzed with the FlowJo software.

### Western blotting

Cells were lysed with 10 mM Tris-HCl, pH7.4+1% SDS+1 mM sodium vanadate, cell lysates were centrifuged at 16,000 × g for 5 min at 4°C, supernatants were collected and total protein concentration was measured using Pierce BCA Protein Assay Kit (Thermo Scientific). Gel electrophoresis was performed according to standard protocols (Laemmli, 1970). Protein samples were prepared with 5× Reducing Laemmli buffer, denatured at 95°C for 5 min and loaded on a 10% acrylamide gel (Invitrogen) for sodium dodecyl sulfate polyacrylamide gel electrophoresis. PageRuler Prestained Protein Ladder (Thermo Fisher Scientific) was used as a protein size ladder. The separated proteins were transferred on Amersham Protran nitrocellulose membrane (GE Healthcare Lifescience). After blocking with 5% skimmed milk in TBS-T (0.1% Tween-20 [Sigma-Aldrich] in 1× Tris-buffered saline) for 1 hr at RT, membranes were incubated overnight at 4°C with anti-SDHB (1:1000; Sigma-Aldrich, HPA002868), anti-DNMT1 (1:1000; Cell Signaling, #5032), anti-Tubulin (1:3000; Sigma-Aldrich, T5186), or anti-β-Actin (1:1000; Cell Signaling, #4967), diluted in 5% BSA in TBS-T. After washing, membranes were incubated for 1 hr at RT with secondary antibodies: goat anti-rabbit IgG HRP-conjugated (1:3000; Jackson ImmunoResearch) or goat anti-mouse IgG HRP-conjugated (1:3000; Jackson ImmunoResearch), diluted in 5% skimmed milk in TBS-T. The signal was detected using the Western Blot Ultra-Sensitive HRP Substrate (Takara) and imaged using the Fusion FX Imaging system (PeqLab Biotechnologie).

### DNA methylation measurement

Genomic DNA from 2×106 NCI-H295R cells was isolated with the Quick-DNA Miniprep Kit (Zymo Research). Bisulfite treatment was performed using the EZ DNA Methylation Kit (Zymo Research), following the manufacturer’s protocol. For each sample, 500 ng genomic DNA was used, bisulfite treated for 14 hr in the dark and, after a desulphonation and cleaning step, eluted in 10 μl nuclease-free water. The SDHB promoter region was amplified with primers for a methylated and a non-methylated sequence (listed in Table 5), using the QIAGEN Multiplex PCR Kit. Equal amount of DNA not treated with bisulfite was amplified as a loading control. The PCR products were then electrophoresed on 3% agarose gel and visualized under UV illumination using the Fusion FX Imaging system (Vilber). The ratio of methylated to non-methylated DNA was calculated after gel intensity quantification in ImageJ.

### Immunofluorescent staining

Adrenal glands cleaned from surrounding fat tissue were fixed in 4% PFA in PBS, washed overnight in PBS, cryopreserved in 30% sucrose (AppliChem GmbH) in PBS overnight at 4°C, embedded in OCT compound (Tissue-Tek), and frozen at −80°C. Each adrenal gland was cut into 8 μm thick serial sections. Before staining, adrenal sections were pre-warmed at RT for 30 min and antigen retrieval was performed by boiling in citrate buffer (pH 6) for 6 min. Adrenal sections were washed with PBS, permeabilized with 0.1% Triton X-100 in PBS for 20 min, treated with TrueBlack Lipofuscin Quencher (1:40 in 70% ethanol; Biotium) for 30 s to reduce autofluorescence and blocked in Dako Protein Block, serum-free buffer for 1 hr at RT. Then, sections were incubated overnight at 4°C with primary antibodies, washed with PBS, and incubated for 1 hr at RT with the secondary antibodies together with DAPI (1:5000; Roche), all diluted in Dako Antibody Diluent. Antibodies and dyes used were: anti-SDHB (1:300; Sigma-Aldrich, HPA002868), anti-IDH2 (1:50; Sigma-Aldrich, HPA007831), anti-SF-1 (1:100; TransGenic Inc KO610), Lectin Esculentum DyLight488 (1:300; Vector Laboratories, DL-1174), 4-HNE (1:200; Abcam, ab48506), Alexa Fluor 555 donkey anti-rabbit (1:300; Life Technologies, #A-31572), Alexa Fluor 647 chicken anti-rat (1:300; Invitrogen, #A21472), and Alexa Fluor 555 donkey anti-mouse (1:300; Invitrogen, #A31570). After washing with PBS, cryosections were mounted with Fluoromount (Sigma-Aldrich), covered with 0.17 mm cover glass, fixed with nail polish, and kept at 4°C until imaging.

### Image acquisition and image analysis

Z-series microscopic images for SDHB and IDH2 staining were acquired on Zeiss LSM 880 inverted confocal microscope (Zeiss, Jena, Germany), illuminated with laser lines at 405 nm, 488 nm, 561 nm, and 633 nm, and detected by two photomultiplier tube detectors. EC Plan-Neofluoar objective with ×40 magnification, 1.30 numerical aperture, and M27 thread, working with an oil immersion medium Immersol 518F, was used. Microscopic images of SF-1 and 4-HNE stainings were acquired with an Axio Observer Z1/7 inverted microscope with Apotome mode (Zeiss, Jena, Germany), illuminated with LED-Module 385 nm and 567 nm, on a Plan-Apochromat objective with ×10 magnification, 0.45 numerical aperture, and M27 thread. Laser power, photomultiplier gain, and pinhole size were set for each antibody individually and kept constant for all image acquisitions. For each condition, at least three view-fields were imaged per tissue section. Images were acquired with the ZEN 3.2 blue edition software, and processed and quantified with the ImageJ software on maximum intensity Z-projection images.

### Statistical analysis

The statistical analysis and data plotting were done with the GraphPad Prism 7.04 software. The statistical tests used are described in each figure legend, p<0.05 was set as a significance level.

### Graphical design

Figure 7 was created with Biorender.com.
