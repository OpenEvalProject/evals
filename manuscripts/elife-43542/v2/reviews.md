# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University United States

Reviewers:
- Axel T Brunger, Stanford University United States
- James S Fraser, University of California, San Francisco United States

## Review text

DOI: [10.7554/eLife.43542.038](https://doi.org/10.7554/eLife.43542.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Automated correlation-based structure refinement for high-resolution cryo-EM maps of large biomolecular complexes" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James S Fraser (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Grubmuller et al., use molecular dynamics refinement against a real-space map-correlation coefficient in combination with a chemically-accurate force field in the presence of explicit solvent. In order to better overcome local minima, the resolution of the model map was gradually increased starting at very low resolution to the maximum available resolution of the EM data. Moreover, high-temperature simulated annealing is used. Although each of these approaches individually are not new, this work describes a new implementation that combines all these approaches. However, there are many shortcomings that preclude publication of the present work in eLife as outlined in detail below. Briefly, the main concerns are the lack of comparison to other existing methods, unsubstantiated claims of model accuracy, the lack of other test cases (both at very high and medium-low resolution), and the potential of overfitting.

Reviewer #1:

Grubmuller et al., use molecular dynamics refinement against a real-space map-correlation coefficient in combination with a chemically-accurate force field in the presence of explicit solvent. In order to better overcome local minima, the resolution of the model map was gradually increased starting at very low resolution to the maximum available resolution of the EM data. Moreover, high-temperature simulated annealing is used. Although each of these approaches individually are not new, this work describes a new implementation that combines all these approaches. The method should be a useful new addition to the growing arsenal of tools for the refinement of three-dimensional models against maps obtained by single particle cryoEM.

Please comment on optimization of the resolution ramp, relative weight (force constant), and simulated annealing temperature vs. simulation time. The Materials and methods section suggests that somewhat different refinement protocols were used for each of the four example systems. What rationale was used to design these different protocols? More generally, please provide a guideline for selecting the various parameters.

There is a lack of a comparison to methods that are implemented in other programs, such as Phenix or Refmac. In particular, Phenix does have a simulated annealing option, although it does not use a full force field.

Afonine et al., 2018, showed that judicious use of restraints improves the quality of real-space refinement against medium/low cryo-EM density maps. The presence of such additional restraints may be beneficial during the low-resolution stages of the refinement. Please comment.

As an additional criterion for the performance of the refinements, please calculate the CaBLAM validation scores for the deposited structures and the re-refined structures. In particular, the CaBLAM scores (Richardson, J. S., et al. Acta Crystallographica Section D74, 132-142. (2018), doi:10.1107/S2059798317009834; implemented in Phenix) asses the geometry of peptide bonds and the geometry of Ca atoms.

Reviewer #2:

This well-written manuscript describes methods for the refinement of atomic models against cryo-EM reconstructions. The basis of the method is the inclusion of a biasing term in a molecular dynamics potential that increases the overlap of the model with the experimental map. This approach is not new, and has been used in programs such as MDFF. The authors do describe a new approach to gradually increasing the resolution of the data in refinement, and the application of simulated annealing protocols. However, the limited novelty of the work, and other considerations significantly reduce my enthusiasm. Some important points for consideration:

In the Abstract the authors make several claims for the work:

"The method utilizes a chemically accurate force field and exhaustive thermodynamic sampling while efficiently improving the cross-correlation between the modeled structure and the cryo-EM map. For several test systems of different size with resolutions 2.5-3.4 Å, it generates stereochemically accurate models from cryo-EM data with a low risk of overfitting. The presented automated framework allows efficient refinement of large molecular complexes such as the ribosome without manual intervention or any additional ad hoc restraints, providing a good balance between stereochemical accuracy, refinement time, and hardware requirements."

There are several problems:

- While it is true that the models are improved in some ways after the refinement protocol, in general the rotamer conformations are significantly poorer (outside the realm of what is acceptable for a protein structure), and the Ramachandran distributions also poorer. Therefore the claim of "stereochemically accurate models" is overreaching.

- "Efficient refinement" clearly means different things to different people. For the systems studied the methods described took between 2 and 25 days running on a multiple core system with 2 GPUs. For many researchers this would be considered very long run times, especially when there are other methods that produce comparable results in much shorter times.

- A minor quibble, but the phrase "exhaustive thermodynamic sampling", suggests just that. However, the protocols described are unlikely to be exhaustive. They employ simulated annealing methods which do expand the conformational space that is sampled, but not exhaustively.

There are other issues that need to be considered:

- The authors apply their method to 4 test cases, including a large ribosome structure. However, this is a limited sampling of models, and in particular doesn't include models with very poor starting geometries. All 4 test cases are of high quality to begin with – as judged by the EMRinger score, Molprobity score and other presented criteria. The manuscript would be much more persuasive if it presented results for a larger number of structures – it should be noted that other researchers have applied automated refinement methods to all suitable cryo-EM structures available from the Protein Data Bank. In particular it would be helpful to see results for models with significant initial structural errors.

- The work, as presented, focuses on higher resolution cryo-EM data (3Å or higher is stated in the Abstract). There is definitely a need for accurate refinement methods at these resolutions. However, the quality of starting models at these resolutions is typically very high, and often don't present significant challenges for refinement algorithms. In addition, it is worth noting that, as of a few weeks ago, there are 107 structures from 3Å or better cryo-EM data, 808 structures between 3Å and 4Å resolution, and 515 structures between 4Å and 5Å resolution. The 3.5Å to 5Å resolution range often presents some serious challenges for both model building and subsequent refinement. The application of the methods to 3.1Å and 3.5Å test cases in the manuscript is applauded. However, the manuscript would have been more exciting if it presented a more thorough analysis of the application of the method at resolutions worse that 3.5Å.

- The authors could consider test cases where there is some higher resolution "gold standard" available to validate the results of refinement with lower resolution data. This is, of course, non-trivial, but very helpful in confirming the accuracy and radius of convergence of the refinement method.

- As noted above, much of what is described has been introduced in earlier works, so the novelty is limited. The approach to a gradual increase in data resolution is interesting – blurring of the model density only. However, the authors don't demonstrate that this is an improvement over previous methods.

- Simulated annealing has been already applied in other programs for model to map fitting (DEN, MDFF). This is also used, as an option, in the phenix.real_space_refine program.

- Other approaches to model refinement have been implemented, with the goal of stereochemical quality and computational efficiency. In particular the phenix.real_space_refine program is not mentioned in the manuscript. This program has been used for the successful refinement of many cryo-EM models.

- In the description of the proteasome 3.1A refinement it is stated that "The improved quality statistics for our model (Figure 4A, top-right) now indicate that the conformations of these loops were refined more accurately". How do the authors know this? The model may have improved overall, while the confirmation of these particular loops may be worse after refinement.

Reviewer #3:

The major goal of this paper is to use molecule dynamics simulations to improve the fit and geometry of structures refined against high resolution (better than 4A) maps from single particle cryoEM. The principle contribution is to combine advances (classic work on simulated annealing, MDFF, and recent work from the Tama group) with improved MD and map calculation codes. The manuscript is beautifully formatted and the figures are very clear. The software is benchmarked against a very limited set of targets, focusing on experimental data and previously known crystal structures, which mimics its potential application in the real world. The ribosome dataset seems to be the only one somewhat challenging case, but even that consists largely of a rigid body rotation with few internal degrees of freedom changing during the low resolution part of the search. Given the long run time of the method, and the lack of comparisons against existing software (REFMAC, MDFF, phenix.real_space_refine), it is unclear how widely used this package will become. The major weaknesses of the manuscript are lack of benchmarking against these methods and whether the radius of convergence will hold for poorer starting models (e.g. structures based on homology modeling, etc.).

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Automated cryo-EM structure refinement using correlation-driven molecular dynamics" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Axel Brunger as the Reviewing Editor, and the evaluation has been overseen by John Kuriyan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James S Fraser (Reviewer #2).

The Reviewing Editor and the reviewers believe that this paper would be of considerable general interest, provided that the validity of the method can be demonstrated in a convincing way. They continue to feel, however, that the demonstration that the method performs better than alternative methods is still not convincing. After discussion, we are prepared to consider a revised manuscript that addresses the concerns raised by reviewers. The eventual acceptance of this paper hinges on a satisfactory resolution of these issues. We recognize that the revisions would require a substantial amount of new work. If this is not possible, you might choose to submit this work elsewhere in its present form.

Summary:

In this revised manuscript, the authors have addressed many, but not all, of the concerns that were raised. The use of a "complete" empirical force field (rather than the simplified force fields commonly used in macromolecular refinement packages) seems to contribute to the differences when compared with other methods, along with the use of simulated annealing, and ramping up the resolution. While each of these individual approaches is not new, the authors suggest that the combination of them produces better quality EM structures. If this claim can be substantiated, it would represent a welcome new tool in the arsenal of refinement tools for EM structures. However, we are not convinced that the current manuscript definitely demonstrates such superiority, and major revisions are required for further consideration of this manuscript as outlined in the following.

Critical points to address:

1) Overall, while the manuscript has been improved by inclusion of multiple test-cases of different quality maps and comparisons to alternative (standard) methods. However, distinct alternative approaches were used for each test case and not applied across all examples. For example, MDFF was initially developed primarily for lower (~5-10 A) resolution cases, but is not used for the CorA example here (perhaps the strongest new result in the paper). Please consistently use a common set of alternative (standard) methods for all cases, and, additionally, use methods such as MDFF for the low resolution cases.

