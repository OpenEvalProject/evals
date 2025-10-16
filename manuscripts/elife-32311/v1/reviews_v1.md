# Peer review - Round 1

Editors:
- Anna Akhmanova, Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32311.040](https://doi.org/10.7554/eLife.32311.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A quantitative approach for the spatio-temporal distribution of 3D intracellular events in fluorescence microscopy" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Anna Akhmanova as the Senior/Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper presents a software tool (QuantEv) for quantitative analysis and visualization of the spatial distribution of intracellular events imaged by fluorescence microscopy and represented by static or dynamic descriptors associated with spatial coordinates. The potential practical value of the tool is demonstrated by studying the distribution of moving Rab6 fluorescently labeled membranes with respect to their direction of movement in differently shaped cells, as well as the position of the generating hub of Rab11 positive membranes, and the effects of actin disruption on Rab11 trafficking in relation to cell shape. The paper is well written, and the results are interesting.

Essential revisions:

1) The manuscript ignores extensive prior relevant work on similar problems. The analysis methods described are simple, and not particularly innovative. Evidence of generalizability is lacking. By not considering and incorporating prior approaches, the potential capabilities and applicability of the software have been significantly limited. It is especially important in describing new software to compare its performance to existing approaches. These comparisons should include not just one similar method (kernel density estimation) that is not widely used but other methods (e.g., http://doi.org/10.1038/nmeth.1486). For example, although developed for a different application, the software tool plusTipTracker (http://dx.doi.org/10.1016/j.jsb.2011.07.009) can also perform various dynamics analyses related to cell location, and should be discussed. The same goes for TrackMate (http://doi.org/10.1016/j.ymeth.2016.09.016). More generally, some discussion is needed of what, exactly, can and cannot be done with existing tools, to make the novelties and benefits of the proposed tool more explicit.

2) It seems that the statistical test the authors are proposing is focusing on comparing two groups using the Wilcoxon signed-rank test. While this is fine as such, often in Biology more than two groups need to be compared with each other; like wt, mutant, and rescue for example. Also, the possibility to compare more than two groups is important to avoid problems with repetitive testing between groups. The problem is the additive per comparison error. This issue should be addressed, and potential solutions should be included in the next version.

3) The authors suggest using intensity as a weight for the analysis. In the cases used in the synthetic test images test and likely in the experimental data here the intensities are comparable. However, the potential user needs to be instructed that appropriate normalization procedures need to be applied in case that intensities are used as weight. Likewise, the segmentation needs to start from a similar selection. The authors should at least discuss this necessity and provide what the prerequisites are for the input.

4) The only datasets used in paper are artificial, in that cells were constrained to specific geometries. This reduces the inherent complexity with unknown other effects. Most investigators would not choose to use artificial geometric constraints, and no analysis is presented for images of cells that show natural variation in shape, either in vitro or in vivo. Such variation might overwhelm the straightforward approaches the authors describe and this possibility should be investigated. Application of the methods to an image dataset for unconstrained cells should be included.

5) The claim that the proposed framework is "generic and non-parametric" seems too strong. In the paper only a few very specific applications are investigated. And many of the underlying components of the framework are not exactly non-parametric. For example, the kernels involved in the weighted density estimation have parameters, and the distance measures depend on the number of bins. This claim should be toned down.

6) The authors claim that their framework is more sensitive than the Kernel density maps. This asks the question of the discriminatory power of the method. The potential to differentiate distribution patterns depends on the resolution of the input; this should be discussed.

7) The meaning of the results of the various analyses is often unclear and very limited in terms of providing understanding of mechanisms for any of the systems studied. Since the paper is written for a general audience, this should be improved.

8) A number of specific comments on the text must be addressed:

