# Mutational scanning reveals the determinants of protein insertion and association energetics in the plasma membrane

## Authors

- Assaf Elazar<sup>1</sup>
- Jonathan Weinstein<sup>1</sup>
- Ido Biran<sup>1</sup>
- Yearit Fridman<sup>1</sup>
- Eitan Bibi<sup>1</sup>
- Sarel Jacob Fleishman<sup>1</sup> ([ORCID: 0000-0002-6831-3770](https://orcid.org/0000-0002-6831-3770)) †

### Affiliations

1. Department of Biomolecular Sciences Weizmann Institute of Science Rehovot Israel

† Corresponding author

## Abstract

10.7554/eLife.12125.001 Insertion of helix-forming segments into the membrane and their association determines the structure, function, and expression levels of all plasma membrane proteins. However, systematic and reliable quantification of membrane-protein energetics has been challenging. We developed a deep mutational scanning method to monitor the effects of hundreds of point mutations on helix insertion and self-association within the bacterial inner membrane. The assay quantifies insertion energetics for all natural amino acids at 27 positions across the membrane, revealing that the hydrophobicity of biological membranes is significantly higher than appreciated. We further quantitate the contributions to membrane-protein insertion from positively charged residues at the cytoplasm-membrane interface and reveal large and unanticipated differences among these residues. Finally, we derive comprehensive mutational landscapes in the membrane domains of Glycophorin A and the ErbB2 oncogene, and find that insertion and self-association are strongly coupled in receptor homodimers. DOI: http://dx.doi.org/10.7554/eLife.12125.001

## Introduction

The past four decades have seen persistent efforts to decipher the contributions to membrane-protein energetics (Reynolds et al., 1974; Cymer et al., 2015). Membrane-protein folding can be conceptually divided into two thermodynamic stages (Popot and Engelman, 1990; Cymer et al., 2015), each of which affects membrane-protein structure, function, and expression levels: the insertion into the membrane of transmembrane segments as α helices, and their association to form helix bundles (Ben-Tal et al., 1996; Heinrich and Rapoport, 2003; Moll and Thompson, 1994; White and Wimley, 1999; Popot and Engelman, 1990). While significant progress has been made in structure prediction, design, and engineering of soluble proteins (Fleishman and Baker, 2012), important but fewer successes were reported in design of membrane proteins (Joh et al., 2014; Li et al., 2004), largely owing to the complexity of the plasma membrane and the lack of systematic and accurate measurements of membrane-protein energetics (Cymer et al., 2015).

Recently, experimental systems that offer a realistic model for biological membranes have advanced. von Heijne and co-workers quantitated the partitioning of engineered peptides fused to the bacterial transmembrane protein, leader peptidase (Lep), between membrane-inserted and translocated states, and highlighted the importance of interactions between the translocon and the nascent polypeptide chain in determining partitioning (Hessa et al., 2007; Öjemalm et al., 2013). The insertion energetics obtained from this assay, however, were significantly lower than expected from previous theoretical and experimental studies; for instance, the apparent atomic-solvation parameter, which quantifies the free-energy contribution from the partitioning of hydrophobic surfaces to the membrane core, was only 10 cal/mol/Å2 according to the Lep measurements (Ojemalm et al., 2011), compared to ~30 cal/mol/Å2 from previous analyses (Andrew Karplus, 1997; Vajda et al., 1995). Additionally, the magnitude of the insertion free energies for individual amino acids were substantially lower according to the Lep system (Hessa et al., 2007; Ojemalm et al., 2011; Öjemalm et al., 2013) compared to other studies (Moon and Fleming, 2011; Shental-Bechor et al., 2006). These discrepancies led to suggestions that the Lep measurements were 'compressed' relative to others due to interactions between the engineered protein and other membrane constituents (Johansson and Lindahl, 2009; Shental-Bechor et al., 2006).

Membrane-protein energetics are governed not only by the insertion but also by the association of helices into bundles. A significant body of work has shown that association is driven by packing interactions and short sequence motifs comprising small-xxx-small residues, where small is any of the small polar residues (Ser, Gly, or Ala) and x is any residue (Russ and Engelman, 2000; Senes et al., 2004; Melnyk et al., 2004). However, while it is recognized that insertion and association both play roles in protein energetics (Duong et al., 2007; Finger et al., 2006; Moll and Thompson, 1994; Ben-Tal et al., 1996; Heinrich and Rapoport, 2003; Popot and Engelman, 1990), the interplay between these two aspects has not been subjected to systematic experimental analysis. Given the remaining open questions on membrane-protein and protein-protein interactions within the membrane, we established a high-throughput assay to shed light on both factors and their coupling in a systematic and unbiased way within the bacterial plasma membrane.

## Results

## dsTβL: a high-throughput assay for measuring membrane-protein energetics

To overcome gaps in our understanding of membrane-protein energetics, we adapted the TOXCAT-β−lactamase (TβL) screen (

![Figure 1.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig1-v3.jpg)

**Figure 1.:** (a) The TβL genetic construct fuses a membrane segment to two antibiotic selection markers: β-lactamase and ToxR, which report on insertion and self-association, respectively. (b) Libraries encoding every point mutation of a membrane segment are plated on selective and non-selective medium. Following overnight growth, the libraries are extracted and DNA segments, which encode the membrane domain, are subjected to deep-sequencing analysis.DOI: http://dx.doi.org/10.7554/eLife.12125.00310.7554/eLife.12125.004Figure 1—source data 1.The deep-sequencing analysis software (Babraham Institute, Cambridge, UK) provides a quality control assessment, which is high (green) throughout the membrane span (marked by red lines).DOI: http://dx.doi.org/10.7554/eLife.12125.00410.7554/eLife.12125.005Figure 1—source data 2.Amino acid positions and substitutions are represented in rows and columns, respectively. (Top) spectinomycin selection (reference) counts. (Bottom) spectinomycin and ampicillin selection.DOI: http://dx.doi.org/10.7554/eLife.12125.005

Previous studies based on ToxR activity measured the effects of mutations using colony growth and enzyme-linked immunosorbant assay (ELISA), which do not allow high-throughput analysis (Mendrola et al., 2002; Langosch et al., 1996; Lis and Blumenthal, 2006; Russ and Engelman, 2000; Melnyk et al., 2004). Here, instead, we subject libraries encoding every amino acid substitution in the membrane domain to selection on agar plates containing either ampicillin alone or ampicillin and chloramphenicol to monitor insertion and self-association, respectively (Figure 1b); the same bacterial population is also plated on non-selective agar and serves as a reference to control for clonal-representation biases. Following overnight growth, the bacteria in each plate are pooled, plasmids encoding the TβL construct are extracted from each pool, and the variable gene segment, which encodes the membrane span, is amplified by PCR. The three resulting DNA samples are subjected to deep sequencing, which reports the relative frequency of each mutant in the selected and reference populations (Boucher et al., 2014) (see equation 1 in Materials and methods). If the cytoplasmic protein fraction were perfectly constant among different mutants, the measured population frequencies could be interpreted as the relative propensities of each mutant to insert into the membrane or to self-associate in the membrane. This condition is unlikely to hold for all mutants; still, the agreement reported below with multiple lines of biophysical evidence on purified proteins suggests that the population frequencies provide a reasonable measure for changes in membrane-insertion and self-association partitioning. Hence, if we treat the population frequencies as if the mutants’ partitioning between cytosolic, membrane-inserted, and self-associated fractions were under thermodynamic control, following the Boltzmann equation we can derive, at each position i in the membrane span, apparent free energy changes for insertion or self-association due to the substitution from wild type to amino acid aa, ∆∆Gaa,iapp (see equations 2–3 in Materials and methods). Although confounding factors, such as nonspecific interactions between the inserted segment and other bacterial membrane proteins, may affect the readout from the experiment, insertion and self-association are likely to dominate, since every mutant in this library differs from the wild type by only one amino acid; furthermore, all mutants are subjected to identical selection conditions, including temperature and antibiotic, thereby minimizing experimental noise (Mackenzie and Fleming, 2008).

## Systematic per-position contributions to membrane-protein insertion

We used dsTβL to comprehensively map the sequence determinants of membrane insertion in a single-pass membrane segment (

![Figure 2.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig2-v3.jpg)

**Figure 2.:** (a) Each tile reports the apparent change in free energy  relative to wild type for every CLS point mutant (see ∆∆Ginsertionappequation 3 in Materials and methods). Gray tiles mark substitutions that were eliminated from the analysis due to low counts (<100) in the reference population. (b) Per-position insertion profiles for each amino acid residue. (c) Comparison of dsTβL insertion results at the plasma membrane mid-plane (Z = 0) with values from the Moon scale (Moon and Fleming, 2011). (d) The apparent atomic-solvation parameter is the slope of the linear regression of  and computed change in solvent-accessible surface area (SASA) due to each mutation (slope = -37 cal/mol/Å∆∆Ginsertionapp2, r2 = 0.48, p<0.0001) (see Materials and methods). (inset) Inferring the atomic-solvation parameter from the relationship of  at ∆∆GinsertionappZ = 0 for aliphatic residues and their change in SASA computed on a model poly-Ala α helix (slope=-32 cal/mol/Å2, p = 0.002). CLS, C-terminal portion of human L-SelectinDOI: http://dx.doi.org/10.7554/eLife.12125.006

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** By plating wild-type human CLS (a) and the library encoding every single-site mutation in its putative membrane span (b) on agar containing different antibiotic markers (spectinomycin on the left; ampicillin in the middle; and chloramphenicol on the right), we show that human CLS inserts into the membrane (ampicillin marker, middle plate) but does not self associate (Srinivasan et al., 2011) (right plate). Supplementary file 2 lists antibiotic concentrations. CLS, C-terminal portion of human L-SelectinDOI: http://dx.doi.org/10.7554/eLife.12125.007

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** 10 single-point substitutions at the membrane-spanning segment’s amino terminus and at its core were grown overnight in non-selective medium, normalized to the same density, and plated in serial dilutions on agar containing 400 μg/ml ampicillin to estimate relative viability.DOI: http://dx.doi.org/10.7554/eLife.12125.008

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** Cells harboring the wild-type construct and point mutations were fractionated by ultra-centrifugation. Whole-cell extract and pelleted membrane fractions are shown with anti-β-lactamase antibody. The band intensity was analyzed by densitometry and normalized to wild type and displayed as log2 fold change.DOI: http://dx.doi.org/10.7554/eLife.12125.009

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig2-figsupp4-v3.jpg)

**Figure 2—figure supplement 4.:** Comparing the membrane mid-plane insertion energy (parameter c in Supplementary file 1 with corresponding values from previously published hydrophobicity scales (Wimley et al., 1996; Kyte and Doolittle, 1982; Kessel and Ben-Tal, 2002; Hessa et al., 2007; Moon and Fleming, 2011). Black points represent aliphatic amino acids, blue represent polar amino acids, orange aromatic amino acids. The aliphatic insertion data in dsTβL and the Hessa scale (Hessa et al., 2007) and Moon scale (Moon and Fleming, 2011) are highly correlated (r2 = 0.79 and r2 = 0.90, respectively). The slope of the correlation line for the aliphatics is close to 1 for the Moon scale, whereas it is 0.26 for the Hessa scale, reflecting a roughly four-fold lower change in hydrophobicity upon membrane insertion in the Hessa et al. (2007) assays compared to the dsTβL assay.DOI: http://dx.doi.org/10.7554/eLife.12125.010

We next computed the apparent free-energy change of each substitution across the membrane relative to a substitution to Ala, and at each position i computed the running average over five neighboring positions [i-2…i+2] (Figure 2b; Supplementary file 1). The resulting profiles describe the energetics of inserting each of the twenty amino acids relative to Ala at each position across the bacterial plasma membrane (Figure 2b). Although the location of the membrane mid-plane (Z = 0) could not be determined unambiguously in this assay, we estimated it by aligning the hydrophobic residues’ profiles (Leu, Ile, Met, and Phe), thereby locating the profiles' troughs and the presumed membrane mid-plane at CLS position Ala311.

The small and polar amino acids, Ser, Thr, and Cys have shallow, nearly neutral profiles, ranging from −0.1 to +0.8 kcal/mol. By contrast, the helix-distorting amino acids, Gly and Pro, which expose the polar protein backbone to the hydrophobic membrane environment, have a high disruptive profile, which peaks (~2 kcal/mol) at the membrane mid-plane, emphasizing the strong unfavorable impact of exposing the polar protein backbone to the membrane environment. The large polar (Asn, His, and Gln) and charged residues (Asp, Glu, Lys, and Arg) are all highly disruptive in the membrane mid-plane. We note that the energetic penalties for Asp, Asn, His, Gln, Glu, and Lys cannot be determined precisely from the dsTβL assay, since the number of reads for substitutions to these residues at the membrane mid-plane in the selected population is nearly 0, reflecting exceedingly large negative-selection pressures (Figure 1; Supplementary file 2).

At the membrane mid-plane, the hydrophobic residues, Val, Ile, Leu, Met, and Phe, show the expected troughs, which are shallower for the small amino acid Val (approximately −0.5 kcal/mol) than for the large amino acids (<−1.5 kcal/mol). We compared the dsTβL values for hydrophobic residues in the membrane mid-plane to values from five hydrophobicity scales (Figure 2—figure supplement 4). dsTβL fits well to the Moon scale (Figure 2c, r2 = 0.90, with a slope close to 1), which similar to dsTβL measures substitution effects in a bacterial membrane – albeit the outer membrane (Moon and Fleming, 2011). The correspondence between dsTβL, which is based on in vivo measurement of membrane integration in a bacterial population, with biophysical assays on purified proteins, partly confirms the use of dsTβL for studying membrane-protein energetics.

The dsTβL profile for Trp is similar to the profiles of the aliphatic residues, whereas Tyr makes a nearly neutral contribution to insertion in the membrane core. These profiles diverge from statistical inferences from membrane-protein structures and partitioning experiments, which show that Tyr and Trp preferentially line the membrane-water interface (Ulmschneider et al., 2005; Schramm et al., 2012; Senes et al., 2007; Nakashima and Nishikawa, 1992; Yau et al., 1998). Further experimental analysis of the role of aromatic residues in membrane-protein stability is warranted, and one possible explanation for these differences is that in the dsTβL assay aromatic residues on the membrane-spanning segment lack neighboring aromatic residues with which to form stabilizing stacking interactions; indeed, experimental stability measurements have shown that stacking makes a significant contribution to the net stabilization provided by aromatic residues in membrane proteins (Hong et al., 2007, 2013).

## Hydrophobicity in the membrane core is similar to that of organic solvents and protein cores

Recently, controversy has surrounded the question of how hydrophobic are biological membranes (Johansson and Lindahl, 2009). On the one hand, theoretical considerations and values inferred from hydrocarbons in solution suggested that the free energy contribution due to inserting aliphatic groups into the membrane, or the atomic-solvation parameter, is ~30 ± 5 cal/mol/Å2 of nonpolar surface area (Vajda et al., 1995; Andrew Karplus, 1997); on the other hand, the Lep measurements suggested values of only 10 cal/mol/Å2 (Ojemalm et al., 2011). We analyzed dsTβL data for 39 substitutions from one aliphatic residue (Ala, Val, Ile, Leu, and Met) to another at the core of the membrane (−9 Å<Z<13 Å) and inferred an apparent atomic-solvation parameter of 37 ± 6 cal/mol/Å2 (Figure 2d). We additionally derived an atomic-solvation parameter of 32 ± 4 cal/mol/Å2 by analyzing the apparent insertion free energies at the membrane mid-plane (∆∆Gz=0app) for each of the aliphatic residues (Figure 2d, inset). The values we infer for the atomic-solvation parameter are therefore in fair agreement with values for protein cores and hydrocarbons in aqueous solution (Vajda et al., 1995), and 3–4 times larger than the value inferred from the Lep system (Ojemalm et al., 2011). We further note that while the ranking of apparent insertion free energies of aliphatic amino acids in dsTβL and Lep (Hessa et al., 2007) is similar (r2 = 0.79, Figure 2—figure supplement 4), the magnitude of the insertion free-energy changes is nearly four times greater according to dsTβL. We conclude that our results support the view that the hydrophobicity of the plasma membrane core is similar to that of hydrocarbons and much higher than measured in the Lep system.

## Large differences and strong asymmetries in insertion of positively charged residues

A hallmark of plasma membrane proteins is the charge asymmetry known as the ‘positive-inside’ rule, according to which the cytoplasmic-facing side of the protein is much more positively charged than the periplasmic or extracellular-facing side (von Heijne, 1989). This asymmetry has been used to successfully predict the orientation of membrane proteins (von Heijne, 1989), but experimental quantification of the energetics of this asymmetry met with difficulty; previous studies measured only a small energy difference (-0.5 kcal/mol) between inserting Arg and Lys in the cytoplasmic relative to the extracellular-facing side of the membrane and no asymmetry for His (Lerch-Bader et al., 2008; Öjemalm et al., 2013). A striking feature of the dsTβL profiles, by contrast, is that they show clear and large asymmetries for Arg, Lys, and His, in agreement with the ‘positive-inside’ rule (Figure 2b). The three profiles, however, are not identical: whereas Lys and Arg are favored by 2 kcal/mol near the cytoplasm compared to near the periplasm, the titratable amino acid His shows a more modest asymmetry of 1 kcal/mol; moreover, of these three amino acids, only Arg stabilizes the segment near the cytosol, whereas Lys and His are nearly neutral at the cytosol-membrane interface. This difference between Arg and Lys, which has not been noted until now, may be due to charge delocalization in the Arg sidechain and Arg’s ability to form more hydrogen bonds with lipid phosphate headgroups.

We compared the relative propensity of each of the 20 amino acids at each position across the membrane (

![Figure 3.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig3-v3.jpg)

**Figure 3.:** (a) The relative frequencies of each amino acid within the membrane (see equation 4 in Materials and methods) in sequence-logo format; the height of each letter corresponds to the amino acid’s propensity.DOI: http://dx.doi.org/10.7554/eLife.12125.011

With the accumulation of membrane-protein molecular structures, it has become possible to derive knowledge-based potentials for the insertion of amino acids across the membrane from distributions of amino acids observed in structures (

![Figure 4.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig4-v3.jpg)

**Figure 4.:** Equations for the knowledge-based profiles were taken from Ulmschneider et al. (2005), Schramm et al. (2012), and Senes et al. (2007).DOI: http://dx.doi.org/10.7554/eLife.12125.012

## Strong coupling between insertion and self-association in membrane-spanning homodimers

Insertion and association of membrane-spanning helices are thermodynamically coupled (Kessel and Ben-Tal, 2002; Moll and Thompson, 1994; Popot and Engelman, 1990), but except in one study (Duong et al., 2007) these two aspects were assayed separately (Fleming et al., 1997; Finger et al., 2009; Hessa et al., 2007; Mendrola et al., 2002). To test the coupling between insertion and association, we applied dsTβL to two model systems for studying membrane protein self-association: the membrane domains of the human erythrocyte sialoglycoprotein Glycophorin A (GpA) and the ErbB2 oncogene, and compared survival on ampicillin and chloramphenicol to survival on ampicillin alone.

Some of the amino acid positions that mediate self-association in GpA and ErbB2 according to their experimentally determined structures (

![Figure 5.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig5-v3.jpg)

**Figure 5.:** () The mutational landscapes discriminate positions that are involved in self-association (known associating residues are depicted in boldface) from those that do not. (a) Comparison of expression-corrected apparent free energy of insertion for 24 Glycophorin A (GpA) mutants (bDuong et al., 2007) with results from the dsTβL self-association mutation landscapes. () Dimer models that associate through positions that are sensitive to mutation (* in panel a), and do not associate through positions that are insensitive to mutation († in panel a). The models (green) are close to the experimental structures (blue) for Glycophorin A (cMacKenzie et al., 1997) (1.3 Å root mean square deviation) and ErbB2 (Bocharov et al., 2008) (1.9 Å). Another ErbB2 model, which agrees with biochemical and computational evidence (Endres et al., 2013; Arkhipov et al., 2013; Fleishman et al., 2002) but has not been observed in experimental structures, is also suggested.DOI: http://dx.doi.org/10.7554/eLife.12125.013

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** The mutational landscapes comparing survival on chloramphenicol and ampicillin are dominated by insertion effects.Chloramphenicol resistance in the dsTβL assay is expected to correlate with self-association (Lis and Blumenthal, 2006; Russ and Engelman, 1999; Langosch et al., 1996). While mutations at some positions that mediate self-association disrupt viability, the majority of extreme effects observed in the mutational landscapes can be attributed to insertion rather than self-association. For instance, the charged and polar residues are highly disfavored in the membrane core, whereas the large hydrophobic residues, Leu and Phe, are favored in most positions in the membrane core. Figure 5a shows mutational landscapes where the effects of insertion were subtracted.DOI: http://dx.doi.org/10.7554/eLife.12125.014

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/12125/elife-12125-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** In addition to the model structures of Figure 5b modeling constrained by the dsTβL, experimental data produced three models for Glycophorin A and two for ErbB2. Improvements in the RosettaMembrane (Yarov-Yarovoy et al., 2006) energy function would be needed to eliminate these alternative models.DOI: http://dx.doi.org/10.7554/eLife.12125.015

We also tested whether the systematic mutational landscapes generated by dsTβL could be used to provide constraints for structure modeling of receptor membrane domains (Fleishman et al., 2002; Kim et al., 2003; Polyansky et al., 2014). We used the Rosetta biomolecular-modeling software (Das and Baker, 2008; Yarov-Yarovoy et al., 2006) to generate 100,000 structure models of GpA and ErbB2 directly from their sequences, and selected structures that self-associate through positions that are sensitive to mutation according to dsTβL but not through positions that are insensitive to mutation (Figure 5c, Figure 5—figure supplement 2). In both cases, fewer than five models passed the selection criteria and of those, some models were within 2 Å of experimentally determined structures.

## Discussion

Despite progress in measuring protein energetics within biological membranes, significant open questions remained, among them, what is the hydrophobicity at the core of biological membranes; what is the magnitude of the bias for positively charged residues at the cytoplasm surface; and how strong is the coupling between membrane-protein insertion and association energetics? To shed light on these fundamental questions, we established a high-throughput genetic screen and used it to generate systematic mutation landscapes of insertion and self-association in the plasma membrane of live bacteria.

The apparent insertion energies in dsTβL are in line with biophysical stability measurements on outer-membrane proteins (Moon and Fleming, 2011), and the inferred atomic-solvation parameter is close to measurements in model systems and protein cores (Andrew Karplus, 1997; Vajda et al., 1995). Our measurements, however, are three to four times larger than the corresponding ones using the Lep system (Ojemalm et al., 2011; 2013; Hessa et al., 2007). To be sure, we are not the first to note these large differences (Johansson and Lindahl, 2009; Shental-Bechor et al., 2006); yet, we find it significant that our measurements, similar to those in the Lep system, use biological membranes. The observation that the dsTβL insertion measurements for aliphatic side chains have the same ranking but are fourfold larger in magnitude compared to those from Lep (Figure 2—figure supplement 4) may indicate that the Lep system measures only a part of the energy contribution to insertion. While further investigation is needed, we speculate that the reason for the large differences between dsTβL and Lep is that total membrane-protein expression levels were not quantified in the Lep system (Hessa et al., 2007; Ojemalm et al., 2011; 2013).

We note the following two caveats regarding the dsTβL insertion profiles. First, the penalties for most polar residues at the membrane mid-plane are likely to indicate lower bounds on their insertion energies, since the number of clones counted in the deep-sequencing data for these mutants is close to 0 (supplementary data). Second, statistical analyses (Ulmschneider et al., 2005; Schramm et al., 2012; Senes et al., 2007) and experiments (Hessa et al., 2007) demonstrated that the aromatics Tyr and Trp are preferred in the water-membrane interface rather than in the core, although dsTβL shows the reverse (Figure 2b). We suggest that these results reflect the fact that dsTβL is based on a monomeric construct where the aromatics are fully exposed to the membrane environment; however, these uncertainties require further research.

The TOXCAT genetic screen has made essential contributions to our understanding of self-association in the membrane (Lindner and Langosch, 2006; Lis and Blumenthal, 2006; Russ and Engelman, 1999; Finger et al., 2009; Mendrola et al., 2002; Li et al., 2004; Srinivasan et al., 2011﻿Reuven et al., 2012). Some early reports demonstrated that chloramphenicol survival also depends on membrane-protein expression levels (Russ and Engelman, 1999; Duong et al., 2007). Our results strongly support this view and show that expression levels are a dominant factor in chloramphenicol survival. This dominance is perhaps not surprising in retrospect, given that a mutation’s effects on monomer concentrations are counted twice in computing its effects on homodimer concentrations, and therefore on chloramphenicol viability (see equation (5) in Materials and methods). A key contribution of unbiased and systematic assays, such as dsTβL, is that they clarify such trends unambiguously. Furthermore, the dsTβL insertion profiles derived from the monomeric CLS provide a self-consistent way to factor out the contributions from insertion energetics in future assays on membrane-protein association or function in unrelated membrane proteins, thereby eschewing the need to measure the expression levels of individual mutants.

Deep mutational scanning has made important inroads to analysis and optimization of diverse protein systems (Whitehead et al., 2012; Fowler and Fields, 2014; Boucher et al., 2014). The main strengths of deep mutational scanning are the ability to measure the effects of all point mutations without bias and that all mutants experience strictly equal experimental conditions, thereby limiting experimental noise. The structural simplicity of the model systems tested here, consisting of a single α helix or of helix homodimers, plays a further role in the ability to accurately infer energetics. Combined with structural modeling, the assay can provide essential information both on association energetics and the molecular architecture of membrane receptors. More generally the data on protein-membrane and protein-protein energetics obtained from dsTβL will be used to improve models of membrane-protein energetics and to design, screen, and engineer high-expression mutants of specific membrane proteins (Fleishman and Baker, 2012; Joh et al., 2014).

## Materials and methods

## Plasmids and bacterial strains

The p-Mal plasmid was generously provided by the Mark Lemmon laboratory. We replaced the maltose-binding protein domain at the open-reading frame carboxy-terminus with β-lactamase (Lis and Blumenthal, 2006). The restriction sites in multiple-cloning site 1 were changed to XhoI and SpeI. The p-Mal plasmid contains a gene for spectinomycin resistance, which is constitutively expressed, providing selection pressure for transformation. The open-reading frame encompassing the TβL construct is also constitutively expressed and is under the control of the weak ToxR promoter.

The DNA coding sequence for the transmembrane constructs used in the paper:

>human CLS

CCGCTGTTCATCCCGGTTGCAGTTATGGTTACCGCTTTTAGTGGATTGGCGTTTATCATCTGGCTGGCT (amino acid sequence: PLFIPVAVMVTAFSGLAFIIWLA)

>Glycophorin A

CTCATTATTTTTGGGGTGATGGCTGGTGTTATTGGAACGATCCTGATC (amino acid sequence: LIIFGVMAGVIGTILI)

>ErbB2

CTGACGTCTATCATCTCTGCGGTGGTTGGCATTCTGCTGGTCGTGGTCTTGGGCGTGGTCTTTGGCATCCTGATC (amino acid sequence: LTSIISAVVGILLVVVLGVVFGILI)

The CLS construct was deposited in the AddGene repository [pMAL_dstβL-(Plasmid #73805)].

All experiments were conducted using the high-transformation efficiency E. cloni cells (Lucigen Corporation, Middleton, WI).

## Library construction

Customized MatLab 8.0 (MathWorks, Nattick, Massachusetts) scripts for generating primers were written (supplementary files) to generate forward and reverse DNA oligos of lengths 40–85 base pairs, where the central codon is replaced by the degenerate codon NNS, where N is any of the four nucleotides (ATGC) and S is G or C, encoding all possible natural amino acids. Resulting primers were ordered from Sigma (Sigma-Aldrich, Rehovot, Israel). For example, to replace the central 302nd codon of human CLS with an NNS codon, the following two primers were ordered:

>forward

GCTGTTCATCCCGGTTGCAGTTNNSTGGTTACCGCTTTTAGTGGATTG

>reverse

CAATCCACTAAAAGCGGTAACCASNNAACTGCAACCGGGATGAACAGC

Each pair of oligos was then cloned into the wild type by restriction-free (RF) cloning (van den Ent and Löwe, 2006).

## Transformation, growth, plating, and harvesting

The resulting plasmids from the library-construction step above were electroporated into E. cloni and plated on agar plates containing 50 μg/ml spectinomycin. Plasmids for each position were transformed and plated separately and positions with fewer than 200 colonies were retransformed. All positions were then pooled and used to inoculate 10 ml of Luria Broth medium (LB) with 50 μg/ml spectinomycin and grown in a shaker at 200 rpm and 37°C over-night, diluted 1:1000 and grown to OD = 0.2–0.4. The libraries were then diluted to OD = 0.1 and 200 μl of the resulting cultures were plated at different dilutions (1:1, 1:10, 1:100, 1:1000) on large 12-cm petri dishes containing spectinomycin, ampicillin alone, or ampicillin and chloramphenicol. After overnight incubation at 37°C, p-Mal plasmids were extracted from the resulting colonies using a miniprep kit (Qiagen, Valencia, California).

## Determining concentrations of antibiotics that result in maximal dynamic range

Every wild-type membrane-spanning segment exhibits different sensitivity to chloramphenicol and ampicillin. To determine the concentrations that are most likely to provide maximal dynamic range, we started by cloning mutants that are predicted to reduce insertion of the membrane-spanning segment or its self association (Mendrola et al., 2002). Results are represented in Supplementary file 1. We next titrated the wild-type construct as well as the mutant on plates with varying concentrations of antibiotic to find the concentration that shows the largest difference in viability between the wild type and the compromising mutants. Supplementary file 2 provides the ampicillin and chloramphenicol concentrations used in each of the experiments reported in the paper.

## Deep sequencing

## DNA preparation

In order to connect the adaptors for deep sequencing, the membrane-spanning segments were amplified from the p-Mal plasmids using KAPA Hifi DNA-polymerase (Kapa Biosystems, London, England) using a two-step PCR.

PCR 1:

>forward

CTCTTTCCCTACACGACGCTCTTCCGATCTCTTGGGGAATCGACTCGAG

>reverse

CTGGAGTTCAGACGTGTGCTCTTCCGATCTGTTTAAAGCTGGATTGGCTTGG

1μl of the PCR product was taken to the next PCR step:

>forward

AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGC

>reverse barcode 1

CAAGCAGAAGACGGCATACGAGAT <barcode>GTGACTGGAGTTCAGACGTGTGC

>reverse barcode 2

CAAGCAGAAGACGGCATACGAGAT <barcode>GTGACTGGAGTTCAGACGTGTGC

The DNA samples from each of the populations (unselected; ampicillin-selected; and chloramphenicol and ampicillin selected) were PCR-amplified using DNA barcodes for deep sequencing. The following barcodes were used:

>barcode1

TCGCCAGA

>barcode2

CGAGTTAG

>barcode3

ACATCCTT

>barcode4

GACTATTG

All the primers were ordered as PAGE-purified oligos. The concentration of the PCR product was verified using Qu-bit assay (Life Technologies, Grand Island, New York).

## Deep-sequencing runs

DNA samples were run on an Illumina MiSeq using 150-bp paired-end kits. The quality control for a typical run showed that the membrane-spanning segment was at high-quality (source data) FASTQ sequence files were obtained for each run and customized MatLab 8.0 scripts were written to generate the selection heat maps from the data (scripts are available in supplementary files). Briefly, the script starts by translating the DNA sequence to amino acid sequence; it then eliminates sequences that harbor more than one amino acid mutation relative to wild type; counts each variant in each population; and eliminates variants with fewer than 100 counts in the reference population (to reduce statistical uncertainty). In a typical experiment, at least 70% of the reads passed these quality-control measures.

## Completeness and dynamic range of the deep sequencing results on insertion energetics

The ampicillin selected and the unselected populations of CLS mutants were subjected to deep sequencing analysis yielding more than 4 million reads for each population. Out of 540 possible single-point substitutions, 472 (~87%) mutants were each counted more than 100 times in the reference population; the remaining mutants were eliminated from analysis to reduce uncertainty (gray tiles in Figure 2a). The dsTβL assay has a large dynamic range; for instance, at position 307 in the membrane center, the number of reads in the selected population for Lys, Gln, and Glu is 0, whereas the number of reads for Leu is nearly 110,000, spanning five orders of magnitude.

## Sequencing analysis

To derive the mutational landscapes (Figures 2a and 4a) we compute the frequency pi,j of each mutant relative to wild-type in the selected and reference pools, where i is the position and j is the substitution, relative to wild-type:

(1)pi,j=counti,jcountwild−type

where count is the number of reads for each mutant. The selection coefficients are then computed as the ratio

(2)si,j=(pi,j)selected(pi,j)reference

where selected refers to the selected population (ampicillin in the case of the CLS insertion analysis, and ampicillin plus chloramphenicol in self-association analyses) and reference refers to the reference population (spectinomycin-selection in the case of CLS insertion analysis, and ampicillin in the case of self-association analysis). The resulting si,j values are then transformed to apparent changes in free energy (∆∆Gapp) due to each single-point substitution through the Gibbs free-energy equation:

(3)∆∆Gi,japp=−RTln(si,j)

where R is the gas constant, T is the absolute temperature (310K), and ln is the natural logarithm.

## Polynomial fitting and smoothing of insertion plots

The readout from the insertion selection in dsTβL comprises contributions from the local environment of each position; for example, substitution to a small residue might form a cavity if surrounded by large residues. To reduce such sequence-specific effects, the insertion free-energy values relative to alanine were smoothed using the MatLab smooth function over a window of 5 residues (2 on each side), excluding gray tiles (with insufficient data), and plotted as points in Figure 2b. The points were then fitted using the polynomial fitting function polyfit to yield 4th-order polynomials (Figure 2b lines and Supplementary file 1). Two centrally located polar amino acid positions, CLS positions Ser307 and Gly308, were discarded from the analysis due to their inconsistency with the general trends of the insertion profiles, likely because mutations at these polar positions distort the helix backbone.

## Position-specific amino acids preference

To compute the amino acid preference at each position in the membrane (Figure 2c), we calculated the Boltzmann-weighted probability of every amino acid residue at each position in the membrane-spanning domain of human CLS(Srinivasan et al., 2011) using the following formula (MatLab script in supplement files):

(4)pi, j=e-Eappi,j/RT-Eappi,x/RT               Σxe

where R is the gas constant, T = 310K and Eappi,j are the apparent free energy of transfer of amino acid j at position i relative to alanine (Figure 2b).

## Inferring the atomic-solvation parameter

We generated a model of the CLS membrane domain by threading its sequence on a canonical α helix, and used Rosetta to singly introduce each substitution from one aliphatic identity (Ala, Val, Ile, Met, Leu, and Phe) to another in the membrane core. Amino acid sidechains were combinatorially repacked and the change in solvent-accessible surface area (ΔSASA) was computed. Four additional data points (marked with asterisks, Figure 2d) were extracted from Glycophorin A’s position Ala82, which is located at the membrane center and away from the dimerization interface. To compute the atomic-solvation parameter from the insertion energies of the aliphatics at the membrane mid plane (Figure 2d, inset), we compared the insertion energy at the membrane mid plane for each aliphatic residue ∆∆Gz=0app with computed ΔSASA of a change from that residue to Ala on a canonical poly-Ala α helix.

## Computing the apparent dimerization free-energy change

ToxR activity depends on homodimer concentrations (Langosch et al., 1996; Russ and Engelman, 1999), and homodimer concentrations depend on both monomer insertion into the membrane and self-association strength. The measured effects of every point mutation on self-association (Figure 5—figure supplement 1) therefore comprise contributions from insertion (multiplied by two because the homodimer comprises two mutants) and dimerization (Duong et al., 2007). To isolate the mutation’s effects on self-association (Figure 5a), we subtract from every data point twice the contribution to insertion at the relevant position along the membrane normal.

(5)∆∆Gdimerizationj,xapp=∆∆Gmeasuredj,xapp−2∆∆Ginsertioni,j,xapp

where, i, j, and x are the wild-type identity, mutation, and the position along the membrane normal, respectively, ΔΔGmeasured is the measured change in self-association free energy (see equation (3)), and ∆∆Ginsertion is the free-energy change expected for a mutation from i to j at position x according to the insertion polynomials of Supplementary file 1.

## β –lactamase blot analysis

Cells were grown in 5 ml LB overnight at 37°C. The cells were then diluted at a 1:100 ratio into 50 ml LB and were grown to A600 = 0.6, harvested on ice, washed in TBS buffer, and equal amounts of cells were re-suspended in extraction buffer (50 mM Tris pH 8 [Bio-Lab, Israel], 100 mM NaCl, 5% [w/w] sucrose and 1 mM AEBSF [Sigma-Aldrich]). The cells were then disrupted by three cycles of sonication with Microson XL at 12 watts for 10 s with 60 s intervals. Samples were centrifuged for 15 min at 13,000 rpm in order to discard cell debris, supernatant was ultracentrifuged for 1 hr at 300,000 g using Optima TLX with TLA100.1 rotor in order to sediment membranes to the pellet. The pellet was re-suspended in 100 mM Na(HCO3)2 and incubated for 15 min at 4°C and ultra-centrifuged for 1 hr at 300,000 g. Pellet and extract protein concentration were measured with Lowry protein assay (Peterson, 1977), and equal amounts of protein were loaded on 12.5% Tris-Glycine SDS PAGE gels. Gels were transferred to Protran nitrocellulose membranes (Whatman) and incubated with mouse anti-β-lactamase antibody (Santa Cruz, Dallas) and a horse-radish-peroxidase-fused rabbit anti-mouse secondary antibody, and imaged using SuperSignal West Femto Maximum Sensitivity Substrate (Thermo, Waltham, MA). ECL and the chemiluminescence signal was detected using the ChemiDoc MP System (Bio-Rad). Band densitometry was analyzed with imageJ (Schneider et al., 2012).

## Ab initio modeling using Rosetta

For each membrane segment, we start by generating all-helical backbone-conformation fragments using the Rosetta utility fragment picker (Gront et al., 2011) and construct a C2 symmetry definition file using the Rosetta symmetry utility function (https://www.rosettacommons.org). We then use the Rosetta Fold-and-Dock application (Das et al., 2009), which samples symmetric degrees of freedom for both docking and folding of the homodimer using the RosettaMembrane energy function (Yarov-Yarovoy et al., 2006). Example files and command lines for running fragment picker and fold-and-dock are available in supplementary files.

## Constraining structure models with experimental results

For each position in the membrane-spanning region of the target protein, we assign two labels: likely mediating binding – if at least four substitutions from wild-type disrupted binding by at least 2kcal/mol (* in Figure 5a); and unlikely to mediate binding – if at least four substitutions improved or did not change binding (†). For each of the 20% lowest-energy Rosetta models, we tested whether at least two of the residues that likely mediate binding are within 5 Å of the partner monomer and all positions, which are unlikely to mediate binding, are outside a 4 Å shell. Structures that passed the filter above were clustered using the Rosetta clustering application with default parameters. The clusters were visually inspected and models showing significant kinks were eliminated.
