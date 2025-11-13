# Visualization and functional dissection of coaxial paired SpoIIIE channels across the sporulation septum

## Authors

- Jae Yen Shin<sup>1</sup>
- Javier Lopez-Garrido<sup>2</sup>
- Sang-Hyuk Lee<sup>1</sup>
- Cesar Diaz-Celis<sup>1</sup>
- Tinya Fleming<sup>2</sup>
- Carlos Bustamante<sup>1</sup> †
- Kit Pogliano<sup>2</sup> †

### Affiliations

1. Howard Hughes Medical Institute, University of California, Berkeley Berkeley United States
2. Division of Biological Sciences University of California, San Diego La Jolla United States
3. Jason L Choy Laboratory of Single Molecule Biophysics Howard Hughes Medical Institute, University of California, Berkeley Berkeley United States
4. QB3 Institute University of California, Berkeley Berkeley United States
5. Kavli Energy NanoSciences Institute University of California, Berkeley Berkeley United States

† Corresponding author

## Abstract

SpoIIIE is a membrane-anchored DNA translocase that localizes to the septal midpoint to mediate chromosome translocation and membrane fission during Bacillus subtilis sporulation. Here we use cell-specific protein degradation and quantitative photoactivated localization microscopy in strains with a thick sporulation septum to investigate the architecture and function of the SpoIIIE DNA translocation complex in vivo. We were able to visualize SpoIIIE complexes with approximately equal numbers of molecules in the mother cell and the forespore. Cell-specific protein degradation showed that only the mother cell complex is required to translocate DNA into the forespore, whereas degradation in either cell reverses membrane fission. Our data suggest that SpoIIIE assembles a coaxially paired channel for each chromosome arm comprised of one hexamer in each cell to maintain membrane fission during DNA translocation. We show that SpoIIIE can operate, in principle, as a bi-directional motor that exports DNA.

## Introduction

The transport of DNA across cellular membranes is an essential part of bacterial processes such as transformation and conjugation (Errington et al., 2001; Burton and Dubnau, 2010). A paradigmatic example is the segregation of chromosomes that are trapped in the septum during cell division, which requires specialized DNA translocases of the SpoIIIE/FtsK/HerA protein superfamily. The members of this superfamily use the energy of ATP to translocate DNA and peptides through membrane pores (Bath et al., 2000; Iyer et al., 2004; Tato et al., 2005; Burton and Dubnau, 2010). SpoIIIE and FtsK contain an N-terminal domain that anchors the protein to the septal membrane (Wu and Errington, 1997; Wang and Lutkenhaus, 1998; Yu et al., 1998), a poorly conserved linker domain, and a cytoplasmic motor domain with ATPase activity that is responsible for DNA translocation. The motdata-left-gapor domain consists of three subdomains: α, β, and γ (Massey et al., 2006). α and β form the core ATPase domain and are responsible for chromosome translocation, while the γ subdomain regulates translocation directionality (Pease et al., 2005; Ptacin et al., 2008).

During Bacillus subtilis sporulation, an asymmetrically-positioned septum creates two daughter cells of different size: the bigger mother cell and the smaller forespore. SpoIIIE is made before polar septation (Foulger and Errington, 1989) and localizes to the leading edge of the constricting septum (Fleming et al., 2010; Fiche et al., 2013) (Figure 1A). As the sporulation septum closes around the chromosome, SpoIIIE forms a stable focus at the septal midpoint (Wu and Errington, 1997; Fleming et al., 2010), where it mediates two key events. First, it keeps the mother cell and forespore septal membranes separated in the presence of a septum-trapped chromosome, playing an important role in septal membrane fission (Liu et al., 2006; Fleming et al., 2010) (Figure 1). Second, it translocates the chromosome remaining in the mother cell (about 2/3 of its total length) to the forespore (Wu and Errington, 1994; Bath et al., 2000). This vectorial DNA translocation is dictated by the interaction of the γ domain with SpoIIIE recognition sequences (SRS) that are distributed in a skewed manner along the B. subtilis chromosome from the origin of replication towards the terminus (Figure 1) (Pease et al., 2005; Ptacin et al., 2008). It has been proposed that SpoIIIE exports DNA (Sharp and Pogliano, 2002; Ptacin et al., 2008) and that the interaction between the γ subdomain of SpoIIIE and the SRS favors either the selective assembly of SpoIIIE in the mother cell or, equivalently, the inactivation or disassembly of motor domains in the forespore (Sharp and Pogliano, 2002; Becker and Pogliano, 2007; Ptacin et al., 2008; Fiche et al., 2013).

![Figure 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig1-v1.jpg)

**Figure 1.:** (A) The sporulation septum traps the oriC-proximal region of the forespore chromosome in the forespore (F), the rest in the mother cell (MC). SpoIIIE (green) localizes at the leading edge of the constricting septum, and assembles a translocation complex at the septal midpoint. The SpoIIIE complex maintains separation of the daughter cell membranes in the presence of trapped DNA. The direction of translocation (white arrow) is determined by the orientation-specific interaction between the SpoIIIE γ domain and the skewed chromosomal recognition sequences known as SRS (black arrowheads on the chromosome, indicating the direction that SpoIIIE motor domains move on the DNA). Engulfment commences during DNA translocation, producing a curved septum and movement of the mother cell membrane around the forespore. (B) The aqueous channel model for SpoIIIE, showing two chromosome arms. Green represents the SpoIIIE channels formed by motor domains, grey the transmembrane domains, and red the membrane. (C) The paired channel model for SpoIIIE, in which each chromosome arm passes through a proteinaceous channel with subunits in both cells.

Structural studies of the motor domains of B. subtilis SpoIIIE (Cattoni et al., 2013; 2014) and of Escherichia coli and Pseudomonas aeruginosa FtsK (Massey et al., 2006; Löwe et al., 2008) reveal that each assembles a hexamer with a central channel large enough to accommodate one dsDNA molecule. Cell biological studies have shown that both arms of the circular chromosome are translocated simultaneously (Burton et al., 2007), suggesting that the translocation complex is made of at least two SpoIIIE hexamers, one for each chromosome arm. However, it remains unclear how SpoIIIE is organized at the septum. One model is that DNA is translocated through an aqueous membrane pore (Figure 1B) (Wu and Errington, 1997; Fiche et al., 2013). According to this model, the transmembrane domains of SpoIIIE simply localize the complex to the septum, and it has been proposed that tension generated during DNA translocation generates an asymmetric complex with hexameric motor domains oriented towards the mother cell cytoplasm (Fiche et al., 2013). A second model proposes that SpoIIIE transmembrane domains in opposite septal membranes pair to form DNA-conducting channel that traverses both septal membranes, with the motor domains in the respective cytosols (Figure 1C) (Liu et al., 2006; Burton et al., 2007; Fleming et al., 2010). This model postulates that assembly of the paired channel mediates septal membrane fission and that the assembled channel maintains separation of daughter cell membranes during DNA translocation (Liu et al., 2006; Fleming et al., 2010).

Here, we investigate the organization of the SpoIIIE DNA translocation complex in living cells. We developed a cell-specific protein degradation system that selectively removes SpoIIIE from each cell after polar septation and used this system with GFP tagging and quantitative PALM (qPALM) to investigate SpoIIIE architecture and function. We show that SpoIIIE forms a complex with approximately equal numbers of molecules in the mother cell and the forespore, enough to assemble at least two hexamers in each cell. Both the forespore and mother cell SpoIIIE subcomplexes are required to maintain septal membrane fission during DNA translocation. However, only the mother cell SpoIIIE is essential for chromosome translocation into the forespore. In the absence of the mother cell protein, forespore SpoIIIE translocates the chromosome out of the forespore, indicating that SpoIIIE exports DNA. Together our results are consistent with the paired channel model in which SpoIIIE assembles a DNA-conducting channel that spans the mother cell and forespore septal membranes. Moreover, we show that SpoIIIE can operate, in principle, as a bi-directional motor that exports DNA from a given cell compartment.

## Results

### Development of a cell-specific protein degradation system

To investigate the organization and the cell-specific function of SpoIIIE we developed a system that allows degradation of specific proteins selectively in the mother cell or forespore during sporulation. Our system is based on a method developed by Griffith and Grossman (2008) in which a heterologous SsrA tag from E. coli (SsrA*) is fused to the C-terminus of target proteins. The SsrA* tag is recognized by B. subtilis ClpXP protease only in the presence of the cognate SspB adaptor protein from E. coli (SspBEc). To achieve cell-specific degradation of SsrA*-tagged proteins during sporulation, we expressed sspBEc in a cell-specific manner by using promoters (PspoIIQ and PspoIID) dependent on the sigma factors σF and σE, which become active only in the forespore or in the mother cell, respectively, immediately after polar septation (Clarke et al., 1986; Rong et al., 1986; Londoño-Vallejo et al., 1997; Sharp and Pogliano, 2002) (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig2-v1.jpg)

