# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47551.sa1](https://doi.org/10.7554/eLife.47551.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper reports on the discovery of an unusual and fascinating form of motility in a magnetotactic bacterium. Through a combination of experiment and theory the authors have found that the two flagellar bundles work in opposite ways – one pushing and one pulling the cells through their fluid environment in double-helical paths. The very fast motility and very rapid trajectories changes appear to arise from these features. This work will surely be of interest not only to those interested in the biology of motility, but also physical scientists interested in the fluid dynamics of locomotion.

Decision letter after peer review:

Thank you for sending your article entitled "High-speed motility originates from cooperatively pushing and pulling flagella bundles in bilophotrichous bacteria" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor.

The essence of the criticisms concerns the interpretation of the experimental observations (and the possibility of achieving better imaging of the flagella) and the analysis of the computational results. In both cases further details are needed, and in the former it appears that additional imaging would be in order.

Reviewer #1:

In my opinion the topic of the article is interesting as it identifies a new flagellar arrangement for motility (though similar simultaneous pushing/pulling has been observed for species with bundles at opposite poles rather than the same hemisphere, both in magnetospirilla). However, I am not completely convinced by the authors' evidence. As detailed below, while the story is quite plausible, the experiments seem to not have key evidence which I would have expected to have easily been observed if the scenario were true, and the numerics are not performed (or perhaps just not described) in a way that convincingly rules out other hypotheses.

1) In the dark field imaging, bright spots on the cell body are identified with flagella. This identification is not obvious to me, and it is quite puzzling why the authors do not actually image the flagellar bundles. If the bundles were indeed extended from the body in front and behind the cell, I would expect that they could be visualized which would definitively prove their proposed configuration. In Son, Guasto and Stocker, 2013, sheathed flagella are quite readily imaged. In my experience, there may be difficulty seeing flagella with darkfield at 1640 fps, but they should be readily imaged at <200 fps using their camera. Note that 200 fps is more than fast enough to resolve the larger helical motion with period 72 ms. It is unclear if the authors attempted this. If the authors tried and were not able to see a leading and lagging bundle, I would take that as evidence against their claim.

2) The authors describe the double helical path as "unexplored" in the Introduction, but based on my knowledge, double helical paths are what should be expected from most types of propulsion by flagellar bundles, with the main distinguishing feature being the size of the larger helix. The smaller helix has in the past been attributed to the rotation of the bundle or flagellar helix, see Keller and Rubinow, 1976. The larger helix arises anytime there is non-axisymmetric propulsion, see Hyon, Powers, Stocker, Fu 2012 and has been observed in many species, albeit with varying sizes of the larger helix. As discussed in point 3 below, an important implication of this is that the bar for numerical simulations cannot be simply qualitative as in "straight" vs. "double-helical," but must involve some quantitative analysis of the trajectory pitch and radius.

3) The numerics have not been described in a way that clearly rules out alternative hypotheses.

First, as mentioned above, the quantitative details of the helical trajectory are important, but these are not well-matched. The authors say that their trajectories match the experimental helical diameter and period of the trajectories but not the pitch. The results are strongly dependent on the angle between the bundles, which is used as a fitting parameter. They say that they believe that the pitch could be matched eventually by fitting the opening angle and flagella length but do not actually do it.

Second, changing directions of bundles is also likely able to produce many different types of helical trajectories with varying pitch and radii. These have not been eliminated as possibilities.

Third, the fast reorientation in the simulations is interesting, but again, it is not ruled out whether other configurations could also yield similarly fast reorientations.

Fourth, the speed of the swimming is used as supporting evidence, but this is achieved by increasing the torque on the motor (to a value somewhat higher than some report for E. coli, but not out of the realm of possibility). If one is allowed to adjust the motor torque, then any speed can be reached for any configuration.

Reviewer #2:

The manuscript reports results of a detailed experimental and numerical study of the swimming motion of magnetotactic cocci, bilophotrichous bacteria with flagellar bundles at both poles. The experiments show that bacteria swim along a double helical path, with a very high swim speed and short reorient time compared to other bacteria. Hydrodynamic modelling demonstrates that this is due to a pushing and a pulling bundle. Experimental and numerical results are in good semi-quantitative agreement.

I think this is a very nice investigation, which carefully elucidates the complex swimming motion of a bilophotrichous bacterium. Experiment and hydrodynamic simulation complement each other very well to characterize the geometry of the flagellar organization and swim pattern. Thus, I strongly support publication of this manuscript in eLife.

I have only a few comments, which the authors should consider before publication:

1) In the main text, the authors talk about flagella as well as flagella bundles. I found this pretty confusing, until I saw Figure S1. I recommend clarifying this point early in the main text.

2) The reorientation angle could be discussed in a bit more detail. As far as I understand, as one bundle changes its direction of rotation, both bundles are in pushing (or pulling) mode, which leads to a (roughly) 90° reorientation of the swimming direction. This would explain the particular value of the reorientation angle. This seems to be somewhat similar to the behavior seen in simulations of the early stages of swimming and bundle formation of peritrichous bacteria, when the flagella are initially pointing in arbitrary directions, see, J. Hu et al., Sci. Rep. 5, 9586 (2015). However, the bundle rotation direction has to change back. This would result in another 90° angle, but uncorrelated with the first. Please clarify.

Reviewer #3:

The authors present a very thorough study of the exceptional swimming capacities in terms of speed and possibilities to suddenly change direction, displayed by a magnetotactic bacterium strain (MC-1). They use a holographic method to track in 3D the swimming trajectories and fast camera observations of the rotating body to visualize the positions of the flagellar bundles hooked to the cell. They discover the presence of a double helical path characterizing the swimming kinematics that can be explained by two sets of pushing and pulling flagella bundles working cooperatively and positioned within the same hemisphere of the spherical body. They simulate a hydrodynamic model to corroborate their finding, yielding very reasonable quantitative agreement with the experiments. The model, when set to some limits also helped to discover a new swimming pattern under the application of a magnetic field. Importantly, they also find that to reach such performances, the flagella must assume motive torque and bundle rigidity significantly larger than what is usually obtained for other bacterial strains.

I found the experimental study excellent with important conclusions on an original propulsion model. My opinion is that the paper could deserve publication in eLife. My only concern is sometimes on the pedagogy and clarity of the explanations delivered. I believe this could be significantly be improved. I do not deny that the authors really tried to make an effort to deliver their message, in particular visually. However, it remains that sometimes, it took me several subsequent readings of the same paragraph to really understand what they actually meant. Figure 3 is a particular example of that, and I found in this instance, very hard to follow the reasoning in the caption in association with the visual message. Then I would suggest that the paper could significant gain in pedagogy and impact, if it was critically read by someone who could help to clarify some explanatory sentences.