2) NSF test case, subsection “N-ethylmaleimide sensitive factor (NSF): comparison with Phenix”: for the re-refinement of the recent NSF/SNAP/SNARE EM single particle structure by White et al., 2018 (Figure 7 in the paper), the most significant advantage appears to be the substantially lower clash score compared to phenix refinement. The authors seem to be able to do better (especially for the clash score), without extensive grid searching (at least as far as we can tell). However, the clashscore itself does not indicate if their refined models are closer to the true structure. We had previously asked for the CABLAM analysis that should be included. Nevertheless, ultimately, the question arises if the re-refined structure is closer to the true structure of the 20S complex. Since there is no higher resolution structure of the entire complex available, the authors could test the quality of their refinement with the D2 domain of NSF by comparing it with the available high-resolution crystal structures.

Other important points to address:

1) NSF test case: "Finally we again point out the strong anti-correlation between the number of steric clashes and rotamer/Ramachandran outliers in the deposited reference and our models (discussed later in the Results section).” Which anti-correlation does this statement refer to?

2) Figure 7: the deposited 6MDO structure (referred to as the "reference" structure) actually has rather reasonable geometry. The improvement by the author's method is primarily a reduction of the clash score (Figure 7B). Please comment and speculate about the reasons (e.g., use of an accurate force field might clean up poorly determined regions?). Note that the Ramachandran statistics also slightly improves, contrary to the suggested anti-correlation (see previous point).