**Figure 2.:** (A) Cell-specific protein degradation system (see text). Red indicates the cell membranes, green the target protein. F = forespore, MC = mother cell. (B) Fluorescence microscopy of GyrA-GFP-SsrA* (green) during sporulation, without degradation (strain JLG917), forespore degradation (F, JLG919) and mother cell degradation (MC, JLG1281). Membranes are stained with FM4-64 (red). Scale bar, 1 μm. (C and D) Quantification of the loss of GyrA-GFP-SsrA* fluorescence after degradation in the (C) mother cell and (D) forespore. No degradation controls express GyrA-GFP-SsrA* but not sspBEc (blue circles and diamonds). The ratio of the mean GFP intensity in the (C) mother cell/forespore (red squares) and (D) forespore/mother cell (red triangles) were calculated for sporangia with flat, slightly curved and engulfing septa 2.5 hr after the initiation of sporulation (t2.5). 25–66 sporangia were analyzed for each cell type.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig2-figsupp1-v1.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Cell-specific degradation of a σA-GFP-SsrA* fusion protein during sporulation. When sspBEc is not expressed (strain JLG247), GFP signal is detected in both forespore and mother cell. Expressison of sspBEc in the forepore (strain JLG261) leads to GFP disappearance in the forespore, while expression of sspBEc in the mother cell (strain JLG259) leads to GFP disappearance in the mother cell. Sporangia were harvested 2.5 h after resuspension (t2.5) and images of σA-GFP-SsrA* (green) and membrane (red) were taken. Membrane was stained with FM4-64 (red). Scale bar is 1 μm. (B and C) Quantification of the loss of σA-GFP-SsrA* fluorescence after degradation in the (B) mother cell and (C) forespore. No degradation controls express σA-GFP-SsrA* but not sspBEc (blue circles and diamonds). The ratio of the mean GFP intensity in the (B) mother cell/forespore (red squares) and (C) forespore/mother cell (red triangles) cell were calculated for sporangia with flat, slightly curved and engulfing at t2.5. 20–46 sporangia were analyzed for each cell type.

We first analyzed the cell-specific degradation of DNA gyrase subunit A (GyrA) by constructing a GyrA-GFP-SsrA* fusion protein. The GFP signal from this protein was initially detected in both the forespore and the mother cell (Figure 2B), but disappeared in the SspBEc–containing cell (Figure 2B). To estimate the degradation kinetics, we correlated loss of the GFP signal with the stages of engulfment, a phagocytosis like process that occurs during DNA translocation. Immediately after polar septation, the septum is first flat, then curved, and finally the mother cell membrane engulfs the forespore (Figure 1A, Figure 2—figure supplement 1). Quantification of GFP fluorescence intensity showed that the protein was lost at similar rates in the cell expressing sspBEc (forespore or mother cell) (Figure 2C,D). In both cases, the fluorescence decreased close to zero when sporangia entered engulfment, indicating that most GyrA-GFP-SsrA* was degraded at this sporulation stage (Figure 2C,D). Similar results were obtained after cell-specific degradation of a σA-GFP-SsrA* fusion protein (Figure 2—figure supplement 2). Thus, cell-specific expression of sspBEc provides a rapid and efficient way to selectively degrade SsrA*-tagged proteins in the mother cell or in the forespore.

### Cell-specific degradation reveals that the translocation complex contains SpoIIIE molecules in each cell

SpoIIIE translocates DNA across a septum comprised of two membranes, yet it remains unclear if the DNA translocation complex contains SpoIIIE monomers in both the mother cell and the forespore or just one cell. To address this question we used the cell-specific degradation system described above. If SpoIIIE assembles in one cell, then triggering degradation in that cell would cause the focus to disappear, while triggering degradation in the other cell would have no effect. However, if the translocation complex is present in both cells, then degradation in only one cell would leave SpoIIIE monomers in the other cell, and the focus would be expected to persist until SpoIIIE was degraded in both cells simultaneously. The SpoIIIE-GFP-SsrA* fusion protein, as expected, formed a bright focus at the septal midpoint and persisted around the forespore during engulfment (Figure 3A). When SpoIIIE was degraded in either cell, more than 80% of the sporangia still contained a SpoIIIE focus. However, when SpoIIIE was degraded in both cells simultaneously just 25% of sporangia retained a focus, and these were faint and present only in sporangia with flat and curved septa (Figure 3A), which are at early stages of sporulation.

![Figure 3.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig3-v1.jpg)

**Figure 3.:** (A) Visualization of SpoIIIE-GFP-SsrA* (green) and FM4-64 stained membranes (red) by deconvolution fluorescence microscopy at t2.5. SpoIIIE was not degraded (None, JLG451) or degraded in the forespore (F, JLG452); mother cell, (MC, JLG453) or both (F and MC, JLG454). Percent sporangia with detectable SpoIIIE foci and the number (n) of scored sporangia are indicated for each strain. Strains containing SpoIIIE-GFP-SsrA* without SspBEc or expressing SspBEc with untagged-SpoIIIE supported wild-type sporulation, chromosome translocation and membrane fission (Supplemental data). Scale bar, 1 μm. (B) Fluorescence intensity of SpoIIIE-GFP foci without degradation (green) or after degradation in the forespore (red) or mother cell (blue) in sporangia with flat, slightly curved and engulfing septa. The mean focus intensity of sporangia with flat septa in the non-degradation strain was normalized to 100. Each dot represents the intensity of a single focus; black dotted lines represent the mean of each data set. Between 35 and 95 foci were analyzed for each data set. (C) Model for SpoIIIE organization at the septal midpoint based on cell-specific degradation. The translocation complex contains SpoIIIE molecules on both sides of the septum so cell-specific degradation will only remove a fraction of the molecules. Degradation in both cells will remove all molecules.

Quantification of focus intensity after degradation in either cell showed that the average focus intensity was reduced by ∼50% in sporangia with curved and engulfing septa (Figure 3B). After degradation in the forespore, cells with flat septa showed a detectable reduction of GFP intensity (Figure 3B), suggesting that SpoIIIE degradation starts slightly faster in the forespore, likely reflecting the earlier activation of σF vs σE. These results indicate that cell-specific degradation of SpoIIIE commences shortly after polar septation and that the SpoIIIE translocation complex is comprised of monomers with C-terminal motor domains (and the SsrA* tags) in the cytosol of each cell (Figure 3C). They also suggest that approximately half of the SpoIIIE molecules in the septal focus are in the mother cell and half in the forespore.

### Direct visualization of SpoIIIE paired channels by PALM

If SpoIIIE assembles a channel with subunits located in each cell, then super-resolution microscopy might show a SpoIIIE cluster in each cell. However, examination of PALM images revealed mainly single foci (Figure 4A), consistent with previous reports (Fleming et al., 2010; Fiche et al., 2013). Most likely this observation reflects the fact that the distance between the forespore and mother cell membranes at the septum is just ∼20 nm (Tocheva et al., 2013), which is close to the limit of resolution via PALM (∼25 nm). Consistent with this idea, occasionally we observed sporangia with what appear to be two clusters of molecules aligned across the septum (Figure 4A, right column). To improve the ability to resolve these two subcomplexes, we used a B. subtilis mutant that retains thick septal peptidoglycan because it lacks the mother cell transcription factor (σE) that controls septal thinning, the first step in engulfment (Figure 4B). In this ΔσE strain, the distance between the mother cell and forespore septal membranes is ∼40 nm, more than twice the distance of wild type (Illing and Errington, 1991), potentially allowing resolution of the SpoIIIE subcomplexes in each cell by PALM. We therefore introduced SpoIIIE-tdEOS into the ΔσE strain. As expected (Pogliano et al., 1999), this strain did not initiate engulfment or block the second potential division septum, producing a high number of disporic sporangia (Figure 4C, Figure 4—figure supplement 1) without impairing DNA translocation (Figure 4—figure supplement 2).

![Figure 4.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-v1.jpg)

