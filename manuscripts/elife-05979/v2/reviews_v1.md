# Peer review - Round 1

Editors:
- Mark S Goldman, University of California at Davis , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05979.010](https://doi.org/10.7554/eLife.05979.010)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Probable nature of higher-dimensional symmetries underlying mammalian grid-cell activity patterns” for consideration at eLife. Your article has been favorably evaluated by Eve Marder (Senior editor), Mark Goldman (guest Reviewing editor), and two reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

In the interesting manuscript “Probable nature of higher-dimensional symmetries underlying mammalian grid-cell activity patterns”, Mathis et al. provide the first principled and theoretically-rooted predictions for how the activity of grid cells might look like in 3D and, more generally, provide interesting predictions on the possible nature of other neural codes for higher-dimensional stimulus spaces, such as e.g. in the prefrontal cortex. The authors do this by considering the Fisher information in a neural code consisting of firing fields that are arranged in a periodic structure in multidimensional space. Under several mathematical idealizations and assumptions, it is argued that the best arrangement for the firing fields is one that leads to maximal packing of the periodic firing fields. These predictions can be tested experimentally in grid-cell recordings in flying bats.

The demonstration that FCC packing of grids is an optimal arrangement of firing fields from the coding perspective is an elegant, intriguing, and valuable result that should be of interest to many neuroscientists, biologists, and physicists. However, despite suggestions to the contrary, the work does not provide a formal argument for optimality of other close packing arrangements (such as HCP and the non-periodic arrangements) and it is not obvious that such arrangements are equivalent from the Fisher information perspective. Furthermore, the work bears close resemblance to unpublished (but cited by the authors and publically posted) work by Balasubramanian et al.

1) The main mathematical derivations are correct and the argument in favor of maximal packing for FCC grids is simple and elegant. However, the work does not provide a formal argument for optimality of other close packing arrangements (such as HCP and the non-periodic arrangements) and it is not clear that all the maximal packing arrangements are equivalent in terms of the Fisher information. The derivation leading to Equation 12 is precise and clear for periodic arrangements that contain one firing field per unit cell (such as the hexagonal packing in 2 dimensions or FCC), but there is a missing link between this derivation and statements about maximal close packing in more general arrangements. This means that the statements on the periodic HCP lattices, as well as the non-periodic hybrids between FCC and HCP, are not clearly justified. This issue, and specifically whether HCP is as good as FCC (or not), must be addressed before the manuscript can be considered for publication.

2) The authors should provide more discussion of the similarities and differences of the present work from that in 2-D lattices by Balasubramanian's group. The reply to reviewers should include specification of how this work provides a significant conceptual advance.

3) HCP and FCC are optimal packings for infinite 3D spaces, but, to our knowledge, there is no mathematical proof for what is the optimal sphere packing for a finite-sized 3D space, such as typical laboratory arenas and rooms. The authors should discuss this “finite size problem”, and in particular, what would happen to the blobs of the grid along the walls of the arena/room. For example, can the notion of maximal-FI/optimal-packing explain the distortions of 2D grids that were recently discovered by O'Keefe's group (in a trapezoid arena) and by the Mosers group (shearing of the grids along the wall)? If so, what would be the implications for 3D grid cell activity near the walls? In a similar vein, could there be a scenario (i.e. a certain ratio of room size to sphere radius) where, for a finite-sized room, an optimal packing will in fact yield elongated columnar hexagons (or elongated “strings of spheres”), as was suggested by the study in rats from the Jeffery group (Hayman et al. 2011)?

4) The manuscript contains some inconsistencies and confusing statements in the discussion of the FCC and HCP lattices. The classification of lattices in 3 dimensions is well established in some areas of mathematics, physics, and engineering, so it is important to be precise and to conform with conventional nomenclature. The FCC arrangement is referred to in the manuscript as the only optimal lattice packing in 3 dimensions, and the HCP arrangement is referred to as a non-lattice arrangement because it cannot be spanned by three vectors with integer coefficients. Both of these statements disagree with the conventional classification of lattices: the FCC as well as the HCP arrangements are perfectly periodic structures.

5) The idea that the function of grid cells is to produce a nested code of position is a hypothesis, not only in three dimensional spaces but also in two dimensions, since the role of grid cells in spatial coding is far from being established experimentally, and even the structure of the grid cell code in rodents has been characterized only in very simple and small environments. This does not diminish the relevance of the theory, but we would prefer to see a larger degree of caution in the discussion on the biological reality.

Minor comments:

1) Due to the existence of global ambiguities, the ability to discriminate between very close locations (quantified by the Fisher information) might not be sufficient to achieve high resolution, as addressed in previous works by the same authors as well as other authors. It is not clear to me that local optimization of the Fisher Information is optimal from this broader perspective, even if this seems reasonable. I suggest the authors clarify or at least acknowledge this point.

2) In spaces of dimension 3 and higher it has been argued by Zhang and Sejnowsky (1998), and by Pouget, Deneve, and Ducom (1999) that it is beneficial to have wide tuning curves in order to maximize the Fisher Information. This brings into question the validity of the assumption that firing fields will have compact support in an optimal code in high dimensional spaces. In general, I thought that the assumption of compact support is perfectly legitimate (and conforms with what we know about grid cells in rodents and crawling bats), but it should be emphasized more clearly that the results rely on this assumption.

3) The diagonal elements of the Fisher information matrix are not the appropriate quantity to consider as a tight bound on the resolution. Instead, one has to consider the diagonal elements of the inverse Fisher information matrix. This is a minor issue because the inverse information matrix scales with the volume of the unit cell in agreement with the conclusions of the derivation. Nevertheless I suggest the authors address this comment by modifying the text in the subsection headed “Fisher information of a grid module with lattice L” below Equation 12.

4) The statement below Equation 4 on isotropy is confusing because the grid cell representation is not truly isotropic (there are obviously special directions in space).

5) We failed to identify in the manuscript a powerful link with cryptography or to the role of maximal close packing in coding theory (which appears there in a different context). Therefore, in my opinion, these declarations in the Introduction do not serve a meaningful or useful purpose.
