# Conformational and dynamic plasticity in substrate-binding proteins underlies selective transport in ABC importers

## Authors

- Marijn de Boer<sup>1</sup> ([ORCID: 0000-0002-0067-9020](https://orcid.org/0000-0002-0067-9020))
- Giorgos Gouridis<sup>1</sup>
- Ruslan Vietrov<sup>4</sup>
- Stephanie L Begg<sup>6</sup>
- Gea K Schuurman-Wolters<sup>4</sup>
- Florence Husada<sup>1</sup>
- Nikolaos Eleftheriadis<sup>1</sup>
- Bert Poolman<sup>4</sup> ([ORCID: 0000-0002-1455-531X](https://orcid.org/0000-0002-1455-531X)) †
- Christopher A McDevitt<sup>6</sup> ([ORCID: 0000-0003-1596-4841](https://orcid.org/0000-0003-1596-4841)) †
- Thorben Cordes<sup>1</sup> ([ORCID: 0000-0002-8598-5499](https://orcid.org/0000-0002-8598-5499)) †

### Affiliations

1. Molecular Microscopy Research Group, Zernike Institute for Advanced Materials University of Groningen Groningen The Netherlands
2. Physical and Synthetic Biology, Faculty of Biology Ludwig-Maximilians-Universität München Planegg-Martinsried Germany
3. Laboratory of Molecular Bacteriology, Department of Microbiology and Immunology, Rega Institute for Medical Research KU Leuven Leuven Belgium
4. Department of Biochemistry, Groningen Biomolecular Science and Biotechnology Institute University of Groningen Groningen The Netherlands
5. Zernike Institute for Advanced Materials University of Groningen Groningen The Netherlands
6. Department of Microbiology and Immunology, The Peter Doherty Institute for Infection and Immunity University of Melbourne Melbourne Australia
7. Research Centre for Infectious Diseases, School of Biological Sciences The University of Adelaide Adelaide Australia

† Corresponding author

## Abstract

Substrate-binding proteins (SBPs) are associated with ATP-binding cassette importers and switch from an open to a closed conformation upon substrate binding, providing specificity for transport. We investigated the effect of substrates on the conformational dynamics of six SBPs and the impact on transport. Using single-molecule FRET, we reveal an unrecognized diversity of plasticity in SBPs. We show that a unique closed SBP conformation does not exist for transported substrates. Instead, SBPs sample a range of conformations that activate transport. Certain non-transported ligands leave the structure largely unaltered or trigger a conformation distinct from that of transported substrates. Intriguingly, in some cases, similar SBP conformations are formed by both transported and non-transported ligands. In this case, the inability for transport arises from slow opening of the SBP or the selectivity provided by the translocator. Our results reveal the complex interplay between ligand-SBP interactions, SBP conformational dynamics and substrate transport.

## Introduction

ATP-binding cassette (ABC) transporters facilitate the unidirectional trans-bilayer movement of a diverse array of molecules using the energy released from ATP hydrolysis (Higgins, 1992). They share a common architecture, with the translocator unit comprising two transmembrane domains (TMDs) that form the translocation pathway and two cytoplasmic nucleotide-binding domains (NBDs) which bind and hydrolyze ATP. ABC importers require an additional extra-cytoplasmic accessory protein referred to as a substrate-binding protein (SBP) or domain (SBD; hereafter SBDs and SBPs are both termed SBPs) (Berntsson et al., 2010; Scheepers et al., 2016; van der Heide and Poolman, 2002). ABC importers that employ SBPs can be subdivided as Type I or Type II based on structural and mechanistic distinctions (Locher, 2016; Swier et al., 2016). A unifying feature of the transport mechanism of Type I and Type II ABC importers is the binding and delivery of substrate from a dedicated SBP to the translocator unit for import into the cytoplasm.

Bacterial genomes encode multiple distinct ABC importers to facilitate the acquisition of essential nutrients such as sugars, amino acids, vitamins, compatible solutes, and metal ions (Higgins, 1992; Davidson et al., 2008). Many ABC importers can transport more than one type of substrate molecule using high-affinity interactions between SBPs and transported ligands (herein termed cognate substrates) (Berntsson et al., 2010). Despite low-sequence similarity between SBPs of different ABC importers, they share a common architecture comprising two structurally conserved rigid lobes connected by a flexible hinge region (Figure 1) (Berntsson et al., 2010). Numerous biophysical (Shilton et al., 1996) and structural analyses (Quiocho and Ledvina, 1996) indicate that ligand binding at the interface of the two lobes facilitates switching between two conformations, that is from an open to a closed conformation. Bending and unbending of the hinge region brings the two lobes together (closed conformation) or apart (open conformation), respectively. Crystallographic analyses show that the amount of opening varies between different SBPs; the lobe-movements observed range from small rearrangements as in the Type II SBP BtuF (Karpowich et al., 2003), to complete reorientation of both lobes by angles as large as 60° in the Type I SBP LivJ (Trakhanov et al., 2005). Nevertheless, the wealth of structural data permits a structural classification of SBPs, wherein the hinge region is the most defining feature of each sub-group or cluster (Figure 1) (Berntsson et al., 2010; Scheepers et al., 2016). Crystal structures of the same protein, but with different ligands bound, generally report the same degree of closing of the SBP (Trakhanov et al., 2005; Nishitani et al., 2012; Pandey et al., 2016; Magnusson et al., 2004; Quiocho et al., 1997).

![Figure 1.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig1-v2.jpg)

**Figure 1.:** X-ray crystal structures of PsaA (3ZK7; cluster A), MalE (1OMP; cluster B), OppA (3FTO; cluster C), OpuAC (3L6G; cluster F), SBD1 (4LA9; cluster F) and SBD2 (4KR5; cluster F) are all shown in the open, ligand-free conformation. Hinge regions are shown in blue and the two rigid lobes in grey. For classification of the proteins in clusters see (Berntsson et al., 2010; Scheepers et al., 2016).

Thus, it is assumed that the conformational switching of the SBPs enables the ABC transporter to allosterically sense the loading state of the SBP-ligand complex (‘translocation competency’), thereby contributing to transport specificity (Davidson et al., 2008; Quiocho and Ledvina, 1996). For example, crystal structures of the SBP MalE show that the protein adopts a unique closed conformation when interacting with cognate ligands maltose, maltotriose and maltotetraose (Quiocho et al., 1997), while the non-transported ligand β-cyclodextrin is bound by MalE (Hall et al., 1997a) but fails to trigger formation of the closed conformation (Hall et al., 1997b; Sharff et al., 1993; Skrynnikov et al., 2000). Ligands that are bound by the SBP, but not transported, are termed herein non-cognate ligands. Such findings suggest that only SBPs which adopt the closed conformation can productively interact with the translocator and initiate transport. However, the TMDs of certain ABC importers were also shown to interact directly with their substrates. In MalFGK2E (Oldham et al., 2013) from Escherichia coli and Art(QM)2 (Yu et al., 2015) from Thermoanaerobacter tengcongensi substrate-binding pockets have been identified inside the TMDs, and these might be linked to regulation of transport. Similar binding pockets within the TMDs have not been observed in the high-resolution structures of other ABC importers, although cavities through which the substrate passes in the transition of the TMD from outward- to inward-facing are likely to be present in all the transporters (Woo et al., 2012; Pinkett et al., 2007; Locher et al., 2002). Additional complexity exists for the coupling of SBP conformational switching and the ligand recognition process, as crystallographic (Flocco and Mowbray, 1994; Oswald et al., 2008), nuclear magnetic resonance (NMR) (Tang et al., 2007) and single-molecule (Feng et al., 2016; Gouridis et al., 2015) studies indicate that SBPs can undergo intrinsic conformational changes in the absence of substrate. Furthermore, crystal structures of the SBPs MalE and a D-xylose SBP were obtained in an open ligand-bound conformation (Duan and Quiocho, 2002; Sooriyaarachchi et al., 2010). Such observations question the precise relationship between SBP-ligand interactions, SBP conformational changes and their involvement in transport function.

A range of biophysical and structural approaches have been used to decipher the mechanistic basis of SBP-ligand interactions (Shilton et al., 1996; Quiocho and Ledvina, 1996; Trakhanov et al., 2005; Hall et al., 1997b; Skrynnikov et al., 2000). However, these techniques only provide information on the overall population of molecules. Recent advances in single-molecule methodologies now permit new insight into the conformational heterogeneity, dynamics and occurrences of rare events in SBPs (Feng et al., 2016; Gouridis et al., 2015; Kim et al., 2013; Seo et al., 2014; Husada et al., 2015; Lerner et al., 2018), which are difficult to obtain in bulk measurements. Here, we combined single-molecule Förster resonance energy transfer (smFRET) (Ha et al., 1996) and transport measurements to investigate how cognate and non-cognate substrates influence the conformational states and the underlying dynamics of SBPs. Six distinct SBPs were selected (Figure 1) (Fulyani et al., 2016; Wolters et al., 2010; Ferenci, 1980; McDevitt et al., 2011; Berntsson et al., 2011), based on two criteria. First, they cover the breadth of SBP structural classes: PsaA (cluster A), MalE (cluster B), OppA (cluster C), SBD1 and SBD2 of GlnPQ, and OpuAC (all cluster F). The selected SBPs provide coverage of hinge region diversity (Berntsson et al., 2010; Scheepers et al., 2016), thereby addressing a hypothesized key determinant in SBP conformational dynamics. Moreover, subtle structural or sequence differences among SBPs that belong to the same cluster are addressed by examining SBD1, SBD2 and OpuAC that all belong to cluster F. Second, the selected SBPs belong to Type I and Type II ABC importers with extensively characterized substrate (cognate and non-cognate) interactions, such as metal ions (PsaA) (McDevitt et al., 2011), sugars (MalE) (Ferenci et al., 1986), peptides (OppA) (Doeven et al., 2004), amino acids (SBD1 and SBD2) (Fulyani et al., 2016), and compatible solutes (OpuAC) (Wolters et al., 2010).

## Results

### Multiple SBP conformations are translocation competent

Crystal structures of SBPs suggest that ligand binding is coupled to switching between an open and a closed conformation. Mechanistically, this process has been linked to the allosteric regulation of substrate transport (Davidson et al., 2008; Shilton et al., 1996; Quiocho and Ledvina, 1996; Oldham and Chen, 2011; Hor and Shuman, 1993; Doeven et al., 2008; Hollenstein et al., 2007; Davidson et al., 1992). Here, we assessed this model by investigating the interaction of six SBPs, PsaA, MalE, OppA, SBD1, SBD2 and OpuAC, with a range of cognate substrates. We employed single-molecule FRET to analyze SBP conformations, wherein each of the two SBP lobes was labeled with either a donor or an acceptor fluorophore (Figure 2A) (Gouridis et al., 2015; Kapanidis et al., 2004). Surface-exposed and non-conserved residues, showing largest distance changes according to the crystal structures of the open and closed states, were selected as suitable cysteine positions for labeling. Labeling and surface-immobilization of the protein molecules did not alter the ligand dissociation constant KD (Table 1). In our assays, the inter-dye distance reports on the relative orientation and distance between the SBP lobes and is thus indicative for the degree of closing. Steady-state anisotropy measurements indicate that the dyes retain sufficient rotational freedom (Table 2) so that relative inter-dye distance can be assessed via the apparent FRET efficiency of freely diffusing or surface-immobilized protein molecules. Although this approach monitors only a single distance in the SBP, it permits rapid screening of ligand induced conformational changes under physiologically relevant conditions.

**Table 1.**
 Dissociation constant KD of substrate-binding proteins.


<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th></th>
      <th colspan="2">KD (µM)</th>
      <th></th>
    </tr>
    <tr>
      <th colspan="2">Protein*</th>
      <th>Ligand</th>
      <th>Freely-diffusing protein</th>
      <th>Surface-tethered protein</th>
      <th>KD WT protein¶ (µM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OpuAC(V360C/N423C)</td>
      <td colspan="2">Glycine betaine</td>
      <td>3.4 ± 0.4†</td>
      <td>3.1‡</td>
      <td>4–5 (Wolters et al., 2010)</td>
    </tr>
    <tr>
      <td>OppA(A209C/S441C)</td>
      <td colspan="2">RPPGFSFR</td>
      <td>7.0 ± 1†</td>
      <td>14 ± 5#</td>
      <td>5 ± 3#</td>
    </tr>
    <tr>
      <td>SBD2(T369C/S451)</td>
      <td colspan="2">Glutamine</td>
      <td>1.2 ± 0.2§</td>
      <td>0.5‡</td>
      <td>0.9 ± 0.1 (Gouridis et al., 2015)</td>
    </tr>
    <tr>
      <td>SBD1(T159C/G87C)</td>
      <td colspan="2">Asparagine</td>
      <td>0.34 ± 0.03§</td>
      <td>0.3‡</td>
      <td>0.2 ± 0.0 (Gouridis et al., 2015)</td>
    </tr>
    <tr>
      <td>MalE(T36C/S352C)</td>
      <td colspan="2">Maltose</td>
      <td>1.7 ± 0.3†</td>
      <td>2.2‡</td>
      <td>1-2 (Hall et al., 1997a, Kim et al., 2013)</td>
    </tr>
    <tr>
      <td>MalE(T36C/S352C)</td>
      <td colspan="2">Maltotriose</td>
      <td>0.6 ± 0.2†</td>
      <td>0.9‡</td>
      <td>0.2-2 (Hall et al., 1997a, Kim et al., 2013)</td>
    </tr>
  </tbody>
</table>

_*. KD could not be determined reliably for labeled PsaA due to background metal contamination.†. Population of the closed conformation P in the presence of a ligand concentration L was determined using solution-based smFRET. The KD=L (1-P)/P for a one-binding site model. Data corresponds to mean ± s.d. of duplicate experiments with the same protein sample.‡. Figure 2—figure supplement 1§. Figure 4—figure supplement 2#. Figure 2—figure supplement 2¶. The KD values of wildtype (WT) proteins are obtained from the indicated references._

**Table 2.**
 Steady-state anisotropy values.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">Anisotropy</th>
    </tr>
    <tr>
      <th></th>
      <th>Alexa555</th>
      <th>Alexa647</th>
      <th>Cy3B</th>
      <th>Atto647N</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Free dye</td>
      <td>0.25</td>
      <td>0.20</td>
      <td>0.08</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>OpuAC(V360C/N423C)</td>
      <td>NA</td>
      <td>NA</td>
      <td>0.17</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>OppA(A209C/S441C)</td>
      <td>0.25</td>
      <td>0.19</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>SBD1(G87C/T159C)</td>
      <td>0.27</td>
      <td>0.19</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>SBD2(T369C/S451)</td>
      <td>0.26</td>
      <td>0.20</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>MalE(T36C/S352C)</td>
      <td>0.29</td>
      <td>0.24</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>PsaA(V76C/K237C)</td>
      <td>0.28</td>
      <td>0.22</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>

_NA: not applicable. Data correspond to mean (s.d. below < 0.01) of duplicate experiments, using the same labeled protein sample._

![Figure 2.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig2-v2.jpg)

**Figure 2.:** (A) Experimental strategy to study SBP conformational changes via FRET. Solution-based apparent FRET efficiency histograms of OpuAC(V360C/N423C) (B), PsaA(V76C/K237C) (C), MalE(T36C/S352C) (D), SBD1(T159C/G87C) (E), SBD2(T369C/S451) (F) and OppA(A209C/S441C) (G) in the absence (grey bars) and presence of different cognate substrates (green bars). The OppA substrates are indicated by one-letter amino acid code. Bars are the data and the solid line a Gaussian fit. The 95% confidence interval of the Gaussian distribution mean is shown in Supplementary file 3, and the interval center is indicated by vertical lines (solid and dashed). (H) Mean of the Gaussian distribution of MalE labeled at T36/S352 (black), T36/N205 (green) or K34/R352 (blue). Error bars indicate 95% confidence interval.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Representative fluorescence trajectories (left) and apparent FRET efficiency histograms from all fluorescence trajectories (right) of MalE(T36C/S352C) (A), SBD2(T369C/S451) (B), OpuAC(V360C/N423C) (C), SBD1(T159C/G87C) (D) and OppA(A209C/S441C) (E) in the presence of the indicated substrate concentration. In the fluorescence trajectories: the top panel shows the calculated apparent FRET efficiency (blue) from the donor (green) and acceptor (red) photon counts as shown in the bottom panels. The most probable state-trajectory of the Hidden Markov Model (HMM) is shown by the orange line. Statistics in Supplementary file 4. The histogram was fitted with two Gaussian distribution to obtain the relative population of the high FRET state $P$. Ignoring the small contribution of intrinsic closing (Figure 3H), we use $K_{D}=L(1-P)/P$ (one site-binding model), where $L$ is the indicated ligand concentration, to determine $K_{D}$ (see Table 1).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Representative fluorescence trajectories of OppA(A209C/S441C) at different peptide (RPPGFSFR) concentrations; donor (green) and acceptor (red) photon counts. The top panel shows the calculated apparent FRET efficiency (blue) with the most probable state-trajectory of the Hidden Markov Model (HMM) (orange). Dwell time histogram of the high FRET (closed conformation) (B) and low FRET state (open conformation) (C) as obtained from the most probable state-trajectory of the HMM. Bars are the data and the solid line is an exponential fit. Statistics in Supplementary file 4. (D) Average closing rate (rate of low to high FRET state; black) and average lifetime of the ligand-bound conformation (lifetime high FRET state; purple). Data correspond to mean ± s.e.m. and the solid line a linear fit. Slope or intercept of the fit are shown (95% confidence interval). From the fit a KD of 14 ± 5 µM (95% confidence interval) is obtained. (E) Isothermal calorimetry binding isotherm of the titration of OppA with RPPGFSFR, obtaining KD of 5 ± 3 µM (mean ± s.d., n = 3). Points are the data and the solid line a fit to a one site-binding model.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Solution-based apparent FRET efficiency histogram of MalE(T36C/S352C) (A) and OppA(A209C/S441C) (B) in the absence and presence of different cognate substrates as indicated. The OppA substrates are indicated by one-letter amino acid code. Bars are the data and solid line a Gaussian fit. The 95% confidence interval for the mean of the Gaussian distribution is shown in Supplementary file 3, and the interval center is indicated by vertical lines (solid and dashed).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Solution-based apparent FRET efficiency histogram of MalE(T36C/S352C), MalE(T36C/N205C) and MalE(K34C/R354C) in the absence and presence of different cognate substrates as indicated. Bars are the data and the solid line a Gaussian fit. The 95% confidence interval for the mean of the Gaussian distribution is shown in Supplementary file 3, and the interval center is indicated by vertical lines (solid and dashed). Structure of ligand-free MalE (PDB ID: 1OMP) with corresponding donor and acceptor fluorophore positions is indicated above the histograms.

The apparent FRET efficiency distributions of individual and freely diffusing SBPs were determined in the presence and absence of their cognate substrates using confocal microscopy. Saturating concentrations of cognate substrate, above the KD (Table 1), shift the FRET efficiency histograms and the fitted Gaussian distributions to higher values compared to the ligand-free SBPs (Figure 2B–G; Supplementary file 3), indicating a reduced distance between the SBP lobes and inferred to be closure of the proteins. For individual surface-immobilized SBPs, we observed ligand-induced opening and closing transitions in the presence of ligand concentrations at the respective KD value (Figure 2—figure supplement 1). The solution-based FRET distributions of ligand-bound and ligand-free SBPs are unimodal and thus do not reveal any substantial conformational heterogeneity, such as a pronounced closing in the absence of substrate or a substantial population of an open-liganded state (vide infra). This strongly suggests that ligands are bound via an induced-fit mechanism, unless dynamics occur on timescales faster than milliseconds. This inference was confirmed for OppA by examining individual surface-immobilized proteins and demonstrating that substrate-induced SBP closing follows first-order kinetics while the opening obeys zeroth-order kinetics (Figure 2—figure supplement 2) (Kim et al., 2013).

Further examination of the FRET distributions shows that multiple substrate-bound SBP conformations exist for SBD1, SBD2 and MalE (Figure 2D–F). For the amino acid binding-proteins SBD1 and SBD2, the cognate substrates (Fulyani et al., 2016) asparagine and glutamine for SBD1, and glutamine and glutamate for SBD2 all stabilize a distinct protein conformation, as shown by the FRET efficiency histograms and fitted Gaussian distributions (Figure 2E–F; Supplementary file 3). Notably, closure of SBD1 by asparagine reduces the inter-dye distance compared to the ligand-free protein by ~9 Å (Supplementary file 3). In contrast, glutamine binding reduces the distance by ~5 Å, suggesting that only a partial closing of SBD1 occurs. In SBD2, glutamine and glutamate reduce the distance ~9 and ~7 Å, respectively (Supplementary file 3).

For the maltodextrin binding-protein MalE, we examined the effect of cognate maltodextrins (Ferenci, 1980), ranging from two to seven glucosyl units, on the protein conformation. Comparison of the FRET efficiency histograms of the different MalE-ligand complexes shows that at least three distinct ligand-bound MalE conformations exist (Figure 2D; Figure 2—figure supplement 3A; Supplementary file 3). In contrast to SBD1 and SBD2, some cognate substrates did not induce a unique MalE conformation (Figure 2—figure supplement 3A). For example, maltopentaose and maltohexaose elicited the same FRET change, and triggered the formation of a partially closed MalE conformation with a ~7 Å reduction in the inter-dye distance. This conformational state is different from the fully closed form of MalE, induced by maltose, maltotriose and maltotetraose, wherein the inter-dye distance is reduced by ~10 Å. Further, it is also distinct from the other partially closed conformation induced by maltoheptaose where the inter-dye distance is reduced by ~5 Å. These results were confirmed by examining different inter-dye distances (Figure 2H; Figure 2—figure supplement 4). However, whether this conformational plasticity is a universal feature among SBPs needs to be investigated further, because in OppA the four examined cognate substrates (Doeven et al., 2004) elicited the same FRET change (Figure 2G; Figure 2—figure supplement 3B). The findings on the conformational changes (and differences) for each SBP were shown to be statistically robust by the non-parametric two-way Kolmogorov-Smirnov (KS) test (p-values in Supplementary file 1), which indicates the absence of any fitting bias. Taken together, these data indicate that although the examined SBPs have a single open conformation, a productive interaction between the SBP and the translocator does not require a single, unique closed SBP conformation. The structural flexibility of the SBP permits the formation of one or more ligand-bound conformations, all of which are able to interact with the translocator and initiate transport (Fulyani et al., 2016; Wolters et al., 2010; Ferenci, 1980; McDevitt et al., 2011; Doeven et al., 2004).

### Intrinsic conformational changes of SBPs

We then investigated whether the conformational changes in the SBPs that were triggered by their ligands, can also occur in their absence. To address this, we investigated surface-tethered SBPs in the absence of ligand and used confocal scanning microscopy to obtain millisecond temporal resolution. Compared to the solution-based smFRET experiments, individual surface-tethered SBPs greatly increase the sensitivity to detect rare events. In contrast to prior work (Feng et al., 2016; Gouridis et al., 2015; Kim et al., 2013; Seo et al., 2014), the labeled SBPs were supplemented with high concentrations of unlabeled protein (10–20 μM), or the divalent chelating compound ethylenediaminetetraacetic acid (1 mM EDTA for PsaA), to remove any contaminating ligands (Figure 3A). Contaminations could otherwise lead to conformational changes that are misinterpreted as intrinsic closing of the SBP. Consistent with the solution-based measurements, all SBPs were predominantly in a low FRET state (open conformation; Figure 3B–G; Figure 3—figure supplement 1). For ligand-free MalE, PsaA and OpuAC, no transitions to higher FRET states were observed within a total observation time of >8 min for each SBP (Figure 3B–D; Supplementary file 4). In SBD1, SBD2 and OppA rare transitions to a high FRET state can be observed and have an average lifetime of 205 ± 36, 90 ± 11 and 211 ± 42 ms (mean ± s.e.m.), respectively (Figure 3E–G; Figure 3—figure supplement 1D–F). Transitions toward these states occur only rarely, that is, on average 2–8 times per minute (Figure 3H; Supplementary file 4). To rule out that these infrequent FRET transitions are caused by rare binding events arising from any non-chelated ligand, we analyzed the protein conformational dynamics of SBD1, SBD2 and OppA in the presence of a 4 to 10-fold lower concentration of unlabeled protein. We observed that the FRET transitions occur with a similar frequency and have the same average lifetime compared to when 10–20 µM unlabeled protein is present (Figure 3—figure supplement 2). This suggests that all potential ligand contamination is efficaciously scavenged by unlabeled protein, thus providing compelling evidence that the rare FRET transitions observed in SBD1, SBD2 and OppA represent intrinsic closing of the protein. Therefore, some SBPs have the ability to also close without the ligand on the second timescale. However, not all SBPs show intrinsic conformational transitions, unless these occur below the temporal resolution of the measurements (millisecond timescale). Overall, the data indicate that diversity exists in the conformational dynamics of ligand-free SBPs.

![Figure 3.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of the experimental strategy to study the conformational dynamics of ligand-free SBPs. Representative fluorescence trajectories of OpuAC(V360C/N423C) (B), PsaA(V76C/K237C) (C), MalE(T36C/S352C) (D), SBD1(T159C/G87C) (E), OppA(A209C/S441C) (F) and SBD2(T369C/S451) (G) in the absence of substrate. 10–20 μM of unlabeled protein or 1 mM EDTA (for PsaA) was added to scavenge any ligand contaminations. In all fluorescence trajectories presented in the figure: top panel shows calculated apparent FRET efficiency (blue) from the donor (green) and acceptor (red) photon counts as shown in the bottom panels. Orange lines indicate average apparent FRET efficiency value or most probable state-trajectory of the Hidden Markov Model (HMM). Statistics in Supplementary file 4. (H) Percentage of time a SBP is in the high FRET state. Statistics in Supplementary file 4.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Representative fluorescence trajectories of OpuAC(V360C/N423C) (A), PsaA(V76C/K237C) (B), MalE(T36C/S352C) (C), SBD1(T159C/G87C) (D), OppA(A209C/S441C) (E) and SBD2(T369C/S451) (F) in the absence of substrate and under saturating conditions of ligand, as indicated. In the absence of ligand, 10–20 μM of unlabeled protein or 1 mM EDTA (for PsaA) was added to scavenge any ligand contaminations. The top panels show the calculated apparent FRET efficiency (blue) from the donor (green) and acceptor (red) photon counts as presented in bottom panels. The orange line indicates the average apparent FRET efficiency value or most probable state-trajectory of the HMM. Statistics in Supplementary file 4.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Closing rate (A) and average lifetime of the closed conformation (B) for OppA, SBD1 and SBD2 in the absence of ligand and in the presence of different concentrations of unlabeled protein to scavenge potential ligand contaminations. Examples of the high FRET transitions are shown in Figure 3 and Figure 3—figure supplement 1. Error bars correspond to s.e.m. The closing rate was determined by dividing the total observation time of all molecules by the number of observed high FRET transitions. The statistical significance of the average closed state lifetime was determined by a two-tailed unpaired t-tests. The statistical significance of the closing rate was determined by testing for the difference in the proportion of time-bins in which a low to high FRET transition is made and using the z-test. Statistics in Supplementary file 4.

### How do non-transported substrates influence the SBP conformation?

Ensemble FRET measurements using all proteinogenic amino acids and citruline were performed to obtain full insight into substrate specificity of SBD1 and SBD2 of GlnPQ. We find that asparagine, glutamine and histidine elicit a FRET change in SBD1, and glutamine in SBD2 (Figure 4—figure supplement 1); glutamate triggers a change in SBD2 at low pH, that is, when a substantial fraction of glutamic acid is present. No other amino acid affected the apparent FRET efficiency. However, arginine and lysine competitively inhibit the conformational changes induced by asparagine binding to SBD1 and glutamine binding to SBD2 (Figure 4—figure supplement 2). Uptake experiments in whole cells and in proteoliposomes show that histidine, lysine and arginine are not transported by GlnPQ, but these amino acids can inhibit the uptake of glutamine (via SBD1 and SBD2) and asparagine (via SBD1) (Figure 4A–C). Thus, some amino acids interact with the SBPs of GlnPQ but fail to trigger transport. Similar ligands have been identified for MalE, OpuAC and PsaA (Hall et al., 1997a; Wolters et al., 2010; Ferenci, 1980; McDevitt et al., 2011), and we refer to these as non-cognate substrates. We then used smFRET to test whether or not ligand-induced SBP conformational changes allow discrimination of cognate from non-cognate substrates.

![Figure 4.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig4-v2.jpg)

**Figure 4.:** (A) Time-dependent uptake [14C]-asparagine (5 μM), [14C]-glutamine (5 μM), [14C]-arginine (100 μM), [14C]-histidine (100 μM) and [3H]-lysine (100 μM) by GlnPQ in L. lactis GKW9000 complemented in trans with a plasmid for expressing GlnPQ; the final amino acid concentrations are indicated between brackets. Points are the data and the solid line a hyperbolic fit. Time-dependent uptake of glutamine (B) and asparagine (C) in proteoliposomes reconstituted with purified GlnPQ (see Materials and methods section). The final concentration of [14C]-glutamine and [14C]-asparagine was 5 μM, respectively; the amino acids indicated in the panel were added at a concentration of 5 mM. Solution-based apparent FRET efficiency histogram of SBD1(T159C/G87C) (D), SBD2(T369C/S451) (E), MalE(T36C/S352C) (F), OpuAC(V360C/N423C) (G) and PsaA(V76C/K237C) (H) in the presence of non-cognate (red bars) substrates as indicated. Bars are the data and solid line a Gaussian fit. The 95% confidence interval for the distribution mean is shown in Supplementary file 3. The interval center is indicated by vertical lines (solid and dashed).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The mean apparent FRET change of SBD1 (top) and SBD2 (bottom) in the presence of 5 mM of the indicated amino acids relative to their absence; measurements were performed in 50 mM KPi, 50 mM KCl, pH 7.4. Amino acids are indicated by their three letter abbreviation. Data correspond to mean ± s.d. of the apparent FRET change of duplicate measurements with the same labeled protein sample.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Solution-based apparent FRET efficiency histograms of SBD1(T159C/G87C) (A and C) and SBD2(T369C/S451) (B) in the presence of different ligand concentrations as indicated. Bars are the data and the solid lines a fit to a mixture model with two Gaussian distributions or a fit with a single Gaussian distribution. The mean of the Gaussian distributions was obtained from the extreme conditions and fixed in the mixture model. Fraction of SBD1 bound to asparagine (D), SBD2 bound to glutamine (E) and SBD1 bound to histidine (F). Points are the data and the solid line a fit to a one site-binding model. (G) Estimated dissociation constants KD as obtained from the fit. Error bars represent 95% confidence interval.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Solution-based apparent FRET efficiency histogram of PsaA(E74C/K237C) in the presence and absence of metals as indicated. Bars are the data and solid line a Gaussian fit. The 95% confidence interval for the distribution mean is shown in Supplementary file 3. The interval center is indicated by vertical lines (solid and dashed).

At saturating concentrations of most non-cognate ligands the FRET efficiencies are altered compared to the ligand-free conditions (Figure 4D–H; Supplementary file 3; Supplementary file 1). This shows that, similar to cognate ligands (Figure 3B–G), non-cognate ligand binding is coupled to SBP conformational changes. However, this is not true in all cases, as the binding of the non-cognate substrates, that is, arginine or lysine for SBD1 and arginine for SBD2 do not alter the FRET efficiency histograms (Figure 4D–E), suggesting that these ligands bind in the open conformation of the SBP and do not trigger a conformational change.

Further analysis of the non-cognate ligand-induced conformational changes reveals states that vary, from a minor opening (carnitine-OpuAC in Figure 4G), to partial (histidine-SBD1 in Figure 4D; various maltodextrin-MalE complexes in Figure 4F; proline-OpuAC in Figure 4G) or full closing (Zn2+-PsaA in Figure 4H) of the SBP relative to the ligand-free state of the corresponding protein. The data of full closing by Zn2+ (non-cognate) and Mn2+ (cognate) were confirmed by examining different inter-dye positions in PsaA (Figure 4—figure supplement 3) and are in line with prior crystallographic analyses (McDevitt et al., 2011; Lawrence et al., 1998). Noteworthy, the non-cognate substrate histidine and the cognate substrate glutamine induce both partial closing of SBD1 (Figure 4D). However, histidine elicited a larger FRET shift in SBD1 (~7 Å reduction in inter-dye distance) than cognate glutamine (~5 Å), but smaller than the cognate substrate asparagine (~9 Å), which induced full closing (Figure 4D, Supplementary file 3). In contrast, the FRET shift induced with certain non-cognate ligands in MalE (β-cyclodextrin, maltotriitol and maltotetraitol) and OpuAC (proline) are smaller (or similar; vide infra) than with their cognate ligands (Figure 4F–G), which corresponds with a reduction in the inter-dye distance of ~3–4 Å, in contrast to ~9–10 Å for full closure of these SBPs (Supplementary file 3). Intriguingly, the data also suggest that the partially closed SBP-ligand complexes of MalE formed with the non-cognate substrates maltooctaose or maltodecaose are similar to that of the cognate substrate maltoheptaose (Figure 4F). Again, this result was confirmed by examining different inter-dye positions in MalE (Supplementary file 3). The findings on the conformational changes (and differences) for each SBP were shown to be statistically robust by the two-way KS test (Supplementary file 1).

In summary, similar to cognate substrates, non-cognate substrates do not induce a single unique ligand-bound SBP state, and solely from the degree of SBP closing a translocator cannot readily discriminate cognate from non-cognates substrates. Notable exceptions are the substrates that do not induce closing and keep the SBP in the open state. This raises fundamental questions as to the mechanistic basis for how certain non-cognate substrates are still excluded from import.

### Altered SBP opening renders PsaA permissive for non-cognate ligand transport

The inability of certain substrates to be transported, while they appear to induce SBP conformations that are similar to those associated with cognate substrates, was observed for MalE (Figure 4F) and PsaA (Figure 4H). First, this was investigated further for PsaA. Upon addition of 1 mM EDTA to PsaA-Mn2+, lower FRET efficiencies are instantaneously recorded (Figure 5A), indicating that the lifetime of the closed PsaA-Mn2+ conformation is shorter than a few seconds. By contrast, Zn2+ kept PsaA closed, irrespective of the duration of the EDTA treatment (up to 15 min) (Figure 5B). Irreversible and reversible binding of these metals was shown previously (Couñago et al., 2014), which can now be explained by the fast and slow opening of PsaA in the presence of Mn2+ and Zn2+, respectively. The extremely slow opening of PsaA may explain why Zn2+ is not transported by PsaBCA, as opening of the SBP is required for release of the ligand to the translocator. However, it is also possible that the translocator controls the transport specificity (Oldham et al., 2013; Yu et al., 2015). To discriminate between these two scenarios, we examined the impact of altered SBP dynamics on the transport activity of PsaBC. We substituted an aspartate in the binding site with asparagine (D280N), which has previously been shown to perturb the stability of the Zn2+-bound SBP (Couñago et al., 2014). Analysis of PsaA and PsaA(D280N), at saturating Zn2+ concentrations, revealed similar FRET efficiency histograms for the two proteins (Figure 5C; Supplementary file 3). However, in contrast to the Zn2+-PsaA complex, opening of the PsaA(D280N) complex renders Zn2+ accessible to EDTA, similar to the cognate ligand Mn2+ (Figure 5A,C). The ability of PsaA(D280N) to open and release Zn2+ was then assessed by measuring the cellular accumulation of Zn2+ within Streptococcus pneumoniae, the host organism. This was achieved by replacement of the psaA gene with the D280N mutant allele (ΩpsaAD280N) in a strain permissive for Zn2+ accumulation, that is incapable of Zn2+ efflux due to deletion of the exporter CzcD (ΩpsaAD280NΔczcD) (Begg et al., 2015). Our data show that cellular Zn2+ accumulation increases in the strain expressing PsaBC with PsaA(D280N) but not with wild-type PsaA (Figure 5D). These results demonstrate that the altered conformational dynamics of the PsaA derivative renders ligand release permissive for transport of non-cognate Zn2+ ions. The data also show that translocator activity is not directly influenced by the nature of the metal ion released by PsaA. Collectively, our findings show that transport specificity of PsaBCA is dictated by the opening kinetics of PsaA.

![Figure 5.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig5-v2.jpg)

**Figure 5.:** Solution-based apparent FRET efficiency histograms of PsaA(V76C/K237C) in the presence of Mn2+ (A) or Zn2+ (B) and PsaA(D280N) in the presence of Zn2+ (C) upon addition of 10 mM EDTA and incubated for the indicated duration. Bars are the data and the solid line a Gaussian fit. The 95% confidence interval for the mean of the Gaussian distribution can be found in Supplementary file 3, and the interval center is indicated by vertical lines (solid, metal-free and dashed, metal-bound). (D) Whole cell Zn2+ accumulation of S. pneumoniae D39 and mutant strains in CDM supplemented with 50 µM ZnSO4 as determined by ICP-MS. Data correspond to mean ± s.d. μg Zn2+.g−1 dry cell weight from three independent biological experiments. Statistical significance was determined by one-way ANOVA with Tukey post-test (***p < 0.005 and ****p < 0.0001).

### MalE conformational dynamics with cognate and non-cognate substrates

Next, we determined the conformational dynamics of MalE induced by maltoheptaose, maltooctaose and maltodecaose. Similar to Zn2+ and Mn2+ in PsaA (Figure 4H), these substrates appear to induce similar MalE conformations (Figure 4F) but only maltoheptaose is transported (Ferenci, 1980). Measurements on individual surface-tethered MalE proteins, in the presence of maltoheptaose, maltooctaose or maltodecaose, show frequent switching between low and higher FRET states, corresponding to opening and (partial) closing of MalE (Figure 6A–D). Consistent with the solution-based smFRET measurements, the average apparent FRET efficiency of the high FRET state is similar for these maltodextrins and lower than with maltose (Figure 6—figure supplement 1). The mean lifetime of the ligand-bound conformations (mean lifetime of the high FRET states) are 328 ± 8 ms for cognate maltoheptaose and 319 ± 12 ms and 341 ± 8 ms for non-cognate maltooctaose and maltodecaose, respectively (mean ± s.e.m.; Figure 6A, Figure 6—figure supplement 2). So, contrary to PsaA-Zn2+ (Figure 5), a slow opening of MalE and inefficient ligand release kinetics cannot explain why maltooctaose and maltodecaose are not transported; the average lifetimes with maltooctaose or maltodecaose are not significantly different from that with maltoheptaose (p = 0.68, one-way analysis of variance (ANOVA); Figure 6A). Most likely, the failure of the maltose system to transport maltooctaose and maltodecaose originates from the size limitations of the translocator domain of MalFGK2 (Oldham et al., 2013).

![Figure 6.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig6-v2.jpg)

**Figure 6.:** (A) Mean lifetime of the ligand-bound conformations of MalE, obtained from all single-molecule fluorescence trajectories in the presence of different maltodextrins as indicated. Data corresponds to mean ± s.e.m. Data in Figure 6—figure supplement 2. Statistical significance was determined by two-tailed unpaired t-tests (***p < 0.005 and ****p < 0.0001). (B, C, D, E, F and G) Representative fluorescence trajectories of MalE(T36C/S352C) in the presence of different substrates as indicated. In all fluorescence trajectories presented: top panel shows calculated apparent FRET efficiency (blue) from the donor (green) and acceptor (red) photon counts as shown in the bottom panels. Most probable state-trajectory of the Hidden Markov Model (HMM) is shown (orange). (H) Published ATPase activity (Hall et al., 1997a) linked to the lifetime of the closed MalE conformation induced by transport of different cognate substrates as indicated. Points are the data and the solid line a simple linear regression fit.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Surface-based apparent FRET efficiency histogram of MalE(T36C/S352C) in the presence of different maltodextrin substrates as indicated. From the probable state-trajectory of the Hidden Markov Model (HMM), the apparent FRET efficiencies of the low (ligand-free conformation) and high FRET state (closed ligand-bound conformation) were obtained. The final histogram was constructed from all fluorescence trajectories. Representative fluorescence trajectories are shown in Figure 6B–G. Bars are the data and solid line a Gaussian fit. The 95% confidence interval for the distribution mean is indicated. The average apparent FRET efficiency of the solution-based smFRET measurements (Figure 2—figure supplement 3A) is indicated by vertical lines.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Dwell time histogram of the high FRET (closed ligand-bound conformation) as obtained from the most probable state-trajectory of the Hidden Markov Model (HMM) of all molecules per condition as shown in Figure 6B–G. Grey bars are the data and the solid line an exponential fit. Statistics in Supplementary file 4.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** (A) Representative fluorescence trajectories of MalE(T36C/S352C/A96W/I329W) in the presence of 10 nM maltose. Fluorescence trajectories: the top panel shows the calculated apparent FRET efficiency (blue) from the donor (green) and acceptor (red) photon counts as shown in the bottom panel. The most probable state-trajectory of the Hidden Markov Model (HMM) is shown (orange). (B) Dwell time histogram of the high FRET state (closed conformation) as obtained from the most probable state-trajectory of the HMM of all molecules. Grey bars are the data and the solid line is an exponential fit. Statistics in Supplementary file 4. (C) Solution-based apparent FRET efficiency histogram of MalE and MalE(A96W/I329W) in the presence of 1 mM maltose for the indicated inter-dye positions. Bars are the data and solid line a Gaussian fit. The 95% confidence interval for the mean of the Gaussian distribution is indicated. The FRET distributions of the wildtype and mutant protein are not significantly different; p = 0.28 (T36C/S352C) and p = 0.30 (K34C/R352) using the two-way KS test.

### Translocator/SBP interplay determines the rate of transport

Finally, we sought to elucidate the mechanistic basis for how substrate preference arises in the maltose system and to what degree the translocator contributes to this process. First, we investigated how the MalE conformational dynamics influences the transport rate of the substrate maltose. For this we used the hinge-mutant variant MalE(A96W/I329W) that has different conformational dynamics compared to the wild-type protein (Figure 6E; Figure 6—figure supplement 3A–B) (Kim et al., 2013). The mutations are believed to not affect SBP-translocator interactions since they are situated on the opposite side of the interaction surface of the SBP (Oldham and Chen, 2011; Gould et al., 2009).

At saturating concentrations of maltose, the FRET efficiency distributions of MalE and MalE(A96W/I329W) are indistinguishable (Figure 6—figure supplement 3C). This could be confirmed by two different inter-dye positions in each protein. Therefore, changes in the rate of maltose transport unlikely arise from differences in SBP docking onto the TMD, since similar SBP conformations are involved. Nonetheless, cellular growth and the maltose-induced ATPase activity are reduced for MalE(A96W/I329W) (Gould et al., 2009; Bao and Duong, 2012). Analysis of the mean lifetime of the closed conformation of MalE(A96W/I329W) shows that the opening of the protein is almost three orders of magnitude slower than in the wild-type protein [63 ± 6 ms (mean ±s.e.m.) in MalE versus 28 ± 5 s (mean ± s.e.m.) in MalE(A96W/I329W); Figure 6A; Figure 6—figure supplement 3B]. These observations suggest that the maltose-stimulated cellular growth and ATPase activity are reduced due to the slower ligand release of MalE(A96W/I329W) compared to wildtype MalE. This negative correlation between the MalE lifetime and the transport activity is in line with the observation that Zn2+-PsaA(D280N) opens fast, so that Zn2+ transfer to the translocator and import can occur, whereas in wildtype Zn2+-PsaA the opening is (extremely) slow and import does not occur (Figure 5B–D).

We then investigated the relationship between maltodextrin-specific lifetimes of the MalE closed conformations and published transport rates or ATPase activities of the full transport system (Hall et al., 1997a). Here, we focused on the cognate substrates maltose, maltotriose and maltotetraose. Analysis of individual surface-tethered MalE proteins in the presence of these substrates shows that the average lifetime of the closed conformation with maltose, maltotriose and maltotetraose are 63 ± 6, 124 ± 4, and 150 ± 8 ms (mean ± s.e.m.), respectively (Figure 6A; Figure 6E–G; Figure 6—figure supplement 2). Thus, these lifetimes correlate positively with their stimulation of the ATPase activity (Figure 6H) (Hall et al., 1997a). A positive relationship also exists between the lifetimes with maltose and maltotetraose (63 ± 6 and 150 ± 8 ms, respectively) and their corresponding transport rates (transport of maltotetraose is ~1.5 fold higher than of maltose) (Hall et al., 1997a). This positive correlation is inconsistent with our earlier findings that a shorter SBP lifetime results in a faster rate of transport. However, this relationship only holds when the SBP conformational dynamics are altered, while leaving all other rate-determining steps of the transport process unaffected. Thus, the observation that some maltodextrins induce a faster opening of MalE, while their corresponding transport and/or stimulation of ATP hydrolysis are slower, implies that the kinetics of certain other rate-determining steps are substrate-dependent. Faster transport or ATP hydrolysis can arise when certain maltodextrins trigger these steps more efficiently than others, thereby overcoming the slower opening of MalE. These steps most likely occur after opening of MalE, as these differences in transport activity are unlikely to arise from differences in docking of MalE onto the TMDs (crystallographic (Quiocho et al., 1997) and smFRET data (Supplementary file 3) shows that maltose, maltotriose and maltotetraose induce similar MalE conformations) or the differences in the binding affinity of MalE (Hall et al., 1997a). Thus, although the precise molecular mechanism of the rate-determining steps remains elusive, the positive correlation between lifetime of the SBP closed conformation and the activity of the transporter strongly suggests involvement of the translocator MalFGK2 in influencing the transport rate of certain maltodextrins.

## Discussion

Prokaryotes occupy diverse ecological niches within terrestrial ecosystems. Irrespective of the niche, their viability depends on selective acquisition of nutrients from the extracellular environment. However, the diversity of the external milieu poses a fundamental challenge for how acquisition of specific compounds can be achieved within the constraints of the chemical selectivity conferred by their import pathways. Numerous studies on SBPs associated with ABC importers have established that these proteins share a common architecture with a well-defined high-affinity ligand-binding site and have the ability to adopt a distinct ligand-free and -bound conformation, that is open and closed, respectively (Berntsson et al., 2010; Davidson et al., 2008; Shilton et al., 1996). Building on this knowledge, we investigated the relationship between SBP conformational dynamics, SBP-ligand interactions and substrate transport.

The general view of SBP conformational changes serving as a binary switch to communicate transport competency may hold for some SBPs, such as OppA (Figure 2—figure supplement 3B), while others employ multiple distinct ligand-bound conformations (Figure 2D–F; Figure 4D–G). To our knowledge, such extreme conformational plasticity of SBPs has not been observed before. MalE shows a remarkable structural flexibility of at least six different ligand-bound conformations (Figure 2D; Figure 4F). SBD1 (Figure 2E; Figure 4D) can sample at least four distinct ligand-bound conformations and SBD2 (Figure 2F; Figure 4E) and OpuAC (Figure 2B; Figure 4G) at least three. Moreover, MalE, SBD1 and SBD2 have multiple distinct ligand-bound conformations that can all interact with the translocator, as they all facilitate substrate import (’multiple conformations activate transport’ in Figure 7; Figure 2D–F). Thus, a productive SBP-translocator interaction in Type I ABC importers can be accomplished without relying on strict structural requirements for docking. This generalization may not apply to all Type I ABC importers since in the Opp importer the translocator might only interact with a unique closed conformation of the SBP OppA (Figure 2—figure supplement 3B), and Opp has no measurable affinity for its open ligand-free conformation (Doeven et al., 2008).

![Figure 7.](https://cdn.elifesciences.org/articles/44652/elife-44652-fig7-v2.jpg)

**Figure 7.:** Schematic summarizing the plasticity of ligand binding and solute import via ABC importers. Intrinsic closing of an SBP is a rare event or absent in some SBPs (‘little intrinsic closing’). Ligands are bound via induced fit (‘ligand-binding via induced fit’). SBPs can acquire one or more conformations that can activate transport (‘multiple conformations activate transport’). Variations in cognate substrate transport are caused by: (i) openings rate of the SBP and substrate transfer to the translocator (‘faster SBP opening – faster transport’) and (ii) substrate-dependent downstream steps (‘kinetics of downstream steps are substrate-dependent’). Although SBPs can acquire a conformation that activates transport (‘conformational match’), transport still fails when: (i) the SBP has no affinity for the translocator and/or cannot make the allosteric interaction with the translocator (‘conformational mismatch’); (ii) the SBP cannot open and release the substrate to the translocator (‘SBP cannot open’); or (iii) due to the specificity and size limitations of the translocator (‘rejected by translocator’).

Exclusion of non-cognate substrates is also a critical biological function for SBPs. Our work has uncovered a hitherto unappreciated complexity in protein-ligand interactions and how this is coupled to regulation of substrate import. Similar to transport, exclusion of non-cognate ligands might be achieved by multiple distinct mechanisms. We have shown that although multiple SBP conformations can activate transport (Figure 2D–F), not all SBP conformational states appear to provide the signal to facilitate transport. For example, the binding of certain non-cognate ligands induces a conformational change in SBD1 (Figure 4D), MalE (Figure 4F) and OpuAC (Figure 4G) that are distinct from those that facilitate transport. However, non-cognate substrate binding is not always coupled to an SBP conformational change, as observed for the binding of arginine or lysine to SBD1 and arginine to SBD2 (Figure 4D–E). These observations provide a general explanation on how substrate import can fail in Type I ABC importers, which would be due to the SBP-ligand complex assuming a conformation that cannot initiate allosteric interactions with the translocator (‘conformational mismatch’ in Figure 7). A similar hypothesis was put forward based on the observation that binding of β-cyclodextrin fails to fully close MalE (Hall et al., 1997b; Sharff et al., 1993; Skrynnikov et al., 2000). However, the sole observation of partial closing of MalE cannot explain why transport of β-cyclodextrin fails, as we here show that also cognate maltodextrins are able to induce partial closing of MalE (Figure 2D).

By contrast, in the Mn2+ transporter PsaBCA, a different mechanism is used. In PsaA, the binding site composition of the SBP precludes the ability of the protein to exclude the non-cognate substrate Zn2+ from interacting. As a consequence, both metals bind and trigger formation of similar PsaA conformations (‘conformational match’ in Figure 7; Figure 4H) (McDevitt et al., 2011; Lawrence et al., 1998). Despite this, the two ions have starkly different conformational dynamics, with Zn2+ forming a highly stable closed conformation, such that it cannot open and release the substrate to its translocator (‘SBP cannot open’ in Figure 7; Figure 5). By altering the binding site interactions between PsaA and Zn2+, opening is faster and transport of the metal ion can occur (Figure 5B–D). Similar observations were made for GlnPQ (Gouridis et al., 2015; Schuurman-Wolters et al., 2018) and MalE (Figure 6E, Figure 6—figure supplement 3A), in which a slower/faster opening of the SBP resulted in a decrease/increase in the corresponding transport of the substrate or ATP hydrolysis rate (‘faster SBP opening – faster transport’ in Figure 7). We therefore conclude that for ligands that induce highly stabilized SBP-substrate conformations, which require more energy (thermal or ATP-dependent) to open, transport becomes slower or is abrogated. Based on these findings, we infer that biological selectivity in ABC importers is largely achieved via a combination of ligand release kinetics and its influence on the conformational state of the SBP. This provides a mechanism to facilitate the import of selective substrates, while excluding other compounds. However, our data also implicate a role for the translocator in contributing to the specificity of ABC importers (‘rejected by translocator’ in Figure 7), consistent with previous studies (Oldham et al., 2013; Yu et al., 2015; Davidson et al., 1992; Speiser and Ames, 1991).

The presence of a substrate binding site in the translocator of the maltose system is well-established (Oldham et al., 2013), although its role, if any, in influencing the rate of transport of maltodextrins is yet unknown. The average time required for the different maltodextrin-MalE complexes to open, correlates positively with the transport and ATP hydrolysis rate (Figure 6H) (Hall et al., 1997a). This suggests that the substrate, after it has been transferred from MalE to the translocator, acts as a trigger for subsequent steps, for example, the transition from the outward- to the inward-facing transporter conformation or the stimulation of ATP hydrolysis and/or Pi and ADP release (‘kinetics of downstream steps are substrate-dependent’ in Figure 7). Irrespective of the precise molecular mechanism, the positive correlation between lifetime of the SBP closed state and activity of the transporter implies that some maltodextrins trigger certain steps more efficient than other maltodextrins, thereby overcoming the slower opening of MalE, and leading to a preferred uptake of certain maltodextrins over others. When transport is solely altered by changing the SBP conformational dynamics, for example in MalE(I329W/A96W) and PsaA(D280N), the kinetics of these steps are not affected, as the same ligands are involved, thus explaining the negative correlation between SBP lifetime and transport in these specific cases.

The volume of the binding cavities in the translocator could be a limiting factor for transport via ABC importers. Analysis of the large non-cognate ligands maltooctaose and maltodecaose shows that these are bound reversibly by MalE (Figure 6A) and induce conformations similar to that of the cognate ligand maltoheptaose (‘conformational match’ in Figure 7; Figure 4F). Therefore, failure of the maltose system to transport maltooctaose and maltodecaose most likely arises due to size limitations of the translocator rather than failure of MalE to close and release the bound ligand. This supposition is supported by an analysis of the binding cavities in the crystal structure of MalFGK2-MalE (Oldham et al., 2013). These data suggest that the transporter could only accommodate maltodextrins as large as maltoheptoase. In contrast, MalE could accommodate larger maltodextrins, including β-cyclodextrin (Figure 4F), probably due to its greater structural flexibility (Figure 2D; Figure 4F), thereby allowing the binding pocket to adapt and ligands to extend into the solvent phase.

The presence of two consecutive binding pockets, one in the SBP and one in the translocator, in at least some ABC importers could indicate that specificity of transport occurs through a proofreading mechanism in a manner analogous to aminoacyl-tRNA synthetases and DNA polymerase (Shevelev and Hübscher, 2002; Kotik-Kogan et al., 2005). In such a mechanism, a substrate can be rejected even if it has been bound by the SBP. Although we show that intrinsic closing is a rare event (‘little intrinsic closing’ in Figure 7; data in Figure 3), it might influence transport in a cellular context where the ratio between SBP and translocator can be high (Schmidt et al., 2016). Moreover, other fast (µs-ms) and short-range conformational changes might be present as shown by NMR analysis on MalE (Tang et al., 2007). We speculate that in Type I ABC importers the wasteful conversion of chemical energy is prevented by a proofreading mechanism, as any thermally driven closing event would not be able to initiate the translocation cycle, as the substrate is absent. In accordance, ATP hydrolysis and transport are tightly coupled in the Type I importer GlnPQ (Lycklama A Nijeholt et al., 2018) that, based on the crystal structure of the homologous Art(QM)2 (Yu et al., 2015), contains an internal binding pocket located within the TMDs. By contrast, futile hydrolysis of ATP in the Type II importer BtuCDF (Borths et al., 2005) appears to correlate with the lack of a defined binding pocket inside the TMDs.

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
      <td>Gene(Escherichia coli)</td>
      <td>MalE</td>
      <td>NA</td>
      <td>UniProt: P0AEX9</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-his</td>
      <td>Qiagen</td>
      <td>RRID:AB_2714179</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Streptococcus pneumoniae)</td>
      <td>D39</td>
      <td>National Collection of Type Cultures</td>
      <td>NCTC:7466</td>
      <td>Capsular serotype 2</td>
    </tr>
    <tr>
      <td>Strain, strain background (Streptococcus pneumoniae)</td>
      <td>D39 ∆psaA</td>
      <td>This paper</td>
      <td></td>
      <td>Replacement of psaA with the Janus cassette (∆psaA::Janus)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Streptococcus pneumoniae)</td>
      <td>D39 ∆czcD</td>
      <td>This paper</td>
      <td></td>
      <td>Replacement of czcD with the Janus cassette (∆czcD::Janus)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Streptococcus pneumoniae)</td>
      <td>D39 ΩpsaAD280N</td>
      <td>This paper</td>
      <td></td>
      <td>Replacement of ∆psaA::Janus with psaA D280N (∆psaA::psaAD280N)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Streptococcus pneumoniae)</td>
      <td>D39 ΩpsaAD280N∆czcD</td>
      <td>This paper</td>
      <td></td>
      <td>Replacement of ∆psaA::Janus with psaA D280N; replacement of czcD with the Janus cassette (∆psaA::psaAD280N∆czcD::Janus)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Lactococcus lactis)</td>
      <td>NZ9000</td>
      <td>NIZO food research</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Lactococcus lactis)</td>
      <td>GKW9000</td>
      <td>DOI: 10.1038/ nsmb2929</td>
      <td></td>
      <td>Lactococcus lactis NZ9000 with glnPQ gene deleted</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>K12</td>
      <td>Other</td>
      <td></td>
      <td>Provided by Tassos Economou, KU Leuven</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL 21 DE3</td>
      <td>Other</td>
      <td></td>
      <td>Provided by Tassos Economou, KU Leuven</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b</td>
      <td>Merck</td>
      <td>Cat#:69739–3</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pNZglnPQhis</td>
      <td>DOI: 10.1047/ jbc.M500522200</td>
      <td></td>
      <td>Expression plasmid for GlnPQ</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SBD1-T159C/G87C</td>
      <td>DOI: 10.1038/ nsmb2929</td>
      <td></td>
      <td>Expression plasmid for SBD1(T159C/G87C)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>SBD2-T369C/S451C</td>
      <td>DOI: 10.1038/ nsmb2929</td>
      <td></td>
      <td>Expression plasmid for SBD2(T369C/S451C)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCAMcLIC01-PsaA</td>
      <td>DOI: 10.1038/ nchembio.1382</td>
      <td></td>
      <td>Expression plasmid for PsaA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCAMcLIC01-PsaAD280N</td>
      <td>DOI: 10.1038/ nchembio.1382</td>
      <td></td>
      <td>Expression plasmid for PsaA(D280N)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pNZOpuCHis</td>
      <td>DOI: 10.1093/ emboj/cdg581</td>
      <td></td>
      <td>Expression plasmid for OpuAC</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pNZcLIC-OppA</td>
      <td>DOI: 10.1002/pro.97</td>
      <td></td>
      <td>Expression plasmid for OppA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PsaA-V76C/K237C</td>
      <td>This paper</td>
      <td></td>
      <td>Expression plasmid for PsaA(V76C/K237C) from the pCAMcLIC01-PsaA construct</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PsaA-E74C/K237C</td>
      <td>This paper</td>
      <td></td>
      <td>Expression plasmid for PsaA(E74C/K237C) from the pCAMcLIC01-PsaA construct</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PsaA-D280N/V76C/K237C</td>
      <td>This paper</td>
      <td></td>
      <td>Expression plasmid for PsaA(D280N/V76C/K237C) from the pCAMcLIC01-PsaAD280N construct</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MalE-T36C/S352C</td>
      <td>This paper</td>
      <td></td>
      <td>Progenitors: PCR, E. coli gDNA; pET20b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MalE-T36C/N205C</td>
      <td>This paper</td>
      <td></td>
      <td>Progenitors: PCR, E. coli gDNA; pET20b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MalE-K34C/ R354C</td>
      <td>This paper</td>
      <td></td>
      <td>Progenitors: PCR, E. coli gDNA; pET20b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MalE-T36C/S352C/ A96W/I329W</td>
      <td>This paper</td>
      <td></td>
      <td>Progenitors: PCR, E. coli gDNA; pET20b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>OpuAC-V360C/ N423C</td>
      <td>This paper</td>
      <td></td>
      <td>Expression plasmid for OpuAC(V360C/N423C) from the pNZOpuCHis construct</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>OppA-A209C/ S441C</td>
      <td>This paper</td>
      <td></td>
      <td>Expression plasmid for OppA(A209C/ S441C) from the pNZcLIC-OppA construct</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>Primers</td>
      <td>Merck</td>
      <td></td>
      <td>see Supplementary File 2</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>RPPGFSPFR</td>
      <td>Merck</td>
      <td>Cat#:B3259</td>
      <td>peptide sequence: RPPGFSPFR</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>RDMPIQAF</td>
      <td>CASLO ApS</td>
      <td></td>
      <td>peptide sequence: RDMPIQAF</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>SLSQSKVLPVPQ</td>
      <td>CASLO ApS</td>
      <td></td>
      <td>peptide sequence: SLSQSKVLPVPQ</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>SLSQSKVLP</td>
      <td>CASLO ApS</td>
      <td></td>
      <td>peptide sequence: SLSQSKVLP</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glycine Betaine</td>
      <td>Merck</td>
      <td>Cat#:B3501</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Carnitine</td>
      <td>Merck</td>
      <td>Cat#:94954</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltose</td>
      <td>Merck</td>
      <td>Cat#:63418</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltotriose</td>
      <td>Merck</td>
      <td>Cat#:851493</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltotetraose</td>
      <td>Carbosynth Limited</td>
      <td>Cat#:OM06979</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltopentaose</td>
      <td>Merck</td>
      <td>Cat#:M8128</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltohexaose</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#:sc-218665</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltoheptaose</td>
      <td>Carbosynth Limited</td>
      <td>Cat#:OM06868</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltodecaose</td>
      <td>Carbosynth Limited</td>
      <td>Cat#:OM146832</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltooctaose</td>
      <td>Carbosynth Limited</td>
      <td>Cat#:OM06941</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Beta Cyclodextrin</td>
      <td>Merck</td>
      <td>Cat#:C4767</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltotetroitol</td>
      <td>Carbosynth Limited</td>
      <td>Cat#:OM02796</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Maltotriitol</td>
      <td>Merck</td>
      <td>Cat#:M4295</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3H-Asparagine</td>
      <td>American Radiolabeled Chemicals</td>
      <td>Cat#:ART 0500–250 µCi</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>14C-Glutamine</td>
      <td>PerkinEllmer</td>
      <td>Cat#:NEC451050UC</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>14C-Histidine</td>
      <td>PerkinEllmer</td>
      <td>Cat#:NEC277E050UC</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>14C-Arginine</td>
      <td>Moravek</td>
      <td>Cat#:MC 137</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3H-Lysine</td>
      <td>PerkinEllmer</td>
      <td>Cat#:NET376250UC</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa555</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:A20346</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa647</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:A20347</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cy3B</td>
      <td>GE Healthcare</td>
      <td>Cat#:PA63131</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ATTO647N</td>
      <td>ATTO-TECH</td>
      <td>Cat#:AD 647 N-45</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Dual-Channel- Burst-Search</td>
      <td>DOI: 10.1021/ jp063483n</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LabView data acquisition</td>
      <td>DOI: 10.1371/journal. pone.0175766</td>
      <td></td>
      <td>Provided by Shimon Weiss, UCLA</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Hidden Markov Model</td>
      <td>DOI: 10.1109/ 5.18626</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Origin</td>
      <td>OriginLab</td>
      <td>RRID:SCR_002815</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>RRID:SCR_001622</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Gene expression and SBP purification

N-terminal extension of the soluble SBPs with a Hisx tag (His10PsaA, His10SBD1, His10SBD2, His10OppA and His6OpuAC) were expressed and purified as previously described (Gouridis et al., 2015; Wolters et al., 2010; Doeven et al., 2004; Couñago et al., 2014). Protein derivatives having the cysteine point mutations were constructed using QuickChange mutagenesis (Bok and Keller, 2012) or Megaprimer PCR mutagenesis (Vander Kooi, 2013) protocols. Primers are indicated in Supplementary file 2 and all sequences were by sequencing. OppA, OpuAC, PsaA and PsaA(D280N) derivatives were constructed using as templates vectors pNZcLIC-OppA (Berntsson et al., 2009), pNZOpuCHis (Biemans-Oldehinkel and Poolman, 2003), pCAMcLIC01-PsaA (Couñago et al., 2014) and pCAMcLIC01-PsaAD280N (Couñago et al., 2014), respectively. Construction of SBD1 and SBD2 cysteine derivatives was accomplished as described previously (Gouridis et al., 2015).

The malE gene (UniProt: P0AEX9) was isolated from the genome of Escherichia coli K12. The primers were designed to exclude the signal peptide (amino acids 1–26). Primers introduced NdeI and HindIII restriction sites, and the gene product was sub-cloned in the pET20b vector (Merck). MalE derivatives having the cysteine or other point mutations were constructed using QuickChange mutagenesis (Bok and Keller, 2012) and Megaprimer PCR mutagenesis (Vander Kooi, 2013) protocols. Primers are indicated in Supplementary file 2 and all sequences were verified by sequencing. His6MalE was over-expressed in E. coli BL21 DE3 cells (F–ompT gal dcm lon hsdSB(rB–mB) λ(DE3 [lacI lacUV5-T7p07 ind1 sam7 nin5]) [malB+]K-12(λS)). Cells harbouring plasmids expressing the MalE wild-type and derivatives were grown at 30°C until an optical density (OD600) of 0.5 was reached. Protein expression was then induced by addition of 0.25 mM isopropyl β-D-1-thiogalactopyranoside (IPTG). After 2 hr induction cells were harvested. DNase 500 ug/ml (Merck) was added and passed twice through a French pressure cell at 1,500 psi and 2 mM phenylmethylsulfonyl fluoride (PMSF) was added to inhibit proteases. The soluble supernatant was isolated by centrifugation at 50,000 × g for 30 min at 4°C. The soluble material was then purified and loaded on Ni2+-sepharose resin (GE Healthcare) in 50 mM Tris-HCl, pH 8.0, 1 M KCl, 10% glycerol, 10 mM imidazole and 1 mM dithiothreitol (DTT; Sigma-Aldrich). The immobilized proteins were washed (50 mM Tris-HCl, pH 8.0, 50 mM KCl, 10% glycerol, 10 mM imidazole and 1 mM DTT plus 50 mM Tris-HCl, pH 8.0, 1 M KCl, 10% glycerol, 30 mM imidazole and 1 mM DTT sequentially) and then eluted (50 mM Tris-HCl, pH 8.0, 50 mM KCl, 10% glycerol, 300 mM imidazole and 1 mM DTT). Protein fractions were pooled (supplemented with 5 mM EDTA and 10 mM DTT), concentrated (10.000 MWCO Amicon; Merck-Millipore), dialyzed against 100–1000 volumes of buffer (50 mM Tris-HCl, pH 8.0, 50 mM KCl, 50% glycerol and 10 mM DTT), aliquoted and stored at −20°C until required.

### Uptake experiments in whole cells

Lactococcus lactis GKW9000 carrying pNZglnPQhis (Schuurman-Wolters and Poolman, 2005) was cultivated semi-anaerobically at 30°C in M17 (Oxoid) medium supplemented with 1% (w/v) glucose and 5 μg/ml chloramphenicol. For uptake experiments cells were grown in GM17 to an OD600 of 0.4, induced for 1 hr with 0.01% of culture supernatant of the nisin A-producing strain NZ9700 and harvested by centrifugation for 10 min at 4000 x g; the final nisin A concentration is ~1 ng/ml. After washing twice with 10 mM PIPES-KOH, 80 mM KCl, pH 6.0, the cells were resuspended to OD600 = 50 in the same buffer. Uptake experiments were performed at 0.1–0.5 mg/ml total protein in 30 mM PIPES-KOH, 30 mM MES-KOH, 30 mM HEPES-KOH (pH 6.0). Before starting the transport assays, the cells were equilibrated and energized at 30°C for 3 min in the presence of 10 mM glucose plus 5 mM MgCl2. After 3 min, the uptake reaction was started by addition of either [14C]-glutamine, [14C]-histidine, [14C]-lysine (all from PerkinElmer), [14C]-arginine (Moravek) or [3H]-asparagine (ARC); the specific radioactivity was adjusted for each experiment (amino-acid concentration) to obtain sufficient signal above background; the final amino acid concentrations are indicated in the figure legends. At given time intervals, samples were taken and diluted into 2 ml ice-cold 100 mM LiCl. The samples were rapidly filtered through 0.45 µm pore-size cellulose nitrate filters (Amersham) and the filter was washed once with ice-cold 100 mM LiCl. The radioactivity on the filters was determined by liquid scintillation counting.

### Purification and membrane reconstitution of GlnPQ for in vitro transport assays

Membrane vesicles of Lactococcus lactis GKW9000 carrying pNZglnPQhis (Schuurman-Wolters and Poolman, 2005) were prepared as described before (Lycklama A Nijeholt et al., 2018). For reconstitution into proteoliposomes, 150 mg of total protein in membrane vesicles was solubilized in 50 mM potassium phosphate pH 8.0, 200 mM NaCl, 20% glycerol and 0.5% (w/v) DDM for 30 min at 4°C. The sample was centrifuged (12 min, 300,000xg) and the supernatant was collected. Subsequently, GlnPQ was allowed to bind to Ni-Sepharose (1.5 ml bed volume) for 1 hr at 4°C after addition of 10 mM imidazole. The resin was rinsed with 20 column volumes of wash buffer (50 mM potassium phosphate, pH 8.0, 200 mM NaCl, 20% (v/v) glycerol, 50 mM imidazole and 0.02% (w/v) DDM). The protein was eluted with five column volumes of elution buffer (50 mM potassium phosphate, pH 8.0, 200 mM NaCl, 10% (w/v) glycerol, 500 mM imidazole plus 0.02% (w/v) DDM). The purified GlnPQ was used for reconstitution into liposomes composed of egg yolk L-α-phosphatidylcholine and purified E. coli lipids (Avanti polar lipids) in a 1:3 ratio (w/w) as described before (Geertsma et al., 2008) with a final protein/lipid ratio of 1:100 (w/w). An ATP regenerating system, consisting of 50 mM potassium phosphate, pH 7.0, creatine kinase (2.4 mg/ml), Na2-ATP (10 mM), MgSO4 (10 mM), and Na2-creatine-phosphate (24 mM) was enclosed in the proteoliposomes by two freeze/thaw cycles, after which the vesicles were stored at −80°C. On the day of the uptake experiment, the proteoliposomes were extruded 13 times through a polycarbonate filter (200 nm pore size), diluted to 3 ml with 100 mM potassium phosphate, pH 7.0, centrifuged (265,000 g for 20 min), and then washed and resuspended in 100 mM potassium phosphate, pH 7.0, to a concentration of 50 mg of lipid/ml.

Uptake in proteoliposomes was measured in 100 mM potassium phosphate, pH 7.0, supplemented with 5 µM of [14C]-glutamine or [3H]-asparagine. This medium, supplemented with or without unlabeled amino acids (asparagine, arginine, glutamine, histidine or lysine), was incubated at 30°C for 2 min prior to adding proteoliposomes (kept on ice) to a final concentration of 1–5 mg of lipid/ml. At given time intervals, 40 µl samples were taken and diluted with 2 ml of ice-cold isotonic buffer (100 mM potassium phosphate, pH 7.0). The samples were collected on 0.45 m pore size cellulose nitrate filters and washed twice as described above. After addition of 2 ml Ultima Gold scintillation liquid (PerkinElmer), radioactivity was measured on a Tri-Carb 2800TR (PerkinElmer). A single time-dependent uptake experiment is shown in Figure 4A–C and consistent results were obtained upon repetition with an independent sample preparation.

### Zinc accumulation in whole cells

The S. pneumoniae D39 mutant strains ΩpsaAD280N and ∆czcD were constructed using the Janus cassette system (Sung et al., 2001). Briefly, the upstream and downstream flanking regions of psaA and czcD were amplified using primers (Supplementary file 2) with complementarity to either psaAD280N (ΩpsaAD280N), generated via site-directed mutagenesis of psaA following manufacturer instructions (Agilent), or the Janus cassette (∆czcD) and were joined by overlap extension PCR. These linear fragments were used to replace by homologous recombination psaA and czcD, respectively, in the chromosome of wild-type and ∆czcD strains. For metal accumulation analyses, S. pneumoniae strains were grown in a cation-defined semi-synthetic medium (CDM) with casein hydrolysate and 0.5% yeast extract, as described previously (Plumptre et al., 2014). Whole cell metal ion accumulation was determined by inductively coupled plasma-mass spectrometry (ICP-MS) essentially as previously described (Begg et al., 2015). Briefly, S. pneumoniae strains were inoculated into CDM supplemented with 50 μM ZnSO4 at a starting OD600 of 0.05 and grown to mid-log phase (OD600 = 0.3–0.4) at 37°C in the presence of 5% CO2. Cells were washed by centrifugation six times in PBS with 5 mM EDTA, harvested, and desiccated at 95°C for 18 hr. Metal ion content was released by treatment with 500 μL of 35% HNO3 at 95°C for 60 min. Metal content was analysed on an Agilent 8900 QQQ ICP-MS (Couñago et al., 2014).

### Isothermal titration calorimetry (ITC)

Purified OppA was dialyzed overnight against 50 mM Tris-HCl, pH 7.4, 50 mM KCl. ITC experiments were carried by microcalorimetry on a ITC200 calorimeter (MicroCal). The peptide (RPPGFSFR) stock solution (200 μM) was prepared in the dialysis buffer and was stepwise injected (2 μl) into the reaction cell containing 20 μM OppA. All experiments were carried out at 25°C with a mixing rate of 400 rpm. Data were analyzed with a one site-binding model using, provided by the Origin software (OriginLab).

### Protein labeling for FRET measurements

Surface-exposed and non-conserved positions were chosen for Cys engineering and subsequent labeling, based on X-ray crystal structures of OpuAC (3L6G, 3L6H), SBD1 (4AL9), SBD2 (4KR5, 4KQP), PsaA (3ZK7, 1PSZ), OppA (3FTO, 3RYA) and MalE (1OMP, 1ANF). Unlabeled protein derivatives (20–40 mg/ml) were stored at −20°C in the appropriate buffer (50 mM Tris-HCl, pH 7.4, 50 mM KCl, 50% glycerol for MalE and OppA. 25 mM Tris-HCl, pH 8.0, 150 mM NaCl, 1 μM EDTA, 50% glycerol for PsaA. 50 mM KPi, pH 7.4, 50 mM KCl, 50% glycerol for OpuAC, SBD1 and SBD2) supplemented with 1 mM DTT.

Stochastic labeling was performed with the maleimide derivative of dyes Cy3B (GE Healthcare) and ATTO647N (ATTO-TEC) for OpuAC. MalE, SBD1, SBD2, OppA and PsaA were labeled with Alexa555 and Alexa647 maleimide (ThermoFisher). The purified proteins were first treated with 10 mM DTT for 30 min to reduce oxidized cysteines. After dilution of the protein sample to a DTT concentration of 1 mM the reduced protein were immobilized on a Ni2+-Sepharose resin (GE Healthcare) and washed with 10 column volumes of buffer A (50 mM Tris-HCl, pH 7.4, 50 mM KCl for MalE and OppA. 25 mM Tris-HCl, pH 8.0, 150 mM NaCl, 1 μM EDTA for PsaA. 50 mM KPi, pH 7.4, 50 mM KCl for OpuAC, SBD1 and SBD2) to remove the DTT. To make sure that no endogenous ligand was left, for some experiments, and prior to removing the DTT, we unfolded the immobilized-SBPs by treatment with 6 M of urea supplemented with 1 mM DTT and refolded them again by washing with buffer A. The resin was incubated 1–8 hr at 4°C with the dyes dissolved in buffer A. To ensure a high labeling efficiency, the dye concentration was ~20 times higher than the protein concentration. Subsequently, unbound dyes were removed by washing the column with at least 20 column volumes of buffer A. Elution of the proteins was done by supplementing buffer A with 400 mM imidazole. The labeled proteins were further purified by size-exclusion chromatography (Superdex 200, GE Healthcare) using buffer A. Sample composition was assessed by recording the absorbance at 280 nm (protein), 559 nm (donor), and 645 nm (acceptor) to estimate labeling efficiency. For all proteins, the labeling efficiency was >90%.

### Fluorescence anisotropy

To verify that the measurements of apparent FRET efficiency report on inter-probe distances between the donor and acceptor fluorophores, at least one of the fluorophores must be able to rotate freely. To investigate this, we determined the anisotropy values of labeled proteins. The fluorescence intensity was measured on a scanning spectrofluorometer (Jasco FP-8300; 10 nm excitation and emission bandwidth; 8 s integration time) around the emission maxima of the fluorophores (for donor, λex = 535 nm and λem = 580 nm; for acceptor, λex = 635 nm and λem = 660 nm). Anisotropy values $r$ were obtained from on $r=(I_{VV}-GI_{VH})/(I_{VV}+2GI_{VH})$, where $I_{VV}$ and $I_{VH}$ are the fluorescence emission intensities in the vertical and horizontal orientation, respectively, upon excitation along the vertical orientation. The sensitivity of the spectrometer to different polarizations was corrected via the factor $G=I_{HV}/I_{HH}$, where $I_{HV}$ and $I_{HH}$ are the fluorescence emission intensities in the vertical and horizontal orientation, respectively, upon excitation along the horizontal orientation. $G$ -values were determined to be 1.8-1.9. The anisotropy was measured in buffer A and the labeled proteins and free-fluorophores in a concentration range of 50−500 nM at room temperature.

### Solution-based smFRET and ALEX

Solution-based smFRET and alternating laser excitation (ALEX) (Kapanidis et al., 2004) experiments were carried out at 25–100 pM of labeled protein at room temperature in buffer A supplemented with additional reagents as stated in the text. Microscope cover slides (no. 1.5H precision cover slides, VWR Marienfeld) were coated with 1 mg/mL BSA for 30–60 s to prevent fluorophore and/or protein interactions with the glass material. Excess BSA was subsequently removed by washing and exchange with buffer A.

All smFRET experiments were performed using a home-built confocal microscope. In brief, two laser-diodes (Coherent Obis) with emission wavelength of 532 and 637 nm were directly modulated for alternating periods of 50 µs and used for confocal excitation. The laser beams where coupled into a single-mode fiber (PM-S405-XP, Thorlabs) and collimated (MB06, Q-Optics/Linos) before entering a water immersion objective (60X, NA 1.2, UPlanSAPO 60XO, Olympus). The fluorescence was collected by excitation at a depth of 20 µm. Average laser powers were 30 μW at 532 nm (~30 kW/cm2) and 15 μW at 637 nm (~15 kW/cm2). Excitation and emission light was separated by a dichroic beam splitter (zt532/642rpc, AHF Analysentechnik), which is mounted in an inverse microscope body (IX71, Olympus). Emitted light was focused onto a 50 µm pinhole and spectrally separated (640DCXR, AHF Analysentechnik) onto two single-photon avalanche diodes (TAU-SPADs-100, Picoquant) with appropriate spectral filtering (donor channel: HC582/75; acceptor channel: Edge Basic 647LP; AHF Analysentechnik). Registration of photon arrival times and alternation of the lasers was controlled by an NI-Card (PXI-6602, National Instruments) using LabView data acquisition software of the Weiss laboratory (Ingargiola et al., 2017).

An individual labeled protein diffusing through the confocal volume generates a burst of photons. To identify fluorescence bursts a dual-channel burst search (Nir et al., 2006) was used with parameters M = 15, T = 500 μs and L = 25. In brief, a fluorescent signal is considered a burst, when a total of L photons having M neighboring photons within a time window of length T centred on their own arrival time. A first burst search was done that includes the donor and acceptor photons detected during the donor excitation, and a second burst search was done including only the acceptor photons detected during the acceptor excitation. The two separate burst searches were combined to define intervals when both donor and acceptor fluorophores are active. These intervals define the bursts. Only bursts having >150 photons were further analysed

The three relevant photon streams were analysed (DA, donor-based acceptor emission; DD, donor-based donor emission; AA, acceptor-based acceptor emission) and assignment is based on the excitation period and detection channel (Kapanidis et al., 2004). The apparent FRET efficiency is calculated via F(DA)/[F(DA)+F(DD)] and the Stoichiometry S by [F(DD)+F(DA)]/[(F(DD)+F(DA)+F(AA)], where F(·) denotes the summing over all photons within the burst (Kapanidis et al., 2004). The accurate FRET efficiency E was calculated by correcting the apparent FRET efficiency for background, direct excitation of the acceptor by donor excitation, leakage of donor fluorescence in the acceptor detection channel and relative differences in the efficiencies of the detectors and the quantum yield of the dyes (Nir et al., 2006). Corrections are made using established protocols as described in Lee et al (Nir et al., 2006). From the average E (see below), the mean inter-dye distance R was calculated via E = 1/(1+(R/R0)6), using R0 of 5.1 nm for Alexa555/Alexa647 and 6.2 nm for Cy3B/Atto647N.

Binning the detected bursts into a 2D (apparent) FRET/S histogram allowed the selection of the donor and acceptor labeled molecules and reduce artefacts arising from fluorophore bleaching (Kapanidis et al., 2004). The selected (apparent) FRET histogram were fitted with a Gaussian distribution using nonlinear least square, to obtain a 95% Wald confidence interval for the distribution mean. Statements about the significance of the mean of the FRET distributions are based on a comparison of the appropriate confidence intervals. In addition, a two-way Kolmogorov-Smirnov test was performed, as implemented in Matlab (MathWorks), on the selected burst corresponding to donor and acceptor-labeled proteins.

### Scanning confocal microscopy

Confocal scanning experiments were performed at room temperature and using a home-built confocal scanning microscope as described previously (Husada et al., 2018). In brief, surface scanning was performed using a XYZ-piezo stage with 100 × 100 × 20 µm range (P-517–3 CD with E-725.3CDA, Physik Instrumente). The detector signal was registered using a HydraHarp 400 picosecond event timer and a module for time-correlated single photon counting (both Picoquant). Data were recorded with constant 532 nm excitation at an intensity of 0.5 μW (~125 W/cm2) for SBD1, SBD2, PsaA, OppA and MalE, but 1.5 μW (~400 W/cm2) for OpuAC. Scanning images of 10 × 10 µm were recorded with 50 nm step size and 2 ms integration time at each pixel. After each surface scan, the positions of labeled proteins were identified manually; the position information was used to subsequently generate time traces. Surface immobilization was conducted using an anti-HIS antibody and established surface-chemistry protocols as described (Gouridis et al., 2015). A flow-cell arrangement was used as described before (Gouridis et al., 2015; Roy et al., 2008) for studies of surface-tethered proteins, except for MalE. MalE was studied on standard functionalized cover-slides since MalE was extremely sensitive to contaminations of maltodextrins in double-sided tape or other flow-cell parts. All experiments of OpuAC and PsaA were carried out in degassed buffer A under oxygen-free conditions obtained utilizing an oxygen-scavenging system supplemented with 10 mM of (±)−6-Hydroxy-2,5,7,8-tetramethylchromane-2-carboxylic acid (Trolox; Merck) (van der Velde et al., 2016). For MalE, SBD1, SBD2 and OppA experiments were carried out in buffer A supplemented with 1 mM Trolox and 10 mM Cysteamine (Merck).

### Analysis of fluorescence trajectories

Time-traces were analysed by integrating the detected red and green photon streams in time-bins as stated throughout the text. Only traces lasting longer than 50 time-bins, having on average more than 10 photons per time-bin that showed clear bleaching steps, were used for further analysis. The number of analysed molecules, transitions and the total observation time are indicated in Supplementary file 4. The apparent FRET per time-bin was calculated by dividing the red photons by the total number of photons per time-bin. The state-trajectory of the FRET time-trace was modelled by a Hidden Markov Model (HMM) (Rabiner and Lawrence, 1990). For this an implementation of HMM was programmed in Matlab (MathWorks), based on the work of Rabiner (Rabiner and Lawrence, 1990). In the analysis, we assumed that the FRET time-trace (the observation sequence) can be considered as a HMM with two states having a one-dimensional Gaussian-output distribution. The Gaussian output-distribution of state $i$ ($i$=1, 2) is parameterized by its mean and variance. The parameters $\lambda$ (transition probabilities that connect the states and parameters of output-distribution), given the observation sequence, was found by maximizing the likelihood function. This was iteratively done using the Baum-Welch algorithm (Baum and Petrie, 1966). Care was taken to avoid floating point underflow and was done as described (Rabiner and Lawrence, 1990). With the inferred parameters $\lambda$, the most probable state-trajectory is then found using the Viterbi algorithm (Viterbi, 1967). The time spent in each state (open, closed) was inferred from the most probable state-trajectory, an histogram was made and the mean time spent in each state was calculated.

### Ensemble FRET

Fluorescence spectra of labeled SBD1 and SBD2 proteins were measured on a scanning spectrofluorometer (Jasco FP-8300; λex = 552 nm, 5 nm excitation and emission bandwidth; 3 s integration time). The apparent FRET efficiency was calculated via Iacceptor/(Iacceptor +Idonor), where Iacceptor and Idonor are fluorescence intensities around the emission maxima of the acceptor (660 nm) and donor fluorophore (600 nm), respectively. Measurements were performed at 20°C with ~200 nM labeled protein dissolved in buffer A.