**Figure 4.:** (A) PALM image of single focus and a rare dual focus of SpoIIIE-Dendra2 in wild type B. subtilis (TCF25), with FM5-95 stained membranes (white). The bottom PALM images are zoomed in from the yellow boxes. Bar is 500 nm and 50 nm for overlaid and PALM images, respectively. Membrane is diffraction-limited image. (B) Schematic diagram of septal thinning. (I) After septation, septal peptidoglycan is degraded by a complex containing the SpoIID, SpoIIM and SpoIIP proteins (pacman) and the second potential division site is blocked. (II) Elimination of SpoIIDMP in the ΔspoIIDMP (spoIID, spoIIM, spoIIP) strain inhibits septal thinning without impairing DNA segregation. (III) Elimination of σE in the ΔσE (spoIIGB) strain inhibits septal thinning and produces disporic cells without impairing DNA segregation. (C) PALM images of SpoIIIE-tdEos in ΔσE strain (JS03). Classification of PALM images as dual foci or single foci were defined according to the parameters of our cluster analysis. Scale bar is 500 nm and 50 nm for overlaid and PALM images, respectively. Membrane is diffraction-limited image. (D) PALM images of SpoIIIE-tdEos in ΔSpoIIDMP strain (JLG571). The diffraction-limited images of the membranes (white) and the DNA (green) were obtained by staining with FM5-95 and DAPI, respectively. The relative forespore DAPI intensity was ∼25% in both sporangia. SpoIIIE dual foci are shown in the left panels. In-gel fluorescence and western blots of the different SpoIIIE fusion proteins used here can be found in Figure 4—figure supplement 7.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Mutation in σE produces a much higher percentage of disporic cells compared to the σE+ strain PY79. More than 700 cells were classified per strain. The strains used were KP161, TCF25 and JS03.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Mutation in σE does not impair DNA translocation. Forespores show brighter DNA signal (single arrowhead) at t2.5 compared to t1.75 of sporulation time showing chromosome translocation from the mother cell into the forespore. ΔσE cells expressing SpoIIIE fused to tdEos (JS03) were stained with DAPI and FM5-95 to visualize DNA (Green) and membrane (red), respectively. DAPI signal was false-colored green for a better contrast. (B) Quantification of DNA translocation at different sporulation times. The amount of DNA in the forespore increases as sporulation progresses (from ∼60–100%, inset). Our PALM experiments using ΔσE strains (Figures 4, 5) were done at t1.75 to maximize the percentage of cells are actively translocating DNA. Error bar represents standard error of the mean from 20 cells for each of the time points. (C) Cells were sporulated at 37°C and samples were taken at indicated times and stained with DAPI and FM5-95 to visualize DNA and membrane (red), respectively. The amount of DAPI (labeled-DNA) in the forespore increased from t1.5 to t2 in ΔσE sporangia expressing wild type SpoIIIE (SpoIIIEWT) fused to tdEos (JYS03), indicating that the forespore received the chromosomal complement from the mother cell. In contrast, ΔσE cells expressing SpoIIIE ATPase mutant (SpoIIIEATP−) fused to tdEos (JYS04) did not translocate DNA. SpoIIIEWT fused to Dendra2 (JYS00) also translocated DNA in ΔσE strain. Altogether, these results indicate that SpoIIIE translocates chromosome during sporulation in ΔσE strain and the fusion protein does not impair the ability of this translocation.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp3-v1.jpg)

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** Classification of monosporic and disporic sporangia in relation to the presence of either single focus or dual foci at the sporulation septum of cells expressing either SpoIIIE fused to tdEos (JS03) or Dendra2 (JS00) in the ΔσE strain.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** To demonstrate that SpoIIIEWT dual foci (Figure 4) are observed when the chromosome is trapped in the septum and discard that are only at septa where chromosome transport is complete we imaged SpoIIIEATP− fused to tdEos by PALM. Single mutation G467S in the conserved region of the SpoIIIE ATPase motor domain impairs DNA translocation without affecting SpoIIIE foci assembly, and the forespore chromosome remains trapped in the septum (Sharp and Pogliano, 1999; Fleming et al., 2010). qPALM shows that SpoIIIEATP− also assembles into dual foci (PALM: left panels and, first and second right panels) and single foci (third right panel) similar to the SpoIIIEWT (Figure 4). As expected sporangia expressing SpoIIIEATP− did not translocate DNA (Figure 4—figure supplement 2C).

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp6-v1.jpg)

**Figure 4—figure supplement 6.:** To demonstrate that dual foci represent SpoIIIE complexes that are actively translocating DNA, we imaged SpoIIIEWT in a different Bacillus strain, spoIIDMP triple mutant strain, which mantains a thick sporulation septum due to the inhibition of septal thinning (Pogliano et al., 1999; Abanes De Mello et al., 2002; Chastanet and Losick, 2007; Gutierrez et al., 2010). In contrast to the ΔσE mutant, the completion of the second polar septum is inhibited in the spoIIDMP triple mutant, leading to the formation of fewer disporic sporangia. This feature allows the estimation of the degree of chromosome translocation using DNA-specific dyes and measuring the dye-intensity in the forespore vs the total intensity (forespore plus mother cell), a standard procedure in the field (Becker and Pogliano, 2007; Ptacin et al., 2008). The relative forespore DAPI intensity of sporangia showing dual foci in the spoIIDMP mutant ranged between 0.1 and 0.32, suggesting that they were actively translocating DNA. These observations suggest that dual foci represent the organization of the SpoIIIE complex during the process of DNA translocation. Criteria for complete and incomplete DNA translocation is described in the chromosome translocation section of the results and in Figure 7—figure supplement 1.

![Figure 4—figure supplement 7.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig4-figsupp7-v1.jpg)

**Figure 4—figure supplement 7.:** Our single SpoIIIE molecule quantification relies on the fluorescent protein fused to SpoIIIE. Therefore, it is crucial that all SpoIIIE molecules are fused to the fluorescent protein and also all the fluorescent proteins fused to SpoIIIE. (A) Fluorescent proteins (GFP, Dendra2 and tdEos) fused to SpoIIIE migrate as a single band in 7% semi-denaturing in-gel fluorescence PAGE (Drew et al., 2006). As expected the tandem dimer Eos (tdEos) fusion proteins migrate slightly higher than the GFP and the Dendra2 fusion proteins. (B) SpoIIIE fused to fluorescent proteins migrates as a higher molecular weight compared to the native SpoIIIE (lanes 2 and 3), indicating that all the SpoIIIE molecules are fused to the fluorescent proteins. The molecular weight of the fusion proteins corresponded to the in-gel fluorescence. The faint band at ∼130 kDa is unspecific. (C) Total protein visualized by Coomassie-Blue staining.

Visualization of SpoIIIE-tdEOS via PALM in this strain showed that 39% of septa contained a medial SpoIIIE assembly comprised of two separate subcomplexes of molecules (hereafter called ‘dual foci’, Figure 4C,D). Most dual foci were aligned across the division septum and a few were slightly tilted (Figure 4C). The average distance between the centers of each focus was 55 nm (Figure 5A,B, Figure 5—figure supplement 1). Electron cryotomography shows that before septal thinning the cytoplasmic faces of the septum are separated by ∼40 nm (Tocheva et al., 2013), suggesting that the centers of each resolved subcomplexes of SpoIIIE lie in separate cells. Dual foci were also observed in 26% of sporangia when septal thinning was blocked by the absence of the SpoIID, SpoIIM and SpoIIP proteins that degrade septal peptidoglycan (Figure 4B,D) (Pogliano et al., 1999; Abanes De Mello et al., 2002; Chastanet and Losick, 2007; Gutierrez et al., 2010). Thus using two strains with thick septa allowed visualization of SpoIIIE foci comprised of molecules in both the mother cell and forespore (Figure 4).

![Figure 5.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig5-v1.jpg)

**Figure 5.:** (A) The distances (D) between the centers of each cluster from SpoIIIE-tdEos dual foci in ΔσE strain (JYS03). The average distance between clusters, indicated by the main peak value of the kernel density estimator (blue line), is 55 nm. (B) Schematic diagram of SpoIIIE (blue) at the division septum in ΔσE strain. To estimate the thickness of the peptidoglycan (PG) we subtracted twice the width of the lipid bilayer (3 nm; Lewis and Engelman, 1983) and twice the height of SpoIIIE (6 nm), based on the FtsK crystal structure (Massey et al., 2006) from 55 nm, to give 37 nm. FP, fluorescent protein. (C) Dimensions of single SpoIIIE-Dendra2 foci and resolved clusters in dual foci. Focus widths in foci parallel (x) and perpendicular (y) to the septum were calculated as described in supplementary methods. For single foci the parallel- and perpendicular-width (in nm) are 86 ± 10 and 94 ± 12 respectively, for dual foci, the forespore proximal cluster is 64 ± 11 and 57 ± 8, the mother cell proximal cluster 77 ± 12 and 52 ± 7. Error bars, standard deviation from Nsingle = 221, Ndual foci = 51. (D) Distribution of the number of SpoIIIE-Dendra2 molecules determined by qPALM at the septum in the mother cell, in the forespore and in both. Data (blue bars) are represented by Kernel Density Estimator (red solid lines). Mean and standard deviations from Nfoci = 51 are shown. More details about qPALM and the algorithm employed for quantification can be found in ‘Materials and methods’.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The main peak value of the kernel density estimator (blue line) is 68 nm, which is slightly higher than the measurement with SpoIIIE-tdEos strain (55 nm, Figure 5A), most likely because Dendra2 is dimmer and thus its localization is less accurate than mEos2.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (Top) Approximate analytic solution of the optimal τc agrees well with the exact solution obtained from full stochastic simulations. The experimental time tF and the number of molecules Nmol were varied, whereas the kinetic rates were fixed to the rates of Dendra2 obtained from in vitro single-molecule experiments (Lee et al., 2012). (Bottom) Photoactivation time of Dendra2 fused to SpoIIIE using Fermi-photoactivation scheme corresponding to the Figure 5D. Details about the quantification of the number of molecules using PALM can be found in ‘Materials and methods’.

