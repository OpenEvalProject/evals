# Peer review - Round 1

Editors:
- Alphee Michelot, Institut de Biologie du Développement France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63046.sa1](https://doi.org/10.7554/eLife.63046.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work shows the molecular complexity involved in the assembly of actin networks, and this in-depth characterization will be important for the field. The FRAP data showing faster recovery of actin networks after regulator disruption is interesting. It questions how this excessive monomeric actin reservoir is maintained and consumed under these conditions, and what it represents in terms of size control for these actin networks. Future modeling would be greatly beneficial to understand how actin fluxes are controlled in this system.

Decision letter after peer review:

Thank you for submitting your article "Combinatorial deployment of F-actin regulators to build complex 3D actin structures in vivo" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Alphee Michelot as the Reviewing Editor, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Anne Cecile Reymann (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Xie and Blankenship present here a characterization of the apical actin architectures during the syncytial cell cycles of the fly early embryo. These actin architectures undergo a series of rapid and transient reorganization correlated with cell cycle. The authors examine the functions of one formin (diaphanous), of the Arp2/3 complex, and of 7 other proteins (called here ANRPs) involved in the activation of the Arp2/3 complex and/or in various other actin regulation activities. Their results reveal a clear complexity, as these proteins display different effects on actin caps dynamics and in anchoring embryonic nuclei.

This work also includes information of ANRPs localization at actin caps, and their relative role in recruiting the Arp2/3 complex. Among those observations, the authors find a clear antagonism between cortactin and coronin, which was shown in previous studies but is nicely confirmed here.

In the last part of this work, which is more debatable, the authors performed FRAP experiments on actin caps, and find surprisingly that recovery of actin signals are faster in mutant conditions than in WT. These results, together with the fact that treatment with LatB or Jasp increases on the contrary characteristic times of recovery, suggest to the authors that the pool of monomeric actin might be increased in mutant conditions, potentially revealing a competition between actin networks for a limited pool of monomeric actin.

Overall, the Reviewers agree that tools and results presented here will be valuable for the community. The experimental procedures are adapted and well performed, and revisions should require limited experimental work. However, the Reviewers regret some lack of explanation on the quantification and statistical analysis of the experiments, notably regarding the lack of detailed explanation on the procedures (segmentation procedure, measure of intensity, calculation of errors, FRAP analysis, colocalization etc).

Essential revisions:

1. Quantification of the data:

Could the authors use a more automatized or robust method, such as via an autocorrelation function, to measure the size of the caps without the bias of using a threshold or a manual segmentation? Could they also provide videos for each conditions as Supplementary data?

How initial time points of cap formation are determined is not clear. Segmentation or thresholding methods to obtain area and intensities are not clearly described. Measured Area is often shown as normalized over the initial area, but this initial time point seems prone to fluctuations or errors of segmentation.

Regarding actin intensity: is it a total intensity or a mean density which is important as the area is indeed changing? Important to know if we are considering total actin filaments change or local density changes. Making this distinction would also be interesting while discussing shRNA results. There is also no mention on the impact of bleaching even though 5s interval of 4D acquisitions are performed over several minutes.

From this quantification and the definition of clear parameters, it should also appear clearly why the authors report that cap dynamics share similar features in cycle 10-13. From an observer's eye, it seems on the contrary that some of these phases are absent from certain cycles. Also, Figure 2C, 3B,E,G,I,K and M are not clear, because each phases are defined based on WT conditions only. It would be important to report how phase durations are modified in shRNAs lines.

Finally, some results from this quantification are curious. For example, between time 0 and 60s in WT, cap intensity only increases moderately (Figure 1G), while cap area increases a lot (Figure 1D). This suggests that actin density should decrease a lot, which seems opposite to what is observed in Figure 1A.

2. Statistical analysis:

In Figures 5 and S7 the number of caps analyzed seems fairly small (n=3 or 4 in some cases) for FRAP experiments. The authors should increase their sample size and show the degree of variability in the FRAP parameters that they measured using box plots and standard deviations (rather than standard error).

The authors should also clarify what the variation observed for cells within a single embryo is vs. the variation for all embryos considered in this study.

3. The authors should report the efficiency of silencing in the shRNA experiments. This would enable readers to evaluate if residual activity of these proteins is expected or not. When some shRNA as Carmil, Wasp or Wash have little impact on cap dynamics, could it be just a question of efficiency of silencing? In the absence of such measurements, we would be more careful with the conclusions of these experiments. In some other systems too, wasp or wave silencing has little effect on cortical dynamics, to compensate gex-3 can be depleted and is more efficient. Did the author consider this option?

4. Based on the hollowed appearance of actin caps in Arp2/3 shRNA embryos, the authors propose that Arp2/3 may promote central actin assembly that then flows outwards. This seems easy enough to test, for example by photobleaching a region in the center of the cap and examining whether that photobleached region propagates outwards. The authors should conduct the same experiment upon Cortactin shRNA or Scar shRNA treatment, which seem to impede actin flow outwards (Figure 3H-I).

5. Regarding FRAP, the authors decided to use MOE:GFP as a proxy for actin dynamics. This rational is not well explained (line 266) and should be more justified.

For example, line 114: "This method of labeling has been used extensively in the Drosophila embryo, and well-represents endogenous filamentous actin dynamics while avoiding problems that occur when fluorescent proteins are directly attached to actin or other labeling paradigms". One could always argue that any fluorescent peptide binding to actin potentially impacts actin dynamics in some ways. What would be important for this study is to justify why this specific marker does not interfere for the specific observations made here. Additionally, it would be important to note that FRAP recovery times are equivalent to GFP:Act88F, indicating that recovery times represent rates of actin turnover rather than dynamics of MoeABD binding/unbinding.

Note that in figure S2 one could show the recovery curves in addition to the extracted value to justify the similarity of the process. Comparison with other published data is not mentioned. For example, injected rhodamine actin followed during cycle 12 (2010 Cao et al. Current Biology) values are t1/2 = 18.9{plus minus}1.7 s and 87.3% of recovery (so 13% immobile). So more than twice the t1/2 value presented here (8.2s). The quantification is also not well documented. What intensity is used? Is it normalized to pre-bleach as well as to the value post bleach? Is there any curve fitting to exponential functions to extract the parameters? The authors could try to use some simple models of actin polymerization to estimate rates of assembly and disassembly from the FRAP data and try to get at which one is changing when Dia or Arp2/3 are lost (e.g. Kobb et al., MBoC, 2019). The authors should also discuss the choice of FRAP timing (performed at max Area 120s) so at a critical point in terms of assembly and reorganization of caps architectures.

Also, FRAP recovery images are provided only for WT condition, but not for shRNA embryos. The authors should provide these images in the Supplementary data.

6. There is an over simplification in this work, in considering that formin (diaphanous) and Arp2/3 networks assemble fully independently. There is clear evidence now, for example in lamellipodia, that formins and Arp2/3 can be synergistic, and it is not demonstrated that dia and Arp2/3 networks assemble independently here. The authors should take into account this possibility when discussing their results, and modify Figure 5G.
