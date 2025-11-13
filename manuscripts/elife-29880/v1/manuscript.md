# Inferring joint sequence-structural determinants of protein functional specificity

## Authors

- Andrew F Neuwald<sup>1</sup> ([ORCID: 0000-0002-0086-5755](https://orcid.org/0000-0002-0086-5755)) †
- L Aravind<sup>3</sup>
- Stephen F Altschul<sup>3</sup>

### Affiliations

1. Institute for Genome Sciences University of Maryland School of Medicine Baltimore United States
2. Department of Biochemistry and Molecular Biology University of Maryland School of Medicine Baltimore United States
3. National Center for Biotechnology Information, National Library of Medicine National Institutes of Health Bethesda United States

† Corresponding author

## Abstract

Residues responsible for allostery, cooperativity, and other subtle but functionally important interactions remain difficult to detect. To aid such detection, we employ statistical inference based on the assumption that residues distinguishing a protein subgroup from evolutionarily divergent subgroups often constitute an interacting functional network. We identify such networks with the aid of two measures of statistical significance. One measure aids identification of divergent subgroups based on distinguishing residue patterns. For each subgroup, a second measure identifies structural interactions involving pattern residues. Such interactions are derived either from atomic coordinates or from Direct Coupling Analysis scores, used as surrogates for structural distances. Applying this approach to N-acetyltransferases, P-loop GTPases, RNA helicases, synaptojanin-superfamily phosphatases and nucleases, and thymine/uracil DNA glycosylases yielded results congruent with biochemical understanding of these proteins, and also revealed striking sequence-structural features overlooked by other methods. These and similar analyses can aid the design of drugs targeting allosteric sites.

## Introduction

Residues remote from an enzyme’s active site can influence catalytic activity and substrate specificity. It has been proposed that an enzyme generally has multiple conformational states that modulate its function, with residues remote from the active site often shifting the enzyme’s conformational equilibrium to favor interactions associated with specific substrates or reactions (Ramanathan et al., 2014; Bhabha et al., 2015; Whitney et al., 2016; Campbell et al., 2016). Computational methods can help identify such functionally relevant non-active-site residues and their interactions. For example, direct coupling analysis (DCA) (Morcos et al., 2011), which predicts structural contacts from covarying residue pairs in a multiple sequence alignment (MSA), has been used to infer major conformational transitions for Hsp70 chaperones (Malinverni et al., 2015) and to explain the conformational heterogeneity seen in molecular dynamics simulations (Sutto et al., 2015). Statistical Coupling Analysis (SCA) (Lockless and Ranganathan, 1999) seeks to identify structural pathways of ‘energetic connectivity’ by applying principal component analysis to a covariance matrix to identify groups of coevolving residue positions (Halabi et al., 2009). SCA has been used to design proteins (Reynolds et al., 2013) and to predict surface sites (Reynolds et al., 2011) and hydrophobic cavities (Tanwar et al., 2013) involved in allosteric regulation. Here, we investigate residue interaction networks by combining two correlation analysis methods distinct from DCA and SCA (see Figure 7): Bayesian Partitioning with Pattern Selection (BPPS) (Neuwald, 2014a; Neuwald, 2014b), which identifies arbitrarily large correlated residue patterns arising through evolutionary divergence, and Structurally Interacting Pattern Residues’ Inferred Significance (SIPRIS), which we first describe here.

BPPS relies on the observation that protein superfamilies often diverge into subgroups, each adapting the superfamily’s structural core to fill a functional niche. Often a subgroup G diverges further into smaller subgroups, each conserving residues constrained by G’s function, as well as other residues constrained by more specialized functions. Repeated rounds of such divergence have led to hierarchically arranged subgroups, each of which conserves distinctive residues at particular positions. BPPS identifies and characterizes these subgroups by partitioning an MSA into a hierarchically nested series of MSAs, a hiMSA, based on correlated residue patterns that are distinctive of each subgroup and that often include non-active site residues.

For each subgroup of interest, the SIPRIS program takes a BPPS-defined residue pattern as input, as well as structural coordinates for a protein from that subgroup. It then identifies the statistically most significant network of pattern residues embedded within a structurally defined cluster, with a view to suggesting hypotheses for experimental investigation. Such a network is doubly significant inasmuch as BPPS identifies significant residue patterns in the absence of structural data, whereas SIPRIS defines structural clusters in the absence of sequence data. In this way, SIPRIS may statistically validate the output of BPPS or other sequence-based methods. Of course, a set of residues identified by a sequence-based method may still be biologically relevant despite a lack of SIPRIS-assigned significance. However, as we illustrate, BPPS-SIPRIS analyses often elucidate sequence/structural properties that conventional computational and experimental approaches have failed to detect.

## Results

SIPRIS takes as input: (1) structural coordinates for a protein of interest; (2) a set of residues defined by BPPS; and, optionally, (3) a predefined cluster of residues, or a starting residue defined either explicitly or as the residue closest to a ‘focal point’ molecule or atom. If a third input is absent, then SIPRIS uses each of the BPPS-defined residues as a starting residue, in turn, and returns the most significant result. Nested clusters are defined around a starting residue in one of three ways: (i) ‘Spherical expansion’, which sequentially adds residues closest to the starting residue, which thus forms the center of each cluster. (ii) ‘Core expansion’, which sequentially adds the residue closest to a residue within the cluster’s ‘core’. This core is defined as the starting residue R plus all cluster residues whose distance to their kth closest cluster residue is less than R’s distance to its kth closest cluster residue (with k = 7 by default; this was selected empirically to avoid both spherical- and tentacle-shaped clusters). In this case, the cluster typically expands less symmetrically. (iii) Hydrogen-bond-network expansion, which sequentially adds a residue forming the closest sidechain-to-sidechain or sidechain-to-backbone hydrogen bond with a cluster residue. (iv) For spherical or core clustering, SIPRIS may also take DCA scores (Marks et al., 2012, 2011) as a surrogate for 3D structural distances. SIPRIS evaluates the intersection between clusters and BPPS-defined residue sets with a p-value.

We applied BPPS-SIPRIS to a GCN5-like N-acetyltransferase (GNAT), several P-loop GTPases, an RNA Superfamily-II helicase, several members of the Synaptojanin/Exonuclease-Endonuclease-Phosphatase (EEP) superfamily, and two uracil/thymine DNA glycosylases. These results are summarized in Table 1. (Go to sipris.igs.umaryland.edu for BPPS output alignments.)

**Table 1.**
 Summary of BPPS-SIPRIS results for the most significant cluster in each test case.


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>PDB</th>
      <th>SIPRIS</th>
      <th>Focal</th>
      <th colspan="3">BPPS-SIPRIS‡</th>
      <th>SIPRIS</th>
      <th>Tree</th>
      <th>Interpretive comments#</th>
    </tr>
    <tr>
      <th></th>
      <th>Structure</th>
      <th>mode*</th>
      <th>point†</th>
      <th>Dist.</th>
      <th>Init.</th>
      <th>Term.</th>
      <th>p-value</th>
      <th>level§</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gna1</td>
      <td>4ag9A</td>
      <td>p=BDF</td>
      <td>-</td>
      <td>22</td>
      <td>57</td>
      <td>71</td>
      <td>8.5 × 10−7</td>
      <td>1</td>
      <td>Substrate and homodimeric interfaces</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>CoA</td>
      <td>17</td>
      <td>41</td>
      <td>87</td>
      <td>6.8 × 10−5</td>
      <td>0</td>
      <td>CoA-binding subdomain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>23</td>
      <td>56</td>
      <td>72</td>
      <td>9.3 × 10−6</td>
      <td>1</td>
      <td>DCA-based clustering</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>14</td>
      <td>21</td>
      <td>107</td>
      <td>2.5 × 10−4</td>
      <td>1</td>
      <td>Structure-based clustering</td>
    </tr>
    <tr>
      <td>Rho1</td>
      <td>3refB</td>
      <td>B</td>
      <td>-</td>
      <td>20</td>
      <td>53</td>
      <td>100</td>
      <td>8.3 × 10−5</td>
      <td>1</td>
      <td>(Active site secondary shell)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>C</td>
      <td>-</td>
      <td>22</td>
      <td>55</td>
      <td>98</td>
      <td>7.8 × 10−7</td>
      <td>1</td>
      <td>“ “ “ “</td>
    </tr>
    <tr>
      <td>Rab4</td>
      <td>1z0kA</td>
      <td>S</td>
      <td>-</td>
      <td>10</td>
      <td>11</td>
      <td>153</td>
      <td>2.1 × 10−5</td>
      <td>1</td>
      <td>(Active site secondary shell)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>C</td>
      <td>-</td>
      <td>25</td>
      <td>91</td>
      <td>73</td>
      <td>2.6 × 10−6</td>
      <td>1</td>
      <td>“ “ “ “</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>p=B</td>
      <td>-</td>
      <td>14</td>
      <td>23</td>
      <td>141</td>
      <td>2.9 × 10−8</td>
      <td>2</td>
      <td>Interface with Rabenosyn-5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>22</td>
      <td>42</td>
      <td>122</td>
      <td>4.8 × 10−10</td>
      <td>2</td>
      <td>“ “ “ “</td>
    </tr>
    <tr>
      <td>Rab8</td>
      <td>3qbtA</td>
      <td>p=B</td>
      <td>-</td>
      <td>13</td>
      <td>23</td>
      <td>139</td>
      <td>5.2 × 10−7</td>
      <td>2</td>
      <td>Interface with Ocrl1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>p=B</td>
      <td>-</td>
      <td>12</td>
      <td>23</td>
      <td>139</td>
      <td>6.1 × 10−6</td>
      <td>3</td>
      <td>Interface with Ocrl1 helix</td>
    </tr>
    <tr>
      <td></td>
      <td>4lhwB</td>
      <td>p=A</td>
      <td>-</td>
      <td>10</td>
      <td>14</td>
      <td>148</td>
      <td>8.7 × 10−7</td>
      <td>2</td>
      <td>Homodimeric interface</td>
    </tr>
    <tr>
      <td>EF-Tu</td>
      <td>1ob5A</td>
      <td>S</td>
      <td>-</td>
      <td>18</td>
      <td>33</td>
      <td>150</td>
      <td>1.4 × 10−7</td>
      <td>1</td>
      <td>(GTP to tRNA allosteric link)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>23</td>
      <td>71</td>
      <td>112</td>
      <td>1.0 × 10−6</td>
      <td>2</td>
      <td>(GTP/tRNA allosteric link to β-barrel)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>1B</td>
      <td>22</td>
      <td>81</td>
      <td>102</td>
      <td>1.3 × 10−5</td>
      <td>1</td>
      <td>Cluster around 5’ base 1 of tRNA</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>2B</td>
      <td>18</td>
      <td>47</td>
      <td>136</td>
      <td>2.6 × 10−6</td>
      <td>1</td>
      <td>Cluster around 5’ base 2 of tRNA</td>
    </tr>
    <tr>
      <td></td>
      <td>1efuA</td>
      <td>S</td>
      <td>81B</td>
      <td>14</td>
      <td>49</td>
      <td>128</td>
      <td>5.2 × 10−5</td>
      <td>1</td>
      <td>(Nucleotide exchange allosteric network)</td>
    </tr>
    <tr>
      <td></td>
      <td>4zv4A</td>
      <td>S</td>
      <td>291C</td>
      <td>21</td>
      <td>66</td>
      <td>109</td>
      <td>0.0060</td>
      <td>1</td>
      <td>(Mediates hijacking by Tse6 toxin)</td>
    </tr>
    <tr>
      <td>CysN</td>
      <td>1zunB</td>
      <td>S</td>
      <td>-</td>
      <td>23</td>
      <td>79</td>
      <td>118</td>
      <td>6.3 × 10−5</td>
      <td>2</td>
      <td>(Allosteric link to β-barrel domain)</td>
    </tr>
    <tr>
      <td>eIF4AIII</td>
      <td>3ex7H</td>
      <td>p=J</td>
      <td>-</td>
      <td>11</td>
      <td>18</td>
      <td>128</td>
      <td>6.4 × 10−6</td>
      <td>1</td>
      <td>(ATP to RNA allosteric link)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>4J</td>
      <td>13</td>
      <td>18</td>
      <td>128</td>
      <td>5.1 × 10−7</td>
      <td>1</td>
      <td>Cluster around RNA rotation bond</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>5J</td>
      <td>16</td>
      <td>41</td>
      <td>105</td>
      <td>5.5 × 10−4</td>
      <td>1</td>
      <td>“ “ “ “ “</td>
    </tr>
    <tr>
      <td>APE1</td>
      <td>5dfiA</td>
      <td>H</td>
      <td>11P</td>
      <td>9</td>
      <td>13</td>
      <td>238</td>
      <td>5.2 × 10-6</td>
      <td>0</td>
      <td>Abasic site H-bond network</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>H</td>
      <td>11P</td>
      <td>22</td>
      <td>99</td>
      <td>152</td>
      <td>1.6 × 10−6</td>
      <td>1</td>
      <td>“ “ “ “</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>H</td>
      <td>-</td>
      <td>25</td>
      <td>137</td>
      <td>114</td>
      <td>1.7 × 10−6</td>
      <td>1</td>
      <td>(Active site secondary shell)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>H</td>
      <td>9P</td>
      <td>25</td>
      <td>137</td>
      <td>114</td>
      <td>1.9 × 10−7</td>
      <td>1</td>
      <td>H-bond network positioning abasic site</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>H</td>
      <td>12P</td>
      <td>23</td>
      <td>119</td>
      <td>132</td>
      <td>7.6 × 10−6</td>
      <td>1</td>
      <td>“ “ “ “ “</td>
    </tr>
    <tr>
      <td>Inpp5b</td>
      <td>4cmlA</td>
      <td>S</td>
      <td>-</td>
      <td>24</td>
      <td>69</td>
      <td>216</td>
      <td>5.8 × 10−13</td>
      <td>0</td>
      <td>Active site core residues</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>21</td>
      <td>77</td>
      <td>208</td>
      <td>3.9 × 10−7</td>
      <td>1</td>
      <td>(Substrate recognition with allosteric link)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>12</td>
      <td>30</td>
      <td>255</td>
      <td>0.0022</td>
      <td>2</td>
      <td>(Membrane substrate sequestration)</td>
    </tr>
    <tr>
      <td>Inpp5b</td>
      <td>3mtcA</td>
      <td>S</td>
      <td>-</td>
      <td>22</td>
      <td>91</td>
      <td>194</td>
      <td>8.0 × 10−7</td>
      <td>1</td>
      <td>(Substrate recognition with allosteric link)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>12</td>
      <td>29</td>
      <td>256</td>
      <td>0.0015</td>
      <td>2</td>
      <td>(Membrane substrate sequestration)</td>
    </tr>
    <tr>
      <td>Inpp5e</td>
      <td>2xswA</td>
      <td>S</td>
      <td>-</td>
      <td>25</td>
      <td>140</td>
      <td>148</td>
      <td>3.7 × 10−7</td>
      <td>1</td>
      <td>(Substrate recognition with allosteric link)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>9</td>
      <td>13</td>
      <td>275</td>
      <td>3.6 × 10−4</td>
      <td>2</td>
      <td>(Membrane substrate sequestration)</td>
    </tr>
    <tr>
      <td>SHIP2</td>
      <td>4a9cA</td>
      <td>S</td>
      <td>-</td>
      <td>17</td>
      <td>38</td>
      <td>260</td>
      <td>6.0 × 10−8</td>
      <td>1</td>
      <td>(Substrate recognition with allosteric link)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>S</td>
      <td>-</td>
      <td>4</td>
      <td>4</td>
      <td>294</td>
      <td>0.30</td>
      <td>2</td>
      <td>(Membrane substrate sequestration)</td>
    </tr>
    <tr>
      <td>TDG</td>
      <td>5hf7A</td>
      <td>H</td>
      <td>17D</td>
      <td>19</td>
      <td>97</td>
      <td>76</td>
      <td>4.1 × 10−4</td>
      <td>1</td>
      <td>H-bond network around excised base</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>H</td>
      <td>-</td>
      <td>20</td>
      <td>98</td>
      <td>75</td>
      <td>3.5 × 10−5</td>
      <td>1</td>
      <td>H-bond network around catalytic water</td>
    </tr>
    <tr>
      <td>UDG</td>
      <td>2dp6A</td>
      <td>B</td>
      <td>-</td>
      <td>13</td>
      <td>17</td>
      <td>121</td>
      <td>1.7 × 10−5</td>
      <td>1</td>
      <td>H-bond network distinct from TDG</td>
    </tr>
  </tbody>
</table>

_*Modes: S, spherical expansion; C, core expansion; H, hydrogen bond expansion (involving sidechain interactions); B, hydrogen bond expansion (also involving backbone-to-backbone interactions); P, predefined clustering (residues in the cluster are those interacting with the chain(s) whose pdb identifiers are given to the right of the equal sign).†Focal points defining starting residue(s): ‘-‘,analysis was optimized over multiple starting residues (i.e., no focal point); CoA, cluster initiated from the residue closest to Coenzyme A; others, cluster initiated from the residue closest to the indicated position and chain (e.g., 1B = position 1 in pdb chain B).‡Nature of the optimum cluster: dist., the number of distinguishing residues within the cluster (total = 25); init., the total number of residues within the cluster; term., the number of residues outside of the cluster.§Codes designate pattern residue class: 0, superfamily; 1, family; 2, subfamily; 3, sub-subfamily. In the figures, these correspond to residues with yellow, red, orange and green sidechains, respectively.#Comments in parentheses indicate possible functions._

### Distinct N-acetyltransferase cofactor- and substrate-binding subdomains

GNATs catalyze the transfer of a carboxylic acyl group from Coenzyme A (acyl-CoA) to a diversity of substrates. Previously, a BPPS analysis of glucosamine-6-phosphate N-acetyltransferase (Gna1) led to two observations (Neuwald and Altschul, 2016a) (Figure 1): (1) Within the homodimeric structure of Gna1 (pdb: 4ag9) (Dorfmueller et al., 2012), BPPS-defined residues for this family are contributed by both subunits to form the dimeric interface and the active site for each subunit. In contrast, within a single subunit most of these residues are far from the active site and face away from it. Thus, the BPPS analysis implicates family-specific residues in the formation of this unusual substrate-binding pocket between subunits. (2) Residues conserved in the GNAT superfamily cluster within an acyl-CoA binding subdomain distinct from the homodimer/substrate interacting subdomain. This raises the question: How likely is such a structural distribution of these family and superfamily residues to have occurred by chance?

![Figure 1.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig1-v1.jpg)

**Figure 1.:** SIPRIS clearly associates Gna1-residues with the substrate and homodimeric interfaces (p=8.5 × 10−7). Color scheme: homodimer subunits A and B, green and blue backbones, respectively; BPPS-defined Gna1-family residues in subunits A and B, magenta and red sidechains, respectively (glycine residues are shown as Cα atom spheres); GNAT superfamily residues, yellow sidechains; ligands, cyan. Lys116 (shown in light red) is outside of the SIPRIS defined cluster, but forms a hydrogen bond to a CoA phosphate group. BPPS-SIPRIS spherical clustering identified the GNAT superfamily residues shown (p=1.7 × 10−5). The following figure supplement and source data are available for Figure 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Residue sets were defined using BPPS and three other programs (with default parameter settings). Residue color schemes: BPPS: NAT superfamily, yellow; Gna1-family, red; FRpred: conserved, yellow; subtype, red; CLIPS-1D: structurally important, yellow; ligand binding, orange; catalytic, red; ET: residues of high functional importance, orange; CoA and substrate, cyan. The SIPRIS predefined clustering p-values corresponding to the homodimer/substrate interface are indicated below each image.

SIPRIS returns a p-value of 8.5 × 10−7 for the intersection between Gna1-family residues and the predefined cluster of 57 residues contacting either the substrate or the other subunit (for residues conserved across GNATs, the corresponding p-value was 0.96). Among the 25 Gna1-family residues defined by BPPS, 22 intersect with the structurally defined cluster. The three remaining residues may perform complementary functions: Gly35 and Gly101 by imparting backbone flexibility and Lys116 by helping properly position CoA via interaction with a CoA phosphate group.

SIPRIS returns a p-value of 6.8 × 10−5 for the intersection between a (spherical) CoA-centered cluster and the set of residues conserved in all GNATs. (The corresponding p-value for Gna1-family residues is >0.99.) Of the 25 residues most distinctive of GNATs, 17 are among the 41 residues of this CoA-centered cluster. Hence, in the absence of explicit structural information, BPPS detects structurally and presumably biologically relevant features: GNAT-residues that map to an acetyl-CoA-binding module and Gna1-family residues that map to a substrate-specific ‘reaction chamber’ facilitating acetylation of glucosamine-6-phosphate.

### DCA-based SIPRIS analysis

Spherical clustering using residue-to-residue pseudo-distances based on DCA pairwise scores (instead of actual structural distances) likewise identifies these Gna1 structural features. In fact, the DCA-based p-value for Gna1-family residues (9.3 × 10−6) was more significant than the corresponding structurally based p-value (2.5 × 10−4). We suggest two possible reasons for this. First, DCA scores are based on multiple sequences (1200 in this case) and thus implicitly on multiple structures rather than one. Second, DCA scores should be affected by pairwise contacts between homodimeric subunits, whereas SIPRIS currently considers distances only within a single subunit. Thus, DCA- and structurally-based analyses provide somewhat different perspectives.

### Likely determinants of GTPase family and subfamily functional specificity

P-loop GTPases, upon binding to GTP versus GDP, undergo a conformational change in their so-called switch I and switch II regions that depends on the presence of a γ-phosphate group; this acts as a signal to downstream cellular components. We applied SIPRIS to two major subgroups: Rab/Rho/Ras/Ran GTPases (termed R4) and translation factor (TF) GTPases (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig2-v1.jpg)

**Figure 2.:** Bound guanine nucleotide (shown in cyan) allows orientation of each subfigure relative to the others. (A). BPPS-defined hierarchical relationships among the GTPases examined here. (B). Entamoeba histolytica Rho1 GTPase (pdb: 3refB) (Bosch et al., 2011). Color scheme: R4-specific residues forming a BPPS-SIPRIS-defined hydrogen-bond network (p=8.3 × 10−5), red sidechains; residues conserved in P-loop GTPases and interacting with bound guanine nucleotide, yellow sidechains; atoms forming hydrogen bonds, CPK coloring. Modeled hydrogen atoms were generated using the Reduce program (Word et al., 1999). (C). Rab4 bound to GTP and to the Rab-binding domain of Rabenosyn (pdb: 1z0kA [Eathiraj et al., 2005]). BPPS-SIPRIS-defined residues distinctive of R4 (red sidechains) and Rab (orange) have core and Rabenosyn-contacting predefined cluster p-values of 2.6 × 10−6 and 2.9 × 10−8, respectively. The sensor threonine (Thr40) has substantial van der Waals contact with Glu44; Thr40 is a R4-specific (red) residue outside of the SIPRIS-defined cluster. (D). Rab8a in complex with the GTP analog, GNP, and with Ocrl1 (residue 540–678) (pdb: 3qbtA) (Hou et al., 2011]). Residues distinctive of Rab GTPases (orange) and of the Rab8 subgroup (green) are enriched at the Ocr1 interface (p=5.2 × 10−7 and 6.1 × 10−6, respectively). (E). Rab8a homodimeric complex (pdb: 4lhwAB) (Guo et al., 2013). Rab-specific residues (orange) are enriched at the homodimeric interface (p=8.7 × 10−7). The following source data are available for Figure 2.

R4 GTPases function as on/off switches regulating cellular processes. GTPase activating proteins (GAPs) facilitate hydrolysis of bound GTP (the ‘on’ state) to GDP (the ‘off’ state). Guanine nucleotide exchange factors (GEFs) turn GTPases back on by stimulating replacement of GDP with GTP. SIPRIS identifies a significant network of BPPS-defined R4 residues. In Rho1 GTPases, this appears within a hydrogen-bond cluster (p=8.3 × 10−5; Figure 2B) or within a core cluster (p=7.8 × 10−7). In most Rab GTPases, this network often appears within a spherical or core cluster (e.g., Figure 2C) and, rarely, within a hydrogen-bond cluster (e.g. Rab9, pdb:1s8f [Wittmann and Rudolph, 2004]; p=9.0 × 10−4). We postulate that a significant hydrogen-bond network forms only in certain conformations. These R4 sequence/structural configurations correspond to features identified through previous analyses, including: (i) Several aromatic-CH-π interactions proposed to stabilize β-strands (Merkel and Regan, 1998) associated with the P-loop and with the guanine binding loop, and to facilitate guanine nucleotide exchange (Neuwald, 2009a) (Phe99-Gly131 and Trp114-Gly27 in Figure 2B). (ii) A salt bridge also associated with the guanine-binding loop (Arg137-Glu163 in Figure 2B). (iii) Residues forming a switch II ‘charge dipole pocket’ proposed to facilitate conformational changes associated with the switching mechanism (Neuwald, 2009b). And (iv) glutamine and glutamate residues proposed to function in GTP hydrolysis (Vetter and Wittinghofer, 2001) and nucleotide exchange (Gasper et al., 2008), respectively. We propose that, together, these residues, which adjoin the GTP-binding site from the guanine-binding loop to the γ-phosphate interacting switch II region, constitute in large part the R4 switching mechanism.

SIPRIS identifies a network of residues distinctive of the Rab subfamily of R4 GTPases within a spherical cluster in the switch I and II regions (p=4.8 × 10−10 for Rab4). Rab subfamily residues also intersect with those residues contacting Rab-binding domains, with high significance based on predefined clustering: for Rab4-Rabenosyn-5 (Figure 2C) (Eathiraj et al., 2005) and Rab8a-Ocr1 (Hou et al., 2011) (Figure 2D) p=2.9 × 10−8 and 5.2 × 10−7, respectively. This occurs despite the Rabenosyn and Ocrl1 domains being structurally distinct. Rab subfamily residues are similarly enriched at the Rab8a homodimeric interface (p=8.7 × 10−7) (Figure 2E) (Guo et al., 2013), supporting the notion that these residues can interact with diverse structural folds. For the Rab4 structure in Figure 2C, Thr40, another R4-specific residue, albeit one outside of the SIPRIS-defined cluster, corresponds to the switch I residue that senses the γ-phosphate of GTP. This residue establishes its greatest contact area (45 Å2) with Glu44, one of the Rab-specific residues contacting Rabenosyn-5; thus Thr40 and Glu44 may link sensing of the γ-phosphate to substrate binding. For Rab8a both Rab- and Rab8-specific residues appear to mediate binding to the Ocr1 domain (Figure 2D); in all, 19 of the 23 Rab8-Ocrl1 interface residues are distinctive of either the Rab subfamily or the Rab8 sub-subfamily. Many of the Rab8-residues interact with an N-terminal helix extending out of the Ocrl1 β-sandwich domain, perhaps thereby compensating for the lack of binding specificity of Rab-subfamily residues.

BPPS grouped translation factor (TF) GTPases into a single family (Figure 2A), which includes initiation factors (e.g. IF2 and eIF5B), sulfate adenyltransferases (CysN), ribosome-releasing factor 2, peptide chain release factor 3, elongation factors EF-Tu, EF1α and selenocysteine-specific elongation factor, EF4, aEF2, and EF-G (Leipe et al., 2002). Within Thermus aquaticus EF-Tu complexed with a GTP analog, Phe-tRNA, and the antibiotic Enacyloxin IIA (Parmeggiani et al., 2006), TF-specific residues (Figure 3A) spherically cluster around the switch I and II and P-loop regions (p=1.4 × 10−7); this differs from the R4-residue arrangement in Figure 2B. The two 5’-terminal tRNA nucleotide bases, which base-pair with the 3’ strand to which the aminoacyl group is attached, establish the greatest contact with the EF-Tu GTPase domain among all the bases of the tRNA. TF-specific residues cluster around these 5’ bases (p=1.3 × 10−5 and 2.6 × 10−6, respectively) and link the 5’ region of aa-tRNA to the GTP γ-phosphate; this cluster includes Thr62, which senses γ-phosphate. We hypothesize that, upon correct tRNA-anticodon pairing with its mRNA codon, these TF residues assist in coupling GTP hydrolysis to coordinated conformational changes that dissociate EF-Tu from the ribosome and from tRNA, which can then fully enter the ribosomal A site.

![Figure 3.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig3-v1.jpg)

**Figure 3.:** (A). Thermus aquaticus EF-Tu complexed with the antibiotic enacyloxin IIA, a GTP analog, and Phe-tRNA (pdb: 1ob5) (Parmeggiani et al., 2006). Color scheme: BPPS-SIPRIS defined GTPase-, TF- and EF-Tu/CysN-specific residues, yellow, red, and orange sidechains, respectively; GTPase domain backbone, green; C-terminal β-barrel domains, gray; phe-tRNA, teal; 5’ end nucleotide bases, light cyan; guanine nucleotide, cyan; enacyloxin IIA, greenish-cyan. Spheres indicate glycine Cα atoms. (B). BPPS-SIPRIS cluster of EF-Tu TF-residues centered on EF-Ts Phe81 at the EF-Tu/EF Ts interface (pdb: 1efu) (Kawashima et al., 1996). Regions in EF-Ts conserved between E. coli and cow are shown in cyan both in the figure and in the corresponding alignment below it. (C). P. aeruginosa EF-Tu bound to the Tse6 toxin domain (pdb: 4zv4) (Whitney et al., 2015). EF-Tu His20, which corresponds to His19 in (B), appears to form a salt bridge with Glu291 of Tse6. In light pink are regions of Tse6 contacting EF-Tu. Spherically clustered residues (p=0.0060) centered on Glu291 of Tse6 are shown with red sidechains. (D). Spherically clustered EF-Tu/CysN residues (orange; p=6.3 × 10−5) within the CysND complex (pdb: 1zun) (Mougous et al., 2006). (E). Spherically clustered EF-Tu/CysN-residues in EF-Tu (pdb: 1ob5) (p=1.0 × 10−6). (F). Human eIF4AIII bound to RNA, ADP, and the γ-phosphate transition state mimic AlF3 (pdb: 3e × 7) (Nielsen et al., 2009). Color scheme: eIF4AIII N- and C-terminal domains, violet and green, respectively; RNA and ADP, cyan; AlF3, light cyan; superfamily-conserved catalytic residues, yellow sidechains; RNA helicase-specific residues clustered on (light cyan-colored) RNA bases 4–5, red; other RNA helicase-specific residues, light red; C-terminal catalytic residues, bright green. The following source data are available for Figure 3.

TF-specific residues also may be important for guanine nucleotide exchange mediated by EF-Ts. Within the structure of EF-Tu bound to EF-Ts (pdb: 1efu) (Kawashima et al., 1996), 14 TF-residues form a (spherical) cluster (p=5.2 × 10−5; Figure 3B) centered on Phe81 of EF-Ts, the residue with the greatest area of contact with EF-Tu. These TF-residues, which include His19, His84, and Gln114 of EF-Tu, adjoin two regions of EF-Ts contacting EF-Tu and are conserved across bacteria and eukaryotes (Figure 3B). His19, which is located in the P-loop of EF-Tu, is the residue that is most characteristic of these translation factors. Both His19 and Gln114 have been implicated in nucleotide exchange (Zhang et al., 1998), and in destabilization of Mg+2 coordination (leading to guanine nucleotide release) upon intrusion of EF-Ts Phe81 near His84 of EF-Tu (Schümmer et al., 2007). Given recent evidence for an EF-Tu/Ts·GTP·aa-tRNA quaternary complex (Burnett et al., 2014), we conjecture that TF-residues may help couple GTP-hydrolysis-mediated loading of aa-tRNA onto the ribosome with nucleotide exchange by EF-Ts. P. aeruginosa Tse6 toxin (Whitney et al., 2015) appears to have hijacked this TF interaction interface with EF-Ts (Figure 3C).

BPPS partitions EF-Tu and CysN into a common subfamily within the TF family, consistent with earlier analysis supporting their specific relationship (Leipe et al., 2002; Inagaki et al., 2002). CysN, together with the catalytic CysD subunit, form a sulfate adenylyltransferase complex involved in sulfur assimilation. The CysND-catalyzed reaction is analogous to the first step in charging a tRNA, and CysN’s contact sites with CysD are similar to, and include residues homologous to, EF-Tu’s contact sites with aa-tRNA. Within the CysND complex (pdb: 1zun) (Mougous et al., 2006) EF-Tu/CysN-residues cluster around the switch I and II regions (p=6.3 × 10−5; Figure 3D). In CysN, these residues adjoin contact regions with CysD and with the CysN C-terminal linker and β-barrel domains. Analogously in EF-Tu, they are proximal to the contact region with aa-tRNA and the EF-Tu C-terminal linker and β-barrel domains (Figure 3E). Within EF-Tu these residues are also located between the bound antibiotic enacyloxin IIA and the GTPase- and TF-specific residues (Figure 3A). Because enacyloxin IIA hinders the release of EF-Tu-GDP from the ribosome (Parmeggiani et al., 2006), we hypothesize that these residues may help mediate this process.

### Comparison of two P-loop NTPase superfamilies: eIF4AIII RNA helicase

For comparison, we analyzed another nucleic-acid-associated P-loop NTPase, the Superfamily II RNA helicase eIF4AIII, which is a component of the exon junction complex (EJC). The EJC deposits onto spliced mRNAs and plays an important role in mRNA transport, translation, and quality control. RNA helicases are part of a huge group of NTPases that undergo ATP-hydrolysis-coupled conformational changes to unwind double-stranded nucleic acids, translocate nucleic acids or re-distribute protein complexes on nucleic acids (Anantharaman et al., 2002; Bourgeois et al., 2016; Lohman et al., 2008; Northall et al., 2016). For the transition state structure of eIF4AIII bound to RNA, a predefined cluster of RNA helicase-specific residues contacting RNA is highly significant (p=6.4 × 10−6; Figure 3F). Focal point spherical clustering indicates that these residues are centered on RNA bases 4 and 5 (p=5.1 × 10−7 and p=5.5 × 10−4, respectively), which establish the greatest contact with the ATPase domain. These observations and a rotated bond between bases 4 and 5 suggest that these residues help couple ATP hydrolysis to disruption of duplex RNA. Clusters centered on other bases are not significant (p>0.9). Most of the remaining RNA helicase-specific residues surround key active site residues or interact with C-terminal domain catalytic residues, including two arginine fingers (Figure 3F). Given this configuration, ATP hydrolysis seems likely to shift the relative orientations of the N- and C-terminal domains, both of which interact with RNA.

### Residue networks adapting the EEP catalytic core to diverse substrates

EEP enzymes cleave phosphodiester bonds in substrates that include nucleic acids and phospholipids. To identify residues likely responsible for EEP functional divergence, we applied BPPS-SIPRIS to APE1, an exonuclease III-like apurinic/apyrimidinic endonuclease (exoIII-AP-endo), and several inositol polyphosphate 5-phosphatases (INPP5) (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig4-v1.jpg)

**Figure 4.:** (A). The two major groups of the BPPS-defined EEP hierarchy examined here. (B). Human APE1 phosphorothioate substrate complex (pdb: 5dfi) (Freudenthal et al., 2015). Replacement of the phosphodiester bond with phosphorothioate prohibits cleavage by APE1 at the abasic site (circled). Cys310, which is nitrosated, is indicated. Color scheme: APE1 backbone trace, green; DNA strand containing the abasic site, cyan; complementary strand, marine blue; the BPPS-SIPRIS-defined residues distinctive of the EEP superfamily and of the exoIII-AP-endo family, yellow and red sidechains, respectively; basic residues within a loop interacting with the major groove of DNA, purple. (C). Close up of the APE1 active site. EEP-specific residues forming a hydrogen-bond network are shown with yellow sidechains. For clarity, only a few of the EEP- and exoIII-AP-endo-specific residues in the network are shown. The following source data are available for Figure 4.

APE1 participates in the DNA excision repair pathway by incising the apurinic/apyrimidinic (AP) site phosphodiester backbone; this generates a single nucleotide DNA gap with 3’-hydroxyl and 5’-deoxyribose phosphate termini—a cytotoxic intermediate substrate that is then processed by DNA polymerase β (Liu et al., 2007). A proposed mechanism for APE1 (Mol et al., 2000) involves superfamily-conserved active site residues forming hydrogen bonds with the oxygen atoms of the phosphate group at the abasic site. Consistent with this, SIPRIS identifies a superfamily-conserved hydrogen-bond network centered on the abasic site (p=5.2 × 10−6) within a structure of APE1 bound to DNA harboring an abasic site phosphate group analog (phosphorothioate) in one strand (Figure 4B,C). Centering on adjacent bases in the same strand was less significant (p>0.003). For exoIII-AP-endo-conserved residues SIPRIS identifies a significant hydrogen-bond network centered on the abasic site (p=1.6 × 10−6) or on adjacent bases 8–9 and 12–13 (p=1.9 × 10−7 to 7.6 × 10−6); these residues may contextually position catalytic residues around the abasic site. In particular, regions associated with these residues insert into the DNA major and minor grooves on either side of the abasic site, and form a kink in and engulf the target DNA strand (Figure 4B). Thus, exoIII-AP-endo residues appear to form a substrate-specific ‘reaction chamber’, as might be expected. They also tend to aggregate between the catalytic core and a loop containing basic residues that interact with the major groove of DNA (Figure 4B). Modification by nitric oxide (nitrosation) of one of these residues, Cys310, results in dissociation of APE1 from DNA and relocation to the cytoplasm (Qu et al., 2007); thus, the associated hydrogen-bond network may communicate the nitrosation signal to the DNA-binding site.

BPPS-SIPRIS-defined INPP5-residues also form a significant hydrogen bond network (p=1.1 × 10−7) adjacent to the superfamily-conserved cluster (Figure 5A,B). We hypothesize that this network recognizes inositol polyphosphates harboring phosphate groups at positions 4 and 5 of the inositol ring. INPP5 phosphatases cleave the 5-phosphate, but require for recognition the 4-phosphate, which directly interacts with three network-associated basic residues—perhaps thereby mediating substrate recognition (Figure 5C). In some structures, the INPP5 network residues most remote from the catalytic core are part of a cleft accommodating a phosphate or a glycerol (Figure 5D,E), suggesting that these may form another (unknown) membrane interaction site or an allosteric site that binds a molecule similar to the known substrate.

![Figure 5.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig5-v1.jpg)

**Figure 5.:** Color code: EEP-residues, yellow sidechains; INPP5 residues, red sidechains; INPP5B-, INPP5E- and SHIP2-subfamily residues, orange sidechains; ligands, cyan; atoms involved in hydrogen bonds, CPK coloring. (A). Human INPP5B in complex with phosphatidylinositol 3,4-bisphosphate (pdb: 4cml) (Trésaugues et al., 2014), which is associated with cytosolic and mitochondrial membranes (Speed et al., 1995). BPPS-SIPRIS results: EEP spherical cluster, p=5.8 × 10−13; INPP5 spherical cluster, p=3.9 × 10−7; INPP5B spherical cluster, p=0.0021. (B). INPP5 hydrogen bond network within human INPP5B (pdb: 3mtc) (unpublished). (C). View of INPP5-residues (in 3mtc) that bind the 4-phosphate group required for substrate recognition. (D). Human INPP5B with phosphate bound to a possible membrane interaction or allosteric site (Mills et al., 2016). (E). Human INPP5B Ocrl with glycerol bound to the same site as indicated in (D) (Trésaugues et al., 2014). (F). INPP5 subgroups within the BPPS-defined hierarchy. (G). Human INPP5E (pdb: 2xsw) (unpublished), which is associated with the primary cilium, an organelle involved in signal transduction (Jacoby et al., 2009) (spherical cluster, p=3.6 × 10−4). (H). Human SHIP2 (pdb: 4a9c) (Mills et al., 2012), which is associated with membrane ruffle formation (Hasegawa et al., 2011) (spherical cluster, p=0.30). The following source data are available for Figure 5.

INPP5 proteins regulate diverse cellular processes, including postsynaptic vesicular trafficking, insulin signaling, cell growth and survival, and endocytosis. With this in mind, we examined three INPP5 subfamilies: INPP5B, INPP5E and SHIP2 (Figure 5F). Residues that most distinguish the INPP5B subfamily form a cluster between the proposed membrane interacting region (Trésaugues et al., 2014) and the EEP catalytic core (Figure 5A). INPP5E- and SHIP2-specific residues also cluster in this same region (Figure 5G,H)—although the SHIP2 cluster is not statistically significant. This suggests a possible role for these residues in sequestering specific membrane-associated phosphoinositide substrates from the lipid bilayer.

### Family-specific catalysis: thymine DNA glycosylases

Uracil DNA glycosylases (UDGs) remove uracil from DNA, thereby initiating the DNA base excision repair pathway (Aravind and Koonin, 2000). Uracil may be incorporated into DNA by DNA polymerase or by cytosine deamination. Thymine DNA glycosylases (TDGs) initiate base excision repair by removing T from G·T mispairs, which can be due to deamination of 5-methylcytosine. These enzymes also remove oxidized derivatives of methyl cytosine such as 5-formyl and 5-carboxymethyl cytosine, which are epigenetic marks or intermediates in the reset of 5mC marks by the TET enzymes (Pastor et al., 2013). Within the structure for human TDG (Pidugu et al., 2016) BPPS-SIPRIS identifies a significant hydrogen-bond network associated with TDG-family residues (Figure 6A,B); also in this network are residues classified by BPPS to a metazoan TDG subfamily. Like APE1, network residues appear to position loops containing basic residues that, in this case, interact with both the major and minor grooves of bound DNA (Figure 6C). Network residues also form hydrogen bonds to DNA oxygen atoms on either side of the thymine base being excised—suggesting that they may help position the substrate for catalysis by sensing particular sequence contexts (Figure 6B). Near the center of this network and in contact with the targeted thymine base is the residue most distinctive of metazoan TDGs, Asn230 (Figure 6B and Figure 6—source data 1); in other TDG subfamilies, a hydrophobic residue occurs at this position. Other TDG-residues in this network encase a water molecule believed to function as a nucleophile in catalysis (Pidugu et al., 2016) (Figure 6D). Hence, for TDG, family-specific residues may play a critical catalytic role. UDG harbors a hydrogen bond network distinct from that of TDG (Figure 6E), indicating a mechanistic divergence.

![Figure 6.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig6-v1.jpg)

**Figure 6.:** (A). Thymine DNA glycosylase (TDG) family (red sidechains) and metazoan subfamily (orange sidechains) residues forming a significant hydrogen bond network (p=3.5 × 10−5) within human TDG (pdb: 5hf7) (Pidugu et al., 2016). (B). TDG H-bond network consisting of residues distinctive both of all TDGs (red sidechains) and of metazoan TDGs (orange sidechains). This network includes hydrogen bonds to DNA oxygen atoms on either side of the thymine base to be excised (cyan); note that Phe238 and Tyr235 appear to position the N-terminus of their helix to hydrogen bond to substrate backbone oxygens; another such hydrogen bond involves Ser273, a residue generally conserved in the entire superfamily. The water molecule shown may act as the nucleophile in the reaction. For clarity, not all of the BPPS-SIPRIS-defined residues are shown. (C). TDG hydrogen-bond network residues may help position basic residues (green sidechains) interacting with the minor and major grooves of DNA. (D). TDG family-specific hydrogen-bond network residues surrounding a proposed catalytic water molecule (red sphere with dot cloud). (E). A BPPS-SIPRIS-defined H-bond network (p=1.7 × 10−5) distinct from that of TDG within Thermus thermophilus uracil DNA glycosylase (UDG) (pdb: 2dp6). The following source data are available for Figure 6.

### Applying SIPRIS with other methods

Applying SIPRIS in conjunction with various protein function determining residue (FDR) methods (Casari et al., 1995; Ye et al., 2008; Pirovano et al., 2006; Kalinina et al., 2004; Hannenhalli and Russell, 2000; Livingstone and Barton, 1996; Mihalek et al., 2004; Mirny and Gelfand, 2002; Lichtarge et al., 1996; Sankararaman and Sjölander, 2008; Fischer et al., 2008; Kalinina et al., 2009; Janda et al., 2012; Janda et al., 2014; Marttinen et al., 2006; Kolesov and Mirny, 2009; Wilkins et al., 2012; Chakraborty and Chakrabarti, 2015; Gaucher et al., 2002; Xin and Radivojac, 2011; Capra and Singh, 2008) is straightforward in principle. However, several factors complicate comparisons to BPPS-SIPRIS. First, a fair number of published FDR methods are no longer available as source code, executables or over the world wide web (e.g. INTREPID [Sankararaman and Sjölander, 2008] and MINER [La and Livesay, 2005]). Second, many FDR methods (e.g. GroupSim [Capra and Singh, 2008]) require user-provided input, such as an MSA, a phylogenetic tree, or prespecified categories with corresponding sequence assignments for each category. This confounds the comparison because the contribution of each user-provided component to overall performance is unclear. In contrast, BPPS-SIPRIS requires no input beyond the query and database sequences, and its algorithmic components are statistically coherent. Third, those FDR methods not requiring user-generated input typically are based on a phylogenetic tree; this renders infeasible their application to large sequence sets, which is a key aspect of SIPRIS’s ability to detect biologically relevant features. Our attempts to input even moderately large sequence sets to various FDR programs resulted in runtime errors. By focusing on a hierarchy of subgroups, each defined by a correlated residue pattern, BPPS eliminates the need for a phylogenetic tree, which would introduce more complexity than either is necessary or can be reliably inferred.

Finally, BPPS-SIPRIS aims to identify biologically relevant interaction networks whose functions are not necessarily known, whereas FDR methods generally try to identify residues responsible for well-characterized functions—such as catalysis or substrate recognition—that can be experimentally benchmarked (Chakrabarti and Panchenko, 2009). However, as has been noted (Dessimoz et al., 2013; Jiang et al., 2014), we lack reliable gold standards for many functionally relevant residues, due to a lack of experimental characterization. Consequently, methods designed to identify residues with specific, known functions, if successful, will tend to penalize residues involved in unknown functions. In contract, the goal of BPPS-SIPRIS is to recognize also such residues of unknown function.

With this in mind, we compared the BPPS-SIPRIS analyses in this study to SIPRIS analyses based on the FRpred (Fischer et al., 2008), CLIPS-1D (Janda et al., 2012), and Evolutionary Trace (ET) (Lichtarge et al., 1996; Wilkins et al., 2012) programs, which define residue sets given only a query sequence. These and similar methods differ from BPPS by not classifying sequences into divergent subgroups per se. Instead, FRpred seeks to classify residues as catalytic, ligand binding and subtype-specific. FRpred catalytic and ligand-binding residues generally correspond to superfamily-conserved residues, whereas FRpred subtype-specific residues fail to correspond to any BPPS subgroups. For example, when we ran the Rab4 analysis as in Figure 2C using FRpred-defined residue sets instead of BPPS-defined sets, the first two FRpred categories nearly entirely overlapped with each other and with the Rab4 structural core; the subtype-specific category failed to return a significant cluster (p>0.05). SIPRIS analyses of other protein domains yielded similar results. CLIPS-1D defines catalytic, ligand-binding and structural categories, which likewise fail to correspond to BPPS subgroups. ET assigns residue functional importance scores without splitting into categories, and thus fails to differentiate between BPPS subgroups. As previously noted (Madabushi et al., 2002), high ET-scoring residues are often clustered structurally, which SIPRIS analyses confirm. Due to methodological differences, however, BPPS-SIPRIS clustering identifies sequence/structural features distinct from these other methods, as illustrated in Figure 1—source data 1. Although other methods may identify biologically relevant residues different than those identified here, this study suggests that by characterizing divergent subgroups, BPPS-SIPRIS analyses can identify significant, otherwise overlooked sequence/structural properties.

## Discussion

Active site residues directly involved in catalysis are believed often to communicate with a network of other functionally important residues, some of which may be far from the active site (Sunden et al., 2015). The problem of identifying these networks is fundamental for understanding how proteins work. As illustrated here, BPPS-SIPRIS analyses can reveal information relevant to functional specialization by identifying statistically significant interaction networks. This includes, for example: (1) The nitrosation associated network in APE1 of the synaptojanin (EEP) superfamily. (2) The protein-protein interaction interfaces for diverse R4 GTPases. (3) The protein-protein interaction interface in EF-Tu, which can be hijacked by the P. aeruginosa Tse6 toxin (Whitney et al., 2015). In each of these cases, the residue-networks identified by our analysis suggest features congruent with current biochemical understanding of these proteins. Additionally, our analyses generated the following hypotheses: (1) Family-specific residues form hydrogen bonds (Figure 4C) responsible for APE1 abasic site substrate specificity. (2) INPP5 family and sub-family specific residues (Figure 5E–F) mediate, respectively, allosteric regulation and sequestration of specific membrane-associated phosphoinositide substrates from the lipid bilayer. (3) A hydrogen bond network associated with the residue most distinctive of metazoan TDGs, Asn230 in humans, mediates substrate-specific catalysis in DNA glycosylases, perhaps related to the discrimination of epigenetic marks present in metazoan DNA (Pastor et al., 2013; Zhang et al., 2012), such as 5-fC and 5-caC.

More generally our analyses suggest: (1) Family-specific residues often form a substrate-specific ‘reaction chamber’ associated with the structural core and active site, as seen for Gna1-related acetyltransferases, phosphoesterases related to APE1, and DNA glycosylases. (2) Subfamily-specific residues serve subordinate roles, such as mediating interactions with effector proteins, or coupling conformational changes to signaling. In this way, the same basic structural core and catalytic mechanism may accommodate a wide variety of cellular functions.

The SIPRIS clustering strategies described here accommodate further development. For example, one might use consensus distances from multiple structures to reduce noise. An open question is the significance of multiple BPPS-SIPRIS networks for a single subgroup, analogous to that for multiple regions of similarity between two sequences (Karlin and Altschul, 1993). Additional strategies include: applying BPPS-SIPRIS to functionally interacting proteins, treating them as a single sequence; and defining clusters using features such as secondary structure, surface accessibility or electrostatic potential. BPPS identifies correlated residue patterns presumably associated with functional specialization, and SIPRIS identifies correlations between defined residue sets and structural features. In contrast, DCA identifies correlations between pairs of residues that presumably interact structurally. Combining BPPS-SIPRIS with DCA may improve protein modeling and the characterization of functional interactions. Given the statistical and information theoretic foundation of these methods, one should be able to combine them in a principled manner.

In summary, the BPPS-SIPRIS system should aid the characterization of functionally interacting residues remote from protein active sites.

## Materials and methods

### BPPS-SIPRIS overview

BPPS-SIPRIS analysis involves the following steps, as illustrated in Figure 7: (1) MAPGAPS (Neuwald, 2009) detects and aligns protein database sequences containing the domain of interest starting from a representative (‘seed’) MSA or from an hiMSA, either of which may be either curated manually or created automatically. This generates an MSA. (2) Bayesian Partitioning with Pattern Selection (BPPS) (Neuwald, 2014a; Neuwald, 2014b; Neuwald and Altschul, 2016a) is applied in three steps: (i) Step 1 uses Markov chain Monte Carlo (MCMC) sampling to partition the MSA into hierarchically-arranged subgroups based on the correlated residue patterns most distinctive of each subgroup. (ii) Step 2 converts the MSA into a hiMSA based on the BPPS hierarchy. (iii) Step 3 creates subgroup ‘contrast alignments’ and corresponding SIPRIS input files. (3) The SIPRIS program performs pattern residue cluster analyses and, as a runtime option, will create corresponding PyMOL (Schrodinger, 2010) scripts for viewing clusters within 3D structures (as in Figures 1–6). Each step in this process applies statistical criteria to ensure significance (see below).

![Figure 7.](https://cdn.elifesciences.org/articles/29880/elife-29880-fig7-v1.jpg)

**Figure 7.:** (A) Steps required for a BPPS-SIPRIS analysis. The fatax program adds phylum-annotations to database sequences. MAPGAPS detects and aligns database sequences containing the domain defined by a cma-formatted MSA or hiMSA. (MAPGAPS can also convert an MSA from fasta- to cma-format.) This creates an MSA that step 1 of BPPS then partitions hierarchically into subgroups based on discriminating pattern residues, as illustrated schematically in (B). Step E of BPPS checks for consistency between BPPS step 1 runs. Step 2 of BPPS adjusts the sub-alignment for each subgroup to align and possibly assign pattern residues to regions uniquely conserved in that subgroup, thereby creating a hiMSA. Step 3 of BPPS creates, for each node in the hiMSA, lineage-specific ‘contrast alignments’, as is illustrated schematically in (C), and a corresponding input file to SIPRIS, which identifies statistically significant structural interaction networks associated with pattern residues. For further descriptions, see text. (B) Schematic diagram of the node eight contrast alignment. Sequences assigned to node 8's subtree (green subfamily nodes in (C)) constitute a ‘foreground’ partition; sequences assigned to the other nodes of the subtree rooted at the parent of node 8 (gray subfamily nodes in (C)) constitute a ‘background’ partition, and the remaining sequences constitute a non-participating partition. Green horizontal bars in (B) represent foreground sequences. The green vertical bars in (B) represent conserved foreground residue patterns (as shown below each bar); these diverge from (or contrast with) the background compositions at those positions (white vertical bars). Red vertical bars above quantify the degree of divergence. (C) Schematic diagram of a BPPS-3-generated set of ‘contrast alignments’ corresponding to the node 9 lineage of the sequence hierarchy in (A). Within a hiMSA, there is one such lineage for each leaf node. Horizontal lines represent aligned sequences and are colored by level in the hierarchy. Thin light gray horizontal lines represent non-homologous and deleted regions. Vertical lines represent the contrasting pattern positions upon which the hierarchy is based and are similarly colored by levels. The trees shown correspond to each subgroup along the lineage. The colored, gray and white nodes in each tree correspond, respectively, to their alignment foreground, background and non-participating partitions. The background for the entire superfamily (lower right) consists of standard amino acid frequencies at each position.

### Software and data availability

BPPS-SIPRIS software, source code, instructions, and the input data required to perform the analyses described here are available at sipris.igs.umaryland.edu; this includes: (1) the MAPGAPS, BPPS, and SIPRIS programs; (2) MSA format conversion programs; (3) a phylum annotation program (fatax); and (4) the full multiple sequence alignments and pdb structural coordinate files used as input to BPPS and SIPRIS. The source code is available at sourceforge (sourceforge.net/p/bpps-sipris/code/; Neuwald, 2017). A copy is archived at https://github.com/elifesciences-publications/bpps-sipris-code.. The fatax program annotates sequences by phylum and kingdom based on the National Center for Biotechnology Information (NCBI) taxdump and prot.accession2taxid files, available at ftp://ftp.ncbi.nlm.nih.gov/. MAPGAPS searches were performed on the NCBI nr, env_nr and translated est databases (April 8, 2016 releases). Modeled hydrogen atoms were added to structural coordinate files using the Reduce program (Word et al., 1999) (http://kinemage.biochem.duke.edu/software/reduce.php).

### MAPGAPS search and alignment

MAPGAPS (Neuwald, 2009) creates an MSA by: (1) Taking as input either a small but ideally very accurate MSA, each sequence of which represents a distinct subgroup within a protein superfamily, or, alternatively, a set of hierarchically aligned MSAs, each of which represents a distinct subgroup. For the analyses here, we obtained from the NCBI conserved domain database (CDD) a set of hierarchically aligned MSAs or, if unavailable, a single curated MSA. A hiMSA from a previous BPPS analysis may also be used. (2) Creating a hidden Markov model (HMM) profile for each subgroup based on the input MSA. (3) Searching a protein sequence database and aligning each significantly scoring sequence (i.e. with p≤0.001) to the profile yielding the highest score. (4) Multiply aligning all the sequences obtained in this way using an alignment among profiles as a template (Neuwald, 2009). This process creates a large MSA that generally preserves the accuracy of the input alignment; BPPS uses this MSA as input. Table 2 describes the structural diversity of proteins with known structure identified in this way and included in our analysis. For a superfamily of domains near the limit of current sequence analysis methods’ ability to identify as related, we find that an average RMSD of 3.75 Å is typical. The RMSDs for the GNAT, EEP and UDG/TDG superfamilies fall below this value. Those for the GTPases are slightly higher, which can easily be explained by the conformational variability arising from GTPases’ function as switches. The helicases yield unusually high RMSDs, which are likely due to the large domain-domain movements typical of this clade.

**Table 2.**
 Structural diversity among proteins identified and aligned by MAPGAPS.


<table>
  <thead>
    <tr>
      <th>Superfamily</th>
      <th colspan="2">structures*</th>
      <th colspan="4">RMSD† (Å)</th>
      <th colspan="3">Domain length‡</th>
      <th colspan="2">Resolution (Å)</th>
    </tr>
    <tr>
      <th></th>
      <th>% ID</th>
      <th>No.</th>
      <th>Avg</th>
      <th>Min</th>
      <th>Max</th>
      <th>S.D.</th>
      <th>MSA</th>
      <th>Avg</th>
      <th>S.D.</th>
      <th>Avg</th>
      <th>Max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GNAT</td>
      <td>27</td>
      <td>16</td>
      <td>3.25</td>
      <td>1.0</td>
      <td>6.7</td>
      <td>1.4</td>
      <td>125</td>
      <td>139.8</td>
      <td>17.0</td>
      <td>1.94</td>
      <td>2.61</td>
    </tr>
    <tr>
      <td>GTPases</td>
      <td>30</td>
      <td>20</td>
      <td>3.96</td>
      <td>0.6</td>
      <td>14.7</td>
      <td>3.5</td>
      <td>164</td>
      <td>195.9</td>
      <td>41.6</td>
      <td>2.31</td>
      <td>3.10</td>
    </tr>
    <tr>
      <td>Helicases</td>
      <td>40</td>
      <td>12</td>
      <td>6.39</td>
      <td>2.6</td>
      <td>9.8</td>
      <td>1.8</td>
      <td>466</td>
      <td>482.8</td>
      <td>60.7</td>
      <td>2.86</td>
      <td>3.56</td>
    </tr>
    <tr>
      <td>EEP</td>
      <td>40</td>
      <td>16</td>
      <td>3.02</td>
      <td>0.8</td>
      <td>5.2</td>
      <td>0.95</td>
      <td>241</td>
      <td>259.0</td>
      <td>27.6</td>
      <td>2.07</td>
      <td>2.99</td>
    </tr>
    <tr>
      <td>UDG/TDG</td>
      <td>40</td>
      <td>8</td>
      <td>2.54</td>
      <td>1.1</td>
      <td>3.6</td>
      <td>0.69</td>
      <td>125</td>
      <td>135.9</td>
      <td>12.7</td>
      <td>1.83</td>
      <td>2.58</td>
    </tr>
  </tbody>
</table>

_*NMR and poor resolution structures were not used; no two proteins in each set contained more than the indicated level of percent sequence identity (% ID); pdb identifies for these are given in supplementary file 1.†RMSDs were computed using MUSTANG (Konagurthu et al., 2006) with default parameters; the structural coordinates used for the analysis were limited to the domain of interest.‡The number of aligned columns in the MSA, and the average length and standard deviation of the domain ‘footprint’._

### MAPGAPS query alignments

Curated MSAs used for MAPGAPS searches were constructed as follows: The GNAT and GTPase MSAs were curated by L. Aravind’s and A. Neuwald’s group, respectively. The NCBI CDD resource group curated the other query MSAs; the CDD codes are: cd00046, DEAD-like helicase superfamily; cd08372, Exonuclease-Endonuclease-Phosphatase (EEP) domain superfamily; and cd09593, Uracil-DNA glycosylases (UDG) and related enzymes. Using these MSAs as MAPGAPS queries, we searched the NCBI nr, env_nr and translated EST databases for matching sequences. For ESTs, we obtained organism codon usage and taxonomic information from NCBI taxdump files.

### BPPS sampling

Step 1 of the BPPS (Neuwald, 2014a, Neuwald, 2014b) program stochastically partitions an MSA into hierarchically arranged subgroups (i.e. nodes). Starting from a single root node, it attaches or removes leaf nodes, moves subtrees, inserts or deletes internal nodes, moves sequences between nodes, and modifies the ‘discriminating’ pattern for each node. BPPS samples from among possible patterns for each subgroup based on how well each pattern distinguishes subgroup-assigned sequences (termed ‘foreground’ sequences) from sequences assigned to the rest of the parent node’s subtree (termed ‘background’ sequences); Figure 7B illustrates this schematically. An optional Step E checks for consistency between BPPS Step 1 runs. Step 2 of BPPS (Neuwald and Altschul, 2016a) uses a combination of multiple sequence alignment and BPPS MCMC sampling. The Gibbs Sampler for Multi-alignment Optimization (GISMO) (Neuwald and Altschul, 2016b) adjusts each sub-group’s alignment by adding regions conserved in the subgroup but not in the superfamily as a whole. Further BPPS sampling then adjusts subgroup sequence and pattern assignments taking into consideration these newly aligned regions. This converts the MSA into a hierarchical interrelated MSA (hiMSA) (Figure 7C). Step 3 creates, for individual nodes in the hiMSA, both a rich text formatted (rtf) contrast alignment (as shown, for example, in figure source data files) and corresponding SIPRIS input files. Table 3 summarizes results for the five superfamilies analyzed here.

**Table 3.**
 Summary of BPPS results for five superfamilies.


<table>
  <thead>
    <tr>
      <th>Superfamily</th>
      <th>Subgroup</th>
      <th># Sequences</th>
      <th>% Identity*</th>
      <th># Nodes in subtree</th>
      <th>Minimum subtree size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GNAT</td>
      <td></td>
      <td>237,359</td>
      <td>98</td>
      <td>44</td>
      <td>200</td>
    </tr>
    <tr>
      <td></td>
      <td>Gna1 family</td>
      <td>1243</td>
      <td></td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>GTPases</td>
      <td></td>
      <td>127,418</td>
      <td>95</td>
      <td>121</td>
      <td>500</td>
    </tr>
    <tr>
      <td></td>
      <td>R4 family</td>
      <td>18,901</td>
      <td></td>
      <td>26</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Rab subfamily</td>
      <td>7002</td>
      <td></td>
      <td>12</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Rab8 sub-subfamily</td>
      <td>3.312</td>
      <td></td>
      <td>7</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>TF family</td>
      <td>25,224</td>
      <td></td>
      <td>10</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>EFTu/CysN subfamily</td>
      <td>4429</td>
      <td></td>
      <td>3</td>
      <td></td>
    </tr>
    <tr>
      <td>Helicases</td>
      <td></td>
      <td>131,321</td>
      <td>98</td>
      <td>47</td>
      <td>300</td>
    </tr>
    <tr>
      <td></td>
      <td>RNA helicases</td>
      <td>36,788</td>
      <td></td>
      <td>8</td>
      <td></td>
    </tr>
    <tr>
      <td>EEP</td>
      <td></td>
      <td>45,799</td>
      <td>99</td>
      <td>166</td>
      <td>100</td>
    </tr>
    <tr>
      <td></td>
      <td>exoIII-AP-endo</td>
      <td>13,711</td>
      <td></td>
      <td>47</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>INPP5</td>
      <td>3855</td>
      <td></td>
      <td>14</td>
      <td></td>
    </tr>
    <tr>
      <td>TDG/UDG</td>
      <td></td>
      <td>23,592</td>
      <td>98</td>
      <td>47</td>
      <td>100</td>
    </tr>
    <tr>
      <td></td>
      <td>TDG</td>
      <td>1639</td>
      <td></td>
      <td>6</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>UDG</td>
      <td>376</td>
      <td></td>
      <td>1</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*The maximum % identity allowed between any two sequences in the set_

### SIPRIS

SIPRIS relies on a statistical approach termed Initial Cluster Analysis (ICA), which addresses the following questions: Consider a string of 0 s and 1 s of length L and containing D 1 s. Are some or all of the 1 s significantly clustered near the start of the sequence, and, if so, how surprising is the most significant such clustering? Elsewhere we describe and validate ICA (Altschul and Neuwald, 2017), which has a variety of biomedical applications. Here, we focus on the statistical and information theoretical bases of ICA as applied to BPPS-SIPRIS analysis.

### BPPS-defined residue sets

Step 2 of BPPS generates a hiMSA (Figure 7). For each subgroup (i.e. subtree) G within a hierarchy, BPPS defines a corresponding set of ‘discriminating’ residues that most distinguish members of that subgroup from closely related subgroups. This set is ordered from the most to the least distinguishing residues. We assume that these residues are likely responsible for functions specific to subgroup G. Although such a set typically includes residues with well-characterized functions, our focus is on residues of unknown functional relevance. When mapped to available structures, these distinguishing residues may readily suggest plausible hypotheses; in this respect, a BPPS analysis is informative by itself. However, SIPRIS can obtain deeper insight into and corroboration of a BPPS analysis by identifying significant overlap between BPPS-defined discriminating residues and structurally defined residue sets; we term the intersection of two such sets a BPPS-SIPRIS cluster. SIPRIS analysis was motivated, in part, by Karlin and Zhu’s approach (Karlin and Zhu, 1996) for identifying significant clusters of residues that share physical-chemical properties.

### BPPS-SIPRIS predefined clusters

The simplest BPPS-SIPRIS analysis is based on a specific, predefined structural cluster of n residues. This corresponds to a ball-in-urn problem, in which the BPPS-defined distinguishing residues correspond to N1 red balls, the remaining residues to N2 black balls, and the cluster to n balls drawn from the urn. The probability that at least x of the n residues are distinguishing (i.e. are ‘red’) is given by the cumulative hypergeometric distribution:

$$
P(x,n,N_{1},N_{2})=[\sumi=max(x,n−N_{2})min(n,N_{1})(N_{1}i)(N_{2}n−i)]\div(N_{1}+N_{2}n)
$$

### BPPS-SIPRIS optimized-clusters

Similar to BPPS-predefined clustering is choosing the optimal BPPS-structural cluster among various alternatives. To construct these, we start from a well-defined position in space, and sequentially add ‘structurally adjacent’ residues (variously defined, as described in Results) to generate a set of nested, structurally defined clusters. From this nested set, we select the structural cluster that optimally overlaps with the BPPS-defined residue set by applying the Minimum Description Length (MDL) principle (Grunwald, 2007), as described in the next section. Optimizing over different starting residues, or different numbers of discriminating residues, requires further p-value adjustment, for which we currently apply the overly-conservative Bonferroni correction to obtain an upper bound.

### The MDL principle

To avoid overfitting BPPS-SIPRIS statistical models to observed data, we apply the MDL principle (Grunwald, 2007), which can be understood as formalizing Occam's Razor (‘a model should not be needlessly complex’). Conceptually, this principle claims that the best among a set of alternative models is that which minimizes the description length of the model, plus the maximum-likelihood description length of the data given the model. This approach accounts for the implicit number of independent tests performed when optimizing the parameters of a model, and strikes a balance between a model's complexity and its ability to fit the data—in our case to describe biologically relevant amino acid residue patterns. More formally, a theory is a probability distribution over all possible sets of data, and a model is a parameterized set of theories. The description length of the data D given a model M, is then defined by DL(D|M) ≡ -log P(D|T), where T is maximum-likelihood theory contained in M (i.e. the theory which yields the greatest probability for D). The description length of the model M is defined by DL(M) ≡ log(N), where N is the number of the effectively distinct theories (i.e. parameter settings) M accommodates (Grunwald, 2007). The MDL principle aims to minimize DL(D|M)+DL(M).

### MDL applied to BPPS-SIPRIS clustering

BPPS-optimized clustering presents several mathematical challenges. Computing valid p-values requires adjusting for the multiple tests implicit in optimizing over starting residues and clusters. Also, this optimization itself may carry an implicit bias favoring small or large clusters, as outlined below.

We start with a null model in which discriminating residues (e.g. defined by BPPS) are distributed randomly throughout an entire sequence. Given a fixed number of discriminating residues, this model yields a uniform likelihood for all sets of data, and serves as a basis of comparison for likelihoods generated by an alternative model. This model divides the sequence into an initial segment of length x (which we refer to as a cluster) having m discriminating residues, and a terminal segment of length y having n discriminating residues. The model assumes discriminating residues are generated with different probabilities in the initial and terminal segments, and its maximum-likelihood theory assigns the likelihood $p=(m/x)^{m}((x−m)/x)^{x−m}(n/y)^{n}((y−n)/y)^{y−n}$ to the data. For a particular cut-point x, this likelihood requires choosing the discriminating-residue probabilities m/x and n/y for the initial and terminal segments, and is easily normalized for the selection of these parameters. Our aim, however, is to pick the x (i.e. cluster) that yields the greatest likelihood for the data. Applying the MDL principle requires calculating the effective number of independent tests N implicit in choosing x (Altschul and Neuwald, 2017). By treating x as a continuous as opposed to a discrete parameter, we are able to calculate its Fisher information (Altschul and Neuwald, 2017), and thus N.

One subtlety is that simply choosing the cut point x yielding the greatest likelihood implicitly favors low or high values of x. This occurs because the Fisher information is greater at extreme values of x, implying that the likelihoods are more independent of one another at those values. Empirical analyses show that this bias toward large and small clusters often yields suboptimal results from a biological perspective. However, by adding an x-dependent correction, derived from the Fisher information, to our optimization, we may flatten the implicit prior associated with x (Altschul and Neuwald, 2017). Random simulation shows that analytic p-values computed using our approach fall within about 20% of empirical p-values. We still need to adjust these p-values for clusters found using different starting residues. Absent a better approach, we currently apply the simple but overly conservative Bonferroni correction (Bonferroni, 1936).

### Runtimes

The runtime bottleneck in an analysis is BPPS. BPPS runtimes depend on the desired depth of the hierarchy, on the width of and the number of sequences in the input MSA and on the minimum number of sequences required to define a leaf node. For example, on a 64-bit Linux workstation, a 125,000-sequence GTPase MSA requires about 4 weeks to generate a 120 node hierarchy up to eight nodes deep and with a minimum leaf node size of 500 sequences. Note that much of this time is spent marginally refining a hierarchy. This approach is not recommended. Instead, we suggest running an initial analysis at a depth of 1 and then using the BPPS ‘focus’ option with a maximum depth of 2–4 to expand the subtree for a specific major node of interest. For the GTPase MSA, this approach takes less than a few days.

### MSA cma format

The programs used here require cma-formatted MSAs. The cma (collinear multiple alignment) format, which is unique to our programs, allows the specification of a hierarchically-arranged set of MSAs, such as are created in step 2 of BPPS and which serve as input to the MAPGAPS program. (MAPGAPS will also take as input a single MSA either in cma or fasta format.) For a single MSA, the cma format consists of a header line, such as ‘[0_(1)=name(135){go = 10000,gx = 2000,pn = 1000.0,lf = 0,rf = 0}:'. The leftmost ‘0’ labels this as the root node of a hierarchical MSA; ‘(1)’ indicates a single aligned block (this parameter is utilized during MCMC sampling); ‘name’ labels the MSA; ‘135’ indicates the number of aligned sequences; and the string in curly brackets gives parameter settings that are not used here. This is followed by a second header line, such as ‘(20)********************', where ‘20’ indicates the number of aligned columns and the asterisks designate which columns MCMC column should be sampled (Neuwald et al., 1997).

Each sequence in the MSA is specified by three lines. An example of the first line is ‘$41 = 34(28):', where ‘$41’ indicates that this is the 41st sequence, ‘34’ indicates the total number of residues in the sequence and ‘28’ the number of residues and gaps (‘-‘) minus the number of insertions (this information is required for MCMC sampling). The second line gives a fasta formatted identifier and description, such as ‘>4ABC_A’. And the third line, such as ‘{(QEYP)ID-QTGKCEPYigqiTKCStfLPNST(NVTN)}*', specifies the aligned sequence where residues within parentheses represent regions flanking the aligned region on either side; upper- and lower-case letters represent matching and insertion residues, respectively; and gap characters represent deletions. The curly brackets on each end allow multiple aligned blocks to be defined during MCMC sampling. The last line of the MSA, such as ‘_0].', indicates the end of the MSA; this syntax allows multiple (hierarchically arranged) MSAs to be included within a single input file.

### Additional considerations

BPPS assigns a log-odds score to each pattern residue; ranked by these scores, a specific number of positions are considered by SIPRIS. SIPRIS identifies the statistically most significant intersection, if any, between the BPPS- and structurally defined residue sets; adjusting its p-value for the number of starting residues considered. Note that discriminating residues outside of the intersection may have BPPS scores as high as or higher than those within; SIPRIS makes no distinctions in this regard.

### PyMol 3D visualization

Given structural coordinates as input, the BPPS and SIPRIS programs will generate PyMol (Schrodinger, 2010) scripts to aid visualization of BPPS-defined residues and of BPPS-SIPRIS structural networks, respectively.
