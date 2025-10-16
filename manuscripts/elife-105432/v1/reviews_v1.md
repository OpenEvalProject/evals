# Peer review - Round 1

Editors:
- Lipi Thukral, CSIR-Institute of Genomics and Integrative Biology India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105432.3.sa0](https://doi.org/10.7554/eLife.105432.3.sa0)

This fundamental study characterizes the mechanics and stability of bolalipids from archaeal membranes using a minimalist, physics-based computational model. The authors present a robust mesoscale model of bolalipids-containing membranes, systematically evaluating it across diverse membrane configurations. The results are compelling, demonstrating that the incorporation of bolalipids and regular bilayer lipids in archaeal membranes significantly enhances membrane fluidity and structural stability.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105432.3.sa1](https://doi.org/10.7554/eLife.105432.3.sa1)

Summary:

The authors aimed to understand the biophysical properties of archeal membranes made of bolalipids. Bacterial and eukaryotic membranes are made of lipids that self-assemble into bilayers. Archea, instead, use bolalipids, lipids that have two headgroups and can span the entire bilayer. The authors wanted to determine if the unique characteristics of archaea, which are often extremophiles, are in part due to the fact that their membranes contain bolalipids.

The authors develop a minimal computational model to compare the biophysics of bilayers made of lipids, bolalipids, and mixtures of the two. Their model enables them to determine essential parameters such as bilayer phase diagrams, mechanical moduli, and the bilayer behavior upon cargo inclusion and remodeling.

The author demonstrates that bolalipid bilayers behave as binary mixtures, containing bolalipids organized either in a straight conformation, spanning the entire bilayer, or in a u-shaped one, confined to a single leaflet. This dynamic mixture allows bolalipid bilayers to be very sturdy but also provides remodeling. However, remodeling is energetically more expensive than with standard lipids. The authors speculate that this might be why lipids were more abundant in the evolutionary process.

Strengths:

This is a wonderful paper, a very fine piece of scholarship. It is interesting from the point of view of biology, biophysics, and material science. The authors mastered the modeling and analysis of these complex systems. The evidence for their findings is really strong and complete. The paper is written superbly, the language is precise and the reading experience very pleasant. The plots are very well-thought.

Weaknesses:

None. The authors have addressed all the potential weaknesses that were raised by the reviewers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105432.3.sa2](https://doi.org/10.7554/eLife.105432.3.sa2)

Summary:

The authors have studied the mechanics of bolalipid and archaeal mixed-lipid membranes via comprehensive molecular dynamics simulations. The Cooke-Deserno 3-bead-per-lipid model is extended to bolalipids with 6 bead. Phase diagrams, bending rigidity, mechanical stability of curved membranes, and cargo uptake are studied. Effects such as formation of U-shaped bolalipids, pore formation in highly curved regions, and changes in membrane rigidity are studied and discussed. The main aim has been to show how the mixture of bolalipids and regular bilayer lipids in archaeal membrane models enhances the fluidity and stability of these membranes.

The authors have presented a wide range of simulation results for different membrane conditions and conformations. Analyses and findings are presented clearly and concisely. Figures, supplementary information and movies are of very high quality and very well present what has been studied. The manuscript is well written and is easy to follow.

The authors have provided detailed response to the points I raised on the first version and have revised their manuscript accordingly. Hence, I only mention what, in my opinion, still deserves to be noted.

Comments:

I previously raised an issue with respect to the resort to the Hamm-Kozlov model for fitting the power spectrum of membrane undulations. The authors provided very nice arguments against my concerns. For the sake of completeness, I include a simple scenario, which will better highlight the issue:

The tilt contribution to the Helfrich Hamiltonian can be written as a quadratic term 1/2 k_t |T|^2, where T is a tilt vector field. This field is written as the difference between the surface normal and the director field aligned with the lipid orientations. In the small deviation Monge description with z=h(x, y) as the height function, the surface normal has the form N=(-dh/dx, -dh/dy, 1). Now assume the director field, n = (b_x, b_y, 1) with small b_x and b_y components. The tilt contribution to the energy thus reads as 1/2 k_t (N - n)^2 ~ = 1/2 k_t [|grad h|^2 + 2 b . grad h]. The first term, 1/2 k_t |grad h|^2, is indeed similar to a surface tension term, \sigma |grad h|^2 that you get from the (1 + 1/2 |grad h|^2) approximation to the area element. Therefore, if you only look at height fluctuations, while your membrane actually has some surface tension, it will make distinguishing the tilt contributions to the fluctuations in the linear Monge gauge impossible.

However, considering that the authors have made sure that the membrane is indeed tensionless, this argument is settled.

I had also raised an issue about the correct NpT sampling in the simulations, and I'm glad that the authors also set up more rigorously thermostatted/barostatted simulations to check the validity of their findings.

Also, from the SI, I previously noted that the authors had neglected the longest wavelength mode because it was not equilibrated. This was an important problem and the authors looked into it and ran more simulations that were better equilibrated.

The analysis of energy of U-shaped lipids with the linear model E=c_0 + c_1 * k_bola is indeed very interesting. I am glad that the authors have expanded this analysis and included mean energy measurements.
