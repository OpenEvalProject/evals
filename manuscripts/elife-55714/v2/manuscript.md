# A unified computational model for cortical post-synaptic plasticity

## Authors

- Tuomo Mäki-Marttunen<sup>1</sup> ([ORCID: 0000-0002-7082-2507](https://orcid.org/0000-0002-7082-2507)) †
- Nicolangelo Iannella<sup>2</sup>
- Andrew G Edwards<sup>1</sup>
- Gaute T Einevoll<sup>3</sup> ([ORCID: 0000-0002-5425-5012](https://orcid.org/0000-0002-5425-5012))
- Kim T Blackwell<sup>5</sup> ([ORCID: 0000-0003-4711-2344](https://orcid.org/0000-0003-4711-2344))

### Affiliations

1. Simula Research Laboratory Oslo Norway
2. Department of Biosciences, University of Oslo Oslo Norway
3. Faculty of Science and Technology, Norwegian University of Life Sciences Oslo Norway
4. Department of Physics, University of Oslo Oslo Norway
5. The Krasnow Institute for Advanced Study, George Mason University Fairfax United States

† Corresponding author

## Abstract

Signalling pathways leading to post-synaptic plasticity have been examined in many types of experimental studies, but a unified picture on how multiple biochemical pathways collectively shape neocortical plasticity is missing. We built a biochemically detailed model of post-synaptic plasticity describing CaMKII, PKA, and PKC pathways and their contribution to synaptic potentiation or depression. We developed a statistical AMPA-receptor-tetramer model, which permits the estimation of the AMPA-receptor-mediated maximal synaptic conductance based on numbers of GluR1s and GluR2s predicted by the biochemical signalling model. We show that our model reproduces neuromodulator-gated spike-timing-dependent plasticity as observed in the visual cortex and can be fit to data from many cortical areas, uncovering the biochemical contributions of the pathways pinpointed by the underlying experimental studies. Our model explains the dependence of different forms of plasticity on the availability of different proteins and can be used for the study of mental disorder-associated impairments of cortical plasticity.

## Introduction

Synaptic plasticity in the neocortex has been under intense research since the first observations of neocortical long-term potentiation (LTP) (Komatsu et al., 1981; Lee, 1982). Although most often studied in brain slices, synaptic plasticity in the neocortex is a key phenomenon underlying vital mammalian brain processes ranging from formation and storage of memories to attentional selection (Roelfsema and Holtmaat, 2018). These processes are impaired in heritable mental illnesses such as schizophrenia and fragile X syndrome, as well as neurodegenerative diseases such as Alzheimer’s disease, all of which have been associated with deficits in cortical plasticity (Kantrowitz et al., 2017; Martin and Huntsman, 2012; Koch et al., 2014). Improved understanding of neocortical synaptic plasticity all the way from molecular to circuit level is therefore needed to further our understanding of these yet incurable diseases.

Similar to hippocampal synaptic plasticity (Larkman and Jack, 1995), synaptic plasticity in the neocortex is highly variable — the outcomes of any plasticity-inducing protocol depends on the cortical area, neuron type as well as details of the stimulation protocol (Castro-Alamancos et al., 1995; Froc and Racine, 2005; Sjöström et al., 2008; Feldman, 2009). Computational models provide a tool for efficient hypothesis testing of mechanisms of neocortical plasticity, which helps to overcome the challenges posed by excessive variability. The foundations of our mechanistic understanding of neocortical synaptic plasticity lie upon the phenomenological Bienenstock-Cooper-Munro (BCM) theory, which predicts that small synaptic activity (later attributed to small Ca2+ transients [Bear et al., 1987; Lisman, 1989]) cause long-term depression (LTD) whereas large synaptic activity (large Ca2+ transients) give rise to LTP (Bienenstock et al., 1982). Simple BCM-based models and the closely related models of spike-timing-dependent plasticity (STDP) have been widely used to explain the emergence of input-specific cell assemblies mediating, e.g., orientation selectivity (Shouval et al., 1997) or memory traces (Klampfl and Maass, 2013) in the cortex. These models, however, typically fail to provide a mechanistic understanding of the biochemistry within the synapse — namely, they do not reveal how various molecules downstream of Ca2+ regulate the induction and maintenance of plasticity occurring in neuronal circuits, their composite neurons and synapses of the cortex. Moreover, current models often ignore the joint contributions of neuromodulators, which are critical for inducing some forms of cortical synaptic plasticity (Meunier et al., 2017; Brzosko et al., 2019). These shortcomings impede testing biochemical mechanisms of heritable mental illnesses associated with impaired cortical plasticity.

In this work, we aim at filling this gap of knowledge by introducing a biochemically detailed, mass-action law-based model of neocortical post-synaptic plasticity that can be used to study the induction of plasticity in different genetic conditions and neuromodulatory states, and under various stimulation protocols. Despite the lack of biochemically detailed models of synaptic plasticity in the neocortex, models of intracellular signalling have been used to study LTP and LTD in the hippocampus (Bhalla and Iyengar, 1999; Jȩdrzejewska-Szmek et al., 2017), cerebellum (Gallimore et al., 2018), and striatum (Blackwell et al., 2019). These models permit systematic studies on how patterns of Ca2+ inputs to the post-synaptic spine, either alone or in combination with neuromodulatory actions, activate different signalling pathways leading to post-synaptic plasticity in the form of, e.g., AMPA-receptor (AMPAR) phosphorylation and membrane insertion. We integrate quantitative descriptions of the intracellular signalling pathways underlying synaptic plasticity in the neocortex into a unified model that is capable of describing both stimulation protocol-dependent plasticity, as well as neocortically observed neuromodulator-gated forms of STDP. We show that our model can be tuned by alterations of protein expression to reproduce not only BCM-like forms of plasticity but also experimental observations on neocortical plasticity from various cortical areas. Our results help to quantify and explain the differences in molecular constituents of different forms of neocortical LTP and LTD, and the different, data-fitted versions of our model can be directly used to examine the effects of chemical inhibitors and genetic manipulations of signalling proteins on synaptic plasticity in different cortical cells.

## Results

### Model construction

We reviewed the literature of molecular signalling pathways that needed for neocortical LTP/LTD, in particular in the post-synaptic spine of pyramidal cells (Table 1A). Three main pathways were highlighted in the experimental studies, namely, the protein kinase A (PKA), protein kinase C (PKC), and Ca2+/calmodulin-dependent kinase II (CaMKII) pathways. To construct a computational model of cortical post-synaptic plasticity that describes these pathways, we adopted mass-action law-based descriptions of these pathways from biochemically detailed models of post-synaptic LTP/LTD in other brain areas, namely, hippocampus, basal ganglia and cerebellum (Table 1B). We prioritised the model components from hippocampal models due to the relatively small ontological differences between hippocampus and neocortex (Kirsch and Chechik, 2016). We focused on the effects of these pathways on AMPARs due to the better description of intracellular regulation of AMPAR dynamics in comparison to that of NMDA and kainate receptors or voltage-gated ion channels. In short, we based our model on that of Jȩdrzejewska-Szmek et al., 2017, which describes the PKA- and CaMKII-dependent phosphorylation of AMPAR subunit 1 (GluR1), and added the metabotropic glutamate receptor (mGluR) and muscarinic acetylcholine M1 receptor-mediated activation of PKC from Kim et al., 2013 and Blackwell et al., 2019, respectively. Other types of receptors that interact with these pathways, such as serotonin (5HT) and dopamine receptors (He et al., 2015), have been shown to underlie certain types of neocortical plasticity. Dopamine D1/D5 receptors as well as serotonin 5HT4, 5HT6 and 5HT7 receptors are coupled to Gs proteins whereas 5HT2 receptors are Gq-coupled. The effects of these neurotransmitters would therefore be similar to those of norepinephrine and acetylcholine in our model (depending on the receptor composition in the post-synaptic neuron), and thus they are omitted in the present work. We then adopted the reactions describing PKC-dependent phosphorylation and endocytosis of AMPAR subunit 2 (GluR2) and reinsertion to the membrane from Gallimore et al., 2018, which allowed the representation of post-synaptic depression with our model. The pathways included in the model are illustrated in Figure 1. A description of the model calibration is given in Materials and methods, section 'Construction and calibration of the biochemically detailed model of post-synaptic plasticity in the cortex', and the full set of model reactions and initial concentrations is provided in Tables 3 and 4, respectively.

**Table 1.**
 Pathways contributing to cortical synaptic plasticity.(A) Experimental evidence on the requirement of various molecular species for specific types of synaptic regulation in different cortical areas. (B) Model components needed for describing the modes of plasticity listed in (A). References are made to previous computational models describing these pathways. The types of phosphorylation of AMPAR subunit that mediate the plasticity are printed in bold.


<table>
  <thead>
    <tr>
      <th colspan="5">(A)</th>
    </tr>
    <tr>
      <th>Pathway components</th>
      <th>Type of neurons</th>
      <th>Type of regulation</th>
      <th>Pre-/post-synaptic</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CaMKII</td>
      <td>Cingulate cortex</td>
      <td>Esophageal acid-induced sensitisation</td>
      <td>post-syn.</td>
      <td>Banerjee et al., 2013</td>
    </tr>
    <tr>
      <td>CaMKII</td>
      <td>Prefrontal cortex, pyramidal neurons</td>
      <td>5-HT1-induced modulation of AMPA currents</td>
      <td>post-syn.</td>
      <td>Cai et al., 2002</td>
    </tr>
    <tr>
      <td>β-adr. receptors, PKA</td>
      <td>Visual cortex, layer 4 pyramidal cells</td>
      <td>Potentiation of AMPA currents</td>
      <td>post-syn.</td>
      <td>Seol et al., 2007</td>
    </tr>
    <tr>
      <td>M1 receptors, PKC</td>
      <td>Visual cortex, layer 4 pyramidal cells</td>
      <td>Depression of AMPA currents</td>
      <td>post-syn.</td>
      <td>Seol et al., 2007</td>
    </tr>
    <tr>
      <td>D1–PKA</td>
      <td>Prefrontal cortex, pyramidal neurons</td>
      <td>Potentiation of AMPA currents</td>
      <td>post-syn.</td>
      <td>Sun et al., 2005</td>
    </tr>
    <tr>
      <td>β-adr. receptors</td>
      <td>Frontal cortex</td>
      <td>Potentiation of field EPSPs</td>
      <td>n/a</td>
      <td>Sáez-Briones et al., 2015</td>
    </tr>
    <tr>
      <td>PKC</td>
      <td>Cultured cortical neurons</td>
      <td>Internalisation of AMPARs</td>
      <td>post-syn.</td>
      <td>Chung et al., 2000</td>
    </tr>
    <tr>
      <td>ERK</td>
      <td>Visual cortex</td>
      <td>Potentiation of field EPSPs</td>
      <td>n/a</td>
      <td>Di Cristo et al., 2001</td>
    </tr>
    <tr>
      <td colspan="5">(B)</td>
    </tr>
    <tr>
      <td>Molecular pathway</td>
      <td colspan="4">Cell type and references</td>
    </tr>
    <tr>
      <td>Ca2+ → CaM → CaMKII</td>
      <td colspan="4">Hippocampal CA1 neuron Bhalla and Iyengar, 1999; Jȩdrzejewska-Szmek et al., 2017, generic Hayer and Bhalla, 2005,</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">cerebellar Purkinje cells Gallimore et al., 2018, striatal spiny projection neuron Blackwell et al., 2019</td>
    </tr>
    <tr>
      <td>CaMKII → GluR1 S831p</td>
      <td colspan="4">Hippocampal CA1 neuron Jȩdrzejewska-Szmek et al., 2017</td>
    </tr>
    <tr>
      <td>β-adrenergic receptors → cAMP</td>
      <td colspan="4">Hippocampal CA1 neuron Jȩdrzejewska-Szmek et al., 2017</td>
    </tr>
    <tr>
      <td>cAMP → PKA</td>
      <td colspan="4">Hippocampal CA1 neuron Bhalla and Iyengar, 1999; Jȩdrzejewska-Szmek et al., 2017, cerebellar Purkinje</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">cells Gallimore et al., 2018</td>
    </tr>
    <tr>
      <td>PKA → GluR1 S845p</td>
      <td colspan="4">Hippocampal CA1 neuron Jȩdrzejewska-Szmek et al., 2017</td>
    </tr>
    <tr>
      <td>M1 receptors → PLC</td>
      <td colspan="4">Cerebellar Purkinje cells Gallimore et al., 2018</td>
    </tr>
    <tr>
      <td>PLC → PKC</td>
      <td colspan="4">Hippocampal CA1 neuron Bhalla and Iyengar, 1999, striatal spiny projection neuron</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">Kim et al., 2013; Blackwell et al., 2019</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">cerebellar Purkinje cells Kotaleski et al., 2002; Gallimore et al., 2018</td>
    </tr>
    <tr>
      <td>PKC → GluR2 S880p</td>
      <td colspan="4">Cerebellar Purkinje cells Gallimore et al., 2018</td>
    </tr>
  </tbody>
</table>

![Figure 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig1-v2.jpg)

**Figure 1.:** The PKA-pathway-related proteins and signalling molecules are highlighted by blue, PKC-pathway molecules by yellow, and CaMKII-pathway molecules by green colours. Reactions associated with a molecular species in parenthesis indicate a dependency on the denoted species — for details, see Table 3. Acronyms: β-AR – β-adrenergic receptor; AC1 and AC8 – adenylyl cyclase type 1 or 8; CaM – calmodulin; CaMKII – calmodulin-dependent protein kinase II; cAMP – cyclic adenosine monophosphate; DAG – diacylglycerol; Epac1 – exchange factor directly activated by cAMP 1; Gi, Gq and Gs – G-protein type I, Q, or S; GluR1 and GluR2 – AMPAR subunit 1 or 2; mGluR – metabotropic glutamate receptor; M1R – cholinergic receptor M1; NCX – Na+-Ca2+ exchanger; Ng – neurogranin; NMDAR – NMDA receptor; PDE1 and PDE4 – phosphodiesterase type 1 or 4; PIP2 – phosphatidylinositol 4;5-bisphosphate; PKA – protein kinase A; PKCt and PKCp – transiently or persistently active protein kinase C; PLC – phospholipase C; PMCA – plasma membrane Ca2+ ATPase; PP1 – protein phosphatase 1; PP2A – protein phosphatase 2A; PP2B – protein phosphatase 2B (calcineurin). In this work, the NMDARs are considered only in section 'Paired pre- and post-synaptic stimulation induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses': in the rest of the work, Ca2+ is directly injected as a square-pulse current into the spine.

### Ca2+ activates multiple pathways that regulate the post-synaptic plasticity in cortical PCs

All pathways of Table 1B are Ca2+-dependent, but due to the variability in binding rates and quantities of different Ca2+-binding molecules, some pathways become more easily activated than others. This permits LTP or LTD to be induced in a way that is sensitive to the amount of Ca2+ inputs and may serve as a basis for BCM-type rules of plasticity.

To examine the sensitivities of LTP- and LTD-inducing pathways to Ca2+, we simulated the injection of a prolonged square-pulse Ca2+ input of varying magnitude (illustrated in Figure 2A) into the post-synaptic spine and quantified the degree of activation of each of the Ca2+-binding molecules and the downstream signalling cascades. The simulations were carried out in the presence of mGluRs and $\beta$-adrenergic and cholinergic neuromodulation, which were modelled as prolonged square-pulse inputs as well.

![Figure 2.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig2-v2.jpg)

**Figure 2.:** (A) Illustration of the stimulus protocols with Ca2+ flux amplitudes 150 (green), 200 (cyan), and 250 (purple) particles/ms. (B–F) Time courses of Ca2+ (in nM) bound to buffers (B), pumps (C), PKC-pathway proteins (D), or CaM (E), and the concentration of free Ca2+ ions (F), according to NeuroRD (solid; averaged across eight samples) or NEURON (dashed) simulations. Colours indicate the Ca2+ flux used (see A). (B) Number of Ca2+ ions bound to Ca2+ buffers, that is immobile buffer and calbindin. (C) Number of Ca2+ ions bound to Ca2+ pumps and exchangers, that is PMCA and NCX. (D) Number of Ca2+ ions bound to PKC-pathway proteins PLC and PLA2. (E) Number of Ca2+ ions bound to CaM, in all its forms. (F) Cytosolic Ca2+ concentration (mM) (G) Degrees of activation of different Ca2+-binding proteins in a steady state (5 min after onset of Ca2+ input) as a function of the magnitude of Ca2+ flux. The x-axis shows the amplitude of the Ca2+ input (see panel A), and the y-axis shows the ratio of the underlying species in a Ca2+-bound form over the total number of the proteins. For CaM, only the CaM molecules bound by four Ca2+ ions are considered activated — in PLC, PLA2, and DGL, binding of only one Ca2+ ion is needed for activation. Here, the measured quantity of active PLC includes both Gq-bound and non-Gq-bound CaPLC. Inset: zoomed-in view on the red area. (H) Ratio of the steady-state concentration of PKA catalytic subunit over the theoretical maximum where all PKA molecules were dissociated into residuals and catalytic subunits. Colour of the curve indicates the amplitude of the β-adrenergic ligand flux (particles/ms). (I) Fraction of phosphorylated CaMKII subunits. (J) Fraction of (transiently or persistently) activated PKC. Colour of the curve indicates the amplitude of the cholinergic and glutamatergic ligand flux (particles/ms). The grey area in panels (G–J) represents Ca2+ inputs that cause cytosolic Ca2+ concentration to reach extremely high levels (>1 mM) that are likely to lead to apoptosis.

The injected Ca2+ quickly bound to Ca2+ buffers (immobile buffer and calbindin, Figure 2B) and pumps (PMCA and NCX, Figure 2C) as well as to the proteins of the PKC pathway (phospholipase A2 (PLA2) and C (PLC), Figure 2D): a 95% saturation was reached in 1–2 s (Figure 2B–D). In contrast, the activation of calmodulin (CaM) was slower (Figure 2E): a 95% saturation was reached in 32–53 s, depending on the magnitude of the Ca2+ input. Consistent with experimental literature, a vast majority of Ca2+ was quickly bound and only a small fraction remained free in the cytosol (Figure 2F).

To further illustrate the differences between the activation patterns of these pathways, we quantified the degrees of Ca2+ binding of these molecules in a steady state (5 min after the onset of Ca2+) and the overall activation/deactivation of downstream molecules as a function of the magnitude of the Ca2+ injection. Both PKC pathway-mediating proteins PLC, diacylglycerol lipase (DGL), and PLA2, along with the PKA and CaMKII pathway-related protein CaM became completely activated if large enough Ca2+ flux is given, but their degrees of activity varied across the magnitude of the injected Ca2+ flux (Figure 2G). DGL was most completely activated throughout the Ca2+ amplitude, owing to the large equilibrium constant of its Ca2+ binding. At extremely large Ca2+ fluxes, CaM was more completely bound by Ca2+ than PLC and PLA2 (Figure 2G), but at lower Ca2+ amplitudes, CaM remained largely unbound (Figure 2G inset). This is reflected in the activation patterns of the catalytic subunit of PKA (Figure 2H) and CaMKII (Figure 2I), both of which are dependent on the activation of CaM and thus had a small response at low Ca2+ amplitudes. PKC, by contrast, became activated at relatively small Ca2+ amplitudes (Figure 2J). Of these three pathways, the PKC pathway was dependent on the cholinergic ligands or the activation of the mGluRs (Figure 2J), and the PKA pathway was dependent on the availability of β-adrenergic ligands (Figure 2H). Taken together, these results highlight the need for large Ca2+ flux to the post-synaptic spine for the activation of the CaMKII pathway, relatively large Ca2+ flux for the activation of the PKA pathway, and relatively small Ca2+ flux for the activation of the PKC pathway.

### High-frequency stimulation (HFS) causes LTP and low-frequency stimulation (LFS) causes LTD in GluR1-GluR2-balanced synapses

The Ca2+ flux entering the post-synaptic spine is extremely large during and after synaptic transmission and low otherwise, which causes the signalling pathways to be activated and deactivated in a more dynamic way than described in the previous section ('Ca2+ activates multiple pathways that regulate the post-synaptic plasticity in cortical PCs'). The activation of these pathways and their dependence on the stimulus protocol are difficult to study experimentally due to methodological constraints (e.g., side effects of fluorescence indicators, lack of signal calibration, and poor temporal or spatial resolution), but biochemically detailed models, such as the one considered in this work, can provide insights into the transient molecular mechanisms behind LTP and LTD. Our model is particularly well suited to study the mechanisms behind CaMKII-, PKA- and PKC-mediated phosphorylation of AMPAR subunits, which are important mediators of long-term plasticity (Wang et al., 2005). Phosphorylation of GluR1 subunits at S845 increases the insertion rate of the AMPAR into the membrane, thus leading to post-synaptic LTP (Diering et al., 2016). Conversely, phosphorylation of GluR2 subunits at S880 increases the rate of receptor endocytosis from the membrane, and has thus been observed to lead to post-synaptic LTD (Xia et al., 2000). However, it is not the number of the membrane-expressed AMPAR subunits alone that determine the strength of the synapse, but different compositions of the subunits have different single-channel conductances, and phosphorylation at S831 of the GluR1 subunit also affects the conductance of the channel (Oh and Derkach, 2005).

To simulate the reaction dynamics in the post-synaptic spine under realistic input patterns, we applied the 4xHFS and LFS protocols. Each input contained transient (3 ms) influxes of Ca2+ (1900 particles/ms) into the cytosol and glutamate (20 particles/ms), acetylcholine (20 particles/ms) and β-adrenergic ligand (10 particles/ms) into the extracellular subspace near the spine membrane. We used a balanced ratio (1:1) of GluR1 and GluR2 subunits. We recorded the time courses of the concentrations of all CaMKII-, PKA-, and PKC-pathway molecules contributing to LTP or LTD to monitor their activity during and following the stimulation protocols. We also recorded the numbers of membrane-inserted GluR1 and GluR2 and their state of phosphorylation and used Equation 5 for determining the maximal synaptic conductance.

In the 4xHFS protocol, which typically causes LTP in plasticity experiments, our model predicts a large increase in total synaptic conductance (Figure 3A) due to a radical increase in membrane-inserted GluR1 subunits (Figure 3B) and a decrease in GluR2 subunits (Figure 3C). These changes in membrane-expression of AMPAR subunits were dependent on activations of many signalling proteins in the CaMKII (Figure 3D–H), PKA (Figure 3I–M), and PKC (Figure 3N–R) pathways. First, the Ca2+ entry (Figure 3D) caused a rapid increase in half-activated calmodulin (bound by two Ca2+ ions; Figure 3E), leading to a longer-lasting increase in active calmodulin (Figure 3F). Calmodulin activation led to an increase in the concentration of phosphorylated CaMKII (Figure 3G), which phosphorylated the GluR1-type receptors at S831 (Figure 3H). The β-adrenergic input (Figure 3I), in turn, bound to the β-adrenergic receptors and activated the Gs proteins (Figure 3J), which bound to the adenylyl cyclase AC1 to produce cyclic adenosine monophosphate (cAMP, Figure 3K). cAMP bound to PKA to release the catalytic subunits of PKA (Figure 3L), which led to a phosphorylation of the GluR1-type receptors at S845 (Figure 3M) and thus to increased membrane expression of GluR1 subunits and total synaptic conductance (Figure 3A–B). Due to the simultaneous activation of the CaMKII pathway, a significant proportion of double phosphorylated GluR1-type receptors was observed (Figure 3H,M). As for the PLC–PKC pathway, glutamate (Figure 3N, blue) bound to mGluRs and acetylcholine (Figure 3N, green) bound to muscarinic receptors (M1), and the activation of these receptors contributed to the activation of Gq proteins (Figure 3O). The activated Gq proteins bound with PLC and metabolised phosphatidylinositol 4,5-bisphosphate (Pip2) into diacylglycerol (DAG, Figure 3P), which activated PKC (Figure 3Q). This led to the phosphorylation of GluR2-type receptors at S880 (Figure 3R), which caused the decrease in membrane expression of GluR2 observed in Figure 3C.

![Figure 3.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig3-v2.jpg)

**Figure 3.:** (A) Total synaptic conductance in response to 4xHFS, determined by the numbers of membrane-inserted GluR1s and GluR2s — see Equation 5. The stimulation starts at 40 s and lasts until 53 s. (B–C) Concentration of membrane-inserted GluR1s (B) and GluR2s (C) in response to 4xHFS. (D–H) Concentration of different species in the CaMKII pathway, namely, intracellular unbound Ca2+ (D), CaM bound with two Ca2+ ions (E), CaM bound with four Ca2+ ions (active CaM; F), phosphorylated CaMKII, bound or unbound by CaMCa4 (G), and S831-phosphorylated and double-phosphorylated GluR1 subunits (H) in response to 4xHFS. (I–M) Concentration of different species in the cAMP-PKA pathway, namely, β-adrenergic ligand in all its forms (I), activated (GTP-bound but not bound to ATP) Gs and Gi proteins (J), intracellular cAMP (K), catalytic subunit of PKA (L), and S845-phosphorylated and double-phosphorylated GluR1 subunits (M) in response to 4xHFS. (N–R) Concentration of different species in the PLC-PKC pathway, namely, glutamate and acetylcholine in all their forms (N), activated (GTP-bound but not bound to DAG) Gq proteins (O), intracellular DAG (P), activated PKC (Q), and S880-phosphorylated GluR2 subunits (R) in response to 4xHFS. S: Total synaptic conductance in response to LFS. (T–U) Concentration of membrane-inserted GluR1s (T) and GluR2s (U) in response to LFS, which starts at 40 s and lasts until 220 s. The solid lines represent stochastic (NeuroRD) simulation results, while the dashed lines represent data from deterministic (NEURON RxD) simulations. β-adrenergic ligands, glutamate, and acetylcholine are measured in numbers of particles as they reside both at the membrane (when bound to receptors) and at the extracellular subspace near the spine membrane (when unbound); other species measured in concentration.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) When GluR1 subunits are absent, 4xHFS induces LTD instead of LTP. (B) When GluR2 subunits are absent, LFS does not lead to changes in synaptic conductance. (C) When GluR1 subunits are absent, the paired-stimulus protocol induces acetylcholine-mediated LTD but not β-adrenergic ligand-mediated pairing interval-dependent LTP. (D) When GluR2 subunits are absent, the paired-stimulus protocol induces β-adrenergic ligand-mediated pairing interval-dependent LTP, but not acetylcholine-dependent LTD. (A–B) The y-axis shows the total synaptic conductance, and the x-axis shows the time. The 4xHFS stimulation lasts from 40 to 53 s, and the LFS stimulation from 40 to 220 s. See Figure 3 for details. (C–D) The y-axis shows the relative synaptic conductance, and the x-axis shows the inter-stimulus interval (ISI). See Figure 5 for details.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Plasticity induced by HFS and LFS. The y-axis shows the total synaptic conductance, and the x-axis shows the time. The 4xHFS stimulation lasts from 40 to 53 s, and the LFS stimulation from 40 to 220 s. See Figure 3 for details. (B) Plasticity induced by pairing protocol in the presence of various neuromodulators. The y-axis shows the relative synaptic conductance, and the x-axis shows the inter-stimulus interval (ISI). See Figure 5 for details. In all these experiments, a dimers-of-like-dimers rule of tetramer formation was used. 35% of the GluR subunits were GluR1 type and 65% GluR2.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The 6xHFSt protocol lasts from 0 to 60 s, while the LFS-1Hz protocol lasts from 0 to 1800s (data shown until 500 s). See Materials and methods, section 'Modelling the Ca2+ inputs and neuromodulatory inputs' for details on the stimulation protocols and the multicompartmental neuron model. All initial concentrations of the biochemical model were the same as in Figure 3.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** In the control case, the pre-synaptic input-associated fluxes of β-adrenergic and cholinergic ligands were 10 and 20 particles/ms, respectively, and the duration of each pulse was 3 ms. Here, the ligand inputs were made four times steeper by reducing the duration to 0.75 ms and the increasing the amplitudes to 40 (β-adrenergic) and 80 (cholinergic) particles/ms (blue), or 3.2 times less steep by increasing the duration to 9.6 ms and reducing the amplitudes to 3.125 (β-adrenergic) and 6.25 (cholinergic) particles/ms (green). Both alterations gave LTP and LTD responses that were indistinguishable from those of the control case. The red dashed line shows the LTP and LTD responses where the pre-synaptic input-associated fluxes of β-adrenergic and cholinergic ligands were replaced by a 10 min pulses of amplitudes 0.4 (β-adrenergic) and 0.8 (cholinergic) particles/ms, respectively, initiated 6 min prior to the pre-synaptic inputs to mimic the bath application of corresponding agents.

The differences between NEURON and NeuroRD simulation results in Figure 3M were due to the stochasticity in NeuroRD simulator — both smaller and larger GluR1 phosphorylation levels compared to NEURON simulation results (Figure 3M, dashed) were obtained when NeuroRD simulations were run with different random number seeds (not shown).

In the LFS protocol, which typically causes LTD in the experiments, our model predicts a prominent (20%) decrease in total synaptic conductance (Figure 3S) due to a decrease in GluR2 subunits. In this protocol, the Ca2+ inputs are insufficiently large to activate CaM, and the Gs proteins remain deactivated as well (data not shown). In consequence, CaMKII and PKA pathways remain deactivated, and the effect of the LFS protocol on GluR1 phosphorylation and membrane insertion is small (Figure 3T). By contrast, the PKC pathway is almost as strongly activated as in the 4xHFS protocol (data not shown), leading to prominent S880 phosphorylation of GluR2 (data not shown) and removal of GluR2 from the membrane (Figure 3U).

The expression of both LFS-induced LTD and 4xHFS-induced LTP of these types is dependent on the presence of both GluR1 and GluR2 subunits: GluR1-deficient synapses failed to show 4xHFS-induced LTP (Figure 3—figure supplement 1A) and GluR2-deficient synapses failed to show LFS-induced LTD (Figure 3—figure supplement 1B). To show that our results were not an artefact of the tetramer formation rule (Equation 1–5), we applied an alternative tetramer formation rule where GluR1 and GluR2 subunits randomly dimerised and the dimers paired with like dimers (which disallows the emergence of heterotetramers with 1:3 or 3:1 proportion of GluR1:GluR2 subunits; Gan et al., 2015). We reproduced the LFS-induced LTD and 4xHFS-induced LTP using this dimer-of-like-dimers rule with a modified (35:65) balance of GluR1 vs. GluR2 subunits (Figure 3—figure supplement 2A).

In the above analyses, we used brief square-pulse fluxes of Ca2+to the synapse model, which is a simple representation of inputs during synaptic plasticity induction protocols. Alternatively, Ca2+ current entering the post-synaptic spines can be estimated by using multicompartmental biophysically detailed neuron models. We simulated a model of layer 2/3 pyramidal cell, stimulated with synaptic inputs from a 6xHFSt or LFS-1Hz protocol (see Materials and methods, section 'Modelling the Ca2+ inputs and neuromodulatory inputs'), to determine the Ca2+ inputs entering the post-synaptic spine through NMDA receptors (NMDARs). In accordance with Figure 3 and experimental data from somatosensory cortex (Heusler et al., 2000), our model predicted that 6xHFSt induced LTP whereas LFS-1Hz induced LTD (Figure 3—figure supplement 3). Here, the 6xHFSt protocol was used instead of 4xHFS to model the same protocol as in Heusler et al., 2000; our model would also predict an LTP for 4xHFS (data not shown). The HFS-induced LTP and LFS-induced LTD of Figure 3 could also be reproduced with alternative durations of neuromodulator inputs, including 10 min bath applications (Figure 3—figure supplement 4). These results indicate that our model can reproduce HFS-induced LTP and LFS-induced LTD also when using realistic NMDAR-conducted Ca2+ transients and that these forms of plasticity are robust to the temporal profile of the neuromodulatory inputs.

The activations of the above pathways are dependent on the magnitude and dynamics of the inputs to the model, namely, Ca2+, β-adrenergic and cholinergic ligands, and glutamate. All pathways leading to GluR1 and GluR2 phosphorylation and the consequent exocytosis and endocytosis are Ca2+-dependent: blocking Ca2+ entry completely abolished 4xHFS-induced LTP (Figure 4A) that followed GluR1 insertion (Figure 4B) and GluR2 endocytosis (Figure 4C). Blocking β-adrenergic ligands abolished the 4xHFS-induced LTP (Figure 4A) by suppressing the membrane-insertion of GluR1 (Figure 4B), but had no effect on GluR2 endocytosis (Figure 4C). Likewise, blocking β-adrenergic ligands had no effect on LFS-induced LTD (not shown). In contrast, LFS-induced LTD (Figure 4E) that followed GluR2 endocytosis (Figure 4G) was reduced by blockade of mGluR activation while the number of GluR1 subunits at the membrane remained unaffected (Figure 4F). This reduction was strengthened by simultaneous blockade of cholinergic inputs (Figure 4E–G, yellow traces). Counterintuitively, blocking mGluR and M1-receptor activation also reduced the amplitude of the 4xHFS-induced LTP (Figure 4A) by disabling GluR2 endocytosis (Figure 4C) while it had no effect on GluR1 insertion (Figure 4B). The reason for this is that in the PKC pathway-blocked case there is a smaller post-4xHFS membrane-bound GluR1 ratio (fraction of GluR1 subunits over all GluR subunits at the membrane) than in the control case, and thus the probability of AMPARs being homomeric GluR1 tetramers (which had a very large conductance compared to other tetramers; Equation 5) is much smaller in the former case than in control (Figure 4D). Although qualitatively similar difference can be observed in post-LFS membrane-bound GluR1 ratios between PKC pathway-blocked case and control, the probability of homomeric GluR1 tetramers and their contribution to the synaptic conductance are very small in both cases (Figure 4H) and thus the LFS-induced LTD is not affected.

![Figure 4.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig4-v2.jpg)

**Figure 4.:** (A–D) 4xHFS-induced LTP in the control case (dark purple), without Ca2+ inputs (blue), without β-adrenergic ligands (green), and under blockade of PKC pathway-activation (mGluRs or cholinergic receptors; yellow). (E–H) LFS-induced LTD in the control case (dark purple), under the blockade of mGluR activation (blue), and under blockade of both mGluRs or cholinergic receptors (yellow). (A, E) Total synaptic conductance. (B, F) Membrane expression of GluR1. (C, G) Membrane expression of GluR2. (D, H) The fraction of membrane-inserted GluR1 over all membrane-inserted GluR subunits (left), the probability of an AMPAR tetramer being homomeric GluR1 (middle), and the relative contribution of homomeric GluR1 subunits to the total conductance (i.e., summed conductance of homomeric GluR1 tetramers divided by the summed conductance of all tetramers; right). The bars represent the values at the end of the 4xHFS (D) or LFS (H) simulation with (dark purple) and without (yellow) PLC-activating ligands.

Taken together, our results show that cortical synapses expressing both GluR1 and GluR2 subunits can express a frequency-dependent form of post-synaptic plasticity (LTP for high-frequency inputs, LTD for low-frequency inputs) that is gated by neuromodulators affecting the PKA and PKC pathways. Our findings also lend support to that GluR2 endocytosis may lead to either potentiation (Figure 4A) or depression (Figure 4E), depending on the prevalence of the GluR1 subunits at the membrane.

### Paired pre- and post-synaptic stimulation induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses

Cortical synapses typically exhibit a type of synaptic plasticity, namely STDP, that is dependent on both the pre- and post-synaptic activity. According to a classical model, the differences in the outcome of STDP for different pairing intervals of pre- and post-synaptic stimulus are explained by different amount of Ca2+ entering the post-synaptic spine, which is affected by both the pre-synaptically released glutamate and the elevation of post-synaptic membrane potential. Biophysically detailed neuron modelling offers a powerful tool for determining the size of these Ca2+ inputs as a function of the pairing interval.

We considered the LTP/LTD response to paired stimulation protocol using a multicompartmental model of a layer 2/3 pyramidal cell (Figure 5A; Markram et al., 2015). We placed a synaptic spine with volume 0.5 μm3 at a random location on the apical dendrite, 250–300 μm from the soma (Figure 5A, thick, black branches), and stimulated the head of the spine with glutamatergic synaptic currents (Hay and Segev, 2015; Markram et al., 2015; Figure 5A, black traces, top). In parallel, we stimulated the soma with a burst of four short (2 ms) supra-threshold square-pulse currents (Figure 5A, black traces, bottom). Given that approximately 10% of the NMDAR-mediated currents and none of the AMPAR-mediated currents are conducted by Ca2+ flux, we could determine the number of Ca2+ ions entering the spine at each time instant following the onset of the synaptic input (Figure 5A, grey traces). This experiment was repeated using different inter-stimulus intervals (ISI) between the synaptic and somatic stimuli and averaged across $N_{samp}=200$ trials. The membrane potential dynamics at the post-synaptic spine depended on the ISI (Figure 5B–D), largest effects response being obtained with near-coincident stimuli (Figure 5C). The higher the membrane potential at the spine, the higher the value of the variable describing the Mg2+-gate opening in the NMDA receptor (Figure 5B–D, insets) (Hay and Segev, 2015; Markram et al., 2015). Thus, the Ca2+ flux time course varied across the pairing ISIs (Figure 5—figure supplement 1). These Ca2+ flux time series were imported into our biochemical model (Ca2+ transients in the spine model showed in Figure 5E–G), which allowed us to predict the magnitude of GluR subunit phosphorylation and membrane insertion for each pairing interval. When added as bath application, the β-adrenergic and cholinergic ligands were simulated by prolonged injections of 50 particles/s for 10 min, starting 8 min before the STDP protocol — these neuromodulators alone (without the electric stimulation-mediated Ca2+ inputs) did not cause synaptic plasticity. Throughout the experiments, the activation of mGluRs was blocked.

![Figure 5.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig5-v2.jpg)

**Figure 5.:** (A) Layer 2/3 pyramidal cell morphology (grey, thin), locations of synaptic input highlighted (black, thick). Inset: Illustration of the inputs (black) and the recorded synaptic intracellular Ca2+ (grey). Scale bar 200 μm. (B–D) Membrane potential at the dendritic spine when the pre-synaptic stimulation onset is 50 ms after (B), at the same time as (C), or 50 ms prior to (D) the onset of the last somatic stimulus. Inset (red): Mg2+-gate variable as a function of time, ranging from −80 ms to 140 ms in a similar manner as the data in the main panel. (E–G) Concentration of free Ca2+ in the dendritic spine according to the biochemical spine model when the pre-synaptic stimulation onset is 50 ms after (B), at the same time as (C), or 50 ms prior to (D) the onset of the last somatic stimulus. (H–J) No LTD was induced by the stimulation protocol (1 Hz paired with post-synaptic stimulation for 2 min) in the absence of M1-receptor activation, but pairing-interval-dependent LTP was induced in presence of β-adrenergic inputs. (K–M) Pairing-interval-dependent LTD was induced when the synaptic input was coupled with cholinergic inputs, and STDP was induced when both cholinergic and β-adrenergic inputs were present. (H, K) Relative concentration of GluR1 at the membrane 16 min after the stimulation onset (normalised by concentration of membrane-inserted GluR1 at rest). (I, L) Relative concentration of GluR2 at the membrane 16 min after the stimulation onset (normalised by concentration of membrane-inserted GluR2 at rest). (J, M) Relative synaptic conductance (Equation 5) 16 min after the stimulation onset (normalised by synaptic conductance at rest).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A–D) The Ca2+ flux time course during the pairing protocol (from 100 ms before to 900 ms after the pre-synaptic stimulus) entering the post-synaptic spine through NMDA receptors when the onset of the last of the four post-synaptic stimuli is 50 ms before (A), coincident with (B), 50 ms after (C), or 150 ms after (D) the onset of the pre-synaptic stimulus. (E) Peak Ca2+ flux (from the data of panels A–D) for different ISIs. (F) Average Ca2+ flux (averaged across the time points of panels A–D, i.e., −100 to 900 ms) for different ISIs.

We first confirmed that the membrane expression of the glutamate receptors was not strongly affected by paired synaptic and somatic stimulation in the absence of β-adrenergic (which activates the PKA pathway) and cholinergic (which activates the PKC pathway) neuromodulation. Our model predicted that there is little change in the membrane expression of GluR1 and GluR2 type receptor subunits in this stimulation protocol (Figure 5H–I, purple). Consequently, our model reproduced the observation (Seol et al., 2007) that this stimulation protocol led to little change in predicted synaptic conductance (Figure 5J, purple).

We next considered the paired synaptic-somatic stimulation in the presence of β-adrenergic ligand. Our model predicted a prominent (up to 70%) increase in GluR1 membrane expression with little effect on GluR2 membrane expression (Figure 5H–I, blue). The predicted increase in GluR1 membrane expression (Figure 5H) and the consequent increase in synaptic conductance (Figure 5J, blue) were most prominent when the ISI was around 20–80 ms, and modest for large ISIs. These predictions are consistent with the experiments where an ISI-dependent potentiation of the EPSCs in the presence of β-adrenergic receptor agonists and absence of cholinergic agonists was observed (Seol et al., 2007).

When β-adrenergic neurotransmission was blocked but M1 receptors were activated by cholinergic ligands, the model predicted a prominent (up to 60%) decrease in GluR2 membrane expression, with little effect on GluR1 membrane expression (Figure 5K–L, purple). Our model of synaptic conductance (Equation 5) predicted a decrease in total conductance in a GluR1-GluR2-balanced synapse for this condition (Figure 5M, purple), which is in line with the experimental data (Seol et al., 2007). The depression takes place throughout the tested ISIs, but the effect was smallest for ISIs very close to zero due to the counteracting effects of GluR1 membrane-insertion (Figure 5K, purple). Finally, when both β-adrenergic and cholinergic neurotransmission were active, our model predicted an increased GluR1 membrane expression and decreased GluR2 membrane expression, both of which were ISI dependent (Figure 5K–L, blue). In these simulations, the predicted synaptic conductance was increased for small and moderate pre-post intervals and decreased otherwise (Figure 5M, blue), which is qualitatively similar to experimental data (Seol et al., 2007). These results are dependent on the availability of both GluR1 and GluR2 subunits at the post-synaptic spine: in simulations where GluR1 or GluR2 subunits were absent, only LTD (Figure 3—figure supplement 1C) or LTP (Figure 3—figure supplement 1D), respectively, was induced by the STDP protocol. In a similar manner as the HFS- and LFS-induced plasticity in Figure 3—figure supplement 2A, we could reproduce the STDP using the dimer-of-like-dimers tetramer formation rule with a GluR1 fraction of 35% (Figure 3—figure supplement 2B). Taken together, our model with balanced numbers of GluR1 and GluR2 subunits reproduces the neuromodulator-gated STDP observed in layer 2/3 pyramidal cells of the visual cortex.

The combination of our biochemically detailed model with the biophysically detailed model of layer 2/3 pyramidal cell model provides a compelling means of hypothesis testing for cortical STDP in this cell type. We analyzed how the shape of the STDP curve of Figure 5M is affected by the number of spikes in each post-synaptic burst stimulus. Our simulations suggest that decreasing the number of spikes per burst decreases the amplitude of both LTP and LTD in the STDP protocol and, in particular, brings the LTD for large post-pre ISIs close to zero (Figure 6A). These alterations are mediated by changes in both the level of membrane-insertion of GluR1 and endocytosis of GluR2 subunits (Figure 6A, insets). For small and moderate pre-post ISIs, the effects of decreasing the number of post-synaptic stimuli on the STDP curve are expected: both GluR1 insertion and GluR2 endocytosis are of smaller amplitude, and hence the dampened LTP amplitude (Figure 6A). By contrast, for post-pre ISIs and large pre-post ISIs, decreasing the number of post-synaptic stimuli results in larger amplitude of GluR1 insertion and GluR2 endocytosis, which yields a dampened LTD for post-pre ISIs and strengthened LTP for large pre-post ISIs (Figure 6A). These counter-intuitive effects can be explained by the accumulation of small-conductance K+ (SK) conductance in the post-synaptic neuron: the larger the number of post-synaptic pulses in the pairing burst, the larger the SK currents (Figure 6B). The SK current decays slowly (matching the Ca2+ concentration decay), and remnants of the SK currents can be observed as long as 200 ms after the post-synaptic stimulus (Figure 6B inset). For large post-pre ISIs, the number of spikes per burst has little effect on the Ca2+ transients during the post-synaptic stimulation (Figure 6C inset), but the SK currents activated by a large number of spikes per burst contribute to significantly decrease the Ca2+ transient caused by the pre-synaptic stimulus during the decay period (Figure 6C). By contrast, for small pre-post intervals, the additional spikes in the post-synaptic stimulus significantly contribute to the Ca2+ transients (Figure 6D). To show that the effects of the number of spikes per post-synaptic burst are mediated by the SK current, we ran the simulation of Figure 5J using a partial to complete blockage of the SK currents in the biophysically detailed simulations of the layer 2/3 pyramidal cell. The paired-pulse protocol of Figure 5M (involving both β-adrenergic and cholinergic neuromodulation) caused an STDP in all cases, but decreasing the SK conductance shortened the post-pre LTD window and decreased the amplitude of LTD (Figure 6E). Similar effects were obtained with a decrease of Ca2+-channel conductances (not shown), which is in agreement with the data of Nevian and Sakmann, 2006. Our model predictions also agree with the observation that the plasticity outcome is not determined by Ca2+ transient amplitude (Nevian and Sakmann, 2006), instead, our model suggests that the total Ca2+ is a better predictor of the plasticity outcome: the correlation coefficient between the post-STDP synaptic conductance and the peak Ca2+ transient amplitude (see Figure 5—figure supplement 1E) was 0.53, while that between the post-STDP synaptic conductance and the mean Ca2+ input during the inter-stimulus interval (see Figure 5—figure supplement 1F) was 0.96 (Figure 6—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig6-v2.jpg)

**Figure 6.:** (A) The STDP curves of Figure 5M when the number of spikes per post-synaptic burst was 1 (yellow), 2 (green), 3 (blue), or 4 (as in Figure 5; dark purple). Inset: relative concentrations of membrane-inserted GluR1 (top) or GluR2 (bottom) subunits — see Figure 5K–L for reference. (B) Top: somatic membrane potential time course (aligned according to the onset of the first stimulus) for different numbers of post-synaptic stimulus pulses. Bottom: somatic SK current-density time course in the four conditions. Inset: the SK current densities 200 ms after the onset of the first post-synaptic stimulus. (C–D) Ca2+ flux to the dendritic spine when the pre-synaptic stimulation onset is 200 ms after (C) or 30 ms before (D) the onset of the last post-synaptic stimulus. (E) The STDP curves of Figure 5M when the number of spikes per post-synaptic burst was four but the somatic SK conductance parameter was either normal (dark purple), 50% smaller (magenta), or 80% smaller (pink).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The y-axis shows the post-STDP synaptic conductance (in presence of β-adrenergic and cholinergic neuromodulation) relative to baseline as in Figure 5M. (A) The x-axis shows the peak Ca2+ input (in particles/ms) for different ISIs (see Figure 5D–F and Figure 5—figure supplement 1E). (B) The x-axis shows the time integral of Ca2+ input of Figure 5D–F from −500 to 500 ms, normalized by 1000 ms (see Figure 5—figure supplement 1F). Different colours represent different ISIs between −200 and 200 ms (intervals 0,±10,±20, and ±50 labeled for reference). The blue dashed line shows the linear regression, and the blue text shows the corresponding Pearson correlation coefficient.

### The model predicts multimodal, protein concentration- and neuromodulation-dependent rules of plasticity

Cortical neurons express a variety of forms of LTP/LTD depending on the brain region and cell type. In computational studies, neocortical plasticity is most typically described by simple rules according to which small-amplitude Ca2+ inputs lead to depression of the synapse whereas large-amplitude inputs lead to potentiation. Apart from a few examples Castellani et al., 2001; d’D'Alcantara et al., 2003; Castellani et al., 2005; Honda et al., 2013, these models typically do not describe the intracellular signalling machinery leading to the resulting plasticity Holthoff et al., 2002; Karmarkar et al., 2002; Badoual et al., 2006; Cornelisse et al., 2007; Kubota and Kitajima, 2008; Urakubo et al., 2008. Unlike biochemically detailed models, the simple models cannot be used to explore whether and how the prevalence of different plasticity-related proteins gives rise to various types of LTP/LTD or their impairments, which is an important question in the study of mental disorders with deficits in cortical plasticity. Here, we analysed the biochemical underpinnings of different types of plasticity rules using our unified model of cortical plasticity in order to predict the conditions for different forms of plasticity.

In a similar fashion to section 'Ca2+ activates multiple pathways that regulate the post-synaptic plasticity in cortical PCs', we simulated our model of the post-synaptic spine when stimulated with a prolonged (5 min) square-pulse influx of Ca2+ and neuromodulators. We randomly altered the model parameters controlling the initial concentrations of different proteins, namely, the ratio of GluR1 to all GluR subunits (i.e., $\frac{[GluR1]_{total}}{[GluR1]_{total}+[GluR2]_{total}}$, from here on referred to as GluR1 ratio), the concentration of NCX (regulating the rate of Ca2+ decay from the spine), and the concentrations of PKA-pathway and PKC-pathway proteins (upstream of PKA and PKC). Alterations of the initial concentration of CaMKII (the only molecule in our model that exclusively affects the CaMKII pathway) had little effect in most domains of plasticity considered here (not shown), and thus, we omitted it in this analysis. We sampled these parameters from the following intervals: GluR1 ratio from the interval from 0 to 1 (keeping the total concentration of GluR subunits fixed at 540 nM), NCX concentration from the interval from 0 to twice the original value (2 × 0.54 mM), and the PKA and PKC-pathway factors $f_{PKA}$ and $f_{PKC}$ from the interval from 0 to 2 (see Materials and methods, section 'Parameter alterations and model fitting'). We simulated the post-synaptic spine 150,000 times using different random values for these parameters under zero, low (50 particles/ms), medium (150 particles/ms), and high (250 particles/ms) levels of Ca2+ input.

We classified the parameter sets based on the total synaptic conductance 15 min after the onset of the stimulation with the high Ca2+ flux (250 particles/ms): the relative synaptic conductance varied between 0.16 and 5.92, and thus, we grouped the parameter sets to 16 classes using a bin size of 0.36 (Figure 7A). We then analysed the parameter distributions and their co-variations within these classes and how the different parameters affected the shape of the LTP/LTD curve within each class. A special subset of the LTP/LTD curves were the BCM-type plasticity curves, where either 50 or 150 particles/ms Ca2+ injection resulted in LTD and the 250 particles/ms resulted in LTP.

![Figure 7.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig7-v2.jpg)

**Figure 7.:** (A) The LTP/LTD curves for all 16 classes. Four values of Ca2+ input amplitude were considered: 0, 50, 150, and 250 particles/ms (x-axis; repeated and overlaid for space). The y-axis shows the relative synaptic conductance, that is, total synaptic conductance 15 min after the onset of the Ca2+ input divided by the total synaptic conductance before the Ca2+ input. 20 representative parameter sets are displayed from each class, coloured from purple (lowest relative synaptic conductance response for medium Ca2+ input) to green (highest conductance). The black, dashed trace in class six represents the model with the default concentration parameters. (B–E) Distribution of model parameters, that is, GluR1 ratio (B), NCX-concentration coefficient (C), PKA pathway-concentration coefficient $f_{PKA}$ (D), and PKC pathway-concentration coefficient $f_{PKC}$ in the 16 classes. Class 6 (purple) highlighted for further analysis. F–H: GluR1 ratio plotted against NCX-concentration coefficient (F), $f_{PKA}$ (G), and $f_{PKC}$ (H) in class 6. The contours represent the distribution of parameters (N = 5837) that produced class-6 plasticity. No parameters yielding class-6 plasticity were found beyond the purple contour, and the inner contours cover the parameter space where the distribution is higher than 0%, 20%, 40%, 60% or 80% of the maximal density value. The black and red markers represent parameter sets that produced two plasticity subclasses, namely, one where the total deviance (summed absolute difference) from the BCM-type plasticity produced by the default parameter set (black, N = 145) or from a linearly increasing LTP (red, N = 183) was less than 0.2 (a.u.). Inset: The LTP/LTD plasticity curves of the two subclasses. The thick lines represent the centre of the subclasses (black: relative conductances in response to 50, 150, and 250 Ca2+ ions/ms: 0.76, 0.96, 2.24; red: relative conductances in response to 50, 150, and 250 Ca2+ ions/ms: 1.41, 1.83, 2.24).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Here, the experiment of Figure 7 is repeated by clustering the parameters sets based on the relative synaptic conductance after a steady-state Ca2+ flux of 50 particles/ms (250 particles/ms in Figure 7) to highlight the contribution of the PKC-pathway parameter. (A) The LTP/LTD curves for all 16 classes (classes 1’—16’). Four values of Ca2+ input amplitude were considered: 0, 50, 150, and 250 particles/ms (x-axis; repeated and overlaid for space). The y-axis shows the relative synaptic conductance, that is, total synaptic conductance 15 min after the onset of the Ca2+ input divided by the total synaptic conductance before the Ca2+ input. 20 representative parameter sets are displayed from each class, coloured from purple (lowest relative synaptic conductance response for medium Ca2+ input) to green (highest conductance). The black, dashed trace in class 6’ (note that this is a different group than class six in Figure 7) represents the model with the default concentration parameters. (B–E) Distribution of model parameters, that is, GluR1 ratio (B), NCX-concentration coefficient (C), PKA pathway-concentration coefficient $f_{PKA}$ (D), and PKC pathway-concentration coefficient $f_{PKC}$ in the 16 classes. Class 6’ (purple) highlighted for further analysis. (F–H) GluR1 ratio plotted against NCX-concentration coefficient (F), $f_{PKA}$ (G), and $f_{PKC}$ (H) in class 6’. The contours represent the distribution of parameters (N = 7275) that produced class-6’ plasticity. No parameters yielding class-6’ plasticity were found beyond the purple contour, and the inner contours cover the parameter space where the distribution is higher than 0%, 20%, 40%, 60% or 80% of the maximal density value. The black and red markers represent parameter sets that produced two plasticity subclasses, namely, one where the total deviance (summed absolute difference) from the BCM-type plasticity produced by the default parameter set (black, N = 98) or from a linearly decreasing LTP (red, N = 44) was less than 0.2 (a.u.). Inset: The LTP/LTD plasticity curves of the two subclasses. The thick lines represent the centre of the subclasses (black: relative conductances in response to 50, 150, and 250 Ca2+ ions/ms: 0.76, 0.96, 2.24; red: relative conductances in response to 50, 150, and 250 Ca2+ ions/ms: 0.76, 0.52, 0.27).

Our model with the standard protein concentrations (GluR1 ratio 0.5, [NCX] = 0.54 mM, $f_{PKA}=f_{PKC}=1.0$) produced a BCM-type curve in class 6 (Figure 7A, black dashed curve). Classes 11–16 exhibited the strongest LTP, with large synaptic conductance for both 150 and 250 particles/ms Ca2+ injection, whereas classes 1 and 2 only exhibited LTD (Figure 7A). Classes 3–12 exhibited BCM-type of plasticity but the majority of the LTP/LTD curves were of non-BCM type in each class (Figure 7A).

Three parameters — the GluR1 ratio, NCX concentration and $f_{PKA}$, differed significantly across the 16 classes (Figure 7B–D). Low GluR1 ratio was needed for strong LTD and medium or high GluR1 ratio for strong LTP (Figure 7B). However, the strongest forms of LTP (classes 11–16) were induced only when GluR1 ratio was smaller than 1 (Figure 7B), because a very low number of GluR2 subunits implied that the synapse has many homomeric GluR1 tetramers at a basal state, and thus stimulation-induced GluR1 exocytosis and GluR2 endocytosis did not radically increase the number of homomeric GluR1 tetramers (Equation 5, see also Figure 4D). For LTD and moderate LTP (classes 1–5), any NCX concentration and PKA-pathway coefficient could be used, but very strong LTP (classes 10–16) required a small to medium NCX concentration (Figure 7C) and a medium to large PKA-pathway coefficient (Figure 7D). By contrast, PKC-pathway coefficient alone was not predictive of plasticity outcome (Figure 7E).

The model results for the large parameter distributions of Figure 7B–E imply that there are manifestly different combinations of parameters that lead to the same LTP/LTD outcome. To analyse this intrinsic variability, we studied the distributions of the model parameters within the class of moderate LTP (class 6, 132–168% LTP for 250 particles/ms; indicated by purple boxes in Figure 7B–E) in more detail. Dependencies among the four parameters could be observed in 2-dimensional contour plots of the parameter distributions (Figure 7F–H). With large ($⪆0.6$) GluR1 ratios, any NCX, PKA or PKC concentration could be used, but with smaller ($⪅0.6$) GluR1 ratios, smaller NCX concentration (Figure 7F) or larger PKA-pathway coefficients (Figure 7G) were needed to obtain class-6 type of plasticity. To illustrate how these parameters affect the shape of the plasticity curves within class 6, we plotted the parameter sets that produced a BCM-type LTP/LTD curve similar to the one produced by our default model (Figure 7F inset, black) or an LTP curve that was linear within this regime (Figure 7F inset, red). Moderate GluR1 ratios (0.40–0.57; Figure 7F, black) and moderate NCX concentrations (0.7–1.4 times the default value; Figure 7F, black) were needed for the default BCM-type plasticity, while for the linear LTP curve a larger GluR1 ratio (0.59–0.92; Figure 7F, red) was needed but the NCX concentration was more variable (values ranged from 0.4 to 1.7 times the default value; Figure 7G, red). The PKA pathway coefficients were generally larger in the default BCM-type plasticity parameter sets than in the parameter sets producing the linear LTP curve (Figure 7G). Figure 7H shows the distributions of a set of coefficients, i.e. the PKC pathway, which were not correlated with the plasticity outcome within this group.

Our previous analysis showed that PKC-pathway-mediated GluR2 endocytosis was important in lower stimulation frequency protocols (Figure 3) or in protocols with large separation between pre- and post-synaptic stimuli (Figure 5). To further analyze the contribution of PKC-pathway proteins to plasticity outcomes, we repeated the analysis of Figure 7 by clustering the plasticity outcome based on the relative synaptic strength after a steady-state Ca2+ input of low amplitude (50 particles/ms; Figure 7—figure supplement 1A). As observed with the previous clustering, the GluR1 ratio and NCX concentration differed across classes (Figure 7—figure supplement 1B and C). However, in this classification, the PKA-pathway coefficient was not predictive of the plasticity outcome (Figure 7—figure supplement 1D) whereas the PKC-pathway coefficient varied across the classes (Figure 7—figure supplement 1E). Separation between BCM-like plasticity and gradual LTD was also evident within class 6’, and due to the same GluR1, PKA and NCX parameters as with the original classification (Figure 7—figure supplement 1F–H). This shows our identification of critical parameters is robust to how the classification was performed.

Taken together, our results show that alterations of the concentrations of the proteins regulating Ca2+ efflux or PKA/PKC-pathway signalling and the numbers of GluR1 and GluR2 subunits, ranging from complete absence to moderate increase (±100%), have a large effect both on the type of plasticity (LTP or LTD) and on the sensitivity of the plasticity outcome to the amplitude of the Ca2+ flux. These data suggest that neocortical post-synaptic spines may exhibit a vast set of plasticity rules by downregulation or relatively mild upregulation of their protein expression.

### A parametric analysis confirms the robustness of the model

We analysed the model responses to 4xHFS and LFS protocols (as in Figure 3) under small (±10%) changes in the parameters describing the initial concentrations and reaction rates (Figure 8). As expected, most parameter changes led to small deviations from the predicted magnitudes of LTP/LTD (Figure 8, grey bars). Alterations of the initial concentration of a number of species (10 out of 47) and reaction rates (12 out of 223) resulted in a notable (>15%) amplification or attenuation of LTD (Figure 8A) or LTP (Figure 8B). The parameters affecting the LFS-induced LTD were all related to GluR1 membrane insertion or total amount of GluR1 or GluR2 (Figure 8A), while the parameters affecting the 4xHFS-induced LTP were related to NCX-mediated Ca2+ extrusion, PP1 concentration, production of cAMP by AC1, PKA buffering/deactivation, or GluR1 membrane insertion (Figure 8B). Importantly, none of the parameter changes completely abolished the LTP or LTD. Taken together, our model is robust to small alterations in initial concentrations and reaction rates, but parameters influencing the Ca2+ dynamics, GluR1 activity, or the PKA-pathway signalling can have relatively large effects on the model output.

![Figure 8.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig8-v2.jpg)

**Figure 8.:** Values of initial concentrations (47 parameters) or reaction rates (223 parameters) were changed one at the time by −10% or +10%, and the resulting synaptic conductance 16 min after LFS (A) or 4xHFS (B) protocol was measured (NEURON RxD simulations). The initial synaptic conductance is 33.4 pS (see Figure 3A,S), although some parameter changes mildly affected this value (data not shown). The x-axis shows the post-LFS (A) or post-HFS (B) synaptic conductance, and the y-axis shows the number of parameter alterations. Majority of the parameter changes had small effect on plasticity (grey bars), but changes in initial concentrations of 10 species and 12 reaction rates caused >15% change in the amplitude of LTP or LTD — these changes are represented by black (multi-pathway parameters), blue (PKA-pathway-related parameters), and green (PKC-pathway-related parameters) bars. The underlying parameter changes are printed above the corresponding bar.

### The model flexibly reproduces data from various cortical LTP/LTD experiments

The richness of the intracellular signalling machinery behind LTP and LTD poses challenges for both qualitative and quantitative comparison between results from different cell types, obtained using different stimulation protocols, or even published by different laboratories Larkman and Jack, 1995. Computational biochemically detailed models have been proposed as an absolutely reproducible tool that is particularly suited for unifying our understanding of LTP and LTD across cell types and brain regions Manninen et al., 2010. Here, we show that our model for intracellular signalling in a cortical post-synaptic spine — through the use of varying concentrations of different proteins — can be flexibly tuned to reproduce data from the experimental literature of cortical LTP/LTD. This allows one to make predictions for the differences in intracellular machineries underlying each of the experiments, leading to a more complete view of the plasticity-related signalling pathways in different cell types in the cortex and the effects of the stimulation protocol on the plasticity outcome across cortical areas.

To show the flexibility of our model, we aimed to reproduce a large amount of data on cortical plasticity across cortical areas and stimulation paradigms. We reviewed the literature of cortical plasticity, and picked eight studies where one or more types of neurons were tested using one or more stimulation protocols and the outcome was quantified using electrophysiological measurements (Table 2). These studies comprised 11 data sets that described the response of a neuron population in entorhinal cortex (EC), prefrontal cortex (PFC), barrel cortex (BC), anterior cingulate cortex (ACC), visual cortex (VC), or auditory cortex (AuC) to plasticity inducing protocols (Table 2). For each experiment in each data set, we assigned an objective function that quantified the error between the predicted LTP/LTD outcome (measured in relative synaptic conductance) and the data (typically measured in fold change of field EPSP slope). The objective functions were averaged across different time instants (10, 15, and 20 min post-stimulus-onset). We then ran a multi-objective optimisation algorithm (see Materials and methods, section 'Parameter alterations and model fitting') that aimed at finding the values for model parameters that minimised these objective functions. The fitted parameters included the amplitudes of pre-synaptic stimulation-associated fluxes of Ca2+, β-adrenergic ligand and glutamate in addition to GluR1 fraction and factors for the protein concentrations of different pathways. Here, both the Ca2+ and the neuromodulatory inputs were square-pulse injections that followed every pre-synaptic stimulation although some of the studies of Table 2 used bath application of neuromodulatory agents; however, the temporal distribution of the neuromodulators has only a small effect in our model as shown earlier (Figure 3—figure supplement 4).We ran the optimiser for 20 generations. For data sets VC-1 and VC-2, we did not find parameter sets that would fulfil all four objective functions, and therefore, we re-fitted the model for these data sets excluding the CaMKII-blocked experiments (printed in grey in Table 2).

**Table 2.**
 List of LTP/LTD experiments in the cortex.The first column labels the experimental data set and names the underlying study. The second column shows the considered synaptic pathway and the third column shows whether the observed LTP/LTD had a pre- or post-synaptic origin. The fourth and fifth columns show the frequency (in Hz) of stimulation and the number of pulses delivered, respectively: 10 × 4 means that 10 trains of 4 pulses with 10 ms interval (100 Hz) were delivered, and likewise, 25 × 5 means that 25 trains of 5 pulses with 10 ms interval were delivered. The sixth column tells whether the data were obtained in control conditions or under additional blockers or agonists. The seventh, eighth, ninth, and tenth columns show the relative change in synaptic strength 10, 15, and 20 min after the start of the stimulus protocol and an average SD of the relative synaptic strengths — these values were approximated from the LTP/LTD curves plotted in the underlying references. The rows correspond to experiments from a given reference that are divided to 11 different experimental data sets. Within each data set, the underlying system is assumed to be otherwise similar to the control except for the applied modifier: as an example, the chemical or genetic blockade of CaMKII activity (as performed in Ma et al., 2008 and Hardingham et al., 2003) is here expected to only affect the ability of CaMKII to autophosphorylate, and the rest of the model parameters are kept fixed. The experiments printed in grey were included in the underlying study, but were excluded from the main analyses of the present work (see main text). EC – entorhinal cortex; PFC – prefrontal cortex; BC – barrel cortex; ACC – anterior cingulate cortex; VC – visual cortex; AuC – auditory cortex; CC – corpus callosum. (*): The LFS of 900 3-ms pulses at 5 Hz in data sets VC-1 and VC-2 was replaced by 180 15-ms pulses at 1 Hz to decrease computational load in the optimisation.


<table>
  <thead>
    <tr>
      <th>Data set</th>
      <th>Reference</th>
      <th>Pathway</th>
      <th>Pre/post</th>
      <th>Freq.</th>
      <th>Npulses</th>
      <th>Experiment</th>
      <th>10 min</th>
      <th>15 min</th>
      <th>20 min</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC-1</td>
      <td>Ma et al., 2008</td>
      <td>horizontal</td>
      <td>mostly</td>
      <td>100</td>
      <td>100</td>
      <td>control</td>
      <td>1.3</td>
      <td>1.4</td>
      <td>1.3</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>post</td>
      <td></td>
      <td></td>
      <td>CaMKII blocked</td>
      <td>1.05</td>
      <td>1.02</td>
      <td>0.95</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>without post-syn. Ca2+</td>
      <td>1.05</td>
      <td>1.05</td>
      <td>1.1</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>EC-2</td>
      <td>Ma et al., 2008</td>
      <td>ascending</td>
      <td>mostly</td>
      <td>100</td>
      <td>100</td>
      <td>control</td>
      <td>1.6</td>
      <td>1.6</td>
      <td>1.6</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>post</td>
      <td></td>
      <td></td>
      <td>PKA blocked</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>without post-syn. Ca2+</td>
      <td>1.3</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>PFC-1</td>
      <td>Sáez-Briones et al., 2015</td>
      <td>CC→PFC</td>
      <td>n/a</td>
      <td>312</td>
      <td>156</td>
      <td>control</td>
      <td>2.0</td>
      <td>1.98</td>
      <td>1.9</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>without β-adrenergic ligand</td>
      <td>1.34</td>
      <td>1.4</td>
      <td>1.36</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>PFC-2</td>
      <td>Flores et al., 2011</td>
      <td>CC→PFC</td>
      <td>n/a</td>
      <td>312</td>
      <td>156</td>
      <td>control</td>
      <td>1.7</td>
      <td>1.6</td>
      <td>1.64</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>without β−1-receptor agonist</td>
      <td>1.43</td>
      <td>1.45</td>
      <td>1.43</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>BC</td>
      <td>Hardingham et al., 2003</td>
      <td>L4→L2/3</td>
      <td>n/a</td>
      <td>5</td>
      <td>10 × 4</td>
      <td>control</td>
      <td>1.35</td>
      <td>1.4</td>
      <td>1.3</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CaMKII mutant</td>
      <td>1.25</td>
      <td>1.2</td>
      <td>1.1</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>ACC</td>
      <td>Song et al., 2017</td>
      <td>L5/6 → L2/3</td>
      <td>post</td>
      <td>5</td>
      <td>10 × 4</td>
      <td>control</td>
      <td>1.55</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>without s845</td>
      <td>1.1</td>
      <td>1.05</td>
      <td>1.05</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>without s831</td>
      <td>1.35</td>
      <td>1.4</td>
      <td>1.3</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>PFC-3</td>
      <td>Zhou et al., 2013</td>
      <td>L2/3 → L2/3</td>
      <td>mostly</td>
      <td>0.1</td>
      <td>50</td>
      <td>control</td>
      <td>1.3</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>post</td>
      <td></td>
      <td></td>
      <td>without β−1-receptor agonist</td>
      <td>1.1</td>
      <td>1.2</td>
      <td>1.2</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>VC-1</td>
      <td>Kirkwood et al., 1997</td>
      <td>L4 → L3</td>
      <td>n/a</td>
      <td>5</td>
      <td>10 × 4</td>
      <td>(CTR, HFS)</td>
      <td>1.3</td>
      <td>1.26</td>
      <td>1.26</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>(adult)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>(without CaMKII, HFS)</td>
      <td>1.02</td>
      <td>1.02</td>
      <td>1.02</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>5</td>
      <td>900*</td>
      <td>(CTR, LFS)</td>
      <td>n/a</td>
      <td>0.95</td>
      <td>0.95</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>(without CaMKII, LFS)</td>
      <td>n/a</td>
      <td>0.88</td>
      <td>0.93</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>VC-2</td>
      <td>Kirkwood et al., 1997</td>
      <td>L4 → L3</td>
      <td>n/a</td>
      <td>5</td>
      <td>10 × 4</td>
      <td>(CTR, HFS)</td>
      <td>1.2</td>
      <td>1.18</td>
      <td>1.18</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>(4–5 w)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>(without CaMKII, HFS)</td>
      <td>1.07</td>
      <td>1.09</td>
      <td>1.08</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>5</td>
      <td>900*</td>
      <td>(CTR, LFS)</td>
      <td>n/a</td>
      <td>0.79</td>
      <td>0.82</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>(without CaMKII, LFS)</td>
      <td>n/a</td>
      <td>0.82</td>
      <td>0.89</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>AuC-1</td>
      <td>Kotak et al., 2007</td>
      <td>L6 → L5</td>
      <td>n/a</td>
      <td>1</td>
      <td>25 × 5</td>
      <td>LTP-expressing cells</td>
      <td>1.98</td>
      <td>1.58</td>
      <td>1.93</td>
      <td>0.19</td>
    </tr>
    <tr>
      <td>AuC-2</td>
      <td>Kotak et al., 2007</td>
      <td>L6 → L5</td>
      <td>n/a</td>
      <td>1</td>
      <td>25 × 5</td>
      <td>LTD-expressing cells</td>
      <td>0.77</td>
      <td>0.68</td>
      <td>0.67</td>
      <td>0.09</td>
    </tr>
  </tbody>
</table>

We found groups of parameter sets that fit within one standard deviation (SD) on average from the target values of synaptic conductance for each data set of Table 2 (Figure 9A–C). There were differences in the numbers of acceptable parameter sets between the data sets due to differences in the postulated strength of the LTP/LTD, the number of experiments, and the SD of the post-stimulus synaptic conductance (Figure 9D). The data sets EC-1 and BC were particularly challenging to fit (<0.2% of the parameter sets tested by the optimiser gave an acceptable fit; Figure 9D). By contrast, the data set AuC-2 was the easiest to fit (3.9% of the parameter sets were acceptable; Figure 9D).

![Figure 9.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-v2.jpg)

**Figure 9.:** (A) The model could be fit to LTP/LTD data from data sets EC-1 (top), EC-2, PFC-1, PFC-2, BC, ACC, PFC-3, AuC-1, and AuC-2 (bottom). The curves represent the model predictions of the best-fit parameter sets, and the dots represent the experimental data from Table 2. For data sets other than AuC-1 and AuC-2, several experiments with various chemical agents or genetic mutations were performed for each neuron population: these are ordered as in Table 2 (e.g., in data set EC-1, purple (1 st experiment) corresponds to control, blue (2nd experiment) to CaMKII-blocked experiment, and green (3rd experiment) to the experiment where post-synaptic Ca2+ was blocked). (B) The model could not be fit to the complete LTP/LTD data from data sets VC-1 (top) and VC-2 (bottom). The best parameter sets correctly predicted the LTP/LTD in up to two experiments (e.g., the selected parameter sets reproduce the HFS data with and without CaMKII inhibitor, but failed to reproduce the LFS data). (C) The model could be fit to the LTP/LTD data from data sets VC-1 (top) and VC-2 (bottom) when CaMKII-blocked experiments were ignored. The vertical bars in (B) and (C) represent the SD from the experimental data. (D) Proportion of accepted parameter sets across the 20 generations of multi-objective optimisation (20’000 parameter sets in total) in each data set. (E) Box plots of selected parameters in the acceptable parameter sets of data sets EC-1 and EC-2 (three left-most pairs) and AuC-1 and AuC-2 (right-most pair). Values of $f_{CaMKII}$ and $f_{PKA}$ are linearly scaled such that the values 0 and 1 correspond to 0 and double the original value of the underlying parameters, respectively (CaM and CaMKII for $f_{CaMKII}$, and R, Gs, AC1, and AC8 for $f_{PKA}$, see Materials and methods, section 'Parameter alterations and model fitting'). The medians were significantly different in the compared data sets (U-test, p-value<0.001).

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** Ranges of each parameter among the accepted parameter sets from the fitting of Figure 9. All parameters are linearly scaled between 0 and 1, which represent the minimal and maximal value of the corresponding model parameter. The values of the parameters reproducing the data of Figure 9A and C are presented by red dots, and their exact (non-scaled) values are listed below the figure. The values of the error functions corresponding to the listed parameter set are displayed in the right-most column for each experiment.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp2-v2.jpg)

**Figure 9—figure supplement 2.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 3.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp3-v2.jpg)

**Figure 9—figure supplement 3.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 4.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp4-v2.jpg)

**Figure 9—figure supplement 4.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 5.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp5-v2.jpg)

