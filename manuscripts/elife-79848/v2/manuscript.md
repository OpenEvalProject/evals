# Fast, high-throughput production of improved rabies viral vectors for specific, efficient and versatile transsynaptic retrograde labeling

## Authors

- Anton Sumser<sup>1</sup> ([ORCID: 0000-0002-4792-1881](https://orcid.org/0000-0002-4792-1881))
- Maximilian Joesch<sup>1</sup> ([ORCID: 0000-0002-3937-1330](https://orcid.org/0000-0002-3937-1330))
- Peter Jonas<sup>1</sup> ([ORCID: 0000-0001-5001-4804](https://orcid.org/0000-0001-5001-4804))
- Yoav Ben-Simon<sup>1</sup> ([ORCID: 0000-0002-7075-097X](https://orcid.org/0000-0002-7075-097X)) †

### Affiliations

1. Institute of Science and Technology Austria (ISTA) Klosterneuburg Austria ([ROR:03gnh5541](https://ror.org/03gnh5541))
2. Department of Neurophysiology and Neuropharmacology, Vienna Medical University Vienna Austria ([ROR:05n3x4p02](https://ror.org/05n3x4p02))
3. Allen Institute for Brain Science Seattle, WA United States ([ROR:00dcv1019](https://ror.org/00dcv1019))

† Corresponding author

## Abstract

To understand the function of neuronal circuits, it is crucial to disentangle the connectivity patterns within the network. However, most tools currently used to explore connectivity have low throughput, low selectivity, or limited accessibility. Here, we report the development of an improved packaging system for the production of the highly neurotropic RVdGenvA-CVS-N2c rabies viral vectors, yielding titers orders of magnitude higher with no background contamination, at a fraction of the production time, while preserving the efficiency of transsynaptic labeling. Along with the production pipeline, we developed suites of ‘starter’ AAV and bicistronic RVdG-CVS-N2c vectors, enabling retrograde labeling from a wide range of neuronal populations, tailored for diverse experimental requirements. We demonstrate the power and flexibility of the new system by uncovering hidden local and distal inhibitory connections in the mouse hippocampal formation and by imaging the functional properties of a cortical microcircuit across weeks. Our novel production pipeline provides a convenient approach to generate new rabies vectors, while our toolkit flexibly and efficiently expands the current capacity to label, manipulate and image the neuronal activity of interconnected neuronal circuits in vitro and in vivo.

## Introduction

Addressing the complexity and underlying structure of neuronal networks remains one of the biggest challenges in modern neuroscience, as this knowledge is essential for the understanding of circuit functionality in health and disease (Fornito et al., 2013; Morgan and Lichtman, 2013). Short- and long-range connectivity between populations of neurons in the central and peripheral nervous systems can be mapped with numerous existing techniques, with varying degrees of simplicity, efficiency and reliability (Luo et al., 2008; Luo et al., 2018). While recent advances in viral technology, such as anterograde and retrograde AAVs, now enable genetic targeting of populations based on their projection pattern (Tervo et al., 2016; Zingg et al., 2017), they can only be used for analysis of macrocircuits, due to their lack of specificity. In contrast, monosynaptic tracing technologies, based on engineered rabies virus, enable cell-type specific labeling of presynaptic partners, making it one of the most powerful toolkits to genetically dissect neuronal populations. This process is achieved in two steps: in the first, the avian TVA receptor and the rabies glycoprotein (G) are co-expressed in a predesignated population of cells, usually via administration of an AAV vector (Figure 1A) and in the second step, G-deleted rabies viral vectors, pseudotyped with the Avian Sarcoma and Leukosis Virus’s envelope glycoprotein A (envA) are introduced to the region containing TVA- and G-expressing neurons (Figure 1B), resulting in propagation of rabies particles exclusively from these starter cells to their presynaptic partners, but not to disynaptically connected neurons, and rarely to post-synaptic targets (Zampieri et al., 2014), regardless of their physical proximity (Ginger et al., 2013; Wickersham et al., 2007a; Figure 1C).

![Figure 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig1-v2.jpg)

**Figure 1.:** (A–C) A schematic representation of the experimental workflow for achieving cell type-specific trans-synaptic retrograde labeling using G-deleted, envA-pseudotyped rabies viral vectors: Genetic dissection of cre+ neurons (blue) for conditional expression of TVA and G (A); targeting of RVdGenvA particles to labeled neurons for expression of a gene of interest (GOI), (B) and subsequent propagation of native-coat RVdG particles from starter cells to their presynaptic partners (C). (D) A schematic representation of the three different cell lines designed for rescue (HEK-GT), pseudotyping and amplification (BHK-eT) and titration (HEK-TVA) of RVdG viral particles, alongside the transgenes used to generate them. (E) Schematic representation of the production process and timeline. L,P and N represent the plasmids encoding the corresponding rabies genes and V represents the vector plasmid. (F) Quantification of the time course for the rescue stage, starting at day 4 after transfection of viral plasmids. (G) Quantification of the time course for amplification of pseudotyped particles, starting at day 1 after transduction with native-coat particles. (H) Quantification of the average titer of concentrated pseudotyped stock from 19 individual productions, with comparison to the titer of a representative production of RVdg-CVS-N2c virus, produced using N2a cells (magenta). Lines represent titers of individual productions. Data in F and G represents the average and SEM of three individual and independent measurements.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A and B) HEK-GT (A) and BHK-eT (B) cells (bright-field illumination shown in cyan) were mixed with HEK293 or BHK-21 cells, respectively, stably expressing tdTomato only (red). Representative images show the gradual removal of tdTomato+ cells following exposure to either of the antibiotics Puromycin, blasticidin, or neomycin used in the generation of the stable cells. Scale bars represent 100 µm. (C) FACS-assisted quantification of the fraction of tdTomato+ cells shows the time course for their removal from the antibiotics-exposed cultures.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Illustration of the injection scheme designed to reveal the extent of leak expression following injection of envA-pseudotyped RVcG-CVS-N2c particles produced in BHK-eT cells. (B) Representative confocal image of a coronal section (left) shows extensive labeling of low-titer N2c-tdTomato vectors (magenta) from the hemisphere previously injected AAV-DIO-EF1a-TVA-2A-N2cG but only a small number of cells labeled with N2c-EGFP (green, left) which was injected into the contralateral hemisphere at a titer 500-fold higher. DAPI signal is labeled blue. (C) Protocol for the experiment in organotypic hippocampal slice cultures, designed to assess the contribution of tissue damage to non-specific labeling by envA-pseudotyped particles. (D and E) Images from three separate cultures transduced with envA-pseudotyped CVS-N2c-tdTomato vectors (red), either immediately (D) or 1 hr after the incision of the tissue (E). The substantially higher number of labeled cells in the cultures shown in (D) suggests that non-specific labeling from envA-pseudotyped particles can occur around injection sites when high-titer virus is applied.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Illustration of the injection scheme for hippocampus-specific retrograde labeling with native coat RVdGoGCVS-N2c-EGFP particles. (B) Representative coronal (left) and sagittal (right) images demonstrating specific and robust retrograde labeling of cortical and subcortical regions projecting to the hippocampus. LEC – Lateral entorhinal cortex; DBB – Diagonal band of Broca; Re – Nucleus reuniuns of thalamus; SuM – Supramammilary Nucleus; MnR – Median nucleus Raphe. 4′,6-diamidino-2-phenylindole (DAPI) signal is labeled blue.

While this approach ostensibly identifies presynaptic partners associated with a predesignated starter population, inefficiencies in the widely used SAD B19 strain, along with potential transmission biases across cell types (Albisetti et al., 2017) suggest the traced cells might represent only a fraction of the complete presynaptic population, rendering smaller, more distributed projections more difficult to identify. Furthermore, since large quantities of native-coat particles are routinely used to initiate the pseudotyping step of the viral production protocol (Osakada and Callaway, 2013), background contamination of native-coat particles in the pseudotyped stock is nearly unavoidable, which can result in false identification of projecting populations directly labeled by native-coat particles and not transsynaptically through the starter cells.

Recently, the deployment of the highly neurotropic CVS-N2c rabies strain for monosynaptic tracing was shown to identify 5–20 fold more presynaptic cells per starter cell than SAD B19, enabling a more comprehensive analysis of the diversity of presynaptic cells innervating a predesignated starter population. In addition, this strain was shown to be less neurotoxic, making it more suitable for experiments in behaving animals. However, the production process for these vectors is time-consuming and yields low viral titers (Reardon et al., 2016), presumably due to the use of neuronal cell lines for the various amplification and packaging steps. This limitation has so far restricted more widespread use of the superior CVS-N2c vector in circuit mapping experiments, particularly in its more useful pseudotyped form, whose preparation is even lengthier and the titers lower still.

Here, we report the development of a new packaging system, allowing expedited production of high-titer RVdGenvA-CVS-N2c particles, free of background contamination from native-coat particles, and show that these vectors retain their superior expansion efficacy when compared to SAD B19 vectors. We also report an extended toolkit of AAV and CVS-N2c vectors which can be applied to a wide range of experimental paradigms, and demonstrate their efficacy in uncovering hidden neuronal connections, even in heavily explored circuits.

## Results

### Improved packaging for RVdG viral vectors

Prolonged and cumbersome production has been a major limitation for G-deleted rabies virus vectors and most profoundly so for the CVS-N2c strain. Because CVS-N2c vectors exhibit enhanced neurotropism and retrograde labeling over SAD B19, improvements in the speed and quality of the various N2c production stages are necessary to realize the full potential of rabies viral vectors for mapping synaptic circuits. Here, we introduce a production protocol, based on two new packaging cell lines we have developed: (1) “HEK293-GT” cells, based on HEK293T cells stably expressing the chimeric SAD B19 codon optimized glycoprotein (oG) comprised of the extracellular domain of the Pasteur strain G and the transmembrane domain of the SAD B19G, along with the optimized T7 RNA polymerase (oT7pol), used for the initial rescue and amplification of native-coat particles, and (2) ‘BHK-eT’ cells, based on BHK21 cells stably expressing the envA glycoprotein, along with the TVA receptor, used for simultaneous vector pseudotyping and amplification (Figure 1D and E). The oG was selected for use in the rescue cell line because it can be used to efficiently rescue both the SAD B19 and the CVS-N2c strains and effectively transduce all cell types, whereas particles coated with the N2cG are highly specific to neuronal cell types and do not effectively transduce HEK293 or BHK-21 cells.

To improve the selection process for the transgene carrying cells, both cell lines make use of antibiotic resistance genes and strong constitutive promoters (Norrman et al., 2018). This ensures that cultures consist of purely transgene-expressing cells and that expression levels in those cells are high (Figure 1—figure supplement 1A-C). Furthermore, unlike previous packaging systems, the co-expression of TVA and envA in the BHK-eT cell line allows pseudotyped particles to propagate within the culture, similar to the native-coat ones (Figure 1F and G), enabling amplification and pseudotyping of vectors in a single short step. In addition, since a very small amount of native-coat, or even trace amounts of pseudotyped virus, are sufficient in order to initiate the pseudotyping process, contamination from native-coat particles in the final pseudotyped stock can be minimized, while the titer of the pseudotyped stock can be exceedingly high (Figure 1H). For each new viral batch produced (37 in total), we injected pseudotyped particles at work concentrations (1–5×108 TU ml-1) into naïve brains. We found only minimal non-specific labeling (a maximum of 1–2 labelled cells per 0.5–1 mm of tissue examined).

Even though the presence of native coat particles can be virtually eliminated from the preparation, it is still possible to see sparse non-specific labeling of pseudotyped particles in the absence of TVA, when extremely high vector titers (100–500-fold higher to our experimental requirements) are introduced into the brain (Figure 1—figure supplement 2A and B). To demonstrate that even this sparse labeling likely results from direct penetration of pseudotyped particles into damaged cells and cell processes along the needle tract, rather than from non-specific labeling with native coat particles, we transduced organotypic hippocampal cultures prepared from a WT mouse brain with envA-pseudotyped CVS-N2c-tdTomato, either immediately or one hour after lacerating the culture with a scalpel, to simulate physical damage to neuronal processes (Figure 1—figure supplement 2C). We observed that cultures transduced immediately after the insult exhibited substantially higher transduction rates than cultures transduced one hour later, after most damaged processes had time to recover (Figure 1—figure supplement 2D and E) confirming that physical damage (such as one that accompanies intracerebral injection with a Hamilton needle), can produce off-target labeling around the injection site, when high-titer virus is delivered. Furthermore, beyond their use as an intermediate to obtain envA-pseudotyped particles, we confirmed that oG coated CVS-N2c particles produced in HEK293-GT cells can be successfully used for non-specific retrograde labeling (Figure 1—figure supplement 3A and B). Together, these new cell lines enable significantly faster production times, higher titers and less background contamination than both other currently used methods for production of either CVS-N2c or SAD B19 (Tables 1 and 2).

**Table 1.**
 Rescue from DNA and amplification of native-coat stock.


<table>
  <thead>
    <tr>
      <th></th>
      <th>B7GG (Osakada and Callaway, 2013)</th>
      <th>Neuro2a-N2cG (Reardon et al., 2016)</th>
      <th>HEK-GT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Stably-expressed transgenes</td>
      <td>T7 polymerase +SAD-B19G</td>
      <td>CVS-N2cG</td>
      <td>Optimized T7 polymerase (oT7)+optimized SAD-B19G (oG)</td>
    </tr>
    <tr>
      <td>Selection markers</td>
      <td>Fluorescence</td>
      <td>Fluorescence</td>
      <td>Antibiotic resistance genes</td>
    </tr>
    <tr>
      <td>Transfected genes</td>
      <td>Vector +N,P, G &amp; L</td>
      <td>Vector +T7, N,P,G &amp; L</td>
      <td>Vector +N,P &amp; L</td>
    </tr>
    <tr>
      <td>Transfection efficiency</td>
      <td>Low</td>
      <td>Low</td>
      <td>High</td>
    </tr>
    <tr>
      <td>Growth conditions</td>
      <td>3% CO2 at 35 °C</td>
      <td>3% CO2 at 35 °C</td>
      <td>5% CO2 at 37 °C</td>
    </tr>
    <tr>
      <td>Rescue timeline</td>
      <td>10–11 days</td>
      <td>10–11 days</td>
      <td>5–6 days</td>
    </tr>
    <tr>
      <td>Initial amplification timeline</td>
      <td>9–11 days</td>
      <td>14–21 days</td>
      <td>Not required</td>
    </tr>
    <tr>
      <td>Compatibility</td>
      <td>SAD-B19 (CVS-N2c) possible, but not tested</td>
      <td>CVS-N2c only</td>
      <td>Both SAD-B19 and CVS-N2c</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Pseudotyping of rescued vectors.


<table>
  <thead>
    <tr>
      <th></th>
      <th>BHK-EnvA (Osakada and Callaway, 2013)</th>
      <th>Neuro2a-envA (Reardon et al., 2016)</th>
      <th>BHK-eT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Stably-expressed transgenes</td>
      <td>envA or envB</td>
      <td>envA</td>
      <td>envA +TVA</td>
    </tr>
    <tr>
      <td>Selection markers</td>
      <td>Fluorescence</td>
      <td>Fluorescence</td>
      <td>Antibiotic resistance genes</td>
    </tr>
    <tr>
      <td>Growth conditions</td>
      <td>3% CO2 at 35 °C</td>
      <td>3% CO2 at 35 °C</td>
      <td>5% CO2 at 37 °C</td>
    </tr>
    <tr>
      <td>Pseudotyping timeline</td>
      <td>7–10 days</td>
      <td>28 days</td>
      <td>4–6 days</td>
    </tr>
    <tr>
      <td>Requirements for pseudotyping</td>
      <td>Large stock of native-coat particles</td>
      <td>Large stock of native-coat particles</td>
      <td>Trace amounts of either native-coat or evA pseudotyped stock</td>
    </tr>
    <tr>
      <td>Titer</td>
      <td>Low 10^8 typical</td>
      <td>Low 10^7 typical</td>
      <td>High 10^9 typical</td>
    </tr>
    <tr>
      <td>Native-coat background</td>
      <td>10^2 typical</td>
      <td>Not detectable</td>
      <td>Not detectable</td>
    </tr>
  </tbody>
</table>

### Selective targeting of starter populations

To test the efficacy and transduction exclusivity of these new vectors, we first delivered a minimal volume (20 nl) of AAV vectors expressing a cre-dependent TVA(FLAG3X)–2A-N2cG cassette into the dentate gyrus (DG) of a Prox1cre mouse (Borges-Merjane et al., 2020) followed by large volume (500 nl) of RVdGenvA-CVS-N2c-EGFP vectors into the same location. Subsequent immunolabeling revealed that only dentate granule cells (DGCs) immunoreactive for the FLAG3X tag were transduced by the rabies vectors, with efficient retrograde labeling from this small group to neurons in the entorhinal cortex (EC, Figure 2A; Borges-Merjane et al., 2020). In parallel, we performed a second set of experiments in which a TVA-2A-N2cG cassette was expressed in a small population of adult-born DGCs, using an Ascl1creERT2 line crossed with the Ai14 tdTomato cre-reporter line (Yang et al., 2015). Four weeks after AAV vectors were delivered to the DG, along with a single i.p. injection of tamoxifen (TMX) to induce recombination in the CreERT2 line, RVdGenvA-CVS-N2c-EGFP vectors were introduced to the same location. This manipulation resulted in both highly specific targeting of tdTomato+ adult-born DGCs in the inner granule cell layer, as well as robust retrograde labeling of afferents to these starter cells. This high efficacy manifested as widespread and specific labeling of layer-2 neurons of the medial and lateral entorhinal cortices (MEC and LEC, respectively), hilar mossy cells, CA3 pyramidal cells and a number of DG-projecting subcortical regions, including the medial septal (MS), the supramamilary (SuM), and the raphe (RN) nuclei (Figure 2B and Figure 2—figure supplement 1A and B), largely consistent with several previous reports (Deshpande et al., 2013; Vivar et al., 2012). Last, to ensure that the envA pseudotyped virus produced using our system lacks non-specific targeting properties and cannot propagate in the absence of its glycoprotein, we expressed a cre-dependent TVA-2A-tdTomato cassette, without the rabies glycoprotein, in DGCs, again using Prox1cre mice. Subsequent delivery of high-volume (0.5 µl), high-titer (~3 × 1010 TU ml–1) RVdGenvA-CVS-N2c-EGFP vectors resulted in exclusive expression of EGFP in dTomato-positive neurons in the DG (Figure 2C) but not in dTomato-negative regions, or in any of the regions projecting to the DG. These experiments provide evidence that the new packaging system we designed is capable of rapidly producing high-titer and high-quality RVdGenvA vectors for transsynaptic retrograde neuronal labeling.

![Figure 2.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig2-v2.jpg)

**Figure 2.:** (A) Illustration of the injection scheme (left) and corresponding representative confocal images demonstrating the targeting specificity of CVS-N2c particles (green) to FLAG3X tagged cells (magenta) along with retrograde labeling to EC layer 2 cells (rightmost image, EC layers are separated by dashed lines and their numbers are denoted above). (B) Illustration of the injection scheme (top left) and corresponding representative confocal images demonstrating efficiency and specificity of CVS-N2c-mediated retrograde labeling from adult-born DGCs. (C) Illustration of the injection scheme (top left) and corresponding representative confocal images demonstrating target specificity, with no accompanying retrograde labeling, in the absence of the rabies glycoprotein in any of its projections in four separate experiments.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A and B) Transsynaptic retrograde labeling with CV-N2c vectors from adult-born cells in the hippocampal DG, using the Ascl1creERT2 line (A) reveals identical labeling pattern in subcortical regions as following the same manipulation on the general population of DGCs, using the DG-specific Prox1cre line (B) MS – Medial Septal Nucleus; SuM – Supramammilary Nucleus; MnR – Median nucleus Raphe.

### Comparative retrograde labeling efficiency of RVdG strains

RVdG-CVS-N2c vectors were originally produced in the neural progenitor cell line N2A, under the premise that this would improve neurotropism of the assembled viruses, enhancing their trans-synaptic transfer rates and reducing their neurotoxicity (Reardon et al., 2016). The new packaging cell lines we developed were designed to increase production speed and efficiency, but the possibility remains that the non-neuronal origin of the BHK-21 cells might compromise the superior properties of CVS-N2c vectors. To evaluate any differences in retrograde labeling efficiency between the vectors assembled using the two approaches, we expressed a TVA-2A-N2cG cassette in CA1 pyramidal neurons and subsequently transduced them with a cocktail of two different RVdGenvA-CVS-N2c vectors expressing either EGFP or dTomato, in equal titers, amplified and pseudotyped using either N2A-based or the new HEK-GT/BHK-eT based packaging systems (Figure 3A). This strategy resulted in highly efficient and specific retrograde labeling of CA1 afferents in the CA3, LEC and medial septum (MS) in equal proportions for both vectors (Figure 3B, C and H).

![Figure 3.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig3-v2.jpg)

**Figure 3.:** (A) Schematic illustration of the injection scheme, designed for comparison of retrograde labeling efficacy between CVS-N2c vectors produced using either the N2a-based or BHK-based packaging cell lines, propagating using the N2c glycoprotein. (B) Representative confocal images of the ipsi- and contra-lateral hippocampus. Expanded images of the CA3 region of both hemispheres and the CA1 of the injection site correspond to the areas delineated by cyan rectangles. (C) Representative confocal images of the LEC (top) and the septal complex (bottom). (D–F) Same as (A–C) but for comparison of CVS-N2c and SAD B19 vectors, both produced with BHK-based packaging cell line and propagating using the SAD-B19 optimized glycoprotein (oG). (G) Summary bar plot showing the ratio of first order starter cells in the CA1 pyramidal layer, between neurons labeled with either CVS-N2cN2a (blue) or SAD B19BHK-et (orange) and the neurons labeled with CVS-N2cBHK-et. (H) Summary bar plot showing the differences in retrograde labeling efficiency, under both injections schemes described in (A) and (D). All values were normalized to the ratio of starter cells shown in (G). N=4 and 3 animals for the N2c-N2c and N2c-B19 comparisons, respectively. Data shown as mean and SEM with black circles denoting individual animals.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Average neuron count per slice for individual animals (empty circles) and averaged count for all animals (full circles) in the different regions projecting to the CA1 following retrograde labeling with CVS-N2c vectors using either the B19-oG (orange) or the N2cG (cyan). (B) Ratio of 2nd order neurons between the two conditions in (A), normalized by the number of putative starter neurons in the CA1 pyramidal layer, demonstrates higher efficacy of propagation under the N2cG, for all regions tested. (C) Retrograde labeling efficacy ratio between CVS-N2c and SAD-B19 vectors shown in Figure 3H, corrected for the added effect of the glycoprotein to the propagation efficacy of the CVS-N2c vectors by dividing the values for the SAD-B19 condition in Figure 2H, with the corresponding ratio estimates measured in (B).

To confirm that these CVS-N2c vectors remain more efficient than the widely used SAD B19 strain, as was previously shown for vectors produced in N2A cells (Reardon et al., 2016; Rowland et al., 2013), the previous experimental design was repeated, using the optimized B19 glycoprotein (oG; Kim et al., 2016) and RVdGenvA-SAD B19 vectors (Figure 3D). Here, a strikingly different result was observed, with afferents labeled with CVS-N2c visibly outnumbering those labeled with SAD B19 in most regions tested (Figure 3E, F and H). Quantification of cell numbers in these experiments showed that while the ratio of 1st order CA1 neurons between the two compared vectors remained low in both experiments (Figure 3G), the ratios of 2nd order neurons in the tested sets of regions differed substantially, with only minor differences observed when the two CVS-N2c vectors were compared, but differences close to an order of magnitude observed when CVS-N2c and SAD B19 vectors were compared (Ipsilateral CA3: 14.43 ± 1.67%; Contralateral CA3: 11.95 ± 2.85%; LEC: 8.17 ± 0.85%; MS: 100.88 ± 4.54%; Figure 3H). A notable exception is seen in the projection from the MS, in which ratios between the SAD B19 and N2c remained identical. This effect could be the result of differences in structure of the synaptic contacts between MS and CA1 neurons or in the projection’s connectivity scheme. Since we observed that CVS-N2c vectors propagate less efficiently when using the oG, as opposed to their endogenous N2cG (Figure 3—figure supplement 1A-C), the actual differences in retrograde labeling between CVS-N2c and SAD B19 are likely to be substantially higher, matching those previously reported (Reardon et al., 2016).

### Identification of intra-hippocampal projections to DGCs

To further test and validate the throughput and sensitivity of this tool, we performed additional retrograde labeling experiments from the DG, in order to see whether we will be able to corroborate and expand on previous reports, describing non-canonical inhibitory projections it receives from inhibitory neurons in the Stratum Oriens (S.O.) and Stratum Lacunosum Moleculare (S.LM.) of the CA1 (Hájos and Mody, 1997; Katona et al., 2017; Klausberger and Somogyi, 2008; Szabo et al., 2017). Those findings are all based on reconstruction of the axonal plexus of biocytin-labeled neurons and, while informative, this approach has low-throughput and mostly lacking information about the identity of the postsynaptic partner. To test if we could locate and identify these cells, we targeted RVdGenvA-CVS-N2c-tdTomato vectors to DGCs of Prox1cre mice crossed with GAD1-EGFP transgenic mice, in which GABAergic neurons are fluorescently labeled (Tamamaki et al., 2003), and examined the regions outside of the DG for colocalization (Figure 4A). Consistent with these reports, we found extensive labeling of neurons with N2c-tdTomato, whose somata were located in the S.O. and S.LM., but not in the Stratum Pyramidal (S.P.) or Radiatum (S.R.) layers. In addition, we uncovered a third population of DG-projecting neurons in the superficial most layer of the subiculum (Figure 4B). Analysis of colocalization has revealed that while half of all retrogradely labeled neurons found in the S.O and S.LM. were also positive for EGFP, in the subicular population, which accounted for more than a third of all intrahippocampal projecting cells, colocalization was almost completely absent (Figure 4C), suggesting that this population consists of excitatory neurons. AAV vectors expressing EGFP under control of either the inhibitory neuron-specific mDLX or the excitatory neuron-specific CaMKIIa promoters, injected into the superficial CA1 or superficial subiculum, respectively, confirmed the existence of axonal branching in the DG (Figure 4—figure supplement 1A and B). Retrograde labeling from adult-born DGCs or ventrally located DGCs revealed similar presynaptic populations (Figure 4—figure supplement 1C and D), providing further support for the abundance of these connections.

![Figure 4.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig4-v2.jpg)

**Figure 4.:** (A) Schematic illustration and representative confocal images, describing the injection scheme designed to target DGCs for retrograde labeling in an interneuron reporter line. (B) Representative confocal images (left) of the regions highlighted in (A) showing retrogradely-labeled neurons along specific hippocampal layers and their overlay with the interneuron-specific marker. (C) Summary bar plot showing the distribution of DG-projecting hippocampal neurons outside of the DG (magenta) and of them, the fraction of double-labeled neurons (grey). Calculation of cell numbers in the dendritic cell layers combined cells along the entire proximo-distal hippocampal axis, from CA3 to CA1. N=189 cells from 3 animals. (D) Representative parasagittal sections of the hippocampus following retrograde labeling from the DG with CVS-N2c-tdTomato, along with immunolabeling of parvalbumin (Pvalb, top) and Somatostatin (Sst, bottom). Expanded view of the S.O. and S.LM. are shown to the right of each image. (E) Summary plot describing the proportion of Pvalb- or Sst-positive neurons of the total CVS-N2c labeled neurons in the S.O. or S.LM. of the CA1. N=125 cells from three animals.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A and B) Both injection of AAV-mDLX-EGFP, for specific expression in inhibitory neurons, into the CA1 (A), as well as injection of AAV-CaMKII-EGFP, for specific expression in excitatory neurons, into the subiculum (B) reveal axonal arborizations in the molecular layer of the DG. (C) Retrograde labeling from a sparse population of adult-born DGCs (as shown in Figure 2B) also reveals projections from the subiculum (top) and S.O. (bottom). (D) Retrograde labeling from the ventral DG (vDG) using the Prox1cre line (left panel) shows projection neurons along the superficial most layer of the ventral subiculum (middle and right panels).

Taking advantage of the high-throughput nature of our labeling approach, we immunostained sections from labeled animals for two of the most prominent interneuron markers, Parvalbumin (Pvalb) and Somatostatin (Sst), and found that while 43 ± 5% of S.O. retrogradely-labeled neurons were positive for Sst, none of the labeled cells in both S.O. and S.LM colocalized with Pvalb (Figure 4D and E). This is consistent with the known projection of S.O. Sst neurons to the S.LM., which borders on the dentate gyrus, while axons of Pvalb neurons in the CA1 project mainly to the pyramidal cell layer and have few, if any axonal arborization in the S.LM. (Freund and Buzsáki, 1996) and are therefore much less likely to branch into the DG.

### Differential targeting of neuronal populations for retrograde labeling

The abundance of population-specific cre/flp driver mouse lines allows for a wide range of possible labeling experiments. However, often such lines are either unavailable, or insufficiently specific for the experimental requirements. To allow for a broader use of this tool, we have developed additional AAV vectors driving expression of the TVA-2A-N2cG cassette which can achieve greater specificity.

First, we wanted to be able to compare between two genetically distinct, yet spatially overlapping populations. To this aim, we designed AAV vectors which contain a cre-off mechanism, using a single-floxed, excisable open reading frame (SEO) to drive transgene expression under control of the excitatory neuronal CaMKIIa promoter (Figure 5—figure supplement 1A). We tested this tool on CA1 pyramidal neurons of Calb1cre mice, in which Cre recombinase is expressed exclusively in deep, but not in superficial CA1 neurons (Li et al., 2017; Valero et al., 2015; Figure 5A). Parallel retrograde labeling from these two subpopulations of CA1 neurons revealed that while both receive relatively equal input from CA3 neurons, deep CA1 neurons receive substantially greater input from LEC-3 neurons (Figure 5B), confirming previous findings obtained using lower-throughput approaches (Li et al., 2017; Masurkar et al., 2017).

![Figure 5.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig5-v2.jpg)

**Figure 5.:** (A) Graphical representation (top left) and representative confocal images, demonstrating differential targeting of superficial and deep CA1 pyramidal neurons using a combination of cre-on and cre-off AAV vectors. (B) Graphical representation (top center) for dual retrograde labeling from superficial (bottom left, green) and deep (bottom right, magenta) CA1 pyramidal neurons and the resulting distribution pattern of their corresponding projection neurons in the EC (top left and top right). (C) Graphical representation of the viral injection scheme for mapping inputs into hippocampal inhibitory neurons (top left), and representative parasagittal images of labeled cells in the HC (bottom left) and LEC (right). Expanded images show a double-labeled neuron in EC-6. (D) Distribution of all retrogradely labeled cells (top) and of double-labeled cells only (bottom) among the superficial layers 2 and 3 and the deep layers 5 and 6 of the LEC. N=8 sections/3 animals. (E) Same as (C), but for Dlx5/6FlpE × Ai65 mice. (F) Same as (D) for the experiments described in (E). N=8 sections/3 animals. (G), A representative parasagittal image of deep brain structures following the injection scheme described in (E). SuM – Supramammilary Nucleus; MnR – Median nucleus Raphe.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) A schematic illustration demonstrating the differential effect of cre-mediated recombination on double-floxed, inverted open reading frames (DIO, left) or single-floxed, excisable open reading frames (SEO, right). (B) Representative confocal images from the hippocampus of a GAD1-EGFP mouse (cyan), injected with AAV-mDLX-TVA-2A-N2cG (orange) and subsequently CVS-N2c-tdTomato (magenta) into the hippocampal CA1. Green arrows in the expanded images indicate starter neurons expressing all three markers, grey arrows indicate 2nd order interneurons, expressing EGFP and tdTomato, but not TVAFLAG-2A-N2cG, and white arrows indicate potential, yet non-participating interneurons expressing GAD1 and TVAFLAG-2A-N2cG, but not tdTomato.

Next, we wanted to test whether our vectors could also label projections to inhibitory neurons. To attain interneuron-specific retrograde labeling, we first used AAV vectors to express the TVA-2A-N2cG cassette under control of the interneuron-specific mDLX promoter (Dimidschstein et al., 2013) in the CA1 of GAD1-EGFP mice. A subsequent injection of CVS-N2c-tdTomato revealed widespread labeling of 2nd order neurons both within the hippocampal CA1 and CA3 fields, as well as in the EC (Figure 5C and Figure 5—figure supplement 1B). An additional analysis of co-labeling in the EC revealed a small population of long-range inhibitory projection neurons, located preferentially in the deeper layers 5 a and 6 (Figure 5D), whose existence has previously been reported (Basu et al., 2016; Melzer et al., 2012) but their location within the EC has so far remained unknown. In order to cross-validate and expand on these findings, we crossed Dlx5/6flpE mice with the double cre +flp, tdTomato reporter line Ai65 (Madisen et al., 2015). Hereby, using injections of AAV vectors with flp-dependent TVA-2A-N2cG expression cassette, followed by RVdGenvA-CVS-N2c-EGFP-iCre, we were able to highlight and isolate the inhibitory projections to hippocampal inhibitory neurons, as the double cre +flp recombination required for tdTomato expression can only take place in inhibitory neurons transduced by the rabies virus (Figure 5E). In line with our previous findings, we show that while the majority of excitatory cortical input to hippocampal inhibitory neurons originated in the superficial layers 2 and 3, long-range inhibitory projection neurons are almost exclusively found in the deeper layers 5 a and 6 (Figure 5F). Further examination of labeling patterns of 2nd order neurons in deep-brain regions showed that in the MS and the diagonal band of Broca (DBB), a large fraction of cells are double-labeled, confirming that our labeling strategy for isolation of long-range inhibitory projections is exhaustive (Figure 5G). This strongly suggests that while the deeper cortical layers give rise to both inhibitory and excitatory hippocampal projections, the excitatory projection originated from a substantially larger population. This is particularly unexpected, as to-date, only sporadic evidence existed for the presence of cortico-hippocampal projections, excitatory or inhibitory, arising from the deeper layers of the EC (Gloveli et al., 2001).

### Bicistronic CVS-N2c vectors for efficient dual labeling

A previous report has shown that the B19 N-P linker sequence, which allows the virus to effectively separate these proteins, can also be used for separation of exogenous genes (Osakada et al., 2018). While this approach could promote an expansion of the rabies toolkit to accommodate more complex experimental designs, it remains to be shown to whether efficient separation indeed takes place and whether, unlike the use of 2 A peptides or the IRES sequence, expression levels of the individual proteins remain unaltered. To test the feasibility and efficacy of this approach, we designed new CVS-N2c bicistronic plasmids, to drive co-expression of a nuclear-localized EGFP (nl.EGFP) with either tdTomato (Figure 6A) or a synaptophysin-tethered EGFP for specific labeling of presynaptic terminals (SypEGFP, Figure 6B) separated by the CVS-N2c N-P liker sequence. Specific delivery of these vectors to hippocampal DGCs using targeted AAV expression of the cre-dependent TVA-2A-N2cG cassette in Prox1cre mice, revealed that in both cases, the individual proteins were efficiently expressed in a compartment-specific manner (Figure 6A and B and Figure 6—figure supplement 1A-D).

![Figure 6.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig6-v2.jpg)

**Figure 6.:** (A) Schematic illustration of the vector sequence, designed to drive independent bicistronic expression of a nuclear-localized EGFP (nl.EGFP) alongside tdTomato, using the N-P linker sequence (top). Representative confocal images of the HC (bottom right) and EC (bottom left) following retrograde labeling from the DG, demonstrate the differential localization, indicating effective separation of the fluorophores. (B) Schematic diagram of a bicistronic nl.EGFP +SypGFP CVS-N2c vector (top) used for retrograde labeling from the DG (right panels) and representative confocal images demonstrating dual nuclear and synaptic localization of EGFP in the dentate granular and molecular layer (top right image) and purely synaptic localization at the mossy fibers terminals (bottom right image). (C) Schematic diagram of a bicistronic tdTomato +oChIEF CVS-N2c vector (top) used for retrograde labeling from the DG, and a representative image of a biocytin-filled neuron (white) in MEC-2 (bottom left) along with representative traces from 10 overlaid recordings at different frequencies (bottom right). (D) Summary plots of the action potential success rate for recordings made 6–7 days after introduction of RVdG (left) and their resting membrane potential at the time of recording (right) demonstrate the light responsiveness and physiological condition of the labeled neurons. (E) Representative confocal images (top) of DGCs (left), DG molecular layer interneurons (center) and CA3 pyramidal neurons (right) and their synaptic responses to optogenetic activation of the perforant path (bottom) following retrograde labeling from the dorsal DG with the bicistronic CVS-N2c-tdTomato-oChIEF vector.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A and B) FACS analysis of fluorescence intensity in HEK-TVA cells transduced with RVdGenvA-CVS-N2c-nl.EGFP-tdTomato (A) or HEK293 cells transduced with 10 X concentration of the same vector (B). Five different clusters of labeled cells are highlighted in (A), likely representing: (1) tdTomato-/nl.EGFP- Non-transduced cells; (2) tdTomato-/nl.EGFP+ Cells with a putative null mutation in the tdTomato gene; (3) tdTomatolow/nl.EGFP- putatively undergoing mitosis and lacking a defined nucleus; (4) tdTomato+/nl.EGFP- with a putative null mutation in the EGFP gene; (5) tdTomato+/nl.EGFP+ with no putative mutations. (C) Quantification of fluorescence intensity for three different RVdG-CVS-N2c vectors, in which tdTomato is expressed alone, or in a bicistronic vector in either the first (tdTomato-FlpO) or second (nl.EGFP-tdTomato) position shows no substantial differences in tdTomato fluorescence intensity. (D) A representative, high-magnification confocal image of the granule cell layer of the DG, following targeting of the RVdGenvA-CVS-N2c-nl.EGFP-tdTomato vector, showing a cell expressing a soluble EGFP, which is likely the result of a mutation in the nuclear localization signal.

Next, we capitalized on this result to create new bicistronic vectors for dual expression of the optogenetic actuator ChIEF (Lin et al., 2009), along with a fluorescent protein, speculating that the increased expression levels and the untethering of the fluorophore will lead to greater responsivity of labeled neurons to optogenetic stimulation, as well as facilitate their identification. We again targeted DGCs for retrograde labeling using these new vectors and recorded the action potential success rate of labeled neurons in the EC, following five light pulses, each 1 ms long, at varying frequencies. As predicted, action potentials could be reliably generated at much higher stimulation frequencies and at a much earlier time point following stimulation onset than has previously been shown for both SAD B19 and CVS-N2c vectors (Osakada et al., 2018; Reardon et al., 2016: Figure 6C and D). In these recorded neurons, the resting membrane potential was −55 mV to −75 mV, corroborating the functional integrity of the cells. From a total of 21 cells, 3 cells had lower membrane potential above –55 mV (but below –50 mV) and these were excluded from the final analysis. By recording synaptic responses to optogenetic stimulation from several neuronal populations sharing the same input as DGCs, such as neighboring, non-transduced DGCs, CA3 pyramidal neurons and dentate gyrus molecular layer interneurons, we also show that this tool can be reliably used for exploring circuit motifs, and also potentially for effective circuit-based manipulation in behaving animals (Figure 6E). Since our observations indicate that under in vitro conditions, cellular health and viability begin to deteriorate in preparations made >10 days from RVdG-CVS-N2c injection, it is important to show that effective optogenetic activation can be achieved at an earlier time point, when the cells remain healthy and viable for the duration of the experiment.

### In vivo measurements from extended cortical networks

While RVdG viral vectors are highly effective in describing circuit architecture, their neurotoxicity limits their use for many applications, in which long-term monitoring or manipulation of labeled circuit is required (Luo et al., 2018) and while a new technology for production of non-neurotoxic RVdG vectors was recently been presented (Chatterjee et al., 2018), the current inability to produce these vectors in a pseudotyped form excludes their use for cell-type-specific tracing experiments. RVdG-CVS-N2c vectors have previously been shown to be less neurotoxic than the SAD B19 strain, and compatible for prolonged imaging of neuronal activity in vivo (Reardon et al., 2016). However, since neurotoxicity has not been completely eliminated, it is still possible that their endogenous activity patterns become impaired within this time period, thereby impinging on results.

To address this question, we dissected a microcircuit within the primary visual cortex (V1) for in vivo calcium imaging, by first injecting retrogradely transported Cre-expressing AAV vectors (Tervo et al., 2016) in the laterodorsal nucleus of the thalamus (LD) and AAV-DIO-CAG-tdTomato+AAV-DIO-EF1a-TVA-2A-N2cG into the V1. A subsequent injection of RVdGenvA-CVS-N2c-GCaMP8m into V1 resulted in specific retrograde labeling from layer 5 neurons in the V1 (Figure 7A and B and Figure 7—figure supplement 1A and B). In the following weeks, we observed the time course of GCaMP8m expression and recorded calcium transients of the labeled 1st and 2nd order neurons using two-photon imaging, in response to visual cues in three awake behaving mice. While we detected the first GCaMP8m labeled neurons already at day 3, substantial labeling at approximately half-maximal numbers in all animals started 7 days after RVdGenvA-CVS-N2c-GCaMP8m injection. Subsequently, the increase of neuronal numbers slowed and remained high until day 16 (on average 1100 neurons), when the experiments were terminated (Figure 7C). While the most superficial tdTomato-labeled starter neurons were detectable in vivo, their depth did not allow a robust estimate of their total numbers in our configuration.

![Figure 7.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig7-v2.jpg)

**Figure 7.:** (A) Illustration of the injection scheme for labeling projections onto the V1 region’s layer 5 neurons with GCaMP8m. (B) A representative confocal image of a coronal section following the injection scheme described in (A). (C) GCaMP8m-positive neuron numbers over recording days. (D) In vivo two-photon imaging in presynaptic neurons. Drifting gratings in 8 directions (top row). Trial responses (grey) and average (black) for example neurons on day 9 and day 16, stimulation starts at black triangle. Polar plot of the directional responses in right column. (E) Histogram of direction selectivity for tdTomato-negative (2nd order) neurons. (F) Same as in E for tdTomato-positive (starter) neurons. (G) Polar scatter plot of direction selectivity (radial) over preferred direction (angular) for all recorded neurons. (H) Mean DSI and proportion of significant direction selectivity over recording days.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/79848/elife-79848-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Representative confocal images of the V1 area in the coronal plane (animal 2, left) or of the sagittal plane (animal 3, right) of the two additional animals used in the experiment. (B) A representative fluorescent microscope image of the lateral geniculate nucleus showing retrogradely-labeled, V1 layer 5-projecting neurons in the dorsolateral geniculate nucleus (dLG) and fibers originating in V1 layer 5 neurons in the ventrolateral geniculate nucleus (vLG). (C) A time plot showing the gradual change in signal-to-noise ratio (SNR) for all three animals throughout the experiment.

Each session, we recorded fluorescence time series for a subset of the GCaMP8m-labeled neurons and determined their calcium activity while presenting drifting grating stimuli to the mouse in a visual dome setup (Figure 7D). Both tdTomato-positive (putative 1st order) neurons as well as tdTomato-negative 2nd order neurons showed similar tuning properties (Figure 7E and F) with preferred directions slightly biased in the horizontal plane (Figure 7G). The fluorescence signal-to-noise ratio per neuron (Figure 7—figure supplement 1C) and the proportion of direction tuned neurons (Figure 7H) remained constant from day 7 to the conclusion of the experiments at day 16. These experiments demonstrate that RVdG-CVS-N2c viral vectors can be reliably used for in vivo experiments in behaving animals for circuit-specific recording and manipulation of activity and delineate a time period during which the neurons retain their normal physiological properties.

## Discussion

### Fast and efficient production of high-titer rabies virus vectors

The published production protocol for RVdGenvA-CVS-N2c rabies viral vectors utilizes the neural precursor N2A cell line since it was hypothesized to increase neuronal tropism, thereby increasing transsynaptic spread from the starter cells. However, since this cell line is relatively more difficult to transfect and maintain than other cell lines, this choice resulted in a lengthy and cumbersome production process, with low titer yields (Reardon et al., 2016). As this premise has not been directly tested, we surmised that the increased labeling efficiency stems from the N2c strain itself, rather than its production process, and created an alternative packaging system to optimize all the different steps of production. By co-expressing mammalian-optimized versions of the genes required for the rabies amplification process, in tandem with antibiotics-resistance genes driven by strong constitutive promoters, in highly resilient and easily maintained cell lines, our method effectively minimizes production time, while simultaneously increasing viral titers by orders of magnitude. The additional co-expression of TVA and envA in the pseudotyping cell lines reduces to a minimum the amount of native-coat virus needed to initiate the process, thereby nearly abolishing the presence of these particles in the pseudotyped stock, and vastly increasing tracing specificity. This advantage is particularly relevant when performing retrograde labeling from single cells (Rossi et al., 2020; Wertz et al., 2015; Wickersham et al., 2007b) where a small number of non-specifically labeled neurons can potentially account for a large fraction of the entire labeled population.

RVdG-CVS-N2c vectors have previously been shown to outperform the SAD B19 in almost any parameter measured (Ohara et al., 2018; Reardon et al., 2016), attributed to the use of neural precursor cells for their production. We show that contrary to the premise, vectors produced using the HEK-GT/BHKeT packaging system show comparable retrograde labeling efficiency to ones produced in N2A cells and significantly higher than that of SAD B19 particles. This attribute has allowed us to efficiently find and characterize non-canonical hippocampal connections, for which only anecdotal reports have been available. While we show that neurons transduced with CVS-N2c vectors produced using our cell lines maintain viability and physiological function for at least 16 days, since no direct comparisons of physiological properties and long-term viability were made with vectors produced in the N2A line, it remains possible that packaging these vectors in N2A cells would result in reduced neurotoxicity, when compared with vector packaged in non-neuronal cell lines.

Using these new vectors, we were able to demonstrate the ease in which non-canonical projections to a target population can be teased out. We chose to focus these efforts in the DG, as the ample existing anecdotal evidence allowed us to compare our results against previously verified data (Hájos and Mody, 1997; Katona et al., 2017; Klausberger and Somogyi, 2008; Szabo et al., 2017). In line with these reports, retrograde labeling from DGCs labeled two distinct populations of inhibitory neurons, residing in the S.O. and S.LM of the CA1, which mainly contain neurons projecting to the apical dendrites of CA1 neurons. In addition to these aforementioned populations, we have also observed a third population of labeled neurons along the superficial most layer of the subiculum, directly in the path of perforant path fibers. Unlike the previous ones, these cells did not express the inhibitory fluorescent indicator for GAD1, which suggests that this might be a yet undiscovered intrahippocampal excitatory projection to the DG. Since in the GAD1-EGFP line not all inhibitory neurons may express the fluorescent marker (Tamamaki et al., 2003), it remains a possibility that these neurons are also inhibitory but are somehow genetically indisposed to express the marker. However, their pyramidal-like morphology, spiny dendritic arbors and putative expression of the CaMKIIa promoter, all hallmarks of excitatory neurons, render this possibility unlikely.

The successful deployment of RVdGenvA viral vectors is mainly limited by the ability to genetically dissect the target population. While many different mouse lines have been previously used for this purpose, covering the vast majority of genetically unique populations, the robust amplification capabilities of RVdG-CVS-N2c vectors require a high degree of specificity, in order to avoid possible off-target effects. We have developed several approaches that could further improve experimental paradigms, designed to attain results that are more specific. For example, cre-off viruses with specific promoters for AAV vectors can be used together with their cre-on equivalents in order to determine which projections are specific to a target population in a given region, and which are shared by the general population of neurons in a given brain region. In addition, intersectional genomic and viral-borne recombination could be used to dissect and highlight specific sub-populations of projection neurons. Using the vectors we designed, this toolbox can be expanded further to include other restriction approaches, such as tet-controlled elements.

Complementing these tools is a new suite of mono- and bicistronic RVdG-CVS-N2c vectors, expressing a broad range of fluorophores, recombinases, synaptic markers, optogenetic actuators and genetically encoded calcium indicators, to enable for diverse experimental purposes (see Key resources table). We demonstrate the flexibility of this approach, by expressing and imaging the recently developed calcium indicator GCaMP8m (Zhang et al., 2021) in the presynaptic neuronal population of starter neurons, that themselves project to the thalamus. Furthermore, we show that using the CVS-N2c endogenous N-P linker, we could effectively separate at least two individual elements, and possibly more. Apart from enabling better tracking of distinct subcellular compartments, we also show that the separation of the fluorophore from optogenetic actuators can increase their light responsiveness, possibly as a result of improved membrane trafficking and higher expression levels. However, some of these properties should also be attributed to the improved ChR2 variant we used, which was shown to possess faster kinetics (Lin et al., 2009). Another benefit of this separation is better identification of labeled neurons, since the untethering of the fluorophore from membrane-bound proteins leads to its predominantly cytosolic expression.

### Conclusion

We present here a comprehensive toolkit for rapid, high-throughput production of RVdG-CVS-N2c rabies viral vectors, along with an extended multipurpose AAV and CVS-N2c vector suites. These vectors now allow extensive labelling of presynaptic projections, facilitating a more comprehensive understanding of neuronal network wiring, at greater specificity, efficiency and versatility for the experimenter. Together, this system enables a fast, simple and highly effective approach for circuit mapping in the mammalian brain.

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
      <td>Strain, strain background (mouse Prox1cre)</td>
      <td>Tg(Prox1-cre)SJ32Gsat/Mmucd</td>
      <td>MMRRC (N. Heintz)</td>
      <td>036644-UCD</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse Calb1cre)</td>
      <td>B6;129S-Calb1tm2.1(cre)Hze/J</td>
      <td>Jackson labs (H. Zeng)</td>
      <td>028532</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse Ascl1creERT2)</td>
      <td>Ascl1tm1.1(Cre/ERT2)Jejo/J</td>
      <td>Jackson labs (J. Johnson)</td>
      <td>012882</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse Ai14)</td>
      <td>B6.Cg-Gt(ROSA)26Sortm14(CAG-tdTomato)Hze/J</td>
      <td>Jackson labs (H. Zeng)</td>
      <td>007914</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse GAD1EGFP)</td>
      <td>Not deposited</td>
      <td>K.Obata and Y.YanagawaTamamaki, N., Yanagawa, Y., Tomioka, R., Miyazaki, J.I., Obata, K., and Tamamaki et al., 2003. Green fluorescent protein expression and colocalization with calretinin, parvalbumin, and somatostatin in the GAD67-GFP knock-in mouse. Journal of Comparative Neurology 467, 60–79. https://doi.org/10.1002/cne.10905.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse Dlx5/6FlpE)</td>
      <td>Tg(mI56i-flpe)39Fsh/J</td>
      <td>Jackson labs (G. Fishell)</td>
      <td>010815</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse RCE-FRT)</td>
      <td>Gt(ROSA)26Sortm1.2(CAG-EGFP)Fsh/Mmjax</td>
      <td>Jackson labs (G. Fishell)</td>
      <td>32038</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse Ai65)</td>
      <td>B6;129S-Gt(ROSA)26Sortm65.1(CAG-tdTomato)Hze/J</td>
      <td>Jackson labs (H. Zeng)</td>
      <td>010815</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>HEK293T</td>
      <td>ATCC</td>
      <td>CRL-3216</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (hamster)</td>
      <td>BHK-21</td>
      <td>ATCC</td>
      <td>CCL-10</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>HEK-GT</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>HEK-TVA</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (hamster)</td>
      <td>BHK-eT</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pCAG-B19N</td>
      <td>AddGene (I. Wickersham)</td>
      <td>#59924</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pCAG-B19P</td>
      <td>AddGene (I. Wickersham)</td>
      <td>#59925</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pCAG-B19L</td>
      <td>AddGene (I. Wickersham)</td>
      <td>#59922</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAdDeltaF6</td>
      <td>AddGene (J. Wilson)</td>
      <td>#112867</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>rAAV-DJ RepCap</td>
      <td>Mark A. Kay</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>rAAV2-retro helper</td>
      <td>AddGene (A. Karpova and D. Schaffer)</td>
      <td>#81070</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-EF1a-Cre</td>
      <td>AddGene (K. Deisseroth)</td>
      <td>#55636</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-hSyn-mCherry</td>
      <td>AddGene (K. Deisseroth)</td>
      <td>#114472</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVdG-RVDG-CVS-N2c-EGFP</td>
      <td>AddGene (T. Jessell)</td>
      <td>#73461</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVdG-RVDG-CVS-N2c-tdTomato</td>
      <td>AddGene (T. Jessell)</td>
      <td>#73462</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-Ef1a-TVA-2A-oG</td>
      <td>This paper</td>
      <td>#172359</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-Ef1a-TVA-2A-N2cG</td>
      <td>This paper</td>
      <td>#172360</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-FRT-EF1a-TVA-2A-N2cG</td>
      <td>This paper</td>
      <td>#172361</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-CaMKII-TVA-P2A-N2cG</td>
      <td>This paper</td>
      <td>#172362</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-SEO-CaMKII-TVA-P2A-N2cG</td>
      <td>This paper</td>
      <td>#172363</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-mDLX-TVA-2A-N2cG</td>
      <td>This paper</td>
      <td>#172364</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-mDLX-TVA-2A-N2cG</td>
      <td>This paper</td>
      <td>#172365</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-CAG-TVA-P2A-dTomato</td>
      <td>This paper</td>
      <td>#177016</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-DIO-EF1a-TVA-P2A-EYFP</td>
      <td>This paper</td>
      <td>#177017</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pAAV-SEO-CaMKII-EGFP</td>
      <td>This paper</td>
      <td>#177018</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>MMLV-CAG-TVA-IRES-Puro</td>
      <td>This paper</td>
      <td>#172366</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>MMLV-CAG-SADB19_oG-IRES-Puro</td>
      <td>This paper</td>
      <td>#172367</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>MMLV-CAG-G_oT7pol-IRES-BSD</td>
      <td>This paper</td>
      <td>#172369</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>pLV-EF1a-N2c_envA-IRES-Neo</td>
      <td>This paper</td>
      <td>#172368</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-tdTomato-ChIEF</td>
      <td>This paper</td>
      <td>#172370</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-EGFP-ChIEF</td>
      <td>This paper</td>
      <td>#172371</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-EGFP-iCre</td>
      <td>This paper</td>
      <td>#172372</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-EGFP-FlpO</td>
      <td>This paper</td>
      <td>#172373</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-tdTomato-iCre</td>
      <td>This paper</td>
      <td>#172374</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-tdTomato-FlpO</td>
      <td>This paper</td>
      <td>#172375</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-mTurquoise</td>
      <td>This paper</td>
      <td>#172376</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-E2_Crimson</td>
      <td>This paper</td>
      <td>#172377</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-nl.mCherry-FlpO</td>
      <td>This paper</td>
      <td>#172378</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-nl.EGFP-FlpO</td>
      <td>This paper</td>
      <td>#172379</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-nl.EGFP-SypGFP</td>
      <td>This paper</td>
      <td>#172380</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-SypRFP</td>
      <td>This paper</td>
      <td>#172381</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-nl.EGFP-tdTomato</td>
      <td>This paper</td>
      <td>#172382</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-EYFP</td>
      <td>This paper</td>
      <td>#172383</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-mCitrine</td>
      <td>This paper</td>
      <td>#172384</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-nl.mCherry-GCaMP7s</td>
      <td>This paper</td>
      <td>#172385</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-nl.EGFP-jRGECO1a</td>
      <td>This paper</td>
      <td>#172386</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-GCaMP8f</td>
      <td>This paper</td>
      <td>#172387</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-GCaMP8m</td>
      <td>This paper</td>
      <td>#172388</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmid)</td>
      <td>RVDG-CVS-N2c-GCaMP8s</td>
      <td>This paper</td>
      <td>#172389</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti parvalbumin (rabbit polyclonal)</td>
      <td>Swant antibodies</td>
      <td>PV-27</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti somatostatin (rabbit polyclonal)</td>
      <td>BMA Biomedicals</td>
      <td>T-4102</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti EGFP (Chicken polyclonal)</td>
      <td>Abcam</td>
      <td>AB13970</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti FLAG (mouse monoclonal)</td>
      <td>Sigma Alderich</td>
      <td>F1804</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 647-conjugated goat anti-rabbit</td>
      <td>Invitrogen</td>
      <td>A-21244</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 647-conjugated goat anti-mouse</td>
      <td>Invitrogen</td>
      <td>A-21235</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488-conjugated goat anti-chicken</td>
      <td>Invitrogen</td>
      <td>A-11039</td>
      <td>1:1000 dilution</td>
    </tr>
  </tbody>
</table>

### Generation of stable packaging cell lines

Retro-, and lentiviral vectors were produced by transfecting HEK293T cells (CRL-3216, ATCC) with one of the following vectors: pMMLV-CAG-SAD B19_optimized_G-IRES-Puro, pMMLV-CAG-optimized_T7pol-IRES-BSD, pLenti-EF1a-envA-IRES-Neo and pMMLV-CAG-TVA-IRES-Puro, along with the compatible retro- or lenti-viral GAG-Pol and the vesicular stomatitis virus glycoprotein (VSV-G), by means of calcium-phosphate precipitation. Viruses were collected and filtered 48 hr post transfection and used to transduce low-passage HEK293T or BHK-21 (CCL-10, ATCC) cells. Three days post transduction, the cells were passaged and one of the following antibiotics were added to the medium in order to select for the cells which stably express the respective construct: Puromycin dihydrochloride (3 µg ml–1), blasticidine S hydrochloride (15 µg ml–1), or G418 disulfate (Neomycin, 500 µg ml–1, Sigma-Aldrich in all cases). Once the cells reached full confluence again, they were passaged, and again supplemented with the antibiotics. This cycle was repeated for at least three times a week for two weeks before initial use for production of rabies viral vectors. The new cell lines have all tested negative for mycoplasma. All cell lines and plasmids presented in this study are available from the corresponding author upon request and all plasmids are also available from Addgene (See Key resources table).

### Generation of bicistronic CVS-N2c rabies viral vectors

A method to produce bicistronic reading frames in rabies viral vectors has previously been described for vectors of the SAD B19 strain (Osakada and Callaway, 2013). Here, we adapted this approach for CVS-N2c vectors by inserting the virus’s endogenous N-P linker between two coding sequences, which led to efficient separation of the proteins with no observable effect on the expression levels of either. The sequence for the linker used is: CATGAAAAAAActAACACTCCTCC (lower case letters indicate the N-P boundary).

### Production of rabies viral vectors

HEK293-GT cells were used to rescue both SAD B19 and CVS-N2c rabies viral vectors. First, the cells were plated in a 35 mm culture dish and allowed to grow till they reached 80–90% confluence. Subsequently, they were transfected with the rabies vector plasmid and the SADB19 helper plasmids pTIT-N, pTIT-P and pTIT-L using polyethylenimine (PEI). Twenty-four hours later, the transfected cells were resuspended and re-plated in a 100 mm culture dish and incubated at 37 °C/5% CO2 until they regained full confluence. Cells were maintained that way with frequent medium changes until ~100% of the cells were fluorescent, usually 5–6 days from time of transfection and 1–2 days from the point fluorescence was first detected. At this point the medium was harvested, filtered, aliquoted, and kept at −80 °C until further use.

For pseudotyping of rabies vectors, BHK-eT cells were used to simultaneously pseudotype and amplify the vectors: First, low confluence BHK-eT cells were plated in two 100 mm culture dishes and each transduced with 0.5 ml of the native-coat virus. Once the cells reached full confluence, they were washed twice with Dulbecco’s modified Eagle medium (DMEM), resuspended and each re-plated in a new 150 mm culture dish. Once the cells reached full confluence again and ~100% of them were fluorescent (~3 days post transduction), the medium was collected, filtered, stored at 4 °C and replaced with fresh medium. This process was then repeated for two to three consecutive days. Following the last collection, the virus was pooled and centrifuged at 70,000 rcf for 1.5 hr. Following centrifugation, the medium was aspirated and the viral pellet resuspended in 200 µl phosphate-buffered saline (PBS), pH 7.4, aliquoted and stored at −80 °C until use.

For titration of envA-pseudotyped rabies viral vectors, HEK293-TVA were plated in 35 mm wells at low confluence along with one well containing HEK293T cells for detection of unpseudotyped particles. The following day, cells from one of the HEK293-TVA wells were resuspended and counted, while the cells in the remaining wells were transduced with 1 µl concentrated virus in serial dilutions ranging from 1:10–1:10,000. To estimate the presence of native coat particles in each preparation, HEK293T cells in similar confluence were transduced in parallel with 1 µl of undiluted virus. Three days later, the cells were resuspended, washed with PBS and fixed with 4% paraformaldehyde (PFA). The fraction of transduced cells in each well was determined using flow cytometry (FACS Aria III), where the most extreme cell in a population of non-treated cells was used to determine the threshold. The titer was finally calculated based on a previously published formula (Wickersham et al., 2010). In all of the titrations performed for viruses produced using our packaging system fluorescently labeled cells were not detected in the control plate containing HEK293T cells, even when transduced with vectors at concentrations an order of magnitude higher than required for complete labeling of HEK-TVA cells. While on some occasions, cells in this control condition were detected beyond the predetermined threshold, these always had substantially weaker fluorescence than the peak fluorescence of the positively labeled cells. While it cannot be completely ruled out that these originate from cells transduced with native coat particles, it is more likely that this weak signal originates from slightly higher autofluorescence.

### Production of adeno-associated viral vectors

Adeno-associated virus (AAV) production was performed in HEK293T cells based on a previously-published protocol (McClure et al., 2011). Briefly, fully confluent HEK293 cells were transfected with an AAV2 vector plasmid along with pAdenoHelper and the AAV-dj RepCap plasmids using PEI. Thirty-six hours post transfection, the cells were harvested, pelleted, and lysed using three freeze-thaw cycles. The lysed cells were incubated with benzonase-nuclease (Sigma-Aldrich) for one hour and then the debris was pelleted and the virus-containing supernatant collected and passed through a 0.22 µm filter. The collected supernatant was subsequently mixed with an equal amount of heparin-agarose (Sigma-Aldrich) and kept at 4 °C overnight with constant agitation. The following day, the agarose-virus mixture was transferred to a chromatography column and the agarose was allowed to settle. The supernatant was then drained from the column by means of gravity and the agarose-bound virus was washed once with PBS and then eluted using PBS supplemented with 0.5 M NaCl. The eluted virus was then filtered again, desalinated and concentrated using a 100 kDa centrifugal filter and then aliquoted and stored at −80 °C until use. All AAV plasmids presented in this study are available from Addgene (see Key resources table).

### Animals

All transgenic driver and reporter lines have been previously characterized(see Key resources table). In all experiments, male and female mice were used interchangeably in equal proportions, in an age range which varied between 1 and 6 months old. Neither sex nor age-related differences could be observed in any of the measurements. Experiments on C57BL/6 wild-type and transgenic mice were performed in strict accordance with institutional, national, and European guidelines for animal experimentation and were approved by the Bundesministerium für Wissenschaft, Forschung und Wirtschaft and Bildung, Wissenschaft und Forschung, respectively, of Austria (A. Haslinger, Vienna; BMWF-66.018/0010-WF/V/3b/2015; BMBWF-66.018/0008-WF/V/3b/2018).

### Organotypic hippocampal slice culture preparation

Hippocampal organotypic slice cultures were prepared from both hemispheres using the interface method (Stoppini et al., 1991). The entire hippocampus with entorhinal cortex was dissected from the brain of 5- to 8-day-old wild type mouse pups and cut perpendicularly to the longitudinal axes using a McIllwain tissue chopper. Hippocampus extraction and cutting were performed in a medium containing Hanks’ Balanced Salt Solution (HBSS, Gibco) and 20% D-glucose (Braun). Slices were placed on microporous membrane inserts (Millicell, Millipore) floating on culture media containing 50% minimum essential medium, 25% basal medium Eagle, 25% heat-inactivated horse serum, 2 mM glutamax (all from GIBCO) and 0.62% D-glucose (Braun). Slice cultures were kept at 37 °C and 5% CO2, until used for viral transduction experiments.

### Stereotaxic intracranial virus injections

For in vivo delivery of viral vectors, 1- to 6-months-old male or female mice were anesthetized with isoflurane, injected with analgesics and placed in a stereotaxic frame where they continued to receive 1–5% isoflurane vaporized in oxygen at a fixed flow rate of 1 l min–1. Leg withdrawal reflexes were tested to evaluate the depth of anesthesia and when no reflex was observed an incision was made across the scalp to expose the skull. Bregma was then located, and its coordinates used as reference for anterior-posterior (AP) and medio-lateral (ML) coordinates while the surface of the dura at the injection site was used as reference for dorso-ventral (DV) coordinates. In our experiments, we used the following sets of AP/ML/DV coordinates (in mm): DG: −1.9/1.3/–1.9; CA1: −1.9/1.5/–1.2; V1: −3.5/2/–0.7; LD: −1.3/1.3/–2.5. AAV vectors were first diluted 1:5 in PBS and delivered to the injection site at a volume of 0.3 µl and a rate of 0.06 µl min-1, using a Hamilton syringe and a 32 G needle. After the injection was completed, the needle was left in place for a few additional minutes to allow the virus to diffuse in the tissue and then slowly retracted. At the end of the injection session, the scalp was glued back together, and the mice were returned to their home cage to recover. Injection of pseudotyped rabies viral vectors took place 2–3 weeks after initial injection of AAV vectors containing the TVA receptor and rabies glycoprotein. Pseudotyped rabies vectors were first diluted to reach a final concentration of ~2–5 x108 TU ml–1 and then injected in the same manner as the AAV. Except for rabies injections into the DG of Prox1-cre transgenic animals, all other injections of rabies virus were shifted –0.2 mm AP and –0.2 mm ML. This was done in order to avoid, as much as possible, non-specific labeling along the needle tract of the first injection, due to the lack of complete specificity of cre-recombinase expression in the other transgenic lines used in this study.

### Slice preparation and electrophysiology

Electrophysiological recordings from identified retrogradely-labeled cells were performed 5–7 days following injection of CVS-N2c vectors. Manipulated animals were anaesthetized using an MMF mixture consisting of medetomidin (0.5 mg kg–1), midazolam (5 mg kg–1) and fentanyl (0.05 mg kg–1) and subsequently perfused through the heart with 20 ml ice-cold dissection solution containing 87 mM NaCl, 25 mM NaHCO3, 2.5 mM KCl, 1.25 mM NaH2PO4, 10 mM D-glucose, 75 mM sucrose, 0.5 mM CaCl2, and 7 mM MgCl2 (pH 7.4 in 95% O2/5% CO2, 325 mOsm). The brain was then removed and the hippocampus along with the adjacent cortical tissue was dissected out and placed into a precast mold made of 4% agarose designed to stabilize the tissue. The mold was transferred to the chamber of a custom-built or a VT1200 vibratome (Leica Microsystems) and the tissue was transversely sectioned into 300-µm-thick slices in the presence of ice-cold dissection solution. Transverse cortico-hippocampal sections were allowed to recover for ∼30 min at ∼31 °C and then kept at room temperature (20 ± 1°C) for the duration of the experiments. During recordings, slices were superfused with recording solution containing 125 mM NaCl, 2.5 mM KCl, 25 mM NaHCO3, 1.25 mM NaH2PO4, 25 mM D-glucose, 2 mM CaCl2, and 1 mM MgCl2 (pH 7.4 in 95% O2/5% CO2, ∼325 mOsm, at a rate of ∼1 ml min–1 using gravity flow). Labeled neurons in the regions of interest were identified according to their fluorescent signal and patched using pulled patch pipettes containing: 125 mM K-gluconate, 20 mM KCl, 0.1 mM EGTA, 10 mM phosphocreatine, 2 mM MgCl2, 2 mM ATP, 0.4 mM GTP, 10 mM HEPES (pH adjusted to 7.28 with KOH, ∼310 mOsm); 0.3% biocytin was added in a subset of recordings. Patched cells were maintained in current-clamp mode at the neuron’s resting membrane potential. Signals from patched cells were acquired using an Axon Axopatch 200 A amplifier (Molecular Devices) and digitized using a CED Power 1401 analog-to-digital converter (Cambridge Electronic Design). Optogenetic stimulation was delivered using a blue-filtered white LED (Prizmatix, IL) at maximum intensity, passed through a 63×objective which was positioned above the recorded neuron. Ten bursts, spaced 20 s apart, consisting each of 5 light pulses (5 ms in duration) at 25 Hz were delivered to the tissue. Cells which exhibited responses with latency shorter than 1 ms or longer than 10 ms were excluded from the final analysis as they likely result from direct ChIEF activation in the recorded neuron or a polysynaptic response, respectively. Following these protocols, current steps ranging from −150 pA to 300 pA, with 25 pA increments, were delivered in current-clamp mode in order to determine firing frequency and input resistance, as previously described (Kowalski et al., 2016). At the end of each recording session, the electrode was slowly retracted to create an outside-out patch, following which the slice was removed from the recording chamber, submerged in 4% PFA and subsequently kept in 0.1 M phosphate buffer (PB) until further processing.

### Fixed tissue preparation

For imaging purposes, animals were sacrificed 5–7 days after injection of CVS-N2c vectors. First, animals were anaesthetized as described in the previous section and intracardially perfused with 15 ml of 0.1 PB followed by 30 ml of 4% PFA. Following perfusion, the brain was removed and kept in 4% PFA overnight at 4 °C, which was subsequently replaced with 0.1 M PB. Fixed brains were sectioned 100 µm thick in either a coronal, parasagittal, or transverse plain and stored in 0.1 M PB at 4 °C.

For immunohistochemical labeling of transduced tissue, standard protocols were used. First, the sections were washed with PB 3 × /10 min. Next, sections were incubated with 10% normal goat serum (NGS) and 0.4% Triton X-100 for 1 hr, at room temperature (RT) with constant agitation and subsequently with the primary antibody (Rabbit anti-somatostatin, 1:500, BMA Biomedicals; Rabbit anti-parvalbumin, 1:1000, Swant antibodies; Chicken anti-GFP, 1:000, Abcam; Mouse anti-FLAG, 1:1000, Sigma-Aldrich), in PB containing 5% NGS and 0.4% Triton X-100, at 4 °C overnight. After washing, slices were incubated with isotype-specific secondary antibodies (Alexa Fluor 647-conjugated goat anti-rabbit, Alexa Fluor 647-conjugated goat anti-mouse or Alexa Fluor 488-conjugated goat anti-chicken) in PB containing 5% NGS and 0.4% Triton X-100 for two hours in RT with constant agitation. After washing, slices were mounted, embedded in Prolong Gold Antifade mountant (Thermo-Fisher Scientific, Cat# P36930) and sealed with a 0.5 mm coverslip.

Neurons in acute slices that were filled with biocytin (0.3%) were processed for morphological analysis. After withdrawal of the pipettes, resulting in the formation of outside-out patches at the pipette tips, slices were fixed for 12–24  hr at 4  °C in a 0.1  M PB solution containing 4% PFA. After fixation, slices were washed, treated with Streptavidin Alexa Fluor 647 Conjugate (Thermo Fisher) for two hours at room temperature, washed again and embedded in Mowiol (Sigma-Aldrich).

### Microscopy and image analysis

All representative confocal images were acquired using either an LSM 800 microscope (Zeiss) or a Dragonfly spinning disc confocal microscope (Andor). All representative confocal images displayed in this manuscript were processed using FIJI (Schindelin et al., 2012) and are shown as a maximal intensity projection of an image stack of 4–12 separate images. For quantification of cell numbers including channel overlap, Imaris 9 software was used.

### Cranial window implantation for in vivo CVS-N2c-GCaMP8m imaging

Before the surgery, animals were injected with meloxicam (20 mg kg–1 s.c., 3.125 mg ml–1 solution) and dexamethasone (0.2 mg kg–1 i.p., 0.02 mg ml–1 solution). Anesthesia was induced by 2.5% isoflurane in oxygen in an anesthesia chamber. The mouse was subsequently fixed in a stereotaxic device (Kopf) with constant isoflurane supply at 0.7 to 1.2% in O2 and body temperature controlled by a heating pad to 37.5 °C. After assertion that reflexes subsided, the cranium was exposed and cleaned of periost and connective tissue. A circular craniotomy of 4 mm diameter was drilled above V1, careful to leave the dura mater intact and the exposed brain constantly irrigated with artificial cerebrospinal fluid. A pulled glass capillary (tip diameter 30–40 µm) was loaded with CVS-N2c-GCaMP8m (5x108 TU ml–1) solution and 300 nl injected into the center of the craniotomy at a depth of 600 µm with a nanoliter injector (Nanoject, World Precision Instruments) at a speed of 30 nl min–1 and leaving the needle in place for 5 min after the volume was injected. Subsequently, a 4 mm circular glass coverslip (CS-4R, Warner Instruments) was positioned on the brain and careful pressure applied with a toothpick mounted in the stereotaxic arm. The glass was first fixed in place with VetBond (3 M). Then after cleaning and drying the surrounding cranium, a multilayer of glues was applied. First, to provide adhesion to the bone, All-in-One Optibond (Kerr) was applied and hardened by blue light (B.A. Optima 10). Second, Charisma Flow (Kulzer) was applied to cover the exposed bone and fix the glass in place by also applying blue light. After removal of the fixation toothpick, a custom designed and manufactured (RPD, Vienna) headplate, selective laser-sintered from the medical alloy TiAl6V4 (containing a small bath chamber and micro-ridges for repeatable fixation in the setup), was positioned in place and glued to the Charisma on the cranium with Paladur (Kulzer). Mice were given 300 µl of saline and 20 mg kg–1 meloxicam s.c., before removing them from the stereotaxic frame and letting them wake up while kept warm on a heating pad. Another dose of 20 mg kg–1 meloxicam s.c. and 0.2 mg kg–1 i.p. dexamethasone was further injected 24 hr after conclusion of the surgery.

### Setup and visual stimuli for in vivo imaging

Mice were head-fixed using a custom-manufactured clamp that was connected to a 3-axis motorized stage (8MT167-25LS, Standa). Mice could run freely on a custom-designed spherical treadmill (20 cm diameter). Visual stimuli were projected by a modified LightCrafter (Texas Instruments) at 60 Hz, reflected by a quarter-sphere mirror (Modulor) below the mouse and presented on a custom-made spherical dome (80 cm diameter) with the mouse’s head at its center. The green and blue LEDs in the projector were replaced by cyan (LZ1-00DB00-0100, Osram) and UV (LZ1-00UB00-01U6, Osram) LEDs respectively. A double band-pass filter (387/480 HD Dualband Filter, Semrock) was positioned in front of the projector to not contaminate the imaging. The reflected red channel of the projector was captured by a transimpedance photo-amplifier (PDA36A2, Thorlabs) and digitized for synchronization. Cyan and UV LED powers were adjusted to match the relative excitation of M- and S-cones during an overcast day, determined and calibrated using opsin templates (Govardovskii et al., 2000) and a spectrometer (CCS-100, Thorlabs). Stimuli were designed and presented with Psychtoolbox (Brainard, 1997), running on MATLAB 2020b (Mathworks). Stimulus frames were morphed on the GPU using a customized projection map and an OpenGL shader to counteract the distortions resulting from the spherical mirror and dome. The dome setup allows to present mesopic stimuli from ca. 90° on the left to ca. 170° on the right in azimuth and from ca. 40° below to ca. 80° above the equator in elevation. During anatomical stack imaging, dense moving dots of different sizes and light intensities, moving in uncorrelated directions were shown, to excite neurons with a complex texture-like stimulus. For functional imaging, full field step gratings with temporal frequency of 2 Hz and spatial frequency of 0.1 cycles/° were shown moving in 8 randomly ordered directions. In each trial, the grating image remained stationary for 3 s and then moved for 7 s in the respective direction. Each direction was shown 5–10 times in total per session.

### Imaging

Two-photon imaging was performed on a custom-built microscope, controlled by Scanimage (Vidrio Technologies) running on MATLAB 2020b (Mathworks) and a PXI system (National Instruments). The beam from a pulsed Ti:Sapphire laser (Mai-Tai DeepSee, Spectra-Physics) was scanned by a galvanometric-resonant (8 kHz) mirror combination (Cambridge Scientific) and expanded to underfill the back-aperture of the objective (16×0.8 N.A. water-immersion, Nikon); 1.9 by 1.9 mm field-of-view; 30 Hz frame rates. Fast volumetric imaging was acquired with a piezo actuator (P-725.4CA, Physik Instrumente). Emitted light was collected (FF775-Di01, Semrock), split (580 nm long-pass, FF580-FDi01, Semrock), band-pass filtered (green: FF03-525/50; red: FF01-641/75, Semrock), measured (GaAsP photomultiplier tubes, H10770B-40, Hamamatsu), amplified (TIA60, Thorlabs), and digitized (PXIe-7961R NI FlexRIO FPGA, NI 5734 16-bit, National Instruments). Laser wavelength was set to 935 or 955 nm, which excited GCaMP8 well and tdTomato sufficiently for anatomical identification. Maximum laser power used at the deepest planes was 80 mW mm–2. Due to the early start of imaging after implantation the tissue cleared only over the course of the imaging days, necessitating relatively high laser powers in the beginning. To avoid heat damage, only 15 min of continuous imaging was performed, after which imaging was paused for at least 5 min (Podgorski and Ranganathan, 2016). At each recording day (day 3, 5, 7, 9, 11, 14, 16 post RVdGenvA-CVS-N2c-GCaMP8m injection), first a dense anatomical stack with a 10 µm plane distance over the full accessible depth and plane averaging over 25 frames was recorded in the injected area. If GCaMP labeled neurons were found, subsequently a functional imaging session was started over 5–8 z-planes with 25–50 µm plane distance and voxel size of 1.4–1.7 µm resulting in a volume rate of 4.2–5 Hz.

### Imaging data analysis

Cell numbers were estimated by Imaris (Oxford Instruments) on anatomical stack images. Functional calcium imaging data was first analyzed with suite2p (v0.10.0) (Pachitariu et al., 2016) for motion correction and ROI extraction. ROIs were then curated manually based on morphological and activity shape. Further analysis was performed in custom MATLAB R2021a (Mathworks) scripts made available on GitLab (Sumser, 2022; copy archived at swh:1:rev:e55a2abf39ac9fb3592767173450c5af774218f7). dF/F0 was estimated based on published procedures (Keller et al., 2012) by first subtracting neuropil contamination (from suite2p, fluorescence signal of 350 pixels surrounding the ROI, excluding other ROIs) with a factor of 0.5 (estimated from fluorescence of small capillaries as reported previously); (Kerlin et al., 2010). From the neuropil-corrected ROI fluorescence, baseline F0 was defined as the 8th percentile of a moving window of 15 s (Dombeck et al., 2013). dF/F0 was then calculated on the same window by first subtracting and then dividing fluorescence trace by median of the same 15-s window (Keller et al., 2012). Signal-to-noise ratio (SNR) was defined for each neuron by dividing the 99th percentile of the dF/F trace (‘signal’) by the standard deviation of its negative values after baseline correction (‘noise’). Direction selectivity index (DSI) and preferred direction was calculated based on the vector sum method (Mazurek et al., 2014) on the mean dF/F0 of the 7 s per direction the grating was moving. DSI significance was estimated by a permutation test of the direction labels (resampled 1000 times) to define the proportion of DSIshuffled >DSI.

### Statistical analysis

All values were reported as mean and error bars as ± SEM. Statistical significance was tested using non-parametric, single-sided Kruskal-Wallis test followed by a double-sided Mann-Whitney test for post-hoc comparisons, or by Fisher’s exact test, in Microsoft Excel. Differences with p<0.05 were considered significant. In figures, a single asterisk (∗), double asterisks (∗∗), and triple asterisks (∗∗∗) indicate p<0.05, p<0.01 and p<0.001, respectively. Each experiment shown in this MS for which statistical information is not provided has been replicated in the lab a minimum of three times with identical results.
