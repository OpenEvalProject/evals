# Improved ANAP incorporation and VCF analysis reveal details of P2X7 current facilitation and a limited conformational interplay between ATP binding and the intracellular ballast domain

## Authors

- Anna Durner<sup>1</sup> ([ORCID: 0000-0002-0993-8869](https://orcid.org/0000-0002-0993-8869))
- Ellis Durner<sup>2</sup> ([ORCID: 0000-0002-4461-9257](https://orcid.org/0000-0002-4461-9257))
- Annette Nicke<sup>1</sup> ([ORCID: 0000-0001-6798-505X](https://orcid.org/0000-0001-6798-505X)) †

### Affiliations

1. Walther Straub Institute of Pharmacology and Toxicology, Faculty of Medicine, LMU Munich Munich Germany ([ROR:05591te55](https://ror.org/05591te55))
2. Lehrstuhl für Angewandte Physik and Center for Nanoscience, LMU Munich Munich Germany ([ROR:05591te55](https://ror.org/05591te55))

† Corresponding author

## Abstract

The large intracellular C-terminus of the pro-inflammatory P2X7 ion channel receptor (P2X7R) is associated with diverse P2X7R-specific functions. Cryo-EM structures of the closed and ATP-bound open full-length P2X7R recently identified a membrane-associated anchoring domain, an open-state stabilizing “cap” domain, and a globular “ballast domain” containing GTP/GDP and dinuclear Zn2+-binding sites with unknown functions. To investigate protein dynamics during channel activation, we improved incorporation of the environment-sensitive fluorescent unnatural amino acid L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP) into Xenopus laevis oocyte-expressed P2X7Rs and performed voltage clamp fluorometry. While we confirmed predicted conformational changes within the extracellular and the transmembrane domains, only 3 out of 41 mutants containing ANAP in the C-terminal domain resulted in ATP-induced fluorescence changes. We conclude that the ballast domain functions rather independently from the extracellular ATP binding domain and might require activation by additional ligands and/or protein interactions. Novel tools to study these are presented.

## Introduction

P2X receptors (P2XR) are trimeric non-selective cation channels that are activated by extracellular adenosine triphosphate (ATP). The structure of a single P2X subunit has been compared to a dolphin, with two transmembrane domains (TM1 and TM2) that form the ‘fluke’, and a large extracellular domain, comprising the ‘body’, left and right ‘flippers’, and a ‘head’ domain that reaches over one of three inter-subunit ATP binding sites (Kawate et al., 2009). The intracellular N- and C-termini are short in most P2X subtypes and have only been resolved in the open state of the P2X3R and, more recently, in the open and closed states of the P2X7R (Mansoor et al., 2016; McCarthy et al., 2019). The pro-inflammatory P2X7 subtype is expressed in immune cells and considered an important drug target. In contrast to the other P2XR family members, it has a low ATP sensitivity, shows complete lack of desensitization, and contains a large intracellular C-terminus (240 amino acids [aa]), which mediates diverse downstream effects such as interleukin secretion, plasma membrane permeabilization, blebbing, phosphatidylserine flip, and cell death (Kopp et al., 2019). The recently determined cryo-EM structures of the full-length rat P2X7R in the apo/closed and ATP-bound open states (McCarthy et al., 2019) did not only elucidate details of P2X desensitization, but finally unveiled the structure of the large P2X7 C-terminus. Accordingly, intertwined β-strands from all three subunits form an open state-stabilizing ‘cap domain’, that was also found in the P2X3R (Mansoor et al., 2016). In the P2X7R, however, this ‘cap’ is stabilized by a highly palmitoylated membrane-associated ‘Cys-anchor’ domain, which prevents desensitization. The remaining residues 393–595 fold into a dense globular structure (the so-called ‘ballast domain’), which contains a novel guanosine nucleotide binding motif and a dinuclear zinc binding site. A stretch of 27–29 aa (S443-R471) was not resolved, and it is unclear if each ballast domain is formed by a single subunit or if a domain swap occurs between subunits (McCarthy et al., 2019). While these structures represent a milestone in P2X7 research, the transition dynamics between receptor states in a cellular environment as well as the molecular function of the ballast domain and how it is affected by ATP binding remain unclear. Likewise, the molecular mechanism of current facilitation, a P2X7-characteristic process that describes faster and/or increased current responses upon repeated ATP application, is not understood. In this study, we set out to determine conformational changes associated with P2X7-specific functions by voltage clamp fluorometry (VCF). This method allows simultaneous recording of current responses and associated molecular movements that are reported by an environment-sensitive fluorophore. We have previously used site-specific cysteine-substitution and the thiol-reactive fluorophore tetramethyl-rhodamine-maleimide (TMRM) to show a closing movement of the head domain during activation of the oocyte-expressed P2X1R (Lörinczi et al., 2012). However, this procedure is limited to extracellularly accessible residues. To investigate intracellular rearrangements, we therefore employed the fluorescent unnatural amino acid (fUAA) L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP) (Lee et al., 2009). This can be site-specifically incorporated into a protein by repurposing the amber stop codon (TAG) and introducing a corresponding suppressor tRNA (CUA anticodon) loaded with ANAP. A plasmid encoding an ANAP-specific bio-orthogonal suppressor tRNA/aminoacyl-tRNA synthetase pair (Chatterjee et al., 2013) has been obtained by co-evolution and selection (Lee et al., 2009) and was successfully used to study voltage-gated and ligand-gated ion channels (Andriani and Kubo, 2021; Kalstrup and Blunck, 2018; Kalstrup and Blunck, 2013; Soh et al., 2017; Wulf and Pless, 2018). This stop-codon suppression can, however, lead to premature translational termination or aberrant stop-codon substitution (read-through) (Braun et al., 2020; Kalstrup and Blunck, 2017; Klippenstein et al., 2018; Pless et al., 2015; Poulsen et al., 2019).

Here, we provide an improved method for fUAA incorporation into Xenopus laevis oocyte-expressed proteins and analyzed membrane surface expression and functionality for a total of 61 P2X7R mutants with ANAP substitutions in the extracellular head domain, the second transmembrane domain (TM2), and the intracellular N- and C-termini. Using VCF, we identified 19 positions in which ANAP reported ATP-induced localized rearrangements. To further expand the VCF toolbox, we demonstrate simultaneous recordings of fluorescence changes from ANAP in combination with other fluorophores. We conclude from our data that (i) current facilitation is intrinsic to the P2X7 protein and likely caused by a change in gating and (ii) the cytoplasmic ballast functions rather independently from the extracellular ligand binding domain and might require activation by additional ligands or protein interactions.

## Results

### Improved ANAP incorporation by cytosolic co-injection of mutated X. laevis eRF1 cRNA

To implement and optimize a protocol for incorporation of ANAP into Xenopus oocyte-expressed protein, we initially used the P2X1R as it was already intensively studied in our lab (Lörinczi et al., 2012) and has functional similarity with the P2X3R, which at the beginning of this study, represented the only P2XR for which the intracellular termini were resolved (Mansoor et al., 2016). Using the original 2-step-injection protocol (Kalstrup and Blunck, 2017; Kalstrup and Blunck, 2013) and a simplified procedure where all components required for the expression of UAA-containing receptors are injected simultaneously (Figure 1A and C), we introduced ANAP into non-conserved positions within the N-terminally His-tagged P2X1R N- and C-termini (position 10 and 388, respectively, ANAP substitutions indicated by *) and compared the formation of full-length and truncated receptors in the plasma membrane by SDS-PAGE. As seen in Figure 1B, ANAP-containing P2X1Rs were efficiently expressed and virtually no read-through product was detected in the absence of ANAP. The new protocol resulted in less variable protein expression but also a reduced ratio of full-length and truncated His-P2X1 EGFP protein (Figure 1D). The relative amount of full-length protein was neither increased by different forms of ANAP application nor by variation of injection protocols (Figure 1—figure supplement 1A and B). Therefore, we tested if a mutated eukaryotic release factor (eRF1(E55D)), which was previously shown to favor UAA-incorporation over translational termination in HEK293T cells (Gordon et al., 2018; Schmied et al., 2014) could also be used in the Xenopus oocyte expression system. Indeed, co-injection of either purified X. laevis eRF1(E55D) protein (Figure 1—figure supplement 1B) or the respective in vitro synthesized cRNA (Figure 1C and D) resulted in a more than threefold higher ratio of full-length and truncated receptor constructs compared to the 1-step injection method without eRF1(E55D) and a smaller standard deviation compared to the 2-step injection method (1-step+eRF1(E55D): 1.469±0.229; 1-step: 0.418±0.082; 2-step: 1.603±0.933; mean ± S.D.). The applicability of this approach was confirmed for the hα1 glycine receptor (GlyR) A52* mutant (Figure 1—figure supplement 1C; Soh et al., 2017). In conclusion, this optimized protocol led to more reproducible expression and increased formation of full-length ANAP-labeled receptors and was used in all following experiments.

![Figure 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig1-v2.jpg)

**Figure 1.:** (A) Molecular structure of L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP) and schematic representation of the 2-step injection method for site-specific ANAP incorporation using the amber stop-codon (UAG) and a plasmid containing the orthogonal tRNA/tRNA-synthetase pair. (B) Representative SDS-PAGE analysis of plasma membrane-expressed ANAP-labeled (S10* or S388*) rat P2X1Rs (46 kDa without glycosylation). A C-terminal EGFP-tag (27 kDa) was added as indicated to enable detection of premature termination at position 388. Oocytes were injected as shown in A and labeled with membrane impermeable Cy5-NHS ester. His-tagged P2X1Rs were extracted in 0.5% n-dodecyl-β-D-maltoside, purified via Ni2+-NTA agarose, and separated by SDS-PAGE (8%). Noninjected oocytes and oocytes injected only with the plasmid pANAP, P2X1 cRNA without the amber stop codon (Wt), or without ANAP (as indicated) served as controls. Note, that twice the amount of protein was loaded for P2X1(S10*). Ø indicates empty lanes. Two to three independent experiments were performed. (C) Representation of the 1-step injection method and all components required for UAA-labeling plus optional X. laevis eRF1(E55D) cRNA (left) and (right) scheme of protein translation termination by eRF1 (upper panel) and how overexpression of the mutated form of eRF1 favors amber-encoded fUAA incorporation by outcompeting endogenous eRF1 (lower panel). (D) Comparison of Cy5-labeled membrane-expressed full-length and truncated His-rP2X1-EGFP(388*) ratios upon expression by the 2-step and 1-step injection method with or without eRF1(E55D) co-expression. A representative SDS-PAGE gel (prepared as in B) and statistical analysis of data from 6 to 11 experiments including oocytes from 4 to 6 different X. laevis frogs per group are shown. Data are represented as mean ± S.D., and significance was determined by a two-tailed unpaired Welch’s t-test and is indicated as *p<0.05 and ****p<0.0001.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Comparison of ANAP-trifluoroacetic salt (TFA, a and b indicate two different batches) and membrane-permeable ANAP methyl ester (OMe) and application forms (injection and/or incubation in 2 mM solution). In the last two lanes, a twofold higher concentration (500 mM) was used for injection. Lanes shown in the same figure are from the same gel but rearranged for clarity. (B) Left: Comparison of ANAP-OMe application forms (injection and incubation as above) and effect of co-injected X. laevis eRF1(E55D) (as purified protein or as cRNA, as indicated) for the 1-step and the 2-step injection method. Right: Effect of different injection intervals. tRNA synthetase was expressed first, either from the pANAP plasmid (injected into the nucleus) or from the in vitro synthesized cRNA (injected into the cytoplasm) as indicated. All other components were then injected into the cytoplasm after the shown intervals. Note that the gel was rearranged for clearer presentation and that lanes marked with a hashtag are shown twice. (C) The optimized 1-step injection protocol with and without co-injection of eRF1(E55D) applied to hα1 GlyR(A52*) and P2X1(S388*)-EGFP.

### Evaluation of plasma membrane expression of full-length ANAP-containing P2X7Rs

Next, we incorporated ANAP into the P2X7R in sites chosen based on previous structure-function studies and the cryo-EM structures (McCarthy et al., 2019). As a positive control, we first introduced ANAP into the head domain (Figure 2A and B), which is known to undergo substantial movements and/or ligand interactions with clear changes of TMRM fluorescence in the P2X1R (Lörinczi et al., 2012) and P2X7R (Figure 2—figure supplement 1A). Next, based on the comparison of the P2X4 and P2X3 crystal structures in the open and closed states (Hattori and Gouaux, 2012; Kawate et al., 2009; Mansoor et al., 2016), and the identification of the human P2X7 channel gate and selectivity filter around residue S342 (Pippel et al., 2017), we selected positions in the second transmembrane helix. Finally, we introduced ANAP throughout the intracellular region in positions that we suspected to undergo conformational changes upon channel activation, as well as in six positions in the unresolved 29 aa stretch. As shown in Figure 2C, all constructs with ANAP substitutions in the N-terminus and the head domain as well as three out of four constructs with substitutions in TM2 were formed in full length, indicating that receptors that are truncated before or within TM2 are retained in the endoplasmic reticulum and likely undergo degradation. Interestingly, ANAP incorporation into G338 completely prevented membrane incorporation while cysteine substitution in the equivalent position of human P2X7R led previously to surface-expressed, but non-functional receptors (Pippel et al., 2017).

![Figure 2.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig2-v2.jpg)

**Figure 2.:** (A, B) Surface representations of the rat P2X7 Cryo-EM structure in the open state (PDB ID: 6u9w). The different domains (A) and selected sites of ANAP substitutions (B) are indicated in one subunit while the two other subunits are shown in gray and wheat, respectively. (C) Evaluation of surface expression and functionality of P2X7Rs generated from constructs containing an amber stop codon in the indicated positions. X. laevis oocytes expressing the constructs were labeled with membrane-impermeant Cy5-NHS ester. His-tagged P2X7Rs were extracted in 0.5% n-dodecyl-β-D-maltoside, purified via Ni2+ NTA agarose, and analyzed by SDS-PAGE (8%). Symbols indicate current responses to 0.3 mM ATP as determined by two-electrode voltage clamp recordings in the voltage clamp fluorometry setup: +, functional and currents comparable to wt P2X7 after 2–4 days of expression; (+), functional and currents comparable to wt P2X7 after 5–7 days of expression; –, not functional or currents ≤0.5 μA and not reproducible after 4 days. Representative data from two to five independent biochemical experiments are shown.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) To estimate plasma membrane expression (upper gel) and accessibility of introduced cysteine residues (lower gel), intact oocytes expressing the indicated cysteine-substituted P2X7R mutants were either labeled with the membrane-impermeant amino-reactive Cy5-NHS ester or with TMRM. Purified His-tagged protein was visualized by fluorescence scanning. Below: Box plot summarizing results from TMRM-labeled oocytes expressing indicated P2X7R mutants with ΔF/F% representing the maximum fluorescence signal during a 15-s ATP application (300 μM). Numbers of recordings are given in brackets and a representative voltage clamp fluorometry (VCF)-recording (-60 mV) of a TMRM-labeled oocyte expressing P2X7(S124C) is shown. (B) Summary of fluorescence (violet and blue) changes of oocytes expressing P2X7Rs containing ANAP in the indicated positions within the head domain and a representative VCF-recording (at –30 mV) from an oocyte expressing P2X7 with ANAP in position 124 (P2X7(S124*)). Note that in case of mutants P120*, E121*, and P123* less than three recordings fulfilled the inclusion criteria described in Material and methods. Original recordings have also been deposited with Dryad and summarized and assigned in Table 1—source data 1.

Starting from T357 in the C-terminus, introduction of the amber stop codon resulted in variable ratios of truncated and full-length receptors. Surface expression of full-length receptors was particularly low for constructs containing ANAP in the C-terminal cap (K387*, C388*) and ballast (I577*) domains, while it was most efficient for ANAP-substitutions in positions 517–537 (in particular L527* and E537*) and in the very C-terminus (Y595* and 596*).

In summary, most substitutions within the C-terminus led to a dominant formation of truncated P2X7 protein besides full-length receptors. Nevertheless, the majority of these constructs showed clear current responses (Figure 2C, Table 1). Since the truncated forms were not expected to interfere with the fluorescence signal, functional constructs that were expressed at least partly in full length were further analyzed by VCF.

**Table 1.**
 Summary of surface expression, current responses (ΔI), and L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid fluorescence changes (%ΔF/F) of the investigated P2X7 mutants.Table 1—source data 1.Summarized data for Table 1 with assignment to the original VCF recordings; also including data from Figure 2—figure supplement 1B (box plot); Figure 3C, D, E, F; Figure 3—figure supplement 3C; Figure 4B, C, D; Figure 4—figure supplement 1B; and Figure 5B, C, D. The respective original recordings are deposited with Dryad.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Position</th>
      <th colspan="2">Surface expression</th>
      <th rowspan="2">ΔI</th>
      <th colspan="2">%ΔF/F Filter set 1</th>
      <th colspan="2">%ΔF/F Filter set 2</th>
    </tr>
    <tr>
      <th>Full-length</th>
      <th>Truncated</th>
      <th>430–470 nm</th>
      <th>470–500 nm</th>
      <th>430–490 nm</th>
      <th>&gt;500 nm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">N-terminus</td>
      <td>A3</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>C5</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>W7</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>(↑)</td>
      <td>(↑)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>V10</td>
      <td>+</td>
      <td>–</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(↑)</td>
      <td>(↑)</td>
    </tr>
    <tr>
      <td>F11</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>K17</td>
      <td>+</td>
      <td>–</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td rowspan="9">Head domain</td>
      <td>P120</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>(↑)</td>
      <td>(↑)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>E121</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>Y122</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↓</td>
      <td>↓</td>
      <td>↓</td>
      <td>↓</td>
    </tr>
    <tr>
      <td>P123</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>↓</td>
      <td>↓</td>
    </tr>
    <tr>
      <td>S124</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
      <td>↓</td>
    </tr>
    <tr>
      <td>R125</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
      <td>↓</td>
    </tr>
    <tr>
      <td>G126</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>K127</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↓</td>
      <td>↓</td>
      <td>↓</td>
      <td>↓</td>
    </tr>
    <tr>
      <td>Q128</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>↑</td>
      <td>↓</td>
    </tr>
    <tr>
      <td rowspan="4">TM2</td>
      <td>G338</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>S339</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>T340</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>– / ↓</td>
      <td>↑</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>L341</td>
      <td>+</td>
      <td>–</td>
      <td>+</td>
      <td>(↑)</td>
      <td>(↑)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td rowspan="19">C-terminus</td>
      <td>N356</td>
      <td>+</td>
      <td>–</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>T357</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>Y358</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>A359</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>T361</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(↓)</td>
      <td>–</td>
      <td>↓</td>
    </tr>
    <tr>
      <td>R364</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>C371</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>A378</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>n.d.</td>
      <td>n.d.</td>
    </tr>
    <tr>
      <td>R385</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>K387</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>C388</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>V392</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>E406</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>Q422</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>D423</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>V424</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>Q433</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>n.d.</td>
      <td>n.d.</td>
    </tr>
    <tr>
      <td>T434</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>n.d.</td>
      <td>n.d.</td>
    </tr>
    <tr>
      <td>F436</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td rowspan="6">Unresolved</td>
      <td>S445</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>P450</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Q455</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Q460</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>E465</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>n.d.</td>
      <td>n.d.</td>
    </tr>
    <tr>
      <td>S470</td>
      <td>+</td>
      <td>+</td>
      <td>(+)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>n.d.</td>
      <td>n.d.</td>
    </tr>
    <tr>
      <td rowspan="16">C-terminus</td>
      <td>E489</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>N490</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>V517</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>L523</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>L527</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>L536</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>E537</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>G538</td>
      <td>–</td>
      <td>+</td>
      <td>–</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>E539</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>A564</td>
      <td>+</td>
      <td>?</td>
      <td>+</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>↑</td>
      <td>↑</td>
    </tr>
    <tr>
      <td>L569</td>
      <td>+</td>
      <td>?</td>
      <td>(+)</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>I577</td>
      <td>+</td>
      <td>?</td>
      <td>–</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>(–)</td>
      <td>(–)</td>
    </tr>
    <tr>
      <td>Q585</td>
      <td>+</td>
      <td>?</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>G586</td>
      <td>+</td>
      <td>?</td>
      <td>+</td>
      <td>(–)</td>
      <td>(–)</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Y595</td>
      <td>+</td>
      <td>?</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>596</td>
      <td>+</td>
      <td>?</td>
      <td>+</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_+ and − indicate presence and absence of protein or signals, respectively. In case of current responses, + means response comparable to wt receptors and (+) means reduced responses. ↑ and ↓ indicate positive and negative fluorescence signals, respectively. 3–50 oocytes were measured per construct and filter set. In case of fluorescence responses, symbols in brackets indicate where less than three recordings met the criteria defined in the methods (mostly because of impaired fucntionality) and represent tendencies only. ?, not distinguishable (because of similar length of full-length and truncated constructs); n.d., not determined._

### Recording of ANAP fluorescence in the head domain reveals mainly gating-associated movements

Next, we recorded ANAP fluorescence changes upon application of 0.3 mM ATP. Control oocytes expressing wt P2X7R showed a gradual fluorescence decrease during ATP application, even when no ANAP was injected (Figure 3—figure supplement 1). A similar fluorescence drift was observed with the P2X2R, but not with the hɑ1 GlyR or the fast-desensitizing P2X1R. The reason for this drift is unclear but needs to be considered when evaluating mutants with small negative fluorescence changes. Specificity of tRNA loading and ANAP-incorporation was evaluated in further control experiments (Figure 3—figure supplement 2). Only recordings that met specific inclusion criteria (see Methods) were considered for analysis.

As a prodan derivative, ANAP is highly sensitive to the polarity of its environment and shows a redshift in emission with increasing polarity (Lee et al., 2009; Weber and Farris, 1979). Consequently, alterations in ANAP fluorescence can be attributed to (i) quenching by ligands, small molecules, or (aromatic) aa, (ii) spectral shift due to changes in the polarity of the environment, or (iii) a combination of these two effects, e.g., in case of ligand interaction.

To allow differentiation between presumably wavelength-independent (de-)quenching of ANAP fluorescence by other molecules or spectral shifts due to changes in the polarity, we simultaneously recorded fluorescence in distinct spectral segments, i.e., (i) 430–470 nm and 470–500 nm with filter set 1 and (ii) 430–490 nm and >500 nm with filter set 2 (Figure 3A). This also enabled us to identify mutants that only showed fluorescence changes at certain wavelengths and would have escaped detection, otherwise.

![Figure 3.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of the voltage clamp fluorometry (VCF)-recording system and summary of filter/dichroic mirror configurations used to detect distinct spectral parts of L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP)-fluorescence (sets 1 and 2) and ANAP in combination with tetramethyl-rhodamine-maleimide (TMRM) or R-GECO1.2 (set 3). The corresponding positions A, B, C, and D are shown in the schematic. A second LED (green) was used for additional excitation of TMRM or R-GECO1.2. (B) Close-up of the P2X7 head domain in surface representation indicating the ANAP-substituted amino acid residues P120-Q128 (red). The three subunits are colored in gray, wheat, and light blue. (C) Principle of VCF and representative VCF recordings in response to 0.3 mM ATP (upon second application). Change of fluorescence intensity of a site-specifically introduced environment-sensitive fluorophore can be induced by ligand binding and/or conformational changes. (D) Box plots summarizing results from the indicated ANAP-labeled P2X7Rs at two different emission wavelengths with ΔF/F% representing the maximum fluorescence signal during a 15-s ATP application. Numbers of recordings are given in brackets. (E) Representative VCF recordings in response to 0.3 mM ATP of P2X7(S124*) at three different emission wavelengths and summary of most likely interpretations. Note that fluorescence changes are most likely resulting from multiple effects, and only the dominant effect is stated. Arrows indicate direction of fluorescent changes. (F) Overlay of VCF recordings upon first (colored) and second (gray) ATP applications (0.3 mM) at two different emission wavelengths for P2X7(S124*) (14 oocytes) and P2X7(K127*) (17 oocytes), respectively. Averaged VCF recordings are shown as lines, and standard deviations are plotted as envelopes. Baseline currents (15 s before ATP application) were adjusted for clarity. All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV. Original recordings have also been deposited with Dryad and summarized and assigned in Table 1—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Representative VCF-recordings of oocytes injected with cRNA encoding the indicated receptors plus either water (negative control) or L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP)-Master Mix (ANAP-MM, containing ANAP, tRNA, cRNA ecoding tRNA-syntethase, and cRNA encoding eRF1(E55D)). The holding potential was –30 mV, if not otherwise indicated.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A,B) Representative voltage clamp fluorometry (VCF) recordings (A) and analysis of membrane expression (B) from oocytes that were injected with cRNA encoding non-mutated P2X7 or P2X7 containing an amber stop codon at the indicated positions together with (a) both, ANAP and a master mix containing tRNA-synthetase cRNA, tRNA, and eRF1(E55D) cRNA (positive control), (b) with the master mix only, (c) with ANAP only, or (d) with water as a negative control. ANAP emission was recorded at two different wavelengths (purple: 430–490 nm, green: >500 nm). VCF recordings showed clear ATP-evoked signals only for the oocytes injected with all essential components necessary for ANAP-incorporation and were in agreement with surface-expression analysis experiments. Although faint surface expression of full-length receptors was seen in the absence of ANAP (indicating limited read through), ATP-evoked fluorescence and current responses were negligible (no fluorescence change and current responses less than 10% of those from positive controls).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) Overlay of representative current traces upon first (black) and second (gray) ATP applications (0.3 mM in 195 s interval) for wt P2X7, and the indicated mutations that were expected to prevent facilitation. Baseline currents (15 s before ATP application) were adjusted for clarity. (B) Box plot summarizing 10–50% rise times of the first and second current responses to ATP for wt and ΔCys P2X7. Note that the low expression of the S23N and Cys-Ala mutants prevented further analysis. (C) Box plots summarizing 10–50% rise times of the first and second current (black) and fluorescence (colored) responses at the indicated emission wavelengths for F11*, S124*, K127*, and the tetramethyl-rhodamine-maleimide-labeled double mutant (F11*, S124C). Significance was determined using the two-tailed paired Student’s t-test (*, p<0.05; **, p<0.005; ***, p<0.0005; ****, p<0.00005; ns, not significant). (D) Normalized dose-response curves for ATP at wt P2X7 and the indicated L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid-containing receptors. Lines represent nonlinear curve fits of the Hill equation to the data. For EC50 values see Table 2. Error bars represent S.D. of 3–11 experiments. All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV. Original recordings have also been deposited with Dryad and summarized and assigned in Table 1—source data 1.

We first recorded ATP-induced fluorescence changes from P2X7Rs containing ANAP in the head domain, which projects over the ATP-binding site (P120-Q128, Figure 3B). In agreement with the pronounced conformational changes and ligand interactions of this domain during receptor activation (Lörinczi et al., 2012; McCarthy et al., 2019), all mutants except E121* and Q128* showed clear fluorescence signals in all spectral segments (Figure 3C and D, Table 1 and Figure 2—figure supplement 1B). For E121* and Q128* fluorescence changes were only detected with filter set 2, albeit with minimal changes for E121*. Analysis of mutants P120*, E121*, and P123* with filter set 1 was only preliminary (Figure 2—figure supplement 1B) but showed the same trends as signals recorded with filter set 2 (Figure 3C and D). Independently of the wavelength, fluorescence changes were always positive for P120* and G126* and negative for Y122*, P123*, and K127*. These consistent changes over the entire ANAP emission spectrum indicate de-/quenching of ANAP either by the ligand ATP and/or other aa residues (see insert table in Figure 3E). In contrast, S124* (Figure 3E), R125*, and Q128* (Figure 3C and D and Figure 2—figure supplement 1B) showed positive fluorescence changes in most spectral segments but negative changes for wavelengths >500 nm. The opposite directions imply that these changes result, at least partly, from an ANAP emission shift toward shorter wavelengths and suggest that ANAP enters a less polar environment during receptor activation (Figure 3E).

In all head-domain constructs that showed clear kinetics, with the exception of K127*, fluorescence and current changes started simultaneously and showed shorter rising times upon repeated ATP applications, thus recapitulating the characteristic ‘current facilitation’ of the P2X7R (Allsopp and Evans, 2015; Janks et al., 2019; Roger et al., 2008). To confirm that these fluorescence signals indeed tracked current facilitation, we analyzed the effects of three additional mutants that were expected to affect facilitation: (i) a single point mutation in the juxtamembrane region (S23N) that in human P2X7 was shown to eliminate current facilitation (Allsopp and Evans, 2015), (ii) a Cys-Ala mutant (replacement of residues identified to be palmitoylated [McCarthy et al., 2019] in the cysteine-rich region by alanine residues [Ser360, Cys362, Cys371, Cys373, Cys374, and Cys377]), and (iii) a ΔCys-mutant (deletion of the cysteine-rich intracellular region, S360-C377 [McCarthy et al., 2019; Roger et al., 2010]). Contrary to findings in human P2X7 (Allsopp and Evans, 2015), the S23N mutation did not eliminate current facilitation in rat P2X7 (Figure 3—figure supplement 3). As expected (Roger et al., 2010) and in contrast to the wt and most of the analyzed ANAP-containing mutants, current rise times of the ΔCys mutant were not significantly altered between first and second ATP applications, demonstrating that we can indeed identify current facilitation in our setup (Figure 3—figure supplement 3). However, the strongly reduced functional expression of the Cys-Ala or ΔCys mutant with additional ANAP-incorporation sites prevented reliable analysis of current and fluorescence kinetics.

Remarkably, the K127* mutant showed a fluorescence change that was faster than the current increase already upon the first receptor activation (Figure 3F, Figure 3—figure supplement 3). EC50 values for ATP were similar at wt, S124* and K127* mutants (Table 2). We conclude from this, that ANAP in position 127 reports a process that precedes channel opening and is most likely related to ligand binding, whereas ANAP reports gating-associated conformational changes in the other positions.

**Table 2.**
 EC50 values for ATP and Hill coefficients (nH) at wt and L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid-containing P2X7 receptor constructs.Table 2—source data 1.Original recordings for Table 2; Figure 3—figure supplement 3D; and Figure 5—figure supplement 2A.Table 2—source data 2.Summarized data for Table 2; Figure 3—figure supplement 3D; and Figure 5—figure supplement 2A.


<table>
  <thead>
    <tr>
      <th>Mutant</th>
      <th>EC50 (M)</th>
      <th>nH</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wt</td>
      <td>4.202e-005 (3.211e-005–5.704e-005)</td>
      <td>1.049 (0.7962–1.380)</td>
    </tr>
    <tr>
      <td>F11*</td>
      <td>7.802e-005 (6.268e-005–9.893e-005)</td>
      <td>1.148 (0.9345–1.410)</td>
    </tr>
    <tr>
      <td>S124*</td>
      <td>8.316e-005 (6.068e-005–0.0001236)</td>
      <td>1.122 (0.8271–1.519)</td>
    </tr>
    <tr>
      <td>F11*, S124C</td>
      <td>0.0001003 (8.439e-005–0.0001216)</td>
      <td>1.290 (1.069–1.571)</td>
    </tr>
    <tr>
      <td>K127*</td>
      <td>6.511e-005 (4.281e-005–0.0001339)</td>
      <td>0.6601 (0.4779–0.8662)</td>
    </tr>
    <tr>
      <td>D423*</td>
      <td>6.513e-005 (4.729e-005–0.0001057)</td>
      <td>1.240 (0.8087–1.821)</td>
    </tr>
    <tr>
      <td>A564*</td>
      <td>5.159e-005 (3.491e-005–9.976e-005)</td>
      <td>0.7810 (0.5364–1.087)</td>
    </tr>
  </tbody>
</table>

_Number in brackets are 95% confidence intervals, n=3–11._

### Detection of TM2 movements in response to receptor activation

The following VCF recordings were performed mainly with filter set 2 (430–490 nm and >500 nm), since this revealed more pronounced signals for most mutants.

To exclude fluorescence changes induced by a direct interaction with ATP and to further investigate P2X7 gating, we next investigated positions 339–341 (Figure 4A), just preceding S342, the major determinant of the channel gate (Pippel et al., 2017). Cysteine substitutions in these positions have previously been shown to be accessible to thiol-reactive dyes only in the open state of the receptor (Pippel et al., 2017). In agreement with a critical role in gating, current recordings from mutants S339*, T340*, and L341* were compromised by 10–20-fold higher leak currents compared to wt receptors or other mutants (see also Figure 4—figure supplement 1). Nevertheless, they showed clear fluorescence changes during receptor activation (Figure 4B), although with higher variability in amplitude and shape between oocytes. While P2X7R mutants S339* and L341* showed positive signals in all spectral ranges, fluorescence changes in T340* were inconsistent at shorter emission wavelengths, but mostly negative below 470 nm, and positive above 470 nm, indicating again that a spectral shift contributed to these signals (Figure 4B and C).

![Figure 4.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig4-v2.jpg)

**Figure 4.:** (A) Overview and close-up of the three P2X7 subunits (in wheat, gray, and purple) with the TM helices as cartoon representations (in wheat, gray, and green) and the ANAP-substituted residues S339, T340, and L341 (in red). (B) Representative voltage clamp fluorometry (VCF) recordings from the indicated mutants in response to 0.3 mM ATP (upon second application) and summary of results at two different emission wavelengths. Note that recordings from all constructs were compromised by high leak currents. Graphs compare maximal fluorescence signals during first (closed circles) and second (open circles) ATP applications (interval 195 s). Data are represented as mean ± S.E.M. Significance was determined using the two-tailed paired Student’s t-test (*, p<0.05; **, p<0.005). (C) Representative recordings and summary (performed as in B) from P2X7(T340*) with filter set 2. (D) Overlay of VCF recordings from P2X7(T340*) upon first (colored) and second (gray) ATP applications (0.3 mM) at two different emission wavelengths. Averaged VCF recordings from 11 oocytes are shown as lines, and standard deviations are plotted as envelopes. Baseline currents (15 s before ATP application) were adjusted for clarity. All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV. Wavelengths passed by the used filter sets are indicated. Original recordings have also been deposited with Dryad and summarized and assigned in Table 1—source data 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Representative current traces showing the effect of the P2X7 antagonist A438079 (100 µM) on baseline currents of mutants containing ANAP within TM2 (T340*, L341*) and on wt P2X7. A438079 was diluted from a 10 mM stock in Dimethyl sulfoxide (DMSO) using divalent-free buffer and applied into the static bath. Control experiments were conducted with 1% DMSO. Oocytes were clamped at –30 mV. (B) Box plot showing 10–50% rise times (in seconds) of the first and second current (black) and fluorescence (blue) responses to 0.3 mM ATP (interval 195 s) for P2X7(T340*). Significance was determined using the two-tailed paired Student’s t-test (*, p<0.05; ns, not significant). Original recordings have also been deposited with Dryad and summarized and assigned in Table 1—source data 1.

Notably, fluorescence signals from P2X7 T340* were also significantly larger during the first ATP application compared to the second (Figure 4B and C), suggesting that the environment of this position changed between both ATP applications. An intriguing explanation could be an involvement of this region in the facilitation process. However, as the T340* mutant displayed no change in fluorescence or current kinetics between ATP applications (Figure 4D and Figure 4—figure supplement 1) the facilitation-associated gating mechanism is likely disturbed by this mutation.

### Scanning of the P2X7 intracellular domains for ATP-induced conformational changes

The large intracellular P2X7 C-terminus mediates many of the P2X7R downstream effects (Kopp et al., 2019). While the P2X7 cryo-EM structures revealed the role of the juxtamembrane N- and C-terminal domains in receptor desensitization, their role in downstream signaling and in particular the molecular function of the ballast domain remain completely unclear. Analysis of ANAP fluorescence changes within the cytoplasmic domain was therefore a primary aim of this study. We first introduced ANAP into juxtamembrane regions within the N- and C-termini (Figure 5A) that form the cytoplasmic cap and anchor domains excluding palmitoylated residues (C4, S360, C362, C363, C374, and C377) (McCarthy et al., 2019). Although all receptors with N-terminal ANAP substitutions were formed in full length (Figure 2C), current and fluorescence responses for S6*, V10*, and K17* substitutions remained small and inconsistent even after 6 days of expression. A3*, C5*, W7*, and F11* mutants showed positive fluorescence signals of variable sizes (Figure 5B), and the kinetics of F11* fluorescence correlated with current facilitation (Figure 5C, Figure 3—figure supplement 3). ANAP fluorescence in F11* was not quenched by the nearby Trp (W7), as its removal had no apparent effect (Figure 5—figure supplement 1). Within the juxtamembrane C-terminal regions, ANAP was introduced between TM2 and the anchor domain (N356*, T357*, Y358*, A359*), upstream of β15, which is part of the cytoplasmic cap structure (T361*, R364*, C371*, A378*, R385*, K387*), and upstream of the cytosolic ballast domain (C388* and V392*). Surface expression of functional full-length receptors was observed for all constructs except for K387* and C388*. In contrast to the juxtamembrane N-terminal residues, however, only one of these C-terminal mutants, T361*, showed a fluorescence change, albeit in only ~50% of the recordings (Figure 5D). Interestingly, both F11 and T361 lie within two of at least four possible cholesterol recognition amino acid consensus (CRAC) motifs that have been proposed to be involved in the cholesterol sensitivity of P2X7 channel gating (Robinson et al., 2014).

![Figure 5.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig5-v2.jpg)

**Figure 5.:** (A) Surface representation of all three P2X7 subunits (in wheat, gray, and purple) showing location of the juxtamembrane regions and close up (top view) detailing the anchor and cap domains (in yellow and blue, respectively) and ANAP-substituted positions (in red) within a single P2X7 subunit. (B) Representative voltage clamp fluorometry (VCF) recordings and data summary from P2X7R mutants containing ANAP at different positions within the N-terminus. Responses to 0.3 mM ATP were recorded at two different emission wavelengths. Graphs compare maximal fluorescence signals during first (closed circles) and second (open circles) ATP applications (interval 195 s). Data are represented as mean ± S.E.M. (C) Overlay of VCF recordings from P2X7(F11*) upon first (colored) and second (gray) ATP application (0.3 mM) at two different emission wavelengths. Lines represent averaged VCF recordings from 13 oocytes. Standard deviations are plotted as envelopes. Baseline currents (15 s before ATP application) were adjusted for clarity. (D) Representative VCF recordings from the indicated mutants in response to a second application of 0.3 mM ATP and summary of results at the indicated emission wavelengths (performed as in B). Graphs compare maximal fluorescence signals during first (closed circles) and second (open circles) ATP applications (interval 195 s). Data are represented as mean ± S.E.M. All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV. (E) Close-up of the cytoplasmic ballast domain from one P2X7 subunit in cartoon and surface representation highlighting a bound GDP (salmon), surrounding α-helices, and residue A564 (red). (F) Surface representation of the cytoplasmic domains of all three P2X7 subunits (in gray, light blue, and wheat) with bound GDP (salmon). Positions in which ATP-induced ANAP fluorescence changes were identified are shown in red. ANAP-substituted positions in which no fluorescence changes were seen (despite surface expression and current responses) are shown in blue. Original recordings have also been deposited with Dryad and summarized and assigned in Table 1—source data 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A, B) Comparison of voltage clamp fluorometry recordings from oocytes expressing P2X7(F11*) with or without Trp in position 7 (W7A, F11*). Oocytes expressing either non-mutated P2X7R or P2X7(W7A) served as controls. Recordings from P2X7(F11*) and P2X7 (W7A, F11*) are not significantly different, indicating that L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid in position 11 is not quenched by Trp7. Data are represented as mean ± S.E.M. (C) Surface expression of P2X7(F11*), P2X7(F11*, W7A), and P2X7(W7A), with unmutated P2X7 and uninjected oocytes as positive and negative controls, respectively.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Normalized dose-response curves for ATP at wt P2X7 and the indicated L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP)-containing receptors. For EC50 values see Table 2. Error bars represent S.D. of three to eight experiments. (B) Representative voltage clamp fluorometry (VCF) recordings from oocytes that were injected with cRNA encoding P2X7 containing an amber stop codon at D423 or A564 with either ANAP and a master mix containing tRNA-synthetase cRNA, tRNA, and eRF1(E55D) cRNA, or with water to produce P2X7 protein truncated at these positions. ANAP emission was recorded at two different wavelengths (purple: 430–490 nm, green: >500 nm). VCF recordings showed clear ATP-evoked signals only for the oocytes injected with all essential components necessary for ANAP incorporation. Current responses of truncated P2X7Rs were less than 5% of those from positive controls. All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) ΔCaM-P2X7 contained the single point mutations I541T, S552C, and V559G (Roger et al., 2010). Overlay of representative current traces during first (dark gray) and second (light gray) ATP applications (0.3 mM, applied in 195 s interval). Baseline currents (15 s before ATP application) were adjusted for clarity. (B) Box plot showing 10–50% rise times (in seconds) of the first and second current responses for wt P2X7 and ΔCaM P2X7. Significance was determined using the two-tailed paired Student’s t-test (**, p<0.005; ns, not significant). All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV. (B) Representative voltage clamp fluorometry (VCF) recordings in response to the second ATP application of the indicated mutants ΔCaM F11*, n=2 (3); ΔCaM, S124*, n=1 (3); ΔCaM, K127*, n=3 (8); ΔCaM, D423*, n=4 (9); ΔCaM, A564*, n=3 (15) with n and numbers in brackets indicating the number of successful and total VCF recordings, respectively. All recordings were performed in divalent-free buffer, and oocytes were clamped at –30 mV.

