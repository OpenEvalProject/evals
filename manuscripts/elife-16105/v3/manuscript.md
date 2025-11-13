# Molecular dynamics-based refinement and validation for sub-5 Å cryo-electron microscopy maps

## Authors

- Abhishek Singharoy<sup>1</sup> †
- Ivan Teo<sup>1</sup>
- Ryan McGreevy<sup>1</sup>
- John E Stone<sup>1</sup>
- Jianhua Zhao<sup>3</sup>
- Klaus Schulten<sup>1</sup> ([ORCID: 0000-0001-7192-9632](https://orcid.org/0000-0001-7192-9632)) †

### Affiliations

1. Beckman Institute for Advanced Science and Technology University of Illinois at Urbana-Champaign Urbana United States
2. Department of Physics University of Illinois at Urbana-Champaign Urbana United States
3. Department of Biochemistry and Biophysics University of California San Francisco School of Medicine San Francisco United States

† Corresponding author

## Abstract

Two structure determination methods, based on the molecular dynamics flexible fitting (MDFF) paradigm, are presented that resolve sub-5 Å cryo-electron microscopy (EM) maps with either single structures or ensembles of such structures. The methods, denoted cascade MDFF and resolution exchange MDFF, sequentially re-refine a search model against a series of maps of progressively higher resolutions, which ends with the original experimental resolution. Application of sequential re-refinement enables MDFF to achieve a radius of convergence of ~25 Å demonstrated with the accurate modeling of β-galactosidase and TRPV1 proteins at 3.2 Å and 3.4 Å resolution, respectively. The MDFF refinements uniquely offer map-model validation and B-factor determination criteria based on the inherent dynamics of the macromolecules studied, captured by means of local root mean square fluctuations. The MDFF tools described are available to researchers through an easy-to-use and cost-effective cloud computing resource on Amazon Web Services.

## Introduction

Cryo-electron microscopy (cryo-EM) has evolved into one of the most effective structure determination tools in modern day structural biology, achieving in recent years resolutions rivalling those of X-ray crystallography or NMR spectroscopy (Cheng, 2015). Furthermore, cryo-EM based structure determination overcomes two major bottlenecks faced in traditional X-ray crystallography, namely, the arduous task of preparing well-ordered crystals of macromolecules (Unger, 2002), and the more fundamental problem with capturing these molecules in unphysiological states as a result of crystal contacts (Neutze et al., 2015). Consequently, cryo-EM provides a natural way of resolving the structures of large macromolecular complexes.

Historically, computational methods were required to bridge the resolution gap between crystallography and cryo-EM to produce atomic-resolution models of biomolecular complexes. Various real-space refinement methods that combine crystallographic structures and cryo-EM densities for structure determination have been developed, including DireX (Schröder et al., 2007), Flex-EM (Topf et al., 2008), Rosetta (DiMaio et al., 2015), FRODA (Jolley et al., 2008), Phenix real space refinement (Afonine et al., 2013), and Molecular Dynamics Flexible Fitting (MDFF) (Trabuco et al., 2008, 2009; McGreevy et al., 2016).

MDFF, in particular, has proven to be an extremely successful refinement method as evidenced by its numerous applications (Goh et al., 2015; McGreevy et al., 2016) ranging from the intricate ribosomal machinery (Villa et al., 2009; Trabuco et al., 2011; Frauenfeld et al., 2011; Wickles et al., 2014) to a host of non-enveloped viruses (Zhao et al., 2013). So far this success has been limited to structure determination from typically low-resolution cryo-EM maps in the 7–25 Å range which, indeed, represented the state-of-the-art at the time of MDFF’s inception (Trabuco et al., 2008). However, seminal advances in detection hardware and programs over the past three years (Li et al., 2013; Milazzo et al., 2011) have enabled now the routine availability of high-resolution (<5 Å) EM maps for a range of biological systems including ion channels (Liao et al., 2013), enzymes (Bartesaghi et al., 2014, 2015), membrane fusion machinery (Zhao et al., 2015), and key functional components of the ribosome (Fischer et al., 2015; Brown et al., 2015).

High-resolution maps pose an imminent challenge to the traditional map-guided structure determination methods as the maps now characterize near-atomic scale features, the interpretation of which requires extremely precise structure building and validation protocols (DiMaio et al., 2015). For example, conformation of the protein sidechains, which are more flexible than the backbone, are now discernible within the maps and, thus, require precise modeling of the dihedral angles up to Cβ atoms while also respecting the map boundaries (Barad et al., 2015).

In order to produce atomic models with correct backbone and sidechain geometries, as well as minimal potential energy, structure determination tools must be augmented with chemically accurate force fields and exhaustive search algorithms respecting density constraints. Inspired by crystallographic modeling techniques, where such structure-building requirements have already been addressed for the resolution of 3–5 Å diffraction data (DiMaio et al., 2013; Murshudov et al., 2011; McGreevy et al., 2014), tools such as Rosetta have introduced Monte Carlo simulation-based segment building and refinement protocols with heuristic force fields (DiMaio et al., 2015), to handle high-resolution EM maps. Other notable automated model-building tools that can be used for the refinement of high-resolution EM maps include Buccaneer (Cowtan, 2006), ARP/wARP (Langer et al., 2008), and Moulder (Topf et al., 2006).

Driven by a vision to extend the capabilities of flexible fitting approaches (Topf et al., 2008; Trabuco et al., 2008; Tama et al., 2004; Suhre et al., 2006; Kovacs et al., 2008; Wu et al., 2013) for addressing high-resolution maps, two new MDFF methods are introduced here. These methods, denoted cascade MDFF (cMDFF) and resolution exchange MDFF (ReMDFF), augment the traditional MDFF method (Trabuco et al., 2008, 2009; McGreevy et al., 2016) (called direct MDFF henceforth) with enhanced conformational sampling techniques, namely simulated annealing (Brünger, 1988) and replica exchange molecular dynamics (Sugita and Okamoto, 1999). The central idea behind the techniques introduced is to fit a search model sequentially to a series of maps of progressively higher resolutions, ending with the original experimental resolution; all but the last in the series are computationally blurred lower-resolution derivatives of the original map, so that larger-scale features of the structure are determined first by fitting to the blurred densities, and smaller-scale refinements are performed subsequently during the fitting to higher-resolution densities. Altogether, this treatment enables a richer conformational sampling of the model within the map than direct MDFF, thereby allowing accurate modeling of the global and local structural features from the map; a similar treatment has previously been employed to increase the radius of convergence of MDFF protocols, but with crystallographic data (Singharoy et al., 2015).

The cMDFF and ReMDFF methods are demonstrated for structure analysis based on 3.2-Å and 3.4-Å resolution maps of β-galactosidase (Bartesaghi et al., 2014) and the TRPV1 channel (Liao et al., 2013), respectively. The two methods were found to resolve atomic structures with accuracy greater than that of direct MDFF and comparable to that of Rosetta, even with poor choices of search models. The accuracy is evaluated in terms of the quality of fit measured through global and local cross-correlations (GCC and LCC), integrated Fourier shell coefficients (iFSC), and EMRinger scores (Barad et al., 2015), as well as in terms of the quality of structural integrity measures like MolProbity (Chen et al., 2010).

In the second part of the present study we establish that structural flexibility, as measured by root mean square fluctuations or RMSF within the MDFF simulation, provides an ensemble-based indicator of local and overall resolution of a map offering, thus, a quality measure of an EM map based on the inherent dynamics of the imaged macromolecule. In line with this new finding, RMSF values are shown to provide a physical basis for the determination of optimal sharpening B-factors that maximize the signal-to-noise ratio within a map. These B-factors are determined at three different levels of model description: whole-system, per-domain, and per-residue.

Finally, use of the ReMDFF method on cloud computing platforms is discussed. Cloud computing is now a highly suitable approach for computational biology and can be employed for large-scale scientific computing, data analysis, and visualization tasks. For example, Amazon Web Services has been previously demonstrated to be a low-cost cloud computing platform for processing cryo-EM data (Cianfrocco et al., 2015). We demonstrate now the usage of Amazon Web Services, highlighting the platform’s capability for rapidly fitting structures to EM density with ReMDFF. The web-interface makes it readily possible for experimental groups around the world to deploy MDFF in an easy and economical way, bypassing the need for their own staff, software, and hardware resources.

## Results

In the following section, we first describe the methodological advances achieved within cMDFF and ReMDFF for the resolution of sub-5 Å maps. Search model preparation, refinement, and structure validation protocols based on these advances are subsequently demonstrated for five exemplary protein complexes that were chosen based on the availability of high-resolution (3–5 Å) EM maps and atomic structures. Finally, the performance of ReMDFF on Amazon’s cloud computing platforms is described, demonstrating that our MDFF software offers an efficient web-based resource for structure determination from EM maps.

### Simulation concept

In direct MDFF, an initial atomic structure is subjected to an MD simulation with an additional potential energy term $V_{EM}$ that is proportional to the sign-inverse of the EM map. Through $V_{EM}$, steering forces locally guide atoms towards high-density regions, thereby fitting the structure to the map (see Materials and methods).

The equilibrium structure obtained in the simulation represents a global minimum in VEM. For maps in the low resolution range (6–15 Å), this global minimum is broad, accomodating an ensemble of conformations defined by the overall shape of the macromolecule (Trabuco et al., 2008, 2011). In contrast, at the mid-resolution range of 4–6 Å, densities corresponding to the backbones become discernible, and at sub-4 Å resolutions, even sidechains can be resolved. At such high resolutions, VEM now features multiple proximal local minima which correspond to recurring spatial patterns within a macromolecule, such as helices aligned in parallel or strands in a β-sheet. As shown in Figure 1, the energy barriers separating these local minima are typically twice as high as those in the case of low-resolution maps. The existence of such potential minima in high-resolution maps exposes MDFF to a long-known weakness of traditional MD-based algorithms, namely entrapment of the fitted structure within undesired local minima instead of reaching the global minimum of VEM. Not unexpectedly, therefore, direct MDFF yields structurally poor or functionally irrelevant models with high-resolution EM maps (Figure 2—figure supplement 1) (DiMaio et al., 2015).

![Figure 1.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig1-v3.jpg)

**Figure 1.:** A graphic table illustrating MDFF refinement of a model of carbon monoxide dehydrogenase using a high-resolution map. The map represents an open conformation while the initial search model was obtained through crystallography of a closed conformation. This search model was independently fitted, using direct MDFF, to individual members of a set of maps obtained by applying Gaussian blurs of various half-widths ($\sigma$, first column) to the experimental density. These maps are visualized as a 3D surface in the second column, while the resulting MDFF potentials $V_{EM}$ are represented in cross-section in the third column. Notice the increase in number of contiguous density regions as $\sigma$ increases. This increase in contiguity is manifested in the lowering of high $V_{EM}$ barriers (red) for small $\sigma$ values to low or flat energy profiles (blue) for larger $\sigma$ values, as observed in the $V_{EM}$ potential cross-sections. Reduced barrier heights allow the structure to explore the conformational space freely during fitting. The structure after 500 ps of fitting, shown in red, is superimposed on the known target structure, shown in blue, in the fourth column. The time evolution of RMSD with respect to the target during fitting is shown in the fifth column. The RMSD plots show that direct fitting to lower resolution maps requires fewer time steps to reach convergence. In fact, the structure never becomes less deviated than the initial 7-Å RMSD from the target in the direct MDFF of the highest-resolution map (i.e. in the absence of Gaussian blurring). The inset shows refinements of the same structure through cMDFF and ReMDFF employing the same set of maps. A clear improvement over direct MDFF is apparent, with convergence to within 1.7 Å and 1.0 Å of the target achieved within 1000 and 100 ps for cMDFF and ReMDFF respectively.

To mitigate this weakness in direct MDFF, we introduce cMDFF and ReMDFF. In cMDFF, the structure is fitted, in a series of MDFF simulations, to maps of gradually increasing resolution. First, the experimental map is smoothened by applying a series of Gaussian blurs with increasing half-widths, σ, to obtain a set of theoretical maps with gradually decreasing resolution; σ = 0 Å corresponds to the experimental map, and σ > 0 Å corresponds to a smoothened one (see Materials and methods). Illustrated in Figure 1, the density-dependent potential derived from the smoothest map (i.e. the one with the largest σ value) features a clear global minimum representing the large-scale structural features of the protein. Second, a search model is fitted to this map, allowing resolution of these large-scale features. Third, the resulting structure is employed as the search model for fitting to the next higher-resolution map in the series. These fitting and search model refreshment steps are repeated through the series of maps in order of decreasing σ, until the structure is finally fitted to the experimental map (see Video 1 for TRPV1 refinement. An additional virtual reality version can be found at https://www.youtube.com/watch?v=UwwVC6C9tw0).

![Video 1.](https://cdn.elifesciences.org/articles/16105/elife-16105-media1.mp4.jpg)

The gradual increase in map resolution over the course of the simulations allows the structure to explore a greater conformational space than in direct MDFF. The structure thus avoids entrapment within local minima of the density-dependent potential and is accurately fitted to the near-atomic density features of the experimental map while also resolving the larger scale features.

In ReMDFF, the cascade scheme is infused with a greater degree of automation. Multiple MDFF simulation replica are run in parallel with each replica fitting a model to a map of a specific resolution. Based on a Metropolis formula analogous to that of conventional replica exchange molecular dynamics simulations (Sugita and Okamoto, 1999), but now derived in terms of density and not temperature (see Materials and methods), the models are exchanged at regular time intervals between maps from neighboring pairs of replica. Stepwise improvements in fit occur during exchanges between a poorly fitted model at a high resolution with a well-fitted model at a lower resolution. This well-fitted model is further refined against the high-resolution map until convergence is reached, and exchange between the chosen resolutions ceases. Further details are described in Materials and methods.

ReMDFF has advantages over cMDFF both in terms of efficiency and automation as it can take advantage of modern parallel computing hardware and the powerful and adaptive replica exchange interface of NAMD (Jiang et al., 2014). Nonetheless, as presented in the following, both cMDFF and ReMDFF outperform direct MDFF in quality and speed across a range of high-resolution examples.

### Search model preparation and refinement

In an initial proof-of-principle computation, cMDFF and ReMDFF were applied to fit a structure of carbon monoxide dehydrogenase to a 3-Å synthetic density map. The same techniques were subsequently applied to obtain refined structures of two more protein systems, namely TRPV1 (Liao et al., 2013) and β-galactosidase (Bartesaghi et al., 2014), for which experimental densities of 3.4 Å and 3.2 Å resolution respectively are available. In each case, a direct MDFF simulation was also performed for the purpose of comparison. The MDFF-derived structures were then subjected to a model validation analysis, to evaluate the quality of the models with established protocols in the cryo-EM field. Additional examples chosen for this analysis include γ-secretase at 4.5 Å (Lu et al., 2014) and 3.4-Å (Bai et al., 2015), β-galactosidase at 2.2-Å (Bartesaghi et al., 2015) and the proteasome at 3.3 Å (Li et al., 2013) resolution. Comparisons between the direct and advanced MDFF protocols, and wherever possible, with other available fitting techniques, such as Rosetta (DiMaio et al., 2015), elucidate the general pros and cons of the flexible fitting strategy.

#### Proof of principle

The performance of cMDFF and ReMDFF was evaluated on a test system, carbon monoxide dehydrogenase, which exhibits a closed and an open conformation (Darnault et al., 2003). Both these conformations have been crystallized, and are reported respectively in chains C and D of the PDB entry 1OAO. For our demonstration, the closed conformation (1OAO:chain C) was used as the search model, while the open one (1OAO:chain D) was the target.

First, a 3-Å resolution synthetic density map was constructed in Phenix (Adams et al., 2010), employing phases from the 1OAO structure and the associated diffraction data truncated at 3 Å. This map was then masked about chain D to yield a high-resolution envelope characterizing the open conformation. Assuming that the crystallographic model provides an accurate benchmark, the corresponding map for chain D determined here represents the best possible density data at 3 Å resolution that is experimentally attainable for the open conformation. Finally, through direct MDFF, cMDFF and ReMDFF, the search model constructed from chain C was fitted into this density to derive an atomic structure representing the open conformation. Both the cMDFF and ReMDFF refinements were performed for a set of six maps with $\sigma$ values ranging from 5 to 0 Å at constant decrements of 1 Å.

Accuracy of the fitting protocols was evaluated by comparing the fitted chain C structures with the crystallographically reported target chain D model. Direct MDFF of the 3 Å synthetic map performed for 2 ns converged to a structure with an RMSD of 7 Å relative to the target model. In sharp contrast, the cMDFF- and ReMDFF-generated structures are within 1.7 Å and 1 Å RMSD of the target (see the inset of Figure 1). It is also noted that fitting to the lowest-resolution (i.e. one with $\sigma$ = 5 Å) brings about an immediate decrease in RMSD from the target generating structures that are within 2 Å RMSD. Fitting of the structure to subsequent high-resolution maps brought the RMSD down to 1.0 Å.

The results demonstrate that the new protocols are capable of attaining well-fit structures where direct MDFF does not. In particular, one can think of the new protocols as extending the radius of convergence to at least 7 Å, rendering the fitting procedures less dependent on the quality of the starting structure.

#### Refinement of β-galactosidase

In a second test case, a search model was fitted into the 3.2 Å map (Bartesaghi et al., 2014) of β-galactosidase employing direct MDFF, cMDFF, and ReMDFF. Noting that the radius of convergence of the proposed MDFF protocols was at least 7 Å for the aforementioned test case, the initial search model was prepared such that it had an RMSD of 7 Å from the reported structure. This model was obtained by applying to the reported structure (obtained by de novo modeling within the EM map [Bartesaghi et al., 2014]) a high temperature MD protocol described in Appendix 1, Section 3 and, subsequently, choosing from the collection of trajectory structures one of RMSD 7 Å from the reported structure and with the lowest GCC with respect to the reported map (Bartesaghi et al., 2014) (Figure 2—figure supplement 2a).

Summarized in Table 1, the fitting results, in terms of quality of fit as well as model quality, are significantly better for cMDFF and ReMDFF than for direct MDFF: (i) RMSD of the fitted structure with respect to the reported de novo model is 0.7 Å and 0.9 Å for cMDFF and ReMDFF respectively, much lower than the 3.7 Å RMSD attained with direct MDFF (Figure 2—figure supplement 3a); (ii) EMRinger scores for cMDFF and ReMDFF are 3.16 and 3.45 respectively, higher than the 1.91 obtained for direct MDFF, implying accurate fitting of sidechains into the density; (iii) MolProbity scores are consistently small for all the flexible fitting techniques in part due to fewer, less severe steric clashes and fewer Ramachandran outliers (further detailed in Table 2); (iv) integrated FSC (iFSC2, corresponding to the range 3.4–10 Å on the FSC plot obtained as per Appendix 1 - Section 6), considered a more stringent measure of model quality than CC (DiMaio et al., 2015), attained higher values of 5.22 Å and 4.66 Å for cMDFF and ReMDFF, respectively, than 2.74 Å for direct MDFF. iFSC1, evaluated at the lower resolution range of 5–10 Å improves from 2.11 Å for direct MDFF to 4.22 Å and 3.76 Å for cMDFF and ReMDFF, respectively, showing a trend similar to that of iFSC2 corresponding to the high-resolution range; and (v) GCCs improved from an initial value of 0.48 to 0.56, 0.67 and 0.67 for direct, cMDFF, and ReMDFF protocols respectively. Similarly, typical residue LCC values improved from about 0 to greater than 0.80 (Figure 2—figure supplement 4a and Figure 2—figure supplement 5). Overall, cMDFF and ReMDFF refinements produce structures that interpret the 3.2-Å β-galactosidase map much more accurately than direct MDFF does. Figure 2a shows, visually, how the cMDFF-derived structure differs from the direct MDFF structure in terms of fit. In judging the RMSD values to the target model the reader is reminded that equilibrium MD simulations of a single structure at room temperature typically exhibit RMSD values relative to the initial structure or the average structure of about 3 Å; the same is true for β-galactosidase (see Figure 2—figure supplement 6 in Appendix 1 - Section 7). Consequently, an RMSD of 0.7 Å of the cMDFF/ReMDFF-fitted model relative to the target implies a high-quality refinement. The high quality of this refinement is further supported by visualizations of accurate sidechain placements within the density, shown in Figure 2—figure supplement 7.

![Figure 2.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-v3.jpg)

**Figure 2.:** Models of (a) β-galactosidase and (b) TRPV1, obtained from cMDFF (blue) and direct MDFF (red) fitting simulations are superimposed. The cMDFF-fitted models fit well into the high-resolution maps (grey) of each molecule, whereas the direct MDFF models have become trapped in local minima that result in portions of the models protruding from the maps. ReMDFF-fitted models are almost identical to those from cMDFF and are therefore not shown.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** The blue and red structures represent the same region of a segment of TRPV1 that have been fitted differently into the density map shown. The global cross-correlations of the structural region shown in each case are 0.728 (red) and 0.723 (blue). However, the blue structure is clearly better fitted than the red structure, as reflected in RMSDs from the published structure of 6.2 Å (red) and 2.3 Å (blue). Although the case described is an extreme one, it shows that global cross-correlation, as a measure of fit, can be misleading, particularly in regards to local correspondence of residues to the map.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** For the purpose of testing cMDFF on (a) β-galactosidase and (b) TRPV1, the published models (blue) were distorted to provide the initial models (red) for fitting. In the case of TRPV1, the distortion was applied to only one subunit.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** RMSD over simulation time is plotted for the cMDFF, ReMDFF, and direct MDFF simulations of (a) β-galactosidase and (b) TRPV1 monomer. RMSD is calculated with respect to the published models (PDB 3J7H for 3.2-Å resolution and PDB 5A1A for 2.2-Å resolution). For ReMDFF, the plot contains data from a single, best-fit, replica. (inset) Same as (b) but now for the TRPV1 tetramer. For both β-galactosidase, and TRPV1 monomer and tetramer, cMDFF and ReMDFF outperformed direct MDFF in terms of both efficiency and fitting accuracy, as reflected in Tables 1 and Supplementary file 1A.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp4-v3.jpg)

**Figure 2—figure supplement 4.:** Local cross-correlations of residues within the fitted regions of (a) β-galactosidase and (b) TRPV1 plotted over the course of the cMDFF fitting show improvement over the successive MDFF refinement steps.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp5-v3.jpg)

**Figure 2—figure supplement 5.:** Local cross-correlations of residues within the fitted regions of (a) β-galactosidase and (b) TRPV1 plotted over the course of direct MDFF of the respective de novo structures show little change. The large-scale structure of the starting de novo models are already well-fitted within the maps, increases in fit and overall structure quality of the refined de novo structures over the starting structures are thus due to local, sporadic improvements.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp6-v3.jpg)

**Figure 2—figure supplement 6.:** The model resulting from a cMDFF fitting of β-galactosidase to the 3.2-Å map is subject to an equilibration MD simulation. The RMSD plot of the structure shows that it converges within 10 ns to an RMSD value of 3 Å.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp7-v3.jpg)