**Figure 9—figure supplement 5.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 6.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp6-v2.jpg)

**Figure 9—figure supplement 6.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 7.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp7-v2.jpg)

**Figure 9—figure supplement 7.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 8.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp8-v2.jpg)

**Figure 9—figure supplement 8.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 9.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp9-v2.jpg)

**Figure 9—figure supplement 9.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 10.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp10-v2.jpg)

**Figure 9—figure supplement 10.:** See Figure 9—figure supplement 1 for details.

![Figure 9—figure supplement 11.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig9-figsupp11-v2.jpg)

**Figure 9—figure supplement 11.:** See Figure 9—figure supplement 1 for details.

The obtained parameters reflect the pathways needed for the type of plasticity. For example, the LTP of synapses of the horizontal but not those of the ascending pathway to EC were blocked by CaMKII inhibition, while the LTP of synapses of the ascending pathway were blocked by PKA inhibition (Ma et al., 2008). This is reflected in the obtained parameter sets: the parameter controlling CaM and CaMKII concentrations ($f_{CaMKII}$) was significantly larger (U-test, p-value<0.001) in the horizontal-pathway (data set EC-1) synapse models, while the parameter controlling upstream PKA-pathway proteins ($f_{PKA}$) was significantly larger in the models reproducing the data from the ascending pathway (data set EC-2; Figure 9E). The GluR1-GluR2 ratio, in turn, was not significantly different between the two data sets (Figure 9E). As a contrasting example, our model predicts a large variety of parameters that reproduce the LTP and LTD of data sets AuC-1 and AuC-2 but, consistent with the results of Figure 7, the GluR1 ratio was significantly larger in the model parameters fitted to the data from LTP-expressing neurons than from LTD-expressing neurons (Figure 9E). The complete graphs of parameter value distributions in the 11 data sets and the parameter set producing the best fit (Figure 9A) for each data set are shown in Supplementary data, Figure 9—figure supplements 1–11. Taken together, our model-fitting experiment shows that the model can be fit to many types of multi-condition plasticity data — without altering the reaction rates — and that the resulting predictions of the underlying protein concentrations reflect the mechanisms proposed by the experimental studies.

