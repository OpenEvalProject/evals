# Design of biochemical pattern forming systems from minimal motifs

## Authors

- Philipp Glock<sup>1</sup> ([ORCID: 0000-0002-0238-2634](https://orcid.org/0000-0002-0238-2634))
- Fridtjof Brauns<sup>2</sup> ([ORCID: 0000-0002-6108-9278](https://orcid.org/0000-0002-6108-9278))
- Jacob Halatek<sup>2</sup> ([ORCID: 0000-0003-3211-2253](https://orcid.org/0000-0003-3211-2253))
- Erwin Frey<sup>2</sup> ([ORCID: 0000-0001-8792-3358](https://orcid.org/0000-0001-8792-3358)) †
- Petra Schwille<sup>1</sup> ([ORCID: 0000-0002-6106-4847](https://orcid.org/0000-0002-6106-4847)) †

### Affiliations

1. Max-Planck-Institute of Biochemistry Martinsried Germany
2. Arnold Sommerfeld Center for Theoretical Physics, Department of Physics Ludwig-Maximilians-Universität München München Germany
3. Center for NanoScience, Department of Physics Ludwig-Maximilians-Universität München München Germany
4. Biological Computation Group Microsoft Research Cambridge United Kingdom

† Corresponding author

## Abstract

Although molecular self-organization and pattern formation are key features of life, only very few pattern-forming biochemical systems have been identified that can be reconstituted and studied in vitro under defined conditions. A systematic understanding of the underlying mechanisms is often hampered by multiple interactions, conformational flexibility and other complex features of the pattern forming proteins. Because of its compositional simplicity of only two proteins and a membrane, the MinDE system from Escherichia coli has in the past years been invaluable for deciphering the mechanisms of spatiotemporal self-organization in cells. Here, we explored the potential of reducing the complexity of this system even further, by identifying key functional motifs in the effector MinE that could be used to design pattern formation from scratch. In a combined approach of experiment and quantitative modeling, we show that starting from a minimal MinE-MinD interaction motif, pattern formation can be obtained by adding either dimerization or membrane-binding motifs. Moreover, we show that the pathways underlying pattern formation are recruitment-driven cytosolic cycling of MinE and recombination of membrane-bound MinE, and that these differ in their in vivo phenomenology.

## Introduction

Patterns are a defining characteristic of living beings and are found throughout all kingdoms of life. In the last years, it has become increasingly clear that protein patterns formed by reaction–diffusion mechanisms are responsible for a large range of spatiotemporal regulation (Green and Sharpe, 2015). Such processes allow organisms and cells to achieve robust intracellular patterning rooted in basic physical and chemical principles.

However, there is a lack of mechanistic understanding of the relationship between biomolecular features of proteins, that is their interaction domains and conformational states, and the collective properties of protein networks resulting in self-organized pattern formation. In other words, it is often unclear what exactly constitutes a mechanism of self-organization on the biochemical level. A major question is to what degree system-level biological functions, for example geometry sensing or length-scale selection, depend on particular biomolecular features. Some of these features may be essential for function, others may be irrelevant or redundant. The ability to unravel this feature–function relationship crucially depends on our ability to reconstitute biochemically distinct minimal systems experimentally and to compare these minimal variants to corresponding quantitative theoretical models. The key merit of such a combined approach is the ability to dissect different network architectures and also explore a broad range of reaction rates, and thereby uncover biomolecular mechanisms for system-level properties.

Here, we address this feature-function relationship in the context of a fairly well-understood biological pattern-forming system: the Min-protein system of Escherichia coli. All its components are known – only two proteins are needed to form the pattern (MinD and MinE) – and the system has been successfully reconstituted in an easily malleable in vitro system (Loose et al., 2008; Ivanov and Mizuuchi, 2010; Vecchiarelli et al., 2014; Caspi and Dekker, 2016; Kretschmer et al., 2017). In the bacterial cell, this system contributes to the positioning of FtsZ, a key component of the division ring, at mid-cell. Two proteins, MinD and MinE, oscillate between the cell poles and thereby form a concentration gradient with a minimum at mid-cell. MinC, piggybacking on MinD, consequently inhibits FtsZ polymerization at the poles and thus positions the Z-ring in the middle.

Even though the Min protein system seems simple at first glance, there is much (and biologically relevant) complexity within the protein domain sequences and structures, and hence in the interaction between proteins. MinD is an ATPase which is believed to dimerize upon ATP-binding, raising its membrane affinity via the C-terminal membrane targeting sequence (MTS) (Lackner et al., 2003; Hu et al., 2002; Szeto et al., 2003). Bound to the membrane, MinD recruits further MinD-ATP, as well as its ATPase-activating protein MinE, which together form membrane-bound MinDE complexes (Hu and Lutkenhaus, 2001; Hu et al., 2002). MinE stimulates MinD's ATPase activity, thereby initiating disintegration of MinDE complexes and subsequent release of MinE and ADP-bound MinD into the cytosol. MinE, although only 88 amino acids in length, is a biochemically complex protein. It is found as a dimer in two distinct conformations (Pichoff et al., 1995; Park et al., 2011): While diffusing in the cytoplasm, both the N-terminal MTS and the sequence directly interacting with MinD are buried within the protein. Upon sensing membrane-bound MinD, these features are released, which allows interaction with both the membrane and MinD (Park et al., 2011).

In summary, MinE exhibits four distinct functional features: activating MinD's ATPase, membrane binding, dimerization, and a switch between an open, active and a closed, inactive conformation. The roles of these distinct functional features of MinE for pattern formation have previously been studied and discussed in the literature (Vecchiarelli et al., 2016; Kretschmer et al., 2017; Denk et al., 2018). It has been shown that MinE’s conformational switch is not essential for pattern formation, but conveys robustness to the Min system, as it allows pattern formation over a broad range of ratios between MinE and MinD concentrations (Denk et al., 2018). Furthermore, membrane binding of MinE was found to be non-essential for pattern formation (Kretschmer et al., 2017). These previous studies essentially retained the structure of MinE, predominantly mutating single residues.

Here, we chose a more radical strategy, in order to attempt a minimal design of fundamental modules towards protein pattern formation from the bottom-up. Specifically, we reduced MinE to its bare minimum function: binding to MinD, and thereby catalyzing MinD’s ATPase activity. We then reintroduced additional features—membrane binding and dimerization—one by one in a modular fashion, to study their specific role in pattern formation. This approach allowed us to identify the essential biochemical modules of MinE and show that these facilitate two biochemically distinct mechanisms of pattern formation. We further analyzed these mechanisms in terms of reaction–diffusion models using theoretical analysis and numerical simulation. In particular, we show that the dimerization-driven mechanism is likely to be the dominant one for in in vivo pattern formation.

## Results and discussion

Full flexibility and control over all parameters was achieved by reconstituting purified Min proteins and peptides in an in vitro well setup consisting of a glass-supported lipid bilayer with a large, open reservoir chamber (see Materials and methods section for further details). To minimize the complexity of MinE in this reconstituted experimental system, we removed all sequences not in direct contact with MinD, keeping only 19 amino acids (13–31, further referred to as minimal MinE peptide) (Figure 1). In agreement with previous studies (Loose et al., 2008; Glock et al., 2018a), we observed that the native in vitro Min system, consisting of MinD and full-length MinE, forms traveling (spiral) waves (see Figure 2a) and (quasi-)stationary patterns. In contrast, we did not observe pattern formation for the reconstituted system containing the minimal MinE peptide in the nanomolar to low micromolar range (see Figure 2b), suggesting that it lacks essential molecular features for pattern formation. Instead, membrane binding of MinD was dominant even for high concentrations of up to 20 μM of the minimal MinE peptide. We next tried to rescue pattern formation capability by re-introducing biomolecular features of MinE in a modular fashion.

![Figure 1.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig1-v2.jpg)

**Figure 1.:** While MinE has the core function to stimulate MinD’s ATPase, three additional properties help MinE to facilitate the emergence of spatiotemporal patterns. We show that two of these properties, dimerization and membrane targeting, can be modularly added to a minimal MinE peptide to facilitate pattern formation.

![Figure 2.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig2-v2.jpg)

**Figure 2.:** (a) MinD and MinE self-organize to form evenly spaced travelling waves when reconstituted on flat lipid bilayers. (b) The minimal MinE peptide capable of ATPase stimulation is MinE(13-31); it does not facilitate pattern formation. (c) The fragments MinE(1-31) and MinE(2-31)-sfGFP contain the membrane-targeting sequence (MTS) in addition to the ATPase stimulation domain. Substituting MinE with these constructs leads to pattern formation; see Figure 2—video 1–3. (d) Fusing the ATPase stimulation domain MinE(13-31) with dimerization domains (we tested Fos, Jun, or GCN-4) facilitates pattern formation in the absence of the MTS. (e) Combining membrane targeting and dimerization in a single construct produces quasi-stationary patterns. (Concentrations and proteins used: (a) 1 μM MinD, 6 μM MinE-His; (b) 1.2 μM MinD, 50 nM MinE(13-31); (c) 1.2 μM MinD, 50 nM MinE(1-31); scalebars = 300 μM; (d) 1 μM MinD, 100 nM MinE(13-31)-Fos; (e) 1.2 μM MinD, 100 nM MinE(1-31)-GCN4. In all assays, MinD is 70 % doped with 30 % Alexa647-KCK-MinD).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Overview images of the same experiment chambers as in Figure 2. (Concentrations and proteins used same as in main figure; scalebars = 1000 μm).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** MinD and the peptide MinE(1-31) or MinE(2-31)-sfGFP, respectively, were titrated to find the range in which patterns are formed. All experiments were done on SLBs consisting of DOPC:DOPG (2:1). Similar titrations for full-length MinE can be found in Glock et al. (2018a). Wild-type MinE generally forms patterns with MinD in a much larger range, going beyond 10 μM. Dashed blue lines were added by hand and highlight that there is a critical MinE-to-MinD concentration-ratio above which no patterns occur, in qualitative agreement with the theoretical results shown in Figure 3—figure supplement 2. A quantitative fit of the model to the threshold ratio of approximately 1/20 is shown in Figure 3—figure supplement 3.

Previous theoretical research has elucidated the key role of MinE cycling for the Min oscillations (Halatek and Frey, 2012). Each cycling step of MinE displaces one MinD from the membrane and thereby drives the oscillations that underlie pattern formation (Halatek et al., 2018b). Specifically, in this model, MinE is assumed to cycle between a cytosolic state and a MinD-bound state on the membrane. To facilitate pattern formation, this cytosolic-cycling mechanism requires sufficiently strong recruitment of cytosolic MinE by membrane-bound MinD (Halatek and Frey, 2012) suggesting that the recruitment rate of the minimal MinE peptide is too low. As the native MinE is a dimer, we hypothesized that dimerization might lead to increased recruitment, thus rescuing pattern formation. To test this hypothesis, we introduced dimerization back to the minimal MinE peptide by synthetically fusing it with well-described human and yeast leucine-zippers. Specifically, we cloned and expressed each construct with three different dimerization domains: Fos, Jun and GCN-4 (Figure 1) (Szalóki et al., 2015; O'Shea et al., 1989). Indeed, this modification enabled sustained pattern formation in the system (see Figure 2d). Compared to native MinDE patterns, those formed by dimerized peptides have larger wavelengths and are less coherent.

Another feature of native MinE that has been discussed in the context of pattern formation is persistent membrane binding via a membrane targeting sequence (MTS) (Loose et al., 2011). The MTS is located at positions 2–12 of the protein and allows MinE to remain membrane-bound after its interaction with MinD, that is it decreases the detachment rate of MinE. This persistent MinE-membrane binding facilitates that, after the dissociation of a MinDE complex, the freed-up MinE can bind to another MinD on the membrane, without cycling through the cytoplasm/bulk. Free, membrane-bound MinE is able to form a MinDE complex with membrane-bound MinD. As a shorthand, we will call this process membrane recombination of MinE. This process might alleviate the requirement for recruitment of MinD from the cytosol by membrane-bound MinD. To test whether the persistent membrane-binding of MinE can facilitate pattern formation, we added back the MTS found in native MinE (residues 2–12) to the N-terminus of the peptide. This construct, contrary to published results (Vecchiarelli et al., 2016), forms patterns with MinD. As shown in Figure 2c, the observed patterns are traveling waves with wavelengths several orders of magnitude larger than those found for the native in vitro Min system. Patterns are sustained over many hours within our assay.

Combining both features, that is adding both the MTS and a dimerization sequence to the minimal MinE peptide, resulted in (quasi-)stationary patterns, but the exact outcome depended heavily on the starting conditions of the assay (see Figure 2e). In general, patterns formed by MinD and our minimal MinE peptides do not show the same degree of order as patterns formed by the wild-type Min proteins (Glock et al., 2018a) or MinD and His-MinE (Loose et al., 2008). In particular, there is no well-controlled characteristic length scale (wavelength), and the defined spirals or stationary patterns observed in the wild-type Min system are sometimes replaced by chaotic centers as shown in Figure 2d. The chaotic behavior is especially pronounced at high MinD concentrations (in this case with a minimal MinE plus MTS and sfGFP or MinE(1-31), respectively) (Figure 2—video 1 and Figure 2—video 2).

Our experimental results suggest that two distinct features of MinE, dimerization and membrane binding, independently facilitate pattern formation of our reconstituted Min system with engineered, minimal MinE peptides. To support these conclusions and gain further insight into the mechanisms underlying pattern formation, we performed a theoretical analysis using a reaction–diffusion model that captures all of the above biomolecular features. We extended the Min ‘skeleton’ model introduced in Huang et al. (2003); Halatek and Frey (2012) by MinE membrane binding, similar to the extension considered in Denk et al. (2018). In this model, dimerization of MinE is effectively accounted for by an increased MinE recruitment rate. We performed linear stability analysis of the reaction–diffusion system to find the parameter regimes where patterns form spontaneously from a homogeneous initial state. The two-parameter phase diagram shown in Figure 3a shows that increased MinE recruitment as well as slower MinE detachment can rescue pattern formation, via two independent cycling pathways of MinE: cytosolic cycling and membrane recombination. This shows that our hypothesis that dimerization increases recruitment of MinE to MinD is consistent with the experimental findings.

![Figure 3.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig3-v2.jpg)

**Figure 3.:** (a) In vitro geometry and two-parameter phase diagram obtained by linear stability analysis, showing the pattern formation capabilities of the MinDE-system in dependence of MinE membrane-binding strength ($k_{e}^{-1}$) and MinE-recruitment rate $k_{dE}$. The regime of spontaneous pattern formation (lateral instability) is indicated in blue. The gray circle represents minimal MinE(13-31) construct, which does not facilitate self-organized pattern formation. The experimental domain additions are accounted for by respective changes of the kinetic rates, as indicated by the arrows. (Parameters: see Materials and methods; blue region: regime of pattern formation for zero MinE attachment, $k_{E}=0$; purple dashed lines: boundary of the pattern-formation regime for non-zero MinE attachment rate, $k_{E}$ = 5 μm s–1). (b) Two-parameter phase diagram obtained by numerical simulations in in vivo geometry. We find regimes of different oscillation pattern types: pole-to-pole oscillations (green squares); side-to-side oscillations (purple triangles); stripe oscillations (blue diamonds); and circular waves (red circles). Figure 3—videos 1–5 show examples each of these pattern types.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Phase diagrams in the parameter plane of total concentrations ($n_{E}$, $n_{D}$).Phase diagrams in the parameter plane of total concentrations $n_{E}$, $n_{D}$ at four points in the $(k_{e}^{-1},k_{dE})$ parameter plane. Note that in the three cases where a linearly unstable regime exists, there is critical ratio $n_{D}/n_{E}$ above which there is instability. The red dot marks the concentrations $(n_{E},n_{D})=(120,1200)$ µm s–﻿2 used in Figure 3a. (In all four cases, the MinE attachment rate was set to $k_{E}$ = 5 µm s–﻿1).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Phase diagrams showing how the range of MinE concentrations where the system is laterally unstable, depends on (a) the MinE detachment rate $k_{e}$ (at $k_{dE}=0$) and (b) the MinE recruitment rate $k_{dE}$ (at $k_{e}^{-1}=0$, i.e. $m_{e}=0$). The MinD concentration is set to $n_{D}$ = 1000 µm–2. The inset in (a) shows the $(n_{E},n_{D})$ phase diagram at $k_{dE}=0,k_{e}=0.2s^{−1}$, as an example for a parameter set that reproduces the experimentally found phase diagram for the MinE(1-31) mutant (cf. Figure 2—figure supplement 2). (The MinE attachment rate was set to $k_{E}$ = 5 µm s–﻿1.).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/48646/elife-48646-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Regions in the phase diagram are colored according to which eigenmode (green for pole-to-pole, purple for side-to-side mode) becomes unstable first for increasing cell size. Above the dashed purple line, the side-to-side mode grows faster at grown cell size ($L$ = 4 µm). Typical relationships between cell size $L$ and growth rate $\sigma$ of the pole-to-pole mode (green line) and side-to-side mode (purple line) are shown for each parameter region. Comparison to the phase diagram from numerical simulations (Figure 3b) shows that the mode becoming unstable first, not the fastest growing mode at full cell size, predicts the axis selected by the fully developed pattern. .

To test whether either or both of these two pattern-forming pathways fulfill the biological function of the Min-protein patterns, we studied pattern formation using the generalized reaction–diffusion model taking into account realistic cell geometry. In E. coli, Min oscillations have to take place along the long axis of the rod-shaped cells for correct positioning FtsZ at midcell. Interestingly, linear stability analysis (see Figure 3—figure supplement 4) shows that the membrane-recombination-driven mechanism favors short-axis oscillations which is at odds with the biological function of the Min system. Indeed, our numerical simulations show that pole-to-pole oscillations are only possible for sufficiently strong cytosolic cycling, whereas the recombination-driven mechanism leads to side-to-side oscillations (see Figure 3b). A recent theoretical study on axis-selection of the PAR system in Caenorhabditis elegans suggests that pattern formation driven by an antagonism of membrane bound proteins generically leads to short-axis selection (Gessele et al., 2018). Here, membrane-bound MinE antagonizes membrane-bound MinD via the membrane-recombination pathway. Sufficiently strong MinE-recruitment from the cytosol supersedes the membrane-recombination pathway and leads to long-axis selection (pole-to-pole oscillations) even when MinE-membrane binding is strong.

Taken together, we conclude that Min-pattern formation in vivo is driven by cytosolic cycling of MinE, because correct axis selection (pole-to-pole oscillations) is essential for cell-division of E. coli and other gram-negative bacteria. In a broader context, our results demonstrate that multiple mechanisms with different characteristics, for example in their ability to sense geometry, can coexist in one reaction network. Most importantly, this highlights that a classification of pattern-forming mechanisms in terms of the reaction network topology alone misses important aspects of pattern formation that can be crucial for the biological function.

With respect to a potential biochemical origin of the pattern-forming mechanisms, we showed how additional protein domains can move the whole system into a mechanistically distinct regime. Enhancing the strength of MinE recruitment by MinD via dimerization shifts the system into a regime of recruitment-driven pattern formation. Alternatively, adding membrane targeting to the peptide unlocked a new pathway and led to sustained patterns via MinD-MinE recombination on the membrane (see supplementary discussion in Appendix 1 for further details).

In conclusion, the concept of modular engineering of pattern formation through distinct protein domains adds an entirely new dimension to the Min system, and establishes it further as a paradigmatic model for studying the mechanisms underlying self-organized pattern formation. Now, defined modules can be added, removed and interchanged. Interestingly, our experimental findings provide evidence that the distinct functional modules of MinE need not be provided by native parts of the proteins, but can be substituted with foreign sequences. Moreover, the part of MinE that interacts with MinD can be added as a small peptide tag of 19 amino acids to any host protein (as shown for superfolder-GFP + MTS, Figure 2—figure supplement 2), leading to a chimera protein that inherits key properties, such as membrane-interactions and protein-protein interactions, from the host protein. The modular domains provide an experimental platform to systematically modify the molecular interactions. Together with systematic theoretical studies, this is a powerful and versatile tool to study the general principles underlying biological pattern formation in multispecies, multicomponent reaction–diffusion systems.

## Materials and methods

Most experimental methods used in this publication were exhaustively described in text and video in a recent publication (Ramm et al., 2018). We therefore describe these techniques only in brief. This publication also includes a detailed and complete materials table for our assay.

### Membranes

SLBs were prepared from DOPC and DOPG (ratio 2:1) small unilamellar vesicles in Min buffer (25 mM Tris-HCl pH 7.5, 150 mM KCl, 5 mM MgCl2) by adding them (at 0.53 mg/mL) on top of a charged, cleaned glass surface. The solution was diluted after one minute by addition of 150 mL Min buffer. After a total of 3 min, membranes in chambers were washed with 2 mL of Min buffer.

### Assay chamber

Assay chambers were assembled from piranha-cleaned coverslips and a cut 0.5 ml plastic reaction tube by gluing the tube upside down onto the cleaned and dried surface using UV-curable adhesive.

### In vitro self-organization assay

The buffer volume in an assay chamber containing an SLB was adjusted to yield a final volume of 200 μL including protein solutions and ATP. Proteins, peptides and further reactants were added and the solution was mixed by pipetting.

### Peptides

Peptides were synthesized using Fmoc chemistry by our in-house Biochemisty Core Facility. MinE(2-31)-KCK-Atto488 was expressed as a SUMO fusion in E. coli BL-21 DE3 pLysS cells, the SUMO tag was then cleaved using SenP2 protease and the remaining peptide was labelled using Atto488-maleimide to site-specifically target the cysteine residue. Labelling was done as described below.

### Protein design and purifications

Detailed information about cloning procedures and design of proteins can be found in the supplementary information.

### Protein concentration measurements

Protein concentrations were determined by using a modified, linearized version of the Bradford assay in 96-well format (Ernst and Zor, 2010).

### Labeling

Atto 488-maleimide in 5–7 μL DMSO (about three molecules of dye per protein) was added dropwise to ∼0.5 mL of protein solution in storage buffer (50 mM HEPES pH 7.25, 300 mM KCl, 10 % glycerol, 0.1 mM EDTA, 0.4 mM TCEP) in a 1.5 mL reaction tube. The tube was wrapped in aluminium foil and incubated at 4° C on a rotating shaker for 2 to 3 hr. Free dye was separated from proteins first by running the solution on a PD-10 buffer exchange column equilibrated with storage buffer. Then, remaining dye was diluted out by dialysis against storage buffer overnight. The labeling efficiency was measured by recording an excitation spectrum of the labeled protein and measuring the protein concentration as described above. We then calculated the resulting labelling efficiency using the molar absorption provided by the dye supplier (Atto 488:9.0×104 M–﻿1 cm–1 ).

### Imaging

Microscopy was done on commercial Zeiss LSM 780 microscopes with 10x air objectives (Plan-Apochromat 10x/0.45 M27 and EC Plan-Neofluar 10x/0.30 M27). Tile scans with 25 tiles (5 × 5) at zoom level 0.6 were stitched to obtain overview images of entire assay chambers and resolve the large-scale patterns formed. More detailed images and videos were acquired on the same instruments using EC Plan-Neofluar 20x/0.50 M27 or Plan-Apochromat 40x/1.20 water-immersion objectives.

### The min ‘skeleton model’ extended by MinE membrane binding

To capture the effect of MinE membrane binding, we extend the ‘skeleton’ model introduced in Halatek and Frey (2012). Figure 3—figure supplement 1 shows a cartoon of the reaction network. We present the model first for a general geometry with a cytosolic volume coupled to a membrane surface. To perform linear stability analysis, we implemented this model in a ‘box geometry’ representing the in vitro setup with a membrane at the bottom, and in an ellipse geometry mimicking the rod-like cell shape of E. coli.

On the membrane, proteins diffuse and undergo chemical reactions, including attachment, detachment and interactions between membrane-bound proteins

$$
∂_{t}m_{d}=D_{m}∇_{m}^{2}m_{d}+R_{d},
$$



$$
∂_{t}m_{de}=D_{m}∇_{m}^{2}m_{de}+R_{de},
$$



$$
∂_{t}m_{e}=D_{m}∇_{m}^{2}m_{e}+R_{e},
$$

where $\nabla_{m}$ is the gradient operator along the membrane. In the cytosol, proteins diffuse and MinD undergoes nucleotide exchange with a rate $\lambda$

$$
∂_{t}c_{DD}=D_{D}∇_{c}^{2}c_{DD}−\lambdac_{DD}
$$



$$
∂_{t}c_{DT}=D_{D}∇_{c}^{2}c_{DT}+\lambdac_{DD}
$$



$$
∂_{t}c_{E}=D_{E}∇_{c}^{2}c_{E}
$$

The two domains are coupled via the boundary conditions at the membrane

$$
−D_{D}∇_{n}c_{DD}=f_{DD},
$$



$$
−D_{D}∇_{n}c_{DT}=f_{DT},
$$



$$
−D_{E}∇_{n}c_{E}=f_{E},
$$

where $\nabla_{𝐧}$ is the gradient along the inward pointing normal (n) to the membrane. The reaction terms are derived from the interaction network Figure 3—figure supplement 1 via the mass-action law and read

$$
R_{d}=(k_{D}+k_{dD}m_{d})C_{DT}−(K_{dE}c_{E}+k_{ed}m_{e})m_{d}
$$



$$
R_{de}=(k_{dE}c_{E}+k_{ed}m_{e})m_{d}−k_{de}m_{de},
$$



$$
R_{e}=k_{E}c_{E}+k_{de}m_{de}−(k_{e}+k_{ed}m_{d})m_{e}.
$$

Correspondingly, the attachment-detachment flows are

$$
f_{DT}=−(k_{D}+k_{dD}m_{d})c_{DT},
$$



$$
f_{DD}=k_{de}m_{de},
$$



$$
f_{E}=k_{de}m_{de}−(k_{E}+k_{dE}m_{d})c_{E},
$$

such that the dynamics conserve the global total densities of MinD and MinE

$$
N_{D}=\int_{mem}dS(m_{d}+m_{de})+\int_{cyt}dV(c_{DD}+c_{DT}),
$$



$$
N_{E}=\int_{mem}dS(m_{e}+m_{de})+\int_{cyt}dVc_{E}.
$$

### Linear stability analysis

To perform linear stability analysis, we need to find a set of orthogonal basis functions that fulfill the boundary conditions and diagonalize the Laplace operator, $\nabla^{2}$, on both domains (membrane and cytosol) simultaneously. In general, this is not analytically possible in arbitrary geometry. However, in a box geometry with a flat membrane, a closed form of the basis functions can easily be obtained. Furthermore, in a two-dimensional ellipse geometry, a perturbative ansatz can be used to obtain an approximate set of basis functions, as was shown in Halatek and Frey (2012) and used in Wu et al. (2016) and Gessele et al. (2018). In the following, we briefly outline how the basis functions can be determined and employed to perform linear stability analysis. For details, we refer to the supplementary materials of Halatek and Frey (2018a), Denk et al. (2018), Halatek and Frey (2012), and Gessele et al. (2018).

#### In vitro box geometry

For linear stability analysis of the in vitro system, we consider a two-dimensional box with a membrane at the bottom surface, representing a slice through the in vitro system. The cytosol domain is a rectangle in the $x$–$z$ plane with height h and length L. The bottom boundary at z = 0 is the one-dimensional membrane domain – a line of length L. It is coupled to the bulk via reactive boundary conditions, Equations (7) to (9). The other boundaries of the rectangular bulk domain are equipped with reflective boundaries. In this geometry, the gradient operators tangential and normal to the membrane are simply $\nabla_{m}≡\partial_{x}$ and $\nabla_{𝐧}≡\partial_{z}$.

The first step of a linear stability analysis is to calculate the steady state whose stability is to be analyzed. Typically this is a homogeneous steady state. In the system considered here, the most simple steady state is homogeneous along the x-direction. However, there must be cytosolic gradients in the z-direction due to the reactive boundary condition and the nucleotide exchange in the cytosol. Because the cytosol dynamics are linear, they can be solved in closed form.

To analyze the stability of such a steady state, one linearizes the dynamics around it. The ansatz to solve the resulting linear system is to diagonalize the Laplace operator. Importantly, in a system with multiple coupled domains, one needs to find a set of basis functions that diagonalize the Laplace operator on all domains (here membrane and cytosol), and that fulfill the reactive boundary conditions that couple these domains, simultaneously. In the x-direction, that is the lateral direction along the one-dimensional membrane, the eigenfunctions are simply Fourier modes. The bulk eigenfunctions in the z-direction, normal to the membrane, are exponential profiles and can be obtained in closed form by solving the linear cytosol dynamics, Equations (4) to (6).

These eigenfunctions can then be plugged into the the membrane dynamics and the boundary conditions linearized around the homogeneous steady state. The resulting set of linear algebraic equations can be solved for the growth rates of the Fourier modes. Thus, one obtains a relationship between wavenumber q of a mode and its growth rate $\sigma⁢(q)$. This relationship is called dispersion relation.

For details of the implementation of the linear stability analysis outlined above, we refer the reader to the supplementary materials of Halatek and Frey (2018a) and Denk et al. (2018). Note that the bulk height dependence saturates above around 50 μm, the maximal penetration depth of bulk gradients (Halatek and Frey, 2018a). The bulk heights in the experiments were well above this saturation threshold at around 1 mm, allowing us to use the limit of large bulk height $h$.

#### In vivo ellipse geometry

Linear stability analysis in an ellipse geometry is technically more involved, because the curved boundary makes it impossible to find a common eigenbasis of the Laplace operator on membrane and cytosol in closed form. For a detailed exposition of linear stability analysis in an elliptical geometry, we refer the reader to the supplementary materials of Halatek and Frey (2012).

### Parameters

#### In vitro

We used the kinetic rates and diffusion constants from Halatek et al. (2018b); see Table 1. In this previous study, the Min skeleton model without MinE membrane binding was studied. Including MinE membrane binding leads to three additional kinetic rates in the model: We set the MinE membrane recombination rate to $k_{ed}$ = 0.1 µms–1, and varied the MinE detachment rate, $k_{e}$, in the range 10–1 µms–1 to 105 µms–1. To test the effect of spontaneous MinE membrane attachment ($k_{E}>0$) we compared the results from LSA for $k_{E}$ = 0 and $k_{E}$ = 5 µm s–1, and found that spontaneous attachment is only relevant for very small MinE detachment rate, $k_{e}$, that is strong MinE membrane binding, where it suppresses pattern formation due to a dominance of membrane-bound MinE (see purple dashed line in Figure 3a).

**Table 1.**
 Overview over the parameters used in the mathematical model.In vitro parameters from Halatek and Frey (2018a), in vivo parameters from Halatek and Frey (2012); Wu et al., 2016. The diffusion constants, nucleotide exchange rate $\lambda$, and total protein densities are known from experiments Loose et al. (2008); Meacci et al. (2006). In Halatek and Frey (2012), the kinetic rates of the Min skeleton model ($k_{D}$, $k_{dD}$, $k_{dE}$, and $k_{de}$) to reproduce the in vivo phenomenology quantitatively, and to optimize the biological function of the in vivo pole-to-pole oscillation (mid-cell localization). The additional rates ($k_{ed}$, $k_{e}$, and $k_{E}$) of the model extended by MinE-membrane binding are not constrained by experiment. We varied $k_{e}$ over several orders of magnitude (see Figure 3 to study the role of persistent MinE-membrane binding. Note that, changing the MinE-recombination rate $k_{ed}$ over several orders of magnitude does not change our results qualitatively (topology of the phase diagrams).


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>In vitro</th>
      <th>In vivo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>μm2 s–1</td>
      <td>0.013</td>
      <td>0.013</td>
      <td>Dm</td>
    </tr>
    <tr>
      <td>μm2 s–1</td>
      <td>60</td>
      <td>16</td>
      <td>DD</td>
    </tr>
    <tr>
      <td>μm2 s–1</td>
      <td>60</td>
      <td>10</td>
      <td>DE</td>
    </tr>
    <tr>
      <td>s–1</td>
      <td>6</td>
      <td>6</td>
      <td>λ</td>
    </tr>
    <tr>
      <td>μm–2</td>
      <td>1200 (≈ 1μM)</td>
      <td>2000/Vcell</td>
      <td>nD</td>
    </tr>
    <tr>
      <td>μm–2</td>
      <td>120 (≈ 1μM)</td>
      <td>700/Vcell</td>
      <td>nE</td>
    </tr>
    <tr>
      <td>μm s–1</td>
      <td>0.065</td>
      <td>0.1</td>
      <td>kD</td>
    </tr>
    <tr>
      <td>μm2 s–1</td>
      <td>0.098</td>
      <td>0.108</td>
      <td>kdD</td>
    </tr>
    <tr>
      <td>μm2 s–1</td>
      <td>0.126</td>
      <td>0.65</td>
      <td>kdE</td>
    </tr>
    <tr>
      <td>s–1</td>
      <td>0.34</td>
      <td>0.4</td>
      <td>kde</td>
    </tr>
    <tr>
      <td>μm s–1</td>
      <td>0.1</td>
      <td>0.2</td>
      <td>ked</td>
    </tr>
    <tr>
      <td>s–1</td>
      <td>10–1 to 105</td>
      <td>10–1 to 103</td>
      <td>ke</td>
    </tr>
    <tr>
      <td>μm s–1</td>
      <td>0, 5</td>
      <td>0, 5</td>
      <td>kE</td>
    </tr>
  </tbody>
</table>

For the $(k_{e}^{-1},k_{dE})$ phase diagram (Figure 3a), the total densities of MinE and MinD were set to $n_{E}$ = 120 µm–2, $n_{D}$ = 1200 µm–2, corresponding to 0.1 μM MinE and 1 μM MinD in bulk solution, respectively. (Note that the unit for bulk concentrations is μm-2 because we consider a two-dimensional slice through the three-dimensional bulk. The membrane concentrations have a unit μm-1 respectively.)

In addition, we calculated $(n_{E},n_{D})$ phase diagrams at four points in $(k_{e}^{-1},k_{dE})$ phase plane (see Figure 3—figure supplement 2). In these phase diagrams, one can see that mostly the E/D-concentration ratio, $n_{E}/n_{D}$, determines the regime of pattern formation. This is in qualitative agreement with the experimentally found phase diagram for the MinE(1-31) mutant (cf. Figure 2—figure supplement 2).

To exemplify how the critical E/D-ratio depends on the kinetic rates, we fixed the MinD concentration ($n_{D}$ = 1000 µm–2) and varied $n_{E}$ and one of the kinetic rates. For the MinE-recombination driven regime, we set $k_{dE}$ = 0 (no MinE recruitment to MinD), and varied the MinE-detachment rate $k_{e}$ (see Figure 3—figure supplement 3a). The critical E/D-ratio of approximately 1/20 below which pattern formation is observed for the MinE(1-31) mutant in experiments is fitted for $k_{e}≈$ 0.2 s–1 (dashed red line and inset in Figure 3—figure supplement 3a). Note however, this ‘fit’ is severely underdetermined, because the remaining kinetic rates are not constrained by experiment. Changing, for instance, the MinE membrane recombination rate $k_{ed}$ (or any other kinetic rate) would lead to a different value for $k_{e}$ that fits the experimentally found concentration dependence. A remaining quantitative difference to the experimental findings is that the regime of pattern formation extends to very low MinE concentrations in the mathematical model, while there is a lower bound at a E/D-ratio of about 1/100 in the experiments.

Figure 3—figure supplement 3b shows the $(k_{dE},n_{E})$ phase diagram for the Min-skeleton model without persistent MinE-membrane binding (corresponding to $m_{e}→∞$).

#### In vivo

We use the parameters from Halatek and Frey (2012) (see Table 1). In this previous study, the Min skeleton model was studied in vivo and the kinetic rates where fitted to reproduce the in vivo phenomenology. The model extended by MinE membrane binding has three additional kinetic rates: We set the MinE membrane recombination rate to $k_{ed}$ = 0.2 µm s–1, and varied the MinE detachment rate, $k_{e}$, in the range 10–1 s–1 to 10–3 s–1 . As in the in vitro case, spontaneous MinE membrane attachment ($k_{E}>0$) has no significant effect, so we set $k_{E}$ = 0. (Linear stability analysis and numerical simulations for a non-zero attachment rate $k_{E}$ = 5 µm s–1 yield a phase diagram with the same qualitative structure as the one presented in Figure 3b.)

We mimic the cell geometry by an ellipse with lengths 0.5 m and 2 m for the short and long half axis, respectively (the corresponding cell ‘volume’ is $V_{cell}$ = 3.14 µm2).

### Numerical simulations

The bulk-boundary coupled reaction–diffusion dynamics Equations (1) to (15) were solved using a finite element solver code (COMSOL Multiphysics).

Due to its large size, simulations of the in vitro system are very time consuming and beyond the scope of this work. Because most of the kinetic rates are not known, extensive parameter studies would be necessary to gain insight from such simulations.
