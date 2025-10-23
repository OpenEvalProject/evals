# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/02feahw73 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72187.sa0](https://doi.org/10.7554/eLife.72187.sa0)

The growth of bacterial colonies on solid substrates is a common assay used in a variety of settings, from probing bacterial organization in biofilms to spatial population genetics. The common setup is an outward growing colony from a central seed. In this work, Basaran et al., study a colony growing inward from an annulus. The authors show that this geometrical modification has profound consequences on the alignment of rod-shaped bacteria. This is caused by a flow alignment effect, and lead to a radial ordering reminiscent of an aster or +1 topological defect. This result is motivated by experimental observations with E. coli and interpreted using modern active matter theories, with ample support from extensive numerical simulations of detailed finite element and continuum models.


---

# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/02feahw73 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72187.sa1](https://doi.org/10.7554/eLife.72187.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Large-scale orientational order in bacterial colonies during inward growth" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Suraj Shankar (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Substantiate your claim that the ordering is caused by flow alignment effect by reporting the flow distribution observed experimentally and comparing it to the theoretical prediction (reviewer #2 question 1)

2) Specify how stress is computed in the simulations, and discuss the extent to which it can be determined experimentally. (reviewer #1 question 2 and reviewer #1 question 1))

3) Improve the discussion of the multilayering transition, and in particular the role of in-plane stress in the process along the lines suggested by reviewer #1 question 1 and reviewer #2 question 2 and question 4

4) Provide a point-by-point answer to all the reviewers comments and questions.

Reviewer #1:

This manuscript combines experiments, theory and simulation to study bacterial patterns in a colony growing inwards, from an annulus. The authors find that in this geometry growth leads to leads to the formation of an aster, which is a defect of topological charge +1, where bacteria tend to align in the radial direction. Previously, a growing colony of bacteria was reported to lead to nematic microdomain formation, with bacteria aligning tangentially at the colony edge, with half-integer defects in between microdomains. Overall I think this work is a nice example of an application of topology to bacterial biophysics, and is likely to appeal the growing active matter community.

The combination of experiments, theory and simulation renders the results convincing. It is nice that the theory allows to get a mechanistic and fundamental understanding of the reason for the aster formation, which can be traced back to the nonlinearity of the bacterial velocity/flow profiles. It is also nice that the simulations reproduce all previous observations in different geometries, providing validation of the current results.

Although overall the methodology is sound and the results appear robust, some clarifications are sought as follows.

1. In the orientational patterns in Figure 3 it appears that some bacteria align out of the plane. If this is the case, and not a visualisation issue, it would be good to mention the relevance of the verticalisation, or to perform simulations where this is disallowed as in a growing monolayer.

2. It would be good to describe in a bit more detail how the plotted stress is computed in the simulation and how it could be estimated experimentally.

3. The patterns in multilayer colonies are of interest but it would be good to add a discussion of the reason why different surfaces lead to results which are so different.

Recommendations for the authors:

As mentioned I find this work interesting and I believe it will stimulate discussion in the active matter and bacterial biophysics community. Specifying more in detail what said in the public summary:

1. I would encourage authors to discuss the issue of verticalisation and to specify more clearly where the director can escape to the 3rd dimensions in their monolayer colony simulations (I understand this is possible in multilayer colony simulations).

2. Please specify how stress is computed, is this a component or a scalar built starting from the stress tensor? This should be specified in the main text.

3. It could be said more clearly that the inward colony is a particular geometry where g' (in the manuscript notation) is non-zero, there could be others as well. Simulations of expanding monolayers I believe suggested a possible radial orientation at the edge for sufficiently large colonies, I think this is mentioned in Ref. 42.

4. Is the drop in nematic order e.g. in Figure 3d, which occurs close to the critical radius for which v is about 0, robust and can be understood via flow-mediated rotation as well? Sorry if I missed this.

