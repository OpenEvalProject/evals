# In silico screening by AlphaFold2 program revealed the potential binding partners of nuage-localizing proteins and piRNA-related proteins

## Authors

- Shinichi Kawaguchi<sup>1</sup> ([ORCID: 0000-0002-7832-1918](https://orcid.org/0000-0002-7832-1918)) †
- Xin Xu<sup>1</sup>
- Takashi Soga<sup>2</sup>
- Kenta Yamaguchi<sup>3</sup>
- Ryuuya Kawasaki<sup>3</sup>
- Ryota Shimouchi<sup>4</sup>
- Susumu Date<sup>2</sup>
- Toshie Kai<sup>1</sup> ([ORCID: 0000-0001-8675-8469](https://orcid.org/0000-0001-8675-8469)) †

### Affiliations

1. Graduate School of Frontier Biosciences, Osaka University Osaka Japan ([ROR:035t8zc32](https://ror.org/035t8zc32))
2. D3 Center, Osaka University Osaka Japan ([ROR:035t8zc32](https://ror.org/035t8zc32))
3. NEC Solution Innovators, Ltd. Tokyo Japan
4. Graduate School of Information Science and Technology, Osaka University Osaka Japan ([ROR:035t8zc32](https://ror.org/035t8zc32))

† Corresponding author

## Abstract

Protein–protein interactions are fundamental to understanding the molecular functions and regulation of proteins. Despite the availability of extensive databases, many interactions remain uncharacterized due to the labor-intensive nature of experimental validation. In this study, we utilized the AlphaFold2 program to predict interactions among proteins localized in the nuage, a germline-specific non-membrane organelle essential for piRNA biogenesis in Drosophila. We screened 20 nuage proteins for 1:1 interactions and predicted dimer structures. Among these, five represented novel interaction candidates. Three pairs, including Spn-E_Squ, were verified by co-immunoprecipitation. Disruption of the salt bridges at the Spn-E_Squ interface confirmed their functional importance, underscoring the predictive model’s accuracy. We extended our analysis to include interactions between three representative nuage components—Vas, Squ, and Tej—and approximately 430 oogenesis-related proteins. Co-immunoprecipitation verified interactions for three pairs: Mei-W68_Squ, CSN3_Squ, and Pka-C1_Tej. Furthermore, we screened the majority of Drosophila proteins (~12,000) for potential interaction with the Piwi protein, a central player in the piRNA pathway, identifying 164 pairs as potential binding partners. This in silico approach not only efficiently identifies potential interaction partners but also significantly bridges the gap by facilitating the integration of bioinformatics and experimental biology.

## Introduction

Around 10,000–20,000 different types of proteins are encoded in the genome of most organisms, catalyzing the vast majority of physico-chemical reactions in cells (Galperin et al., 2021). Many proteins have specialized functions and are often regulated through protein–protein interactions, where the formation of protein complexes can activate, inhibit, or stabilize their partners. Furthermore, protein–protein interactions can recruit target proteins to specific locations where they will function or regulate the mobility of the protein complex (Phair and Misteli, 2000). Within cells, proteins are thought to exist in a crowded environment and frequently interact with other molecules (Yu et al., 2016). Thus, characterizing protein–protein interactions is fundamental for understanding protein function and regulation. Large-scale analyses of protein–protein interactions have been carried out, including Tandem Affinity Purification coupled with Mass Spectrometry for the yeast proteome (Gavin et al., 2002) and the comprehensive 2-hybrid screening for the Human Reference Interactome (Luck et al., 2020). Despite these extensive studies, the overall protein–protein interactions are still not fully understood in many organisms.

The binding between proteins is significantly influenced by their three-dimensional (3D) structures. The characteristics of their interfaces, including hydrogen bonds, salt bridges, and hydrophobicity, determine the interactions (Keskin et al., 2008). Therefore, to analyze protein–protein interactions physically and chemically, information on the individual 3D structures of proteins is necessary. The 3D structures of proteins have been determined through experimental methods such as X-ray crystallography, nuclear magnetic resonance (NMR), and cryo-electron microscopy (Burley et al., 2023). However, these techniques demand considerable labor and time. The recently developed AlphaFold2 program can predict the 3D structure from its amino acid sequence with high accuracy (Jumper et al., 2021). AlphaFold2 requires sequence homology information to predict protein–protein interactions and the complex structure model. The reliability of these predictions is basically dependent on the strength of co-evolutionary signals (Evans et al., 2021). This tool has not only been utilized in computational studies but has also become a valuable resource in experimental sciences for predicting protein complexes, as demonstrated with yeast protein complexes (Humphreys et al., 2021).

In this study, we attempted a rapid screening of the protein interactions using AlphaFold2 prediction, primarily focusing on components of nuage, a germline-specific, non-membrane organelle that involves a wide variety of proteins containing unique motifs and domains in Drosophila melanogaster (Pek et al., 2012). Nuage is known to serve as the production and amplification site for small non-coding piRNA, which is bound to PIWI-family proteins. The piRNAs and the PIWI family proteins function to repress mobile genetic elements, or transposons, that disrupt the genomes through their active transpositions (Ross et al., 2014). Not only proteins involved in piRNA production, but also translation repressor proteins, including Me31B, Cup, and Trailer hitch (Tral), also localize in nuage (McCambridge et al., 2020). Previous studies have shown that the localization of several components in nuage depends on their partners in a hierarchical manner (Lim and Kai, 2007). However, the interaction and organization among nuage components remain unclear.

By using AlphaFold2 predictions, we investigated 20 of the nuage-localizing or piRNA-related proteins for pairwise interactions. AlphaFold2 was initially trained to predict the structure of individual proteins (Jumper et al., 2021). Its application to complex prediction is an extrapolative use beyond its original intended scope, and its accuracy remains unverified. Even high-confidence predictions may not correspond to actual interactions, necessitating experimental validation to confirm whether predicted protein dimers truly bind. In this study, we confirmed the novel interactions of candidate pairs, including Spindle-E (Spn-E)_Squash (Squ), by co-immunoprecipitation assay using cultured cells. In addition, a Squ mutant, which disrupts the salt bridges predicted at the interface with Spn-E, failed to interact with Spn-E, validating the accuracy of the predicted dimer structure. This screening was expanded for direct interacting pairs between piRNA-related proteins and proteins involved in oogenesis, as well as Piwi and other Drosophila proteins. This in silico approach not only streamlines the identification of interaction partners but also bridges the gap between bioinformatics predictions and experimental validation in biological research.

## Results and discussion

### The nuage-localizing proteins and piRNA-related proteins used in the AlphaFold2 screening

Several dozen proteins engaged in piRNA production in germline cells exert their function by recruiting piRNA precursors and interacting with their partner proteins, forming non-membrane structure called a nuage (Pek et al., 2012; Lim and Kai, 2007). Previous studies reported that many piRNA-related proteins localized to nuage and some proteins localized in mitochondria (Table 1). In addition, protein components of processing bodies and sponge bodies, which are involved in the translation, storage, degradation, and transportation of mRNAs—such as Me31B, Cup, and Tral—also localize to nuage (McCambridge et al., 2020; Table 1). However, the details of how these proteins interact and organize themselves within the nuage remain unclear.

**Table 1.**
 The piRNA production-related proteins used in this study.


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Ortholog</th>
      <th>Number of residues</th>
      <th>Domain</th>
      <th>Direct binding(MIST database)</th>
      <th>Localization</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vas</td>
      <td>DDX4</td>
      <td>661</td>
      <td>DEAD-Box, Hel-C</td>
      <td>Aub</td>
      <td>Nuage</td>
      <td>Lim and Kai, 2007</td>
    </tr>
    <tr>
      <td>Spn-E</td>
      <td>Tdrd9</td>
      <td>1434</td>
      <td>DEAD-Box, Hel-C, HA2, eTud</td>
      <td></td>
      <td>Nuage</td>
      <td>Andress et al., 2016</td>
    </tr>
    <tr>
      <td>Tej</td>
      <td>Tdrd5</td>
      <td>559</td>
      <td>Lotus, eTud</td>
      <td></td>
      <td>Nuage</td>
      <td>Lin et al., 2023</td>
    </tr>
    <tr>
      <td>Tapas</td>
      <td>Tdrd7</td>
      <td>1222</td>
      <td>Lotus, eTud</td>
      <td></td>
      <td>Nuage</td>
      <td>Patil et al., 2014</td>
    </tr>
    <tr>
      <td>Qin</td>
      <td>Rnf17</td>
      <td>1857</td>
      <td>RING, eTud</td>
      <td></td>
      <td>Nuage</td>
      <td>Andress et al., 2016</td>
    </tr>
    <tr>
      <td>Kots</td>
      <td>Tdrd1</td>
      <td>892</td>
      <td>eTud</td>
      <td></td>
      <td>Nuage</td>
      <td>Lim et al., 2022</td>
    </tr>
    <tr>
      <td>Krimp</td>
      <td>-</td>
      <td>746</td>
      <td>eTud</td>
      <td></td>
      <td>Nuage</td>
      <td>Lim and Kai, 2007</td>
    </tr>
    <tr>
      <td>Squ</td>
      <td>-</td>
      <td>241</td>
      <td></td>
      <td></td>
      <td>Nuage</td>
      <td>Pane et al., 2007</td>
    </tr>
    <tr>
      <td>Mael</td>
      <td>Mael</td>
      <td>462</td>
      <td>HMG, MAEL</td>
      <td></td>
      <td>Nuage</td>
      <td>Lim and Kai, 2007</td>
    </tr>
    <tr>
      <td>Aub</td>
      <td>PIWIL2</td>
      <td>866</td>
      <td>N, PAZ, PIWI, MID</td>
      <td>Vas, Papi, Me31B</td>
      <td>Nuage</td>
      <td>Lim and Kai, 2007</td>
    </tr>
    <tr>
      <td>AGO3</td>
      <td>PIWIL4</td>
      <td>867</td>
      <td>N, PAZ, PIWI, MID</td>
      <td>Papi</td>
      <td>Nuage</td>
      <td>Webster et al., 2015</td>
    </tr>
    <tr>
      <td>Papi</td>
      <td>Tdrkh</td>
      <td>576</td>
      <td>eTud, KH</td>
      <td>Aub, AGO3</td>
      <td>Mitochondria</td>
      <td>Liu et al., 2011</td>
    </tr>
    <tr>
      <td>Vret</td>
      <td>Tdrd1</td>
      <td>691</td>
      <td>eTud</td>
      <td>BoYb</td>
      <td>Nuage</td>
      <td>Handler et al., 2011</td>
    </tr>
    <tr>
      <td>Bel</td>
      <td>DDX3</td>
      <td>801</td>
      <td>DEAD-Box</td>
      <td></td>
      <td>Nuage</td>
      <td>Johnstone et al., 2005</td>
    </tr>
    <tr>
      <td>Zuc</td>
      <td>Pld6</td>
      <td>253</td>
      <td>PLD-like</td>
      <td>Zuc</td>
      <td>Mitochondria</td>
      <td>Nguyen et al., 2023</td>
    </tr>
    <tr>
      <td>Cup</td>
      <td>Eif4enif1</td>
      <td>1117</td>
      <td></td>
      <td>Me31B</td>
      <td>Nuage</td>
      <td>McCambridge et al., 2020</td>
    </tr>
    <tr>
      <td>Tral</td>
      <td>Lsm14</td>
      <td>657</td>
      <td>Lsm, FDF</td>
      <td>Me31B</td>
      <td>Nuage</td>
      <td>McCambridge et al., 2020</td>
    </tr>
    <tr>
      <td>Me31B</td>
      <td>DDX6</td>
      <td>459</td>
      <td>DEAD-Box</td>
      <td>Aub, Cup, Tral</td>
      <td>Nuage</td>
      <td>McCambridge et al., 2020</td>
    </tr>
    <tr>
      <td>Shu</td>
      <td>Fkbp6</td>
      <td>455</td>
      <td>PPIase</td>
      <td></td>
      <td>Nuage</td>
      <td>Olivieri et al., 2012</td>
    </tr>
    <tr>
      <td>BoYb</td>
      <td>Tdrd12</td>
      <td>1059</td>
      <td>DEAD-Box, eTud</td>
      <td>Vret</td>
      <td>Nuage</td>
      <td>Handler et al., 2011</td>
    </tr>
  </tbody>
</table>

_MIST, Molecular Interaction Search Tool._

In this study, we used the AlphaFold2 program to screen for interactions among 20 proteins that are localized in the nuage and/or involved in piRNA production in Drosophila (Table 1). The monomeric structures of these 20 proteins, ranging in size from 20 kDa to 250 kDa, have already been predicted and are registered in databases (Varadi et al., 2024). This set includes both well-structured proteins and those that are largely disordered with numerous loops (Figure 1—figure supplement 1A). Of those, eight proteins feature one or more Tudor domains or extended Tudor (eTud) domains. The Tudor domain contains approximately 60 residues and folds into an antiparallel β-sheet with five strands forming a barrel-like fold, while the eTud domains include an additional Oligonucleotide/oligosaccharide-Binding fold domain (Ren et al., 2014). Both Tudor and eTud domains are known to bind predominantly to methylated lysine or arginine residues. In addition, five RNA helicases, such as Vasa (Vas) and the fly homolog of Tdrd9, Spn-E, which are essential for piRNA processing, are also included (Table 1). The Vas’s C-terminal region is known to bind to the Lotus domain shared by two nuage components, Tejas (Tej) and Tapas. Spn-E is also recently shown to interact with Tej (Lin et al., 2023). Among those 20 proteins, the Molecular Interaction Search Tool (MIST), a conventional database of protein–protein interactions, registers 8 interacting pairs as direct binding, and 28 interactions which are direct or indirect (Table 1, Figure 1—figure supplement 1B and C; Hu et al., 2018).

### Screening for the protein–protein interactions by AlphaFold2

We used AlphaFold2 program to predict the direct protein–protein interaction and 3D structure of the complex. Assuming a 1:1 binding of 20 types of proteins, a total of 400 pairs of dimer predictions were calculated by a supercomputer. The prediction flow of AlphaFold2 consisted of two main parts (Jumper et al., 2021). Initially, a multiple sequence alignment was performed for each query protein and stored for the future use. Subsequently, the AlphaFold2 program predicted 3D dimer structures based on the co-evolution inferred from the multiple sequence alignments. For each dimer prediction, five different structure models with varying parameters were generated. Among these, the model with the highest prediction confidence score (ranking confidence) was selected as the final prediction result. The ranking confidence is constituted by two evaluations, the overall structure (pTM) and an evaluation of the dimeric interface (ipTM), emphasizing the interface evaluation as represented by the following formula (Evans et al., 2021): ranking confidence = 0.8 × ipTM + 0.2 × pTM.

These three values, ranking confidence, ipTM, and pTM, for each prediction pairs were visualized in the separate heatmaps (Figure 1A, Supplementary file 1). In general, ranking confidence and ipTM values showed similar trends although a well-structured protein (e.g., Spn-E) tended to have a higher pTM value, which slightly elevated the ranking confidence. Based on this, in this study, we used the ranking confidence as an indicator of the protein–protein interaction. Each heterodimeric pair was calculated twice in the pairwise screening (e.g., proteins A_B and B_A), and the ranking confidences were plotted (Figure 1B). The results showed that there was significant variance in the pairs with lower ranking confidences, while pairs with ranking confidences above 0.6 had relatively higher reproducibility. Consequently, we set a threshold of 0.6 and considered protein pairs with ranking confidences above 0.6 as likely complex-forming candidates. This approach identified 13 pairs; seven of these were already known to form complexes, confirming the effectiveness of AlphaFold2 in predicting complex formations (Table 2). The highest ranking confidence pair was the Zuc homodimer, possibly because AlphaFold2 had learned from Zuc homodimer’s crystal structure registered in the database (Nishimasu et al., 2012). The structures of the 20 proteins used in this study have been analyzed to varying extents in previous studies (Supplementary file 2). A complex of Vas and the Lotus domain of Osk has been reported (Jeske et al., 2017), and based on this complex structure, the interaction between Vas and Tej Lotus domain was predicted with a high score. Although the conformational analyses of the RNA helicase domain and the eTud domain have been reported previously, many of those cover only a subset of the regions and unlikely to affect our predictions in this study.

![Figure 1.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig1-v1.jpg)

**Figure 1.:** (A) Heatmaps of the prediction confidence scores (ranking confidence, green), pTM values (blue), and ipTM values (red) provided by AlphaFold2. The 20 types of proteins are aligned from top to bottom and left to right in the same order. Boxes on diagonal line represent homodimers. (B) Scatter plot of the ranking confidences. The scores from first and second predictions for each heterodimer pair are plotted on X and Y axis, respectively. (Ci~xii) The predicted 3D structures (top panels) and the Predicted Aligned Error (PAE) plots (bottom panels) for each candidate heterodimers scoring above 0.6. The PAE plot displays the positional errors between all amino acid residue pairs, formatted in a matrix layout. (D) Co-immunoprecipitation assays using tagged proteins to verify interactions between specific pairs: Spn-E_Squ (i), Aub_Vret (ii), Spn-E_BoYb (iii), BoYb_Shu (iv), and Me31B_Vret (v). Single transfected cells expressing only Myc-tagged but not Flag-tagged proteins are used as negative controls for each set. Box and whisker plots show the intensity ratio between immunoprecipitated and input bands (n = 3 biological replicates). p-values were calculated using Student’s t-test.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Predicted monomeric structures of 20 proteins used in this study, presented as ribbon models scaled uniformly. Residues are colored by per-residue model confidence scores (pLDDT). (B) Direct binding pairs from the MIST database, shown with AlphaFold2 scores. (C) Direct or indirect binding pairs from the MIST database, shown with AlphaFold2 scores.

**Table 2.**
 The screening for the interacting proteins (prediction confidence score, ranking confidence >0.6).


<table>
  <thead>
    <tr>
      <th>Protein A_Bfirst prediction</th>
      <th>ranking confidence</th>
      <th>Protein B_Asecond prediction</th>
      <th>Ranking confidence</th>
      <th>Reference</th>
      <th>Validation by co-IP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zuc_Zuc</td>
      <td>0.85</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>Nishimasu et al., 2012</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>AGO3_Mael</td>
      <td>0.78</td>
      <td>Mael_AGO3</td>
      <td>0.78</td>
      <td>Namba et al., 2022</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Aub_Mael</td>
      <td>0.78</td>
      <td>Mael_Aub</td>
      <td>0.78</td>
      <td>Namba et al., 2022</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Spn-E_Squ</td>
      <td>0.77</td>
      <td>Squ_Spn-E</td>
      <td>0.78</td>
      <td>This study</td>
      <td>++</td>
    </tr>
    <tr>
      <td>Me31B_Tral</td>
      <td>0.74</td>
      <td>Tral_Me31B</td>
      <td>0.72</td>
      <td>McCambridge et al., 2020</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Aub_Vret</td>
      <td>0.72</td>
      <td>Vret_Aub</td>
      <td>0.72</td>
      <td>This study</td>
      <td>+</td>
    </tr>
    <tr>
      <td>BoYb_Spn-E</td>
      <td>0.69</td>
      <td>Spn-E_BoYb</td>
      <td>0.69</td>
      <td>This study</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Cup_Me31B</td>
      <td>0.68</td>
      <td>Me31B_Cup</td>
      <td>0.70</td>
      <td>McCambridge et al., 2020</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Spn-E_Tej</td>
      <td>0.65</td>
      <td>Tej_Spn-E</td>
      <td>0.65</td>
      <td>Lin et al., 2023</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>BoYb_Vret</td>
      <td>0.64</td>
      <td>Vret_BoYb</td>
      <td>0.65</td>
      <td>Handler et al., 2011</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>BoYb_Shu</td>
      <td>0.64</td>
      <td>Shu_BoYb</td>
      <td>0.56</td>
      <td>This study</td>
      <td>+</td>
    </tr>
    <tr>
      <td>Me31B_Vret</td>
      <td>0.64</td>
      <td>Vret_Me31B</td>
      <td>0.45</td>
      <td>This study</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Tej_Vas</td>
      <td>0.61</td>
      <td>Vas_Tej</td>
      <td>0.62</td>
      <td>Patil and Kai, 2010</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>

The predicted 3D structures and the Predicted Aligned Error (PAE) plots for the 12 pairs are shown in Figure 1C. Consistent with a previous report using silkworm Bombyx mori (Namba et al., 2022), both Argonaute 3 (AGO3) and Aub, members of PIWI-family proteins sharing 50–60% amino acid sequence similarity, were predicted to form dimers with Maelstrom (Mael) (Figure 1Ci and ii, Table 2). AGO3 and Aub appeared well-folded protein except for their N-terminal flexible regions. In contrast, Mael protein was divided into three parts: N-terminal HMG domain, middle MAEL domain, and C-terminal disordered region (Matsumoto et al., 2015; Figure 1Ci and ii). AlphaFold2 predicted the MAEL domain interacted with AGO3 and Aub.

Me31B, Tral, and Cup are recognized as RNA regulators localized to the nuage and/or sponge body, though they are not directly involved in the piRNA pathway. Previous studies have indicated that these proteins form complexes (McCambridge et al., 2020; Tritschler et al., 2009; Tritschler et al., 2008). Me31B is a well-conserved RNA helicase and showed the tightly folded structure composed of two concatenated RecA helicase domains (Peter et al., 2019). On the other hand, Tral and Cup were predicted largely disordered structure with some secondary structures (Figure 1Ciii and iv). The predicted dimer structures of Me31B_Tral and Cup_Me31B showed scores of 0.74 and 0.68, respectively. (Table 2). Consistent with the previous study (Tritschler et al., 2008), AlphaFold2 predicted that the FDF motif of Tral, which contains a Phe-Asp-Phe sequence folded into two a-helixes from residue 405–537, was associated with Me31B (Figure 1Ciii). In addition, an α-helix and loop regions of Cup were predicted to make a contact with Me31B (Figure 1Civ). BoYb and Vret, both are eTud domain containing proteins (Chen et al., 2011) and their direct interaction has been suggested by the high retrieval rate for BoYb in the immunoprecipitant of Vret from the ovary (Handler et al., 2011). The predicted structure revealed that both BoYb and Vret proteins consist of two domains, one at the N-terminal and the other at the C-terminal, connected by a flexible region. (Figure 1Cv). Interactions were predicted between their N-terminal domains and between C-terminal domains, respectively. It has been reported that Tej, known as Tdrd5 in mammal, binds directly to Vas through its N-terminal Lotus domain (Jeske et al., 2017; Figure 1Cvi) and to Spn-E through its loop region continuing the eTud domain (Lin et al., 2023; Figure 1Cvii). The predicted structures of Tej_Vas and Spn-E_Tej were consistent to their binding properties reported previously.

The remaining five pairs, previously unreported as directly interacting, were considered novel binding pairs (Table 2, Figure 1Cviii–xii). These interactions were experimentally examined using Drosophila S2 culture cells derived from embryonic somatic cells that lack germline-specific proteins. Previously, Squ was co-immunoprecipitated with Spn-E along with other nuage components from ovarian lysate (Andress et al., 2016), but whether this interaction was direct had not been examined. Co-immunoprecipitation assay in S2 cells, Myc-Spn-E was strongly detected in the precipitant of Flag-Squ by western blotting, possibly supporting the direct interaction between Spn-E and Squ in the S2 cells devoid of germline proteins (Figure 1Di). Similarly, AlphaFold2 predicted a direct interaction between Aub and Vret, which was corroborated by co-immunoprecipitation assays (Figure 1Dii). The binding capabilities of another pair, BoYb-Shutdown (Shu), were also confirmed in S2 cells (Figure 1Div). Three out of five candidate pairs confirmed interactions, validating the effectiveness of AlphaFold2 in identifying the binding partners. However, BoYb-Spn-E and Me31B-Vret did not show interaction in these assays (Figure 1Diii and v), possibly suggesting weak interactions that co-immunoprecipitation may have failed to detect. While co-immunoprecipitation is a widely used method, it may not always detect weak or transient interactions. Other validation methods, such as FRET or co-localization assay in culture cells, could offer further insights to support the results. It is also important to note that AlphaFold2’s predictions are not definitive and may lead to false positives, particularly when analyzing a large number of interactions.

### Evaluation of Spn-E and Squ interaction in culture cells and ovaries

Among the binding candidates, we focused on the predicted dimer structure of Spn-E and Squ pair. Spn-E is an evolutionarily conserved RNA helicase that is expressed in germline cells. It plays a crucial role in the piRNA production and transposon suppression in germline cells (Andress et al., 2016; Czech et al., 2013). Similarly, Squ is also expressed in ovary and testis and involved in the piRNA production, although its molecular role is less defined (Czech et al., 2013; Pane et al., 2007). While squ is conserved across Drosophila species (Figure 2—figure supplement 1A, B), vertebrate orthologs remain unidentified. Spn-E contains four domains: DEAD/DEAH helicase, Hel-C, HA2, and eTud domains (Figure 2A). Its predicted 3D structure was well folded and contained few flexible regions (Figure 1Cviii). In contrast, Squ was predicted to be largely disordered, consisting of three α-helices and two β-strands (Figure 2A). The middle parts of Squ were in close contact with Spn-E, showing lower PAE values, suggestive of their interaction (Figures 1Cviii and 2A). AlphaFold2 predicts the five structure models for each query using different initial model parameters (models 1–5) and ranking confidence is given to each model. As for Spn-E_Squ pair, the ranking confidence scores were ranging from 0.74 to 0.77. The 3D structures of Spn-E were very similar across all five models, superimposing almost perfectly (Figure 2B). The middle region of Squ was consistently positioned relative to Spn-E, although the N- and C-terminal regions of Squ remained flexible (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig2-v1.jpg)

**Figure 2.:** (A) Schematic of Spn-E domain structures defined in SMART (Letunic et al., 2021). Boxes (α-helix: orange) and arrow (β-sheet: green) for Squ structure. The predicted interacting regions between Spn-E and Squ are indicated in gray boxes. Tej interaction site of Spn-E is also shown (Lin et al., 2023). (B) The predicted five models of heterodimer of Spn-E (in gray) and Squ (in magenta). Spn-E molecules in all five models are superimposed. (C) 3D structure of the Spn-E_Squ dimer colored by Spn-E domains as indicated in (A), with Squ in magenta. The enlarged image of the interface indicated by box is also shown. (D) The predicted salt bridges at the interface, with Spn-E in gray and Squ in magenta. The residues forming salt bridges are depicted in stick model. (E) Co-immunoprecipitation assay using S2 cell lysate to examine the interaction between Myc-Spn-E and Flag-Squ mutant (4A) whose salt bridge-forming residues are mutated to Ala. S2 cells expressing Myc-Spn-E alone is used as a control. The ratios of the band intensity (IP/input) are shown in a box and whisker plot (n = 3 biological replicates). p-values were calculated using Student’s t-test. (F) The heterotetramer model of Spn-E_Squ_Tej_RNA predicted by AlphaFold3. Spn-E is shown as a space filled model in gray, Squ in magenta, Tej in cyan, and RNA in yellow. The model on the left is rotated 180° in the Y axis to produce the image on the right.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Phylogenetic tree of Squ homologs across various Drosophila species. (B) Multiple sequence alignment of Squ orthologs from different Drosophila species, highlighting residues predicted to form salt bridges with Spn-E. (C) Multiple sequence alignment of Spn-E orthologs in Drosophila species focusing on regions around residues predicted to interact with Squ. The legend was shown in the original pdf, but the legends has been removed during the process.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Co-immunoprecipitation of Myc-Spn-E and Flag-Squ expressed in S2 culture cells. In addition to the wildtype, Squ mutants containing amino acid residues predicted to form salt bridges altered to Alanine were also examined. The right panel shows quantifications of the intensity ratio (IP/input) with error bars indicating s.d. (n=3). ns: not significant. *: p-value < 0.10. (B) Localization of GFP-Squ wildtype and mutants in S2 cells (upper panels). Scale bars: 5 µm. Co-localization of mK2-Spn-E and GFP-Squ wildtype or mutant proteins (except for the 4A mutant) are shown in lower panels. Scale bars: 5 µm. (C) Structural comparison of the Vasa-ssRNA complex (PDB: 2db3, left) and the predicted SpnE_Squ_Tej_RNA complex by AlphaFold3 (right). The Spn-E helicase domain is highlighted in red, with Vas superimposed for comparison. Both views are from the same orientation.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) SpnE_Squ_Tej. (B) Vas_Tej_Spn-E. (C) BoYb_Vret_Shu. (D) Me31B_Cup_Tral.PAE plots are also shown on the right. Orange lines indicate the protein boundaries.

The closer examination of the Spn-E_Squ dimer interface revealed a short α-helix of Squ (106th–116th residues) fitted into a groove on the Spn-E surface, while the anti-parallel β-sheet (140th–153rd) was also predicted to interact with Spn-E (Figure 2A and C). Physico-chemical structural analysis using PDBePISA server (EMBL-EBI) identified salt bridges between Spn-E and Squ (Supplementary file 3; Supplementary file 4; Krissinel and Henrick, 2007). To validate these predicted interactions, we generated Squ mutants substituting each residue involved in the four salt bridges (E107, E109, R115, and K163) with alanine (Figure 2D, Figure 2—figure supplement 1B) and assessed their interactions by co-immunoprecipitation in S2 cells expressing tagged proteins, Myc-Spn-E and Flag-Squ. The assay revealed that while the E107A single mutation did not affect the interaction, other single mutations mildly reduced the binding affinity of Squ to Spn-E (Figure 2—figure supplement 2A), Furthermore, the localization of GFP-tagged Squ and mKate2 (mK2)-tagged Spn-E was examined in S2 cells. When only Squ was expressed, it was dispersed in cytosol (Figure 2—figure supplement 2B). On the other hand, when only Spn-E was expressed, it localized in the nucleus as reported previously (Lin et al., 2023). In the co-expression of Squ wildtype or single mutants, Spn-E was moved to the cytoplasm and form granules together with Squ, suggesting the interaction between them. Although the single mutants still could bind to Spn-E, Squ quadruple mutant (Squ4A) completely lost the binding (Figure 2E) and did not show the co-localization with Spn-E in S2 cells (Figure 2—figure supplement 2B). These results suggest that the salt bridges are important for the interaction between Spn-E and Squ and support the accuracy of their dimer structure predicted by AlphaFold2.

While the RNA binding site of Spn-E has not been extensively studied, it is presumed to be near the helicase domain, similar to the Vas helicase-RNA complex (Sengoku et al., 2006). In addition, Lin et al., 2023 demonstrated that Hel-C domain of Spn-E interacted with the Tej’s eSRS region, which recruits Spn-E to nuage, a site distinct from the predicted Squ binding sites (Figure 2A). Interestingly, a tetramer complex of Spn-E_Squ_Tej_RNA predicted by the recently available AlphaFold3 (Abramson et al., 2024) placed the single-strand RNA (ssRNA) near Spn-E’s helicase domain (Figure 2F), aligning with the ssRNA binding position found in Vas (Figure 2—figure supplement 2C). The predicted tetramer model suggests that Squ binding to Spn-E does not inhibit but may potentially regulate Spn-E’s interaction with Tej or RNA by stabilizing the domain orientation of Spn-E (Figure 2F).

In addition to the Spn-E_Squ_Tej complex, 1:1 dimer prediction described above further suggested potential trimers (Figure 1, Figure 2—figure supplement 3). For example, Tej protein is predicted to bind both Vas and Spn-E, and AlfaFold3 indeed further predicted a Vas_Tej_Spn-E trimer, where Tej’s Lotus and eTud domains interact with Vas and Spn-E, respectively. However, Lin et al. reported that Tej binds exclusively either with Vas or Spn-E, but not simultaneously, in Drosophila ovary (Lin et al., 2023), suggesting that the predicted trimers may be weak or transient. Similarly, the BoYb_Vret_Shu and the Me31B_Cup_Tral trimers remain hypothetical and require experimental verification (Figure 2—figure supplement 3).

We investigated whether Spn-E also interacts with Squ within the Drosophila ovary. The antibody against Squ detected a specific band at the expected size by western blotting in the heterozygous control ovarian lysate, which was absent in the transheterozygote mutant, squPP32/HE47 (Figure 3A; Pane et al., 2007). Consistent with the previous report conducted with the transgenic line expressing HA-Squ (Pane et al., 2007), immunostaining of ovaries revealed the Squ’s localization in nuage, which overlaps with endogenously-tagged Spn-E with mK2 (Figure 3B). Spn-E was co-immunoprecipitated together with Squ from ovarian lysate, indicating the interaction between Squ and Spn-E (Figure 3C). While the previous mass spectrometry analysis detected PIWI family proteins, Piwi, Aub, and AGO3, in Spn-E immunoprecipitates (Andress et al., 2016), these three proteins were not present in the immunoprecipitant of Squ (Figure 3C), further supporting the direct interaction between Squ and Spn-E.

![Figure 3.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig3-v1.jpg)

**Figure 3.:** (A) Western blotting analysis using anti-Squ antibody reveals a specific band at the expected size (approximately 28 kDa) for endogenous Squ in Drosophila ovarian lysates of the heterozygous control. This band is absent in the transheterozygote, squPP32/HE47. (B) Immunostaining of Drosophila egg chambers with anti-Squ antibody and anti-mKate2 (mK2) antibody demonstrates colocalization of Squ and Spn-E-mK2 in nuage, a perinuclear granule in germline cells. The enlarged images of nuclei are shown in the panels below. Scale bars: 10 μm (top row), 2.5 μm (enlarged images). (C) Immunoprecipitation of the endogenous Squ from ovarian lysate revealed the interaction with Spn-E protein. Proteins were detected by western blotting analysis using the specific antibody for each protein. The negative control was performed without anti-Squ antibody (beads only).

In this study, three novel protein–protein interactions were predicted and experimentally confirmed. AlphaFold2 also predicted the 3D structure of these complexes, providing insight into the important regions involved in complex formation. These predictions will provide fundamental information to elucidate nuage assembly. Nuage is thought to form by liquid-phase separation; however, direct protein–protein interactions likely occur within protein-dense nuage, facilitating RNA processing. Although the precise roles of individual interactions require further study, characterization of protein–protein interactions within nuage will help clarify the mechanism of piRNA production.

### Screening oogenesis-related proteins for interaction with nuage proteins

Given the role of nuage for piRNA biogenesis and germline development, interactions between nuage-localized proteins and those involved in oogenesis were expected. We employed AlphaFold2 to predict these interactions using Vas, Squ, and Tej, the representative nuage components yet remain elusive, as baits. Of 430 proteins in oogenesis pathway (Aleksander et al., 2023), dimeric binding of 1290 pairs was predicted (Supplementary file 5), with 18 pairs showing dimer structures scoring above 0.6 (Table 3). Among those, co-immunoprecipitation in S2 cells confirmed interactions of three pairs, Mei-W68_Squ, CSN3_Squ, and Pka-C1_Tej (Figure 4A and B, Table 3). The Mei-W68_Squ dimer, scoring 0.63, the binding site of Squ to Mei-W68 was predicted at α-helixes in its middle region, which overlaps with the interacting site to Spn-E (Table 3, Figure 4Ai, compare with Figure 1Cviii). Mei-W68 is a topoisomerase, known as Spo11 in many organisms, which is required for the formation of double-strand breaks during meiosis (McKim and Hayashi-Hagihara, 1998). Interestingly, Squ also plays a role in DNA damage response pathway and showed the genetic interaction with chk2, a meiotic checkpoint gene (Pane et al., 2007). These results suggest that the binding of Squ to Mei-W68 may regulate the enzymatic activity of Mei-W68 in order to suppress the excessive formation of double-strand breaks. Another confirmed pair was CSN3_Squ pair scoring 0.62 (Figure 4Aii and Bii). CSN3, a component of COP9 signalosome which removes Nedd8 modifications from target proteins, is required for the self-renewal of the germline stem cells (Pan et al., 2014). Pka-C1, a cAMP-dependent protein kinase involved in axis specification, rhythmic behavior and synaptic transmission (Öztürk-Çolak et al., 2024) and predicted to bind with the N-terminal Lotus domain of Tej (Score 0.64, Figure 4Aiii and Biii), which is also known as binding site to Vas (Jeske et al., 2017). This suggests a potential competitive interaction between Pka-C1 and Vas for Tej. Although the success rate of confirmed interactions was low (3 out of 18) (Table 3, Figure 4—figure supplement 1), the results indicate that these protein pairs could interact within cells if co-expressed in vivo. The ranking confidence score reflects the reliability of AlphaFold2’s predicted structure but does not always ensure accuracy. Therefore, we assessed complex affinity based on the predicted three-dimensional structures (Xue et al., 2016; Supplementary file 6). Most dimers with high-ranking confidence scores exhibited low Kd values indicative of high affinity, while some showed high Kd values indicating weak interactions (Supplementary file 6). For example, the Baf_Vas complex had a high AlphaFold2 ranking confidence score (0.85) but a relatively high Kd value (1.1E-4 M), indicating low affinity. Consistently, Baf_Vas binding was not detected in co-IP experiments (Figure 4—figure supplement 1C). Although accurate Kd prediction may be limited due to insufficient structural optimization, it could serve as a valuable secondary screening tool following AlphaFold2 predictions.

![Figure 4.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig4-v1.jpg)

**Figure 4.:** (Ai–iii) The predicted dimer structures (top) and Predicted Aligned Error (PAE) plots (bottom) of Mei-W68 in blue and Squ in magenta (i), CSN3 in green and Squ in magenta (ii), Pka-C1 in orange and Tej in cyan (iii). The PAE plot displays the positional errors between all amino acid residue pairs, formatted in a matrix layout. (Bi–iii) Co-immunoprecipitation assays using tagged proteins to verify interactions between specific pairs: Mei-W68_Squ (i), CSN3_Squ (ii), and Pka-C1_Tej (iii). Single transfected cells expressing only Myc-tagged but not Flag-tagged proteins are used as negative controls for each set. Box and whisker plots show the intensity ratio between immunoprecipitated and input bands (n = 3 biological replicates). p-values were calculated using Student’s t-test.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Examination of Squ-interacting candidates predicted by AlphaFold2. (B) Examination of Tej-interacting candidates predicted by AlphaFold2. (C) Examination of Vas-interacting candidates predicted by AlphaFold2.In all the experiments, Flag-tagged proteins are immunoprecipitated and blotted with anti-Myc and anti-Flag antibodies. Single-transfection of Myc-tagged proteins serve as controls.

**Table 3.**
 The binding candidates predicted by AlphaFold2.


<table>
  <thead>
    <tr>
      <th>Protein_A</th>
      <th>Protein_B</th>
      <th>AlphaFold2ranking confidence</th>
      <th>Validation by co-IP</th>
      <th>Function of Protein_A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vps25</td>
      <td>Squ</td>
      <td>0.71</td>
      <td>No</td>
      <td>A member of the ESCRT-II complex</td>
    </tr>
    <tr>
      <td>Nup44A</td>
      <td>Squ</td>
      <td>0.65</td>
      <td>No</td>
      <td>A nuclear pore protein</td>
    </tr>
    <tr>
      <td>Nclb</td>
      <td>Squ</td>
      <td>0.64</td>
      <td>No</td>
      <td>Chromatin-associated factor</td>
    </tr>
    <tr>
      <td>Mei-W68</td>
      <td>Squ</td>
      <td>0.63</td>
      <td>Bound</td>
      <td>Formation of double-strand breaks</td>
    </tr>
    <tr>
      <td>DNaseII</td>
      <td>Squ</td>
      <td>0.63</td>
      <td>N/E</td>
      <td>Deoxyribonuclease II</td>
    </tr>
    <tr>
      <td>Spn-D</td>
      <td>Squ</td>
      <td>0.62</td>
      <td>No</td>
      <td>Homologous recombinational DNA repair</td>
    </tr>
    <tr>
      <td>CSN3</td>
      <td>Squ</td>
      <td>0.62</td>
      <td>Bound</td>
      <td>Subunit of the COP9 signalosome</td>
    </tr>
    <tr>
      <td>Jagn</td>
      <td>Tej</td>
      <td>0.72</td>
      <td>No</td>
      <td>Located in the endoplasmic reticulum</td>
    </tr>
    <tr>
      <td>Pka-C1</td>
      <td>Tej</td>
      <td>0.64</td>
      <td>Bound</td>
      <td>Serine/threonine kinase</td>
    </tr>
    <tr>
      <td>Rab7</td>
      <td>Tej</td>
      <td>0.62</td>
      <td>No</td>
      <td>Vesicle trafficking regulation</td>
    </tr>
    <tr>
      <td>Baf</td>
      <td>Vas</td>
      <td>0.85</td>
      <td>No</td>
      <td>Chromatin organization</td>
    </tr>
    <tr>
      <td>Mats</td>
      <td>Vas</td>
      <td>0.79</td>
      <td>No</td>
      <td>Coactivator of Warts (Wts) kinase</td>
    </tr>
    <tr>
      <td>Abo</td>
      <td>Vas</td>
      <td>0.68</td>
      <td>No</td>
      <td>Negative regulator of histone transcription genes</td>
    </tr>
    <tr>
      <td>CathD</td>
      <td>Vas</td>
      <td>0.67</td>
      <td>N/E</td>
      <td>Apoptosis and the defense response</td>
    </tr>
    <tr>
      <td>Rab11</td>
      <td>Vas</td>
      <td>0.67</td>
      <td>No</td>
      <td>Endomembrane trafficking</td>
    </tr>
    <tr>
      <td>Vls</td>
      <td>Vas</td>
      <td>0.63</td>
      <td>No</td>
      <td>Substrate recognition platform for cusl</td>
    </tr>
    <tr>
      <td>Hsc70-4</td>
      <td>Vas</td>
      <td>0.62</td>
      <td>No</td>
      <td>Protein folding</td>
    </tr>
    <tr>
      <td>RhoL</td>
      <td>Vas</td>
      <td>0.61</td>
      <td>N/E</td>
      <td>Maturation of hemocytes</td>
    </tr>
  </tbody>
</table>

_The expression plasmids were not constructed due to the technical reasons.N/E, not examined._

### Screening all Drosophila proteins for Piwi-interacting proteins

Given the crucial role of Piwi in piRNA biogenesis, heterochromatin formation, and germline stem cell (GSC) maintenance, we employed AlfaFold2 to screen all proteins in D. melanogaster for potential Piwi interactions. Piwi, the founder member of the PIWI family proteins, is not only essential for binding piRNAs and regulating complementary mRNAs but also plays a critical role in GSC self-renewal (Klenov et al., 2011). Studies have shown that Piwi, lacking the N-terminal moiety containing the nuclear localization signal (NLS), still retains GSC self-renewal capabilities. Its function in GSC self-renewal is realized independently in the cytoplasm of GSC niche cells, separate from its role in transposon repression. The crystal structures of Drosophila Piwi and silkworm Siwi have been solved and revealed the organization of four domains (N, PAZ, MID, and PIWI) (Matsumoto et al., 2016; Yamaguchi et al., 2020). Recently, the ternary structure of piRNA, target RNA, and MILI, a mouse ortholog of Piwi, has been reported and the bound piRNA threaded through the channel between N-PAZ and MID–PIWI lobes (Figure 5—figure supplement 1A; Li et al., 2024).

To identify novel Piwi-binding proteins, we conducted a 1:1 interaction screening involving approximately 12,000 Drosophila proteins, excluding any proteins over 2000 amino acid residues due to the computational limits. The ranking confidences by AlphaFold2 were primarily low, with over 98% being below 0.6, suggesting a low likelihood of interaction between Piwi and the vast majority of the proteins (Figure 5A). Approximately 1.5% of the pairs, totaling 164 pairs, scored above 0.6, was expected to contain the novel binding partners (Supplementary file 7). Top 24 candidates with greater than 0.75 ranking confidence are listed in Table 4. This list contained many metabolic enzymes and three piRNA-related proteins, Asterix (Arx), Mael, and Hen1. The interactions between Mael and Piwi-family proteins have been already reported (Namba et al., 2022). Arx, known as Gtsf1 in mammals and integral to Piwi–piRISC-mediated transcriptional silencing in nucleus (Ohtani et al., 2013), had high ranking confidences (0.83, Table 4). Despite its known three-dimensional structure determined by NMR spectroscopy (Ipsaro et al., 2021), the Arx_Piwi complex structure remained elusive. AlphaFoldF2 predicted that while Arx lacked a compact domain, the majority of Arx protein associated around the PIWI domain, except for the flexible C-terminal region (130th–167th residues) (Figure 5Bi). Three Arx paralogs in Drosophila (CG34283, CG32625, and CG14036) were also predicted to bind to Piwi with high-ranking confidences, suggesting their interactions within the cells (Figure 5—figure supplement 1B). Although CG34283 is not expressed, CG32625 and CG14036 are moderately and highly expressed in ovary, respectively (Öztürk-Çolak et al., 2024). However, unlike arx, knockdown of each paralogous gene did not result in de-repression of a transposon, mdg1 (Ohtani et al., 2013), suggesting that they may be pseudogenes or possess redundant roles.

![Figure 5.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig5-v1.jpg)

**Figure 5.:** (A) Pie chart displaying the distribution of ranking confidences from the AlphaFold2 screening for Piwi-interacting proteins among those encoded by Drosophila genome. (Bi–v) The predicted dimer structure (top) and PAE plots (bottom) for the Piwi and the binding candidates in red: Arx (i), Hen1 (ii), CG33703 (iii), Twf (iv), and Brn (v). Piwi is shown in the same colors as Figure 5—figure supplement 1A. (C) Co-immunoprecipitation assays using tagged proteins to verify interactions between Piwi and the binding candidates, Twf and Brn. Single transfected cells expressing only Flag-Piwi is used as negative control. Box and whisker plots show the intensity ratio between immunoprecipitated and input bands (n = 3 biological replicates). p-values were calculated using Student’s t-test.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/101967/elife-101967-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) The ternary complex of mouse Piwi ortholog (MILI), piRNA, and the target RNA determined by cryo-EM (PDB: 7YFY). (B) PAE plots for the predicted dimer structures of Piwi and Arx paralogs in Drosophila melanogaster. (C) PAE plots for the predicted dimer structures of Piwi and CG33703 paralogs in Drosophila melanogaster.

**Table 4.**
 Piwi-interacting proteins predicted by AlphaFold2 (score ≥ 0.75).


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Length (residue)</th>
      <th>Ranking confidence</th>
      <th>Human ortholog</th>
      <th>Gene summary (FlyBase)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CG34283</td>
      <td>153</td>
      <td>0.85</td>
      <td>GTSF1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CG32625</td>
      <td>144</td>
      <td>0.84</td>
      <td>GTSF1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Arx</td>
      <td>167</td>
      <td>0.83</td>
      <td>GTSF1</td>
      <td>It plays an essential role in piRNA-guided transcriptional silencing, interacting probably directly with the product of piwi</td>
    </tr>
    <tr>
      <td>CG33703</td>
      <td>181</td>
      <td>0.82</td>
      <td>-</td>
      <td>No phenotypic data is available</td>
    </tr>
    <tr>
      <td>GstE12</td>
      <td>223</td>
      <td>0.82</td>
      <td>GSTT2B</td>
      <td>Glutathione S transferase E12 (GstE12) encodes an enzyme involved in glutathione metabolism</td>
    </tr>
    <tr>
      <td>CAH4</td>
      <td>279</td>
      <td>0.81</td>
      <td>CA6</td>
      <td>Predicted to enable carbonate dehydratase activity. Predicted to be active in cytoplasm</td>
    </tr>
    <tr>
      <td>CG13192</td>
      <td>323</td>
      <td>0.81</td>
      <td>GNB1L</td>
      <td>Predicted to be involved in social behavior</td>
    </tr>
    <tr>
      <td>Mael</td>
      <td>462</td>
      <td>0.79</td>
      <td>MAEL</td>
      <td>Involved both in the piRNA and miRNA metabolic processes</td>
    </tr>
    <tr>
      <td>Adk3</td>
      <td>366</td>
      <td>0.78</td>
      <td>ADK</td>
      <td>Predicted to enable adenosine kinase activity</td>
    </tr>
    <tr>
      <td>Alg11</td>
      <td>475</td>
      <td>0.78</td>
      <td>ALG11</td>
      <td>Predicted to enable GDP-Man:Man3GlcNAc2-PP-Dol alpha-1,2-mannosyltransferase activity</td>
    </tr>
    <tr>
      <td>CG41378</td>
      <td>228</td>
      <td>0.78</td>
      <td>IFI30</td>
      <td>Predicted to enable oxidoreductase activity</td>
    </tr>
    <tr>
      <td>CG14036</td>
      <td>93</td>
      <td>0.77</td>
      <td>GTSF1</td>
      <td>Involved in copper ion homeostasis</td>
    </tr>
    <tr>
      <td>CG7966</td>
      <td>486</td>
      <td>0.77</td>
      <td>SELENBP1</td>
      <td>Predicted to enable methanethiol oxidase activity</td>
    </tr>
    <tr>
      <td>Hen1</td>
      <td>391</td>
      <td>0.77</td>
      <td>HENMT1</td>
      <td>Hen1 encodes a methyltransferase that methylates the terminal 2' hydroxyl group of small interfering RNAs and Piwi-interacting RNAs</td>
    </tr>
    <tr>
      <td>Rpp14b</td>
      <td>112</td>
      <td>0.77</td>
      <td>RPP14</td>
      <td>Predicted to enable ribonuclease P RNA binding activity</td>
    </tr>
    <tr>
      <td>CG33783</td>
      <td>164</td>
      <td>0.76</td>
      <td>-</td>
      <td>No phenotypic data is available</td>
    </tr>
    <tr>
      <td>AANATL4</td>
      <td>224</td>
      <td>0.75</td>
      <td>-</td>
      <td>Predicted to enable aralkylamine N-acetyltransferase activity</td>
    </tr>
    <tr>
      <td>CG14787</td>
      <td>260</td>
      <td>0.75</td>
      <td>CDYL2</td>
      <td>Is expressed in adult heart; embryonic Malpighian tubule; and embryonic main segment of Malpighian tubule</td>
    </tr>
    <tr>
      <td>CG33160</td>
      <td>258</td>
      <td>0.75</td>
      <td>PRSS1</td>
      <td>Predicted to enable serine-type endopeptidase activity</td>
    </tr>
    <tr>
      <td>CG3397</td>
      <td>342</td>
      <td>0.75</td>
      <td>AKR7A2</td>
      <td>Predicted to enable D-arabinose 1-dehydrogenase [NAD(P)+] activity</td>
    </tr>
    <tr>
      <td>CG4390</td>
      <td>330</td>
      <td>0.75</td>
      <td>ESD</td>
      <td>Enables serine hydrolase activity</td>
    </tr>
    <tr>
      <td>CG7142</td>
      <td>334</td>
      <td>0.75</td>
      <td>KLK1</td>
      <td>Predicted to enable serine-type endopeptidase activity</td>
    </tr>
    <tr>
      <td>JanA</td>
      <td>135</td>
      <td>0.75</td>
      <td>PHPT1</td>
      <td>JanA and janB regulate somatic sex differentiation</td>
    </tr>
    <tr>
      <td>Yip7</td>
      <td>270</td>
      <td>0.75</td>
      <td>CTRB1</td>
      <td>Enables serine hydrolase activity</td>
    </tr>
  </tbody>
</table>

Hen1 is a methyltransferase known to mediate methylation of the terminal 2' hydroxyl group of small interfering RNAs and piRNAs, thereby enhancing the stability of the small RNAs. Consistent with the previous report showing Hen1 binding to Piwi (Ohtani et al., 2013), the dimer structure of Hen1_Piwi was predicted with high-ranking confidence, 0.77. This prediction further suggests that Hen1 is recruited to Piwi, thereby positioning it closer to the piRNA substrate (Figure 5Bii). Another potential interacting protein for Piwi was CG33703, a protein whose functions remains uncharacterized despite having 75 paralogs listed in Drosophila genome (Öztürk-Çolak et al., 2024). Together with three of these paralogs (CG33783, CG33647, and CG33644), CG33703 was predicted to form dimer with Piwi (ranking confidences 0.82) (Table 4, Figure 5—figure supplement 1C). The domain of unknown function, DUF1091 (Letunic et al., 2021), shared by these paralogs was predicted to associate with the PIWI-domain (Figure 5Biii). Although these proteins are generally not expressed under the normal conditions (Öztürk-Çolak et al., 2024), their potential to bind Piwi suggests a regulatory role in the abnormal or stress conditions where CG33703 or its paralogs are expressed. In addition, we investigated two oogenesis-related proteins, Twinfilin (Twf, ranking confidence 0.64, Figure 5Biv) and Brainiac (Brn, ranking confidence 0.63, Figure 5Bv), for their binding with Piwi through co-immunoprecipitation (Figure 5C, Supplementary file 7). While no binding was observed with Twf, significant binding was detected with Brn, which is involved in dorsal-ventral polarity determination in follicle cells (Goode et al., 1996).

This study identifies several potential protein interactions, but AlphaFold2 predictions require caution. Protein–protein interactions involve conformational changes and dependencies on ligands, ions, and cofactors, which AlphaFold2 does not consider, potentially reducing prediction accuracy. Notably, the presence of a high-scoring model in terms of structural complementarity does not guarantee that the interaction is biologically significant. The expression patterns of these candidate proteins within the organism are crucial for further validation of our findings. It is likely that these proteins interact when co-expressed in the same cellular context. Under typical growth conditions, these interactions might not occur; however, in stress or disease states where these proteins are upregulated, the likelihood of interaction increases, potentially implicating these interactions in the disruption of normal cellular functions and contributing to disease or tumorigenesis. Furthermore, in silico screening proves extremely valuable, especially when dealing with toxic bait proteins, as it allows us to narrow down the list of potential candidates and reduce the need for hazardous experimental procedures. Ultimately, establishing these potential interactions in vivo could significantly advance our understanding of protein functions under both normal and pathological conditions.

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
      <td>Gene (Drosophila melanogaster)</td>
      <td>Vas</td>
      <td>FlyBase</td>
      <td>FBgn0283442</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Spn-E</td>
      <td>FlyBase</td>
      <td>FBgn0003483</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D .melanogaster)</td>
      <td>Tej</td>
      <td>FlyBase</td>
      <td>FBgn0033921</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Tapas</td>
      <td>FlyBase</td>
      <td>FBgn0027529</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Qin</td>
      <td>FlyBase</td>
      <td>FBgn0263974</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Kots</td>
      <td>FlyBase</td>
      <td>FBgn0038191</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Krimp</td>
      <td>FlyBase</td>
      <td>FBgn0034098</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Squ</td>
      <td>FlyBase</td>
      <td>FBgn0267347</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Mael</td>
      <td>FlyBase</td>
      <td>FBgn0016034</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Aub</td>
      <td>FlyBase</td>
      <td>FBgn0000146</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>AGO3</td>
      <td>FlyBase</td>
      <td>FBgn0250816</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Papi</td>
      <td>FlyBase</td>
      <td>FBgn0031401</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Vret</td>
      <td>FlyBase</td>
      <td>FBgn0263143</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Bel</td>
      <td>FlyBase</td>
      <td>FBgn0263231</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Zuc</td>
      <td>FlyBase</td>
      <td>FBgn0261266</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Cup</td>
      <td>FlyBase</td>
      <td>FBgn0000392</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Tral</td>
      <td>FlyBase</td>
      <td>FBgn0041775</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Me31B</td>
      <td>FlyBase</td>
      <td>FBgn0004419</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Shu</td>
      <td>FlyBase</td>
      <td>FBgn0003401</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>BoYb</td>
      <td>FlyBase</td>
      <td>FBgn0037205</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Piwi</td>
      <td>FlyBase</td>
      <td>FBgn0004872</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Mei-W68</td>
      <td>FlyBase</td>
      <td>FBgn0002716</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>CSN3</td>
      <td>FlyBase</td>
      <td>FBgn0027055</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Pka-C1</td>
      <td>FlyBase</td>
      <td>FBgn0000273</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Twf</td>
      <td>FlyBase</td>
      <td>FBgn0038206</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Brn</td>
      <td>FlyBase</td>
      <td>FBgn0000221</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Vps25</td>
      <td>FlyBase</td>
      <td>FBgn0022027</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Nup44A</td>
      <td>FlyBase</td>
      <td>FBgn0033247</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Nclb</td>
      <td>FlyBase</td>
      <td>FBgn0263510</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Spn-D</td>
      <td>FlyBase</td>
      <td>FBgn0003482</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Jagn</td>
      <td>FlyBase</td>
      <td>FBgn0037374</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Rab7</td>
      <td>FlyBase</td>
      <td>FBgn0015795</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Baf</td>
      <td>FlyBase</td>
      <td>FBgn0031977</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Mats</td>
      <td>FlyBase</td>
      <td>FBgn0038965</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Abo</td>
      <td>FlyBase</td>
      <td>FBgn0000018</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Rab11</td>
      <td>FlyBase</td>
      <td>FBgn0015790</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Vls</td>
      <td>FlyBase</td>
      <td>FBgn0003978</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Hsc70-4</td>
      <td>FlyBase</td>
      <td>FBgn0266599</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5α</td>
      <td>Takara</td>
      <td>Cat# 9057</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w-; squHE47 cn bw/CyO; TM3 Sb/TM6 Tb</td>
      <td>Pane et al., 2007</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; squpp32/CyO; TM3 Sb/TM6 Tb</td>
      <td>Pane et al., 2007</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (D. melanogaster)</td>
      <td>S2</td>
      <td>DRSC</td>
      <td>FLYB:FBtc0000181; RRID:CVCL_Z992</td>
      <td>Cell line maintained in T. Kai lab</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Squ (rat polyclonal)</td>
      <td>This study</td>
      <td></td>
      <td>IF (1:5000)WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Spn-E (rat polyclonal)</td>
      <td>Lin et al., 2023</td>
      <td></td>
      <td>WB (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Ago3 (rat polyclonal)</td>
      <td>Lin et al., 2023</td>
      <td></td>
      <td>WB (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Aub (guinea pig polyclonal)</td>
      <td>Lim et al., 2022</td>
      <td></td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Piwi (mouse monoclonal G-1)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc-390946</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-α-Tubulin (mouse monoclonal DM1A)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc-32293; RRID:AB_628412</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-guinea pig HRP-conjugated (rabbit polyclonal)</td>
      <td>Dako</td>
      <td>Cat # P0141; RRID:AB_628412</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rat HRP-conjugated (rabbit polyclonal)</td>
      <td>Dako</td>
      <td>Cat # P0450; RRID:AB_2630354</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse HRP-conjugated (goat polyclonal)</td>
      <td>Bio-Rad</td>
      <td>Cat # 1706516; RRID:AB_2921252</td>
      <td>WB (1:3000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit HRP-conjugated (goat polyclonal)</td>
      <td>Bio-Rad</td>
      <td>Cat # 1706515; RRID:AB_11125142</td>
      <td>WB (1:3000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-DDDDK-tag HRP-conjugated (mouse monoclonal)</td>
      <td>MBL</td>
      <td>Cat# M185-7; RRID:AB_2687989</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Myc-tag HRP-conjugated (mouse monoclonal)</td>
      <td>MBL</td>
      <td>Cat# M192-7; RRID:AB_3678890</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Spn-E (plasmid)</td>
      <td>Lin et al., 2023</td>
      <td></td>
      <td>Myc-tag mK2-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Aub (plasmid)</td>
      <td>Patil and Kai, 2010</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>BoYb (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tagFlag-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Me31B (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Vret (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Shu (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SquWT (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tagGFP tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Squ4A (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tagGFP tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SquE107A (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tagGFP tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SquE109A (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tagGFP tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SquR115A (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tagGFP tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SquK163A (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tagGFP tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Tej (plasmid)</td>
      <td>Patil and Kai, 2010</td>
      <td></td>
      <td>Flag-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Vas (plasmid)</td>
      <td>Patil and Kai, 2010</td>
      <td></td>
      <td>Flag-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Mei-W68 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CSN3 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Pka-C1 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Vps25 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Nup44A (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Nclb (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Spn-D (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Jagn (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Rab7 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Baf (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Mats (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Abo (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Rab11 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Vls (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Hsc70-4 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Piwi (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Flag-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Twf (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Brn (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Myc-tag</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>anti-FLAG magnetic beads</td>
      <td>MBL</td>
      <td>Cat# M185-11R</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>anti-Myc magnetic beads</td>
      <td>Thermo Fisher</td>
      <td>Cat# 88842</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Dynabeads protein A</td>
      <td>Thermo Fisher</td>
      <td>Cat# 10001D</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Dynabeads protein G</td>
      <td>Thermo Fisher</td>
      <td>Cat# 10003D</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hilymax</td>
      <td>Dojindo</td>
      <td>Cat# 342-91103</td>
      <td>Transfection in S2</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Signal Enhancer HIKARI</td>
      <td>Nacalai Tesque</td>
      <td>Cat# 02270-81</td>
      <td>Western blotting</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Chemi-Lumi One reagent kit</td>
      <td>Nacalai Tesque</td>
      <td>Cat# 07880-54</td>
      <td>Western blotting</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fluoro-Keeper Antifade Reagent</td>
      <td>Nacalai Tesque</td>
      <td>Cat# 12593-64</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>AlphaFold v2.2</td>
      <td>Developed by DeepMind</td>
      <td>RRID:SCR_025454</td>
      <td>Installed in SQUID (Osaka University)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>Schneider et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Antibodies

The anti-Squ antibody was generated as follows. His-tagged full-length Squ was expressed in Escherichia coli BL21(DE3) strain, with the plasmid that subcloned the squ coding region into pDEST17 vector (Thermo Fisher Scientific). His-Squ was solubilized with 6 M urea in PBS, purified using Nickel Sepharose beads (GE healthcare) following the manufacturer’s protocol, and subsequently used for immunization in rats. The antibodies used for western blotting analysis were rat anti-Spn-E17 (1:500), rat anti-Ago317 (1:200), guinea pig anti-Aub (Lim et al., 2022) (1:1000), mouse monoclonal anti-Piwi (G-1, sc-390946, Santa Cruz Biotechnology, USA), and mouse monoclonal anti-α-Tubulin (DM1A, sc-32293, Santa Cruz Biotechnology). The secondary antibodies used in this study were HRP-conjugated goat anti-guinea pig (Dako, Cat# P0141), HRP-conjugated goat anti-rat (Dako, Cat# P0450), HRP-conjugated goat anti-mouse (Bio-Rad, Cat# 1706516), and HRP-conjugated goat anti-rabbit (Bio-Rad, Cat# 1706515). HRP-conjugated anti-DDDDK-tag antibody (MBL, Cat# M185-7) and HRP-conjugated anti-Myc-tag antibody (MBL, Cat# M192-7) were used to detect FLAG-tagged and Myc-tagged proteins, respectively.

### AlphaFold2 prediction for the direct interacting protein pairs

Amino acid sequences for Drosophila proteins were obtained from FlyBase (Öztürk-Çolak et al., 2024). For proteins annotated with multiple isoforms, only the longest isoform was selected. Proteins exceeding 2000 residues were excluded due to computational limitations. AlphaFold v2.2 program was installed in the Supercomputer for Quest to Unsolved Interdisciplinary Datascience (SQUID) at the Cyber Media Center in Osaka University. All necessary protein sequence databases for AlphaFold2 were stored on an SSD device connected to the SQUID system.

The AlphaFold2 prediction process was divided into two steps: generation of the multiple sequence alignment (MSA) and the prediction of the 3D structure. The MSAs were computed on SQUID’s CPU node and stored for reuse. The calculation of the MSA took on average 2–4 h per protein, with the more homologs of the protein in query, the longer it took. For dimer structure prediction, two MSAs corresponding to the dimer pair were placed in the directory of msas/A and msas/B. The calculations were performed on the GPU node with the options of -t 2022-05-14 -m multimer -l 1 -p true. AlphaFold2 generates five structural models for each prediction. To speed up the prediction, five computations were assigned to five GPU units, even though the original AlphaFold2 program computes five models one at a time. Prediction of dimer structure took approximately 1–2 h per pair on average, depending on protein size. Each user can compute 100–200 pairs of calculations per day, but since the supercomputer is shared, job availability varies with overall demand.

The prediction confidence score (ranking confidence) was provided for each model, and among five models, the highest ranking confidence was used as the prediction score for the corresponding dimer structure. PAE plots for dimer structures were drawn by extracting the data form pkl files generated by AlphaFold2. The list of protein pairs scoring above 0.6 and the corresponding PAE plots and PDB structures is available on GitHub (https://dme-research.github.io/AF2_2/).

### AlphaFold3 prediction for the structure of the trimer complex

The structure of Spn-E_Squ_Tej complexed with RNA, 5’-CUGACUACCGAAGUACUACG-3’ was predicted by the AlphaFold3 prediction server (https://alphafoldserver.com/) (Abramson et al., 2024). The trimer structures of Spn-E_Squ_Tej, Vas_Tej_Spn-E, BoYb_Vret_Shu, and Me31B_Cup_Tral were also predicted by AlphaFold3.

### Analysis of protein 3D structure

The protein 3D structure was visualized using ChimeraX software (Pettersen et al., 2021). The SpnE_Squ dimer interface was analyzed with the 'Protein interfaces, surfaces and assemblies' service (PISA) at the European Bioinformatics Institute (http://www.ebi.ac.uk/pdbe/prot_int/pistart.html; Krissinel and Henrick, 2007).

### Fly stocks

All stocks were maintained at 25℃ with standard methods. Mutant alleles of squ (squpp32 and squHE47) were used in this study (Pane et al., 2007). The mK2-tagged Spn-E-mK2 knock-in fly was previously generated (Lin et al., 2023). y w strain served as the control.

### Western blotting

Ovaries were homogenized in the ice-cold PBS and denatured in the presence of SDS sample buffer at 95°C for 5 min. The samples were then subjected to SDS-PAGE and transferred to ClearTrans SP PVDF membrane (Wako). The primary and secondary antibodies described above were diluted in the Signal Enhancer reagent HIKARI (Nacalai Tesque). Chemiluminescence was induced by the Chemi-Lumi One reagent kit (Nacalai Tesque) and detected with ChemiDoc Touch (Bio-Rad). The bands were quantified using ImageJ (Schneider et al., 2012) or Image Lab software (Bio-Rad).

### Co-immunoprecipitation in S2 cells

The Drosophila Schneider S2 cell line (S2-DRSC), derived from D. melanogaster embryos, was obtained from the Drosophila Genomics Resource Centre (DGRC) and is not listed among commonly misidentified cell lines. The S2 cells were cultured at 28°C in Schneider’s medium supplemented with 10% (v/v) fetal bovine serum and antibiotics (penicillin and streptomycin). Mycoplasma contamination was not detected using the VenorGeM Classic Mycoplasma Detection Kit (Minerva Biolabs). Protein coding regions were cloned into pENTR vector (Thermo Fisher Scientific) and then transferred into pAFW or pAMW destination vectors. S2 cells (0.2–2 × 106 cells/ml) were seeded in 12-well plates overnight and transfected using Hilymax (Dojindo Molecular Technologies, Japan). After 36–48 h, S2 cells were resuspended in 360 μl of ice-cold PBS containing 0.02% Triton-X100 and 1× protease inhibitor cocktail (Roche), and sonicated (0.5 s, five times). The resulted lysate was clarified by spinning at 15,000 × g for 15 min at 4°C. 300 μl of supernatant was incubated with 6 μl of prewashed anti-FLAG magnetic beads (MBL) or anti-Myc magnetic beads (Thermo Fisher Scientific) for 1.5 h at 4°C with gentle rotation. After incubation, the beads were washed three times with 800 μl of ice-cold PBS with 0.02% Triton-X100, denatured in SDS sample buffer and subjected to SDS-PAGE and western blot. 1% of the total lysates were loaded as input samples.

### Co-localization assay in S2 cells

Construction of GFP-tagged or mKate2-tagged proteins and transfection were conducted as described in the previous section. After 48 h of transfection, the cells were placed onto the concanavalin A-coated coverslips for 20 min, fixed with PBS containing 4% (w/v) paraformaldehyde for 15 min at room temperature, permeabilized with PBX (PBS containing 0.2% [v/v] TritonX-100) for 10 min twice, stained with DAPI (1:1000) and mounted with Fluoro-Keeper Antifade Reagent (Nacalai Tesque). Images were taken by ZEISS LSM 900 with Airy Scan 2 using ×63 oil NA 6.0 objectives and processed using ZEISS ZEN 3.0 and ImageJ (Schneider et al., 2012).

### Crosslinking immunoprecipitation (CL-IP)

As previously described (Lin et al., 2023), 100 ovaries from y w flies were dissected in ice-cold PBS and fixed in PBS containing 0.1% (w/v) paraformaldehyde for 20 min on ice, quenched in 125 mM glycine for 20 min, and then homogenized in CL-IP lysis buffer. The lysate was incubated at 4°C for 20 min and then sonicated. After centrifugation at maximum speed for 10 min at 4°C, the supernatant was collected and diluted with an equal volume of CL-IP wash buffer. 10 μl of pre-washed Dynabeads Protein G/A mixture (1:1) (Invitrogen) was added for pre-clearance at 4°C for 1 h. Anti-Squ antibody was added to the cleared supernatant with 1:500 dilution and incubated at 4°C overnight. The 20 μl of pre-washed Dynabeads Protein G/A 1:1 mixture beads (Invitrogen) were added for binding and incubated at 4°C for 3 h. After washed with CL-IP wash buffer for three times, beads were collected and 50 μl of CL-IP wash buffer containing SDS sample buffer was added. The beads were boiled at 95°C for 5 min and subjected for SDS-PAGE and western blotting analysis.

### Immunostaining of ovaries

As previously described (Lin et al., 2023; Lim et al., 2022), ovaries were dissected, fixed, permeabilized with PBX and immunostained. The primary and the secondary antibodies were anti-Squ antibody (in this study, 1:500) and Alexa Fluor 488-conjugated anti-rat IgG (Thermo Fisher Scientific, 1:200). Images were taken by ZEISS LSM 900 with Airy Scan 2 using ×63 oil NA 1.4 objectives and processed by ZEISS ZEN 3.0 and ImageJ (Schneider et al., 2012).
