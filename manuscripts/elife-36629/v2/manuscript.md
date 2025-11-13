# Structure of the CLC-1 chloride channel from Homo sapiens

## Authors

- Eunyong Park<sup>1</sup> ([ORCID: 0000-0003-2994-5174](https://orcid.org/0000-0003-2994-5174))
- Roderick MacKinnon<sup>1</sup> ([ORCID: 0000-0001-7605-4679](https://orcid.org/0000-0001-7605-4679)) †

### Affiliations

1. Laboratory of Molecular Neurobiology and Biophysics Howard Hughes Medical Institute, The Rockefeller University New York United States

† Corresponding author

## Abstract

CLC channels mediate passive Cl− conduction, while CLC transporters mediate active Cl− transport coupled to H+ transport in the opposite direction. The distinction between CLC-0/1/2 channels and CLC transporters seems undetectable by amino acid sequence. To understand why they are different functionally we determined the structure of the human CLC-1 channel. Its ‘glutamate gate’ residue, known to mediate proton transfer in CLC transporters, adopts a location in the structure that appears to preclude it from its transport function. Furthermore, smaller side chains produce a wider pore near the intracellular surface, potentially reducing a kinetic barrier for Cl− conduction. When the corresponding residues are mutated in a transporter, it is converted to a channel. Finally, Cl− at key sites in the pore appear to interact with reduced affinity compared to transporters. Thus, subtle differences in glutamate gate conformation, internal pore diameter and Cl− affinity distinguish CLC channels and transporters.

## Introduction

Transporters – also known as pumps – and channels both mediate the transfer of ions and molecules across biological membranes. But the two are thermodynamically contrasting: transporters require the input of external energy while channels are passive, meaning the substrate simply diffuses down its electrochemical gradient. Except in rare cases, transporters and channels correspond to separate, unrelated structural families. CLC proteins are one of the exceptions. Channel-forming CLCs are passive Cl− conductors (Jentsch et al., 1990; Miller and White, 1984), while transporter-forming CLCs exchange, with fixed stoichiometry, two Cl− ions and one proton (H+) in opposite directions (i.e., they are Cl−/H+ antiporters) (Accardi and Miller, 2004; Picollo and Pusch, 2005; Scheel et al., 2005). The external energy input in CLC transporters comes from the energetic coupling of the transported ions, Cl− and H+, such that the electrochemical gradient of one ion drives movement of the other. The puzzling aspect of this dual functionality within the CLC protein family is that at the level of amino acid sequence, the distinction between the channels and transporters is not apparent.

Conceptually, the distinction between channels and transporters in general has been explained in terms of gating models that invoke one or two primary gates: channels are described as pores with one gate and transporters as pores with two gates that are never permitted to open simultaneously (Figure 1) (for review see [Gadsby, 2009]). While it is true that channels and transporters are most often unrelated structurally, the gating model description implies that, in principle, similar structures could give rise to both, as one can imagine that a transporter could become a channel if one or both gates are compromised. CLC channels seem to fall under this category of channels that emerged from a family of transporters (Accardi and Picollo, 2010; Lísal and Maduke, 2008; Miller, 2006).

![Figure 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig1-v2.jpg)

**Figure 1.:** One-gate (A) and two-gate (B) models explaining passive transport by a channel and active transport by a transporter (shown is an antiporter). Direction of the solute electrochemical gradient is indicated by a wedge (the thicker end means more positive).

Structural and functional studies support a plausible mechanistic model for the operation of CLC transporters. CLC transporter structures show a narrow Cl− transport pathway with three consecutive Cl−-binding sites, referred to as Sext, Scen and Sint, for external (nearest the extracellular solution), central and internal (nearest the intracellular solution), respectively. Chloride is observed at these sites in various structures (Dutzler et al., 2002; Dutzler et al., 2003; Feng et al., 2010; Jayaram et al., 2011). In addition, the transporters all contain a glutamate residue positioned such that its side chain carboxylate group can bind either at Sext or Scen – in competition with a Cl− ion – or reside in the extracellular solution. Thus, CLC transporters are like Cl− channels with a weird feature – a glutamate side chain that clogs its own pore. This led to the idea that glutamate might not only be a competitor for the Cl− binding sites as the structures suggest, but it might also transfer a proton from inside to out (or the reverse) when it moves between its Scen position to its extracellular position (Feng et al., 2010; Feng et al., 2012). The transfer would naturally give rise to the 2:1 Cl−:H+ exchange stoichiometry characteristic of CLC transporters because 2 Cl− ions must be displaced when the glutamate gate moves between the extracellular solution and Scen. This mechanism is consistent with the demonstrated conversion of a CLC transporter into a passive (but slow) Cl− channel upon mutation of the glutamate, as well as the demonstrated ability of small carboxylate-containing organic acids to compete with Cl− inside the pore (Accardi et al., 2004; Accardi and Miller, 2004; Feng et al., 2012). But there was one important caveat to make this transporter mechanism work: there must exist a relatively high kinetic barrier to Cl− flow near the intracellular side of the pore (Feng et al., 2010). This barrier would serve as the ‘second gate’ in the gating model conceptualization of transporters. So far, data for CLC transporters seem consistent with this mechanism: they have a channel-like pore, an external ‘glutamate gate’ that competes with Cl− binding and (presumably) transfers H+ across the membrane, and structurally what appears to be a relatively high resistance (i.e., a large kinetic barrier) to Cl− flow near the intracellular aspect of the pore (i.e., the pore there is very narrow.)

Less is known about the chemistry and structure of CLC channels. Only one CLC channel structure has been determined, CLC-K from Bos taurus (referred to as bCLC-K or shortly CLC-K) (Park et al., 2017). This is a special case, a rare type of CLC channel that can be distinguished from CLC transporters based on its amino acid sequence because it does not have a ‘glutamate gate’. That difference alone renders CLC-K inert to H+ transfer. The structure of CLC-K also revealed a wider pore diameter on the intracellular side, consistent with a lowered kinetic barrier to Cl− flow. CLC-0/1/2 channels, by contrast, contain a ‘glutamate gate’ and are not distinguishable from CLC transporters by sequence. Thus, there must be an even more subtle distinction between these CLC channels and the transporters. Why does the glutamate gate in these channel CLCs not give rise to H+ transfer coupled to Cl− transfer? Is a reduced kinetic barrier to Cl− flow near the intracellular side, suggested by the CLC-K structure, a common feature in CLC channels? To address these questions, we have determined the structure of CLC-1 from Homo sapiens (referred to as hCLC-1 or CLC-1).

We are also interested in the CLC-1 channel because it plays an important role in membrane repolarization of skeletal muscle cells following muscular contraction, and its mutation in humans causes hereditary muscle disorders known as myotonia congenita (George et al., 1993; Koch et al., 1992; Lorenz et al., 1994; Steinmeyer et al., 1991).

## Results

### Determination of a human CLC-1 channel structure by cryo-EM

We purified the CLC-1 protein in mild detergent from cultured human cells and examined them by cryo-EM single particle analysis (Figure 2 and Figure 2—figure supplements 1 and 2). Despite its small molecular size (200 kDa), particles showed good contrast on micrographs under the optimized freezing and data acquisition conditions (Figure 2A). Two-dimensional (2D) class averages of selected particles displayed 2-fold rotational symmetry around an axis normal to the membrane (detergent micelle) (Figure 2B), as expected from the homodimeric architecture of CLC proteins (Dutzler et al., 2002; Ludewig et al., 1996; Miller and White, 1984). After removing artifacts and damaged particles by 2D classification, a density map was reconstructed at 3.9 Å resolution with C2 symmetry imposed (Figure 2—figure supplement 1B). This map showed a well-resolved transmembrane domain (TMD) with clearly visible α-helical features. By contrast, density for the carboxy-terminal cytosolic domain (CTD) was lower quality, suggesting conformational flexibility in this region.

![Figure 2.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig2-v2.jpg)

**Figure 2.:** (A) Representative micrograph of the purified CLC-1 channel (scale bar, 50 nm) on a cryo-EM grid. Representative particles (white squares) are magnified and shown in the right panels. (B) Images of selected 2D classes from reference-free 2D classification by RELION. Scale bar, 10 nm. (C and D) Cryo-EM density map (C) and atomic model (D) of the hCLC-1 channel. The transmembrane domain (TMD; blue and salmon) and the cytosolic domain (CTD; light blue and tan) were separately refined and combined for visualization. Ext, extracellular side. Int, intracellular side. The approximate lipid bilayer region is shown by arrows.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Superdex-200 gel-filtration profile (UV absorbance at 280 nm) of affinity purified human CLC-1. Peak fractions (arrowhead) were collected for cryo-EM grid preparation and SDS-PAGE analysis (right). (B) Summary of cryo-EM image processing procedure (see the Methods section). (C) Classes indicated were aligned and superimposed to compare their CTD density. Note that there are significant mismatches between classes mainly due to pivotal movements of the two arms. (D) A model for CTD was generated by Rosetta using a crystal structure of the CLC-0 CBS domains and the CLC-1 density map. The model was superimposed (blue and salmon for each monomer) onto the CBS density map (semi-transparent gray surface). Note that density for a segment of ~127 amino acids is missing likely due to flexibility of the segment.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Local resolution was estimated by the RELION program (relion_postprocess) and displayed on the TMD map. Shown is the combined map (a sum of two half maps), which is not sharpened or filtered. Top, a view from the extracellular side. Bottom, a side view. (B) Fourier shell correlation (FSC) of two half maps before (black) and after (red) masking for TMD. The masked FSC curve was corrected for masking effects during the RELION postprocessing procedure. Correlation between the map and the phase-randomized mask is shown as a black dashed line. (C) FSC between the atomic model and EM maps of the CLC-1 TMD. The red curve shows the FSC between the final refined atomic model and the combined map that the model was refined against (FSCfull). To test potential overfitting during the model refinement procedure, a test refinement was performed using the first half map. The resulting model was then compared to the first half map (FSCwork; solid black curve) and the second half map (FSCfree; dashed black curve). Similarity of the two curves indicates that overfitting is insignificant. (D) Segments of the TMD model in stick representation were superimposed with EM density (semi-transparent gray surface). Numbers indicate amino acid positions of segments. The density map was sharpened with a B-factor of −97 Å2 and low-pass filtered at 3.4 Å.

To improve the map quality, we subjected particles to a round of 3D classification (Figure 2—figure supplement 1B). The results demonstrated that while the TMD is largely indistinguishable between classes, the CTDs deviate from each other by pivotal movements of varying degrees (Figure 2—figure supplement 1C). Based on this, we pooled ~170,000 particles from the two most populated and structurally similar classes, which correspond to 50% of particles. This particle set led to an improved density map at an overall resolution of 3.6 Å (data not shown). Using masking techniques to isolate individual regions, the resolution of the TMD was further improved to 3.4 Å (Figure 2C, Figure 2—figure supplement 1B, Video 1). The CTD remained poorly defined, likely due to continuous pivotal movements of its two wing-like structures (Figure 2C, Figure 2—figure supplement 1C, Video 1).

![Video 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-video1.mp4.jpg)

**Video 1.:** The cryo-EM map and atomic model of human CLC-1 are illustrated. Also see Figure 2C and D.

The good quality TMD density map enabled building a molecular model that included nearly all side chains (Figure 2C, Figure 2—figure supplement 2, and Video 1). The model was refined using Rosetta (Wang et al., 2016). The CTD map did not show side chain density but we could dock with confidence the crystal structure of the CLC-0 CTD (Figure 2D and Figure 2—figure supplement 1D) (Meyer and Dutzler, 2006). Both CLC-1 and CLC-0 channels contain a large loop extending from the CTD’s cystathionin-β-synthase (CBS) domains, which was not visible in either the EM density map or the crystal structure. The function of the CTD is poorly understood; it may even be dispensable for ion transport given its high tolerance to mutation (Estévez et al., 2004) and absence in most bacterial CLC transporters.

### Bifurcated pore structure of CLC-1

The TMD of CLC-1 exhibits the canonical dimeric architecture of a CLC protein (Figure 2C,D). Each monomer is roughly a triangular prism shape and contains a complete ion transport pathway that appears structurally independent from that of the neighboring monomer. As in other CLC structures (Dutzler et al., 2002; Dutzler et al., 2003; Feng et al., 2010; Park et al., 2017), the Cl− transport pore in CLC-1 is most narrowly constricted halfway across the membrane, within the region referred to as the selectivity filter (Figure 3A). Overall, the pore lining is charged positive to attract Cl− (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig3-v2.jpg)

**Figure 3.:** (A) The canonical Cl− transport pathway (green) and the second intracellular pore (yellow) are depicted in a side view of CLC-1. The pores of only one monomer are shown for simplicity. (B) Surface electrostatistics of CLC-1’s pore lining. The protein surface was clipped to show optimally the pore lining of the CLC-1 monomer on the left. The yellow arrowhead indicates the position of the selectivity filter. The insets show views into the pore entrances, which are marked with asterisks. (C) A view into the second intracellular pore entrance from the cytosolic surface was compared to equivalent views with other CLC proteins. In the CLC-1 panel, the pore is indicated by a dashed gray circle. Amino acids lining the pore were indicated with their side chain atoms shown in ball-and-stick representation.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) and (B) As in Figure 2A, pores in the protein interior were detected in EcCLC (A) and CmCLC (B) transporters using the Caver program. The canonical Cl− transport pathway and the second intracellular pore are shown as green and yellow surfaces, respectively, superimposed on ribbon representations of the proteins (side view). For simplicity, pores of only one monomer (blue) are shown. Note that the second intracellular pore (minimal radius larger than 0.9 Å) could be detected only with the E203 mutant of the EcCLC and wild-type CmCLC transporters, not with the wild-type EcCLC or the bovine CLC-K channel (not shown). (C) The pore radii are displayed as a color map. The second intracellular pore is indicated by a red asterisk. The view angle is similar to (A) and (B).

In contrast to other CLC proteins the potential route for ion diffusion in CLC-1 is bifurcated on the intracellular side of the selectivity filter– one following the canonical Cl− transport pathway found in all CLC proteins and the ‘second’ pore directed toward the protomer-protomer boundary on the cytosolic surface, which is distinctive in CLC-1 (Figure 3A,B and Figure 3—figure supplement 1). Both branches of the bifurcation are potentially hydrated because the radius is greater than that of water (1.4 Å) and the linings contain chemical groups with hydrogen bonding potential. A branch equivalent to CLC-1’s secondary pore in the CLC-K channel is sealed off by F222 and V226 (corresponding to F288 and V292 of CLC-1) due to a different αH helix position (Figure 3C). In transporters, only a much narrower (~0.9–1.0 Å radius) pore could be detected, where stable dwelling of water molecules seems unlikely (Figure 3—figure supplement 1). In the E. coli transporter (EcCLC), the pore is further capped near the cytosolic surface by E203 (corresponding to V292 of CLC-1). We note that E203 of EcCLC and the equivalent Glu of mammalian CLC-4 and CLC-5 transporters have been implicated in shuttling H+ between the intracellular solvent and the protein interior (Lim and Miller, 2009; Lim et al., 2012; Zdebik et al., 2008) by side-chain protonation and deprotonation, although this feature does not seem to be essential for H+ transport in other cases, including the C. merolae transporter (CmCLC) (Feng et al., 2010; Feng et al., 2012; Phillips et al., 2012). It is possible that during Cl−/H+ exchange cycles, the αH helix of transporters transiently undergoes a conformational change such that a water-accessible pore is formed similarly to the CLC-1 case, which might facilitate H+ transfer. Unlike transporter-type CLCs, the CLC-1 channel does not transport H+ in a manner tightly coupled to Cl− and thus it is unclear whether CLC-1’s second intracellular pore is utilized for ion transport. Cl− ions may move through this pore in addition to the primary Cl− pathway.

### Chloride-selectivity filter and bound Cl− ions

The CLC-1 structure shows an anion selectivity filter largely similar to other CLC proteins but with some distinctive features (Figure 4A and Video 2). The filter is formed at the central constriction of the Cl− pathway by αN, αF, and αD helices, all of which point their N-terminal ends towards the center where Cl−-binding sites are formed. This arrangement contributes to an electrostatically positive environment at the Cl−-binding sites through α-helix end charges. Backbone nitrogen atoms from αN and αF segments are arranged to coordinate a partially dehydrated Cl− ion near the extracellular end of the constriction (external site or Sext). In the CLC-1 density map we observe a clear density feature at Sext, which likely corresponds to a bound Cl− ion (Figure 4A and Video 2). Typically, CLC proteins have two additional Cl−-binding sites, namely, central (Scen) and internal (Sint) sites (Dutzler et al., 2003). Scen has been observed to bind a Cl− ion through polar interactions with one or two backbone nitrogen atoms and the side chains of the conserved tyrosine (denoted TyrC; Y578 of CLC-1 or Y445 of EcCLC) and serine residues (denoted SerC; S189 of CLC-1 or S107 of EcCLC) (Dutzler et al., 2002; Dutzler et al., 2003). In the EcCLC transporter, Scen has been shown to bind Cl− relatively strongly (Kd ~1 mM) (Lobet and Dutzler, 2006; Picollo et al., 2009). Sint is largely exposed to the intracellular solvent and binds Cl− with lower affinity (Kd >20 mM) (Lobet and Dutzler, 2006; Picollo et al., 2009). In the CLC-1 map (determined in the presence of 116 mM Cl−), Sint shows a density peak whose intensity is comparable to that of the Sext density (Figure 4A and Video 2). By contrast, we do not observe density for an ion at Scen above the noise level, suggesting that Scen of CLC-1 may have a lower Cl− occupancy than Sext and Sint. This is somewhat surprising given the conservation of structural elements for Scen, including TyrC and SerC. Perhaps subtle structural differences account for the absence of an ion at this site compared to other CLC proteins. For example, we note that the position of TyrC is shifted away from Scen by ~1.5 Å (see Figure 5B).

![Figure 4.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig4-v2.jpg)

**Figure 4.:** (A) View (stereo) into the selectivity filter of CLC-1. αN, αF, αR, and αC-D segments (Cα trace and side chains) are shown in cyan, salmon, yellow, and olive, respectively. The side chains of Glugate, TyrC, and SerC are represented with balls and sticks. Cl−-binding sites are indicated by green (Sext and Sint) and gray (Scen) spheres. The cryo-EM density map is shown in mesh (Sext and Sint in magenta and the rest in gray). (B) Water-accessible regions in the filter region, probed by Hollow (Ho and Gruswitz, 2008), are shown with purple (extracellular vestibule) and blue (intracellular vestibule) dots. Glugate is represented in ball-and-stick. (C) Comparison of Glugate positions between the CLC-1 channel and CLC transporters. The amino acid segments 146–149 and 355–358 forming the anion selectivity filter were aligned between structures. Cα-traces of the segments are shown with the Glugate side chains in ball-and-stick representation. Blue, CLC-1. Light orange, WT EcCLC (PDB ID: 1OTS). Yellow, EcCLC E148Q mutant (PDB ID: 1OTU). Magenta, CmCLC (PDB ID: 3ORG). Gray spheres represent the positions of Cl− ions seen in EcCLC E148Q mutant (Sext and Scen). Note that the Cl− ion at CLC-1’s Sext (not shown) essentially coincides with Sext of EcCLC.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A–D) As in Figure 3B, but focused on Glugate and neighboring hydrophobic amino acids (stereo views with the same view angle). (B–D) also include superimposed Glugate of CLC-1 in pink semi-transparent sticks, to show steric clashes with neighboring hydrophobic amino acid side chains of other CLC proteins. The green spheres indicate the position of Sext or Scen. Note that in the EcCLC and CmCLC structures, Glugate’s side chain occupies Sext and Scen, respectively, and in the bCLC-K, Sext is unoccupied.

![Figure 5.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig5-v2.jpg)

**Figure 5.:** (A) Atomic model and cryo-EM density of the CLC-1 αC-D. (B) Comparison of the αC-D and αR segments (shown in Cα-only trace) among CLC channels and transporters. The side chains of SerC and TyrC are shown in sticks.

![Video 2.](https://cdn.elifesciences.org/articles/36629/elife-36629-video2.mp4.jpg)

**Video 2.:** The selectivity filter region of human CLC-1 is shown. The same color scheme and representation are used in Figure 4A.

### New conformation of the gating glutamate

Like transporter-type CLC proteins and in contrast to CLC-K, the CLC-1 channel has a Glugate, but in CLC-1 it adopts a notably different conformation than previously observed in CLC transporters (Figure 4 and Figure 4—figure supplement 1). Based on previous studies on transporters (Dutzler et al., 2002; Dutzler et al., 2003; Feng et al., 2010), Glugate, located in the immediate vicinity of Sext and Scen, plays a key role in ion transport: when deprotonated its side-chain carboxylic moiety resides in either the Sext or Scen Cl− binding sites, preventing the binding of a Cl− ion therein. In the CLC-1 structure, the Glugate side chain occupies neither Sext nor Scen, but instead it is oriented in a different direction. The difference in Glugate’s conformation is mainly due to changes in its side-chain rotamer, whereas the polypeptide backbone arrangement in this region is similar among the structures (Figure 4C). The observed Glugate conformation is also different than the outwardly-oriented (side chain projecting into the extracellular funnel) conformation that has been seen in the structure of an EcCLC Glu-to-Gln (E148Q) mutant (Figure 4C), which is hypothesized to mimic the protonated state of Glugate (Dutzler et al., 2003).

It is unclear whether the Glugate in the CLC-1 structure (determined at pH 7.4) is protonated. The pKa of the Glugate side chain might be shifted towards a more neutral pH as it is neighbored by multiple hydrophobic amino acids (Isom et al., 2010). Yet, Glugate at this position is more likely deprotonated because its side chain seems exposed to water molecules due to the presence of the second intracellular pore (Figure 4B). In CLC transporters, this conformation would be highly unfavorable because it would produce steric clashes with neighboring side chains (equivalent to V236, V265, and F279 of CLC-1; Figure 4—figure supplement 1), which are moved away in CLC-1 by a shift of the αG and αH helices. In other words, this conformation of Glugate does not seem possible in CLC transporters studied so far.

The observed Glugate conformation of CLC-1 was unexpected because it was never observed in other CLC protein structures, and yet it is consistent with an open CLC-1 channel, which is expected in the absence of an applied membrane potential. CLC-1 is a voltage-gated channel, which closes when the membrane potential is negative (i.e., at its ‘resting’ value) (Fahlke et al., 1996; Pusch et al., 1995). Perhaps in the presence of an applied negative membrane potential the Glugate side chain moves into either the Sext or Scen position, as seen in CLC transporters, and prevents Cl− conduction. This possibility would account for the observation that CLC-1 and related CLC-0 conduct Cl− ions at all membrane voltages when the Glugate residue is mutated to Gln (Dutzler et al., 2003; Fahlke et al., 1997).

### ‘Transporter-like’ αC-D loop

The previous CLC-K channel structure has suggested that a wider pore diameter between Scen and Sint is crucial for its channel function (Park et al., 2017). In CLC transporters, a kinetic barrier for Cl− passage (i.e., a narrowing of the pore) exists on the intracellular side of the vestibule to preclude slippage of Cl− ions during the Cl−/H+ exchange cycle (Feng et al., 2010). This barrier is due to a narrow pore width between Scen and Sint, which is created in part by SerC of the αC-D loop interposed between the two Cl− binding sites. In the CLC-K structure, the αC-D loop has a distinctly different conformation, where SerC is flipped down and thus no longer interposed between the two Cl− binding sites. Consequently, the pore diameter is wider such that Cl− ions will more readily permeate. Given that CLC-1 is also a channel, we wondered whether the αC-D loop in CLC-1 would adopt a similar ‘flipped-down’ conformation.

While a different conformation of the αC-D loop is a key feature distinguishing CLC-K from transporters, a structural comparison shows that this is not the case for the CLC-1 channel (Figure 5). In contrast to CLC-K, the αC-D loop in CLC-1 adopts the loop conformation seen in CLC transporters, especially CmCLC (Feng et al., 2010). Consequently, the SerC side chain is positioned between Sint and Scen (Figure 5B). Therefore, in the case of CLC-1 the αC-D loop itself does not provide an explanation for why CLC-1 functions as a Cl− channel (see below). This also suggests that the ‘flipped-down’ conformation of SerC may be unique to the CLC-K channel.

### Comparison of Cl− pore structures of CLC proteins

To understand why CLC-1 functions as a channel we compared its Cl− pore structure to that of other CLC proteins. In both CLC-1 and CLC-K channels, a continuous Cl− pathway was evident in between the extracellular and intracellular funnels, through the selectivity filter (Figure 6A,B). In the EcCLC and CmCLC transporters, a continuous pore could be detected only when the Glugate side-chain atoms (from Cβ) were excluded from the pore radius calculation as Glugate sits at Sext or Scen (Figure 6C,D). These results would therefore reflect the pore structure when the transporter’s Glugate transiently moves away from the Cl− pathway upon protonation (hypothetically, akin to the crystal structure of the EcCLC E148Q mutant). However, we note that calculated pore radii around Sext may be somewhat overestimated due to the actual presence of the Glugate side-chain atoms.

![Figure 6.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig6-v2.jpg)

**Figure 6.:** Pore structures along the Cl− pathway are shown in dot representation together with amino acids around it. Glugate, TyrC, and SerC side chains are shown in ball-and-stick representation. The color scheme is the same as in Figure 4. Pore-lining amino acids that are distinctive between CLC channels and transporters are shown in gray.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Amino acids and their positions (numbers) of selected residues in the filter and pore lining are indicated. For transporters, E. coli CLC (EcCLC), C. merolae CLC (CmCLC), and human CLC transporters (hCLC-3 to hCLC-7) were selected. For channels, Torpedo marmorata CLC-0, human CLC channels (hCLC-1, hCLC-2, and hCLC-Ka), and bovine CLC-K (bCLC-K) channel were included. Amino acids showing a pattern distinguishing channels and transporters were highlighted (positions 348 and 356 in EcCLC). Note that in hCLC-Ka and bCLC-K, the side chains of tyrosine and phenylalanine, denoted by an asterisk, are involved in binding of a Cl− ion at Scen by quadrupole-anion interactions (see Figure 6D).

The CLC-1 channel has the narrowest (1.0 Å in radius) constriction above Sext toward the extracellular side due to the placement of the M485 side chain near the external end of the Cl− pathway (Figure 6A). While the radius is significantly smaller than the Cl− radius (~1.7 Å), the flexibility of the M485 side chain must allow Cl− ions to pass through this region. Given the narrowness of this constriction, it is likely that M485 affects the Cl− throughput of the channel. In fact, its mutation to less flexible valine (M485V) causes recessive myotonia congenita and has been shown to reduce the single channel conductance of CLC-1 to about 20% of the wild type channel conductance (Wollnik et al., 1997).

From Sext to the intracellular opening the CLC-1 channel structure shows a relatively wide pore opening despite its ‘transporter-like’ αC-D loop. This suggests the absence of a large kinetic barrier in CLC-1, but for reasons other than the αC-D loop conformation. Compared to the CLC-K channel, CLC-1 has a slightly narrower (1.5 Å vs 1.7 Å in radius) opening between Scen and Sint because of SerC. This might create a kinetic barrier to some degree, but the pore is still significantly wider and more hydrophilic than the equivalent region in the EcCLC transporter (Figure 6C). The difference originates mainly from two amino acids (T475 and G483) lining the constriction. In EcCLC, the equivalent positions are F348 and I356, which project their bulky, hydrophobic side chains towards the Cl− pathway between Scen and Sint. Together with proximal placement of SerC and TyrC, this narrows the opening (1.0 Å in radius) in EcCLC. In the CmCLC transporter, the constriction at the kinetic barrier region is wider (1.6 Å in radius) than EcCLC because of smaller side chains at the equivalent positions (I421 and V429; Figure 6D) and a slight downward shift (1.5 Å) of SerC with respect to the positions in EcCLC (Figure 5B). Yet, hydrophobicity provided by the I421 and V429 side chains might result in a significantly higher kinetic barrier than in CLC-1.

It is noteworthy that the CLC-1 channel shows a 1.5 Å outward shift of the TyrC side chain with respect to the position that is almost invariant in the other CLC structures (Figure 5B). In CLC-1, this shift contributes to pore widening in the cytosolic vestibule. At present it is unclear if this shift of TyrC is static or part of dynamic movements in CLC-1 and if it is unique in CLC-1 or a similar movement exists in other CLC proteins. Previous biophysical studies have proposed a movement of TyrC to explain alternating gate opening of the EcCLC Cl−/H+ transporter (Basilio et al., 2014; Jayaram et al., 2008; Khantwal et al., 2016). On the other hand, EcCLC crystal structures obtained with a number of different variants and crystallization conditions have not yet revealed any movement of TyrC.

### Distinctive amino acid pattern between CLC channels and transporters around the kinetic barrier region

Because the CLC-1 structure suggests that T475 and G483 (equivalent to F348 and I356 in EcCLC, respectively) likely contribute to lowering of the kinetic barrier, we compared amino acids lining this region among both CLC channels and transporters (Figure 6—figure supplement 1). Indeed, these two positions showed a distinctive differential pattern when comparing CLC channels and transporters, whereas other positions (i.e., H369, C481, L577, and I581 in CLC-1) did not. Generally, these two positions are filled with large, hydrophobic amino acids in transporters but are replaced by a small, polar amino acid in CLC channels. One notable outlier is position 417 of the CLC-K channels (Y425). However, the CLC-K channel structure shows that its phenyl side chain is skewed off the Cl− pathway, and thus does not seem to create a kinetic barrier in CLC-K (Figure 6B). In fact, it forms the Scen Cl− binding site together with TyrC and F519 through anion-quadrupole interactions (Park et al., 2017) (Figure 6B). In summary, the observed amino acid pattern and structural information suggest that a lowered barrier in the Scen–Sint region of the pore is a common feature of CLC channels, but CLC-1 and CLC-K channels achieve this somewhat differently. In the CLC-1 channel, small side chains in pore-lining residues lower the kinetic barrier, whereas in CLC-K mainly the reorientation of SerC lowers it. The extent of the kinetic barrier should also be affected by the hydrophobic and electrostatic nature of the lining residues, not only the physical dimensions of the pore.

### Working model and experimental validation

Combining the new structural information and previous data, we propose a working model that channel behavior in CLC proteins arises out of the following physical conditions (Figure 7): (1) Glugate is either absent (i.e., in CLC-K) or allowed to reside in an ‘open’ configuration (i.e., CLC-1) for a sufficiently extended period of time (rather than occupying Sext or Scen); (2) a lowered kinetic barrier between Scen and Sint; (3) reduced Cl−-binding affinity at Scen (or Sext, as suggested by apparent low occupancy in the CLC-K structure). A reduced kinetic barrier would be an important feature to achieve fast Cl− throughput. On the other hand, a sufficient kinetic barrier would be crucial in transporters to preclude undesired slippage of Cl− ions through the transiently open pore (Feng et al., 2010). In addition, reduction of Cl−-binding affinity at Scen and/or Sext, which is energetically related to the kinetic barrier, might also contribute to high Cl− throughput in channels. For example, relatively deep energy wells at Scen and Sext, as implied by the high occupancy of sites in the EcCLC transporter, would create a larger energy difference between the binding sites and the ‘transition states’, which effectively raises the energy barrier. In CLC-1 the relatively low binding site occupancy implies not very deep energy wells and thus a smaller energy difference between the binding sites and ‘transition states’.

![Figure 7.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig7-v2.jpg)

**Figure 7.:** (A) General architecture of CLC proteins. F348 and I356 are labelled according to E. coli transporter (EcCLC) numbering. (B) Model for 2:1 Cl−/H+ exchange by CLC transporters. The negatively-charged carboxylic group of the Glugate side chain can occupy Sext (state 2) or Scen (state 3) by a swinging motion, competing with a Cl− ion for binding therein. When protonated at Scen by a proton transferred from the cytosol (state 4), the Glugate side chain flips out to the extracellular side (state5). The kinetic barrier between Scen and Sint would prevent leakage of Cl− ions through the open pore during this transient step. Also, as seen previously with EcCLC (Picollo et al., 2009), synergistic binding of two Cl− ions at Sext and Scen (depicted by solid gray curves around Sext and Scen) might further deter slippage of Cl− ions. Deprotonation resets the cycle (state1). The cycle is reversible, and for simplicity the intermediate steps were omitted. Cl− ions and H+ are depicted as green and blue spheres, respectively. (C) Model for the CLC-1 channel. The cryo-EM structure of CLC-1 presented in this study represents the depolarized state. Although the conformation of the αC-D loop remains similar to that of transporters, CLC-1’s kinetic barrier is lower than transporters due to the lack of additional kinetic barrier elements. In addition, weak Cl−-binding affinity at Scen might facilitate rapid permeation of Cl− ions along the pore. When the membrane potential is negative (resting), the Glugate side chain may occupy Sext or Scen as in transporters, blocking the pore. (D) Model for CLC-K channels. The outer gate is removed by a natural mutation of Glugate to valine (V166). The kinetic barrier is largely reduced due to a flip-down of SerC, as well as lack of other kinetic barrier elements. The cryo-EM structure suggested that Sext and Scen have weaker Cl−-binding affinity than transporters (empty and with a semi-transparent Cl− sphere).

We carried out biophysical experiments to test some of these ideas using the EcCLC transporter (Figure 8A,D). EcCLC mutants were produced, purified and reconstituted into lipid vesicles for assessment of Cl− and H+ transport activity (Figure 8 and Figure 8—figure supplement 1) (Feng et al., 2012; Jayaram et al., 2008; Walden et al., 2007). The ideas outlined above predict that if the kinetic barrier in EcCLC is lowered it should behave more like a CLC channel (i.e., rapid Cl− permeation with decreased H+ transport activity). Cl− permeation is expected to be further increased if the Glugate is rendered persistently opened. As reported previously (Jayaram et al., 2008), opening of Glugate alone by the Glu-to-Ala mutation (E148A) abolishes the H+ transport activity, but it also reduced Cl− throughput by a factor of approximately 0.25. We reason that this is likely because the mutant still retains the kinetic barrier deterring Cl− ions from moving between Scen and Sint. Thus, while removal of the Glugate is sufficient to convert the transporter into a Cl− channel, a reduced kinetic barrier would be key to an increased Cl− throughput, an important feature of the native CLC channels.

![Figure 8.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig8-v2.jpg)

**Figure 8.:** (A) Schematics of the Cl− dump assay to measure the Cl− transport rate of EcCLC. Purified EcCLC protein is reconstituted into proteoliposomes containing 300 mM KCl inside. Buffer outside the liposomes was reduced to 150 mM K2SO4, lowering the Cl− concentration outside to ~1 mM. Transmembrane ion flux was initiated by addition of the K+-ionophore valinomycin (Vln) and the protonophore carbonyl cyanide-4-(trifluoromethoxy)phenylhydrazone (FCCP). Increase of the Cl− concentration outside the liposomes was monitored using a Cl−-selective electrode. (B) and (C) Examples of raw traces of Cl− dump assays. Vln/FCCP was added at t = 0. the gray arrowheads indicate addition of the β-octyl glucoside detergent to the reaction to release all Cl− from liposomes. (D) Schematics of the fluorescence-based H+ influx assay to measure the H+ transport activity of EcCLC. EcCLC proteoliposomes containing 450 mM KCl inside were diluted to buffer containing 450 mM potassium gluconate, lowering Cl− concentration outside to ~30 mM. The flux was initiated by addition of valinomycin at t = 100 s. As H+ are transported into the vesicles by EcCLC, intravesicular pH drops, which can be monitored by the quenching of 9-amino-6-chloro-2-methoxyacridine (ACMA) fluorescence. At the end of experiments (t = 1200 s), the protonophore carbonyl cyanide m-chlorophenylhydrazone (CCCP) was added to release all H+ from the vesicles. (E) and (F) Examples of normalized fluorescence traces of ACMA-based H+ influx assay. Shown are means (line and symbols) and s.e.m. (band) of 4 experiments.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/36629/elife-36629-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** Cl− (blue bars) and H+ (orange bars) transport rates of EcCLC mutants were calculated from raw data (Figure 8) as described in the Materials and methods section and shown as relative values with respect to the values of wildtype EcCLC. The Cl− transport measurement assay allows quantification of Cl− turnover rates, which was 800 s−1 per monomer for wildtype EcCLC. Error bars, s.e.m. (n = 4 or 5). n.d., not determined.

Previous studies have shown that when the E148A mutation is combined with a TyrC mutation (e.g., Y445S), the Cl− transport rate dramatically increases (Jayaram et al., 2008), demonstrating that efficient Cl− channel activity can be produced from EcCLC by altering its gates. However, we note that Y445S is rather unphysiological as TyrC is invariant among all CLC channels and transporters. Therefore, here we examined the effects of lowering the kinetic barrier in wild type EcCLC by mutating SerC or neighboring pore-lining amino acids, guided by the CLC-1 and CLC-K structures (Figure 8B,E and Figure 8—figure supplement 1). Trimming the side chain of SerC (S107G), with the intention of mimicking the flipped SerC in the CLC-K channel, increased the Cl− transport rate by a factor of 2, as previously reported (Jayaram et al., 2008). At the same time, this mutation lowered H+ coupling 3-fold, as one would expect due to the slippage of uncoupled Cl− ions. Next, since CLC-K has a polar amino acid (Thr) at one of its pore-lining residues (F348 of EcCLC), we further introduced a similar (F348A) mutation. This increased the Cl− throughput and almost abolished coupled H+ transport. Finally, by adding a Glugate mutation (E148A) to this double mutant the Cl− throughput was further increased. Compared to the E148A single mutant, the triple mutant (S107G/F348A/E148A) has a Cl− transport rate increased about 25-fold (Figure 8—figure supplement 1).

Similar results were obtained when mutations mimicking the CLC-1 channel were introduced to EcCLC (Figure 8C,F and Figure 8—figure supplement 1). While single mutations at the pore-lining amino acids (F348T or I356G) did not increase the Cl− transport rate, the double mutation (F348T/I356G) moderately increased the Cl− throughput (1.5-fold with respect to the wildtype). We note that this mutant displayed no measurable H+ transport activity. When the double mutant was combined with the Glugate mutation (E148A), which was used as a surrogate of the Glugate conformation observed in the CLC-1 structure, the Cl− throughput dramatically increased (22-fold with respect to the single E148A mutant; Figure 8—figure supplement 1). Single mutations (F348T or I356G) in the E148A background showed intermediate increases in Cl− throughput, suggesting that the effects of these mutations are somewhat additive.

## Discussion

The human CLC-1 channel exhibits interesting structural differences in the Cl− transport pathway and the gates, which can explain why this protein functions as a Cl− channel instead of a Cl−/H+ antiporter. The outer gate of the channel remains open because the carboxylic side-chain Glugate is located off to the side, away from the Cl− transport pathway (Figure 4). The inner kinetic barrier seems to be substantially lowered compared to transporters owing to a wider pore diameter near the cytosolic side (Figure 6). The pore widening is subtle, but distinctive enough to reveal a pattern separating channels and transporters at the protein sequence level (independent of the presence or absence of a Glugate) (Figure 6—figure supplement 1).

The position of the Glugate residue in CLC-1 is unique among CLC structures so far observed. The new Glugate position, where its carboxylic side chain is directed off to the side of the Cl− pathway, is enabled by a pocket that is large and hydrophilic (owing to its bifurcated pore structure) enough to accommodate Glugate’s side chain. This pocket may also exist in other Glugate-containing CLC channels (i.e., CLC-0 and CLC-2) but does not seem to exist in transporters because of a different arrangement of neighboring amino acids. It seems likely that this Glugate position is key to understanding why CLC-1 exhibits a stable open (i.e., conducting) state. On the basis of mutagenesis studies (Dutzler et al., 2003; Fahlke et al., 1997), the Glugate in CLC-0 and CLC-1 has been identified as a ‘voltage sensor’ because its removal abolishes voltage-dependent gating. From this observation, we would suggest that the position of Glugate (i.e., whether it resides off to the side, not occluding the pore, or within the pore) depends on the transmembrane voltage and generally dictates gating each CLC-1 monomer’s pore (also referred to as a ‘protopore’).

An unresolved issue raised by the new Glugate side chain conformation is this: if this conformation corresponds to the conducting state, how is it favored by low pH outside (Rychkov et al., 1996)? One possibility is the Glugate might be protonated in this conformation. Alternatively, low pH might stabilize a conformation of Glugate outside the pore, as in the EcCLC E148Q mutant. This conformation would also remove Glugate from the pore and permit conduction. Finally, the pH effect might be produced allosterically by protonation of an unidentified amino acid on the extracellular side. For example, both CLC-2 and CLC-K channels are inhibited by external pH <6.5, but it has been shown that a His residue (H532 of CLC-2 and H497 of CLC-K), which is located ~20 Å away from the pore, is responsible for this effect (Gradogna et al., 2010; Niemeyer et al., 2009). This issue remains unresolved for now.

Functional experiments using EcCLC provide support for our model that a low kinetic barrier in the cytosolic vestibule is necessary for high Cl− transport rates, which are general characteristics of native CLC channels (Figure 8 and also see (Jayaram et al., 2008)). The results indicate that a small increase in the pore diameter and a decrease in hydrophobicity of the pore lining can substantially lower the kinetic barrier. The structures, however, suggest that the extent might be somewhat less in the CLC-1 channel than in the CLC-K channel because of CLC-1’s SerC ‘transporter-like’ conformation. This is in fact consistent with the observation that CLC-1 has vestigial H+ transport activity (Picollo and Pusch, 2005) and a relatively slow Cl− throughput compared to that of CLC-K channels (1.2–1.8 pS versus 20–30 pS of CLC-K) (L'Hoste et al., 2013; Saviane et al., 1999; Scholl et al., 2006; Weinreich and Jentsch, 2001). What then causes the SerC to adopt its flipped-down conformation in the CLC-K channel? In CLC-K, position 425 contains a bulky amino acid (Y425), in contrast to other CLC proteins. In the canonical conformation SerC would sterically clash with Y425 (e.g., the center-to-center distance between the SerC-Oγ and Y425-Cε atoms would become 2.3 Å). We speculate that this steric incompatibility imposed by the unique Y425 might lead to the flipped-down conformation of SerC in the CLC-K channel.

The observed low Cl− occupancy at Scen in the CLC-1 structure has a striking resemblance to previous crystallographic observations on EcCLC, wherein Scen remained unoccupied when experiments were performed with TyrC mutants lacking H+ transport activity or with pseudohalides, which permeate without coupled H+ transport (Accardi et al., 2006; Nguitragool and Miller, 2006). It has been shown that in EcCLC, low Cl− occupancy correlates with low anion binding affinity (Picollo et al., 2009). This comparison suggests a reduced Cl− binding affinity at Scen in CLC-1, although further biophysical measurements will be necessary to confirm this. We speculate that this feature contributes to reduced H+ transport and increased Cl− conduction. Possible causes underlying the altered Cl− affinity include the shifted position of TyrC and subtle changes in positions and orientations of neighboring backbone nitrogen atoms coordinating the Cl− ion. For example, we note that CLC-0/1/2 channels have smaller, more flexible residues (Gly or Ala) at the G483 position, in contrast to Leu, Ile, or Val in CLC transporters.

CLC-1 is now the second structure of a channel-forming CLC, the first being CLC-K (Park et al., 2017). One of the major features giving rise to channel behavior is a more conductive pore. The structural differences giving rise to the higher Cl− conductivity are fairly subtle: the pore is slightly wider and the chemical properties a little different, accounting for what we propose to be a reduced kinetic barrier. We think there is a very important lesson here. Throughput rates in the range of 106 ions per second do not require a wide pore. We conclude that even if the pore in places is on average narrower than the ion, as long as the lining atoms are favorable to a conducting ion with respect to their electrostatic and chemical properties, and as long as they are sufficiently dynamic (i.e. they can move out of the way), then the ion can diffuse through. We offer as an example of this idea, the selectivity filter of K+ channels (Zhou et al., 2001). The atomic structures show us that in fact the pore’s radius between the K+ binding sites is smaller than the radius of a K+ ion. And yet some K+ channels approach throughput rates of 108 per second. It is not surprising to now understand that the radius of the pore in CLC channels and transporters is not very different.

The structures of CLC-1 and CLC-K channels support the idea that CLC channels are ‘broken transporters’ (Jayaram et al., 2008; Lísal and Maduke, 2008; Miller, 2006), where their channel function is built upon a transporter structure with modifications of the gates. The structures demonstrate that relatively small changes in the active site and ion transport pathway of a transporter gives rise to channel function.

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
      <td>Gene (Homo sapiens)</td>
      <td>CLCN1</td>
      <td>Synthetic</td>
      <td>UniProt: P35523</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293S GnTI-</td>
      <td>ATCC</td>
      <td>ATCC: CRL-3022 RRID:CVCL_A785</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>Sf9</td>
      <td>ATCC</td>
      <td>ATCC: CRL-1711 RRID:CVCL_0549</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pEG BacMam</td>
      <td>doi: 10.1038/nprot.2014.173</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION-2</td>
      <td>doi: 10.1016/j.jsb.2012.09.006</td>
      <td></td>
      <td>https://www2.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>doi:10.1038/nmeth.4193</td>
      <td></td>
      <td>http://msg.ucsf.edu/em/software/motioncor2.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CTFFIND4</td>
      <td>10.1016/j.jsb.2015.08.008</td>
      <td></td>
      <td>http://grigoriefflab.janelia.org/ctffind4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Alightpart_lmbfgs</td>
      <td>doi: 10.1016/j.jsb.2015.08.007</td>
      <td></td>
      <td>https://sites.google.com/site/rubinsteingroup/direct-detector-align_lmbfgs</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Rosetta</td>
      <td>RosettaCommons</td>
      <td>RRID:SCR_015701</td>
      <td>https://www.rosettacommons.org/software</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pymol</td>
      <td>PyMOL Molecular Graphics System, Schrödinger, LLC</td>
      <td>RRID:SCR_000305</td>
      <td>http://www.pymol.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>UCSF Resource for Biocomputing, Visualization, and Bioinformatics</td>
      <td>RRID:SCR_004097</td>
      <td>http://plato.cgl.ucsf.edu/chimera/</td>
    </tr>
  </tbody>
</table>

### Protein expression and purification

Human CLC-1 was expressed in HEK293 GnTI− cells (ATCC CRL-3022) by transduction using a modified baculovirus as described previously (Goehring et al., 2014; Park et al., 2017). A human CLC-1 coding sequence (CDS) was synthesized and inserted into a modified pFastBac vector, which contains a CMV promoter upstream of CDS. The expressed CLC-1 construct has a truncation of N-terminal 80 amino acids (residues 2–80), which were predicted to be unstructured, and its C-terminus is fused to enhanced green fluorescent protein (eGFP) (it also contains a HRV 3C protease cleavage sequence between CLC-1 and eGFP). The vector was used for transformation of DH10Bac E. coli cells (Invitrogen) to generate a baculovirus bacmid. Baculoviruses were produced by transfecting Spodoptera frugiperda (Sf9; ATCC CRL-1711) cells with the bacmid using Cellfectin-II (Invitrogen). Viruses were then amplified twice for large-scale transduction. HEK293 GnTI− cells were grown at 37°C in suspension in Freestyle 293 medium (Invitrogen) supplemented 2% FBS in the presence of 8% CO2. At a cell density of ~2.5 × 106 mL−1, baculovirus was added to the culture (6–8% v/v). After incubating at 37°C for ~0.5 day, the culture was supplemented with 10 mM sodium butyrate, then further incubated at 30°C for 2 days before harvest.

All protein purification steps were carried out at 4°C. Harvested HEK293 cells (typically from 1 to 2 L) were suspended in a buffer containing 50 mM Tris-HCl pH 7.5, 300 mM NaCl, 1 mM dithiothreitol (DTT), 1 mM ethylenediaminetetraacetic acid (EDTA), and 10% v/v glycerol, and supplemented with protease inhibitors (50 μM leupeptin, 1 ug/mL aprotinin, 1 uM pepstatin and 1 mM phenylmethylsulfonyl fluoride). 1% dodecyl-β-maltoside (DDM) and 0.2% cholesteryl semisuccinate (CHS) were added to the cell suspension. After extraction for 1.5 h, the lysate was clarified by centrifugation (Beckman Type 70Ti rotor, 40,000 RPM, 1.5 h). The clarified lysate was then mixed with 5 mL of CNBr-sepharose beads (GE Healthcare) coupled with anti-GFP nanobody for 2.5 h. Beads were washed on 60 mL of the buffer containing 0.04% DDM and 0.004% CHS. Bound protein was released from beads by overnight incubation with 5 mL buffer containing 0.04% DDM, 0.004% CHS, and 0.2 mg HRV 3C protease. The retrieved protein was concentrated to 0.5–1.0 mL using Amicon Ultra (100 kDa cutoff; EMD Millipore) and applied to a Superose 6 300/10 GL column (GE Healthcare) equilibrated with 20 mM Tris-HCl pH 7.5, 100 mM NaCl, 1 mM DTT, 0.5 mM EDTA, 0.04% DDM, and 0.004% CHS. The peak fractions were pooled and concentrated to ~4 mg/mL, and immediately used for cryo-EM grid preparation.

The wild-type and mutant E. coli CLC transporter proteins (EcCLC) were expressed and purified essentially as described previously (Dutzler et al., 2002). E. coli BL21 (DE3) (Novagen) was transformed by pET28b vector containing EcCLC CDS, the C-terminal of which was fused to a hexa-histidine tag (His-tag). E. coli cells were grown at 37°C in Luria broth (LB) medium containing 60 μg/mL kanamycin until they reached OD600 of 1.2. The expression was induced by addition of 0.2 mM isopropyl β-D-1-thiogalactopyranoside (IPTG). The cells were further grown at 21°C for ~16 h before harvest by centrifugation. The cell pellets were frozen with liquid N2 and stored at −80°C until purification. The frozen E. coli cells (typically from 3 L) were thawed and suspended in 20 mM Tris-HCl pH 7.5 and 150 mM NaCl. The cells were lysed by sonication (1 mM PMSF and 50 uM leupeptin were supplemented before the lysis), and 2% decylmaltoside (DM) and 10 mM imidazole were added. After 2-h gentle stirring at 4°C, the lysate was spun for 1 h at 15,000 rpm (Beckman JA-17 rotor). The supernatant was mixed with 5 mL of Talon cobalt agarose beads (Takara Bio) for 2 h. The beads were packed in a column and washed with 25 mL of lysis buffer containing 20 mM imidazole, 12.5 mL of buffer containing 30 mM imidazole, and then 12.5 mL of buffer containing 40 mM imidazole. The protein was eluted by buffer containing 200 mM imidazole. The eluate was concentrated to ~0.5 mL using Amicon Ultra (50 kDa cutoff). The His-tag was removed by adding 0.5 U of Lys-C endopeptidase (Roche) and incubating the mixture at 23°C for 3 h. The eluate was applied to a Superdex 200 300/10 GL column (GE Healthcare) equilibrated with 25 mM Tris-HCl pH 7.5, 100 mM NaCl, 1 mM DTT, 0.5 mM EDTA, 10% glycerol, and 0.3% DM. The peak fraction was collected and used for reconstitution without freezing.

### Cryo-EM analysis

3 μL of purified CLC-1 protein was applied to a glow-discharged gold (or copper for the third dataset) Quantifoil R 1.2/1.3 holey carbon grids (Quantifoil) and incubated for 15 s. Grids were then blotted for 1.5–2.0 s at 4°C and 90% humidity and plunge-frozen in liquid-nitrogen-cooled liquid using Vitrobot Mark III (FEI).

The data sets were collected on a Titan Krios electron microscope (FEI) operated at an acceleration voltage of 300 kV. Dose-fractionated images were recorded on a K2 Summit direct electron detector (Gatan) operated in super-resolution counting mode (a super-resolution pixel size of 0.515 Å) using SerialEM software (Mastronarde, 2005). For the first two datasets (2293 movies), the dose rate was 8 e− per pixel per s, and total exposure time was 10 s with 0.2 s for each frame (total cumulative dose of ~75 e− per Å2 over 50 frames). For the third dataset (1998 movies), the dose rate was 5.33 e− per pixel per s, and total exposure time was 15 s with 0.15 s for each frame (total cumulative dose of ~75 e− per Å2 over 100 frames). Defocus values were set from −0.8 μm to −2.4 μm.

Dose-fractionated movies were corrected for gain and motion by MotionCor2 (Zheng et al., 2017). Also the pixels were binned to 1.03 Å/pixel during this process. Defocus values were estimated using CTFFIND4 (Rohou and Grigorieff, 2015) on the summed micrographs produced by MotionCor2 (using the full dose). Particles were picked automatically by RELION2 (Kimanius et al., 2016; Scheres, 2012), and obvious artifacts, such as ice contamination and carbon foil, were removed by manual inspection. Total 725,959 particles were extracted with a box size of 320 pixels and subjected to reference-free 2D classification (performed separately per dataset). Based on visual inspection of quality of 2D average classes, 411,260 particles were pooled. This particle set was then applied to the alignpart_lmbfgs program (Rubinstein and Brubaker, 2015) to perform per-particle motion correction (particle polishing). The particle polishing step was done using motion-corrected (whole-frame-only) movie stacks, which were first produced by MotionCor2 and then 2x or 4x frame-binned by relion_image_handler (resulting in a total of 25 frames per movie and 3 e− per Å2 per frame). Particles were extracted from 1 to 13 frames (total dose of 39 e− per Å2) and using alignparts_lmbfgs’s exposure filter. The ‘polished’ particles were subjected to another round of clean-up by RELION 2D classification (resulting in 350,750 particles). The initial model was generated by RELION auto-refine using particle images from the first dataset and a 50 Å lowpass-filtered model from the CLC-K channel density map (excluding antibody fragments; (Park et al., 2017)). All 350,750 polished particle images were subjected to auto-refine (RELION 2.1), using the updated initial model and a soft mask surrounding the protein and detergent micelle density. This refinement step produced a 3.8 Å map (Figure 2—figure supplement 1B). This was then followed by a RELION 3D classification procedure skipping image alignment (sorting into five classes). Particles from two classes were combined (175,613 particles) by visual inspection in UCSF Chimera (Pettersen et al., 2004) and subjected to RELION auto-refine again. During the later iterations (upon entering the local search mode), the soft mask was updated to contain only the transmembrane or cytosolic domain (focused refinement). The resolution of the final TMD domain map (3.36 Å) was estimated by RELION based on gold-standard Fourier shell correlation (FSC) of independently refined half maps (using the 0.143 cut-off criterion). The focused refinement of the cytosolic domain was performed by 2 iterations of local refinement using reference maps in which information at lower than 4.6 Å resolution were combined from the previous iteration’s two half maps. The nominal resolution of the final CTD map is 4.1 Å, but this is likely somewhat overestimated (the resolution before the focused refinement is 4.5 Å). Local resolution was estimated using RELION2’s postprocess program (Figure 2—figure supplement 1A). Unless stated otherwise, the TMD map shown in figures is a combined map, which was sharpened (B-factor of −97.9 Å2) and lowpass-filtered at 3.36 Å by RELION’s automatic postprocess procedure using user-provided soft masks. The TMD map in Figure 2C and Videos 1 and 2 was sharpened with a B-factor of −97.9 Å2 and low-pass filtered at 3.1 Å. The CTD density map was low-pass filtered at 4.2 Å without B-factor sharpening.

### Atomic model building

An initial model of the CLC-1’s TMD was generated by the SWISS-MODEL homology modelling webserver using the CLC-K model (PDB ID: 5TQQ) as a template. The output model was fit into the TMD density map using Chimera and rebuilt using Coot (Emsley et al., 2010). Model refinement was done in real space using Rosetta 3.7 using a script developed for cryo-EM model refinements (Wang et al., 2016) (Table 1). The first round was performed with an asymmetric unit model, and the five best output models were selected based on Rosetta’s energy scores. A consensus model was generated by combining fragments from these models based on the fit to the density map. The subsequent two rounds of Rosetta refinement were done with two-fold symmetry imposed. To prevent overfitting, the weight between Rosetta energy scores and the fit to the experimental density map was adjusted, and test refinement was performed on one of two half maps. The output models were then compared to both half maps by calculating FSC (Figure 2—figure supplement 2). To this end, we used a weight of 25, which gave us a good fitting to the map and negligible overfitting. While the first two rounds of refinement were done using one of the two half maps, the last round was performed on the combined map to maximize the use of experimental data in refining the model (see Figure 2—figure supplement 2 for FSC between the final model and the combined map). The final model was selected among ~2000 Rosetta-generated models based on Rosetta’s total score (top 20%) and the fit of side chains to the map (visual inspection). No further modifications were made except for Cl− ions at Sext and Sint, which were modelled in Coot (Coot’s real-space refinement was used) since Rosetta could not refine Cl− ions. Modelling of CTD was done similarly using Rosetta, but using a crystal structure of CLC-0 CBS domain as an initial model. A weight of 7 was used, and the refinement was limited to 4.5 Å resolution. As side chains were not visible in the CTD density map, we removed all side chain atoms from the final CTD model generated by Rosetta. The following segments were not modelled as they were invisible in the density maps: N–115, 251–262 (a cytosolic segment between αF and αG), 671–796 (a loop in CTD), and 877–988(C). MolProbity was used for structural validation of models (Table 1) (Chen et al., 2010).

**Table 1.**
 Model refinement and validation statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>TMD</th>
      <th>CTD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">Rosetta Model Refinement</td>
    </tr>
    <tr>
      <td>Map pixel size (Å)</td>
      <td>1.03</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td>Map sharpening B-factor (Å2)</td>
      <td>−97.9</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Map lowpass filter (Å)</td>
      <td>3.36</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>Refinement resolution limit (Å)</td>
      <td>3.36</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>Number of atoms</td>
      <td>14,536</td>
      <td>5124†</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>14,536</td>
      <td>5124†</td>
    </tr>
    <tr>
      <td>Non-hydrogen atoms</td>
      <td>7152</td>
      <td>2550†</td>
    </tr>
    <tr>
      <td>Hydrogen atoms</td>
      <td>7384</td>
      <td>2574†</td>
    </tr>
    <tr>
      <td>Non-protein</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Refined Model Statistics</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Average B-factor (Å2)</td>
      <td>24.59</td>
      <td>161.34</td>
    </tr>
    <tr>
      <td>r.m.s deviations</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond length (Å)</td>
      <td>0.02</td>
      <td>0.02†</td>
    </tr>
    <tr>
      <td>Bond angle (°)</td>
      <td>1.42</td>
      <td>1.55†</td>
    </tr>
    <tr>
      <td>Ramachandran Plot</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored (%)</td>
      <td>96.75</td>
      <td>96.15†</td>
    </tr>
    <tr>
      <td>Outliers (%)</td>
      <td>0.43</td>
      <td>0.64†</td>
    </tr>
    <tr>
      <td>MolProbity</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Clash score*/percentile</td>
      <td>1.38 (99 %)</td>
      <td>0.39# (99%)</td>
    </tr>
    <tr>
      <td>Rotamers</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored (%)</td>
      <td>99.48%</td>
      <td>100.00# %</td>
    </tr>
    <tr>
      <td>Outliers (%)</td>
      <td>0.00%</td>
      <td>0.0† %</td>
    </tr>
    <tr>
      <td>Overall score/percentile</td>
      <td>1.07 (100 %)</td>
      <td>0.90† (100%)</td>
    </tr>
  </tbody>
</table>

_*number of steric overlaps >0.4 Å per 1000 atoms.†numbers and scores before truncation of side chain atoms._

Detection of pores and estimation of pore radii (Figures 3 and 6) were performed using Caver (Chovancova et al., 2012). In the case of EcCLC (PDB ID: 1OTS) and CmCLC (PDB ID: 3ORG), Glugate (E148 of EcCLC and E210 of CmCLC) was mutated to Ala before estimation since its side chain is blocking the Cl− pathway. In the case of bovine CLC-K (PDB ID: 5TTQ) (Figure 6B), we changed the rotamer conformation of V166 (equivalent to Glugate) from original gauche+ (63°) to trans (175°). With the original rotamer, the constriction around Sext was found to be too narrow (radius < 0.9 Å) for pore detection. Because both rotamers can be fitted equally well into the cryo-EM density map, it is uncertain which is right or if both can exist in the protein. We note that trans is in general an energetically more favored rotamer than gauche+. Water accessibility in CLC-1’s vestibules (Figure 4B) was probed using HOLLOW (Ho and Gruswitz, 2008) using a probe radius of 1.4 Å. Protein electrostatics were calculated using the Adaptive Poisson-Boltzmann Solver (Baker et al., 2001) with a parameter of 150 mM monovalent salt concentration. UCSF Chimera and PyMOL (Schrödinger) were used to prepare structure figures.

### Reconstitution of E. coli CLC transporter mutants and flux assays

To reconstitute EcCLC mutant proteins for Cl− efflux assays, E. coli polar lipids in chloroform (Avanti Polar Lipids) was dried in a glass tube with an argon stream, followed by overnight incubation in a vacuum chamber. Dried lipids were suspended by sonication in buffer (RB-Cit) containing 25 mM sodium citrate (pH 4.6) and 300 mM KCl and then solubilized with 35 mM (3-((3-cholamidopropyl) dimethylammonio)−1-propanesulfonate) (CHAPS; Anatrace) and additional sonication. Purified EcCLC protein was added to the lipid/CHAPS mixture in a protein-to-lipid ratio of 1:5000 (wt:wt). After 30 min incubation at 23°C, the mixture was dialyzed against RB-Cit buffer to remove CHAPS. The dialysis was carried out at 4–10°C for 48 h with three additional buffer changes. To reconstitute EcCLC proteins for fluorescence-based flux assays, the same procedure was used except that buffer containing 10 mM HEPES-NaOH (pH 7.0) and 450 mM KCl instead of RB-Cit and a protein-to-lipid ratio of 1:500 (wt:wt) were used. After dialysis, proteoliposome vesicles were aliquoted, flash-frozen with liquid N2, and stored at −80°C until use.

The Cl− efflux (dump) assays were performed essentially as described previously (Jayaram et al., 2008; Walden et al., 2007). A frozen aliquot of vesicles was thawed and briefly sonicated in the bath sonicator (Branson). Vesicles were extruded through a 0.4 μm polycarbonate filter 19 times (Avanti Mini-Extruder). The extruded vesicles were desalted with a spin column packed with Sephadex G-50 resin (~2.5 mL bed volume) equilibrated with buffer (EB) containing 25 mM sodium citrate (pH 4.7), 250 mM K2SO4, and 1 mM NaCl. 100 μL of the desalted vesicles were then mixed with 900 μL EB in a chamber equipped with a magnetic stirrer and Cl−-selective electrode (Fisher Accumet). Changes in extravesicular Cl− concentration was monitored over time by the Cl−-selective electrode connected to a computer through a digitizer (DataQ). To calibrate the electrode, 0.1 mM NaCl was added before the vesicles were added. Flux was initiated by addition of 2 μg/mL valinomycin and 1 μg/mL carbonyl cyanide-p-trifluoromethoxyphenylhydrazone (FCCP) or 3 μg/mL valinomycin (for E148A mutants). At the end of assays, 30 mM octyl β-glucoside (Anatrace) was added to release all Cl− content from vesicles. Calculation of Cl− transport rates were carried out as described previously (Walden et al., 2007). Volume changes by dialysis, extrusion, and desalting steps were included in calculation.

The fluorescence-based flux assays were performed as follows based on (Feng et al., 2012). A frozen aliquot of vesicles was thawed and briefly sonicated in a bath sonicator. 3 μL of vesicles were mixed with 40 μL of assay buffer containing 20 mM HEPES-NaOH (pH 7.0), 450 mM K-gluconate and 4 μM ACMA in a well of a 384-well fluorescence assay. After measuring initial AMCA fluorescence intensity (λEx=410 nm, λEm=490 nm), Cl−/H+ flux was initiated by addition of 1 μM valinomycin, followed by monitoring fluorescence over time (10 s intervals) using a plate reader (Tecan Infinite M1000) at 27°C. Note that there is a dead time for measurement between t = 80 s to t = 120 s due to handling of the plate during valinomycin addition. Valinomycin was added to the reactions at t = ~100 s. As a control, 0.9 μM carbonyl cyanide 3-chlorophenylhydrazone (CCCP) was added to the assay mixture at the end of the experiment to dissipate an accumulated H+ gradient. To measure relative H+ transport activity of each mutant, time required to fluorescence reaches 75% (or 85% in the case of S106G/F348A double mutant) of the initial fluorescence upon addition of valinomycin was calculated. This time value was then inversed and normalized with respect to a value obtained with wild-type EcCLC.

### Data availability

Cryo-EM density maps of human CLC-1 have been deposited in the electron microscopy data bank under accession code EMD-7544 and 7545. Atomic coordinates have been deposited in the protein data bank under accession code 6COY and 6COZ.
