# Structural basis for the hijacking of endosomal sorting nexin proteins by Chlamydia trachomatis

## Authors

- Blessy Paul<sup>1</sup>
- Hyun Sung Kim<sup>1</sup>
- Markus C Kerr<sup>1</sup>
- Wilhelmina M Huston<sup>2</sup>
- Rohan D Teasdale<sup>1</sup> †
- Brett M Collins<sup>1</sup> ([ORCID: 0000-0002-6070-3774](https://orcid.org/0000-0002-6070-3774)) †

### Affiliations

1. Institute for Molecular Bioscience The University of Queensland St. Lucia Australia
2. School of Life Sciences University of Technology Sydney Sydney Australia

† Corresponding author

## Abstract

During infection chlamydial pathogens form an intracellular membrane-bound replicative niche termed the inclusion, which is enriched with bacterial transmembrane proteins called Incs. Incs bind and manipulate host cell proteins to promote inclusion expansion and provide camouflage against innate immune responses. Sorting nexin (SNX) proteins that normally function in endosomal membrane trafficking are a major class of inclusion-associated host proteins, and are recruited by IncE/CT116. Crystal structures of the SNX5 phox-homology (PX) domain in complex with IncE define the precise molecular basis for these interactions. The binding site is unique to SNX5 and related family members SNX6 and SNX32. Intriguingly the site is also conserved in SNX5 homologues throughout evolution, suggesting that IncE captures SNX5-related proteins by mimicking a native host protein interaction. These findings thus provide the first mechanistic insights both into how chlamydial Incs hijack host proteins, and how SNX5-related PX domains function as scaffolds in protein complex assembly.

## Introduction

To counter host defence mechanisms intracellular bacterial pathogens have evolved numerous strategies to evade immune detection, replicate and cause infection. Many pathogens manipulate endocytic pathways to gain entry into host cells and generate a membrane-enclosed replicative niche. This frequently involves hijacking or inhibiting the host cell trafficking machinery, first to generate the pathogen containing vacuole (PCV) and subsequently to prevent fusion with lysosomal degradative compartments. Concomitantly the pathogen often endeavors to decorate the PCV with host proteins and lipids that mimic other host cell organelles in order to circumvent innate immune detection, expand the replicative niche and acquire nutrients to support intracellular replication (Di Russo Case and Samuel, 2016; Personnic et al., 2016). This process is often orchestrated through the action of molecular syringe-like secretion systems that deliver bacterial effector proteins directly into the host cell cytoplasm.

Chlamydia trachomatis is arguably one of the most successful human bacterial pathogens by virtue of its capacity to hijack host cell intracellular trafficking and lipid transport pathways to promote infection (Bastidas et al., 2013; Derré, 2015; Elwell et al., 2016; Moore and Ouellette, 2014). C. trachomatis causes nearly 100 million sexually transmitted infections annually worldwide, and if left unchecked leads to various human diseases including infection-induced blindness, pelvic inflammatory disease, infertility and ectopic pregnancy (Aral et al., 2006; Newman et al., 2015). Even though chlamydial infections can generally be treated with antibiotics, persistent infections remain a challenge (Kohlhoff and Hammerschlag, 2015; Mpiga and Ravaoarinoro, 2006).

All Chlamydiae share a common dimorphic life cycle, where the bacteria alternates between the infectious but non-dividing elementary body (EB) form, and the non-infectious but replicative reticulate body (RB) form. Following internalization of EBs through a poorly defined endocytic process, the bacteria reside in a membrane-bound vacuole termed the inclusion, where they convert into RBs and replication occurs over 24–72 hr. RBs eventually redifferentiate back to EBs in an asynchronous manner, and are then released to infect neighboring cells (Di Russo Case and Samuel, 2016; Hybiske, 2015; Ward, 1983). The encapsulating inclusion membrane provides the primary interface between the bacteria and the host cell’s cytoplasm and organelles. From the initial stages of invasion until eventual bacterial egress the chlamydial inclusion is extensively modified by insertion of numerous Type-III secreted bacterial effector proteins called inclusion membrane proteins or ‘Incs’. The Incs modulate host trafficking and signaling pathways to promote bacterial survival at different stages, including cell invasion, inclusion membrane remodeling, avoidance of the host cell innate immune defense system, nutrient acquisition and interactions with other host cell organelles (Elwell et al., 2016; Moore and Ouellette, 2014; Rockey et al., 2002).

Chlamydiae secrete more than fifty different Inc proteins. While Incs possess little sequence similarity, they share a common membrane topology with cytoplasmic N- and C-terminal domains, separated by two closely spaced transmembrane regions with a short intra-vacuolar loop (Dehoux et al., 2011; Kostriukova et al., 2008; Li et al., 2008; Lutter et al., 2012; Rockey et al., 2002) (Figure 1A). The cytoplasmic N- and C-terminal sequences of the Inc proteins act to bind and manipulate host cell proteins. Reported examples include the binding of the small GTPase Rab4A by CT229 (Rzomp et al., 2006), Rab11A by Cpn0585 (Cortes et al., 2007), SNARE proteins by IncA (Delevoye et al., 2008), centrosomal and cytoskeletal proteins by Inc850 and inclusion protein acting on microtubules (IPAM) (Dumoux et al., 2015; Mital et al., 2015, 2010), myosin phosphatase by CT228 (Lutter et al., 2013), 14-3-3 and Arf family proteins by IncG and InaC (Kokes et al., 2015; Scidmore and Hackstadt, 2001), and the lipid transfer protein CERT by IncD (Derré et al., 2011; Elwell et al., 2011). Despite these reports, there are no known structures of Inc family members either alone or in complex with host effectors.

![Figure 1.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig1-v2.jpg)

**Figure 1.:** (A) HeLa cells stably expressing the mCherry-Rab25 inclusion membrane marker (red) were infected with C. trachomatis serovar L2 (24 hr) and transfected with myc-tagged SNX expression constructs. The samples were fixed and immunolabeled with anti-myc (green) and anti-chlamydial HtrA antibodies (white) and counterstained with DAPI (blue). Similar experiments using GFP-tagged proteins are shown in Figure 1—figure supplement 1A.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Hela cells were transiently transfected with GFP-tagged SNX and mCherry-Rab25 proteins as indicated, and infected with C. trachomatis serovar L2. Cells were imaged by confocal fluorescence microscopy for GFP-tagged proteins (green), endogenous SNX1 (blue), mCherry-Rab25 (red) and DAPI-stained nuclear material (white). Both GFP-SNX5 and GFP-SNX32 are recruited to inclusion membranes, but the distantly related SNX-BAR protein SNX8 is not. The images are maximum projections. (B) An example of SNX1-decorated tubules (green) often observed emanating from inclusion membranes (mCherry-Rab25 in red; DAPI staining in blue). The image is a maximum projection.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** HeLa cells stably expressing mCherry-Rab25 were infected with C. trachomatis serovar L2 (MOI ~0.5) for 24 hr and imaged by immunofluorescence microscopy using antibodies to SNX1, SNX2 and SNX5. mCherry-Rab25 provides marker for the inclusion membrane. The upper panels show control infections and lower panels show cells treated with wortmannin or Vps34-IN1 with concomitant loss of SNX association with endosomal compartments while inclusion localisation is unaffected. The images are maximum projections. Endosomal compartments are labeled with antibodies to endogenous Rab5 or Vps35 and Pearson’s correlation coefficients used to quantify loss of endosomal recruitment (100 cells per group; error bars, S.D). A movie showing the effect of wortmannin on GFP-SNX5 is shown in Video 1.

Two recent studies have greatly expanded the repertoire of host cell proteins known to associate with chlamydial inclusions and Inc proteins (Aeberhard et al., 2015; Mirrashidi et al., 2015). Both reports confirmed that membrane trafficking proteins are major components of the inclusion proteome; and in particular members of the endosomal sorting nexin (SNX) family are highly enriched. Specifically it was shown that the C. trachomatis IncE/CT116 protein could recruit SNX proteins containing bin-amphiphysin-Rvs (BAR) domains SNX1, SNX2, SNX5 and SNX6 (Mirrashidi et al., 2015). SNX1 and SNX2 are highly homologous and form heterodimeric assemblies with either SNX5 or SNX6 to promote endosomal membrane tubulation and trafficking (van Weering et al., 2012). A fifth protein SNX32 is highly similar to SNX5 and SNX6 but is almost exclusively expressed in the brain and has not yet been characterized. SNX recruitment to the inclusion occurs via the C-terminal region of IncE interacting with the phox-homology (PX) domains of SNX5 or SNX6 (Mirrashidi et al., 2015) (Figure 1A). Interestingly, RNAi-mediated depletion of SNX5/SNX6 does not slow infection but rather increases the production of infectious C. trachomatis progeny suggesting that the SNX recruitment is not done to enable bacterial infection. Instead it was proposed that because SNX proteins regulate endocytic and lysosomal degradation, the manipulation by IncE could be an attempt to circumvent SNX-enhanced bacterial destruction (Aeberhard et al., 2015; Mirrashidi et al., 2015).

Here we use X-ray crystallographic structure determination to define the molecular mechanism of SNX5-IncE interaction, and confirm this mechanism using mutagenesis both in vitro and in cells. When bound to SNX5, IncE adopts an elongated β-hairpin structure, with key hydrophobic residues docked into a complementary binding groove encompassing a helix-turn-helix structural extension that is unique to SNX5, SNX6, and the brain-specific homologue SNX32. A striking degree of evolutionary conservation in the IncE-binding groove suggests that IncE co-opts the SNX5-related molecules by displacing a host protein (as yet unidentified) that normally binds to this site. Our work thus provides both the first mechanistic insights into how protein hijacking is mediated by inclusion membrane proteins, and also sheds light on the functional role of the SNX5-related PX domains as scaffolds for protein complex assembly.

## Results

### IncE specifically binds and recruits SNX5, SNX6 and SNX32 to C. trachomatis inclusions

It was previously shown that the sorting nexins SNX1, SNX2, SNX5 and SNX6 are recruited to the inclusion membrane in C. trachomatis infected cells (Aeberhard et al., 2015; Mirrashidi et al., 2015). We first confirmed this for myc-tagged SNX1, SNX2 and SNX5 in HeLa cells infected with C. trachomatis serovar L2 (MOI ~0.5) for 18 hr. All three proteins were recruited to the inclusion membrane as assessed by co-localisation with the inclusion marker mCherry-Rab25 (Figure 1B) (Teo et al., 2016), as were GFP-tagged SNX1 and SNX5 but not the more distantly homologous GFP-SNX8 (Figure 1—figure supplement 1A). We also observed localization of the SNX proteins to extensive inclusion-associated membrane tubules in a subset of infected cells as described previously (Figure 1—figure supplement 1B) (Aeberhard et al., 2015; Mirrashidi et al., 2015). Interestingly, when infected cells are treated with wortmannin, a pan-specific inhibitor of phosphoinositide-3-kinase (PI3K) activity, we see a loss of the SNX proteins from punctate endosomes, but not from the inclusion membrane (Figure 1—figure supplement 2; Video 1). A similar result is seen for specific inhibition of PtdIns3P production by Vps34 using Vps34-IN1 (Figure 1—figure supplement 2). This offers two possibilities; that either SNX recruitment to the inclusion occurs via protein-protein interactions, and does not depend on the presence of 3-phosphoinositide lipids that typically recruit SNX proteins to endosomal membranes, or alternatively that PI3Ks are not present at the inclusion and therefore wortmannin treatment has no effect at this particular compartment. Given our structural and mutagenesis studies below we favor the former explanation.

![Video 1.](https://cdn.elifesciences.org/articles/22311/elife-22311-media1.mp4.jpg)

**Video 1.:** HeLa cells stably expressing mCherry-Rab25 (red) were transfected transiently with GFP-SNX5 (green) and infected with Chlamydia trachomatis L2 for 24 hr. Time-lapse videomicroscopy was performed using an interval of 1 min on an inverted Nikon Ti-E deconvolution microscope with environmental control at 40 x magnification. 10 min into recording 100 nM wortmannin was added.

Mirrashidi et al. (2015), demonstrated an in vitro interaction between IncE and the SNX5 and SNX6 PX domains. To confirm their direct association we assessed the binding affinities using isothermal titration calorimetry (ITC) (Figure 2A; Table 1). Initial experiments with the human SNX5 and SNX6 PX domains showed robust interactions with the IncE C-terminal domain (residues 107–132). The affinities (Kd) for SNX5 and SNX6 were essentially indistinguishable (0.9 and 1.1 µM respectively), but we detected no interaction with the PX domain of SNX1 confirming the binding specificity. The PX domains of SNX5 and SNX6 possess a helix-turn-helix structural insert (Koharudin et al., 2009), which is not found in any other SNX family members except for SNX32 (Figure 2B), a homologue expressed primarily in neurons (BioGPS (Wu et al., 2009)). Confirming a common recruitment motif in the SNX5-related proteins, ITC showed a strong interaction between IncE and the SNX32 PX domain similar to SNX5 and SNX6 (Kd = 1.0 µM) (Figure 2A; Table 1), and SNX32 was robustly recruited to inclusion membranes in infected cells (Figure 1B; Figure 1—figure supplement 1A). Overall, our data indicates that a common structure within the SNX5, SNX6 and SNX32 PX domains is required for IncE interaction.

![Figure 2.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig2-v2.jpg)

**Figure 2.:** (A) Binding affinity between IncE peptide (residues 107–132) and SNX PX domains by ITC. Top panels show raw data and lower panels show normalised integrated data. See Table 1 for the calculated binding parameters. Truncation analyses of the IncE peptide by ITC are shown in Figure 3, Table 2. (B) Sequence alignment of human SNX1, SNX5, SNX6 and SNX32 PX domains. Conserved residues are indicated in red. Side-chains that directly contact IncE in the crystal structure are indicated with black circles. Mutations that block IncE binding are highlighted with red triangles, and mutations that do not affect binding indicated with green circles. Secondary structure elements derived from the SNX5 crystal structure are indicated above. (C) Sequence alignment of IncE from C. trachomatis and putative homologues from C. muridarum and C. suis. IncE side-chains that directly contact SNX5 in the crystal structure are indicated with black circles. Mutations that block SNX5 binding are highlighted with red triangles, and mutations that do not affect binding indicated with green circles. Predicted transmembrane regions are indicated and C-terminal IncE sequences that form β-strands in complex with SNX5 are shown.

**Table 1.**
 Thermodynamic parameters of IncE binding to SNX PX domains*.


<table>
  <thead>
    <tr>
      <th>Sample cell</th>
      <th>Titrant</th>
      <th>Kd (µM)</th>
      <th>△H (kcal/mol)</th>
      <th>T△S (kcal/mol)</th>
      <th>△G (kcal/mol)</th>
      <th>N</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SNX5 PX</td>
      <td>IncE peptide†</td>
      <td>0.95 ± 0.07</td>
      <td>−6.9 ± 0.3</td>
      <td>−1.9 ± 0.05</td>
      <td>−8.2 ± 0.01</td>
      <td>1.01 ± 0.01</td>
    </tr>
    <tr>
      <td>SNX6 PX</td>
      <td>IncE peptide</td>
      <td>1.13 ± 0.08</td>
      <td>−5.0 ± 0.9</td>
      <td>−3.0 ± 1</td>
      <td>−8.0 ± 0.07</td>
      <td>1.01 ± 0.08</td>
    </tr>
    <tr>
      <td>SNX32 PX</td>
      <td>IncE peptide</td>
      <td>1.15 ± 0.07</td>
      <td>−6.9 ± 0.4</td>
      <td>−1.3 ± 0.8</td>
      <td>−8.2 ± 0.4</td>
      <td>1.06 ± 0.005</td>
    </tr>
    <tr>
      <td>SNX1 PX</td>
      <td>IncE peptide</td>
      <td>No binding</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Values are the mean from three experiments ±SEM.b.†IncE synthetic peptide sequence PANGPAVQFFKGKNGSADQVILVTQ._

Finally we tested a series of IncE truncation mutants for their binding to the SNX5 PX domain (Figure 3A, B and C; Table 2). Synthetic peptides were used with single amino acids removed sequentially from the N and C-terminus to determine the minimal sequence required for binding. These experiments showed that the shortest region of IncE able to support full binding to SNX5 encompasses residues 110–131 (GPAVQFFKGKNGSADQVILVT), while a shorter fragment containing residues 113–130 (VQFFKGKNGSADQVILV) can bind to SNX5 with a slightly reduced affinity. While variations are observed across the different C. trachomatis serovars (Harris et al., 2012) the SNX5-binding sequence appears to be preserved in all detected variants (Figure 3D). A comparison with other chlamydial species suggests that IncE is not very widely conserved in this Genus, being clearly identifiable only in the closely related mouse pathogen C. muridarum and swine pathogen C. suis (Figure 2C). Residues required for binding to SNX5 are preserved in these IncE homologues, but whether SNX proteins are also recruited during infection by these other chlamydial species remains to be determined.

![Figure 3.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig3-v2.jpg)

**Figure 3.:** (A) Representative ITC experiments for truncated IncE peptides. These experiments were conducted using a single batch of SNX5 PX domain to minimize batch-to-batch protein variation. (B) Plots of the affinity constants for selected peptides to highlight the progressive loss of binding with N and C-terminal truncations. (C) Sequences of the truncated IncE peptides are given, with a qualitative indication of binding strength relative to the IncE_1 peptide containing residues 107–132. Full binding is indicated by ‘++’ reduced binding by ‘+’ and lack of binding by ‘−‘. All sequence information and their Kd values are given in Table 2. When compared to the reference ITC experiment the binding affinity of peptides was unaffected when the first three N-terminal residues were removed (IncE_2, IncE_3 and IncE_4) and gradually became weaker until IncE_7, after which binding was abolished. Results from IncE_6 are inconclusive due to the difficulty in successfully dissolving the peptides in buffer (n.d.). C-terminal truncations showed that IncE_14 and IncE_15 had similar high binding affinities to the reference, while the binding of IncE_16 and IncE_17 became progressively weaker and peptides shorter than IncE_17 showed no binding. This data indicates that the minimal IncE binding sequence retaining full SNX5 binding is GPAVQFFKGKNGSADQVILVT, and a shorter fragment VQFFKGKNGSADQVIL can bind to SNX5, albeit with a slightly reduced affinity. (D) Sequence alignment of IncE from different C. trachomatis serovars.

**Table 2.**
 ITC data for SNX5 PX domain binding to truncated and mutated IncE peptides*.


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Peptide</th>
      <th>Sequence</th>
      <th>Kd (µM)</th>
      <th>△H (kcal/mol)</th>
      <th>T△S (kcal/mol)</th>
      <th>△G (kcal/mol)</th>
      <th>N</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SNX5 PX</td>
      <td>IncE_1</td>
      <td>PANGPAVQFFKGKNGSADQVILVTQ</td>
      <td>0.95 ± 0.07</td>
      <td>−6.9 ± 0.3</td>
      <td>−1.9 ± 0.05</td>
      <td>−8.2 ± 0.01</td>
      <td>1.01 ± 0.01</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_2</td>
      <td>ANGPAVQFFKGKNGSADQVILVTQ</td>
      <td>1</td>
      <td>−5.0</td>
      <td>−2.6</td>
      <td>−8.1</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_3</td>
      <td>NGPAVQFFKGKNGSADQVILVTQ</td>
      <td>0.93</td>
      <td>−6.7</td>
      <td>−1.4</td>
      <td>−8.1</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_4</td>
      <td>GPAVQFFKGKNGSADQVILVTQ</td>
      <td>0.87</td>
      <td>−6.8</td>
      <td>−1.2</td>
      <td>−8.2</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_5</td>
      <td>PAVQFFKGKNGSADQVILVTQ</td>
      <td>2</td>
      <td>−5.9</td>
      <td>−1.2</td>
      <td>−8.3</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_6</td>
      <td>AVQFFKGKNGSADQVILVTQ</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_7</td>
      <td>VQFFKGKNGSADQVILVTQ</td>
      <td>2.2</td>
      <td>−6.9</td>
      <td>−1.1</td>
      <td>−7.7</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_8</td>
      <td>QFFKGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_9</td>
      <td>FFKGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_10</td>
      <td>FKGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_11</td>
      <td>KGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_12</td>
      <td>GKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_13</td>
      <td>KNGSADQVILVTQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_14</td>
      <td>PANGPAVQFFKGKNGSADQVILVT</td>
      <td>0.72</td>
      <td>−5.1</td>
      <td>−1.6</td>
      <td>−8.4</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_15</td>
      <td>PANGPAVQFFKGKNGSADQVILV</td>
      <td>0.97</td>
      <td>−6.5</td>
      <td>−1.3</td>
      <td>−8.2</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_16</td>
      <td>PANGPAVQFFKGKNGSADQVIL</td>
      <td>1.1</td>
      <td>−5.6</td>
      <td>−1.4</td>
      <td>−8.12</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_17</td>
      <td>PANGPAVQFFKGKNGSADQVI</td>
      <td>8.7</td>
      <td>−2.7</td>
      <td>−2.5</td>
      <td>−6.9</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_18</td>
      <td>PANGPAVQFFKGKNGSADQV</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_19</td>
      <td>PANGPAVQFFKGKNGSADQ</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_20</td>
      <td>PANGPAVQFFKGKNGSAD</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_21</td>
      <td>PANGPAVQFFKGKNGSA</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_22</td>
      <td>PANGPAVQFFKGKNGS</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_23</td>
      <td>PANGPAVQFFKGKNG</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE_24</td>
      <td>PANGPAVQFFKGKN</td>
      <td>No binding</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE Q115A</td>
      <td>PANGPAVAFFKGKNGSADQVILVTQ</td>
      <td>6.3</td>
      <td>−5.3</td>
      <td>−1.6</td>
      <td>−6.9</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE F116D</td>
      <td>PANGPAVQAFKGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>IncE K118A</td>
      <td>PANGPAVQFFAGKNGSADQVILVTQ</td>
      <td>2.8</td>
      <td>−6.0</td>
      <td>−1.5</td>
      <td>−7.5</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td></td>
      <td>IncE V127D</td>
      <td>PANGPAVQFFKGKNGSADQDILVTQ</td>
      <td>No binding</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SNX5 PX L133D</td>
      <td>IncE_1</td>
      <td>PANGPAVQFFKGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SNX5 PX F136A</td>
      <td>IncE_1</td>
      <td>PANGPAVQFFKGKNGSADQVILVTQ</td>
      <td>No binding</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SNX5 PX E144A</td>
      <td>IncE_1</td>
      <td>PANGPAVQFFKGKNGSADQVILVTQ</td>
      <td>15</td>
      <td>−9.9</td>
      <td>−3.1</td>
      <td>−13</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>

_*Except for IncE_1 all other peptide-binding experiments were performed only once._

### The crystal structure of IncE in complex with the SNX5 PX domain

The canonical PX domain structure is composed of a three-stranded β-sheet (β1, β2 and β3) followed by three close-packed α-helices. The first and second α-helices are connected by an extended proline-rich sequence. Typically PX domains have been found to bind to the endosome-enriched lipid phosphatidylinositol-3-phosphate (PtdIns3P) via a basic pocket formed at the junction between the β3 strand, α1 helix and Pro-rich loop. In contrast SNX5, SNX6 and SNX32 possess major alterations in the PtdIns3P-binding pocket that preclude canonical lipid head-group docking (see below). In addition they possess a unique extended helix-turn-helix insert between the Pro-rich loop and α2 helix of unknown function (Figure 2B) (Koharudin et al., 2009).

To determine the structure of the SNX5-IncE complex we generated a fusion protein encoding the human SNX5 PX domain (residues 22–170) and C. trachomatis IncE C-terminal sequence (residues 108–132) attached at the PX domain C-terminus Figure 4—figure supplement 1A). This construct readily crystallised in several crystal forms, and we were able to determine the structure of the complex in three different spacegroups (Figure 4; Table 3; Figure 4—figure supplement 1B). Confirming that the fusion does not alter complex formation, the short linker region is disordered, and the mode of IncE-binding to SNX5 is identical in all three structures (Figure 4—figure supplement 1C and D). Because of the higher resolution, we focus our discussions on the structure of the SNX5 PX-IncE complex observed in the P212121 crystal form. The first three IncE N-terminal residues (Pro107, Ala108, Asn109) and the last three IncE C-terminal residues (Val130, Thr131, Gln132) were not modeled due to lack of electron density, suggesting disorder and matching precisely with our mapping experiments showing these residues are not necessary for SNX5 association.

![Figure 4.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig4-v2.jpg)

**Figure 4.:** (A) Crystal structure of the SNX5 PX domain (yellow) in complex with IncE residues 107–132 (magenta) shown in cartoon representation. (B) Backbone atoms of the SNX5 and IncE proteins are shown to highlight the prominent β-sheet augmentation mediating the association between the two molecules. (C) Close up view of the SNX5-IncE interface highlighting specific contact areas at the N-terminus of the IncE peptide. (D) Close up of the SNX5-IncE interface highlighting specific contact areas at the hairpin loop of the IncE peptide shown at 90° to Figure 4C. (E). Close up of the SNX5-IncE interface highlighting contact areas at the C-terminus of the IncE peptide in approximately the same orientation as Figure 4C. Residues in SNX5 (Phe136) and IncE (Phe116) that are critical for binding based on mutagenesis are boxed.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Sequence of the SNX5 PX domain fusion protein with the IncE C-terminal peptide. (B) Refined 2fo-fc electron density contoured at 1.5σ for the SNX5-IncE structure in spacegroup P212121. (C) Overlay of each independent SNX5-IncE complex observed in the three crystal forms. (D) Ribbon structures indicating the locations of the linker regions in each crystal form. The C-terminal SNX5 residues and the N-terminal IncE residues are shown by spheres with distances indicated.

**Table 3.**
 Summary of crystallographic structure determination statistics*.


<table>
  <thead>
    <tr>
      <th>Crystal</th>
      <th>SNX5 PX-IncE Form 1</th>
      <th>SNX5 PX-IncE Form 2</th>
      <th>SNX5 PX-IncE Form 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDB ID</td>
      <td>5TGI</td>
      <td>5TGJ</td>
      <td>5TGH</td>
    </tr>
    <tr>
      <td colspan="4">Data collection</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.95370</td>
      <td>0.95370</td>
      <td>0.95370</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P212121</td>
      <td>I2</td>
      <td>P32</td>
    </tr>
    <tr>
      <td colspan="4">Cell dimensions</td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>60.7, 67.5, 88.2</td>
      <td>58.4, 80.3, 94.6</td>
      <td>100.6, 100.6, 71.7</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 97.2, 90</td>
      <td>90, 90, 120</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>60.7–1.98 (2.03–1.98)</td>
      <td>31.9–2.6 (2.72–2.60)</td>
      <td>50.3–2.80 (2.95–2.80)</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>0.104 (0.525)</td>
      <td>0.153 (0.659)</td>
      <td>0.101 (0.713)</td>
    </tr>
    <tr>
      <td>Rmeas</td>
      <td>0.112 (0.572)</td>
      <td>0.18 (0.777)</td>
      <td>0.124 (0.873)</td>
    </tr>
    <tr>
      <td>Rpim</td>
      <td>0.042 (0.225)</td>
      <td>0.096 (0.408)</td>
      <td>0.051 (0.363)</td>
    </tr>
    <tr>
      <td>&lt;I&gt; / σI</td>
      <td>12.4 (3.4)</td>
      <td>39.6 (3.2)</td>
      <td>11.7 (2.3)</td>
    </tr>
    <tr>
      <td>Total number reflections</td>
      <td>178868 (11000)</td>
      <td>46691 (5757)</td>
      <td>115149 (16861)</td>
    </tr>
    <tr>
      <td>Total unique reflections</td>
      <td>26075 (1805)</td>
      <td>13432 (1632)</td>
      <td>20001 (2923)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>100 (100)</td>
      <td>99.9 (100.0)</td>
      <td>100 (100)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>6.9 (6.1)</td>
      <td>3.5 (3.5)</td>
      <td>5.8 (5.8)</td>
    </tr>
    <tr>
      <td>Half-set correlation (CC(1/2))</td>
      <td>0.997 (0.868)</td>
      <td>0.986 (0.55)</td>
      <td>0.997 (0.683)</td>
    </tr>
    <tr>
      <td colspan="4">Refinement</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>45.1–1.98 (2.02–1.98)</td>
      <td>31.9–2.6 (2.69–2.60)</td>
      <td>41.2–2.8 (2.87–2.80)</td>
    </tr>
    <tr>
      <td>No. reflections/No. Rfree</td>
      <td>26021/2000</td>
      <td>13421/1342 (1208/134)</td>
      <td>19975/1972 (1301/144)</td>
    </tr>
    <tr>
      <td>Rwork/Rfree</td>
      <td>0.192/0.214 (0.221/0.246)</td>
      <td>0.199/0.242 (0.276/0.332)</td>
      <td>0.236/0.254 (0.329/0.372)</td>
    </tr>
    <tr>
      <td colspan="4">No. atoms</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>2579</td>
      <td>2619</td>
      <td>5189</td>
    </tr>
    <tr>
      <td>Solvent</td>
      <td>281</td>
      <td>69</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Average B-factor (Å2)</td>
      <td>31.8</td>
      <td>42.5</td>
      <td>56.0</td>
    </tr>
    <tr>
      <td colspan="4">R.m.s deviations</td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.012</td>
      <td>0.011</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>1.27</td>
      <td>1.15</td>
      <td>1.27</td>
    </tr>
  </tbody>
</table>

_*Highest resolution shell is shown in parentheses._

The IncE sequence forms a long β-hairpin structure that binds within a complementary groove at the base of the extended α-helical insertion of the SNX5 PX domain and adjacent to the β-sheet sub-domain (Figure 4A; Video 2). The β-hairpin structure of IncE (N-terminal βA and C-terminal βB strands) is directly incorporated as a β-sheet augmentation of the β1, β2 and β3 strands of SNX5 (Figure 4B). The N-terminal βA strand of the IncE sequence (Gly111-Lys118) forms the primary interface with SNX5, making main-chain hydrogen bonds with the β1 strand of the SNX5 PX domain for the stable positioning of the IncE structure. The two anti-parallel β-strands of IncE are connected by a short loop (Gly119-Ala124) that makes no direct contact with the SNX5 protein, and the C-terminal IncE βB strand (Asp125-Val130) forms an interface with the extended α-helical region of the SNX5 PX domain.

![Video 2.](https://cdn.elifesciences.org/articles/22311/elife-22311-media2.mp4.jpg)

**Video 2.:** The SNX5 PX domain is shown in yellow ribbons and the IncE peptide is shown in magenta.

Detailed views of the SNX5-IncE interface are shown in Figure 4C, D and E. Aside from main-chain hydrogen bonding to form the extended β-sheet, IncE engages in several critical side-chain interactions with the relatively hydrophobic SNX5 binding groove. At the N-terminus of the βA strand Val114 of IncE inserts into a pocket formed primarily by Tyr132 and Phe136 on the SNX5 α’’ helix (Figure 4C). A major contribution comes from IncE Phe116, with π-stacking occurring with the Phe136 side-chain and hydrophobic docking with Val140 of SNX5 (Figure 4D). Adjacent to IncE Phe116 at the end of the βA strand Lys118 makes an electrostatic contact with SNX5 Glu144. Finally, at the C-terminal end of the IncE βB strand Val127 and Leu129 contact an extended SNX5 surface composed of Leu133, Tyr132 and Met106 (Figure 4E).

### Mutations in the SNX5-IncE interface disrupt complex formation in vitro and in cells

To verify the crystal structure we mutated residues from both SNX5 and IncE and measured their affinities using ITC (Figure 5A and B; Table 2). At the interface between SNX5 and IncE several side chains make key contributions to peptide recognition. Because Leu133 and Phe136 residues in SNX5 are located at the core of the IncE-binding interface, and also due to the structural rearrangements these residues make on binding (see below), we reasoned that L133D and F136A mutations would inhibit the interaction. Indeed these mutants abolished association with the IncE peptide (Figure 5A). The reciprocal mutations in IncE residues F116A and V127D also abolished binding to the SNX5 PX domain (Figure 5B), and the SNX6 and SNX32 PX domains (Figure 5—figure supplement 1), demonstrating the importance of these hydrophobic and π-stacking interactions for stable complex formation. In contrast mutations predicted to disrupt an observed electrostatic contact (IncE K118A or SNX5 E144A) had little effect on binding. Thus the core hydrophobic interactions are critical for IncE binding but the peripheral electrostatic contact is not essential.

![Figure 5.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig5-v2.jpg)

**Figure 5.:** (A) ITC experiments testing the effect of SNX5 mutations on IncE binding. Both L133D and F136A mutations prevented IncE binding, but the A144A mutation had little effect. (B) ITC experiments testing the effect of IncE mutations on SNX5 binding. Both F116A and V127D blocked SNX5 interaction, while Q115A had a partial effect and K118A had no effect on association.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** ITC experiments testing the effect of IncE peptide mutations on binding to SNX6 and SNX32 PX domains. The IncE F116A mutation blocks interaction with both PX domains similarly to SNX5 (Figure 5B).

To confirm the role of IncE in direct SNX5 protein recruitment to the chlamydial inclusion we examined the localisation of GFP-tagged SNX5 in HeLa cells infected with C. trachomatis L2 (CTL2) for 24 hr (MOI ~0.5). Cells expressing the GFP-SNX5 protein showed clear and uniform recruitment to the limiting membrane of the inclusion as defined by mCherry-Rab25 (Figure 6A), which is consistent with the localisation observed by others (Aeberhard et al., 2015; Mirrashidi et al., 2015). In contrast, the GFP-SNX5 (F136A) mutant protein showed no recruitment to the chlamydial inclusion. The change in relative distribution of these GFP-SNX5 proteins on the inclusion was quantified for wildtype SNX5 (Mander’s coefficient 0.67 ± 0.14) and GFP-SNX5 (F136A) (0.041 ± 0.051) (Figure 6—figure supplement 1A). Like wild-type GFP-SNX5 the GFP-SNX5 (F136A) mutant was recruited to punctate endosomal structures throughout the cytoplasm of these cells, and in addition was able to co-immunoprecipate endogenous SNX1 in heterodimeric complexes identically to the wild-type GFP-SNX5 protein (Figure 6—figure supplement 1B). This implies that BAR-domain mediated heterodimer formation with SNX1 or SNX2 is required for endosomal recruitment, and is not perturbed by the IncE-binding mutation in the PX domain. Lastly, we tested the importance of IncE residues for SNX interaction in situ by expressing the GFP-tagged IncE C-terminal domain. The wild-type GFP-IncE(91-132) was recruited to endosomal structures via its interaction with SNX5-related proteins in both uninfected and infected HeLa cells (Figure 6B; Figure 6—figure supplement 1C). In contrast however, GFP-IncE(91-132)(F116D), a SNX5-binding mutant, was exclusively cytosolic. Note that neither IncE construct is localised to the inclusion, as expected due to lack of signal peptides and transmembrane domains (Figure 6—figure supplement 1C).

![Figure 6.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig6-v2.jpg)

**Figure 6.:** (A) Single amino-acid mutation in the PX domain of the SNX5 (F136A) abolishes recruitment to the chlamydial inclusion. HeLa cells stably expressing mCherry-Rab25 (red) were transfected transiently with GFP-SNX5 or GFP-SNX5 (F136A) (green) and infected with Chlamydia trachomatis L2 for 18–24 hr. The cells were fixed and the nucleic materials were counter-stained with DAPI (blue). (B) HeLa cells were transfected transiently with GFP-IncE(91-132) or GFP-IncE(91-132)(F116D) (green) and co-labelled for the early endosomal marker EEA1 (red). Mutation in the SNX5 binding IncE peptide (F116D) abolishes recruitment to endosomal structures. *Represents the inclusion. Scale bar 20 μm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Quantitation of the degree of overlap between the GFP-SNX5 constructs and the mCherry-Rab25 inclusion membrane marker from Figure 6A. Mander’s correlation coefficient of mChRab25 signal over GFP-SNX5 signals (10 cells per group; error bars, S.D). (B) Co-immunoprecipitation of GFP-SNX5 from HeLa cells shows that both the wild-type and mutant protein (F136A) interact equally with endogenous SNX1. This indicates that both proteins are correctly folded and otherwise functional. (C) HeLa cells stably expressing mCherry-Rab25 (red) were transfected transiently with GFP-IncE(91-132) or GFP-IncE(91-132)(F116D) (green) and infected with C. trachomatis L2 for 18–24 hr. Mutation in the SNX5 binding IncE peptide (F116D) abolishes recruitment to endosomal structures. Neither construct is recruited to inclusions, which is consistent with the lack of transmembrane regions. *Represents the inclusion. Scale bar 20 μm.

### A model for SNX-BAR recruitment to the inclusion membrane by IncE

Superposition of the SNX5-IncE complex with the SNX5 PX domain in the apo state (Koharudin et al., 2009) reveals a significant conformational change in the α-helical extension, as well as localized alterations in the loop between the β1 and β2 strands to accommodate peptide binding (Figure 7A). In essence the IncE β-hairpin acts as a tether between the core PX fold and extended α-helical hairpin, pulling the two sub-structures closer together. Overall the α-helical extension undergoes a maximal movement of ~8–10 Å at the furthest tip, facilitated by the flexibility of the structure following the Pro-rich linker and an apparent hinge-point at Pro97 (Figure 7A upper panel). In the immediate vicinity of Pro97 the SNX5 loop that encompasses Asp43 is significantly shifted and stabilized by the repositioning of Arg103. At both the start of the first α’ helix of the extension and the end of the second α’’ helix more subtle changes occur in the positions of Met106, Leu128, Tyr132, Leu133 and Phe136. These changes result in formation of the hydrophobic pocket that engages the IncE side-chains Val114, Phe116, Val127 and Leu129 (Figure 7A, middle and lower panels).

![Figure 7.](https://cdn.elifesciences.org/articles/22311/elife-22311-fig7-v2.jpg)

**Figure 7.:** (A) Comparison of the SNX5-IncE complex (yellow-magenta) with the previously reported apo- SNX5 PX domain crystal structure (blue) (PDB ID 3HPB)(Koharudin et al., 2009). The α-helical extension undergoes a significant displacement in the bound state. The enlarged panels to the right show several close-up views of the binding pocket highlighting conformational changes that are required to accommodate IncE. (B) A model for the SNX5-SNX1 PX-BAR heterodimer and its interaction with IncE at the inclusion membrane. The PX-BAR structure was modeled in silico (see methods). The left panel shows cartoon representations of the structure, viewed from the side and from the membrane surface. Middle panels show the same structures in electrostatic surface representation (red, negative; blue positive). The right panels show close ups of the putative PtdIns3P-binding pocket in SNX1 and SNX5, with a PtdIns3P head-group (shown in spheres) docked by aligning the previous SNX9 crystal structure (Pylypenko et al., 2007). SNX1 has a canonical PtdIns3P pocket, while SNX5 lacks a clear site for lipid head-group binding. (C) Sequence conservation of SNX5-related proteins was calculated and plotted using CONSURF. The surface representation indicates exposed side-chains that are evolutionarily conserved in green. The IncE peptide binds to a highly conserved surface groove, while the putative phosphoinositide binding region (Koharudin et al., 2009) on the opposite face is neither highly conserved nor poised to allow docking. (D) Cartoon model depicting the recruitment of SNX5 and related proteins to the inclusion membrane. Heterodimers with SNX1 or SNX2 will be recruited via IncE in infected cells, and this recruitment will be in competition with the binding of SNX1 and SNX2 to PtdIns3P for normal endosomal association, as well as interactions with other proteins including retromer and unidentified molecules that potentially bind to the conserved groove of the SNX5 PX domain.

To better understand how IncE can recruit the SNX5-containing SNX-BAR complexes to inclusion membranes we constructed an in silico model of the SNX5-SNX1 heterodimeric PX-BAR proteins (Figure 7B). Consistent with the length of the IncE C-terminal cytoplasmic sequence the model predicts that the IncE sequence will bind to the surface of SNX5 close to, but oriented away from, the inclusion membrane. While PX domains are commonly able to recognise PtdIns3P lipid headgroups, SNX5-related proteins lack the typical binding pocket (Figure 7B right panel), and there is some controversy regarding their ability to mediate specific membrane interactions (Koharudin et al., 2009; Teasdale and Collins, 2012). We propose that in the context of C. trachomatis infection, SNX5-related proteins are directly associated with the inclusion via IncE protein-protein interactions in a phosphoinositide-independent manner, and are able to recruit their heterodimeric partners SNX1 and SNX2 (Sierecki et al., 2014; van Weering et al., 2012; Wassmer et al., 2009). The PX-BAR-domain containing complexes are then localised to the inclusion in a retromer-independent manner (Mirrashidi et al., 2015), and may contribute to the formation of the dynamic inclusion-associated membrane tubules.

Interestingly, when a cross-species evolutionary analysis of side-chain conservation in the SNX5-related proteins is performed it is clear that the IncE peptide binds a hydrophobic surface groove that is strictly conserved in this protein family (Figure 7C). This very strongly implies that the site is normally engaged in a protein-protein interaction with an as yet unidentified binding partner(s) required for SNX5’s regular biological function, and that IncE is directly competing for this interface.

## Discussion

Although more than fifty putative Incs have been identified in C. trachomatis, the exact roles of these inclusion membrane proteins are still poorly understood. Chlamydiae manipulate the host cellular and signaling networks via interactions between the cytoplasmic region of Incs and numerous host cell proteins. Recent studies reported retrograde trafficking proteins as significant components of the inclusion, with sorting nexin family members being particularly enriched (Aeberhard et al., 2015; Mirrashidi et al., 2015). In this study, we present the first reported crystal structure of a chlamydial inclusion protein (IncE) binding to its host effector protein (SNX5). While the detailed mechanism of IncE-mediated protein recruitment will be specific to this family member, the principle of extended cytoplasmic Inc sequences engaging with cellular host proteins on the inclusion is certain to be a general one. A simple analogy would be to consider the Inc proteins as being like a molecular ‘velcro’ that recognises and attaches host machinery needed for bacterial replication and survival.

The manipulation of endocytic transport machinery is clearly critical for the obligate intracellular survival of C. trachomatis (Aeberhard et al., 2015; Mirrashidi et al., 2015; Moore and Ouellette, 2014). In addition to C. trachomatis, SNX1, SNX2, SNX5, SNX6 and the associated retromer complex have also been directly implicated in the cellular pathogenesis of Coxiella burnetii (McDonough et al., 2013), Salmonella enterica serovar Typhimurium (Bujny et al., 2008), hepatitis C virus (Yin et al., 2016), human papilloma virus (Ganti et al., 2016; Popa et al., 2015), and Legionella pneumophila (Finsel et al., 2013). Broadly then the manipulation of SNX proteins and endosomal trafficking machinery by viral and bacterial pathogens is a common occurrence during intracellular infection, and points to a wide-ranging role in host-pathogen interactions.

Typically PX domains of sorting nexins, including SNX1 and SNX2 (Cozier et al., 2002; Zhong et al., 2005), play an important role in endosomal membrane recruitment by binding the endosome-enriched lipid PtdIns3P through four conserved residues (Mas et al., 2014; Teasdale and Collins, 2012). These residues are conserved in most PX domains including in SNX1 and SNX2, but are entirely absent in SNX5, SNX6 and SNX32. Although there is evidence for the weak association of the SNX5 PX domain with the lipid PtdIns(4,5)P2 from nuclear magnetic resonance (NMR) spectroscopy experiments (Koharudin et al., 2009), the crystal structure does not point to a clear binding mechanism. A second feature that sets SNX5-related proteins apart from the rest of the SNX family is the presence of an extended α-helical insertion. Our work confirms the central importance of this unique insert for the binding of the IncE inclusion protein, and provides the first clear description of how a PX domain can function as a protein-protein interaction scaffold as opposed to a lipid-binding domain.

The high degree of conservation in the IncE binding surface of SNX5 implies that this site is critical for the normal function of SNX5 and its homologs. Previously, the expression of a GFP-tagged IncE C-terminal domain was shown to interfere with the SNX5/SNX6-dependent retrograde trafficking of the cation-independent mannose-6-phosphate receptor (CI-MPR) (Mirrashidi et al., 2015). Combined with our structural data, this infers that IncE is mimicking and interfering with SNX5/SNX6-mediated protein interactions, with a ligand(s) required for normal endosomal trafficking that remains to be discovered. Once recruited to the inclusion, SNX-BAR proteins are localized to the bulk membrane and dynamic tubules. While it is logical to imagine they could play a positive role in the sculpting of the inclusion, this is somewhat difficult to reconcile with the effect of SNX5 and SNX6 knockdown, which results in an increased production of C. trachomatis infectious progeny. Alternatively, although a pool of SNX5/SNX6 and associated SNX1/SNX2 proteins remain on endosomes in C. trachomatis infected cells, their sequestering by the chlamydial inclusion may interfere with normal endosomal trafficking (Figure 7D). It was thus proposed that the role of IncE could be to compete for SNX-retromer endosomal interactions, resulting in the breakdown of normal trafficking of the CI-MPR and lysosomal hydrolases and hence perturbation of the endolysosomal system’s capacity for bacterial destruction (Aeberhard et al., 2015; Mirrashidi et al., 2015). Defining the precise role of SNX proteins and other endocytic machinery in chlamydial infection will clearly require further study.

In conclusion, our work provides novel molecular insights into the mechanism of SNX protein coercion by the IncE chlamydial effector, and presents a blueprint for future studies of other inclusion protein activities. In addition, our results provide a possible clue to understanding how SNX5-related molecules mediate protein interactions required for canonical cell trafficking pathways.

## Materials and methods

### Peptides

All synthetic peptides used for isothermal titration were purchased from Genscript (USA). For ITC experiments, peptides were weighed and dissolved in 50 mM Tris (pH 8.0) and 100 mM NaCl (ITC buffer) to make a stock peptide concentration of 2 mM, which was diluted to 0.75 mM before use.

### Antibodies and reagents

Polyclonal antibodies against C. trachomatis HtrA were generated previously (Huston et al., 2008). Monoclonal antibodies against EEA1 (610457, 1:100), SNX1 (611483,1:200) and SNX2 (611308, 1:200) were supplied by BD Bioscience. Monoclonal antibodies against the myc epiptope (9B11, 1:2000) were supplied by Abcam. Rabbit polyclonal antibodies against GFP (A-6455, 1:500) were purchased from Molecular Probes (Invitrogen). Rabbit polyclonal antibodies against Rab5 (C8B1, 1:100) were from Cell Signaling Technology. Goat polyclonal antibodies against Vps35 (IMG-3575, 1:400) were from Imgenex. Secondary antibodies were purchased from Molecular Probes (Life Technologies) and Li-Cor Bioscience. Wortmannin was supplied by Sigma-Aldrich (W1628). VPS34-In1 was from Merck Millipore (532628).

### Molecular biology and expression constructs

The IncE sequence used in this study is from the L3 serovar L3/404/LN (NCBI reference WP_015506602) (Harris et al., 2012). The pGEX-4T-2 bacterial expression plasmid encoding the human SNX5 PX domain (residues 22–170) was generated using a standard PCR-based cloning strategy, and its identity confirmed by sequencing. All other bacterial expression constructs for human SNX proteins were synthesized and cloned into pGEX-4T-2 by Genscript (USA). These included the SNX5 PX domain IncE fusion (SNX5 residues 22–170 with IncE residues 108–132 fused at the C-terminus (Figure 4—figure supplement 1A), SNX6 (residues 29–170), SNX32 (residues 17–166), and SNX5 PX domain mutants. The pcDNA3.1-N-eGFP mammalian expression constructs encoding full-length human SNX5, SNX5(F136A), IncE(91-132) and IncE(91-132)(F116D) with N-terminal GFP-tags were generated by Genscript (USA). The pCMU-myc-SNX5 was as described previously (Kerr et al., 2006), and the SNX6 and SNX32 genes cloned into the pcDNA3.1-nMyc vector at BamHI and XhoI restriction sites (Kerr et al., 2012). SNX5, SNX32 and SNX8 were also cloned by polymerase chain reaction, restriction digest and ligation into pEGFP-C1 for expression with N-terminal GFP tags as described previously (Wang et al., 2010).

### Recombinant protein expression and purification

All proteins except SNX5 PX domain mutants were expressed in Escherichia coli Rosetta cells, whereas mutant constructs were expressed in BL21 Codon Plus supplemented with appropriate antibiotics. Single colonies from cultures grown on LB agar plates were inoculated into 50 mL LB2+ with ampicillin (0.1 mg/mL) and chloramphenicol (0.1 mg/mL), and grown at 37°C with shaking overnight. The following day, 30 mL from the overnight culture was used to inoculate 1 L LB media containing ampicillin (0.1 mg/mL) and chloramphenicol (0.1 mg/mL) and incubated at 37°C. Cells were grown to an optical density (OD) of 0.5–0.6 at 600 nm and induced with 0.5 mM isopropyl-β-D-thiogalactopyranoside (IPTG) (except for the SNX5-IncE fusion, where expression was induced at OD600 of 0.8 with 1 mM IPTG). Cultures were incubated with shaking overnight at 18°C until the cells reach an O.D of 3.0 (~24 hr). Cells were harvested using a Beckman rotor JLA 8.1000 at 4000 RPM for 30 min at 4°C. Pellets were resuspended in 10 mL lysis buffer (50 mM Tris (pH 8.0), 100 mM NaCl, 5% glycerol, 1 mM DTT, 0.1 mg/ml benzamidine, 0.1 mg/ml DNase) per litre of culture. The cells were subjected to cell disruption and centrifugation at 18,000 RPM for 30 min at 4°C. The soluble fractions were first purified using affinity chromatography with glutathione-sepharose, and when required the GST tags were cleaved by thrombin while still bound to the column. The proteins were eluted in 50 mM Tris (pH 8.0), 100 mM NaCl, 5% glycerol, and 1 mM DTT, and then further polished using gel filtration chromatography (Superdex 200, GE healthcare) in a buffer containing 50 mM Tris (pH 8.0), 100 mM NaCl. The fractions corresponding to the respective proteins were then pooled and used directly for ITC or were further concentrated for crystallization.

### Isothermal titration calorimetry

ITC experiments were performed on a Microcal iTC200 instrument at 25°C. The proteins were buffer exchanged into ITC buffer (50 mM Tris (pH 8.0) and 100 mM NaCl) by gel filtration prior to ITC experiments. IncE peptides at 750 µM were titrated into 50 µM PX domain samples. The binding data was processed using ORIGIN 7.0 with a single site binding model to determine the stoichiometry (n), the equilibrium association constant Ka (1/Kd), and the enthalpy (△H). The Gibbs free energy (△G) was calculated using the equation △G = −RTIn(Ka); binding entropy (△S) was calculated by △G = △H – T△S. Three experiments were performed for each set of samples to determine the average ± standard error of the mean (SEM) for thermodynamic quantities, except for the peptide truncation experiments where only single experiments were performed. For these truncated peptide experiments, all experiments were performed using the same batch of protein to allow direct comparions to be made.

### Crystallization, data collection and structure determination

The SNX5 PX domain fusion with IncE was concentrated to 15 mg/ml for crystallization. Eight 96-well crystallization hanging-drop screens were set up using a Mosquito Liquid Handling robot (TTP LabTech) at 20°C. Optimized diffraction-quality crystals were obtained using streak seeding in sitting drop vapor diffusion plates. The crystallisation solution for crystal form 1 was 0.2 M KSCN, 25% PEG 2K MME, 100 mM sodium acetate (pH 5.5), for crystal form 2 was 0.1 M NaCl, 0.1 M MgCl2, 0.1 M Nacitrate (pH 3.5), 12 % PEG 4000, and for crystal form 3 was 1.26 M (NH4)2SO4, acetate (pH 4.5), 0.2 M NaCl. Data were collected at the Australian Synchrotron MX1 and MX2 Beamlines, integrated with iMOSFLM (Battye et al., 2011), and scaled with AIMLESS (Evans and Murshudov, 2013) in the CCP4 suite (Winn et al., 2011). The structures were initially solved by molecular replacement with PHASER (McCoy et al., 2007) using the apo-SNX5 PX domain crystal structure as the input model (PDB code 3HPB), minus the extended α-helical domain. The resulting model was rebuilt with COOT (Emsley et al., 2010), followed by repeated rounds of refinement with PHENIX (Adams et al., 2011). All structural figures were generated using PyMOL (DeLano scientific).

### Cell culture and transfections

HeLa cells stably expressing mCherry-Rab25 were previously generated within the lab (Teo et al., 2016) and were maintained in DMEM (Gibco) supplemented with 10% (v/v) FCS (Bovogen) and 2 mM L-glutamine (Invitrogen) in a humidified air/atmosphere (5% CO2) at 37°C. Cells were transfected at 70% confluence with pcDNA3.1-N-eGFP plasmid constructs using Lipofectamine 2000 as per manufacturer’s protocol (Invitrogen) and examined 18–24 hr later. The HeLa cell line used in this study was from America Type Culture Collection (#ATCC CCL2). Parental and stable cells lines were negative for mycoplasma by DAPI staining, and authenticated by STR profiling (Cell Bank Australia). For inhibitor treatments, cells were treated with either 100 nM wortmannin or 1 µM Vps34-IN1 for 1 hr.

### Chlamydial infection assays

C.C. trachomatis serovar L2 (ATCC VR-902B) was used to infect cells at a multiplicity of infection (MOI) of ~0.5. Cells were infected 2 hr post-transfection in normal DMEM (Gibco) supplemented with 10% (v/v) FCS (Bovogen) and 2 mM L-glutamine (Invitrogen) in a humidified air/atmosphere (5% CO2) incubator at 37°C. After 2 hr media was replaced with fresh media.

### Microscopy

Transfected and infected cells (18–24 hr post-infection) were fixed with 4% paraformaldehyde, permeabilised using TritonX-100 (Sigma) and immunolabeled as described previously (Teo et al., 2016) and counter-stained with DAPI. The coverslips were imaged using a confocal laser-scanning microscope (LSM 710 meta, Zeiss) with 63x oil immersion objective. Time-lapse videomicroscopy was carried out on individual live cells using a Nikon Ti-E inverted deconvolution microscope using a 40x, 0.9 Plan Apo DIC objective, a Hamamatsu Flash 4.0 4Mp sCMOS monochrome camera and 37°C incubated chamber with 5% CO2. GFP was excited with a 485/20 nm LED and captured using a 525/30 nm emission filter, and mCherry was excited using a 560/25 nm LED and captured using a 607/36 nm emission filter. Data was processed using ImageJ (https://imagej.nih.gov/ij/) and compiled using Adobe Illustrator CS6.

### Image quantification

The immunofluorescence colocalisation of GFP-SNX5 with chlamydial inclusion membranes (Figure 6A; Figure 6—figure supplement 1A) imaged on a confocal microscope was measured by Mander’s correlation coefficient of red pixel (EEA1 or mCherry-Rab25) over green pixel (GFP-SNX5) signals, which were determined using ImageJ (https://imagej.nih.gov/ij/) with the JACoP plugin (Bolte and Cordelières, 2006). Punctate structures were automatically counted using ImageJ analyse particle tool across total of 10 cells from two biological replicates. To quantify the effect of PI3K inhibitors on SNX recruitment (Figure 1—figure supplement 2), Z-stacks were captured with a Zeiss 710 confocal laser scanning microscope using a 40x objective. Maximum projections were generated with FIJI (https://fiji.sc/) and Pearson’s correlation coefficients for individual cells determined using the FIJI ‘Coloc 2’ function with Costes threshold regression and 100 Costes randomisations. Co-localization analyses were conducted on two independent experiments from five images per condition each containing at least 20 cells (>100 cells analysed per condition).

### Co-precipitation of GFP-SNX5 and endogenous SNX1

HeLa cells were transfected with pcDNA3.1-N-eGFP plasmid constructs overnight at 70% confluence and the cells were lysed using lysis buffer (H2O, 50 mM HEPES, 150 mM NaCl, 1% Triton-X100, 10 mM Na4P2O7, 30 mM NaF, 2 mM Na3VO4, 10 mM EDTA, 0.5 mM AEBSF and protease inhibitor cocktail). Cell lysates were incubated with GFP nano-trap agarose beads (Protein Expression Facility, UQ) after preclear using protein G-agarose beads (Invitrogen). Protein complexes attached to the beads were detached by boiling for 5 min with 5x denaturing and reducing buffer (0.625 M Tris pH 6.8, 50% glycerol, 10% SDS, 0.25% Bromophenol blue and 500 mM DTT). Denatured and reduced proteins were separated by molecular mass using SDS-PAGE. Proteins were transferred onto PVDF-FL membrane (Immobilon) and were detected by immunoblotting with polyclonal anti-GFP and monoclonal SNX1 antibodies, and near-infrared fluorescent dyes (LI-COR). Immunolabelled proteins were visualised using LI-COR Odyssey imaging system.

### Modelling of the SNX5-SNX1 heterodimer

Human SNX5 and SNX1 sequences were submitted to the PHYRE2 server for automated homology-based model building (Kelley et al., 2015). For both proteins the top scoring modelling template was the crystal structure of the SNX9 PX-BAR domains (PDB ID 2RAJ) (Pylypenko et al., 2007) with Confidence Scores of 100% (and sequence identities of 19% and 16% respectively). The PX domain of the SNX5 model generated using this structural template was missing the extended α-helical insert, so to complete the model the SNX5 PX domain-IncE complex was substituted and a dimer of SNX5 and SNX1 PX-BAR domains generated by overlaying with the SNX9 dimer in the PtdIns3P-bound state (PDB ID 2RAK) (Pylypenko et al., 2007). The resulting model was subjected to simple energy minimisation in PHENIX (Adams et al., 2011). Conservation of surface residues was computed using the CONSURF server (Ashkenazy et al., 2016).

### Data deposition

Structural data are deposited in the protein data bank (PDB) under accession numbers 5TGI, 5TGJ, and 5TGH. Raw diffraction images are available on the University of Queensland eSPACE server (http://espace.library.uq.edu.au/view/UQ:409277).
