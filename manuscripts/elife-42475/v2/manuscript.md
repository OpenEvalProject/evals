# Optogenetic control shows that kinetic proofreading regulates the activity of the T cell receptor

## Authors

- O Sascha Yousefi<sup>1</sup> ([ORCID: 0000-0001-5304-729X](https://orcid.org/0000-0001-5304-729X))
- Matthias Günther<sup>4</sup> ([ORCID: 0000-0001-8077-8194](https://orcid.org/0000-0001-8077-8194))
- Maximilian Hörner<sup>1</sup> ([ORCID: 0000-0003-1743-9581](https://orcid.org/0000-0003-1743-9581))
- Julia Chalupsky<sup>1</sup>
- Maximilian Wess<sup>1</sup>
- Simon M Brandl<sup>1</sup>
- Robert W Smith<sup>7</sup> ([ORCID: 0000-0001-9657-7477](https://orcid.org/0000-0001-9657-7477))
- Christian Fleck<sup>7</sup>
- Tim Kunkel<sup>2</sup>
- Matias D Zurbriggen<sup>1</sup>
- Thomas Höfer<sup>4</sup>
- Wilfried Weber<sup>1</sup>
- Wolfgang WA Schamel<sup>1</sup> ([ORCID: 0000-0003-4496-3100](https://orcid.org/0000-0003-4496-3100)) †

### Affiliations

1. Signalling Research Centres BIOSS and CIBSS University of Freiburg Freiburg Germany
2. Faculty of Biology University of Freiburg Freiburg Germany
3. Spemann Graduate School of Biology and Medicine University of Freiburg Freiburg Germany
4. Division of Theoretical Systems Biology German Cancer Research Center Heidelberg Germany
5. BioQuant Center University of Heidelberg Heidelberg Germany
6. Center for Chronic Immunodeficiency, Medical Center Freiburg and Faculty of Medicine University of Freiburg Freiburg Germany
7. Laboratory of Systems and Synthetic Biology Wageningen University and Research Wageningen Netherlands
8. Institute of Synthetic Biology and Cluster of Excellence on Plant Sciences University of Düsseldorf Düsseldorf Germany

† Corresponding author

## Abstract

The immune system distinguishes between self and foreign antigens. The kinetic proofreading (KPR) model proposes that T cells discriminate self from foreign ligands by the different ligand binding half-lives to the T cell receptor (TCR). It is challenging to test KPR as the available experimental systems fall short of only altering the binding half-lives and keeping other parameters of the interaction unchanged. We engineered an optogenetic system using the plant photoreceptor phytochrome B (PhyB) as a ligand to selectively control the dynamics of ligand binding to the TCR by light. This opto-ligand-TCR system was combined with the unique property of PhyB to continuously cycle between the binding and non-binding states under red light, with the light intensity determining the cycling rate and thus the binding duration. Mathematical modeling of our experimental datasets showed that indeed the ligand-TCR interaction half-life is the decisive factor for activating downstream TCR signaling, substantiating KPR.

## Introduction

The function of T cells is to mount an immune response to foreign ligands, such as derived from bacteria or viruses, but not to respond to self ligands stemming from the body’s own cells. These ligands are composed of a foreign peptide presented by major histocompatibility complexes molecules (pMHC) on the own cells. Activation of a T cell is initiated when foreign pMHC bind to the T cell receptor (TCR) on the T cell surface. The pMHC-TCR binding event stimulates intracellular signaling pathways, such as calcium influx into the cytosol, leading to the functional responses of the T cell (Courtney et al., 2018). Self peptides on MHC (self pMHCs) also bind to the TCR and are important for the development and survival of naïve T cells, but do not trigger an immune response as seen for foreign peptides on MHC (Davis et al., 1998). This discrimination between foreign and self pMHC correlates with the affinity of the ligand-TCR interaction, in that foreign, stimulatory pMHCs bind with higher affinity to the TCR than non-stimulatory pMHC (Davis et al., 1998; Sykulev et al., 1994). However, how the affinity of a ligand is determined by the cell to generate a T cell response or not remains enigmatic (Chakraborty and Weiss, 2014). Note that in case of pMHC binding to T cells other processes than the pure pMHC-TCR interaction are involved, such as interactions with the co-receptors CD8 or CD4; thus, the terms ‘apparent affinity’ or ‘potency’ might be more suitable when describing these complex binding events.

One model is kinetic proofreading (KPR), which originally described the specificity by which the genetic code is read in protein synthesis (Hopfield, 1974) and inspired a similar theoretical model for ligand discrimination in T cells (McKeithan, 1995). In KPR the T cell does not simply measure the amount of ligand-bound TCRs (called occupancy model), but monitors the dynamics of the binding events. These dynamics can be described by the on-rate and the half-life of the interaction. The KPR model proposes that a long half-life of the ligand-TCR interaction, such as seen for high affinity pMHC, allows a series of biochemical reactions to be completed that eventually trigger downstream signaling. By contrast, a low affinity ligand detaches before an activatory signal is produced and the TCR then reverts quickly to the initial inactive state, thus not initiating T cell activation. Although the half-life is the decisive factor, it was recently shown that the on-rate also plays a role (Aleksic et al., 2010; Govern et al., 2010; Lin et al., 2019). If the on-rate is very fast a ligand that has detached can rapidly rebind to the same TCR before the first biochemical reactions are reverted. Again, the duration of the binding event, in this case interrupted by short dissociations, is the relevant parameter.

The KPR model has also been extended to include feedback and feed-forward loops in the signaling network below the TCR (Altan-Bonnet and Germain, 2005; Chakraborty and Weiss, 2014; Dushek et al., 2011; Lever et al., 2016; Rabinowitz et al., 1996). Inclusion of these signaling network loops improved the mathematical description of the observed sharp ligand discrimination threshold, when relating ligand half-life to T cell activation. At the same time, the high sensitivity of the T cells towards low numbers of ligands (1–10 molecules) was retained (Irvine et al., 2002; Purbhoo et al., 2004).

To get experimental insight into the mechanism of ligand discrimination by T cells, pMHC or TCRs have been mutated at the binding sites to generate ligand-TCR pairs of different affinities and half-lives (Aleksic et al., 2010; Altan-Bonnet and Germain, 2005; Daniels et al., 2006; Davis and van der Merwe, 2006; Dushek et al., 2011; Govern et al., 2010; Holler and Kranz, 2003; Kalergis et al., 2001; Kersh et al., 1998; Krogsgaard et al., 2003; Lever et al., 2016). Although such studies are broadly consistent with KPR, other biophysical parameters, such as the free binding energy, geometry of the interaction (Adams et al., 2011), conformational changes at the TCR (Dopfer et al., 2014; Gil et al., 2002; Risueño et al., 2006) and the ability to withstand pulling (Kim et al., 2009; Liu et al., 2014), might also have been changed along with the affinity, and therefore alternative models of ligand discrimination cannot be ruled out. Unfortunately, no method to specifically modulate only the dynamics of ligand-receptor interactions is currently available. Thus, in order to disentangle the half-life from these other parameters, we engineered an optogenetic system in which the duration of ligand binding to the TCR can be remotely controlled in a reversible manner (ON-OFF switch), called the opto-ligand-TCR system.

Our opto-ligand-TCR approach harnesses the PhyB-PIF (phytochrome B-PhyB interacting factor) protein pair from Arabidopsis thaliana (Bae and Choi, 2008; Levskaya et al., 2009; Toettcher et al., 2013). In this pair, the photoreceptor PhyB is the light-responsive element, due to its chromophore phycocyanobilin, which undergoes a conformational cis-trans isomerization when absorbing photons of the appropriate wavelength. Upon illumination with 660 nm light, PhyB switches to its ON state in which it interacts with PIF6 with a nanomolar affinity (Levskaya et al., 2009). With 740 nm light, PhyB undergoes a conformational transition to the OFF state preventing binding to PIF6. This light-dependent protein-protein interaction was utilized in several optogenetic applications (Kolar et al., 2018), such as the control of protein or organelle localization (Adrian et al., 2017; Beyer et al., 2018; Levskaya et al., 2009), intracellular signaling (Toettcher et al., 2013), nuclear transport of proteins (Beyer et al., 2015), cell adhesion (Baaske et al., 2019; Yüz et al., 2018) or gene expression (Müller et al., 2013a). Using high intensity light, the PhyB-PIF interaction can be switched ON and OFF within seconds (Levskaya et al., 2009; Mancinelli, 1994; Smith et al., 2016). Importantly for our study, at continuous 660 nm illumination the individual PhyB molecules constantly switch between the ON and OFF states, again in the order of seconds, thus being within the range of the estimated KPR times (Mancinelli, 1994; Smith et al., 2016).

We and others have previously fused binding domains to the ectodomain of the TCRβ subunit; either a single chain Fv fragment (Minguet et al., 2007) or a single strand DNA oligonucleotide (Taylor et al., 2017). Indeed, the chimeric TCRs were expressed on the cell surface and were activated via the appended binding domains. Importantly, ligand discrimination also occurred when using the DNA-TCR; i.e., a low affinity binder to the DNA did not evoke TCR stimulation and a high affinity binder did (Taylor et al., 2017). This clearly showed that ligands do not need to bind to the canonical pMHC binding site within the TCR and that co-receptors are not required for ligand discrimination. It should be noted that the developmental state of the T cell can modulate the discrimination process as do the co-receptors (CD8 or CD4) or the expression levels of intracellular signaling molecules (Altan-Bonnet and Germain, 2005; Davey et al., 1998; Lucas et al., 1999; Madrenas et al., 1997; Stepanek et al., 2014).

Here we fused the first 100 amino acids of PIF6 together with GFP to the ectodomain of TCRβ and used the first 651 amino acids of PhyB in a tetramerized form as the ligand (Figure 1). Using continuous 660 nm light of different intensities to modulate the dynamics of PhyB tetramer binding to the TCR and calcium influx as a readout we find that there is an intensity threshold: at lower intensities and longer ligand-TCR half-lives the T cell is activated and at higher intensities and shorter half-lives the cell is not activated. Using a mathematical model of KPR we show that the threshold half-life in our opto-ligand-TCR system is 8 s.

![Figure 1.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig1-v2.jpg)

**Figure 1.:** Light of 660 nm and 740 nm wavelength reversibly switches PhyB between the OFF and ON states. In the ON state PhyB tetramers (PhyBt) bind to and cluster GFP-PIFS-TCRs leading to signaling and the activation of the T cell. The red dot indicates the fluorophore-coupled streptavidin tetramer.

## Results

The first aim of our study was to establish an optogenetic system in which ligand binding to the TCR can be reversibly controlled by light (Figure 1).

### Engineering of the opto-ligand-TCR system: the ligand

The light-responsive N-terminal 651 amino acids of A. thaliana PhyB (PhyB1-651) have been used as an optogenetic tool (Adrian et al., 2017; Baaske et al., 2019; Beyer et al., 2015; Beyer et al., 2018; Johnson and Toettcher, 2018; Levskaya et al., 2009; Müller et al., 2013b; Toettcher et al., 2013) and the photobiology of this fragment has been described previously (Smith et al., 2016). Here we used this PhyB form as a ligand. PhyB1-651 fused to the biotinylation site Avitag (Beckett et al., 1999) and a His6-tag (Figure 2A) was produced in E. coli. Additionally, the bacteria were engineered to produce the cyanobacterial version of the phytochrome chromophore, phycocyanobilin (Essen et al., 2008; Smith et al., 2016). PhyB1-651-Avitag-His6, called PhyB in the remainder of this article, was isolated by Ni2+-affinity chromatography (Smith et al., 2016). We then tested the functionality of PhyB through its light-dependent interaction with PIF6. To this aim, we produced the first 100 amino acids of A. thaliana PIF6 (PIF61-100), which were shown to be sufficient for photoreversible PhyB binding with nanomolar affinity (Tischer and Weiner, 2014), as a fusion protein with the maltose-binding protein and a His6-tag [MBP-PIF61-100-His6, from now on called MBP-PIF(wt)]. After illuminating a mixture of PhyB and an excess MBP-PIF(wt) with saturating 660 nm light, 70% of the PhyB molecules were complexed with PIF as depicted by a shift in elution from a size exclusion chromatography column (Figure 2B). This was not the case when the proteins were exposed to 740 nm light. Since at photoequilibrium under 660 nm light only 80% of the PhyB molecules are in the ON state (Bae and Choi, 2008; Smith et al., 2016), we conclude that the majority of PhyB molecules were functionally active.

![Figure 2.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig2-v2.jpg)

**Figure 2.:** (A) Schematics of the PhyB1-651 construct and the PhyB tetramers. PCB = phycocyanobilin. (B) Purified PhyB was illuminated with 660 nm light [PhyB(660)] and added in a 1:2 molar ratio to MBP-PIF(wt). The proteins were separated by gel filtration and PhyB was detected by its absorbance at the isosbestic point of 671 nm. PhyB molecules around 14.5 ml elution volume are the free PhyB molecules and the ones around 12.5 ml are the PhyB-MBP-PIF complexes. As controls, PhyB illuminated with 740 nm light [PhyB(740)] plus MBP-PIF(wt) and PhyB alone was only detected at 14.5 ml elution volume. Results show one experiment of n > 3. (C) Affinity chromatography-purified PhyB was mixed in a 10:1 molar ratio with streptavidin-DyLight650, incubated for 2 hr at room temperature and the formed PhyB tetramers (PhyBt) were isolated from monomers using size-exclusion chromatography. The elution of PhyB was monitored via its absorbance at 365 nm. Results show one experiment of n > 3.

Although soluble TCR ligands are active as dimers (Boniface et al., 1998; Cochran et al., 2000; Minguet and Schamel, 2008; Minguet et al., 2007), tetrameric pMHC based on streptavidin are routinely used to stimulate the TCR (Altman et al., 1996) and to obtain insight into ligand discrimination by T cells (Stone et al., 2011; Stone et al., 2001). Thus, we wanted to construct PhyB tetramers (PhyBt) to be used as ligands in our system (Figure 1). To this end, biotinylated PhyB was tetramerized using fluorophore-coupled streptavidin. After separating the tetramers from monomers by size exclusion chromatography (Figure 2C), we obtained purified PhyBt that we used in this work.

### Engineering of the opto-ligand-TCR system: the TCR

Next, we engineered a PIF-fused TCR that can bind to and be activated by PhyBt when the PhyB molecules are in the ON (but not in the OFF) state (Figure 1). In plants PIF6 is produced in the cytoplasm, whereas in our system PIF6 is produced in the oxidative environment of the endoplasmic reticulum. Therefore, we mutated cysteines and N-linked glycosylation sites (Asn-X-Ser/Thr) in PIF6. We produced a panel of five different PIF61-100 mutants abolishing cysteines 9 and 10 as well as asparagine 35 or serine 37 as MBP fusion proteins (Figure 3—figure supplement 1A,B). We analyzed the interaction of PhyB with these PIF61-100 mutants under limiting amounts of MBP-PIF using size exclusion chromatography (Figure 3—figure supplement 1C,D). All mutants formed complexes with PhyB pre-illuminated with 660 nm light [PhyB(660)] similar to MBP-PIF(wt).

Having seen that all PIF61-100 mutants interacted well with PhyB, they were fused - preceded by a signal peptide - to the N-terminus of the human HA1.7 TCRβ chain that contains a Vβ3 variable region (Hennecke et al., 2000; Hewitt et al., 1992) (Figure 3A). We analyzed the presence of the different PIF61-100-TCRβ constructs on the cell surface following lentiviral transduction of Jurkat T cells (Abraham and Weiss, 2004). PIF61-100 C9S C10S S37A [PIF(SSA)] showed the highest surface presence (Figure 3B), indicating that it assembled to a complete TCR complex (Alarcón et al., 2003; Call and Wucherpfennig, 2005). Hence, PIF(SSA) was therefore used for all future optimizations and termed secretory PIF or PIFS (Figure 3C). Surprisingly, despite the good interaction of MBP-PIFS with PhyB in size-exclusion chromatography (Figure 3—figure supplement 1C,D), no binding of PhyBt to the PIFS-TCR on the surface of Jurkat cells could be detected (Figure 3D). GFP-PIFS-TCR cells (described below) served as a positive control for binding (Figures 3D and 4F panels are from the same experiment). Furthermore, PIFS-TCR Jurkat cells could be stimulated to flux calcium via cross-linking of the PIFS-TCR using an anti-Vβ3 antibody, but not using PhyBt pre-illuminated with 660 nm light, called PhyBt(660) (Figure 3E). Consequently, although PIFS-TCRβ is present at the cell surface and PIFS itself binds to PhyB (in the form of MBP-PIF), PIFS loses its binding capacity towards PhyB when it is fused to the TCR and exposed on the T cell’s surface.

![Figure 3.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig3-v2.jpg)

**Figure 3.:** (A) Schematics of the PIF-TCRβ constructs, including wild-type and mutant PIF. SP depicts the signal peptide and the arrow the signal peptidase cleavage site. The schematic constructs are drawn to scale with the scale bar indicated. (B) The presence of the different PIF-TCRs and a single chain variable fragment (scFv)-TCR on the cell surface was measured in lentivirally transduced Jurkat cells together with the parental cell line using an anti-Vβ3 antibody (Jovi3) via flow cytometry. The median fluorescence intensity (MFI) averaged for three experiments ± SEM is depicted. (C) Scheme of PIFS-TCRβ as integrated into the TCR. (D) 100 nM phycoerythrin (PE)-labeled PhyBt pre-illuminated with 660 nm or 740 nm light were incubated with Jurkat, PIFS-TCR Jurkat and GFP-PIFS-TCR cells and binding detected by flow cytometry. Numbers depict the % of cells in the respective quadrant. Results show one experiment of n = 3. (E) PIFS-TCR cells were labeled with Indo-1 and calcium influx measured by flow cytometry. 100 nM PhyBt(660) (orange) or 1 µg/ml anti-Vβ3 antibody (blue) were added as stimuli. Their addition is marked by an arrow and the illumination procedure by a bar above the graph (grey = dark). Results show one experiment of n > 3.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) The first 100 amino acids of different PIF proteins from A. thaliana were aligned using MUSCLE. Cysteines are marked in yellow and asparagines that are used for N-linked glycosylation in blue. The highly conserved region that most likely constitutes the PhyB-binding site (Khanna et al., 2004) is boxed and was not mutated. The residue numbering is based on PIF6. (B) We fused the maltose-binding protein (MBP) of E. coli to the first 100 amino acids of PIF6 (PIF61-100) and a His6-tag for purification. We mutated Cys9, Cys10, Asn35 or Ser37 and the resulting mutant MBP-PIF61-100 molecules are shown alongside the wild-type MBP-PIF61-100 molecule. (C) 200 µg recombinant PhyB (see Figure 2) was illuminated with 660 nm light [PhyB(660)] and added in a 2:1 molar ratio to MBP-PIF(SSA). The mixture was incubated for 60 min at room temperature. We used a molar excess of PhyB to not saturate PIF-binding to PhyB. The proteins were then separated by gel filtration using a Superdex 200 10/300 GL column and PhyB was detected by its absorbance at 671 nm (grey line). PhyB molecules around 14.5 ml elution volume are the free PhyB molecules and the ones around 12.5 ml are the PhyB-MBP-PIF complexes, showing that approximately 60% of the PhyB molecules were PIF bound under these conditions. As controls, MBP-PIF alone did not absorb at 671 nm and PhyB alone was only detected at 14.5 ml elution volume. One representative experiment is depicted of n = 3. (D) Quantification of the binding data from (C) using all MBP-PIF variants, demonstrating that all mutants bound similarly to PhyB(660) as the wild-type MBP-PIF. Shown are the mean of 3 independent experiments ± SEM.

![Figure 4.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig4-v2.jpg)

**Figure 4.:** (A) Schematics of the GFP-PIFS-TCRβ constructs, including three different furin cleavage sites (F1, F2, F3) or omitting any cleavage site (noF). SP depicts the signal peptide, the arrow the signal peptidase cleavage site and moxGFP the monomeric GFP optimized for an oxidative environment. (B) The surface expression of the different GFP-PIFS-TCRs and PIFS-TCR was measured in transduced Jurkat cells together with the parental cell line using an anti-Vβ3 antibody (Jovi3) via flow cytometry. (C) Analogous to (B), the amount of GFP was quantified on the surface of the different transductants using a polyclonal anti-GFP antibody via flow cytometry. (B) and (C) depict the median fluorescence intensity (MFI) averaged for three measurements ± SEM. (D) Scheme of GFP-PIFS-TCRβ as integrated into the TCR. (E) 100 nM phycoerythrin (PE)-labeled PhyBt pre-illuminated with 660 nm or 740 nm light were incubated with the cells indicated and binding was detected by flow cytometry. One experiment out of three is depicted displaying the average of quadruplicates ± SEM. (F) Together with Figure 3D these are the GFP vs PhyBt plots of the experiment quantified in (E).

A major difference between the functional MBP-PIFS and the dysfunctional PIFS-TCRβ construct is the C- and N-terminal localization of PIFS, respectively. Thus, adding an unrelated protein to the N-terminus of PIFS might rescue the PhyB-binding ability of the PIFS-TCR. To test this possibility, we attached a monomeric green fluorescent protein optimized for the oxidative environment of the endoplasmic reticulum (moxGFP, (Costantini et al., 2015)) to the N-terminus of PIFS-TCRβ. We distinguished the effect of a permanently attached moxGFP or a moxGFP that is only present during folding of PIFS in the endoplasmic reticulum. To this end, we added different furin protease recognition sequences (F1-F3) or a flexible linker without protease cleavage site (noF) between moxGFP and PIFS (Figure 4A). The protease furin is expressed in the Golgi and would cleave off the moxGFP as the engineered TCRs are exported to the cell surface. All constructs were well expressed on Jurkat cells (Figure 4B) and showed the expected absence or presence of moxGFP on the cell surface (Figure 4C). The construct using a truncated furin site (F3) had intermediate surface moxGFP levels, indicating that moxGFP is inefficiently cleaved. PhyBt(660) hardly bound to the surface of Jurkat cells expressing GFP-F1-PIFS-TCR or GFP-F2-PIFS-TCR with efficiently cleaved moxGFP (Figure 4E,F). However, fusing moxGFP permanently to PIFS-TCRβ resulted in strong light-dependent binding of PhyBt to the cell surface. In line with this, GFP-F3-PIFS-TCR with partly cleaved GFP bound intermediate amounts of PhyBt(660). These data suggest that moxGFP has to be present at the GFP-PIFS-TCR on the cell surface, in order for PIFS to bind to PhyBt(660). The optimized construct, moxGFP-noF-PIFS-TCR, will be called GFP-PIFS-TCR in the remainder of this article.

In conclusion, through several steps of engineering and optimization we generated the opto-ligand-TCR interaction system (Figure 1) based on the red/far-red light-regulated PhyB-PIF pair.

### The GFP-PIFS-TCR is switched ON with 660 nm and OFF with 740 nm light

PhyBt(660) bound to cells expressing the GFP-PIFS-TCR, whereas PhyBt pre-illuminated with 740 nm light [PhyBt(740)] did not (Figure 4E,F). Binding induced TCR signaling, since addition of PhyBt(660), but not PhyBt(740), resulted in a strong calcium influx into the cells similar to a stimulation using an anti-TCR antibody (Figure 5A,B). The experiment was done in the dark, since in the absence of any light, the PhyB molecules rest in their state (ON or OFF) for time scales exceeding the duration of the calcium experiments (Smith et al., 2017; Smith et al., 2016). 660 nm light alone in the absence of PhyBt or GFP-PIFS-TCR did not evoke signaling; similarly Jurkat cells not expressing the GFP-PIFS-TCR could not be stimulated with PhyBt(660) (Figure 5—figure supplement 1A,B). Both experiments show that the light acted through inducing PhyBt binding to GFP-PIFS-TCR. Furthermore, as seen with soluble pMHC ligands (Boniface et al., 1998; Cochran et al., 2000; Minguet et al., 2007), PhyB monomers (in contrast to tetramers) could not stimulate calcium influx (Figure 5—figure supplement 1C). Lastly, stimulation with bead-coupled PhyBt(660) in the dark resulted in up-regulation of the activation marker CD69 (Figure 5C). Together these data show that light-mediated PhyBt-binding to GFP-PIFS-TCR induced TCR signaling and T cell activation.

![Figure 5.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig5-v2.jpg)

**Figure 5.:** (A) GFP-PIFS-TCR cells were labeled with Indo-1 and calcium influx measured by flow cytometry. The arrow marks the addition of the stimuli indicated, and the grey rectangle the absence of any light. Results show one experiment of n > 3. (B) Calcium influx into GFP-PIFS-TCR cells stimulated with anti-Vβ3, PhyBt(660), PhyBt(740) or PBS was measured as in (A). Results show one experiment of n > 3. (C) GFP-PIFS-TCR Jurkat cells were incubated with PhyBt bound to sepharose beads after a 30 s 660 nm or 740 nm light pulse for 6 hr. Expression of CD69 was quantified by flow cytometry using an APC-labeled anti-CD69 antibody. Data points depict two experiments. (D) Calcium influx was measured as in (A). PhyBt(660) induced calcium influx (blue and orange lines). After 2 min a 1 s short pulse of 100% intensity 740 nm light (red break in the grey bar) terminated the calcium response (blue line). Addition of PhyBt(740) did not induce calcium influx (red line). Results show one experiment of n > 3.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Calcium influx was only seen in cells expressing GFP-PIFS-TCR and treated with PhyBt(660) (orange line). Cells lacking GFP-PIFS-TCR (parental Jurkat, grey and blue lines) or treatment with PhyBt(740) (red line) did not lead to intracellular calcium mobilization. Stimuli addition is marked by an arrow and the illumination procedure by a bar above the graph (grey = dark); One representative experiment is depicted of n = 2. (B) Treatment of GFP-PIFS-TCR cells with 660 or 740 nm light alone in the absence of PhyBt did not induce calcium influx (grey and blue lines). Addition of PhyBt(660) elicited a calcium response, whereas PhyBt(740) did not. Stimuli addition is marked by an arrow and the illumination procedures by bars above the graph (grey = dark, orange = 660 nm, red = 740 nm); One representative experiment is depicted of n = 3. (C) In contrast to PhyBt(660) (orange line) the PhyB(660) monomers (blue line) did not stimulate calcium influx in the GFP-PIFS-TCR cells. As controls, both PhyB forms illuminated with 740 light (red and grey lines) did not evoke any calcium influx; One representative experiment is depicted of n = 3. Panels A, B and C are from the same experiment.

The PhyB-PIF system allows the rapid switching between the ON and OFF states in both directions. When we switched PhyBt from the ON to the OFF state by a 1 s pulse of 740 nm light, we stopped the ongoing calcium response initially evoked by PhyBt(660) (Figure 5D), demonstrating that our system is reversible.

### The intensity of continuous 660 nm light determines GFP-PIFS-TCR activation

Having established the opto-ligand-TCR system, the second aim of our study was to test the kinetic proofreading (KPR) model.

The KPR model predicts that the half-life of the ligand-TCR interaction determines TCR signaling. Here, we wanted to implement a protocol to control this half-life by light and study the consequences for TCR signaling. To this end, we exploited the property of PhyB that its continuous exposure to 660 nm light triggers both the switch from PhyB OFF to ON and the reverse switch from ON to OFF (Figure 6A) as the absorption spectra of both PhyB states partially overlap (Rockwell et al., 2006). Thus, each individual PhyB molecule constantly shuttles between the ON and OFF state under 660 nm light, with high 660 nm intensities leading to a faster shuttling rate and thus to shorter binding duration (note that in Figure 5 continuous light was not used and the PhyB molecules stayed in their ON or OFF state for the duration of the experiment). Accordingly, continuous high intensity (100%) 660 nm light prevented calcium influx when PhyBt(660) was added to the GFP-PIFS-TCR cells (Figure 6B, orange line). After 390 s the constant 660 nm illumination was stopped, so that the PhyB molecules that were in the ON state at this moment were trapped in this state. This allowed them to bind long enough to the TCR and to induce a strong calcium response (Figure 6B). This experiment also demonstrates that the constant high intensity 660 nm illumination did not harm the cells.

![Figure 6.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig6-v2.jpg)

**Figure 6.:** (A) Schematics of the different PhyB conversions under 660 nm and 740 nm light. In the dark the PhyB states do not change in the timescales relevant for this work. (B) Calcium influx was measured as in Figure 5. GFP-PIFS-TCR cells were constantly illuminated with 100% intensity 660 nm light (orange line). After 150 s PhyBt(660) was added (arrow) and after 390 s the light was switched off. As controls, PhyBt(660) (blue line) or PhyBt(740) (red line) was added to the cells in the dark. The bars represent the illumination procedure during the measurement (grey = dark, orange = 660 nm light). (C) 20 nM PhyBt(660) was added (arrow) after 90 s to GFP-PIFS-TCR cells continuously illuminated with 660 nm light of the depicted intensities. Results in (B) and (C) show one experiment of n > 3. (D) Quantification of experiments done as in (C) with the indicated PhyBt concentrations. Duplicates are shown with connecting lines going through the mean.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) A threshold of the 660 nm light intensity to induce a calcium response. The data from Figure 6D were normalized for each PhyBt concentration by setting the value of dark (0% intensity) to 1.0 and value of 32% intensity to 0 to better visualize the overlap of the different curves. Duplicates are shown with connecting lines going through the mean. (B) Calcium influx was measured as in Figure 5. After 85 s of measurement 20 nM PhyBt(660) was added (arrow) to GFP-PIFS-TCR cells in the dark. After 205 s cells were illuminated with 660 nm light of the depicted intensities, or with 740 nm light (red line). As a control, cells were kept in the dark (black line). The result shows one representative experiment of n = 3. (C) Quantification of experiments done as in (B) using normalization as in (A). Shown are the mean of 3 independent experiments ± SEM.

The intensity of 660 nm light determines the half-life of both PhyB states and consequently the switch rates between the ON and the OFF state. However, the 80:20 molar ratio of PhyB ON to OFF molecules at photoequilibrium is largely independent of the light intensity (Figure 6A) (Bae and Choi, 2008; Smith et al., 2016). Lowering the 660 nm intensity increases the half-life of PhyB ON without altering its concentration, and hence may allow PhyBt to bind for longer durations to the GFP-PIFS-TCR. Indeed, at 4% and 2% constant 660 nm intensity, calcium influx was evoked (Figure 6C). These percentage values refer to the maximum intensity of 100% that was determined by the light source we used. We observed a threshold of the PhyB ON half-life in inducing a calcium response that was largely independent of the PhyBt concentration, a crucial property of TCR ligand discrimination (McKeithan, 1995) (Figure 6D and Figure 6—figure supplement 1A). This threshold half-life was at 3% 660 nm intensity. Thus, we were able to control TCR signaling by changing the intensity of continuous 660 nm light, suggesting that the duration of the ligand-TCR interaction controls calcium signaling.

Next, we tested whether very fast kinetics can terminate an ongoing TCR signal. GFP-PIFS-TCR cells were stimulated with PhyBt(660) in the dark, inducing a strong calcium response (Figure 6—figure supplement 1B). During this response the long binding events were changed to fast binding events by illuminating with high intensity continuous 660 nm light (32% and 16%). As expected, the calcium signal was stopped, similar as when using 740 nm light (Figure 6—figure supplement 1B and Figure 5D). The calcium response was not stopped when low intensity continuous 660 nm light (2% and 4%) was used, where the half-life of binding is still long. The threshold half-life of the PhyBt-GFP-PIFS-TCR interaction to maintain the calcium response was again at 3% 660 nm intensity (Figure 6—figure supplement 1C).

In conclusion, we engineered the opto-ligand-TCR system, in which one single ligand-TCR pair explores a wide range of different binding half-lives when changing the intensity of red light and in which other parameters of the interaction remain constant, because we have not mutated the binding interface.

### A mathematical model describing KPR in the opto-ligand-TCR system

Next, we developed a mathematical model and confronted it with the experimental data, to obtain quantitative insight into how the half-life of the PhyB ON-TCR complex determines TCR signaling. The model comprises the PhyB ON-OFF cycle, binding of PhyBt to the TCR, and potentially KPR (Figure 7A, Figure 7—figure supplements 1 and 2 and Appendix 2). In the absence of KPR, the activity of each component in the signaling network depends only on the activity of its immediate upstream component(s), making TCR occupancy the ultimate source of ligand discrimination. In contrast, KPR assumes that the first signaling steps at the receptor in addition depend on the half-life of the ligand-TCR complex, while only the more downstream components respond exclusively to the activity of their immediate upstream component(s). We refer to the time required to complete the first half-life-dependent signaling steps as KPR duration or KPR time, τKPR.

![Figure 7.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig7-v2.jpg)

**Figure 7.:** (A) The PhyB ON-OFF cycle, binding of PhyB ON to the TCR and kinetic proofreading (KPR) were combined into one model. (B) In this model the effective off-rate is a linear function, and (C) the effective affinity is the reciprocal of a linear function, of the 660 nm light intensity. (D) A likelihood ratio test (null hypothesis: τKPR = 0, i.e., no KPR; alternative hypothesis: τKPR > 0) strongly supports the existence of a KPR mechanism. (E) The amount of PhyBt bound to the GFP-PIFS-TCR cells and (F) calcium influx at different continuous 660 nm light intensities (from Figure 6D) and different PhyBt concentrations are plotted. The line and shaded area represent the fit and the estimated uncertainties of the KPR model. The data points represent the mean ±SEM of 6–9 replicates in (E), or individual data points of two experiments in (F).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Basic scheme of kinetic proofreading (KPR) according to McKeithan (McKeithan, 1995). Upon formation of an active TCR conformation (rate kform), the receptor has to undergo n modification steps, each with the same rate kp, in order to establish a signal. If the active conformation decays at any stage (rate kdec), all modifications are removed rapidly. The time span from forming an active TCR conformation (i.e., from the second binding event of the bivalent ligand binding) to signal initiation is termed the KPR duration τKPR. (B) The fraction of signaling receptors among all receptors in the active conformation in dependence on the half-life of the active conformation τactive = ln(2)/kdec, expressed relative to the duration of the KPR mechanism τKPR. Shown are curves that share the same KPR duration but differ in the number of steps.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A) PhyB can reversibly interconvert between the ON and the OFF state. (B) Only the PhyB in the ON state can bind to GFP-PIFS-TCRs. (C) If exposed to light, PhyB ON can convert to PhyB OFF while still in complex with a GFP-PIFS-TCR (left). Because dissociation in this state is very fast, conversion into PhyB OFF effectively increases the off-rate of the GFP-PIFS-TCRs-PhyB ON complex (right). (D) Extension of the model to account for the oligomeric structure of the PhyB ligands. Since TCRs are required to be cross-linked for signaling in our experimental setup, only multivalently bound PIF-TCRs can induce an intracellular signal.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Photoconversion rates of PhyB were measured in the presence or absence of MBP-PIF(wt) by tracking the fraction of converted PhyB every 10 s using absorbance spectra acquisition. Conversion from a pool of solely PhyB OFF to PhyB ON and vice versa (the latter starting with the achievable 4:1 ON:OFF ratio) was induced by illumination with 70 µmol m−2 s−1 660 nm (orange bars) or 740 nm (red bars) light. MBP-PIF(wt) binding to PhyB did not influence the photoconversion rate. Shown are the mean ±SEM of three independent experiments, tested with two-way ANOVA. P-value with vs without MBP-PIF(wt) is 0.52.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** Amount of bound PhyBt on the surface of GFP-PIFs-TCRs under different continuous 660 nm light intensities and PhyBt concentrations as indicated. PhyBt(660) were added to the cells under continuous 660 nm light and incubated for 90 s at 37°C. Subsequently, samples were washed in the dark and the tetramer fluorescence (DyLight650 at streptavidin) analyzed by flow cytometry. Connecting lines going through the mean of 6–9 replicates, error bars depicting the SEM.

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig7-figsupp5-v2.jpg)

**Figure 7—figure supplement 5.:** Kinetic proofreading (KPR) is required to explain the data if the off-rates of mono- and multivalent binding (koff respectively qoff) are the same. Allowing the off-rates to be distinct from each other in the absence of KPR does not improve the fit.

We used a soluble TCR ligand for which - in case of antibodies or pMHC - it was shown that bivalent binding is required to activate the TCR (Boniface et al., 1998; Cochran et al., 2000; Kaye and Janeway, 1984; Minguet et al., 2007), and this most likely was also the case for our opto-ligand-TCR system (Figure 5—figure supplement 1C). Thus, the KPR duration in our system is the time from bivalent binding to the completion of the biochemical signaling steps (Figure 7—figure supplement 2).

KPR requires the bivalently bound PhyBt-TCR complex to exist for at least the KPR time, in order to generate a signal that then leads to a calcium response more downstream (Altan-Bonnet and Germain, 2005; Davis and van der Merwe, 2006; Lever et al., 2016; McKeithan, 1995) (Figure 7A, bivalent binding is shown in Figure 7—figure supplement 2). Thus, the time delay between bivalent ligand binding and calcium influx consists of the KPR duration plus the extra time beyond KPR required for the additional signaling steps until opening of the calcium channels. The half-life of the bivalent PhyBt-TCR complex is determined by the sum of the light-independent off-rate of PhyB ON from the TCR, koff, and the light intensity-dependent rate ki with which PhyB molecules return to the OFF state, detaching from the TCR (Figure 7B).

In support of the model (Figure 7A), we experimentally demonstrated that the rate of converting PhyB from ON to OFF is the same for free PhyB and PIF-bound PhyB (Figure 7—figure supplement 3). These data imply that PhyB molecules also convert to OFF while being bound to PIF and thereby the PhyB-PIF interaction is lost. Hence, the effective off-rate and binding affinity of PhyB ON to the TCR are also light-dependent (Figure 7B,C). Taken together, the model predicts that the amount of TCR-bound PhyB decreases with increasing light intensity, which we confirmed experimentally (Figure 7—figure supplement 4). Importantly, the change of PhyB ON affinity is a straightforward consequence of the light-controlled PhyB ON half-life (this contrasts with mutated pMHC ligands (Altan-Bonnet and Germain, 2005; Daniels et al., 2006; Davis and van der Merwe, 2006; Holler and Kranz, 2003; Lever et al., 2016), where affinity changes can be brought about by changes in both on- and off-rates, and potentially other parameters such as orientation of binding (Adams et al., 2011)).

### Experimental data and modeling demonstrate that KPR takes place

Although we intended to only change the ligand-TCR half-life with light, we also changed the affinity, due to the intrinsic relationship between off-rate and affinity. Hence, the intensity of 660 nm light regulates both the half-life of PhyB ON and the amount of bound PhyBt. To disentangle the half-life from the amount of ligand-bound TCRs, we asked whether calcium signaling was directly sensitive to the PhyB ON half-life through KPR or solely responded to the level of TCR occupancy with PhyB ON (absence of KPR). We fitted both mathematical models, the one with and the one without KPR, to the PhyBt binding and calcium signaling data together. Only the model with KPR yielded a satisfactory fit, and a likelihood ratio test, with the absence of KPR being the null hypothesis and the presence of KPR being the alternative hypothesis, showed highly significant support for the KPR model (p<10−6, Figure 7D,E,F and Figure 7—figure supplement 5). Taken together, these findings strongly support the existence of KPR at the TCR.

### The KPR time in Jurkat cells using the opto-ligand-TCR is 8 s

The steady-state data (Figure 7E,F) prevented the model to deduce the KPR time τKPR, yielding only the product τKPR · koff. To overcome this limitation, we determined the conversion kinetics of PhyB in our experimental system by illuminating PhyBt OFF with short light pulses of 660 nm light and subsequently switching to darkness. This protocol traps the ligands in the ON state, which we quantified through the resulting calcium signal (Figure 8A and Appendix 2). The resulting kinetics of switching PhyB to the ON state was highly consistent across different light intensities and PhyBt concentrations (Figure 8B) and were described well by the mathematical model. Importantly, combining the steady-state data (Figure 7E,F) and the kinetic data (Figure 8B) was sufficiently informative to identify all five parameters of the model (Figure 8—figure supplement 1). Utilizing the kinetic data, we determined the half-life of the PhyB ON-TCR complex, ln2 /(koff +ki), which varied from 40 s to 2 s over the range of light intensities used (Figure 8C). We determined the threshold half-life of the bivalent PhyBt-TCR interaction, i.e. the proofreading duration τKPR, to be 8 s (95% CI: 3 s, 19 s) (Figure 8D). Thus, for a threshold half-life of bivalent binding of PhyBt to the TCR complex of 8 s, signaling from the active TCR is half-maximal. Furthermore, our results largely exclude the possibility of fast rebinding events, which would have effectively prolonged the half-life of the PhyB ON-TCR complex sensed by a KPR mechanism (Aleksic et al., 2010; Govern et al., 2010) (Appendix 2).

![Figure 8.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig8-v2.jpg)

**Figure 8.:** (A) 20 nM PhyBt(740) was added to GFP-PIFS-TCR cells and a 660 nm pulse of 100% intensity was given for the indicated durations. The calcium influx was quantified over time, indicating that longer pulse durations switch more PhyB OFF molecules to the ON state. Stimuli addition is marked by an arrow and the illumination procedure by a bar above the graph (grey = dark, orange = 660 nm). (B) Experiment as in (A) were performed using 6.3 nM or 20 nM PhyBt and 32% or 100% intensity 660 nm light. The data is shown together with the fit and estimated SD. Results in (A) and (B) show one experiment of n > 3. (C) The estimated half-lives of the PhyB-TCR complex in dependence on the light intensity. (D) The profile likelihood of the KPR time shows that the 95% confidence interval (CI) ranges from 3 s to 19 s, while the best-fit value is 8 s.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** The confidence intervals were computed using the profile likelihood method.

## Discussion

In this study, we engineered a tailor-made optogenetic system, the opto-ligand-TCR, to control a ligand-receptor interaction by light, allowing us to overcome current experimental limitations. In fact, one single ligand-TCR pair (the PhyBt - GFP-PIFS-TCR pair) can explore a wide range of different binding half-lives when changing the intensity of 660 nm light. Indeed, our approach exploits the remarkable, but in optogenetics so far unexplored, biophysical property of PhyB that the intensity of 660 nm light determines the half-life of the PhyB ON state (Bae and Choi, 2008; Rockwell et al., 2006; Smith et al., 2016) and thus the half-life of the ligand-TCR interaction. Other parameters of the interaction remain constant, because the binding interface is always the same under the different light conditions. Together with a mathematical model, our data show that KPR can explain ligand discrimination by T cells.

Furthermore, using the PhyB-PIF pair enables switching ON and OFF ligand binding (short pulse of 660 and 740 nm light, respectively) in less than a second (Figure 8B). Importantly, we show that 740 nm light actively disrupts an existing PhyB-PIF interaction, rather than preventing rebinding. Both features, the light-induced switch between both states and the light intensity-dependent change in the binding dynamics, is only found with phytochromes and not with other optogenetic or synthetic systems (Kolar et al., 2018; Smith et al., 2016).

Previously, light has been used to induce ligand-binding to the TCR. A lysine side chain of the peptide presented by MHC was modified with a light-sensitive caging group (Huse et al., 2007). This modified pMHC could not bind to the TCR until a short UV light pulse (microsecond range) removed the caging group. Subsequently, pMHC could bind and stimulate signaling. In contrast to the opto-ligand-TCR system, this approach is not reversible, thus not allowing varying the half-life. Another approach is presented in the accompanying paper by Tischer and Weiner (Tischer and Weiner, 2019). It uses a blue-light responsive optogenetic tool, namely the LOVTRAP system (Wang et al., 2016). In this case LOV2 binds to a chimeric antigen receptor and the blue light intensity controls the duration of binding. In analogy to our data, they show that the half-life of ligand binding controlled T cell activation.

The opto-ligand-TCR system was not only able to provoke calcium and Erk MAP kinase signaling (not shown), but also led to the stimulation of the T cell as measured by the upregulation of the activation marker CD69. This is in line with systems where other binding domains were fused to the TCR (single chain Fv and DNA, (Minguet et al., 2007; Schamel and Reth, 2012; Taylor et al., 2017), indicating that the TCR can be fully stimulated in synthetic settings and not only by pMHC. This feature is also exploited in chimeric antigen receptors used for cancer immunotherapy (Lim and June, 2017; Sadelain, 2016).

Our opto-ligand-TCR system allowed us to show that T cells discriminate between ligands due to differences in the ligand-TCR half-lives (Figure 8), consistent with KPR models (Altan-Bonnet and Germain, 2005; Davis and van der Merwe, 2006; Lever et al., 2016; McKeithan, 1995). Using the identical ligand-TCR pair for the different half-lives excludes differences in binding geometry (Adams et al., 2011), forces (Kim et al., 2009; Liu et al., 2014) or conformational changes (Gil et al., 2002) as discriminatory parameters in this setup. Furthermore, we measured total binding, the binding kinetics and the activation readout in the same experimental system. Thus, all parameters for the mathematical model are derived using identical conditions. This is often different when using pMHC and variants thereof as ligands for the TCR: the binding parameters are derived by surface plasmon resonance at 25°C using recombinant parts of the proteins (ectodomains of pMHC and only the immunoglobulin domains of the TCRα and TCRβ subunits) and the activation assays are done with native, membrane or surface bound proteins at 37°C (Aleksic et al., 2010; Dushek et al., 2011; Govern et al., 2010; Holler and Kranz, 2003; Krogsgaard et al., 2003). Thus, it is often unclear how well these different biological setups can be compared and compiled into one model.

Besides our and other studies on the correlation of binding parameters with the biological activity of the ligands, differential CD3ζ phosphorylation is another hint for KPR. CD3ζ is a signaling subunit of the TCR that can be partially or fully phosphorylated. Low affinity pMHC, which are non-stimulatory, lead to partial phosphorylation, whereas high affinity pMHC, which are stimulatory, lead to full phosphorylation of CD3ζ (Madrenas et al., 1995; van Oers et al., 1993). This is consistent with the idea that the low affinity ligands only bind shortly, not allowing all phosphorylation steps to be completed and high affinity ligands bind long enough to complete all phosphorylations. Indeed, increasing the concentration of the low affinity binders did not lead to full CD3ζ phosphorylation (Madrenas et al., 1997), being consistent with KPR.

Interestingly, changing the half-life of PhyB ON and thus the lifetime of the ligand-TCR interaction also altered the amount of bound receptors, and with the help of the mathematical model we could show that the half-life was the decisive parameter for the magnitude of T cell stimulation as measured by calcium influx. We calculated the threshold half-life above which TCR stimulation occurs, i.e., the KPR duration, to be 8 s. For soluble TCR ligands, as we have used here, it has been shown that bivalent binding is required to trigger the TCR (Boniface et al., 1998; Cochran et al., 2000; Kaye and Janeway, 1984), possibly due to both a lack of clustering and stabilization of conformational changes of the TCR (Minguet et al., 2007; Schamel et al., 2017; Swamy et al., 2016). Indeed, also in our case PhyB monomers did not activate the TCR whereas PhyB tetramers (PhyBt) did. Thus, the PhyBt ligands needed to bind for at least 8 s bivalently, in order to stimulate calcium influx that itself occurred later. Of note, the KPR duration is not identical to the time delay between ligand binding and calcium influx or other downstream events (Figure 9). A time delay is a prerequisite for KPR, but does not necessarily indicate that KPR takes place.

![Figure 9.](https://cdn.elifesciences.org/articles/42475/elife-42475-fig9-v2.jpg)

**Figure 9.:** Ligands that bind shorter than the KPR time of 8 s (half-life of binding) fail to induce efficient TCR signaling. Ligands that bind longer allow the completion of several biochemical steps (white arrows) that result in an activatory signal by the TCR. This signal provokes further signaling (grey arrows) that ultimately leads to T cell activation.

In line with our 8 s KPR time, the accompanying paper by Tischer and Weiner found a KPR time of approximately 7 s (Tischer and Weiner, 2019). This study also used Jurkat cells, but a different optogenetic system, a different activation readout and a chimeric antigen receptor instead of a TCR. Thus, independent of the readout and exact design of the optogenetic system Jurkat cells have a TCR/-chimeric antigen receptor based KPR time of 7–8 s. Most other studies have calculated a KPR time of between 1–5 s (Aleksic et al., 2010; Altan-Bonnet and Germain, 2005; Daniels et al., 2006; Govern et al., 2010; Holler and Kranz, 2003; Kersh et al., 1998) and the time delay between ligand binding and calcium influx was 7 s in one study (Huse et al., 2007). In contrast to those studies, our and the Tischer/Weiner systems lack the co-receptor CD4 and CD8 that have been shown to increase the speed of signaling, most likely by efficiently recruiting the kinase Lck to the TCR (Artyomov et al., 2010; Holler and Kranz, 2003; Veillette et al., 1988). Differences in the cellular background (primary murine T cells versus the human T cell line Jurkat) might also contribute to differences in the KPR time, e.g., if the concentration of kinases or phosphatases was different (Altan-Bonnet and Germain, 2005).

The half-life of the interaction is a population average over many binding events. Thus, it might be that individual binding events longer than the threshold half-life (8 s in our case) are the ones that triggered T cell activation, as suggested recently (Lin et al., 2019). The opto-ligand-TCR system is well suited to precisely control the exact binding time (and not the average half-life) by using 740 nm light to break the ligand-TCR interaction.

An aspect to consider in KPR is a potential contribution of fast rebinding of ligands to TCRs (Aleksic et al., 2010; Govern et al., 2010). When the on-rate of multivalent binding of the pMHC-TCR interaction is sufficiently fast, dissociated TCRs are rebound before KPR modifications are removed (Aleksic et al., 2010; Govern et al., 2010), effectively prolonging the half-life of the TCR-ligand interaction. However, the on-rate in our opto-ligand-TCR system seems to be too slow to significantly contribute to this effect (Appendix 2).

Our approach, including the designed PIFS mutant, could be a blueprint to study other ligand-receptor pairs and to understand how the kinetics of protein-protein interactions governs the activity of these binding events in diverse biological systems. Further, the opto-ligand-receptor approach is also well suited to locally induce signaling by focusing the light beam to the region of interest.

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
      <td>Genetic reagent (Aequorea victoria)</td>
      <td>moxGFP</td>
      <td>PMID: 26158227</td>
      <td></td>
      <td>Erik Snapp (Albert Einstein College of Medicine), Addgene plasmid # 68070</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>PIF6</td>
      <td>PMID: 29603429</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>HA1.7 TCRβ</td>
      <td>PMID: 17188005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>scFv</td>
      <td>PMID: 17188005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat</td>
      <td>PMID: 15057788</td>
      <td></td>
      <td>Arthur Weiss (HHMI, UCSF)</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat scFv-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing scFv-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat PIF(wt)-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing PIF(wt)-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat PIF(Q)-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing PIF(Q)-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat PIF(A)-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing PIF(A)-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat PIF(SS)-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing PIF(SS)-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat PIF(SSQ)-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing PIF(SSQ)-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat PIF(SSA)-TCRβ; Jurkat PIFS-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing PIF(SSA)-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat GFP-F1-PIFS-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing GFP-F1-PIFS-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat GFP-F2-PIFS-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing GFP-F2-PIFS-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Jurkat GFP-F3-PIFS-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing GFP-F3-PIFS-TCRβ</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>Jurkat GFP-noF-PIFS-TCRβ; Jurkat GFP-PIFS-TCRβ</td>
      <td>this paper</td>
      <td></td>
      <td>Jurkat expressing GFP-noF-PIFS-TCRβ</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Vβ3 Jovi3</td>
      <td>Ancell Cat# 102-020</td>
      <td>-</td>
      <td>5 µg/ml</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>biotin-conjugated anti-GFP</td>
      <td>Rockland Cat# 600-106-215</td>
      <td>RRID:AB_218204</td>
      <td>5 µg/ml</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>APC-conjugated anti-CD69</td>
      <td>Thermo Fisher Cat# MHCD6905</td>
      <td>RRID:AB_10372807</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>APC-conjugated anti-mouse</td>
      <td>SouthernBiotech Cat# 1031-11L</td>
      <td>-</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PhyB1-651-Aviag-His6; pMH17</td>
      <td>PMID: 27884151</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>p171</td>
      <td>PMID: 18832155</td>
      <td></td>
      <td>Lars-Oliver Essen (University Marburg)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PIF(wt)-TCRβ; pOSY015</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PIF(Q)-TCRβ; pOSY016</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PIF(A)-TCRβ; pOSY017</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>scFv-TCRβ; pOSY019</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PIF(SS)-TCRβ; pOSY026</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PIF(SSQ)-TCRβ; pOSY027</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PIF(SSA)-TCRβ; PIFS-TCRβ; pOSY028</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MBP-PIF(wt); pOSY061</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MBP-PIF(Q); pOSY062</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MBP-PIF(A); pOSY063</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MBP-PIF(SS); pOSY064</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MBP-PIF(SSQ); pOSY065</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MBP-PIF(SSA); pOSY066</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>GFP-F1-PIFS-TCRβ; pOSY073</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>GFP-F2-PIFS-TCRβ; pOSY074</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>GFP-F3-PIFS-TCRβ; pOSY075</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>GFP-noF-PIFS-TCRβ; GFP-PIFS-TCRβ; pOSY076</td>
      <td>this paper</td>
      <td></td>
      <td>see Table S1</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>PE-conjugated streptavidin</td>
      <td>Thermo Fisher Cat# S866</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>DyLight650-conjugated streptavidin</td>
      <td>Thermo Fisher Cat# 84547</td>
      <td>-</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Molecular cloning

All plasmids generated in this study were created using standard molecular cloning techniques like polymerase chain reaction, restriction enzyme digestion and ligation or Gibson assembly (Gibson et al., 2009). The plasmids are listed in Table S1 together with the corresponding coded protein, a brief description of the used components and the cloning strategy. The primers used as described in Supplementary file 1 are summarized in Supplementary file 2. Plasmid maps and nucleotide sequences in GeneBank format are available as supplementary information. Plasmid maps were generated with Geneious 6.1.8 (https://www.geneious.com). The integrity of each plasmid was verified by restriction enzyme digestion and Sanger sequencing. The plasmid containing moxGFP was a gift from Erik Snapp (Addgene plasmid # 68070) (Costantini et al., 2015).

### Protein production and purification

The production of PhyB1-651-Aviag-His6 was performed similarly as described before (Smith et al., 2016). Briefly, the PhyB-coding plasmid pMH17 was co-transformed into E. coli BL21(DE3) with plasmid p171 (Rohmer et al., 2008), which codes for the Synechocystis enzymes heme oxygenase and phycocyanobilin synthase, necessary for phycocyanobilin production. Co-transformed cells were selected with 100 μg/ml ampicillin and 40 μg/ml kanamycin. Bacterial cultures were grown at 30°C in lysogeny broth until OD600 reached 0.6, then expression was induced with 1 mM isopropyl β-D-1-thiogalactopyranoside (IPTG) and 0.4% (w/v) arabinose in the presence of 50 μM biotin. Protein production was sustained for 20 hr at 18°C in the dark. Following centrifugation of the bacteria for 8 min at 6500 g, the cells were resuspended in lysis buffer (50 mM HEPES, 500 mM NaCl, 5% glycerol, 0.5 mM TCEP, 20 mM imidazole, pH 7.4) and disrupted using a French Press (APV 2000, APV Manufacturing) at 1,000 bar. The lysate was cleared from debris by centrifuging twice at 30,000 g at 4°C for 30 min. The cleared lysate was loaded onto a Ni-NTA Superflow cartridge (Qiagen) using an Äkta Explorer chromatography system (GE Healthcare). After washing with 30 column volumes lysis buffer, purified PhyB1-651-Avitag-His6 was eluted with 10 column volumes elution buffer (50 mM HEPES, 500 mM NaCl, 5% glycerol, 0.5 mM TCEP, 500 mM imidazole, pH 7.4). The eluate fractions containing the purified proteins were pooled and the buffer was exchanged to PBS (phosphate-buffered saline, Sigma-Aldrich) containing 0.5 mM TCEP and 10% glycerol using a HiPrep 26/10 desalting column (GE Healthcare).

The expression and purification of the different MBP-PIF61-100 proteins was performed analogous to PhyB, with the difference that the plasmids pOSY061 until pOSY066 were transformed individually without p171, protein expression was induced using only IPTG and no biotin was added to the medium.

PhyB tetramers (PhyBt) were formed by mixing Ni-NTA column-purified PhyB1-651-Avitag-His6 in a 10:1 molar ratio with PE- or DyLight650-conjugated streptavidin (Thermo Fisher) and incubating the mixture for 2 hr at room temperature in the dark. The formed PhyB tetramers were separated from the excess of PhyB monomers by size-exclusion chromatography on a HiLoad Superdex 200 pg column (GE Healthcare) using PBS with 0.5 mM TCEP as running buffer.

### Analytical size-exclusion chromatography

To test the interaction of PhyB and MBP-PIF, PhyB was illuminated with saturating amounts of 660 or 740 nm light and MBP-PIF was added as depicted. Following incubation for 1 hr at room temperature in the dark, the samples were separated by size-exclusion chromatography on a Superdex 200 10/300 GL column (GE Healthcare) using PBS with 0.5 mM TCEP as running buffer.

### Cell line generation and cultivation

Jurkat E6.1 and derived cell lines were cultivated in RPMI 1640 medium supplemented with 10% fetal bovine serum (FBS), 2 mM L-glutamine, 10 mM HEPES, 100 U/ml penicillin and 100 µg/ml streptomycin (all Thermo Fisher) at 37°C in a humidified atmosphere of 5% CO2. HEK 293 T cells were cultured in DMEM (Thermo Fisher) supplemented as the RPMI medium at 37°C in a humidified atmosphere of 7.5% CO2.

For the generation of Jurkat-based cell lines stably expressing the chimeric TCRβ chains, we used lentiviral transduction as described earlier (Dopfer et al., 2014). Briefly, HEK 293 T cells were transfected with the lentiviral packaging plasmid pCMV dR8.74, the envelope plasmid pMD2 vsvG (both kind gifts from Didier Trono) and the respective transfer plasmid by calcium phosphate precipitation. 6 hr post-transfection the medium was replaced and lentiviral particles were produced by the HEK 293 T cells for 48 hr. Lentiviral particle-containing HEK 293T supernatant was harvested, filtered through a 0.45 µm syringe filter and concentrated by overnight centrifugation at 3,000 g at 4°C through a 20% (w/v in PBS) sucrose cushion. After discarding the supernatant, the viral particles were resuspended in medium using 1/100th of the harvested volume. Jurkat cells were transduced with different dilutions of concentrated lentiviral particles and 48 hr after transduction, surface expression and cell viability were analyzed by flow cytometry.

The identity of the Jurkat cells was confirmed by the binding to the antibody C305 that only binds to the TCR expressed on Jurkat cells (Weiss and Stobo, 1984). The identity of the HEK 293 T cells was not confirmed. All cells were routinely tested for mycoplasma and devoid of contamination.

### Cell surface staining for flow cytometry

Cells were stained for surface proteins according to standard protocols. Briefly, cells were washed once with washing buffer (PBS supplemented with 1% FBS), then incubated for 30 min at 4°C in a diluted solution of the labeling antibody as depicted in the key resources table. Finally, the cells were washed twice as before and analyzed on a MACSQuant X flow cytometer (Miltenyi). The labeling reagents used in this study were anti-Vβ3 Jovi3 (Ancell), biotin-conjugated anti-GFP (Rockland Immunochemicals), APC-conjugated anti-CD69 (Thermo Fisher), APC-conjugated anti-mouse (Thermo Fisher) and PE-conjugated streptavidin (Thermo Fisher).

### Light-dependent PhyBt binding to the cell surface

Binding of PhyBt to the different cells lines was performed analogous to the cell surface staining with antibodies, but instead of labeled antibodies 100 nM pre-illuminated Phycoerythrin (PE)-labeled PhyBt(660) or PhyBt(740) were added to the cells and incubated for 30 min at 4°C in the dark. Subsequent washing steps and the measurement at the flow cytometer were executed under green light.

To evaluate the amount of surface bound PhyBt under constant illumination with varying intensities of 660 nm light, different concentrations of PhyBt(660) were added to GFP-PIFS-TCR cells under illumination conditions as depicted and incubated for 90 s at 37°C. Subsequently, the cells were transferred to a ten-fold excess of ice-cold washing buffer, immediately centrifuged for 10 s under green light and the supernatant aspirated. After a second washing step, surface-bound PhyBt was quantified by flow cytometry. Unspecific binding was accounted for and subtracted from each sample by adding ten-fold diluted amounts of PhyBt(660) to control samples that were treated with washing buffer during the 90 s incubation step.

### Calcium influx measurement

Five million cells were centrifuged for 5 min at 300 g and the medium was discarded. The cell pellet was resuspended in 1 ml stimulation medium (RPMI 1640 medium supplemented with 1% FBS, 2 mM L-glutamine, 10 mM HEPES, 100 U/ml penicillin and 100 µg/ml streptomycin) with 0.1% (v/v) pluronic F-127 and 4 µM Indo-1 AM (all Thermo Fisher) and incubated in the dark for 30 min at 37°C. The stained cells were washed and kept on ice in the dark until the measurement. For calcium influx, cells were diluted 1:20 with pre-warmed stimulation medium and maintained at 37°C during the event collection on a MACSQuant X flow cytometer. After fluorescence baseline acquisition, stimuli were added or activated by illumination as depicted. If not indicated otherwise PhyBt were added to a final concentration of 20 nM.

For the graphs showing the percent of responding cells, the events above the 90th percentile during baseline acquisition were quantified using FlowJo 9 (FlowJo LLC). To calculate the calcium influx values (a.u.), average Indo-1 ratio values after stimuli addition (250–400 s) minus baseline values (30–60 s) were normalized for each experiment using an internal control of 20 nM PhyBt(660) in the dark.

### CD69 upregulation

200,000 Jurkat or GFP-PIFS-TCR cells were seeded per well in a 96-well flat-bottom plate in 100 µl stimulation medium and incubated for 1 hr in the cultivating incubator. Meanwhile, streptavidin sepharose beads (GE Healthcare) were washed with PBS and then incubated with 5 µg purified PhyB per µl beads (diluted in PBS) at 37°C for 30 min. The beads were washed twice with PBS and resuspended in stimulation medium at 2 µl beads per 100 µl medium. The diluted beads were illuminated as described, 100 µl bead suspension added per well to the cells and the cells stimulated for 6 hr in the incubator. Following the incubation, surface expression of CD69 was analyzed by flow cytometry as described above.

### Determination of PhyB conversion rates

50 µg purified PhyB(660) or PhyB(740) was mixed with a 6-fold excess of MBP-PIF(wt) or an equal volume of buffer (PBS with 0.5 mM TCEP) and incubated for 60 min at room temperature. Each protein mixture was transferred to a quartz cuvette, a blank measurement was taken and under constant illumination with 70 µmol m−2 s−1 660 or 740 nm light difference absorbance spectra were acquired every 10 s using a HR4000 spectrometer in combination with a DT-Mini-2-GS light source (Ocean Optics). We quantified the conformational change of PhyB by subtracting the minimum absorbance value from the maximum value and plotted this ΔΔA value against the time of illumination (not shown). From the resulting curves, we calculated the photoconversion rates by first order association kinetics nonlinear regression using the software Prism 6 (GraphPad Software). Differences in the conversion rates with or without MBP-PIF were tested by two-way ANOVA using Prism 6.

### Illumination devices

For the different experiments performed in this study, we used two types of illumination devices. One device was built as a closed box with an array of red (Osram, LH W5AM, Mouser Electronics) and far-red (LZ4-00R308, LED Engin) light-emitting diodes (LEDs) at the top, resulting in a planar light source. Ventilated openings in the box in combination with light traps allowed gas exchange for the use of the device in an incubator. This illumination box was used for all pre-illumination steps, the CD69 upregulation experiments and PhyB conversion rate measurements.

The second device was built together with Opto Biolabs as a cylinder enclosing a reaction tube in the center. Surrounding the reaction tube, is a water-filled space, which is connected to a 37°C water bath to keep a physiological temperature. Further outside we placed rings of red (Super Bright Red, Kingbright Electronic Europe) and far-red (LED740 series, Roithner Lasertechnik) LEDs, pointing towards the reaction tube. An opaque outmost cylinder shields the sample from external light. The cylindrical illumination device was used for all calcium experiments and experiments under constant 660 nm illumination in combination with a MACSQuant X flow cytometer.

### Repetition of experiments and data presentation

In this study, all graphs derived from data of multiple experiments depict individual data points for less than three replicates and average values for three or more replicates. The uncertainties of these experiments are shown by the standard error of the mean (SEM). For graphs displaying representative experiments, ‘n’ in the legend defines the number of independent experiments that the depicted results were done.