ANAP introduction in most of the 29 ballast domain positions led to a dominant formation of truncated protein, indicating that this domain does not tolerate substitutions very well and/or that the truncated constructs form stable proteins. Four of these mutants (Q422*, V424*, G538*, I577*) did not form functional receptors at all. For most of the remaining constructs, no specific fluorescence changes could be detected, despite promising surface transport and current responses comparable to wt receptors for at least 12 of them (see Table 1, Figure 2C).

Only in two mutants, A564* and D423*, fluorescence changes could be recorded: A564* showed clearly positive signals, while D423* showed positive signals in only ~40% of the recordings (Figure 5D). Both mutants showed EC50 values similar to wt P2X7 and were not functional in control oocytes injected without ANAP (Figure 5—figure supplement 2), suggesting that the respective truncated proteins (compare Figure 2C) do either not contribute to current responses or only in complex with full-length (ANAP-containing) P2X7 subunits. D423 is located within a loop connecting the β17 and β18 strands and situated on the outer surface of the cytoplasmic ballast, facing away from both the central axis of the receptor and the neighboring subunits (Figure 5F). Notably, mutation of the neighboring positions (Q422*, V424*) resulted in non-functional receptors. A564 is located in the α15 helix at the very end of a cavity formed by the α13, α14, and α16 helices and a short α9 helix of the neighboring subunit (Figure 5E). This cavity harbors the guanosine nucleotide binding site identified by cryo-EM and liquid chromatography-tandem mass spectrometry analysis, and GDP was found to interact with residues A567 and L569 (McCarthy et al., 2019), both in close proximity to A564. α16, is also part of a proposed lipid interaction or lipopolysaccharide (LPS) binding motif (Denlinger et al., 2001) and α14 at the bottom of the cavity is part of a proposed calcium-dependent calmodulin binding motif (residues I541-S560) (Roger et al., 2010; Roger et al., 2008). To identify possible palmitoylation or CaM-dependent movements of the ballast domain or effects on receptor function, we analyzed the influence of the non-palmitoylated ΔCys- and Cys-Ala mutants (Figure 3—figure supplement 3) as well as a ΔCaM mutant, in which a proposed calmodulin binding site was deleted (Roger et al., 2010) on ANAP fluorescence. While the poor expression of the ΔCys and Cys-Ala mutants in combination with ANAP prevented VCF analysis, combination of the ΔCaM mutation with ANAP (in intracellular positions F11*, D423*, or A564* or in the head domain S124*, K127*) yielded good expression and similar current kinetics and fluorescence changes, as observed before for the single mutants (Figure 5—figure supplement 3). This argues against a major functional effect of the CaM binding site mutation on the current facilitation or on molecular movements, at least in the oocyte-expressed receptor.