**Figure 2—figure supplement 7.:** Several examples of residue segments, consisting of residues (a) 50–55, (b) 179–189, (c) 310–320, and (d) 413–420, are shown within the corresponding map regions. In general, both backbone and sidechains were found to have fitted well after MDFF refinement.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig2-figsupp8-v3.jpg)

**Figure 2—figure supplement 8.:** The reported structures for (a) β-galactosidase and (b) TRPV1 were each fitted by direct MDFF against two half-maps, labelled 1 and 2, from their respective EM data. Simulated maps were generated from the resulting structures, with labels corresponding to the half-maps used in the fitting. FSC plots of the simulated maps against the half-maps are so similar that they superimpose on one another. In addition, the differences in iFSCs between the various plots are negligible. These results demonstrate that the MDFF method, with the parameters used in the present study, does not overfit the structure.

**Table 1.**
 β-galactosidase MDFF results. cMDFF and ReMDFF provide better fitted structures than direct MDFF according to various criteria. It is noteworthy that all structures refined by any form of MDFF display an improved MolProbity (Chen et al., 2010) score compared to the original de novo structure.


<table>
  <thead>
    <tr>
      <th>Structure</th>
      <th>RMSD(Å)</th>
      <th>EMRinger</th>
      <th>iFSC1(Å)</th>
      <th>iFSC2(Å)</th>
      <th>MolProb.</th>
      <th>GCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>de novo (Bartesaghi et al., 2014)</td>
      <td>0.0</td>
      <td>2.25</td>
      <td>4.03</td>
      <td>5.00</td>
      <td>3.14</td>
      <td>0.67</td>
    </tr>
    <tr>
      <td>Refined de novo</td>
      <td>0.6</td>
      <td>4.23</td>
      <td>4.19</td>
      <td>5.20</td>
      <td>1.23</td>
      <td>0.68</td>
    </tr>
    <tr>
      <td>Initial</td>
      <td>7.7</td>
      <td>0.24</td>
      <td>0.14</td>
      <td>0.15</td>
      <td>1.49</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>Direct MDFF</td>
      <td>3.7</td>
      <td>2.31</td>
      <td>2.11</td>
      <td>2.74</td>
      <td>1.38</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>cMDFF</td>
      <td>0.7</td>
      <td>3.16</td>
      <td>4.22</td>
      <td>5.22</td>
      <td>1.37</td>
      <td>0.67</td>
    </tr>
    <tr>
      <td>ReMDFF</td>
      <td>0.9</td>
      <td>3.45</td>
      <td>3.76</td>
      <td>4.66</td>
      <td>1.13</td>
      <td>0.67</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Structure quality indicators for β-galactosidase structures. β-galactosidase structures investigated in the present study were uploaded to the MolProbity server (http://molprobity.biochem.duke.edu) to extract the quantities presented below. The results show that the cMDFF- and ReMDFF-refined structures not only exhibit good measures of fit, but also improve the clash score and rotamer geometries, relative to the de novo and initial structures, while incurring only a small expense in Ramachandran statistics, bad angles, and Cβ deviations.


<table>
  <thead>
    <tr>
      <th></th>
      <th>de novo (Bartesaghi et al., 2014)</th>
      <th>Refined de novo</th>
      <th>Initial</th>
      <th>Direct MDFF</th>
      <th>cMDFF</th>
      <th>ReMDFF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Clashscore</td>
      <td>53.7</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>Poor rotamers (%)</td>
      <td>11.6</td>
      <td>3.8</td>
      <td>4.2</td>
      <td>3.0</td>
      <td>4.4</td>
      <td>1.37</td>
    </tr>
    <tr>
      <td>Favored rotamers (%)</td>
      <td>67.4</td>
      <td>90.8</td>
      <td>87.8</td>
      <td>92.1</td>
      <td>89.8</td>
      <td>95.3</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>2.7</td>
      <td>3.0</td>
      <td>1.6</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>97.4</td>
      <td>95.8</td>
      <td>91.1</td>
      <td>91.1</td>
      <td>94.4</td>
      <td>90.9</td>
    </tr>
    <tr>
      <td>MolProbity</td>
      <td>3.14</td>
      <td>1.23</td>
      <td>1.49</td>
      <td>1.38</td>
      <td>1.37</td>
      <td>1.13</td>
    </tr>
    <tr>
      <td>Cβ deviations (%)</td>
      <td>0.0</td>
      <td>0.05</td>
      <td>4.92</td>
      <td>0.18</td>
      <td>0.29</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td>Bad bonds (%)</td>
      <td>0.09</td>
      <td>0.04</td>
      <td>3.61</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>Bad angles (%)</td>
      <td>0.03</td>
      <td>0.60</td>
      <td>3.98</td>
      <td>0.63</td>
      <td>0.49</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>RMS distance (Å)</td>
      <td>0.007 (0.025%)</td>
      <td>0.019 (0%)</td>
      <td>0.035 (0.237%)</td>
      <td>0.022 (0%)</td>
      <td>0.019 (0%)</td>
      <td>0.021 (0%)</td>
    </tr>
    <tr>
      <td>RMS angle (degrees)</td>
      <td>1.1 (0.009%)</td>
      <td>2.2 (0.009%)</td>
      <td>3.6 (1.177%)</td>
      <td>2.4 (0.103%)</td>
      <td>2.1 (0.018%)</td>
      <td>2.3 (0.085%)</td>
    </tr>
    <tr>
      <td>Cis prolines (%)</td>
      <td>8.06</td>
      <td>8.06</td>
      <td>6.45</td>
      <td>6.45</td>
      <td>6.45</td>
      <td>8.06</td>
    </tr>
    <tr>
      <td>Cis non-prolines (%)</td>
      <td>1.15</td>
      <td>1.15</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.15</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

The cMDFF- and ReMDFF-refined structures were found to be comparable in every quality measure in comparison to the reported de novo structure (Bartesaghi et al., 2014); in fact, the overall Molprobity and EMRinger scores are significantly better in cMDFF and ReMDFF. However, a closer look at the Molprobity score (Table 2) reveals that even though cMDFF vastly improves clash score and poor rotamers, it marginally increases the percentage of Ramachandran outliers and Cβ deviations relative to the de novo structure. Nonetheless, both cMDFF and ReMDFF improved structural statistics with respect to the initial model (Table 1, third row) which was intentionally chosen to have a large deviation (RMSD of 7.7 Å) from the de novo structure.

Noting that the quality of MDFF output depends strongly on that of the search model, a second cMDFF simulation was also performed to refine the de novo structure within the reported map. The simulation, labeled ‘refined de novo’ in Table 1, yielded a structure that was superior in all the quality measures considered in comparison to the de novo structure as well as to the structures obtained from the various MDFF fittings of the other, 7.7 Å deviated initial model. A closer look at the Molprobity scores (Table 2) now reveals that not only are clash score and poor rotamers vastly improved, but the Ramachandran outliers and Cβ deviations are also comparable to the de novo structure.

A third cMDFF refinement was further performed with a search model of even lower structural quality (Supplementary file 1E, third row) compared to that of Table 1 (third row). Structural statistics for the refinements from this lower-quality search model are provided in Supplementary file 1F. Comparison of the three cMDFF refinements starting with three search models of varying structural quality reveal that the poorer the secondary structure of the search model, measured in terms of higher percentages of rotamer and Ramachandran outliers, the worse the local structural statistics of the MDFF/cMDFF/ReMDFF-refined model. Surprisingly, large scale map-model validation measures, such as RMSD, GCC, or iFSC values, remain insensitive to such local discrepancies in the refined model. This insensitivity is apparent in the similarity of RMSD, GCC, and iFSC values of the three refined models of β-galactosidase (Table 1 and Supplementary file 1E), which indeed feature very different number of Ramachandran outliers: 0.7% (Table 2-Refined de novo), 1.6% (Table 2-cMDFF) and 7.8% (Supplementary file 1F-cMDFF).

The high-precision of sub-5 Å maps demands correct assignment of secondary structure, which determines backbone geometry directly and sidechain conformations indirectly. In light of the initial model quality dependence of MDFF, it is advisable to begin refinement with an initial model of maximal secondary structure information, yet with minimal tertiary structure. Dependable initial secondary structure is also required since MD simulations have limited capability of recovering the structure of a protein fold if the search model begins with a random coil conformation (Freddolino et al., 2010). To this end, notwithstanding observed cMDFF improvements of the secondary structure (Table 2 columns 4 vs. 6, and also demonstrated for γ-secretase [Supplementary file 1D]), moderate- to high-confidence homology models will serve as the most optimal starting point, as has been successfully shown for MDFF with low-resolution EM (Chan et al., 2011; Noble et al., 2013; Wickles et al., 2014) and crystallographic data (McGreevy et al., 2014; Li et al., 2014). Quantitatively speaking, employing the current example (β-galactosidase) and the following one (TRPV1), it is now shown that a search model which deviates from the target by an RMSD of 7–25 Å featuring Ramachandran outliers of ~3%, poor rotamers of 11–38%, overall Molprobity score of ~4 and EMRinger score of ~0.20 can be accurately refined against a sub-5 Å EM map with cMDFF or ReMDFF.

In terms of efficiency, the ReMDFF protocol exhibits the quickest convergence, arriving at steady state within 0.1 ns of simulation, whereas cMDFF requires around 0.8 ns. Both methods employed eleven maps with Gaussian blurs starting from a width of 5 Å and decreasing in steps of 0.5 Å towards the original reported map. To ensure that the cMDFF procedure did not over-fit the structures, cross-validation using EMRinger and FSC analysis was performed using half-maps from the EMD-5995 entry. iFSC and EMRinger values were found to be almost identical in both direct and cross comparisons. Details are provided in Appendix 1 - Section 11.

In addition to the MDFF simulations described so far for β-galactosidase, other simulations were performed to investigate in more detail the capabilities of MDFF. These simulations are described in Appendix 1 - Section 7. First, it was found that fitting of the Cβ atoms to the density is crucial for accurate placement of the sidechains. In agreement with prior EMRringer results (Barad et al., 2015), it is confirmed that MDFF placement of the backbone does not guarantee correct sidechain geometries, even with state-of-the-art CHARMM36 (Klauda et al., 2010) force fields. Second, MD simulation of the cMDFF-fitted β-galactosidase model revealed that this model is indeed an excellent representation of the most probable structures of the thermodynamic ensemble that characterizes the 3.2 Å map.

#### Refinement of TRPV1

In the third test case, cMDFF and ReMDFF protocols were employed to fit an initial model to the 3.4-Å map (Liao et al., 2013) of the temperature-sensing protein TRPV1. The search model was prepared from the reported de novo structure through an interactive MD protocol described in Appendix 1 - Section 3. The model deviated from the de novo structure by an overall RMSD of 10 Å and locally, by about 25 Å in the vicinity of the ankyrin repeats represented by residues 199 to 430. This degree of deviation is in the ballpark of the lowest resolutions of usable EM maps and, therefore, represents the upper limit of uncertainty between a search model and the fitted structure that MDFF can still reconcile. Having to address an RMSD of 25 Å between search and target models, the present example represents an extreme test case for judging the radius of convergence of the proposed MDFF methods.

Fitting results for TRPV1, described in Appendix 1 - Section 8, were significantly better for cMDFF and ReMDFF than for direct MDFF, but now with much poorer search models than those employed for the β-galactosidase refinements. For example, cMDFF and ReMDFF refinements produced structures that interpret the 3.4-Å TRPV1 map within an RMSD of 2.4 Å and 2.5 Å from the target de novo model, much more accurately than does direct MDFF which converges to structures at an RMSD of 7.9 Å.

The cMDFF- and ReMDFF-obtained structures were found to be better in every overall quality metric in comparison to the de novo structure. Figure 2b illustrates the contrast in fit between the cMDFF and direct MDFF-derived structures. To observe the effect of MDFF on a substantially well-fitted initial structure, a direct MDFF simulation was also performed to refine the de novo structure within the reported map. The simulation yielded a structure that was comparable in all the quality measures considered to the structures obtained from cMDFF and ReMDFF (Appendix 1 - Section 8). However, the TRPV1 fitting results show that cMDFF and ReMDFF can have a radius of convergence as high as 25 Å in RMSD, whereas direct MDFF requires at the outset a well-fitted structure to deliver a satisfactory model. Also, since the number of Ramachandran outliers were minimal in both the 25 Å-deviated and de novo initial models, the cMDFF, ReMDFF, and direct MDFF-refined models exhibited low percentages of Ramachandran outliers, as reflected in Supplementary file 1B.

As was observed already for β-galactosidase, the ReMDFF protocol exhibited the quickest convergence, arriving at steady state within 0.02 ns of simulation, whereas cMDFF required around 0.27 ns. Both methods employed six maps with Gaussian blurs starting from a width of σ = 5 Å and decreasing in steps of 1 Å to the reported σ = 0 Å map. Cross-validation with half-maps was also performed on the cMDFF structure, as per the β-galactosidase simulations, to ensure that it was not over-fitted. As in the case of β-galactosidase, iFSC and EMRinger scores for direct and cross comparisons were similar. FSC analysis results are described in Appendix 1 - Section 11.

A separate set of model validation analyses was performed on the well-resolved TM portion of TRPV1 to pursue a direct comparison of a MDFF refined model with one from Rosetta (Barad et al., 2015). As reported in Appendix 1 - Section 9, MDFF produced results comparable to those of Rosetta when all the heavy atoms are coupled to the density: though the EMRinger score is marginally lower relative to that from Rosetta, the GCC and iFSCs are higher for MDFF; also MDFF provides a marginally higher MolProbity score. Altogether, major discrepencies between Rosetta and direct MDFF that were reported for the high-resolution EM maps (DiMaio et al., 2015) are now absent when employing the cMDFF and ReMDFF protocols, even with poorer choices of search models than those used with Rosetta. Thus, cMDFF and ReMDFF enable flexible fitting techniques to pursue resolution of structures within state-of-the-art maps obtained via cryo-EM.

### Model validation

An EM density map represents a thermodynamic ensemble of atomic conformations (Schröder et al., 2007; Brunger et al., 2012; Schröder et al., 2010). Conventionally, however, only a single model representing a best fit to the map is reported. One may ask how statistically representative a single model can be. To quantify the deviation of a fitted model from the rest of an ensemble of simulated molecules, root mean square fluctuation (RMSF) of the model relative to the ensemble-averaged structure was computed during an MDFF refinement simulation employing the protocol described in Methods. In the following, the RMSF of a fitted model is first shown to be indicative of the quality of fit of the model, as well as to represent the degree of natural conformational variation exhibited within the thermodynamic ensemble underlying the map. Second, the RMSF values are found to correlate both locally and globally with the resolution of an EM map, providing an interpretation of map quality based on the inherent (i.e., natural) dynamics of the macromolecule under observation. Finally, RMSF values are also employed to identify optimal B-factor values for the sharpening of a map. Altogether, the results of the present study demonstrate that RMSF of a fitted model during an MDFF refinement provides valuable information on the model.

#### RMSF and quality of fit

The relationship between RMSF values and quality of model fit is demonstrated for the cMDFF refinement of β-galactosidase at 3.2 Å resolution. The initial conformation is a poor fit of the map, characterized by low values of GCC, LCC, and iFSC (the row containing ‘initial’ structure in Table 1). Such conformations belong to a diverse ensemble of poorly fit structures, explored by the search model in the early phase of the fitting, that gives rise to high initial RMSF values shown in Figure 4—figure supplement 1. In the ending phase of the refinement, well-fitted structures are obtained with improved GCC, LCC, and iFSC (cMDFF row of Table 1). Owing to the high resolution (3.2 Å) of the EM density map, the population of these well-fitted structures is much smaller than that of partially-fitted structures. Thus, as can be observed in Figure 4—figure supplement 1, the converged ensemble of the well-fitted structures exhibit much smaller fluctuations than the initial one. Low RMSF values for the fitted structure indicate therefore, that (i) the structure has been modeled unambiguously within the map, and (ii) the structure can be regarded as representative of the ensemble underlying the 3.2-Å β-galactosidase map; since per-residue fluctuations about the fitted structure (Figure 4—figure supplement 1) are less than 1 Å, only marginal backbone and sidechain variations within the ensemble arise (Singharoy et al., 2013).

#### RMSF and quality of map

Apart from representing the quality of fit, RMSF values monitored during an MDFF simulation correlate closely with the overall and local resolution of an EM map. Even though high-resolution cryo-EM data are becoming increasingly obtainable, resolution is not always uniform throughout a map. For example, Figure 3 reflects the variation in local resolution of map regions corresponding to residues of β-galactosidase and TRPV1. Conformational flexibility can cause heterogeneity in the cryo-EM data (Leschziner and Nogales, 2007), producing local resolutions lower than that of the overall map.

![Figure 3.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig3-v3.jpg)

**Figure 3.:** The published models of (a) β-galactosidase (PDB 5A1A) and (b) TRPV1 (PDB 3J5P) are colored by the local EM map resolutions, the per-residue mean square fluctuations (RMSF$^{2}$) during MDFF simulation, and published B-factors. Comparison of these figures shows qualitative agreement between local resolution, RMSF$^{2}$, and B-factor. In fact, the local resolutions and B-factors correlate linearly with RMSF$^{2}$ of a fitted model both in the presence as well as absence of the EM map (more details in Figure 4).

Local resolution analysis (Kucukelbir et al., 2014) can be especially important for determining the parts of a high-resolution map that realistically contain side chain information and the parts that do not, preventing over-interpretation of the latter. MDFF protocols can be adjusted to account for such local variations and better inform the process of model validation. For example, if analysis shows that certain residues reside in low-resolution regions of the density, the per-atom weighting factor applied to the forces derived from the density can be lowered.

The RMSF-resolution correlation is found to hold in the cases of TRPV1 (PDB 3J5P), 2.2-Å β-galactosidase (PDB 5A1A), γ-secretase (PDB 5A63 and 4UPC), and the T20S Proteasome (PDB 3J9I). Generally, the lower the resolution of the map, the higher the corresponding overall RMSF during MDFF simulations. For example, the overall RMSF during MDFF of the 4.5-Å γ-secretase model and map is greater than that of the 3.4-Å model and map which, in turn, is greater than that of the 2.2-Å map and model of β-galactosidase (see RMSF labels on the upper column of Figure 4). The correlation between map resolution and model RMSF extends further to local features within the density. In Figure 4 (upper row), RMSFs of atoms plotted against local resolutions of the corresponding map regions display linear correlation between the two quantities. Again, higher RMSF indicates lower local resolution.

![Figure 4.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig4-v3.jpg)

**Figure 4.:** For each test case shown, atoms in the MDFF-refined structure are classified by local resolution of the map regions they are fitted into. The average RMSF value of atoms (during MDFF simulation) in each resolution bin is calculated and plotted against the local resolution in the cases of (a) β-galactosidase (β-gal) at 2.2 Å, (b) TRPV1 at 3.4 Å, γ-secretase (γ-sec) at (c) 3.4 Å and (d) 4.5 Å resolution, and proteasome (see Figure 4—figure supplement 3). The numbers of atoms in the resolution bins are displayed as a histogram (in red) spanning a system-specific range of resolutions. The lowest resolution bins contained low (<20) populations and visual inspection consistently revealed the atoms to be on the edges of the density or were otherwise located inside map noise, and were therefore ignored during further analysis. A clear linear correlation between RMSF and local resolution can be found in each case, such that applying a linear fit produces the high $R^{2}$ value shown in each graph heading. Also displayed in each heading is an overall RMSF, averaged over all atoms in the system. The overall RMSF reflects the conformational variety of structures that fit within the map, and is found to correspond to the map resolution such that higher resolutions produce lower RMSFs. The second row of plots show that the RMSF during MDFF simulation also linearly correlates with RMSF during unbiased MD simulations of (e) β-gal, (f) TRPV1 and (g,h) γ-sec, establishing that fluctuations during MDFF reflect the inherent flexibility of a system.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Residue RMSFs as a function of progress of cMDFF fitting show a general trend of decrease as the structure becomes better fit.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Published models corresponding to the 2.2-Å and 3.2-Å maps of β-galactosidase are fitted to their respective maps using direct MDFF. The RMSF values of all the residues along the protein sequence are plotted showing those from the 2.2-Å map are lesser than those from 3.2-Å map.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** In the proteasome test case, the average RMSF of atoms corresponding to each local resolution, determined by ResMap, correlates linearly with the resolution. The same correlation was observed in all test cases considered (see Results).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig4-figsupp4-v3.jpg)

