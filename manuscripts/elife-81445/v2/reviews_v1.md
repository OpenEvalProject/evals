# Peer review - Round 1

Editors:
- Toby W Allen, https://ror.org/04ttjf776 RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81445.sa0](https://doi.org/10.7554/eLife.81445.sa0)

The manuscript reports a new structure of the small conductance mechanosensitive channel MscS from E. coli in the open state, together with coarse-grained and atomistic molecular dynamics simulations of MscS and the related channel MSL1 of plant mitochondria in closed and open states. The important finding is that the surrounding lipid bilayer is severely distorted in the closed state only, with the protein inducing high curvature in the inner leaflet due to the membrane protruding into the cytoplasm. The authors argue convincingly that the role of membrane tension is to increase the energy of the protein-membrane system in this closed state compared to the relatively flat-membrane open state, in contrast to the previous proposal that tension-induced gating is driven by expansion of the in-plane area of the protein. The finding may be relevant for the understanding of ion channel mechano-sensation more generally, including of the PIEZO1 channel.


---

# Peer review - Round 1

Editors:
- Toby W Allen, https://ror.org/04ttjf776 RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81445.sa1](https://doi.org/10.7554/eLife.81445.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "State-specific morphological deformations of the lipid bilayer explain mechanosensitive gating of MscS ion channels" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gerhard Hummer (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Relaxation in simulations and the effect of restraints: It is important to allay any concern that the severe membrane distortion in the closed state may be due to lack of relaxation of the model or due to the restraints used. Please continue at least one all-atom simulation without any restraints in a tension-free membrane to demonstrate the structure is stable. This should include at least one new simulation of at least a few hundred nanoseconds.

2. Dependence on starting configuration: Please clarify the extent to which the membrane distortion was already formed before all-atom MD. You may consider adding an all-atom simulation starting with a flat membrane, although this is optional.

3. Lipid composition and relevance to physiology: It is important to be sure that the simulations represent the physiologically relevant case representative of that in E. coli. In particular, there could be an important role for PE lipids. Please explain why simulations without PE lipids are relevant. Running an additional simulation with PE lipids could be considered, but convincing arguments would suffice.

4. Description of lipid interactions: Please include a figure showing how hook lipids in MD compare to the cryo-EM density for the open state (if they exist). Please offer improved views of the chemistry of the sites and how these residues move when the channel gates. Are other lipids seen in a nearby cavity (as reported in structures in past work – see reviewer query) and do they change upon channel opening? Please discuss any interactions between the headgroups of distorted lipids with charged amino acids. Provide an improved description of the data in Figure 6, including the position of Ile150 and lipids in proximity to this residue. Please also better explain the difference in the maximum possible fold-change in unique lipids and the comparison of AA and CG results, as explained in a reviewer query.

5. Structure and thickness changes: Please better describe measurements and visualise changes in protein and membrane thickness between the states, as requested by a reviewer.

6. Past studies: Please discuss results in the context of previous mechanical/continuum models of the membrane and contrast to the proposed model. Comment on past studies that might have seen closed-state membrane deformations, including MD simulations of 6PWN of MscL. For MSL1, how does the previously reported movement of TM2-3 impact lipid organisation?

Reviewer #1 (Recommendations for the authors):

– Figure 1A. in the panel showing a single protomer, it would be helpful to highlight where the pore is relative to the various TMs. Alternatively, choosing a colored subunit in the same orientation as in the left panel of Figure 1A might help a reader better visualize the orientation.

– Please add a caption to Figure 4 indicating the inner and outer leaflets. The main text states that the deformation is more pronounced for the inner leaflet, whereas the protrusions are topologically continuous to what could be construed be the outer leaflet. I realize that prokaryotic and eukaryotic conventions are opposite, but it is still confusing.

– Given that the functionally relevant changes in the pore happen because of a rearrangement in TM3, could the authors add a panel similar to those shown in Figure 3A-B for TM1 and 2 for the TM3? This would allow a rationalization of the observed pore-widening.