Taken together, only two positions, D423 and A564, could be identified within the ballast domain, where ANAP reported environmental changes, suggesting only limited ATP-induced movements in this domain. However, mutant A564* has great potential as a reporter for yet undefined processes that affect GDP binding and/or metabolism.

### Parallel recording of ANAP fluorescence with other fluorophores

Based on the above findings, we propose that yet unknown intracellular ligands or protein interactors are required to mediate downstream signaling via the ballast domain. As potential tools to further investigate such molecules and the dynamics of their molecular interplay with the P2X7R, we combined ANAP with other fluorophores and equipped the VCF setup with a second LED for parallel excitation of two different fluorophores within the same protein.

First, we generated a double mutant (F11*/ S124C) suited to investigate the dynamics of P2X7 activation in different parts of the receptor by parallel labeling with the thiol-reactive fluorophore TMRM in the extracellular head domain and with ANAP in the cytoplasmic N-terminus. As seen in Figure 6A, and similar to ANAP in K127*, TMRM in the head-domain showed an instant fluorescent change already upon a first ATP application, whereas the ANAP fluorescence change in F11* was clearly slower. However, both signals coincided upon a second ATP application, further supporting our hypothesis that the so-called current facilitation in P2X7 is due to a change in receptor gating rather than ligand binding. EC50 values for ATP at these mutants and at wt P2X7 were comparable (Figure 3—figure supplement 3 and Table 2).