We reasoned that if the 61% of septa that showed single foci in the ΔσE strain (Figure 4C, Figure 4—figure supplement 3) were unresolved dual foci, they should be elongated across the septum compared to each focus in septa with dual-foci. We therefore determined the width of the SpoIIIE clusters in single foci and in each resolved subcomplexes from dual foci both perpendicular and parallel to the septum. On average, the width perpendicular to the septum of the single foci (94 nm) was ∼1.7× larger than that of each individually resolved cluster in dual foci (54 nm), while their width parallel to the septum was similar (∼80 nm, Figure 5C), suggesting that single foci are unresolved dual foci. Consistent with this hypothesis, PALM images of SpoIIIE-Dendra2 showed a larger (83%) number of septa with a single focus than SpoIIIE-tdEOS (Figure 4—figure supplement 4), as expected for a dimmer fluorescent protein with reduced localization accuracy (Lee et al., 2012).

### Dual foci are observed when DNA traverses the septum

We performed two experiments to determine if the dual foci represented the architecture of the SpoIIIE complex during or after DNA translocation. First, we examined PALM images of the translocation-deficient SpoIIIE ATPase mutant (G467S; hereafter SpoIIIEATP−) in ΔσE background. This strain showed dual foci in 23% of septa (Figure 4—figure supplement 5), suggesting that dual foci represent the structure of SpoIIIE when it assembles around the trapped chromosome, not after DNA translocation. Second, we used PALM to localize wild type SpoIIIE-tdEOS in ΔSpoIIDMP strain in sporangia stained with both the membrane stain FM5-95 and the DNA stain DAPI, so we could discriminate between cells in which DNA translocation was ongoing and those in which it was complete. Quantification of the forespore DNA relative to the total (mother cell plus forespore), demonstrated that 81% of sporangia with dual foci had not completed DNA translocation (Figure 4D, Figure 4—figure supplement 6). These data suggest that dual foci represent the SpoIIIE DNA translocation complex.

### The mother cell and forespore subcomplexes have similar numbers of SpoIIIE molecules

We next used qPALM to determine the relative numbers of SpoIIIE molecules in each cell in ΔσE sporangia with resolved dual foci, applying an algorithm recently developed in our laboratory (Lee et al., 2012; see ‘Materials and methods’ for details). We detected, on average, 34 ± 17 molecules in the entire dual foci, consistent with the number of molecules of wild type SpoIIIE and SpoIIIEATP− in strains with thin septa (Figure 5D, Table 1). We detected 19 ± 11 and 15 ± 8 molecules in the mother cell- and forespore-proximal subcomplexes from dual foci, respectively. Thus each subcomplex contains approximately half the number of SpoIIIE molecules detected in the entire dual focus, consistent with our quantification of the fluorescence intensity after cell-specific degradation of SpoIIIE-GFP (Figure 3B, Table 1). Together these results suggest that the SpoIIIE translocation complex consist of two complexes containing equivalent numbers of SpoIIIE molecules, one in the mother cell and one in the forespore.

**Table 1.**
 Summary of SpoIIIE quantification obtained by qPALM and diffraction-limited images in the wild type strain, cell-specific degradation system and the thick septum strain (ΔσE)


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">SpoIIIE-dendra2 quantification by qPALM, absolute numbers</th>
      <th colspan="3">SpoIIIE-GFP intensity, %</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="2">Wild type</th>
      <th colspan="3">ΔσE (dual foci)</th>
      <th colspan="3">Cell-specific degradation</th>
    </tr>
    <tr>
      <th>Strain</th>
      <th>SpoIIIEWT</th>
      <th>SpoIIIEATP−</th>
      <th>MC + F</th>
      <th>MC</th>
      <th>F</th>
      <th>None</th>
      <th>F</th>
      <th>MC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mean (SD)</td>
      <td>31 (18)</td>
      <td>31 (14)</td>
      <td>34 (17)</td>
      <td>19 (11)</td>
      <td>15 (8)</td>
      <td>100 (29)</td>
      <td>51 (25)</td>
      <td>52 (31)</td>
    </tr>
    <tr>
      <td>N</td>
      <td>91</td>
      <td>128</td>
      <td>51</td>
      <td>51</td>
      <td>51</td>
      <td>72</td>
      <td>66</td>
      <td>123</td>
    </tr>
  </tbody>
</table>

### Septal membrane fission is reversible and requires SpoIIIE in both cells

The last step of cell division is a membrane fission event that divides the septal membrane to render two physically separated daughter cells. During sporulation, septal membrane fission occurs in the presence of a trapped chromosome (Burton et al., 2007; Fleming et al., 2010) and depends on the assembly of a stable SpoIIIE translocation complex (Fleming et al., 2010). It has been proposed that SpoIIIE mediates membrane fission by assembling a paired channel spanning both septal membranes (Liu et al., 2006; Fleming et al., 2010), with both halves of the channel required to mediate and maintain septal membrane fission. To test this hypothesis, we used cell-specific SpoIIIE degradation together with fluorescence recovery after photobleaching (FRAP) to assess the continuity of the forespore and mother cell membranes after degrading SpoIIIE in one or the other cell. Briefly, sporangia were stained with the membrane dye FM4-64 and the dye in the forespore photobleached with a laser. If the membrane of the mother cell and the forespore are connected to form a continuous unit, FM4-64 will diffuse from the mother cell to the forespore and fluorescence will completely recover (Figure 6A, right). However, if the membranes are separated and physically disjointed, FM4-64 will not diffuse and forespore fluorescence will not recover (Figure 6A, left).

![Figure 6.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig6-v1.jpg)

**Figure 6.:** (A) Membrane organization in wild type (left) and ΔSpoIIIE (right) strains. SpoIIIE (green) blocks the FM4-64 (red) diffusion from the mother cell to the forespore, which remains bleached (pale red forespore). Arrows show diffusion of FM4-64 to the forespore. (B) Corrected fluorescence recovery (cFR) of individual sporangia without degradation (JLG808) or after degradation in the forespore (F, JLG821), mother cell (MC, JLG823) or both (F and MC, JLG825). When calculating the average cFR (black lines) we excluded curves (pale lines) that resembled those without degradation because they likely represent sporangia in which SpoIIIE is not yet degraded. (C) Average cFR in sporangia without SpoIIIE degradation (green, n = 27) or degradation in the mother cell (blue, n = 35), the forespore (orange, n = 33) or both (red, n = 33). Error bars, standard deviation.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) Visualization of SpoIIIEATP−-GFP-SsrA* (green) by deconvolution fluorescence microscopy. SpoIIIE was not degraded (strain JLG808) or selectively degraded in the mother cell (strain JLG823), in the forespore (strain JLG821) or in both (strain JLG825). The SpoIIIE foci disappear when SpoIIIE is degraded simultaneously in forespore and mother cell, but not when degraded only in one cell. Membranes were stained with FM4-64 (red). Scale bar is 1 μm. (B) Normalized fluorescence intensity of SpoIIIEATP−-GFP-SsrA* foci without degradation (green; JLG808), or after degradation in the forespore (red; JLG821) or mother cell (blue; JLG823). Foci intensities were measured in sporangia with flat septum, curved septum and engulfing. Each dot represents the focus intensity from a single sporangium, and black dotted lines represent the mean. The mean foci intensity of sporangia with flat septa in the non-degradation strain was normalized to 100. Similarly to wild type SpoIIIE (Figure 3B), the foci intensity decreases to approximately half when SpoIIIEATP−-GFP is degraded either in the forespore shortly after polar septation (curve septa). The mean foci intensities, standard deviations, and number (n) of analyzed sporangia are indicated in the table below the graph.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Images show the FRAP the forespore membranes of representative sporangia when SpoIIIEATP− is not degraded (strain JLG808) or selectively degraded in the forespore (F; strain JLG821), in the mother cell (MC; strain JLG823), or degraded in both (MC and F; strain JLG825). The first column (−2 s) is before photobleaching the forespore area (indicated by yellow box). Snapshots after photobleaching were taken at the indicated times.

Since SpoIIIE is only essential for septal membrane fission in the presence of trapped DNA, we used SpoIIIEATP−, which supports septal membrane fission (Fleming et al., 2010) but not chromosome translocation (Sharp and Pogliano, 1999). We detected the same number of molecules in the foci of SpoIIIEATP− as the wild type (Table 1), suggesting that the organization of the complex is similar. We constructed a GFP-SsrA* tagged version of SpoIIIEATP−, which was degraded similarly to the wild-type allele (Figure 6—figure supplement 1), and performed FRAP of engulfing sporangia. Fluorescence did not recover when SpoIIIE was not degraded, indicating that the membranes are separated (Figure 6B,C, Figure 6—figure supplement 2). However, fluorescence completely recovered in most sporangia within 60 s when SpoIIIE was degraded in the mother cell, the forespore or both (Figure 6B,C, Figure 6—figure supplement 2). These results indicate that SpoIIIE subcomplexes in both cells are required for septal membrane fission, supporting the model that assembly of a paired channel contributes to membrane fission (Figure 7C). Furthermore, the observation that the separated membranes before degradation were converted to continuous membranes after degradation suggests that membrane fission is reversible during DNA translocation and depends on the integrity of the paired channel.

