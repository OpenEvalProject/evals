# Author response - Round 1

Authors:
- Vladimir Chubanov ([ORCID: 0000-0002-6042-4193](https://orcid.org/0000-0002-6042-4193))
- Silvia Ferioli
- Annika Wisnowsky
- David G Simmons ([ORCID: 0000-0002-4115-9371](https://orcid.org/0000-0002-4115-9371))
- Christin Leitzinger
- Claudia Einer
- Wenke Jonas
- Yuriy Shymkiv
- Harald Bartsch
- Attila Braun
- Banu Akdogan
- Lorenz Mittermeier
- Ludmila Sytik
- Friedrich Torben
- Vindi Jurinovic
- Emiel PC van der Vorst
- Christian Weber
- Önder A Yildirim
- Karl Sotlar
- Annette Schürmann
- Susanna Zierler ([ORCID: 0000-0002-4684-0385](https://orcid.org/0000-0002-4684-0385))
- Hans Zischka
- Alexey G Ryazanov
- Thomas Gudermann

## Response text

DOI: [10.7554/eLife.20914.030](https://doi.org/10.7554/eLife.20914.030)

Essential revisions:

1) The authors suggest that Mg2+ deprivation in TRPM6-deficient mice impairs ATP levels by preventing the use of acylcarnitine as a substrate. The link between Mg2+, AC metabolism and ATP is only shown for isolated mitochondria and nonphysiological concentrations of [Mg2+]. A simple measurement of ATP or mitochondrial potential (using fluorescent dyes) in intact cells from WT vs. KO mice would provide direct support to strengthen this conclusion.

Thank you for this important point. The studies with isolated liver mitochondria were conducted because our metabolic profiling experiments suggested that mitochondrial metabolism of acylcarnitines was affected by sustained Mg2+ deficiency in Trpm6-deficient adult mice. Since freshly isolated mitochondria are metabolically active for a very short time only (a few hours), we had to acutely deplete Mg2+ in the mitochondrial matrix using buffers with low Mg2+ concentrations.

When attempting to recapitulate the phenotype of living Trpm6-deficient mice at the cellular levels, several critical issues need to be considered: First, according to our model Trpm6-mediated Mg2+ uptake is not required for cell autonomous functions, implying that Trpm6-deficient cells (like TS cells, Figure 6 and Figure 6—figure supplement 1) will not develop Mg2+ deficiency and abnormal energy metabolism, because TRPM7 is still functional. Second, Trpm6 is not expressed in tissues, which critically rely on mitochondrial energy production, such as skeletal muscle or liver. Furthermore, during the isolation process of primary cells it is virtually impossible to “clamp” intracellular Mg2+ concentrations at exactly the same levels normally occurring in vivo in Trpm6-deficient mice. Accordingly, in vitro experiments with liver or skeletal muscle cells isolated from Trpm6-deficient mice would not truly reflect in vivo conditions of Trpm6-deficient mice, such as prolonged (several weeks) organismal Mg2+ deficiency.

Considering these limitations, we resorted to an alternative experimental model that allowed us to investigate whether Mg2+ deficiency in isolated cells affects mitochondrial function. We found that CRISPR/Cas9-mediated inactivation of TRPM7 in the genetically tractable HAP1 cell line (human haploid leukaemia cells) results in Mg2+ deficiency and, consequently, a Mg2+-dependent proliferation defect (new Figure 6—figure supplement 3). Remarkably, we observed that TRPM7-deficient HAP1 cells display reduced ATP levels at resting conditions. Finally, we show that the respiration rate of TRPM7-deficient HAP1 cells was markedly supressed when compared to control cells (new Figure 6—figure supplement 3). Taken together, we conclude that Mg2+ deficiency of HAP1 cells recapitulates our key findings in Trpm6-deficient mice. These new findings are now shown in Figure 6—figure supplement 3.

2) The authors propose that TRPM6 regulates Mg2+ transport by reducing the MgATP-dependent inhibition of heteromeric TRPM6/7 channels. First, the evidence for this rests on whether the inhibition curves in Figure 6B and C are significantly different between WT and KO animals; this should be evaluated. In addition, it is not clear that MgATP in intact cells is in the required range that would differentially affect the current in the WT vs. TRPM6 groups (Figure 6B); either the ATP level should be measured, or a suitable reference provided. Finally, another group (Zhang, Yu et al., 2014) reported that TRPM6 expression by itself produced currents, and TRPM6 and M7 coexpression generated currents that were essentially insensitive to MgATP inhibition. This should be discussed in the context of the results shown in Figure 6, where TRPM7 KO completely eliminated current, and wild type and TRPM6 currents are both inhibited by MgATP.

We agree with the referees and introduced several changes in the manuscript to address their concerns. We re-analyzed the inhibition curves for Mg2+ and MgATP using a nonlinear (least-squares) regression fitting and F-test (GraphPad Prism 6.0 software) to address the questions: (i) Is the dose-response dataset of KO cells is statistically different from that in control cells? And (ii) are IC50 values distinct for the inhibitory curves obtained for KO and control cells? This analysis supported our initial conclusion that Mg2+ elicits similar inhibitory effects on the currents in WT and KO cells, whereas the inhibitory dose-response curves for MgATP were statistically different between KO and control cells. This information is now included in the Results (subsection “TRPM6 cooperates with TRPM7 to regulate divalent cation currents”) and Methods (subsection “Isolation and characterization of mouse trophoblast stem (TS) cells”) sections.

As suggested, we referenced the physiological levels of cytosolic MgATP (subsection “TRPM6 cooperates with TRPM7 to regulate divalent cation currents”) to support the notion that intracellular MgATP can differentially affect ion currents in control and KO cells. In addition, we discuss the work of Zhang et al. (Discussion, fifth paragraph) reporting the functional analysis of recombinant TRPM6 and TRPM7 co-transfected at the ratio 1:1 in HEK 293 cells. A key finding of this study was that recombinant TRPM6 offset the sensitivity of the TRPM7/M6 complex to cytosolic MgATP. Assuming that native currents in WT cells are mediated by TRPM7 homomers and TRPM6/M7 heterotetramers, it is imaginable that genetic ablation of the TRPM6/M7 fraction would only partially reduce the inhibitory effect of MgATP on whole-cell currents. Hence, we conclude that the observations of Zhang et al. are compatible with our results. Another finding from Zhang et al. is that overexpression of TRPM6 homomers in HEK 293 cells results in expression of a functional channel only if TRPM6 cDNA was expressed by the pCINeo-IRES-GFP vector, whereas the same cDNA sequence placed in various other expression plasmids did not produce active TRPM6 channels. This feature of TRPM6 cDNA appears to be unique among TRP channels, and as the nature of this observation is not currently understood, some caution is required in interpreting the results. Therefore, we have concentrated on the functional analysis of endogenous TRPM6 channels in primary cells for defining the cellular role of TRPM6 rather than on overexpression data.

Finally, we would like to emphasize that according to our model, TRPM6 regulates Mg2+ uptake by two means: (i) by increasing amplitudes of TRPM7-like currents and (ii) by relieving TRPM7 from the negative feedback by MgATP. To better illustrate the first mechanism, we now include a new Figure 6B, showing measurements of native currents in the absence of external divalent cations. This approach is widely used for a quantitative assessment of otherwise very small inward currents of TRPM7/M6, since external divalent cations elicit a strong permeation block of the channel at physiological membrane potentials. As expected, these experiments showed that current amplitudes recorded in KO cells were substantially lower than in control cells.
