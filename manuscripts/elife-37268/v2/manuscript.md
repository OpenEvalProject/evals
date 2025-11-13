# Tuning site-specific dynamics to drive allosteric activation in a pneumococcal zinc uptake regulator

## Authors

- Daiana A Capdevila<sup>1</sup> ([ORCID: 0000-0002-0500-1016](https://orcid.org/0000-0002-0500-1016))
- Fidel Huerta<sup>1</sup>
- Katherine A Edmonds<sup>1</sup>
- My Tra Le<sup>1</sup>
- Hongwei Wu<sup>1</sup>
- David P Giedroc<sup>1</sup> ([ORCID: 0000-0002-2342-1620](https://orcid.org/0000-0002-2342-1620)) †

### Affiliations

1. Department of Chemistry Indiana University Bloomington United States
2. Graduate Program in Biochemistry Indiana University Bloomington United States
3. Department of Molecular and Cellular Biochemistry Indiana University Bloomington United States

† Corresponding author

## Abstract

MarR (multiple antibiotic resistance repressor) family proteins are bacterial repressors that regulate transcription in response to a wide range of chemical signals. Although specific features of MarR family function have been described, the role of atomic motions in MarRs remains unexplored thus limiting insights into the evolution of allostery in this ubiquitous family of repressors. Here, we provide the first experimental evidence that internal dynamics play a crucial functional role in MarR proteins. Streptococcus pneumoniae AdcR (adhesin-competence repressor) regulates ZnII homeostasis and ZnII functions as an allosteric activator of DNA binding. ZnII coordination triggers a transition from somewhat independent domains to a more compact structure. We identify residues that impact allosteric activation on the basis of ZnII-induced perturbations of atomic motions over a wide range of timescales. These findings appear to reconcile the distinct allosteric mechanisms proposed for other MarRs and highlight the importance of conformational dynamics in biological regulation.

## Introduction

Successful bacterial pathogens respond to diverse environmental insults or changes in intracellular metabolism by modulating gene expression (Alekshun and Levy, 2007). Such changes in gene expression are often mediated by ‘one-component’ transcriptional regulators, which directly sense chemical signals and convert such signals into changes in transcription. Members of the multiple antibiotic resistance regulator (MarR) family are critical for the survival of pathogenic bacteria in hostile environments, particularly for highly antibiotic-resistant pathogens (Ellison and Miller, 2006; Yoon et al., 2009; Weatherspoon-Griffin and Wing, 2016; Tamber and Cheung, 2009; Aranda et al., 2009; Grove, 2017). Chemical signals sensed by MarRs include small molecule metabolites (Deochand and Grove, 2017), reactive oxygen species (ROS) (Liu et al., 2017; Sun et al., 2012) and possibly reactive sulfur species (RSS) (Peng et al., 2017). It has been proposed that evolution of new MarR proteins enables microorganisms to colonize new niches (Deochand and Grove, 2017), since species characterized by large genomes and a complex lifestyle encode many, and obligate parasitic species with reduced genome sizes encode few (Pérez-Rueda et al., 2004). Therefore, elucidating how new inducer specificities and responses have evolved in this ubiquitous family of proteins on what is essentially an unchanging molecule scaffold is of great interest, as is the molecular mechanism by which inducer binding or cysteine thiol modification allosterically regulates DNA operator binding in promoter regions of regulated genes.

Obtaining an understanding of how allostery has evolved in one-component regulatory systems (Ulrich et al., 2005; Marijuán et al., 2010), including MarR family repressors, requires a comprehensive analysis of the structural and dynamical changes that occur upon inducer and DNA binding (Capdevila et al., 2017a; Tzeng and Kalodimos, 2013; West et al., 2012; Tzeng and Kalodimos, 2009; Capdevila et al., 2018). For MarRs, several distinct allosteric mechanisms have been proposed, from a ‘domino-like’ response (Bordelon et al., 2006; Gupta and Grove, 2014; Perera and Grove, 2010) to ligand binding-mediated effects on asymmetry within the dimer (Anandapadamanaban et al., 2016), to oxidative crosslinking of E. coli MarR dimers into DNA binding-incompetent tetramers (Hao et al., 2014). While there are more than 130 crystal structures of MarR family repressors in different allosteric states (Figure 1—figure supplement 1), an understanding of the role of atomic motions and the conformational ensemble in MarRs is nearly totally lacking and what is known is based exclusively on simulations (Anandapadamanaban et al., 2016; Sun et al., 2012). Here, we provide the first experimental evidence in solution that internal dynamics play a crucial functional role in a MarR protein, thus define characteristics that may have impacted the evolution of new biological outputs in this functionally diverse family of regulators.

In the conventional regulatory paradigm, the binding of a small molecule ligand, or the oxidation of conserved ROS-sensing cysteines, induces a structural change in the homodimer that typically negatively impacts DNA binding affinity. This results in a weakening or dissociation of the protein-DNA complex and transcriptional derepression. Several reports provide evidence for a rigid body reorientation of the two α4 (or αR)-reading heads within the dimer (Figure 1A–B, Figure 1—figure supplement 1) (Alekshun et al., 2001; Fuangthong and Helmann, 2002; Wilke et al., 2008; Chang et al., 2010; Liu et al., 2017; Deochand and Grove, 2017; Dolan et al., 2011; Deochand et al., 2016). The generality of this simple paradigm is inconsistent with the findings that some MarR proteins share very similar static structures in the DNA binding competent and DNA binding-incompetent states (Anandapadamanaban et al., 2016; Kim et al., 2016; Liguori et al., 2016); furthermore, several DNA binding competent states have been shown to require a significant rearrangement to bind DNA (Alekshun et al., 2001; Liu et al., 2017; Zhu et al., 2017b; Hao et al., 2014; Gao et al., 2017; Chin et al., 2006; Saridakis et al., 2008). In fact, a comprehensive analysis of all available MarR family structures strongly suggests that the degree of structural reorganization required to bind DNA, characterized by a narrow distribution of α4-α4’ orientations, is comparable whether transitioning from the DNA-binding incompetent or competent states of the repressor (Figure 1C, Table 1, Figure 1—source data 1). These observations strongly implicate a conformational ensemble model of allostery (Motlagh et al., 2014) (Figure 1B–D), where inducer sensing impacts DNA binding by restricting the conformational spread of the active repressor, as was proposed in a recent molecular dynamics study (Anandapadamanaban et al., 2016).

![Figure 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig1-v2.jpg)

**Figure 1.:** The two Zn(II) ions in each protomer are represented by spheres, and coordinating ligands are shown in stick representation. The DNA binding helices are shaded red. (B) Simplified free energy diagram showing the DNA binding competent (green) and DNA binding incompetent (blue) states with the relative population of two distinct conformations: compatible with DNA binding (red rectangle, α4-α4’ distance between DNA binding helices, ≈30 Å) and incompatible with DNA binding (larger α4-α4’ distances). In this free energy diagram, the DNA binding-incompetent state has a comparatively higher population of the conformation incompatible with DNA binding relative to the DNA binding-competent state. (C) The α4-α4’ distance distribution plotted against the DNA-binding inter-helical α4-α4’ orientation distribution for all the reported MarR crystal structures (see Table 1 and Figure 1—source data 1 for details) in the allosterically DNA binding competent conformation (green), a DNA binding incompetent conformation (blue) and in the DNA-bound (red) conformation. Filled circles represent states that have been assigned based on DNA binding data, while for the hollow circles the DNA binding properties were assigned taking into account the conformational state in the crystal structure (i.e., reduced, ligand bound) and the degree of sequence similarity to other MarR repressors. The structures for ZitR and AdcR have been highlighted with a white star. The inferred conformational space occupied by the DNA-bound conformation in all MarR regulators (Table 1) is shaded in red oval. Ribbon representations of the molecules in each conformation are shown in the inset, as well as a scheme of how the distances and angles were measured. (D) Histogram plot of the α4-α4’ distance (see panel C) extracted from 136 different crystal structures of MarR repressors in the DNA binding incompetent, DNA binding competent and DNA-bound conformations.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Structural comparison (global superposition) between AdcR (3tgn, shaded slate in all panels. (Guerra et al., 2011) and L. lactis ZitR (Zhu et al., 2017a) in the different allosteric states (DNA-bound PDB codes, 5yi2, 5yi3; ZnII2-bound, 5hyx; Apo-state, 5yi1; Zn1-bound PDB ID 5yhy, 5yl0; ZnII2-bound alternative state with a MES molecule in Zn site 1, 5yhz; Zn2-bound from Group A Streptococcus pyogenes AdcR (Sanson et al., 2015) with flexible loop, 5jls, 5lju). (B) Structural comparisons of various MarR family repressors in the DNA-bound states. (B. subtilis OhrR, PDB code, 1z9c; S. enterica SlyA, 3q5f; S. aureus MepR, 4lln; S. epidermis AbfR, 5hlg; M. tuberculosis Rv2887, 5hso; L. Lactis ZitR, 5yi2.

**Table 1.**
 Interprotomer distances between the Cα of the N-terminal residue in the α4 and α4’ helices for representatives MarR proteins


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">DNA-bound state</th>
      <th colspan="2">DNA binding incompetent statea,*</th>
      <th colspan="2">DNA binding competent stateb*</th>
    </tr>
    <tr>
      <th>MarR</th>
      <th>Distance (Å)</th>
      <th>Pdb id</th>
      <th>Distance (Å)</th>
      <th>Pdb id</th>
      <th>Distance (Å)</th>
      <th>Pdb id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ZitR (AdcR)</td>
      <td>32.3/31.7</td>
      <td>5yi2/5yi3</td>
      <td>59.6/57.3</td>
      <td>5yh0/5yh1</td>
      <td>35.5/54.0/50.2 (22.2/34/33.8)</td>
      <td>5yhx/5yhy/ 5yhz (3tgn/5jls/5 jlu)</td>
    </tr>
    <tr>
      <td>Ec MarR</td>
      <td>29</td>
      <td>5hr3</td>
      <td>12.9/12</td>
      <td>1jgs/4jba</td>
      <td>8.3/8.4</td>
      <td>3vod/3voe</td>
    </tr>
    <tr>
      <td>OhrR</td>
      <td>27.6</td>
      <td>1z9c</td>
      <td>(32.2)</td>
      <td>(2pfb)</td>
      <td>23.9 (28.9)</td>
      <td>1z91 (2pex)</td>
    </tr>
    <tr>
      <td>SlyA</td>
      <td>27.8</td>
      <td>3q5f</td>
      <td>29.4</td>
      <td>3deu</td>
      <td>15.5 (23.8, 20)</td>
      <td>3qpt (1lj9, 4mnu)</td>
    </tr>
    <tr>
      <td>AbsC</td>
      <td>26.3</td>
      <td>3zpl</td>
      <td>30.8</td>
      <td>3zmd</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>RovA</td>
      <td>21.8/21.9</td>
      <td>4aij/ 4aik</td>
      <td>-</td>
      <td>-</td>
      <td>20.9</td>
      <td>4aih</td>
    </tr>
    <tr>
      <td>MosR</td>
      <td>25.1</td>
      <td>4f×4</td>
      <td>15.1</td>
      <td>4f×0</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MepR</td>
      <td>26.4/26.9</td>
      <td>4lll/ 4lln</td>
      <td>18.9/16.9/ 30.8/57.9</td>
      <td>3eco/4l9n/ 4l9t/4l9v</td>
      <td>27.9/46.8</td>
      <td>4l9j/4ld5</td>
    </tr>
    <tr>
      <td>AbfR</td>
      <td>29.9/30</td>
      <td>5hlh/5hlg</td>
      <td>40.7</td>
      <td>5hli</td>
      <td>37</td>
      <td>4hbl</td>
    </tr>
    <tr>
      <td>Rv2887</td>
      <td>22.5</td>
      <td>5hso</td>
      <td>7.9/15.1</td>
      <td>5hsn/5hsl</td>
      <td>8.3</td>
      <td>5hsm</td>
    </tr>
    <tr>
      <td>HcaR</td>
      <td>28.6</td>
      <td>5bmz</td>
      <td>19.1/19.8/19.5/19.2</td>
      <td>4rgx/4 rgu/4rgs/ 4rgr</td>
      <td>18.7</td>
      <td>3k0l</td>
    </tr>
    <tr>
      <td>ST1710</td>
      <td>10.1c</td>
      <td>3gji</td>
      <td>23</td>
      <td>3gf2</td>
      <td>22.8</td>
      <td>2eb7</td>
    </tr>
    <tr>
      <td>TcaR</td>
      <td>19.1d</td>
      <td>4kdp</td>
      <td>22.3/24.7</td>
      <td>4eju/3kp7</td>
      <td>26.4/22.5/21.1/22/27.6/ 18.3/21.1/18.2</td>
      <td>3kp2/3kp3/3kp4/3kp5 /3kp7/4ejt/4ejv/4ejw</td>
    </tr>
  </tbody>
</table>

_aAny protein allosteric state that has been shown to bind to DNA in-vitro with an affinity higher than 107 M-1 or is capable of repressing the expression of downstream gene. bAny protein allosteric state that fails to repress these genes and/or exhibits a significantly lower DNA binding affinity from the DNA binding-competent conformation (at least 10-fold) or an affinity lower than 106 M-1 *In addition to these two categories, two other categories were classified as DNA binding-competent or DNA binding-incompetent states in Figure 1C. They refer to any protein allosteric state for which the DNA binding properties have not been determined, but the conformational state in the crystal structure is known (i.e., reduced, ligand bound). cNot inserted in the major groove of the DNA. dThis structure was co-crystallized with ssDNA. Any entry in parentheses corresponds to a structure of a homologue from a different organism (see Figure 1—source data 1)._

MarR proteins are obligate homodimers that share a winged-helical DNA-binding domain connected to a DNA-distal all-helical dimerization domain where organic molecules bind in a cleft between the two domains (Figure 1—figure supplement 1B). Individual MarR members have been shown to bind a diverse range of ligands at different sites on the dimer (Otani et al., 2016; Takano et al., 2016); likewise, oxidation-sensing cysteine residues are also widely distributed in the dimer (Fuangthong and Helmann, 2002; Liu et al., 2017; Hao et al., 2014; Dolan et al., 2011; Chen et al., 2006). This functional diversity is accompanied by relatively low overall sequence similarity, which suggests that a conserved molecular pathway that connects sensing sites and the DNA binding heads is highly improbable. Complicating our current mechanistic understanding of this family is that for many members, including E. coli MarR, the physiological inducer (if any) is unknown, rendering functional conclusions on allostery from crystallographic experiments alone less certain (Hao et al., 2014, Zhu et al., 2017b).

In contrast to the extraordinary diversity of thiol-based switching MarRs, MarR family metallosensors are confined to a single known regulator of ZnII uptake, exemplified by AdcR (adhesin competence regulator) from S. pneumoniae and closely related Streptococcus ssp. (Loo et al., 2003; Reyes-Caballero et al., 2010) and ZitR from Lactococcus spp (Llull et al., 2011; Zhu et al., 2017c). AdcR and ZitR both possess two closely spaced pseudotetrahedral ZnII binding sites termed site 1 and site 2 (Figure 1A) that bind ZnII with different affinities (Reyes-Caballero et al., 2010; Guerra et al., 2011; Sanson et al., 2015; Zhu et al., 2017c). ZnII is an allosteric activator of DNA operator binding which is primarily dependent on the structural integrity of site 1 (Reyes-Caballero et al., 2010; Zhu et al., 2017c). ZitR has been recently structurally characterized, with crystallographic models now available for the apo- and ZnII1- (bound to site 1) and ZnII2- and ZnII2-DNA operator complexes, thus providing significant new insights into ZitR and AdcR function (Zhu et al., 2017c). These structures reveal that ZnII2-ZitR and ZnII2-AdcR form triangularly-shaped homodimers and are essentially identical, as anticipated from their high sequence identity (49%). Apo-ZitR adopts a conformation that is incompatible with DNA binding, and filling of both ZnII sites is required to adopt a conformation that is similar to that of the DNA-complex. Thermodynamically, filling of the low affinity site two enhances allosteric activation of DNA-binding by ≈10-fold, and this occurs concomitant with a change in the H42 donor atom to the site 1 ZnII ion from Nε2 in the apo- and ZnII1-states to Nδ1 in the ZnII2-ZitR [as in ZnII2 AdcR; (Guerra et al., 2011) and ZnII2 ZitR-DNA operator complexes (Zhu et al., 2017c). Allosteric activation by ZnII is in strong contrast to all other members of the MarR superfamily, consistent with its biological function as uptake repressor at high intracellular ZnII.

Here we employ a combination of NMR-based techniques and small angle x-ray scattering (SAXS) to show that apo- (metal-free) AdcR in solution is characterized by multiple semi-independent domains connected by flexible linkers, resulting in a distinct quaternary structure from the Zn-bound state previously structurally characterized (Guerra et al., 2011). Our backbone relaxation dispersion-based NMR experiments show that apo-AdcR samples distinct conformational states in the µs-ms timescale, while ZnII narrows this distribution, likely increasing the population of a state that has higher affinity for DNA. This finding is consistent with the crystallographic structures of ZnII2 ZitR and the ZnII2 ZitR:DNA complex (Zhu et al., 2017c). The site-specific backbone and methyl sidechain dynamics in the sub-ns timescale show that ZnII not only induces a general restriction of these internal protein dynamics, but also subtly enhances fast timescale backbone and sidechain motions in the DNA binding domains. Together, these data suggest that ZnII coordination drives a conformational change that enhances internal dynamics uniquely within the DNA binding domain, thus poising the repressor to interact productively with various DNA operator target sequences (Reyes-Caballero et al., 2010). We demonstrate the functional importance of these dynamics by characterizing both methyl sidechain and hydrogen-bonding substitution mutants of AdcR (Capdevila et al., 2017a) in terms of function, stability and dynamical impact. Overall, our findings suggest that protein dynamics on a wide range of timescales strongly impact AdcR function. We propose an ensemble model of allostery that successfully reconciles the distinct mechanisms proposed for other MarR family repressors and suggests a mechanism of how evolution tunes dynamics and structure to render distinct biological outputs (allosteric activation vs. allosteric inhibition) on a rigorously conserved molecular scaffold.

## Results and discussion

### Solution structural differences between apo and ZnII bound forms of AdcR

Our crystal structure suggests that once AdcR is bound to both ZnII, the αR- (α4) reading heads adopt a favorable orientation for DNA binding (Guerra et al., 2011), a finding compatible with structural studies of L. lactis ZitR (Zhu et al., 2017c) (Figure 1A). These structural studies suggest a ‘pre-locked’ model, where ZnII binding to both sites 1 and 2, concomitant with a H42 ligand atom switch, locks the AdcR homodimer into a DNA binding-competent conformation. This model makes the prediction that the unligated AdcR can explore conformations structurally incompatible with DNA binding, as shown previously for ZnII1 ZitR (Zhu et al., 2017c), thus requiring a significant degree of reorganization to bind with high affinity to the DNA (Figure 1B). Despite substantial efforts, it has not yet been possible to obtain the crystal structure of apo-AdcR, suggesting that the apo-repressor may be highly flexible in solution (Guerra et al., 2011; Sanson et al., 2015). Thus, we employed SAXS as a means to explore the apo-AdcR structure and elucidate the structural changes induced by ZnII binding and conformational switching within the AdcR homodimer.

We first examined the behavior of apo- and ZnII-bound states. Both states show Guinier plots indicative of monodispersity and similar radii of gyration (Rg). These data reveal that each state is readily distinguished from the other in the raw scattering profiles (to q = 0.5 Å−1) (Figure 2A)as well as in the PDDF plots (p(r) versus r), with the experimental scattering curve of the ZnII bound state being more consistent than the unligated state with the one obtained from the ZnII2 AdcR crystal structure (Figure 2A, inset). Moreover, a qualitative analysis of the PDDF plots suggests that apo-AdcR is less compact than the ZnII-bound state (Figure 2—figure supplement 1). The molecular scattering envelopes calculated as bead models with the ab initio program DAMMIF for apo-AdcR suggest that the differences between the apo and ZnII AdcR SAXS profiles can be explained on the basis of a reorientation of the winged helix-turn-helix motif with respect to the dimerization domain, particularly in a distortion in the α5 helix (Figure 2B). The models obtained confirm that the Zn-bound structure in solution resembles the crystallographic models of apo-ZitR and ZnII AdcR (Guerra et al., 2011; Zhu et al., 2017c) (Figure 2C); however, we note that the SAXS profile of the apo-AdcR differs significantly from the ZitR crystal structure (Figure 2—figure supplement 1D) which is likely related to the high flexibility of this conformational state in solution. Moreover, the resolution of SAXS based models cannot be used to obtain residue-specific information about structural perturbations introduced by ZnII binding (Figure 2—figure supplement 1). Thus, we turned to NMR-based techniques to provide both high resolution and site-specific information on this highly dynamic system.

![Figure 2.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig2-v2.jpg)

**Figure 2.:** Insets present the residual intensity and χ2 estimated for the calculated scattering profile of the previously published AdcR-Zn2 structure (PDB: 3tgn) in comparison with the scattering profiles of AdcR of apo and Zn2-states (Guerra et al., 2011). Best-fit DAMMIF ab initio model (Franke and Svergun, 2009) for apo- (B) (blue) and ZnII2-states (C) (green), aligned with the ribbon representation of the ZnII2 structure (Figure 1A, PDB: 3tgn). The corresponding Guinier, Kratky and pairwise distribution histogram plots are shown in Figure 2—figure supplement 1, along with the fitting parameters.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) The Guinier region with linear fit of the scattering curve of the apo AdcR state (red) and Zn-binding state (black). Radius of gyration (Rg) of each state is presented at the low left corner. Note that scattering intensity is in arbitrary units. The linear fit of Guinier region is shown with its calculated R value. (B) Kratky plot of apo AdcR (red) and Zn-binding (black) state, normalized with I(0). (C) Pair distance distribution function (PDDF) of apo AdcR (red) and Zn-AdcR (black) states. The end-to-end distance (Dmax) of apo state is 65 Å and Dmax of the Zn-binding state is 75 Å. Rg of each state obtained from PDDF is also presented. (D) calculated scattering profiles of crystal structures of apo ZitRC30AH42A (5yi1), Zn1-bound ZitRE41A (5yhz) (Zhu et al., 2017a) and Zn-binding state of AdcR (3tgn) compared to the experimental scattering profile of apo-AdcR.

TROSY NMR on the 100% deuterated AdcR homodimer (32 kDa) and optimized buffer conditions for both states (pH 5.5, 50 mM NaCl, 35°C) enabled us to obtain complete backbone assignments for ZnII2-AdcR and nearly complete assignments for apo-AdcR (missing residues 21, 38 – 40 due to exchange broadening) (Figure 3—figure supplement 1). The chemical shift perturbation maps (Figure 3A–B) reveal that the largest perturbations are found in the immediate vicinity of the metal site region, that is the α1-α2 loop (residues 21 – 35), the remainder of the α2 helix (residues 41 – 47), and the central region of the α5 helix, which provides donor groups to both site 1 (H108, H112) and site 2 (E107) ZnII. These changes derive partially from changes in secondary structure, such as the extension of the α1 helix and partial unfolding of the α2 helix (Figure 3—figure supplement 1), as well as from proximity to the ZnII.

![Figure 3.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig3-v2.jpg)

**Figure 3.:** (A) Backbone CSPs. CSPs of the sterospecifically assigned methyl groups at pH 5.5, 50 mM NaCl, 35°C. (B) Both these CSPs are painted on the ribbon representation of the structure of ZnII2 AdcR. The shaded bar in each case represents one standard deviation from the mean perturbation. Site 1 and site 2 ligands in the primary structure in panel A are denoted by the yellow and green circles, respectively; the asterisks at residue positions 21 and 38 – 40 indicate no assignment in the apo-state (see materials and methods), while asterisks mark residue positions 103 and 128 for prolines. Insets show the CSP values painted onto the 3tgn structure.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Sequential residue-specific connectivities that link the chemical shifts of the 13Cα resonances in the α5 helix (E107-L116; H108, H112 ZnII ligands in bold) from an HNCA experiment. (B) (C) 1H,15N NOESY-HSQC strips obtained from the same region of the α5 helix in the apo- (B) and ZnII2 (C) states. Right, TALOS +predictions in the apo- (top) and ZnII2 (bottom) states. Despite fully α-helical predictions, the apo-state is characterized by weaker i, i + 2 NH-NH correlations, and stronger NOEs (as solvent exchange crosspeaks) to water, relative to the ZnII state. This is consistent with a more highly dynamic α5 helix in the apo-state.

The changes in Cα and Cβ chemical shifts in the central region of the α5 helix and the presence of strong NOEs to water for these residues are consistent with a kink in this helix in the apo-state (Figure 3—figure supplement 2A–B), as is commonly found in other structurally characterized MarR repressors in DNA-binding incompetent conformations (Zhu et al., 2017b; Duval et al., 2013). However, the kink is expected to be local and transient, since a TALOS+ analysis of chemical shifts predicts that the α5 helix remains the most probable secondary structure for all tripeptides containing these residues in the apo-state (Shen et al., 2009) (Figure 3—figure supplement 2C). The backbone changes in chemical shifts are accompanied by changes in the hydrophobic cores in the proximity of ZnII binding as reported by the stereospecific sidechain methyl group chemical shift perturbation maps (Figure 3B). Comparatively smaller perturbations extend to the α1 helix and the C-terminal region of the α6 helix, DNA-binding α4 helix (S74) and into the β-wing itself, consistent with a significant change in quaternary structure within the AdcR homodimer upon binding of both allosteric metal ions (Figure 3A–B).

Overall, our NMR and SAXS data show that the main structural differences between the apo- and ZnII2 states are localized in the region immediately surrounding the ZnII coordination sites, giving rise to a change in quaternary structure, while conserving the size and the overall secondary structure of the molecule. In particular, our data point to a kink in the α5 helix and a structural perturbation in the α1-α2 loop, which could be inducing a reorientation of the winged helix-turn-helix motifs relative to the dimerization domain. In addition to these structural changes, metal binding seems to be restricting the α1-α2 loop dynamics by means of metal coordination bonds, a hydrogen-bond network (Chakravorty et al., 2013) and other intermolecular contacts within the dimerization and DNA binding domains (Zhu et al., 2017c). Flexibility of the α1-α2 loop could potentially destabilize the DNA complex; in this case, interactions formed as a result of ZnII coordination may be important in allosteric activation of DNA binding. Such a dynamical model contrasts sharply with a rigid body mechanism as previously suggested for other MarRs (Alekshun et al., 2001; Chang et al., 2010; Dolan et al., 2011; Saridakis et al., 2008; Birukou et al., 2014; Radhakrishnan et al., 2014), thus motivating efforts to understand how conformational dynamics impacts biological regulation by ZnII in AdcR.

### ZnII-induced changes in AdcR conformational plasticity along the backbone

We therefore turned to an investigation of protein dynamics in AdcR. 15N R1, R2, and steady-state heteronuclear 15N{1H} NOEs provide information on internal mobility along the backbone, as well as on the overall rotational dynamics (Figure 4A–D; Figure 4—figure supplements 1–2). The R1 and R2 data reveal that ZnII2 AdcR tumbles predominantly as a single globular unit in solution with a rotational diffusion tensor and 15N R2/R1 ratio compatible with those parameters predicted from the crystal structure (Guerra et al., 2011) using hydroNMR (García de la Torre et al., 2000) (Figure 4B; Figure 4—figure supplement 1). The β-wing region tumbles independently from the rest of the molecule (Figure 4B, Figure 4—figure supplement 1B). These data also reveal that the α1-α2 linker region that donates the E24 ligand to ZnII binding site one is ordered to an extent similar to the rest of the molecule (Figure 4—figure supplement 1B). In striking contrast, in apo-AdcR, the dimerization and DNA-binding domains each have a significantly smaller 15N R2/R1 ratio (Figure 4B), somewhat closer to what is expected if these domains tumble independently of one another in solution, which might be facilitated by a highly dynamic α1-α2 loop (see also Figure 4—figure supplement 1). These findings are consistent with the SAXS data, which show that apo-AdcR is less compact than the ZnII2 state. As in the ZnII2 state, the β−wing tumbles independently of the rest of the molecule, revealing that a change in the flexibility or orientation of the β−hairpin is likely not part of the allosteric mechanism, contrary to what has been proposed for other MarRs on the basis of crystal structures alone (Liu et al., 2017; Deochand and Grove, 2017; Kim et al., 2016). Overall, the 15N relaxation data for backbone amides suggest that ZnII binding leads to a reduction of mobility of the α1-α2 loop, which in turn, decreases the dynamical independence the DNA-binding and dimerization domains, thereby stabilizing a conformation that tumbles in solution as a single globular unit.

![Figure 4.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig4-v2.jpg)

**Figure 4.:** Backbone 1H-15N amide R2/R1 for apo- (A) and ZnII2 AdcR (B) painted onto the 3tgn structure (Guerra et al., 2011). Heteronuclear NOE analysis of apo- (C) and ZnII2 (D) AdcR with the values of the 15N-{1H}-NOE (hNOE) painted onto the 3tgn structure. Values of Rex determined from HSQC 15N-1H CPMG relaxation dispersion experiments at a field of 600 MHz for the apo- (E) and ZnII2 (F) AdcRs (see Figure 4—figure supplement 3 for complete data sets). Similar results were obtained at 800 MHz. ZnII ions are shown as black spheres and residues excluded due to overlap are shown in gray. The width of the ribbon reflects the value represented in the color bar.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Experimental values of relaxation times and associated uncertainties for WT AdcR in apo-state (left, blue), ZnII2-bound state (middle, green) and overlay of both allosteric states (right) at 800 MHz with respect to the protein sequence from top to bottom: T1, T2, T1/T2 and hNOE. The position of the secondary structure elements is shown above the top panel. The grey line in the T1, T2, T1/T2 panels represent the predicted values obtained from hydroNMR for the ZnII2-AdcR crystal structure (3tgn). (B) Average backbone amide 1H-15N relaxation parameters R2/R1 for the apo- (blue boxes) and ZnII2- (green boxes) states of the AdcR homodimer in different regions of the molecule: DimD, dimerization domain (residues 5 – 20, 101 – 144); Zn-loop (α1-α2 loop, residues 21 – 37); DBD, DNA binding domain (residues 38 – 101, excluding the β-wing; β-wing (residues 81 – 101). The dashed line around 68 represent the average value predicted from hydroNMR for the ZnII2-AdcR crystal structure, while the dashed line at three represent the value obtained from the DNA binding domain on its own. Cartoon representations of the data shown in panel (B) in which the two linkers that connect the two domains (middle of the α5-helix, dark coil; α1-α2 loop, light pencil) are more dynamic in the apo-state. Note that residues analogous to the α1-α2 loop in AdcR are not observed in the crystal structure of the apo-state of L. lactis ZitR (Zhu et al., 2017b) (see Figure 1—figure supplement 1A), consistent with these findings in solution in apo-AdcR.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** These parameters assume an anisotropic rotational diffusion tensor: (top, left) amide order parameter, S2, (top, right) internal correlation time, (bottom, left) phenomenological chemical exchange contribution, (bottom, right) error function for the corresponding model determined for each residue.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Representative raw relaxation dispersion curves obtained for the indicated backbone (NH) used to obtain Rex at 600 MHz and 800 MHz. Rex for both allosteric states are shown for data acquired at 600 and 800 MHz, as indicated. All the residues excluded due to overlap are shown with an asterisk (Backbone Apo: 5, 7, 16, 18, 19, 22, 48, 50, 51, 58, 64, 68, 70, 73, 75, 78, 95, 100, 105, 106, 110, 113, 114, 115, 121, 125, 130, 135, 138, 145; Backbone Zn-bound: 12, 18, 19, 29, 40, 41, 51, 61, 86, 92, 134, 135, 137, 141, as are the unassigned residues 21,37–40 for apo and the prolines 103,128 for both states). Other residues are omitted due to poor overall fit, as indicated by χ2, shown in the bottom panel. Error bars show error of the fit for Rex.

To further probe this reduction of flexibility upon ZnII binding, we investigated sub-nanosecond backbone mobility as reported by the steady-state heteronuclear 15N{1H} NOEs (Figure 4C–D, Figure 4—figure supplement 1, Figure 4—figure supplement 2) and millisecond mobility as reported by 15N relaxation dispersion experiments (Figure 4E–F, Figure 4—figure supplement 3). These hNOE data confirm that the internal mobility of the apo-state on this timescale largely localizes to the β−wing, the α1-α2 loop, and the central region of the α5 helix, around E107 (ZnII site 2 ligand) and H108 and H112 (ZnII site 1 ligands) (Figure 4C, Figure 4—figure supplement 1). This short-timescale flexibility in these regions is significantly restricted upon ZnII binding, but somewhat paradoxically leads to a small increase in sub-nanosecond backbone motion in the DNA-binding domain (Figure 4C–D, inset), particularly in the α2 helix, the α3 helix and the N-terminal region of the α4 helix, the latter of which harbors the key DNA-binding determinants (Figure 1—figure supplement 1A) (Zhu et al., 2017c). The ZnII- induced quenching of sub-nanosecond mobility is also accompanied by an increase in mobility on the µs-ms (slow) timescale in the metal binding site, particularly at or near metal binding residues, including H112 (site 1) and C30 (site 2) (Figure 4F). In addition, the slow timescale backbone dynamics show a restriction of a conformational sampling in a band across the middle of the dimerization domain, including the upper region of the α5 helix, the N-terminus of α1, and the C-terminus of α6 (Figure 4E–F). These slow motions in the apo-state likely report on a global breathing mode of the homodimer reflective of the conformational ensemble, which is substantially restricted upon ZnII binding.

These large differences in structure and dynamics between the apo and ZnII2 AdcRs along the backbone suggest an allosteric mechanism that relies on a redistribution of internal mobility in both fast- and slow timescales, rather than one described by a rigid body motion. This mobility redistribution effectively locks AdcR in a triangular shape compatible with DNA binding, while also inducing a small, but measurable increase in motional disorder in the DNA binding domain (Figure 4C–D). Since other studies connect changes in motional disorder like these to sequence recognition and high affinity binding to DNA, particularly in the side chains (Capdevila et al., 2017a; Kalodimos et al., 2004; Anderson et al., 2013), we decided to probe side chain dynamics in greater detail.

### ZnII-induced perturbations of side chain conformational disorder in AdcR

Sub-nanosecond timescale dynamics have been used as a proxy for the underlying thermodynamics of ligand binding and can report on the role of conformational entropy (∆Sconf) in allosteric mechanisms (Caro et al., 2017; Frederick et al., 2007; Sharp et al., 2015) The contribution of changes in backbone dynamics to the ∆Sconf of ligand binding processes measured in a number of model systems has been shown to be small (<5%), relative to the contribution to ∆Sconf from the side chains (Caro et al., 2017). However, in the case of AdcR, ZnII binding clearly restricts the backbone dynamics of the α1-α2 loop as reflected by an increase in the N-H order parameters in this region (S2bb, Figure 4—figure supplement 2), which sums to –T∆Sconf, bb to ≈3.5 kcal mol−1 (see materials and methods). Thus, α1-α2 loop restriction to the internal dynamics may well be a significant contributor to the underlying thermodynamics of metal binding. Moreover, if this motional redistribution along the backbone is accompanied by changes in the internal dynamics of the side chains, particularly those in the DNA binding domain, these fast internal dynamics could greatly impact the entropy of metal binding and/or allostery. Mapping these perturbations by measuring the change in methyl group order parameter (ΔS2axis) upon ZnII binding, employed as dynamical proxy (Capdevila et al., 2017a; Caro et al., 2017) may in turn, pinpoint residues with functional roles, that is allosteric hotspots (Capdevila et al., 2017a; Capdevila et al., 2018).

We measured the axial order parameter, S2axis, for all 82 methyl groups, comparing the apo- and Zn-bound states of AdcR (Figure 5—figure supplement 1). These dynamics changes are overall consistent with the stiffening observed along the protein backbone, for example in the α1-α2 loop; L26, in particular, is strongly impacted, changing motional regimes, |∆S2axis|>0.2 (Frederick et al., 2007) (Figure 5A). We observe a significant redistribution of sidechain mobility throughout the molecular scaffold (23 probes change motional regimes), as has been previously shown for other transcriptional regulators (Capdevila et al., 2017a; Tzeng and Kalodimos, 2012), summing to a small net decrease in conformational entropy upon ZnII coordination, –T∆Sconf,sc = 1.1 ± 0.2 kcal mol−1 (Figure 5B). Note that this value is quantitatively less than that attributed to the backbone of the α1-α2 loop. However, many of the methyl groups that change motional regimes are located in the DNA binding domain (Figure 5A–B, Figure 5—figure supplement 2). In particular, the side chain flexibility of many residues in the α3 helix increases, including L47, L57, L61, while a small hydrophobic core in the C-terminus of the α4 helix stiffens significantly, for example L81, V34. These changes are accompanied by perturbations in the dynamics at the dimer interface, that is L4, I16, V142, in both motional regimes as reported by ∆S2axis and ∆Rex (in the µs-ms timescale), the latter derived from relaxation dispersion experiments (Supplementary file 1-Table S1; Figure 5—figure supplement 3).

![Figure 5.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig5-v2.jpg)

**Figure 5.:** (A) Difference in axial order parameter (∆S2axis = S2axisZn–S2axisapo) between apo- and ZnII2-states, with the specific type of methyl group color-coded as indicated: Cβ, Ala; Cε, Met; Cγ1, Cγ2, Val; Cδ1, Cδ2, Leu. The dark shaded region shows no significant difference between apo- and Zn-II2-bound states and the lighter shaded region represents the cutoff for ‘dynamically active’ residues. S2axis (B) and Rex (C) plotted as ∆S2axis (S2axisZn – S2axisapo) and ∆Rex (RexZn – Rexapo) values, respectively, mapped onto the structure of ZnII2 AdcR (3tgn). A ∆S2axis <0 indicates that the methyl group becomes more dynamic in the ZnII2-bound state, while ∆Rex <0 indicates quenching of motion on the µs-ms timescale in the in the ZnII2-bound state. See Figure 5—figure supplements 1 and 2 for a graphical representation of all S2axis and Rex values in each conformation from which these differences were determined, respectively. Residues harboring methyl groups that show major dynamical perturbations on ZnII binding are highlighted, with selected residues subjected to methyl substitution mutagenesis (Figure 6).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Stereospecific methyl group axial order parameters, S2axis, for apo-(A) and ZnII2- (B) AdcRs as measured at 600 MHz (similar results were obtained at 800 MHz; data not shown). Errors in S2axis were obtained by Monte Carlo simulation where a Gaussian-distributed random number generator was used to generate simulated datasets by generating random values for the ratios at each delay value according to a distribution dictated by the error propagated from spectral noise (Source code 1).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Absolute values, and (B) Histogram plot of S2axis from fitting the apo (top) and ZnII2 (bottom) states in panel (A) calculated according to (Marlow et al., 2010).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Representative raw relaxation dispersion curves obtained for the indicated methyl group used to obtain Rex at 600 MHz and 800 MHz (A). Rex for both allosteric states at 600 and 800 MHz are shown in panels below. All the residues excluded due to overlap are shown with an asterisk (sidechain apo: L4-δ2, L46-δ2, L52-δ2, L97-δ2, L100-δ2, L116-δ2, L117-δ2; sidechain Zn-bound: L12-δ2, L17-δ1,L57-δ1, L75-δ1, L75-δ2, L81-δ2, L97-δ1, L117-δ1, L117-δ2, L141-δ2). V142-γ2 is also marked with an asterisk and used with caution for apo at 800 MHz due to poor overall fit, as indicated by χ2, shown in the bottom panel. Error bars for Rex show error of the fit for Rex. Panel B shows the Rex values for the apo and Zn-bound states plotted on the 3tgn structure.

### On-pathway and off-pathway allosterically impaired mutants of AdcR

Our previous work (Capdevila et al., 2017a) makes the prediction that ‘dynamically active’ sidechains (methyl groups with |∆S2axis|>0.1 upon ZnII binding) (see Figure 5A–B) are crucial for allosteric activation of DNA binding by ZnII. To test this prediction, we prepared and characterized several mutant AdcRs in an effort to disrupt allosteric activation of DNA binding, while maintaining the structure and stability of the dimer, and high affinity ZnII binding. Since it was not clear a priori how mutations that perturb mobility distributions in one timescale or the other (sub-ns or µs-ms) would impact function, we focused on two kinds of substitution mutants: methyl group substitution mutants of dynamically ‘active’ side chains positioned in either the DNA binding or the dimerization subdomains (Figure 6A,B) (Capdevila et al., 2017a), and substitutions in the hydrogen-bonding pathway in the Zn-state that may contribute to the rigidity of the α1-α2 loop in ZnII2-AdcR (Figure 6A) (Chakravorty et al., 2013). We measured DNA binding affinities of the apo and ZnII2-states, and calculated the allosteric coupling free energy, ∆Gc, from ∆Gc=–RTln(KZn,DNA/Kapo, DNA) (Giedroc and Arunkumar, 2007) (Figure 6C, Figure 6—figure supplement 1 and Table 2). All mutants are homodimers by size-exclusion chromatography (Figure 6—figure supplement 2) and all bind the first protomer equivalent of ZnII (to site 1) with wild-type-like affinity (Figure 6—figure supplement 3, Supplementary file 1-Table S1). Two of the sixteen mutants investigated here (L61V and V63A AdcRs) showed a significantly lower thermal stability as estimated by differential scanning fluorimetry (Figure 6—figure supplement 4, Supplementary file 1-Table S2); this prevented a quantitative analysis of their DNA and metal binding affinities and thus they were not considered further.

![Figure 6.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-v2.jpg)

**Figure 6.:** (A) Cα positions of the residues targeted for methyl substitution mutagenesis in the DNA binding domain (DBD) (red spheres) and in the dimerization domain (DIM) (blue spheres); other residues targeted for substitution in the hydrogen-bonding pathway (N38, Q40; green spheres) and zinc ligand E24 (yellow spheres) highlighted on the structure of the ZnII2 ZitR-DNA operator complex (Zhu et al., 2017c); ZnII ions (black spheres). (B) Zoom of the DNA binding domain (DBD) of one of the two ZnII2-bound AdcR protomers highlighting the residues targeted for mutagenesis (methyl substitution mutants, red stick; hydrogen-bonding pathway mutants, green stick; zinc ligand E24, yellow stick), with the helical elements (α1-α5) indicated. (C) Coupling free energy analysis for all AdcR mutants highlighted using the same color scheme as in panels A and B. DBD, DNA-binding domain; DIM, dimerization domain; H-bond, hydrogen binding mutants. KDNA for apo-AdcRs are shown in fill circles; KDNA for ZnII2 -AdcRs are shown in hollow circles. Lower horizontal line, KDNA for wild-type apo-AdcR; upper horizontal line, KDNA for wild-type ZnII2 AdcR, for reference. The trend in ∆S2axis and ∆Rex is qualitatively indicated (see Table 2). These residues are conserved to various degrees in AdcR-like repressors (Figure 6—figure supplement 5).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The continuous lines through each set of data correspond to nonlinear least squares fit to a 1:1 non-dissociable AdcR dimer binding model, with parameters compiled in Supplementary file 1-Table S1, and ∆Gc shown graphically in Figure 6C (main text). The red vertical and horizontal lines represent the AdcR monomer concentrations that correspond to 50% DNA-saturation points for the wild-type AdcR under the same solution conditions, presented as a guide only. Conditions: 10 mM Hepes, pH 7.0, 0.23 M NaCl, 1 mM TCEP (chelexed), 10 or 20 nM DNA, 25.0°C with 1.0 mM EDTA (for apo).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Lower right, calibration curve with standards (empty squares) and AdcR variants (filled squares).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** ZnII binding parameters for these and other AdcRs are compiled in Supplementary file 1-Table S1. Open symbols represent the 505 nm emission resulting from 324 nm excitation; filled symbols, 366 nm excitation; red lines represent data fit; black lines represent simulated curves corresponding to one order of magnitude lower (solid) or higher (dashed) KZn3 and KZn4. Experiments were conducted in triplicate for each AdcR variant.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** (A) Wild-type AdcR in apo- (black) and ZnII2-states (red). (b–f) wild-type AdcR in the apo state overlaid with selected mutants in the apo state. (g) Isotopically labeled wild-type AdcR overlaid with isotopically labeled V34A AdcR, both at pH 5.5. (h) V34A AdcR at pH 7.0 overlaid with isotopically labeled V34A AdcR mutants, at pH 5.5. Tm values from triplicate measurements are compiled in Supplementary file 1-Table S2.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** Amino acid sequence conservation of S. pneumoniae AdcR and candidate closely related MarR family repressors. Sequence conservation highlighting those residues targeted for mutagenesis in this work with a Cα sphere on the ZnII2 AdcR structure (Guerra et al., 2011) in the DNA binding domain (A) and the entire molecule (B). The ribbon structure shows the degree of conservation by ramping the color from white to bright red, with those residues of high conservation shaded bright red, using Protskin (Ritter et al., 2004). For reference, ZnII ligands are invariant (100% conserved). (B) Multiple sequence analysis of the 17 AdcR-like repressors used to create the sequence conservation map.

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp6-v2.jpg)

![Figure 6—figure supplement 7.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp7-v2.jpg)

**Figure 6—figure supplement 7.:** ZnII binding to WT AdcR is repeated for reference in panel (A) ZnII binding to L57M AdcR is shown in panel (B) CSPs of the mutation are shown for apo in panel (C) and ZnII2-bound AdcR in panel (D) CSPs are painted on the ribbon representation of the structure of ZnII2 AdcR. The shaded bar in each case represents one standard deviation from the mean perturbation. Site 1 and site 2 ligands in the primary structure are denoted by the yellow and green circles, respectively; the asterisks at residue positions 21 and 38 – 40 indicate no assignment in the apo-state, while asterisks at positions 103 and 128 denote prolines. For panels (C) and (D), the CSP of the mutated residue L57M is indicated with a cyan bar, and L57 is shown as cyan sticks on the painted cartoon.

![Figure 6—figure supplement 8.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp8-v2.jpg)

**Figure 6—figure supplement 8.:** Experimental values of relaxation times and associated uncertainties for L57M AdcR in apo-state (left, blue), ZnII2-bound state (middle, green) and overlay of both allosteric states (right) at 800 MHz with respect to the protein sequence T1/T2 (top) and hNOE (bottom). The position of the secondary structure motifs is shown above the top panel. The grey line in the T1/T2 panel represent the predicted values obtained from hydroNMR for ZnII2-AdcR crystal structure (3tgn) at 35°C, radius of atomic element of 3.2 Å and the corresponding viscosity for 10% D2O (0.7192). Apo and ZnII2-WT AdcR results are represented in blue and green lines for comparison.

![Figure 6—figure supplement 9.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp9-v2.jpg)

**Figure 6—figure supplement 9.:** The ovals highlight a region of the DNA binding domain where the L57M and WT dynamics differ from one another.

![Figure 6—figure supplement 10.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp10-v2.jpg)

**Figure 6—figure supplement 10.:** Dynamics parameters odtained with tensor2 for (A) apo- and (B) ZnII2-L57M AdcR assuming an anisotropic rotational diffusion tensor: (top, left) amide order parameter, S2, (top, right) internal correlation time, (bottom, left) phenomenological chemical exchange contribution, (bottom, right) error function for the corresponding model determined for each residue. Apo and ZnII2-WT AdcR results are represented in blue and green continuous lines for comparison.

![Figure 6—figure supplement 11.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp11-v2.jpg)

**Figure 6—figure supplement 11.:** Values of Rex determined from 15N-1H TROSY CPMG relaxation dispersion experiments at 800 MHz for the apo- and ZnII2 L57M AdcR are shown in panel A. Residues 5, 7, 15, 19, 22, 44, 56, 70, 75, 77, 86, 88, 95, 106, 115, 120, 125, 130, 135, and 145 are omitted due to resonance overlap for the apoprotein, while residues 12, 19, 20, 29, 41, 45, 58, 75, 80, 86, 87, 95, 130, 135, 137, 138, and 141 are omitted due to overlap for the Zn-bound state, as are the proline residues 103 and 128 from both charts. Residue 142 is omitted due to poor fit for the apo state, while residues 23, 33, 111, and 115 are omitted due to poor fit for the Zn-bound state, as indicated by the χ2 values. Representative relaxation dispersion curves are shown in panel B, including the reduced χ2 values indicating the quality of the fits. Note that Apo L57M is prone to significant aggregation over multiple days at 35°C and pH 5.5, thus leading to decreased signal intensities relative to reference spectra, and thus the unexpectedly high apparent R2eff values observed in these relaxation dispersion curves. Panel C shows the values of Rex painted onto the 3tgn structure, relative to the WT parameters reproduced below to facilitate comparison. The ovals expand and highlight a region of the DNA binding domain where the L57M and WT dynamics differ from one another. The L57 side chain in shown in magenta, in stick representation.

![Figure 6—figure supplement 12.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig6-figsupp12-v2.jpg)

**Figure 6—figure supplement 12.:** 2D 1H,15N TROSY spectra of apo- (left) and ZnII2 (right) states of N38A and E24D AdcRs, compared to the wild-type AdcR (black contour; single contour line shown only) acquired under the same solution conditions (50 mM NaCl, pH 6.0, 35°C).

**Table 2.**
 DNA binding parameters for wild-type AdcR and substitution mutants*


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">ZnII</th>
      <th colspan="2">Dynamic changes (ZnII) at 600 MHz</th>
      <th></th>
    </tr>
    <tr>
      <th>AdcR</th>
      <th>Kapo,DNA (x106 M−1)</th>
      <th>KZn, DNA (x106 M−1)</th>
      <th>ΔGc (kcal mol−1)</th>
      <th>ΔS2axis</th>
      <th>ΔRex</th>
      <th>Fractional ASA†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wild-type</td>
      <td>0.5 ± 0.2</td>
      <td>450 ± 220</td>
      <td>–4.0 ± 0.6</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>I104A</td>
      <td>0.20 ± 0.01</td>
      <td>280 ± 30</td>
      <td>–4.3 ± 0.4</td>
      <td>−0.08 ± 0.01</td>
      <td>−0.3 ± 0.6</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>L36A</td>
      <td>0.07 ± 0.01</td>
      <td>80 ± 30</td>
      <td>–4.1 ± 0.4</td>
      <td>0.13 ± 0.10</td>
      <td>−2.0 ± 0.5</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>V34A</td>
      <td>0.37 ± 0.17</td>
      <td>13 ± 1</td>
      <td>–2.0 ± 0.3</td>
      <td>0.13 ± 0.02</td>
      <td>−2.0 ± 0.5</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>L81V</td>
      <td>0.16 ± 0.12</td>
      <td>12 ± 8</td>
      <td>–2.4 ± 0.6</td>
      <td>0.13 ± 0.05</td>
      <td>0.0 ± 0.5</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>L61V**</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>−0.23 ± 0.01</td>
      <td>−1.0 ± 0.5</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>L57M</td>
      <td>0.035‡ ± 0.030</td>
      <td>1 ± 0.2</td>
      <td>–2.0 ± 0.7</td>
      <td>−0.18 ± 0.02</td>
      <td>1.0 ± 0.5</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>L57V**</td>
      <td>&lt;0.05§</td>
      <td>&lt;0.05§</td>
      <td>N/A</td>
      <td>−0.18 ± 0.02</td>
      <td>1.0 ± 0.5</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>I16A</td>
      <td>1.8 ± 0.9</td>
      <td>17 ± 14</td>
      <td>–1.8 ± 0.4</td>
      <td>−0.08 ± 0.02</td>
      <td>−4.0 ± 1.0</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>L4A</td>
      <td>0.5 ± 0.2</td>
      <td>11 ± 8</td>
      <td>–1.8 ± 0.3</td>
      <td>0.004 ± 0.045</td>
      <td>−4.0 ± 1.0</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>V142A</td>
      <td>0.41 ± 0.05</td>
      <td>4.1 ± 2.3</td>
      <td>–1.4 ± 0.2</td>
      <td>−0.09 ± 0.02</td>
      <td>−3.0 ± 1.0</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>I27A</td>
      <td>0.09 ± 0.01</td>
      <td>80 ± 3</td>
      <td>–4.0 ± 0.2</td>
      <td>0.03 ± 0.01</td>
      <td>1.2 ± 0.5</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>L17A</td>
      <td>0.22 ± 0.1</td>
      <td>219 ± 36</td>
      <td>–4.0 ± 0.2</td>
      <td>−0.10 ± 0.02</td>
      <td>0.0 ± 0.5</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>V63A**</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>0.01 ± 0.04</td>
      <td>1.0 ± 0.5</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>N38A</td>
      <td>0.05 ± 0.01</td>
      <td>19 ± 10</td>
      <td>–3.5 ± 0.7</td>
      <td>–#</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>N38A/Q40A</td>
      <td>0.10 ± 0.04</td>
      <td>2.2 ± 0.4</td>
      <td>–1.9 ± 0.2</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>E24D</td>
      <td>0.17 ± 0.04</td>
      <td>2.2 ± 1.7</td>
      <td>–1.6 ± 0.3</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_*Conditions: 10 mM Hepes, pH 7.0, 0.23 M NaCl, 1 mM TCEP (chelexed), 10 nM DNA, 25.0°C with 2.0 mM EDTA (for apo-AdcR) or 20 μM ZnCl2 (for ZnII2 AdcR) added to these reactions. See Figure 6C, for a graphical representation of these data. All ∆Gc values lower than −3.5 kcal mol-1, with the exception of N38A AdcR are statistically significantly different (p≤0.1) from the wild-type ∆Gc value.†Accessible surface area (ASA) was calculated from the ZnII2-bound AdcR (Guerra et al., 2011) using the web server for quantitative evaluation of protein structure VADAR 1.8 (vadar.wishartlab.com/)‡Upper limit on measureable Kapo,DNA under these solution conditions.§ Weaker than upper limit.#Not measurable using the NMR experiments employed here.**Significantly lower thermal stability as estimated by differential scanning fluorimetry (Supplementary file 1-Table S2) prevented a quantitative analysis of their DNA and metal binding affinities._

### DNA-binding domain mutants

The redistribution of fast time scale side-chain dynamics in the DNA binding domain is delocalized throughout the different secondary structure motifs (Figure 5A–B). Thus, we prepared several methyl substitution mutants of methyl-bearing residues in the α3 (L57, L61, V63), α4 (L81) and α5 (I104) helices, as well as two residues in the α1-α2 loop, V34 and L36. I104 and V63 are not dynamically active in AdcR (|∆S2axis|<0.1; ∆Rex <1.0); thus, these mutant are predicted to function as control substitutions. V34 and L36 are dynamically active on both timescales, which is not surprising since the α1-α2 loop folds upon ZnII binding to AdcR (vide supra) (Zhu et al., 2017c). In contrast, L57, L61 and L81 are characterized by significant perturbations in ∆S2axis only (|∆S2axis|≥0.2), with L81 stiffening and L57 and L61 methyls in the α3 helix becoming significantly more dynamic upon ZnII binding (Figure 5A, Table 2). To investigate the functional role of these residues, we chose missense substitutions (Table 2) generally designed to restrict the number of χ angles (Leu to Val or Ala; Val to Ala) and thus impact their dynamical sensitivities (Capdevila et al., 2017a; Capdevila et al., 2018); in one case (L57), we introduced multiple substitutions, with one characterized by a larger number of χ angles (Leu to Met).

As expected, I104A AdcR is characterized by a DNA binding affinity in the apo- and Zn-states just ≈2-fold lower than wild-type AdcR, returning a ∆Gc that is not statistically different from wild-type AdcR (Figure 6C). Functional characterization of all other methyl substitution mutants in the DNA binding domain results in a ≈5–10-fold decrease or greater (L57V AdcR; Table 2) in the DNA binding affinity of the apo-state (Figure 6C), with ZnII binding inducing markedly variable degrees of allosteric activation (Figure 6C). L36A, closest to the N-terminus of the α2 helix, is most like wild-type AdcR, while L81V AdcR is severely allosterically crippled, with KZn,DNA some 40-fold lower than wild-type AdcR, and ∆Gc ≈2-fold lower, from –4.0 to –2.4 kcal mol−1. L57M AdcR is even more strongly perturbed (∆Gc≈–2.0 kcal mol−1). V34A AdcR shows a comparable degree of functional perturbation, while effectively retaining binding of ZnII only to site 1, like V142A AdcR (discussed below; Supplementary file 1-Table S1). We emphasize that these methyl-bearing side chains targeted for substitution are not expected to be in direct contact with the DNA, based on solvent accessible area (Table 2) and distance from the DNA binding interface (Figure 6B, Figure 6—figure supplement 5). With the exception of L36A AdcR, the functional impact of each residue substitution correlates with the magnitude of the dynamical perturbations on that residue. This finding provides additional support for the idea that those methyl-bearing side chains in the DNA-binding domain that exhibit large changes in conformational entropy (as measured by ∆S2axis) make significant contributions to both DNA binding and allosteric activation by ZnII (Tzeng and Kalodimos, 2012; Capdevila et al., 2017a). Further characterization of the structural and dynamical impact of these substitutions is necessary to confirm that the functional impact of each is a consequence of dynamical perturbations rather than minor structural changes that would escape detection.

To evaluate the possible contributions of backbone dynamics and structural changes, we purified 15N-labelled V34A and L57M AdcRs. Unfortunately, the thermal stability of V34A AdcR at the slightly acidic pH and temperature (35°C) required to yield high quality NMR spectra proved inadequate (Supplementary file 1-Table S2, Figure 6—figure supplement 4) and it was therefore not investigated further. L57M AdcR, on the other hand, yielded excellent quality spectra in both apo and ZnII2 allosteric states, readily yielding backbone resonance assignments (Figure 6—figure supplement 6), which could be used to undertake a detailed backbone dynamics characterization. Although the structural changes upon ZnII binding are wild-type-like as reported by a chemical shift perturbation map, the impact of the mutation is not restricted to the α3 helix but also affects the α2 helix as anticipated by the crystal structure (Figure 6—figure supplement 7). While the backbone dynamics are largely indistinguishable from wild-type AdcR on both timescales (Figure 6—figure supplement 8–12), there are several small differences in the DNA-binding domain in the immediate vicinity of M57 that could contribute to the allosteric impact of the L57M mutation (Figure 6—figure supplement 8–11). By and large, however, wild-type and L57M AdcRs are rather dynamically similar along the backbone, thus implicating side chain conformational entropy redistribution as an important contributor to allostery in this system. However, it should be noted that although the structural impact of the L57M mutation is likely small and localized as suggested by the chemical shift perturbation maps (Figure 6—figure supplement 7), the effect of a small structural perturbation by M57 can not be ruled out.

### Hydrogen-bonding mutants

A candidate hydrogen-bonding pathway in AdcR (Chakravorty et al., 2013) was previously proposed to transmit the ZnII2 binding signal to the DNA binding domain. In this pathway, the Oε1 atom from the ZnII ligand E24 accepts a hydrogen bond from the carboxamide side chain of N38. N38 is the +1 residue of the α2 helix, which is then connected to the α4 helix via a hydrogen bond between the Q40 and S74 side chains; further, Q40 accepts a hydrogen bond from the γ-OH of T37 as part of a non-canonical helix N-capping interaction (Guerra et al., 2011) (Figure 6A). We expect that regardless of the impact that these interactions have on the overall energetics of ZnII binding, they are important in the restriction of fast-time scale dynamics in the α1-α2 loop. We therefore targeted residues E24 (Zn-ligand and H-bond acceptor), N38 and Q40, by characterizing two single mutants, E24D and N38A, and the double mutant, N38A/Q40A AdcR. Although all three mutants undergo conformational switching upon Zn-binding as revealed by 1H−15N TROSY spectra (Figure 6—figure supplement 12) all three exhibit ≈5 – 10-fold decreases in apo-state DNA-binding affinity (Figure 6C; Table 2). While the single mutant N38A binds ZnII to give ∆Gc of ≈–3.5 kcal mol−1, quite similar to that of wild-type AdcR, in marked contrast, N38A/Q40A AdcR is functionally perturbed, characterized by a ∆Gc of ≈–1.9 kcal mol−1 as is E24D AdcR, which targets a ZnII binding residue (Figure 6C). These perturbations provide additional evidence that this hydrogen-bonding pathway may contribute to the motional restriction of the α1-α2 loop, jointly with a redistribution of internal dynamics in the DNA binding domain. This effect can be perturbed directly by mutation of ‘dynamically active’ sidechains (L81V, L57M) or by significantly impacting the interactions that restrict the loop (N38A/Q40A).

### Dimerization domain mutants

To test the functional role of the dimerization domain in dynamical changes, we targeted four methyl-bearing residues in this domain, including L4, I16 and L17 on opposite ends of the α1 helix; V142, near the C-terminus of the α6 helix (Figure 6B) and I27 a α1-α2 loop in the proximity of V142. I16 and L17 are closer to the intervening minor groove of the DNA operator, while V142, I27 and L4 are increasingly distant from the DNA. With the exception of L17 and I27, these side chains are primarily active in slow timescale dynamics, with ZnII-binding quenching side chain mobility on the µs-ms timescale, that is, global motions, but relatively smaller changes in ∆S2axis (Figure 5B; Table 2). Methyl substitution mutants of these residues (I16A, L4A and V142A) bind DNA in the apo-state with wild-type like affinities, but each is allosterically strongly perturbed, with only ≈10 – 20-fold allosteric activation by ZnII, giving ∆Gc values of –1.4 to –1.8 kcal mol−1. On the contrary, L17A and I27A AdcR shows a wild-type-like ∆Gc, consistent with the fact that L17 and I27 are nearly dynamically silent upon Zn binding (Figure 5B).

These findings suggest that ZnII-dependent quenching of global motions far from the DNA binding domain play a significant role in allostery in this system. Our characterization of allosterically compromised mutants that affect site-specific conformational entropy (L81V, L57M) and conformational exchange (V34A, L4A, I16A) provides evidence for two classes of functional dynamics in AdcR that comprise different regions of the molecule, operating on different timescales (from sub-nanoseconds to milliseconds). Thus, we propose that a ZnII-dependent redistribution of internal dynamics quenches global, slow and fast motions in the dimer, yet detectably enhances local dynamical disorder in the DNA binding domain, which we propose can ultimately be harnessed to maximize contacts at the protein-DNA interface.

### Conclusions

Members of the multiple antibiotic resistance repressor (MarR) family of proteins comprise at least 12,000 members (Capdevila et al., 2017b), and many have been subjected to significant structural inquiry since the original discovery of the E. coli mar operon and characterization of E. coli MarR some 25 years ago (Cohen et al., 1993; Seoane and Levy, 1995). The crystallographic structure of this prototypical E. coli MarR appeared a few years later (Alekshun et al., 2001) and has inspired considerable efforts to understand the inducer specificity and mechanisms of transcriptional regulation in E. coli MarR (Hao et al., 2014) and other MarR family repressors (Grove, 2013), which collectively respond to an wide range of stimuli, including small molecules, metal ions, antibiotics and oxidative stress (Deochand and Grove, 2017). We have examined the wealth of crystallographic data available from 135 MarR family repressor structures solved in a variety of functional states, including DNA-binding competent, DNA-binding incompetent and DNA-bound states (Figure 1). This analysis of the crystal structures suggests that a conformational ensemble model of allostery must be operative in a significant number of these repressor systems, where ligand binding or thiol oxidation narrows the conformational spread and, thus, activates or inhibits DNA binding. Here, we present the first site-specific dynamics analysis of any MarR family repressor in solution, and establish that conformational dynamics on a range of timescales is a central feature of ZnII-dependent allosteric activation of DNA operator binding by the zinc uptake regulator S. pneumoniae AdcR (Reyes-Caballero et al., 2010) and closely related repressors (Zhu et al., 2017c).

We explored dynamics in the sub-nanosecond and ms timescales with residue-specific resolution, both along the backbone, as measured by N-H bond vectors, and in the methyl groups of the methyl-bearing side chains of Ala, Met, Val, Leu and Ile. These measurements, coupled with small angle x-ray scattering measurements of both conformational states, lead to a self-consistent picture of allosteric activation by ZnII in AdcR. The apo-state conformational ensemble is far broader than the ZnII2 state, and features at least partial dynamical uncoupling of the core DNA-binding and dimerization domains, facilitated by rapid motions in the α1-α2 loop and the α5 helix in the immediate vicinity of the ZnII coordinating residues. This motion is superimposed on much slower motions across the dimerization domain, far from the DNA interface, which affect both backbone amide and side chain methyl groups (Figures 4–5). ZnII binding substantially quenches both the low amplitude internal motions and global, larger amplitude movements like the ones reflected by SAXS data, with an accompanying redistribution of these dynamics into the DNA-binding domain.

As observed previously for another ZnII metalloregulatory protein (Capdevila et al., 2018), ZnII binding induces a small, net global conformational stiffening of the internal dynamics or sub-ns motions; however, in AdcR, there are significant contributions from both the backbone (in folding the α1-α2 loop) and the methyl-bearing side chains upon ZnII binding. These are superimposed on pockets of increased dynamical disorder, particularly in the α2-α3 loop along the backbone (Figure 4), and in the α3-α4 region of the DNA binding domain (Figure 5). To test the functional importance of both these fast-time scale motions in the DNA binding domain, as well as slow timescale dynamics in the dimerization domain, we exploited these side chain dynamics results (Figure 5) (Capdevila et al., 2017a) to guide our introduction of methyl substitutions of both dynamically active and dynamically silent residues (Figure 6). We generally find that methyl substitutions in the DNA binding domain are strongly deleterious for residues that are dynamically active in the fast timescale (|∆S2axis|>0.2), that is L81, L61, L57. The same is true of dynamically active slow timescale residues,that is L4, I16 and V142. These findings confirm a functional role of these pronounced changes in dynamics (Capdevila et al., 2017a; Capdevila et al., 2018) and suggest that ZnII2-bound AdcR has an optimal distribution of internal millisecond dynamics that if perturbed, leads to weakened DNA binding affinity in the allosterically active Zn-bound state.

The extent to which this dynamics-centered regulatory model characterizes other MarR family repressors in solution is of course unknown. However, the differences between the crystal structures of the DNA binding-competent and incompetent states appear sufficient to adequately describe the allosteric mechanism in only a handful of MarR repressors (Figure 1). From this perspective, it is interesting to speculate on the evolutionary origin of allosteric activation and allosteric inhibition within this simple molecular scaffold. Clearly, models that invoke only rigid body domain motions as contributing to allostery (Alekshun et al., 2001; Chang et al., 2010; Dolan et al., 2011; Saridakis et al., 2008; Birukou et al., 2014; Radhakrishnan et al., 2014) would fail to capture the evolution of allosteric activation vs. inhibition from a common progenitor repressor (Motlagh et al., 2014). Further, we have previously speculated that nature is capable of harnessing dynamics properties and entropy reservoirs to evolve new inducer specificities in another structural class of bacterial repressors (Capdevila et al., 2017a).

Here, we propose that both internal dynamics, reflected in a more favorable conformational entropy term, and structural features, reflected in a more favorable ΔH term, were originally optimized in a common progenitor MarR that was capable of transcriptionally repressing genes that became deleterious when colonizing a new environment (Deochand and Grove, 2017). Then, any set of sequence variations could allow for the emergence of both allosteric activation and inhibition. For example, introduction of a dynamic element(s), that is loops or disordered regions (Pabis et al., 2018; Campbell et al., 2016) would impact both coupled fast sub-ns motions and concerted slower motions and as a result, introduce an entropic penalty that leads to inhibition of DNA-binding. Indeed, a structural comparison and an extensive multiple sequence alignment reveals that only AdcR-like repressors harbor an α1-α2 loop larger than 10 residues (Figure 7A), and that ligand (ZnII) binding to what we now know is a highly dynamical loop element, becomes an important feature of allosteric activation of DNA binding.

![Figure 7.](https://cdn.elifesciences.org/articles/37268/elife-37268-fig7-v2.jpg)

**Figure 7.:** Proteins that are DNA binding-competent in the apo- state and DNA binding-incompetent in the ligand-bound state are colored in red, while proteins that are DNA binding-incompetent in the apo-state and DNA binding-competent in the liganded state are colored in blue (see Figure 1—source data 1 for a full accounting of these structures). A schematic representation of allosteric inhibition and activation are shown (inset), with shorter α1-α2 loops associated with allosteric inhibition of DNA binding upon ligand binding, while longer loops are associated with allosteric activation (like that for AdcR/ZitR) upon ligand binding. (B) Dynamically driven model for how conformational dynamics can be harnessed to evolve allosteric activation (upper right) vs. allosteric inhibition (lower right) in the same molecular scaffold. This model suggests that dynamic properties of the DNA binding competent states have been conserved to give rise to a more favorable conformational entropy. In the metalloregulatory MarRs (AdcR, ZitR), the inactive state shows perturbed dynamics over a range of timescales; apo-AdcR therefore exhibits low affinity for DNA. Metal ion (yellow circle) coordination quenches both local and global modes in the dimerization domain and linkers, while inducing conformational disorder in the DNA-binding domain that enhances DNA binding affinity, thus stabilizing a conformation that has high affinity for DNA and giving rise to a favorable conformational entropy. For prototypical MarRs, where the ligand (yellow star) is an allosteric inhibitor, ligand binding narrows the conformational ensemble to a DNA-binding incompetent conformation decreasing the enthalpic contribution to DNA binding.

On the other hand, allosteric inhibition could have arisen from sequence variations that define a pocket where ligand binding disrupts structural (Hong et al., 2005; Dolan et al., 2011; Quade et al., 2012; Birukou et al., 2014; Zhu et al., 2017a; Gao et al., 2017; Otani et al., 2016) and/or dynamical features (Capdevila et al., 2017a) of a DNA binding-competent conformation (Figure 7B). Although the presence of functionally important entropic reservoirs on any allosterically inhibited MarR has not yet been reported experimentally, molecular dynamics simulations show that DNA binding-impaired mutants of MexR differ from the wild-type repressor in the nature of the dynamical connection between the dimerization and DNA binding domains (Anandapadamanaban et al., 2016). This dynamical connectivity is in fact exploited by the binding the ArmR peptide, leading to DNA dissociation (Anandapadamanaban et al., 2016; Wilke et al., 2008). We propose that conformational entropy can contribute to other mechanisms of allosteric inhibition to yield a repressor that binds tightly to the operator sequence and yet has the ability to readily evolve new inducer specificities.

It is interesting to note that mutations that lead to inactivation are not necessarily part of a physical pathway with the DNA binding site (Clarke et al., 2016), since they only need to affect dynamical properties that are likely delocalized in an extended network. Notably, single point mutants in the dimerization domain of various MarR family repressors have been shown to modulate allostery and DNA binding (Anandapadamanaban et al., 2016; Deochand et al., 2016; Liguori et al., 2016; Duval et al., 2013; Alekshun and Levy, 1999; Andrésen et al., 2010), perhaps exemplified by the L4, I16 and V142 AdcR substitution mutants. In AdcR, while structural perturbations induced by ZnII binding are essentially confined to the ZnII binding pocket, dynamical perturbations extend all over the molecule, and feature many residues that are far from either ligand binding site, and are dynamically active on the sub-nanosecond and/or µs-ms timescales (Figures 4–5). Thus, a conformational entropy contribution that is inherently delocalized and easily perturbed can enable rapid optimization of new inactivation mechanisms that would allow new biological functionalities to emerge (Figure 7). These findings inspire efforts to explore the evolution of allostery in this remarkable family of transcriptional repressors, by exploiting an allosterically crippled AdcR, for example L57M AdcR, to re-evolve allostery in this system.

## Materials and methods

### AdcR mutant plasmid production

An overexpression plasmid for S. pneumoniae AdcR in a pET3a vector was obtained as previously described and was used as a template for the production of all mutant plasmids (Reyes-Caballero et al., 2010). Mutant AdcR plasmids were constructed by PCR-based site-directed mutagenesis, and verified using DNA sequencing.

### Protein production and purification

AdcR plasmids were transformed into either E. coli BL21(DE3) pLysS or Rosetta cells. E. coli cultures were either grown in LB media or M9 minimal media supplemented with 15NH4Cl as the sole nitrogen source with simple 1H,15N HSQC spectroscopy to assess the structural integrity of selected mutant proteins. Protein samples for backbone and methyl group assignments of AdcR were isotopically labeled using published procedures as described in our previous work (Capdevila et al., 2017a; Arunkumar et al., 2007), with all isotopes for NMR experiments purchased from Cambridge Isotope Laboratories. Protein expression and purification were carried out essentially as previously described (Reyes-Caballero et al., 2010). All proteins were confirmed to have <0.05 molar equivalents of Zn(II) as measured by atomic absorption spectroscopy and were dimeric by gel filtration chromatography. The AdcR protein concentration was measured using the estimated molar extinction coefficient at 280 nm of 2980 M−1 cm−1.

### Small angle x-ray scattering experiments

Small angle and wide angle x-ray scattering data of the apo and ZnII2 states of AdcR was collected at three different protein concentrations (5 mg/mL, 2.5 mg/mL and 1.25 mg/mL) in buffer 25 mM MES pH 5.5, 400 mM NaCl, 2 mM EDTA/10 μM ZnCl2, 2 mM TCEP at sector 12ID-B at the Advanced Photo Source (APS) at Argonne National Laboratory. For each protein concentration and matching background buffer, 30 images were collected and averaged using NCI-SAXS program package. The scattering profile at each concentration was manually adjusted with the scale factor to remove the effect of concentration prior to subtraction of the scattering profile of the buffer. Scattering profiles of each protein concentration were then merged for further analysis. The GUINIER region was plotted with ln (I(q)) vs q2 to check for monodispersity of the sample and to obtain I0 and the radius of gyration (Rg) within the range of qmax*Rg <1.3. The Rg values obtained for apo-AdcR and Zn(II)-bound-AdcR are 25.5 ± 0.9 Å and 23.7 ± 1.1 Å, respectively. The scattering profiles of each AdcR conformational state was then normalized with I0. The compaction of each states of AdcR was examined using the Kratky plot for q < 0.3 Å−1. Scattering profiles for apo and ZnII2 states of AdcR were then Fourier-transformed using GNOM of the ATSAS package to obtain the normalized pair-wise distance distribution graph (PDDF).

Ab initio modeling was performed using the program DAMMIF in a slow mode (Franke and Svergun, 2009). For each conformational state of AdcR, 10 models were obtained. These models were compared, aligned and averaged using the DAMSEL, DAMSUP, DAMAVER, DAMFILT, respectively, as described in the ATSAS package (http://www.embl-hamburg.de/bioSAXS). Normalized spatial discrepancy (NSD) between each pair of the models was computed. The model with the lowest NSD value was selected as the reference against which the other models were superimposed. Outliner models (two models) with an NSD above mean +2*standard deviation of NSD were removed before averaging. For refinement, the averaged envelope of the first run was used as search volume for the second round of modeling. Modeling of the envelope of apo-AdcR was restrained by enforcing P2 rotational symmetry while that ZnII2 AdcR was restrained using compact, hallow and no-penalty constraints. Scattering profiles of crystal structures were calculated using the fast x-ray scattering (FOXS) webserver (https://modbase.compbio.ucsf.edu/foxs/) (Schneidman-Duhovny et al., 2010).

### NMR spectroscopy

NMR spectra were acquired on a Varian VNMRS 600 or 800 MHz spectrometer, each equipped with a cryogenic probe, at the Indiana University METACyt Biomolecular NMR laboratory. The two-dimensional spectra were processed using NMRPipe (Delaglio et al., 1995). The three-dimensional spectra were acquired using Poisson-gap non-uniform sampling and reconstructed using hmsIST (Hyberts et al., 2012) and analyzed using Sparky (Lee et al., 2015) or CARA (http://cara.nmr.ch). Typical solution conditions were ~500 µM protein (protomer), 25 mM MES pH 5.5, 50 mM NaCl, 1 mM TCEP, 0.02% (w/v) NaN3, and 10% D2O. Some spectra were recorded at pH 6.0 as indicated. Our previous NMR studies of AdcR (Guerra et al., 2011; Guerra and Giedroc, 2014) were carried out with samples containing ≈70% random fractional deuteration, pH 6.0, 50 mM NaCl, 35°C; under those conditions, the backbone amides of residues 21 – 26 in the α1-α2 loop and harboring zinc ligand E24 as well as the N-terminal region of the α2 helix (residues 37 – 40) exhibited significant conformational exchange broadening in the apo-state and could not be assigned (Guerra et al., 2011). In this work, we acquired comprehensive 1H-15N TROSY-edited NMR data sets at 600 and 800 MHz for a 100% deuterated AdcR sample in both apo- and Zn2-bound states at pH 5.5, 50 mM NaCl, 35° C. Under these conditions, only four backbone amides residues in the apo-state were broadened beyond detection (residues 21, 38 – 40); all were visible and therefore assignable in the ZnII2 state. Thus, the N-terminus of the α2 helix, including N38 and Q40 are clearly exchange broadened in the apo-state. Sidechains were assigned following published procedures as described in our previous work (Capdevila et al., 2017a; Arunkumar et al., 2007). The Leu and Val methyl resonances were distinguished using through-bond information such as HMCMCBCA or HMCM[CG]CBCA experiments (Tugarinov and Kay, 2003) which correlate the Leu or Val methyl resonances with other side chain carbon resonances. All apo-protein samples contained 1 mM EDTA. All ZnII2 samples contained two monomer mol equiv of ZnII. Chemical shifts were referenced to 2,2-dimethyl-2-silapentane-5-sulfonic acid (DSS; Sigma) (Wishart and Sykes, 1994). Chemical shift perturbations (CSP) of the backbone and methyl groups upon ZnII binding or mutation were calculated using 1H and 15N chemical shifts of the methyl groups (Δδ=(ΔδH)2+ 0.2(ΔδN)2) and 1H and 13C chemical shifts of the methyl groups (Δδ=(ΔδH)2+ 0.3(ΔδC)2), respectively.

15N spin relaxation rates, R1 and R2, and 1H-15N heteronuclear NOE (hNOE) values were measured using TROSY pulse sequences described elsewhere (Zhu et al., 2000) on the 100% deuterated AdcR sample. The relaxation delays used were 0.01, 0.05, 0.11, 0.19, 0.31, 0.65, 1, 1.5, 1.9, 2.3, 2.7, and 3.2 s for R1 and 0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.19, and 0.25 s for R2. Residue-specific R1 and R2 values were obtained from fits of peak intensities vs. relaxation time to a single exponential decay function, while hNOE ratios were ascertained directly from intensities in experiments recorded with (2 s relaxation delay followed by 3 s saturation) and without saturation (relaxation delay of 5 s). Theoretical hNOEs values were estimated using the Solomon equation that takes into account the fact that the recycle delay is not much longer than T1 (Gong and Ishima, 2007; Freedberg et al., 2002; Lakomek et al., 2012). Errors in hNOE values were calculated by propagating the error from the signal to noise.

Values of rotational correlation times were obtained from Monte Carlo simulations with tensor2 software (Dosset et al., 2000), using T1, T2, and heteronuclear NOE (hNOE) recorded at 35°C at 800 MHz, in 10% D2O (Figure 4—figure supplement 2). A chemical shift anisotropy (CSA) angle of value of 17 degrees was used for these calculations. For apo- and ZnII2 AdcRs, the τc obtained in this way is 16.9 ± 0.1 ns and 21.1 ± 0.1 ns respectively. The results for ZnII2-AdcR were in very good agreement with the correlation time and relaxation rates obtained from HydroNMR (García de la Torre et al., 2000) for the crystal structure of ZnII2-AdcR (3tgn, τc=20 ns, Figure 4—figure supplement 1, grey lines). A value of the atomic radius element of 3.2 Å and the known viscosity for water at 35°C (Cho et al., 1999) were used for this calculation.

S2axis of the Ile δ1, Leu δ1/δ2, Val γ1/γ2, Ala β, and Met ε methyl groups in apo and Zn(II)2 states were determined using 1H spin-based relaxation experiments at 600 MHz at 35.0°C (Tugarinov et al., 2007). S2axis values, cross-correlated relaxation rates, η, between pairs of 1H–1H vectors in 13CH3 methyl groups were measured using Equation. 2

$$
η= \frac{R_{2,H}^{F}− R_{2,H}^{S}}{2} ≈ \frac{9}{10}(\frac{\mu_{o}}{4\pi})^{2}[P_{2}(cos\theta_{axis,HH})]^{2}\frac{S_{axis}^{2}\gamma_{H}^{4}ħ^{2}\tau_{c}}{r_{HH}^{6}}
$$

where τc is the tumbling time of the protein; RF2,H and RS2,H are the fast and slow relaxing magnetization, respectively; γH is the gyromagnetic ratio of the proton; and rHH is the distance between pairs of methyl protons.

In order to obtain an approximation of the differences in fast and slow relaxation rates (2η, we measured the time-dependence of the cross peak intensities in a correlated pair of single and double quantum (2Q) experiments (Tugarinov et al., 2007). Using various delay time, T, values (3, 5, 8, 12, 17, 22, and 27 ms, recorded in an interleaved manner), the rates of η were obtained by fitting ratios of peak intensities measured in pairs of experiments (Ia and Ib, spin-forbidden and spin-allowed, respectively) with Equation. 3:

$$
\frac{I_{a}}{I_{b}}=\frac{-0.5ηtanh⁡(\sqrt{η^{2}+\delta^{2}}T)}{\sqrt{η^{2}+\delta^{2}}-\deltatanh(\sqrt{η^{2}+\delta^{2}}T)}
$$

where T is the variable delay time, δ is a parameter that is related to the 1H spin density around the methyl group, and Ia and Ib are the time dependencies of differences and sums, respectively, of magnetization derived from methyl 1H single-quantum transitions, as described (Tugarinov et al., 2007). Peak heights and spectral noise were measured in Sparky (Lee et al., 2015). A python script (Source code 1) was used to fit the peak height ratios to η values and to determine S2axis values in the apo- or Zn-bound states, as described previously (Tugarinov and Kay, 2004; Tugarinov et al., 2007; Capdevila et al., 2017a). τc was obtained from Monte Carlo simulations with tensor2 software.

The conformational entropy between Zn and apo states was obtained using a methyl order parameters, S2axis, as dynamical proxy (Caro et al., 2017):

$$
-T\DeltaS_{CONF,sc,a→b}^{}=-T-0.00116kcalmol^{-1}K^{-1}N_{χ}^{prot}S_{b}^{2}-S_{a}^{2}
$$

where Nχprot is the total number of side-chain torsion angles in the protein dimer.

We also evaluated the contribution of the changes in the backbone dynamics using previously reported calibration curve for backbone entropy obtained from molecular dynamics simulations (Sharp et al., 2015):

$$
−TΔS_{conf, bb,a→b}^{}=−T (0.0017 kcalmol^{-1}K^{-1})N_{res}^{prot} [⟨ln(1−S_{NH,b}^{2})−ln(1−S_{NH,a}^{2})⟩]
$$

where Nresprot is the total number of residues in the protein dimer (292 in the case of AdcR). This calculation was performed only for residues that had $S_{NH}^{2}$<0.8 in at least one of the allosteric states.

Relaxation dispersion measurements were acquired using a TROSY adaptation of 15N and a 1H-13C HMQC-based Carr–Purcell–Meiboom–Gill (CPMG) pulse sequence for amides from the backbone (Tollinger et al., 2001) and methyl groups from the sidechains (Korzhnev et al., 2004), respectively. Experiments were performed at 35°C at 600 and 800 MHz 1H frequencies using constant time interval T = 40 ms with CPMG field strengths (νCPMG) of 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 850, and 1,000 Hz. Peak intensities in CPMG experiments were converted to effective transverse relaxation rates (R2,eff) using the equation, R2,eff = (−1/T) ln(I/I0), where I and I0 are peak intensities measured with and without the CPMG delay (Korzhnev et al., 2004). We estimated the exchange regime from the analysis of the R2,eff dependence with the B0 (Millet et al., 2000). Since all the measured probes had values compatible with a fast exchange regime, variation in R2,eff as a function of CPMG pulsing frequency was fit to:

$$
R_{2,eff}^{}=R_{2}+R_{ex}.1-2\tauv_{CPMG}tanh⁡\frac{1}{2\tau.v_{CPMG}}
$$

The authors note that this analysis fails to provide several additional details that could be obtained from the full Carver-Richards equations such as populations and chemical shift differences, however to obtain those parameters it is necessary to have a significant number of probes in slow or intermediate exchange (Kovrigin et al., 2006).Most of the probes that show significant exchange share similar values of τ and there was no significant improvement in the fit using a residue-specific τ, so a two-state model was preferred (Source code 2). The global τ for each state was obtained by averaging the fitted τs for all well-fit probes showing significant exchange, and evaluated by the reduced χ2 (Source code 3). Rex values were included in the analysis only if the reduced χ2 value for the fit fell under the threshold of 1.7. The χ2 values for representative probes are shown in Figure 4—figure supplement 3, Figure 5—figure supplement 3, and Figure 6—figure supplement 11.

### DNA binding experiments and determination of allosteric coupling free energies (∆Gc)

For all DNA binding experiments a 28 bp double stranded DNA was obtained as previously described (Reyes-Caballero et al., 2010) with the following sequence of the AdcO: 5’-TGATATAATTAACTGGTAAACAAAATGT[F]−3’. Apo AdcR binding experiments were conducted in solution conditions of 10 mM HEPES, pH 7.0, 0.23 M NaCl, 1 mM TCEP (chelexed), 10 nM DNA, 25.0°C with 2.0 mM EDTA (for apo-AdcR) or 20 μM ZnCl2 (for ZnII2 AdcR) added to these reactions. Anisotropy experiments were performed on an ISS PC1 spectrofluorometer in steady-state mode with Glan-Thompson polarizers in the L-format. The excitation wavelength was set at 494 nm with a 1 mm slit and the total emission intensity collected through a 515 nm filter. For Zn(II)-bound-AdcR DNA-binding experiments, the data were fit with DynaFit (Kuzmic, 1996) using a non-dissociable dimer 1:1 dimer:DNA binding model (Kdim = 1012 M−1) (Source code 4). For Zn(II)-bound experiments, the initial anisotropy (r0) was fixed to the measured value for the free DNA, with the anisotropy response of the saturated protein:DNA complex (rcomplex) optimized during a nonlinear least squares fit using DynaFit (Kuzmic, 1996). Apo binding data were fit in the same manner, except rcomplex was fixed to reflect the anisotropy change (rcomplex – r0) observed for wild-type AdcR in the presence of zinc. The errors on Kapo,DNA and KZn,DNA, reflect the standard deviation of 3 independent titrations (Table 2). The coupling free energies were calculated using the following equation:

∆Gc= −RTln(KZn,DNA/Kapo,DNA)(Giedroc and Arunkumar, 2007). Negative values of ∆Gc were observed since AdcR is a positive allosteric activator in the presence of ZnII (Kapo,DNA <KZn,DNA,).

### Mag-fura-2 competition assays

All mag-fura-2 competition experiments were performed on an ISS PC1 spectrofluorometer in operating steady-state mode or a HP8453 UV-Vis spectrophotometer as described in our previous work (Capdevila et al., 2017a; Campanello et al., 2013) using the following solution conditions: 10 mM Hepes, pH 7.2, 400 mM NaCl that was Chelex (Bio-rad) treated to remove contaminating metals. 10 mM protein concentration was used for all and MF2 concentration ranged from 13 to 16 μM. These data were fit using a competitive binding model with DynaFit (Kuzmic, 1996) (Source code 5) to determine zinc binding affinities for wild-type and each mutant AdcR using a four-site-nondissociable homodimer binding model, as previously described (Reyes-Caballero et al., 2010) with KZn = 4.9×106 M−1 for mag-fura-2 fixed in these fits. K1 and K2 correspond to filling the two high affinity sites (site 1), and only a lower limits (≥109 M−1) could be obtained for these sites; K3 and K4 were allowed to vary in the fit, and are reported in Supplementary file 1-Table S1. Experiments were conducted three times for each AdcR variant. Errors of the binding constant parameters were estimated from global fits.

### SYPRO orange Differential Scanning Fluorimetry assays

All SYPRO Orange assays were done in triplicate 25 μL reactions on a 96-well plate in a PCR machine in a chelexed buffer containing 10 mM Hepes, pH 7.0, 0.23 M NaCl, 1 mM TCEP. 4 – 8 μM protein concentration and 5x SYPRO orange were added to all reactions (Niesen et al., 2007). 10 μM EDTA was added to apo-AdcR melts to remove any contaminating metals from apo-AdcR samples. For ZnII2 AdcR samples, two protomer mol-equivalents of ZnCl2 were added to these reactions (for ZnII2 AdcR). Other assays were carried out in solution conditions used for NMR spectroscopy, 25 mM MES, pH 5.5, 50 mM NaCl, 1 mM TCEP (chelexed), and 4 – 8 μM protein concentration and 5x SYPRO orange. The temperature was increased from 25°C to 95°C at a ramp rate of 1°C per minute. Apparent melting temperatures (Tm) were determined from the maximum of the first derivative of the florescence signal in each data set. Errors were determined from the standard deviation derived from triplicate measurements.