![Figure 7.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig7-v1.jpg)

**Figure 7.:** (A) Visualization of DAPI-stained DNA (blue) after cell-specific degradation of SpoIIIE-GFP-SsrA* (green). Membranes are stained with FM4-64 (red). Single arrowheads show forespores containing small amounts of DNA; double arrowhead shows anucleate forespores. Scale bar, 1 μm. (B) Forespore DAPI intensity normalized to the total intensity (forespore plus mother cell) of sporangia about to complete engulfment in the indicated degradation strains. Each dot shows the normalized DAPI intensity of one forespore. Median (red line) and the number of sporangia (n) are indicated. Sporangia containing <0.05 DNA in the forespore were considered anucleate. (C) Models for SpoIIIE and membrane organization before and after cell-specific SpoIIIE degradation. During division, SpoIIIE assembles channels that separate daughter cell membranes and mediate forward chromosome translocation. Selective degradation of SpoIIIE either in the mother cell or the forespore reverses membrane fission, with the remaining molecules exporting DNA from their respective cell.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** The graph shows the normalized forespore DAPI intensity of wild type (PY79) and SpoIIIEATP− mutant strain (KP541) for sporangia at different stages of engulfment. Normalized forespore DAPI intensity was calculated as [Forespore DAPI intensity/(Foresore DAPI intensity + Mother cell DAPI intensity)], for details see ‘Meterials and methods’. As engulfment progresses, the normalized DAPI intensity of the wild type sporangia increases gradually until it reaches a plateau in cells undergoing engulfment. SpoIIIE degradation in either mother cell or forespore happens before engulfment starts (Figure 3B), and therefore before chromosome translocation is completed. As expected, the DAPI intensity does not increase in the translocation-defective SpoIIIEATP− mutant sporangia. The average and standard deviation of at least 25 different sporangia is represented for every engulfment stage.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** The normalized forespore DAPI intensity was calculated for sporangia about to complete engulfment, in strains not expressing sspBEc (PY79) or expressing sspBEc in the forespore (JLG170), mother cell (JLG180), or both (JLG323). SpoIIIE is not tagged with SsrA* in those strains and therefore no degradation is expected. In these strains DNA translocation is not impaired. Each dot represents the normalized DAPI intensity of a sporangium. Median (red line) and the number of sporangia (n) are indicated.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig7-figsupp3-v1.jpg)

**Figure 7—figure supplement 3.:** (A) We inserted a gene encoding CFP under the control of a σF-dependent promoter (PspoIIQ) in the cotC locus of Bacillus subtilis chromosome (I). cotC (168°) is close to the dif site (166°) and therefore is one of the last regions of the chromosome to be translocated into the forespore. Since the CFP gene is expressed from a σF-dependent promoter, it will not be transcribed until it reaches the forespore. Therefore, we can use the presence of CFP in the forespore as an indicator that chromosome translocation has been completed (II). If chromosome translocation is impaired and the cfp gene does not reach the forespore, no CFP signal will be detected (III). (B) Deconvolution fluorescence microscopy of sporangia containing cfp under the control of spoIIQ promoter inserted in the cotC locus, in strains in which SpoIIIE is not degraded (JLG981), degraded in the forespore (JLG1001), degraded in the mother cell (JLG1002) or degraded in both (JLG1003). When SpoIIIE is not degraded or degraded only in the forespore most sporangia show CFP signal in the forespore, indicating that translocation has been completed. However, when SpoIIIE is degraded in the mother cell or in both the forespore and mother cell simultaneously, many sporangia in late stages of engulfment do not show CFP signal in the forespore (arrowheads), indicating that chromosome translocation is not completed. Cells were imaged at t2.5. Scale bar is 1 μm. (C) Percentage of forespores showing CFP signal in strains containing SsrA* untagged SpoIIIE for sporangia in different stages of engulfment. The adaptor protein SspBEc was not expressed (EBS606) or expressed in the forespore (JLG978), mother cell (JLG979), or both (JLG980). Contrary to the SsrA* tagged SpoIIIE strains (from Firugre S6D and F) all sporangia about to complete engulfment show GFP signal in the forespore, indicating that chromosome translocation is already completed at this stage. Expression of sspBEc does not affect the rate at which CFP signal appears in the forespore. Between 25 and 216 sporangia were analyzed, depending on the strain and cell type. (D) Percentage of sporangia in different stages of engulfment showing CFP signal in the forespore when SpoIIIE is not degraded (JLG981) or degraded in the forespore (JLG1001), mother cell (JLG1002) or both (JLG1003). Degradation of SpoIIIE in the mother cell or in both the mother cell and forespore simultaneously reduces the percentage of sporangia showing CFP signal in late stages of engulfment by ∼50%. Degradation of SpoIIIE in the forespore produces a delay in the appearance of CFP signal compared to the control, but >90% of the forespores are blue by the completion of engulfment. Between 32 and 306 sporangia were analyzed, depending on the strain and cell type.

### DNA translocation involves different contributions by forespore and mother cell SpoIIIE

We next used the cell-specific degradation system to determine if both SpoIIIE subcomplexes were necessary for chromosome translocation, taking advantage of the observation that SpoIIIE degradation occurs before chromosome translocation is complete (Figure 7—figure supplement 1). We used the SpoIIIE-GFP-SsrA* cell-specific degradation strains and quantified the amount of DAPI-stained DNA in the forespore relative to the total DNA in sporangia that were about to complete engulfment (Figure 7A,B). As previously reported (Becker and Pogliano, 2007; Ptacin et al., 2008), when chromosome translocation is completed the normalized forespore DAPI intensity is just ∼30–40% (of the total DNA) rather than the expected 50% (one full chromosome in the forespore and the other in the mother cell), likely due to self-quenching of DAPI in the smaller volume of the forespore. In the SpoIIIEATP− mutant, where chromosome translocation is blocked, and before DNA translocation starts in the wild type, the normalized forespore DAPI intensity is 10–15% (Figure 7—figure supplement 1). Without degradation, most sporangia finished chromosome translocation before the completion of engulfment showing an average normalized forespore DAPI intensity of 37% (Figure 7B). Similarly, when SpoIIIE was degraded in the forespore, most sporangia completed chromosome translocation (normalized DAPI intensity, 38%). However, 26% of sporangia showed a normalized DAPI intensity <30% (Figure 7B), suggesting that in some sporangia the absence of the forespore complex impaired the ability of the mother cell complex to translocate DNA. In contrast, degradation of SpoIIIE in the mother cell blocked chromosome translocation (normalized DAPI intensity, 20%) in most sporangia and 20% of sporangia showed anucleate forespores (Figure 7A,B), indicating that in the absence of the SpoIIIE mother cell subcomplex, the forespore subcomplex can ultimately translocate the chromosome in the reverse direction. As expected, degradation in both cells blocked chromosome translocation (normalized DAPI intensity, 21%) and generated 6% anucleate forespores, less than when SpoIIIE was degraded only in the mother cell (Figure 7B). Expresison of sspBEc in strains in which SpoIIIE was not tagged with SsrA* did not show any defect in chromosome translocation, indicating that the observed phenotypes are indeed due to the degradation of SpoIIIE molecules (Figure 7—figure supplement 2). These results support the notion that SpoIIIE functions as a DNA exporter (Sharp and Pogliano, 2002), and that although it normally operates in the mother cell, it is capable of operating in the forespore in the absence of the mother cell subcomplex (Figure 7C), generating anucleate forespores. Surprisingly, our results also provide evidence that the forespore subcomplex is necessary for maximal DNA translocation efficiency, a result confirmed by quantifying the frequency with which a CFP reporter of forespore gene expression that was positioned near the terminus entered the forespore (Figure 7—figure supplement 3).

## Discussion

We investigate here the organization and function of the SpoIIIE DNA translocation channel during B. subtilis sporulation using cell-specific protein degradation, quantitative super-resolution microscopy, and FRAP. We were able to directly visualize the assembly of SpoIIIE into two subcomplexes consisting of subunits in each daughter cell. Cell-specific protein degradation and qPALM were used to determine the relative abundance of SpoIIIE in each daughter cell, and our results indicate that each contain approximately equal numbers of SpoIIIE molecules. These observations support a model in which each chromosome arm is transported through a paired channel that spans two lipid bilayers (Figure 8B, Liu et al., 2006; Burton et al., 2007; Fleming et al., 2010). The distance between the clusters in each cell was found to be 55 nm, which is larger than the 40 nm width of the septum in the strains used here, providing some support for a channel architecture in which the motor domains of each complex are within the cytoplasm of the respective daughter cell (Figure 8B, left) rather than within the septum (Figure 8B, right), although further experiments are required to address this point.

