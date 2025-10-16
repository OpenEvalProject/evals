# Peer review - Round 1

Editors:
- Merritt Maduke, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105895.4.sa0](https://doi.org/10.7554/eLife.105895.4.sa0)

This valuable study addresses the structural basis of voltage-activation of BK channels using atomistic simulations of several microseconds, to assess conformational changes that underlie both voltage-sensing and gating of the pore. The findings, including movement of specific charged residues, combined with the degree to which these movements are coupled to pore movements, provide a solid basis for understanding voltage-gating mechanisms in this class of channels. This paper will likely be of interest to ion channel biologists and biophysicists focused on voltage-dependent channel gating mechanisms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105895.4.sa1](https://doi.org/10.7554/eLife.105895.4.sa1)

Summary:

This study provides new insight into the non-canonicial voltage-gating mechanism of BK channels through prolonged (10 us) MD simulations of the Slo1 transmembrane domain conformation and K+ conduction in response to high imposed voltages (300, 750 mV). The results support previous conclusions based on functional and structural data and MD simulations that the voltage-sensor domain (VSD) of Slo1 undergoes limited conformational changes compared to Kv channels, and predicts gating charge movement comparable in magnitude to experimental results. The gating charge calculations further indicate that R213 and R210 in S4 are the main contributors owing to their large side chain movements and the presence of a locally focused electric field, consistent with recent experimental and MD simulation results by Carrasquel-Ursulaez et al.,2022. Most interestingly, changes in pore conformation and K+ conduction driven by VSD activation are resolved, providing information regarding changes in VSD/pore interaction through S4/S5/S6 segments proposed to underly electromechanical coupling.

Strengths:

Include that the prolonged timescale and high voltage of the simulation allow apparent equilibration in the voltage-sensor domain (VSD) conformational changes and at least partial opening of the pore. The study extends the results of previous MD simulations of VSD activation by providing quantitative estimates of gating charge movement, showing how the electric field distribution across the VSD is altered in resting and activated states, and testing the hypothesis that R213 and R210 are the primary gating charges by steered MD simulations. The ability to estimate gating charge contributions of individual residues in the WT channel is useful as a comparison to experimental studies based on mutagenesis which have yielded conflicting results that could reflect perturbations in structure. Use of dynamic community analysis to identify coupling pathways and information flow for VSD-pore (electromechanical) coupling as well as analysis of state-dependent S4/S5/S6 interactions that could mediate coupling provide useful predictions extending beyond what has been experimentally tested.

Weaknesses:

Weaknesses include that a truncated channel (lacking the C-terminal gating ring) was used for simulations, which is known to have reduced single channel conductance and electromechanical coupling compared to the full-length channel. In addition, as VSD activation in BK channels is much faster than opening, the timescale of simulations was likely insufficient to achieve a fully open state as supported by differences in the degree of pore expansion in replicate simulations, which are also smaller than observed in Ca-bound open structures of the full-length channel. Taken together, these limitations suggest that inferences regarding coupling pathways and interactions in the fully open voltage-activated channel may be only partially supported and therefore incomplete. That said, adequate discussion regarding these limitations are provided together with dynamic community analysis based on the Ca-bound open structure. The latter supports the main conclusions based on simulations, while providing an indication of potential interaction differences between simulated and fully open conformations. Another limitation is that while the simulations convincingly demonstrate voltage-dependent channel opening as evidenced by pore expansion and conduction of K+ and water through the pore, single channel conductance is underestimated by at least an order of magnitude, as in previous studies of other K+ channels. These quantitative discrepancies suggest that MD simulations may not yet be sufficiently advanced to provide insight into mechanisms underlying the extraordinarily large conductance of BK channels.

Comments on revisions:

My previous questions and concerns have been adequately addressed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105895.4.sa2](https://doi.org/10.7554/eLife.105895.4.sa2)

Summary:

The manuscript by Jia and Chen addresses the structural basis of voltage-activation of BK channels using computational approaches. Although a number of experimental studies using gating current and patch-clamp recording have analyzed voltage-activation in terms of observed charge movements and the apparent energetic coupling between voltage-sensor movement and channel opening, the structural changes that underlie this phenomenon have been unclear. The present studies use a reduced molecular system comprising the transmembrane portion of the BK channel (i.e. the cytosolic domain was deleted), embedded in a POPC membrane, with either 0 or 750 mV applied across the membrane. This system enabled acquisition of long simulations of 10 microseconds, to permit tracking of conformational changes of the channel. The authors principal findings were that the side chains of R210 and R213 rapidly moved toward the extracellular side of the membrane (by 8 - 10 Å), with greater displacements than any of the other charged transmembrane residues. These movements appeared tightly coupled to movement of the pore-lining helix, pore hydration, and ion permeation. The authors estimate that R210 and R213 contribute 0.25 and 0.19 elementary charges per residue to the gating current, which is roughly consistent with estimates based on electrophysiological measurements that used the full-length channel.

Strengths:

The methodologies used in this work are sound, and these studies certainly contribute to our understanding of voltage-gating of BK channels. An intriguing observation is the strongly coupled movement of the S4, S5, and S6 helices that appear to underlie voltage-dependent opening. Based on Fig 2a-d, the substantial movements of the R210 and R213 side chains occur nearly simultaneously to the S6 movement (between 4 - 5 usec of simulation time). This seems to provide support for a "helix-packing" mechanism of voltage gating in the so-called "non-domain-swapped" voltage-gated K channels.

Weaknesses:

The main limitation is that these studies used a truncated version of the BK channel, and there are likely to be differences in VSD-pore coupling in the context of the full-length channels that will not be resolved in the present work. Nonetheless, the authors provide a strong rationale for their use of the truncated channel, and the results presented will provide a good starting point for future computational studies of this channel.
