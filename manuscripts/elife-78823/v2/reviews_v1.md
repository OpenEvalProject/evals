# Peer review - Round 1

Editors:
- Alphee Michelot, https://ror.org/02me5cy06 Institut de Biologie du Développement France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78823.sa0](https://doi.org/10.7554/eLife.78823.sa0)

This paper describes an inexpensive but very powerful microfluidic approach to quantitatively determine the viscoelastic properties of living cells from their deformation in a flow. Its implementation seems simple so that even people not specialized in cell mechanics can use it, and the method offers the possibility to perform measurements on a large number of cells (up to 50-100 per second). The data are compelling and this technique should set a new standard in the field.


---

# Peer review - Round 1

Editors:
- Alphee Michelot, https://ror.org/02me5cy06 Institut de Biologie du Développement France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78823.sa1](https://doi.org/10.7554/eLife.78823.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Viscoelastic properties of suspended cells measured with shear flow deformation cytometry" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Clément Campillo (Reviewer #1); Timo Betz (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

You will see from the comments of the two Reviewers that they agree on the usefulness of your method. However, they also point out some weaknesses in this study that need to be addressed in the revision. Essential revisions should include:

1) A much more in-depth introduction and discussion of existing methods (see Reviewer 1's comment). The interest of a method paper is certainly to describe new protocols/tools, but also to discuss their interest (and also their disadvantages) compared to existing tools. This is particularly important as papers using microfluidics to characterize the mechanical properties of cells have recently been published (including the paper by Oliver Otto which is mentioned). This discussion would be useful for less specialized readers (e.g. cell biologists wanting to characterize their cells but not necessarily having a strong biophysics background). Why would it make a difference in their experiments to have a frequency-dependent response? In what specific cases would having frequency dependent values allow them to discriminate cells better than static parameters?

These modifications to the manuscript should be particularly easy to make.

2) Further analysis of the experimental data to justify or refute the validity of a single powerlaw approach versus a two powerlaw approach, or a modification of the experimental setup to acquire and present data only in the linear regime (see reviewer comment 2). This would answer two questions:

(a) whether the discrepancy is truly due to strain stiffening, and

b) whether one can reliably use the data in the high frequency level to obtain the correct stiffness and powerlaw exponent. This point will certainly give you much more work, but it is essential to address it to convince us that the final values and model are reliable.

3) Presenting experiments investigating the role of intermediate filaments from the same cell line so that the results are easier to interpret.

Reviewer #1 (Recommendations for the authors):

I am not able to evaluate the validity of the Roscoe model and the equations 10 -19, nevertheless the agreement between the measurements obtained by the two techniques used are very convincing. This is even surprising in the case of THP1 cells (Figure 5a and b), because SF-DC and AFM probe cell mechanics at very different scales.

The novelty of the technique compared to Fregin NatComm 2019 has to be discussed in detail as the main claim of the article is the approach for cell mechanics measurements. From a physics point of view, the technique presented here gives for instance G' and G' as a function of frequency, whereas Fregin et al., give only effective cell elasticity and viscosity. Therefore, the measurement of cell's mechanics is more complete with this assay, as described in the manuscript l.217. Note that the experimental setup presented in the manuscript is simpler than the one presented by Fregin et al., which might favor its use by other labs. This justifies the publication of the article in eLife, as physical methods are in the scope of the journal. On the other hand, such a detailed physical description might not be required to only discriminate between cell populations, as it is the main application of this type of experiment.

The introduction is very short and the authors start presenting their technique immediately. I think the readers need more context on why these type of measurements are useful, which experimental techniques are used and the mechanical models on which these techniques rely. Some of these aspects are in the Discussion section, to highlight the interest of their technique but the introduction should be more detailed.

On the tank treading movement of cells in shear flows, several articles are cited but the article comports no discussion at all on this mechanism, and how it has been characterized for red blood cells for instance.

Similarly, some readers may not be familiar with viscoelastic models, the article is not very pedagogic on this.

Reviewer #2 (Recommendations for the authors):

While I really like the method, and think it should be published in eLife after successful revision, I am worried about the reliability of some parts of the paper. Mainly, I think the strain stiffening explanation needs to be better nailed. Why is it not possible to change the conditions, so that the deformation remains in the linear regime throughout the measurement. Even if correct, all the data that is in the strain stiffening regime would then lead to wrong stiffness and powerlaw exponent. Would it not make more sense, to only focus on the results as close to the measurements as possible? We have a G' and G' for a given frequency, why do we need to translate this into other parameters that are even less reliable?

Besides this main concern, I have a couple of other points that I would like to transmit to the authors to consider for a further improvement of the paper.

– Why is in figure 2a/b no data given for the position close to 0? I did not realize an explanation for this when I read the paper. Is it problematic in this regime to determine the deformation?

– In figure 2 g it is shown that for a large enough shear rate the rheometer and the flow cytometer values of viscosity are the same. If I understand this correctly, it also means that only right at the center the shear rate is so low that this matters… however in the distances that correspond to this shear no measurements are given. Is this right? If so, maybe it is worthwhile to mention this in more detail.

– Why seem the stiffness values of the PAA beads to be so pressure dependent as seen in figure 4e. And in figure S3, the values of the AFM and the flow cytometer should be plotted on the same y scale, or ideally even plotted over each other. What keeps you from adding the values a in b,c, and the same for d and g?

– In Equation 2 µ seems not to be defined.

– For the cell experiments with vimentin it is very confusing why you compare WT 3T3 with MEF desmin-knockouts and knockins of vimentin. It looks like you don't have WT MEF. Why comparing different cell types. This makes it hard to believe that your conclusion is correct. At least all differences between 3T3 and MEFs might be because of the different cell type. Use also MEFs for the 'normal' situation.

– Also, there is a statistical test in figure 7 b and c missing. How many cells did you measure for each of the datapoints in 7b,c?

– In the discussion you mention a local viscosity of the fluid. This is a bit misleading as it suggests that the viscosity depends on the position, but it depends on the shear rate (which depends on the position for a given pressure).

– It should be more focused on the actual measurement of G' G' at a single frequency. I think we don't know sufficiently well if a single powerlaw can explain the measurements, to use this hypothesis in a way that makes the reader think the method provides information about frequency dependence from a single snapshot.

– It would be good to get a reference for the statement that you find similar values for the E50 as other authors (line 269).

– Please tone down the statement of line 284-286. There is no statistical test, and you compare apples with oranges… don't say that you have shown the effect of vimentin. All you see is the increase in stiffness in the knock-in situation.

– It would be interesting to provide a measure of variance in the text describing the different \σ values. (line 502-503)

– Why not using a non-shear thinning medium to do the measurements? Everything should be much more simple there.

– You treat \eta_0, \tau, and \δ as independent parameters. Is this really the case, or could some depend on each other? Also please give the values you measured for these parameters.

– You say that stress stiffening happens, but then you use a model (equations 21,22) that breaks down under these conditions. Here you basically say that the measurements you obtain in the high frequency regime do not work. Why are these not excluded, and how do you determine the stress at which we cannot take the G' and G' as unaffected.

– In Line 580 you say the AFM goes from 0.1 to 150Hz, but the measurements you show are up to 10000 rad/s. What is right?