![Figure 8.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig8-v1.jpg)

**Figure 8.:** (A and B) Septal cross sections showing SpoIIIE (red), DNA (blue) and lipids (grey) and displaying just one DNA strand traversing the septum for simplicity, although at least two arms of the circular chromosome must cross the septum. Our results indicate that the translocation channel has approximately equal numbers of SpoIIIE motor domains in each cell, consistent with the models shown in B, but not with the simple aqueous channel model in A. They further indicate that the SpoIIIE membrane domains are arranged in such a way that they form a continuous protein barrier at the septum that blocks diffusion within the lipid bilayer and that molecules in each cell are required to form this barrier. We envision two alternative organizations to achieve this. First, the transmembrane domains might form channels in each septal membrane that interact within the septal space and conduct the DNA across the septum, with the motor domains projecting into the cytoplasm (left). Second, the transmembrane domains might form a contiguous external ring that blocks lipid diffusion, with motor domains projecting towards the lumen of an aqueous channel (right). The distance between the centers of the forespore and mother cell clusters (55 nm) is larger than the thickness of the septum (40 nm, Tocheva et al., 2013) leading us to prefer the paired channel model (left). (C) Each chromosome arm is translocated by a different SpoIIIE channel that is comprised of opposing motor domains that have the ability to export DNA from their respective cell. Translocation directionality is established by the interaction between SRS and the SpoIIIE γ domain, which activates the mother cell motor (green), and inactivates the forespore motor (grey). Consequently, the mother cell-SpoIIIE exports DNA until the final loop (ter) reaches the septum. We propose that translocation of the loop generates tension that destabilizes and opens the channels forming a larger pore to pass the loop.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** A detailed analysis of qPALM data reveals the existence of two populations of sporangia with different numbers of SpoIIIE monomers at the septum. (A and B) Comparison between two different analyses—Gaussian Kernel Density Estimator (GKDE) and Variational Bayesian Gaussian Mixture Model (VBGMM)—for quantification of SpoIIIE in (A) the wild type strain and (B) the ΔσE strain. Both analyses lead to the finding of two populations with the peak values ∼24 and 50 (red dotted lines). (Top panels from A and B) GKDE (blue curves) of the SpoIIIE counting data (blue bars) were fitted well by a mixture of two Gaussian functions (red solid curves). See ‘Materials and methods’ for details on the analyses.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/06474/elife-06474-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** Septum containing four arms of DNA still can translocate the entire chromosome toward the forepore. The orientation of SRSs along the chromosme and their interaction with SpoIIIE is such that three arms are translocated toward the forespore by the mother cell-SpoIIIE while one arm is translocated into the mother cell by the forespore-SpoIIIE. Therefore, the net translocation is toward the forespore.

The stability of the SpoIIIE complex during DNA translocation (Fleming et al., 2010) allowed us to use qPALM (Lee et al., 2012) to image and quantify SpoIIIE in living cells. However, it is important to note that imaging live rather than fixed cells would likely overestimate the dimensions of the complex if SpoIIIE moves during DNA translocation, which could explain why the measured width of the foci (80 nm) is wider than expected for two side by side hexamers (∼24 nm). Furthermore, the spatial resolution of PALM (∼25 nm) remains significantly larger than the size of most macromolecular assemblies, and it is larger than the distance between the two faces of the septum in wild type cells (∼20 nm). We partially overcame the current limitations of PALM by using two genetic tools, the thick septum mutant which increased the distance between the subcomplexes in each cell, and cell-specific protein degradation which improved our ability to discriminate between molecules in each cell.

The method to extract absolute numbers using PALM may depend on other factors, such as label efficiency and inactivation (Lee et al., 2012; Puchner et al., 2013; Durisic et al., 2014). Although our qPALM approach balances the over- and undercounting errors (Lee et al., 2012), the numbers of SpoIIIE molecules determined here may represent a lower bound to their true number if some of the photoactivatable fusion domains did not fold properly at the foci. Nevertheless, it is tantalizing to note that our counting method (Lee et al., 2012) indicated that the SpoIIIE complex contains 31 (±18) SpoIIIE molecules, enough to form at least two dodecameric channels, one for each chromosome arm (24 molecules in total, Table 1). Furthermore, a more detailed analysis of qPALM data revealed the existence of two populations of sporangia with different numbers of SpoIIIE monomers at the septum (∼25 and ∼50; Figure 8—figure supplement 1), suggesting that some translocation complexes have enough molecules to assemble two channels while others could assemble four (Figure 8—figure supplement 2). Therefore, we speculate that SpoIIIE organizes around an even number of DNA arms (two or four) during sporulation (Figure 8—figure supplement 2), as would be expected if a circular chromosome crossed the septum one or two times, respectively.

Cell-specific protein degradation was used both to quantify and to functionally dissect the role of SpoIIIE molecules in each cell. Our results demonstrate that SpoIIIE is required in both cells to maintain separate septal membranes during DNA translocation and that septal membrane fission is reversible in the presence of trapped DNA (Figure 6). The simplest explanation for this finding is that transmembrane domains in each cell assemble a structure that excludes lipids and blocks membrane diffusion between the two cells. This scenario could occur if during assembly of a translocation complex, SpoIIIE membrane domains in the mother cell and the forespore dock via their extracellular domains and the membrane domains of each subunit—within each bilayer—compact into their hexameric form, excluding lipids to form a paired central channel (Almers, 2001; Peters et al., 2001; Liu et al., 2006; Fleming et al., 2010). It is possible that docking is indirect and requires additional, accessory proteins that connect the extracellular domains of SpoIIIE. In addition to the data presented here, the paired channel model for septal membrane fission is supported by our previous demonstration that septal membrane fission depends on the SpoIIIE transmembrane domain (Sharp and Pogliano, 2003) and its large extracellular loop (Liu et al., 2006) and on the assembly of a compact focus (Fleming et al., 2010).

In contrast to membrane fission, which requires SpoIIIE in both cells, only mother cell SpoIIIE is essential for DNA segregation, demonstrating that SpoIIIE functions as a DNA exporter (Sharp and Pogliano, 2002). While the assembly of SpoIIIE in both sides of the septum provides a structural scaffold for membrane fission, it poses a topological challenge for directional chromosome translocation. Prior to the establishment of directional DNA translocation, both complexes could, in principle, export DNA out of its respective compartment (Sharp and Pogliano, 2002; Becker and Pogliano, 2007; Ptacin et al., 2008) (Figure 7A,B), leading to a potential clash between complexes in each cell; as a result, these complexes would compete to translocate DNA either out of or into the forespore. However, our cell-specific degradation data show that chromosome translocation happens most efficiently when both complexes are present (Figure 7B, Figure 7—figure supplement 3), suggesting that rather than a competition, there is a potentiation between the two hexamers of a channel. We therefore propose that the hexamers within a dodecameric channel should be considered as an integral entity (Figure 8C). In this model, docking of the transmembrane domains of hexamers in opposite septal membranes might contribute to the robustness of chromosome translocation in two ways. First, it might stabilize the translocation complex, distributing the tension produced by the movement of the chromosome between the two septal membranes and insulating the DNA from interactions with the membrane or periplasm. Second, it might facilitate the deactivation of the forespore motor domains after activation of the mother cell motor domains by encountering SRSs in the permissive orientation (Besprozvannaya et al., 2013; Cattoni et al., 2013).

Some members of the SpoIIIE/FtsK/HerA superfamily, including SpoIIIE and FtsK in bacteria (Burton and Dubnau, 2010), and possibly HerA in archaea (Iyer et al., 2004), are involved in the post-septational segregation of chromosomes when one of them is accidentally trapped in the septum during vegetative cell division. Since the trapped chromosome can belong to either daughter cell, a paired channel similar to the one described here could function as a bidirectional translocation machinery guided by SRS-like sequences that would allow the transport of the chromosome to the appropriate compartment. So, by analogy to SpoIIIE, we hypothesize that the transmembrane domain of these proteins might also form a paired channel crossing both septal membranes.

## Materials and methods

### Strains and cell culture

All the strains used in this study are derivatives of B. subtilis PY79. The strains, plasmids and oligonucleotides used in this study, can be found in Supplementary file 1A–C. The amino acid sequence of the linker between GFP-SsrA* and the target protein is provided in Supplementary file 1D. All the SpoIIIE fusion proteins used here support sporulation with wild type efficiency (Supplementary file 1E). Sporulation was induced by resuspension (Sterlini and Mandelstam, 1969) at 37°C, except the bacteria were grown in 20% LB prior to resuspension (Becker and Pogliano, 2007).

### Plasmid construction

