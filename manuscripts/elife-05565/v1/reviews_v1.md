# Peer review - Round 1

Editors:
- Taekjip Ha, University of Illinois, Urbana-Champaign , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05565.016](https://doi.org/10.7554/eLife.05565.016)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “A simple biophysical model emulates budding yeast chromosome condensation” for consideration at eLife. Your article has been favorably evaluated by Aviv Regev (Senior editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This manuscript takes a computational approach to study the mechanisms responsible for chromosome condensation in budding yeast. Using the simplifying assumption of a bead spring model for nucleosomes and various ways to represent condensin (bridging two sites or more sites, Type I and Type II) they go a remarkable long way toward capturing the major experimental measurement in the literature as well as their new data. Known sites of condensin binding are assumed to coalesce into one complex temporarily if they come within 40 nm of each other, the capture radius consistent with the physical dimension of condensin. The lifetime of the complex is used as a parameter that can be used to tune the dynamic nature of such interaction and is the sole parameter varied between interphase and mitotic chromatin. In Type II model, more than two condensin binding sites are allowed to coalesce. Remarkably, simulations can explain the main features of the experimental data with Type I model performing significantly better. What's attractive about this work is that a simple physical model can get us quite far in explaining the chromosome behavior at a quantitative level, and that the model is general enough that straightforward extensions to include other effects may be possible in the future. In general this is a nice manuscript and clearly explained.

Main points:

1) It is unclear how some of the parameters were set. Presumably, these parameters are determined to satisfy the constraints provided by modern biophysical measurements referenced but currently, their description is too cursory to help the readers understand why these numbers were chosen. For example, entropic force are set at 17 pN, presumably to give a kick to a nucleosome at each time point, but it is not clearly stated why previous observations referred to demand this particular value. The same for the spring constant for internucleosomal tension, 50 pN/nm. For a typical displacement during the simulation, what is the resulting internucleosomal tension? Please note that if the forces go beyond a few pN, the nucleosomal DNA will unravel to a large degree, which may not be physiological, and may also affect the simulation itself to such a degree that required modifications to the model. If there is not actual basis for the number, does it mean that the authors have tried a range of forces and spring constants and only this set of values is able to fit the data? What if the Type II model works better if a different set is used for this parameter?

There are two sentences hinting at how the parameters were chosen.

“The balance of all forces are calibrated based on experimental measurements of nucleosome movements and the angles between neighboring nucleosome linkers.”

“Parameters with defined values are benchmarked based on the observed α angles and local movements of nucleosomes, as described above.”

But there isn't even any reference given what these experimental measurements of nucleosome movements are and the alpha angles. At the minimum, they need to show how the chosen set of parameters are compared to the experimental measurements of nucleosome movements and the angles and show that these choices are unique. If there are other sets of parameters that are similarly good, they need to show that the main conclusions of the paper still hold with those alternative sets of parameters.

2) They find the measured distance using TetO and LacO markers (670 nm) to match the starting configuration of the model. The statement that the correspondence implies the configurations are similar is over-interpreted. These data are correlative, not proof of a common structural basis. In addition, they measured only one set of loci, which limits the statistical power of the statement quoted below:

“This striking correspondence implies that interphase chromatin in vivo adopts a configuration of similar dimensions to an unconstrained nucleosome fiber.”

3) The authors state that persistence length increase with greater genomic distance, as expected from loop models. As the authors know, Lp is defined as <cosΘ(s)> = e(-s/l), where Θ(s) is the angle between two ends on a chain separated by contour length s. My understanding was that the persistence length was dictated by the physical properties of the chain, independent of where you are on the chain. Again, there is no question that the chain explores more space in the middle (Increased Rc, see Verdaasdonk, ibid.) and less at the ends, but this is not due to change in Lp, rather at least for a chromosome is a result from tethering. The authors need to justify their statement that Lp increases with increased genomic distance.

4) The conclusion that condensin is responsible for individualization is unfortunately rather trivial. It is based on the fact that intramolecular interactions will always dominate intermolecular interactions. This falls out of the polymer books referred to above. Thus it is the case that condensin will further the tendency for chromosome individualization, but it is not causative.

5) One suggestion that is hinted at in the Introduction but is not well emphasized is the proposal that no scaffolding structures are required to account for the experimental data. In this sense, Maeshima, 2014 was referred to as being supportive of the loops with scaffolding model, but in fact Maeshima, 2014 was agnostic about the presence or absence of scaffolding (see Figure 3 of Maeshima, 2014). Would it be possible to suggest that the present work is able to differentiate between models that Maeshima, 2014 could not? On a similar note, 2014 Cell paper by the Heard lab should be referenced as it examined the chromosomal conformations using a physics-based polymer model.

6) Is the inter-chromatin marker distance determined via imaging two colors a distance projected to the plane of imaging or a 3D distance? The method indicates that it is the 3D distance. If so, it should be mentioned explicitly in the main text. Also, determining distance based on two color imaging is not trivial due to chromatic aberration and the authors need to elaborate how much confidence they have on the distribution of distances. This is critical because the deviation of the distribution from gaussian was used to deduce Kurtosis and to provide additional support for their model.

In summary, this is an interesting model that emphasizes how few parameters are needed to recapitulate the course-grain behavior of eukaryotic chromosomes. There are several places that the authors need to clarify and expand to make the paper more accessible to beginners in polymer physics. The main concern is about the choice of parameters and there isn't information given how the parameters were optimized to fit what types of experimental constraints, and how unique the parameters are. What if another set of parameters that can fit the constraints just as well show that the main conclusions do not hold anymore?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for sending your work entitled “A simple biophysical model emulates budding yeast chromosome condensation” for consideration at eLife. Your revision has been evaluated by a member of our Board of Reviewing Editors. Although the revision has improved the manuscript significantly, it needs additional revision to address one major point and one minor point described below.

Major point: The authors still do not show how their parameters are benchmarked.

“Parameters with defined values are benchmarked based on experimentally observed α angles (Luger, 1997; Bednar, 1998; Engelhardt, 2007) and local movements of nucleosomes (Hihara, 2012), as described above.”

At the minimum, they need to show the experimental observed alpha angle distribution, i.e. probability distribution vs alpha and show that their simulated alpha angle distribution matches the experimental distribution. In addition, they need to show, preferentially in figures, how the simulated local movements of nucleosomes match the experimental movements.

Minor point: They argue in the rebuttal that 2-5 pN of force should not unravel DNA by referencing a 2001 paper. However, more recent papers in PNAS by Michelle Wang's group and Carlos Bustamante's group showed that DNA indeed unravels at such forces.