**Figure 4—figure supplement 4.:** (a) Local cross-correlation and (b) EMRinger scores obtained from residues of a fitted model of TRPV1 do not exhibit one-to-one correspondence to local map resolutions.

The physical basis for considering RMSF values of a group of fitted atoms during an MDFF refinement as an indicator of the map resolution follows from the linear correlation of these values with RMSF of the same set of atoms during unbiased MD (Figure 4, bottom row). Noting that the RMSF value during unbiased MD simulations reflects flexibility (Karplus, 1990), this linear correlation clearly establishes the dependence of RMSF during MDFF refinement on the inherent flexibility of the macromolecule, at least for our four demonstration systems (see Appendix 1 - Section 2 for MD simulation details). Since the flexibility of a molecule during the imaging process contributes to the limiting resolution of the resulting EM density map (Kucukelbir et al., 2014), it is not surprising that overall and local map resolutions correlate with overall and local RMSF values of the best fitted model (Figure 4).

In broad terms, through the present study we establish that RMSF, together with GCC, LCC, EMRinger (Barad et al., 2015), and iFSC, provide a comprehensive set of criteria for evaluating model and map quality on both global and local levels. The added value of RMSF is particularly evident on the local level, where the other measures may not perform as consistently. For example, a high LCC may be the result of a highly flexible structure fitting to a low-resolution region of the map, and not necessarily of a good representation of the local structure. As a result, although multiple low-resolution regions of the model in Figure 4—figure supplement 2a possess similar LCCs, disparate RMSFs of the same regions clearly indicate differences in local quality of the model. Likewise, EMRinger scoring, when applied to small groups of residues, does not correlate with local resolution (Figure 4—figure supplement 2b), and, therefore, is incapable of distinguishing regions of small number of atoms by local model quality. In contrast, RMSF clearly resolves local resolution, and, thus, resolves the map and model quality even with as few as 100 atoms.

