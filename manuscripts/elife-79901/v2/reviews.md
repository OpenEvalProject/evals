# Peer review - Round 1

Editors:
- Naama Barkai, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79901.sa0](https://doi.org/10.7554/eLife.79901.sa0)

This manuscript will be of interest to readers in the field of physical biology and molecular biology for understanding genome organization. The idea of this computational study and its outcomes suggest a novel phase-separated structure and will shed new light on the role of enzymatic activity in chromatin organization. Overall, modeling and simulation are properly performed and analyzed, and the data support the key claims of the manuscript.


---

# Peer review - Round 1

Editors:
- Naama Barkai, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79901.sa1](https://doi.org/10.7554/eLife.79901.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "How enzymatic activity is involved in chromatin organization" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers appreciated the significance of your findings. In particular, the suggested role of topoisomerase activity is very original and the wall structure found is very interesting and novel. Please note, however, the comments below and address them.

Reviewer #1 (Recommendations for the authors):

The role of topoisomerase II activity in the spatial organization of chromatin is poorly understood. Typically it is suggested that topoisomerase is required to prevent entanglement of DNA during replication. In the present paper the authors propose a novel idea: That topoisomerase activity in euchromatin would trigger micro phase separation of chromatin in hetero- and euchromatin and could thus play a key role for the spatial organization of chromatin. This is a compelling idea that the authors test using a coarse-grained polymer model of chromatin. Interestingly, in the simulations micro phase separation is observed that is different from equilibrium phase separation in that it generates wall like structures of the phase in which topoisomerase activity is simulated. The model used is simple and elegant, the results interesting and stimulating. However key aspects of the model remain quite unclear.

Key to the work is the coarse-grained polymer model including topoisomerase activity. When reading the paper the description of the model seems incomplete in the main text and somewhat clumsy in the methods part. The model should be more precisely defined so that the model choices are clear and work could be repeated.

– A major point of criticism is that key aspects of the model to describe the topisomerase activity are not properly explained and the model therefore remains unclear. It is not clear how Brownian dynamics is combined with the stochastic transitions at rates λan and λnr and λra in the simulation. Furthermore the rates λan, λnr and λra are unclear. These rates refer to pairs of beads but it is not explained which pairs of beads are are selected and how. Can these rates be related to the concentration of topoisomerase molecules? Should these not be rates per volume rather than rates?

– The Brownian dynamics is explained in the methods section but as a list of bullet points on p. 14 and 15. Here the model definition and some parameter values are mixed together and some points are rather unclear. Parameter values should be summarized in a table and the contributions to the potential H should be written as equations to improve clarity.

– It seems plausible that the rates λan, λnr and λra can describe the effects of topoisomerase activity as they allow chromatin strands pass each other. However transiently switching off steric repulsion of coarse grained beads has other effects that one may not associate with topoisomerase action. For example transiently removing steric repulsion will affect osmotic compressibility which could also contribute to micro phase separation. It is not clear to what degree the genuine effects associated with topoisomerase activity and other effects that are introduced by the model but could be seen as artefacts contribute relatively to the micro phase separation. In that context there is a short sentence about effects from attraction due to topoisomerase activity: (l. 166) "the possibility … was ruled out". It is unclear to me how this can be "ruled out" and to me this sentence sounds too strong and not clear. A more careful discussion would help clarify these points.

– I am somewhat puzzled by the HC affinity potential described in line 389. It vanishes for r=0 and for large r, so I cannot see that it describes an affinity. What is the physical meaning of epsilonHC and why this choice of potential? In contrast the attractive potential due to enzyme activity is clearly an attractive potential. Why the different choices of potential?

– The quantification of nematic bond order to demonstrate the wall-like nature of microphases is very interesting. However only the nematic order of A-A bonds is discussed. It would be good to show that the B-B bonds do not exhibit similar nematic order.

Reviewer #2 (Recommendations for the authors):

This computational work provides a new role of enzymatic activity in chromatin organization, especially Topoisomerase-II (Topo-II). The authors newly introduced a catch-and-release mechanism among euchromatin regions mimicking Topo-II activity and performed simulations of the polymer model. They show that the enzymatic activity promotes the microphase separation of the chromatin model. The model configurations seem consistent with the experimentally observed distribution of euchromatin and heterochromatin. Besides, they provide a theoretical framework for understanding the physical origin of the microphase separation using a simplified mean-field model. The mean-field calculation explains an effective attraction among heterochromatin due to the phantom and self-avoiding contributions, promoting a phase separation. The simulated configurations reveal a characteristic structure called wall-like organization of euchromatin components, which the mean-field framework cannot explain. These data suggest a possibility of forming a wall-like microphase separation in the cell nucleus by enzymatic activity.

1) As polymer modeling approaches have revealed a phase-separated organization such as A/B compartments in the cell nucleus, the existence or assumption of the two type interactions on the active/inactive genomic regions should be a critical factor. This work assumes the catch-and-release mechanism among AA pairs and the attractive interaction among BB pairs. Therefore, the microphase separation would be predictable. However, the wall-like organization is not trivial and might become a universal phase-separated structure in a micro-scale. The outer walls in Figures 1d and 2b seem to be spherical and can be an effect of the spherical boundary condition. The authors do not address the possibility.

2) The reason why the authors change the volume fraction of A and fix the heterochromatin affinity as ε=4 in Figure 3 would be needed to clarify motivation in section "Wall-like organization of EC due to Topo-II."

3) Figure 3a shows the conversion of the A/B compartment configuration due to the enzymatic activity. Then, the authors characterize the wall-like organization of euchromatin by the local nematic order in Figure 3c. How about the local nematic order of BB bonds? The difference would strengthen the wall feature of A compartment regions.
