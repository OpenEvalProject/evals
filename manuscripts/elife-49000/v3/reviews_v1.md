# Peer review - Round 1

Editors:
- Dominique C Bergmann, Stanford University United States

Reviewers:
- Johannes Liesche, Northwest A&F University China
- Michael Knoblauch, Washington State University United States
- Valentin Couvreur, Université catholique de Louvain Belgium

## Review text

DOI: [10.7554/eLife.49000.sa1](https://doi.org/10.7554/eLife.49000.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Plasmodesmata (PD) are highly regulated channel-like structures between plant cells that enable movement of diverse molecules including metabolites, proteins and viruses. Long standing questions include how the PD is structured and how this structure enables selectivity that changes during plant growth and upon stress.

In this manuscript, the authors present a mechanistic model to investigate the relation between the geometry of PD, molecular diffusion rate across PD, and molecule residence time in the PD. Key achievements are the scaling of single PD models to whole cell-cell interfaces, providing valuable insight on the design principles of PD and their distributions, as well as providing a tool to predict flux based on structural parameters. This is especially important for internal plant tissues that are not accessible for many experimental approaches. The major novelty of the model is that it is based on a realistic description of PD geometry and mostly relies on measurable parameters. It is a valuable companion to the direct measurements of symplasmic fluxes using molecular reporters and new microscopy technologies allow the fast acquisition of datasets about PD geometry, but that cannot be exploited to their full potential without modelling tools. The release of an open source version of their model constitutes a substantial service to the plant biology community.

Decision letter after peer review:

Thank you for submitting your article "From plasmodesma geometry to effective symplastic permeability through biophysical modelling" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Hardtke as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Johannes Liesche (Reviewer #1); Michael Knoblauch (Reviewer #2); Valentin Couvreur (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Through discussions among the reviewers it was clarified that further experiments would improve the manuscript, but were not strictly necessary for the work to be a strong advance for the field, so long as a number of textual changes were made give a clear context for this work in light of previous studies. For this reason, I am compiling the extensive notes from the three reviewers as a list below. Please consider these previous data when writing a revision and a response.

Overall, it will be essential to demonstrate that the model has broad applicability, but to recognize that it was not yet tested in many situations.

1) Since the model was only applied to a single interface, and reviewer one seems to think the data basis seems to be handled loosely, please see comments from reviewer 1 to address this issue.

2) A more careful evaluation of the current literature, including the discussion of previous models by various authors, is needed.

3) The authors should consider if their model could be even more ambitious, for example by including evaluation of neck length and non-straight shapes.

Reviewer 1:

Introduction paragraph four: The paper by Liesche and Schulz, 2013, is not presented here accurately. This paper compares three different models of PD anatomy. One of them is a cytosolic sleeve model that shares quite some similarity with the model proposed here. The sub-nano channel model was only developed for a very specific question: whether PD can be constricted enough to enable the filter effect that has been ascribed to them as part of the polymer-trap mechanism for phloem loading. According to the hypothesis, sucrose should be able to diffuse through the PD at the bundle-sheath-to-phloem interface, but the slightly larger raffinose should not. It was the aim of that paper to test what kind of PD architecture could be compatible with this mechanism.

Introduction paragraph five: There is no principle limit to using fluorophores of different sizes. Terry and Robards, 1987, actually used tracers of all sizes. Only because fluorescein, especially as carboxyfluorescein diacetate (CFDA) it is widely used, because it crosses membranes, allowing for non-invasive observations.

Modern tracer-based approaches using confocal microscopy can yield very similar results. Compare Rutschow et al., 2011 and Liesche and Schulz, 2013. See also Liesche and Schulz (2012, Plant Physiology), who compared permeabilities across plant species and different cell-cell interfaces.

Photoactivation and photobleaching approaches are not time consuming. Quite the opposite. Application of tracer, sample preparation and imaging can easily done within half an hour.

Introduction paragraph six: I suggest formulating with greater care. Photoactivation and photobleaching approaches as well as GFP transport studies have been very valuable tools for assessing PD function.

