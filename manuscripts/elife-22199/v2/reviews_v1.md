# Peer review - Round 1

Editors:
- Robb Krumlauf, Stowers Institute for Medical Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22199.019](https://doi.org/10.7554/eLife.22199.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Systems biology derived source-sink mechanism of BMP gradient formation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Robb Krumlauf as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors use quantitative imaging and modeling to come to the conclusion that a source-sink mechanism underlies the BMP/Chordin patterning system. This is novel as formation of a BMP gradient by a source-sink mechanism is distinct from previously reported models such as transcriptional, shuttling, or counter-gradient mechanisms. The measurement of BMP2 diffusion in vivo is novel. The topic is not only of broad interest but also quite controversial, and this study brings some much needed clarity to the field. The main weakness is the limited attempt to minimize the parameter space used for the modeling. Some of the measurements are difficult but there are several key measurements that need to be made. The computational and experimental analyses are incomplete, and some details of simulations have not been provided. For their model to be made more convincing a variety of concerns/comments should be fully addressed.

Major specific points:

1) The source-sink model is puzzling in light of previous reports showing that zebrafish and Xenopus chordin mRNA injections at the one-cell stage can fully rescue zebrafish chordino mutants (Fisher and Halpern, 1999; Schulte-Merker et al., 1997). In these embryos, injected chordin mRNA is present throughout the embryo and yet, the rescued mutants develop normally to adulthood (and presumably form a normal BMP gradient). The mRNA rescue experiments also call into question the notion that the transcriptional pattern is critical for BMP gradient formation. The authors should discuss the various models in light of these reports.

2) Relevant to the above, did the authors measure the effective diffusion of BMP2 by FRAP in chordin mutant embryos? This will provide experimental evidence to test the models.

3) Cell numbers increase substantially between 4 and 7 hpf, when the authors report a steep increase in the BMP gradient. How does the change in cell number in the zebrafish gastrula (between 4-7 hpf) compare to that during fly DV patterning? To what extent does this account for the increase in gradient slope in zebrafish?

4) The authors state "The equations were simulated 1,000,000 times".

Table 1 lists 15 free parameters; therefore each parameter can, in principle, only take ~2.5 different values when combined randomly (2.52^15 is ~10^6). However, the plots in Figure 4 suggest that many more values have been chosen for individual parameters. The authors should clarify how the parameters were varied in the simulations.

5) The authors state "To our surprise, there are greater than 50 times the number of source-sink to counter-gradient modeling solutions (Figure 6B'), suggesting that the source-sink mechanism predominates." However, the number of different parameter combinations that can explain the data cannot be taken as a measure of support for a specific modelling solution. Different parameter combinations can result in similar solutions simply because the model is not identifiable or because it is difficult to find a unique solution when trying to fit the data directly.

6) If the authors already have or are making a BMP-destabilized GFP/degradFP fusion, precise measurement of BMP2 decay rates would be useful to distinguish between the models. If these are available it would be useful but not essential for the paper.

7) Why were the equations solved for the developmental window from 3.5 to 5.7 hpf and not from 4.7 to 6.7 hpf, when the pSMAD intensities were measured?

8) The authors presumably solved the equations in 1D in order to sample parameter space in a reasonable amount of time. I think it would add to the paper if the authors showed that the same parameters found to satisfy the 1D case would also set up the 3D P-Smad gradient when solving the equations in the hemispherical geometry of the zebrafish embryo as in Zhang, Lander, and Nie, J. Theor. Biol., 2007.

9) Can the P-Smad5 gradient of the chordin heterozygotes be included? Why are they "not shown"? Does the model fit the chordin heterozygote P-Smad5 gradient?

10) The pSmad5 measurements are impressive but the models ultimately rest on the BMP transcript and (active and inactive) protein expression profiles. I understand that there are no good antibodies to detect BMP but minimally, the authors need to use now standard quantitative fluorescent in situ hybridization approaches to measure BMP transcript distribution.

11) The BMP FRAP experiment goes a long way to reduce parameter space but why not also measure BMP diffusion in the presence of Chordin? This experiment seems trivial but would greatly help to test the shuttling model.

12) The characterization of the bmp2-venus chimera is too superficial. Does it have the same range and activity as wild-type bmp2?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Systems biology derived source-sink mechanism of BMP gradient formation" for further consideration at eLife. Your revised article has been favorably evaluated by Marianne Bronner as Senior editor, a Reviewing editor, and three reviewers. =

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. In the absence of measurements of BMP diffusion in the presence of chordin or Chordin protein expression, the alternate model Zinski et al. suggest for BMP gradient formation cannot be substantiated. To support their clams, it is crucial that the authors:i) determine how the BMP gradient forms in the presence of uniform chordin ii) show expression of tagged BMP / Chordin proteins at early gastrula stages in mutants injected with RNA. iii) clarify how random sampling was done.

Key comments:

1) In response to how BMP diffuses in the absence and presence of chordin (previous review comments 2 and 11), in the revised Zinski m/s, the authors examined BMP diffusion without chordin. However, they did not examine BMP diffusion with uniform chordin. This is a crucial test of the model which is missing.

2) In their explanation of how their data and preferred model can explain the previous reports of rescue of chordino mutants with uniform chordin injections, Zinski et al. contend that chordin RNA injections likely do not generate uniform Chordin protein expression in embryos. But no evidence is provided to support this view – either experimentally or in their simulations. (The triple morphant is not relevant to the comment).

3) Regarding how parameters were varied in their simulations, the authors state that they prefer random sampling as opposed to a regular grid.

Did the authors refine sampling depending on the outcomes? If solutions did not change in a region in parameter space, did they increase the sampling density?
