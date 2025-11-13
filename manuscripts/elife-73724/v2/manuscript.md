# High-resolution structures of the actomyosin-V complex in three nucleotide states provide insights into the force generation mechanism

## Authors

- Sabrina Pospich<sup>1</sup> ([ORCID: 0000-0002-5119-3039](https://orcid.org/0000-0002-5119-3039))
- H Lee Sweeney<sup>2</sup> ([ORCID: 0000-0002-6290-8853](https://orcid.org/0000-0002-6290-8853))
- Anne Houdusse<sup>3</sup> ([ORCID: 0000-0002-8566-0336](https://orcid.org/0000-0002-8566-0336))
- Stefan Raunser<sup>1</sup> ([ORCID: 0000-0001-9373-3016](https://orcid.org/0000-0001-9373-3016)) †

### Affiliations

1. Department of Structural Biochemistry, Max Planck Institute of Molecular Physiology Dortmund Germany
2. Department of Pharmacology and Therapeutics and the Myology Institute, University of Florida Gainesville United States
3. Structural Motility, Institut Curie, Centre National de la Recherche Scientifique Paris France

† Corresponding author

## Abstract

The molecular motor myosin undergoes a series of major structural transitions during its force-producing motor cycle. The underlying mechanism and its coupling to ATP hydrolysis and actin binding are only partially understood, mostly due to sparse structural data on actin-bound states of myosin. Here, we report 26 high-resolution cryo-EM structures of the actomyosin-V complex in the strong-ADP, rigor, and a previously unseen post-rigor transition state that binds the ATP analog AppNHp. The structures reveal a high flexibility of myosin in each state and provide valuable insights into the structural transitions of myosin-V upon ADP release and binding of AppNHp, as well as the actomyosin interface. In addition, they show how myosin is able to specifically alter the structure of F-actin.

## Introduction

The molecular motor myosin is well known for its central role in muscle contraction (Hanson and Huxley, 1953; Szent-Györgyi, 2004). By using the actin cytoskeleton as tracks, myosin also powers cellular cargo transport processes and can serve as a molecular anchor and force sensor (Hartman et al., 2011; Woolner and Bement, 2009). Due to its versatility, myosin is key to numerous essential cellular processes including cytokinesis, transcription, signal transduction, cell migration and adhesion, and endo- and exocytosis (Coluccio, 2020; Krendel and Mooseker, 2005). While this variety in functions is well reflected by the diversity of the myosin superfamily (Sellers, 2000), the ATP-dependent force generation mechanism as well as the architecture of the motor domain is shared by all myosins (Cope et al., 1996).

The myosin motor domain consists of four subdomains: the actin-binding upper and lower 50 kDa (U50 and L50) domains, which are separated by the central actin-binding cleft, the N-terminal domain, and the converter domain, containing the long α-helical extension known as the lever arm (Rayment et al., 1993b). The active site of myosin is located at the interface of the U50 domain and the N-terminal domain and is allosterically coupled to both the actin-binding interface and the lever arm (Sweeney and Houdusse, 2010). This coupling ultimately enables the amplification of small rearrangements at the active site to large, force-producing conformational changes of the lever arm (Holmes, 1997; Rayment et al., 1993a).

The ATP-driven mechanism of myosin force generation relies on several major structural transitions and is described in the myosin motor cycle (Huxley, 1958; Lymn and Taylor, 1971). Initially, hydrolysis of ATP places myosin in a conformation known as the pre-powerstroke (PPS) state. The mechano-chemical energy stored in this conformation is released by binding to filamentous actin (F-actin), which serves as an activator and initiates a cascade of allosteric structural changes (Rosenfeld and Sweeney, 2004; Walker et al., 2000). These changes eventually result in phosphate release—potentially via a phosphate release (PiR) state (Llinas et al., 2015)—and the major, force-producing lever arm swing known as the powerstroke. Subsequent release of ADP from myosin in a state that binds both F-actin and ADP strongly (strong-ADP state) gives rise to a second, smaller lever arm swing, leaving myosin strongly bound to F-actin in the rigor state (Whittaker et al., 1995; Mentes et al., 2018). Binding of ATP to the now unoccupied active site causes a transition to the post-rigor state and eventual detachment from F-actin (Kühner and Fischer, 2011). Finally, ATP hydrolysis triggers the repriming of the lever arm through the so-called recovery stroke, thus completing the myosin motor cycle.

Decades of biochemical studies have brought great insights into the diversity and kinetics of the myosin superfamily (Coluccio, 2020; Geeves et al., 2005). However, detailed structural information is ultimately required to understand the mechanism of force generation. Over the years, X-ray crystallography has revealed the structures of various myosins in the post-rigor state (Rayment et al., 1993b), the PPS state (Smith and Rayment, 1996), the rigor-like state (Coureux et al., 2003), a putative PiR state (Llinas et al., 2015), as well as the intermediate recovery stroke state (Blanc et al., 2018; for a recent review of all available crystal structures, see Sweeney et al., 2020). Due to the reluctance of F-actin to crystallize, actin-bound states of myosin are not accessible by X-ray crystallography. Instead, cryo electron microscopy (cryo-EM) has proven to be an optimal tool to study filamentous proteins (Pospich and Raunser, 2018) such as the actomyosin complex (Behrmann et al., 2012; von der Ecken et al., 2016). To date, the structure of the actomyosin rigor complex has been determined for a variety of myosins (Banerjee et al., 2017; Behrmann et al., 2012; Doran et al., 2020; Fujii and Namba, 2017; Gong et al., 2021; Gurel et al., 2017; Mentes et al., 2018; Risi et al., 2021; Robert-Paganin et al., 2021; Vahokoski et al., 2020; von der Ecken et al., 2016). States other than the nucleotide-free rigor state have proven more difficult to study, mainly due to lower binding affinities and short lifetimes. In fact, the only other state solved to date is the strong-ADP state; and only two (myosin-IB, myosin-XV) (Gong et al., 2021; Mentes et al., 2018) of four independent studies (myosin-Va, myosin-VI) (Gurel et al., 2017; Wulf et al., 2016) have achieved high resolution (<4 Å). However, the actin-bound states of myosin, in particular weakly bound transition states for which no structure is yet available, are precisely those that are urgently needed to understand important properties of the myosin motor cycle, such as binding to and detachment from F-actin (recently reviewed in Schröder, 2020). In addition, high-resolution structures of other myosins in the rigor and especially strong-ADP state are required to identify conserved and specific features within the myosin superfamily. Finally, structures of all key states of the motor cycle need to be determined for a single myosin to allow the assembly of a reliable structural model since the structures of different myosins vary considerably within the same state (Merino et al., 2020).

Some myosins, including myosin-IB and the high-duty ratio myosins V and VI, have comparatively high binding affinities for F-actin and long lifetimes of actin-bound states (De La Cruz and Ostap, 2004; De La Cruz et al., 2001; De La Cruz et al., 1999; Laakso et al., 2008). Therefore, they are best suited to structurally study actin-bound states other than the rigor. Today, class V and VI myosins are probably the best-characterized unconventional myosins, both structurally and biochemically (Coluccio, 2020). Cryo-EM studies of actomyosin-V have further reported structures of the strong-ADP and rigor state (Wulf et al., 2016), as well as a potential PPS transition state (Volkmann et al., 2005). However, due to the limited resolution of these structures, atomic details could not be modeled and the structural transition of actin-bound myosin-V during its motor cycle has consequently remained elusive. Interestingly, myosin-V was also shown to be sensitive to the nucleotide state of phalloidin (PHD)-stabilized F-actin, preferring young ATP/ADP-Pi-bound F-actin over aged (post-Pi release) ADP-bound F-actin (Zimmermann et al., 2015). The structural basis and implications of this preference have not yet been uncovered.

Here, we present high-resolution cryo-EM structures of the actomyosin-V complex in three nucleotide states. Specifically, we have solved the structure of myosin-V in the strong-ADP state (ADP), the rigor state (nucleotide free), and a previously unseen post-rigor transition (PRT) state, which has the non-hydrolyzable ATP analog AppNHp bound to its active site. To investigate the structural effect the nucleotide state of F-actin has on myosin-V, we have also determined the structure of the rigor complex starting from young ADP-Pi-bound F-actin, rather than from aged ADP-bound F-actin. In addition to these structures and their implications, we report a pronounced conformational heterogeneity of myosin-V in all our data sets and characterize it in detail based on 18 high-resolution subset structures.

## Results and discussion

### High-resolution cryo-EM structures of the actomyosin-V complex

To provide insights into the structural transitions of myosin along its motor cycle, we determined the structure of the actomyosin-V complex in three different nucleotide states using single-particle cryo-EM. Specifically, we have decorated aged ADP-bound F-actin (rabbit skeletal α-actin) stabilized by PHD (Lynen and Wieland, 1938) with myosin-Va –S1 fragment bound to one essential light chain, hereafter referred to as myosin-V. The complex, referred to as aged actomyosin-V, was either prepared in the absence of a nucleotide or after brief incubation of myosin with Mg2+-ADP or Mg2+-AppNHp (see Materials and methods for details). AppNHp, also known as AMPPNP, is an ATP analog that has been shown to be non-hydrolyzable by myosin-V (Yengo et al., 2002). It is coordinated similarly to ATP in crystal structures of myosin-II (Bauer et al., 2000; Gulick et al., 1997) and has also been reported to lead to a mixture of a pre- and post-powerstroke conformations in myosin-V (Yengo et al., 2002; Volkmann et al., 2005). These results suggest that AppNHp can potentially mimic both ATP and ADP-Pi and is thus well suited to capture short-lived actin-bound transition states, such as the weakly bound PPS and post-rigor states (Sweeney and Houdusse, 2010).

We collected cryo-EM data sets of the different samples (Table 1) and processed them using the helical processing pipeline implemented in the SPHIRE package (Moriya et al., 2017; Pospich et al., 2021; Stabrin et al., 2020), which applies helical restraints but no symmetry. For each data set, two all-particle density maps were reconstructed (Figure 1—figure supplement 1, see Materials and methods for details). In this way, we achieved nominal resolutions of 3.0 Å/3.1 Å (ADP), 3.2 Å/3.3 Å (rigor), and 2.9 Å/2.9 Å (AppNHp), respectively (Figure 1—figure supplement 1 and Figure 1—figure supplement 2, Table 2, Table 3, Table 4), allowing us to reliably model each state and analyze its molecular interactions.

**Table 1.**
 Data collection statistics of F-actin and actomyosin data sets.Aged PHD-stabilized F-actin (F-actin-PHD) was decorated with myosin-V in the rigor (no nucleotide), strong-ADP (bound to Mg2+-ADP) and post-rigor transition (PRT) state (bound to Mg2+-AppNHp). Young JASP-stabilized F-actin (F-actin-JASP) was imaged in absence and presence of myosin-V in the rigor state. Refinement and model building statistics can be found in Table 2, Table 3, Table 4 and Table 6. See Figure 1—figure supplement 1 for an overview of the processing pipeline.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Aged F-actin-PHD</th>
      <th colspan="2">Young F-actin-JASP</th>
    </tr>
    <tr>
      <th rowspan="2">Microscopy</th>
      <th>ADP</th>
      <th>Rigor</th>
      <th>AppNHp 4°C</th>
      <th>AppNHp 25°C</th>
      <th>AppNHp*</th>
      <th>Actin only</th>
      <th>Rigor</th>
    </tr>
    <tr>
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
      <td>Microscope</td>
      <td colspan="2">Titan Krios – Cs 2.7 mm</td>
      <td colspan="5">Titan Krios – Cs-corrected</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td colspan="7">300</td>
    </tr>
    <tr>
      <td>Camera</td>
      <td colspan="7">K2 – super resolution</td>
    </tr>
    <tr>
      <td>Energy filter slit width (eV)</td>
      <td colspan="7">20</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td colspan="2">1.06</td>
      <td colspan="5">1.10</td>
    </tr>
    <tr>
      <td>Frames per movie</td>
      <td colspan="7">40</td>
    </tr>
    <tr>
      <td>Exposure time (s)</td>
      <td colspan="7">15</td>
    </tr>
    <tr>
      <td>Total electron dose (e/Å2)</td>
      <td>79</td>
      <td>82</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <td>Final electron dose (e/Å2)</td>
      <td colspan="5">Dose weighted</td>
      <td colspan="2">Polished particles</td>
    </tr>
    <tr>
      <td>Defocus range (µm)</td>
      <td>0.3–3.2</td>
      <td>0.5–3.0</td>
      <td>0.3–3.0</td>
      <td>0.3–3.0</td>
      <td>0.3–3.0</td>
      <td>0.3–2.9</td>
      <td>0.3–3.0</td>
    </tr>
    <tr>
      <td>Number of images†</td>
      <td>4571 (5908)</td>
      <td>2304 (3623)</td>
      <td>5858 (7121)</td>
      <td>6617 (7023)</td>
      <td>12,475</td>
      <td>936 (1064)</td>
      <td>2970 (3336)</td>
    </tr>
  </tbody>
</table>

_*Combined from two data sets (4°C and 25°C).†In parenthesis is the initial number of images._

**Table 2.**
 Statistics of aged actomyosin in the strong-ADP state.Refinement and model building statistics of aged F-actin-PHD in complex with myosin-V in the strong-ADP state.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="8">Strong-ADP state: aged F-actin-PHD + myosin-Va-LC + Mg2+-ADP</th>
    </tr>
    <tr>
      <th>Central 3er/2er</th>
      <th>Central 1er(subtracted)</th>
      <th>Class 2</th>
      <th>Class 3</th>
      <th>Class 4</th>
      <th>Class 5</th>
      <th>Class 6</th>
      <th>Class 7</th>
    </tr>
    <tr>
      <th colspan="5">3D refinement statistics</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of helical segments</td>
      <td>871,844</td>
      <td>871,844</td>
      <td>140,383</td>
      <td>107,848</td>
      <td>113,766</td>
      <td>107,961</td>
      <td>118,875</td>
      <td>104,552</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>3.0</td>
      <td>3.1</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.7</td>
      <td>3.6</td>
      <td>3.6</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>Map sharpeningfactor (Å2)</td>
      <td>–60</td>
      <td>–60</td>
      <td>–78</td>
      <td>–78</td>
      <td>–94</td>
      <td>–86</td>
      <td>–83</td>
      <td>–88</td>
    </tr>
    <tr>
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
      <td colspan="5">Atomic model statistics</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Non-hydrogen atoms</td>
      <td>23,334</td>
      <td>10,171</td>
      <td>10,149</td>
      <td>10,149</td>
      <td>10,086</td>
      <td>10,066</td>
      <td>10,113</td>
      <td>10,139</td>
    </tr>
    <tr>
      <td>Cross-correlation masked</td>
      <td>0.85</td>
      <td>0.83</td>
      <td>0.83</td>
      <td>0.83</td>
      <td>0.80</td>
      <td>0.82</td>
      <td>0.83</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td>MolProbity score</td>
      <td>1.35</td>
      <td>1.23</td>
      <td>1.28</td>
      <td>1.36</td>
      <td>1.38</td>
      <td>1.36</td>
      <td>1.35</td>
      <td>1.39</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>6.28</td>
      <td>4.55</td>
      <td>5.31</td>
      <td>6.45</td>
      <td>6.94</td>
      <td>6.50</td>
      <td>6.37</td>
      <td>7.15</td>
    </tr>
    <tr>
      <td>EMRinger score*</td>
      <td>3.42/2.83</td>
      <td>3.56/3.36</td>
      <td>3.44/3.49</td>
      <td>2.83/2.92</td>
      <td>2.67/2.23</td>
      <td>2.99/2.92</td>
      <td>2.92/2.52</td>
      <td>2.68/2.38</td>
    </tr>
    <tr>
      <td>Bond RMSD (Å)</td>
      <td>0.012</td>
      <td>0.005</td>
      <td>0.004</td>
      <td>0.005</td>
      <td>0.005</td>
      <td>0.004</td>
      <td>0.006</td>
      <td>0.008</td>
    </tr>
    <tr>
      <td>Angle RMSD (°)</td>
      <td>1.07</td>
      <td>0.83</td>
      <td>0.85</td>
      <td>0.89</td>
      <td>0.92</td>
      <td>0.88</td>
      <td>0.93</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.04</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>Ramachandranfavored (%)</td>
      <td>99.65</td>
      <td>99.68</td>
      <td>99.76</td>
      <td>99.68</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
    </tr>
    <tr>
      <td>Ramachandranoutliers (%)</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>CaBLAM outliers (%)</td>
      <td>0.7</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.3</td>
      <td>1.2</td>
      <td>1.0</td>
      <td>0.8</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>

_*Values correspond to score against the post-refined map used for real-space refinement/a map filtered to local resolution._

**Table 3.**
 Statistics of aged actomyosin in the rigor state.Refinement and model building statistics of aged F-actin-PHD in complex with myosin-V in the rigor state.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="5">Rigor state: aged F-actin-PHD + myosin-Va-LC</th>
    </tr>
    <tr>
      <th>Central 3er/2er</th>
      <th>Central 1er(subtracted)</th>
      <th>Class 1</th>
      <th>Class 2</th>
      <th>Class 4</th>
    </tr>
    <tr>
      <th>3D refinement statistics</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of helical segments</td>
      <td>299,784</td>
      <td>299,784</td>
      <td>94,077</td>
      <td>102,818</td>
      <td>81,757</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>3.2</td>
      <td>3.3</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.6</td>
    </tr>
    <tr>
      <td>Map sharpening factor (Å2)</td>
      <td>–81</td>
      <td>–80</td>
      <td>–89</td>
      <td>–89</td>
      <td>–87</td>
    </tr>
    <tr>
      <td>Atomic model statistics</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Non-hydrogen atoms</td>
      <td>23,288</td>
      <td>10,148</td>
      <td>10,139</td>
      <td>10,139</td>
      <td>10,139</td>
    </tr>
    <tr>
      <td>Cross-correlation masked</td>
      <td>0.83</td>
      <td>0.86</td>
      <td>0.83</td>
      <td>0.82</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>MolProbity score</td>
      <td>1.28</td>
      <td>1.18</td>
      <td>1.24</td>
      <td>1.25</td>
      <td>1.31</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>5.25</td>
      <td>3.97</td>
      <td>4.66</td>
      <td>4.81</td>
      <td>5.75</td>
    </tr>
    <tr>
      <td>EMRinger score*</td>
      <td>3.14/3.39</td>
      <td>3.41/3.10</td>
      <td>2.97/3.00</td>
      <td>3.53/3.00</td>
      <td>3.01/3.06</td>
    </tr>
    <tr>
      <td>Bond RMSD (Å)</td>
      <td>0.005</td>
      <td>0.014</td>
      <td>0.005</td>
      <td>0.005</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>Angle RMSD (°)</td>
      <td>0.84</td>
      <td>1.14</td>
      <td>0.80</td>
      <td>0.84</td>
      <td>0.82</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.04</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>99.86</td>
      <td>99.84</td>
      <td>99.60</td>
      <td>99.76</td>
      <td>99.76</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>CaBLAM outliers (%)</td>
      <td>0.8</td>
      <td>0.9</td>
      <td>0.9</td>
      <td>0.9</td>
      <td>0.8</td>
    </tr>
  </tbody>
</table>

_*Values correspond to score against the post-refined map used for real-space refinement/a map filtered to local resolution._

**Table 4.**
 Statistics of aged actomyosin in the post-rigor transition (PRT) state.Refinement and model building statistics of aged F-actin-PHD in complex with myosin-V in the PRT state (bound to AppNHp).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="8">Post-rigor transition state: aged F-actin-PHD + myosin-Va-LC + Mg2+-AppNHp</th>
    </tr>
    <tr>
      <th></th>
      <th>Central 3er/2er</th>
      <th>Central 1er(subtracted)</th>
      <th>Class 1</th>
      <th>Class 3</th>
      <th>Class 4</th>
      <th>Class 5</th>
      <th>Class 6</th>
      <th>Class 8</th>
    </tr>
    <tr>
      <th>3D refinement statistics</th>
      <th></th>
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
      <td>Number of helical segments</td>
      <td>2,446,218</td>
      <td>2,446,218</td>
      <td>330,197</td>
      <td>365,722</td>
      <td>350,069</td>
      <td>321,218</td>
      <td>277,487</td>
      <td>343,500</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>2.9</td>
      <td>2.9</td>
      <td>3.4</td>
      <td>3.3</td>
      <td>3.4</td>
      <td>3.3</td>
      <td>3.4</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td>Map sharpening factor (Å2)</td>
      <td>–80</td>
      <td>–100</td>
      <td>–113</td>
      <td>–106</td>
      <td>–114</td>
      <td>–106</td>
      <td>–111</td>
      <td>–104</td>
    </tr>
    <tr>
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
      <td>Atomic model statistics</td>
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
      <td>Non-hydrogen atoms</td>
      <td>23,370</td>
      <td>10,189</td>
      <td>10,125</td>
      <td>10,189</td>
      <td>10,154</td>
      <td>10,189</td>
      <td>10,085</td>
      <td>10,189</td>
    </tr>
    <tr>
      <td>Cross-correlation masked</td>
      <td>0.85</td>
      <td>0.84</td>
      <td>0.84</td>
      <td>0.86</td>
      <td>0.85</td>
      <td>0.85</td>
      <td>0.83</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>MolProbity score</td>
      <td>1.25</td>
      <td>1.15</td>
      <td>1.17</td>
      <td>1.24</td>
      <td>1.20</td>
      <td>1.26</td>
      <td>1.37</td>
      <td>1.18</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>4.76</td>
      <td>3.56</td>
      <td>3.78</td>
      <td>4.64</td>
      <td>4.12</td>
      <td>4.99</td>
      <td>6.74</td>
      <td>3.95</td>
    </tr>
    <tr>
      <td>EMRinger score*</td>
      <td>3.29/3.45</td>
      <td>3.82/3.40</td>
      <td>3.35/3.07</td>
      <td>3.58/3.45</td>
      <td>3.18/3.35</td>
      <td>2.94/2.97</td>
      <td>3.01/3.01</td>
      <td>3.09/2.88</td>
    </tr>
    <tr>
      <td>Bond RMSD (Å)</td>
      <td>0.004</td>
      <td>0.012</td>
      <td>0.009</td>
      <td>0.014</td>
      <td>0.009</td>
      <td>0.014</td>
      <td>0.009</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>Angle RMSD (°)</td>
      <td>0.78</td>
      <td>1.01</td>
      <td>0.96</td>
      <td>1.15</td>
      <td>0.97</td>
      <td>1.14</td>
      <td>1.08</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.08</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>99.86</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>CaBLAM outliers (%)</td>
      <td>1.1</td>
      <td>1.2</td>
      <td>1.1</td>
      <td>1.1</td>
      <td>1.2</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>

_*Values correspond to score against the post-refined map used for real-space refinement/a map filtered to local resolution._

### Varying conformations in the strong-ADP state of different myosins

The structure of F-actin decorated with myosin-V in complex with Mg2+-ADP represents the strong-ADP state, which has high affinity for both F-actin and ADP and directly precedes the nucleotide-free rigor state within the myosin motor cycle. The overall structure encompasses all hallmarks of the strong-ADP state including a closed actin-binding cleft, which allows strong binding to F-actin, and a post-powerstroke lever arm orientation (Figure 1, Figure 1—video 1), in line with an earlier medium-resolution structure of the same complex (Wulf et al., 2016).

![Figure 1.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-v2.jpg)

**Figure 1.:** (A) Atomic model and LAFTER density map of the central myosin-V-LC subunit (orange, LC: white) bound to aged F-actin-PHD (shades of sea green, three subunits shown, A-1 to A+1). Nucleotides and PHD are highlighted in orange, pink, and yellow, respectively. The HF helix is marked by a black arrowhead. (B) Close-up view of the myosin active site consisting of the P-loop (yellow, 164–168), switch I (blue, aa 208–220), switch II (green, aa 439–448), and the A-loop (purple, aa 111–116). Only side chains involved in the binding of ADP are displayed, also see Figure 1—figure supplement 3. (C) 2D protein-ligand interaction diagram illustrating the coordination of Mg2+-ADP by hydrogen bonds (dashed green lines) and hydrophobic interactions (red rays). (D) Illustration of the model-map agreement within a central section of myosin. Most side chains are resolved by the post-refined density map (transparent gray). See Figure 1—video 1 for a three-dimensional visualization and Figure 1—figure supplements 1–2 for an overview of the processing pipeline and the cryo-EM data, respectively. A comparison of the strong-ADP state of different myosins can be found in Figure 1—figure supplements 4 and 5. Figure 1—figure supplement 6 illustrates the domain architecture of myosin.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Auto-picked particle stacks were initially pre-cleaned by 2D classification (final number of particles stated). Cleaned stacks were 3D refined against an initial reference generated from an atomic model of actomyosin (PDB: 5JLH; von der Ecken et al., 2016) without applying a 3D mask. The resulting 3D density map was used as reference volume in a subsequent masked 3D refinement yielding a first high-resolution structure of the full actomyosin filament. Based on this, particle stacks were optimized by CTF refinement and in case of the young F-actin-JASP data sets by additional particle polishing, followed by a local 3D refinement. By applying a mask including only the central three actin and two myosin molecules (central 3er/2er), the refinement was subsequently focused on the central section of the filament (central 3er/2er maps, resolutions stated). To account for the structural heterogeneity observed in the actomyosin data sets, a heterogeneity analysis was performed. Here, particles were initially signal subtracted to remove everything but the central actomyosin subunit (central 1er). These particles were then locally 3D refined to produce average structures (central 1er maps, resolutions stated). In addition, signal-subtracted particles were 3D classified without alignment to separate distinct conformations. The number of classes was optimized experimentally to yield a maximum number of high-resolution 3D classes. Finally, subsets were locally 3D refined, resulting in 18 high-resolution structures (central 1er classes, final number of particles and resolutions stated). Classes of insufficient quality (struck through) were not modeled and omitted in all subsequent analysis steps.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Representative micrographs at –1.3 μm defocus and (B) their power spectra. (C) Fourier shell correlation (FSC) curves for masked (darker shade, with resolution values) and unmasked half maps (lighter shade) including either three actin subunits and two myosin molecules (central 3er/2er, shades of blue, also see Figure 1—figure supplement 1) or one actomyosin subunit (signal subtracted, central 1er, shades of green). (D) Color-coded local resolution of full filaments and (E) signal-subtracted actomyosin subunits for all three states. Note that the two AppNHp data sets (4°C and 25°C) were combined to increase the overall resolution. Scale bar 500 Å.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Close-up views of the active site of F-actin (left column) and myosin-V (middle and right column) of all five structures. Ribbons are color-coded according to the respective structural state; aged F-actin-PHD: sea green; young F-actin-JASP: blue; and myosin-V in the rigor: red; ADP: orange; and AppNHp state: purple. Key loops of the myosin active site are highlighted by pastel colors; P-loop: yellow; switch I: blue; switch II: green; and A-loop: purple. Nucleotide densities are shown in orange and clearly support the presence of Pi in young JASP-stabilized F-actin. While there is density for a Mg2+ ion in all occupied active sites, there is an additional density, likely corresponding to a second Mg2+ ion, in AppNHp-bound myosin.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Comparison of the active sites of myosin-V in the strong-ADP state (orange) with the ones of (A) myosin-IB (PDB: 6C1D; Mentes et al., 2018), (B) myosin-VI (PDB: 6BNQ, nucleotide not modeled; Gurel et al., 2017), and (C) myosin-XV (PDB: 7R91, Gong et al., 2021) in the same state (shades of blue, shown as transparent). The coordination of Mg2+-ADP is almost identical in all four atomic models. Only the relative positions of switch I differ considerably, resulting in shifting of the coordinated Mg2+ ion. Atomic models were aligned on the HF helix (aa 169–181). Residue labels are given for myosin-V only.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Comparison of atomic models of the rigor and strong-ADP states of different actomyosin complexes solved by cryo-EM. (A) Superposition of the rigor states of myosin-V (red), myosin-II (PDB: 5H53; Fujii and Namba, 2017), myosin-NMIIC (PDB: 5JLH; von der Ecken et al., 2016), myosin-NMIIC (PDB: 5JLH; von der Ecken et al., 2016), myosin-IB (PDB: 6C1H; Mentes et al., 2018), and myosin-XV (PDB: 7R91; Gong et al., 2021) (shades of gray), illustrating strongly varying conformations and lever arm orientations. (B) Superposition of the strong-ADP states of myosin-V (orange), myosin-IB (PDB: 6C1D; Mentes et al., 2018), and myosin-XV (PDB: 7RB8; Gong et al., 2021) (shades of gray). The corresponding rigor states are shown as transparent. The difference in the orientation of the lever arm, which is caused by variations in the overall conformation, is even more pronounced in the strong-ADP state, increasing from a relative rotation of 54° to 71° for myosin-V and myosin-IB. These variations highlight the need to solve all key states of the motor cycle for a single myosin to reliably describe its structural transitions and ultimately the force generation mechanism. Structures are shown without the light chain after alignment on the actin subunit.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** Schematic illustrating the architecture of the myosin motor domain consisting of the actin-binding upper (U50, dark green) and lower 50 kDa domains (L50, tan), as well as the N-terminal domain (light green) and the converter domain (brown), which includes the light chain-binding lever arm. The U50 and L50 kDa domains are separated by a large cleft known as actin-binding cleft (highlighted by an asterisk). The active site resides at the interface of the U50 and N-terminal domain (black box, nucleotide shown in orange). The nucleotide localizes close to the HF helix (aa 169–183) and is coordinated by four loops including the P-loop: pastel yellow (aa 164–168); switch I: pastel blue (aa 208–220); switch II: pastel green (aa 439–448); and the A-loop: pastel purple (aa 111–116). Key structural elements such as the central transducer β-sheet and the relay helix (aa 449–479) are labeled.

The density corresponding to Mg2+-ADP is pronounced, indicating high to complete saturation of the active site (Figure 1, Figure 1—figure supplement 3). The β-phosphate of ADP is tightly coordinated by the P-loop (aa 164–168) via a conserved Walker-A nucleotide binding motif (Walker et al., 1982), which is also found in other ATPases as well as G-proteins (Kull and Endow, 2013; Vale, 1996).

The HF helix (aa 169–183) and switch I (aa 208–220) mediate additional contacts by either directly binding to the β-phosphate or coordinating the Mg2+ ion (Figure 1B and C). The third key loop of the active site, switch II (aa 439–448), does not directly contribute to the binding of Mg2+-ADP, which is in agreement with its proposed role in ATP hydrolysis and the subsequent release of the inorganic phosphate (Sweeney et al., 2020). Yet, switch II contributes to the stability of the active site by forming a hydrogen bond with the HF helix (D437-T170, predicted by PDBsum; Laskowski et al., 2018). In addition to the coordination of the β-phosphate, ADP binding is mediated by primarily hydrophobic interactions of the adenosine moiety with the purine-binding loop (Bloemink et al., 2020) (aa 111–116)—for brevity, hereafter referred to as A-loop (adenosine-binding loop) (Figure 1B and C, Figure 1—video 1, Figure 1—figure supplement 3). A tyrosine (Y119) trailing the A-loop forms another putative hydrogen bond with the adenosine, completing the coordination of ADP.

The coordination of Mg2+-ADP in our structure closely resembles the ones reported for the strong-ADP state of myosin-IB (Mentes et al., 2018), myosin-VI (Gurel et al., 2017), and myosin-XV (Gong et al., 2021; Figure 1—figure supplement 4). Only the position of switch I differs appreciably between myosins, ultimately resulting in varying positions of the coordinated Mg2+ ion. These differences highlight that while the general architecture of the active site is common to all myosins, small local reorganizations occur and possibly account for the different kinetics within the myosin superfamily. In contrast to the similarities of the active site, the overall structures of the strong-ADP states of myosin-V, -IB, and -XV differ considerably, resulting in lever arm orientations deviating by 71° and 22°, respectively (Figure 1—figure supplement 5).

### Structural transition of myosin-V upon ADP release

The structure of the actomyosin-V complex in the absence of any nucleotide in myosin represents the rigor state (Figure 2, Figure 2—video 1). In addition to an unoccupied and open active site (Figure 2—video 1, Figure 1—figure supplement 3), the actin-binding cleft is closed, facilitating strong binding to F-actin, and the lever arm adopts a post-powerstroke orientation (Figure 2, Figure 2—video 1). These features are common to all rigor structures solved to date (Banerjee et al., 2017; Behrmann et al., 2012; Doran et al., 2020; Fujii and Namba, 2017; Gong et al., 2021; Gurel et al., 2017; Mentes et al., 2018; Risi et al., 2021; Robert-Paganin et al., 2021; Vahokoski et al., 2020; von der Ecken et al., 2016). Yet, the structures of different myosins vary, particularly in the orientation of the lever arm (Figure 1—figure supplement 5A).

![Figure 2.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig2-v2.jpg)

**Figure 2.:** (A) Atomic model and LAFTER density map of the central myosin-V-LC subunit (red, LC: white) bound to aged F-actin-PHD (shades of sea green, three subunits shown, A-1 to A+1). Nucleotides and PHD are highlighted in orange and yellow, respectively. (B) Illustration of the model-map agreement within a central section of myosin. Most side chains are resolved by the post-refined density map (transparent gray). See Figure 2—video 1 for a three-dimensional visualization. (C–F) Comparison of the rigor state of myosin-V with crystal structures of the same myosin in the rigor-like state (PDB: 1OE9; Coureux et al., 2003; and PDB: 1W7I, also called weak-ADP state; Coureux et al., 2004; shades of gray). (C) Superposition of atomic models illustrating that deviations are limited to the actin interface, particularly (D) the CM loop, loop 4, and loop 2 and (E) the lever arm. Interestingly, the lever arm orientation seen in the rigor-like states does not superimpose with any conformation seen for the rigor complex (average: red; and 3D classes: transparent red), but localizes outside of its conformational space. (F) The active site is open in both the rigor and rigor-like states, and the SO4 and ADP bound to the rigor-like crystal structures only give rise to small, isolated changes of the P-loop (highlighted by a black arrowhead). Differences in the rigor-like structure can be readily attributed to the absence of F-actin and crystal packing, respectively.

While the actomyosin interface of the rigor state of myosin-V is basically indistinguishable from the one in the strong-ADP state, the lever arm orientations of the two states differ by ~9° (Figure 3A, Figure 3—video 1A), in agreement with a previously reported rotation of 9.5° (Wulf et al., 2016). The overall architecture of our rigor state structure not only is in good agreement with the medium-resolution cryo-EM structure published earlier (Wulf et al., 2016), but also strongly resembles the rigor-like crystal structures solved for this myosin isoform (Figure 2C–F; Coureux et al., 2003; Coureux et al., 2004).

![Figure 3.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig3-v2.jpg)

**Figure 3.:** (A) Superposition of the strong-ADP (orange) and rigor (red) atomic models. Changes at the active site (black box) are not transmitted to the actomyosin interface, but to the N-terminal and converter domain, resulting in a lever swing of 9°. (B) Close-up view of the active site showing the structural rearrangements upon Mg2+-ADP release (indicated by black arrows). The rigor structure is shown as transparent; see Figure 1 for color code. (C) Illustration of domain movements associated with Mg2+-ADP release predicted by DynDom (Hayward and Lee, 2002). Identified domains correlate well with myosins structural domains (see Figure 1—figure supplement 6) with domain 1 (yellow, 452 residues), domain 2 (181 residues, blue), and domain 3 (93 residues, red) representing the L50 and U50 domains, the N-terminal domain, and the converter domain, respectively. Bending residues primarily localize to the P-loop, the A-loop, and the central transducer β-sheet (1–2, green), as well as to a small part of the N-terminal and converter domain (2–3, purple). (D) Scheme illustrating the structural changes associated with Mg2+-ADP release. (E) Same views as in (D), but colored by DynDom domains, also see (C). The HF helix and the lever arm are highlighted by a black and a yellow arrowhead, respectively. Models were aligned on F-actin. See Figure 3—video 1 for a three-dimensional visualization.

As the strong-ADP and rigor state represent sequential states within the myosin motor cycle, a comparison of the respective high-resolution structures allows the detailed description of the structural transition of myosin-V upon Mg2+-ADP release (Figure 3, Figure 3—video 1). In addition to the ~9° lever arm rotation described above (Figure 3A), the two sequential states differ primarily in their conformation of the central transducer β-sheet and the N-terminal domain, which twist and rotate, respectively (Figure 3C–E, Figure 3—video 1; see Figure 1—figure supplement 6 for an overview of the myosin domain architecture). Notably, the structural changes are not transmitted to the U50 and L50 domains and thus do not alter the actin-binding interface (Figure 3A and C, Figure 3—video 1A and B).

The transducer rearrangements are directly linked to a reorganization of the active site that accounts for the reduced Mg2+-ADP affinity of the rigor state. By promoting a piston movement of the HF helix, twisting of the transducer increases the distance between the P-loop and switch I, thereby opening the active site (Figure 3B and D, Figure 3—video 1A–C). The resulting conformation is incompatible with the Mg2+-coordinating hydrogen bond between the HF helix and switch II (T170-D437). Loss of Mg2+ is thought to lead to the weak-ADP state of myosin (Coureux et al., 2004), which is so named due to its low nucleotide affinity that promotes the release of ADP. The subsequent rigor state is stabilized by a new network of hydrogen bonds formed between lysine K169 (HF helix, previously coordinated to the β-phosphate of ADP), and aspartate D437 and isoleucine I438 (switch II).

Upon Mg2+-ADP release, the A-loop also undergoes a small lateral shift (Figure 3B, D and E, Figure 3—video 1C and D). In this way, it likely stabilizes the twisting of the transducer and the N-terminal domain rotation. Surprisingly, the role of the A-loop in both the coordination of ADP and the coupling of the active site to the periphery has not been fully appreciated previously, although it is also involved in nucleotide binding in other myosins (Bloemink et al., 2020). Given their central importance for the coordination of Mg2+-ADP (Figure 1), we propose that the P-loop, the A-loop, and switch I contribute to the sensing of the nucleotide state and its transmission from the nucleotide-binding pocket to the periphery. Their mutual interplay defines the orientation of the N-terminal domain relative to the U50 and L50 subdomains. In this way, small changes in the active site (~1–2 Å) are amplified into significant rotations of the N-terminal and converter domain, eventually leading to a lever arm swing of ~9° upon Mg2+-ADP release (Figure 3, Figure 3—video 1).

Our high-resolution structures of the strong-ADP and rigor state are consistent with the sequential release of Mg2+ and ADP due to the isomerization of myosin to a conformation with reduced nucleotide affinity. In line with this, ADP binding to the rigor state can favor the reversal of this isomerization in the presence of Mg2+.

A similar structural transition upon Mg2+-ADP release has been reported for myosin-IB, -V, and -VI based on medium- and high-resolution cryo-EM structures (Gurel et al., 2017; Mentes et al., 2018; Wulf et al., 2016), suggesting a common coupling mechanism. Although most of the details are intriguingly similar, for example, the remodeling of hydrogen bonds due to the piston movement of the HF helix (Mentes et al., 2018), we find notable differences in the extent of the lever arm swing associated with Mg2+-ADP release (Figure 1—figure supplement 5), as well as the conformation of the relay helix, which partially unwinds in myosin-IB and -VI to allow for the larger lever arm swings (Gurel et al., 2017; Mentes et al., 2018). Interestingly, myosin-IB not only performs a larger lever arm swing (25°) (Mentes et al., 2018), but is also almost 40 times more sensitive to force than myosin-V (9° swing) (Laakso et al., 2008; Veigel et al., 2005). Since load will more easily prevent the isomerization of myosin if Mg2+-ADP release requires a large converter swing, we propose that the force sensitivity, which tunes the kinetics of the transition to the rigor state (Kovács et al., 2007; Laakso et al., 2008; Takagi et al., 2006; Veigel et al., 2005), increases with the extent of the lever arm swing upon Mg2+-ADP release.

### AppNHp gives rise to a strongly bound PRT state

We determined the structure of F-actin-myosin-V in complex with the non-hydrolyzable ATP analog AppNHp with the aim to characterize a potentially short-lived, weakly bound state of myosin. The resulting cryo-EM density map shows strong density for AppNHp, indicating high to complete saturation (Figure 4, Figure 4—video 1, Figure 1—figure supplement 3). Interestingly, the density also suggests the presence of two ions, both likely corresponding to Mg2+, given the size of the density and the buffer composition. While one ion occupies approximately the position that Mg2+ takes in the active site of the strong-ADP state, namely close to the γ-phosphate of AppNHp, the other one resides in between the α- and β-phosphates of AppNHp (Figures 1 and 4).

![Figure 4.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig4-v2.jpg)

**Figure 4.:** (A) Atomic model and LAFTER density map of the central myosin-V-LC subunit (purple, LC: white) bound to aged F-actin-PHD (shades of sea green, three subunits shown, A-1 to A+1). Nucleotides and PHD are highlighted in orange and yellow, respectively. (B) Close-up view of the myosin active site; see Figure 1 for color code. Only side chains involved in the binding of AppNHp are displayed. The density suggests the presence of two Mg2+ ions coordinating the γ, and α- and β-phosphate, respectively; also see Figure 1—figure supplement 3 and Figure 4—video 1. (C) 2D protein-ligand interaction diagram illustrating the coordination of Mg2+-AppNHp by hydrogen bonds (dashed green lines) and hydrophobic interactions (red rays). (D) Illustration of the model-map agreement within a central section of myosin. Most side chains are resolved by the post-refined density map (transparent gray). See Figure 4—figure supplements 1–3 for comparisons of the AppNHp-myosin-V structure with other structures as well as an analysis of unbound myosin in the AppNHp data set.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Superposition and (B) color-coded backbone root mean square deviation (RMSD) of the rigor (red) and the AppNHp (purple) atomic models, illustrating their close resemblance. Higher RMSD values localize exclusively to regions of lower local resolution and thus are likely due to modeling inaccuracies. A black box highlights the position of the active site. (C, D) Comparison of the active site of myosin bound to AppNHp (purple) with the one of myosin in the rigor (transparent red) (C) and strong-ADP state (transparent orange) (D). While only small, local changes are associated with the binding of AppNHp (C), the active sites of AppNHp- and ADP-bound myosin-V differ markedly (rearrangements are indicated by black arrows). Models were aligned on F-actin; for color code, see Figure 1.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A, B) Comparison of the active site of myosin-V bound to AppNHp with the one of (A) rigor-like myosin-V with ADP weakly bound (PDB: 17WI, also known as weak-ADP state, transparent gray; Coureux et al., 2004) and (B) ADP-bound myosin-IB in a strong-ADP to rigor transition state (PDB: 6C1G, transparent blue; Mentes et al., 2018). Models were aligned on the HF helix (aa 169–190, trailing the P-loop). The overall conformation of the active site as well as the coordination of the nucleotide is remarkably similar in all three structures, suggesting it to be characteristic for actin-bound transition states with weakly bound nucleotide.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Representative contrast-enhanced micrograph of the aged actomyosin-V complex bound to AppNHp (sample plunged at 4°C) illustrating many unbound particles in the background, which likely correspond to myosin-V molecules. Particle boxes (white) are shown for a few particles to highlight their size. Scale bar 500 Å. (B) Representative 2D class averages confirming that the particles in the background are indeed unbound myosin-V molecules. Scale bar 100 Å.

Similar to ADP, AppNHp is coordinated by a network of hydrogen bonds and additional hydrophobic interactions with the P-loop, switch I, and the A-loop (Figure 1C and Figure 4C). The details of the interactions, however, differ due to the different sizes of the two nucleotides and their relative positions in the active site, that is, the γ-phosphate of AppNHp almost takes the position of the β-phosphate of ADP relative to the HF helix (Figure 4, Figure 1—figure supplement 3, Figure 1).

Surprisingly, and in contrast to a previous low-resolution cryo-EM reconstruction (Volkmann et al., 2005), the overall structure of AppNHp-bound myosin-V is reminiscent of the rigor state (Figure 4—figure supplement 1). In particular, myosin is strongly bound to F-actin and adopts a post-powerstroke lever arm orientation (Figure 4, Figure 4—video 1, Figure 4—figure supplement 1A and B). The active site of AppNHp-bound myosin also closely resembles that of the rigor state, and thereby significantly deviates from the conformation found in the strong-ADP state (Figure 4—figure supplement 1C and D).

The compatibility of an ATP analog, specifically the presence of a γ-phosphate at the active site, with strong F-actin binding is initially puzzling and seemingly at odds with the reported reciprocal nature of these two processes (Coureux et al., 2004; Kühner and Fischer, 2011). A comparison of our AppNHp-bound structure with a rigor-like crystal structure of myosin-V with ADP weakly bound to its active site (Coureux et al., 2004) resolves this conflict (Figure 4—figure supplement 2A). The relative position of AppNHp and ADP in these two structures as well as their coordination, which in particular lacks contacts between K169 of the P-loop and the β-phosphate, is almost identical, suggesting that AppNHp is only weakly bound in our structure and therefore compatible with strong F-actin binding. Interestingly, a similar coordination was observed for Mg2+-ADP in a putative strong-ADP to rigor transition state cryo-EM structure of myosin-IB (Mentes et al., 2018; Figure 4—figure supplement 2B). These comparisons indicate that AppNHp and ADP can both weakly bind to myosin in a conformation reminiscent of the rigor.

Our prior kinetic studies (De La Cruz et al., 1999; Yengo et al., 2002) demonstrated that AppNHp reduces the binding affinity of myosin-V for F-actin by >5000-fold as compared to the rigor state, thus favoring dissociation. A weakened affinity is also supported by the higher concentrations required to achieve decoration of F-actin with myosin in the AppNHp state (see Materials and methods). AppNHp also induces greater structural flexibility in myosin-V (see below) as compared to the rigor state, which may facilitate the transition to a detached state. Based on the presented structural and prior kinetic studies, we propose that our AppNHp-bound myosin-V structure represents a post-rigor transtion (PRT) state that allows to visualize how ATP binds in the rigor state, prior to the transition that involves a switch I movement and promotes detachment of myosin from F-actin. The characteristic weak coordination of AppNHp in the PRT state allows myosin to remain strongly bound to F-actin until a strong coordination of the nucleotide is established. The report of a transition state with weakly bound ADP (Mentes et al., 2018; Figure 4—figure supplement 2B) suggests that weak nucleotide binding is a common scheme and that the PRT state is therefore not limited to AppNHp. The visualization of an ATP analog bound to a state reminiscent of the rigor shows that ATP mainly binds via its adenine ring, as does ADP (Figure 1). It also explains how the γ-phosphate can fit into the relatively small pocket created by the rigor conformation of the P-loop (Figure 4), and how its presence leads to local changes of the active site facilitating a tight coordination (Figure 4—figure supplement 1). In this way, the PRT state provides new insights on how myosin detaches from F-actin and indicates that the theoretical weakly bound post-rigor state (Sweeney and Houdusse, 2010; Walklate et al., 2016) is unlikely to be populated within the motor cycle.

Although we find myosin-V-AppNHp strongly bound to F-actin in the PRT state (Figure 4—figure supplement 1), we had to significantly increase the myosin concentration to achieve full decoration of actin filaments (see Materials and methods for details), in agreement with a weaker binding affinity (Konrad and Goody, 2005; Yengo et al., 2002). We therefore conclude that AppNHp can potentially lead to different structural states, similar to ADP in myosin-IB (Mentes et al., 2018). Likely due to large differences in the binding affinity of these states or rapid detachment of myosin from F-actin, we only find myosin bound to F-actin in the PRT state. In line with this assumption, we find a significant amount of unbound myosin in the background of our AppNHp data sets (Figure 4—figure supplement 3). The 3D reconstruction and thus identification of the structural state of the background myosin were unfortunately impeded by a strong orientational preference of the myosin particles (Figure 4—figure supplement 3B). Further studies are therefore required to test the conformation of AppNHp-bound myosin-V in absence of F-actin.

### Conservation and specificity of the actomyosin-V interface

A comparison of the three states of the actomyosin-V complex (strong-ADP, rigor, and PRT state) reveals a striking similarity of the actomyosin interface (Figure 5, Figure 5—video 1). The atomic models superimpose almost perfectly with only little variations in the orientation of some incompletely resolved side chains. The remarkable similarity suggests that the same set of interactions is maintained during all strongly bound states of the myosin motor cycle, despite their varying F-actin-binding affinities. Differences in the affinity might therefore not be linked to altered contacts, but rather to the degree of structural flexibility inherent to each state (see below).

![Figure 5.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig5-v2.jpg)

**Figure 5.:** Comparison of the actomyosin-V interface within all three states (rigor: red; strong-ADP: orange; and AppNHp-bound PRT: purple) illustrating the remarkable similarity of interactions with F-actin. (Top) Front and back views of the central myosin molecule and the two actin subunits it is bound to (shades of green and blue, A+1 and A-1; see Figure 1—figure supplement 3 for color code). Black boxes indicate the location of close-up views shown below. (Bottom) Close-up views of all actin-myosin interfaces including the cardiomyopathy (CM) loop, the helix-loop-helix (HLH) motif, loops 2–4, and the activation loop (highlighted by an asterisk). Side chains of key residues are displayed and labeled for all states (rigor: black; ADP and AppNHp: gray). Dashed lines indicate hydrogen bonds predicted for the rigor (black) and ADP/AppNHp state (gray), respectively. See Figure 5—video 1 for a three-dimensional visualization including density maps.

The actomyosin-V interface comprises six structural elements, namely the cardiomyopathy (CM) loop (aa 376–392), loop 4 (aa 338–354), the helix-loop-helix (HLH) motif (505–531), the activation loop (aa 501–504), loop 3 (aa 532–546), and loop 2 (aa 594–635) (Figure 5, Figure 5—video 1). While these elements represent a common set of actin-binding elements, most of which have conserved hydrophobic and electrostatic properties, not all myosins utilize all of them. Moreover, the precise nature of individual interactions and the residues involved varies considerably among myosins, largely due to sequence variations known to tune the kinetic properties of myosin (Mentes et al., 2018; Robert-Paganin et al., 2021). Comparisons of the actomyosin interface of different myosins are therefore essential for identifying common and specific features of the myosin superfamily.

A detailed comparison of the actomyosin interface of myosin-V with previously published actomyosin structures (Banerjee et al., 2017; Behrmann et al., 2012; Doran et al., 2020; Gong et al., 2021; Gurel et al., 2017; Mentes et al., 2018; Risi et al., 2021; Robert-Paganin et al., 2021; Vahokoski et al., 2020; von der Ecken et al., 2016) shows many common features, but also some myosin-V-specific ones. The tightest and most conserved contact is formed by the HLH motif (Robert-Paganin et al., 2021). In analogy to other myosins, it relies primarily on extensive hydrophobic contacts with F-actin, complemented by a series of hydrogen bonds (predicted by PDBsum [Laskowski et al., 2018], Figure 5, Figure 5—video 1E and F). The comparably short CM loop of myosin-V is also highly conserved, with respect to its hydrophobic nature. However, unlike the CM loop of other myosins (Fujii and Namba, 2017; Gurel et al., 2017; Mentes et al., 2018; Risi et al., 2021; von der Ecken et al., 2016), its tip does not engage in complementary electrostatic interactions (Figure 5, Figure 5—video 1C). The conformation we found for loop 4 differs from all others reported so far. Not only is it more compact, folding in a β-hairpin, but it also localizes closer to the base of the CM loop, where it is stabilized by a non-conserved hydrogen bond between C348 and I391 (Figure 5, Figure 5—video 1C). However, its electrostatic interactions with F-actin are reminiscent of those reported for other myosins (Fujii and Namba, 2017; Gurel et al., 2017; Risi et al., 2021; von der Ecken et al., 2016). Loop 2 is exceptionally long in myosin-V and only partially resolved in our structures (Figure 5—video 1). While this is also the case for most actomyosin structures resolved so far (Banerjee et al., 2017; Doran et al., 2020; Gong et al., 2021; Risi et al., 2021; Robert-Paganin et al., 2021; von der Ecken et al., 2016), loop 2 of myosin-V stands out by the unique α-helical fold of its C-terminal part (Figure 5—video 1I). This fold facilitates a compact packing of basic residues and thereby promotes the electrostatic interactions commonly found at the loop 2 interface. The activation loop is a structural element that does not contribute to F-actin binding in all myosins (Gurel et al., 2017; Robert-Paganin et al., 2021). In myosin-V, it forms primarily electrostatic interactions with the N-terminus of F-actin, but does not lead to its ordering, as has been reported for other myosins (Figure 5, Figure 5—video 1E; Banerjee et al., 2017; Behrmann et al., 2012; Fujii and Namba, 2017; Mentes et al., 2018; Vahokoski et al., 2020). The last structural element involved in actin binding is loop 3. It forms the so-called Milligan contact (Milligan et al., 1990), which is strong in myosin-V and includes electrostatic and hydrophobic interactions as well as several hydrogen bonds (Figure 5, Figure 5—video 1H). The contact is furthermore strengthened by hydrogen bonds between K540-N545 and S544-K546 that stabilize the conformation of loop 3. Interestingly, a strong Milligan contact has also been reported for myosin-IB and -VI (Gurel et al., 2017; Mentes et al., 2018), whereas no or only weak interactions were found in class II myosins (Doran et al., 2020; Fujii and Namba, 2017; Risi et al., 2021; von der Ecken et al., 2016). We therefore speculate that an intimate Milligan contact might be a general feature of myosins with long actin-attachment lifetimes and high binding affinities for F-actin and ADP, allowing them to bind particularly tightly to fulfill their function as cargo transporters or molecular anchors.

In summary, we demonstrated that myosin-V establishes a maximum of contacts with F-actin, utilizing all six potential binding elements (Figure 5, Figure 5—video 1E and F). In addition, we have identified a previously unseen α-helical fold of the C-terminus of loop 2 (Figure 5, Figure 5—video 1I), which possibly strengthens the interactions at this interface.

### Myosin-V specifically selects the closed D-loop conformation of F-actin

To assess the structural effect of myosin binding on F-actin, we compared the structure of aged F-actin-PHD in the presence (rigor state, representative for all states) and absence of myosin-V (PDB: 6T20; Pospich et al., 2020; Figure 6). The observed differences are subtle and primarily involve the DNase-binding loop (D-loop, aa 39–55) of F-actin and loops known for their flexibility (Pospich et al., 2020). The most prominent alteration involves glutamine Q49 within the D-loop, which moves away from the actomyosin interface by ~2 Å to enable the formation of a hydrogen bond with N529 in the HLH motif of myosin (Figure 5 and Figure 6). Similar, but not identical, subtle changes have been reported for other actomyosins (Behrmann et al., 2012; Gong et al., 2021; Gurel et al., 2017; Robert-Paganin et al., 2021; von der Ecken et al., 2016), in addition to an ordering of the N-terminus of actin (Banerjee et al., 2017; Behrmann et al., 2012; Fujii and Namba, 2017; Mentes et al., 2018; Vahokoski et al., 2020; von der Ecken et al., 2016), which we do not observe for myosin-V.

![Figure 6.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig6-v2.jpg)

**Figure 6.:** Illustration of the structural similarity of aged F-actin-PHD in the absence and presence of myosin. (A) Atomic model of aged F-actin-PHD (PDB: 6T20; Pospich et al., 2020; three subunits shown, A-1 to A+1) color-coded by the backbone root mean square deviation (RMSD) of this structure with the one of aged F-actin-PHD decorated with myosin-V in the rigor state. (B) Close-up view of the D-loop interface illustrating that the structural changes associated with myosin binding are small. For a direct comparison, the atomic model of the rigor actomyosin-V complex is superimposed (transparent gray). F-actin subunits were aligned individually to account for errors in the calibration of the pixel size. (C) Comparison of LAFTER density maps of aged F-actin-PHD on its own (blue mesh) and bound to myosin-V (gray). For guidance, the atomic model of F-actin-PHD colored by RMSD is also shown. See Table 5 for a comparison of helical symmetry parameters.

Notably, our data show no significant change of the helical symmetry parameters upon myosin binding, neither in rigor nor in any other state of myosin (Table 5). This is in stark contrast to an earlier medium-resolution study of myosin-V, which reported additional twisting of PHD-stabilized F-actin dependent upon the nucleotide state of myosin (Wulf et al., 2016).

**Table 5.**
 Summary of helical symmetry parameters.Overview of helical symmetry parameters of aged PHD-stabilized and young JASP-stabilized actomyosin-V complexes. For a direct comparison, the parameters of aged F-actin-PHD (PDB: 6T20; Pospich et al., 2020) and young F-actin-JASP (PDB: 5OOD; Merino et al., 2018) are shown alongside. Differences in both the helical rise and twist can be readily explained by errors of the pixel size, which is not identical for all data sets. Helical parameters were estimated from the atomic model of five consecutive subunits independently fitted into the map; see Pospich et al., 2017 for details. To make results more comparable, only actin subunits were considered during fitting. Note that fitting inaccuracies can also give rise to small deviations.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Rise (Å)</th>
      <th>Twist (°)</th>
      <th>Pixel size (Å)</th>
    </tr>
    <tr>
      <th>Helical symmetry</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aged F-actin-PHD+ rigor</td>
      <td>27.82±0.02</td>
      <td>–167.27±0.02</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>Aged F-actin-PHD+ ADP</td>
      <td>27.81±0.02</td>
      <td>–167.32±0.02</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>Aged F-actin-PHD+ AppNHp</td>
      <td>27.77±0.02</td>
      <td>–167.32±0.02</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Aged F-actin-PHD (PDB: 6T20)</td>
      <td>27.59±0.02</td>
      <td>–166.9±0.1</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Young F-actin-JASP</td>
      <td>27.85±0.08</td>
      <td>–166.87±0.02</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td>Young F-actin-JASP+ Rigor</td>
      <td>27.72±0.01</td>
      <td>–167.06±0.02</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Young F-actin-JASP (PDB: 5OOD)</td>
      <td>27.39</td>
      <td>–166.41</td>
      <td>1.09</td>
    </tr>
  </tbody>
</table>

It was reported that myosin-V is sensitive to the nucleotide state of F-actin and prefers young PHD-stabilized F-actin over aged F-actin-PHD (Zimmermann et al., 2015). We have recently shown that young ATP/ADP-Pi-bound and aged ADP-bound F-actin primarily differ in their conformation of the D-loop-C-terminus interface and that actin-binding proteins like coronin-IB (Cai et al., 2007) probably recognize the nucleotide state of F-actin from this interface (Merino et al., 2018). We have furthermore shown that the short-lived ATP/ADP-Pi-bound state of F-actin can be specifically stabilized using either PHD (Lynen and Wieland, 1938) or jasplakinolide (JASP) (Crews et al., 1986; Pospich et al., 2020). To reveal the structural mechanism by which myosin-V senses the nucleotide state of F-actin, we have solved the structure of myosin-V in the rigor state in complex with young JASP-stabilized F-actin (F-actin-JASP) to 3.2 Å (referred to as young actomyosin-V, Figure 7, Table 6, Figure 7—figure supplement 1, Figure 1—figure supplement 1, Table 1). The atomic model of myosin in this structure superimposes perfectly with the one bound to aged F-actin-PHD (Figure 7C and D), indicating that the nucleotide state of F-actin has no structural effect on myosin-V in the rigor state. Surprisingly, and despite having ADP-Pi bound to its active site (Figure 1—figure supplement 3), F-actin adopts the closed D-loop state, which is characteristic for aged ADP-bound F-actin (Figure 7; Merino et al., 2018). However, a control structure of F-actin-JASP alone (3.1 Å, Figure 7—figure supplement 1, Table 1, Table 6, Figure 1—figure supplement 1) confirms that actin was successfully stabilized in the desired young state, having a characteristic open D-loop conformation (Figure 7—figure supplement 2) and ADP-Pi bound to its active site (Figure 1—figure supplement 3). Thus, we conclude that binding of myosin-V to young F-actin-JASP induces structural changes that ultimately result in the closed D-loop conformation (Figure 8, Figure 8—video 1, Figure 8—figure supplement 1), thereby abolishing the effect of JASP (Pospich et al., 2020). Interestingly, our data show that the open D-loop state would not clash with bound myosin (Figure 8C and D). The closed conformation may therefore be selected for its superior shape complementarity to myosin, which possibly establishes a strong binding interface between the D-loop and HLH motif and by doing so contributes to the high-binding affinity of the rigor state (Figure 8).

![Figure 7.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig7-v2.jpg)

**Figure 7.:** (A) Atomic model and LAFTER density map of the central myosin-V-LC subunit (red, LC: white) bound to young F-actin-JASP (shades of blue, three subunits shown, A-1 to A+1). Nucleotides and JASP are highlighted in orange and yellow, respectively; also see Figure 8—video 1F–H. (B) Illustration of the model-map agreement within a central section of myosin. Most side chains are resolved by the post-refined density map (transparent gray). (C) Superposition and (D) color-coded root mean square deviation (RMSD) of the young and aged actomyosin-V complex in the rigor state illustrating their structural identity. Residues with increased RMSD solely localize to regions of lower local resolution and can therefore be explained by modeling inaccuracies. See Figure 7—figure supplement 1 and Table 6 for an overview of the cryo-EM data and refinement and model building statistics, respectively. The structure of young F-actin-JASP in the absence of myosin is shown in Figure 7—figure supplement 2.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Representative micrographs at –1.3 μm defocus and (B) their power spectra. (C) Fourier shell correlation (FSC) curves for masked (darker shade, with resolution values) and unmasked (lighter shade) half maps. For bare F-actin, the FSC of a map covering the central three subunits is shown (shades of blue), while for actomyosin either the FSC for three actin subunits and two myosin molecules (central 3er/2er, shades of blue) or for one actomyosin subunit (signal subtracted, central 1er, shades of green) is shown. (D) Color-coded local resolution of full filaments for both data sets and of the (E) signal-subtracted central subunit of the young actomyosin complex. Note that signal subtraction was only performed for actomyosin complexes; also see Figure 1—figure supplement 1. Scale bar 500 Å.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A) Atomic model and LAFTER density map of young F-actin-JASP (shades of blue, three subunits shown, A-1 to A+1). Nucleotides and JASP are highlighted in orange and yellow, respectively; also see Figure 8—video 1A–C. (B) Illustration of the model-map agreement within a central section of myosin. Most side chains are resolved by the post-refined density map (transparent gray).

**Table 6.**
 Statistics of young actomyosin in the rigor state.Refinement and model building statistics of young F-actin-JASP alone and in complex with myosin-V in the rigor state.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th>Young F-actin-JASP</th>
      <th colspan="5">Rigor state: young F-actin-JASP + myosin-Va-LC</th>
    </tr>
    <tr>
      <th>Actin only3er/2er</th>
      <th>Central 3er/2er</th>
      <th>Central 1er(subtracted)</th>
      <th>Class 1</th>
      <th>Class 2</th>
      <th>Class 4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">3D refinement statistics</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of helical segments</td>
      <td>212,660</td>
      <td>414,148</td>
      <td>414,148</td>
      <td>110,797</td>
      <td>107,022</td>
      <td>107,174</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>3.1</td>
      <td>3.2</td>
      <td>3.2</td>
      <td>3.6</td>
      <td>3.5</td>
      <td>3.6</td>
    </tr>
    <tr>
      <td>Map sharpening factor (Å2)</td>
      <td>–56</td>
      <td>–83</td>
      <td>–50</td>
      <td>–55</td>
      <td>–49</td>
      <td>–54</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="4">Atomic model statistics</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Non-hydrogen atoms</td>
      <td>8940</td>
      <td>23,278</td>
      <td>10,149</td>
      <td>10,169</td>
      <td>10,169</td>
      <td>10,156</td>
    </tr>
    <tr>
      <td>Cross-correlation masked</td>
      <td>0.81</td>
      <td>0.84</td>
      <td>0.83</td>
      <td>0.84</td>
      <td>0.83</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>MolProbity score</td>
      <td>1.27</td>
      <td>1.29</td>
      <td>1.15</td>
      <td>1.24</td>
      <td>1.26</td>
      <td>1.23</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>5.11</td>
      <td>5.46</td>
      <td>3.62</td>
      <td>4.66</td>
      <td>4.91</td>
      <td>4.57</td>
    </tr>
    <tr>
      <td>EMRinger score*</td>
      <td>3.11/3.08</td>
      <td>2.92/2.66</td>
      <td>3.11/2.92</td>
      <td>2.89/2.96</td>
      <td>2.99/3.39</td>
      <td>2.88/2.55</td>
    </tr>
    <tr>
      <td>Bond RMSD (Å)</td>
      <td>0.004</td>
      <td>0.004</td>
      <td>0.009</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>Angle RMSD (°)</td>
      <td>0.915</td>
      <td>0.780</td>
      <td>0.950</td>
      <td>0.836</td>
      <td>0.807</td>
      <td>0.835</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>100.00</td>
      <td>99.86</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
      <td>99.84</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>CaBLAM outliers (%)</td>
      <td>0.27</td>
      <td>0.75</td>
      <td>0.90</td>
      <td>0.81</td>
      <td>0.65</td>
      <td>0.49</td>
    </tr>
  </tbody>
</table>

_*Values correspond to score against the post-refined map used for real-space refinement/a map filtered to local resolution._

![Figure 8.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig8-v2.jpg)

**Figure 8.:** (A) Atomic model and LAFTER density map of young F-actin-JASP (shades of blue, subunits A-1 and A+1). Before myosin binding, the D-loop primarily adopts the open conformation and the C-terminus is extended. A superimposed atomic model (gray) highlights a minor density potentially corresponding to the closed D-loop conformation. (B) Binding of myosin-V in the rigor state (red) causes a structural transition to the closed D-loop conformation, which comes with an α-helical C-terminus; also see Figure 8—video 1 and Figure 8—figure supplement 1. (C) Surface representation of young F-actin-JASP (open D-loop, as shown in A) illustrating that the open D-loop conformation would not clash with myosin (computationally docked). (D) Surface representation of the young JASP-stabilized actomyosin complex (closed D-loop, as shown in B). See Figure 8—figure supplement 2 for an illustration how pyrene labeling might interfere with myosin binding.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A, B) Root mean square deviation (RMSD) of young F-actin-JASP before and after myosin binding illustrating a major but spatially confined rearrangement of the D-loop and C-terminus interface. (C, D) Root mean square deviation (RMSD) highlighting the remarkable similarity of myosin-bound aged F-actin-PHD and myosin-bound young F-actin-JASP. Subunits were aligned individually to account for errors in the calibration of the pixel size.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** (A) Root mean square deviation (RMSD) of pyrene-labeled F-actin bound to ADP-Pi (PDB: 7K21; Chou and Pollard, 2020) and young F-actin-JASP in complex with myosin-V illustrating that differences primarily localize to the D-loop and C-terminus interface (black box). Subunits were aligned individually to account for errors in the calibration of the pixel size. (B) Close-up view of the D-loop C-terminus interface of pyrene-labeled F-actin bound to ADP-Pi (shades of green, PDB: 7K21; Chou and Pollard, 2020). Pyrene (magenta) wedges in-between the D-loop and C-terminus and thereby displaces the D-loop. In this way, pyrene likely interferes with myosin (transparent red) selecting the closed D-loop conformation (transparent gray).

Our structure does not provide a structural explanation for the reported nucleotide-sensitivity of myosin-V (Zimmermann et al., 2015). This could be due to three, possibly complementary, reasons. First, myosin-V might be sensitive to the nucleotide state of F-actin only in certain structural states, such as the initially binding PPS (Wulf et al., 2016) and PiR states (Llinas et al., 2015). Second, the structural plasticity of young ATP/ADP-Pi-bound F-actin (Kueh and Mitchison, 2009), rather than the open D-loop conformation, might be beneficial for myosin binding. Third, the open D-loop conformation might promote the formation of initial contacts with myosin-V. Once these are established, the subsequent transition from a weak- to a strong binding state potentially causes a structural transition of F-actin, eventually locking it in the closed D-loop conformation. In line with these theories, a number of biochemical and biophysical studies suggested that a structural rearrangement of F-actin and its structural plasticity are critical for proper myosin activity (Anson et al., 1995; Drummond et al., 1990; Kim et al., 2002; Nishikawa et al., 2002; Noguchi et al., 2012; Oztug Durer et al., 2011; Prochniewicz and Thomas, 2001; Prochniewicz et al., 2010). Moreover, the D-loop C-terminus interface was predicted to contribute to the initial binding interface of myosin (Gurel et al., 2017; Lehman et al., 2013; Risi et al., 2017; Robert-Paganin et al., 2020).

Finally, the conformational selection mechanism of myosin-V offers a structural explanation for the quenching of pyrene fluorescence upon myosin binding. Pyrene conjugated to cysteine 374 in the C-terminus of F-actin has been often used to report not only actin kinetics, but also myosin binding (Kouyama and Mihashi, 1981). Closure of the actin-binding cleft of myosin is thought to expose pyrene to the solvent and thus cause fluorescence quenching (Chou and Pollard, 2020), but the exact timing and the structural basis are not yet known (Llinas et al., 2015; Robert-Paganin et al., 2020). A recent cryo-EM structure of pyrene-labeled F-actin has revealed that pyrene wedges itself between the tip of the D-loop and the hydrophobic groove surrounding it, partially pushing the D-loop out of its binding pocket (Chou and Pollard, 2020). This likely interferes with myosin selecting the closed D-loop state (Figure 8—figure supplement 2). We furthermore suggest that myosin quenches the fluorescence of pyrene by pushing it out of its binding pocket when selecting the closed D-loop state during its transition to a strong binding state.

### Pronounced structural heterogeneity of myosin-V

To identify a potential mixture of structural states, we performed 3D classifications of signal-subtracted particles for all our data sets (Figure 1—figure supplement 1). Interestingly, the results indicate a continuous conformational heterogeneity of myosin-V as opposed to a mixture of several discrete structural states (see Materials and methods for details). Based on the identified 3D classes, we solved and modeled a total of 18 high-resolution (<3.7 Å) structures of actomyosin-V (Figure 1—figure supplement 1, Table 2, Table 3, Table 4 and Table 6). A superposition of all structures from one data set illustrates pronounced structural flexibility of all domains, but the L50 domain, F-actin, and the actomyosin interface (Figure 9, also see Figure 5). Primarily, the U50 domain pivots and moves toward or away from the actin interface, resulting in twisting and shifting of the central transducer β-sheet, which is coupled to rotations of the N-terminal and the converter domain (Figure 9A). In this way, pivoting of the U50 domain leads to different lever arm positions within the 3D classes of a single data set (Figure 9A, Figure 9—video 1, Figure 9—video 2, Figure 9—video 3). The extent (~9–12°) of the relative lever arm swings is intriguing (Figure 9A, Figure 9—figure supplement 1), considering that the swing associated with Mg2+-ADP-release is only ~9° for myosin-V (Figure 3).

![Figure 9.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig9-v2.jpg)

**Figure 9.:** Illustration of the conformational heterogeneity of myosin-V in the rigor (red), strong-ADP (orange), and AppNHp-bound post-rigor transition (PRT) state (purple) when bound to F-actin (aged F-actin-PHD: sea green; young F-actin-JASP: blue). (A) Superposition of all atomic models (central 1er, average: opaque; 3D classes: transparent) built for each state. Models were either aligned on the F-actin subunit or the HF helix (indicated by black arrowhead). Pivoting of the U50 domain in combination with shifting and twisting of the central transducer β-sheet results in a rotation of the N-terminal and converter domain, giving rise to a two-dimensional distribution of lever arm orientations. The extent of these changes depends on the nucleotide state and is largest in the strong-ADP and PRT state. Insets show either the transducer β-sheet (black dot) or the active site (asterisk), which basically remains unchanged within all models of one state. (B) Mapping of atomic models (average and 3D classes) into the first two principal components of a principal component analysis (PCA) illustrating the overall conformational space covered. Classes are labeled by their number (#1–#8; also see Figure 1—figure supplement 1). For a comparison of conformational extremes, see Figure 9—figure supplement 1. Morphs of extremes and trajectories along the principal components are visualized in Figure 9—video 1, Figure 9—video 2, and Figure 9—video 3. See Figure 1—figure supplement 6 for an overview of the domain architecture of myosin.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** Extreme conformations of myosin-V in the rigor, strong-ADP, and AppNHp-bound PRT state. (A) Superposition of atomic models as shown in Figure 9, but displaying only the extreme structures along the first principal component (yellow and gray). (B) Mapping of atomic models (average and 3D classes) into the first two principal components as shown in Figure 9. The localization of the extreme structures shown in (A) is highlighted by a yellow and gray dot, respectively.

Our data show that the conformational heterogeneity of myosin-V is not caused by variations of the active site or mixed nucleotide states (Figure 9). Nevertheless, the presence of a nucleotide does affect the extent of flexibility as ADP and AppNHp lead to a greater change in lever arm position (Figure 9A). This tendency is also reflected by the size of the respective conformational spaces when mapping all models belonging to one data set onto their principal components (PCs) using principal component analysis (PCA) (Figure 9B).

To impartially compare the conformations of the different nucleotide states of myosin-V, we performed a PCA of all models (Figure 10). The structural similarity and differences of the atomic models are well reflected by their localization within the PC space as well as their corresponding conformational spaces (Figure 10A). Notably, the significantly larger conformational space of the AppNHp data indicates a considerable difference to the rigor state, supporting our proposal of a PRT state. The fact that the conformational spaces of the strong-ADP and rigor state do not overlap is anticipated, given that we have oversaturated myosin with Mg2+-ADP (see Materials and methods).

![Figure 10.](https://cdn.elifesciences.org/articles/73724/elife-73724-fig10-v2.jpg)

**Figure 10.:** Principal component analysis of all atomic models of the actomyosin-V complex, including average and 3D class average models of the strong-ADP, rigor, and post-rigor transition (PRT) state (central actomyosin subunit only). (A) Mapping of atomic models into the first and second as well as the second and third principal components. Data points are colored by the state of the actomyosin-V complex (aged rigor: red; aged strong-ADP: orange; aged AppNHp-bound PRT: purple; and young rigor: blue). Atomic models of average structures are shown as opaque, and models of 3D classes as transparent. The conformational space covered within each state is indicated by a correspondingly colored 2D polygon. (B) Superposition of all lever arm positions reflecting the relative mapping of individual conformational spaces. Changes along the first and third principal components are highlighted by black and gray arrows, respectively (extremes marked with asterisks). (C) Color-coded trajectories along the first, second, and third principal components (red minimum, blue maximum). Arrows indicate the mapped conformational changes. (D) Same views as in (C) but showing the extreme structures along each principal component; see Figure 9 for color code. For an animation of trajectories and morphs of the extreme structures, see Figure 10—video 1; and see Figure 1—figure supplement 6 for an overview of the domain architecture of myosin.

The conformational changes mapped on each PC are readily illustrated by their corresponding trajectories as well as the extreme structures along each PC (Figure 10C, Figure 10—video 1). The motions along the first and second PCs correspond to an almost perpendicular pivoting of the U50 domain, causing a twist and shift of the central transducer β-sheet and ultimately rotations of the N-terminal and converter domain. The third PC maps a rotation of the N-terminal and converter domain around the transducer, which acts as a hinge region. Since all average structures localize close to the origin of PC 3 (Figure 10A, Figure 10—video 1E and F), we suggest that this PC accounts for an inherent flexibility of the transducer β-sheet.

The rearrangements, especially along the first PC, are reminiscent of the structural transition of myosin-V upon Mg2+-ADP release (Figures 3 and 10C, Figure 10—video 1). In line with this, we find the strong-ADP and rigor average structures to be arranged diagonally within the PC 1–PC 2 space (Figure 10A). This indicates that the conformational heterogeneity of myosin-V as well as the isomerization associated with Mg2+-ADP release relies on the same principal coupling mechanism. Furthermore, this suggests that the structural transition of myosin-V along its motor cycle is driven, at least in part, by its conformational flexibility. Based on this, we therefore propose that the active site of myosin-V is not mechanically, and thus rigidly, coupled to the surrounding domains, particularly the lever arm, as previously proposed (Fischer et al., 2005). Rather, its coupling seems to be statistical in nature, ultimately leading to a thermodynamic ensemble of conformations within each state. The associated structural flexibility of myosin-V possibly initiates transitions between structural states by giving rise to short-lived intermediate conformations with favorable nucleotide-binding affinities. Interactions with a nucleotide would consequently not trigger the transition, but merely stabilize myosin in its transient conformation, thereby promoting the transition to a new structural ensemble state.

A non-rigid, stochastic coupling of the active site of myosin-V is in good agreement with the release of Mg2+-ADP due to an isomerization as well as the existence of the PRT state. It also provides a good explanation for the different binding affinities of the rigor and strong-ADP state. Specifically, we propose that the extent of conformational heterogeneity tunes the binding affinity rather than changes in the actomyosin interface since these are almost the same in all three nucleotide states studied (Figure 5). Restrictions of the conformational space by external forces, that is, load on the lever arm, could account for the load dependence of transitions within the cycle, such as the delay of ADP release under load (Mentes et al., 2018).

The conformational flexibility we observe (Figures 9 and 10) as well as our conclusions on its role in the motor cycle are in line with more than two decades of molecular spectroscopy experiments, which have primarily, but not exclusively, studied myosin-II. In particular, site-directed labeling has demonstrated that myosin is highly dynamic and that multiple, functionally relevant structural states coexist within a single biochemical state (Forkey et al., 2003; Nesmelov et al., 2008; Nesmelov et al., 2011; Thomas et al., 2009). Moreover, it was shown that neither the active site is tightly coupled to the structural domains of the motor nor are the domains themselves (Klein et al., 2008; Korman et al., 2006; Naber et al., 2010; Sun et al., 2006). Our results extend the spectroscopic data, which have already elucidated conformational amplitudes and kinetics, by directly visualizing the dynamics of myosin as well as the underlying molecular coupling.

While the agreement of our results with the spectroscopic data on myosin-II (Thomas et al., 2009) already suggests that statistical coupling and conformational flexibility are general features of the myosin superfamily, rather than a hallmark of myosin-V, there are additional independent indications. On the one hand, statistical coupling of the active site has also been proposed for myosin-VI based on a recovery stroke intermediate crystal structure, showing that the lever arm can partially re-prime while the active site remains unchanged (Blanc et al., 2018). On the other hand, conformational heterogeneity has also been reported for myosin-IE and -IB based on either crystal structures or cryo-EM data of the actomyosin complex (Behrmann et al., 2012; Kollmar et al., 2002; Mentes et al., 2018). Notably, a flexibility reminiscent of the one observed for myosin-V (Figures 9 and 10) was reported for myosin-IE in the rigor state (Behrmann et al., 2012). Conversely, no flexibility was described for myosin-IB, which adopts a single state in the absence of a nucleotide and two discrete states when bound to Mg2+-ADP (Mentes et al., 2018). Whether these results reflect properties of specific myosins or rather current limitations of data analysis methods, for example, number of particles, low signal-to-noise ratio, robustness of 3D classifications (Pospich and Raunser, 2018), remains to be investigated. In general, there is little structural data on the conformational dynamics of myosin as most structures originate either from small cryo-EM data sets, which have an insufficient number of particles for extensive 3D classifications, or from X-ray crystallography. We therefore believe that the structural characterization of myosin’s dynamic landscape will provide novel insights into the details of force generation.

### Summary

The presented high-resolution cryo-EM structures of the actomyosin-V complex in three nucleotide states—nucleotide-free, Mg2+-ADP, and Mg2+-AppNHp (Table 1)—provide valuable insights into the structural basis of force generation. First, a comparison of the strong-ADP (Figure 1) and rigor state (Figure 2) has revealed the structural transition of myosin-V upon Mg2+-ADP-release (Figure 3), which is reminiscent of the one of myosin-IB (Mentes et al., 2018) and yet differs in its details. Second, the structure of Mg2+-AppNHp-bound myosin-V has uncovered a previously unseen post-rigor transition (PRT) state (Figure 4), which is strongly bound to F-actin and adopts a conformation resembling the rigor state. Because of the weak binding to the active site, AppNHp, and probably ATP, does not directly trigger the detachment from F-actin and thus the transition to the post-rigor state. Instead, strong nucleotide binding likely needs to be established to eventually initiate detachment.

Interestingly, and despite the differences in the F-actin-binding affinity, we find that the actin-binding interface is basically indistinguishable in all three nucleotide states (Figure 5), suggesting that strongly bound states utilize a common binding scheme. Furthermore, a comparison of the interface with the one of other myosins has revealed specific features of the myosin-V interface and indicates that a strong Milligan contact (Milligan et al., 1990) is characteristic of myosins with long lifetimes of actin-bound states and high binding affinities for ADP and F-actin, as found in high duty-ratio myosins and myosin-IB (Laakso et al., 2008; Lewis et al., 2006).

In contrast to previous reports (Wulf et al., 2016), our results elucidate that myosin-V hardly alters the structure of aged F-actin-PHD (Figure 6). Conversely, it has a remarkable effect on the structure of young F-actin-JASP, specifically selecting the closed D-loop state (Figures 7 and 8) and thereby overriding the ‘rejuvenating effect’ of JASP (Merino et al., 2018; Pospich et al., 2020). Whilst this result does not reveal the structural basis of myosin-V’s nucleotide sensitivity (Zimmermann et al., 2015), it offers an explanation for pyrene fluorescence quenching upon myosin binding (Kouyama and Mihashi, 1981).

Additional heterogeneity analysis of our data revealed a pronounced structural flexibility of myosin-V (Figures 9 and 10), indicating a non-rigid, stochastic coupling of the active site. While the extent of flexibility is altered by the presence of a nucleotide, structural transitions of myosin-V are likely not initiated by binding of a specific nucleotide, but rather by thermodynamic fluctuations, as previously suggested for myosin-VI (Blanc et al., 2018).

Taken together, we have elucidated many, previously unknown details of the force generation mechanism. The general validity of these results, that is, if they are limited to myosin-V or hold for the complete myosin superfamily, as well as the possible implications of our findings has to be thoroughly tested in future studies. Structural data on how actin activates myosin and how myosin eventually detaches will surely be of interest (Robert-Paganin et al., 2020; Schröder, 2020; Sweeney et al., 2020). Yet, great insights could also come from the structural characterization of myosin’s dynamic landscape. Finally, unraveling the structural basis of nucleotide sensitivity (Zimmermann et al., 2015) will further promote our understanding of the regulation of both myosin and the actin cytoskeleton (Merino et al., 2020).

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
      <td>Gene (Gallus gallus)</td>
      <td>MYO5A</td>
      <td>De La Cruz et al., 1999</td>
      <td>Uniprot ID:Q02440</td>
      <td>Unconventional myosin-Va</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>MYL6B (MLC1SA)</td>
      <td>De La Cruz et al., 1999</td>
      <td>Uniprot ID:P14649</td>
      <td>Myosin light chain 6B/myosin LC 1 – slow-twitch muscle A isoform</td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>SF9 cells</td>
      <td>De La Cruz et al., 1999</td>
      <td></td>
      <td>Insect cells, for baculovirus expression</td>
    </tr>
    <tr>
      <td>Biological sample (Oryctolagus cuniculus)</td>
      <td>Rabbit skeletal muscle acetone powder</td>
      <td>Gift from W. Linke and A. Unger (Ruhr-Universität Bochum, Germany)</td>
      <td>N/A</td>
      <td>For purification of α-actin (Uniprot ID:P68135)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pVL1392 pVL1393(plasmids)</td>
      <td>De La Cruz et al., 1999</td>
      <td>Invitrogen, V1392-20</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phalloidin (PHD)Amanita phalloides</td>
      <td>Sigma-Aldrich</td>
      <td>P2141</td>
      <td>For stabilization of aged ADP-bound F-actin</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Jasplakinolide (JASP)</td>
      <td>Sigma-Aldrich</td>
      <td>J4580</td>
      <td>For stabilization of young ADP-Pi-bound F-actin</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>AppNHp (AMPPNP)</td>
      <td>Jena Bioscience</td>
      <td>NU-407-10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ADP</td>
      <td>Sigma-Aldrich</td>
      <td>A2754</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>TranSPHIRE</td>
      <td>Stabrin et al., 2020; PMID:33177513</td>
      <td>v1.4–1.5.7</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>Zheng et al., 2017; PMID:28250466</td>
      <td>v1.1.0; v1.3.0; v1.2.6</td>
      <td>Within TranSPHIRE</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GCTF</td>
      <td>Zhang, 2016; PMID:26592709</td>
      <td>v1.06</td>
      <td>Within TranSPHIRE</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>crYOLO</td>
      <td>Wagner et al., 2020; PMID:32627734</td>
      <td>v1.2.2; v1.2.4; v1.4.1</td>
      <td>Within TranSPHIRE</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GPU-ISAC</td>
      <td>Stabrin et al., 2020; PMID:33177513</td>
      <td>v1.2 and earlier</td>
      <td>Within TranSPHIRE</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cinderella</td>
      <td>Stabrin et al., 2020; PMID:33177513</td>
      <td>v0.3.1</td>
      <td>Within TranSPHIRE</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SPHIRE</td>
      <td>Moriya et al., 2017; PMID:28570515</td>
      <td>v1.3</td>
      <td>Helical processing pipeline, including CTF refinement and signal subtraction</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Relion</td>
      <td>Scheres, 2012; PMID:23000701</td>
      <td>v3.0.4</td>
      <td>For particle polishing and 3D classifications</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>Pettersen et al., 2004; PMID:15264254</td>
      <td>v1.15</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF ChimeraX</td>
      <td>Goddard et al., 2018; PMID:28710774</td>
      <td>v0.91</td>
      <td>For model building with ISOLDE</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ISOLDE</td>
      <td>Croll, 2018; PMID:29872003</td>
      <td>v1.0b4</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>Emsley et al., 2010; PMID:20383002</td>
      <td>v0.8.9.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix</td>
      <td>Adams et al., 2011; Afonine et al., 2018; PMID:18094468</td>
      <td>v1.17.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>elBOW</td>
      <td>Moriarty et al., 2009; PMID:19770504</td>
      <td>v1.17.1</td>
      <td>Within Phenix</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MolProbity</td>
      <td>Chen et al., 2010; PMID:20057044</td>
      <td>v1.17.1</td>
      <td>Within Phenix</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EMRinger</td>
      <td>Barad et al., 2015; PMID:26280328</td>
      <td>v1.17.1</td>
      <td>Within Phenix</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LAFTER</td>
      <td>Ramlaul et al., 2019; PMID:30502495</td>
      <td>v1.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Bio3d</td>
      <td>Grant et al., 2006; PMID:32734663</td>
      <td>v2.3-4</td>
      <td>Library for PCA in R</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DynDom</td>
      <td>Hayward and Lee, 2002; PMID:12463636;http://dyndom.cmp.uea.ac.uk</td>
      <td></td>
      <td>Accessed October 2020</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PDBsum</td>
      <td>Laskowski et al., 2018; PMID:28875543;https://www.ebi.ac.uk/pdbsum/</td>
      <td></td>
      <td>Accessed November 2020</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Cryo-EM grids</td>
      <td>Quantifoil (QF)</td>
      <td>R2/1 300 mesh</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Protein expression and purification

Actin was purified from rabbit skeletal muscle acetone powder by cycles of polymerization and depolymerization as described previously (Merino et al., 2018; Pardee and Spudich, 1982; Pospich et al., 2020). Purified G-actin was flash-frozen and stored in G-actin buffer (5 mM Tris pH 7.5, 1 mM DTT, 0.2 mM CaCl2, 2 mM NaN3, and 0.5 mM ATP) at –80°C.

Myosin V was expressed using the baculovirus/SF9 cell expression system. To create the recombinant virus used for expression, the cDNA coding for chicken myosin-Va was truncated after the codon corresponding to Arg792. This construct encompassed the motor domain and the first light chain/calmodulin-binding site of myosin-Va. A ‘Flag’ tag DNA sequence (encoding GDYKDDDDK) (Hopp et al., 1988) was appended to the truncated myosin-V coding sequence to facilitate purification. A truncated cDNA for the LC1-sa light chain (De La Cruz et al., 2000) was coexpressed with the truncated myosin-V heavy chain in SF9 cells as described in De La Cruz et al., 1999. The cells were grown for 72 hr in medium containing 0.2 mg/ml biotin, harvested and lysed by sonication in 10 mM imidazole, pH 7.4, 0.2 M NaCl, 1 mM EGTA, 5 mM MgCl2, 7% (w/v) sucrose, 2 mM DTT, 0.5 mM 4-(2-aminoethyl)benzenesuflonyl fluoride, 5 μg/ml leupeptin, and 2 mM MgATP. An additional 2 mM MgATP was added prior to a clarifying spin at 200,000 × g for 40 min. The supernatant was purified using FLAG-affinity chromatography (Sigma). The column was washed with 10 mM imidazole pH 7.4, 0.2 M NaCl, and 1 mM EGTA, and the myosin eluted from the column using the same buffer plus 0.1 mg/ml FLAG peptide. The fractions containing myosin were pooled and concentrated using an Amicon centrifugal filter device (Millipore) and dialyzed overnight against F-actin buffer (10 mM HEPES pH 7,5, 100 mM KCl, 2 mM MgCl2, 1 mM DTT, and 1 mM NaN3). Purified myosin-V-LC was flash-frozen and stored at –80°C.

### Sample preparation for cryo-EM

Aliquots of G-actin were freshly thawed and cleared by ultracentrifugation (Beckmann Rotors, TLA 120.1, 100.000 × g, 1 hr, 4°C). The concentration of G-actin was measured by absorption spectroscopy (Spectrophotometer DS-11, DeNovix, E290 nm ≈ 22,000 M–1 cm–1 at 290 nm; Hertzog and Carlier, 2005). Polymerization was induced by adding 100 mM KCl, 2 mM MgCl2, and 0.5 mM ATP. In case of young JASP-stabilized F-actin, actin was polymerized in the presence of a 2× molar excess of JASP (Sigma-Aldrich, freshly solved in DMSO, 1 mM stock). After 2 hr of incubation at room temperature, the sample was transferred to 4°C for further polymerization overnight. Filaments were collected by ultracentrifugation (Beckmann Rotors, TLA 120.1, 100.000 × g, 2 hr, 4°C) and pellets rinsed and resuspended in F-actin buffer (10 mM HEPES pH 7.5, 100 mM KCl, 2 mM MgCl2, 1 mM DTT, 1 mM NaN3) supplemented with 0.02 w/v% Tween 20 (to improve spreading of the sample droplet on the cryo-EM grid). No additional ADP or JASP was added. In case of aged PHD-stabilized F-actin, a 2× molar excess of PHD (Sigma-Aldrich, freshly solved in methanol, 1.25 mM stock) was added to resuspended filaments, which have aged, that is, hydrolyzed ATP and released the inorganic phosphate, during the overnight polymerization step. Filaments were stored at 4°C for a few hours before preparation of cryo-EM grids.

Aliquots of myosin-V-LC were freshly thawed, diluted 1:1 with F-actin buffer, and cleared by centrifugation (Eppendorf centrifuge 5424R, 21,000 × g, 5 min, 4°C). The concentration was determined by absorption spectroscopy (Spectrophotometer DS-11, DeNovix, E280 nm ≈ 106,580 M–1 cm–1 at 280 nm).

### Cryo-EM grid preparation and screening

To avoid bundling of actomyosin filaments, F-actin was decorated with myosin-V-LC on the grid, as described previously (von der Ecken et al., 2016). A freshly glow-discharged holey-carbon grid (QF R2/1 300 mesh, Quantifoil) was mounted to a Vitrobot cryoplunger (Thermo Fisher). 3 µl of F-actin (3–4 µM) were applied onto the front of the grid and incubated for 60 s. Excess solution was manually blotted from the side using blotting paper (Whatman No. 4). Immediately, 3 µl of myosin-V-LC (3–13 µM) were applied onto the grid and incubated for 30 s. The grid was automatically blotted for 9 s (blot force –15 or –25, drain time 0–1 s) and plunged into liquid ethane. The temperature was set to 13°C for all samples but the AppNHp sample, where either 4 or 25°C were used (two settings and data sets, see Table 1).

Myosin was kept in F-actin buffer and was only diluted and supplemented with a nucleotide and Tween 20 immediately before application to the grid to avoid any adverse effects. When preparing the strong-ADP state, myosin was diluted 1:1 in a 2× ADP buffer (F-actin buffer with 40 mM MgCl2, 4 mM ADP, and 0.04 w/v% Tween 20). For the rigor samples, myosin was diluted in F-actin buffer supplemented with 0.02 w/v% Tween 20. AppNHp-bound samples were prepared in analogy to rigor samples, but additional 5 mM AppNHp and 4 mM MgCl2 were added. As AppNHp hydrolyzes spontaneously, only freshly solved (10 mM HEPES pH 8.0, 1 mM DTT, 1 mM NaN3, and 2 mM MgCl2) or recently frozen AppNHp was used. Ion-pair reversed-phase chromatography experiments using freshly solved AppNHp indicated a purity of ≥98%, with 1.5% AppNH2 (hydrolysis product) and no preferential binding of AppNH2 to myosin. Thus, AppNH2 does not get enriched in the active site of myosin-V as it is the case for F-actin (Cooke and Murdoch, 1973). To increase the binding affinity of AppNHp-bound myosin to F-actin (Konrad and Goody, 2005), the concentration of potassium chloride in the myosin sample buffer was reduced to 10–13 mM KCl by dilution with F-actin buffer without KCl. F-actin samples were diluted using F-actin buffer supplemented with 0.02 w/v% Tween 20. After dilution to the final concentration, the PHD-stabilized F-actin samples contained 0.4–0.9% methanol.

Protein concentrations were adjusted empirically based on the overall concentration on the grid and decoration of actin filaments. The concentration of myosin required to saturate F-actin (3–4 µM) strongly depended on the nucleotide state; while 3–4 µM myosin were sufficient in case of the rigor and strong-ADP state, 10–13 µM myosin were required for the AppNHp sample, even though the salt concentration of the buffer was lowered to increase the binding affinity.

Grids were screened on a Talos Arctica microscope (Thermo Fisher) operated at 200 kV and equipped with a Falcon III direct detector (Thermo Fisher).

In total, six different samples were plunged, screened, and imaged; also see Table 1. On the one hand, aged PHD-stabilized F-actin was decorated with myosin-V-LC in three different nucleotide states, that is, in the absence of a nucleotide and bound to either Mg2+-ADP or Mg2+-AppNHp (aged rigor, ADP, and AppNHp). For the AppNHp-bound sample, two data sets were collected from grids that were plunged using different incubation temperatures, that is, 4°C or 25°C. On the other hand, young JASP-stabilized F-actin was imaged on its own and in complex with myosin-V-LC in the rigor state (young F-actin and rigor). The corresponding grids were prepared in one plunging session, that is, within a short time frame of 1–2 hr, using the same JASP-stabilized F-actin sample.

### Cryo-EM data acquisition

Data sets were acquired on Titan Krios microscopes (FEI Thermo Fisher) operated at 300 kV and equipped with a X-FEG using EPU. Specifically, data sets of the rigor and strong-ADP state were acquired on a standard Krios (Cs 2.7 mm, pixel size 1.06 Å), while a Cs-corrected Krios (pixel size 1.10 Å) was used for the remaining data sets. Equally dosed frames were collected using a K2 Summit (super-resolution mode, Gatan) direct electron detector in combination with a GIF quantum-energy filter (Bioquantum, Gatan) set to a slit width of 20 eV. For every hole, four micrographs consisting of 40 frames were collected close to the carbon edge, resulting in a total electron dose of ~79–82 eÅ–2 within an exposure time of 15 s. The defocus was varied within a range of ~0.4–3.2 µm. Acquisition details of all six data sets (aged rigor, ADP, and AppNHp 4°C + 25°C as well as young F-actin and rigor) including pixel size, electron dose, defocus range, and the total number of images collected are summarized in Table 1. Data acquisitions were monitored and evaluated live using TranSPHIRE (Stabrin et al., 2020).

### Cryo-EM data processing

Data sets were automatically preprocessed on-the-fly during the data acquisition using TranSPHIRE (Stabrin et al., 2020). Preprocessing included drift correction and dose weighting by MotionCor2 (Zheng et al., 2017), CTF estimation using GCTF (Zhang, 2016), and particle picking with crYOLO (Wagner et al., 2020; Wagner et al., 2019) (filament mode, box distance 26–27 px equivalent to one rise of ~27.5 Å, minimum number of boxes 6) for all data sets. The latest version of TranSPHIRE, which was used for the processing of the AppNHp data sets, also supported automatic, on-the-fly particle extraction (box size 320 px, filament width 200 px) as well as batch-wise 2D classification (batch size 13k, filament width 200 px, radius 150 px, 60–100 particles per class), 2D class selection, and 3D refinement using software of the SPHIRE package (Moriya et al., 2017). In particular, a GPU-accelerated version of ISAC (Stabrin et al., 2020; Yang et al., 2012) and the deep-learning 2D class selection tool Cinderella (Wagner, 2020) were used. For all other data sets, particles were extracted and 2D classified after data collection using analogous settings and helical SPHIRE 1.3 (Moriya et al., 2017; Stabrin et al., 2020). Particles that were not accounted during the initial, batch-wise 2D classification, for example, because they represent rare views, were merged and inputted to another round of 2D classification until no more stable classes were found. All micrographs were assessed manually and images sorted based on ice and protein quality, resulting in a removal of 6–36% of the data sets; see Table 1 for details. Particles contributing to classes found ‘good’ by either Cinderella or manual inspection and belonging to micrographs of good quality were written to virtual particle stacks for further processing in 3D.

As an initial 3D refinement and 3D classification revealed no differences in the overall structure of myosin in the two AppNHp data sets, plunged at 4°C and 25°C, corresponding particles were merged for further processing. The final number of particles ranged from 212,660 (young JASP-stabilized F-actin) to 2,446,218 (combined AppNHp data sets); see Table 2, Table 3, Table 4 and Table 6 for details. A concise overview of all key processing steps including the number of particles and nominal resolutions can be found in Figure 1—figure supplement 1.

All data sets were processed using the helical refinement program sp_meridien_alpha.py implemented in SPHIRE 1.3 (Moriya et al., 2017; Stabrin et al., 2020). In contrast to other helical refinement routines, SPHIRE does not refine or apply any helical symmetry, and thereby avoids possible symmetrization pitfalls. Instead, the software offers the usage of constraints tailored to helical specimen, for example, on the tilt angle and shift along the filament, to guide the refinement (also see Methods section of Pospich et al., 2021). For all 3D refinements, the tilt angle was softly restrained to the equator during exhaustive searches (--theta_min 90 --theta_max 90 --howmany 10). The shift along the filament axis was furthermore limited to plus or minus half of the rise (--helical_rise 27.5) to avoid shifts larger than one subunit. Finally, the smear (number of views considered for the reprojection of each particle) was reduced to a combined weight of 90% (--ccfpercentage 90). An initial 3D reference was created from the atomic model of a previously published actomyosin complex in the rigor state (PDB:5JLH, without tropomyosin; von der Ecken et al., 2016) and filtered to 25 Å using EMAN2 (Tang et al., 2007) and SPHIRE (Moriya et al., 2017). For the initial 3D refinement, a sampling angle of 3.7°, filament width of 120 px and a radius of 144 px (45% of the box size), but no 3D mask, was used. Based on the resulting 3D density map, a wide mask covering the central 85% of the filament was created. This map and mask were then used to run a fresh, global 3D refinement using the same settings as before. Based on the results of this refinement, particles were CTF refined within SPHIRE (Moriya et al., 2017) providing the nominal resolution according to the FSC0.143-criterion. CTF-refined particles were locally 3D refined using the final map of the previous 3D refinement filtered to 4 Å as reference. The fine angular sampling typically used in local refinements makes helical restraints superfluous as projections parameters can only locally relax anyways. For this reason, particles were locally refined using the non-helical 3D refinement program sp_meridien.py in combination with a sampling angle of 0.9°, a shift range of 2 px, and a shift step size of 0.5 px. In case of the young F-actin and young rigor data sets, the resolution could be further improved by particle polishing in Relion 3.0.4 (Scheres, 2012; Zivanov et al., 2018). For this purpose, refinement results were converted to Relion star format using sp_sphire2relion.py. Metadata of the initial motion correction step required for polishing were automatically created by TranSPHIRE and were directly provided. Polished particles were transferred back to SPHIRE and passed through another round of local 3D refinement using the same settings as before.

To focus the refinement on the central part of the filament, a wide mask containing the central three actin and central two myosin-V-LC subunits including all ligands (subvolume referred to as central 3er/2er map) was created and applied in a subsequent local 3D refinement. Post refinement of the resulting half maps using a central 3er/2er mask yielded maps with average resolutions ranging from 2.9 to 3.2 Å according to the FSC0.143-criterion; see Figure 1—figure supplement 1, Table 2, Table 3, Table 4 and Table 6 for details.

With the aim to further improve the density of myosin, the signal of all subunits but the central actomyosin subunit (subvolume referred to as central 1er map) was subtracted from the 2D particle images within SPHIRE 1.3 (Moriya et al., 2017). Particles were additionally recentered to bring the center of mass close to the center of the box. Signal-subtracted particles were subjected to another round of local 3D refinement applying a central 1er mask and filtering the centered reference map to 3.5 Å. Although post refinement of the resulting half maps using a central 1er mask did not yield density maps of higher nominal resolution, the map quality of especially myosin could be significantly improved; see Figure 1—figure supplements 1–2, Table 2, Table 3, Table 4, Table 6, and Figure 7—figure supplement 2 for details.

The anisotropic quality of the final central 1er maps suggested structural heterogeneity within myosin. For this reason, signal-subtracted particles and corresponding projection parameters were transferred to and 3D classified in Relion 3.0.4 (Scheres, 2012). As domain movement was assumed to be small and to reduce the risk of overrefinement, 3D alignment was deactivated (--skip_align) and the resolution strictly limited to 8 Å (--strict_highres_exp 8). The final central 1er map filtered to 15 Å was inputted as a reference, while a corresponding wide mask was applied and solvent flattening and CTF correction activated. The regularization parameter T and number of classes K were empirically adjusted. While a parameter of T = 40 (--tau2_fudge 40) proved well suited for all data sets, finding a suitable number of classes posed a challenge. Running multiple 3D classifications with different numbers of classes resulted in classes of various, related structural states with little overlap, that is, classes of different runs could not be matched as they did generally not superimpose. The same was true when rerunning a 3D classification job using the same settings but a different seed. These results suggest a continuous structural heterogeneity of myosin in contrast to several discrete states. While software tailored to the characterization of cryo-EM data exhibiting continuous structural states has recently been published (Zhong et al., 2021), it proved unsuitable for the processing of signal-subtracted actomyosin filaments due to the need of 3D masking. To characterize the structural heterogeneity of myosin-V by standard 3D classification in Relion 3.0.4 (Scheres, 2012) as good as possible, the number of 3D classes was optimized experimentally to yield the highest number of classes with a resolution and map quality sufficient for atomic modeling (≤3.7 Å). To do so, multiple 3D classifications with varying number of classes, for example, from 2 to 12, were performed and particles split into subsets according to the classification results. Subsets were then transferred to SPHIRE and individually subjected to a local 3D refinement from stack (no reference required, same settings as before). Eventually, each subset was post-refined and the resulting map manually assessed. In the end, the 3D classification that yielded the most maps of high quality was chosen. In this way, a total of 18 high-resolution maps (referred to as 3D class averages or 3D classes) were achieved for the four actomyosin data sets. Corresponding subsets contained 81,757 to 365,722 particles; see Table 2, Table 3, Table 4 and Table 6 for details. An overview of all refined maps, associated resolutions, and the underlying number of particles is given in Figure 1—figure supplement 1.

To ease the interpretation of maps as well as model building, all final maps, that is, central 3er/2er, central 1er, and 3D class averages, were additionally filtered to local resolution using SPHIRE 1.3 (Moriya et al., 2017) and denoized using LAFTER (Ramlaul et al., 2019).

### Model building, refinement, and validation

Previous cryo-EM structures of PHD-stabilized aged F-actin (PDB: 6T20; Pospich et al., 2020) and JASP-stabilized young F-actin (PDB: 5OOD; Merino et al., 2018) were used as starting models for F-actin in the rigor actomyosin complexes (aged and young rigor). The models of PHD and JASP were replaced by single-residue initial models generated from SMILES strings by elBOW (Moriarty et al., 2009) within Phenix (Adams et al., 2011) using the --amber option. The corresponding cif constraints libraries were used for all further refinements. A rigor-like crystal structure of the myosin-V-LC complex (PDB: 1OE9; Coureux et al., 2003) was used as an initial model for myosin and the bound light chain within the aged rigor structure. Stubs were replaced by full residues, and residues that are missing in the crystal structure, but are resolved in the cryo-EM density map, were added manually in Coot (Debreczeni and Emsley, 2012; Emsley et al., 2010). For all other models, that is, of the ADP, AppNHp, and young rigor state, the final refined model of the PHD-stabilized rigor actomyosin complex was used as a starting model. Initial models of nucleotides (ADP and AppNHp) are based on previous cryo-EM and crystal structures of myosin (PDB: 6C1D; Mentes et al., 2018; and PDB: 1MMN; Gulick et al., 1997). Starting models were rigid-body fitted into the density map using UCSF Chimera (Pettersen et al., 2004) and ligands were coarsely refined in Coot (Debreczeni and Emsley, 2012; Emsley et al., 2010) prior to model building.

Atomic models of the central actomyosin subunit, consisting of one F-actin, myosin, LC, and PHD/JASP molecule (central 1er), were refined using ISOLDE (Croll, 2018) within UCSF ChimeraX (Goddard et al., 2018). For this purpose, hydrogens were added to the starting model using the addh command in UCSF Chimera (Pettersen et al., 2004) and manually adjusted when necessary. Custom residue definitions for PHD and JASP were created based on the elBOW output within the ISOLDE shell. To reliably model both high- and medium-resolution features, several maps, for example, filtered to nominal or local resolution and sharpened by different B-factors, were loaded to ISOLDE. Maps filtered by LAFTER (Ramlaul et al., 2019) were also loaded for visual guidance, but excluded from the refinement (weight set to 0, MDFF deactivated). All density maps were segmented based on the starting model using the color zone tool within UCSF Chimera (Pettersen et al., 2004) to exclude density not corresponding to the central actomyosin subunit.

Each refinement in ISOLDE was started with a 2–3 min all atom simulation to reduce the overall energy of the system. Afterward, overlapping stretches of the protein and atoms within close vicinity were successively adjusted and refined. When necessary, rotamer and secondary structure restraints were introduced. After passing through the complete protein complex once, the quality of the model was assessed using the metrics provided by ISOLDE, that is, Ramachandran plot, rotamer outlier, and clash score, and outliers were locally addressed. Residues not resolved by the electron density map, for example, due to flexibility, were not included in the respective atomic model, while incompletely resolved side chains were set to most likely rotamers.

The density corresponding to the light chain was of insufficient quality for reliable model building. Hence, the model of the light chain was kept fixed during refinements in ISOLDE. Afterward, the reference crystal structure (PDB: 1OE9; Coureux et al., 2003) was rotamer-optimized in Coot and rigid-body fitted into the density using UCSF Chimera.

Finally, atomic models were real-space refined in Phenix (Adams et al., 2011; Afonine et al., 2018) against a sharpened density map filtered to nominal resolution (FSC0.143). To only relax and validate the model but prohibit large changes, local grid search, rotamer, and Ramachandran restraints were deactivated and the starting model was used as a reference. Furthermore, NCS and secondary structure restraints were applied and cif libraries provided for PHD and JASP.

Only models of the central actomyosin subunit (central 1er) were built in ISOLDE. Atomic models of subsets, that is, 3D class averages, were built starting from the average, all-particle model, and the corresponding ISOLDE/UCSF ChimeraX session including restraints. Whereas average models of different states, that is, rigor, ADP, and AppNHp, were built within new sessions to avoid any bias. Atomic models consisting of three actin and two myosin-LC subunits (central 3er/2er) were assembled from the models of the monomeric complex (central 1er) by rigid-body fitting in UCSF Chimera. The filament interface was manually inspected in Coot and side chain orientations adjusted when necessary. Finally, the multimeric model was real-space refinement in Phenix.

After real-space refinement, the residue assignment of PHD was changed from a single non-standard residue to a hepta-peptide consisting of TRP-EEP-ALA-DTH-CYS-HYP-ALA. All atomic models were assessed and validated using model-map agreement (FSC, CC), MolProbity (Chen et al., 2010), and EMRinger (Barad et al., 2015) statistics.

In total, 27 atomic models were built based on density maps with a resolution ranging from 2.9 Å to 3.7 Å; models include 4 central 1er and 5 central 3er/2er all-particle models as well as 18 models representing subsets identified by 3D classification (see Table 2, Table 3, Table 4 and Table 6 for details).

### Structural analysis and visualization

Figures and movies were created with UCSF Chimera (Pettersen et al., 2004) and modified using image or movie processing software when required.

For the visualization of myosin and the actomyosin interface, central 1er (central actomyosin subunit) and central 3er/2er (central three F-actin and two myosin molecules) models and maps are shown, respectively, as they include all important contact sites and are best resolved. Models protonated by H++ (Anandakrishnan et al., 2012) at pH 7.5 with HIC replaced by HIS were used for all surface representations. To optimally visualize features of different local resolution, a variety of maps are displayed within figures and movies (also see legends). Specifically, LAFTER maps are used to visualize the complete actomyosin structure and features of lower resolution, while post-refined maps are shown in close-up views, for example, of the active site.

Relative rotation angles of the lever arm were computed as angles between axes created for the corresponding helices in Chimera (Pettersen et al., 2004) using default settings.

Protein-protein and protein-ligand interactions were analyzed with PDBsum (Laskowski, 2009). Conformational changes and structural heterogeneity of the central 1er models were characterized by PCA using the Bio3d library (Grant et al., 2006) in R (R Core Team, 2017). Initially, model sequences were aligned using the pdbaln method. With the help of the methods core.find and pdbfit, models were then superimposed on an automatically determined structural stable core, which encompasses almost the complete F-actin subunit and parts of the HLH-motif in the L50 domain. PCA was performed running px.xray, excluding gaps within the sequence and ligands. Data points were manually grouped and colored based on the underlying data set and type of model, that is, average model vs. 3D class average. For the direct visualization of PCA results, trajectories along each principal component were exported using mktrj.pca and morphed in UCSF Chimera (Pettersen et al., 2004). Mobile domains within myosin (central 1er, chain A) and their motion were identified and analyzed using DynDom (Hayward and Lee, 2002).

### Data availability

The atomic models and cryo-EM maps are available in the PDB (Burley et al., 2019) and EMDB databases (Lawson et al., 2011) under the following accession numbers: aged PHD-stabilized actomyosin-V in the strong-ADP state: 7PM5, EMD-13521 (central 1er), 7PM6, EMD-13522 (central 3er/2er), 7PM7, EMD-13523 (class 2), 7PM8, EMD-13524 (class 3), 7PM9, EMD-13525 (class 4), 7PMA, EMD-13526 (class 5), 7PMB, EMD-13527 (class 6), 7PMC, EMD-13528 (class 7); aged PHD-stabilized actomyosin-V in the rigor state: 7PLT, EMD-13501 (central 1er), 7PLU, EMD-13502 (central 3er/2er), 7PLV, EMD-13503 (class 1), 7PLW, EMD-13504 (class 3) and 7PLX, EMD-13505 (class 4); aged PHD-stabilized actomyosin-V in the PRT state: 7PMD, EMD-13529 (central 1er), 7PME, EMD-13530 (central 3er/2er), 7PMF, EMD-13531 (class 1), 7PMG, EMD-13532 (class 3), 7PMH, EMD-13533 (class 4), 7PMI, EMD-13535 (class 5), 7PMJ, EMD-13536 (class 6), 7PML, EMD-13538 (class 8); young JASP-stabilized actomyosin-V in the rigor state: 7PLY, EMD-13506 (central 1er), 7PLZ, EMD-13507 (central 3er/2er), 7PM0, EMD-13508 (class 1), 7PM1, EMD-13509 (class 2), 7PM2, EMD-13510 (class 4); and young JASP-stabilized F-actin: 7PM3, EMD-13511. The data sets generated during the current study are available from the corresponding author upon reasonable request.