#### RMSF and B-factor determination

High contrast within an EM map allows clear identification of secondary structural elements. However, experimental imaging discrepancies arising from specimen movement and charging, radiation damage, and partial microscope coherence, or computational discrepancies due to inaccurate determination of the single particle order parameters (Wade, 1992; Fernández et al., 2008), introduce fuzziness to the EM map, thus hindering secondary structure identification. B-factor sharpening restores lost contrast by resolving the fuzzy features and, therefore, is a crucial step of map generation that affects map interpretation. Here, we describe the use of RMSF as a physical basis for the determination of optimal B-factors that preserve contrast during map sharpening.

Figure 5, Figure 5—figure supplement 3, Figure 4—figure supplement 4 demonstrate the relationship between RMSF and B-factor for the 2.2-Å map of β-galactosidase, 3.4-Å map of TRPV1 and 4.5-Å map of γ-secretase; these three systems were chosen due to their reasonable size and availability of unsharpened data. An initial decrease in the RMSF values is observed with increase in B-factor sharpening of the map. However, the RMSF eventually reaches a minimum before increasing as the B-factor is further increased. Surprisingly, for all the three structures the B-factor corresponding to the minimum RMSF coincides with the one determined by Guinier analysis (Fernández et al., 2008; Rosenthal and Henderson, 2003) to provide maximum contrast. In fact, for TRPV1, B-factors determined from the RMSF minima are found to be higher for the soluble regions than for the transmembrane helices (Figure 5—figure supplement 1, b vs. c), again, in agreement with those B-factors derived from the Guinier analysis. Therefore, the RMSF analysis of maps with varying B-factor sharpening provides an alternate procedure for the determination of the optimal B-factor, which has been traditionally determined by Guinier analysis.