3) Figure 7A: Please calculate the heat map but compared to 6MDO instead of 3J94 as well since 6MDO and 3J94 are not equivalent models (e.g., they just pasted the SNAP-25 N terminal residues into 3J94, in which those residues do not exist in 3J94).

4) Figure 7A: it appears that their method mostly fixed the geometry of the solvent exposed parts of the model, so likely the ATP binding pocket is pretty much the same? These differences could possibly also arise from changes in rigid body positions of the domains in the hexamer. Please comment.

5) Figure 7: clarify how the various parameters for their refinement were chosen. Was there a lot of trial and error involved?

6) "Furthermore, the NSF refinement demonstrates the usefulness of the half-map-based cross-validation procedure as, for a refinement against a full map only, much more refinement runs have to done to identify the optimal map bias". Where is it is shown that more refinement runs have to be performed without access to half maps?

7) The question of whether a single model or an ensemble is more appropriate is worth discussing. For example, the three TRPV1 structures produced by independent refinement vary across the model (Figure 5—figure supplement 2), and may suggest that an ensemble refinement may be suitable. Moreover, the discussion of "ideal geometry and over/underfitting" in the last paragraph of the subsection “Force-field dependence of the model geometry” completely ignores the effect of conformational heterogeneity that may be related to the non-ideal nature of refining a single conformation against an EM map. Ensemble averaging misinterpreted as a single structure is a possible reason. See Rice, Shamoo and Brünger, 1998, and Burnley et al., 2012 for crystallographic multi-start and ensemble refinements, respectively, and Herzik, Fraser and Lander et al., 2018 and Bonomi, Pellarin and Vendruscolo, et al.2018 for EM structure ensemble refinement. On the other hand, low determinacy of 3D classification and refinement of the particles may be another reason for the non-ideal nature of the refinement. These two issues are likely convoluted and represent a major challenge for the interpretation of single particle EM data. The authors are not expected to perform ensemble refinements, but rather, a discussion of this point is requested.

