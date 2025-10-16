# Peer review - Round 1

Editors:
- Xiaojun Tian, https://ror.org/03efmqc40 Arizona State University, School of Biological and Health Systems Engineering United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74540.sa0](https://doi.org/10.7554/eLife.74540.sa0)

This paper used multiple strains to build gene circuits and demonstrate the modular composition of strain circuits with an automated design strategy to achieve a target behavior from a large space of possible functional circuit architectures. This paper provides synthetic biologists with an alternative solution for the problems of scalability, robustness, and modularity.


---

# Peer review - Round 1

Editors:
- Xiaojun Tian, https://ror.org/03efmqc40 Arizona State University, School of Biological and Health Systems Engineering United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74540.sa1](https://doi.org/10.7554/eLife.74540.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Modular, robust and extendible multicellular circuit design in yeast" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. One of the major concerns is that I am not sure if and how the authors consider the cell growth and growth feedback into their design and modeling? The growth rates could heavily depend on the burden caused by the circuits, and host cell growth could dilute the gene expression. Will a small difference in growth rates lead to the imbalanced ratio of the strain or even loss of one of the strains in the long term? Especially in the experiment with the concentration of the upstream strain increased to10-fold. If appliable, the authors could discuss the relevance of growth rate and growth feedback in the design of multistrain circuits when they talk about the discrepancies between the simulations and experimental data. Here are some relevant publications (PMID: 29414718, 32251409)

2. The multicellular circuits in the currents look much more complicated than the original design. For example, the original toggle switch only needs two genes. In contrast, now four strains are needed in the authors' multistrain toggle switch. Similar to the logic gates. So it will add complexity and limits the scalability and robustness. What we really need is the simplicity and modularity of the circuit design is still maintained for the multistrain circuit. An in-depth discussion is expected in the revised manuscript.

3. Looks like the increased nonlinearity with external positive feedback was not used at all for the multistrain circuit designs. If so, what is the purpose of this section? Would that be used for the bistable switch? Maybe two strains instead of four is enough to make a multistrain bistable switch.

4. In the introduction, I suggest the author discuss the potential loss of modularity in the single-strain circuit but which can be solved with multiple strains. Some relevant publications (PMID: 33558556).

5. While the modeling framework can generally be applicable to all the strains, it would be better for the audience to understand if the authors specify what x1 and χ2 represent in the circuits.

6. What is the potential mechanism of ultrasensitivity in the strain in Figure 1D 2nd panel where n=2.2 was found? Would using the 1st-order Hill repressing function add or decrease some of the nonlinearity if you compare activation cases where a linear function is used?

All the reference of figures needs 'Figure ' or 'Figure' before figure number/panel

Figure 2A, what is the yellow semicircle? Should it be removed?

What is the reason why there are only 3 data points in Figure 2D-panel 4?

How did the author decide which data points are used for fitting while the rest for validation?

7. The area of bistability in Figure 3D needs to be defined.

Page 9, typo, the toggle switch circuit should be four-strain, not five-strain.

Add unit for the growth rate in Figure S10.

8. Orthogonality or no cross-talk between signaling molecules should be supported by either references or the first-hand data in this work. Please add this information when combing signals was mentioned at the first time in line 130. This data could further support the claim in line 406 that modularity is achieved through cell-cell communication that avoids cross-talk.

9. Line 309, based on the estimated growth rates in SI Figure 10, growth rates are actually statistically different by using t-test. Why did the authors say "we could not detect any growth difference…" here?

10. Line 389, what do the authors mean by "cytometrically isolating the sensor strain from other strains"? Do you mean data gating or cell sorting? The cytometer Accuri C6 cannot do cell sorting.

11. Line 418, it is unclear what individual cell difference that the authors refer to? Please be explicit about the difference.

12. Line 426, similarly, it is unclear what differences are in the initial strain populations? Please be explicit about the difference.

13. Consider changing the chemical formula H2O (lines 435 and 438) to sterile deionized water if applicable.

14. Line 439, please specify as yeast Saccharomyces cerevisiae strain MATa W303-1A.

15. Line 441, when using CSampler plate adapter, what is the temperature of the plate exposed to during the measurement?

16. For others to reproduce the results, please provide the details.

17. Line 444, what is the flow rate of cytometer?

18. Line 451, in 16 hrs of overnight growth, what is the rpm setting of the shaker? Are the shaker settings the same across all the experiments? What is the vessel, a tube or a plate, and what catalog number from which company?

19. Line 452, in 10 hrs of growth, what is the vessel? Is it the same rpm setting? After dilution to 3 mL medium, what is the vessel, a tube or a plate?

20. Line 453, what is the stock concentration of the inducers? 1000x stock?

21. Line454, when taking 100 uL samples periodically, do the author replenish 100 uL fresh medium after each sampling?

22. Line478, did the authors replenish fresh medium after sampling 120 uL every 3 hours?

23. Line 33. This sentence "Albeit very successful, this approach shows its limitations when it comes to scalability and robustness." is redundant.

All the numbering of the figures in the main text did not start with "Figure." Please add it.

24. Line 123, A. thaliana and C. papaya should be italic.

25. Line 155, please indicate where readers could find the data of the auxin activating strains which have a 3 fold-change activation.

26. The labeling of figure panels which use uppercase A,B,C… is not consistent with the labeling in the caption which use lowercase a, b, c….

27. SI Figure 8 and SI Figure 11 are better re-named as SI Note 1 and SI Note 2 because they are not figures.

28. Line 292, should "a set concentrations" be written as "a set of concentrations"?

29. Line 296, should Figure 3E be Figure 3F?

30. It is much clear to draw the bistable switch and the fifth reporter strain in Figure 3F.