#### pTF25

dendra2 coding sequence was amplified with primers TF-55 and TF-56. The PCR fragment was digested with SpeI and cloned in pEB410 (Fleming et al., 2010) digested with the same enzyme.

#### pJLG3

ssrA*Ωkan fragment was created by amplifying the kanamycin resistant gene of pEB19 (Becker et al., 2006) with primers JLG-1 and JLG-5. The fragment was digested with NheI and PstI and was cloned in pBR329 digested with the same enzymes.

#### pJLG7

sspB was amplified from genomic DNA of E. coli K12 MG1655 with primers JLG-16 and JLG-17, digested with EcoRI and BglII, and cloned in pDG1731 (Guérout-Fleury et al., 1996) digested with EcoRI and BamHI.

#### pJLG13

sspB gene was amplified with primers JLG-16 and JLG-32 from genomic DNA of E. coli K12 MG1655, digested with BamHI and EagI, and inserted in pMDS13 (Sharp and Pogliano, 2002) digested with the same enzymes. This plasmid contanis sspB under the control of spoIIQ promoter and can be integrated into amyE locus in B. subtilis chromosome.

#### pJLG20

pMDS14 (Sharp and Pogliano, 2002) was digested with EcoRI and BamHI, and the resulting fragment containing spoIID promoter was cloned in EcoRI-BamHI sites of pJLG7. This plasmid contains sspB under the control of spoIID promoter and can be integrated into thrC locus in B. subtilis chromosome.

#### pJLG36

sfGFP coding sequence was amplified with primers JLG-33 and JLG-34, digested with SphI and SpeI, and cloned in pJLG3 digested with SphI and NheI. It contains sfGFP fused to the ssrA*, and eight codons encoding an Ala-Ser linker immediately upstream of sfGFP.

#### pJLG38

pJLG36 was amplified with primers JLG-86 and JLG-87 (both phosphorylated at the 5′end) and religated. The resulting primer contained sfGFP coding sequence preceded by eight codons encoding an Ala-Ser linker, without the ssrA*.

#### pJLG49

This plasmid was constructed by assembling the following four fragments by Gibson Assembly (New England Bioloabs, Ipswich, Massachusetts): (i) the last 852 bp of sigA coding sequence (not including the stop codon) amplified with primers JLG-132 and JLG-133 from genomic DNA of B. subtilis PY79; (ii) sfGFP-ssrA*Ωkan fragment amplified with primers JLG-7 and JLG-77 from pJLG36; (iii) a fragment of 940 bp corresponding to the region immediately dowstream of sigA stop codon, amplified with primers JLG-130 and JLG-131 from genomic DNA of B. subtilis PY79; and (iv) a DNA fragment encompassing the spectinomycin resistant gene, the origin of replication, and the ampicillin resistant gene from pDG1662 (Guérout-Fleury et al., 1996), amplified with primers JLG-95 and JLG-96.

#### pJLG72

This plasmid was constructed by assembling the following four fragments by Gibson Assembly (New England Bioloabs): (i) the last 852 bp of spoIIIE coding sequence (not including the stop codon) amplified with primers JLG-234 and JLG-236 from genomic DNA of B. subtilis PY79; (ii) sfGFP-ssrA*Ωkan fragment amplified with primers JLG-7 and JLG-77 from pJLG36; (iii) a fragment of 844 bp corresponding to the region immediately dowstream of spoIIIE stop codon, amplified with primers JLG-232 and JLG-233 from genomic DNA of B. subtilis PY79; and (iv) a DNA fragment encompassing the spectinomycin resistant gene, the origin of replication, and the ampicillin resistant gene from pDG1662 (Guérout-Fleury et al., 1996), amplified with primers JLG-95 and JLG-96.

#### pJLG112

This plasmid was constructed by assembling the following four fragments by Gibson Assembly (New England Bioloabs): (i) the last 856 bp of gyrA coding sequence (not including the stop codon) amplified with primers JLG-416 and JLG-417 from genomic DNA of B. subtilis PY79; (ii) ssrA*Ωkan fragment amplified with primers JLG-7 and JLG-184 from pJLG3; (iii) a fragment of 861 bp corresponding to the region immediately dowstream of spoIIIE stop codon, amplified with primers JLG-418 and JLG-419 from genomic DNA of B. subtilis PY79; and (iv) a DNA fragment encompassing the spectinomycin resistant gene, the origin of replication, and the ampicillin resistant gene from pDG1662 (Guérout-Fleury et al., 1996), amplified with primers JLG-95 and JLG-96.

#### pJLG118

A 2212 bp DNA fragment of spoIIIEATP− coding sequence was amplified from genomic DNA of KP541 with primers JLG-248 and JLG-450, and assembled with pJLG72 amplified with primers JLG-95 and JLG-245 by Gibson assembly.

#### pJLG125

sfGFP was amplified with primers JLG-55 and JLG-77, from pJLG38 and assembled with pJLG112 amplified with primers JLG-539 and JLG-540 by Gibson assembly.

### PALM imaging

Cells were sporulated in presence of 25 ng/ml membrane dye FM5-95 (Life Technologies, Waltham, Massachusetts) and harvested 1 hr and 45 min (t1.75) after resuspension. 5 μl of cell suspension mixed with gold fiducial particles was spotted in a poly-L-Lys (Sigma–Aldrich, St. Louis, Missouri) coated coverslip and covered with a second coverslip to generate a cell monolayer (Fleming et al., 2010). To minimize the over- and under- quantification of PA-FP molecules: first, the sample was illuminated with the excitation laser (561 nm, 22 mW/mm2) simultaneously with the activation laser (405 nm) whose power varied (from 0 to 9.1 mW/mm2) in time according to the Fermi activation scheme (Lee et al., 2012) with parameters tF = 3.2 min and T = 10 s; and second, we employed our previously developed optimal tc method (Lee et al., 2012). PALM data was taken and analyzed using our custom built microscope and custom written Matlab program (Fleming et al., 2010; Lee et al., 2012). Single molecule counting was performed in strains with Dendra2 fusion protein.

### Identification and characterization of SpoIIIE clusters in PALM images

#### Identification of SpoIIIE clusters (foci)

We first visually inspected each sporangium from the overlaid SpoIIIE-PALM image and membrane labeled image. Then, SpoIIIE-PALM foci were identified as the spatially localized intensely emitting sources in the PALM images that typically organized symmetrically at the mid point of the septum.

#### Identification of dual-foci

Only those images in which the two foci could be discerned clearly were identified as dual foci and included in the analysis. Thus, even though in some cases the clusters could be seen as distinct, they were not included in our analysis if they appeared physically connected in the PALM image. To formalize the identification, we employed the Rayleigh resolution criterion. We used the fact that the average width (four times the standard deviation) in perpendicular direction to the septum of the forespore- and mother cell-proximal cluster from dual-foci was 57 nm and 52 nm, respectively (Figure 5C). Accordingly, dual foci were identified as such if the distance between the peaks of the individual foci were at least 39 nm or more. It should be pointed out that 94% of the measured distance between these adjacent two clusters are larger than the Rayleigh criteria as shown in Figure 5A.

#### Characterization of foci

To obtain the position of the clusters we first manually drew a Region of Interest (ROI) that surrounds each cluster and that contains 99% of the fluorescence localization signal. Then, the FM-labeled membrane image was used to draw a line that coincided with the septum across each sporangium (septal line). From the distribution of point localization data of each cluster we obtained the center of mass of that cluster and its dispersion in the direction perpendicular and parallel to the septal line. Four times the standard deviation of these dispersions was used to define the widths of the cluster in each direction.

### Steps for qPALM

