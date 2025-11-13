# How clustered protocadherin binding specificity is tuned for neuronal self-/nonself-recognition

## Authors

- Kerry Marie Goodman<sup>1</sup> ([ORCID: 0000-0003-2063-5823](https://orcid.org/0000-0003-2063-5823))
- Phinikoula S Katsamba<sup>1</sup> ([ORCID: 0000-0003-3981-1604](https://orcid.org/0000-0003-3981-1604))
- Rotem Rubinstein<sup>2</sup> ([ORCID: 0000-0003-3657-5984](https://orcid.org/0000-0003-3657-5984))
- Göran Ahlsén<sup>1</sup>
- Fabiana Bahna<sup>1</sup>
- Seetha Mannepalli<sup>1</sup>
- Hanbin Dan<sup>4</sup>
- Rosemary V Sampogna<sup>4</sup> ([ORCID: 0000-0002-1279-4552](https://orcid.org/0000-0002-1279-4552))
- Lawrence Shapiro<sup>1</sup> ([ORCID: 0000-0001-9943-8819](https://orcid.org/0000-0001-9943-8819)) †
- Barry Honig<sup>1</sup> ([ORCID: 0000-0002-2480-6696](https://orcid.org/0000-0002-2480-6696)) †

### Affiliations

1. Zuckerman Mind, Brain and Behavior Institute, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
2. School of Neurobiology, Biochemistry and Biophysics, Tel Aviv University Tel Aviv Israel ([ROR:04mhzgx49](https://ror.org/04mhzgx49))
3. Sagol School of Neuroscience, Tel Aviv University Tel Aviv Israel ([ROR:04mhzgx49](https://ror.org/04mhzgx49))
4. Department of Medicine, Division of Nephrology, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
5. Department of Biochemistry and Molecular Biophysics, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
6. Department of Systems Biology, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))

† Corresponding author

## Abstract

The stochastic expression of fewer than 60 clustered protocadherin (cPcdh) isoforms provides diverse identities to individual vertebrate neurons and a molecular basis for self-/nonself-discrimination. cPcdhs form chains mediated by alternating cis and trans interactions between apposed membranes, which has been suggested to signal self-recognition. Such a mechanism requires that cPcdh cis dimers form promiscuously to generate diverse recognition units, and that trans interactions have precise specificity so that isoform mismatches terminate chain growth. However, the extent to which cPcdh interactions fulfill these requirements has not been definitively demonstrated. Here, we report biophysical experiments showing that cPcdh cis interactions are promiscuous, but with preferences favoring formation of heterologous cis dimers. Trans homophilic interactions are remarkably precise, with no evidence for heterophilic interactions between different isoforms. A new C-type cPcdh crystal structure and mutagenesis data help to explain these observations. Overall, the interaction characteristics we report for cPcdhs help explain their function in neuronal self-/nonself-discrimination.

## Introduction

Clustered protocadherins (cPcdhs) are a large family of cadherin-like proteins named for the clustered arrangement of their genes in vertebrate genomes (Wu and Maniatis, 1999; Wu et al., 2001). cPcdhs play roles in many facets of neural development (Peek et al., 2017), including circuit development, most notably neurite self-avoidance in vertebrates (Kostadinov and Sanes, 2015; Lefebvre et al., 2012; Mountoufaris et al., 2017), and tiling (Chen et al., 2017). In self-avoidance, neurites from the same neuron (sister neurites) actively avoid one another, whereas neurons from different neurons can freely interact. Tiling is similar to self-avoidance, but in tiling all neurons acquire the same identity, so that there is uniform repulsion among self- and nonself-neurites (Chen et al., 2017). Self-avoidance among sister neurites leads to the characteristic arbor structures of dendritic trees, and prevents the formation of self-synapses (Kostadinov and Sanes, 2015; Lefebvre et al., 2012).

The molecular mechanisms through which neurons discriminate self from nonself, differ between vertebrate and most invertebrate animals. For arthropod invertebrates such as Drosophila melanogaster, self-avoidance is mediated by immunoglobulin superfamily Dscam1 cell surface proteins. The stochastic alternative splicing of Dscam1 pre-mRNAs can, in principle, generate 19,008 distinct extracellular isoforms; the vast majority of which, based on ELISA-based binding assays, mediate homophilic recognition (Miura et al., 2013; Schmucker et al., 2000; Wojtowicz et al., 2004; Wojtowicz et al., 2007). Each Drosophila neuron expresses a repertoire estimated at 10–50 isoforms and the large number of Dscam1 isoforms ensures a low probability that any two contacting neurons will have an identical or even a similar isoform repertoire thus minimizing the chance of inappropriate avoidance between nonself-neurons (Hattori et al., 2009).

In mammalian nervous systems, cPcdh isoform expression is controlled by the unique organization of three tandem gene clusters, Pcdhα, Pcdhβ, and Pcdhγ (Wu and Maniatis, 1999), with each cluster containing multiple variable exons, which encode full cPcdh ectodomain regions with six extracellular cadherin (EC) domains, a single transmembrane region, and a short cytoplasmic extension (Figure 1A). The Pcdhα and Pcdhγ gene clusters also contain three ‘constant’ exons that encode cluster-specific intracellular domains. The last two variable exons in the Pcdhα gene cluster and the last three variable exons of the Pcdhγ gene cluster diverge in sequence from other cPcdh isoforms and are referred to as ‘C-type’ cPcdhs (Wu and Maniatis, 1999; Wu et al., 2001). Sequence differences further subdivide Pcdhγ genes into two subfamilies – PcdhγA and PcdhγB (Wu and Maniatis, 1999). The full mouse cPcdh complement is comprised of 53 non-C-type cPcdhs, commonly known as alternate cPcdhs (α1–12, β1–22, γA1–12, and γB1–7), whose expression choices vary stochastically between cells through alternate promoter choice (Canzio and Maniatis, 2019) and 5 C-type cPcdhs (αC1, αC2, γC3, γC4, and γC5), which are constitutively expressed. cPcdh expression, either stochastic or constitutive, varies between cell types: for example, olfactory sensory neurons express ~5–10 cPcdhs stochastically; Purkinje neurons express ~10 alternate cPcdhs stochastically and all five C-types constitutively (Esumi et al., 2005; Kaneko et al., 2006); and serotonergic neurons express just αC2 constitutively (Canzio and Maniatis, 2019; Chen et al., 2017). While the cPcdh and Dscam1 systems bear striking similarities, the relatively small number of cPcdh isoforms – fewer than 60 – has presented a significant challenge to generation of sufficient diversity to provide mammalian neurons with functionally unique identities.

![Figure 1.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig1-v1.jpg)

**Figure 1.:** (A) Schematic depicting the domain organization of cPcdhs. EC, extracellular cadherin domain; TM, transmembrane domain; ECD, ectodomain; ICD, intracellular domain. (B) Schematic of two cPcdhs interacting via the EC1–4 trans interface. (C) Schematic of two cPcdhs interacting via the EC5–6/EC6 cis interface. (D) Schematic depiction of the cis/trans cPcdh zipper comprising multiple cPcdh isoforms (various colors) engaged in homophilic trans interactions and promiscuous cis interactions as required for the proposed ‘isoform-mismatch chain-termination model’ of cPcdh-mediated neuronal self-recognition and self-avoidance.

Solution biophysics and functional mutagenesis studies have shown that cPcdhs interact in trans through antiparallel interactions between their EC1–4 regions (Rubinstein et al., 2015), and crystal structures of alternate α, β, and γ cPcdh trans homodimers have revealed interfaces involving EC1 interacting with EC4 and EC2 with EC3 (Figure 1B; Goodman et al., 2016c; Goodman et al., 2016a; Nicoludis et al., 2016; Rubinstein et al., 2015; Thu et al., 2014). cPcdhs also form cis dimers through their membrane-proximal EC5–6 regions, and are presented on cell surfaces as cis dimers (Goodman et al., 2017; Rubinstein et al., 2015; Thu et al., 2014). Crystal structures of cis-interacting protocadherin ectodomains (Brasch et al., 2019; Goodman et al., 2017) have revealed an asymmetrical interaction mode, where one molecule interacts through elements of EC5 and EC6, and the other interacts exclusively through EC6 (Figure 1C). To date, structural studies of C-type cPcdh interactions have not been available. Here, we extend our molecular understanding of cPcdhs to C-type isoforms as well, with the goal of understanding the evolutionary design of the entire family.

In order to explain how about 60 cPcdh isoforms can provide a comparable or even greater level of neuronal diversity as 19,000 Dscam isoforms, Rubinstein et al., 2015 proposed that cPcdhs located on apposed membrane surfaces would form an extended zipper-like lattice through alternating cis and trans interactions (Figure 1D). In self-interactions – between two membranes with identical cPcdh repertoires – these chains would grow to form large structures, limited mainly by the number of molecules (Brasch et al., 2019; Rubinstein et al., 2015). However, in nonself-interactions – between two membranes with differing cPcdh repertoires – such large linear assemblies would not form since even a single mismatch between expressed isoforms would terminate chain assembly (Brasch et al., 2019; Rubinstein et al., 2017; Rubinstein et al., 2015). This ‘isoform-mismatch chain-termination model’ for the ‘barcoding’ of vertebrate neurons envisions the assembly of long cPcdh chains between sites of neurite–neurite contact to represent the signature of ‘self’, which is then translated by downstream signaling that leads to self-avoidance (Fan et al., 2018). X-ray crystallographic studies and cryo-electron tomography studies of the full-length cPcdh ectodomains bound between the surfaces of adherent liposomes revealed the existence of linear zippers thus providing strong evidence supporting the validity of the model (Brasch et al., 2019). However, crucial questions remain unanswered. Here, a number of them are addressed.

Overall, in accordance with the requirements of the isoform-mismatch chain-termination model, we find that trans homophilic interactions are remarkably precise, with no evidence for heterophilic interactions between different cPcdh isoforms. In contrast cPcdh cis interactions are largely promiscuous but with relatively weak intrasubfamily and, especially, homophilic interactions. Possible implications of this somewhat surprising finding are considered in the discussion. Our study reveals how the extraordinary demands posed by the need to assign each neuron with a unique identity are met by an unprecedented level of protein–protein interaction specificity.

## Results

### cPcdh trans interactions are strictly homophilic

We generated biotinylated ectodomain fragments containing the trans-interacting EC1–4 regions (Nicoludis et al., 2015; Rubinstein et al., 2015) of six representative α, β, γA, and γB mouse cPcdh isoforms – α7, β6, β8, γA8, γA9, and γB2 – which include the most closely related isoforms by sequence identity from the β and γA subfamilies (β6/8 and γA8/9) (Rubinstein et al., 2015). These molecules were coupled over independent NeutrAvidin-immobilized flow cells and trans-interacting ectodomain fragments of multiple members of each mouse cPcdh subfamily, including the C-types (α4, α7, α12, β6, β8, γA4, γA8, γA9, γB2, γB4, γB5, αC2, γC3, γC4, and γC5), were then flowed over the six cPcdh surfaces to assess their binding. The surface plasmon resonance (SPR)-binding profiles reveal strictly homophilic binding (Figure 2A). All ectodomain fragments used in these SPR experiments were confirmed to form homodimers in solution by sedimentation equilibrium analytical ultracentrifugation (AUC) (Figure 2—source data 1), validating that these proteins are well behaved and active. Remarkably, no heterophilic binding was observed for any of the analytes over any of the six surfaces (Figure 2A). Even β6/8 and γA8/9 that have 92% and 82% sequence identities, respectively, in their trans-binding EC1–4 regions exhibit no heterophilic binding. We estimate that, for heterophilic trans dimers, the lower limit for the dissociation constant (KD) would be ~200 μM. Mutations designed to disrupt α7, β6, and γA8 trans interaction inhibited homophilic binding, demonstrating that the observed binding occurs via the trans interface (Figure 2—figure supplement 1A; Goodman et al., 2016a; Goodman et al., 2016c; Rubinstein et al., 2015). This behavior is unlike that of other adhesion receptor families where, whether they display homophilic or heterophilic preferences, the signal is never as binary as the one shown in Figure 2 (Honig and Shapiro, 2020).

![Figure 2.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig2-v1.jpg)

**Figure 2.:** (A) Surface plasmon resonance (SPR) binding profiles of cPcdh trans fragment analytes from all cPcdh subfamilies (denoted in the top row) flowed over six surfaces coated with alternate cPcdh trans fragments (rows). Responses over all surfaces are drawn on the same scale and normalized for molecular weight (mw). (B) SPR binding profiles of cPcdh trans fragment analytes from all cPcdh subfamilies (shown in columns) flowed over individual surfaces coated with C-type and α4 cPcdh trans fragments (rows). Responses over all surfaces are drawn on the same scale and normalized for molecular weight.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) SPR-binding curves for wild-type and trans mutant alternate clustered protocadherins (cPcdhs) flowed over their respective immobilized wild-type molecule. (B) SPR-binding curves for wild-type and trans mutant C-type cPcdh γC5 flowed over immobilized wild-type γC5.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Structural superposition of the β61–4 and β81–4 trans dimer crystal structures (PDBs: 5DZX and 5DZY) shown in ribbon depiction above, with close-up views of the trans interfacial regions containing the five interfacial residues that vary between β61–4 and β81–4 shown below. The two protomers forming the β61–4 dimer are colored green and pale green, respectively. The β81–4 dimer is colored magenta/light pink. Bound calcium ions are shown as green spheres. Interfacial residue side chains are shown in the close-up views. The five variable residues are labeled with the β61–4 amino acid given in green and the β81–4 amino acid in magenta: R/N41 is in EC1; E/K369 and Y/F371 are in EC4; S/I117 is in EC2 and self-interacts at the trans dimer center of symmetry; and L/P125 is also in EC2. (B) Surface plasmon resonance (SPR)-binding profiles of β6 trans interface mutants converting β61–4 to β81–4 and the wild-type molecules (shown in columns) were flowed over surfaces coated with wild-type β61–4 or β81–4 (rows). (C) Results of the K562 coaggregation assay where cells transfected with mCherry-labeled β6 and β8 wild-types (WT) and the same trans specificity mutants as in (B) were each mixed with cells transfected with mVenus labeled β6 and β8 WT. Experiments where the red and green cells coaggregate demonstrating interaction between the mCherry-labeled WT or mutant clustered protocadherin (cPcdh) and the mVenus-labeled WT cPcdh are labeled ‘mixed’ and highlighted with magenta boxes. Scale bar, 100 μM.

Much of the original evidence as to homophilic specificity was based on cell aggregation assays (Rubinstein et al., 2015; Schreiner and Weiner, 2010; Thu et al., 2014) and it is of interest to compare the results obtained from these assays to those obtained from SPR. We do this in the context of examining the heterophilic binding specificity between β61–4 and β81–4trans fragments that share 92% sequence identity and differ at only five residues (Figure 2—figure supplement 2A), within their respective binding interfaces (Goodman et al., 2016c). Each of these residues was mutated individually and in combination. Figure 2—figure supplement 2B, C displays SPR profiles and cell aggregation images, respectively, for wild-type β6 and β8 and for the various mutations. We first note that changing all five residues in β6 to those of β8 generates a mutant protein with essentially wild-type β8 properties; it binds strongly to β8 but not to β6 as seen in SPR and also forms mixed aggregates with β8 but not β6. In contrast, most of the single residue mutants retain β6-like properties in both assays whereas double and triple mutants exhibit intermediate behavior between β6 and β8. These results demonstrate that despite the 92% sequence identity between β6 and β8, their highly specific homophilic properties can be attributed to five interfacial residues. Moreover, the cell aggregation assays are consistent with the heterophilic binding traces measured by SPR; cells expressing mutants that generate strong SPR signals with either wild-type β6 or β8 also form mixed aggregates with cells expressing the same wild-type protein.

Of note, trans-interacting fragments of all four C-type cPcdhs tested showed no binding over the alternate cPcdh SPR surfaces (Figure 2A). To test whether C-type cPcdhs also show strict homophilic specificity with respect to each other we coupled biotinylated trans-interacting fragments of αC2, γC3, γC4, and γC5 to SPR chips and passed the same four fragments alongside alternate cPcdh trans fragments over these four surfaces. Only homophilic binding was observed, with each of the four C-type fragments binding to its cognate partner and no other isoform (Figure 2B). Disrupting the γC5 trans interaction with the S116R mutation (Rubinstein et al., 2015), inhibited binding to the γC5 surface, demonstrating that the observed binding occurs via the trans interface (Figure 2—figure supplement 1B).

In contrast to the other C-type isoforms, αC1 does not mediate cell–cell interactions in cell aggregation assays even when coexpressed with cPcdhs that facilitate cell-surface delivery of γC4 (Thu et al., 2014). Although we have been able to produce an αC1 EC1–4 fragment the recombinant molecule forms disulfide-linked multimers which are likely nonnative, precluding confident examination of αC1’s potential trans interactions. Notably, the sequence of mouse αC1 reveals the EC3:EC4 linker does not contain the full complement of calcium-coordinating residues, which may impact the structure and binding properties of this protein (Thu et al., 2014).

Since all the cPcdh trans fragment molecules used in these SPR experiments homodimerize our SPR data cannot be used to determine accurate binding affinities (Rich and Myszka, 2007). We therefore used AUC to measure the trans homodimer KDs (Figure 2—source data 1) revealing a >200-fold range of binding affinities, from 2.9 μM (α71–5) to >500 μM (γC41–4). Regardless of their trans-binding affinity, all cPcdhs (except αC1) have previously been shown to effectively mediate cell–cell interactions in cell aggregation assays (Schreiner and Weiner, 2010; Thu et al., 2014).

### Crystal structure of C-type cPcdh γC4 reveals EC1–4-mediated head-to-tail trans dimer interaction

The biophysical properties of C-type cPcdhs pose a number of interesting questions: Despite their more divergent sequences compared with alternate cPcdhs, AUC data have confirmed that C-type cPcdhs αC2, γC3, and γC5 form trans dimers using their EC1–4 domains (Goodman et al., 2016a; Rubinstein et al., 2015). However, γC41–4 behaved as a very weak dimer in AUC (KD >500 μM; Figure 2—source data 1), nevertheless full-length γC4 can mediate cell aggregation when delivered to the cell surface by coexpression with a ‘carrier’ cPcdh (Thu et al., 2014). In addition, C-type isoforms have unique expression profile and function compared to alternate cPcdhs (Canzio and Maniatis, 2019; Mountoufaris et al., 2018). However, there are no published crystal structures of C-type cPcdh trans dimers. We therefore sought to crystallize a mouse C-type cPcdh engaged in a trans interaction and obtained two distinct crystal forms of γC4EC1–4, one at 2.4 Å resolution (crystallized at pH 7.5) and the other with anisotropic diffraction at 4.6/3.9/3.5 Å resolution (Figure 3A, Figure 3—figure supplement 1A, B, Figure 3—source data 1) (crystallized at pH 6.0). Both crystal structures revealed an EC1–4-mediated head-to-tail trans dimer: The 4.6/3.9/3.5 Å crystal structure appears to have a fully intact trans interface with a total buried surface area of 3800 Å2, which is a similar size to other cPcdh trans dimer interfaces (Goodman et al., 2016a; Goodman et al., 2016c; Nicoludis et al., 2016; Figure 3B, Figure 3—figure supplement 1B). However, the 2.4 Å structure had an apparently partially disrupted EC2:EC3 interface resulting in a total buried surface area of just 2900 Å2 (Figure 3B). The difference between the two structures may be due to differences in the pH of the crystallization and its effect on the ionization state of the three histidines present in the EC2:EC3 interface (Figure 3B). The differences could also reflect distinct states of a dynamic interaction, as has previously been observed crystallographically (Nicoludis et al., 2016; Goodman et al., 2016a) and explored computationally for other cPcdh trans interactions (Nicoludis et al., 2019).

![Figure 3.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig3-v1.jpg)

**Figure 3.:** (A) Ribbon diagrams of the γC4EC1–4 trans dimer crystal structures obtained from two different crystal forms. Bound calcium ions are shown as green spheres and glycans are shown in pale blue spheres. (B) The two crystal structures have a markedly different trans interface buried surface area (BSA). Left, surface views of the two trans dimer crystal structures highlight the difference, with a gap apparent in the EC2:EC3 region of the interface in crystal form two that is absent from crystal form 1. Surfaces are colored by atom type with the carbons colored orange for crystal form one and yellow for crystal form 2. Right, close-up view of the gap region in the crystal form two dimer with the side chains depicted as sticks. The intact crystal form 1 γC4 dimer is similar overall to those of the published intact alternate α, β, γA, and γB cPcdhs and the published δ2 nonclustered (nc) Pcdh trans dimers (root mean square deviation [RMSD] over aligned Cαs 2.4–4.5 Å; Figure 3—source data 2). The published crystal structures of γA1, γA8, and γB3 also show partially disrupted trans interfaces though in differing regions of the interface (Goodman et al., 2016a, Nicoludis et al., 2016). (C) Comparison between the (i) EC1:EC4 and (ii) EC2:EC3 regions of the γC4 (orange) and γB2 (blue, PDB 5T9T) trans dimer interfaces. Potential hydrogen bonds are depicted as dashed black/yellow (γC4) or blue (γB2) lines. (i) Structural alignment of the EC1:EC4 portion of the γC4 and γB2 trans dimers highlights a possible destabilizing role for γC4 residue E78 since unlike its counterpart in γB2 (D77), it is not juxtaposed with a basic residue. (ii) Similarly, an additional negatively charged residue (D290) which occupies a central position in the γC4 EC2:EC3 interface may also contribute to γC4’s comparatively weak trans dimer interaction. Distances between the D290 side chain and its nearest contacts are shown as dashed gray lines with distances given in Angstroms. (D) Sedimentation equilibrium analytical ultracentrifugation (AUC) experiments were conducted on γC4 EC1–4 wild-type (wt) and interface mutants to assess whether E78 and D290 negatively impact trans dimerization. Table details the oligomeric state and dissociation constants for each protein tested.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Our crystallization experiments with γC4EC1–4 yielded two distinct crystal forms the first of which showed significant X-ray diffraction anisotropy. (i) UCLA Diffraction Anisotropy Server (Strong et al., 2006) plot shows the F/sigma by resolution along the a*, b*, and c* axes. (ii) Synthetic precession photographs of the X-ray diffraction in the k = 0 plane (left) and the h = 0 plane (right) showing the comparatively stronger/weaker diffraction. (B) Close-up views of the EC1:EC4 and EC2:EC3 interfacial regions from the first crystal form. One protomer in the symmetric dimer is colored yellow the other orange. Interfacial residues are labeled, side chains are shown in stick representation and dashed black lines depict potential interfacial hydrogen bond interactions. The two charged residues, E78 and D290, we selected for mutagenesis experiments to see whether they play a destabilizing role in the γC4 trans interaction are marked with red dashed boxes. (C) Representative plot of analytical ultracentrifugation (AUC) data for the wild-type (wt) and mutant γC4 EC1–4 molecules. Raw data are shown in black circles, and the nonlinear fits to a monomer-to-dimer model are shown as blue lines. The residuals between the data and fits are shown in the plot below. Table detailing the oligomeric state and dissociation constants determined from the AUC data is shown in Figure 3.

Despite the γC4 trans dimer sharing structural similarity and the interface having similar buried surface area as alternate α, β, γA, and γB cPcdhs and δ2 nonclustered Pcdhs (Figure 3—source data 2; Cooper et al., 2016; Goodman et al., 2016a; Goodman et al., 2016c; Harrison et al., 2020; Hudson et al., 2021; Nicoludis et al., 2016), its binding affinity is very weak. The two most structurally similar molecules to γC4 over their trans-interacting domains are cPcdh γB2 and nonclustered Pcdh19. γB2 and Pcdh19 have trans dimer KDs of 21.8 and 0.48 μM, respectively (Harrison et al., 2020), while that of γC4 is >500 μM. Comparison between the γB2 and γC4 dimer interfaces highlighted two buried charges in the γC4 trans interface, E78 and D290, which could potentially contribute to the low interaction affinity (Figure 3C). To test this, we mutated these two residues to neutral amino acids and used AUC to determine whether the binding affinity increased: The two D290 mutations we tested, D290A and D290N, had no measurable impact on binding; but mutating E78 significantly increased the binding affinity with γC4EC1–4 E78A showing a KD of 58 μM and γC4EC1–4 E78Q, 83 μM (Figure 3D, Figure 3—figure supplement 1C). The equivalent residue to E78 in γB2 is also charged (D77) and forms a salt bridge with K340 in the γB2 dimer (Figure 3C). To assess whether generating a similar salt bridge in γC4 would compensate for the negative impact of E78 on dimer affinity we generated an S344R mutant. Similar to the E78 mutants, γC4EC1–4 S344R also had a stronger binding affinity than wild-type with a KD of 112 μM (Figure 3D, Figure 3—figure supplement 1C). It appears then that E78 plays an important role in weakening cPcdh γC4’s trans interaction although the functional reasons for γC4’s weak trans interaction are unclear.

### cPcdh cis interactions are promiscuous with a range of interaction strengths

To systematically investigate cPcdh cis interactions, we coupled cis-interacting fragments of mouse β9, γA4, γA9, γB2, αC2, γC3, and γC5 to SPR chip surfaces. Cis-interacting fragments of three members from each of the β, γA, and γB subfamilies (β1, β6, β9, γA3, γA4, γA9, γB2, γB5, and γB7) alongside αC2, γC3, and γC5 fragments were flowed over the seven surfaces to detect their heterophilic binding (Figure 4A). Alternate α-cPcdhs, and the C-types αC1 and γC4 were not included in this study since EC6-containing fragments of these molecules cannot be expressed, although an α7EC1–5/γC3EC6 chimera was included among the analytes to assess the role of α7 EC5 (Figure 4—figure supplement 1C). Each of the analytes was also analyzed by AUC to determine their homophilic cis-interaction behavior (Figure 4—source data 1): Four analytes, β13–6, γA43–6, γA93–6, and γC33–6, are monomeric in solution as measured by AUC, therefore their SPR binding profiles could be analyzed to determine their heterophilic binding affinities (Figure 4B, Figure 4—figure supplement 1A, B). For the remaining analytes, due to the added complexity of their homophilic cis interactions in solution competing with their binding to the immobilized molecules, the SPR responses could not be analyzed to determine accurate KDs (Rich and Myszka, 2007).

![Figure 4.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig4-v1.jpg)

**Figure 4.:** (A) Surface plasmon resonance (SPR)-binding profiles of cPcdh cis fragment analytes from all cPcdh subfamilies except alphas (shown in columns) flowed over individual surfaces coated with cPcdh cis fragments. Binding profiles for each surface are individually scaled and responses are normalized for molecular weight. (B) Table of dissociation constants calculated from the SPR data for the four monomeric analytes. The number in brackets represents the error of the fit based on analysis of duplicate responses. Binding signals were not detected for interactions labeled NB (no binding) while >50 represents interactions with KDs > 50 μM, where an accurate KD cannot be determined.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Kinetic binding analysis of γC33–6 analyte binding over a β93–6 covered surface. Data are shown in black, and the red traces represent the fit to an 1:1 binding model. (B) Left, surface plasmon resonance (SPR)-binding profiles from Figure 4 for the four monomeric cis fragment analytes over all six cis fragment surfaces. Right, fit of the binding data for these four analytes to 1:1 binding isotherms to calculate KDs. γA43–6 and γA93–6 are monomeric and they are not included in the binding isotherms over their respective surface. (C) SPR-binding profiles for γC33–6 (from Figure 4) and an α71–5/γC36 chimera flowed over the immobilized cis fragment surfaces. Binding profiles for each surface are individually scaled as in Figure 4.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Chart shows the cPcdh trans dimer, homophilic cis dimer, and heterophilic cis dimer interactions for which we have determined binding affinities divided into four subgroups based on their dissociation constant. The trans and homophilic cis dimer affinities were determined using analytical ultracentrifugation (AUC; Figure 2—source data 1 and Figure 4—source data 1) and the heterophilic cis dimer affinities were determined using surface plasmon resonance (SPR; Figure 4B). Of the interactions in the >50 μM group one trans interaction and four homophilic cis interactions are monomeric in solution (>500 μM KD in AUC). Three of the 11 heterophilic cis interactions in the >50 μM group show no binding in our SPR experiments based on a 40-RU-binding threshold.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A) Amino acid sequence alignments of cis interfacial residues from the EC6-only and EC5–6 surfaces for all 58 mouse cPcdhs subdivided by subfamily. Completely conserved residues are highlighted in red with white lettering. Residues 540 and 541 are included in the EC6-only alignments since the crystal structure of γA4 EC3–6 (PDB: 5SZQ) revealed a distinct EC6 A–A′ loop architecture to that observed in the γB2, 4, and 7 (PDBs: 5SZR, 6E6B, and 5V5X) cis fragment crystal structures that would place these residues in the EC6-only interface if maintained in cis interactions. (B) Sequence logos based on the sequence alignment shown in (A) for the EC6-only cis interfacial residues from each of the five cPcdh subfamilies highlighting the similarities and conserved differences between the subfamilies. Residues 540 and 541 are included for all isoforms but grayed out for the non-γA isoforms since their involvement may be γA specific. NB: Previous studies have shown that α-cPcdhs have an impaired EC6-only interface (Thu et al., 2014; Goodman et al., 2017). (C) Sequence logos for the EC5–6 cis interfacial residues from each of the five cPcdh subfamilies.

The data clearly demonstrate a wide range of cis dimerization affinities with strong heterophilic binding signals (500–2000 RU), with much weaker homophilic binding responses typically between 100 and 140 RU. The strongest heterophilic cis interactions are in the submicromolar range; for example, γC3/β9 can heterophilically cis-dimerize with a KD of 0.22 μM, while β93–6, γB23–6, αC22–6, and γC52–6 homodimerize with AUC-determined KDs of 9–80 μM. In addition to uniformly weak homophilic interactions, within-subfamily cis interactions were consistently among the weakest observed although a number of intersubfamily interactions were also relatively weak (Figure 4A). For example, for the β9 surface comparatively weak binding was observed for all tested β and γA isoforms except γA3, with the monomeric β1, γA4, and γA9 producing low responses that could not be fit to a binding isotherm to calculate accurate KDs (Figure 4B, Figure 4—figure supplement 1B). In contrast, robust binding to the β9 surface was observed for all γB and C-type isoforms. These data are consistent with the binding responses when β9 was used as an analyte over the other six surfaces, with weak to no binding observed over the γA4 and γA9 surfaces and robust responses over the γB2, αC2, γC3, and γC5 surfaces (Figure 4A). The γA4 and γA9 surfaces showed a similar pattern of binding behaviors, with weak to no binding observed for the γA and αC2 analytes, and robust binding for the γC-cPcdhs with KDs for γC33–6 of 2.73 and 9.60 μM, respectively, over each surface (Figure 4, Figure 4—figure supplement 1B).

Overall, these SPR data show that cPcdh cis binding is generally promiscuous, with measurable cis interactions observed for 86% of pairs tested (using a 40 RU threshold). However, the wide range of binding responses and homo- and heterodimeric KDs that span 0.2201 μM to no measurable interaction in solution suggests certain cis dimers will form preferentially to others. For the heterophilic binding pairs for which KDs could be determined (Figure 4B, Figure 4—figure supplement 1, Figure 4—figure supplement 2), the alternate cPcdhs in particular, form markedly stronger cis heterodimers with members of different subfamilies, particularly γC3 and/or γC5, compared to their homodimeric and within-subfamily interactions. γC3 also formed stronger heterodimers with αC2 than with itself or γC5. Of note, αC2 and γC5 both form strong cis homodimers with KDs of 8.9 and 18.4 μM, respectively, as determined from AUC experiments (Figure 4—source data 1), a magnitude similar to many of their heterodimeric interactions of 11.5 and 6.9–18.2 μM, respectively (Figure 4B).

In the next section, we rationalize cis-binding preferences in terms of the structural properties of cis dimers.

### The asymmetric cis dimer interface and cis-binding specificity

The crystal structure of the γB7 cis dimer revealed an asymmetric interaction, with the dimer formed by one protomer engaging using surface of both EC5 and EC6 and one protomer engaging using only EC6 (Goodman et al., 2017) with regions of EC6 overlapping in both EC5–6 and the EC6-only interfaces for all cPcdh subfamilies (Thu et al., 2014; Goodman et al., 2017). The asymmetric nature of the cis interaction implies that for each dimer interaction there are two possible arrangements: one with protomer ‘1’ forming the EC5–6 side and protomer ‘2’ forming the EC6-only side and the second where protomer ‘1’ forms the EC6-only side and ‘2’ the EC5–6 side. These two configurations are distinct with different residue:residue interactions. Alternate α-cPcdhs, which can only form the EC5–6 side of the cis dimer, require coexpression with a ‘carrier’ cPcdh from another cPcdh subfamily, which can form the EC6-only side of the cis dimer, for robust delivery to the cell surface (Thu et al., 2014; Goodman et al., 2017). Although α-cPcdhs and γC4, which also requires a carrier for delivery to the cell surface, are likely to be extreme cases, sequence analysis alongside the low homodimerization ability of many cPcdh isoforms suggests many cPcdhs will more readily form one side of the cis interface than the other (Goodman et al., 2017).

We previously suggested that γA-cPcdhs will prefer to form the EC6-only side of the interface since they have a poorly conserved EC5 interface and do not form strong homodimers in solution (Figure 4—source data 1; Goodman et al., 2017). The C-type cPcdh γC3 also does not form cis homodimers in solution. However, as shown in Figure 4, γA-cPcdhs form strong heterodimers with γC3 with dissociation constants in the low-micromolar range (Figure 4B and Figure 4—figure supplement 1B). Structure-guided sequence analysis for the γA4/γC3 dimer in both EC6-only and EC5–6 possible orientations, using the available crystal structures of the γB7EC3–6 cis dimer and monomeric γA4EC3–6 (Figure 5A and Figure 5—figure supplement 1), suggests that γC3 prefers to form the EC5–6 side: γC3 has a number of residue differences in interface residues that are conserved among β, γA, and γB cPcdhs (V/L555, R/K558, W/V562, and S/R595) that seem likely to disfavor the EC6-only side of the interface and favor the EC5–6 side (Figure 5—figure supplement 1B, C,). Two of these residues, V555 and S595, result in a potential loss of EC6-only interface buried surface area and are shared with α-cPcdhs, which cannot occupy the EC6-only position (Goodman et al., 2017). Structural analysis further suggests that γC3-specific residue R558 would not be well accommodated from the EC6-only side, potentially causing van der Waals clashes (Figure 5—figure supplement 1C). By contrast, from the EC5–6 side R558 is positioned to form an additional salt bridge with γA4 residue E544 and a hydrogen bond with Y532, promoting dimer formation (Figure 5A; Figure 5—figure supplement 1B). γA4 residue E544 is positioned to form this salt bridge due to the EC6 A/A′ loop region adopting a different arrangement in the γA4 crystal structure to that observed for γB2 and γB7 in their respective crystal structures (Goodman et al., 2016a; Goodman et al., 2017).

![Figure 5.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig5-v1.jpg)

**Figure 5.:** (A) Structural model of γA4/γC3 cis dimer based on γB7EC3–6 cis dimer and γA4EC3–6 crystal structures (PDBs: 5V5X and 5SZQ). γA4 is shown adopting the EC6-only side (blue protomer) and γC3 is shown adopting the EC5–6 side (yellow protomer). Left, schematic of the γA4/γC3 EC3–6 cis dimer. Right, close-up view of the EC6:EC6 interface from the modeled cis dimer showing interfacial residue side chains. Bound calcium ions are shown as green spheres. Residues which were mutated in the panel B are circled in red. γB7 crystal structure numbering is used for both γA4 and γC3 residues. See methods for γA4 and γC3 alignment. Please note the model shown here is solely for hypothesis generation, since it is unlikely to be completely accurate. See methods for further details of structural modeling. (B) Top, size exclusion-coupled multiangle light scattering (SEC-MALS) data for an equimolar mixture of wild-type γA4EC3–6 and γC3EC3–6 showing dimer formation. Plot shows size exclusion absorbance at 280 nm trace (left axis), molecular weight of the eluant peaks (right axis), and the monomer molecular weights of γA4EC3–6 and γC3EC3–6 measured by mass spectrometry – 54.5 and 56.5 kDa, respectively – as dashed gray lines. Average molecular weight of the molecules in the dimer and monomer eluant peaks are labeled. Middle, SEC-MALS data for V560R mutants, which target the EC6-only side of the interface. Bottom, SEC-MALS data for residue 558 mutants. The γC3-like K558R mutation in γA4 inhibits heterodimer formation with wild-type γC3. Similarly, the γA4-like R558K in γC3 inhibits dimerization with wild-type γA4. (C) SPR-binding profiles for γB7EC3–6 wild-type and cis interface mutants flowed over three individual wild-type cis fragment surfaces. The two mutations specifically target one side of the cis interface.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) (i) Schematic of the asymmetric γB7EC3–6 cis dimer crystal structure. (ii) Close-up view of the γB7 cis interface: interfacial residue side chains are shown in pink for the EC6-only protomer and purple for the EC5–6 protomer. Bound calcium ions are shown as green spheres. (B) (i) Schematic of the γA4EC6/γC3EC5–6 cis dimer. (ii) Model of the γA4EC6/γC3EC5–6 cis dimer interaction generated using structural alignment of EC6 from the monomeric γA4 EC3–6 crystal structure (PDB 5SZQ) to the γB7 EC3–6 cis dimer structure for the EC6-only side and computational mutagenesis of γB7 to γC3 selecting the best-fit rotamer (without energy minimization) for the EC5–6 side. The model suggests that this will be the preferred orientation for the γA4/γC3 cis dimer interaction. Favorable residue differences between γB7 from (A) and γA4/γC3 in this orientation are noted in green. Please note the model shown here is only used for hypothesis generation, since it is unlikely to be completely accurate. (C) (i) Schematic of the γC3EC6/γA4EC5–6 cis dimer. (ii) Model of the γC3EC6/γA4EC5–6 cis dimer generated using computational mutagenesis of γB7 to γC3 selecting the best-fit rotamer (without energy minimization) for the EC6-only side and structural alignment of EC5–6 from the γA4 EC3–6 crystal structure to the γB7 EC3–6 cis dimer structure for the EC5–6 side. The model suggests that this orientation for the γA4/γC3 cis dimer interaction will be disfavored. Unfavorable residue differences between γB7 and γA4/γC3 in this orientation are noted in red. Please note the model shown here is unlikely to be completely accurate and is simply for hypothesis generation.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/72416/elife-72416-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) SEC-MALS data for wild-type γA43–6, wild-type γC33–6, and γC33–6 V560R showing all three molecules are monomeric in SEC-MALS, consistent with their behavior in sedimentation equilibrium AUC. Plots show size exclusion absorbance at 280 nm trace in blue (left axis), molecular weight of the eluant peak in black (right axis), and the monomer molecular weight of γA43–6 or γC33–6 measured by mass spectrometry – 54.5 and 56.5 kDa, respectively – as dashed gray lines. Average molecular weight of the molecules in the eluant peaks are labeled. (B) Surface plasmon resonance (SPR)-binding profiles for γA43–6 wild-type and γA43–6 with γC3-like cis interface mutation K558R flowed over immobilized wild-type γC33–6. Loss of γC33–6 interaction in the presence of the K558R mutation is consistent with the SEC-MALS results shown in Figure 5.

Based on our analysis, we generated mutants of both γA4 and γC3 targeting the EC6-only side of the interface and used size exclusion-coupled multiangle light scattering (SEC-MALS) to assess their preferred orientation on γA4/γC3 heterodimerization. In SEC-MALS wild-type γA4EC3–6 and γC3EC3–6 behave as monomers when run alone, and form a dimer when mixed in equimolar amounts (Figure 5B; Figure 5—figure supplement 2A). The V560R mutation (γB7 numbering, see methods for sequence alignment) is based on EC6-only impaired α-cPcdhs, and has been previously shown to block γB6’s homophilic cis interaction in solution (Goodman et al., 2017). γA4 V560R did not dimerize with wild-type γC3, whereas γC3 V560R could still dimerize with wild-type γA4 (Figure 5B). Therefore, impairing γA4’s EC6-only interface blocks γA4/γC3 dimer formation while impairing γC3’s EC6-only interface does not (although the dimerization appears to be weaker compared to the wild-type γA4/γC3 cis-interacting pairs). We also generated a γC3-like mutant of γA4, K558R, which also targets the EC6-only interface. Like γA4 V560R, γA4 K558R also did not dimerize with wild-type γC3 in MALS and, when replicated, in SPR experiments (Figure 5B, Figure 5—figure supplement 2B). The reverse mutation in γC3, R558K, inhibited dimerization with wild-type γA4 (Figure 5B). Therefore, like the α-specific R560 residue, γC3-specific R558 has distinct effects on dimerization when in γA4 or γC3, inhibiting heterodimerization when mutated into γA4 but promoting heterodimerization in γC3. Together these data suggest that the γA4/γC3 dimer has a preferred orientation, with γA4 predominantly occupying the EC6-only position and γC3 the EC5–6 side. Our data also account for the fact that neither isoform homodimerizes in solution since the EC5–6 side would be impaired in the γA4 homodimer while the EC6 side would be impaired in the γC3 homodimer.

Next, we sought to test whether γA4 and γC3 preferentially adopt these specific positions in cis interactions with a γB isoform. To accomplish this we generated mutants of γB7 individually targeting the EC6-only interaction surface, γB7 Y532G, and the EC5–6 side, γB7 A570R, respectively (Goodman et al., 2017; Figure 4—source data 1). In SPR, γB7 Y532G had only a small impact on γA4 binding, while γB7 A570R abolished γA4 binding (Figure 5C). In contrast, γB7 Y532G prevented γC3 binding while γB7 A570R showed robust γC3 binding (Figure 5C). These results suggest that γA4/γB7 and γC3/γB7 cis heterodimers also have preferred orientations with γA4 and γC3 maintaining their preferences for the EC6-only and EC5–6 positions, respectively. Additionally, SPR data for the γB7 mutants over the αC2 surface suggest αC2 preferentially occupies the EC6-only side in αC2/γB7 dimers (Figure 5C). This is notable since αC2 forms robust cis homodimers and therefore, like γB7, can presumably readily occupy both positions in its homophilic interactions, implying that the αC2/γB7 orientation preference could be specific to the particular heterodimer pairing. However, since this interpretation is based on a single mutation further interrogation of αC2’s interactions would be required to be conclusive. A broader examination of orientation preferences among cis dimer pairings beyond those of molecules with weak cis homodimer affinities, such as γA4 and γC3 examined here, could be instructive.

## Discussion

### Trans specificity

The results of this study add to our current understanding of cPcdhs in a number of ways. First, they reveal a remarkable level of specificity in trans homophilic interactions since in no case was a heterophilic trans interaction detected in our SPR measurements. Prior data have clearly indicated that cPcdhs exhibit a preference for homophilic trans interactions but the extent of this specificity was not established in quantitative terms but were, rather, based on cell aggregation experiments. The SPR experiments with cPcdhs reported here show no evidence of cross-interaction between nonidentical cPcdh isoforms. This level of specificity is unusual for cell–cell recognition proteins, as significant intrafamily interactions are evident in most other families examined to date including type I cadherins (Katsamba et al., 2009; Vendome et al., 2014), type II cadherins (Brasch et al., 2018), DIPs and Dprs (Cosmanescu et al., 2018), sidekicks (Goodman et al., 2016b), and nectins (Harrison et al., 2012). Even the nonclustered δ- protocadherins, which are preferentially homophilic and utilize an antiparallel EC1–4 interface like the cPcdhs (Cooper et al., 2016; Harrison et al., 2020; Modak and Sotomayor, 2019), show heterophilic intra-family trans interactions, though they show no cross-reactivity with cPcdhs (Harrison et al., 2020).

High-fidelity homophilic interaction is a strict requirement of the chain-termination model for the barcoding of vertebrate neurons and has been accomplished through the exploitation of a multidomain interface of almost 4000 Å2 (Nicoludis et al., 2019) that enables the positioning of enough ‘negative constraints’ (Sergeeva et al., 2020) to preclude the dimerization of about 1600 heterophilic pairs of 58 mouse cPcdh isoforms (Rubinstein et al., 2017). Dscams accomplish the same task for thousands of isoforms by exploiting the combinatorics made possible by a three-domain interface where each domain interacts largely independently with an identical domain on its interacting partner (see discussion in Zipursky and Grueber, 2013). Although it is likely that Dscams dimerize with a comparable level of homophilic specificity to that of cPcdhs, the evidence is based on a semiquantitative ELISA-type assay of recombinant multimerized isoforms (Wojtowicz et al., 2007) and AUC experiments on a few select isoforms (Wu et al., 2012).

### Cis interactions

Despite early evidence that cis interactions are promiscuous, the data reported here indicate that this generalization needs to be significantly refined. Functional mutagenesis studies have already established that alternate α cPcdhs and the C-type γC4 do not form intrasubtype cis interactions and can only reach the cell surface when mediated by heterophilic cis interactions with members of other subtype families (Goodman et al., 2017; Thu et al., 2014). The data presented in Figure 4 indicate that this is an extreme example of quite general behavior: intrasubtype cis interactions are invariably weaker than intersubtype interactions. However, unlike α cPcdhs, most cPcdhs can reach the cell surface on their own. This includes β1, all γA-Pcdhs, and γC3 which do not form measurable homodimeric cis interactions in our solution-based AUC experiments. We have attributed this to their presence on the restricted 2D surface of membranes which can promote cis dimerization (Wu et al., 2013) whereas biophysical experiments are carried out in a 3D solution environment (Goodman et al., 2016a). (There may of course be other, still undetermined, factors involved in cPcdh cell surface transport [Phillips et al., 2017].) Therefore, although our biophysical experiments demonstrate that intrasubtype cis interactions are comparatively weak and, in some cases undetectable in solution, intrasubtype cis dimers likely assemble when constrained in more native membrane environments. As such, while α cPcdhs and γC4 are obligate participants in cis heterodimers, at least in their cell surface transport, our data show that the remaining cPcdhs are preferentially, although not exclusively, participants in cis heterodimers.

The cis-binding preferences indicated by our data can be largely understood in terms of the asymmetric interface discussed above. Specifically, different isoforms preferentially form one side of the cis dimer: for example, the EC6-only side for cPcdh-γA4 and the EC5–6 side for cPcdh-γC3. Homodimerization requires participation of single isoform on both sides of an interface posing challenges in the optimization of binding affinities since, in some cases, the same residue must participate in different intermolecular interactions. Given significant sequence conservation in all members of an alternate cPcdh subfamily (Figure 4—figure supplement 3) even intrasubfamily heterophilic interactions are more difficult to optimize relative to intersubfamily heterodimerization where there are no constraints on the two interacting surfaces. Additionally, the robust cell surface delivery of many cPcdhs in cells expressing only a single isoform also suggests that all carrier isoforms – β-, γA-, and γB-cPcdhs, plus C-types αC2, γC3, and γC5 – can fill both the EC6 and EC5–6 roles, as cis dimer formation is thought to be required for cell surface export (Goodman et al., 2017; Goodman et al., 2016a; ; Thu et al., 2014). Therefore side preferences are most likely not absolute for carrier cPcdh isoforms and may vary among individual isoform and/or subtype pairings.

### Functional implications of cPcdh interactions

The functional role of precise trans homophilic specificity in ensuring high-fidelity discrimination between neuron self and nonself has been discussed previously (Rubinstein et al., 2017; Rubinstein et al., 2015) and is summarized above. It is an essential feature of the chain-termination model. The role of promiscuous cis interactions can also be understood in terms of this model in that cis promiscuity enables the formation of a large and diverse set of cis dimers that can only form long molecular zippers when all isoforms are matched. However, the results of this study reveal strong preferences for intersubgroup heterophilic interactions whose biological rationale is uncertain. cPcdhs from the three subfamilies have been shown to act cooperatively in certain neuronal contexts although whether this relates to their cis interactions is unknown (Hasegawa et al., 2016; Ing-Esteves et al., 2018).

One possible advantage of weak homophilic cis interactions would be to ensure that once reaching the cell surface a diverse set of cis dimers forms. This explanation implicitly assumes that most isoforms (except for α-Pcdhs and γC4) reach the surface as homodimers that must then quickly dissociate and form more stable heterodimers. Another explanation posits that homotypic zippers consisting solely of cis homodimers are kinetically easier to form than heterotypic zippers since in a homotypic zipper, either ‘wing’ of the new cis dimer can form trans interactions with the wing at the chain terminus. In contrast, in a heterodimeric zipper, only one wing can form homophilic interactions with the chain terminus (Figure 1D). A preference for homotypic zippers would then reduce the diversity required in the chain-termination model since, in this model, it is essential that all isoforms be incorporated into a growing zipper. The formation of long homotypic zippers might lead to a repulsive phenotype even when mismatches are present.

However, these explanations would not fully account for interfamily heterophilic preferences. One possibility is suggested by the observation that C-types are often highly expressed compared to alternate cPcdhs, for example in Purkinje cells (Esumi et al., 2005; Kaneko et al., 2006). To ensure sufficient diversity in growing zippers, it would then be important to ensure that zippers that are formed are not overly enriched in C-type isoforms as would be accomplished through preferential heterophilic cis interactions. This same logic would also pertain to alternate cPcdhs in cases where one subfamily is more heavily expressed than another.

C-type cPcdhs have different functions than alternate cPcdhs and these are reflected in different expression patterns. For example, αC2 can be alone responsible for tiling (Chen et al., 2017). (Of note, in the chain-termination model, a completely homophilic zipper is sufficient to initiate self-avoidance facilitating tiling.) On the other hand, γC4, which has a unique and crucial role in neuronal survival (Garrett et al., 2019), requires coexpression with another cPcdh isoform for robust cell surface expression and therefore is likely unable to act in isolation (Thu et al., 2014). Furthermore, as detailed above, γC4 has a much weaker trans interaction affinity than any other cPcdh isoform measured to date, although it is still able to mediate cell aggregation when delivered to the cell surface (Thu et al., 2014). The presence of E78 appears in large part to be responsible for this weak affinity. It is unclear whether γC4’s weak trans affinity plays any functional role, although a weak homodimer interaction may facilitate extracellular interactions with other, currently unidentified, proteins. More generally, it seems likely that different intracellular interactions account for the specialized functions of C-type Pcdhs. The cytoplasmic domain plays an important role in the activation of Wnt, WAVE, and other signaling cascades (Chen et al., 2009; Fukuda et al., 2008; Keeler et al., 2015; Mah and Weiner, 2017; Onouchi et al., 2015; Pancho et al., 2020). In some cases, the cytoplasmic domains of a subset or even a single cPcdh isoform activates a specific signaling cascade. For example, cPcdh γC3 is the only isoform able to interact and inhibit Axin1, a Wnt pathway activator (Mah et al., 2016). Of note, γ-cPcdh intracellular domains consist of a C-terminal constant region common to all γ isoforms (including the three γ C-types) and a membrane-proximal variable region consisting of ~100 residues that could account for the unique intracellular interactions and signaling of individual isoforms. Additionally, it is possible that extracellular interactions to molecules from other families, such as Neuroligins, may account for some distinctions in function (Molumby et al., 2017; Steffen et al., 2021).

Overall, the results of this study demonstrate the remarkable tuning of the interactions among cPcdh family members: homophilic trans interactions are remarkably specific despite the high level of sequence identity among family members while cis interactions, though somewhat promiscuous, also appear designed to have binding preferences of still uncertain function. These binding properties match requirements of the ‘isoform-mismatch chain-termination model’ for neuronal self- vs nonself-discrimination in which all expressed cPcdh isoforms assemble into intercellular zippers formed by alternating promiscuous cis and matched trans interactions with assembly size dictated by the presence or absence of mismatched isoforms. It remains to be seen whether such assemblies can be observed in vivo and how they control downstream signaling pathways.

## Materials and methods

### Protein production and purification

cDNAs for mouse cPcdh ectodomain fragments, excluding the predicted signal sequences, were cloned into a pαSHP-H mammalian expression vector (a kind gift from Daniel J. Leahy, John Hopkins University) modified with the human binding immunoglobulin protein (BiP; MKLSLVAAMLLLLSAARA) signal sequence and a C-terminal octa-histidine tag (Rubinstein et al., 2015). The signal sequences were predicted using the SignalP 4.0 server (Petersen et al., 2011). Point mutations were introduced into cDNA constructs using the KOD hot start polymerase (Novagen) following the standard Quikchange protocol (Stratagene).

Suspension-adapted HEK293 Freestyle cells (Invitrogen) in serum-free media (Invitrogen) grown and maintained at 37°C and 10% carbon dioxide were used for protein expression. FreeStyle 293F cell line has been authenticated and verified negative for mycoplasma using PCR testing (Thermo Fisher). The plasmid constructs were transfected into cells using polyethyleneimine (Polysciences Inc) (Baldi et al., 2012). Media was supplemented with 10 mM CaCl2 4 hr after transfection. Conditioned media was harvested ~6 days after transfection and the secreted proteins were purified using batch nickel-nitrilotriacetic acid (Ni-NTA) affinity chromatography followed by size exclusion chromatography over Superdex 200 26/60 column (Cytiva) on an AKTA pure fast protein liquid chromatography system (Cytiva). Purified proteins were concentrated to >2 mg/ml in 10 mM Tris–Cl, pH 8.0, 150 mM NaCl, 3 mM CaCl2, and 100–250 mM imidazole pH 8.0 and stored at 4°C for short-term use or flash frozen in liquid nitrogen for long-term storage at −80°C.

Constructs encoding biotinylated cPcdh fragments for immobilization in SPR experiments were prepared by insertion of an Avi-tag (GLNDIFEAQKIEWHE)-encoding sequence between the octa-histidine tag and stop codon. These were cotransfected with a plasmid encoding the biotin-Ligase BirA from E. coli (Lys2–Lys321) with a BiP signal sequence and a C-terminal endoplasmic reticulum-retention signal (DYKDEL) (Barat and Wu, 2007). The expression and BirA plasmids were mixed at a 9:1 ratio for transfection and 50 μM Biotin (Sigma) was added to the media 4 hr post-transfection. Purification was carried out exactly as for the nonbiotinylated constructs and biotinylation was confirmed by western blot using NeutrAvidin-HRP (Thermo Fisher).

### Sedimentation equilibrium AUC

<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Imidazole pH 8.0 (mM)</th>
      <th>Spin speeds (rpm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>α4 EC1–5</td>
      <td>100</td>
      <td>9000, 11,000, 13,000, 15,000</td>
    </tr>
    <tr>
      <td>α7 EC1–5 L301R</td>
      <td>100</td>
      <td>9000, 11,000, 13,000, 15,000</td>
    </tr>
    <tr>
      <td>α12 EC1–5 (poorly behaved)</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γB4 EC1–5</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γB5 EC1–4-AVI</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC5 EC1–5 S116R</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4</td>
      <td>100</td>
      <td>9000, 11,000, 13,000, 15,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4-AVI tag</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 S117I</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 L125P</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 E369K</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 Y371F</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N/S117I (precipitates)</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N/E369K</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 S117I/L125P</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N/S117I/L125P</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N/S117I/E369K</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N/E369K/Y371F</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β6 EC1–4 R41N/S117I/L125P/ E369K/Y371F</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>β1 EC3–6</td>
      <td>200</td>
      <td>12,000, 16,000, 20,000, 24,000</td>
    </tr>
    <tr>
      <td>β6 EC1–6</td>
      <td>250</td>
      <td>9000, 11,000, 13,000, 15,000</td>
    </tr>
    <tr>
      <td>β9 EC3–6</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γA3 EC3–6</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γA9 EC3–6</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γB7 EC3–6 A570R</td>
      <td>200</td>
      <td>13,000, 17,000, 21,000, 25,000</td>
    </tr>
    <tr>
      <td>αC2 EC3–6-AVI tag</td>
      <td>200</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC5 EC2–6</td>
      <td>250</td>
      <td>9000, 11,000, 13,000, 15,000</td>
    </tr>
    <tr>
      <td>γC4 EC1–4</td>
      <td>250</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC4 EC1–4 D290A</td>
      <td>250</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC4 EC1–4 D290N</td>
      <td>250</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC4 EC1–4 E78A</td>
      <td>250</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC4 EC1–4 E78Q</td>
      <td>250</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
    <tr>
      <td>γC4 EC1–4 S344R</td>
      <td>250</td>
      <td>11,000, 14,000, 17,000, 20,000</td>
    </tr>
  </tbody>
</table>

Experiments were performed in a Beckman XL-A/I analytical ultracentrifuge (Beckman-Coulter, Palo Alto CA, USA), utilizing six-cell centerpieces with straight walls, 12-mm path length and sapphire windows. Protein samples were dialyzed overnight and then diluted in 10 mM Tris–Cl, pH 8.0, 150 mM NaCl, 3 mM CaCl2 with 100–250 mM imidazole pH 8.0, as detailed in the above table. The samples were diluted to an absorbance of 0.65, 0.43, and 0.23 at 10 and 280 nm in channels A, B, and C, respectively. For each sample, buffer was used as blank. The samples were run in duplicate at four speeds as detailed in the above table. The lowest speed was held for 20 hr then four scans were conducted with 1-hr interval, the subsequent three speeds were each held for 10 hr followed by four scans with 1-hr interval each. Measurements were taken at 25°C, and detection was by UV at 280 nm or interference. Solvent density and protein v-bar at both temperatures were determined using the program SednTerp (Alliance Protein Laboratories, Corte Cancion, Thousand Oaks, CA, USA). The molecular weight of each protomer used in AUC experiments was determined by MALDI mass spectrometry. For the calculation of dimeric KD and apparent molecular weight, all data were used in a global fit, using the program HeteroAnalysis (http://www.biotech.uconn.edu/auf). The calculation of the tetramer KDs was done with the program Sedphat (http://www.analyticalultracentrifugation.com/sedphat/index.htm).

### SPR binding experiments

SPR-binding experiments were performed using a Biacore T100 biosensor equipped with a Series S CM4 sensor chip, immobilized with NeutrAvidin over all four flow cells. NeutrAvidin immobilization was performed in HBS-P (HEPES-Buffered Saline-P20) buffer, pH 7.4 at 32°C, over all four surfaces using amine-coupling chemistry as described in Katsamba et al., 2009, resulting in approximately 10,000 RU of NeutrAvidin immobilized (Katsamba et al., 2009). Binding experiments were performed at 25°C in a running buffer containing 10 mM Tris–Cl, pH 8.0, 150 mM NaCl, 3 mM CaCl2, 20 mM imidazole, 0.25 mg/ml BSA (Bovine Serum Albumin), and 0.005% (vol/vol) Tween-20 unless otherwise noted.

C-terminal biotinylated fragments were tethered over individual NeutrAvidin-immobilized flow cells (shown in the left column of each Figures 2, 4,, 5C, Figure 2—figure supplement 1, Figure 2—figure supplement 2B, Figure 4—figure supplement 1, and Figure 5—figure supplement 2B) at 2300–3000 RU, depending on the experiment, using a flow rate of 20 μl/min. A NeutrAvidin-immobilized flow cell was used as a reference in each experiment to subtract bulk refractive index changes. The analytes tested in each experiment are listed at the top row. All analytes (with exceptions for the cis-interacting pairs γC33–6/β93–6, in both orientations, and β61–6/γC33–6 in Figure 4A, discussed below) were tested at six concentrations ranging between 24, 8, 2.667, 0.889, 0.296, and 0.099 μM, prepared using a threefold dilution series. γC33–6 binding over β93–6 (Figure 4A) was tested at five concentrations from 8 to 0.099 μM.

For all experiments, analyte samples were injected over the captured surfaces at 50 μl/min for 40 s, followed by 180 s of dissociation phase, a running buffer wash step and a buffer injection at 100 μl/min for 60 s. Protein samples were tested in order of increasing concentration, and within the same experiment the entire concentration series was repeated to confirm reproducibility. Every three binding cycles, buffer was used as an analyte instead of a protein sample to double reference the binding responses by removing systematic noise and instrument drift. The resulting binding curves were normalized for molecular weight differences according to data provided by mass spec for each molecule. The data were processed using Scrubber 2.0 (BioLogic Software). To provide an estimate of the number of possible heterophilic binding pairs, we have used a cutoff of 40 RU, which is the lowest signal that can be observed for a homodimeric cis fragment pair, γB23–6.

In Figure 4A, β61–6 and β93–6 were tested over γC33–6 at six concentrations ranging from 900 to 3.7 nM, which is 27-fold lower than the other interactions, prepared using a threefold dilution series in a running buffer containing increased concentrations of imidazole (100 mM) and BSA (0.5 mg/ml) to minimize nonspecific interactions. For these two interactions, although analyte samples were injected over the captured surfaces at 50 μl/min for 40 s, the dissociation phase was monitored for 300 s to provide additional time for complex dissociation. Nevertheless, higher analyte concentrations produced binding profiles that were not reproducible, most likely due to the fact that bound complexes could not dissociate completely at these higher concentrations.

For the calculation of heterophilic KDs for the monomeric cis fragments β13–6, γA43–6, γA93–6, and γC33–6 over each of the six surfaces, except β93–6, the duplicate binding responses were fit globally, using an 1:1 interaction model and a single KD was calculated as the analyte concentration that would yield 0.5 Rmax and a fitting error, indicated in brackets. KDs lower than 24 μM were calculated using an independent Rmax. For KDs greater 24 μM, the Rmax was fixed to a global value determined by the Rmax of a different cPcdh analyte tested over the same surface during the same experiment that showed binding above 50% and therefore produced a more accurate Rmax. For KDs > 50 μM, a lower limit is listed since at the analyte concentrations used (0.098–24 μM), accurate KDs could not be determined, even when the Rmax is fixed. NB (no binding) represents interactions that did not yield any binding signal. The binding curves of γC33–6 over the β93–6 did not come to equilibrium during the time-course of the experiment, so a kinetic analysis was performed to calculate a KD (Figure 4—figure supplement 1A). Binding of γC33–6 was tested using a concentration range of 900–0.411 nM prepared using a threefold dilution series in a running buffer containing increased concentrations or imidazole (100 mM) and BSA (0.5 mg/ml) to minimize any nonspecific interactions. Protein samples were injected over the captured surfaces at 50 μl/min for 90 s, followed by 420 s of dissociation phase, a running buffer wash step and a buffer injection at 100 μl/min for 60 s. Protein samples were tested in order of increasing concentration in triplicate to confirm reproducibility. Every three binding cycles, buffer was used as an analyte instead of a protein sample to double reference the binding responses by removing systematic noise and instrument drift. The binding data were analyzed using an 1:1 interaction model to calculate the kinetic parameters and the KD.

### K562 cell aggregation assays

Full-length cPcdhs β6 and β8 cDNAs were cloned into the pMax expression vectors encoding C-terminal mCherry- or mVenus-tagged cPcdh proteins, then transfected into K562 cells (ATCC CCL243) as previously described (Goodman et al., 2017; Thu et al., 2014). K-562 bone marrow chronic myelogenous leukemia cell line has been authenticated and verified negative for mycoplasma using PCR testing (ATCC). Point mutants were generated using the QuikChange method (Stratagene). In brief, K562 cells were cultured at 37°C with 5% CO2 in Dulbecco’s modified Eagle medium with GlutaMAX (GIBCO) supplemented with 10% fetal bovine serum and 1% penicillin–streptomycin for 2 days. Next, cells were counted, centrifuged, and resuspended at a density of 1.5 × 104 cells/μl in SF Cell Line 4D-Nucleofector Solution SF with supplement according to the manufacturer’s instructions (Lonza). 2 μg of each Pcdh expression construct were transfected into 20 μl of the K562 cell suspension by electroporation using an Amaxa 4D-Nucleofector (Lonza). Transfected cells were transferred to a 24-well plate in 500 μl of medium per well and incubated overnight at 37°C and 5% CO2. Cells then were mixed, reincubated with gentle rocking for 4 hr, then imaged with an Olympus IX73 fluorescent microscope to determine the extent of aggregation.

### Size exclusion-coupled multiangle light scattering

SEC-MALS experiments were performed using a Superdex 200 Increase 3.2/300 size exclusion column on an AKTA FPLC system (Cytiva) coupled to inline static light scattering (Dawn Heleos II, Wyatt Technology), differential refractive index (Optilab rEX, Wyatt Technology), and UV detection. Purified cPcdh proteins were diluted to 18 μM in running buffer (150 mM NaCl, 10 mM Tris–Cl, pH 8, 3 mM CaCl2, 200 mM imidazole, pH 8) and 50 or 100 μl samples were run at a flow rate of 0.5 ml/min at room temperature. Mixtures of cPcdh fragments were prepared in the same buffer at final concentrations of 18 μM for each protein and run under the same conditions. Data were analyzed using ASTRA software (Wyatt Technologies).

During SEC-MALS experiments, a dimer/monomer equilibrium is established as proteins move through the size exclusion chromatography column, which is influenced by the KD of the interaction. The concentrations used in the current experiments (18 μM for each cPcdh fragment), although above the KD of 3 μM for the γC3/γA4 cis interaction, are not sufficiently high for all the cis fragments to be bound into heterodimers, leaving a significant population of molecules as monomers, resulting in apparent molecular weights of ~76 kDa for the dimeric species compared to the predicted molecular weight for a dimer of ~108 kDa.

### X-ray crystallography

Crystallization screening of γC41–4 using the vapor diffusion method yielded two protein crystal forms: The first crystal form crystals were grown using a protein concentration of 7 mg/ml in 10% (wt/vol) PEG8000, 20% ethylene glycol, 10% Morpheus Amino Acids (Molecular Dimensions), and 0.1 M Morpheus Buffer System 2 (Hepes/MOPS buffer; Molecular Dimensions), pH 7.5. No additional cryoprotection was required for this crystal form. The second crystal form crystals were grown using a protein concentration of 7 mg/ml in 1 M LiCl, 0.1 M Mes pH 6.0, and 10% (wt/vol) PEG 6000. The crystal used for data collection was cryoprotected in the crystallization condition plus 30% (wt/vol) glycerol. X-ray diffraction data for each crystal form were collected at 100 K from single crystals at Northeastern Collaborative Access Team (NE-CAT) beamline 24ID-E at the Advanced Photon Source, Argonne National Laboratory.

### γC41–4 crystal form 1: diffraction anisotropy and pseudosymmetry

The X-ray diffraction data for the first crystal form showed strong diffraction anisotropy, with relatively strong diffraction along c* and much weaker diffraction along a* and b* (Figure 3—figure supplement 1A). These data were therefore truncated using ellipsoidal limits with using a 3.0 F/sigma cutoff along each of the three principal crystal axes as implemented in the UCLA Diffraction Anisotropy Server (Strong et al., 2006) to 4.6/3.9/3.5 Å. The completeness within the applied ellipsoidal resolution limits was 96.8% (Figure 3—source data 1).

### γC41–4 crystal form 1: crystal structure phasing and refinement

The γC41–4 crystal structure was solved by molecular replacement using Phaser (McCoy et al., 2007), implemented in CCP4 (Winn et al., 2011). The γC5EC1–3 crystal structure (PDB: 4ZPO) modified using a sequence alignment to γC4 with Phenix’s MRage program (Liebschner et al., 2019) was used as a search model. Following an initial round of rigid body refinement in Phenix (Liebschner et al., 2019) the EC domain 4 from the α7EC1–5 crystal structure (PDB: 5DZV) was manually placed into the electron density map, using structural alignment to the EC1–3 regions as a guide. The resulting model was subjected to a further round of rigid body refinement. At this stage there was clear difference density for the interdomain calcium ions and covalently linked glycans not present in the models. Iterative model building using Coot (Emsley et al., 2010) and maximum-likelihood refinement using Phenix (Liebschner et al., 2019) was subsequently conducted. The higher resolution (2.4 Å) crystal form two crystal structure (see below) was used as a reference model in later rounds of iterative model building and refinement to guide the local geometry choices in this lower resolution structure. Final refinement statistics are given in Figure 3—source data 1.

### γC41–4 crystal form 2: data processing, phasing, and refinement

The γC41–4 crystal form two dataset was indexed using XDS (Kabsch, 2010) and scaled using AIMLESS (Evans and Murshudov, 2013). The data were spherically truncated with high resolution limit of 2.4 Å. Data collection statistics are given in Figure 3—source data 1.

The γC41–4 crystal form two crystal structure has two molecules in the asymmetric unit was solved by molecular replacement using Phaser (McCoy et al., 2007), implemented in Phenix (Liebschner et al., 2019), using the EC2–3 portion of the trans dimer from the γC41–4 crystal form one crystal structure early in refinement as a search model. The molecular replacement solution was then subjected to an initial round of rigid body refinement using Phenix, followed by two rounds of model building in Coot (Emsley et al., 2010) and maximum-likelihood refinement in Phenix. The two EC4 domains were then manually placed in the electron density and subjected to rigid body refinement. Following a further two iterative rounds of model building and refinement the two EC1 domains were manually placed. Iterative model building and refinement continued yielding the final crystal structure whose statistics are given in Figure 3—source data 1.

### Structure analysis

Buried surface areas were calculated using ‘Protein interfaces, surfaces and assemblies’ service (PISA) at the European Bioinformatics Institute (http://www.ebi.ac.uk/pdbe/prot_int/pistart.html) (Krissinel and Henrick, 2007) and are given as the change in accessible surface area over both protomers. Root mean square deviations over aligned Cα atoms (RMSDs) between structures were calculated using Pymol (Schrödinger, LLC). Crystal structure figures were made using Pymol (Schrödinger, LLC).

### Sequence analysis

Multiple sequence alignments were generated using Clustal Omega (Sievers et al., 2011) and visualized using ESPript3.0 (Robert and Gouet, 2014). Sequence logos were generated from multiple sequence alignments using WebLogo3 (Crooks et al., 2004).

### Amino acid sequence alignment of cPcdhs γB7, γA4, and γC3 EC1–6 regions

CLUSTAL O(1.2.4) multiple sequence alignmentγB7   -QPVRYSIPEELDRGSVVGKLAKDLGLSVLEVSARKLRVS--AEKLHFSVDSESGDLLVK     57γA4   -EQIRYSVPEELERGSVVGNLAADLGLEPGKLAERGVRIVSRGKTQLFALNPRSGSLVTA     59γC3   STIIHYEILEERERGFPVGNVVTDLGLDLGSLSARRLRVVSGASRRFFEVNWETGEMFVN    60::*.: ** :** **::. ****. .:: * :*:  .. * :: .:*.:..γB7   DRIDREQICKGRRKCELQLEAVLENPLNIFHVVVEIEDVNDHAPQFPKDEINLEISESDS    117γA4   GRVDREGLCDRSPKCTANLEILLEDKVRILAIEVEIIDVNDNAPSFGAQQREIKVAESEN    119γC3   DRLDREELCGTLPSCTVTLELVVENPLELFSAEVVVQDINDNNPSFPTGEMKLEISEALA    120.*:*** :*   .* **  ::*: :.::  * : *:**: *.* :  : :::: *:γB7   PGARTILESAKDLDIGMNSLSKYQLSPNDYFLLLVKDNPDGSKYPELELQKMLDREAEST    177γA4   PGTRFPLPEAFDLDIGVNALQGYQLSSNDHFSLDVQSGPDGIKYPELVLENALDREEEAV    179γC3   PGTRFPLESAHDPDVGSNSLQTYELSHNEYFALRVQTREDGTKYAELVLERALDWEREPS   180**:* * .* * *:* *:*. *:** *::* * *: ** ** ** *:. ** * *γB7   HHLMLTAVDGGDPPRTGTTQLRIRVVDANDNRPVFSQDVYRVRLPEDLPPGTTVLRLKAM    237γA4   HHLVLTAFDGGDPVRSGTATIQVTLVDTNDNAPVFTQPEYHISVKENLPVGTRLLTIKAT    239γC3   VQLVLTALDGGTPARSATLPIRITVLDANDNAPAFNQSLYRARVREDAPPGTRVAQVLAT    240:*:***.*** * *:.* ::: ::*:*** *.*.* *: : *: * ** : : *γB7   DQDEGINAEFTYSFLGV-ANK--AQFSLDPITGDIVTRQSLDFEEVEQYTIDVEAKDRGS    294γA4   DPDEGVNGEVTYSFRNV-REKISQLFQLNSLTGDITVLGELDYEDSGFYDVDVEAHDGPG    298γC3   DLDEGLNGEIVYSFGSHNRAGVRELFALDLVTGVLTIKGRLDFEDTKLHEIYIQAKDKGA    300* ***:*.*..***.        * *: :** :.  **:*:  : : ::*:* .γB7   --LSSQCKVIIEVLDENDNRPEIIITSLSDQISEDSPSGTVVALFKVRDRDSGENAEVMC    352γA4   --LRARSKVLVTVLDVNDNAPEVTVTSLTSSIQEASSPGTVIALFNVHDSDSGENGLVTC    356γC3   NPEGAHCKVLVEVVDVNDNAPEITVTSVYSPVPEDAPLGTVIALLSVTDLDAGENGLVTC    360::.**:: *:* *** **: :**: . : * : ***:**:.* * *:***. * *γB7   SLSGNNPFKIHSSSNNYYKLVTDSILDREQTPGYNVTITATDRGKPPLSSSTTITLNVAD    412γA4   SIPDNLPFRLEKTYGNYHRLLIHRTLDREEVSDYNITITATDQGTPPLSTETYISLQVVD    416γC3   EVPPGLPFSLTSSLKNYFTLKTSAALDRETMPEYNLSITARDSGIPSLSALTTVKVQVSD    420.: . ** : .: **. *     ****   **::*** * * * **: * :.::* *γB7   VNDNAPVFQQQAYLINVAENNQPGTSITQVKAWDPDVGSNGLVSYSIIASDLEPKALSSF    472γA4   INDNPPTFTHASYSAYIPENNPRGASILSITAQDPDSGENAQVIYSLSEDTIQGAPMSSY     476γC3   INDNPPQSSQSSYDVYVEENNLPGVPILNLSVWDPDAPPNARLSFFLLEPGAETGLVSRY    480:*** * : :*  : *** *. *   .:... *** *. : : :    :   :* :γB7   VSVNQDSGVVYAQRAFDHEQIRSFQLTLQARDQGSPALSANVSMRVLVDDRNDNAPRVLY    532γA4   VSINSNTGVLYALRSFDYEQFQDLKLLVTARDSGTPPLSSNVSLSLSVLDQNDNTPEILY    536γC3   FTINRDNGVLTTLVPLDYEDQREFQLTAHINDGGTPVLATNISVNVFVTDRNDNAPQVLY    540.::* :.**: :  :*:*: :.::*   .* *:* *::*:*: : * *:***:*.:**γB7   PTLEPDGSALFDMVPRAAEPGYLVTKVVAVDADSGHNAWLSYHVLQASDPGLFSLGLRTG    592γA4   PTIPTDGSTGVELTPRSADPGYLVTKVVAVDKDSGQNAWLSYRLLKASEPGLFSVGLHTG    596γC3   PR---PGQSSVEMLPRGTAAGHVVSRVVGWDADAGHNAWLSYSLLGAPNQSLFAVGLHTG    597*   *.: .:: **.: *::*::**. * *:*:****** :* * : .**::**:**γB7   EVRTARALSDKDAARQRLLVAVRDGGQPPLSATATLLLVFADSLQE                  638γA4   EVRTARALLDRDALKQSLVVTVQDHGQPPLSATVTLTIAVSDNIPD                  642γC3   QISTARPIQDTDSPRQILTVLISDSGEPLLSTTATLTVSVTEESPE                  643:: *** : * *: :* * * : * *:* **:*.** : .::.  :

### Structure-based sequence analysis of the γA4/γC3 interaction

Since both γA43–6 and γC33–6 are monomeric in solution but form a robust heterodimer when mixed (in SPR, AUC, and SEC-MALS) we hypothesized that these molecules might have opposing cis interaction side preferences. To facilitate hypothesis generation on the nature of their cis heterodimer interaction we modeled the two possible γA4/γC3 cis dimers: one with γA4 occupying the EC6-only position and γC3 the EC5–6 position; and the second with γC3 in the EC6-only position and γA4 in the EC5–6 position. To do this the monomeric γA4EC3–6 crystal structure (PDB: 5SZQ) was structurally superimposed over EC6 domains with the EC6-only protomer from the γB7EC3–6 cis dimer crystal structure (PDB: 5V5X; RMSD 0.7 Å over 91 aligned Cαs) or over EC5–6 domains with the EC5–6 protomer (RMSD 1.0 Å over 194 aligned Cαs). Since γA4 and γB7 are so structurally similar in their EC5–6 regions modeling γA4’s cis interactions in this manner as a basis for hypothesis generation seemed reasonable. The only region of significant structural deviation within the EC5–6 regions between γA4 and γB7 is in the EC6 A–A′ loop region which has a peripheral role in the EC6-only protomer interface. For modeling γC3 we used computational mutagenesis of the γB7 structure selecting the best-fit rotamer for each amino acid from the Dunbrack rotamer library (Shapovalov and Dunbrack, 2011), implemented in UCSF Chimera (Pettersen et al., 2004). No energy minimization was conducted and the models are intended only for use in hypothesis generation.

### Cis interface mutants

Our studies of Pcdh cis interactions we have found that mutagenesis of the cis interface commonly has a deleterious impact on protein expression levels in our system (Goodman et al., 2017). We assume this is because cis interaction is required for robust cell surface delivery/secretion (Thu et al., 2014), although this has not been specifically addressed in our HEK293 protein expression system.

To test our structure-guided hypotheses regarding γA4 and γC3s′ cis interactions and side preferences as we tried to make a number of different cis interface mutants and were able to obtain four different mutants (see table below). Since protein yields were generally too low for AUC and SPR, MALS was used to study the impact of these mutants on γA4/γC3 cis dimer formation.

<table>
  <thead>
    <tr>
      <th>Mutant protein(γB7 numbering given in parentheses)</th>
      <th>Cis interface side targeted</th>
      <th>Protein expression in 25 ml test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>γC3 EC3–6 Y540G (Y532G equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>γC3 EC3–6 V560D (L555D equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>γC3 EC3–6 V565R (V560R equivalent)</td>
      <td>EC6-only</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>γC3 EC3–6 A575R (A570R equivalent)</td>
      <td>EC5–6</td>
      <td>No</td>
    </tr>
    <tr>
      <td>γC3 EC3–6 R563K (K558R equivalent)</td>
      <td>Both</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>γA4 EC3–6 Y536G (Y532G equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>γA4 EC3–6 L559D (L555D equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>γA4 EC3–6 V564R (V560R equivalent)</td>
      <td>EC6-only</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>γA4 EC3–6 A574R (A570R equivalent)</td>
      <td>EC5–6</td>
      <td>No</td>
    </tr>
    <tr>
      <td>γA4 EC3–6 K562R (K558R equivalent)</td>
      <td>EC6-only</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>β1 EC3–6 V563R (V560R equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>β1 EC3–6 S573R (A570R equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>β1 EC3–6 K561R (K558R equivalent)</td>
      <td>EC5–6</td>
      <td>No</td>
    </tr>
    <tr>
      <td>β9 EC3–6 V563R (V560R equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>β9 EC3–6 A573R (A570R equivalent)</td>
      <td>EC6-only</td>
      <td>No</td>
    </tr>
    <tr>
      <td>β9 EC3–6 K561R (K558R equivalent)</td>
      <td>EC5–6</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