![Figure 5.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig5-v3.jpg)

**Figure 5.:** (a) Overall RMSF of a fitted 2.2Å β-galactosidase structure (PDB 5A1A) during direct MDFF fitting as a function of the B-factor of the fitting map exhibits a parabolic trend. Guinier analysis identifies a B-factor of −75 as optimal, for which the corresponding RMSF (shown in red) coincides with the minimum of the trend line. EMRinger scores (shown in blue) of the same structures show a negative parabolic trend, with the peak coinciding with the minimum of the RMSF plot. (b) The linear relationships between local RMSF during MDFF and during unbiased MD for the unsharpened map and optimally sharpened map are compared. While the linear relationship is preserved in both cases, RMSFs in the sharpened case are slightly lower than in the unsharpened case.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** RMSF values of a fitted TRPV1 structure during MDFF fitting as a function of the B-factor of the fitting map exhibits a parabolic trend. This trend is prsented for (a) the whole protein, (b) the soluble region, and (c) the transmembrane domain. Guinier analysis identifies a B-factor of −100 as optimal for the whole protein as well as the transmembrane domain; the soluble region is characterized by a B-factor of −150. These B-factors are in close agreement with those representing a minimal RMSF: −100 (whole protein), −150 to −200 (soluble region), −100 to −125 (transmembrane domain).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** (a) Overall RMSF of a fitted γ-secretase structure during MDFF fitting plotted as a function of the B-factor of the fitting map forms a parabola. Guinier analysis of map sharpening identifies a B-factor of −131 as optimal. The corresponding RMSF (shown in red) lies close to the minimum of the parabola. (b) The linear relationships between local RMSF during MDFF and during unbiased MD for the unsharpened map and the sharpened map of B-factor −100 are compared. For all but the first resolution bin, RMSF for the sharpened map is higher than that of the unsharpened map. However, the first resolution bin contains about 98% of atoms in the structure, so that atoms in the other bins are outliers, which fall into map regions of non-optimal local resolution.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig5-figsupp3-v3.jpg)

