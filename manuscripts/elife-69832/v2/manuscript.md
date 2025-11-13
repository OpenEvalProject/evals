# Genetic, cellular, and structural characterization of the membrane potential-dependent cell-penetrating peptide translocation pore

## Authors

- Evgeniya Trofimenko<sup>1</sup> ([ORCID: 0000-0003-4910-5324](https://orcid.org/0000-0003-4910-5324))
- Gianvito Grasso<sup>2</sup> ([ORCID: 0000-0002-7761-222X](https://orcid.org/0000-0002-7761-222X))
- Mathieu Heulot<sup>1</sup> ([ORCID: 0000-0001-9641-941X](https://orcid.org/0000-0001-9641-941X))
- Nadja Chevalier<sup>1</sup>
- Marco A Deriu<sup>3</sup> ([ORCID: 0000-0003-1918-1772](https://orcid.org/0000-0003-1918-1772))
- Gilles Dubuis<sup>1</sup>
- Yoan Arribat<sup>1</sup> ([ORCID: 0000-0003-0952-5279](https://orcid.org/0000-0003-0952-5279))
- Marc Serulla<sup>1</sup> ([ORCID: 0000-0002-4166-1556](https://orcid.org/0000-0002-4166-1556))
- Sebastien Michel<sup>1</sup>
- Gil Vantomme<sup>4</sup> ([ORCID: 0000-0002-7441-0737](https://orcid.org/0000-0002-7441-0737))
- Florine Ory<sup>1</sup>
- Linh Chi Dam<sup>1</sup> ([ORCID: 0000-0002-6874-2049](https://orcid.org/0000-0002-6874-2049))
- Julien Puyal<sup>4</sup> ([ORCID: 0000-0002-8140-7026](https://orcid.org/0000-0002-8140-7026))
- Francesca Amati<sup>1</sup> ([ORCID: 0000-0002-1731-0262](https://orcid.org/0000-0002-1731-0262))
- Anita Lüthi<sup>4</sup> ([ORCID: 0000-0002-4954-4143](https://orcid.org/0000-0002-4954-4143))
- Andrea Danani<sup>2</sup> ([ORCID: 0000-0001-6578-5089](https://orcid.org/0000-0001-6578-5089))
- Christian Widmann<sup>1</sup> ([ORCID: 0000-0002-6881-0363](https://orcid.org/0000-0002-6881-0363)) †

### Affiliations

1. Department of Biomedical Sciences, University of Lausanne Lausanne Switzerland
2. Dalle Molle Institute for Artificial Intelligence Research, Università della Svizzera italiana, Scuola Universitaria Professionale della Svizzera Italiana Lugano Switzerland
3. PolitoBIOMed Lab Department of Mechanical and Aerospace Engineering, Politecnico di Torino Torino Italy
4. Department of Fundamental Neurosciences, University of Lausanne Lausanne Switzerland
5. CURML (University Center of Legal Medicine), Lausanne University Hospital Lausanne Switzerland

† Corresponding author

## Abstract

Cell-penetrating peptides (CPPs) allow intracellular delivery of bioactive cargo molecules. The mechanisms allowing CPPs to enter cells are ill-defined. Using a CRISPR/Cas9-based screening, we discovered that KCNQ5, KCNN4, and KCNK5 potassium channels positively modulate cationic CPP direct translocation into cells by decreasing the transmembrane potential (Vm). These findings provide the first unbiased genetic validation of the role of Vm in CPP translocation in cells. In silico modeling and live cell experiments indicate that CPPs, by bringing positive charges on the outer surface of the plasma membrane, decrease the Vm to very low values (–150 mV or less), a situation we have coined megapolarization that then triggers formation of water pores used by CPPs to enter cells. Megapolarization lowers the free energy barrier associated with CPP membrane translocation. Using dyes of varying dimensions in CPP co-entry experiments, the diameter of the water pores in living cells was estimated to be 2 (–5) nm, in accordance with the structural characteristics of the pores predicted by in silico modeling. Pharmacological manipulation to lower transmembrane potential boosted CPP cellular internalization in zebrafish and mouse models. Besides identifying the first proteins that regulate CPP translocation, this work characterized key mechanistic steps used by CPPs to cross cellular membranes. This opens the ground for strategies aimed at improving the ability of cells to capture CPP-linked cargos in vitro and in vivo.

## Introduction

Cell-penetrating peptides (CPPs) are short non-toxic sequences of 5–30 amino acids present in proteins able to cross membranes such as homeoproteins and some viral components. CPPs can also be used to deliver bioactive cargos (siRNAs, DNA, polypeptides, liposomes, nanoparticles, and others) in cells for therapeutic or experimental purposes (Bechara and Sagan, 2013; Futaki et al., 2013; Guidotti et al., 2017; Illien et al., 2016; Jones and Sayers, 2012; Koren and Torchilin, 2012; Madani et al., 2011; Mueller et al., 2008; Ruseska and Zimmer, 2020; Trabulo et al., 2010; Vasconcelos et al., 2013). Even though they differ in their origin (Frankel and Pabo, 1988; Green and Loewenstein, 1988; Joliot et al., 1991; Oehlke et al., 1998) and physico-chemical properties, the majority of CPPs carry positive charges in their sequence (Bechara and Sagan, 2013; Guidotti et al., 2017; Jones and Sayers, 2012; Madani et al., 2011). Polyarginine (e.g. R9), HIV-1 TAT47-57, and Penetratin (Antennapedia43-58) are among the most used and studied CPPs.

The mode of CPP cellular entry is still debated and no proteins have been identified that regulate this process. CPP entry starts after the initial electrostatic interactions between the positively charged CPP and the negatively charged components of the cell membrane (Bechara and Sagan, 2013; Futaki et al., 2013; Guidotti et al., 2017; Jones and Sayers, 2012; Koren and Torchilin, 2012; Madani et al., 2011; Ruseska and Zimmer, 2020; Trabulo et al., 2010; Vasconcelos et al., 2013). Interaction with acid sphingomyelinase (Verdurmen et al., 2010) and glycosaminoglycans (Amand et al., 2012; Bechara et al., 2013; Butterfield et al., 2010; Fuchs and Raines, 2004; Futaki and Nakase, 2017; Ghibaudi et al., 2005; Gonçalves et al., 2005; Hakansson and Caffrey, 2003; Rullo et al., 2011; Rusnati et al., 1999; Ziegler, 2008; Ziegler and Seelig, 2004; Ziegler and Seelig, 2011), local membrane deformation (Hirose et al., 2012), as well as calcium fluxes (Melikov et al., 2015) have been suggested to play a role in CPP internalization. CPPs enter cells through a combination of two non-mutually exclusive mechanisms (Illien et al., 2016; Bechara et al., 2013): endocytosis and direct translocation (Bechara and Sagan, 2013; Futaki et al., 2013; Guidotti et al., 2017; Jones and Sayers, 2012; Koren and Torchilin, 2012; Madani et al., 2011; Ruseska and Zimmer, 2020; Trabulo et al., 2010; Vasconcelos et al., 2013). The nature of these entry mechanisms is debated and not fully understood at the molecular level. The vesicular internalization of CPPs has been suggested to occur through clathrin-dependent endocytosis, macropinocytosis, and caveolin-1-mediated endocytosis (Bechara and Sagan, 2013; Futaki et al., 2013; Guidotti et al., 2017; Jones and Sayers, 2012; Koren and Torchilin, 2012; Madani et al., 2011; Trabulo et al., 2010). However, recent data indicate that CPP endocytosis proceeds via a newly discovered pathway that is Rab14-dependent but Rab5- and Rab7-independent (Trofimenko et al., 2021). When CPPs are endocytosed, access to the cytosol requires that the CPPs break out of endosomes through a poorly understood process called endosomal escape.

Direct translocation allows the CPPs to access the cytosol through their ability to cross the plasma membrane. There is currently no unifying model to explain mechanistically how direct translocation proceeds and no genes have yet been identified to modulate the manner by which CPPs cross cellular membranes. Direct translocation across the plasma membrane often seemed to originate from specific areas of the cells, suggesting discrete structures on the plasma membrane involved in CPP entry (Allolio et al., 2018; Duchardt et al., 2007; Hirose et al., 2012; Wallbrecher et al., 2017; Ziegler et al., 2005). There is a general consensus though that an adequate plasma membrane potential (Vm) is required for direct translocation to occur based on live cell experiments (Rothbard et al., 2004; Wallbrecher et al., 2017; Zhang et al., 2009), as well as in silico studies (Gao et al., 2019; Lin and Alexander-Katz, 2013; Moghal et al., 2020; Via et al., 2018). Electrophysiological and pharmacological Vm modulations have revealed that depolarization blocks CPP internalization (Rothbard et al., 2004; Zhang et al., 2009) and hyperpolarization improves the internalization of cationic CPPs (Chaloin et al., 1998; Henriques et al., 2005; Moghal et al., 2020; Rothbard et al., 2004; Wallbrecher et al., 2017). By itself, a sufficiently low Vm (i.e. hyperpolarization) appears to trigger CPP direct translocation in live cells (Rothbard et al., 2004; Wallbrecher et al., 2017; Zhang et al., 2009). In silico modeling has provided evidence that membrane hyperpolarization leads to the formation of transient water pores, allowing CPP translocation into cells (Gao et al., 2019; Herce and Garcia, 2007; Herce et al., 2009; Lin and Alexander-Katz, 2013; Via et al., 2018), but the free energy landscape governing CPP translocation has not been determined. Moreover, the nature and the structural characteristics of the pores used by CPPs to cross the plasma membrane have not been investigated in live cells.

Here, we provide the first genetic evidence that validates the importance of Vm for CPP direct translocation and we characterize the diameter of the water pores used by CPPs to enter live cells. We also determined the role of the Vm in modulating the free energy barrier associated with membrane translocation and the impact of the Vm on CPP translocation kinetics.

## Results

### Modes of TAT-RasGAP317-326 cellular entry

In the present work, we have used TAT-RasGAP317-326 as a model compound to investigate the molecular basis of CPP cellular internalization. This peptide is made up of the TAT48-57 CPP and a 10 amino acid sequence derived from the SH3 domain of p120 RasGAP (Michod et al., 2004). TAT-RasGAP317-326 sensitizes cancer cells to chemo-, radio-, and photodynamic therapies (Chevalier et al., 2015; Michod et al., 2009; Pittet et al., 2007; Tsoutsou et al., 2017) and prevents cell migration and invasion (Barras et al., 2014). This peptide also exhibits antimicrobial activity (Heulot et al., 2017; Georgieva et al., 2021; Heinonen et al., 2021). Some cancer cell lines, such as Raji (Burkitt’s lymphoma), SKW6.4 (transformed B-lymphocytes), and HeLa (cervix carcinoma), are directly killed by this peptide (Heulot et al., 2016). The manner by which TAT-RasGAP317-326 kills cells has recently been uncovered (Serulla et al., 2020). The peptide first accesses the cell’s cytosol by direct translocation through the plasma membrane. It then binds to specific phospholipids, such as phosphatidylserine and phosphatidylinositol-bisphosphate that are enriched in the inner leaflet of the plasma membrane. This binding allows the peptide to disrupt the cell’s membrane causing its death by necrosis.

Most CPPs can enter cells by direct translocation and by endocytosis (Bechara and Sagan, 2013; Futaki et al., 2013; Guidotti et al., 2017; Illien et al., 2016; Jones and Sayers, 2012; Koren and Torchilin, 2012; Madani et al., 2011; Mueller et al., 2008; Ruseska and Zimmer, 2020; Trabulo et al., 2010; Vasconcelos et al., 2013). This is also the case for TAT-RasGAP317-326 (Figure 1A–B and Videos 1–3). Two types of staining were observed in cells incubated with this peptide: (i) vesicular only and (ii) vesicular and cytosolic (Figure 1A and Figure 1—figure supplement 1A). When the peptide cytosolic signal was strong, it masked the vesicular staining (Figure 1A). In our experimental settings, the cytosolic acquisition of TAT-RasGAP317-326 occurred only through direct translocation and not through endosomal escape (Figure 1—figure supplement 2, Video 4) and was not due to phototoxicity (Figure 1—figure supplement 3) as can occur in some settings (Dixit and Cyr, 2003; Ha and Tinnefeld, 2012; Levitus and Ranjit, 2011; Zheng et al., 2014).

![Figure 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig1-v2.jpg)

**Figure 1.:** (A) Depiction of the different modes of cell-penetrating peptide (CPP) entry into cells. Confocal microscopy was performed on the indicated cell lines incubated for 1 hr with 40 μM FITC-TAT-RasGAP317-326 in RPMI, 10% fetal bovine serum (FBS). Cells were washed with PBS prior to visualization. Vesicular staining is indicative of CPP endocytosis while diffuse cytosolic staining is a consequence of CPP direct translocation into cells. Scale bar: 10 μm. (B) Quantitation of the different modes of CPP entry as a function of time (FITC-TAT-RasGAP317-326 continually present in the media) using the experimental conditions presented in panel A. Types of staining were visually quantitated as indicated in Figure 1—figure supplement 1A (n = 157 cells per condition). There was no indication of fluorescence quenching, due to endosomal acidification, preventing the detection of CPP-containing endosomes (in at least during the first hour of CPP exposure) (Figure 1—figure supplement 1B). TAT-RasGAP317-326 enters cells via endocytosis and direct translocation, but only direct translocation mediates its biological activity and leads to cell death (Figure 1—figure supplement 4). Results correspond to the average of three independent experiments.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Visual attribution of the various types of staining associated with FITC-CPP internalization in wild-type HeLa cells. Cells 1–9 took up the CPP through both direct translocation and endocytosis (cells 1–4 and cells 5–9 displaying strong and weak cytosolic signal, respectively); cells 10–15 acquired FITC-TAT-RasGAP317-326 in vesicles only, no cytosolic staining being detected. The experimental conditions are those of Figure 1A. Scale bar: 20 μm. (B) Potential fluorophore quenching does not prevent detection of CPP-containing endosomes. Wild-type HeLa cells were incubated for 1 hr at 37°C in the presence of 40 μM TAT-RasGAP317-326 labeled with either FITC (susceptible to quenching at low pH) or TMR (not quenched at low pH) fluorophores. The number of vesicles was visually determined based on confocal images. There were no fewer vesicles detected in cells when the peptide was labeled with FITC than when it was labeled with TMR.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** To assess whether cytosolic peptide accumulation could be due to endosomal escape, we incubated cells with the indicated concentrations of FITC-TAT-RasGAP317-326 for 30 min, washed the cells, and then monitored the cytosolic cell-penetrating peptide (CPP) acquisition only in cells that had initially taken up the peptide by endocytosis, that is, cells that did not display, at the beginning of image acquisition, a cytosolic signal indicative of direct translocation (examples of such cells are indicated by red arrows in the scheme). The graphs show single cell quantitation of FITC-TAT-RasGAP317-326 cytosolic fluorescence (see panel D) according to the experimental setups shown on the left. The cell traces correspond to acquisitions gathered from three independent experiments (panel A, 19 cells, panel B, 16 cells, and panel C, 22 cells). As a control, when cells were not washed (i.e. the peptide was present in the medium), cytosolic acquisition increased over time (panel A; see also left panel in Video 4). However, no increase in the cytosolic signal was observed in washed out cells containing peptide-labeled endosomes (panel B and Video 4, right panel). An increase in cytosolic fluorescence could be detected when endosomal escape was artificially induced by the lysosome disruptor LLOME (Repnik et al., 2017) (panel C). In live cells therefore diffuse cytosolic TAT-RasGAP317-326 signal originates from direct translocation and not from endosomal escape. (D) Representative confocal image showing two FITC-TAT-positive cells. Nucleus is labeled in blue, endosomes with pink arrows and the orange-circled zone corresponds to a cytosolic region devoid of endosomes. Such regions are those that are used to record CPP cytosolic fluorescence signals. Scale bar: 10 μm.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** HeLa cells were incubated with 80 μM FITC-TAT-RasGAP317-326 for 30 min with the indicated frequencies of laser exposures (n = 133 cells per condition). Quantitation of the cytosolic fluorescence intensity after 30 min (n = 235 cells per condition) is shown on the left and the percentage of cells with cytosolic fluorescence is shown on the right. FITC-TAT-RasGAP317-326 translocation into cells occurred similarly after 30 min whether the cells were illuminated once or 60 times over the 30 min period. Even if one argues that a single illumination is sufficient to cause the internalization seen after a 30 min incubation period with the CPP, then the internalization should be the same whether the illumination is performed at 1 or 30 min. This is not what is observed: the internalization of the FITC-labeled CPP increases overtime independently of the number of times the cells are illuminated. The results correspond to three independent experiments.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A–E) HeLa cells were incubated with 80 μM FITC-TAT-RasGAP317-326 in RPMI, 10% fetal bovine serum (FBS) for the indicated periods of time. Peptide internalization and cell death was assessed by flow cytometry. (A) Left: Representative flow cytometry dot plot showing the gating strategy used in flow cytometry experiments. Right: Representative flow cytometry histogram of HeLa cells incubated with FITC-TAT-RasGAP317-326 in RPMI, 10% FBS for 60 min. The dotted line represents cellular autofluorescence. (B) Variation over time of the low and high intensity peak values. Peptide internalization was assessed by flow cytometry. The results correspond to three independent experiments. Note the different scales used to plot the median values of the low and high intensity populations. (C) Quantitation of cells with low intensity peptide fluorescence and vesicular staining. Total peptide internalization was assessed by flow cytometry. The percentage of cells with low cell-penetrating peptide (CPP) cytosolic fluorescence was visually quantitated on confocal images (n = 164 cells per condition). The results correspond to three independent experiments. (D) Quantitation of the pattern of appearance of cells with high intensity peptide fluorescence and strong diffuse cytosolic staining. Data assessment as in panel C. The results correspond to three independent experiments. (E) Kinetics of FITC-TAT-RasGAP317-326-induced death in the two populations described in panel B. Cell death was assessed by propidium iodide (PI) staining. The results correspond to three independent experiments.

![Video 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-video1.mp4.jpg)

**Video 1.:** Representative confocal time-lapse recording of wild-type Raji cells incubated with 5 μM TAT-RasGAP317-326 for 16 hr in RPMI in the absence of serum. For the first 30 min of the recording, images were taken every 30 s, then until the end of the recording, images were taken every 5 min. Peptide was present in the media throughout the recording. Yellow and pink arrows indicate cells taking up the peptide by direct translocation and by endocytosis, respectively. Cyan arrows point toward labeled endosomes and green asterisks to dead cells. Scale bar: 20 μm. Time is displayed in hours:minutes.

![Video 2.](https://cdn.elifesciences.org/articles/69832/elife-69832-video2.mp4.jpg)

**Video 2.:** Time-lapse recording of Raji cells incubated with 40 μM TAT-RasGAP317-326 for 30 min in RPMI, 10% fetal bovine serum (FBS). Peptide was present in the media throughout the recording and images were taken for 30 min at 10 s intervals. Scale bar: 10 μm. Time is displayed in minutes:seconds.

![Video 3.](https://cdn.elifesciences.org/articles/69832/elife-69832-video3.mp4.jpg)

**Video 3.:** Time-lapse recording of HeLa cells incubated with 80 μM FITC-TAT-RasGAP317-326 in RPMI, 10% fetal bovine serum (FBS). Yellow and pink arrows indicate cells experiencing direct translocation and endocytosis, respectively. Images were taken for 30 min at 10 s intervals. Scale bar: 20 μm. Time is displayed in minutes:seconds.

![Video 4.](https://cdn.elifesciences.org/articles/69832/elife-69832-video4.mp4.jpg)

**Video 4.:** Wild-type HeLa cells were pre-incubated with 80 μM FITC-TAT-RasGAP317-326 for 30 min in RPMI, 10% fetal bovine serum (FBS) and then imaged every 5 min for 4 hr at 37°C, 5% CO2. Video on the left was recorded in the continuous presence of the peptide. Video on the right was recorded after the peptide was washed out three times with RPMI, 10% FBS. Scale bar: 10 μm. Time is displayed in hours:minutes.

### Identification of potassium channels as mediators of TAT cargo direct translocation into cells

As TAT-RasGAP317-326 needs to translocate through the plasma membrane to reach the cytosol, a prerequisite for the peptide to kill cells (Serulla et al., 2020), we used the killing ability of the peptide in a CRISPR/Cas9 screen to identify genes involved in CPP direct translocation in two different cell lines (Raji and SKW6.4 cells) (Figure 2—figure supplement 1A). The top candidate genes identified through this approach were specific potassium channels or genes coding for proteins known to regulate such channels indirectly (e.g. PIP5K1A; Suh and Hille, 2008; Figure 2A and Figure 2—figure supplement 1B). KCNQ5, identified in Raji cells, is a voltage-dependent potassium channel. KCNN4 and KCNK5, identified in SKW6.4 cells, are calcium-activated channels and belong to the two-pore (voltage-independent) potassium channel family (Shieh et al., 2000), respectively.

![Figure 2.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig2-v2.jpg)

**Figure 2.:** (A) Identification of genes implicated in TAT-RasGAP317-326 internalization in Raji and SKW6.4 cells. The graphs depict the p-value (calculated using the MAGeCK procedure; see Materials and methods) for the difference in sgRNA expression between peptide-treated and control cells for the ~20,000 genes targeted by the CRISPR/Cas9 library. (B) Quantitation of TAT-RasGAP317-326 entry (top) and induced death (bottom) in wild-type (WT) and knock-out (KO) cells. The WT and the corresponding potassium channel KO versions of the indicated cell lines were pretreated or not for 30 min with 10 μM XE-991 or with TRAM-34 and then incubated (still in the presence of the inhibitors when initially added) with or without 40 μM (Raji and SKW6.4 cells) or 80 μM (HeLa cells) TAT-RasGAP317-326. Internalization was recorded after 1 hr and cell death after 16 hr (Raji and SKW6.4) or 24 hr (HeLa). Results correspond to the average of three independent experiments. TAT-RasGAP317-326 concentrations and time of incubation used were adjusted so that the CPP induced similar cell death (between 60% and 90%) in the WT versions of the different cell lines. (C) Quantitation of the modalities of TAT-RasGAP317-326 entry in WT and KCNQ5 KO Raji cells. Cells were incubated with FITC-TAT-RasGAP317-326 for various periods of time and peptide staining was visually quantitated on confocal images (n = 165 cells for each time-point). The high percentage of cells with vesicular staining in the KO cells results from the absence of strong diffuse staining masking endosomes. The results correspond to the average of three experiments.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Scheme of the CRISPR/Cas9 screening strategy to identify genes involved in TAT-RasGAP317-326 cellular entry. Raji and SKW6.4 cells were infected with a single guide RNA (sgRNA) CRISPR/Cas9 lentiviral library in conditions favoring the expression of only one specific sgRNA per cell (which is indicated by differentially colored cells). The infected cells were then incubated with or without 40 μM TAT-RasGAP317-326 for 8 days (Raji) or 17 days (SKW6.4). The expression of sgRNAs in both populations was assessed by massive parallel sequencing to determine the enrichment or depletion in specific sgRNAs in the peptide-treated population. (B) Scatter-plot depicting the changes in sgRNA expression between the control and treated cell populations. The most significantly modulated sgRNA sets are color-coded.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A–C) Sequencing of the regions targeted by the single guide RNAs (sgRNAs) disrupting KCNQ5, KCNK5, and KCNN4 potassium channels in Raji (panel A), SKW6.4 (panel B), or HeLa cells (panel C). Mutations, insertions, and deletions induced by the CRISPR/Cas9 system are shown in red. Except the cases mentioned below, these mutations induce a frame shift and early termination of the open reading frame. The sequences targeted by the sgRNAs are highlighted in yellow. The sgRNA-induced mutations in the first allele of clone Q5-2, in the first allele of SKW6.4 cells clone N4-2, and in the first allele of clone K5-2 do not induce a frame shift but are located in critical domains necessary for potassium channel activity, such as the pore-forming region of KCNK5 (uniprot accession number: O95279), region adjacent to the pore of KCNQ5 (uniprot accession number: Q9NR82), or calcium recognition domain of KCNN4 (uniprot accession number: O15554). Hence, these alleles presumably encode non-functional channels. Clones Q5-1 in Raji, N4-1, and K5-1 in SKW6.4, and N4-1 in HeLa cells were those that were used in subsequent experiments. The blue nucleotides correspond to silent changes, aimed at reducing sgRNA targeting, introduced in the KCNQ5-encoding lentiviral vector used in panel E. PAM (protospacer adjacent motif) sequences are italicized. (D–F) The indicated wild-type (WT) and knock-out (KO) cells, infected or not with sgRNA-resistant FLAG-KCNQ5-encoding lentiviruses or KCNN4-expressing lentiviruses, were tested for their ability to be killed by TAT-RasGAP317-326. Cell death was assessed by flow cytometry of propidium iodide (PI)-stained cells after 16 hr (Raji and SKW6.4 cells) or 24 hr (HeLa cells). The results correspond to the average of three independent experiments. Expression of the FLAG-KCNQ5 and KCNN4-V5 constructs was detected by Western blotting using an anti-FLAG antibody and an anti-V5 antibody, respectively. Note that the Raji, SKW6.4, and HeLa KO cell lines still express Cas9 and the sgRNAs targeting the potassium channels. Hence, the ectopically expressed WT potassium channel-encoding cDNAs can be targeted by the CRISPR/Cas9 system but this nevertheless allows for a detectable expression of the FLAG- or V5-tagged constructs although to much lower levels than in similarly infected WT cells lacking Cas9 and sgRNAs (Figure 2—figure supplement 2—source data 1; compare last two lanes). In Raji cells, the re-expressed KCNQ5 channel contained five silent changes in the sgRNA recognition site (see panel A) but this proved insufficient to allow for a strong ectopic expression (compare lanes 2 and 4 in Figure 2—figure supplement 2—source data 3; Figure 2—figure supplement 2—source data 5).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Same as Figure 2C, but for wild-type (WT), KCNN4 and KCNK5 SKW6.4 knock-out (KO) cells. The results correspond to the average of three independent experiments. (B) As panel A, but for WT and KCNN4 KO HeLa cells. The results correspond to the average of three independent experiments. (C) Quantitation by flow cytometry of 20 μg/ml AlexaFluor488-transferrin (left) or 200 μg/ml 10 kDa FITC-Dextran (right) internalization in the indicated WT cell lines and their corresponding KO versions, pretreated or not for 30 min with the XE-991 (10 μM) or TRAM-34 (10 μM) potassium channel inhibitors. Transferrin and dextran internalization was allowed to proceed for 60 min (still in the presence of inhibitors when these were used in the 30 min pre-incubation period). To quench membrane-bound fluorescence, cells were incubated with 0.2% trypan blue prior to flow cytometry analysis. The independent experiment replicates are color-coded. (D) Assessment of FITC-TAT-RasGAP317-326 cell surface binding on WT and KCNQ5 KO Raji cells after 60 s of incubation (top), as well as associated peptide internalization after 1 hr of treatment (bottom). The results correspond to at least five independent experiments.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) TAT-PNA-induced luciferase activity in the indicated cell lines pretreated or not with potassium channel inhibitors (XE-991 or TRAM-34) or genetically invalidated for specific potassium channels. Results are normalized to non-stimulated cells (dashed lines). The independent experiment replicates are color-coded. The p-values correspond to the assessment of the significance of the differences with the control wild-type (WT) condition using ANOVA multiple comparison analysis with Dunnett’s correction. (B) Representative microscopy images of WT and KCNQ5 knock-out (KO) Raji cells expressing loxP-RFP-STOP-loxP-GFP and treated or not with 20 μM TAT-Cre for 48 hr. The results correspond to one of three independent experiments. (C) Internalization, recorded by flow cytometry, of FITC-D-JNKI1 after 1 hr of incubation in the indicated cell lines genetically invalidated (KO) or not (WT) for specific potassium channels. The results correspond to the median of three independent experiments.

These potassium channels were pharmacologically or genetically inactivated (Figure 2B and Figure 2—figure supplement 2A-C) to validate their involvement in the direct translocation of TAT-RasGAP317-326 through the plasma membrane and the resulting death induction. The KCNQ family inhibitor, XE-991 (Schroeder et al., 2000), as well as KCNQ5 genetic invalidation (Figure 2—figure supplement 2A), fully blocked peptide internalization in Raji cells and protected them from the killing activity of the peptide (Figure 2B and Figure 2—figure supplement 2D). SKW6.4 cells individually lacking KCNN4 or KCNK5 (Figure 2—figure supplement 2B), or SKW6.4 cells treated with TRAM-34, a KCNN4 inhibitor (Wulff et al., 2001; Wulff et al., 2000), were impaired in their ability to take up the peptide and were partially protected against its cytotoxic activity (Figure 2B and Figure 2—figure supplement 2D). Inhibition of KCNN4 activity with TRAM-34 in KCNK5 knock-out cells did not further protect the cells against TAT-RasGAP317-326-induced death. In HeLa cells, TRAM-34, but not XE-991, inhibited TAT-RasGAP317-326 internalization and subsequent death (Figure 2B). Thus, in HeLa cells, KCNN4 channels regulate the membrane translocation of the peptide. This was confirmed by knocking out KCNN4 in these cells (Figure 2B and Figure 2—figure supplement 2C). Resistance to TAT-RasGAP317-326-induced death in KCNQ5 knock-out Raji cells and KCNN4 knock-out SKW6.4 or HeLa cells was restored through ectopic expression of the corresponding FLAG- or V5-tagged channels (Figure 2—figure supplement 2E-F), ruling out off-target effects.

We next determined whether vesicular internalization or direct translocation were affected in cells with impaired potassium channel activities. Compared to their respective wild-type controls, the percentage of cells with diffuse cytosolic location of FITC-TAT-RasGAP317-326 was drastically diminished in cells lacking one of the CRISPR/Cas9 screen-identified potassium channels in the respective cell lines (Figure 2C and Figure 2—figure supplement 3A-B). This was mirrored by an increase in the percentage of knock-out cells with vesicular staining. The invalidation of potassium channels did not affect transferrin or dextran internalization into cells (Figure 2—figure supplement 3C) or the infectivity of vesicular stomatitis virus (Torriani et al., 2019), substantiating the non-involvement of these channels in endocytic pathways.

One possibility to explain the above-mentioned results is that the absence of potassium channels reduces peptide binding to cells, thereby hampering subsequent peptide cellular uptake. At a 20 μM concentration, TAT-RasGAP317-326 is readily taken up by wild-type Raji cells but not by KCNQ5 knock-out cells. At this concentration, peptide binding was slightly lower in knock-out than in wild-type cells (Figure 2—figure supplement 3D, upper graph). However, augmenting the peptide concentrations in the extracellular medium of KCNQ5 knock-out cells to reach surface binding signals equivalent or higher than what was obtained in wild-type cells still did not result in peptide cellular internalization unless ≥80 μM of the peptides were used and even in this case, the uptake remained inefficient (Figure 2—figure supplement 3D). Difference in peptide binding is therefore not the cause of the inability of potassium channel knock-out cells to take up TAT-RasGAP317-326.

We then assessed whether the role of potassium channels in cellular internalization also applied to TAT cargos other than RasGAP317-326. TAT-PNA is an oligonucleotide covalently bound to TAT, which can correct a splicing mutation within the luciferase-coding sequence (Abes et al., 2007; Kang et al., 1998). This can only occur if TAT-PNA reaches the cytosol. The luciferase activity triggered by TAT-PNA was diminished in the presence of potassium channel inhibitors and in potassium channel knock-out cell lines (Figure 2—figure supplement 4A). Cytosolic access of TAT-Cre, which can recombine a loxP-RFP-STOP-loxP-GFP (D’Astolfo et al., 2015; Wadia et al., 2004) gene construct, was then assessed. Switch from red to green fluorescence occurs only when TAT-Cre reaches the nucleus. This took place in wild-type Raji cells but not in the KCNQ5 knock-out cells (Figure 2—figure supplement 4B). We finally tested a clinical phase III therapeutic D-JNKI1 compound (Guidotti et al., 2017; Vasconcelos et al., 2013) used in the context of hearing loss and intraocular inflammation. The internalization of this peptide was completely blocked in Raji cells lacking KCNQ5 (Figure 2—figure supplement 4C, left). D-JNKI1 internalization was also diminished in SKW6.4 cells lacking KCNN4 and KCNK5 channels, as well as in HeLa cells lacking the KCNN4 potassium channel (Figure 2—figure supplement 4C, middle and right panels). These data demonstrate that the absence of specific potassium channels diminishes or even blocks the entry of various TAT-bound cargos.

### Potassium channels maintain plasma membrane polarization that is required for cationic CPP entry into cells

Potassium is the main ion involved in setting the plasma membrane potential (Vm). The potassium channels identified in the CRISPR/Cas9 screen may therefore participate in the establishment of an adequate Vm permissive for CPP direct translocation (Chaloin et al., 1998; Henriques et al., 2005; Moghal et al., 2020; Rothbard et al., 2004; Wallbrecher et al., 2017; Zhang et al., 2009). Figure 3A (left graph) shows that genetic disruption or pharmacological inhibition of KCNQ5 in Raji cells led to an increase in their Vm (from –26 to –15 mV, validated with electrophysiological recordings; see Figure 3—figure supplement 1A). Surprisingly, such minimal increase in Vm in the KCNQ5 knock-out Raji cells practically abolished CPP internalization (Figure 3B, left graph), indicating that above a certain threshold, the Vm is no longer permissive for CPP direct translocation. In SKW6.4 and HeLa cells, Vm measurement was much more variable than in Raji cells. Nevertheless, a trend of increased Vm was observed when KCNN4 or KCNK5 were invalidated genetically or pharmacologically (Figure 3A, middle and right graphs) and this was accompanied by reduced peptide uptake (Figure 3B, middle and right graphs). As the CRISPR/Cas9 screens performed in various cell lines identified a variety of potassium channels required for efficient CPP internalization, we conclude that it is the Vm maintenance activity of these channels that is important for CPP direct translocation and not some specific features of the channels.

![Figure 3.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig3-v2.jpg)

**Figure 3.:** (A) Assessment of the resting plasma membrane potential in the indicated wild-type cell lines and the corresponding potassium channel knock-out (KO) clones in the presence or in the absence 10 μM XE-991 or TRAM-34. The gray and white zones correspond to non-treated cells and inhibitor-treated cells, respectively. NT, not treated. The p-values correspond to the assessment of the significance of the differences with the control wild-type condition using ANOVA multiple comparison analysis with Dunnett’s correction. Each dot in a given condition represents an independent experiment. (B) Effect of cellular depolarization (left of the gray zone) and hyperpolarization (right of the gray zone) on peptide internalization in the absence of serum. The indicated cell lines and the corresponding channel KO clones were pretreated or not with depolarization agents (2 μg/ml gramicidin for 5 min or high extracellular potassium buffer for 30 min) or with hyperpolarization inducer (10 μM valinomycin), followed by the addition of TAT-RasGAP317-326 for 1 hr. Alternatively, hyperpolarization was achieved by ectopic expression of the KCNJ2 potassium channel. Membrane potential and peptide internalization were then determined. Membrane potential was measured in the presence of DiBac4(3) by flow cytometry. Peptide internalization was measured by flow cytometry in the presence of 0.2% trypan blue. The p-values correspond to the assessment of the significance of the differences with the control wild-type condition using ANOVA multiple comparison analysis with Dunnett’s correction. Each dot in a given condition represents an independent experiment. Treatment with valinomycin was used in the absence of serum as the latter is expected to interfere with the drug (Rimmele and Chatton, 2014). As shown in Figure 3—figure supplement 5A, removing serum from the culture medium sensitized cells to TAT-RasGAP317-326 and consequently, the CPP concentration had to be adapted accordingly (Figure 3—figure supplement 5B). Serum withdrawal does not affect the Vm (Figure 3—figure supplement 5C). (C) Quantitation of cytosolic CPP signal (top) and the number of endocytic vesicles per cell (bottom) in wild-type HeLa cells (n = 158 cells) incubated for 1 hr with 10 μM FITC-CPP in control, depolarizing (2 μg/ml gramicidin), or hyperpolarizing (10 μM valinomycin) conditions in the absence of serum based on confocal microscopy images (Figure 3—figure supplement 2D). Comparison between different conditions to non-treated control was done using ANOVA test with Dunnett’s correction for multiple comparison. The number of endocytic vesicles per cell was quantitated based on confocal images. Statistical comparison was done using t-tests. Quantitation of vesicles was not performed in hyperpolarizing conditions due to masking from strong cytosolic signal. (D) Modulation of the Vm membrane potential by varying extracellular potassium concentrations. Assessment of membrane potential changes in Raji cells incubated in RPMI medium containing the indicated concentrations of potassium chloride (isotonicity was maintained by adapting the sodium chloride concentrations; see Materials and methods). Membrane potential was measured with DiBac4(3). The results correspond to the median of six independent experiments. (E) Internalization of various CPPs in the presence of different concentrations of potassium chloride in the media. Data for a given experiment are linked with thin blue lines.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Membrane potential measurement validation. Membrane potential of wild-type and KCNQ5 knock-out (KO) Raji cells was measured using DiBac4(3), a fluorescent membrane potential sensor, or by performing perforated patch electrophysiology recordings. Each dot in the figures reporting DiBac4(3) measurements corresponds to the median of 10,000 cells recording. For perforated patch, each dot in the figures corresponds to the membrane potential of one cell. (B) Representative confocal images of wild-type HeLa cells incubated with 80 μM FITC-TAT-RasGAP317-326 for 1 hr in the presence (depolarized) or in the absence (not treated) of 2 μg/ml gramicidin. Scale bar: 10 μm. (C) Effect of ectopic expression of the CRISPR/Cas9-identified potassium channels in wild-type cells and the corresponding KOs (right of the gray zone) on the cell membrane potential and FITC-TAT-RasGAP317-326 internalization in the absence of serum. Cells were incubated with TAT-RasGAP317-326 for 1 hr. Membrane potential was measured using DiBac4(3) by flow cytometry. Peptide internalization was measured by flow cytometry in the presence of 0.2% trypan blue. The p-values correspond to the assessment of the significance of the differences with the control wild-type condition using ANOVA multiple comparison analysis with Dunnett’s correction. (D) Representative confocal images of primary rat cortical neurons (left) and wild-type HeLa cells (right) incubated for 1 hr at 37°C with FITC-TAT-RasGAP317-326 in the absence of serum. To highlight the differential capacity of these cells to take up the CPP in cytosol, a low concentration of TAT-RasGAP317-326 (2 μM) was used here. At higher concentrations, this CPP readily enters HeLa cells (see panel B). Post-incubation cells were washed and imaged with a confocal microscope using the same laser settings for both cell types. Nuclei of HeLa cells were labeled with Hoechst (blue staining). Scale bar: 20 μm.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Sequences of the indicated CPPs and their net charge. Positively charged amino acids (arginine and lysine) are color-coded. (B) Confocal microscopy quantitation of HeLa cells displaying the indicated types of CPP internalization at various concentrations after 30 min of incubation. The results correspond to the average of three independent experiments. We did not observe cells with only cytosolic fluorescence (i.e. without fluorescent endosomes). (C) Confocal microscopy quantitation of HeLa cells displaying the indicated types of CPP internalization. The CPPs (40 μM) were continuously present in the media during the course of the experiment. The results correspond to the average of three independent experiments. (D) Left: Representative confocal images of wild-type HeLa cells incubated with 10 μM of the indicated CPP in the absence of serum in physiological, depolarized (2 μg/ml gramicidin) or hyperpolarized (10 μM valinomycin) conditions. Right: Quantitation of the cell percentage with the indicated FITC-CPP cytosolic signal intensity in depolarized, non-treated, and hyperpolarized conditions. Refer to Figure 3C for the corresponding quantitation of cytosolic fluorescence intensity and number of CPP-positive endocytic vesicles per cell. Scale bar: 10 μm.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Assessment of membrane potential (top) and FITC-TAT-RasGAP317-326 (2 μM) cytosolic uptake after 1 hr (bottom) in control, depolarized, and hyperpolarized primary rat cortical neurons. Depolarization was induced by 30 min pre-incubation with 5 mM tetraethylammonium (TEA), a potassium channel blocker and hyperpolarization was induced by 30 min pre-incubation with 10 μM valinomycin. The membrane potential modulators were present throughout the experiment. Membrane potential measurements were performed with DiBac(4)3 (see Materials and methods section). The results correspond to the median of at least three independent experiments based on confocal images (n = 111 cells).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Assessment of FITC-CPP binding to cellular membranes of wild-type Raji cells in normal or depolarized conditions after 60 s of incubation (top), as well as associated peptide internalization after 1 hr of treatment (bottom). Cells were pre-incubated for 30 min in the presence of RPMI containing 5.2 or 91.9 mM potassium chloride and then treated with 40 μM of the indicated CPPs. The results correspond to at least six independent experiments. Comparison between non-treated or depolarized conditions was done using two-tailed paired t-test.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (A) Quantitation of TAT-RasGAP317-326-induced death in Raji, SKW6.4, and HeLa cells in the presence or in the absence of serum. The results correspond to the median of three independent experiments. This panel shows that serum removal sensitizes cells to TAT-RasGAP317-326. This is in line with previous observations that cationic CPPs interact with proteins present in serum (Kosuge et al., 2008; Ziegler et al., 2005), which results in lower CPP availability in the media. (B) Quantitation of wild-type (WT) and knock-out (KO) cell death after incubation for 16 hr (Raji and SKW6.4) or 24 hr (HeLa) in serum-free RPMI media in the presence of increasing concentrations of TAT-RasGAP317-326. Arrows indicate the chosen peptide concentrations for experiments performed in the absence of serum. The results correspond to the median of three independent experiments. Cytosolic internalization results were very similar between the experiments performed in the presence or in the absence of serum, once the CPP concentrations were adjusted (Figure 3C and Figure 3—figure supplement 2E). (C) Membrane potential measurement in wild-type Raji cells performed in the presence or in the absence of 10% serum. Membrane potential was assessed using DiBac4(3).

If the reason why invalidation of the KCNQ5, KCNN4, and KCNK5 potassium channels inhibits TAT-RasGAP317-326 cellular entry is cell depolarization, a similar response should be obtained by artificially depolarizing cells. Indeed, depolarizing cells with gramicidin (Eisenman et al., 1978) (making non-specific 0.4 nm pores [Kelkar and Chattopadhyay, 2007] in cell membranes) or by increasing the extracellular concentration of potassium (dissipating the potassium gradient) totally blocked cytosolic peptide acquisition into the three studied cell lines (Figure 3B) but not peptide endocytosis (Figure 3—figure supplement 1B). Hence, cellular depolarization in itself inhibits TAT-RasGAP317-326 direct translocation into the cytosol.

Next, we determined whether hyperpolarization could reverse the inability of potassium channel knock-out cells to take up TAT-RasGAP317-326. Cells were either incubated in the presence of valinomycin (Rimmele and Chatton, 2014), which leads to formation of potassium-like channels, or transfected with KCNJ2 channel that also provokes potassium efflux and membrane hyperpolarization (Xue et al., 2014). Figure 3B shows that hyperpolarization of cells lacking CRISPR/Cas9-identified potassium channels fully restored peptide translocation. Moreover, hyperpolarization increased peptide cytosolic acquisition in wild-type cells (Figure 3B). Similar effect, albeit to a lesser extent, was observed by ectopically expressing KCNQ5 in wild-type and KCNN4 knock-out SKW6.4 and HeLa cells as well as by ectopically expressing KCNN4 in wild-type and KCNQ5 knock-out Raji cells (Figure 3—figure supplement 1C). Additionally, cells such as primary rat cortical neurons that naturally have a low Vm (–48 mV) take up the CPP in their cytosol more efficiently than cells with higher Vm such as HeLa cells (–25 mV) (Figure 3—figure supplement 1D). Altogether, these results demonstrate that the Vm modulates internalization of TAT-RasGAP317-326 in various cell lines. This internalization can be manipulated through cellular depolarization to block it and through hyperpolarization to increase it, confirming earlier results obtained for the R8 CPP in Jurkat cells (Rothbard et al., 2004).

We then assessed whether the entry of TAT, nanomeric arginine (R9), and Penetratin (Figure 3—figure supplement 2A), three commonly used cationic CPPs in biology and medicine, was regulated by the plasma membrane potential as shown above for TAT-RasGAP317-326. Similarly to TAT-RasGAP317-326, these CPPs are taken up by HeLa cells by both direct translocation and endocytosis (Figure 3—figure supplement 2B-C). Depolarization, induced by either gramicidin or high extracellular potassium concentrations (Figure 3D), led to decreased cytosolic fluorescence of these CPPs, while valinomycin-mediated hyperpolarization favored their translocation in the cytosol (Figure 3C, upper graphs, Figure 3E, and Figure 3—figure supplement 2D-E). Although the cellular membrane composition of neurons may differ from the other cell lines used in this study, the Vm also controlled peptide translocation in non-transformed rat primary cortical neurons (Figure 3—figure supplement 3). In contrast, depolarization had no impact on the ability of the cells to endocytose these CPPs (Figure 3C, bottom graphs), further confirming that CPP endocytosis is not affected by Vm. Finally, we note that CPP membrane binding was only minimally affected by depolarization (Figure 3—figure supplement 4). Hence, the reason why depolarized cells do no take up CPPs is not a consequence of reduced CPP binding to cells, confirming our earlier observation obtained with TAT-RasGAP317-326 (Figure 2—figure supplement 3D). Altogether the data presented in Figure 3 show that direct translocation of cationic CPPs is modulated by the Vm of cells and that specific potassium channels are involved in this modulation.

### CPP direct translocation modeling

To further study the mechanism of CPP cellular entry through direct translocation, we took advantage of coarse-grained molecular dynamics (MD) technique and MARTINI force field 2.2p (Marrink et al., 2007; Marrink and Tieleman, 2013). In our simulations we have used TAT-RasGAP317-326, TAT, R9 and Penetratin in presence of a natural cell membrane-like composition (for both inner and outer leaflets) while earlier studies have employed simpler membrane composition (Gao et al., 2019; Herce et al., 2009; Lin and Alexander-Katz, 2013; Moghal et al., 2020; Via et al., 2018; Zhang et al., 2009). Membrane hyperpolarization was achieved by setting an ion imbalance (Delemotte et al., 2008; Gao et al., 2019; Gurtovenko and Vattulainen, 2007; Herrera and Pantano, 2009) through a net charge difference of 30 positive ions (corresponding to a Vm of ~2 V) between the intracellular and extracellular spaces. The use of very high Vm values, typically used in computational studies, is required to capture nanosecond occurring events. This protocol (Figure 4—figure supplement 1A) allowed us to observe CPP translocation across membranes within a few tens of nanoseconds (Figure 4A and Video 5). In presence of ~2 V Vm, the CPPs approached the membrane on the extracellular side and this led to the formation of a water column within the membrane that the CPP then used to move to the intracellular space (Video 5). The movement of the positive charges carried by the CPPs, as well as extracellular cations, to the intracellular compartment via the water pore induced membrane depolarization. This depolarization provoked the collapse of the water pore and membrane resealing. Even though CPPs play an active role in their internalization, the mere presence of the CPP in the absence of a sufficiently low Vm was not enough to trigger water pore formation (Figure 4B, right graph and Video 6). These data confirm earlier work describing the role of the Vm in CPP penetration into or through bilipidic membranes (Gao et al., 2019; Herce and Garcia, 2007; Herce et al., 2009; Lin and Alexander-Katz, 2013; Moghal et al., 2020; Via et al., 2018; Zhang et al., 2009). TAT, R9, and Penetratin all translocated into the intracellular compartment but with different propensities (Figure 4B, left graph) and with different kinetics (Figure 4—figure supplement 1B) that appeared to be related to the positive charges they carry (Figure 3—figure supplement 2A): the more positively charged a CPP, the higher probability to translocate across cell membranes and the faster kinetics of water pore formation at a given Vm.

![Figure 4.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig4-v2.jpg)

**Figure 4.:** (A) Visualization of in silico modeled, time-dependent, TAT-RasGAP317-326 penetration and subsequent translocation across cellular membrane through a water pore. Water molecules within membranes are depicted by red spheres (and by red dots outside the membrane). (B) Quantitation of CPP localization in hyperpolarized or depolarized conditions based on coarse-grained molecular dynamics simulations. Membrane hyperpolarization was achieved through a net charge difference of 30 positive ions between intracellular and extracellular space in a double-bilayer system (D’Astolfo et al., 2015, Kang et al., 1998; Kauffman et al., 2018; Kelkar and Chattopadhyay, 2007; Khalil et al., 2018) obtaining a transmembrane potential of –2.2 V. Such low membrane potential was required to visualize translocation within the time frame of the simulations (100 ns). (C) Free energy landscape of R9 translocation reported as a function of CPP-membrane distance. The metadynamics simulations were performed at transmembrane potential values of 0, –80, and –150 mV (black, brown, and green curves). (D) Free energy barrier for CPP translocation at different transmembrane potential values. (E) Electrostatic potential map of a molecular system containing one R9 peptide in contact with the cell membrane, without any applied external electrostatic field.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Schematic depiction of the molecular system used to estimate water pore formation kinetics. The static electric field (Eext) has been highlighted with a green arrow. Water molecules are shown as red structures (small when outside membranes and large when found within membranes). (B) Assessment of the time necessary for water pore formation in the presence or in the absence of the indicated CPPs at 37°C based on in silico pore formation kinetics experiments. To estimate the time needed for CPPs to translocate through membranes at –150 mV, we established the relationship (see fitting function below) between the time of CPP translocation and the Vm in the volt range used during the simulation runs and extrapolated from this relationship the time needed for CPP translocation at a Vm of –150 mV. Even though this extrapolation is likely to lack accuracy because of the well-known limitation of the MARTINI force field in describing the absolute kinetics of the molecular events, the values obtained are consistent with the kinetics of CPP direct translocation observed in living cells (Figures 1B and 2C and Figure 3—figure supplement 2C). Fitting function: t=A0*e(A1*V), where t is the simulation time of water pore formation, V is the transmembrane potential, A0 and A1 the fitting coefficients. The Pearson correlation coefficients of the fitting curves are RR9 = 0.85, RPenetratin = 0.95, RTATRasGAP = 0.91, and RNoCPP = 0.87. (C) Cells can concentrate CPPs in their cytosol. Wild-type Raji and HeLa cells were incubated with 40 μM FITC-TAT-RasGAP317-326 for 1 hr at 37°C in RPMI, 10% fetal bovine serum (FBS). Images were acquired with a confocal microscope. TAT-RasGAP317-326 fluorescence quantitation was performed using ImageJ using region of interest within the cytosol of cells that had acquired the peptide through direct translocation. The dotted line represents the fluorescence in the cell culture media (i.e. outside of the cells).

![Video 5.](https://cdn.elifesciences.org/articles/69832/elife-69832-video5.mp4.jpg)

**Video 5.:** This video shows the translocation of the indicated CPPs across a plasma membrane in the presence of a membrane potential of –2.2 V. This simulation was performed by molecular dynamics MARTINI coarse-grained approach using an asymmetric multi-component bilayer in the presence of ion imbalance to polarize the membrane.

![Video 6.](https://cdn.elifesciences.org/articles/69832/elife-69832-video6.mp4.jpg)

**Video 6.:** This video shows the lack of translocation of the indicated CPPs across a plasma membrane in the absence of a membrane potential (0 V). This simulation was performed by molecular dynamics MARTINI coarse-grained approach using an asymmetric multi-component bilayer in the absence of ion imbalance.

We also applied a metadynamics protocol to estimate the impact of the Vm on the free energy landscape of R9 translocation. The free energy barriers recorded in depolarized membranes (Vm = 0) and polarized membranes (Vm = –80 mV) were similar (Figure 4C–D). The obtained value of about 200 kJ/mol is in line with recent estimation of the free energy barrier associated with CPP translocation at a Vm = 0 (Gao et al., 2019). Only at much lower Vm values (–150 mV) was a marked decrease in free energy barrier recorded. This indicates that hyperpolarization values found in resting cells (down to about –80 mV in neurons and higher in many other cells types; Yang and Brackenbury, 2013) are not more favorable than fully depolarized membranes to establish conditions for the formation of water pores. It appears therefore that cells need to decrease their Vm to much lower values (e.g. –150 mV or lower) to reach conditions compatible with water pore formation. This in silico observation may appear contradictory with our results obtained in live cells showing direct translocation at –25 mV (Figure 2), as well as with the experiment demonstrating that CPP cytosolic internalization was more efficient in cortical neurons in comparison to less negatively charged HeLa cells (Figure 3—figure supplement 1D). We therefore postulate that the presence of CPPs on the cell surface induces locally a substantial voltage drop from the resting Vm. To test this assumption, we analyzed the electrostatic potential map in a molecular system composed of the R9 peptide in contact with the plasma membrane in the absence of an external electrostatic field (Figure 4E). This simulation indicated that the presence of CPPs at the cell surface is sufficient to decrease locally the transmembrane potential to about –150 mV (Figure 4E). This was not observed in the absence of the CPP. In conclusion, our data support a model where CPPs further decrease the Vm of resting cells to very low values (equal to or less than –150 mV) that are compatible with spontaneous water pore formation and that we coin megapolarization.

Our model also predicts that the electric force exerted on CPPs when cells are megapolarized permit CPPs to accumulate in the cytosol and reach concentrations that are higher than in the extracellular milieu. Figure 4—figure supplement 1C shows indeed that cells can concentrate TAT-RasGAP317-326 in the cytosol of Raji and HeLa cells, up to 100 times in extreme cases.

### Structural characterization of the pore allowing CPP entry in live cells

Propidium iodide (PI), with a diameter of 0.8–1.5 nm (Bowman et al., 2010) or fluorophore-labeled 3, 10, and 40 kDa dextrans, with diameters (provided by Thermo Fisher) of 2.3 ± 0.38 (Thorne and Nicholson, 2006), 4.5, and 8.6 nm, respectively (Figure 5—figure supplement 1A), were used to estimate the size of the water pores formed in the presence of CPPs in live cells. These molecules by themselves did not translocate in the cytosol of cells (Figure 5A and Figure 5—figure supplement 1B). They were then co-incubated with different FITC-labeled CPPs and their uptake monitored by confocal microscopy. While PI and CPPs efficiently co-entered cells (Figure 5B and Figure 5—figure supplement 1C-D), there was only marginal co-entry of the dextrans with the CPPs (Figure 5B). The marginal dextran co-entry was inversely correlated with the dextran diameters (inset in Figure 5B): ~2.3-nm-wide dextrans entered cells better than ~4.5-nm-wide dextrans and ~8.6-nm-wide dextrans mostly remained outside cells. The entry of PI and CPPs in cells occurred with identical kinetics (Figure 5—figure supplement 1D), further supporting the notion that they enter cells together. The PI/CPP co-entry was prevented by cell depolarization (Figure 5—figure supplement 1B), which is expected if PI accesses the cytosol via the megapolarization-induced pores used by CPP to enter cells. CPPs do not need to be labeled with a fluorophore to allow PI co-entry into cells (Figure 5B, ‘unlabeled TAT+ PI’ condition), ruling out phototoxicity as a confounding effect. Similar results were obtained in primary rat cortical neurons, where PI cytosolic signal was observed in cells that took up the selected CPPs through direct translocation (Figure 5C). These data are compatible with the notion that water pores triggered by CPPs allow molecules up to ~2 nm in diameter to efficiently enter cells. They are also in line with the in silico prediction of the water pore diameter of 1.6±0.26 nm obtained by analyzing the structure of the pore at the transition state (i.e. when the CPP is crossing the cell membrane; see Figure 4A). Molecules in the 2–5 nm diameter range, such as 3 and 10 kDa dextrans, can still use this entry route to a limited extent. In this context, the Cre recombinase, with a diameter of 5 nm (estimated from its crystal structure; NDB:PD0003), can be transported by TAT into cells (Figure 2—figure supplement 4B), another indication that the pores used by cationic CPPs to enter cells can allow the passage of molecules up to 5 nm.

![Figure 5.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig5-v2.jpg)

**Figure 5.:** (A–B) Quantitation of the percentage of cells with cytosolic staining after the indicated treatment. The indicated compounds (32 μg/ml propidium iodide [PI], 200 μg/ml dextran, 40 μM CPP) were incubated for 30 min with HeLa cells. Depolarization, indicated by an asterisk, was induced with 2 μg/ml gramicidin. The percentage of cells displaying cytosolic internalization of the indicated molecules was then determined on confocal images (n = 207 cells; see the Materials and methods and Figure 5—figure supplement 1C). Inset corresponds to an enlargement of the percentage of cells positive for dextran in the presence of R9. The results correspond to at least three independent experiments. CPPs such as R9 do not bind to PI (Figure 5—figure supplement 2A) and thus PI entry and accumulation within cells was not the result of CPP carry over. (C) Quantitation of the percentage of primary rat cortical neurons with cytosolic staining following incubation for 30 min with the indicated CPPs (2 μM) and PI (32 μg/ml). The percentage of cells displaying cytosolic internalization of the indicated molecules was then determined on confocal images (n = 153 cells), as in panel B. (D) Left graph: quantitation of PI cytosolic internalization in wild-type HeLa cells after 30 min of incubation in normal, depolarizing (2 μg/ml gramicidin) or hyperpolarizing (10 μM valinomycin) conditions in the presence or in the absence of 40 μM FITC-R9. Right graph: as in left graph, but using lower laser power to avoid saturation of the signal obtained in saponin-permeabilized cells. Cytosolic internalization was quantitated from confocal images using ImageJ (n = 319 cells; see Materials and methods). The p-values correspond to the assessment of the significance of the differences with the non- treated (NT) control condition using ANOVA multiple comparison analysis with Dunnett’s correction. The results correspond to three independent experiments. PI staining is commonly used to assess cell membrane integrity, frequently associated with cell death (see for example Figure 2B, lower graphs). This dye poorly fluoresces in solution (Figure 5—figure supplement 2B). However, the PI cytosolic intensity values in dead permeabilized cells are several orders of magnitude higher than those recorded after cell hyperpolarization (compare the left and right graphs in the present panel). (E) Relation between cytosolic PI intensity and membrane potential measured with the DiBac4(3) sensor in HeLa cells. Each dot represents an independent experiment. (F) The fitted curve from panel E was used to calculate membrane potential values based on cytosolic PI intensities in HeLa cells and its corresponding KCNN4 knock-out (KO). These values are those labelled "calculated" in the graph. Those labelled "measured" correspond to the membrane potentials determined via DiBac4(3) uptake. Each dot in a given condition represents an independent experiment.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Structure and dimensions of the molecules used to probe the size of the pore used by CPPs to enter cells. Dextran molecules are fluorescently labeled with Texas Red or TMR. (B–D) HeLa cells were incubated with 32 μg/ml propidium iodide (PI) with or without 40 μM FITC-R9, or left untreated for 30 min at 37°C in RPMI, 10% fetal bovine serum (FBS). Depolarization was induced with 2 μg/ml gramicidin. Images were obtained by confocal microscopy. As shown in Figure 5—figure supplement 2B, the fluorescence produced by 32 μg/ml of PI in solution (i.e. without cells) is under our threshold of detection. The observed fluorescence dots and signal in cells incubated with this PI concentration correspond therefore to cell autofluorescence and not PI fluorescence (compare images i and ii in panel B). Hence, when PI fluorescence is detected in cells (see the examples in panel C or D), the corresponding PI concentration is higher than 32 μg/ml (Figure 5—figure supplement 2B). In other words, cellular PI fluorescence is detected because cells are able to concentrate this cationic dye in their cytosol, as they are able to do with cationic CPPs (Figure 4—figure supplement 1C). (B) PI does neither enter live cells by itself (left images), nor does it enter depolarized cells, whether CPPs (here R9) are present or not (middle images). The fluorescent signal from FITC-labeled CPPs is not detected in the channel used to record PI fluorescence. In other words, the signal recorded as PI does not come from FITC fluorescence leaking into the PI channel (right images). (C) Criteria used for the visual scoring performed in Figure 5 in HeLa cells. The percentage of cells positive for PI and cells that have acquired FITC-R9 through direct translocation were assessed based on the following criteria. Cells 1, 3–6 are considered as positive for PI (left) and cells 1–6 are counted as those where direct translocation has occurred (right). The rest of the cells were considered as negative. Scale bar: 20 μm. (D) Kinetics of FITC-CPP and PI uptake. Images were acquired over time with a confocal microscope and cytosolic fluorescence was quantitated using ImageJ similarly to what is shown in Figure 1—figure supplement 2D.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) PI does not interact with R9. The potential binding between PI (6 mM) and R9 (0.6 mM) at 37°C was assessed by isothermal titration calorimetry. Representative power and heat of injection are shown. This experiment was repeated three times with similar results. (B) PI fluorescence detection in media in the absence of cells. Wells containing the indicated PI concentrations in RPMI were illuminated using the same settings as in Figure 5B and C, left panel. Fluorescence intensity within the full field of the acquired images was quantitated using ImageJ. The arrow indicates the PI concentration used for water pore-related experiments (32 μg/ml). (C) Assessment of colony formation potential after transient cell-penetrating peptide (CPP) and membrane potential treatments. DMSO was used as a vehicle for gramicidin and valinomycin. HeLa cells were incubated for 1 hr with the indicated treatment, washed, and plated on 10 cm dishes. Number of colonies were counted after 14 days in culture after Giemsa staining. These data indicate that cell viability is not affected by transient treatment with the indicated CPPs, Vm modulating agents, and PI. The results obtained in cells incubated with CPPs further show that water pore formation does not compromise cell survival.

Despite identical net positive charges (Figure 3—figure supplement 2A), and as reported earlier (Mitchell et al., 2000), the K9 peptide made of nine lysine residues was less capable of translocating into cells compared to R9 (Figure 5B and Figure 3—figure supplement 2C, right graph). This may be due to the deprotonation of K9 once in the plasma membrane (see Discussion). However, in the few cases when cells have taken up K9, PI co-internalized as well (middle graph of Figure 5B). This indicates that K9 has a reduced capacity compared to R9 to trigger water pore formation but when they do, PI can efficiently translocate through the pores created by K9.

Modeling experiments indicate that water pores are created in membranes subjected to sufficiently high (absolute values) Vm. We therefore tested whether the mere hyperpolarization of cells (i.e. in the absence of CPPs) could trigger the translocation of PI into cells, indicative of water pore formation. Figure 5D (left) shows that the hyperpolarizing drug valinomycin significantly increased PI cell permeability. In contrast, depolarization, mediated by gramicidin, reduced PI internalization (Figure 5D, left). Cells incubated with CPPs took up PI in their cytosol to a much greater extent than when cells were treated with valinomycin (Figure 5D, left), as expected if CPPs participate in setting plasma membrane megapolarization.

Figure 5E shows the correlation between cytosolic PI accumulation over time and Vm. Based on this correlation, we estimated the Vm of cells incubated with a CPP to be in the order of –150 mV (Figure 5F). In accordance with the modeling experiments, these data further support the notion (i) that water pore formation in cells is favored by cell hyperpolarization and inhibited by depolarization and (ii) that CPPs themselves (Rao et al., 2014; Wallbrecher et al., 2017) further contribute to the establishment of local megapolarization in the plasma membrane.

### Megapolarization improves CPP internalization in vivo

We investigated whether it was possible to experimentally manipulate the Vm to favor CPP internalization in in vivo situations. Systemic exposure of zebrafish embryos to valinomycin in Egg water led to cell hyperpolarization (Figure 6—figure supplement 1A) and improved internalization of a TAT-based CPP (Figure 6—figure supplement 1B). This systemic treatment, while not acutely toxic, halted development (Figure 6—figure supplement 1C-E). However, local valinomycin injection did not affect long-term viability (Figure 6—figure supplement 1F) and efficiently increased CPP cellular internalization (Figure 6A). Subcutaneous injections of valinomycin in mice induced tissue hyperpolarization (Figure 6—figure supplement 1G) and boosted the CPP delivery in skin cells (Figure 6B). These results demonstrate that hyperpolarizing drugs can be used to ameliorate CPP internalization in animal tissues.

![Figure 6.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig6-v2.jpg)

**Figure 6.:** (A) CPP internalization in zebrafish embryos in normal and hyperpolarized conditions. Forty-eight-hour post fertilization, zebrafish embryos were injected with 3.12 μM FITC-TAT-RasGAP317-326(W317A) with or without 10 μM valinomycin. Scale bar: 200 μm. The results correspond to three independent experiments. (B) CPP internalization in C57BL/6 N mice in normal and hyperpolarized conditions. Mice were injected with 5 μM FITC-TAT-RasGAP317-326(W317A) with or without 10 μM valinomycin (n = 11 injections per condition). In both panels, the p-values associated with the comparisons of the ‘CPP’ and ‘CPP + valinomycin’ conditions were calculated using two-tailed paired t-tests.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Eighteen hours post fertilization zebrafish embryos were incubated for 40 min with the indicated concentrations of valinomycin and 950 nM DiBac4(3). DiBac4(3) fluorescence was then recorded and normalized to the non-treated control. The decrease in DiBac4(3) fluorescence indicates membrane hyperpolarization. Membrane potential values could not be calculated, as a standard curve would have to be performed in zebrafish. DiBac4(3) internalization was assessed from confocal images of the fish tail region. (B) Eighteen hours post fertilization, zebrafish embryos were incubated with or without 3.12 μM TAT-RasGAP317-326 (W317A), a mutant version that is not toxic to cells, in the presence of the indicated concentrations of valinomycin. Peptide internalization was assessed from confocal images of the fish tail region. (C–D) Eighteen hours post fertilization, zebrafish embryos were incubated 1 hr with the indicated concentrations of valinomycin, in the absence (panel C) or in the presence (panel D) of 3.12 μM TAT-RasGAP317-326 (W317A), then washed, and incubated in Egg water. The viability of each fish was assessed over 52 hr at the indicated time points. (E) Representative images of zebrafish treated as described in panels C and D, washed, and further incubated in Egg water. Images were taken with a CYTATION3 apparatus at a 4× magnification at 70 hr post fertilization (hpf). (F) Survival of 48 hr post fertilization zebrafish embryos following intramuscular injection of 3.12 μM TAT-RasGAP317-326 (W317A) peptide in the presence or in the absence of 10 μM valinomycin. Survival was visually assessed under a binocular microscope by taking into consideration the embryo transparency (as dead embryos appear opaque), development characteristics, and motility. (G) Mice were intradermally injected with DiBac4(3) in the presence or in the absence of 10 μM valinomycin. DiBac4(3) fluorescence was then recorded and normalized to the mean of non-treated (NT) control. DiBac4(3) fluorescence was assessed as in panel A.

## Discussion

Multiple models, mostly inferred from artificial experimental paradigms, have been proposed to explain CPP direct translocation. These include the formation of pores made of the CPPs themselves that they use for their own entry, the formation of inverted micelles in the plasma membrane that translocate the CPPs, or diffusion of the CPPs across the plasma membrane (Bechara and Sagan, 2013; Futaki et al., 2013; Guidotti et al., 2017; Koren and Torchilin, 2012; Trabulo et al., 2010). Our simulation and cellular data, while providing no evidence for such models, demonstrate that CPP cellular internalization is potassium channel- and Vm-dependent in vitro and in vivo. Potassium channels are required to establish a basal low Vm, subsequently permissive for CPP direct translocation. Hyperpolarizing drugs, such as valinomycin, enhance permissiveness. When CPPs come into contact with the plasma membrane, they decrease even more the Vm, resulting in a locally megapolarized membrane. This increases the likelihood of water pore formation that the CPPs then use to penetrate into cells according to their electrochemical gradient (Figure 7). Water pores are created by a combination of lipid head group reorientation coupled to intrusion of a column of water in the membrane bilayer. Water movement plays therefore an active role in the formation of the pore and is not merely occurring once the pores are formed. The movement of the positive charges carried by the CPPs into the cell, as well as the transport of extracellular cations (e.g. Na+), dissipates the Vm, resulting in the collapse of the water pores and sealing of the plasma membrane. CPP-mediated formation of water pores is therefore transient and does not affect cell viability. Multiple rounds of CPP-driven water pore formation and CPP translocation into cells can lead to intracellular accumulation of the CPP to concentrations higher than found outside cells (Figure 4—figure supplement 1C).

![Figure 7.](https://cdn.elifesciences.org/articles/69832/elife-69832-fig7-v2.jpg)

**Figure 7.:** Cationic CPP translocation across cellular membranes is favored by the opening of potassium channels or by hyperpolarizing drugs, such as valinomycin. This sets a sufficiently low membrane potential permissive for CPP direct translocation. When cationic CPPs bind to these already polarized membranes, they induce megapolarization (i.e. a membrane potential estimated to be –150 mV or lower). This leads to the formation of water pores that are then used by CPPs to enter cells.

It has not been possible to measure directly the precise values of the Vm that allow the formation of water pores used by CPPs to enter cells. Using an indirect calculation mode based on the uptake of PI alongside CPPs, we have estimated that a Vm in the order of –150 mV is required for water pores to be formed (Figure 5F). This might be an underestimation however as modeling data indicate that, at –150 mV, the free energy barrier, while being markedly diminished compared to those calculated at –80 or 0 mV, is not fully abrogated (Figure 4D). Possibly therefore, the local Vm where CPPs interact with the plasma membranes is much lower than –150 mV and/or changes in CPP structures occur (e.g. refolding, aggregation) leading to further reduction in free energy barrier.

It is worth mentioning that the applied coarse-grained MARTINI force field, as any other model, has a number of known limitations (Marrink et al., 2019; Marrink and Tieleman, 2013) such as the chemical and spatial resolution, which are both limited compared to atomistic models. There is also a shifted balance between entropy and enthalpy due to the reduced number of degrees of freedom. Moreover, the secondary structure is an input parameter of the model, which implies that secondary structure elements remain fixed during the simulation (Monticelli et al., 2008). However, the coarse-grained approach has provided reliable results in the context of protein-membrane interactions and peptide translocation (Castillo et al., 2013; Koch et al., 2019; Marrink et al., 2003; Monticelli et al., 2008; Monticelli et al., 2010; Periole et al., 2009; Periole et al., 2007; Ramadurai et al., 2010; Yesylevskyy et al., 2010). Moreover, the ability of MARTINI coarse-grained force field to model realistic and heterogeneous membranes has been repeatedly reported in literature, as summarized in a recent review paper (Marrink et al., 2019).

Our model posits that the number of positively charged amino acids influence the ability of CPPs to hyperpolarize cells and hence to form water pores that they take to translocate into cells. CPP hydropathy strongly correlates with penetration of water molecules in the lipid bilayer, thus supporting the hypothesis that the amount of water each CPP can route inside the membrane is modulated by the hydrophobic and hydrophilic character of the peptide (Grasso et al., 2018). The nature of cationic amino acids in peptides determines their translocation abilities. It is known for example that peptides made of nine lysines (K9) poorly reaches the cytosol (Figure 5B and Figure 3—figure supplement 2C) and that replacing arginine by lysine in Penetratin significantly diminishes its internalization (Amand et al., 2012; Mitchell et al., 2000). According to our model, K9 should induce megapolarization and formation of water pores that should then allow their translocation into cells. However, it has been determined that, once embedded into membranes, lysine residues tend to lose protons (Armstrong et al., 2016; Li et al., 2013; MacCallum et al., 2008). This will thus dissipate the strong membrane potential required for the formation of water pores and prevent lysine-containing CPPs to cross the membrane. In contrast, arginine residues are not deprotonated in membranes and water pores can therefore be maintained allowing the arginine-rich CPPs to be taken up by cells. This phenomenon was not modeled in our coarse-grained in silico simulations because the protonation state was fixed at the beginning of the simulation runs and was not allowed to evolve. An additional potential explanation for the internalization differences observed between arginine- and lysine-rich peptides is that even though both arginine and lysine are basic amino acids, they differ in their ability to form hydrogen bonds, the guanidinium group of arginine being able to form two hydrogen bonds (Fromm et al., 1995) while the lysyl group of lysine can only form one. Compared to lysine, arginine would therefore form more stable electrostatic interactions with the plasma membrane. According to previously published studies (Kosuge et al., 2008; Mitchell et al., 2000), the optimal length of consecutive arginine residues appears to be between 9 and 16 amino acids, resulting in optimal CPP cytosolic acquisition. Shorter and longer peptides have decreased internalization efficiencies. The role of the Vm presented in our model is consistent with the reduced uptake of short polyarginine peptides but the Vm parameter of our model cannot explain why longer polyarginine peptides are less efficiently taken up by cells. Our work however also indicates that the water pores created by megapolarization have a diameter of about 2 (–5) nm. Molecules larger than 2 nm are therefore less efficiently transported through these water pores and if polyarginine peptides reach that size their internalization will be hindered. The efficiency of direct translocation of peptides is therefore likely modulated by their sizes, the secondary structures they adopt, and the number of positive charges they carry.

Cationic residues are not the only determinant in CPP direct translocation. The presence of tryptophan residues also plays important roles in the ability of CPPs to cross cellular membranes. This can be inferred from the observation that Penetratin, despite only bearing three arginine residues, can penetrate cells with similar propensities compared to R9 or TAT that contain 9 and 8 arginine residues, respectively. The aromatic characteristics of tryptophan is not sufficient to explain how it favors direct translocation as replacing tryptophan with the aromatic amino acid phenylalanine decreases the translocation potency of the RW9 (RRWWRRWRR) CPP (Derossi et al., 1994). Rather, differences in the direct translocation promoting activities of tryptophan and phenylalanine residues may come from the higher lipid bilayer insertion capability of tryptophan compared to phenylalanine (Christiaens et al., 2002; Jobin et al., 2015; MacCallum et al., 2008). There is a certain degree of interchangeability between arginine and tryptophan residues as demonstrated by the fact that replacing up to four arginine residues with tryptophan amino acids in the R9 CPP preserves its ability to enter cells (Walrant et al., 2020). Therefore, despite the importance of the membrane potential for CPP direct translocation into cells, other factors also appear to play a role in this process.

While the nature of the CPPs likely dictate their uptake efficiency as discussed in the previous paragraph, the composition of the plasma membrane could also modulate how CPPs translocate into cells. In the present work, we have recorded CPP direct translocation in transformed or cancerous cell lines as well as in primary cells. These cells display various abilities to take up CPPs by direct translocation and the present work indicates that this is modulated by their Vm. But as cancer cells display abnormal plasma membrane composition (Szlasa et al., 2020), it will be of interest in the future to determine how important this is for their capacity to take up CPPs.

We propose, based on the work described here, that hyperpolarization induced by drugs such as valinomycin represents a simple alternative or parallel approach to optimize CPP internalization. However, hyperpolarizing drugs may be toxic when systemically applied. For example, valinomycin at the concentrations used to induce hyperpolarization (10 μM) would be lethal if systemically injected in mice (LD50 in the low micromolar range; Daoud and Juliano, 1986). On the other hand, local administration of valinomycin is far less toxic (Gad et al., 1985; Waksman, 1953) as confirmed here in zebrafish and mice. Hyperpolarizing agents may therefore be preferentially used for local or topical applications, which is incidentally the case for the clinically approved CPPs (Abes et al., 2007; Abraham et al., 2015).

Strategies to improve CPP delivery are becoming increasingly elaborate through the use of nanoparticles (Bansal et al., 2018), double-coated nanoparticles (Khalil et al., 2018), liposome-polycation-DNA complexes (Wu et al., 2018), branched peptides (Jeong et al., 2016), etc. Our molecular characterization of the process of CPP direct translocation can be taken advantage of to (i) improve or optimize ‘old’ CPPs, (ii) design new CPPs, (iii) help explain the behavior of newly discovered CPPs (Du et al., 2011; Kauffman et al., 2018; Yin et al., 2009), (iv) discriminate between target cells and cells that should be left unaffected based on Vm, and (v) distinguish between direct translocation and endosomal escape. The present work indicates that the impact on megapolarization should be evaluated when chemical modifications are performed on cationic CPPs to augment their delivery capacities.

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
      <td>Antibody</td>
      <td>Anti-V5(rabbit polyclonal)</td>
      <td>Bethyl</td>
      <td>Cat#A190-A120</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-FLAG(Mouse monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#F1804</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Actin(Rabbit monoclonal)</td>
      <td>Cell Signaling</td>
      <td>Cat#4970</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-α-Tubulin(Rat monoclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat#sc-51715</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Puromycin</td>
      <td>Thermo Fisher</td>
      <td>Cat#A11138-002</td>
      <td>10 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Blasticidin</td>
      <td>Applichem</td>
      <td>Cat#A3784</td>
      <td>10 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>XE-991</td>
      <td>Alomone Labs</td>
      <td>Cat#X-100</td>
      <td>10 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRAM-34</td>
      <td>Alomone Labs</td>
      <td>Cat#T-105</td>
      <td>10 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hoechst 3342</td>
      <td>Thermo Fisher</td>
      <td>Cat#H21492</td>
      <td>10 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trypan Blue 0.4%</td>
      <td>Life Technologies</td>
      <td>Cat#1520061</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>AlexaFluor488-Transferrin</td>
      <td>Thermo Fisher</td>
      <td>Cat#13342</td>
      <td>20 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TexasRed-Dextran 3000</td>
      <td>Thermo Fisher</td>
      <td>Cat#D3329</td>
      <td>200 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TMR-Dextran 10000</td>
      <td>Thermo Fisher</td>
      <td>Cat#D1816</td>
      <td>200 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TexasRed-Dextran 40000</td>
      <td>Thermo Fisher</td>
      <td>Cat#D1829</td>
      <td>200 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Valinomycin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#V0627</td>
      <td>10 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gamicidin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#G5002</td>
      <td>2 μg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tetraethylammonium</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#T2265</td>
      <td>5 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Propidium Iodide</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#81845</td>
      <td>32 μg/ml PI</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DiBac4(3)</td>
      <td>Thermo Fisher</td>
      <td>Cat#B438</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Saponin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#4706</td>
      <td>0.1%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Restriction enzyme: BamHI</td>
      <td>New England Biolabs</td>
      <td>Cat#R313614</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Restriction enzyme: XmaI</td>
      <td>New England Biolabs</td>
      <td>Cat#0180S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Restriction enzyme: XhoI</td>
      <td>New England Biolabs</td>
      <td>Cat#R0146L</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Restriction enzyme: HindIII</td>
      <td>Promega</td>
      <td>Cat#R6041</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>TAT-RasGAP317-326</td>
      <td>Biochemistry Department, University of Lausanne</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>TAT-RasGAP317-326</td>
      <td>SBS Genetech</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>TAT-RasGAP317-326</td>
      <td>Creative Peptides</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-TAT-RasGAP317-326</td>
      <td>Biochemistry Department, University of Lausanne</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-TAT-RasGAP317-326</td>
      <td>Creative Peptides</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-TAT-RasGAP317-326</td>
      <td>SBS Genetech</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>TMR-TAT-RasGAP317-326</td>
      <td>Creative Peptides</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-TAT-RasGAP317-326(W317A)</td>
      <td>Creative Peptides</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-TAT</td>
      <td>SBS Genetech</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>TAT</td>
      <td>SBS Genetech</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-R9</td>
      <td>Biochemistry Department, University of Lausanne</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-Penetratin</td>
      <td>Biochemistry Department, University of Lausanne</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-MAP</td>
      <td>Biochemistry Department, University of Lausanne</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-Transportan</td>
      <td>Biochemistry Department, University of Lausanne</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-D-JNKI1</td>
      <td>SBS Genetech</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FITC-K9</td>
      <td>SBS Genetech</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TA cloning</td>
      <td>Thermo Fisher</td>
      <td>Cat#K202020</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QuikChange II XL Site-Directed Mutagenesis Kit</td>
      <td>Aligent</td>
      <td>Cat#200522</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Dual-Luciferase Reporter Assay</td>
      <td>Promega</td>
      <td>Cat#E1910</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Raji</td>
      <td>Laboratory of Aimable Nahimana</td>
      <td>CCL-86 (ATCC)</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>SKW6.4</td>
      <td>Laboratory of Pascal Schneider</td>
      <td>TIB-215 (ATCC)</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HeLa</td>
      <td>ATCC</td>
      <td>CCL-2</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>C57BL/6NCrl</td>
      <td>Charles River Laboratories</td>
      <td>C57BL/6NCrl</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Sprague-Dawley rat)</td>
      <td>Sprague-Dawley</td>
      <td>Janvier Laboratories</td>
      <td>Sprague-Dawley</td>
      <td></td>
    </tr>
    <tr>
      <td>Experimental Models (Danio rerio)</td>
      <td>AB line</td>
      <td>European Zebrafish Resource Center</td>
      <td>Cat#1175</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: PCR amplification of FLAG-hKCNQ5 from pShuttlw-FLAG-hKCNQ5(G278S)-IRES-hrGFP2 Forward:</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CATCGGGATCCGCTATACCGGCCACCATGGATTACAAGGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: PCR amplification of FLAG-hKCNQ5 from pShuttlw-FLAG-hKCNQ5(G278S)-IRES-hrGFP2 Reverse:</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CATCGCCCGGGGCTATACCGTACCGTCGACTGCAGAATTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: introducing silent mutations in FLAG-hKCNQ5(G278S)-IRES-Neo Forward:</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AAA TAA GAA CCA AAA ATC CTA TGT ACC ATG CCG TTA TCA GCT CCT TGC TGT GAG CAT AAA CCA CTG AAC CCA G</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: introducing silent mutations in FLAG-hKCNQ5(G278S)-IRES-Neo Reverse:</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTG GGT TCA GTG GTT TAT GCT CAC AGC AAG GAG CTG ATA ACG GCA TGG TAC ATA GGA TTT TTG GTT CTT ATT T</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: reverting G278S mutation in FLAG-hKCNQ5(SM, G278S)-IRES-Neo Forward:</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TTT TGT CTC CAT AGC CAA TAG TTG TCA ATG TAA TTG TGC CCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: reverting G278S mutation in FLAG-hKCNQ5(SM, G278S)-IRES-Neo Reverse:</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGG GCA CAA TTA CAT TGA CAA CTA TTG GCT ATG GAG ACA AAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>sgRNA targeting KCNQ5, KCNN4 and KCNK5, see Supplementary file 5</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: first PCR to amplify the lentiCRISPR sgRNA region Forward:</td>
      <td>Shalem et al., 2014</td>
      <td>PCR primers</td>
      <td>AATGGACTATCATATGCTTACCGTAACTTGAAAGTATTTCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primer: first PCR to amplify the lentiCRISPR sgRNA region Reverse:</td>
      <td>Shalem et al., 2014</td>
      <td>PCR primers</td>
      <td>CTTTAGTTTGTATGTCTGTTGCTATTATGTCTACTATTCTTTCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Primers used during the second PCR to attach Illumina adaptors with barcodes, see Supplementary file 4</td>
      <td>Shalem et al., 2014</td>
      <td>PCR primers</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid:hKCNN4-V5.lti</td>
      <td>DNASU</td>
      <td>HsCD00441560</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: hKCNK5-FLAG.dn3</td>
      <td>GenScript</td>
      <td>OHu13506</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: Myc-mKCNJ2-T2A-IRES-tdTomato.lti</td>
      <td>Xue et al., 2014</td>
      <td>Addgene Plasmid #60598</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: LeGo-iT2</td>
      <td>Weber et al., 2008</td>
      <td>Addgene Plasmid #27343</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: pMD2.G</td>
      <td>Didier Trono Laboratory</td>
      <td>Addgene Plasmid #12259</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: psPAX2</td>
      <td>Didier Trono Laboratory</td>
      <td>Addgene Plasmid #12260</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: FLAG-hKCNQ5(G278S)-IHRES-NeoR</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: pShuttle-FLAG-hKCNQ5(G278S)-IRES-hrGFP2</td>
      <td>Kenneth L Byron Laboratory</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: TRIP-PGK-IRES-Neo</td>
      <td>Didier Trono Laboratory</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: FLAG-hKCNQ5(SM,G278S)-IRES-Neo</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: FLAG-hKCNQ5(SM)-IRES-Neo</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid:pLUC705</td>
      <td>Bin Yang Laboratory</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: LeGo-iG2</td>
      <td>Weber et al., 2008</td>
      <td>Addgene Plasmid #27341</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: pLUC705.LeGo-iG2</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: pTAT-Cre</td>
      <td>Wadia et al., 2004</td>
      <td>Addgene Plasmid #35619</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: Cre-reporter.lti</td>
      <td>D’Astolfo et al., 2015</td>
      <td>Addgene Plasmid #62732</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: GeCKO v2 library</td>
      <td>Shalem et al., 2014</td>
      <td>Addgene Plasmid #1000000049</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>Schneider et al., 2012</td>
      <td>https://imagej.nih.gov/ij/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zeiss Zen Lite 2.3</td>
      <td>Carl Zeiss Microscopy GmbH</td>
      <td>https://www.zeiss.fr/microscopie/produits/microscope-software/zen-lite.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MultiClamp 2.2.0</td>
      <td>Axon MultiClamp (Molecular Devices)</td>
      <td>http://mdc.custhelp.com/app/answers/detail/a_id/18877/~/axon%E2%84%A2-multiclamp%E2%84%A2-commander-software-download-page</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clampfit 10.7.0</td>
      <td>Axon pCLAMP (Molecular Devices)</td>
      <td>http://mdc.custhelp.com/app/answers/detail/a_id/18779/~/axon%E2%84%A2pclamp%E2%84%A2-10-electrophysiology-data-acquisition-%26-analysis-software-download</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Kaluza 1.3</td>
      <td>Beckman Coulter</td>
      <td>https://www.beckman.ch/flow-cytometry/software/kaluza</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Gen5.2.5</td>
      <td>BioTek Instruments</td>
      <td>https://www.biotek.com/products/software-robotics-software/gen5-microplate-reader-and-imager-software/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GloMax</td>
      <td>Promega</td>
      <td>https://ch.promega.com/resources/software-firmware/detection-instruments-software/promega-branded-instruments/glomax-96-microplate-luminometer/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism8</td>
      <td>GraphPad</td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MicroCal ITC200</td>
      <td>Malvern Panalytical</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clone Manager9</td>
      <td>Sci-Ed Software</td>
      <td>https://www.scied.com/dl_cm10.htm</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Li-Cor Odyssey</td>
      <td>LI-COR Biosciences</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GROMACS 2018.3</td>
      <td>http://www.gromacs.org/Downloads</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>VISUAL MOLECULAR DYNAMICS (VMD)</td>
      <td>https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XMGRACE 5.1</td>
      <td>http://plasma-gate.weizmann.ac.il/Grace/</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PEP-FOLD SERVER</td>
      <td>http://mobyle.rpbs.univ-paris-diderot.fr/cgi-bin/portal.py#forms::PEP-FOLD</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>RPMI-like media without KCl and NaCl</td>
      <td>Biowest</td>
      <td>N/A</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Chemicals

Puromycin 10 mg/ml (Thermo Fisher, ref no. A11138-02) was aliquoted and stored at –20°C. Blasticidin (Applichem, ref no. A3784) was dissolved at 1 mg/ml in water and stored at –20°C. XE-991 and TRAM-34 (Alomone Labs, ref no. X-100 and T-105, respectively) was dissolved in DMSO at 100 mM and stored at –20°C. Cells were pre-incubated with 10 μM of these inhibitors for 30 min and then kept throughout the experiments. Live Hoechst 33342 (Sigma, ref no. CDS023389) was aliquoted and stored at –20°C. Trypan Blue 0.4% (Life Technologies, ref no. 15250061) was stored at room temperature. AlexaFluor488-labeled human transferrin was dissolved in PBS at 5 mg/ml and stored at 4°C (Thermo Fisher, ref no. 13342). TexasRed-labeled neutral 3000 and 40,000 Da dextran was dissolved in PBS at 10 mg/ml and stored at –20°C (Thermo Fisher, ref no. D3329 and D1829, respectively). TMR-labeled 10,000 neutral dextran was dissolved in PBS at 10 mg/ml and stored at –20°C (Thermo Fisher, ref no. D1816).

### Antibodies

The rabbit polyclonal anti-V5 (Bethyl, ref no. A190-A120), mouse monoclonal anti-FLAG antibody was from Sigma-Aldrich (ref no. F1804), rabbit monoclonal anti-actin (Cell Signaling, ref no. 4970), and rat monoclonal anti-γ-tubulin (Santa Cruz, ref no. sc-51715) antibodies were used for Western blotting.

### Cell lines

All cell lines were culture in 5% CO2 at 37°C. Raji (kind gift from the laboratory of Aimable Nahimana, ATCC: CCL-86), SKW6.4 (kind gift from the laboratory of Pascal Schneider, ATCC: TIB-215), and HeLa (ATCC: CCL-2) cells were cultured in RPMI (Invitrogen, ref no. 61870) supplemented with 10% heat-inactivated FBS (Invitrogen, ref no. 10270–106). HEK293T cells (ATCC: CRL-3216) were cultured in DMEM supplemented with 10% FBS and were used here only for lentiviral production. All cell lines were mycoplasma-negative and authenticated via Microsynth cell authentication service. Unless, otherwise indicated, experiments were performed in RPMI with 10% FBS.

### Zebrafish

Zebrafish (Danio rerio) from AB line were bred and maintained in our animal facility under standard conditions (Marrink et al., 2019), more specifically at 28.5°C and on a 14:10 hr light:dark cycle at the Zebrafish facility of the Faculty of Biology and Medicine, University of Lausanne (cantonal veterinary approval VD-H21). Zebrafish of 20 hr post fertilization were collected and treated with 0.2 mM phenylthiourea (Sigma, St Louis, MO) to suppress pigmentation. Embryos were raised at 28.5°C in Egg water (0.3 g sea salt/l reverse osmosis water) up to 4 days post fertilization.

### Mice

C57BL/6NCrl were acquired from Charles River laboratories, which were then housed and bred in our animal facility. All experiments were performed according to the principles of laboratory animal care and Swiss legislation under ethical approval (Swiss Animal Protection Ordinance; permit number VD3374.a).

### Primary cortical neuronal culture

Sprague-Dawley rat pups (from Janvier, France) were euthanized in accordance with the Swiss Laws for the protection of animals, and the procedures were approved by the Vaud Cantonal Veterinary Office (permit number VD1407.9). Primary neuronal cultures from cortices of 2-day-old rats were prepared and maintained at 37°C with a 5% CO2-containing atmosphere in neurobasal medium (Life Technologies, 21103–049) supplemented with 2% B27 (Invitrogen, 17504044), 0.5 mM glutamine (Sigma, G7513), and 100 μg/ml penicillin-streptomycin (Invitrogen, 15140122) as described previously (Vaslin et al., 2007). Neurons were plated at a density of ~3 × 105 cells on 12 mm glass coverslips coated with 0.01% poly-L-lysine (Sigma, P4832). Half of the medium was changed every 3–4 days and experiments were performed at 12–13 days in vitro.

### Confocal microscopy

Confocal microscopy experiments were done on live 300,000 cells. Cells were seeded for 16 hr onto glass bottom culture dishes (MatTek, corporation ref no. P35G-1.5–14C) in 2 ml RPMI, 10% FBS and treated as described in the figures in 1 ml media, 10% FBS. For nuclear staining, 10 μg/ml live Hoechst 33342 (Molecular Probes, ref no. H21492) was added in the culture medium 5 min before washing cells twice with PBS. After washing, cells were examined with a plan Apochromat 63× oil immersion objective mounted on a Zeiss LSM 780 laser scanning fluorescence confocal microscope equipped with gallium arsenide phosphide detectors and three lasers (a 405 nm diode laser, a 458-476-488-514 nm argon laser, and a 561 nm diode-pumped solid-state laser). Time-lapse experiments were done using an incubation chamber set at 37°C, 5% CO2 and visualized with a Zeiss LSM710 Quasar laser scanning fluorescence confocal microscope equipped with either Neofluar 63×, 1.2 numerical aperture (NA) or plan Neofluar 100×, 1.3 NA plan oil immersion objective (and the same lasers as above). Visual segregation of cells based on types of CPP entry, associated with either vesicular or diffuse cytosolic staining, was performed as shown in Figure 1—figure supplement 1A. Cell images were acquired at a focal plane near the middle of the cell making sure that nuclei were visible. Image acquisition was performed using identical settings for the data presented in a given panel and the related supplementary information.

### Flow cytometry

Flow cytometry experiments were performed using a Beckman Coulter FC500 instrument. Cells were centrifuged and resuspended in PBS prior to flow cytometry. Data analysis was done with Kaluza Version 1.3 software (Beckman Coulter).

### Cell death and CPP internalization measurements

With the exception of neurons, cell death was quantitated with 8 μg/ml PI (Sigma, ref no. 81845). Unless otherwise indicated, cell death was assessed after 16 hr of continuous incubation in Raji and SKW6.4 cells and 24 hr in HeLa cells. Prior to treatment, 300,000 cells were seeded in six-well plates for 16 hr in 2 ml media, 10% FBS. Treatment was done in 1 ml media with 10% FBS. Cell death and peptide internalization were analyzed by flow cytometry. Internalization measurements were done after 1 hr of incubation. Peptide internalization in primary cortical neurons was assessed by confocal microscopy. Cell-associated fluorescence was quantitated with ImageJ. When cytosolic fluorescent was recorded with ImageJ, the regions of interest that were analyzed were chosen so as not to contain labeled endosomes (Figure 1—figure supplement 2D, circle).

### Lentivirus production

Recombinant lentiviruses were produced as described (Marrink et al., 2019; Melikov et al., 2015) with the following modification: the envelope plasmid pMD.G and the packaging vector pCMVΔR8.91 were replaced by pMD2.G and psPAX2, respectively.

### In vitro membrane potential measurements

Two methods were used to assess cellular membrane potential in vitro. With the first method, the membrane potential was determined by incubating 300,000 cells for 40 min with 100 nM of the fluorescent probe DiBAC4(3) (Thermo Fisher, ref no. B438) in six-well plates in 1 ml media, 10% FBS, and the median fluorescence intensity was then assessed by flow cytometry. Calculation of the actual membrane potential in mV based on the DiBAC4(3) signals was performed as described earlier (Klapperstück et al., 2009; Krasznai et al., 1995). The second method relied on electrophysiology recordings. To perform these, the bath solution composition was (in mM): 103.9 NaCl, 23.9 NaHCO3, 2 CaCl2, 1.2 MgCl2, 5.2 KCl, 1.2 NaH2PO4, 2 glucose, and 1.7 ascorbic acid. The pipet solution was composed of (in mM): 140 KMeSO4, 10 HEPES, 10 KCl, 0.1 EGTA, 10 phosphocreatine, and 4 MgATP. The patch pipets had a resistance of 2.4–3.6 MΩ. Perforated patch recordings were performed as previously described (Cueni et al., 2008). Briefly, freshly prepared gramicidin D (Sigma, ref no. G5002), at 2.8 μM final concentration, was added to prefiltered patch pipet solution and then sonicated for three consecutive times during 10 s. Cell-attached configuration was achieved by applying negative pressure on patch pipet until seal resistance of over 1 GΩ was reached. After gaining cell access through gramicidin created pores, membrane potential measurements were done in current clamp at 0 pA for at least 3 min. Since primary rat neurons are killed following full depolarization induced by gramicidin, the standard curve from membrane potential calculations (Klapperstück et al., 2009; Krasznai et al., 1995) was performed using gramicidin-treated Raji cells incubated with increasing concentrations of DiBac4(3) for 40 min. Images of the cells were then taken using an LSM780 confocal microscope and the cell-associated fluorescence quantitated with ImageJ.

### Relative membrane potential assessment in vivo

Zebrafish embryos in Egg water (see ‘Zebrafish’ section) were incubated for 40 min in the presence or in the absence of various concentrations of valinomycin together with 950 nM DiBac4(3). The embryos were then fixed and visualized under a confocal LSM710 microscope (Adams and Levin, 2012). DiBac4(3)-associated fluorescence of a region of interest (ROI) of about 0.0125 mm2 in the tail region was quantitated with ImageJ. The values were normalized to the control condition (i.e. in the absence of valinomycin). Mice were intradermally injected with 10 μl of a 950 nM DiBac4(3) PBS solution containing or not 10 μM valinomycin and sacrificed 1 hr later. The skin was excised, fixed in 4% formalin, paraffin-embedded, and used to prepare serial histological slices. Pictures of the slices were taken with a CYTATION3 apparatus. The DiBac4(3)-associated fluorescence in the whole slice was quantitated with ImageJ. The slice in the series of slices prepared from a given skin sample displaying the highest fluorescence signal was considered as the one nearest to the injection site. The signals from such slices are those reported in the figures.

### Experimental modulation of the plasma membrane potential

#### Flow cytometry assessment of CPP internalization

Raji, SKW6.4, or HeLa cells: 300,000 cells were plated on non-coated plates to avoid cell adherence in 500 μl RPMI, 10% FBS. Cellular depolarization was induced by pre-incubating the cells at 37°C with 2 μg/ml gramicidin for 5 min and/or by placing them in potassium-rich buffer (Hirose et al., 2012) for 30 min (40 mM KCl, 100 mM potassium glutamate, 1 mM MgCl2, 1 mM CaCl2, 5 mM glucose, 20 mM HEPES, pH 7.4). Cells were then treated with the selected CPPs at the indicated concentrations for 1 hr when peptide internalization was recorded or with 100 nM DiBac4(3) for 40 min when membrane potential needed to be measured. Hyperpolarization in Raji cells in the presence of TAT-RasGAP317-326 was performed by treating the cells with 10 μM valinomycin for 20 min in RPMI without serum. Cells were then treated with 5 µM TAT-RasGAP317-326 for 1 hr or 100 nM DiBac4(3) for 40 min. In the case of SKW6.4 and HeLa cells, hyperpolarization was induced by infection with a viral construct expressing KCNJ2 (see ‘Lentivirus production’ section). Cells were then treated with 40 µM of indicated CPP for 1 hr or 100 nM DiBac4(3) for 40 min.

#### CPP cytosolic internalization quantitation based on confocal microscopy

Three-hundred thousand wild-type HeLa cells were plated overnight on glass-bottom dishes in 2 ml RPMI with 10% FBS. The next day, serum was removed and cells were pre-incubated at 37°C with 2 μg/ml gramicidin for 5 min, 10 μM valinomycin for 20 min, or were left untreated in 1 ml media with 10% FBS. The indicated CPPs were then added and cells were incubated for 1 hr at 37°C. Cells were then washed and visualized in RPMI without serum under a confocal microscope. CPP cytosolic internalization was quantitated within a cytosolic region devoid of endosomes using ImageJ. The number of CPP-positive vesicles per cell was visually determined in a given focal plane.

Neurons (12 days post isolation) were pre-incubated 30 min with 5 mM TEA (tetraethylammonium, Sigma Aldrich, ref no. T2265; gramicidin is toxic in these neurons; see section ‘In vitro membrane potential measurements’) to induce depolarization or 10 μM valinomycin to induce hyperpolarization in bicarbonate-buffered saline solution (116 mM NaCl, 5.4 mM KCl, 0.8 mM MgSO4, 1 mM NaH2PO4, 26.2 mM NaHCO3, 0.01 mM glycine, 1.8 mM CaCl2, 4.5 mg/ml glucose) in a 37°C, 5% CO2 incubator. The cells were then incubated 1 hr with 2 μM of FITC-labeled TAT-RasGAP317-326. The cells were finally washed thrice with PBS and images were acquired using a LSM780 confocal microscope. Cell-associated peptide fluorescence was quantitated using ImageJ.

### Setting membrane potential by changing potassium concentrations in the media

RPMI-like media made without potassium chloride and without sodium chloride was from Biowest (Supplementary file 1). Varying concentrations of potassium chloride were added to this medium containing 10% FBS. Sodium chloride was also added so that the sum of potassium and sodium chloride equaled 119 mM (also taking into account the concentrations of sodium and potassium in FBS). Three-hundred thousand cells were pre-incubated in 1 ml media, 10% FBS containing different concentrations of potassium for 20 min, then different CPPs at a 40 μM concentration were added and cells were incubated for 1 hr at 37°C in 5% CO2. Cells were washed once in PBS and CPP internalization was measured by flow cytometry. The corresponding membrane potential was measured with DiBac4(3).

### In silico CPP translocation free energy assessment through MARTINI coarse-grained simulations

An asymmetric multi-component membrane was constructed and solvated using CHARMM-GUI (Jo et al., 2008; Qi et al., 2015). Each layer contained 100 lipids (Supplementary file 2), in a previously described composition (Ingólfsson et al., 2014). The membrane was solvated with 2700 water molecules, obtaining a molecular system of 10,200 particles. The MARTINI force field 2.2p (Marrink et al., 2003; Wassenaar et al., 2015) was used to define phospholipids’ topology through a coarse-grained approach. The polarizable water model has been used to assess the water topology (Yesylevskyy et al., 2010). Each peptide (R9, TAT, and TAT-RasGAP317-326) structural model has been obtained by PEPFOLD-3 server (Lamiable et al., 2016), as done in previous studies in the field (Grasso et al., 2015; Grasso et al., 2018; Serulla et al., 2020). For each molecular system, one CPP was positioned 3 nm away from the membrane outer leaflet, in the water environment corresponding to the extracellular space. Then, the system was equilibrated through four MD simulations of 100 ps, 200 ps, 500 ps, and 100 ns under the NPT ensemble. Position restraints were applied during the first three MD simulations and gradually removed, from 200 to 10 kJ/mol*nm2. Velocity rescaling (Bussi et al., 2007), temperature coupling algorithm, and time constant of 1.0 ps were applied to keep the temperature at 310.00 K. Berendsen (Berendsen et al., 1984) semi-isotropic pressure coupling algorithm with reference pressure equal to 1 bar and time constant 5.0 ps was employed. Then, all systems were simulated for the production run in the NPT ensemble with a time step of 20 fs. Electrostatic interactions were calculated by applying the particle-mesh Ewald (Darden et al., 1993) method and van der Waals interactions were defined within a cut-off of 1.2 nm. Periodic boundary conditions were applied in all directions. Trajectories were collected every 10 ps and the Visual Molecular Dynamics (VMD) (Humphrey et al., 1996) package was employed to visually inspect the simulated systems. Three different transmembrane potential values were considered: 0, 80, and 150 mV. In the MD simulations, an external electric field Eext was applied parallel to the membrane normal z, that is, perpendicular to the bilayer surface. This was achieved by including additional forces Fi = q*Eext acting on all charged particles i. In order to determine the effective electric field in simulations, we applied a computational procedure reported in literature (Gumbart et al., 2012). A well-tempered metadynamics protocol (Barducci et al., 2008) was applied to estimate the free energy landscape of CPP translocation. Two collective variables were considered: the lipid/water density index and the CPP-membrane distance. Gaussian deposition rate of 2.4 kJ/mol every 5 ps was initially applied and gradually decreased on the basis of an adaptive scheme. Gaussian widths of 0.5 and 0.2 nm were applied following a well-established scheme (Deriu et al., 2016; Granata et al., 2013; Grasso et al., 2017; Laio and Gervasio, 2008). In particular, the Gaussian width value was of the same order of magnitude as the standard deviation of the distance CV, calculated during unbiased simulations. The well-tempered metadynamics simulations were computed using GROMACS 2019.4 package (Abraham et al., 2015) and the PLUMED 2.5 open-source plug-in (Tribello et al., 2014). The reconstruction of the free-energy surface was performed by the reweighting algorithm procedure (Tiwary and Parrinello, 2015) allowing the estimation of the free energy landscape. The comparison between the water pore formation free energy estimated by our MARTINI coarse-grained simulations and previous estimations available in literature is reported in Supplementary file 3. Each system was simulated (with a 20 fs time step) until convergence was reached. The electrostatic potential maps were computed by the APBS package (Baker, 2004) on the molecular system composed of R9 peptide in contact with the cell membrane, without any applied external electrostatic field. In detail, the non-linear Poisson-Boltzmann equation was applied using single Debye-Huckel sphere boundary conditions on a 97 × 97 × 127 grid with a spacing of 1 Å centered at the COM of the molecular system. The relative dielectric constants of the solute and the solvent were set to 2.5 and 78.4, respectively. The ionic strength was set to 150 mM and the temperature was fixed at 310 K (Baker, 2004; Grasso et al., 2017). The average and standard deviation values of the local transmembrane potential were computed considering 10 different trajectory snapshots taken from the molecular trajectory.

### In silico pore formation kinetics through MARTINI coarse-grained simulations

The same molecular system previously constructed and equilibrated was investigated to estimate the water pore formation kinetics by applying a constant electrostatic potential (Böckmann et al., 2008; Fernández et al., 2010; Gao et al., 2019; Gumbart et al., 2012; Gurtovenko and Lyulina, 2014; Kirsch and Böckmann, 2016; Tieleman, 2004; Ziegler and Vernier, 2008). Each peptide (R9, TAT, and TAT-RasGAP317-326) was positioned 3 nm away from the membrane at the beginning of each simulation. The relatively small size of the molecular system and the application of coarse-grained MARTINI force field allowed us to study the pore formation kinetics, requiring many simulations at varying field strengths. In detail, 25 simulations were performed for each molecular system at different external electric field strengths from 0.0055 to 0.090 V/nm. In the MD simulations, an external electric field Eext was applied parallel to the membrane normal z, that is, perpendicular to the bilayer surface. This was achieved by including additional forces Fi = q*Eext acting on all charged particles i. In order to determine the effective electric field in simulations, we applied a computational procedure reported in literature (Gumbart et al., 2012). The results are reported in Figure 4—figure supplement 1.

### In silico cell membrane hyperpolarization modeling through ion imbalance in MARTINI coarse-grained simulations

The translocation mechanism of each CPP was studied by ion imbalance in a double-bilayer system (Delemotte et al., 2008; Gao et al., 2019; Gurtovenko and Vattulainen, 2007; Herrera and Pantano, 2009). The same asymmetric membrane considered to perform the single-bilayer simulations (Supplementary file 2) was used to build up the double-bilayer system. The double-membrane system was solvated with 4300 water molecules, obtaining a molecular system of 20,000 particles. The MARTINI force field 2.2p (Marrink et al., 2003; Wassenaar et al., 2015) was used to define phospholipids’ topology through a coarse-grained approach. The polarizable water model was used to model the water topology (Yesylevskyy et al., 2010). The elastic network ELNEDYN (Periole et al., 2009) was applied to reproduce the structural and dynamic properties of the CPPs.

For each molecular system, one CPP was positioned in the middle of the double-bilayer system, 2 nm away from the membrane outer leaflets, in the water environment corresponding to the extracellular space. Then, the system was equilibrated through four MD simulations of 100 ps, 200 ps, 500 ps, and 100 ns under the NPT ensemble. Position restraints were applied during the first three MD simulations and gradually removed, from 200 to 10 kJ/mol*nm2. Velocity rescaling (Bussi et al., 2007), temperature coupling algorithm, and time constant of 1 ps were applied to keep the temperature at 310 K. Berendsen (Berendsen et al., 1984) semi-isotropic pressure coupling algorithm with reference pressure equal to 1 bar and time constant 5 ps was employed. Then, all systems were simulated for the production run in the NPT ensemble with the time step of 20 fs with Parrinello-Rahman pressure coupling (Parrinello and Rahman, 1981).

Membrane hyperpolarization was achieved through a net charge difference of 30 positive ions between intracellular and extracellular space, considering all charged ions of the system and fulfilling the full system electroneutrality. Ten different replicas of each molecular simulation were performed until the water pore formation and closure events were observed. The visual inspection of the simulated molecular systems is reported in Figure 4—figure supplement 1A. To analyze whether the CPPs were able to cross the membrane and reach the intracellular compartment, their trajectories were studied in the last 5 ns of each simulation replica. Considering the CPP position with respect to the membrane bilayers and the CPP’s solvent accessible surface area, three different compartments were defined: intracellular space, lipid bilayer (cell membrane), and extracellular space. The radius of the water pores within the membrane was calculated as previously done (Gurtovenko and Vattulainen, 2007; Leontiadou et al., 2004). We assumed that the central part of the cylindrical water pore contains N water molecules at the same density as outside of the water flux.

### In vitro assessment of water pores

Three-hundred thousand wild-type HeLa cells or primary rat cortical neurons were incubated with 32 µg/ml PI (0.8–1.5 nm diameter 75) or 200 µg/ml dextran of different molecular weight in the presence or in the absence of the indicated CPPs in normal, depolarizing (2 µg/ml gramicidin), or hyperpolarizing (10 µM valinomycin) conditions in 1 ml media, 10% FBS. Time-lapse images were acquired by confocal microscopy every 10 s. The percentage of cells where direct CPP translocation occurred, as well as the percentage of cells positively stained for PI, were manually quantitated using ImageJ based on snap shot images taken after 30 min of incubation, as shown in Figure 5—figure supplement 1C. Cytosolic PI fluorescence was assessed with ImageJ, by selecting a region within the cell's cytosol devoid of endosomes. Cells were permeabilized with 0.1% saponin (Sigma, ref no. 4706, diluted in PBS weight:volume; 30 min incubation at 37°C in a 5% CO2 incubator) to determine the maximal PI uptake cell capacity. Three fitting models were obtained:

These equations fitted equally well the PI uptake/Vm curve in Figure 5E. For the calculations used in Figure 5F, the exponential decline equation was used.

### Zebrafish viability

FITC-TAT-RasGAP317-326(W317A) internalization in zebrafish was assessed either by adding the peptide directly in Egg water or by injection. Experiments in which the peptide was added in the water were performed on fish between 4 and 24 hr post fertilization. Viability assays were done on embryos of 4, 6, and 24 hr post fertilization to determine a maximal nonlethal dose of the peptide that can be used. Different concentrations of the peptide were added to 500 µl water per well in 24-well plate, with between eight and eleven embryos per well. Fish viability was visually assessed at 20 hr post incubation with the peptide. Hyperpolarization-associated viability was visually assessed at different time points in the presence or in the absence of the peptide with or without various valinomycin concentrations. Zebrafish were visualized with binocular microscope and CYTATION3 apparatus. Survival was visually assessed under a binocular microscope by taking into consideration the embryo transparency (as dead embryos appear opaque), general development characteristics, and motility.

### CPP internalization in vivo

To assess peptide internalization in zebrafish, two methods were used: (i) addition of the peptide directly in 500 µl of Egg water in 24-well plates containing between eight and twelve embryos per well and (ii) intramuscular injections. In the case of the first method, after the indicated treatments, zebrafish were washed, fixed in 4% PFA/PBS for 1 hr at room temperature. Whole embryos were mounted on slides with Fluoromount-G (cBioscience, ref no. 00-4958-02). Zebrafish were then visualized under an LSM710 confocal microscope. Experiments where the peptide was added directly to the water were performed on zebrafish at 18 hr post fertilization to limit cuticle development that would hinder peptide access to the cells. In the case of the second method, 8 nl injections (containing the various combinations of peptide and valinomycin and 0.05% (vol:vol) phenol red as an injection site labeling agent) were done on 48 hr post fertilization embryos into the tail muscle around the extremity of yolk extension, after chorion removal and anesthesia with 0.02% (w:vol) tricaine (Schroeder et al., 2000) buffered with sodium bicarbonate to pH 7.3. At this age, zebrafish already have well developed tissues that can be easily visually distinguished. Injections were done with an Eppendorf Microinjections FemtoJet 4i apparatus. After the indicated treatments, embryos were fixed in 4% PFA/PBS and visualized under a confocal microscope. Some embryos were kept alive for viability evaluation post injection until the age of 4 days.

Experiments with mice were performed in 10- to 14-week-old C57BL/6NCrl mice anesthetized with ketasol/xylasol (9.09 mg/ml ketasol and 1.82 mg/ml xylasol in water; injection: 10 μl per g of body weight). The back of the mice was shaved and intradermic injections were performed (a total of 10 μl was injected). Mice were kept under anesthesia for 1 hr and Artificial tears (Lacryvisc) were used to avoid eye dryness. Mice were then sacrificed by CO2 inhalation, skin was cut at injection sites, fixed in 4% formalin, and paraffin embedded for histology analysis. For each sample, 10–15 slides were prepared and peptide internalization was visualized with a CYTATION3 apparatus. Fluorescence intensity was quantitated with ImageJ. The slices displaying the highest fluorescence signal were considered as those nearest to the injection site and the fluorescent values from these slides were used in Figure 6B.

### Assessment of endosomal escape and direct translocation

Three hundred thousand cells were seeded onto glass-bottom dishes in 2 ml RPMI, 10% FBS for 16 hr. Quantitation of cytosolic fluorescence was performed within live HeLa cells pre-incubated with 80 µM TAT-RasGAP317-326 for 30 min at 37°C in 1 ml media, with 10% FBS and then incubated for the indicated periods of time in the presence (i.e. no wash after the pre-incubation) or in the absence (i.e. following three consecutive washes with RPMI supplemented with 10% FBS) of extracellular labeled peptide. Endosomal escape from lysosomes was induced by 1 mM LLOME (L-leucyl-L-leucine methyl ester) (Repnik et al., 2017), added in the 1 ml media, 10% FBS 30 min after the CPPs were washed out (cells were exposed to LLOME for 100 min). Confocal images were taken every 5 min after the 30 min pre-incubation with the CPPs. For each cell, the fluorescence intensity of one ROI devoid of labeled endosomes throughout the experiment was quantitated over time using ImageJ Time Series Analyzer V3. The surface of the ROI was identical for all cells. Only cells displaying labeled endosomes after the 30 min pre-incubation (that is cells that had taken up the CPPs by endocytosis) were analyzed. Note that the washing steps, for reasons unclear at this time, induced a slightly higher initial ROI intensity signal.

### Transferrin internalization quantitation

Wild-type HeLa cells were plated in 12-well plates (200,000 cells per well) for 16 hr in 1 ml RPMI (Invitrogen, ref no. 61870), supplemented with 10% heat-inactivated FBS (Invitrogen, ref no. 10270–106). Cells were then incubated with 20 µg/ml AlexaFluor488-conjugated transferrin for 20 min at 37°C in 5% CO2. Cells were washed with PBS and pelleted after trypsinization. To quench membrane-bound transferrin fluorescence, cells were resuspended in 0.2% trypan blue diluted in PBS. Transferrin internalization was quantitated by flow cytometry using Beckman Coulter FC500 instrument. Data analysis was done with Kaluza Version 1.3 software (Beckman Coulter).

### TAT-PNA-induced luciferase activity

The LeGOiG2-LUC705 lentiviral construct (plasmid #975) encodes a luciferase gene interrupted by a mutated human beta globin intron 2. This mutation creates a new aberrant splicing site at position 705 that, when used, produced an mRNA that encodes a truncated non-functional luciferase (Guidotti et al., 2017). In the presence of the TAT-peptide nucleic acid (TAT-PNA) CPP described below, the aberrant splice site is masked allowing the production of a functional luciferase enzyme. Lentiviruses produced using this construct were employed to infect cells. The doses used resulted in >90% cells infected (based on GFP expression from the lentiviral vector). The infected cells (200,000 cells in 12-well plates containing 1 ml of RPMI, 10% FBS) were treated or not with 5 μM TAT-PNA (GRKKRRQRRR-CCTCCTACCTCAGTTACA). TAT-PNA is made of TAT48-57 and an oligonucleotide complimentary to a sequence containing the aberrant splice site. After 16 hr incubation, cells were washed twice in HKR buffer (119 mM NaCl, 2.5 mM KCl, 1 mM NaH2PO4, 2.5 mM CaCl2, 1.3 mM MgCl2, 20 mM HEPES, 11 mM dextrose, pH 7.4) and lysed in 40 μl HKR containing 0.1% Triton X-100 for 15 min at room temperature. Luciferase activity was measured with a GLOMAXTM 96 Microplate Luminometer (Promega) using a Dual-Luciferase Reporter Assay (Promega) and normalized to the protein content. Results are displayed as the ratio between the protein-normalized luciferase signal obtained in TAT-PNA-treated cells and the signal obtained in control untreated cells.

### TAT-Cre recombinase production, purification, and recombination assay

Raji cells were infected with a lentivirus encoding a Cre-reporter gene construct (D’Astolfo et al., 2015). TAT-Cre recombinase was produced as described (Wadia et al., 2004). Briefly, Escherichia coli BL21 transformed with the pTAT-Cre plasmid (#917, Addgene plasmid #35619) were grown for 16 hr in LB containing 100 µg/ml kanamycin. Protein production was induced at OD600 of 0.6 with 500 µM IPTG (isopropyl β-D-1-thiogalactopyranoside) for 3 hr. Bacteria were collected by centrifugation at 5000× g and kept at –20°C. Purification was performed on Äkta prime (GE, Healthcare, Chicago, IL) equipped with a 1 ml HisTrap FF column equilibrated with binding buffer (20 mM sodium phosphate, 500 mM NaCl, 5 mM imidazole pH 7.4). The day of the purification, bacterial pellet was resuspended in lysis buffer (binding buffer with protease inhibitors; Roche, ref no. 4693132001; one tablet per 50 ml), 0.025 mg/ml DNase I (Roche, ref no. 04716728001), and 2 mg/ml lysozyme (Roche, ref no. 10 837 059 001) and sonicated six times for 30 s. After 20 min centrifugation at 5000× g, the supernatant was filtered through Steriflip 0.45 µm and loaded on the column. Elution buffer (20 mM sodium phosphate, 500 mM NaCl, 500 mM imidazole pH 7.4) was used to detach His-tagged proteins from the column. Imidazole was removed from collected fractions by overnight dialysis using 10 K MWCO cassette (Thermo Scientific, ref no. 66807) in PBS. Raji cells encoding the Cre-reporter were treated for 48 hr with 20 µM TAT-Cre-recombinase. Fluorescence was imaged using a Nikon Eclipse TS100 microscope.

### Assessment of CPP binding to plasma membranes

Three-hundred thousand cells were incubated for 60 s in 1 ml RPMI supplemented with 10% FBS and 10 mM HEPES in Eppendorf tubes at 37°C in the presence of increasing concentrations of FITC-TAT-RasGAP317-326. Half of the cells were then immediately placed on ice, pelleted at 4°C, and resuspended in 1 ml of ice-cold PBS and then split into two tubes, one of which receiving a final concentration of 0.2% (w:w) trypan blue to quench surface-associated FITC signals. The cells (still kept at 4°C) were then analyzed by flow cytometry. The surface associated peptide signal was calculated by subtracting total fluorescence measured in PBS and fluorescence measured after trypan blue quenching. The other half of the cells after the 60 s peptide incubation was incubated at 37°C for 1 hr at which time the cellular internalization of the labeled peptide was assessed by flow cytometry.

### Transient calcium phosphate transfection in HeLa cells

Calcium phosphate-based transfection of HeLa cells was performed as previously described (Jordan et al., 1996). Briefly, cells were plated overnight in DMEM (Invitrogen, ref no. 61965) medium supplemented with 10% heat-inactivated FBS (Invitrogen, ref no. 10270–106), 2.5 µg of total plasmid DNA of interest was diluted in water, CaCl2 was added and the mixture was incubated in presence of HEPES 2× for 60 s before adding the total mixture drop by drop to the cells. Media was changed 10 hr after.

### Isothermal titration calorimetry

Isothermal titration calorimetry (ITC) was performed using MicroCal ITC200 (Malvern Panalytical) at 37°C with 600 µM FITC-R9 in the cell (total volume 300 µl) and consecutive injections (2.5 µl/injection, except for the first injection of 0.4 µl) of 6 mM PI from the syringe (total volume 40 µl) with 2 min delay between injections and 800 rotations/min rotation speed. Differential power was set to 7, as we had no prior knowledge of the expected reaction thermodynamics. The results in Figure 5—figure supplement 2A are represented as a: thermogram (measurement of thermal power need to ensure that there is no temperature difference between reference and sample cells in the calorimeter as a function of time) and a binding isotherm (normalized heat per peak as a function of molar ratio).

### Colony formation assay

Three-hundred thousand wild-type HeLa cells were plated overnight in RPMI with 10% FBS in six-well plates. Cells were then treated for 1 hr with the indicated concentrations of CPP, PI, and membrane potential modulating agents (gramicidin or valinomycin) in 1 ml RPMI. As control, cells were either left untreated or incubated with DMSO, the vehicle used to dilute gramicidin and valinomycin. Cells were then washed, trypsinized, and plated on 10 cm dishes at a density of 300 cells per condition. Colonies were counted at day 14 after 100% ethanol fixation for 10 min and Giemsa staining. Washes were done with PBS.

### Genome-scale CRISPR/Cas9 knock-out screening

The human GeCKO v2 library (two plasmid system) (Addgene plasmid #1000000049) was amplified by electroporation using a Bio-Rad Gene Pulser II electroporation apparatus (Bio-Rad #165–2105) and the Lucigen Endura bacteria (Lucigen ref no. 60242). Cells were plated on LB agar plates containing 100 µg/ml ampicillin. After 14 hr at 32°C, colonies were scrapped and plasmids recovered with the Plasmid Maxi kit (Qiagen, ref no. 12162). To produce lentivirus library, 12 T-225 flasks were seeded with 12 × 106 HEK293T cells per flask in 40 ml DMEM, 10% FBS. The following day, 10 µg pMD2.G, 30 µg psPAX2, and 25 µg GeCKO plasmid library in 1.8 ml H2O were mixed with 0.2 ml 2.5 M CaCl2 (final calcium concentration: 250 mM). This solution was mixed (v/v) with 2× HEPES buffer (280 mM NaCl, 10 mM KCl, 1.5 mM Na2HPO4, 12 mM D-glucose, 50 mM HEPES), incubated for 1 min at room temperature, added to the culture medium, and the cells placed back in a 37°C, 5% CO2 incubator for 7 hr. The culture medium was then removed and replaced by DMEM supplemented with 10% FBS containing 100 U/ml penicillin and 100 µg/ml streptomycin. Forty-eight hours later, the medium was collected and centrifuged 5 min at 2000× g to pellet the cells. The remaining cell-free medium (12 × 40 ml) was then filtered through a 0.45 µm HV/PVDF (Millipore, ref no. SE1M003M00) and concentrated ~100 times by resuspending the viral pellet obtained by ultracentrifugation at 70000× g for 2 hr at 4°C in ~5 ml ice-cold PBS. The concentrated viruses were aliquoted in 500 µl samples and stored at –80°C.

To express the Cas9 endonuclease, cells (e.g. Raji or SKW6.4) were infected with Cas9-expressing viruses that were produced in HEK293T cells transfected with the lentiCas9-Blast (#849, Addgene plasmid #52962), pMD2.G, and psPAX2 plasmids as described under ‘Lentivirus production’. The infected cells were selected with 10 µg/ml blasticidin for a week. The multiplicity of infection (MOI) of the GeCKO virus library was determined as follows. Different volumes of the virus library were added to 3 × 106 Cas9-expressing cells plated in 12-well plates. Twenty-four hours later, the cells were split into two wells of 12-well plates. One well per pair was treated with 10 µg/ml puromycin for 3 days (the other cultured in normal medium). Cell viability was determined by trypan blue exclusion and MOI was calculated as the number of cells in the well treated with puromycin divided by the number of cells in the control well. The virus volume yielding to a MOI ~ 0.4 was chosen to perform large-scale infection of 12 × 107 cells that was carried out in 12-well plates with 3 × 106 cells per well. After 24 hr, the infected cells were collected and pooled in a T-225 flask and selected with 10 µg/ml puromycin for a week. Thirty millions of these were frozen (control untreated cells) and 60 million others were treated with 40 µM TAT-RasGAP317-326 for 8 days (Raji) or for 17 days (SKW6.4) with a medium and peptide renewal every 2–3 days. Thirty million of the peptide-treated cells were then also frozen. Genomic DNA was extracted from the control and the peptide-treated frozen cells using the Blood & Cell Culture DNA Midi Kit according to manufacturer’s instructions (Qiagen, ref no. 13343). A first PCR was performed to amplify the lentiCRISPR sgRNA region using the following primers:

A second PCR (see Supplementary file 4 for the primers used) was performed on 5 µl of the first PCR reaction to attach Illumina adaptors with barcodes (nucleotides highlighted in green) and to increase library complexity (using the sequences highlighted in red) to prevent signal saturation when the sequencing is performed. The blue sequences are complementary to the extremities of the first PCR fragments.

Both PCRs were performed in 100 µl with the 2 µl of the Herculase II Fusion DNA Polymerase from Agilent (ref no. 600675) according the manufacturer’s instructions. Amplicons were gel extracted, quantitated, mixed, and sequenced with an MiSeq (Illumina). Raw FASTQ files were demultiplexed and processed to contain only unique sgRNA sequences. The number of reads of each sgRNA was normalized as described (Tribello et al., 2014). The MAGeCK algorithm (Tsoutsou et al., 2017) was used to rank screening hits by the consistent enrichment among multiple sgRNAs targeting the same gene.

### CRISPR/Cas9-based genome editing

Single guide RNAs targeting an early exon of the gene of interest were chosen in the sgRNA library (Wallbrecher et al., 2017) and are listed in Supplementary file 5. LentiCRISPR plasmids specific for a gene were created according to the provided instructions (Vasconcelos et al., 2013). Briefly, oligos were designed as follows: Forward 5’-CACCGnnnnnnnnnnnnnnnnnnnn-3’; Reverse-3’-CnnnnnnnnnnnnnnnnnnnnCAA-5’, where nnnnnnnnnnnnnnnnnnnn in the forward oligo corresponds to the 20 bp sgRNA. Oligos were synthetized, then phosphorylated, and annealed to form oligo complexes. LentiCRISPR vector was BsmBI digested and dephosphorylated. Linearized vector was purified and gel extracted and ligated to oligo complexes. The lentiCRISPR vector containing the sgRNA was then used for virus production. Recombinant lentiviruses were produced as described (Mitchell et al., 2000) with the following modification: pMD.G and pCMVDR8.91 were replaced by pMD2.G and psPAX2, respectively. Cells were infected and selected with the appropriate dose of puromycin (2 µg/ml for HeLa cells). Clone isolation was performed by limiting dilution in 96-well plate.

### TA cloning

TA cloning is a subcloning technique that allows integration of a PCR-amplified product of choice into a PCR2.1 vector based on complementarity of deoxyadenosine added onto the PCR fragment by Taq polymerase. This approach is useful to distinguish between several alleles and to determine whether the cells are heterozygous or homozygous at a given locus. TA cloning kit (Life Technologies, ref no. K202020) was used according to manufacturer’s instructions to sequence DNA fragment containing the region targeted by a given sgRNA. Briefly, DNA was isolated and the fragment of interest was PCR-amplified using primers listed in Supplementary file 6, then ligated into PCR2.1 vector. E. coli competent cells were then transformed and at least 15 colonies were selected per condition for DNA isolation and sequencing.

### Plasmid constructs

The hKCNN4-V5.lti (#953) lentiviral plasmid encoding a V5-labeled version of the KCNN4 potassium channel was from DNASU (ref no. HsCD00441560). The hKCNK5-FLAG.dn3 (#979) plasmid encoding the human KCNK5 potassium channel (NCBI reference sequence NM_003740.3), Flag-tagged at the C-terminus, was purchased from GenScript (ref no. OHu13506). The Myc-mKCNJ2-T2A-IRES-tdTomato.lti (#978) lentiviral vector encoding the mouse Kir2.1 (KCNJ2) potassium channel and tdTomato (separated by an IRES) was generated by subcloning myc-mKCNJ2-T2A-Tomato.pCAG plasmid (#974, Addgene plasmid #60598) into the LeGo-iT2 lentiviral backbone (#809), a gift from Boris Fehse (Addgene plasmid #27343), through ligation of both plasmids after digestion with BamHI (NEB, reg. no. R313614). The pMD2.G plasmid (#554, Addgene plasmid #12259) encodes the envelope of lentivirus. The psPAX2 plasmid (#842, Addgene plasmid #12260) encodes the packaging system. Both pMD2.G and psPAX2 plasmids were used for lentiviral production. The Flag-hKCNQ5(G278S)-IRES-NeoR plasmid (#938) codes for the N-terminal Flag-tagged G278S human KCNQ5 inactive mutant and a neomycin resistant gene separated by an IRES sequence. It was generated by subcloning a BamHI/XmaI digested PCR fragment obtained by amplification of pShuttle-Flag-hKCNQ5(G278S)-IRES-hrGFP2 (#937, kind gift from Dr Kenneth L Byron) using forward primer #1397 (CAT CGG GAT CCG CTA TAC CGG CCA CCA TGG ATT ACA AGG A) and reverse primer #1398 (CAT CGC CCG GGG CTA TAC CGT ACC GTC GAC TGC AGA ATT C) into the lentiviral vector TRIP-PGK-IRES-Neo (#350) opened with the same enzyme. The Flag-hKCNQ5(SM,G278S)-IRES-Neo (#939) plasmid is identical to Flag-hKCNQ5(G278S)-IRES-NeoR except that the sequence targeted by the sgKCNQ5.1 sgRNA (Supplementary file 5) was mutated with the aim to decrease Cas9-mediated degradation. Silent mutations (SM), at the protein level, were introduced using the QuikChange II XL Site-Directed Mutagenesis Kit (ref no. 200522) according to manufacturer’s instructions using forward primer #1460 (AAA TAA GAA CCA AAA ATC CTA TGT ACC ATG CCG TTA TCA GCT CCT TGC TGT GAG CAT AAA CCA CTG AAC CCA G) and reverse primer #1461 (CTG GGT TCA GTG GTT TAT GCT CAC AGC AAG GAG CTG ATA ACG GCA TGG TAC ATA GGA TTT TTG GTT CTT ATT T).

The Flag-hKCNQ5(SM)-IRES-NeoR (#940) lentiviral construct codes for a Flag-tagged wild-type version of human KCNQ5. It was made by reverting the G278S mutation in Flag-hKCNQ5(SM,G278S)-IRES-Neo (#939) using the QuikChange II XL Site-Directed Mutagenesis Kit with the #1462 forward primer (TTT TGT CTC CAT AGC CAA TAG TTG TCA ATG TAA TTG TGC CCC) and the #1463 reverse primer (GGG GCA CAA TTA CAT TGA CAA CTA TTG GCT ATG GAG ACA AAA). The pLUC705 (Kang et al., 1998) (#876, gift from Dr Bing Yang) plasmid encodes a luciferase gene interrupted by a mutated human beta globin intron 2. This mutation creates a new aberrant splicing site at position 705 that when used produced an mRNA that encodes a truncated non-functional luciferase (Kang et al., 1998). To introduce this construct into a lentiviral vector, the pLUC705 plasmid was digested with HindIII/XhoI, blunted with T4 DNA polymerase, and ligated into StuI-digested and dephosphorylated LeGO-iG2 (#807, Addgene plasmid #27341), resulting in plasmid pLUC705.LeGO-iG2 (#875). The pTAT-Cre (#917, Addgene plasmid #35619) bacterial plasmid encodes a histidine-tagged TAT-Cre recombinase. The Cre reporter lentiviral vector (#918, Addgene plasmid #62732) encodes a LOXP-RFP-STOP-LOXP-GFP gene construct. Cells expressing this plasmid appear red but once recombination has occurred when TAT-Cre is translocated into cells, the RFP-STOP fragment will be excised, GFP but not RFP will now be produced, and cells will appear green.

### Peptides

TAT-RasGAP317-326 is a retro-inverso peptide (i.e. synthesized with D-amino-acids in the opposite direction compared to the natural sequence) labeled or not with FITC or TMR. The TAT moiety corresponds to amino acids 48–57 of the HIV TAT protein (RRRQRRKKRG) and the RasGAP317–326 moiety corresponds to amino acids from 317 to 326 of the human RasGAP protein (DTRLNTVWMW). These two moieties are separated by two glycine linker residues in the TAT-Ras-GAP317-326 peptide. FITC-bound peptides without cargo: TAT, Penetratin (RQIKWFQNRRMKWKK), R9 (RRRRRRRRR), and K9 (KKKKKKKKK) were synthesized in D-amino acid conformation. All peptides were synthesized in retro-inverso conformation (over the years different suppliers were used with routine checks for activity of TAT-RasGAP317-326 derived peptides, Biochemistry Department of University of Lausanne, SBS Genetech, China and Creative Peptides, USA) and resuspended to 1 mM in water.

### Statistical analysis

Statistical analysis was performed on non-normalized data, using GraphPad Prism 7. ANOVA multiple comparison analysis to wild-type condition was done using Dunnett’s correction (Figure 3A–C and Figure 3—figure supplement 1B, C and Figure 3C, top panel, and PI internalization in Figure 5C, as well as TAT-PNA internalization in Figure 2—figure supplement 4A). ANOVA multiple comparison analysis between several conditions was done using Tuckey’s correction (Figure 3—figure supplement 2E). Comparison between two conditions was done using two-tailed paired t-test for the CPP internalization experiments described in Figure 3C (bottom panel), Figure 6A–B, Figure 1—figure supplement 1B, and Figure 3—figure supplement 4. All measurements were from biological replicates. Unless otherwise stated, the horizontal bars in the graph represent the median, the height of columns correspond to averages, and the dots in the figures correspond to values derived from independent experiments.