Quantitative single-molecule-counting PALM is based on the previously established method (Lee et al., 2012) and is carried out through the following steps: (1) obtain the photoactivation rate, blinking rate, and photobleaching rate of a PA-FP that will be used as a fluorescent marker, for instance, through in vitro single-molecule characterization, (2) acquire PALM raw movie data using Fermi-photoactivation scheme, which assures photoactivation of all the PA-FP molecules within a given experimental time at the almost constant rate (Figure 5—figure supplement 2), (3) analyze the raw data to localize the appearance of fluorescence bursts in space and time and render a reconstructed PALM image, (4) select a ROI, for example a focus of SpoIIIE, from the visual inspection of the PALM image, and (5) apply the optimal-τc counting (Matlab code available in Source code 1 also at https://github.com/shyuklee/pafpcluster) to the ROI to obtain the blinking-corrected number of molecules inside the ROI.

### Detailed description of qPALM methodology

The in vitro photophysics of Dendra2 was well described by four states: Nonactive (N), Active (A), Dark (D), and photoBleach (B); and the rates: N to A (ka), A to B (kb), and A to D (kd). The fluorescence recovery, D to A, was well explained by two different rates (kr1 and kr2) with their population ratio (α), which implies the existence of at least two dark states. The photoactivation rate ka can be externally changed by the intensity of UV light whereas all the other rates are constants fixed by the intrinsic molecular properties of Dendra2. In order to optimize the temporal separation of molecules we changed ka in time such that a Dendra2 molecule gets photoactivated during a given experimental time, tF, with an almost uniform probability distribution. To account for the overcounting error induced by multiple transitions between the state A and the state D, we introduced a tolerance time of the dwell in the dark states, τc: if the fluorescence at the same location recovers within a given τc then the two events are considered due to a blink of an identical Dendra2 molecule rather than due to two independent photoactivation events of two different molecules. However, the introduction of τc also induces molecular undercounting error because it is probabilistically not impossible that two different Dendra2 molecules actually get photoactivated one after the other within a time interval shorter than the given value of τc.

We can achieve the unbiased molecular counting by balancing the overcounting and undercounting through a careful selection of the value of τc. This optimal τc depends not only on all the rate constants but also on the actual number of Dendra2 molecules (Nmol) that we aim at counting by PALM. In the previous work, we obtained the optimal τc by stochastic simulations, but this method was computationally too costly to explore the extensive parameter space defined by the rate constants and Nmol (Lee et al., 2012). We instead developed an approximate analytic solution of the optimal τc for instantaneous calculation.

If we assume that Nmol molecules are independently photoactivated uniformly in time between 0 and tF, then the probability density function of the time lag, Δti, between the two successive ith and (i + 1)th photoactivation events is given by the well known order statistics of the uniform distribution:

$$
p(Δt_{i})=N_{mol} (1−Δt_{i}/t_{F})^{N_{mol}}.
$$

In order to estimate the undercounting error, we apply a rule of counting for a given τc such that ith and (i + 1)th photoactivations are combined together to be counted as one molecule if Δti < τc. Then the mean of undercounted number, denoted by ⟨Nu⟩, can be calculated as follows:

$$
⟨N_{u}⟩=N_{mol}−(1+\sumi=1N_{mol}−1 \int_{0}^{\tau_{c}} p(Δt_{i}) dΔt_{i}),
$$



$$
=(N_{mol}−1)[1−(1−\tau_{c}/t_{F})^{N_{mol}}].
$$

The overcounting due to blinking can be estimated using the geometrically distributed probability of the number of transitions that a single Dendra2 molecule makes between the state A and the state D with the dwell in the state D being longer than τc before photobleaching (Lee et al., 2012):

$$
P{N_{blink}^{(\tau_{c})}=n}=η¯^{n}(1−η¯),
$$

where

$$
η¯=\frac{p_{\tau_{c}}η}{1−η+p_{\tau_{c}}η}   and   p_{\tau_{c}}=\frac{e^{−k_{r1}\tau_{c}}+\alphae^{−k_{r2}\tau_{c}}}{1+\alpha}.
$$

Then the mean of total overcounted number of independently blinking Nmol molecules, denoted by ⟨No⟩, is given by

$$
⟨N_{o}⟩=N_{mol} \sumn=0∞ P{N_{blink}^{(\tau_{c})}=n},
$$



$$
=N_{mol} \frac{η¯}{1−η¯}.
$$

Note that ⟨Nu⟩ and ⟨No⟩ are not the exact solutions but just approximate estimates of the undercounting and overcounting because they account for only the situation when the ith photoactivated molecule photobleaches much earlier than the next photoactivation of another molecule. Nevertheless, they are the dominant contributions to the counting error and we can expect to obtain the optimal τc rather accurately from the balance condition, ⟨Nu⟩ = ⟨No⟩, which results in an analytic equation for the optimal τc:

$$
h(\tau_{c}; N_{mol},t_{F},k_{d},k_{b},k_{r1},k_{r2},\alpha)=0,
$$

where

$$
h(\tau_{c}; N_{mol},t_{F},k_{d},k_{b},k_{r1},k_{r2},\alpha)≡1−(1−\tau_{c}/t_{F})^{N_{mol}}−p_{\tau_{c}}\frac{k_{d}}{k_{b}}\frac{N_{mol}}{N_{mol}−1}.
$$

This approximate analytic solution agrees well with the result from the stochastic simulation over experimentally realistic range of Nmol and tF when the rates are fixed to the rates of Dendra2 obtained from in vitro single-molecule experiments (Figure 5—figure supplement 2).

To count the number of SpoIIIE-Dendra2 molecules inside a cluster, we iterated the feedback between τc and Nmol using the in vitro Dendra2 kinetic rates and the analytic solution of optimal τc(Nmol) until convergence (Lee et al., 2012).

### Statistical analysis of qPALM data

#### Gaussian Kernel Density Estimator (GKDE)

GKDE is independent of bin size, and therefore a more accurate estimator than a histogram of an unknown probability distribution. It is commonly used across a broad range of disciplines, including single-molecule studies. We used a built-in Matlab function ‘ksdensity’ that implemented a GKDE algorithm provided in Botev et al. (2010). We first calculated a GKDE curve form the data, and then fitted it to either a single Gaussian or a mixture of two Gaussian functions.

#### Variational Bayesian Gaussian Mixture Model (VBGMM)

To further justify the existence of two populations in the SpoIIIE counting data (Figure 8—figure supplement 1), we employed VBGMM. Basically, Gaussian Mixture Models (GMM) treats the data by a mixture of multiple Gaussian components. Then, one can fit the GMM model distribution directly to the data without resorting to a histogram or GKDE curve using various methods; among these the simplest is the maximum likelihood method. However, the downside of the maximum likelihood method is that it cannot uniquely determine the number of Gaussian components—denoted by ‘K’ henceforth—due to the problem of overfitting data. Therefore, the maximum likelihood method is not ideal because it relies on a manual input of ‘K’ that is predetermined in a subjective and heuristic manner. In contrast, the VBGMM is a Bayesian approach in which the model parameters, such as the mean and the standard deviation of a Gaussian component, are regarded as random variables. The probability distribution of the model parameters, defined as a ‘posterior’ distribution, is then marginalized and optimized to determine the ‘K’ value in the VBGMM method (Bishop, 2006). VBGMM determines the optimal ‘K’ that best explains the data without the problem of overfitting. VBGMM automatically takes care of the problem of overfitting within its self-contained statistical framework. This Bayesian approach has been proved to be very successful in objectively determining the number of states from single-molecule FRET data (Bronson et al., 2009).

### Fluorescence deconvolution microscopy: imaging and analysis

Samples from sporulating cell cultures were taken 2.5 hr after resuspension (t2.5) and added to agarose pads supplemented with 0.5 μg/ml of FM4-64 (Life Technologies) for membrane visualization and 40 ng/ml of DAPI (Invitrogen, Waltham, Massachusetts) for DNA visualization. Images were collected using an Applied Precision optical sectioning microscope equipped with a Photometrics CoolsnapHQ2 camera using identical exposure times for each sample. Images were deconvolved and analyzed with SoftWoRx version 5.5 (Applied Precision, Issaquah, Washington). Sporangia with flat, curved, and engulfing septa (as defined in Sharp and Pogliano, 1999) from 2–4 microscopy fields were quantified. To determine SpoIIIE-GFP-SsrA* foci intensities, GFP intensities of eight optical sections covering a total thickness of 1.05 μm within the cells were summed using SoftWoRx Z-projection tool. The intensity of each projected GFP focus was determined by drawing a ∼150 nm2 circumference centered in the middle of the focus, subtracting the average background intensity for each field. The average focus intensity after SpoIIIE-GFP degradation in the mother cell or in the forespore was normalized to the average intensity when SpoIIIE-GFP was not degraded.

To determine the fluorescence intensities of GyrA-GFP-SsrA* and SigA-GFP-SsrA* in the forespore and mother cell, pixel intensities of four optical sections from deconvolved images covering a total thickness of 0.45 μm were summed. Mean GFP intensities of the forespore and the mother cell were determined separately by drawing a polygon encompassing the whole area of every cell. The ratios were calculated after subtracting the mean background intensity. For each graph, values were made relative to the average ratio of cells with flat septum in the non-degradation strain.

To determine the degree of DNA translocation, DAPI pixel intensities of four optical sections covering a total thickness of 0.45 μm were summed. Samples were taken 3 hr after resuspension (t3), and DAPI intensities of forespore (F) and mother cell (MC) from sporangia about to complete engulfment were determined separately by drawing a polygon encompassing the whole DNA area of every compartment. After subtraction of the average background intensity, the normalized DAPI intensity [F intensity/(F intensity + MC intensity)] was determined for each sporangium.

### FRAP

FRAP of forespore membranes was performed as described (Fleming et al., 2010). Briefly, cells were sporulated in the presence of 2 μg/ml FM4-64. After 2.5 hr, cells were washed three times with sporulation medium and placed onto 1.2% agarose pads. Forespore membranes were bleached with 0.3 s pulse from a 488-nm argon laser set to 30% power, and membrane images collected at appropriate time intervals. FRAP quantification was performed as described (Fleming et al., 2010).
