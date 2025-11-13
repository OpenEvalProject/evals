# T2N as a new tool for robust electrophysiological modeling demonstrated for mature and adult-born dentate granule cells

## Authors

- Marcel Beining<sup>1</sup> ([ORCID: 0000-0002-6577-2648](https://orcid.org/0000-0002-6577-2648)) †
- Lucas Alberto Mongiat<sup>5</sup>
- Stephan Wolfgang Schwarzacher<sup>3</sup>
- Hermann Cuntz<sup>1</sup> ([ORCID: 0000-0001-5445-0507](https://orcid.org/0000-0001-5445-0507)) †
- Peter Jedlicka<sup>3</sup> ([ORCID: 0000-0001-6571-5742](https://orcid.org/0000-0001-6571-5742))

### Affiliations

1. Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Frankfurt Germany
2. Frankfurt Institute for Advanced Studies Frankfurt Germany
3. Institute of Clinical Neuroanatomy, Neuroscience Center Goethe University Frankfurt Germany
4. Faculty of Biosciences Goethe University Frankfurt Germany
5. Instituto de Investigación en Biodiversidad y Medioambiente Universidad Nacional del Comahue-CONICET San Carlos de Bariloche Argentina

† Corresponding author

## Abstract

Compartmental models are the theoretical tool of choice for understanding single neuron computations. However, many models are incomplete, built ad hoc and require tuning for each novel condition rendering them of limited usability. Here, we present T2N, a powerful interface to control NEURON with Matlab and TREES toolbox, which supports generating models stable over a broad range of reconstructed and synthetic morphologies. We illustrate this for a novel, highly detailed active model of dentate granule cells (GCs) replicating a wide palette of experiments from various labs. By implementing known differences in ion channel composition and morphology, our model reproduces data from mouse or rat, mature or adult-born GCs as well as pharmacological interventions and epileptic conditions. This work sets a new benchmark for detailed compartmental modeling. T2N is suitable for creating robust models useful for large-scale networks that could lead to novel predictions. We discuss possible T2N application in degeneracy studies.

## Introduction

Traditionally, neurons have long been interpreted as passive integrators of input signals that fire action potentials when a threshold is reached (Knight, 1972). This paradigm has meanwhile changed as the output of neurons was shown to depend on many intrinsic cellular mechanisms (e.g. voltage-gated channels, dendritic architecture, synaptic plasticity, active dendrites, axon initial segment) indicating that single neuron computation is rather complex (Softky and Koch, 1993; Brunel et al., 2014; Volgushev, 2016). Consequently, detailed compartmental models have found their way into the set of tools for neuroscientists to understand, test, or predict mechanisms underlying neuronal function (de Schutter, 1994). Compartmental models are easy to manipulate and models of cellular mechanisms such as ion channels and synapses can be incorporated in arbitrary detail. Many recent models include reconstructed morphologies, which are often available online through specialized databases. As these models seem to become more and more realistic, the hope arises that one will soon be able to simulate entire circuits or even the brain itself simply by including more and more details (Markram, 2006, 2012; Markram et al., 2015; Hawrylycz et al., 2016). However, most published models behave poorly when used outside of the scope for which they were created. There are several reasons for this, such as bona fide adaptation of other models without knowing their limitations, too few target constraints because of using a low number of target parameters, no scientific rationale for setting the parameters, missing axon initial segments and a lack of data from pharmacology to fit and test the model’s individual components (Almog and Korngreen, 2016). Furthermore, model neurons often contain a mix of constraints from very different experimental conditions and animals, combined in sometimes inconsistent ways.

To make addressing these issues easier and to help build consistent and robust models, we developed T2N, a new software interface to control compartmental modeling package NEURON (Carnevale and Hines, 2006) using Matlab and the TREES toolbox (Cuntz et al., 2010; 2011). T2N enables to design detailed electrophysiology models on the basis not of single morphologies but rather on large datasets of reconstructed and synthetic morphologies. Such datasets have become more easily available from online databases such as NeuroMorpho.Org (Ascoli et al., 2007) and morphological modeling studies (Cuntz et al., 2008, 2010; Koene et al., 2009; Beining et al., 2017). In addition, ion channel models from newly available databases (Ranjan et al., 2011; Podlaski et al., 2016; McDougal et al., 2017) can be directly incorporated into T2N models to consider the many new insights from recent studies on neuronal electrophysiology and protein expression. Through this tool, we aimed here to create novel compartmental models that (1) are solely based on ion channel isoforms known to exist in the neurons of interest, (2) are robust over many different real and synthetic dendritic morphologies and (3) reproduce experimental results from various studies. Although T2N can be used to create robust models for any neuron type, in this work we focused on hippocampal dentate granule cells, which play a crucial role in learning and memory and exhibit the unique feature that they integrate into the adult hippocampal network as newborn neurons throughout life.

## Results

### Development of T2N

Our novel modeling framework for creating compartmental models with realistic biophysical properties in multiple morphologies is depicted in Figure 1. In this framework, our T2N package interfaces between TREES toolbox and NEURON. Since the TREES toolbox (Cuntz et al., 2010, 2011) is a recently established versatile tool for the analysis and modeling of 3D morphologies of dendrites, its coupling to NEURON (Carnevale and Hines, 2006) opens many new possibilities: (1) Biophysical mechanisms can be inserted not only into reconstructed but also into synthetic morphologies (e.g. created with TREES toolbox; Cuntz et al., 2010; Schneider et al., 2014; Beining et al., 2017; Platschek et al., 2016), which is important for the creation of a large set of realistic compartmental models capturing neuron-to-neuron variability of dendritic trees. For the insertion of biophysical mechanisms, T2N makes maximal use of region specifications that are available in TREES toolbox. Handling of section lists in NEURON is not necessary. (2) For a given set of biophysical mechanisms, T2N enables an easy and efficient switch among diverse morphologies from different species including any number of morphologies downloaded from for example, databases of reconstructed morphologies such as NeuroMorpho.Org. This facilitates the generalization of predictions from one dendritic tree type to other types and supports the search for universal principles valid for all dendritic morphologies. (3) T2N provides a simple and clear set up and controls NEURON compartmental models with a direct subsequent analysis with Matlab and the TREES toolbox allowing for any morphology related analyses. This is a unique feature of T2N. By generating stereotyped NEURON scripts, T2N enhances the readability and compatibility of the code. (4) Multiple simulations are run automatically in parallel on different cores without the need of rewriting the NEURON code. When activated, T2N also supports parallel NEURON (Migliore et al., 2006; Hines and Carnevale, 2008) and distributes cells automatically on a given amount of cores, thereby increasing the speed of large-scale network simulations drastically. (5) By connecting NEURON to Matlab, T2N makes it easier to plot and visualize the results of simulations and their analysis. In summary, by coupling morphological software and compartmental simulations, T2N provides users with powerful tools for an in-depth analysis of structure-function relationships in neurons. In the following, we show on the example of the dentate GC (see also Appendix 2) how to build a robust compartmental model using T2N.

![Figure 1.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig1-v3.jpg)

**Figure 1.:** T2N enables fast and simple incorporation of many diverse morphologies in compartmental simulations facilitating the search for morphologically robust biophysical models. (A) Illustration of T2N workflow. T2N allows for setting up a full compartmental model in Matlab by importing reconstructed or synthetic morphologies (orange; e.g. from NeuroMorpho.org) and by distributing subcellular channel mechanisms (green; mod files generated with NEURON’s NMODL or obtained from databases such as IonChannelGenealogy or Channelpedia). In addition, T2N enables setting up full simulation control by attaching stimulation and recording electrodes and specifying simulation conditions (e.g. stimulation protocols; blue). T2N then automatically produces stereotyped NEURON hoc code, initializes and runs simulations and returns recorded data in a structured output format (red). (B) A comparison of two example results in NEURON and T2N validates T2N simulation output. The orange script shows sample code for visualizing the output. Upper row: somatic voltage trace during a current injection. Lower row: membrane voltage at each dendrite location at a single time point. (C) Examples of using T2N for a simple and fast analysis and visualization of simulation results. (Code for creating the panels is shown in orange; code for the specific labels is omitted).

### T2N facilitates creation of compartmental models with detailed channel composition

T2N simplifies distributing dendritic, somatic and axonal ion channels in layer- or branch-specific manner. We illustrate this for an experimentally well constrained set of GC ion channels that we identified and modeled based on extensive literature search (see Appendix 2 for more details). Importantly, we included only those channel isoforms, which were described for GCs. Moreover, we carefully implemented compartment-specific distributions of the channels according to immunohistochemical labeling and light or electron microscopy as well as electrophysiological data (Table 1 and Figure 2A). Available tools of NEURON have limitations with regard to specifying layer- or branch-specific biophysical properties in a large dataset of morphologies. T2N makes it easy to insert ion channels in selected regions because it maps the nodes, branches and regions of the TREES toolbox (Cuntz et al., 2010, 2011) onto sections and segments in NEURON (see Tutorial 1 in Appendix 1). Of note, for cell types or compartments where channel expression data is not available, T2N can be used in a more exploratory manner, for example such as mapping model responses on single cell current sweep data.

![Figure 2.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig2-v3.jpg)

**Figure 2.:** (A) Ion channel composition of the mouse dentate granule cell (GC) model. Left: Passive and active ion channels with their specific distribution in six different regions: outer molecular layer (OML), middle molecular layer (MML), inner molecular layer (IML), soma, axon initial segment (AIS) and axon. The relative spatial distribution of voltage-dependent (V.-dep.) and calcium-dependent (Ca2+-dep.) channels is in line with an extensive amount of data from the literature (see Table 1, Appendix 2 and Materials and methods for details). Right: Three exemplary morphologies out of eight reconstructed mouse GCs (Schmidt-Hieber et al., 2007) used for compartmental modeling of mouse GCs. (B) Schematic of the morphological model used to generate synthetic mouse morphologies which is analogous to the previously reported rat model (Beining et al., 2017; see Material and methods there for details). Upper left: A synthetic 3D young dentate gyrus (DG) was created comprising different layers (GCL, IML, MML, and OML, from bottom to top). A soma (red dot) was defined and random target points (black dots) were distributed within a 3D cone (red dashed lines). These points were complemented by directed target points (gray dots) that were placed automatically between clusters of target points and the soma. Upper right: The target points were connected by a minimum spanning tree algorithm (Cuntz et al., 2010) and terminal dendritic segments shorter than 20 µm were pruned off (red segments, see Beining et al., 2017). Lower right: The young DG and the dendritic tree have been stretched to their mature size (see Beining et al., 2017 for more information). Lower left: Adding a somatic diameter profile, a synthetic axon, applying jittering and dendritic diameter taper (not shown for visualization purposes) to the dendrites results in realistic synthetic GC morphologies suitable for compartmental modeling. (C) Six out of 15 synthetic morphologies created by the morphological model and used for compartmental modeling with their anatomical borders (gray dashed lines). (D) General and layer-specific structural comparison of the reconstructed (blue, Schmidt-Hieber et al., 2007) and synthetic (green) mouse GC morphologies.

**Table 1.**
 Summary of all ion channel models and densities implemented in the mouse mature GC model.Categorial values of the ion channel expression profiles: 0 = not existent or very weak, 1 = weak, 2 = moderate, 3 = strong. Conductances [mS/cm²] for each ion channel used in the model are given in the gray fields.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Soma</th>
      <th>Axon</th>
      <th>AIS</th>
      <th>GCL</th>
      <th>IML</th>
      <th>MML</th>
      <th>OML</th>
      <th>Reference</th>
      <th>Ion channel model</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Nav 1.1 Nav 1.2 Nav 1.6</td>
      <td>3 0</td>
      <td>0 3</td>
      <td>0 3</td>
      <td>0 0</td>
      <td>0 0</td>
      <td>0 0</td>
      <td>0 0</td>
      <td>(Westenbroek et al., 1989; Schmidt-Hieber and Bischofberger, 2010)</td>
      <td rowspan="3">8-state model from (Schmidt-Hieber and Bischofberger, 2010). Inact. modified according to (Rush et al., 2005; Schmidt-Hieber and Bischofberger, 2010) (see text)</td>
    </tr>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>(Kress et al., 2010; Schmidt-Hieber and Bischofberger, 2010)</td>
    </tr>
    <tr>
      <td>88.128</td>
      <td>88.1280</td>
      <td>518.400</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">K2Ps (passive)</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td rowspan="2">(Lesage et al., 1997; Hervieu et al., 2001; Talley et al., 2001; Gabriel et al., 2002; Aller and Wisden, 2008; Yarishkin et al., 2014)</td>
      <td rowspan="2"></td>
    </tr>
    <tr>
      <td>0.014</td>
      <td>0.007</td>
      <td>0.007</td>
      <td>0.014</td>
      <td>0.014</td>
      <td>0.014</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td rowspan="2">Kir 2.x</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>(Karschin et al., 1996; Miyashita and Kubo, 1997; Stonehouse et al., 1999; Prüss et al., 2003)</td>
      <td rowspan="2">6-state model, modification see Appendix 2.</td>
    </tr>
    <tr>
      <td>0.1416</td>
      <td>0.0674</td>
      <td>0.0674</td>
      <td>0.1416</td>
      <td>0.1416</td>
      <td>0.1416</td>
      <td>0.1416</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">HCN1-3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>(Notomi and Shigemoto, 2004)</td>
      <td rowspan="2">2-state model, from (Stegen et al., 2012); activation −10 mV, added cAMP-sens. and slow comp. of act.</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>0.004</td>
      <td>0.004</td>
      <td>0.004</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Kv 1.1</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td rowspan="2">(Rhodes et al., 1997; Grosse et al., 2000; Monaghan et al., 2001)</td>
      <td rowspan="2">nh model from (Christie et al., 1989)</td>
    </tr>
    <tr>
      <td>-</td>
      <td>0.25</td>
      <td>0.25</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="2">Kv 1.4</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>(Rhodes et al., 1997; Cooper et al., 1998; Grosse et al., 2000; Monaghan et al., 2001)</td>
      <td rowspan="2">n4h model from (Wissmann et al., 2003)</td>
    </tr>
    <tr>
      <td>-</td>
      <td>1</td>
      <td>1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Kv 2.1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>(Rhodes et al., 1997; Murakoshi and Trimmer, 1999)</td>
      <td rowspan="2">mh model, fitted using (VanDongen et al., 1990; Kramer et al., 1998; Kerschensteiner and Stocker, 1999; McCrossan et al., 2003; Gordon et al., 2006)</td>
    </tr>
    <tr>
      <td>7.09</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Kv 3.3/3.4</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>(Weiser et al., 1994; Chang et al., 2007)</td>
      <td rowspan="2">mh model, fitted using (Rudy et al., 1991; Schröter et al., 1991; Rettig et al., 1992; Miera et al., 1992; Riazanski et al., 2001; Desai et al., 2008)</td>
    </tr>
    <tr>
      <td>-</td>
      <td>7.6562</td>
      <td>30.7813</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Kv 4.2/3 +KChIP/DPP6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td rowspan="2">(Rhodes et al., 2004; Zagha et al., 2005; Menegola and Trimmer, 2006)</td>
      <td rowspan="2">13-state model from (Barghaan et al., 2008); activation −20 mV according to (Barghaan et al., 2008; Figure S1A) and (Jerng et al., 1999; An et al., 2000; Bähring et al., 2001; Patel et al., 2004; Jerng et al., 2005; Rüschenschmidt et al., 2006; Kaulin et al., 2008; Kim et al., 2008)</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2.1750</td>
      <td>4.35</td>
      <td>4.35</td>
      <td>4.35</td>
    </tr>
    <tr>
      <td rowspan="2">Kv 7.2/3 (KCNQ2 and 3)</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>(Cooper et al., 2001; Klinger et al., 2011; Martinello et al., 2015)</td>
      <td rowspan="2">mh model from (Mateos-Aparicio et al., 2014) (η = 0.5, see Tab. S1 in that publication)</td>
    </tr>
    <tr>
      <td>-</td>
      <td>1.3400</td>
      <td>6.7000</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Cav 1.2 (L-type)</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>(Tippens et al., 2008; Leitch et al., 2009)</td>
      <td rowspan="2">mh1h2 model from GENESIS (Evans et al., 2013), added Ca2+-dep. inactivation (h2)</td>
    </tr>
    <tr>
      <td>0.0200</td>
      <td>-</td>
      <td>0.0100</td>
      <td>0.0100</td>
      <td>0.0400</td>
      <td>0.0400</td>
      <td>0.0400</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Cav 1.3</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>(Tippens et al., 2008; Leitch et al., 2009)</td>
      <td rowspan="2">mh1h2 model from GENESIS (Evans et al., 2013), added Ca2+-dep. inactivation, modified after (Bell et al., 2001; Koschak et al., 2001)</td>
    </tr>
    <tr>
      <td>0.0160</td>
      <td>0.0040</td>
      <td>0.0080</td>
      <td>0.0040</td>
      <td>0.0080</td>
      <td>0.0080</td>
      <td>0.0080</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Cav 2.1/2 (N-/P/Q-type)</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>(Day et al., 1996; Chung et al., 2001; Li et al., 2007; Xu et al., 2007; 2010)</td>
      <td rowspan="2">m²h model from (Fox et al., 1987); set inact. time constant to 100 ms according to (Fox et al., 1987; Huang et al., 2010)</td>
    </tr>
    <tr>
      <td>0.3000</td>
      <td>0.0500</td>
      <td>0.0500</td>
      <td>0.0500</td>
      <td>0.0500</td>
      <td>0.0500</td>
      <td>0.0500</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Cav 3.2 (T-type)</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>(Craig et al., 1999; McKay et al., 2006; Martinello et al., 2015)</td>
      <td rowspan="2">8-state model from (Burgess et al., 2002)</td>
    </tr>
    <tr>
      <td>0.0220</td>
      <td>0.0080</td>
      <td>0.0080</td>
      <td>0.0220</td>
      <td>0.0220</td>
      <td>0.0220</td>
      <td>0.0220</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">BK (slo1) α αβ</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>(Knaus et al., 1996; Misonou et al., 2006; Sailer et al., 2006; Kaufmann et al., 2010)</td>
      <td rowspan="2">Model from (Jaffe et al., 2011); modification see Appendix 2</td>
    </tr>
    <tr>
      <td>15.6 3.9</td>
      <td>62.4 15.6</td>
      <td>62.4 15.6</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">SK2</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td rowspan="2">(Obermair et al., 2003; Sailer et al., 2004; Maciaszek et al., 2012; Ballesteros-Merino et al., 2014)</td>
      <td rowspan="2">Model from (Solinas et al., 2007) based on (Hirschberg et al., 1998; 1999)</td>
    </tr>
    <tr>
      <td>0.001</td>
      <td>0.013</td>
      <td>0.083</td>
      <td>0.002</td>
      <td>0.004</td>
      <td>0.004</td>
      <td>0.004</td>
    </tr>
  </tbody>
</table>

### T2N facilitates use of synthetic morphologies based on optimal wiring principles

T2N allows users to investigate electrophysiological properties of morphological models created with TREES toolbox. The underlying morphological modeling algorithm (minimum spanning tree (MST) algorithm) finds optimal weighted solution for connecting dendritic target points considering a fundamental trade-off between cable length and conduction times (Cuntz et al., 2010, 2011; Cuntz et al., 2012). Realistic morphological models of dendrites, created by the MST algorithm, can be easily imported into NEURON via T2N (see Tutorial 2 in Appendix 1). In this way, users can test whether their compartmental models are stable over a large set of dendritic morphologies. To create a set of GC synthetic morphologies, we took our previously published morphological model of mature rat GCs (Beining et al., 2017) and adapted it for mature mouse GCs (Figure 2B). The resulting synthetic dendritic trees were morphologically comparable to the reconstructed trees of mouse GCs from Schmidt-Hieber et al. (2007) (Figure 2C). These synthetic neurons were introduced into the compartmental model as a further validation of the fitted passive and active properties (see below).

### T2N allows for an easy switch between real and synthetic morphologies and facilitates comparison of simulation results with experimental data

To illustrate the flexibility and versatility of T2N, we used it to fit the GC model equipped with ion channels from Figure 2A (see also Table 1) to experimental data. The channels were inserted into reconstructed (Figure 2A) or synthetic (Figure 2B) morphologies. Our goal was to replicate electrophysiological recordings from mature GCs including voltage clamp and current clamp experiments. For this purpose we used raw experimental traces from published data (Mongiat et al., 2009). Tutorials 3‒5 (Appendix 1) explain how to use T2N to define and run simulations, especially how to generate I-V and spiking frequency vs. current (f-I) curves. Figure 3 (middle column) and Table 2 show the results of such simulations in morphologies of mature GCs (for details see Appendix 2) indicating that our model is able to reproduce passive properties, steady state currents as well as AP shape and spiking behavior observed in patch-clamp experiments (Figure 3, left column; Mongiat et al., 2009). Importantly, the GC model remained stable and continued to generate realistic electrophysiological traces even after replacing one set of GC morphologies (reconstructed dendrites) by a different set of morphologies (synthetic dendrites; Figure 3, right column; see also Appendix 2) while keeping all biophysical mechanisms unaltered. Interestingly, the insertion of different morphologies introduced certain amount of variability in electrophysiological behavior (see Appendix 2 for details). Thus, some of the variance observed in electrophysiological recordings might be explained by the morphological variability of GCs.

![Figure 3.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig3-v3.jpg)

**Figure 3.:** Comparison of electrophysiological features between experimental data (left column, grayish colors) (Mongiat et al., 2009), GC model with reconstructed morphologies (middle column, blueish colors) and GC model with synthetic morphologies (right column, greenish colors). (A) Current-voltage (I–V) relationships before and after application of 200 µM Ba2+. Simulations (blue and green curves) are compared to experimental data (mean and s.e.m. from raw traces (Mongiat et al., 2009) as black curve and gray patch; arrows are average values reported from further literature: red (Brenner et al., 2005), yellow (Mongiat et al., 2009), green (Schmidt-Hieber et al., 2007)). Ba2+ simulations correspond to 99% Kir2 and 30 % K2P channel blockade. (B) Number of spikes elicited by 200 ms current steps (F-I relationship) from a holding potential of −80 mV. Right subgraph shows F-I relation after adding Ba2+. Experimental standard deviation is shown as gray patches in all columns. Red arrows point to the rheobase, which is different between control and BaCl2 application. (C) Exemplary spiking traces from control condition in (B) (200 ms, 30 and 75 pA somatic current injections). (D–E) Action potential (AP) features of the first AP (90 pA somatic step current injection, 200 ms). Convex hulls around experimental data are shown in all columns as gray patches. (D) AP width vs. AP amplitude. (E) Amplitude of fast afterhyperpolarisation (fAHP) vs. AP threshold. (F) Phase plots of the first AP (dV/V curve, 90 pA current step, 200 ms).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** This figure is analogous to Figure 3 (experimental data in left column, grayish colors) but in order to compare our model’s robustness to standard mature GC models, the biophysical model of Aradi and Holmes (Aradi and Holmes, 1999) was used here together with our set of reconstructed (middle column, blueish colors) and synthetic (right column, greenish colors) mouse morphologies. (A) Current-voltage (I–V) relationships before and after application of 200 µM Ba2+. Simulations (blue and green curves) are compared to experimental data (mean and s.e.m. from raw traces (Mongiat et al., 2009) as black curve and gray patch; arrows are average values reported from further literature: red (Brenner et al., 2005), yellow (Mongiat et al., 2009), green (Schmidt-Hieber et al., 2007)). Ba2+ simulations here only correspond to 30% passive channel blockade as this model does not include Kir2 channels. (B) Number of spikes elicited by 200 ms current steps (F-I relationship) including Ba2+ block as in A). Experimental standard deviation is shown as gray patches in all columns. (C) Exemplary spiking traces (200 ms, 30 and 90 pA somatic current injections. This is different to Figure 3 because no spiking occurred at 75 pA in the Aradi and Holmes mature GC model. (D–E) Action potential (AP) features of the first AP (90 pA somatic step current injection, 200 ms). Convex hulls around experimental data are shown in all columns as gray patches. (D) AP width vs. AP amplitude. (E) Amplitude of fast afterhyperpolarisation (fAHP) vs. AP threshold. (F) Phase plots of the first AP (dV/V curve, 90 pA current step, 200 ms).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** Influence of dendritic (left column) and somatic (right column) surface size on electrophysiological parameters (fAHP, AP width, AP threshold and number of APs) in the model with reconstructed (blue circles) and synthetic (green circles) morphologies. Correlation coefficients are given as inset text and trend lines are shown as gray dashed lines.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Currents measured during a highly hyperpolarized voltage step (−120 mV) in the experiment (left) and the models with reconstructed (middle) and synthetic (right) morphologies. The slowly activating currents (black arrows) originate from Kir currents in the model.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig3-figsupp4-v3.jpg)

**Figure 3—figure supplement 4.:** The maximal voltage deflection during a spike shows a sudden jump and then slow decay in the experiment when current amplitudes are increased in mature (upper row, left) and young GCs (lower row, left) which is not reproduced in the mature/young GC model with the na8st sodium channel model (from Schmidt-Hieber and Bischofberger, 2010) in reconstructed (middle column) or synthetic (right column) morphologies.

**Table 2.**
 Electrophysiology in mature mouse GCs – experiment vs. model.


<table>
  <thead>
    <tr>
      <th>Intrinsic properties</th>
      <th>Experiment</th>
      <th>Model reconstr. morphologies</th>
      <th>Model synth. morphologies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rin [MΩ] (@ −82.1 mV)</td>
      <td>289.5 ± 34.9</td>
      <td>287.0 ± 14.7</td>
      <td>279.6 ± 6.9</td>
    </tr>
    <tr>
      <td>cm [pF]</td>
      <td>48.9 ± 5.3</td>
      <td>55.7 ± 2.8</td>
      <td>61.2 ± 1.6</td>
    </tr>
    <tr>
      <td>tau [ms]</td>
      <td>34.0 ± 2.0</td>
      <td>31.4 ± 0.2</td>
      <td>31.6 ± 0.1</td>
    </tr>
    <tr>
      <td>Vrest [mV]</td>
      <td>−92.7 ± 0.5 *</td>
      <td>−88.7 ± 0.1</td>
      <td>−88.6 ± 0.0</td>
    </tr>
    <tr>
      <td>Ithreshold [pA]</td>
      <td>47.5 ± 4.5</td>
      <td>52.5 ± 3.7</td>
      <td>50.3 ± 1.6</td>
    </tr>
    <tr>
      <td>Vthreshold [mV]</td>
      <td>−46.3 ± 1.6 *</td>
      <td>−44.9 ± 0.3</td>
      <td>−43.8 ± 0.2</td>
    </tr>
    <tr>
      <td>AP amplitude [mV]</td>
      <td>95.6 ± 2.1</td>
      <td>96.3 ± 2.9</td>
      <td>97.7 ± 1.7</td>
    </tr>
    <tr>
      <td>AP width [ms]</td>
      <td>1.03 ± 0.02</td>
      <td>1.00 ± 0.04</td>
      <td>0.93 ± 0.02</td>
    </tr>
    <tr>
      <td>fAHP [mV]</td>
      <td>15.7 ± 1.4</td>
      <td>17.5 ± 1.7</td>
      <td>15.8 ± 0.8</td>
    </tr>
    <tr>
      <td>Interspike interval [ms]</td>
      <td>36.3 ± 4.9</td>
      <td>36.2 ± 3.2</td>
      <td>34.5 ± 1.1</td>
    </tr>
    <tr>
      <td>Max. spike slope [V/s]</td>
      <td>450.1 ± 23.7</td>
      <td>428.0 ± 39.5</td>
      <td>519.7 ± 24.9</td>
    </tr>
    <tr>
      <td>gKir [nS]</td>
      <td>5.46 ± 1.31</td>
      <td>5.90 ± 0.89</td>
      <td>5.97 ± 0.6</td>
    </tr>
  </tbody>
</table>

_*after subtraction of a calculated liquid junction potential of 12.1 mV._

### T2N facilitates the use of real or synthetic morphologies from different species

To test whether the ion channels from Figure 2A can account for mature rat GC electrophysiology, we used T2N to simulate rat I-V and f-I curves simply by replacing the mouse with rat GC morphologies. For this we used reconstructed and synthetic mature rat GC morphologies (Figure 4A), which we have recently published (Beining et al., 2017). Interestingly, increasing the Kir conductance (see Appendix 2 for details) was sufficient to replicate mature rat GC I-V recordings (Pourbadie et al., 2015) using rat morphologies (Figure 4B). Also, after the adjustment of the Kir conductance, active channel properties and densities from mouse GCs (Table 1) reproduced the spiking behavior of rat GCs (Figure 4C–D). This result indicates that both rodent species might share a similar GC ionic channel density pattern, conferring to these neurons their electrophysiological identity. Similarly to the mouse GC model, we could interchange real and synthetic rat morphologies without affecting the spiking behavior (Figure 4B–D, left vs. right). This shows an inherent robustness of our active model and validates its usefulness for large-scale network simulations of the rat DG.

![Figure 4.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig4-v3.jpg)

**Figure 4.:** Comparison of electrophysiological features between GC model with reconstructed morphologies (left column, blueish colors) and GC model with synthetic morphologies (right column, greenish colors) as it was adapted for reproducing rat data. (A) Illustration of reconstructed (left) and synthetic (right) rat morphologies used for simulations of rat GCs, from (Beining et al., 2017). (B) I-V relationship of the model with (dark solid lines) or without (bright dashed lines) adjustment of passive conductance to experimental rat data (indicated by arrows: red (Staley et al., 1992), yellow (Mateos-Aparicio et al., 2014), green (Pourbadie et al., 2015), violet (Schmidt-Hieber et al., 2004). (C) F-I relationship of the model compared to data (black line and standard deviation as gray patch) from Pourbadie et al., 2015. (D) Exemplary spiking traces simulated during a 1 s current injection of 200 pA.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** This figure is analogous to Figure 4 but in order to compare our model’s robustness to standard GC models, the biophysical model of Aradi and Holmes (Aradi and Holmes, 1999) was used here with reconstructed (middle column, blueish colors) and synthetic (right column, greenish colors) rat morphologies. (A) I-V relationship of the model (dark solid lines) compared to experimental rat data (indicated by arrows: red (Staley et al., 1992), yellow (Mateos-Aparicio et al., 2014), green (Pourbadie et al., 2015), and violet (Schmidt-Hieber et al., 2004). (B) F-I relationship of the model compared to data (black line and standard deviation as gray patch) from (Pourbadie et al., 2015). (C) Exemplary spiking traces simulated during a 1 s current injection of 200 pA.

![Figure 5.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig5-v3.jpg)

**Figure 5.:** bAP characteristics at 33°C (experiment and simulation), elicited in the soma by a brief current injection. Inset: Exemplary rat and mouse GC morphology with local maximum voltage amplitudes. (A) Maximal voltage amplitude as a function of Euclidean distance from the soma. Black data points are experimental data from rat (Krueppel et al., 2011). There are no available data on bAP characteristics for mouse GCs. (B) Corresponding delay of the maximal bAP amplitude in the model compared to experimental rat data (black dots) (Krueppel et al., 2011). (C) Peak Ca2+ amplitudes at room temperature following an AP measured at different locations in the rat (left) and mouse (right) GC model using reconstructed (blue) and synthetic (green) morphologies. Experimental rat data measured in proximal dendrites (Stocca et al., 2008) and axonal mossy fiber boutons (MFBs) (Jackson and Redman, 2003) are added as black bars. There are no available data on bAP characteristics for mouse GCs. (D) Ca2+ decay time constants analogous to C.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** bAP characteristics at 33°C (experiment and simulation), elicited in the soma by a brief current injection. Inset: Exemplary rat and mouse GC morphology with local maximum voltage amplitudes. Note that in order to measure dendritic bAP and Ca2+ characteristics in the classical GC model using a short strong current pulse as in Figure 5, it was necessary to isolate the cell from its axon (by increasing Ra) because the latter was a source of ongoing spike generation after the first spike in most morphologies and thus made measurements otherwise impossible. (A) Maximal voltage amplitude as a function of Euclidean distance from the soma. Note the higher amplitudes in the dendrites due to activated Nav channels there. Black data points are experimental data from rat (Krueppel et al., 2011). (B) Corresponding delay of the maximal bAP amplitude in the model compared to experimental rat data (black dots) (Krueppel et al., 2011). (C) Peak Ca2+ amplitudes at room temperature following an AP measured at different locations in the rat (left) and mouse (right) GC model using reconstructed (blue) and synthetic (green) morphologies. Note that the Aradi and Holmes mature GC model has no Ca2+ channels in the axon, thus the measurement was omitted there. Experimental rat data measured in proximal dendrites (Stocca et al., 2008) and axonal mossy fiber boutons (MFBs) (Jackson and Redman, 2003) are added as black bars, which are very small, as the Ca2+ concentrations in the Aradi and Holmes GC model are higher by a factor of ~1000 compared to our model. (D) Ca2+ decay time constants analogous to C.

### T2N simplifies analysis of dendritic voltage propagation and Ca2+ signaling across different morphologies and species

T2N supports simulations, efficient analysis and visualization of distance-dependent changes of dendritic voltage and Ca2+ spread. In Tutorial 6 (Appendix 1), we show how a few lines of code are sufficient for plotting bAP amplitudes on the shape of neuronal trees (shape plot: see insets in Figure 5A) and for creating bAP amplitude vs. distance plots (Figure 5B). In Tutorial 7 (Appendix 1), we explain how to evaluate Ca2+ dynamics in different compartments of a model using the T2N tools.

In the specific case of GCs, we used T2N and our active GC models from Figures 3 and 4, to compare backpropagating APs (bAPs) in mouse and rat (for details see Appendix 2). The rat GC model was able to reproduce bAP attenuation (Figure 5A, left; see Appendix 2 for details) determined from dendritic patch clamp experiments (Krueppel et al., 2011). Interestingly, for a realistic delay of the bAP peak, we had to adjust the specific axial resistance Ra and the passive membrane conductance to the higher temperature of 33°C (Figure 5B, left) that was used in experiments (Krueppel et al., 2011). This provides further evidence for the consistency of our model with experimental data. Moreover, we used a well-tuned phenomenological Ca2+ buffer model (see Appendix 2 for details), which generated realistic intracellular Ca2+ signals induced by bAPs (Figure 5C, left). Ca2+ dynamics in synthetic morphologies (Figure 5C, green bars) matched Ca2+ signals from experiments (black bars) as well as those from reconstructed morphologies (blue bars). Thus, our GC model generated realistic and stable intracellular Ca2+ dynamics over a broad range of different morphologies in rat and mouse.

After validating the rat GC model for bAPs, we computed an experimentally testable prediction for bAP attenuation in mouse GCs (Figure 5A,B, right), for which no experimental data on bAPs exist so far. The model predicted that bAP attenuation was smaller in mouse GCs than in rat GCs. This prediction can be tested by dendritic patch clamp recordings in mouse GCs. We also computed a prediction for bAP-induced intracellular Ca2+ changes in mouse morphologies (Figure 5C, right). Ca2+ levels in mouse GCs were comparable to Ca2+ levels in rat GCs. Provided that Ca2+ buffering and extrusion mechanisms are comparable between mouse and rat GCs (Stocca et al., 2008), this suggests that dendritic Ca2+ signaling is relatively similar in both species despite differences in backpropagating dendritic voltage spread.

### Example of sensitivity analysis performed with T2N revealing critical ion channels in mature mouse and rat GCs

T2N helps identify crucial parameters affecting electrophysiological behavior of compartmental models because it supports flexible whole cell as well region- and layer-specific manipulations of ion channel properties. In Tutorial 8 (Appendix 1), we show how to use a T2N function to upregulate or downregulate individual or multiple channels in defined regions of a dendritic tree. We applied these T2N features to perform a sensitivity analysis of the GC model predicting the effects of a reduction (Figure 6A) or an increase (Figure 6—figure supplement 1) of model parameter values. In addition, we used the T2N channel block function (Tutorial 8, Appendix 1) to completely turn off individual ion channels (Kv3, BK, SK and Kv7) and explore their impact on AP repolarization and spike adaptation (Figure 6B,C). In Appendix 2, we provide a summary of the results with detailed information on key GC ion channels and other factors (e.g. temperature) involved in the regulation of GC excitability, action potential (AP) properties, voltage propagation and output firing. These results describe single parameter sensitivity analyses. However, T2N can be used also for analyzing the impact of any combinations of parameters, thus contributing to assessments of degeneracy in compartmental models (see Discussion).

![Figure 6.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig6-v3.jpg)

**Figure 6.:** (A) Sensitivity matrix showing the relative change (color-coded) in electrophysiological parameters (y-axis) in the mature rat GC model following a 50% reduction in ion channel densities or other model parameters (x-axis), except for the cases marked with an asterix (*): the reversal potential of potassium EK as well as the passive reversal potential EPas were raised by +10 mV (to reduce ionic drive) and ENa was lowered by −20 mV. The temperature was raised by +10°C. cAMP concentration (influencing HCN channels in the model) was raised from 0 to 1 µM. (B) Left: Exemplary voltage traces during 1 s current injection of 90 pA (left, first AP) or 250 pA (right, fifth AP) under control (black lines), Kv3.4 block (red lines) or BK block (blue lines) conditions in the mature rat GC model. Right: Half-amplitude AP widths compared to experimental data that used paxilline to block BK (Brenner et al., 2005; Müller et al., 2007) or BDS-I to block Kv3.4 channels (Riazanski et al., 2001). (C) Impact of the blockade of SK and Kv7 channels on spike frequency adaptation in the mature rat GC model. (D) Input resistance measurements in the rat GC model in the control case and when post-epileptic conditions are modeled (doubled Kir2 and HCN channel conductance). (E) A reported overexpression of Kv1.1 following an in vivo approach to elicit temporal lobe epilepsy in mice (Kirchheim et al., 2013) was mimicked in silico by a three-fold increase of Kv1.1 channel density in the mature mouse GC model. Left graph illustrates increased spiking delay, whereas the right plot shows the reduced excitability.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** Sensitivity matrix analogous to Figure 6A but with increased (doubled) instead of reduced channel densities or parameters except for the cases marked with an asterix (*): the reversal potential of potassium EK was lowered by −20 mV (to increase ionic drive) and ENa was increased by +20 mV. HCN is increased from 0 to 1 µM in both cases. Temperature was reduced from 24°C to 14°C.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig6-figsupp2-v3.jpg)

**Figure 6—figure supplement 2.:** GCs were injected with oscillating currents of increasing frequency to calculate their impedance. The graph shows experimental (solid curves, human GCs (Stegen et al., 2012)) and simulation (dashed curves, rat GCs) data under control conditions (black) and when Kir (blue) or Kir and HCN (red) channels are blocked.

### T2N supports prediction of clinically relevant ion channel alterations in multiple neuronal morphologies

T2N’s strength relies in its capability of handling and manipulating compartmental simulations in many morphologies. Therefore, it is suitable to predict the consequences of ion channel changes not only in healthy cells but also under pathological conditions. We exemplify this by using our mouse GC model to calculate the effects of compensatory ion channel alterations observed during temporal lobe epilepsy (TLE). As shown previously in experiments, protective upregulation of HCN and Kir (Young et al., 2009; Stegen et al., 2012) or Kv1.1 channels (Kirchheim et al., 2013) decreases GC excitability under epilepsy conditions. In line with these data, our model GCs exhibited similar changes (Figure 6D,E; see also Figure 6—figure supplement 2 and Appendix 2 for further details). This shows that T2N can be used to estimate effects of pathology-related alterations, which are robust across multiple non-identical single-cell morphologies. Moreover, by providing and exploiting powerful morphological modeling tools from the TREES toolbox, T2N creates a unique opportunity for making clinically relevant cell-type models with hundreds to thousands of distinct morphologies that can be inserted into network models to study neuronal pathology on the level of microcircuits or large circuits.

### Example of using T2N for building a data-driven young adult-born GC model

To demonstrate the flexibility of T2N in building compartmental models, we used it to create the first model of young adult-born GCs (abGCs). During a critical period (starting around the 4th week of cell age), abGCs exhibit increased excitability as compared to older abGCs or mature GCs (Mongiat et al., 2009). Our goal was to reproduce the electrophysiology of these young (28 days old) abGCs (Mongiat et al., 2009). For this purpose, we adapted our mature GC model by modifying its biophysics according to ion channel data from abGCs and postnatal developing GCs (Table 3, Figure 7; see Appendix 2 for details). We did not change the morphology of dendrites since our previous study in rat showed that dendritic trees of young and mature adult-born GCs are similar (Beining et al., 2017). In line with experimental findings (Mongiat et al., 2009), changing the expression of Kir2 channels and other channel types (Table 3) led to altered I-V curves and increased excitability in young abGCs as compared to mature GCs (Figure 7). These results indicate that the robust compartmental models generated using T2N can easily be adapted for exploring varying electrophysiological states of the same cell type, for example, during adult neurogenesis and potentially also during development.

![Figure 7.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig7-v3.jpg)

**Figure 7.:** Panels are analogous to Figure 3, with comparison of electrophysiological features between experimental data (left column, grayish colors), GC model with reconstructed morphologies (middle column, blueish colors) and GC model with synthetic morphologies (right column, greenish colors). The experimental data of young abGCs at a cell age of 28 dpi is from Mongiat et al. (2009). The model was obtained by a reduction of several ion channels (see Table 3). (A) Current-voltage (I–V) relationships before and after application of 200 µM Ba2+; Ba2+ simulations correspond to 99% Kir2 and 30 % K2P channel blockade. Experimental measurements of Rin in 28 dpi old abGCs from further literature are indicated by arrows (red [Mongiat et al., 2009], green [Piatti et al., 2011], pink [Yang et al., 2015]). (B) Exemplary spiking traces (200 ms, 10 and 50 pA somatic current injections). (C) Number of spikes elicited by 200 ms current steps (F-I relationship). Experimental standard deviation is shown as gray patches in all columns and the F-I curve of mature GCs is plotted in the left column (gray dashed line) for comparison. (D–E) Action potential (AP) features (90 pA somatic step current injection, 200 ms). Convex hulls around experimental data are shown in all columns as gray patches. (D) AP width vs. AP amplitude. (E) Amplitude of fast afterhyperpolarisation (fAHP) vs. AP threshold. (F) Phase plots of the first AP (dV/V curve, 90 pA current step, 200 ms).

**Table 3.**
 Ion channels or currents that were reported to be less expressed in immature GCs and were downregulated in the young GC model


<table>
  <thead>
    <tr>
      <th>Channel name</th>
      <th>Cell type and Reference</th>
      <th>Downregulation in the model [%]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Kir 2.x</td>
      <td>Young adult-born GCs (Mongiat et al., 2009)</td>
      <td>73</td>
    </tr>
    <tr>
      <td>Kv1.4</td>
      <td>Young postnatal GCs (Maletic-Savatic et al., 1995; Guan et al., 2011)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Kv 2.1</td>
      <td>Young postnatal GCs (Maletic-Savatic et al., 1995; Antonucci et al., 2001; Guan et al., 2011)</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Kv3.4</td>
      <td>Young postnatal GCs (Riazanski et al., 2001)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Kv4.2/4.3 +KChIP/DPP6</td>
      <td>Young postnatal GCs (Maletic-Savatic et al., 1995; Riazanski et al., 2001)</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Kv 7.2 and 7.3 (KCNQ2 and 3)</td>
      <td>Young postnatal GCs (Tinel et al., 1998; Smith et al., 2001; Geiger et al., 2006; Safiulina et al., 2008)</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Nav1.2/6</td>
      <td>Young postnatal GCs (Liu et al., 1996; Pedroni et al., 2014)</td>
      <td>25</td>
    </tr>
    <tr>
      <td>Cav1.2</td>
      <td>Young postnatal GCs (Jones et al., 1997)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cav1.3 (L-type)</td>
      <td>Young postnatal GCs (Kramer et al., 2012)</td>
      <td>50</td>
    </tr>
    <tr>
      <td>BK-α/BK-β4</td>
      <td>Young postnatal GCs (MacDonald et al., 2006; Xu et al., 2015)</td>
      <td>40/100</td>
    </tr>
  </tbody>
</table>

### T2N simplifies modeling of synaptic drive and facilitates making experimental predictions

T2N makes it easier to equip compartmental models with layer-specific synaptic inputs and connect them to spike generators. Tutorial 9 (Appendix 1) provides a step-by-step description of T2N-assisted insertion of AMPA synapses modeled as exponential rise and decay of synaptic conductance upon receiving spikes from a spike train generator (artificial presynaptic cell). The tutorial also explains how to generate random (Poisson) spike train to drive presynaptic spike generators. Because generating random spike streams in NEURON is not trivial (see https://www.neuron.yale.edu/neuron/node/60), T2N allows users to employ random number generators of Matlab to simplify this process. This illustrates one strength of T2N, which relies in providing Matlab functions not only for analyzing simulation results but also for setting up models as well as their instrumentation and control.

We employed above-mentioned functions of T2N to generate experimentally testable predictions for synaptic integration of abGCs and mature GCs (mGCs; Figure 8, see Appendix 2 for details). Four-week-old abGCs are known to have a lower number of excitatory synapses as reflected by lower spine densities (Zhao et al., 2006) and decreased frequency of miniature excitatory post-synaptic currents (Mongiat et al., 2009). Importantly, when abGCs were driven by a smaller number of synapses, they exhibited similar synaptic input/output relationships as mGCs (Figure 8A). This suggests that higher intrinsic excitability of abGCs (see also Figure 7C) compensates for their lower numbers of synaptic inputs. Moreover, our modeling indicates that both young abGCs and mature GCs are tuned to follow input frequencies in the theta range (<10 Hz; Figure 8B). This result is consistent with studies showing that diminished glutamatergic input is compensated by the enhanced excitability when GABAergic inhibition is blocked (Mongiat et al., 2009; Pardi et al., 2015).

![Figure 8.](https://cdn.elifesciences.org/articles/26517/elife-26517-fig8-v3.jpg)

**Figure 8.:** (A) Left: Scheme of the simulation configuration with 15 synapses distributed in the MML and 15 in the OML. Middle: All synapses are activated synchronously at 40 Hz. Note that young abGCs (middle row) followed the input (black vertical lines) better than mature GCs (upper row), but performed similarly (lower row) when the biologically lower synapse number (15 synapses in total, yGC15) was implemented. Right: Summary of the input/output relation at all tested frequencies (5, 10, 20, 40, 75, 100 Hz). Gray dashed line illustrates the theoretically perfect input/output ratio. (B) Upper left: Scheme of the simulation configuration when MML and OML synapses are activated with a delay of Δt to analyze temporal summation of inputs. Upper right: Note that young abGCs perform better than mature GCs at following the 10 Hz input when the MML and OML inputs are delayed (left, −15 ms) compared to synchronous activation (right, 0 ms). Lower row: Summary over all tested frequencies (10, 20, 40, 75 Hz) showing that young abGCs have a broader time window of temporal summation than mature GCs at low frequencies but perform slightly worse than mature GCs at high frequencies.

Finally, we used the model to test synaptic integration of abGCs for temporally shifted synaptic inputs. Our model predicts that at low frequencies in the theta range, young abGCs were able to integrate synaptic inputs with a broader time window than mGCs (Figure 8B and Appendix 2). This is in line with the proposed special role of abGCs in hippocampal pattern separation and integration due to their broader tuning to the activity of synaptic inputs (Aimone et al., 2010; Johnston et al., 2016; Rangel et al., 2013). In conclusion, our model reproduces and predicts the activation patterns of young and mature granule cells under those conditions when inhibition is not present.

## Discussion

In this work, we developed T2N, a novel software tool for linking morphological with compartmental modeling and analysis. T2N allows communicating seamlessly between the TREES toolbox in Matlab (Cuntz et al., 2010, 2011) and the software package NEURON (Carnevale and Hines, 2006). T2N enables to fit models directly on any population of morphologies including those from morphological models. In this way, we provide tools to generate the kind of robust models for which we presented one example for dentate granule cells (GCs). T2N as well as the new GC model are freely available online (http://www.treestoolbox.org/T2N.html; senselab.med.yale.edu/modeldb/, accession # 231862; we also uploaded a pure NEURON version of the GC model including all morphologies and biophysics but only two protocols on ModelDB under the accession # 231818) as a resource for scientists working with detailed biophysical compartmental models.

What is the strength of T2N? What are its unique features? T2N provides user-friendly definition and control of NEURON compartmental models (morphologies, channel distributions, simulations etc.) as well as a subsequent analysis with Matlab and the TREES toolbox. Moreover, the automatic parallelization of multiple simulation runs (e.g. to create an F-I relationship) and the parallelization option using NEURON‘s parallel computing feature (Migliore et al., 2006) for single simulations that include a large amount of cells (e.g. large-scale networks) reduces simulation time considerably. The clear structure of the definitions of a model’s biophysical features as well as the automatically produced stereotyped NEURON code improves reading the model scripts and merging of different models developed with T2N. Sensitivity analyses, plots and visualizations are much easier to do with T2N than other commonly used software tools. In addition to simulations in reconstructed morphologies, T2N easily allows running simulations using synthetic morphologies from morphological models thereby facilitating the generation of biophysically and morphologically realistic large-scale network models. By enabling the use of diverse reconstructed and synthetic dendritic trees, T2N makes it possible to generalize the predictions of compartmental simulations to any morphology and supports the search for universal principles valid across different species and cell types. By supporting the inclusion of variable morphologies and precise incorporation of ion channels, T2N will allow users to more fully harness the resources from online databases such as NeuroMorpho (Ascoli et al., 2007) and IonChannelGenealogy (Podlaski et al., 2016) or Channelpedia (Ranjan et al., 2011). In summary, T2N is a versatile and adaptable tool for extensive in silico structure-function analyses in NEURON.

### New robust GC model

Using T2N we developed a new compartmental model that mimics the detailed electrophysiological behavior of mature GCs and young abGCs in mouse and rat. The model has five important advantages and improvements when compared to previously published models: (1) Our model is the first compartmental GC model – and one of the first neuron models overall – which remains robust across a wide variety of reconstructed and synthetic morphologies. (2) The model contains only conductances of channel isoforms that are currently known to exist in GCs and accurately implements their kinetics. The model is based on information from more than 220 publications (see the Reference list) that were required to cover the full extent of the biological detail in our model, rendering its development an in-depth quantitative review of the electrophysiology of granule cells. (3) The model is capable of reproducing findings and experiments from many different studies. (4) After adjustment of Kir2 channel density, the model reproduced electrophysiological behavior of both rat and mouse mature GCs indicating that these species might share similar active channels. (5) The adapted model for young abGCs represents the first available data-driven compartmental model of these neurons. With this consistent model at hand, we were able to reproduce the effects of compensatory ion channel changes under epileptic conditions in mature GCs. Furthermore, the model predicted the impact of differences in intrinsic properties between young abGCs and mature GCs on the temporal summation of synaptic input. We found that the higher intrinsic excitability allows young abGCs to integrate synaptic inputs in a broader time window compared to mature GCs. Altogether, this suggests a universal nature of the stability of the model. To sum up, our granule cell simulations provide important insights and tools for the hippocampus research field in general and the adult neurogenesis field in particular. Our study builds the cornerstone for future GC modeling approaches, by providing a model with which hypotheses on the impact of structural and functional alterations can be tested and further mechanisms such as synaptic plasticity and inhibition can be added at will. Our study further underlines the importance of biological soundness and the appropriate level and amount of detail for realistic modeling.

### Morphologically robust compartmental modeling

Many existing GC compartmental models were based on a very simplified representation of morphology comprising two cylinders in place of realistic dendrites (e.g. Jedlicka et al., 2015; Santhakumar et al., 2005). Furthermore, models that did not use such simplified compartments were mostly tested in single morphologies (Aradi and Holmes, 1999; Ferrante et al., 2009). Therefore, there was a need for a new biophysical model, which would be transferable to further morphologies. We found previous biophysical models of hippocampal GCs to be unstable across different dendritic morphologies (Figure 3—figure supplement 1, Figure 4—figure supplement 1, Figure 5—figure supplement 1, Supplementary file 1). In our study, we introduced electrophysiological variability (Figure 3—figure supplement 2) to the compartmental model by using diverse realistic and synthetic morphologies while keeping the channel densities the same. We developed a morphological mouse model capable of reproducing detailed morphological parameters of reconstructed mouse GCs (Schmidt-Hieber et al., 2007). We also created synthetic rat GCs using our recently published morphological model fitted on fully reconstructed rat morphologies (Beining et al., 2017). The morphological variability produced by each model was similar to the biological variability in the reconstructions. Interestingly, the resulting electrophysiological variability was in the range of experimental data indicating that morphological variability is able to account for a large part of electrophysiological variability. Hence, our model provides a valuable tool to create a DG network model with thousands of different but realistic GC morphologies (c.f. Schneider et al., 2012; Schneider et al., 2014) and data-driven GC spiking behavior.

Why was our compartmental model able to reliably reproduce electrophysiological data despite morphological variability of dendrites? One important reason is that our biophysical mechanisms were based on detailed, up-to-date knowledge of the ion channel distribution and kinetics. Second, both morphological as well as biophysical model parameters were determined in a species-, cell type- and cell-age-specific manner. Third, instead of using one morphology or simplified morphologies, we tuned the model using a large set of realistic dendritic trees. Fourth, because we implemented realistic intracellular Ca2+ dynamics we did not have to use unrealistic Ca2+- or Ca2+-dependent channel densities (for details see Appendix 2). This is a significant amendment of previous GC models. Fifth, instead of using a single voltage trace or a single recording, we used several traces and datasets to tune the model. By reproducing numerous electrophysiological phenotypes rather than one phenotype, our approach was similar to a multiple objective approach of Druckmann et al. (2007). Of note, we found a single solution that works across many morphologies, not a set of solutions with different parameter combinations for each morphology. However, we do not exclude the possibility that there exists such a set of solutions with distinct parameters for different morphologies. Taken together, our work suggests that morphologic robustness arises naturally in models in which parameters have been tuned using multiple different experiments and morphologies. This conclusion is also supported by a comparison of our biophysical model to an earlier widely used GC model from Aradi and Holmes (1999) (e.g. Schneider et al., 2012; Liu et al., 2014; Mateos-Aparicio, Murphy and Storm, 2014; Jedlicka et al., 2015; Platschek et al., 2016), which failed to reproduce electrophysiological data after transferring it to diverse mouse and rat GC morphologies (Figure 3—figure supplement 1, Figure 4—figure supplement 1, Figure 5—figure supplement 1, Supplementary file 1). However, the point of our new model is not to disregard valid predictions of previously published compartmental GC models. We rather emphasize the need for using diverse morphologies in combination with realistic channels for the improvement of GC models and compartmental models in general. We believe that now the community of computational neuroscientists should start to build models, which perform well outside of the scope, for which they were created (Almog and Korngreen, 2016). T2N provides a way to achieve this.

### Predictions of the GC model

Our results suggest that mature rat GCs display a reduced excitability due to incorporation of additional Kir channels. As an alternative, this could also be achieved by other leak channels such as K2P channels; however, the rat I-V curve from experimental data in Figure 4B showed pronounced inward rectification, further supporting Kir channels as an underlying mechanism. In line with this, the increased leak conductance in the rat GC model improved the fitting of simulated bAP attenuation to physiological recordings obtained from rat experiments (Krueppel et al., 2011), as the attenuation was too weak in the unmodified rat model (data not shown).

In our attempt to create the first compartmental model of abGCs, we focused on their special intrinsic, non-synaptic properties known to exist at the start of the critical time window, namely their increased input resistance and weaker Na/K peak conductance (Mongiat et al., 2009). To implement these changes we used data on ion channels which are known to be upregulated during postnatal development (Table 3) assuming that adult-born is similar to postnatal GC development (Espósito et al., 2005; Zhao et al., 2006; Snyder et al., 2012). Even though a lower expression (or alternative splicing) of BK channels is only visible at P14 or earlier, we also had to reduce BK channels in our young abGC model because the fast AHP, which is mainly regulated by BK channels in GCs, was reported to be reduced in young abGCs (Yang et al., 2015), an observation we also found in our raw traces (Figure 7B, left) from Mongiat et al. (2009). The parameters of the young abGC model were fitted best when we reduced the beta4-subunit associated BK current (gabk) by 100%. Thus, the abGC model predicts that the beta4 subunit is less expressed or not associated with BK channels in young abGCs. Future improvements of the abGC model should focus on more realistic simulations of details in voltage traces including fAHP kinetics, which are reproduced qualitatively but not quantitatively by the current model (Figure 7B).

To investigate the impact of the special intrinsic properties of young abGCs on their synaptic integration, we subjected both young and mature GC models to a broad range of synaptic input stimulation frequencies ranging from 10 to 75 Hz. In line with experimental data (Mongiat et al., 2009; Pardi et al., 2015), we found that diminished glutamatergic input onto abGCs was compensated by their enhanced excitability when GABAergic inhibition was absent. Both populations of GCs responded in a similar fashion over a wide range of stimuli, which is also in agreement with electrophysiological recordings (Pardi et al., 2015). Furthermore, despite their weaker excitatory input, we found that young abGCs were more efficiently activated by temporally separated (>15 ms) incoming activity from medial and lateral perforant path inputs as compared to mature GCs. Of note, in our study we did not model very young abGCs with reduced dendrite arborization but only focused on 4 weeks old abGCs that do not display any further significant alterations in their dendritic morphology (see our dendrite analyses and modeling in Beining et al. (2017). However, T2N can be used to model also younger abGC at various ages. By coupling different phases of dendrite development to corresponding biophysical models, T2N may reveal the principles, which support the maintenance of structural and functional integrity of real or synthetic morphologies as they mature or change during pathology (see Narayanan and Chattarji, 2010; Dhupia et al., 2014; Bozelos et al., 2015; Platschek et al., 2016; Platschek et al., 2017).

Most existing GC models did not implement specific ion channels but instead used equations describing ion currents (A-, M-, T-type, L-type, N-type, delayed rectifier etc.) that had been measured in GCs, but which are formed by the combined action of several differently distributed ion channels in the real cell (e.g. Kv1 and Kv4 form the A-type current in GCs but are localized in the axon or dendrite, respectively). By incorporating the contributions of different ion channel isoforms, our model can be used to analyze and predict the impact of different channelopathies or compensatory ion channel adaptations onto the cell’s active and passive behavior. This might be of special interest since specific isoforms dynamically control excitability (e.g. Kv2.1; Misonou et al., 2005) and alter their expression under pathological conditions such as epilepsy (e.g. Kv1.1; Kirchheim et al., 2013; or Kir2.1 and HCN; Stegen et al., 2012) or oxidative stress (e.g. Kv4; Rüschenschmidt et al., 2006). Indeed, our model was able to reproduce qualitatively the effects of a compensatory upregulation of Kir, HCN and Kv1.1 channels reported in TLE (Stegen et al., 2012; Kirchheim et al., 2013) demonstrating its predictive power there. Thus, the model might further be used to predict single or combined effects of other TLE-induced hippocampal alterations such as the reduction of BK channels in GCs (Pacheco Otalora et al., 2008), the aberrant connectivity (see review by Sharma et al., 2007; and network model by Santhakumar et al., 2005), as well as the impact of therapeutic gene transfer approaches, such as the transfer of the K2P leak channel TREK-1 to ameliorate status epilepticus (Dey et al., 2014).

As we did not investigate the entire parameter space of our electrophysiological models (especially in the young abGC model), for example using a genetic algorithm, we cannot exclude that a different channel density distribution would result in a similarly robust and successful reproduction of experimental results (Achard and De Schutter, 2006). We took great care to compare the expression and subcellular distribution data of ion channels in immunohistochemical studies with different studies by other labs or with electrophysiological evidence (e.g. pharmacological blockade). However, previous work in other cell types and animals has shown that similar electrical behavior might arise from different combinations and parameters of ion channels (Achard and De Schutter, 2006; Günay et al., 2008; Prinz et al., 2004; for review see Marder, 2011; Marder and Goaillard, 2006).

### T2N limitations and future directions

So far, T2N is specialized on handling neuronal morphologies and neuronal models. As other cellular interactions, such as astrocytic-neuronal contacts are emerging to play an important role, e.g. for meta-plasticity (Abraham and Bear, 1996; Abraham, 2008), future versions of T2N should make it possible to reconstruct, build and simulate astrocytes and astrocyte-neuron interactions. The set of T2N functions can be extended to simplify modeling of new experimental settings including simulations of nonlinear synaptic integration or synaptic and intrinsic plasticity as well as structural dendritic plasticity such as dendritic retraction or pruning of dendritic segments (Beining et al., 2017; Platschek et al., 2017). Including stochastic sampling algorithms would make T2N suitable to study degeneracy by supporting a search for distinct combinations of morphological and biophysical properties generating similar physiological outcomes.

### GC modeling and degeneracy

With our newly developed T2N, we were able to create a novel compartmental model of mature and adult-born mouse and mature rat GCs that is biologically and physiologically consistent. Therefore, it is of high predictive value for studies on the single-cell and network behavior of mature GCs and young abGCs, as well as under pathological conditions of synaptic, morphological or physiological alterations of GCs. As compared to more standardized methods with automated parameter fitting such as those used in the Allen Brain Project or Blue Brain Project (Druckmann et al., 2007Druckmann et al., 2007; Hay et al., 2011; Markram et al., 2015; Shai et al., 2015; Van Geit et al., 2016), our model resulted from a more traditional approach of incorporating as much biological data as possible. Nevertheless, our model satisfies the objective constraints from experiments (Table 2) and is robust to experimentally verifiable manipulations. We do not criticize automated parameter fitting, which is of great value. Our main point is the emphasis on using many different morphologies in combination with carefully, biologically constrained ion channel models. While one reason for the particular robustness of our model comes from the modeling approach using T2N, it is likely that the complete GC ion channel set offers redundancy and stability with respect to differences such as in morphology or species. Therefore, it will be interesting to further investigate whether the redundancy introduced by the set of existing ion channels is responsible for the robustness to morphological modifications in our GC model. Thus, our biophysical and morphological model provides a basis for future studies determining how cell-to-cell and animal-to-animal variability of ion channel expression combined with morphological and synaptic variability affects the robustness of GC passive and active behavior.

Our model is available on the ModelDB public database (http://senselab.med.yale.edu/ModelDB/default.asp) and can now be used to address the exciting question whether ion channel degeneracy in GCs exists in terms of compensatory interactions between multiple ion channels (Drion et al., 2015) and how it contributes to the homeostasis of GC function. Future work should also address the question whether variation of some other biological factors besides morphology or in addition to it would also lead to robust GC simulation results. As mentioned above, for this purpose, T2N could be extended by incorporating stochastic search algorithms (Foster et al., 1993; Goldman et al., 2001; Weaver and Wearne, 2008; Rathour and Narayanan, 2014; Mishra and Narayanan, 2017), which would allow users to generate multiple randomized models with different biophysical and morphological parameters leading to similar electrophysiological behavior. This would help to reveal which combinations of channel properties and dendritic arborization support robustness of GC function. A recent study (Mishra and Narayanan, 2017) addressed this issue using a large number of GC models with variable channel parameters in reduced morphologies. It would be interesting to employ a similar approach and use T2N and our new GC model with the updated layer-specific composition of ionic channels to stochastically generate many biophysically distinct GC models with variable location-dependent channel expression as well as variable full dendritic morphologies (Schneider et al., 2014). Simulations and analyses in such large collections of detailed conductance-based GC models might contribute to the identification of subcellular mechanisms of degeneracy. Specifically, this approach would show whether disparate dendrite and channel parameters, including dendrite length and branching as well as gradients in channel densities, kinetics, voltage-dependence or intracellular milieu may lead to identical GC electrophysiology. T2N will be useful to generalize such analyses also to other cell types.

## Materials and methods

### Compartmental modeling with T2N

Compartmental modeling was done in the NEURON (Carnevale and Hines, 2006) environment (V7.4) controlled and run using our novel T2N interface. T2N was written as an extension of the freely-available TREES toolbox (Cuntz et al., 2010, 2011) providing an interface between Matlab (Mathworks) and NEURON. It was developed on Matlab 2015b and it is recommended to use Matlab 2015b or higher. All ion channels, point processes, connections, morphologies and NEURON settings are directly set in a well-defined Matlab structure. For any morphology-related settings or manipulations, T2N uses the set of TREES toolbox functions (e.g. to create and handle reconstructed and synthetic dendritic morphologies). Neuronal morphologies including precise node locations are automatically translated into NEURON sections and segments. Multiple NEURON simulations (e.g. to simulate several cells or to create an f-I relationship) can be run in parallel as T2N is able to start separate NEURON instances on different cores, thus reducing simulation time. Even more important, T2N allows the use of the parallel NEURON environment (Migliore et al., 2006; Hines and Carnevale, 2008), thus drastically increasing performance of large-scale networks by distributing cells of single NEURON simulations on multiple cores using a round robin approach. Recorded variables are returned to Matlab in a well-ordered structure for further analysis. For more information, see the T2N manual, which is provided with the code (see Data sharing).

### Data analysis and visualization

The programming environment Matlab (Mathworks, version 2015b, some functions of the GC model are not functional in earlier Matlab versions) was used together with the TREES toolbox to analyze raw electrophysiological data from Mongiat et al. (2009), as well as the output of the compartmental modeling simulations. Electrophysiological properties were measured as following: The input resistance Rin was measured using the steady-state current during a depolarizing 10 mV voltage step (200 ms long, from a holding potential of −92.1 mV). In the raw data from Mongiat et al. (2009), on which we fitted most of the active properties of our compartmental model, a liquid junction potential (LJP) of 12.1 mV existed for which we corrected the voltage traces and voltage commands. Hence, to compare Kir conductance in the raw data and the model as performed in Mongiat et al. (2009), we calculated the slope conductance at hyperpolarized values (−152.1 to −122.1 mV) and subtracted the slope conductance at a potential range where Kir channels are largely closed (−82.1 to −62.1 mV). The cell capacitance was obtained from a −10 mV voltage step as the integral of the measured current (steady-state current subtracted) divided by the amplitude of the voltage step. The membrane time constant was measured as the exponential voltage decay following a 500 ms long hyperpolarizing current step (10 pA) from a holding potential of −80 mV. All action potential (AP) property measurements were done on the first AP of a 200 ms long 90 pA current step (from a −80 mV holding potential). The voltage threshold of an action potential (AP) was defined as the point when the voltage slope exceeded 15 mV/ms. The rheobase was the current step (5 mV intervals, 200 ms current step from −80 mV holding potential) at which the first AP occurred. The AP amplitude was defined as the difference between the absolute AP amplitude and the AP voltage threshold and AP width was the half-maximum width of this amplitude. The fast afterhyperpolarization potential (fAHP) was calculated as the difference between the voltage threshold and the minimum voltage between two consecutive APs, provided that the time difference between the voltage minimum and voltage threshold was less than 5 ms (larger intervals were assumed to be medium AHPs). The interspike interval (ISI) was the delay between two consecutive AP maxima, whereas the ISI adaptation ratio was defined as one minus the first divided by the last ISI. The backpropagating AP (bAP) amplitude was the maximal amplitude at a specific dendritic location during an AP elicited at the soma and the bAP delay was the time delay between the somatic and the dendritic voltage maximum. The dendritic or axonal velocity was the inverse of this delay times the path distance between the soma and the dendritic/axonal location. The Ca2+ amplitude was the local maximal amplitude following an AP elicited at the soma. The Ca2+ decay time constant was obtained by fitting a biexponential curve to the Ca2+ decay curve that followed an AP and calculating the weighted sum of the two time constants, as has been done in Stocca et al. (2008).

Individual figure panels throughout the manuscript were generated with Matlab and combined in Adobe Illustrator CS6.

### Data sharing

All compartmental models along with all simulation protocols that have been performed in this study as well as the T2N software are available on the TREES homepage (http://www.treestoolbox.org/T2N.html) and on the ModelDB public database (http://senselab.med.yale.edu/ModelDB, accession # 231862. We also uploaded a pure NEURON version of the GC model including all morphologies and biophysics but only two simulation protocols on ModelDB under the accession # 231818)

### Models of mouse and rat mature GCs and young mouse abGCs

See Appendix 2, Tables 1 and 3 for details of reconstructed and synthetic GC morphologies and ion channel properties used in compartmental simulations of GCs.
