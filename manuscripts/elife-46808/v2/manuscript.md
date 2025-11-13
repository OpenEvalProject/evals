# Interactions between a subset of substrate side chains and AAA+ motor pore loops determine grip during protein unfolding

## Authors

- Tristan A Bell<sup>1</sup> ([ORCID: 0000-0002-3668-8412](https://orcid.org/0000-0002-3668-8412)) †
- Tania A Baker<sup>1</sup> ([ORCID: 0000-0002-0737-3411](https://orcid.org/0000-0002-0737-3411))
- Robert T Sauer<sup>1</sup> †

### Affiliations

1. Department of Biology Massachusetts Institute of Technology Cambridge United States
2. Howard Hughes Medical Institute, Massachusetts Institute of Technology Cambridge United States

† Corresponding author

## Abstract

Most AAA+ remodeling motors denature proteins by pulling on the peptide termini of folded substrates, but it is not well-understood how motors produce grip when resisting a folded domain. Here, at single amino-acid resolution, we identify the determinants of grip by measuring how substrate tail sequences alter the unfolding activity of the unfoldase-protease ClpXP. The seven amino acids abutting a stable substrate domain are key, with residues 2–6 forming a core that contributes most significantly to grip. ClpX grips large hydrophobic and aromatic side chains strongly and small, polar, or charged side chains weakly. Multiple side chains interact with pore loops synergistically to strengthen grip. In combination with recent structures, our results support a mechanism in which unfolding grip is primarily mediated by non-specific van der Waal’s interactions between core side chains of the substrate tail and a subset of YVG loops at the top of the ClpX axial pore.

## Introduction

Cells maintain homeostasis by balancing protein synthesis and degradation with growth. When nutrients are available, new proteins are constantly synthesized, whereas damaged, misfolded, or unneeded proteins are degraded. Regulated degradation typically requires a protein-unfolding motor of the AAA+ family (ATPases associated with various cellular activities) that associates with a self-compartmentalized protease (e.g., ClpX with ClpP, the 19S regulatory particle with the 20S proteasome) or is genetically tethered to a protease (e.g., Lon, FtsH, Yme1) (Sauer and Baker, 2011; Olivares et al., 2016; Glynn, 2017). When challenged with degrading a folded substrate, AAA+ motors couple ATP hydrolysis to mechanical motion that overcomes the resistance of the folded domain. Despite broad consensus on the overall mechanism of protein unfolding, it is largely unknown how interactions between a AAA+ motor and its substrate produce grip, the ability for the motor to maintain hold of the substrate while applying an unfolding force.

ClpX is a ring-shaped AAA+ homohexamer that functions autonomously in protein remodeling in bacteria and eukaryotic organelles and also associates with ClpP tetradecamers to form the ATP-dependent ClpXP protease (Baker and Sauer, 2012). Substrates are targeted to ClpX or ClpXP by N- or C-terminal peptide tails (also called degradation tags or degrons), which initially bind in the ClpX axial pore. Proteins marked with a sequence-defined degron or post-translational modification can be recruited to the AAA+ protease directly or with assistance from auxiliary adaptors (Sauer and Baker, 2011; Trentini et al., 2016). For example, during rescue of stalled ribosomes in Escherichia coli, the 11-residue ssrA tag is appended to the C-terminus of abortive protein products (Keiler et al., 1996), allowing ClpXP to recognize and degrade the attached protein (Gottesman et al., 1998; Farrell et al., 2005).

The ssrA tag and other degron tails interact with ClpX loops that line the axial pore. A Tyr-Val-Gly (YVG) sequence in the pore-1 loop is critical for substrate binding, unfolding, and translocation (Siddiqui et al., 2004; Martin et al., 2008a; Martin et al., 2008b; Iosefson et al., 2015). Other AAA+ unfolding motors contain related pore-1 loops and mutation of these loops typically abolishes function (Yamada-Inagawa et al., 2003; Schlieker et al., 2004; Hinnerwisch et al., 2005; Park et al., 2005). In several AAA+ unfolding motors, the pore-1 loops adopt a spiral staircase conformation within the pore, which facilitates multivalent interaction with the bound peptide tail (Monroe et al., 2017; Gates et al., 2017; Puchades et al., 2017; de la Peña et al., 2018; Majumder et al., 2019; Dong et al., 2019; White et al., 2018). ATP-dependent conformational changes are thought to draw the tail of a substrate into the pore until a folded domain too large to transit the pore impedes progress. For ClpXP, repeated cycles of ATP hydrolysis are then required to unfold the substrate and to translocate the polypeptide through the pore and into ClpP for degradation (Kenniston et al., 2003; Aubin-Tam et al., 2011; Maillard et al., 2011; Sen et al., 2013; Cordova et al., 2014).

How the amino acids in the bound substrate tail contribute to grip during unfolding remains poorly understood. When degrading unfolded substrates, the rate of substrate translocation through ClpXP is largely insensitive to amino-acid charge, size, or peptide-bond spacing (Barkow et al., 2009). In contrast, when directly abutting a folded domain, sequences rich in glycine can result in failed unfolding by ClpXP or the 26S proteasome, leading to release of partially processed intermediates (Lin and Ghosh, 1996; Levitskaya et al., 1997; Sharipo et al., 2001; Hoyt et al., 2006; Daskalogianni et al., 2008; Too et al., 2013; Kraut, 2013; Vass and Chien, 2013). Abortive unfolding caused by Gly-rich motifs occurs as a result of slower domain unfolding rather than rapid substrate dissociation, suggesting that these motifs bind normally but are gripped poorly during unfolding (Kraut, 2013; Kraut et al., 2012). These results suggest that AAA+ motors struggle to efficiently grip sequences with very small side chains. Alternatively, sequence complexity rather than composition may dictate grip strength (Tian et al., 2005).

Here, we use green fluorescent protein (GFP) reporter substrates to interrogate the contributions of individual amino acids in the peptide tail to grip strength by ClpXP. In degradation assays performed in vivo and in vitro, we observe that substrate grip by ClpX is primarily mediated by interactions with a block of five amino acids, located two to six residues from the native GFP domain. Through systematic mutation, we characterize the ability of each amino acid to promote ClpX grip, and find that aromatic and large hydrophobic residues are gripped well, whereas charged and polar residues impair grip. Finally, we analyze synergistic contributions of multiple residues to unfolding, and show that contacts with more than one side chain lead to stronger grip and faster substrate unfolding. Our results provide unprecedented detail into the mechanism by which AAA+ motors grip terminal substrate tails during protein unfolding.

## Results

### Substrate design and degradation assays

To probe grip during substrate unfolding, we used Aequorea victoria GFP, as its native structure is highly kinetically stable, unfolding is rate limiting for ClpXP degradation of GFP-ssrA, and the pathway of mechanical unfolding of GFP-ssrA by ClpXP is well characterized (Maillard et al., 2011; Kim et al., 2000; Nager et al., 2011). In our substrates, we truncated GFP at Ile-229, the last amino acid that makes extensive native contacts in multiple crystal structures (Ormö et al., 1996; Yang et al., 1996), and added a 12-residue cassette of variable sequence followed by a partial ssrA degron to allow recognition by ClpXP (Figure 1A). Given the length of the axial pore (~35 Å; Glynn et al., 2009), we reasoned that ClpX should only interact with residues within the cassette region during GFP unfolding.

![Figure 1.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig1-v2.jpg)

**Figure 1.:** (A) Starting at the N terminus, substrates contained residues 1–229 of A.victoria GFP (PDB 1GFL, Yang et al., 1996), a cassette with 12 variable residues, and a partial ssrA degron. (B) Method for measuring intracellular degradation of substrates by ClpXΔN/ClpP. (C) Cellular fluorescence depends upon ClpXΔN/ClpP expression and cassette sequence (listed in Table 1). (D) Fraction intracellular degradation for substrates bearing different cassettes. (E) Fits of the substrate dependence of degradation in vitro to a hyperbolic Michaelis-Menten equation. (F) Vmax values for different substrates. In panels, C–F, values represent averages (± S.D.) of three biological replicates.

**Table 1.**
 Degradation of variable-tail substrates in the bacterial cytoplasm.Sequences of all substrate tails tested and the extent of degradation by ClpXΔNP in E. coli after 35 min. For substrates tested in multiple panels, the value presented is from the panel in which they first appear. Values are the average of three biological replicates ± S.D.


<table>
  <thead>
    <tr>
      <th>Substrate</th>
      <th>Variable tail sequence</th>
      <th>Fraction degraded in vivo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gly12</td>
      <td>GGGG GGGG GGGG</td>
      <td>0.20 ± 0.05</td>
    </tr>
    <tr>
      <td>GA</td>
      <td>AGAG GGAG AGGA</td>
      <td>0.88 ± 0.07</td>
    </tr>
    <tr>
      <td>Titin</td>
      <td>HLGL IEVE KPLY</td>
      <td>0.78 ± 0.01</td>
    </tr>
    <tr>
      <td>Basic</td>
      <td>GKGR GKGR GKGR</td>
      <td>0.83 ± 0.05</td>
    </tr>
    <tr>
      <td>Acidic</td>
      <td>GEGD GEGD GEGD</td>
      <td>0.96 ± 0.01</td>
    </tr>
    <tr>
      <td>LYV2-4</td>
      <td>GLYV GGGG GGGG</td>
      <td>0.82 ± 0.03</td>
    </tr>
    <tr>
      <td>LYV4-6</td>
      <td>GGGL YVGG GGGG</td>
      <td>0.83 ± 0.01</td>
    </tr>
    <tr>
      <td>LYV6-8</td>
      <td>GGGG GLYV GGGG</td>
      <td>0.65 ± 0.08</td>
    </tr>
    <tr>
      <td>LYV8-10</td>
      <td>GGGG GGGL YVGG</td>
      <td>0.23 ± 0.01</td>
    </tr>
    <tr>
      <td>LYV10-12</td>
      <td>GGGG GGGG GLYV</td>
      <td>0.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr1</td>
      <td>YGGG GGGG GGGG</td>
      <td>0.3 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr2</td>
      <td>GYGG GGGG GGGG</td>
      <td>0.49 ± 0.08</td>
    </tr>
    <tr>
      <td>Tyr3</td>
      <td>GGYG GGGG GGGG</td>
      <td>0.80 ± 0.01</td>
    </tr>
    <tr>
      <td>Tyr4</td>
      <td>GGGY GGGG GGGG</td>
      <td>0.80 ± 0.02</td>
    </tr>
    <tr>
      <td>Tyr5</td>
      <td>GGGG YGGG GGGG</td>
      <td>0.8 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr6</td>
      <td>GGGG GYGG GGGG</td>
      <td>0.4 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr7</td>
      <td>GGGG GGYG GGGG</td>
      <td>0.32 ± 0.05</td>
    </tr>
    <tr>
      <td>Tyr8</td>
      <td>GGGG GGGY GGGG</td>
      <td>0.20 ± 0.03</td>
    </tr>
    <tr>
      <td>Ala4</td>
      <td>GGGA GGGG GGGG</td>
      <td>0.28 ± 0.03</td>
    </tr>
    <tr>
      <td>Arg4</td>
      <td>GGGR GGGG GGGG</td>
      <td>0.39 ± 0.03</td>
    </tr>
    <tr>
      <td>Asn4</td>
      <td>GGGN GGGG GGGG</td>
      <td>0.23 ± 0.01</td>
    </tr>
    <tr>
      <td>Asp4</td>
      <td>GGGD GGGG GGGG</td>
      <td>0.20 ± 0.02</td>
    </tr>
    <tr>
      <td>Cys4</td>
      <td>GGGC GGGG GGGG</td>
      <td>0.35 ± 0.02</td>
    </tr>
    <tr>
      <td>Glu4</td>
      <td>GGGE GGGG GGGG</td>
      <td>0.27 ± 0.02</td>
    </tr>
    <tr>
      <td>Gln4</td>
      <td>GGGQ GGGG GGGG</td>
      <td>0.41 ± 0.04</td>
    </tr>
    <tr>
      <td>His4</td>
      <td>GGGH GGGG GGGG</td>
      <td>0.26 ± 0.01</td>
    </tr>
    <tr>
      <td>Ile4</td>
      <td>GGGI GGGG GGGG</td>
      <td>0.78 ± 0.05</td>
    </tr>
    <tr>
      <td>Leu4</td>
      <td>GGGL GGGG GGGG</td>
      <td>0.7 ± 0.1</td>
    </tr>
    <tr>
      <td>Lys4</td>
      <td>GGGK GGGG GGGG</td>
      <td>0.36 ± 0.02</td>
    </tr>
    <tr>
      <td>Met4</td>
      <td>GGGM GGGG GGGG</td>
      <td>0.6 ± 0.2</td>
    </tr>
    <tr>
      <td>Phe4</td>
      <td>GGGF GGGG GGGG</td>
      <td>0.7 ± 0.1</td>
    </tr>
    <tr>
      <td>Pro4</td>
      <td>GGGP GGGG GGGG</td>
      <td>0.19 ± 0.03</td>
    </tr>
    <tr>
      <td>Ser4</td>
      <td>GGGS GGGG GGGG</td>
      <td>0.24 ± 0.04</td>
    </tr>
    <tr>
      <td>Thr4</td>
      <td>GGGT GGGG GGGG</td>
      <td>0.24 ± 0.01</td>
    </tr>
    <tr>
      <td>Trp4</td>
      <td>GGGW GGGG GGGG</td>
      <td>0.5 ± 0.1</td>
    </tr>
    <tr>
      <td>Val4</td>
      <td>GGGV GGGG GGGG</td>
      <td>0.7 ± 0.1</td>
    </tr>
    <tr>
      <td>Ala1</td>
      <td>AGGG GGGG GGGG</td>
      <td>0.41 ± 0.03</td>
    </tr>
    <tr>
      <td>Ala1 + 4</td>
      <td>AGGA GGGG GGGG</td>
      <td>0.84 ± 0.03</td>
    </tr>
    <tr>
      <td>Ala2 + 4</td>
      <td>GAGA GGGG GGGG</td>
      <td>0.88 ± 0.01</td>
    </tr>
    <tr>
      <td>Ala3 + 4</td>
      <td>GGAA GGGG GGGG</td>
      <td>0.88 ± 0.01</td>
    </tr>
    <tr>
      <td>Ala4 + 5</td>
      <td>GGGA AGGG GGGG</td>
      <td>0.87 ± 0.02</td>
    </tr>
    <tr>
      <td>Ala4 + 6</td>
      <td>GGGA GAGG GGGG</td>
      <td>0.7 ± 0.1</td>
    </tr>
    <tr>
      <td>Ala4 + 7</td>
      <td>GGGA GGAG GGGG</td>
      <td>0.51 ± 0.09</td>
    </tr>
    <tr>
      <td>Ala4 + 8</td>
      <td>GGGA GGGA GGGG</td>
      <td>0.31 ± 0.04</td>
    </tr>
    <tr>
      <td>Ala4 + 9</td>
      <td>GGGA GGGG AGGG</td>
      <td>0.24 ± 0.07</td>
    </tr>
    <tr>
      <td>Ala4 + 10</td>
      <td>GGGA GGGG GAGG</td>
      <td>0.29 ± 0.07</td>
    </tr>
    <tr>
      <td>Ala4 + 11</td>
      <td>GGGA GGGG GGAG</td>
      <td>0.33 ± 0.06</td>
    </tr>
    <tr>
      <td>Ala4 + 12</td>
      <td>GGGA GGGG GGGA</td>
      <td>0.31 ± 0.04</td>
    </tr>
  </tbody>
</table>

For studies of intracellular degradation, we used an E. coli B strain, which lacks the AAA+ Lon protease; deleted the chromosomal copies of clpP, clpX, and clpA, as ClpAP can also degrade ssrA-tagged substrates (Gottesman et al., 1998; Farrell et al., 2005); and placed genes encoding ClpX∆N and ClpP on a plasmid under arabinose-inducible control (Figure 1B; Guzman et al., 1995). Despite lacking a family-specific N-terminal domain, ClpXΔN supports ClpP-degradation of ssrA-tagged substrates as well as wild-type ClpX but does not interact with many other cellular substrates and adaptors (Singh et al., 2001; Wojtyra et al., 2003; Flynn et al., 2003; Martin et al., 2005). GFP substrates were cloned under transcriptional control of a constitutive ProD promoter (Figure 1B; Davis et al., 2011). To control for ClpXP-independent degradation, we used a pBAD plasmid isogenic to the clpP/clpX∆N vector but lacking these genes (Figure 1B). To determine the extent of intracellular GFP degradation, we measured GFP fluorescence after arabinose induction and growth for 35 min.

We first used this system to characterize substrates with different high or low complexity sequences in the 12-residue cassette. Substrate expression levels were sensitive to the cassette sequence, possibly because of effects on mRNA stability or translation, varying by as much as 7-fold (Figure 1C). To control for differences in expression when measuring degradation of different substrates, we normalized measurements in the strain expressing ClpXΔNP to a strain lacking it (Figure 1D, Table 1). In these experiments, low-complexity tails rich in acidic or basic residues promoted GFP degradation at levels comparable to a high-complexity sequence derived from the human titinI27 domain or a sequence of interspersed glycines and alanines (called GA). By contrast, a cassette sequence of twelve glycines (called Gly12) resulted in poor degradation.

We purified N-terminally His6-tagged variants of these substrates and performed Michaelis-Menten analysis of steady-state ClpXΔNP degradation in vitro (Figure 1E). Degradation with the Gly12 cassette was too slow to measure, but the GA and acidic cassettes promoted degradation with Vmax values similar to the titin sequence (Figure 1F, Table 2). The basic cassette sequence resulted in an intermediate rate of maximal degradation.

**Table 2.**
 Degradation of purified variable-tail substrates in vitro.Fitted parameters from Michaelis-Menten analysis of substrate degradation by ClpXΔNP. No fit – substrate degradation too slow to be accurately fit. Values are the average of three biological replicates ± S.D.


<table>
  <thead>
    <tr>
      <th>Substrate</th>
      <th>Vmax (min−1 hex−1)</th>
      <th>KM (μM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gly12</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>GA</td>
      <td>2.4 ± 0.1</td>
      <td>1.7 ± 0.1</td>
    </tr>
    <tr>
      <td>Titin</td>
      <td>2.3 ± 0.2</td>
      <td>1.1 ± 0.1</td>
    </tr>
    <tr>
      <td>Basic</td>
      <td>1.1 ± 0.1</td>
      <td>1.4 ± 0.1</td>
    </tr>
    <tr>
      <td>Acidic</td>
      <td>2.7 ± 0.3</td>
      <td>1.9 ± 0.2</td>
    </tr>
    <tr>
      <td>Tyr1</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Tyr2</td>
      <td>0.10 ± 0.03</td>
      <td>0.7 ± 0.2</td>
    </tr>
    <tr>
      <td>Tyr3</td>
      <td>0.7 ± 0.2</td>
      <td>1.3 ± 0.2</td>
    </tr>
    <tr>
      <td>Tyr4</td>
      <td>1.7 ± 0.1</td>
      <td>1.9 ± 0.2</td>
    </tr>
    <tr>
      <td>Tyr5</td>
      <td>1.1 ± 0.1</td>
      <td>1.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr6</td>
      <td>0.08 ± 0.02</td>
      <td>0.7 ± 0.3</td>
    </tr>
    <tr>
      <td>Tyr7</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Tyr8</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Ala4</td>
      <td>0.13 ± 0.06</td>
      <td>1.6 ± 0.8</td>
    </tr>
    <tr>
      <td>Arg4</td>
      <td>0.4 ± 0.1</td>
      <td>1.8 ± 0.4</td>
    </tr>
    <tr>
      <td>Asn4</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Asp4</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Cys4</td>
      <td>0.16 ± 0.04</td>
      <td>0.9 ± 0.4</td>
    </tr>
    <tr>
      <td>Glu4</td>
      <td>0.11 ± 0.06</td>
      <td>1.1 ± 0.6</td>
    </tr>
    <tr>
      <td>Gln4</td>
      <td>0.40 ± 0.07</td>
      <td>1.8 ± 0.3</td>
    </tr>
    <tr>
      <td>Ile4</td>
      <td>1.4 ± 0.3</td>
      <td>2.2 ± 0.3</td>
    </tr>
    <tr>
      <td>Leu4</td>
      <td>1.3 ± 0.1</td>
      <td>2.0 ± 0.2</td>
    </tr>
    <tr>
      <td>Lys4</td>
      <td>0.3 ± 0.1</td>
      <td>2.0 ± 0.7</td>
    </tr>
    <tr>
      <td>Met4</td>
      <td>1.3 ± 0.1</td>
      <td>2.1 ± 0.3</td>
    </tr>
    <tr>
      <td>Phe4</td>
      <td>1.4 ± 0.2</td>
      <td>2.5 ± 0.2</td>
    </tr>
    <tr>
      <td>Pro4</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Ser4</td>
      <td>No fit</td>
      <td></td>
    </tr>
    <tr>
      <td>Thr4</td>
      <td>0.10 ± 0.02</td>
      <td>2.0 ± 0.6</td>
    </tr>
    <tr>
      <td>Trp4</td>
      <td>0.48 ± 0.03</td>
      <td>1.4 ± 0.1</td>
    </tr>
    <tr>
      <td>Val4</td>
      <td>1.7 ± 0.2</td>
      <td>2.2 ± 0.2</td>
    </tr>
    <tr>
      <td>Ala1</td>
      <td>0.19 ± 0.04</td>
      <td>1.8 ± 0.8</td>
    </tr>
    <tr>
      <td>Ala1 + 4</td>
      <td>2.3 ± 0.2</td>
      <td>2.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Ala3 + 4</td>
      <td>2.4 ± 0.1</td>
      <td>2.1 ± 0.1</td>
    </tr>
    <tr>
      <td>Ala4 + 5</td>
      <td>1.7 ± 0.2</td>
      <td>1.5 ± 0.1</td>
    </tr>
    <tr>
      <td>Ala4 + 7</td>
      <td>0.38 ± 0.09</td>
      <td>0.8 ± 0.2</td>
    </tr>
    <tr>
      <td>Ala4 + 9</td>
      <td>0.09 ± 0.04</td>
      <td>0.5 ± 0.3</td>
    </tr>
    <tr>
      <td>Tyr1 + 4</td>
      <td>1.5 ± 0.1</td>
      <td>1.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr2 + 4</td>
      <td>2.1 ± 0.1</td>
      <td>1.1 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr3 + 4</td>
      <td>1.2 ± 0.1</td>
      <td>2.4 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr4 + 5</td>
      <td>1.4 ± 0.2</td>
      <td>1.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr4 + 6</td>
      <td>2.4 ± 0.2</td>
      <td>1.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr4 + 7</td>
      <td>1.0 ± 0.1</td>
      <td>0.67 ± 0.05</td>
    </tr>
    <tr>
      <td>Tyr4 + 8</td>
      <td>2.0 ± 0.3</td>
      <td>0.92 ± 0.06</td>
    </tr>
    <tr>
      <td>Tyr1 + 3</td>
      <td>1.4 ± 0.1</td>
      <td>0.9 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr2 + 3</td>
      <td>0.81 ± 0.03</td>
      <td>1.1 ± 0.1</td>
    </tr>
    <tr>
      <td>Tyr3 + 5</td>
      <td>0.7 ± 0.1</td>
      <td>0.43 ± 0.03</td>
    </tr>
    <tr>
      <td>Tyr3 + 6</td>
      <td>1.1 ± 0.1</td>
      <td>0.62 ± 0.05</td>
    </tr>
    <tr>
      <td>Tyr3 + 7</td>
      <td>0.97 ± 0.08</td>
      <td>0.61 ± 0.03</td>
    </tr>
    <tr>
      <td>Tyr3 + 8</td>
      <td>0.49 ± 0.07</td>
      <td>0.39 ± 0.06</td>
    </tr>
    <tr>
      <td>Val1 + 4</td>
      <td>2.3 ± 0.1</td>
      <td>1.6 ± 0.1</td>
    </tr>
    <tr>
      <td>Val2 + 4</td>
      <td>1.8 ± 0.1</td>
      <td>1.2 ± 0.1</td>
    </tr>
    <tr>
      <td>Val3 + 4</td>
      <td>1.6 ± 0.1</td>
      <td>1.1 ± 0.1</td>
    </tr>
    <tr>
      <td>Val4 + 5</td>
      <td>2.1 ± 0.1</td>
      <td>1.5 ± 0.1</td>
    </tr>
    <tr>
      <td>Val4 + 6</td>
      <td>1.4 ± 0.1</td>
      <td>1.1 ± 0.1</td>
    </tr>
    <tr>
      <td>Val4 + 7</td>
      <td>1.3 ± 0.1</td>
      <td>0.93 ± 0.01</td>
    </tr>
    <tr>
      <td>Val4 + 8</td>
      <td>1.0 ± 0.1</td>
      <td>0.88 ± 0.06</td>
    </tr>
  </tbody>
</table>

The differences between our results in vivo and in vitro suggest that the endpoint assay in vivo has an upper limit and cannot differentiate rates once the pool of cellular GFP has been degraded. About 20% of the Gly12 substrate appeared to be degraded in vivo, whereas no degradation was seen in vitro. Maturation of the GFP chromophore lags protein folding (Reid and Flynn, 1997), and thus degradation of immature non-fluorescent GFP would not be detected in our cellular assay. It is possible that solutes or macromolecular crowding in the cell enhance ClpXP activity or make GFP easier to unfold. Nevertheless, 12 consecutive glycines inhibit ClpXP unfolding/degradation of GFP both in vivo and in vitro, whereas other low-complexity sequences do not.

### A small stretch of tail residues mediates unfolding grip

We substituted amino acids in the Gly12 cassette to identify residues/positions that might improve ClpX grip and thus rates of unfolding and degradation. We first positioned a three-residue Leu-Tyr-Val (LYV) sequence in a sliding window across an otherwise poly-Gly cassette (Figure 2A). This tripeptide sequence was selected because its residues are large and hydrophobic, unlike the surrounding Gly residues. Placing the LYV sequence at positions 2–4, 4–6, or 6–8 (numbered relative to the last residue of the folded domain) improved GFP degradation to levels similar to the GA substrate, whereas this tripeptide at positions 8–10 and 10–12 had no substantial effect relative to the Gly12 parent (Figure 2A, Table 1). These results suggest that ClpX grips side chains within the first eight residues of the substrate tail during unfolding.

![Figure 2.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig2-v2.jpg)

**Figure 2.:** (A) Fraction intracellular degradation for substrates with tails containing LYV tripeptides in otherwise all-glycine cassettes. Gly12 and GA substrates were included as internal controls. (B) Fraction intracellular degradation for substrates with tails containing one tyrosine (Y) in otherwise all-glycine cassettes. Gly12 and GA substrates were included as internal controls. (C) Vmax values from Michaelis-Menten analysis of degradation of purified substrates with single-tyrosine cassettes. (D) Rates of ATP hydrolysis by ClpXΔN (0.1 μM hexamer) in the presence of ClpP (0.3 μM 14-mer) in the absence (–) or presence of different substrates (15 μM monomer). (E) ATP cost of degrading substrates with single-tyrosine cassettes. Note that the Y-axis is logarithmic. In all panels, values represent averages (± S.D.) of three biological replicates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Values are the average of three biological replicates ± S.D. None of the substrates exhibited a substantial increase in KM, indicating that differences in degradation rates result from differences in grip rather than in initial substrate recognition.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Rates of ATP hydrolysis by ClpXΔN (0.1 μM hexamer) in the presence of ClpP (0.3 μM 14-mer) in the absence (–) or presence of different substrates (15 μM monomer). (B) ATP cost of degrading substrates. In both panels, values represent averages (± S.D.) of three biological replicates.

To examine the contributions of individual residues to grip, we constructed another panel of substrates in which a single Tyr residue was placed at each of the first eight tail positions in otherwise all-glycine cassettes (Figure 2B). We then tested degradation in vivo. Substrates with a single Tyr at positions 3, 4, and 5 were efficiently degraded, a Tyr at position 2 supported an intermediate level of degradation, and Tyr side chains at other cassette positions supported degradation similar to the Gly12 parent (Figure 2B, Table 1). Thus, four residues appear to contribute the most important grip contacts during unfolding, with tail positions 3–5 being most significant. When we measured degradation of purified substrates in vitro (Figure 2C, Table 2), single Tyr side chains at positions 2–6 facilitated GFP degradation, with the experimental Vmax values forming a roughly normal distribution centered around position 4. Again, Tyr side chains at positions 3–5 were most important, Tyr residues at the flanking 2 and 6 positions had small effects, and Tyr side chains at positions 1, 7, or 8 had no discernable effect. Importantly, changing the position of the Tyr side chain altered the maximal rate of unfolding/degradation without substantially affecting KM for degradation or the ability of substrate to stimulate ATP hydrolysis (Figure 2D, Figure 2—figure supplements 1–2, Figure 2—source data 1). As a result, substrates that were degraded slowly also exhibited a high ATP cost for degradation (Figure 2E). In combination, these results support a model in which ClpX preferentially grips the side chains of residues at positions 3–5 during GFP unfolding. Moreover, gripping a single Tyr side chain at one of these positions is sufficient for robust unfolding and degradation of GFP.

### Side-chain grip preferences

Next, we exploited this system to determine how different types of side chains affect ClpX grip. We constructed substrates in which each of the remaining 18 natural amino acids was placed at position 4 of a cassette with glycines at the other 11 positions. These substrates exhibited a wide range of susceptibility to ClpXP degradation in E. coli (Figure 3A, Table 1). In general, tails containing an aromatic or large/branched hydrophobic side chain (Tyr, Phe, Val, Ile, Leu, or Met) promoted the most efficient unfolding and degradation, whereas small and/or polar side chains were least efficient. The inhibitory effects of polarity and charge on grip were most obvious for side chains with similar shapes. For example, Val was one of the best side chains for grip, whereas the isosteric Thr side chain was very poor (Figure 3B). Similarly, a polar Gln side chain resulted in better grip than an isosteric but negatively charged Glu side chain (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig3-v2.jpg)

**Figure 3.:** (A) In substrates with otherwise all-glycine cassettes, fraction intracellular degradation depends on side-chain identity at tail-position 4. (B) Comparison of degradation in vivo for substrates with Thr or Val at tail-position four or Glu or Gln at tail-position 4 (Student’s two-tailed t-test significance; Val/Thr: t = 6.37, df = 4; Glu/Gln: t = 5.47, df = 4). (C) Vmax values from Michaelis-Menten analysis of degradation of purified substrates. (D) Effects of position-4 residues, color-coded by side-chain properties, on Vmax. (E) Comparison of degradation in vitro between substrates with Ala, Ser, Cys, Thr, or Val at tail-position four or Glu or Gln at tail-position 4 (Student’s two-tailed t-test significance; Val/Thr: t = 13.3, df = 4; Glu/Gln: t = 5.49, df = 4). (F) ATP cost of degrading substrates with Ala, Cys, Thr, Val, Glu, or Gln at tail-position 4. With the exception of panel A, where Gly12 and GA values represent averages (± S.D.) of nine biological replicates, all values represent three biological replicates.

We also determined steady-state kinetic parameters for degradation of a subset of purified substrates in vitro (Figure 3C, Table 2). These results largely mirrored results in vivo, with mid-sized or large hydrophobic and aromatic residues promoting the fastest rates of degradation (Figure 3D).

Again, Val supported much better degradation than Thr, and Gln promoted significantly faster degradation than Glu in degradation assays in vitro (Figure 3E). Further, Ser failed to support GFP degradation while both Ala and Cys facilitated low-level degradation (Figure 3E). The Ala-4, Ser-4, Cys-4, Thr-4, Val-4, Glu-4, and Gln-4 substrates at concentrations of 15 µM stimulated the rate of ClpX ATP hydrolysis ~3–4 fold compared to the absence of substrate (Figure 2—figure supplement 2, Figure 2—source data 1). Thus, each substrate binds ClpX well at this concentration, supporting a model in which the large differences in maximal degradation arise from poor grip caused, at least in part, by differences in side-chain charge and polarity. The maximal degradation rates for these substrates (Figure 3E) were inversely correlated with their energetic efficiencies of degradation (Figure 3F), indicating that poor grip results in non-productive ATP hydrolysis.

### Synergistic side-chain interactions promote GFP unfolding

Placing a single alanine at cassette position four with glycines at the remaining positions resulted in only marginally better degradation than the Gly12 substrate (Figure 3A and C). By contrast, the GA cassette – with alanines at positions 1, 3, 7, 9, and 12 – supported efficient degradation (Figure 1D and F), despite the fact that positions 1, 7, 9, and 12 do not seem to be important determinants of grip (Figure 4A). This discrepancy suggested that synergistic interactions between the ClpX pore and multiple side chains might allow substantially better grip. To test this model, we constructed a panel of substrates with one alanine at position 4 and a second alanine at position 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, or 12 (Figure 4B). In our cellular assay, alanines at cassette positions 1/4, 2/4, 3/4, and 4/5 supported robust degradation, alanines at positions 4/6 and 4/7 facilitated moderate degradation, and alanines at positions 4/8, 4/9, 4/10, 4/11 and 4/12 were little better than the single alanine at position 4 (Figure 4B). A single Ala at position 1 supported slightly better degradation in vivo than a single Ala at position 4, but the Ala-1/4 substrate was degraded more efficiently (Figure 4C). This difference was more pronounced in assays of degradation in vitro (Figure 4D, Table 2). Indeed, Vmax for degradation of the Ala-1/4 substrate (2.3 ± 0.2 min−1) was more that 10-fold greater than Vmax for the Ala-1 substrate (0.19 ± 0.04 min−1) or Ala-4 substrate (0.13 ± 0.06 min−1). The non-additivity of these Vmax values provides direct evidence for synergy in grip.

![Figure 4.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig4-v2.jpg)

**Figure 4.:** (A) GA and Ala-4 cassette sequences. A heatmap of Vmax values from Figure 2C is overlaid to show contribution of single tyrosine residues as each tail position. (B) Fraction intracellular degradation of substrates with one alanine at tail-position 4 and a second alanine at a variable position in otherwise all-glycine cassettes. (C) Comparison of intracellular degradation for a subset of substrates, including Ala-1. (D) Vmax values from Michaelis-Menten analysis of degradation of purified substrates. (E and F) Michaelis-Menten Vmax values for purified substrates with one tyrosine (E) or valine (F) at tail-position four and a second tyrosine (E) or valine (F) at each tail position in otherwise all-glycine cassettes. Overlaid dashed lines indicate degradation rate for the parental Tyr-4 (E) or Val-4 (F) substrates. In all panels, values represent averages (± S.D.) of three biological replicates.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Vmax values for degradation from Michaelis-Menten analysis of purified substrates with one tyrosine at tail-position three and a second tyrosine at a variable position in otherwise all-glycine cassettes.Relative degradation for substrate tails with a single Tyr residue at position 3 or 4 indicated by dashed lines. Values represent averages (± S.D.) of three biological replicates.

Because the pore loops of ClpX and other AAA+ motors interact with every other substrate residue in cryo-EM structures (Monroe et al., 2017; Gates et al., 2017; Puchades et al., 2017; de la Peña et al., 2018; Majumder et al., 2019; Dong et al., 2019; White et al., 2018), we investigated whether a similar spacing of large side chains enhances grip. We designed panels of substrates with either Tyr or Val fixed at tail position 4 and a second residue of the same type at positions 1, 2, 3, 5, 6, 7, or 8 in an otherwise all-Gly cassette (Figure 4E and F). Among the Tyr substrates, the Tyr-2/4, Tyr-4/6, and Tyr-4/8 substrates promoted faster GFP degradation than the parental Tyr-4 substrate, whereas the other substrates exhibited similar or slower degradation (Table 2; Figure 4E). It is noteworthy that although the effect of multiple residues was irrelevant for the Ala-4/8 substrate (Figure 4B), the Tyr-4/8 substrate was gripped well, suggesting that spacing of Tyr in multiples of two may allow ClpX to grip substrate in a preferred conformation. Among the Val substrates, Val-1/4 and Val-4/5 facilitated slightly faster GFP degradation than the parental Val-4 substrate, Val-2/4 and Val-3/4 were degraded at similar rates to Val-4, and Val-4/6, Val-4/7, and Val-4/8 were degraded slightly slower (Figure 4F; Table 2). As the pattern of degradation rates for the branched Val residue (Figure 4F) is more similar to Ala (Figure 4B and D) than the aromatic Tyr (Figure 4E), it is possible that the ClpX pore-1 loops interact with aromatic residues somewhat differently from non-aromatic residues.

We tested an additional panel of substrates with a Tyr residue at position three and a second Tyr at positions 1, 2, 4, 5, 6, 7, or 8 (Figure 4—figure supplement 1). Unlike the other Tyr substrates, these substrates were generally degraded at rates slightly higher than those of the parental Tyr-3 substrate irrespective of spacing (Table 2; Figure 4—figure supplement 1). Thus, binding Tyr residues separated by multiples of two residues does not always enhance grip.

## Discussion

To unfold target proteins, ClpX and other AAA +protein remodeling machines use cycles of ATP binding and hydrolysis to pull on the degron tail of a substrate, thereby transmitting force to the native domain, but how these machines interact with individual tail residues during unfolding was poorly understood. Here, we identify and quantify the abilities of different tail residues to promote substrate grip during unfolding by ClpXP. Our experiments are enabled by the observation that placing 12 Gly residues between native GFP and a degron eliminates ClpXP degradation in vitro and markedly slows degradation in vivo. GFP unfolding/degradation was not inhibited by 12-residue sequences containing mixtures of Gly and Ala (GA cassette); Gly, Lys, and Arg (basic cassette); or Gly, Asp, and Glu (acidic cassette). Compared with these sequences, ClpXP probably grips Gly12 poorly because of the absence of β-carbons and distal side-chain atoms or increased backbone flexibility. We use ‘grip’ in a functional rather than strictly physical sense, although the two concepts are undoubtedly related.

Ensemble and single-molecule experiments show that ClpXP can translocate an enormous number of different amino-acid sequences, including long Gly tracts, with only minor velocity differences (Aubin-Tam et al., 2011; Maillard et al., 2011; Sen et al., 2013; Cordova et al., 2014; Barkow et al., 2009). For example, in assays requiring ATP-dependent translocation, ClpXP degraded peptide substrates containing Gly10, [Val-Gly]5, or [Phe-Gly]5 sequences at similar rates (Barkow et al., 2009). However, if ClpX can translocate poly-Gly sequences, then why does Gly12 inhibit or slow unfolding/degradation? When ClpX pulls on a native protein, Newtonian mechanics dictate that the folded domain resists with an opposing force, which would be absent during translocation of an unstructured polypeptide. Hence, when ATP hydrolysis is coupled to molecular motion during an unfolding power stroke, we imagine that ClpX's grip on the Gly12 sequence is insufficient to resist the opposition of the folded domain, causing an unproductive power stroke in which the pore-1 loops slip and fail to advance the substrate tail. In support of this model, we find that poor grip correlates with substantial increases in the ATP cost of degradation for the position-4 and Tyr-scan variants, an indication of slipping and futile power strokes. For example, degradation of one molecule of the Tyr-3, Tyr-4, and Tyr-5 substrates required hydrolysis of an average of ~180–240 ATPs, whereas degradation of the Tyr-2 or Tyr-6 substrates required hydrolysis of ~1900 and~3700 ATPs, respectively. These findings corroborate a previous report of futile power strokes during unsuccessful unfolding of a difficult substrate by ClpXP (Kraut, 2013). Furthermore, substrate-tail contacts with the axial pore that stimulate ATP hydrolysis by ClpX do not fully overlap with the contacts that determine grip.

A Tyr-scan experiment shows that tail-position 4 is most important for grip, with flanking positions showing diminishing effects. We expect that amino-acid substitutions at positions 3 and 5 would show side-chain grip trends similar to those observed at position 4. This is not true at tail-position 1, where Tyr did not improve grip but Ala did, perhaps because this part of the tail interacts with different residues in ClpX or the folded GFP domain than downstream positions. A single Ala at tail-position four is gripped poorly but a second Ala at certain positions can improve unfolding/degradation. Contacts between the second Ala and the ClpX pore may contribute to stronger grip. Alternatively, the second Ala might affect ClpX contacts made by the first Ala by altering the substrate conformation.

In our GFP substrate with a single Tyr at tail-position 4, this side chain is likely to contact a pore-1 loop close to the folded GFP domain. In an extended chain, four residues would span ~12 Å, a distance that modeling suggests would allow interaction with either the highest or second highest pore-1 loop of ClpX (Figure 5A; Puchades et al., 2017; X. Fei, personal communication). This is also an area where the axial channel is most tightly constricted around substrate. The distribution of Tyr-effects at positions 2–6 could reflect interactions with different pore-1 loops or the probability that Tyr side chains at different positions contact one specific pore-1 loop. Optical trapping studies indicate that 5–8 residues are moved by a single ClpXP power stroke (Aubin-Tam et al., 2011; Maillard et al., 2011). Thus, once the Tyr side chain at position 4 is engaged by a pore-1 loop, one successful translocation event probably unfolds GFP. Indeed, although many unsuccessful power strokes and ATP hydrolysis events occur while ClpXP is attempting to unfold a stable domain, hydrolysis of a single ATP ultimately results in unfolding. We find it notable that the Tyr-scan distribution is only two residues wide at half height. Hence, one tyrosine at position 4 mediates robust unfolding, whereas one tyrosine at position 7 has no effect. If a position-4 side chain can contact a pore-1 loop high in the ClpX pore, then a position-7 side chain should be able to contact another pore-1 loop lower in the pore. If this model is correct, then it implies that physical contacts between substrate tail residues and the upper pore-1 loops of ClpX are far more important for grip than interaction with the lower loops.

![Figure 5.](https://cdn.elifesciences.org/articles/46808/elife-46808-fig5-v2.jpg)

**Figure 5.:** (A) Model of an extended poly-alanine substrate in the axial pore of ClpX and its interactions with different pore-1 loops based on cryo-EM structures of ClpXP (X.Fei, T.A. Bell, B.M. Stinson, S. Jenni, T.A. Baker, S.C. Harrison, and R.T. Sauer, in preparation). Similar loop-substrate interactions are observed in the yeast AAA+ protease Yme1 (Puchades et al., 2017). On the right, a heatmap of Vmax values from Figure 2C is shown. The substrate tail residues are numbered relative to where a folded domain would be expected to sit at the apical surface of the AAA+ ring during unfolding. Tail residues 2–6, which promote strong grip in ClpX, are positioned to interact with the three pore-1 loops at the top of the axial pore. (B) Two models for asymmetric contribution of pore-1 loops to substrate grip.

We can imagine several different mechanisms for the asymmetry in grip between pore-1 loops in the upper and lower sections of the ClpX pore. In one model, the stronger grip of upper pore-1 loops occurs because these loops maintain relatively static interactions with substrate throughout a power stroke (Figure 5B, left). Several translocation models have been recently proposed for AAA+ unfoldases in which ATP-bound subunits with pore-1 loops oriented near the top of the pore move together as a rigid unit in response to ATP hydrolysis in a lower subunit (Monroe et al., 2017; Puchades et al., 2017; de la Peña et al., 2018; Dong et al., 2019). Furthermore, a previous study demonstrated that pore-1 loop mutations disrupt substrate unfolding most dramatically when they are in neighboring ClpX subunits, consistent with grip mediated by a clustered subset of pore-1 loops (Iosefson et al., 2015). Alternatively, the substrate tail in the pore could absorb some unfolding force through elastic expansion, diverting part of the energy of each power stroke away from unfolding (Figure 5B, right). Substrate interactions with the uppermost pore-1 loops would minimize the expansion length of the substrate tail, whereas interactions with lower pore-1 loops would allow the tail to absorb more force.

In an otherwise all-Gly cassette context, we find that Val, Ile, Leu, Met, Phe, and Tyr at tail-position 4 all promote reasonable levels of grip. If we think of poly-Gly as a smooth and relatively featureless rope, then these larger and generally non-polar side chains can be viewed as knots in the rope that afford better grip. However, grip is not a simple function of side-chain size. For example, Trp supports slower GFP unfolding than the better-gripped residues, suggesting that there may be an upper limit on the size of a side chain that can be efficiently gripped. Polar atoms, especially those close to the peptide backbone of the substrate, weaken grip. For example, Val is one of the best residues in terms of grip, whereas Thr, which differs only by substituting a hydroxyl for a methyl group, barely supports unfolding. Similarly, Ser alone does not support GFP unfolding, but removing the hydroxyl group (Ala) or substituting a less-polar thiol group (Cys) restores low-level unfolding activity. ClpXP may grip polar side chains less tightly because oxygen or nitrogen atoms bearing partial or full charges are not fully solvated when they are in productive contact with a pore-1 loop and thus incur an energetic penalty. Our finding that large hydrophobic and aromatic side chains are gripped well by ClpX is consistent with a model in which van der Waal’s or hydrophobic interactions between the pore-1 loops and specific side chains in the tail are largely responsible for grip.

Several recent cryo-EM structures of AAA+ proteases and protein-remodeling motors reveal a spiral arrangement of subunits in which aromatic residues in the pore-1 loops interact with substrate side chains spaced two residues apart (Monroe et al., 2017; Gates et al., 2017; Puchades et al., 2017; de la Peña et al., 2018; Majumder et al., 2019; Dong et al., 2019; White et al., 2018). Our observation that substrate tails with two tyrosines can in some cases specifically enhance grip when spaced by a multiple of two residues is consistent with these structures. However, substrates with two Val residues do not exhibit the same periodic grip enhancement as Tyr, and multiple Ala residues together promote strong grip regardless of their relative spacing. It is clear that nonspecific interactions between the axial pore and substrate side chains are sufficient to promote strong grip independent of precise pore-1 loop intercalation. In specific cases, periodic side chain intercalation could enhance grip for aromatic side chains through the establishment of π-stacking networks with the pore-1 loop Tyr residues, possibly by optimizing the bound substrate conformation.

A recent cryo-EM structure of the AAA+ motor NSF, which disassembles SNARE complexes following vesicle fusion, contains well-resolved density for substrate side chains, revealing interactions with the pore-1 loop tyrosine (White et al., 2018). Although NSF disassembles SNARE complexes in a single round of ATP turnover in a mechanism distinct from ClpX (Ryu et al., 2015), the structural similarities between NSF and many AAA+ unfoldase proteases suggests a common mode of substrate interaction and grip. The assembled SNARE complex is remarkably stable, and NSF likely requires strong grip to disassemble the complex. Consistent with our biochemical observations for ClpX, this structure indicates that the strongest substrate contacts are formed with pore-1 loops high in the upper ring of NSF, and that two substrate residues (Met and Leu) that are gripped well by ClpX participate in these interactions.

A previous study found that a Gly15 sequence placed between GFP and an ssrA tag did not slow ClpXP degradation (Barkow et al., 2009). However, their substrate contained six additional residues (Thr1-His2-Gly3-Met4-Asp5-Glu6) between folded GFP and the Gly15 sequence. As we find that Met at position four supports robust unfolding, it is likely that interactions with the extra sequence mediate unfolding of the Gly15 substrate. Our findings suggest that evolutionary placement of tail residues that are gripped well by ClpX may tune degradation of substrates that unfold non-cooperatively or that have multiple-folded domains. Complete, processive unfolding of multi-domain substrates depends critically on interactions between ClpX and the peptide-tail remnants from unfolding and degradation of the previous domain. For example, ClpXP degradation of Domain III of C. crescentus DnaX is inhibited by a Gly-rich sequence between Domains III and IV, which acts as a partial processing mechanism essential for DNA replication (Vass and Chien, 2013). Gly-rich tracts also inhibit unfolding/degradation of E. coli DHFR, although multiple alanines in the tail do not improve degradation of this substrate (Too et al., 2013). Thus, ClpX unfolding of different native substrates probably requires different degrees of grip strength, which could be mediated by more and/or better-gripped amino acids adjacent to the folded domain.

ClpXP contains just two types of subunits, whereas the 26S proteasome consists of more than 30 subunit types (Budenholzer et al., 2017). Nevertheless, our work is reminiscent of and reinforces studies of proteasomal degradation by Matouschek and colleagues. For example, they find that low-complexity sequences primarily composed of Gly, Ser, or Thr residues can inhibit proteasomal degradation (Tian et al., 2005); these residues individually are also insufficient to promote ClpXP degradation of GFP. Similarly, sequences that include Phe and Tyr residues can improve or rescue degradation by both the proteasome and ClpXP. These similarities may arise because the Rpt1-6 unfolding ring of the proteasome, despite containing six distinct subunits, has pore-1 loops very similar to those of ClpX. Given the structural similarities between many AAA+ protein remodeling machines, we expect that the principles underlying grip in ClpX reflect those of the broader family.

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
      <td>Cell line (Escherichia coli)</td>
      <td>E. coli T7 Express ΔclpA ΔclpP ΔclpX</td>
      <td>this paper</td>
      <td></td>
      <td>E. coli strain lacking the ClpA, ClpP, and ClpX genes. progenitor: E. coli T7 Express (New England Biolabs #C2566)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pT7 ClpXΔN(plasmid)</td>
      <td>Martin et al., 2005</td>
      <td></td>
      <td>N-terminally His6-tagged ClpXΔN (residues 62–424) for overexpression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pT7 ClpP (plasmid)</td>
      <td>Kim et al., 2000</td>
      <td></td>
      <td>C-terminally His6-tagged ClpP for overexpression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBAD ClpP/ClpXΔN(plasmid)</td>
      <td>this paper</td>
      <td></td>
      <td>for inducible polycistronic expression of ClpP and ClpXΔN(residues 62–424) for cytoplasmic GFP degradation assays. Progenitor: pBAD (Guzman et al., 1995; jb.177.14.4121–4130.199)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBAD null (plasmid)</td>
      <td>this paper</td>
      <td></td>
      <td>control plasmid for cytoplasmic GFP degradation assays. Progenitor: pBAD (Guzman et al., 1995)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ProD GFP Gly12 ssrA (plasmid)</td>
      <td>this paper</td>
      <td></td>
      <td>for constitutive expression of GFP (residues 1–229) substrates with a 12xGly cassette and partial ssrA (GSENYALAA). All other substrates are derivatives of this construct with different variable cassette sequences. Progenitor: ProD Gemini (Davis et al., 2011; nar/gkq81)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pT7 GFP Gly12 ssrA (plasmid)</td>
      <td>this paper</td>
      <td></td>
      <td>for overexpression of N-terminally His6-tagged GFP (1-229) substrates with a 12xGly cassette and partial ssrA (GSENYALAA). All other substrates are derivatives of this construct with different variable cassette sequences.</td>
    </tr>
  </tbody>
</table>

### Plasmid and strain construction

An expression plasmid containing E. coli ClpP and E. coli ClpXΔN was constructed by cloning ClpP into the open reading frame downstream of the pBAD promoter in pBAD18 (Guzman et al., 1995). A second ribosome binding site (5’-CAAGGAGAATAACG-3’) and the ClpX∆N coding sequence (residues 62–424) was added downstream of the ClpP stop codon to produce a polycistronic expression construct. GFP substrates for cytoplasmic degradation assays were cloned downstream of the constitutive insulated ProD promoter in pSB3C5 (Davis et al., 2011). His6-GFP substrates for purification were cloned into a pET4b derivative downstream of the pT7 promoter. For all substrates, the 12-residue variable cassette was encoded on an oligonucleotide and introduced upstream of a partial ssrA degron (Gly-Ser-Glu-Asn-Tyr-Ala-Leu-Ala-Ala) using PCR mutagenesis. The seven C-terminal residues of this degron are identical to those of the ssrA tag, but we removed the N-terminal part of the ssrA tag to preclude potential SspB inhibition (Hersch et al., 2004).

T7 Express ΔclpA ΔclpP ΔclpX was generated from the E. coli strain T7 Express (New England Biolabs). The bicistronic clpP–clpX locus was removed by using lambda red recombineering (Yu et al., 2000) to replace the locus with an FRT-KanR cassette, which was subsequently removed by FLP recombinase expression. ClpA::FRT-KanR was then transduced into this strain with P1 phage from a ClpA::FRT-KanR strain in the Keio collection (Baba et al., 2006), and the resistance marker was again removed with FLP recombinase. Modification of the correct loci was verified by PCR at each step in strain construction.

### Protein expression and purification

His6-GFP-cassette-ssrA constructs were expressed as described (Kim et al., 2000) and purified by Ni-NTA affinity, Source 15Q anion exchange, and Superdex 200 size-exclusion chromatography. Purified substrates were assessed to be >99% pure by SDS-PAGE and were stored in 25 mM HEPES-KOH (pH 7.5), 150 mM KCl, 10% glycerol, and 500 μM dithiothreitol.

### Degradation assays in vivo

The ProD-GFP plasmid encoding each substrate was transformed into T7 Express ΔclpA ΔclpP ΔclpX cells carrying either pBAD18(ClpP/ClpXΔN) or pBAD18(null). After overnight growth at 30°C on LB agar plates supplemented with 100 μg/mL ampicillin and 34 μg/mL chloramphenicol, single colonies were picked into 5 mL of the same medium and antibiotics and cultures were grown overnight at 30°C. At the start of degradation assays, 50 µL of culture of either the ClpP/ClpXΔN expression strain or the null control strain for each substrate was inoculated into fresh 5 mL LB plus antibiotics and grown at 37°C to OD600 0.7–1.0. The cultures were then centrifuged; resuspended at OD600 1.2 in fresh media plus antibiotics; and 500 μL was added to 1 mL of fresh media plus antibiotics supplemented with 120 mM L-arabinose, for a final concentration of 80 mM L-arabinose and OD600 of 0.4. After 35 min of growth at 37°C, 1 mL of culture was removed, centrifuged, and resuspended in 600 μL of phosphate buffered saline (pH 7.4). Three 150 μL technical replicates of resuspended cells were transferred to wells of a clear-bottom black 96-well plate (Greiner). Both the GFP fluorescence of the cell resuspension (excitation 467 nm, emission 511 nm) and the optical density (absorbance 600 nm) were measured on a SpectraMax M5 plate reader (Molecular Devices). The GFP fluorescence for each ClpX∆NP sample and control sample was divided by the measured cell density to give normalized flprotease and flcontrol values respectively. Fraction degraded was calculated as:

$$
1−(fl_{protease}/fl_{control})
$$

Each degradation assay was performed independently in multiple biological replicates, and the calculated value of fraction degraded was averaged across biological replicates. No obvious outliers were observed, and all values were included in the subsequent analysis.

### Biochemical assays in vitro

Degradation assays were performed at 37°C in 25 mM HEPES-KOH (pH 7.5), 5 mM MgCl2, 200 mM KCl, 10% glycerol, with 0.1 μM ClpX∆N (hexamer), 0.3 μM ClpP (14-mer), 5 mM ATP, 32 mM creatine phosphate (Roche), and 0.08 mg/mL creatine kinase (Millipore-Sigma). For the Thr-4 substrate, assays were performed with 0.5 μM ClpX∆N (hexamer) and 1.5 μM ClpP (14-mer) to measure degradation rates more accurately and facilitate comparison with substrates that were degraded more rapidly. Degradation rates were measured by decrease in fluorescence (excitation 467 nm; emission 511 nm) in 20 μL reactions on a SpectraMax M5 plate reader. To control for signal loss from photobleaching, a parallel set of reactions was measured for each substrate without ClpX∆N or ClpP, and changes in GFP fluorescence in this experiment were subtracted from those in the degradation reaction. Each measurement included three technical replicates measured together in parallel, and the average values of these replicates were fit to a hyperbolic equation to determine KM and Vmax. Three independently-conducted biological replicates were performed in this manner for each substrate to determine average values (± S.D.) for KM and Vmax. No obvious outliers were observed, and all values were included in the subsequent analysis.

ATP hydrolysis rates were measured using a coupled-NADH oxidation assay as described (Martin et al., 2005). Degradation efficiency (ATP hydrolyzed per substrate degraded) was calculated by dividing the rate of ATP hydrolysis at a near saturating substrate concentration (15 μM) by Vmax for substrate degradation.