The models obtained by fitting the initial concentrations to data provide an important tool for predicting the outcome of plasticity under various stimulus protocols and chemical agents. We carried out additional simulations with the obtained models using HFS protocol. The models fitted for data from EC (data sets EC-1 and EC-2, [Ma et al., 2008]), BC (Hardingham et al., 2003), ACC (Song et al., 2017), and LTP-expressing auditory cortical neurons (data set AuC-1, Kotak et al., 2007) predicted a steady increase in response to HFS, while models fitted for other cortical data predicted a mixture of LTP, LTD, and no change (Figure 10A). Furthermore, to obtain experimentally testable predictions for the dependency of the plasticity outcome in different cortical areas on the intracellular signalling, we simulated the models from each data set with the corresponding stimulus protocol with CaMKII, PKA, or PKC blockade. The inhibition of CaMKII impaired the LTP in data set EC-1 (horizontal pathway) but had little or no effect on the plasticity in other cortical areas (Figure 10B). The lack of effect of CaMKII blockade on the ascending pathway of EC — an experiment which was not included in the fitting of the model (Table 2) — validates the underlying models in this aspect since similar results were observed in Ma et al., 2008. Moreover, the similarities in the predicted effect of CaMKII-, PKA-, and PKC-pathway blockades between the two models of CC→PFC synapses (PFC-1 and PFC-2; Figure 10B–D) serve as an additional validation of these models. The inhibition of PKA impaired LTP in all cortical areas, except for LTP in the horizontal pathway of the EC (EC-1; Figure 10C). Our models also predicted that LTP of the CC→PFC pathway and LFS-induced LTP in VC can be effectively weakened or even be transformed to a mild LTD by PKA blockade (Figure 10C). Finally, our models predicted that PKC inhibition transformed all forms of LTD (LFS-induced LTD in VC-1 and VC-2; LTD in AuC-2) into LTP and impaired certain forms of LTP (LTP in EC-2; LTP in AuC-1) (Figure 10D). Taken together, our results suggest that almost all forms of post-synaptic plasticity in the cortex are likely to be PKA-dependent, and that many types of cortical plasticity are also influenced by CaMKII and PKC activity. Our results highlight the need for additional chemical or genetic manipulations to be done when experimenting on cortical plasticity in order to correctly reveal the intracellular signalling cascades in the post-synaptic spine.

