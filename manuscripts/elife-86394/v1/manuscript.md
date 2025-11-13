# Improved isolation of extracellular vesicles by removal of both free proteins and lipoproteins

## Authors

- Dmitry Ter-Ovanesyan<sup>1</sup> ([ORCID: 0000-0002-1134-0073](https://orcid.org/0000-0002-1134-0073))
- Tal Gilboa<sup>1</sup> ([ORCID: 0000-0001-8172-7786](https://orcid.org/0000-0001-8172-7786))
- Bogdan Budnik<sup>1</sup>
- Adele Nikitina<sup>1</sup>
- Sara Whiteman<sup>1</sup>
- Roey Lazarovits<sup>1</sup> ([ORCID: 0000-0002-4635-9700](https://orcid.org/0000-0002-4635-9700))
- Wendy Trieu<sup>1</sup>
- David Kalish<sup>1</sup>
- George M Church<sup>1</sup>
- David R Walt<sup>1</sup> ([ORCID: 0000-0002-5524-7348](https://orcid.org/0000-0002-5524-7348)) †

### Affiliations

1. Wyss Institute for Biologically Inspired Engineering Boston United States ([ROR:008cfmj78](https://ror.org/008cfmj78))
2. Department of Pathology, Brigham and Women’s Hospital Boston United States ([ROR:04b6nzv94](https://ror.org/04b6nzv94))
3. Harvard Medical School Boston United States

† Corresponding author

## Abstract

Extracellular vesicles (EVs) are released by all cells into biofluids such as plasma. The separation of EVs from highly abundant free proteins and similarly sized lipoproteins remains technically challenging. We developed a digital ELISA assay based on Single Molecule Array (Simoa) technology for ApoB-100, the protein component of several lipoproteins. Combining this ApoB-100 assay with previously developed Simoa assays for albumin and three tetraspanin proteins found on EVs (Ter-Ovanesyan, Norman et al., 2021), we were able to measure the separation of EVs from both lipoproteins and free proteins. We used these five assays to compare EV separation from lipoproteins using size exclusion chromatography with resins containing different pore sizes. We also developed improved methods for EV isolation based on combining several types of chromatography resins in the same column. We present a simple approach to quantitatively measure the main impurities of EV isolation in plasma and apply this approach to develop novel methods for enriching EVs from human plasma. These methods will enable applications where high-purity EVs are required to both understand EV biology and profile EVs for biomarker discovery.

## Introduction

Extracellular vesicles (EVs) are membrane vesicles released by all cells. EVs contain RNA and protein cargo from their cell of origin and are a promising class of biomarkers in biofluids such as plasma (Shah et al., 2018). Since EVs are much less abundant than free proteins and lipoproteins in plasma, enriching them without the co-isolation of these impurities remains highly challenging (Sódar et al., 2016; Smolarz et al., 2019). This is particularly the case for separating EVs and lipoproteins, as these two classes of particles have overlapping size ranges (Simonsen, 2017). Developing EV isolation methods is also particularly challenging due to the inability of most methods, such as the commonly used Nanoparticle Tracking Analysis (NTA) to differentiate between EVs and similarly sized lipoproteins (Johnsen et al., 2019). Thus, it is difficult to compare EV isolation methods without suitable techniques to quantify both EV yield and lipoprotein content (Hartjes et al., 2019).

We have previously developed a framework for comparing EV isolation methods by measuring three tetraspanin transmembrane proteins present on EVs (CD9, CD63, and CD81) and albumin (Ter-Ovanesyan et al., 2021). We used the tetraspanins as a way to compare EV yields across different isolation methods and albumin (the most abundant free protein in plasma) as a way to measure protein contamination. To measure these proteins, we used Single Molecule Array (Simoa) technology, a digital ELISA method that results in high sensitivity and a wide dynamic range (Rissin et al., 2010).

In this work, we developed a Simoa assay for ApoB-100, the major protein component of several lipoproteins. ApoB-100 is present on low-density lipoproteins (LDL), intermediate-density lipoproteins (IDL), and very low-density lipoproteins (VLDL) (German et al., 2006; Sniderman et al., 2019). By combining the new ApoB-100 assay with our previously developed CD9, CD63, CD81, and albumin assays, we could quantify EVs, lipoproteins, and free proteins for each sample on the same platform. We then used these assays to further improve EV isolation methods from plasma, enabling us to separate EVs from lipoproteins and free proteins at purity levels beyond those of previously described methods. We envision these methods to enable applications requiring high EV purity, such as EV proteomics for biomarker discovery from human biofluids.

## Results

To measure lipoproteins, we developed a Simoa assay against ApoB-100, the protein component of lipoproteins LDL, IDL, and VLDL. Simoa is a digital ELISA method where individual immuno-complexes are trapped on magnetic beads that are loaded into microwells that fit, at most, one bead per well. Counting the ‘on wells’ thus translates to counting individual protein molecules, providing much higher sensitivity than traditional ELISA (Rissin et al., 2010). First, we compared a variety of capture and detector antibodies using calibration curves of the purified ApoB-100 protein standard. We then chose the antibody pair with the highest signal-to-background ratio (Figure 1A) and validated this assay with dilution linearity experiments in three individual plasma samples (Figure 1B). We also performed spike and recovery experiments using a purified protein standard (Table 1). We then combined this Simoa assay for ApoB-100 with our previously developed CD9, CD63, CD81, and albumin assays (Ter-Ovanesyan et al., 2021; Norman et al., 2021) to simultaneously measure EVs, free proteins, and lipoproteins on the same platform.

![Figure 1.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig1-v1.jpg)

**Figure 1.:** Simoa ApoB-100 assay was validated using: (A) Calibration curve using purified ApoB-100 protein. (B) Dilutions of human plasma (from three different individuals) to confirm dilution linearity of endogenous ApoB-100. Error bars represent the standard deviation from two technical replicates.

**Table 1.**
 Spike and recovery for ApoB-100 assay.Percent recovery of different concentrations of purified ApoB-100 spike added to plasma and measured using the ApoB-100 Simoa assay.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Spike concentration(ng/ml)</th>
      <th>Average recovery (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Spike 1</td>
      <td>5</td>
      <td>94.7</td>
    </tr>
    <tr>
      <td>Spike 2</td>
      <td>10</td>
      <td>87.2</td>
    </tr>
    <tr>
      <td>Spike 3</td>
      <td>50</td>
      <td>90.8</td>
    </tr>
    <tr>
      <td>Spike 4</td>
      <td>500</td>
      <td>90.6</td>
    </tr>
  </tbody>
</table>

We first investigated whether EVs can be separated from ApoB-100-containing lipoproteins using existing techniques. We tested EV separation based on size using size exclusion chromatography (SEC) columns with three different resins (Sepharose CL-2B, CL-4B, and CL-6B). We collected 0.5 ml fractions after performing SEC and used Simoa to measure CD9, CD63, CD81, albumin, and ApoB-100 in each fraction (Figure 2A). As in our previous work (Ter-Ovanesyan et al., 2021), we calculated relative EV yields between different EV isolation methods (Figure 2B). To calculate EV yield, we first determined the ratio of each tetraspanin between conditions and then took the average of the three tetraspanin ratios. To then calculate EV purity, we calculated the ratio of EV yield relative to albumin or ApoB-100 levels. We found that although the ratio of EVs relative to ApoB-100 was higher in the resin with the largest pore size, Sepharose CL-2B, this was at the expense of EV yield relative to the other two resins (Figure 2C).

![Figure 2.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig2-v1.jpg)

**Figure 2.:** (A) Levels of CD9, CD63, CD81, ApoB-100, and albumin were measured by Simoa after SEC of 1 ml plasma in each fraction using either Sepharose CL-2B, Sepharose CL-4B, or Sepharose CL-6B resin. (B) Extracellular vesicle (EV) yield is calculated in fractions 7–10 for Sepharose CL-2B, Sepharose CL-4B, or Sepharose CL-6B by averaging the ratios of CD9, CD63, and CD81. (C) Purity of EVs with respect to lipoproteins or free proteins is calculated by dividing relative EV yield (the average of the ratios of CD9, CD63, and CD81) by levels of ApoB-100 (top) or albumin (bottom). Error bars represent the standard deviation of four columns measured on different days with two technical replicates each.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Levels of CD9, CD63, CD81, and albumin were measured by Simoa after EV isolation from 1 ml plasma with size exclusion chromatography (SEC) using 0, 1, 2, or 3 in-column 10 ml PBS washes. Error bars represent the standard deviation from two technical replicates. (B) Percent recovery of EVs using average of ratios of CD9, CD63, and CD81 in SEC isolation relative to plasma.

Because separating EVs from lipoproteins based on size alone was not fruitful, we attempted to separate EVs from lipoproteins based on other properties. We first investigated the separation of EVs from lipoproteins and albumin using density gradient ultracentrifugation (DGC). We loaded 1 ml of plasma on an iodixanol gradient and performed ultracentrifugation for 16 hr. We then collected 1 ml fractions and used Simoa to measure tetraspanins, albumin, and ApoB-100 in each fraction. We found that we could readily separate EVs from ApoB-100-containing lipoproteins (Figure 3) using DGC, although the EV yield was lower than in SEC (Figure 3—figure supplement 1A). As DGC is time-consuming and low throughput, we explored other EV isolation methods that would be more suitable for processing clinical samples.

![Figure 3.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig3-v1.jpg)

**Figure 3.:** Levels of CD9, CD63, CD81, albumin, and ApoB-100 were measured by Simoa in individual 1 ml fractions (collected from the top) after density gradient centrifugation of plasma using an iodixanol gradient. Error bars represent the standard deviation of two replicates of each measurement.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Levels of CD9, CD63, CD81, ApoB-100 albumin were measured (in duplicate and then averaged) by Simoa to compare extracellular vesicle (EV) isolation from 1 ml plasma using density gradient (DG) centrifugation, SEC, or density gradient centrifugation followed by size exclusion chromatography (DG-SEC). For the DG and DG-SEC condition, fraction 10 was analyzed. Simoa measurements were used to quantify relative EV recovery (A), EV/ApoB-100 ratio (B), and EV/albumin ratio (C).

We next considered whether SEC could be modified to maximize EV yield while removing both free proteins and lipoproteins. First, we wanted to assess the absolute recovery of EVs by SEC using Sepharose CL-6B, the resin with the highest EV yield (Figure 2—figure supplement 1). We took advantage of Simoa’s wide dynamic range and specificity to measure tetraspanin levels in diluted plasma and compared these levels after EV purification from the same batch of plasma by SEC. We also evaluated how various other parameters affected EV recovery by SEC. We found that performing at least one 10 ml phosphate-buffered saline (PBS) wash in-column, instead of simply washing the resin in bulk before making the column, increased the EV yield significantly (Figure 2—figure supplement 1A). One potential reason for this result could be that in-column washes are more effective at removing the ethanol in which the resin is supplied. After performing an in-column wash, we were able to achieve >50% EV yield using SEC with Sepharose CL-6B (Figure 2—figure supplement 1B), as measured by comparing tetraspanin levels in SEC fractions 7–10 relative to diluted plasma.

We then decided to take advantage of the property that ApoB-100 is positively charged (Olsson et al., 1991), while EVs are generally negatively charged (Brownlee et al., 2014) to separate EVs from lipoproteins. It has previously been demonstrated that dual-mode chromatography (DMC) columns with a bottom layer of cation exchange resin below Sepharose CL-4B can be used to isolate EVs (Van Deun et al., 2020). Since Sepharose CL-6B yields more EVs than Sepharose CL-4B (Figure 2C), we constructed DMC columns with a 2-ml cation exchange resin bottom layer and a top layer of 10 ml Sepharose CL-6B. Inspired by the DMC approach of combining different resins in the same column, we also developed a new type of column, Tri-Mode mixed-mode Chromatography (TMC), where we further added Capto Core 700 to the cation exchange resin in the bottom layer. Capto Core 700 is a multimodal chromatography resin that contains porous beads with an inner core layer functionalized with octylamine groups that bind and trap proteins (Blom et al., 2014). Thus, we reasoned that having this resin in the bottom layer would ‘catch’ free proteins that co-isolate with EVs during SEC (Figure 4A). By changing the volumes and ratios of the two resins, the depletion of both albumin and ApoB-100 could be tuned to increase purity, although at the cost of EV yield (Figure 4—figure supplement 1). To balance EV yield and purity, we settled on a 2:1 ratio of solid cation exchange resin to multimodal resin in the 2 ml bottom layer.

![Figure 4.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig4-v1.jpg)

**Figure 4.:** (A) Schematic of the columns being compared: size exclusion chromatography (SEC) column comprised of 10 ml Sepharose CL-6B, dual-mode chromatography (DMC) columns comprised of 10 ml Sepharose CL-6B SEC resin atop 2 ml Fractogel cation exchange resin, Tri-Mode Chromatography (TMC) columns comprised of 10 ml Sepharose CL-6B SEC resin atop 2 ml 2:1 ratio of 2 ml Fractogel cation exchange resin to Capto Core 700 multimodal chromatography resin. (B) Electron microscopy of EVs isolated from plasma using SEC (left), DMC (middle), or TMC (right) columns. EVs indicated with red arrows (among background of lipoproteins). (C) EV recovery is calculated for EV isolation from plasma for SEC (fractions 7–10), DMC (fractions 9–12), or TMC (fractions 9–12). Simoa measurements in the designated fractions for CD9, CD63, and CD81 are taken as a ratio relative to measurements of these proteins from diluted plasma and these three ratios are then averaged to calculate recovery. (D) Purity of EVs with respect to free proteins is determined by dividing relative EV yield (the average of the ratios of CD9, CD63, and CD81) by relative levels of albumin in each condition. (E) Purity of EVs with respect to lipoproteins is determined by dividing relative EV yield (the average of the ratios of CD9, CD63, and CD81) by relative levels of ApoB-100 in each condition. Error bars represent the standard deviation of four column measured on different days with two technical replicates each.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Levels of CD9, CD63, CD81, ApoB-100, and albumin were measured (in duplicate and then averaged) by Simoa in extracellular vesicle (EV) samples isolated from 1 ml plasma to compare TMC columns with different volumes and ratios of Fractogel cation exchange resin to Capto Core 700 resin. All conditions describe the bottom layer under a 10 ml Sepharose CL-6B top layer. The 1, 2, or 4 ml volume of the bottom later indicates the volume of the solid resin mixture of Fractogel cation exchange resin and Capto Core 700 resin. The following fractions were collected for each: 8–11 for 1 ml bottom layer, 9–12 for 2 ml bottom layer, and 11–14 for 4 ml bottom layer.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Levels of CD9, CD63, CD81, ApoB-100, and albumin were measured by Simoa in fractions 7–10 for SEC with 10 ml Sepharose CL-6B column and fractions 7–14 for DMC using a column with 2 ml Fractogel cation exchange bottom layer and 10 ml Sepharose CL-6B top layer. Error bars represent the standard deviation from two technical replicates.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** Levels of CD9, CD63, CD81, ApoB-100, and albumin were measured by Simoa in extracellular vesicle (EV) samples isolated from 1 ml plasma using SEC (fractions 7–10), DMC (fractions 9–12), or TMC columns (fractions 9–12). Error bars represent the standard deviation of four column measured on different days with two technical replicates each.

We compared EV purification from plasma using SEC, DMC, and TMC columns. We first used electron microscopy to image EVs from each column. We found that, although lipoproteins were still present, DMC and TMC led to a higher purity of EVs relative to lipoproteins (Figure 4B). We then used Simoa to quantify the relative levels of EVs, lipoproteins, and free proteins using SEC, DMC, and TMC columns. We collected fractions 9–12 (instead of fractions 7–10 as for SEC) for DMC and TMC to account for the extra 2 ml of resin in the column (Figure 4—figure supplement 2). We found that DMC and TMC columns significantly depleted ApoB-100, but also led to some loss in EV yield, particularly CD9, compared to SEC columns (Figure 4—figure supplement 3). Calculating the relative yields of each tetraspanin and averaging the three tetraspanin ratios to calculate EV yield, we found that DMC and TMC columns had a lower EV yield than SEC but significantly higher EV/ApoB-100 ratios. Although DMC columns had higher ratios of EVs to ApoB-100 compared to SEC, the ratio of EVs to albumin remained the same. The TMC column, on the other hand, had a higher ratio of both EVs to ApoB-100 and EVs to albumin compared to the SEC column (Figure 4C–E).

To assess the utility of highly pure EVs isolated with TMC, we performed mass spectrometry-based proteomic analysis. Performing mass spectrometry on EVs from plasma is challenging because levels of both free proteins and lipoproteins are several orders of magnitude higher than those of EV proteins (Smolarz et al., 2019). Using TMC, we were able to detect 780 proteins from EVs isolated from only 1 ml of plasma (Supplementary file 1). These results demonstrate the advantage of using TMC for deep proteomics analysis using a small sample volume.

Single-use chromatography columns, whether SEC to maximize EV yield or TMC to maximize EV purity, represent an attractive platform for isolating EVs from clinical samples as they are inexpensive and take a short time to run (Monguió-Tortajada et al., 2019). The throughput of columns, however, is limited. Columns are usually run one at a time, and although it is possible to run more than one column at the same time, this becomes challenging if done manually. To increase the throughput and reproducibility of column-based EV isolation, we built a semi-automated stand for running eight columns in parallel. Using a syringe pump run by a Raspberry Pi, we were able to dispense liquid to all columns in parallel (Figure 5A, B). We tested the reproducibility of our device using Simoa and found high concordance between eight SEC columns run by the device and eight SEC columns run manually for EV isolation from plasma (Figure 5C). Although this device was built as a proof of principle to run eight columns in parallel, we envision building a similar device that could run many more columns simultaneously in the future.

![Figure 5.](https://cdn.elifesciences.org/articles/86394/elife-86394-fig5-v1.jpg)

**Figure 5.:** (A) CAD image of semi-automated SEC stand designed to hold eight columns at once with sliding collection tube holder that allows liquid to drip either into 2 ml collection tubes, or to waste. (B) Photograph of stand connected to a Tecan Cavro syringe pump controlled by a Raspberry Pi. (C) Simoa comparison of CD9, CD63, CD81, ApoB-100, and albumin when SEC was performed on 16 samples of 1 ml plasma using either manual SEC (8 samples) or SEC on the automated device (8 samples). Each point is the average of two Simoa measurements (technical replicates).

## Discussion

In this work, we developed methods to enrich EVs from both lipoproteins and free proteins in plasma based on our ability to measure proteins associated with these different components using ultrasensitive assays. First, we developed and validated a Simoa assay for ApoB-100. We then combined this assay with previously developed Simoa assays for the tetraspanins CD9, CD63, and CD81, as well as albumin (Ter-Ovanesyan et al., 2021; Norman et al., 2021). With these assays in place, we were able to quantify EVs, free proteins, and lipoproteins from the same sample on one experimental platform. Using this approach, we assessed different ways of separating EVs from lipoproteins with the aim of developing improved EV isolation methods.

Plasma contains several types of lipoproteins with varying protein and lipid compositions. Although there is not a single present on all lipoproteins, we chose to measure ApoB-100, as it is a protein component of several lipoproteins (such as LDL, IDL, and VLDL) that overlap in size with EVs (Simonsen, 2017; Johnsen et al., 2019). We evaluated the possibility that SEC using resins with three different pore sizes might separate EVs from ApoB-100-containing lipoproteins using our platform. We previously used our tetraspanin and albumin Simoa assays to directly compare EV yield and free protein contamination for different SEC resins (Ter-Ovanesyan et al., 2021). Here, we used a similar approach to compare EV yield and lipoprotein contamination by including the ApoB-100 assay and found that we were unable to effectively separate tetraspanins from ApoB-100 by SEC. We also used our Simoa assays to evaluate DGC and showed that this technique enables good separation of tetraspanins from ApoB-100 and albumin; however, since DGC requires an ultracentrifuge, is low throughput, and time-intensive, it is not suitable for clinical samples.

We used our assays to develop novel methods for separating EVs from lipoproteins. A previous study described DMC columns that deplete lipoproteins by combining SEC using Sepharose CL-4B with a second bottom layer of cation exchange resin (Van Deun et al., 2020). We modified DMC to include the higher yield Sepharose CL-6B resin and demonstrated depletion of most of the ApoB-100, although at the cost of some EV depletion. To improve the ratio of EVs to ApoB-100 and albumin, we developed a new method that combines a top layer of Sepharose CL-6B with a bottom layer of both cation exchange resin and a multimodal chromatography resin called Capto Core 700. These ‘Tri-Mode mixed-mode Chromatography’, or TMC columns, produced EV preparations of higher purity relative to SEC columns in terms of both their lower albumin and lipoprotein content. As the multimodal chromatography resin binds free proteins but not EVs, the TMC columns reduce the co-elution of free protein with EVs.

This work presents a framework for quantitatively comparing EV isolation methods. There is not a single optimal way to isolate EVs because the purification method must be matched to the application; therefore, it is crucial to have effective ways of comparing both the yield and purity of different isolation methods. We developed TMC columns for applications where EVs of very high purity are needed and optimized these columns for EV purification from plasma using our Simoa assays. We envision these columns will be particularly useful for EV biomarker discovery using proteomics, where EV contamination with lipoproteins and free proteins prevents deep coverage (Smolarz et al., 2019). A recent study using a three-step protocol (polyethylene glycol precipitation followed by iohexol gradient fractionation and SEC) to enrich EVs from 1 ml plasma reported the detection of 250 proteins (Zhang et al., 2020). Another study reported the detection of 1187 proteins from plasma using ultracentrifugation, density gradient, and then SEC; the starting volume in that study was 40–80 ml plasma (Karimi et al., 2018). Using TMC columns, we were able to measure the plasma EV proteome using an easy, single-step isolation protocol and detect 780 proteins using a 1-ml sample. By also building an automated device for running columns in parallel, we demonstrate a path toward using column-based methods for clinical samples. Future iterations of the device will further increase the sample throughput. Taken together, the methods we developed will contribute to the realization of EV profiling in molecular diagnostics.

## Methods

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
      <td>Biological sample (human)</td>
      <td>Plasma</td>
      <td>BioIVT</td>
      <td>Cat#HUMANPLK2PNN</td>
      <td>Pooled gender, K2EDTA</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CD9 (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab263024</td>
      <td>Simoa capture (0.031 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CD9 (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab58989</td>
      <td>Simoa detector (0.06 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CD63 (mouse monoclonal)</td>
      <td>R&amp;D Systems</td>
      <td>Cat# MAB5048</td>
      <td>Simoa capture (0.031 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CD63 (mouse monoclonal)</td>
      <td>BD</td>
      <td>Cat# 556019RRID: AB_396297</td>
      <td>Simoa detector (0.0435 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CD81 (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab79559</td>
      <td>Simoa capture (0.031 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CD81 (mouse monoclonal)</td>
      <td>BioLegend</td>
      <td>Cat# 349502RRID: AB_10643417</td>
      <td>Simoa detector (0.0435 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Human Serum Albumin DuoSet ELISA</td>
      <td>R&amp;D Systems</td>
      <td>Cat# DY1455</td>
      <td>Simoa capture (0.031 μg per assay) and detector (0.002 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-ApoB (mouse monoclonal)</td>
      <td>R&amp;D Systems</td>
      <td>Cat# mab4124RRID:AB_2057095</td>
      <td>Simoa capture (0.031 μg per assay)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-ApoB (mouse monoclonal)</td>
      <td>R&amp;D Systems</td>
      <td>Cat# mab41242</td>
      <td>Simoa detector (0.08 μg per assay)</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CD9</td>
      <td>Abcam</td>
      <td>Cat# ab152262</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CD63</td>
      <td>Origene</td>
      <td>Cat# TP301733</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CD81</td>
      <td>Origene</td>
      <td>Cat# TP317508</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Albumin</td>
      <td>Abcam</td>
      <td>Cat# ab201876</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Purified ApoB-100 Standard</td>
      <td>Origene</td>
      <td>Cat# BA1030</td>
      <td>Protein standard for Simoa</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sepharose CL-2B</td>
      <td>Cytiva</td>
      <td>Cat# 17014001</td>
      <td>Resin for SEC</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sepharose CL-4B</td>
      <td>Cytiva</td>
      <td>Cat# 17015001</td>
      <td>Resin for SEC</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sepharose CL-6B</td>
      <td>Cytiva</td>
      <td>Cat# 17016001</td>
      <td>Resin for SEC</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fractogel EMD SO3- (M)</td>
      <td>MilliporeSigma</td>
      <td>Cat# 1168820100</td>
      <td>Resin for DMC/TMC</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Capto Core 700 multimodal chromatography resin</td>
      <td>Cytiva</td>
      <td>Cat# 17548102</td>
      <td>Resin for TMC</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Econo-Pac Chromatography Columns</td>
      <td>Bio-Rad</td>
      <td>Cat # 7321010</td>
      <td>Empty columns</td>
    </tr>
  </tbody>
</table>

### Human samples

Pooled human plasma (collected in K2 EDTA tubes) was ordered from BioIVT. Plasma was thawed at room temperature and centrifuged at 2000 × g for 10 min. The supernatant was filtered through a 0.45-μm Corning Costar Spin-X centrifuge tube (MilliporeSigma) at 2000 × g for 10 min. For all direct comparison experiments, plasma was first pooled and 1 ml used per EV isolation.

### Simoa assays

Simoa assays for CD63, CD81, and albumin were performed as previously described (Ter-Ovanesyan et al., 2021; Norman et al., 2021). Due to antibody availability, CD9 ab263024 (Abcam) was used as a capture antibody instead of ab195422 (Abcam). For ApoB-100, mab4124 (R&D Systems) was used as the capture antibody, mab41242 (R&D Systems) was used as the detector antibody, and purified ApoB-100 BA1030 (Origene) was used as a standard. For SEC, onboard dilution was performed with 4× dilution for each of the assays, with an additional 4× off-board dilution for CD9 and 10× off-board dilution for ApoB-100. For measuring protein levels in total plasma, each protein was measured with 4× onboard dilution and three additional off-board dilutions: for CD9 – 40×, 80×, and 160×; for CD63 and CD81 – 3×, 9×, and 27×; for albumin – 100×, 3000×, and 9000×; and for ApoB-100 – 100×, 300×, and 900× dilution. All samples were measured in duplicate using the HD-X analyzer (Quanterix). Tetraspanins were measured with a two-step assay, while albumin and ApoB-100 were measured with a three-step assay. Average Enzyme per Bead (AEB) values were calculated by the HD-X software.

### Calculation of EV yield and purity

EV yield was calculated for EV isolation from plasma for SEC (fractions 7–10), DMC (fractions 9–12), or TMC (fractions 9–12). Levels of the three tetraspanins CD9, CD63, and CD81 in the designated EV fractions and their levels in total plasma were measured using Simoa. The yield of each tetraspanin was calculated by dividing its level in the EV fraction by its level in total plasma. The total EV yield was then calculated as the average of the three ratios. Relative EV yield for comparing multiple conditions was calculated by dividing the EV yield of each condition by the highest EV yield of all the conditions. The purity of EVs with respect to free proteins or lipoproteins was determined by dividing the relative EV yield by relative levels of albumin or ApoB-100 in the EV fractions.

### Validation of ApoB-100 Simoa assay

Antibodies were first cross-tested using serial dilutions of purified protein standard. The antibody pair with the highest signal-to-background ratio was chosen. The assay was validated using dilution linearity and spike and recovery experiments. Plasma samples were diluted serially in the assay-specific buffer, a dilution factor in the middle of the linear range was chosen to be the dilution factor for the spike and recovery test. Three protein concentrations of purified ApoB-100 were spiked into the diluted plasma from the top calibrator used in the calibration curve. All recoveries fell in the range of 85–100% (Table 1). The assay validation was conducted using commercially available plasma samples (BioIVT).

### Preparation of columns

Sepharose CL-2B, Sepharose CL-4B, and Sepharose CL-6B resins (Cytiva) were washed with PBS in a glass bottle. The volume of resin was washed three times with an equal volume of PBS before use. Econo-Pac Chromatography columns (Bio-Rad) were packed with resin and a frit was inserted into the column above the resin. For all columns in Figures 4 and 5, each column was washed with 10 ml PBS (twice 5 ml at a time) prior to loading of sample. For SEC columns, resin was added until the bed volume (resin without liquid) reached 10 ml. For DMC columns, Fractogel EMD SO3- (M) (MilliporeSigma) was added as a bottom layer with 2 ml bed volume, and 10 ml of Sepharose CL-6B bed volume was added as a top layer. For TMC columns, a 2:1 by volume (of dry resin) mixture was prepared of Fractogel EMD SO3- (M) (MilliporeSigma) and Capto Core 700 (Cytiva) and 2 ml bed volume bottom layer was added to the column before 10 ml of Sepharose CL-6B bed volume was added as a top layer.

### Collection of column fractions

Sample (1 ml plasma) was loaded once PBS from wash had finished going through the column. Once the sample fully entered the column, 0.5 ml fractions were collected. PBS was then added in volumes equal to those being collected for one fraction (0.5 ml) or a set of four fractions (2 ml). In experiments where just the EV fractions were collected, fractions 7–10 were collected for SEC and fractions 9–12 were collected for DMC and TMC.

### Density gradient centrifugation

DGC was performed as previously described (Norman et al., 2021). Four layers of OptiPrep (iodixanol) were prepared and stacked in a 13.2-ml polypropylene tubes (Beckman Coulter) from bottom to top: 3 ml 40%, 3 ml 20%, 3 ml 10%, and 2 ml 5%. OptiPrep (MilliporeSigma) was diluted in a solution of 0.25 M sucrose (MilliporeSigma) and pH 7.4 Tris–EDTA (MilliporeSigma). Sample (1 ml plasma) was loaded on top of the gradient and centrifuged at 100,000 RCF in an SW 41 Ti swinging bucket rotor for 18 hr at 4°C using a Beckman Coulter Optima XPN-80 ultracentrifuge. After centrifugation, fractions were removed from the top 1 ml at a time. For the DGC, SEC, and DGC–SEC comparisons, fraction 10 was analyzed (directly for the DGC condition, or then run through an SEC column for DGC–SEC condition).

### Negative staining and transmission electron microscopy (TEM) imaging

Carbon-coated grids (CF-400CU, Electron Microscopy Sciences) were glow discharged, and 5 μl of the sample was absorbed to the grid for 1 min. Excess sample was blotted with a Whatman paper. The grid was then stained with 5 μl 1% uranyl acetate for 15 s and excess stain was blotted. Samples were imaged on a JEOL 1200EX – 80 kV transmission electron microscope with an AMT 2k CCD camera.

### Mass spectrometry

EVs were isolated from 1 ml plasma using TMC columns with a 2-ml bed volume bottom layer of 2:1 of Fractogel EMD SO3- (M) (MilliporeSigma) to Capto Core 700 (Cytiva) and 10-ml bed volume top layer of Sepharose CL-6B (Cytiva). EVs were concentrated using Amicon Ultra-2 centrifugal 10 kD filter (MilliporeSigma). After concentration, EV protein was precipitated by adding 9 volumes of 100% ethanol to 1 volume of EVs, vortexing and leaving at −20°C for 30 min. Sample was then centrifuged at 16,000 × g for 15 min at 4°C. Supernatant was removed and pellet was left to air dry for 10 min. Sample was then sent to Bruker for proteomics analysis. Sample was resuspended in 50 mM triethylammonium bicarbonate (Thermo Fisher Scientific) and digested for 2 hr at 50°C using Trypsin Platinum (Promega) using 1:50 Trypsin to sample ratio by mass. After evaporating solution in a Vacufuge (Eppendorf) ar 45°C, sample was resolubilized in 10 μl 0.1% formic acid (Thermo Fisher Scientific). Next, 1.5 μl of sample was injected into C18 tips (Evosep) and eluted into a 25-cm length 150 μm internal diameter PepSep analytical column packed with 1.5 μm C18 beads (Dr. Maisch). Sample was eluted into a Bruker timsTOF HT. A gradient from 3% of to 28% of 0.1% formic acid in acetonitrile at 63 min was then increased to 85% until 80 min. Data were analyzed using Spectronaut 17 (Biognosys) software for data-independent acquisition (DIA). A false discovery rate of 1% was used at both the peptide and protein levels. Keratin proteins (likely contaminants) were manually removed from the list.

### SEC stand and automated device

Experiments in Figure 5 were performed using the automated SEC stand connected to a Cavro XLP 6000 syringe pump (Tecan) controlled by a Raspberry Pi 4 model B. CAD files and instructions for assembly are provided in the Supplementary Information. Code for Raspberry Pi is deposited at: https://github.com/Wyss/automated-chromatography/, (Kalish and Tat, 2023). All other SEC experiments were performed using custom SEC stand described previously (Ter-Ovanesyan et al., 2021).