![Figure 6.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig6-v2.jpg)

**Figure 6.:** (A) Scheme of a P2X7 subunit double-labeled with L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid (ANAP) and tetramethyl-rhodamine-maleimide (TMRM) (F11*, S124C) and overlay of fluorescence and current responses to first (colored) and second (gray) ATP applications (0.3 mM) at the indicated emission wavelengths. Lines represent averaged voltage clamp fluorometry (VCF) recordings from five different oocytes and standard deviations are plotted as envelopes. Baseline currents (15 s before ATP application) were adjusted for clarity. (B) Scheme of P2X7(K127*) subunit C-terminally fused to R-GECO1.2 and representative VCF recording in response to 0.3 mM ATP. Recordings were performed in buffer containing 0.5 mM Ca2+. (C) Scheme showing the P2X7(Y595*)-CaM-M13-mNeonGreen construct that served as positive control for recordings of FRET between ANAP and mNeonGreen. Ca2+ entry through the P2X7R is supposed to induce conformational changes in the CaM-M13-mNeonGreen reporter, which are detected as a FRET signal. A representative VCF recording in response to 0.3 mM ATP is shown. In all recordings, oocytes were clamped at –30 mV.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) In Ca2+-containing buffers, voltage clamp fluorometry (VCF) recordings from unmutated wt P2X7R (left) showed large irregular fluorescence changes in the ANAP emission range, even in the absence of ANAP. These masked ATP-evoked and ANAP-specific fluorescence signals from ANAP-substituted P2X7(T340*) (right). (B) The irregular fluorescence changes in Ca2+-containing buffers could be prevented by injection of EGTA (1 mM) 3–4 hr before the measurement. (C) VCF recordings of oocytes expressing P2X7(F11*) in divalent-free buffer supplemented with EGTA and flufenamic acid (left) and in buffer containing 0.5 mM Ca2+ (center and right). (D) VCF recordings of oocytes expressing P2X7(S124*) and P2X7(S124*)-R-GECO1.2. The Ca2+-dependent fluorescence changes are only detected in the ANAP emission spectrum. If not otherwise indicated, recordings were performed at –30 mV in divalent-free buffer supplemented with EGTA and flufenamic acid. (E) ANAP (1 μM) and the indicated CaCl2 concentrations were dissolved in otherwise divalent-free recording solution. Fluorescence emission spectra were measured using a Tecan Reader Infinite M200 Pro (excitation 360 nm) and normalized to the averaged fluorescence emission at the maximum emission (492 nm, dotted line) of buffer containing only ANAP. Note that values for the (1 M Ca2+ + ANAP)–solution were out of measurement range.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Scheme representing the constructs tested (left) with fluorescence signals at two different emission wavelengths (for L-3-(6-acetylnaphthalen-2-ylamino)–2-aminopropanoic acid [ANAP; blue] and mNeonGreen [green], respectively) summarized as horizontal bar diagrams (right). The positive control P2X7(Y595*)-CaM-M13-mNeonGreen is the only construct showing negative fluorescence signals for ANAP and positive signals for mNeonGreen, consistent with FRET. The control constructs containing only ANAP show either negative or no fluorescence signal for mNeonGreen. Constructs without sites for ANAP incorporation but co-injected ANAP (as master mix with tRNA and cRNAs) served as a control for background fluorescence. Error bars represent S.E.M. Numbers of experiments are given in brackets.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/82479/elife-82479-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** The indicated ANAP-containing P2X7 constructs were co-injected with soluble mNeonGreen-tagged CaM and ANAP-Master Mix containing ANAP, tRNA, cRNA encoding tRNA-syntethase, and cRNA encoding eRF1(E55D). Corresponding fluorescence signals at two different emission wavelengths are summarized for ANAP (blue) and mNeonGreen (green). Note that soluble mNeonGreen-tagged CaM appeared to interact with the co-injected ANAP. Error bars represent S.E.M. Numbers of experiments are given in brackets.