![Figure 10.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig10-v2.jpg)

**Figure 10.:** (A) The predicted responses of the 20 best models in each data set to HFS (100 pulses at 100 Hz) stimulation. (B–D) The predicted responses of the 20 best models in each data set to the applied stimulation protocol (see Table 2) when CaMKII (B), PKA (C), or PKC (D) activity was blocked (red) or under control condition (black).

## Discussion

We built a single-compartment model describing the major post-synaptic signalling pathways leading to LTP and LTD in the cortex. We showed that our model reproduced conventional types of LTP and LTD, where an HFS-induced increase in GluR1 can increase the synaptic conductance (LTP) and an LFS-induced endocytosis of GluR2 can decrease it (LTD; Figure 3) and reproduced STDP data from visual cortical layer 2/3 pyramidal cells (Figure 5). Our model explains how different forms of plasticity depend on the concentrations of PKA- and PKC-pathway proteins (Figure 7). We also showed that our model can be fit to explain the pathway dependencies of various types of neocortical LTP/LTD data published in the literature by altering the magnitude of Ca2+ and ligand fluxes and the concentrations of post-synaptic proteins regulating the Ca2+ efflux and PKA- and PKC-pathway dynamics (Figure 9). Our fitted models provide a powerful tool for testing hypotheses on the effects of chemical or genetic manipulations on the LTP and LTD in different cortical regions (Figure 10).