Introduction, first paragraph “Automatic methods have the obvious advantage of being quicker and reproducible. However, most computational methods are based on the complex combination of heterogeneous features such as statistical, geometrical, morphological and frequency properties (Peng, 2008), whichmakes difficult to draw de1nitive biological conclusions”: This statement ignores extensive work on generative or mechanistic models, which produce interpretable parameters. Such work includes mechanistic models of dynamics of endocytic vesicles (e.g., http://doi.org/10.1038/nmeth.1237) and cytoskeletal dynamics (http://doi.org/10.1126/science.1100533), and generative models of vesicle distribution (e.g., http://doi.org/10.1371/journal.pcbi.1004614).

Introduction, first paragraph “Additionally, most experimental designs, especially at single cell level, pool together data coming from replicated experiments of a given condition (Schauer et al., 2010; Merouane et al., 2015; Biot et al., 2016), neglecting the biological variability between individual cells.”: Again, this ignores work on generative models that specifically analyzes and captures variation between cells. Past examples include microtubule networks (e.g., http://doi.org/10.1371/journal.pone.0050292), and cell and nuclear shape (e.g., http://dx.doi.org/10.1091/mbc.E15-06-0370). Traditional feature-based methods also frequently analyze heterogeneity within populations (e.g., http://doi.org/10.1371/journal.pone.0102678).

Introduction, third paragraph and subsection “Weighted density estimation”, first paragraph – The use of circular and/or cylindrical coordinate systems for description of object positions within a cell is well established (e.g., http://doi.org/10.1002/cyto.a.20487 and http://doi.org/10.1002/cyto.a.21066) and in these cases rotation angle was more powerfully defined relative to the major axis of each cell rather than being defined by the confinement fields. Alternative approaches to the problem, such as morphing, were not discussed.

Introduction, third paragraph and subsection “Distance between densities”, first paragraph – There is no discussion of more recent metrics related to Earth Mover's Distance that have been described and used to compare subcellular patterns (http://doi.org/10.1007/s11263-012-0566-z).

"The KD approach concludes… Instead, QuantEv selectively identifies…" How do we know which method comes closest to the truth? Can this be verified? Without some control experiment or simulation, how can we conclude that QuantEv is to be preferred over other methods?

Subsection “Visualizing and quantifying the influence of micropatterns on the spatial distribution of Rab6 positive membranes” – There is no clear peak at the two-thirds position in Figure 2D and no evidence of significance or reproducibility is presented.

"Rab6 trajectories were classified into two categories…" How do we know these trajectories are trustworthy? What kind of control experiment was performed to confirm this? This is especially important since it seems the trajectories were not obtained with the best methods available these days (for example according to http://doi.org/10.1038/nmeth.2808 there seem to be better tracking methods than the method mentioned in the subsection “Event detection and localization”).

"we extracted Rab11 trajectories…" Same as previous comment.

"On the image sequences considered in the previous section (see Figure 4A), this distance remains stable (see Figure 5A). We analyzed cells treated with Latrunculin A… the ERC location is moving away as the drug is affecting the cell (see Figure 5B)". But the time scales are very different in these two cases (seconds versus minutes). Control experiments would be needed to confirm that the ERC location in non-treated cells remains stable over the same time scale as in the treated cells.

The claim that the presented software tool "is efficient with small and large amounts of data" has not been demonstrated in the paper. Neither dataset sizes nor processing times are mentioned.

The claim that "QuantEv is quite flexible since the user can specify any distance…" contradicts the statement that "it is fully automated and non-parametric".

"a reference point… and a reference direction have to be specified by the user…" Same as previous comment.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A quantitative approach for the spatio-temporal distribution of 3D intracellular events in fluorescence microscopy" for further consideration at eLife. Your revised article has been favorably evaluated by Anna Akhmanova (Senior/Reviewing Editor) and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

There were significant reservations about using constrained cells, as the use of such cells greatly simplifies the analysis. The authors have now done additional work to add results comparing unconstrained cells and two different types of constrained cells. The results show that QuantEV is able to distinguish among the three groups. However, no perturbation studies (e.g., Latrunculin B) were done with unconstrained cells. Thus the main concern remains about the suitability of QuantEV for use in future studies, the majority of which are expected to be done with unconstrained cells. This is an important point: the method may be able to distinguish changes within constrained cells upon various treatments, but may not be able to distinguish perturbations on the background of significant variation within unconstrained cells. There is no information provided on the variance of the profiles in Figure 2F within the unconstrained population. This is a major concern in the context of the very broad claims made in the manuscript (especially in the Discussion) about the power and generality of QuantEV. To support these broad claims, the authors must provide conclusive evidence that QuantEV can distinguish physiologically relevant changes upon perturbations in unconstrained cells. Since the necessary datasets are undoubtedly available to the authors, no collection of new experimental data is expected to be necessary to address this point.
