# Peer review - Round 1

Editors:
- Fabrizio Marinelli, Medical College of Wisconsin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105138.3.sa0](https://doi.org/10.7554/eLife.105138.3.sa0)

This work represents an important contribution to our understanding of how membrane energetics influence protein conformation and function in mechano-sensitive channels. Through extensive molecular dynamics simulations and energetic analysis, the study convincingly demonstrates how the channel structure is shaped by a balance of protein and membrane-induced forces, effectively reconciling experimental data from different membrane environments. This work will appeal broadly to researchers and readers with interests in ion channel structure and function, mechanosensation, and membrane biophysics.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105138.3.sa1](https://doi.org/10.7554/eLife.105138.3.sa1)

Dixit, Noe, and Weikl apply coarse-grained and all-atom molecular dynamics to determine the response of the mechanosensitive proteins Piezo 1 and Piezo 2 proteins to tension. Cryo-EM structures in micelles show a high curvature of the protein whereas structures in lipid bilayers show lower curvature. Is the zero-stress state of the protein closer to the micelle structure or the bilayer structure? Moreover, while the tension sensitivity of channel function can be inferred from experiment, molecular details are not clearly available. How much does the protein's height and effective area change in response to tension? With these in hand, a quantitative model of its function follows that can be related to the properties of the membrane and the effect of external forces.

Simulations indicate that in a bilayer the protein relaxes from the highly curved cryo-EM dome (Figure 1).

Under applied tension the dome flattens (Figure 2) including the underlying lipid bilayer. The shape of the system is a combination of the membrane mechanical and protein conformational energies (Eq. 1). The membrane mechanical energy is well-characterized. It requires only the curvature and bending modulus as inputs. They determine membrane curvature and the local area metric (Eq. 4) by averaging the height on a grid and computing second derivatives (Eqs. 7, 8) consistent with known differential geometric formulas.

While I am still critical generally of a precise estimate of the energy from simulated membrane shapes (after all it is not trivial to precisely determine even the bending modulus from a simulation), I believe with their revision the authors have convinced me that their estimate is a high quality one, without obvious issues. Although there appears to have been a miscommunication about increasing the density of grain or lowering the density of grain, the authors have tried two grains and determined a similar deformation energy, which addresses my concern. Furthermore, they have computed a dramatically reduced simplification of the curve and determined a similar value.

In summary, this paper uses molecular dynamics simulations to quantify the force of the Piezo 1 and Piezo 2 proteins on a lipid bilayer using simulations under controlled tension, observing the membrane deformation, and using that data to infer protein mechanics. While much of the physical mechanism was previously known, the study itself is a valuable quantification.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105138.3.sa2](https://doi.org/10.7554/eLife.105138.3.sa2)

Summary:

In this study the authors suggest that the structure of Piezo2 in a tensionless simulation is flatter compared to the electron microscopy structure. This is an interesting observation and highlights the fact that the membrane environment is important for Piezo2 curvature. Additionally, the authors calculate the excess area of Piezo2 and Piezo1, suggesting that it is significantly smaller compared the area calculated using the EM structure or simulations with restrained Piezo2. Finally, the authors propose an elastic model for Piezo proteins. Those are very important findings, which would be of interest to the mechanobiology field.

Whilst I like the suggestion that the membrane environment will change Piezo2 flatness, could this be happening because of the lower resolution of the MARTINI simulations? In other words, would it be possible that MARTINI is not able to model such curvature due to its lower resolution?

Related to my comment above, the authors say that they only restrained the secondary structure using an elastic network model. Whilst I understand why they did this, Piezo proteins are relatively large. How can the authors know that this type of elastic network model restrains, combined with the fact that MARTINI simulations are perhaps not very accurate in predicting protein conformations, can accurately represent the changes that happen within Piezo channel during membrane tension?

Modelling or Piezo1, seems to be based on homology to Piezo2. However, the authors need to further evaluate their model, e.g. how it compares with an Alphafold model.

To calculate the tension induce flattening of Piezo channel, the authors "divide all simulation trajectories into 5 equal intervals and determine the nanodome shape in each interval by averaging over the conformations of all independent simulation runs in this interval.". However, probably the change in the flattening of Piezo channel happens very quickly during the simulations, possibly within the same interval. Is this the case? and if yes does this affects their calculations?

Finally, the authors use a specific lipid composition, which is asymmetric. Is it possible that the asymmetry of the membrane causes some of the changes in the curvature that they observe? Perhaps more controls, e.g. with a symmetric POPC bilayer is needed to identify whether membrane asymmetry plays a role in the membrane curvature they observe.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105138.3.sa3](https://doi.org/10.7554/eLife.105138.3.sa3)

Strengths:

This work focuses on a problem of deep significance: quantifying the structure-tension relationship and underlying mechanism for the mechanosensitive Piezo 1 and 2 channels. Such an objective is challenging for molecular dynamics simulations, due to the relatively large size of each membrane-protein system. Nonetheless, the approach chosen here is based on methodology that is, in principle, established and widely accessible. Therefore, another group of practitioners would likely be able to reproduce these findings with reasonable effort.

More specifically, while acknowledging the limitations of the MARTINI force field, this work makes a significant improvement compared to previous simulations of Piezo proteins by adopting a range of membrane tensions that includes physiologically relevant values (below 10 mN/m).

Weaknesses:

The two main results of this paper are (1) that both channels exhibit a flatter structure compared to cryo-EM measurements, and (2) their estimated force vs. displacement relationship. Although the former correlates at least quantitatively with prior experimental work, the latter relies exclusively on simulation results and model parameters.

My remaining technical concerns in the revised manuscript are as follows:

(1) At each membrane tension, all concurrent atomistic simulations were initialized from the same snapshot of a previous CG simulation: in my opinion, it is inaccurate to refer to those atomistic simulations as "independent" from each other (as is done twice in the caption of Figure 3, as well as in the text).

(2) Continuum mechanics calculations were employed to model the membrane's curvature energetics. The bending modulus, k, was not determined for the specific lipid composition used in this study, but was instead taken from previous MARTINI simulations involving the same primary lipid, POPC. Given that these calculations are intended to describe MARTINI simulations specifically, this approximation may be acceptable. However, it does not account for the increased stiffness observed in POPC/cholesterol mixtures-an effect measured experimentally but not reproduced by the MARTINI model-nor does it reflect the asymmetric conditions, as all referenced simulations involve symmetric bilayers. As a result, the bending energies and forces shown in Figure 5(c,d) are internally consistent within the model, but they probably correspond to real values up to an unknown multiplicative factor.