Since P2X7 is known to permeate Ca2+, an important mediator of intracellular signaling, we also established a protocol to combine VCF recording of ANAP-fluorescence with imaging of P2X7-mediated Ca2+ influx by fusing the genetically encoded Ca2+-sensor R-GECO1.2 (Wu et al., 2013) C-terminally to the receptor. Combination of P2X7 R-GECO1.2 with the K127* mutant, in which ANAP most likely reports a ligand binding-associated process, showed a clearly delayed onset of the Ca2+-dependent R-GECO fluorescence signal, as expected (Figure 6B). A limitation of this protocol was, however, that Ca2+ promoted P2X7 desensitization and affected baseline fluorescence, specifically in the ANAP emission spectrum (Figure 6—figure supplement 1). Use of an alternative fluorescent unnatural amino acid (fUAA) would therefore be advantageous.

ANAP has been successfully used as a FRET partner in combination with acceptor transition metals (Gordon et al., 2018), with EGFP (Mitchell et al., 2017), and with YFP to study the apoptosis-regulating Bax-Hsp70 interaction in HeLa cells (Park et al., 2019) and the interaction between BACE1 and KCNQ2/3 in tsA-201 cells (Dai, 2022). Thus, we finally tested whether we could detect FRET signals between ANAP and potential interactors carrying a mNeonGreen-tag. As a proof of concept and based on a CaM-M13-EGFP fusion protein (Mitchell et al., 2017), we generated a positive control (P2X7(Y595*)CaM-M13-mNeonGreen), in which ANAP was introduced into the very C-terminus of a P2X7R that was C-terminally fused to a construct consisting of calmodulin (CaM), CaM-binding myosin light chain kinase (M13), and mNeonGreen (Shaner et al., 2013). Upon Ca2+-binding, this construct should move the acceptor protein mNeonGreen in closer proximity to ANAP, which acts as FRET donor.