The incompatibility here could have very different reasons. A better citation would be Liesche et al., 2019, which actually tries to compare structure-based modeling with functional data. As mentioned above, the Liesche and Schulz, 2013, paper had a different objective.

General comment to the Introduction: I advise a more nuanced view at the current state of the field and approaches carried out in the past. Also, I recommend using the Liesche et al., 2019 paper in Plant Physiology as starting point because it actually is the first systematic comparison of PD structure and function. Moreover, this publication clearly demonstrates the need for better models.

Figure 1: The effective symplasmic permeability in a file of cells also depends on cell size and properties of the cytosol.

Final paragraph of the Introduction: Python is a start, but how about making a standalone app? Or an add-in/macro for Excel? Something that any molecular biologist (and especially students) can use! Last year I got quite a bit of experimental data on phloem transport and I wanted to check it against theoretical models that have been described as easy to use. My basic Matlab skills were not enough to make it work. In my opinion, if you are serious about getting a lot of scientists to try the model, you have to provide a truly easy-to-use solution.

Results subsection “Outline of the model”: Many of the equations used in this model were applied to calculate PD transport for the first time by Liesche and Schulz, 2013. Maybe that should be acknowledged somewhere in this paragraph or the Introduction.

Figure 3: What is the reasoning behind plot B? How can I see from the plot that D always has a big influence (which, of course, is not unexpected)? All values of permeability are very low.

Results paragraph five: density jump is not a term often used in PD literature. You could consider using concentration potential.

Subsection ““Necked” PDs increase molecular flux in thicker cell walls”: I find this heading slightly misleading. Shouldn't it be "dilated PDs increase molecular flux"? Because Rn is the same in both cases, meaning that the neck doesn't change. Or am I just misled by the drawing in Figure 4?

First paragraph of subsection ““Necked” PDs increase molecular flux in thicker cell walls”: Maybe write "electron microscopy" instead of "evidence".

Figure 4: Again, "dilated" seems more appropriate than "necked". Panel C has a different y axis scale from all the other panels. The legend in panel C is confusing as it is missing an α. I recommend either legends in all panels or description in the figure caption.

Figure 4 and accompanying text: Is Rn = 12nm in the 'necked' PD and 17.5 in case of narrow PD? This should be formulated clearly, both in the figure and the text. The drawing above panel A gives the impression that they have the same Rn.

Paragraph three of the same section: In this case the length of the neck region is still 1/3rd of the total PD length, right? It might be worthwhile to also check the effect of variation in the length of the necked region. Ideally, this should also be one parameter of the python tool, because it can be estimated from TEM images.

Subsection “The desmotubule increases PD transport and changes the dependence on particle size”: I also find this heading misleading. My first intuition would be to compare a PD with DT to a PD without DT.

In the same subsection what exactly does the assumption on selection towards size-selectivity mean? That a plant would make the PD as narrow as possible, depending on the molecule that is supposed to pass? This assumption might be valid for relatively big molecules, but probably not for small ones (below 1-2nm). Except for the very special PDs in the polymer trapping species mentioned earlier. I recommend discussing this assumption in more detail.

Where exactly does the "see methods" refer to? I don't find a section on DT-related calculations in the methods.

Paragraph two of subsection “Clustering of PDs in pit 1elds reduces effective symplastic permeability”: Wasn't Rn = 12 nm in Figure 4?

In paragraph three of the same section: Rpit is not in the list of mathematical symbols. Moreover, it is not clear why the radius of a pit field should be comparable to the radius of individual PD, since the number and size of PD within a pit field can vary.

In the final paragraph of the same section: How should this be measurable? As a correlation of clustering with wall thickness?

Figure 7: In panel A, is the distance between PD or the radius of the pit field constant?

Paragraph three of subsection “Application of the model to compute effective permeability for fluorescein derivatives”: With a density of 5 (as specified by Zhu et al., see comments below), it seems like the value for Rn should be 22 nm.

Paragraph four: Why is a density of 10 μm2 used here instead of the value from Zhu et al. (5.4 μm2)?