**Figure 5—figure supplement 3.:** For the cases of (a) β-galactosidase and (b) γ-secretase, the reported model was fitted to maps sharpened with various B-factors. EMRinger scores for the fitted model/map pairs are plotted against the corresponding B-factors. The maxima of the plots, at B-factors −50 and −100 for β-galactosidase and γ-secretase respectively, correspond with the RMSF minima in Figures 4a and 4—figure supplement 1a.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/16105/elife-16105-fig5-figsupp4-v3.jpg)

**Figure 5—figure supplement 4.:** The B-factor, measured for each atom employing the relationship 8π2/3(RMSF)2 employing RMSF values from Figure 3 (black line), are fairly comparable to the B-factors reported experimentally (red rhombus). An overall cross-correlation of 55% is found between these two sets of B-factors.

The rationale for optimal B-factor selection based on an analysis of RMSF values is the following. As pointed out above and in Figure 4, RMSF of a fitted model is a function of the quality of the corresponding map. Following this argument, the maps in Figure 5, Figure 5—figure supplement 1 and Figure 5—figure supplement 2 that produce the model with the lowest RMSF during fitting represent the density envelopes where atoms can be positioned with the least uncertainty at the given experimental resolutions. The corresponding sharpening B-factor thus provides the optimal contrast for atom placement and secondary structure determination.

Our argument for the RMSF-based selection of B-factors is supported by the well-established quadratic relationship of B-factors with the RMSF of atoms of a structure in an experimental setting, i.e. 8π2/3(RMSF)2 (Rosenthal and Henderson, 2003; Liu and Xiong, 2014). This relationship indeed implies that the smaller the average atomic fluctuations, the lower are the B-factors, and by definition (Liu and Xiong, 2014) the higher are the measured structure factor amplitudes, and hence the contrast, of the resulting map in both crystallographic and EM experiments (Liu and Xiong, 2014; Fernández et al., 2008). By analogy, RMSF within MDFF is a measure of these average atomic fluctuations under the experimental setting (Figure 4, bottom row) and, therefore, within a set of maps of varying B-factors, the highest contrast is indicated by the lowest RMSF obtained during fitting of a model. Since Guinier analysis of EM data selects B-factors based on the same atomic displacement-structure factor relationship that justifies the RMSF-based selection of B-factors (Rosenthal and Henderson, 2003), the B-factor selected from our analysis of the lowest RMSF matches excellently with those from the Guinier analysis of EM maps.

The higher contrast of the B-factor sharpened map, over the unsharpened one, is evident from the higher quality of the models derived from the sharpened maps. Presented in Figure 5a, Figure 5—figure supplement 3b, and Figure 5—figure supplement 1a, for the cases of β-galactosidase, γ-secretase, and TRPV1, respectively, are EMRinger scores of models fitted to unsharpened and sharpened maps. These scores indicate clearly that the models derived from maps at B-factor sharpening of −50 (Figure 5a), −100 (Figure 5—figure supplement 3b), and −100 (Figure 5—figure supplement 1a) are more accurate than those derived from the unsharpened ones. Indeed, as further illustrated in Figure 5a, Figure 5—figure supplement 3b, and Figure 5—figure supplement 1, the maximum EMRinger score is attained for the same B-factor that produces the minimum RMSF. Sharpening by B-factors of magnitudes any higher than 50 for β-galactosidase, and 100 for γ-secretase or TRPV1 damages key density features thus reducing the quality of the associated fitted models. In addition, correlation of the RMSF of the fitted structure with that from an unbiased MD of the system is still preserved (Figure 5b and Figure 5—figure supplement 2b) for the B-factor sharpened map, confirming that the dynamical fluctuations of the structure within the sharpened map reflects the inherent dynamics of the system. Altogether, RMSF establishes a unique map-model validation criterion that represents an ensemble view of the fitted structures, while also preventing over-sharpening of the EM maps.

#### RMSF and per-residue B-factors

The quadratic relationship between RMSF and B-factors can be further employed to determine per-residue B-factors. Presented in Figure 3, the per-residue RMSF$^{2}$ of β-galactosidase and TRPV1, derived from MDFF, show excellent agreement with the distribution of local resolution and experimentally reported B-factors: regions with higher RMSF2 correspond to lower local resolution and higher per-residue B-factors, and vice versa. In fact, the quantitative agreement between the B-factors derived from MDFF through the computation of 8π2/3(RMSF)2 (0.02 $<$ (RMSF)2$<$4.43 [Figure 3]) and those reported in the experiments is remarkable (Figure 5—figure supplement 4); a cross-correlation of 55% is found between the data sets, which improves to 60% in the structured regions. Larger discrepencies are observed between the RMSF-based and reported B-factors of TRPV1, particularly in the soluble region (Figure 3b). This discrepency is expected, as for poorly resolved regions MD provides up to six-fold higher B-factors (Kuzmanic et al., 2014); the higher B-factors indeed have been demonstrated to be a more accurate representation of conformational diversity (Kuzmanic et al., 2014). For the TRPV1 example, the highest computed B-factor is 8π2/3*9.25 = 240.5 (Figure 3b) compared to the reported value 53.17. However, the majority of the computed B-factors fluctuatate about the value of 8π2/3*1.73 = 44.98, which is in fair agreement with the reported values of 20–30.

Overall, B-factors of cryo-EM maps are typically calculated by Guinier analysis for maps with resolutions better than ~10 Å (Fernández et al., 2008; Rosenthal and Henderson, 2003). Using a mask around specific regions of interest, estimation of local B-factors for different parts of a map is also possible. However, this method is limited to large domains of macromolecular complexes due to problems associated with tight masking of cryo-EM maps. For maps with resolutions better than ~3 Å, local B-factors could be estimated and refined in X-ray crystallography programs. However, most highresolution cryo-EM maps have resolutions between 3 to 5 Å (Liao et al., 2013; Bartesaghi et al., 2014; Zhao et al., 2015; Fischer et al., 2015). In this resolution range, B-factors could be estimated from MDFF and used as prior information to improve model building and refinement. For resolutions better than 3 Å, MDFF-derived values may serve as initial estimates of B-factors. Furthermore, many cryo-EM maps show local variations in resolution, complicating the model building process. A possible solution may be to combine local B-factor refinement for highresolution regions of a map and B-factors derived from MDFF for lower resolution regions. A resolution-dependent weighting scheme could be incorporated to combine the different values for optimal performance, which may help improve the accuracy of atomic models derived from high-resolution cryo-EM maps.

### Accessibility through cloud computing

ReMDFF involves many independent, though sporadically communicating, MDFF simulations that can be run well on a parallel computer as exploited by the NAMD software for the case of replica exchange simulations (Jiang et al., 2014). As a result, ReMDFF provides an efficient and automated method which can converge on a final fitted structure more quickly than direct or cMDFF (Figure 2—figure supplement 3). However, a potential bottleneck may exist with respect to the computing hardware that a researcher has access to. Cloud computing offers a potential solution, allowing a researcher to focus on the scientific challenges of their project without having to worry about local availability and administration of suitable computer hardware.

