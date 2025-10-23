# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61012.sa1](https://doi.org/10.7554/eLife.61012.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The fluid dynamics of filter feeding in sponges is a complex problem on many length scales, from the flagella of filter-feeding cells within small chambers to the large scale flow past the entire sponge. Asadzadeh et al. address a significant puzzle in the physiology of sponges lacking the "gasket" which, in other species, diverts flow toward the filtration devices on the feeding cells. Through a combination of experimental work and numerical computations the authors demonstrate the existence of an unusual flow pattern that accomplishes this diversion, and suggest implications for our understanding of the evolution of the first metazoans.

Decision letter after peer review:

Thank you for submitting your article "Hydodynamics of sponge pumps and evolution of the sponge body plan" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that substantial revisions are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors present a numerical and experimental investigation of the pumping mechanism in filter feeding sponges. The feeding is performed by choanocytes, which comprise a pumping flagellum and a feeding collar that protrude from the wall of the feeding chambers, which has periodically arranged holes through which unfiltered fluid can enter when pulled by the flagellar action.

In this study, the mechanism is examined for the case of sponges that do not possess a "gasket" (canopy-structure) over these feeding collars. The key question that the authors examine is, then, "how is the flow forced through the collars (allowing particle capture), when there is no gasket to stop it simply going straight to the centre of the chamber"?

The answer given is that just as flow is pulled through the holes, a reverse flow (which arises from the condition that flow in the chamber is, at least locally, divergence free), forms above the hole, which creates a stagnation point that pushes the incoming fluid laterally out through the feeding collars.

Essential revisions:

1) On the whole we found this to be a solid paper that addresses an important question by means of computational studies. Having said that, we are disappointed at the lack of physical interpretation given to the setup of the system and the results. In essence, the papers reads like an experimental study of the system with essentially no interpretation of the magnitudes of any of the physical quantities calculated, particularly in light of the fact that sponge hydrodynamics is not a commonly studied subject for the readers of eLife. The authors need to do a serious job of re-presentation of the results to establish the physical significance of various pressures (are these arising from Bernoulli-like pressure differences across the sponge body due to the external flow?), flow rates (say, by comparing them to Poiseuille flow), powers (comparing to the flagellar input power), etc. There is very little in the way of dimensional analysis to make the results intuitively clear. As such, the very many numerical values of physical quantities have no context.

2) From a fluid dynamics perspective, the fundamental result is fairly easy to see, and is simply a manifestation of local mass conservation (though of course retrodiction is of course much easier than prediction). The presentation would be greatly aided by a very simple schematic of the streamlines from two forces above a wall, either side of a hole, below a no-penetration (not no slip) boundary. We would have liked to have seen a reduced model of this kind involving stokeslets over a wall with a gap, which the authors should consider looking at, but this is not is a necessity for publication.

3) The description of the "flagellar vane" is a bit arcane. We are familiar with standard flagellae, and flagellae with mastigonemes, but have not come across this sort of ultrastructure before (is this a uniquely choanoflagellate/sponge structure). Reading other papers helped, but the manuscript needs a clearer description of these 3 types of flagellae, particularly when the image in Appendix 1—figure 1C seems to have ordinary flagellae.

4) An image of gasket-type vs. non gasket type would have helped our understanding of the motivation for the study earlier on. In general, we found that it was only possible to understand what was actually going on by the end of the paper, so it would be good to go through the Introduction once more to make sure it is as clear as possible to the more general reader.

5) The flagellum model (Equation 1) is not arclength preserving. Reading a previous paper it seems that the total change in arclength is only a few percent over a beat, however the velocities on the flagellum will also be subtly wrong, as material points will not be exhibiting the characteristic figure of eight motion. We have convinced ourselves that this doesn't affect the results too significantly (any error would be smaller than the error associated with taking very difficult experimental measurements), so we will not insist on a rerunning of the results, but it would not have been hard to make the waveform arclength preserving.

6) We are confused by the wedge geometry of Figure 2. If fluid leaves the computational domain "vertically" then how is there any net transport of fluid along the long axis of the ascon? Would not the flagella be strongly perturbed by the lateral flow?

7) No detail is given at all as to how the flagella beating is modelled in the CFD code. Are there regularized Stokeslets? Is slender body hydrodynamics used? Please clarify.

8) We strongly suggest the authors avoid the rainbow colourmap wherever possible, as it is not perceptually uniform (see https://peterkovesi.com/projects/colourmaps/) and is also generally bad for people who are colour blind.

9) The authors end up documenting a large number of individual differences between ascon and leucon sponges, but only study them in isolation – and only a subset of them. Compared to leucons, ascons have: (1) no physical gasket (2) shorter collars and (3) one large incurrent pore for 24 choanocytes (per choanocyte chamber), instead of many small pores (one per choanocyte.) Only the third difference is usually considered part of the definition of leuconoid vs. asconoid type, but the paper focuses almost entirely on the first and second differences. We recommend that the authors comment on the third parameter as well – if only by drawing a comparison with their earlier, published model.

10) Regarding the total difference of overall efficiency between the leuconoid and asconoid organizations, the discussion is a bit unclear. The authors state that "Our results indicate that reduced resistance in the ascon and sycon-type aquiferous systems comes with reduced volume filtered for high retention efficiency." But the paper performs no explicit comparison of filtered volumes between sycon and leucons until the very end, and even then it concludes that these are actually not really different: "Furthermore, both experimental and CFD estimates of flow rate per choanocyte [in sycons] are comparable to published estimates for leucon sponges that range from 17 to 236 µm3 s-1 for different species of demosponges and glass sponges (Larsen and Riisgård, 1994; Leys et al., 2011; Ludeman et al., 2017), suggesting similar pumping capacity despite different pumping mechanism." This contradicts the statement of the Introduction – even though the highest pumping capacity reported for a leuconoid sponge (236 µm3 s-1 per choanocyte) is higher than the one reported for syconoid sponges (48 µm3 s-1 per choanocyte) suggesting that the leucon organization has at least higher potential.

We think the authors should settle on one of their two interpretations, or alternatively state that both are valid alternatives. In particular, if leucons do not have higher filtration capacity, what advantage do they have over ascons and sycons (which additionally do not risk clogging, as the authors mention)? What is the specific niche of leuconoid sponges?

11) Figure 2 shows that all flagella within the chamber beat in the same plane (with all vanes parallel to each other), parallel to the long axis. Are there reasons to think this reflects biological reality or is it a simplification of the model?

12) Subsection “Pumping mechanism”: the vane width considered is in the 0.3-0.7 µm range. How was this range of values decided? Is it close to real vanes of calcareous sponges? Why does it stay so far below the collar diameter (2.5 µm)?

13) Some calcareous sponges have a leuconoid organization, yet lack a physical gasket. Can the authors comment on how they think these sponges work?
