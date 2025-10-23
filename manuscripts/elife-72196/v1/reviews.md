# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72196.sa0](https://doi.org/10.7554/eLife.72196.sa0)

This paper explores the question of the optimum strategy for odor detection in a turbulent environment. The authors use high-resolution simulations of turbulent flow to investigate the transport and detection of odors advected by the flow, comparing machine learning strategies based on the temporal dynamics of the signal with those based on intensity. The work should be of interest to researchers working on a broad range of problems in sensation and navigation across scales.


---

# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72196.sa1](https://doi.org/10.7554/eLife.72196.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Learning to predict target location with turbulent odor plumes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) It would be good if the authors could provide evidence that their conclusions do not depend on the precise location of the odor source relative to the cylinder. We do not require an exhaustive study, but some evidence would be very helpful.

2) We think that more could have been understood from these data, had the authors tried to focus on dimensionless quantities. It would be important to understand what sets the distance from the source where the intensity-based search strategy becomes less effective than the time-based one, and how the results depend on the Schmidt number.

3) The authors should carefully specify how dimensionless parameters are introduced. They do it in places but not systematically. For instance, how are wavenumbers in Figure 1(d) are made dimensionless?

4) On a similar note, how does the range of k's in Figure 1(d) compare to the height of the channel? Are these k's taken along the streamwise direction only? What is the vertical axis in that graph? Would it integral over all k's correspond to the odour density variance? These need to be specified.

5) What is the value of odour diffusivity \kapppa_\theta? What is the Schmidt number in these simulations? Visual inspection of Figure 1(d) suggests that Sc>>1, which might explain why the -5/3 slope is so far from representing the data. A reference to passive scalar advection by turbulence is in order here. We would suggest K. Sreenivasan, Turbulent mixing: A perspective, PNAS (2019).

6) Perhaps T in line 335 should be replaced by \theta.

7) Please provide figure numbers in lines 377, 412, and 414.Reviewer #1 (Recommendations for the authors):

In this work, the authors combine high resolution numerical simulations of turbulent airflow that advects a passive scalar (an "odor") and machine learning algorithms to investigate the question of how a navigation strategy based on the temporal dynamics of odor detection compares with one based on the intensity of the plume. In the simulations, the odor is introduced downstream of a cylinder that induces turbulence in the flow and the machine learning algorithm is trained and evaluated at various points further downstream. The authors conclude that intensity/gradient based measurements work closer to the source, while temporal schemes are good throughout the range. The study is done to a very high standard and presented clearly, although there are general questions about the data analysis (see below) that should be improved. That said, the work should have significant impact on a broad range of fields, from sensing to navigation, across a range of organism length scales.

One concern is the nature of the turbulent profile and its advection of the passive scalar. It would help if the characteristic dimensionless numbers of the problem were specified (Peclet, Schmidt numbers), and it was made clear how the choice of odor release point affects the conclusions. The turbulence itself spreads and diffuses with distance from the source, and one would presume the location of the odor release can matter substantially.

Also, as mentioned briefly in the Discussion, this work examines algorithms based on evaluating accuracy of prediction at a given measurement point. Unless I have missed something in the presentation, the issue of navigation is left unexamined. As in bacterial chemotaxis or any related problem, no navigation strategy is perfect, especially in the face of such a fluctuating source of information, so the full problem involves making estimates of where the source is and then moving to a new location, estimating again, moving, etc. The authors should clarify under what circumstances an evaluation at a fixed point is sufficiently predictive of "learning".Reviewer #2 (Recommendations for the authors):

In their manuscript, Rigolli et al., studied how measurements of intensity of a passive scalar (odour), its spatial gradients, and its time variations can be used to efficiently find the spatial location of its source. To this end, the authors performed direct numerical simulations of high-Reynolds number pressure-driven channel flow, partially blocked by a cylinder to generate turbulent velocity fluctuations. At a fixed position downstream the cylinder, they introduce a source of odour that diffuses through the fluid and is advected by its turbulent motion. The authors then trained a supervised machine learning algorithm on a collection of spatial and temporal odour profiles thus obtained. The algorithm was subsequently tested on various odour signals originating from the same pool of simulations. By varying the spatial position of the measurement point and the temporal exposure, the authors concluded that detection strategies based on the odour concentration and its spatial gradient work best at small separations from the source (and also close to the zero-odour concentration boundaries), while time-based strategies work reasonably well everywhere within the domain selected for detection.

Within the geometry set by the authors, the conclusions of the paper are supported by data. However, this setup leads to a natural question whether the search strategies determined here pertain to the distance to the odour source or to the distance to the turbulence source (the half-cylinder). Turbulence generated by an obstacle has a particular spatial profile; its temporal profile also depends on the distance to the obstacle. It is therefore possible that the machine learning algorithm has indirectly picked up these features rather than the odour profile itself. This can be settled by feeding the existing algorithm signals from simulations with various distances between the source and the obstacle. In the absence of this check, it is impossible to make general statements about applicability of these search strategies in other situations.

Another weak point of this study is the use of a cone of detection as it dramatically reduces the search complexity to almost a quasi one-dimensional problem. The authors appreciate it and point out that their choice is forced by a very limited by a very small number of detections outside the cone. This shortcoming should be addressed in future work.