As expected, ATP-induced Ca2+-influx reduced ANAP fluorescence and increased mNeonGreen fluorescence (Figure 6C). The specificity of the signals was confirmed in control experiments (Figure 6—figure supplement 2).

Driven by these results we sought to investigate a potential interaction between the rat P2X7 receptor and CaM (Roger et al., 2010; Roger et al., 2008) and performed experiments with ANAP-labeled P2X7 receptors and mNeonGreen-tagged CaM. However, these recordings revealed no differences to the negative controls, as the CaM-mNeonGreen construct yielded unspecific fluorescence signals (Figure 6—figure supplement 3), possibly due to interaction of soluble mNeonGreen-tagged CaM with the co-injected ANAP.

Since the small FRET signals additionally complicated these analyses, the use of another fUAA with superior photophysical properties such as Acd (Zagotta et al., 2021) might provide a better alternative.

In summary, we identified kinetically different fluorescence changes in the head domain that are most likely associated with ligand binding and gating, respectively, and suggest an involvement of the region around T340 in P2X7 current facilitation. We find, however, only limited ATP-induced movements in the intracellular domains and hypothesize that additional interactions might be required to ‘activate’ the ballast domain. Protocols for parallel recordings of ANAP with TMRM, mNeonGreen, and R-Geco1.2 were established to further analyze such interactions.

## Discussion

### Optimization of UAA incorporation into P2X7

Site-specific UAA-incorporation represents a powerful method for protein structure-function analysis, and protocols exist for several model systems (Braun et al., 2020; Klippenstein et al., 2018; Leisle et al., 2015; Pless et al., 2015). In X. laevis oocytes, stop codon suppression either by in vitro synthesized UAA-aminoacylated tRNAs or by expression of co-evolved tRNA/aminoacyl-tRNA synthetase pairs has been established. Recently, the semisynthetic ligation of peptide fragments containing the modification using split intervening proteins (inteins) (Sarkar et al., 2021) has also been described (Galleano et al., 2021; Khoo et al., 2020). While chemically aminoacylated tRNA cannot be reloaded after deacylation without a tRNA synthetase (Klippenstein et al., 2018), expression of co-evolved orthogonal tRNA/aminoacyl-tRNA synthetase pairs requires an additional nuclear injection (Kalstrup and Blunck, 2013; Ye et al., 2013). Here, we combined both methods by simultaneously injecting a synthesized suppressor tRNA, cRNA encoding the tRNA synthetase, ANAP, and cRNA encoding the target protein into the cytoplasm. We further enhanced ANAP incorporation by co-injection of cRNA encoding mutated X. laevis eRF1, disfavoring premature translation termination. While mutated eRF1 could potentially interfere with correct translation of endogenous amber-terminated oocyte proteins, we observed no apparent impact on oocyte properties. The presented procedure also improved oocyte quality, expression efficiency, and reproducibility and facilitated optimization of injection ratios. While it does not require equipment for synthesis and purification of UAA-labeled tRNA and is easily applicable in a molecular biology lab, it still depends on a co-evolved tRNA/aminoacyl-tRNA synthetase pair. In combination with UAAs suitable for click chemistry, its flexibility and the choice of fluorophores or functional groups could be greatly expanded (Braun et al., 2020). Here, we could successfully employ the optimized ANAP labeling strategy to explore conformational changes associated with P2X7R activation.

### Is P2X7 current facilitation an intrinsic receptor property?

Based on crystal and cryo-EM structures, a molecular mechanism of P2XR gating has been established: ATP-binding to its extracellular inter-subunit binding sites leads to a jaw-like tightening of the head and dorsal fin domains of neighboring subunits around the ATP molecule. This induces an upward movement of β strands in the lower part of the extracellular domain and associated pore opening. Upon prolonged and/or repeated activation, the P2X7R shows a characteristic increase in current amplitude and speed of channel opening, which is generally associated with a shift toward higher ATP sensitivity. Several mechanisms have been proposed to contribute to this so-called current facilitation: modulation of receptor activity by cholesterol (via direct binding to TM domains or cholesterol recognition amino acid consensus [CRAC] motifs) (Karasawa et al., 2017; Murrell-Lagnado, 2017; Robinson et al., 2014), palmitoylation (Di Virgilio et al., 2018; Gonnord et al., 2009; Karasawa et al., 2017), cooperative interactions between intracellular N- and C-termini (Allsopp and Evans, 2015), and calcium-dependent calmodulin binding (Roger et al., 2008). The latter, however, appeared to be specific for rat P2X7 and was not found in the human isoform (Roger et al., 2010). In monocyte-derived human macrophages, current facilitation as well as inflammasome activation, IL-1β release, blebbing, PS flip, and membrane permeabilization were inhibited by phospholipase A2 (PLA2) and Cl- channel antagonists (Janks et al., 2019), and it was suggested that facilitation represents a downstream effect of P2X7-mediated PLA2 and Cl- channel activation. Single channel recordings of HEK293 cell-expressed rat P2X7Rs recently revealed an increased open probability as a result of ATP-evoked current facilitation (Dunning et al., 2021). Here, we also observed a faster onset of current signal upon the second ATP application while changes in the amplitude were less obvious. Importantly, for most ANAP-containing P2X7R constructs studied here, fluorescence changes mirrored this behavior, strongly suggesting that it is a receptor-intrinsic property and does not involve currents from downstream-activated channels, such as Ca2+-activated Cl- channels or pannexins (Dunning et al., 2021; Ousingsawat et al., 2015; Pelegrin and Surprenant, 2006; Riedel et al., 2007). Interestingly, the K127* head domain mutant showed faster fluorescence than current changes even upon the first ATP application. Thus, ANAP in this position reports a movement or interaction that precedes channel opening and is most likely related to ligand binding. A similar result was observed for the TMRM-labeled F11*/S124C double mutant, where the onset of TMRM signal upon the first ATP application was faster than the current and ANAP fluorescence change (but coincided upon the second application). In contrast to TMRM, ANAP in position 124 showed fluorescence signals that paralleled current responses, suggesting that different fluorophores can report different processes, possibly due to differences in size and/or sensitivity to the environment. Supporting the idea that these fast fluorescence changes are related to ligand binding, they were only observed in mutants containing fluorophores near the ATP binding site. Fast ligand-induced fluorescence changes already in the non-facilitated P2X7 state imply that ligand binding is unaltered between the first and second activation and consequently, changes in channel gating account for the observed current facilitation.

Fluorescence signals recorded from ANAP in positions near the channel gate (Pippel et al., 2017) could result from different simultaneously occurring effects during channel opening and evidence for both, a shift in ANAP emission toward longer wavelengths (position 340) and dequenching (positions 339 and 341) were observed. Interestingly, ANAP in position 340 revealed significant differences in the fluorescence amplitudes between the first and second ATP application. An intriguing explanation would be that it detects a slowly or non-reversible conformational change after the first ATP application, which could facilitate subsequent gating movements and thereby account for current facilitation. However, T340* was the only construct that did not show a faster current onset upon the second ATP application, possibly because ANAP substitution in this critical position already strongly facilitated gating, as indicated by the large ‘leak’ currents, likely reflecting partial constitutive ligand-independent opening.

Based on the above observations, we propose that the faster activation upon the second ATP application is an intrinsic property of the P2X7R. This conclusion is also in good agreement with the fact that the current facilitation but not downstream signaling events is seen in truncated P2X7 constructs (Kopp et al., 2019; McCarthy et al., 2019). One possibility for a molecular mechanism would be a pre-tensioning of TM2-helices during the first receptor activation that eases channel opening upon a second activation. It is not known, but likely that the cryo-EM structure of the ATP-bound open P2X7R represents the facilitated state. If so, the open-state stabilizing cap domain might not be locked in place in the naïve state but could be formed during the first receptor activation and then stabilized via the cysteine-rich anchor domain. The cap domain may then support the upward transition of TM2 and thereby accelerate current responses. Dynamic cysteine palmitoylation and cholesterol interactions might modulate this process as suggested before (Di Virgilio et al., 2018; Dunning et al., 2021; Karasawa et al., 2017; Robinson et al., 2014). Alternatively, initial receptor activation may change accessibility and/or affinity for a yet unknown allosteric ligand and thereby modulate P2X7 activation. All these suggested mechanisms are not mutually exclusive.

### Is the ballast domain affected by ATP-binding/channel opening?

While the functionality of P2X7 as a cation channel is not impaired by lack of the intracellular C-terminus (Becker et al., 2008; Klapperstück et al., 2001; McCarthy et al., 2019), its deletion disrupts a number of P2X7-mediated effects (Kopp et al., 2019), which most likely depend on downstream signaling pathways. A major aim of this study was the identification of C-terminal domains involved in such signaling. Most of the intracellular positions in which ANAP reported relative protein rearrangements were, however, located upstream of the cap domain either within the N-terminus (A3, C5, W7, F11) or right after TM2 (T361). Despite clear surface expression and current responses of at least 12 constructs with ANAP in the cytoplasmic ballast domain, only two of these mutants (D423* and A564*) revealed detectable but small fluorescence changes upon ligand application, suggesting that ATP binding induces only limited structural rearrangement in this domain, and that it is largely uncoupled from the extracellularly initiated conformational changes. Interestingly D423*, which showed only sporadic changes, lies in a short sequence with homology to an α-actinin 2 binding sequence (Kim et al., 2001). Since P2X7 activation induces plasma membrane morphology changes, and interactions with cytoskeletal proteins have been proposed (Gu et al., 2009; Kim et al., 2001; Kopp et al., 2019), an intriguing possibility would be that ANAP in position 423 reports interactions with cytoskeletal components. In A564*, ANAP is located near the GTP/GDP-binding site but showed much smaller signals than in positions near the ATP binding site, arguing against GTP/GDP (un-)binding, in agreement with the cryo-EM structures (McCarthy et al., 2019). However, A564 is also surrounded by other proposed interaction sites, including an LPS binding sequence and a calcium-dependent CaM binding motif (Denlinger et al., 2001; Roger et al., 2010; Roger et al., 2008), which might account for the observed signals.

In summary, we improved ANAP incorporation into Xenopus oocyte-expressed protein and performed an extensive VCF analysis of P2X7R mutants carrying ANAP in 61 positions throughout the receptor. We conclude from our data, that current facilitation is, at least partly, an intrinsic property of the P2X7R and involves an accelerated channel gating rather than ligand binding. In addition, we propose that ligand-induced extracellular and TM domain movements are not significantly translated to the cytosolic ballast domain and that intracellular ligands or interactors are required to ‘activate’ this domain. Protocols for simultaneous recording of ANAP with TMRM, Ca2+-dependent R-GECO1.2, or mNeonGreen-labeled FRET partners are presented that might help to validate P2X7 downstream signaling events and analyze their molecular mechanisms and dynamics, once such interactors have been reliably determined.