### Role of GluR2 in synaptic plasticity in the neocortex

GluR2 subunits are highly expressed in neocortical neurons (Kondo et al., 1997), and their endocytosis mediates (or, at minimum, is correlated with) synaptic depression in many cortical regions such as ACC (Toyoda et al., 2007), VC (Heynen et al., 2003), and PFC (Van den Oever et al., 2008). Previous intracellular signalling-based models of neocortical LTP/LTD exist, but they do not take into account the contributions of GluR2 subunit. For example, in three previous models (D'Alcantara et al., 2003; Castellani et al., 2005; Honda et al., 2013), S831-phosphorylation-mediated LTP was described in a fashion similar to our model (although more approximations were made), but the phosphorylation site S845 was assumed to be basally phosphorylated and LTD was caused by modest Ca2+ inputs that led to PP1 or PP2B-mediated dephosphorylation of S845. Although there is support for this order of events (Lee and Kirkwood, 2011; Diering et al., 2016), newer findings have confirmed the low degrees of phosphorylation of both S831 and S845 at a basal state in cortical cells, especially in synaptic spines (Diering et al., 2016). A recent phenomenological model has also shed light on the dependency of cortical STDP on the pairing interval and location of the synapse (Ebner et al., 2019), but their mechanisms are not specific to any particular AMPAR or NMDAR subunit. To analyse the contributions of GluR2 subunits to neocortical LTP/LTD, we included in our model the signalling pathways leading to both phosphorylation-mediated exocytosis of GluR1 and endocytosis of GluR2. Our model could thus be used to study not only PKA-mediated LTP or PKC-mediated LTD but also their co-effects and co-dependencies.

### Implications of the study

The modelling results of the present work give rise to experimentally testable predictions. For example, our STDP model, when stimulated without β-adrenergic ligands, suggests that at near-zero pairing-intervals the magnitude of the depression may be decreased or even switched to mild LTP (Figure 5J). In many experimental studies (including Seol et al., 2007), the type and magnitude of plasticity in this regime of STDP is not reported. We also predict that a mild LTP (24–60% LTP; class 4 in Figure 7) can be obtained through many differently weighted interactions of PKA and PKC pathways and Ca2+ extrusion strengths (Figure 7F–H, Figure 9—figure supplement 1 and 2, Figure 9—figure supplement 5–7).Importantly, this is the regime of a wealth of experimental LTP data (Tsumoto, 1990; Table 2), which is consistent with the great diversity of LTP mechanisms observed in the neocortex (Feldman, 2009). Based on our simulated data (Figure 10), we suggest that in order to correctly characterise the mechanisms behind LTP of especially this magnitude, both experiments that activate the PKA pathway and experiments that block or activate the PKC pathway should be carried out. It is also important to know whether and to what degree GluR1 and GluR2 subunits are present in the synapse, since the balance of GluR1 and GluR2 subunits seems to be a determinant parameter permitting certain types of plasticity while prohibiting others (Figures 7B and 9E, and Figure 3—figure supplement 1).

A key challenge in the study of synaptic plasticity is the diversity of LTP/LTD observed across the cell types in the brain (Granger and Nicoll, 2014). Differences in the transcriptome have been proposed as one of the sources for this variability (Lisachev and Shtark, 2018). We believe our model can be used to explain some of the discrepancies in the experimental data in this regard and expand the understanding of possible molecular contributors to LTP/LTD. For example, it is known that activation of PKA pathway by dopamine or noradrenaline in PFC pyramidal neurons increases the synaptic conductance through GluR1 membrane insertion (Sun et al., 2005; Xu et al., 2010). Our model is in agreement with this (Figure 3), but it also proposes that the LTP can be impaired by over- or underexpression of many involved proteins, such as AC1, I-1 (inhibitor of PP1), PDE4, PDE1, GluR1, and CaM, and even alterations in ATP concentration (see Figure 8B). Small differences in the concentrations of a number of such contributing proteins are likely to cause significant alterations to LTP observed in different brain areas and cell types.

Due to the inclusion of three major LTP/LTD pathways in the neocortex, our model provides a more accurate means than earlier models for exploring how the Ca2+ dynamics in the spine affects the plasticity outcome in many stimulation protocols, STDP in particular. Our model suggests that the plasticity outcome of the STDP protocol is strongly correlated with the total amount of Ca2+ entering the post-synaptic spine, and less so with the peak Ca2+ flux (Figure 6—figure supplement 1).The total amount of Ca2+ influx could thus provide a better biomarker for plasticity than the previously considered amplitude and duration of the Ca2+ transient (Evans and Blackwell, 2015).

### Validity of the results and limitations of the study

Our model of total synaptic conductance of the post-synaptic spine is based upon a number of assumptions. First, the prediction of a large increase of conductance that follows the replacement of GluR2 subunits at the membrane by GluR1 subunits (e.g., Figure 3) is based upon the findings on differences in single-channel conductances of different types of AMPAR tetramers in hippocampal neurons (Oh and Derkach, 2005). Following Oh and Derkach, 2005, we assumed that CaMKII-phosphorylation of S831 only increases the conductance of GluR1 homomers and not that of GluR1/GluR2 heteromers, although also heteromers have been observed to increase their conductance in the presence of transmembrane AMPAR regulatory proteins (Kristensen et al., 2011). Second, we assumed a random tetramerization procedure in which each of the four subunits in the tetramer may be either GluR1 or GluR2 subunit. Traditionally, AMPARs were thought to assemble as dimers of like dimers, that is, that first GluR1s and GluR2s assemble into homomeric R1-R1 and R2-R2 dimers and R1-R2 heterodimers and that these three types of dimers only assemble into tetramers with a dimer of its own kind (Gan et al., 2015). However, recent findings of heterotetramers with only one GluR1 subunit (Zhao et al., 2019) challenge this model. To show that our results were not dependent on the details of this process, we reproduced our results using the alternative (dimer of like dimers) tetramer formation rule. Using a slightly modified GluR1-GluR2 balance (35:65), this model reproduced HFS-induced LTP and LFS-induced LTD (Figure 3—figure supplement 2A) as well as the neuromodulator-gated STDP (Figure 3—figure supplement 2A).In summary, our model predictions were not dependent on the assumptions on the tetramer formation rule.

Our model reproduced the qualitative results of STDP of layer 2/3 pyramidal cells in visual cortex being gated by neuromodulators, but there were quantitative differences. When acetylcholine was present, our model predicted a prominent decrease in GluR2 membrane-expression regardless the pairing interval (Figure 5I), which caused a notable LTD for very large pairing intervals (Figure 5J), whereas the experimental data showed attenuation of the depression for large inter-stimulus intervals (Seol et al., 2007). This discrepancy is likely caused by processes allowing slower time-scale (>50 ms) interaction between the pre- and post-synaptic stimulus that are either not included (e.g., Ca2+-induced Ca2+ release or cAMP-dependence of HCN channels) or not adequately strong in the multi-compartmental model. For example, the contributions of voltage-gated Ca2+ channels and SK channels to the neuron electrophysiology may be large (Mäki-Marttunen et al., 2017; Mäki-Marttunen et al., 2018) — to this end, we showed here that the SK currents are amplified by the subsequent pulses stimulating the post-synaptic neuron and that this is one factor increasing the LTD for large ISIs (Figure 6). Note that this prediction of lowered synaptic strength for large absolute ISIs is not to be considered a basal synaptic state under spontaneous activity since the amplitude of the LTD is significantly decreased both by the removal of cholinergic neuromodulation (Figure 6J) and a decrease of stimulating frequency (data not shown). On the other hand, mechanisms lacking from the biochemical model (e.g., voltage-dependence of the Ca2+-extrusion rate of NCX Weber et al., 2002) could also impede our results in this matter. Some aspects of cellular physiology could therefore be better represented if we incorporated both biochemical signalling and multicompartmental Hodgkin-Huxley-type modelling into the simulations, as done in modelling studies of persistent neuron firing (Neymotin et al., 2016) and astrocyte electrophysiology (Savtchenko et al., 2018).

The quality of the model fitting to experimental data in Figure 9 is restricted by the fact that not all of the LTP/LTD data in Table 2 were confirmed to have a post-synaptic origin. This may be the key source of discrepancy in the fitting of the model to the CaMKII-blocked data from Kirkwood et al., 1997 (Figure 9B), since CaMKII activation at the pre-synaptic spine may lead to EPSC potentiation through an increase in neurotransmitter release (Ninan and Arancio, 2004). This scenario is supported by Seol et al., 2007 where S831-deficient mice were observed to show normal post-synaptic LTP in the VC.

### Outlook

Our results on interactions of the different pathways in post-synaptic spines including both GluR1 and GluR2 subunits provide valuable insights on the contributions of protein expression on the plasticity of the synapse. Previously, synaptic plasticity outcomes in the cortex have been conjectured to depend on the type of the post-synaptic cell type, in addition to the timing and frequency of the applied stimuli and dendritic filtering properties (Bi and Poo, 1998; Sjöström et al., 2001). Our model provides a way to analyse exactly which aspects of PKA-, PKC- and CaMKII-pathway signalling underlie these cell-type-dependent differences in synaptic plasticity. Combining our biochemically detailed model with biophysically detailed models from different cortical areas will provide models with better predictive power in the future. Moreover, our model can be used for initial testing of hypotheses concerning dysfunctions (including chemical and genetic manipulations) of many intracellular signalling proteins and their role in impairments of cortical synaptic plasticity. By altering the initial concentrations or reaction rates of various species according to disease-associated functional genetics data, the model can be used to provide insights into the disease mechanisms of mental disorders that express both genetic disposition of post-synaptic signalling pathways and plasticity-related phenotypes, such as schizophrenia (Devor et al., 2017).

## Materials and methods

### Construction and calibration of the biochemically detailed model of post-synaptic plasticity in the cortex

We created a model of pathways leading from Ca2+ inputs and activation of β-adrenergic receptors, metabotropic glutamate receptors, and muscarinic acetylcholine receptors to the phosphorylation and insertion of AMPARs into the membrane. We started by using the model of Jȩdrzejewska-Szmek et al., 2017 for GluR1 phosphorylation at sites S831 and S845, which are phosphorylated by PKA and CaMKII, respectively, as a basis for our unified model. We added the mGluR- and M1 receptor-dependent pathways leading to PKC activation from Kim et al., 2013 and Blackwell et al., 2019, respectively, and adopted the PKC-dependent endocytosis of GluR2 and reinsertion to the membrane from Gallimore et al., 2018 as these pathways are critical for neocortical plasticity (Seol et al., 2007). As we included molecular species from different models and as we omitted certain molecular species that affected the dynamics of the underlying species but were not imperative for the pathways we wanted to describe, calibration of the model reactions was necessary. Following Hayer and Bhalla, 2005, we allowed the insertion and removal of GluR1 subunits to and from the membrane that depended on their state of S845 phosphorylation. We also allowed spontaneous membrane insertion of non-S845-phosphorylated GluR1; we chose the rate of this reaction so that on average one fifth of the (non-S845-phosphorylated) GluR1s were membrane-expressed in steady state, as suggested by experimental data (Oh et al., 2006). We adjusted the forward rate of GluR2 insertion to the membrane to decrease the proportion of membrane-inserted vs. internalised GluR2s (Figure 11A), following experimental data according to which 45% of GluR2s were membrane-inserted at resting conditions (Ashby et al., 2004). We also adopted the three-step CaM activation of Gallimore et al., 2018 instead of the two-step activation of Jȩdrzejewska-Szmek et al., 2017 where the reaction rates of CaM binding two Ca2+ ions were linearly dependent on the number of Ca2+ ions. The response curve for CaM activation by Ca2+ was steeper in this model (Figure 11B), which was in better accordance with recent experimental data (Hoffman et al., 2014). As a result, our model predicted a more prominent activation of CaM in response to a large influx of Ca2+ but milder activation in respose to small Ca2+ influx than the model of Jȩdrzejewska-Szmek et al., 2017 (Figure 11C).

![Figure 11.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig11-v2.jpg)

**Figure 11.:** Black curves represent the final model, while grey lines represent predictions of models where previous model components or tentative parameter values were used. (A) Concentration of membrane-inserted GluR2 in 4xHFS when the forward rate of the membrane insertion of non-phosphorylated GluR2 was 0.0055 1/ms Gallimore et al., 2018 (grey) or 0.00025 1/ms (black). The rate 0.00025 1/ms caused a resting-state concentration of 121 nM for the membrane-bound GluR2 subunits, which is 45% of the total GluR2 concentration (270 nM). (B) Steady-state concentration of activated (bound by four Ca2+ ions) CaM in response to a prolonged Ca2+ input amplitude when the two-step (grey) or three-step (black) activation of CaM by Ca2+ was used. The x-axis shows the corresponding steady-state concentration of free Ca2+. Here, the initial concentrations of molecular species were as in Li et al., 2020, namely, 50 μM for CaM, Ng, PP2B, and CaMKII and 0 μM for all other species. Red dots show experimental data from Hoffman et al., 2014. (C) Concentration time course of non-protein-bound activated CaM (inset) or total activated CaM (main figure) in response to 4xHFS when the two-step (grey) or three-step (black) activation of CaM by Ca2+ was used. (D) Percentage of S880-phosphorylated GluR2 15 min after LFS when different forward rates of the activation of persistent PKC (kf between 0.00005 and 0.005 1/(nM ms)) were used. The value kf = 0.0005 1/(nM ms) gave a percentage of 47%, in close agreement with Ashby et al., 2004. (E–G) The dynamics of transiently active PKC (E) were not strongly influenced by the forward rate of the activation of persistent PKC (reaction 140), but those of persistently active PKC (F) and S880-phosphorylated GluR2 (G) were significantly affected. Black curves show the data corresponding to kf = 0.0005 1/(nM ms), while the grey lines show the data corresponding to kf = 0.00015 1/(nM ms) (dashed) and kf = 0.0015 1/(nM ms) (dotted). (H) Predicted responses of an isolated PKA activation model (reactions 59 and 93) to a 16 s cAMP input (dim grey background) when different values of the forward rate of PKA binding with four cAMP molecules were used. The curves show the concentration of the catalytic PKA subunit when different forward rates of PKA–cAMP binding (from bottom to top: 0.4 ×109, 1.0×10 9, 1.6 ×109, 2.2×10 9, and 2.8 ×109 1/(nM4ms)) were used. The markers show the corresponding data when the two-step PKA–cAMP binding model of Jȩdrzejewska-Szmek et al., 2017 was used. Inset: summed absolute differences between the tentative data (curves) and simulated data from the previous model (markers). The model with the forward rate of kf = 1.6 × 109 1/(nM4ms) gave the closest correspondence to the model of Jȩdrzejewska-Szmek et al., 2017. (I) Concentration of S845-phosphorylated GluR1 in response to 4xHFS when the single-step (reaction 59, black) or two-step (from Jȩdrzejewska-Szmek et al., 2017, grey) PKA–cAMP binding was used. (J) Concentration of S831-phosphorylated GluR1 in response to 4xHFS when PKC did (black) or did not (grey, overlaid) phosphorylated S831 in GluR1s.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig11-figsupp1-v2.jpg)

