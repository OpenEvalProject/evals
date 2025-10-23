# Peer review - Round 1

Editors:
- Bin Zhang, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95180.3.sa0](https://doi.org/10.7554/eLife.95180.3.sa0)

This study provides important biophysical insights into the molecular mechanism underlying the association of alpha-synuclein chains, which is essential for understanding the pathogenesis of Parkinson's disease. The data analysis is solid, and the methodology can help investigate other molecular processes involving intrinsically disordered proteins.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95180.3.sa1](https://doi.org/10.7554/eLife.95180.3.sa1)

Summary:

In this paper, the authors performed molecular dynamics (MD) simulations to investigate the molecular basis of association of alpha-synuclein chains under molecular crowding and salt conditions. Aggregation of alpha-synuclein is linked to the pathogenesis of Parkinson's disease, and the liquid-liquid phase separation (LLPS) is considered to play an important role in the nucleation step of the alpha-synuclein aggregation. This paper re-tuned the Martini3 coarse-grained force field parameters, which allows long-timescale MD simulations of intrinsically disordered proteins with explicit solvent under diverse environmental perturbation. Their MD simulations showed that alpha-synuclein does not have a high LLPS-forming propensity, but the molecular crowding and salt addition tend to enhance the tendency of droplet formation and therefore modulate the alpha-synuclein aggregation. The MD simulation results also revealed important intra and inter-molecule conformational features of the alpha-synuclein chains in the formed droplets and the key interactions responsible for the stability of the droplets. These MD simulation data add biophysical insights into the molecular mechanism underlying the association of alpha-synuclein chains, which may be useful for understanding the pathogenesis of Parkinson's disease.

Strengths:

(1) The re-parameterized Martini 3 coarse-grained force field enables the large-scale MD simulations of the intrinsically disordered proteins with explicit solvent, which will be useful for a more realistic description of the molecular basis of LLPS.

(2) This paper showed that the molecular crowding and salt contribute to the modulation of the LLPS through different means. The molecular crowding minimally affects surface tension, but adding salt increases surface tension. It is also interesting to show that the aggregation pathway involves the disruption of the intra-chain interactions arising from C-terminal regions, which potentially facilitates the formation of inter-chain interactions.

Weaknesses:

(1) Although the authors emphasized the advantage of the Martini3 force field for its explicit description of solvent, this paper did not analyze the water behavior contained in the simulation trajectories and discuss the water's role in the aggregation and LLPS.

(2) This paper discussed the effects of crowders and salt on the surface tension of the droplets. The calculation of the surface tension relies on the droplet shape. However, for the formed clusters in the MD simulations, the typical size is <10, which may be too small to rigorously define the droplet shape. As shown in previous work cited by this paper [Benayad et al., J. Chem. Theory Comput. 2021, 17, 525−537], the calculated surface tension becomes stable when the chain number is larger than 100.

(3) Both the sizes and volume fractions of the crowders can affect the protein association. It will be interesting to perform MD simulations by adding crowders with various sizes and volume fractions. In addition, in this work the crowders were modelled by fullerenes, which contribute to protein aggregation mainly by entropic means as discussed in the manuscript. It is not very clear how the crowder effect is sensitive to the chemical nature of the crowders (e.g., inert crowers with excluded volume effect or crowders with non-specific attractive interactions with proteins, etc).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95180.3.sa2](https://doi.org/10.7554/eLife.95180.3.sa2)

In the manuscript "Modulation of α-Synuclein Aggregation Amid Diverse Environmental Perturbation", Wasim et al describe coarse-grained molecular dynamics (cgMD) simulations of α-Synuclein (aSyn) at several concentrations and in the presence of molecular crowding agents or high salt. They begin by bench-marking their cgMD against all-atom simulations by Shaw. They then carry 2.4-4.3 µs cgMD simulations under the above-noted conditions and analyze the data in terms of protein structure, interaction network analysis, and extrapolated fluid mechanics properties. This is an interesting study because a molecular scale understanding of protein droplets is currently lacking.
