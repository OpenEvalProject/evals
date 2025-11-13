# Extensive site-directed mutagenesis reveals interconnected functional units in the alkaline phosphatase active site

## Authors

- Fanny Sunden<sup>1</sup> †
- Ariana Peck<sup>1</sup>
- Julia Salzman<sup>1</sup>
- Susanne Ressl<sup>2</sup>
- Daniel Herschlag<sup>1</sup> †

### Affiliations

1. Department of Biochemistry, Beckman Center Stanford University Stanford United States
2. Molecular and Cellular Biochemistry Department Indiana University Bloomington Bloomington United States

† Corresponding author

## Abstract

Enzymes enable life by accelerating reaction rates to biological timescales. Conventional studies have focused on identifying the residues that have a direct involvement in an enzymatic reaction, but these so-called ‘catalytic residues’ are embedded in extensive interaction networks. Although fundamental to our understanding of enzyme function, evolution, and engineering, the properties of these networks have yet to be quantitatively and systematically explored. We dissected an interaction network of five residues in the active site of Escherichia coli alkaline phosphatase. Analysis of the complex catalytic interdependence of specific residues identified three energetically independent but structurally interconnected functional units with distinct modes of cooperativity. From an evolutionary perspective, this network is orders of magnitude more probable to arise than a fully cooperative network. From a functional perspective, new catalytic insights emerge. Further, such comprehensive energetic characterization will be necessary to benchmark the algorithms required to rationally engineer highly efficient enzymes.

## Introduction

Scientists have long marveled at the enormous rate enhancements and exquisite specificities of enzymes. Remarkable progress has been made since catalysis was viewed as a ‘life force’ just over a century ago (Buchner, 1897; Hein, 1961; Barnett, 2003). Now, the chemical moieties involved in enzymatic transformations can be identified by a combination of structural and functional approaches. The positions of functional groups in X-ray structures can typically be combined with chemical intuition to derive mechanisms for enzymatic reactions (Benkovic and Bruice, 1966; Walsh, 1979; Sinnott, 1998; Silverman, 2002). Such mechanisms are routinely supported by site-directed mutagenesis experiments in which large deleterious rate effects are observed when putative catalytic residues are mutated.

While there remain a subset of reactions that are less understood and whose important and fascinating reaction details are still being worked out (e.g., Das et al., 2011; Weeks et al., 2012), we can write reasonable chemical mechanisms for the vast majority of enzymes (Benkovic and Bruice, 1966; Walsh, 1979; Sinnott, 1998; Silverman, 2002). In contrast, our understanding of the energetics that underlie enzymatic catalysis is far less developed. Such understanding is critical for elucidating the pathways that have been followed in molecular evolution and for designing new, highly efficient enzymes.

The current dominant mechanistic tools, X-ray crystallography and removal of catalytic residues via site-directed mutagenesis, while powerful, have fundamental limitations. Structures reveal the positions of functional groups in active sites, but these static pictures do not allow reaction probabilities to be determined. Specifically, although energies derived from a given structure can, in principle, reveal potential energies, full sampling of the ensemble states of the enzyme, substrates, and surrounding solvent is needed to obtain free energies. It is difficult to combine such sampling with high-level energy functions and to make nontrivial predictions required for independent assessment of such energetic models.

Site-directed mutagenesis has two fundamental limitations. First, site-directed mutagenesis reads out the difference in free energy of the reaction (ΔΔG) for the mutant enzyme relative to the wild type (WT), and so does not report an absolute energetic contribution to catalysis (Kraut et al., 2003; Herschlag and Natarajan, 2013). As an example, the vastly different assignments of the catalytic contributions of residues in the Ketosteroid Isomerase oxyanion hole, dependent on the type and extent of mutation, provide a particularly clear demonstration of this limitation and underscore the need to clearly and explicitly define the comparison states (Kraut et al., 2010; Schwans et al., 2011).

The second limitation of site-directed mutagenesis is that enzymatic residues do not act in isolation (Narlikar and Herschlag, 1998; Kraut et al., 2003). The apparent contribution of one residue is also a function of the surrounding residues and the overall structure, as demonstrated by energetic coupling in double mutant cycles and more dramatically by the fact that a denatured protein still contains its catalytic residues but these so-called catalytic residues no longer provide catalysis (see Kraut et al., 2003 for discussion) (Carter et al., 1984; Horovitz, 1996).

One seemingly important aspect of the interconnectivity of enzymatic residues is highlighted in X-ray structures, which typically reveal or suggest active site hydrogen bond networks and imply a functional connection between the identified catalytic residues and these more extensive ‘network residues’. Indeed, prior investigations have identified networks of energetically coupled residues in enzymes that contribute synergistically to catalysis. These studies include incisive double mutant cycle analysis demonstrating functional and energetic connections between residues (Hermes et al., 1990; Dion et al., 1993; Horovitz et al., 1994; Rajagopalan et al., 2002; Masterson et al., 2008; Singh et al., 2014). Larger scale coupled networks have been observed through statistical analysis of co-evolution and characterization of individual residue's relaxation timescales by NMR (e.g., Lockless and Ranganathan, 1999; Eisenmesser et al., 2002, 2005; McElheny et al., 2005; Freedman et al., 2009; Halabi et al., 2009; Doucet et al., 2011).

A remaining challenge, undertaken in this study, is to link mutant cycle analysis to extended networks. Currently, we lack the ability to ascertain the energetic properties of network residues from structural inspection, first principles, or empirical models. For example, do these networks act as fully cooperative units where disruption of any connection would dissipate the advantage from all of the residues in the network? In the other extreme, do certain side chains act independently from their network neighbors, positioned for function by their backbone placement and/or packing interactions with other portions of the side chain?

Although either extreme might be presumed unlikely, such expectations are not grounded in data given the current absence of quantitative assessments of these extended networks. We have therefore investigated the functional behaviors of an interaction network hypothesized from available structural data in the Escherichia coli alkaline phosphatase (AP) active site (Figure 1). Our experiments reveal and quantitatively delineate the energetic interconnectivity within this highly proficient active site, the type of active site that will be necessary to create if we are to engineer enzymes that rival the catalytic power of natural enzymes.

![Figure 1.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig1-v2.jpg)

**Figure 1.:** (A) The three-dimensional structure of AP with bound Pi (PDB 3TG0). Active site residues are depicted as follows: D101, brown; R166, black; D153, red; K328, green; E322 and Mg2+ ion, blue. (B) A close-up of AP active site from two angles. Dashes represent putative hydrogen bonds. Residues colored as in part (A). (C) Schematic of AP active site interactions represented with the phosphoryl transfer transition state. Residues colored as in part (A). (D) Reaction scheme for phosphomonoester hydrolysis by AP, where ROP represents a phosphate monoester dianion substrate, and E-P represents the covalent seryl-phosphate intermediate (Coleman, 1992).

## Results and discussion