**Figure 11—figure supplement 1.:** The model was run for 4040 s without inputs. The absolute values of the time derivatives for each molecular species were determined, and the black curve shows the sum of these derivatives (nM/sec) across the species. The dashed blue line shows the concentration derivative value that corresponds to a change of one molecule/sec in a spine of volume 0.5 μm3.

![Figure 11—figure supplement 2.](https://cdn.elifesciences.org/articles/55714/elife-55714-fig11-figsupp2-v2.jpg)

**Figure 11—figure supplement 2.:** The model of Figure 5 was simulated with altered AMPAR (A) or NMDAR (B) conductances, and the effects on STDP curves were measured. See Figure 5 for details. (A) Half (blue) or double (red) the original value (black) of the AMPAR conductances were used. (B) Half (blue) or double (red) the original value (black) of the NMDAR conductances were used.

To allow long-term activation of PKC, we adopted a persistently activated form of PKC, mediated by arachidonic acid (AA), from Kotaleski et al., 2002. We calibrated the rates of this reaction as follows. The backward rate was chosen so that approximately 90% of PKC would be active after 10 min, inspired by experimental data of Shirai et al., 1998. The forward rate was chosen so that LFS with effective PLC activation led to approximately 50% of the GluR2s being phosphorylated (Figure 11D), following experimental data (Ahmadian et al., 2004). The implications of these adjustments on the dynamics of transiently activated PKC, persistently activated PKC and GluR2 S880 phosphorylation are illustrated in Figures 11E, F and G, respectively.

We adopted the simplified, mass-action law-based PKA activation model (reaction 59; Table 3) from Williamson et al., 2009 (where it was called model ‘C’) instead of the 2-stage, linearised cAMP-binding of PKA in Jȩdrzejewska-Szmek et al., 2017 and Blackwell et al., 2019. We fitted the forward rate to data simulated with the original model (Figure 11H) to produce a longer-lasting S845 phosphorylation (typically,>10 min duration of S845 phosphorylation was observed Seol et al., 2007; Xue et al., 2014) in the 4xHFS protocol (Figure 11I). To account for the experimental observation the PKC phosphorylates GluR1 at site S831 Roche et al., 1996, we added this reaction using the rates identical to those of GluR1-S831 phosphorylation by phosphorylated CaMKII (see reactions 71–72). However, the presence of this reaction did not have a large effect on the S831 phosphorylation of GluR1 under standard conditions (Figure 11J). Finally, we introduced an immobile Ca2+ buffer with a Ca2+ binding rate of 0.0004 1/(nM ms), a release rate 20.0 1/ms, and an initial concentration of 500 μM (these values are within the range of experimental observations and values used in models Matthews and Dietrich, 2015). The model reactions are described in Table 3 and the initial concentrations are listed in Table 4.

**Table 3.**
 List of model reactions.(A) The reaction-rate units are in 1/ms, 1/(nMms), 1/(nM2ms), 1/(nM3ms), or 1/(nM4ms), depending on the number of reactants. Reactions are grouped by similar modes of action and identical forward and backward rates. The denominators $𝐗$, $𝐘$, and $𝐙$ represent groups of species detailed below. †: backward reaction rate proportional to [PKAc], not to [PKAc]2. (B) Groups of species as used in panel (A).


<table>
  <thead>
    <tr>
      <th>(A)</th>
      <th></th>
      <th>Forw.</th>
      <th>Backw.</th>
      <th></th>
      <th></th>
      <th>Forw.</th>
      <th>Backw.</th>
    </tr>
    <tr>
      <th>ID</th>
      <th>Reaction</th>
      <th>Rate</th>
      <th>Rate</th>
      <th>ID</th>
      <th>Reaction</th>
      <th>Rate</th>
      <th>Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Ca + PMCA ⇌ PMCACa</td>
      <td>5e-05</td>
      <td>0.007</td>
      <td>71</td>
      <td>GluR1𝐗22 + 𝐘22 ⇌ GluR1𝐙22</td>
      <td>2.78e-08</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>2</td>
      <td>PMCACa ⇌ PMCA + CaOut</td>
      <td>0.0035</td>
      <td>0.0</td>
      <td>72</td>
      <td>GluR1𝐗23 ⇌ GluR1 𝐘23 + 𝐙23</td>
      <td>0.0005</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Ca + NCX ⇌ NCXCa</td>
      <td>1.68e-05</td>
      <td>0.0112</td>
      <td>73</td>
      <td>GluR1𝐗24 + PKAc ⇌ GluR1𝐙24</td>
      <td>4e-06</td>
      <td>0.024</td>
    </tr>
    <tr>
      <td>4</td>
      <td>NCXCa ⇌ NCX + CaOut</td>
      <td>0.0056</td>
      <td>0.0</td>
      <td>74</td>
      <td>GluR1𝐗25 + PP1 ⇌ GluR1𝐙25</td>
      <td>8.7e-07</td>
      <td>0.00068</td>
    </tr>
    <tr>
      <td>5</td>
      <td>CaOut + Leak ⇌ CaOutLeak</td>
      <td>1.5e-06</td>
      <td>0.0011</td>
      <td>75</td>
      <td>GluR1𝐗26 ⇌ GluR1 𝐘26 + PP1</td>
      <td>0.00017</td>
      <td>0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>CaOutLeak ⇌ Ca + Leak</td>
      <td>0.0011</td>
      <td>0.0</td>
      <td>76</td>
      <td>GluR1𝐗27 + PP1 ⇌ GluR1𝐙27</td>
      <td>8.75e-07</td>
      <td>0.0014</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Ca + Calbin ⇌ CalbinC</td>
      <td>2.8e-05</td>
      <td>0.0196</td>
      <td>77</td>
      <td>GluR1𝐗28 ⇌ GluR1 𝐘28 + PP1</td>
      <td>0.00035</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>L ⇌ LOut</td>
      <td>0.0005</td>
      <td>2e-09</td>
      <td>78</td>
      <td>GluR1𝐗29 + PP2BCaMCa4 ⇌ GluR1𝐙29</td>
      <td>2.01e-06</td>
      <td>0.008</td>
    </tr>
    <tr>
      <td>9</td>
      <td>L + R ⇌ LR</td>
      <td>5.555e-06</td>
      <td>0.005</td>
      <td>79</td>
      <td>GluR1𝐗30 ⇌ GluR1𝐘30 + PP2BCaMCa4</td>
      <td>0.002</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>LR + Gs ⇌ LRGs</td>
      <td>6e-07</td>
      <td>1e-06</td>
      <td>80</td>
      <td>GluR1𝐗31 ⇌ GluR1_memb𝐗31</td>
      <td>2e-07</td>
      <td>8e-07</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Gs + R ⇌ GsR</td>
      <td>4e-08</td>
      <td>3e-07</td>
      <td>81</td>
      <td>GluR1_S845𝐗32</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12</td>
      <td>GsR + L ⇌ LRGs</td>
      <td>2.5e-06</td>
      <td>0.0005</td>
      <td></td>
      <td>⇌ GluR1_memb_S845𝐗32</td>
      <td>3.28e-05</td>
      <td>8e-06</td>
    </tr>
    <tr>
      <td>13</td>
      <td>LRGs ⇌ LRGsbg + GsaGTP</td>
      <td>0.02</td>
      <td>0.0</td>
      <td>82</td>
      <td>PDE1 + CaMCa4 ⇌ PDE1CaMCa4</td>
      <td>0.0001</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>14</td>
      <td>LRGsbg ⇌ LR + Gsbg</td>
      <td>0.08</td>
      <td>0.0</td>
      <td>83</td>
      <td>PDE1CaMCa4 + cAMP ⇌ PDE1CaMCa4cAMP</td>
      <td>4.6e-06</td>
      <td>0.044</td>
    </tr>
    <tr>
      <td>15</td>
      <td>𝐗1 + PKAc ⇌ PKAc𝐗1</td>
      <td>8e-07</td>
      <td>0.00448</td>
      <td>84</td>
      <td>PDE1CaMCa4cAMP ⇌ PDE1CaMCa4 + AMP</td>
      <td>0.011</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>16</td>
      <td>PKAc𝐗2 ⇌ p𝐗2 + PKAc</td>
      <td>0.001</td>
      <td>0.0</td>
      <td>85</td>
      <td>AMP ⇌ ATP</td>
      <td>0.001</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>17</td>
      <td>ppLR + PKAc ⇌ PKAcppLR</td>
      <td>1.712e-05</td>
      <td>0.00448</td>
      <td>86</td>
      <td>PDE4 + cAMP ⇌ PDE4cAMP</td>
      <td>2.166e-05</td>
      <td>0.0034656</td>
    </tr>
    <tr>
      <td>18</td>
      <td>pppLR + PKAc ⇌ PKAcpppLR</td>
      <td>0.001712</td>
      <td>0.00448</td>
      <td>87</td>
      <td>PDE4cAMP ⇌ PDE4 + AMP</td>
      <td>0.017233</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>19</td>
      <td>ppppLR + Gi ⇌ ppppLRGi</td>
      <td>0.00015</td>
      <td>0.00025</td>
      <td>88</td>
      <td>𝐗33 + 𝐘33 ⇌ PKAc 𝐙33</td>
      <td>2.5e-07</td>
      <td>8e-05</td>
    </tr>
    <tr>
      <td>20</td>
      <td>ppppLRGi ⇌ ppppLRGibg + GiaGTP</td>
      <td>0.000125</td>
      <td>0.0</td>
      <td>89</td>
      <td>PKAc𝐗34 ⇌ pPDE4𝐘34 + PKAc</td>
      <td>2e-05</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>21</td>
      <td>pppp𝐗3 ⇌ pppp𝐘3 + Gibg</td>
      <td>0.001</td>
      <td>0.0</td>
      <td>90</td>
      <td>pPDE4 ⇌ PDE4</td>
      <td>2.5e-06</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>22</td>
      <td>p 𝐗4 ⇌ 𝐗4</td>
      <td>2.5e-06</td>
      <td>0.0</td>
      <td>91</td>
      <td>pPDE4 + cAMP ⇌ pPDE4cAMP</td>
      <td>0.000433175</td>
      <td>0.069308</td>
    </tr>
    <tr>
      <td>23</td>
      <td>pp𝐗5 ⇌ p𝐗5</td>
      <td>2.5e-06</td>
      <td>0.0</td>
      <td>92</td>
      <td>pPDE4cAMP ⇌ pPDE4 + AMP</td>
      <td>0.3446674</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>24</td>
      <td>R + PKAc ⇌ PKAcR</td>
      <td>4e-08</td>
      <td>0.00448</td>
      <td>93</td>
      <td>PKAcAMP4 ⇌ PKAr + 2*PKAc</td>
      <td>0.00024</td>
      <td>2.55e-05</td>
    </tr>
    <tr>
      <td>25</td>
      <td>pR + PKAc ⇌ PKAcpR</td>
      <td>4e-07</td>
      <td>0.00448</td>
      <td>94</td>
      <td>Ca + fixedbuffer ⇌ fixedbufferCa</td>
      <td>0.0004</td>
      <td>20.0</td>
    </tr>
    <tr>
      <td>26</td>
      <td>ppR + PKAc ⇌ PKAcppR</td>
      <td>4e-06</td>
      <td>0.00448</td>
      <td>95</td>
      <td>Glu ⇌ GluOut</td>
      <td>0.0005</td>
      <td>2e-10</td>
    </tr>
    <tr>
      <td>27</td>
      <td>pppR + PKAc ⇌ PKAcpppR</td>
      <td>0.0004</td>
      <td>0.00448</td>
      <td>96</td>
      <td>Ca + PLC ⇌ PLCCa</td>
      <td>4e-07</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>28</td>
      <td>ppppR + Gi ⇌ ppppRGi</td>
      <td>7.5e-05</td>
      <td>0.000125</td>
      <td>97</td>
      <td>GqaGTP + PLC ⇌ PLCGqaGTP</td>
      <td>7e-07</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>29</td>
      <td>ppppRGi ⇌ ppppRGibg + GiaGTP</td>
      <td>6.25e-05</td>
      <td>0.0</td>
      <td>98</td>
      <td>Ca + PLCGqaGTP ⇌ PLCCaGqaGTP</td>
      <td>8e-05</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>30</td>
      <td>GsaGTP ⇌ GsaGDP</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>99</td>
      <td>GqaGTP + PLCCa ⇌ PLCCaGqaGTP</td>
      <td>0.0001</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>31</td>
      <td>GsaGDP + Gsbg ⇌ Gs</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>100</td>
      <td>PLCCa + Pip2 ⇌ PLCCaPip2</td>
      <td>3e-08</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>32</td>
      <td>GiaGTP ⇌ GiaGDP</td>
      <td>0.000125</td>
      <td>0.0</td>
      <td>101</td>
      <td>PLCCaPip2 ⇌ PLCCaDAG + Ip3</td>
      <td>0.0003</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>33</td>
      <td>GiaGDP + Gibg ⇌ Gi</td>
      <td>0.00125</td>
      <td>0.0</td>
      <td>102</td>
      <td>PLCCaDAG ⇌ PLCCa + DAG</td>
      <td>0.2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>34</td>
      <td>GsaGTP + AC1 ⇌ AC1GsaGTP</td>
      <td>3.85e-05</td>
      <td>0.01</td>
      <td>103</td>
      <td>PLCCaGqaGTP + Pip2 ⇌ PLCCaGqaGTPPip2</td>
      <td>1.5e-05</td>
      <td>0.075</td>
    </tr>
    <tr>
      <td>35</td>
      <td>AC1 𝐗6 + CaMCa4 ⇌ AC1 𝐙6</td>
      <td>6e-06</td>
      <td>0.0009</td>
      <td>104</td>
      <td>PLCCaGqaGTPPip2 ⇌ PLCCaGqaGTPDAG + Ip3</td>
      <td>0.25</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>36</td>
      <td>𝐗7 + ATP ⇌ 𝐙7</td>
      <td>1e-05</td>
      <td>2.273</td>
      <td>105</td>
      <td>PLCCaGqaGTPDAG ⇌ PLCCaGqaGTP + DAG</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>37</td>
      <td>AC1GsaGTPCaMCa4ATP</td>
      <td></td>
      <td></td>
      <td>106</td>
      <td>Ip3degrad + PIkinase ⇌ Ip3degPIk</td>
      <td>2e-06</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td></td>
      <td>⇌ cAMP + AC1GsaGTPCaMCa4</td>
      <td>0.02842</td>
      <td>0.0</td>
      <td>107</td>
      <td>Ip3degPIk ⇌ PIkinase + Pip2</td>
      <td>0.001</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>38</td>
      <td>𝐗8 + 𝐘8 ⇌ AC1Gsa𝐙8</td>
      <td>6.25e-05</td>
      <td>0.01</td>
      <td>108</td>
      <td>PLC𝐗35 ⇌ PLC𝐘35 + GqaGDP</td>
      <td>0.012</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>39</td>
      <td>𝐗9 ⇌ cAMP + 𝐙9</td>
      <td>0.002842</td>
      <td>0.0</td>
      <td>109</td>
      <td>GqaGTP ⇌ GqaGDP</td>
      <td>0.001</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>40</td>
      <td>AC1GiaGTPCaMCa4ATP</td>
      <td></td>
      <td></td>
      <td>110</td>
      <td>GqaGDP ⇌ Gqabg</td>
      <td>0.01</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td></td>
      <td>⇌ cAMP + AC1GiaGTPCaMCa4</td>
      <td>0.0005684</td>
      <td>0.0</td>
      <td>111</td>
      <td>Ca + DGL ⇌ CaDGL</td>
      <td>0.000125</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>41</td>
      <td>AC1CaMCa4ATP ⇌ cAMP + AC1CaMCa4</td>
      <td>0.005684</td>
      <td>0.0</td>
      <td>112</td>
      <td>DAG + CaDGL ⇌ DAGCaDGL</td>
      <td>5e-07</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>42</td>
      <td>AC8 + CaMCa4 ⇌ AC8CaMCa4</td>
      <td>1.25e-06</td>
      <td>0.001</td>
      <td>113</td>
      <td>DAGCaDGL ⇌ CaDGL + 2AG</td>
      <td>0.00025</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>43</td>
      <td>CaM + 2*Ca ⇌ CaMCa2</td>
      <td>1.7e-08</td>
      <td>0.035</td>
      <td>114</td>
      <td>Ip3 ⇌ Ip3degrad</td>
      <td>0.01</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>44</td>
      <td>𝐗10 + Ca ⇌ 𝐙10</td>
      <td>1.4e-05</td>
      <td>0.228</td>
      <td>115</td>
      <td>2AG ⇌ 2AGdegrad</td>
      <td>0.005</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>45</td>
      <td>𝐗11 + Ca ⇌ 𝐙11</td>
      <td>2.6e-05</td>
      <td>0.064</td>
      <td>116</td>
      <td>DAG + DAGK ⇌ DAGKdag</td>
      <td>7e-08</td>
      <td>0.0008</td>
    </tr>
    <tr>
      <td>46</td>
      <td>CaM + Ng ⇌ NgCaM</td>
      <td>2.8e-05</td>
      <td>0.036</td>
      <td>117</td>
      <td>DAGKdag ⇌ DAGK + PA</td>
      <td>0.0002</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>47</td>
      <td>CaM + PP2B ⇌ PP2BCaM</td>
      <td>4.6e-06</td>
      <td>1.2e-06</td>
      <td>118</td>
      <td>Ca + PKC ⇌ PKCCa</td>
      <td>1.33e-05</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>48</td>
      <td>CaMCa𝐗12 + PP2B ⇌ PP2B𝐙12</td>
      <td>4.6e-05</td>
      <td>1.2e-06</td>
      <td>119</td>
      <td>PKCCa + DAG ⇌ PKCt</td>
      <td>1.5e-08</td>
      <td>0.00015</td>
    </tr>
    <tr>
      <td>49</td>
      <td>PP2BCaM + 2*Ca ⇌ PP2BCaMCa2</td>
      <td>1.7e-07</td>
      <td>0.35</td>
      <td>120</td>
      <td>Glu + MGluR ⇌ MGluR_Glu</td>
      <td>1.68e-08</td>
      <td>0.0001</td>
    </tr>
    <tr>
      <td>50</td>
      <td>CaMCa4 + CK ⇌ CKCaMCa4</td>
      <td>1e-05</td>
      <td>0.003</td>
      <td>121</td>
      <td>MGluR_Glu ⇌ MGluR_Glu_desens</td>
      <td>6.25e-05</td>
      <td>1e-06</td>
    </tr>
    <tr>
      <td>51</td>
      <td>2*CKCaMCa4 ⇌ Complex</td>
      <td>1e-07</td>
      <td>0.01</td>
      <td>122</td>
      <td>Gqabg + MGluR_Glu ⇌ MGluR_Gqabg_Glu</td>
      <td>9e-06</td>
      <td>0.00136</td>
    </tr>
    <tr>
      <td>52</td>
      <td>CKpCaMCa4 + CKCaMCa4 ⇌ pComplex</td>
      <td>1e-07</td>
      <td>0.01</td>
      <td>123</td>
      <td>MGluR_Gqabg_Glu ⇌ GqaGTP + MGluR_Glu</td>
      <td>0.0015</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>53</td>
      <td>CK𝐗13 + Complex ⇌ CK𝐗13 + pComplex</td>
      <td>1e-07</td>
      <td>0.0</td>
      <td>124</td>
      <td>GluR2𝐗36 + PKC𝐘36 ⇌ GluR2𝐙36</td>
      <td>4e-07</td>
      <td>0.0008</td>
    </tr>
    <tr>
      <td>54</td>
      <td>2*Complex ⇌ Complex + pComplex</td>
      <td>1e-05</td>
      <td>0.0</td>
      <td>125</td>
      <td>GluR2𝐗37 ⇌ GluR2𝐘37 + PKC𝐙37</td>
      <td>0.0047</td>
      <td>0</td>
    </tr>
    <tr>
      <td>55</td>
      <td>Complex + pComplex ⇌ 2*pComplex</td>
      <td>3e-05</td>
      <td>0.0</td>
      <td>126</td>
      <td>GluR2𝐗38 + PP2A ⇌ GluR2𝐙38</td>
      <td>5e-07</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>56</td>
      <td>CKpCaMCa4 ⇌ CaMCa4 + CKp</td>
      <td>8e-07</td>
      <td>1e-05</td>
      <td>127</td>
      <td>GluR2𝐗39 ⇌ GluR2𝐘39 + PP2A</td>
      <td>0.00015</td>
      <td>0</td>
    </tr>
    <tr>
      <td>57</td>
      <td>CKp𝐗14 + PP1 ⇌ CKp𝐙14</td>
      <td>4e-09</td>
      <td>0.00034</td>
      <td>128</td>
      <td>GluR2𝐗40 ⇌ GluR2_memb𝐗40</td>
      <td>0.00024545</td>
      <td>0.0003</td>
    </tr>
    <tr>
      <td>58</td>
      <td>CKp𝐗15 ⇌ PP1 + CK𝐙15</td>
      <td>8.6e-05</td>
      <td>0.0</td>
      <td>129</td>
      <td>GluR2_S880𝐗41 ⇌ GluR2_memb_S880𝐗41</td>
      <td>0.0055</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>59</td>
      <td>PKA + 4*cAMP ⇌ PKAcAMP4</td>
      <td>1.6e-15</td>
      <td>6e-05</td>
      <td>130</td>
      <td>ACh + M1R ⇌ AChM1R</td>
      <td>9.5e-08</td>
      <td>0.0025</td>
    </tr>
    <tr>
      <td>60</td>
      <td>Epac1 + cAMP ⇌ Epac1cAMP</td>
      <td>3.1e-08</td>
      <td>6.51e-05</td>
      <td>131</td>
      <td>Gqabg + AChM1R ⇌ AChM1RGq</td>
      <td>2.4e-05</td>
      <td>0.00042</td>
    </tr>
    <tr>
      <td>61</td>
      <td>I1 + PKAc ⇌ I1PKAc</td>
      <td>1.4e-06</td>
      <td>0.0056</td>
      <td>132</td>
      <td>Gqabg + M1R ⇌ M1RGq</td>
      <td>5.76e-07</td>
      <td>0.00042</td>
    </tr>
    <tr>
      <td>62</td>
      <td>I1PKAc ⇌ Ip35 + PKAc</td>
      <td>0.0014</td>
      <td>0.0</td>
      <td>133</td>
      <td>ACh + M1RGq ⇌ AChM1RGq</td>
      <td>3.96e-06</td>
      <td>0.0025</td>
    </tr>
    <tr>
      <td>63</td>
      <td>Ip35 + PP1 ⇌ Ip35PP1</td>
      <td>1e-06</td>
      <td>1.1e-06</td>
      <td>134</td>
      <td>AChM1RGq ⇌ GqaGTP + AChM1R</td>
      <td>0.0005</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>64</td>
      <td>Ip35𝐗16 + PP2BCaMCa4 ⇌ Ip35PP2B𝐙16</td>
      <td>9.625e-05</td>
      <td>0.33</td>
      <td>135</td>
      <td>ACh ⇌</td>
      <td>0.006</td>
      <td>0</td>
    </tr>
    <tr>
      <td>65</td>
      <td>Ip35PP2B𝐗17 ⇌ I1 + PP2B𝐗17</td>
      <td>0.055</td>
      <td>0.0</td>
      <td>136</td>
      <td>Ca + PLA2 ⇌ CaPLA2</td>
      <td>6e-07</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>66</td>
      <td>PP1PP2BCaMCa4 ⇌ PP1 + PP2BCaMCa4</td>
      <td>0.0015</td>
      <td>0.0</td>
      <td>137</td>
      <td>CaPLA2 + Pip2 ⇌ CaPLA2Pip2</td>
      <td>2.2e-05</td>
      <td>0.444</td>
    </tr>
    <tr>
      <td>67</td>
      <td>GluR1𝐗18 + PKAc ⇌ GluR1𝐙18</td>
      <td>4.02e-06</td>
      <td>0.024</td>
      <td>138</td>
      <td>CaPLA2Pip2 ⇌ CaPLA2 + AA</td>
      <td>0.111</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>68</td>
      <td>GluR1𝐗19 ⇌ GluR1𝐘19 + PKAc</td>
      <td>0.006</td>
      <td>0</td>
      <td>139</td>
      <td>AA ⇌ Pip2</td>
      <td>0.001</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>69</td>
      <td>GluR1𝐗20 + CK𝐘20 ⇌ GluR1𝐙20</td>
      <td>2.224e-08</td>
      <td>0.0016</td>
      <td>140</td>
      <td>PKCt + AA ⇌ PKCp</td>
      <td>5e-09</td>
      <td>1.76e-07</td>
    </tr>
    <tr>
      <td>70</td>
      <td>GluR1𝐗21 ⇌ GluR1𝐘21 + CK𝐙21</td>
      <td>0.0004</td>
      <td>0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 4.**
 List of initial concentrations of molecular species.All non-mentioned species have an initial concentration of 0 nM.


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th></th>
      <th>Conc. (nM)</th>
      <th>Species</th>
      <th></th>
      <th>Conc. (nM)</th>
      <th>Species</th>
      <th></th>
      <th>Conc. (nM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CaOut</td>
      <td>extracell. Ca2+</td>
      <td>1900000</td>
      <td>AMP</td>
      <td>adenosine monophosphate</td>
      <td>980</td>
      <td>Pip2</td>
      <td>phosphatidylinositol 4,5-bisphosphate</td>
      <td>24000</td>
    </tr>
    <tr>
      <td>Leak</td>
      <td>leak channels</td>
      <td>2000</td>
      <td>Ng</td>
      <td>neurogranin</td>
      <td>20000</td>
      <td>PIkinase</td>
      <td>phosphatidylinositol kinase</td>
      <td>290</td>
    </tr>
    <tr>
      <td>Calbin</td>
      <td>calbindin</td>
      <td>150000</td>
      <td>CaM</td>
      <td>calmodulin</td>
      <td>60000</td>
      <td>Ip3degPIk</td>
      <td>Ip3-bound PI kinase</td>
      <td>400</td>
    </tr>
    <tr>
      <td>CalbinC</td>
      <td>Ca2+-bound calbindin</td>
      <td>15000</td>
      <td>PP2B</td>
      <td>protein phosphatase 2B</td>
      <td>2300</td>
      <td>PKC</td>
      <td>protein kinase C</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>LOut</td>
      <td>extracell. β-adr. ligand</td>
      <td>2500000</td>
      <td>CK</td>
      <td>CaMKII</td>
      <td>23000</td>
      <td>DAG</td>
      <td>diacylglycerol</td>
      <td>90</td>
    </tr>
    <tr>
      <td>Epac1</td>
      <td>Epac1</td>
      <td>500</td>
      <td>PKA</td>
      <td>protein kinase A</td>
      <td>6400</td>
      <td>DAGK</td>
      <td>DAG kinase</td>
      <td>300</td>
    </tr>
    <tr>
      <td>PMCA</td>
      <td>Ca2+ pump</td>
      <td>22000</td>
      <td>I1</td>
      <td>inhibitor-1</td>
      <td>2200</td>
      <td>DGL</td>
      <td>DAG lipase</td>
      <td>1600</td>
    </tr>
    <tr>
      <td>NCX</td>
      <td>Ca2+ exchanger</td>
      <td>540000</td>
      <td>PP1</td>
      <td>protein phosphatase 1</td>
      <td>1600</td>
      <td>CaDGL</td>
      <td>Ca2+-bound DAG lipase</td>
      <td>250</td>
    </tr>
    <tr>
      <td>L</td>
      <td>β-adrenergic ligand</td>
      <td>10</td>
      <td>GluR1</td>
      <td>AMPAR subunit type 1</td>
      <td>180</td>
      <td>DAGCaDGL</td>
      <td>Ca2+-and DAG-bound DAG lipase</td>
      <td>90</td>
    </tr>
    <tr>
      <td>R</td>
      <td>β-adrenergic receptor</td>
      <td>1600</td>
      <td>GluR1_memb</td>
      <td>membrane-inserted GluR1</td>
      <td>90</td>
      <td>Ip3degrad</td>
      <td>degraded Ip3</td>
      <td>600</td>
    </tr>
    <tr>
      <td>Gs</td>
      <td>S-type G-protein</td>
      <td>13000</td>
      <td>PDE4</td>
      <td>phosphodiesterase type 4</td>
      <td>670</td>
      <td>GluR2</td>
      <td>AMPAR subunit type 2</td>
      <td>14</td>
    </tr>
    <tr>
      <td>Gi</td>
      <td>I-type G-protein</td>
      <td>2600</td>
      <td>fixedbuffer</td>
      <td>immobile buffer</td>
      <td>500000</td>
      <td>GluR2_memb</td>
      <td>membrane-inserted GluR2</td>
      <td>256</td>
    </tr>
    <tr>
      <td>AC1</td>
      <td>adenylyl cyclase type 1</td>
      <td>430.0</td>
      <td>mGluR</td>
      <td>metab. glutamate receptor</td>
      <td>800</td>
      <td>PP2A</td>
      <td>protein phosphatase 2A</td>
      <td>500</td>
    </tr>
    <tr>
      <td>ATP</td>
      <td>adenosine triphosphate</td>
      <td>2000000</td>
      <td>GluOut</td>
      <td>extracell. glutamate</td>
      <td>1000000</td>
      <td>M1R</td>
      <td>acetylcholine receptor M1</td>
      <td>450</td>
    </tr>
    <tr>
      <td>AC8</td>
      <td>adenylyl cyclase type 8</td>
      <td>370</td>
      <td>Gqabg</td>
      <td>Q-type G-protein</td>
      <td>1400</td>
      <td>PLA2</td>
      <td>phospholipase A2</td>
      <td>1000</td>
    </tr>
    <tr>
      <td>PDE1</td>
      <td>phosphodiesterase type 1</td>
      <td>12000</td>
      <td>PLC</td>
      <td>phospholipase C</td>
      <td>250</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Throughout the work, we simulated the signalling pathways in a single compartment representing a dendritic spine of size 0.5 μm3. In reality, some of the molecular species are prevalently present in the cytosol, some attached to the membrane, some in the extracellular medium in an immediate vicinity to the membrane, and others outside the cell further away from the synaptic cleft (free in the extracellular medium or sequestered to other cells). As commonly done in the field, we solved this problem by introducing species that represent a molecular species confined in a particular location: reactions 1–6 describe the extrusion of Ca2+ from the cytosol into the extracellular medium, reactions 8, 95, and 135 describe the escape of ligands from the vicinity of the synapse, and reactions 80–81 and 128–129 for the translocation of the AMPARs to/from the membrane (Table 3). All stimulations start after 4040 s of simulation without inputs, which is sufficient for attaining a steady state for all species (Figure 11—figure supplement 1).

### Statistical model for numbers of AMPAR tetramers at the membrane and the total synaptic conductance

AMPARs have different conductances depending on their subunit composition and phosphorylation state (Oh and Derkach, 2005), but it is challenging to take this into account in models that include a large number of receptor subunits. In our model, AMPAR subunits GluR1 and GluR2 can be in one of 21 or five states, respectively, when counting all the different phosphorylation states and bonds with other molecules (Table 3), which leads to 284 possible types of tetramers. This makes it virtually impossible to model the dynamics of AMPAR tetramer assembly using the mass-action law-based approach where the concentration of each type of species is monitored (Michalski and Loew, 2012). To avoid this problem, we used a statistical model that estimated the numbers and types of different types of AMPAR tetramers given the numbers of GluR1 and GluR2 subunits located at the membrane.

We assumed that the composition of AMPAR tetramers is random such that there is no preference of one type of subunit being more likely to bind with any other type of subunit. Thus, the probability of a tetramer being a GluR1 homomer without any S831-phosphorylated subunits is approximately

$$
p_{GluR1 homomer, non−phos.}=\frac{(N_{1}−N_{1,phos.}4)}{(N_{1}+N_{2}4)}≈\frac{(N_{1}−N_{1,phos.})^{4}}{(N_{1}+N_{2})^{4}}
$$

where N1 and N2 are the numbers of GluR1 and GluR2 subunits bound to the membrane, respectively, and $N_{1,phos.}$ is the number of S831-phosphorylated GluR1 subunits at the membrane (note that the $N_{1,phos.}$ subunits are included in all GluR1 subunits, that is, $N_{1,phos.}\leqN_{1}$). Accordingly, the probabilities of a tetramer being a GluR1 homomer with at least one S831-phosphorylated subunit, a GluR2 homomer, or a heteromer, are approximately:

$$
(2)rlp_{GluR1 homomer, phos.}=\frac{N_{1}^{4}−(N_{1}−N_{1,phos.})^{4}}{(N_{1}+N_{2})^{4}}(3)p_{GluR2 homomer}=\frac{N_{2}^{4}}{(N_{1}+N_{2})^{4}}(4)p_{heteromer}=1−\frac{N_{1}^{4}}{(N_{1}+N_{2})^{4}}−\frac{N_{2}^{4}}{(N_{1}+N_{2})^{4}}.
$$

The number of membrane-bound tetramers that the N1 GluR1 subunits and N2 GluR2 subunits at the membrane can form is $\frac{N_{1}+N_{2}}{4}$. Here, we ignore the unpaired subunits by estimating that $\frac{N_{1}+N_{2}}{4}≈⌊\frac{N_{1}+N_{2}}{4}⌋$ — we also disregard the states of the non-membrane-bound subunits as they are not assumed to contribute to the synaptic conductance. This gives us approximate values for expected numbers of different types of tetramers on the membrane:

$$
N_{GluR1 homomer, non−phos.}=\frac{N_{1}+N_{2}}{4}p_{GluR1 homomer, non−phos.}N_{GluR1 homomer, phos.}=\frac{N_{1}+N_{2}}{4}p_{GluR1 homomer, phos.}N_{GluR2 homomer}=\frac{N_{1}+N_{2}}{4}p_{GluR2 homomer}N_{heteromer}=\frac{N_{1}+N_{2}}{4}p_{heteromer}
$$

These estimates allow us to determine the total maximal synaptic conductance as the sum of the numbers of these tetramers multiplied with the corresponding single-channel conductances:

$$
g_{syn}=12.4pS\timesN_{GluR1 homomer, non−phos.}+18.9pS\timesN_{GluR1 homomer, phos.}+2.2pS\timesN_{GluR2 homomer}+2.5pS\timesN_{heteromer}.
$$

The single-channel conductance values 12.4 pS, 18.9 pS, 2.2 pS, and 2.5 pS are taken from experimental data (Oh and Derkach, 2005).

### Modelling the Ca2+ inputs and neuromodulatory inputs

We modelled the neurotransmission to the post-synaptic spine as fluxes of Ca2+ ions, β-adrenergic ligand, glutamate, and acetylcholine (labelled as Ca, L, Glu, and ACh, respectively, in Table 3). We used various stimulation paradigms: In sections 'Ca2+ activates multiple pathways that regulate the post-synaptic plasticity in cortical PCs' and 'The model predicts multimodal, protein concentration- and neuromodulation-dependent rules of plasticity', long-lasting, single pulses of input species were applied. In sections 'High-frequency stimulation (HFS) causes LTP and low-frequency stimulation (LFS) causes LTD in GluR1-GluR2-balanced synapses' and 'A parametric analysis confirms the robustness of the model', we used the following repeated stimulus protocols: HFS — 100 pulses of Ca2+ (3 ms), repeated at 100 Hz; 4xHFS — 4 trains of HFS, separated by 3 s of quiescence; LFS — 900 pulses of Ca2+ (3 ms), repeated at 5 Hz. Unless otherwise stated, each Ca2+ pulse was accompanied by a 3 ms pulse of β-adrenergic ligand, glutamate, and acetylcholine. The activation of cholinergic and noradrenergic terminals by electrical stimulation is supported by experimental data in, e.g., slices of mouse prefrontal cortex (Mundorf et al., 2001). In section 'The model flexibly reproduces data from various cortical LTP/LTD experiments', the same approach was used, but the frequencies and numbers of repetitions of the inputs were taken from the experiments (see Table 2).

In section 'Paired pre- and post-synaptic stimulation induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses' (and Figure 3—figure supplement 3 of section 'High-frequency stimulation (HFS) causes LTP and low-frequency stimulation (LFS) causes LTD in GluR1-GluR2-balanced synapses'), we used a multicompartmental model of a layer 2/3 pyramidal cell (Markram et al., 2015) (L23_PC_cADpyr229_1) to determine the amplitudes and time courses of the Ca2+ inputs conducted by NMDARs when different stimulus patterns were applied. This model included the fast Na+ current $I_{Na,t}$, Shaw-related K+ current $I_{Kv3⁢.1}$, muscarinic K+ current $I_{m}$, and hyperpolarization-activated cyclic nucleotide-gated current $I_{HCN}$ in the apical dendrite. The axo-somatic region contained all these (except for $I_{m}$) as well as the low and high-voltage activated Ca2+ currents $I_{CaLVA}$ and $I_{CaLVA}$, the small-conductance Ca2+-dependent K+ current $I_{SK}$, the transient K+ current $I_{K,t}$, and the persistent Na+ and K+ currents $I_{Na,p}$ and $I_{K,p}$ in the axo-somatic region (Markram et al., 2015). We placed 10 post-synaptic spines, consisting of a 0.5 μm long and 0.1 μm thick neck and a 0.4 μm long and 0.4 μm thick head, to the proximal apical dendrite (250–300 μm from the soma). For an analysis of the effects of synapse location on Ca2+ flux and plasticity in cortical pyramidal cells, see Ebner et al., 2019. Each spine was equipped with the AMPA–NMDA synapse model of Hay and Segev, 2015 using the NMDA gating mechanism of Spruston et al., 1995 and an adjustment in the pre-synaptic resource update (Mäki-Marttunen et al., 2019). The ten synapses were synchronously stimulated but the glutamate release was probabilistic, the release events at different synapses being independent of each other as in Hay and Segev, 2015). We set the maximal AMPAR conductance to 0.001 μS, a value typically used in computational neuron models. We set the maximal conductance of NMDARs to 0.0032 μS to compensate for the lack of the slow component in the model of the NMDA current (Markram et al., 2015) — a value significantly smaller or larger than this abolished the LTP or LTD, respectively, in our STDP model, while the AMPAR conductance was a less crucial parameter (Figure 11—figure supplement 2).We estimated the numbers of Ca2+ ions entering into the post-synaptic spine across time, and used these numbers as the input to the biochemical model. In section 'Paired pre- and post-synaptic stimulation induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses', following the experiments of Seol et al., 2007, we used extracellular [Mg2+] of 1.0 mM and a 1 Hz pre-synaptic stimulation, where each pulse was paired with a burst of post-synaptic stimulus currents (Seol et al., 2007). For Figure 3—figure supplement 3 of section 'High-frequency stimulation (HFS) causes LTP and low-frequency stimulation (LFS) causes LTD in GluR1-GluR2-balanced synapses', following the experiments of Heusler et al., 2000 we used [Mg2+] of 1.3 mM and solely pre-synaptic stimulation of one of the two stimulus protocols: 6xHFSt — 10 bursts of 4 pulses (at 100 Hz), repeated every 100 ms, and the whole train repeated 6 times every 10 s; LFS-1Hz — 1800 pulses delivered at a frequency of 1 Hz.

The effects of LTP/LTD on the size of Ca2+ inputs were not considered in this work.

### Parameter alterations and model fitting

In sections 'The model predicts multimodal, protein concentration- and neuromodulation-dependent rules of plasticity' and 'The model flexibly reproduces data from various cortical LTP/LTD experiments', we altered the initial concentrations of many proteins to explore the parameter space or to perform model fitting. We chose to fit protein concentrations instead of reaction rates, since the reaction rates can be considered to be the same across cell types while the protein expression is known to be cell-type and age-dependent. This is analogous to fitting maximal conductances that correlate with ion-channel densities in Hodgkin-Huxley-type models instead of the ion-channel activation and inactivation curve parameters as is usually done in the fitting of biophysically detailed neuron models. The concentrations of upstream PKA-pathway proteins R (β-adrenergic receptor), Gs, AC1, and AC8 were varied in proportion using a factor parameter $f_{PKA}\in[0,2]$, and, likewise, the concentrations of upstream PKC-pathway proteins mGluR, M1, Gq, and PLC using a factor parameter $f_{PKC}\in[0,2]$. Furthermore, in section 'The model flexibly reproduces data from various cortical LTP/LTD experiments', CaM and CaMKII were altered in proportion by a factor $f_{CaMKII}\in[0,2]$, phosphatases PP1 and PP2B by a factor $f_{PP}\in[0,2]$, and phosphodiesterases PDE1 and PDE4 by a factor $f_{PDE}\in[0,2]$. In both sections, the rapidity of Ca2+ extrusion was varied by altering the concentration of NCX, and in section 'The model flexibly reproduces data from various cortical LTP/LTD experiments', the concentrations of PKA and PKC were varied in addition to the upstream proteins — these concentrations were varied within the interval from 0 to double the original value. For the multi-objective optimisation in section 'The model flexibly reproduces data from various cortical LTP/LTD experiments', we used the Python implementation (published by the authors of Bahl et al., 2012) of the non-dominated sorting genetic algorithm II (NSGA-II) (Deb et al., 2002) with population size 1000. To restrict to physiologically realistic Ca2+ dynamics, we disregarded the data where free Ca2+ concentrations rose above 2 μM for one or more levels of Ca2+ input in section 'The model predicts multimodal, protein concentration- and neuromodulation-dependent rules of plasticity'. In a similar manner, in section 'The model flexibly reproduces data from various cortical LTP/LTD experiments', we introduced an objective function that penalised parameter sets that produced Ca2+ transients larger than 2 μM.

### Simulation software and code accessibility

For deterministic simulations of intracellular signalling, we used the NEURON simulator with the reaction-diffusion (RxD) extension (McDougal et al., 2013). For stochastic simulations, we used NeuroRD software (https://github.com/neurord). In both types of simulations, we used adaptive time-step integration methods. The NEURON simulator was also used for simulating the multicompartmental model of layer 2/3 pyramidal cell in section 'Paired pre- and post-synaptic stimulation induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses'. The full model along with the fitting and data-analysis algorithms (Python scripts) that were used in this study are publicly available in ModelDB at http://modeldb.yale.edu/260971.