Reviewer #2 (Recommendations for the authors):

The manuscript by Park et al. reports a new structure of the mechanosensitive channel MscS of E. coli in the open state and the results of extensive coarse grained and atomistic molecular dynamics (MD) simulations of MscS and the related channel MSL1 of plant mitochondria in presumed closed and open states. The major new finding is that in the closed state, the lipid bilayer contacting the channel is severely distorted. In the open state, this distortion is not present. The MD simulations forming the basis of this finding have been carefully executed and the finding is interesting and relevant for the understanding of channel mechanosensation (with a membrane distortion reported also for PIEZO1). Therefore the study certainly meets the standards for publication in eLife in terms of relevance. However, a number of issues should be addressed.

1) Stability of the channel structures. The atomistic simulations used weak restraints on all phi and psi backbone dihedral angles of the protein. As I understand, the idea here is to ensure that the experimental structure is preserved during the long simulations. However, in my opinion this raises a concern, namely that the structures are not inherently stable. I realize that this can be a result of force field issues, but with current force fields such instabilities can also point to other issues. It would in my view by critical to establish that the closed-state structure of MscS, with its highly distorted membrane, is stable in the absence of membrane tension also without stabilizing backbone restraints, e.g., by continuing one of the atomistic simulations without restraints for about 1 microsecond. Otherwise, doubts might linger whether the main finding is the consequence of a structure that is in one way or another atypical and that the effect would go away with maybe only a small relaxation of the structure.

2) Lipid composition. Eight of the 11 simulations were conducted with membranes of pure POPC, one with a mixture of POPC:POPG and two with pure DMPC. According to the numbers in the manuscript, the native membrane of E. coli is 75% PE, 20% PG and 5% CL -- so no PC. I appreciate the fact that the structure 6PWN was determined in PC:PG nanodiscs. Nevertheless, I urge the authors to perform control simulations also for a membrane containing PE lipids. Otherwise, doubts might linger whether the main finding is the consequence of a lipid composition that is not reflective of the bacterial membrane and thus not relevant physiologically.

Reviewer #3 (Recommendations for the authors):

– Would the authors discuss their idea of the energy competition terms in the context of previous mechanical models of the membrane? For instance, did Rob Philips ever make an MscS-inspired model, or just the MsCl-like model from his PNAS paper with Paul Wiggins? I know it is a different protein, I just looked over that paper, and they seemed to imply that the protein energy is the same in the closed and fully open states with steric barriers in between (including a subconducting state), that is totally different than is what is suggested here. All of that said, the authors nicely lay out how they think the protein works, I think the "membrane deformation model" fits a little into these mathematical models, but those mathematical models might have key ideas all backwards. Can you go into it, or are the math models not relevant to MscS? The authors do set up this idea with the "Jack-in-the-box" model, and they nicely show that it is wrong given their current work. I would just like a little more discussion of other continuum membrane models applied to membrane proteins out there in the literature (e.g. Andersen, Huang, Oster, Pincus, etc) , again, if appropriate.

I especially do not understand how your current model applied to PIEZO is different from more classical ideas of membrane mechanics that come from continuum approaches. I agree that specific lipid binding sites are important and continuum can't easily give you that insight; however, lipid-protein interactions are included abstractly through the boundary conditions. Regardless, the large scale structure and energy of the membrane might be described quite well by even simple continuum membrane models such as the one developed by Haselwandter and MacKinnon.

– I would like to see a close-up view of the chemistry of the sites in the closed channel that draw the inner lipids down from the bulk bilayer. I would then like to see where these key residues on the protein move when the channel opens. It could be an inset to Figure 5 and/or Figure 7.

– Were the AA simulations started from CG? The authors state, "The AA trajectories were initiated in a representative configuration of a CG trajectory obtained under the same condition, and lasted 10 μs each." It would be good to know if an AA simulation starting with a flat membrane eventually results in the kinds of deformed membranes like those shown in Figure 4.

– I find it fascinating that the inner leaflet lipids contacting the protein in the closed state exchange readily with the bulk.