5. The final part on competition is interesting but I am missing the difference between e.g. a and c in Figure 6 or in general where red and green are swapped but the ratio between long and short is the same. Are these not symmetric?

6. A very minor point: why is the left-hand side of Eq. 6 not written as a material derivative?

Reviewer #2:

The growth of bacterial colonies on solid substrates is a common assay used in a variety of settings, from probing bacterial organization in biofilms to spatial population genetics. In this work, Basaran et al., study how crowded bacterial colonies invade an enclosed space, in contrast to the more common setup of a growing monolayer that expands outward in a unconstrained fashion. This seemingly innocuous modification has dramatic consequences as the authors show. Geometric confinement and growth from cell division dictate a characteristic velocity field that vanishes at a finite radius and the resulting shear flow aligns bacteria to orient in a radial fashion. The colony wide radial ordering is reminiscent of an aster or +1 topological defect seen in liquid crystals. A key point emphasized in the paper is that such large scale ordering of bacteria does not occur in outward expanding colonies, but is typical of inward growth. This result is motivated by experimental observations with E. coli and interpreted using modern active matter theories, with ample support from extensive numerical simulations of detailed finite element and continuum models. The structure and flow generated by radially oriented bacteria is shown to affect multilayering, both in simulations and in experiments with prepatterned annular rings of bacteria. Finally the authors demonstrate a potential biological significance of such orientational order by considering (in silico) two competing bacterial strains that are genetically neutral but have different lengths. The enhanced propensity of the longer bacterium to radially order endows it with a selective advantage to out compete the shorter strain in a spatial setting.

I find that most of the claims are well substantiated and justified by the data presented, though a few points need better support. The main strength of the paper is the involved and detailed numerical modelling employed to describe the invasion of bacterial colonies. It is an impressive amount of computational work. While some of the main points such as the emergence of a radial aster accompanied by a sign changing velocity field in inward growth are recapitulated in experimental data, the authors only make qualitative comparisons with the model. This I feel is a missed opportunity that can be easily remedied given the present data, particularly in the case of patterned colonies (Figure 5). For instance, it is unclear what selects the critical radius Rc, and how it is determined by the initial inoculation geometry. A more quantitative comparison between the experimental and numerical data might help elucidate this point more.

Another weakness is in the discussion surrounding multilayer formation which is a bit disjointed and separate from the first part of the paper. The primary claim rests on a plausible argument suggesting compressive stresses near the critical radius cause buckling and multilayer formation, but the current data is only partially convincing. Figure 4 only demonstrates the presence of multilayering in the finite element simulations and in the experiments but does not validate the suggested mechanism. A straightforward resolution would be to present measurements (at least from the simulation) of the hoop and radial stress in the monolayer and correlate it with the flow, radial order and buckling. The experimental demonstrations also lack descriptions of simple details regarding their setup at various places, which needs to be improved.

In the last section on bacterial competition with differential length strains, I feel the claim regarding the enhanced radial order in the longer bacterium is also not sufficiently substantiated. The red and green curves in Figure 6a-f are meant to demonstrate this claim, but all three plots look rather similar and it is unclear how statistically significant the difference between the curves really is. Either the data must be presented along with a statistical analysis demonstrating significant difference in radial order or the claim must be toned down. Note, the statement about enhanced radial order doesn't necessarily affect (though it is suggested as a causal mechanism) the more significant and consequential result regarding the excess area fraction of the longer bacterium over the shorter, which does demonstrate the claimed selective advantage.

Recommendations for the authors:

Most of my comments are regarding presentation. The current structure of the paper is a bit confusing with the many different numerical simulation methods and experimental setups used. The following suggestions may help clarify and improve the paper. I recommend publication once the comments and questions are satisfactorily answered.

