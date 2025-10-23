# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- Roderick MacKinnon, Howard Hughes Medical Institute, The Rockefeller University United States
- Sergei Sukharev, University of Maryland, College Park United States

## Review text

DOI: [10.7554/eLife.50486.sa1](https://doi.org/10.7554/eLife.50486.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The ion channel MscS has been an important model system to study the physical principles that explain molecular mechanosensation – which remain to be completely understood. In this article, Perozo and co-workers report single-particle cryo-EM structures of the MscS in lipid nanodiscs. These structures reveal the position of the channel relative to the membrane, which had been previously misjudged based on then-available structures. Specifically, the new data shows the transmembrane region is shifted by ~14 Å, taking TM3a and much of TM2 out of the membrane, and placing more of TM1 inside the membrane. These insights are consistent with free-energy calculations based on MD simulations. The structures also reveal the fold of a previously unrecognized 'anchor domain' at the N-terminus (of TM1), as well as ordered lipid molecules seemingly bound along the periphery of the channel as well as inside the pore. These are important insights that will no doubt serve as the foundation for future studies of the mechanism of gating of MscS and related mechanosensitive channels.

Decision letter after peer review:

Thank you for submitting your article "Molecular basis of force-from-lipidsgating in the mechanosensitive channel MscS" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by José D. Faraldo-Gomez as the Reviewing Editor andRichard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Roderick MacKinnon (Reviewer #2); Sergei Sukharev (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers find that the central conclusions of the article are "well supported" and "convincing". By contrast, the computational examination of the mechanism of channel opening, and of the role that the bound lipids might play in this process, was perceived as too preliminary and inconclusive.

Essential revisions:

1) The reviewers agree that the computational section that examines the gating mechanism of the channel in response to a bilayer expansion and the potential role that bound lipids might have in this process is too preliminary and incomplete for publication in eLife. The reviewers are skeptical that these challenging questions can be addressed convincingly within the limited timeframe permitted to make revisions (2 months). Thus, we very strongly recommend that this element be removed from the article. The reviewers agree that this change will not diminish the value of the study, but rather the opposite. The authors are however encouraged to pursue this kind of studies in the future; some of the reviewers' comments are therefore provided below, as they might be useful to the authors:

– As the data stands, it is concerning that the process induced is clearly far from equilibrium, as a very large perturbation in membrane morphology is created in a very short time. To establish statistical significance on the basis of this kind of data, the authors ought to carry out and analyze a large number of repeats; alternatively, the authors could change their simulation protocol so that the system remains close to equilibrium throughout the perturbation of the membrane.

– The surface tension of the simulated membrane was increased from 50 mN/m at rest to 150 mN/m. The authors state that this is several times larger than the experimental value so that the opening can be observed in shorter times. But the lytic tension of ordinary lipid membranes is 10-15 mN/m, which means the tension in the simulation goes from about 5 times lytic to about 15 times lytic. What happens to the bilayer in the simulation? These simulated tensions deserve some careful thought, consideration and explanation for the reader.

– Forcing MscS opening by applying 150 mN/m of tension within 10 ns is a regime that imposes unnatural force and time scales on the transition. The bilayer gets much thinner than can be expected under MscS gating tension; hence the lipid-derived forces are acting at very different z levels. The bilayer thins so much that in videos it looks like the outer monolayer reaches the level of the "anchor" lipids that used to be close to the midplane. Also, why so much (50 mN/m) tension at rest? POPE seems to be pretty well parameterized in the latest release of CHARMM. Did the bilayer over-compact too much at zero tension or was the structure collapsing as in some previous simulations? This should be explained.

– The putative role of R88-associated lipids seems important and warrants a much more thorough MD study that would require several repetitions of channel opening under 'slow' regimes closer to equilibrium. Regarding ways to illustrate the conclusions, either cartoons should be presented (Figure 6B) or a real and convincing MD trajectory, not both. We suggest that in the next paper the authors devote special effort to the MD part which appears unfinished in the present form.

– The simulations do not seem to clearly reveal the role that either the 'hook lipids' or the 'pore lipids' might play in the mechanism of gating, or indeed whether they do play a role. For example, the authors propose that the pore lipids are a feature of the closed state, and that they must return the membrane upon channel opening. Simulations could in principle be used to evaluate the plausibility of this hypothesis, but the trajectories discussed in the manuscript are much too short to explore the dynamics of these lipids in a meaningful way. Similarly, much longer simulations (or simulations based on enhanced-sampling techniques) could be used to ascertain whether the sites occupied by lipid molecules in the cryo-EM structure indeed remain occupied in this closed state, as hypothesized, and to evaluate how this occupancy might depend on the membrane surface tension. In summary, this element of the study is promising but as it stands, it also appears inconclusive and not ready for publication.

2) The hypothesis that lipids are naturally present inside the pore in the resting state and move out during gating seems to be far-fetched. The lipid action in K2P channels, for instance, appears to be feasible due to clear fenestrations in the channel wall; similarly, a possible action of the 'hook' lipids here in MscS can be envisioned because there is an exchange path with the lipid bilayer. There is no obvious path that would connect the pore lipids with the bilayer. In this case, the detachment from the hydrophobic wall would imply a complete solvation by water, which would be energetically costly and slow. Because the headgroups of these lipids have not been resolved in any of the structures, would it be possible that these densities are fatty acids that came as products of lipid degradation? Fatty acid exchange is much more feasible due to higher solubility.

Given these concerns, we strongly recommend that the authors tone down their conclusions in regard to the observation of 'pore lipids' and that they discuss other plausible interpretations of the density signals. Otherwise, the authors are asked to provide an additional WT MscS structure obtained with a deliberate attempt to remove or minimize putative free-fatty acids, e.g. by incubating the nanodiscs with cyclodextrins or other type of fatty-acid absorbents. High-resolution structures might not be required to discern whether the densities inside the pore are still present or not.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting the revised version of your article "Molecular basis of force-from-lipids gating in the mechanosensitive channel MscS" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by José D. Faraldo-Gómez as the Reviewing Editor and Richard Aldrich as the Senior Editor. The following individuals involved in review of your resubmission have agreed to reveal their identity: Roderick MacKinnon (Reviewer #2); Sergei Sukharev (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers believe the most important issues addressed in the earlier evaluation have been addressed, and that the revised manuscript will be worthy of publication in eLife, pending the following revisions:

The quantity defined as DGc in paragraph three of subsection “Continuum-Mean filed calculations of the free energy change” is not a free energy but a free-energy density, defined only locally at a point where the membrane curvature is C. The free energy that the authors seek should be an integral of this density over the area of membrane; the resulting values will be therefore considerably larger than the values currently plotted in Figure 3—figure supplement 3D. In addition, although it is valid as a first approximation to assume that at a given point (X, Y) the curvature C is same in the both directions, C(X,Y) cannot be assumed to be constant everywhere – i.e. the value of the abovementioned integral must be finite. Thus, the statement that "Although the contribution of curvature in our PMF calculations are minimal compared to the effect of hydrophobic mismatch" is not evident based on the data provided.