8) Note that the use of an empirical force field for crystallographic refinement was first suggested by Brunger et al., 1987, and re-investigated in more recent papers, e.g., Fenn et al., 2011. A discussion of this point would be appropriate.

9) How were the MolProbity statistics calculated? There are some subtleties that might need to be taken into consideration. By default Molprobity uses bond lengths for hydrogen atoms that are centered on the X-ray scattering position (electron cloud), as opposed to the nuclear position of the atom – i.e. the former is shorter than the latter (see Protein Sci. 2018, 27:293-315). This can have some consequences depending on the workflow. If MolProbity is given a model containing hydrogen atoms whose positions have been defined using nuclear positions the clash score may be reported as high. Alternatively, if a model is optimized using nuclear position hydrogen atoms, and these are removed, MolProbity automatically adds hydrogen atoms at the electron cloud position, resulting in systematically low clash scores. The authors should consider their protocol in light of this, and make it clear what was done in the Materials and methods section.

10) Is a complete model a requirement for the method? In the Materials and methods section it appears that any missing residues in the test structures were "filled in" using homology modeling or other approaches. Is this mandatory? If so it needs to be clearly communicated in the paper. The creation of parts of models for which there is no clear experimental data to support that model are questionable.

11) The authors make an interesting argument about clashes and side- and mainchain outliers. However, arguing that a very low clash score and a significant number of geometry outliers is reasonable stretches credulity. It is well known from high resolution structures what the expectations are for outliers. It is also observed that at lower resolution it becomes increasingly hard to determine correct rotamer and mainchain conformations based on the experimental data. The authors might be better off to emphasize that they are able to create models with a quality consistent with many other methods at this resolution, often better than the starting models, and accept that there is room for improvement.

12) The authors should be clear what they mean when they use the phrase "overfitting" in this context. There is often confusion about this term's meaning – e.g. fitting of noise, model correctness, determination of the optimal protocol.

13) It would seem appropriate to mention the work of Sanbonmatsu and colleagues: Kirmizialtin et al., 2015.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Automated cryo-EM structure refinement using correlation-driven molecular dynamics" for further consideration at eLife. Your revised article has been favorably evaluated by John Kuriyan (Senior Editor), a Reviewing Editor, and three reviewers.

We thank you for addressing many of our concerns, in particular with the new discussion sections, the CorA analysis, and the comparisons for all refinements. The application to NSF shows that the method can obtain a model that is closer to the true structure as assessed by the agreement with the high-resolution crystal structures of the NSF D2 domain. In particular, the improved placement of the nucleotide is impressive. However, there are some remaining minor issues that need to be addressed before acceptance, as outlined below:

1. Please provide the CABLAM and other statistics (provided in the supplemental files as. tex files) as proper tables.

2. You are correct in their assertion that the CDMD procedure has a larger radius of convergence than the Refmac, Phenix and Rosetta procedures. However, while it is very much appreciated that making use of other programs can be challenging, it is probable that some of the protocols used are not optimal for the particular cases being studied. For example, in the case of phenix.real_space_refine the default protocols are appropriate for refinement of models close to correct, i.e. not significantly displaced from the cryo-EM volume (globally or locally). Moreover, the protocol outlined in White et al., 2018 helps extend the radius of convergence. However, for models that have more significant starting errors, morphing is an important option for increasing the radius of convergence. It can also be necessary to run more refinement cycles to increase the convergence radius. Please comment in the Discussion.

3. The benchmark information in Table 2 is likely to be confusing for many readers (the timings provided in the Benchmark text are very useful). Would it be possible to provide statistics in the form of total run times for refinements in a table form?
