# The selectivity of the Na+/K+-pump is controlled by binding site protonation and self-correcting occlusion

## Authors

- Huan Rui<sup>1</sup> ([ORCID: 0000-0002-6459-9871](https://orcid.org/0000-0002-6459-9871))
- Pablo Artigas<sup>2</sup>
- Benoît Roux<sup>1</sup> ([ORCID: 0000-0002-5254-2712](https://orcid.org/0000-0002-5254-2712)) †

### Affiliations

1. Department of Biochemistry and Molecular Biology The University of Chicago Chicago United States
2. Department of Cell Physiology and Molecular Biophysics Texas Tech University Health Sciences Center Lubbock United States

† Corresponding author

## Abstract

The Na+/K+-pump maintains the physiological K+ and Na+ electrochemical gradients across the cell membrane. It operates via an 'alternating-access' mechanism, making iterative transitions between inward-facing (E1) and outward-facing (E2) conformations. Although the general features of the transport cycle are known, the detailed physicochemical factors governing the binding site selectivity remain mysterious. Free energy molecular dynamics simulations show that the ion binding sites switch their binding specificity in E1 and E2. This is accompanied by small structural arrangements and changes in protonation states of the coordinating residues. Additional computations on structural models of the intermediate states along the conformational transition pathway reveal that the free energy barrier toward the occlusion step is considerably increased when the wrong type of ion is loaded into the binding pocket, prohibiting the pump cycle from proceeding forward. This self-correcting mechanism strengthens the overall transport selectivity and protects the stoichiometry of the pump cycle.

## Introduction

The Na+/K+-pump is a primary active membrane transporter present in nearly all animal cells. It belongs to the P-type ATPase family, which utilizes the energy released from ATP hydrolysis to move ions against their concentration gradients across a membrane barrier. The ion species transported by the pump under physiological conditions are Na+ and K+. Like many other membrane transporters, the Na+/K+-pump works according to an 'alternating-access' ion transport mechanism, with the bound ions accessible from only one side of the membrane at a time. The consensus scheme of the pump cycle is known as the 'Albers-Post' cycle (Albers, 1967; Post et al., 1969). It involves two major conformations, E1 and E2, with inward- and outward-facing ion binding sites, respectively. In each cycle, the E1 conformation binds three Na+ from the cytosol and exports them using the energy from ATP hydrolysis. After external release of Na+, binding of extracellular K+ promotes the structural transition to the occluded E2 state, which finally imports two K+ as binding of ATP returns the pump to the E1 conformation. E1/E2 conformational change and the accompanied electrogenic active transport are facilitated by the phosphorylation and dephosphorylation of an aspartate residue in the cytoplasmic domain, which is a hallmark of the P-type ATPase family (Axelsen et al., 1998).

The presence of the Na+/K+-pump is essential for excitability and secondary active transport. More than 40% of the energy produced in mammals is consumed by the Na+/K+-pump (Milligan et al., 1985). Although it is a machine designed for such a precise and important function, it has been shown that many cations, including congeners of K+ and some organic cations, can bind to the same sites used by the pump to bind and transport K+ ions (Mahmmoud et al., 2015; Ratheal et al., 2010). Competitive binding between Na+ and other cations at the cytoplasmic side of the membrane has also been observed (Schneeberger et al., 2001). An unsolved puzzle, therefore, is how the Na+/K+-pump is able to recognize and accept two K+ from the extracellular matrix, where Na+ concentration is much higher, and how it selectively binds Na+ from the cytoplasm to keep the pump cycle running forward.

Structural studies have provided tremendous insights into the function of the Na+/K+-pump, which consists of two obligatory subunits, α (catalytic) and β (auxiliary), and sometimes a tissue specific regulatory subunit from the FXYD protein family (Geering, 2006; Mercer et al., 1993). The transmembrane region of the α-subunit contains the ion binding sites within its 10 helices (called M1-M10). Recent crystal structures of the pump in its E1 and E2 states reveal the locations of the three Na+ binding sites in E1 and the two K+ binding sites in E2 (Kanai et al., 2013; Laursen et al., 2013; Morth et al., 2007; Shinoda et al., 2009). From structural alignments based on the heavy atom positions in the binding sites, it becomes clear that the binding pocket harboring sites I and II in E1 overlaps with those in E2 (Figure 1). Site III is only formed in E1. It is located between the transmembrane helices M5, M6, and M8 and is thought to exclusively bind Na+ but appears to catalyze H+ transport (Poulsen et al., 2010; Ratheal et al., 2010) in a manner that presents a complex dependence on the concentrations of Na+, K+, and H+ (Mitchell et al., 2014). Previous studies have indicated that protonation at the ion binding pocket may play a role in the selectivity of these sites for K+ when the pump is in its E2 state (Yu et al., 2011). Biochemical assays on the mutant D926N, which is often used as a surrogate for protonated D926, also show that it induces distinct effects on Na+ and K+ binding (Einholm et al., 2010; Jewell-Motz et al., 1993), suggesting a potential change in its protonation state upon the E1/E2 transition. Taken together, the evidence, although indirect, suggests the possibility of an E1 specific protonation state that favors Na+ binding to the pump. The nature of this protonation state is, however, unclear.

![Figure 1.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig1-v2.jpg)

**Figure 1.:** Only the transmembrane helices M4, M5, M6, M8, and M9 from the α subunit are shown. Residues in the binding site are highlighted in stick presentation with those protonatable colored in yellow. Na+ (yellow) and K+ (magenta) ions are in spheres. The binding site number indices are presented on top of the ions. The view is from the extracellular side towards the intracellular side. The figure is produced with PyMOL (DeLano, 2002).

In the present study, we started with the recently published crystal structure of the Na+/K+-pump in a partially occluded Na3·E1(ADP·Pi) state and used molecular dynamics (MD) simulations to show that there is a correlation between the binding pocket protonation and the Na+ selectivity in E1. The binding sites in Na3·E1(ADP·Pi) were tested one by one by 'alchemically transforming' the bound Na+ into a K+ while keeping the other two sites occupied by Na+. A similar approach was previously used to study the selectivity in other conformational states of the pump (Yu et al., 2011) (see also Materials and methods section). The results show that the Na+ selectivity at all three sites is realized only when a specific set of binding pocket residues are protonated. This set of residues is, by comparison, different from that in the K+ selective E2 state. The implication is that the protonation state and the selectivity of the pump are tightly coupled; when the pump undergoes a transition between E1 and E2, a protonation state switch occurs. The present findings also show that the effective selectivity of the pump is reinforced by a self-correcting mechanism, which prevents the occlusion step on either side of the membrane if the wrong type of ions were loaded into the binding sites. This mechanism ensures that counterproductive transport cycles do not occur.

## Results

### pKa of the binding pocket protonatable residues

The crystal structures of the pump in its E1 (PDBID 3WGV [Kanai et al., 2013]) and E2 (PDBID 2ZXE [Shinoda et al., 2009]) conformations show that there is a large structural overlap between the Na+ and K+ binding pockets. The sites I and II are in the main binding chamber formed by helices M4, M5, and M6, while site III, located in between M5, M6, and M8 (Figure 1), is Na+ exclusive and appears in E1 only. The coordination of Na+ and K+ at sites I and II are similar. Many residues are found to coordinate both Na+ and K+ at these two sites in E1 and E2 (Table 1). Although the structural difference between the ion binding pockets in E1 and E2 may not be particularly large, the local physicochemical environment can display considrable variations. In particular, the latter could affect the pKa and the protonation states of the six protonatable residues in the binding pocket (Figure 1). Their pKa values calculated using PROPKA3.1 (Olsson et al., 2011) are listed in Table 2.

**Table 1.**
 Atoms coordinating the binding site ions in the crystal structures and from the MD simulations. O is the backbone carbonyl oxygen atom. OG and OG1 are the hydroxyl oxygen atoms in serine and threonine. OD1 and OD2 are the carboxyl oxygen atoms in asparate. OE1 and OE2 are the carboxyl oxygen atoms in glutamate. OH2 is the water oxygen.


<table>
  <thead>
    <tr>
      <th rowspan="2">E1</th>
      <th colspan="4">Site I</th>
      <th colspan="4">Site II</th>
      <th colspan="4">Site III</th>
    </tr>
    <tr>
      <th colspan="2">x-ray</th>
      <th colspan="2">MD</th>
      <th colspan="2">x-ray</th>
      <th colspan="2">MD</th>
      <th colspan="2">x-ray</th>
      <th colspan="2">MD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>A323</td>
      <td>O</td>
      <td>T772</td>
      <td>OG1</td>
      <td>V322</td>
      <td>O</td>
      <td>E779</td>
      <td>OE1</td>
      <td>Y771</td>
      <td>O</td>
      <td>Y771</td>
      <td>O</td>
    </tr>
    <tr>
      <td></td>
      <td>E779</td>
      <td>OE1</td>
      <td>T772</td>
      <td>O</td>
      <td>V325</td>
      <td>O</td>
      <td>D804</td>
      <td>OD1</td>
      <td>T774</td>
      <td>O</td>
      <td>T774</td>
      <td>O</td>
    </tr>
    <tr>
      <td></td>
      <td>D808</td>
      <td>OD1</td>
      <td>N776</td>
      <td>OD1</td>
      <td>E327</td>
      <td>OE2</td>
      <td>D808</td>
      <td>OD1</td>
      <td>Q923</td>
      <td>OE1</td>
      <td>Q923</td>
      <td>OE1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>D808</td>
      <td>OD1</td>
      <td>D804</td>
      <td>OD1</td>
      <td>Water</td>
      <td>OH2</td>
      <td></td>
      <td></td>
      <td>D926</td>
      <td>OD1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>D808</td>
      <td>OD2</td>
      <td>Water</td>
      <td>OH2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 2.**
 pKa values of binding site titratable residues calculated from the crystal structures. The crystal structure resolution is given below the PDB ID.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">E1</th>
      <th colspan="2">E2</th>
    </tr>
    <tr>
      <th></th>
      <th>3WGV 2.8 Å</th>
      <th>4HQJ 4.3 Å</th>
      <th>2ZXE 2.4 Å</th>
      <th>3B8E 3.5 Å</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>D804</td>
      <td>5.9(6.2)*</td>
      <td>11.1 (11.2)</td>
      <td>3.7</td>
      <td>0.8 (2.1)</td>
    </tr>
    <tr>
      <td>D808</td>
      <td>3.5(3.1)</td>
      <td>3.7 (3.7)</td>
      <td>5.8</td>
      <td>6.8 (6.6)</td>
    </tr>
    <tr>
      <td>D926</td>
      <td>6.4(7.2)</td>
      <td>5.6 (5.6)</td>
      <td>8.9</td>
      <td>7.4 (8.4)</td>
    </tr>
    <tr>
      <td>E327</td>
      <td>11.0(11.3)</td>
      <td>5.7 (5.6)</td>
      <td>8.3</td>
      <td>10.8 (9.9)</td>
    </tr>
    <tr>
      <td>E779</td>
      <td>9.9(8.4)</td>
      <td>7.4 (7.3)</td>
      <td>10.7</td>
      <td>9.6 (8.0)</td>
    </tr>
    <tr>
      <td>E954</td>
      <td>9.6(9.7)</td>
      <td>9.2 (9.2)</td>
      <td>10.3</td>
      <td>10.7 (10.3)</td>
    </tr>
  </tbody>
</table>

_*If two chains are present in the same asymmetric unit, the pKa of the same residue in the other chain is shown inside the parenthesis._

It is important to note that the pKa values calculated with empirical methods like PROPKA are sensitive to local structural perturbations. Even when the structures assume the identical conformational state and are taken from the same asymmetric unit from a crystal, the pKa values of the same residue can differ by more than one pH unit. For example, the pKa of E779 is 9.9 in chain A of the crystal structure 3WGV but the value is 8.4 in chain C, yet, the structural difference between the two chains is minimal (Table 2). Because of this, only the structures with the highest resolution for the E1 and E2 states of the pump, 3WGV and 2ZXE, were used to guide the protonation state assignments in order to avoid false assignments of protonation state originated from structural uncertainty in lower resolution crystal structures. Interestingly, the protonation states of E327 and D804 assigned based on the 3WGV and 4HQJ structures are reversed. According to the PROPKA results, E327 appears to be deprotonated and D804 protonated in 3WGV, and vice versa in 4HQJ. While this inconsistency could be due to the lower resolution in the crystal structure of 4HQJ, it is worth noting that these two residues are in close proximity from one another suggesting that a proton could be passed back and forth between them in the E1 state.

### Protonation states and E1 binding pocket stability

Previous calculations have indicated that a specific set of residues has to be protonated for the E2 binding sites to be K+ selective (Yu et al., 2011). Although the protonation states of D926 and E954 were not considered in the previous study because they lie outside of the two K+ binding sites, they are likely to be protonated in E2 according to the predicted pKa (Table 2). The binding pocket protonation derived from the crystal structure of the pump in its partially occluded Na3·E1(ADP·Pi) state differs from that in E2. According to their pKa values, D804, D808, and D926 should be deprotonated and the glutamates, E327, E786, and E954, should be protonated. Arguments based on pKa values predicted by PROPKA, however, have to be taken with caution, because the empirical method is highly sensitive to the local structural variation. For example, a deprotonated acidic side chain could have a PROPKA predicted pKa value at slightly higher than 7 because of the structural snapshot used to make the prediction. To seek a more robust assessment of these factors, molecular dynamics (MD) simulations were conducted to examine the structural stability of the binding pocket for different protonation configurations. One goal is to determine the protonation states of D804 and D926, both of which have a predicted pKa value within 1.5 pH unit to 7. The protonation state of D808 was also investigated since it affects the K+ selectivity of the binding sites in the E2(K2) state. A total of eight MD simulations were carried out (Table 3), starting from all possible protonation state configurations accessible by these three residues. The protocol for setting up these systems is given in details in the Materials and methods section.

**Table 3.**
 Summary of the all-atom simulation systems and the FEP/H-REMD reduced systems. The binding site residues E327, E779, and E954 were kept protonated in all the systems.


<table>
  <thead>
    <tr>
      <th>Systems</th>
      <th colspan="3">Binding site residues</th>
      <th colspan="2">Simulation time (ns)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td colspan="3"></td>
      <td>MD</td>
      <td>FEP/H-REMD</td>
    </tr>
    <tr>
      <td>Wildtype</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S0</td>
      <td>D804-</td>
      <td>D808-</td>
      <td>D926-</td>
      <td>140</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E1_S1</td>
      <td>D804p</td>
      <td>D808-</td>
      <td>D926-</td>
      <td>300</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E1_S2</td>
      <td>D804-</td>
      <td>D808p</td>
      <td>D926-</td>
      <td>139</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E1_S3</td>
      <td>D804-</td>
      <td>D808-</td>
      <td>D926p</td>
      <td>503</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E1_S4</td>
      <td>D804p</td>
      <td>D808p</td>
      <td>D926-</td>
      <td>94</td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S5</td>
      <td>D804p</td>
      <td>D808-</td>
      <td>D926p</td>
      <td>87</td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S6</td>
      <td>D804-</td>
      <td>D808p</td>
      <td>D926p</td>
      <td>277</td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S7</td>
      <td>D804p</td>
      <td>D808p</td>
      <td>D926p</td>
      <td>141</td>
      <td></td>
    </tr>
    <tr>
      <td>E2_S0</td>
      <td>D804-</td>
      <td>D808p</td>
      <td>D926-</td>
      <td>193</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E2_S1</td>
      <td>D804-</td>
      <td>D808p</td>
      <td>D926p</td>
      <td>350</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>P-E2_S0</td>
      <td>D804-</td>
      <td>D808p</td>
      <td>D926p</td>
      <td>100</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>Mutants</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S1M</td>
      <td>D804N</td>
      <td>D808-</td>
      <td>D926-</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E1_S2M</td>
      <td>D804-</td>
      <td>D808N</td>
      <td>D926-</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E1_S3M</td>
      <td>D804-</td>
      <td>D808-</td>
      <td>D926N</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E2_S1M</td>
      <td>D804N</td>
      <td>D808-</td>
      <td>D926p</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E2_S2M</td>
      <td>D804-</td>
      <td>D808N</td>
      <td>D926p</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>E2_S3M</td>
      <td>D804-</td>
      <td>D808-</td>
      <td>D926N</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>P-E2_S1M</td>
      <td>D804N</td>
      <td>D808-</td>
      <td>D926p</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
    <tr>
      <td>P-E2_S2M</td>
      <td>D804-</td>
      <td>D808N</td>
      <td>D926p</td>
      <td>40</td>
      <td>2 × 128</td>
    </tr>
  </tbody>
</table>

Figure 2 shows the binding pocket conformation in the E1 systems (Table 3) at the end of the all-atom MD simulations. Out of the three aspartates when two or more are protonated the binding pocket becomes unstable, showing a large deviation from the crystal structure either with one of the bound Na+ expelled from its binding site (systems E1_S5-7), or with a Cl- ion attracted into the binding pocket (system E1_S4). These scenarios are not likely to happen in the normal function cycle of the pump. On the other hand, when the number of protonated aspartates is less than two the binding pocket remains structurally close to that in the crystal structure (systems E1_S0-3). The heavy atom root mean squared deviations (RMSD) between the crystal structure and the structure snapshots from the last 50 ns of the simulations are less than 1.6 Å.

![Figure 2.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig2-v2.jpg)

**Figure 2.:** The binding site residues are shown in stick presentation and the ions are shown as spheres. Binding site Na+ ions from the MD simulation snapshots are in yellow, and the crystal Na+ are in orange. A Cl- ion has entered the binding site in system E1_S4 during the simulation and is shown in green. The view is from the extracellular side towards the intracellular side. The figure is produced with PyMOL (DeLano, 2002).

### Protonation state and the E1 binding pocket selectivity

Analysis of the structural stability of the binding sites based on the MD simulations indicates that all of the four protonation states producing stable ion binding pockets may coexist when the pump is in the Na3·E1(ADP·Pi) state. The relative population of these states in the state Na3·E1(ADP·Pi), however, would differ from one another. The overall selectivity of the binding sites has contributions from all the states, and the predominant protonation state configuration should produce binding sites that are Na+ selective. The determination of this protonation state configuration starts from the protein-membrane systems generated by the restraint-free MD simulations. A reduced structural model of the binding pocket is derived from each of these systems (Table 3) and the binding free energy differences between Na+ and K+ (ΔΔGNa→K) at the binding sites are calculated (See Materials and methods). The value of ΔΔGNa→K reflects the affinity difference between K+ and Na+ binding as ΔΔGNa→K=ΔGk−ΔGNa=RT ln(KD,K/KD,Na). The results are plotted as the logarithm of the affinity ratio, ln(KD,K/KD,Na), in Figure 3. The values of ΔΔGNa→K are shown in Table 4.

![Figure 3.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig3-v2.jpg)

**Figure 3.:** Ion binding sites selectivity characterized by $ln(K_{D,K}/K_{D,Na})$ in states Na3E1·(ADP·Pi) (blue) and E2(K2) (red).Sites I (square), II (circle), and III (triangle) are distinguished by their shapes. Values from the previous calculations with a smaller reduced region are shown as empty symbols. All the binding site glutamates (i.e., E327, E779, and E954) are kept protonated. The protonation states of the binding site aspartates are indicated below the plot.

**Table 4.**
 The binding free energy difference ($ΔΔG_{Na→K}$) at all the binding sites calculated from FEP/H-REMD simulations. The energy values are in kcal/mol.


<table>
  <thead>
    <tr>
      <th>Systems</th>
      <th colspan="3">Binding sites</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>I</td>
      <td>II</td>
      <td>III</td>
    </tr>
    <tr>
      <td>Wildtype</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S0</td>
      <td>0.1 ± 0.1</td>
      <td>4.5 ± 0.1</td>
      <td>1.8 ± 0.1</td>
    </tr>
    <tr>
      <td>E1_S1</td>
      <td>3.7 ± 0.2</td>
      <td>1.7 ± 0.1</td>
      <td>4.7 ± 0.1</td>
    </tr>
    <tr>
      <td>E1_S2</td>
      <td>-3.5 ± 1.0</td>
      <td>3.8 ± 0.3</td>
      <td>2.9 ± 0.6</td>
    </tr>
    <tr>
      <td>E1_S3</td>
      <td>-1.5 ± 0.2</td>
      <td>4.7 ± 0.4</td>
      <td>-0.5 ± 0.3</td>
    </tr>
    <tr>
      <td>E2_S0</td>
      <td>-4.4 ± 0.3</td>
      <td>-6.1 ± 0.0</td>
      <td></td>
    </tr>
    <tr>
      <td>E2_S1</td>
      <td>-3.5 ± 0.1</td>
      <td>-6.1 ± 0.1</td>
      <td></td>
    </tr>
    <tr>
      <td>P-E2_S0</td>
      <td>-1.0 ± 0.6</td>
      <td>0.7 ± 0.4</td>
      <td></td>
    </tr>
    <tr>
      <td>Mutants</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E1_S1M</td>
      <td>1.4 ± 0.1</td>
      <td>5.7 ± 0.0</td>
      <td>2.4 ± 0.1</td>
    </tr>
    <tr>
      <td>E1_S2M</td>
      <td>4.3 ± 0.7</td>
      <td>6.6 ± 0.6</td>
      <td>5.2 ± 0.9</td>
    </tr>
    <tr>
      <td>E1_S3M</td>
      <td>-0.6 ± 0.1</td>
      <td>1.7 ± 0.1</td>
      <td>0.0 ± 0.0</td>
    </tr>
    <tr>
      <td>E2_S1M</td>
      <td>-3.3 ± 0.3</td>
      <td>-5.7 ± 0.0</td>
      <td></td>
    </tr>
    <tr>
      <td>E2_S2M</td>
      <td>-5.4 ± 0.1</td>
      <td>-6.4 ± 0.1</td>
      <td></td>
    </tr>
    <tr>
      <td>E2_S3M</td>
      <td>-3.8 ± 0.1</td>
      <td>-7.2 ± 0.1</td>
      <td></td>
    </tr>
    <tr>
      <td>P-E2_S1M</td>
      <td>0.8 ± 0.9</td>
      <td>1.9 ± 0.4</td>
      <td></td>
    </tr>
    <tr>
      <td>P-E2_S2M</td>
      <td>1.6 ± 0.5</td>
      <td>1.9 ± 0.4</td>
      <td></td>
    </tr>
  </tbody>
</table>

As shown in Figure 3, the protonation state of the aspartates greatly affects both the E1 and E2 binding sites selectivity. The protonation state at E2(K2) binding pocket proposed in the earlier study (Yu et al., 2011) is confirmed by the present calculations, in which the reduced system includes a larger region of the protein and more residues at the outskirt of the main binding pocket, including D926 and E954. It is evident that a different set of residues is protonated in the Na+ selective E1 as compared to in the K+ selective E2 (Figure 3). While the glutamates (i.e., E327, E779, and E954) remain protonated in both the Na3·E1(ADP·Pi) and E2(K2) states, the binding pocket aspartates take on opposite protonation states. In Na3·E1(ADP·Pi) D804 is protonated and both D808 and D926 are deprotonated, and their protonation states are reversed in E2(K2). Free energy perturbation (FEP) calculations on the protonation/deprotonation of D804 estimated a pKa value of 9.2 (See Materials and methods), further supporting its protonated form under physiological conditions in E1.

### Charge-neutralizing mutations and shift in selectivity

The impact of charge-neutralizing mutations of the key aspartate residues on the binding site selectivity was examined. D to N mutations have previously been used in experimental studies as a strategy to ascertain the possible charged state of these residues. The results of the free energy calculations, summarized in Figure 4, indicate that all the three sites remain Na+ selective in the partly occluded Na3·E1(ADP·Pi) in both D804N and D808N, whilst D926N causes the sites to lose most of the Na+ selectivity. Using Na+ dependent phosphorylation and ATP binding assays, it was shown that the cytoplasmic binding affinity for both Na+ and K+ is reduced in D804N and D808N (Jorgensen et al., 2001; Pedersen et al., 1997). The D804N mutation affects the cytoplasmic K+ and Na+ binding differently. The mutation’s impact on cytoplasmic Na+ binding is not as prominent as on K+ binding and D804N would appear more Na+ selective than the wildtype. This is reflected in the calculation results. The KD,K/KD,Na at sites I and III are reduced by a factor of ~50 from 476.6 and 2523.3 in the wildtype to 10.3 and 54.6 in the D804N mutant, but the sites are still Na+ selective. The selectivity of site II is increased to a much larger extent, from 17.0 in the wildtype to 13359.7 in the mutant. This is an ~1000 fold increase in selectivity and it implies that D804N is likely more Na+ selective than the wildtype pump. The D808N mutant also becomes more Na+ selective compared to the wildtype pump. The most dramatic increase in Na+ selectivity happens at site II as in the case of D804N. Interestingly, site I, which prefers to bind K+ in the wildtype with the protonated D808 (Figure 3), is now Na+ selective in D808N. It could be that the spatial packing is the major contributing factor to the site I ion selectivity. In the calculations, both sites II and III lose their Na+ selectivity in the D926N mutant. The shifting of selectivity towards K+ at site III in this mutant is a bit surprising, and worth commenting on. There are two possible explanations. First, substituting a negatively charged carbonyl oxygen with a bulkier but neutral –NH2 at the D926 sidechain could prevent entrance of an ion to this site. Thus, the simulated conformation with an ion at this site could be energetically inaccessible. In other words, this is a metastable state with the absolute free energy of Na+ and K+ binding to this conformation equally prohibitive. An alternative explanation is that the D926N mutation alters the available conformational space accessible by helix M5 and this allows K+ to go into site III as suggested in reference (Kanai et al., 2013). The binding of this K+, however, prevents the further binding of Na+, and results in the compromised Na+ selectivity in this mutant. Even though the calculations show D926N with decreased Na+ selectivity, they do not explain why experimentally the D926N mutant has compromised Na+ binding ability in the absence of K+ (Einholm et al., 2010). The loss in selectivity seen in this D926N mutant, however, could account for the strong inhibition by high K+ on Na+/K+-ATPase activity (cf. Figure 2A in reference [Einholm et al., 2010]).

![Figure 4.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig4-v2.jpg)

**Figure 4.:** The wildtype protein is colored black and the mutations in E1 (blue) and E2 (red) are colored differently. Sites I (square), II (circle), and III (triangle) are distinguished by their shapes. The empty symbols represent values calculated from the outward facing P-E2 model.

All the D to N mutations tested for the occluded E2(K2) state appear to have little impact on the K+ selectivity, in apparent contradiction with the experimental observations showing that both D804N and D808N display decreased selectivity for external K+ (Kuntzweiler et al., 1996; Pedersen et al., 1997). In a previous computational study, the D808N mutation was also shown to minimally affect the K+ selectivity in E2(K2). Discrepancies between the calculations and the selectivity inferred from biochemical experiments have been noted previously, though the reason was not clear. A plausible explanation could be that the experimentally measured selectivity is an outcome from the relevant states including both P-E2 and E2(K2). However, any contribution from the P-E2 state to the observed selectivity was not taken into account by the calculations because of the missing crystal structure of the outward-facing state. To test this idea, we generated a model structure of the P-E2 state based on the homolog structures from the Ca2+ SERCA pump (see below). This model was then used to calculate the $ΔΔG_{Na→K}$ in the wildtype and the mutant pumps. The results show that both sites I and II have increased preference for external Na+ in the P-E2 state of D808N (Figure 4), which explains previous discrepancies between the calculations and the experiments.

### Ion selectivity along the pump cycle

Using the crystal structures of the Ca2+ SERCA pump as templates and a coarse grained transition pathway calculation method, ANMpathway (Das et al., 2014), we generated structural models of the Na+– and K+–loaded outward-facing P-E2 state (see Materials and methods). The models appear to be structurally similar to the recently published P-E2 like structures of the Na+/K+-pump (Gregersen et al., 2016; Laursen et al., 2013) and the vanadate-Inhibited, P-E2 mimic of the Ca2+ SERCA pump (Clausen et al., 2016). The MD simulations of the models are also able to predict with considerable accuracy the experimentally measured gating charge upon ion binding (Castillo et al., 2015). The structural transition pathways leading to these models provide a view of the intermediate structures along the pump cycle. Using these models, we calculated the ΔΔGNa→K for the binding site of the intermediate state structures. The entire atomistic protein-membrane systems were used in the calculations. The results are presented in Figure 5 and Table 5. The calculations are valid as the ΔΔGNa→K values mirror those computed from the reduced systems with the same protonation states (Figure 3).

![Figure 5.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig5-v2.jpg)

**Figure 5.:** Sites I (square), II (circle), and III (triangle) are distinguished by their shapes. Different colors indicate whether there are two (red) or three (blue) sites that are included in the calculations. The conformational states are numbered and stamped along the pump cycle in the top panel. The protonation states of the aspartates are indicated below.

**Table 5.**
 Selectivity in the form of at the binding sites along the pump cycle from state P-E2·K2 to P-E2·Na3. The energies are in kcal/mol.


<table>
  <thead>
    <tr>
      <th></th>
      <th>*p/-</th>
      <th>-/p</th>
      <th>p/p</th>
      <th>p/p</th>
      <th>p/p</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>s/-</th>
      <th>-/s</th>
      <th>s/p</th>
      <th>p/s</th>
      <th>s/s</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(1) P-E2.K2</td>
      <td>-0.7 ± 1.0</td>
      <td>0.1 ± 0.5</td>
      <td>-1.0 ± 0.6</td>
      <td>0.7 ± 0.4</td>
      <td>-0.6 ± 0.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>(2) Intermediate</td>
      <td>0.0 ± 0.4</td>
      <td>1.8 ± 1.3</td>
      <td>-0.5 ± 0.3</td>
      <td>-5.1 ± 0.3</td>
      <td>-4.0 ± 0.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>(3) E2(K2)</td>
      <td>-4.9 ± 0.8</td>
      <td>-3.0 ± 0.5</td>
      <td>-5.0 ± 0.2</td>
      <td>-4.2 ± 0.1</td>
      <td>-9.3 ± 0.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>(4) Intermediate</td>
      <td>0.6 ± 0.7</td>
      <td>-0.8 ± 0.3</td>
      <td>2.0 ± 0.3</td>
      <td>-2.7 ± 0.2</td>
      <td>-1.6 ± 0.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>(5) K2.E1</td>
      <td>1.5 ± 0.3</td>
      <td>1.1 ± 0.2</td>
      <td>1.1 ± 0.1</td>
      <td>-3.8 ± 0.3</td>
      <td>-1.2 ± 0.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>(6) K2.E1*</td>
      <td>0.6 ± 0.5</td>
      <td>0.7 ± 0.4</td>
      <td>1.3 ± 0.2</td>
      <td>-0.4 ± 0.8</td>
      <td>0.1 ± 0.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_*The top and bottom rows represent the starting and ending binding site ion configurations. A 'p' represents a K+ (potassium) ion and an 's' represents a Na+ (sodium) ion. The binding sites I, II, and III in this order are separated by '/'._

The results reveal a fascinating feature of the binding site selectivity along the pump cycle. Initially, the two K+ binding sites in the outward-facing model P-E2·K2 (state ① in Figure 5) appear to be non-selective or only weakly K+ selective. However, the selectivity for K+ over Na+ increases as the pump occludes to form the K+–bound occluded state E2(K2) (state ③). After the dephosphorylation of P-E2, the binding pocket opens up to the cytoplasmic side. Accompanying this structural transition is the selectivity reversal at site I, switching the site from K+ to Na+ selective (③ to ④ in Figure 5). The protonation state change further shifts the ion selectivity at the sites in E1 towards Na+. Changing the protonation state in K2E1 (④ to ⑤ in Figure 5) to the protonation state dominant in Na3·E1(ADP·Pi), i.e., state ⑥ in Figure 5 with protonated D804 and deprotonated D808 and D926, further reduces the K+ selectivity at both sites I and II. When the pump is in this state, site I is Na+ selective and site II is only weakly K+ selective. Together, the E2 to E1 structural transition and the protonation state change promote the release of K+ to the cytoplasmic side. Transient changes in the binding pocket protonation state upon occlusion/deocclusion are possible and could lead to variations in the magnitude of $ΔΔG_{Na→K}$ for the intermediate states. Nonetheless, the general trend in free energy changes upon occlusion/deocclusion should remain because the $ΔΔG_{Na→K}$ of the occluded state E2(K2) has a much larger magnitude than that of the open-access outward- and inward-facing states.

The free energy calculations corroborate the notion that the two K+ binding from the extracellular side is sequential and possibly cooperative. The sequential binding of extracellular K+ was initially demonstrated by Forbush (Forbush, 1987). Recently using crystallography and isotopic measurements Ogawa et al. presented strong evidence that the first K+ binds at site I and the second K+ at site II (Ogawa et al., 2015). Whether there is cooperativity upon extracellular K+ binding, however, is not clear from the crystal structures. Two electrode voltage clamp experiments have shown that the two extracellular K+ binding events are relatively independent in the absence of extracellular Na+, but there is positive cooperativity of K+ binding when extracellular Na+ ions are present (Jaisser et al., 1994). The current $ΔΔG_{Na→K}$ calculations of the two ion bound P-E2 (Table 5) provide an interpretation of this phenomenon. With a K+ ion at site I, site II is relatively nondiscriminatory ($ΔΔG_{Na→K}$ = 0.7 kcal/mol, p/p to p/s in state ① P-E2.K2, Table 5), but it becomes much more Na+ selective ($ΔΔG_{Na→K}$ = 2.4 kcal/mol, s/s to s/p in state ⑨ P-E2·Na3, Table 5) when there is a Na+ ion bound at site I. In the presence of extracellular Na+, K+ ions have to first compete with Na+ to bind at site I in order for the subsequent K+ to bind, therefore resulting in the observed binding cooperativity in the presence of extracellular Na+.

A similar phenomenon is seen in the Na+ branch of the pump cycle. Initially, site I in the inward-facing Na3·E1(ADP·Pi) structure (state ⑦) is weakly Na+ selective when the other two sites are filled with Na+. However, the intermediate state ⑧ during the occlusion process shows that its site I is highly discriminating against K+ with a $ΔΔG_{Na→K}$ of 2.9 kcal/mol (Figure 5 and Table 5). Therefore, if a K+ is bound in this site, the free energy barrier toward occlusion would be much higher than when a Na+ ion was bound and the subsequent occlusion is not likely. In the case when a K+ ion replaces a Na+ at site II or III, although the energy barrier of occlusion is not as prominent, such a binding pocket ion configuration is energetically less favorable than the native configuration and its appearance is unlikely in the first place.

Unlike the K+ branch, the $ΔΔG_{Na→K}$ calculations along the Na+ branch offers limited insights on the sequence of Na+ binding from the cytoplasmic side. The results are indicative of the selectivity at the sites, but not the absolute binding affinity. Based on the calculations alone, it is not possible to determine which site is the first to bind cytoplasmic Na+. It could be site III, as suggested by Kanai et al., and this prepares the other two sites for the following Na+ binding (Kanai et al., 2013). Or, alternatively, the first two Na+ bind at sites I and II in the main binding pocket and the last Na+ enters, takes over site II, and pushes the two previously bound ions further, so that the ions in sites II and I now move to sites I and III, in a process reminiscent of the “knock-on” mechanism occurring in potassium channels (Hodgkin et al., 1955). A direct assessment of these proposed binding sequences will require further experiments.

## Discussion

The results from the MD simulations support the notion that the protonation state of the binding pocket and its selectivity are closely related. Because the binding pocket in the Na+/K+-pump displays considerable flexibility, it is worth pausing to reflect on the possible mechanism that underlies this relation. While the selectivity of a very rigid binding site is first and foremost predetermined by its atomic geometry, the selectivity of a flexible binding site is strongly affected by local ion-ligand and ligand-ligand interactions. In such flexible systems, selectivity is controlled by the both number and the physicochemical properties of ion-coordinating ligands (Yu et al., 2010). For example, high-field ligands, such as deprotonated acidic side chains tend to favor Na+ binding and protonation revert those to low-field ligands, which tend to favor K+. Hence, in the Na+/K+-pump protonation is exploited to modulate selectivity by altering the electrostatic properties of several of residues in the binding pocket. This is also consistent with the results from our previous study on the ion selectivity in E2(K2), which concluded that changes in the electrostatic properties of the protonatable residues was the likely mechanism responsible for the K+ selectivity in the E2 state of the pump (Yu et al., 2011). Even though the local structural rearrangements at the binding sites are small upon the change in protonation state, it is enough to change the physical properties of the coordinating ligand, thus giving rise to discernable differences in the ion selectivity. The crystal structures of the Na+/K+-pump in its Na3.E1·(ADP·Pi) and E2(K2) states show similarity in their binding pocket configurations (Figure 1), including the coordination patterns of the bound ions at sites I and II (Table 1). The heavy atom RMSD between the binding pocket residues is 2.5 Å and the structural difference remains after hundreds of ns of simulations. Empirical pKa and FEP calculations based on the MD simulation equilibrated structures indicate that the binding pocket glutamates (i.e., E327, E779, and E954) are likely protonated in both Na3.E1·(ADP·Pi) and E2(K2), although previous mutagenesis experiments showed that charge-neutralizing mutation E327Q affects pump function, possibly by altering ion-pump interactions and the kinetics of the occlusion/deocclusion reactions along the pump cycle (Jorgensen et al., 2001; Kuntzweiler et al., 1995; Li et al., 2006; Nielsen et al., 1998). The calculations also suggest that the protonation states of D804, D808, and D926 are different in Na3·E1·(ADP·Pi) and E2(K2). Among the three aspartates only D804 is protonated in order for all three sites to stay Na+ selective in Na3·E1·(ADP·Pi). The E1 binding pocket devoid of ions carries a net charge of -2, consistent with that deduced from previous fluorescence studies (Schneeberger et al., 1999). Mutagenesis experiments are also consistent with the unlikely protonation of D808 and D926 when the pump is in E1 trying to bind cytoplasmic Na+ (Jewell-Motz et al., 1993; Pedersen et al., 1997). The protonation states of these three residues are reversed in E2(K2) with D804 deprotonated and the other two protonated, a result that is supported by a previous computational study (Yu et al., 2011). The different protonation states for E1 and E2 also agree well with the 'four-site' model proposed by Skou and Esmann more than 30 years ago with the K+-bound E2 state carrying two sidechain protons (H2EK2) and the Na+-bound E1 state carrying only one (HENa3) (Skou et al., 1980).

It is worth pointing out that the second proton (i.e., the proton on D926) in the K+ bound E2 state must come from and return to the same side of the membrane during the pump cycle so that the net charge moved per cycle by the pump is one. It seems unlikely that this proton could come from the extracellular side because altering extracellular pH would then protonate or deprotonate D926, causing major changes in Na+ binding affinity and the maximum pumping turnover rate. This is not observed over an external pH range 9.6 to 5.6 (Mitchell et al., 2014; Vasilyev et al., 2004; Yu et al., 2011). Therefore, it is more likely that the D926 proton comes from the cytoplasmic side. This is supported by MD simulations of the P-E2·Na2 and Na2·E1·(ADP·Pi) revealing the existence of aqueous pathways connecting the cytoplasm and D926 (Figure 6). One of the water pathways is located between the helices M5, M7, and M8 (Figure 6B), similar to the C-terminal proton pathway previously proposed (Poulsen et al., 2010). A proton could enter through this pathway to protonate D926 and then leave through the same pathway during the E2 to E1 transition, or through an alternative path passing the main binding pocket along with the dissociating ions as seen in the Na2·E1·(ADP·Pi) simulation (Figure 6A).

![Figure 6.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig6-v2.jpg)

**Figure 6.:** The top (top) and side (bottom) views are shown. D926 are shown in sphere representation. Water path connecting the cytoplasm and the D926 are in surface representation colored in blue. Na+ (yellow) are shown as spheres.

Under physiological conditions, the challenge faced by the Na+/K+-pump is to effectively pick out the correct ion species from a solution much more concentrated with other types of ions. Even when the binding affinity of the ion species being transported is a few orders of magnitude higher than that of the other ion ($ΔΔG_{bind}$ = 1 to 3 kcal/mol), the advantage in binding is undermined by the higher concentration of the competing ion. The pump overcomes this problem by raising the free energy barrier for the occlusion step in the presence of incorrect ions in the binding pocket, thus preventing the faulty transport (Figure 5 and Table 5). This self-correcting mechanism makes sure that the intracellular and the extracellular gates do not close (i.e., occlude), which is required for the pump cycle to go forward, unless the correct ion configuration is present at the binding pocket. Therefore, this is an inherent part of the ping-pong mechanism the pump uses to transport ions with high selectivity. Although other energetic barriers, like pathways the ions use to travel to the binding site, could contribute to the ion binding specificity, it is not likely the case here as both Na+ and K+ can access the binding pocket in the simulations of the E1 and P-E2 states without ions bound.

The concept of a self-correcting pumping mechanism sheds new light on a number of puzzling functional observations. For instance, it explains why E1 displays a strong apparent affinity for K+ in competitive binding assays (Schneeberger et al., 2001), even though the pump still binds and occludes Na+ from the cytoplasmic side. The calculations show that all the sites in the Na3·E1·(ADP·Pi) state are selective for Na+, likely because this is a partially occluded state. A wrong combination of binding site ions would not have been occluded and reached such a state. In a fully inward-open conformation, the selectivity of the sites ought to be fairly weak. The high affinity for K+ observed in E1 in these experiments is due to the backward occlusion leading to the K+-bound state E2(K2). The proposed self-correcting mechanism parallels the suggestion based on experiments that the phosphorylation and occlusion of E1 requires 3 Na+ bound, and this increases the apparent affinity for Na+ in the normal pump cycle (Schneeberger et al., 2001). The self-correcting mechanism can also account for the different effects of Na+ and K+ congeners on the release rate of the occluded 86Rb+ (a K+ congener) to the extracellular side upon the “backdoor” phosphorylation in the presence of Pi reported by Forbush (Forbush, 1987). This backward deocclusion is accelerated in the presence of Na+, and it follows a single phase, while a much slower deocclusion process with a second slow phase is observed in the presence of K+ or Rb+. According to the self-correcting mechanism, it is likely that upon the replacement of one of the two occluded 42K+ or 86Rb+ by cold K+ at one site, the pump succeeded to occlude again, resulting in the second slow phase. These explanations are sensible, in turn lending support to the proposed self-correcting mechanism. Given that the selectivity in the outward/inward facing states is after all not as strong as previously thought, such a mechanism must be in place.

This analysis suggests that an important component of the overall selectivity emerges from the increased free energy barrier associated with the occlusion process while the wrong type of ion is bound to a site. Although the pump would be kinetically more efficient by preventing the wrong ions from reaching the binding sites to begin with, the free energy calculations do not support the notion of highly selective binding sites for the open-access states. While such mechanism may seem inefficient because the pump must try to figure out that there is an issue with selectivity only after binding of several ions of the wrong type, it is important to realize that the Na+/K+-pump is not a particular fast molecular machine. The estimated turnover rate is less than 100 per second and decreases even further as the transmembrane voltage becomes more negative (Heyse et al., 1994). The implication is that the system has plenty of time, at the molecular level, to function near thermodynamic equilibrium. In other words, the pump has not been evolutionarily optimized to be a particularly fast molecular machine, but an energetically efficient one. Thus, even though the idea of a self-correcting ion selectivity mechanism seems counterintuitive and inefficient, it is consistent with the physical conditions under which the pump has to operate.

In summary, the present study highlights the tight coupling between the Na+/K+ selectivity of the binding sites, the protonation state of the coordinating residues, and the conformational state of the pump. The important functional consequence of such tight coupling is the necessity to have the correct type and number of ions in the binding pocket for the pumping cycle to proceed forward toward the occlusion step. Because the ion binding selectivity is strongly dependent upon the protein conformation, a self-correcting mechanism counteracting the effect of the ion concentration in the environment ensures an efficient function of the pump.

## Materials and methods

### Preparing the all-atom membrane-Na+/K+-pump simulation systems

The crystal structures, 3WGV (Kanai et al., 2013) and 2ZXE (Shinoda et al., 2009), representing the Na+/K+-pump in its Na3·E1(ADP·Pi) and E2(K2) states were used to build the simulation systems. The structure 3WGV contains two copies of the pump assembly in the asymmetric unit. Since the structural variations between the two assemblies are minimal, only the copy including chains A, B, and G was kept. Several small molecule ligands were co-crystalized with the pump in 3WGV, including an ADP, a $AlF_{4}^{−}$ ion, an oligomycin A, two Mg2+, three cholesterol, four Na+, and five 1,2-diacyl-sn-glycero-3-phosphocholine molecules for each copy of the pump structure. Among these ligands, oligomycin A was not included in the simulation system. The ion was replaced by a $PO_{4}^{3−}$ and POPC molecules were used in place of the 1,2-diacyl-sn-glycero-3-phosphocholine. The structure of 2ZXE also contains small molecule ligands including cholesterol, K+, Mg2+, and $MgF_{4}^{2−}$. Similarly, a $PO_{4}^{3−}$ was used to replace the $MgF_{4}^{2−}$ ion. Since the Na+/K+-pump crystal structures were obtained from different organisms, the residue numbers differ slightly. For the sake of convenience, the numbering scheme in the newly resolved 3WGV from pig kidney was adopted in this study.

After removing irregularities from the PDB files, the Na+/K+-pump subunits were capped with acetylated N-termini and amidated C-termini. The ectodomain of the β-subunit was not included in simulation systems to reduce the computational cost. The orientation was chosen to be the same as in the OPM database (Lomize et al., 2006). At this stage, the protonation states of the binding site residues were assigned with the PATCH command in CHARMM (Brooks et al., 2009). Eight different protonation states were considered in Na3·E1(ADP·Pi) state systems and both the protonated and charged D926 were included in the E2(K2) state systems. This resulted in a total of ten systems before proceeding to the next step. Table 3 shows the system names and the associated binding site protonation. We used the membrane builder module in CHARMM-GUI (Jo et al., 2007, 2008, 2009; Wu et al., 2014) to generate POPC bilayers around the pump structures. Once this was completed, each protein-membrane complex was solvated by an equal molar mixture of KCl and NaCl. The final system had a combined cation concentration of 0.3 M (i.e., [K+] = [Na+] = 0.15 M). At the end the E1 system was 84 × 110 × 158 Å3 in size and contained ~138,000 atoms, while the dimension of the E2 system was 85 × 109 × 105 Å3 with ~134,000 atoms. Each completed system was subjected to a 675-ps equilibration with reducing restraints on the heavy atoms to relax the initially uncorrelated components, followed by a 10-ns unrestrained pre-production using the simulation package NAMD2.9 (Phillips et al., 2005). After the systems were well equilibrated, they were simulated longer using the special-purpose supercomputer Anton (Shaw et al., 2009), which is designed for long time scale MD simulations.

### Generating the D to N mutant systems

Experimentally asparagine and glutamine are used as surrogates for protonated aspartate to study the effect of protonation. The effects of these charge-neutralizing mutants on the selectivity of the pump can be investigated computationally. The most interesting mutations in the context of this study are the single D to N mutations at the binding pocket, including residues D804, D808, and D926. The mutations were made on the crystal structures by replacing the proton on the OD2 atom in the aspartate with an –NH2 amine group. D804N and D808N mutations were also made in the outward facing P-E2 structural model (see below) to study how they affect the external K+ binding. The protonation states of the other titratable residues were determined with PROPKA. Each of these systems was equilibrated without any restraints for 40 ns. The system snapshot with the least structural deviation of the pump to the averaged structure during the simulation was used to generate the reduced system. The mutant systems are shown in Table 3.

### Selectivity at the binding site

The absolute free energy of an ion i binding to a binding site inside a protein has the following form,

$$
ΔG_{i, bind}=(G_{i, int}^{site}−G_{i, int}^{bulk})+[−k_{B}TIn(F_{t}C^{∘})−G_{i, trans}^{site}].
$$

The difference in the first term, $G_{i, int}^{site}−G_{i, int}^{bulk}$, represents the nonbonded interaction component of the free energy change upon moving the ion from the bulk solution to the binding site. The subtraction in the second term, $−k_{B}TIn(F_{t}C^{∘})−G_{i, trans}^{site}$, reflects the lost of translational freedom. The translational freedom factor Ft in bulk solution can be evaluated analytically under a rigid rotor approximation (Deng et al., 2006). Its final form depends on the force constants and the equilibrium values in the distance and angle restraints applied on the ion and the surrounding protein atoms. Based on Equation (1), the selectivity of a binding site can be expressed as the binding free energy difference of two ion species. For example, the binding free energy change upon changing ion i to j at the binding site is

$$
ΔΔG_{i→j}=(G_{j, int}^{site}−G_{j, int}^{bulk})−(G_{i, int}^{site}−G_{i, int}^{bulk})+(G_{i, trans}^{site}−G_{j, trans}^{site})=ΔG_{i→j}^{site}−G_{i→j}^{bulk}−G_{i→j}^{trans}.
$$

A negative value of $ΔΔG_{i→j}$ indicates that ion j binds more favorably than ion i and the site is j selective. There are three terms to be evaluated in Equation (2). $ΔG_{i→j}^{site}$ and $ΔG_{i→j}^{trans}$ are calculated using the reduce binding site model, while $ΔG_{i→j}^{bulk}$ is computed using a water sphere with the impact from the bulk solution factored in with a boundary potential (see below).

### Generating the reduced binding site systems

To generate the reduced binding site, the all-atom system prepared according to the procedures above was divided into an inner region and an outer region. The inner region was defined as residues and water molecules within 15 Å to the center of mass of the bound ions. Everything within this region was treated explicitly. An extended inner region was specified by a 3-Å thick shell continuing from the inner region outwards to create a smooth spherical dielectric cavity. Water molecules in this region were removed and their impact on the binding site was included implicitly. The coordinates of atoms in these extended region and those linked to them within three atomic bonds in the inner region were held fixed during the simulations. The rest of the system was considered the outer region, in which the atoms were removed and their impact on the inner region atoms was represented by the General Solvent Boundary Potential (GSBP) in the form of a solvent-shielded static field and a solvent-induced reaction field (Im et al., 2001). The reaction field arising from changes in charge distribution in the inner region was expressed in terms of a generalized multipole expansion using 11 spherical harmonic functions. Both the solvent-shielded static field and the reaction field matrix were independent of the inner region configuration, and therefore were calculated only once before further simulations using the finite-difference Poisson−Boltzmann (PB) method with the PBEQ module (Im et al., 1998) in CHARMM. In these calculations a dielectric constant of 1 was used for the inside of the protein within the inner and outer regions, whereas the rest of the system had a dielectric constant of 80. The atomic Born radii used in the PB calculations were determined by free energy calculations in explicit solvent (Nina et al., 1997). All these reduced systems were further equilibrated for 200 ps using Langevin dynamics at 303.15 K with a friction coefficient of 5 ps−1 assigned to all non-hydrogen atoms. All bonds involving hydrogen atoms were fixed with the SHAKE algorithm (Ryckaert et al., 1977). Nonbonded interactions within 14.5 Å were accounted for explicitly, while everything else beyond this distance was treated with an extended electrostatics method (Stote et al., 1991). The simulation program CHARMM (Brooks et al., 2009) was used for the equilibration. Table 3 lists all the reduced systems.

### Free energy perturbation simulations with boosting potential

It is known that the binding free energy calculated from FEP/MD simulations suffers from convergence issues because the residue sidechains at the binding site only sample a few of the several accessible rotameric states. This problem can be alleviated by introducing a replica-exchange scheme aiming at enhancing the sampling of sidechains (Jiang et al., 2009, 2010). This scheme allows exchange between the neighboring λ windows. Each λ window is coupled with a set of replica systems with a boosting potential of increasing strength used to accelerate the inter-conversion between sidechain rotameric states. We employed this hybrid FEP/H-REMD scheme implemented in the REPDSTR module in CHARMM (Jiang et al., 2010) to calculate the $ΔΔG_{i→j}$.

The boosting potential for the χ1 sidechain torsion of a binding site residue was obtained by fitting the potential of mean force as a function of the torsion χ, $𝒲(χ)$, with a cosine Fourier series in the form of

$$
U_{BP}(χ)=\sumn=1nK_{n}{1+cos⁡[n(χ−χ_{0,n})]}.
$$

The angle χ1 is dihedral formed by the bonded atoms N, CA, CB, and CG. The total number of the cosine terms, N, varies from 3 to 6, depending on which one produce a better fit to the 𝒲(χ). A residue is considered in the binding site if any of its sidechain heavy atoms is within 4.5 Å to the bound Na+ or K+. Table 6 lists all the binding site residues included in the boosting potential calculations.

**Table 6.**
 Binding site residues and the fitted parameters ki and χ0,i.


<table>
  <thead>
    <tr>
      <th></th>
      <th>k1</th>
      <th>χ0,1</th>
      <th>k2</th>
      <th>χ0,2</th>
      <th>k3</th>
      <th>χ0,3</th>
      <th>k4</th>
      <th>χ0,4</th>
      <th>k5</th>
      <th>χ0,5</th>
      <th>k6</th>
      <th>χ0,6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E327p</td>
      <td>-0.932</td>
      <td>53.11</td>
      <td>1.055</td>
      <td>61.08</td>
      <td>1.844</td>
      <td>62.05</td>
      <td>-0.312</td>
      <td>56.44</td>
      <td>0.392</td>
      <td>89.04</td>
      <td>0.225</td>
      <td>82.28</td>
    </tr>
    <tr>
      <td>M5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Y771</td>
      <td>-2.19</td>
      <td>62.51</td>
      <td>1.219</td>
      <td>89.27</td>
      <td>2.46</td>
      <td>60.91</td>
      <td>0.662</td>
      <td>40.85</td>
      <td>0.721</td>
      <td>44.75</td>
      <td>0.639</td>
      <td>50.42</td>
    </tr>
    <tr>
      <td>T774</td>
      <td>-4.25</td>
      <td>35.82</td>
      <td>2.437</td>
      <td>101.3</td>
      <td>3.602</td>
      <td>61.71</td>
      <td>1.128</td>
      <td>44.86</td>
      <td>1.071</td>
      <td>91.96</td>
      <td>0.857</td>
      <td>76.09</td>
    </tr>
    <tr>
      <td>S775</td>
      <td>3.068</td>
      <td>-26.37</td>
      <td>0.124</td>
      <td>38.67</td>
      <td>1.291</td>
      <td>62.22</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>N776</td>
      <td>2.664</td>
      <td>-166.23</td>
      <td>0.918</td>
      <td>87.15</td>
      <td>1.709</td>
      <td>62.85</td>
      <td>-0.53</td>
      <td>71.79</td>
      <td>-0.495</td>
      <td>50.76</td>
      <td>-0.406</td>
      <td>75</td>
    </tr>
    <tr>
      <td>E779p</td>
      <td>-2.508</td>
      <td>29.17</td>
      <td>1.792</td>
      <td>88.01</td>
      <td>2.591</td>
      <td>62.28</td>
      <td>0.487</td>
      <td>24.81</td>
      <td>0.476</td>
      <td>73.74</td>
      <td>0.462</td>
      <td>53.74</td>
    </tr>
    <tr>
      <td>M6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>D804-</td>
      <td>3.895</td>
      <td>-172.95</td>
      <td>0.489</td>
      <td>80.04</td>
      <td>1.897</td>
      <td>60.56</td>
      <td>-0.197</td>
      <td>82.91</td>
      <td>-0.271</td>
      <td>82.85</td>
      <td>-0.193</td>
      <td>79.47</td>
    </tr>
    <tr>
      <td>D804p</td>
      <td>2.968</td>
      <td>-157.98</td>
      <td>0.532</td>
      <td>81.76</td>
      <td>1.835</td>
      <td>60.45</td>
      <td>-0.247</td>
      <td>31.05</td>
      <td>-0.296</td>
      <td>89.84</td>
      <td>-0.278</td>
      <td>83.37</td>
    </tr>
    <tr>
      <td>N804</td>
      <td>2.981</td>
      <td>-160.18</td>
      <td>0.371</td>
      <td>84</td>
      <td>1.451</td>
      <td>59.42</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>D808-</td>
      <td>3.215</td>
      <td>-159.94</td>
      <td>0.21</td>
      <td>57.87</td>
      <td>1.744</td>
      <td>59.13</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>D808p</td>
      <td>-2.298</td>
      <td>55.97</td>
      <td>1.204</td>
      <td>66.88</td>
      <td>2.44</td>
      <td>62.53</td>
      <td>0.746</td>
      <td>37.74</td>
      <td>0.715</td>
      <td>55.74</td>
      <td>0.627</td>
      <td>63.72</td>
    </tr>
    <tr>
      <td>N808</td>
      <td>-2.344</td>
      <td>29.85</td>
      <td>1.771</td>
      <td>63.6</td>
      <td>2.654</td>
      <td>64.99</td>
      <td>0.914</td>
      <td>39.19</td>
      <td>0.73</td>
      <td>58.37</td>
      <td>0.63</td>
      <td>61.7</td>
    </tr>
    <tr>
      <td>M8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Q923</td>
      <td>-2.943</td>
      <td>33.4</td>
      <td>2.217</td>
      <td>87.95</td>
      <td>2.671</td>
      <td>61.48</td>
      <td>0.603</td>
      <td>74.2</td>
      <td>0.535</td>
      <td>30.65</td>
      <td>0.551</td>
      <td>44.23</td>
    </tr>
    <tr>
      <td>D926-</td>
      <td>4.361</td>
      <td>-169.1</td>
      <td>0.454</td>
      <td>95.51</td>
      <td>1.902</td>
      <td>60.16</td>
      <td>-0.283</td>
      <td>92.02</td>
      <td>-0.306</td>
      <td>88.18</td>
      <td>-0.215</td>
      <td>85.37</td>
    </tr>
    <tr>
      <td>D926p</td>
      <td>-2.704</td>
      <td>28.74</td>
      <td>1.477</td>
      <td>93.38</td>
      <td>2.744</td>
      <td>61.08</td>
      <td>0.816</td>
      <td>58.99</td>
      <td>0.852</td>
      <td>58.37</td>
      <td>0.809</td>
      <td>58.93</td>
    </tr>
    <tr>
      <td>N926</td>
      <td>3.674</td>
      <td>-157.18</td>
      <td>0.479</td>
      <td>89.17</td>
      <td>1.377</td>
      <td>61.78</td>
      <td>-0.625</td>
      <td>82.59</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![Figure 7.](https://cdn.elifesciences.org/articles/16616/elife-16616-fig7-v2.jpg)

**Figure 7.:** Fitting the potential of mean force $𝒲(χ)$ (red) with the boosting potential, $U_{BP}(χ)$ (black).

We performed umbrella sampling simulations to obtain the $𝒲(χ)$ for each binding site residue. First, the entire transmembrane helix containing the residue of interest was taken from the crystal structure with its orientation kept the same as in the OPM database. This was to provide a proper secondary structure environment. Next, we replaced the sidechains of all the other residues on the helix to hydrogen atoms to remove their steric effects. An implicit planar membrane model, EEF1/IMM1 (Lazaridis, 2003; Schneeberger et al., 1999) was used in place of a membrane bilayer to solvate the helix. 72 umbrella windows along χ were set up with a window spacing of of 5°. A harmonic bias potential was applied in each window with a force constant of 100 kcal/mol/rad2. After the windows were generated, each of them was simulated for 50 ns at 303.15 K using Langevin dynamics with a 2 fs time-step. All bond lengths involving hydrogen were fixed with the SHAKE algorithm (Ryckaert et al., 1977). The cutoff distance for nonbonded interactions was set to 11 Å. The simulation program CHARMM (Brooks et al., 2009) was used to conduct the simulations. The resulting distributions of χ were unbiased using the weighted histogram analysis method (WHAM) (Kumar et al., 1992). Figure 7 shows the $𝒲(χ)$ and the fitted curves. The fitting parameters and are given in Table 6. An appropriate boosting potential can be easily applied using the CONS DIHE command in CHARMM, with the sign in front of $U_{BP}(χ)$ reversed. This will effectively cancel out the potential barrier between the rotamers of a given residue sidechain.

Before computing $ΔG_{i→j}^{site}$ and $ΔG_{i→j}^{trans}$, restraints were set up to restrict the translational freedom of the bound ion of interest. First, three points within the protein region were picked out. They were used along with the position of the bound ion to set up the restraints. We employed the same protocol as in the Ligand Binder module (Jo et al., 2013) in CHARMM-GUI to select the three protein anchor points, p1, p2, and p3. The relative position of the bound ions to the protein can be defined by the distance r from l1 to p1, the angle θ between l1, p1 and p2, and the torsion ψ along l1, p1, p2, and p3. The translational restraint potential took the form of

$$
u_{trans}=\frac{1}{2}[k_{r}(r−r_{0})^{2}+k_{\theta}(\theta−\theta_{0})^{2}+k_{ψ}(ψ−ψ_{0})^{2}].
$$

The force constant regarding distance (i.e., kr) was set to 10 kcal/mol/Å2, and the rest of the force constants were 200 kcal/mol/rad2. The equilibrium values in utrans were taken from the 200 ps equilibration of the reduced binding site.

$ΔG_{Na→K}^{site}$ was computed with a set of FEP/H-REMD simulations. The translational restraint, utrans, was applied to restrict the translational freedom of the ion. The Na+ ion was changed alchemically to a K+ with an alchemical coupling factor, λ. 16 λ windows were used. Each λ window included 8 replicas with the strength of boosting potential scaled from 0 to 1. Exchange attempts were made every 0.2 ps and were only allowed between neighboring replicas with different boosting potential strengths in the same λ window and between the neighboring λ windows with zero boosting potential. A total of 128 replica systems were included in the calculations. Each replica system was simulated for 2 ns. To compute $ΔG_{Na→K}^{trans}$ at a given binding site, two sets of simulations were set up, one with Na+ at the binding site and the other with K+ for the calculation of$ΔG_{Na, trans}^{site}$ and $ΔG_{K, trans}^{site}$. The translational and orientational restraints were decoupled gradually (Beglov et al., 1994) using a coupling factor λ. The λ window and the boosting potential setup were similar to those used in the $ΔG_{Na→K}^{site}$ calculations. All the FEP/H-REMD calculations were performed using the REPDSTR module in CHARMM (Jiang et al., 2010). The output energies from the zero boosting potential systems were collected and processed using WHAM (Kumar et al., 1992). To compute the standard error of $ΔΔG$, we divided the trajectories into 10 blocks. The standard deviations of the averaged $ΔΔG$ from all the blocks are computed and reported in Tables 4 and 5 and Figures 3–5. Cautions should be taken when comparing the calculated and experimentally measured $ΔΔG$, because the latter usually contains contributions from multiple states of the pump while the calculated $ΔΔG$ is done using a single state.

### The bulk ion-water system and the calculation of ΔGNa→Kbulk

The bulk system was generated by building a water sphere of 10 Å radius and centering it at the origin. The water sphere was made form pre-equilibrated water boxes with TIP3P water molecules. A Na+ ion was placed at the center of the sphere. Any water molecules overlapping with the ion were deleted. The influence of the remaining bulk was approximated by the spherical solvent boundary potential (Beglov et al., 1994). The system was equilibrated for 200 ps at 303.15 K. Other simulation options were kept the same as described in the reduced binding site system. During the equilibration the position of the ion was restrained using a weak harmonic bias potential with a force constant of 0.5 kcal/mol/Å2. Once equilibrated, the Na+ was gradually changed to a K+ using the PERT module in CHARMM with 11 λ windows. The simulation time for each λ window was 1 ns. The resulting $ΔG_{Na→K}^{bulk}$ is 18.34 kcal/mol after unbiasing the energy outputs with WHAM. The calculated $ΔG_{Na→K}$ for all the binding sites in the systems summarized in Table 3 are shown in Table 4.

### D804 pKa calculations with explicit solvent

To further confirm the protonation state of D804, we evaluated its pKa shift with additional simulations in explicit solvent using the following formula:

$$
ΔpKa=(ΔG_{site}^{deprot}−ΔG_{bulk}^{deprot})/2.303k_{B}T.
$$

$ΔG_{site}^{deprot}$ and $ΔG_{site}^{deprot}$ are the free energy change of aspartate deprotonation in the protein environment and in bulk water, respectively. The reduced system of E1_S1 (Table 3) was used to compute the deprotonation free energy of D804 at the ion binding site ($ΔG_{site}^{deprot}$). To calculate the $ΔG_{bulk}^{deprot}$, an aspartic acid residue with an acetylated N-terminus and an amidated C-terminus was put into a pre-equilibrated water sphere of 15 Å radius. As in the calculations of $ΔG_{Na→K}^{bulk}$ and $ΔG_{K→Na}^{bulk}$, the impact of the bulk solution beyond the current system was incorporated by the spherical solvent boundary potential (Beglov et al., 1994). Alchemical FEP calculations were carried out in both systems. The λ windows were evenly spaced to gradually deprotonate the aspartate. The numbers of windows used in the $ΔG_{site}^{deprot}$ and $ΔG_{bulk}^{deprot}$ calculations were 24 and 10 respectively. Each window was equilibrated for 200 ps and contained 5 ns of sampling. The calculated $ΔG_{site}^{deprot}$ and $ΔG_{bulk}^{deprot}$ are −44.8 kcal/mol and −51.9 kcal/mol, respectively. Using Equation (5), the ΔpKa is 5.1, meaning the pKa of D804 is right shifted by 5.1 pK unit when it is in the Na+/K+ pump ion binding site. The final calculated pKa of D804 is 4.1 + 5.1 = 9.2 with 4.1 being the pKa value of an aspartate in bulk water (Berg et al., 2002), reinforcing the conclusion that D804 is protonated in the E1 state of the pump.

### Transition pathway calculations

Three conformational transition pathways were generated based on the shared homology between the Na+/K+-pump and the Ca2+ SERCA pump. One of such pathways connects states E2(K2) and P-E2·K2. The second connects states E2(K2) and K2·E1, and the third describes the transition between states Na3·E1-P and P-E2·Na3. First, A Cα-atom-only transition pathway for each of these was generated using the ANMPathway online server (http://anmpathway.lcrc.anl.gov/anmpathway.cgi) (Das et al., 2014) based on the SERCA pump crystal structures including 3B9B (Olesen et al., 2007), 1WPG (Toyoshima et al., 2004), and 1VFP (Toyoshima et al., 2004). Since both the Na+/K+-pump and the Ca2+ SERCA pump are P-type ATPases, it is reasonable to assume that they have similar pumping mechanisms and they share the same set of states along the pump cycle. Although crystal structures of the Na+/K+-pump are scarce, multiple high-resolution structures of the SERCA pump in different states are available (Karlsen et al., 2016). Among them, 3B9B represents the outward facing P-E2 state. All the other SERCA pump structures were aligned based on their transmembrane region Cα positions to the Na+/K+-pump and the Cα RMSD were computed to find those that resemble the structural states captured by the Na+/K+-pump crystal structures 3WGV (Kanai et al., 2013) and 2ZXE (Shinoda et al., 2009). The two SERCA pump structures representing states Na3·E1ATP (3WGV) and E2(K2) (2ZXE) are 1VFP and 1WPG, respectively. Each generated coarse-grained pathway is made of a sequence of structural snapshots containing Cα atoms only. These snapshots are called images and are distributed at equal RMSD intervals. The images from the coarse-grained pathways were then used in the all-atom targeted molecular dynamics (TMD) simulations to guide each transition. The starting system in the first and second pathway TMD simulations was taken from the well-equilibrated MD simulation system E2_S1 starting from the crystal structure 2ZXE. The third pathway was realized using the MD simulation system E1_S1 built from the crystal structure 3WGV, with the catalytic D369 phosphorylated. The protocol of the TMD simulations followed those published before (Castillo et al., 2015)

### Selectivity calculations along the pump cycle

Binding site ion selectivity was evaluated for nine systems representing different stages along the pump cycle. Among these systems are well-defined states: P-E2·K2, E2(K2), K2·E1, Na3·E1(ADP·Pi), and P-E2·Na3. The structures used for them are ① the generated P-E2·K2 model, ③ the equilibrated crystal structure 2ZXE, the equilibrated crystal structure 3WGV with ⑦ bound Na+ and with ⑤ bound Na+ replaced by K+ at sites I and II, and ⑨ the generated P-E2·Na3 model. Several intermediate states were also included. Intermediate state ② is between states ① P-E2·K2 and ③ E2(K2), taken from the TMD simulations of the first path after image 35. State ④ was taken at image 33 along the transition from state ③ E2(K2) to ⑤ K2·E1. Along the same vein, state ⑧ represented the intermediate at image 29 between states ⑦ Na3·E1(ADP.Pi) and ⑨ P-E2·Na3. The intermediates were taken near the midpoints of the transitions. An additional state ⑥ K2·E1* with altered binding site residue protonation was also included to reflect the protonation state change upon the E2 to E1 transition. All the states included in the selectivity calculations and their relative placement along the pump cycle can be seen in Figure 5.

To evaluate the selectivity at a given binding site in a system, three simulations were performed with slightly varied Lennard-Jones (LJ) parameters for the ion of interest. In the first simulation, the parameters of the ion were unaltered. A linear interpolation of the LJ and the NBFIX parameters between Na+ and K+ was made. In the second simulation, the LJ and NBFIX parameters of the ion were replaced by those of a Na/K hybrid at the middle point of the interpolation. In the last simulation, the ion’s parameters were completely changed to represent the other ion type, either K+ or Na+, depending on the starting ion type. 10 ns trajectories were generated for each simulation using the simulation package OpenMM6.2 (Eastman et al., 2013). Energies were calculated from each trajectory using two parameter sets. The difference was fed into the WHAM equation (Kumar et al., 1992) and the free energy changes upon mutating the ion to the intermediate as well as upon mutating the intermediate to the other ion type were solved self-consistently. The sum of the two free energies gives the $ΔG^{site}$. The same strategy was used to compute the $ΔG^{bulk}$ in water ($ΔG^{bulk}$ kcal/mol). The binding free energy difference is given by $ΔΔG_{bind}=ΔG^{site}−G^{bulk}$. The selectivity of binding site with different occupancies was also included in the calculations. The $ΔΔG_{bind}$ are shown in Table 5.

### NAMD simulation protocol

The initial relaxation and the restraint-free equilibration of the membrane pump systems were performed using the NAMD2.9 (Phillips et al., 2005) simulation package with the input scripts from the CHARMM-GUI membrane builder module. The NAMD simulation temperature was set to 303.15 K using Langevin Dynamics with a damping coefficient of 10 ps−1 during the relaxation and 1 ps−1 during the restraint-free equilibration. The van der Waals interactions were smoothly switched off at 10–12 Å by a force switching function (Steinbach et al., 1994) and the electrostatic interactions were calculated using the particle-mesh Ewald method with a mesh size of ~1 Å.

### Anton simulation protocol

After a short equilibration with NAMD, each all-atom system listed in Table 3 were subjected to a hundred ns scale long production without any restraints using the special-purpose supercomputer Anton (Shaw et al., 2009). The volume of the periodic cell was kept constant and the temperature was set to 303.15K using the Nosé-Hoover thermostats (Martyna et al., 1992). The lengths of all bonds involving hydrogen atoms were constrained using M-SHAKE (Kräutler et al., 2001). The cutoff of the van der Waals and short-range electrostatic interactions was set to an optimal value suggested by the Anton guesser script, guess_chem. Long-range electrostatic interactions were evaluated using the k-space Gaussian split Ewald method (Shan et al., 2005) with a 64 × 64 × 64 mesh. The integration time step was 2 fs. The r-RESPA integration method (Tuckerman et al., 1992) was employed and long-range electrostatics were evaluated every 6 fs.

### OpenMM simulation protocol

Simulations used to compute ion selectivity along the pump cycle were conducted using the simulation package OpenMM6.2 (Eastman et al., 2013). The constant pressure and temperature (NPT) ensemble was used for these simulations. The pressure was maintained at 1 atm with a Monte Carlo barostat, which attempts to adjust the system volume every 0.2 ps. The Langevin dynamics algorithm with a 1.0 ps−1 friction coefficient was used to hold the simulation temperature, which is at 303.15 K. The lengths of all bonds involving hydrogen were fixed and the integration time step was set to 2 fs. A force switching function was applied from 10 to 12 Å to gradually turn off the van der Waals interactions and the particle-mesh Ewald method with an error tolerance of 0.0005 was used to evaluate the electrostatic interactions.

### Simulation force field parameters

The same force field parameters were used in all other simulations in this study. The PARAM27 all-atom force field of CHARMM (MacKerell et al., 1998) with a modified version of dihedral cross-term correction (Mackerell et al., 2004) was used for the protein and the C36 lipid force field (Klauda et al., 2010) was used for POPC. Water molecules were modeled with the TIP3P potential (Jorgensen et al., 1983).