## Materials and methods

### Xenopus laevis oocytes

X. laevis females were obtained from NASCO (Fort Atkinson, WI) and kept at the Core Facility Animal Models (CAM) of the Biomedical Center (BMC) of LMU Munich, Germany (Az:4.3.2–5682/LMU/BMC/CAM) in accordance with the EU Animal Welfare Act. To obtain oocytes, frogs were deeply anesthetized in MS222 and killed by decapitation. Surgically extracted ovary lobes were divided into smaller lobes and dissociated by ~2.5 hr incubation (16°C) with gentle shaking in ND96 solution (96 mM NaCl, 2 mM KCl, 1 mM CaCl2, 1 mM MgCl2, 5 mM HEPES, pH 7.4) containing 2 mg/ml collagenase (Nordmark, Uetersen, Germany) and subsequently defolliculated by washing (15 min) with Ca2+-free oocyte Ringer solution (90 mM NaCl, 1 mM KCl, 2 mM MgCl2, 5 mM HEPES). Stage V-VI oocytes were selected and kept in ND96 containing 5 µg/ml gentamicin until further use. In some cases, oocytes were commercially obtained (Ecocyte Bioscience, Dortmund, Germany), or ovaries were provided by Prof. Dr. Luis Pardo (Max Planck Institute for Experimental Medicine, Göttingen, Germany).

### cDNA and cloning

N-terminally His-tagged rat P2X1 cDNA in pNKS2 has been described (Lörinczi et al., 2012). An EGFP-tag was C-terminally added via a GSAGSA-linker sequence by Gibson assembly (Gibson et al., 2009) according to the protocol of the manufacturer (New England Biolabs GmbH, Frankfurt am Main, Germany).

cDNA encoding an N-terminally His-tagged rat P2X7R was subcloned into a pUC19 vector modified for cRNA expression in oocytes (termed pUC19o). pUC19o was generated by insertion (from 5` to 3`) of a synthesized T7 promoter sequence, a Xenopus globin 5’-UTR, and a Kozak sequence (Kozak, 1987) (GeneArt String DNA fragment, Life Technologies / Thermo Fisher Scientific Inc, Regensburg, Germany) and a 27 bp 3’-UTR (Tanguay and Gallie, 1996) followed by a poly A tail (51 adenines) obtained from the pNKS2 vector (Gloor et al., 1995) (for details of the UTRs see Key resource table).

