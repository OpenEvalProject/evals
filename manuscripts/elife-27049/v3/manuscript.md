# Acidic C-terminal domains autoregulate the RNA chaperone Hfq

## Authors

- Andrew Santiago-Frangos<sup>1</sup> ([ORCID: 0000-0001-9615-065X](https://orcid.org/0000-0001-9615-065X))
- Jeliazko R Jeliazkov<sup>2</sup> ([ORCID: 0000-0003-4249-1955](https://orcid.org/0000-0003-4249-1955))
- Jeffrey J Gray<sup>3</sup> ([ORCID: 0000-0001-6380-2324](https://orcid.org/0000-0001-6380-2324))
- Sarah A Woodson<sup>4</sup> ([ORCID: 0000-0003-0170-1987](https://orcid.org/0000-0003-0170-1987)) †

### Affiliations

1. Cell, Molecular and Developmental Biology and Biophysics Program Johns Hopkins University Baltimore United States
2. Program in Molecular Biophysics Johns Hopkins University Baltimore United States
3. Department of Chemical and Biomolecular Engineering Johns Hopkins University Baltimore United States
4. T.C. Jenkins Department of Biophysics Johns Hopkins University Baltimore United States

† Corresponding author

## Abstract

The RNA chaperone Hfq is an Sm protein that facilitates base pairing between bacterial small RNAs (sRNAs) and mRNAs involved in stress response and pathogenesis. Hfq possesses an intrinsically disordered C-terminal domain (CTD) that may tune the function of the Sm domain in different organisms. In Escherichia coli, the Hfq CTD increases kinetic competition between sRNAs and recycles Hfq from the sRNA-mRNA duplex. Here, de novo Rosetta modeling and competitive binding experiments show that the acidic tip of the E. coli Hfq CTD transiently binds the basic Sm core residues necessary for RNA annealing. The CTD tip competes against non-specific RNA binding, facilitates dsRNA release, and prevents indiscriminate DNA aggregation, suggesting that this acidic peptide mimics nucleic acid to auto-regulate RNA binding to the Sm ring. The mechanism of CTD auto-inhibition predicts the chaperone function of Hfq in bacterial genera and illuminates how Sm proteins may evolve new functions.

## Introduction

Host factor for RNA phage Qβ replication (Hfq) is found in most sequenced bacterial genomes (Sun et al., 2002) and plays a well characterized role in post-transcriptional regulation by small non-coding RNA (sRNA) (Gottesman et al., 2006; Storz et al., 2011). Regulation by Hfq and sRNAs is important for controlling the expression of metabolic, stress-response and virulence genes in many genera (Feliciano et al., 2016). Hfq binds sRNA and facilitates interactions between sRNAs and their mRNA targets (Zhang et al., 2002; Moller et al., 2002). To chaperone sRNA target recognition, Hfq must select its substrates from a large pool of nucleic acid in the cell and efficiently dissociate from its products at the end of each RNA annealing cycle (Rajkowitsch et al., 2007).

E. coli Hfq contains an Sm-like domain (residues 7–65) that oligomerizes into a homohexameric ring with two sequence-specific RNA-binding faces. The proximal face of the ring is highly conserved and binds to uridines (Zhang et al., 2002; Schumacher et al., 2002) at the 3’-ends of bacterial small non-coding RNA (sRNA) that resemble a classic Sm binding site (Zhou et al., 2014). In E. coli and many Gram negative bacteria, the distal face of Hfq binds to AAN triplet repeats (Mikulecky et al., 2004; Link et al., 2009) found in mRNA leaders (Link et al., 2009; Soper et al., 2011) and certain sRNAs (Schu et al., 2015; Małecka et al., 2015). In addition to these sequence-specific RNA binding sites, arginine-rich basic patches at the rim of the E. coli Hfq hexamer interact with the sRNA body (Zhang et al., 2002; Otaka et al., 2011; Sauer et al., 2012; Ishikawa et al., 2012; Zhang et al., 2013) and facilitate annealing with target mRNAs (Panja et al., 2013; Zheng et al., 2016).

Like many RNA binding proteins, Hfq also possesses intrinsically disordered domains that have the potential to modulate the function of the core Sm ring. The E. coli Hfq Sm domain is flanked by a short, disordered, N-terminal domain (NTD; residues 1–6), which protrudes from the proximal face of the hexamer, and a longer disordered C-terminal domain (CTD; residues 66–102), which extends from the rim (Beich-Frandsen et al., 2011a; Vincent et al., 2012). NMR chemical shift perturbations from a comparison of full-length Hfq (Hfq102) and a truncated variant lacking the CTD (Hfq65) suggested that some part of the CTD contacts residues on the rim of the hexamer, although the specificity of these proposed contacts was uncertain since they occur near where the CTD protrudes from the ring (Beich-Frandsen et al., 2011a; Vincent et al., 2012).

The functional importance of the CTD for sRNA regulation has also been unclear, owing to the conflicting results of different studies (Sonnleitner et al., 2004; Olsen et al., 2010; Večerek et al., 2008; Salim et al., 2012). Using a combination of biophysical and genetic approaches, we recently showed that the CTD displaces RNA from the rim and proximal face of Hfq (Santiago-Frangos et al., 2016), with two important consequences. First, release of annealed dsRNA from the arginine-rich rim is accelerated, increasing Hfq turnover. Second, kinetic competition between sRNAs is increased, which allows dominant sRNAs to bind to Hfq and accumulate in the cell, while weaker competitors are degraded (Santiago-Frangos et al., 2016). The latter creates a hierarchy of sRNA regulation that depends on the CTD.

The mechanism by which the CTD displaces RNA from the core (Sm domain and NTD) of Hfq is unknown. No common sequence motifs have been identified in the CTD (Sun et al., 2002; Vincent et al., 2012; Weichenrieder, 2014; Sobrero and Valverde, 2012; Fortas et al., 2015; Updegrove et al., 2016), which varies in length and composition across bacteria (Attia et al., 2008; Schilling and Gerischer, 2009; Baba et al., 2010). This diversity is characteristic of disordered peptides, which rapidly evolve via non-conservative substitutions and indels (Liu et al., 2008; Brown et al., 2010; Light et al., 2013). Two models could explain the displacement of RNA by CTDs in E. coli Hfq. The ‘polymer brush’ model suggests the CTDs passively obstruct RNA binding sites. This model is attractive since it depends only on the length and flexibility of the CTD. In contrast, the ‘nucleic acid mimic’ model suggests that the CTDs specifically bind to basic core residues and actively compete against nucleic acids. Given the divergence of CTD and core sequences, this model predicts that CTD auto-regulation is likely in some Hfq clades but not others.

In this study, we use de novo modeling and biophysical experiments to determine the mechanism by which the CTD regulates Hfq activity. We propose that the acidic CTD tip transiently binds the rim of E. coli Hfq and makes distributed interactions with basic residues, thereby modulating RNA and DNA binding and RNA annealing. Applying our modeling procedure to Hfqs from other bacteria demonstrates that stable interactions between the acidic CTD and the basic rim correlate with the importance of Hfq for sRNA regulation in that host. Thus, our proposed mechanism of CTD auto-inhibition provides a basis for predicting the function of Hfq in different bacteria. Our approach may be useful for predicting the sequence–function relationship of disordered domains in other partially disordered proteins.

## Results

### C-terminus of Hfq is enriched for acidic residues

To search for conserved features or amino acid motifs amongst the highly heterogeneous Hfq CTDs, we first built a phylogenetic tree (Figure 1—figure supplement 1) from the multiple sequence alignment of nearly 1000 non-redundant sequences (see Methods). The cluster containing E. coli Hfq contained many other Hfq variants previously identified as functional in RNA annealing (Zheng et al., 2016) or sRNA regulation (Gottesman et al., 2006). Therefore, we examined the sequence logo of this cluster of 222 Hfqs in more detail (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig1-v3.jpg)

**Figure 1.:** (A) Sequence logo (Crooks et al., 2004) of the CTD generated from gapped alignment of Hfq sequences that clustered with Escherichia coli Hfq (Group 1 in Figure 1—figure supplement 1A,B), numbered according to the E. coli sequence. Regions of interest are denoted above. The gapped E. coli CTD sequence is shown below. Eukaryotic Sm proteins cluster separately (Figure 1—figure supplement 1D). (B) (Top) Average number of times a given core residue favorably interacts (E < −1.0 Rosetta Energy Units) with at least one acidic CTD residue, per low energy model. Acidic CTD residues most frequently interact with basic Hfq core residues. (Bottom) Mutation of acidic CTD residues 97, 99, 100 and 102 to basic or polar residues decreases the number of predicted core interactions. Error bars represent ± 1 s.d. as computed by bootstrap resampling of the computational models (see Methods and Figure 1—figure supplement 2). Of 36 core residues not predicted to interact with the CTD, 14 had accessible surface area < 2.0 A2, computed in PyMOL. (C) (Left) Example low-energy model of wildtype E. coli Hfq; top-down proximal view. Light grey, NTD; cyan, Hfq core; pink-purple, CTD; red, CTD tip. (Center) Side view of rim of the same Hfq model. (Inset) Example hydrogen bonding network at the CTD–core binding interface showing interactions between the acidic CTD residues (red) and core residues as indicated. Additional models in Figure 1—figure supplement 3.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Neighbor-joining phylogenetic tree of 985 non-redundant, representative Hfq sequences. Tree was visualized using iTOL (Letunic and Bork, 2016). (B) Sequence logo (Crooks et al., 2004) generated for Group 1, containing Pseudomonas, Vibrio, Escherichia, Shewanella, Xanthomonas and Haemophilus species. Residues are colored according to the Zappo coloring scheme. The C-terminal region of this logo is examined in Figure 1A. (C) Schematic of domain structure with logos for basic motifs on the rim of the Like-Sm (Lsm) domain and acidic residues in the C-terminal domain. (D) Neighbour-joining phylogenetic tree of a subset of the bacterial Hfqs, an Archaeal Hfq (Methanoccocus jannaschii) and human proteins containing LSm domains. This phylogenetic relationship is similar to that in Ref. (Mura et al., 2013).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** The mean lowest energy observed for ten simulations is shown in black, with ± one standard deviation filled in gray. A single simulation run with 1,000,000 attempted moves is shown in red. The change in energy between 100,000 and 1,000,000 steps is ~ 60 REU, which is marginal in comparison to the ~360 REU change in the first 100,000 attempted moves. The beneficial energy drop beyond 100,000 steps is outweighed by the computational cost. Thus, to generate one model, 100,000 low-resolution moves are attempted.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** A gallery of additional low-energy E. coli Hfq models from either a top-down view through the proximal pore (right) or side-on view of the rim (left), colored as in Figure 1.

The start of the CTD region is delineated by a proline at position 64 of E. coli Hfq that is strongly conserved across all clades. Additionally, an arginine at the beginning of the CTD (position 66 in E. coli) that packs against the lateral edge of the Hfq hexamer (Beich-Frandsen et al., 2011a; Sauter et al., 2003; Dimastrogiovanni et al., 2014) is strongly conserved. Although the middle linker region of the CTD lacks conserved motifs (Figure 1—figure supplement 1), the C-terminus is rich in acidic residues, corresponding to the sequence DSEETE in E. coli. Noting that most Hfq clusters containing a basic patch on the rim also end in acidic residues, we hypothesized that the CTD tip binds the rim. Because the basic patch is essential for sRNA binding and annealing, direct interaction between the CTD tip and the Hfq core could explain the previously observed auto-inhibition of the CTD (Santiago-Frangos et al., 2016).

### De novo modeling of CTD interactions in the Hfq hexamer

To determine whether the acidic tip of the E. coli Hfq CTD could interact with basic residues in the core, we used Rosetta FloppyTail (Kleiger et al., 2009), a de novo modeling approach for disordered regions of proteins. We updated the original FloppyTail algorithm to model multiple disordered regions simultaneously and to ensure adequate sampling of backbone degrees of freedom (see Materials and methods and Figure 1—figure supplement 2). Then, we generated and analyzed ~30,000 models of the full-length E. coli Hfq hexamer. In the lowest energy (1%) subset of models, the acidic CTD residues (D97, E99, E100, and E102) frequently interact with basic residues on the rim (R16, R17, R19 and K47) and in the NTD (K3) (Figure 1B, top). By contrast, K31 on the distal face is not predicted to be contacted by the CTD, although K31 is highly accessible. This bias accords with prior observations that the CTD does not displace RNA from Hfq’s distal face (Santiago-Frangos et al., 2016). As anticipated for a disordered domain, no single conformation dominated the ensemble of models (Figure 1—figure supplement 3). Rather, the acidic CTD tip was found to bind to various combinations of residues in the basic patch (Figure 1C, inset).

To confirm we were not simply observing the non-specific collapse of the disordered CTD onto the core, or enriching interactions between highly solvent-accessible polar residues, we repeated our simulations using a mutant Hfq in which the acidic CTD residues were replaced with polar or basic side chains (D97R-E99N-E100K-E102N). These mutations drastically decreased the frequency of predicted interactions between the basic core residues and CTD residues at positions 97, 99, 100 and 102 in our simulations (Figure 1B, bottom), without increasing predicted interactions between this mutant CTD and solvent-accessible acidic residues on the Hfq core (D9, E18, E37 and D40).

### Acidic CTD specifically binds Hfq rim

To determine whether the CTD interacts with the rim as predicted by our models, we used fluorescence anisotropy to measure the affinity of core Hfq (Hfq65) for a fluorescently-labeled CTD peptide, CTD-FITC (Figure 2A and Figure 2—figure supplement 1). CTD-FITC lacks residues 65–72 to avoid contributions to binding from this region, which packs against the Sm domain as one strand of the β-sheet (Arluison et al., 2004). Hfq65 bound to CTD-FITC with a Kd of 2.9 µM Hfq monomer in low salt buffer (cyan in Figure 2B) and 22 µM in a higher salt buffer (Figure 2—figure supplement 2). These interaction strengths are meaningful even at higher ionic strength, because the effective concentration of each individual acidic CTD tip is roughly 350 μM in the full-length protein (see Materials and methods).

![Figure 2.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig2-v3.jpg)

**Figure 2.:** (A) Scheme for in vitro binding of fluorescent CTD-FITC peptide by Hfq core. The CTD linker is shown in purple, the acidic tip in red and the N-terminal FITC as a yellow star. Hfq core is shown in cyan, with basic rim patches in dark blue. (B) Binding of CTD-FITC to variants of Hfq65 core at 30 ˚C. 45 nM CTD-FITC was titrated with 0–100 µM Hfq monomer in duplicate, and the average (±s.d.) was fit to Equation 5 (Materials and methods). (C) Reaction scheme for annealing an RNA molecular beacon to a target RNA (open bar) (Hopkins et al., 2011; Panja et al., 2015). (D) Progress curves for annealing 50 nM molecular beacon and 100 nM Target by 50 nM Hfq65 hexamer at 30°C, measured by stopped-flow fluorescence. See Figure 2—figure supplement 3 for further data. (E) Contribution of core residues to CTD binding. Interaction energy (Expected Energetic Contribution; EEC) in silico for a core residue in the Rosetta models (solid symbols and solid line; adjusted R2 = 0.77) or the average annealing rates for Target and Target-A18 relative to Hfq65 (open symbols and dashed line; adjusted R2 = 0.94) versus experimental CTD binding energy (∆∆G°) for each Hfq65 variant. The binding energy, ∆∆G° = –RTln(KdMUT/Kd), reflects the perturbation to CTD binding by a mutation in Hfq65. The interaction energy in silico or EEC is defined as the average energy of a tail–core interaction multiplied by the average number of tail–core interactions per model (Figure 1B, top and Equation 3). The relative annealing rate for Hfq65 variants, krel = kobsMUT/kobsWT, is <1 if the mutated residue is important for RNA annealing.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** WT Hfq assembles into hexamers and dodecamers that are stable to SDS-PAGE, which can be used to evaluate the oligomerization of Hfq variants. Purified Hfq protein (~2.8 µg) was separated on a 4–20% SDS-PAGE gel and stained with Coomassie blue (lanes 2–6). Samples were prepared in 2% SDS and boiled before loading. Lane 1, Protein standards (10 µL All Blue Precision Plus, NEB). Colored dots mark oligomers: green, blue, red, Hfq102 monomer, hexamer, and dodecamer; yellow and cyan, Hfq65 monomer and hexamer. Under these conditions, Hfq102 migrates as a dodecamer (red dot) and monomer (green dot) with no visible hexamer band. Hfq102-R16A only forms hexamer (blue dot) and monomer, as previously reported (Wang et al., 2011). Hfq-sCTD forms a mixture of dodecamer, hexamer and monomer. Hfq65 and its variants form hexamers with slightly different stabilities that migrate according to the number of charged surface amino acids (Rath et al., 2009; Shi et al., 2012). All of the Hfq variants used in this study were capable of hexamerisation, and none formed oligomers larger than those seen with wildtype Hfq.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** Binding of CTD-FITC to Hfq65 at 30 ˚C, in 10 mM Tris·HCl pH 7.5, 50 mM K-Glutamate. 45 nM CTD-FITC was titrated with 0–190 µM Hfq monomer in duplicate, and the average (±SD) was fit to a binding isotherm (Equation 5; Materials and methods).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** Annealing of 100 nM Target RNA to 50 nM beacon RNA by Hfq65 and Hfq65 variants was measured by stopped flow fluorescence at 30°C in 1 × TNK buffer. (A) Observed annealing constants with 0–200 nM Hfq hexamer. Cyan, Hfq65; orange, Hfq65-Q35A; pink, Hfq65-K47A; green, Hfq65-R19D; steel-blue, Hfq65-R16A. Rate constants are the average of 5 technical replicates with standard deviations less than 5%. The vertical dashed line indicates the Hfq concentration for which annealing progress curves are shown in Figure 2D and Figure 2—figure supplement 3B. The single turnover annealing rate reaches a maximum at equimolar concentrations of (Hfq)6:beacon. Higher Hfq concentrations can inhibit annealing due to random-order binding of RNA substrates and the formation of Hfq12, which is inactive (Sagawa et al., 2015). (B) Target-A18 (distal) annealed by 33 nM Hfq65 hexamer and variants on Hfq65 background. The change in fluorescence emission intensity was normalized to the maximum fluorescence within an experiment. The average of five measurements is shown per progress curve. All progress curves were fitted to single- or double-exponential rate equations to obtain kobs, as previously described (Santiago-Frangos et al., 2016).

Binding of the CTD-FITC peptide to Hfq65 was weakened by mutations in the basic rim residues R16A, R19D and K47A (Figure 2B), which frequently interact with the CTD in our computational models (Figure 1B). Although we were not able to test the predicted interactions between NTD K3 and the CTD (see Materials and methods), K3 is also known to form electrostatic interactions with the RNA backbone (Dimastrogiovanni et al., 2014). In contrast, mutation of a surface-accessible polar residue (Q35A) close to the binding interface (Figure 1C, inset), slightly enhanced CTD binding (Figure 2B). Intriguingly, A35 is common in Hfq from γ-proteobacteria. Finally, a CTD peptide containing the mutated C-terminal tip (RSNKTN) was not able to bind Hfq65, confirming that the acidic residues on the CTD peptide are necessary for this interaction (grey in Figure 2B).

### CTD-bound core residues play a role in RNA annealing

To determine how much core residues that bind the CTD contribute to Hfq’s RNA annealing activity, we compared the effect of rim mutations on the rate of base pairing between an RNA molecular beacon and the 16 nt Target RNA by stopped-flow fluorescence spectroscopy (Figure 2C) (Hopkins et al., 2011). In the absence of competition from the CTD, the rate of annealing in this assay depends only on interactions between the two RNAs and the Hfq core. As previously observed (Santiago-Frangos et al., 2016), Hfq65 is highly active in single-turnover annealing assays (Figure 2—figure supplement 3A). The observed annealing rate was most diminished by the loss of basic residues, especially the conserved R16A, and relatively unaffected by the mutation Q35A (Figure 2D). Similar results were obtained with Target-A18, which anchors to the distal face (Figure 2—figure supplement 3B). The average relative annealing rates of Hfq65 variants correlated well with the importance of each residue for CTD binding in vitro (Figure 2E), suggesting that the CTD peptide and the RNA interact with the same residues on the rim of Hfq.

The predictive value of our computational approach was validated by a direct correlation between the experimentally measured contribution (∆∆G°) of each core residue for CTD binding with the predicted Expected Energetic Contribution (EEC) of that core residue to interactions with the acidic CTD in silico (solid symbols and solid line, Figure 2E). EEC is defined as the average energy of a tail–core interaction multiplied by the average number of tail–core interactions per model. The absolute binding and simulated interaction energies cannot be directly compared because the peptide binding assay is performed in trans rather than in cis, and the Rosetta Energy does not account for entropic contributions to binding. Nevertheless, amino acids that most strongly impacted the free energy of CTD binding when mutated, also had larger contributions to CTD binding in silico (solid symbols and solid line, Figure 2E; linear regression p-value=0.078), and had stronger effects on Hfq65 RNA annealing activity in vitro (open symbols and dashed line, Figure 2E; linear regression p-value=0.020).

### Nucleic acids compete with the CTD for binding the Hfq core

If the CTD peptide and RNA interact with the same basic Hfq residues, direct competition between the two could explain how the CTD triggers the release of annealed RNAs from Hfq (Santiago-Frangos et al., 2016) and why it increases the stringency of RNA or DNA binding. To examine whether nucleic acids are in competition against the CTD for binding to the Hfq core, we compared the ability of different nucleic acids to displace CTD-FITC from a preformed Hfq65·CTD-FITC complex (Figure 3A). The strength of competition was expressed as the concentration of nucleic acid needed to displace 50% of CTD-FITC from Hfq65, IC50.

![Figure 3.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig3-v3.jpg)

**Figure 3.:** (A) Scheme for in vitro competition of the CTD-FITC·Hfq65 interaction by nucleic acids. (B) Example titrations of the CTD-FITC·Hfq65 complex with sRNA. Titrations were done in duplicate, and the averages (±s.d.) fit to Equation 6 (Materials and methods) to determine the IC50.(C) IC50 values for nucleic acids of different lengths (blue, RNA oligomers; orange, DNA oligomers; green, sRNAs). From shortest to longest: Target, A18, minRCRB, Target-U6, Target-A18, DNA1, DNA2, DNA2c, dsDNA2, ChiX, RyhB, DsrA, RprA). Dashed circles indicate nucleic acids that deviate from the linear relationship between log IC50 and length (adjusted R2 = 0.85).

Natural sRNAs strongly competed against the CTD-FITC peptide, in keeping with their strong (~10 nM) affinity for Hfq (Figure 3B). Short RNA and DNA oligomers that bind Hfq weakly were poorer competitors than natural sRNAs, as expected. In general, competition against the CTD peptide correlated with nucleic acid length, suggesting little sequence specificity, or that longer nucleic acids may occupy more than one basic patch (Figure 3C). However, minRCRB RNA, DNA1 and dsDNA2 deviated from this linear trend (dashed circles; Figure 3C). minRCRB, a stronger than expected competitor, consists of a stem-loop with a 5’-overhang, and has been shown to specifically bind to the rim (Santiago-Frangos et al., 2016; Dimastrogiovanni et al., 2014). Similarly, DNA1 possesses a stable minRCRB-like motif at its 5-end and was also a stronger competitor than expected based on its length. By contrast, the completely double-stranded dsDNA2 was a weaker competitor than expected, consistent with the CTD’s ability to displace annealed dsRNAs from the rim of Hfq (Santiago-Frangos et al., 2016).

### Higher local concentration of acidic residues increases CTD autoinhibition

The results above indicate that an interaction between the acidic CTD tip and the basic rim inhibits RNA binding to the basic patch and stimulates release of dsRNA. If this model is correct, shortening the CTD should increase the local concentration of the acidic CTD tip and exacerbate autoinhibition. Alternatively, if the CTD acts as a polymer brush, a shorter CTD should exhibit less autoinhibition because it will exclude less volume around the Hfq core. To test these predictions, we generated the mutant Hfq-sCTD, which lacks residues 86–96 (inclusive). Truncation of this non-conserved ‘linker’ region is predicted to increase the local concentration of the acidic tip around the Hfq core roughly three-fold, from roughly 350 μM per CTD in Hfq102, to ~1220 μM per CTD in Hfq-sCTD (Equation 4 in Materials and methods).

As previously shown (Santiago-Frangos et al., 2016), Hfq65, which lacks the CTD entirely, anneals the 16 nt Target and Target-U6 RNA about five times faster than full-length Hfq102 (100–60-fold vs. 20–10-fold; cyan and black in Figure 4A). In our model, this is because the CTD sweeps RNAs from the rim and proximal face of Hfq. By contrast, both proteins accelerate Target-A18 annealing roughly 100-fold compared to no Hfq, because this RNA remains anchored to the distal face of Hfq and resists CTD displacement (Santiago-Frangos et al., 2016). Importantly, the shortened CTD linker (Hfq-sCTD) decreased annealing rates relative to Hfq102 for all RNA targets (Figure 4A and Figure 4—figure supplement 1), suggesting that access to the basic patch was more restricted.

![Figure 4.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig4-v3.jpg)

**Figure 4.:** (A) Observed annealing rate constants for 100 nM target RNA and 50 nM molecular beacon with 0–200 nM Hfq hexamer at 30°C, measured by stopped-flow fluorescence. Black, Hfq102; red, Hfq-sCTD; cyan, Hfq65. (B) Fluorescence anisotropy assay for RNA binding and release. In stopped-flow FRET experiments, the dsRNA is released after pairing with its complementary strand (Panja et al., 2013; Santiago-Frangos et al., 2016). D16-FAM RNA (50 nM) was allowed to bind 50 nM Hfq hexamer. The Hfq·D16-FAM complex was challenged with 50 nM complementary R16 RNA. Most of the D16-FAM·R16 product is released from Hfq102 and Hfq102-sCTD, but not Hfq65. Remaining RNA was displaced from Hfq by excess ssDNA (400 nM DNA2). The averages and standard deviations for three trials are plotted for each Hfq variant. (C) Molar fractions of D16-FAM·R16 product released (light grey), remaining D16-FAM·Hfq·R16 ternary complex (hatched), and Hfq·D16-FAM binary complex (dark grey) calculated from Equation 7 (Materials and methods), based on the anisotropies at the end of the annealing phase and the maximum anisotropies of ternary complexes from equilibrium binding experiments (Table 3). (D) Annealing of 5 nM 32P-ChiX sRNA with 30 nM chiP mRNA without Hfq, or with Hfq65, Hfq102 or Hfq-sCTD, as indicated above each lane. Samples were loaded on a native polyacrylamide gel 60 min or 20 s after the components were mixed. Full gel images are in Figure 4—figure supplement 2. (E) Fractions of free ChiX (black), ChiX·chiP dsRNA (light grey), ChiX·Hfq·chiP ternary complex (hatched) and ChiX·Hfq binary complex (dark grey) after 4 min of annealing, as analyzed by EMSA (Figure 4—figure supplement 2).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Annealing of 100 nM Target RNA to 50 nM beacon RNA by Hfq variants was measured by stopped flow fluorescence at 30°C in 1 × TNK buffer. (A) Target RNA annealed by Hfq65 (no CTD), Hfq102 (complete CTD) or Hfq-sCTD (shortened linker CTD). (B) Target-U6 (proximal) annealed by Hfq65, Hfq102 or Hfq-sCTD. (C) Target-A18 annealed Hfq65, Hfq102 or Hfq-sCTD. The change in fluorescence emission intensity was normalized to the maximum fluorescence within an experiment. The average of five measurements is shown per progress curve. Annealing data were also collected for 0–200 nM Hfq hexamer. All progress curves were fitted to single- or double-exponential rate equations to obtain kobs, as previously described (Santiago-Frangos et al., 2016).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** EMSAs of the annealing of 5 nM 32P-ChiX to 30 nM chiP (Rasmussen et al., 2009) at 10°C in 1 × TNK buffer. Reactions were done (A) without Hfq, or with 33.3 nM hexamer (B) Hfq102, (C) Hfq65 or (D) Hfq-sCTD, Control reactions with ChiX only, ChiX and chiP mRNA, ChiX and Hfq or three components were loaded at the beginning (left) and end (right) of each time course, as indicated above the lanes. In the absence of Hfq, only 20% of ChiX·chiP annealed after 30 min. In the presence of all Hfq variants, at least 50% ChiX was in a ternary complex containing ChiX·Hfq·chiP within 1 min, and annealing reached a plateau within 2 min. In corroboration with the RNA oligomer annealing data (Figure 4C), the ternary complex was most stable with Hfq65, medium with Hfq102 and least stable with Hfq-sCTD.

Next, we used steady-state fluorescence anisotropy to examine how a shorter CTD affects the release of annealed dsRNA from the Hfq core (Figure 4B). Binding of Hfq102, Hfq65 or Hfq-sCTD to FAM-labeled D16 RNA increased the anisotropy of FAM fluorescence, as expected (Figure 4D). The smaller anisotropy of the Hfq65·D16-FAM complex is due to its smaller hydrodynamic drag, since all Hfqs have similar affinities for D16-FAM (Table 1). When complementary R16 RNA was added to the Hfq102·D16-FAM complex, the anisotropy decreased since most of the annealed dsRNA dissociated from Hfq102 (Santiago-Frangos et al., 2016) (black, Figure 4B). Whereas, when complementary RNA was added to the Hfq65·D16-FAM complex, the anisotropy increased (Santiago-Frangos et al., 2016), because a large proportion of the dsRNA remained bound to Hfq65 (cyan, Figure 4C). When the same experiment was done for Hfq-sCTD, the anisotropy decreased even further than for Hfq102, suggesting that more dsRNA was released when the CTD is shortened. This smaller anisotropy cannot be explained by the slightly smaller molecular weight of Hfq-sCTD, since the maximum anisotropies of Hfq102 and Hfq-sCTD ternary complexes during equilibrium binding experiments were very similar.

**Table 1.**
 Equilibrium dissociation constants for Hfq.Values are the mean ± SD of three independent experiments. Kd values were determined by fluorescence anisotropy (see Methods). *Values were previously determined (Santiago-Frangos et al., 2016).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Kd (nM hexamer)</th>
      <th colspan="3">Hill coefficient</th>
    </tr>
    <tr>
      <th>RNA</th>
      <th>Hfq102</th>
      <th>Hfq65</th>
      <th>Hfq-sCTD</th>
      <th>Hfq102</th>
      <th>Hfq65</th>
      <th>Hfq-sCTD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>D16-FAM</td>
      <td>15.5 ± 0.9*</td>
      <td>20.0 ± 1.3*</td>
      <td>12.9 ± 2.1</td>
      <td>0.7 ± 0.1*</td>
      <td>0.6 ± 0.1*</td>
      <td>0.8 ± 0.1</td>
    </tr>
    <tr>
      <td>D16-FAM·R16</td>
      <td>117 ± 12</td>
      <td>45.5 ± 2.4</td>
      <td>181 ± 12</td>
      <td>1.2 ± 0.1</td>
      <td>1.0 ± 0.1</td>
      <td>1.0 ± 0.1</td>
    </tr>
    <tr>
      <td>minRCRB</td>
      <td>13.9 ± 1.5*</td>
      <td>6.46 ± 0.7*</td>
      <td>20.1 ± 1.9</td>
      <td>1.4 ± 0.2*</td>
      <td>2.5 ± 0.6*</td>
      <td>1.1 ± 0.1</td>
    </tr>
  </tbody>
</table>

As a control, we also measured the relative affinities of each Hfq for the dsRNA product (D16-FAM·R16) versus ssRNA substrate (D16-FAM), Krel = Kd(P)/Kd(S) (Table 1). The Krel of each protein corresponded to the efficiency of product release in the anisotropy experiment (Figure 4C and Table 3): Hfq102 had a high Krel = 7.5, Hfq65 had a low Krel = 2.3, and Hfq-sCTD had the highest Krel = 14.0. Thus, the number of non-conserved residues between the acidic tip and the core of Hfq dictates the stringency of CTD autoinhibition and the efficiency of dsRNA displacement, presumably by controlling the effective concentration of the acidic tip around the Hfq core.

### CTD limits sRNA-mRNA association

To determine whether the above results on RNA oligomers apply to natural RNA substrates for Hfq, we examined the annealing of the Class II sRNA ChiX to the mRNA chiP via electrophoretic mobility shift assays (EMSAs). Because the mRNA targets of class II sRNAs interact with the rim of Hfq (Schu et al., 2015; Małecka et al., 2015), we reasoned that this sRNA-mRNA pair would be sensitive to displacement by the CTD. Low nanomolar amounts of ChiX and chiP anneal very slowly at 10°C, in the absence of Hfq (Figure 4—figure supplement 2). Whereas, Hfq102, Hfq65 and Hfq-sCTD all form a ternary complex with ChiX and chiP within 20 s (Figure 4D), reaching equilibrium in a few minutes (Figure 4—figure supplement 2). These results demonstrate that the CTD is not necessarily required for annealing longer natural RNAs. In addition, Hfq65 formed the most stable ChiX·Hfq·chiP ternary complex, with almost no ChiX-Hfq65 binary complex remaining after 20 s (Figure 4E). Less ternary complex was formed by Hfq102, and the least by Hfq-sCTD. These results are consistent with the idea that the CTD limits access of chiP mRNA to the rim of Hfq.

### DNA binding is regulated by the CTD

Hfq binds dsDNA and has been reported to associate with the bacterial chromosome (Kajitani et al., 1994; Takada et al., 1997; Azam and Ishihama, 1999; Updegrove et al., 2010; Jiang et al., 2015). Since the CTD peptide competes with DNA for binding to the Hfq core (Figure 3B) and inhibits binding of dsRNA and dsDNA more strongly than ssRNA (Table 1 and Figure 3), we asked whether the CTD modulates binding of Hfq to DNA. A change in DNA binding could alter the distribution of Hfq within the cell.

We quantified Hfq102 binding to linearized pUC19 DNA by measuring the change in DNA electrophoretic mobility in 1.5% agarose (Figure 5A,B). The mobility of the DNA-Hfq complexes decreased with added Hfq102, indicating increasing numbers of Hfq hexamers bound per DNA. The complexes exhibited uniform mobility at each protein concentration, however, except for a smear below the main band that may arise from dissociation of Hfq during electrophoresis (Figure 5C, top). This pattern is consistent with an equal (non-cooperative) distribution of Hfq102 between DNA molecules, although Hfq was previously suggested to bind DNA cooperatively (Cech et al., 2016). Cooperative binding to neighboring sites on the DNA would result in distinct bound and unbound populations of pUC19 (Tapias et al., 2000; Kozlov et al., 2010), which we do not observe here. The rim mutation R16A lowered the maximum gel retardation and increased the intensity of the ‘smear’, consistent with a reduced affinity of this mutant for dsDNA (Updegrove et al., 2010).

![Figure 5.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig5-v3.jpg)

**Figure 5.:** (A, B) Agarose gel electrophoretic mobility shift assays of 0–3.3 μM hexamer Hfq102, Hfq102-R16A, Hfq65 or Hfq65-R16A binding to 6 nM linear pUC19 DNA (2635 nts) at 25°C, stained with SYBR Gold. Hfq65 forms large aggregates that fail to enter the gel (Figure 5—figure supplement 1). (C, D) Line densitometry of DNA migration in (A, B). Free pUC19 (no Hfq) is shown in light grey. Samples with increasing Hfq concentration are shown in darker shades of grey. (E, F) RNA competition. Complexes of 0.5 μM Hfq102 hexamer and 6 nM linear pUC19 (black) were challenged by 0–2 μM RNA or DNA competitor (darker shades of red). pUC19 control in the absence of Hfq is shown in light grey. Icons indicate the binding surface for each competitor. See Figure 5—figure supplement 2 for gel images.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) Protease assay. 3.5 µM Hfq hexamer incubated with 6 nM linear (L) plus relaxed circular (N) pUC19 DNA at 25°C, for 30 min, in 50 mM Tris-HCl pH 7.5 and 10 mM CaCl2. The samples were divided in two. One set was diluted with a small amount of buffer and incubated at 25°C for an additional 2 hr. The second set was brought to 0.5% SDS, and 0.4 U Proteinase K (NEB) was added, followed by incubation at 50°C for an additional 2 hr. Loading dye was added to all samples just before they were loaded onto a native gel. Under the extended incubation time, both Hfq65 and Hfq65-R16A form insoluble aggregates with DNA which do not enter the gel (lanes 4 and 5). Digestion of Hfq65 and Hfq65-R16A with Proteinase K liberates DNA from Hfq•DNA aggregates, allowing it to be detected (lanes 9 and 10). (B) Pelleting assay. 3.5 µM Hfq hexamer was incubated with 15 nM 1000 bp DNA (Thermo Scientific) at 25°C for 30 min in 50 mM Tris-HCl pH 7.5. Hfq·DNA aggregates were pelleted by centrifugation at 20,000 × g, 4°C, for 30 min. Supernatants were removed and split in two. The pellet and half the supernatant were brought to 1 M NaCl, and the Hfq·DNA aggregates were further disrupted by phenol-chloroform extraction, before all of the samples were loaded on an agarose gel. Nearly all of the Hfq65·DNA complexes were found in the pellet fraction. The small proportion of Hfq65·DNA complexes remaining in the supernatant were only detected in the gel after treatment with salt. Hfq65-R16A·DNA complexes were more evenly distributed between pellet and supernatant fractions, and some untreated Hfq65-R16A·DNA complexes in the supernatant were able to enter the gel.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** EMSAs of 0.5 μM Hfq102 hexamer binding to 6 nM linearized pUC19 plasmid, that were competed with 0.1–2 μM RNAs or DNA at 30°C. Gels were run in a cold room. Signal intensity on a line drawn through the center of each lane was plotted (Figure 5). (A) Competition of Hfq102·pUC19 complexes with A18, Target-A18, Target and Target-U6 RNAs. (B) Competition of Hfq102·pUC19 complexes with DNA oligomer DNA1, RNA oligomer minRCRB, and sRNAs ChiX and RyhB.

In contrast to the results with the full-length protein, we observed two behaviors when Hfq65 core interacted with pUC19 DNA. At low protein concentrations, the DNA was sparsely bound by Hfq65, resulting in a small mobility shift (Figure 5B). At higher protein concentrations, the DNA formed aggregates that were too large to enter the gel, resulting in a loss of signal (Figure 5B and Figure 5D, top). Aggregation of the DNA was confirmed by solubilization with Proteinase K or by pelleting assays (Figure 5—figure supplement 1). The rim mutation Hfq65-R16A rescued the formation of insoluble aggregates, confirming that dsDNA interacts with the basic rim and not the CTD itself, as previously proposed (Jiang et al., 2015). Moreover, the Hfq65-R16A complexes migrated more slowly than those formed by similar concentrations of Hfq102 (Figure 5C and Figure 5D, bottom), suggesting that Hfq65 and Hfq65-R16A bind pUC19 at higher densities than Hfq102. Thus, the CTD appears to limit Hfq102 binding to DNA, perhaps by maintaining a regular spacing between Hfq hexamers or by enforcing a dynamic equilibrium between bound and free protein. By contrast, when the Hfq core is exposed by deletion of the CTD, Hfq65 binds and aggregates dsDNA indiscriminately.

To examine which Hfq surfaces bind dsDNA, we challenged complexes of 0.5 μM Hfq102 hexamer and pUC19 DNA with 0–2 μM RNA or DNA oligomers that interact with different sites on Hfq (Figure 5E and Figure 5—figure supplement 2). A18 RNA that binds the distal face of Hfq did not compete for DNA binding (Figure 5E, top). However, when the 16 nt Target RNA that weakly interacts with the rim is appended to A18 (Target-A18), the oligomer strongly competed against DNA for binding to Hfq (Figure 5E). Target-U6 was also a good competitor, whereas the 16 nt Target sequence alone, which binds Hfq102 weakly at the rim (1 µM), was a poor competitor. DNA1 and minRCRB, which bind to the rim of Hfq (Santiago-Frangos et al., 2016; Dimastrogiovanni et al., 2014) (Figure 3C), but have low affinities for Hfq102, were weak competitors for DNA (Figure 5F). Finally, the sRNAs ChiX and RyhB were the strongest competitors, with competition saturating at a 1:1 ratio of sRNA to Hfq102 hexamer (Figure 5F).

Overall these data indicate that the CTD does not directly bind DNA as previously suggested (Updegrove et al., 2010; Jiang et al., 2015), but rather modulates the ability of the Hfq core to bind DNA, so that the extent of binding is limited and Hfq-DNA complexes remain soluble. Our data do not conflict with a low-resolution SANS model that suggests Hfq binds perpendicularly to the DNA duplex with a slight tilt (Jiang et al., 2015), but suggest that this occurs when the basic rim of Hfq interacts with the phosphate backbone of the DNA duplex. We note that the potent competition from sRNAs, which are more numerous than Hfq in the cell (Wagner, 2013), calls into question the hypothesis that E. coli Hfq regulates cellular processes via DNA binding (Sobrero and Valverde, 2012; Cech et al., 2016).

### CTD–core interactions in other bacterial Hfq’s

Our results on E. coli Hfq show that the strength and frequency of CTD–core interactions depend on the number of basic residues in the core, the acidic residues in the CTD, and the linker length. Thus, our proposed mechanism for CTD-core interactions can be used to predict how the degree of CTD autoinhibition may vary among bacterial Hfq’s. We applied our de novo modeling procedure to estimate the CTD–core interactions in four other bacterial Hfqs (Figure 6A) for which the genetic function and in vitro annealing activity have been previously characterized (Zheng et al., 2016; Bohn et al., 2007; Liu et al., 2010; Rochat et al., 2015; Christiansen et al., 2004; Oglesby-Sherrouse and Vasil, 2010). We examined low energy models of each Hfq hexamer, and compared how frequently acidic CTD residues interact with basic rim and NTD residues (‘on-target’) versus other core residues (‘off-target’) (see Materials and methods) (Figure 6B,C). This comparison was quantitatively expressed as the difference in the EEC of on-target and off-target interactions (∆EEC).

![Figure 6.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig6-v3.jpg)

**Figure 6.:** (A) Alignment of modeled Hfq sequences in order of decreasing in vitro RNA annealing activity. Residues are numbered according to the E. coli sequence. Yellow stars, residues mutated in this study; red hexagon, last residue in Hfq65; grey box, linker removed in Hfq-sCTD. (B) Average number of favorable interactions per model for each core residue with at least one acidic CTD residue (Equation 1) in the lowest energy models (≤1%). As in Figure 1B. Number of residues with < 2.0 A2 accessible surface area: P. aeruginosa, 10; L. monocytogenes, 25; B. subtilis, 19; S. aureus, 12. (C) Top-down (proximal face) and side (rim) views of example low-energy models for each Hfq, as in Figure 1C. (D) Relative RNA beacon annealing rate for Target-U6 (boxes) and Target-A18 (circles) in Hfq vs. no Hfq (relative kobs) versus the specificity of predicted CTD–core interactions (∆EEC) for B. subtilis, S. aureus, L. monocytogenes and E. coli Hfq (blue), and P. aeruginosa Hfq, which is more active in vitro than predicted by its ΔEEC (red). Annealing data are from Zheng et al. (2016).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** A chimera of E. coli Hfq core (residues 1–65 E. coli numbering) and the B. subtilis CTD (residues 66–102 E. coli numbering; Figure 6A) was modeled with Rosetta FloppyTail as in Figure 1. (A) Average number of energetically favorable interactions (E < −1.0 Rosetta Energy Units) with at least one acidic CTD residue, per low energy model as in Figure 1. Error bars (±1 SD) computed by bootstrap resampling. 14 of the core residues not predicted to interact with the CTD were solvent inaccessible. (B) Binding of BsCTD-FITC peptide to E. coli Hfq65 core at 30 ˚C. 45 nM BsCTD-FITC was titrated with 0–100 µM Hfq monomer in duplicate, and the average (±SD) was fit to Equation 5 (Materials and methods) with Kd = 8.7 µM. Although the binding strength is three time weaker than for the E. coli CTD peptide, the rank order for interactions with basic core residues no longer coincides with their relative importance for RNA annealing in vitro (Figure 2E). Therefore, the B. subtilis CTD may not be optimal for auto-regulating the core of E. coli Hfq.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig6-figsupp2-v3.jpg)

**Figure 6—figure supplement 2.:** Monomer-resolution, log-scale, heat maps of interactions between the CTDs and core residues, in the first percentile of models, sorted by energy, for all species of Hfq. The monomer identities (A, B, C, D, E, and F; corresponding to the chain identities in the input PDB) are specified for the CTD (tail) along the y-axis and the core along the x-axis. Counts are added to each bin if an interaction between a CTD residue and core residue, belonging to the respective monomer, is observed. Longer CTDs (e.g. E. coli) can interact with all monomers, but are not required to do so (e.g. L. monocytogenes).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/27049/elife-27049-fig6-figsupp3-v3.jpg)

**Figure 6—figure supplement 3.:** Similar to Figure Supplement 1 except counts are added to each bin if an interaction between an acidic CTD residue and a basic core residue (see Materials and methods for selection definitions), belonging to the respective monomer, is observed. Longer CTDs (e.g. E. coli) can interact with all monomers, but are not required to do so (e.g. L. monocytogenes).

For E. coli Hfq, an active chaperone with a basic rim patch and long CTD, the CTD tip tended to interact with basic residues on the rim and NTD more often and more strongly than with other residues, resulting in ΔEEC = −1.11 ± 0.20 REU. This was also true for Listeria monocytogenes Hfq (ΔEEC = −1.08 ± 0.22 REU). In contrast, Bacillus subtilis (ΔEEC = 0.51 ± 0.14 REU) and Staphylococcus aureus (ΔEEC = 0.19 ± 0.05 REU) Hfq, which are inactive in our in vitro annealing assay (Zheng et al., 2016), did not exhibit specific CTD-core interactions. Finally, in models of full-length Pseudomonas aeruginosa Hfq, the CTD adopts an extended β conformation that wraps over the rim of the hexamer and places the C-terminal acidic residues near the weakly basic NTDs (ΔEEC = −0.30 ± 0.04 REU) (Figure 6C). In the absence of the NTD, however, the CTDs dock with R16 and K17 on the rim (ΔEEC = −0.50 ± 0.18 REU). Thus, Hfqs that do not anneal RNA in vitro tend to possess shorter, less acidic CTDs that form weaker and less frequent interactions with the basic rim and NTD in silico (Figure 6D). There is a similar trend between ∆EEC and the importance of Hfq for sRNA regulation in each bacterium (Zhang et al., 2013; Bohn et al., 2007; Liu et al., 2010; Rochat et al., 2015; Oglesby-Sherrouse and Vasil, 2010; Tsui et al., 1994; Nielsen et al., 2010; Rochat et al., 2012).

In the above examples, both the CTD and the core co-vary between different species. We next asked whether the CTD conferred specificity or strength to CTD-core interactions. We modeled an Hfq chimera consisting of the highly basic E. coli Sm core, fused to the shorter and slightly less acidic B. subtilis CTD. In our models, the B. subtilis CTD contacted K3 in the NTD and R17 on the rim more frequently than E. coli CTD (Figure 6—figure supplement 1A), but contacted R16 and R19, which are functionally very important (Figure 1 and Figure 2), less frequently than E. coli CTD (Figure 6—figure supplement 1A). This was corroborated with fluorescence anisotropy results showing that E. coli Hfq65 binds a BsCTD-FITC peptide about three times more weakly than its own CTD (8.7 µM vs. 2.9 µM; Figure 6—figure supplement 1B). Although we have shown that a foreign CTD can bind the core of E. coli Hfq, the ‘specificity’ of this interaction may have been lost.

## Discussion

We previously found that the flexible CTD of E. coli Hfq sweeps RNAs from the proximal and rim surfaces of the Hfq ring by an unknown mechanism (Santiago-Frangos et al., 2016). Because the mechanism was not known, it was not possible to predict whether other bacterial Hfq CTDs, which are highly variable in sequence composition and length, would perform similar functions. Here, we have used computational models and experiments to show that the acidic tip of the CTD directly displaces RNA from basic patches on the rim of Hfq. The CTD’s mimicry of nucleic acids is supported by direct competition between nucleic acids and the CTD for binding the Hfq core, and stronger autoinhibition when the linker connecting the acidic tip to the core is shortened (Hfq-sCTD). The good agreement between the modeled CTD–core contacts and the contributions of individual residues to the measured CTD binding energies and to RNA annealing validates our modeling approach, and further suggests that nucleic acids and the acidic tip of the CTD interact with the same residues in the Hfq core. As expected for a nucleic acid mimic, CTD·core interactions are dominated by electrostatics and exhibit a salt dependence (Figure 2 and Figure 2—figure supplement 2) similar to that seen for the autoregulatory CTD of HTLV-1 nucleocapsid (Qualley et al., 2010).

Our results show that competition between the CTD and RNA improves the efficiency of E. coli Hfq’s chaperone activity while increasing the stringency of substrate selection. In our model, sRNA and mRNA substrates are recruited through specific interactions with the proximal or distal face of the Sm ring. When complementary RNA segments engage one or more basic patches on the rim of Hfq, these interactions favor nucleation and zippering of the double helix (Panja et al., 2013; Panja et al., 2015). Transient interactions between the CTD and the rim leads to the displacement of the dsRNA product, preventing strand dissociation and recycling Hfq. In support of the model, we observe that Hfq102 binds dsRNA less strongly than single-stranded RNA, whereas Hfq65 binds them more similarly (Table 1).

We propose that the CTD makes Hfq a more selective RNA binding protein by inhibiting access to its rim. Single-stranded nucleic acids compete with the CTD approximately in proportion to length, suggesting that nucleic acid binding to the Hfq rim has low sequence-specificity. Consequently, short RNAs that only bind the rim, such as the 16 nt Target, weakly compete with the CTD and are poor substrates for annealing. By contrast, sRNAs or mRNAs that specifically bind the proximal or distal face of Hfq strongly compete against the CTD, and gain access to the basic patch on the rim. We previously showed that the CTD increases competition among E. coli sRNAs, resulting in different levels of sRNA accumulation in the cell (Santiago-Frangos et al., 2016). It remains to be shown whether the CTD also increases the stringency of target site selection. The six CTDs, which are disordered and mobile (Beich-Frandsen et al., 2011b), exclude a large volume around the core of E. coli Hfq (Figure 1C). This excluded volume is expected to limit the number of sRNAs that may bind E. coli Hfq at any one time, perhaps further increasing the stringency of RNA selection.

The hyper-variability of the Hfq CTD among different bacteria points to a continuous optimization of autoinhibition and binding selectivity, possibly in response to the acquisition or evolution of novel sRNA-mRNA regulatory pairs (Peer and Margalit, 2014). A balance of interactions at the rim of Hfq is needed, since a CTD that inhibits RNA binding too strongly may adversely affect interactions with genuine RNA substrates (Figure 4). Conversely, our DNA binding results show that an exposed basic patch can bind DNA (and RNA) indiscriminately, hinting that a basic patch necessitates co-evolution with a ‘protective’ CTD. Intriguingly, most Hfqs contain acidic sequences at the end of the CTD (Figure 1—figure supplement 1), despite a general bias toward basic residues at protein C-termini (Berezovsky et al., 1999) and within intrinsically disordered domains (Williams et al., 2001; Lise and Jones, 2005). Additionally, the CTDs of E. coli Hfq are long enough to contact the rims of neighboring monomers (Figure 6—figure supplements 2–3), which may explain the contribution of the CTD to hexamer stability (Vincent et al., 2012), and inter-hexamer contacts (Figure 2—figure supplement 1).

Computational modeling provided atomic-scale insight to the accessible conformations of the disordered N- and C- termini of E. coli Hfq (Figure 1C). Our experimentally validated EEC metric (Figure 2E) defines residue–residue interactions more accurately with respect to experimental data than commonly used distance cutoffs (Cα–Cα and Cβ–Cβ) (Kleiger et al., 2009; Fischer et al., 2006). This de novo modeling strategy was able to identify frequent and specific CTD–rim interactions in Lm and Pa Hfq, which act in sRNA regulation and annealing (Panja et al., 2013; Zheng et al., 2016; Bohn et al., 2007; Liu et al., 2010; Rochat et al., 2015; Rochat et al., 2012), but not for Bs and Sa Hfq (Figure 6D), in agreement with in vitro experiments. This suggests that the FloppyTail algorithm could be generally useful for predicting the interactions of disordered regions with ordered domains.

Many RNA and DNA binding proteins contain disordered or flexible domains that have been implicated in cooperativity, autoinhibition and liquid phase separation (Trudeau et al., 2013; Varadi et al., 2015; Järvelin et al., 2016). Hfq is an example of an emerging paradigm of autoregulation of nucleic acid binding by nucleic acid mimic peptides. Other examples in which a disordered CTD autoinhibits RNA or DNA binding include HTLV-1 NC (Qualley et al., 2010), E. coli gyrase (Tretter and Berger, 2012), E. coli ssDNA binding protein (Kozlov et al., 2010) and mammalian high-mobility group B1 (Watson et al., 2007). Unlike HTLV-1 NC, which also remodels RNA, the Hfq CTD gives rise to dynamic cycling of bound RNAs needed to chaperone sRNA-mRNA interactions. Our modeling procedure could be utilized to screen disordered domains found in kinases, such as myosin light chain kinases and protein kinase C (Kobe and Kemp, 1999), and nucleic acid binding proteins from all kingdoms of life (Trudeau et al., 2013; Adams, 2003; Ward et al., 2004; Wang et al., 2016).

## Materials and methods

### Hfq alignments and sequence logos

All Hfq gene sequences were taken from Uniprot (UniProt Consortium, 2015). 5359 sequences were aligned using the G-INS-1 algorithm on MAFFT webservers (Yamada et al., 2016). This alignment was reduced using CD-HIT (Li and Godzik, 2006) and Max-Align (Gouveia-Oliveira et al., 2007). An unrooted, neighbor-joining tree of the remaining 985 non-redundant, representative, sequences was made on MAFFT webservers (Yamada et al., 2016). Sequence logos of re-aligned sequences from chosen clusters were generated using WebLogo (Crooks et al., 2004).

### Computational modeling of the intrinsically disordered regions

#### Structure preparation

The crystal structures of E. coli (1HK9) (Sauter et al., 2003), P. aeruginosa (1U1S) (Nikulin et al., 2005), L. monocytogenes (4NL2) (Kovach et al., 2014), B. subtilis (3HSB) (Someya et al., 2012), and S. aureus (1KQ1) (Schumacher et al., 2002) Hfqs were used as starting points for the computational modeling. All crystal structures contained the hexameric form of Hfq, except for 4NL2, for which we generated the biologically relevant hexamer using the reported symmetry operations. Missing residues were appended or prepended to the crystal structures in the following manner. First, on a single subunit, absent N-terminal residues were prepended and all N-terminal residues predicted to be disordered (Buchan et al., 2013; Jones and Cozzetto, 2015) were initialized in an extended conformation, with backbone dihedral angles set to: $ϕ=-135°$ and$ψ=135°$. Since the Hfq hexamer is C6 symmetric, the modified subunit could be symmetrized to all other subunits. The same process was repeated to append C-terminal residues, except the base of the tail (residues 64–69 in 1HK9, 1U1S, and 1KQ1, 66–71 in 4NL2, and 62–67 in 3HSB) was ‘kinked’ to point proximally as in the 1HK9 structure. For the RSNKTN tail mutant, side chains were mutated using the PyMOL ‘mutate’ function. The structures with extended termini were ‘relaxed’ with constraints, using Rosetta (Conway et al., 2014), to eliminate energetically unfavorable atomic clashes, before modeling.

#### Modeling

A modified version of the FloppyTail algorithm (Kleiger et al., 2009) was used to model the disordered termini (see Appendix 1 for step-by-step protocol). The source code is freely available to academic users through the RosettaCommons: www.rosettacommons.org. The FloppyTail algorithm generates hypothetical, low-energy conformations of disordered regions through two stages of modeling: (i) low-resolution modeling, where side chains are represented as single pseudo-atom centroids, with aggressive sampling of backbone conformational space and gradient-based minimization, and (ii) all-atom modeling, where all side-chain atoms are restored, with fine sampling of backbone conformational space, side-chain optimization, and minimization. We adapted the original algorithm to permit simultaneous modeling of multiple disordered termini and to more extensively sample conformation space. In our simulations, any Hfq region predicted to be disordered was allowed to move and approximately 500 backbone moves (changes in ϕ/ψ angles) were attempted per disordered residue (Kleiger et al., 2009) attempted ~25 backbone moves per disordered residue). Non-disordered residues had no backbone motion, but were permitted to sample side-chain conformations. In total, simulations were used to generate ~30,000 hypothetical structures for each species’ Hfq.

#### Analysis

PyRosetta (Chaudhury et al., 2010) was used to evaluate the energies of pairwise residue–residue interactions. Pairwise energies were computed with the talaris2014 energy function (O’Meara et al., 2015), comprised of terms capturing van der Waals, solvation, hydrogen bonding and electrostatic interactions. If a pairwise energy was unfavorable (0 or greater), we did not consider it for further analysis.

In our analysis, we considered a set of core residues $𝒞$ and a set of tail residues $𝒯$. We calculated the average number of tail interactions for a single core residue, $x\in𝒞$, by counting the number of pairwise interactions, with a lower energy than the threshold, between x and every residue in the $𝒯$ and dividing by the total number of CTDs:

$$
⟨N_{x}⟩=\summodels\sumsubunits \sumy\in𝒯\delta(x,y)/(N_{subunits}N_{models}),
$$

where

$$
\delta(x,y)={1, if E(x,y)<−1 REU0, if E(x,y)\geq−1 REUand E(x,y) is the pairwise energy.
$$

To compute a standard deviation for the average number of interactions with core residue $x$, we used bootstrap resampling as described in Chaudhury et al. (2011). We resampled, with replacement, our set of models for $B=1,000$ times and re-computed $N_{x}^{'}$ (same as Equation 1, but using the resampled set of models), acquiring a standard deviation: $\sigma_{N}^{2}=\frac{1}{B}\sum_{B}N_{x}^{'}-N_{x}^{'}^{2}$.

In addition, we calculated the average energy for each interaction above the threshold (between one core residue, $x\in𝒞$, and a set of tail residues, $𝒯$):

$$
⟨E_{x:𝒯}⟩=\frac{1}{N_{subunits}N_{models}}\summodels \sumsubunits \sumy\in𝒯E(x,y) \delta(x,y),
$$

The standard deviation for the interaction energy was computed without bootstrap resampling; the energy has a distribution within a set of models, whereas the presence of an interaction is binary and only varies when the models are resampled. We compute the standard deviation as:

$$
\sigma_{E}^{2}=\frac{1}{N_{subunits} N_{models} }\summodels \sumsubunits(\sumy\in𝒯E(x,y) \delta(x,y)−⟨E_{x:𝒯}⟩)^{2}.
$$

Finally, EEC was computed over a set of basic core residues, by multiplying the average tail–core interaction energy by the average number of interactions per model and summing:

$$
EEC=\sumℬ ⟨N_{x}⟩⟨E_{x:𝒯}⟩.
$$

Standard deviation for EEC was computed by assuming that the standard deviations of the above values are independent: $\sigma_{EEC}^{2}=\sigma_{E}^{2}\sigma_{N}^{2}+\sigma_{E}^{2}⟨N_{x}⟩^{2}+\sigma_{N}^{2}⟨E_{x:𝒯}⟩^{2}$.

#### Tail/Core Selections (E. coli numbering)

<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Core (𝒞)</th>
      <th>Basic core (ℬ,for EEC)</th>
      <th>Acidic tail (𝒯)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E. coli</td>
      <td>1–65</td>
      <td>3, 16, 17, 19, 47</td>
      <td>97, 99, 100, 102</td>
    </tr>
    <tr>
      <td>P. aeruginosa</td>
      <td>1–65</td>
      <td>3, 5, 16, 17, 19, 47</td>
      <td>94, 97</td>
    </tr>
    <tr>
      <td>L. monocytogenes</td>
      <td>1–65</td>
      <td>2, 16, 17, 19, 35</td>
      <td>100, 102</td>
    </tr>
    <tr>
      <td>B. subtilis</td>
      <td>1–65</td>
      <td>2, 16, 17, 37</td>
      <td>100, 102</td>
    </tr>
    <tr>
      <td>S. aureus</td>
      <td>1–65</td>
      <td>10, 16, 41</td>
      <td>65, 67, 99, 101, 102</td>
    </tr>
  </tbody>
</table>

### Local concentration of the acidic CTD tip in E. coli Hfq

The intrinsically disordered CTD linker was represented by a worm-like chain model (Kratky and Porod, 1949) with a statistical chain segment of 35 Å or 10 residues, which is twice the persistence length of 15–20 Å for a random coil polypeptide chain (Krigbaum and Hsu, 1975; Damaschun et al., 1991; Damaschun et al., 1993; Kellermayer et al., 1997). The disordered linker region (Schumacher et al., 2002; Beich-Frandsen et al., 2011a; Dimastrogiovanni et al., 2014), was assumed to begin at residue 71 because the first few residues of the CTD tend to pack along the core (Arluison et al., 2004). The last five residues of the CTD constitute the acidic tip. The local concentration of the acidic tip on a single CTD was calculated for full-length Hfq (Hfq102) and for Hfq-sCTD:

$$
C=\frac{\frac{1}{V_{tail}-V_{core}}}{N_{A}}.
$$

In which C is the concentration of the acidic tip, Vtail is the total volume the acidic tip can access around the center of mass of a single Hfq hexamer, Vcore is the inaccessible volume of the Hfq core, and NA is Avogadro’s number. Vtail is estimated as a sphere with radius of 105 Å for Hfq102, and a radius of 70 Å for Hfq-sCTD. Vcore is estimated as a cylinder with radius 31.5 Å and height 25 Å (Sauter et al., 2003).

### Hfq purification

Untagged E. coli Hfq102, Hfq-sCTD, Hfq65, Hfq65-Q35A, Hfq65-K47A, Hfq65-R19D and Hfq65-R16A were over-expressed in E. coli BL21(DE3)Δhfq::cat-sacB cells grown in 1 L LB-Miller media (10 g/L Tryptone, 10 g/L NaCl, 5 g/L yeast extract) supplemented with 100 µg/mL ampicillin. Plasmids for over-expression of mutant Hfq proteins were created by site-directed mutagenesis of pET21b-Hfq (Zhang et al., 2002). The purification method has been previously described (Santiago-Frangos et al., 2016). In brief, resuspended cell lysates of Hfq102 and Hfq-sCTD variants were clarified by heat denaturation and untagged Hfq was purified via Ni2+-affinity. Lysates of Hfq65 variants were further clarified by ammonium sulfate precipitation after heat treatment, and the protein purified by hydrophobic interaction chromatography. Finally, all Hfq variants were purified by cation-exchange chromatography to remove nucleic acids (Figure 2—figure supplement 1).

### Nucleic acid preparation

The sequences of RNA and DNA substrates are listed in Table 2. Synthetic Target RNAs, molecular beacon (Panja and Woodson, 2012a), A18, D16-FAM and R16 have been previously described (Hopkins et al., 2009). minRCRB RNA (IDT) was reduced with TCEP (tris(2-carboxyethyl)phosphine) and purified by denaturing PAGE before labeling with Cy3-maleimide (GE Healthcare), as previously described (Santiago-Frangos et al., 2016). The extent of labeling was estimated from the absorbance at 260 and 552 nm. The sRNAs ChiX, RprA, DsrA and RyhB and mRNA chiP were transcribed in vitro as previously described (Lease and Woodson, 2004). pUC19 plasmid (NEB) for Hfq binding assays was isolated from transformed DH5α cells (NEB) using Plasmid Maxi kit (QIAGEN) and digested with EcoRI (NEB) and HindIII (NEB) and purified by phenol-chloroform extraction followed by ethanol precipitation.

### CTD binding and displacement

To measure binding of CTD-FITC, CTDpos-FITC, or BsCTD-FITC peptides (Table 2) to Hfq65 or Hfq65 mutants, the fluorescence polarization of FITC-labeled peptide was measured 3 min after the addition of 0–33.3 µM Hfq65. Anisotropy measurements were normalized to the average anisotropy in the absence of Hfq. Samples were prepared in a 100 µL cuvette containing 100 µL 50 mM Tris·HCl pH 7.5, 45 nM CTD-FITC or CTDpos-FITC, at 30°C. Fluorescence polarization with grating correction factor was measured using a Horiba Fluorolog-3 (L-format) with single excitation and emission monochromators at 495 nm and 515 nm respectively (5 nm slit widths). Titrations were performed in duplicate and the curves were fit to a single-site binding isotherm:

$$
y=\frac{K_{a}*x}{1+(K_{a}*x)},
$$

in which Ka is the association constant.

Although residue K3 in the NTD was observed to bind the acidic CTD in silico, the contribution of K3 to in vitro binding could not be determined because neither Hfq65-K3S nor Hfq65-K3Q formed stable proteins.

To measure the displacement of CTD-FITC from Hfq65·CTD-FITC complexes by nucleic acids, samples were prepared in a 100 µL cuvette containing 1 µM CTD-FITC and 1.67 µM Hfq65 hexamer so that roughly 50% of CTD-FITC peptides were bound at the start of the experiment. The polarization of CTD-FITC was measured 3 min after the addition of increasing amounts of RNA or DNA as above. Competition curves were fit to:

$$
y=\frac{minY+(maxY-minY)}{1+\frac{x}{IC_{50}}^{n}},
$$

where minY and maxY are the minimum and maximum anisotropy values measured, and IC50 is the concentration of nucleic acid which displaced 50% of the bound CTD-FITC from Hfq65.

### RNA binding and annealing

Binding constants for D16-FAM or minRCRB-Cy3 (5 nM) were measured in TNK buffer (10 mM Tris·HCl, pH 7.5, 50 mM NaCl, 50 mM KCl) at 30°C by FAM fluorescence anisotropy as described before (Hopkins et al., 2009). To measure the affinity of Hfq for D16-FAM·R16 dsRNA complex, 50 nM of both RNAs were mixed and allowed to equilibrate at 30°C for 10 min before titration with Hfq. Annealing kinetics of molecular beacon (50 nM) to either Target or Target-A18 RNA (100 nM) by 0–200 nM Hfq hexamer, in 1X TNK (10 mM Tris·HCl pH 7.5, 50 mM NaCl, 50 mM KCl) buffer at 30°C was measured by stopped-flow fluorescence spectroscopy as described previously (Soper et al., 2011; Panja and Woodson, 2012b). Annealing progress curves were fit to single or double-exponential rate equations.

### Anisotropy time-course

To measure RNA binding and release from unlabeled Hfq102, Hfq-sCTD and Hfq65 by anisotropy, the polarization of D16-FAM was recorded every 20 s for ≥ 3 min after each addition, as previously described (Santiago-Frangos et al., 2016). Samples were prepared in a 500 µL cuvette containing 50 nM D16-FAM in TNK buffer at 30°C, with additions of 50 nM Hfq102, 50 nM Hfq-sCTD, or 50 nM Hfq65 (binding phase), followed by 50 nM R16 RNA (annealing and release phase), and finally 400 nM of the ssDNA competitor, DNA2 (stimulated release phase). RNA binding and release experiments were done in triplicate for each Hfq variant. The molar fractions of released dsRNA product D16-FAM·R16 (χdr), remaining ternary complex D16-FAM·Hfq·R16 (χhdr) and binary complex Hfq·D16-FAM (χhd) at the end of the ‘annealing and release phase’ of the experiment were calculated from

$$
r_{AP}=χ_{dr}*r_{Mdr}+χ_{hdr}*r_{Mhdr}+χ_{hd}*r_{Mhd},
$$

where rAP is the anisotropy measured at the end of the ‘annealing and release’ phase in the above annealing experiments, rMdr is the average anisotropy of D16-FAM·R16 complex during the ‘stimulated release’ phase that is indistinguishable from its anisotropy without Hfq, rMhdr is the maximum anisotropy of Hfq·D16-FAM·R16 complex from equilibrium binding experiments, and rMhd is the maximum anisotropy of Hfq·D16-FAM complex from equilibrium binding experiments. Using the conservation of mass, χdr + χhdr + χhd=1, and the relative Kd values for Hfq binding to D16Fl and D16Fl·R16, χhd=Krel * χhdr, yields an expression for the molar fraction of ternary complex:

$$
χ_{hdr}=\frac{(r_{AP}-r_{Mdr})}{r_{Mdr}*1+K_{drel}+r_{Mhdr}+(r_{hd}*K_{drel})}
$$

### Hfq–plasmid DNA binding assays

Samples (10 µL) containing linear pUC19 (0.145 nmol bp), 0–3.333 µM Hfq hexamer, in 40 mM Tris-HCl pH 7.5, 0.14 mM EDTA, 35 mM NH4Cl, 3.7% (v/v) glycerol, 0.05% (w/v) bromophenol blue were incubated at 25°C for 30 min. 2 µL of each reaction was loaded into a sample well of a 15 × 8 cm agarose gel (1.5% (w/v) Seakem LE agarose (Lonza) in 1X TAE (40 mM Tris, 20 mM acetate, 1 mM EDTA, pH 8.0). Electrophoresis was carried out in the cold room (4°C) at 4 V/cm for 6.5 hr. Hfq was dissociated from the bound complexes by soaking agarose gels in 150 mL TBE (89 mM Tris, 89 mM borate, 2 mM EDTA, pH 8.3) and 1 M NaCl, for 30 min at 25°C, at 85 rpm. The gels were washed twice with 150 mL TBE for 10 min, stained with 1X SYBR Gold (Invitrogen) in 150 mL TBE for 45 min, and washed twice with 150 mL TBE for 10 min before imaging on a Typhoon 9410 (GE Healthcare) via excitation at 488 nm and using a 555 nm bandpass 30 emission filter. The fluorescence intensity was measured on a line from the bottom edge of the well through the middle of the lane to visualize the migration of pUC19. For RNA competition experiments, 10 µL samples were prepared as above with 0–2 µM RNA or DNA competitor and 0 or 0.5 µM Hfq102 hexamer.

**Table 2.**
 Sequences of oligomers and sRNAs.


<table>
  <thead>
    <tr>
      <th>RNA or DNA oligomers</th>
      <th>Sequences (5’ to 3’)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Target</td>
      <td>GUGGUCAGUCGAGUGG</td>
    </tr>
    <tr>
      <td>Target-U6</td>
      <td>GUGGUCAGUCGAGUGGUUUUUU</td>
    </tr>
    <tr>
      <td>Target-A18</td>
      <td>GUGGUCAGUCGAGUGGAAAAAAAAAAAAAAAAAA</td>
    </tr>
    <tr>
      <td>A18</td>
      <td>AAAAAAAAAAAAAAAAAA</td>
    </tr>
    <tr>
      <td>R16</td>
      <td>GCACUUAAAAAAUUCG</td>
    </tr>
    <tr>
      <td>Molecular beacon</td>
      <td>FAM-GGUCCCCCACUCGACUCACCACCGGACC-DABCYL</td>
    </tr>
    <tr>
      <td>D16-FAM</td>
      <td>FAM-CGAAUUUUUUAAGUGC</td>
    </tr>
    <tr>
      <td>minRCRB</td>
      <td>Thiol-C6-CUUCCGUCCAUUUCGGACG</td>
    </tr>
    <tr>
      <td>DNA1</td>
      <td>TATCCGTATGACGTTCCGGACTATGCGGCTAAGGGGCAATCTTTAC</td>
    </tr>
    <tr>
      <td>DNA2</td>
      <td>TTTTTCAAACTGCGGATGAGACCACATATGTATATCTCCTTCTTAAAGTTAAAC</td>
    </tr>
    <tr>
      <td>DNA2c</td>
      <td>CAAATTGAAATTCTTCCTCTATATGTATACACCAGAGTAGGCGTCAAACTTTTT</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Parameters used to calculate molar fractions of D16-FAM complexes.Values are the mean of at least two independent experiments determined by fluorescence anisotropy. A further description of the parameters and their usage is provided in the Methods.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Anisotropy</th>
      <th>Complex/complexes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rMdr</td>
      <td>0.0400</td>
      <td>[D16-FAM·R16]</td>
    </tr>
    <tr>
      <td>Hfq102 rMhdr</td>
      <td>0.2227</td>
      <td>[Hfq102·D16-FAM·R16]</td>
    </tr>
    <tr>
      <td>Hfq-sCTD rMhdr</td>
      <td>0.2203</td>
      <td>[HfqsCTD·D16-FAM·R16]</td>
    </tr>
    <tr>
      <td>Hfq65 rMhdr</td>
      <td>0.2161</td>
      <td>[Hfq65·D16-FAM·R16]</td>
    </tr>
    <tr>
      <td>Hfq102 rAP</td>
      <td>0.0732</td>
      <td>[Hfq102·D16-FAM·R16] + [D16-FAM·R16] + [Hfq102·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq-sCTD rAP</td>
      <td>0.0663</td>
      <td>[Hfq-sCTD·D16-FAM·R16] + [D16-FAM·R16] + [Hfq-sCTD·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq65 rAP</td>
      <td>0.1099</td>
      <td>[Hfq65·D16-FAM·R16] + [D16-FAM·R16] + [Hfq65·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq102 rMhd</td>
      <td>0.2195</td>
      <td>[Hfq102·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq-sCTD rMhd</td>
      <td>0.1985</td>
      <td>[Hfq-sCTD·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq65 rMhd</td>
      <td>0.1935</td>
      <td>[Hfq65·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq102 rhd</td>
      <td>0.1332</td>
      <td>[Hfq102·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq-sCTD rhd</td>
      <td>0.1353</td>
      <td>[Hfq-sCTD·D16-FAM]</td>
    </tr>
    <tr>
      <td>Hfq65 rhd</td>
      <td>0.0969</td>
      <td>[Hfq65·D16-FAM]</td>
    </tr>
  </tbody>
</table>
