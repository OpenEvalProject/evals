# Peer review - Round 1

Editors:
- Lilianna Solnica-Krezel, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54894.sa1](https://doi.org/10.7554/eLife.54894.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In developing embryos cells make fate decisions using morphogens, diffusible signaling molecules that induce concentration-dependent responses in target cells. The manuscript by Lord et al., addresses the question of how the Nodal morphogen gradient forms in developing zebrafish embryo. This work offers two main findings: first, diffusion is sufficient for the Nodal gradient formation without a relay of Nodal production; second, the co-receptor Oep shapes the Nodal gradient and restricts its range by ligand capture.

Decision letter after peer review:

Thank you for sending your article entitled "The pattern of Nodal morphogen signaling is shaped by co-receptor expression" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Naama Barkai as the Senior Editor.

Given the number of questions and concerns raised by the three reviewers about the data, their interpretation and conclusions drawn, the manuscript requires significant amount of experimental work before it can be accepted at eLife. The reviewers expressed skepticism whether the authors could address them within two months under normal circumstances. Below I summarize the key questions and concerns expressed by the reviewers and the experiments considered by the reviewers as essential. I also include the complete reviews for your perusal.

1. There was a consensus that the proposed model that Nodal signaling activity is not determined by signaling feedback but rather is set by the EGF-CFC co-receptor Oep, to be novel and significant. However, they also thought these main conclusions are quite speculative at this point. A main issue is that the distribution of Nodal ligands in the various experimental conditions is indirectly inferred from the levels of downstream pSmad2 signaling. Specifically, direct observation of the ligands in different oep homozygous and heterozygous mutant and overexpression backgrounds can help to resolve some of the key issues raised by all reviewers. This would rule out that the effects are due to changed balance in positive and negative feedback in signaling rather than ligand distributions. The Schier lab has visualized these ligands in the past (Müller et al., 2012) and could address this issue directly by comparing ligand distributions in WT and MZoep mutants, as well as in oep overexpression condition.

2. The genetic background used for the sensor cells (Mvg1) is a major concern for the analysis and interpretation of these experiments. Although, Vg1 can form heterodimers with both Nodal ligands and is required for their endogenous activity, residual Nodal signaling still persists in MZvg1 mutant embryos (Pellicia et al., eLife. 2017). Accordingly, injection of relatively low doses of squint mRNA (10pg) in MZvg1 mutant embryos is sufficient to induce Goosecoid expression (Montague et al., eLife. 2017; Pellicia et al., eLife. 2017). Therefore, the "sensor" cell assay should be repeated using sqt;cyc double mutant cells to ensure all positive feedback signaling is absent.

3. Moreover, it will be crucial to demonstrate the requirement for ligand-induced acceleration of endocytosis (this is beyond normal endocytosis model that rely on constitutive endocytosis).

4. In addition, there are several simulation questions, which need addressing (please also see the individual reviews below).

a. The rate for λ n is not provided.

b. In supplemental material for the model description: The model requires a very high endocytosis rate for the traveling wave to work.- on the order of 1.7*10-3/sec (supplement table). This is 10-20 times faster than estimates for BMP receptors and endocytosis (Pomreinke et al. 2017), however not measured here. This leads to a half-life of 6.8 minutes. That is much faster than other turnover studies from Ed Leof's data for TGF-β endocytosis in a number of cell culture studies inconsistent with modeling studies in TGF-β.

5. The transplanted cells do not seem to remain highly cohesive and rather spread within the blastoderm (Figures 1, 2 and 3). This is an important issue, as a given sensor cell might end up positioned away from the margin, but have initially been located close to the YSL and therefore received a very high dose of Nodal ligands, independently of long-range ligand diffusion. Thus, the authors should analyze sensor cell dispersion post-transplantation and their p-Smad2 signaling status in a more dynamic manner.

6. To support the rationale of Oep loss and traveling wave, the level of maternal RNA over time should be analyzed by RT PCR to quantify maternal RNA loss to see if consistent with timing of wave or cite where this data is available.

7. The authors claim that the p-Smad2 gradient is expanded in MZoep host embryos. However, there are hardly any cells quantified for the control transplants at more than 100µms distance from the margin. The authors should address this issue.

8. Both the number of transplanted sensor cells and their distance to the YSL is highly variable across experimental conditions (compare Figures 1, 2 and 3). This renders the interpretation of the results difficult. Therefore, the authors should perform a detailed analysis of the p-Smad2 behavior as a function of the number of transplanted sensor cells and their distance to the YSL. Perhaps, by binning their data in sub-classes and plotting the variability in p-Smad2 staining across the transplanted cell cluster.

9. Related to that, in the simulations in Figure 4 the size of the clones is very small compared to the experimental data and one cannot get an impression of any position-dependent differences in signaling activity. The level of signaling as a function of position differs in the different experimental conditions – the simulations should allow assessing whether the model adequately captures these changes.

10. A central claim in this manuscript is that the Oep co-receptor critically modulates the diffusion range of the Nodal ligands. The Oep overexpression experiments in Figure 3 show opposite phenotypes. In Figure 3B there is a very large oep overexpressing clone which touches the margin and shows pSmad signaling several cell diameters away from the margin. In Figure 3D a sensor clone in oep overexpressing background shows almost no signal at a comparable distance to the margin. How do the authors reconcile this?

11. The authors state (lines 165-167) that "Loss of Oep led to an expanded range of action of both Cyclops and Squint" based on the "sensor" experiment performed in MZoep;sqt and MZoep;cyc double mutant. However, this conclusion is supported by single images from these double mutants without any quantification. To make this conclusion, such experiments need to be quantified as illustrated in Figure 1B. This is important, as this result would imply that it is Oep that discriminates between Cyc and Sqt ligands and their distinct signaling range, demonstrated by earlier work from the Schier lab and also in this manuscript.

Reviewer #1:

1. To address the key question of how the Nodal signaling gradient is formed in zebrafish embryos and the relative contributions of Nodal ligand diffusion and feedback signaling for this process, the authors established a transplantation-based "sensor" cell assay. However, the genetic background used for the sensor cells (Mvg1) is a major concern for the analysis and interpretation of these experiments. Although, Vg1 can form heterodimers with both Nodal ligands and is required for their endogenous activity, residual Nodal signaling still persists in MZvg1 mutant embryos (Pellicia et al., eLife. 2017). Accordingly, injection of relatively low doses of squint mRNA (10pg) in MZvg1 mutant embryos is sufficient to induce Goosecoid expression (Montague et al., eLife. 2017; Pellicia et al., eLife. 2017). Therefore, the "sensor" cell assay should be repeated using sqt;cyc double mutant cells to ensure all positive feedback signaling is abolished.

2. The transplanted cells do not seem to remain highly cohesive and rather spread within the blastoderm (Figures 1, 2 and 3). This is an important issue, as a given sensor cell might end up positioned away from the margin, but have initially been located close to the YSL and therefore received a very high dose of Nodal ligands, independently of long-range ligand diffusion. Thus, the authors should analyze sensor cell dispersion post-transplantation and their p-Smad2 signaling status in a more dynamic manner.

3. Both the number of transplanted sensor cells and their distance to the YSL is highly variable across experimental conditions (compare Figures 1, 2 and 3). This renders the interpretation of the results difficult. Therefore, the authors should perform a detailed analysis of the p-Smad2 behavior as a function of the number of transplanted sensor cells and their distance to the YSL. Perhaps, by binning their data in sub-classes and plotting the variability in p-Smad2 staining across the transplanted cell cluster.

4. A central claim in this manuscript is that the Oep co-receptor critically modulates the diffusion range of the Nodal ligands. In Figures 3c and d, the authors claim that modulating Oep levels in MZsmad2 hosts dramatically reduces the range of p-Smad2 activation in sensor cells. While this seems to be the case when comparing the data in Figures 3c and d, this is not the case when looking at the example for the same control experiment in Figure 1c (Mvg1 → MZsmad2). Why would this be the case?

5. The authors claim that "by facilitating capture of Nodal ligands, Oep regulates range and intensity of the Nodal activity gradient". Although the author's theoretical model is consistent with this interpretation, this remains to be experimentally tested. For this, the authors could analyze the intra- versus extracellular distribution of Nodal ligands ligands in homo- and heterozygous oep mutant embryos, in Zoep mutants and upon oep overexpression in a wt background.

6. Additionally, the authors should experimentally measure the diffusion dynamics of both Nodal ligands in homo- and heterozygous oep mutant embryos, in Zoep mutants and upon oep overexpression in a wt background. Furthermore, it would be interesting to perform similar measurements for Lefty 1 and 2, given the authors suggestion that binding to Oep results in different diffusion ranges for Nodals and Leftys.

7. The dynamics of Oep decay in zygotic oep mutants should be studied in this study.

8. Is the function of Oep in controlling the Nodal signaling range specific? Or would modulating Activin receptor expression produce similar phenotypes?

9. It is unclear why the transplantation assays are reproduced using different parameters from those used to simulate the Nodal signaling gradient in Figure 5. Can the authors comment on why this is? It would be preferable to use similar parameters to reproduce both the transplantation assays and the in vivo gradients.

10. It would be interesting to test whether Lefty overexpression in the MZoep background is sufficient to reduce the Nodal signaling range in sensor cells.

Reviewer #2:

In the paper by Lord et al., the authors address two important questions regarding the formation of the Nodal gradient (Cyclops and Squint) from the YSL 6-8 cells into the margin- a pathway that is also regulated by Nodal inhibitors lefty1/2. First, the authors address a recent hypothesis that the nodal signaling gradient is formed by a sequence of positive feedback expression events in a relay that initiates in YSL and that diffusion or transport is not the mechanism of gradient formation. In the process of addressing this, they identify the role for the co-receptor Oep that "sets cell sensitivity" to Nodal. Overall, addressing the feedback question in MZsmad2 embryo hosts with clones of nodal sensitive cells establishes gradient formation in the absence of feedback- this is quite a challenging but convincing experiment to determine the range of Nodal without feedback.

In regards to MZoep mutants, the behavior of MZoep is consistent with co-receptor activity- increasing sensitivity by presumably increasing the formation of receptor competent receptor complexes, while simultaneously impacting gradient spread due to additional ligand capture. Basically- increase the frequency of ligand capture shapes the gradient by reducing the length scale, related to the dimensionless Thiele modulus (ratio of the reaction rate to diffusion rate). The behavior of systems without feedback in the presence of a co-receptor are very well developed and known, so it is unclear what new information is provided by the simulations in figure 4 that behaves similarly to other systems with receptors, binders, and ligand capture. In the model and supplemental materials for the model, the first test assumes "pseudo first-order kinetics"- making the gradient formation a linear ODE at steady-state and it is shown that 4A-it forms a gradient; in 4B- when there's no decay by setting receptor levels to zero, the gradient expands- increasing the rate of decay by receptors reduces the range. Thus 4A-4D really prove things that are widely known in general and have been shown analytically and numerically in many papers. Some papers that have carried out similar but more developed analysis on trapping and/or endocytosis with and without diffusion include the following: (Lander, Nie and Wan, 2002; Lander, 2007) (Coppey et al., 2007; Coppey et al., 2008) (Eldar et al., 2003) (Lander et al., 2020) (Umulis et al., 2006) (Hornung, Berkowitz and Barkai, 2005) some more effort looking at previous co-receptor simulations or mathematical studies that relate binders to gradients should be considered.

Next, in figure 5C, the experiment suggests development of a traveling wave due to receptor depletion. This only occurs in the simulation when there is a "ligand-induced" increase in endocytosis. The preponderance of evidence in cell culture and for other TGF-β ligand-receptor systems, supports an alternative hypothesis- that receptors are constitutively turned over at a constant rate dependent on the turn-over of the membrane via clathrin-mediated endocytosis. The evidence for a positive feedback on the rate of receptor endocytosis in this system that is essential to the underlying hypothesis is not provided. The system that doesn't have ligand-induced endocytosis will not lead to a traveling wave.

The hypothesis for the wave here in the simulation relies on too many unsubstantiated requirements- and is therefore speculative. It requires rapid and ligand-induced endocytosis, loss of receptors and no resupply by maternal transcript (PCR not shown) and operating far from saturation- or it would be a flat signal.

To support the hypothesis, experiments could be attempted to:

1. Determine how close to saturation the receptors are via determining maximum signaling achievable in overexpressed sqt. If it is near saturation, then excess nodal will lead to no increases in PSmad2.

2. Determine the level of maternal RNA over time by RT PCR to quantify maternal RNA loss to see if consistent with timing of wave or cite where this data is available.

3. Block or use endocytosis deficient clones to better determine the validity of the critical ligand-induced endocytosis hypothesis.

4. Identify whether Oep is part of the receptor complex or if it dissociates before signaling- the model is predicated on the co-receptor functioning as the receptor. It is hard to envision a system where to co-receptor is part of the complex for TGF-β and signaling, and then if it is not a part of the complex, then how is ligand-induced rapid endocytosis of the Oep achieved?

In addition there are many simulation questions:

– the rate for λ n is not provided,

In supplemental material for the model description: The model requires a very high endocytosis rate for the traveling wave to work.- on the order of 1.7*10-3/sec (supplement table). This is 10-20 times faster than estimates for BMP receptors and endocytosis (Pomreinke et al., 2017), however not measured here. This leads to a half-life of 6.8 minutes. That is much faster than other turnover studies from Ed Leof's data for TGF-β endocytosis in a number of cell culture studies inconsistent with modeling studies in TGF-β.

The units for parameter k1 are not correct in the parameter table- the nodal-receptor association rate. Perhaps, they should be (uM sec)-1. Otherwise the units in the differential equations are not consistent. Also the reference is for BMPRII binding rate. The dissociation constant (assuming the rate parameter units is a typo) is then 6.25 X 10-5 μm or 6.25*10-2 nM. This is quite high and would saturate receptors at 0.12 nM. Here are some constants from Aykul et al.

Ligand Interacting ka(s-1M-1s-1) kd(s-1) Kd(nM)

Nodal ACTRIIA 2.0×104 2.0×10-3 100

ACTRIIB ~4.9×104 (est) ~4.9×10-4 (est) ~10 (est)

BMPRII 3.1×105 4.6×10-5 0.149

ALK4 ~4.6×104 (est) ~3.2×10-4 (est) ~15 (est)

ALK7 No Binding

Cripto-1 1.0×104 2.6×10-4 16

Cryptic 5.5×102 1.0×10-3 2,000 †

Reviewer #3:

The manuscript by Lord et al., addresses the question of how the Nodal morphogen gradient forms during zebrafish development. This work makes two main points: (1) the Nodal gradient can be established by diffusion alone without a relay of Nodal production; (2) the co-receptor Oep shapes the Nodal gradient and restricts its range by ligand capture. While the presented observations are novel, relevant and important for understanding the mechanism of gradient formation in this system, the conclusions and interpretation require further support. In particular:

1. A main issue is that the distribution of Nodal ligands in the various experimental conditions is indirectly inferred from the levels of downstream pSmad2 signaling. The conclusions are strongly worded, implying proportionality between Nodal ligand levels and pSmad2 levels, eg. in MZSmad2 (line 146-147) and MZoep embryos (line 174-175). However, the pSmad2 levels in this system are dependent not only on the level of activators (Sqt, Cyc), but also on the level of negative regulators such as lefty1 and 2. Although lef1, lef2 are key negative regulators, they might not be the only Nodal-dependent negative feedback on pSmad2. Thus, it is difficult to rule out the possibility that the effects that the authors are seeing on pSmad2 range in the MZSmad2 and MZoep embryos are due to modified negative feedback, rather than distribution of Sqt and Cyc. The Schier lab has visualized these ligands in the past (Müller et al., 2012) and could address this issue directly by comparing ligand distributions in WT and MZoep mutants, as well as in oep overexpression condition.

2. The Oep overexpression experiments in Figure 3 show opposite phenotypes. In Figure 3B there is a very large oep overexpressing clone which touches the margin and shows pSmad signaling several cell diameters away from the margin. In Figure 3D a sensor clone in oep overexpressing background shows almost no signal at a comparable distance to the margin. How do the authors reconcile this?

3. In the simulations in Figure 4 the size of the clones is very small compared to the experimental data and one cannot get an impression of any position-dependent differences in signaling activity. The level of signaling as a function of position differs in the different experimental conditions – the simulations should allow assessing whether the model adequately captures these changes.

4. To draw their conclusions, the authors make certain assumptions about cell rearrangements in this tissue (or the lack thereof). These assumptions are not stated or justified. This needs to be done both for interpreting the results in MZSmad2 and MZoep embryos, but also in the traveling wave experiments in Figure 5 where they look at a later stage (Schield).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The pattern of Nodal morphogen signaling is shaped by co-receptor expression" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and a Reviewing Editor.

The manuscript has been improved and the reviewers were satisfied with the revisions. However, the reviewers requested that your response to point 5 (regarding cell rearrangements) should be incorporated into the main text of the manuscript. This is important, so that readers are aware of the assumptions that are made in interpreting the experimental data and know what these assumptions are based on. Not all readers will be familiar with the zebrafish system and this information will make the study more accessible to a wider audience.