Also didn't a previous paragraph show that central dilation ("necking") is especially effective for long PDs? How does that fit with the results presented here?

Table 1: PD density seems to start at 10 μm2. This value is higher than the 5.4 μm2 specified by Zhu et al. (Table 2). Their value should be considered a max value as the area that was analyzed by Rutschow et al. is reaching into the mature root zone already. Mature zone has much lower density values (0.62 μm2, Table 3 in Zhu et al.).

In paragraph five the model seems incompatible with the low-concentration H2O2 data. At a density of 5.4 μm2, Rn would need to increase to over 40 nm according to Figure 8B. This seems unrealistic. An increase in PD number can also not be expected because of the short treatment period of 2h.

“We also compared the results obtained with our model and the sub-nano channel model reported before (Liesche and Schulz, 2013).”: This makes very little sense as this model was put forward only for a very specific case, as mentioned above. It would be better to compare with the cytosolic slit model that was also described in that paper.

Discussion paragraph two: Again, this model should not be compared here or it should be clearly stated that it was not developed to be applied in this way. Instead the authors should compare their model to the cytosolic sleeve model of Liesche and Schulz (2013) or the 'pure diffusion' model by Doelger et al., 2014 or the model for 'diffusion through simple PD' included in Ross-Elliott et al., 2017.

“For example, sucrose moves symplastically from bundle sheet cells (BSC) to intermediary cells (IC), where it is polymerized into the larger oligomers raffinose and stachyose, that do not diffuse back in detectable amounts”: It should be mentioned that this only happens in certain species (active symplasmic phloem loaders) with the Cucurbits as the most prominent example.

Discussion paragraph four: The Liesche et al., 2019, paper does not analyze correlation of PD length with permeability at the BSC-phloem interface of active symplasmic loaders. It analyzes correlations of PD anatomical parameters (including length) with permeability across species. I don't understand why a correlation of PD length with permeability would be expected, as the study generally finds permeability to depend to a much higher degree on PD diameter. Please also note that it is very unlikely that a bulk flow was overlooked in that study as the measurements were performed on detached leaves. Indeed, this has been tested by Liesche and Schulz, 2012 who compared full photosynthesising leaf and cut-out tissues and found no difference in PD permeability in tobacco.

Discussion paragraph six: please include 'at the root unloading zone'. Funnel PDs are not found at other phloem interfaces.

“Applying our model for diffusion as a sole driver of symplastic transport can indeed explain experimentally observed measurements of effective symplastic permeability for CF, but only with somewhat wider PDs/neck regions or several fold higher PD densities than usually measured by EM.”: This statement seems to contradict itself. In addition, I highly recommend application of the model to additional interfaces. Liesche et al., 2019, for example, found a model that matches observations of permeability for the bundle-sheath-phloem interface, but not for the bundle sheath-mesophyll interface. In the present case, it should be noted that PD density and dimensions were determined for sand-grown plants (Zhu et al., 1998), whereas effective diffusivity was measured for plate-grown plants (Rutschow et al., 2011). I don't know how growth conditions affect PDs, but it has been previously shown that there are big differences, for example in gene expression, between soil- and plate-grown plants. I mention this just to illustrate the need for additional tests.

“Our model can also explain the effect on permeability after treatment with high and low concentrations of H2O2 in Rutschow et al., 2011.”: Please reconsider this statement regarding low H2O2 in light of comments above.

I am very skeptical about the conclusion. Stress perception, signaling, and two rounds of twinning, all within 2h seem unrealistic. I also didn't find evidence for such a rapid multiplication of PD numbers in the two citations provided here. Moreover, 30 PD μm2 would be an extremely high number, that, to my knowledge, has never been observed at a "regular" cell-cell interface.

Discussion paragraph seven, “Despite these deviations, comparing our model to the sub-nano channel model, we found that the latter requires roughly twice as high PD densities to produce the same permeability values P (CF)” and following sentences: Again, this is not an appropriate comparison. Please compare to other models listed in a comment above.
