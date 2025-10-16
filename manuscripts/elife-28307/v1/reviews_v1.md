# Peer review - Round 1

Editors:
- Deborah Yelon, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28307.024](https://doi.org/10.7554/eLife.28307.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cell-accurate optical mapping across the entire developing heart" for consideration by eLife. Your article has been reviewed by 1 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Hee Cheol Cho (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Understanding the interplay among individual cells during organogenesis can provide fundamental insights into tissue-level morphogenesis during development. The quest for this essential knowledge has been elusive partly due to limitations with imaging instrumentation. In this manuscript, Huisken and colleagues adapt their pioneering technology of high-speed, high-resolution light sheet microscopy to study how conductivity evolves and matures during zebrafish heart development. Specifically, they built a high-speed, dual-color light sheet microscope to image the heart at subcellular resolution, based on a published design called post-acquisition synchronization. They then developed a set of computational tools to analyze calcium activity at cellular resolution. These include a curved cylindrical coordinate system to describe cell position along the midline, a graph-based method to calculate the conduction speed in terms of the number of cells per unit time, and a 2D projection method to display cellular properties across the 3D heart. Finally, they applied these methods to measure the emergence of region-specific activation and conduction between 36 hpf and 44 hpf that accompanies the morphological emergence of three regions of the heart.

The biological insights revealed are in line with what is known in the developing heart, including the faster Ca2+ rise time in atrial vs. ventricular cardiomyocytes and slower conduction velocities in proximal atrial myocytes and in AVC. These data validate that the temporal and spatial sampling rates were adequate so that the inherent lag between the beginning of biological phenomena and image capture would be irrelevant. Comparison of physical conduction velocity, afforded by this technology, and the routine biological conduction velocity revealed that the larger dimensions of atrial cardiomyocytes gave rise to faster physical conduction velocity. Altogether, this study presented a set of impressively careful technical characterization that will benefit the field. In particular, this manuscript makes a very important contribution by reconstructing the geometry of the heart, and then transforming it to a convenient "map" of the cell positions, permitting the neighbor relationships to be more easily seen and analyzed. Moreover, the manuscript is well written with beautiful figures that are well organized, intuitively informative and aesthetically appealing. However, the manuscript has several limitations in its current form (as described below) that should be addressed in a revised version.

Essential revisions:

1) The authors must be clear in their title, Abstract, and elsewhere in the text that these are hearts without excitation-contraction coupling. This is an understandable decision in the experimental design, but this does mean that the normal mechanics of the contractile tissues and the normal forces from the blood flow through the system are absent. It is probably beyond the scope of this paper to perform the study with function intact, but the authors can only argue this if they are clear in the title, Abstract, and text.

2) The authors discuss proudly the performance of the microscope used, and they show lovely data. However, beyond knowing what it is better than, the paper does not really teach the reader what the microscope is. More detail is desirable here.

3) The key steps in re-assembly of the imaging data into the volumetric rendering are underspecified, and more detail is needed.

4) The authors quantify that, strikingly, less than 10 pacemaker cells serve as the origin of electrical activation at 52 hpf. The location of these cells is the sinus venosus at the heart's inflow in a ring-like formation. The authors cite an earlier work which indicate that the myocardial cells in the outer curvature are oriented perpendicular to the inflow-outflow direction. Do the authors suggest that the pacemaker cells exhibit anisotropy at the level of individual cell morphology, linking them in a ring-like manner, and this is paralleled by neighboring atrial myocytes oriented orthogonal to the inflow-outflow line? If so, it may be easier to see this by illustrating the estimated cell shapes of the pacemaker cells as scaled ellipsoids.

5) In terms of the biology presented here, there seem to be some missed opportunities. Could the authors address how the magic transition occurs between 36 hpf and 44 hpf (e.g. gradual and smooth, or sudden appearance with chaotic transition)? Could they address whether heterogeneity exists at the cellular level (aside from the pacemaker) and, if so, whether cellular heterogeneity matters in the transition?