1) The experimental data in Figure 1 only shows the presence of radial order (Figure 1d), but the following figure panels (the rest of Figure 1, and also Figures 2-3) provide details of both radial ordering and the velocity profile. The latter is shown to be the more important and primary ingredient (in numerical simulations) that causes radial alignment of bacteria. In this regard the experimental results of Figure 1only provides circumstantial evidence for the proposed flow induced mechanism. Only much later, in the section on "Inward growing domains in monolayer colonies", is it mentioned that "So far, we studied naturally emerged inward growing domains on agar surfaces. These domains are randomly formed across the plate. In these experiments particularly, the confinement is defined by the crowded multilayered environment. Thus, observing critical radius and detailed velocity profiles are not possible." The lithographically patterned bacterial rings on a PC surface shown in Figure 5 do allow the measurement of both radial order and the flow field, both of which display the qualitative features predicted by the model.

I would hence suggest moving part of the results on patterned bacteria to the beginning, as it provides a clearer and more striking comparison with the numerical work. It should also be clarified when the experiments in Figure 1 are discussed whether the bacterial colony exhibits multilayering outside the field of view shown, in which case prevents a good measurement of the flow field is not possible. Several details about Figure 5 are missing though. What bacteria were used for these experiments and what are the time stamps for the various snapshots in panels a and b? Are the plots in d and e also averaged over 4 independent experiments? Presumably, the whiter regions in the phase contrast images are small patches of double or triple layers. These points should be clarified and explicitly mentioned.

2) Is it understood why decreasing substrate friction permits larger monolayers? Is there a way to test this using the 3D FEM simulation? It would be helpful if some intuition could be given about the connection between friction and buckling, perhaps as a balance of traction forces and growth pressure? On line 256, it is mentioned that "Previous studies showed that, particularly, the surface friction and stress accumulation are responsible for the formation of this multi-layered structures". What previous studies are being referred to here?

For the FEM simulations modelling biofilm forming bacteria, what parameters were modified? The methods section primarily doesn't seem to provide any details about this.

3) While one of the main strengths of the paper is the sophisticated modelling, the use of so many different methods (2D and 3D FEM, continuum theory) makes the reader wonder what benefit is gained from one method over the other. In particular, it is unclear what specific role the continuum active nematic model plays in understanding the phenomena of radial ordering in growing bacterial collectives. All of the results from the continuum model in Figure 3 are essentially the same as obtained from the detailed FEM simulation in Figure 2. Although the use of active nematic continuum models to describe growing bacteria has become fashionable in recent years, it is unclear in the current paper if it offers any new insight that may not be gained otherwise.

I would suggest that the authors reword this section to highlight specific benefits and insights gained from using the continuum model, or move some of the discussion to the SI. It might also help to frame the benefit of the continuum model as generalizing the results (by virtue of coarse-graining over irrelevant microscopic details) beyond the specific bacterial and particle based implementation. As of now, the relevance of the active nematic model is not apparent.

4) I don't quite understand the line "Herein, experimentally we only observed inward growing domains around the inner edge because the accumulated stress triggers multi-layer formation" (Line 206-207). What does stress triggered multilayer formation have to do with observing (or not) inward growth of the colony? I thought the former was causal consequence of the latter and not the other way around.

As mentioned earlier, I think it would be useful to present stress profiles (both radial and hoop components separately as a function of r) from the simulations to substantiate the mechanism triggering buckling and multilayer formation. I suspect that the annular geometry and self-induced confinement due to cell proliferation generates a compressive hoop stress that underlies escape into the third dimension. In this regard it might be worth making a comparison with a classic wrinkling instability of thin sheets in the so-called Lame problem (see for instance, Davidovitch et al. "Prototypical model for tensional wrinkling in thin sheets." PNAS 108.45 (2011): 18227-18232.) In the passive elastic case, outward tension combined with the annular geometry of the elastic film generates compressive hoop stresses that are resolved by wrinkling. Analogously, growth (instead of outward external tension) combined with the geometry leads to a potentially similar effect, now in an active bacterial layer, which resolves the stresses by forming multiple layers, rather than wrinkling.
