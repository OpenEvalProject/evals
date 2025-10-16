# Peer review - Round 1

Editors:
- Randy B Stockbridge, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90606.3.sa0](https://doi.org/10.7554/eLife.90606.3.sa0)

This article offers important updates to qFit, the state-of-the art tool for modeling alternative conformations of protein molecules based on high-resolution X-ray diffraction or cryo-EM data. While the authors provide convincing examples of qFit's performance, these are restricted to selected test cases. This article will be of interest to structural biologists and protein biochemists more generally.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90606.3.sa1](https://doi.org/10.7554/eLife.90606.3.sa1)

Summary:

Protein conformational changes are often critical to protein function, but obtaining structural information about conformational ensembles is a challenge. Over a number of years, the authors of the current manuscript have developed and improved an algorithm, qFit protein, that models multiple conformations into high resolution electron density maps in an automated way. The current manuscript describes the latest improvements to the program, and analyzes the performance of qFit protein in a number of test cases, including classical statistical metrics of data fit like Rfree and the gap between Rwork and Rfree, model geometry, and global and case-by-case assessment of qFit performance at different data resolution cutoffs. The authors have also updated qFit to handle cryo-EM datasets, although the analysis of its performance is more limited due to a limited number of high-resolution test cases and less standardization of deposited/processed data.

Strengths:

The strengths of the manuscript are the careful and extensive analysis of qFit's performance over a variety of metrics and a diversity of test cases, as well as the careful discussion of the limitations of qFit. This manuscript also serves as a very useful guide for users in evaluating if and when qFit should be applied during structural refinement.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90606.3.sa2](https://doi.org/10.7554/eLife.90606.3.sa2)

Summary:

The manuscript by Wankowicz et al. describes updates to qFit, an algorithm for the characterization of conformational heterogeneity of protein molecules based on X-ray diffraction of Cryo-EM data. The work provides a clear description of the algorithm used by qFit. The authors then proceed to validate the performance of qFit by comparing it to deposited X-ray entries in the PDB in the 1.2-1.5 Å resolution range as quantified by Rfree, Rwork-Rfree, detailed examination of the conformations introduced by qFit, and performance on stereochemical measures (MolProbity scores). To examine the effect of experimental resolution of X-ray diffraction data, they start from an ultra high-resolution structure (SARS-CoV2 Nsp3 macrodomain) to determine how the loss of resolution (introduced artificially) degrades the ability of qFit to correctly infer the nature and presence of alternate conformations. The authors observe a gradual loss of ability to correctly infer alternate conformations as resolution degrades past 2 Å. The authors repeat this analysis for a larger set of entries in a more automated fashion and again observe that qFit works well for structures with resolutions better than 2 Å, with a rapid loss of accuracy at lower resolution. Finally, the authors examine the performance of qFit on cryo-EM data. Despite a few prominent examples, the authors find only a handful (8) of datasets for which they can confirm a resolution better than 2.0 Å. The performance of qFit on these maps is encouraging and will be of much interest because cryo-EM maps will, presumably, continue to improve and because of the rapid increase in the availability of such data for many supramolecular biological assemblies. As the authors note, practices in cryo-EM analysis are far from uniform, hampering the development and assessment of tools like qFit.

Strengths:

qFit improves the quality of refined structures at resolutions better than 2.0 A, in terms of reflecting true conformational heterogeneity and geometry. The algorithm is well designed and does not introduce spurious or unnecessary conformational heterogeneity. I was able to install and run the program without a problem within a computing cluster environment. The paper is well written and the validation thorough.

I found the section on cryo-EM particularly enlightening, both because it demonstrates the potential for discovery of conformational heterogeneity from such data by qFit, and because it clearly explains the hurdles towards this becoming common practice, including lack of uniformity in reporting resolution, and differences in map and solvent treatment.

Weaknesses:

The authors begin the results section by claiming that they made "substantial improvement" relative to the previous iteration of qFit, "both algorithmically (e.g., scoring is improved by BIC, sampling of B factors is now included) and computationally (improving the efficiency and reliability of the code)" (bottom of page 3). However, the paper does not provide a comparison to previous iterations of the software or quantitation of the effects of these specific improvements, such as whether scoring is improved by the BIC, how the application of BIC has changed since the previous paper, whether sampling of B factors helps, and whether the code faster. It would help the reader to understand what, if any, the significance of each of these improvements was.

The exclusion of structures containing ligands and multichain protein models in the validation of qFit was puzzling since both are very common in the PDB. This may convey the impression that qFit cannot handle such use cases. (Although it seems that qFit has an algorithm dedicated to modeling ligand heterogeneity and seems to be able to handle multiple chains). The paper would be more effective if it explained how a user of the software would handle scenarios with ligands and multiple chains, and why these would be excluded from analysis here.

It would be helpful to add some guidance on how/whether qFit models can be further refined afterwards in Coot, Phenix, ..., or whether these models are strictly intended as the terminal step in refinement.

Appraisal & Discussion:

Overall, the authors convincingly demonstrate that qFit provides a reliable means to detect and model conformational heterogeneity within high-resolution X-ray diffraction datasets and (based on a smaller sample) in cryo-EM density maps. This represents the state of the art in the field and will be of interest to any structural biologist or biochemist seeking to attain an understanding of the structural basis of the function of their system of interest, including potential allosteric mechanisms-an area where there are still few good solutions. That is, I expect qFit to find widespread use.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90606.3.sa3](https://doi.org/10.7554/eLife.90606.3.sa3)

Summary:

The authors address a very important issue of going beyond a single-copy model obtained by the two principal experimental methods of structural biology, macromolecular crystallography and cryo electron microscopy (cryo-EM). Such multiconformer model is based on the fact that experimental data from both these methods represent a space- and time-average of a huge number of the molecules in a sample, or even in several samples, and that the respective distributions can be multimodal. Different from structure prediction methods, this approach is strongly based on high-resolution experimental information and requires validated single-copy high-quality models as input. Overall, the results support the authors' conclusions.

In fact, the method addresses two problems which could be considered separately:

- An automation of construction of multiple conformations when they can be identified visually;

- A determination of multiple conformations when their visual identification is difficult or impossible.

The first one is a known problem, when missing alternative conformations may cost a few percent in R-factors. While these conformations are relatively easy to detect and build manually, the current procedure may save significant time being quite efficient, as the test results show.

The second problem is important from the physical point of view and has been addressed first by Burling & Brunger (1994; https://doi.org/10.1002/ijch.199400022). The new procedure deals with a second-order variation in the R-factors, of about 1% or less, like placing riding hydrogen atoms, modeling density deformation or variation of the bulk solvent. In such situations, it is hard to justify model improvement. Keeping Rfree values or their marginal decreasing can be considered as a sign that the model is not overfitted data but hardly as a strong argument in favor of the model.

In general, overall targets are less appropriate for this kind of problem and local characteristics may be better indicators. Improvement of the model geometry is a good choice. Indeed, yet Cruickshank (1956; https://doi.org/10.1107/S0365110X56002059) showed that averaged density images may lead to a shortening of covalent bonds when interpreting such maps by a single model. However, a total absence of geometric outliers is not necessarily required for the structures solved at a high resolution where diffraction data should have more freedom to place the atoms where the experiments "see" them.

The key local characteristic for multi conformer models is a closeness of the model map to the experimental one. Actually, the procedure uses a kind of such measure, the Bayesian information criteria (BIC). Unfortunately, there is no information about how sharply it identifies the best model, how much it changes between the initial and final models; in overall there is not any feeling about its values. The Q-score (page 17) can be a tool for the first problem where the multiple conformations are clearly separated and not for the second problem where the contributions from neighboring conformations are merged. In addition to BIC or to even more conventional target functions such as LS or local map correlation, the extreme and mean values of the local difference maps may help to validate the models.

This method with its results is a strong argument for a need in experimental data and information they contain, differently from a pure structure prediction. At the same time, absence of strong density-based proofs may limit its impact.

Strengths:

Addressing an important problem and automatization of model construction for alternative conformations using high-resolution experimental data.

Weaknesses:

An insufficient validation of the models when no discrete alternative conformations are visible and essentially missing local real-space validation indicators.