To prove the feasibility of performing ReMDFF simulations on a cloud platform, we performed ReMDFF for a test system, carbon monoxide dehydrogenase (PDB 1OAO:chain C), on the Amazon Web Services (AWS) Elastic Compute Cloud (EC2) platform. The test system converges to the known target structure in approximately 0.1 ns simulation time. The time to convergence requires very little wall clock time, and, therefore, incurs a small monetary cost to a user (Table 3). However, it should be noted that human error and varying experience level can easily add to the incurred cost of cloud usage. Some systems may require multiple simulations to achieve a high quality structure and, therefore, additional time beyond the example discussed here. Furthermore, preparing a structure for simulation may require additional time and resources over the purely simulation-oriented results presented here. The files and information necessary to run ReMDFF on the test system using EC2 cloud computing resources are available at (http://www.ks.uiuc.edu/Research/cloud/). The Implementation section of the Methods contains further details for setting up and running ReMDFF simulations.

**Table 3.**
 Performance and cost results for ReMDFF of carbon monoxide dehydrogenase on Amazon Web Services (AWS) Elastic Compute Cloud (EC2) platform. Costs are incurred on a per-hour basis, with a 1 hr minimum.


<table>
  <thead>
    <tr>
      <th>Instance type</th>
      <th>CPU</th>
      <th>Performance (ns/day)</th>
      <th>Time (hours)</th>
      <th>Simulation cost ($)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>c3.8xlarge</td>
      <td>30</td>
      <td>5.88</td>
      <td>0.41</td>
      <td>1.68</td>
    </tr>
    <tr>
      <td>c3.4xlarge</td>
      <td>12</td>
      <td>3.33</td>
      <td>0.72</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>c3.2xlarge</td>
      <td>6</td>
      <td>1.35</td>
      <td>1.78</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>

## Discussion

Flexible fitting methods have facilitated structure determination from low-resolution EM maps for more than a decade (Tama et al., 2004; Suhre et al., 2006; Velazquez-Muriel et al., 2006; Orzechowski and Tama, 2008; Topf et al., 2008; Kovacs et al., 2008; Lopéz-Blanco and Chacón, 2013; Wu et al., 2013) and continue to be the methods of choice for resolving molecular systems with atomic resolution. MDFF, in particular, has been a front-runner among methods that have facilitated the discovery of some of the most complicated structures in modern day structural biology (Hsin et al., 2009; Sener et al., 2009; Gumbart et al., 2011; Frauenfeld et al., 2011; Zhao et al., 2013; Wickles et al., 2014).

cMDFF and ReMDFF, the new variants of MDFF introduced above, offer now accurate fitting of atomic-level structures within sub-5 Å EM maps, a feat thus far inaccessible to direct MDFF. These new methods extend the radius of convergence of MDFF to at least 25 Å, fitting models to maps of resolutions as high as 3.2 Å. This radius of convergence is at least twice that reported for Rosetta refinements of the 20S proteasome (DiMaio et al., 2015). Such a broad radius of convergence will allow the refinement of extremely poorly guessed initial models with MDFF, as demonstrated in the cases of β-galactosidase and TRPV1 reported here.

ReMDFF simulations involving the so-called replica-exchange molecular dynamics converge quickly using a small number of replicas and are thus amenable to cloud computing applications. Running ReMDFF on the cloud lowers greatly the barrier to usage of the method, providing a cost-effective and practical solution to fitting structures to high-resolution cryo-EM densities for researchers who neither own nor can administer their own advanced computer hardware.

The accuracy of structures refined by cMDFF and ReMDFF has been confirmed by standard error analysis protocols, both in terms of quality of fit as well as in terms of the quality of the model. The results clearly show that sidechain refinements through MDFF produce accurate placement of Cα and Cβ atoms and modeling of the associated dihedrals.

Beyond the standard error analysis protocols, which apply to single static structures, the quality of both the fit and the model can be evaluated by ensemble-based measures. An example demonstrated in this study pertains to the use of RMSF during MDFF refinement for simultaneously evaluating the quality of model, map, and fit. Furthermore, utilizing the fact that the inherent flexibility of a macromolecule is a key determinant of the achievable resolution of the corresponding map, RMSF values have been employed to identify the optimal amount of sharpening for a given map offering the highest contrast, as established typically through Guinier analysis. The RMSF computations in MDFF provide a viable means of determining per-residue B-factors.

Altogether, interpretation of a map as being representative of an ensemble rather than a single model brings to light new ways of model validation. EM maps, including those at high-resolution, typically do not have a uniform local resolution (Kucukelbir et al., 2014) and contain low-resolution regions, such as flexible exterior or transmembrane segments (Leschziner and Nogales, 2007). The sub-5 Å EM maps have also been able to resolve proteins in multiple conformations (Matthies et al., 2016). Both these type of maps will continue to benefit from accurate ensemble-based flexible fitting techniques for the foreseeable future. MDFF provides a natural method to model flexible regions; de novo models constructed for one conformational state can be flexibley fitted into the density of the other state(s), thus avoiding the arduous task of model construction for all the conformational states for capturing a conformational transition process with cryo-EM.

## Materials and methods

In the following section, we first outline the methodology underlying direct MDFF, cMDFF, and ReMDFF, along with specific protocols applied for the refinement of β-galactosidase and TRPV1 models. Second, we describe the computations of local and global root mean square fluctuation (RMSF) values, that are utilized for the evaluation of map-model quality. Finally, details on the computational implementation of all the three MDFF protocols are provided.

### Direct MDFF

MDFF requires, as input data, an initial structure and a cryo-EM density map. A potential map is generated from the density and subsequently used to bias a MD simulation of the initial structure. The structure is subject to the EM-derived potential while simultaneously undergoing structural dynamics as described by the MD force field.

Let the Coulomb potential associated with the EM map be $Φ⁢(𝐫)$. Then the MDFF potential map is given by

$$
V_{EM}(r)={ζ(\frac{Φ(r)−Φ_{thr}}{Φ_{max}−Φ_{thr}})ifΦ(r)\geqΦ_{thr},ζifΦ(r)<Φ_{thr}.
$$

where $ζ$ is a scaling factor that controls the strength of the coupling of atoms to the MDFF potential, $Φ_{thr}$ is a threshold for disregarding noise, and $Φ_{max}=max(Φ(r))$. The potential energy contribution from the MDFF forces is then

$$
U_{EM}=\sumiw_{i}V_{EM}(r_{i}),
$$

where $i$ labels the atoms in the structure and $w_{i}$ is an atom-dependent weight, usually the atomic mass.

During the simulation, the total potential acting on the system is given by

$$
U_{total}=U_{MD}+U_{EM}+U_{SS}
$$

where $U_{MD}$ is the MD potential energy as provided by MD force fields (e.g. CHARMM) and $U_{SS}$ is a secondary structure restraint potential that prevents warping of the secondary structure by the potentially strong forces due to $U_{EM}$. A detailed description of the potentials arising in Equation 3 is given in Trabuco et al (Trabuco et al., 2008, 2009).

After the MDFF and restraint potentials are created through the MDFF plugin of VMD (Humphrey et al., 1996), the initial structure is rigid-body docked (e.g. with Situs [Wriggers, 2010]) into the density map. Prior to simulation, MDFF-specific parameters can be modified and include $ζ$ and the subset of atoms to be coupled to the MDFF potential. The latter typically consists of all non-hydrogen atoms or backbone atoms and $ζ$ is usually set to 0.3. MDFF can be performed in various simulated conditions, including different temperatures and vacuum, membrane, and explicit or implicit (Tanner et al., 2011) solvent environments. The choice of parameters and conditions depends on the requirements of each specific case. For example, a highly polar molecule would be more accurately simulated in explicit solvent rather than in vacuum, but the computational cost would be much higher in this case. The MDFF simulation is run until the system has reached stationarity, as determined by RMSD; typical run times are nanoseconds.

### Cascade MDFF

In cascade MDFF (cMDFF), the initial structure is sequentially fitted to a series of potential maps of successively higher resolution, with the final potential map being the original one derived from the EM map. Starting with $i=1$, the $i$th map in the series is obtained by applying a Gaussian blur of width $\sigma_{i}\geq0⁢Å$ to the original potential map, such that $\sigma_{i}$ decreases as the structure is fitted in the sequence $i=1,2,…,L$, where $L$ is the total number of maps in the series, so that $\sigma_{L}\geq0 \AA$. One can intuitively understand cMDFF as fitting the simulated structure to an initially large and ergodic conformational space that is shrinking over the course of the simulation towards the highly corrugated space described by the original MDFF potential map.

Figure 1 provides a visual representation of cMDFF. For a mathematical illustration, suppose that the original potential map can be written as a sum of Gaussians

$$
V_{EM}(r)=\sumnc_{n}G(r;r_{n}^{′},s_{n}),
$$

where $c_{n}$ is a weight, $G⁢(𝐫;𝐫_{n}^{′},s_{n})$ is a Gaussian function centered at $𝐫_{n}^{′}$ with half-width $s_{n}$ and evaluated at $𝐫$. The result of a Gaussian blur of half-width $\sigma_{i}$ on $V_{EM}$ is (see Appendix 1 - Section 1 for details)

$$
V_{\sigma_{i}}⁢(𝐫)=\sumnc_{n}⁢G⁢(𝐫;𝐫_{n}^{′},\sqrt{s_{n}^{2}+\sigma^{2}}).
$$

Hence, the half-width $\sigma_{i}$ allows one to tune the characteristic width of the potential map through the half-widths of its component Gaussians $\sqrt{s_{n}^{2}+\sigma_{i}^{2}}$. The initial fitting starts with a large $\sigma_{1}$, corresponding to a diffuse potential which allows much structural mobility, and proceeds along decreasing values of $\sigma_{i}$, corresponding to narrower potentials with steeper gradients, so that the structure is gradually settled into the original potential map, characterized by $\sigma_{L}\geq0 \AA$.

In practice, the series of cMDFF maps is generated from the original potential map using VMD’s volutil Gaussian blur tool. Optimal values for the first half-width $\sigma_{1}$ and the change in $\sigma_{i}$ from one map to the next are case-dependent. Values used in the present study were obtained through trial and error. In general, structures far from the ideal conformation benefit from a large $\sigma_{1}$ ($>5$ Å) so as to explore a large conformation space. On the other hand, if the original map has a high resolution, small changes in $\sigma_{i}$ ($<1$ Å) would allow a gradual convergence required to avoid being trapped in local potential minima. In our simulations, the change in $\sigma_{i}$ is initially 1 Å. A concrete example is $\sigma_{1}=5$ Å, $\sigma_{2}=4$ Å, $\sigma_{3}=3$ Å, $\sigma_{4}=2$ Å, $\sigma_{5}=1$ Å, $\sigma_{6}=0$ Å. A second trial using changes of 0.5 Å was performed ($\sigma_{1}=5$ Å, $\sigma_{2}=4.5$ Å, $\sigma_{3}=4$ Å,$…$, $\sigma_{10}=0.5$ Å, $\sigma_{11}=0$ Å), and if the resulting structure of the second trial presented a better fit, then the first trial was discarded.

### Resolution exchange MDFF

Replica Exchange MD (ReMD) is an advanced sampling method that explores conformational phase space in search of conformational intermediates, which are separated by energy barriers too high to be overcome readily by fixed temperature simulations. Instead of working with a single, fixed MD simulation, ReMD carries out many simulations in parallel, but at different temperatures $T_{1} < T_{2} < T_{3} < …$ where the lowest temperature $T_{1}$ is the temperature of actual interest, typically, room temperature. The simulations of several copies of the system, the so-called replicas, run mainly independently, such that ReMD can be easily parallellized on a computer, but at regular time points the instantaneous conformations of replicas of neighboring temperatures are compared in terms of energy and transitions between replicas are permitted according to the so-called Metropolis criterion (Sugita and Okamoto, 1999). This way the highest temperature replicas overcome the energy barriers between conformational intermediates and through the Metropolis criterion moves the $T_{1}$ replica benefits from it such that transitions between intermediates occur frequently. The application of the Metropolis criterion in the protocol guarantees that the conformations of the $T_{1}$ replica are Boltzmann-distributed.

ReMDFF extends the concept of ReMD to MDFF by simply differentiating replicas not by temperatures $T_{1} < T_{2} < T_{3} < …$, but by the half-width parameters $\sigma_{1} > \sigma_{2} > \sigma_{3} > …$. Numerical experiments showed that ReMDFF works extremely well as documented in the present study. As NAMD can parallelize ReMD well (Jiang et al., 2014), it can do the same for ReMDFF, such that the enhanced sampling achieved translates into extremely fast MDFF convergence. At certain time instances replicas $i$ and $j$, of coordinates $𝐱_{i}$ and $𝐱_{j}$ and fitting maps of blur widths $\sigma_{i}$ and $\sigma_{j}$, are compared energetically and exchanged with Metropolis acceptance probability

$$
p(x_{i},\sigma_{i},x_{j},\sigma_{j})=min(1,exp⁡(\frac{−E(x_{i},\sigma_{j})−E(x_{j},\sigma_{i})+E(x_{i},\sigma_{i})+E(x_{j},\sigma_{j})}{k_{B}T})),
$$

where $k_{B}$ is the Boltzmann constant, $E⁢(𝐱,\sigma)$ is the instantaneous total energy of the configuration $𝐱$ within a fitting potential map of blur width $\sigma$.

### MDFF protocols for β-galactosidase and TRPV1

Computational protocols for performing direct MDFF, cMDFF, and ReMDFF refinements of the two test systems, β-galactosidase and TRPV1, are now outlined.

#### Direct MDFF

In order to provide a basis for comparison with cMDFF and ReMDFF, direct MDFF simulations were performed for both β-galactosidase and TRPV1. Original published maps of resolutions 3.2 Å and 3.4 Å for β-galactosidase (EMD-5995 [Bartesaghi et al., 2014]) and TRPV1 (EMD-5778 [Liao et al., 2013]), respectively, were fitted with search models characterized by RMSD values of 7 Å and 25 Å, respectively, relative to the known de novo target models (PDB entries 3J7H and 3J5P, respectively); these search models were prepared as described in Appendix 1 - Section 3. Scale factors $ζ$ (Equation 1) of values 1.0 and 0.3 were employed for β-galactosidase and TRPV1, respectively, to couple all the heavy atoms of the models to the respective maps. All other simulation parameters are noted in Appendix 1 - Section 2. The resulting structure from each MDFF simulation was then subjected to a final re-refinement applying a scaling factor of 1.0. Furthermore, the temperature was ramped down from 300 K to 0 K over 30 ps and held at 0 K for an additional 1 ns. This re-refinement step additionally improved the fitting of sidechains (McGreevy et al., 2014). Thus, all the MDFF results reported in the present study pertain to the structures that are obtained from direct MDFF, cMDFF, or ReMDFF simulations followed by the final re-refinement step.

#### cMDFF

The general simulation protocol consists of a series of consecutive MDFF simulations. The search models for β-galactosidase and TRPV1 were first minimized over between 500 to 1000 time steps. Next, MDFF simulation runs were sequentially performed, starting with the map of the lowest resolution, progressing through maps of successively higher resolution, and ending with the original map. Each run was chosen to be long enough for the structure to equilibrate within the MDFF potential. Taking advantage of the stochastic nature of MDFF simulations, multiple independent cMDFF simulations (10 in the present study) were performed for each system to be fitted, generating an ensemble of fitted structures. From the ensemble, the best structure was determined by the various quality indicators described in Results. This structure was then subjected to the final re-refinement step to allow for accurate resolution of sidechains.

For β-galactosidase, cMDFF was initiated with a map blurred with half-width $\sigma_{1}=5$ Å. Use of 0.5 Å resolution steps produced better-fitted structures than 1 Å steps. Hence, the final simulation utilized $L=11$ maps in total, including the original. A search model was obtained by subjecting the published structure to a 5-ns equilibration MD run with temperature 1000 K, yielding a structure with backbone RMSD of 7.6 Å relative to the original structure (see Appendix 1 - Section 3). 70-ps MDFF simulations were performed at each of the 11 resolutions to achieve convergence during the cMDFF protocol. Simulation parameters for all these MDFF runs are identical to those used for the direct MDFF simulations above.

For TRPV1, Gaussian blurred maps were generated starting with a half-width of $\sigma_{1}=5$ Å, and decreasing by 1 Å for each subsequent map, thus yielding a series of $L=6$ maps, including the original. The initial structure for this case was obtained using an interactive MD protocol, described in Appendix 1 - Section 2, to displace the ankyrin repeat region of one subunit. The resulting model deviated from the de novo model by an RMSD of about 10 Å in the displaced region and about 25 Å in the overall structure. Unlike β-galactosidase, now, 100-ps MDFF simulations were performed at each of the 6 resolutions to achieve convergence.

#### ReMDFF

ReMDFF was performed on both β-galactosidase and TRPV1 using the same search models, simulation parameters, and high-resolution maps as in the cMDFF simulations. 11 and 6 replicas were employed for β-galactosidase and TRPV1 respectively with an exchange trial interval of 1 ps. In each case, the total energy of each replica was monitored and the simulation was run until the energies reached a stationary level. The ReMDFF simulation was found to converge in 0.1 ns for the β-galactosidase refinement, and in 0.02 ns for that of TRPV1. Finally, similar to direct MDFF and cMDFF, the re-refinement step was performed to improve sidechain geometry.

### Fluctuation analysis

The local resolutions of a density map can be computed with ResMap (Kucukelbir et al., 2014) and used within VMD to select the atoms of a structure that are contained in a range of resolutions found by the ResMap analysis. First, the local resolution map output by ResMap is loaded into VMD and then the interpvol keyword can be used to automatically select the atoms found inside the volume values specified, using interpolation. The average RMSF of each selection can then be calculated for a structure during the steps of a MDFF simulation after the initial fitting has occured and the structure has stabilized. In principle any criteria for atom selection can be used for RMSF analysis, though we use local resolution of the EM density here to illustrate the correlation between the two measurements. Additionally, we compute a global average RMSF of the entire structure.

The ensemble-based nature of the RMSF analysis means that the quality metric is not dependent on a single structure, but instead a large family of structures can be employed as a better representative of the data. Ensemble-based analyses are a natural and powerful benefit of the MD-based nature of MDFF. RMSF analysis does not, however, require MDFF to be used as the method of refinement. In principle, any refinement method can be used to obtain the fitted model. A subsequent short MDFF simulation of the fitted model can then be performed to obtain the data necessary for the RMSF analysis.

### Implementation

Incorporating advanced simulation techniques, such as multi-copy algorithms (Jiang et al., 2014), into the MDFF protocol creates a more efficient and accurate computational strategy in cMDFF and ReMDFF. However, these advanced simulation techniques come with an added complexity in the setup and execution of the methods. The current implementation of these methods in NAMD (Phillips et al., 2005) and VMD (Humphrey et al., 1996) aim to automate the steps previously discussed. The MDFF Graphical User Interface (GUI) (McGreevy et al., 2016) can be used to set up cMDFF and ReMDFF simulations and provides default parameters, including the number and extent of smoothed maps used for the fitting, with which to run. The parameters for the smoothed maps and number of steps used per map are set heuristically based on previous experience and represent an adequate initial starting point. The GUI automatically generates each of the smoothed maps and converts them to potentials for use in the ReMDFF simulation. All parameters can be tuned by a user to adapt the protocols to their specific system and preference. The GUI produces a series of NAMD configuration files and scripts used for running the simulation, as well sorting and visualizing the results in VMD. Instruction on the use of MDFF, including the GUI, is given in the tutorial found at http://www.ks.uiuc.edu/Training/Tutorials/science/mdff/tutorial_mdff-html/.

Future development will allow for the automatic generation of the smoothed maps in NAMD at runtime. NAMD will also analyse the dynamics of the system to determine when the simulation has converged and move on to fitting to the next density map in the sequence in case of cMDFF calculations. Furthermore, advanced visualization and analysis techniques in VMD (e.g. new graphical representations) will be critical for properly understanding the RMSF analyses and to provide greater insight when examining the quality of a model.

The use of advanced simulation techniques also comes with an added cost of computational requirements. Adapting the algorithms to best utilize available computational hardware is key when developing efficient methods. Fortunately, the cMDFF and ReMDFF methods and associated analysis algorithms are well suited to highly efficient software implementations on contemporary multi-core CPUs and graphics processing unit (GPU) accelerators. We observe that by storing the complete cascade resolution series in efficient multi-resolution data structures such as mip maps (Williams, 1983), the MDFF cascade algorithm can access a continuously variable resolution representation of the original cryo-EM density map, while making efficient use of CPU and GPU processors and memory systems (Stone et al., 2007).

The parallel nature of ReMDFF presents an opportunity for efficient, automated sampling of maps of varying resolution. However, to achieve the best efficiency, the simulations should be performed on multi-core CPUs with relatively high core counts (i.e. at least 1 core per replica). Access to such multi-core computers could prohibit use of ReMDFF, however access to machines with the necessary hardware is easily achieved through cloud computing. The cloud computing model provides researchers with access to powerful computational equipment that would otherwise be too costly to procure, maintain, and administer on their own. A particular obstacle is that structural modeling often involves the use of different software suites, such as VMD (Humphrey et al., 1996) for simulation preparation and Situs (Wriggers, 2010) for initial rigid-body docking or VMD, NAMD (Phillips et al., 2005), and Rosetta (Leaver-Fay et al., 2011) for iterative refinement of models (Lindert and McCammon, 2015). Cloud platforms can easily bundle different software packages used in a modeling workflow to guarantee their availablity and interoperability on a standardized system. Through the cloud version of our MDFF program suite a user does not need to be aware of any of the above mentioned technical issues.

To prove the feasibility of performing ReMDFF simulations on a cloud platform, we ran ReMDFF for the test system, carbon monoxide dehydrogenase (PDB 1OAO:chain C), on the Amazon Web Services (AWS) Elastic Compute Cloud (EC2) platform. For the purposes of testing ReMDFF on EC2, we ran benchmarks on a variety of compute-optimized EC2 instance types. The details of the instance types can be found in Table 3. We used the same 6 smoothed density maps as the previously discussed cMDFF and ReMDFF simulations in the Proof of Principle and, therefore, also 6 replicas. The files and information necessary to run ReMDFF on the test system using EC2 cloud computing resources are available at (http://www.ks.uiuc.edu/Research/cloud/).