The cDNA sequence of the aminoacyl-tRNA synthetase was obtained from the plasmid pANAP (Addgene #48696) (Chatterjee et al., 2013) and subcloned via Gibson assembly into pUC19o.

The coding sequence of X. laevis eRF1 (NCBI Reference Sequence: NM_001090894.1) with an E55D mutation (GeneArt String DNA fragment, Life Technologies/Thermo Fisher Scientific Inc, Regensburg, Germany) was cloned into pNKS2 via Gibson assembly. For recombinant expression in E. coli, the coding sequence of His-eRF1(E55D) was cloned into a modified pET28a vector via Gibson assembly.

Site-specific mutagenesis was performed with the Q5 Site-Directed Mutagenesis Kit (based on PCR-amplification) according to the manufacturer’s protocol (New England Biolabs GmbH, Frankfurt am Main, Germany). Oligonucleotides were ordered from metabion GmbH (Planegg/Steinkirchen, Germany).

All constructs contained either an ochre (TAA) or opal (TGA) stop codon for normal translational termination to avoid C-terminal ANAP incorporation and read-through and were confirmed by sequencing (Eurofins Genomics, Ebersberg, Germany).

### eRF1 protein preparation

NiCo(DE3) bacteria were transformed with His-eRF1(E55D) in pET28a. 5 ml of a LB-Kanamicin pre-culture (~12 hr) was added to 300 ml ZY-5052 autoinduction media (Studier, 2005) supplemented with 100 µg/ml Kanamycin and grown for 6 hr at 37°C. The temperature was then reduced to 25°C, and bacteria were grown for another 18 hr. After pelleting by centrifugation (6500 g, 20 min) cells were resuspended in 40 ml lysis buffer (50 mM TRIS (tris(hydroxymethyl)aminomethane)-HCl, pH 8.0, 50 mM NaCl, 5 mM MgCl2, 10% (v/v) glycerol, 0.1% (v/v) Triton X-100, 10 µg/ml DNase I, 100 µg/ml lysozyme), and sonicated (Bandelin Sono plus, TT13 cap, 50% duty cycle, 50% power) for 5 min in an ice bath. The lysate was pelleted at 40,000 × g (1 hr at 4°C). The supernatant was filtered (0.2 µm) and applied onto a Ni-NTA column (HisTrap FF, 5 ml, GE Healthcare Europe GmbH, Freiburg, Germany). Bound protein was washed with 10 column volumes of washing buffer (25 mM TRIS-HCl, pH 7.8, 500 mM NaCl, 20 mM imidazole, 0.25% [v/v] Tween 20, 10% [v/v] glycerol) and eluted with 6 column volumes of elution buffer (25 mM TRIS-HCl, pH 7.8, 500 mM NaCl, 300 mM imidazole, 0.25% [v/v] Tween 20 [v/v], 10% [v/v] glycerol). The eluate was concentrated (Amicon Ultra-15, 10 kDa MWCO, Millipore/Merck KgaA, Darmstadt, Germany), and buffer was exchanged by low-salt buffer (20 mM TRIS, 100 mM NaCl, pH 7.5) for subsequent anion exchange chromatography on a 5 ml Mono-Q column (GE Healthcare Europe GmbH, Freiburg, Germany). Following an elution gradient with high-salt buffer (20 mM TRIS, 1 M NaCl, pH 7.5), protein-containing fractions were pooled, concentrated, and buffer was exchanged (1× PBS with 500 mM NaCl) for size exclusion chromatography on a Superdex 75 Increase (10/300). Purified His-eRF1(E55D) was shock-frozen in 10 µl aliquots and stored at –80°C.

### cRNA synthesis and tRNA

To prepare templates for cRNA synthesis, plasmids were linearized with EcoRI-HF (pNKS2) or NotI-HF (pUC19o) from New England Biolabs GmbH (Frankfurt am Main, Germany) and purified via MinElute Reaction Cleanup columns (Qiagen, Hilden, Germany) according to the manufacturer’s protocol. Alternatively, templates (including the 5’-terminal RNA polymerase promoter site (T7 or SP6) and the 3’-terminal poly A) were amplified by PCR and purified using the NucleoSpin Gel and PCR Clean-up Kit (Macherey-Nagel, Düren, Germany) according to the manufacturer’s protocol.

Capped cRNA was synthesized using the mMESSAGE mMACHINE SP6 or T7 Transcription Kits (Invitrogen/Thermo Fisher Scientific Inc, Schwerte, Germany), precipitated with LiCl, and dissolved in nuclease-free water (1 µg/µl if not stated otherwise).

The amber suppressor tRNA sequence was translated from the plasmid pANAP (Addgene #48696) (Chatterjee et al., 2013), provided with an universal 3’-terminal CCA-sequence (important for tRNA aminoacylation and translation), and chemically synthesized and purified via PAGE and HPLC (biomers.net GmbH, Ulm, Germany).

### Oocyte injection and ANAP incorporation

A Nanoject II injector (Science Products GmbH/Drummond, Hofheim, Germany) was used for nuclear and cytoplasmic injections.

cRNAs encoding cysteine-substituted receptors for TMRM labeling were injected as described (Lörinczi et al., 2012). Two different procedures were used for incorporation of ANAP:

The 2-step injection method was performed according to Kalstrup and Blunck, 2017 using the plasmid pANAP that encodes the co-evolved, orthogonal, and ANAP-specific amber suppressor tRNA/tRNA synthetase pair (Addgene #48696 Chatterjee et al., 2013). 9.2 nl of pANAP (0.1 μg/μl) per oocyte were injected into the nucleus. 1–2 days later, 46 nl of an injection mix containing 0.20–0.25 μg/μl receptor-encoding cRNA (with or without an UAG codon at the site of interest) and 0.2–1.0 mM ANAP (L-ANAP trifluoroacetic salt or L-ANAP methyl ester, both AsisChem Inc, Waltham, MA) were injected into the cytoplasm.

The 1-step injection method was performed as described before (Durner and Nicke, 2022) with addition of mutated X. laevis eRF1 as indicated. An injection master mix comprising 0.25 mM ANAP TFA, 0.25 μg/μl cRNA encoding X. laevis eRF1 E55D, 0.2 μg/μl cRNA encoding the tRNA synthetase, and 0.4 μg/μl tRNA was freshly prepared. Three parts of the injection master mix were added to one part of 1 μg/μl receptor-encoding cRNA (with or without an UAG codon). 50.6 nl per oocyte were injected into the cytoplasm. Uninjected oocytes and oocytes injected with wt receptor cRNA served as negative and positive controls, respectively. Nuclease free water served as a substitute for individual components in control groups.

To optimize fUAA incorporation into X. laevis oocyte-expressed receptors, different procedures, concentrations of substances, and injection time points were compared (Figure 1—figure supplement 1). To optimize the concentrations of an individual component, the ratios and concentrations of the other components, as well as the expression times and receptor cRNA concentrations were kept constant in individual experiments. In cases where oocytes were incubated in membrane-permeable L-ANAP methyl ester, a 2 μM concentration in ND96 buffer (see below) was used.

Injected oocytes were kept in ND96 (96 mM NaCl, 2 mM KCl, 1 mM MgCl2, 1 mM CaCl2, 5 mM HEPES, pH 7.4–7.5) supplemented with gentamicin (50 µg/ml) at 16°C for at least 2 days.

### Receptor purification and SDS-PAGE

To evaluate plasma membrane expression of truncated and full-length His-tagged P2X7R mutants, surface-expressed receptors were fluorescently labeled, purified, and analyzed by SDS-PAGE. Three days after injection, 10 oocytes per group were labeled for 30–60 min (in the dark under rotation) in 200 μl 0.003% (m/V) aminoreactive, membrane-impermeant Cy5 Mono NHS Ester (Merck / Sigma-Aldrich, Taufkirchen, Germany, diluted from a 1% [m/V] stock in DMSO) in ND96 (pH 8.5, 4°C) and then washed in ND96. Bright blue-stained damaged oocytes were then discarded, and intact oocytes were homogenized with a 200 μl pipet tip in 10 µl homogenization buffer per oocyte (0.1 M sodium phosphate buffer, pH 8.0, containing 0.4 mM Pefabloc SC and 0.5% n-dodecyl-β-D-maltoside, [both Merck/Sigma-Aldrich, Taufkirchen, Germany]). Membrane proteins were extracted by 10 min incubation on ice and separated from the debris by two centrifugation steps (10 min at 14,000 × g and 4°C). 100 µl of the protein extract were then supplemented with 400 µl of homogenization buffer containing 10 mM imidazole and added to 50 µl Ni2+-NTA agarose beads (Qiagen GmbH, Hilden, Germany) preconditioned with washing buffer (0.1 M sodium phosphate buffer [pH 8.0] containing 0.08 mM Pefabloc, 0.1% n-dodecyl-β-D-maltoside, and 25 mM imidazole). After 1 hr incubation under inversion at 4°C in the dark, beads were washed three to four times with 500 µl washing buffer, and His-tagged protein was eluted (≥10 min at RT with occasional flipping to suspend the beads) with 2×50 µl elution buffer (20 mM Tris-HCl, 300 mM imidazole, 10 mM EDTA, and 0.5% n-dodecyl-β-D-maltoside). 32 µl of the eluate were supplemented with 8 µl 5× lithium dodecyl sulfate (LiDS) sample buffer (5% [w/v] LiDS, 0.1% bromphenol blue, 100 mM dithiothreitol, 40% [v/v] glycerol in 0.3 M Tris HCl [pH 6.8]), incubated at 95°C for 10 min, and separated by reducing SDS-PAGE on an 8% gel. Fluorescence-labeled protein was visualized with a Typhoon trio fluorescence scanner (GE Healthcare, Chicago, IL), and relative protein quantities were determined using FIJI (Schindelin et al., 2012). Lanes were selected as regions of interest and transformed into 1D profile plots. Band intensities were then quantified by integrating the area of each peak in the profile plot relative to the baseline of each lane. Data was visualized using GraphPad Prism software (Version 9.3.0, San Diego, CA).

### VCF recordings

Recordings were performed in a custom-made measuring chamber (Figure 3) that is split into an upper and lower compartment, which are individually perfused and connected by a 0.75 mm hole on which the oocyte is placed. The lower compartment has a transparent bottom, and the chamber was mounted on an Axiovert 200 inverted fluorescence microscope (Carl Zeiss Microscopy LLC, Oberkochen, Germany) so that the oocyte was centered above the objective with the animal pole facing down to avoid increased background fluorescence by the lighter vegetal pole. Upper and lower compartments were separately perfused with recording solution and recording or agonist solution, respectively, using a gravity-based perfusion system and a membrane vacuum pump. Solutions in the lower compartment were switched by computer-controlled magnetic valves.

To avoid inhibition by Ca2+ or Mg2+ and Ca2+-mediated downstream effects and to obtain reproducible current responses, recordings were performed in divalent-free buffer (90 mM NaCl, 1 mM KCl, 5 mM HEPES, pH 7.4–7.5) complemented with flufenamic acid and ethylene glycol tetraacetic acid (EGTA) (both 0.1 mM). For measurements with Ca2+-containing buffers, EGTA was omitted, and Ca2+ (0.2–0.5 mM) was added (in case of P2X7-R-GECO constructs, FRET measurements between ANAP and mNeonGreen and control measurements of ANAP-containing constructs to test for Ca2+-specific effects). If not otherwise noted, the agonist solution contained 300 μM ATP and was applied for 15 s in 195 s intervals. Intracellular electrode resistances were below 1.2 MΩ, and recordings were performed at room temperature at a holding potential of –30 mV to keep the current amplitudes reproducible. The solution exchange in the lower chamber is finished in about 1 s (Lörinczi et al., 2012).

To exclude mechanically induced fluorescence changes due to solution switching, all recording protocols started with sequential applications of ATP-free recording solutions from different tubes and magnetic valves. If required, solution speed and oocyte position were readjusted to ensure the absence of mechanical artifacts.

For fluorescence recordings, the microscope was equipped with two LEDs as excitation sources (UV-LED M365LP1 with 365 nm, green LED M565L3 with 565 nm, both Thorlabs GmbH, Bergkirchen, Germany). Since UV excitation in oocytes causes relatively high background fluorescence levels, detectors must feature a wide dynamic range, while maintaining a sufficiently high sensitivity in order to record small fluorescence changes. To this end, two cooled, high-sensitivity MPPC detectors (Hamamatsu Photonics K.K., Japan) were used for simultaneous fluorescence detection at two different spectral segments. For optical filters and dichroic mirrors see Key resource table.

Single-channel fully programmable instrumentation amplifiers with Bessel low-pass filter characteristics (Alligator Technologies, Costa Mesa, CA) were used for signal scaling. To minimize photobleaching, LEDs were pulsed using self-developed high-speed LED drivers with sub-μs rise time. Pulse lengths were set in the ~20 μs range to allow for the fluorescence readout signal chain to settle. Fluorescence signal digitization was synchronized to the excitation pulses using an STM32F407 microcontroller (STMicroelectronics, Geneva, Switzerland). Its timer peripherals were re-triggered by each ADC conversion cycle in order to create an LED illumination pulse that starts shortly before the next ADC conversion cycle. Whenever two excitation wavelengths were used, excitation pulses were staggered in time with the longer wavelength excitation pulse signal being digitized first, preventing bleedthrough of background fluorescence excited by the shorter excitation wavelength to the longer-wavelength detection channel. A water-immersion objective with high numerical aperture and a large working distance (W N-Achroplan 63×/0,9 M27, Carl Zeiss Microscopy LLC, Oberkochen, Germany) was used to maximize the collection of emitted photons and to focus on the oocyte membrane.

Currents were measured with a Turbo Tec-05X amplifier and CellWorks E 5.5.1 software (both npi electronic GmbH, Tamm, Germany) and were used for current and fluorescence recordings and valve control. Current signals were digitized at 400 Hz and downsampled in CellWorks to 200 Hz.

### Dose-response analysis

To determine agonist dose-response curves, ATP was applied for 15 s in 195 s intervals. A reference concentration (ATPRef) of 300 μM was applied until stable responses were obtained and was then alternately applied with ATP concentrations ranging from 10 μM to 3 mM (ATPTest). All responses were normalized to the response of ATPRef, and EC50 values were calculated using the four-parameter Hill equation: % Response = Bottom + (Top−Bottom)/(1+10^[(LogEC50−X)*nH]) with Bottom and Top constrained to 0%, and maximum responses, respectively, X corresponding to the log of agonist concentration, and nH corresponding to the Hill coefficient.

### Data analysis

Fluorescence and current signals were analyzed and visualized using a Python-based script (for packages used, see Key resource table): Fluorescence signals were denoised using a fifth-order Bessel filter with a low-pass corner frequency of 4 Hz. Maximum amplitudes of ATP-evoked current and fluorescence responses from different receptor constructs were summarized, compared, and visualized using GraphPad Prism software (Version 9.3.0, San Diego, CA). The following inclusion criteria were applied for recordings:

(i) ATP application must evoke a current response >0.1 μA, (ii) leak currents must be stable for the duration of the recording (at least two ATP applications), (iii) repeated ATP applications must elicit reproducible current responses (>0.8 μA), (iv) fluorescence signals must be without mechanical artifacts and clearly distinguishable from fluorescence changes of wt expressing oocytes (see below). 2–3 days after injection, repeated application of 300 μM ATP to wt-expressing oocytes elicited reproducible currents (i.e. first and second current responses differed less than 10% and reached a plateau, at least during the second application), which were taken as a reference. Longer expression times resulted in irregular and irreproducible current responses and less stable oocytes. In case of mutated receptors, longer expression times were often needed to yield current responses comparable to wt P2X7.

We observed a gradual decrease in fluorescence signal for the duration of ligand application in control oocytes expressing wt receptors even in the absence of ANAP. To distinguish ANAP-specific fluorescence signals from these gradual changes, for signal analysis only fluorescence changes upon ATP application were considered that were either positive, or negative but additionally not linear. If fluorescence signals from mutant expressing oocytes were not distinguishable from fluorescence changes observed for wt expressing oocytes no fluorescence change was assumed (0% ΔF/F). Only signals that were recorded in at least three different oocytes were considered for analysis. Additionally, fluorescence changes that were recorded in less than 40% of analyzed oocytes expressing one specific receptor construct or that had averaged ΔF/F values <0.3% were not considered.

### Statistical analysis

Data were either represented as mean ± S.D., as box plots, or as mean ± S.E.M. with the number of recordings given in brackets, and statistical analysis was performed by either two-tailed unpaired Welch’s t-test or two-tailed paired Student’s t-test, as indicated. Values of p<0.05 were defined as statistically significant with *, **, ***, and **** denoting values of p<0.05, 0.005, 0.0005, and 0.0001 or 0.00005, respectively.

### Data availability

All data generated or analyzed during this study are included in the manuscript and supporting files. Original VCF recordings, extracted VCF data, and scans from SDS-PAGE gels are provided as source data files for Figure 1, Figure 1—figure supplement 1, Figure 2, Figure 2—figure supplement 1, Figure 3, Figure 3—figure supplement 1, Figure 3—figure supplement 2, Figure 3—figure supplement 3, Figure 4, Figure 4—figure supplement 1, Figure 5, Figure 5—figure supplement 1, Figure 5—figure supplement 2, Figure 5—figure supplement 3, Figure 6, Figure 6—figure supplement 1, Figure 6—figure supplement 2, Figure 6—figure supplement 3, Table 1, and Table 2. The source data files of Table 1 include source data of Figure 2—figure supplement 1, Figure 3, Figure 4, and Figure 5 and are assigned accordingly in Table 1—source data 1. The original recordings of Table 1 have been deposited with Dryad (DOI https://doi.org/10.5061/dryad.p8cz8w9tb). The source data files of Table 2 include source data of Figure 3—figure supplement 3 and Figure 5—figure supplement 2.

Note that original current and fluorescence recordings provided as comma separated value files each contain three columns of values (from left to right): (1) current values, (2) fluorescence signals of longer emission wavelengths, and (3) fluorescence signals of shorter emission wavelengths.