Figure 1A shows the three-dimensional structure of E. coli AP; for simplicity, a single monomer of the homodimeric active enzyme is presented. Figure 1B,C shows a close-up and a schematic depiction of the network of residues in the active site, respectively, and Figure 1D depicts the reaction catalyzed by AP. As expected based on structural data, the presence of the Zn2+ ions and the active site nucleophile, S102, are required for measureable activity (Plocke et al., 1962; O'Brien and Herschlag, 2001; Andrews et al., 2013), and prior work has revealed functional effects from mutation of some of the Zn2+ ligands (Xu and Kantrowitz, 1992; Tibbits et al., 1994, 1996; Ma et al., 1995).

Here, we focus on the other residues in the active site and determine their functional and energetic connectivity (Figure 1C). The energetic effects we refer to here and in the remainder of this study are related to free energy differences. Prior work identified E322, which is required for Mg2+ binding, and R166 as catalytic residues, with mutations of these leading to 88,000 and 6300-fold decreases in the rate of catalytic activity, respectively (Zalatan et al., 2008; O'Brien et al., 2008). Nevertheless, these residues are part of an extensive hydrogen-bonded and Mg2+-coordinating network that also involves D101, D153, K328, the Mg2+ ion liganded by E322, and two water molecules (Figure 1C).

As described in the following sections, we determined the effects of removing each of the five side chains of this apparent network individually and in combination. To determine if a residue's contribution is independent of or dependent on the other side chains, we determined the activity of a minimal form of the AP active site with all five residues mutated, herein referred to as AP minimal (D101A/D153A/R166S/E322Y/K328A), and we also restored each side chain individually to this minimal enzyme. As described below, the results indicated a strong interdependence of the residues, prompting us to explore these interconnections by making nearly all possible combinations of these five mutants (28 out of 32; 2n, where n = 5, the number of positions mutated). Our results identified three interconnected functional units, each with distinct underlying energetic properties, and allowed us to develop a quantitative model that reproduces the observed rate constants and predicts the rate constants of the remaining four mutants not tested herein. For ease of reference, all of the measured and calculated rate constants are listed in Table 1 and shown graphically in Figure 2A and Figure 2B.

**Table 1.**
 Kinetic constants for WT and mutant AP*,†


<table>
  <thead>
    <tr>
      <th>AP mutant</th>
      <th>kcat/KM (M−1s−1)</th>
      <th>fold decrease†</th>
      <th>KM (µM)</th>
      <th>kcat (s−1)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">WT</td>
      <td>3.3 × 107‡</td>
      <td>–</td>
      <td rowspan="2">3.6 × 10−1</td>
      <td rowspan="2">12</td>
    </tr>
    <tr>
      <td>(6.3 × 108)§</td>
      <td>(1)</td>
    </tr>
    <tr>
      <td>D101A</td>
      <td>9.9 (2.0) × 106</td>
      <td>64</td>
      <td>3.6 (0.9)</td>
      <td>36 (9)</td>
    </tr>
    <tr>
      <td>R166S¶,#</td>
      <td>1.0 × 105</td>
      <td>6.3 × 103</td>
      <td>5.0</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>D153A</td>
      <td>2.8 (0.4) × 106</td>
      <td>2.3 × 102</td>
      <td>2.6 (0.7)</td>
      <td>7.6 (2.8)</td>
    </tr>
    <tr>
      <td>E332Y**,#</td>
      <td>7.2 (2.2) × 103</td>
      <td>8.8 × 104</td>
      <td>∼0.5</td>
      <td>–</td>
    </tr>
    <tr>
      <td>K328A#</td>
      <td>7.5 (2.4) × 105</td>
      <td>8.4 × 102</td>
      <td>5.4 (1.8)</td>
      <td>3.4 (0.9)</td>
    </tr>
    <tr>
      <td>D101A/R166S</td>
      <td>5.8 (0.2) × 104</td>
      <td>1.1 × 104</td>
      <td>8.4 (2.3)</td>
      <td>4.2 (2.0) × 10−1</td>
    </tr>
    <tr>
      <td>D101A/D153A#</td>
      <td>3.3 (0.7) × 105</td>
      <td>1.9 × 103</td>
      <td>6.2 (2.1)</td>
      <td>2.2 (0.7)</td>
    </tr>
    <tr>
      <td>D101A/E322Y#</td>
      <td>3.1 (0.1)</td>
      <td>2.0 × 108</td>
      <td>1.5 (0.3) × 102</td>
      <td>4.6 (0.8) × 10−4</td>
    </tr>
    <tr>
      <td>D101A/K328A††</td>
      <td>(2.8 × 104)</td>
      <td>2.3 × 104</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>R166S/D153A</td>
      <td>1.3 (0.1) × 104</td>
      <td>4.9 × 104</td>
      <td>5.3</td>
      <td>7.0 × 10−2</td>
    </tr>
    <tr>
      <td>R166S/E322Y**</td>
      <td>1.6 (0.5)</td>
      <td>3.9 × 108</td>
      <td>27 (11)</td>
      <td>–</td>
    </tr>
    <tr>
      <td>R166S/K328A#</td>
      <td>2.4 (0.4) × 102</td>
      <td>2.6 × 106</td>
      <td>6.3 (2.5) × 101</td>
      <td>1.6 (0.4) × 10−2</td>
    </tr>
    <tr>
      <td>D153A/E322Y</td>
      <td>2.3 (0.1) × 103</td>
      <td>2.7 × 105</td>
      <td>5.2 (0.4) × 10−1</td>
      <td>1.4 (0.3) × 10−3</td>
    </tr>
    <tr>
      <td>D153A/K328A</td>
      <td>4.4 (1.4) × 105</td>
      <td>1.4 × 103</td>
      <td>2.4</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>E322Y/K328A</td>
      <td>1.5 (0.1) × 103</td>
      <td>4.2 × 105</td>
      <td>2.2</td>
      <td>3.4 × 10−3</td>
    </tr>
    <tr>
      <td>D101A/R166S/D153A#</td>
      <td>2.0 (0.7) × 104</td>
      <td>3.2 × 104</td>
      <td>4.8 (1.4)</td>
      <td>8.3 (1.8) × 10−2</td>
    </tr>
    <tr>
      <td>D101A/R166S/E322Y††</td>
      <td>(4.2 × 10−2)</td>
      <td>1.5 × 1010</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>D101A/R166S/K328A††</td>
      <td>(2.8 × 102)</td>
      <td>2.3 × 106</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>D101A/D153A/E322Y††</td>
      <td>(1.3 × 101)</td>
      <td>4.8 × 107</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>D101A/D153A/K328A</td>
      <td>1.2 (0.1) × 105</td>
      <td>5.3 × 103</td>
      <td>11</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>D101A/E322Y/K328A</td>
      <td>1.1 (0.1)</td>
      <td>5.7 × 108</td>
      <td>78</td>
      <td>8.9 × 10−5</td>
    </tr>
    <tr>
      <td>R166S/D153A/E322Y</td>
      <td>1.9 (0.1) × 101</td>
      <td>3.3 × 107</td>
      <td>4.4 (0.2) × 102</td>
      <td>8.3 (1.0) × 10−3</td>
    </tr>
    <tr>
      <td>R166S/D153A/K328A</td>
      <td>3.6 (0.1) × 103</td>
      <td>1.8 × 105</td>
      <td>7.2 (0.1)</td>
      <td>2.6 (0.1) × 10−2</td>
    </tr>
    <tr>
      <td>R166S/E322Y/K328A</td>
      <td>3.9 (0.8) × 10−1</td>
      <td>1.6 × 109</td>
      <td>1.4 (0.3) × 102</td>
      <td>5.7 (1.1) × 10−5</td>
    </tr>
    <tr>
      <td>D153A/E322Y/K328A</td>
      <td>3.2 (0.3) × 102</td>
      <td>2.0 × 106</td>
      <td>2.1 (0.3)</td>
      <td>7.3 (0.3) × 10−4</td>
    </tr>
    <tr>
      <td>D101A/R166S/D153A/E322Y</td>
      <td>9.4 (1.6) × 10−1</td>
      <td>6.7 × 108</td>
      <td>3.5 × 102</td>
      <td>3.2 (0.7) × 10−4</td>
    </tr>
    <tr>
      <td>D101A/R166S/D153A/K328A</td>
      <td>5.5 (1.7) × 103</td>
      <td>1.2 × 105</td>
      <td>12 (5.0)</td>
      <td>6.1 (0.3) × 10−2</td>
    </tr>
    <tr>
      <td>D101A/R166S/E322Y/K328A</td>
      <td>≤2.0 × 10−2</td>
      <td>≥3 × 1010</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>D101A/D153A/E322Y/K328A</td>
      <td>2.0 (0.1)</td>
      <td>3.2 × 108</td>
      <td>1.4 (0.1) × 102</td>
      <td>2.4 (0.3) × 10−4</td>
    </tr>
    <tr>
      <td>R166S/D153A/E322Y/K328A#</td>
      <td>4.4 (0.1)</td>
      <td>1.4 × 108</td>
      <td>2.2 (0.1) × 102</td>
      <td>9.6 (0.5) × 10−4</td>
    </tr>
    <tr>
      <td>D101A/R166S/D153A/E322Y/K328A#</td>
      <td>1.7 (0.3) × 10−1</td>
      <td>3.7 × 109</td>
      <td>1.6 (0.6) × 102</td>
      <td>2.9 (0.7) × 10−5</td>
    </tr>
  </tbody>
</table>

_*Activities were measured in 0.1 M MOPS, pH 8.0, 0.5 M NaCl, 100 µM ZnCl2, and 500 µM MgCl2 at 25°C. Errors in activities are standard deviations from duplicate with the same or independent enzyme preparations (see ‘Materials and methods’).†‘Fold down’ values are kcat/KM for WT AP estimated for reaction with the chemical step rate limiting (footnote d and description in Appendix 1) divided by (kcat/KM) for each mutant. By definition the value for WT AP is one.‡(kcat/KM)obsd (O'Brien and Herschlag, 2002).§For WT AP, the chemical step is not rate limiting (O'Brien and Herschlag, 2002). As has been carried out previously, we used comparisons with a substrate for which the chemical step is rate limiting to estimate the value of kcat/KM for WT AP that would be expected with fast association and the chemical step rate limiting (see description in Appendix 1). Relative values are compared to this number.#The mutant was expressed in two independent enzyme preparations and standard deviations are from activity measurements for the independent preparations.¶From reference (O'Brien et al., 2008).**From reference (Zalatan et al., 2008).††Values in brackets were not measured but are calculated from the energetic behavior of the functional units according to the mathematical model described in Appendix 1 and shown in Appendix 1 Table 2._

![Figure 2.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig2-v2.jpg)

**Figure 2.:** (A) The 32 possible combinations of the five residues diagrammed with color-coding of residues as in Figure 1 to represent whether a particular WT residue is present: D101, brown; R166, black; D153, red; K328, green; and E322 and the Mg2+ ion, blue; the absence of a WT residue at a particular position is indicated by a white square. The catalytic efficiency, kcat/KM (M−1s−1), of each combination is noted below each construct (Table 1). Rate constants calculated from the energetic behavior of the functional units are shown in grey (Table 1). (B) Three-dimensional representation of the activities of the 32 AP variants, with the height of each bar corresponding to kcat/KM (M−1s−1 on a log scale) and the same color scheme as in (A).

### Testing catalytic residues for independence vs interdependence

Figure 3A shows the effects from mutating each of the five active site residues depicted in Figure 1C. Each residue has a significant effect ranging from 64 to 88,000-fold, with the largest effects coming from R166 mutation and Mg2+ ion removal (E322Y). Previous studies have shown that replacing the E322 side chain with a tyrosine leads to loss of Mg2+ from the active site (Zalatan et al., 2008). We confirmed this result and showed that the E322Y mutant reaction is not activated by the presence of Mg2+ (‘Materials and methods’). The absence of Mg2+ binding and activation is consistent with the finding that other members of the AP superfamily that lack Mg2+ have a tyrosine at this position (Zalatan et al., 2008). Indeed, we chose the E322Y mutation for our studies because it gives the same functional effect as E322A while also creating this steric block to Mg2+ binding (Zalatan et al., 2008). While we did not test all possible mutations, several different mutations were tested at each position and shown to give very similar effects, providing no indication of idiosyncratic effects from any of the subtractive mutations made in this study (Appendix 1 Table 1).

![Figure 3.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig3-v2.jpg)

**Figure 3.:** Rate effects from removing individual residues from WT AP (A) or restoring individual WT residues to AP minimal (B). The symbol (±) indicates which residue is varied. Residues are color-coded as in Figure 1: D101, brown; R166, black; D153, red; K328, green; and E322 and Mg2+ ion, blue. The following mutations were made: D101A, R166S, D153A, K328A, and E322Y; several alternative mutations gave similar effects (Appendix 1 Table 1). To the right of the dashed line is the activity of WT AP relative to AP minimal observed (A, B, grey bars) and predicted from the effects of removal of each WT residue from the WT background and assuming independent (energetically additive) effects (A, open bar) or from the effects of addition of each WT residue in the minimal background, assuming independence (B, open bar).

We next determined the degree to which these residues were dependent on one another in two simple ways. First, we removed all five residues simultaneously; if independent, the effects of removal would be multiplicative—that is, energetically additive (Equation 1). However, the cumulative effect assuming additivity gives a predicted activity that is 106-fold lower than the observed activity of the minimal construct (Equation 1), indicating substantial energetic interdependence between these residues (Figure 3A);

$$
ΔΔG^{‡}=[−RTln((k_{cat}/K_{M})_{obsd}/(k_{cat}/K_{M})_{predicted})]=8.3 kcal/mol,
$$



$$
k_{rel,}^{predicted}=k_{rel, D101} \times k_{rel, R166} \times k_{rel,  D153 }\times k_{rel, K328}\times k_{rel, Mg^{2+}}.
$$

We next added each residue back in isolation to the minimal AP construct lacking all five residues, and we compared the rate effect from the added residue to the corresponding rate decrease from removing that residue from WT AP (Figure 3A,B). In each case, there was a larger deleterious effect from removing the residue than the rate enhancement afforded by adding it back. The differential effects ranged from 2.6 to >1900-fold, corresponding to differential energetic effects of up to at least 4.5 kcal/mol. Indeed, D153 added back in isolation is deleterious by at least 10-fold (Figure 3B) but beneficial by 230-fold when added in the otherwise WT background (Figure 3A). Further, the small 2.6-fold (0.57 kcal/mol) differential between restoring D101 to AP minimal and removing it from WT AP likely arises coincidentally from different mechanistic contributions (see below). Thus, each of the five residues has some energetic connection to at least one residue in this network. Overall, the contribution from adding all five residues back is 580-fold greater than predicted from assuming energetically additive effects from addition of each residue individually (Equation 1).

An empirical or theoretical framework to explain this energetic behavior is lacking. In particular, there is no way to discern from structural inspection of an active site whether all neighbors have substantial energetic interactions, the scale and form of these energetic connections, or whether and how far beyond nearest neighbors functional effects extend. Therefore, we proceeded to define the interconnections between active site residues for this model enzyme system.

### Deep mutagenesis to uncover the interrelationships between active site residues: interconnected catalytic units

Figure 2A depicts the set of all 32 possible combinations of mutations of the five catalytic residues, using the color-coding from Figure 1 to represent the presence (colored) or absence (white) of each residue. In the following sections, we describe the energetic properties and interconnections of these residues.

#### The D101/R166/D153 functional unit

R166 was previously identified as a catalytic residue in the AP active site and hypothesized to stabilize the transition state via hydrogen bonds to the non-bridging oxygens (Figure 1C) (O'Brien and Herschlag, 1999; O'Brien et al., 2008). Mutation of R166 to serine or alanine has a similar energetic effect (O'Brien et al., 2008), and given the energetic similarity of R166S and R166A and the practical limits on the number of mutants that could be investigated, we used R166S in all subsequent experiments.

The effects of the other residues on R166 were determined by comparing the effect of mutation of this residue (R166S) in 13 different mutant backgrounds. We first determined the effects of D153 and D101, which are both within hydrogen bonding distance of R166. In the extremes, if the function of R166 was fully dependent on the neighboring aspartate residues then there would be little or no effect from adding back the R166 side chain in the absence of both D101 and D153. Alternatively, if R166 was independent of its neighbors, its full catalytic effect would be restored regardless of the presence of the aspartate residues.

Relative to the full effect of 6300-fold from addition of the R166 side chain with all other residues present, addition of this side chain in the absence of both aspartate side chains gives a much smaller rate increase of only ∼10-fold (Figure 4, left black bar). The presence of either aspartate residue increases the catalytic effectiveness of R166, such that reintroduction of the arginine side chain contributes 170 or 220-fold with D153 or D101 present, respectively, more than the increase from R166 addition with neither aspartate residue present. However, this is still considerably less than the 6300-fold increase with both aspartate residues present (Figure 4, black bars).

![Figure 4.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig4-v2.jpg)

**Figure 4.:** The effects of restoring R166 in different aspartate backgrounds with the Mg2+ ion and K328 present (black) or absent (grey). The arrow above the bar in the D153 background indicates that the ratio is a lower limit. Residues are color-coded as in Figure 1, rate constants are from Table 1, and mutations made are listed in Table 1.

These results indicate that the function of R166 is interconnected with and enhanced by its neighbors, D101 and D153. The simplest model to account for these effects is that each aspartate residue helps to position the arginine side chain for interaction with the non-bridging phosphoryl oxygen atoms (Figure 1C and see below).

We next asked whether the other network side chains are needed for full R166 function and enhance its function through either or both aspartate residues. The gray bars in Figure 4 compare the effects from reintroduction of the arginine side chain with or without the neighboring aspartate residues as in the black bars from this figure described above, but now comparing the effects in the presence or absence of K328 and the active site Mg2+. The effect of arginine add-back is nearly the same with and without K328 and the Mg2+ ion (cf. the pairs of black and gray bars in Figure 4). Hence, R166, D101, and D153 form a functional unit, independent of the Mg2+ ion and K328.

##### Structural effects of D101 and D153

Based on the functional effects shown in Figure 4, we expected mutation of D101 and D153 to result in a misaligned or less-ordered R166. This expectation is supported by prior X-ray structures of single mutants of D101 (Chen et al., 1992) or D153 (PDB 1AJC, 1AJD) and by a structure of the D101A/D153A double mutant collected as part of this investigation.

R166 adopts the same position in structures of WT AP, regardless of the presence of Pi in the active site (PDB 1ED9, 3TG0). Independent structures of apo D153G AP (PDB 1AJC, 1AJD) show displacement of R166 relative to its WT position. In one of these structures, the guanidinium group of R166 is rotated by ∼19°, which would distort the hydrogen bond angles with the non-bridging oxygen atoms of a phosphate bound as it is in WT AP (Figure 5—figure supplement 1). In the second structure of D153G AP, the R166 side chain is flipped away from the active site. The crystal structure of apo D101S similarly shows displacement of R166 (Chen et al., 1992). In contrast, E322Y AP, which lacks the bound Mg2+ ion that is not part of the R166 functional unit, does not influence the position of R166 (Zalatan et al., 2008; Figure 5—figure supplement 2).

To further explore the effects of the aspartate residues on the R166 functional unit, we solved the crystal structure of D101A/D153A AP (Table 2). In one subunit of the AP homodimer, the guanidinium group is flipped away from the active site and adopts a catalytically unproductive conformation that is similar to the conformation observed in one structure of D153G, but more displaced than in the other structure of D153G and D101S AP (Figure 5A). In the other monomer, R166 was observed to populate two rotameric positions, one of which is similarly flipped away from the active site while the other is pointed towards the active site. (Figure 5B). Although this structure lacks a bound Mg2+ ion in the active site, the functional and structural data presented above suggest that this loss will not influence the position of R166. In both active sites of D101A/D153A AP, the bound Pi is not well positioned, populating multiple conformations that are each distinct from its position in WT AP, which likely closely mimics the reactive phosphoryl conformation (Appendix 2 and Appendix 2 Figure 1) (Holtz et al., 1999; O'Brien et al., 2008). These structural comparisons provide evidence that the aspartate residues that flank R166 help to correctly position the reactive phosphoryl group and provide a self-consistent picture of the functional effects of the D101/R166/D153 functional unit. Nevertheless, a future challenge will be to quantitatively link structural rearrangements and resulting structural ensembles to functional effects (Frederick et al., 2007).

**Table 2.**
 X-ray crystallographic data collection and refinement statistics


<table>
  <tbody>
    <tr>
      <td colspan="2">Data collection</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P6322</td>
    </tr>
    <tr>
      <td colspan="2">Unit cell axes</td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>161.4, 161.4, 140.1</td>
    </tr>
    <tr>
      <td>α, β, γ (ο)</td>
      <td>90.0, 90.0, 120.0</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>52.89–2.24 (2.31–2.24)*,†</td>
    </tr>
    <tr>
      <td>Rmerge (%)</td>
      <td>43.0 (305.9)</td>
    </tr>
    <tr>
      <td>Rpim (%)‡</td>
      <td>9.6 (71.9)</td>
    </tr>
    <tr>
      <td>&lt;I&gt;/&lt;σI&gt;</td>
      <td>7.8 (1.4)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>100.0 (100.0)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>21.6 (19.7)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.996 (0.582)</td>
    </tr>
    <tr>
      <td colspan="2">Refinement</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>52.89–2.24†</td>
    </tr>
    <tr>
      <td>No. unique reflections</td>
      <td>51,819 (5086)</td>
    </tr>
    <tr>
      <td>Rwork/Rfree (%)</td>
      <td>21.7/25.9</td>
    </tr>
    <tr>
      <td>Number of atoms</td>
      <td>6794</td>
    </tr>
    <tr>
      <td colspan="2">Average B-factors (Å2)</td>
    </tr>
    <tr>
      <td>protein</td>
      <td>37.8</td>
    </tr>
    <tr>
      <td>water</td>
      <td>30.2</td>
    </tr>
    <tr>
      <td>ligands</td>
      <td>41.2</td>
    </tr>
    <tr>
      <td colspan="2">R.m.s. deviation from ideality</td>
    </tr>
    <tr>
      <td>Bond length (Å)</td>
      <td>0.006</td>
    </tr>
    <tr>
      <td>Bond angles (ο)</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td colspan="2">Ramachandran statistics</td>
    </tr>
    <tr>
      <td>Favored regions (%)</td>
      <td>98.4</td>
    </tr>
    <tr>
      <td>Allowed regions (%)</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>Outliers (%)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>PDB code</td>
      <td>4YR1</td>
    </tr>
  </tbody>
</table>

_*Values in parenthesis are for the highest resolution shell.†The high resolution cut-off applied during scaling and refinement was decided based on CC1/2 and completeness (Diederichs and Karplus, 2013; Evans and Murshudov, 2013).‡Rpim is reported in addition to Rmerge due to the high multiplicity of the data set._

![Figure 5.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig5-v2.jpg)

**Figure 5.:** The active sites of the superimposed crystal structures of Pi-bound D101A/D153A AP (protein: blue, Pi: orange) and Pi-bound WT AP (protein: white, Pi: transparent). The two monomers of the AP dimer exhibit different active site configurations and are therefore both shown (A, B). (In contrast, the WT AP monomers are remarkably similar, as can be seen by comparing panels A and B.) In both monomers of D101A/D153A AP, Pi populates two positions that are distinct from its position in WT AP. (A) In one active site of D101A/D153A, R166 is rotated away from the active site. The hydrogen bond distances between R166 and Pi in WT AP are 2.8 Å (shown in A). (B) In the other active site of D101A/D153A, R166 partially occupies two positions, one of which faces the active site and hydrogen bonds to one of the partially occupied Pi ions. The other rotameric position adopted by R166 is flipped away from the active site, and presumably coincides with the other partially occupied Pi ion, as it would sterically clash with the active-site facing R166 rotamer. Hydrogen bond distances and angles for WT and D101A/D153A AP are listed in Appendix 2 Table 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Superimposed crystal structures of Pi-bound WT AP (purple, PDB 3TG0), apo WT AP (grey, PDB 1ED9), and apo D153G AP (magenta). In two independent structures of D153G AP, R166 is rotated from its position in Pi-bound WT AP by > 19° (PDB 1AJC) or rotated away from the active site (PDB 1AJD).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Superimposed crystal structures of Pi-bound E322Y AP (yellow, PDB 3DYC), which lacks the active site Mg2+ ion, and Pi-bound WT AP (purple, PDB 3TG0). R166 overlays closely in these structures.

##### Possible roles of groups beyond the D101/R166/D153 functional unit in R166 positioning

Single hydrogen bonds between the aspartate residues and R166 might be expected to precisely position the arginine residue only if other interactions position the aspartate residues themselves. We have determined that the remaining groups of the apparent active site network, K328 and the Mg2+ ion, are not required, so positioning of the aspartate side chains must arise from distinct interactions.

The D101 carboxylate group accepts a hydrogen bond from a backbone amide and therefore could be directed by that interaction (Figure 1C). In contrast, the D153 carboxylate group does not appear to accept a hydrogen bond from residues beyond the five probed herein; however, its methylene group packs against the side chains of nearby residues.

Testing the role of the backbone amide in positioning D101 to, in turn, position R166 will be difficult, but the model for D153 is readily testable: mutation of the nearby side chains is predicted to eliminate the ability of D153 to stimulate R166 function. It will also be of interest to determine if, in the absence of the side chains that putatively pack around and position D153, the hydrogen bond network that comprises K328, the Mg2+ ion, and their associated water molecules is now needed to position D153 and, in turn, position the R166 side chain.

#### The D153/Mg2+(E322)/K328 functional unit

The Mg2+ ion in the AP active site had previously been identified as important for catalysis, decreasing activity ∼105-fold when removed by replacing one of the metal ligands, E322, with a tyrosine or alanine, an effect even larger than that from removal of R166 (Zalatan et al., 2008). We assessed possible functional connections to the Mg2+ ion analogously to the approach taken above for R166.

Figure 6 shows the effect from addition of the bound Mg2+ ion (via restoration of E322; Zalatan et al., 2008 and ‘Materials and methods’) in eight different mutant backgrounds. These comparisons test the energetic interconnectivity of the Mg2+ ion with all residues other than D101, and we address D101 and the Mg2+ ion in the following section (‘The D101/Mg2+(E322) Functional Unit’). There is a substantial rate increase of 820-fold from Mg2+ ion addition in the absence of any of the other three residues (Figure 6, far left). This effect is ∼100-fold less than the maximal effect of 88,000-fold from Mg2+ ion addition in the otherwise WT context (Figure 6, far right).

![Figure 6.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig6-v2.jpg)

**Figure 6.:** The effect of Mg2+ ion addition in different mutational backgrounds. Residues are color-coded as in Figure 1, rate constants are from Table 1, and mutations made are listed in Table 1.

Consistent with the results presented above for R166, the presence of R166 has virtually no effect on the rate advantage from adding Mg2+ back to the active site, regardless of which other residues are present or absent (Figure 6, mutant sets −/+R166). Also, when either D153 or K328 is present, the effect from Mg2+ add-back remains the same. Only when both D153 and K328 are present is the full 88,000 effect observed (Figure 6, far right). The ∼100-fold differential effect with or without D153 and K328 indicates that the Mg2+ ion, D153, and K328 form a unit that is functionally separate from the catalytic contributions of the D101/R166/D153 unit.

Nevertheless, the two functional units are interconnected as they have D153 in common. From a functional perspective, given the close quarters within an active site, even if fully independent functional units were readily obtainable, interconnected units might still be preferable to allow a compact active site that can accommodate the density of groups needed to provide multiple interactions with centrally located substrates and thus optimal catalysis. From an evolutionary perspective, parsimony in natural selection might be expected to lead to multiple uses of the same residue, such that one residue could serve in two functional units, and one functional unit might serve as a foundation or scaffold from which to build other functional units, thereby leading to interconnected functional units. This idea is related to a proposal of Hanson and Rose that natural selection favors the use of the minimal number of acidic and basic residues in active sites, so that such residues tend to be reused when mechanistically reasonable (Hanson and Rose, 1975).

Whereas AP in its fully evolved form has functionally distinct D101/R166/D153 and D153/Mg2+/K328 units (i.e., these functional units do not provide an additional advantage to one another), mutations that disrupt the surrounding AP scaffold could alter these energetics and possibly render these units energetically interdependent (Narlikar and Herschlag, 1998; Kraut et al., 2003). Such mutations may have been present during the early evolution of the AP active site, when its scaffold may have been less precisely arranged.

#### The D101/Mg2+(E322) functional unit

Given the absence of direct connections between the active site Mg2+ or K328 and D101 and the above findings of circumscribed functional units, we initially expected that there would be no interactions between D101 and these groups. Data analogous to that of Figures 4, 6 probing the dependence of the K328 contribution with or without D101 confirmed this expectation for K328 (Figure 8—figure supplement 1). However, a connection was observed between D101 and the Mg2+ ion. Addition of D101 when the Mg2+ ion is not present leads to a ∼20-fold rate increase (Figure 7A); in contrast, there is no increase when Mg2+ is present (Figure 7B). Figure 7A,B shows only cases in which R166 is not present because D101 enhances the potency of R166 as part of the D101/R166/D153 functional unit (Figure 4); nevertheless, the interconnection of D101 with R166 and the Mg2+ ion are distinct, as the enhancement by D101 of the R166 contribution is the same with and without the Mg2+ ion present (Figure 4). Together, these results indicate that D101 has a stimulatory effect independent of R166, but only when the Mg2+ ion is not present.

![Figure 7.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig7-v2.jpg)

**Figure 7.:** The effects of restoring D101 in backgrounds without bound Mg2+ (A) and with bound Mg2+ (B). The arrow indicates that the ratio is a lower limit. Residues are color-coded as in Figure 1, rate constants are from Table 1, and mutations made are listed in Table 1. R166 is absent because it is also coupled with D101 (Figure 4).

To further explore coupling between D101 and the Mg2+ ion, we plotted the effect of adding the Mg2+ ion with or without D101 present (Figure 8). The effect from the added Mg2+ ion varies depending on whether D153 and K328 are present, as described in the preceding section, but in each case the effect is diminished if D101 is present. Mirroring the larger effect from D101 addition in the absence of Mg2+, addition of the Mg2+ ion had a 30-fold larger effect in the absence of D101.

![Figure 8.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig8-v2.jpg)

**Figure 8.:** The effects of restoring Mg2+ in the absence of D101 (light blue) and the presence of D101 (dark blue). Residues are color coded as in Figure 1, rate constants are from Table 1, and mutations made are listed in Table 1.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** The effect of adding K328 is the same, within approximately twofold, whether D101 is present, indicating that these residues are essentially independent of one another.

Thus, D101 and the Mg2+ ion form a third functional unit, with energetic behavior distinct from the other two units. In the D101/R166/D153 functional unit, R166 has close to energetically additive effects from the neighboring aspartate residues, and the Mg2+ functional unit (D153/Mg2+/K328) exhibits cooperative energetic effects from K328 and D153. In contrast, the Mg2+ ion and D101 are energetically anti-cooperative, with a 20–30-fold contribution from each occurring only when the other group is absent.

These observations raise two questions addressed immediately below: (1) how are D101 and the Mg2+ ion functionally linked, and (2) what is the origin of their anti-cooperative energetics?

##### How are D101 and the Mg2+ ion functionally linked?

Consideration of the AP active site structural network reveals potential linkages between D101 and the Mg2+ ion. They are linked via R166 and D153 (Figure 1C), but these residues have no effect on the energetic coupling between D101 and the Mg2+ ion, so models involving these residues and this connection are ruled out. A second structural connection between D101 and the Mg2+ ion can be traced as follows: D51 is a ligand of both the Mg2+ ion and the Zn2+ ion that coordinates the nucleophilic oxyanion of S102 ($Zn_{2}^{2+}$), and D101 is directly upstream of S102, with its side chain anchored to the backbone amide of S102 (Figure 1C).

##### What is the origin of their anti-cooperative energetics?

Given this connection, why are these energetically anti-cooperative—that is, how is a favorable effect from each residue prevented or obviated by the presence of the other residue? A model that D101 and the Mg2+ ion can each make a catalytic interaction alone that is prevented by a steric block or conformational rearrangement upon addition of the other residue would require fortuitous catalytic interactions present in mutant enzyme forms that are not maintained in WT and is therefore unlikely. A more appealing model is the one in which the two residues have a redundant effect, such that either residue can alone provide a rate advantage through the same mechanism. Given that D51 is a ligand of both the Mg2+ ion and the Zn2+ ion that coordinates the nucleophilic oxyanion of S102 ($Zn_{2}^{2+}$, Figure 1B,C), the Mg2+ ion could help position the serine oxyanion with respect to the rest of the catalytic apparatus (Figure 1C). D101 is directly upstream of S102 with its side chain anchored to the backbone amide of the S102. Thus, it is possible that either D101 or Mg2+ interactions can facilitate proper positioning of the S102 oxyanion for nucleophilic attack and that, once either of the two interactions is made, positioning is optimized such that no further functional enhancement occurs upon addition of the second (Figure 1C).

##### Active site redundancy

As described above, our energetic data indicate that there is a redundant effect of the Mg2+ ion and D101. Redundancy is often observed in functional studies from the molecular to the cellular to the organismal level (Peracchi et al., 1998; Naor et al., 2005), but its origins are less clear. It is sometimes suggested that more ‘important’ pathways or functions evolve redundancy, but more complex mechanisms are required to maintain redundancy, otherwise it would simply be lost over evolution (Cookea et al., 1997). One intriguing idea is that redundancy is built to aid evolvability, and evolvability itself is a property that has been selected for over evolution (Maynard Smith, 1978; Conrad, 1979; Joyce, 1997). It is also possible that many reported cases of redundancy have individual functional effects that are too small to be detected in laboratory assays or have favorable functional effects that manifest only under natural growth conditions.

We propose a distinct origin of the D101/Mg2+ redundancy, arising from the high degree of connectivity within the AP active site. D101 and the Mg2+ ion are each involved in other functional networks and are embedded in an extensively interwoven active site. These interconnections presumably position functional groups to make optimal catalytic interactions. As noted above, the functional networks overlap with one another that is, have shared residues (Figure 9), and these overlaps may have arisen as evolution co-opted residues within active sites as anchor points for positioning new residues. Given the high density of functional groups within active sites and the presumed need for multiple interconnections to provide optimal positioning of functional groups for transition state interactions, residues that evolved for different functional purposes may end up structurally linked and with the ability to position the same group or groups.

![Figure 9.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig9-v2.jpg)

**Figure 9.:** The residues of the functional unit are color-coded as in Figure 1. For the D101/Mg2+ functional unit (left), the black residues and Zn2+ ion represent a potential route for the energetic connections between these residues.

### Conclusions and implications

X-ray crystallographic structures reveal connections between residues but cannot define the energetic properties of these connections. Site-directed mutagenesis reveals residues that give large functional effects upon mutation, and double mutant cycles provide powerful tests for energetic dependence vs independence between two residues (Carter et al., 1984; Hertel et al., 1994; Horovitz, 1996; Narlikar et al., 1999). However, residues never function in isolation, and essentially every residue in a protein structure can be connected, via chains of hydrogen bonding and packing interactions, to every other residue. In cases of allostery, there are energetic interactions over large distances, and in certain cases the residues and conformations involved in the allosteric transition have been mapped (Monod et al., 1965; Shulman et al., 2004; Cui and Karplus, 2008; McLaughlin et al., 2012). We are particularly interested in active site networks because the residues constituting these networks are critical for the most basic catalytic functions of enzymes, these networks have not been previously mapped, and an understanding of their extent and properties may facilitate engineering of enzymes that rival natural enzymes in catalytic efficiency and specificity.

### Active site networks and functional units

We have interrogated a network of five residues in the active site of the model enzyme AP (Figure 1B,C; Figure 2A). A priori, these residues could have functioned fully cooperatively or fully independently. Although either extreme might have been considered unlikely, there were no data for this system (or, to our knowledge, other systems) that would allow us to know or predict the degree and extent of functional interconnectivity.

We observed three overlapping functional units, D101/R166/D153, D153/Mg2+/K328, and D101/Mg2+ (Figure 9). Each functional unit exhibited distinct energetic behaviors. The aspartate residues of the D101/R166/D153 unit make nearly independent contributions to the catalytic function of the central arginine residue; D153 and K328 (and presumably their associated water molecules) act cooperatively with the Mg2+ ion and increase its contribution to catalysis; and the Mg2+ ion and D101 are energetically anti-cooperative and apparently constitute a redundant functional unit.

A mathematical model that describes these energetics quantitatively accounts for all of the AP variants, reproducing the observed catalytic rates for all 28 mutants within a factor of two and predicting the catalytic rates of the remaining four variants that were not tested herein (Appendix 1 Table 2). Nevertheless, the atomic-level interactions and properties that underlie each of these distinct and complex energetic behaviors are not known. We propose the following models: each aspartate residue of the D101/R166/D153 unit helps to position R166, thereby lowering the conformational entropy cost for making its interactions with the two phosphoryl oxygen atoms; the network of the D153/Mg2+/K328 functional unit and its two associated water molecules exists in alternative, likely less structured conformations until all three of these groups are present and can position hydrogen bond donors to one of the oxygen atoms of the transferred phosphoryl group; and D101 and the Mg2+ ion can each position the serine oxyanion nucleophile with respect to $Zn_{2}^{2+}$, rendering their contributions redundant. These models will require future testing and refinement.

The interconnections between the functional units (Figure 9)—that is, the residues common to more than one functional unit—may be favored both evolutionarily and functionally. An interconnected active site will have fewer residues and thus require a less expansive search of mutational space. Further, multiple functional groups need to ‘pack’ into a limited space to interact with the substrate and stabilize the transition state.

### Synergy between experimental and computational enzymology

The approach taken in this study introduces a powerful opportunity to deepen the feedback loop between experiment and computation. It is generally recognized that the most powerful tests of computational approaches are true predictions, made ‘blindly’ with pertinent data not yet collected or obtained by others but not released prior to reporting computational results and predictions. Such blind predictions have proven critical in other areas of biochemistry and biophysics to determine whether seemingly predictive and descriptive algorithms were indeed predictive and correct (Moult et al., 2004, 2011; Nielsen et al., 2011; Cruz et al., 2012; Dill and MacCallum, 2012). Nevertheless, the vast majority of computational studies of enzyme mechanism make ‘predictions’ for results that are already known and are thus not true independent tests. Further, single active site mutations predominantly give effects that fall within typical and rather narrow ranges, limiting the usefulness of traditional site-directed mutagenesis as a robust test of computational approaches.

We suggest that computational predictions of the rate effects from multiple mutations may provide extensive and nontrivial predictions that can be quantitatively tested by experiment and that are needed to effectively advance computational methods and our understanding. Our group is willing to test predictions from individual computational groups or consortia, using AP or other systems where we know robust kinetic measurements are possible; we are willing to carry out such experiments in advance and withhold the results or send them to an independent evaluator to ensure that comparisons between experiment and computation will be possible and made in a timely manner; and we are willing to discuss with computational groups the best systems to carry out such tests. We strongly believe that such synergistic approaches, informal and formal, will be required to unite computational and experimental enzymology and to make the greatest advances in our understanding of catalysis.

### Enzyme design

There has been recent excitement about the ability to design new enzymes, some of which catalyze reactions not seen in nature (Röthlisberger et al., 2008; Siegel et al., 2010; Hilvert, 2013; Bos and Roelfes, 2014). The ability to repurpose and create protein scaffolds and to place functional groups in desired locations is a truly remarkable advance. Nevertheless, designed enzymes to-date have modest rate enhancements relative to naturally occurring enzymes and can lack the stereospecificity observed with naturally occurring enzymes (Wolfenden and Snide, 2001; Lassila et al., 2009; Baker, 2010; Bos and Roelfes, 2014). Indeed, enzyme mimics and bovine serum albumin (BSA) can catalyze reactions with rate enhancements similar to designed enzymes prior to their improvement by randomization and selection (Kirkby et al., 2000; Schmidt et al., 2013).

These observations raise the following questions: what distinguishes naturally occurring enzymes from current designed enzymes, and what is needed to achieve more proficient designs? The most apparent difference is the absence of extended and extensive hydrogen bond networks in and around active sites of designed enzymes. For example, the most carefully studied designed enzyme, a retroaldolase, has a lysine residue placed within a hydrophobic pocket (Jiang et al., 2008). Rate enhancements are achieved by lowering the lysine pKa due to its non-polar environment (to increase the concentration of the reactive free amine at neutral pH) and from binding the hydrophobic substrate in this lysine-containing pocket; these mechanisms provide ∼105-fold catalysis for a designed enzyme, with modest additional rate enhancement obtained through subsequent rounds of selection (Lassila et al., 2009; Hilvert, 2013).

We hope that an empirical understanding of the extent and properties of active site networks will help in future design efforts as well as promote more conceptual and theoretical understanding. Although it would not be appropriate to generalize from the single example of AP, our dissection of the AP active site network does show that optimal positioning of catalytic residues can occur with only a subset of the full network; thus, it may be possible to attempt designs with active site modules that correspond to functional units identified in this study and, we hope, subsequent studies. A recent attempt to incorporate an active site catalytic triad produced designed enzymes that, after several rounds of selection, were able to catalyze a side reaction with efficiencies similar to analogous natural enzymes (Rajagopalan et al., 2014). Taking a longer view, the hand-in-hand development and testing of computational approaches, as outlined above (see ‘Synergy between experimental and computational enzymology’), will ultimately provide foundational models for the efficient design of highly effective and specific new enzymes.

### Evolutionary pathways and probabilities

The evolution of a fully cooperative network would be exceedingly improbable and more difficult the larger the number of constituent residues, as all of the residues would need to arise through random drift with a selective advantage accruing only once the entire network was in place. A probability model in which each of five residues would arise with a one in twenty probability (i.e., one active residue out of the total 20 amino acids) and all are needed for a selective advantage (i.e., full cooperativity) has a probability of 1/(6.8 × 105) (Figure 10A, bottom pathway and Appendix 3). This probability arises because there are five steps (or positions) each with 20 possible residues, and there are five chances of ‘choosing’ a WT residue, starting with AP minimal with all five WT residues missing, four chances of choosing the next residue, etc.

![Figure 10.](https://cdn.elifesciences.org/articles/06181/elife-06181-fig10-v2.jpg)

**Figure 10.:** (A) Schematic comparing fully cooperative (bottom) and stepwise (top) models for a single pathway. In the fully cooperative model, simultaneous acquisition of all five WT residues is required to confer a selective advantage, leading to a mean waiting time of 4.7 × 105 (arbitrary units) considering all 120 pathways of adding in the residues (black net rates; for simplicity, only one intermediate of the multiple possible mutant combinations is shown in each step). In contrast, the stepwise model, in which acquisition of any WT residue confers a fitness advantage and is thus irreversible (top, black numbers), has a minimum mean waiting time of 32. If only one of the 120 pathways leads to a stepwise increase in fitness (top, grey numbers) then the mean waiting time would be 69. The model and simplifying assumptions made to highlight the differences arising from the presence or absence of cooperativity are described in Appendix 3. (B) Model of active site evolution showing the 120 possible paths in the AP landscape for introduction of the five residues investigated herein, in an otherwise WT background. A stepwise model in which acquisition of any WT residue is considered irreversible and all paths are possible would result in a mean waiting time of 32 (all arrows, grey and black, same as part A, top). As a subset of mutagenic steps toward WT AP (36 of the 80 potential evolutionary steps) confers a selective advantage (here defined as a rate increase of >threefold) and paths containing steps that do not confer such an advantage have much lower probabilities, we consider the 34 of 120 pathways that provide a monotonic fitness increase as all five WT residues are added. This gives a mean waiting time between the mean waiting times for the stepwise models for a single pathway and 120 pathways, 32 and 69, respectively.

Conversely, evolution of a hypothetical enzyme in which each active site residue provides an independent rate advantage would be considerably more probable, as addition of those residues would lead to monotonically increasing catalysis (i.e., be continually uphill on a fitness landscape and thus selected for after each addition). We first consider a simplified model with a single pathway of five successive steps that each lead to increased fitness, each with a one in twenty probability representing a single advantageous residue of the twenty possible residues (Figure 10A, top path, black numbers). The probability of achieving the final state for a multi-step process can be considered in terms of a mean waiting time, akin to a reaction's half-time or the inverse of its rate constant (scaled by ln 2). In this case, with five successive irreversible steps each with probability 1/20, the ‘rate constant’ is 1/100 and the mean wait time is 69 (in arbitrary units; Appendix 3). (Calculating probabilistic waiting times using a hidden Markov Model, such as is often used for probability calculations, gives the same relative values as the kinetic mean times [Appendix 3].) This kinetic mean wait time is about three orders of magnitude lower than that for the fully cooperative process, which is obtained by computing the mean waiting time: 4.7 × 105 (=6.8 × 105 × ln 2; Appendix 3). Thus, if it were functionally equally probable to obtain an active site with these different underlying energetic properties (i.e., fully cooperative vs stepwise; Figure 10A), evolution would favor the non-cooperative solution by greater than 1000-fold. In other words, for every enzyme that evolved five residues with full functional dependence on one another, there would be more than 1000 with active sites containing residues whose stepwise addition each provided a selective advantage.

As we observed functional units exhibiting a range of energetic behaviors within the AP active site, we asked the question: where does the energetic behavior of AP place it along this wide range of evolutionary probabilities? There are 120 possible pathways from AP minimal to WT AP (Figure 10B). To assess the range of possible mean waiting times, we consider two limiting cases (Figure 10A, top pathway): i. The case in which there is a single pathway of the 120 that is favorable; this is the simplified model presented above and gives a mean wait time of 69. ii. The case in which all 120 potential pathways are favorable—that is, proceed with a selective advantage at each step; in this case the mean waiting time is 32, even shorter than for case (i) because there are more ways to traverse the landscape from AP minimal to WT AP.

Because we have rate constants for each AP species (Table 1; Figure 2), we can determine which pathways would confer a selective advantage. Using an arbitrary minimal cutoff of >threefold increase in kcat/KM, 34 of the 120 pathways confer a fitness advantage; with a cut-off of a fivefold increase in kcat/KM, 28 of these pathways remain. Thus, although the AP active site residues studied herein have varied energetic behaviors, in many cases addition of a WT residue leads to a significant rate increase, providing multiple favorable evolutionary routes. While not all 120 pathways are favorable for AP, many are, and the mean waiting time will thus be within the range of 32–69, >1000-fold shorter than the expected waiting time to evolve a fully cooperative network.

Although a fully cooperative network would probably not have been anticipated, we were unaware of how strong the evolutionary pressure would be for stepwise increases in fitness. Similar conclusions have been drawn for the evolution of unlinked loci where largely additive rather than fully cooperative or synergistic effects have been observed (Arnegard et al., 2014). It will be fascinating to explore more broadly the interplay of functional effects and evolutionary probabilities and how this interplay has biased the complement of extant enzymes. Such underlying probabilistic preferences presumably also impact biological solutions at higher levels of function such as gene regulation and neuronal function (McLean et al., 2011).

### Implications for exclusion of water from active sites

Many enzymes have loops or flaps that close over active sites or domains that accomplish analogous closure (Pai et al., 1977; Bennett and Steitz, 1978; Alber et al., 1987). These events exclude solvent, and it is often stated or implied that the exclusion of water provides the underlying driving force to evolve these processes (Pai et al., 1977; Bennett and Steitz, 1978; Harris et al., 1997; Cleland et al., 1998; Richard and Amyes, 2004). However, the observation that water is excluded does not logically indicate that the exclusion of water causes enhanced catalysis.

AP has an open cavity to allow cleavage of a wide range of phosphate esters, consistent with its putative role in scavenging inorganic phosphate; nevertheless, it has one of the largest known rate enhancements, suggesting that full exclusion of water is not required to attain extremely efficient enzymatic catalysis.

AP does, however, appear to exclude water from access to the non-bridging phosphoryl oxygen atoms, and we considered whether that exclusion is catalytically important. Removal of R166 (and D101), which allows solvent access to the phosphoryl oxygen atoms (O'Brien et al., 2008) does not diminish the catalytic contribution from the Mg2+ ion or the D153/Mg2+/K328 functional unit, which also interact with at least one of these phosphoryl oxygen atoms. Thus, at least for AP, the wholesale exclusion of solvent from the active site does not enhance catalytic contributions. We suggest, most generally, that flap or domain closure allows the establishment of additional specific interactions for optimal transition state interactions while providing a route for the ingress and egress of substrates and products, rather than generic rate enhancements from solvent exclusion (Wolfenden, 1974, 1976; Alber et al., 1987; Herschlag, 1988; Pompliano et al., 1990; Herschlag, 1991).

### Closing remarks

A deeper investigation into the energetics and energetic interconnections within an active site—that of E. coli AP—has led to new knowledge, new models for catalytic effects, and a quantitative assessment of the evolutionary probability of establishing an active site network. Nevertheless, this is just one study, and it remains to be determined how similar or different the behaviors of active sites of other enzymes are. In addition, while extending beyond traditional studies, our work investigates a miniscule fraction of the possible connections and interrelationships in AP. Of particular interest will be understanding the interplay between the broader scaffold and the active site residues along with their functional roles and energetic connections, and such studies will ultimately rely on the development of methods that are high-throughput and highly quantitative.

## Materials and methods

### Protein expression and purification

WT and mutant AP were purified from a fusion construct containing an N-terminal maltose binding protein (MBP) tag and a C-terminal strepII tag with a factor Xa cleavage site between it and the natural C-terminal end of AP. D101 was mutated to alanine, R166 to serine, D153 to alanine, K328 to alanine, and the Mg2+ ion ligand E322 to tyrosine to prevent the Mg2+ from binding in the active site; these mutations were made alone and in combination. To test for idiosyncratic effects, mutations to alternative residues were tested (Appendix 1 Table 1).

E. coli SM547(DE3) cells were transformed with the MBP-AP-strepII constructs and were grown to an OD600 of 0.6 in rich media and glucose (10 g of tryptone, 5 g of yeast extract, 5 g of NaCl, and 2 g of glucose per liter) with 50 µg/ml of carbenicillin at 37°C. IPTG was added to a final concentration of 0.3 mM to induce protein expression. Cultures were then grown at 30°C for 16–20 hr.

Cells were harvested from 2 l culture by centrifugation at 4400×g for 20 min and lysed with osmotic shock. The cell pellet was resuspended in 800 ml 20% sucrose solution (30 mM Tris-HCl, pH 8.0, 1 mM EDTA) and incubated at room temperature for 10 min on a shaking table. The cells were pelleted by centrifugation at 13,000×g for 10 min. The pelleted cells were resuspended in 800 ml ice cold water at 4°C. The cells were incubated on a shaking table at 4°C for 10 min and then pelleted at 13,000×g for 20 min. The supernatant was adjusted to 10 mM Tris-HCl, pH 7.4, 200 mM NaCl, and 10 µM ZnCl2. The sample was then passed over a 10 ml amylose resin (New England BioLabs, Ipswich, MA) gravity column. All mutants were purified with fresh amylose resin to prevent inadvertent co-purification with other mutants. The amylose column was washed with 10 column volumes of 10 mM Tris-HCl, pH 7.4, 200 mM NaCl, and 10 µM ZnCl2 and eluted with the same buffer supplemented with 10 mM maltose. Protein-containing fractions were concentrated by centrifugation through a 10 kDa cutoff filter (Amicon) and buffer exchanged at least twice into 10 mM sodium MOPS, pH 7.0, 50 mM NaCl, 100 µM ZnCl2, 1.0 mM MgCl2 unless the E322Y mutation was present, in which case MgCl2 was omitted.

For all enzymes, purity was determined to be >95% by SDS-PAGE gel electrophoresis based on staining with Coomassie Blue. To further test for a possible contaminant and to determine the reproducibility of the results, nine out of the 28 mutants were re-expressed and re-characterized: K328A, R166S, E322Y, D101A/D153A, D101A/E322Y, R166S/K328A, D101A/D153A/R166S, D153A/R166S/E322Y/K328A, and D101A/D153A/R166S/E322Y/K328A. Independent preparations gave activities within twofold of one another. To most strongly test whether the observed activities might arise from an enzyme contaminant, the construct with all five residues mutated was further mutated by removal of the serine nucleophile (to give S102G/D101A/D153A/R166S/E322Y/K328A AP). This mutant had no measurable activity above background and a reaction rate at least 100-fold lower than that for any of the AP mutants reported herein, suggesting that the observed activities do not arise from a contaminant.

To control for potential unintended complications specific to the mutant residue introduced, several additional mutations were tested (Appendix 1 Table 1). The values of kcat/KM with mutations to different residues were within twofold in all cases. Alternative AP variants investigated from previous papers are also added to the table and have similar efficiencies.

### Kinetic assays

Activity measurements were performed in 0.1 M MOPS, pH 8.0, 0.5 M NaCl, 100 µM ZnCl2, and 500 µM MgCl2 at 25°C in a UV/Vis Lambda 25 spectrophotometer (Perkin Elmer, Waltham, MA), unless otherwise noted; for mutants containing E322Y, MgCl2 was excluded. The formation of free p-nitrophenolate from hydrolysis of the substrate p-nitrophenol phosphate (pNPP) was monitored continuously at 400 nm.

Rate constants were determined from initial rates, and the activity of the free enzyme, kcat/KM, was determined. (Rate measurements were limited to kcat/KM measurements because kcat for WT represents dissociation of product rather than a chemical step and because the rate-limiting step for kcat could vary with mutation. We ensured that the chemical step was rate limiting for the kcat/KM comparisons carried out herein, as described in Table 3 and described in Appendix 1.)

**Table 3.**
 Kinetic constants for Me-P hydrolysis


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">kcat/KM (M−1s−1)</th>
    </tr>
    <tr>
      <th>AP mutant</th>
      <th>pNPP</th>
      <th>Me-P</th>
      <th>(kcat/KM)pNPP(kcat/KM)Me-Pi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">WT*,†</td>
      <td>3.3 × 107</td>
      <td>1.2 × 106</td>
      <td>28</td>
    </tr>
    <tr>
      <td></td>
      <td>3.5 × 105</td>
      <td>80</td>
    </tr>
    <tr>
      <td rowspan="2">R166S†</td>
      <td>1.0 × 105</td>
      <td>110</td>
      <td>910</td>
    </tr>
    <tr>
      <td></td>
      <td>56</td>
      <td>1800</td>
    </tr>
    <tr>
      <td>E322Y‡</td>
      <td>7.2 × 103</td>
      <td>1.6</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>D101A</td>
      <td>9.9 × 106</td>
      <td>2.7 × 103</td>
      <td>3600</td>
    </tr>
    <tr>
      <td>D153A</td>
      <td>2.8 × 106</td>
      <td>1.1 × 103</td>
      <td>2500</td>
    </tr>
    <tr>
      <td>D101A/D153A</td>
      <td>3.3 × 105</td>
      <td>61</td>
      <td>5400</td>
    </tr>
  </tbody>
</table>

_*(kcat/KM)obsd; the chemical step is not rate limiting.†Values of kcat/KM of 1.2 × 106 M−1s−1 and 110 M−1s−1 for WT and R166S, respectively for Me-P was obtained previously from reference (O'Brien and Herschlag, 2002; O'Brien et al., 2008). This difference in value would not affect the conclusions herein.‡From reference (Zalatan et al., 2008).The efficiency of Me-P hydrolysis was measured for mutants with pNPP activities close to the rate of diffusion. The ratios measured for the enzyme with pNPP and Me-P were close to what had been measured previously for R166S and E322Y, two mutants for which chemistry is rate limiting for both substrates. The ratios suggest that chemistry is rate limiting for the pNPP hydrolysis in D101A and D153A._

At least two different enzyme concentrations and at least seven different substrate concentrations were used for each enzyme. Enzyme concentrations were varied by at least fivefold, and substrate concentrations were extended to at least fivefold below the KM value for each enzyme based on KM values determined over wider ranges of substrate. Reaction rates were linear in enzyme concentration at each substrate concentration for each enzyme, and no reaction was observed without added enzyme. Values of kcat/KM determined from linear fits to the lowest substrate concentrations were the same, within error, as values determined from full Michaelis–Menten fits, and R2 values were >0.98 in all cases. For E322Y AP and D153A/E322Y, because of their very low KM (∼0.5 µM), kcat/KM was determined from rate measurements in the presence of inhibitory Pi and the independently measured inhibition constant of Pi using an alternative, high KM substrate, as described previously (Zalatan et al., 2008).

Errors were estimated from two independent kinetic measurements, and comparisons with independent enzyme preparations for nine of the AP variants gave the same values and similar error estimates as the same preparation used on separate days.

All mutants were incubated at room temperature for at least a week to test for Zn2+ activation. The E322Y mutants exhibited time-dependent Zn2+ activation, as observed previously, and were shown to level to a maximal rate (Zalatan et al., 2008). Mutants with E322 not mutated were incubated in storage buffer with Mg2+ added (10 mM sodium MOPS, pH 7.0, 50 mM NaCl, 100 µM ZnCl2, 1 mM MgCl2). To test for kinetic effects arising from decreased metal affinity of the mutants compared to WT, mutants R166S, D101A/R166S/D153A/K328A, D101A/D153A, E322Y, D101A/R166S/D153A/E322Y/K328A, and D101A/R166S were also incubated with varying Zn2+ and Mg2+ concentrations for a week. The following metal ion concentrations were used in the incubation experiment: 100 µM ZnCl2; 1.0 mM ZnCl2; 100 µM ZnCl2 and 100 µM MgCl2; 100 µM ZnCl2 and 1.0 mM MgCl2; 100 µM ZnCl2 and 10 mM MgCl2; 1.0 mM ZnCl2 and 10 mM MgCl2. Only AP mutants with E322Y exhibited time-dependent activation, as observed previously (Zalatan et al., 2008); the Mg2+ concentration did not affect the Zn2+ activation; and the activities of the E322Y mutants were not dependent on the presence of Mg2+. The activities of mutants R166S, D101A/R166S/D153A/K328A, D101A/D153A, and D101A/R166S do not increase with higher concentrations of Mg2+.

Phosphate monoester hydrolysis by D101A, D153A, R166S, and D101A/D153A AP was also measured with methyl phosphate (Me-P), using the same reaction buffer and conditions as for pNPP. The formation of the inorganic phosphate (Pi) product from Me-P hydrolysis was monitored discontinuously by withdrawing aliquots from ongoing reactions, quenching in 6 M guanidine-HCl, and detecting Pi with a modified Malachite Green assay (Lanzetta et al., 1979) at eight or more specified times. Rate constants were determined from initial rates, and activity of the free enzyme, kcat/KM, was determined. At least two different enzyme concentrations and at least seven different substrate concentrations were used for each enzyme. Enzyme concentrations were varied by at least fivefold, and substrate concentrations were extended to at least fivefold below the KM value for each enzyme based on KM values determined over wider ranges of substrate. Reaction rates were linear in enzyme concentration at the lowest substrate concentration for each enzyme, and no reaction was observed without added enzyme. R2 values were >0.98 in all cases.

### Test of Mg2+ occupancy

To test if the most mutated AP mutant, AP minimal (D101A/R166S/D153A/E322Y/K328A), had Mg2+ in the active site and full Zn2+ occupancy, we carried out atomic emission spectroscopy, as previously used for the E322Y single mutant, with the AP minimal mutant (Zalatan et al., 2008). The metal ion occupancies were consistent with an active site saturated with Zn2+ and lacking Mg2+ (Zn2+:protein ratio 2.49; Mg2+: protein ratio 0.01; Pi: protein ratio 0.06). As described above, kinetic experiments were also carried out to test for Mg2+ activation.

### Crystallization and structure determination

The MBP tag used for purifying D101A/D153A was cleaved with factor Xa, and the enzyme was separated from the tag over a 5 ml HiTrap Q HP column (GE Healthcare, Amersham, UK). The purified enzyme was buffer exchanged into 10 mM sodium Tris, pH 7.0, 50 mM NaCl, and 100 µM ZnCl2 and concentrated to 5.1 mg/ml. Equal volumes of enzyme and precipitant solution (22% PEG3350, 0.1 mM Bis-Tris, pH 5.0, 0.2 mM ammonium sulfate) were mixed and placed over a reservoir of 1 ml precipitant solution to crystalize by the hanging drop method. No inorganic phosphate (Pi) was added to the precipitant solution, but 0.8 mM contaminating Pi was found in the crystallization solution using a Malachite Green assay (Lanzetta et al., 1979). Crystals were soaked in a cryoprotectant solution of 30% glycerol, 0.1 mM Bis-Tris, pH 5.0, and 0.2 mM ammonium sulfate prior to being frozen in liquid nitrogen. Crystallographic data were collected at the Stanford Linear Accelerator at beamline 11-1.

The D101A/D153A mutant of AP crystallized in space group P6322 with one dimer per asymmetric unit. Data were integrated with MOSFLM (Battye et al., 2011) and scaled and merged with AIMLESS (Evans and Murshudov, 2013). Five percent of reflections were set aside for calculation of Rfree. Molecular replacement was performed with PHASER (McCoy et al., 2007) using WT AP (PDB 3TG0) stripped of phosphate and metal ions as a search model. Rounds of alternating manual and automated refinement were performed with COOT and REFMAC5, respectively (Emsley et al., 2010; Murshudov et al., 2011). Stereochemistry was assessed with MOLPROBITY, and images were generated with PYMOL (Schrödinger, 2010). The PDB deposition ID is 4YR1.
